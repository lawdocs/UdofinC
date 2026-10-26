# Appendix D — Integration Adapter Specifications

> Binding reference for master §4.4 and §8. Every external vendor sits behind a port (NestJS provider token) in `apps/api/src/integrations/ports/*` with adapters in `.../adapters/{provider}`. Phase prompts reference this appendix by section (e.g. "Appendix D §D.2.1 VOICE_PORT"). Vendor endpoint paths and header names marked **[VERIFY]** must be confirmed against the vendor's current documentation during the adapter's spike; do not hard-code them outside the adapter. Status after the October 2026 verification: the ElevenLabs post-call webhook signature, Leegality `mac` (HMAC-SHA1) and RazorpayX payout idempotency header are confirmed (22 Oct 2026 round also confirmed ElevenLabs paths, Sarvam/Exotel/MSG91/Digio/Setu items, Razorpay capture window, Cashfree idempotency, Bedrock India profiles); items still open are marked **[VERIFY — open: …]** and listed in §D.10.

## D.0 Conventions that apply to every adapter

### D.0.1 Shared types (`packages/domain/src/integrations/common.ts`)

```ts
export type Lang = 'en'|'hi'|'mr'|'ta'|'te'|'kn'|'bn'|'gu'|'pa'|'ml'|'or'|'ur'|'as';
export type CurrencyCode = 'INR'|'USD'|'EUR'|'GBP'|'SGD'|'AED';
export interface Money { amountMinor: bigint; currency: CurrencyCode }          // NN-13: integer minor units
export type DataClass = 'public'|'internal'|'personal'|'sensitive'|'sealed';    // sealed never leaves Equator stores
export interface ProviderContext {
  tenantId: string; caseId?: string; vertical?: 'FIN'|'COM'|'FAM'|'INS'|'WRK'|'INT'|'SEC';
  dataClass: DataClass; language?: Lang; stateCode?: string; correlationId: string;
  idempotencyKey: string;                                                       // sha256(case_id|action|version|attempt)
}
export type ProviderErrorKind =
  'AUTH'|'VALIDATION'|'NOT_FOUND'|'CONFLICT'|'RATE_LIMITED'|'TIMEOUT'|'UNAVAILABLE'|
  'POLICY_REJECTED'|'INSUFFICIENT_FUNDS'|'RESIDENCY'|'UNSUPPORTED'|'UNKNOWN';
export class ProviderError extends Error {
  constructor(public readonly kind: ProviderErrorKind, public readonly provider: string,
              public readonly retryable: boolean, public readonly providerCode?: string,
              public readonly httpStatus?: number, message?: string) { super(message); }
}
export interface NormalisedEvent<T = unknown> {
  provider: string; externalEventId: string; type: string; occurredAt: Date;
  subjectRef: { kind: string; providerId: string }; payload: T; rawSha256: string;
}
export interface WebhookVerifier { verify(headers: Headers, rawBody: Buffer, now: Date): Promise<void> } // throws ProviderError('AUTH')
export interface Capabilities { residency: 'IN'|'IN_PARTIAL'|'NON_IN'; languages?: Lang[]; features: string[]; maxConcurrency?: number }
```

### D.0.2 Error mapping to problem+json (Appendix F)

| `ProviderErrorKind` | Typical vendor signals | Retry | Problem `code` surfaced to API callers |
|---|---|---|---|
| `AUTH` | 401/403, bad signature, expired token | No (alert on-call; rotate secret) | `INTEGRATION_AUTH_FAILED` |
| `VALIDATION` | 400/422, template mismatch, invalid MSISDN | No | `INTEGRATION_REQUEST_INVALID` (+ field details) |
| `NOT_FOUND` | 404 | No | `INTEGRATION_RESOURCE_NOT_FOUND` |
| `CONFLICT` | 409, duplicate idempotency key with different payload | No (fetch existing) | `INTEGRATION_CONFLICT` |
| `RATE_LIMITED` | 429, Bedrock `ThrottlingException`, WA error 130429 (throughput) | Yes, honour `Retry-After`, else exp. backoff | `INTEGRATION_RATE_LIMITED` |
| `TIMEOUT` | client timeout, 504 | Only if operation idempotent at provider | `INTEGRATION_TIMEOUT` |
| `UNAVAILABLE` | 5xx, connection reset, circuit open | Yes / failover per port policy | `INTEGRATION_UNAVAILABLE` |
| `POLICY_REJECTED` | WA template rejected, DLT scrub fail, KYC mismatch, sanctions hit | No | port-specific (e.g. `COMMS_DLT_TEMPLATE_MISMATCH`) |
| `INSUFFICIENT_FUNDS` | payout balance low, escrow underfunded | No (ops task) | `PAYOUT_INSUFFICIENT_BALANCE` |
| `RESIDENCY` | adapter refuses data class for non-IN endpoint | No | `INTEGRATION_RESIDENCY_VIOLATION` |
| `UNSUPPORTED` | state/instrument/language not supported | No (try next provider) | `INTEGRATION_UNSUPPORTED` |

### D.0.3 Resilience defaults

- **Timeouts**: connect 3 s; request per port (below). **Retries**: max 3 with full-jitter exponential backoff (base 500 ms, cap 30 s) **only** for idempotent operations or where the provider honours an idempotency key.
- **Circuit breaker** (opossum) per `(provider, port, tenant-group)`: open when ≥ 50% failures over a rolling 20-request / 60-s window; half-open after 60 s with 3 probe calls; state exported as metric `integration_circuit_state` and persisted to `core.integration_providers.health` for the resolver.
- **Failover policy** per port: `auto` (stateless: SMS, email, push, KYC lookups, FX, translation), `reinitiate` (stateful objects: eSign envelope, eStamp, payment order, escrow, voice call — never silently moved; a new object is created on the fallback with user re-consent where required), `none` (AA consent, LLM for personal data outside residency).
- **Outbox**: every side-effecting call is enqueued in `core.outbox` in the same transaction as the domain change; the dispatcher executes the adapter call and records `core.outbound_requests(idempotency_key, port, provider, request_sha256, response_sha256, status, attempts)` (unique on `idempotency_key`).
- **Webhook ingress**: `POST /webhooks/:provider` → raw body captured (no JSON parse before verification) → `WebhookVerifier.verify` → insert into `core.webhook_inbox(provider, external_event_id, received_at, headers_redacted, raw_body_enc, raw_sha256, status)` with `UNIQUE(provider, external_event_id)` → 200 within 2 s → async processing → domain events. Replay window ±5 min where the provider signs timestamps. **Nightly reconciliation poll** per provider re-fetches state for objects with non-terminal status older than 2 h.
- **Cost telemetry**: each adapter emits `integration_cost{provider,port,tenant,unit}` and writes `core.comm_cost_ledger` (comms/voice) or `core.integration_cost_ledger` (others).
- **Testing**: each adapter ships (1) an in-memory fake implementing the port for unit tests; (2) a Pact-style contract test against the vendor sandbox (nightly, not on every PR); (3) recorded fixtures for webhook signature tests (valid, tampered, stale timestamp, duplicate). Production credentials never exist in non-prod (master §11).

### D.0.4 Provider registry and routing

```sql
CREATE TABLE core.integration_providers (
  code text PRIMARY KEY,                          -- 'elevenlabs', 'exotel', 'gupshup_wa', 'msg91', ...
  port text NOT NULL CHECK (port IN ('VOICE_PORT','TELEPHONY_PORT','MESSAGING_PORT','EMAIL_PORT','PUSH_PORT','ESIGN_PORT',
      'ESTAMP_PORT','KYC_PORT','PAYMENTS_PORT','PAYOUT_PORT','ESCROW_PORT','TAX_INVOICE_PORT','VIDEO_PORT','TRANSCRIPTION_PORT',
      'TRANSLATION_PORT','LLM_PORT','DOC_AI_PORT','FX_PORT','SANCTIONS_PORT','AA_PORT','POSTAL_PORT','CRM_PORT','ANALYTICS_PORT',
      'GROUP','GOV')),                                -- the 23 master §4.4 port tokens + group/government connectors
  display_name text NOT NULL,
  residency text NOT NULL CHECK (residency IN ('IN','IN_PARTIAL','NON_IN')),
  max_data_class text NOT NULL CHECK (max_data_class IN ('public','internal','personal','sensitive')),
  capabilities jsonb NOT NULL,                   -- languages, states, instruments, features, limits
  contract_ref text, dpa_ref text, residency_attestation_ref text, attestation_expires date,
  secret_ref text NOT NULL,                      -- AWS Secrets Manager ARN; never the secret
  sandbox boolean NOT NULL DEFAULT false,
  health jsonb NOT NULL DEFAULT '{"circuit":"closed"}',
  status text NOT NULL CHECK (status IN ('active','suspended','retired'))
);

CREATE TABLE core.provider_routing (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id uuid REFERENCES core.tenants(id),     -- NULL = platform default
  port text NOT NULL,
  provider_code text NOT NULL REFERENCES core.integration_providers(code),
  priority smallint NOT NULL CHECK (priority BETWEEN 1 AND 9),
  conditions jsonb NOT NULL DEFAULT '{}',         -- {"vertical":["FIN"],"language":["mr"],"state":["MH"],"series":"1600","currency":["USD"]}
  conditions_sha256 char(64) GENERATED ALWAYS AS (encode(sha256(conditions::text::bytea),'hex')) STORED,
  weight smallint NOT NULL DEFAULT 100,           -- for canary splits within the same priority
  failover_policy text NOT NULL CHECK (failover_policy IN ('auto','reinitiate','none')),
  effective_from timestamptz NOT NULL, effective_to timestamptz,
  version int NOT NULL, change_request_id uuid REFERENCES core.config_change_requests(id),  -- maker–checker (NN-21)
  UNIQUE (tenant_id, port, priority, conditions_sha256, version)
);
-- RLS: tenants read their own rows + platform defaults; writes only via config_change_requests approval.
```

Reconciliation with P00 FR-P00-36: P00 creates `core.provider_routing` first with the 23 master port tokens and columns `provider`, `credential_mode`, `circuit`, `enabled`. The first integration migration adds the D.0.4 columns (`weight`, `failover_policy`, `effective_from/to`, `version`, `change_request_id`), keeps P00's column names where they differ (`provider` = `provider_code`), and widens the P00 `port` CHECK to admit `GROUP` and `GOV`; record this in an ADR (master §15).

**Resolver algorithm** (`ProviderResolver.resolve(port, ctx)`):
1. Load active rows for `(ctx.tenantId, port)` and platform defaults (`tenant_id IS NULL`), effective now.
2. Keep rows whose `conditions` match `ctx` (every present key must contain the context value).
3. Drop providers with `status <> 'active'`, open circuit, expired residency attestation, or `max_data_class` lower than `ctx.dataClass`, or `residency <> 'IN'` when `ctx.dataClass ∈ {personal, sensitive}` unless a residency ADR ID is recorded on the routing row.
4. Order: tenant rows before platform rows; then `priority` ascending; within equal priority, weighted random by `weight`.
5. Return the ordered list; the caller tries index 0, and on `UNAVAILABLE`/`RATE_LIMITED`/`UNSUPPORTED` moves to the next only if `failover_policy = 'auto'`.

**Seed routing (platform defaults)**

| Port | P1 | P2 | P3 | Failover | Notes |
|---|---|---|---|---|---|
| VOICE | `elevenlabs` | `sarvam_voice` | `livekit_agents_sarvam` | reinitiate | Per-language override rows after bake-off (R3 U2) |
| TELEPHONY | `exotel` | `plivo` | `twilio` (INT foreign numbers only) | reinitiate | 1600 numbers tenant-specific |
| MESSAGING (whatsapp) | `gupshup_wa` | `interakt_wa` | `msg91_wa` | reinitiate | Templates must pre-exist on fallback WABA |
| MESSAGING (sms) | `msg91` | `gupshup_sms` | `kaleyra_sms` | auto | Same DLT PE/templates |
| EMAIL | `ses_apsouth1` | `resend` | — | auto (non-legal-service) | Resend only for `internal` data class unless ADR |
| PUSH | `expo` | `fcm_apns_direct` | — | auto | |
| ESIGN | `leegality` | `setu_esign` | `digio` | reinitiate | `lawdocs_esign` optional tenant row |
| ESTAMP | `leegality_bharatstamp` | `setu_estamp` | `digio_estamp` / `signdesk_nesl` | reinitiate | State-conditioned rows (D.3.2) |
| KYC | `surepass` | `hyperverge` | `idfy` | auto (lookups) | Liveness: `hyperverge` P1 |
| PAYMENTS | `razorpay` | `cashfree` | `razorpay_intl` (currency ≠ INR) | reinitiate | |
| PAYOUT | `razorpay_route` | `cashfree_payouts` | — | reinitiate | |
| ESCROW | `castler` | `razorpayx_escrow_plus` | `direct_with_proof` | none | Legal sign-off per tenant (R3 U7) |
| TAX_INVOICE | `cleartax_gsp` | `masters_india_gsp` | — | reinitiate | |
| VIDEO | `livekit_cloud_india` | `livekit_selfhost` | `hms_100ms` | reinitiate | |
| TRANSCRIPTION | `sarvam_saaras` | `indicconformer_selfhost` | — | auto | |
| TRANSLATION | `sarvam_translate` | `indictrans2_selfhost` | `bhashini` (gov tenants) | auto | |
| LLM | `bedrock_claude_in` | `sarvam_105b` (indic_low_risk tier only) | `anthropic_direct` (public data only) | none for personal data | |
| DOC_AI | `sarvam_vision` | `azure_docintel_centralindia` **[VERIFY — open (vendor): Central India not confirmed 22 Oct 2026 — provision a test resource in centralindia before enabling]** | `google_docai` (non-personal) | auto | |
| FX | `fbil_reference` | `commercial_fx_api` | `manual_entry` | auto | |
| SANCTIONS | `commercial_screening` | `local_list_matcher` | — | auto | |
| AA | `tenant_fiu_tsp` (Setu AA / Finvu / OneMoney under lender credentials) | `manual_statement_upload` | — | none | NN-14 |
| POSTAL | `manual_desk` | `indiapost_api` | — | none | Master §4.4 port (X-02); `indiapost_api` only after a written DoP agreement |
| CRM | `native_crm` (growth DB; source of truth) | `hubspot` / `zoho` (tenant choice; sync only) | — | none | NN-16: growth data only; separate database (P13 FR-P13-26) |
| ANALYTICS | `posthog_selfhost_apsouth1` | `ga4` (acquisition only, consent-gated) | — | auto (drop events, never block a page) | Never loaded on case pages (P13 FR-P13-23) |

## D.1 Port catalogue summary

| Port token | Interface | Primary / fallback (master §8) | Request timeout | Idempotency source |
|---|---|---|---|---|
| `VOICE_PORT` | `VoicePort` | ElevenLabs Agents / Sarvam, LiveKit+Sarvam | 15 s (API); call async | Equator `call_id` stored as provider metadata; de-dupe before dial |
| `TELEPHONY_PORT` | `TelephonyPort` | Exotel / Plivo | 10 s | Equator `call_id` in custom field |
| `MESSAGING_PORT` | `MessagingPort` | Gupshup (WA), MSG91 (SMS) / Interakt, AiSensy, MSG91; Gupshup, Kaleyra | 10 s | local de-dupe + provider ref field |
| `EMAIL_PORT` | `EmailPort` | SES / Resend | 10 s | local de-dupe; Resend `Idempotency-Key` |
| `PUSH_PORT` | `PushPort` | Expo / FCM+APNs | 10 s | local de-dupe |
| `ESIGN_PORT` | `ESignPort` | Leegality / Setu, Digio, SignDesk | 30 s | envelope external reference = Equator ID |
| `ESTAMP_PORT` | `EStampPort` | Leegality BharatStamp / Setu, Digio, SignDesk–NeSL | 60 s | stamp request reference |
| `KYC_PORT` | `KycPort` | Surepass / IDfy, Signzy, HyperVerge | 20 s | request ID; lookups naturally idempotent |
| `PAYMENTS_PORT` | `PaymentsPort` | Razorpay / Cashfree | 15 s | order `receipt` = Equator ID; provider idempotency header where supported |
| `PAYOUT_PORT` | `PayoutPort` | Razorpay Route/RazorpayX / Cashfree Payouts | 15 s | payout idempotency header (mandatory) |
| `ESCROW_PORT` | `EscrowPort` | Castler / RazorpayX Escrow+ / direct-with-proof | 30 s | escrow reference |
| `TAX_INVOICE_PORT` | `TaxInvoicePort` | GSP (ClearTax/Masters India/IRIS) | 30 s | invoice number unique per GSTIN per FY |
| `VIDEO_PORT` | `VideoPort` | LiveKit Cloud India / self-host / 100ms | 10 s | room key deterministic |
| `TRANSCRIPTION_PORT` | `TranscriptionPort` | Sarvam Saaras / IndicConformer | async jobs | job reference |
| `TRANSLATION_PORT` | `TranslationPort` | Sarvam Translate / IndicTrans2 / Bhashini | 20 s | content hash cache |
| `LLM_PORT` | `LlmPort` | Bedrock Claude (IN) / Anthropic direct (public only) | per tier (P11) | interaction ID; not retried after partial stream |
| `DOC_AI_PORT` | `DocAiPort` | Sarvam Vision / Google DocAI / Azure DI | async | file sha256 cache |
| `FX_PORT` | `FxPort` | FBIL reference / commercial API | 10 s | (date, pair, source) unique |
| `SANCTIONS_PORT` | `SanctionsPort` | Commercial screening / local matcher | 20 s | screening request ID |
| `AA_PORT` | `AaPort` | Tenant FIU via TSP / manual upload | 30 s | consent handle |
| `POSTAL_PORT` | `PostalPort` | Manual desk / India Post API (by contract) | 15 s | `dispatchId` |
| `CRM_PORT` | `CrmPort` | Native mini-CRM / HubSpot, Zoho sync | 15 s | `(lead_id, sync_version)` |
| `ANALYTICS_PORT` | `AnalyticsPort` | PostHog self-hosted (ap-south-1) / GA4 | 5 s (async) | event UUID |

## D.2 Communications ports

### D.2.1 `VOICE_PORT`

```ts
export interface VoiceAgentDefinition {
  agentKey: string; version: string; useCase: 'notice_explainer'|'consent_capture'|'slot_booking'|'hearing_reminder'|
    'offer_relay'|'payment_link'|'feedback'|'inbound_helpline';
  languages: Lang[]; voices: Record<Lang, string>;               // provider voice IDs
  workflow: { nodes: VoiceNode[]; edges: VoiceEdge[] };            // provider-neutral graph (Appendix E §6.1)
  tools: { name: string; url: string; schema: JsonSchema; timeoutMs: number }[];
  knowledgeBaseIds: string[];                                      // per case-type corpora, no case data
  dataCollection: JsonSchema; evaluationCriteria: { id: string; prompt: string }[];
  maxDurationSec: number; promptVersionId: string; zeroRetention: boolean;
  llm: { mode: 'provider_hosted'|'custom_proxy'; proxyUrl?: string; modelAlias?: ModelAlias };  // custom_proxy = Equator OpenAI-compatible proxy in ap-south-1 → Bedrock India
}
export interface OutboundCallRequest {
  callId: string; agentProviderId: string; toE164: string; fromNumberRef: string;
  language: Lang; dynamicVariables: { first_name: string; case_ref: string; call_jwt: string;
    tenant_display_name: string; notice_date_spoken?: string };   // allow-list only (P07 FR-P07-31)
  scheduledAt?: Date; recordingEnabled: boolean;
  policyToken: string;                                            // signed ContactPolicy decision (call_id, to, series, CLI, PE, 60-s TTL) — NN-12/M-05
}
export interface VoiceCallResult {
  providerCallId: string; status: 'queued'|'ringing'|'in_progress'|'completed'|'failed'|'no_answer'|'busy'|'machine';
  startedAt?: Date; endedAt?: Date; billableSec?: number; transcript?: TranscriptTurn[];
  dataCollection?: Record<string, unknown>; evaluation?: Record<string, 'success'|'failure'|'unknown'>;
  costMinor?: bigint; languageDetected?: Lang[]; toolInvocations?: { name: string; at: Date; ok: boolean }[];
}
export interface VoicePort {
  capabilities(): Capabilities & { batch: boolean; zeroRetention: boolean; sip: boolean };
  upsertAgent(def: VoiceAgentDefinition, ctx: ProviderContext): Promise<{ providerAgentId: string }>;
  syncKnowledgeBase(providerAgentId: string, docs: { id: string; title: string; text: string; lang: Lang }[]): Promise<void>;
  placeCall(req: OutboundCallRequest, ctx: ProviderContext): Promise<{ providerCallId: string }>;
  createBatch(rows: OutboundCallRequest[], ctx: ProviderContext): Promise<{ providerBatchId: string }>; // ≤ 500 rows, pre-cleared
  cancelBatch(providerBatchId: string): Promise<void>;
  cancelScheduled(providerCallIds: string[]): Promise<void>;
  getCall(providerCallId: string): Promise<VoiceCallResult>;
  getRecording(providerCallId: string): Promise<NodeJS.ReadableStream | null>;
  deleteConversationData(providerCallId: string): Promise<void>;  // after WORM copy (T+24h) and DPDP erasure
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent<VoiceCallResult>[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **ElevenLabs Agents Platform** (Enterprise, India Data Residency) — workflows (Subagent, Say, Dispatch tool, Update state, Agent transfer, Transfer to number, End), server tools, KB/RAG per node, batch calling, post-call webhooks with data collection and evaluation, SIP trunk inbound/outbound (Exotel). Fallback **Sarvam Voice Agents** (India-hosted ASR/LLM/TTS, from ₹3/min) and **LiveKit Agents worker** (self-hosted Mumbai) with Sarvam Saaras STT + Bulbul v3 TTS + Bedrock Claude Haiku via `LLM_PORT`. **Custom LLM**: ElevenLabs accepts any server exposing an OpenAI-compatible `/v1/chat/completions` or `/v1/responses` SSE endpoint with function calling; Bedrock is not a native option, so Equator runs an OpenAI-compatible proxy in ap-south-1 that calls the Bedrock India profile through the AI gateway (P11 FR-P11-01). All PSTN legs run over Indian operator/CPaaS SIP trunks registered under Equator's (or the tenant's) DLT Principal Entity (P07 FR-P07-20). |
| Auth | ElevenLabs: `xi-api-key` header (workspace key per environment; per-tenant sub-workspaces not required); production uses the India-residency environment, API base `https://api.in.residency.elevenlabs.io` (separate account and API key). Sarvam: `api-subscription-key`. LiveKit: API key/secret → JWT. |
| Key endpoints [Verified 22 Oct 2026, ElevenLabs API ref: agents/create, sip-trunk/outbound-call, batch-calling/submit; India base URL https://api.in.residency.elevenlabs.io (separate workspace/keys); re-read other paths at spike] | ElevenLabs: `POST /v1/convai/agents/create`, `PATCH /v1/convai/agents/{agent_id}`, `POST /v1/convai/sip-trunk/outbound-call`, `POST /v1/convai/batch-calling/submit`, `GET/POST /v1/convai/batch-calling/{id}` (+`/cancel`, `/retry`), `GET /v1/convai/conversations/{id}`, `GET .../{id}/audio`, `DELETE .../{id}`, knowledge-base create endpoints. Batch CSV reserved columns: `phone_number` (mandatory), `language`, `first_message`, `system_prompt`, `voice_id`; batch calling is **not supported in Zero Retention Mode**. |
| Webhooks | ElevenLabs post-call webhook (transcription; audio) signed with HMAC-SHA256: header `ElevenLabs-Signature: t=<unix>,v0=<hex>` over `"{t}.{rawBody}"` with the workspace webhook secret (confirmed Oct 2026; event types `post_call_transcription`, `post_call_audio` with base64 MP3); tolerance 30 min per vendor guidance, Equator uses ±5 min + inbox de-dupe on `conversation_id`. The webhook endpoint is hosted in ap-south-1 (ElevenLabs states post-call webhook traffic is outside its residency guarantee). Sarvam: batch-job callback carries the caller-set `auth_token` in header `X-SARVAM-JOB-CALLBACK-TOKEN` (shared token, not HMAC; per-job random token, constant-time compare, re-fetch job status) [Verified 22 Oct 2026, Sarvam Batch STT docs]. LiveKit Agents: Equator-owned worker emits internal events (no external webhook). |
| Idempotency | Equator `call_id` is placed in provider metadata/dynamic variable; before dialling, adapter checks `core.call_records` for an existing provider call with that `call_id`; batch rows carry `call_id` column. Retries of `placeCall` only on connection errors **before** the provider returns an ID; never on timeout after submission (reconcile via `getCall`/batch status instead). |
| Compliance hooks | `placeCall`/`createBatch` refuse any row without a valid `policyToken` whose CLI is the tenant's authorised 1600 number or an Equator CLI inside an acknowledged A2P declaration (`ops.telecom_declarations`) — `COMMS_CLI_NOT_DECLARED` / `COMMS_NUMBER_SERIES_UNAVAILABLE`; mandatory C-OPEN node verified in the compiled agent (Appendix E VP-01, VP-21). |
| Errors | 401 → AUTH; 422 invalid agent/config → VALIDATION; 429 concurrency/burst → RATE_LIMITED (fall back to scheduling later, not to burst pricing unless tenant enabled); 5xx → UNAVAILABLE; residency attestation missing → RESIDENCY. |
| Retries / CB | API calls retry ×3; calls themselves are retried by the P07 campaign logic, never by the adapter. CB per provider; when open, `OutboundCallWorkflow` re-queues to next permitted slot on the next provider **only** if that provider has an approved agent version for the language. |
| Sandbox / test | Non-prod ElevenLabs workspace with synthetic agents; test numbers owned by Equator staff; "test call to my number" from SCR-P07-08 restricted to staff; recorded webhook fixtures; nightly contract test (create agent → patch → run Agent Testing suites via `POST /v1/convai/agents/{agent_id}/run-tests` (simulate-conversation endpoints are deprecated) [Verified 22 Oct 2026, ElevenLabs docs]). |
| Residency | ElevenLabs India Data Residency is Enterprise-only (launched 30 Jul 2025; isolated environment `in.residency.elevenlabs.io`; agents must be recreated via API in that environment). Storage is in India, but ElevenLabs states that some processing (support, moderation, sub-processors per DPA) may occur elsewhere and that **custom LLMs and post-call webhooks may process data outside the region** — hence the India-hosted LLM proxy and webhook endpoint; Zero Retention Mode optional. Obtain written confirmation that Agents conversations, transcripts, recordings and post-call data are stored in India (R3 U1) — store as `residency_attestation_ref`. Until confirmed, `max_data_class = 'internal'` and only synthetic/staff calls permitted. Sarvam: India-hosted. |
| Cost | ElevenLabs ≈ $0.08/min platform + LLM pass-through ($0.0005–$0.045/min) + telephony; burst above concurrency $0.16/min; silence > 10 s discounted 95% (R3 §1.1 [S]). All-in ≈ ₹8–9 per connected minute before enterprise discount. Sarvam from ₹3/min. Metered per call into `core.comm_cost_ledger`. |

### D.2.2 `TELEPHONY_PORT`

```ts
export type NumberSeries = '1600'|'1601'|'DID'|'TOLLFREE'|'INTL';   // 140 (promotional) is never provisioned for case traffic
export interface TelephonyPort {
  capabilities(): Capabilities & { amd: boolean; sipTrunk: boolean; streaming: boolean; series: NumberSeries[] };
  provisionNumber(spec: { series: NumberSeries; circle?: string; principalEntityId: string; tenantId?: string }): Promise<{ numberRef: string; e164: string }>;
  bindNumberToSip(numberRef: string, target: { sipUri: string; transport: 'tls'; srtp: boolean }): Promise<void>;
  dial(req: { callId: string; fromNumberRef: string; toE164: string; flowUrl?: string; amd: boolean; record: boolean; statusCallbackUrl: string }): Promise<{ callSid: string }>;
  transferToHuman(callSid: string, queue: { e164?: string; sipUri?: string }): Promise<void>;
  hangup(callSid: string): Promise<void>;
  checkDnd(e164: string): Promise<{ registered: boolean; preference: 'none'|'fully_block'|'block_promo'|'category'; categories: string[]; checkedAt: Date }>;  // every voice/SMS row (P07 FR-P07-19)
  registerConsent?(c: { e164: string; principalEntityId: string; purpose: string; consentTextSha256: string; capturedAt: Date; channel: string }): Promise<{ registrationRef: string }>; // operator Digital Consent platform via CPaaS/DCA, where supported
  getRecording(callSid: string): Promise<NodeJS.ReadableStream | null>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent<{ callSid: string; status: string; durationSec?: number; answeredBy?: 'human'|'machine' }>[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Exotel** (SIP trunk to ElevenLabs; AgentStream bidirectional WebSocket 8 kHz PCM for LiveKit/Sarvam path; registered as telemarketer under Equator's DLT PE; tenant 1600 numbers and Equator DID numbers in declared A2P ranges; never 140 for case calls), **Plivo India** (₹0.38/min, 30-s pulses, numbers ₹200/month, free AMD), **Twilio** only for INT calls to foreign numbers (flag `telephony.intl.enabled`). |
| Auth | Exotel: HTTP Basic (API key:token) on the India (Mumbai) cluster `https://api.in.exotel.com/v1/Accounts/{sid}/...` (the Singapore cluster is `api.exotel.com`; confirm the cluster on the account). Plivo: Basic (Auth ID:Auth Token). Twilio: Basic (Account SID:Auth Token). SIP: TLS + digest credentials or IP ACL. |
| Webhooks | Exotel status callbacks are unsigned [Verified 22 Oct 2026, Exotel webhook docs: no signature; IP validation, TLS, de-dupe and Details API fallback recommended]: use an unguessable per-tenant callback path token + Basic auth on the callback URL + Exotel IP allow-list; reconcile with `GET Calls/{sid}`. Plivo: `X-Plivo-Signature-V3` + `X-Plivo-Signature-V3-Nonce` (HMAC-SHA256 over URL + nonce + sorted params). Twilio: `X-Twilio-Signature` (HMAC-SHA1 over full URL + sorted POST params). |
| Idempotency | Equator `call_id` in custom field (`CustomField` on Exotel; `X-PH-` custom SIP headers on Plivo); no retry after a `callSid` is returned. |
| Errors | Invalid number/blocked series → POLICY_REJECTED (`COMMS_NUMBER_SERIES_UNAVAILABLE`); DLT scrub failure → POLICY_REJECTED; carrier congestion → UNAVAILABLE. |
| Sandbox | Exotel/Plivo trial accounts with verified staff numbers only; no live party numbers in non-prod. |
| Residency | Indian carriers; recordings fetched to S3 ap-south-1 and deleted from carrier storage after copy (Plivo stores 90 days by default); CDRs and telephony logs retained ≥ 180 days in ap-south-1 (CERT-In Directions, 28 Apr 2022). |
| Cost | Pulse-based billing (30/60 s); failed/busy attempts may be billed — AMD and pre-dial number validation reduce waste. 1600-series numbers are provisioned for the **regulated tenant** (Principal Entity) and billed to that tenant. Equator's own A2P DID traffic may attract the A2P termination charge (up to ₹0.05/min; TCCCPR Third Amendment 2026, reg 18), which does not apply on the 140/1600/1601 series. |
| Compliance hooks | Adapter refuses `dial` (and `bindNumberToSip` for A2P use) if the P07 `ContactPolicy` decision token (signed JWT, 60-s TTL, binding `call_id`, `to`, `series`, CLI and PE) is absent or mismatched, or if the CLI is not inside an acknowledged A2P declaration for that PE (`COMMS_CLI_NOT_DECLARED`) — defence in depth for NN-12. |

#### D.2.2.1 M-05 calling controls (Equator places its own calls) — where each control is enforced

Source: TCCCPR 2018 as amended by the Second Amendment Regulations 2025 (No. 1 of 2025, 12 Feb 2025) and the Third Amendment Regulations 2026 (No. 05 of 2026, 18 Sep 2026); TRAI PR 91/2026 (10 Jul 2026); TRAI Direction and PR 113/2026 (10 Aug 2026). Build detail: P07 FR-P07-19/20/21/30.

| # | Control | Enforced in |
|---|---|---|
| D1 | Equator registered as **Principal Entity** on each originating operator's DLT; Exotel/Plivo linked as telemarketers; voice agents reach the PSTN only via Indian SIP trunks | `core.dlt_registry`; `ops.telecom_declarations` (`pe_registration`, `telemarketer_link`); provider onboarding checklist |
| D2 | **Lender-number mode** (default for FIN/INS regulated-tenant matters): tenant's 1600 number, tenant as PE, Equator/CPaaS chained as telemarketer, written authorisation | `core.number_authorisations`; ContactPolicy series selection; `COMMS_NUMBER_SERIES_UNAVAILABLE` |
| D3 | Equator's own service calls on Equator DID numbers **declared as A2P CLI ranges**; flag `voice.equator_service_number.enabled` OFF until operator written confirmation + telecom-counsel opinion are on file | `core.number_inventory`; flag guard on `ops.telecom_declarations` (`operator_cli_confirmation`, `counsel_opinion`) |
| — | **1601 watch**: apply when a phase covering legal/ODR services is notified (Phase I = utilities, courier/logistics); numbers allotted directly to the entity | Legal Rules Register `LR-TEL-002`; `series_1601_application` row |
| D4 | Explicit consent to AI/automated calls and recording captured and registered on the operator Digital Consent platform | `core.consent_records`; `TelephonyPort.registerConsent` |
| D5 | DND/NCPR scrub of every list; explicit-consent service calls blocked for DND numbers unless consent registered or party-initiated | `TelephonyPort.checkDnd`; ContactPolicy (`COMMS_NO_LAWFUL_BASIS`) |
| D6 | A2P declaration (purpose + CLI ranges) filed before go-live; undeclared CLIs refused | `ops.telecom_declarations`; VOICE/TELEPHONY adapter guard (`COMMS_CLI_NOT_DECLARED`) |
| D7 | Per-CLI hygiene against operator AI "UCC_Detect" (reg 21A): rate caps, answer-rate and short-call monitoring, rotation within declared ranges, complaint alarm ≥ 2 per CLI in 10 days | `core.number_inventory.status = 'paused_ucc'`; SCR-P07-16 monitor |
| D8 | First utterance: entity, "automated AI assistant", purpose, recording, opt-out; human hand-over; no impersonation | Appendix E C-OPEN, VP-01/VP-15; compiler mandatory node; QA item 1 |
| D9 | Hours: recovery-related 08:00–19:00 local (NN-12); Equator applies the same window to all party voice calls | ContactPolicy (P07 FR-P07-15/16) |
| D10 | Records: CDRs, recordings, transcripts in ap-south-1; ≥ 6 months for recovery calls (longer if sub judice); CERT-In 180-day logs | P07 FR-P07-30; retention jobs |

### D.2.3 `MESSAGING_PORT` (WhatsApp, SMS)

```ts
export type WaCategory = 'utility'|'authentication'|'marketing';
export interface TemplateDraft { key: string; channel: 'whatsapp'|'sms'; locale: Lang; category: WaCategory|'service'|'transactional';
  body: string; header?: { type: 'text'|'document'|'image'; text?: string }; buttons?: WaButton[]; footer?: string;
  dltTemplateId?: string; dltHeader?: string; variables: { name: string; example: string; maxLen: number }[] }
export interface TemplateMessage { to: string; templateRef: string; locale: Lang; params: Record<string, string>;
  category: WaCategory|'service'|'transactional'; dltTemplateId?: string; dltEntityId?: string; dltHeader?: string;
  shortLinkDomain?: string; idempotencyKey: string; policyToken: string }
export interface FlowMessage { to: string; flowId: string; flowToken: string; ctaText: string; templateRef?: string; initialData?: Record<string, unknown> }
export interface WaOrderDetails { to: string; referenceId: string; items: { name: string; amount: Money; quantity: number }[];
  total: Money; paymentConfiguration: string; expiresAt: Date }      // Razorpay PG deep integration; fees only (NN-13)
export interface MessagingPort {
  channel(): 'whatsapp'|'sms';
  capabilities(): Capabilities & { flows?: boolean; payments?: boolean; calling?: boolean };
  submitTemplate(t: TemplateDraft): Promise<{ providerTemplateId: string; status: 'pending'|'approved'|'rejected' }>;
  getTemplateStatus(providerTemplateId: string): Promise<{ status: string; category?: WaCategory; reason?: string; quality?: 'green'|'yellow'|'red' }>;
  sendTemplate(m: TemplateMessage): Promise<{ providerMessageId: string; acceptedAt: Date }>;
  sendSessionMessage(m: { to: string; text?: string; interactive?: unknown; idempotencyKey: string; policyToken: string }): Promise<{ providerMessageId: string }>;
  sendFlow(m: FlowMessage & { idempotencyKey: string; policyToken: string }): Promise<{ providerMessageId: string }>;
  sendPaymentRequest(o: WaOrderDetails & { idempotencyKey: string; policyToken: string }): Promise<{ providerMessageId: string }>;
  requestCallPermission?(to: string): Promise<{ providerMessageId: string }>;   // flag OFF (wa_calling)
  optOut(to: string, scope: { purpose: string }): Promise<void>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent<MessageEventPayload>[]>; // sent|delivered|read|failed|inbound|flow_response|payment|template_status
}
```

| Attribute | WhatsApp | SMS |
|---|---|---|
| Providers | **Gupshup** (Meta Cloud API BSP; INR WABA) / Interakt / AiSensy / MSG91. Long-term option: Meta Cloud API direct. | **MSG91** (DLT flows, OTP widget) / Gupshup SMS / Kaleyra |
| Auth | Gupshup: `apikey` header **[VERIFY — open (vendor): self-serve uses `apikey`; Partner API uses `Authorization` partner JWT, then per-app token via `GET /partner/app/{appId}/token/` (Gupshup Partner docs, 22 Oct 2026); choose at contracting]**; Meta direct: system-user access token (Bearer). | MSG91: `authkey` header; Gupshup: userid/password or API key; Kaleyra: `api-key`. |
| Endpoints | Meta: `POST /{phone_number_id}/messages`, `POST /{waba_id}/message_templates`, Flows via `/{waba_id}/flows` (consistent with Cloud API). Gupshup template-message endpoint per account type **[VERIFY — open (vendor): Partner API `POST https://partner.gupshup.io/partner/app/{appId}/template/msg` or `/v3/message`; self-serve endpoints differ — fix at contracting]**. | MSG91: `POST /api/v5/flow/` (template_id mapped to DLT template); OTP `POST /api/v5/otp`. |
| Webhooks | Meta-format payloads: `X-Hub-Signature-256: sha256=<hex>` = HMAC-SHA256(app secret, raw body); subscription handshake via `hub.verify_token`. Gupshup callbacks: if Meta-format passthrough is enabled verify `X-Hub-Signature-256`; else per-app secret token in callback URL + IP allow-list **[VERIFY — open (vendor): no public Gupshup callback signature found 22 Oct 2026; treat as unsigned until Gupshup confirms in writing]**. Event ID = `messages[].id` + status. | MSG91 delivery reports: unsigned [Verified 22 Oct 2026, MSG91 DLR webhook help: no signature/auth header documented] → secret path token + IP allow-list; event ID = request ID + MSISDN + status. |
| Idempotency | Local de-dupe on `idempotencyKey` (P07 FR-P07-05) before send; provider `biz_opaque_callback_data` (Cloud API send-message field echoed in status webhooks) carries the communication ID. | Local de-dupe; MSG91 `CRQID` (caller-set, alphanumeric, ≤ 52 chars, echoed per recipient in the DLR) + MSG91 `requestId` [Verified 22 Oct 2026, MSG91 help]. |
| Error mapping | 131026 undeliverable / not on WhatsApp → `POLICY_REJECTED` (fallback to SMS); 131047 re-engagement (outside 24-h window) → VALIDATION; 132xxx template errors → VALIDATION; 130429 throughput → RATE_LIMITED; 131048 spam rate limit → RATE_LIMITED + alert. | DLT template mismatch → `POLICY_REJECTED` (`COMMS_DLT_TEMPLATE_MISMATCH`); invalid number → VALIDATION; operator failure → UNAVAILABLE. |
| Retries / CB | Template sends retried on 5xx/RATE_LIMITED only; failover to another BSP only if the same template is approved there (`reinitiate`); otherwise fall back to SMS step. | `auto` failover to Gupshup/Kaleyra with identical DLT IDs. |
| Sandbox | Meta test WABA + test numbers; Gupshup sandbox app; Flow JSON validated with Meta's Flow schema in CI. | MSG91 test mode with staff numbers; DLT templates in "test" status not used in prod. |
| Residency | Meta hosts Cloud API outside India by default; enable Local Storage (`storage_configuration: {status: IN_COUNTRY_STORAGE_ENABLED, data_localization_region: "IN"}`, API v21+) so content at rest stays in India (in-use processing abroad ≤ 60 min) — content minimised; transfer basis recorded (DPDP s.16). | Indian operators. |
| Cost | Per delivered template: marketing ≈ ₹0.8631, utility ≈ ₹0.115 (free inside open 24-h window), authentication ≈ ₹0.115; service replies free; + 18% GST + BSP markup; Meta may reprice up to 4×/year; **INR WABA mandatory by 31 Dec 2026** (R3 §2.1 [S]). | OTP ≈ ₹0.13–0.17/SMS; DLT PE registration ≈ ₹5,900, header ≈ ₹5,900 each; templates free (R3 §8 [S]). |

### D.2.4 `EMAIL_PORT`

```ts
export interface EmailMessage { from: { tenantDomainId: string; localPart: string }; to: string[]; cc?: string[]; replyTo?: string;
  subject: string; html: string; text: string; headers?: Record<string, string>; listUnsubscribe?: string;
  attachments?: never;                           // policy: links only (P07 FR-P07-08)
  configurationSet: string; tags: Record<string, string>; idempotencyKey: string; policyToken: string }
export interface EmailPort {
  capabilities(): Capabilities;
  send(m: EmailMessage): Promise<{ providerMessageId: string }>;
  verifyDomain(domain: string): Promise<{ dkimTokens: string[]; mailFrom: string; status: string }>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent<{ messageId: string; type: 'delivery'|'bounce'|'complaint'|'reject'|'open'|'click'; bounceType?: 'Permanent'|'Transient' }>[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **AWS SES v2** (ap-south-1) with configuration sets per tenant; **Resend** fallback (React Email) for `internal` data class unless a residency ADR approves personal data. |
| Auth | SES: IAM role (task role), no static keys. Resend: Bearer API key. |
| Webhooks | SES → EventBridge or SNS → `/webhooks/ses`: verify SNS signature (SignatureVersion 2, SHA256; fetch and pin the `SigningCertURL` host `sns.ap-south-1.amazonaws.com`); confirm subscription via `SubscribeURL`. Resend: Svix headers `svix-id`, `svix-timestamp`, `svix-signature` (HMAC-SHA256 with `whsec_` secret). |
| Idempotency | SES has no idempotency key — local de-dupe; Resend `Idempotency-Key` header. |
| Errors | `MessageRejected` → POLICY_REJECTED; `AccountSendingPausedException` → UNAVAILABLE (page on-call); throttling → RATE_LIMITED. Hard bounce → contact point invalid. |
| Sandbox | SES sandbox in non-prod with verified staff addresses; SES mailbox simulator addresses for bounce/complaint tests. |
| Cost | SES US$0.10 per 1,000 emails (list price, Oct 2026); dedicated IPs optional. |

### D.2.5 `PUSH_PORT`

```ts
export interface PushMessage { tokens: string[]; title: string; body: string; data: { deepLink: string; caseId?: string };
  priority: 'default'|'high'; ttlSec: number; collapseId?: string }
export interface PushPort {
  register(deviceToken: string, personId: string, platform: 'ios'|'android', appVariant: string): Promise<void>;
  send(batch: PushMessage[]): Promise<{ ticketId: string; token: string; status: 'ok'|'error'; error?: string }[]>; // ≤ 100 per request
  getReceipts(ticketIds: string[]): Promise<{ ticketId: string; status: 'ok'|'error'; error?: 'DeviceNotRegistered'|'MessageTooBig'|'MessageRateExceeded'|'InvalidCredentials' }[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Expo Push Service** (`POST https://exp.host/--/api/v2/push/send`, receipts `.../push/getReceipts`) with enhanced-security access token; fallback direct **FCM HTTP v1** (OAuth2 service account) and **APNs** token auth (.p8). White-label app variants have their own credentials (`appVariant`). |
| Webhooks | None (poll receipts at +15 min). |
| Errors | `DeviceNotRegistered` → prune token; `MessageRateExceeded` → RATE_LIMITED; `InvalidCredentials` → AUTH (variant credential issue). |
| Policy | Payload never contains case facts (P07 FR-P07-11). |
| Cost | Expo push free; EAS plan separate. |

### D.2.6 `POSTAL_PORT`

```ts
export interface PostalPort {
  createBatch(items: { dispatchId: string; addressee: PostalAddress; documentSha256: string; serviceType: 'SPEED_POST'|'REGISTERED_AD' }[]): Promise<{ batchRef: string; printPdfUri?: string }>;
  recordBooking(dispatchId: string, articleNumber: string, bookedAt: Date, receiptScanUri: string): Promise<void>;
  track(articleNumber: string): Promise<{ events: { at: Date; office: string; status: 'BOOKED'|'IN_TRANSIT'|'OUT_FOR_DELIVERY'|'DELIVERED'|'RTS'|'REFUSED' }[] }>;
  recordPod(dispatchId: string, podScanUri: string, deliveredAt: Date): Promise<void>;
}
```
Adapters: `manual_desk` (default; ops users scan article barcodes in SCR-P07-14), `indiapost_api` (only if a bulk-customer booking/tracking integration is contracted **[VERIFY — open: India Post bulk-customer integration only by DoP contract; no public API or terms]**). Postage billed at actuals (master §7). Port listed in master §4.4 (X-02); used by P02 (`PostalTrackingPollJob`) and P07 (FR-P07-13).

## D.3 Execution and identity ports

### D.3.1 `ESIGN_PORT`

```ts
export type SignType = 'AADHAAR_OTP'|'AADHAAR_BIO'|'DSC'|'VIRTUAL';
export interface EnvelopeRequest { envelopeRef: string; documentPdf: Buffer; documentSha256: string;
  signers: { signerRef: string; role: 'party'|'counsel'|'neutral'|'witness'|'institution'; name: string; mobile?: string; email?: string;
    signType: SignType; order: number; positions: { page: number; x: number; y: number }[] }[];
  stamp?: { stampRef: string; position: 'start'|'end' };   // NN-09: stamp bound before signing
  expiresAt: Date; callbackUrl: string; excludedInstrument: false }   // NN-08: excluded instruments rejected before call
export interface ESignPort {
  createEnvelope(req: EnvelopeRequest, ctx: ProviderContext): Promise<{ envelopeId: string; signerUrls: Record<string, string> }>;
  getEnvelope(envelopeId: string): Promise<{ status: 'sent'|'partially_signed'|'completed'|'expired'|'cancelled'|'failed';
    signers: { signerRef: string; status: string; signedAt?: Date; certSubject?: string }[] }>;
  downloadSignedDocument(envelopeId: string): Promise<Buffer>;   // download immediately (CDN URLs short-lived), write to WORM
  downloadAuditTrail(envelopeId: string): Promise<Buffer>;
  remindSigner(envelopeId: string, signerRef: string): Promise<void>;
  cancelEnvelope(envelopeId: string, reason: string): Promise<void>;
  verifySignature(pdf: Buffer): Promise<{ valid: boolean; signatures: { signer: string; issuer: string; chainValid: boolean; at: Date }[] }>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Leegality** (REST v3.3; Aadhaar eSign OTP/biometric, DSC, virtual sign; ESP auto-switch; NeSL DDE) / **Setu** (multi-ESP orchestration eMudhra/Protean with live switch) / **Digio** / **SignDesk**; optional tenant route `lawdocs_esign` via the LawDocs connector (D.7). Legal basis: IT Act 2000 s.3A + Second Schedule (CCA-licensed ESPs); arbitrators sign with DSC Class 3 or Aadhaar eSign (A&C Act s.31(1)). |
| Auth | Leegality `X-Auth-Token`; Setu client-id/secret + product-instance header (`x-client-id`, `x-client-secret`, `x-product-instance-id`) [Verified 22 Oct 2026, Setu eSign quickstart]; Digio Basic (client_id:secret). |
| Webhooks | Leegality per-invitee webhook `mac` = HMAC-SHA1(documentId, privateSalt) (Leegality knowledge base); confirm hex vs base64 encoding against a sample payload; then re-fetch `GET /v3.3/document/details?file=true&auditTrail=true` before trusting status. Digio: `X-Digio-Checksum` = HMAC-SHA256 hex of payload with webhook secret + Digio IP allow-list [Digio support KB, 22 Oct 2026]. Setu: public docs show only an unsigned `redirectUrl` — poll status **[VERIFY — open (vendor): Setu webhook signing]**. |
| Idempotency | `envelopeRef` = Equator `esign_requests.id` sent as external reference; duplicate create returns existing (adapter checks local table first). |
| Failover | `reinitiate`: a failed/expired envelope on Leegality is cancelled and a new envelope created on Setu after the signer is re-notified; partially signed envelopes are never migrated. |
| Errors | ESP down → UNAVAILABLE (provider auto-switch first); Aadhaar name mismatch → POLICY_REJECTED (case manager task); document too large → VALIDATION (Equator limit 10 MB — matches Cashfree eSign's published cap **[VERIFY — open (vendor): Leegality/Digio/Setu limits in writing]**). |
| Sandbox | Leegality/Setu sandbox with test Aadhaar flows; eMudhra sandbox ESP; signature-validation tests against CCA test roots. |
| Residency | Indian ESPs; signed PDFs and audit trails stored in S3 Object Lock ap-south-1. |
| Cost | Market ₹15–40/eSign **[UNVERIFIED]**; direct ESP ≈ ₹5/sign at volume (eMudhra sandbox page). |

### D.3.2 `ESTAMP_PORT`

```ts
export interface EStampPort {
  isAvailable(state: StateCode, instrument: InstrumentType): Promise<{ available: boolean; mode: 'estamp'|'franking'|'esbtr'|'physical_only' }>;
  quoteDuty(req: { state: StateCode; instrument: InstrumentType; consideration?: Money; article?: string }): Promise<{ duty: Money; ruleRef: string; computedBy: 'equator_rules'|'provider' }>;
  procureStamp(req: { stampRef: string; state: StateCode; instrument: InstrumentType; firstParty: string; secondParty: string;
    purpose: string; duty: Money; payerPartyRef: string }, ctx: ProviderContext): Promise<{ stampId: string; certificateNo: string; issuedAt: Date }>;
  attachToDocument(stampId: string, pdf: Buffer, position: 'start'|'end'): Promise<Buffer>;
  getCertificate(stampId: string): Promise<Buffer>;
  releaseUnused(stampId: string): Promise<void>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Leegality BharatStamp** ("Available in 31 States/UTs" via Leegality Stamp Network + NeSL; Lakshadweep, Nagaland and DNH&DD appear uncovered — Oct 2026) / **Setu** (docs list Assam, Chandigarh, Delhi, Gujarat, Haryana, HP, J&K, Jharkhand, Karnataka, Puducherry, Punjab, Rajasthan, Tamil Nadu, UP, Uttarakhand, Ladakh, MP; Maharashtra, Telangana, West Bengal physical only; stamps procured offline in advance [Verified 22 Oct 2026, docs.setu.co/data/esign/estamp: MP both eStamp and physical; MH/TG/WB physical only]) / **Digio** / **SignDesk–NeSL**. SHCIL has no public API (aggregators only). |
| Routing | State-conditioned rows: `conditions: {"state":["MH","TG","WB"]}` → Leegality only, else `physical_only` path to the P06 registration/physical execution checklist. Duty is **always computed by Equator's state duty matrix** (`core.legal_rules` + stamp rules config, NN-09) and compared with the provider quote; mismatch > ₹1 → block and task. |
| Auth / webhooks | As ESIGN_PORT for the same vendor. |
| Idempotency | `stampRef` unique; procurement is money-moving — never retried after timeout without `getCertificate` reconciliation. |
| Errors | State/instrument unsupported → UNSUPPORTED (next provider or physical route); insufficient prepaid wallet → INSUFFICIENT_FUNDS. |
| Sandbox | Provider test stamps (non-legal) only; per-state live test transaction matrix before launch for DL, UP, RJ, MH, KA, TN, TG, WB, GJ, HR (R3 §3.2, U6). |
| Cost | Duty at actuals (pass-through fee line `stamp_duty_passthrough`, not GST-able) + procurement fee (₹50–120/doc incl. eSign **[UNVERIFIED]**). |

### D.3.3 `KYC_PORT`

```ts
export interface KycPort {
  startDigiLockerConsent(req: { personRef: string; docTypes: ('AADHAAR'|'PAN'|'DL'|'VOTER')[]; redirectUrl: string }): Promise<{ url: string; requestId: string }>;
  fetchDigiLockerDocuments(requestId: string): Promise<{ docType: string; issuer: string; xmlSha256: string; maskedId: string; name: string; dob?: string; photo?: Buffer }[]>;
  verifyPan(pan: string, name?: string, dob?: string): Promise<{ valid: boolean; nameMatch?: number; status: string }>;
  verifyBankAccount(acc: { ifsc: string; number: string; name?: string }): Promise<{ valid: boolean; registeredName?: string; nameMatch?: number }>;
  verifyGstin(gstin: string): Promise<{ legalName: string; status: string; stateCode: string }>;
  verifyCompany(cinOrLlpin: string): Promise<{ name: string; status: string; directors: { din: string; name: string }[] }>;
  verifyUdyam(udyamNo: string): Promise<{ enterpriseName: string; category: 'micro'|'small'|'medium'; valid: boolean }>;
  faceMatch(selfie: Buffer, reference: Buffer): Promise<{ score: number; match: boolean }>;
  liveness(media: Buffer | { sdkToken: string }): Promise<{ live: boolean; score: number }>;
  searchCourtCases(q: { name?: string; cnr?: string; state?: string }): Promise<{ cnr: string; court: string; status: string; source: 'aggregator' }[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Surepass** (DigiLocker, PAN, bank, GSTIN, MCA, Udyam, eCourts CNR, face/liveness) / IDfy / Signzy / **HyperVerge** (P1 for liveness; RN SDK). |
| Legal limits | No Aadhaar OTP e-KYC by Equator (Aadhaar Act s.4(4), s.8 — AUA/KUA only); DigiLocker/offline XML route; store masked Aadhaar (last 4) and XML hash only (NN-14). CKYC only via a PMLA reporting-entity tenant. Court-record results are labelled "aggregator data, not an official court record". |
| Auth | Surepass Bearer token; HyperVerge appId/appKey; IDfy account-id + api-key. |
| Webhooks | DigiLocker redirect/callback via provider (state parameter = signed Equator nonce); async liveness callbacks signed per provider **[VERIFY — open: provider liveness callback signing at contracting]**. |
| Idempotency | Lookups idempotent; cache results 24 h per (tenant, identifier hash) to control cost. |
| Errors | Source registry down (NSDL/MCA/GSTN) → UNAVAILABLE with `auto` failover; mismatch → POLICY_REJECTED (manual review). |
| Residency | Indian vendors; DPAs requiring deletion of source documents after response. |
| Cost | Low per-call **[UNVERIFIED]**; metered per check. |

## D.4 Money ports

### D.4.1 `PAYMENTS_PORT`

```ts
export interface PaymentsPort {
  createOrder(o: { orderRef: string; amount: Money; caseId: string; feeLines: FeeLineRef[]; splits?: { linkedAccountId: string; amount: Money; holdUntil?: Date }[] }, ctx: ProviderContext): Promise<{ orderId: string; checkout: Record<string, string> }>;
  createPaymentLink(l: { linkRef: string; amount: Money; description: string; payer: { name: string; contact?: string; email?: string }; expiresAt: Date; notify: boolean }, ctx: ProviderContext): Promise<{ linkId: string; url: string }>;
  createVirtualAccount(caseId: string, payerPartyRef: string): Promise<{ vaId: string; accountNumber?: string; ifsc?: string; upiId?: string }>;
  createMandate(m: { mandateRef: string; maxAmount: Money; frequency: 'monthly'|'as_presented'; startAt: Date; endAt: Date; payer: PartyContact }): Promise<{ mandateId: string; authUrl: string }>;
  refund(paymentId: string, amount: Money, reason: string, refundRef: string): Promise<{ refundId: string; status: string }>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;   // payment.captured|failed, refund.processed, order.paid, va.credited, mandate.*
}
```

| Attribute | Specification |
|---|---|
| Providers | **Razorpay** (Orders, Payment Links, Smart Collect, UPI AutoPay/eMandate, WhatsApp Payments deep integration) / **Cashfree**; **Razorpay International / PA-CB** for USD/EUR/GBP/SGD/AED; PayPal for foreign parties; Stripe India not used (invite-only since Jun 2024). |
| Scope rule | Only platform fees and neutral fees (NN-13). `createOrder` rejects any fee line of type `settlement_sum` (`PAYMENTS_SETTLEMENT_ON_MERCHANT_FORBIDDEN`). RBI Payment Aggregator Directions, 15 Sep 2025. |
| Auth | Razorpay Basic (key_id:key_secret); Cashfree `x-client-id`, `x-client-secret`, `x-api-version`. |
| Webhooks | Razorpay `X-Razorpay-Signature` = hex HMAC-SHA256(webhook secret, raw body); event ID header `x-razorpay-event-id`. Cashfree `x-webhook-signature` = base64 HMAC-SHA256(secret, `x-webhook-timestamp` + raw body). |
| Idempotency | Razorpay order `receipt` = `orderRef` (unique, ≤ 40 chars); local de-dupe; Cashfree `x-idempotency-key` (optional on Create Order; `x-api-version` default 2026-01-01) [Verified 22 Oct 2026, Cashfree PG API ref]. Refunds carry `refundRef`. |
| Errors | `BAD_REQUEST_ERROR` → VALIDATION; `GATEWAY_ERROR`/`SERVER_ERROR` → UNAVAILABLE; payment failures are domain events, not adapter errors. |
| Limits | Manual-capture window is at most 3 days (no 7-day authorisation hold — use capture + auto-refund); UPI AutoPay maximum debit ₹99,999 (category-dependent); loan/settlement instalment e-mandates are AFA-free only up to ₹15,000 per debit (the ₹1 lakh limit applies only to insurance, mutual-fund and credit-card categories). Values are configuration, not code. |
| Reconciliation | Daily settlement report pull and match against `core.payments`; mismatches → finance task. |
| Sandbox | Razorpay/Cashfree test mode; test cards/UPI handles; webhook replay tests. |
| Cost | PG ≈ 2% standard; UPI P2M often 0% MDR for small merchants (negotiate) **[UNVERIFIED]**; international higher MDR. |

### D.4.2 `PAYOUT_PORT`

```ts
export interface PayoutPort {
  onboardLinkedAccount(a: { neutralOrInstitutionRef: string; legalName: string; pan: string; gstin?: string; bank: { ifsc: string; number: string }; email: string; phone: string }): Promise<{ linkedAccountId: string; status: 'created'|'under_review'|'activated'|'needs_clarification' }>;
  transfer(t: { transferRef: string; paymentId?: string; linkedAccountId: string; amount: Money; holdUntil?: Date; notes: Record<string, string> }): Promise<{ transferId: string; status: string }>;
  releaseHold(transferId: string): Promise<void>;
  reverseTransfer(transferId: string, amount?: Money): Promise<{ reversalId: string }>;
  payout(p: { payoutRef: string; beneficiary: { ifsc: string; number: string; name: string }; amount: Money; mode: 'IMPS'|'NEFT'|'RTGS'|'UPI'; purpose: 'refund'|'payout' }): Promise<{ payoutId: string; status: string }>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;  // transfer.processed|failed, payout.*
}
```

| Attribute | Specification |
|---|---|
| Providers | **Razorpay Route** (linked accounts for neutrals/institutions as marketplace sellers; transfers with on-hold; 24-h cooling after linked-account creation; failed transfers retried up to 3 times by Razorpay) + RazorpayX Payouts / **Cashfree Easy Split + Payouts** (holds via delayed split-after-payment). |
| Rules | Neutral payouts only after bank verification (`KYC_PORT.verifyBankAccount`); TDS computed by `billing` (Income-tax Act 2025 mapping, master §7) before transfer amount is set; foreign neutrals → Form 145/146 workflow (R5) outside this port. |
| Idempotency | RazorpayX payouts require `X-Payout-Idempotency` (mandatory since 15 Mar 2025; 4–36 chars; identical body on retry); transfers keyed by `transferRef` in notes + local de-dupe. Never retry after timeout without status fetch. |
| Errors | Insufficient balance → INSUFFICIENT_FUNDS; beneficiary bank down → UNAVAILABLE (provider queues); linked account not activated → POLICY_REJECTED. |
| Sandbox | Route test mode linked accounts; RazorpayX test payouts. |

### D.4.3 `ESCROW_PORT`

```ts
export interface EscrowPort {
  openEscrow(e: { escrowRef: string; caseId: string; depositor: PartyRef; beneficiary: PartyRef; amount: Money;
    releaseConditions: { milestoneRef: string; condition: string; evidenceTypes: string[]; amount: Money }[]; trusteeRef?: string }, ctx: ProviderContext): Promise<{ escrowId: string; status: 'pending_kyc'|'open' }>;
  getDepositInstructions(escrowId: string): Promise<{ accountNumber: string; ifsc: string; beneficiaryName: string; upiId?: string; reference: string }>;
  instructRelease(escrowId: string, r: { milestoneRef: string; amount: Money; settlementAgreementSha256: string; approvals: { userId: string; role: 'escrow_officer'; at: Date }[] }): Promise<{ releaseId: string; status: string }>; // maker–checker (two escrow_officer approvals)
  instructRefund(escrowId: string, reason: string, approvals: Approval[]): Promise<{ releaseId: string }>;
  getStatement(escrowId: string): Promise<{ balance: Money; entries: { at: Date; type: 'deposit'|'release'|'refund'|'fee'; amount: Money; utr?: string }[] }>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;
}
```

| Attribute | Specification |
|---|---|
| Providers | **Castler** (escrow-as-a-service with bank + trustee) / **RazorpayX Escrow+** / `direct_with_proof` (payer pays payee directly; party uploads UTR/receipt; counter-party confirms; platform records evidence only). Settlement sums never touch Equator's merchant account (NN-13). |
| Auth / webhooks | Enterprise APIs not public — signature schemes and endpoints to be fixed at contracting **[VERIFY — open: contract condition — no public spec]**; require HMAC-signed callbacks or mTLS as a contract condition. |
| Idempotency | `escrowRef`, `milestoneRef`; release instructions are never retried without statement reconciliation. |
| Failover | `none` — an open escrow stays with its bank/trustee. |
| Legal | Eligibility of dispute settlement sums for each provider's escrow product requires PA risk-team sign-off and legal opinion (R3 U7). |
| Cost | Setup + per-transaction fee (bank tariff) **[UNVERIFIED]**; billed as `escrow_fee` line (master §7). |

### D.4.4 `TAX_INVOICE_PORT`

```ts
export interface TaxInvoicePort {
  generateEInvoice(inv: { invoiceNo: string; invoiceDate: string; supplierGstin: string; buyerGstin?: string; placeOfSupply: string;
    lines: { hsnSac: string; description: string; taxable: Money; cgst?: Money; sgst?: Money; igst?: Money }[]; exportLut?: string }): Promise<{ irn: string; ackNo: string; ackDate: Date; signedQr: string; signedInvoice: string }>;
  cancelEInvoice(irn: string, reasonCode: '1'|'2'|'3'|'4', remark: string): Promise<void>;  // within 24 h of IRN generation
  getByIrn(irn: string): Promise<{ status: 'ACT'|'CNL' }>;
  validateGstin(gstin: string): Promise<{ legalName: string; status: string }>;
}
```

| Attribute | Specification |
|---|---|
| Providers | GSP/ASP: **ClearTax** / **Masters India** / IRIS → IRP. Mandatory for B2B/export invoices once AATO > ₹5 crore; for AATO ≥ ₹10 crore the IRP rejects documents older than 30 days (R3 §4.3 [S]). B2C fee invoices are not e-invoiced (dynamic QR rules apply where AATO > ₹500 crore — not expected). |
| Auth | GSP client credentials + IRP user credentials with 2FA (IRP auth token valid 6 hours; refresh before expiry). |
| Idempotency | IRP rejects duplicate (supplier GSTIN, doc type, doc no., FY) with "duplicate IRN" — adapter maps to CONFLICT and fetches existing IRN. |
| Errors | Schema/GSTIN errors → VALIDATION (invoice held, finance task); IRP downtime → UNAVAILABLE (queue; invoice issued only after IRN for B2B). |
| Sandbox | IRP sandbox via GSP. |

## D.5 Hearing, language and AI ports

### D.5.1 `VIDEO_PORT`

```ts
export interface VideoPort {
  createRoom(r: { roomKey: string; kind: 'JOINT'|'CAUCUS'|'LOBBY'|'BREAKOUT'|'INTERPRETER'; caseId: string; sessionId: string; region: 'india'; maxParticipants: number; emptyTimeoutSec: number }): Promise<{ roomSid: string }>;
  issueJoinToken(t: { roomKey: string; identity: string; displayName: string; role: 'neutral'|'party'|'counsel'|'witness'|'observer'|'interpreter'|'case_manager'; canPublish: boolean; canSubscribe: boolean; ttlSec: number }): Promise<string>;
  moveParticipant(identity: string, fromRoom: string, toRoom: string): Promise<void>;     // implemented as revoke + new token if unsupported (R3 U9)
  updatePermissions(roomKey: string, identity: string, perms: { canPublish?: boolean; canSubscribe?: boolean }): Promise<void>;
  removeParticipant(roomKey: string, identity: string): Promise<void>;
  startRecording(roomKey: string, o: { consentIds: string[]; layout: 'speaker'|'grid'; s3Prefix: string }): Promise<{ egressId: string }>; // NN-11: refused for mediation/conciliation rooms and CAUCUS
  stopRecording(egressId: string): Promise<void>;
  dialOutPstn(roomKey: string, e164: string, identity: string): Promise<void>;
  closeRoom(roomKey: string): Promise<void>;
  verifier: WebhookVerifier;
  parseWebhook(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;  // participant_joined/left, egress_ended, room_finished
}
```

| Attribute | Specification |
|---|---|
| Providers | **LiveKit Cloud** (Scale plan, region pinning `india`) / self-hosted LiveKit OSS in ap-south-1 / **100ms**. Caucus isolation = separate rooms with server-minted, room-scoped tokens (isolation enforced by the SFU, not UI). |
| Auth | LiveKit API key/secret → JWT access tokens; server SDK for room service and egress. 100ms management token. |
| Webhooks | LiveKit: `Authorization` header carries a JWT signed with the API secret containing a `sha256` claim of the body — verify both. 100ms: webhook secret header configured per workspace **[VERIFY — open (vendor): header name/scheme on 100ms 'Secure Your Webhooks' page not readable 22 Oct 2026]**. |
| Recording guard | `startRecording` requires `consentIds` covering every participant and the tribunal's direction (arbitration only); adapter double-checks room `kind` and proceeding mechanism metadata. |
| Residency | Region pinning on Scale+; egress written directly to S3 ap-south-1 Object Lock bucket; confirm agents/egress pinning (R3 U9). |
| Cost | LiveKit Scale $500/mo incl. 1.5M participant-min, then $0.0004/min; recordings $0.005/min; 100ms $0.004/participant-min. |

### D.5.2 `TRANSCRIPTION_PORT` and `TRANSLATION_PORT`

```ts
export interface TranscriptionPort {
  startLive(roomKey: string, o: { languages: Lang[]; diarize: boolean; persist: boolean }): Promise<{ sessionId: string }>; // persist=false for mediation captions
  stopLive(sessionId: string): Promise<void>;
  transcribeFile(audio: { s3Uri: string; sha256: string }, o: { language?: Lang; diarize: boolean }): Promise<{ jobId: string }>;
  getTranscript(jobId: string): Promise<{ status: 'pending'|'done'|'failed'; turns?: TranscriptTurn[]; wer?: number }>;
}
export interface TranslationPort {
  translateText(text: string, from: Lang, to: Lang, o?: { glossaryId?: string; formality?: 'formal' }): Promise<{ text: string; glossaryHits: string[]; uncertainSpans: [number, number][] }>;
  translateDocument(doc: { s3Uri: string; sha256: string }, to: Lang[]): Promise<{ jobId: string }>;
  detectLanguage(text: string): Promise<{ lang: Lang; confidence: number }>;
}
```

| Attribute | Specification |
|---|---|
| Providers | Transcription: **Sarvam Saaras** (STT ₹30/hr; ₹45/hr with diarization) / AI4Bharat IndicConformer self-hosted (telephony WER ~22–30% Hindi [S]). Translation: **Sarvam Translate** (₹20 per 10K chars) / **IndicTrans2** self-hosted on GPU in Mumbai / **Bhashini** for government tenants (no SLA — never sole stack). |
| Auth | Sarvam `api-subscription-key`; Bhashini ULCA `userID` + `ulcaApiKey` headers (pipeline API); self-hosted via internal mTLS. |
| Rules | Machine translation in hearings labelled "unofficial machine translation"; certified interpreter remains the record; legal templates need human approval (NN-23). Mediation live captions: `persist=false`, discarded at session end (NN-11). |
| Idempotency | Cache by (content sha256, from, to, glossary version). |
| Cost | As above; self-hosted GPU cost allocated per tenant by characters. |

### D.5.3 `LLM_PORT`

```ts
export type ModelAlias = 'haiku-4.5'|'sonnet-5'|'opus-5'|'sarvam-105b';
export interface LlmRequest { model: ModelAlias; system: string; messages: { role: 'user'|'assistant'; content: ContentBlock[] }[];
  tools?: ToolDef[]; documents?: { id: string; title: string; text: string }[]; citations?: boolean;
  maxTokens: number; temperature: number; residency: 'IN'; dataClass: DataClass; interactionId: string; cacheSystem?: boolean }
export interface LlmResult { text?: string; toolCalls?: { id: string; name: string; input: unknown }[];
  citations?: { documentId: string; start: number; end: number; quoted: string }[];
  stopReason: 'end_turn'|'tool_use'|'max_tokens'|'refusal'; usage: { inTokens: number; outTokens: number; cacheRead: number; cacheWrite: number };
  modelId: string; region: string }
export interface LlmPort {
  complete(r: LlmRequest): Promise<LlmResult>;
  structured<T>(r: LlmRequest & { schema: JsonSchema }): Promise<{ value: T; raw: LlmResult }>;  // ajv-validated; 1 repair retry
  embed(texts: string[], o: { model: 'titan-embed-text-v2'|'cohere-embed-multilingual-v3'; inputType: 'document'|'query' }): Promise<number[][]>; // in-Region only (no cross-Region profile for embeddings)
  capabilities(): Capabilities & { citations: boolean; promptCaching: boolean; maxContext: number };
}
```

| Attribute | Specification |
|---|---|
| Providers | **Amazon Bedrock** — Claude Opus 5 / Sonnet 5 / Haiku 4.5 via the **India geographic cross-Region inference profile** (Mumbai + Hyderabad; launched 5 Oct 2026; Opus 5, Sonnet 5, Haiku 4.5 — confirmed); Converse/InvokeModel APIs; prompt caching supported on all three `in.` profiles (min tokens/checkpoint Opus 5 512, Sonnet 5 1,024, Haiku 4.5 4,096; TTL 5 min/1 h) [Verified 22 Oct 2026, Bedrock model cards]; Haiku 4.5 on the India profile has no structured outputs; Citations (Converse `CitationsConfig`) **[VERIFY — open (vendor): per-model Citations support not stated on the model cards; test at build]**. Embeddings in-Region: Amazon Titan Text Embeddings V2 (ap-south-1, ap-south-2) or Cohere Embed Multilingual v3 (ap-south-1). Fallback: Sarvam 105B (India-hosted; ₹15/₹60 per 1M in/out tokens) for `indic_low_risk` tier only; Anthropic API direct for `dataClass = 'public'` only. |
| Auth | IAM role (SigV4) scoped to the inference-profile ARN; no static keys. Sarvam API key. |
| Residency guard | Adapter refuses (`RESIDENCY`) if `residency !== 'IN'` is unsatisfiable for the resolved endpoint or if the profile ARN is not on the allow-list; health check asserts profile region set ⊆ {ap-south-1, ap-south-2} daily; embedding calls must target an ap-south-1/ap-south-2 in-Region endpoint. |
| Errors | `ThrottlingException` → RATE_LIMITED; `ModelTimeoutException`/`ServiceUnavailableException` → UNAVAILABLE; `ValidationException` → VALIDATION; `AccessDeniedException` → AUTH; content refusal → returned as `stopReason: 'refusal'` (not an error). |
| Retries / CB | Retry ×2 on RATE_LIMITED/UNAVAILABLE before any tokens streamed; no retry mid-stream; CB open → P11 deterministic fallback (NN-02). |
| Sandbox | Separate AWS accounts per environment; eval runs use synthetic data only. |
| Cost | Tokens metered per interaction into `core.ai_interactions`; INR via FX snapshot. |

### D.5.4 `DOC_AI_PORT`

```ts
export interface DocAiPort {
  digitize(file: { s3Uri: string; sha256: string; mime: string }, o: { languages?: Lang[]; output: 'markdown'|'json' }): Promise<{ jobId: string }>;
  extract(file: { s3Uri: string; sha256: string }, schema: JsonSchema): Promise<{ jobId: string }>;
  classify(file: { s3Uri: string; sha256: string }, labels: string[]): Promise<{ label: string; confidence: number }[]>;
  getJob(jobId: string): Promise<{ status: 'pending'|'done'|'failed'; pages?: { n: number; text: string; blocks: Block[] }[]; fields?: Record<string, { value: unknown; confidence: number; page: number; bbox?: number[] }> }>;
}
```
Providers: **Sarvam Vision 2.1** (Digitize ₹0.5/page, Extract ₹1/page, 10 pages per job; vendor Indic OCR bench 87.39) / Azure Document Intelligence v4.0 API 2024-11-30 (Central India region **[VERIFY — open (vendor): provision a test resource in centralindia before enabling]**) / Google Document AI (non-personal data unless residency ADR). Files are passed by pre-signed S3 URL (15-min TTL) or upload; provider deletion confirmed by contract. Cache by file sha256. Sealed-schema documents are never sent (NN-07).

## D.6 Reference-data and regulated-rail ports

### D.6.1 `FX_PORT`

```ts
export interface FxPort {
  getRate(q: { base: CurrencyCode; quote: 'INR'; date: string; kind: 'reference'|'settlement' }): Promise<{ rate: string; source: 'FBIL'|'COMMERCIAL'|'PSP_SETTLEMENT'|'MANUAL'; publishedAt: Date; sourceRef: string }>;
}
```
Primary: **FBIL** reference rates (USD, EUR, GBP, JPY only; no SGD/AED) ingested daily after publication at ~13:00 IST (time effective 6 Jan 2025; poll until available) into `core.fx_rates`. SGD and AED: derived cross-rates (AED via the USD peg of 3.6725) or the AD bank's TT rate — the method is configuration; fallback commercial FX API; settlement-kind rates taken from the PSP's settlement report (Razorpay International/PayPal). Rates stored as decimal strings with source and timestamp; every quote/invoice in non-INR snapshots the rate ID (NN-13, master §7). Manual entry requires maker–checker.

### D.6.2 `SANCTIONS_PORT`

```ts
export interface SanctionsPort {
  screen(s: { screeningRef: string; subjects: { kind: 'person'|'entity'|'vessel'; names: string[]; dob?: string; nationality?: string[]; country?: string; identifiers?: Record<string, string> }[];
    lists: ('UN'|'OFAC_SDN'|'OFAC_50PCT'|'EU'|'UK'|'MHA_UAPA')[] }): Promise<{ screeningId: string; hits: { subjectIndex: number; list: string; entryId: string; name: string; score: number; reasons: string[] }[]; listVersions: Record<string, string> }>;
  rescreen(screeningId: string): Promise<{ changed: boolean; hits: unknown[] }>;
  subscribeMonitoring(screeningId: string, untilDate: string): Promise<void>;
}
```
Providers: commercial screening API (ComplyAdvantage-class or Surepass Anti Money Laundering Verification API) / `local_list_matcher` (Equator-hosted ingest of UN SC Consolidated List XML, OFAC SDN, EU consolidated list, UK sanctions list, MHA UAPA designations entered manually from the Gazette; matching: Unicode/transliteration normalisation, Jaro-Winkler ≥ 0.88 on name tokens, DOB/country tie-breakers). Any hit → case hold and compliance review with documented decision (NN-19, R5 Gate G1); annual re-screen and on party change; list versions recorded on each screening.

### D.6.3 `AA_PORT`

```ts
export interface AaPort {
  requestConsent(r: { fiuTenantId: string; customerVua: string; fiTypes: ('DEPOSIT'|'TERM_DEPOSIT'|'RECURRING_DEPOSIT')[]; purposeCode: string;
    dateRange: { from: string; to: string }; consentMode: 'VIEW'|'STORE'; fetchType: 'ONETIME'; dataLifeDays: number }): Promise<{ consentHandle: string; redirectUrl: string }>;
  getConsentStatus(handle: string): Promise<{ status: 'PENDING'|'ACTIVE'|'REJECTED'|'REVOKED'|'EXPIRED'; consentId?: string }>;
  fetchData(consentId: string): Promise<{ accounts: { maskedAccNo: string; fiType: string; summary: Record<string, unknown>; transactions?: unknown[] }[]; fetchedAt: Date }>;
  revokeConsent(consentId: string): Promise<void>;
}
```
Rules: Equator is never an FIU (NN-14). The adapter runs **under the lender tenant's FIU credentials** through its TSP (Setu AA / Finvu / OneMoney) and ReBIT AA specifications (JWS-signed requests, Curve25519 key exchange for FI data); purpose code 105 (explicit one-time consent for the accounts) or 103 (aggregated statement) per the ReBIT purpose list **[VERIFY — open: confirm with the tenant's TSP]**; `consentMode = 'VIEW'` default; raw statements decrypted only inside the tenant's processing context and reduced to derived summaries for neutrals (D6); raw data deleted at data-life expiry. Fallback: party uploads bank statement PDF → `DOC_AI_PORT`. Failover `none`.

## D.7 Group-company connectors (`GROUP`)

All group connectors use: OAuth 2.0 client credentials (per tenant, scopes per resource) + mTLS between AWS accounts; outbound webhooks from Equator signed `X-Equator-Signature: t=<unix>,v1=<hex HMAC-SHA256("t.body")>` with per-subscription secrets (`core.webhook_subscriptions`); inbound calls carry `Idempotency-Key`; payload schemas versioned in `packages/domain/src/connectors/*` and published in the developer portal (P09). Group companies are separate data fiduciaries/processors: data sharing only within the tenant's purpose and contract (DPDP s.6/s.7; NN-16 — no case data to group marketing).

| Connector | Direction | Contract | Notes |
|---|---|---|---|
| **Finbyx (LOS/LMS)** | Finbyx → Equator | `POST /v1/clauses/registrations` (loan ID, borrower person ref, clause version ID, e-signed loan-agreement hash, sanction date) — **clause-at-sanction (D1)**; `POST /v1/bulk-jobs` (default/dispute referrals, CSV/JSON, ≤ 100,000 rows); `POST /v1/integrations/finbyx/repayments` (UTR, amount, date — instalment reconciliation for settlements); `PUT /v1/integrations/finbyx/contact-preferences` (borrower preferred time, language, blackout flags from lender records) | Lender tenant is the RE; Equator acts as service provider (RBI Digital Lending Directions 2025; outsourcing terms). Appointment triggers from Finbyx are **ignored** for neutral selection (NN-03): the API has no field for arbitrator choice and rejects unknown fields. |
| | Equator → Finbyx | Webhooks: `equator.cases.case.status_changed.v1`, `equator.outcomes.settlement.executed.v1` (terms, instalment schedule), `equator.outcomes.award.issued.v1` (award PDF hash + certified-copy link), `equator.escrow.milestone.released.v1` | No counter-party transcripts or caucus data ever sent. |
| **Udofin (LSP/DLA)** | Udofin → Equator | Grievance escalation `POST /v1/grm/desks/{deskId}/tickets` (RE name, DLA name, GRO, complaint, 30-day clock start); DLA disclosure metadata | Equator never collects payments into its account for Udofin-originated matters; RE name and GRO shown on borrower screens. |
| | Equator → Udofin | Ticket status, ODR escalation, outcome summary | — |
| **LawDocs** | LawDocs → Equator | Template/clause library sync (`POST /v1/integrations/lawdocs/templates` → `core.document_templates` in `draft`, **legal review required before activation**); optional `ESIGN_PORT` provider `lawdocs_esign` delegating to LawDocs' ESP integration **[VERIFY — open: internal — LawDocs ESP delegation]** | Templates imported never auto-activate (NN-23). |
| | Equator → LawDocs | Executed-document references for the party's LawDocs vault (party consent purpose `document_vault_sync`) | Opt-in per party. |
| **BestComply / LawDocsComply** | Equator → BestComply | Compliance obligations and regulatory MIS: GRM TAT reports, Internal Ombudsman referrals, RB-IOS escalation counts, POSH annual-report **numbers only** (NN-07), award stamping deadlines (`core.compliance_obligations`) | Aggregates only; no personal data unless the tenant enables named-officer tasks. |
| | BestComply → Equator | Regulatory calendar updates proposed as `core.config_change_requests` (maker–checker) | Never auto-applied to Legal Rules Register. |

## D.8 Government and ecosystem connectors (`GOV`)

Port token: **`CONNECTOR_PORT`** (master §4.4). Adapter codes also include `SCORES` (SEBI SCORES 2.0 reference capture) and `LSA_EXPORT` (Form-1 PIMS application pack for the Legal Services Authority under Commercial Courts Act s.12A and the PIMS Rules 2018 — M-06), both `export_pack` mode, as used in P09.

```ts
export interface GovConnector {
  code: 'MSME_ODR'|'ONDC_IGM'|'ECOURTS_LOOKUP'|'SAHAMATI_VIKALP'|'SEBI_SMART_ODR';
  capabilities(): { mode: 'api'|'export_pack'|'lookup'; inbound: boolean; outbound: boolean; flag: string };
  buildExportPack?(caseId: string): Promise<{ zipUri: string; manifestSha256: string }>;   // JSON + PDFs + hash manifest + BSA s.63 cert (NN-10)
  submit?(caseId: string, packUri: string): Promise<{ externalRef: string }>;
  receive?(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;
  getStatus?(externalRef: string): Promise<{ status: string; updatedAt: Date }>;
}
```

| Connector | Mode (default) | Flag | Specification |
|---|---|---|---|
| **MSME ODR / MSEFC** | `export_pack` | `gov.msme_odr.enabled` (ON for export) | No public API (checked Oct 2026; MSME ODR portal live 27 Jun 2025; Centre considering empanelling private ODR firms, still a proposal). Export pack only. Signposting (MSMED Act s.18; *Gujarat State Civil Supplies v Mahakali Foods*, SC 31 Oct 2022) for Udyam-registered micro/small suppliers; export pack = F-C14 reference fields (Udyam no., invoices, acceptance date, s.15 due date ≤ 45 days, s.16 interest computed by Equator calculator) + documents; the **supplier files**; status updated manually by case manager. |
| **ONDC IGM** | `api` | `gov.ondc_igm.enabled` (OFF) | Beckn-based IGM APIs (`/issue`, `/on_issue`, `/issue_status`, `/on_issue_status`) with network-participant registry subscription and request signing (Ed25519 `Authorization` signature header) **[VERIFY — open: current ONDC IGM version and ODR-provider onboarding]**. Requires Equator registration as an ODR provider on the network; inbound escalations create GRM/ODR cases with buyer/seller app references. |
| **eCourts / NJDG lookups** | `lookup` | `gov.ecourts_lookup.enabled` (ON) | No official public developer API; uses `KYC_PORT.searchCourtCases` (Surepass eCourt CNR aggregator). Purpose: parallel-litigation and s.12A/s.8 checks; results labelled "aggregator data, not an official court record", never placed in evidence bundles without a certified copy. Export packs for future eCourts Phase III ODR ingest. |
| **Sahamati inter-member dispute framework** (no "Vikalp" programme exists — corrected 22 Oct 2026) | `api` (stub) | `gov.sahamati_imdr.enabled` (OFF) | Equator is not empanelled (window closed, R1). Build schema mapping only (complaint first raised with FI; counterparty AA-network participant; AA consent logs as evidence). Activate only after empanelment. |
| **SEBI SMART ODR** | `api` (stub) | `sec.smart_odr.enabled` (OFF; master §1.2) | SEC connector; regulated fee schedule applied exactly (NN-18); SEBI consultation of 23 Jul 2026 may move administration to MIIs — no revenue dependency. No SEBI/MII API for ODRIs exists in the current Master Circular or the 23 Jul 2026 draft; interface = manual case-pack import/export, with an API stub kept behind the flag. |

## D.8A Consent Manager port (`CONSENT_MANAGER_PORT`)

DPDP Act s.6(7)–(9) and DPDP Rules 2025 Rule 4 (Consent Manager registration from 13 Nov 2026; core obligations from 13 May 2027). Equator captures consent natively in `core.consent_records` (P01); this port lets a Data Principal manage the same consents through a registered Consent Manager once one is contracted. Mock adapter in sandbox until then (P14).

```ts
export interface ConsentManagerPort {
  registerNotice(n: { purposeCodes: string[]; noticeId: string; noticeSha256: string; locale: string }): Promise<{ cmNoticeRef: string }>;
  pushConsent(c: { consentRecordId: string; principalRef: string; purposeCode: string; status: 'given'|'withdrawn'; at: Date }): Promise<{ cmConsentRef: string }>;
  receive(headers: Headers, rawBody: Buffer): Promise<NormalisedEvent[]>;   // withdrawal / modification from the CM → propagate per P01 withdrawal rules
  getStatus(cmConsentRef: string): Promise<{ status: 'given'|'withdrawn'|'expired'; updatedAt: Date }>;
}
```

## D.9 Growth ports (`CRM_PORT`, `ANALYTICS_PORT`)

Both ports serve the `growth` bounded context only (P13), run against the physically separate growth database, and never receive case data (NN-16; P13 FR-P13-26). Every call passes the respondent suppression check (P07 `GET /v1/suppression/check`) and the person's marketing/analytics consent before any outbound sync.

```ts
export interface CrmPort {
  upsertContact(c: { leadId: string; email?: string; phone?: string; name?: string; persona: string; consents: string[]; syncVersion: number }): Promise<{ externalId: string }>;
  upsertCompany(a: { accountId: string; name: string; domain?: string; volumeBand?: string; syncVersion: number }): Promise<{ externalId: string }>;
  upsertDeal(o: { opportunityId: string; accountId: string; stage: string; amount?: Money; syncVersion: number }): Promise<{ externalId: string }>;
  deleteContact(leadId: string, reason: 'consent_withdrawn'|'erasure'|'suppressed'): Promise<void>;   // within 15 min of withdrawal
  pullChanges(since: Date): Promise<{ kind: 'contact'|'company'|'deal'; externalId: string; changedAt: Date; fields: Record<string, unknown> }[]>;
  verifier?: WebhookVerifier;
}
export interface AnalyticsPort {
  capture(e: { eventId: string; name: string; schemaVersion: string; distinctId: string; at: Date; props: Record<string, string|number|boolean>; consent: 'analytics'|'none' }): Promise<void>; // fire-and-forget; dropped when consent = 'none'
  identify?(distinctId: string, traits: Record<string, string>): Promise<void>;    // leads only; never respondents
  deleteSubject(distinctId: string): Promise<void>;                                  // DPDP erasure
}
```

| Attribute | `CRM_PORT` | `ANALYTICS_PORT` |
|---|---|---|
| Providers | Native mini-CRM (`growth.leads/accounts/opportunities`, source of truth) with sync adapters **HubSpot** or **Zoho** (tenant choice) | **PostHog self-hosted** in ap-south-1 (primary); **GA4** for acquisition only, consent-gated |
| Auth | HubSpot private-app token (Bearer); Zoho OAuth 2.0 (refresh token) — secrets in Secrets Manager | PostHog project API key (server-side); GA4 Measurement Protocol API secret |
| Data rules | Growth data only; schema validator rejects case identifiers, party names, pleadings and offers; served respondents are suppressed unless they gave separate marketing consent | Event taxonomy in `packages/domain/analytics` (P13 FR-P13-23); never loaded on `/app`, `/verify`, `/settlements-and-awards` or any case page; case-lifecycle events only as anonymous counts |
| Idempotency | `(lead_id, sync_version)`; `CrmSyncWorkflow` 5-minute incremental | `eventId` (UUID) de-duplicated by the provider/ingest |
| Failover | `none` — native CRM continues; sync queue retries | `auto`; events dropped, never block a page |
| Residency | HubSpot/Zoho data centres per contract; record the DPDP s.16 basis; growth data class `personal` only with a residency ADR | PostHog in India; GA4 receives no personal data (IP anonymised, no user IDs) |
| Webhooks | HubSpot `X-HubSpot-Signature-v3` / Zoho notification token — confirm at contracting | None |

## D.10 Contract-test and verification register

Status as verified on 20 Oct 2026 (research pack RES_A4).

| # | Item | Port | Status (Oct 2026) | Closure required before |
|---|---|---|---|---|
| V-D1 | ElevenLabs India residency covers Agents, transcripts, recordings, post-call data | VOICE | Residency is Enterprise-only; custom-LLM and post-call webhook traffic outside the guarantee (mitigated by India-hosted proxy/webhook); written confirmation still required | First production call |
| V-D2 | ElevenLabs endpoint paths, webhook signature format, custom-LLM (Bedrock) support | VOICE | Webhook signature and custom-LLM (OpenAI-compatible proxy) confirmed; endpoint paths and text-only test API open | P07 adapter merge |
| V-D3 | Exotel/MSG91/Gupshup webhook authentication options | TELEPHONY, MESSAGING | Open (design compensates with path token + Basic + IP allow-list) | P07 adapter merge |
| V-D4 | Equator-originated service calls (M-05): DLT PE registration, A2P declaration of CLI ranges, operator written confirmation of the permitted CLI type, telecom-counsel opinion, Third Amendment Gazette date; 1601 eligibility watch; lender 1600 authorisation format | TELEPHONY | Framework confirmed (TCCCPR Third Amendment 2026; PR 91/2026; PR 113/2026); no series designated for ODR/legal services — operator confirmation and counsel opinion open | `voice.equator_service_number.enabled` ON |
| V-D5 | WhatsApp error codes, Gupshup API generation, Meta data location | MESSAGING | Error codes and Local Storage (`IN`) confirmed; Gupshup API generation open | P07 exit |
| V-D6 | Leegality `mac` algorithm; per-state eStamp matrix (10 priority states) | ESIGN, ESTAMP | HMAC-SHA1 confirmed (encoding to test); state matrix open | P06 go-live per state |
| V-D7 | RazorpayX payout idempotency header; Route/Escrow+/Castler eligibility for ODR | PAYOUT, ESCROW | Header confirmed; escrow eligibility open | P05 go-live |
| V-D8 | IRP token lifetime and GSP contract | TAX_INVOICE | Token 6 h confirmed; GSP contract open | First B2B invoice |
| V-D9 | LiveKit participant-move API and region pinning for egress/agents | VIDEO | Region group `india` (Scale+) covers signalling and media; agents deployed separately; participant move open | P04 exit |
| V-D10 | Bedrock India profile coverage for all three Claude models and embeddings; Citations/caching on Bedrock | LLM | Models and in-Region embeddings confirmed; Citations/caching open | P11 exit |
| V-D11 | FBIL currency coverage (SGD, AED) | FX | Resolved: FBIL publishes USD, GBP, EUR, JPY only (13:00 IST); SGD/AED by configured cross-rate or AD bank TT rate | First INT invoice |
| V-D12 | Sanctions provider coverage incl. MHA UAPA list ingestion | SANCTIONS | Surepass AML API exists; list coverage open | First INT registration |
| V-D13 | ReBIT purpose code for dispute-resolution fetch; TSP terms for FIU-on-behalf processing | AA | 105 (or 103) per ReBIT list; TSP confirmation open | D6 pilot |
| V-D14 | India Post bulk API; ONDC IGM ODR onboarding; MSME ODR API; SMART ODR ODRI API | POSTAL, GOV | India Post by contract only; no MSME ODR or SMART ODR API; ONDC open | Respective flags ON |
| V-D15 | HubSpot/Zoho webhook signing and data-centre location; PostHog self-host sizing | CRM, ANALYTICS | Open | P13 exit |
