# Phase P20 — Data Preservation, Portability, BYO Storage and Migration Safety

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (prefixed ULIDs, audit ledger with daily anchors, S3 SSE-KMS + versioning + Object Lock, expand-migrate-contract framework, Temporal), P02 (approvals, delegations), P03 (settings registry, `wf.items`, configuration bundle), P04 (Legal Vault/DMS: documents, versions, SHA-256 at ingest, folders as views, retention classes, legal hold), P19 core (connector framework, `int`, secrets vault for connector credentials), P05 (document classification — Wave 2 import assist), P08 (evidence packs and BSA s.63 certificate generator). Every module that persists records registers its record types in `xpt.export_map` before its own exit gate (NN-11) — enforced by the CI contract test built here.
> **Sequencing:** **Core (Wave 1, 2 sprints):** extend the P00 export-map registry head and its CI contract test (FR-P00-87; `NN-11_export_map_complete` and `ci/export-contract` are the same gate) in sprint 1, before P04 exits; `LD-EXPORT-1.0` builder for on-demand full and partial exports with download, folder/ZIP import with rule-based placement, golden archives. **Full (Wave 2, 4 sprints):** BYO storage targets and continuous mirror, scheduled exports, AI-assisted import classification, verifier and loader tools, exit/offboarding, region and vendor move runbooks, ecosystem archive sharing.
> **Binding IPB files *(v1.1)*:** IPB-01 §01.4.6 (database portability), §01.4.7 (object storage portability and Object Lock equivalents), §01.4.8–01.4.9 (containers, Helm, Terraform per cloud), §01.4.13 (cloud/vendor exit as a design property); IPB-09 §09.3.H (data-safety gates); IPB-07 node 12 (Storage & data). New FR-P20-52…55 extend §4H (renumbered at the 26 Oct 2026 independent review: 44…47 are the v1.0 exit, closure, retention and handover requirements in §4I); FR-P20-42's AWS-only runbook is kept and generalised.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), K (export package `LD-EXPORT-1.0` and folder taxonomy — binding for every folder, file name, format and manifest field), R (settings `xpt.*`), D (roles), F (eligibility — for evidence-pack contents), Y (Ecosystem Spec v1.2 change request: folder-profile registration and `portability` producer). **The Infrabyx Ecosystem Integration Specification v1.1 §12.1 (archive standard 1.0) and §12.2 (customer-controlled storage connector contract) prevail on conflict** (NN-24); `LD-EXPORT-1.0` is LawDocs' set of folder profiles within that standard.
> **Requirements covered:** R-021, R-022, R-024, R-068, R-011 (preserve), R-043 (selective export/sharing), R-053, R-055, R-023 (archive sharing across ecosystem apps), R-031 (DPDP portability and erasure), R-061, R-067 (audit trail export).
> **Decisions applied:** D-01, D-02, D-06, D-10, D-11 · **Challenges applied:** CH-15, CH-16, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-10, NN-11, NN-12, NN-13, NN-17, NN-18, NN-19, NN-24, NN-25, NN-26, NN-32, NN-42, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints (core 2 in Wave 1; full 4 in Wave 2), squad of 8 (portability core 3 backend, connectors 2, import 1, frontend 1, QA/verification 1).

---

## 1. Objective and business outcome

A LawDocs user must never feel trapped and must never lose a document. On any day — while subscribed, after cancelling, during a court case, when an auditor asks, or when a company switches tools — any individual or company can take **everything** as an ordinary folder tree of Word, Excel, PDF/A, CSV and original files, with self-explanatory folder and file names that a person can follow in Windows Explorer or macOS Finder without LawDocs. A company can keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, Google Drive, SFTP server, NAS or data centre). The same taxonomy works in reverse: a user drops an existing folder of 3,000 agreements and LawDocs files them, instead of the user uploading one by one (R-024).

Because folder paths are **views over permanent canonical IDs** and the export layout is a versioned contract rather than today's code, the owner can push patches, add features, change the database engine, swap storage vendor or move data centre without any customer re-filing or migrating data (R-021, R-022, NN-12).

| Outcome | Exit-gate measure |
|---|---|
| Everything exportable (NN-11) | Export-coverage test: every persisted record type maps to `xpt.export_map`; a seeded tenant with every record type exports with 100% count reconciliation per type and 100% of originals byte-identical (SHA-256) |
| Understandable without LawDocs | Usability test: 5 of 5 non-technical participants (a homeowner, an office manager, a junior lawyer, a startup founder, an external auditor) each find a named signed agreement with its stamp certificate and signing evidence, a court order, and the audit trail of a status change within 3 minutes using only Explorer/Finder and Office |
| Verifiable offline | Open-source verifier (Apache-2.0) confirms checksums, the detached JWS, control totals and audit-chain continuity; fails on one changed byte or one missing file |
| Stable across change (R-022) | Golden-archive test: the same synthetic tenants exported before and after (a) a release with schema changes, (b) a PostgreSQL major upgrade, (c) a storage-vendor swap, (d) a region-move rehearsal give identical paths, file names and IDs for unchanged records; differences only as additions declared in `CHANGES-SINCE-PREVIOUS.csv` |
| BYO storage (R-021) | A tenant connects S3, Azure Blob, SharePoint and SFTP targets; residency and canary pass; continuous mirror lag p95 ≤ 15 min; nightly reconciliation zero drift; restore test from the tenant's own copy passes |
| Bulk intake (R-024) | A 5,000-file folder imports with ≥ 90% automatic placement on a tidy tree (100% for a tree previously exported by LawDocs), duplicates linked by hash, every unplaced file in a correction queue before commit, nothing overwritten, full undo for 7 days |
| Exit without friction | Exit export of a 200 GB company completes in ≤ 24 h; read-only period; deletion certificate; never blocked by billing state |

---

## 2. Scope (in / out)

**In scope**

- `xpt` module: export map registry, export jobs and scopes, package builder, folder profiles, manifest, checksums and signing, verifier and loader, download service, scheduled exports, continuous mirror, BYO storage targets (`stg_`), import jobs (`imp_`), exit/offboarding workflow, deletion certificates, DPDP access and portability exports.
- `StorageTarget` adapters built on P19's connector framework, implementing Ecosystem Spec §12.2.
- Schema-evolution and infrastructure-move safety mechanisms that protect customer data and folder structure (CI gates, golden archives, archive versioning, move runbooks). Platform backups, PITR and DR of LawDocs' own estate are P23.

**Out of scope (owner phase)**

- Business retention rules per record type (owning modules + P04 retention engine); P20 enforces retention classes and legal holds on exports, targets and deletion.
- Co-authoring in Microsoft 365 or Google Workspace (P19 suite connectors); P20 uses the same connector credentials only for storage push.
- Ops Hub exit-project tracking (OH4 receives status and counts only, NN-19).
- Platform backup/restore and DR drills (P23).

---

## 3. Personas and permissions touched

Cerbos resources: `export_job` (`request`, `approve`, `download`), `storage_target` (`connect`, `approve`, `pause`, `disconnect`), `import_job` (`create`, `commit`, `undo`), `exit_request` (`request`, `approve`), `export_map` (`register` — CI/platform only).

| Role | P20 permissions |
|---|---|
| `IND_OWNER` | Full personal export any time with step-up only; connect personal OneDrive/Google Drive/S3/SFTP targets; import folders; close account with export first; set nominee/legacy release (P01/P04 policy) |
| `IND_FAMILY_MEMBER`, `IND_DELEGATE` | Export records they can read (RECORD, VIEW scopes); no full export of the owner's workspace |
| `IND_GUARDIAN` | Export a ward's records within guardianship scope |
| `IND_NOMINEE` | Export only after time-locked release is triggered and verified (P01) |
| `ORG_OWNER`, `ORG_ADMIN` | Request FULL_TENANT, ENTITY, YEAR, DEPARTMENT and EXIT exports (maker-checker, NN-18); connect storage targets; configure schedules and mirror; tenant-wide imports; folder-profile customisation within bounds |
| `ORG_CLO`, `ORG_DEPT_HEAD` | MATTER, AGREEMENT, DEPARTMENT (own), YEAR (own area) exports; imports into their areas; checker for tenant exports |
| `ORG_LEGAL_MAKER`, `ORG_CHECKER`, `ORG_MEMBER`, `ORG_DIRECTOR`, `ORG_KMP` | RECORD and VIEW exports of what they can see; "Download as folder" |
| `ORG_AUDITOR_RO`, `ORG_EXT_COUNSEL` | Watermarked, scoped exports under their grant (AUDIT_PACK, COURT_BUNDLE for a matter) |
| `ORG_DELEGATED_MAKER`, `OPS_RM`, `OPS_PROFESSIONAL` | Exports only inside a delivery grant scope that includes `xpt:export` (NN-17); never FULL_TENANT |
| `PRO_FIRM_ADMIN` | Practice workspace exports (own matters and engagements; client-owned material only with the client's grant) |
| `OPS_CONSUMER_CASE_MANAGER` | Consumer-case bundles for the user's own case at the user's request; never bulk exports of users |
| `PLT_SUPER_ADMIN` | Folder-profile versions (GOVERNED); break-glass export only on a court or statutory order with `PLT_SECURITY_OFFICER` + `PLT_DPO` approval, tenant notified unless legally barred; deletion certificates |
| `PLT_DPO` | Approves DSR access/portability exports for LawDocs-as-fiduciary data; approves cross-border target warnings policy |
| `PLT_SRE` | Job metadata and health only; no content |
| `AGT_*` | May **propose** an export or import as a draft request in the user's inbox; never starts, approves or receives a download link (NN-13, NN-43) |

---

## 4. Functional requirements

### 4A. Export package `LD-EXPORT-1.0`

**FR-P20-01 — Standard and profiles.** Every export is an archive under Ecosystem Spec §12.1 `archive_standard_version` 1.0 with one of four LawDocs folder profiles (full trees in Appendix K): `ld_company_v1` (Company workspace), `ld_individual_v1` (Personal workspace), `ld_professional_v1` (practice workspace of a professional or firm), `ld_consumer_help_v1` (Consumer Help brand cases). The profiles are registered with the ecosystem through Appendix Y before GA [OWNER: approve the Spec v1.2 change request].

**FR-P20-02 — Root and start files.** Root folder: `<Owner name> - LawDocs Archive - <Scope> - as of <YYYY-MM-DD>/` (Spec §12.1 pattern; ASCII hyphens). At the root, two beginner files sort first: `00 READ ME FIRST.pdf` (plain-language guide, one-page folder map, how to verify) and `00 Index.xlsx` (one row per record and per file with clickable relative hyperlinks, filters by year, type, department, counterparty, status). The mandatory `00 Start Here/` folder (identical in every profile, Spec §12.1) holds `README.pdf/.docx/.txt`, `export-manifest.csv`, `manifest.json`, `manifest.json.jws`, `data-dictionary.xlsx/.csv`, `relationships.csv`, `relationship-map.pdf`, `code-tables/`, `schemas/`, `verify/`, `Folder guide.xlsx`, `CHANGES-SINCE-PREVIOUS.csv` (for repeat and incremental exports) and `BSA Section 63 Certificate (draft).docx/.pdf` (NN-10). `checksums.sha256` also sits at the root so `sha256sum -c checksums.sha256` works from the root (X-07: Appendix K governs the layout, following Appendix Y §Y.11.2).

**FR-P20-03 — Top level (summary; Appendix K binding).** Company: `01 Company Profile`, `02 Agreements and Contracts`, `03 Litigation and Disputes`, `04 Trademarks and IP`, `05 Board and Governance`, `06 Policies and Registers`, `07 People and HR`, `08 Notices and Correspondence`, `09 Services and Engagements`, `10 Billing and Invoices`, `11 AI Work Products (labelled)`, `12 Tax` (X-12), `99 System Data (CSV and JSON)`. Individual: `01 My Profile and IDs (masked)`, `02 Property`, `03 Family and Succession`, `04 Employment`, `05 Finance, Loans and Insurance`, `06 Vehicles`, `07 Disputes and Court Cases`, `08 Agreements`, `09 Tax`, `10 Receipts and Invoices`, `11 AI Work Products (labelled)`, `99 System Data`. Professional and Consumer Help profiles: Appendix K §K.3.3–§K.3.4. Top-level numbers and names are LOCKED; tenants may rename or split below level 2 through a versioned folder policy (FR-P20-15).

**FR-P20-04 — Record folders.** An agreement exports as `02 Agreements and Contracts/<FY or Year>/<Department>/<Counterparty> - <Agreement title> (LD-AGR-2026-000123)/` with `01 Drafts`, `02 Negotiation and Redlines`, `03 Signed and Stamped`, `04 Evidence and Certificates`, `05 Amendments and Renewals`, `06 Correspondence`, plus `Agreement summary.pdf` (one page: parties, dates, value, status, formalities with status, renewal dates, obligations) and `Open and Waiting Items.xlsx` (P03). A court case exports as `03 Litigation and Disputes/<Year>/<Forum>/<Case title> (LD-CAS-…)/` with pleadings, orders, hearings, evidence (originals + type copies + translations, labelled — NN-09, NN-48), correspondence and a case summary. Single-entity tenants omit the entity level (`xpt.folder.entity_level = auto`).

**FR-P20-05 — Manifest and checksums.** `export-manifest.csv`: one row per file with Spec §12.1 columns (`path, sha256, bytes, media_type, record_count, legal_entity, dataset, schema_version, as_of, created_at, source_ids, restricted, retention_class, legal_hold, upsi`) plus LawDocs columns (`record_type, record_id, business_ref, canonical_path, department_id, year_label, module, version_label, status_canonical, is_original, derived_from, archive_part`). `manifest.json` adds `archive_id` (`exp_`-linked ULID), standard version, folder profile and version, producer release, tenant, scope, requester and approvers, `as_of` instant, control totals (counts per record type, documents count and bytes, signatures, stamp certificates, audit events and last chain anchor), `predecessor_archive_id`, pack-level SHA-256 over the sorted file list, signing key ID. `manifest.json.jws`: detached JWS (RFC 7515/7797, ES256 or EdDSA) with the tenant's export-signing key (public key in `verify/`, fingerprint in the README). `checksums.sha256` (root) uses the `sha256sum` format so `sha256sum -c` works directly.

**FR-P20-06 — Consistent snapshot.** The job snapshots at one instant (repeatable-read export transaction or replica at a recorded LSN + S3 version pinning), reconciles control totals to the live system at that instant, and fails without producing a signed package if any count differs. Large tenants export from a read replica at an agreed `as_of`.

**FR-P20-07 — What never appears.** Full Aadhaar numbers (only masked forms exist anywhere — NN-04), OTPs, DSC PINs, passwords, recovery codes and credential-vault secrets (the export lists only credential metadata: portal, owner, last rotated — NN-16), card data, other tenants' data, internal-only comments of a counterparty's side, LawDocs internal notes. A content scan on the assembled package checks Aadhaar patterns (Verhoeff-valid 12-digit numbers), PAN in paths, phone and email in paths, and fails the job on any hit outside permitted fields.

**FR-P20-08 — Restricted parts.** HR and payroll (`07 People and HR` restricted subfolders), privileged legal advice flagged by the tenant, health information in consumer cases, and any record flagged `restricted` are produced as separate AES-256 encrypted ZIP archives (or age/OpenPGP to a recipient public key) each with its own manifest; included only when the requester holds `export.restricted.<class>` and a second approver (`ORG_CLO` for privileged material, HR head for HR, plus the tenant's privacy contact) approves; passwords generated per archive and delivered out of band to the named recipient, never stored by LawDocs after delivery.

**FR-P20-09 — DigiLocker-pulled documents (NN-42).** Where a document came from DigiLocker and LawDocs kept only the URI and verification result, the export includes `DigiLocker references.xlsx` + `.csv` (document type, issuer, URI, verified at, result) in `01 My Profile and IDs (masked)/` or `01 Company Profile/` (P04) instead of a copy; a copy appears only where a recorded user purpose permitted retention [VERIFY with NeGD requester terms].

### 4B. Export scopes, triggers and approvals

**FR-P20-10 — Scopes.**

| Scope code | Contents | Who may request | Approval |
|---|---|---|---|
| `RECORD` | One record with children (agreement + versions + signatures + stamp + evidence + items + trail) | Anyone who can read it | None |
| `VIEW` | Records in a saved view or filter (≤ 10,000 records) | Anyone (own permissions) | None; above cap needs `ORG_DEPT_HEAD` |
| `USER` | Everything a user owns or created (e.g., a leaving employee hands over; an individual's family member) | The user; `ORG_ADMIN` for a departing member | Company: `ORG_ADMIN` + checker |
| `AGREEMENT_SET` | Agreements by counterparty, type, status or date range | `ORG_LEGAL_MAKER`+ | None for own; checker above 1,000 |
| `MATTER` / `CASE` | One matter or case with all linked records | Matter team | None |
| `COURT_BUNDLE` | Court-ready bundle: index, paginated PDF/A, originals, type copies, translations, s.63 certificate drafts | Matter team, `ORG_EXT_COUNSEL` under grant | Matter lead |
| `YEAR` | Everything for one FY (companies) or calendar year (individuals) | `ORG_ADMIN`, `ORG_CLO`; `IND_OWNER` | Company: maker-checker |
| `DEPARTMENT` | All records owned by a department | `ORG_DEPT_HEAD` | `ORG_ADMIN` |
| `ENTITY` | Everything for one legal entity | `ORG_ADMIN` | Maker-checker |
| `AUDIT_PACK` | Grant-scoped evidence and registers, watermarked | `ORG_AUDITOR_RO` under grant | Per grant |
| `DSR_ACCESS` / `DSR_PORTABILITY` | A data principal's personal data where LawDocs is fiduciary (DPDP ss.11–14; R3 LG-068) | `PLT_DPO` on a verified request | DPO |
| `FULL_TENANT` | Everything | `ORG_OWNER`/`ORG_ADMIN`; `IND_OWNER` | Company: step-up + second approver (NN-18); Individual: step-up only |
| `EXIT` | Full + exit artefacts (§4I) | As `FULL_TENANT` | As `FULL_TENANT` |
| `SCHEDULED_FULL` / `SCHEDULED_INCREMENTAL` / `MIRROR` | Copies to a BYO target | Configured by admin | Configuration approval only (target connection is GOVERNED for regulated data classes) |

**FR-P20-11 — Small companies.** Where a company has fewer than two users eligible to approve, a tenant export follows the P02 solo-owner rule (FR-P02-34, which governs): AAL2 step-up, notice to every contact point of the owner and of any other director on record, a cooling-off of `wf.mc.solo_owner.cooling_off_hours` (24 h) during which any of them can stop it, and a "solo approval" ledger mark. This keeps NN-11 (no staff help) and the spirit of NN-18.

**FR-P20-12 — Triggers.** On demand (screen action ≤ 2 clicks from any list or record); scheduled (RRULE: e.g., monthly full on the 1st at 02:00 IST, FY-full on 30 April); event-driven (e.g., "when an agreement reaches `EXECUTED`, push its folder to SharePoint"); on module detach; on exit; on a court or statutory order (break-glass).

**FR-P20-13 — Never blocked (NN-11; Spec §6.26–§6.27).** On-demand, scheduled, mirror and exit exports never depend on subscription, trial or dunning state. A tenant in restricted or termination-notice state keeps every export function; only capacity queuing applies.

**FR-P20-14 — Preview and dry run.** Before a large export the user sees the folder tree with counts and estimated size, items to be excluded or encrypted, and approvals required; a dry run produces the manifest and `Folder guide.xlsx` only.

### 4C. Folder taxonomy as views over canonical IDs (NN-12)

**FR-P20-15 — Export map registry.** `xpt.export_map` holds, per record type and folder-profile version: record type code, owning module, canonical path template (e.g., `02 Agreements and Contracts/{year_label}/{department_name@record_date}/{counterparty_label} - {title} ({business_ref})/`), file naming templates per artefact, dataset name and columns (JSON Pointer to the canonical model, data class, code table), attachment rules, restricted class, retention class, and the **path stability key** — the immutable fields that determine the path (record ID, business reference, record date), never mutable display fields alone. Display parts (department name, counterparty label, title) come from the value valid at the record's date by default (`xpt.folder.name_mode = historical`; option `current`); the manifest always carries IDs, so both views map. A change to an existing path template is a **major** profile change (GOVERNED, `PLT_SUPER_ADMIN` + `PLT_LEGAL_REVIEWER` for legal folders), with `legacy_path` carried for one major version.

**FR-P20-16 — Folder policy.** Tenants may, within Appendix K §K.8 bounds: choose year label (`FY 2026-27`, `FY26-27`, `CY 2026`), entity level (`auto`/`always`/`never`), department level on/off for agreements, split a folder below level 2 (e.g., by branch or contract type), choose person-naming mode (§FR-P20-17), choose README languages (English plus one of the D-07 languages as a labelled machine translation). Every folder-policy version is a ledger event; each export records the version used.

**FR-P20-17 — Naming rules (Appendix K §K.5 binding).** Plain English; numbered top-level folders; Windows/macOS/OneDrive/Google Drive-safe (no `\ / : * ? " < > |`, no leading/trailing space or dot, no reserved names `CON PRN AUX NUL COM1–9 LPT1–9`, no `.lock`, `desktop.ini`, `~$` prefixes); Unicode NFC; non-Latin titles transliterated for paths by default (`xpt.folder.path_script = latin`) with the original title in the index; total path ≤ 240 characters (shorten titles from the right, append ` - <short id>`); dates first for dated items (`2026-08-14 - Order - Interim stay`); version and status words in names (`v3 - SIGNED`, `v2 - DRAFT`) and parenthesised derived/AI labels after the source name (`(Type copy - <status>)`, `(Translation - English - Machine)`, `(AI draft - not reviewed)` — P04/P05/P09). **Person names:** organisations are always named; natural persons follow `xpt.naming.person_mode` — `full_name` (default for the Individual profile, which is the user's own archive), `masked_name` (first name + surname initial; default for Company and Professional), `ids_only` (default for Consumer Help). Aadhaar, PAN, phone numbers and email addresses never appear in any path (scanner enforced). These modes apply to archives delivered to the data owner itself (Appendix Y §Y.11.2 naming mode `owner_readable`); archives for third parties — auditors, court bundles, ecosystem shares — use `ids_only` or `id_and_masked_name` (Spec §12.1). Until Spec v1.2 accepts `owner_readable`, cross-product archives use `ids_only`.

**FR-P20-18 — Storage keys independent of paths.** Object keys are `t/{tenant_id}/o/{sha256[0:2]}/{sha256[2:4]}/{doc_id}/{ver_id}` with metadata `{record_type, record_id, doc_id, ver_id, sha256, media_type, created_at, data_class, retention_class, legal_hold}`; human paths are computed at export time from the export map and are never stored as object keys. Renaming a folder, department, module or code package never moves an object (P04, NN-09).

### 4D. Formats per record type (summary; Appendix K §K.4 binding)

**FR-P20-19 — Format matrix.**

| Content | Human files | Machine files |
|---|---|---|
| Registers and lists (agreements, obligations, matters, hearings, trademarks, items, users) | `.xlsx` (Read-me sheet, frozen header, filters, typed cells, leading zeros kept, column notes from dictionary) | `.csv` (RFC 4180, UTF-8 with BOM) + `.schema.json`; `.jsonl` in FULL/EXIT |
| Drafts and generated narratives | `.docx` (editable) + `.pdf` (PDF/A-2b, XMP with `document_id` and source hash) | — |
| Negotiation rounds | Each round `.docx` with tracked changes + redline `.pdf`; `Negotiation log.xlsx` (round, sender, date, accepted/rejected changes) — internal comments excluded from counterparty-shared copies (NN-37) | `.jsonl` |
| Originals and signed files | As stored, byte-identical (SHA-256 equals vault hash) | — |
| Signature evidence | `Evidence pack.pdf` (hashes, signer events, IP/device, timestamps, ESP/DSC certificate details, consent screen version) + provider response files as received | `signature-events.jsonl` |
| Stamp | eStamp certificate as issued + `Stamp details.pdf` (UIN, State, article, duty, verification result and hash link — NN-08) | `.json` |
| Type copies, OCR text, translations (`drv_`) | `.docx` + `.pdf` next to the original, labelled in the name; confidence summary | `.json` anchors |
| Court orders, cause lists, case status | As obtained + `Case status history.xlsx` with source and fetched-at (staleness shown) | `.csv` |
| Calendars | `.xlsx` list | `.ics` |
| Messages and deal-room chat | `Conversation – <thread>.pdf` transcript | `.jsonl` |
| Audit trail | `Audit trail <YYYY-MM>.xlsx` (who, what, when, before → after, reason, correction links) | `audit-events-YYYY-MM.jsonl` + chain anchors |
| Settings and customisations (P03) | `Settings and customisations.xlsx` | `ld-config-1.0.json` (signed) |
| Invoices and receipts (mirrors from OH8) | Tax invoice `.pdf` as issued | `.csv` |
| AI work products | `.docx` + `.pdf` with the AI label in the file and the name (`… (AI draft - not reviewed)`) and a sources sheet (NN-14) | `.json` (model, date, sources) |

**FR-P20-20 — Quality gates.** Every generated PDF validates as PDF/A-2b (veraPDF) and every Office file renders headless (LibreOffice) in CI and on a per-job sample; a failure stops the job with an actionable error (Spec §12.1).

**FR-P20-21 — Evidence admissibility (NN-10).** Each package and each `COURT_BUNDLE` includes a pre-filled BSA 2023 s.63(4) certificate draft (Part A for the party; Part B for the expert, as the Schedule requires) with hash values of `manifest.json` and the pack hash, and the **LawDocs Platform Statement** (hosting in India, controls, hashing at ingest, ledger, NTP time source; signed by LawDocs' designated officer with DSC) [VERIFY certificate wording against the official Schedule; [COUNSEL] to confirm who signs Part B for SaaS-held records]. The generator works per record too.

### 4E. Delivery

**FR-P20-22 — Download.** Resumable HTTPS download from the export page, split into parts (default 4 GB ZIP64 with a parts manifest) or one file for small packages; links valid 7 days (`xpt.download.link_validity_days`, 1–30), only for the requester after re-authentication; mobile shows size and recommends Wi-Fi; "Save to Files" (iOS) and Storage Access Framework (Android) for small packages.

**FR-P20-23 — Push to a connected target** (§4G) and **SFTP pull** from a per-tenant chroot for very large exports. LawDocs never ships disks; "external drive" means the user downloads to their drive or runs the on-premises agent with an attached disk as the target.

**FR-P20-24 — Progress and resumption.** Stages snapshot → collect → render → package → reconcile → sign → deliver with ETA; resumable after interruption without repeating completed stages; notification on completion; failure explains the next action.

### 4F. Bulk import from folders, ZIPs and drives (R-024)

**FR-P20-25 — Sources.** (a) Browser folder upload (drag a folder; directory upload) or a `.zip` (≤ 20 GB per job on web; mobile accepts files and ZIPs from Files/Drive); (b) a folder in a connected SharePoint/OneDrive library or Google Drive; (c) a watched folder on the on-premises agent (NAS, file server, attached drive); (d) an earlier `LD-EXPORT-1.0` package (round trip into the same or a new workspace); (e) another tool's export with a CSV index (mapping template).

**FR-P20-26 — Five steps (`ImportWorkflow`).**

1. **Scan:** inventory, SHA-256, malware scan, file-type sniffing (magic bytes), encrypted/password-protected detection, oversized/unsupported list, **duplicate detection** (same SHA-256 already in the workspace → link, never duplicate; same name different hash → version candidate). Aadhaar detection runs on any extracted text; derived text is masked before storage (NN-04); image originals with a visible Aadhaar number are flagged for the P04 redaction choice.
2. **Recognise structure:** an LD package (valid `manifest.json` + JWS) places exactly by `canonical_path`, `record_type` and IDs. Otherwise the mapper proposes rules from path segments (years and FY patterns `2025-26`, `FY26`, `FY 2025-2026`; department names and aliases; counterparty names matched to existing parties; document-type words — "Lease", "Rent", "NDA", "MoU", "Sale deed", "Affidavit", "Vakalatnama", "Order", "Notice", "Reply", "Invoice", "Policy"; court and case-number patterns such as CNR; trademark application numbers), file-name patterns (dates, `v2`, `signed`, `final`, `executed`, `stamp`), and the Appendix K reverse-mapping table (§K.10).
3. **Classify (AI-assisted, Wave 2):** `dix` classifies document type, parties, dates, value, jurisdiction, and whether a file is an original, a signed copy, a stamp certificate or a scan; each suggestion has a confidence and page anchors. Confidence ≥ 0.85 auto-proposed; 0.5–0.85 needs confirmation; < 0.5 goes to the correction queue (`xpt.import.confidence_auto`, `…_confirm`).
4. **Preview and correct before commit:** a table of every file with proposed destination (record type, record — existing or new, folder view, year, department, tags), confidence, conflicts and actions (accept, change destination, skip, create new agreement or case from a folder, merge into an existing record); bulk accept by rule; keyboard-accessible grid with screen-reader summaries ("312 files ready, 41 need your choice, 7 duplicates").
5. **Commit:** creates documents and versions; never overwrites (conflicts become new versions labelled `IMPORTED` with `source_created_at` from file metadata); creates records with `imported_historical = true` where the user chose to (e.g., a 2019 lease executed outside LawDocs, flagged so the timeline does not pretend it was signed here); writes an **import report** (`Import report – <date>.xlsx`: every file, destination, decision, hash, duplicate link, skipped reason) and a `wf.items` item `DMS_IMPORT_REVIEW` for anything unresolved.

**FR-P20-27 — Undo.** Each import is one change batch with an undo window (`xpt.import.undo_window_days`, default 7, 1–30); undo removes only what that import created and lists items already signed, shared or approved that need explicit confirmation. After the window, corrections follow normal record edits.

**FR-P20-28 — Signed originals imported.** Imported signed PDFs are validated for embedded signatures (PAdES/PKCS#7: signer, certificate chain, timestamp, integrity) and the result is shown; validation never alters the file. A file imported as "executed" without a recognisable signature is labelled "Executed outside LawDocs — signature not verified".

**FR-P20-29 — Agent proposals.** An `AGT_*` agent may draft an import plan (folder → module, columns → fields, unknown columns → custom fields); nothing is written until a human approves the plan and commits (NN-13).

### 4G. BYO storage targets and sync semantics

**FR-P20-30 — Adapters (Spec §12.2 `StorageTarget`).** Each implements `describe`, `verifyResidency`, `testWrite`, `put` (resumable; `writeOnce`, `retainUntil`), `head`, `list`, `retentionInfo`, `healthCheck`, and passes connector certification (Spec §14.3) before production.

| Target | Authentication | Residency check | Write-once | Plans |
|---|---|---|---|---|
| Amazon S3 / S3-compatible (MinIO, Indian clouds, on-prem object stores) | Cross-account IAM role with `ExternalId` (S3); access key in vault rotated ≤ 90 days or on-prem agent (others) | `GetBucketLocation` = ap-south-1/ap-south-2; signed attestation for others | S3 Object Lock; others where supported [VERIFY per product] | Business, Enterprise; Personal/Pro one-off push |
| Azure Blob | Entra workload identity federation or user-delegation SAS ≤ 7 days | Central/South/West India | Immutability policy | Business, Enterprise |
| Google Cloud Storage | Workload identity federation | asia-south1/asia-south2 | Retention policy + bucket lock | Business, Enterprise |
| SharePoint / OneDrive for Business (Microsoft Graph) | Entra app; `Sites.Selected` for the granted site only; large files via upload sessions [VERIFY scope names and upload-session limits] | Tenant data location attested by the client's IT head, re-attested yearly [VERIFY Graph property] | Retention label [VERIFY per plan] | Business, Enterprise; companies on M365 (R-053, R-055; CH-29) |
| OneDrive personal (individuals) | Delegated consent to an app folder [VERIFY permission name, e.g., app-folder scope] | Not India-guaranteed → user notice (FR-P20-32) | Not offered | All plans (one-off push); Personal+ scheduled |
| Google Drive (shared drive for companies; My Drive for individuals) | `drive.file` per-file scope preferred to avoid restricted-scope verification [VERIFY]; resumable uploads | No India region guarantee → non-regulated data only for companies (Spec §12.2); user notice for individuals | Not offered | All plans (one-off); Business+ scheduled |
| SFTP / on-premises server | ed25519 keys, pinned host key, yearly rotation | Signed attestation of location | Only if server enforces WORM (attested) | Business, Enterprise |
| NAS / file server / attached external drive via the on-premises agent | Outbound-only mTLS device certificate; agent signed and auto-updating | Signed attestation of site | As underlying store | Business, Enterprise |
| External drive by download | — (user downloads the package) | n/a | n/a | All plans |

Scheduled exports and continuous mirror to BYO targets are the `LD-ADD-BYO` add-on on Business and included in Enterprise (R6 §R6.2.3) [OWNER TO SET]; one-off exports and downloads are free on every plan (NN-11).

**FR-P20-31 — Data-class policy per target.** Each target declares the data classes it may hold (Spec §13.2). For companies, regulated classes — KYC records, credit and loan documents of a regulated lender, books of account and tax records, board-confidential papers, HR and payroll — require an India-resident target (Companies (Accounts) Rules 2014 r.3(5) for electronic books back-up on servers in India [LAW; VERIFY current text]; sector rules). Google Drive and non-attested targets may hold only `PUBLIC`/`INTERNAL` material and `CONFIDENTIAL` documents without personal data, books or returns; otherwise `LD-XPT-031 residency-blocked` before upload.

**FR-P20-32 — Individuals' own destinations.** An individual may send their own data to a personal OneDrive or Google Drive at their instruction. Before the first push the app shows a plain notice ("Your files will be stored by Google/Microsoft and may be held outside India. LawDocs keeps its own copy in India.") and records the user's instruction; this is the user exercising control over their data, recorded in the transfer register as user-directed (NN-25) [INTERP].

**FR-P20-33 — Sync semantics (binding).**

| Aspect | Rule |
|---|---|
| Direction | **Push-only** (LawDocs → target) for exports, schedules and mirror. Intake from a target is a separate **watch-folder import** (§4F) into a different folder (`LawDocs Inbox/`). Never two-way merge on one tree [REC: avoids conflict loops and silent overwrites] |
| Overwrite | Never overwrite a file whose hash differs from what LawDocs last wrote. New versions are new files (`… v3 - SIGNED.pdf`); an optional `Latest/` convenience copy per record may be replaced only if unchanged by the customer |
| Conflict | If the customer changed or deleted a LawDocs-written file, LawDocs does not restore or overwrite it silently: it writes `… (LawDocs copy <date>)`, logs a conflict, and raises a `wf.items` item `XPT_TARGET_CONFLICT` to the target owner |
| Deletion | LawDocs deletes on a target only objects it wrote, only under the tenant's configured pruning policy, and never past a lock; a retention-driven deletion in LawDocs is mirrored only if `xpt.mirror.propagate_deletions` is ON (default OFF) |
| Encryption | Provider-side encryption (SSE-KMS, Azure, GCS) on; optional BYOK (cross-account key grant); optional client-side encryption of the package to the tenant's public key (age X25519 or OpenPGP) |
| Idempotency | Every `put` carries `(target_id, record_id, ver_id, path_version)` as idempotency key (NN-46); re-runs never create duplicate folders after a release (golden check) |
| Revoke | When the customer revokes the credential or key, health fails closed (`key_unavailable` / `credential_revoked`), jobs pause, nothing is retried against another target, LawDocs deletes its stored credential on disconnect, and **disconnecting never deletes customer copies** |
| Residency drift | Weekly and pre-job residency checks; failure pauses the target and notifies |

**FR-P20-34 — Continuous mirror.** Optional per target: an outbox subscription streams changes (new document versions, record updates, item state changes) into incremental packages applied to the target within `xpt.mirror.max_lag_minutes` (default 15); nightly reconciliation compares target `list()` with the expected manifest and repairs gaps (never overwriting customer-changed files); a monthly full package anchors the chain. Each delivered increment is a valid package (deltas + cumulative `state-index.csv`) so the latest state can be assembled offline.

**FR-P20-35 — Health and events.** Residency at registration, weekly and before full/exit jobs; daily `healthCheck()` and canary; credential expiry warnings 30 days ahead; one missed scheduled copy → P2 alert, two consecutive → P1 alert and tenant notice. Events `StorageTargetConnected`, `BackupCompleted`, `RestoreTested` and health failures are published per Spec §6.26 (§4J).

**FR-P20-36 — Restore tests from customer copies.** Quarterly by default (`xpt.restore_test.frequency`, monthly–annually): verifier over latest full + increments in the customer's store (integrity), headless open of a sample (readability), optional rehydration into a scratch workspace with count reconciliation; report for the customer's continuity evidence.

### 4H. Schema evolution and infrastructure-move safety (R-021, R-022, NN-12)

**FR-P20-37 — Canonical IDs.** Every record has an immutable prefixed ULID (Appendix B §B.1; master §5.4) and, where defined, a permanent business reference (`LD-AGR-…`); neither is derived from table names or sequences; both survive export, import, migration, region move and vendor change. External identifiers (CNR, TM application number, CIN, stamp UIN) are attributes, never keys.

**FR-P20-38 — Expand → migrate → contract.** All schema changes follow P23 FR-P23-17: additive first, idempotent and verified backfills (Temporal jobs with checkpoints), dual-read/dual-write where needed, contract only after a full release cycle and after the export map no longer references the old shape. A migration that removes or renames a column still referenced by `xpt.export_map` fails `ci/export-contract`.

**FR-P20-39 — Export-map contract test (CI gate).** CI introspects schemas and module registries: every persisted business table maps to an export-map entry or is explicitly annotated `x-export: derived` (with source) or `x-export: excluded` (with approved reason, e.g., caches). A new column on a mapped table must declare its export column or `x-export: internal`. A PR adding a record type without a mapping fails.

**FR-P20-40 — Golden archives.** Synthetic golden workspaces (one per profile; every record type; edge cases: long titles, Hindi and Tamil titles, 400-character counterparty names, duplicate names, renamed departments, deleted-then-restored records, legal holds) are exported on every release candidate and compared with the previous release's golden archive: unexpected path, file name, column header, code-table meaning or count changes fail the release. Approved additive changes are listed in `CHANGES-SINCE-PREVIOUS.csv`.

**FR-P20-41 — Archive versioning.** `LD-EXPORT` follows semantic versioning per profile: **patch** (wording, README), **minor** (new folders, files or columns — additive; a 1.0 reader ignores unknown parts), **major** (any path-template or column-meaning change — GOVERNED `REGULATED` change, compatibility map old → new path in `00 Start Here/path-map.csv`, announced to tenants ≥ 30 days ahead, mirror targets keep receiving the old layout until the tenant opts in or the next annual window). The loader reads every past minor without loss.

**FR-P20-42 — Vendor and region move runbook.** Documented, rehearsed tooling for: (a) database provider move (e.g., Supabase non-prod → RDS/Aurora; Aurora major upgrade): logical replication, per-table row counts and checksums, audit-chain verification end to end, cut-over in a read-only window, golden-archive diff = empty; (b) object storage move (bucket, account, provider within India): copy with per-object SHA-256 verification, dual-read during migration, KMS re-wrap, Object Lock re-application where supported; (c) region pair change (ap-south-1 ↔ ap-south-2 or a new India region): (a)+(b) plus residency attestation; (d) cloud change to another India-resident provider: `LD-EXPORT` full + logical dump re-imported with ID preservation and the same diff. Each move produces a **migration evidence pack** (counts, hashes, diffs, approvals) stored as P23 control evidence, and tenants receive ≥ 30 days' notice where a sub-processor or location changes. Customers' mirror targets need no action: paths and IDs are unchanged.

**FR-P20-43 — Release blockers for customer data.** A release cannot ship if it: changes canonical paths without a profile major; drops or renames mapped columns; changes ID formats or business-reference formats; redefines an existing code-table value (adding values is allowed); or fails the golden-archive diff. No release note may contain a customer migration step (`release-notes-lint`).

**FR-P20-52 — Cloud and vendor portability as a design property *(v1.1; IPB-01 §01.4.13, IPB-D-02)*.** FR-P20-42's runbook assumed one production cloud (AWS ap-south-1 → ap-south-2). *(v1.1 — superseded in scope, not content: AWS is the reference deployment; the runbook must work for any target that satisfies the port contracts.)* Requirements: (a) **no direct cloud SDK** outside `packages/connectors/<port>/<adapter>/` — a lint (`ci/ports-not-vendors`) fails the build on `@aws-sdk/*`, `@azure/*`, `@google-cloud/*` imports elsewhere; (b) **PostgreSQL-only** with the IPB-01 extension allow-list (`pgcrypto`, `pg_trgm`, `pgvector`, `uuid-ossp`, `btree_gist`); vendor-specific features (Aurora-only functions, Supabase RPC) are forbidden in migrations and queries (`ci/pg-portability`); (c) **object storage** through `STORAGE_PORT` with the Object Lock equivalence table (S3 Object Lock COMPLIANCE ↔ Azure Blob immutability policy (locked) ↔ GCS bucket retention lock ↔ MinIO WORM) — the evidence-class retention test runs against two adapters in CI; (d) **containers**: one image per app from the shared multi-stage Dockerfile, deployable by the `infrabyx-app` Helm chart on any Kubernetes (EKS reference; AKS and GKE module parity), with no cloud-specific sidecars; (e) **Terraform modules per cloud** under `infra/terraform/{aws,azure,gcp}` with identical module names and the IPB-01 §01.4.9.3 output contract (`db_endpoint`, `object_store_buckets`, `kms_key_refs`, `queue_endpoint`, `cluster_endpoint`, `dns_zone`); (f) the **exit runbook and BOM** (`docs/runbooks/exit.md`, `docs/bom.json`) are generated artefacts, published to the Vendor Assurance Room (P23 FR-P23-60) as `EXIT_RUNBOOK` and `BOM`.

**FR-P20-53 — Provider-swap RTO and drills.** For each Tier-0 port (STORAGE, DATABASE engine host, KMS, SECRETS, QUEUE, IDENTITY, LLM `in_zero`) the pack states a **provider-swap RTO** (design property, measured in a drill): database host move ≤ 24 h for ≤ 2 TB (logical replication, per-table row counts and checksums, audit-chain verification end to end — FR-P20-42(a)); object storage ≤ 72 h for ≤ 50 TB with hash manifests and retention re-application; KMS re-wrap of per-tenant data keys ≤ 8 h (envelope encryption makes this a key-wrap operation, never a data re-encryption); identity realm export/import ≤ 8 h with forced re-login; LLM adapter switch ≤ 1 h (configuration). A **portability drill** runs at least every six months in `staging`: restore the latest golden archive and a synthetic tenant onto the alternative adapters (MinIO, CloudNativePG or a second managed PostgreSQL, Vault), run the full acceptance suite, and record `in.lawdocs.xpt.ExitDrillCompleted.v1` with timings; the P23 go-live checklist requires one passed drill per wave. Failure of a drill is a Sev-3 incident with a CAB item.

**FR-P20-54 — Supabase and non-production boundaries.** Supabase PostgreSQL may host `dev`/`test`/`staging` databases **only** (IPB-01 §01.4.11): no Supabase Auth, Storage, Edge Functions or RPC in product code; schemas and migrations identical to production; the database adapter is the same `pg` client; `IPB_DATA_RESIDENCY=IN` must be satisfied by the Supabase project region (ap-south-1) [VERIFY project region at P00]; synthetic data only (OP-7). Production and DR never run on Supabase.

**FR-P20-55 — Settings › Storage & data (IPB-07 node 12).** The tenant node shows usage by data class, BYO storage (connect a target via `STORAGE_PORT`, test, cut-over — FR-P20-27…36), export (on demand or scheduled, FR-P20-05…), retention schedules per record type with regulatory floors locked (Appendix G), legal holds, deletion requests and the data-residency statement; every action has a help key and an "explain why" line; click budget ≤ 3 from Settings to start an export.

### 4I. Exit, offboarding and erasure

**FR-P20-44 — Company exit workflow.** `EXIT_REQUESTED` (maker-checker) → **exit export** (`EXIT`: full workspace, all versions, restricted archives as approved, full audit trail, configuration bundle, integration mapping history, AI work-product ledger) → **tenant confirms receipt and verification** (verifier report uploaded or confirmed) → **read-only period** (`xpt.exit.read_only_days`, default 90, 30–180) → **deletion** from primary stores, search indexes, vector stores, caches and replicas, with backups expiring at their natural retention (documented, immutable) → **deletion certificate** (PDF/A signed with DSC: scope, dates, systems, backup expiry dates, exceptions) → `CLOSED`. Exceptions listed with basis: legal holds, records LawDocs must itself keep (its own invoices and tax records for the subscription — CGST Act s.36, 72 months [VERIFY]; eSign transaction evidence and logs it holds as the hosting platform under the route's `asp_mode` — ≥ 7 years, R3 LG-008), records under a pending court or statutory order.

**FR-P20-45 — Individual account closure.** Closing a Personal workspace always offers a full export first; shows what LawDocs must retain and why (e.g., eSign evidence held for the signing route; invoices); applies the DPDP erasure duty when the purpose ends, with a pre-erasure notice to the user (DPDP Rules 2025 r.8 provides a 48-hour notice for Third-Schedule classes — applied voluntarily to all individuals, R3 LG-065) [VERIFY commencement 13 May 2027]; respects nominee/legacy settings (a nominee's time-locked access is cancelled or triggered per the user's choice, P01); and confirms erasure by email with the certificate. Counterparties keep their own copies of shared agreements in their own workspaces — closure never deletes another person's records.

**FR-P20-46 — Retention engine interplay.** Erasure and pruning run through P04's retention engine: longest applicable retention class wins (`longest` merge), legal hold blocks deletion, and every deletion is a ledger event without content. Default floors (Appendix R): eSign evidence ≥ 7 years after the later of signing and account closure; CERT-In logs 180 days in India; DPDP logs ≥ 1 year (r.6/r.8(3), R3 LG-065); tax documents 8 years [REC]; contracts ≥ term + limitation + buffer, never < 7 years [REC] (R3 LG-092).

**FR-P20-47 — Delivery and RM handover.** Retainer clients leaving LawDocs services (but not the platform) get delivery-grant closure and a handover export of the engagement folder; RMs lose access at grant end (NN-17).

### 4J. Ecosystem archive standard and cross-product sharing

**FR-P20-48 — Conformance.** Packages pass the ecosystem certification suite for archives (Spec §14.3): structure, `00 Start Here`, manifest columns, JWS, checksums, README coverage, PDF/A, headless render, restricted-archive handling.

**FR-P20-49 — Portability events via `int`.** LawDocs publishes, only through `int`, `in.infrabyx.portability.ExportRequested.v1`, `…ExportCompleted.v1` (signed), `…StorageTargetConnected.v1`, `…BackupCompleted.v1`, `…RestoreTested.v1` (Spec §6.26) to the tenant's configured compliance destination (e.g., the tenant's LDC workspace) and counts/status only to OH4/OH13 (NN-19). Payloads describe jobs, never content. LawDocs' producer registration for the `portability` domain is requested in Appendix Y.

**FR-P20-50 — Sharing archives across products (R-023, CH-16).** A package or folder may be shared, under a scoped, expiring, logged grant with a `consentref` or `legalbasis` (NN-24): to the same customer's LDC workspace (e.g., policies folder for compliance evidence), to an Equator case as a referral pack (by reference with consent), to a marketplace engagement, or to an auditor workspace. Evidence held in another product is referenced by ID + SHA-256 + producer, not copied, unless the producer permits copies. Never an open public link.

**FR-P20-51 — Importing ecosystem archives.** LawDocs accepts `archive_standard_version` 1.0 packages from other Infrabyx products (e.g., an LDC export's agreements folder, an Equator settlement agreement) with the same import pipeline; IDs from the producing product are kept as external references.

---

## 5. Workflows and state machines

### 5.1 Export job (`xpt.export_jobs.state`)

State machine: Appendix A §A.22 governs.

```
REQUESTED → AWAITING_APPROVAL (scope needs it; step-up recorded) → APPROVED
  → SNAPSHOTTING → COLLECTING (per record type via export map) → RENDERING (DOCX/PDF/A/XLSX; gates)
  → PACKAGING (tree, names, restricted archives, index) → RECONCILING (control totals)
  → SIGNING (JWS, checksums) → DELIVERING (download | target put | SFTP)
  → COMPLETED → CONFIRMED (recipient or target verified)
any stage → FAILED (reason; resumable) | CANCELLED (requester/approver, before SIGNING)
AWAITING_APPROVAL → REJECTED | EXPIRED (72 h)
```

Events: `in.lawdocs.xpt.ExportRequested.v1`, `…ExportApproved.v1`, `…ExportCompleted.v1`, `…ExportFailed.v1`; ecosystem copies via `int` (§4J).

### 5.2 Storage target (`xpt.storage_targets.state`)

State machine: Appendix A §A.24 governs.

`DRAFT → VERIFYING (describe, verifyResidency, testWrite) → PENDING_APPROVAL (regulated classes: maker-checker) → ACTIVE → DEGRADED (one failed check) → PAUSED (two failures, credential revoked, residency drift, key unavailable) → ACTIVE (after re-verify) | DISCONNECTED (credentials deleted; customer copies untouched)`.

### 5.3 Import job (`xpt.import_jobs.state`)

State machine: Appendix A §A.21 governs (Resolution R-A-10); this section is its canonical source. There is **one** `imp_` ID space owned by `xpt`: P04 folder intake (`source_kind = DMS_FOLDER`; its labels `EXPANDING` = `SCANNING`, `MAPPING_PREVIEW` = `AWAITING_REVIEW`, `COMMITTED_WITH_EXCEPTIONS` = `COMMITTED` with exception rows), P11 case-register imports (`LIT_REGISTER`) and P12 portfolio imports (`IPM_REGISTER`) are rows of this machine with module-specific mapping and validation; P03 configuration import and P21 DOCX import are separate machines.

`CREATED → SCANNING → MAPPING → CLASSIFYING (optional) → AWAITING_REVIEW (preview and corrections) → COMMITTING → COMMITTED (report; undo window open) → UNDONE | FINALISED`; `FAILED` with resumable checkpoint; `CANCELLED` before commit (staging purged).

### 5.4 Mirror increment

State machine: Appendix A §A.24 governs.

`CHANGE_CAPTURED (outbox) → BATCHED (≤ lag window) → PACKAGED (delta + cumulative index) → PUT (idempotent) → VERIFIED (head hashes) → ACKNOWLEDGED`; nightly `RECONCILE → REPAIRED | CONFLICTS_RAISED`.

### 5.5 Exit

State machine: Appendix A §A.23 governs (Resolution R-A-11: P17 `EXIT → CLOSED` and P01 `CLOSING → CLOSED` are entry points into this machine; billing never blocks read or export during `READ_ONLY`).

`EXIT_REQUESTED → APPROVED → EXPORTING → AWAITING_RECEIPT_CONFIRMATION → READ_ONLY (n days) → DELETING → DELETION_CERTIFIED → CLOSED`; legal hold or order → `HELD` with listed exceptions; a tenant may `REACTIVATE` during `READ_ONLY`.

### 5.6 Release gate for portability (CI, with P23)

`ci/export-contract` → `ci/golden-archive-diff` → `ci/pdfa-render` → `ci/path-pii-scan` → `release-notes-lint`; any failure blocks promotion beyond staging.

---

## 6. Screens and UX

| Screen ID | App | Name | Purpose and components | Empty / error | Mobile and accessibility |
|---|---|---|---|---|---|
| SCR-P20-01 | web, mobile | My data and exports `/settings/data` | "Export everything", presets (this year, one matter, one counterparty), history, downloads | "No exports yet — Export everything in one click" | ≤ 2 taps from Settings; progress announced via live region |
| SCR-P20-02 | web | Export wizard | Scope, filters, preview tree with counts and size, restricted items, approvals, delivery | Approval needed explained | Tree has list alternative |
| SCR-P20-03 | web, mobile | Export progress and download | Stages, ETA, parts list, verify instructions | Failed stage with next action | Wi-Fi recommendation on mobile |
| SCR-P20-04 | web | Approval card (export) | Scope, size, restricted parts, requester; approve with step-up | — | Mobile approval supported |
| SCR-P20-05 | web | Storage targets `/settings/data/storage` | Add target wizard per provider, residency result, canary, data classes, schedule, mirror toggle, health | Residency blocked explained | — |
| SCR-P20-06 | web | Target detail and health | Last copies, lag, conflicts, restore tests, credentials expiry, pause/disconnect | Conflict list with items | — |
| SCR-P20-07 | web | Import wizard `/import` | Source choice (upload folder/ZIP/drive/agent/LD package), scan summary | Unsupported files list | Drag-and-drop has "Choose folder" button alternative |
| SCR-P20-08 | web | Import review grid | Proposed destinations, confidence, conflicts, bulk accept by rule, create records | "41 need your choice" | Grid keyboard navigable; summaries for screen readers |
| SCR-P20-09 | web, mobile | Import report and undo | Report download, undo until date | — | — |
| SCR-P20-10 | web | Folder policy `/settings/data/folders` | Year label, entity level, splits, person-naming mode, README language, preview | Locked top-level shown | — |
| SCR-P20-11 | web | Exit plan and closure | Exit steps, dates, read-only period, retention exceptions, certificate | — | — |
| SCR-P20-12 | web, mobile | Close my account (individual) | Export first, what is kept and why, nominee choice, confirm | — | Plain language; no confirm-shaming (NN-50) |
| SCR-P20-13 | console | Export map registry | Record types, profile versions, coverage, golden diffs | Unmapped types (must be zero) | — |
| SCR-P20-14 | console | Platform portability health | Jobs, failures, mirror lag, targets degraded, restore tests | — | — |
| SCR-P20-15 | web | "Download as folder" action | On every list and record | — | 1 click |

Click budgets: export everything ≤ 3 clicks from home (Settings → My data → Export everything) plus approval where required; export one record ≤ 2 clicks; start a folder import ≤ 2 clicks from Documents ("Upload folder").

---

## 7. Backend design

### 7.1 Modules

`xpt` (owner), `dms` (documents, versions, retention, legal hold), `core` (IDs, ledger, anchors), `int` (connector framework, ecosystem events), `dix` (classification), `sgn` (evidence packs, s.63 certificate), `cfg` (settings, bundle), `wf` (items), every module's export-map registrations.

### 7.2 Tables (schema `xpt`; RLS on tenant tables)

| Table | Key columns | Notes / retention |
|---|---|---|
| `export_map` *platform* | record_type, profile, profile_version, module, path_template, file_templates jsonb, dataset, columns jsonb, attachments_rule, restricted_class, retention_class, stability_key[], legacy_path_template | permanent |
| `folder_policies` | tenant_id, version, options jsonb, recorded_at | permanent |
| `export_jobs` | id (`exp_`), tenant_id, scope_code, filters, profile, profile_version, as_of, state, requester_id, approvals jsonb, stage_checkpoints jsonb, size_bytes, parts, archive_id, predecessor_archive_id, error | 7 years |
| `export_files` | job_id, path, sha256, bytes, record_type, record_id, canonical_path | as job |
| `storage_targets` | id (`stg_`), tenant_id, provider, config jsonb (no secrets), secret_ref, region, residency_result, data_classes[], key_mode, write_once, state, schedule rrule, mirror_enabled, last_health_at | life of target + 1 year |
| `target_writes` | target_id, idempotency_key, path, sha256, written_at, customer_modified_detected | 7 years |
| `target_conflicts` | target_id, path, expected_sha256, found_sha256, item_id, resolution | 3 years |
| `import_jobs` | id (`imp_`), tenant_id, source_kind, source_ref, state, counts jsonb, rules jsonb, batch_id, undo_until, report_doc_id | 7 years |
| `import_files` | job_id, source_path, sha256, detected_type, proposal jsonb, confidence, decision, destination_ref, duplicate_of | as job |
| `exit_requests` | tenant_id, state, dates, exceptions jsonb, certificate_doc_id | permanent |
| `restore_tests` | target_id, kind, result, discrepancies, report_doc_id | 7 years |
| `golden_runs` *platform* | release, profile, diff_summary, result | permanent |

### 7.3 APIs (`/v1`; Idempotency-Key on POST)

`POST /v1/exports` (scope, filters, delivery) · `POST /v1/exports/{id}:approve|reject|cancel` · `GET /v1/exports/{id}` · `GET /v1/exports/{id}/parts/{n}` (re-auth) · `POST /v1/exports:preview` · `POST /v1/records/{type}/{id}:export` · `GET/POST /v1/storage-targets` · `POST /v1/storage-targets/{id}:verify|approve|pause|resume|disconnect|restore-test` · `POST /v1/imports` (source) · `POST /v1/imports/{id}/files:upload` (resumable, tus-style) · `GET /v1/imports/{id}/proposals` · `PATCH /v1/imports/{id}/proposals` (bulk corrections) · `POST /v1/imports/{id}:commit|undo|cancel` · `POST /v1/exit` · `POST /v1/exit/{id}:approve|confirm-receipt|reactivate` · `GET /v1/folder-policy` · `PUT /v1/folder-policy` · Console: `GET /v1/console/export-map`, `POST /v1/console/export-map/{type}/versions`, `GET /v1/console/golden-runs`. Mobile BFF: `/m/v1/exports` (create, status, download link), `/m/v1/imports` (files and ZIP only).

### 7.4 Domain events

Internal: `in.lawdocs.xpt.ExportRequested.v1`, `…ExportApproved.v1`, `…ExportCompleted.v1`, `…ExportFailed.v1`, `…StorageTargetConnected.v1`, `…StorageTargetDegraded.v1`, `…StorageTargetPaused.v1`, `…MirrorIncrementDelivered.v1`, `…TargetConflictDetected.v1`, `…ImportCommitted.v1`, `…ImportUndone.v1`, `…ExitRequested.v1`, `…DeletionCertified.v1`, `…RestoreTested.v1`, `…ExportMapVersionPublished.v1`. Cross-product (via `int` only): `in.infrabyx.portability.ExportRequested.v1`, `…ExportCompleted.v1`, `…StorageTargetConnected.v1`, `…BackupCompleted.v1`, `…RestoreTested.v1`; health failures as `ControlTestResultPublished` (control `STORAGE_TARGET_HEALTH`) per Spec §6.26.

### 7.5 Jobs and Temporal workflows

`ExportWorkflow` (stages with checkpoints; activities per module collector), `IncrementalExportWorkflow`, `MirrorWorkflow` (per target; outbox consumer + nightly reconcile), `TargetHealthJob` (daily), `ResidencyRecheckJob` (weekly), `CredentialExpiryJob`, `ImportWorkflow`, `ImportUndoWorkflow`, `ExitWorkflow`, `DeletionWorkflow` (with retention/legal-hold checks), `RestoreTestWorkflow`, `GoldenArchiveJob` (CI and release candidates), `PathPiiScanJob`, `DownloadLinkExpiryJob`.

---

## 8. Integrations

| Port | Adapters | Failure behaviour | Manual fallback |
|---|---|---|---|
| `STORAGE_TARGET_PORT` (Spec §12.2) | S3, S3-compatible, Azure Blob, GCS, Microsoft Graph (SharePoint/OneDrive), Google Drive API, SFTP, on-prem agent | Pause; alert; never silent re-route | Download and copy manually |
| `SUITE_PORT` (P19) | Microsoft Graph, Google Workspace | Token expired → reconnect prompt | Download |
| `DIX_PORT` (P05) | Classification and extraction | Unavailable → rule-based mapping only; more items to review | Manual correction grid |
| `AV_SCAN_PORT` | ClamAV-type engine in isolated container | Unscanned files quarantined | — |
| `SIGNATURE_VALIDATION_PORT` (P08) | PAdES/PKCS#7 validation | "Not verified" label | — |
| `KMS_PORT` | AWS KMS; customer BYOK grants | `key_unavailable` fail-closed | — |

Graph and Drive throttling: honour `Retry-After` and 429/503 with exponential back-off and jitter; resumable uploads for large files; per-tenant concurrency caps [VERIFY current Graph and Drive quotas at build].

---

## 9. Settings and configuration

Full list in Appendix R §R.9 (`xpt`).

| Key | Tier (scopes) | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `xpt.export.never_blocked_by_billing` | PLATFORM | LOCKED | boolean | true | — | — |
| `xpt.export.tenant_full_requires_checker` | PLATFORM | LOCKED | boolean | true (companies) | — | — |
| `xpt.portability.drill_interval_months` *(v1.1)* | PLATFORM | GOVERNED | integer 3–12 | 6 | `PLT_RELEASE_MANAGER` | Y |
| `xpt.portability.rto_hours.<port>` *(v1.1)* | PLATFORM | GOVERNED | integer | per FR-P20-53 | `PLT_SRE` | Y |
| `xpt.storage.object_lock_mode` *(v1.1)* | PLATFORM | LOCKED | enum COMPLIANCE | COMPLIANCE (prod) | — | — |
| `xpt.db.engine` *(v1.1)* | PLATFORM | LOCKED | enum postgresql | postgresql | — | — |
| `xpt.export.small_company_cooling_minutes` | PLATFORM | GOVERNED | — | **superseded** — solo-owner exports use P02 `wf.mc.solo_owner.cooling_off_hours` (24 h); do not read this key (deprecate in Appendix R) | — | — |
| `xpt.download.link_validity_days` | TENANT | OPEN | integer 1–30 | 7 | `ORG_ADMIN`, `IND_OWNER` | N |
| `xpt.download.part_size_gb` | TENANT | OPEN | integer 1–16 | 4 | `ORG_ADMIN` | N |
| `xpt.folder.year_label` | TENANT | OPEN | enum FY_LONG/FY_SHORT/CY | FY_LONG (company), CY (individual) | `ORG_ADMIN`, `IND_OWNER` | N |
| `xpt.folder.entity_level` | TENANT | OPEN | enum auto/always/never | auto | `ORG_ADMIN` | N |
| `xpt.folder.name_mode` | TENANT | OPEN | enum historical/current | historical | `ORG_ADMIN` | N |
| `xpt.folder.path_script` | TENANT | OPEN | enum latin/original | latin | `ORG_ADMIN` | N |
| `xpt.naming.person_mode` | BRAND→TENANT | GOVERNED-privacy | enum full_name/masked_name/ids_only | per profile (FR-P20-17) | `ORG_OWNER` (Consumer Help: LOCKED ids_only) | Y |
| `xpt.readme.languages` | TENANT | OPEN | multi-enum | [en] | `ORG_ADMIN` | N |
| `xpt.mirror.max_lag_minutes` | PLAN→TENANT (`raise_only`) | OPEN | integer 5–1440 | 15 | `ORG_ADMIN` | N |
| `xpt.mirror.propagate_deletions` | TENANT | GOVERNED-elevated | boolean | false | `ORG_ADMIN` | Y |
| `xpt.targets.regulated_classes_india_only` | PLATFORM | LOCKED | boolean | true | — | — |
| `xpt.targets.connect_requires_checker` | TENANT | GOVERNED-elevated | boolean | true for regulated classes | `ORG_OWNER` | Y |
| `xpt.import.max_zip_gb` | PLAN | GOVERNED | integer | 2 (Free) … 20 (Business+) | `PLT_SUPER_ADMIN` | N |
| `xpt.import.confidence_auto` / `xpt.import.confidence_confirm` | TENANT | OPEN | decimal | 0.85 / 0.50 | `ORG_ADMIN` | N |
| `xpt.import.undo_window_days` | TENANT | OPEN | integer 1–30 | 7 | `ORG_ADMIN` | N |
| `xpt.import.never_overwrite` | PLATFORM | LOCKED | boolean | true | — | — |
| `xpt.restore_test.frequency` | TENANT | OPEN | enum monthly/quarterly/half_yearly/annual | quarterly | `ORG_ADMIN` | N |
| `xpt.exit.read_only_days` | PLATFORM→TENANT | GOVERNED | integer 30–180 | 90 | `ORG_OWNER` | Y |
| `xpt.profile.major_change_notice_days` | PLATFORM | GOVERNED | integer ≥ 30 | 30 | `PLT_SUPER_ADMIN` | Y |
| `xpt.flag.ai_import_classification` | PLATFORM→TENANT | GOVERNED | boolean | false (Wave 1) / true (Wave 2) | `PLT_RELEASE_MANAGER`; tenant may switch off | N |
| `int.kill.storage_<provider>` | PLATFORM/TENANT | GOVERNED | boolean | off | `PLT_SECURITY_OFFICER` / `ORG_ADMIN` | Release Y |

---

## 10. Security, privacy and audit

| Threat | Control |
|---|---|
| Insider exfiltrates a whole company | Tenant exports maker-checker (NN-18); step-up; watermarking for external grants; download only by requester after re-auth; anomalous export volume alert to owners |
| Delivery staff export client data | Delivery grants must include `xpt:export`; never FULL_TENANT; logged in the client's access-transparency view (NN-17) |
| Malicious upload via import | Magic-byte checks, AV scan, macro-disabled previews in a sandbox, size limits, zip-bomb detection (ratio and depth), path-traversal rejection (`../`, absolute paths, symlinks) |
| Personal data in paths leaks via sync logs | Person-naming modes; path PII scanner; Aadhaar never present (NN-04) |
| Target credential theft | Federation where available; secrets only in vault (`secret_ref`); short-lived SAS; rotation alerts |
| Silent overwrite of customer copies | Push-only, never-overwrite, conflict items |
| Tampered archive presented in court | SHA-256 manifest, detached JWS, chain anchors, s.63 certificate, verifier |
| Residency breach | Data-class policy per target; residency checks; India-only for regulated classes (NN-25) |

Audit (same transaction, NN-45): export requested/approved/downloaded (who, when, IP/device class), target connected/changed/paused/disconnected, every put batch, import commits and undos, exit milestones, deletion certificates. Logs never include file content or names of personal-data-bearing paths beyond IDs (NN-32). DPDP: exports implement access and portability for individuals (fiduciary role) and for tenants (processor role; tenants respond to their own principals); erasure implements r.8 with notice and certificate; breach involving an export link follows P23 incident clocks.

---

## 11. AI touchpoints and guardrails

| Touchpoint | Agent / feature | Autonomy | Human confirmation |
|---|---|---|---|
| Import classification and extraction | `dix` + Vidhi (`AGT_DMS_LIBRARIAN` per Appendix H) | L2 | User confirms proposals in the review grid before commit |
| Import plan from a messy tree or another tool's CSV | Vidhi | L2 | Plan approved by a human; commit is a human action |
| "Find my documents" in an export | README offline viewer search (no AI) | — | — |
| Export proposals ("export this matter for the new counsel") | Vidhi | L2 | Draft request in inbox; a human starts it; download link never returned to an AI client (NN-13) |

Evaluation: classification precision ≥ 0.92 and recall ≥ 0.90 on the golden import set of 2,000 Indian legal documents (agreements, deeds, affidavits, orders, notices, invoices; English, Hindi and two regional languages) before `xpt.flag.ai_import_classification` turns on by default.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p20/*.feature`)

```gherkin
@P20-AT-01 @NN-11
Scenario: Every record type is exportable
  Given the seeded golden company workspace with every record type
  When ORG_ADMIN requests a FULL_TENANT export and ORG_CLO approves
  Then the package contains every record with count reconciliation per type
  And every original is byte-identical to the vault (SHA-256)

@P20-AT-02 @NN-11
Scenario: Missing export mapping fails CI
  Given a pull request adding table "ipm.watch_hits" without an export-map entry or x-export annotation
  When ci/export-contract runs
  Then the build fails naming "ipm.watch_hits"

@P20-AT-03 @NN-12
Scenario: Paths are stable across a release with schema changes
  Given golden archive G1 from release 2026.11.1
  And release 2026.11.2 renames column "clm.agreements.title" via expand-migrate-contract
  When the golden archive G2 is generated
  Then every path and file name for unchanged records equals G1
  And differences appear only in CHANGES-SINCE-PREVIOUS.csv as additions

@P20-AT-04 @NN-12
Scenario: Renaming a department does not move files
  Given department "Legal" renamed to "Legal and Compliance" on 2027-01-10
  When an export runs with name_mode historical
  Then agreements dated 2026 are under "Legal" and those dated after 2027-01-10 under "Legal and Compliance"
  And the manifest carries the same department_id for both
  And no S3 object key changed

@P20-AT-05 @NN-10
Scenario: Offline verification detects tampering
  Given a completed package
  When one byte of "03 Signed and Stamped/… v3 - SIGNED.pdf" is changed
  Then "sha256sum -c checksums.sha256" reports a failure
  And the verifier reports the JWS still valid but the file hash mismatched

@P20-AT-06 @NN-04
Scenario: No Aadhaar number in any export
  Given a scanned Aadhaar card uploaded with masked derived text
  When a FULL_TENANT export is assembled
  Then the content scan finds no unmasked 12-digit Aadhaar number in any derived file, index or path

@P20-AT-07 @NN-18
Scenario: Company full export needs a second approver
  Given ORG_ADMIN "A" requests a FULL_TENANT export
  When "A" tries to approve it
  Then the response is 403 with LD-XPT-012 "A second person must approve"

@P20-AT-08 @NN-11
Scenario: Individual exports everything without staff help
  Given IND_OWNER on the Free plan
  When she taps Settings, My data, Export everything and confirms with step-up
  Then the package builds without any LawDocs staff action and a download link is sent

@P20-AT-09 @NN-11
Scenario: Export is never blocked by billing state
  Given a Business tenant in termination-notice state for non-payment
  When ORG_ADMIN requests an EXIT export
  Then the export proceeds and no payment check is evaluated

@P20-AT-10 @NN-25
Scenario: Regulated data refused for Google Drive
  Given a company target on Google Drive with data classes INTERNAL
  When a scheduled export includes board-confidential papers
  Then those files are not uploaded and LD-XPT-031 "residency-blocked" is recorded
  And the rest of the package is delivered

@P20-AT-11
Scenario: Customer-modified file is never overwritten
  Given LawDocs wrote "… v2 - SIGNED.pdf" to SharePoint and the customer edited it
  When the mirror runs
  Then LawDocs writes "… (LawDocs copy 2026-11-03).pdf" and raises an XPT_TARGET_CONFLICT item
  And the customer's file is unchanged

@P20-AT-12 @NN-46
Scenario: Mirror is idempotent after a release
  Given a target mirrored before release 2026.12.1
  When the mirror re-runs after the release
  Then no duplicate folders or files are created

@P20-AT-13
Scenario: Revoked credential pauses safely
  Given an S3 target whose IAM role trust is removed by the customer
  When the next health check runs
  Then the target state is PAUSED with "credential_revoked"
  And no job is retried against another target
  And no object on the customer bucket is deleted

@P20-AT-14 @NN-13
Scenario: Import commits only after human review
  Given a 3,000-file folder upload with AI classification on
  When classification finishes
  Then no document is created until the user reviews proposals and clicks Commit

@P20-AT-15
Scenario: Duplicates are linked not copied
  Given 120 files already in the vault with identical SHA-256
  When they appear in an import
  Then they are linked to existing documents and listed as duplicates in the import report

@P20-AT-16
Scenario: Import undo removes only what it created
  Given import IMP-1 created 400 documents and one was later sent for signature
  When the admin undoes IMP-1 within 7 days
  Then 399 documents are removed and the signed one is listed for explicit confirmation

@P20-AT-17
Scenario: LD package round trip places exactly
  Given an LD-EXPORT-1.0 package from workspace W1
  When imported into a new workspace W2
  Then 100% of files are placed by canonical_path with record IDs preserved as references
  And counts equal the source manifest

@P20-AT-18 @NN-26
Scenario: Individual closure honours erasure with notice and retention exceptions
  Given IND_OWNER requests account closure after downloading an export
  Then she is told 48 hours before erasure
  And after erasure she receives a deletion certificate listing eSign evidence retained for the signing route with its retention basis

@P20-AT-19 @NN-19
Scenario: Ops Hub receives counts only
  When an EXIT export completes
  Then OH4 receives job status, file count and bytes
  And no file names, paths or content

@P20-AT-20 @NN-17
Scenario: RM cannot run a full export
  Given OPS_RM with a delivery grant including xpt:export for matter LD-MAT-2026-000045
  When the RM requests FULL_TENANT
  Then the response is 403 LD-XPT-015 and the attempt appears in the client's access log

@P20-AT-21
Scenario: Path rules keep archives openable
  Given an agreement titled "Lease: Shop No. 4/12 \"Ground Floor\" — Jaipur" with a 300-character counterparty name
  When exported
  Then the folder name contains no forbidden characters, the full path is at most 240 characters and ends with the short ID

@P20-AT-22 @NN-42
Scenario: DigiLocker document exported as reference
  Given a PAN document pulled from DigiLocker with no retention purpose
  When exported
  Then "DigiLocker references.xlsx" lists issuer, URI and verification result and no copy of the file is included

# ---- v1.1 additions (IPB-01 portability) ----

@P20-AT-23 @IPB-01 @NN-12
Scenario: Portability drill restores onto alternative adapters
  Given the latest golden company archive and a synthetic tenant
  When the drill restores them onto MinIO and a second PostgreSQL host in staging
  Then the acceptance suite passes, the audit hash chain verifies end to end, and ExitDrillCompleted records timings within the stated RTOs

@P20-AT-24 @IPB-01
Scenario: Vendor SDK import outside connectors fails the build
  Given a module imports "@aws-sdk/client-s3" directly
  When CI runs "ci/ports-not-vendors"
  Then the build fails naming the file and the port to use

@P20-AT-25 @IPB-01
Scenario: Evidence retention survives a storage adapter swap
  Given an evidence pack under Object Lock COMPLIANCE on S3
  When the storage target is switched to a MinIO WORM bucket in the drill
  Then the object's retain-until date is re-applied and a delete attempt before expiry is refused on both adapters

@P20-AT-26 @IPB-01 @OP-7
Scenario: Supabase is database-only and non-production only
  Given APP_ENV=prod with a Supabase connection string
  When the API boots
  Then boot fails with a configuration error
  And in staging a code path calling Supabase Auth or Storage is rejected by the ports lint
```

NN tests added: `NN-11_export_map_coverage`, `NN-11_never_blocked_by_billing`, `NN-12_golden_archive_stability`, `NN-12_storage_keys_independent_of_paths`, `NN-04_no_aadhaar_in_exports`, `NN-10_s63_certificate_present`, `NN-18_tenant_export_checker`, `NN-25_target_residency_policy`, `NN-46_mirror_idempotent`, `NN-19_ops_hub_counts_only`.

---

## 13. Exit gate, deliverables and open items

**Deliverables:** `packages/export` (builder, profiles, naming, manifest, signing), `xpt` schema and APIs, verifier `ld-verify` and loader `ld-load` (Apache-2.0; CLI + desktop build) in `verify/`, storage adapters (Wave 2) certified per Spec §14.3, on-premises agent (signed installer, auto-update, mTLS), import pipeline and review grid, golden workspaces and CI gates, move runbooks (`docs/runbooks/data-moves/*.md`), exit runbook template, help articles.

**Exit gate (core, Wave 1):** export-map coverage 100% for the record types of the Wave 1 phases built so far (P00–P04, P06–P08, P17, P19 core, P21 core; P05 and other Wave 2 types at the full gate); FULL and RECORD exports for Company and Individual profiles; folder/ZIP import with rule mapping, duplicates, review, report and undo; golden-archive diff in CI; PDF/A and render gates; s.63 certificate draft; scenarios AT-01–09, 15–17, 21 green (AT-14 needs AI import classification, which is Wave 2).

**Exit gate (full, Wave 2):** all scenarios green; S3, Azure Blob, GCS, SharePoint/OneDrive, Google Drive, SFTP and agent targets certified; mirror lag p95 ≤ 15 min over 7 days on the pilot tenant; restore test from a customer copy passes; exit rehearsal for a 200 GB synthetic tenant ≤ 24 h; region-move rehearsal (ap-south-1 → ap-south-2) with empty golden diff; usability test (5/5) passed.

**Registered:** export-map entries for `xpt.export_jobs`, `xpt.storage_targets` (metadata only), `xpt.import_jobs` + `import_files` → `99 System Data (CSV and JSON)/Exports, Imports and Storage/` with human `Export and import history.xlsx`; import reports → `99 System Data (CSV and JSON)/Exports, Imports and Storage/Import reports/`; deletion certificates and exit records → `00 Start Here/` of the exit package and `01 Company Profile/Account and Exit/`. Settings `xpt.*` in Appendix R; help keys `hlp.xpt.export_everything`, `hlp.xpt.manifest`, `hlp.xpt.checksum`, `hlp.xpt.verify`, `hlp.xpt.restricted_archive`, `hlp.xpt.byo_storage`, `hlp.xpt.residency`, `hlp.xpt.mirror`, `hlp.xpt.conflict`, `hlp.xpt.import_review`, `hlp.xpt.duplicate`, `hlp.xpt.undo_import`, `hlp.xpt.exit`, `hlp.xpt.deletion_certificate`, `hlp.xpt.s63_certificate`, `hlp.xpt.folder_policy`. Errors `LD-XPT-001`–`LD-XPT-099`. Screens SCR-P20-01–15.

**Demo script:** a founder drags a messy 2,000-file Google Drive folder into LawDocs, fixes 30 proposals and commits; an NBFC legal head connects SharePoint and watches an executed agreement appear in the mirror within minutes; the SRE renames a database column via expand-migrate-contract and the golden diff stays empty; an individual exports everything on her phone and verifies the checksum on a laptop.

| ID | Open item | Owner | Fallback |
|---|---|---|---|
| OI-P20-01 | Appendix Y §Y.11 registers all four profiles (`ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1` — X-08) and proposes `owner_readable`; awaiting Spec v1.2 acceptance | [OWNER] / ecosystem architecture board | Cross-product archives use `ids_only` |
| OI-P20-02 | Microsoft Graph permission names (SharePoint `Sites.Selected`, OneDrive app folder), upload-session limits and residency evidence; Google Drive `drive.file` behaviour on shared drives | P19 lead | Download-only for that provider |
| OI-P20-03 | BSA 2023 s.63 Schedule wording; who signs Part B for SaaS-held records | [COUNSEL] | Draft labelled "for review by your advocate" |
| OI-P20-04 | Companies (Accounts) Rules 2014 r.3(5) current text for India back-up of electronic books | Content team | Treat books as India-only (protective) |
| OI-P20-05 | DigiLocker requester-terms permitted retention purposes | P01 / NeGD | Reference-only exports |
| OI-P20-06 | Price and plan placement of `LD-ADD-BYO` | [OWNER TO SET] with P17 | Business add-on, Enterprise included |
| OI-P20-07 | Retention period for LawDocs' own tax records (CGST s.36; Income-tax Act 2025 equivalents) | [TAX MEMO] | 8 years |
| OI-P20-08 *(v1.1)* | Second production-grade cloud target to keep green (Azure Central India vs GCP asia-south1 vs self-hosted) and its Terraform module owner | CTO | AWS reference + MinIO/CloudNativePG drill only |
| OI-P20-09 *(v1.1)* | Supabase project region and residency attestation for non-prod [VERIFY] | `PLT_SRE` | Self-hosted PostgreSQL in non-prod |
