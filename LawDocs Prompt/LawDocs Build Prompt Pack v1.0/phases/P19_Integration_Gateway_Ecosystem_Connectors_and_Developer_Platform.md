# Phase P19 — Integration Gateway, Ecosystem Connectors and Developer Platform

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, transactional outbox, audit ledger, KMS, Temporal, OpenTelemetry), P02 (tenancy, roles, maker-checker, delivery grants), P03 (settings registry, flags). Built on P19 later: P01 (KYB/identity adapters), P04 (vault deposits), P07/P08 (eSign/eStamp adapters, hosted signing hand-off), P09 (MCP server edge), P11/P12 (court-data and trademark adapters), P13 (LDC system-of-record switch), P17 (OH8 billing connector), P18 (Delivery Console UI over the OH connector), P20 (storage targets, `LD-EXPORT-1.0`). External: Infrabyx Ecosystem Integration Specification v1.1 (committed unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, SHA-256 checked in CI), the `infrabyx-contracts` registry, the Ecosystem PKI, `@infrabyx/connector-sdk`, and the Appendix Y change request (Ecosystem Spec v1.2) for every LawDocs-specific contract.
>
> **Sequencing:** **Core (Wave 1, sprints 1–3):** gateway, OAuth 2.1 profile, scopes, error model, idempotency, correlation, rate limits, outbox relay, tenant webhooks, DLQ, connector runtime, Operations Hub connector, eSign/eStamp/KYB adapter scaffolding for P01/P08, minimum developer portal. **Full (Wave 2, sprints 4–9):** LDC, Finbyx, Udofin and Equator connectors (behind `int.eco.v12_contracts.enabled` until Appendix Y is merged), partner onboarding API, court-data, trademark, workplace, accounting, HRMS and CRM adapters, Zapier/Make and iPaaS, SDKs, sandbox personas, health dashboard, certification workbench. **Freeze:** scope catalogue and tenant webhook catalogue (Appendix I §I.6–§I.7) freeze at the end of sprint 3; later changes follow FR-P19-06.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), I (Integration Adapters and API Catalogue), Y (Ecosystem Spec v1.2 Change Request — LawDocs), K (`LD-EXPORT-1.0`), R (settings), D (roles), F (instrument eligibility, via P08), M (professional rules), W (verification log). The Ecosystem Spec prevails for any cross-product contract (NN-24).
> **Requirements covered:** R-002, R-003, R-005 (KYB pre-fill transport), R-006 and R-078 (eSign/eStamp adapters), R-012 and R-076 (court data), R-013 (trademark data), R-021 and R-022 (connector framework, stable IDs), R-023, R-024 (bulk intake by API), R-029 and R-062 (Jio channels as adapters), R-034 (payments via OH8), R-041 and R-081 (Academy feed), R-050 (CRM openness via OH3/Brevo), R-053 and R-055 (Microsoft 365, Google Workspace), R-058, R-067 (sharing ledger).
> **Decisions applied:** D-01, D-02, D-10, D-11, D-12, D-14, D-16 · **Challenges applied:** CH-02, CH-03, CH-04, CH-05, CH-06, CH-13, CH-16, CH-17, CH-27 · **Non-negotiables tested:** NN-01, NN-05, NN-06, NN-07, NN-11, NN-13, NN-18, NN-19, NN-23, NN-24, NN-25, NN-32, NN-34, NN-38, NN-39, NN-46, NN-47
> **Estimated effort:** 9 two-week sprints (core 3 in Wave 1), squad of 8 (gateway and platform 3, ecosystem connectors 2, third-party adapters 2, developer experience 1)

---

## 1. Objective and business outcome

LawDocs must exchange data with four sister products, the group Operations Hub and many third-party systems without each new counterparty becoming a project, and must make "onboarding of new companies easy" (R-002, R-003). P19 delivers one gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK with mapping packs, a file fallback — and the module `int`, the **only** LawDocs module that publishes or consumes cross-product events (master §5.3). Modules write internal events to the outbox; `int` decides, through registered contracts, what may leave LawDocs, to whom, on which consent or legal basis, and records each movement in a **sharing ledger** the customer can read (CH-16).

Three boundaries shape the design; the brief's wording is challenged where it would breach them:

1. **eSign is not shared.** "Data shareable across ecosystem apps both ways" (R-023) does not extend to LawDocs' ASP capability: an ASP may integrate eSign "only for applications owned or operated by them", and consent and logs stay with the ASP (CCA eSign FAQ; R3 LG-007) [LAW]. Finbyx, Udofin, Equator, LDC and the Operations Hub never use LawDocs' ESP route. A sister product's user signs through LawDocs only as a **LawDocs customer**, in a LawDocs tenant, on a LawDocs-hosted ceremony under LawDocs' consent screen — or the sister product uses its own ESP (NN-06). P19 offers a **hosted signing hand-off**, not an eSign API.
2. **Cross-product data needs a contract and a reason.** No shared database, no direct table reads; every message is a registered event, API or layout with `consentref` or `legalbasis` (NN-24; Spec principles 1, 5). LawDocs has no owner code in Spec v1.1; Appendix Y raises the change request and v1.2-dependent flows stay behind a flag until it is merged (NN-38).
3. **Walls stay up.** Consumer Help (`chp`) exchanges nothing with Finbyx, Udofin, Equator or LDC tenants (NN-23); the Hub receives only commercial records and aggregates (NN-19; Spec principle 12); the Equator neutrality wall covers LawDocs staff identities (Spec §4.6).

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | Spec §14.3 groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, Aggregates only, Isolation, Archive and storage, plus Appendix Y §Y.13 "Legal-tech boundaries", pass; `ConnectorCertified` emitted for OH, LDC, Finbyx, Udofin and Equator connectors in sandbox |
| One way in | 100% of machine traffic passes the gateway; no module controller reachable outside it |
| Easy company onboarding | A 500-row partner batch gets KYB pre-fill for ≥ 90% of valid CINs/GSTINs at ≤ 5 s p95 per row; invitations go out the same day; activation ≤ 4 taps from the email |
| Time to first API call | ≤ 15 minutes from developer sign-up to an authenticated sandbox call (usability test, 5 developers) |
| Reliable events | Outbox lag p95 ≤ 30 s; webhook delivery p95 ≤ 5 min; zero loss in a 4-hour counterpart-outage drill; DLQ replay only under maker-checker |
| Every share visible | Each cross-product movement of tenant or personal data appears in the sharing ledger within 60 s with counterparty, purpose, basis, record ids and hash |
| No portal automation | No HTTP client in the gateway or connector runtime targets eCourts, IP India, MCA21, GSTN portal UI, CKYCR, bureaus, Parivahan or income-tax portal domains; CI egress test passes (NN-05) |

## 2. Scope (in / out)

**In scope**
- `int`: edge gateway, contract registry client (`contracts.lock`), OAuth 2.1 authorisation-server profile on Keycloak (realms `ld`, `ld-staff`), client registry, restricted API keys, scopes, client-tenant consents, rate limits and quotas, correlation, idempotency store, outbox relay, inbox, tenant webhooks, ecosystem push/pull, DLQ and replay, event-type map, sharing ledger, connector runtime, mapping packs, file fallback, partner onboarding API, health dashboard, developer portal, sandbox, SDKs, automation connectors, certification workbench.
- **Ecosystem connectors:** Operations Hub (provisioning, catalogue, quotes, orders, invoices, entitlements, usage, CRM requests, tickets, directory, claims gate, SCIM staff identity, engineering evidence); LDC (kernel system-of-record switch, legal-matter and contract-obligation projections, policy documents, template packs); Finbyx (template and drafting packs, recovery-litigation projection, hosted signing hand-off for RE tenants that are LawDocs customers); Udofin (opt-in deposit of a borrower's own documents into their Personal vault); Equator (ADR referral, evidence pack, status, award into vault).
- **Third-party adapters** (Appendix I §I.2): eSign, eStamp, KYB/identity, court data, trademark data, Microsoft Graph, Google Workspace, email/SMS/RCS/WhatsApp/voice (JioCX and alternates), TallyPrime, Zoho Books, customer HRMS and CRM, storage (framework; feature in P20), FinLegal Academy feed.
- Tenant webhooks, Zapier/Make-style triggers and actions, Power Automate connector, OpenAPI/AsyncAPI exports.

**Out of scope (owner phase)**
- Ceremony, eligibility and evidence logic (P08); KYC/KYB journeys (P01); vault and folder import UX (P04); litigation and IP modules (P11, P12); governance/HRMS mounts (P13); marketplace (P16); billing UI (P17); Delivery Console screens (P18); exports and BYO storage (P20); website forms (P21).
- MCP server and MCP client registry — **P09** (FR-P19-83).
- Razorpay: LawDocs holds no Razorpay keys; payments run on OH8 (Spec §6.27). P19 builds only `BILLING_PORT` to OH8.
- Machine filing to, or scraping of, any court, registry, regulator, government or bureau portal (NN-05; Spec §10.2 `PORTAL_MANUAL`); bureau pulls, CKYC, direct PAN-database calls (CH-03–CH-05).
- Cross-product A2A agent traffic (OI-P19-09).

## 3. Personas and permissions touched

Full matrix in Appendix D.

| Role / principal | P19 permissions |
|---|---|
| `ORG_OWNER`, `ORG_ADMIN` | Connect/disconnect connectors; approve API clients and automation connections; manage webhooks; approve another admin's DLQ replay; view health and sharing ledger; propose (admin) and approve (owner) a system-of-record switch |
| `ORG_CLO` | Enable Finbyx litigation and LDC legal projections; approve Equator referral packs; mandatory approver for connectors sending `LEGAL` data out |
| `ORG_LEGAL_MAKER` | Create signing requests through approved clients; prepare referral packs (maker) |
| `ORG_MEMBER` | Use automation actions within own permissions; no tenant-wide connectors |
| `IND_OWNER` | Link/unlink Udofin or another approved app for deposits; view and export personal sharing ledger; revoke apps (delegates and family members cannot) |
| `PRO_FIRM_ADMIN` | API clients for own practitioner workspace |
| `PLT_SUPER_ADMIN` | Platform connector catalogue, vendor credentials, kill switches (re-enable needs `PLT_SECURITY_OFFICER`) |
| `PLT_SECURITY_OFFICER` | Security reviews, certification sign-off, key/PKI oversight |
| `PLT_SRE` | Platform monitor and DLQ metadata only |
| `PLT_DPO` | Approves every new cross-product flow carrying `PII` or above; monthly sharing-ledger anomaly review |
| `OPS_ONBOARDING`, `OPS_SUPPORT_AGENT` | Batch/invitation status for support; tenant health only under a delivery grant (NN-17); never activate a tenant for a customer |
| `PRT_ADMIN`, `PRT_OPERATOR` (new; Appendix D) | Partner portal: submit batches, view invitation outcomes; no tenant data after activation |
| `DEV_ACCOUNT` (new; Appendix D) | Developer portal and sandbox only |
| Ecosystem clients `svc_oh_<env>`, `svc_ldc_<env>`, `svc_finbyx_<env>`, `svc_udofin_<env>`, `svc_equator_<env>` | Certificate-bound OAuth clients, one per (product, counterparty, environment, purpose); scopes per Spec §4.5 and Appendix Y §Y.9 |
| `ext_<connector-id>` | Certified third-party connectors with tenant consent |
| `AGT_*` | Maker only: draft mapping packs or webhook filters; never approve, enable, replay or raise ceilings (NN-43) |

## 4. Functional requirements

### 4A. Gateway and contract discipline

**FR-P19-01 — One gateway.** All machine traffic enters through AWS API Gateway or Envoy behind ALB in ap-south-1 (DR ap-south-2; NN-25) with WAF, TLS 1.3, HSTS. Hosts: `api.lawdocs.in`, `api.sandbox.lawdocs.in`, `events.lawdocs.in` (ecosystem push, mTLS only), `hooks.lawdocs.in` (vendor callbacks), `auth.lawdocs.in`, `developers.lawdocs.in`. The gateway enforces authentication, audience and scope, tenant resolution, schema validation, size limits (10 MB; files by pre-signed URL), idempotency-key presence, rate limits, mTLS for ecosystem and certified connectors, optional IP allow-lists, and logs without bodies or personal data (NN-32). Web apps use BFF sessions (no tokens in browser storage); mobile uses `/m/v1` (P22).

**FR-P19-02 — Contract-first.** OpenAPI 3.1 for every endpoint and AsyncAPI 3.0 for every event, JSON Schema 2020-12 generated from Zod in `packages/contracts`; ecosystem contracts generated from `infrabyx-contracts` and pinned in `contracts.lock`, never hand-written (Spec "How to use"). CI blocks an API change without a contract change, a field added to a published schema version, or a breaking change within a major; Pact tests gate each ecosystem counterpart.

**FR-P19-03 — Conventions.** `/v1/<module-path>/<resource>` with plural nouns and action sub-resources; ecosystem endpoints exactly as the Spec, not module-prefixed (`/v1/events`, `/v1/provisioning-requests/{id}`, `/v1/entitlements`). `snake_case`; `UPPER_SNAKE_CASE` enums with `x-extensible-enum`; prefixed ULIDs as keys and business references (`LD-AGR-2026-000123`) as separate fields; cursor pagination (`limit` ≤ 500); `updated_since` on every list; `fields`; `expand` ≤ depth 2; RFC 3339 with offset; money `{"amount": "1499.00", "currency": "INR"}`; ETag/`If-Match` on PATCH.

**FR-P19-04 — Error model.** RFC 9457 problem details with `type`, `title`, `status`, `detail` (no personal data), `instance`, `code`, `correlation_id`, `retryable`, `errors[]` (JSON Pointers) and `help_key`. Ecosystem calls use the Spec §3.9 codes; LawDocs codes are `LD-<MODULE>-<NNN>` (P19 range §7.6; model Appendix I §I.10). `entitlement-missing` is never returned for reading or exporting one's own data (NN-11).

**FR-P19-05 — Idempotency.** `Idempotency-Key` (UUIDv7) mandatory on machine POST/PATCH/DELETE; key, body hash and response kept 24 hours (7 days for payment orders, eSign/eStamp requests, outbound messages and external exports). Different body → 422 (`LD-INT-021`); retry while processing → 409 (`LD-INT-022`) (Spec §3.4; IETF draft [VERIFY: status]). Every adapter side effect carries its own vendor idempotency key where supported and is reconciled (NN-46).

**FR-P19-06 — Versioning.** Major in the path; ecosystem majors run in parallel ≥ 90 days (Spec §14.1); a superseded public major runs ≥ 12 months with `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers and monthly usage reports to client owners.

**FR-P19-07 — Correlation and tracing.** W3C `traceparent` propagated; `X-Correlation-Id` (ULID) issued when absent and returned on every response; CloudEvents carry `correlationid` and `causationid`. Admins can paste a correlation id to see the hop list (metadata only).

### 4B. Machine authentication and authorisation

**FR-P19-08 — Client types.**

| Type | Who | Grant and binding | Token life |
|---|---|---|---|
| Ecosystem service | OH, LDC, Finbyx, Udofin, Equator | OAuth 2.1 client credentials [VERIFY: draft status] per RFC 9700; certificate-bound (RFC 8705) with Ecosystem PKI; RFC 9421 `ed25519` signatures (Spec §3.6) | ≤ 10 min, audience-restricted |
| Certified connector | Third-party connector vendors | `private_key_jwt` (RFC 7523) or mTLS; consent per tenant | ≤ 10 min |
| Tenant integration | A company's scripts, ERP, CRM, HRMS | `private_key_jwt`; client secret only in sandbox | ≤ 15 min |
| Partner | Resellers, CA/CS firms, chambers, banks' SME desks | `private_key_jwt`; partner agreement on file | ≤ 15 min |
| Delegated user app | Zapier, Make, Power Automate, intranets, Udofin's app for deposits | Auth code + PKCE (S256) + PAR (RFC 9126); DPoP (RFC 9449) for public clients; LawDocs consent screen; rotated, sender-constrained refresh tokens | ≤ 10 min; refresh ≤ 30 days idle |
| Restricted API key | Sandbox; Pro read-only automation | `ldk_test_…`/`ldk_live_…`, Argon2id-hashed, shown once, read scopes only in production | ≤ 90 days |
| Publishable key | Public widgets | `ldpk_…` bound to origins; create-only public scopes | n/a |

**FR-P19-09 — Authorisation-server profile.** Human sign-in stays in P01 (Aadhaar never a login — NN-03). P19 adds RFC 9728 Protected Resource Metadata, RFC 8414 metadata, RFC 9207 issuer identification, Client ID Metadata Documents where supported, and `acr`/`auth_time` claims so APIs can demand step-up (`acr=ld:mfa` for `esign.request:create`).

**FR-P19-10 — Scopes.** `[domain].[resource]:[action]` (Spec §4.5). Each scope declares its highest data class and grantor roles; a client gets the intersection of its scopes, the consenting user's or tenant's permissions and its `data_class_max`; fields above the ceiling are omitted and listed in `x-omitted-fields`. Catalogue: Appendix I §I.6; ecosystem scopes: Appendix Y §Y.9.

**FR-P19-11 — Contextual authorisation.** Cerbos evaluates every call with tenant, entity, department, record sensitivity, privilege flag, grant and link state and consent; RLS underneath (NN-01). An expired link or revoked consent disables the client for that tenant within 60 s. BOLA tests run per endpoint with a second tenant's ids.

**FR-P19-12 — Consent or legal basis.** Every cross-product message with personal data carries `consentref` or `legalbasis`; otherwise `consent-missing` (`LD-INT-031`). LawDocs' role per flow is recorded in the ROPA (fiduciary for individuals; processor for company tenants — R3 LG-072).

**FR-P19-13 — mTLS and keys.** Ecosystem endpoints accept only Ecosystem PKI certificates (separate sandbox and production CAs, ≤ 397 days, automated rotation with 30/7/1-day warnings); the certificate subject maps to exactly one client (`LD-INT-012`). Secrets live in KMS-backed storage referenced by handle, rotated ≤ 90 days with overlap, never in logs, traces, DLQ metadata or tickets (NN-32). RFC 9421 and JWS keys (`ed25519`) are HSM-backed, rotated annually, published at `/.well-known/jwks.json` per environment.

### 4C. Events, webhooks, outbox, retries and DLQ

**FR-P19-14 — Outbox relay; `int` as sole publisher.** Modules write internal events (`in.lawdocs.<module>.<EventName>.v<n>`) to the outbox in the same transaction as the change and the audit entry (NN-45). The relay feeds internal handlers, tenant webhooks and the `int` mapper, which alone produces ecosystem events (`in.infrabyx.<domain>.<EventName>.v<major>`, `source = urn:infrabyx:lawdocs:<tenantid>`) per `int.event_type_map`. Test `arch/int-only-publisher.spec.ts` fails any other publisher.

**FR-P19-15 — Envelope.** CloudEvents 1.0.2 plus Spec extensions: `id` (UUIDv7), `source`, `type`, `subject`, `time`, `dataschema`, `tenantid`, `reid` (`none` outside an RE lending context), `productfamily` (`na`), `correlationid`, `causationid`, `consentref`/`legalbasis`, `dataclass`, `schemaver`, `seq`, `traceparent`. Internal and tenant-webhook events use `source = urn:lawdocs:<tenantid>`.

**FR-P19-16 — Inbox, ordering, catch-up.** Consumers store `(source, id)` and the business key before processing; duplicates return 200 with no effect. Order per `subject` by `seq`; gaps park 15 minutes, then catch up via the producer's `GET /v1/events?after=&types=`, else `ReconciliationBreakRaised` (Spec §3.5). LawDocs serves its own feed with ≥ 90 days replay (365 for `adr`, `legal` court-case and `esign` subjects).

**FR-P19-17 — Tenant webhooks.** Pro and above (plan limits) subscribe HTTPS endpoints to the catalogue (Appendix I §I.7) using Standard Webhooks (`webhook-id`, `webhook-timestamp`, `webhook-signature` HMAC-SHA256 over `id.timestamp.body`, `whsec_` secret, two secrets during rotation). Payloads are thin: class `INTERNAL` (ids, references, statuses, dates); receivers fetch details with their own scopes. An admin may raise named events to `PII` with `ORG_OWNER` approval; `LEGAL` and above never go by webhook. Private, loopback, link-local and metadata IPs are blocked at resolve time; redirects are not followed.

**FR-P19-18 — Retries.** At-least-once; `408`, `429`, `5xx`, timeouts (10 s) retry with exponential back-off and full jitter (base 30 s, cap 1 h) for 72 hours honouring `Retry-After`; other `4xx` are permanent. Endpoints failing for 24 hours auto-pause with notice (new events for the endpoint are held, not dropped; events already in retry continue to the 72-hour limit); resume is one click.

**FR-P19-19 — DLQ and replay.** Exhausted or permanent failures (both directions) go to the DLQ with reason and attempts. Replay is requested by one user and approved by another (NN-18), shows window, filters and count, and re-enqueues with the **same** event id. DLQ items expire after 30 days (ecosystem 90) with a summary to the owner.

**FR-P19-20 — Transports and file fallback.** Ecosystem delivery by HTTP push (Standard Webhooks + RFC 9421) or the shared MSK/Redpanda bus where both sides are on the Infrabyx ap-south-1 estate (Spec §3.1), chosen per link without changing payloads. Fallback: SFTP from allow-listed Indian IPs or signed-URL upload; CloudEvents batches, NDJSON or registered layouts; manifest with counts, control totals and SHA-256 signed by detached JWS; acknowledgement file; names `[producer]_[reid]_[layoutid]_v[major]_[yyyymmdd]_[seq].[ext]` (Spec §3.11).

### 4D. Rate limits and quotas

**FR-P19-21 — Token buckets.** Per client, tenant and operation class (read, write, bulk/export, signing, onboarding lookup); signing and payment-adjacent commands never share a bucket with bulk reads (Spec §3.10). Tiers in Appendix I §I.9 via `int.ratelimit.tier`; reviewed Enterprise overrides. `RateLimit-Policy`/`RateLimit` headers [VERIFY: final names]; 429 with `Retry-After` (`LD-INT-041`).

**FR-P19-22 — Quotas and metering.** Monthly quotas per plan; overage meters (`API_CALLS_OVERAGE`, `API_ESIGN_AADHAAR`, `API_ESTAMP`, `API_AGREEMENT_GENERATE`, `COURT_DATA_REFRESH`) counted at source and sent to OH8 only as `usage_aggregate_v1` (Spec §6.27; R6 §R6.2.6); failed calls are not billed (R1 IMP-088). Warnings at 80% and 100%; at 100% non-essential writes soft-block while reads and exports always work (NN-11, NN-50).

**FR-P19-23 — Abuse controls.** Accessible bot protection on public lookups (no image-only CAPTCHA — R3 LG-136); anomaly detection on volume (10× daily median), enumeration and cross-tenant probing raises a security event and can suspend a client pending review.

### 4E. Ecosystem links and the sharing ledger

**FR-P19-24 — Link registry.** `int.links` records each authorised relationship: kind (`OH_PROVISIONING`, `LDC_SOR`, `LDC_PROJECTION`, `FINBYX_LEGAL`, `FINBYX_SIGNING_HANDOFF`, `UDOFIN_DEPOSIT`, `EQUATOR_PARTY`, `GROUP_GRANT_REF`), counterpart `org_id` and tenant (Spec §4.1 tenant map), purposes, data classes, permitted contracts, validity, approvals, state. No active link, no message (`LD-INT-032`). Kinds map to the Spec link types proposed in Appendix Y §Y.3.3: `LDC_SOR` and `LDC_PROJECTION` → `legal_sor_link`; `FINBYX_LEGAL` → `finbyx_legal_link`; `FINBYX_SIGNING_HANDOFF` → `signing_handoff_link`; `UDOFIN_DEPOSIT` → `deposit_link`; `GROUP_GRANT_REF` → `group_grant` (Spec §4.6).

**FR-P19-25 — Event-type map.** `int.event_type_map` maps internal events to ecosystem events with transform, data-class ceiling and link kind. Only rows whose contract is `APPROVED` in the pinned registry are active; Appendix Y rows are `PROPOSED` and inert until `int.eco.v12_contracts.enabled` is ON and the registry holds the subject (NN-38).

**FR-P19-26 — Sharing ledger.** Every cross-product movement of tenant or personal data writes an append-only, hash-chained entry (NN-02): time, direction, counterparty, link, contract, purpose, `consentref`/`legalbasis`, canonical record ids (never content), payload hash, data class, outcome. Admins see the tenant ledger (SCR-P19-09); individuals see theirs under Privacy → Connected apps (SCR-P19-10); exported in `LD-EXPORT-1.0` (NN-11).

**FR-P19-27 — Interim manual channel.** Until Appendix Y is merged, an exchange a tenant needs (e.g., an Equator referral pack) runs as a logged manual channel: the user downloads a signed pack (manifest, hashes, detached JWS) and uploads it to the counterpart; the ledger records `channel = MANUAL_INTERIM` (mirrors the Spec §6.1 "(A)" interim rule).

### 4F. LawDocs ↔ LawDocsComply

LDC is SoR for compliance, governance and client HRMS; LawDocs is SoR for legal work (D-10). Both mount the shared kernels and never fork them (NN-47).

**FR-P19-28 — Kernel system-of-record switch.** A LawDocs-only company runs the governance and HRMS kernels locally (P13). When the same `org_id` also subscribes to LDC, the tenant sets `int.eco.ldc.sor_mode.governance`/`.hrms` to `LDC` through the switch in §5.6: export with hash-chain heads → LDC import and reconciliation → dual running (one board-meeting cycle or 30 days, LawDocs read-only for kernel writes with deep links) → cutover → signed reconciliation; any failure rolls back with LawDocs still SoR and nothing deleted. Users sign in once and never enter data twice [VERIFY: LDC customer-realm federation]. The reverse switch uses the same states. Event `SystemOfRecordSwitched` is proposed (Appendix Y §Y.7.7).

**FR-P19-29 — Governance facts for the formalities gate.** With LDC as SoR, P07/P08 read resolutions and authorised-signatory facts through LDC APIs (`governance.resolution:read`, `governance.kmp:read`) on demand, without caching beyond the request, for NN-40 ("board approval recorded") and delegation-of-authority checks. Spec §6.23 rule 1 keeps governance events tenant-internal; Appendix Y §Y.7.6 proposes letting them reach the **same organisation's** legal SoR under an `LDC_SOR` link.

**FR-P19-30 — Obligations from contracts.** Contractual obligations extracted in P07 (`obl_`) are published to a linked LDC tenant as `ContractObligationRegistered` and `ContractObligationStatusChanged` (proposed `legal` domain) or pulled via `GET /v1/contract-obligations?updated_since=`, so LDC can show them as non-regulatory obligations and link them to regulatory ones (e.g., an outsourcing agreement's audit-right clause). LDC never edits them; completion evidence stays in LawDocs.

**FR-P19-31 — Policies and templates.** LDC stays SoR for regulated entities' policies. LawDocs offers policy, contract and notice templates as versioned packs (`GET /v1/template-packs/{pack}/versions/{v}`, `templates.pack:read`) with reviewer of record and effective dates (NN-30), consumed by LDC's CLM/notice features (LDC P26 `TEMPLATE_PORT`). A policy drafted in LawDocs for an LDC-linked tenant is handed over as `DocumentShared` (Spec §6.13); approval and attestation happen in LDC.

**FR-P19-32 — Legal projections to LDC.** For contingent-liability disclosures, Reg 30 materiality and penalty registers, LawDocs publishes `LegalMatterOpened/Updated/Closed`, `CourtCaseRegistered/Updated`, `CourtHearingScheduled` and `CourtOrderRecorded` to the linked LDC tenant (proposed `legal` domain; class `LEGAL`; `legalbasis = LEGAL_CLAIM`; privileged material only per record with `ORG_CLO` approval). **Conflict raised:** LDC Pack v1.2 P26 builds its own legal-matter register and CLM; under D-10, where an organisation uses both, LawDocs is SoR and LDC P26 should consume these projections (Appendix Y §Y.14).

**FR-P19-33 — Minimal people projection.** With LDC as HRMS SoR, LawDocs reads only name, work email, department, position and status (`hr.employee:read.minimal`) to assign legal tasks and approvals; salary, leave, attendance and identity documents never move (Spec §6.23 rule 3).

**FR-P19-34 — No compliance records in LawDocs.** LawDocs does not store LDC compliance records; links from LawDocs screens deep-link into LDC.

### 4G. LawDocs ↔ Finbyx

Finbyx and the Recovery Suite (later Udolex) are SoR for loans, notices, recovery, settlements and recovery litigation (Spec entities #19–#26).

**FR-P19-35 — Template and drafting packs.** Versioned lending templates — loan agreement variants, guarantee, hypothecation, sanction annexures, loan recall notice, SARFAESI s.13(2)/s.13(4) notices, NI Act s.138 notice, A&C Act s.21 notice — with jurisdiction variants, citations, reviewer of record and effective dates (NN-30), pulled by Finbyx (`templates.pack:read`). Finbyx generates, approves and issues notices and records `LegalNoticeIssued`; LawDocs never issues a notice in an RE's name.

**FR-P19-36 — Bespoke drafting.** An RE legal team that is a LawDocs tenant may draft a non-standard notice, reply or pleading (P10) and share the final document to its Finbyx tenant as `DocumentShared` with the `recovery_case_id` the user selects (link `FINBYX_LEGAL`; `legalbasis = LEGAL_CLAIM`). Finbyx records issuance.

**FR-P19-37 — Recovery-litigation projection.** With `int.eco.finbyx.litigation_projection.enabled` (by `ORG_CLO`), LawDocs consumes `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled`, `OrderRecorded`, `LitigationCaseClosed` (Spec §6.10) as read-only "Recovery proceedings (Finbyx)" in `lit`, so the CLO sees one portfolio and calendar. RS stays owner; values show "source: Finbyx Recovery Suite, as of …"; no edits. Needs Appendix Y §Y.7.5 (LawDocs as consumer; `litigation.case:read.legal`).

**FR-P19-38 — Hosted signing hand-off (NN-06).** An RE that is itself a LawDocs customer may let its Finbyx tenant create signing requests **in the RE's own LawDocs tenant** for staff-operated documents (MSME or corporate loan agreements, guarantees, security documents):
1. The client is approved by the RE's LawDocs `ORG_ADMIN` (`esign.request:create`, step-up at approval); Finbyx never receives ESP credentials, ASP keys or frameable signing URLs.
2. LawDocs runs the eligibility gate (Appendix F; NN-07), stamp-before-sign (NN-08) and its own consent screen; ceremonies are served only from `sign.lawdocs.in` as top-level navigation or an in-app browser tab (`frame-ancestors 'none'`) [REC; COUNSEL: confirm with the contracted ESP/aggregator — OI-P19-02].
3. Consent records and eSign logs stay with the ASP of record for the route (the contracted aggregator or LawDocs' own ASP arrangement, `asp_mode`; NN-06 as amended, X-15) and LawDocs' evidence copies stay in the LawDocs tenant (R3 LG-007); the RE receives the signed PDF and evidence pack by reference, and LawDocs emits `SigningRequestCompleted` (proposed `esign` domain, signed message).
4. Retail digital-lending journeys stay out: KFS acceptance and DLA loan-agreement signing remain in Udofin/Finbyx with their own ESP (`ESignCompleted`, Spec §6.2), because that evidence chain belongs to the RE's DLA journey [INTERP]. LawDocs never emits `ESignCompleted` or `EStampCompleted`.
5. NeSL DDE e-stamping for financial documents only via an aggregator for Enterprise RE tenants (R6 D-26) [VERIFY].

**FR-P19-39 — Counsel and directory.** Finbyx allocates counsel from OH9 (Spec §6.29). When an organisation engages an advocate through the LawDocs marketplace, LawDocs sends `MatterAllocated` counts to OH9 (proposed producer, Appendix Y §Y.7.8) — no party names, matter numbers or amounts — so the Equator conflict check stays complete.

**FR-P19-40 — No borrower data.** LawDocs receives no borrower, KYC, bureau or loan-level data from Finbyx except inside a document the RE chose to sign or share; other subjects are rejected (`dataclass-not-permitted`).

### 4H. LawDocs ↔ Udofin

**FR-P19-41 — Opt-in deposit to the Personal vault.** A Udofin borrower may save copies of **their own** documents (sanction letter, KFS copy, signed agreement, schedule, NOC, interest certificate, grievance correspondence) into a LawDocs Personal vault:
1. Link: "Save to LawDocs" in Udofin opens LawDocs authorisation (auth code + PKCE + PAR, in-app browser tab); the borrower signs in (OTP or passkey) and approves `documents.deposit:write` limited to one folder (default `05 Finance, Loans and Insurance/From Udofin`). ≤ 3 taps after sign-in.
2. Udofin records its own consent and calls `POST /v1/document-deposits` with `document_id`, `sha256`, JWS and `consentref` (proposed, Appendix Y §Y.8). LawDocs fetches bytes from Udofin's `GET /v1/documents/{id}` signed URL (Spec §6.13), verifies hash and JWS, stores an immutable original with `origin = RECEIVED_FROM_PRODUCT` (NN-09) and returns `DocumentDeposited`.
3. LawDocs gives Udofin only an opaque pairwise link id; Udofin sends no borrower identifier beyond what the document contains (Spec §4.3).
4. One way only: nothing flows from the vault to Udofin; wellness data is rejected (Spec principle 13).
5. One-tap unlink on either side stops deposits; saved copies remain the user's.

**FR-P19-42 — No cross-sell feed.** No LawDocs offer appears inside a Udofin loan journey; Udofin sends no borrower lists (R6 LD-X02; RS-LD-38 OFF). "Save to LawDocs" appears only after a document is issued and is never pre-ticked (NN-50).

**FR-P19-43 — Grievance hand-off is not to Consumer Help.** Udofin grievances go to the RE's grievance host (Spec §6.12); Udofin never steers a borrower to `[Consumer Help Brand]`. (a) No API, event, deep link, banner or referral exists from Udofin or Finbyx to `chp`; `int.chp.ecosystem_clients.allowlist` is empty and locked. (b) A borrower who independently approaches Consumer Help is screened by the P15 conflict check against group client organisations through the proposed OH API `POST /v1/client-conflicts/check` (flag and category only; Appendix Y §Y.8); where the respondent is a group client, `chp` applies its conflict policy (decline, or disclose and obtain consent) [COUNSEL]. (c) The borrower may attach documents from their own vault to their own case — their data, their action, not a feed. (d) `chp` never queries Udofin, Finbyx or Equator.

**FR-P19-44 — Neutral route information.** The general Personal workspace (not `chp`) may show public RB-IOS 2026 route information for any lender from the rules register (P03), never targeted at Udofin borrowers. Udofin-to-Equator launch uses Spec §4.4 token exchange; LawDocs is not in that path.

### 4I. LawDocs ↔ Equator Resolution

Equator is an independent ODR institution; common Infrabyx ownership is disclosed in every case (Spec §8.1). LawDocs treats Equator as **one** ODR option behind the provider-neutral `ODR_PORT` (Spec §8.9 `OdrProvider`), never as the default.

**FR-P19-45 — Where referrals start.** A referral can start from (a) a legal matter or court case in `lit`/`lgo` (P11, P13), (b) an executed agreement whose dispute-resolution clause names an institution (P07), or (c) a notice exchange in P10. Vidhi may suggest routes; the user decides (NN-13).

**FR-P19-46 — Route options shown neutrally.** The route panel lists, with plain-language "i" help (`hlp.int.adr_routes`): negotiation; pre-institution mediation under Commercial Courts Act 2015 s.12A for commercial suits not seeking urgent interim relief; conciliation (A&C Act Part III; a s.73 settlement has award status under s.74); arbitration only with a valid basis — a clause naming an institution or written post-dispute consent (A&C Act s.7, s.7(4)(b)) — and never a unilateral appointment (*Perkins Eastman v HSCC* (2020) 20 SCC 760; *CORE v ECI-SPIC-SMO-MCML (JV)*, SC Constitution Bench, 8 Nov 2024; Spec §8.2) [LAW]; Lok Adalat; court. Equator appears with the disclosure "Equator Resolution is an Infrabyx group company" next to other configured providers (`int.eco.equator.show_alternatives` locked ON). Non-arbitrable categories (matrimonial status, custody, testamentary validity, criminal matters, insolvency in rem, *Vidya Drolia* tests) show arbitration as unavailable (EQ NN-06) [LAW]; a pending consumer complaint cannot be compelled to arbitration (*Emaar MGF v Aftab Singh* (2019) 12 SCC 751). The Mediation Act 2023 provisions on enforcement and online mediation are shown as "not yet in force" until the rules register says otherwise (Spec §8.2) [VERIFY: e-Gazette at release].

**FR-P19-47 — Referral pack.** The maker (`ORG_LEGAL_MAKER` or `IND_OWNER`) selects documents: the agreement (signed original), stamp certificate, signing evidence pack and BSA s.63(4) certificate draft (NN-10), notices with service proofs, chosen correspondence, claim statement. `int` assembles a manifest (document ids, SHA-256, detached JWS each) — documents travel by reference (Spec §3.6, §6.13). `ORG_CLO` approves (company) or the individual confirms with step-up; privileged advice is excluded unless explicitly selected with a warning. The referral is created at the provider the user chose through `ODR_PORT` — for Equator, `POST /v1/adr/referrals` with `dispute_origin` and `basis` (proposed fields, Appendix Y §Y.7.4); for other providers, their adapter route (API, webhook, file or portal-manual) — and emits the ledger entry. No provider is pre-selected; a loan dispute is never referred (`regulatory-guard`).

**FR-P19-48 — Status, hearings and outcome back.** LawDocs consumes `ADRCaseStatusChanged`, `ADRHearingScheduled`, `ADRNeutralAppointed` (name only) and `ADROutcomeRecorded` for cases where the LawDocs user is a party (party view; scope `adr.case:read.party`). The matter timeline and calendar show them; the user joins sessions through Equator's own launch link (LawDocs never hosts hearings). On `ADROutcomeRecorded`, LawDocs fetches the award or settlement (eSigned and e-stamped by Equator; PDF/A-2b) by reference into the vault as an immutable original, creates obligations from its payment schedule (P07 `obl_`), and adds advisory clocks: correction s.33 (30 days) and challenge s.34(3) (3 months + 30 days) from the party's receipt date (Spec §8.8), labelled "advisory — confirm with your advocate" [INTERP].

**FR-P19-49 — Walls.** LawDocs never receives hearing content, recordings (mediation and conciliation are never recorded — A&C Act s.75), the selection log, neutral performance or other parties' documents (Spec §4.4, §8.4). LawDocs staff identities holding any `OPS_*` delivery role for a party may not hold an Equator case role in a matter referred from that party (Appendix Y §Y.14 proposes adding LawDocs to Spec §8.6); a professional engaged through the LawDocs marketplace by a party is reported to OH9 via `MatterAllocated` so Equator's conflict check counts it.

**FR-P19-50 — Model clauses.** Equator's published model clauses are imported as a clause pack (through Equator's clause API [VERIFY: EQ P09 endpoint] or a reviewed manual import) into the clause library (P06) with the disclosure label; they are never pre-selected. The tenant may set its own default dispute clause (`tpl.dispute_clause.tenant_default`, P06); the platform default is "no institution named — choose".

### 4J. LawDocs ↔ Operations Hub

The Operations Hub (OH) runs CRM (OH3), onboarding and delivery (OH4), support (OH5), billing and the catalogue (OH8), the professional directory (OH9), staff HRMS and identity (OH10), engineering operations (OH13) and the certification library and claims gate (OH14). LawDocs never rebuilds these (D-02) and sends them only commercial records and aggregates (NN-19). P18 builds the Delivery Console screens over this connector.

**FR-P19-51 — Provisioning.** LawDocs consumes `TenantProvisioned` (signed), creates or links the tenant, registers it in the tenant map (Spec §4.1) and acknowledges with `PUT /v1/provisioning-requests/{id}` (`ACCEPTED`, `READY`, `FAILED` with reason); it serves `GET /v1/tenants/{tenantid}/provisioning-status` for OH's fallback poll and holds at most one live tenant per `(org_id, product, environment)` (Spec §6.29). Self-service and partner-originated tenants are reported to OH with the proposed `TenantRegistered` event (Appendix Y §Y.7.7) so OH holds the commercial record. Until approved, LawDocs sends OH a daily signed file of new tenants (`ld_tenant_registrations_v1`, commercial fields only) through the manual interim channel (FR-P19-27).

**FR-P19-52 — Billing through OH8 (`BILLING_PORT`).** P17 calls OH8 for catalogue (`GET /v1/catalogue/versions/{v}`, signed), quotes (`POST /v1/billing/quotes`), orders and hosted checkout URLs (`POST /v1/billing/orders`), invoices (`GET /v1/billing/invoices?tenantid=`), and usage disputes; LawDocs consumes `PlanChanged`, `EntitlementChanged` (JWS verified against the pinned Hub key), `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`, and serves `GET /v1/entitlements?tenant=` for OH8's daily reconciliation. A browser redirect is never proof of payment (Spec §6.27). LawDocs keeps the last valid signed entitlement for 30 days if OH is unreachable. Marketplace orders need split settlement through Razorpay Route and line items separated by supplier type (LawDocs fee, professional fee, government fee, stamp duty as pure agent — NN-22); Appendix Y §Y.7.7 proposes the optional order fields and the `MarketplacePayoutSettled` event.

**FR-P19-53 — Individual buyers' billing identity.** D-11 puts LawDocs B2C invoicing on OH8, so OH8 needs an individual buyer's billing name, email, mobile, billing State (place of supply) and GSTIN if any. That is commercial-record data, but the Spec's `CONTRACT_PERFORMANCE_VENDOR` basis covers only customer staff contacts and OH-bound subjects accept at most `INTERNAL`. Appendix Y §Y.6 proposes `legalbasis = CONTRACT_PERFORMANCE_CUSTOMER` and a `PII` ceiling for named billing fields only. Never sent: vault, matter, case, document, consumer-case or credential data (NN-19). [OWNER] [COUNSEL] — DPO sign-off required before go-live.

**FR-P19-54 — Usage aggregates.** `UsageRecorded` (`usage_aggregate_v1`) monthly by WD+3 and daily provisional: tenant, legal entity, meter, `meter_kind`, period, quantity, statement hash; never user, document, agreement or matter ids (Spec §6.27). Meters: seats, eSign successful signatories by method, eStamp count, AI credits, court-data refreshes, storage GB-month, API overage, WhatsApp messages (cost pass-through).

**FR-P19-55 — CRM and support.** Lead forms (P21) and "Contact sales" (P17) call OH3 `POST /v1/crm/requests` with the requester's consented business contact (individuals only when they ask to be contacted, with separate marketing consent — R3 LG-063); in-product help calls `POST /v1/support/tickets` with redacted screenshots only (Spec §6.29). Brevo marketing sync is OH3's (`CrmSink`, Spec §10.2); in LawDocs Brevo is only an optional transactional `EMAIL_PORT` adapter.

**FR-P19-56 — Staff identity and group grants.** OH10 provisions LawDocs staff into realm `ld-staff` by SCIM 2.0 (groups carry `valid_to`); OH10 deprovisions leavers within 4 hours (privileged within 1 hour; Spec §4.6) and, on receipt of the SCIM deactivation, LawDocs ends sessions and grants within 60 seconds (P02 FR-P02-42); LawDocs evaluates its own roles and never treats an OH role name as a permission (Spec §4.6). Cross-company access arrives as `group_grant` memberships, enforced locally with sessions ended within 60 s of `valid_to`. Staff reach customer tenant data only through delivery grants or break-glass inside LawDocs (NN-17), never through OH.

**FR-P19-57 — Directory, claims gate, engineering evidence.** LawDocs consumes `ProfessionalEmpanelled`/`ProfessionalSuspended` (Rule 36 fields only) for the marketplace directory, OFF by default (D-05; NN-21), and blocks new engagements for a suspended professional within 1 hour; public claims pass `GET /v1/claims-gate/check` (NN-20); P23 sends `ReleasePublished`, `ControlEvidenceCollected` and `AccessReviewCompleted` (PLATFORM) to OH13/OH14.

### 4K. Partner onboarding API (bulk company onboarding)

**FR-P19-58 — Who may onboard companies in bulk.** (a) **Group products** (Finbyx, Udofin, LDC) never create LawDocs tenants directly: they raise a request to OH (`POST /v1/crm/requests` with product `LAWDOCS`, or OH4's provisioning flow), OH approves with maker-checker and emits `TenantProvisioned` (Spec §6.29). (b) **OH4** provisions directly. (c) **Third-party partners** under a partner agreement (resellers, CA/CS firms acting for their clients, chambers of commerce, banks' SME desks — R6 RS-LD-37) use LawDocs' partner API. The partner is never a regulated professional receiving a referral fee from LawDocs in breach of NN-21 (partner-type check at partner registration).

**FR-P19-59 — Batch submission.** `POST /v1/int/partner/onboarding-batches` (scope `partner.onboarding:write`; `Idempotency-Key`) accepts JSON or CSV (`ld_partner_onboarding_v1`, Appendix I §I.11) up to `int.partner.onboarding.max_batch_rows` (default 500) rows: `partner_ref` (unique per partner), legal name, constitution, CIN/LLPIN/registration no., GSTIN, PAN (validated format, stored masked + token), registered State, authorised signatory's name, work email and mobile, requested plan, workspace template, language, `authority_attestation` (partner confirms the company authorised it). `dry_run=true` validates without side effects and returns row-level problems (JSON Pointers).

**FR-P19-60 — KYB pre-fill.** For each row, `kyc` (P01) calls `COMPANY_DATA_PORT` (licensed MCA-data vendor), `GSTIN_PORT` (GSP "search taxpayer") and `LEI_PORT` (GLEIF) through the P19 runtime in parallel with a 5 s budget; results are stored as an `onboarding_snapshot` with provider attribution and fetch time, **unconfirmed**. No MCA scraping (CH-06), no bureau pull (CH-05), no CKYC (CH-03), no direct PAN-database call (CH-04); PAN verification uses DigiLocker/Entity Locker documents or a vendor with a lawful-upstream warranty (R3 LG-047). Directors' PAN and date of birth are never stored (R6 D-15).

**FR-P19-61 — Invitation, consent and activation.** Each valid row becomes an **onboarding invitation**, not a live tenant. The signatory receives one email (and one SMS only if the partner supplied a mobile and the template is DLT-registered — NN-34) naming the partner. The invitation page shows the DPDP notice, the partner's identity, the pre-filled fields with source labels, plan and price (all-in, NN-50) and terms. The signatory verifies identity (OTP + optional DigiLocker/Entity Locker pull), confirms or corrects each KYB field, accepts terms and DPA, and becomes `ORG_OWNER`. LawDocs captures the consent artefact (`cns_`) itself. Activation is ≤ 4 taps from the email. Invitations expire after `int.partner.onboarding.invite_expiry_days` (30) and the partner may resend once.

**FR-P19-62 — Partner visibility and commercial record.** The partner sees only status per `partner_ref` (`INVITED`, `OPENED`, `ACTIVATED`, `DECLINED`, `EXPIRED`), plan and activation date, plus status webhooks (`in.lawdocs.int.OnboardingInvitationAccepted.v1`, `…Declined.v1`, `…Expired.v1`); further access needs a delivery grant the company approves (NN-17). On activation LawDocs reports the tenant to OH (`TenantRegistered`) with the partner reference for OH8 partner accounting (RS-LD-37); LawDocs computes no partner commission.

**FR-P19-63 — Individuals are not bulk-onboarded from partner data.** An employer or partner may send invite links to individuals (work email only) for Personal plans; LawDocs pre-fills nothing about an individual from a partner, and identity is verified by the individual (DigiLocker, Aadhaar App offline verification, OTP — NN-03, NN-04). Finbyx and Udofin may not bulk-invite borrowers (`int.partner.individual_bulk.enabled` = OFF, locked for ecosystem clients).

**FR-P19-64 — Single-company onboarding.** `POST /v1/int/partner/onboarding-invitations` creates one invitation under the same rules; integrators may link to the activation page (top-level navigation, never a frame).

### 4L. Connector SDK host and third-party adapters

**FR-P19-65 — Connector runtime.** LawDocs hosts connectors implementing `@infrabyx/connector-sdk` (`manifest`, `capabilities`, `healthCheck`, `send`, `receive`, `call`, `reconcile`; Spec §10.1) out of process: one container per connector per region, read-only filesystem, non-root, network egress allow-list per manifest, secrets through the vault handle in `TenantContext`, no database access (APIs and events only). Connector ids follow `[counterparty]-[capability]-lawdocs` (e.g., `leegality-esign-lawdocs`, `probe42-company-lawdocs`). A `TenantContext` without `tenantid` fails.

**FR-P19-66 — Ports, not vendors.** Modules call ports (`ESIGN_PORT`, `ESTAMP_PORT`, `COMPANY_DATA_PORT`, `COURT_DATA_PORT`, `TRADEMARK_DATA_PORT`, `WORKSPACE_PORT`, `SMS_PORT`, `RCS_PORT`, `WHATSAPP_PORT`, `VOICE_PORT`, `EMAIL_PORT`, `ACCOUNTING_PORT`, `HRMS_SOURCE_PORT`, `CUSTOMER_CRM_PORT`, `STORAGE_PORT`, `ODR_PORT`, `ACADEMY_PORT`, `BILLING_PORT` and others in Appendix I §I.2), never vendor SDKs. Each port has at least one fallback (another vendor or a manual path), an enablement setting `int.adapter.<adapter_id>.enabled` and a kill switch `int.kill.<adapter_id>` in the single P03 registry (FR-P03-84; NN-39). Swapping a vendor is a configuration change plus certification, never a module code change.

**FR-P19-67 — Adapter rules by port.** Vendors, fallbacks, legality and status are binding in Appendix I §I.2; the rules below are what P19 enforces in the runtime.

| Port(s) | Runtime rules |
|---|---|
| `ESIGN_PORT`, `ESTAMP_PORT` (D-12; P08 owns ceremonies) | Aggregator first (Leegality, Digio fallback); second ESP route within 30 days of the first (eSign API v3.3 — R3 LG-008) [VERIFY: applicability to aggregator-ASP structures]; nightly ESP-licence watcher (R3 LG-005); OTP click-acceptance is labelled e-acceptance (IT Act s.10A), never "eSign" (R3 LG-001); eStamp only through authorised channels with State coverage registry and UIN verification (NN-08); a direct ASP–ESP route can be added later without code change |
| `DIGILOCKER_PORT`, `ENTITY_LOCKER_PORT`, `AADHAAR_OFFLINE_PORT`, `COMPANY_DATA_PORT`, `GSTIN_PORT`, `PAN_VERIFY_PORT`, `LEI_PORT` (P01) | DigiLocker direct as Requester: consent per access, URI + verification result by default, 24-hour NeGD incident clock, annual CERT-In-empanelled audit, no extension to sister apps without NeGD approval (R3 LG-038); Aadhaar App/QR offline verification only, no Aadhaar number stored (NN-04); licensed MCA-data and GSP vendors only, no scraping (CH-06) |
| `COURT_DATA_PORT` (P11) | Two licensed aggregators plus `ManualCNR`; `eCourtsOfficialApi` only with an Enterprise institutional litigant's own credentials (R6 D-01, D-08) [VERIFY]; scheduled-diff refresh; every display shows source and "as of", never "real-time", "official" or "certified" (NN-20) |
| `TRADEMARK_DATA_PORT`, `TM_JOURNAL_PORT` (P12) | User-entered application numbers, WIPO Brand DB screening labelled "screening aid", Journal watch via licensed partner or PDF ingestion; no IP India scraping (R6 D-11–D-13) [VERIFY: WIPO terms] |
| `WORKSPACE_PORT` (R-053, R-055) | Microsoft 365 first (confirm plan — CH-29 [OWNER]), Google Workspace second: SSO/SCIM (P01), Open in Word/Docs with check-in as a new version (NN-37 redline stays in LawDocs), Teams/Meet links, a dedicated "LawDocs" calendar (statutory dates authoritative), SharePoint/OneDrive/shared drives as export targets (P20); Graph `Sites.Selected` only [VERIFY: scope names]; Google Drive refused for `LEGAL`, `SPI`, `HR` (`residency-blocked`, Spec §12.2) |
| `EMAIL_PORT`, `SMS_PORT`, `RCS_PORT`, `WHATSAPP_PORT`, `VOICE_PORT`, `TELEPHONY_PORT`, `CALLER_ID_PORT`, `VOICE_AGENT_PORT` (R-029, R-062) | DLT-registered headers and templates with whitelisted URL domains; A2P CLI declaration before any automated or AI-voice call (TCCCPR Third Amendment 2026, Reg. 4 — R4 §5.2) [VERIFY: commencement]; AI-voice disclosure and human hand-off (R3 LG-078); WhatsApp opt-in utility templates only, INR-billed account, never for legal notices or debt recovery (R6 D-31); JioCX RCS becomes the primary signing-link channel once DLR and DLT binding tests pass (R4 D-R4-04); every Jio adapter OFF until DPA, India-processing and no-training terms are signed (R4 D-R4-02); counterparty rule `R4-COMMS-01` — at most one LawDocs-originated invitation to an unopened counterparty, no automated voice until opt-in (NN-34) |
| `ACCOUNTING_PORT` (P13 `lgo`) | TallyPrime through the on-premises agent (`svCurrentCompany` always set) and Zoho Books (India DC): read legal-vendor ledgers; push approved legal invoices as vouchers only after tenant maker-checker (NN-18) |
| `HRMS_SOURCE_PORT`, `CUSTOMER_CRM_PORT` | Customer HRMS joiner/leaver events trigger appointment letters and NDAs and deactivate leavers' approvals (minimal fields only; LDC is the source when it is HRMS SoR); customer CRM "deal won" opens a contract request and receives status updates — never document content unless the tenant enables expiring links. Infrabyx's own CRM is OH3 |
| `ACADEMY_PORT` (D-16) | FinLegal Academy catalogue by feed/API where Graphy supports it [VERIFY], deep links and SSO hand-off; never copy paid content |

**FR-P19-68 — Mapping packs.** Each connector ships a semantically versioned mapping pack (`mappings/<connector-id>/<version>/mapping.yaml`: JSON Pointer maps, code-table maps, transformations, validation rules, golden fixtures in CI; Spec §10.3). Tenants override only `x-tenant-overridable` fields by maker-checker, creating a patch version (`1.2.0+ten_01J…`); meaning-changing edits need recertification. Vidhi may propose a mapping from sample files; a human approves (NN-43).

### 4M. No-code automation and iPaaS

**FR-P19-69 — Zapier/Make-style triggers and actions.** A LawDocs app for Zapier and Make [VERIFY: partner terms and residency] built only on public contracts: triggers are REST-hook subscriptions to thin webhook events (Appendix I §I.7); actions are a safe set — create a contract request, create a draft from a template with supplied answers, upload a document to a folder, create a task, add a hearing date. No action can sign, send to a counterparty, share outside the tenant, pay, file or delete (`LD-INT-091`; NN-13). OAuth auth code + PKCE; tenant admin approval; per-tenant kill switch.

**FR-P19-70 — Power Automate and iPaaS.** A certified Power Automate custom connector for Microsoft 365 customers with the same actions (any approval happens in LawDocs, never in the flow); OpenAPI 3.1 and AsyncAPI 3.0 downloads per scope set, a Postman collection and import notes for Workato, MuleSoft and Boomi; a generic HMAC-verified inbound hook (`POST /v1/int/inbound-hooks/{hook_id}`) mapped by a mapping pack to a permitted action.

**FR-P19-71 — Data-class ceiling for automation.** Automation connections default to `INTERNAL`; raising one to `PII` needs `ORG_OWNER` approval, a warning that the platform may process data abroad, and a transfer-register entry (NN-25; R3 LG-069). `LEGAL`, `SPI`, `HR` and `CONSUMER_HELP` are never available to these platforms.

### 4N. Developer platform

**FR-P19-72 — Developer portal (`developers.lawdocs.in`).** Server-rendered (NN-31), WCAG 2.2 AA (NN-28), generated from contracts in CI (a contract change without a docs build fails the pipeline): quick start, authentication guides per client type, OpenAPI reference with try-it against sandbox only, AsyncAPI event catalogue, webhook signature samples (TypeScript, Python, Java, C#, PHP), error catalogue with help keys, rate limits, SDKs, Postman collection, mapping-pack and connector-SDK guides, changelog and deprecation calendar, status page, `/.well-known/security.txt`, API terms.

**FR-P19-73 — Sandbox tenants and test data.** Self-service sandbox (separate environment, CA and keys — Spec §3.7) seeded per persona: individual with a family vault; startup; SME with 40 agreements, 6 court cases and 3 trademarks; NBFC legal department with Finbyx recovery projections; practitioner workspace. Simulators for OH provisioning and entitlements, Finbyx litigation, Equator status and award, Udofin deposits; eSign/eStamp mocks including ESP downtime and decline; court-data and trademark mocks; a time-travel clock. Downloadable fixtures: template answer sets, sample PDF/DOCX with known hashes, signing-evidence samples, a sample `LD-EXPORT-1.0` archive, webhook payload examples, golden files per layout. Reset every `int.devportal.sandbox.auto_reset_hours` unless pinned; uploads containing Aadhaar or PAN patterns are rejected.

**FR-P19-74 — Client registration.** `DEV_ACCOUNT` sign-up (email verification, MFA) creates sandbox clients instantly; production clients are requested against a tenant and approved by its `ORG_ADMIN` (and `PLT_SECURITY_OFFICER` for certified-connector status). Each client records owner, purpose, scopes, `data_class_max`, environments, keys (JWKS URL or public key), redirect URIs, origins, expiry (≤ 12 months), optional IP allow-list. Click budget: ≤ 4 clicks from Settings → Integrations → API clients.

**FR-P19-75 — SDKs.** TypeScript (`@lawdocs/sdk`) and Python (`lawdocs`), generated from OpenAPI with helpers for `private_key_jwt`, idempotency keys, pagination, retries with jitter, webhook verification, problem details, pre-signed uploads and correlation ids; semantic versioning; SBOM and Sigstore provenance; supported for the current and previous API major.

**FR-P19-76 — Connector certification and catalogue.** Third-party connectors submit manifest, mapping pack, VAPT ≤ 12 months, sub-processor and residency statement and DPA; run the Spec §14.3 groups plus Appendix Y §Y.13; pass manual review; emit `ConnectorCertified`; recertify on schema, hosting, key or sub-processor change and annually. The tenant catalogue (Settings → Integrations) shows for each connector what data moves each way, data classes, residency, plan, pass-through costs, approvers, and how to undo.

**FR-P19-77 — API terms.** No resale of licensed vendor data obtained through LawDocs (R6 D-08), no scraping of LawDocs, no use of the API to build an advocate directory or ranking (NN-21).

### 4O. Integration health dashboard and operations

**FR-P19-78 — Tenant health dashboard (SCR-P19-14).** Per connector and link: state, last success, latency p95, error rate, DLQ depth, quota use, certificate/key expiry, residency check status, certification status, reconciliation result; per webhook subscription: success rate, last failure reason, auto-pause state. Health badges appear in context (e.g., on the litigation screen if the court-data adapter is degraded, with "showing data as of …").

**FR-P19-79 — Platform monitor (SCR-P19-16).** Cross-tenant metadata only: event lag per subject, DLQ depth, adapter error budgets, vendor incident status, ESP licence status, cost per adapter. No tenant payloads (NN-32). Alerts to on-call by severity; CERT-In 6-hour reporting clock opened automatically for qualifying incidents (NN-27).

**FR-P19-80 — Daily reconciliation.** By 06:00 IST: counts and hashes sent versus acknowledged per link (Spec §3.8, §7.4), entitlements as applied versus OH8, provisioning requests versus acknowledged tenants, usage statements versus source events before invoicing, eSign/eStamp vendor transactions versus LawDocs records (NN-46). Breaks raise `ReconciliationBreakRaised` and a task to the integration owner.

**FR-P19-81 — Circuit breakers and kill switches.** Per-tenant and per-adapter circuit breakers; kill switches for every adapter, ecosystem link kind and outbound channel (NN-39), operable by `PLT_SUPER_ADMIN` with `PLT_SECURITY_OFFICER` as checker to re-enable; a tenant admin can kill its own connectors instantly (no checker needed to switch off). Each toggle is audited and shown on the status page when it affects customers.

**FR-P19-82 — Status page.** Public status page (`status.lawdocs.in`) with component status (API, webhooks, signing, stamping, court data, messaging) and incident history; no claims of "real-time" third-party data (NN-20).

### 4P. MCP server and AI assistants (cross-reference)

**FR-P19-83 — MCP is P09.** The LawDocs MCP server for customers' own AI assistants and the MCP client registry are specified in P09. P19 supplies the OAuth 2.1 authorisation server profile (RFC 9728 metadata, audience-restricted tokens, no token pass-through), the scope and data-class engine, rate limits, the sharing ledger (an MCP read of tenant data by an external assistant is a ledger entry), and the kill switch. No MCP tool may sign, send, file, pay, share or delete (NN-13).

**FR-P19-84 — Regulatory-role boundary for lending (added at traceability review; ChatGPT prompt "LawDocs is not automatically an RE or LSP", Appendix Z TC-040).** LawDocs is a legal-technology and services platform. It is not a regulated lender, lending service provider (LSP), DSA/DMA, recovery agent or credit-information user, and no LawDocs or Consumer Help feature performs those activities: no loan sourcing, comparison or referral, no lead or data sale to lenders, no underwriting signals, no collection messaging on a lender's behalf and no bureau pulls (NN-05, NN-19, NN-23; P17 FR-P17-59). Where a tenant is itself a regulated entity, its own obligations (for example under the RBI Digital Lending Directions 2025 and the IT outsourcing directions [VERIFY current titles and paragraphs]) are mapped to that tenant's entity category in P13 (FR-P13-48, FR-P13-49) and P18 (FR-P18-20), and to LawDocsComply when the tenant also uses it (NN-47). A proposed feature that could bring LawDocs within those definitions (a loan marketplace, a lender referral fee, an embedded collection workflow, a Udofin cross-sell feed — see FR-P19-42) is a scope and revenue-stream change: it needs a counsel opinion recorded by `PLT_LEGAL_REVIEWER` and owner approval under P17 FR-P17-57/58 before any flag is registered, and the egress policy (Appendix I §I.14) keeps lender-lead and bureau endpoints blocked meanwhile.

## 5. Workflows and state machines

### 5.1 Connector instance (`int.connector_instances.state`)

```
AVAILABLE → REQUESTED (ORG_ADMIN; plan allows) → PREREQUISITES_PENDING (keys, consent, DPA, agent, vendor account)
→ CONFIGURED (maker: mapping pack + overrides) → APPROVED (checker ≠ maker; + ORG_CLO for LEGAL outbound; + PLT_DPO for a new PII+ cross-product flow)
→ TESTING (test transaction or sandbox replay) → ACTIVE ⇄ DEGRADED (auto: error budget or residency recheck)
ACTIVE/DEGRADED → SUSPENDED (kill switch, key/link expiry, residency fail, certification lapse; re-enable needs checker)
any → DISCONNECTING (drain outbox, final reconciliation, revoke tokens, export mapping history) → DISCONNECTED (ledger entry)
```
Every transition emits `in.lawdocs.int.ConnectorInstanceStateChanged.v1` and an audit entry; ACTIVE requires valid certification and keys valid ≥ 7 days; health probes run every 5 minutes.

### 5.2 Ecosystem link (`int.links.state`)

`PROPOSED` (either side) → `APPROVED_LOCAL` (tenant maker-checker) → `APPROVED_COUNTERPART` (counterpart product records its approval) → `CERTIFIED_CHECK` (both connectors hold valid `ConnectorCertified`; v1.2 contracts approved where needed) → `ACTIVE` ⇄ `PAUSED` (either side; messages queue, nothing dropped) → `EXPIRED` (`valid_to` reached) or `REVOKED` → `CLOSED`. A link without `valid_to` is invalid; default validity 12 months for tenant links, renewable by fresh approval; group-grant references follow Spec §4.6 (≤ 90 days).

### 5.3 Outbound delivery (per subscription or link)

```
outbox row → relay (FIFO per subject) → event_type_map lookup (internal → ecosystem? link active? dataclass ≤ ceiling? consentref/legalbasis present?)
  → no: drop to policy-reject log (no delivery) + sharing-ledger "blocked" entry if personal data was involved
  → yes: build envelope → sign (RFC 9421 + Standard Webhooks for ecosystem; Standard Webhooks HMAC for tenants) → POST
     → 2xx: DELIVERED (latency, code) → sharing-ledger entry (ecosystem only)
     → 408/429/5xx/timeout: RETRY (exp. back-off, full jitter, ≤ 72 h) → DLQ + alert
     → other 4xx: FAILED_PERMANENT → DLQ + alert
DLQ → replay requested (maker) → approved (checker) → re-enqueue with same event id
```

### 5.4 Inbound ecosystem message

```
receive (events.lawdocs.in, mTLS) → verify RFC 9421 + webhook timestamp (±5 min) + client cert ↔ client id
→ validate schema (pinned registry version) → consentref/legalbasis, dataclass ≤ LawDocs ceiling for that subject, tenant map resolves, link ACTIVE
→ inbox insert (source,id) [duplicate → 200 no-op] → seq check [gap → park 15 min → GET /v1/events catch-up → else ReconciliationBreakRaised]
→ module handler → 2xx after durable write → sharing-ledger entry
handler failure → internal retry → poison → inbox DLQ + integration incident
```

### 5.5 Partner onboarding batch and invitation

Batch: `RECEIVED → VALIDATING → VALIDATED` (dry run stops) `→ PREFILLING → INVITING → COMPLETED`, or `REJECTED`. Validation de-duplicates `partner_ref` and marks a CIN/GSTIN that is already a tenant as `ALREADY_CUSTOMER` (no invitation; the partner learns only "already registered"). Pre-fill runs the KYB ports in parallel and accepts partial results; invitations send one email per row and an SMS only with a DLT template.

State machine: Appendix A §A.2 governs (Resolution R-A-02); `iam.onboarding_invitations` is the single invitation record and `int.onboarding_invitations` holds the partner-batch row.

Invitation: `CREATED → SENT → OPENED → IDENTITY_VERIFIED → KYB_CONFIRMED → TERMS_ACCEPTED → ACTIVATED`; or `DECLINED`, `EXPIRED` (30 days), `BOUNCED`. `ACTIVATED` creates the tenant (P02), the consent artefact, `TenantRegistered` to OH, and the partner webhook.

### 5.6 Kernel system-of-record switch (LDC)

State machine: Appendix A §A.48 governs.

`PROPOSED` (ORG_ADMIN; same `org_id` in both products; impact preview by kernel) → `APPROVED` (ORG_OWNER ≠ maker, and the LDC admin) → `EXPORTING` (kernel writes frozen; layouts with hash-chain heads) → `IMPORTING` (LDC reconciles counts and hashes) → `DUAL_RUNNING` (≥ one board-meeting cycle or 30 days; LawDocs read-only with deep links) → `CUTOVER` (`SystemOfRecordSwitched`, proposed) → `RECONCILED` (signed report stored in the vault) → `CLOSED`; any failure → `ROLLBACK` (LawDocs remains SoR; nothing deleted).

### 5.7 Udofin deposit link

`NOT_LINKED → AUTHORISING` (PKCE flow) `→ LINKED` (consent + folder) `⇄ PAUSED` (user) `→ UNLINKED` (either side; deposits stop; saved copies remain). Each deposit: `RECEIVED → FETCHING → VERIFIED` (hash and JWS) `→ STORED` (`DocumentDeposited`) or `REJECTED` (hash mismatch `LD-INT-051`, wellness class, folder missing).

### 5.8 ADR referral transport through `ODR_PORT` (party view)

State machine: Appendix A §A.43 governs (Resolution R-A-15). The referral machine is **owned by P11** (`lit.adr_referrals`, `AdrReferralWorkflow`); P19 provides only the transport (`EquatorReferralWorkflow` for Equator, adapter routes for other providers) and the party-view projection. Mapping of the labels earlier drafts of this phase used: `DRAFT_PACK` = canonical `DRAFT`/`READY`; `OUTCOME_RECEIVED` = canonical `OUTCOME_RECORDED`. P19 adds no state of its own: it moves a referral from `APPROVED` to `SUBMITTED` (or `MANUAL_INTERIM` before Appendix Y is merged), projects provider states read-only from `adr.ADRCaseStatusChanged`, and delivers the outcome document by reference for P11 to record. Withdrawal before `SUBMITTED` is a user action with confirmation (NN-13); after it, only through the provider. Equator is one provider among those configured, never the default (§4I).

### 5.9 Hosted signing hand-off (API-initiated)

State machine: Appendix A §A.31 governs (signing request and participant); this is its API-initiated entry path.

`REQUESTED` (client API; idempotent) → `ELIGIBILITY_CHECKED` (Appendix F; ineligible → `WET_INK_PACK_OFFERED`, `LD-INT-061`) → `STAMP_PENDING` (if chargeable; stamp-before-sign) → `READY` (LawDocs signing URLs issued to the tenant user, never to the calling app as a frame target) → P08 ceremony states → `COMPLETED` (`SigningRequestCompleted` to the linked counterpart; evidence pack by reference) or `DECLINED`/`EXPIRED`/`WITHDRAWN`.

## 6. Screens and UX

| ID | App | Purpose and key components | Notes (empty/error, mobile, accessibility) |
|---|---|---|---|
| SCR-P19-01 | web (Company) | Integrations home: Category cards (Ecosystem, Signing and stamping, Identity, Courts and IP, Workplace, Messaging, Accounting, HRMS and CRM, Automation, Storage); status badges; "what data moves" panel | "No connections yet — start with Microsoft 365 or Google Workspace"; Mobile: Read-only list; setup deep-links to web; Cards are buttons with names; badges have text, not colour only |
| SCR-P19-02 | web | Connector setup wizard: Prerequisites checklist, consent text, mapping preview, test, approval request, undo explanation | Vendor unreachable → retry later, nothing saved; Mobile: Not offered; Step indicator announced; errors linked to fields |
| SCR-P19-03 | web | Connector detail and health: Health, logs (metadata), reconciliation, keys and expiry, kill switch, disconnect | Degraded banner with "as of"; Mobile: Health summary only; Kill switch has confirm dialog with focus trap |
| SCR-P19-04 | web | Infrabyx ecosystem connections: Links to OH, LDC, Finbyx, Udofin, Equator; state, purposes, contracts, `valid_to`, approvals; v1.2 status ("awaiting Ecosystem Spec v1.2 — manual channel in use") | No sister-product subscription → explainer; Mobile: Read-only; Table with header scope |
| SCR-P19-05 | web | Kernel system-of-record switch (LDC): Impact preview, approvals, progress by state, dual-running banner, reconciliation report | Same `org_id` not found → contact support; Mobile: Not offered; Progress region `aria-live=polite` |
| SCR-P19-06 | web | API clients and keys: Register, approve, scopes with data-class labels, keys (shown once), expiry, IP allow-list, last use | Mobile: Not offered; Copy buttons labelled; secrets masked |
| SCR-P19-07 | web | Webhooks: Subscriptions, event picker (catalogue), data-class ceiling, secret rotation, "Send test event" | Endpoint paused → resume; Mobile: Not offered |
| SCR-P19-08 | web | Delivery log and DLQ: Last 30 days metadata, filters, replay request (maker), approval queue (checker) | Mobile: Not offered |
| SCR-P19-09 | web | Sharing ledger (company): Filter by counterparty, purpose, basis, date; export CSV; record links | "Nothing shared yet"; Mobile: List view; Sortable table with keyboard |
| SCR-P19-10 | web + mobile (Personal) | Connected apps and sharing: Linked apps (e.g., Udofin), folder, last deposit, unlink; personal sharing ledger | "No connected apps"; Mobile: Full feature; unlink ≤ 2 taps; Large targets; screen-reader labels |
| SCR-P19-11 | partner portal (web) | Onboarding batches: Upload CSV/JSON, dry run, row errors, batch progress, invitation states, resend | Validation errors inline with row numbers; Mobile: Read-only status; Error summary at top |
| SCR-P19-12 | web (public route) | Invitation acceptance: Partner identity, DPDP notice, pre-filled KYB with source labels, plan and all-in price, terms, activate | Expired → request a new invite; Mobile: Full feature; OTP field labelled; no time pressure |
| SCR-P19-13 | web | Automation (Zapier, Make, Power Automate): Connected platforms, data-class ceiling, recipes gallery, kill switch | Mobile: Not offered |
| SCR-P19-14 | web | Integration health dashboard: Per connector/link/webhook health, quotas, alerts, reconciliation | All green summary; Mobile: Summary tiles; Tiles have text values |
| SCR-P19-15 | console | Platform connector catalogue and kill switches: Versions, certification, adapters per port, primary/fallback order, ESP licence status | — |
| SCR-P19-16 | console | Platform integration monitor: Lag, DLQ, error budgets, vendor incidents, costs (metadata only) | — |
| SCR-P19-17 | console | Certification workbench: Submissions, suite results, sign-off | — |
| SCR-P19-18 | console | Contract registry status: Pinned `contracts.lock`, Appendix Y subjects (PROPOSED/APPROVED), event-type map activation | — |
| SCR-P19-19 | developers | Portal home and quick start: Guides, "first call in 15 minutes" | Mobile: Responsive; Server-rendered; skip links |
| SCR-P19-20 | developers | API reference and try-it (sandbox): OpenAPI render, auth helper, problem examples | Mobile: Responsive; Code blocks with copy buttons |
| SCR-P19-21 | developers | Sandbox and test data: Tenants by persona, simulators, time-travel, reset | — |
| SCR-P19-22 | developers | SDKs, events and changelog: SDK downloads, AsyncAPI catalogue, deprecation calendar | Mobile: Responsive |

**Click budgets.** Connect Microsoft 365: ≤ 5 clicks from Settings (admin consent hand-off counts as one). Create a webhook: ≤ 4 clicks. Request a DLQ replay: ≤ 3 clicks (plus checker approval). Link Udofin for deposits: ≤ 3 taps after LawDocs sign-in. Activate an invited company: ≤ 4 taps from the email. Find a sharing record for a document: ≤ 3 clicks from the document (Document → Activity → Shared with).

**Customisation hooks (tenant Settings).** Webhook data-class ceilings per subscription; default vault folder for each deposit link; automation recipe allow-list; rate-limit alert thresholds; integration owner and alert recipients; partner-batch notification language; ICS/Graph calendar mode; which ecosystem projections are visible to which roles.

**"i" help keys.** `hlp.int.scopes`, `hlp.int.data_class`, `hlp.int.webhook_signatures`, `hlp.int.idempotency`, `hlp.int.dlq_replay`, `hlp.int.sharing_ledger`, `hlp.int.sor_switch`, `hlp.int.hosted_signing`, `hlp.int.no_esign_sublet`, `hlp.int.deposit_link`, `hlp.int.adr_routes`, `hlp.int.equator_disclosure`, `hlp.int.partner_invite`, `hlp.int.kyb_prefill_sources`, `hlp.int.dlt`, `hlp.int.zapier_ceiling`, `hlp.int.court_data_staleness`, `hlp.int.mapping_pack`.

## 7. Backend design

### 7.1 Modules

`int` (owner; schema `int`). Collaborators: `iam` (Keycloak clients, consent screens, SCIM), `core` (outbox, audit ledger, IDs), `cfg` (settings, flags, mapping-pack overrides), `kyc` (KYB/identity journeys calling ports), `dms` (deposits, document references), `sgn` (hosted signing hand-off), `lit`, `ipm`, `clm`, `gov`, `hr`, `lgo`, `mkp`, `bil` (OH8 calls), `ntf` (channel adapters), `xpt` (exports of `int` records), `hlp` (help keys), `rpt` (health dashboards), `eng` (release evidence).

### 7.2 Tables (schema `int`; RLS on every tenant table — NN-01)

| Table | Key columns | RLS | Retention |
|---|---|---|---|
| `int.clients` | client_id, tenant_id (null for ecosystem/platform), type, owner_user_id, purpose, scopes[], data_class_max, auth_method, jwks_uri, cert_thumbprint, redirect_uris[], allowed_origins[], ip_allowlist[], expires_at, status | tenant | Life of client + 7 y |
| `int.client_tenant_consents` | client_id, tenant_id, scopes[], granted_by, granted_at, revoked_at, consent_id (`cns_`) | tenant | 7 y |
| `int.api_keys` | key_id, client_id, prefix, hash (Argon2id), scopes[], expires_at, last_used_at | tenant | 7 y |
| `int.idempotency_keys` | client_id, key, body_hash, status, response_ref, expires_at | tenant | 24 h / 7 d |
| `int.webhook_subscriptions` | sub_id, tenant_id, url, event_types[], data_class_max, secret_refs[], status, paused_reason, created_by | tenant | Life + 1 y |
| `int.deliveries` | delivery_id, sub_id/link_id, event_id, attempt, status, http_status, latency_ms, next_attempt_at | tenant | 90 d (metadata) |
| `int.inbox` | source, event_id, business_key, subject, seq, received_at, processed_at, status | tenant | 365 d |
| `int.dlq` | dlq_id, direction, ref, reason, attempts, first_failed_at, expires_at, replay_request_id | tenant | 30/90 d |
| `int.replay_requests` | request_id, scope_filter_json, count_preview, requested_by, approved_by, state | tenant | 7 y |
| `int.event_type_map` | internal_type, ecosystem_type, direction, link_kind, dataclass_ceiling, transform_ref, contract_status | platform | Versioned |
| `int.links` | link_id, kind, tenant_id or user_id, counterpart_product, counterpart_org_id, counterpart_tenant, purposes[], dataclasses[], contracts[], valid_from, valid_to, approvals_json, state | tenant | Life + 8 y |
| `int.sharing_ledger` | entry_id, tenant_id or user_id, direction, link_id, counterparty, contract, purpose, consentref, legalbasis, record_ids[], payload_sha256, dataclass, outcome, prev_hash | tenant / user | 8 y (append-only) |
| `int.connectors` | connector_id, version, port, category, manifest_json, capabilities[], scopes[], dataclasses[], residency, certification_state, certified_at, recert_due, kill_switch_key | platform | Versioned |
| `int.connector_instances` | instance_id, tenant_id, connector_id, version, state, config_ref, mapping_pack_version, owner_user_id, approved_by, health_state, last_success_at | tenant | Life + 1 y |
| `int.mapping_packs`, `int.mapping_overrides` | pack_id, version, yaml_ref, sha256; overrides with patch version, maker, checker | platform / tenant | Versioned |
| `int.partners` | partner_id, legal_name, partner_type, agreement_ref, regulated_professional (bool; blocks revenue-share if true), status | platform | Life + 8 y |
| `int.onboarding_batches` | batch_id, partner_id, row_count, state, dry_run, created_at | partner | 3 y |
| `int.onboarding_invitations` | invitation_id, batch_id, partner_ref, org snapshot ref, signatory contact (encrypted), state, expires_at, activated_tenant_id | partner + platform | 3 y; contact erased 90 d after EXPIRED/DECLINED |
| `int.sor_switches` | switch_id, tenant_id, kernel (GOVERNANCE, HRMS), from_product, to_product, state, report_doc_id | tenant | 8 y |
| `int.deposit_links` | link_id, user_id, client_id, folder_id, pairwise_ref, state | user | Life + 1 y |
| `int.reconciliation_reports` | link_id, business_date, sent_count, ack_count, hash_sent, hash_ack, breaks_json | tenant | 8 y |
| `int.rate_limit_overrides` | tenant_id, tier, limits_json, approved_by, valid_to | platform | 3 y |
| `int.sandbox_tenants` | sandbox_id, dev_account_id, persona, pinned, reset_at | sandbox | 30 d after last use |

### 7.3 APIs (P19-owned; full catalogue in Appendix I §I.5)

| Method and path | Purpose | Scope | Idempotency |
|---|---|---|---|
| `GET /v1/events?after=&types=&limit=` | Ecosystem catch-up feed of LawDocs-produced events | per contract | n/a |
| `POST /v1/int/inbound/{link_id}` (`events.lawdocs.in`) | Ecosystem push receiver | mTLS + RFC 9421 | inbox `(source,id)` |
| `GET/POST/PATCH/DELETE /v1/int/webhook-subscriptions` | Tenant webhooks | `int.webhook:manage` | Yes |
| `POST /v1/int/webhook-subscriptions/{id}/test` | Test event | `int.webhook:manage` | Yes |
| `GET /v1/int/deliveries`, `POST /v1/int/replay-requests`, `POST /v1/int/replay-requests/{id}/approval` | Delivery log and DLQ replay | `int.webhook:manage`; approval needs a different user | Yes |
| `GET/POST/PATCH /v1/int/clients`, `POST /v1/int/clients/{id}/keys` | API clients | `int.client:manage` | Yes |
| `GET /v1/int/sharing-ledger` | Ledger (tenant or personal) | `int.ledger:read` | n/a |
| `GET/POST /v1/int/links`, `POST /v1/int/links/{id}/approval` | Ecosystem links | `int.link:manage` | Yes |
| `POST /v1/int/sor-switches`, `POST /v1/int/sor-switches/{id}/approval` | Kernel SoR switch | `int.link:manage` + ORG_OWNER | Yes |
| `POST /v1/int/partner/onboarding-batches` (`?dry_run=`), `GET …/{id}`, `GET …/{id}/rows` | Partner batches | `partner.onboarding:write` / `:read` | Yes |
| `POST /v1/int/partner/onboarding-invitations`, `POST …/{id}/resend` | Single invitation | `partner.onboarding:write` | Yes |
| `PUT /v1/provisioning-requests/{id}` (LawDocs → OH) | Acknowledge `TenantProvisioned` | `ops.provisioning:ack` | Yes |
| `GET /v1/tenants/{tenantid}/provisioning-status` | OH fallback poll | `ops.tenant:provision` (OH only) | n/a |
| `GET /v1/entitlements?tenant=` | OH8 reconciliation | `platform.entitlement:read` (OH only) | n/a |
| `POST /v1/document-deposits` (proposed, Appendix Y) | Udofin deposit | `documents.deposit:write` (delegated) | Yes |
| `POST /v1/signing-requests`, `GET …/{id}`, `POST …/{id}/withdrawal`, `GET …/{id}/evidence-pack` (ecosystem path, Appendix Y §Y.8) — gateway route only: P08 owns the resource and implementation (`/v1/sgn/requests…`, P08 §7.3); P19 owns the route, client approval, scopes and sublet checks | Hosted signing hand-off | `esign.request:create` / `:read` | Yes |
| `GET /v1/template-packs/{pack}/versions/{v}` | Template packs to Finbyx/LDC/OH | `templates.pack:read` | n/a |
| `GET /v1/contract-obligations?updated_since=`, `GET /v1/legal-matters?updated_since=` | LDC pulls | `legal.obligation:read`, `legal.matter:read` | n/a |
| `POST /v1/int/inbound-hooks/{hook_id}` | Generic automation inbound | HMAC | Yes |
| `GET /v1/int/health` | Tenant integration health | `int.health:read` | n/a |
| `/scim/v2/Users`, `/scim/v2/Groups` | SCIM for customer IdPs (P01 owns UX) | SCIM bearer (per tenant) | n/a |

### 7.4 Domain events

**Internal (`in.lawdocs.int.*.v1`):** `ApiClientRegistered`, `ApiClientApproved`, `ApiClientRevoked`, `ApiKeyIssued`, `SecretRotated`, `WebhookSubscriptionCreated`, `WebhookEndpointPaused`, `WebhookDeliveryFailed`, `DlqReplayRequested`, `DlqReplayApproved`, `ConnectorInstanceStateChanged`, `EcosystemLinkStateChanged`, `SharingLedgerEntryRecorded`, `OnboardingBatchSubmitted`, `OnboardingInvitationSent`, `OnboardingInvitationAccepted`, `OnboardingInvitationDeclined`, `OnboardingInvitationExpired`, `SorSwitchStateChanged`, `DepositLinkCreated`, `DepositLinkRevoked`, `ReconciliationBreakDetected`, `RateLimitTierChanged`, `WebhookTest`. Adapter and connector kill switches emit the canonical `in.lawdocs.cfg.KillSwitchEngaged.v1` / `cfg.KillSwitchReleased.v1` with scope `VENDOR_ADAPTER` or `CONNECTOR` (Resolution R-A-09; the former `int.KillSwitchToggled` is retired). Deposits are stored by `dms` and emit `in.lawdocs.dms.DocumentDeposited.v1`, which `int` maps to `documents.DocumentDeposited` (Appendix B §B.4.2).

**Ecosystem — produced by `int` (v1.1 now):** `UsageRecorded`, `ModuleAttached`, `ModuleDetached`, `ReconciliationBreakRaised`, `ConnectorCertified` (via certification service), `DocumentShared`, `ConsentRecorded`, `ConsentWithdrawn`, `DataPrincipalRequest`, `ExportRequested`/`ExportCompleted`/`StorageTargetConnected`/`BackupCompleted`/`RestoreTested` (P20 data), `ReleasePublished`/`ControlEvidenceCollected` (P23 data), `SecurityIncidentNotified` copies without personal data. **Proposed (Appendix Y §Y.7; inert until approved):** the `legal`, `esign`, `ip` and `engagement` domains, plus `DocumentDeposited`, `TenantRegistered`, `SystemOfRecordSwitched`, LawDocs as producer of `ADRReferralCreated` and `MatterAllocated`; `ops.ServiceOrderRouted` and `ops.ServiceOrderStatusChanged` (P14/P16; §Y.7.9); `billing.MarketplaceTransferInstructed` and `billing.ServiceCreditIssued` (P16/P18); `ops.TenantSelfServeCreated`, `ops.ClientHealthSignal`, `ops.SurveyResponseRecorded`, `ops.TimesheetAggregated`, `ops.DeliveryMetricsMonthly`, `ops.ContentPublished`, `ops.GrievanceStatusChanged` (P18/P21; §Y.7.10); and the token-exchange launch for same-organisation customers (§Y.3.6; OI-P01-12). Mapping table: Appendix I §I.8.

**Ecosystem — consumed:** `TenantProvisioned`, `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`, `SupportTicketOpened`, `SupportTicketResolved`, `ImplementationMilestoneReached`, `ProfessionalEmpanelled`, `ProfessionalSuspended`, `ChangeApproved`, `LegalHoldChanged`, `ConsentWithdrawn`, `DataPrincipalRequest`; proposed: `litigation.*` (LD as consumer), `adr.*` party view, `governance` facts under `LDC_SOR`, `MarketplacePayoutSettled`, `ops.ServiceOrderStatusChanged`, `EmployeeOffboarded` (OH10 → leaver sweep, P18).

### 7.5 Jobs and Temporal workflows

`OutboxRelay` (continuous), `WebhookDeliveryWorker`, `EcosystemPushWorker`, `InboxProcessor`, `GapCatchUp` (15-minute park), `DailyReconciliation` (06:00 IST), `EntitlementReconciliation` (daily with OH8), `UsageStatementBuilder` (monthly WD+3, daily provisional), `PartnerBatchWorkflow` (validate → prefill → invite), `InvitationExpiryJob`, `SorSwitchWorkflow`, `DepositFetchWorkflow`, `EquatorReferralWorkflow`, `HostedSigningHandOffWorkflow` (delegates to P08), `KeyAndCertExpiryWatcher` (30/7/1 days), `ConnectorHealthProbe` (5 min), `EspLicenceWatcher` (nightly; R3 LG-005), `ResidencyRecheck` (weekly for storage targets), `DeprecationUsageReport` (monthly), `SandboxReset` (per setting), `DlqExpiry`, `LedgerAnchor` (daily hash anchor).

### 7.6 Error codes (`LD-INT-001`–`LD-INT-099`; model in Appendix I §I.10)

| Code | Meaning | User message (summary) | Help key |
|---|---|---|---|
| LD-INT-001 | Client not authorised for this tenant | "This app is not approved for your organisation. Ask your admin." | `hlp.int.scopes` |
| LD-INT-002 | Scope insufficient (`scope-insufficient`) | "This app needs more access than it was given." | `hlp.int.scopes` |
| LD-INT-003 | Step-up required (`acr`) | "Confirm with your second factor to continue." | `hlp.int.scopes` |
| LD-INT-010 | Token expired or wrong audience | "Session for this app expired. Reconnect it." | — |
| LD-INT-011 | Signature verification failed (RFC 9421 / webhook) | "Message signature invalid." | `hlp.int.webhook_signatures` |
| LD-INT-012 | Client certificate does not match client | "Certificate not recognised for this client." | — |
| LD-INT-020 | Idempotency-Key missing on state change | "Add an Idempotency-Key header." | `hlp.int.idempotency` |
| LD-INT-021 | Key reused with a different body (422) | "This key was used for a different request." | `hlp.int.idempotency` |
| LD-INT-022 | Request still in progress (409) | "Your earlier request is still running." | `hlp.int.idempotency` |
| LD-INT-030 | Data class above ceiling (`dataclass-not-permitted`) | "This connection is not allowed to carry this kind of data." | `hlp.int.data_class` |
| LD-INT-031 | Consent or legal basis missing (`consent-missing`) | "A consent or legal basis is required for this data." | `hlp.int.sharing_ledger` |
| LD-INT-032 | No active ecosystem link | "This product is not connected for your organisation." | `hlp.int.sharing_ledger` |
| LD-INT-033 | Contract not yet approved (Appendix Y pending) | "This exchange awaits group approval; use the manual channel." | `hlp.int.sharing_ledger` |
| LD-INT-034 | Residency blocked (`residency-blocked`) | "This destination is outside India for this data." | `hlp.int.data_class` |
| LD-INT-035 | Ethical-wall block (Consumer Help) | "This connection is not available for Consumer Help cases." | `hlp.int.data_class` |
| LD-INT-040 | Quota exhausted | "Monthly API quota reached. Reads and exports still work." | — |
| LD-INT-041 | Rate limited (`rate-limited`, 429) | "Too many requests. Retry after the time shown." | — |
| LD-INT-050 | Webhook endpoint rejected (private IP, invalid certificate) | "This endpoint address is not allowed." | `hlp.int.webhook_signatures` |
| LD-INT-051 | Deposited document hash or JWS mismatch | "The document changed in transit and was not saved." | `hlp.int.deposit_link` |
| LD-INT-052 | Deposit link inactive or folder missing | "Your link to this app is paused or the folder was removed." | `hlp.int.deposit_link` |
| LD-INT-060 | eSign route requested by a non-LawDocs application (sublet attempt) | "Signing happens in LawDocs. Use the signing link." | `hlp.int.no_esign_sublet` |
| LD-INT-061 | Instrument not eligible for eSign (hand-off) | "This document cannot be eSigned; a wet-ink pack is offered." | `hlp.int.hosted_signing` |
| LD-INT-062 | Framing of signing page refused | "Open the signing page in a new tab." | `hlp.int.hosted_signing` |
| LD-INT-070 | Partner batch row invalid | Row-level message with field pointer | `hlp.int.partner_invite` |
| LD-INT-071 | Partner not permitted (regulated-professional revenue share) | "This partner type cannot receive revenue share." | `hlp.int.partner_invite` |
| LD-INT-072 | Bulk onboarding of individuals refused | "Individuals must register themselves." | `hlp.int.partner_invite` |
| LD-INT-080 | Connector suspended (kill switch) | "This integration is switched off." | — |
| LD-INT-081 | Connector certification lapsed | "This integration needs recertification." | — |
| LD-INT-082 | Vendor dependency unavailable (`dependency-unavailable`) | "Provider unavailable; we will retry or use the fallback." | — |
| LD-INT-090 | Regulator/portal domain blocked by egress policy | "Automated access to that portal is not permitted." | `hlp.int.court_data_staleness` |
| LD-INT-091 | Automation action not permitted (irreversible) | "This action needs a person to confirm in LawDocs." | `hlp.int.zapier_ceiling` |

## 8. Integrations

Ports, primary and fallback vendors, legality, status and kill switches are binding in Appendix I §I.2; ecosystem connectors in Appendix I §I.4. Failure rules common to all ports: (1) a port failure never blocks reading or exporting the customer's own data (NN-11); (2) every port has a fallback vendor or a manual path — wet-ink pack for eSign, uploaded stamp certificate with UIN check for eStamp, manual entry with document upload for KYB, user-entered CNR and uploaded orders for court data, uploaded status PDF for trademarks, ICS feed for calendars, signed pack download for ODR, email for messaging; (3) OH8 unavailability keeps the last signed entitlement for 30 days and queues orders (Spec §6.27); (4) stale third-party data is labelled with its "as of" time, never presented as live (NN-20).

## 9. Settings and configuration (register in Appendix R before code reads them — NN-29)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `int.gateway.public_api.enabled` | PLATFORM | bool | true | PLT_SUPER_ADMIN | Y |
| `int.auth.access_token_ttl_seconds` | PLATFORM | int | 600 | PLT_SECURITY_OFFICER | Y |
| `int.auth.secret_rotation_days` | PLATFORM | int | 90 | PLT_SECURITY_OFFICER | Y |
| `int.auth.api_keys.production_scopes` | PLATFORM | enum list | `[READ_ONLY]` | PLT_SECURITY_OFFICER | Y |
| `int.auth.client_max_validity_months` | PLATFORM | int | 12 | PLT_SECURITY_OFFICER | Y |
| `int.webhooks.max_endpoints` | PLAN | int | Free 0 · Personal 0 · Pro 3 · Business 20 · Enterprise 100 | PLT_SUPER_ADMIN (catalogue) | Y |
| `int.webhooks.data_class_max_default` | TENANT | enum | `INTERNAL` | ORG_ADMIN (raise needs ORG_OWNER) | Y |
| `int.webhooks.retry_window_hours` | PLATFORM | int | 72 | PLT_SRE | Y |
| `int.webhooks.auto_pause_after_hours` | PLATFORM | int | 24 | PLT_SRE | N |
| `int.dlq.retention_days` | PLATFORM | int | 30 (ecosystem 90) | PLT_SRE | Y |
| `int.dlq.replay_requires_checker` | PLATFORM | bool | true (locked) | — | — |
| `int.ratelimit.tier` | PLAN | enum | per plan (Appendix I §I.9) | PLT_SUPER_ADMIN | Y |
| `int.ratelimit.override` | TENANT | json | null | PLT_SUPER_ADMIN (Enterprise) | Y |
| `int.quota.soft_block_at_pct` | PLAN | int | 100 | PLT_SUPER_ADMIN | Y |
| `int.eco.v12_contracts.enabled` | PLATFORM | bool | false | PLT_SUPER_ADMIN + PLT_SECURITY_OFFICER | Y |
| `int.eco.ldc.sor_mode.governance` / `.hrms` | TENANT | enum `LOCAL`/`LDC` | `LOCAL` | ORG_ADMIN (maker), ORG_OWNER (checker) | Y |
| `int.eco.ldc.projections.enabled` | TENANT | bool | false | ORG_CLO | Y |
| `int.eco.finbyx.litigation_projection.enabled` | TENANT | bool | false | ORG_CLO | Y |
| `int.eco.finbyx.signing_handoff.enabled` | TENANT | bool | false | ORG_ADMIN | Y |
| `int.eco.udofin.deposit.enabled` | PLATFORM | bool | false (until connector certified) | PLT_SUPER_ADMIN | Y |
| `int.eco.udofin.deposit.default_folder` | USER | string | `05 Finance, Loans and Insurance/From Udofin` | IND_OWNER | N |
| `int.eco.equator.referral.enabled` | TENANT | bool | false | ORG_CLO | Y |
| `int.eco.equator.show_alternatives` | PLATFORM | bool | true (locked) | — | — |
| `int.chp.ecosystem_clients.allowlist` | BRAND | list | `[]` (locked) | — | — |
| `int.partner.onboarding.max_batch_rows` | PLATFORM | int | 500 | PLT_SUPER_ADMIN | Y |
| `int.partner.onboarding.invite_expiry_days` | PLATFORM | int | 30 | PLT_SUPER_ADMIN | N |
| `int.partner.onboarding.kyb_prefill.enabled` | PLATFORM | bool | true | PLT_SUPER_ADMIN | Y |
| `int.partner.individual_bulk.enabled` | PLATFORM | bool | false (locked for ecosystem clients) | PLT_SUPER_ADMIN + PLT_DPO | Y |
| `int.esign.api_initiation.enabled` | TENANT | bool | false | ORG_ADMIN | Y |
| `int.esign.hosted_ceremony.framing_allowed` | PLATFORM | bool | false (locked) | — | — |
| `int.adapter.<adapter_id>.enabled` | PLATFORM | bool | per Appendix I §I.2 | PLT_SUPER_ADMIN (on needs PLT_SECURITY_OFFICER) | Y |
| `int.connector.<connector_id>.tenant_enabled` | TENANT | bool | false | ORG_ADMIN (off without checker) | Y (on) |
| `int.automation.platforms_allowed` | TENANT | enum list | `[]` | ORG_ADMIN | Y |
| `int.automation.data_class_max` | TENANT | enum | `INTERNAL` | ORG_OWNER | Y |
| `int.devportal.sandbox.auto_reset_hours` | PLATFORM | int | 24 | PLT_SRE | N |
| `int.health.alert_recipients` | TENANT | user list | ORG_ADMIN | ORG_ADMIN | N |
| `int.status_page.enabled` | PLATFORM | bool | true | PLT_SRE | N |
| `int.sharing_ledger.user_visible` | PLATFORM | bool | true (locked) | — | — |

## 10. Security, privacy and audit

**Threats and controls.**

| Threat | Control |
|---|---|
| BOLA/IDOR across tenants | RLS deny-by-default; Cerbos per call; BOLA suite with second-tenant ids for every endpoint (NN-01) |
| Token theft and replay | Short-lived, audience-restricted, sender-constrained tokens (mTLS/DPoP); refresh rotation with reuse detection; RFC 9421 for ecosystem |
| Webhook SSRF | Resolve-time IP checks, no redirects, egress proxy, allow-listed ports 443 only |
| Forged inbound events | mTLS identity ↔ client mapping, signature and timestamp checks, schema validation, inbox de-duplication |
| Data over-sharing to sister products | Event-type map with data-class ceilings, link checks, consent/legal-basis enforcement, sharing ledger, DPO approval for new `PII`+ flows (NN-19, NN-24) |
| eSign sub-letting | No ESP credential reachable by any client; framing blocked; sublet attempts rejected (`LD-INT-060`) and alerted (NN-06) |
| Ethical-wall breach (Consumer Help) | `CONSUMER_HELP` data class (proposed) never mapped to any ecosystem subject; locked empty allow-list; wall breaches logged and reviewed monthly (NN-23) |
| Portal scraping by a connector | Egress allow-list per manifest; CI test for blocked domains; certification "Filing boundaries" group (NN-05) |
| Vendor compromise | Out-of-process connectors, least-privilege secrets, SBOM, VAPT ≤ 12 months, kill switch |
| Residency drift | India-only hosting for queues, DLQs, logs and backups; vendor residency evidence; transfer register for any abroad processing (NN-25) |

**Data classes.** `int` itself holds metadata (`INTERNAL`), client and partner contacts (`PII`), signatory contacts in invitations (`PII`, erased 90 days after expiry/decline), sharing-ledger record ids (`INTERNAL`) and hashes. Payload bodies are never stored in `int` except inbox/outbox rows for their retention window, encrypted per tenant.

**Audit events.** Client registration/approval/revocation, key issue and rotation, scope changes, webhook create/change/pause, DLQ replay request and approval, link and SoR-switch transitions, connector state changes, kill-switch toggles, partner batch submission and invitation outcomes, every sharing-ledger entry, every policy rejection. All in the same transaction as the change (NN-45), hash-chained (NN-02).

**DPDP.** Purpose-specific consent for deposits, referral packs and partner invitations; withdrawal stops future flows within 1 hour and is propagated as `ConsentWithdrawn` (Spec §6.14); data-principal requests forwarded within 1 working day; the sharing ledger satisfies "who received my data" requests. CERT-In: 180-day India log retention (400 days default), NTP sync, 6-hour incident reporting (NN-27). DigiLocker incidents also start a 24-hour NeGD clock (R3 LG-038).

**Export-map entries (`xpt.export_map`; NN-11).**

| Record type | Folder in `LD-EXPORT-1.0` |
|---|---|
| `int.sharing_ledger` | `99 System Data (CSV and JSON)/Integrations/sharing-ledger.csv` (individuals: `99 System Data/Integrations/`) |
| `int.clients`, `int.client_tenant_consents` (metadata, no secrets) | `99 System Data (CSV and JSON)/Integrations/api-clients.csv` |
| `int.webhook_subscriptions` (no secrets), `int.deliveries` (90 days) | `99 System Data (CSV and JSON)/Integrations/webhooks.csv`, `webhook-deliveries.csv` |
| `int.links`, `int.sor_switches` (+ reconciliation reports as PDF) | `99 System Data (CSV and JSON)/Integrations/ecosystem-links.csv`; reports under `01 Company Profile/System of record changes/` |
| `int.connector_instances`, `int.mapping_overrides` | `99 System Data (CSV and JSON)/Integrations/connectors.csv`, `mapping-overrides/` |
| `int.deposit_links` | `99 System Data/Integrations/connected-apps.csv` |
| `int.onboarding_invitations` (for the activated company: its own invitation record) | `01 Company Profile/Onboarding/` |

## 11. AI touchpoints and guardrails

Vidhi touchpoints: mapping-pack proposals from sample files (an in-session Vidhi skill run by the maker; the Appendix H roster has no integration-mapper agent, so none may run as an agent until P09 adds one to Appendix H — X-27; output is a draft the maker approves and a checker publishes), webhook-filter and recipe suggestions (L1), integration-incident summaries for SRE review (L1), ADR route explanations (L1, information only; the user chooses and a referral needs CLO approval or individual step-up — NN-13), and partner row-error explanations (L1).

Guardrails: agents never approve clients, enable connectors, replay DLQs, raise data-class ceilings, create referral packs for submission or initiate signing (NN-43, NN-13). Prompts and tool outputs pass the PII/secret scrubber; integration logs given to Vidhi are metadata only (NN-15, NN-32). Evaluation: mapping proposals scored against golden fixtures (≥ 95% field accuracy before L2 is allowed for a connector).

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p19/*.feature`)

```gherkin
Feature: P19 integration gateway, ecosystem connectors and developer platform

  @P19-AT-01 @NN-01
  Scenario: Cross-tenant id is rejected
    Given client "erp-acme" is approved for tenant "Acme"
    When it calls GET /v1/clm/agreements/{id} with an agreement id of tenant "Beta"
    Then the response is 404 with no data and no existence leak (P00 FR-P00-31)
    And an audit event "authz.denied" is written

  @P19-AT-02 @NN-46
  Scenario: Idempotency key reuse with a different body
    Given a POST /v1/signing-requests succeeded with Idempotency-Key K
    When the same client repeats the call with key K and a different body
    Then the response is 422 with code "LD-INT-021"
    And no second signing request exists

  @P19-AT-03
  Scenario: Webhook retries then DLQ
    Given a tenant webhook endpoint returns 503 for 73 hours
    Then the endpoint is auto-paused after 24 hours and the subscription owner is notified
    And new events for the endpoint are held, not dropped
    And deliveries already in retry continue with exponential back-off and jitter until 72 hours
    And then land in the DLQ with reason "RETRY_EXHAUSTED"

  @P19-AT-04 @NN-18
  Scenario: DLQ replay needs a different approver
    Given admin "Asha" requests a replay of 40 DLQ items
    When "Asha" tries to approve her own request
    Then approval is refused
    When admin "Vikram" approves
    Then 40 events are re-enqueued with their original event ids

  @P19-AT-05 @NN-24
  Scenario: Personal data without consent or legal basis is rejected
    Given an inbound ecosystem event carries a party name
    And it has neither consentref nor legalbasis
    Then the gateway rejects it with "consent-missing" and code "LD-INT-031"
    And nothing is written to the inbox

  @P19-AT-06 @NN-38
  Scenario: Appendix Y contracts are inert until approved
    Given "int.eco.v12_contracts.enabled" is OFF
    When an agreement is executed in a tenant linked to LawDocsComply
    Then no "AgreementExecuted" ecosystem event is published
    And the sharing ledger shows no ecosystem entry

  @P19-AT-07 @NN-06
  Scenario: A sister product cannot use LawDocs' ESP route
    Given the Finbyx service client requests ESP credentials or a raw eSign transaction
    Then the request is refused with "LD-INT-060"
    And a security event "esign.sublet_attempt" is raised

  @P19-AT-08 @NN-06
  Scenario: Hosted signing hand-off keeps the ceremony in LawDocs
    Given RE tenant "Alpha NBFC" is a LawDocs customer and approved client "finbyx-alpha" with scope "esign.request:create"
    When "finbyx-alpha" creates a signing request for an eligible loan agreement
    Then signing links are issued to the Alpha NBFC user on sign.lawdocs.in
    And the signing page sends "Content-Security-Policy: frame-ancestors 'none'"
    And on completion "SigningRequestCompleted" carries the ESP transaction id and signed hash but no consent logs

  @P19-AT-09 @NN-07
  Scenario: Ineligible instrument via API gets a wet-ink pack
    When a client creates a signing request for a general power of attorney
    Then the response is 422 with code "LD-INT-061"
    And a wet-ink, notary and registration checklist pack is offered

  @P19-AT-10 @NN-19
  Scenario: The Operations Hub receives aggregates only
    When the monthly usage statement is sent to OH8
    Then "UsageRecorded" contains tenant, meter, period and quantity
    And it contains no user, document, agreement or matter identifier
    And a seeded document id in the payload makes the certification test fail with "dataclass-not-permitted"

  @P19-AT-11 @NN-23
  Scenario: No ecosystem client can reach Consumer Help
    Given the Udofin service client holds a valid certificate
    When it calls any /v1/chp/* endpoint
    Then the response is 403 with code "LD-INT-035"
    And the wall-breach log records the attempt

  @P19-AT-12
  Scenario: Udofin deposit is verified and immutable
    Given individual "Meena" linked Udofin with folder "From Udofin"
    When Udofin deposits a sanction letter with sha256 H and a valid JWS
    Then LawDocs fetches the bytes, verifies H, stores the file under Object Lock with origin "RECEIVED_FROM_PRODUCT"
    And "DocumentDeposited" is returned and the personal sharing ledger shows the entry
    When a deposit arrives whose bytes do not match H
    Then it is rejected with "LD-INT-051" and nothing is stored
    When a deposit message declares dataclass "WELLNESS"
    Then it is rejected with "dataclass-not-permitted"

  @P19-AT-13 @NN-47
  Scenario: Kernel system-of-record switch to LawDocsComply loses nothing
    Given tenant "Beta Ltd" runs the governance kernel locally with 120 resolutions
    When ORG_ADMIN proposes and ORG_OWNER approves switching governance to LDC
    Then LawDocs exports 120 resolutions with the hash-chain head
    And LDC reports 120 imported with a matching head
    And during DUAL_RUNNING LawDocs refuses new governance writes with a deep link to LDC
    And on failure the switch rolls back with LawDocs still the system of record

  @P19-AT-14
  Scenario: Finbyx recovery litigation is read-only in LawDocs
    Given the CLO enabled the Finbyx litigation projection
    When "LitigationCaseUpdated" arrives with stage "EVIDENCE"
    Then the recovery proceeding shows stage "EVIDENCE" with "source: Finbyx Recovery Suite"
    And editing the proceeding in LawDocs is not possible

  @P19-AT-15
  Scenario: Equator is shown neutrally with disclosure
    Given an agreement's dispute clause names no institution
    When the user opens "Resolve this dispute"
    Then Equator appears with "Equator Resolution is an Infrabyx group company" alongside other providers
    And arbitration is shown as needing written post-dispute consent
    And nothing is pre-selected

  @P19-AT-16 @NN-13
  Scenario: Referral pack needs human approval
    Given Vidhi drafted a referral pack for matter "LD-MAT-2026-000045"
    When no ORG_CLO approval exists
    Then the referral cannot be submitted to any ODR provider

  @P19-AT-17
  Scenario: Award arrives in the vault with advisory clocks
    When "ADROutcomeRecorded" arrives for a party's case with an award document reference
    Then the award PDF/A is stored as an immutable original
    And obligations are created from its payment schedule
    And s.33 and s.34(3) clocks are shown as advisory

  @P19-AT-18
  Scenario: Partner batch with KYB pre-fill and consent
    Given partner "SME Desk Bank" submits 500 rows
    Then each valid row receives KYB pre-fill with source labels marked unconfirmed
    And one invitation email per signatory is sent
    When a signatory confirms fields and accepts terms
    Then a Company workspace is activated with the signatory as ORG_OWNER
    And the partner sees only status "ACTIVATED" for that partner_ref

  @P19-AT-19 @NN-05
  Scenario: No scraping and no bureau, CKYC or PAN-database calls during onboarding
    When the KYB pre-fill workflow runs
    Then no request goes to any MCA21, CKYCR, credit bureau or eCourts portal domain
    And the egress log shows only licensed vendor and GLEIF endpoints

  @P19-AT-20
  Scenario: Individuals cannot be bulk-onboarded by an ecosystem client
    When the Udofin service client submits a batch of individual borrowers
    Then the batch is rejected with "LD-INT-072"

  @P19-AT-21 @NN-34
  Scenario: Counterparty contact limit on API-created signing requests
    Given a signing request created via API invites counterparty "Ravi"
    And Ravi has not opened the link
    Then LawDocs has sent at most one business-initiated message to Ravi
    And no automated voice call is placed to Ravi

  @P19-AT-22 @NN-39
  Scenario: Adapter kill switch
    Given PLT_SUPER_ADMIN engages kill switch "int.kill.leegality-esign-lawdocs" with a reason
    Then within 60 seconds new signing requests route to the fallback adapter
    And releasing it requires a second authorised person, PLT_SECURITY_OFFICER (FR-P03-85)

  @P19-AT-23 @NN-25
  Scenario: Automation platform data ceiling
    Given tenant "Acme" connected Zapier with ceiling "INTERNAL"
    When a Zap requests an agreement's counterparty email
    Then the field is omitted and listed in "x-omitted-fields"
    And an action "send agreement to counterparty" is refused with "LD-INT-091"

  @P19-AT-24 @NN-32
  Scenario: Integration logs carry no personal data
    When 1,000 synthetic deliveries containing PAN and Aadhaar patterns in payloads are processed
    Then no log line, trace attribute or DLQ metadata field contains those patterns

  @P19-AT-25 @NN-11
  Scenario: Sharing ledger is exportable
    When ORG_ADMIN exports the tenant in LD-EXPORT-1.0
    Then "99 System Data (CSV and JSON)/Integrations/sharing-ledger.csv" exists with every ledger entry and hash

  @P19-AT-26 @NN-05 @NN-19 @NN-23
  Scenario: LawDocs is not a lender, RE, LSP or DSA (FR-P19-84)
    Given the egress policy of Appendix I §I.14 is loaded
    When any module or adapter attempts a call to a credit-bureau, lender-lead or loan-origination endpoint
    Then the call is blocked at egress with "LD-INT-090" (problem type "regulatory-guard") and an integration incident is raised
    And no API, webhook, event mapping or connector exists that sends a LawDocs or Consumer Help user's data to a lender as a lead
    And the feature-flag registry contains no flag for loan sourcing, loan comparison, lender referral fees or collection messaging
    When a maker proposes a flag "mkp.loan_marketplace.enabled"
    Then registration is refused with "LD-CFG-012" (governed key — change request needed) until a counsel opinion recorded by PLT_LEGAL_REVIEWER and owner approval under FR-P17-57/58 are attached

  @P19-AT-27 @NN-24
  Scenario: Proposed service-order and OH metric events stay inert until Appendix Y is merged
    Given "int.eco.v12_contracts.enabled" is OFF
    When an LDC-fulfilled storefront order is paid
    Then no "in.infrabyx.ops.ServiceOrderRouted.v1" is published
    And the order context is handed over through the logged MANUAL_INTERIM channel with the buyer's consent reference
```

## 13. Exit gate, deliverables and open items

**Exit checklist**

- [ ] Gateway, OAuth profile, scopes, error model, idempotency, correlation and rate limits live in all environments; BOLA suite green.
- [ ] Outbox relay, inbox, tenant webhooks, ecosystem push, DLQ with maker-checker replay; 4-hour outage drill with zero loss.
- [ ] OH connector certified in sandbox (provisioning, catalogue, quotes, orders, invoices, entitlements, usage); aggregates-only tests pass.
- [ ] LDC, Finbyx, Udofin and Equator connectors certified in sandbox; v1.2-dependent contracts inert until Appendix Y is merged, manual interim channel tested.
- [ ] Partner onboarding API with KYB pre-fill, invitations, consent and activation; dry run; partner webhooks.
- [ ] Adapters scaffolded and certified for Wave 1 ports (eSign, eStamp, KYB, DigiLocker, messaging, OH8); Wave 2 ports per Appendix I §I.2 status.
- [ ] Developer portal, sandbox personas, simulators, SDKs (TypeScript, Python), Postman, OpenAPI/AsyncAPI downloads, Zapier/Make/Power Automate connectors in private beta.
- [ ] Integration health dashboard (tenant and platform), status page, reconciliation jobs, kill switches.
- [ ] Settings registered in Appendix R; help keys registered in `hlp`; export-map entries registered; error codes registered.
- [ ] Gherkin `@P19-AT-01…27` green; NN tests `tests/nn/NN-01, -05, -06, -07, -11, -13, -18, -19, -23, -24, -25, -32, -34, -38, -39, -46, -47` green.

**Demo script (20 minutes).** (1) Developer signs up and makes a sandbox call in under 15 minutes. (2) Partner uploads a 50-row batch; a signatory activates in four taps. (3) A webhook endpoint fails; DLQ replay with two admins. (4) Finbyx sandbox creates a hosted signing request; the ceremony opens on `sign.lawdocs.in`; a POA request is refused with a wet-ink pack. (5) A Udofin sandbox borrower links and deposits a sanction letter; the sharing ledger shows it. (6) A contract dispute is referred to the Equator sandbox; an award returns into the vault with advisory clocks. (7) OH8 receives the month's usage aggregates; a seeded identifier is rejected.

**Deliverables.** `apps/api/src/int/**`, `packages/connectors/**` (ports and adapters), `packages/contracts/**`, `docs/interfaces/api.md`, `docs/interfaces/webhooks.md`, `docs/ecosystem/infrabyx-integration-spec.md` (unchanged copy), `infrabyx-contracts/proposals/2026-10-25-add-lawdocs-ld.md` (from Appendix Y), developer portal site, SDK repositories, certification reports.

**Open items**

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-P19-01 | Approval of Appendix Y (Ecosystem Spec v1.2) by every affected product owner | [OWNER] | Manual interim channel, logged (FR-P19-27) |
| OI-P19-02 | ESP/aggregator written confirmation that API-initiated, LawDocs-hosted ceremonies for a customer's own documents are within ASP terms and not sub-letting | [COUNSEL] + procurement | Disable `int.esign.api_initiation.enabled` |
| OI-P19-03 | B2C billing identity to OH8 (`CONTRACT_PERFORMANCE_CUSTOMER`, `PII` ceiling) | [OWNER] + PLT_DPO | LawDocs issues B2C invoices itself (deviation from D-11) |
| OI-P19-04 | Consumer Help conflict-check API at OH and conflict policy | [COUNSEL] + OH lead | Manual conflict declaration by user + staff check |
| OI-P19-05 | LDC P26 legal-matter/CLM overlap with D-10 (LawDocs SoR) | Pack leads (LDC, LD) | Tenant-level choice recorded in `LDC_SOR` link |
| OI-P19-06 | Court-data aggregator contracts (two vendors) with lawful-collection warranties | Procurement + [COUNSEL] | Manual CNR only |
| OI-P19-07 | Zapier/Make partner terms, data residency and transfer assessment | PLT_DPO | Power Automate + webhooks only |
| OI-P19-08 | Graphy API/feed for FinLegal Academy catalogue | Academy lead | Curated catalogue import |
| OI-P19-09 | A2A agent-task contracts across products | Ecosystem spec owners | Not built |
| OI-P19-10 | JioCX DPA, India-processing and no-training terms; WhatsApp BSP status | Procurement | Meta Cloud API direct + other DLT aggregator |
| OI-P19-11 | Equator clause API endpoint and model-clause licence | EQ lead | Manual reviewed import |
| OI-P19-12 | Entity Locker requester API coverage for company onboarding | P01 lead | Licensed MCA-data vendor + document upload |
