# R4 — Reliance Jio Business, Agentic AI, and Autopilot Growth (Research Stream R4)

> **Pack:** LawDocs (lawdocs.in) Build Prompt Pack · **Stream:** R4 · **Prepared:** 25 October 2026 · **Consumers:** master §8 (vendor stack), Vidhi AI phase, Communications/Notifications phase, Operations Hub & Marketing phase, Marketplace phase, Integration Gateway phase.
>
> **Builds on (re-verified, not repeated):** Equator Appendix T §4 (Jio AI evaluation, 21 Oct 2026); LawDocsComply Appendix AA (future-ready agentic architecture) and Appendix K (Vidhi agent specification). Where this stream finds a newer or different fact, it is recorded as a **delta** in §0.3 — downstream LawDocs files must use the R4 value.
>
> **Method and limits.** Live sources were read with WebSearch/WebFetch on 25 Oct 2026. jio.com/business, jiocx.com, developer.jiocx.com, haptik.ai, trai.gov.in, pib.gov.in, platform.claude.com, anthropic.com, aws.amazon.com and the competitor homepages were fetched directly. The session's web-search quota was exhausted part-way through the benchmark section; remaining benchmark facts come from direct fetches of vendor homepages, and one item (NyayGPT) could not be checked at all and is marked [U]. No curl/python bypass was used.

---

## 0. Scope, evidence tags and reconciliations

### 0.1 Evidence tags

| Tag | Meaning |
|---|---|
| **[V]** | Read on the primary/official page in this session (25 Oct 2026) |
| **[V2]** | Read on a reputable secondary source (news, law-firm note) in this session |
| **[K]** | Carried from the sister packs or prior knowledge; not re-read in this session — treat as **[VERIFY]** before it becomes product copy or a contract term |
| **[U]** | Unverified claim; do not rely |
| **[VERIFY]** | Must be confirmed with the vendor/regulator before build or publication |

### 0.2 Scope

Jio Business catalogue and integration routes; TRAI/DLT, recording and residency constraints; late-2026 agentic-AI baseline and Vidhi roster; PTSTDM funnel teardown and the LawDocs autopilot growth blueprint.

### 0.3 Deltas against the sister packs (binding for LawDocs)

| # | Topic | Sister-pack statement | R4 finding (25 Oct 2026) | Consequence for LawDocs |
|---|---|---|---|---|
| D-R4-01 | **JioCX API documentation** | EQ T §4.1: "No public API reference" | **A public developer portal exists**: developer.jiocx.com with quick-start guides for SMS, RCS, Email, Voice (Click-to-Call, Missed Call, Smart IVR, OBD) and WhatsApp; EasyPhone "coming soon". SMS testing allowance: **100 free SMS/month**; full access through sales@jiocx.com. Detailed endpoint/auth pages sit behind sign-up [V] | Gate G1 ("written API specification + sandbox") is **partially met** for JioCX. Move JioCX from "no docs" to "docs behind sign-up; sandbox credit available". Engineering should open a developer account and read the authentication and DLR pages before the RFP. |
| D-R4-02 | **JioCX security** | EQ: certifications not stated | jiocx.com/security lists **ISO/IEC 27001:2022, ISO 22301:2019, SOC 2 (type not stated), CERT-In**, ISO 27701; encryption in transit and at rest. **No data-residency statement, no DPDP statement, no retention period, no sub-processor list** [V] | G7 partly evidenced; G2–G4 (DPA, India-only processing, no training/retention) are still open. |
| D-R4-03 | **JioCX Pulse** | Not covered | A WhatsApp platform (Jio Things Ltd) with broadcasts, shared inbox, no-code bot builder (5 bots on entry plan), FAQ-trained AI bot with human hand-off, in-chat payments, WhatsApp Forms, 22 regional languages, 7-day free trial; no published INR prices [V] | A credible Interakt-class alternative for LawDocs's **internal** marketing/support WhatsApp; never a substitute for LawDocs's own CRM (owner brief: "own system, not third-party tools"). |
| D-R4-04 | **RCS on iPhone** | Not covered | Jio says it is the **"exclusive RCS provider for iOS in India"**; Apple's business messaging is live in India; Jio RCS moved from a flat ₹0.08–0.10 to tiered pricing: marketing ₹0.27–0.30, transactional ₹0.25, OTP ₹0.11–0.16 per message (9 Sep 2026) [V2] | RCS becomes a realistic **verified-sender channel for signing links** to both Android and iPhone users; price is now close to SMS + WhatsApp utility. |
| D-R4-05 | **TCCCPR Third Amendment** | EQ cites "No. 05 of 2026, 18 Sep 2026" | **Confirmed** on the TRAI gazette PDF: *Telecom Commercial Communications Customer Preference (Third Amendment) Regulations, 2026* (05 of 2026), RG-25/(25)/2023-QoS, dated 18 Sep 2026; commencement **30 / 60 / 90 days after Gazette publication** by provision (Reg. 1(3)) [V] | A2P-declaration (Reg. 4) applies 60 days after publication — on current information **around late November 2026** [VERIFY Gazette date]. LawDocs must declare every automated-calling CLI before go-live. |
| D-R4-06 | **Bedrock India date** | LDC: announced 29 Sep 2026; EQ: 5 Oct 2026 | **Both are right**: AWS ML Blog post dated **29 Sep 2026**; Anthropic/press announcement reported **5 Oct 2026** (CRN Asia). India geographic profile prefix **`in.`**, routing only ap-south-1 ⇄ ap-south-2; models **Opus 5, Sonnet 5, Haiku 4.5** [V] | Cite the AWS blog (29 Sep) as the primary source. |
| D-R4-07 | **Claude model generation** | LDC/EQ: Opus 5 / Sonnet 5 / Haiku 4.5 | Anthropic API now lists **Claude Opus 5.5 (`claude-opus-5-5`, 22 Sep 2026, $4/$20 per MTok, 1M context)**, **Sonnet 5.5 (`claude-sonnet-5-5`, 28 Sep 2026)**, **Haiku 5.5 (`claude-haiku-5-5`, 7 Oct 2026, 1M context)**; Sonnet 4.5 retires 30 Nov 2026 [V]. The **5.5 models are not yet shown on the Bedrock India `in.` profile** in any source read [VERIFY] | Model registry must carry both generations: 5.5 on the global API (public/non-personal data only) and 5 / Haiku 4.5 on Bedrock India for personal data until AWS lists 5.5 under `in.`. Never hard-code model names (LDC FP-01 already requires this). |
| D-R4-08 | **MCP version** | LDC AA: spec 2025-11-25 | **MCP 2026-07-28 specification released 28 Jul 2026**: stateless core (no `initialize` handshake, no `Mcp-Session-Id`), `server/discover`, multi-round-trip requests replacing server-initiated sampling/elicitation, `Mcp-Method`/`Mcp-Name` routing headers, cacheable lists, formal **extensions** (Tasks, MCP Apps, Enterprise-Managed Authorization), RFC 9207 issuer validation, Client ID Metadata Documents preferred over Dynamic Client Registration; Roots, Sampling, Logging and HTTP+SSE deprecated (≥ 12-month window) [V] | LawDocs's MCP server targets **2026-07-28** with 2025-11-25 back-compat for one year. |
| D-R4-09 | **Anthropic Usage Policy — legal** | Not analysed in either pack | New AUP version **effective 12 Nov 2026**. "Legal" is a High-risk Area covering **"advising an individual on their legal rights, obligations, or liability, or on what to do in a specific legal matter, or preparing legal documents for them to sign or file."** A qualified person must **meaningfully review** the recommendation before delivery, with authority to change it, and the individual must be **told AI was used**. Exclusions: general information that does not apply the law to the person's circumstances; internal drafting/research that is not the ultimate recommendation [V] | **The single most important AI finding for LawDocs.** "Free AI draft on every page" for individuals cannot be delivered as a sign-ready document without a qualified-review gate. See §6.4. |
| D-R4-10 | **Reliance AI enterprise products** | EQ: REIL announced, no product | Still **no public REIL product, API or price**. REIL CEO appointed 23 Apr 2026 (Parminder Singh); a go-to-market head joined Sep 2026; FY26 annual report (28 May 2026) describes Llama-based enterprise/SMB tools as plans; Jio "partners with REIL to distribute enterprise AI products" (Angel One, 17 Oct 2026) [V/V2] | Watch-list unchanged. Re-check after Jio Platforms listing (tentatively 28 Oct 2026). |
| D-R4-11 | **Haptik security** | EQ: residency not stated | Haptik's security page: deployed on **Azure & AWS**, regions not named; ISO/IEC 27001:2022, HIPAA, FIPS 140-2 encryption, GDPR/CCPA/PDPA alignment; **no DPDP, retention or no-training statement**; voice agents claim "100+ languages", sub-second latency, BYO-LLM ("integrate your own LLMs"), model choice incl. Claude [V] | BYO-LLM claim improves Haptik's RFP position (Q3); residency/DPA gaps remain. |

---

## 1. Executive summary

1. **Jio is a carrier and CPaaS for LawDocs, not an AI-model supplier.** Contractable today: SIP trunk, toll-free, IP Centrex, JioCX (SMS, Voice/IVR/OBD/C2C/missed call, RCS, WhatsApp, Email, Alerts, Verify, EasyPhone, Pulse), Haptik agents, JioCloud compute/GPU, security services, JioAds. Not contractable: JioBrain (internal network AI), Reliance Intelligence/REIL (no product), AGM-2026 consumer apps.
2. **Best fits:** JioCX **RCS** (verified-sender signing links, now reaching iPhones), **Verify** (branded caller ID on nudge calls), **Voice** (C2C, IVR, missed call), **SIP trunk** (second carrier), **Haptik** (RFP challenger for a multilingual intake voice agent).
3. **Vidhi stays on Claude** — Bedrock India `in.` for personal data, Anthropic API for public content only.
4. **Telecom law tightened in 2026:** every automated call is an A2P call that must be pre-declared with its CLIs (Third Amendment 2026, Reg. 4); inquiry-based contact lasts 7 days.
5. **Counterparties are not customers:** "send-it-yourself" sharing, one LawDocs email + one service message, no automated voice until the counterparty opts in (§5.6).
6. **Anthropic's usage policy (eff. 12 Nov 2026) makes preparing documents for an individual to sign High-risk legal** — LawDocs needs a **Qualified Review Gate** and two-lane drafting (§6.4).
7. **21 Vidhi role agents** specified on the LDC L0–L4 model (§7).
8. **PTSTDM** is a GTM-tracked ₹99 tripwire funnel with per-source pages, value stack, live-only urgency and 24-hour refund; copy the mechanics, not its inconsistent anchors or unevidenced scarcity (dark-pattern risk).
9. **Autopilot = own CRM + Brevo + JioCX/RCS + inbound-only AI SDR**, bounded by BCI Rule 36: market the platform, never individual advocates.

---

## 2. Jio Business — directory map (verified 25 Oct 2026)

### 2.1 Navigation as published on jio.com/business [V]

- **Product families:** Business Solutions · Connectivity · Voice & Collaboration · Cloud Infrastructure · Application Modernization · Data Center Transformation · Analytics, Insights, AI · Security · Management · GPU Accelerated Computing · **CPaaS – JioCX** · Mobile · Internet of Things · Marketing Solution.
- **Segments:** Startup · MSME · Large Enterprise · Government (FAQ also refers to Strategic and Large Groups, SMBs and micro businesses).
- **Industries:** BFSI · Manufacturing · Education · Retail · Logistics · Healthcare.
- **Resources:** 130 items (filter types Article, Case Study, Infographic, Leaflet, Service Video, Use Case, Whitepaper); **none of the first page concerns AI, BFSI, DLT or telemarketing**; plus Press release, Regulatory, Policies, T&C.
- **Separate sites:** jio.com/enterprisecloud (Jio Enterprise AI Cloud), jiocx.com (JioCX marketing site, solutions, resources), developer.jiocx.com (APIs), haptik.ai (Jio Haptik), jio.com/jioads (advertising).
- **Buying route for nearly everything:** "Request a callback" form with OTP → assisted sale → CAF/enterprise KYC/order form [K]; self-care at enterprise.jio.com.
- **No developer/API link anywhere on jio.com/business.** The only developer portal found is JioCX's.

### 2.2 Government segment [V]

Lists ILL, MPLS VPN, Cloud Connect, JioConnect, IoT for PSU factories, AI + ML, and the security suite. **No MeitY empanelment, sovereign-cloud certificate or GeM listing is claimed on the page.** Relevance to LawDocs: none directly; relevant to LawDocsComply/Equator public-sector tenders only after Jio states empanelment [VERIFY].

---

## 3. Jio service catalogue for LawDocs (and Finbyx/Udofin)

Status key: **VERIFIED** = product page read in this session; **[VERIFY]** = exists but a material detail (API, price, residency, terms) is unconfirmed. "Route" is the integration path LawDocs would take.

| # | Service | URL | Capability (as published) | LawDocs use — client-facing | LawDocs use — internal ops | Finbyx / Udofin relevance | API availability / route | Status |
|---|---|---|---|---|---|---|---|---|
| J-01 | **JioCX SMS** | jio.com/business/services/cpaas/products/jiocx-sms/ · jiocx.com/products/bulk-sms-marketing | High-volume, time-sensitive SMS; usage-based ("pay only for what you send") | OTP fallback; signing-link and payment-link service messages (-S/-T headers); hearing-date and TM-deadline alerts | Staff alerts; ops-hub SLA breach alerts | EMI/sanction/disbursal alerts; 1600/-T headers | **API** (developer.jiocx.com SMS quick start; credentials → token → send; requires DLT template; 100 free SMS/month in testing) | VERIFIED (docs behind sign-up) |
| J-02 | **JioCX Voice** | jio.com/business/services/cpaas/products/jiocx-voice/ · jiocx.com/products/voice-messaging-solution | OBD (pre-recorded), IVR (voice + DTMF), Click-to-Call, Missed Call, Voice OTP (TTS), campaign portal, real-time DLRs/analytics, on-demand channels; FAQ titles mention virtual numbers, porting, recording, webhooks | **C2C** from an advocate profile ("Talk to the assigned advocate" without exposing numbers — masking via virtual number/flow [VERIFY]); **missed-call** "call me back for help"; **IVR** helpline with language menu; Voice OTP for low-literacy users | Telecalling team C2C from CRM; IVR routing to ops hub queues | Collections/servicing IVR; C2C for RMs (lender's 1600 CLI) | **API** (C2C quick start needs a **Flow ID** and a JioCX-issued **virtual number**); IVR/OBD via portal or API [VERIFY endpoints] | VERIFIED |
| J-03 | **JioCX RCS** | jio.com/business/services/cpaas/products/jiocx-rcs/ · jiocx.com/products/rcs-messaging-api | Rich cards, carousels, quick replies, action buttons, verified business profile; via Jio–Google and Jio–Apple partnerships; Jio "exclusive RCS provider for iOS in India"; tiered pricing ₹0.25 transactional / ₹0.27–0.30 marketing / ₹0.11–0.16 OTP | **Signing-link card** ("Review & eSign" button, verified LawDocs sender) to Android **and iPhone**; payment-link cards; hearing reminders with "Add to calendar" | Campaigns to consented leads | Sanction letter/KFS acknowledgement cards; EMI reminders | **API** (developer.jiocx.com/rcs) | VERIFIED (pricing [V2]) |
| J-04 | **JioCX WhatsApp** | jio.com/business/services/cpaas/products/jiocx-whatsapp/ · developer.jiocx.com/whatsapp/getting-started | WhatsApp Business Platform onboarding (support number → Business Portfolio → form → register → Meta verification → API docs → testing) | Utility templates for opted-in users: signing status, document ready, payment receipt; Vidhi chat on WhatsApp (opt-in) | Support desk channel | Borrower servicing (Udofin) | **API** (BSP-style onboarding; endpoint/auth pages behind sign-up) | VERIFIED |
| J-05 | **JioCX Pulse** | jiocx.com/products/pulse | WhatsApp platform: broadcasts (opted-in), shared inbox, no-code bot builder, FAQ AI bot with escalation, payments in chat, Forms, 22 languages, 7-day trial | — (LawDocs's own app must be the system of record) | Optional **marketing/support inbox** for the growth team if Brevo WhatsApp proves weak | SMB lenders' collections inbox | SaaS; integrations menu, API not described | VERIFIED; pricing [VERIFY] |
| J-06 | **JioCX Email** | jio.com/business/services/cpaas/products/jiocx-email/ · developer.jiocx.com/email | No-code transactional + promotional email | Secondary transactional email route (fallback to SES/Brevo) | — | Statements, notices | **API** (email quick start) | VERIFIED |
| J-07 | **JioCX Alerts** | jio.com/business/services/cpaas/products/jiocx-alerts/ | Omnichannel emergency/verified notifications (SMS, Voice, Email, WhatsApp, RCS) | Platform-incident notices to tenants (CERT-In/DPDP breach communication fan-out) | Incident response broadcast | Same | Product; API [VERIFY] | VERIFIED |
| J-08 | **JioCX Verify** | jio.com/business/services/cpaas/business-solutions/jiocx-verify/ · jiocx.com/products/verify | Branded caller ID — verified brand name shown instead of "Unknown caller" | Brand "LawDocs" on signing-nudge, payment and advocate-callback calls; reduces fraud fear ("is this a scam?") | Telecalling answer-rate uplift | **High** for collections/servicing calls | Product; coverage on non-Jio networks [VERIFY] | VERIFIED |
| J-09 | **JioCX EasyPhone** | jio.com/business/services/cpaas/business-solutions/jiocx-easyphone/ | Cloud business phone: virtual number, call management, real-time tracking; developer API "coming soon" | Single LawDocs helpline number | **WFH relationship managers**: calls on a business number from their own phones, logged (owner brief: RMs work from home, performance measured) | DSA/field teams | SaaS; API coming soon | VERIFIED |
| J-10 | **JioCX EasyListing** | jio.com/business/services/cpaas/business-solutions/jiocx-easylisting/ | Directory listings with SEO-optimised profiles | Local SEO for Delhi/Noida/Jaipur offices (LawDocs as a company, **not** advocates — BCI Rule 36) | Review management (see §10.9) | Branch listings | SaaS | VERIFIED |
| J-11 | **Jio Haptik — AI Agents / Voice AI Agents** | haptik.ai · haptik.ai/voice-ai-agents · haptik.ai/platform/enterprise-security | Customer-service, sales, booking, lead-qualification agents; Agent Studio; voice agents inbound/outbound, "100+ languages", human hand-off with summary, CRM/payment/WhatsApp integrations via REST, "integrate your own LLMs"; housing-finance voice loan-qualification case study; Azure/AWS hosting, regions not named; ISO 27001:2022 | Candidate engine for the **multilingual legal-intake voice line** and inbound "where is my document?" bot | **AI SDR** for inbound leads (callback within 5 minutes) | **Strong** — lead qualification, payment reminders for NBFCs; housing-finance proof point | Sales-led; demo; **no public docs/pricing**; SMB WhatsApp agents from ₹10,000 (Sep 2025) [K] | VERIFIED (capability); residency/DPA [VERIFY] |
| J-12 | **Haptik Interakt / Contakt** | haptik.ai/interakt | WhatsApp-first marketing CRM (Interakt); Contakt named only | — | Optional WhatsApp marketing tool | SMB lenders | SaaS | VERIFIED (named); detail [VERIFY] |
| J-13 | **SIP Trunk** | jio.com/business/services/voice-and-collaboration/sip-trunk/ | 10–10,000 simultaneous sessions over one link to an IP-PBX | — | **Second PSTN carrier** behind the AI voice stack (Exotel/ElevenLabs primary per pack) | Collections dialler carriage | Order form (CAF/MSA) | VERIFIED |
| J-14 | **Toll-Free** | jio.com/business/services/voice-and-collaboration/toll-free-number/ | Single national virtual number free for callers | "1800" legal-help line (grievance/loan-complaint vertical — owner brief) | — | Grievance line for REs | Order form | VERIFIED |
| J-15 | **IP Centrex** | jio.com/business/services/voice-and-collaboration/ip-centrex/ | Cloud PBX, fixed-mobile convergence | — | Office telephony Delhi/Noida/Jaipur | Branch telephony | Order form | VERIFIED |
| J-16 | **JioMeet** | jio.com/business/services/voice-and-collaboration/jio-meet/ | HD video, up to 1,000 participants | Not for consultations (no embed/recording-export API) — LawDocs uses Teams (owner's M365) or in-app WebRTC | — | — | No API published | VERIFIED; **reject** |
| J-17 | **JioCloud (Microsoft Azure through JioCloud) — AI + ML** | jio.com/business/services/jio-cloud/data-analytics/ai-machine-learning/ · jio.com/business/offer/jiocloud-azure/ | Azure AI services ("Jio Azure cognitive services": vision, speech, language, decision), Azure ML, GPU/FPGA/CPU; **no Azure OpenAI or LLM listed; regions not named** | — | Possible **export destination** for client data packs (Azure Blob in "Jio Regions") when a client asks for an Indian data-centre copy | Lender analytics | Callback form (OTP) | VERIFIED; regions [VERIFY] |
| J-18 | **Jio Enterprise AI Cloud** | jio.com/enterprisecloud/services/ai-cloud/ · /pricing/ | NVIDIA H200 and AMD (ROCm) GPU worker nodes, bare-metal and GPU VMs; AI Cognitive Services (inferencing, translation, STT, speech translation, TTS, transcription, transliteration — Indian-language focus); AI Workbench; "Indian data stays in India"; **no model catalogue, no prices on the pricing page, no certifications named** | Indic STT/TTS/transliteration **challenger to Sarvam/Bhashini** for type-copy and voice | Sovereign route R3 hosting for an open-weight model (LDC AA.15) if a client demands it | Same | Contact form; no public API reference | VERIFIED (capability); API/price [VERIFY] |
| J-19 | **GPU Accelerated Computing** | jio.com/business/services/jio-cloud/gpu-accelerated-computing/ | "Nvidia GPUs" on Jio sovereign cloud built on Azure tech, "fully housed in India"; subscriptions save "up to 20%" | — | Not needed (Vidhi uses managed Claude); keep for R3 sovereign route evaluation | — | Enquire/callback | VERIFIED |
| J-20 | **Security — vCISO, CyberSOC, TVM, NetSensor, DDoS** | jio.com/business/services/security/ (+ /vciso/, /cybersoc/, /threat-and-vulnerability-management/, /netsensor/, /ddos-mitigation/) | vCISO aligned to ISO 27001, NIST, GDPR, PCI DSS, **DPDP**; CyberSOC "real-time threat detection" (no operating model published) | — | **MSSP candidate** for LawDocs's SOC 2 / ISO 27001 / PCI-DSS programme (owner brief); CERT-In empanelment **not stated** — VAPT must still use a CERT-In-empanelled auditor | RE cyber programmes (RBI IT governance) | Callback form | VERIFIED |
| J-21 | **JioAds (incl. GoLocal)** | jio.com/jioads | Video, display, connected devices, in-store, DOOH, audio, coupons; 480M reach claim; segments incl. "EMI holders", "stock market traders"; **GoLocal** PIN-code targeting with AI creative templates; dashboard reporting | Hyper-local campaigns for city launches (Delhi NCR, Jaipur); vehicle-sale-agreement and challan offers to car-owner segments | Media-buying channel | Udofin borrower acquisition (subject to RBI DL Directions on LSP marketing) | Contact sales; no API, no self-serve confirmed; **JioAdsXchange not found** in any source read | VERIFIED (JioAds); JioAdsXchange [U] |
| J-22 | **Jio DLT (operator portal)** | [K] trueconnect.jio.com | Principal Entity, header, template, consent registration; telemarketer binding | Mandatory for all LawDocs SMS/voice | — | Mandatory | Operator portal | [K] [VERIFY URL] |
| J-23 | **Other: JioAttendance, JioPC, connectivity** | jio.com/business menus; TechCrunch 2 Sep 2026 (JioPC) | JioAttendance (named only); JioPC cloud PC from ₹1,000/2 months, consumer plans only; ILL/SD-WAN/5G | — | Not adopted (owner wants own HRMS); JioPC as WFH thin client [VERIFY business plan]; office links | Branch connectivity | SaaS / order form | Named / [V2] |

### 3.1 Reliance/Jio AI initiatives 2025–2026 (what is and is not usable)

| Initiative | Facts (dated) | Usable by LawDocs? |
|---|---|---|
| **Reliance Intelligence Ltd** | Wholly owned RIL subsidiary announced at 48th AGM (29 Aug 2025) to build AI for consumers, SMBs and enterprises, with "full-stack environments" to customise, deploy and govern generative models [V2]; at 49th AGM (19 Jun 2026) described as moving "from planning to execution" [V2] | No product to contract |
| **REIL (Reliance Enterprise Intelligence Ltd)** | JV 70:30 Reliance Intelligence : Meta; initial ₹855 crore; Llama-based enterprise AI PaaS; CEO Parminder Singh appointed 23 Apr 2026; GTM head Sep 2026; no named product, customer, residency term or price [V] | **Watch-list** |
| **Google Cloud – Jamnagar** | Cloud region in Jamnagar to host compute and AI services (29 Aug 2025); no rollout date [V2] | No; LawDocs buys AWS (pack default) |
| **Meta – Jamnagar capacity** | Meta to use capacity in a 168 MW AI-enabled Jamnagar DC (Jun 2026) [V2] | No |
| **Jamnagar AI data centres** | > 120 MW AI-ready capacity targeted H2 2026; gigawatt ambition [V2] | Indirect (future Indian GPU capacity) |
| **JioBrain** | Described (Oct 2026) as a proprietary AI engine embedded in Jio's network operations — capacity allocation, fault prediction, optimisation [V2]. The Startupory "public API" claim remains **[U]** | **No** — not an enterprise product |
| **AGM 2026 consumer AI** | JioBharat IQ, **AI Vyapar** (small merchants), JioHealth IQ, JioLearn IQ, JioKrishi IQ (22 languages); **Jio AI Call Agent** ("Hey Jio" on live calls: transcribe, identify up to 10 speakers, summarise, act); **Jio TeleFrame** (voice-first agentic OS, acts with permission, keeps an action record) [V2] | No integration; **risk**: network-side transcription of LawDocs advocate calls (§5.8) |
| **IMC 2026 (Oct 2026)** | "AI-Powered Enterprise Stack" (connectivity + cloud + AI for BFSI, government, etc.), Education Stack, JioAIHome, AI-native autonomous network [V2] | Re-check for an API after launch |
| **Jio Platforms IPO** | ₹30,213 crore fresh issue; 21–23 Oct 2026; listing tentatively 28 Oct 2026; RHP describes "enterprise solutions" and "AI-driven applications" [V2] | Read the RHP's business section for committed enterprise-AI products [VERIFY] |

**Posture (carried from EQ T §4.4, re-confirmed):** Adopt Jio as carrier (SIP), DLT registrar, secondary SMS/RCS route and branded-CLI pilot; **RFP-challenge** Haptik for voice/WhatsApp agents; watch-list REIL/JioBrain/Reliance Intelligence; reject JioMeet for consultations. **LawDocs-specific upgrade:** JioCX RCS moves to **primary verified-sender channel for signing links** once the DLR callback and DLT binding are tested, because of iPhone reach (D-R4-04).

### 3.2 Integration design (LawDocs ports)

Use the pack's port-and-adapter pattern (LDC Appendix L; EQ G11 replaceability). Jio adapters are flag-gated and never the only route.

| Port | Primary (pack) | Jio adapter | Flag (default OFF) | Activation preconditions |
|---|---|---|---|---|
| `SMS_PORT` | MSG91 [K] | `jiocx-sms` | `comms.jiocx.sms.enabled` | DLT PE/headers/templates bound to JioCX as telemarketer; authenticated DLR webhook live; 100-message sandbox test passed |
| `RCS_PORT` | — (new) | `jiocx-rcs` (primary) | `comms.jiocx.rcs.enabled` | Verified brand profile; template approval; DLR + read receipts; SMS fallback on non-RCS handsets |
| `WHATSAPP_PORT` | Meta Cloud API via BSP [K] | `jiocx-whatsapp` | `comms.jiocx.wa.enabled` | Meta business verification; utility templates approved; signed webhooks |
| `VOICE_PORT` (CPaaS) | Exotel India cluster [K] | `jiocx-voice` (C2C, IVR, missed call) | `voice.jiocx.enabled` | Flow IDs per use case; virtual numbers; A2P declaration filed (Reg. 4); recording-notice prompt in each language |
| `TELEPHONY_PORT` (SIP) | Exotel/Plivo | `jio-sip` | `telephony.jio_sip.enabled` | CAF/MSA; failover test; ≤ 70% carrier share (EQ JR-10) |
| `CALLER_ID_PORT` | Truecaller for Business [K] | `jiocx-verify` | `voice.branded_cli.jiocx.enabled` | Pilot shows ≥ 10% answer-rate uplift, zero impersonation complaints |
| `VOICE_AGENT_PORT` | ElevenLabs Agents + Claude via Bedrock proxy [K] | `haptik-voice` | `voice.agent.haptik.enabled` | Passes EQ gates G1–G11 incl. BYO-LLM through LawDocs's Bedrock proxy so case content never reaches a vendor LLM |
| `INDIC_SPEECH_PORT` | Sarvam [K] | `jio-ai-cloud-cognitive` | `ai.speech.jio.enabled` | Published API + price; India-only processing in writing; WER bake-off |

**RFP:** Re-use EQ T §4.5 questions Q1–Q12 with three LawDocs additions — **Q13** signing-link deep-link support in RCS/WhatsApp templates with URL whitelisting proof; **Q14** per-tenant sub-accounts (so a company tenant's own DLT headers can be used in "tenant-branded" mode); **Q15** privilege controls (no vendor human review of legal-consultation recordings).

---

## 4. Use-case design: what Jio-class channels do for LawDocs

### 4.1 Client-facing

| Use case | Channel sequence | Vendor | Consent basis | Notes |
|---|---|---|---|---|
| **Signing invitation to counterparty** | (1) "Send it yourself" WhatsApp/SMS share sheet from the initiator's phone; (2) LawDocs email; (3) one service SMS or RCS card | Device share; SES/Brevo; JioCX RCS/SMS | Initiator's instruction + legitimate use for performance of the transaction the counterparty is party to [VERIFY under TCCCPR "service" category] | No voice, no repeat SMS until the counterparty opts in on the signing page (§5.6) |
| **Signing nudges (opted-in signer)** | T+24h RCS/WhatsApp utility → T+72h SMS → T+5d AI voice call (declared A2P CLI, Verify branding) → T+7d human RM call (company tenants) | JioCX + voice agent | Explicit consent captured in signing flow; "remind me" toggles per channel | Stop all nudges on sign, decline or "stop" |
| **eStamp/payment pending** | RCS payment card → SMS with Razorpay link (whitelisted URL) | JioCX, Razorpay | Contract with the payer | URL must be whitelisted (TRAI Direction 20 Aug 2024) |
| **Multilingual legal intake** | Inbound IVR (language menu) → voice agent collects facts → creates a case in LawDocs → books a consultation → WhatsApp summary | Toll-free/IVR + voice agent | Caller-initiated; disclosure + recording notice in first utterance | Agent gives **general information only**; matter-specific advice routed to a qualified advocate (AUP §6.4) |
| **Advocate consultation call** | Click-to-Call from booking page; both legs masked by virtual number | JioCX C2C | Booking contract | Recording **off by default**; privilege notice; advise parties to disable network AI assistants (§5.8) |
| **Hearing-date / limitation / TM-deadline alerts** | App push → WhatsApp utility → SMS | JioCX | Service relationship (subscriber) | Dates only from the calendar engine (deterministic) |
| **Grievance vertical (loans/insurance)** | Toll-free → intake agent → case file → status updates | Toll-free + agent | Caller-initiated | Never contacts the lender/insurer's customers outbound for marketing |

### 4.2 Internal operations

- **Telecalling:** CRM click-to-call (JioCX C2C or EasyPhone numbers); every call logged with duration, disposition and consented recording; RM dashboards use the logs (owner brief: work measured).
- **AI SDR, support, marketing, incidents:** see LV-19 and LV-18 (§7), §11.4, and JioCX Alerts for DPDP breach fan-out (Rules 2025 r.7).

### 4.3 Finbyx / Udofin (lending) — Jio relevance

- **1600-series migration** is mandatory for regulated lenders: commercial banks 1 Jan 2026; large NBFCs, payments banks, SFBs 1 Feb 2026; remaining NBFCs, co-operative banks, RRBs 1 Mar 2026; MFs/AMCs, CRAs, pension fund managers 15 Feb 2026; QSBs 15 Mar 2026; insurers to be notified (TRAI direction reported 19 Nov 2025) [V2]. Finbyx's telephony module must support **lender-number mode** (the RE's own 1600xx CLI) and refuse 10-digit CLIs for service calls.
- **Udofin as LSP** calls on behalf of partner REs: calls must originate from the RE's 1600 series or the LSP's declared CLI under the RE's authorisation, with the RE named in the first utterance [K — RBI Digital Lending Directions 2025, VERIFY clause].
- **JioCX Verify** and **Haptik voice agents** (housing-finance lead-qualification case study) are the strongest Jio fits for Finbyx/Udofin; collections calls must also respect RBI calling-hour limits (08:00–19:00) [K].
- 1600xx/1601xx CLIs **cannot be spam-tagged by call-management apps** (Reg. 34A, Third Amendment 2026) — a concrete answer-rate benefit for REs.

---

## 5. TRAI / DLT and telecom constraints

### 5.1 Instrument chain (as of 25 Oct 2026)

| Instrument | Date | What it does (LawDocs-relevant) | Tag |
|---|---|---|---|
| **TCCCPR 2018** (TRAI Regulation 6 of 2018) | 19 Jul 2018 | DLT-based framework: Principal Entity (sender) registration, headers, content templates, consent and preference registers, scrubbing against DND preferences | [K] |
| **TRAI Directions** | 20 Aug 2024 (revised 30 Aug 2024) | **140-series voice on DLT end-to-end by 30 Sep 2024**; **only whitelisted URLs/APKs/OTT links from 1 Oct 2024**; message **traceability from PE to recipient from 1 Nov 2024**; one template ↔ one header; template blacklisting for mis-categorisation | [V2] |
| **TCCCPR (Amendment) 2025** | Press release 12 Feb 2025 | 140-series for promotional, **1600-series for service/transactional calls**; 10-digit numbers barred for telemarketing; header suffixes **-P / -S / -T / -G**; complaint window 7 days; action at 5 complaints in 10 days; first violation: 15-day bar on all sender resources; repeat: 1-year disconnection and blacklisting; mandatory opt-out in promotional messages; no re-seeking consent for 90 days after opt-out; transaction-related consent valid 7 days; robocall/auto-dialler use must be disclosed | [V] |
| **TRAI direction on BFSI 1600-series** | Reported 19 Nov 2025 | Sector-wise deadlines (§4.3) | [V2] |
| **TCCCPR (Third Amendment) 2026, No. 05 of 2026** | 18 Sep 2026 (commencement 30/60/90 days after Gazette) | See §5.2 | [V] |
| **DPDP Act 2023 + DPDP Rules 2025** | Rules notified 13 Nov 2025; Consent Manager registration from 13 Nov 2026; core obligations (notice, security, breach, deletion, rights) from **13 May 2027** | TCCCPR consent ≠ DPDP consent (Third Amendment Reg. 2(k) Explanations); both must be captured | [V2] |

### 5.2 Third Amendment 2026 — clause points that change LawDocs's build [V]

| Clause | Rule | LawDocs implementation |
|---|---|---|
| Reg. 2(ea) | **A2P call** = call initiated by an application/software/automated platform without direct human dialling, incl. autodial, robo-call, pre-recorded or **artificial voice** | Every AI-voice, IVR-outbound and OBD call is A2P. A human RM pressing click-to-call is not A2P [VERIFY with TSP]. |
| Reg. 4 (replaced) | Sender must **declare A2P use and CLI ranges in advance** to the originating access provider; recorded on DLT; undeclared A2P calls = UCC | `voice.a2p_declarations` table (CLI, TSP, declaration ref, date, purpose); dialler refuses any CLI without an active declaration. |
| Reg. 35A | Terminating operator may charge up to **₹0.05/min** for A2P calls, **except** on 140xx, 1600xx, 1601xx | Cost model: AI voice on 10-digit declared CLIs costs more than on designated series. |
| Reg. 21A | TSPs flag high-probability UCC CLIs with AI/ML ("UCC_Detect") within 2 hours; 5+ flagged CLIs in 10 days → KYC re-verification (3 business days), then physical KYC (5 days), then 15-day bar | Monitor sender-notification SMS/email from the OAP; ops runbook to respond within 3 business days; keep KYC documents current. |
| Reg. 2(bb) | "Relationship" based on **inquiry** counts only if written/digital and kept verifiably; communication on it limited to **7 days**; application-based relationship limited to **3 months** | Lead record stores the inquiry artefact (form submission, WhatsApp opt-in message) with timestamp; marketing calls on that basis stop at day 7 unless explicit consent is registered. |
| Reg. 2(y), 2(k) | Explicit consent includes consent captured outside the operator's CRF **if registered in the Consent Register** per TRAI procedure; TCCCPR consent revocation does not revoke DPDP consent | Two consent objects: `telecom_consent` (registered with TSP DCA/consent register when the procedure is live) and `dpdp_consent` (purpose-wise). |
| Reg. 2(bh)(ii) | Explicit consent for **service messages** valid 7 days or until revoked; renewable in 7-day blocks | Signing-nudge consent is captured per document and expires 7 days after capture unless renewed in-flow ("keep reminding me"). |
| Reg. 22 | Misused header/template suspended within 6 hours; sender resets credentials and files a police complaint within 3 business days | Security runbook; DLT credentials in vault; maker–checker on template changes. |
| Reg. 25(6) | First violation: 15-day bar on all resources; subsequent: 1-year disconnection, blacklisting | Business-continuity risk: **never** let marketing traffic share CLIs/headers with transactional traffic. |
| Reg. 34A | Call-management apps may not tag/block designated commercial series | Prefer 1600/140 series where DoT will allot them to LawDocs [VERIFY eligibility of a non-BFSI entity for 1600]. |

### 5.3 DLT registration checklist (LawDocs and each group company)

1. **Principal Entity registration** on one operator DLT (e.g., Jio TrueConnect [K]) with PAN, GSTIN, CoI, authorisation letter; PE ID is honoured across operators.
2. **Headers**: separate for transactional (-T: OTP, payment), service (-S: signing status, hearing alerts), promotional (-P: offers) — e.g., `LAWDOC-S`, `LAWDOC-T`, `LAWDOC-P` [header format VERIFY].
3. **Content templates**: one header per template; variables only where allowed; **every URL domain whitelisted** (lawdocs.in, short-link domain, Razorpay, ESP domain).
4. **Telemarketer binding** (JioCX, MSG91, Exotel) and **chain declaration** (traceability).
5. **Voice**: 140-series for promotional voice; A2P CLI declaration for automated service calls; 1600-series application if eligible.
6. **Consent templates** (for consent acquisition via DCA once operational) [VERIFY DCA status for non-banks — pilot with 11 banks under the 10 Dec 2025 direction per Explanatory Memo].
7. **Tenant-branded mode**: a company tenant may send under its own PE/headers; LawDocs stores the tenant's PE ID and template IDs and refuses sends without them.

### 5.4 Calling hours

TCCCPR itself regulates by preference and category; LawDocs adopts **09:00–21:00 local time** for any service call and **10:00–19:00** for promotional calls as a conservative house rule [policy choice], and **08:00–19:00** for any lender-borrower contact via Finbyx/Udofin (RBI) [K]. Quiet-hours enforcement sits in the notification scheduler (LDC VG-14).

### 5.5 Call recording consent

- No Indian statute requires all-party consent for a participant to record; the Telecommunications Act 2023 governs State interception [K]. Recordings are **personal data** — DPDP s.5–6 notice and consent for the stated purpose [K]; evidential admissibility subject to relevance and authenticity [K — VERIFY current Supreme Court authority].
- **LawDocs rule:** first utterance: "This call is from LawDocs and is recorded. Say 'stop recording' to continue without recording." Recording **off for advocate–client consultations** unless both opt in (privilege, BSA 2023 s.132 [K]). SHA-256 per file; retention by purpose (sales 90 days, support 180 days); AI disclosure at session start (Anthropic AUP [V]).

### 5.6 Counterparty-contact rule (signing flows) — recommended binding rule `R4-COMMS-01`

1. The **initiator** chooses how to invite: (a) "Share from my phone" (wa.me / SMS deep link with a pre-filled message and the signing URL — user-to-user, not business messaging); (b) LawDocs email; (c) one LawDocs service SMS/RCS.
2. LawDocs sends **at most one** business-initiated message to a counterparty who has not opened the link.
3. On opening, the signing page shows a DPDP notice and **channel toggles** (WhatsApp / SMS / RCS / call reminders, preferred language, preferred time). Only toggled channels are used; consent expires 7 days after capture unless renewed (Reg. 2(bh)(ii)).
4. **No automated voice** to a counterparty who has not opted in.
5. Every message names the initiator ("Ravi Sharma has sent you a rental agreement via LawDocs") and contains an opt-out.

### 5.7 Data residency

| Data | Rule |
|---|---|
| SMS/RCS/WhatsApp content and metadata | Indian TSP/CPaaS; written India-processing commitment required for JioCX and Haptik (G3) — **not stated** on either site [V] |
| WhatsApp | Meta Cloud API local-storage `IN` for data at rest; data in use may transit for up to 60 minutes [K] |
| Voice recordings, transcripts | Stored in LawDocs's AWS ap-south-1/2 buckets (Object Lock where evidential); vendor copies deleted after export |
| AI prompts/outputs with personal data | Bedrock India `in.` profile only (§6.2) |
| Network-side AI (Jio AI Call Agent, TeleFrame) | Outside LawDocs's control — handled by notice (§5.8) |

### 5.8 Consumer-side network AI

The Jio AI Call Agent can transcribe and summarise ordinary PSTN calls for Jio subscribers [V2]. For advocate consultations, mediation-style negotiations and grievance calls, LawDocs (a) defaults to in-app VoIP/WebRTC, (b) reads a confidentiality script ("Please do not use call-recording or AI assistants, including features provided by your network"), (c) includes the same in the consultation terms. (Re-uses EQ T §4.9.)

---

## 6. Agentic AI baseline for a legal SaaS (late 2026)

### 6.1 Claude models and platform features [V unless marked]

| Item | State (25 Oct 2026) | LawDocs use |
|---|---|---|
| **Models (Anthropic API)** | Opus 5.5 (22 Sep 2026; $4/$20 per MTok; 1M context; adaptive thinking), Sonnet 5.5 (28 Sep 2026; on API, Bedrock, Google Cloud, Microsoft Foundry), Haiku 5.5 (7 Oct 2026; 1M context; 128k output); Opus 5 (24 Jul 2026; $5/$25), Sonnet 5 (30 Jun 2026; $2/$10). Sonnet 4.5 retires 30 Nov 2026. Restricted-access models (Fable/Mythos) not relevant | Planner/drafting = Opus tier; worker/extraction = Sonnet; classification/routing = Haiku |
| **Bedrock India** | `in.` geographic cross-Region profile (ap-south-1 ⇄ ap-south-2) for **Opus 5, Sonnet 5, Haiku 4.5**; "keeps inference within India"; no storage in destination Region; zero data retention by default but **flagged content may undergo AWS human review** for some models; Messages API, Converse, Guardrails, intelligent prompt routing supported (AWS blog 29 Sep 2026). Caching/batch/citations on `in.` not stated [VERIFY] | **Default route for any personal or client data** |
| **Python SDK 1.0** | 20 Aug 2026: removed Text Completions and `temperature`/`top_p`/`top_k` params | Pin SDK major versions; adapter hides SDK churn |
| **API version** | `2026-10-21` released with new SDK majors | Contract test in CI against the pinned version |
| **Tool use / structured outputs** | Structured outputs recommended over forced `tool_choice` | All Vidhi tool calls validated by JSON Schema |
| **MCP connector** | Inline MCP toolsets (`mcp-client-2026-09-15` beta) | Vidhi reaches tenant MCP servers (M365, Drive) without bespoke code |
| **Memory** | Managed Agents memory stores (Jul–Aug 2026) | Per-user preference memory only; matter facts live in LawDocs DB, not model memory |
| **Files API** | GA 19 Aug 2026; `expires_in_seconds`; pagination | Upload PDFs/scans once per run; set expiry ≤ 24 h |
| **Prompt caching** | Cache diagnostics GA (23 Sep 2026); compaction on demand (`compact-2026-09-04`); Sonnet 5.5 cache reads $0.10/MTok | Mandatory for system prompt + clause library prefixes |
| **Computer use** | `computer_toolset_20260801` GA (19 Aug 2026) | **Not** for government portals (eCourts, IP India) in v1 — use official data feeds; computer use only in sandboxed internal QA |
| **Agent Skills** | `/v1/skills` GA (19 Aug 2026); skills loadable from GitHub in Managed Agents | Package LawDocs drafting playbooks as versioned skills |
| **Web search/fetch controls** | Org-level domain controls (Oct 2026) | Research Associate restricted to allow-listed legal sources |
| **Code execution** | Generated media carries **C2PA** credentials (Sep 2026) | Aligns with IT Intermediary Amendment Rules 2026 labelling [K] |
| **`inference_geo`** | For Managed Agents (7 Aug 2026) | Evaluate once India appears as a geo [VERIFY] |
| **OpenTelemetry export** | Beta 14 Oct 2026 | Feeds LawDocs AI run ledger |
| **Citations, batch** | No 2026 change noted; batch remains the cheap path for nightly jobs [K] | TM-watch and order-digest batches overnight |

### 6.2 Routing rule for LawDocs (`R4-AI-01`)

```
if context.contains(personal_data or client_document or matter_data):
    route = bedrock.in   # Opus 5 / Sonnet 5 / Haiku 4.5 until 5.5 appears under in.
elif context.is_public_only:            # website help, public statutes, blog drafts
    route = anthropic.api  # 5.5 generation allowed
else: deny
record(route, model_id, region_pair, reason) in ai.run_ledger
```

### 6.3 Protocols

- **MCP 2026-07-28** (D-R4-08): LawDocs ships `ld-mcp` (read + propose tools: `search_documents`, `get_matter_status`, `draft_from_template`, `list_obligations`, `get_hearing_calendar`) for clients' Copilot/Claude/ChatGPT assistants, with Enterprise-Managed Authorization extension and Keycloak as authorisation server (LDC AA.7 pattern).
- **A2A v1.0** (Linux Foundation; Signed Agent Cards; AP2 extension; production on Azure AI Foundry and Bedrock AgentCore) [V2]: LawDocs publishes Agent Cards for the Litigation Clerk (to Equator for ADR hand-off), Obligation Tracker (to LawDocsComply), Loan-Document Agent (to Finbyx/Udofin). The Ecosystem Spec remains the data contract.

### 6.4 Anthropic Usage Policy — what it means for LawDocs (`R4-AI-02`, binding)

**Rule text (effective 12 Nov 2026) [V]:** Legal High-risk Area = advising an individual on legal rights/obligations/liability, on what to do in a specific matter, or **preparing legal documents for them to sign or file**. Requirements: (i) a qualified person **meaningfully reviews** the High-risk AI Recommendation **before delivery**, with authority to change it, and remains responsible; (ii) the individual is **clearly told AI was used**. Not covered: general information that explains the law without applying it to the person; internal drafting/research that is not the delivered recommendation; business operations not about a specific individual. Consumer-facing agents must disclose AI at least at session start. Agent builders are responsible for agents' tool actions.

**Design consequences:**

| LawDocs feature | Classification | Required design |
|---|---|---|
| "Draft this agreement free" on every SEO page (individuals) | **High-risk** (document to sign) | **Two-lane drafting**: (1) *Template lane* — lawyer-authored, versioned templates filled deterministically from the intake form; Claude may extract facts from the user's free text into fields and explain clauses in general terms, but the **document text comes from the approved template**; (2) *AI-custom lane* — Claude drafts bespoke clauses; output is locked as "AI draft — review required" and cannot be sent for eSign until the **Qualified Review Gate** records a review by a qualified person (LawDocs in-house/panel advocate; or, in a company tenant, a user who attests a legal qualification/role — CLO, CS, advocate). [VERIFY with Anthropic account team whether template-lane fact extraction is outside the High-risk definition] |
| Vidhi Q&A ("can my landlord keep my deposit?") | High-risk if applied to the person's facts | Free tier answers as **general information** with cited provisions and a "Book a 15-minute review" CTA; matter-specific advice only through a paid advocate consultation where the advocate reviews Vidhi's draft answer |
| Pleadings self-help, notice replies, grievance letters | High-risk (file/send) | QRG before download in "final" form; AI-use disclosure printed in the footer |
| Company legal team drafting (B2B) | Internal drafting by a qualified user is excluded until delivered to an individual; but a company's counterparty is not the "individual" being advised | Record reviewer identity and approval on every external send (already a maker–checker rule) |
| Contract review for a company, litigation tracking, TM watch, board minutes | Business operations / internal analysis | Normal guardrails |
| Disclosures | All | "Prepared with AI assistance; reviewed by [name, enrolment no.] on [date]" stamp; session-start AI notice in chat and voice |

The QRG is also the ethical answer to BCI expectations: the reviewing advocate is accountable, and LawDocs (not the advocate) is the product publisher.

### 6.5 Guardrails (carry LDC Appendix K/AA; LawDocs additions)

- **Autonomy L0–L4** exactly as LDC AA.3; LawDocs tenant agents capped at **L2**, notification agents **L3-eligible**; L4 platform-internal only.
- **Prohibited for every agent:** eSign, pay, file to a court/IP India/MCA portal, send an external legal notice, accept a marketplace engagement, change access, read the password tracker (owner's ops-hub credential page — vault-only, never in model context).
- **Prompt-injection defences:** uploaded WhatsApp screenshots, counterparty redlines and court orders are untrusted content — delimited, scanned, never allowed to trigger tools; output sanitiser strips external URLs (data exfiltration); MCP tool-description hashes pinned (LDC AA.17).
- **Evaluation:** per-agent golden sets (Indian contract types, Hindi + English first), citation validity 100%, number/date fidelity 100% in translations, QRG reviewer-edit rate tracked as the quality KPI (target: material edits < 15% after 90 days).
- **Kill switches** ≤ 60 s at platform, tenant, agent, skill, connector (LDC AA.17.2).

---

## 7. Vidhi agent roster for LawDocs

**Personas:** IND = individual; LT = company legal team/CLO; KMP = CS/CFO/CEO; BRD = directors/board; OPS = LawDocs operations hub; MKT = LawDocs growth team; PRO = marketplace professional. **AUP:** HR = High-risk legal (QRG applies); INT = internal/business operations; GEN = general information.

| ID | Agent | Persona(s) | Core tasks | Tools (action class) | Autonomy ceiling | Human approval points | AUP |
|---|---|---|---|---|---|---|---|
| LV-01 | **Contract Drafter** | IND, LT, PRO | Intake interview (chat/voice, 22 languages), fact extraction, template selection, clause drafting, eStamp duty estimate (from rules engine), IT Act First-Schedule exclusion check (e.g., contracts for sale/conveyance of immovable property and powers of attorney are outside eSign) [K] | `tpl.fill` (DRAFT), `cl.search`, `stamp.calc` (READ, deterministic), `dms.save_draft` (INTERNAL_WRITE_LOW) | L2 | QRG before eSign for AI-custom lane; user confirms every field | HR |
| LV-02 | **Redline Negotiator** | LT, IND, PRO | Compare counterparty version vs playbook, propose tracked changes and comment explanations, fallback positions | `dms.redline_docx` (DRAFT), `playbook.get` (READ) | L2 | User accepts each change; external send only by user | HR (IND) / INT (LT) |
| LV-03 | **Obligation Tracker** | LT, KMP, IND | Extract obligations, renewal/notice dates, lock-ins, payment schedules into calendar; reminders | `obl.extract` (PROPOSE), `cal.create_reminder` (INTERNAL_WRITE_LOW) | L3 (reminders) | Owner confirms extracted dates once per contract | INT |
| LV-04 | **Litigation Clerk** | LT, IND | Track cases (CNR/eCourts data feeds), next dates, cause lists, order downloads, matter timeline, limitation calculator (deterministic) | `courts.sync` (READ), `lit.update_timeline` (INTERNAL_WRITE_LOW), `limitation.calc` | L3 (sync, alerts) | Limitation dates shown with rule citation; advocate confirms | INT |
| LV-05 | **Order Digest & Hearing Prep** | LT, PRO, IND | Summarise orders/judgments, prepare hearing briefs, list documents to carry, chronology, issues | `dms.get_text`, `brief.draft` (DRAFT) | L1 | Advocate reviews brief; IND gets general summary only | HR (IND) / INT (PRO) |
| LV-06 | **Evidence & Type-copy Clerk** | IND, LT, PRO | OCR handwritten documents/WhatsApp screenshots, produce typed copies with originals preserved, page-mapped annexure index, translation into English, BSA s.63 certificate draft [K] | `ocr.run`, `translate.run`, `annex.build` (DRAFT) | L2 | User corrects and certifies each typed copy; certificate signed by human | INT (user certifies) |
| LV-07 | **Translator** | all | Translate documents/chats between English and the 22 Eighth-Schedule languages + UN languages; preserve numbers, dates, defined terms (LDC VG-16) | `translate.run`, `fidelity.check` | L2 | Human-certified translation workflow for court use | GEN/INT |
| LV-08 | **Research Associate** | PRO, LT | Statute/case research over allow-listed sources with pinpoint citations; "cite or decline" | `search.legal` (READ), `web.fetch` (allow-list) | L1 | Researcher validates citations | INT (internal) |
| LV-09 | **Notice Responder** | LT, IND | Classify incoming legal/regulatory notices, extract deadlines, draft reply skeletons, propose counsel assignment | `notice.classify`, `reply.draft` | L1 | Advocate signs every reply; deadline confirmed | HR |
| LV-10 | **TM Watch** | LT, IND (startups) | Track own applications (status, examination report deadlines, opposition windows), watch Trade Marks Journal for conflicting marks, draft response outlines | `ipindia.sync` (READ; official data, not computer use), `tm.similarity`, `cal.create_reminder` | L3 (status sync, alerts) | Attorney files responses; conflict scoring is advisory | INT / HR (response drafts) |
| LV-11 | **Board Secretary** | KMP, BRD | Notices, agendas, board packs, attendance/quorum checks, SS-1/SS-2 checklists, statutory register entries | `gov.build_pack`, `gov.check_quorum` (deterministic), `dms.redline_docx` | L2 | CS approves pack and notices | INT |
| LV-12 | **Minutes Writer** | KMP, BRD | Draft minutes from agenda + recording/notes (consented), action-taken report | `stt.transcribe`, `minutes.draft` | L1 | Chairperson/CS finalise; never invent attendance/votes (LDC VG-20) | INT |
| LV-13 | **Compliance Calendar** | KMP, IND (tax), LT | Companies Act/LLP/GST/TDS/ROC filing calendar from the rules engine; document chasers; integrates with LawDocsComply for regulated entities | `cal.rules_engine` (READ), `task.create` (INTERNAL_WRITE_LOW) | L3 | Filing always human; no "complied" marking by AI | INT |
| LV-14 | **Grievance Assistant** | IND | Loan/insurance/challan grievance intake, document checklist, ombudsman/forum signposting (RBI Integrated Ombudsman, insurance ombudsman), complaint drafts, status tracking | `grv.intake`, `forum.signpost` (deterministic), `letter.draft` | L1 | Legal team reviews before any complaint is filed or the company is approached | HR |
| LV-15 | **DMS Librarian** | all | Auto-classify uploads into the standard folder taxonomy, deduplicate, tag year/department/party, bulk-folder intake, export packs | `dms.classify` (PROPOSE), `dms.move` (INTERNAL_WRITE_LOW, undo 24 h) | L3 | User confirms ambiguous classifications | INT |
| LV-16 | **Signing Coordinator** | IND, LT | Track signer status, schedule nudges inside consent (R4-COMMS-01), resolve Aadhaar eSign failures, eStamp sequencing | `sign.status`, `notify.schedule` (template-approved EXTERNAL_SEND only) | L3 (template sends) | Initiator approves the nudge plan once | INT |
| LV-17 | **Matter Intake Voice Agent** | IND | Inbound phone intake (IVR → agent), facts capture, conflict pre-check, booking, WhatsApp summary | `voice.session`, `case.create`, `booking.create` | L2 | General information only; escalation to human on distress, crime, minors, urgent liberty matters | GEN (advice routed to HR lane) |
| LV-18 | **Support Agent** | all | Product how-to, "i"-button explanations, ticket triage, refund-policy answers | `kb.search`, `ticket.create` | L3 | Refunds/credits approved by ops | GEN |
| LV-19 | **AI SDR** (internal) | MKT | Respond to inbound leads within 5 min (chat/WhatsApp/voice from declared CLI), qualify, book demo/consultation, update CRM | `crm.update`, `booking.create`, `voice.session` | L3 (inbound only) | No cold outreach; promotional calls only to registered-consent leads within windows | INT |
| LV-20 | **Content Studio** (internal) | MKT, OPS | Blog/FAQ drafts from owner's Word files, schema markup, shorts scripts, social calendar entries | `cms.draft`, `seo.audit` | L1 | Human publishes (no auto-publish); claims register check; BCI Rule 36 filter | INT |
| LV-21 | **Ops Hub Delivery Assistant** (internal) | OPS | For retainership clients: task decomposition, draft deliverables as Maker, chase client Checker, SLA tracking | `task.*`, `dms.*` | L2 | RM (Maker) and client Checker approve; no access to password tracker | INT/HR (per deliverable) |

**Packaging:** Free = LV-01 template lane, LV-07, LV-15, LV-18; Individual Plus = + LV-03, LV-04, LV-06, LV-10, LV-14, LV-16; Business = + LV-02, LV-05, LV-09, LV-11, LV-12, LV-13; Enterprise = all + MCP/A2A + missions. Each agent "hired" via the LDC AA.4.3 workflow (sponsor, 30-day supervised period, monthly review).

**Marketing bundles:** individual litigant (LV-04, 06, 07, 14); CLO-only company (LV-01, 02, 03, 04, 09, 10); CS/board (LV-11, 12, 13).

---

## 8. AI architecture notes (LawDocs-specific)

1. **Runtime:** Temporal-orchestrated runs; agents are configuration (LDC AA.4.1); Claude Agent SDK/Managed Agents optional behind `AGENT_RUNTIME_PORT`.
2. **Deterministic core:** stamp duty, limitation, court fees, compliance dates, quorum, eSign eligibility are rules-engine outputs, never model outputs.
3. **Clause library is the moat:** lawyer-authored, versioned clauses with jurisdiction, state stamp rules, risk level and plain-language explanations in 12+ languages; it powers the template lane and the evaluation sets.
4. **QRG service:** queue with SLA (4 working hours standard, 1 hour express), in-house + empanelled reviewers, attestation, diff, AI-use stamp; reviewers paid a flat fee per review, not a share of legal fees.
5. **Voice stack:** Exotel (primary) / Jio SIP (secondary) → voice agent (ElevenLabs / Haptik / Sarvam) → LLM through LawDocs proxy on Bedrock India; recordings to LawDocs S3; non-skippable AI + recording disclosure.
6. **Memory, cost, observability, portability:** as LDC AA.10, AA.14, AA.15 — preferences only in memory; Haiku-tier routing, caching, nightly batch; OTel + run ledger incl. QRG reviewer; Jio/REIL adapter stubs OFF until K.4 admission.

---

## 9. Legal-AI benchmarks (what LawDocs copies or avoids)

| Product | Verified facts (25 Oct 2026) | What LawDocs takes | What LawDocs does differently |
|---|---|---|---|
| **Harvey** (harvey.ai) [V] | "Harvey II"; purpose-built **Agents** with auto-routing; Vault (bulk docs); Knowledge (legal/regulatory/tax research); **Spaces** (shared workspaces with ethical walls for firms, clients, co-counsel); Command Center (usage analytics/benchmarking); Contract Intelligence; Horizon Scanning; **Intake** (new); **Connector Library** incl. custom MCP (new); **Legal Work Orchestration** (agents + staff); 3,500+ legal organisations, 200,000+ professionals, 85+ countries; Indian logos Shardul Amarchand Mangaldas and Khaitan & Co; instances US/EU/AU (no India) | Spaces (shared matter rooms with counterparties), work orchestration of agents + humans, Intake, connector library via MCP | India-resident processing; individuals and SMEs; vernacular; price points in ₹ |
| **Legora** (legora.com) [V] | "Legora aOS — the agentic operating system for legal work"; Agent (plan–execute–review), **Monitors** (regulatory change), Lists, Word and Outlook add-ins, Editor, mobile app, Tabular Review, Workflows, Legal Research, Portal, Skills, Intake; "$550M Series E" banner (date not shown) | Tabular review (many contracts × questions), Portal for clients, Word/Outlook add-ins (owner uses M365) | Consumer-grade onboarding (Aadhaar/DigiLocker) |
| **Spellbook** (spellbook.com) [V] | Word add-in; Draft, Review with Playbooks, surgical redlines, Compare to market standards, Ask, **Associate** (multi-document), new **Autonomous Contract Management (ACM)** (intake → draft → review → repository), early access; live ACM demo 29 Oct 2026; uses GPT-5, Claude and others; ZDR with LLM providers; SOC 2 Type II; 5,000+ legal teams; 7-day trial | Word-native redlining, playbooks, "compare to market" | Indian clause/stamp rules; eSign + eStamp in the same flow |
| **Luminance** (luminance.com) [V] | Negotiate (precedent/playbook-driven redlines), Discover (portfolio risk, obligations, opportunities), Automate (intake to signature); 1,000+ enterprises; 1.3M+ questions answered | Portfolio obligation discovery (LV-03) | — |
| **CoCounsel** (Thomson Reuters) [V] | CoCounsel Legal combines research, analysis and drafting grounded in Westlaw and Practical Law; connects to M365 and DMS; agentic AI mentioned for Westlaw Advantage; US hosting, regional hosting UK/AU/CA; **no India availability stated** | Grounding in authoritative content; show sources and reasoning | Indian primary sources; vernacular |
| **Jhana** (jhana.ai) [V] | Has repositioned toward **public-sector court automation** (Karnataka, Madras, Telangana, Gujarat HCs; TN and Sikkim governments; BCI), AI agents for court/case pages, judge dashboards, cause-list delivery; **CADRE ODR** for bank credit-card/personal-loan defaults (36-hour turnaround); due-diligence and wills/estates services via independent professionals; 16,150+ lawyers and 650 judges have used it; no public pricing | Cause-list delivery and case-page processing patterns for LV-04 | Jhana's CADRE is a direct reference for **Equator** (flag to Equator pack) |
| **SpotDraft** (spotdraft.com) [V] | AI-native CLM: VerifAI (review in Word), **Sidebar agents** (Q&A, review, regulatory change), Contract Data Intelligence, Negotiation Intelligence, Clickwrap, eSignatures, Repository, Intake (new), Fall Release '26; ISO 27001:2022, SOC 2 Type II; India LinkedIn page | Clickwrap (for LawDocs's own T&Cs and marketplace SLAs); intake | Aadhaar eSign + eStamp + litigation in one product |
| **Lexlegis.ai** (lexlegis.ai) [V] | Ask (research with citations, "14M curated legal documents"), Interact, Draft, MIRA (large jobs), power tools (Devil's Advocate, citation checker "Truth or Dare", Translate 23 languages), practice management (intake, conflicts, billing, timesheets), specialist desks (Contracts, Case Tracking, Compliance, IP), **WhatsApp and MS Word access**, on-desk offline; ₹9,000–₹30,000 per user/month; 300+ organisations; partners NVIDIA, IIT Bombay | **Citation checker** (adopt as a QRG pre-check), WhatsApp access to the assistant | Free/low-cost consumer tier; marketplace |
| **NyayGPT** | Not checked — search quota exhausted | — | [U] — verify before any comparison is published |


**Takeaways:** the market has moved to agents + orchestration + intake + MCP connectors; Word/Outlook presence is table stakes; no global leader offers India-resident processing or vernacular consumer flows (LawDocs's gap); Indian per-seat pricing is ₹9k–30k/month, so consumer/SME tiers must sit far below it.

---

## 10. Funnel teardown — ptstdm.co.in/vsl-yt-v2/ (and siblings)

### 10.1 What was fetched [V]

- **/vsl-yt-v2/** (YouTube traffic; Elementor 4.1.1): H1 "How to Get Your Business To Autopilot Using PTSTDM"; YouTube VSL with controls, keyboard, fullscreen and related videos **disabled**; "Stop doing the work of a Manager" + a 6-step framework; CTA "Apply for Consultation Call (₹99) ➔" (pop-up); 3-field forms labelled per source ("YT VSL 99rs – Optin Form", "99 webinar – YouTube", "99 webinar – Facebook"); **GTM-5X53HXB**; no testimonials, FAQ, guarantee or seller identity on the page. **/vsl/** is the Facebook twin.
- **Home page:** Sumit Agarwal (ex-COO Edureka; I Design My Life); Carvemylife Coaching Services Pvt Ltd, Bengaluru; PTSTDM = People, Targets, Systems, Tracking, Delegation, Monitoring; live 2-hour Zoom on 25 Oct 2026, "no replay"; ₹99 + GST vs "regular ₹999"; five valued bonuses; "10,000+ trained"; image and video testimonials; "few seats remaining"; 24-hour refund; one seat transfer.
- **Inconsistencies:** bonus "total ₹17,597" vs listed values summing to ₹8,095 vs "Total Value ₹7,486"; post-deadline ₹1,099 vs "regular ₹999"; "One Friday" vs a Sunday date; timer referenced but absent.

### 10.2 Funnel anatomy (inferred from the pages; ad side not observable)

| Stage | PTSTDM mechanic | Purpose |
|---|---|---|
| Traffic | YouTube and Facebook ads → **source-specific landing pages** (yt-v2 vs vsl) | Attribute CPL/ROAS by channel; tailor copy |
| Hook | Pain-identity headline ("trapped in daily operations"; "stop doing the work of a manager") | Self-selection of SME founders |
| VSL | Locked player (no scrubbing) forces linear watch | Maximises message completion before CTA |
| Tripwire offer | ₹99 consultation ("operational audit") or ₹99 + GST live workshop | Converts cold traffic into **paying** buyers (filters tyre-kickers, funds ad spend) |
| Form + payment | 3 fields → payment pop-up | Minimum friction |
| Value stack | Bonuses with rupee "values", anchor ₹999 | Perceived value ≫ price |
| Urgency/scarcity | Live-only, no replay, limited seats, early-bird price | Show-up rate; conversion |
| Social proof | "10,000+ trained", video testimonials | Trust |
| Risk reversal | 24-hour refund; seat transfer | Lowers purchase anxiety |
| Back-end (inferred) | Workshop → consultation/audit → high-ticket coaching programme | Margin is in the back-end offer |
| Tracking | GTM container (no visible pixel in fetched text; pixels likely loaded via GTM [inferred]); per-source form names | Attribution; retargeting audiences |

### 10.3 Lessons and red flags for LawDocs

- **Copy:** source-specific pages, a single locked short video, a low-price paid first step, 3-field forms, live events, risk reversal.
- **Do not copy:** unverifiable "values" and conflicting anchors (Consumer Protection Act 2019 misleading-advertisement risk; **CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 — "false urgency", "drip pricing"** [K]); "few seats remaining" unless the count is real; testimonials without consent records. For legal services there is a further limit: **advocates may not solicit or advertise** (BCI Rule 36, §10.6).

---

## 11. LawDocs autopilot growth blueprint

### 11.1 Architecture (all in LawDocs's own CRM/ops hub; vendors are pipes)

```
Content engine (blog, vlog, shorts, FAQs, calculators) ─┐
Paid (Google, Meta, YouTube, JioAds GoLocal) ───────────┼─► Landing pages (one per intent: rent agreement, NDA,
Referral/affiliate links ───────────────────────────────┘     vehicle sale, startup, loan grievance, challan)
                                                                │  embedded "Draft free" widget (template lane)
                                                                ▼
                                         Lead magnet / micro-conversion (free draft, legal health check,
                                         stamp-duty calculator, TM search, challan check)
                                                                ▼
                                         Lead in LawDocs CRM (consent objects: DPDP purpose + telecom)
                                                                ▼
                    ┌──────────── AI SDR (inbound, ≤5 min) ─── booking (own scheduler / M365 Bookings) ───┐
                    ▼                                                                                     ▼
          Nurture: Brevo email + WhatsApp (opt-in) + RCS            Webinar/VSL track (₹0–₹99 tripwire for SMEs/startups)
                    ▼                                                                                     ▼
          Purchase: Razorpay (one-time, subscription, retainership); GST invoice auto-emailed
                    ▼
          Onboarding automation (Aadhaar/PAN/CKYC/DigiLocker fetch; first document in 10 minutes)
                    ▼
          Activation → review request → referral prompt → expansion (retainership, marketplace)
```

### 11.2 Lead magnets (by segment)

| Segment | Magnet | Conversion target | Compliance note |
|---|---|---|---|
| Individuals (rent, vehicle, loan, family) | **Free AI-assisted draft** (template lane), downloadable as watermarked PDF; **eSign + eStamp** paid | Free → paid eSign/eStamp ≥ 15% [target] | AUP: template lane; AI-custom lane needs QRG (§6.4); "AI assisted" disclosure |
| Individuals | **Challan check**, **stamp-duty calculator**, **limitation calculator**, **"Is my agreement valid for eSign?" checker** | Tool → account creation ≥ 25% | Deterministic tools (no AI advice) |
| SMEs/startups | **Free Legal Health Check** (20-question self-assessment → score + report of missing agreements/registrations/filings) | Report → consultation booking ≥ 10% | General information; report states it is not legal advice; consultation with LawDocs team |
| Companies/NBFCs | **Compliance gap snapshot** (hand-off to LawDocsComply) and "Board pack in a day" demo | Demo booked ≥ 5% | B2B |
| Startups | **TM availability search + founder kit** (founders' agreement, ESOP, NDA templates) | Kit → TM filing order ≥ 8% | TM search results advisory |

### 11.3 VSL / webinar track (SMEs, startups, finance companies — not consumers in distress)

- **Format:** 6–9-minute locked VSL per intent ("Stop losing money on unsigned agreements", "Run your company's legal team with one person + AI"), followed by **free or ₹99 live webinar** (weekly, Teams Live) and a **₹499 "Legal health audit" call** credited against any purchase.
- **Truthful urgency only:** real session dates; replay **is** provided to registrants within 48 hours (lower complaint risk than "no replay"); seat caps only if the platform enforces them.
- **Value stack** uses real deliverables with actual list prices from the LawDocs price book (claims register).
- **Presenter:** LawDocs as a company (founder/CS/product lead). If an advocate presents, content is **educational**, without soliciting work or naming fees for that advocate (Rule 36).

### 11.4 Nurture and AI SDR

- **Email (Brevo):** Brevo covers email, SMS, WhatsApp campaigns, automation, CRM, Meetings, Conversations, Aura AI agents and open APIs [V]; contacts and consent live in LawDocs's CRM and sync to Brevo (migratable). Sequence: D0 magnet; D1 "sign in 5 minutes"; D3 consented case story; D5 offer; D10 webinar; D21 re-engage; monthly newsletter.
- **WhatsApp:** explicit opt-in only (box unticked by default); utility vs marketing templates; Brevo or JioCX Pulse.
- **AI SDR (LV-19):** inbound only; call within 5 minutes from a **declared A2P CLI** in permitted hours with AI + recording disclosure; qualify, book or hand off; promotional voice only from 140-series with registered consent; inquiry-based follow-up ends at **day 7**.
- **Missed-call capture** on offline material — caller-initiated; consent captured by IVR/WhatsApp opt-in.

### 11.5 Booking, payment and onboarding

- **Booking:** LawDocs scheduler (or Microsoft Bookings in the owner's M365) with round-robin across the ops team; reminders by email + WhatsApp; no-show auto-rebook link.
- **Payment:** Razorpay checkout/links/subscriptions (UPI AutoPay for monthly plans; mandates per RBI e-mandate rules [K]); GST invoice generated and emailed automatically; refunds via policy engine.
- **Onboarding automation:** Aadhaar/DigiLocker/PAN/CKYC fetch → profile pre-filled → "first document" wizard → DMS folder skeleton created → Vidhi tour → day-2 check-in by Support Agent → day-7 CSM call for business plans.

### 11.6 Referral and affiliate

| Programme | Mechanics | Limits |
|---|---|---|
| **User referral** | Both sides get credits (e.g., one free eSign) when the referee completes a paid action | Credits, not cash, for consumers; disclose in T&C |
| **Partner affiliate** (CA/CS firms, DSAs, real-estate brokers, car dealers, startup incubators) | Revenue share on **software subscriptions and non-legal services** (eStamp, eSign, DMS) via tracked links/coupons | **No commission on advocates' professional fees**; CA/CS partners subject to their own institute rules on sharing fees/commissions [K — VERIFY ICAI/ICSI rules]; disclose affiliate relationship in partner content |
| **Professional marketplace** | Advocates pay a **flat listing/subscription fee**, not a percentage of fees [K — fee-sharing risk under BCI Rules Part VI Ch. II; VERIFY]; CAs/CSs per their institutes | No ranking of advocates by ratings or paid placement; allocation by objective filters (practice area, language, location, availability) + rotation |

### 11.7 Content engine

- **Pillars:** agreement explainers by type and state; "your rights" guides (general information); KMP compliance calendars; startup legal; product tutorials (the "i"-button library doubles as content).
- **Loop:** owner's Word files → LV-20 draft → editor + claims register → CMS publish by marketing (no developer) → 3–5 shorts scripts → Adobe Express scheduling, with the **social calendar held in LawDocs** → performance logged back.
- **SEO/GEO:** FAQ/HowTo/Organization schema for LawDocs (company), `llms.txt`, original data tables (stamp duty by state); YouTube vlog with Hindi/English captions; AI media labelled [K].

### 11.8 Review generation

- Trigger after a successful outcome (document signed, consultation rated ≥ 4 in-app) → request a Google review of **LawDocs (the company)**.
- No incentives conditional on positive reviews; no suppression of negative reviews; display reviews **without photos** (owner brief) and with consent; follow **BIS IS 19000:2022 (online consumer reviews)** principles [K]; never review individual advocates (Rule 36).

### 11.9 Tracking and attribution

- **Capture:** UTM (source/medium/campaign/content/term), **GCLID/GBRAID/WBRAID**, **FBCLID/fbp/fbc**, landing page, referrer, first/last touch — stored on the lead record server-side.
- **Server-side events:** Google Ads offline conversions/Enhanced Conversions and Meta Conversions API sent from the CRM on qualified lead, purchase and activation — **only for users who consented to marketing cookies/measurement** (consent banner with purpose toggles; DPDP notice).
- **Source-specific landing pages** (PTSTDM pattern) for YouTube, Meta, Google Search, JioAds GoLocal, partner links.
- **Retargeting:** consented audiences only; **exclude** sensitive intents (criminal matters, matrimonial disputes, debt distress, health insurance claims) from retargeting and lookalikes — both for dignity and platform policies.

### 11.10 KPIs (targets to calibrate in the first 90 days)

| Metric | Target |
|---|---|
| Speed-to-lead (inbound → first contact) | ≤ 5 minutes, 90% |
| Landing page → magnet conversion | ≥ 20% (tool pages), ≥ 8% (VSL pages) |
| Free draft → paid eSign/eStamp | ≥ 15% |
| Webinar show-up | ≥ 35% |
| CAC payback (SME plans) | ≤ 4 months |
| Review request → review | ≥ 12% |
| Telecom compliance incidents (UCC complaints upheld) | 0 |
| QRG turnaround (standard) | ≤ 4 working hours |

### 11.11 Compliance limits for autopilot marketing (binding list `R4-MKT-*`)

| ID | Rule | Source |
|---|---|---|
| R4-MKT-01 | Market LawDocs (company) and its products; never advertise or solicit for an individual advocate; advocate profiles limited to BCI-permitted particulars | BCI Rule 36 (Part VI Ch. II); Madras HC (Quikr/Sulekha/JustDial) 2024; BCI warning Mar 2025; SC challenge pending (*JustDial v PN Vignesh*, notice issued 2026) [V2] |
| R4-MKT-02 | No advocate rankings, "best lawyer", paid placement or rating-based allocation | Same |
| R4-MKT-03 | No commission/referral fee on advocates' fees | BCI Rules Part VI Ch. II [K, VERIFY rule number] |
| R4-MKT-04 | Promotional SMS only on -P headers/whitelisted URLs; promotional voice only from 140-series; opt-out in every promotional message; no re-solicitation for 90 days after opt-out | TCCCPR 2018 as amended 2025, 2026; TRAI Directions 20 Aug 2024 [V] |
| R4-MKT-05 | Every automated call from a pre-declared A2P CLI | TCCCPR Third Amendment 2026 Reg. 4 [V] |
| R4-MKT-06 | Inquiry-based follow-up ≤ 7 days; explicit consent registered for longer | Reg. 2(bb), 2(y) [V] |
| R4-MKT-07 | AI disclosure at the start of every chat/voice session; AI-assisted content labelled | Anthropic AUP (eff. 12 Nov 2026) [V]; IT Intermediary Amendment Rules 2026 [K] |
| R4-MKT-08 | No false urgency, drip pricing, fake scarcity, unverifiable anchor prices | Consumer Protection Act 2019; CCPA Dark Patterns Guidelines 2023 [K] |
| R4-MKT-09 | DPDP notice + purpose-wise consent at capture; withdrawal as easy as giving; children's data only with verifiable parental consent | DPDP Act 2023; Rules 2025 (r.3, r.10; core from 13 May 2027) [V2] |
| R4-MKT-10 | No retargeting on sensitive legal intents | Policy (platform ad policies; dignity) |
| R4-MKT-11 | Reviews: genuine, unincentivised, about LawDocs; consent to display | Consumer Protection Act 2019; BIS IS 19000:2022 [K] |
| R4-MKT-12 | Marketing data never mixed with signing-counterparty data (counterparties are not leads) | R4-COMMS-01; DPDP purpose limitation |

---

## 12. Open items

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-R4-01 | Open a developer.jiocx.com account; read authentication, DLR/webhook and error-code pages; confirm HMAC signing and India processing | Integration lead | Keep JioCX adapters OFF |
| OI-R4-02 | Confirm Gazette publication date of TCCCPR Third Amendment 2026 (commencement maths) | Compliance | Treat Reg. 4 as in force from 1 Dec 2026 |
| OI-R4-03 | Whether DoT/TSPs allot **1600-series** to a non-BFSI service provider such as LawDocs | Compliance + Jio account manager | Declared 10-digit A2P CLIs for service calls; 140 for promotional |
| OI-R4-04 | Bedrock India `in.` support for Claude 5.5 models and for prompt caching/batch/citations | CTO | Use Opus 5/Sonnet 5/Haiku 4.5 on `in.` |
| OI-R4-05 | Anthropic account-team confirmation of the template-lane interpretation under the AUP High-risk legal requirements | Owner/legal | Put both lanes behind QRG for individuals |
| OI-R4-06 | Haptik RFP (EQ Q1–Q12 + R4 Q13–Q15) | Procurement | ElevenLabs/Sarvam stack |
| OI-R4-07 | Jio Platforms RHP: committed enterprise-AI products and timelines | Research | Watch-list |
| OI-R4-08 | NyayGPT and LegalKart AI features | Research (next session) | Exclude from public comparisons |
| OI-R4-09 | BCI rule numbers on fee-sharing; ICAI/ICSI rules on commissions to platforms | Legal | Flat-fee marketplace model only |
| OI-R4-10 | RCS DLT treatment (header/template registration requirement for A2P RCS) | Compliance | Treat RCS like SMS for consent and templates |
| OI-R4-11 | JioCX Verify coverage on Airtel/Vi handsets | Jio account manager | Truecaller for Business in parallel |

---

**Phase hand-offs:** Communications phase ← `R4-COMMS-01`, §3.2 ports, §5.2–5.3; Vidhi phase ← `R4-AI-01`, `R4-AI-02`, §7; Marketing/Ops Hub phase ← §11 and `R4-MKT-*`.

---

## 13. Sources (all accessed 25 October 2026)

| # | URL | Title / description |
|---|---|---|
| 1 | https://www.jio.com/business/ | Jio Business — home and navigation (services, segments, industries, resources) |
| 2 | https://www.jio.com/business/services/jiocx/ | Elevate customer engagement with JioCX |
| 3 | https://jiocx.com/sitemap | JioCX sitemap |
| 4 | https://developer.jiocx.com/ | JioCX developer portal |
| 5 | https://developer.jiocx.com/sms/getting-started/quick-start-guide | JioCX SMS quick start |
| 6 | https://developer.jiocx.com/voice/c2c/getting-started/quick-start-guide | JioCX Click-to-Call quick start |
| 7 | https://developer.jiocx.com/whatsapp/getting-started | JioCX WhatsApp onboarding |
| 8 | https://jiocx.com/security | JioCX Security |
| 9 | https://jiocx.com/products/voice-messaging-solution | JioCX Voice |
| 10 | https://jiocx.com/products/pulse | JioCX Pulse |
| 11 | https://jiocx.com/resources/newsfeed | JioCX Newsfeed (WhatsApp pricing update 1 Oct 2026) |
| 12 | https://www.jio.com/business/services/voice-and-collaboration/ | Jio Business Voice & Collaboration (SIP Trunk, IP Centrex, Toll-Free, JioMeet) |
| 13 | https://www.jio.com/business/resources/ | Jio Business Resources |
| 14 | https://www.jio.com/business/services/jio-cloud/data-analytics/ai-machine-learning/ | JioCloud AI + Machine Learning (Azure) |
| 15 | https://www.jio.com/business/services/jio-cloud/gpu-accelerated-computing/ | GPU Accelerated Computing |
| 16 | https://www.jio.com/enterprisecloud/services/ai-cloud/ | Jio Enterprise AI Cloud |
| 17 | https://www.jio.com/enterprisecloud/pricing/ | Jio Enterprise Cloud pricing page |
| 18 | https://www.jio.com/business/segment/government/ | Jio Business — Government segment |
| 19 | https://www.jio.com/business/services/security/vciso/ | Jio vCISO (and security suite links) |
| 20 | https://jio.com/jioads | JioAds |
| 21 | https://www.haptik.ai/ | Jio Haptik home |
| 22 | https://www.haptik.ai/voice-ai-agents | Jio Haptik Voice AI Agents |
| 23 | https://www.haptik.ai/platform/enterprise-security | Jio Haptik Enterprise Security |
| 24 | https://www.newsbytesapp.com/news/science/jio-unveils-tiered-rcs-pricing-in-india-apple-challenges-whatsapp/tldr | Jio unveils tiered RCS pricing (9 Sep 2026) |
| 25 | https://digitalterminal.in/trending/apple-and-jio-bring-rcs-business-messaging-to-iphone-users | Apple and Jio bring RCS business messaging to iPhone users (9 Sep 2026) |
| 26 | https://www.etvbharat.com/en/technology/reliance-agm-2026-jio-unveils-ai-voice-agent-teleframe-agents-and-five-new-iq-apps-enn26061904822 | Reliance AGM 2026: AI voice agent, TeleFrame, IQ apps |
| 27 | https://thetechportal.com/2026/06/19/reliance-agm26-from-reliance-intelligence-to-jio-ai-call-agent-mukesh-ambani-reveals-an-ai-roadmap-for-india/ | Reliance AGM'26 AI roadmap |
| 28 | https://www.outlookbusiness.com/deeptech/artificial-intelligence/reliance-goes-the-ai-way-unveils-meta-jv-google-cloud-pact-launch-of-reliance-intelligence | Reliance Intelligence, Meta JV, Google Cloud pact (Aug 2025) |
| 29 | https://www.ril.com/sites/default/files/2026-04/REIL_CEO_Appointment_Media_Release.pdf | REIL CEO appointment (23 Apr 2026) |
| 30 | https://oga-prod.angelone.in/news/stocks/reliance-eyes-international-markets-for-jio-telecom-stack-scales-enterprise-ai-initiatives-with-meta | Reliance FY26 annual report coverage — REIL plans (29 May 2026) |
| 31 | https://www.angelone.in/news/ipos/jio-platforms-ai-and-cloud-services-emerge-as-next-growth-engine-ahead-of-ipo | Jio Platforms AI and cloud ahead of IPO (17 Oct 2026) |
| 32 | https://en.channeliam.com/2026/10/08/jio-ai-first-homegrown-technology-ecosystem-imc/ | Jio at IMC 2026 |
| 33 | https://groww.in/blog/jio-platforms-ipo-to-open-on-october-21-2026 | Jio Platforms IPO details |
| 34 | https://techcrunch.com/2026/09/02/indias-richest-man-now-wants-to-turn-aging-computers-into-ai-ready-pcs/ | JioPC standalone launch (2 Sep 2026) |
| 35 | https://www.trai.gov.in/sites/default/files/2026-09/Regulation_18092026.pdf | TCCCPR (Third Amendment) Regulations, 2026 (05 of 2026) |
| 36 | https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2311989&lang=1&reg=3 | PIB: TRAI strengthens UCC framework (18 Sep 2026) |
| 37 | https://callerdesk.io/blog/trai-spam-rules-2026/ | TRAI new rules 2026 — business explainer |
| 38 | https://cms.trai.gov.in/sites/default/files/2025-02/PR_No.11of2025.pdf | TRAI Press Release 11/2025 — TCCCPR amendments (12 Feb 2025) |
| 39 | https://mondaq.com/india/telecoms-mobile-cable-communications/1514356/trai-issues-directions-to-access-service-providers-for-taking-measures-to-curb-misuse-of-messaging-services | TRAI directions of 20/30 Aug 2024 |
| 40 | https://www.outlookbusiness.com/news/trai-sets-firm-deadlines-for-bfsi-entities-to-adopt-1600-series-for-service-transactional-calls | TRAI 1600-series deadlines for BFSI (19 Nov 2025) |
| 41 | https://taxguru.in/corporate-law/indias-digital-personal-data-protection-rules-2025-detailed-breakdown.html | DPDP Rules 2025 breakdown |
| 42 | https://www.medianama.com/2025/03/223-the-bar-council-of-india-warns-against-legal-advertising-online/ | BCI warns against online legal advertising (18 Mar 2025) |
| 43 | https://indialegallive.com/cover-story-articles/il-feature-news/supreme-court-revisits-rule-banning-advocates-from-self-promotion/ | Rule 36 at the crossroads (1 Aug 2026) |
| 44 | https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-expands-claude-model-availability-to-india-cross-region-inference/ | AWS: Claude in-country inference in India (29 Sep 2026) |
| 45 | https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html | Bedrock regional availability by model |
| 46 | https://www.crnasia.com/india/news/2026/anthropic-takes-claude-inference-live-in-india-opens-path-to-regulated-ai-deployments | Anthropic takes Claude inference live in India (5 Oct 2026) |
| 47 | https://justbeingresourceful.com/2026/10/11/claude-now-runs-inside-india-what-in-country-inference-on-amazon-bedrock-means-and-how-to-try-it/ | Claude in-country inference explainer (11 Oct 2026) |
| 48 | https://platform.claude.com/docs/en/release-notes/overview | Claude Platform release notes |
| 49 | https://anthropic.com/news/2026-usage-policy-update | Anthropic 2026 Usage Policy update (8 Oct 2026) |
| 50 | https://www.anthropic.com/legal/aup | Anthropic Usage Policy (effective 12 Nov 2026) |
| 51 | https://blog.mcpservers.org/posts/mcp-spec-2026-07-28 | MCP 2026-07-28 specification preview |
| 52 | https://blog.modelcontextprotocol.io/posts/index.xml | MCP blog: "The 2026-07-28 Specification" (28 Jul 2026) |
| 53 | https://letsdatascience.com/news/a2a-solidifies-cross-vendor-agent-interoperability-53400ea4 | A2A v1.0 cross-vendor interoperability |
| 54 | https://www.harvey.ai/ | Harvey |
| 55 | https://legora.com/ | Legora |
| 56 | https://spellbook.com/ | Spellbook |
| 57 | https://www.luminance.com/ | Luminance |
| 58 | https://www.thomsonreuters.com/en/cocounsel | CoCounsel (Thomson Reuters) |
| 59 | https://www.jhana.ai/ | Jhana |
| 60 | https://www.spotdraft.com/ | SpotDraft |
| 61 | https://lexlegis.ai/ | Lexlegis.ai |
| 62 | https://www.brevo.com/ | Brevo |
| 63 | https://ptstdm.co.in/vsl-yt-v2/ | PTSTDM VSL (YouTube version 2) |
| 64 | https://ptstdm.co.in/vsl/ | PTSTDM VSL (Facebook version) |
| 65 | https://ptstdm.co.in/ | PTSTDM home / workshop page |
| 66 | /home/claude/ldpack/ref/EQ/appendices/T_Benchmarks_Competitors_Institutions_Training_Jio_AI.md | Equator Appendix T §4 (sister pack, 21 Oct 2026) |
| 67 | /home/claude/ldpack/ref/LDC/appendices/AA_Future_Ready_AI_and_Agentic_Architecture.md | LawDocsComply Appendix AA (sister pack) |
| 68 | /home/claude/ldpack/ref/LDC/appendices/K_Vidhi_AI_Agent_Specification.md | LawDocsComply Appendix K (sister pack) |

*End of R4.*
