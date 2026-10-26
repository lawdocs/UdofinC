# Appendix I — Integration Adapters and API Catalogue

**Status:** Binding. **Used by:** P19 (owner), P01 (identity and KYB ports), P04 (deposits, bulk intake transport), P05 (OCR and translation ports), P07/P08 (eSign, eStamp, workplace co-authoring), P09 (LLM port, MCP edge), P10 (postal dispatch), P11 (court data), P12 (trademark data), P13 (accounting, HRMS), P16 (directory, academy, meetings), P17 (billing), P18 (Operations Hub interface), P20 (storage), P21 (video embeds, claims gate), P22 (push), P23 (certification evidence).

**How to use.** This appendix is the single list of (1) every external port, its adapters, fallbacks, legality and verification status, and its kill switch; (2) the ecosystem connectors; (3) the public API resource surface by module; (4) the scope catalogue; (5) the tenant webhook event catalogue (`in.lawdocs.*`); (6) internal-to-ecosystem event mapping; (7) rate-limit tiers; (8) the error model; (9) LawDocs file layouts. **Precedence:** Ecosystem Integration Specification v1.1 (and, once merged, v1.2 per Appendix Y) for any cross-product contract (NN-24) → this appendix for ports, conventions, scopes, webhook catalogue and tiers → each phase file's §7.3 for module endpoint paths (the API catalogue in §I.5 is a representative partner-facing view; where it differs from a phase §7.3, the phase path is canonical and the difference is fixed in the contract registry, never implemented twice). An adapter marked **[VERIFY]** ships behind its kill switch set OFF (or advisory-only) until the fact is verified and logged in `docs/compliance/verification-log.md` (NN-38).

---

## I.1 Conventions (summary of P19 §4A)

| Item | Rule |
|---|---|
| Base URLs | `https://api.lawdocs.in/v1` (production), `https://api.sandbox.lawdocs.in/v1` (sandbox), `https://events.lawdocs.in` (ecosystem push, mTLS), `https://hooks.lawdocs.in/v1/<provider>` (vendor callbacks), mobile BFF `https://api.lawdocs.in/m/v1` (P22) |
| Formats | JSON (`application/json`), problems `application/problem+json` (RFC 9457), files by pre-signed upload/download URLs (India buckets, ≤ 15 minutes validity) |
| Naming | `snake_case` fields; `UPPER_SNAKE_CASE` enums with `x-extensible-enum`; prefixed ULIDs (`agr_`, `sgr_`, `doc_`…) as keys; business references (`LD-AGR-2026-000123`) as separate fields |
| Lists | Cursor pagination (`limit` ≤ 500, `cursor`, `next_cursor`), `updated_since`, `fields`, `expand` (depth ≤ 2) |
| Writes | `Idempotency-Key` (UUIDv7) on POST/PATCH/DELETE; ETag + `If-Match` on PATCH |
| Common sub-resources | `/history` (read-only audit), `/corrections` (correction entries, NN-02), `/comments`, `/attachments`, `/links`, `/shares`, `/export` (record-scope export, P20) |
| Ecosystem paths | Not module-prefixed (Spec §3.3); where the same operation is also offered to tenant clients under a module path, the gateway serves one implementation under both paths and the registry records the ecosystem path as canonical (Appendix Y §Y.8) |
| Versioning | Major in path; `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers; public majors ≥ 12 months parallel, ecosystem ≥ 90 days |
| Tracing | `traceparent`; `X-Correlation-Id` on every response |
| Payments | LawDocs holds no payment-gateway keys; all payment flows use `BILLING_PORT` to OH8 (Spec §6.27) |

---

## I.2 Port and adapter catalogue

Columns: **Port** (called by modules; never a vendor SDK) · **Purpose** · **Primary** → **Fallback** · **Data exchanged** · **Legality / terms** (research IDs) · **Status** (VERIFIED = verified in research on 25 Oct 2026; [VERIFY] = open point) · **Kill switch** (`int.adapter.<adapter_id>.enabled`; default shown). Every adapter implements `healthCheck()`, cost reporting where billable, residency attestation where it stores or processes tenant data, and idempotent calls (NN-46).

### I.2.1 Commerce and group services

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `BILLING_PORT` | Catalogue, quotes, orders and hosted checkout, invoices, entitlements, usage, disputes (P17) | OH8 → none (Delivery Console invoice request, P18) | Commercial records; usage aggregates only; B2C billing identity only after Appendix Y §Y.6 | Spec §6.27; Razorpay keys only in OH8; PA Directions 2025 via Razorpay Route (R3 LG-145) | VERIFIED (Spec); OH8 API readiness per OH O6 [VERIFY] | `oh8-billing` (ON) |
| `DIRECTORY_PORT` | Professional directory (Rule 36 fields) for marketplace (P16) | OH9 → none | Professional id, Rule 36 fields, status | BCI Rule 36; Madras HC 3 Jul 2024 (R3 LG-111, LG-113) | VERIFIED (Spec) | `oh9-directory` (ON; directory display OFF per D-05) |
| `CLAIMS_GATE_PORT` | Pre-publication check of claims (P21) | OH14 → block publication | Text or asset | NN-20; Spec §6.29 | VERIFIED (Spec) | `oh14-claims` (ON) |
| `CRM_REQUEST_PORT`, `SUPPORT_PORT` | Leads, contact-sales, tickets | OH3, OH5 → email to ops mailbox | Consented business contact; redacted ticket text | DPDP consent (R3 LG-063); Spec §6.29 | VERIFIED (Spec) | `oh3-crm`, `oh5-support` (ON) |

### I.2.2 Signing, stamping and execution

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `ESIGN_PORT` | Aadhaar OTP eSign (API 2.1), account-based eSign (API 3.x), signer consent evidence, signed PDF (PKCS7pdf/PAdES), audit trail (P08) | Leegality → Digio; later direct ASP with Protean or eMudhra (D-12; R6 §R6.6.6) | Final document hash (one per request), signer name/mobile/email, consent version, ESP response, certificate, signed PDF | IT Act s.3A, Second Schedule; First Schedule exclusions (R3 LG-001–LG-004); eSign API v2.1 consent `sc="Y"` (LG-006); ASP may not sublet (LG-007; NN-06); second ESP within one month under v3.3 (LG-008) [VERIFY: applicability to aggregator structures]; ESP licence expiries (LG-005): routing blocks any ESP whose CCA licence has lapsed or expired without recorded renewal evidence (X-16); `asp_mode` per vendor (aggregator as ASP or LawDocs' own ASP; X-15); never offered to another product as a provider — other products use the hosted hand-off (X-05; §I.4 `finbyx-signing-lawdocs`) | VERIFIED (ESP list, API terms); aggregator ASP structure [VERIFY] | `leegality-esign` (ON after contract), `digio-esign` (ON after contract) |
| `DSC_SIGN_PORT` | Class 3 DSC signing on USB token through a local PKCS#11 signer (company signatories, MCA-type use) | LawDocs desktop signer (signed installer) → vendor signer component | Hash only; certificate chain; signature | Class 2 discontinued (R3 LG-011) [VERIFY]; no named "DocSigner" instrument (LG-012) | [VERIFY] | `dsc-local` (OFF until certified) |
| `ESTAMP_PORT` | Procure e-stamp as the user's agent through authorised channels; attach; verify UIN; lock to document hash (P08) | Leegality BharatStamp → Surepass e-Stamping (SHCIL), Digio; physical/franked stamp upload with UIN check | State, article, consideration, duty, first party, stamp PDF, UIN, lock status | Stamp Act s.17, s.35; State Acts; SHCIL as CRA and ACCs; platform buys only as agent (R3 LG-096–LG-100; NN-08); duty pure agent (R6 D-25) | VERIFIED (vendor claims, coverage 16–31 States/UTs); per-State coverage and vendor rules [VERIFY] | `leegality-estamp` (ON per covered State), `surepass-estamp` (OFF until contract) |
| `ESTAMP_VERIFY` (part of `ESTAMP_PORT`) | Certificate verification | Vendor verification API → human verification by `OPS_*` staff on the public SHCIL verification page (no automation) | UIN, State | No scraping (NN-05) | [VERIFY: vendor verification API] | with `ESTAMP_PORT` |
| `NESL_DDE` (adapter of `ESTAMP_PORT`/`ESIGN_PORT`) | Financial-document execution for Enterprise RE tenants | Via aggregator (Leegality NeSL DDE add-on, emSigner) → standard eStamp + eSign | Document hash, parties, stamp | MoF notification 30 Jun 2020 (R3 LG-101) [VERIFY] | [VERIFY] | `nesl-dde` (OFF) |
| `POSTAL_DISPATCH_PORT` | Dispatch of legal notices with tracking evidence (P10) | India Post bulk API (CEPT onboarding) [VERIFY] → courier APIs; print-and-post by user | Addressee, address, tracking id, delivery events, proof image | Registered Post merged into Speed Post from 1 Sep 2025 (Spec §10.2); WhatsApp never used for legal notices | [VERIFY: India Post API access for LawDocs] | `indiapost-dispatch` (OFF) |
| `NOTARY_FACILITATION` (manual) | Appointment and wet-ink packs for affidavits, POAs | Manual partner network → user's own notary | Appointment metadata | Notaries Act 1952; no operational e-notarisation (R3 LG-106) [VERIFY] | Manual | n/a |

### I.2.3 Identity, KYB and onboarding (P01; partner onboarding P19 §4K)

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `DIGILOCKER_PORT` | Consented pull of issued documents (PAN, DL, RC, certificates) into vault; verification | NeGD direct, LawDocs as Requester → aggregator only with NeGD written approval | URI, metadata, verification result; copy only for a recorded user purpose | Requester ToU 2 Jun 2025: consent per access, no storage beyond purpose, 24-h NeGD breach report, annual CERT-In audit, no extension to affiliates without approval (R3 LG-037, LG-038; NN-42) | VERIFIED | `digilocker-direct` (ON after onboarding) |
| `ENTITY_LOCKER_PORT` | Company documents with authorised signatory's consent | NeGD Entity Locker → licensed MCA-data vendor + upload | Organisation documents, URIs | Entity Locker requester API (28 Nov 2024) (R3 LG-039) | [VERIFY: coverage, eligibility] | `entity-locker` (OFF) |
| `AADHAAR_OFFLINE_PORT` | Aadhaar App QR / e-Aadhaar verification now; Aadhaar Verifiable Credential after OVSE registration | UIDAI Aadhaar App → DigiLocker Aadhaar document; manual document with masking | UIDAI-signed attributes requested (name, 18+ flag, photo where needed), last 4 digits only | Aadhaar Act s.8A(4), s.29(4); Regulations 2021 as amended 2025 (Reg 13A OVSE); OVSE Playbook Jan 2026 (R3 LG-025–LG-030); NN-03, NN-04 | VERIFIED (secondary); OVSE registration route [VERIFY] | `aadhaar-app-qr` (ON), `aadhaar-avc` (OFF until OVSE) |
| `COMPANY_DATA_PORT` | CIN/LLPIN master data pre-fill | Probe42 or Signzy → Surepass; Perfios-Karza | Legal name, constitution, status, incorporation date, ROC, address, capital, directors with DIN (no PAN/DOB), charges summary, AGM/BS dates | No open MCA API; no scraping; vendor lawful-collection warranty and display rights (R3 LG-050; R6 D-15; CH-06) | Vendors VERIFIED to exist; contracts, pricing, display rights [VERIFY] | `probe42-company`, `signzy-company`, `surepass-company` (OFF until contract) |
| `GSTIN_PORT` | GSTIN search | GSP "Search Taxpayer" common API → second GSP | Legal/trade name, status, constitution, dates, jurisdiction, addresses | GSP contract; public taxpayer data; OTP consent for taxpayer APIs (R3 LG-049; R6 D-16) | VERIFIED | `gsp-gstin` (ON after contract) |
| `PAN_VERIFY_PORT` | PAN name match | DigiLocker PAN document + name match → KYC aggregator with written lawful-upstream warranty | Masked PAN + token; match result | Protean verification limited to eligible entities; LawDocs likely ineligible (R3 LG-047; R6 D-17; CH-04) | VERIFIED (Protean terms); aggregator lawfulness [VERIFY] | `pan-digilocker` (ON), `pan-aggregator` (OFF) |
| `LEI_PORT` | LEI lookup | GLEIF public API → none | LEI, legal name, status, parent relationships | Open data | VERIFIED (carried, LDC L.15) | `gleif-lei` (ON) |
| `UDYAM_PORT` | MSME registration check | Aggregator → certificate upload | Udyam number, enterprise type | [VERIFY] | [VERIFY] | `udyam-aggregator` (OFF) |
| `CONSENT_MANAGER_PORT` | Accept consent artefacts from DPDP consent managers | Registered consent managers → LawDocs consent ledger | Consent artefacts | DPDP s.6(7)–(9); Rule 4 from 13 Nov 2026 (R3 LG-070) | [VERIFY: registered managers and APIs] | `dpdp-consent-manager` (OFF) |
| Closed sources — **no adapter** | CKYC search/download; credit-bureau pulls; Aadhaar authentication/e-KYC; direct PAN database; Account Aggregator | — | — | PML Rules r.9 (LG-046); CICRA s.17(4), s.22 (LG-057, LG-058); Aadhaar Act s.4(4) (LG-022); NN-05 | Blocked by egress policy | n/a |

### I.2.4 Courts, tribunals and IP

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `COURT_DATA_PORT` | Case status, hearings, cause-list matches, orders for watch lists (P11) | Licensed aggregator A (e.g., eCourtsIndia API) → aggregator B (e.g., Surepass eCourts); `ManualCNR`; `eCourtsOfficialApi` only with an Enterprise institutional litigant's own e-Committee/High Court credentials | CNR, case number, parties (as published), stage, next date, order PDFs, "as of" | eCourts open APIs restricted to institutional litigants/government; no scraping or CAPTCHA bypass (R6 D-01; R3 LG-096A; NN-05); vendor contract: lawful collection, India residency, DPDP processor clauses, no resale (D-08); never "real-time" (NN-20) | Vendors VERIFIED (claims); platform eligibility for official API [VERIFY] | `ecourtsindia-court`, `surepass-court` (OFF until contract), `ecourts-official` (OFF) |
| `COURT_DATA_PORT` — tribunals | NCLT/NCLAT, DRT/DRAT, consumer commissions (e-Jagriti), ITAT, CESTAT, RERA | Aggregator where covered → manual matter type with reminders | As above | Public portals; no API found (R6 D-05–D-09) | [VERIFY: coverage per forum] | with court adapters |
| `TRADEMARK_DATA_PORT` | Application tracking, screening, status-change watch (P12) | `ManualAppNo` + WIPO Global Brand Database → licensed watch partner | Mark, owner, status, classes, dates, images | No IP India API; respect site terms; WIPO terms of reuse (R6 D-11, D-12); screening aid, not clearance | VERIFIED (no IP India API); WIPO terms [VERIFY] | `wipo-branddb` (OFF until terms checked) |
| `TM_JOURNAL_PORT` | Weekly Trade Marks Journal ingestion and similarity watch; 4-month opposition clock (Trade Marks Act s.21) | Licensed watch partner → PDF ingestion + OCR (AI credits) | Journal entries, advertised marks | Public documents (R6 D-13; R3 LG-170) | [VERIFY: journal format, partner] | `tm-journal-watch` (OFF) |
| Patents, designs, copyright, GI | Portfolio records | Manual entry and uploads | Application data entered by user | No API | Manual | n/a |
| `ODR_PORT` (`OdrProvider`, Spec §8.9) | Referral, status, consent, hearing, outcome (P19 §4I) | **No default provider.** The user (or the parties under their clause) chooses from configured providers shown in neutral order: Equator Resolution (Infrabyx group company — disclosed on every screen), Presolv360, Sama, Jupitice, CADRE, Webnyay and others, as API/WEBHOOK/FILE/PORTAL_MANUAL routes; Equator is one provider, never pre-selected or mandatory (master §2.1; Appendix Y §Y.7.4) | Referral pack by reference (ids, hashes, JWS), status, outcome document reference | A&C Act ss.7, 11, 12, 21, 29A, 33, 34; *Perkins Eastman*, *CORE* (Spec §8.2); Equator wall (Spec §4.6, §8.6) | Equator connector per EQ P09 [VERIFY endpoints]; others PORTAL_MANUAL | `equator-adr` (OFF until certified) |

### I.2.5 Workplace, storage and documents

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `WORKSPACE_PORT` | SSO/SCIM, Open in Word/Docs co-authoring with check-in, calendars, Teams/Meet links, export folders | Microsoft 365 (Graph, Entra ID) → Google Workspace (Admin SDK, Drive, Calendar) | Files (granted sites/drives only), calendar events, meeting links, directory entries | Least-privilege scopes: `Sites.Selected`, delegated `Calendars.ReadWrite`, `OnlineMeetings.ReadWrite` [VERIFY names]; Google `drive.file` preferred [VERIFY]; owner's M365 plan to confirm (CH-29) | M365 carried from LDC [VERIFY scopes]; Google [VERIFY] | `m365-graph` (ON after admin consent), `google-workspace` (OFF) |
| `MEETING_PORT` | Consultation and board-meeting links | Microsoft Teams → Google Meet; in-app WebRTC | Meeting link, attendance (where consented) | Recording off by default for advocate–client consultations (R4 §5.5) | VERIFIED (Teams via Graph); JioMeet rejected — no API (R4 J-16) | `teams-meetings` (ON), `google-meet` (OFF) |
| `STORAGE_PORT` (`StorageTarget`, Spec §12.2) | BYO export and backup targets (P20) | Customer S3 (cross-account role + ExternalId) → Azure Blob (India regions), GCS (asia-south1/2), SharePoint/OneDrive (`Sites.Selected`), Google shared drive (non-regulated classes only), SFTP, on-premises agent | Archives in `LD-EXPORT-1.0`, manifests, checksums | Residency per data class; Google Drive barred for regulated classes (`residency-blocked`); write-once where supported (Spec §12.2) | VERIFIED (Spec contract); per-provider property names [VERIFY] | per provider (OFF until tenant connects) |
| `OCR_PORT`, `TRANSLATE_PORT`, `INDIC_SPEECH_PORT` | Type copy, translation, speech (P05) | Tesseract/PaddleOCR + Claude vision on Bedrock India → Bhashini [VERIFY], Google/Azure (India regions); Sarvam [VERIFY]; Jio AI Cloud cognitive services [VERIFY] | Document pages, audio | Machine translations labelled (NN-48); India processing for confidential classes (NN-15) | Per P05 | per adapter (OFF until verified) |
| `LLM_PORT` | Vidhi model gateway (P09) | Claude on Amazon Bedrock India `in.` profile (confidential classes) → Anthropic API (public, non-personal content only) | Prompts and outputs after PII scrubber | NN-15; Anthropic Usage Policy high-risk legal use (R4 D-R4-09) [VERIFY effective date] | VERIFIED (Bedrock India announcement 29 Sep 2026, R4 D-R4-06); 5.5 models on `in.` [VERIFY] | per P09 |
| `VIDEO_EMBED_PORT` | Vlog and tutorials (P21) | YouTube privacy-enhanced embed behind a click-to-load facade → self-hosted captioned MP4 | Video id | Consent before load; captions (R6 D-32) [VERIFY cookie behaviour] | [VERIFY] | `youtube-embed` (ON with facade) |
| `PUSH_PORT` | Mobile push (P22) | Expo push → FCM/APNs direct | Notification titles without sensitive content (NN-44) | Store policies | VERIFIED (stack) | `expo-push` (ON) |
| `ACADEMY_PORT` | FinLegal Academy catalogue, deep links, SSO hand-off (P16) | Graphy feed/API [VERIFY] → curated catalogue import | Course metadata, URLs, enrolment hand-off | D-16; never copy paid content | [VERIFY] | `graphy-academy` (OFF until verified) |

### I.2.6 Messaging and voice (P19 FR-P19-67; `packages/notify`)

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `EMAIL_PORT` | Transactional email (invitations, signing links, receipts, alerts) | Amazon SES ap-south-1 → Brevo transactional; JioCX Email | Recipient, template, links | DKIM/SPF/DMARC per sender domain; marketing email is OH3's (Spec §10.2) | SES VERIFIED (stack); Brevo limits VERIFIED (R6 D-30); JioCX terms [VERIFY] | `ses-email` (ON), `brevo-transactional` (OFF), `jiocx-email` (OFF) |
| `SMS_PORT` | OTP fallback, signing and payment links, deadline alerts | DLT-registered aggregator → JioCX SMS | Mobile, DLT template id, variables | TCCCPR 2018 as amended 2025 and 2026; headers -T/-S/-P; whitelisted URLs only (R4 §5.1–§5.3; R3 LG-149) | JioCX docs VERIFIED (behind sign-up); contracts [VERIFY] | `dlt-sms-primary` (ON after DLT), `jiocx-sms` (OFF) |
| `RCS_PORT` | Verified-sender signing-link cards (Android and iPhone), payment cards | JioCX RCS → SMS | Template, card, DLR, read receipts | Brand verification; template approval (R4 J-03, D-R4-04) | VERIFIED (pricing V2) | `jiocx-rcs` (OFF until DLR + DLT tests pass) |
| `WHATSAPP_PORT` | Opt-in utility messages (signing status, document ready, receipts); Vidhi chat (opt-in) | Meta Cloud API direct → JioCX WhatsApp (BSP) | Opted-in number, template, variables | Per-message pricing since 1 Jul 2025; utility charges inside service window from 1 Oct 2026; INR billing — non-INR accounts stop from 1 Jan 2027 (R6 D-31); never legal notices or debt recovery (Spec §4.4, §10.2) | VERIFIED (Meta docs); JioCX BSP status [VERIFY] | `meta-whatsapp` (OFF until templates approved), `jiocx-whatsapp` (OFF) |
| `VOICE_PORT` | Click-to-call with masked numbers, IVR helpline, missed-call callback | CPaaS default (e.g., Exotel) [VERIFY] → JioCX Voice | Numbers (masked), flow id, call events, consented recordings | A2P declaration of CLIs before automated calls (Third Amendment 2026 Reg. 4) [VERIFY commencement]; 140-series promotional, 1600-series for regulated-entity service calls; recording notice; calling windows (R4 §5.2–§5.5) | JioCX VERIFIED (product docs) | `cpaas-voice` (OFF), `jiocx-voice` (OFF) |
| `TELEPHONY_PORT` | PSTN carriage | CPaaS SIP → Jio SIP Trunk (second carrier) | SIP sessions | CAF/MSA | VERIFIED (product) | `jio-sip` (OFF) |
| `CALLER_ID_PORT` | Branded caller ID on nudge and callback calls | Truecaller for Business [VERIFY] → JioCX Verify (pilot) | Brand profile | Pilot criteria (R4 §3.2) | VERIFIED (product); non-Jio coverage [VERIFY] | `jiocx-verify` (OFF) |
| `VOICE_AGENT_PORT` | Multilingual legal-intake voice line (general information only) | Pack default (voice agent + Claude via Bedrock proxy) [VERIFY] → Jio Haptik (RFP) | Call audio and transcript (India storage) | AI-voice is synthetic content: disclosure and labelling (R3 LG-078); human hand-off; Anthropic AUP legal high-risk (R4 §6.4); no vendor LLM sees case content | Haptik residency/DPA [VERIFY] (R4 D-R4-11) | `voice-agent` (OFF), `haptik-voice` (OFF) |

### I.2.7 Customer business systems

| Port | Purpose | Primary → Fallback | Data exchanged | Legality / terms | Status | Kill switch (default) |
|---|---|---|---|---|---|---|
| `ACCOUNTING_PORT` | Legal-spend and contract-value reconciliation (P13 `lgo`) | TallyPrime via on-premises agent (XML; native JSON on TallyPrime 7.0+ [VERIFY]) → Zoho Books (OAuth, India DC); CSV | Vendor masters, ledger postings for legal vendors; approved voucher push after maker-checker | Spec §12 Tally XML; CA13 audit-trail duties stay with the customer's books | [VERIFY versions] | `tally-agent`, `zoho-books` (OFF) |
| `HRMS_SOURCE_PORT` | Joiner/leaver triggers for appointment letters, NDAs; deactivate approvals | Generic SCIM/CSV → Darwinbox, Keka, Zoho People, SAP SuccessFactors adapters [VERIFY APIs]; LDC when HRMS SoR | Minimal people fields (name, work email, department, position, manager, status) | No salary, leave, health or identity data (Spec §6.23 rule 3; NN-33) | [VERIFY] | `hrms-generic` (ON), vendor adapters (OFF) |
| `CUSTOMER_CRM_PORT` | "Deal won" → contract request; agreement status back | Salesforce, HubSpot, Zoho CRM adapters [VERIFY APIs] → webhooks + CSV | Counterparty organisation, commercial fields, status, executed date | Customer's own CRM; never Infrabyx CRM (OH3) | [VERIFY] | per vendor (OFF) |
| Automation platforms | Triggers and safe actions (P19 §4M) | Zapier, Make → Power Automate custom connector; generic inbound hook | Thin events (`INTERNAL`); action inputs | Platform terms and residency; transfer register (NN-25) [VERIFY] | [VERIFY partner terms] | `zapier`, `make`, `power-automate` (OFF until listed) |

---

## I.3 Adapter interface essentials

All adapters extend the SDK `Connector` (Spec §10.1). Representative port signatures (TypeScript, `packages/connectors`):

```ts
interface EsignPort {
  createRequest(ctx: TenantContext, req: {
    documentSha256: string; documentRef: string;            // final, stamped PDF only
    signers: { ref: string; name: string; mobile?: string; email?: string; order: number;
               method: 'AADHAAR_OTP' | 'ACCOUNT_ESIGN' | 'DSC' | 'E_ACCEPTANCE_OTP' }[];
    consentVersion: string; callbackUrl: string; eligibilityRef: string;   // Appendix F result
  }, idemKey: string): Promise<{ providerRequestId: string; signingUrls: Record<string,string> }>;
  status(ctx: TenantContext, providerRequestId: string): Promise<EsignStatus>;
  fetchSigned(ctx: TenantContext, providerRequestId: string): Promise<{ pdfRef: string; sha256: string; certificate: string; espTxnId: string; auditTrailRef: string }>;
  cancel(ctx: TenantContext, providerRequestId: string, idemKey: string): Promise<void>;
  receive(raw: InboundMessage): Promise<CloudEvent[]>;      // vendor webhook → internal events
}

interface EstampPort {
  quote(ctx: TenantContext, q: { state: string; article: string; consideration?: Money }): Promise<{ duty: Money; facilitationFee: Money; channel: 'SHCIL'|'STATE_PORTAL'|'GRAS'|'FRANKING'|'PHYSICAL' }>;
  procure(ctx: TenantContext, o: { quoteId: string; firstParty: PartyRef; secondParty?: PartyRef }, idemKey: string): Promise<{ orderId: string }>;
  verify(ctx: TenantContext, uin: string, state: string): Promise<{ valid: boolean; lockStatus?: string; source: 'VENDOR_API'|'HUMAN_CHECK' }>;
}

interface CourtDataPort {
  addWatch(ctx: TenantContext, k: { cnr?: string; forum: string; caseNo?: string; year?: number }): Promise<{ watchId: string }>;
  refresh(ctx: TenantContext, watchId: string, idemKey: string): Promise<{ asOf: string; stage?: string; nextDate?: string; orders: { date: string; ref: string }[] }>;
  coverage(): Promise<{ forum: string; supported: boolean }[]>;
}

interface CompanyDataPort {
  lookup(ctx: TenantContext, k: { cin?: string; llpin?: string; name?: string }, consentRef: string): Promise<{ fields: Record<string, { value: unknown; source: string; fetchedAt: string }> }>;
}
```

Rules: every method takes `TenantContext` (no tenant, no call); vendor errors are normalised to `LD-INT-082` with a vendor code extension (no personal data); costs per call are reported to `bil` meters; signing URLs are LawDocs URLs (`sign.lawdocs.in`) that wrap the vendor session — vendor URLs are never handed to a third-party client (NN-06).

---

## I.4 Ecosystem connector catalogue

Connector ids follow Spec §11.4 (`[counterparty]-[capability]-[product]`). "v1.1" = runs on current contracts; "v1.2" = needs Appendix Y and stays inert behind `int.eco.v12_contracts.enabled` (manual interim channel meanwhile).

| Connector id | Direction | Contracts | Link kind | Contract version |
|---|---|---|---|---|
| `oh-provisioning-lawdocs` | OH → LD; LD → OH | `TenantProvisioned` (consume); `PUT /v1/provisioning-requests/{id}`; serve `GET /v1/tenants/{tenantid}/provisioning-status`; `TenantRegistered` (produce) | `OH_PROVISIONING` | v1.1 (consume, ack); v1.2 (`TenantRegistered`, LD as product value) |
| `oh-billing-lawdocs` | Both | Catalogue, quotes, orders, invoices, usage disputes (LD → OH APIs); `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPayment*`, `SubscriptionCancelled` (consume); `UsageRecorded`, `ModuleAttached/Detached` (produce); serve `GET /v1/entitlements` | `OH_PROVISIONING` | v1.1 for the API set once LD scopes are added (Appendix Y §Y.9); order line-item fields, `buyer_billing_identity` (`CONTRACT_PERFORMANCE_CUSTOMER`, X-13), `MarketplaceTransferInstructed`, `MarketplacePayoutSettled` and `ServiceCreditIssued` v1.2 |
| `oh-ops-lawdocs` | Both | CRM requests, support tickets, `SupportTicket*`, `ImplementationMilestoneReached`, `ProfessionalEmpanelled/Suspended`, claims gate, `ReleasePublished`, `ControlEvidenceCollected`, `AccessReviewCompleted` (PLATFORM), SCIM from OH10 | `OH_PROVISIONING`, `GROUP_GRANT_REF` | v1.1; v1.2: `MatterAllocated` from LD, `POST /v1/client-conflicts/check`, `TenantSelfServeCreated`, `ClientHealthSignal`, `SurveyResponseRecorded`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `ContentPublished`, `GrievanceStatusChanged`, `EmployeeOffboarded` (consume), CRM leads/activities and asset-library calls (Appendix Y §Y.7.10, §Y.8) |
| `ldc-sor-lawdocs` | Both | Kernel export/import layouts; `SystemOfRecordSwitched`; governance read APIs; `ResolutionPassed`, `KmpChanged` under `LDC_SOR` | `LDC_SOR` | v1.2 |
| `ldc-legal-lawdocs` | LD ↔ LDC | `legal` domain events; `GET /v1/legal-matters`, `GET /v1/contract-obligations`; template packs; `DocumentShared`; `ops.ServiceOrderRouted` (LD → LDC) and `ops.ServiceOrderStatusChanged` (both ways) for storefront orders; token-exchange launch for same-organisation customers (Appendix Y §Y.3.6) | `LDC_PROJECTION` | v1.2 (`DocumentShared` v1.1) |
| `finbyx-legal-lawdocs` | Both | Template packs (LD → FX pull); `DocumentShared` to a recovery case; `litigation.*` (FX → LD consume) | `FINBYX_LEGAL` | v1.2 (consumer and scope additions); `DocumentShared` v1.1 |
| `finbyx-signing-lawdocs` | FX → LD → FX | Hosted hand-off only (X-05): `POST /v1/signing-requests` creates a LawDocs-hosted ceremony in the RE's own LawDocs tenant; no signing URLs, ESP credentials or consent logs go to Finbyx; `SigningRequestCompleted` etc. back with evidence by reference | `FINBYX_SIGNING_HANDOFF` | v1.2 |
| `udofin-deposit-lawdocs` | UD → LD | `POST /v1/document-deposits`; `GET /v1/documents/{id}` at UD; `DocumentDeposited` back | `UDOFIN_DEPOSIT` (per individual) | v1.2 |
| `equator-adr-lawdocs` | Both | One of several `ODR_PORT` connectors (no default provider); `POST /v1/adr/referrals` at EQ; `ADRCaseStatusChanged`, `ADRHearingScheduled`, `ADRNeutralAppointed`, `ADROutcomeRecorded` (party view); `GET /v1/documents/{id}` both ways; model-clause pack | `EQUATOR_PARTY` | v1.2 (LD as referrer and party consumer) |

No connector exists between `chp` (Consumer Help) and any ecosystem product (NN-23).

---

## I.5 Public API resource catalogue (representative; phase §7.3 canonical)

Scopes per §I.6. "(E)" marks ecosystem-facing endpoints that follow the Spec. Modules with **no external API**: `cvl` (credential vault — never exposed to any machine client, connector or agent; NN-16), `chp` (Consumer Help — own apps only; no partner or ecosystem client), `eng`, `mob` (BFF only).

| Module | Resources | Key endpoints | Scopes |
|---|---|---|---|
| `core` | tenant, legal entities, audit, corrections | `GET /v1/core/tenant`, `GET /v1/core/entities`, `GET /v1/core/audit-events?updated_since=`, `POST /v1/core/corrections` | `core.tenant:read`, `core.audit:read`, `core.correction:write` |
| `iam` / `org` | users, invitations, roles, departments, positions, delegations, SCIM | `GET/POST /v1/iam/users`, `POST /v1/iam/invitations`, `GET /v1/org/departments`, `/scim/v2/Users`, `/scim/v2/Groups` | `iam.user:read`, `iam.user:write`, `org.structure:read`, SCIM bearer |
| `kyc` | verifications, consent artefacts, onboarding lookups | `POST /v1/kyc/lookups` (company/GSTIN/LEI), `GET /v1/kyc/verifications/{id}`, `GET /v1/kyc/consents` | `kyc.lookup:create`, `kyc.consent:read` |
| `dms` | folders, documents, versions, renditions, shares, legal holds, bulk imports, deposits | `GET/POST /v1/dms/folders`, `POST /v1/dms/documents` (pre-signed upload), `GET /v1/dms/documents/{id}`, `GET /v1/dms/documents/{id}/versions`, `GET /v1/dms/documents/{id}/renditions`, `POST /v1/dms/documents/{id}/shares`, `POST /v1/dms/imports` (folder manifest), `POST /v1/document-deposits` (E, v1.2) | `dms.document:read`, `dms.document:write`, `dms.share:create`, `dms.import:create`, `documents.deposit:write` |
| `dix` | OCR jobs, type copies, translations | `POST /v1/dix/jobs`, `GET /v1/dix/jobs/{id}`, `GET /v1/dix/renditions/{id}` | `dix.job:create`, `dix.rendition:read` |
| `tpl` / `drf` | templates, clauses, questionnaires, template packs, drafts | `GET /v1/tpl/templates`, `GET /v1/tpl/templates/{id}/questionnaire`, `POST /v1/drf/drafts` (template assembly from answers), `GET /v1/template-packs/{pack}/versions/{v}` (E) | `tpl.template:read`, `drf.draft:create`, `templates.pack:read` |
| `clm` | contract requests, agreements, negotiation rounds, approvals, obligations, renewals | `POST /v1/clm/requests`, `GET /v1/clm/agreements?status=&updated_since=`, `GET /v1/clm/agreements/{id}`, `GET /v1/clm/agreements/{id}/rounds`, `GET /v1/clm/obligations?due_before=`, `GET /v1/contract-obligations` (E, v1.2) | `clm.request:create`, `clm.agreement:read`, `clm.obligation:read`, `legal.obligation:read` |
| `sgn` | signing requests, signers, stamp instruments, evidence packs | `POST /v1/sgn/signing-requests` (E alias `/v1/signing-requests`), `GET /v1/sgn/signing-requests/{id}`, `POST /v1/sgn/signing-requests/{id}/withdrawal`, `GET /v1/sgn/signing-requests/{id}/evidence-pack`, `POST /v1/sgn/stamp-instruments` (attach), `GET /v1/sgn/stamp-instruments/{id}` | `esign.request:create` (step-up), `esign.request:read`, `sgn.stamp:write`, `sgn.evidence:read` |
| `pld` | notices, pleadings drafts | `POST /v1/pld/drafts`, `GET /v1/pld/notices/{id}`, `GET /v1/pld/notices/{id}/dispatch` | `pld.draft:create`, `pld.notice:read` |
| `lit` | matters, court cases, hearings, orders, watch lists | `GET/POST /v1/lit/matters`, `GET /v1/lit/cases?next_date_before=`, `POST /v1/lit/cases` (by CNR/case no.), `GET /v1/lit/cases/{id}/hearings`, `GET /v1/lit/cases/{id}/orders`, `GET /v1/legal-matters` (E, v1.2) | `lit.matter:read`, `lit.matter:write`, `legal.matter:read` |
| `ipm` | IP assets, deadlines, watch results | `GET/POST /v1/ipm/assets`, `GET /v1/ipm/assets/{id}/deadlines`, `GET /v1/ipm/watch-results` | `ipm.asset:read`, `ipm.asset:write` |
| `gov` / `hr` (local kernel mode) | meetings, resolutions, registers, KMP; people (minimal) | `GET /v1/gov/meetings`, `GET /v1/gov/resolutions`, `GET /v1/hr/people?fields=minimal` | `gov.meeting:read`, `gov.resolution:read`, `hr.employee:read.minimal` |
| `lgo` | legal intake requests, legal calendar, legal spend | `POST /v1/lgo/intake-requests`, `GET /v1/lgo/calendar`, `GET /v1/lgo/spend?period=` | `lgo.intake:create`, `lgo.calendar:read`, `lgo.spend:read` |
| `wf` | tasks, approvals, open/interim/waiting items | `GET /v1/wf/tasks?assignee=me`, `POST /v1/wf/tasks`, `GET /v1/wf/items?state=WAITING` | `wf.task:read`, `wf.task:write` |
| `mkp` | catalogue (public), engagements, retainers, deliverables | `GET /v1/public/marketplace/services` (no auth), `GET /v1/mkp/engagements`, `GET /v1/mkp/engagements/{id}/deliverables`, `GET /v1/mkp/retainers/{id}` | public; `mkp.engagement:read` |
| `bil` / `sav` | entitlements mirror, invoices mirror, usage, savings | `GET /v1/bil/entitlements`, `GET /v1/bil/invoices`, `GET /v1/bil/usage?period=`, `GET /v1/sav/summary?period=` | `bil.read`, `sav.read` |
| `sdc` | delivery grants (client view) | `GET /v1/sdc/delivery-grants`, `POST /v1/sdc/delivery-grants/{id}/revocation` | `sdc.grant:read`, `sdc.grant:revoke` |
| `xpt` | export jobs, storage targets, export map | `POST /v1/xpt/exports`, `GET /v1/xpt/exports/{id}`, `GET /v1/xpt/export-map` | `xpt.export:create` (step-up for full tenant), `xpt.export:read` |
| `int` | webhooks, clients, ledger, links, partner onboarding, health, events | `/v1/int/webhook-subscriptions`, `/v1/int/clients`, `GET /v1/int/sharing-ledger`, `/v1/int/links`, `/v1/int/partner/onboarding-batches`, `GET /v1/int/health`, `GET /v1/events` (E) | `int.webhook:manage`, `int.client:manage`, `int.ledger:read`, `int.link:manage`, `partner.onboarding:write`, `int.health:read` |
| `hlp` / `web` (public) | glossary, help articles, tutorials | `GET /v1/public/glossary/{key}`, `GET /v1/public/help/articles` | public |

---

## I.6 Scope catalogue (tenant, partner and public)

Ecosystem scopes are listed in Appendix Y §Y.9. "Max class" is the highest data class a response can contain; fields above a client's `data_class_max` are omitted (P19 FR-P19-10).

| Scope | Max class | Typical grantees | Grant rule |
|---|---|---|---|
| `core.tenant:read`, `org.structure:read` | INTERNAL | All tenant clients | ORG_ADMIN |
| `core.audit:read` | CONFIDENTIAL (masked PII) | Tenant SIEM, auditors | ORG_OWNER |
| `iam.user:read` / `:write` | PII (business contact) | HR/IdP integrations | ORG_ADMIN |
| `kyc.lookup:create` | PII | Partner onboarding, tenant onboarding tools | ORG_ADMIN; partners by agreement |
| `dms.document:read` | Up to LEGAL (per document class and privilege) | Approved integrations only | ORG_ADMIN + ORG_CLO for LEGAL |
| `dms.document:write`, `dms.import:create` | — | ERP/DMS migrations, scanners | ORG_ADMIN |
| `dms.share:create` | — | Never to automation platforms | ORG_OWNER |
| `tpl.template:read`, `drf.draft:create` | INTERNAL / CONFIDENTIAL | HR, CRM, lender platforms (template assembly API — R6 `API_AGREEMENT_GENERATE`) | ORG_ADMIN |
| `clm.request:create`, `clm.agreement:read`, `clm.obligation:read` | CONFIDENTIAL | Customer CRM, ERP | ORG_ADMIN |
| `esign.request:create` | — | Customer systems creating LawDocs-hosted ceremonies in their own tenant | ORG_ADMIN with step-up; `int.esign.api_initiation.enabled` |
| `esign.request:read`, `sgn.evidence:read` | CONFIDENTIAL | Same | ORG_ADMIN |
| `lit.matter:read` / `:write`, `ipm.asset:read` / `:write` | LEGAL | Corporate legal tools, law-firm systems | ORG_CLO |
| `gov.*:read` | CONFIDENTIAL | Board portals | ORG_OWNER |
| `hr.employee:read.minimal` | PII | Task and approval routing | ORG_ADMIN |
| `wf.task:read` / `:write`, `lgo.intake:create` | INTERNAL | Intranets, Teams apps | ORG_ADMIN |
| `mkp.engagement:read` | CONFIDENTIAL | Procurement systems | ORG_ADMIN |
| `bil.read`, `sav.read` | INTERNAL | Finance systems | ORG_ADMIN |
| `xpt.export:create` | Per scope | Admin automations (step-up for full tenant; maker-checker for tenant exports — NN-18) | ORG_OWNER |
| `int.webhook:manage`, `int.client:manage`, `int.link:manage` | INTERNAL | Admin tooling | ORG_ADMIN |
| `int.ledger:read` | INTERNAL | DPO tools, auditors | ORG_OWNER |
| `partner.onboarding:write` / `:read` | PII (signatory contacts) | Partners under agreement | PLT_SUPER_ADMIN at partner registration |
| `automation.trigger:read`, `automation.action:write` | INTERNAL (default) | Zapier, Make, Power Automate | ORG_ADMIN; ceiling raise by ORG_OWNER |
| Never granted to any external client | — | Credential vault (`cvl`), Consumer Help (`chp`), agent autonomy, role elevation, payment refunds, deletion of records, signing on a user's behalf | — |

---

## I.7 Tenant webhook event catalogue (`in.lawdocs.*`)

Thin events: `data` carries ids, business references, status, dates and counts only; class `INTERNAL` unless the subscription is raised to `PII` (never `LEGAL`). **The producing phase's §7.4 is canonical**; the "Event type" column below uses those names (re-keyed per Appendix B §B.4.3 in this release). The "Former name" column lists the name an earlier draft of this appendix used; the gateway accepts a subscription to a former name for one major version and maps it to the canonical type (subscription response carries `Deprecation` and the canonical type), and never emits the former name. Subscribable by Company tenants (Pro and above per plan) and practitioner workspaces; individuals use in-app notifications instead. Consumer Help (`chp`) events are never subscribable (NN-23).

| Event type (canonical) | Module | Trigger | `data` (thin) | Former name |
|---|---|---|---|---|
| `in.lawdocs.dms.DocumentUploaded.v1` | dms | Original stored (hash computed) | document_id, folder_id, sha256, origin | — |
| `in.lawdocs.dms.IntakeJobCommitted.v1` | dms | Folder intake job committed (A.21) | import_id, counts (accepted, rejected, duplicates) | `dms.BulkImportCompleted` |
| `in.lawdocs.dms.ShareCreated.v1` | dms | Share created | document_id, share_id, audience type, expiry | `dms.DocumentShared` |
| `in.lawdocs.dms.ShareRevoked.v1` | dms | Share revoked | share_id | — |
| `in.lawdocs.dms.LegalHoldPlaced.v1` / `…LegalHoldReleased.v1` | dms | Hold applied / released | hold_id, scope | `dms.LegalHoldChanged` |
| `in.lawdocs.dms.DocumentDeposited.v1` | dms | Deposit from a connected app stored (A.58) | document_id, link_id, source product | — |
| `in.lawdocs.dix.TypeCopyGenerated.v1` | dix | Typed copy produced | rendition_id, document_id, confidence band | `dix.TypeCopyReady` |
| `in.lawdocs.dix.TranslationGenerated.v1` | dix | Machine translation produced (labelled, NN-48) | rendition_id, language pair | `dix.TranslationReady` |
| `in.lawdocs.drf.DraftStarted.v1` | drf | Draft created from template or Vidhi | draft_id, template_id, label (TEMPLATE / AI_DRAFT) | `drf.DraftCreated` |
| `in.lawdocs.clm.IntakeRequestSubmitted.v1` | clm | Contract intake request | request_id, type, department | `clm.ContractRequestCreated` |
| `in.lawdocs.clm.VersionShared.v1` | clm | Round version shared with counterparty | agreement_id, round_no | `clm.NegotiationRoundShared` |
| `in.lawdocs.clm.ApprovalDecided.v1` | clm | Approval step decided (last step = internal approvals complete) | agreement_id, approval_ref, final (bool) | `clm.AgreementApproved` |
| `in.lawdocs.clm.AgreementExecuted.v1` | clm | Formalities gate passed (NN-40) | agreement_id, ld_ref, executed_at | — |
| `in.lawdocs.clm.ObligationOverdue.v1` | clm | Obligation past due (lead-time reminders use `KeyDateApproaching`) | obligation_id, agreement_id, due_date | `clm.ObligationDue` |
| `in.lawdocs.clm.KeyDateApproaching.v1` | clm | Renewal, expiry, notice or obligation lead time | agreement_id, key-date type, date | `clm.RenewalDue` |
| `in.lawdocs.sgn.SigningRequestSent.v1` | sgn | Invitations issued | signing_request_id, signer count | — |
| `in.lawdocs.sgn.SignatureApplied.v1` | sgn | One signer completed | signing_request_id, signer_ref, method | `sgn.SignerSigned` |
| `in.lawdocs.sgn.SigningCompleted.v1` | sgn | All signatures applied | signing_request_id, document_id, sha256 | — |
| `in.lawdocs.sgn.SignerDeclined.v1` | sgn | A signer declined | signing_request_id, signer_ref | `sgn.SigningDeclined` |
| `in.lawdocs.sgn.SigningRequestExpired.v1` | sgn | Deadline passed | signing_request_id | `sgn.SigningExpired` |
| `in.lawdocs.sgn.StampVerified.v1` | sgn | Stamp certificate attached and UIN verified | stamp_id, state, verified (bool) | `sgn.StampAttached` |
| `in.lawdocs.sgn.EvidencePackSealed.v1` | sgn | Evidence pack and s.63(4) draft generated | evidence_pack_id, document_id | `sgn.EvidencePackReady` |
| `in.lawdocs.pld.NoticeDispatched.v1` | pld | Notice sent through a dispatch channel | notice_id, channel, tracking ref | — |
| `in.lawdocs.pld.NoticeDelivered.v1` | pld | Delivery tracking event | notice_id, status, event time | `pld.NoticeDeliveryUpdated` |
| `in.lawdocs.lit.MatterOpened.v1` | lit | Matter created | matter_id, ld_ref, type | — |
| `in.lawdocs.lit.CaseStatusChanged.v1` | lit | Stage or status change (any source) | case_id, stage, source, as_of | — |
| `in.lawdocs.lit.HearingScheduled.v1` | lit | Next date recorded | case_id, hearing_id, date | — |
| `in.lawdocs.lit.OrderUploaded.v1` | lit | Order added | case_id, order_id, date | — |
| `in.lawdocs.ipm.StatusChanged.v1` | ipm | Trademark/IP status change | asset_id, status, source, as_of | — |
| `in.lawdocs.ipm.RenewalWindowOpened.v1` | ipm | Renewal lead time (opposition and response deadlines run on `lit.clocks` with subject type `IPM_ASSET` and alert through `lit.ClockDueSoon`, not subscribable) | asset_id, deadline type, date | `ipm.DeadlineApproaching` |
| `in.lawdocs.lgo.RequestSubmitted.v1` | lgo | Business user raised a legal request | request_id, category, department | `lgo.IntakeRequestCreated` |
| `in.lawdocs.wf.TaskAssigned.v1` | wf | Task assigned (R-A-08) | task_id, assignee_ref, due | — |
| `in.lawdocs.wf.ApprovalRequested.v1` | wf | Approval needed | approval_id, object ref | — |
| `in.lawdocs.wf.ApprovalDecided.v1` | wf | Approved/rejected | approval_id, decision | — |
| `in.lawdocs.wf.ItemOpened.v1` … `ItemWaived.v1` (`wf.Item*`) | wf | Open, interim or waiting item changed (A.15) | itm_id, type, parent ref, party type | — |
| `in.lawdocs.cfg.KillSwitchEngaged.v1` / `…KillSwitchReleased.v1` | cfg | Tenant-scope kill switch changed (R-A-09) | scope, target | — |
| `in.lawdocs.mkp.EngagementContracted.v1` | mkp | Engagement started | engagement_id, service_id | `mkp.EngagementCreated` |
| `in.lawdocs.mkp.MilestoneDelivered.v1` | mkp | Professional submitted a deliverable | engagement_id, deliverable_id | `mkp.DeliverableSubmitted` |
| `in.lawdocs.mkp.EngagementClosed.v1` | mkp | Closed | engagement_id | `mkp.EngagementCompleted` |
| `in.lawdocs.bil.InvoiceFiled.v1` | bil | OH8 invoice mirrored | invoice_ref, amount, due date | `bil.InvoiceAvailable` |
| `in.lawdocs.bil.EntitlementApplied.v1` | bil | Plan or add-on change applied | plan, effective_at | `bil.EntitlementChanged` |
| `in.lawdocs.xpt.ExportCompleted.v1` | xpt | Export archive ready | export_id, archive_id, file count | — |
| `in.lawdocs.sdc.DeliveryGrantProposed.v1`, `…Activated.v1`, `…Renewed.v1`, `…Suspended.v1`, `…Revoked.v1`, `…Expired.v1` | sdc | Grant state change (A.9) | grant_id, state | `sdc.DeliveryGrantChanged` |
| `in.lawdocs.int.WebhookTest.v1` | int | Test button | test_id | — |
| `in.lawdocs.int.OnboardingInvitationAccepted.v1` / `…Declined.v1` / `…Expired.v1` | int | Partner invitation outcome (partner subscriptions only) | partner_ref, state | — |

---

## I.8 Event mapping — internal ↔ ecosystem

Internal names are the producing phase's §7.4 names (re-keyed per Appendix B §B.4.3). "v1.2 proposed" rows are inert behind `int.eco.v12_contracts.enabled` (OFF) until Appendix Y is merged (`LD-INT-033`); the manual interim channel applies meanwhile.

| Internal (`in.lawdocs.*`) | Ecosystem (`in.infrabyx.*`) | Direction | Status |
|---|---|---|---|
| `bil.UsageStatementClosed` | `billing.UsageRecorded.v1` (`usage_aggregate_v1`) | LD → OH8 | v1.1 event; LD added as producer (Appendix Y §Y.7.7, §Y.9) |
| `bil.EntitlementApplied` (module list diff) | `platform.ModuleAttached.v1` / `platform.ModuleDetached.v1` | LD → OH8 | v1.1 |
| (consumed → `core`, `bil`) | `ops.TenantProvisioned.v1`, `billing.PlanChanged.v1`, `billing.EntitlementChanged.v1`, `billing.InvoiceIssued.v1`, `billing.SubscriptionPaymentReceived.v1`, `billing.SubscriptionPaymentFailed.v1`, `billing.SubscriptionCancelled.v1` | OH → LD | v1.1 (LD as consumer, Appendix Y §Y.14) |
| `core.TenantProvisioned` (self-service) / `iam.OnboardingInvitationActivated` (partner) | `ops.TenantRegistered.v1` | LD → OH | v1.2 proposed |
| `core.TenantProvisioned` (self-service, origin recorded) | `ops.TenantSelfServeCreated.v1` | LD → OH4/OH3 | v1.2 proposed (Appendix Y §Y.7.10) |
| `dms.ShareCreated` (to a product, with consent) | `documents.DocumentShared.v1` | LD → FX, LDC, EQ | v1.1 |
| `dms.DocumentDeposited` | `documents.DocumentDeposited.v1` | LD → UD (and any depositor) | v1.2 proposed |
| `clm.AgreementExecuted` / `clm.AmendmentInitiated` (executed child) / `clm.AgreementTerminated` | `legal.AgreementExecuted.v1` / `AgreementAmended.v1` / `AgreementTerminated.v1` | LD → LDC (projection), FX (when a recovery case is linked) | v1.2 proposed |
| `clm.ObligationVerified` / `clm.ObligationOverdue` (+ `wf.ItemResolved` on DONE) | `legal.ContractObligationRegistered.v1` / `ContractObligationStatusChanged.v1` | LD → LDC | v1.2 proposed (status projection per R-A-14) |
| `lit.MatterOpened` / `MatterUpdated` / `MatterSettled` / `MatterClosed` | `legal.LegalMatterOpened.v1` / `LegalMatterUpdated.v1` (settled = update) / `LegalMatterClosed.v1` | LD → LDC | v1.2 proposed |
| `lit.CaseRegistered` / `CaseStatusChanged` / `HearingScheduled` / `OrderConfirmed` (LawDocs-owned cases only) | `legal.CourtCaseRegistered.v1` / `CourtCaseUpdated.v1` / `CourtHearingScheduled.v1` / `CourtOrderRecorded.v1` | LD → LDC | v1.2 proposed (order published only after user verification) |
| (consumed → `lit.projections_rs`) | `litigation.LitigationCaseOpened/Updated/Closed.v1`, `litigation.HearingScheduled.v1`, `litigation.OrderRecorded.v1` | FX RS → LD (read-only projection) | v1.2 proposed (LD as consumer) |
| `sgn.SigningRequestCreated` (API-initiated only) | `esign.SigningRequestCreated.v1` | LD → requesting product (hosted hand-off; NN-06, X-05) | v1.2 proposed |
| `sgn.SigningCompleted` / `sgn.SignerDeclined` / `sgn.SigningRequestExpired` / `sgn.SigningRequestVoided` | `esign.SigningRequestCompleted.v1` (signed) / `…Declined.v1` / `…Expired.v1` / `…Withdrawn.v1` | LD → requesting product | v1.2 proposed |
| `sgn.StampVerified` | `esign.StampInstrumentVerified.v1` (signed) | LD → requesting product | v1.2 proposed |
| `ipm.AssetCreated` / `ipm.StatusChanged` | `ip.IpAssetRegistered.v1` / `IpAssetStatusChanged.v1` | LD → LDC (opt-in) | v1.2 proposed (status projection per R-A-16) |
| `mkp.EngagementContracted` / other `mkp.Engagement*`; `mkp.RetainerActivated` / `RetainerEnded` | `engagement.EngagementCreated.v1` / `EngagementStatusChanged.v1` / `RetainerActivated.v1` / `RetainerEnded.v1` | LD → OH (commercial fields only) | v1.2 proposed |
| `mkp.EngagementContracted` where supplier type ADVOCATE and the client is an organisation | `directory.MatterAllocated.v1` (counts-only fields, basis `CLIENT_CHOICE`) | LD → OH9 | v1.2 proposed (LD as producer) |
| `mkp.PayoutReleaseRequested` (and refund/dispute outcomes) | `billing.MarketplaceTransferInstructed.v1` (signed; RELEASE / REVERSE / EXTEND_HOLD) | LD → OH8 | v1.2 proposed (Appendix Y §Y.7.7) |
| (consumed → `mkp.PayoutReconciled`) | `billing.MarketplacePayoutSettled.v1` | OH8 → LD | v1.2 proposed |
| `mkp.ServiceCreditRequested` (approved, maker-checker) | `billing.ServiceCreditIssued.v1` (signed) | LD → OH8 | v1.2 proposed (Appendix Y §Y.7.10) |
| `mkp.ServiceRequested` for an LDC-fulfilled SKU after payment (group storefront, FR-P16-76) | `ops.ServiceOrderRouted.v1` | LD → LDC | v1.2 proposed (Appendix Y §Y.7.9) |
| (consumed → `bsv`/`mkp` order mirror) | `ops.ServiceOrderStatusChanged.v1` | LDC → LD (and LD → LDC for LawDocs-fulfilled lines bought in LDC, from `bsv.*` status events) | v1.2 proposed (Appendix Y §Y.7.9) |
| `lit.AdrReferralSubmitted` | `adr.ADRReferralCreated.v1` (signed) | LD → EQ or another ODR provider through `ODR_PORT` (Equator is one provider, never default) | v1.2 proposed for Equator (LD as producer for non-loan disputes) |
| (consumed → `lit`) | `adr.ADRCaseStatusChanged.v1`, `adr.ADRHearingScheduled.v1`, `adr.ADRNeutralAppointed.v1`, `adr.ADROutcomeRecorded.v1` | EQ → LD (party view) | v1.2 proposed (LD as consumer) |
| `int.SorSwitchStateChanged` (CUTOVER) | `platform.SystemOfRecordSwitched.v1` | LD ↔ LDC | v1.2 proposed |
| `kyc.ConsentRecorded` / `kyc.ConsentWithdrawn` | `privacy.ConsentRecorded.v1` / `privacy.ConsentWithdrawn.v1` | LD ↔ recipients | v1.1 (LD as capturer, Appendix Y §Y.5 #29) |
| `kyc.RightsRequestChanged` | `privacy.DataPrincipalRequest.v1` | LD ↔ recipients | v1.1 |
| `int.ReconciliationBreakDetected` | `platform.ReconciliationBreakRaised.v1` | LD ↔ counterpart | v1.1 |
| `xpt.ExportRequested` / `xpt.ExportCompleted` / `xpt.StorageTargetConnected` / `xpt.MirrorIncrementDelivered` / `xpt.RestoreTested` | `portability.ExportRequested.v1` / `ExportCompleted.v1` / `StorageTargetConnected.v1` / `BackupCompleted.v1` / `RestoreTested.v1` | LD → OH13 (counts and status only) | v1.1 |
| `eng.ReleasePromoted`; control evidence from `EvidenceCollector-*` jobs (no internal event; mapped directly by `int`) | `ops.ReleasePublished.v1`, `ops.ControlEvidenceCollected.v1` | LD → OH13/OH14 | v1.1 [VERIFY: domain segment per Spec §6.29] |
| `iam.AccessReviewCompleted` (PLATFORM scope) | `ops.AccessReviewCompleted.v1` (counts) | LD → OH13 | v1.1 |
| `web.PageVersionPublished`, `hlp.TutorialPublished`, `hlp.ClipExported` (linked to an OH7 calendar item) | `ops.ContentPublished.v1` | LD → OH7 | v1.2 proposed (Appendix Y §Y.7.10) |
| `sdc.TimeEntryLogged` (daily roll-up job) | `ops.TimesheetAggregated.v1` | LD → OH10/OH11 | v1.2 proposed |
| Monthly delivery-metrics job (P18 FR-P18-69) | `ops.DeliveryMetricsMonthly.v1` | LD → OH10/OH11 | v1.2 proposed |
| Daily client-health job (P18) | `ops.ClientHealthSignal.v1` | LD → OH5 | v1.2 proposed |
| Survey response recorded (P18) | `ops.SurveyResponseRecorded.v1` | LD → OH5 | v1.2 proposed |
| Grievance queue state change (P01 identity/privacy, P16 marketplace, P21 content and accessibility; P15 Consumer Help only into its own entity scope) | `ops.GrievanceStatusChanged.v1` (metadata only) | LD → OH6 | v1.2 proposed |
| (consumed → `sdc` leaver sweep, `iam`) | `EmployeeOffboarded` (Spec Part 6.23) | OH10 → LD | v1.2 proposed (LD as consumer) |
| (consumed) | `ops.SupportTicketOpened/Resolved.v1`, `ops.ImplementationMilestoneReached.v1`, `ops.ChangeApproved.v1`, `directory.ProfessionalEmpanelled/Suspended.v1` | OH → LD | v1.1 |
| (consumed) | `privacy.LegalHoldChanged.v1`, `privacy.DataPrincipalRequest.v1` | Products → LD | v1.1 |

Consumer Help (`chp`) events never appear in this table (NN-23; Appendix Y principle 14). Consumer Help purchases reach OH8 only as billing API calls carrying the closed `CONTRACT_PERFORMANCE_CUSTOMER` field list (X-13; Appendix Y §Y.6.2), never as events.

---

## I.9 Rate-limit tiers (seed; `int.ratelimit.tier`)

| Tier | Applies to | Read | Write | Signing / stamping commands | Bulk / export | Onboarding lookups | Monthly API quota (included) |
|---|---|---|---|---|---|---|---|
| `T0_FREE` | Free (no API access; in-app only) | — | — | — | — | — | 0 |
| `T1_PERSONAL` | Personal (no third-party API; connected apps only) | 30/min per user | 10/min | 5/min | 1 job | — | Connected-app calls only |
| `T2_PRO` | Pro | 120/min per tenant | 60/min | 20/min | 2 concurrent jobs | 30/hour | 50,000 |
| `T3_BUSINESS` | Business | 300/min | 120/min | 60/min | 5 concurrent | 300/hour | 250,000 |
| `T4_ENTERPRISE` | Enterprise (reviewed overrides) | 1,200/min | 600/min | 300/min | 20 concurrent | 3,000/hour | Contracted |
| `P_PARTNER` | Partner onboarding clients | 120/min | 30 batches/day (≤ 500 rows each) | — | — | 3,000 rows/day | Per agreement |
| `E_ECOSYSTEM` | OH, LDC, Finbyx, Udofin, Equator service clients | 600/min per tenant | 300/min | 120/min (separate bucket) | Separate bucket | — | Not metered |
| `C_CERTIFIED` | Certified third-party connectors | 300/min per tenant | 120/min | 60/min | 10 concurrent | — | Counts toward tenant quota |
| `D_DELEGATED` | Zapier, Make, Power Automate, intranet apps | 60/min per user | 30/min per user | Not permitted | — | — | Counts toward tenant quota |
| `X_EMBED` | Publishable keys | 30/min per IP | 10 submissions/hour per IP | — | — | — | — |
| `X_PUBLIC` | Public catalogue, glossary, pricing | 60/min per IP | — | — | — | — | — |

Signing and payment-adjacent commands never share a bucket with bulk reads (Spec §3.10). Overage above the included quota is metered as `API_CALLS_OVERAGE` (per 1,000 calls, R6 §R6.2.6 [OWNER TO SET]); failed calls are not counted. Headers: `RateLimit-Policy`, `RateLimit` [VERIFY: IETF final names], `Retry-After` on 429.

---

## I.10 Error model

**Shape (RFC 9457).**

```json
{
  "type": "https://developers.lawdocs.in/problems/LD-INT-031",
  "title": "Consent or legal basis missing",
  "status": 403,
  "detail": "This exchange carries personal data and needs a consent reference or a legal basis.",
  "instance": "/v1/document-deposits/req_01JB…",
  "code": "LD-INT-031",
  "spec_code": "consent-missing",
  "correlation_id": "01JB7Z…",
  "retryable": false,
  "help_key": "hlp.int.sharing_ledger",
  "errors": [{ "pointer": "/consentref", "detail": "required" }]
}
```

**Rules.**
1. `detail` and `errors[]` never contain personal data, document content, secrets or vendor raw payloads (NN-32).
2. Each LawDocs code is `LD-<MODULE>-<NNN>`, owned and registered by its phase (P19 owns `LD-INT-001`–`LD-INT-099`, P19 §7.6); each has an actionable user message in all launch languages (D-07) and an "i" help key.
3. Ecosystem-facing responses also carry `spec_code` from Spec §3.9; the mapping is fixed:

| Spec code | HTTP | LawDocs code(s) |
|---|---|---|
| `schema-validation-failed` | 422 | module validation codes; `LD-INT-070` (partner rows) |
| `consent-missing` | 403 | `LD-INT-031` |
| `scope-insufficient` | 403 | `LD-INT-002`, `LD-INT-003` (step-up) |
| `tenant-unknown` | 404 | `LD-INT-001` |
| `idempotency-key-reuse` | 422 | `LD-INT-021` |
| `request-in-progress` | 409 | `LD-INT-022` |
| `state-transition-invalid` | 409 | module state codes |
| `regulatory-guard` | 422 | `LD-INT-060` (eSign sublet), `LD-INT-061` (instrument ineligible), `LD-INT-072` (bulk individuals), `LD-INT-090` (portal automation) — `detail` names the rule and citation |
| `rate-limited` | 429 | `LD-INT-041` (`LD-INT-040` quota) |
| `dependency-unavailable` | 503 | `LD-INT-082` |
| `dataclass-not-permitted` | 422 | `LD-INT-030`, `LD-INT-035` (Consumer Help wall) |
| `residency-blocked` | 422 | `LD-INT-034` |
| `grant-expired` | 403 | `LD-INT-032` (link expired) |
| `entitlement-missing` | 403 | Module entitlement codes — never for reading or exporting one's own data (NN-11) |

4. Vendor errors are normalised: `LD-INT-082` with `vendor` and `vendor_code` extension members (no personal data); retryable flag reflects the vendor's semantics; the circuit breaker opens after the configured error budget.
5. Webhook receivers' failures are recorded as delivery status, never surfaced as problems to end users.

---

## I.11 LawDocs-registered file layouts

Each layout: UTF-8 CSV with BOM (RFC 4180) or XLSX, a JSON Schema 2020-12 dictionary, manifest with counts, control totals and SHA-256, detached JWS (Spec §3.11, §12). Canonical register layouts proposed for the Spec are in Appendix Y §Y.11.

| Layout id | Producer → consumer | Use | Key columns |
|---|---|---|---|
| `ld_partner_onboarding_v1` | Partner → LD | Bulk company onboarding (P19 §4K) | partner_ref, legal_name, constitution, cin_or_llpin, gstin, pan_masked, registered_state, signatory_name, signatory_email, signatory_mobile, plan_code, workspace_template, language, authority_attestation |
| `ld_tenant_registrations_v1` | LD → OH (interim until `TenantRegistered`) | Daily commercial record of new tenants | tenantid, org legal name, constitution, cin_or_llpin, gstin, plan_code, partner_ref, activated_at, first-admin work email (`CONTRACT_PERFORMANCE_VENDOR`) |
| `ld_referral_pack_manifest_v1` | LD → ODR provider (interim or file route) | Referral pack by reference | referral_ref, dispute_origin, basis, clause_ref, document_id, document_type, sha256, jws, included_by, approved_by |
| `ld_contract_request_v1` | Customer CRM/ERP → LD | Bulk contract requests | external_ref, contract_type, counterparty_org, counterparty_contact (business), value, currency, start, term_months, department, requester_email |
| `ld_people_minimal_v1` | Customer HRMS → LD | Minimal people sync | employee_ref, display_name, work_email, department_code, position, manager_ref, status, effective_date |
| `ld_court_watch_import_v1` | Customer → LD | Bulk add of court cases for tracking | external_ref, forum, state, district, court, case_type, case_no, year, cnr, client_role, matter_ref |
| `ld_tm_portfolio_import_v1` | Customer → LD | Bulk add of trademark applications | external_ref, application_no, mark, class, filing_date, status (as known), owner_entity |
| `ld_vault_folder_manifest_v1` | Customer → LD (P04 bulk intake) | Folder-structure intake manifest (canonical folder mapping) | relative_path, file_name, sha256, category, year, department, counterparty, document_date, tags |

---

## I.12 Jio Business services — mapping to LawDocs ports (R4)

Every row is flag-gated OFF until DPA, India-processing commitment, no-training terms (AI) and certification exist (R4 D-R4-02, D-R4-11). Jio is a carrier and CPaaS for LawDocs, not an AI-model supplier; Vidhi stays on Claude (D-14; R4 §1).

| Jio offering | LawDocs use | Port / adapter | Gate |
|---|---|---|---|
| JioCX SMS (J-01) | OTP fallback, signing and payment links, deadline alerts | `SMS_PORT` / `jiocx-sms` | DLT binding; DLR webhook; 100-message sandbox test |
| JioCX RCS (J-03) | Primary verified-sender signing-link channel incl. iPhone | `RCS_PORT` / `jiocx-rcs` | Brand profile; template approval; SMS fallback |
| JioCX WhatsApp (J-04) | Utility messages to opted-in users | `WHATSAPP_PORT` / `jiocx-whatsapp` | Meta verification; BSP status [VERIFY] |
| JioCX Voice (J-02) | Masked click-to-call with assigned professional; IVR; missed call | `VOICE_PORT` / `jiocx-voice` | Flow ids; virtual numbers; A2P declaration |
| JioCX Verify (J-08) | Branded caller ID on nudges and callbacks | `CALLER_ID_PORT` / `jiocx-verify` | Pilot ≥ 10% answer-rate uplift |
| JioCX Email (J-06), Alerts (J-07) | Alternate transactional email; incident fan-out | `EMAIL_PORT` / `jiocx-email` | Terms |
| Jio SIP Trunk (J-13), Toll-Free (J-14) | Second carrier; legal-help toll-free line | `TELEPHONY_PORT` / `jio-sip` | CAF/MSA; failover test |
| Jio Haptik (J-11) | RFP challenger for intake voice agent | `VOICE_AGENT_PORT` / `haptik-voice` | BYO-LLM via LawDocs' Bedrock proxy; residency |
| Jio Enterprise AI Cloud (J-18) | Indic STT/TTS challenger | `INDIC_SPEECH_PORT` | Published API, price, India-only processing [VERIFY] |
| JioCloud Azure (J-17) | Optional client export destination in Indian regions | `STORAGE_PORT` (Azure Blob) | Region evidence [VERIFY] |
| JioMeet (J-16) | Rejected for consultations (no API) | — | — |
| JioBrain, REIL, Reliance Intelligence | No product or API — watch-list | — | — |

---

## I.13 Connector certification checklist

| Area | Requirement |
|---|---|
| Manifest | `id` (`[counterparty]-[capability]-lawdocs`), version, port, capabilities (API, WEBHOOK, POLL, FILE, PORTAL_MANUAL), schemas, scopes, data classes, residency, sub-processors, egress allow-list |
| Security | mTLS or `private_key_jwt`; secrets by vault handle; no secrets in logs; SBOM; read-only, non-root container; egress allow-list enforced; VAPT ≤ 12 months |
| Contract | Pact/contract tests; schema validation; projections carry no forbidden fields |
| Idempotency and ordering | Duplicates harmless; key reuse 422; concurrent 409; `seq` ordering |
| Resilience | 4-hour counterpart outage; partial failures; DLQ and replay; circuit breaker |
| Privacy | `consentref`/`legalbasis`; data-class ceilings; no personal data in logs; residency checks; transfer register entry for any abroad processing |
| Regulatory guards (LawDocs) | No court, registry, regulator, bureau or government portal automation (NN-05); WhatsApp never for legal notices or recovery; DLT compliance; no ESP credential exposure (NN-06); eligibility gate enforced for API-initiated signing (NN-07); no `CONSUMER_HELP` class mapped (NN-23) |
| Reconciliation | Daily counts and hashes; break detection |
| Operations | Health endpoint, metrics, traces, runbook, kill switch tested |
| Result | `ConnectorCertified`; catalogue listing; recertify on schema, hosting, key or sub-processor change and annually |

---

## I.14 Egress policy: blocked and allowed destinations (NN-05)

The connector runtime and every `apps/api` worker run behind an egress proxy with a default-deny policy. Each connector manifest lists its allowed hostnames; CI fails if any manifest, code path or configuration names a blocked domain.

| Category | Blocked domains (pattern, non-exhaustive; maintained in `packages/connectors/egress/deny.yaml`) | Lawful route instead |
|---|---|---|
| Courts | `*.ecourts.gov.in`, `njdg.ecourts.gov.in`, `hcservices.ecourts.gov.in`, `sci.gov.in`, `*.nclt.gov.in`, `drt.gov.in`, `e-jagriti` portal hosts [VERIFY host], High Court sites | Licensed aggregators; `ManualCNR`; official API only with an institutional litigant's own credentials (R6 D-01, D-08) |
| IP | `tmrsearch.ipindia.gov.in`, `ipindiaonline.gov.in`, `search.ipindia.gov.in` | Manual application number; WIPO Brand DB; licensed watch partner |
| Company and tax registries | `mca.gov.in`, `*.gst.gov.in` (portal UI), `incometax.gov.in`, `tin-nsdl`/Protean PAN service hosts, `traces` hosts | Licensed MCA-data vendors; GSP APIs; user-initiated deep links (R3 LG-047–LG-050) |
| KYC and credit | `ckycindia.in`/CKYCR hosts, `cibil.com`, `experian.in`, `equifax.co.in`, `crif` hosts | None (closed to LawDocs — CH-03, CH-05); user uploads own report |
| Transport and challans | `parivahan.gov.in`, `echallan.parivahan.gov.in`, `vahan` hosts | Deep link for the user; user-entered details (R6 D-10) |
| Regulator portals | RBI CIMS/DAKSH/PRAVAAH, `cms.rbi.org.in`, `bimabharosa.irdai.gov.in`, `scores.sebi.gov.in` | Deep links; drafted complaints the user files (Spec §6.18 principle 11; NN-23) |

Allowed by default: ecosystem hosts (Infrabyx PKI-authenticated), contracted vendor API hosts per manifest, `api.gleif.org`, DigiLocker/Entity Locker partner API hosts (NeGD), UIDAI-published verification endpoints used by the Aadhaar App flow [VERIFY], Microsoft Graph, Google APIs, Meta Graph (WhatsApp Cloud API), Amazon Bedrock and SES in ap-south-1/2.

## I.15 Vendor contract checklist (before any adapter leaves its kill switch)

| Clause | Requirement |
|---|---|
| Lawful collection and licence | Written warranty that the vendor's data is lawfully collected and that its licence covers LawDocs' stated use and display; no-resale terms compatible with LawDocs' use (R6 D-08, D-15) |
| Processor terms (DPDP) | DPA: purpose limitation, sub-processor list and change notice, deletion on termination, breach notice to LawDocs within 6 hours (so LawDocs can meet CERT-In 6 h and DPDP timelines — R3 LG-065, LG-079), audit rights |
| Residency | Processing and storage in India for tenant data; written commitment where the vendor's site is silent (R4 D-R4-02) |
| No training | No use of LawDocs or customer data to train models (AI, voice, OCR vendors — NN-15) |
| Security evidence | ISO/IEC 27001 or SOC 2 report, VAPT ≤ 12 months, CERT-In-empanelled audit where the vendor is a requester or ASP-facing |
| eSign/eStamp specifics | ESP licence status and renewal evidence; second-ESP route; log export and retention ≥ 7 years after account closure (R3 LG-008); State coverage list with dates; pure-agent duty handling (R6 D-25) |
| Telecom specifics | DLT telemarketer binding, A2P declaration support, DLR webhooks, per-tenant sub-accounts for tenant-branded sending (R4 §3.2 Q14) |
| SLA and exit | Availability, support hours, incident communication, data export in open formats, termination assistance |
| Pricing | Per-unit price, minimums, overage, currency (WhatsApp INR billing — R6 D-31), pass-through rules (R6 §R6.7) |

---

## I.16 Open items

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-I-01 | Aggregator ASP structure and second-ESP rule under eSign API v3.3 for Leegality/Digio routes | Procurement + [COUNSEL] | Direct ASP with one ESP plus aggregator as second route |
| OI-I-02 | eStamp vendor State coverage and verification APIs; SHCIL corporate channel | Procurement | Physical/franked stamp upload with human UIN check |
| OI-I-03 | Court-data vendor contracts (two), coverage of NCLT/DRT/e-Jagriti, no-resale terms | Procurement + [COUNSEL] | Manual CNR |
| OI-I-04 | MCA-data vendor display rights; GSP selection | Procurement | Manual entry with documents |
| OI-I-05 | WIPO Global Brand Database terms of reuse; TM Journal partner | P12 lead | Manual application tracking |
| OI-I-06 | Microsoft Graph and Google scope names; owner's M365 plan (CH-29) | CTO + [OWNER] | ICS feeds; download/upload |
| OI-I-07 | JioCX contracts, BSP status, Haptik residency/DPA | Procurement | Other DLT aggregator; Meta Cloud API direct |
| OI-I-08 | India Post bulk API access for LawDocs | P10 lead | Courier APIs; user print-and-post |
| OI-I-09 | Graphy API/feed for FinLegal Academy | Academy lead | Curated import |
| OI-I-10 | Zapier, Make, Power Automate listing terms and residency | PLT_DPO | Webhooks + OpenAPI only |
| OI-I-11 | IETF RateLimit and Idempotency-Key header final status | P19 lead | Keep current headers; document |
| OI-I-12 | Exact Spec `domain` segment for engineering events (`ops` vs `platform`) | Integration lead | Use Spec §6.29 table names at wiring |
