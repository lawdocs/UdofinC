# Phase P18 — Integration Gateway, Ecosystem Connectors and Developer Platform

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (outbox, audit ledger, tenancy, KMS, Temporal), P01 (identity, SSO, SCIM, service accounts, step-up), P02 (settings registry, mapping-pack overrides), P04 (tasks, calendar, notifications — consumers of calendar and messaging connectors), P07 (DMS — consumer of storage and eSign connectors). Commit the **Infrabyx Ecosystem Integration Specification v1.1** unchanged as `docs/ecosystem/infrabyx-integration-spec.md` (SHA-256 checked in CI; Spec §0 instruction 1) and the `infrabyx-contracts` registry client.
>
> **Sequencing:** Gateway, auth, error model, idempotency and outbox/webhook delivery ship in sprints 1–3 (every later phase publishes and consumes through them). Ecosystem connectors (Finbyx, Udofin, Ops Hub) in sprints 3–6; identity/KYB onboarding adapters in sprint 2 (needed by P01 self-onboarding and P23 health check); workplace/calendar connectors in sprints 4–6; communications and embeds in sprints 6–8; developer portal and certification in sprints 8–10. P19 (portability and storage targets) builds on the storage connector framework delivered here.
>
> **Binding appendices:** L (adapter specifications and REST/API catalogue), B (data model, event and error registers), Q (security), U (settings), M (export formats where connectors exchange files). Ecosystem Spec v1.1 prevails over this file for any cross-product contract (NN-23).
>
> **Requirements covered:** R-002, R-029, R-043 (integration parts), R-047 (group grants), R-049 and R-052 (data intake from Finbyx/Udofin/LMS), R-050 (Tally/Excel intake transport; transformation in P11), R-053, R-057 (federated external access), R-058, R-063 (Jio channels), R-082, R-094, R-098.
>
> **Estimated effort:** 10 two-week sprints, squad of 8 (gateway and platform 3, ecosystem connectors 2, third-party adapters 2, developer experience 1). *(v1.1: +4 sprints for v1.1 scope (MCP server/client, A2A, cell routing, new ports and connectors) — 14 in total)*


> **v1.3 changes (26 October 2026)** *(v1.3; IPB-01 ports, IPB-10 API and event standard — D-60, X-71)*
> - New §4Y **IPB port catalogue, connector marketplace and Ecosystem events**: every LDC port is named with its IPB-01 equivalent and its two adapters (FR-P18-113); the connector catalogue of §4M becomes the IPB-10 connector marketplace with the manifest schema, permission preview and install flow (FR-P18-114); the ten IPB-10 proposed Ecosystem events plus the IPB-05 policy events and the IPB-07 glossary event are listed with LDC's role and payload minima and registered in Ecosystem Spec v1.2 (FR-P18-115); `/v1` conventions, RFC 9457 problem details, Standard Webhooks headers and the `ldck_` key prefix confirmed (FR-P18-116); MCP exposure rules (FR-P18-117); `LAW_REGISTER_PORT` provider role (FR-P18-118).
> - Errors LDC-INT-207–210; tests P18-AT-v13-01–04; open items OI-P18-32–OI-P18-34.

> **v1.2 changes (25 October 2026)**
> - New §4W API-first onboarding and KYB adapters: ports `COMPANY_DATA_PORT`, `IDENTITY_PORT`, `GSTIN_PORT`, `LEI_PORT`, `REGISTER_LOOKUP_PORT`, `ESIGN_PORT` (renaming the v1.0 provider interfaces), normalised schema `ldc.onboarding.entity.v1`, waterfall with hedging and circuit breakers, cost and provider-quality scoring, official-register snapshot ingestion, partner and bulk onboarding endpoints (FR-P18-100 to FR-P18-103; D-56; consumed by P01 §4H)
> - New §4X public API, webhooks and MCP by business ID: `GET /v1/compliances/{compId}`, instances by period, `/v1/risks/{riskId}`, `/v1/kris/{kriId}`, `/v1/controls/{ctlId}`, `/v1/gov/{govId}`, `/v1/history/{bizId}`, stars, conversations and accountability by ID, list and export API, ID-keyed webhooks, CloudEvents extension `ldcbizid`, MCP tools `find_by_id`, `get_compliance`, `get_history`, `get_risk`, `get_governance_item`, `list_urgent`, `list_my_starred`, `draft_conversation_message`, `star_item`; enumeration protection; replies from Teams, e-mail and messaging (FR-P18-104 to FR-P18-112; D-51, D-53, NN-56, NN-57)
> - New screens SCR-INT-28 to SCR-INT-30; tables, settings, events, error codes LDC-INT-160 to LDC-INT-167, Gherkin and open items OI-P18-28 to OI-P18-31

**v1.1 changes (25 October 2026)** *(v1.1)*

- New §4P **LDC MCP server** (`ldc-mcp`) and §4Q **MCP client registry** implementing Appendix AA §AA.7–§AA.8, D-35 and NN-52 (FR-P18-62–FR-P18-71).
- New §4R **A2A gateway** for agent tasks with Finbyx, Udofin, Equator and the Ops Hub — behind a flag until the Ecosystem Spec v1.2 change request is approved (FR-P18-72–FR-P18-76).
- New §4S **multi-region cell routing** for APIs, webhooks, connectors and events (NN-24 as amended; Appendix Y §Y.7) (FR-P18-77–FR-P18-81).
- New §4T ports `REG_INTEL_PORT` (licensed regulatory intelligence) and `FX_RATE_PORT` (reference rates) (FR-P18-82–FR-P18-85).
- New §4U connectors for the v1.1 modules: litigation/court data and notices (P26), contract repositories and CLM (P26), ESG and emissions data (P27), foreign company registries (P25) (FR-P18-86–FR-P18-92).
- New §4V improvements from the feedback backlog: connector health alerts (IMP-130), public OpenAPI + MCP (IMP-131), Admin API (IMP-132), ITSM/Jira issue sync (IMP-133), no mandatory endpoint agent (IMP-134), import undo (NN-49) (FR-P18-93–FR-P18-99).
- Error fixed (G5 E-01): litigation, hearing and order events now route to the legal-matter register `lit.matters` built in P26 (D-41) instead of an unowned register.
- Partner roles use the lead's names (`prt_admin`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`); new screens, settings, events, error codes, acceptance scenarios and open items added in §6, §9, §7.4, §12 and §14.

---

## 1. Objective and business outcome

LawDocsComply must connect to the rest of the Infrabyx ecosystem (Finbyx, Udofin, Equator, LawDocs, the Infrabyx Operations Hub, FinLegal Academy) and to the systems its customers already run (third-party LOS/LMS/LSP and recovery systems, Tally and other accounting packages, Microsoft 365 or Google Workspace, their websites and apps, eSign providers, messaging and calling providers) **without redesign** each time a new counterparty appears. The answer is one integration gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK, mapping packs and a file fallback — and an onboarding path that lets a new company, a group company or a channel partner connect in days, not projects.

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | LDC passes the Ecosystem Spec §14.3 certification suite groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, External and group access, Risk feed, Archive and storage — and emits `ConnectorCertified` for the Finbyx↔LDC, Udofin↔LDC and Ops Hub↔LDC connectors in sandbox |
| Compliance-mode switch works both ways | A Finbyx tenant can move from `EMBEDDED` to `LDC_EXTERNAL` (and back) with obligations, controls, open issues and the evidence index carried over (hash-chain heads reconciled), dual-publishing for one compliance period, zero lost records (Ecosystem Spec §9.1) |
| New counterparty without code in the core | A certified third-party LMS connector (Apache Fineract reference adapter) and a generic CSV/SFTP layout are onboarded by mapping pack only; a fictitious "Lender X LOS" is connected in ≤ 5 working days in the sandbox with no change to `cmp`, `erm`, `ral` or `ret` code |
| Self-service onboarding data | A prospect entering a PAN or CIN in the health check (P23) or onboarding wizard (P01) gets name, constitution, registration date, registered address, status, directors (for companies/LLPs), GSTINs and LEI pre-filled from licensed sources in ≤ 5 s p95, with consent captured and source attribution shown |
| Calendars everywhere | Tasks and deadlines appear in Microsoft 365, Google Calendar, Outlook.com, Gmail and Apple Calendar (through native sync or ICS/CalDAV), role-scoped, within 5 minutes of a change, with reminders reaching the user's phone through their own calendar app |
| Website and app embeds | A client NBFC puts a "Grievance Redressal" button on its website or app (script tag, hosted page or API) in ≤ 1 hour; complaints land in its P14 grievance desk with acknowledgement in seconds |
| Developer platform | Public developer portal with OpenAPI 3.1 and AsyncAPI 3.0 references, sandbox tenants with synthetic data, client self-registration with tenant-admin approval, SDKs (TypeScript, Python, Java), Postman collection, status page and changelog |
| Safe by default | Every inbound and outbound call authenticated, scoped, rate-limited and logged; personal data never leaves India through a connector unless a recorded basis exists; regulator portals handled as `PORTAL_MANUAL` only (no credentials, OTPs, cookies, RPA or scraping) |

---

## 2. Scope (in / out)

**In scope**

- `int` module: API gateway configuration (edge), contract registry client, OAuth 2.x authorisation server profile for machine clients (Keycloak), client registry, scopes, consent records, rate limits, webhook subscriptions and delivery, event catalogue, outbox relay, inbox de-duplication, DLQ and replay, connector runtime (SDK host), mapping-pack runtime, integration monitor, on-premises agent management, developer portal, sandbox provisioning, connector certification.
- **Ecosystem connectors**: Finbyx (all LDC-relevant domains in Ecosystem Spec §§6.15, 6.18–6.23, 6.26, 9), Udofin (LSP-side GRC, grievance, DLG disclosures, risk metrics for RE-scoped KRIs), Equator (grievance → ADR opt-in referral, litigation/ADR status for the compliance register), LawDocs (templates, eSign envelopes, advisory requests, public professional directory references), Infrabyx Operations Hub (provisioning acknowledgement, catalogue read, claims gate, usage aggregates, support-ticket hand-off metadata), FinLegal Academy (`trainings.lawdocs.in` LMS — catalogue, enrolment, completion, certificates).
- **Third-party lending and recovery systems**: LOS/LMS/LSP/recovery/collections connectors through the connector SDK; inbound generic GRC connector contract (Spec §9.2); OSCAL export/import (Spec §9.4); CSV/XLSX/SFTP registered layouts (Spec §3.11, §12).
- **Accounting sources** (transport only; transformation is P11): TallyPrime (XML/JSON over the on-premises agent), Zoho Books, SAP Business One/S/4HANA (OData), Busy and Marg via export files [VERIFY APIs], generic trial-balance CSV/XLSX.
- **Identity, KYB and registry adapters** for onboarding: PAN verification, company/LLP master (licensed aggregators), GSTIN, LEI (GLEIF), Udyam, DigiLocker (consented document pull), Aadhaar-based eSign through ESPs (no Aadhaar storage), regulator public registers (RBI NBFC/ARC/UCB lists, SEBI intermediary lists, IRDAI, IFSCA, co-operative registrars) as downloaded datasets for verification.
- **Workplace**: Microsoft 365 (Entra ID SSO/SCIM, Graph calendar, Teams meetings and transcripts, Outlook mail send/receive for designated mailboxes, OneDrive/SharePoint document libraries, Word for the web opening), Google Workspace (later; same port), personal calendars via ICS subscription and CalDAV (Apple iCloud), Outlook.com and Gmail via ICS or OAuth calendar APIs.
- **eSign and stamping** adapters (Leegality, Digio, SignDesk, Surepass, eMudhra; DSC desktop signer; e-stamp through ESP partners).
- **Communications**: email (Amazon SES ap-south-1 / customer SMTP relay / Microsoft 365 send-as), SMS (DLT-registered; JioCX SMS and other aggregators), WhatsApp Business Platform (JioCX WhatsApp or another BSP), voice (JioCX Voice, Jio SIP Trunk through a CPaaS, Exotel/Plivo as alternates), RCS (JioCX RCS, flag), web push, in-app; Haptik conversational agents as an optional channel for client customer-support intake (flag).
- **Embeds**: grievance and help-desk widgets, public policy disclosure pages, complaint status tracker, JavaScript SDK and mobile deep links; client website/app/LMS/LOS/LSP integration APIs (R-098).
- **Tenant onboarding by API** for group companies, Finbyx/Udofin cross-sell, channel partners and enterprise groups (R-002).

**Out of scope**

- Business logic of the modules that consume connectors (P04 calendars and notifications, P07 DMS, P11 return transformation, P13 HRMS, P14 grievance, P19 export and storage targets, P20 billing — although the Razorpay adapter lives in `int` and is used by P20).
- Filing to regulator portals by machine (D-13; Spec §10.2 `PORTAL_MANUAL`). The gateway contains **no** HTTP client configured for RBI, SEBI, IFSCA, IRDAI, MCA, GSTN, CERSAI, CKYCR or income-tax portal domains (certification test "Filing boundaries", Spec §14.3).
- Credit-bureau pulls for onboarding (see FR-P18-33 — LDC is not a specified user under CICRA 2005 for a SaaS sign-up purpose).
- Accessing borrower, member or loan-level personal data from Finbyx/Udofin beyond the Ecosystem Spec projections (risk feed is pseudonymised and aggregated; Spec §6.22).

---

## 3. Personas and permissions touched

| Role / principal | P18 permissions |
|---|---|
| `ten_admin` | Connect/disconnect connectors for the tenant, approve API clients, manage webhook subscriptions, view integration health, approve DLQ replays (maker ≠ checker: replay requested by one admin, approved by another or by `ten_cco`/CISO), manage SSO/SCIM, approve storage and calendar connections, install the on-premises agent |
| `ten_kmp` (CISO, CTO/CIO) | Same as admin for security-relevant connectors; mandatory approver for connectors that move CONFIDENTIAL or higher data out of LDC |
| `ten_cco` | Approves compliance-mode switches (`re_grc_link`), approves external-access federation, is the default maker for external-access grants received from Finbyx (Spec §4.7) |
| Every tenant user | Connects their **own** calendar (personal sync) and personal Microsoft/Google account for calendar only; cannot connect tenant-wide connectors |
| Tenant developers (permission `int.client:manage` delegated by admin) | Register API clients in sandbox; production clients need admin approval |
| `plt_super_admin` | Platform connector catalogue, platform-level connector credentials (e.g. aggregator contracts), kill switches; Governed changes only |
| `plt_support` | Integration monitor read (metadata only), assist tenants via break-glass (NN-30) |
| `plt_security_officer` | Connector security reviews, certification sign-off, key rotation oversight |
| External ecosystem service accounts | `svc_finbyx_<env>`, `svc_udofin_<env>`, `svc_ops_hub_<env>`, `svc_equator_<env>`, `svc_lawdocs_<env>`, `svc_academy_<env>` — OAuth clients bound to `re_grc_link`/links, scopes per Spec §4.5 |
| Third-party connector clients | `ext_<connector-id>` — certified connectors with tenant consent |

Proposed additions to the role catalogue (master notes): tenant permission set `ten_integration_admin` (delegable subset of `ten_admin`) and external `ext_developer` (developer-portal account, no tenant data).

---

## 4. Functional requirements

### 4A. API gateway and contract discipline

**FR-P18-01 — One gateway per environment.** All machine traffic (ecosystem, third-party, tenant scripts, mobile/web embeds) enters through the LDC gateway (AWS API Gateway or an Envoy/Kong layer behind AWS ALB in ap-south-1; WAF; TLS 1.3; HSTS). The gateway enforces: authentication, audience and scope checks, tenant resolution, schema validation against the registered OpenAPI document, request size limits, rate limits, idempotency-key presence on state-changing calls, mTLS for ecosystem and certified connectors, IP allow-lists where configured, and request/response logging **without** bodies or personal data (NN-32). Browser traffic for `apps/web` uses the BFF pattern (same-origin session cookies; no tokens in browser storage); public embeds use a separate hostname (`embed.lawdocscomply.com`) with its own CSP.

**FR-P18-02 — Contract-first.** Every API is defined in OpenAPI 3.1 and every event in AsyncAPI 3.0 with JSON Schema 2020-12 payloads in the `infrabyx-contracts` registry (ecosystem-facing) or the LDC contracts package `packages/contracts` (tenant/third-party-facing). Code is generated from contracts (Zod/TypeScript types, NestJS DTOs, SDKs). CI blocks merges that change an API without a contract change, or that make a backward-incompatible change within a major (Spec §3.3, §14.1). Pact consumer-driven tests gate deployments for every ecosystem counterpart (`contracts.lock`).

**FR-P18-03 — Conventions.** Paths `/v1/...` plural nouns with action sub-resources (`/v1/obligations/{id}/attest`); `snake_case` fields; `UPPER_SNAKE_CASE` enums with `x-extensible-enum`; identifiers prefix + ULID (`obl_`, `cmi_`, `evd_`, `pol_`, `mtg_`, `rsk_`, `aud_`, `ret_`, `grv_`, `doc_`); cursor pagination (`limit` ≤ 500, `cursor`); `updated_since` on every list for reconciliation; `fields` sparse fieldsets; `expand` for related objects (max depth 2); RFC 3339 timestamps with offset (IST default in UI, UTC in storage); money `{ "amount": "125000.00", "currency": "INR" }`; ETags and `If-Match` for optimistic concurrency on PATCH.

**FR-P18-04 — Error model.** RFC 9457 problem details with the Ecosystem Spec §3.9 code set plus LDC codes `LDC-INT-001…` (Appendix B). `detail` never contains personal data. `regulatory-guard` problems name the rule and citation. `entitlement-missing` is never raised for a regulated tenant reading or exporting its own data (Spec §3.9; NN-10).

**FR-P18-05 — Idempotency.** `Idempotency-Key` (UUIDv7) mandatory on POST/PATCH/DELETE from machine clients; stored with request hash and response for 24 hours (7 days for billing and money-adjacent calls); same key with a different body → 422 `idempotency-key-reuse`; concurrent retry while processing → 409 `request-in-progress` (Spec §3.4). Business keys (Spec Part 6) are unique constraints at the consumer.

**FR-P18-06 — Versioning and deprecation.** Major versions in the path; a new major runs in parallel ≥ 90 days (ecosystem) or ≥ 12 months (public third-party API, G tier) with `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers and developer-portal notices; usage of deprecated endpoints is reported to each client's owner monthly. Event schemas are BACKWARD-compatible within a major.

### 4B. Machine authentication and authorisation

**FR-P18-07 — Client types.**
1. **Ecosystem service clients** — OAuth 2.0 client credentials profiled to OAuth 2.1/RFC 9700, certificate-bound (RFC 8705) with Infrabyx Ecosystem PKI, tokens ≤ 10 minutes, audience-restricted, one client per (product, counterparty, environment, purpose); RFC 9421 HTTP message signatures (`ed25519`) on every request and webhook, covering `@method`, `@target-uri`, `content-digest` (RFC 9530), `content-type`, `idempotency-key` (Spec §3.6).
2. **Certified third-party connectors** — client credentials with `private_key_jwt` (RFC 7523) or mTLS; tenant consent record required per tenant (`int.client_tenant_consents`).
3. **Tenant integration clients** (a client's own scripts, its LMS, its website backend) — client credentials with `private_key_jwt`; client secrets permitted only in sandbox; secrets/keys rotate ≤ 90 days with overlap; owner, purpose, scopes, expiry mandatory.
4. **Delegated user access for partner apps** (e.g. a client's intranet showing "my compliance tasks") — authorisation code + PKCE + PAR (RFC 9126), DPoP (RFC 9449) for public clients, consent screen listing scopes; refresh tokens rotated; FAPI 2.0 Security Profile for any client that can act on obligations or evidence.
5. **Embed keys** (public, for widgets) — publishable keys bound to allowed origins, limited to `grievance.intake:create`, `help.article:read` and status-lookup with complainant OTP; never read tenant data.

**FR-P18-08 — Scopes.** Format `[domain].[resource]:[action]` (Spec §4.5). LDC publishes the scope catalogue (Appendix L §L.4) including ecosystem scopes it serves (`grc.obligation:read`, `grc.evidence:write`, `grc.kri:read`, `privacy.request:write`, `external.workspace:read`, `external.grant:write`) and LDC scopes (`cmp.instance:read`, `cmp.evidence:write`, `wf.task:read`, `wf.task:write`, `cal.feed:read`, `dms.document:read`, `dms.document:write`, `gov.meeting:read`, `pol.policy:read`, `erm.risk:read`, `ral.result:read`, `aud.finding:read`, `ret.package:read`, `grv.case:create`, `grv.case:read`, `hr.employee:read.minimal`, `int.webhook:manage`, `xpt.export:create`, `bil.usage:read`). Every scope declares the data classes it can return; a client whose `data_class_max` is below a response field's class receives that field masked or omitted (field-level filtering in the BFF/gateway service layer).

**FR-P18-09 — Authorisation is server-side and contextual.** Gateway scopes are necessary but not sufficient: every request is evaluated by the policy engine (Cerbos/OPA) with tenant, legal entity, department, record sensitivity, link status (`re_grc_link`, `re_lsp_link`, `tenant_link`, `group_grant`, `external_access_grant`) and consent. An expired link disables the client's access for that tenant within 60 seconds.

**FR-P18-10 — Consent and legal basis on personal data.** Every inbound or outbound message carrying personal data must carry `consentref` or `legalbasis` (Spec §3.2); the gateway rejects messages without one (`consent-missing`). LDC records its role per purpose (processor for the tenant in most flows; fiduciary for its own customer-account and marketing data) in the P12 ROPA.

### 4C. Events, webhooks and the outbox

**FR-P18-11 — Outbox and relay.** Every module writes domain events to the transactional outbox in the same database transaction as the state change (P00). The relay publishes to: (a) internal subscribers (Temporal signals, module handlers), (b) ecosystem counterparts via Standard Webhooks HTTP push or the shared streaming bus (MSK/Redpanda on the Infrabyx AWS ap-south-1 estate, CloudEvents Kafka binding, one topic per domain per producer) where both sides are on it, (c) tenant webhook subscriptions. Outbox lag p95 ≤ 30 s; delivery p95 ≤ 5 min (Spec §3.8).

**FR-P18-12 — Event type naming (resolves a convention conflict).** Ecosystem-facing events use the Ecosystem Spec names and types exactly: `type = in.infrabyx.[domain].[EventName].v[major]` (e.g. `in.infrabyx.grc.ObligationPublished.v1`, `in.infrabyx.risk.KriBreached.v1`, `in.infrabyx.portability.ExportCompleted.v1`), `source = urn:infrabyx:ldc:[tenantid]`. LDC-internal and tenant-webhook events use `in.lawdocscomply.[module].[EventName].v[major]` (conventions §8). A mapping table (`int.event_type_map`) relates internal events to ecosystem events; an internal event is never published to the ecosystem under the LDC namespace. *(Master note M-S8-01.)*

**FR-P18-13 — CloudEvents envelope.** All events (internal included) carry the CloudEvents 1.0.2 attributes and Ecosystem Spec extensions: `id` (UUIDv7), `source`, `type`, `subject` (aggregate id, partition key), `time`, `dataschema`, `tenantid`, `reid` (or `none`), `productfamily` (`na` for LDC events), `correlationid`, `causationid`, `consentref`/`legalbasis` when personal data is present, `dataclass`, `schemaver`, `seq` (per subject), `traceparent`. Risk-feed consumption validates `asof`, `metricversion`, `citation`, `contenthash`, `prevhash` and the per-producer hash chain (Spec §6.22).

**FR-P18-14 — Inbox and ordering.** Consumers persist `(source, id)` and the business key before processing (exactly-once effect); order per `subject` by `seq`; gaps parked 15 minutes, then a catch-up via the producer's `GET /v1/events?after=&types=`; unresolved gaps raise `ReconciliationBreakRaised` and an integration incident (Spec §3.5). LDC also serves `GET /v1/events?after=&types=` for its own produced events with ≥ 90 days replay retention.

**FR-P18-15 — Tenant webhooks.** Tenants subscribe endpoints to LDC events from the published catalogue (e.g. `ObligationDueSoon`, `ComplianceInstanceStatusChanged`, `EvidenceRejected`, `UpdatePublished`, `TaskAssigned`, `GrievanceRaised`, `GrievanceClosed`, `PolicyApproved`, `MeetingScheduled`, `ExportCompleted`). Delivery: Standard Webhooks (`webhook-id`, `webhook-timestamp`, `webhook-signature` HMAC-SHA256 over `id.timestamp.body` with a `whsec_` secret, rotating with overlap), at-least-once, exponential back-off with jitter for 72 hours, then DLQ with alert; endpoint must be HTTPS with a valid public certificate; private IP ranges blocked (SSRF defence); payload data class capped by the subscription's approved `data_class_max` (default `INTERNAL`: ids, statuses, dates, no personal data — consumer fetches details via API with its own scopes). A "Send test event" button and a delivery log (last 30 days, metadata only) are provided.

**FR-P18-16 — DLQ replay under maker-checker.** Replays of DLQ messages (ecosystem or tenant webhooks) are requested by one authorised user and approved by another (NN-05), with the replay window and filters shown; replay is idempotent at the consumer by `(source, id)`.

### 4D. Ecosystem connectors

**FR-P18-17 — Compliance-mode link (`re_grc_link`).** LDC implements its side of Spec §9.1: a Finbyx (or Udofin) tenant linked to an LDC tenant in mode `LDC_EXTERNAL` or `LDC_GROUP`. Link creation is initiated by either side, approved by the RE's CCO (maker) and CISO or MD/CEO delegate (checker) in LDC, and by the counterpart in its product; the link records reid, legal entities covered, effective date, data scopes, and a switch plan. A mode switch: the outgoing system exports obligations, controls, open issues and the evidence index with hash-chain heads; LDC imports before the effective date; producers dual-publish for one compliance period; reconciliation report signed by both CCO views. A switch never loses data.

**FR-P18-18 — Finbyx → LDC (inbound) — minimum set.**

| Domain (Spec §) | Events / APIs consumed by LDC | LDC handling |
|---|---|---|
| `grc` (6.15) | `ControlTestResultPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `PolicyAttested`, `SecurityIncidentNotified`, `ReturnStatusUpdated` | Evidence attached to compliance instances by `obligation_ref` (P04); issues into the issue register (P04/P10); incidents into P12 incident register with clocks; return status into P11 Return Studio calendar |
| `reporting` (6.18) | Return definitions metadata, `return_run` packages (`return_package_v1`), `ReturnApproved`, `ReturnFiled` | D-05: LDC consumes Finbyx runs instead of recomputing; evidence of filing linked to the return obligation |
| `bureau` (6.19) | `bureau_cycle` status, `BureauFileSubmitted`, rejection/DQI summaries | Compliance with CIC reporting timelines tracked (P11) |
| `finance` (6.20) | `FinancialStatementsApproved`, trial-balance snapshot references, `PeriodClosed` | Ratio engine inputs (P09) by reference; audit module (P10) |
| `audit` (6.21) | `ExternalAccessGranted`/`Used`/`Revoked`, `POST /v1/external-access/grants` (federation) | LDC provisions the same grant locally for the RE's compliance records (Spec §4.7) |
| `risk` (6.22) | `KriBreached`, `LossEventRecorded`, `CapitalRatioComputed`, `LimitBreached`, `StressTestCompleted`, `RiskSnapshotPublished`, `RiskSignalRaised` | ERM register, CRO dashboards, ICAAP (P08/P09); LDC never sends formula logic back; LDC serves `GET /v1/grc/kris?updated_since=` and `GET /v1/grc/obligations?updated_since=` |
| `governance`, `workforce` (6.23) | `BoardMeetingScheduled`, `ResolutionPassed`, `KmpChanged`, `TaskAssigned`, `EmployeeOnboarded`, `EmployeeOffboarded`, `MailboxProvisioned`, `AccessReviewCompleted` (TENANT scope) | Governance registers (P06), HR minimal projection (P13) for task assignment and committee membership; tenant-internal routing rules enforced (never forwarded to OH) |
| `members` (6.24) | Society governance counts and events relevant to compliance | P16 co-operative suite |
| `investments` (6.25) | `InvestmentLimitBreached` (always with `LimitBreached`), aggregates | P09/P15 investment-entity checks |
| `portability` (6.26) | `ExportRequested`, `ExportCompleted`, `BackupCompleted`, `RestoreTested`, `StorageTargetConnected` | Compliance evidence for BCP/data-retention obligations (P19) |
| `litigation`, `recovery`, `adr` (6.8–6.10) | `LitigationCaseOpened/Updated/Closed`, `HearingScheduled`, `OrderRecorded`, `RecoveryCaseOpened/Closed`, ADR status | Legal-matter register `lit.matters` built in **P26** (D-41): case/hearing/order records, directions with due dates → tasks; LDC owns legal matters, the Finbyx Recovery Suite/Udolex owns lender debt recovery *(v1.1, G5 E-01)* |
| `grievance` (6.12) | `GrievanceRaised`, `OmbudsmanReferralRecorded`, `GrievanceRated` (aggregates) | When LDC is the grievance host for the tenant (P14) |
| `dlg` (6.11) | `DLGDisclosurePublished` | Compliance evidence for DLG disclosure obligations |

**FR-P18-19 — LDC → Finbyx/Udofin (outbound).** `ObligationPublished` (change feed of obligations applicable to the tenant, with `obligation_ref`, change type, dates, applicability), KRI definitions and approved thresholds (pull API; threshold versions carry LDC approval reference), `PolicyApproved`/policy versions metadata for attestation flows, external-access grant status responses, `ComplianceIssueRaised` (when an LDC finding requires action in the operating product), privacy requests `privacy.request:write` (DPDP data-principal requests the tenant routes to the operating product). LDC sends no personal data to Finbyx/Udofin except where the tenant's own records require it and a legal basis is recorded.

**FR-P18-20 — Udofin.** As LSP, Udofin's own LDC tenant (and the RE's slice under Udofin RA1/RA2) consumes the same `grc` and `risk` contracts for RE-scoped KRIs and LSP metrics (Udofin never computes RE prudential ratios). Grievance intake from Udofin's borrower app may route to the RE's LDC grievance desk where the RE chooses LDC as grievance host (Spec §6.12). Wellness data is never accepted (gateway rejects `WELLNESS`).

**FR-P18-21 — Equator.** LDC's grievance desk (P14) offers, only on explicit complainant choice and the tenant's configuration, a referral to Equator (or another ODR provider through `OdrProvider`, Spec §8.9) for mediation/conciliation/arbitration; LDC sends a minimal referral package by reference (document ids, hashes) after consent; Equator's case status returns as ADR events for the legal-matter register. LDC never receives hearing content, neutral selection logs or other parties' documents. The Equator neutrality wall applies to any shared staff identity (Spec §4.6).

**FR-P18-22 — LawDocs, Operations Hub and FinLegal Academy.**
- **LawDocs** (`lawdocs.in`): template and clause packs (model agreements, policy templates) imported as versioned packs into P07; eSign envelopes can be created through LawDocs' eSign service where the tenant prefers it (adapter, same `ESignProvider` port); advisory/service requests created from LDC open a marketplace order (P21) — LawDocs is a provider, not a data store for tenant compliance records.
- **Infrabyx Operations Hub** (Spec §4.6, §6.27, §6.29): LDC consumes `TenantProvisioned`, `PlanChanged`, `EntitlementChanged` (signed) and serves provisioning-status and entitlement APIs; LDC calls the Hub only with scopes `ops.provisioning:ack`, `billing.catalogue:read`, `ops.claims:check` (Spec §4.5 row for LDC) and emits `UsageRecorded` aggregates (`usage_aggregate_v1`), `ModuleAttached`/`ModuleDetached`, `ReleasePublished`, `ControlEvidenceCollected`, copies of `SecurityIncidentNotified` without personal data, `AccessReviewCompleted` (PLATFORM scope), and portability/external-access **counts**. The Hub never receives tenant content (gateway rejects `dataclass-not-permitted` above `INTERNAL` on OH subjects). Support-ticket and CRM interactions use the Hub's APIs from `apps/delivery` (P22) under those limits. *(Conflict to resolve in master: Spec §6.27 places the revenue catalogue and the Razorpay account in the Hub (OH8); D-21/P20 place the pricing catalogue and checkout in LDC — see master note M-S8-02.)*
- **FinLegal Academy** (`trainings.lawdocs.in`, an LMS): `AcademyProvider` port — read the course catalogue (title, category, duration, price, accreditation, URL) for the marketplace (P21); create enrolments for tenant employees with SSO hand-off (OIDC; or LTI 1.3 if the LMS supports it [VERIFY]); receive completion events and certificates (PDF + verification URL) into the employee's training record (P13) and into compliance evidence where a training obligation exists (e.g. KYC/AML, POSH, cyber awareness); xAPI/SCORM statements accepted if the LMS emits them [VERIFY LMS platform].

**FR-P18-23 — Group mode (`LDC_GROUP`).** One LDC tenant per `group_id` with every record tagged by `reid`/legal entity; group roll-up dashboards; entity-level segregation for users without group roles; group grants (Spec §4.6) for cross-company staff with ≤ 90-day validity, approvals by both entity heads and the DPO, enforced locally with sessions ended within 60 s of expiry. Infrabyx's own obligations run in an `LDC_GROUP` instance for the Infrabyx group; no client RE's LDC data is visible to the Hub.

### 4E. Third-party lending, LSP and recovery systems

**FR-P18-24 — Connector SDK host.** LDC hosts connectors implementing `@infrabyx/connector-sdk` (`manifest`, `capabilities`, `healthCheck`, `send`, `receive`, `call`, `reconcile`; Spec §10.1) out of process (separate container per connector per region; network egress allow-list per manifest; secrets via vault handle in `TenantContext`; no access to the LDC database — APIs and events only). A connector without RE context (`reid`) fails. Third-party connectors require residency and sub-processor review, VAPT ≤ 12 months old, and the outsourcing clauses (Spec §10.1).

**FR-P18-25 — Inbound generic GRC contract.** For tenants whose LOS/LMS is not Finbyx, LDC accepts the generic GRC connector resources of Spec §9.2 (`Obligation` pull, `ControlTestResult`, `Evidence`, `Issue`, `Incident`, `RegulatoryReturn`, `PolicyAttestation`, `OutsourcingArrangement`, `KRI`, `RegulatoryChange`) and the minimum control feed list (classification sync T+1, agent notice before contact, contact windows, KFS before execution, DLG cap and disclosure, etc.) as `ControlTestResult` submissions mapped to obligations.

**FR-P18-26 — Reference adapters and mapping packs.** Reference connectors: (1) **Apache Fineract** (REST `/fineract-provider/api/v1/` — loan products, loans, repayment schedules, delinquency buckets, GL entries) feeding P09 ratio inputs and P11 return data-prep in aggregate or tenant-approved record-level form; (2) **Generic LMS CSV/XLSX** registered layouts (`loan_master_v1`, `schedule_v1`, `payment_v1`, `collateral_register_v1`, `gl_journal_v1`, plus LDC layouts `ldc_trial_balance_v1`, `ldc_portfolio_snapshot_v1`, `ldc_alm_buckets_v1`, `ldc_grievance_log_v1`, `ldc_recovery_log_v1`); (3) **Webhook-capable LOS** (generic inbound webhook with mapping pack). Each connector ships a mapping pack (`mappings/[connector-id]/[version]/mapping.yaml`: JSON Pointer maps, code-table maps, approved transformations, validation rules, golden fixtures; Spec §10.3). Tenants override only `x-tenant-overridable` fields by maker-checker (patch version `1.4.0+tenant_01J…`); meaning-changing edits require recertification. Vidhi (V-SK-17) may propose a mapping from sample files; a human approves.

**FR-P18-27 — File-transfer fallback.** SFTP (allow-listed Indian IPs; ed25519 keys; per-tenant chroot), signed-URL upload, or the on-premises agent; CloudEvents batches (`application/cloudevents-batch+json`), NDJSON or registered CSV/XML layouts; signed manifest (layout, version, count, control totals, period, SHA-256; detached JWS); acknowledgement file of accepted and rejected records; naming `[producer]_[reid]_[layoutid]_v[major]_[yyyymmdd]_[seq].[ext]` (Spec §3.11).

**FR-P18-28 — On-premises agent (`ldc-agent`).** A signed, auto-updating agent (Windows service and Linux daemon; outbound-only mTLS with a device certificate; no inbound ports) installed on the client's network for: TallyPrime access (listener on localhost:9000 is never exposed to the internet), on-premises LMS/database extracts (read-only DB user, parameterised extract jobs defined in the mapping pack), NAS/SMB/hard-disk storage targets (P19), CIC SFTP submission from a tenant-controlled host (Spec §10.2 `BureauSubmitter`), and DSC signing helpers where needed. Agent management: register with a one-time token, health heartbeat, version pinning, job logs (metadata), remote disable; agent updates are signed (Sigstore/cosign) and verified before install.

### 4F. Accounting and books sources (transport)

**FR-P18-29 — TallyPrime.** Through `ldc-agent`: (a) XML over HTTP (`<ENVELOPE><HEADER><TALLYREQUEST>Export Data</TALLYREQUEST>…`) for Trial Balance, Balance Sheet, Profit & Loss, Ledger and Voucher collections, Day Book, stock items; (b) **native JSON** for TallyPrime 7.0 and later (headers `content-type: application/json`, `version: 1`, `tallyrequest: Export`, `type: Data|Collection|Object`, `id`, and static variable `svCurrentCompany` always set to avoid exchanging data with the wrong company); (c) ODBC for collections marked ODBC tables where the client prefers. Extract profiles: period trial balance with ledger groups, opening/closing, voucher-level GL for audit sampling (P10), GST registers (P11), loan ledgers where Tally is used for loan accounting by small NBFCs/co-operatives. Data is pushed to LDC as `ldc_trial_balance_v1` / `gl_journal_v1` with control totals; P11 maps ledgers to the chart of accounts and Ind AS/AS schedules. Write-back to Tally (journal import) is out of scope for LDC (Finbyx owns ledger posting; Spec §10.2 `AccountingSink`).

**FR-P18-30 — Other accounting systems.** Zoho Books (OAuth REST, India data centre `zoho.in`), SAP S/4HANA (OData) and SAP Business One (Service Layer) via certified connectors; Busy, Marg, and others via their export files [VERIFY native APIs]; generic XLSX/CSV trial balance with a mapping wizard (P11).

### 4G. Identity, KYB and registry adapters (onboarding)

**FR-P18-31 — Company and LLP master data.** `CompanyRegistryProvider` port with licensed aggregator adapters (candidates: Probe42, Signzy, Surepass, Perfios/Karza, HyperVerge, Qorpiq — contract and DPA required; [VERIFY data rights for display and storage]). Inputs: CIN, LLPIN, company name search, PAN (to CIN mapping where the provider supports it). Outputs (as available): legal name, constitution (private, public, OPC, Section 8, LLP, foreign company), status, date of incorporation, ROC, registered address, authorised and paid-up capital, directors/designated partners with DIN (no PAN or date of birth stored), charges summary, last AGM/balance-sheet dates, listed status, industry classification. Source and retrieval time shown; user confirms each field; stored as `onboarding_snapshot` with provider attribution. No scraping of MCA21.

**FR-P18-32 — PAN, GSTIN, LEI, Udyam and DigiLocker.**
- **PAN verification** through an authorised channel (Protean/NSDL PAN verification service for eligible entities, API Setu where permitted, or a licensed KYB aggregator) returning name match and status; PAN stored masked + token (NN-12) [VERIFY eligibility of LDC/aggregator].
- **GSTIN** search via a GST Suvidha Provider or aggregator (legal name, trade name, status, registration date, state, taxpayer type); multiple GSTINs per PAN listed for selection.
- **LEI** via GLEIF public API (free; legal name, LEI status, registration authority, parent relationships).
- **Udyam** registration verification (MSME) via aggregator [VERIFY].
- **DigiLocker** (Authorized Partner API, OAuth 2.0 + PKCE, user consent): optional pull of issued documents for **individual users** (e.g. professional's certificates for marketplace onboarding, P21; KMP identity documents only where a tenant's fit-and-proper workflow needs them, P06) — documents stored in the DMS under the HR/SPI class with retention rules; Aadhaar number is never stored; masked Aadhaar from DigiLocker XML is retained only if the workflow requires and the user consents.

**FR-P18-33 — No bureau pull at onboarding (push-back recorded).** The brief mentions CIBIL APIs for registration (R-029). LDC is not a credit institution or specified user entitled to obtain credit information under the Credit Information Companies (Regulation) Act 2005 for a SaaS sign-up or lead-qualification purpose [INTERP; VERIFY with counsel], and consumer bureau data for directors would be personal data with no lawful purpose here. Therefore: no bureau pull in onboarding or the health check. Optional alternative: a tenant may **upload** its own CIBIL commercial (CCR/CMR) report for use in its own risk module, stored as the tenant's document. Bureau *submission* compliance for lender tenants is handled through Finbyx or the tenant's own CIC membership (P11, Spec §6.19).

**FR-P18-34 — Regulator registry datasets.** For applicability and verification (P01, P15), LDC maintains platform datasets downloaded from official public lists (RBI lists of NBFCs, ARCs, UCBs, banks; SEBI registered intermediaries; IRDAI registered insurers and intermediaries; IFSCA registered entities; co-operative registrar lists where published), refreshed on a schedule by the content team with source hash and date. Matching a tenant to a registry entry (e.g. RBI CoR number, SEBI registration number) proposes entity type and layer; the tenant confirms; mismatches create an onboarding task. These are public datasets — no login, no scraping of authenticated pages.

### 4H. Workplace suites, identity federation and calendars

**FR-P18-35 — `WorkplaceProvider` port (suite-neutral; D-10).** Capabilities: SSO federation, SCIM provisioning, calendar, meetings, mail (designated mailboxes), document libraries, file opening/editing in the suite's web apps. Adapters: Microsoft 365 (first), Google Workspace (second), generic SAML/OIDC + SCIM (Okta, Zoho Directory, Keycloak), "no suite" (LDC-native email via SES and ICS feeds). The tenant's suite and plan are recorded (`int.workplace_profiles`); features are enabled per plan capability (e.g. Teams transcripts need a Teams licence with transcription; SharePoint advanced retention needs specific plans) and the UI explains missing capabilities. *(Owner to confirm plan: "Microsoft 365 Business Starter" is not a Microsoft plan — D-10.)*

**FR-P18-36 — SSO and SCIM.** Tenants may federate their IdP (Entra ID, Google, Okta; OIDC preferred, SAML 2.0 supported) — P01 owns login UX; P18 owns the connector configuration, metadata exchange, certificate rotation reminders and SCIM 2.0 endpoint (`/scim/v2/Users`, `/Groups`) with attribute mapping to LDC users, departments and role groups (role assignment from IdP groups is optional; LDC role catalogue remains authoritative; SoD rules re-checked on every SCIM change). Leavers deprovisioned within 4 hours (privileged within 1 hour) (Spec §4.2).

**FR-P18-37 — Calendar sync (R-094).** Three modes, chosen per user (admin can mandate a mode per tenant):
1. **Native two-way for work accounts** — Microsoft Graph (`Calendars.ReadWrite` delegated, change notifications via Graph subscriptions with renewal) or Google Calendar API (OAuth, push notifications via watch channels): LDC writes events into a dedicated secondary calendar "LawDocsComply" (default; avoids cluttering the primary calendar; option to write into primary), with event categories by type (deadline, task due, meeting, review, filing). Changes made by the user in their calendar to LDC-owned events (time moves) are **not** written back to LDC deadlines (statutory dates are authoritative; NN-07); only meeting events created from LDC can sync RSVP/attendance back (P06).
2. **ICS subscription for any calendar** (Outlook.com, Gmail personal, Apple Calendar, Thunderbird): per-user secret feed URL (`https://cal.lawdocscomply.com/feeds/{token}.ics`, RFC 5545) with role-scoped content, rotating token, revocable, minimal data in event text (titles without personal data of third parties; optional "privacy mode" shows only "LawDocsComply item — open app"). Refresh depends on the client app (typically 15 minutes to a few hours — the UI says so) so reminders are also sent by LDC notifications.
3. **CalDAV** (RFC 4791) read-only server for Apple Calendar and other CalDAV clients that prefer it, with app-specific passwords tied to the user's LDC account [REC; optional].
Visibility follows role rules (P04): a department head's feed includes all department entries; a user's feed includes items assigned to them, items they own, meetings they attend and deadlines they follow; board members get meetings and board deadlines only. Reminders: VALARM entries at the user's preferred lead times so phones alert through the native calendar.

**FR-P18-38 — Meetings and transcripts.** Microsoft Teams meeting creation for Board/committee meetings scheduled in P06 (online meeting link inserted into notice), attendance report retrieval, and transcript retrieval (Graph `onlineMeetings/{id}/transcripts`) for Vidhi minutes (P17) when the organiser consents; Google Meet equivalent later; JioMeet listed as a candidate adapter [VERIFY API]. Board-confidential meetings may be configured "no transcript import".

**FR-P18-39 — Document libraries.** Microsoft Graph `Sites.Selected` permission (application) limited to sites the tenant grants; LDC can (a) **mirror** approved documents (policies, board packs after approval) to a SharePoint library with metadata columns (LDC id, version, owner, approval date, next review date) for staff who live in SharePoint; (b) **open drafts in Word for the web** for co-authoring and return the edited file to LDC as a new version (check-in), or (c) act as a **storage target** for exports/backups (P19). LDC remains the system of record for compliance artefacts; mirrored copies carry "copy — system of record is LawDocsComply" metadata. Google Drive equivalents with shared drives only, non-regulated data only (Spec §12.2).

### 4I. eSign and stamping

**FR-P18-40 — `ESignProvider` port.** Adapters: Leegality, Digio, SignDesk, Surepass, eMudhra (emSigner), LawDocs eSign (group); capabilities per adapter: Aadhaar eSign (OTP/biometric via ESP under CCA guidelines), DSC signing (Class 3 USB token via desktop signer or the agent), electronic signature (non-Aadhaar, click-to-sign with OTP) for documents where the law permits, e-stamping (where the ESP offers state e-stamp integration), signer sequencing, witnesses, audit trail certificate, webhook callbacks. Flow: P07 creates an envelope (document hash, signers, order, signature types per signer, placement), the adapter returns signing URLs; completion returns signed PDF (PAdES), audit certificate, signer details (name, masked identifiers), which P07 stores with hashes (NN-09). Rules: IT Act 2000 First Schedule exclusions (e.g. negotiable instruments other than cheques, powers of attorney, trusts, wills, contracts for sale or conveyance of immovable property) are blocked from eSign with an explanation (D-20); MCA e-forms require DSC; service-level agreements and engagement letters for retainers (P21) and employment agreements (P13) are typical eSign uses.

**FR-P18-41 — Signature evidence.** The signed document's own signature validation (certificate chain, timestamp, LTV where available) is checked on receipt and periodically; failures alert the document owner.

### 4J. Communications channels

**FR-P18-42 — Email.** Outbound: Amazon SES (ap-south-1) with tenant-branded sender domains (DKIM, SPF, DMARC alignment checks before activation), or the tenant's Microsoft 365 send-as for designated mailboxes, or the tenant's SMTP relay (TLS). Transactional templates only from LDC; bulk marketing is not an LDC function (Ops Hub/Brevo; Spec §10.2 CRM). Inbound: dedicated per-tenant addresses (e.g. `grievance+{tenant}@in.lawdocscomply.com` or the tenant's own address forwarded) parsed into P14 cases or P07 documents; bounce and complaint handling; invoices emailed by P20 through this channel (R-035).

**FR-P18-43 — SMS.** DLT-compliant (TRAI TCCCPR 2018 as amended): the **tenant** is the Principal Entity for messages to its customers; LDC stores the tenant's registered headers and template IDs and refuses to send unregistered content; categories (transactional, service-implicit, service-explicit, promotional) recorded; adapters JioCX SMS and other aggregators. LDC's own platform messages (OTP to LDC users) use LDC's DLT registration.

**FR-P18-44 — WhatsApp Business Platform.** Through a Business Solution Provider adapter (JioCX WhatsApp or another BSP). Rules: opt-in captured and stored; template messages (utility/authentication; marketing only by tenant choice outside LDC's core); per-message pricing since 1 July 2025 and Meta Business Agent per-token billing from 1 July 2026 surfaced as usage cost to the tenant; for India sold-to accounts, INR billing migration required by 31 December 2026 (non-INR accounts stop delivering from 1 January 2027) [VERIFY with BSP]; **never used for debt collection, recovery or legal notices** (WhatsApp Business Messaging Policy; Spec §4.4/§10.2); grievance acknowledgements and status updates allowed where the complainant opted in.

**FR-P18-45 — Voice and contact centre.** `VoiceProvider` adapters: JioCX Voice and Jio SIP Trunk via a CPaaS/contact-centre platform; Exotel/Plivo/Ozonetel as alternates. Uses in LDC: (a) tenant's grievance helpline IVR and call-back logging into P14; (b) automated reminder calls to the tenant's **own staff** for critical deadlines (opt-in, internal); (c) Ops/Delivery outreach is an Ops Hub function, not LDC. Rules: calls to a regulated tenant's customers present the tenant's **1600-series** number where required (TRAI direction for RBI/SEBI/IRDAI/PFRDA-regulated entities) [VERIFY current TRAI series rules]; promotional calls only from 140-series and never from LDC; consent, recording disclosure, DND scrub, time windows (RBI contact-hour rules for borrower-facing calls are the tenant's responsibility and are enforced by Finbyx/Udofin, not LDC). AI voice agents (Jio Haptik or others) only behind flag `int.voice.ai_agent.enabled = OFF` with disclosure in the first utterance.

**FR-P18-46 — RCS, web push and in-app.** RCS through JioCX RCS behind a flag; web push (VAPID) for LDC users who opt in; in-app notifications are P04's. Channel preference and quiet hours per user (P04) are honoured by every adapter.

### 4K. Website, app and system embeds

**FR-P18-47 — Grievance and help widgets (R-080, R-098).** Three integration options for a client company's website or mobile app:
1. **Script embed** — `<script src="https://embed.lawdocscomply.com/v1/grievance.js" data-key="pk_live_…" data-lang="en,hi" async></script>` rendering an accessible launcher (WCAG 2.2 AA) and form (category, description, attachments, contact, consent notice, preferred language), with the tenant's branding; posts to `POST /v1/embed/grievances` using a publishable key bound to allowed origins; returns a complaint reference and acknowledgement text.
2. **Hosted page** — `https://{tenant-slug}.care.lawdocscomply.com/grievance` (or a CNAME such as `grievance.{clientdomain}` with managed certificates), linkable from footers, apps, SMS and emails; includes the escalation matrix (support → GRO → escalation → Ombudsman links per regulator) that P14 configures, and a status tracker (reference + OTP).
3. **API** — `POST /v1/grievances` server-to-server for clients who build their own forms (their website backend, LOS, LMS, LSP app, call-centre CRM), with webhooks for status changes.
Help & support (level-1 tickets) uses the same widget with a "Help" mode routing to the client's support team in P14, so the client's support staff close tickets inside LDC.

**FR-P18-48 — Public disclosure pages.** Hosted, versioned public pages for documents that regulated entities must publish (e.g. Fair Practices Code, grievance redressal mechanism and GRO details, interest-rate policy summary, privacy notice, list of outsourced agencies where applicable) generated from approved policy versions in P07, with change history and embed snippets — the client's website links to or embeds them, so updates happen once [REC; applicability per sector pack, P15].

**FR-P18-49 — System integration APIs.** For a client's own LOS/LMS/recovery/LSP: create evidence, report control results, raise issues, read obligations and tasks, post incidents, post grievance cases, read policies for display; sample integration recipes in the developer portal ("Post daily KFS-before-disbursal control results", "Send monthly DLG disclosure evidence", "Push complaints from your call-centre CRM").

### 4L. Payment gateway adapter

**FR-P18-50 — `PaymentGateway` port (used by P20/P21).** Razorpay adapter (orders, payment links, Subscriptions, UPI Autopay/e-mandates, refunds, webhooks with signature verification and server-side status fetch; hosted checkout only; no card data touches LDC — NN-16; Razorpay Route for marketplace split settlements only after P21 legal clearance, flag OFF). Alternate adapters (e.g. Cashfree, PayU) stubbed. Webhook endpoint isolated (`/v1/webhooks/payments/razorpay`), idempotent by event id.

### 4M. Developer platform

**FR-P18-51 — Developer portal (`developers.lawdocscomply.com`).** Content: getting started, authentication guides, API reference (OpenAPI 3.1 rendered; try-it against sandbox only), event catalogue (AsyncAPI 3.0), webhook guide with signature verification samples (TypeScript, Python, Java, C#, PHP), SDK downloads, Postman collection, mapping-pack authoring guide, connector SDK guide, rate limits, error codes, changelog, deprecation calendar, status page link, security disclosure (`/.well-known/security.txt`), terms of API use. Accessible and indexable (SEO/GEO, P23).

**FR-P18-52 — Sandbox.** Self-service sandbox tenants pre-seeded with synthetic data per entity family (NBFC-ML, UCB, listed company, AIF, insurer, credit co-operative), a time-travel clock for deadlines, and simulators for ecosystem events (Finbyx risk feed, Udofin grievance, Ops Hub provisioning). Sandbox data is synthetic only; sandbox is a separate environment with separate CA and keys (Spec §3.7).

**FR-P18-53 — Client registration.** Developers register (`ext_developer` account; email verification; MFA), create sandbox clients instantly; production clients are requested against a tenant and approved by the tenant admin (and by platform security for certified-connector status). Each client: owner, purpose, scopes, `data_class_max`, environments, keys (JWKS URL or uploaded public key), redirect URIs, allowed origins, expiry, IP allow-list (optional).

**FR-P18-54 — Connector certification.** For third-party connectors offered to multiple tenants: submission (manifest, mapping pack, VAPT ≤ 12 months, sub-processor and residency statement, DPA), automated certification suite (Spec §14.3 groups relevant to the connector), manual review, `ConnectorCertified` event, listing in the connector catalogue (tenant-visible), recertification on schema/hosting/key/sub-processor change and annually.

**FR-P18-55 — Connector catalogue (tenant view).** Settings → Integrations shows available connectors (ecosystem, certified third-party, built-in adapters) with what data moves in each direction, data classes, residency, cost implications (e.g. WhatsApp per-message charges, aggregator per-lookup charges passed through per P20), required plan, and a guided setup.

### 4N. Tenant onboarding by API

**FR-P18-56 — Provisioning API (R-002).** `POST /v1/provisioning/tenants` (Ops Hub and authorised channel partners only; scope `ops.tenant:provision`) creates a tenant from a signed `TenantProvisioned` payload: organisation (`org_id`, legal name, constitution, CIN/LLPIN, masked PAN, GSTIN, LEI), entity family and regulator profile proposal, plan/entitlements, first admin's work email (legal basis `CONTRACT_PERFORMANCE_VENDOR`), region, data-residency attestation; idempotent by `org_id`; returns provisioning status and emits `TenantProvisioned` acknowledgement (`ops.provisioning:ack`). Self-service sign-up (P01) uses the same internal service.

**FR-P18-57 — Group and bulk onboarding.** A group (holding + subsidiaries; or a co-operative federation) can onboard N legal entities in one request (`/v1/provisioning/groups`) with entity-level profiles, shared admin roles, and `LDC_GROUP` mode where chosen; Finbyx can initiate "connect my NBFC to LawDocsComply" from its console, creating a `re_grc_link` request plus (if needed) a new LDC tenant, subject to the RE's approvals.

**FR-P18-58 — Data migration import API.** `POST /v1/imports/{kind}` (obligation registers from other GRC tools, task histories, policies with versions, board minutes archives, risk registers, audit findings, user lists) with a dry-run mode, validation report, mapping templates (CSV/XLSX), and commit with rollback window; imports from competitor tools (exports from Lexplosion, Lawrbit, Komrisk, etc.) via CSV mapping templates [REC]. Imports never set audit history as if it happened in LDC; imported history is labelled with source system and original timestamps (D-02 bitemporal).

### 4O. Integration monitoring and operations

**FR-P18-59 — Integration monitor.** Tenant view and platform view: per connector health (last success, latency p95, error rate, DLQ depth, certificate/key expiry, residency check status, certification status), event lag per subject, reconciliation results (daily counts and hashes sent vs acknowledged; monthly value sampling for the risk feed — Spec §6.22), alerts by email and in-app to integration owners; incident creation for persistent failures; per-connector circuit breakers and kill switch (tenant and platform).

**FR-P18-60 — Regulator portals are manual.** For RBI CIMS/DAKSH/PRAVAAH, SEBI SI portal, IFSCA, IRDAI, MCA, GSTN, CERSAI, FIU-IND FINGate, EPFO/ESIC and income-tax portals: LDC produces validated upload files (P11), a guided checklist and acknowledgement capture (`PORTAL_MANUAL`); it never stores portal credentials for automated use, never stores OTPs, cookies or session tokens, and never runs RPA or scraping (Spec §10.2; D-13). Credential vault entries (D-04, P22) are for **human** reveal only and are not readable by any connector or by Vidhi.

**FR-P18-61 — Fewer clicks for integration setup.** Guided setups with prerequisites checks (e.g. "Your Microsoft 365 admin must consent to the LawDocsComply app — send them this link"), copy-paste snippets, test buttons, and a "connection health" badge on every screen that depends on a connector (e.g. calendar sync status in the user menu).

### 4P. LDC MCP server (`ldc-mcp`) *(v1.1; D-35; NN-52; Appendix AA §AA.7)*

**FR-P18-62 — Purpose and position.** LDC exposes a Model Context Protocol server so that a client's own AI assistant (Claude, Microsoft Copilot through Copilot Studio, ChatGPT, Gemini or an in-house agent) can work with LawDocsComply **as the signed-in user**. The MCP server is an *edge* on top of the same REST services and policy engine; it introduces no new data path and no new authority. It ships before the MCP client (D-35).

**FR-P18-63 — Endpoint and transport.** Streamable HTTP at `https://mcp.lawdocscomply.com/<cell>/v1` (cell code `in` first; `eu`, `gcc`, `sg`, `us` when those cells exist, §4S). Invalid `Origin` headers are rejected (403). Spec version negotiated (baseline MCP 2025-11-25; older revisions supported for 12 months after a newer one is adopted; policy in `docs/interfaces/mcp.md`). Long operations are exposed as MCP tasks where the client supports them, otherwise as a job id plus a `get_job_status` tool.

**FR-P18-64 — Authorisation.** OAuth 2.1 with PKCE against Keycloak (`ldc` realm) as authorisation server; Protected Resource Metadata (RFC 9728) at `/.well-known/oauth-protected-resource`; clients identified by Client ID Metadata Documents (preferred) or pre-registration; tokens audience-restricted to `ldc-mcp` (no token pass-through — the server performs an internal token exchange to call LDC services as the user); incremental scope consent via `WWW-Authenticate`. Scopes:

| Scope | Grants | Default ceiling |
|---|---|---|
| `mcp.read` | Resources and READ tools (obligations, instances, calendar, Updates, policies metadata, KRIs/ratios as permitted) | Allowed when the tenant enables the server |
| `mcp.draft` | DRAFT tools (`draft_note`) — output lands in the user's LDC drafts | Allowed |
| `mcp.propose` | PROPOSE tools (`propose_tasks`) — lands in the Work Inbox for acceptance | Allowed |
| `mcp.reminder` | INTERNAL_WRITE_LOW (`create_my_reminder`) with elicitation confirmation | Allowed |
| `mcp.evidence_draft` | `attach_evidence_draft` — only through URL-mode elicitation into LDC with preview and approval | Off; tenant may enable |
| — | Approve, attest, mark complied, sign, file, pay, publish, change access, credential vault | **Never exposed** (NN-14, NN-52) |

**FR-P18-65 — Tool catalogue.** The tool and resource catalogue is exactly Appendix AA §AA.7.3–§AA.7.5 (resources `ldc://tenant/profile`, `ldc://obligations/{id}`, `ldc://instances?…`, `ldc://calendar/{yyyy-mm}`, `ldc://updates?since=`, `ldc://policies/{id}`, `ldc://risks/register`, `ldc://kri/{id}`, `ldc://notebooks/{id}`, `ldc://reports/{id}`; tools `search_obligations`, `get_obligation`, `explain_applicability`, `list_due_items`, `list_overdue_items`, `get_instance_status`, `ask_regulation`, `list_updates`, `get_update_impact`, `get_kri`, `get_ratio`, `draft_note`, `propose_tasks`, `create_my_reminder`, `attach_evidence_draft`, `get_job_status`). Tool definitions (name, description, input/output JSON Schema, action class, data classes) live in `packages/contracts/mcp/` and are versioned; a description change is a contract change (CI diff gate). `ask_regulation` is answered inside LDC by Vidhi on the governed India route — the external assistant receives the cited answer, never the raw notebook corpus.

**FR-P18-66 — Tenant controls.** Off by default (`int.mcp.server.enabled`, T). The tenant admin or `ten_integration_admin` approves each external AI client (allow-list by client metadata URL), sets a per-client scope ceiling, and records the legal basis for sending `PII`/`CONFIDENTIAL` results to that AI provider (`int.mcp.client_basis`); without a basis, tools return masked or aggregated results. Users consent per client on first use and can revoke from their profile. Sealed classes are never returned (NN-13, NN-52) — the filter runs in the service layer, not in the MCP adapter, so no tool bug can bypass it.

**FR-P18-67 — Limits and protection.** Rate limits per user (default 60 tool calls/min) and per tenant (default 10,000/day), payload size caps, result pagination, output truncation with continuation tokens; anomaly detection (sudden enumeration of obligations or bulk reads across departments) raises a security alert and can auto-suspend the client (P24 SIEM rule).

**FR-P18-68 — Audit and transparency.** Every MCP call is written to the AI run ledger as `ExternalAiAccessed` (client id, user, tool, arguments hash, result size, data classes returned, cell) and shown on the tenant's **External AI access log** (SCR-AI-24) and in the access-transparency page (P22, IMP-112). Exported in LDC-EXPORT folder 18.

**FR-P18-69 — Conformance.** CI runs the MCP conformance suite and an LDC permission matrix test: every tool is called as each role in Appendix D; a tool must never return a record the same user cannot read through the REST API (`NN-52_mcp_parity`). Sealed-class canaries are planted in the test tenant and must never appear in any MCP result.

**FR-P18-70 — Listing.** Server metadata and icons are published to the public MCP registry and to Microsoft and other assistant marketplaces only after a security review and a claims-register entry for the listing text (NN-19) [VERIFY registry and marketplace processes at build time].

**FR-P18-71 — Fewer clicks.** Settings → Integrations → AI assistants offers one-click "Connect Claude / Copilot / ChatGPT" cards that show the redirect URI, scopes and a test prompt; a QR/URL hand-off lets the user finish consent on another device.

### 4Q. MCP client registry (Vidhi reaching client systems) *(v1.1; Appendix AA §AA.8)*

**FR-P18-72 — Registration.** The tenant registers an external MCP server (URL, authentication, owner, region, data classes it returns). Off by default (`ai.mcp.client.enabled`, T). Native adapters (Graph, Google, Tally, Finbyx, ITSM) always take precedence over MCP for the same system.

**FR-P18-73 — Tool admission.** LDC discovers the server's tools, classifies each (action class, data classes) and shows them for **per-tool approval**. Approved tool descriptions and schemas are pinned by hash; any change suspends the tool until re-approved (`McpToolSuspended`) — defence against tool-description poisoning. External write tools default to `EXTERNAL_SEND` (human Send on the exact payload). Results are untrusted content (prompt-injection isolation, P17) and enter LDC only as evidence drafts the user accepts. Calls to servers outside the tenant's home cell are allowed only for data with a recorded transfer basis (NN-24).

### 4R. A2A gateway *(v1.1; Appendix AA §AA.9; flag `int.a2a.enabled` = OFF until Ecosystem Spec v1.2)*

**FR-P18-74 — Agent Cards.** Each exposed LDC agent publishes a signed A2A Agent Card at `https://<cell>.agents.lawdocscomply.com/.well-known/agent-card.json` (per agent path), listing skills offered, input/output schemas that reference Ecosystem contracts, authentication (mTLS + OAuth client credentials with RFC 8693 token exchange carrying the delegating user or sponsor), data classes, region, rate limits, version and JWS signature (key in KMS). Cards are registered in the group Agent Registry in `infrabyx-contracts`.

**FR-P18-75 — Contract mapping.** `int.a2a_contract_map` maps every accepted A2A skill/task type to one Ecosystem API or event (Appendix AA §AA.9.3). A task without a mapping is rejected (`LDC-INT-120`) — the protocol is the edge, the contract is the core (NN-52). Responses are untrusted content; no inbound A2A task can trigger a PROHIBITED or EXTERNAL_SEND action in LDC.

**FR-P18-76 — Peers.** Peers are allow-listed per tenant (Finbyx, Udofin, Equator, Ops Hub by default once enabled; a client's in-house agent only on Enterprise plans, and MCP remains the preferred route for clients). A2A traffic is logged in the run ledger and the integration monitor.

### 4S. Multi-region cell routing *(v1.1; NN-24 as amended; Appendix Y §Y.7; D-42)*

**FR-P18-77 — Routing.** The global control plane resolves `tenant_id` + `legal_entity_id` → home cell. Public API, MCP, webhooks and developer-portal base URLs are cell-qualified (`https://api.<cell>.lawdocscomply.com/v1`, `mcp.lawdocscomply.com/<cell>/v1`); a request that reaches the wrong cell receives `307` with the correct cell URL (never served cross-cell). SDKs resolve the cell from the token's `cell` claim.

**FR-P18-78 — Connectors bound to cells.** Every connector instance is created in the cell of the legal entity it serves; its outbound destinations are checked against the transfer register before activation (residency check status shown on SCR-INT-03). A group-level connector (e.g., a group Microsoft 365 tenant) is created per cell with entity scoping.

**FR-P18-79 — Ecosystem events across cells.** Ecosystem events carry `dataregion` (CloudEvents extension) and are published from the producing cell; group products in another region receive only event types classified as metadata/aggregate unless a transfer basis is recorded (Ecosystem Spec v1.2 CR: residency attribute per entity).

**FR-P18-80 — Cross-cell aggregation API.** Internal, mTLS-only API that each cell exposes for group views (counts, statuses, due dates, scores, KPI values, document titles without content). Personal data and document content never travel through it (NN-24).

**FR-P18-81 — Cell readiness gate.** A new cell is enabled only when: infrastructure and DR are tested (P24), the AI route for that region is verified (NN-41), egress allowlist includes the jurisdiction's official sources (Appendix F), data-transfer opinions are on file (Appendix Y §Y.8), and the cell appears in the Trust Centre (P23).

### 4T. Regulatory intelligence and FX rate ports *(v1.1; Appendix Y §Y.11, §Y.9.1)*

**FR-P18-82 — `REG_INTEL_PORT`.** Adapter interface for licensed regulatory-intelligence feeds (candidates: Thomson Reuters Regulatory Intelligence, LexisNexis, Wolters Kluwer, CUBE, Regology, Corlytics, OneTrust DataGuidance). Each adapter declares licence display rights (headline / summary / link / full text), jurisdictions, latency and attribution text. Items enter the P05 Radar as `LICENSED_SIGNAL` with provider attribution and become Updates only after the pack's reviewer of record confirms the primary source (NN-34). Full text is never redistributed beyond the licence.

**FR-P18-83 — `FX_RATE_PORT`.** Reference-rate sources configurable per tenant and purpose (default for INR: RBI/FBIL reference rates; EUR: ECB euro reference rates; AED: CBUAE; SGD: MAS) [VERIFY source availability and terms]. Every converted figure stores a rate snapshot (source, date, rate type: spot, monthly average, closing). Rates are never fetched at render time for regulatory figures — the snapshot travels with the value (NN-22).

**FR-P18-84 — Fallbacks.** If a source is down, the last snapshot within a configurable staleness window is used and labelled; beyond it, dependent conversions show "rate unavailable" and block report approval.

**FR-P18-85 — Pricing currencies.** Commercial pricing currencies (INR, USD, AED, SGD, EUR, GBP) are OH8's price books (X-02); `FX_RATE_PORT` is used only for display conversions and reporting, never to set prices.

### 4U. Connectors for the v1.1 modules *(v1.1)*

**FR-P18-86 — `LITIGATION_DATA_PORT` (P26).** Case-status and cause-list data for Indian courts and tribunals (e-Courts/NJDG case status, High Courts, NCLT/NCLAT, DRT/DRAT, consumer commissions via e-Jagriti, tax tribunals) through licensed data aggregators or official APIs where available; no scraping where terms prohibit it [VERIFY provider licences, OI-P18-21]. Fallback: manual case-number entry with a daily reminder to update status. Imports create or update `lit.matters`, hearings and orders; directions with due dates become tasks (P04).

**FR-P18-87 — Notices intake (P26).** E-mail-in mailbox per tenant for legal and regulatory notices (`notices+<tenant>@in.lawdocscomply.com`), with OCR/classification by Vidhi (draft only) and a human confirmation step before a matter or regulator-correspondence record is created.

**FR-P18-88 — `CONTRACT_REPO_PORT` (P26).** Read-only import of executed contracts and metadata from SharePoint/OneDrive/Google Drive folders, CLM tools (candidates: SpotDraft, Leegality CLM, Ironclad, DocuSign CLM) and eSign envelope histories (Leegality, Digio, DocuSign); obligations extracted from contracts are Vidhi drafts until accepted (NN-14).

**FR-P18-89 — `ESG_DATA_PORT` (P27).** CSV/XLSX templates and APIs for energy, fuel, water, waste and travel data; HRMS headcount and diversity aggregates (P13, k ≥ 5); utility and meter data; emission-factor libraries (India CEA grid factor, IPCC, DEFRA/DESNZ, GHG Protocol tools) held as signed rule packs (NN-26 pattern); BRSR/BRSR Core outputs go to P27 and P11 for XBRL.

**FR-P18-90 — `ENTITY_REGISTRY_PORT` (P25).** Foreign company-registry data for global entity management (candidates: UK Companies House API, Singapore ACRA via licensed channel, OpenCorporates licensed data, local registered-agent feeds) [VERIFY licences]; populates foreign entity records, officers and filing calendars as drafts for confirmation.

**FR-P18-91 — `ITSM_PORT`.** Bi-directional issue sync with Jira, ServiceNow and Freshservice (status, assignee, due date, comments; evidence links not content) for compliance issues, audit findings and remediation actions (IMP-133).

**FR-P18-92 — Connector catalogue metadata.** Every new connector declares owner phase, data classes, cell support, licence terms and certification status in the catalogue (SCR-INT-01).

### 4V. Improvements from client feedback *(v1.1; Appendix Z)*

**FR-P18-93 — Connector health alerts (IMP-130).** Each connector instance shows last successful sync, next run, error count, retries and DLQ depth on SCR-INT-03; failures beyond a threshold (`int.health.alert_after_failures`, T, default 3) notify the integration admin and create a Work Inbox item with the fix-it action (re-consent, rotate key, fix mapping).

**FR-P18-94 — Open by default (IMP-131).** Public OpenAPI 3.1 for all tenant-facing APIs, webhooks for every material state change, and the MCP server (§4P). The developer portal shows "try it" with sandbox tenants.

**FR-P18-95 — Admin API (IMP-132).** Scoped admin endpoints for users, roles, department/function trees, settings (T tier only), connectors and webhooks, authenticated by tenant API keys with `admin:*` scopes and step-up for key creation; every call audited.

**FR-P18-96 — ITSM sync (IMP-133).** See FR-P18-91; round-trip status mapping configurable per tenant.

**FR-P18-97 — No mandatory endpoint agent (IMP-134).** Core features never require software installed on client endpoints; the on-premises agent (P19) is optional and only for NAS/disk storage targets or isolated systems.

**FR-P18-98 — Reversible imports (NN-49).** Every inbound bulk import through a connector (records created or updated) is a single change set with a 24-hour undo window (`int.import.undo_window_hours`, T, default 24, max 168); undo applies compensating changes and is audited; items already approved by a checker are listed and require explicit confirmation to revert.

**FR-P18-99 — Fewer clicks for global groups.** Connector templates can be cloned across legal entities in the same cell with entity-specific credentials, reducing set-up for multi-entity groups to one wizard plus per-entity consent.

### 4W. API-first onboarding and KYB adapters *(v1.2; D-56; consumed by P01 §4H)*

**FR-P18-100 — Port set (renaming and split).** The onboarding ports used by P01 FR-P01-54 to FR-P01-76 are implemented here; v1.0 adapter interfaces are renamed so that every phase uses one name:

| v1.2 port | Replaces | Operations | Adapters (candidates; contract and DPA before use) |
|---|---|---|---|
| `COMPANY_DATA_PORT` | `CompanyRegistryProvider` | `byCin(cin)`, `byLlpin(llpin)`, `byPan(pan)` (where licensed), `searchName(name, state)`, `directors(cin)`, `charges(cin)`, `groupHints(cin)`, `msme(udyamNo)` | Licensed MCA-data aggregators: Surepass, Signzy, Probe42, Perfios/Karza, AuthBridge, Zoop, Gridlines [VERIFY data rights for display and storage]; no MCA21 scraping |
| `IDENTITY_PORT` | PAN part of `TaxIdProvider` | `verifyPan(pan, name)` → status, name-match score | Protean (NSDL) PAN verification for eligible users, or a licensed aggregator [VERIFY eligibility] |
| `GSTIN_PORT` | GSTIN part of `TaxIdProvider` | `byGstin(gstin)`, `byPan(pan)` → all GSTINs, `placesOfBusiness(gstin)` | GST Suvidha Providers (e.g. Vayana, IRIS) or aggregator |
| `LEI_PORT` | `LeiProvider` | `byLei(lei)`, `searchName(name, country)`, `directParent(lei)`, `ultimateParent(lei)`, `children(lei)` | GLEIF API (free, no key) |
| `REGISTER_LOOKUP_PORT` | FR-P18-34 manual datasets | `match(registerCode, regNo | name+state)`, `snapshot(registerCode)` | Official public registers ingested as snapshots (FR-P18-102); EPFO establishment search behind flag `onb.epfo_lookup.enabled` (OFF, OI-P01-19) |
| `ESIGN_PORT` | `ESignProvider` | unchanged (signatory confirmation, P01 FR-P01-65) | Aadhaar eSign through ASPs using CCA-empanelled ESPs; DSC |

Every adapter returns the normalised schema `ldc.onboarding.entity.v1` (JSON Schema in `contracts/onboarding/`): a list of fields `{key, value, source, provider, retrieved_at, confidence EXACT|DERIVED|INFERRED, evidence_hash}` plus `provider_status`, `cost_units` and `raw_hash`. Provider-specific payloads never leave the adapter. Contract tests per adapter run against recorded fixtures (PII synthesised); live calls are impossible outside production (`provider_routing`, FR-P00-10).

**FR-P18-101 — Waterfall, resilience and cost.** Per port an ordered provider list (P01 setting `onb.discovery.provider_order.*`). Each call: 8 s timeout; a hedged request to the next provider when the first has not answered in 4 s and the field set is critical (name, status, constitution); circuit breaker per provider (5 failures in 60 s opens for 120 s; half-open probe); idempotency per `(identifier, purpose, cache window)` so retries never double-bill. Raw responses are stored encrypted for 30 days (dispute window) and then deleted; only normalised fields are kept (data minimisation; Digital Personal Data Protection Act 2023 s.8(7)). Every paid call is metered in `int.lookup_costs`; field-level agreement between providers is scored in `int.provider_quality` (agreement rate, stale-field rate, latency p95) and shown on the super-admin dashboard so the platform can reorder providers on evidence.

**FR-P18-102 — Register snapshot ingestion (`REGISTER_LOOKUP_PORT`).** Temporal workflow `RegisterSnapshotIngest` per register: download the published file or page from the official source (RBI list of NBFCs registered with RBI, RBI list of ARCs, RBI lists of scheduled banks and UCBs, RBI's NBFC Upper Layer list from its press release, SEBI registered intermediaries, IRDAI lists of insurers and intermediaries, IFSCA registered entities, Central Registrar of Co-operative Societies list of multi-State co-operative societies, State registrar lists where published) → store the file with SHA-256 → parse with a versioned parser → normalise (`register_code`, `reg_no`, `name`, `normalised_name` with legal-suffix folding, `state`, `category`, `classification` as published, `status`, `as_on`) → diff against the previous snapshot → publish. Refresh daily for RBI, SEBI, IRDAI and IFSCA lists, weekly for others. A parser schema change or a diff above 5 % of rows holds the snapshot for content-checker sign-off. Matching uses exact registration number first, then trigram similarity on normalised name plus State (score shown; below 0.85 the match is a suggestion only). Only public, unauthenticated pages and files are used; site terms and robots rules are recorded per source (`int.register_sources.terms_checked_on`). A change affecting a tenant's own entry (status cancelled, layer changed, name changed) raises an Updates item and a task for the tenant (P01 FR-P01-73).

**FR-P18-103 — Partner and bulk onboarding endpoints.** `POST /v1/onboarding/requests` (scopes `onb.request:create` for Finbyx, Udofin, Ops Hub and approved channel partners; body: identifiers, consent artefact reference, partner reference, intended plan) creates a discovery session and returns a signed prefill link for the client's signatory; no tenant is created until a person at the client confirms (P01 FR-P01-68). Webhook `onboarding.session.completed` returns the outcome and, once confirmed, the tenant code. `POST /v1/onboarding/bulk` (practitioner firms, ≤ 500 rows, CSV/XLSX template `LDC-DT-ONB-v1`) runs discovery per row with partial results and a downloadable exceptions file.

### 4X. Public API, webhooks and MCP by business ID *(v1.2; D-51, D-53, NN-56, NN-57)*

**FR-P18-104 — Business-ID-addressable resources.** Every resource that has a business ID (Appendix B §B.12) can be read by it; ULID paths continue to work and every response carries both `id` and `biz_id`:

| Method and path | Returns | Scope |
|---|---|---|
| `GET /v1/bizids/{bizId}` | Resolve any ID or alias (P00 FR-P00-77) | any read scope |
| `GET /v1/compliances/{compId}` | Library item (platform version pinned for the tenant) + tenant overlay + applicability decision + list-view fields + chips (next due, days to due, RAG) | `cmp.obligation:read` |
| `GET /v1/compliances/{compId}/instances?from=&to=&status=&entity=` | Instances of the CompID | `cmp.instance:read` |
| `GET /v1/compliances/{compId}/instances/{period}[/{entity}]` | One instance by reference (`RBI-NBFC-GOV25-0042` + `2026-Q3`) with maker, checker, auditor and evidence summary | `cmp.instance:read` |
| `GET /v1/risks/{riskId}` · `/kris` · `/controls` | Risk with ratings, owner, treatment, links | `erm.risk:read` |
| `GET /v1/kris/{kriId}` · `GET /v1/controls/{ctlId}` | KRI with latest values; control with test results | `erm.kri:read`, `erm.control:read` |
| `GET /v1/gov/{govId}` | Governance item (meeting, agenda item, minutes, resolution, register entry, filing, policy, committee, director/KMP event, declaration) | `gov.item:read` |
| `GET /v1/history/{bizId}` | Timeline (P00 FR-P00-76) | `core.history:read` |
| `GET /v1/links?bizId=` | Cross-ID links both directions (P00 FR-P00-78) | read scope of both ends |

Alias requests return the canonical record with `Content-Location` set to the canonical path and `resolved_from` in the body. RETIRED, MERGED and VOID IDs return 200 with `state` and `successor`; any write returns LDC-CORE-122. An ID the caller cannot see returns 404 LDC-CORE-031 exactly as for a missing one.

**FR-P18-105 — Stars, conversations and accountability by ID (façade over P04, P06, P08).** `PUT /v1/me/stars/{bizId}` (label, reminder date) and `DELETE …`, `GET /v1/me/stars`; `GET /v1/compliances/{compId}/conversations`, `POST /v1/compliances/{compId}/instances/{period}/conversations` (typed message: QUERY, EXPLANATION_REQUEST, GUIDANCE_REQUEST, NOTE, DECISION — rules, SLAs and visibility per P04), `POST /v1/conversations/{threadId}/messages`, `POST /v1/conversations/{threadId}:resolve`; `GET /v1/compliances/{compId}/instances/{period}/accountability` (computed timeline, NN-60); equivalent `/v1/risks/{riskId}/conversations` and `/v1/gov/{govId}/conversations`. A token always posts as its own principal: user tokens as the user; service accounts only NOTE messages labelled "via <integration>"; no API can post as another person or edit a sent message after the 5-minute window (NN-59). Canonical internal paths and payloads are those of P04 §7.3; this façade adds no rules.

**FR-P18-106 — List and export by API.** `GET /v1/compliance-list?view=&filter=&sort=&group_by=&fields=&cursor=` returns the nine list-view columns plus chips by default (D-50) and any field by key; `POST /v1/exports` exposes the P04 export builder (filter, group-by up to three levels, columns, XLSX/PDF/CSV, schedule) asynchronously with webhook `export.ready`; scope `cmp.export:create`. Each export is a ledger event per CompID in scope (NN-57).

**FR-P18-107 — Webhooks keyed by business ID.** Payloads for compliance, risk and governance topics carry `biz_id` and, for instances, `instance_ref`. Subscriptions can filter by ID prefix (`comp_id_prefix=RBI-NBFC-GOV25-`), department, RAG transition and message type. New topics: `compliance.rag_changed`, `compliance.explanation_requested`, `compliance.guidance_requested`, `compliance.conversation.message_created`, `compliance.accountability_recorded`, `risk.rating_changed`, `risk.kri_breached`, `gov.item_completed`, `bizid.retired`, `bizid.continued`, `onboarding.session.completed`, `export.ready`. Payloads follow the minimum-necessary rule (no message bodies; a link and the message type only).

**FR-P18-108 — Business ID on ecosystem events.** Ecosystem events that concern a compliance, risk or governance item (for example `ObligationPublished`, `ControlEvidenceCollected`, risk-feed events to Finbyx) carry the CloudEvents extension attribute `ldcbizid` (and `ldcinstref` for instances) so that Finbyx, Udofin, Equator and the Ops Hub can show and deep-link the same ID. CloudEvents permits extension attributes; registering them in the Ecosystem Spec is raised as a v1.2 change request, and receivers that ignore unknown extensions are unaffected.

**FR-P18-109 — MCP tools and resources by ID.** Added to the `ldc-mcp` catalogue (Appendix AA §AA.7; same permission parity, NN-52): resources `ldc://compliances/{compId}`, `ldc://compliances/{compId}/instances/{period}`, `ldc://risks/{riskId}`, `ldc://gov/{govId}`, `ldc://history/{bizId}`; READ tools `find_by_id` (any ID or alias), `get_compliance`, `get_history`, `get_risk`, `get_governance_item`, `list_urgent` (the caller's Red and Amber items, D-54), `list_my_starred`; DRAFT tool `draft_conversation_message` (drafts a reply to an explanation or guidance request into the user's LDC drafts; never sends); INTERNAL_WRITE_LOW tool `star_item` (scope `mcp.reminder`, elicitation confirmation). Existing `get_obligation` and `search_obligations` accept CompIDs. Sending a message, accepting an assignment, recording an explanation or changing status are never MCP tools (NN-14, NN-52).

**FR-P18-110 — Enumeration protection.** Business IDs are sequential and therefore guessable; authorisation is checked on every request and invisible IDs return 404. More than 50 not-found ID lookups per minute from one client or token are throttled (429, LDC-INT-163) and raise a SIEM alert (P24); MCP and API anomaly rules (FR-P18-67) include ID enumeration.

**FR-P18-111 — SDK and OpenAPI.** ID formats are published as OpenAPI `pattern`s generated from `packages/bizid`; the TypeScript and Python SDKs offer `client.compliances.get("RBI-NBFC-GOV25-0042")`, `client.history.get(id)`, `client.stars.add(id)`; examples in the developer portal use business IDs.

**FR-P18-112 — Replying from Teams, e-mail and messaging.** Conversation notifications (P04 FR-P04-240 to FR-P04-242) are delivered as a Microsoft Teams adaptive card with Reply, Ask for more time and Open actions, and as e-mail with a signed per-thread reply-to address (`reply+<signed token>@reply.lawdocscomply.com`; the token binds thread, recipient and expiry; inbound mail must pass SPF, DKIM and DMARC alignment, otherwise the reply is held and the sender is told to reply in the app — LDC-WF-201). A reply is posted as the verified recipient with the channel recorded. Red-alert nudges on WhatsApp (Business Platform approved templates) and SMS (DLT-registered templates under TRAI's TCCCPR 2018) are opt-in per user, carry the business ID and a link only, never the compliance text.

---

### 4Y. IPB port catalogue, connector marketplace and Ecosystem events *(v1.3; IPB-01 §01.4.4, IPB-10; D-60; X-71)*

**FR-P18-113 — Ports named against the IPB catalogue (two adapters each).** The table below is binding on `packages/connectors` interface names; LDC aliases stay in documentation (X-71). "Reference" is the adapter live in production first; "Alternate" must pass the contract tests in CI before the port's phase exits (IPB-01 §01.3.C; one alternate per Tier-0 port live in CI — owner decision IPB #8).

| LDC port (alias) | IPB-01 port | Reference adapter | Alternate adapter(s) | Notes |
|---|---|---|---|---|
| `AI_PORT` | `LLM_PORT` (+ `EMBEDDING`, `RERANK`, `SPEECH`, `IMAGE_GEN`) | `bedrock_claude_in` | `azure_openai_in`, `gemini_vertex_asia_south1` (India band); `anthropic_direct`, `openai` (open band); `self_hosted_vllm` (sealed) | P17 §4Y; all non-reference OFF until verified |
| `IDENTITY_PORT` (users) | `IDENTITY_PORT` | Keycloak (`ldc`, `ldc-staff` realms) | Entra ID (staff federation), Auth0/Cognito contract-tested | SCIM, passkeys |
| `IDENTITY_PORT` (KYB), `COMPANY_DATA_PORT`, `GSTIN_PORT`, `LEI_PORT`, `REGISTER_LOOKUP_PORT` | `COMPANY_DATA_PORT`, `KYB_PORT` | licensed provider A (owner decision #24) | provider B; public registers (MCA, GSTN, GLEIF) as read-only fallback | no bureau pulls (X-07) |
| `STORAGE_PORT` | `STORAGE_PORT` | S3 (Object Lock) | Azure Blob (immutable), GCS (retention lock), MinIO (local), tenant BYO targets | P19 |
| `SEARCH_PORT` | `SEARCH_PORT` | OpenSearch | PostgreSQL FTS | — |
| `DOCGEN_PORT` | `DOCGEN_PORT` | docxtemplater + Gotenberg | self-hosted LibreOffice headless | PDF/A |
| `SECRETS` | `SECRETS_PORT` | AWS Secrets Manager/KMS | Vault; Azure KV; GCP SM; `env` (local only) | — |
| `BILLING_PORT` | `PAYMENTS_PORT` (wrapped; OH8 engine of record) | Razorpay hosted checkout via OH8 | PayU/Cashfree via OH8; Stripe (international) | X-02; SAQ A |
| `MESSAGING_PORT` | `NOTIFY_PORT`, `SMS_PORT`, `WHATSAPP_PORT` | SMTP/SES; DLT SMS provider A; Meta Cloud API | SendGrid/Postmark; SMS provider B; BSP (Gupshup/JioCX) | super-admin WhatsApp toggle; never collection or legal notices |
| `CALENDAR_PORT`, `WORKSPACE_PORT` | `CALENDAR_PORT`, `WORKSPACE_PORT` | Microsoft Graph | Google Calendar/Workspace; ICS/CalDAV | D-10 |
| `ESIGN_PORT` | `ESIGN_PORT` | ASP adapter A (CCA-empanelled ESP) | ASP adapter B; DSC | X-04 |
| `ACCOUNTING_PORT` | `ACCOUNTING_PORT` | Tally Prime export | Excel/CSV TB; Zoho Books | read-only |
| `LENDING_SYSTEM_PORT`, `ECOSYSTEM_PORT` | `ECOSYSTEM_BUS` | NATS CloudEvents bus (Spec v1.2) | HTTPS webhooks with Standard Webhooks | `int` only |
| `GRC_EXPORT_PORT` | product-specific | OSCAL JSON | REST | — |
| `MCP_SERVER`, `MCP_CLIENT`, `A2A_GATEWAY` | `MCP_SERVER`, `MCP_CLIENT`, `A2A` | `ldc-mcp` (OAuth 2.1) | — (protocol, not vendor) | `fut.mcp-server`, `fut.a2a-agent-card` |
| `TRUST_PORT` *(new)* | `TRUST_PORT` | OH14.6 feed | product-local cache | P24 §4M |
| `LAW_REGISTER_PORT` *(new; LDC provides)* | `LAW_REGISTER_PORT` | LDC Appendix G register (read-only HTTP) | product-local JSON snapshot | consumed by all products |
| `CRM_PORT`, `HR_PORT` *(new)* | `CRM_PORT`, `HR_PORT` | Operations Hub OH3/OH10 | CSV dead-letter to Hub import | public forms |
| `TAG_MANAGER_PORT`, `ANALYTICS_PORT` *(new)* | same | `none` / first-party analytics (India) | GTM web; server-side tagging | NN-62; owner decision #30 |
| `FEATURE_FLAG_PORT` *(new)* | `FEATURE_FLAG_PORT` | OpenFeature file provider (local) / Unleash | Flagsmith | P24 |
| `DNS_CDN_PORT` *(new)* | `DNS_CDN_PORT` | AWS Route 53 + CloudFront/ACM | Cloudflare | white-label hosts |
| `REG_INTEL_PORT`, `FX_RATE_PORT`, `ENTITY_REGISTRY_PORT`, `LITIGATION_DATA_PORT`, `CONTRACT_REPO_PORT`, `ESG_DATA_PORT`, `ENERGY_EHS_PORT`, `ITSM_PORT`, `AI_MONITORING_PORT` | registered as supplementary ports (IPB-01 §01.4.4.3) | per v1.1 phase files | second provider or file import | flags OFF until licensed |

**FR-P18-114 — Connector marketplace (IPB-10 §10.4.6).** The tenant connector catalogue (FR-P18-55) and certification (FR-P18-54) adopt the IPB manifest schema: `connector_id`, `publisher`, `version`, `category`, `ports_used[]`, `scopes_requested[]`, `data_classes[]`, `data_egress` (bool, destinations, residency), `webhooks[]`, `settings_schema`, `support`, `attestations` (VAPT date, DPA ref, sub-processor statement). Install flow: permission preview (what data moves, in which direction, where it lives) → `ten_admin` approval (maker-checker when `data_egress = true`, `int.mc_threshold`) → sandbox test → enable; uninstall revokes tokens and lists retained data with the deletion date. The reference connector set of IPB-10 §10.4.6.2 that applies to LDC: Microsoft 365, Google Workspace, Slack/Teams notifications, Jira/ServiceNow (`ITSM_PORT`), Tally, SFTP batch, generic webhook, OH CRM. Certified third-party connectors appear with publisher attestation dates; an expired VAPT (> 12 months) suspends new installs (`LDC-INT-207`).

**FR-P18-115 — Ecosystem events LDC produces or consumes (registered in Ecosystem Spec v1.2 §3; master §19 items 15–26).** All carry the CloudEvents envelope of IPB-10 §10.4.9 with `dataregion` and `source = urn:infrabyx:ldc:<tenantid>`; published only by `int` (X-01).

| Event | LDC role | Minimum `data` | Where raised |
|---|---|---|---|
| `in.infrabyx.trust.VendorAssuranceDocumentPublished.v1` | consumer | `vad_id`, `title`, `category`, `cadence`, `valid_from`, `valid_until`, `storage_ref`, `hash_sha256`, `visibility` | P24 §4M mirror |
| `in.infrabyx.feedback.FeedbackSubmitted.v1` | producer | `fbk_id`, `product=LDC`, `tenant_id`, `module`, `release`, `severity`, `category`, `summary`, `attachments_count` | P23 FR-P23-227 |
| `in.infrabyx.crm.LeadCaptured.v1` | producer | `lead_id`, `product`, `brand_id`, `source`, `consent_ref`, `utm?`, `contact_hash`, `fields_ref` | P23 §5.7, forms |
| `in.infrabyx.vidhi.VidhiTaskDelegated.v1` | producer/consumer (flag OFF) | `msn_id`, `from_product`, `to_product`, `task_type`, `tenant_id`, `requested_by`, `autonomy_ceiling`, `due_at`, `inputs_ref` | P17 §4T |
| `in.infrabyx.tenancy.WhiteLabelTenantProvisioned.v1` | consumer | `tenant_id`, `brd_id`, `hosts[]`, `legal_entity_ref`, `plan_id`, `email_domain`, `provisioned_by` | P02 FR-P02-92 |
| `in.infrabyx.consent.MarketingConsentUpdated.v1` | producer/consumer | `consent_id`, `principal_hash`, `purpose`, `state`, `channel`, `notice_version`, `occurred_at` | P01 ledger; P23 §4O |
| `in.infrabyx.messaging.WhatsAppTemplateApproved.v1` | consumer | `template_name`, `waba_id`, `brand_id`, `language`, `category`, `status`, `approved_at` | §4J |
| `in.infrabyx.cms.BlogPostPublished.v1` | producer | `pst_id`, `product`, `brand_id`, `title`, `slug`, `url`, `author_type`, `tags[]`, `published_at`, `ai_assisted` | P23 §4W |
| `in.infrabyx.cms.ResourcePublished.v1` | producer/consumer | `res_id`, `product`, `brand_id`, `title`, `type`, `url`, `gated`, `published_at` | P23 §4W; P17 notebooks |
| `in.infrabyx.eng.ReleaseNotePublished.v1` | producer | `rel_id`, `product`, `version`, `channels[]`, `audiences[]`, `regulatory_tags[]`, `url`, `published_at` | P24 §4M |
| `in.infrabyx.grc.PolicyEffective.v1`, `in.infrabyx.grc.PolicyAttested.v1` | producer | `key`, `version_label`, `effective_at`, `reconsent`, `product`; acceptance: `user_hash`, `key`, `version_label`, `at` | P23 FR-P23-226 |
| `in.infrabyx.content.GlossaryEntryPublished.v1` | producer | `key`, `term`, `definition`, `law_refs[]`, `reviewer_of_record`, `published_at` | P23 FR-P23-233 |
| `in.infrabyx.eng.ExportMapBumped.v1`, `in.lawdocscomply.eng.PostmortemPublished.v1` (product-internal per IPB-09 §09.4), `in.infrabyx.grc.VulnerabilityRecorded.v1` (canonical; Spec v1.2 §6.15 — `security.VulnerabilityRecorded` is superseded, §6.17), `in.lawdocscomply.platform.BomGenerated.v1` (product-internal per IPB-01 §01.6), `in.infrabyx.platform.ExitDrillCompleted.v1` | consumer (GRC evidence for LDC's own controls) | per IPB-09/02/01 | P24, P12 |

**FR-P18-116 — API conventions confirmed (IPB-10 §10.3.A–C).** `/v1` resources, kebab-case paths, `ldck_` API-key prefix (`ldck_live_`, `ldck_test_`), RFC 9457 `application/problem+json` with LDC error codes in `code`, cursor pagination (`page[after]`, `page[size]`), `Idempotency-Key` on every POST, `ETag`/`If-Match` on PATCH, scopes `read:obligations`, `write:evidence`, `export:*` and partner client credentials; Standard Webhooks headers (`webhook-id`, `webhook-timestamp`, `webhook-signature`) with the IPB retry schedule and a webhook designer (endpoint, secrets rotation, event filter, delivery log, replay). Breaking changes are a new major with dual-run and sunset headers.

**FR-P18-117 — MCP exposure rules (IPB-10 §10.4.8.2).** `ldc-mcp` exposes only tools generated from kernel skill manifests (P17 §4Y) with read scopes by default; write tools above `INTERNAL_WRITE_LOW` need URL-mode step-up; sealed classes are never returned; every tool call is ledgered with the delegating user; `fut.mcp-server` is per-tenant OFF until the tenant admin enables it in Settings › Integrations.

**FR-P18-118 — `LAW_REGISTER_PORT` (LDC as provider).** Read-only HTTP endpoints `GET /v1/law-register/instruments`, `/instruments/{id}`, `/citations:check` (batch) over Appendix G, with status (in force, amended, superseded, repealed), effective dates and successor links; used by every product's policy lint (`IPB-POL-004`) and "i" reference panel; rate-limited per product client; published as a connector with snapshot export (JSON) for product-local fallback. A cited instrument marked superseded returns the successor so the caller can offer a fix.

## 5. Workflows and state machines

### 5.1 Connector instance lifecycle (`int.connector_instances.state`)

```
AVAILABLE → REQUESTED (tenant admin) → PREREQUISITES_PENDING (consents, keys, agent, DPA)
→ CONFIGURED (mapping pack + overrides, maker) → APPROVED (checker; CISO for ≥ CONFIDENTIAL outbound)
→ TESTING (sandbox or test window; certification checks for third-party)
→ ACTIVE ⇄ DEGRADED (health failures; auto) → SUSPENDED (kill switch, key expiry, link expiry, residency fail)
→ DISCONNECTING (drain outbox, final reconciliation, revoke tokens, export mapping history) → DISCONNECTED
```
Guards: residency verification for any connector that stores tenant data outside LDC; `re_grc_link`/link active; certification valid; keys valid ≥ 7 days (warn 30 days ahead).

### 5.2 Outbound event delivery (per subscription)

```
outbox row → relay picks (FIFO per subject) → envelope build + sign (RFC 9421 for ecosystem; Standard Webhooks HMAC for tenant webhooks)
→ POST → 2xx: DELIVERED (store response code, latency)
       → 4xx (except 408/429): FAILED_PERMANENT → DLQ + alert (no retry)
       → 408/429/5xx/timeout: RETRY (exponential back-off with jitter, max 72 h) → DLQ + alert
DLQ → replay requested (maker) → approved (checker) → re-enqueue (same event id)
```

### 5.3 Inbound event processing

```
receive → verify signature + timestamp (±5 min) + mTLS identity → validate schema (registry version) → check consentref/legalbasis, dataclass ≤ ceiling, reid mapped
→ inbox insert (source,id) [duplicate → 200 no-op] → ordering check (seq) [gap → park 15 min → catch-up GET /v1/events] → handler (module) → ack
handler failure → retry (internal) → poison → inbox DLQ + integration incident
```

### 5.4 Compliance-mode switch (`re_grc_link` mode change)

```
PROPOSED (either side) → APPROVED_RE (CCO maker, CISO/MD checker) → APPROVED_COUNTERPART
→ EXPORTING (outgoing system: obligations, controls, open issues, evidence index + hash heads)
→ IMPORTING (incoming: validate, map, reconcile counts and hash heads) → DUAL_PUBLISHING (one compliance period)
→ CUTOVER (effective date) → RECONCILED (signed report) → CLOSED
failure at any step → ROLLBACK (outgoing remains authoritative; no data deleted)
```

### 5.5 Calendar sync (native)

```
LDC item created/changed (deadline, task due, meeting) → visibility resolver (who sees it) → per subscribed user: upsert event in "LawDocsComply" calendar (idempotent by ldc_item_id + user)
user changes LDC-owned event in their calendar → change notification → if kind = MEETING created from LDC: sync RSVP; else: revert time and annotate "Statutory/assigned date is managed in LawDocsComply"
token expiry/consent revoked → mark sync BROKEN → notify user once; fall back to ICS link suggestion
```

### 5.6 Onboarding lookup (PAN/CIN)

```
user enters PAN or CIN + consent checkbox (notice text) → rate-limit + bot check → provider call(s) in parallel (registry, GSTIN, LEI) with 5 s budget
→ normalise → show fields with source + time → user confirms/edits → onboarding_snapshot stored (masked PAN token) → applicability proposal (P15) → tenant confirms
provider timeout → partial results + manual entry; never block onboarding
```

### 5.7 Register snapshot ingestion *(v1.2)*

```
schedule (daily RBI/SEBI/IRDAI/IFSCA; weekly others) → download official file/page → SHA-256 → parse (versioned parser)
→ normalise → diff vs previous → diff ≤ 5 % and parser unchanged ? publish : HOLD for content-checker sign-off
→ publish snapshot version → re-match tenants' registered entities → changes to a tenant's own entry → Updates item + task (P01 FR-P01-73)
download or parse failure → keep previous snapshot (stale badge with date) → alert content ops after 2 consecutive failures
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-INT-01 | Integrations home (catalogue) | Settings → Integrations | Cards by category; status badges; "what data moves" panel |
| SCR-INT-02 | Connector setup wizard | Settings → Integrations → [connector] → Connect | Prerequisites, consent, mapping preview, test, approval request |
| SCR-INT-03 | Connector detail and health | Settings → Integrations → [instance] | Health, logs (metadata), reconciliation, keys, kill switch |
| SCR-INT-04 | Ecosystem links | Settings → Integrations → Infrabyx ecosystem | `re_grc_link` status, compliance mode, switch wizard, grants federation |
| SCR-INT-05 | API clients | Settings → Integrations → API clients | Register/approve clients, scopes, keys, expiry |
| SCR-INT-06 | Webhooks | Settings → Integrations → Webhooks | Subscriptions, secrets rotation, test event, delivery log, DLQ replay (maker-checker) |
| SCR-INT-07 | Mapping packs | Settings → Integrations → Mappings | Versions, tenant overrides (maker-checker), golden fixture results, Vidhi mapping proposals |
| SCR-INT-08 | On-premises agents | Settings → Integrations → Agents | Install token, heartbeat, version, jobs |
| SCR-INT-09 | Workplace and SSO | Settings → Security → Single sign-on & provisioning | IdP config, SCIM token, group mapping, suite capability matrix |
| SCR-INT-10 | My calendar connection | User menu → Calendar sync | Choose native/ICS/CalDAV, privacy mode, reminder lead times, status |
| SCR-INT-11 | Channels | Settings → Communications | Email domains (DKIM/SPF/DMARC checks), SMS DLT headers/templates, WhatsApp BSP, voice numbers, quiet hours defaults |
| SCR-INT-12 | Website and app embeds | Settings → Grievance & help → Embeds | Snippets, hosted page domain, allowed origins, branding, preview, accessibility check |
| SCR-INT-13 | eSign providers | Settings → Documents → eSign | Provider connection, signature types, IT Act exclusions list, test envelope |
| SCR-INT-14 | Integration monitor (tenant) | Settings → Integrations → Monitor | Lag, errors, DLQ, reconciliation |
| SCR-CON-INT-01 | Platform connector catalogue | Console → Integrations → Catalogue | Certification, versions, kill switches |
| SCR-CON-INT-02 | Platform integration monitor | Console → Integrations → Monitor | Cross-tenant metadata only |
| SCR-CON-INT-03 | Certification workbench | Console → Integrations → Certification | Submissions, suite results, sign-off |
| SCR-DEV-01…08 | Developer portal | developers.lawdocscomply.com | Home, guides, API reference, events, SDKs, sandbox, clients, changelog |

UX: every setup shows *what will happen*, *who must approve*, and *how to undo*. Secrets are shown once with copy-to-clipboard and auto-masking. Health problems surface in context (e.g. a banner on the Calendar screen if sync is broken). "i" help keys: `help.int.scopes`, `help.int.webhook_signatures`, `help.int.mapping_pack`, `help.int.agent`, `help.int.compliance_mode`, `help.int.ics_privacy`, `help.int.dlt`, `help.int.embed`.

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-AI-24 | External AI access (MCP server) | Settings → Integrations → AI assistants | Owned jointly with P17; client allow-list, scope ceiling, basis, access log |
| SCR-AI-25 | External MCP servers (client) | Settings → Integrations → MCP servers | Tool admission, pinned hashes, suspensions |
| SCR-INT-20 | A2A peers and Agent Cards | Settings → Integrations → Agent connections | Peer allow-list, contract map, traffic (flag OFF until Spec v1.2) |
| SCR-INT-21 | Issue sync (ITSM) | Settings → Integrations → Jira / ServiceNow / Freshservice | Status mapping, test round trip |
| SCR-INT-22 | Admin API keys | Settings → Integrations → Admin API | Scoped keys, step-up, last use |
| SCR-INT-23 | Licensed intelligence providers | Console → Content → Intelligence feeds | Licence rights, jurisdictions, latency |
| SCR-INT-24 | Court and notice data | Settings → Integrations → Litigation data | Provider, matter mapping, notice mailbox |
| SCR-INT-25 | ESG data sources | Settings → Integrations → ESG data | Templates, meters, factor library version |
| SCR-INT-26 | Contract repositories | Settings → Integrations → Contracts | Folder/CLM mapping, extraction queue |
| SCR-INT-27 | Cell and routing (platform) | Console → Platform → Cells → Routing | Per-cell endpoints, readiness gate checklist |

**v1.2 screens** *(v1.2)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-INT-28 | Onboarding providers and quality (platform) | Console → Integrations → Onboarding providers | Provider order per port, circuit-breaker state, latency, agreement rate, cost per lookup, monthly spend, quota usage by tenant |
| SCR-INT-29 | Register snapshots (platform) | Console → Content → Registers | Per register: last snapshot, rows, diff, held snapshots awaiting sign-off, parser version, source terms check date |
| SCR-INT-30 | API and webhooks by ID (developer portal) | Developer portal → Business IDs | ID formats, resolver playground, webhook topic catalogue with ID filters, MCP tool list |

---

## 7. Backend design

### 7.1 Modules touched

`int` (owner); `iam` (Keycloak clients, SCIM, consent); `core` (outbox, ledger, KMS); `cfg` (mapping-pack overrides, settings); consumers in `cmp`, `wf`, `gov`, `pol`, `dms`, `erm`, `ral`, `aud`, `ret`, `acc`, `dpc`, `hr`, `grv`, `coop`, `ai`, `xpt`, `bil`, `mkp`, `sdc`, `web`.

### 7.2 Tables (schema `int`)

| Table | Key columns |
|---|---|
| `int.connectors` (platform) | connector_id (`[counterparty]-[capability]-ldc`), version, category, manifest_json, capabilities[], scopes[], data_classes[], residency, certification_state, certified_at, recert_due |
| `int.connector_instances` | instance_id, tenant_id, connector_id, version, state, config_ref (vault), mapping_pack_version, owner_user_id, approved_by, approved_at, health_state, last_success_at |
| `int.mapping_packs` / `int.mapping_overrides` | pack_id, version, yaml_ref, sha256; tenant overrides with patch version, maker, checker |
| `int.clients` | client_id, tenant_id (nullable for ecosystem), type (ECOSYSTEM, CERTIFIED, TENANT, DELEGATED, EMBED), owner, purpose, scopes[], data_class_max, auth_method, jwks_uri, cert_thumbprint, allowed_origins[], ip_allowlist[], expires_at, status |
| `int.client_tenant_consents` | client_id, tenant_id, scopes[], granted_by, granted_at, revoked_at |
| `int.links` | link_id, kind (RE_GRC, RE_LSP, TENANT_LINK, GROUP_GRANT_REF, EXTERNAL_ACCESS_REF), counterpart_product, counterpart_tenant, reid, mode, valid_from, valid_to, approvals_json, state |
| `int.webhook_subscriptions` | sub_id, tenant_id, url, event_types[], data_class_max, secret_ref (versions), status, created_by |
| `int.deliveries` | delivery_id, sub_id/link_id, event_id, attempt, status, http_status, latency_ms, next_attempt_at |
| `int.inbox` | source, event_id, business_key, received_at, processed_at, status |
| `int.dlq` | dlq_id, direction, ref, reason, first_failed_at, replay_request_id |
| `int.replay_requests` | request_id, scope_filter_json, requested_by, approved_by, state |
| `int.event_type_map` | internal_type, ecosystem_type, direction, transform_ref |
| `int.agents` | agent_id, tenant_id, device_cert_thumbprint, os, version, last_heartbeat, status |
| `int.agent_jobs` | job_id, agent_id, kind (TALLY_EXTRACT, DB_EXTRACT, STORAGE_PUT, CIC_SFTP, DSC_SIGN), schedule, last_run, status |
| `int.workplace_profiles` | tenant_id, suite (M365, GOOGLE, OTHER, NONE), plan_sku, capabilities_json, residency_evidence_ref, admin_consent_at |
| `int.calendar_connections` | user_id, mode (NATIVE_M365, NATIVE_GOOGLE, ICS, CALDAV), token_ref, privacy_mode, status, last_sync_at |
| `int.ics_feeds` | feed_id, user_id, token_hash, scope_json, created_at, rotated_at, revoked_at |
| `int.channel_configs` | tenant_id, channel (EMAIL, SMS, WHATSAPP, VOICE, RCS, PUSH), provider, sender_ids, dlt_entity_id, templates_json, status |
| `int.embed_configs` | tenant_id, kind (GRIEVANCE, HELP, DISCLOSURE), publishable_key, allowed_origins[], hosted_domain, branding_json, languages[] |
| `int.onboarding_lookups` | lookup_id, tenant_or_lead_id, input_kind (PAN, CIN, LLPIN, GSTIN, LEI, NAME), provider, consent_ref, result_ref, created_at (results retained per P01 retention) |
| `int.reconciliation_reports` | link_id, business_date, sent_count, ack_count, hash_sent, hash_ack, breaks |

### 7.3 APIs

Full catalogue in Appendix L §L.3. Platform-owned P18 endpoints:

| Method & path | Purpose |
|---|---|
| `GET /v1/events?after=&types=&limit=` | Catch-up feed of LDC-produced events (per client scopes) |
| `POST /v1/webhooks/inbound/{link_id}` | Ecosystem push receiver (RFC 9421 + Standard Webhooks) |
| `GET/POST/PATCH/DELETE /v1/webhook-subscriptions` | Tenant webhooks |
| `POST /v1/webhook-subscriptions/{id}/test` | Test event |
| `GET /v1/grc/obligations?updated_since=` | Ecosystem pull (Spec §6.22) |
| `GET /v1/grc/kris?updated_since=` | Ecosystem pull (Spec §6.22) |
| `POST /v1/external-access/grants`, `DELETE /v1/external-access/grants/{id}` | Federation receiver (Spec §4.7) |
| `GET /v1/provisioning/tenants/{org_id}/status`; `POST /v1/provisioning/tenants`; `POST /v1/provisioning/groups` | Provisioning |
| `GET /v1/entitlements` | Entitlements as applied (reconciled by OH8) |
| `POST /v1/imports/{kind}` (+ `/dry-run`, `/{id}/commit`, `/{id}/rollback`) | Migration imports |
| `POST /v1/onboarding/lookups` | PAN/CIN/GSTIN/LEI lookup (P01/P23 callers) |
| `GET /v1/calendar/feeds/{token}.ics` | ICS feed (served on `cal.` host) |
| `/scim/v2/Users`, `/scim/v2/Groups` | SCIM 2.0 |
| `POST /v1/embed/grievances`, `GET /v1/embed/grievances/{ref}/status` | Embed endpoints (publishable key + OTP) |
| `POST /v1/webhooks/payments/razorpay`, `/v1/webhooks/esign/{provider}`, `/v1/webhooks/channels/{provider}` | Provider callbacks |
| `GET /v1/integrations/health` | Tenant integration health |

### 7.4 Domain events

Ecosystem-facing (exact Spec names): `ObligationPublished` (produced), `ExternalAccessGranted/Used/Revoked` (produced for LDC-hosted slices), `UsageRecorded` (aggregates), `ModuleAttached`, `ModuleDetached`, `ReleasePublished`, `ControlEvidenceCollected`, `ConnectorCertified`, `ReconciliationBreakRaised`, `ExportRequested`, `ExportCompleted`, `StorageTargetConnected`, `BackupCompleted`, `RestoreTested` (P19 produces), `SecurityIncidentNotified` copies (P12 produces). Internal (`in.lawdocscomply.int.*`): `ConnectorInstanceStateChanged`, `WebhookDeliveryFailed`, `DlqReplayRequested`, `DlqReplayApproved`, `AgentRegistered`, `AgentHeartbeatMissed`, `CalendarSyncBroken`, `OnboardingLookupCompleted`, `ComplianceModeSwitchStateChanged`, `ApiClientApproved`, `ApiClientRevoked`, `SecretRotated`.

### 7.5 Jobs and Temporal workflows

`OutboxRelay` (continuous), `WebhookDeliveryWorker`, `InboxProcessor`, `GapCatchUp` (15-minute parking → producer catch-up), `DailyReconciliation` (06:00 IST counts/hashes per link; Spec §3.8), `MonthlyRiskFeedSampling`, `ComplianceModeSwitchWorkflow`, `CalendarFanOut` (per item change), `GraphSubscriptionRenewal`, `IcsTokenRotationReminder`, `KeyAndCertExpiryWatcher` (30/7/1-day warnings), `ConnectorHealthProbe` (5-minute), `RegistryDatasetRefresh` (content team schedule), `AgentUpdateRollout` (staged), `DeprecationUsageReport` (monthly), `SandboxReset` (nightly).

**Events and error codes added in v1.1** *(v1.1)*

| Event (`in.lawdocscomply.int.*` unless an ecosystem type applies, X-01) | Producer | Consumers | Key payload |
|---|---|---|---|
| `ExternalAiAccessed` | `int` (MCP server) | AI run ledger, tenant access log, SIEM | client_id, user_id, tool, args_hash, result_size, data_classes, cell |
| `McpClientApproved` / `McpClientRevoked` | `int` | audit, notify | client_id, scopes ceiling, basis |
| `McpToolSuspended` | `int` (MCP client) | `ai`, notify tenant admin | server_id, tool, old_hash, new_hash |
| `A2aTaskReceived` / `A2aTaskRejected` | `int` (A2A gateway) | run ledger, monitor | peer, task_type, contract_ref, reason |
| `CellRoutingChanged` | control plane | all cells, `xpt` | legal_entity_id, from_cell, to_cell, migration_id |
| `ConnectorImportUndone` | `int` | `cmp`, `dms`, audit | import_id, records_reverted, records_confirmed |
| `LegalMatterSignalReceived` | `int` (litigation data) | `lit` (P26) | matter_ref, court, stage, next_date |

| Code | Meaning | User message |
|---|---|---|
| LDC-INT-110 | MCP client not on tenant allow-list | "Your organisation has not approved this AI assistant. Ask your admin to approve it in Settings → Integrations → AI assistants." |
| LDC-INT-111 | MCP scope above tenant ceiling | "This assistant asked for more access than your organisation allows." |
| LDC-INT-112 | Tool requires URL-mode approval in LDC | "Open LawDocsComply to review and approve this action." |
| LDC-INT-113 | MCP rate limit reached | "Too many requests from your assistant. Try again in a minute." |
| LDC-INT-120 | A2A task has no mapped Ecosystem contract | "This agent request type is not supported." |
| LDC-INT-121 | A2A peer not allow-listed | "This agent connection is not enabled for your organisation." |
| LDC-INT-130 | Request reached the wrong cell | (307 redirect; no user message) |
| LDC-INT-131 | Destination outside home cell without transfer basis | "This connection would send data outside your data region. Record a transfer basis first." |
| LDC-INT-140 | Import undo window expired | "This import can no longer be undone automatically. Use a Correction Entry." |
| LDC-INT-150 | FX rate stale beyond limit | "Exchange rate unavailable for this date — the report cannot be approved until a rate is recorded." |

### 7.6 v1.2 backend additions *(v1.2)*

**Tables (schema `int`):**

| Table | Key columns |
|---|---|
| `int.lookup_requests` | id, session_ref (P01 onboarding session), port, provider, identifier_kind, identifier_token, purpose, consent_ref, requested_at, cache_hit |
| `int.lookup_results` | request_id, status (OK, PARTIAL, NOT_FOUND, ERROR, TIMEOUT), fields jsonb (normalised `ldc.onboarding.entity.v1`), raw_enc (deleted after 30 days), raw_hash, latency_ms |
| `int.lookup_costs` | request_id, provider, unit_cost, currency, billed_to (tenant or ANONYMOUS or PLATFORM), purpose, month |
| `int.provider_quality` | provider, port, month, calls, error_rate, p95_ms, field_agreement jsonb, stale_rate |
| `int.register_sources` | register_code, authority, url, format, refresh, parser_version, terms_checked_on, status |
| `int.register_snapshots` | id, register_code, version_date, row_count, file_sha256, diff_added, diff_removed, diff_changed, state (PUBLISHED, HELD, REJECTED), signed_off_by |
| `int.register_entries` | snapshot_id, register_code, reg_no, name, normalised_name, state, category, classification_as_published, status, as_on |
| `int.webhook_filters` | subscription_id, biz_id_prefix, department_codes[], rag_transitions[], message_types[] |

`int.onboarding_lookups` (v1.0) becomes a view over `int.lookup_requests` and `int.lookup_results`.

**APIs:** §4W and §4X tables; plus `GET /v1/platform/onboarding/providers` and `PATCH …/{port}` (order, enable; plt_super_admin with second approver), `GET /v1/platform/registers` and `POST /v1/platform/registers/{code}/snapshots/{id}:sign-off`.

**Events:** `in.lawdocscomply.int.RegisterSnapshotPublished.v1` (register, version, counts), `…int.RegisterSnapshotHeld.v1`, `…int.RegisterEntryChanged.v1` (tenant-matched changes only; consumed by iam re-verification), `…int.ProviderCircuitOpened.v1` / `…Closed.v1`, `…int.LookupQuotaExceeded.v1`, `…int.IdEnumerationSuspected.v1`.

**Jobs:** `RegisterSnapshotIngest` (per register), `ProviderQualityRollup` (daily), `RawLookupPurge` (daily; deletes raw payloads older than 30 days), `OnboardingBulkRun`.

**Errors:**

| Code | Meaning | User message |
|---|---|---|
| LDC-INT-160 | Provider not configured for this port | "Automatic look-up isn't available for this identifier yet. Please enter the details." |
| LDC-INT-161 | Provider circuit open; trying next provider | (no user message unless all fail — then LDC-IAM-122) |
| LDC-INT-162 | Register snapshot stale beyond limit | "The official list was last checked on {date}. Your result may be out of date." |
| LDC-INT-163 | Too many not-found ID look-ups (enumeration guard) | "Too many requests. Please wait a minute and try again." |
| LDC-INT-164 | Webhook filter pattern invalid | "That ID prefix isn't valid. Use the start of a CompID, RiskID or GovID." |
| LDC-INT-165 | Partner onboarding request without consent artefact | "Attach the client's consent reference to start onboarding." |
| LDC-INT-166 | Service account attempted a non-NOTE conversation message | "Integrations can only add notes to a conversation." |
| LDC-INT-167 | Snapshot held for sign-off; publication blocked | (platform) "Review the changes before publishing this register." |

---

## 8. Integrations (ports and adapters) — summary

Binding detail is Appendix L §L.5. Ports implemented in P18: `LmsConnector`/`LosConnector` (generic SDK), `AccountingSource`, `CompanyRegistryProvider`, `TaxIdProvider` (PAN, GSTIN), `LeiProvider`, `DigiLockerProvider`, `WorkplaceProvider`, `CalendarProvider`, `ESignProvider`, `EmailProvider`, `SmsProvider`, `WhatsAppProvider`, `VoiceProvider`, `ConversationalAgentProvider` (Haptik, flag), `PaymentGateway`, `AcademyProvider`, `OdrProvider` (Equator and others), `GrcThirdParty` (OSCAL; MetricStream, ServiceNow IRM, Archer, IBM OpenPages, Komrisk, Komply360, Compfie, TeamLease RegTech, Lawrbit, OnFinance — Spec §9.4), `StorageTarget` (framework here; targets in P19).

*(v1.2)* Onboarding ports are now named `COMPANY_DATA_PORT` (was `CompanyRegistryProvider`), `IDENTITY_PORT` and `GSTIN_PORT` (split of `TaxIdProvider`), `LEI_PORT` (was `LeiProvider`), `REGISTER_LOOKUP_PORT` (new) and `ESIGN_PORT` (was `ESignProvider`) — FR-P18-100; Appendix L §L.15.

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `int.webhooks.max_subscriptions` | G | 25 per tenant | 1–200 | platform |
| `int.webhooks.default_data_class_max` | G | INTERNAL | ≤ CONFIDENTIAL with CISO approval | platform / tenant CISO |
| `int.webhooks.retry_hours` | L | 72 | — | locked (Spec §3.4) |
| `int.idempotency.retention_hours` | L | 24 (168 for billing) | — | locked |
| `int.rate_limits.profile` | G | per client type | — | platform |
| `int.clients.secret_rotation_days` | G | 90 | 30–90 | platform |
| `int.clients.production_requires_admin_approval` | L | true | — | locked |
| `int.dlq.replay_requires_checker` | L | true | — | locked (NN-05) |
| `int.calendar.default_mode` | T | ICS (no suite) / NATIVE (suite connected) | enum | `ten_admin` |
| `int.calendar.write_to_primary` | T | false | bool | `ten_admin` (users may opt in if allowed) |
| `int.calendar.privacy_mode_default` | T | false | bool | `ten_admin` |
| `int.calendar.reminder_lead_times` | T | [7d, 1d, 2h] | up to 5 values | user |
| `int.ics.token_rotation_days` | T | 180 | 30–365 | `ten_admin` |
| `int.onboarding.lookup_providers` | G | ordered list | approved providers | platform |
| `int.onboarding.lookup_timeout_ms` | G | 5000 | 2000–10000 | platform |
| `int.embed.allowed_origins` | T | [] | valid HTTPS origins | `ten_admin` |
| `int.embed.hosted_domain` | T | `{slug}.care.lawdocscomply.com` | CNAME verified | `ten_admin` |
| `int.channels.whatsapp.enabled` | T | OFF | flag | `ten_admin` |
| `int.voice.ai_agent.enabled` | G→T | OFF | flag | platform enables, tenant opts in |
| `int.rcs.enabled` | G | OFF | flag | platform |
| `int.agent.auto_update` | T | true | bool | `ten_admin` |
| `int.compliance_mode.dual_publish_periods` | G | 1 | 1–3 | platform |
| `int.registry_datasets.refresh_days` | G | 30 | 1–90 | content team |
| `int.deprecation.public_api_months` | G | 12 | 6–24 | platform |
| `int.academy.sso_mode` | G | OIDC | OIDC / LTI13 | platform |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `int.mcp.server.enabled` | T | false | — | `ten_admin` |
| `int.mcp.client_allowlist` | T | empty | client metadata URLs | `ten_admin`, `ten_integration_admin` |
| `int.mcp.client_basis` | T | none | basis code per client | `ten_admin` + DPO note |
| `int.mcp.rate_limit_user_per_min` | G | 60 | 10–300 | platform |
| `int.mcp.rate_limit_tenant_per_day` | G | 10,000 | 1,000–200,000 | platform (plan-linked) |
| `int.mcp.evidence_draft.enabled` | T | false | — | `ten_admin` |
| `ai.mcp.client.enabled` | T | false | — | `ten_admin` |
| `int.a2a.enabled` | G | false | requires Spec v1.2 | `plt_super_admin` + checker |
| `int.a2a.peers_allowlist` | T | ecosystem peers | — | `ten_admin` |
| `int.health.alert_after_failures` | T | 3 | 1–10 | `ten_integration_admin` |
| `int.import.undo_window_hours` | T | 24 | 1–168 | `ten_admin` |
| `int.fx.source.<ccy>` | T | RBI/FBIL (INR), ECB (EUR), CBUAE (AED), MAS (SGD) | registered sources | `ten_admin` |
| `int.fx.max_staleness_days` | G | 3 | 1–10 | platform |
| `int.reg_intel.providers` | G | none | licensed adapters | `plt_content_publisher` |
| `int.litigation_data.provider` | T | MANUAL | MANUAL or licensed adapter | `ten_admin` |
| `int.itsm.enabled` | T | false | — | `ten_integration_admin` |

**v1.2 settings** *(v1.2)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `int.lookup.hedge_after_ms` | G | 4000 | 2000–8000 | `plt_super_admin` |
| `int.lookup.circuit.failures` / `.window_s` / `.open_s` | G | 5 / 60 / 120 | 3–20 / 30–300 / 30–900 | `plt_super_admin` |
| `int.lookup.raw_retention_days` | L | 30 | — | — |
| `int.registers.hold_diff_pct` | G | 5 | 1–20 | `plt_content_checker` |
| `int.registers.stale_after_days` | G | 7 (daily registers), 21 (weekly) | 2–60 | `plt_content_checker` |
| `int.registers.name_match_min` | G | 0.85 | 0.70–0.98 | `plt_content_checker` |
| `int.api.notfound_throttle_per_min` | G | 50 | 10–500 | `plt_security_officer` |
| `int.events.bizid_extension` | G | true | — | `plt_super_admin` |
| `int.mcp.bizid_tools.enabled` | T | true (when the MCP server is enabled) | — | `ten_integration_admin` |

---

## 10. Security, privacy and audit

- **Threats addressed** (STRIDE per connector in the threat model, Appendix Q): token theft (short-lived, sender-constrained tokens), replay (timestamps ±5 min, idempotency, nonces), SSRF (webhook URL validation, egress proxy with allow-list, private-range block), injection via mapping packs (declarative transforms only; no user-supplied code execution), malicious agent (signed binaries, outbound-only, least-privilege job definitions, remote disable), data exfiltration through webhooks (data-class ceilings, approvals for CONFIDENTIAL+), supply-chain (SBOM, dependency pinning, connector containers with read-only file systems and no shell).
- **Residency**: connectors that store LDC tenant data externally (storage targets, document mirroring, calendars with item titles) are checked for region (Spec §12.2); Google Workspace and personal calendars receive only titles/dates in privacy mode for regulated tenants by default (`int.calendar.privacy_mode_default = true` for RE families [REC]).
- **Secrets**: all third-party credentials in the vault (per-tenant KMS keys); never in configuration files, logs, events or exports; rotation reminders; automated rotation where providers support it.
- **Audit**: every connector state change, client approval, scope grant, consent, replay, mapping override and kill-switch action is a ledger event (NN-02). Delivery logs keep metadata only.
- **Privacy**: DPDP notices for onboarding lookups (purpose: verifying the organisation's identity and pre-filling the profile; data: business identifiers and director names/DIN as published; retention: life of the account or 90 days for abandoned sign-ups [REC]); no personal bureau data (FR-P18-33); Aadhaar never stored (NN-12).
- **Ecosystem**: certification evidence retained; `ConnectorCertified` and test results stored as control evidence (P24, Appendix Q).

---

## 11. AI touchpoints and guardrails

- V-SK-17 proposes mapping-pack field maps from sample files (column names, sample values, code lists) — a human approves; meaning-changing transforms need recertification.
- Vidhi explains integration errors in plain language from RFC 9457 problem details.
- Vidhi never receives connector secrets, tokens or raw webhook bodies containing personal data; it cannot create clients, approve consents or replay DLQs (NN-14).

---

## 12. Acceptance criteria (`tests/acceptance/p18/*.feature`)

```gherkin
Feature: Ecosystem contract conformance
  Scenario: ObligationPublished uses the ecosystem type
    Given a platform content update changes an obligation applicable to tenant T linked to Finbyx
    When the outbox relays the event
    Then the CloudEvent type is "in.infrabyx.grc.ObligationPublished.v1"
    And the source is "urn:infrabyx:ldc:<T>"
    And the request carries a valid RFC 9421 signature and Standard Webhooks headers

  Scenario: Duplicate inbound event is harmless
    Given LDC has processed EvidenceSubmitted with id E1 from Finbyx
    When the same event E1 is delivered again
    Then LDC responds 2xx
    And no second evidence record is created

  Scenario: Personal data without consentref is rejected
    When Finbyx sends an event with dataclass "PII" and neither consentref nor legalbasis
    Then LDC rejects it with problem "consent-missing"

  Scenario: Hub subject rejects personal data
    When LDC attempts to publish a UsageRecorded payload containing a user id
    Then the gateway blocks it with "dataclass-not-permitted"

Feature: Compliance-mode switch without data loss
  Scenario: EMBEDDED to LDC_EXTERNAL
    Given a Finbyx tenant with 1,240 obligations, 310 controls, 22 open issues and 9,800 evidence index entries
    When the CCO and CISO approve a switch to LDC_EXTERNAL effective next quarter
    Then LDC imports all records before the effective date
    And the reconciliation report shows equal counts and matching hash-chain heads
    And both systems publish evidence for one compliance period

Feature: Regulator portals are manual
  Scenario: No machine channel to RBI portals
    Given the codebase and configuration
    Then no HTTP client, credential or cookie store is configured for rbi.org.in portal domains
    And the RBI return connector capability is "PORTAL_MANUAL"

Feature: Onboarding lookup
  Scenario: CIN pre-fill with consent
    Given a prospect enters a valid CIN and accepts the lookup notice
    When the lookup runs
    Then legal name, constitution, incorporation date, registered address and directors with DIN are shown with provider and time
    And no director PAN or date of birth is stored

  Scenario: No bureau pull
    When a prospect completes onboarding
    Then no request is made to any credit information company

Feature: Calendar
  Scenario: ICS feed respects role scope
    Given user U in Treasury subscribes to her ICS feed
    Then the feed contains her tasks, her meetings and deadlines she follows
    And does not contain Credit department items she cannot view

  Scenario: Statutory dates are not changed from the calendar
    Given a deadline event written to U's Microsoft 365 calendar
    When U drags the event to a later date in Outlook
    Then LDC restores the original date and annotates the event
    And the obligation due date in LDC is unchanged

Feature: Webhooks and DLQ
  Scenario: Replay requires a second approver
    Given 12 deliveries to endpoint W are in the DLQ
    When admin A requests a replay
    Then the replay does not start until admin B approves
    And admin A cannot approve their own request

Feature: Grievance embed
  Scenario: Complaint from client website
    Given tenant T has allowed origin "https://www.nbfc-example.in"
    When a visitor submits a complaint through the embedded widget
    Then a grievance case is created in T's P14 desk with an acknowledgement reference
    And a submission from an origin not in the allow-list is rejected
```

NN tests: `NN-01_int_tenant_isolation_clients`, `NN-05_int_dlq_replay_checker`, `NN-08_int_no_portal_machine_channel`, `NN-12_int_no_aadhaar_storage`, `NN-23_int_contracts_only`, `NN-24_int_storage_residency`, `NN-30_int_no_ops_hub_tenant_data`, `NN-32_int_no_bodies_in_logs`.

```gherkin
Feature: v1.1 — MCP server, A2A, cells and new connectors

  Scenario: MCP never returns sealed data (NN-52)
    Given a POSH case exists in tenant T and the MCP server is enabled
    When an approved AI client calls search_obligations and list_due_items as the IC presiding officer
    Then no result contains any field of the POSH case
    And the sealed-class canary is absent from every MCP response in the CI run

  Scenario: Prohibited actions are not exposed
    When an AI client lists tools from ldc-mcp
    Then no tool can approve, attest, mark complied, sign, file, pay, publish or change access

  Scenario: MCP parity with REST permissions
    Given user U cannot read department D's instances through the REST API
    When U's AI client calls list_due_items
    Then no instance of department D is returned

  Scenario: Changed external tool description suspends the tool
    Given an approved external MCP tool with pinned description hash H
    When the server advertises a different description
    Then the tool is suspended, McpToolSuspended is emitted and Vidhi cannot call it

  Scenario: Unmapped A2A task is rejected
    Given int.a2a.enabled is true for tenant T
    When a peer sends a task type with no entry in int.a2a_contract_map
    Then LDC returns LDC-INT-120 and no action is taken

  Scenario: Request routed to the wrong cell
    Given entity E has home cell EU
    When a client calls api.in.lawdocscomply.com for E's records
    Then the response is 307 to api.eu.lawdocscomply.com and no data is served from the IN cell

  Scenario: Connector import can be undone
    Given a Tally import created 412 records 3 hours ago
    When the integration admin clicks Undo import
    Then compensating changes revert the 412 records, items already approved are listed for explicit confirmation, and the audit ledger records the undo

  Scenario: FX snapshot travels with the value
    Given a penalty exposure in AED is converted to INR for a group dashboard
    Then the stored value carries source, date and rate type, and re-rendering next month shows the same INR figure
```

```gherkin
Feature: API-first onboarding adapters (v1.2)
  Scenario: Slow primary provider is hedged without double billing
    Given COMPANY_DATA_PORT providers "A" then "B"
    And provider "A" has not answered after 4 seconds for CIN "U65999MH2019PTC123456"
    When the hedged request to "B" returns first
    Then the result is taken from "B" and "A" is cancelled
    And int.lookup_costs records one billable call per provider that answered

  Scenario: A large register change is held for review
    Given yesterday's RBI NBFC list snapshot has 9,400 rows
    When today's file parses to 8,600 rows
    Then the snapshot is HELD and SCR-INT-29 shows the diff for content-checker sign-off
    And onboarding continues to use yesterday's snapshot

Feature: API by business ID (v1.2)
  Scenario: Read a compliance instance by CompID and period
    Given a token with scope cmp.instance:read for tenant "RCPL"
    When the client calls GET /v1/compliances/RBI-NBFC-GOV25-0042/instances/2026-Q3
    Then the response contains biz_id "RBI-NBFC-GOV25-0042", instance_ref "RBI-NBFC-GOV25-0042/2026-Q3", status, next due date and RAG

  Scenario: Alias resolves to the canonical item
    Given legacy alias "NBFC-KYC-17" maps to "RBI-NBFC-KYC16-0017"
    When the client calls GET /v1/compliances/NBFC-KYC-17
    Then the response header Content-Location is "/v1/compliances/RBI-NBFC-KYC16-0017" and resolved_from is "NBFC-KYC-17"

  Scenario: Enumeration is throttled
    Given a client requests 60 non-existent RiskIDs within one minute
    Then requests after the 50th fail with LDC-INT-163 and a SIEM alert is raised

  Scenario: MCP cannot send a conversation message
    Given an external AI client with scopes mcp.read and mcp.draft
    When it calls draft_conversation_message for an explanation request on RBI-NBFC-GOV25-0042/2026-Q3
    Then a draft appears in the user's LDC drafts and no message is posted to the thread
```

---

```gherkin
# v1.3 — IPB-10 alignment (P18-AT-v13-01 … 04)
Feature: Connector install with data egress (P18-AT-v13-01)
  Scenario: Egress connector needs maker-checker and shows the preview
    Given connector "Jira Cloud" with data_egress = true
    When ten_admin installs it
    Then the permission preview lists every data class and destination region
    And a second approver is required before tokens are issued
  Scenario: Expired VAPT suspends installs
    Given a certified connector whose attestation VAPT date is 13 months old
    Then new installs are refused with LDC-INT-207 and existing instances show a warning

Feature: Ecosystem event envelope (P18-AT-v13-02)
  Scenario: Blog publication emits the registered event
    When a staff post is published on the public site
    Then in.infrabyx.cms.BlogPostPublished.v1 is emitted by int with source urn:infrabyx:ldc:<platform>, dataregion "IN" and author_type "staff"
    And the payload passes the Spec v1.2 schema

Feature: Problem details and keys (P18-AT-v13-03)
  Scenario: Errors are RFC 9457
    When a client requests /v1/compliances/BAD-ID
    Then the response is application/problem+json with type, title, status 404, detail and code "LDC-INT-003"
  Scenario: Test key refused in production
    Given a request with key prefix ldck_test_ against the production host
    Then the response is 401 with LDC-INT-208

Feature: Law register provider (P18-AT-v13-04)
  Scenario: Superseded instrument returns its successor
    Given LawDocs lints a policy citing the 2017 NBFC outsourcing directions
    When it calls POST /v1/law-register/citations:check
    Then the response marks the instrument SUPERSEDED with the 2025 Directions as successor and the caller shows a fix
```

## 13. Deliverables and exit gate

**Deliverables**: gateway configuration as code; `int` module; `packages/contracts` (OpenAPI 3.1, AsyncAPI 3.0, JSON Schemas); generated SDKs (TypeScript, Python, Java); connector host and SDK integration; Finbyx, Udofin, Ops Hub, Equator, LawDocs and Academy connectors; Fineract reference connector; generic CSV/SFTP layouts; `ldc-agent` (Windows/Linux, signed) with Tally XML/JSON extractors; onboarding lookup adapters (at least one licensed company-data provider, GSTIN, GLEIF, PAN channel); Microsoft 365 adapter (SSO, SCIM, calendar, Teams meetings/transcripts, SharePoint `Sites.Selected`); ICS and CalDAV services; eSign adapters (at least two ESPs + DSC desktop signer); email/SMS/WhatsApp/voice adapters (at least JioCX for SMS and one alternate); embeds (script, hosted page, API) with accessibility audit; Razorpay adapter; developer portal and sandbox; certification workbench; integration monitor; runbooks (`docs/runbooks/integration-incident.md`, `dlq-replay.md`, `key-rotation.md`, `compliance-mode-switch.md`, `agent-install.md`).

**Exit gate**: §12 scenarios and NN tests green; Ecosystem Spec §14.3 suite groups relevant to LDC green in sandbox with `ConnectorCertified` emitted for Finbyx↔LDC, Udofin↔LDC, OH↔LDC; Pact tests green with `contracts.lock` pinned; penetration test of gateway, embeds and agent with no open critical/high; load: 500 req/s sustained per region on read APIs with p95 ≤ 800 ms excluding third parties; webhook fan-out 50,000 deliveries/hour with outbox lag p95 ≤ 30 s; documentation complete in the developer portal.

- [ ] *(v1.2)* Onboarding ports and adapters with contract tests, register snapshot ingestion for the listed official registers, provider quality dashboard; business-ID API façade, ID-keyed webhooks, `ldcbizid` extension, MCP ID tools with `NN-52_mcp_parity` extended; enumeration guard.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P18-01 | Ecosystem Spec §9.3 still describes LDC as "Node, TypeScript, MongoDB" | Superseded by D-01 | Owner (contracts change process §14.2) | Raise proposal for Spec v1.2 |
| OI-P18-02 | Revenue catalogue and Razorpay ownership (Spec §6.27/OH8) vs LDC Pricing Catalogue (D-21, P20) | Cross-document conflict | Owner / P20 | Master note M-S8-02 |
| OI-P18-03 | Licensed company-data provider selection, data-display and storage rights | Commercial/legal | Procurement / counsel | Manual entry fallback |
| OI-P18-04 | PAN verification channel eligibility for LDC or its aggregator | Regulatory/vendor | Compliance | Name-only entry; verify later |
| OI-P18-05 | CICRA position on bureau pulls for onboarding | Counsel confirmation of FR-P18-33 | General Counsel | No pulls (default) |
| OI-P18-06 | TRAI number-series and DLT rules current text for automated calls to RE customers | Rules changed in 2025–26 | Telecom counsel | `int.voice.ai_agent.enabled = OFF`; tenant's own CPaaS |
| OI-P18-07 | JioCX API documentation and WhatsApp BSP status | No public developer portal found | Procurement | Alternate CPaaS |
| OI-P18-08 | WhatsApp INR billing migration deadline 31 Dec 2026 and BSP handling | Meta notice | Procurement | Do not activate WhatsApp until BSP confirms |
| OI-P18-09 | FinLegal Academy LMS platform and SSO/LTI/xAPI support | Unknown platform | LawDocs Trainings | Catalogue CSV + manual completion upload |
| OI-P18-10 | Microsoft 365 plan held by Infrabyx and typical client plans (transcripts, `Sites.Selected`, retention labels) | D-10 | Company Secretary / CTO | Capability matrix gates features |
| OI-P18-11 | JioMeet API availability for meeting creation | Not verified | CTO | Teams/Google Meet only |
| OI-P18-12 | Native APIs of Busy, Marg and other Indian accounting packages | Not verified | Integrations lead | File-export layouts |
| OI-P18-13 | Bhashini/ULCA use for SMS/notice translation in regional languages | Terms | AI lead | Human translation |
| OI-P18-14 | Public disclosure pages — which documents each sector must publish | Sector packs (P15) | Content team | Tenant chooses documents |

**Open items added in v1.1** *(v1.1)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P18-21 | Court/tribunal data licences (e-Courts/NJDG, NCLT, DRT, e-Jagriti) | Terms and lawful API access to verify | CTO / counsel | `int.litigation_data.provider = MANUAL` |
| OI-P18-22 | MCP registry and assistant-marketplace listing processes | Ecosystems evolving | CTO | Unlisted; direct URL onboarding |
| OI-P18-23 | A2A as Ecosystem transport (Spec v1.2 CR) | Needs group approval | Owner | `int.a2a.enabled = OFF` |
| OI-P18-24 | Licensed regulatory-intelligence contracts and display rights | Commercial | Owner / content lead | Official feeds only |
| OI-P18-25 | Reference-rate sources' terms of use (FBIL, CBUAE, MAS) | Licence check | CTO | Manual rate entry with evidence |
| OI-P18-26 | Foreign registry data licences (Companies House, ACRA, OpenCorporates) | Licence check | CTO | Manual entry |
| OI-P18-27 | Partner role naming: lead names `prt_admin`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer` vs P25's `prt_content_author`, `prt_content_reviewer`, `prt_delivery_professional` | Cross-file reconciliation | Lead (Appendix D) | Lead names used here |

**v1.2 open items** *(v1.2)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P18-28 | Formats and stable URLs of each official register file (RBI NBFC and ARC lists, Upper Layer list, SEBI intermediaries, IRDAI, IFSCA, CRCS) | Publishers change formats without notice | Content ops | Parser versioning and HOLD on schema change; manual upload of the file by the content team |
| OI-P18-29 | Commercial terms, storage and display rights of MCA-data, PAN and GST providers | Contracts not signed | CTO / counsel | Discovery runs on GLEIF and public registers only; manual entry for the rest |
| OI-P18-30 | Ecosystem Spec registration of CloudEvents extensions `ldcbizid` and `ldcinstref` | Ecosystem change process | Integration lead | Extensions sent anyway (CloudEvents receivers ignore unknown extensions) |
| OI-P18-31 | Whether GSP access may be used for onboarding look-ups (non-filing purpose) | GSP licence terms | Counsel | Use an aggregator with an explicit taxpayer-search product |
| OI-P18-32 | *(v1.3)* Alternate adapters to contract first for Tier-0 ports (one alternate live in CI per port — IPB open item 8) | Vendor contracts | CTO / procurement | Contract tests against sandboxes; production reference adapter only |
| OI-P18-33 | *(v1.3)* Registration of items 15–26 of master §19 in Ecosystem Spec v1.2 §3 (names, payload minima, `dataregion`) | Ecosystem agent | Ecosystem Spec editor | Emit internally as `in.lawdocscomply.*` until registered |
| OI-P18-34 | *(v1.3)* `LAW_REGISTER_PORT` SLA and rate limits as a shared service; whether a product-local snapshot is refreshed daily or on `PolicyReviewDue` | Cross-product design | LDC lead / IPB owner | Daily snapshot; 24-h cache |

---

## 15. Sources (accessed 25 October 2026 unless stated)

1. Infrabyx Ecosystem Integration Specification v1.1 (owner's folder) — Parts 3, 4, 6.15–6.27, 9, 10, 11, 12, 13, 14.
2. CloudEvents 1.0.2 specification (CNCF); Standard Webhooks specification (standardwebhooks.com); OpenAPI 3.1.0; AsyncAPI 3.0.0; JSON Schema 2020-12.
3. IETF RFCs: 9457 (problem details), 9421 (HTTP message signatures), 9530 (digest fields), 8705 (mTLS-bound tokens), 7523 (JWT client auth), 9700 (OAuth 2.0 security BCP), 9126 (PAR), 9449 (DPoP), 8693 (token exchange), 9745 (Deprecation header), 8594 (Sunset header), 7643/7644 (SCIM 2.0), 5545 (iCalendar), 4791 (CalDAV), 9562 (UUIDv7).
4. OpenID Foundation, FAPI 2.0 Security Profile (Final, February 2025).
5. Tally Solutions, "TallyPrime as server" and "TallyPrime integration using JSON" (native JSON from TallyPrime 7.0): https://help.tallysolutions.com/tallyprime-as-server/ ; https://help.tallysolutions.com/tally-prime-integration-using-json-1/
6. DigiLocker Authorized Partner API Specification v1.11: https://img1.digitallocker.gov.in/assets/img/Digital%20Locker%20Authorized%20Partner%20API%20Specification%20v1.11.pdf ; API Setu: https://api.apisetu.gov.in
7. Microsoft, "SharePoint now supports delegated Sites.Selected authentication" (9 Feb 2024): https://devblogs.microsoft.com/microsoft365dev/sharepoint-now-supports-delegated-sites-selected-authentication/ ; Microsoft Graph calendar and onlineMeetings transcripts documentation.
8. Meta, Pricing on the WhatsApp Business Platform: https://developers.facebook.com/docs/whatsapp/pricing
9. Jio Business portal (JioCX SMS/Email/Voice/RCS/WhatsApp, SIP Trunk, IP Centrex, Toll-Free, JioMeet): https://www.jio.com/business/ ; https://www.jio.com/business/services/voice-and-collaboration/
10. UNI India, Jio Haptik WhatsApp AI agents for SMBs.
11. Information Technology Act 2000, s.1(4) and First Schedule [LAW]; CCA eSign guidelines (cca.gov.in) [LAW/guidance].
12. Credit Information Companies (Regulation) Act 2005, ss.2, 17–19 [LAW] — basis for FR-P18-33 [INTERP; VERIFY].
13. TRAI Telecom Commercial Communications Customer Preference Regulations 2018 (as amended) [LAW]; TRAI directions on 1600/140 number series [VERIFY current text].
14. GLEIF API documentation (api.gleif.org).
15. Probe42 resources (company data in India): https://resources.probe42.in/ ; Qorpiq developer docs: https://developers.qorpiq.com/docs/intro/

16. *(v1.2)* GLEIF API documentation (Level 1 and Level 2 relationship data) — https://www.gleif.org/en/lei-data/gleif-api
17. *(v1.2)* RBI, NBFC list — https://rbi.org.in/scripts/BS_NBFCList.aspx ; SEBI, Recognised intermediaries — https://www.sebi.gov.in/intermediaries.html
18. *(v1.2)* CloudEvents 1.0.2 specification, "Extension Context Attributes" — https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
19. *(v1.2)* Digital Personal Data Protection Act 2023, s.8(7) (erasure when purpose served) — https://www.meity.gov.in/

---

## 16. Master integration notes (pack lead, v1.1 and v1.2, 25 October 2026)

**From v1.0 integration:** X-01, X-03, X-04, X-07, X-23, X-24, X-41; implement the Ecosystem Spec v1.2 change requests of master §19 only after approval.

**Added in v1.1:** NN-52; D-35; X-50.

**Added in v1.2:** D-51, D-56; NN-57 (onboarding discovery ports, partner onboarding API and the business-ID API; events carry `ldcbizid`).

**Added in v1.3:** D-60; X-71 (port aliases); IPB-01 port catalogue with two adapters per port, IPB-10 connector marketplace manifest, `/v1` conventions, Standard Webhooks and MCP exposure rules; the twelve Ecosystem events of master §19 items 15–26 (OI-P18-33 until Spec v1.2 registers them); LDC as `LAW_REGISTER_PORT` provider for all products.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
