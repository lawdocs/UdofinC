# Phase P21 — Group Operations, Integrations and Portability
> Paste after `01_MASTER_PROMPT.md` (v3). **Dependencies:** P15 (configuration and settings framework — three-tier settings, rule packs, maker-checker), P16 (Operations Platform, `apps/ops`, `ops`/`mkt` schemas, Equator CRM and `CRM_PORT` adapter `brevo`), P17 (marketing; `MARKETING_PORT` and `SOCIAL_PORT` adapters), P18 (HRMS and payroll, `hr`/`pay` schemas, JML events) complete; P00–P14 complete (P02 DMS, P04 hearings, P06 outcomes, P09 connectors and P13 growth are consumed directly). **Binding appendices:** AC (Workspace Suites, Open Integrations and Data Portability) and AD (Group Companies and Cross-Functional Operations); read with D, F, L, Q, S. Estimated effort: 6 sprints (2-week) for a squad of 8 in two sub-squads — Integrations and Portability (5), Group Operations (3).

---

## 1. Objective and business outcome

Build the layer that lets Equator and its group companies work as one operation without becoming one data pool, connect to the tools staff already use, and let every customer leave with all its data.

| Line | Built here | Business outcome (exit-gate measurable) |
|---|---|---|
| Workspace connector | Extends the `WORKSPACE_PORT` built in P18 (Appendix Z §Z.5.2; Microsoft 365 Graph adapter that works on Business Basic, Google stub, manual IT-desk fallback) with customer connections, the capability resolver and set-up runbook, meeting-class policy, file facade, chat notifications and audit-log ingest | JML from P18 runs against the connection registry and capability matrix built here; a leaver is disabled in ≤ 4 h even when Graph is down; no privileged console role is granted on a SKU without access and device controls; Teams is never used for an Equator-administered proceeding |
| Files and mirror | SharePoint/OneDrive export push and optional one-way working-copy mirror with conflict handling | A chambers tenant's team edits working copies in its SharePoint library; Equator never loses the record, never overwrites an edited copy, and stops within 5 minutes of consent revocation |
| Open integrations | Catalogue with SoR register, field-mapping registry, connector health; Brevo, Adobe Express hand-off, social adapters (OFF until approved), Tally/Zoho Books and payroll file exchange, storage destinations | Any connector can be switched off and its data recovered into Equator-native form within one migration rehearsal |
| Portability | `EQ-EXPORT-1.0` packages for 15 scopes, standard folder and archival BagIt layouts, ZIP64 parts, resumable download, direct push, validation gate; import and migration with dry run and reconciliation | A 25 GB chambers exit export is ready in ≤ 7 days, opens cleanly in Office for the web, and verifies offline; a 50,000-row spreadsheet import reconciles to zero variance |
| Group operations | `grp` schema: entities, brands, billing profiles, policies, admins; shared services with entity partitions; cross-company grants; secondments; shared dashboards and content; GDSA, ICSA and related-party registers; ethical walls; referral model; per-entity exports and audit | A Finbyx employee seconded to Equator's support desk works there under a 90-day grant, is walled off from every Equator case involving Finbyx clients, and her cost is recharged monthly under an active inter-company agreement with its s.188 status recorded |

Rationale: management asked for M365 and SharePoint today with Google possibly later, documents that open in MS Office, self-explanatory export folders, openness to Brevo and Adobe Express, and cross-functional work across Finbyx and Udofin (V3 brief items 3, 5, 7, 11, 13). Jupitice offers no export (Appendix AC §AC.13.1), so portability is also a competitive commitment.

---

## 2. Scope (in / out)

**In scope**
- `WORKSPACE_PORT` extensions (customer connections, meetings, file facade, notifications, audit ingest; the port and its JML operations are built in P18 — Appendix Z §Z.5.2), `STORAGE_PORT` (SharePoint, OneDrive, SFTP, S3-compatible; Google Drive OFF), `ACCOUNTING_PORT` (Tally file, Zoho Books spike), and use of Appendix Z's `PAYROLL_EXCHANGE_PORT` (`generic_csv`) for the integrations catalogue — Appendix AC §AC.2, §AC.11.
- Workspace connection set-up wizard and CS/IT runbook, SKU detection and capability matrix, SKU-sufficiency check at role grant, migration of P18's workspace configuration into `cfg.workspace_connections`, audit-log ingest — AC §AC.2–AC.7 (JML workflow and deletion guard stay in P18, Appendix Z §Z.5.3).
- Meeting classes and the Teams bridge for chambers tenants (flag OFF), ICS for every session, calendar opt-in, chat notifications — AC §AC.8, §AC.10.
- SharePoint/OneDrive export push and working-copy mirror; Google Drive equivalents behind the flag — AC §AC.9.
- Integrations catalogue, system-of-record register, mapping sets and field mappings with dry run, connector health, migration rehearsals — AC §AC.1, §AC.11–AC.12.
- Catalogue registration, SoR rows, mapping sets, connector health, migration rehearsals and AC vendor-contract conformance tests for the Brevo adapters built in P16 (`CRM_PORT`, Appendix X §X.10.2) and P17 (`MARKETING_PORT`), the Adobe Express hand-off and the `SOCIAL_PORT` adapters built in P17 (FR-P17-16) — P21 does not rebuild them; the marketing calendar and approvals are P17's.
- Export engine (`packages/export-spec`, `xpt` schema), all scopes, both layouts, naming/path validators, format conversion, manifest, export certificate, parts, resumable download, push and re-hash, exclusions, redaction profiles, verification suite — AC §AC.13.
- Import and migration engine with templates, mapping, dry run, approval, commit, reconciliation and rollback window — AC §AC.14.
- `grp` schema and entity partition RLS across shared-service schemas; group and entity administration; shared services; cross-company grants; secondment group columns and recharge run; shared artefacts with purposes and field policies; GDSA, ICSA, related-party registers and workflows; ethical walls and attestation; referral model; per-entity exports, audit and consolidated aggregates — Appendix AD.

**Out of scope**
- HR calculations, payroll rule packs, attendance, leave and appraisal (P18); the Operations Platform modules themselves (P16); the marketing calendar, brand governance and campaign workflow (P17); revenue streams and pricing of exports (D3-08 registry; P19, Appendix AB).
- Hearing rooms (P04; unchanged — LiveKit only for Equator-administered proceedings).
- Professional registry functions other than group propagation (P19, Appendix AA; D3-05).
- Third-party backup of M365 mail and files (decision OFF pending CS; AC §AC.3.4).
- Any data flow of Equator case, neutral or allocation data to a group company (NN-38; never built).

---

## 3. Personas and permissions touched

| Role | What changes in this phase | Limits |
|---|---|---|
| `it_admin` | Sets up workspace connections, runs the runbook, maps groups, monitors JML and connector health | Cannot grant platform roles; deletion needs a checker |
| `entity_admin` (new) | Administers one legal entity: settings, admins, brands, billing profiles; approves grants into its partition; approves `GROUP_COMPANY` exports | No access to other entities; no Equator case data |
| `group_admin` | Maintains entities (with CS), shared services, purposes, GDSA/ICSA registers, consolidated aggregates | No record-level data by default; cannot alone approve a grant |
| `group_hr` | Approves secondments with both entities' HR; group HR aggregates | Files only via secondment-linked grants |
| `compliance_officer` (CS) | Related-party register, ICSA s.188 status, walls, attestation campaigns | — |
| `security_lead` (Appendix AE §AE.1.1) | SKU-sufficiency exceptions (≤ 90 days, compensating control) | Cannot approve own exception |
| `dpo` (per entity) | GDSA privacy terms, restricted grants second approval, export approvals for DSRs, erasure propagation | — |
| `finance_ops`, `accounts_maker`, `accounts_checker` | Accounting exports, recharge runs and checks, ledger maps | Maker ≠ checker (NN-36) |
| `hr_manager`, `payroll_checker` | Employee-file and payroll exports; secondments | Employing entity only |
| `department_head`, `ops_director` | Department exports; delegated grant approvals in their entity | — |
| `marketing_manager` | Brevo and social adapter settings within bounds | Flags need `legal_reviewer`/DPO |
| `chambers_owner`, `chambers_admin` | Chambers exports, SharePoint mirror, Teams bridge request | Bridge and mirror flags need Equator checker |
| `enterprise_admin` (Appendix S) | Enterprise exports, mirror, storage destinations | — |
| `registrar` | `CASE_FULL` exports (maker-checker) | Exclusions still apply |
| Every user (`party`, `counsel`, neutral, `employee`) | Self exports (`USER_SELF`, `PARTY_IN_CASE`, `NEUTRAL_PRACTICE`, `EMPLOYEE_SELF`); ICS; calendar opt-in; chat opt-in | Entitlement filter and redaction profile |
| `internal_auditor` | Read-only entity audit views and grant access reports | Time-boxed engagement |

SoD additions (Appendix S §6.7 extended): `entity_admin` cannot approve a grant it requested or holds; `panel_manager` and allocation administrators cannot hold roles in Finbyx or Udofin (EW-03); export maker ≠ checker; mapping-set maker ≠ checker for tier G sets; recharge maker ≠ checker.

---

## 4. Functional requirements

### 4A. Workspace connector (Appendix AC §AC.2–AC.8, §AC.10)

**FR-P21-01 — `WORKSPACE_PORT` extensions and `STORAGE_PORT`.** Extend the port built in P18 (FR-P18-13; Appendix Z §Z.5.2) to the full interface in AC §AC.2.2 — `detectSkus`, `ensureGroup`, `createMeeting`/`updateMeeting` with meeting classes, the file facade over `STORAGE_PORT`, `postNotification`, `pullAuditLogs` — in the `m365_graph` adapter (Graph v1.0, certificate credentials), keeping `google_workspace` OFF and `manual_it_desk` as fallback; implement `STORAGE_PORT` and `ACCOUNTING_PORT` and register them, together with P17's `MARKETING_PORT` and `SOCIAL_PORT`, in the master §4.4 list and the Appendix D §D.0.4 CHECK (X-63). *Acceptance:* in-memory fakes pass the port contract suite; adapter contract tests run nightly against a Microsoft developer tenant; P18 JML tests still pass unchanged.

**FR-P21-02 — Two connection kinds.** `cfg.workspace_connections` rows of kind `workforce` (an entity's own tenant) and `customer` (a chambers or enterprise tenant's workspace) with separate app registrations (`eq-hrms-provisioner`, `eq-ops-collab`, `eq-tenant-connector`), separate secrets and no cross-use. Forbidden application permissions (`Files.ReadWrite.All`, `Sites.ReadWrite.All`) fail CI on the Entra manifests. *Acceptance:* a `customer` connection cannot be selected by HRMS JML; manifest scan test.

**FR-P21-03 — Set-up wizard and runbook.** SCR-P21-02 guides the CS and IT admin through the 15 steps of AC §AC.7 (SKU confirmation, data location, domains and UPN pattern, app registrations, consent, `Sites.Selected` grant, groups, Teams access policy, security defaults, mailbox quotas, transcript decision, audit ingest, backup decision, self-test, JML switch-on), storing evidence hashes on the connection row. *Acceptance:* JML automation cannot be switched ON until steps 1–12 and 14 are complete.

**FR-P21-04 — SKU detection and capability matrix.** `detectSkus` reads `GET /subscribedSkus`; the result plus `cfg.workspace_capability_matrix` (seeded from AC §AC.3.2) resolves `WorkspaceCapabilities`; the UI hides actions whose capability is false and shows the fallback. The CS-confirmed SKU and the detected SKU are both stored; a mismatch opens a task. Management's "Business Starter" label is shown with the note "Microsoft has no plan of this name; detected plan: {sku}". *Acceptance:* AC-T01.

**FR-P21-05 — SKU-sufficiency rule on detected capabilities.** Appendix Z's rule (`HR_WORKSPACE_SKU_INSUFFICIENT`) now reads the capability resolver: at every grant of a privileged console role (AC §AC.3.3 list) the membership service checks the grantee's workspace capabilities; without Conditional Access plus device management, the grant fails with `HR_WORKSPACE_SKU_INSUFFICIENT` unless an unexpired exception (≤ 90 days, compensating control recorded) exists. Collector `workspace_sku_role_check` runs daily. *Acceptance:* AC-T03.

**FR-P21-06 — JML on the connection registry.** Migrate P18's workspace configuration into `cfg.workspace_connections` (kind `workforce`) and point P18's `WorkspaceJmlWorkflow` (Appendix Z §Z.5.3) at the capability resolver, so that SKU rules, the manual-desk fallback and the leaver ≤ 4 h rule (X-57) use the detected and confirmed SKUs; JML automation for a connection cannot be ON (`tenant.hr.workspace.jml_automation`) until the runbook steps of FR-P21-03 are complete. *Acceptance:* AC-T02; `jml_sla_report` stays green through the migration.

**FR-P21-07 — Audit-log ingest.** `WorkspaceAuditIngestJob` (hourly) pulls Entra sign-in and audit logs and the Microsoft 365 unified audit log for every `workforce` connection into `eq-log-archive` (Object Lock, India, 400 days) as `NormalisedEvent`s; gaps raise a High alert. *Acceptance:* oldest-object probe shows ≥ 180 days after six months (CERT-In).

**FR-P21-08 — Meeting classes and the Teams bridge.** `createMeeting` accepts only the meeting classes in AC §AC.8.3; Equator-administered proceedings, mediation, conciliation, negotiation, caucus and sealed matters have no class and are refused; the chambers Teams bridge requires flag `tenant.chm.meetings.teams_bridge` (G), host tenant = administering body (never a party: `OPS_MEETING_HOST_TENANT_IS_PARTY`), recording/transcription-off attestation, per-session all-party consent `online_platform_teams`, lobby on, attendance recorded in Equator. *Acceptance:* AC-T04, AC-T05.

**FR-P21-09 — ICS and calendar opt-in.** Every session invitation carries an ICS with `UID` = session ID and content-minimised subject; staff may opt in to calendar sync (delegated `Calendars.ReadWrite`); updates and cancellations flow one way; calendar-side edits are ignored and flagged. *Acceptance:* rescheduling a session updates the ICS sequence and the synced event.

**FR-P21-10 — Chat notifications.** Optional per user and per channel; templates `notify.chat.*` only; lint `NOTIFICATION_CONTENT_MINIMISED`; Teams endpoint configured by the tenant admin (mechanism confirmed at spike). *Acceptance:* a notification for a mediation session contains no party name or case content.

**FR-P21-11 — Workforce meeting data is not performance data.** CI test `NO_MEETING_DATA_IN_APPRAISAL` blocks any HRMS scoring source from workspace meeting, presence or transcript data (NN-35). *Acceptance:* test present and green.

### 4B. Files: export push and working-copy mirror (AC §AC.9)

**FR-P21-12 — Export push.** `ExportPushWorkflow` pushes a ready export to a SharePoint library, OneDrive folder, SFTP or S3-compatible destination through `STORAGE_PORT` (upload sessions above 250 MB), then re-hashes a sample (≥ 2% or ≥ 50 files) and records `migration_verified`; a mismatch sets `XPT_PUSH_VERIFY_FAILED` and the delivery is marked failed. *Acceptance:* AC-T16.

**FR-P21-13 — Working-copy mirror.** `SharePointMirrorWorkflow` (event-driven, one way) mirrors eligible documents (AC §AC.9.2) to `/{Library}/Equator/{CaseFolder}/{ExportFolder}/{FileName}` with the library columns of AC §AC.9.3, the `EquatorStatus` property and rendition banners; flags `tenant.chm.sharepoint_mirror` / `tenant.ent.sharepoint_mirror` (G, OFF). Mediation and conciliation mirrors need consent `working_copy_mirror` from every party. *Acceptance:* ineligible items (caucus, `NEUTRAL_ONLY`, sealed, recordings) are never mirrored (AC-T13 extended to the mirror).

**FR-P21-14 — Conflicts and return of working files.** Change detection by eTag (and delta where available) per AC §AC.9.4: never overwrite an edited working copy (side-by-side `_EQ-vNN`), rename on withdrawal or supersession, record user deletions, and "File back to Equator" creates a new draft or version under Appendix L rules. *Acceptance:* AC-T06.

**FR-P21-15 — Disconnection and erasure propagation.** Revocation detected on `401/403` or flag OFF stops pushes within 5 minutes, deletes stored tokens and shows the disconnection banner; erasure requests notify the tenant's DPO contact of mirrored items (`xpt.erasure_propagations`). *Acceptance:* revocation test shows zero pushes after 5 minutes.

### 4C. Open integrations (AC §AC.1, §AC.11–AC.12)

**FR-P21-16 — Integrations catalogue and enable gate.** `cfg.integration_catalogue` seeded from AC §AC.11.1 and shown on SCR-P21-05; enabling a connector requires a `cfg.system_of_record` row for each data category it touches (`CFG_SOR_UNDECLARED`), an approved mapping set (`CFG_MAPPING_MISSING`), the transfer-register row where data leaves India, the provider's DPA reference where personal data is involved, and the named approver of its flag. *Acceptance:* AC-T07 (fallback for every row).

**FR-P21-17 — Field-mapping registry.** Mapping sets and field mappings (AC §AC.12.2) with transforms, PII class, validation, versioning and status; tier G for identity, consent and money fields (maker-checker), tier T otherwise; dry run on 20 sample records before approval; connectors run against a pinned approved version. *Acceptance:* changing an approved mapping creates a new version; in-flight syncs keep the pinned version.

**FR-P21-18 — Connector health.** `ConnectorHealthProbeJob` every 5 minutes computes the signals in AC §AC.12.3, emits `equator.cfg.connector.health_changed.v1`, pages on red and renders SCR-P21-04 tiles with 30-day history. *Acceptance:* AC-T23.

**FR-P21-19 — Migration rehearsals.** `cfg.migration_rehearsals` with runbook per connector (export from vendor → import to Equator-native or alternate → reconciliation); due date reminders; health amber at 366 days and red above 400 (L). *Acceptance:* rehearsal record with reconciliation report attached for each enabled connector before P14 gate.

**FR-P21-20 — Brevo in the catalogue.** The `CRM_PORT` adapter `brevo` (built in P16, Appendix X §X.10.2; CRM-object sync flag `tenant.ops.connectors.brevo_crm_sync.enabled`) and the `MARKETING_PORT` adapter `brevo` (built in P17, FR-P17-24), both behind the connector flag `mkt.brevo.enabled` (AC §AC.17), are registered in `cfg.integration_catalogue` with SoR rows (CRM in `ops.crm_*`, X-51; consent in `core.consent_records`), mapping sets seeded from X §X.10.2, connector health and a migration rehearsal (`CrmMigrationWorkflow`, X §X.10.3). P21 adds the one account-level request budget shared by both adapters (`tenant.mkt.brevo.max_requests_per_hour`, default 80), the nightly contact and deal export to a business-database snapshot, the `BREVO_EU` transfer-row gate, and contract tests proving the AC §AC.11.2 compensating webhook controls (bearer token + IP allow-list + inbox dedupe + **re-fetch before applying consent events**) and two-way consent sync within 15 minutes; `mkt.brevo.sms_whatsapp.enabled` stays OFF. *Acceptance:* AC-T08, AC-T09.

**FR-P21-21 — Adobe Express hand-off and social adapters in the catalogue.** The hand-off (design link and asset upload with hash; `published_via` and operator-confirmed `post_url`; Embed SDK behind `mkt.adobe_embed.enabled`, OFF) and the `SOCIAL_PORT` adapters `linkedin_cm`, `meta_graph` (per-account 24-hour cap `tenant.mkt.social.ig_daily_cap`, default 50), `x_v2` (`tenant.mkt.social.x_monthly_budget_usd`), `youtube_data` (100 uploads/day ceiling) and `manual_handoff` are built in P17 (Appendix Y; FR-P17-16); P21 registers them in the catalogue with fallback, SoR rows (AC §AC.12.1) and health probes, each flag OFF until its access is granted. *Acceptance:* with all adapters OFF, a post can still be published and recorded through `manual_handoff` (AC-T07).

**FR-P21-22 — Accounting exports.** `ACCOUNTING_PORT` file adapter for Tally and an API spike for Zoho Books: invoices, receipts, credit notes, payouts/TDS, payroll journals and inter-company charges from closed periods only, with ledger maps per entity, hashed files and re-export variance (`XPT_ACCOUNTING_PERIOD_REEXPORT_REQUIRED`). One books SoR per entity declared in `grp.legal_entities.books_sor`. *Acceptance:* AC-T20.

**FR-P21-23 — Payroll file exchange.** `PAYROLL_EXCHANGE_PORT` generic import/export templates (employee master, attendance and leave summaries, pay register, statutory-dues summary, journals); bank-advice files encrypted and released by maker-checker; an entity declaring an external payroll SoR imports pay registers read-only. *Acceptance:* imported pay register cannot be edited in Equator.

### 4D. Portability — export packages (AC §AC.13)

**FR-P21-24 — Export engine.** `packages/export-spec` implements `EQ-EXPORT-1.0`: taxonomy (AC §AC.13.4–AC.13.6), both layouts (standard folder package; archival BagIt bag), naming and path validators with the deterministic shortening algorithm (AC §AC.13.7), format rules and pinned converters (AC §AC.13.8), manifest CSV/JSON, `bag-info.txt`, checksums SHA-256 and SHA-512, export certificate signed with Equator's DSC, `verify_package.py` and `verify_audit.py` tools. *Acceptance:* AC-T10, AC-T11.

**FR-P21-25 — Scopes, approvals and step-up.** All 15 scopes of AC §AC.13.3 with their requesters, maker-checker rules, aal2 or aal2-pr step-up and target times; `POST /v1/me/exports` aliases `USER_SELF` (D3-41). *Acceptance:* each scope has a role test (permitted and refused).

**FR-P21-26 — Entitlement filter, exclusions and redaction.** The item resolver applies RLS-equivalent entitlement for the requester, the exclusion table (AC §AC.13.11) and the redaction profile (AC §AC.13.12); an **independent second policy pass** in `validating` re-checks exclusions (`XPT_EXCLUSION_RULE_VIOLATION` = Critical incident). Documents are exported as served; redaction touches generated data only. *Acceptance:* AC-T13, AC-T14.

**FR-P21-27 — Signed originals and audit trails.** Signed PDFs are copied byte-for-byte from the evidence bucket and verified against `core.evidence_ledger`; renditions are separate PDF/A-2b files; ESP audit trails, certificate chains, eStamp certificates and s.63(4) certificates are included; the audit extract with anchors verifies offline. *Acceptance:* AC-T12.

**FR-P21-28 — Large exports and delivery.** ZIP64 always with UTF-8 names; parts above `tenant.xpt.part_max_gb` split by folder; presigned links ≤ 5 minutes per click; HTTP range resume; web download manager with per-part hash check; mobile "send links to my email"; regeneration after expiry; exit packages regenerable for 90 days after cancellation. *Acceptance:* AC-T15, AC-T22.

**FR-P21-29 — Verification suite.** CI and nightly checks of AC §AC.13.13 (OOXML validation, PDF/A validation, round-trip open, names and paths, manifest completeness, signed-original identity, audit verification, CSV checks); quarterly manual Office test with evidence. *Acceptance:* AC-T17.

**FR-P21-30 — Billing never blocks exit.** Export scopes for self, DSR and exit are never blocked or priced by billing state (Appendix O item (i)); periodic enterprise exports beyond plan are priced only through the revenue registry and never block legal-rights downloads. *Acceptance:* AC-T24.

**FR-P21-44 — Estimate, presets, progress, resumable build and download, test-open and verify.** *(v3.1; Appendix AC §AC.13.3 "Pre-flight estimate and presets" and §AC.13.15)*
- **Estimate:** SCR-P21-08 calls `POST /v1/exports:estimate` (same body as `POST /v1/exports`, no side effects) and shows counts and size per top-level folder, parts at `tenant.xpt.part_max_gb`, estimated time to ready (trailing 30-day p50 for the scope), excluded-item counts by reason code without content, approval and step-up needed with the checker role, and the destination. Labelled "estimate"; never blocks a request.
- **Presets and schedules:** named presets (`xpt.export_presets`, ≤ 10 per user) and, where the plan includes periodic exports, monthly or quarterly schedules (`xpt.export_schedules`, `tenant.xpt.schedules`); sensitive scopes still pass maker-checker on every scheduled run.
- **Progress:** `xpt.export_runs.progress` (phase, items, bytes, parts, `eta_at`, last checkpoint); `GET /v1/exports/{id}/progress` and the SSE stream `GET /v1/exports/{id}/progress:stream` (≤ one push per 5 s); phase stepper on SCR-P21-09; notification on ready or failure without file content or a download link in the message body.
- **Resumable build:** `ExportBuildWorkflow` checkpoints (`xpt.export_checkpoints`) after each top-level folder, case folder and part; writes are idempotent on `(export_run_id, path)` with SHA-256; a crashed worker resumes on the same pinned snapshot; an unreadable snapshot restarts under a new run ID recorded in the README.
- **Early parts and resumable download:** each part passes the gate on its own and is downloadable early when `tenant.xpt.early_part_download` is ON; parallel parts (`platform.xpt.download.parallel_parts`, 3), range resume, automatic retries (`platform.xpt.download.auto_retries`, 3), link renewal within the availability window with step-up only (after it `XPT_LINK_RENEWAL_NOT_ALLOWED`, 410, with "request again" from the preset), per-part hash check recorded in `xpt.export_deliveries.client_verified`.
- **Test-open:** `TestOpenActivity` opens a stratified sample (`tenant.xpt.test_open.sample_pct`, 5%, minimum 20, maximum 500 files) in the pinned LibreOffice build with the AC §AC.13.13 validators; signed originals are hash-checked only; one regeneration, then "Files that may need repair"; above `tenant.xpt.test_open.max_fail_pct` (2%) the run fails with `XPT_TEST_OPEN_FAILED` (500) and a Sev-3 incident; results in `xpt.test_open_results` and printed in `00_README.pdf` and the certificate.
- **Verify:** SCR-P21-31 `/exports/verify` checks an extracted folder or ZIP against `manifest.json` with in-browser streaming SHA-256; no file bytes leave the browser; `verify_package.py` stays the offline route.
- **KPIs:** time to ready p50/p95 per scope; first-pass validation ≥ 98%; test-open failure ≤ 0.5% of sampled files; download completion ≥ 95% within the window; resumed-build share — on SCR-P21-04.
- *Acceptance:* AC-T25…AC-T29 (§12).

### 4E. Import and migration (AC §AC.14)

**FR-P21-31 — Import engine.** Templates per object, quarantine and scan, mapping sets for spreadsheets, other ODR tools, HubSpot/Zoho/Brevo, payroll and ledger opening balances, and Equator packages; dry run with per-row results and duplicate detection; approval per AC §AC.14.2; commit in idempotent batches through module services; reconciliation reports with control totals; soft rollback window for CRM, contacts, tickets and configuration only. *Acceptance:* AC-T18.

**FR-P21-32 — Imported-record integrity.** `legacy_import` ruleset pin and banner, `imported` audit events with source hashes, chain of custody from import, consent provenance or `no_marketing_consent`, and refusal of Bar Council or institute roll imports (`XPT_IMPORT_SOURCE_FORBIDDEN`). *Acceptance:* an imported contact without proof of consent is suppressed from marketing.

### 4F. Group structure and administration (Appendix AD §AD.2–AD.4, §AD.13)

**FR-P21-33 — `grp` schema and grant-aware entity scope.** Create the `grp` DDL of AD §AD.14 with view `grp.companies` and helper `grp.active_grant_entities`; migrate `hr.legal_entities` IDs into `grp.legal_entities` and add the foreign key (AD-R1); keep Appendix Z's `rls.enable_entity_rls` / `app.entity_ids` / `entity_scope` and Appendix X's `ops_company_isolation` (AD-R2) and add the policy-engine step that computes the entity list per request from module-matching grants; widen the entity-scope CI catalogue to `cfg` entity tables, `xpt` and `dir` consumer tables; CI `GROUP_SHARE_SCOPE`. *Acceptance:* AD-T01, AD-T03, AD-T15.

**FR-P21-34 — Entities, brands, billing profiles, policies, admins.** Seed EQR and ICOPC, placeholders for Finbyx, Udofin and LawDocs (particulars `[VERIFY — open: CS]`); CRUD with CS approval for creation and particulars; `entity_admin` and `group_admin` per AD §AD.3; policy adoption records; workspace topology setting. *Acceptance:* `group_admin` sees no record-level data of any entity without a grant.

**FR-P21-35 — Shared services.** Catalogue (AD §AD.4.1) with provider entity, processing role and processing agreement; Operations Platform workspaces per entity; HRMS and registry consumers configured. *Acceptance:* deactivating an entity's consumption hides its workspace from shared-service UIs and stops new writes.

### 4G. Cross-company grants and ethical walls (AD §AD.5, §AD.10)

**FR-P21-36 — Grant lifecycle.** Request, approval (target entity's approver; second approver for restricted purposes), activation, entity switcher and banner, access logging with `grant_id` and purpose, weekly digest to approver, T-7 notice, access ending at `expires_at` on every request (the time window is tested by `grp.active_grant_entities()`), status job every minute and session end within 60 s, revocation, leaver/mover revocation, GDSA-suspension cascade, limits of AD §AD.5.4. **v3.1 workflow:** pre-filled requests (templates, last grant, renewal) proposing the narrowest modules and fields; approver must belong to the target entity (`GRP_GRANT_APPROVER_NOT_TARGET`); approval SLA 3 working days with reminder at day 2 and escalation at day 3; undecided requests `lapsed` at 10 days (`GRP_GRANT_LAPSED` on late approval; one-click re-submit); expiry notices at T-14, T-7 and T-1 with an access-report summary and one-click renew as a new request narrowed to what was used; dormant grants (no use for 30 days) confirmed or revoked; default duration 90 days, group cap 365 days and role maxima (365 only for shared-desk roles) per AD §AD.5.2. *Acceptance:* AD-T02, AD-T03, AD-T05, AD-T19, AD-T20, AD-T23. *(v3.1)*

**FR-P21-37 — Ethical walls.** Client-relationship hashes and user exposures (AD §AD.10.2) loaded from CRM ownership, collections queues, onboarding projects and support assignments; EW-01 to EW-07 enforced at case assignment, grant request, membership grant, neutral disclosure and case disclosure; annual attestation campaign; breach review queue. *Acceptance:* AD-T06, AD-T07, AD-T16.

### 4H. Employment, related parties and charges (AD §AD.6, §AD.9)

**FR-P21-38 — Secondments and cross-entity employment guard.** Additive group columns on Appendix Z's `hr.secondments` (AD-R3), template `HR-SEC-01` with e-sign, lifecycle of AD §AD.6.3 creating a grant template (not access), `GRP_DUPLICATE_EMPLOYMENT` extending Z's one-active-employment-per-PAN rule across entity tenants, and recharges from Z's `hr.assignments.allocation_pct` or timesheet actuals (disclosed, purpose-limited — NN-35). **v3.1:** cross-company assignment requests (`grp.assignment_requests`, AD §AD.6.5) from the host manager with allocation ≤ 100%, wall pre-check, ICSA check, employer decision SLA 5 working days (reminder day 3, escalation day 5, `lapsed` day 10), acceptance creating a pre-filled secondment draft, planned assignments and a grant template, and lapse if unsigned by start + 10 working days; secondment states `scheduled` and `cancelled`, signature reminders, T-30/T-7 end reminders and automatic end at 23:59 IST on `ends_on`. *Acceptance:* AD-T08, AD-T09, AD-T21. *(v3.1)*

**FR-P21-39 — Related parties, ICSAs and recharges.** Related-party register with nightly candidate detection from director data; ICSA register and `RelatedPartyApprovalWorkflow` (CS review, s.188 status, Board and shareholder references, AOC-2 flag, tax review); `IntercompanyChargeRunWorkflow` monthly with maker-checker, GST lines, invoices in the provider's billing profile, append-only after invoicing; migration of the Institute-referral approval record (X-29) into the register. *Acceptance:* AD-T10, AD-T11, AD-T12.

### 4I. Sharing, GDSA and referrals (AD §AD.7, §AD.8, §AD.11, §AD.12)

**FR-P21-40 — Shared artefacts and purposes.** Purpose catalogue (tier G), shared dashboards, reports, saved views, KB articles, templates and brand assets with server-side field policies, k-suppression (≥ 5; outcome cells ≥ 10), header labels, no drill-through without a grant, expiry; Equator case-related dashboards shareable only as aggregates and never by group-client organisation. *Acceptance:* AD-T13.

**FR-P21-41 — GDSA registry.** Structured GDSA with role matrix, purposes, field allow-list, lawful basis, 72-hour propagation SLA, onward-transfer ban, s.188 link, signatures, lifecycle and annual review; grants and personal-data artefacts require an active GDSA listing the purpose; registry propagation reconciliation daily. *Acceptance:* AD-T04, AD-T18.

**FR-P21-42 — Referrals.** Referral types and lifecycle of AD §AD.11 with mandatory party authorisation, recorded professional choice, group-relationship disclosure, no fees or rewards to professionals, and the X-64 rule that Equator never pushes case data to a group company. *Acceptance:* AD-T14, AD-T15.

**FR-P21-43 — Per-entity exports, audit and consolidated reporting.** `GROUP_COMPANY` export scope limited to the entity's partition; entity audit views; `grant_access_report` collector; `grp_consolidated` aggregate views for the Board pack. *Acceptance:* AD-T17.

---

## 5. Workflows and state machines

### 5.1 Export run (`xpt.export_runs.status`; AC §AC.13.14)
```
requested ──(scope needs checker)──▶ awaiting_approval ──(checker ≠ maker, step-up)──▶ approved
requested ──(self scope)──────────────────────────────────────────────────────────────▶ approved
approved ─▶ snapshotting ─▶ building ─▶ validating ──gate pass──▶ ready ─▶ delivered ─▶ expired
                                          └──gate fail──▶ failed (Critical if hash mismatch or exclusion violation)
awaiting_approval ─▶ rejected ; any pre-ready state ─▶ cancelled (requester or approver)
```
Gate: package/bag valid; signed originals equal ledger hashes; audit extract verifies; names and paths pass; independent exclusion pass. Timers: `ready` → `expired` at 7 days (bucket lifecycle); exit packages regenerable 90 days after cancellation.

### 5.2 Cross-company grant (`grp.cross_company_grants.status`; AD §AD.5)

| From | To | Trigger / guard |
|---|---|---|
| — | `requested` | Request passes role, purpose, module, GDSA, duration, SoD and wall checks |
| `requested` | `approved` | Target approver (≠ requester, ≠ grantee); second approver if restricted; aal2-pr |
| `requested` | `rejected` | Approver decision with reason |
| `requested` | `lapsed` | Not decided within `group.grants.request_lapse_days` (default 10) after reminder (day 2) and escalation (day 3) *(v3.1)* |
| `approved` | `active` | `starts_at` reached; wall check re-run |
| `active` | `expiring` | T-7 days (notices also at T-14 and T-1, *v3.1*) |
| `active`/`expiring` | `expired` | `expires_at`: access ends at once (time window checked per request); status job every minute; sessions end ≤ 60 s *(v3.1)* |
| `active`/`expiring` | `revoked` | Approver, manager, DPO, `group_admin`, `compliance_officer`, leaver/mover event; or reason `dormant` after 30 days' non-use and no confirmation within 5 working days *(v3.1)* |
| `active`/`expiring` | `suspended` | GDSA suspended; attestation overdue |
| `suspended` | `active` | Cause cleared before `expires_at` |

### 5.3 Workspace JML (canonical: Appendix Z §Z.5.3, built in P18; restated for the connector)
`WorkspaceJmlWorkflow` per employee: `J1 provision → poll mailbox → licence → groups → credential to personal channel → done`; `M1 diff → apply`; `L1 suspend + revoke sessions (≤ 4 h; manual-desk escalation at T+60 min if connector down) → L2 convert to shared + transfer files + remove licence (T+1) → L3 delete at T+delete_after_days if guard passes`. Every step emits an `hr.jml_events` row and an audit event; signals allow HR to pause L3 when a hold appears.

### 5.4 Import batch (`xpt.import_batches.status`; AC §AC.14.2)
`uploaded → scanned → mapped → dry_run_complete → awaiting_approval → approved → committing → committed → reconciled → closed`; side states `rejected`, `failed`, `rolled_back` (allowed only for CRM, contacts, tickets, configuration within the rollback window). `reconciled → closed` requires zero variance or an approved variance explanation (`XPT_IMPORT_RECONCILIATION_VARIANCE` otherwise).

### 5.5 Mirror item (`cfg.mirror_items.state`; AC §AC.9.4)
`pending → mirrored → (updated) → mirrored`; `mirrored → conflict` when eTag differs on a new Equator version; `conflict → mirrored` when the user resolves (keeps one, or files back); `mirrored → withdrawn_label | superseded_label` on DMS events; `mirrored → deleted_in_workspace`; any → `disconnected` on revocation.

### 5.6 GDSA (`grp.data_sharing_agreements.status`; AD §AD.8)
`draft → legal_review → signature → active → suspended ⇄ active → terminated`. Suspension cascades to dependent grants and shared artefacts; termination triggers deletion tasks at recipients and a deletion certificate.

### 5.7 Inter-company agreement and charge (AD §AD.9)
ICSA: `draft → cs_review → approvals → active → expired | terminated`. Charge: `draft → checked → invoiced → settled`; `invoiced → reversed` only by a reversing entry (append-only).

### 5.8 Referral (AD §AD.11.3)
`draft → authorised → sent → accepted | declined → in_progress → closed`; `withdrawn` by the party before `accepted`.

### 5.9 Secondment (AD §AD.6.3)
`draft → pending_signatures → scheduled → active → extended → ended`; `draft | pending_signatures | scheduled → cancelled` (reason); `pending_signatures → draft` when unsigned after 15 working days *(v3.1)*.

### 5.10 Cross-company assignment request (AD §AD.6.5) *(v3.1)*
`requested → employer_review → (declined | accepted) → secondment_drafted → closed`; `requested | employer_review → withdrawn` by the requester; `employer_review → lapsed` at day 10; `accepted → lapsed` if the secondment is unsigned by `start_on` + 10 working days.

---

## 6. Screens and UX (web + mobile)

Common rules: Appendix C and P16 design system; skeleton, empty, error and success states; WCAG 2.2 AA; en/hi at launch; tier badges (L/G/T) and "who can change this / approval needed" on every setting (NN-33); entity banner on every screen when acting under a cross-company grant ("Working for {entity} · purpose {label} · until {date}").

| ID | Route (app) | Persona | Purpose and key components | Notable states | Mobile |
|---|---|---|---|---|---|
| SCR-P21-01 | `ops /settings/workspace` | `it_admin`, CS | Connection list (workforce/customer), suite, detected SKU vs confirmed SKU, data location, health tile | Mismatch banner; consent revoked | read |
| SCR-P21-02 | `ops /settings/workspace/{id}/setup` | `it_admin`, CS | 15-step runbook checklist with evidence upload, "Test connection", JML switch | Steps incomplete → switch disabled | — |
| SCR-P21-03 | `ops /settings/workspace/{id}/capabilities` | CS, `it_admin` | Capability matrix for detected plan; upgrade guide (AC §AC.3.4); SKU rules editor; exceptions list | Exception expiring | — |
| SCR-P21-04 | `ops /integrations/health` | `it_admin`, `ops_director` | Connector tiles (auth, error rate, lag, throttles, drift, rehearsal age, credential age), 30-day history, incidents | Red/amber | read |
| SCR-P21-05 | `ops /integrations/catalogue` and tenant `/settings/integrations` | tenant admins | Catalogue rows (AC §AC.11.1): what moves, SoR, fallback, flag and approver; enable wizard with gates | Gate failures explained | — |
| SCR-P21-06 | `/settings/integrations/{connector}/mappings` | tenant admin, `compliance_officer` | Mapping-set editor, transforms, PII class, dry run on 20 samples, submit for approval, version history | Tier G needs checker | — |
| SCR-P21-07 | `/settings/integrations/sor` | tenant admin | System-of-record register per data category | Undeclared category warnings | — |
| SCR-P21-08 | `/exports/new` | all users | Scope picker filtered by role; layout; destination (download / SharePoint / OneDrive / SFTP / S3); redaction profile; preview of folders and counts; exclusions summary; step-up. *v3.1:* pre-flight estimate panel (sizes, parts, time to ready, exclusion counts, approver) and saved presets (FR-P21-44) | Approval required | yes (request, status) |
| SCR-P21-09 | `/exports` | all users; approvers | Runs with status timeline, approvals queue, download manager with parts and resume, push status and re-hash result. *v3.1:* phase stepper with progress and ETA, early parts, link renewal, per-part verification; saved view "Department exports" (scope `OPS_DEPARTMENT`) replaces SCR-P16-40 (Appendix AG §AG.0.5 #4) | Failed gate details | yes (status, links by email) |
| SCR-P21-10 | `/exports/{id}/certificate` | requester | Export certificate, manifest download, verification instructions | — | yes |
| SCR-P21-11 | `/imports` | tenant admin, `ops_manager`, `hr_manager` | Template downloads, upload, mapping, dry-run report (per-row), approve, commit progress, reconciliation | Variance blocks close | — |
| SCR-P21-12 | `/settings/files/mirror` | `chambers_owner`, `enterprise_admin` | Mirror target library, columns check, eligibility rules, consent status for mediation matters, conflicts list, disconnect | Conflict items | read |
| SCR-P21-13 | case page → "Working copies" panel | case-side users | Mirror status per document, "File back to Equator", conflict resolution | Conflict | read |
| SCR-P21-14 | `/settings/meetings` (chambers) | `chambers_owner` | Teams bridge request: host-tenant check, attestation upload, meeting classes, consent template | Equator checker pending | — |
| SCR-P21-15 | `/me/notifications/chat` | staff | Chat channel opt-in, calendar opt-in | — | yes |
| SCR-P21-20 | `ops /group` | `group_admin`, CS | Entities, brands, billing profiles, policies, admins, workspace topology, shared services | Particulars unverified | read |
| SCR-P21-21 | `ops /group/grants/new` and `/me/grants` | any staff | Request grant: target entity, role, purpose, modules, field preview ("you will see these fields"), dates; my grants with countdown | Wall or SoD block | yes (view, approve) |
| SCR-P21-22 | `ops /group/grants/approvals` | target approver, DPO | Approval queue with field preview, wall-check result, GDSA link; access report per grant | Restricted → second approver | yes (approve with step-up) |
| SCR-P21-23 | `ops /group/walls` | `compliance_officer` | Client-relationship hashes, user exposures, conflicts, breach queue, attestation campaign | Overdue attestations | — |
| SCR-P21-24 | `ops /group/agreements` | CS, `dpo`, `finance_ops` | GDSA and ICSA registers, related-party register, s.188 status, AOC-2 extract | Pending approvals | read |
| SCR-P21-25 | `ops /group/charges` | `accounts_maker`, `accounts_checker` | Monthly recharge run, basis lines, check, invoice, variance notes | Maker = checker blocked | — |
| SCR-P21-26 | `ops /group/secondments` | HR of both entities, `group_hr` | Secondment list, letter generation and e-sign, grant template, allocation codes | Signatures pending | read |
| SCR-P21-27 | `ops /group/shared` | owners, recipients | Shared artefacts: share wizard (entities, purposes, field policy, k, refresh, expiry), recipients' view | Field blocked | read |
| SCR-P21-28 | case page → "Next steps" and `/referrals` | party, regulated tenant signatory | Execution and registration signposts; referral authorisation with disclosure; professional choice list (alphabetical/seeded-random, no ranking) | Authorisation pending | yes |
| SCR-P21-29 | `ops /group/consolidated` | `group_admin` | Aggregate Board pack (k-suppressed) | Suppressed cells | read |
| SCR-P21-30 | `ops /group/assignment-requests` *(v3.1)* | Host `department_head`, employing HR and line manager, employee (view and comment) | Request form (employee or role profile, time %, dates, purpose, modules) with live allocation meter, wall pre-check and ICSA status; decision queue with SLA countdown; "Create secondment draft" on acceptance | Lapsing soon; allocation over 100% blocked | yes (view, decide) |
| SCR-P21-31 *(v3.1)* | `/exports/verify` | any recipient (no sign-in needed) | Drop an extracted folder or ZIP; in-browser streaming SHA-256 against `manifest.json`; per-file result list; nothing uploaded (AC §AC.13.15 (5)) | Mismatch list; unsupported browser → offline `verify_package.py` | — |
| SCR-P21-AE01…AE12 *(v3.1)* | `ops /eng/...` (governance overview, CAB, change records, releases, vulnerabilities, backup and DR, VAPT, audit plan, assurance workspace, production access, keys, capacity) | engineering roles per Appendix AE §AE.1.1; `auditor` (AE09) | Canonical IDs for Appendix AE's `SCR-AE-01…12` (kept as aliases; Appendix AG §AG.0.5 #11). P21 owns the ID namespace only; each screen is built by the phase addendum that cites it (FR-P00-V3-AE*, FR-P14-V3-AE*) | Per AE §AE.10.2 | read (AE06, AE08) |

**v3.1 additions to SCR-P21-21/22:** pre-fill picker (template, last grant, renewal); "narrow to what was used" toggle on renewals; approval queue sorted by requested start date then age, with SLA chips (due, reminded, escalated, lapsing) and bulk reject with one reason; dormant-grant confirmation card on `/me/grants`. *(v3.1)*

---

## 7. Backend design

### 7.1 Modules touched
New NestJS modules: `integrations/workspace` (port, adapters, connection service, capability resolver), `integrations/storage`, `integrations/accounting`, `integrations/payroll-exchange`, `integrations/catalogue` (catalogue, SoR, mappings, health, rehearsals), `exports` (`xpt` export engine; uses `packages/export-spec`), `imports` (`xpt` import engine), `group` (`grp`: entities, grants, walls, agreements, charges, secondment group columns, shared artefacts, referrals, consolidated views). Touched: `identity` (policy cache, SoD triggers, entity switcher), `documents` (mirror hooks, export item resolver), `hearings` (meeting-class guard), Operations Platform CRM and `mkt` modules (catalogue registration of the P16/P17 Brevo and social adapters; shared Brevo budget), `billing` (accounting export, inter-company invoices), `hrms` (JML events consumer, secondments), `audit` (entity views, access log fields `grant_id`, `purpose_code`, `legal_entity_id`), `reporting` (shared artefacts, consolidated views). New package: `packages/export-spec` (taxonomy, validators, manifest writer, BagIt writer, ZIP64 streamer, tools).

### 7.2 Tables (key columns; Appendix F conventions; `grp` DDL in Appendix AD §AD.14 is canonical)

```sql
CREATE SCHEMA IF NOT EXISTS cfg; CREATE SCHEMA IF NOT EXISTS xpt;

CREATE TABLE cfg.workspace_connections (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  kind text NOT NULL CHECK (kind IN ('workforce','customer')), suite text NOT NULL CHECK (suite IN ('m365','google','manual')),
  external_tenant_ref text NOT NULL, domains text[] NOT NULL DEFAULT '{}', provider_code text NOT NULL REFERENCES core.integration_providers(code),
  app_registration_ref text, secret_ref text, consent_status text NOT NULL CHECK (consent_status IN ('pending','granted','revoked')),
  confirmed_skus text[] NOT NULL DEFAULT '{}', detected_skus jsonb, data_location text, data_location_evidence_sha256 char(64),
  setup_evidence jsonb NOT NULL DEFAULT '[]', jml_automation boolean NOT NULL DEFAULT false,
  status text NOT NULL CHECK (status IN ('draft','active','degraded','revoked','retired')), std_cols);

CREATE TABLE cfg.workspace_capability_matrix (
  sku text NOT NULL, capability text NOT NULL, value jsonb NOT NULL, source_ref text NOT NULL, verified boolean NOT NULL,
  version int NOT NULL, PRIMARY KEY (sku, capability, version));

CREATE TABLE cfg.workspace_group_map (
  connection_id uuid NOT NULL REFERENCES cfg.workspace_connections(id), group_key text NOT NULL,   -- dept:case_services, loc:jaipur, entity:EQR, role:eq-meeting-hosts
  external_group_id text NOT NULL, kind text NOT NULL, PRIMARY KEY (connection_id, group_key));

CREATE TABLE cfg.workspace_sku_exceptions (
  id uuid PRIMARY KEY DEFAULT uuidv7(), user_id uuid NOT NULL, role_code text NOT NULL, compensating_control text NOT NULL,
  approved_by uuid NOT NULL, expires_at timestamptz NOT NULL CHECK (expires_at <= created_at + interval '90 days'), std_cols);

CREATE TABLE cfg.integration_catalogue (
  code text PRIMARY KEY, tool text NOT NULL, port text NOT NULL, adapters text[] NOT NULL, objects jsonb NOT NULL,
  direction text NOT NULL, fallback text NOT NULL, flag_key text, flag_approver text, notes text, version int NOT NULL);

CREATE TABLE cfg.system_of_record (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  data_category text NOT NULL, sor_system text NOT NULL, mirrors text[] NOT NULL DEFAULT '{}', conflict_rule text NOT NULL,
  change_request_id uuid REFERENCES core.config_change_requests(id), std_cols, UNIQUE (tenant_id, legal_entity_id, data_category),
  CHECK (data_category <> 'consent' OR sor_system = 'equator_consent_ledger'));   -- consent never has an external SoR (Appendix X)

CREATE TABLE cfg.mapping_sets (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, connector_code text NOT NULL, object text NOT NULL,
  direction text NOT NULL CHECK (direction IN ('inbound','outbound','both')), version int NOT NULL,
  tier text NOT NULL CHECK (tier IN ('G','T')), status text NOT NULL CHECK (status IN ('draft','in_review','approved','retired')),
  maker uuid NOT NULL, checker uuid CHECK (checker IS NULL OR checker <> maker), dry_run_report jsonb, std_cols,
  UNIQUE (tenant_id, connector_code, object, direction, version));

CREATE TABLE cfg.field_mappings (
  id uuid PRIMARY KEY DEFAULT uuidv7(), mapping_set_id uuid NOT NULL REFERENCES cfg.mapping_sets(id),
  source_field text NOT NULL, target_field text NOT NULL,
  transform text NOT NULL CHECK (transform IN ('copy','map_enum','concat','split','format_date','hash','mask','constant','lookup')),
  transform_params jsonb, pii_class text NOT NULL CHECK (pii_class IN ('none','personal','sensitive','identifier','consent','money')),
  required boolean NOT NULL DEFAULT false, null_policy text NOT NULL DEFAULT 'skip', validation_regex text, example text);

CREATE TABLE cfg.ledger_maps (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid NOT NULL, tool text NOT NULL,
  equator_account_code text NOT NULL, tool_ledger_name text NOT NULL, cost_centre text, version int NOT NULL, std_cols);

CREATE TABLE cfg.migration_rehearsals (
  id uuid PRIMARY KEY DEFAULT uuidv7(), connector_code text NOT NULL, tenant_id uuid, run_at timestamptz NOT NULL,
  runbook_ref text NOT NULL, reconciliation_report_id uuid, outcome text NOT NULL CHECK (outcome IN ('pass','pass_with_findings','fail')),
  next_due date NOT NULL, std_cols);

CREATE TABLE cfg.connector_health_checks (
  connection_or_provider text NOT NULL, checked_at timestamptz NOT NULL, signals jsonb NOT NULL,
  state text NOT NULL CHECK (state IN ('green','amber','red')), PRIMARY KEY (checked_at, connection_or_provider))
  PARTITION BY RANGE (checked_at);                                   -- F.1.5 pattern

CREATE TABLE cfg.mirror_targets (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, connection_id uuid NOT NULL REFERENCES cfg.workspace_connections(id),
  drive_ref text NOT NULL, library_path text NOT NULL, high_tier_approved boolean NOT NULL DEFAULT false,
  delete_on_revocation boolean NOT NULL DEFAULT false, status text NOT NULL, std_cols);

CREATE TABLE cfg.mirror_items (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, target_id uuid NOT NULL REFERENCES cfg.mirror_targets(id),
  document_id uuid NOT NULL, version_id uuid NOT NULL, external_item_id text, external_etag text, path text NOT NULL,
  state text NOT NULL CHECK (state IN ('pending','mirrored','conflict','withdrawn_label','superseded_label','deleted_in_workspace','disconnected')),
  last_mirrored_at timestamptz, std_cols);

CREATE TABLE cfg.transliteration_tables (script text NOT NULL, source text NOT NULL, ascii text NOT NULL, version int NOT NULL,
  PRIMARY KEY (script, source, version));
CREATE TABLE cfg.doc_type_abbreviations (doc_type text PRIMARY KEY, abbreviation text NOT NULL CHECK (abbreviation ~ '^[A-Za-z0-9-]{2,12}$'));
CREATE TABLE cfg.vendor_price_refs (vendor text, sku text, currency core.currency_code, price_minor bigint, gst_note text,
  source_ref text NOT NULL, observed_on date NOT NULL, PRIMARY KEY (vendor, sku, observed_on));

CREATE TABLE xpt.redaction_profiles (code text PRIMARY KEY, rules jsonb NOT NULL, tier text NOT NULL DEFAULT 'G', version int NOT NULL,
  change_request_id uuid REFERENCES core.config_change_requests(id));

CREATE TABLE xpt.export_requests (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  scope text NOT NULL CHECK (scope IN ('USER_SELF','DSR_PORTABILITY','PARTY_IN_CASE','CASE_FULL','NEUTRAL_PRACTICE','MARKETPLACE_PROVIDER','CHAMBERS_TENANT',
    'ENTERPRISE_TENANT','OPS_DEPARTMENT','EMPLOYEE_SELF','EMPLOYEE_FILE','PAYROLL_FY','GROUP_COMPANY','PLATFORM_TENANT_EXIT','STATUTORY_BOOKS','ASSURANCE_PACK')),
  scope_ref jsonb NOT NULL, layout text NOT NULL CHECK (layout IN ('standard_package','archival_bag')),
  redaction_profile text NOT NULL REFERENCES xpt.redaction_profiles(code), destination jsonb NOT NULL,
  requested_by uuid NOT NULL, requested_role text NOT NULL, approved_by uuid, approved_role text,
  CHECK (approved_by IS NULL OR approved_by <> requested_by), purpose text, dsr_request_id uuid, std_cols);

CREATE TABLE xpt.export_runs (
  id uuid PRIMARY KEY DEFAULT uuidv7(), request_id uuid NOT NULL REFERENCES xpt.export_requests(id), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  status text NOT NULL CHECK (status IN ('requested','awaiting_approval','approved','snapshotting','building','validating','ready','delivered','expired','rejected','failed','cancelled')),
  snapshot_ref text, spec_version text NOT NULL DEFAULT 'EQ-EXPORT-1.0', root_name text NOT NULL CHECK (char_length(root_name) <= 40),
  counts jsonb, bytes_total bigint, parts int, manifest_sha256 char(64), bag_valid boolean, gate_results jsonb,
  certificate_document_id uuid, expires_at timestamptz, failure_code text,
  progress jsonb,                                -- v3.1 AC §AC.13.15 (1): phase, items_done/total, bytes_done/total, parts_ready/total, eta_at, last_checkpoint
  restarted_from_run_id uuid REFERENCES xpt.export_runs(id),   -- v3.1: snapshot no longer readable → new run
  std_cols);

CREATE TABLE xpt.export_items (
  run_id uuid NOT NULL REFERENCES xpt.export_runs(id), seq int NOT NULL, path text NOT NULL CHECK (char_length(path) <= 140),
  export_name text NOT NULL, original_name text, sha256 char(64) NOT NULL, sha512 char(128) NOT NULL, bytes bigint NOT NULL,
  media_type text NOT NULL, format text NOT NULL, record_class text, record_association jsonb, source_system text, source_id uuid,
  version int, is_signed_original boolean NOT NULL DEFAULT false, evidence_ledger_seq bigint, rendition_of text,
  conversion_performed text NOT NULL DEFAULT 'none', redactions_applied int NOT NULL DEFAULT 0, part_no int NOT NULL DEFAULT 1,
  PRIMARY KEY (run_id, seq));
CREATE UNIQUE INDEX export_items_path_ci ON xpt.export_items (run_id, lower(path));   -- case-insensitive uniqueness (Windows)

CREATE TABLE xpt.export_parts (run_id uuid NOT NULL REFERENCES xpt.export_runs(id), part_no int NOT NULL, object_key text NOT NULL,
  bytes bigint NOT NULL, sha256 char(64) NOT NULL, PRIMARY KEY (run_id, part_no));

CREATE TABLE xpt.export_deliveries (
  id uuid PRIMARY KEY DEFAULT uuidv7(), run_id uuid NOT NULL REFERENCES xpt.export_runs(id),
  channel text NOT NULL CHECK (channel IN ('download','sharepoint','onedrive','google_drive','sftp','s3_compatible')),
  destination_ref text, destination_geo text, started_at timestamptz, completed_at timestamptz,
  sample_size int, sample_mismatches int, migration_verified boolean, status text NOT NULL,
  part_no int, bytes bigint, client_verified boolean,   -- v3.1 AC §AC.13.15 (3): per-part download verified by SHA-256 in the client
  std_cols);

CREATE TABLE xpt.export_presets (                -- v3.1; ≤ 10 per user (trigger)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, owner_user_id uuid NOT NULL, name text NOT NULL,
  scope text NOT NULL, layout text NOT NULL, redaction_profile text NOT NULL REFERENCES xpt.redaction_profiles(code),
  destination jsonb NOT NULL, std_cols, UNIQUE (owner_user_id, name));

CREATE TABLE xpt.export_schedules (              -- v3.1; plan-entitled (`tenant.xpt.schedules`)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, preset_id uuid NOT NULL REFERENCES xpt.export_presets(id),
  cadence text NOT NULL CHECK (cadence IN ('monthly','quarterly')), next_run_at timestamptz NOT NULL,
  paused boolean NOT NULL DEFAULT false, last_request_id uuid REFERENCES xpt.export_requests(id), std_cols);

CREATE TABLE xpt.export_checkpoints (            -- v3.1; resumable build on the same snapshot
  run_id uuid NOT NULL REFERENCES xpt.export_runs(id), seq int NOT NULL,
  kind text NOT NULL CHECK (kind IN ('top_folder','case_folder','part')), ref text NOT NULL,
  items_done int NOT NULL, bytes_done bigint NOT NULL, recorded_at timestamptz NOT NULL, PRIMARY KEY (run_id, seq));

CREATE TABLE xpt.test_open_results (             -- v3.1; one row per sampled file
  run_id uuid NOT NULL REFERENCES xpt.export_runs(id), path text NOT NULL, doc_type text NOT NULL,
  attempt smallint NOT NULL CHECK (attempt IN (1,2)), passed boolean NOT NULL,
  failure_reason text, checked_at timestamptz NOT NULL, PRIMARY KEY (run_id, path, attempt));

CREATE TABLE xpt.erasure_propagations (
  id uuid PRIMARY KEY DEFAULT uuidv7(), dsr_request_id uuid NOT NULL, tenant_id uuid NOT NULL, target text NOT NULL,
  items jsonb NOT NULL, notified_at timestamptz, deleted_by_equator boolean NOT NULL DEFAULT false, std_cols);

CREATE TABLE xpt.import_templates (code text PRIMARY KEY, object text NOT NULL, version int NOT NULL, file_document_id uuid NOT NULL);

CREATE TABLE xpt.import_batches (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL, source_kind text NOT NULL,
  mapping_set_id uuid NOT NULL REFERENCES cfg.mapping_sets(id), source_files jsonb NOT NULL,      -- [{document_id, sha256}]
  status text NOT NULL CHECK (status IN ('uploaded','scanned','mapped','dry_run_complete','awaiting_approval','approved','committing',
    'committed','reconciled','closed','rejected','failed','rolled_back')),
  dry_run_summary jsonb, maker uuid NOT NULL, checker uuid CHECK (checker IS NULL OR checker <> maker),
  rollback_until timestamptz, std_cols);

CREATE TABLE xpt.import_rows (batch_id uuid NOT NULL REFERENCES xpt.import_batches(id), row_no int NOT NULL,
  outcome text NOT NULL CHECK (outcome IN ('ok','warning','error','duplicate','committed','skipped')),
  messages jsonb, target_ref jsonb, PRIMARY KEY (batch_id, row_no));

CREATE TABLE xpt.reconciliation_reports (
  id uuid PRIMARY KEY DEFAULT uuidv7(), subject_kind text NOT NULL CHECK (subject_kind IN ('import_batch','migration_rehearsal','export_push')),
  subject_id uuid NOT NULL, control_totals jsonb NOT NULL, variances jsonb NOT NULL, explained_by uuid, outcome text NOT NULL, std_cols);
```
RLS: tenant RLS on all tenant-scoped `cfg`/`xpt` tables plus Appendix Z's `entity_scope` policy (AD §AD.4.2); `xpt.export_items` readable only by the run's requester, approver, DPO and `internal_auditor`; `cfg.workspace_connections.secret_ref` readable only by the integrations service role.

### 7.3 APIs (all `/v1`; problem+json; cursor pagination; Idempotency-Key on creating POSTs)

| Method and path | Purpose |
|---|---|
| `GET/POST /v1/workspace/connections`, `GET/PATCH /v1/workspace/connections/{id}` | Connections (kind, suite, consent, SKUs, data location) |
| `POST /v1/workspace/connections/{id}/setup-steps/{step}` | Record runbook step evidence |
| `POST /v1/workspace/connections/{id}/test` · `GET …/capabilities` · `POST …/detect-skus` | Self-test, capabilities, SKU detection |
| `GET/POST /v1/workspace/sku-exceptions` | SKU exceptions (≤ 90 days) |
| `GET /v1/workspace/jml/{employeeId}` | JML step status for an employee |
| `GET /v1/integrations/catalogue` · `POST /v1/integrations/{code}/enable` · `/disable` | Catalogue and gated enable |
| `GET/PUT /v1/integrations/sor` | System-of-record register |
| `GET/POST /v1/integrations/{code}/mapping-sets`, `POST …/{id}/dry-run`, `POST …/{id}/submit`, `POST …/{id}/approve` | Mappings |
| `GET /v1/integrations/health` · `GET /v1/integrations/{code}/rehearsals` · `POST …/rehearsals` | Health and rehearsals |
| `GET/POST /v1/files/mirror-targets`, `GET /v1/files/mirror-items?caseId=`, `POST /v1/files/mirror-items/{id}/resolve`, `POST /v1/documents/{id}/file-back` | Mirror and file-back |
| `POST /v1/meetings` (meeting class guard) · `POST /v1/tenants/{id}/meetings/teams-bridge-request` | Workspace meetings and bridge request |
| `POST /v1/exports` (alias `POST /v1/me/exports` for `USER_SELF`) · `GET /v1/exports` · `GET /v1/exports/{runId}` | Request and list exports |
| `POST /v1/exports/{runId}/approve` · `/reject` · `/cancel` | Decisions |
| `POST /v1/exports:estimate` *(v3.1)* | Pre-flight estimate; no side effects (AC §AC.13.3) |
| `GET /v1/exports/{runId}/progress` · `GET /v1/exports/{runId}/progress:stream` (SSE) *(v3.1)* | Progress (AC §AC.13.15 (1)) |
| `GET/POST /v1/exports/presets`, `PATCH/DELETE /v1/exports/presets/{id}` · `GET/POST /v1/exports/schedules`, `PATCH /v1/exports/schedules/{id}` *(v3.1)* | Presets (≤ 10 per user) and plan-entitled schedules |
| `POST /v1/exports/{runId}/parts/{n}/link` | Presigned link (≤ 5 min) per part; *v3.1:* renewal within the availability window needs step-up only, after it `XPT_LINK_RENEWAL_NOT_ALLOWED` (410) |
| `POST /v1/exports/{runId}/deliveries/{id}/verified` *(v3.1)* | Client records a part's verified SHA-256 (`client_verified`) |
| `POST /v1/exports/{runId}/deliveries` | Push to a destination |
| `GET /v1/exports/{runId}/manifest` · `/certificate` | Manifest and certificate |
| `GET /v1/imports/templates` · `POST /v1/imports` · `POST /v1/imports/{id}/dry-run` · `/submit` · `/approve` · `/commit` · `/rollback` · `GET …/reconciliation` | Imports |
| `POST /v1/accounting/exports` (period, entity, tool) | Accounting export (creates an `xpt` run of scope `STATUTORY_BOOKS` sub-type `accounting_period`) |
| `/v1/group/...` | Appendix AD §AD.15.1 |

### 7.4 Domain events (outbox → CloudEvents `equator.<context>.<entity>.<verb>.v1`)
`cfg.workspace_connection.activated`, `cfg.workspace_connection.consent_revoked`, `cfg.workspace_connection.sku_mismatch_detected` (account lifecycle events stay Appendix Z's `hr.workspace.account_provisioned` / `.account_disabled`, emitted by P18's JML workflow), `cfg.connector.enabled`, `cfg.connector.disabled`, `cfg.connector.health_changed`, `cfg.mapping_set.approved`, `cfg.rehearsal.completed`, `cfg.mirror.item_conflicted`, `cfg.mirror.disconnected`, `xpt.export.requested`, `xpt.export.approved`, `xpt.export.ready`, `xpt.export.failed`, `xpt.export.delivered`, `xpt.export.expired`, `xpt.import.dry_run_completed`, `xpt.import.committed`, `xpt.import.reconciled`, `xpt.import.rolled_back`, plus the `grp.*` events of Appendix AD §AD.15.2. Payloads carry IDs and codes only.

### 7.5 Temporal workflows and jobs

| Workflow / job | Trigger | Notes |
|---|---|---|
| `WorkspaceJmlWorkflow` (P18, Appendix Z) | P18 HR events | Unchanged; now reads `cfg.workspace_connections` and the capability resolver |
| `WorkspaceDeletionWorkflow` (P18) | L3 due | Guard unchanged; P21 adds the `EMPLOYEE_FILE` export check (AC §AC.2.5) |
| `WorkspaceAuditIngestJob` | Hourly | To `eq-log-archive` |
| `TeamsAccessPolicyReconcileJob` | Nightly | Host group vs policy grants; drift ticket |
| `SharePointMirrorWorkflow` | DMS events | One way; eTag conflict logic |
| `ExportBuildWorkflow` | Export approved | Snapshot → resolve → convert → write → validate (child activities per folder; heartbeat for long conversions). *v3.1:* checkpoints to `xpt.export_checkpoints`; idempotent writes on `(export_run_id, path)`; resumes on the same snapshot; child `TestOpenActivity` before `ready` (AC §AC.13.15) |
| `ExportScheduleJob` *(v3.1)* | Hourly | Creates export requests from due `xpt.export_schedules`; sensitive scopes go to maker-checker |
| `ExportPushWorkflow` | Delivery requested | Upload sessions; sample re-hash |
| `ExportExpiryJob` | Hourly | Lifecycle and regeneration eligibility |
| `ImportMigrationWorkflow` | Import uploaded | Scan → map → dry run → approval signal → commit batches → reconcile |
| `ConnectorHealthProbeJob` | Every 5 min | Signals and state |
| `BrevoBudgetLimiter` (shared by P16 `CrmSyncWorkflow` and P17 marketing executors) | Every request to Brevo | Account-level hourly budget; queues excess; no sync logic of its own |
| `MarketingConsentDiffJob` | Daily | Diffs must be zero after 15 min |
| `MigrationRehearsalReminderJob` | Daily | Due and overdue rehearsals |
| `CrossCompanyGrantExpiryJob` | Every minute *(v3.1; was 5 min)* | Expiry status, T-14/T-7/T-1 notices, cache refresh (access already ends at `expires_at` per request) |
| `GrantRequestSlaJob` *(v3.1)* | Hourly | Reminders (day 2), escalation (day 3), lapse (day 10) for grant and assignment requests |
| `DormantGrantJob` *(v3.1)* | Daily | Flags grants unused for 30 days; revokes after 5 working days without confirmation |
| `SecondmentReminderJob` *(v3.1)* | Daily | Signature reminders, T-30/T-7 end reminders, automatic end on `ends_on` |
| `EthicalWallIndexJob` | On CRM/collections/support assignment events + nightly | Exposures → `ConflictIndex` |
| `WallAttestationCampaign` | Annual | T-30 reminders; suspension on overdue |
| `RelatedPartyDetectionJob` | Nightly | Director data → candidate pairs → CS task |
| `RelatedPartyApprovalWorkflow` | ICSA submitted | CS review → approvals → signatures → active |
| `IntercompanyChargeRunWorkflow` | Monthly | Payroll cost × allocation → draft invoices → check |
| `RegistryPropagationReconcileJob` | Daily | Registry events vs consumers; 72 h SLA |
| `GrantAccessReportCollector` | Weekly | Evidence to `eng.control_evidence` |

---

## 8. Integrations (ports and adapters)

| Port | Adapters in this phase | Failover | Residency rule | Spike items before merge |
|---|---|---|---|---|
| `WORKSPACE_PORT` (Appendix Z; extended here) | `m365_graph` (P1), `google_workspace` (stub, OFF), `manual_it_desk` | none (queue + manual desk) | M365 India-default tenant recorded; Google needs residency ADR | `usageLocation` ordering; mailbox delay; shared-mailbox conversion (app-only PowerShell); Exchange app RBAC for `Mail.Send`; `onlineMeeting` options; Teams webhook mechanism; Management Activity API permissions |
| `STORAGE_PORT` (new) | `sharepoint_graph`, `onedrive_graph`, `sftp_generic`, `s3_compatible`, `google_drive` (OFF) | none | Destination geography recorded on delivery | `Sites.Selected` grant request shape; upload fragment size; delta under `Sites.Selected`; conflict behaviour parameter |
| `ACCOUNTING_PORT` (new) | `tally_file`, `zoho_books` (spike) | none (CSV/XLSX download) | India | Tally import schema/version; Zoho Books API |
| `PAYROLL_EXCHANGE_PORT` (Appendix Z) | `generic_csv` | none | India | Candidate vendor formats |
| `CRM_PORT` | `brevo` (built in P16, Appendix X), existing `hubspot`, `zoho` — catalogued here | none (native CRM continues) | `BREVO_EU` transfer row; DPA | Brevo catch-all limit for CRM; webhook retries; import field limits |
| `MARKETING_PORT` (registered here, X-63) | `brevo`, `ses_marketing` (built in P17) — catalogued here | `ses_marketing` | As above | DLT support (keeps SMS/WhatsApp OFF) |
| `SOCIAL_PORT` (registered here, X-63) | `linkedin_cm`, `meta_graph`, `x_v2`, `youtube_data` (all OFF), `manual_handoff` (built in P17) — catalogued here | `manual_handoff` | Public content only | Access tiers and app reviews |
| `ESIGN_PORT` (existing) | unchanged | reinitiate | — | LTV data for India CCA chains (export evidence) |
| `VIDEO_PORT` (existing) | unchanged; meeting-class guard added upstream | reinitiate | India | — |
| `GROUP` connectors (Appendix D §D.7) | Subscription ownership and labelling per X-64 | — | — | — |

Contract tests: in-memory fakes for every new port; nightly sandbox tests against a Microsoft 365 developer tenant, a Brevo test account and SFTP/S3 test targets; webhook fixtures for Brevo (valid bearer, wrong bearer, wrong IP, duplicate, forged unsubscribe).

---

## 9. Configuration surface (NN-33 tiers: L locked · G governed · T tenant)

| Key | Tier | Default | Bounds / values | Who may change | Approval |
|---|---|---|---|---|---|
| `iam.leaver_revoke_hours` | L | 4 | tenant may only tighten (1–4) | `it_admin` | `compliance_officer` |
| `tenant.hr.workspace.jml_automation` | G | OFF | ON/OFF | `it_admin` | `entity_admin` |
| `tenant.hr.workspace.sku_rules` | T with maker-checker (Appendix Z key) | AC §AC.3.3 | role → SKU list | `it_admin` | security lead |
| `tenant.hr.workspace.upn_pattern` | T | `{first}.{last}` | tokens `{first}`, `{last}`, `{mi}`, `{n}` | `it_admin` | — (audit + rollback) |
| `tenant.hr.workspace.delete_delay_days` | T (Appendix Z key) | 90 | 30–365 | `it_admin` | `hr_manager` |
| `tenant.hr.workspace.manual_fallback_after_minutes` | T | 60 | 15–240 | `it_admin` | — |
| `ops.workspace.google.enabled` | G | OFF | flag | CS | DPO (residency ADR) |
| `platform.hr.workspace.sku_exception_max_days` | L | 90 | — | — | — |
| `tenant.chm.meetings.teams_bridge` | G | OFF | flag | `chambers_owner` | Equator `legal_reviewer` |
| `platform.ops.meetings.permitted_classes` | L | AC §AC.8.3 | — | — | — |
| `user.notifications.chat_enabled` | T | OFF | per user | user | — |
| `tenant.chm.sharepoint_mirror` / `tenant.ent.sharepoint_mirror` | G | OFF | flag | tenant owner | Equator DPO |
| `tenant.files.mirror.delete_on_revocation` | T | false | bool | tenant owner | — |
| `tenant.xpt.push_to_workspace` (chambers alias `tenant.chm.export.push_to_workspace`, Appendix W) | T | ON when a customer connection exists | bool | tenant admin | — |
| `tenant.xpt.push_destinations` | T | download | list | tenant admin | — |
| `tenant.xpt.part_max_gb` | T | 20 | 1–50 | tenant admin | — |
| `tenant.xpt.default_layout.<scope>` | T | AC §AC.13.2 | `standard_package`, `archival_bag` | tenant admin | — |
| `tenant.xpt.readme_languages` | T | en, hi | + tenant language | tenant admin | — |
| `platform.xpt.path_budget_below_root` | L | 140 | — | — | — |
| `platform.xpt.root_name_max` | L | 40 (incl. part suffix) | — | — | — |
| `platform.xpt.file_name_max` | L | 80 (default target 64) | — | — | — |
| `platform.xpt.exclusions.*` | L | AC §AC.13.11 | — | — | — |
| `platform.xpt.redaction_profiles.*` | G | AC §AC.13.12 | profile rules | `legal_reviewer` | DPO |
| `platform.xpt.signed_original_rerender` | L | forbidden | — | — | — |
| `tenant.xpt.import_rollback_days` | T | 7 | 0–30 | tenant admin | — |
| `tenant.xpt.early_part_download` *(v3.1)* | T | ON | bool | tenant admin | — |
| `tenant.xpt.test_open.sample_pct` / `.max_fail_pct` *(v3.1)* | T | 5 / 2 | 1–20 / 0–5; minimum 20 sampled files (L) | tenant admin | — |
| `tenant.xpt.schedules` *(v3.1)* | T | none | monthly, quarterly; plan-entitled; sensitive scopes maker-checker (L) | tenant admin | — |
| `platform.xpt.download.parallel_parts` / `.auto_retries` *(v3.1)* | T | 3 / 3 | 1–6 / 0–5 | platform engineering | — |
| `platform.integrations.rehearsal_max_age_days` | L | 400 | — | — | — |
| `platform.integrations.credential_max_age_days` | L | 90 | — | — | — |
| `tenant.integrations.<code>.enabled` | G | OFF | flag; gate FR-P21-16 | tenant admin | named approver per catalogue row |
| `tenant.integrations.mapping_set.<id>` | G (identity/consent/money) / T (other) | — | versions | tenant admin | `compliance_officer` for G |
| `mkt.brevo.enabled` (connector flag for both Brevo ports; AC §AC.17) | G | OFF | flag | `marketing_manager` | DPO (DPA on file) |
| `tenant.ops.connectors.brevo_crm_sync.enabled` (CRM-object sync; Appendix X key) | T | OFF | cannot be ON while `mkt.brevo.enabled` is OFF | `ops_director` | DPO approval recorded |
| `tenant.mkt.brevo.max_requests_per_hour` (shared account budget for both Brevo ports; AC §AC.17, Appendices X and Y) | T | 80 | 1 – 95% of plan limit | `marketing_manager` | — |
| `mkt.brevo.sms_whatsapp.enabled` | G | OFF | flag | `compliance_officer` | written DLT confirmation |
| `mkt.adobe_embed.enabled` | G | OFF | flag | `marketing_manager` | Adobe review evidence |
| `mkt.social.linkedin_cm.enabled`, `.meta_graph.enabled`, `.x_v2.enabled`, `.youtube_data.enabled` | G | OFF | flags | `marketing_manager` | `legal_reviewer` |
| `tenant.mkt.social.ig_daily_cap` (Appendix Y key) | T | 50 | ≤ 100 | `social_media_executive` | — |
| `tenant.mkt.social.x_monthly_budget_usd` (Appendix Y key) | T | 50 | budget line required | `marketing_manager` | — |
| `tenant.fin.accounting_export.tally` / `.zoho_books` | T / G | OFF | flags | `finance_ops` | `accounts_checker` |
| `tenant.pay.external_payroll.enabled` | G | OFF | flag | `hr_manager` | `payroll_checker` + CS |
| `group.workspace.topology` | G | `tenant_per_entity` | or `shared_tenant_multi_domain` | `group_admin` | CS |
| `group.grants.default_duration_days` *(v3.1)* | T | 90 | 1 – group cap | `entity_admin` | — |
| `group.grants.max_duration_days` | G | 365 *(v3.1; was 90, which made the AD-R4 role maximum unreachable)* | 1–365 (per-role maximum in `grp.grantable_roles`, seed 90; 365 only for shared-desk roles; AD-R4) | `group_admin` | DPO |
| `group.grants.approval_sla_working_days` / `.request_lapse_days` / `.dormant_days` *(v3.1)* | T | 3 / 10 / 30 | 1–10 / 3–30 / 14–90 | `entity_admin` | — |
| `group.assignments.decision_sla_working_days` / `.max_months` *(v3.1)* | T | 5 / 12 | 2–10 / 1–24 | `group_hr` | — |
| `group.grants.max_concurrent_entities` | G | 2 | 1–4 | `group_admin` | DPO |
| `group.grants.review_interval_days` | T | 30 | 7–90 | `entity_admin` | — |
| `group.walls.cooling_off_months` | G | 12 | ≥ 6 | `compliance_officer` | `legal_reviewer` |
| `group.walls.attestation_month` | T | April | month | `compliance_officer` | — |
| `group.gdsa.propagation_sla_hours` | G | 72 | ≤ 72 | DPO | `legal_reviewer` |
| `group.purposes` | G | AD §AD.7.2 | catalogue | `group_admin` | DPO |
| `group.shared_artifacts.default_expiry_months` | T | 12 | 1–24 | `entity_admin` | — |
| `group.consolidated.min_k` | L | 5 (outcome cells 10) | — | — | — |
| `platform.grp.modules.never_shareable` | L | `core`, `cases`, `neutrals`, `allocation`, `proceedings`, `documents`, sealed | — | — | — |
| `group.referrals.retention_years` | G | 3 | 1–8 | DPO | `legal_reviewer` |
| `group.audit.applicability.*` (per entity; Appendix AE §AE.8.2 key) | G | CS-entered facts | source + effective date | CS | `legal_reviewer` (Appendix AE §AE.15) |

Every row is a `cfg.setting_definitions` row (values in `cfg.setting_values`; Appendix V §V.6.1) with tier metadata, bounds, approver, review date and rollback (P15). Flags dependent on counsel, a vendor contract, a Board approval or an unconfirmed fact default OFF and name their approver.

---

## 10. Security, privacy and audit

- **Neutrality and group boundaries:** CI tests `NO_CASE_DATA_TO_WORKSPACE`, `GROUP_SHARE_SCOPE`, `NO_MEETING_DATA_IN_APPRAISAL`, `NO_VENDOR_SDK_OUTSIDE_ADAPTERS`, `NOTIFICATION_CONTENT_MINIMISED`; schema validators on every outbound adapter payload; no `core` case module in any grant (DB CHECK + policy).
- **Identity:** Keycloak `eq-portal-ops` with phishing-resistant MFA is the control point for every console regardless of workspace SKU (D3-40); SKU-sufficiency rule for privileged roles; leaver ≤ 4 h; grant-bound sessions end ≤ 60 s after expiry.
- **Credentials:** certificate credentials only for app registrations; private keys in AWS Secrets Manager/KMS; rotation ≤ 90 days; forbidden broad permissions; consent recorded as change records; quarterly access review including app registrations and cross-company grants.
- **Exports:** step-up per scope; maker-checker for sensitive scopes (NN-36); independent exclusion pass; Critical incident on hash mismatch or exclusion violation; watermark only on renditions of `high`-tier PDFs (requester role and time), never on signed originals or court exports (Appendix L §1.12); every download in `audit.access_log`; presigned links ≤ 5 min.
- **Privacy:** transfer-register rows for Brevo, Google (if enabled) and non-India destinations; DPAs before activation; GDSA before any cross-entity personal data; erasure propagation to mirrors and GDSA recipients ≤ 72 h; DSR portability through `DSR_PORTABILITY`; employee notices name group entities and purposes (RE F5.1).
- **Logging and CERT-In:** workspace audit logs ingested hourly into `eq-log-archive` (India, 400 days; floor 180).
- **Accounting audit trail:** inter-company charges append-only after invoicing; master-data history; exports of ledgers include the edit log (Companies (Accounts) Rules r.3(1) proviso; NN-36).
- **Evidence collectors** added to Appendix Q §7.3: `jml_sla_report`, `workspace_sku_role_check`, `m365_audit_log_ingest`, `export_run_register`, `marketing_consent_sync`, `connector_health_summary`, `migration_rehearsal_register`, `grant_access_report`, `wall_attestation_status`, `related_party_register_snapshot`.

---

## 11. AI touchpoints and guardrails

| Touchpoint | Allowed | Guardrails |
|---|---|---|
| Mapping assistant (suggest source → target field mappings from column headers and sample values) | Yes, as suggestions | Runs on Bedrock India; sample values masked; suggestions labelled "Suggested — review"; a human approves every mapping (NN-01) |
| README drafting for exports | Template-generated, not AI | Deterministic text with variables; no AI in the export path |
| Import anomaly explanations | Yes | Explains validation errors in plain language; never changes data |
| Shared-dashboard narratives | Only through `analytics_narrator` on aggregates (k-suppressed) | No case-identifying data; no cross-entity inference |
| Wall and grant decisions | **No AI** | Deterministic rules only |
| Teams/Meet transcripts, Copilot outputs | **Not ingested** | NN-11, NN-35 |

---

## 12. Acceptance criteria (Gherkin)

Files `tests/acceptance/appendix-AC.feature`, `tests/acceptance/appendix-AD.feature`, `tests/acceptance/P21.feature`.

```gherkin
Feature: Appendix AC — workspace, integrations and portability

Scenario: AC-T01 SKU detection hides unavailable capabilities
  Given a workforce connection whose subscribedSkus returns only Business Basic
  When the IT admin opens the capabilities screen
  Then "Conditional Access" and "Retention policies" show as unavailable with their fallback
  And the screen states "Microsoft has no plan named Business Starter; detected plan: Business Basic"

Scenario: AC-T02 Leaver revoked within 4 hours while Graph is down
  Given an employee's exit becomes effective at 10:00 IST and the m365_graph circuit is open
  When 60 minutes pass
  Then a manual IT-desk ticket "Disable account" exists with an SLA due at 14:00 IST
  And the employee's Keycloak sessions were revoked within 60 seconds of 10:00

Scenario: AC-T03 Privileged role blocked on an insufficient SKU
  Given a user on Business Basic without an exception
  When an admin grants the role "registrar"
  Then the API returns 409 HR_WORKSPACE_SKU_INSUFFICIENT

Scenario: AC-T04 Mediation cannot be scheduled on Teams
  When a chambers user calls POST /v1/meetings with a mediation session reference
  Then the API returns 422 OPS_MEETING_CLASS_NOT_PERMITTED
  And the session can be scheduled only in a VIDEO_PORT room

Scenario: AC-T05 Teams bridge refused in a party's tenant
  Given the Teams bridge flag is ON for a chambers tenant
  When the selected host connection belongs to the claimant organisation
  Then the API returns 409 OPS_MEETING_HOST_TENANT_IS_PARTY

Scenario: AC-T06 Mirror never overwrites an edited working copy
  Given a mirrored DOCX whose SharePoint eTag changed after mirroring
  When a new version is filed in Equator
  Then Equator uploads "{name}_EQ-v02.docx" beside the edited file
  And both mirror items are in state "conflict"

Scenario: AC-T07 Every catalogue row has a working fallback
  Given each catalogue connector is disabled in turn
  Then the fallback named in the catalogue completes the user journey

Scenario: AC-T08 Forged Brevo unsubscribe is not applied
  Given a webhook with a valid bearer token reports "unsubscribed" for a contact
  And the Brevo API re-fetch shows the contact subscribed
  Then no consent withdrawal is recorded and a security event is logged

Scenario: AC-T09 Consent withdrawal syncs within 15 minutes
  Given a contact withdraws marketing consent in Equator
  Then the contact is unsubscribed in Brevo within 15 minutes
  And the daily consent diff shows zero differences

Scenario: AC-T10 Export uses the standard taxonomy and names
  When a party exports case EQ/FIN/JAI/2027/00042
  Then the package root is "Equator_Export_<OrgSlug>_<YYYY-MM-DD>" with 00_README.pdf, 00_Contents.xlsx and 99_Manifest
  And the case folder "03_Cases/EQ-FIN-JAI-2027-00042_<ShortTitle>" contains folders 01_Intake to 10_Audit_Trail

Scenario: AC-T11 Path budget enforced
  Given a document whose generated path would be 171 characters below the root
  When the export is built
  Then the shortening algorithm reduces it to 140 or fewer characters
  And the root folder name is 40 characters or fewer
  And the manifest records original_name and export_name

Scenario: AC-T12 Signed original is byte-identical
  Given an award signed with DSC
  When the award-holder exports the case
  Then "…_signed.pdf" has the SHA-256 recorded in core.evidence_ledger
  And a separate "…_rendition.pdf" is PDF/A-2b labelled "Rendition — not the signed original"

Scenario: AC-T13 Caucus material excluded
  Given the respondent shared a caucus note NEUTRAL_ONLY with the mediator
  When the claimant exports the case
  Then no caucus item appears and 00_README.pdf states that confidential caucus material is not included

Scenario: AC-T14 Multi-party redaction keeps served documents intact
  Given a three-party mediation where a document was shared with party B only
  When party C exports the case
  Then the document is absent from C's package
  And party B's phone number is masked in generated data files but served pleadings are unchanged

Scenario: AC-T15 Large export in parts with resume
  Given a 45 GB chambers exit export and part_max_gb 20
  Then three ZIP64 parts with UTF-8 names are produced, each with 00_README.pdf
  And an interrupted download of part 2 resumes with an HTTP range request and its SHA-256 verifies

Scenario: AC-T16 Push to SharePoint is verified
  When a ready export is pushed to a SharePoint library
  Then at least 2% or 50 files are re-downloaded and their SHA-256 match the manifest
  And the delivery is marked migration_verified

Scenario: AC-T17 Files open in Office for the web
  Given the nightly seeded exports
  Then OOXML validation, PDF/A validation and LibreOffice round-trip pass with zero errors
  And the latest quarterly manual test record shows no repair prompts in Word, Excel and PowerPoint for the web

Scenario: AC-T18 Import dry run and reconciliation
  Given a 50,000-row case spreadsheet with 120 invalid rows and 30 duplicates
  When the dry run completes
  Then the report lists 120 errors and 30 duplicates by row
  And after approval and commit the reconciliation shows control totals equal to the source minus rejected rows

Scenario: AC-T19 No case data reaches the workspace
  When any workspace adapter payload contains a case number in a non-administering tenant context or a party name
  Then the adapter rejects it with INTEGRATION_POLICY_REJECTED

Scenario: AC-T20 Accounting re-export after period change
  Given October was exported to Tally and an invoice was later reversed in October
  When the next accounting export runs
  Then it fails with 409 XPT_ACCOUNTING_PERIOD_REEXPORT_REQUIRED until October is re-exported

Scenario: AC-T21 DSR portability in JSON first
  When a data principal requests portability
  Then the package contains JSON with schemas for every entity and a PDF/A summary within the DSR clock

Scenario: AC-T22 Tenant exit
  Given a chambers tenant cancels on 1 November
  Then its archival bag is ready by 8 November
  And it can be regenerated until 30 January

Scenario: AC-T23 Connector turns red on stale rehearsal
  Given Brevo's last migration rehearsal was 401 days ago
  Then the Brevo health tile is red and the integration on-call is paged

Scenario: AC-T24 Billing never blocks an exit export
  Given a tenant with an overdue invoice
  When the tenant owner requests PLATFORM_TENANT_EXIT
  Then the export proceeds without payment

# v3.1 (Appendix AC §AC.13.15; FR-P21-44)
Scenario: AC-T25 Pre-flight estimate has no side effects
  Given a tenant admin prepares a CHAMBERS_TENANT export
  When the screen calls POST /v1/exports:estimate
  Then sizes, parts, time to ready and exclusion counts by reason code are shown
  And no export request, run, approval item or audit "export" event is created

Scenario: AC-T26 Killed worker resumes on the same snapshot
  Given an export run in building with checkpoints after 3 of 7 top-level folders
  When the worker is killed and the workflow resumes
  Then the run continues on the same snapshot_ref
  And the manifest has no duplicate and no missing rows

Scenario: AC-T27 Dropped download resumes by range request
  Given part 2 of 3 is 60% downloaded when the connection drops
  When the download manager retries
  Then it resumes with an HTTP Range request
  And the part's SHA-256 verifies and client_verified is recorded

Scenario: AC-T28 Corrupt working copy is listed, then the threshold fails the run
  Given a seeded corrupt DOCX working copy in the test-open sample
  When TestOpenActivity runs
  Then the file is regenerated once and, failing again, listed under "Files that may need repair" with its PDF/A record copy kept
  When failures exceed tenant.xpt.test_open.max_fail_pct
  Then the run fails with 500 XPT_TEST_OPEN_FAILED and a Sev-3 incident is opened

Scenario: AC-T29 Verify page sends no file bytes
  Given a recipient opens /exports/verify and drops an extracted package
  Then every file is checked against manifest.json in the browser
  And the network log shows no request carrying file content
```

```gherkin
Feature: Appendix AD — group companies

Scenario: AD-T01 Entity partition isolation
  Given a Finbyx user with no grant
  When the user queries ops.crm_accounts
  Then only rows with company_id = Finbyx's grp.legal_entities.id are returned (AD-R1)

Scenario: AD-T02 Grant needs the target approver and expires
  Given a Finbyx user requests sales_executive in EQR for 30 days
  When the requester's own Finbyx manager tries to approve
  Then the API returns 403 GRP_GRANT_APPROVER_NOT_TARGET
  When the requester tries to approve the request
  Then the API returns 409 GRP_GRANT_SELF_APPROVAL
  When EQR's entity_admin approves
  Then after 30 days the grant is expired and the user's session loses EQR data within 60 seconds

Scenario: AD-T03 No grant can include case data
  When a grant is requested with module "cases"
  Then the API returns 422 GRP_MODULE_NOT_SHAREABLE

Scenario: AD-T04 GDSA required for personal data
  Given purpose.shared_support_desk requires a GDSA
  When a grant is requested without an active GDSA listing that purpose
  Then the API returns 409 GRP_GDSA_REQUIRED

Scenario: AD-T05 Field policy strips columns server-side
  Given a grant whose field policy excludes contact phone numbers
  When the grantee calls the CRM contacts API
  Then responses and exports contain no phone field

Scenario: AD-T06 Ethical wall blocks assignment
  Given a user managed Alpha Finance collections in Finbyx within the last 12 months
  When a registrar assigns that user to an Equator case where Alpha Finance is claimant
  Then the API returns 409 GRP_ETHICAL_WALL_CONFLICT

Scenario: AD-T07 Case handler cannot take lender-side collections grant
  Given a case_manager in EQR
  When a grant for Finbyx collections is requested for that user
  Then the request is blocked by rule EW-02

Scenario: AD-T08 Duplicate employment blocked
  Given an active EQR employee
  When Udofin HR creates a second employment for the same PAN hash
  Then the API returns 409 GRP_DUPLICATE_EMPLOYMENT and suggests a secondment

Scenario: AD-T09 Secondment creates a template, not access
  When a secondment becomes active
  Then a grant template exists for the host role
  And the secondee has no host data access until the host approver approves the grant

Scenario: AD-T10 Recharge run is maker-checker and append-only
  Given an invoiced inter-company charge
  When anyone updates its amount
  Then the database rejects the update and only a reversal is allowed

Scenario: AD-T11 No invoice without an active ICSA
  When a recharge is run for an agreement in status "approvals"
  Then the API returns 409 GRP_ICSA_NOT_ACTIVE

Scenario: AD-T12 Related-party change opens a CS task
  Given a director is appointed to both Finbyx and EQR
  When the nightly detection runs
  Then a CS review task is created for the pair under s.2(76)(iv)

Scenario: AD-T13 Shared dashboard suppression
  Given a shared group dashboard with a cell of 3 cases
  Then the cell shows "fewer than 5" and drill-through is disabled

Scenario: AD-T14 Referral requires party authorisation and records choice
  Given an award-holding lender
  When an execution referral is created without the lender's authorisation
  Then the API returns 409 GRP_REFERRAL_AUTHORISATION_MISSING
  And after authorisation the list shown and the professional chosen are recorded, with no ranking or sponsored entries

Scenario: AD-T15 Equator never pushes case data to a group company
  When GROUP_SHARE_SCOPE runs in CI
  Then no path exists from grp sharing views, grants or group webhook subscriptions to core case tables
  And Finbyx-hosted webhook subscriptions are owned by the lender tenant and carry only that lender's cases

Scenario: AD-T16 Group relationship disclosed to the counterparty
  Given the claimant is a software client of Finbyx
  When the respondent opens the case disclosure panel
  Then it states that the claimant is a client of a company in the same group as Equator

Scenario: AD-T17 Group company export excludes other partitions
  When Udofin's entity_admin exports GROUP_COMPANY
  Then the bag contains only Udofin partition rows and no Equator case data

Scenario: AD-T18 Registry withdrawal propagates within 72 hours
  Given an advocate withdraws consent_group_share
  Then every consuming tenant hides the record within 72 hours and the reconciliation shows zero drift

# --- v3.1 additions (24 October 2026) ---

Scenario: AD-T19 Undecided grant request lapses
  Given a grant request into Udofin submitted on Monday 2 November 2026 with approval SLA 3 working days
  Then the approver is reminded on Wednesday 4 November and Udofin's entity_admin is alerted on Thursday 5 November
  And on Thursday 12 November the request is lapsed and approving it returns 409 GRP_GRANT_LAPSED
  And the requester can re-submit it pre-filled in one action

Scenario: AD-T20 Dormant grant is revoked
  Given an active grant with no access for 30 days
  When neither the grantee nor the approver confirms the need within 5 working days
  Then the grant is revoked with reason "dormant" and the grantee loses access within 60 seconds

Scenario: AD-T21 Assignment request becomes a secondment draft
  Given a Udofin department head requests 20% of an EQR employee whose planned allocations total 70%
  When EQR HR accepts within 5 working days
  Then a secondment draft pre-filled with host, dates, 20% and the ICSA recharge basis exists with a grant template
  And a second request for 20% more for the same period is refused because allocations would exceed 100%
  And if the secondment is unsigned 10 working days after the start date the request and draft lapse

Scenario: AD-T22 Dotted module codes cannot smuggle case data
  When a grant row with modules ['ops.crm','core.cases'] is inserted directly in the database
  Then the insert fails the grp.modules_shareable CHECK

Scenario: AD-T23 Role maximum governs long grants
  Given group.grants.max_duration_days is 365, support_agent has a role maximum of 365 for purpose.shared_support_desk and sales_executive has 90
  When 180-day grants are requested for both roles
  Then the support_agent grant is accepted for review and the sales_executive request returns 422 GRP_GRANT_DURATION_EXCEEDED
```

---

## 13. Deliverables and exit gate

- [ ] `STORAGE_PORT`, `ACCOUNTING_PORT`, `MARKETING_PORT` and `SOCIAL_PORT` registered (X-63); `WORKSPACE_PORT` extended to the AC §AC.2.2 interface; `m365_graph`, `manual_it_desk`, `sharepoint_graph`, `onedrive_graph`, `sftp_generic`, `s3_compatible`, `tally_file`, `generic_csv` adapters merged with contract tests; P16/P17 `brevo` and `SOCIAL_PORT` adapters catalogued with AC conformance tests green; Google adapters stubbed and OFF.
- [ ] Workspace set-up wizard and runbook (`docs/runbooks/workspace-m365-setup.md`) completed on Equator's own tenant with the **CS-confirmed SKU** recorded (D3-04).
- [ ] P18 JML migrated onto `cfg.workspace_connections` for EQR with a 30-day soak; `jml_sla_report` green; leaver ≤ 4 h proven with the connector down.
- [ ] Meeting-class guard live; Teams bridge built and OFF; ICS on every session.
- [ ] Integrations catalogue, SoR register, mapping sets with dry run, health dashboard and a migration rehearsal for every enabled connector.
- [ ] `EQ-EXPORT-1.0` engine for all 15 scopes and both layouts; verification suite green (including `XPT_EXPORT_COVERAGE`, AC §AC.13.13 item 9); first quarterly manual Office test recorded.
- [ ] v3.1: estimate, presets and schedules, progress stream, resumable build and download, test-open and `/exports/verify` (FR-P21-44; AC-T25…AC-T29) *(v3.1)*.
- [ ] Import engine with templates and reconciliation; one rehearsal importing a CRM export and a case spreadsheet.
- [ ] `grp` schema, entity partitions across shared-service schemas, grants, walls, secondments, ICSA/GDSA/related-party registers, recharge run, shared artefacts, referrals, consolidated views.
- [ ] CI tests `NO_CASE_DATA_TO_WORKSPACE`, `GROUP_SHARE_SCOPE`, `NO_MEETING_DATA_IN_APPRAISAL`, `NO_VENDOR_SDK_OUTSIDE_ADAPTERS`, `NOTIFICATION_CONTENT_MINIMISED`, `db:entity-rls-catalogue` green.
- [ ] All 52 Gherkin scenarios above passing (42 v3.0 + AD-T19…AD-T23 and AC-T25…AC-T29 v3.1); error codes registered in Appendix F §F.10.4 (v3); events in Appendix F §F.9 (v3); seed data: EQR, ICOPC, Finbyx, Udofin (placeholders), one chambers tenant with a SharePoint test library, one enterprise tenant, two seconded staff, one GDSA, one ICSA.
- [ ] ADRs: workspace topology (D3-40), export package layout (D3-41), group model and entity RLS (D3-42), X-63, X-64.

---

## 14. Open items and legal verification flags

1. **Microsoft SKU** — CS to confirm (no "Business Starter" plan exists; Business Basic assumed) [RD F1.1]. Gate: JML automation ON.
2. **Microsoft details** — group-based licensing and Entra ID P1; `usageLocation` ordering; mailbox delay; shared-mailbox conversion and limits; Audit (Standard) retention; recording licence on Basic; add-on India prices; Exchange application RBAC; `onlineMeeting` options; `Sites.Selected` grant shape; delta under `Sites.Selected`; upload fragment size; Teams notification webhook mechanism **[VERIFY — open (vendor)]** [RD open points 2–3].
3. **Google Workspace** — INR prices, scopes, delegation, endpoints; adapter OFF; no India region [RD F2].
4. **Brevo** — INR prices, CRM endpoint rate class, webhook retries, DPA and sub-processors, DLT support **[VERIFY — open (vendor)]** [RD open point 5].
5. **Adobe Express** private API; **social** access tiers and the Instagram 100 vs 50 inconsistency [RD open points 6–7].
6. **Tally, Zoho Books and payroll tools** — import formats and APIs (adapter spikes).
7. **RFC 8493** tag-file placement and **ZIP64** behaviour of built-in extractors (AC §AC.13.2, §AC.13.10).
8. **Companies Act** — shareholding chain, related-party status, s.188 proviso numbering and r.15(3) thresholds, G.S.R. 464(E) filing-default check; legal names and CINs of Finbyx, Udofin, LawDocs; Equator ADR Institute operating entity (D2-17) — CS [RE open point 8].
9. **Tax** — secondment GST (*Northern Operating Systems*; CBIC Instruction 05/2023-GST); valuation of related-person supplies; Income-tax Act 2025 transfer-pricing successors — tax adviser [RE open point 7].
10. **Labour** — part-time multiple appointments (PF/ESI), OSH Code contract-labour thresholds for intra-group deputation, State registrations for remote staff — payroll adviser and counsel [RE open point 9].
11. **DPDP** — host entity's own s.7(i) basis for secondees; GDSA role matrix sign-off — counsel [RE F5.1]. DPDP substantive duties from 13 May 2027 (build now).
12. **Board decisions** — Directory Owner entity (D3-05); HRMS provider entity; M365 third-party backup (CS/CTO).
