# Appendix L — Integration Adapters and API Catalogue

**LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Binding for P18 (gateway, connectors), P17 (AI providers), P19 (storage), P20/P21 (payments), and the API surface of every module.**

## L.0 Purpose and precedence

This appendix catalogues (1) the LDC public and partner REST API at representative depth for every module, (2) the scope catalogue, (3) the port/adapter specifications for every external integration, (4) the Jio services mapping, (5) the mapping between LDC-internal events and Infrabyx ecosystem events, and (6) LDC-registered file layouts. Precedence: Ecosystem Integration Specification v1.1 for any cross-product contract (NN-23) → this appendix for conventions, scopes, adapters and ecosystem endpoints → for module (tenant) endpoints the phase file §7.3 is binding and §L.3 below is a representative, partner-facing view (§L.1A). Module owners may add endpoints following these conventions; each addition is registered in `packages/contracts` (OpenAPI 3.1) before use and appears in the developer portal automatically.

## L.1 Conventions (summary of P18 §4A)

Base URL `https://api.lawdocscomply.com/v1` (production), `https://api.sandbox.lawdocscomply.com/v1` (sandbox). JSON only (`application/json`; `application/problem+json` for errors; `multipart/form-data` or pre-signed upload URLs for files). `snake_case`; prefixed ULIDs; cursor pagination (`limit` ≤ 500, `cursor`, response `next_cursor`); `updated_since`; `fields`; `expand` (depth ≤ 2); `If-Match`/ETag for PATCH; `Idempotency-Key` on POST/PATCH/DELETE; RFC 9457 errors; rate-limit headers; `Deprecation`/`Sunset` on deprecated endpoints. Ecosystem endpoints follow the Spec exactly (`/v1/grc/...`, `/v1/external-access/...`, `/v1/events`).

Common sub-resources on most business records: `/comments`, `/attachments`, `/history` (audit trail of the record, read-only), `/corrections` (D-02 correction entries; create needs Governed approval for platform overrides), `/watchers`, `/links` (relations), `/export` (record-scope export, P19).

## L.1A Path reconciliation (review, 25 October 2026)

The phase files and §L.3 were drafted in parallel and use two path styles: module-prefixed (`/v1/gov/meetings`, `/v1/dpc/incidents`, `/v1/hr/pay-runs`) and resource-style (`/v1/meetings`). Phases P06 and P07 also write `/api/v1/...` with paths relative to their module. To remove the conflict:

1. **Canonical tenant API = module-prefixed** `/v1/<module-path>/<resource>` exactly as declared in each phase file §7.3 (`/api/v1/...` in P06/P07 means `/v1/...`; the edge gateway serves only `/v1`). The module path is the NestJS module code or its readable plural (`/v1/gov`, `/v1/pol`, `/v1/dms`, `/v1/erm`, `/v1/ral`, `/v1/audit`, `/v1/returns`, `/v1/accounting`, `/v1/dpc`, `/v1/tpr`, `/v1/hr`, `/v1/lab`, `/v1/posh`, `/v1/grv`, `/v1/coop`, `/v1/billing`, `/v1/public`, …); the P18 contract registry records one canonical path per operation.
2. **§L.3 resource-style paths** are a partner-facing summary. Where §L.3 and a phase file name the same operation differently, the phase path is canonical; P18 sprint 1 either publishes the §L.3 path as a documented alias (gateway rewrite, same scopes) or drops it — recorded in an ADR, never two independent implementations.
3. **Ecosystem endpoints** (`/v1/grc/...`, `/v1/external-access/...`, `/v1/events`, `/v1/catalogue/...`, `/v1/evidence-requests`) follow the Ecosystem Spec (and its v1.2 change requests, master §19) and are not module-prefixed.
4. **Contract check:** CI fails when an endpoint appears in code without a registry entry, or when two registry entries implement the same `operationId`.

### L.1A.1 Module path prefixes declared in the phase files (§7.3), with operation counts

| Phase | Path prefixes declared | Operations listed |
|---|---|---|
| P00 | `/v1/audit`, `/v1/corrections`, `/v1/corrections?tenant=…`, `/v1/documents`, `/v1/events?after=…&types=…`, `/v1/flags`, `/v1/migration`, `/v1/platform` | 15 |
| P01 | `/v1/audit-grants`, `/v1/authz`, `/v1/break-glass`, `/v1/delegations`, `/v1/delivery-grants`, `/v1/external-access`, `/v1/invitations`, `/v1/me`, `/v1/onboarding`, `/v1/privacy`, `/v1/role-grants`, `/v1/sso-connections`, `/v1/supervisor-grants`, `/v1/users`, `/v1/users:bulk-import` | 24 |
| P02 | `/v1/branding`, `/v1/config-bundles:export`, `/v1/config-bundles:import`, `/v1/config-change-requests`, `/v1/config:compare?a=&b=`, `/v1/console`, `/v1/custom-fields`, `/v1/dashboards`, `/v1/forms`, `/v1/navigation`, `/v1/notification-templates`, `/v1/org-nodes`, `/v1/org-nodes:merge\|split`, `/v1/rule-challenges`, `/v1/rule-pack-versions`, `/v1/rule-packs`, `/v1/rules:evaluate`, `/v1/setting-packs`, `/v1/settings`, `/v1/settings?section=&scope=`, `/v1/status-sets`, `/v1/terminology`, `/v1/workflow-defs` | 34 |
| P03 | `/v1/applicability`, `/v1/content`, `/v1/templates`, `/v1/templates?family=`, `/v1/tenant` | 14 |
| P04 | `/v1/cmp`, `/v1/ics`, `/v1/rpt`, `/v1/wf` | 22 |
| P05 | `/v1/ai`, `/v1/changes`, `/v1/checkpoints`, `/v1/chg`, `/v1/updates`, `/v1/updates?category&state` | 21 |
| P06 | `/v1/gov` | 32 |
| P07 | `/v1/pol`, `/v1/dms` | 33 |
| P08 | `/v1/erm`, `/v1/grc`, `/v1/int` | 24 |
| P09 | `/v1/alm-runs`, `/v1/capital-runs`, `/v1/compute-modes`, `/v1/icaap-cycles`, `/v1/metric-changes`, `/v1/metric-values?metric=&entity=&from=&to=`, `/v1/metrics`, `/v1/pca`, `/v1/reverse-stress`, `/v1/scenarios`, `/v1/snapshots`, `/v1/stress-runs`, `/v1/templates`, `/v1/uploads`, `/v1/what-if` | 27 |
| P10 | `/v1/acb-packs`, `/v1/analytic-tests`, `/v1/atr`, `/v1/aud-directions-runs`, `/v1/branch-coverage`, `/v1/caro-runs`, `/v1/concurrent`, `/v1/engagements`, `/v1/evidence-links`, `/v1/evidence-requests`, `/v1/findings`, `/v1/inspections`, `/v1/pbc-items`, `/v1/plans`, `/v1/populations`, `/v1/risk-assessments`, `/v1/samples`, `/v1/secretarial`, `/v1/statutory`, `/v1/universe-units`, `/v1/vapt`, `/v1/workpapers` | 33 |
| P11 | `/v1/accounting`, `/v1/applicability`, `/v1/applicability?entity_id=`, `/v1/batches`, `/v1/cic`, `/v1/coa-mappings`, `/v1/datasets`, `/v1/due-instances`, `/v1/due-instances?from&to&state`, `/v1/explained-variances`, `/v1/gst`, `/v1/mapping-profiles`, `/v1/mca`, `/v1/reconciliations`, `/v1/registry`, `/v1/runs`, `/v1/tds`, `/v1/uploads` | 24 |
| P12 | `/v1/dpc`, `/v1/tpr`, `/v1/vendor-portal` | 21 |
| P13 | `/v1/hr`, `/v1/lab`, `/v1/posh` (bare-path list) | 0 |
| P14 | `/v1/grv`, `/v1/public` | 3 |
| P15 | `/v1/applicability`, `/v1/applicability-overlays`, `/v1/applicability?legalEntityId=&status=&regulator=`, `/v1/console`, `/v1/entity-profiles`, `/v1/exemptions`, `/v1/investment-monitors`, `/v1/investment-register`, `/v1/profile-changes`, `/v1/sector-pack` | 19 |
| P16 | `/v1/coop` | 8 |
| P17 | `/v1/ai` | 12 |
| P18 | `/v1/calendar`, `/v1/embed`, `/v1/entitlements`, `/v1/events?after=&types=&limit=`, `/v1/external-access`, `/v1/grc`, `/v1/imports`, `/v1/integrations`, `/v1/onboarding`, `/v1/provisioning`, `/v1/webhook-subscriptions`, `/v1/webhooks` | 19 |
| P19 | `/v1/exits`, `/v1/export-map`, `/v1/export-schedules`, `/v1/exports`, `/v1/folder-policy`, `/v1/intakes`, `/v1/storage-targets` | 18 |
| P20 | `/v1/billing`, `/v1/entitlements`, `/v1/public`, `/v1/savings`, `/v1/savings?period=`, `/v1/signup` | 28 |
| P21 | `/v1/marketplace`, `/v1/public` | 14 |
| P22 | `/v1/delivery`, `/v1/tenant` | 16 |
| P23 | `/v1/help`, `/v1/llms.txt`, `/v1/me`, `/v1/public`, `/v1/tenant` | 19 |
| P24 | `/v1/eng`, `/v1/trust` | 8 |

Counts are those written explicitly in each phase §7.3 (P13 lists resources without methods, so its count reads 0; its prefixes are `/v1/hr`, `/v1/lab`, `/v1/posh`). Together with §L.3 the pack defines roughly 500 operations; the full list is generated from `packages/contracts` and published in the developer portal (P18).

## L.2 Connector certification checklist

| Area | Requirement |
|---|---|
| Manifest | `id` (`[counterparty]-[capability]-ldc`), version, counterparty, capabilities (API, WEBHOOK, POLL, FILE, PORTAL_MANUAL), schemas, scopes, data classes, residency, sub-processors |
| Security | mTLS or `private_key_jwt`; secrets in vault; no secrets in logs; dependency SBOM; container hardening (read-only FS, no shell, non-root); egress allow-list |
| Contract | Pact/contract tests; schema validation; projections carry no forbidden fields |
| Idempotency/ordering | Duplicate-safe; key reuse 422; concurrent 409; out-of-order resolved by `seq` |
| Resilience | 4-hour counterpart outage simulation; partial failures; DLQ and replay; circuit breaker |
| Privacy | `consentref`/`legalbasis` on personal data; data-class ceilings; no personal data in logs; residency checks |
| Regulatory guards | No regulator-portal automation; WhatsApp not used for debt collection; DLT compliance for SMS/voice |
| Reconciliation | Daily counts/hashes; break detection |
| Operations | Health endpoint, metrics, traces, monitor visibility, runbook |
| Evidence | VAPT ≤ 12 months; DPA and outsourcing clauses where an RE is involved (Spec §10.1) |
| Result | `ConnectorCertified` event; listing; recertify on schema/hosting/key/sub-processor change and annually |

## L.3 REST API catalogue (representative; by module)

Scopes in the last column follow §L.4. "(E)" = ecosystem-facing per Spec.

### L.3.1 `core` — tenancy, legal entities, ledger

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/tenant` | Tenant profile | `core.tenant:read` |
| `GET/POST/PATCH /v1/legal-entities` | Legal entities (CIN/LLPIN/registration no., FY, regulators) | `core.entity:*` |
| `GET /v1/audit-events?record_type=&record_id=&from=&to=` | Audit trail query (masked per role) | `core.audit:read` |
| `GET /v1/audit-anchors?date=` | Daily chain anchors | `core.audit:read` |
| `POST /v1/corrections` | Correction entry request (D-02) | `core.correction:request` |
| `POST /v1/corrections/{id}/approve` | Second approval | `core.correction:approve` |
| `GET /v1/feature-flags` | Effective flags for tenant | `core.flags:read` |

### L.3.2 `iam` — identity and access

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST/PATCH /v1/users`; `POST /v1/users/{id}/deactivate` | Users | `iam.user:*` |
| `GET/POST /v1/roles`; `GET /v1/roles/{id}/permissions` | Role catalogue and tenant roles | `iam.role:*` |
| `POST /v1/role-assignments`; `DELETE /v1/role-assignments/{id}` | Assign/revoke (SoD checks) | `iam.assignment:*` |
| `GET/POST /v1/delegations` | Leave delegations (never to the maker) | `iam.delegation:*` |
| `GET/POST /v1/break-glass-sessions` | Platform/delivery access requests (NN-30) | `iam.breakglass:*` |
| `/scim/v2/Users`, `/scim/v2/Groups` | SCIM 2.0 | `iam.scim` |
| `GET /v1/access-reviews`, `POST /v1/access-reviews/{id}/attest` | Access reviews | `iam.review:*` |

### L.3.3 `cfg` — settings, rule packs, terminology, menus

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/settings?keys=` ; `PUT /v1/settings/{key}` | Resolve/change settings (tier rules) | `cfg.setting:read/write` |
| `GET/POST /v1/config-change-requests`; `/{id}/approve` | Governed changes | `cfg.change:*` |
| `GET/PUT /v1/terminology` | Department/function/committee names, labels | `cfg.terminology:*` |
| `GET/POST /v1/rule-packs`, `/{id}/versions`, `/{id}/simulate` | Rule packs (labour, payroll, applicability, calendars) | `cfg.rulepack:*` |
| `GET/PUT /v1/navigation` | Menu customisation (tenant tier) | `cfg.nav:*` |

### L.3.4 `cnt` — regulatory content library

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/authorities` | Regulators/authorities | `cnt.read` |
| `GET /v1/instruments?authority=&entity_family=&status=` | Instrument catalogue (name, date, last update, applicability summary) | `cnt.read` |
| `GET /v1/instruments/{id}/versions`; `/versions/{v}/clauses` | Versions and clauses | `cnt.read` |
| `GET /v1/instruments/{id}/diff?from=&to=` | Clause-level diff | `cnt.read` |
| `GET /v1/content-packs`; `/{id}` | Packs by regulator/entity family | `cnt.read` |
| Console: `POST /v1/console/instruments`, `/versions`, `/publish` | Content operations (maker-checker-publisher) | `plt.content:*` |

### L.3.5 `tpl` — templates and Excel import

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/templates?family=` ; `GET /v1/templates/{code}/download` | Template registry; download exact `.xlsx` | `tpl.read` |
| `POST /v1/question-imports` (multipart xlsx) | Upload a question sheet (platform: global pack; tenant: tenant-only) | `tpl.import:create` |
| `GET /v1/question-imports/{id}` | Validation report (row-level errors/warnings), diff vs existing | `tpl.import:read` |
| `POST /v1/question-imports/{id}/commit` / `/reject` | Commit after review (maker ≠ checker) | `tpl.import:approve` |
| `POST /v1/question-drafts` | Start AI question authoring from an instrument (P05, V-SK-12) | `tpl.draft:create` |
| `GET /v1/question-drafts/{id}/xlsx` | Export draft in exact template | `tpl.draft:read` |

### L.3.6 `cmp` — compliance workspace

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/applicability` ; `POST /v1/applicability/instruments/{id}:add` / `:remove` | Instrument selection with impact preview | `cmp.applicability:*` |
| `GET /v1/obligations?instrument=&department=&status=` | Tenant obligations (base + overlay) | `cmp.obligation:read` |
| `PATCH /v1/obligations/{id}` | Tenant overlay edit (text/actionable/department) — audited | `cmp.obligation:overlay` |
| `POST /v1/obligations` | Tenant-authored obligation | `cmp.obligation:create` |
| `GET /v1/compliance-instances?due_from=&due_to=&owner=&status=` | Instances (calendarised) | `cmp.instance:read` |
| `POST /v1/compliance-instances/{id}/submit` | Maker submits with evidence | `cmp.instance:submit` |
| `POST /v1/compliance-instances/{id}/review` | Checker approve/reject/reallocate | `cmp.instance:review` |
| `POST /v1/compliance-instances/{id}/evidence` | Attach evidence (doc ids) | `cmp.evidence:write` |
| `POST /v1/compliance-instances/{id}/exceptions` | Waiver/exception/extension request | `cmp.exception:create` |
| `POST /v1/attestations/campaigns` ; `/{id}/responses` | Attestation campaigns | `cmp.attestation:*` |
| `GET /v1/issues` ; `POST /v1/issues` | Compliance issues register | `cmp.issue:*` |
| `GET /v1/grc/obligations?updated_since=` (E) | Ecosystem pull | `grc.obligation:read` |
| `GET /v1/grc/kris?updated_since=` (E) | Ecosystem pull | `grc.kri:read` |

### L.3.7 `chg` — regulatory change management

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/updates?authority=&status=&since=` | Updates inbox (regulatory) | `chg.update:read` |
| `GET /v1/updates/{id}` ; `/impact` | Update with what-changed/why/what-to-do and tenant impact | `chg.update:read` |
| `POST /v1/updates/{id}/assess` | Tenant applicability/impact assessment | `chg.assessment:write` |
| `GET /v1/source-monitor/status` | Source freshness (platform; tenant read summary) | `chg.monitor:read` |

### L.3.8 `wf` — tasks, approvals, notifications, calendar

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST/PATCH /v1/tasks` ; `POST /v1/tasks/{id}/complete` | Tasks (hierarchy rules) | `wf.task:*` |
| `GET /v1/inbox` | Work Inbox (approvals, tasks, mentions, AI outputs) | `wf.inbox:read` |
| `POST /v1/approvals/{id}/decision` | Approve/reject | `wf.approval:decide` |
| `GET /v1/notifications` ; `POST /v1/notifications/read` | Notifications (work) — separate from Updates (NN-27) | `wf.notification:*` |
| `GET /v1/calendar/events?from=&to=` | Calendar items (role-scoped) | `cal.event:read` |
| `GET /v1/calendar/feeds` ; `POST /v1/calendar/feeds` (rotate) | ICS feed management | `cal.feed:*` |

### L.3.9 `gov` — governance and company secretarial

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST /v1/boards`, `/v1/committees` ; `/members` | Board and committees (HRMS-linked) | `gov.body:*` |
| `GET/POST/PATCH /v1/meetings` ; `/agenda`, `/notice`, `/papers`, `/attendance`, `/minutes`, `/resolutions` | Meeting lifecycle | `gov.meeting:*` |
| `POST /v1/meetings/{id}/minutes:draft` | Vidhi draft (V-SK-08) | `gov.meeting:write` + `ai.run:create` |
| `GET /v1/registers/{register_code}` | Statutory registers (MGT-1, MBP-2, MBP-3, MBP-4, CHG-7, BEN-3, SH-6 …; MBP-1 is a disclosure form, not a register — X-37) | `gov.register:read` |
| `GET/POST /v1/filings` ; `/{id}/srn` | MCA filings tracker (manual filing, SRN capture) | `gov.filing:*` |
| `GET/POST /v1/fit-and-proper/declarations` | Fit & proper declarations and Board/NRC assessment | `gov.fitproper:*` |
| `GET/POST /v1/disclosures` | Director disclosures (MBP-1, DIR-8), interests | `gov.disclosure:*` |
| `GET/POST /v1/listed/lodr-filings` | Listed-company LODR filings tracker | `gov.lodr:*` |
| `GET/POST /v1/upsi/sdd-entries` | Structured digital database (SEBI PIT) — sealed | `gov.upsi:*` |

### L.3.10 `pol` — policies

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST /v1/policies` ; `/versions` ; `/versions/{v}/submit\|approve\|publish` | Policy lifecycle | `pol.policy:*` |
| `POST /v1/policies/{id}/drafts:ai` | Vidhi redline draft (V-SK-05) | `pol.policy:write` + `ai.run:create` |
| `GET /v1/policy-templates?type=&family=` | Model templates | `pol.template:read` |
| `POST /v1/policies/{id}/attestations` | Staff attestations | `pol.attestation:*` |
| `GET /v1/public/disclosures/{tenant}/{slug}` | Public disclosure page data (embed) | public |

### L.3.11 `dms` — documents and evidence

| Method & path | Purpose | Scope |
|---|---|---|
| `POST /v1/uploads` (pre-signed) ; `POST /v1/documents` | Upload and register | `dms.document:write` |
| `GET /v1/documents?folder=&tag=&q=` ; `GET /v1/documents/{id}/versions` | Search/list, versions | `dms.document:read` |
| `GET /v1/documents/{id}/content?version=&rendition=` | Download (original, PDF, type copy, translation) | `dms.document:read` |
| `POST /v1/documents/{id}/share` | Selective share (users, external recipients with expiry) | `dms.share:create` |
| `POST /v1/esign-envelopes` ; `GET /v1/esign-envelopes/{id}` | eSign | `dms.esign:*` |
| `POST /v1/documents/{id}/typecopy` / `/translate` | AI renditions (P17) | `dms.document:read` + `ai.run:create` |
| `POST /v1/legal-holds` ; `DELETE /v1/legal-holds/{id}` | Legal holds | `dms.hold:*` |

### L.3.12 `erm` and `ral` — risk

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST/PATCH /v1/risks` ; `/assessments` | Risk register, inherent/residual | `erm.risk:*` |
| `GET/POST /v1/rcsa-campaigns` ; `/responses` | RCSA | `erm.rcsa:*` |
| `GET/POST /v1/kris` ; `/observations` | KRIs (local or from Finbyx feed) | `erm.kri:*` |
| `GET/POST /v1/loss-events` | Loss events | `erm.loss:*` |
| `GET/PUT /v1/risk-appetite` | RAS and thresholds (approval flow) | `erm.appetite:*` |
| `GET/POST /v1/scenarios` ; `POST /v1/stress-runs` ; `GET /v1/stress-runs/{id}` | Scenario library and stress runs | `ral.stress:*` |
| `GET/POST /v1/icaap-cycles` ; `/chapters` | ICAAP | `ral.icaap:*` |
| `GET /v1/ratios?entity=&as_of=` | Ratio library values (computed or received) | `ral.ratio:read` |
| `POST /v1/ratio-inputs` | Manual/imported inputs (non-Finbyx tenants) | `ral.input:write` |

### L.3.13 `aud` — audit

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST /v1/audit-universe` ; `/v1/audit-plans` | Universe and plans | `aud.plan:*` |
| `GET/POST /v1/engagements` ; `/programs`, `/workpapers`, `/samples`, `/findings` | Engagement lifecycle | `aud.engagement:*` |
| `POST /v1/findings/{id}/responses` | Management response | `aud.finding:respond` |
| `POST /v1/engagements/{id}/report:draft` | Report drafting (V-SK-16) | `aud.report:write` |

### L.3.14 `ret` and `acc` — returns, data prep, accounting bridge

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/return-definitions?regulator=&entity_family=` | Return catalogue (kernel) | `ret.definition:read` |
| `GET/POST /v1/return-runs` ; `/validate`, `/approve`, `/package`, `/acknowledgement` | Return Studio runs (non-Finbyx) | `ret.run:*` |
| `POST /v1/data-prep-jobs` ; `/mapping`, `/execute` | Data preparation from Tally/Excel/LMS | `ret.prep:*` |
| `GET /v1/bureau-files` ; `POST /v1/bureau-files` | CIC submission files (layout packs) | `ret.bureau:*` |
| `GET/POST /v1/tax-exports` | GST/TDS export files (GSTN offline-tool JSON etc.) | `ret.tax:*` |
| `POST /v1/trial-balances` ; `GET /v1/financial-statements?entity=&period=` | Accounting bridge | `acc.tb:*`, `acc.fs:read` |

### L.3.15 `dpc`, `tpr` — data protection, cyber, third parties

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST /v1/processing-activities` | ROPA | `dpc.ropa:*` |
| `GET/POST /v1/dpias` | DPIAs | `dpc.dpia:*` |
| `GET/POST /v1/consents` ; `/withdrawals` | Consent ledger (tenant's data principals where hosted) | `dpc.consent:*` |
| `GET/POST /v1/data-principal-requests` | DSR workflow | `dpc.dsr:*`, `privacy.request:write` (E) |
| `GET/POST /v1/incidents` ; `/notifications` | Security/data incidents with CERT-In/RBI/DPB clocks | `dpc.incident:*` |
| `GET/POST /v1/controls` ; `/tests` | ISMS controls library and tests | `dpc.control:*` |
| `GET/POST /v1/vendors` ; `/assessments`, `/contracts` | TPRM and outsourcing register | `tpr.vendor:*` |

### L.3.16 `hr`, `lab` — HRMS and labour

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST/PATCH /v1/employees` (minimal vs full views by role) | Employees | `hr.employee:*` |
| `GET/POST /v1/org-units` ; `/positions` | Departments, positions, reporting lines | `hr.org:*` |
| `GET/POST /v1/leave-requests` ; `/attendance` | Leave and attendance | `hr.leave:*`, `hr.attendance:*` |
| `GET/POST /v1/pay-runs` ; `/approve` ; `/bank-file` | Payroll (maker-checker; bank file, D-11) | `hr.payroll:*` |
| `GET /v1/labour-registers/{code}` | Registers under the Labour Codes | `lab.register:read` |
| `GET/POST /v1/posh/committees` ; `/v1/posh/cases` (sealed) | POSH IC | `lab.posh:*` |
| `GET/POST /v1/employment-agreements` | Agreements with eSign | `lab.agreement:*` |

### L.3.17 `grv`, `coop`, `ai`, `int`, `xpt`

| Method & path | Purpose | Scope |
|---|---|---|
| `GET/POST /v1/grievances` ; `/acknowledge`, `/escalate`, `/resolve`, `/reopen` | Grievance desk | `grv.case:*` |
| `POST /v1/embed/grievances` ; `GET /v1/embed/grievances/{ref}/status` | Embeds (publishable key) | `grievance.intake:create` |
| `GET/POST /v1/societies/members` ; `/elections` ; `/general-body-meetings` | Co-operative suite | `coop.*` |
| `/v1/ai/*` | See P17 §7.3 | `ai.*` |
| `/v1/events`, `/v1/webhook-subscriptions`, `/v1/provisioning/*`, `/v1/imports/*`, `/v1/onboarding/lookups`, `/v1/external-access/grants` (E) | See P18 §7.3 | `int.*` / (E) |
| `/v1/exports`, `/v1/storage-targets`, `/v1/export-schedules`, `/v1/intakes`, `/v1/exits` | See P19 §7.3 | `xpt.*` |

### L.3.18 `bil`, `mkp`, `sdc`, `web`, `hlp`, `rpt`, `eng`

| Method & path | Purpose | Scope |
|---|---|---|
| `GET /v1/public/pricing` | Public pricing catalogue (plans, components, features) | public |
| `POST /v1/public/quotes` | Configurator quote (Apple-style builder) | public (rate-limited) |
| `GET/POST /v1/subscriptions` ; `/change-plan` ; `/cancel` | Subscription management | `bil.subscription:*` |
| `GET /v1/invoices` ; `/{id}/pdf` | Invoices (GST) | `bil.invoice:read` |
| `GET /v1/savings` | Savings ledger (hours, money, penalties avoided — evidence-backed) | `bil.savings:read` |
| `GET /v1/public/marketplace/services?category=` ; `/providers/{id}` | Public marketplace | public |
| `POST /v1/marketplace/orders` ; `/engagements` ; `/retainers` | Orders and engagements | `mkp.order:*` |
| `GET/POST /v1/delivery/clients/{tenant}/messages` ; `/deliverables` ; `/drive-links` | Service Delivery Console (P22) | `sdc.*` |
| `GET/POST /v1/delivery/clients/{tenant}/credentials` ; `/reveal` (MFA) | Credential vault (D-04) — not callable by connectors or Vidhi | `sdc.vault:*` |
| `POST /v1/public/health-check/sessions` ; `/answers` ; `/report` | Free compliance health check | public (bot-protected) |
| `GET /v1/help/articles` ; `/glossary/{key}` | Help centre and "i" tooltips | `hlp.read` / public |
| `GET/POST /v1/dashboards` ; `/widgets` ; `/board-packs` | Reporting | `rpt.*` |
| `GET /v1/engineering/releases` ; `/changes` (tenant view of release notes) | Engineering governance (P24) | `eng.release:read` |

## L.4 Scope catalogue (excerpt; full list generated from contracts)

| Scope | Data classes returned (max) | Typical grantees |
|---|---|---|
| `core.tenant:read`, `core.entity:read` | INTERNAL | All tenant clients |
| `core.audit:read` | CONFIDENTIAL (masked PII) | Admins, auditors, tenant SIEM |
| `iam.user:read` | PII (business contact) | Admin apps, SCIM |
| `cnt.read` | PUBLIC | Any |
| `cmp.obligation:read`, `cmp.instance:read` | INTERNAL | Tenant integrations, Finbyx (E: `grc.obligation:read`) |
| `cmp.evidence:write` | — | Operating systems (E: `grc.evidence:write`) |
| `wf.task:read`, `cal.event:read` | INTERNAL | Intranets, calendar connectors |
| `dms.document:read` | up to CONFIDENTIAL (per document class) | Approved integrations only |
| `gov.meeting:read` | CONFIDENTIAL | Board portals (approved) |
| `gov.upsi:*` | SEALED | Never to third parties |
| `erm.risk:read`, `ral.ratio:read` | CONFIDENTIAL / FINANCIAL | Group reporting, auditors |
| `ret.run:read` | FINANCIAL | Auditors, Finbyx |
| `grv.case:read` | PII | Tenant CRM with DPO approval |
| `hr.employee:read.minimal` | PII (name, role, department) | Committees, tasks |
| `hr.payroll:*` | HR | Payroll integrations only with DPO approval |
| `grievance.intake:create` | — | Embeds |
| `privacy.request:write` (E) | PII | Ecosystem products |
| `external.workspace:read` (E) | per grant | Named external users |
| `ops.provisioning:ack`, `billing.catalogue:read`, `ops.claims:check` (E, outbound to OH) | INTERNAL | LDC → Ops Hub |
| `xpt.export:create` | per scope | Admin automations (step-up for broad scopes) |

## L.5 Adapter specifications

Each port lists interface essentials, adapters, authentication, residency, data classes and notes. All adapters implement `health()`, region attestation where they store or process tenant data, and cost reporting where usage is billable.

### L.5.1 `LlmProvider`, `OcrProvider`, `TranslationProvider`, `SpeechToTextProvider`, `TextToSpeechProvider`, `EmbeddingProvider`

See Appendix K §K.4 for the `LlmProvider` interface.

| Port | Default adapter | Alternates | Residency rule |
|---|---|---|---|
| LLM | Amazon Bedrock — Claude via India geographic CRIS (ap-south-1 ⇄ ap-south-2) | Anthropic API (global; PUBLIC/INTERNAL only); Jio (stub, OFF) | Regulated classes India-only |
| OCR | Claude vision (Bedrock India) | AWS Textract ap-south-1 [VERIFY handwriting/Indic]; Tesseract (local) | India |
| Translation | Claude (Bedrock India) | Bhashini [VERIFY]; Azure Translator Central India; Google Translation asia-south1 | India |
| STT | Amazon Transcribe ap-south-1 (en-IN, hi-IN) | Bhashini ASR; Azure Speech Central India | India |
| TTS | Amazon Polly ap-south-1 | Bhashini TTS; Azure Central India | India |
| Embeddings | Bedrock embedding model on India route [VERIFY] | Self-hosted model in VPC | India |

### L.5.2 `LmsConnector` / `LosConnector` (third-party lending systems)

- **Interface**: connector SDK (`manifest`, `capabilities`, `healthCheck`, `send`, `receive`, `call`, `reconcile`).
- **Canonical outputs to LDC**: `ControlTestResult` submissions; `portfolio_snapshot` aggregates for ratios (P09) — e.g. outstanding by product/asset classification/DPD bucket, provisions, sanctioned vs disbursed, concentration by counterparty group (pseudonymised), ALM bucket cash flows; `grievance_log`, `recovery_log`, `collection_agency_register` for compliance evidence; record-level data only when the tenant explicitly enables return data prep in LDC (P11) and with the masking rules of Spec §13.2.
- **Reference adapter**: Apache Fineract REST (`/fineract-provider/api/v1/loans`, `/loans/{id}/transactions`, `/glaccounts`, `/journalentries`, `/runreports/{report}`) [VERIFY deployed version events].
- **Fallback**: SFTP/CSV layouts (§L.8).
- **Auth**: tenant-provided API credentials in vault; on-prem agent for internal systems.

### L.5.3 `AccountingSource` — TallyPrime and others

| Item | TallyPrime specification |
|---|---|
| Access | Via `ldc-agent` on the client LAN; TallyPrime in server mode with HTTP listener (default port 9000) bound to localhost or LAN only — never exposed to the internet |
| Protocols | XML (`ENVELOPE/HEADER/BODY`, `TALLYREQUEST` = `Export Data`/`Import Data`); **native JSON from TallyPrime 7.0** (headers `content-type: application/json`, `version: 1`, `tallyrequest: Export\|Import`, `type: Data\|Collection\|Object\|Function`, `subtype`, `id`, optional `id-encoded`, `detailed-response`; body `static_variables` incl. mandatory `svCurrentCompany`, `svExportFormat`); ODBC for collections with `IsODBCTable: Yes` |
| Extract profiles | `TB_PERIOD` (Trial Balance with groups, opening, debit, credit, closing), `BS`, `PL`, `LEDGER_MASTERS` (with parent groups, GSTIN, PAN where set — masked on ingest), `VOUCHERS_PERIOD` (collection `TSPLVoucherColl` or Day Book), `GST_REGISTERS` (sales/purchase with GSTIN, HSN/SAC, tax heads), `STOCK` (where relevant), `COST_CENTRES` |
| Output | `ldc_trial_balance_v1`, `gl_journal_v1`, `ldc_ledger_master_v1`, `ldc_gst_register_v1` with control totals and manifest |
| Write-back | Not supported in LDC (Finbyx owns posting; Spec §10.2) |
| Errors | Company not open, listener disabled, wrong company — explicit messages; Tally runtime log path guidance |

Others: Zoho Books (REST, `zoho.in` data centre, OAuth), SAP S/4HANA (OData) and Business One (Service Layer), generic XLSX/CSV trial balance with mapping wizard; Busy/Marg via exports [VERIFY APIs].

### L.5.4 `CompanyRegistryProvider`, `TaxIdProvider`, `LeiProvider`, `DigiLockerProvider`

| Port | Adapters | Notes |
|---|---|---|
| Company/LLP registry | Licensed aggregators (candidates: Probe42, Signzy, Surepass, Perfios/Karza, HyperVerge, Qorpiq) | Contract + DPA; store minimal fields with attribution; no MCA scraping; directors' PAN/DOB never stored |
| PAN verification | Protean (NSDL) PAN verification service for eligible entities; API Setu where permitted; aggregator | Eligibility [VERIFY]; PAN stored masked + token |
| GSTIN | GSP/aggregator taxpayer search | Multiple GSTINs per PAN |
| LEI | GLEIF public API | Free; parent relationships |
| Udyam | Aggregator [VERIFY] | MSME status |
| DigiLocker | Authorized Partner API (OAuth 2.0 + PKCE; issued documents pull; v1.11 spec) | User consent per pull; Aadhaar never stored |
| Regulator registries | Platform datasets from official public lists (RBI, SEBI, IRDAI, IFSCA, co-op registrars) | Content team refresh; source hash |
| Credit bureaus | **Not used for onboarding** (P18 FR-P18-33) | Tenant may upload its own reports |

### L.5.5 `WorkplaceProvider` (Microsoft 365 first)

| Capability | Microsoft Graph / Entra | Permissions (least privilege) |
|---|---|---|
| SSO | Entra ID OIDC/SAML (enterprise app) | `openid`, `profile`, `email` |
| Provisioning | SCIM from Entra to LDC `/scim/v2` | Entra provisioning service |
| Calendar (per user, delegated) | `/me/calendars`, `/me/events`, change notifications (`/subscriptions`) | `Calendars.ReadWrite` (delegated), `offline_access` |
| Teams meetings | `/me/onlineMeetings` (create), attendance reports, transcripts `/onlineMeetings/{id}/transcripts` | `OnlineMeetings.ReadWrite` (delegated); `OnlineMeetingTranscript.Read.All` per policy [VERIFY consent model] |
| Mail (designated shared mailboxes) | `/users/{shared}/messages` (read), `/sendMail` (send-as) | `Mail.Read` / `Mail.Send` scoped with an application access policy to listed mailboxes |
| Document libraries | `/sites/{id}/drives`, `/drives/{id}/items` | `Sites.Selected` (application) with site-level grant |
| Word for the web | WOPI host or Graph file links for co-authoring where licensed [VERIFY approach] | As above |
| Directory (optional) | `/users`, `/groups` for org sync | `User.Read.All`, `Group.Read.All` (application; admin consent) |

Google Workspace (later): Admin SDK Directory, Calendar API (watch channels), Drive API (shared drives; non-regulated data only), Google Meet REST API for meeting creation/transcripts [VERIFY], Gmail API for designated mailboxes.

### L.5.6 `CalendarProvider` — ICS and CalDAV

- ICS: RFC 5545 `VCALENDAR` with `VEVENT` per item; `UID` = `{ldc_item_id}@lawdocscomply.com`; `SUMMARY` (privacy mode → generic), `DESCRIPTION` with deep link, `DTSTART`/`DTEND` (all-day for deadlines), `VALARM` per user preferences, `CATEGORIES` (DEADLINE, TASK, MEETING, REVIEW, FILING), `X-LDC-KIND`; feed tokens 256-bit, revocable, rotating.
- CalDAV (RFC 4791) read-only collection per user; authentication with app-specific passwords; `REPORT calendar-query` support for date ranges.

### L.5.7 `ESignProvider`

Adapters: Leegality, Digio, SignDesk, Surepass, eMudhra emSigner, LawDocs eSign. Interface: `createEnvelope(doc, signers[{name, email, mobile, order, type: AADHAAR_OTP|AADHAAR_BIO|DSC|ELECTRONIC_OTP}], placement, callbackUrl)`, `getStatus`, `downloadSigned`, `downloadAuditCertificate`, `cancel`, `webhook(raw)`. Rules: IT Act First Schedule exclusions blocked; DSC for MCA forms; signed PDF PAdES-LTV where available; hashes recorded.

### L.5.8 `EmailProvider`, `SmsProvider`, `WhatsAppProvider`, `VoiceProvider`, `ConversationalAgentProvider`

| Port | Adapters | Rules |
|---|---|---|
| Email | Amazon SES ap-south-1; Microsoft 365 send-as; tenant SMTP relay | DKIM/SPF/DMARC verified before use; transactional only |
| SMS | JioCX SMS; other DLT-registered aggregators | Tenant as Principal Entity for its customers; registered headers/templates only; LDC's own registration for platform OTPs |
| WhatsApp | JioCX WhatsApp; other BSPs | Opt-in; templates; per-message pricing (since 1 Jul 2025); INR billing migration by 31 Dec 2026 for India sold-to [VERIFY]; never for debt collection/recovery/legal notices |
| Voice | JioCX Voice; Jio SIP Trunk via CPaaS; Exotel/Plivo/Ozonetel | DND scrub, consent, recording disclosure, number-series rules (1600 for regulated-entity service calls; 140 promotional) [VERIFY current TRAI text]; AI voice behind flag with disclosure |
| Conversational agent | Jio Haptik (WhatsApp/web AI agents) | Flag OFF; intake bots only; hand-off to human; data residency and no-training terms required |

### L.5.9 `PaymentGateway` — Razorpay

Objects: Orders, Payments, Payment Links, Subscriptions (plans, add-ons, upgrades/downgrades via plan change), Invoices (Razorpay invoices not used as tax invoices — LDC issues GST invoices, P20), Refunds, UPI Autopay/e-mandate, Route (OFF). Webhooks consumed: `payment.authorized`, `payment.captured`, `payment.failed`, `order.paid`, `subscription.activated`, `subscription.charged`, `subscription.pending`, `subscription.halted`, `subscription.cancelled`, `subscription.completed`, `refund.processed`, `refund.failed`, `payment_link.paid`, `invoice.paid` [VERIFY current event list]. Verification: `X-Razorpay-Signature` HMAC-SHA256 with the webhook secret; server-side fetch of payment status before marking paid; idempotency by event id. No card data in LDC (NN-16). Ownership note: Spec §6.27 places the group Razorpay account in the Ops Hub (OH8); P20 resolves whether LDC checkout uses the Hub's billing APIs or its own adapter (master note M-S8-02).

### L.5.10 `AcademyProvider` (FinLegal Academy, `trainings.lawdocs.in`)

`listCourses(filters)` → title, slug, category (compliance, DSA/DMA, CISO, KYC/AML, POSH, labour, data protection, board/director programmes), duration, mode, price, CPE/CPD credits if any, certificate type, URL; `createEnrolment(user, course, sponsor_tenant)` with SSO hand-off (OIDC; LTI 1.3 if supported [VERIFY]); `onCompletion(webhook)` → certificate PDF + verification URL + score; xAPI/SCORM statements optional. Completion records feed P13 training records and compliance evidence for training obligations.

### L.5.11 `OdrProvider` (Equator and others)

Per Spec §8.9; LDC uses it from the grievance desk only on complainant choice and tenant configuration; referral package by reference; status events back.

### L.5.12 `GrcThirdParty` and OSCAL

OSCAL v1.2.x JSON (catalog, profile, component-definition, system-security-plan, assessment-results, plan-of-action-and-milestones), JWS-signed. Mapping: LDC instrument → OSCAL `catalog` groups/controls (control id = obligation_ref); tenant applicability → `profile`; operating product controls → `component-definition`; compliance instance results → `assessment-results`; issues → `poam`. Adapters (on request): MetricStream, ServiceNow IRM (staging tables; never core tables), Archer, IBM OpenPages, Komrisk, Komply360, Compfie, TeamLease RegTech, Lawrbit, OnFinance (REST where available, else CSV/OSCAL) [VERIFY APIs].

### L.5.13 `StorageTarget`

See P19 §4D and Spec §12.2.

## L.6 Jio Business services — mapping to LawDocsComply (R-026, R-063)

Status from the Jio Business portal and press coverage, accessed 25 October 2026. Every row is **[VERIFY commercially]**: confirm API availability, India residency, data retention, no-training terms (for AI), SLA and pricing before enabling. Flags default OFF until a contract and certification exist.

| Jio offering (as named on jio.com/business or in announcements) | What it is (public description) | LDC use | Port / flag | For whom |
|---|---|---|---|---|
| JioCX SMS | CPaaS SMS | OTPs (platform), deadline reminders to staff, grievance acknowledgements to complainants (tenant as PE) | `SmsProvider` / `int.sms.provider = jiocx` | Clients and LDC platform |
| JioCX WhatsApp | WhatsApp Business messaging via Jio CPaaS | Opt-in grievance acknowledgements and status; staff digests (internal opt-in) | `WhatsAppProvider` / `int.channels.whatsapp.enabled` | Clients |
| JioCX Voice, JioCX EasyPhone | Programmable voice / cloud business phone | Grievance helpline IVR and call logging; critical deadline call reminders to internal staff | `VoiceProvider` / `int.voice.provider` | Clients; LDC support desk (Ops Hub owns outbound sales/support calling) |
| JioCX RCS | Rich communication services | Rich reminders/notifications (Android) | `RcsProvider` / `int.rcs.enabled = OFF` | Clients |
| JioCX Email | Email delivery | Alternate transactional email route | `EmailProvider` (alternate) | LDC |
| JioCX Alerts, JioCX Verify | Alerts and verification (OTP-style) services | OTP/verification alternate | `SmsProvider`/`OtpProvider` | LDC |
| SIP Trunk, IP Centrex, Toll-Free Service | Enterprise voice | Toll-free grievance number for clients (through a CPaaS/contact centre that terminates on Jio SIP) | `VoiceProvider` via CPaaS | Clients |
| JioMeet | Video conferencing (≤ 1,000 participants) | Candidate meeting platform for Board/committee meetings where clients use it [API VERIFY] | `MeetingProvider` (stub) | Clients |
| Jio Haptik (Reliance-owned) — "AI for All" WhatsApp AI agents (from ₹10,000, usage-based) | Conversational AI agents for customer support | Optional first-line grievance/help intake bot on WhatsApp/web for clients, with human hand-off into P14 | `ConversationalAgentProvider` / `int.agent.haptik.enabled = OFF` | Clients |
| AI + Machine Learning, GPU Accelerated Computing, JioBrain (ML-as-a-service) | AI/ML platform services | Candidate inference host for Vidhi **only** if an enterprise LLM API with India residency and no-training terms is offered | `LlmProvider` stub / `ai.provider.jio.enabled = OFF` | LDC platform |
| Jio AI Call Agent (announced 19 Jun 2026; consumer, consent-based in-call assistant) | Consumer in-call AI | None in v1.0 (consumer product); monitor for enterprise APIs | — | — |
| Microsoft Azure through JioCloud | Azure resale/managed | Contingency hosting/AI route in India regions via Azure (if ever chosen) | — | LDC platform |
| Security: CyberSOC, vCISO, DDoS Mitigation, Threat & Vulnerability Management | Managed security | Candidate managed SOC for LDC (P24 vendor evaluation); marketplace listing for clients' vCISO/SOC needs (P21) | Vendor / marketplace | LDC; clients |
| Marketing Solution | Marketing services | Ops Hub concern (OH7), not LDC | — | Ops Hub |
| JioAttendance (AI contactless attendance) | Attendance | Candidate attendance source for client HRMS (P13) with notice and DPIA (NN-25) | `AttendanceSource` (stub) | Clients |
| Connectivity (ILL, SD-WAN, MPLS), Jio True 5G | Network | None (infrastructure) | — | — |

## L.7 Event mapping — internal ↔ ecosystem

| LDC internal event (`in.lawdocscomply.*`) | Ecosystem event (`in.infrabyx.*`) | Direction | Notes |
|---|---|---|---|
| `cnt.ContentVersionPublished` + `cmp.TenantObligationChanged` | `grc.ObligationPublished.v1` | LDC → products in a GRC link | Per tenant; obligation_ref, change type, dates, applicability |
| `cmp.EvidenceAccepted` | — (internal only) | — | Evidence originating in Finbyx keeps Finbyx `evidence_id` |
| (consumed) | `grc.EvidenceSubmitted.v1`, `grc.ControlTestResultPublished.v1`, `grc.ComplianceIssueRaised.v1`, `grc.PolicyAttested.v1`, `grc.ReturnStatusUpdated.v1`, `grc.SecurityIncidentNotified.v1` | products → LDC | Mapped to `cmp`, `dpc`, `ret` handlers |
| `cmp.IssueRaised` (when action needed in operating product) | `grc.ComplianceIssueRaised.v1` | LDC → product | Severity, owner, due |
| (consumed) | `risk.KriBreached.v1`, `risk.LossEventRecorded.v1`, `risk.CapitalRatioComputed.v1`, `risk.LimitBreached.v1`, `risk.StressTestCompleted.v1`, `risk.RiskSnapshotPublished.v1`, `risk.RiskSignalRaised` | Finbyx/Udofin → LDC | P08/P09 |
| (consumed) | `governance.*`, `workforce.*` (tenant-internal) | Finbyx → LDC | Never forwarded |
| `audit.ExternalAccessProvisioned` | `audit.ExternalAccessGranted.v1` / `Used` / `Revoked` | LDC → RE register | For LDC-hosted slices |
| `xpt.ExportJobStateChanged` (DELIVERED/CONFIRMED) | `portability.ExportRequested.v1`, `portability.ExportCompleted.v1` | LDC → tenant compliance destination; OH (counts) | Signed |
| `xpt.StorageTargetVerified` | `portability.StorageTargetConnected.v1` | LDC → same | — |
| `xpt.BackupCopyConfirmed` | `portability.BackupCompleted.v1` | LDC → same | — |
| `xpt.RestoreTestCompleted` | `portability.RestoreTested.v1` | LDC → same | — |
| `xpt.StorageTargetDegraded` | `grc.ControlTestResultPublished.v1` (control `STORAGE_TARGET_HEALTH`, FAIL) | LDC → tenant compliance destination | — |
| `bil.UsageAggregated` | `billing.UsageRecorded.v1` (`usage_aggregate_v1`) | LDC → OH | Aggregates only |
| `core.ModuleEnabled` / `core.ModuleReadOnly` | `platform.ModuleAttached.v1` / `platform.ModuleDetached.v1` | LDC → OH | Reconciled daily |
| `eng.ReleaseDeployed` | `platform.ReleasePublished.v1` | LDC → OH | Metadata |
| `eng.ControlEvidenceStored` | `platform.ControlEvidenceCollected.v1` | LDC → OH14 | No tenant content |
| `int.ConnectorCertificationPassed` | `platform.ConnectorCertified.v1` | LDC → registry | — |
| `int.ReconciliationBreak` | `platform.ReconciliationBreakRaised.v1` | LDC ↔ counterpart | — |
| (consumed) | `ops.TenantProvisioned.v1`, `billing.PlanChanged.v1`, `billing.EntitlementChanged.v1` (signed) | OH → LDC | Provisioning and entitlements |

[VERIFY exact `domain` segments for platform/billing/ops events against Spec Part 6.16, 6.27, 6.29 when wiring.]

## L.8 LDC-registered file layouts (in addition to Spec §12 layouts)

| Layout id | Use | Key columns (excerpt) |
|---|---|---|
| `ldc_trial_balance_v1` | TB import for ratios, audit, annual report drafts | entity, period_start, period_end, ledger_code, ledger_name, group_path, opening_dr, opening_cr, period_dr, period_cr, closing_dr, closing_cr, currency |
| `ldc_ledger_master_v1` | Ledger mapping | ledger_code, name, parent_group, nature (asset/liability/income/expense), gstin_masked, pan_token |
| `ldc_portfolio_snapshot_v1` | Ratio and risk inputs from non-Finbyx LMS | as_of, product, asset_classification (SMA-0/1/2, NPA sub-standard/doubtful/loss), dpd_bucket, count, principal_os, interest_receivable, provision, security_value_band, sector, state |
| `ldc_alm_buckets_v1` | Structural liquidity | as_of, bucket (per RBI SLS buckets), inflows by type, outflows by type, currency |
| `ldc_concentration_v1` | Concentration (pseudonymised) | as_of, counterparty_ref (HMAC), group_ref, exposure_funded, exposure_nonfunded, tier1_pct |
| `ldc_investment_book_v1` | NBFC-ICC/investment entities | as_of, instrument_type (equity, AIF units, REIT/InvIT units, MF units, bonds, G-sec), isin, issuer_group_ref, quantity, cost, fair_value, valuation_level, classification (AC/FVOCI/FVTPL or HTM/AFS/HFT), listed_flag |
| `ldc_grievance_log_v1` | Grievance evidence from external systems | case_ref, received_at, channel, category, status, resolved_at, tat_days, escalation_level |
| `ldc_recovery_log_v1` | Recovery/collection conduct evidence | case_ref, agency_ref, contact_at, mode, within_permitted_hours (bool), notice_sent_at |
| `ldc_gst_register_v1` | GST data prep | doc_type, doc_no, doc_date, counterparty_gstin, place_of_supply, hsn_sac, taxable_value, igst, cgst, sgst, cess, reverse_charge |
| `ldc_employee_minimal_v1` | HR minimal sync for tasks/committees | employee_ref, display_name, email, department_id, position, manager_ref, status |
| `ldc_question_sheet_v1` | Excel question import (exact template; Appendix E) | Columns A–AD as template |

All layouts: UTF-8 with BOM CSV or XLSX; manifest with counts, control totals, SHA-256, detached JWS (Spec §3.11).

## L.9 Rate-limit profiles (seed; G tier)

| Client type | Read | Write | Bulk/export | Notes |
|---|---|---|---|---|
| Ecosystem service | 600 req/min per tenant | 300 req/min | separate bucket | Regulated commands never share buckets with bulk reads (Spec §3.10) |
| Certified connector | 300/min per tenant | 120/min | 10 concurrent jobs | — |
| Tenant integration | 120/min | 60/min | 5 concurrent jobs | Raise on request |
| Delegated user app | 60/min per user | 30/min per user | — | — |
| Embed (publishable key) | 30/min per IP | 10 submissions/hour per IP | — | Bot protection, OTP for status |
| Public (pricing, marketplace, health check) | 60/min per IP | health-check 3 sessions/hour per IP | — | CAPTCHA after thresholds |

Headers follow the IETF RateLimit header fields draft [VERIFY final names]; `429` with `Retry-After`.

## L.10 Open items

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-L-01 | JioCX API documentation, BSP status for WhatsApp, Haptik data terms | Procurement | Alternate CPaaS/BSP |
| OI-L-02 | Exact ecosystem `domain` names for platform/billing/ops events | Integration lead | Use Spec Part 6 table names at wiring |
| OI-L-03 | Microsoft Teams transcript permissions and consent model per tenant policy | CTO | Manual transcript upload |
| OI-L-04 | Razorpay current webhook event list and Subscriptions upgrade/downgrade semantics | P20 lead | Order-based billing |
| OI-L-05 | Fineract version and external events available at client sites | Integrations | REST polling |
| OI-L-06 | Aggregator data-display rights (company data) | Counsel | Manual entry |

## L.11 Sources

Ecosystem Integration Specification v1.1 (Parts 3, 4.5, 6, 9, 10, 12, 13); Jio Business portal (https://www.jio.com/business/, accessed 25 Oct 2026) and voice page; Business Today (Jio Call Agent, 19 Jun 2026); UNI India (Haptik AI for All); Tally Solutions developer help (TallyPrime server, JSON integration); DigiLocker Authorized Partner API Specification v1.11; Microsoft Graph documentation (calendar, onlineMeetings, transcripts, `Sites.Selected`); Meta WhatsApp Business Platform pricing (accessed 25 Oct 2026); Razorpay API and webhooks documentation (razorpay.com/docs) [VERIFY]; NIST OSCAL 1.2; GLEIF API; RFC 5545, 4791, 9457, 9421, 7643/7644.

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular X-01, X-03, X-04, X-07, X-23, X-41. Where text above conflicts with them, the master prevails.
