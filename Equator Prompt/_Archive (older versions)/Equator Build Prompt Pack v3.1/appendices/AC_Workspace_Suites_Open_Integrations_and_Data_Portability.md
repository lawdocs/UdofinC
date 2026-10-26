# Appendix AC — Workspace Suites, Open Integrations and Data Portability (v3.0, 23 October 2026)

> **Binding** for P21 (Group Operations, Integrations and Portability) and for the v3 addenda it lists for P01, P02, P04, P07, P10, P14, P16 and P17. Consumed by P16 (Operations Platform), P17 (marketing and growth), P18 (HRMS and payroll) and every phase that produces records a user may export. Read with master NN-10, NN-11, NN-16, NN-22, NN-30, NN-32 and the v3 rules NN-33 (three-tier configuration), NN-35, NN-36, NN-37 (data portability), NN-38 (group boundaries) and NN-40 (open, replaceable integrations); Appendix D (ports, provider registry, resilience), Appendix F (naming, RLS, events, errors), Appendix L (DMS folders, renditions, retention, legal hold), Appendix Q (transfer register, retention schedule, SC controls, PC-39), Appendix S (workforce identity, RBAC, break-glass). Companion: **Appendix AD** (group companies and cross-functional operations).

## AC.0 Purpose, sources, precedence

### AC.0.1 Purpose
This appendix specifies four things the coding agent builds once and every module reuses:
1. **A suite-neutral workspace connector** (`WORKSPACE_PORT`) for identity provisioning, licences, groups, mail, calendar, meetings, files and chat notifications. Its first adapter is Microsoft 365 (management's "Business Starter" — most likely **Business Basic**, SKU to be confirmed by the Company Secretary; D3-04). A Google Workspace adapter is a stub behind a flag.
2. **SharePoint/OneDrive (and Google Drive) integration patterns** in which Equator stays the system of record and the workspace holds only labelled working copies.
3. **An open integrations catalogue** (NN-40): Brevo, Adobe Express, social platforms, accounting, payroll, CRMs, calendars, e-sign and storage, each with a declared system of record per data category, a field-mapping registry entry, import/export, connector health monitoring and a migration rehearsal.
4. **The portable export package** `EQ-EXPORT-1.0` (NN-37, D3-07) for every export scope from a single user to a whole-tenant exit, and the **import and migration** path into Equator.

### AC.0.2 Sources
Research: **[RD]** (Microsoft 365 plans, Graph, Google Workspace, Brevo, Adobe Express, social APIs, export standards, path limits), **[RE]** (group data sharing; used for AC.13 scopes that touch group companies), **[RA]** (Jupitice has no portability: RA F7, EQM-17), **[RC]** (payroll exports, RC E-30), **[RB]** (consent per channel and per group company, RB-23). Primary sources are cited as RD cites them: Microsoft India plan comparison [RD 1]; Exchange Online limits [RD 2]; Microsoft 365 for business security overview [RD 3]; Graph `assignLicense`, `POST /users`, online-meeting application access policy, `onlineMeetings`, transcripts and recordings, throttling [RD 5–9, 13]; OneDrive/SharePoint restrictions and path limits [RD 10, 11]; Win32 naming [RD 12]; Microsoft 365 data residency [RD 14]; Purview licensing [RD 15]; Google Workspace editions, Meet REST API, Directory API, data regions [RD 16–19]; Brevo rate limits, webhooks, security, data storage, OAuth scopes, deals [RD 21–28]; Adobe Express scheduler and Embed SDK [RD 29, 30]; Instagram, LinkedIn, YouTube, X [RD 31–34]; RFC 8493 BagIt [RD 35]; ISO 19005 PDF/A [RD 36]; PKWARE APPNOTE 6.3.10 (ZIP64) [RD 37]; ISO/IEC 29500 [RD 38]; RFC 4180 CSV [RD 39].

### AC.0.3 Precedence
Master §15 applies: master prompt → Appendix G (legal rules) → Appendix V on tiers and keys (X-45) → Appendix B on any fee or tax figure (e.g., priced bulk exports) → Appendix F (names, types, events, errors; this appendix's DDL is additive and registers its codes in F §F.10.4 v3) → Appendix A (states) → P21 → other appendices; under the master's v3 rule this appendix is canonical for schema `xpt`, the export package and the connector catalogue it owns. *(v3.1 fix: order aligned with master §15)* Where this appendix and Appendix D differ on a port's interface, Appendix D governs existing ports and this appendix governs `WORKSPACE_PORT`, `STORAGE_PORT` and the catalogue entries it adds (X-63). Where this appendix and Appendix L differ on export folder names, this appendix governs exports and Appendix L governs the in-platform DMS folder codes (`PLD`, `ANX`, …); AC.13.5 maps one to the other.

### AC.0.4 Registrations for 02 and master §15 (to be copied into those files in the v3 merge)

| Kind | ID | Text | Where specified | Status |
|---|---|---|---|---|
| Requirement | **R-67** | Microsoft 365 today (SKU to be confirmed; design works on Business Basic, Standard or Premium) with Teams and SharePoint; Google Workspace possibly later; documents open in MS Office; downloads as self-explanatory folders and subfolders of Word, Excel and PDF files; open, replaceable integrations (Brevo, Adobe Express, social, accounting, payroll, CRM) with migration in and out | App. AC; P21 §4A–4D | S+V (SKU and vendor items open) |
| Decision | **D3-40** | **Workspace topology and meeting policy.** One suite-neutral `WORKSPACE_PORT`; adapter `m365_graph` is the default; every feature must work on **Business Basic**; staff holding console, Tier-High, sealed or finance access are recommended for **Business Premium** (or Basic plus Entra ID P1, Intune P1 and Defender for Business add-ons), a governed setting; **Keycloak (`eq-portal-ops`, phishing-resistant MFA) is the access control point for every Equator console regardless of SKU**, so no NN control depends on the M365 plan; **Equator-administered proceedings never run on Teams or Google Meet** (locked); Teams may be used for Equator's internal and commercial meetings and, behind a governed per-tenant flag, for a Private Chambers or enterprise tenant's administrative meetings and non-recorded non-administered hearings held in the administering body's own Microsoft tenant (AC.8.4); Google Workspace adapter OFF (`ops.workspace.google.enabled`) because Google offers no India data region [RD F2] | App. AC §AC.2–AC.8 | Decided (CS to confirm SKU) |
| Decision | **D3-41** | **Export package `EQ-EXPORT-1.0`** (implements D3-07). One human-readable folder taxonomy for every scope (`Equator_Export_<Org>_<YYYY-MM-DD>/00_README.pdf`, `01_Organisation_Profile/` … `99_Manifest/`); two layouts with identical content — **Standard folder package** (default for people, parties, employees and small organisations) and **Archival bag** (RFC 8493 BagIt; default for tenant exit, group-company, platform and statutory scopes); ZIP64 with UTF-8 names; ASCII names; path budget (root folder ≤ 40 characters, path below root ≤ 140, so that a package unzipped with Windows "Extract All" into `C:\Users\<name>\Downloads\` — which adds a folder named after the ZIP — stays within the 256-character limit of Office desktop apps [RD F4.2]); DOCX/XLSX/PPTX working copies, PDF/A-2b record copies, byte-exact signed originals, CSV + JSON data, manifest CSV + JSON with SHA-256; schema `xpt` is canonical for exports and imports (supersedes RD's `ops.export_runs` naming) and `POST /v1/me/exports` (Appendix Q PC-39) becomes an alias of `POST /v1/exports` with scope `USER_SELF` | App. AC §AC.13–AC.14 | Decided |
| Cross-file | **X-63** | **Ports and Teams.** Master §4.4 port list and Appendix D §D.0.4 `port` CHECK gain `STORAGE_PORT` and `ACCOUNTING_PORT` (this appendix) and `MARKETING_PORT` and `SOCIAL_PORT` (specified by Appendix Y and built in P17 FR-P17-16/24; Appendix Y has no registration addendum, so this resolution registers them); `WORKSPACE_PORT` and `PAYROLL_EXCHANGE_PORT` are registered once by Appendix Z (FR-P00-V3-Z02) — this appendix extends `WORKSPACE_PORT` (customer connections, meetings, files facade, notifications, audit ingest) without re-registering it. `core.integration_providers` gains `sharepoint_graph`, `onedrive_graph`, `google_drive`, `sftp_generic`, `s3_compatible`, `tally_file`, `zoho_books` (AC.11). RD's recommendation that "hearings must not move to Teams" and management's request to use Teams are reconciled by D3-40: Equator-administered proceedings stay on `VIDEO_PORT` (LiveKit) — locked; tenant-scoped Teams bridge only as AC.8.4 permits; NN-11 is never weakened | Master §4.4; App. D; App. AC §AC.8 | Resolved |

## AC.1 Integration principles (NN-40 made concrete)

| # | Principle | Enforcement |
|---|---|---|
| IP-01 | **Every external tool sits behind a port.** No module imports a vendor SDK; adapters live in `apps/api/src/integrations/adapters/{provider}` (Appendix D convention). | CI lint `NO_VENDOR_SDK_OUTSIDE_ADAPTERS` (ESLint import rule over `apps/*/src/**` except `integrations/adapters/**`). |
| IP-02 | **One system of record (SoR) per data category**, declared in `cfg.system_of_record` (AC.12.1). A mirror never overrides the SoR; conflicts resolve to the SoR. | `cfg.system_of_record` row required before a connector can be enabled (`CFG_SOR_UNDECLARED`, 409). |
| IP-03 | **Documented field mapping** for every object a connector moves, versioned in `cfg.field_mappings` (AC.12.2), maker-checker for any mapping that touches consent, identity or money. | Connector enable blocked while any active object lacks an approved mapping (`CFG_MAPPING_MISSING`, 409). |
| IP-04 | **Import, export and a migration rehearsal** for every connector: the vendor's data can be exported into Equator-native form, and Equator's data can be exported in `EQ-EXPORT-1.0`. A rehearsal is run before go-live and at least once a year (`cfg.migration_rehearsals`). | Connector health turns `amber` when the last rehearsal is older than 365 days and `red` when it is older than `platform.integrations.rehearsal_max_age_days` (L, 400 — a ceiling that may only be tightened) (AC.12.3). *(v3.1 fix)* |
| IP-05 | **No feature depends on a single vendor without a fallback.** Every capability has a degraded mode: `manual_it_desk` for workspace provisioning, `manual_handoff` for social publishing, native CRM for Brevo/HubSpot/Zoho, file export for accounting and payroll tools, LiveKit for meetings, Equator DMS for files. | Each catalogue row in AC.11 names its fallback; acceptance test AC-T07. |
| IP-06 | **Neutrality firewall extends to workforce, marketing and storage tools** (NN-16, NN-38). Case content, party identities, allocation data, caucus material and sealed data never flow to M365, Google Workspace, Brevo, Adobe Express, social platforms, CRMs or accounting tools, except (a) a governed export or mirror requested by an entitled user for a recorded purpose (AC.9, AC.13), and (b) invoice and payment records to the entity's own books (AC.11.5). | Schema validators on every outbound adapter payload reject case identifiers, party names, pleadings, offers and document bytes (`INTEGRATION_POLICY_REJECTED` → port code); CI test `NO_CASE_DATA_TO_WORKSPACE`. |
| IP-07 | **Least privilege, separate credentials per purpose and per tenant.** Application permissions are narrowed (Sites.Selected, application access policies); certificate credentials in AWS Secrets Manager; rotation ≤ 90 days; quarterly access review (Q §7.3). | Collector `integration_credential_age` (fails above 90 days). |
| IP-08 | **Residency is recorded, not assumed.** Every provider row carries `residency`, `residency_attestation_ref` and an `eng.transfer_register` flow when data leaves India (Q §2.6). | Resolver step 3 (D.0.4) drops non-India providers for `personal` data without a residency ADR. |
| IP-09 | **Configuration follows NN-33.** Every connector setting is L, G or T; AC.17 lists them. Routine settings (labels, schedules, budgets within bounds) are tenant-editable without a super admin. | Settings UI tier badges; `cfg.setting_definitions` metadata (Appendix V §V.6.1). |
| IP-10 | **Content minimisation in notifications.** Messages sent through workspace mail, chat or calendar carry no case content: only "You have a new item in Equator", a deep link and, at most, the case number for staff of the administering tenant. | Template lint `NOTIFICATION_CONTENT_MINIMISED`. |

## AC.2 Workspace connector port (`WORKSPACE_PORT`)

### AC.2.1 Scope and consumers
`WORKSPACE_PORT` serves the `hrms`, `ops`, `chambers` and `exports` bounded contexts. It is never called by `cases`, `proceedings`, `hearings`, `notices` or any vertical module. Two connection kinds exist:

| Connection kind | Whose tenant | Typical uses | Who connects it |
|---|---|---|---|
| `workforce` | The legal entity's own workspace (Equator Resolution Service Private Limited first; each group company per Appendix AD §AD.13) | Joiner–mover–leaver (JML) provisioning from HRMS (P18), department and location groups, internal meetings, staff calendars, audit-log ingest, export pushes for the entity's own records | `it_admin` of that entity, with `entity_admin` approval (maker-checker) |
| `customer` | A Private Chambers, enterprise or GRM tenant's own Microsoft 365 or Google Workspace | Export push to the tenant's SharePoint/OneDrive/Drive, optional SharePoint mirror of working files (AC.9), optional Teams bridge (AC.8.4), calendar invites for the tenant's own staff | `chambers_owner`/`chambers_admin` or `tenant_admin`, plus the customer's own Microsoft or Google administrator granting consent |

A `workforce` connection never serves a `customer` purpose and vice versa (separate app registrations, separate secrets, separate `cfg.workspace_connections` rows).

### AC.2.2 Interface (`packages/domain/src/integrations/workspace.ts`)

```ts
export type WorkspaceSuite = 'm365' | 'google' | 'manual';
export type WorkspaceSku =
  | 'M365_BUSINESS_BASIC' | 'M365_BUSINESS_BASIC_NO_TEAMS' | 'M365_BUSINESS_STANDARD' | 'M365_BUSINESS_PREMIUM'
  | 'M365_APPS_FOR_BUSINESS' | 'M365_OTHER' | 'GWS_BUSINESS_STARTER' | 'GWS_BUSINESS_STANDARD' | 'GWS_BUSINESS_PLUS' | 'GWS_OTHER';
export interface WorkspaceCapabilities {           // resolved per connection from cfg.workspace_capability_matrix + detected SKUs
  suite: WorkspaceSuite; skus: WorkspaceSku[];
  provisionUsers: boolean; assignLicences: boolean; manageGroups: boolean; sharedMailboxConversion: boolean;
  sendMail: boolean; calendarEvents: boolean; onlineMeetings: boolean; meetingMaxAttendees: number;
  meetingRecordingLicensed: 'yes'|'no'|'unknown'; transcriptApi: boolean; webinars: boolean;
  conditionalAccess: boolean; deviceManagement: 'none'|'basic'|'intune_p1'|'fundamental'|'advanced';
  endpointDetection: boolean; retentionPolicies: 'none'|'teams_only'|'full'; legalHoldOrVault: boolean;
  dataAtRestIndia: boolean; fileUploadMaxBytesSimple: number; fileUploadResumable: boolean;
  chatNotifications: 'webhook'|'delegated'|'none';
}
export interface WorkspacePort {
  capabilities(connectionId: string): Promise<WorkspaceCapabilities>;
  detectSkus(connectionId: string): Promise<{ skuPartNumber: string; skuId: string; consumed: number; enabled: number }[]>; // M365: GET /subscribedSkus
  createAccount(a: { connectionId: string; employeeId: string; givenName: string; surname: string; upnLocalPart: string;
                     domain: string; sku: WorkspaceSku; usageLocation: 'IN'; groups: string[];
                     tempSecretChannel: 'personal_email'|'sms'; idempotencyKey: string }): Promise<{ externalId: string; upn: string }>;
  setLicences(connectionId: string, externalId: string, add: WorkspaceSku[], remove: WorkspaceSku[]): Promise<void>;
  setGroups(connectionId: string, externalId: string, add: string[], remove: string[]): Promise<void>;
  ensureGroup(connectionId: string, g: { key: string; displayName: string; kind: 'security'|'distribution'|'m365'; mailNickname?: string }): Promise<{ externalId: string }>;
  suspend(connectionId: string, externalId: string, reason: 'exit'|'investigation'|'leave'): Promise<void>;   // disable + revoke sessions
  convertToShared?(connectionId: string, externalId: string, delegateTo: string[]): Promise<void>;           // M365 only (Exchange Online PowerShell runner)
  transferFiles?(connectionId: string, externalId: string, toExternalId: string): Promise<{ transferRef: string }>;
  deleteAccount(connectionId: string, externalId: string): Promise<void>;     // guarded: AC.2.5
  sendMail?(connectionId: string, m: { fromMailbox: string; to: string[]; subject: string; bodyHtml: string; templateId: string }): Promise<{ messageId: string }>; // internal mail only; never case notices
  createMeeting(connectionId: string, e: { organiserExternalId: string; subject: string; start: Date; end: Date; attendees: string[];
                     online: boolean; meetingClass: MeetingClass; icsUid: string }): Promise<{ eventId: string; joinUrl?: string }>;
  updateMeeting(connectionId: string, eventId: string, patch: Partial<{ start: Date; end: Date; attendees: string[]; cancelled: boolean }>): Promise<void>;
  uploadFile(f: { connectionId: string; driveRef: string; path: string; sha256: string; bytes: number; contentType: string;
                  stream: NodeJS.ReadableStream; metadata: Record<string, string>; onConflict: 'fail'|'rename' }): Promise<{ itemId: string; webUrl: string; eTag: string }>;
  getItem(connectionId: string, driveRef: string, itemId: string): Promise<{ eTag: string; lastModifiedAt: Date; lastModifiedBy?: string; sha256?: string }>;
  listChanges?(connectionId: string, driveRef: string, cursor?: string): AsyncIterable<{ itemId: string; eTag: string; deleted: boolean; cursor: string }>;
  createShareLink?(connectionId: string, itemId: string, scope: 'organization'|'specific_people', expiresAt: Date): Promise<{ url: string }>;
  postNotification?(connectionId: string, n: { channelRef: string; text: string; deepLink: string }): Promise<void>;      // AC.10
  pullAuditLogs(connectionId: string, since: Date): AsyncIterable<NormalisedEvent>;   // to eq-log-archive (CERT-In 180 days)
}
export type MeetingClass = 'internal_ops' | 'commercial' | 'tenant_admin' | 'chambers_case_admin' | 'chambers_hearing_unrecorded';
```

Rules:
0. `uploadFile`, `getItem`, `listChanges` and `createShareLink` are a facade over `STORAGE_PORT` (AC.11.8) so that references in Appendices W, X and Z to "push via `WORKSPACE_PORT`" remain valid; the storage adapters do the work.
1. `createMeeting` with `meetingClass` outside the set permitted for the connection (AC.8.4) throws `ProviderError('POLICY_REJECTED')` surfaced as `OPS_MEETING_CLASS_NOT_PERMITTED` (422). No value exists for mediation, conciliation, caucus, Equator-administered arbitration or any sealed matter — the type system itself excludes them.
2. Every M365 calendar meeting that may later need artefacts is **calendar-backed** (`POST /users/{id}/events` with `isOnlineMeeting: true`, `onlineMeetingProvider: "teamsForBusiness"`), because transcript retrieval works only for calendar-backed meetings [RD F1.3, RD 8]. Standalone `onlineMeetings` are used only for `internal_ops` quick calls and require the application access policy (AC.4.3).
3. `sendMail` is for internal operations mail (e.g., offer letters from HR, onboarding emails to a new joiner's personal address are sent through `EMAIL_PORT`, not M365). **Case notices, OTPs and statutory communications never use `WORKSPACE_PORT`**; they stay on `EMAIL_PORT` (SES) and `MESSAGING_PORT` (Appendix D) [RD F1.3]. Locked.
4. `pullAuditLogs` runs hourly for every `workforce` connection (collector `m365_audit_log_ingest`, [RD DI-G]) so the CERT-In 180-day log obligation never depends on the M365 plan [RD F7.1].

### AC.2.3 Adapters

| Adapter code | Suite | Status at v3 | Credential | Notes |
|---|---|---|---|---|
| `m365_graph` | Microsoft 365 | **Default (P21 build)** | Entra app registration, certificate credential (no client secret) | Graph v1.0; Exchange Online PowerShell runner (app-only) for shared-mailbox conversion **[VERIFY — open (vendor): certificate-based app-only auth for the Exchange Online module; conversion cmdlet; shared-mailbox size/licence limit — RD open point 2]** |
| `google_workspace` | Google Workspace | Stub; flag `ops.workspace.google.enabled` **OFF** (approver: CS + DPO, after residency ADR) | Service account with domain-wide delegation impersonating an admin **[VERIFY — open (vendor): scopes and delegation set-up, RD open point 4]** | Directory API users (`POST /admin/directory/v1/users`; suspension via `suspended`; `DELETE` fails under Vault hold; `undelete` ≤ 20 days, super-admin only) [RD F2]; licence via Enterprise License Manager **[VERIFY — open]**; Calendar `events.insert` with `conferenceData.createRequest`; Drive resumable upload and shared drives **[VERIFY — open]** |
| `manual_it_desk` | Any | Always available (fallback) | none | Creates an `ops` IT ticket with a checklist (create account, licence, groups, temporary password to personal channel, confirm UPN back into HRMS); SLA clock per step; used when the connector is down, consent is missing, or the suite is not M365/Google |

Failover policy for `WORKSPACE_PORT` is `none` (identity is stateful; Appendix D §D.0.3): an outage queues JML steps and, after three failed attempts (Appendix Z) or `tenant.hr.workspace.manual_fallback_after_minutes` (T, default 60) whichever comes first, opens `manual_it_desk` tickets for steps on an SLA clock (the leaver revoke at ≤ 4 h is never allowed to wait for the connector; AC.2.4 step L1).

### AC.2.4 Joiner–mover–leaver contract (canonical in Appendix Z §Z.5.3; built in P18 FR-P18-13)
The JML workflow, its HR preconditions, SKU rules and the `hr.jml_events` log are owned by Appendix Z and built in P18. The table below restates only the connector-side contract that `WORKSPACE_PORT` must honour; where it and Appendix Z differ, Appendix Z governs. P21 adds the customer-connection kind, the capability resolver, meeting and file operations, notifications and audit ingest.

| Step | Trigger (HRMS event, P18) | `WORKSPACE_PORT` calls | SLA | Locked guards |
|---|---|---|---|---|
| J1 Joiner | `equator.hr.employee.activated.v1` (offer accepted, background verification passed, NDA and acceptable-use e-signed — Q SC-21) | `createAccount` (UPN from `tenant.hr.workspace.upn_pattern`, default `{first}.{last}`, collision suffix middle initial then digit; Indic names transliterated by the stored table in `cfg.transliteration_tables`) → set `usageLocation = "IN"` **before** licence assignment **[VERIFY — open (vendor): mandatory ordering, RD F1.3]** → `setLicences` per SKU rule (AC.3.3) → `setGroups` (department, location: Delhi/Noida/Jaipur/remote, legal entity) → temporary credential to the **personal** channel on file via `EMAIL_PORT`/`MESSAGING_PORT` with force-change at first sign-in | Account ready ≤ 1 working day; mailbox readiness polled (`GET /users/{id}/mailboxSettings` until 200; delay **[VERIFY — open]**) | No account before background check and NDA (`HR_PREJOIN_CHECKS_INCOMPLETE`, 409); UPN never reuses a former employee's UPN within 365 days |
| M1 Mover | `equator.hr.employee.role_changed.v1`, `equator.hr.employee.transferred.v1` (department, location or entity transfer; Appendix Z §Z.4.8, §Z.17.2) | diff of groups and SKU; `setGroups`, `setLicences` | ≤ 1 working day | SKU sufficiency check (AC.3.3) runs before any console role is granted |
| L1 Leaver | `equator.hr.employee.exit_effective.v1` | `suspend` (`accountEnabled=false` + `revokeSignInSessions`), remove from groups | **≤ 4 h** (`iam.leaver_revoke_hours`, Q SC-01; L floor 4, tenant may only tighten) | Keycloak `eq-portal-ops` sessions revoked in ≤ 60 s independent of M365 (S §1.3) |
| L2 Leaver continuity | L1 + 1 day | `convertToShared` (delegates: manager), `transferFiles` (OneDrive to manager), remove licence | T+1 working day | Gross-misconduct exit (`termination_for_cause`) runs L1 immediately on HR plus second approver (NN-36 maker-checker) |
| L3 Deletion | `deletion_due_at` = exit + `tenant.hr.workspace.delete_delay_days` (T per Appendix Z, default 90, bounds 30–365) | `deleteAccount` | — | Blocked while any legal hold, open grievance, POSH matter, disciplinary case or investigation references the employee (`HR_WORKSPACE_DELETE_BLOCKED_HOLD`, 409) |

Every step writes `audit.append_event` and an `hr.jml_events` row (owned by P18; columns `employee_id`, `step`, `requested_at`, `completed_at`, `provider_ref`, `sla_met`). Collector `jml_sla_report` (daily) reports leaver revoke times [RD DI-G].

### AC.2.5 Account and data deletion guard
`deleteAccount` is executed only by `WorkspaceDeletionWorkflow`, which checks (a) holds and open matters (AC.2.4 L3), (b) that mailbox and OneDrive content required by Appendix Q retention classes has been exported to the entity's records store (Equator `xpt` export of scope `EMPLOYEE_FILE` with mailbox export attached by the `it_admin`, or a documented decision that mailbox content is not a record), and (c) maker-checker (`it_admin` maker, `hr_manager` or `entity_admin` checker). M365 is never the system of record for any record Appendix Q §2.8 retains, because Business Basic has no organisation-wide retention policies for Exchange, SharePoint or OneDrive [RD F1.2, RD 15].

## AC.3 Capability matrix by plan and the upgrade path

### AC.3.1 Plan facts (India price page and service descriptions, 23 October 2026)
Microsoft's India comparison page lists Business Basic (₹170 per user per month, annual commitment, GST extra), Business Basic (no Teams) (₹130), Business Standard with Copilot (₹1,955), Business Premium with Copilot (₹2,660), the no-Teams variants of those, and Apps for business (₹830). **No plan is named "Business Starter"**; that is a Google Workspace edition name [RD F1.1, RD 1]. Prices are vendor list prices, exclusive of GST at 18% **[VERIFY — open (tax): GST rate on SaaS subscriptions; confirm on invoice]**, and are stored as reference data (`cfg.vendor_price_refs`), never hard-coded. Google lists Business Starter at USD 7, Business Standard USD 14 and Business Plus USD 22 per user per month (INR not shown) [RD F2, RD 16]. Every "for business" Microsoft plan and every Google Business edition has a 300-user cap [RD 3, RD 16].

### AC.3.2 Capability matrix (seed of `cfg.workspace_capability_matrix`)
Cells are what Equator may rely on. "✗" means the UI hides the action and the fallback in the last column applies. **[NC]** marks a fact the research could not confirm; the matrix treats it as unavailable until the tenant's own detection or the CS confirms it.

| Capability | M365 Business Basic | M365 Business Standard | M365 Business Premium | Google Business Starter | Google Business Standard / Plus | Equator behaviour when unavailable |
|---|---|---|---|---|---|---|
| Create/disable users, groups, licences by API | ✓ Graph `POST /users`, `assignLicense` [RD 5, 6] | ✓ | ✓ | ✓ Directory API [RD 18] | ✓ | `manual_it_desk` ticket |
| Group-based licensing | **[NC]** whether Entra ID P1 is needed [RD 20] — use direct assignment | **[NC]** | ✓ (P1 included) | n/a | n/a | Direct per-user assignment |
| Mailbox | 100 GB primary (service description; one Microsoft page still says 50 GB — check tenant quota) [RD 2, RD F1.2] | 100 GB | 100 GB + archive auto-expanding to 1.5 TB [RD 2] | 30 GB pooled per user [RD 16] | 2 TB / 5 TB pooled [RD 16] | Large records stay in Equator DMS, never in mail |
| Recipient rate limit | 10,000 recipients per 24 h per mailbox [RD 2] | same | same | **[NC]** | **[NC]** | Bulk mail uses `EMAIL_PORT` (SES) or `MARKETING` (Brevo), never M365 |
| Max message size | 150 MB internal; 112 MB once routed outside Microsoft; defaults 35 MB send / 36 MB receive [RD 2] | same | same | **[NC]** | **[NC]** | Links to Equator secure download, never attachments of records |
| OneDrive | 1 TB per user [RD 1, 4] | 1 TB | 1 TB | pooled (above) | pooled | — |
| Office apps | **Web and mobile only** [RD 4] | Desktop | Desktop | Web (Docs/Sheets; Office files editable) **[NC]** | same **[NC]** | Exports tested in Office for the web (AC.13.11) |
| Teams / Meet meetings | up to 300 attendees [RD 4] | 300 | 300 | Meet 100 participants, **no recording** [RD 16] | 150 / 500, recording [RD 16] | LiveKit (Appendix D §D.5.1) |
| Meeting recording licensed | **[NC]** [RD F1.3] | **[NC]** | **[NC]** | ✗ | ✓ (artefacts to organiser's Drive) [RD 17] | Equator never relies on workspace recording (AC.8) |
| Transcript/recording retrieval by API | Graph transcripts (`.vtt`) and recordings (`.mp4`), not metered since 25 Aug 2025; tenant admin can disable (403 `GraphAccessToTranscriptsDisabled`) [RD 9] | ✓ | ✓ | ✗ | Meet REST artefacts [RD 17] | Not used for any case or appraisal purpose (AC.8.6) |
| Webinars | not listed [RD 1] | ✓ "included with Teams" [RD 1] | ✓ | — | — | Public webinars via LiveKit or a CMS-embedded stream |
| Teams Premium features (custom meeting templates) | ✗ [RD 8] | ✗ | ✗ | n/a | n/a | Meeting options set per meeting by API **[VERIFY — open (vendor): `onlineMeeting` properties for recording/transcription/lobby]** |
| Identity protection | Entra ID Free, **security defaults** (MFA on, all-or-nothing) [RD 3] | Entra ID Free | **Entra ID P1 — Conditional Access** [RD 3] | ✗ context-aware access [RD 16] | ✗ (Enterprise editions) [RD 16] | Keycloak `eq-portal-ops` enforces phishing-resistant MFA and device/IP policy for consoles (X-24) |
| Device management | Basic Mobility and Security (subset of Intune) [RD 3] | same | **Intune Plan 1** [RD 3] | Fundamental endpoint management [RD 16] | Fundamental / Advanced (Plus) [RD 16] | Console access refused from non-compliant devices where Keycloak device policy applies; SKU rule (AC.3.3) |
| Endpoint detection and response | ✗ | ✗ | **Defender for Business** [RD 3] | ✗ | ✗ | SC-15 met only on Premium or add-ons |
| Email security | EOP anti-malware/spam/phishing [RD 3] | same | **Defender for Office 365 P1** (Safe Links, Safe Attachments) [RD 3] | **[NC]** | **[NC]** | — |
| Retention policies (Exchange/SharePoint/OneDrive) | **Teams chats/channels only** [RD 15] | Teams only | ✓ [RD 15] | ✗ (no Vault) [RD 16] | Plus: Vault [RD 16] | **Equator is the record**; workspace copies are working copies only |
| Audit (Standard) | ✓ [RD 15]; retention period **[NC]** | ✓ | ✓ | **[NC]** | **[NC]** | Hourly ingest to `eq-log-archive` (Object Lock, India, 400 days) |
| Data at rest in India | ✓ Product Terms commitment for India-default tenants (Exchange, SharePoint/OneDrive, Teams, Microsoft 365 Copilot) [RD 14] | ✓ | ✓ | ✗ (regions: US, EU, no preference; Starter not eligible) [RD 19] | ✗ India not offered [RD 19] | Google adapter OFF; residency ADR required to enable |
| Simple file upload limit | 250 MB per `PUT …/content`; larger by upload session; max file 250 GB [RD 10, F1.3] | same | same | resumable upload **[NC]** | same | Chunked push (AC.13.9) |
| Folder and sync limits | ≤ 50,000 sub-items per shared folder; sync ≤ 300,000 items recommended; decoded path ≤ 400 characters [RD 10, 11] | same | same | **[NC]** | **[NC]** | Export layout splits case folders (AC.13.6) |

### AC.3.3 Licence policy and the locked SKU-sufficiency rule
`tenant.hr.workspace.sku_rules` (Appendix Z key; T tier with maker-checker; approver `it_admin` + security lead), default [RD DI-A3]:

| Holder | Default SKU | Reason |
|---|---|---|
| Staff with any Equator console role at Tier-High, sealed, finance, payroll, `platform_admin`, `it_admin`, `registrar`, `case_counsel`, `escrow_officer`, `dpo`, security | **Business Premium** (or Basic + Entra ID P1 + Intune P1 + Defender for Business add-ons; add-on availability and India price **[VERIFY — open (vendor)]**) | Conditional Access, device compliance and EDR (Q SC-01, SC-03, SC-14, SC-15 cannot be met on Basic alone) [RD F1.2] |
| Other staff, including case managers working from home | **Business Basic** | Mail, Teams, OneDrive, web Office |
| Contractors, interns without a mailbox need, external committee members | No mailbox; guest access where needed | Minimisation |

**Locked rule** `HR_WORKSPACE_SKU_INSUFFICIENT` (409): a privileged Equator console role (list above) cannot be granted to a user whose workspace account lacks Conditional Access plus device management, unless `security_lead` (Appendix AE §AE.1.1) records an exception with expiry ≤ 90 days and a compensating control (Keycloak device-bound passkey, IP allow-list). Collector `workspace_sku_role_check` runs daily; any unexcepted hit is a High finding [RD DI-G].

### AC.3.4 Upgrade decision guide (shown on SCR-P21-03 for the CS and IT admin)

| Need | Smallest change that delivers it | Notes |
|---|---|---|
| Conditional Access, risk-based sign-in | Business Premium for the affected users, or Entra ID P1 add-on | Keycloak already enforces MFA for Equator consoles; this protects mail and files |
| Company-device management and EDR (SC-15) | Business Premium, or Intune P1 + Defender for Business add-ons | Required before remote case managers handle Tier-High matters on company laptops |
| Organisation-wide retention or legal hold on mail and files | Business Premium (or E3+) [RD 15] | Not needed for Equator records; needed only if the entity wants M365 to retain its own correspondence |
| Desktop Office apps | Business Standard, Premium or Apps for business | Exports are verified in Office for the web, so Basic users are not blocked |
| Webinars | Business Standard or Premium [RD 1] | Or LiveKit-based webinar room |
| Teams meeting templates | Teams Premium add-on [RD 8] | Not required by any Equator feature |
| Third-party backup of mail and OneDrive | Separate vendor (decision **OFF pending CS**, RD F6 tier T3) | Equator records do not depend on it |

## AC.4 Permission model

### AC.4.1 Application versus delegated permissions
- **Application permissions** (client-credentials flow, no signed-in user) suit JML automation, audit ingest and export pushes. They are tenant-wide unless narrowed: `Sites.Selected` for SharePoint, Teams application access policies for online meetings, and Exchange application RBAC / application access policy for mail **[VERIFY — open (vendor): Exchange application RBAC mechanism for scoping `Mail.Send`, RD open point 2]** [RD F1.3].
- **Delegated permissions** suit "act as the signed-in staff member" features — adding a meeting to *my* calendar, saving *my* export to *my* OneDrive. The user signs in through the Microsoft consent screen; Equator stores refresh tokens encrypted (`*_enc`, per-tenant key) and never uses them outside the user's own action.
- **Admin consent** is required for every application permission. Granting consent is recorded as a `normal` change record (`eng.change_records`, Q §7.3) with the consent screenshot hash and the granted scopes.

### AC.4.2 App registrations (least privilege)

| Registration | Tenant | Type | Permissions (least privileged first) | Credential |
|---|---|---|---|---|
| `eq-hrms-provisioner` | Each group entity's own workforce tenant | Single-tenant, application | `User.Create`; `User.ReadWrite.All` (disable, update manager); `LicenseAssignment.ReadWrite.All`; `GroupMember.ReadWrite.All`; `Group.Create` (department groups) [RD F1.3] | Certificate; Secrets Manager; rotation ≤ 90 days |
| `eq-ops-collab` | Workforce tenant | Single-tenant, application | `Sites.Selected` (granted per site); `Calendars.ReadWrite` (scoped to named mailboxes **[VERIFY — open]**); `OnlineMeetings.ReadWrite.All` with an application access policy limited to members of `eq-meeting-hosts` (never `-Global`); `AuditLog.Read.All` and Office 365 Management Activity API subscription for audit ingest **[VERIFY — open (vendor): exact permission names for Management Activity API]** | Certificate |
| `eq-tenant-connector` | Multi-tenant (Equator publisher), installed into a **customer** tenant by the customer's admin | Multi-tenant, application + delegated | Application: `Sites.Selected` only (customer admin grants the chosen site); delegated (per user): `Files.ReadWrite` (save my export), `Calendars.ReadWrite` (add to my calendar), `OnlineMeetings.ReadWrite` (Teams bridge, AC.8.4) | Certificate (publisher-side); customer can revoke consent at any time |
| `eq-user-signin` (optional) | Multi-tenant | Delegated OIDC | `openid`, `profile`, `email` — sign-in to Equator portals with a work account brokered by Keycloak (enterprise SSO, Appendix S) | — |

`Files.ReadWrite.All` and `Sites.ReadWrite.All` application permissions are **forbidden** (Locked; CI scans the manifest JSON in `infra/entra/*.json` and fails on them).

### AC.4.3 Teams application access policy
For `OnlineMeetings.ReadWrite.All` the tenant admin runs `New-CsApplicationAccessPolicy` and `Grant-CsApplicationAccessPolicy` for each member of `eq-meeting-hosts` (per user or `-Global`; propagation up to 30 minutes) [RD 7]. Equator's runbook grants **per user** from the group membership list; a nightly job reconciles policy grants with the group and opens an IT ticket for drift **[VERIFY — open (vendor): whether a group-based assignment exists for this policy type]**.

### AC.4.4 Google equivalents
Service account with domain-wide delegation, restricted to the Admin SDK Directory scopes for provisioning and Drive scopes for export push; delegated OAuth for per-user calendar and Drive. Every scope is **[VERIFY — open]** until the adapter spike (RD open point 4).

## AC.5 Throttling, retries and idempotency

| Limit (Microsoft Graph) | Value [RD 13] | Equator handling |
|---|---|---|
| Global | 130,000 requests per 10 s per app across all tenants | Per-app token bucket in Redis at 50% of the limit |
| Identity and access (tenant size M, 50–500 users) | 5,000 resource units per 10 s per app per tenant; `GET users` = 2 RU | Per-tenant bucket; directory reads cached 15 min |
| Identity writes | 3,000 requests per 2 min 30 s per app per tenant; tenant-wide 18,000 writes per 5 min | JML queue concurrency 4 per tenant |
| Conditional Access APIs | 1 request/s per tenant | Read-only use; no writes from Equator |
| Teams meeting information | 2,000 meetings per user per month | Meeting host pool (`eq-meeting-hosts`) spreads load |
| Response on throttle | `429` with `x-ms-throttle-scope`, `x-ms-throttle-information`; `Retry-After` when present | Honour `Retry-After`; else full-jitter exponential backoff (Appendix D §D.0.3); map to `RATE_LIMITED` |
| Bulk backfills | `x-ms-throttle-priority: low` header | Used for initial user import, audit backfill, export pushes |

Brevo: General tier contacts 10 rps (36,000/h), events 10 rps, **all other endpoints 100 requests per hour** on non-Enterprise plans; no `Retry-After` guidance [RD 21]. Equator budget `tenant.mkt.brevo.max_requests_per_hour` (T, default 80, bounds 1–95% of the plan limit recorded in the provider row; one budget for the account, shared by `CRM_PORT` and `MARKETING_PORT` through one token bucket); bulk import for > 50 records; queue-based, never synchronous per UI action [RD F3.1].

Idempotency: every side-effecting workspace call goes through `core.outbox` with `idempotency_key = sha256(connection_id|object|action|version)`; `createAccount` first queries by `employeeId` extension attribute (M365 `onPremisesExtensionAttributes` or a directory schema extension **[VERIFY — open]**) so retries never create duplicate accounts.

## AC.6 Data residency

| Suite / tool | Location facts | Record in `eng.transfer_register` | Rule |
|---|---|---|---|
| Microsoft 365 (India-default tenant) | India is a Local Region Geography (Chennai, Mumbai, Pune); Product Terms data-residency commitment covers Exchange Online, SharePoint/OneDrive, Teams and Microsoft 365 Copilot data at rest; Advanced Data Residency and Multi-Geo are add-ons; default geography is fixed at tenant creation [RD 14] | None if the tenant's data location shows India; otherwise a flow row `M365_<entity>_<geo>` | The `it_admin` records the tenant's data location (admin centre → Settings → Org profile → Data location) as evidence on the connection row; Advanced Data Residency is never assumed [RD F1.3] |
| Microsoft 365 (customer tenant) | Customer's own geography | Customer is the controller of its copy; Equator records the destination geography on the export delivery row | Push of a `personal`-class export to a non-India customer tenant requires the requester's acknowledgement (DPDP s.16; not restricted unless notified) |
| Google Workspace | No India data region; regions US/EU only for eligible editions; Starter not eligible [RD 19] | Mandatory row before enabling | Adapter OFF until a residency ADR, DPO approval and a transfer-register row |
| Brevo | Servers in the EU (OVH France and Germany; Google Cloud Belgium) [RD 26] | Row `BREVO_EU` (data class `personal`, CRM and marketing data only) | Activation requires the DPA and sub-processor list on file **[VERIFY — open (vendor): DPA, sub-processors]** |
| Adobe Express | **[VERIFY — open (vendor)]** | Row `ADOBE_EXPRESS` if personal data in assets | Assets must contain no personal data other than consented brand ambassadors |
| Social platforms | Platform-defined | Rows per platform for analytics pulls | Only public brand content goes out; no personal data except consented testimonials (Appendix P rules) |

## AC.7 Tenant configuration runbook (for the Company Secretary and the IT admin)

The P21 build ships this runbook as `docs/runbooks/workspace-m365-setup.md` and as a guided checklist on SCR-P21-02. Each step records evidence on `cfg.workspace_connections.setup_evidence` (JSON: step, actor, timestamp, artefact hash).

| # | Step | Who | How | Evidence |
|---|---|---|---|---|
| 1 | **Confirm the SKU.** Management calls the plan "Business Starter"; Microsoft has no plan of that name [RD F1.1]. | CS | Microsoft 365 admin centre → Billing → Your products; or let Equator call `GET /subscribedSkus` after step 4. The Basic SKU part number is commonly `O365_BUSINESS_ESSENTIALS` **[VERIFY — open (tenant)]** | Screenshot hash; `detectSkus` output stored |
| 2 | Record the tenant's data location | IT admin | Admin centre → Settings → Org profile → Data location [RD F1.3] | Screenshot hash on connection row; transfer-register decision |
| 3 | Verify domains and decide UPN pattern | IT admin + HR | Domains verified in admin centre; UPN pattern setting (AC.17) | Setting change record |
| 4 | Create app registrations `eq-hrms-provisioner` and `eq-ops-collab` with certificate credentials | IT admin | Entra admin centre → App registrations; upload the public certificate generated by Equator (private key never leaves AWS) | App IDs; certificate thumbprints |
| 5 | Grant admin consent to the least-privileged permissions only | Global admin of the tenant | Consent screen; record as `normal` change | Change record ID |
| 6 | Grant `Sites.Selected` on the named SharePoint site(s) | SharePoint admin | Site permission grant for the app (Graph `POST /sites/{id}/permissions` **[VERIFY — open (vendor): request shape and role values]**) | Site ID; role |
| 7 | Create groups `eq-meeting-hosts`, department and location groups | IT admin (or Equator via `ensureGroup`) | Admin centre or API | Group IDs mapped in `cfg.workspace_group_map` |
| 8 | Teams application access policy for meeting hosts | Teams admin | `New-CsApplicationAccessPolicy` / `Grant-CsApplicationAccessPolicy` per host [RD 7] | PowerShell transcript hash |
| 9 | Confirm security defaults are ON (Basic/Standard) or Conditional Access policies exist (Premium) | IT admin | Entra → Properties → Security defaults | Screenshot hash |
| 10 | Check mailbox quotas | IT admin | Exchange admin: `ProhibitSendReceiveQuota` [RD F1.2] | Value recorded |
| 11 | Decide transcript access | IT admin + DPO | Tenant may disable Graph transcript access [RD 9]; Equator does not need it for any case or appraisal purpose | Setting recorded |
| 12 | Enable audit ingest | IT admin | Management Activity API subscription; Entra sign-in/audit log read | First ingest batch hash |
| 13 | Decide M365 backup (third-party) | CS + CTO | Decision record (`OFF pending CS` by default) [RD F6] | Decision log entry |
| 14 | Run the connector self-test | IT admin | SCR-P21-02 "Test connection": read SKUs, create and delete a test group, upload and delete a 1 KB file in the granted site, create and cancel a calendar event | Self-test report (all green) |
| 15 | Turn on JML automation | `entity_admin` (checker) | Flag `tenant.hr.workspace.jml_automation` ON (G) | Change request approved |

## AC.8 Mail, calendar and meetings — and the Teams versus LiveKit policy

### AC.8.1 Mail
Workforce mail (staff-to-staff, staff-to-customer commercial mail) runs in the workspace. Equator uses `WORKSPACE_PORT.sendMail` only for internal operational mail from named mailboxes (`hr@`, `ops@`), scoped by the Exchange application policy. **Locked:** case notices, service of process, OTPs, statutory and regulatory communications, recovery-related messages and anything that must be proven delivered go through `EMAIL_PORT` (SES ap-south-1), `MESSAGING_PORT` and `POSTAL_PORT`, never through M365 or Gmail [RD F1.3]. A staff member who corresponds with a party about a case from a workspace mailbox must file the correspondence into the case (`COR` folder) using the "File to Equator" action (delegated `Mail.Read` on the user's own mailbox, user-initiated, one message at a time **[VERIFY — open (vendor): Outlook add-in vs Graph-only approach decided at spike]**); the filed copy becomes the record.

### AC.8.2 Calendar
- Every hearing, session and case-management conference has its **schedule of record in Equator** (`core.sessions`, P04). Invitations to participants carry an **ICS attachment** (iCalendar, RFC 5545 **[NC — standard not in research; confirm at spike]**) generated by Equator with a stable `UID` = session ID, so any calendar client works without a workspace connector.
- Staff may opt in to "Add my Equator sessions to my work calendar" (delegated `Calendars.ReadWrite`). The event body contains only the Equator deep link and the session time; the subject is `Equator session — {case number}` for staff of the administering tenant and `Equator session` for others (IP-10). Updates and cancellations flow one way (Equator → calendar).
- Internal and commercial meetings (sales demos, onboarding calls, customer-success reviews, staff meetings, training) are created in the workspace calendar from the Operations Platform (P16) with `meetingClass = internal_ops | commercial`, and the join URL is stored on the CRM activity.

### AC.8.3 Meeting classes and the permitted platform

| Meeting class | Examples | Permitted platform | Recording | Tier |
|---|---|---|---|---|
| Equator-administered proceeding (any mechanism) | Mediation joint session, caucus, conciliation, negotiation round, arbitration hearing, case-management conference, witness examination, emergency arbitrator hearing, committee challenge hearing | **`VIDEO_PORT` (LiveKit, India) only** | Per NN-11 and P04 FR-P04-41 (arbitration with all consents and tribunal direction; never mediation, conciliation, negotiation or caucus) | **L** |
| Sealed or safety matters (POSH inquiry, FAM safety-flagged, INS health) | IC inquiry hearings | `VIDEO_PORT` only | Per sealed-service rules (P09) | **L** |
| `internal_ops` | Staff stand-ups, training, HR one-to-ones, IT support | Workspace (Teams default; Google Meet when that adapter is ON) | Tenant policy; never used for appraisal scoring (AC.8.6) | T |
| `commercial` | Sales demos, onboarding, customer-success reviews, partner calls | Workspace | Tenant policy with recorded consent of external attendees | T |
| `tenant_admin` | A chambers' or enterprise's internal administration meeting with no case content | Tenant's own workspace via `customer` connection | Tenant policy | T |
| `chambers_case_admin` | Scheduling or logistics call in a **non-administered** chambers matter (no evidence, no submissions) | Teams bridge in the chambers' own tenant, flag `tenant.chm.meetings.teams_bridge` (G, default OFF) | **Never recorded or transcribed** | G |
| `chambers_hearing_unrecorded` | Non-administered arbitration or expert-determination hearing that the parties and the tribunal agree to hold on Teams | Teams bridge in the chambers' own tenant, same flag plus all-party written consent per session | **Never recorded or transcribed**; if a record is needed, the hearing moves to LiveKit | G |

No meeting class exists for mediation, conciliation or negotiation on Teams in any tenant: the confidentiality analysis in AC.8.5 shows Equator cannot guarantee NN-11 there.

### AC.8.4 Conditions for the Teams bridge (chambers and enterprise tenants)
The flag `tenant.chm.meetings.teams_bridge` may be turned ON (approver: `chambers_owner` as maker, Equator `legal_reviewer` as checker) only when all of the following are recorded:
1. The meeting is hosted in the **administering body's own Microsoft tenant** (the chambers or the neutral's practice) through a `customer` connection. Hosting in **a party's tenant is forbidden** (Locked; `OPS_MEETING_HOST_TENANT_IS_PARTY`, 409): a lender's or employer's IT administrators and eDiscovery tools would have access to the other side's appearance, chat and shared material.
2. The tenant admin attests (uploaded evidence) that the Teams meeting policy applied to `eq-meeting-hosts` disables cloud recording, transcription and AI meeting recap for those organisers; Equator also sets per-meeting options through Graph where the API allows **[VERIFY — open (vendor): `onlineMeeting` properties such as `allowRecording`, `allowTranscription`, `lobbyBypassSettings`, `allowedPresenters` and whether they override tenant policy]**. Without both, the bridge stays OFF.
3. Every participant has given written consent to the online platform for that session (FR-P04-12 s.30 pattern applied by analogy), recorded in `core.consent_records` with purpose `online_platform_teams`.
4. Lobby on; only invited identities admitted; meeting chat disabled or the neutral confirms it is not used for submissions (documents go through the Equator DMS, never Teams chat or Teams file share).
5. Attendance is recorded in Equator by the neutral at session end (the Teams attendance report is not the record).

### AC.8.5 Confidentiality analysis — LiveKit versus Teams

| Dimension | LiveKit via `VIDEO_PORT` (Equator) | Microsoft Teams (customer or Equator tenant) | Consequence |
|---|---|---|---|
| Recording control | Equator API refuses recording for mediation, conciliation, negotiation and caucus rooms; arbitration needs consents and a tribunal direction (FR-P04-41) | Controlled by the hosting tenant's meeting policy; any organiser or permitted presenter may start recording or transcription where policy allows; licence position on Basic **[NC]** [RD F1.3] | NN-11 cannot be enforced by Equator on Teams → no mediation on Teams (Locked) |
| Caucus isolation | Separate rooms with server-minted, room-scoped tokens; isolation enforced by the SFU (Appendix D §D.5.1) | Breakout rooms managed by the organiser inside one meeting **[VERIFY — open (vendor): breakout-room isolation and presenter access]** | Caucus never on Teams |
| AI features | No AI on session audio except the consented, tribunal-directed transcript in arbitration | Copilot or intelligent recap may process transcripts where licensed and enabled **[NC]** | Bridge requires the attestation in AC.8.4(2) |
| Data location | LiveKit region `india`; egress to S3 ap-south-1 Object Lock [D.5.1] | Customer tenant geography; India commitment only for India-default tenants [RD 14] | Recorded on the session row |
| Who can access artefacts | Equator evidence store, RLS, access log | Tenant admins, eDiscovery, organiser's mailbox and OneDrive | Hosting in a party's tenant forbidden |
| Identity and attendance | OTP plus optional face match; attendance register ledgered (FR-P04-42) | Work/guest/anonymous join per tenant settings | Neutral confirms attendance in Equator |
| Evidence chain | Attendance, recording hashes in `core.evidence_ledger`; s.63(4) certificate (NN-10) | Outside Equator's ledger | Only unrecorded hearings permitted on the bridge |
| PSTN and low bandwidth | LiveKit SIP over Exotel; audio-only mode (FR-P04-40) | Audio conferencing licence-dependent **[NC]** | — |
| Neutral's duty of equal treatment | Same platform, same features for all sides | Parties outside the host tenant join as guests with fewer features **[NC]** | Bridge only with all-party consent per session |

### AC.8.6 Workforce meeting data is not performance data
Meeting attendance, presence status, transcripts and Meet/Teams analytics are never inputs to attendance, work measurement or appraisal (NN-35). Google states that the Meet REST API "isn't intended for performance tracking or user evaluation" [RD F2, RD 17]; Equator applies the same rule to Teams. CI test `NO_MEETING_DATA_IN_APPRAISAL` fails if any HRMS scoring table reads a workspace meeting source.

## AC.9 Files — SharePoint, OneDrive and Google Drive integration patterns

### AC.9.1 System of record
**Equator is the system of record for every case document**: originals in the WORM evidence bucket with Object Lock and the evidence-ledger hash (Appendix L §1.1, NN-22). A SharePoint or OneDrive copy is a **working copy** or a **delivered export**, never the record. Three patterns exist:

| Pattern | Direction | Use | Flag / tier |
|---|---|---|---|
| P-1 Export push | Equator → workspace, one-off | Deliver an `EQ-EXPORT-1.0` package (AC.13) into a library or OneDrive folder | `tenant.xpt.push_to_workspace` (T, default ON once a `customer` connection exists) |
| P-2 Working-copy mirror | Equator → workspace, continuous, one way | A chambers or enterprise team keeps DOCX/XLSX working copies of its **own side's** or its administered matters' documents in its SharePoint library | `tenant.chm.sharepoint_mirror` / `tenant.ent.sharepoint_mirror` (G, default OFF; approver tenant owner + Equator DPO checker) |
| P-3 Return of working files | Workspace → Equator, user-initiated | A user picks an edited working copy and files it into Equator as a new **draft** (`PRIVATE_DRAFT`) or a new version where the DMS rules allow | Always user-initiated; no automatic inbound sync |

There is **no automatic two-way sync** (Locked). An on-record, served or issued document is never replaced by a workspace file; a returned file becomes a new draft or a new version subject to Appendix L §1.3 supersession rules and neutral leave after service.

### AC.9.2 What may be mirrored
Mirrorable: documents whose audience includes the tenant's own side (`OWN_SIDE`, `ALL_PARTIES`, `REGISTRY` for the administering chambers tenant), at confidentiality tier `standard`, and tier `high` only with a per-case opt-in by the `chambers_owner` or `tenant_admin` and a library marked `eq_high_tier_approved` (column). **Never mirrored** (Locked): `CAU` caucus notes, `NEUTRAL_ONLY` shares, `INT` folder items to anyone outside the registry, other sides' `PRIVATE_DRAFT`, sealed stores (POSH, health, safety), KYC media, neutral annotations and deliberations, recordings and transcripts of any proceeding, and any document under a confidentiality ring the tenant is not inside. For mediation and conciliation matters the mirror is OFF unless every party to the mediation agreement has consented to working copies leaving the platform (consent purpose `working_copy_mirror`).

### AC.9.3 Library layout, naming and metadata mapping
Path in the library: `/{Library}/Equator/{CaseFolder}/{ExportFolder}/{FileName}` where `CaseFolder`, `ExportFolder` and `FileName` follow AC.13.5–AC.13.7 (same names as an export, so a later export and the mirror line up). Library columns (created by Equator on connection if the `Sites.Selected` role allows; otherwise the admin creates them from the checklist):

| Library column | Type | Source |
|---|---|---|
| `EQ_Case_No` | Single line | `core.cases.case_no` (slashes → hyphens) |
| `EQ_Record_Class` | Choice | Appendix L system folder code mapped to the export folder (AC.13.5) |
| `EQ_Document_Id` | Single line | `core.documents.id` |
| `EQ_Version` | Number | `core.document_versions.version_no` |
| `EQ_SHA256` | Single line | Version or rendition hash |
| `EQ_Is_Record_Copy` | Yes/No | Always "No" for mirror files; "Yes" only for files inside a delivered export that are byte-exact originals |
| `EQ_Retention_Class` | Single line | Appendix Q class (informational; Equator enforces retention) [RD F4.4] |
| `EQ_Confidentiality` | Choice | `standard` / `high` |
| `EQ_Mirrored_At` | Date/time | Mirror run time (IST display) |
| `EQ_Source_Link` | Hyperlink | Deep link to the document in Equator |

Every mirrored DOCX/XLSX carries a document property `EquatorStatus = "Working copy — the record is in Equator"` and, for PDFs, a first-page banner on a **rendition** (never on a signed original) [RD F4.3].

### AC.9.4 Change detection and sync conflicts

| Situation | Detection | Equator action |
|---|---|---|
| New version in Equator, workspace copy unchanged since last mirror | Stored `eTag` equals current `eTag` (`getItem`) | Overwrite in place with the new version; update columns |
| New version in Equator, workspace copy edited by a user | `eTag` differs | Never overwrite; upload the new version as `{name}_EQ-v{NN}.{ext}` beside it; mark both rows `conflict`; notify the uploader's side ("Your team edited the working copy; Equator has a newer version") |
| Workspace copy deleted by a user | Change feed (`listChanges`, Graph delta **[VERIFY — open (vendor): delta query support under `Sites.Selected`]**) or `getItem` 404 | Record `deleted_in_workspace`; do not re-create unless the user asks ("Restore working copy") |
| Workspace copy edited and user wants Equator to have it | User action "File back to Equator" (P-3) | New draft or version per DMS rules; hash computed at ingest; original workspace item untouched |
| Equator document withdrawn, superseded or access revoked for that side | Domain event | Rename workspace copy with prefix `WITHDRAWN_` or `SUPERSEDED_` and set column; the copy is not deleted (the tenant is controller of its copy) unless the tenant set `delete_on_revocation = true` and Equator still holds `Sites.Selected` write |
| Name collision with a non-Equator file | `onConflict: 'fail'` → 409 | Append `_EQ` and retry once |
| Path over 400 characters (decoded) | Pre-flight check | Shorten per AC.13.7; never fail silently |

### AC.9.5 Disconnection and data return
- **Customer disconnects** (revokes consent in Entra/Google, or turns the flag OFF): Equator stops all pushes within 5 minutes of detecting a `401/403` or the flag change, marks the connection `revoked`, deletes stored refresh tokens, keeps `cfg.mirror_items` rows for audit (no content), and shows "Mirror disconnected on {date}; copies already in your library remain yours".
- **Tenant exit:** the `PLATFORM_TENANT_EXIT` or `CHAMBERS_TENANT` export (AC.13.3) is the data return; the mirror is not a substitute. The exit certificate lists whether a mirror existed and the last mirror time.
- **Erasure requests:** where a data principal's erasure request reaches Equator (Q §2.4) and a mirrored copy exists, Equator (a) erases its own data per retention rules, (b) notifies the tenant's DPO contact of the mirrored items to erase (DPDP s.8(7) — the tenant is a fiduciary for its copy), and (c) deletes the copy itself only if the tenant granted that instruction in the connection terms. The notification is logged (`xpt.erasure_propagations`).

### AC.9.6 Google Drive equivalent
Same patterns with shared drives, resumable upload and file `appProperties` for the column set; all endpoint details **[VERIFY — open (vendor)]** [RD F4.4]. Adapter `google_drive` OFF with the Google flag.

## AC.10 Chat notifications
Purpose: tell staff that something needs attention in Equator without moving case content into chat.
- **Teams:** a tenant admin configures an incoming notification endpoint for a channel (Teams Workflows webhook or an equivalent the tenant permits) and pastes the URL into SCR-P21-02; Equator posts `{text, deepLink}` only. Delegated posting (`ChannelMessage.Send`) is an alternative for a user's own messages **[VERIFY — open (vendor): current Teams webhook mechanism and Graph application posting restrictions]**.
- **Google Chat:** space webhook **[VERIFY — open (vendor)]**, behind the Google flag.
- **Content rule (Locked):** text from the template set `notify.chat.*` only; variables limited to item type, due time, deep link, and the case number for administering-tenant staff (IP-10). Lint `NOTIFICATION_CONTENT_MINIMISED`.
- In-app and push notifications (P07) remain the primary channel; chat is optional per user (`user.notifications.chat_enabled`, T).

## AC.11 Open integrations catalogue (NN-40)

The catalogue is data (`cfg.integration_catalogue`, seeded from this section) and is rendered on SCR-P21-05 for tenant admins. Each row states the port, what moves, the system of record, the fallback and the flag. Marketing workflow (campaign and social calendar, approvals, brand governance) is owned by Appendix Y and P17, which also own the `mkt.*` flag keys (Y X-55 aliases `growth.*` keys); this section specifies only the vendor-facing contract, SoR, mapping and catalogue entry, and Appendix Y governs where the two differ.

### AC.11.1 Catalogue summary

| Tool | Port / adapter | Objects moved | Direction | System of record | Fallback | Flag (default) |
|---|---|---|---|---|---|---|
| Microsoft 365 | `WORKSPACE_PORT` / `m365_graph`; `STORAGE_PORT` / `sharepoint_graph` | Accounts, licences, groups, calendar events, files (exports, mirror) | Equator → M365 (audit logs inbound) | HRMS for employment; Entra for credentials; Equator for records | `manual_it_desk`; download | `tenant.hr.workspace.jml_automation` (OFF until runbook done) |
| Google Workspace | `WORKSPACE_PORT` / `google_workspace`; `STORAGE_PORT` / `google_drive` | As above | As above | As above | As above | `ops.workspace.google.enabled` (OFF) |
| Brevo | `CRM_PORT` / `brevo` (built in P16, Appendix X §X.10.2); `MARKETING_PORT` / `brevo` (built in P17, Appendix Y) | Contacts, attributes, lists, companies, deals, tasks (one way), campaigns, marketing events | Two way for consent and engagement events; one way (Equator → Brevo) for contacts and deals | Equator CRM (`ops.crm_*`, X-51) and consent ledger (`core.consent_records`) | Native CRM + `ses_marketing` (Appendix Y); campaign export CSV | Connector flag for both ports `mkt.brevo.enabled` (OFF until DPA; owned here, AC.17); CRM-object sync additionally `tenant.ops.connectors.brevo_crm_sync.enabled` (Appendix X; OFF; cannot be ON while `mkt.brevo.enabled` is OFF) |
| Adobe Express | `adobe_express_handoff` (no API) | Design brief out; asset file and design link back | Manual hand-off | Equator DAM for approved assets; calendar for plan and approvals | Any design tool; upload | `mkt.adobe_embed.enabled` (OFF; Adobe review needed) |
| LinkedIn, Meta (Facebook, Instagram), X, YouTube | `SOCIAL_PORT` / `linkedin_cm`, `meta_graph`, `x_v2`, `youtube_data`, `manual_handoff` | Approved posts out; post URL and metrics back | Out (publish) and in (metrics) | Equator calendar for plan, copy and approvals; platform for published post and metrics | `manual_handoff` (default) | Each adapter OFF until its app review/access tier is granted |
| Tally (accounting) | `ACCOUNTING_PORT` / `tally_file` (file adapter) | Sales invoices, receipts, credit notes, payroll journals, inter-company charges | Equator → Tally (file) | General ledger in Tally or Zoho Books per entity (D3-30); Equator sub-ledgers export to it | CSV/XLSX journal | `tenant.fin.accounting_export.tally` (T, OFF) |
| Zoho Books | `ACCOUNTING_PORT` / `zoho_books` | As Tally | Equator → Zoho Books (API) | As Tally | CSV/XLSX | `tenant.fin.accounting_export.zoho_books` (OFF until spike) |
| Payroll tools | `PAYROLL_EXCHANGE_PORT` / `generic_csv` | Employee master, attendance and leave summaries, pay register, bank-advice summary (import or export) | Both, file-based | Equator payroll (D3-03) unless the entity declares an external payroll SoR | Equator payroll | `tenant.pay.external_payroll.enabled` (G, OFF) |
| HubSpot, Zoho CRM | `CRM_PORT` / `hubspot`, `zoho` (Appendix D §D.9; moved to the Operations Platform, Appendix X §X.10) | Contacts, companies, deals | Sync | Equator CRM (`ops.crm_*`, X-51) | Native CRM | `tenant.ops.connectors.hubspot.enabled` / `.zoho.enabled` (G, OFF; Appendix X §X.13) |
| Calendars (any) | ICS attachments; `WORKSPACE_PORT.createMeeting` (opt-in) | Session times | Equator → calendar | Equator session schedule | ICS | Always ICS; connector opt-in |
| E-sign | `ESIGN_PORT` (Appendix D §D.3.1: Leegality, Setu, Digio; optional `lawdocs_esign`) | Envelopes, signed PDFs, audit trails | Both | Equator evidence store for signed bytes | Next ESP (reinitiate) | Existing |
| Storage (export destinations) | `STORAGE_PORT` / `sharepoint_graph`, `onedrive_graph`, `google_drive`, `sftp_generic`, `s3_compatible` | Export packages | Equator → destination | Equator for the record; destination holds a copy | Download link | `tenant.xpt.push_destinations` (T) |

### AC.11.2 Brevo (CRM sync and marketing execution)
- **Objects and endpoints** [RD F3.1, RD 21–28]: contacts, attributes, lists and segments (`/v3/contacts/…`); bulk `POST /v3/contacts/import` and asynchronous `POST /v3/contacts/export` (**[VERIFY — open (vendor)]** field limits); email, SMS and WhatsApp campaigns (OAuth scopes `campaigns.email`, `campaigns.sms`, `campaigns.whatsapp`); transactional `POST /v3/smtp/email`; CRM companies, deals, tasks and notes under scope `crm`; `POST /v3/crm/deals` with `name`, `attributes` (`deal_owner`, `pipeline`, `deal_stage`), `linkedContactsIds[]`, `linkedCompaniesIds[]`, returning `201 {id}`.
- **Mapping** (seed of `cfg.field_mappings`, connector `brevo`; the object-level mapping is canonical in Appendix X §X.10.2 and governs where it differs): `ops.crm_contacts` (marketing-eligible only) → contacts (attributes such as `EQ_ID`, `PERSONA`, `LANGUAGE`, `COMPANY_CODE`, `SEGMENT_CODES`, consent flags per purpose and per group company [RB-23]); `ops.crm_segments` → the `SEGMENT_CODES` attribute only (send lists are pushed only by `MARKETING_PORT` from `mkt.audience_snapshots`, Appendix Y); `ops.crm_accounts` → companies; `ops.crm_opportunities` → deals (pipeline and stage IDs stored in the provider config); tasks one way Equator → Brevo [RD DI-B8]. RD's `growth.leads`/`growth.accounts`/`growth.opportunities` mapping is superseded by X-51 (`growth.leads` remains only the web capture inbox).
- **Rate budget:** AC.5 — one account-level budget `tenant.mkt.brevo.max_requests_per_hour` shared by the `CRM_PORT` and `MARKETING_PORT` adapters on the same Brevo account (both draw on the same 100 requests/hour catch-all [RD 21]); bulk import above 50 records; incremental queue every 5 minutes (`CrmSyncWorkflow`, Appendix D §D.9, moved to the EOP CRM by X-51).
- **Webhooks:** `POST /v3/webhooks` with `type ∈ {transactional, marketing, inbound}`; events listed in RD F3.1. Equator exposes one ingress for both ports, `POST /webhooks/brevo` (Appendix X §X.16); engagement events are forwarded to `mkt.touchpoints` via `equator.ops.connector.engagement_received.v1`. **Brevo documents no HMAC signature** (options: IP allow-list, Basic auth in URL, bearer token, custom headers) [RD 23]. **Compensating controls (Locked):** (1) per-subscription bearer token, rotated ≤ 90 days; (2) source IP allow-list from Brevo's published ranges; (3) `webhook_inbox` dedupe as Appendix D §D.0.3; (4) **re-fetch state from the Brevo API before acting** on any consent-changing event (`unsubscribed`, `contactDeleted`, `spam`), so a forged call cannot change consent; (5) unsubscribe in Brevo creates a consent withdrawal in Equator within 15 minutes and vice versa (D.9 rule) [RD DI-B10]; collector `marketing_consent_sync` (daily) must show zero diffs older than 15 minutes.
- **Residency and DPDP:** Brevo hosts in the EU [RD 26]; transfer-register row `BREVO_EU` with mechanism `dpdp_s16_not_restricted` (cross-border transfer permitted unless the destination is restricted by notification) and the DPA on file before activation [RD F3.1].
- **Scope limits (Locked):** CRM and marketing data only; never case notices, OTPs or respondents without separate marketing consent (NN-16 suppression check); **India SMS and WhatsApp marketing stays on DLT-registered `MESSAGING_PORT` providers** until Brevo confirms DLT template support in writing (flag `mkt.brevo.sms_whatsapp.enabled` OFF) [RD F3.1].
- **Exit:** nightly API export of contacts and deals to a snapshot in the business database (the `ops`/`mkt` plane, X-50, X-53; 13 months) [RD DI-E]; migration rehearsal = full contact and deal export, re-import into the native CRM (`ops`), reconciliation counts by list and stage (`CrmMigrationWorkflow`, Appendix X §X.10.3).

### AC.11.3 Adobe Express (asset hand-off)
There is **no public API to create, schedule or publish posts through Adobe Express Content Scheduler**; the Embed SDK embeds the editor and returns projects to the host app but offers no scheduling or publishing, and production use needs Adobe Developer Console registration and Adobe review [RD F3.2, RD 29–30]. Integration pattern [RD DI-B13]:
1. The Social Calendar item (P17) holds the brief, copy, approvals and target channels.
2. The designer works in Adobe Express — natively (pastes the share link; uploads the exported file to the Equator DAM, which hashes it with SHA-256) or, where `mkt.adobe_embed.enabled` is ON, through the Embed SDK inside the Operations Platform.
3. Publishing: (a) manual in Adobe's Content Scheduler, with the operator recording scheduled time and post URL back on the item (`published_via = adobe_scheduler`, operator-confirmed), or (b) Equator's `SOCIAL_PORT` adapter where API access is approved, or (c) the platform's native app.
4. Maker-checker approval of copy and asset (legal claims; Bar Council advertising limits for neutrals and advocates; NN-17 claims register; no case data) happens in Equator before an item is "ready to schedule".

### AC.11.4 Social platforms (`SOCIAL_PORT`)

| Adapter | Capability | Gate | Limits Equator enforces | Source |
|---|---|---|---|---|
| `linkedin_cm` | Organisation posts, comments, page and follower analytics (Community Management API) | Vetted product: development tier, then Standard tier after a screencast per use case; new developer app with no other API product | Versioned API; adapter pins the version and alerts 90 days before sunset | [RD 32] |
| `meta_graph` (Instagram, Facebook Pages) | Instagram images (JPEG), videos, Reels, carousels (≤ 20), Stories; media at a public URL at publish time | Advanced/Standard access with `instagram_business_content_publish` or `instagram_content_publish`; Facebook `pages_manage_posts` with App Review **[VERIFY — open]** | Counter per account per 24 h, default **50** (the page states both 100 and 50) | [RD 31] |
| `x_v2` | `POST /2/tweets` | Pay-per-use credits | Monthly credit budget (T); post with URL costs more (USD 0.200 vs 0.015) | [RD 34] |
| `youtube_data` | `videos.insert` | OAuth `youtube.upload` | 100 uploads per day ceiling; ≤ 256 GB | [RD 33] |
| `manual_handoff` | Operator publishes in the native app and records URL and time | None | — | Default |

Analytics are pulled daily into schema `mkt` in the business database plane only (Appendix Y; X-53; NN-16). Every outbound post passes maker-checker; Equator never auto-publishes AI-generated copy without human approval [RD DI-B14].

### AC.11.5 Accounting (Tally, Zoho Books)
- **One general ledger per legal entity.** D3-30 (Appendix Z) places the general ledger in Tally or Zoho Books; Equator's billing, escrow and payroll ledgers are **sub-ledgers** whose postings and edit logs are exported to it. The tool is declared in `cfg.system_of_record` (`data_category = 'general_ledger'`) and in `grp.legal_entities.books_sor`; an entity may instead keep its books on Equator only by a recorded CS decision. The Companies (Accounts) Rules 2014 r.3(1) proviso requires accounting software that records an audit trail of every transaction with an edit log that cannot be disabled [RD F7.3, RD 52]; Equator's sub-ledgers meet this by append-only tables, master-data history and `pgaudit` (NN-36; RD DI-F); the external tool must meet it on its own (the CS records the vendor's confirmation).
- **Exports:** sales invoices (with GSTIN, place of supply, CGST/SGST/IGST per line, IRN and acknowledgement number where e-invoiced), receipts, refunds and credit notes, payout and TDS records, payroll journals (P18), inter-company charges (AD §AD.9). Formats: XLSX + CSV voucher journals with a ledger-mapping table (`cfg.ledger_maps`: Equator account code → tool ledger name, cost centre, legal entity) and, for Tally, the tool's import format **[VERIFY — open (vendor): Tally import schema and version]**; for Zoho Books, the API **[VERIFY — open (vendor)]**.
- **Controls:** exports are generated only from **closed** periods or posted documents; every export file is hashed and listed in `xpt.export_items`; re-export of the same period produces the same hash or a variance report; a period re-opened in Equator after export raises `XPT_ACCOUNTING_PERIOD_REEXPORT_REQUIRED` (409) on the next run.

### AC.11.6 Payroll tools
D3-03 builds payroll inside Equator with exports to and from specialist tools. The exchange is file-based by default: employee master (no bank account numbers in plain text — masked except in the bank-advice file, which is encrypted and maker-checker released per NN-36), attendance and leave summaries per period, pay register, statutory-dues summary, journals. Candidate adapters (greytHR, Keka, Zoho Payroll, RazorpayX Payroll) are **candidates only; no API facts were verified** **[VERIFY — open (vendor)]**. An entity that keeps payroll in an external tool declares it as SoR for `payroll_run`; Equator then imports the pay register for HR self-service and records, never recalculates it.

### AC.11.7 Calendars and e-sign
See AC.8.2 (ICS always; workspace calendar opt-in) and Appendix D §D.3.1 (ESIGN_PORT). E-sign evidence exported per AC.13.8.

### AC.11.8 Storage destinations (`STORAGE_PORT`)

```ts
export interface StoragePort {
  ensureFolder(d: { connectionId: string; destRef: string; path: string }): Promise<{ folderRef: string }>;
  putObject(o: { connectionId: string; destRef: string; path: string; bytes: number; sha256: string; stream: NodeJS.ReadableStream;
                 resumable: boolean; metadata: Record<string,string> }): Promise<{ ref: string; url?: string }>;
  headObject(connectionId: string, destRef: string, path: string): Promise<{ bytes: number; sha256?: string; eTag?: string } | null>;
  getObject(connectionId: string, destRef: string, path: string): Promise<NodeJS.ReadableStream>;   // for post-push sample re-hash
}
```
Adapters: `sharepoint_graph`, `onedrive_graph` (upload session for files > 250 MB; fragment size a multiple of 320 KiB **[VERIFY — open (vendor)]**), `google_drive` (OFF), `sftp_generic` (key-based, host-key pinned), `s3_compatible` (customer bucket; customer-supplied role or access key in Secrets Manager). Failover `none`.

## AC.12 System-of-record register, field-mapping registry and connector health

### AC.12.1 System-of-record register (seed of `cfg.system_of_record`; rows are tier G — a change needs an ADR and DPO approval; consent can never have an external SoR)

| Data category | System of record | Mirrors / consumers | Conflict rule |
|---|---|---|---|
| Case record, parties, proceedings, orders, outcomes | Equator `core` + vertical schemas | Exports; party's own systems via enterprise API/webhooks (AD X-64) | Equator wins; mirrors never write back |
| Evidence and signed instruments (bytes) | Equator evidence bucket (Object Lock) + `core.evidence_ledger` | Export packages; SharePoint working copies | Hash mismatch = Critical incident (`HASH_MISMATCH_CRITICAL`) |
| Hearing and session schedule | Equator `core.sessions` | ICS; workspace calendars | Equator wins; calendar edits ignored and flagged |
| Workforce person and employment | Equator HRMS (`hr`, P18) | Entra/Google directory, payroll tools | HRMS wins; directory drift reconciled nightly |
| Workforce credentials and sign-in | Entra ID / Google (mail, files); Keycloak (Equator consoles) | — | Each authoritative for its own sessions |
| Workforce mail and chat content | Microsoft 365 / Google | Case-relevant items filed into Equator (`COR`) | Filed copy is the case record |
| Leads, contacts, accounts, opportunities, activities | Equator CRM in the Operations Platform (`ops.crm_*`, P16; X-51 — `growth.leads` is only the web capture inbox, promoted to `ops.crm_leads` within 60 s); Appendix X §X.10.1 refines this row | Brevo, HubSpot, Zoho | Equator wins except engagement events |
| Marketing consent and suppression | Equator consent ledger (`core.consent_records`; mirrored once in `ops.crm_comm_prefs`); respondent hashes `growth.suppression_hashes` (P13); channel suppressions `mkt.suppressions` (Appendix Y) | Brevo, HubSpot, Zoho | **Most restrictive wins**: a withdrawal anywhere applies everywhere within 15 min; opt-ins are never accepted from an external tool without the consent artefact |
| Campaign plan, copy, approvals | Equator marketing calendar (`mkt`, P17) | Brevo campaigns | Equator wins; Brevo-side edits after approval raise a variance |
| Campaign send results, opens, clicks | Brevo (raw events) | `mkt.touchpoints` (normalised); reported figures frozen in `mkt.metric_snapshots` (Appendix Y D3-25) | Raw-event disputes → Brevo; the reported figure is the Equator snapshot |
| Social post plan, copy, approvals | Equator calendar (`mkt`) | Platforms | Equator wins |
| Published post and platform metrics | Platform | `mkt.metric_snapshots` (business database plane, X-53) | Platform wins; the reported figure is the Equator snapshot |
| Segments and send audiences | Equator `ops.crm_segments` (CRM) / `mkt.audiences` with `mkt.audience_snapshots` (marketing) | Brevo static lists (pushed only by `MARKETING_PORT`) | Equator wins |
| Design source files | Adobe Express (or other tool) | Equator DAM (approved exports) | DAM holds the approved, hashed asset |
| General ledger (books of account) | Tally or Zoho Books per entity (D3-30), unless the CS records books on Equator | Equator sub-ledgers export postings and edit logs | Declared SoR wins; dual-entry forbidden |
| Payroll run | Equator payroll (default) or declared external tool | Accounting tool (journals) | Declared SoR wins |
| Statutory filing acknowledgements | Government portals | Equator (uploaded acknowledgement, hashed) | Portal wins |
| Professional registry (advocates, CAs, CSs, CMAs) | `dir` (group shared service, D3-05) | Consuming tenants under GDSA | `dir` wins; consumers apply update/withdraw events (AD §AD.8) |
| Group agreements, grants, secondments | `grp` (Appendix AD) | HRMS, finance | `grp` wins |

### AC.12.2 Field-mapping registry
`cfg.field_mappings` (AC.15) holds one row per `(connector, object, direction, source_field, target_field, version)` with transform (`copy`, `map_enum`, `concat`, `split`, `format_date`, `hash`, `mask`, `constant`, `lookup`), PII class, required flag, null policy, validation regex and an example. Mappings are published as **mapping sets** (`cfg.mapping_sets`) with status `draft → in_review → approved → retired`; a mapping set touching identity, consent or money fields is tier **G** (maker-checker, `compliance_officer` checker); other mapping sets are tier **T** (tenant admin, audit and rollback). The connector always runs against a pinned approved mapping-set version (NN-21 pattern). A **dry run** shows, for 20 sample records, source values, target values and validation outcomes before approval (SCR-P21-06).

### AC.12.3 Connector health monitoring
`ConnectorHealthProbeJob` (every 5 minutes per active connection) computes:

| Signal | Green | Amber | Red |
|---|---|---|---|
| Auth (token/cert valid, consent present) | valid, > 30 days to expiry | ≤ 30 days to expiry | invalid / revoked |
| Error rate (rolling 1 h) | < 2% | 2–10% | > 10% or circuit open |
| Sync lag (oldest unsent outbox item) | < 15 min | 15–60 min | > 60 min (consent sync: > 15 min is red) |
| Throttle events (rolling 1 h) | 0–5 | 6–50 | > 50 |
| Reconciliation drift (nightly) | 0 | ≤ 0.5% of records | > 0.5% or any consent drift |
| Migration rehearsal age | ≤ 365 days | 366–400 | > 400 (IP-04 floor) |
| Credential age | ≤ 60 days | 61–90 | > 90 |

State changes emit `equator.cfg.connector.health_changed.v1`; red pages the integration on-call and the tenant's `it_admin`; SCR-P21-04 shows per-connector tiles with the last 30 days.

## AC.13 Data portability and export packages (`EQ-EXPORT-1.0`; NN-37, D3-07, D3-41)

### AC.13.1 Guarantees
1. **Any time, by the data owner.** Every organisation, user, party, neutral, employee and group company can export the data it is entitled to at any time through `POST /v1/exports`. Exports for a person's own data (`USER_SELF`, `DSR_PORTABILITY`, `EMPLOYEE_SELF`, `NEUTRAL_PRACTICE`, `MARKETPLACE_PROVIDER`) and every exit export are **free**; periodic bulk exports for enterprise or chambers tenants beyond the plan's included runs may be priced in the revenue-stream registry (D3-08), but **billing state never blocks an export needed to exit or to protect legal rights** (Appendix O billing-never-blocks list, item (i)).
2. **Self-explanatory.** A recipient with no Equator account can understand the package from its folder names, `00_README.pdf` and `00_Contents.xlsx` alone.
3. **Opens in Microsoft Office.** Every DOCX, XLSX and PPTX opens in Word, Excel and PowerPoint for the web (the only Office apps on Business Basic [RD 4]) and desktop; every PDF opens in any PDF reader; AC.13.13 tests this.
4. **Verifiable.** Checksums for every file; signed originals are byte-identical to the evidence store; the audit-trail extract can be verified offline.
5. **Lawful.** The package contains only what the requester is entitled to see; AC.13.11 lists what is never exported and AC.13.12 the redaction rules.
6. **Competitive basis.** Jupitice describes no export function and its terms place data-loss risk on the user [RA F7]; Equator's "export everything, any time" is a published commitment (EQM-17) and a website claim only once this appendix passes its tests (NN-17 claims register).

### AC.13.2 Two layouts, one taxonomy (D3-41)

| Layout | Default for | Structure | Verification |
|---|---|---|---|
| **Standard folder package** | `USER_SELF`, `PARTY_IN_CASE`, `EMPLOYEE_SELF`, `NEUTRAL_PRACTICE`, `MARKETPLACE_PROVIDER`, `DSR_PORTABILITY`, `OPS_DEPARTMENT`, `CASE_FULL` for court use | Root folder `Equator_Export_<Org>_<YYYY-MM-DD>/` containing `00_README.pdf`, `00_README.html`, `00_Contents.xlsx`, the numbered taxonomy folders and `99_Manifest/` | `99_Manifest/checksums-sha256.txt` (BagIt manifest-line syntax), `manifest.csv`, `manifest.json`; `99_Manifest/Tools/verify_package.py` |
| **Archival bag** (RFC 8493 BagIt 1.0) | `CHAMBERS_TENANT`, `ENTERPRISE_TENANT`, `GROUP_COMPANY`, `PLATFORM_TENANT_EXIT`, `STATUTORY_BOOKS`, `ASSURANCE_PACK`, `PAYROLL_FY` | Bag root `Equator_Export_<Org>_<YYYY-MM-DD>/` with `bagit.txt`, `bag-info.txt`, `manifest-sha512.txt`, `manifest-sha256.txt`, `tagmanifest-sha512.txt`, `00_README.pdf` (tag file), `99_Manifest/` (tag directory) and `data/` holding the taxonomy folders | BagIt "valid" (all checksums match; every payload file listed exactly once; SHA-512 default; SHA-256 also provided because evidence-ledger hashes are SHA-256) [RD 35] **[VERIFY — open (spec): confirm RFC 8493 permits additional tag files and a tag directory at the base; if not, `00_README.pdf` and `99_Manifest/` move under `data/`]** |

Either layout may be requested for any scope (`layout` parameter). The taxonomy, names, formats and manifest fields are identical; only the BagIt wrapper differs.

### AC.13.3 Export scopes

| Scope code | Who may request | Contents (top-level folders) | Approval | Step-up | Target time to ready |
|---|---|---|---|---|---|
| `USER_SELF` | Any signed-in user | 01 (own profile), 02 (own roles and memberships), 03 (cases where the user is a party/representative — party view), 04 (own invoices and receipts), 09 (own settings, consents, notification preferences) | None | aal2 ≤ 10 min (Appendix S) | ≤ 24 h |
| `DSR_PORTABILITY` | Data principal via rights centre (Q §2.4) | As `USER_SELF` with JSON first (PC-39) | DPO queue for identity verification | aal2 | Within Q §2.4 clock (DPDP/GDPR/CCPA) |
| `PARTY_IN_CASE` | Party, `party_org_user` with `auth`, representative with `export_case_file` scope | 03 for the named case(s), party view | None (representative: party notified) | aal2 | ≤ 24 h |
| `CASE_FULL` | `registrar` of the administering tenant; `chambers_owner` for its own administered matters | 03 with registry view (still excluding AC.13.11 items) | Maker-checker (registrar + `case_counsel` or `deputy_registrar`) | aal2-pr | ≤ 24 h |
| `NEUTRAL_PRACTICE` | Neutral | 01 (profile, credentials, disclosures history), 03 (orders and awards the neutral issued — neutral view; never caucus notes of others; own caucus notes only while retained and only to the author), 04 (fee notes, payouts, TDS certificates), 08 (own feedback aggregates at n ≥ 5, X-28) | None | aal2 | ≤ 48 h |
| `MARKETPLACE_PROVIDER` | `mkp_provider_owner` (Appendix AA §AA.16) | 01 (profile; credential verification records, not third-party evidence images), 04 (invoices, statements, TCS/TDS), 05 (engagements, proposals and terms, complaints and decisions), 08 (reviews with replies) — Appendix AA §AA.21 | None (own data) | aal2 | ≤ 7 days (at exit within 7 days) |
| `CHAMBERS_TENANT` | `chambers_owner` | 01–04, 05 (practice operations), 07 (restricted, practice HR-lite), 08, 09 | Maker-checker (`chambers_owner` + `chambers_admin`, or Equator `support_lead` checker for a sole practitioner) | aal2-pr | ≤ 7 days |
| `ENTERPRISE_TENANT` | `enterprise_admin` (Appendix S) | 01–04, 08 (MIS), 09; 05 for GRM desks (tickets) | Maker-checker within the tenant | aal2-pr | ≤ 7 days |
| `OPS_DEPARTMENT` | `department_head` of an Operations Platform department (P16) | 05 and/or 06 for the department and legal entity; 08 department reports | `ops_director` checker | aal2-pr | ≤ 48 h |
| `EMPLOYEE_SELF` | `employee` | 02 (own role history), 07 (own employment file, payslips, Form 16-equivalent, leave, attendance, appraisals), own consents | None | aal2 | ≤ 48 h |
| `EMPLOYEE_FILE` | `hr_manager` (employing entity only) | 07 for one employee | `hr_manager` + `group_hr` or second HR checker | aal2-pr | ≤ 48 h |
| `PAYROLL_FY` | `payroll_checker` | 07 payroll registers for a financial year | Maker-checker (NN-36: sensitive export) | aal2-pr | ≤ 7 days |
| `GROUP_COMPANY` | `entity_admin` of that legal entity | All folders for that entity's partition only (Appendix AD §AD.12); never another entity's partition; never Equator case data for a non-Equator entity | `entity_admin` + `group_admin` checker | aal2-pr | ≤ 14 days |
| `PLATFORM_TENANT_EXIT` | Tenant owner on cancellation, or Equator on termination | Everything the tenant is entitled to | Maker-checker; exit certificate | aal2-pr | ≤ 7 days; available for 90 days after cancellation (Appendix O) |
| `STATUTORY_BOOKS` | `finance_ops` / `accounts_checker` | 04 and 07 ledgers, registers and audit trails for an FY (RD F7.3); ledger audit-trail reports in `08_Reports/08_Audit_Trail_Reports/` (Appendix AE §AE.8.4) | Maker-checker; checker is the CS (`compliance_officer`), never the requester (Appendix AE §AE.8.4) | aal2-pr | ≤ 7 days |
| `ASSURANCE_PACK` | `compliance_officer` for a client or auditor request | 08 assurance evidence in the Appendix AE §AE.8.4 subfolders (controls, change management, vulnerability and VAPT, backup and DR, access reviews, incidents, policies, findings), NDA watermark on renditions | `compliance_officer` (maker) + `security_lead` (checker) (Appendix AE §AE.8.4) | aal2-pr | ≤ 7 days |

Every run writes `xpt.export_runs` (AC.15) and `audit.append_event`; every download writes `audit.access_log` (`action = export`). Maker-checker for sensitive scopes (`EMPLOYEE_FILE`, `PAYROLL_FY`, `STATUTORY_BOOKS`, `GROUP_COMPANY`, `PLATFORM_TENANT_EXIT`, and any scope containing HR, payroll or bulk personal data) is executed through the `ctl` approval engine with action `EXPORT-SENSITIVE` (Appendix Z §Z.12, X-56; NN-36).

**Scope-name aliases (accepted by `POST /v1/exports` for v3.0; this table is canonical).** RD DI-C 21 and sibling appendices use earlier names: `CASE` → `PARTY_IN_CASE` (or `CASE_FULL` for the administering registry); `PARTY_DSR` → `DSR_PORTABILITY`; `TENANT_EXIT` → `PLATFORM_TENANT_EXIT`; `CHAMBERS_PRACTICE` (Appendix W §W.15.3) → `CHAMBERS_TENANT`; `OPS_CRM` (Appendix X) → `OPS_DEPARTMENT` for a department or `ENTERPRISE_TENANT`/`GROUP_COMPANY` for a whole company. `POST /v1/ops/exports` (Appendix X) is an alias of `POST /v1/exports`.

**Pre-flight estimate and presets *(v3.1)*.** Before submitting, the request screen calls `POST /v1/exports:estimate` (same body as `POST /v1/exports`, no side effects) and shows: item counts and estimated size per top-level folder; number of parts at the current `tenant.xpt.part_max_gb`; estimated time to ready (from the trailing 30-day p50 build rate for that scope); counts of excluded items by reason code (AC.13.11) without content; whether approval and step-up are needed and who the checker will be; and the destination (download or a `STORAGE_PORT` push). A user may save the scope, layout, redaction profile and destination as a named **preset** (`xpt.export_presets`, per user, ≤ 10) and, where the plan includes periodic exports, schedule it (`tenant.xpt.schedules`, T; monthly or quarterly; sensitive scopes still pass maker-checker on every run). Estimates are labelled "estimate"; they never block a request.

### AC.13.4 Standard folder taxonomy (top level)

```
Equator_Export_<Org>_<YYYY-MM-DD>/
  00_README.pdf                    PDF/A-2b, English + Hindi (+ tenant language): what this is, who requested it, scope, date (IST),
                                   folder guide, how to verify, what was excluded and why, legal notices, contact
  00_README.html                   Same content, for screen readers and browsers
  00_Contents.xlsx                 One row per file: folder, file name, title (native script allowed), record type, date, case no,
                                   format, signed original?, SHA-256 (also in 99_Manifest)
  01_Organisation_Profile/         Organisation or person profile, KYB summary (masked identifiers), brands, addresses, signatories
  02_People_and_Roles/             Users, memberships, roles, delegations, representative authorities (LoA/Vakalatnama), staff lists
  03_Cases/                        One folder per case (AC.13.5)
  04_Billing_and_Subscriptions/    Plans, subscriptions, quotes, invoices (PDF/A + XLSX register), receipts, refunds, credit notes, payouts, TDS/TCS records
  05_Operations/                   CRM accounts and activities, onboarding projects, tickets, grievances, knowledge-base articles, SLAs (Operations Platform, P16)
  06_Marketing/                    Campaign plans, social calendar, approved assets (originals), consent and suppression lists (hashed where required), PR log
  07_HR_and_Payroll/               RESTRICTED — employment files, attendance, leave, payslips, payroll registers, appraisals (P18); present only in HR scopes
  08_Reports/                      Dashboards and MIS as XLSX + PDF/A; regulatory MIS; assurance evidence
  09_Settings_and_Configuration/   Settings with tier (L/G/T), rule-pack versions pinned, templates, mapping sets, provider routing (secrets never)
  99_Manifest/                     manifest.csv, manifest.json, checksums-sha256.txt, bag-info.txt (labels), export_certificate.pdf,
                                   schemas/ (JSON Schema per entity), Tools/ (verify_package.py, verify_audit.py, public keys, README_TOOLS.txt)
```

Rules: (1) a folder is omitted when the scope has nothing for it, and `00_README.pdf` lists omitted folders with the reason; (2) folder labels are configurable per tenant language within the locked `NN_Title_Case_English` code (the two-digit prefix and ASCII form never change; a tenant may add a native-language caption in the README only); (3) `07_HR_and_Payroll/` appears only in `EMPLOYEE_SELF`, `EMPLOYEE_FILE`, `PAYROLL_FY`, `CHAMBERS_TENANT` (practice HR-lite), `GROUP_COMPANY` and `PLATFORM_TENANT_EXIT` (where the tenant ran HR on Equator), and its PDFs carry a "Restricted — HR" header on renditions; (4) structured data for each folder sits in a `_Data/` subfolder as CSV (RFC 4180, UTF-8 with BOM) and JSON (with JSON Schema in `99_Manifest/schemas/`) [RD F4.1].

### AC.13.5 Case folder taxonomy and mapping from the DMS

```
03_Cases/<CaseNo>_<ShortTitle>/
  00_Case_Summary.pdf              Case number, parties (roles; names per redaction profile), mechanism, vertical, pinned rule versions, key dates, status
  00_Case_Index.xlsx               Index of every file in this case folder
  01_Intake/
  02_Notices_and_Service/
  03_Submissions/
  04_Evidence_and_Annexures/
  05_Orders_and_Directions/
  06_Hearings_and_Meetings/
  07_Settlement_or_Award/
  08_Billing_and_Receipts/
  09_Correspondence/
  10_Audit_Trail/
```

| Export folder | Source (Appendix L §1.2 folder or module) | Contents and rules |
|---|---|---|
| `01_Intake` | Intake forms, filing receipt, scrutiny outcome visible to the side, Dispute Explorer summary (own), registration notice, routing and signposting record (NN-20) | Filed forms as PDF/A + JSON answers; never other sides' intake answers |
| `02_Notices_and_Service` | `NTC` | Notices, service certificates, postal proofs, delivery receipts (`core.communications` summary as XLSX) |
| `03_Submissions` | `PLD`; own `DRF` (only in the owning side's export, subfolder `My_Drafts_Not_Filed/`) | Pleadings, responses, counterclaims, applications; type copies and translations next to originals with labels (NN-32) |
| `04_Evidence_and_Annexures` | `ANX`, `EVD`, `BND` (subfolder `Bundles/`) | Originals first, then type copies `(T)` and translations (Appendix L §6.8); bundles with `manifest.json` and s.63(4) certificate |
| `05_Orders_and_Directions` | `ORD` | Procedural orders, directions, institutional orders; signed originals + renditions |
| `06_Hearings_and_Meetings` | `core.sessions`, attendance registers, arbitration recordings and transcripts **only where lawfully made** (FR-P04-41) | Session list (XLSX), attendance registers (signed PDF), recordings (MP4/M4A original) and transcripts (DOCX + VTT) for arbitration only; mediation sessions show attendance only (no content exists) |
| `07_Settlement_or_Award` | `OUT`, eSign and eStamp artefacts, registration and execution packs (Appendix R) | `…_signed.pdf` (byte-exact), `…_rendition.pdf`, ESP audit trail, eStamp certificate, certified copies, execution pack |
| `08_Billing_and_Receipts` | `billing`, `payments`, `escrow` for this case and this side | Quotes, invoices, receipts, refunds, escrow milestone statements |
| `09_Correspondence` | `COR` | Correspondence in the side's audience; emails as PDF/A + original `.eml` where filed |
| `10_Audit_Trail` | `audit.audit_events` extract, `core.evidence_ledger` extract, anchors, `audit.access_log` summary, s.63(4) certificates | `audit_trail.csv` + `.json` (`seq`, `row_hash`, `prev_hash`, actor role, action, time IST), `evidence_ledger.csv`, `anchors/*.json` (KMS-signed), `Access_History.xlsx` (own side by name, other sides by role and count — Appendix L §2.7) |

Sub-folders inside a numbered folder are named `<YYYY-MM-DD>_<Title>` (e.g. `06_Hearings_and_Meetings/2027-03-04_Session-03/`), maximum one further level. Multi-volume or large cases split by sub-folder, never by breaking the numbered structure; a single folder never exceeds 5,000 files (well under the 50,000 sub-item share limit [RD 10]) — beyond that, `Part-01`, `Part-02` sub-folders are created.

### AC.13.6 Other subtrees (minimum contents)

| Folder | Minimum contents |
|---|---|
| `01_Organisation_Profile` | `Organisation_Profile.docx` + `.pdf`; `Legal_Entity_Details.xlsx` (CIN, GSTIN, PAN masked `ABCDE****F`, registered office); `Brands/` (logos as original files); `Signatories.xlsx` (authority limits) |
| `02_People_and_Roles` | `Users_and_Roles.xlsx`; `Delegations.xlsx`; `Representative_Authorities/` (LoA/Vakalatnama signed originals + renditions); `Access_Reviews.xlsx` (tenant scopes) |
| `04_Billing_and_Subscriptions` | `Invoices/` (PDF/A per invoice; e-invoice IRN and QR as issued), `Invoice_Register.xlsx`, `Receipts_and_Refunds.xlsx`, `Subscriptions.xlsx`, `Payouts_and_TDS.xlsx`, `Ledger_Audit_Trail.csv` (edit log, NN-36) |
| `05_Operations` | `CRM_Accounts.xlsx`, `CRM_Contacts.xlsx`, `CRM_Leads.xlsx`, `CRM_Opportunities.xlsx`, `CRM_Activities.xlsx`, `Onboarding_Projects/`, `Tickets.xlsx` + `Tickets/` (threads as PDF/A), `Grievances.xlsx` + `Grievances/` (records as PDF/A), `Knowledge_Base/` (DOCX), `SLA_Report.xlsx` (Appendix X §X.10.5 list) |
| `06_Marketing` | `Campaign_Calendar.xlsx`, `Social_Calendar.xlsx`, `Approved_Assets/` (originals with SHA-256), `Claims_Register.xlsx` (NN-17), `Consent_and_Suppression.csv` (hashed identifiers where the export leaves the tenant), `PR_Log.xlsx` |
| `07_HR_and_Payroll` | `Employment_File/` (appointment letter, secondment letters — Appendix AD), `Attendance_and_Leave.xlsx`, `Payslips/<FY>/` (PDF/A), `Payroll_Register_<FY>.xlsx`, `Statutory_Dues.xlsx`, `Appraisals/` (DOCX + PDF/A), `Payroll_Audit_Trail.csv` [RC E-30] |
| `08_Reports` | Each dashboard as `<Report>_<YYYY-MM>.xlsx` + `.pdf`; regulatory MIS; assurance evidence |
| `09_Settings_and_Configuration` | `Settings.xlsx` (key, value, tier, last changed, by role, approval ref), `Rule_Packs.xlsx` (pinned versions, effective dates, citations), `Templates/` (DOCX), `Mapping_Sets.json`, `Provider_Routing.xlsx` (no secrets) |

### AC.13.7 Naming rules and path limits

| Rule | Value | Basis |
|---|---|---|
| Root folder | `Equator_Export_<OrgSlug>_<YYYY-MM-DD>[_pNN]`; **≤ 40 characters** including the part suffix; the scope is stated in `00_README.pdf`, `bag-info.txt` (`EQ-Scope`) and the manifest, not in the name. The ZIP file carries the same base name (`<root>.zip`) and contains exactly one top-level entry, the root folder **[VERIFY — open (spec): RFC 8493 §4 serialisation rules for bags; not covered by RD F4.1]** | AC.13.2; RD F4.1 |
| `OrgSlug` | ASCII transliteration of the organisation or person name, `[A-Za-z0-9-]`, ≤ 10 characters (longer names are truncated; the full name is in the README and manifest) | RD F4.2 (ASCII English names; native titles in README/manifest) |
| Case folder | `<CaseNo>_<ShortTitle>`: case number with `/` → `-` (e.g. `EQ-FIN-JAI-2027-00042`), short title ≤ 18 characters (`Lender-v-Borrower` style built from roles where names are redacted) — total ≤ 40 | Path budget |
| File name | `<YYYY-MM-DD>_<DocType>_<ShortRef>_v<NN>.<ext>`; `_signed`, `_rendition`, `_T` (type copy), `_TR-<lang>` (translation) suffixes before the extension; ≤ 64 characters by default, hard maximum 80 | RD DI-C18 |
| Allowed characters | `[A-Za-z0-9._-]` only | Windows and SharePoint invalid characters `< > : " / \ \| ? *`, control characters 0–31 [RD 10, 12] |
| Forbidden names | `CON`, `PRN`, `AUX`, `NUL`, `COM1–COM9`, `LPT1–LPT9` (also with any extension), `.lock`, `desktop.ini`, names starting `~$`, `_vti_` anywhere, trailing space or period, leading space | [RD 10, 12] |
| Case-insensitive uniqueness | Two names differing only in case are not allowed in one folder (Windows is case-insensitive) | [RD 12] |
| Path below root | ≤ **140** characters (root excluded; includes `data/` in archival bags) | Office desktop apps on Windows are limited to 256 characters; Windows MAX_PATH 260 unless long paths enabled [RD 11, 12]. Windows "Extract All" creates a folder named after the ZIP, so the worst case is `C:\Users\<10-char name>\Downloads\` (30) + ZIP-name folder (≤ 40 + 1) + root (≤ 40 + 1) + 140 = 252 ≤ 256; measured from the extraction folder the path is ≤ 181, in line with RD's ≤ 180 budget relative to the bag root and ≥ 70 characters of local prefix [RD F4.2] |
| Depth | ≤ 6 levels below root | RD F4.2 |
| SharePoint/OneDrive | Decoded path including file name ≤ 400; sync error beyond 520 (local path plus root) — met by the budget above for libraries with paths ≤ 190 characters. Desktop Office opening a file from a OneDrive-synced folder is still bound by 256 characters: the push (AC.13.10) places packages directly under a short library folder (`/Equator/`) and the README advises a short sync location | [RD 10, 11] |
| macOS | Office 1,024 UTF-8 bytes; names ≤ 255 — met by ASCII names | [RD 11] |

**Shortening algorithm (deterministic):** (1) drop vowels from `ShortRef` after its first letter; (2) truncate `ShortTitle`; (3) truncate `DocType` to its registered abbreviation (`cfg.doc_type_abbreviations`, e.g. `StatementOfClaim` → `SoC`); (4) replace `ShortRef` with an 8-character base32 hash of the document ID. Each shortening is recorded in the manifest (`export_name` vs `original_name`). The validator `XPT_NAME_INVALID` / `XPT_PATH_TOO_LONG` (422) runs on the full tree before packaging; an export never ships with a failing name.

### AC.13.8 File-format rules

| Record kind | Working copy | Record copy | Notes |
|---|---|---|---|
| Narrative documents generated by Equator (orders, notices, minutes, summaries, letters) | DOCX (OOXML Transitional conformance) | PDF/A-2b | ISO/IEC 29500-1:2016 in force; Edition 5 being published (stage 60.00, 13 Oct 2026) — recheck Office defaults Q1 2027 [RD 38] |
| Registers, ledgers, indexes, MIS | XLSX | PDF/A-2b summary where a signed or certified statement is needed | Also CSV (RFC 4180, CRLF, quoted fields, UTF-8 **with BOM** for Excel with Indic text) and JSON [RD F4.1, RD 39] |
| Presentations (training decks, board-style reports) | PPTX | PDF/A-2b | — |
| User uploads (any allowed type) | — | **Original bytes, untouched** | Plus existing renditions (PDF conversion, OCR, type copy, translation) labelled per NN-32 |
| Signed instruments (awards, settlements, orders signed by DSC or Aadhaar eSign, LoAs) | — | **Byte-exact signed original** `…_signed.pdf`; human-readable `…_rendition.pdf` (PDF/A-2b) labelled "Rendition — not the signed original" | Never re-render, flatten, OCR or watermark a signed PDF; SHA-256 of the exported file must equal the evidence-ledger hash [RD F4.3] |
| E-signature evidence | — | ESP audit-trail PDF (as received), signer certificate chain, ESP transaction ID, timestamps (`Signature_Evidence.json`) | Long-term validation (PAdES-LTV) per ESP **[VERIFY — open (vendor), RD open point 9]** |
| eStamp | — | eStamp certificate as issued | — |
| BSA 2023 s.63(4) certificates | — | PDF/A as generated (Part A, Part B where signed) | NN-10 |
| Audit trails | `audit_trail.csv`, `audit_trail.json` | `audit_trail_summary.pdf` (PDF/A-2b) | With anchors and `verify_audit.py` [RD F4.3] |
| Recordings (arbitration only) | — | Original MP4/M4A | Transcript DOCX + VTT; "unverified" label until tribunal approval (FR-P04-41) |
| Structured data | CSV + JSON | — | JSON Schema per entity in `99_Manifest/schemas/` |
| Sources embedded in a PDF statement | — | PDF/A-3b only | PDF/A-2 attachments must themselves be PDF/A or plain text; A-3 permits arbitrary attachments [RD 36] |

Conversion uses the pinned, sandboxed LibreOffice build already used for court exports (Appendix L §5.7) with output validated by a PDF/A validator (AC.13.13). If conversion fails for a file, the original is exported and the manifest records `conversion_performed = failed` with the reason; the export does not fail for a conversion problem (it fails only for the validation-gate items in AC.13.14).

### AC.13.9 Manifest

**`bag-info.txt` labels** (archival bag; also written as `99_Manifest/bag-info.txt` in the standard package): `Source-Organization: Equator Resolution Service Private Limited` (or the group entity that is the export's data fiduciary), `Contact-Email`, `External-Identifier: <export_run_id>`, `Bagging-Date`, `Bag-Size`, `Payload-Oxum`, `Bag-Group-Identifier` and `Bag-Count` (multi-part), plus Equator labels `EQ-Export-Spec: EQ-EXPORT-1.0`, `EQ-Scope`, `EQ-Scope-Ref`, `EQ-Layout`, `EQ-Requested-By-Role` (role, not name, for DSR exports), `EQ-Approved-By-Role`, `EQ-Redaction-Profile`, `EQ-Generated-At-IST` [RD 35, RD DI-C16].

**`manifest.csv` / `manifest.json` fields** (one row per file; JSON adds nested arrays):

| Field | Meaning |
|---|---|
| `path` | Path relative to the taxonomy root |
| `export_name` | File name as exported |
| `original_name` | Name as uploaded or generated in Equator (native script allowed) |
| `title`, `title_native`, `language` | Human title, native-script title, BCP-47 language |
| `sha256`, `sha512`, `bytes` | Checksums and size |
| `media_type`, `format` | MIME type; format label (`DOCX`, `PDF/A-2b`, `PDF (signed original)`, `CSV`, `JSON`, `MP4`) |
| `record_class`, `retention_class`, `legal_hold`, `confidentiality_tier` | From Appendix L / Q |
| `record_association` | `{entity, id, human_ref}` where entity is one of case, invoice, employee, ticket, … and human_ref is e.g. the case number |
| `source_system`, `source_id`, `version` | Equator module, record ID, version number |
| `document_date`, `created_at_ist` | Legal date and creation instant (IST display) |
| `is_signed_original`, `signature_type` (`aadhaar_esign`, `dsc`, `none`), `esp_txn_ref`, `evidence_ledger_seq` | Signature and ledger linkage |
| `rendition_of` | Path of the signed original or source version this file renders |
| `conversion_performed` | `none`, `docx_to_pdfa2b`, `xlsx_to_pdfa2b`, `ocr_text`, `transliterated_name`, `shortened_name`, `failed:<reason>` |
| `redaction_profile`, `redactions_applied` | Profile code and count (AC.13.12) |
| `excluded_siblings` | Count of items excluded from this record's folder and the exclusion reason codes (AC.13.11) |

`99_Manifest/export_certificate.pdf` (PDF/A-2b, signed with Equator's DSC): scope, requester role, approver role, counts by folder, manifest SHA-256, generation time (IST), layout, exclusions summary [RD DI-C16].

### AC.13.10 Large exports
- **Archive format:** ZIP with ZIP64 records always written (needed when any size or offset exceeds 4 GiB or entries exceed 65,535) and general-purpose bit 11 set for UTF-8 names [RD 37]. Windows File Explorer and macOS Archive Utility compatibility with ZIP64 is tested in AC.13.13; the README names a free fallback extractor **[VERIFY — open (test): built-in extractor behaviour with ZIP64 and > 4 GiB parts on Windows 11 and macOS]**.
- **Parts:** packages larger than `tenant.xpt.part_max_gb` (T, default 20, bounds 1–50) are split into self-contained parts by top-level or case folder (never mid-file), named `Equator_Export_<Org>_<YYYY-MM-DD>_p01.zip` (root folder inside of the same name, ≤ 40 characters, AC.13.7); each part carries the full `00_README.pdf` stating "part 1 of 3" and a part manifest; `Bag-Group-Identifier`/`Bag-Count` link them [RD F4.1].
- **Delivery:** the `exports` bucket (7-day lifecycle, P00 FR-P00-20); presigned links ≤ 5 minutes issued on demand per click; HTTP range requests allow **resumable download**; the web download manager shows per-part progress and verifies each part's SHA-256 after download; mobile offers "Send to my email as links" rather than downloading multi-GB parts.
- **Direct push:** to SharePoint, OneDrive, Google Drive (when ON), SFTP or a customer S3 bucket through `STORAGE_PORT`; uploads > 250 MB use upload sessions [RD F1.3]; after push, a **sample re-hash** (≥ 2% of files or ≥ 50 files, whichever is more) compares SHA-256 with the manifest and records `migration_verified` [RD F4.4].
- **Regeneration:** an expired package is regenerated on request from the same pinned data snapshot ID where retention allows; otherwise from current data with a new run ID.

### AC.13.11 What cannot be exported, and why

| Item | Excluded from | Reason | What the README says |
|---|---|---|---|
| Caucus notes (`CAU`) and `NEUTRAL_ONLY` caucus shares of **other** parties | Every party, tenant and full-case export | NN-11; A&C s.75 and s.70 proviso; Mediation Act s.22–23 once notified | "Confidential caucus material is not included." |
| Own caucus submissions marked "keep confidential" | Other parties' exports (included in the submitting party's own export) | Same | — |
| Neutral annotations, deliberation room notes, draft awards | All exports except the author neutral's own `NEUTRAL_PRACTICE` while retained | Deliberation secrecy (Appendix L §1.10) | "Tribunal working papers are not part of the record." |
| `INT` (registry internal) items: scrutiny notes, conflict checks, file notes | Party and tenant exports other than `CASE_FULL` for the administering registrar | Appendix L §1.2(c) | Count only |
| Sealed stores (POSH, health, family safety) | All exports, except through the sealed service's own export to the authorised IC presiding officer or to the data principal for her own data (break-glass rules, Q SC-14) | NN-07 | "Sealed records are available only through the sealed records process." |
| Other parties' private drafts, KYC documents, liveness media, contact details beyond what was served | Party exports | Appendix L §2; S §3.14 | — |
| Data of other tenants, other legal entities' partitions (AD) | All | RLS; NN-38 | — |
| Sealed third-party data (e.g., a lender's internal credit data seen under AA consent, confidentiality-ring material the requester is outside) | Requesters outside the ring or consent | NN-14; confidentiality ring orders | Count and reason |
| Allocation internals (rotation pointers, Quality Index inputs of other neutrals) | All except aggregated Independence Evidence Pack | NN-03, NN-28 | "The Independence Evidence Pack is included instead." |
| Security logs, secrets, keys, provider credentials | All | Q SC-08 | — |
| Aadhaar numbers (never stored) | All | NN-14 | — |
| Data under a legal hold that a court or regulator has ordered not to be disclosed | Per order | Legal order | Generic notice where the order permits |

### AC.13.12 Redaction for multi-party cases
Redaction profiles (`xpt.redaction_profiles`, tier G; maker-checker `legal_reviewer`):
- `party_standard` (default for `PARTY_IN_CASE`, `USER_SELF`): documents are exported **as they were served or filed** — never altered, because the party has already received them; redaction applies only to **structured data and metadata Equator generates for the export** — other parties' contact details (phone, email, address) masked unless already contained in a served document; access history of other sides shown by role and count only; other sides' payment details excluded; vulnerability flags and screening outcomes never included (CaseParty rules).
- `party_minimal` (requester chooses; e.g. for sharing with an adviser): additionally replaces other parties' names in generated summaries with roles.
- `registry_full` (`CASE_FULL`): no redaction of party identities; still applies AC.13.11 exclusions.
- `public_redacted` (only through Appendix R publication; never used for exports).
- `dsr_subject` (`DSR_PORTABILITY`): only the data principal's own data plus case documents in their audience; third-party personal data in generated data files masked.
Arbitration filings are always `ALL_PARTIES` (Appendix L L-D-03), so in arbitration every party's export contains the same filed record; in mediation and conciliation, documents shared with only some parties appear only in those parties' exports.

### AC.13.13 Verification tests (CI and quarterly manual)
Automated on every build of `packages/export-spec` and nightly on a seeded export of each scope:
1. **OOXML validation** of every generated DOCX/XLSX/PPTX with the Open XML SDK validator (Transitional), zero errors.
2. **PDF/A validation** of every record copy with a PDF/A validator (veraPDF or equivalent), declared part and level must pass.
3. **Round-trip open** in a pinned LibreOffice headless build (no repair prompt).
4. **Path and name validator** (AC.13.7) on the whole tree.
5. **Manifest completeness**: every file listed exactly once; checksums match; BagIt validity for archival bags.
6. **Signed-original identity**: SHA-256 equals `core.evidence_ledger` for every `is_signed_original`.
7. **Audit verification**: `verify_audit.py` passes on `10_Audit_Trail` against the anchors.
8. **CSV checks**: RFC 4180 conformance; BOM present; Indic text round-trips in Excel import test fixtures.
9. **Export coverage** *(v3.1; master OP-4, DoD V-4)*: CI test `XPT_EXPORT_COVERAGE` reads the schema catalogue of every plane and fails the build when a table holding tenant, legal-entity or personal data (detected by `tenant_id`, `legal_entity_id`, `person_id`, `employee_id` or `party_id` columns, or a `pii` column tag) is neither mapped to an export scope and folder (AC.13.3–AC.13.6, in `packages/export-spec/coverage.yaml`) nor listed in AC.13.11 with its reason. The test also fails on a mapping that names a table or column that no longer exists, and prints the unmapped tables per owning phase so that the phase adding a table maps it in the same PR.
Quarterly manual test (evidence to `eng.control_evidence`): open a sample of 30 files from each layout in **Word, Excel and PowerPoint for the web (Business Basic)**, desktop Office on Windows 11 and macOS, after extracting with the built-in extractor into `C:\Users\<10-char name>\Downloads\` and into a OneDrive-synced folder; record any repair prompt, path error or garbling as a defect.

### AC.13.14 Export lifecycle and validation gate
States (`xpt.export_runs.status`): `requested → awaiting_approval → approved → snapshotting → building → validating → ready → delivered → expired`; side states `rejected`, `failed`, `cancelled`. Transitions:

| From | To | Condition |
|---|---|---|
| `requested` | `awaiting_approval` | Scope requires maker-checker (AC.13.3) |
| `requested` / `awaiting_approval` | `approved` | Checker ≠ maker; step-up valid |
| `approved` | `snapshotting` | `ExportBuildWorkflow` starts; a consistent read snapshot ID is recorded |
| `snapshotting` | `building` | Item list resolved with entitlement filter and exclusions |
| `building` | `validating` | All files written to the staging prefix |
| `validating` | `ready` | **Gate:** bag/package valid; every signed original's SHA-256 equals its ledger hash (`XPT_SIGNATURE_HASH_MISMATCH` otherwise); audit extract verifies (`XPT_AUDIT_EXTRACT_INVALID`); names and paths pass (`XPT_PATH_TOO_LONG`, `XPT_NAME_INVALID`); exclusion rules re-checked by an independent policy pass (`XPT_EXCLUSION_RULE_VIOLATION`) |
| `validating` | `failed` | Any gate failure (Critical incident if a hash mismatch) |
| `ready` | `delivered` | First successful download or push with `migration_verified` |
| `ready` / `delivered` | `expired` | Bucket lifecycle (7 days) or 90-day exit window end for exit packages (link regenerable) |
| `snapshotting` / `building` / `validating` *(v3.1)* | `cancelled` | Requester or checker cancels; staging prefix deleted; nothing delivered |
| `building` *(v3.1)* | `building` (resumed) | Worker or activity failure: resumes from the last checkpoint on the same snapshot ID (AC.13.15 (2)) |
| `validating` *(v3.1)* | `failed` | Test-open failures above the threshold (AC.13.15 (4); `XPT_TEST_OPEN_FAILED`) |

### AC.13.15 Progress, resumable build and download, and test-open verification *(v3.1)*

1. **Progress you can see.** `xpt.export_runs.progress` (jsonb) holds `phase`, `items_done`/`items_total`, `bytes_done`/`bytes_total`, `parts_ready`/`parts_total`, `eta_at` and the last checkpoint. `GET /v1/exports/{id}/progress` returns it, and a server-sent-events stream `GET /v1/exports/{id}/progress:stream` pushes changes at most every 5 seconds. The UI shows a phase stepper (Approval → Snapshot → Building → Checking → Ready), a percentage bar per phase, the ETA and the approver's name or role while waiting; the user may leave the page. On `ready` (or failure, with the reason in plain words) the requester is notified in-app, by e-mail through `EMAIL_PORT` and by push where enabled — never with file content or a download link in the message body (the link opens Equator, IP-10).
2. **Resumable build.** `ExportBuildWorkflow` checkpoints after each top-level folder, each case folder and each part; every file write is idempotent on `(export_run_id, path)` with its SHA-256, so a crashed worker resumes without duplicates or gaps on the **same pinned snapshot** (AC.13.14 `snapshotting`). If the snapshot can no longer be read (retention or legal hold change), the run restarts from a new snapshot with a new run ID and the README states both IDs.
3. **Early parts and resumable download.** For multi-part packages each part passes the full validation gate on its own (AC.13.14) and becomes downloadable as soon as it passes, if `tenant.xpt.early_part_download` (T, default ON) — the README in each part says "part n of N; the export certificate follows when all parts are ready". The web download manager downloads parts in parallel (≤ 3), uses HTTP range requests to **resume** after a dropped connection, retries automatically 3 times with back-off, renews expired presigned links on demand within the availability window without a new approval (step-up only; after the window `XPT_LINK_RENEWAL_NOT_ALLOWED`, 410, with a one-click "request again" that re-uses the preset), verifies each part's SHA-256 after download, and records each completed and verified download in `xpt.export_deliveries` (`bytes`, `completed_at`, `client_verified`). A plain "copy all links" list is offered for users who prefer their own download tool; links stay single-use and ≤ 5 minutes once issued.
4. **Test-open verification on the actual package.** Before `ready`, `TestOpenActivity` opens a stratified sample of the run's own files — every generated document type at least once, plus `tenant.xpt.test_open.sample_pct` (T, default 5%; minimum 20 files, maximum 500) — in the pinned headless LibreOffice build with the OOXML and PDF/A validators of AC.13.13 (no repair prompt, no validation error, page count > 0, text extractable for non-scanned documents). Signed originals are checked by hash only and are never opened by a converter. A failing working copy is regenerated once; if it fails again, the PDF/A record copy is kept, the manifest records `conversion_performed = failed:test_open`, and `00_README.pdf` lists the file under "Files that may need repair". If more than `tenant.xpt.test_open.max_fail_pct` (T, default 2%, bounds 0–5) of sampled files fail, the run fails with `XPT_TEST_OPEN_FAILED` and a Sev-3 engineering incident is opened (Appendix AE §AE.9.1). The result ("48 of 48 sampled files opened without repair on {date} IST") is printed in `00_README.pdf` and `export_certificate.pdf`.
5. **Verify after download (self-service).** `/exports/verify` lets a recipient drop the extracted folder or the ZIP and checks every file against `manifest.json` with in-browser streaming SHA-256 (WebAssembly); **nothing is uploaded** to Equator. `99_Manifest/Tools/verify_package.py` remains the offline route.
6. **KPIs.** Time to ready (p50/p95) against the AC.13.3 targets per scope; first-pass validation rate ≥ 98%; test-open failure rate ≤ 0.5% of sampled files; download completion rate ≥ 95% within the availability window; resumed-build share (an operational health signal). These feed SCR-P21-04 and the Appendix AE metrics. *(v3.1)*

## AC.14 Import and migration into Equator

### AC.14.1 Sources and templates

| Source | Format | Template / mapping set | Lands in |
|---|---|---|---|
| Spreadsheets (cases, parties, claims, contacts, employees, tickets) | XLSX or CSV (RFC 4180) | Downloadable templates per object with a `README` sheet, data-validation lists and an example row (`xpt.import_templates`) | Target module via its own validated service (never direct table writes) |
| Other ODR tools | CSV/JSON case export + document folder | Mapping set `odr_generic_v1` (case, party, document, event) | `core.cases` with source `imported_legacy`; documents through DMS ingest |
| CRMs (HubSpot, Zoho CRM, Brevo) | Vendor export CSV or API pull | Mapping sets `hubspot_v1`, `zoho_crm_v1`, `brevo_v1` (run by `CrmMigrationWorkflow`, Appendix X §X.10.3) | `ops.crm_*` (Equator CRM, X-51) with consent provenance |
| Payroll and HR tools | CSV/XLSX employee master, leave balances, YTD pay | `payroll_generic_v1` | `hr`, `pay` (P18) opening balances |
| Accounting (opening balances, customers) | CSV/XLSX | `ledger_opening_v1` | Billing masters with history rows |
| Another Equator tenant or entity | `EQ-EXPORT-1.0` package | Native (manifest-driven) | Target tenant, subject to AD grants and GDSA where cross-entity |

### AC.14.2 Process (`ImportMigrationWorkflow`)
1. **Upload and scan:** files to quarantine; malware scan; SHA-256; schema sniff.
2. **Map:** choose or clone a mapping set; unmapped columns listed; enum values mapped through lookup tables; tier G review for identity, consent or money fields.
3. **Dry run:** full validation without writes; report per row (`ok`, `warning`, `error` with field and code), duplicate detection (PAN/GSTIN/CIN keyed hashes, email, phone, case reference), and projected counts per target object.
4. **Approve:** maker-checker (`ops_manager` + `compliance_officer` for personal data; `registrar` checker for cases; `hr_manager` + `payroll_checker` for payroll).
5. **Commit:** in batches of ≤ 1,000 rows, idempotent per `(import_batch_id, row_no)`; each created record carries `import_batch_id` and `source_ref`.
6. **Reconcile:** `xpt.reconciliation_reports` compares source counts and control totals (rows, sum of claim amounts in minor units, number of documents, total bytes, hash list) with committed results; any variance blocks closure of the batch until explained.
7. **Rollback window:** for CRM, contacts, tickets and configuration imports, a batch may be soft-rolled back within `tenant.xpt.import_rollback_days` (T, default 7) if nothing downstream depends on it; **cases, documents, ledgers and payroll are never rolled back** — corrections are new records or reversing entries (NN-22, NN-36).

### AC.14.3 Integrity rules for imported records
- Imported cases are pinned to a `legacy_import` ruleset version and show the banner "Imported record — history before {import date} comes from {source}" (no fabricated Equator audit history: the audit chain starts with `imported` events carrying the source file hash).
- Imported documents are originals for Equator's purposes from the import time; the chain of custody starts at import; a s.63(4) Part A certificate can be generated only by the importing party for its own records (NN-10).
- Imported consents keep their source, date and wording reference; a contact without provable marketing consent is imported as `no_marketing_consent` (RB-23; NN-16 suppression).
- No bulk import of Bar Council rolls or institute directories (NN-39): the `dir` importer rejects professional records not created or claimed by the professional (`XPT_IMPORT_SOURCE_FORBIDDEN`, 422).

## AC.15 Data model summary
Full DDL is in P21 §7.2. New tables (Appendix F conventions; tenant RLS; `xpt` and `cfg` tables carry `legal_entity_id` for group partitioning per Appendix AD):
- `cfg`: `workspace_connections`, `workspace_capability_matrix`, `workspace_group_map`, `integration_catalogue`, `system_of_record`, `mapping_sets`, `field_mappings`, `ledger_maps`, `migration_rehearsals`, `connector_health_checks`, `mirror_targets`, `mirror_items`, `transliteration_tables`, `doc_type_abbreviations`, `vendor_price_refs`.
- `xpt`: `export_requests`, `export_runs`, `export_items`, `export_parts`, `export_deliveries`, `redaction_profiles`, `erasure_propagations`, `import_templates`, `import_batches`, `import_rows`, `reconciliation_reports`; *v3.1:* `export_presets`, `export_schedules`, `export_checkpoints`, `test_open_results`, and columns `export_runs.progress jsonb`, `export_deliveries.client_verified boolean` (AC.13.15).

## AC.16 Error codes (register in Appendix F §F.10.4 v3)
Workspace JML codes `HR_PREJOIN_CHECKS_INCOMPLETE`, `HR_WORKSPACE_SKU_INSUFFICIENT` and `HR_WORKSPACE_DELETE_BLOCKED_HOLD` are registered by Appendix Z and used here unchanged.

| Code | HTTP | Message (en) |
|---|---|---|
| `CFG_SOR_UNDECLARED` | 409 | Declare the system of record for this data before enabling the connector. |
| `CFG_MAPPING_MISSING` | 409 | An approved field mapping is required for this object. |
| `CFG_CONNECTION_CONSENT_REVOKED` | 409 | The connected workspace has revoked Equator's access. |
| `OPS_MEETING_CLASS_NOT_PERMITTED` | 422 | This meeting must be held in an Equator hearing room. |
| `OPS_MEETING_HOST_TENANT_IS_PARTY` | 409 | A meeting cannot be hosted in a party's own workspace. |
| `XPT_SCOPE_NOT_PERMITTED` | 403 | You cannot export this scope. |
| `XPT_APPROVAL_REQUIRED` | 409 | This export needs a second approver. |
| `XPT_NAME_INVALID` | 422 | A file or folder name is not portable. |
| `XPT_PATH_TOO_LONG` | 422 | A path exceeds the portable length budget. |
| `XPT_SIGNATURE_HASH_MISMATCH` | 500 | A signed original does not match its ledger hash. (Critical incident) |
| `XPT_AUDIT_EXTRACT_INVALID` | 500 | The audit-trail extract failed verification. |
| `XPT_EXCLUSION_RULE_VIOLATION` | 500 | The package included an item that must be excluded. (Critical incident) |
| `XPT_PUSH_VERIFY_FAILED` | 502 | Files pushed to the destination did not match the manifest. |
| `XPT_ACCOUNTING_PERIOD_REEXPORT_REQUIRED` | 409 | This period changed after export; re-export is required. |
| `XPT_IMPORT_RECONCILIATION_VARIANCE` | 409 | Import totals do not match the source; explain or fix before closing. |
| `XPT_IMPORT_SOURCE_FORBIDDEN` | 422 | This source cannot be imported. |
| `XPT_TEST_OPEN_FAILED` *(v3.1)* | 500 | Too many sampled files failed to open cleanly; the export was not released. |
| `XPT_LINK_RENEWAL_NOT_ALLOWED` *(v3.1)* | 410 | This package is no longer available; request a new export. |

## AC.17 Key settings (full catalogue in P21 §9)

| Key | Tier | Default | Who may change |
|---|---|---|---|
| `iam.leaver_revoke_hours` | L (floor 4; tenant may only tighten) | 4 | `it_admin` + `compliance_officer` |
| `tenant.hr.workspace.sku_rules` | T with maker-checker (Appendix Z) | AC.3.3 | `it_admin` maker, security lead checker |
| `tenant.hr.workspace.upn_pattern` | T | `{first}.{last}` | `it_admin` |
| `tenant.hr.workspace.delete_delay_days` | T (30–365; Appendix Z) | 90 | `it_admin` + `hr_manager` |
| `ops.workspace.google.enabled` (canonical `platform.ops.workspace.google.enabled`; written form kept as alias, Appendix V X-44; also used by Appendices X and Z) | G (flag) | OFF | Company Secretary + DPO after residency ADR |
| `tenant.chm.meetings.teams_bridge` | G (flag) | OFF | `chambers_owner` + Equator `legal_reviewer` |
| `tenant.chm.sharepoint_mirror` / `tenant.ent.sharepoint_mirror` | G (flag) | OFF | Tenant owner + Equator DPO |
| `mkt.brevo.enabled` (connector flag for both Brevo ports; also used by Appendices X and Y) | G (flag) | OFF | `marketing_manager` + DPO (DPA on file) |
| `tenant.ops.connectors.brevo_crm_sync.enabled` (CRM-object sync; Appendix X §X.13) | T (cannot be ON while `mkt.brevo.enabled` is OFF, or before the DPA record, DPDP s.16 check and DPO approval exist) | OFF | `ops_director`; DPO approval recorded |
| `tenant.mkt.brevo.max_requests_per_hour` (account-level budget shared by both Brevo ports, `CRM_PORT` and `MARKETING_PORT`; Appendices X §X.13 and Y §Y.12) | T (≤ 95% of plan limit) | 80 | `marketing_manager` |
| `mkt.brevo.sms_whatsapp.enabled` | G (flag) | OFF | `compliance_officer` after DLT confirmation |
| `mkt.social.<adapter>.enabled` | G (flag) | OFF | `marketing_manager` + `legal_reviewer` |
| `tenant.xpt.part_max_gb` | T (1–50) | 20 | Tenant admin |
| `tenant.xpt.default_layout.<scope>` | T | AC.13.2 | Tenant admin |
| `platform.xpt.root_name_max` | L | 40 | — |
| `platform.xpt.path_budget_below_root` | L | 140 | — |
| `platform.xpt.exclusions.*` | L | AC.13.11 | — |
| `tenant.xpt.import_rollback_days` | T (0–30) | 7 | Tenant admin |
| `tenant.xpt.early_part_download` *(v3.1)* | T | ON | Tenant admin |
| `tenant.xpt.test_open.sample_pct` / `.max_fail_pct` *(v3.1)* | T (1–20 / 0–5); minimum 20 sampled files (L) | 5 / 2 | Tenant admin |
| `tenant.xpt.schedules` *(v3.1)* | T (plan-entitled; sensitive scopes still maker-checker) | none | Tenant admin |
| `platform.xpt.download.parallel_parts` / `.auto_retries` *(v3.1)* | T | 3 / 3 | Platform engineering |
| `platform.integrations.rehearsal_max_age_days` | L | 400 | — |

## AC.18 Acceptance tests
Gherkin scenarios AC-T01 to AC-T24 are in P21 §12 (`tests/acceptance/appendix-AC.feature`), covering: SKU detection and capability hiding (T01), leaver revoke ≤ 4 h with connector down (T02), SKU-insufficient role grant blocked (T03), Teams meeting refused for mediation (T04), Teams host tenant is a party (T05), mirror never overwrites an edited working copy (T06), fallback for every catalogue row (T07), Brevo forged unsubscribe ignored after re-fetch (T08), consent sync within 15 minutes (T09), export taxonomy and names (T10), path budget (T11), signed original byte identity (T12), caucus exclusion (T13), multi-party redaction (T14), ZIP64 parts and resumable download (T15), push re-hash (T16), Office-for-the-web open (T17), import dry run and reconciliation (T18), no case data to workspace (T19), accounting re-export after period change (T20), DSR portability JSON (T21), tenant exit within 7 days and 90-day availability (T22), connector health red on rehearsal age (T23), billing never blocks exit export (T24). *v3.1 additions (now in P21 §12 with FR-P21-44):* AC-T25 pre-flight estimate has no side effects and shows exclusion counts; AC-T26 a worker killed mid-build resumes on the same snapshot with no duplicate or missing manifest rows; AC-T27 a dropped download resumes by range request and the part hash verifies; AC-T28 a seeded corrupt DOCX is regenerated once, then listed under "Files that may need repair"; above the threshold the run fails with `XPT_TEST_OPEN_FAILED`; AC-T29 `/exports/verify` sends no file bytes to the server (network assertion).

## AC.19 Open items and verification flags
1. **Microsoft SKU** — CS to confirm from admin centre or `subscribedSkus`; this appendix assumes Business Basic (D3-04).
2. **Microsoft details** [RD open point 2]: group-based licensing and Entra ID P1; `usageLocation` ordering; mailbox provisioning delay; shared-mailbox limits; Audit (Standard) retention on Basic; Teams recording licence on Basic; add-on India prices; Exchange application RBAC for `Mail.Send`; `onlineMeeting` option properties; delta queries under `Sites.Selected`; Teams webhook mechanism; upload fragment size.
3. **Mailbox size** 100 GB vs 50 GB inconsistency — check tenant quota [RD 2, 4].
4. **Google Workspace** INR prices, scopes, delegation, endpoints [RD open point 4]; adapter OFF.
5. **Brevo** INR prices, catch-all limit for CRM endpoints, webhook retries, DPA and sub-processors, DLT support [RD open point 5].
6. **Adobe** private scheduling API; plan coverage of Content Scheduler [RD open point 6].
7. **Social** Instagram 100 vs 50 limit; Facebook Pages permissions; LinkedIn Standard-tier criteria; X price changes [RD open point 7].
8. **Tally / Zoho Books / payroll tools** import formats and APIs — adapter spikes.
9. **RFC 8493** tag-file placement (AC.13.2); **ZIP64** behaviour of built-in extractors (AC.13.10).
10. **ESP long-term validation** for India CCA chains [RD open point 9].
11. **GST** rate on vendor SaaS for price references — tax adviser.

## AC.20 Phase addenda

### For P01
**FR-P01-V3-AC01 — Portability alias.** `POST /v1/me/exports` (Appendix Q PC-39) becomes an alias of `POST /v1/exports` with scope `USER_SELF`; the rights centre offers `DSR_PORTABILITY` in JSON-first form inside an `EQ-EXPORT-1.0` standard package. *Acceptance:* AC-T21.
**FR-P01-V3-AC02 — SKU-sufficiency check at role grant.** Membership grants of the privileged roles in AC.3.3 call the workspace capability check and fail with `HR_WORKSPACE_SKU_INSUFFICIENT` unless an unexpired exception exists. *Acceptance:* AC-T03.

### For P02
**FR-P02-V3-AC01 — Case export from the DMS.** "Export case file" on the case page creates a `PARTY_IN_CASE` or `CASE_FULL` export with the AC.13.5 mapping from DMS folders; exclusions per AC.13.11. *Acceptance:* AC-T10, AC-T13.
**FR-P02-V3-AC02 — File to Equator from mail.** Staff can file a workspace email into a case `COR` folder through the user-initiated action in AC.8.1; the filed copy is the record. *Acceptance:* filed `.eml` hashed and ledgered.

### For P04
**FR-P04-V3-AC01 — Hearing platform lock.** `VIDEO_PORT` is the only platform for Equator-administered proceedings; the Teams bridge exists only for chambers meeting classes in AC.8.3 and never records. *Acceptance:* AC-T04, AC-T05.

### For P07
**FR-P07-V3-AC01 — Workspace is not a notice channel.** Notice, OTP and statutory templates cannot be bound to `WORKSPACE_PORT` or `MARKETING_PORT` (template-binding validator). *Acceptance:* binding attempt returns 422.

### For P10
**FR-P10-V3-AC01 — Chambers exits and mirrors.** Chambers run-off exports (FR-P10-04) use `CHAMBERS_TENANT` archival bags; the optional SharePoint working-copy mirror follows AC.9. *Acceptance:* AC-T06, AC-T22.

### For P16
**FR-P16-V3-AC01 — Brevo CRM adapter conformance.** The `CRM_PORT` adapter `brevo` built in P16 (Appendix X §X.10.2) meets the vendor contract of AC.11.2: compensating webhook controls (bearer token, IP allow-list, inbox dedupe, re-fetch before any consent-changing event), the shared account-level request budget (AC.5), the `BREVO_EU` transfer row and a `cfg.system_of_record` row for CRM data in `ops`. *Acceptance:* AC-T08, AC-T09.

### For P17
**FR-P17-V3-AC01 — Marketing and social adapter conformance.** The `MARKETING_PORT` adapter `brevo` and the `SOCIAL_PORT` adapters built in P17 (FR-P17-16, FR-P17-24) meet AC.11.2–AC.11.4 and are registered in the integrations catalogue with fallback, SoR rows, approved mapping sets and a migration rehearsal (AC.12). *Acceptance:* AC-T07, AC-T09; each adapter appears on SCR-P21-05 with its flag and approver.

### For P14
**FR-P14-V3-AC01 — Portability and integration go-live gates.** Go-live requires: AC.13.13 automated suite green; one quarterly manual Office test recorded; every enabled connector with an SoR row, approved mapping set and a migration rehearsal ≤ 365 days old; workspace audit-log ingest running for every `workforce` connection. *Acceptance:* go-live checklist items `XPT-01…XPT-04`, `INT-01…INT-03` pass.
