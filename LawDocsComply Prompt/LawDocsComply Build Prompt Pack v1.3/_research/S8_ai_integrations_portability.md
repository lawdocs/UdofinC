# S8 Research Notes — Vidhi AI, Integrations, Portability (as of 25 October 2026)

All facts dated; [VERIFY] = re-check before the dependent feature ships.

## 1. Infrabyx Ecosystem Integration Specification v1.1 (read on owner's Mac, 25 Oct 2026)
- §3.1 transports: HTTP push of CloudEvents as Standard Webhooks with RFC 9421 signatures; streaming (MSK/Redpanda) between Infrabyx products on AWS ap-south-1; every producer serves `GET /v1/events?after=&types=`; file fallback §3.11.
- §3.2 envelope: `id` UUIDv7; `source` `urn:infrabyx:ldc:[tenantid]`; **`type` = `in.infrabyx.[domain].[EventName].v[major]`** (conflicts with pack convention `in.lawdocscomply.<module>…` for ecosystem-facing events — resolution: ecosystem-facing events use `in.infrabyx.grc.*` / `in.infrabyx.risk.*` / `in.infrabyx.portability.*` etc.; LDC-internal events use `in.lawdocscomply.*`). Extension attributes `tenantid`, `reid`, `productfamily` (`na`), `correlationid`, `causationid`, `consentref`/`legalbasis`, `dataclass`, `schemaver`, `seq`, `traceparent`.
- §3.3 `infrabyx-contracts` repo, JSON Schema 2020-12, OpenAPI 3.1, AsyncAPI 3.0, BACKWARD compatibility, `contracts.lock`, Pact gates; paths `/v[major]/`, snake_case, cursor pagination limit ≤ 500, `updated_since`.
- §3.4 Standard Webhooks headers; HMAC-SHA256; ±5 min; at-least-once; retries 72 h then DLQ; Idempotency-Key (UUIDv7) stored ≥ 24 h; 422 on key reuse with different body, 409 while in progress.
- §3.5 transactional outbox/inbox; per-subject `seq`; gap parking 15 min; replay retention ≥ 90 days.
- §3.6 OAuth client credentials (OAuth 2.1 profile, RFC 9700), certificate-bound (RFC 8705) or private_key_jwt (RFC 7523), tokens ≤ 10 min; mTLS with Infrabyx PKI (≤ 397 days); RFC 9421 ed25519; documents by reference with detached JWS.
- §3.8 LDC availability target 99.5% monthly; outbox lag p95 ≤ 30 s; delivery p95 ≤ 5 min.
- §3.9 RFC 9457 problem details with codes incl. `dataclass-not-permitted`, `residency-blocked`, `channel-not-confirmed`, `grant-expired`, `entitlement-missing` (never raised for a regulated tenant's read/export of its own data).
- §4.5 scopes relevant to LDC: `grc.obligation:read`, `grc.evidence:write`, `privacy.request:write`, `risk.feed:write`, `grc.kri:read`, `external.workspace:read`, `external.grant:write`; Ops Hub provisioning ack, catalogue and claims gate only for LDC.
- §4.6 Ops Hub never holds tenant content; staff identity by SCIM from OH10; group grants ≤ 90 days.
- §4.7 external auditor/supervisor grants: RE authorises; `POST /v1/external-access/grants`; lifecycle; ≤ 90 days; read-only replica; masking; watermarked, capped exports; sessions end ≤ 60 s after expiry.
- §6.15 `grc` events: ObligationPublished (LDC → products), ControlTestResultPublished, EvidenceSubmitted, ComplianceIssueRaised, ReturnStatusUpdated, PolicyAttested, SecurityIncidentNotified.
- §6.22 risk feed: KriBreached, LossEventRecorded, CapitalRatioComputed (signed), LimitBreached (signed), StressTestCompleted, RiskSnapshotPublished; LDC serves `GET /v1/grc/kris?updated_since=` and `GET /v1/grc/obligations?updated_since=`; HMAC pseudonyms LDC cannot reverse; no raw PII; formula logic never accepted from LDC.
- §6.23 governance and workforce events tenant-internal; never to OH.
- §6.26 portability events ExportRequested, ExportCompleted (signed), StorageTargetConnected, BackupCompleted, RestoreTested; storage health failure → ControlTestResultPublished control `STORAGE_TARGET_HEALTH`; export/read never suspended for non-payment.
- §9.1 compliance modes EMBEDDED, LDC_EXTERNAL, LDC_GROUP, THIRD_PARTY_GRC, EXPORT_ONLY; switch never loses data.
- §9.2 generic GRC connector contract resources Obligation, Control, ControlTestResult, Evidence, Issue, Incident, RegulatoryReturn, PolicyAttestation, OutsourcingArrangement, KRI, RegulatoryChange; OSCAL mapping.
- §9.3 "LawDocsComply (Node, TypeScript, MongoDB) builds the connector in its own repository" — now superseded by D-01 (PostgreSQL); spec text must be updated in v1.2 [master note].
- §9.4 OSCAL v1.2.x JWS-signed package; adapters MetricStream, ServiceNow IRM, Archer, IBM OpenPages, Komrisk, Komply360, Compfie, TeamLease RegTech, Lawrbit, OnFinance.
- §10.1 connector SPI `@infrabyx/connector-sdk` (manifest, capabilities, healthCheck, send, receive, call, reconcile); §10.2 adapter catalogue (Tally XML port 9000; regulator portals PORTAL_MANUAL only — no credentials, OTPs, cookies, RPA or scraping; JioCX/Jio SIP as VoiceProvider; Razorpay only in OH8 and Udofin B2C billing [conflict with LDC billing — S9 owns]); §10.3 mapping packs YAML.
- §11.1 module.yaml, entitlement flags `mod.[id].[capability]`, lifecycle AVAILABLE→…→DETACHED; detaching never deletes regulated records.
- §12 formats; §12.1 archive standard 1.0 (folder `00 Start Here` mandatory; numbered top-level folders; naming rules: Windows-safe, NFC, path ≤ 240 chars, no personal data in names; CSV RFC 4180 UTF-8 BOM; XLSX "Read me" sheet; PDF/A-2b + DOCX; audit-events.jsonl monthly; manifest archive_manifest_v1 columns; detached JWS; verifier Apache-2.0; README PDF/DOCX/TXT; restricted folders as AES-256 ZIP with out-of-band password; veraPDF and headless LibreOffice render gates).
- §12.2 StorageTarget interface (describe, verifyResidency, testWrite, put, head, list, retentionInfo, healthCheck); provider table (S3 IAM role ExternalId; Azure workload identity; GCS WIF; SharePoint/OneDrive Graph `Sites.Selected`; Google Drive non-regulated only; SFTP ed25519; on-prem agent outbound mTLS); residency re-verified weekly; BYOK/HYOK; write-once retainUntil; daily canary; no promise after customer purges own store.
- §13.2 data classes PUBLIC, INTERNAL, CONFIDENTIAL, PII, SPI, FINANCIAL, LEGAL, HR, WELLNESS.
- §14 versioning; Deprecation (RFC 9745) and Sunset (RFC 8594) headers; certification suite groups.

## 2. AI
- **Viktor** (viktor.com): AI coworker in Slack, Microsoft Teams and (from Aug 2026) Discord; 3,200+ OAuth integrations; memory across channels; completes tasks on its own cloud computer; approval before sensitive actions on by default; credit-based pricing (Team $100/month for 40,000 credits); SOC 2 Type I; does not train on customer data (Lindy review, Aug 2026 — competitor source) [VERIFY on vendor site]. Pattern adopted: "AI employee" that is addressed in the team's channel, has a task queue, memory, scheduled prompts, connected tools, approval gates and credit metering.
- **NotebookLM** (DigitalOcean article 2026): sources (Drive, PDF, DOCX, TXT, CSV, audio, video, images with OCR, web research), source caps per plan (50–600 per notebook), citations to passages, Audio Overviews (deep dive/brief/critique/debate; interactive), Video Overviews, Mind Maps, Reports (briefing doc, study guide, custom), flashcards, quizzes, infographics, slide decks, data tables, Deep Research, sharing; enterprise data not used for training. Pattern adopted for "Vidhi Notebooks".
- **Claude API features page** (platform.claude.com, fetched 25 Oct 2026): GA — 1M context, adaptive thinking, batch (50% cost), citations, PDF support, search-result blocks, structured outputs, Files API (not ZDR-eligible), code execution, web fetch, web search, memory tool, Agent Skills (not ZDR), tool search, programmatic tool calling, prompt caching 5 m/1 h, token counting; Beta — MCP connector, compaction, context editing, server-side fallback, advisor tool. **`inference_geo` supports only `"global"` or `"us"`** on the first-party API → no India-only inference on Anthropic API.
- **Amazon Bedrock India geographic cross-Region inference** (AWS ML blog, 29 Sep 2026): Claude Opus 5, Claude Sonnet 5, Claude Haiku 4.5; requests route only between ap-south-1 and ap-south-2; customer data not stored in destination Region; Bedrock does not store inputs/outputs by default; CloudWatch/CloudTrail in source Region. Earlier (9 Mar 2026) Global CRIS from Mumbai/Hyderabad routed to any commercial Region. → **Default AI route for tenant data: Bedrock India geo profile.** [VERIFY model IDs and quotas at build].
- **Jio** (jio.com/business, fetched 25 Oct 2026): segments include AI + Machine Learning, Microsoft Azure through JioCloud, GPU computing, SIP Trunk (10–10,000 sessions), IP Centrex, Toll-Free, JioMeet (≤ 1,000 participants), **JioCX** (SMS, Email, Voice, RCS, WhatsApp, EasyPhone, Alerts, Verify), Marketing Solution, Security (CyberSOC, vCISO, DDoS, Threat & Vulnerability Management), JioAttendance; no public developer portal/API docs found. JioBrain = ML-as-a-service (network-centric). Jio Call Agent (announced 19 Jun 2026, RIL AGM; consumer, consent-based in-call assistant). Jio Haptik "AI for All" WhatsApp AI agents from ₹10,000 usage-based (UNI, 3 Sep [2025/2026 VERIFY]). Reliance Intelligence sovereign AI infra (Jamnagar, 120 MW by end-2026). → Jio is integrated as adapters: `VoiceProvider` (JioCX Voice/SIP), `MessagingProvider` (JioCX SMS/WhatsApp/RCS/Email), `ConversationalAgentProvider` (Haptik), `LlmProvider` (only when an enterprise API with India residency and no-training terms is contracted) [VERIFY all commercially].
- **WhatsApp Business Platform pricing** (Meta developer docs, fetched 25 Oct 2026): per-message pricing since 1 Jul 2025; categories marketing/utility/authentication (templates) and service; Meta Business Agent billed per token from 1 Jul 2026; 1,000 free service messages per number per month; from 1 Oct 2026 service messages beyond free tier and utility within window billable; INR billing must be migrated by 31 Dec 2026 (non-INR accounts stop delivering from 1 Jan 2027 for India sold-to). WhatsApp Business Messaging Policy bars debt collection (Ecosystem §4.4).
- **Bhashini** (MeitY National Language Translation Mission; ULCA): ASR, NMT, TTS, OCR for 22 scheduled languages [VERIFY API access terms for private entities].

## 3. Data and identity APIs
- **TallyPrime**: server mode HTTP listener default port 9000; XML Export/Import Data envelopes; ODBC on collections; **native JSON from TallyPrime 7.0** (headers `content-type`, `version: 1`, `tallyrequest: Export|Import`, `type: Data|Collection|Object|Function`, `id`, `svCurrentCompany` mandatory) (help.tallysolutions.com, fetched 25 Oct 2026). Current release banner: TallyPrime 7.2. No authentication on the listener → LDC uses an on-premises agent on the client LAN, never exposes port 9000 to the internet.
- **Company data**: MCA V3 portal has no public company-master API for private parties [VERIFY]; licensed aggregators: Probe42, Signzy, Surepass, Perfios (Karza), HyperVerge, Qorpiq (qorpiq.com developer docs) — CIN/LLPIN master, directors, charges, filings, financials. Scraping MCA is excluded.
- **DigiLocker**: Authorized Partner API Specification v1.11 (img1.digitallocker.gov.in) — OAuth 2.0 PKCE pull of issued documents with user consent; requester onboarding via DigiLocker partner portal / API Setu [VERIFY eligibility].
- **API Setu** (apisetu.gov.in): government API exchange (PAN verification, GSTN, etc.) for authorised entities [VERIFY].
- **Microsoft Graph**: `Sites.Selected` (application, and delegated since Feb 2024) limits an app to granted SharePoint sites; calendar via `/users/{id}/events`, subscriptions (change notifications), `Calendars.ReadWrite`.

## 4. Standards
Standard Webhooks (standardwebhooks.com); CloudEvents 1.0.2; OpenAPI 3.1; AsyncAPI 3.0; JSON Schema 2020-12; RFC 9457, 9421, 9530, 8705, 7523, 8693, 9126, 9449, 9745, 8594, 7643/7644 (SCIM), 5545 (iCalendar), 4791 (CalDAV), 6638 (CardDAV — not needed), OSCAL 1.2.x (NIST), PDF/A-2b (ISO 19005-2), OOXML ISO/IEC 29500, BagIt RFC 8493 (considered; archive standard is canonical).

## Sources
- Ecosystem Spec v1.1 (owner's folder `Finbyx and Udofin Prompts/Ecosystem/`), read 25 Oct 2026
- https://www.lindy.ai/blog/viktor-review (Aug 2026)
- https://www.digitalocean.com/resources/articles/what-is-notebooklm (2026)
- https://platform.claude.com/docs/en/build-with-claude/overview (fetched 25 Oct 2026)
- https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-expands-claude-model-availability-to-india-cross-region-inference/ (29 Sep 2026)
- https://aws.amazon.com/blogs/machine-learning/access-anthropic-claude-models-in-india-on-amazon-bedrock-with-global-cross-region-inference (9 Mar 2026)
- https://www.jio.com/business/ ; https://www.jio.com/business/services/voice-and-collaboration/ (fetched 25 Oct 2026)
- https://www.businesstoday.in/…/jio-call-agent…-2026-06-19
- https://www.bajajbroking.in/blog/jio-platforms-and-ai-products-strategy-and-growth-potential (16 Oct 2026)
- https://uniindia.com/~/jio-s-haptik-launches-whatsapp-ai-agents-at-starting-price-rs-10-000-for-smbs/…
- https://developers.facebook.com/docs/whatsapp/pricing (fetched 25 Oct 2026)
- https://help.tallysolutions.com/tallyprime-as-server/ ; https://help.tallysolutions.com/tally-prime-integration-using-json-1/
- https://img1.digitallocker.gov.in/assets/img/Digital%20Locker%20Authorized%20Partner%20API%20Specification%20v1.11.pdf
- https://api.apisetu.gov.in
- https://devblogs.microsoft.com/microsoft365dev/sharepoint-now-supports-delegated-sites-selected-authentication/ (9 Feb 2024)
- https://resources.probe42.in/ ; https://developers.qorpiq.com/docs/intro/
