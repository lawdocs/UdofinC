# Appendix J — Jio Business Services and Telecom Rules

**Status:** Binding for telecom rules (§J.5–§J.7) and port design (§J.3); Reference for the service catalogue (§J.2), which must be re-verified before any contract. **Used by:** P01 (OTP fallback), P08 (signing invitations and reminders), P09 (voice agent, speech adapters, agent sends), P11 and P12 (hearing and deadline alerts), P15 (Consumer Help toll-free line), P17 (usage pricing of messages), P18 (RM telephony), P19 (`packages/notify` and `packages/connectors` adapters), P20 (export destinations), P21 (growth/autopilot channels), P23 (vendor assessment).

**How to use.** The owner asked for Jio's AI and business services to be explored and integrated for customers and internal operations (R-029, R-062). Research (R4, 25 Oct 2026) found that Jio is a **carrier and CPaaS supplier for LawDocs, not an AI-model supplier**: no Jio or Reliance enterprise LLM has a public product, API or price, and JioBrain is internal network AI (R4 §1, §3.1). Vidhi therefore stays on Claude (D-14). Jio services enter LawDocs only as **adapters behind ports**, each with a flag that is OFF until its activation preconditions are met (NN-38, NN-39), and never as the only route. Every outbound message or call obeys §J.5 (NN-34; CH-17). Status tags: **VERIFIED** = product page read on 25 Oct 2026 (R4); **[VERIFY]** = a material detail (API, price, residency, terms) is unconfirmed; **[K]** = carried from sister packs, not re-read.

---

## J.1 Position in one table

| Question | Answer | Basis |
|---|---|---|
| Can Vidhi run on a Jio AI model? | No — no contractable Jio/REIL LLM exists; adapter stub stays OFF; admission criteria in P09 §8 | R4 D-R4-10, §3.1 |
| What Jio services are useful now? | JioCX RCS, SMS, WhatsApp, Voice (C2C, IVR, missed call), Verify (branded caller ID), Email, Alerts; SIP trunk and toll-free; Haptik as RFP challenger for voice/WhatsApp agents; Jio AI Cloud cognitive services as a future Indic speech challenger | R4 §1, §3 |
| Is there developer documentation? | Yes for JioCX (developer.jiocx.com quick starts; endpoint/auth pages behind sign-up; 100 free test SMS/month). None for jio.com/business products. | R4 D-R4-01 |
| What blocks go-live? | DLT registration, A2P CLI declarations, written India-processing and DPA terms (not published by JioCX or Haptik), authenticated delivery-report webhooks | R4 D-R4-02, D-R4-11, §5 |
| What changed in 2026? | TCCCPR (Third Amendment) Regulations 2026 (No. 05 of 2026, 18 Sep 2026): automated/AI-voice calls are A2P and must come from pre-declared CLIs; inquiry-based contact limited to 7 days; service-message consent valid 7 days | R4 D-R4-05, §5.2 |
| Biggest opportunity | RCS signing-link cards with a verified LawDocs sender that reach Android and iPhone (Jio states it is the exclusive RCS provider for iOS in India) | R4 D-R4-04 [V2] |

---

## J.2 Service catalogue — LawDocs use, route, status and contract needs

| # | Jio service | LawDocs use — customer-facing | LawDocs use — internal ops | Route (port → adapter; flag) | Status (25 Oct 2026) | Commercial / contract needs |
|---|---|---|---|---|---|---|
| J-01 | **JioCX SMS** | OTP fallback (P01); signing-link and payment-link service messages; hearing-date and TM-deadline alerts | Staff SLA-breach alerts | `COMMS_PORT/SMS` → `jiocx-sms`; `ntf.jiocx.sms_enabled` | VERIFIED; API docs behind sign-up | DLT PE/headers/templates bound to JioCX as telemarketer; usage pricing [VERIFY rate card]; DLR webhook auth (HMAC) [VERIFY]; DPA |
| J-02 | **JioCX Voice** (OBD, IVR, Click-to-Call, Missed Call, Voice OTP) | C2C "talk to the assigned professional" with masked numbers [VERIFY masking]; missed-call "call me back"; multilingual IVR helpline; Voice OTP for low-literacy users | Telecalling C2C from the Delivery Console; IVR routing to ops queues | `VOICE_PORT` → `jiocx-voice`; `ntf.voice.jiocx_enabled` | VERIFIED (C2C needs Flow ID + JioCX virtual number); IVR/OBD endpoints [VERIFY] | Flow IDs per use case; virtual numbers; A2P declaration for any automated leg (§J.5.3); recording-notice prompts in each language; per-minute pricing [VERIFY] |
| J-03 | **JioCX RCS** | **Primary verified-sender channel for signing links** ("Review and eSign" button) to Android and iPhone; payment-link cards; hearing reminders with "Add to calendar" | Campaigns to consented leads only | `COMMS_PORT/RCS` → `jiocx-rcs`; `ntf.jiocx.rcs_enabled` | VERIFIED; tiered pricing ₹0.25 transactional / ₹0.27–0.30 marketing / ₹0.11–0.16 OTP per message [V2] | Verified brand profile; template approval; DLR + read receipts; SMS fallback on non-RCS handsets; RCS DLT treatment [VERIFY — OI-R4-10]; URL whitelisting |
| J-04 | **JioCX WhatsApp** | Utility templates for opted-in users (signing status, document ready, receipt); Vidhi chat on WhatsApp (opt-in) | Support desk channel (via OH) | `COMMS_PORT/WHATSAPP` → `jiocx-whatsapp`; `ntf.jiocx.whatsapp_enabled` | VERIFIED (BSP-style onboarding) | Meta business verification; utility templates approved; signed webhooks; Meta per-message pricing pass-through [VERIFY]; Meta local storage `IN` [K] |
| J-05 | **JioCX Pulse** | — (LawDocs app is the system of record) | Optional marketing/support WhatsApp inbox for the growth team if Brevo WhatsApp is weak (OH decision, D-02) | Not integrated into LawDocs; OH-side tool | VERIFIED; pricing [VERIFY] | OH procurement; never holds tenant documents (NN-19) |
| J-06 | **JioCX Email** | Secondary transactional email route (fallback to SES/Brevo) | — | `COMMS_PORT/EMAIL` → `jiocx-email`; `ntf.jiocx.email_enabled` | VERIFIED | SPF/DKIM/DMARC alignment; bounce webhooks |
| J-07 | **JioCX Alerts** | Platform-incident notices to tenants (breach communication fan-out: DPDP Rules 2025 r.7; CERT-In 6 h) | Incident broadcast to staff | `COMMS_PORT/ALERTS` → `jiocx-alerts`; `ntf.jiocx.alerts_enabled` | VERIFIED; API [VERIFY] | Pre-approved incident templates per channel |
| J-08 | **JioCX Verify** (branded caller ID) | "LawDocs" shown on signing-nudge, payment and professional call-back calls; lowers scam fear | Telecalling answer-rate uplift | `CALLER_ID_PORT` → `jiocx-verify`; `ntf.voice.branded_cli_jiocx_enabled` | VERIFIED; non-Jio network coverage [VERIFY — OI-R4-11] | Pilot gate: ≥ 10% answer-rate uplift and zero impersonation complaints; Truecaller for Business in parallel [K] |
| J-09 | **JioCX EasyPhone** | Single LawDocs helpline number | WFH RMs call on a business number from own phones, calls logged for SLA reporting (outcome metrics only — NN-33) | OH/P18 telephony; API "coming soon" | VERIFIED | Business-number plan; export of call logs into OH |
| J-10 | **JioCX EasyListing** | Local listings for LawDocs as a company (Delhi, Noida, Jaipur) — **never** for individual advocates (BCI Rule 36) | Review management for the company (NN-49) | OH marketing tool | VERIFIED | Listing content via claims register (NN-20) |
| J-11 | **Jio Haptik — AI/voice agents** | Candidate engine for the multilingual intake voice line (`AGT_INTAKE_VOICE`) and "where is my document?" bot | Inbound AI SDR candidate | `VOICE_AGENT_PORT` → `haptik-voice`; `ai.voice_agent.haptik_enabled` | VERIFIED capability; residency/DPA/no-training [VERIFY] | RFP (EQ Q1–Q12 + Q13–Q15, §J.4); **BYO-LLM through LawDocs' Bedrock India proxy** so case content never reaches a vendor LLM; no vendor human review of recordings |
| J-12 | **Haptik Interakt / Contakt** | — | Optional WhatsApp marketing CRM for OH | OH tool | Named; detail [VERIFY] | OH decision only |
| J-13 | **SIP Trunk** | — | **Second PSTN carrier** behind the voice stack | `TELEPHONY_PORT` → `jio-sip`; `ntf.telephony.jio_sip_enabled` | VERIFIED | CAF/MSA; failover test; ≤ 70% traffic on one carrier (EQ JR-10 [K]) |
| J-14 | **Toll-Free** | "1800" legal-help line, including the Consumer Help brand line (separate number per brand, NN-23) | — | `TELEPHONY_PORT` → `jio-tollfree` | VERIFIED | Order form; per-minute cost borne by LawDocs |
| J-15 | **IP Centrex** | — | Office telephony Delhi/Noida/Jaipur | OH/IT | VERIFIED | Order form |
| J-16 | **JioMeet** | **Rejected** for consultations (no embed or recording-export API) — use in-app WebRTC or Teams/Google Meet links via `WORKSPACE_PORT` | — | — | VERIFIED; reject | — |
| J-17 | **JioCloud (Azure through JioCloud) — AI + ML** | Export destination for a client who wants an Indian data-centre copy (Azure Blob in "Jio regions") | — | `CLOUD`: P20 `STORAGE_TARGET` → `azure-blob` (Jio-hosted variant) | VERIFIED; regions not named [VERIFY] | Region attestation in writing; tenant-signed India attestation (Ecosystem Spec storage table) |
| J-18 | **Jio Enterprise AI Cloud** (GPU nodes; cognitive services: STT, TTS, translation, transliteration) | Indic STT/TTS/transliteration challenger for voice notes, read-outs and type copy | Sovereign route candidate for an open-weight model if an Enterprise client demands it (P09 FR-P09-01 stub) | `INDIC_SPEECH_PORT` → `jio-ai-cloud-cognitive`; `ai.speech.jio_enabled` · `CLOUD`: `AI_PORT` → `sovereign-openweight` | VERIFIED capability; no public API reference, prices or certifications [VERIFY] | Published API + price; India-only processing in writing; WER bake-off pass; evaluation parity within 3 points |
| J-19 | **GPU Accelerated Computing** | — | Not needed (managed Claude); keep for sovereign-route evaluation | `CLOUD` | VERIFIED | — |
| J-20 | **Security services** (vCISO, CyberSOC, TVM, NetSensor, DDoS) | — | MSSP candidate for LawDocs' SOC 2 / ISO 27001 / PCI DSS programme (R-033) | P23 vendor | VERIFIED; CERT-In empanelment not stated | VAPT must still use a CERT-In-empanelled auditor (R3 LG-080) |
| J-21 | **JioAds / GoLocal** | Hyper-local campaigns for LawDocs city launches (public offers such as vehicle-sale kits) — company advertising only | Media-buying channel (OH) | OH marketing | VERIFIED; JioAdsXchange not found [U] | No targeting on sensitive legal intents (R4-MKT-10); never advertise advocates (R4-MKT-01); NN-35 is about ads shown *on* LawDocs pages and is unaffected |
| J-22 | **Jio DLT (operator portal)** | Mandatory registration for all LawDocs SMS/voice | — | Operator portal (e.g., Jio TrueConnect [K]) | [K] [VERIFY URL] | PE registration, headers, templates, consent templates, telemarketer binding (§J.5.4) |
| J-23 | **JioAttendance, JioPC, connectivity** | — | Not adopted (own HRMS in OH, NN-33); JioPC as WFH thin client [VERIFY business plan]; office links | — | Named / [V2] | — |

**Watch-list (no integration):** Reliance Intelligence and REIL (no product), JioBrain (network AI), AGM 2026 consumer AI apps including the **Jio AI Call Agent** and **TeleFrame** — the call agent creates a confidentiality risk for advocate consultations (§J.6.2). Re-check Jio Platforms' RHP and IMC 2026 announcements for enterprise-AI APIs (OI-R4-07).

---

## J.3 Ports, adapters and activation preconditions

`COMMS_PORT` is the umbrella port in `packages/notify` for message channels; its channel sub-ports carry the R4 adapter names. Settings keys from R4 are renamed to the Conventions pattern `<module>.<area>.<key>` (module `ntf` for channels, `ai` for speech/voice agents).

| Port | Primary (pack) | Jio adapter | Flag (default OFF) | Activation preconditions (all must be logged in `docs/compliance/verification-log.md`) |
|---|---|---|---|---|
| `COMMS_PORT/SMS` | MSG91 [K] | `jiocx-sms` | `ntf.jiocx.sms_enabled` | DLT PE/headers/templates bound to JioCX; authenticated DLR webhook; 100-message sandbox test passed |
| `COMMS_PORT/RCS` | — (new) | `jiocx-rcs` (primary once live) | `ntf.jiocx.rcs_enabled` | Verified brand profile; templates approved; DLR + read receipts; SMS fallback; RCS DLT treatment confirmed |
| `COMMS_PORT/WHATSAPP` | Meta Cloud API via BSP [K] | `jiocx-whatsapp` | `ntf.jiocx.whatsapp_enabled` | Meta verification; utility templates; signed webhooks |
| `COMMS_PORT/EMAIL` | SES / Brevo | `jiocx-email` | `ntf.jiocx.email_enabled` | Domain authentication; bounce handling |
| `COMMS_PORT/ALERTS` | Native fan-out | `jiocx-alerts` | `ntf.jiocx.alerts_enabled` | Incident templates approved |
| `VOICE_PORT` (CPaaS) | Exotel India cluster [K] | `jiocx-voice` | `ntf.voice.jiocx_enabled` | Flow IDs; virtual numbers; A2P declarations filed; recording notice per language |
| `TELEPHONY_PORT` (SIP/toll-free) | Exotel/Plivo [K] | `jio-sip`, `jio-tollfree` | `ntf.telephony.jio_sip_enabled` | CAF/MSA; failover test; carrier-share cap |
| `CALLER_ID_PORT` | Truecaller for Business [K] | `jiocx-verify` | `ntf.voice.branded_cli_jiocx_enabled` | Pilot uplift ≥ 10%, zero impersonation complaints |
| `VOICE_AGENT_PORT` | ElevenLabs Agents + Claude via Bedrock proxy [K] | `haptik-voice` | `ai.voice_agent.haptik_enabled` | RFP gates G1–G11 + Q13–Q15; BYO-LLM via LawDocs proxy |
| `INDIC_SPEECH_PORT` | Sarvam [K] | `jio-ai-cloud-cognitive` | `ai.speech.jio_enabled` | Published API + price; India-only processing in writing; WER bake-off |
| `CLOUD` — export destination | S3 / Azure Blob / SharePoint / Drive (P20) | Azure Blob in Jio regions | `xpt.storage.jio_azure_enabled` | Region attestation; tenant attestation |
| `CLOUD` — sovereign AI route | — | Jio Enterprise AI Cloud GPU | `ai.routing.sovereign_route` | P09 admission criteria; DPIA; evaluation parity |

**Adapter rules.** (1) Each adapter implements the port contract, idempotency keys and reconciliation of delivery reports (NN-46). (2) Every adapter has a kill switch (NN-39) at platform and tenant level. (3) Failover order per channel is a PLATFORM setting; a failed send never silently switches to a channel the recipient did not consent to. (4) Delivery reports update `ntf.deliveries` and the signing evidence pack where relevant (P08). (5) Message bodies are not logged; only template ID, variables hash, recipient token and status (NN-32).

---

## J.4 Vendor admission and contract checklist (JioCX, Haptik, Jio AI Cloud)

| Gate | Requirement | JioCX (25 Oct 2026) | Haptik | Jio AI Cloud |
|---|---|---|---|---|
| G1 | Written API specification + sandbox | Partly met (docs behind sign-up; 100 free SMS) | Not public | Not public |
| G2 | DPA with DPDP processor terms (s.8(2)) | Open | Open | Open |
| G3 | India-only processing and storage in writing | Not stated | Regions not named | "Indian data stays in India" (marketing text) — need contract |
| G4 | No training on LawDocs data; retention period stated | Not stated | Not stated | Not stated |
| G5 | Sub-processor list | Not published | Not published | Not published |
| G6 | Authenticated webhooks (HMAC/mTLS), DLR completeness | [VERIFY] | [VERIFY] | n/a |
| G7 | Security certifications | ISO 27001:2022, ISO 22301, SOC 2 (type not stated), ISO 27701 listed | ISO 27001:2022 | None named |
| G8 | Incident notice to LawDocs within 6 h (to meet CERT-In) | Open | Open | Open |
| G9 | SLA, support, uptime credits | Open | Open | Open |
| G10 | Exit: data return and deletion certificate | Open | Open | Open |
| G11 | Replaceability: port contract test passes against a second vendor | Required | Required | Required |
| Q13 | Signing-link deep links in RCS/WhatsApp templates with URL whitelisting proof | Ask | Ask | — |
| Q14 | Per-tenant sub-accounts for "tenant-branded" sending under the tenant's own PE/headers | Ask | Ask | — |
| Q15 | Privilege controls: no vendor human review of legal-consultation recordings | Ask | Ask | Ask |

(G1–G12 and Q1–Q12 originate in EQ Appendix T §4 [K]; Q13–Q15 are R4 additions.) Commercial: usage-based pricing pass-through is shown to tenants in `bil` only as LawDocs message credits; per-message costs are reconciled monthly (P17). Contracts are signed by `[LawDocs Operating Entity]`; each group company signs its own DLT PE and telemarketer bindings (§J.8).

---

## J.5 TRAI TCCCPR / DLT rules (binding)

### J.5.1 Instrument chain

| Instrument | Date | LawDocs-relevant effect | Tag |
|---|---|---|---|
| Telecom Commercial Communications Customer Preference Regulations 2018 (TRAI Regulation 6 of 2018) | 19 Jul 2018 | DLT framework: Principal Entity (PE) registration, headers, content templates, consent and preference registers, DND scrubbing | [K] |
| TRAI Directions | 20 Aug 2024 (revised 30 Aug 2024) | 140-series voice on DLT by 30 Sep 2024; only whitelisted URLs/APKs/OTT links from 1 Oct 2024; PE-to-recipient traceability from 1 Nov 2024; one template ↔ one header; template blacklisting for mis-categorisation | [V2] |
| TCCCPR (Amendment) Regulations 2025 | Press release 12 Feb 2025 | 140-series promotional, 1600-series service/transactional calls; 10-digit numbers barred for telemarketing; header suffixes -P/-S/-T/-G; complaint window 7 days; action at 5 complaints in 10 days; mandatory opt-out in promotions; no re-seeking consent for 90 days after opt-out; transaction-related consent 7 days; auto-dialler/robocall use disclosed | [V] |
| TRAI direction on 1600-series for BFSI | Reported 19 Nov 2025 | Sector deadlines (relevant to Finbyx/Udofin, §J.8) | [V2] |
| **TCCCPR (Third Amendment) Regulations 2026, No. 05 of 2026** (RG-25/(25)/2023-QoS) | 18 Sep 2026; commencement 30/60/90 days after Gazette publication by provision (Reg. 1(3)) | §J.5.2 | [V]; Gazette date [VERIFY — OI-R4-02; fallback: treat Reg. 4 as in force from 1 Dec 2026] |
| DPDP Act 2023 + Rules 2025 | Rules 13 Nov 2025; consent managers 13 Nov 2026; core obligations 13 May 2027 | TCCCPR consent and DPDP consent are separate objects (Third Amendment Reg. 2(k) Explanations) | [V2]; R3 LG-061–063 |

### J.5.2 Third Amendment 2026 — clause points and LawDocs implementation

| Clause | Rule (R4 §5.2) | Implementation |
|---|---|---|
| Reg. 2(ea) | A2P call = call initiated by an application/software/automated platform without direct human dialling, incl. autodial, robocall, pre-recorded or **artificial voice** | Every AI-voice, IVR-outbound and OBD call is A2P. A human pressing click-to-call is treated as not A2P [VERIFY with TSP]. |
| Reg. 4 (replaced) | Sender declares A2P use and CLI ranges in advance to the originating access provider; recorded on DLT; undeclared A2P = UCC | `ntf.a2p_declarations` (CLI, TSP, declaration ref, purpose, valid_from, valid_to); dialler refuses a CLI without an active declaration (`LD-NTF-041`); expiry alert 30 days ahead |
| Reg. 35A | Terminating operator may charge up to ₹0.05/min for A2P calls except on 140xx, 1600xx, 1601xx | Cost model in P17 usage pricing |
| Reg. 21A | TSPs flag high-probability UCC CLIs (UCC_Detect) within 2 h; 5+ flagged CLIs in 10 days → KYC re-verification (3 business days), physical KYC (5 days), then 15-day bar | Ops runbook: respond to OAP sender notices within 3 business days; KYC pack kept current by `PLT_SECURITY_OFFICER` |
| Reg. 2(bb) | Inquiry-based "relationship" only if written/digital and verifiably kept; communication on it limited to **7 days**; application-based relationship 3 months | Lead records store the inquiry artefact with timestamp; marketing contact stops at day 7 unless explicit consent is registered (R4-MKT-06) |
| Reg. 2(y), 2(k) | Explicit consent may be captured outside the operator's CRF if registered in the Consent Register per TRAI procedure; TCCCPR revocation does not revoke DPDP consent (and vice versa) | Two consent objects: `ntf.telecom_consents` (registered with TSP DCA/consent register when the procedure is live [VERIFY DCA status for non-banks]) and `kyc.consent_artefacts` (DPDP, purpose-wise) |
| Reg. 2(bh)(ii) | Explicit consent for **service messages** valid 7 days or until revoked; renewable in 7-day blocks | Signing-reminder consent captured per signing request, expires 7 days after capture unless renewed in-flow ("keep reminding me") |
| Reg. 22 | Misused header/template suspended within 6 h; sender resets credentials and files a police complaint within 3 business days | DLT credentials in the platform secrets vault; maker-checker on template changes (NN-18); security runbook |
| Reg. 25(6) | First violation: 15-day bar on all sender resources; subsequent: 1-year disconnection and blacklisting | **Never** share CLIs/headers between promotional and transactional/service traffic; separate PE per group company |
| Reg. 34A | Call-management apps may not tag/block designated commercial series (140xx/1600xx/1601xx) | Prefer designated series where allotted; LawDocs' eligibility for 1600-series as a non-BFSI entity [VERIFY — OI-R4-03; fallback: declared 10-digit A2P CLIs for service calls, 140-series for promotional] |

### J.5.3 Channel rules matrix (enforced by the `ntf` scheduler and dialler)

| Traffic | Allowed channels | Header / CLI | Consent basis | Window (local time) | Must include |
|---|---|---|---|---|---|
| OTP (login, eSign consent screens are ESP-owned) | SMS (-T), Voice OTP, RCS OTP | -T header; declared CLI for voice OTP | Transaction | Any | No links in OTP SMS |
| Service (signing status, document ready, hearing/TM alerts to subscribers) | App push, email, RCS, WhatsApp utility, SMS (-S) | -S header | Service relationship (subscriber) or 7-day service consent (Reg. 2(bh)(ii)) | 09:00–21:00 for calls [policy]; messages any time except quiet hours set by user | Initiator/brand name; opt-out for non-essential alerts |
| Signing invitation to counterparty | Initiator's own share sheet; one LawDocs email; one LawDocs service SMS/RCS | -S | Initiator's instruction + performance of a transaction the counterparty is party to [VERIFY TCCCPR "service" category] | 09:00–21:00 | Initiator's name; opt-out (§J.5.5) |
| Reminders to an opted-in signer | Toggled channels only; AI voice only if toggled | -S; declared A2P CLI for AI voice | 7-day service consent per channel | 09:00–21:00 | AI disclosure on voice; stop on sign/decline/"stop" |
| Promotional (offers, webinars) | Email (Brevo via OH), RCS/SMS (-P), WhatsApp marketing templates | -P header; 140-series for voice | Registered explicit consent; inquiry ≤ 7 days | 10:00–19:00 [policy] | Opt-out; no re-solicitation for 90 days after opt-out |
| Inbound-lead response (AI SDR) | Chat, WhatsApp reply, call-back from declared CLI | Declared CLI | Inquiry (≤ 7 days) or explicit consent | 10:00–19:00 [policy] | AI disclosure; human hand-off |
| Incident/breach notices | All channels via Alerts fan-out | -S/-T | Legal obligation (DPDP r.7; CERT-In) | Any | Plain description, actions, contact |

Calling-hour windows are a conservative house rule [policy choice; R4 §5.4] stored as settings; lender–borrower contact via Finbyx/Udofin follows RBI windows (§J.8).

### J.5.4 DLT registration checklist (LawDocs and each group company separately)

1. Principal Entity registration on one operator DLT (e.g., Jio TrueConnect [K]) with PAN, GSTIN, certificate of incorporation, authorisation letter; PE ID honoured across operators.
2. Headers separated by category: transactional (-T), service (-S), promotional (-P) — e.g., `LAWDOC-T`, `LAWDOC-S`, `LAWDOC-P` [VERIFY header format and length]; the Consumer Help brand gets its own headers (NN-23).
3. Content templates: one header per template; variables only where allowed; every URL domain whitelisted (lawdocs.in, short-link domain, Razorpay, ESP domains).
4. Telemarketer binding (JioCX, MSG91, Exotel) and chain declaration (traceability).
5. Voice: 140-series for promotional voice; A2P CLI declaration for automated service calls; 1600-series application if eligible.
6. Consent templates for digital consent acquisition once the DCA route is available to non-banks [VERIFY].
7. **Tenant-branded mode:** a company tenant may send under its own PE/headers; LawDocs stores the tenant's PE ID and template IDs (`ntf.tenant_dlt_profiles`) and refuses sends without them.
8. Template changes are maker-checker (`PLT_CONTENT_EDITOR` → `PLT_SECURITY_OFFICER`); DLT credentials rotate on any suspected misuse (Reg. 22).

### J.5.5 Counterparty-contact rule `R4-COMMS-01` (binding; implements NN-34)

1. The initiator chooses how to invite: (a) "Share from my phone" (wa.me / SMS deep link with a pre-filled message and the signing URL — user-to-user, not business messaging); (b) LawDocs email; (c) one LawDocs service SMS or RCS card.
2. LawDocs sends **at most one** business-initiated message to a counterparty who has not opened the link, plus reminders only on channels the counterparty later opts into.
3. On opening, the signing page shows a DPDP notice and channel toggles (WhatsApp / SMS / RCS / call reminders, preferred language, preferred time). Only toggled channels are used; consent expires 7 days after capture unless renewed.
4. **No automated voice** to a counterparty who has not opted in.
5. Every message names the initiator ("Ravi Sharma has sent you a rental agreement via LawDocs") and contains an opt-out.
6. Counterparty contact data is never used for marketing and never passed to the OH CRM (R4-MKT-12; NN-19).

### J.5.6 AI voice specifics (with P09)

- AI voice is synthetically generated audio under IT Rules 2026 r.2(1)(wa), r.3(3) (R3 LG-078): audible AI prefix in the session language, provenance metadata on stored audio.
- Outbound AI calls only: from declared A2P CLIs (Reg. 4), to opted-in recipients, inside windows, with "say 'agent' for a person" and a real human queue during operating hours; outside hours the agent books a call-back and never continues a sales or collections-style script.
- The voice agent gives general information only; matter-specific advice goes to a professional (Anthropic Usage Policy, P09 FR-P09-53).
- `LD-NTF-041` (no active declaration), `LD-NTF-042` (outside window), `LD-NTF-043` (no channel consent), `LD-NTF-044` (counterparty not opted in), `LD-NTF-045` (DND/preference block) are raised by the dialler/scheduler; `LD-AGT-015` is the agent-facing wrapper (P09).

---

## J.6 Call recording consent and network-side AI

### J.6.1 Recording

| Point | Rule |
|---|---|
| Law | No Indian statute found that requires all-party consent for a participant to record; the Telecommunications Act 2023 governs State interception [K]. Recordings are personal data: DPDP notice and consent/legitimate use for the stated purpose (ss.5–7, from 13 May 2027) [K]. Evidential use depends on relevance and authenticity; electronic records need the BSA 2023 s.63(4) certificate (R3 LG-091). [VERIFY current Supreme Court authority on recorded-call admissibility] |
| First utterance (every recorded call) | "This call is from LawDocs and is recorded. Say 'stop recording' to continue without recording." + AI disclosure where an AI voice is used (`dsc.ai.voice_start`, Appendix H §H.7) |
| Advocate–client consultations | Recording **OFF by default**; ON only if both opt in in-app; privilege notice (BSA 2023 s.132 [K, VERIFY]); summaries only from consented recordings and approved by the professional |
| Storage | LawDocs S3 ap-south-1/2; SHA-256 per file; Object Lock where evidential; vendor copies deleted after export (confirmation logged) |
| Retention by purpose | Sales 90 days; support 180 days; evidential (user-designated) per matter retention; consultation recordings per engagement terms — all settings (`ntf.recording.retention_days.<purpose>`) |
| Access | Purpose-bound roles; every playback logged; no use for staff surveillance beyond declared QA sampling (NN-33) |

### J.6.2 Network-side AI (Jio AI Call Agent, TeleFrame)

The Jio AI Call Agent can transcribe and summarise ordinary PSTN calls for Jio subscribers (R4 §3.1 [V2]). For consultations, negotiations and grievance calls, LawDocs: (a) defaults to in-app VoIP/WebRTC; (b) reads a confidentiality script ("Please do not use call-recording or AI assistants, including features provided by your network"); (c) includes the same in consultation terms (P16). LawDocs cannot technically prevent network-side features on PSTN legs; the risk is disclosed, not hidden.

---

## J.7 Data residency for telecom data

| Data | Rule |
|---|---|
| SMS/RCS/WhatsApp content and metadata | Indian TSP/CPaaS; written India-processing commitment required for JioCX and Haptik (G3) — not stated on their sites [V] |
| WhatsApp | Meta Cloud API local storage `IN` for data at rest; data in use may transit for up to 60 minutes [K] — record in the transfer register (DPDP s.16, R3 LG-069) |
| Voice recordings, transcripts | LawDocs AWS ap-south-1/2 only (NN-25) |
| AI prompts/outputs in voice sessions | Bedrock India route only (P09 FR-P09-02) |
| Delivery reports, consent records, A2P declarations | LawDocs PostgreSQL (India); retention ≥ 1 year (DPDP r.6(e)) and per TRAI audit needs |
| Network-side AI | Outside LawDocs' control — notice only (§J.6.2) |

---

## J.8 Finbyx and Udofin (pointer only)

Jio services can serve the lending products, but their rules live in the Finbyx v1.5 and Udofin v1.2 packs and the Ecosystem Spec v1.1; LawDocs shares **no** telecom resources, headers, CLIs, consents or DLT PE with them (separate entities, NN-24; Reg. 25(6) contagion risk). Pointers from R4 §4.3: regulated lenders migrate service/transactional calls to the **1600-series** on TRAI's sector deadlines (banks 1 Jan 2026; large NBFCs, payments banks, SFBs 1 Feb 2026; remaining NBFCs, co-operative banks, RRBs 1 Mar 2026 [V2]) — Finbyx telephony needs a "lender-number mode"; Udofin as LSP calls on behalf of an RE only from the RE's 1600 series or a declared CLI under the RE's authorisation with the RE named in the first utterance [K — VERIFY RBI Digital Lending Directions 2025 clause]; RBI calling windows for borrower contact apply [K]; JioCX Verify and Haptik voice agents (housing-finance lead-qualification case study) are the strongest Jio fits for lenders. LawDocs-built adapters (`packages/connectors`) may be reused as shared code (OP-1) without sharing accounts.

---

## J.9 Decision table — use Jio or an alternative

| Need | Use Jio when… | Use the alternative when… | Default at Wave 1 |
|---|---|---|---|
| Signing-link delivery with verified sender to iPhone and Android | JioCX RCS passes DLR/read-receipt and DLT tests and Q13 (deep links) is confirmed | RCS unavailable on the handset or tests fail → SMS (-S) + email | Email + one SMS; RCS behind flag, pilot in Wave 1 end |
| OTP SMS | As secondary route for resilience | Primary DLT CPaaS (MSG91 [K]) remains primary | MSG91 primary, JioCX secondary after G1/G6 |
| WhatsApp utility messages and Vidhi on WhatsApp | JioCX WhatsApp offers better pricing/support and signed webhooks | Meta Cloud API via incumbent BSP | Incumbent BSP; JioCX in RFP |
| Branded caller ID | Pilot shows ≥ 10% uplift and coverage on non-Jio networks is confirmed | Coverage gaps → Truecaller for Business | Pilot both |
| Click-to-call with masking | JioCX C2C masking confirmed for both legs | Exotel masking | Exotel [K] |
| Second PSTN carrier | Always (SIP trunk) once MSA signed | — | Jio SIP as secondary |
| Toll-free legal-help line | Cost and IVR features acceptable | Exotel virtual toll-free | Jio toll-free |
| Multilingual AI voice intake agent | Haptik passes G1–G11, Q13–Q15 and supports BYO-LLM through LawDocs' Bedrock proxy | Any gate fails → ElevenLabs/Sarvam stack | ElevenLabs/Sarvam [K]; Haptik RFP |
| Indic STT/TTS/transliteration | Jio AI Cloud publishes API, price and India-only terms and wins the WER bake-off for a language | Otherwise Sarvam/Bhashini/Azure/Google India | Bake-off winner per language |
| LLM for Vidhi | Never at Wave 1–3 (no product) | Claude via Bedrock India (D-14) | Claude |
| Sovereign/on-premises AI for an Enterprise client | Client mandates Jio cloud and an open-weight model passes P09 admission | Client's own data centre or AWS dedicated cell | Not offered until requested [OWNER] |
| Video consultations | Never (JioMeet lacks embed/recording export API) | In-app WebRTC; Teams/Meet links | WebRTC |
| Export copy to an Indian data centre | Client wants Jio/Azure-in-India and region is attested | S3/Azure Blob/SharePoint/Drive (P20) | P20 targets |
| Security MSSP | Commercials and SOC operating model acceptable | Other MSSP; VAPT always by CERT-In-empanelled auditor | Evaluate in P23 |
| Local advertising | City launches, company-level offers | Other ad networks | OH decision |
| Marketing WhatsApp inbox | OH chooses Pulse over Brevo WhatsApp | Brevo | OH decision (outside LawDocs) |

---

## J.10 Settings (registered in Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `ntf.jiocx.sms_enabled` / `rcs_enabled` / `whatsapp_enabled` / `email_enabled` / `alerts_enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y (NN-38 verification-log link) |
| `ntf.voice.jiocx_enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y |
| `ntf.voice.branded_cli_jiocx_enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y |
| `ntf.telephony.jio_sip_enabled` | PLATFORM | bool | false | `PLT_SRE` | Y |
| `ntf.channel.failover_order` | PLATFORM | json | per channel | `PLT_SRE` | Y |
| `ntf.calling_window.service` | BRAND | json | 09:00–21:00 | `PLT_SUPER_ADMIN` | Y |
| `ntf.calling_window.promotional` | BRAND | json | 10:00–19:00 | `PLT_SUPER_ADMIN` | Y |
| `ntf.counterparty.max_unopened_invites` | PLATFORM | int | 1 (locked max 1) | — | — |
| `ntf.service_consent.validity_days` | PLATFORM | int | 7 (locked) | — | — |
| `ntf.inquiry_contact.max_days` | PLATFORM | int | 7 (locked) | — | — |
| `ntf.optout.cooldown_days` | PLATFORM | int | 90 (locked) | — | — |
| `ntf.recording.default` | BRAND | enum | ON with notice (consultations OFF) | `PLT_SUPER_ADMIN` | Y |
| `ntf.recording.retention_days.<purpose>` | BRAND | int | sales 90; support 180 | `PLT_DPO` | Y |
| `ntf.tenant_branded_mode.enabled` | TENANT | bool | false | `ORG_ADMIN` | Y (PE ID required) |
| `ai.voice_agent.haptik_enabled`, `ai.speech.jio_enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y |
| `xpt.storage.jio_azure_enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y |
| `ntf.user.channel_preferences` | USER | json | app + email | User | N |

Kill switches (NN-39): every key above has a corresponding platform switch; channel-level agent sends can also be blocked from P09's kill-switch board.

---

## J.11 Open items

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-R4-01 | Open developer.jiocx.com account; read auth, DLR/webhook and error pages; confirm HMAC and India processing | Integration lead | JioCX adapters OFF |
| OI-R4-02 | Gazette publication date of TCCCPR Third Amendment 2026 (commencement maths) | Compliance | Treat Reg. 4 as in force from 1 Dec 2026 |
| OI-R4-03 | 1600-series allotment to a non-BFSI service provider | Compliance + Jio account manager | Declared 10-digit A2P CLIs (service); 140 (promotional) |
| OI-R4-06 | Haptik RFP (EQ Q1–Q12 + Q13–Q15) | Procurement | ElevenLabs/Sarvam |
| OI-R4-07 | Jio Platforms RHP / IMC 2026: committed enterprise-AI APIs | Research | Watch-list |
| OI-R4-10 | RCS DLT treatment (header/template registration for A2P RCS) | Compliance | Treat RCS like SMS for consent and templates |
| OI-R4-11 | JioCX Verify coverage on Airtel/Vi handsets | Jio account manager | Truecaller for Business in parallel |
| OI-J-01 | Whether a counterparty signing invitation qualifies as a "service" message under TCCCPR categories | [COUNSEL] / Compliance | Email + initiator's own share sheet only |
| OI-J-02 | Whether human-initiated click-to-call through a CPaaS flow is outside "A2P" (Reg. 2(ea)) | Compliance with TSP | Declare C2C CLIs as A2P anyway |
| OI-J-03 | DCA (digital consent acquisition) availability for non-bank PEs | Compliance | Consent captured in LawDocs and stored with evidence |

## J.12 Sources

R4 §2–§5 and §13 sources 1–40 (all accessed 25 Oct 2026: jio.com/business product pages; jiocx.com and developer.jiocx.com; haptik.ai; TRAI Regulation_18092026.pdf; PIB 18 Sep 2026; TRAI PR 11/2025; TRAI directions 20/30 Aug 2024; RCS pricing reports 9 Sep 2026); R3 LG-061–063, LG-069, LG-078, LG-091, LG-149; EQ Appendix T §4 (sister pack, [K]); Conventions NN-34, CH-17, §13 item 14 and 19.
