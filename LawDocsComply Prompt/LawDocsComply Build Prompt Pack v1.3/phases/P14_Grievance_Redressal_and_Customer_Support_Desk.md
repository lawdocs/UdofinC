# Phase P14 — Grievance Redressal and Customer Support Desk

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00, P01 (identity, public intake realm, OTP), P02 (settings, rule packs for SLA clocks), P04 (tasks, notifications, calendar, maker-checker), P07 (DMS, OCR/translation for complaint attachments and letters), P12 (rights-request desk shares the intake widget; breach linkage), P13 (GRO/PNO/IO positions and support-team rosters), P18 (website/app/LMS integration, Ecosystem events).
>
> **Sequencing:** after P04 exit; can run in parallel with P12. Sub-iterations: **P14a** Support desk (omnichannel ticketing, knowledge base, embeddable widget) → **P14b** Grievance redressal ladder (GRO → PNO/Internal Ombudsman → external signposting) with regulator clock packs → **P14c** MIS, regulatory reports and Board/Customer Service Committee packs → **P14d** Ecosystem (Finbyx/Udofin/Equator) and investor/member/policyholder variants.
>
> **Binding appendices:** A (state machines), B (events `grievance` scope reuse), D (roles), G (`LR-RBI-*` grievance and IO rules, `LR-SEBI-*` SCORES/LODR, `LR-IRDAI-*` PPHI, `LR-IFSCA-*`, `LR-COOP-*`), L (website/app widget SDK, Ecosystem adapters), U (settings).
>
> **Requirements covered:** R-080, R-098, R-013, R-023, R-031, R-062, R-066, R-086, R-090 (grievance work items are Notifications; regulatory changes to grievance rules arrive as Updates), R-075.
>
> **Estimated effort:** 6 two-week sprints, squad of 7 (desk 3, ladder & clocks 2, MIS & reports 1, integrations 1).

>
> **v1.1 changes (25 October 2026)**
> - New **§4I AI-assisted triage** under bounded autonomy (NN-50) — category, sub-category, regulator category, language, urgency, vulnerability cues, duplicates and suggested ladder are proposals; deterministic acknowledgement and clocks; AI never sets the final category, status or decision (NN-47) (FR-P14-35–FR-P14-38).
> - New **§4J unified omnichannel thread** — e-mail, widget/portal, WhatsApp (service only, never recovery or legal notices, X-23), voice/IVR with transcription (JioCX adapter), branch walk-in, letters (OCR), social (optional), API — one thread per case with identity matching (FR-P14-39–FR-P14-41).
> - New **§4K customisable taxonomy and SLAs** — tenant categories mapped once to regulator categories for MIS; internal targets never later than statutory clocks (NN-33) (FR-P14-42–FR-P14-44).
> - New **§4L regulator MIS in one click and Board/Customer Service Committee packs** (registered as P28 report definitions), **§4M speed features** (Review next, smart macros, bulk only for spam/duplicates with undo, keyboard flows) and **§4N customer human route for AI conversations** (FREE-AI expectation) (FR-P14-45–FR-P14-50).
> - Internal Ombudsman citations aligned to the RBI catalogue (D-39): NBFC RBI/CEPD/2025-26/383 or /384 [VERIFY] (catalogue lists /383 for NBFCs and /384 for non-bank PPI issuers); commercial banks /380, SFBs /381, payments banks /382, credit information companies /385 [VERIFY all].
> - Global readiness: foreign subsidiaries' complaint schemes arrive as P25 jurisdiction packs; multilingual intake already supported.
---

## 1. Objective and business outcome

A borrower, depositor, member, investor, policyholder or customer first contacts the client's help and support channels (website, app, branch, phone, e-mail, WhatsApp, LSP app such as Udofin, LMS borrower portal such as Finbyx). If unresolved, the complaint escalates to the client's Grievance Redressal Officer (GRO), then — where the regulator requires — to the Principal Nodal Officer (PNO) and/or the **Internal Ombudsman (IO)**, and finally the complainant is told how to approach the external forum (RBI Integrated Ombudsman via CMS, SEBI SCORES, IRDAI Bima Bharosa / Insurance Ombudsman, IFSCA, Co-operative Ombudsman or Registrar, Consumer Commission). LawDocsComply hosts the **whole ladder** for the client: the support team closes tickets inside LDC, the GRO has a dedicated workspace, regulator clocks are owned and escalated, and complaint MIS and regulatory reports are generated. The client's website shows the grievance link; the system runs on LDC.

| Outcome | Exit-gate measure |
|---|---|
| One desk from first contact to final reply | A complaint raised on the client's website widget, by e-mail and by Udofin event lands as one ticket per issue (dedup), is acknowledged within the configured time with a reference number, and is resolved, escalated or signposted with every step time-stamped |
| Regulator clocks never silently lapse | For an NBFC tenant covered by the NBFC IO Directions 2026: a partially-resolved complaint is auto-escalated to the IO so that the IO has ≥ 10 days before any RBI/NPCI/card-network TAT, otherwise within 20 days of receipt (cl.14(1)); the final reply issues within 30 days of receipt (cl.14(9)); the RB-IOS 2026 route (30-day wait, then 90-day window) is stated in the final reply |
| Correct ladder per entity type | Ladder templates for bank, NBFC (with and without IO), UCB, credit co-operative/MSCS, ARC, listed company (investors), AMC/AIF/intermediary (SCORES), insurer/intermediary (IRDAI), IFSCA RE, ordinary company/LLP (customers, MCA/IEPF investor grievances), employer (IR Code GRC lives in P13) — selected automatically from the P15 entity profile |
| GRO workspace that saves hours | GRO resolves a complaint in ≤ 5 clicks from inbox with templates, knowledge base suggestions and Vidhi draft reply; bulk acknowledge; SLA-sorted queues |
| Regulatory reports generated | Quarterly IO report to RBI (cl.16(2), due by the 15th after quarter end), Board/Customer Service Committee complaint review with top-5 categories (cl.13(5)), annual report disclosures (complaints received/resolved/pending, maintainability per RBI format [VERIFY current disclosure circular]), SEBI LODR Reg 13(3) quarterly investor-complaint statement, IRDAI grievance returns [VERIFY form] — each export-ready |
| Ecosystem-ready | Finbyx/Udofin `GrievanceRaised` events open tickets in LDC when LDC is the grievance host; `GrievanceUpdated/Escalated` flow back; Equator referral only on the complainant's or RE's explicit choice (never automatic) |

---

## 2. Scope (in / out)

**In scope**
- `grv` module: channels (web widget, hosted portal, e-mail-in, API, WhatsApp Business API via BSP adapter, phone/IVR logging, branch/walk-in entry, social-media mentions as manual intake, physical letters with OCR), contacts (complainants — pseudonymous for analytics), tickets (service requests vs complaints vs grievances — classification), categories and sub-categories (regulator taxonomies mapped: RBI CMS categories, SCORES categories, IRDAI IGMS categories [VERIFY lists]), priorities, SLAs, queues, teams (support L1, L2 product teams, GRO office, PNO, IO office), knowledge base, canned responses, macros, surveys (CSAT, CES), escalations, reopen, merge/split, duplicates, attachments (malware-scanned, P07), translations (P07), consent and privacy (P12 notice in widget), regulatory reports, Board/CSC packs, analytics and root-cause tagging, linkage to compliance obligations (P04), risk events (P08 conduct-risk KRIs), incidents (P12 when a complaint reveals a breach or fraud), and to the rights-request desk (P12 when a complaint is a DPDP/GDPR/CCPA request).
- Embeddable client-side artefacts: JavaScript widget, hosted portal page on a tenant sub-domain or custom domain (CNAME, TLS), React Native/Flutter/Android/iOS SDK wrappers (thin, P18), "Grievance Redressal" footer link snippet with GRO/PNO contact details auto-rendered from P13 positions and the RB-IOS/SCORES/Bima Bharosa signposting text (the client's website must display this information — e.g., NBFC GRO name and contact on website and branches [VERIFY RBC directions para]).
- Ladder engine with regulator clock packs (rule packs, Governed).
- Investor grievances for listed companies and debt-listed entities (SCORES 2.0 sync as manual/semi-automated, LODR Reg 13), member grievances for co-operatives, policyholder grievances for insurers/intermediaries.

**Out of scope**
- Filing on behalf of the complainant with the RBI Ombudsman, SCORES, Bima Bharosa or Consumer Commission — the complainant files; LDC tells them how (NN-08; Ecosystem Spec `OmbudsmanReferralRecorded`: "the borrower files, never Udofin").
- Dispute adjudication — Equator (separate product; referral only on explicit choice, NN-23).
- IR Code employee grievances (P13 GRC) and POSH (P13 sealed) — different desks; the widget routes employees away.
- Call-centre telephony (CTI) as a product — LDC integrates (P18: Exotel, Knowlarity, Ozonetel, Jio Business voice/AI agents after verification, D-14) for click-to-call and call logging.

---

## 3. Personas and permissions touched

| Role | Rights |
|---|---|
| `ten_support_agent` | Works L1/L2 queues; can resolve service requests and complaints within delegated authority; cannot close a complaint as "rejected" — rejection or partial resolution routes to GRO review (and IO where applicable) |
| `ten_kmp` (GRO) | GRO workspace; final decision at GRO level; signs final replies; owns GRO-level clocks |
| `ten_kmp` (PNO) | Nodal oversight; regulator correspondence; reports |
| `ten_kmp` (IO) | IO workspace (independent): sees escalated complaints, records IO decision, cannot be overruled silently — overruling records the Competent Authority decision and routes to Board review (NBFC IO Directions 2026 cl.13(3)–(4)) |
| `ten_cco` | Compliance view: clocks, breaches, MIS, regulatory reports |
| `ten_board_member` / Customer Service Committee member | Reports and packs; no case PII by default (aggregates and anonymised case summaries) |
| `ten_dept_head` (product/branch heads) | Assigned complaints of their unit; root-cause actions |
| `ten_internal_auditor` | IO internal audit annual review (cl.11), sample testing |
| `ten_supervisor_view` | Time-boxed grant: complaint registers and MIS (D-12) |
| `dlv_professional` | Retainer delivery: may act as GRO assistant (maker) under tenant grant; never the IO |
| Complainant (`anon` / `lead` / authenticated customer) | Raise, track, add information, accept/reject resolution, reopen within window, rate |
| `svc_vidhi` | Classify, summarise, suggest KB articles, draft replies in the complainant's language; never sends without a human (NN-14) |

SoD: IO must not be in the reporting line of the business heads whose complaints they review; the person who rejected at GRO level cannot be the IO reviewer; complaint closure as "rejected" requires a different user from the drafter (NN-05).

---

## 4. Functional requirements

### 4A. Channels and intake

**FR-P14-01 — Web widget and hosted portal.** Tenant-branded, WCAG 2.2 AA (NN-21), available in English, Hindi and the tenant's selected Eighth Schedule languages; captures: complainant type (customer, borrower, guarantor, depositor, member, investor, policyholder, prospective customer, other), identifiers the tenant configures (loan account, folio, policy, membership number — validated by checksum/format; optional lookup via the tenant's system through P18), category (guided by plain-language choices that map to the regulator taxonomy), description, desired resolution, attachments (images/PDF up to 25 MB; screenshots and WhatsApp exports OCR'd by P07 with confidence shown), preferred language and channel, consent/notice (P12). OTP verification of mobile or e-mail before submission (anti-spam) with accessible alternative (audio CAPTCHA not used; OTP + rate limit). Acknowledgement page with complaint reference number and expected timelines.

**FR-P14-02 — E-mail-in.** Per-tenant addresses (e.g., `grievance@<tenant-domain>` forwarded to LDC ingestion, or Graph/Gmail mailbox connector); threading by reference number; auto-acknowledgement; attachments scanned; language detection.

**FR-P14-03 — WhatsApp.** Via WhatsApp Business Platform through a BSP adapter (Gupshup, Meta Cloud API, Jio Business messaging after verification); template messages for acknowledgement and status (pre-approved templates); opt-in captured; 24-hour customer-service window respected for free-form replies [VERIFY current Meta policy].

**FR-P14-04 — Phone/IVR and branch.** Agents log calls (with call-recording link from CTI where integrated), branch staff log walk-in complaints on tablet/desktop with the complainant's signature or OTP acknowledgement; physical letters scanned with OCR and typed copy (editable, P07 type-copy feature, R-038).

**FR-P14-05 — API and ecosystem events.** `POST /v1/grv/complaints` for the tenant's own apps/LMS/LOS/recovery systems (API key + OAuth client credentials, idempotent); Ecosystem events `GrievanceRaised` (from Udofin, Finbyx, Equator where LDC is the host) create tickets; outbound `GrievanceUpdated`, `GrievanceEscalated`, `GrievanceReopened` handling, `GrievanceRated` (Ecosystem Spec §6.12) — with grievance-host switch recorded per RE (Ecosystem Spec §9.1 notes the grievance-host switch is separate from the compliance-mode switch).

**FR-P14-06 — Classification.** Each item is classified as **query/service request** (not a complaint), **complaint** (expression of dissatisfaction requiring a response), or **grievance** (complaint not resolved at first level / escalated) — mapping configurable per regulator definitions (RB-IOS "complaint" and "deficiency in service" definitions [VERIFY clause]). Category, sub-category, product, channel, branch, partner/LSP/DSA/recovery agent involved (important for RBI digital lending and recovery-agent conduct monitoring), severity, vulnerable-customer flag (senior citizen, disability, bereavement — triggers priority handling and accessible communication). Vidhi suggests classification with confidence; agent confirms.

**FR-P14-07 — Duplicate and linked complaints.** Detect duplicates (same complainant + same account + similar text within 30 days) → merge with link; split multi-issue complaints into child tickets each with its own clock but a single communication thread.

### 4B. Ladder engine and clocks

**FR-P14-08 — Ladder templates (rule packs `grv.ladder@<ver>`).** Selected by entity profile (P15) and product line; each step has: owner role, entry conditions, SLA, auto-escalation rule, communication templates, mandatory content in replies (e.g., escalation route, IO/RBI Ombudsman details), closure conditions.

| Ladder | Steps and key timings (all Governed parameters with citations; [VERIFY] where marked) |
|---|---|
| **NBFC covered by IO Directions 2026** (NBFC-D ≥ 10 branches; NBFC-ND ≥ ₹5,000 cr with public customer interface, measured on 31 Mar 2025; newly crossing NBFCs within 6 months; exclusions HFC, CIC, IDF-NBFC, NBFC-IFC, NOFHC, PD, MGC — cl.3) | L1 support → GRO → **auto-escalation to IO** for complaints partly resolved or wholly rejected (cl.14(1)): forwarded so the IO has ≥ 10 days before any RBI/NPCI/card-network-prescribed TAT; otherwise within 20 days of receipt → IO decision → final reply to complainant within **30 days of receipt by the NBFC** (cl.14(9)) → final reply states RB-IOS route |
| **NBFC not covered by IO** | L1 → GRO → (optional PNO) → final reply within 30 days → RB-IOS route |
| **Bank / SFB / PB** (RBI (Commercial Banks / Small Finance Banks / Payments Banks – Internal Ombudsman) Directions 2026, RBI/CEPD/2025-26/380, /381, /382 respectively, 14 Jan 2026 [VERIFY numbers and thresholds] *(v1.1)*) | L1 → branch/regional → GRO/PNO → IO auto-escalation (partly/wholly rejected) → final reply within 30 days → RB-IOS route; card/digital-payment TATs (failed transactions TAT and compensation framework [VERIFY current circular]) as separate clocks |
| **CIC, non-bank PPI issuer** | As per IO Directions applicable to that RE type + RB-IOS 2026 coverage |
| **RB-IOS 2026 external route (signposting)** | Effective 1 Jul 2026; covers banks, NBFCs, non-bank PPI issuers, CICs; complainant may approach RBI Ombudsman if the RE rejects, does not reply within 30 days, or reply unsatisfactory — within 90 days [VERIFY reference point: cl.10(1)(f)–(g) per Ecosystem Spec]; channels cms.rbi.org.in, e-mail, post, toll-free 14448; compensation up to ₹30 lakh consequential loss + ₹3 lakh for harassment/time/expenses; appeal by either party within 30 days to the Appellate Authority |
| **UCB / StCB / DCCB** | RB-IOS coverage of co-operative banks per scheme text [VERIFY — some salient-feature summaries list only banks, NBFCs, PPI issuers and CICs; confirm whether "banks" includes UCBs under the 2026 scheme as it did under RB-IOS 2021 for scheduled UCBs and non-scheduled UCBs above ₹50 crore deposits]; plus State Registrar route for member disputes |
| **Credit co-operative society (State Act)** | Member services → Secretary/CEO → Managing Committee grievance sub-committee (if bye-laws provide) → Registrar of Co-operative Societies / co-operative court route per State Act; timings per bye-laws (T) and State Act [VERIFY per State] |
| **Multi-State Co-operative Society** | Society → **Co-operative Ombudsman** (MSCS Act 2002 s.85A as inserted by the MSCS (Amendment) Act 2023) [VERIFY timelines: complaint within 3 months; Ombudsman decision within 3 months] → appeal to Central Registrar |
| **Listed company / RTA (investors)** | Investor services / RTA → Compliance Officer (LODR Reg 6) → SCORES 2.0: entity resolves within **21 calendar days**; first review by Designated Body (stock exchange/depository) if investor dissatisfied; second review by SEBI; auto-escalation on missed timelines (SCORES 2.0 live 1 Apr 2024 [VERIFY circular SEBI/HO/OIAE/IGRD/P/CIR/2023/156, 20 Sep 2023]); ODR through SMART ODR (SEBI ODR circular 31 Jul 2023, as amended) as a signposting step; quarterly LODR Reg 13(3) statement |
| **AMC / AIF manager / stock broker / IA / RA / PMS / other SEBI intermediaries** | Entity → SCORES 2.0 (21 days) → Designated Body → SEBI; SMART ODR signposting; entity-specific timelines (e.g., IA/RA complaint data on website monthly [VERIFY]) |
| **Insurer** (IRDAI PPHI Regulations 2024 + Master Circular 5 Sep 2024) | Acknowledge **immediately**; seek further details within 7 days; resolve within **14 days** with written reasons if not accepted; a grievance with no reply from the complainant closes after 56 days [VERIFY]; Bima Bharosa (IGMS successor) registration/update [VERIFY integration format]; Insurance Ombudsman (Insurance Ombudsman Rules 2017) — award to be complied within 30 days with ₹5,000/day penalty for delay; appeal against award within 30 days |
| **Insurance intermediary** (broker, corporate agent, web aggregator) | Acknowledge within 14 days [VERIFY "unchanged" per secondary source]; resolution per IRDAI intermediary regulations; Bima Bharosa |
| **IFSCA RE** | Entity complaint handling per IFSCA grievance framework [VERIFY instrument]; IFSCA complaint portal signposting |
| **Ordinary company / LLP** (customer complaints) | Customer service → designated officer → Consumer Protection Act 2019 signposting (e-Jagriti / National Consumer Helpline 1915); e-commerce entities: grievance officer acknowledgement 48 hours, redressal 1 month (Consumer Protection (E-Commerce) Rules 2020 r.4(5)) [VERIFY current amendments] |
| **Company investor grievances (unlisted)** | Company secretary → MCA / IEPF Authority route for unclaimed dividends/shares (IEPF-5 refund claims) — signposting |

**FR-P14-09 — Clock semantics.** Clock starts at **receipt by the RE** on any channel (including receipt by an LSP/DSA/recovery agent on the RE's behalf — the Udofin-received timestamp is the start, because receipt by the RE's agent is receipt by the RE [INTERP; VERIFY]); calendar days unless the rule says working days; never pauses for internal reasons (NN-33): "waiting on complainant/business" pauses only internal targets; a regulatory clock stops only where the governing instrument itself defines a stop-the-clock condition that is encoded, with citation, in the Governed rule pack (for example, if the applicable IRDAI provision treats a complaint as incomplete until requested details are received [VERIFY]) — the stop is explicit, reason-coded, ledgered and visible in the clock history, and the original computed due date is retained; clocks owned by a named role with escalation at 50/75/90 % (T) and lapse → Critical exception, CCO alert, Board/CSC pack entry (NN-31). Clocks are Governed rule packs (NN-28) with source citations; tenant may set **internal** targets earlier than regulatory windows, never later.

**FR-P14-10 — Auto-escalation to IO.** When a GRO decision is "partly resolved" or "rejected", the system creates an IO review item automatically (no user can skip it for covered NBFCs/banks — Locked); computes the latest forward date (`min(receipt + 20 days, regulator_TAT − 10 days)` for NBFC cl.14(1)); IO can request information from the business; IO decision recorded with reasons; if the Competent Authority overrules, the record shows both and creates a Board-review item (cl.13(3)–(4)).

**FR-P14-11 — Final reply content.** Final-reply templates must include (validators block sending if missing): reference number, summary of complaint, decision and reasons, any compensation/refund and timeline, and the **external-route block** chosen by ladder (e.g., for RB-IOS: "If you are not satisfied with our reply, or if you do not receive a reply within 30 days of lodging your complaint, you may file a complaint with the RBI Ombudsman at https://cms.rbi.org.in, by e-mail …, or by calling 14448, within 90 days of …" with dates computed [VERIFY exact phrasing of the 90-day rule]). For SCORES, the SCORES route; for IRDAI, Bima Bharosa / Insurance Ombudsman. Language: the complainant's preferred language (P07 translation with human review), plus English.

**FR-P14-12 — Signposting record.** Every external-route communication creates a signposting event (`GrievanceEscalated` with `level = EXTERNAL_INFO`). When the complainant declares an external filing (RBI CMS reference, SCORES reference, Bima Bharosa token), `OmbudsmanReferralRecorded` captures forum and reference; later stages (facilitation, conciliation, advisory, award, appeal) are recorded by the RE (Ecosystem Spec §6.12).

**FR-P14-13 — Reopen.** Complainant may reopen within the tenant window (default 30 days [REC]); reopened complaint is treated as a fresh receipt for clock purposes where the regulator treats it so [INTERP], linked to the original.

**FR-P14-14 — Equator referral.** A "Consider mediation/ODR" option appears only (a) for a complainant who explicitly opts in after reading an information note, or (b) for the RE to propose to the complainant — the referral is created only after the complainant's recorded consent (Ecosystem Spec §6.9 ADR referral gates); grievance clock obligations continue regardless; a grievance never auto-becomes a dispute case (Architecture baseline "Grievance redressal workspace").

### 4C. Support desk features (speed and quality)

**FR-P14-15 — Queues and routing.** Skills-based and round-robin routing; branch/product routing; language routing; VIP/vulnerable priority; SLA-sorted default view ("next breach first"); load balancing with caps; out-of-office aware (P13 leave).

**FR-P14-16 — Work faster.** Macros (classify + reply + set status), canned responses with variables, KB suggestions (semantic search over tenant KB + approved FAQs), Vidhi draft reply grounded in the account facts supplied by the agent or fetched via P18 lookup (no free hallucination: Vidhi may only use the ticket thread, the KB and fetched fields — NN-14), bulk acknowledge, bulk status with preview and undo, keyboard shortcuts (`J/K` next/previous, `R` reply, `E` escalate, `M` macro), collision detection (two agents on one ticket), internal notes with @mentions (Notifications, NN-27), side-by-side customer 360 (from the tenant's LMS/CRM via P18 — read-only fields).

**FR-P14-17 — Knowledge base.** Internal and public articles, versioned, with review dates; public FAQ page for the tenant (SEO-friendly, P23 patterns); article feedback; gaps report (searches with no result).

**FR-P14-18 — Surveys.** CSAT (1–5) and optional CES after closure; never shown to the handling agent before closure; low rating offers escalation, never a retention offer (Ecosystem `GrievanceRated` rule).

**FR-P14-19 — Root cause and conduct analytics.** RCA taxonomy (process, people, system, policy, third party — LSP/DSA/recovery agent), repeat-complaint detection, product/branch/partner heatmaps, complaint-to-account ratio, turnaround distributions, maintainable vs non-maintainable (RBI annual disclosure format), compensation paid, ombudsman outcomes vs internal decisions (IO performance assessment input, cl.14(15)), conduct-risk KRIs to P08 (e.g., recovery-agent harassment complaints per 1,000 accounts, mis-selling complaints, digital-lending app complaints), linkages to compliance obligations (e.g., KFS not provided → obligation breach exception).

### 4D. Regulatory reports and governance packs

**FR-P14-20 — Reports.**

| Report | Recipient | Frequency / due | Source |
|---|---|---|---|
| IO quarterly report (Annexure format) | RBI CEPD | by 15th of month after quarter (NBFC IO Directions 2026 cl.16(2)) | IO register |
| IO appointment details | RBI CEPD | within 5 working days of appointment (cl.16(1)) | P13 regulated-role event |
| IO vacancy intimation | RBI | within 10 working days; replacement within 3 months (cl.8(6)) | P13 |
| Board / CSC complaint review | Board, Customer Service Committee | quarterly; IO reports at least half-yearly (cl.13(2)); top-5 categories and RBI Ombudsman decisions in customer's favour (cl.13(5)) | `grv` MIS |
| Annual report disclosure on complaints | Annual report (P06) | annual (format per RBI disclosure circular for the entity type [VERIFY]) | MIS |
| SEBI LODR Reg 13(3) investor complaints statement | Stock exchange | quarterly within 21 days of quarter end [VERIFY current timeline] | Investor ladder |
| SEBI intermediary complaint data disclosure on website | Public | monthly [VERIFY per intermediary type] | MIS |
| IRDAI grievance statistics | IRDAI | per PPHI master circular [VERIFY] | Insurer ladder |
| Co-operative society complaint summary | Managing Committee / AGM | per bye-laws (T) | Co-op ladder |
| Internal audit of IO function | Audit Committee / RBI | annual (cl.11) | P10 engagement template |

Each report: preview, maker-checker, export DOCX/XLSX/PDF, filing-evidence upload (NN-08).

**FR-P14-21 — Policy.** Customer Grievance Redressal Policy model templates per entity type (P07; e.g., NBFC policy covering GRO/PNO/IO, timelines, display obligations, escalation matrix, compensation); policy-to-ladder consistency check ("policy says 21 days, ladder configured 30 days" → warning).

**FR-P14-22 — Display obligations checklist.** Website/branch display of GRO/PNO details, RB-IOS salient features, IO existence (if applicable), SCORES/ODR links for listed entities and SEBI intermediaries, Bima Bharosa/Ombudsman for insurers — generated snippet and a periodic attestation task with screenshot evidence.

### 4E. Linkages

**FR-P14-23 — Privacy requests.** If classified as a DPDP/GDPR/CCPA rights request or a DPDP s.13 grievance, the ticket hands off to P12 rights desk with linked clocks (DPDP requires the grievance mechanism be exhausted before approaching the Board, s.13(3)).

**FR-P14-24 — Fraud and incidents.** Complaints indicating fraud (unauthorised transactions, impersonation, phishing) raise a P12 incident and a fraud-risk record (P08/P10 fraud module) and start any card/digital-payment liability clocks [VERIFY customer-liability circular for the entity type].

**FR-P14-25 — Compliance evidence.** Grievance obligations in the tenant's compliance register (P04) are evidenced automatically from MIS (e.g., "Is the GRO's name displayed?" → attestation; "Are complaints resolved within 30 days?" → KPI with evidence export).


### 4F. Sector-specific complaint features

**FR-P14-26 — Digital lending and LSP complaints.** For REs with digital lending arrangements (RBI Digital Lending Directions, consolidated into the NBFC/bank Responsible Business Conduct and Credit Facilities directions of Nov 2025 [VERIFY current instrument and paras]): each Lending Service Provider and Digital Lending App is a configured partner with its own nodal grievance officer; complaints against an LSP/DLA are the RE's responsibility and run on the RE's ladder; the widget snippet supplied to the LSP shows the RE's GRO details alongside the LSP's nodal officer; complaints tagged with LSP, DLA and DSA identifiers feed the partner scorecard (P12 TPRM ongoing monitoring) and the Udofin partner view (aggregates). Complaints on unauthorised digital lending apps (not linked to any RE) are signposted to the RBI Sachet portal and to the police cyber-crime portal (1930 / cybercrime.gov.in) [VERIFY current portal names].

**FR-P14-27 — Recovery-agent conduct complaints.** Category set for collection and recovery conduct (calls outside permitted hours, harassment, threats, misrepresentation, contacting relatives/references, visiting at inappropriate times, use of abusive language) with mandatory linkage to the agency and agent identifiers (from Finbyx Recovery Suite events where available); automatic conduct-risk flag to P08 and a compliance exception against the tenant's recovery-conduct obligations (e.g., contact windows 08:00–19:00 and the microfinance 09:00–18:00 window under the NBFC RBC Directions 2025 [VERIFY paras 90, 91(2), 100 per Ecosystem Spec §9.2 minimum control feed]); agency suspension task proposal to the business head (human decision).

**FR-P14-28 — Credit-information complaints.** For credit-information disputes (incorrect bureau reporting), the ladder includes the CIC-correction step: RE must rectify and update the CIC within the time allowed under the Credit Information Companies Regulation Act 2005 and RBI directions on CIC complaint handling (including compensation for delayed resolution — RBI framework on compensation for delayed updation/rectification of credit information [VERIFY current consolidated directions and 30-day timeline]); clock `grv.cic.rectification`; link to P11 Return Studio bureau correction file (`bureau_consumer_v374` correction records via Finbyx when Finbyx is the producer).

**FR-P14-29 — Co-operative member services.** Member-specific categories (share certificate issue, dividend, loan sanction delay, deposit repayment, election/voting rights, AGM notices, inspection of records/bye-laws access, expulsion); routes to Managing Committee sub-committee and Registrar per the State Act configured in P16; member complaints counted for AGM report; sensitive categories (election disputes) carry a "statutory forum" banner — election disputes typically lie before the co-operative tribunal/court or the State Co-operative Election Authority, not the society's desk [VERIFY per State Act].

**FR-P14-30 — Investor services (listed and debt-listed entities).** Investor categories (non-receipt of dividend/interest/redemption, transmission, duplicate certificates, demat/remat, KYC update with RTA, IEPF transfers and refund claims, rights/bonus entitlements); RTA integration (Bigshare, KFinTech, MUFG Intime/Link Intime, Cameo — via SFTP/CSV reconciliation [VERIFY RTA APIs]); Stakeholders Relationship Committee pack (LODR Reg 20) feeds P06; SCORES reference capture and status mirroring; statement of investor complaints (Reg 13(3)) auto-filled.

**FR-P14-31 — Policyholder services (insurers and intermediaries).** Grievance categories aligned to IRDAI IGMS/Bima Bharosa taxonomy [VERIFY]; claim-related complaints link to claim reference; mis-selling complaints feed conduct KRIs; Insurance Ombudsman award tracking with the 30-day compliance clock and ₹5,000/day delay-penalty computation (PPHI Master Circular 2024) for the tenant's provisioning.

**FR-P14-32 — Compensation engine.** Configurable compensation rules (T) with Governed regulatory floors where a regulator prescribes compensation (e.g., failed-transaction TAT compensation, delayed CIC rectification, delayed release of security documents/original property documents after loan closure under RBI's 2023 directions — ₹5,000 per day of delay beyond 30 days [VERIFY current consolidated reference]); computed amounts appear as suggestions with rule citations; approval workflow (amount bands by authority matrix, P02); payout instruction exported to the tenant's payment system (D-11 pattern — LDC moves no money); compensation ledger for MIS and annual disclosure.

**FR-P14-33 — Customer rights charter and service commitments.** Tenant's customer charter (P07 template per entity type) linked to service-request SLAs (e.g., NOC/closure certificate issuance, statement of account, foreclosure statement, document return); breaches of charter SLAs create complaints automatically when the customer has raised a request and the SLA lapses [REC — "proactive complaint" option `grv.proactive_breach_tickets`, default OFF].

**FR-P14-34 — Senior citizens and persons with disabilities.** Priority queues, assisted complaint lodging (agent-assisted with consent recording), accessible communication formats (large-print PDF, screen-reader-friendly HTML, audio call-back), sign-language video-call booking where the tenant offers it, and accessible status tracker (NN-21); tags excluded from any adverse treatment and visible only to handlers.

### 4G. Seed category taxonomy (excerpt; full list in rule pack `grv.categories@1.0`)

| Group | Example categories | Regulator code mapping |
|---|---|---|
| Loans — origination | Non-receipt of KFS/sanction letter; interest/charges not disclosed; loan not disbursed after sanction; processing-fee refund | RBI CMS: "Loans and advances" sub-categories [VERIFY codes] |
| Loans — servicing | Excess interest/penal charges; EMI not credited; statement of account; foreclosure charges; floating-to-fixed reset | RBI CMS |
| Loans — closure | NOC delay; original documents not returned; charge not satisfied (CHG-4/CERSAI) | RBI CMS; links to P06 charge register |
| Recovery conduct | §FR-P14-27 list | RBI CMS (recovery agents) |
| Credit information | Wrong DPD reporting; account not closed in bureau; identity mix-up | RBI CMS (CICs) |
| Deposits (NBFC-D / UCB / co-op) | Non-repayment on maturity; interest not paid; nomination | RBI CMS / Registrar |
| Digital lending / LSP | Unauthorised app; data misuse; harassment by LSP staff | RBI CMS; Sachet |
| Investor | §FR-P14-30 list | SCORES categories [VERIFY] |
| Policyholder | Claim delay/rejection; policy servicing; mis-selling | IRDAI Bima Bharosa [VERIFY] |
| Privacy | Consent withdrawal not honoured; data access request; unsolicited marketing | DPDP s.13 / TRAI TCCCPR |
| Service quality | Staff behaviour; branch service; call-centre waiting | Tenant |


---

### 4H. Complaint MIS formats and regulator TAT matrix (added in review, 25 October 2026)

**FR-P14-30 — Annual-report complaint disclosure (RBI REs).** The MIS produces the RBI disclosure on complaints in two tables, from `grv` data with lineage (NN-22) [VERIFY the current consolidated-direction reference for each RE type; the format below follows the RBI disclosure on complaints first prescribed for banks, NBFCs and UCBs in January 2021]:

| Table A — Summary information on complaints received from customers and from the Offices of Ombudsman | Value |
|---|---|
| Complaints pending at the beginning of the year | count |
| Complaints received during the year | count |
| Complaints disposed of during the year, of which rejected by the RE | count, count |
| Complaints pending at the end of the year | count |
| Maintainable complaints received by the RE from the Office of Ombudsman | count |
| …of which resolved in favour of the RE by the Ombudsman | count |
| …of which resolved through conciliation/mediation/advisories issued by the Ombudsman | count |
| …of which resolved after passing of awards against the RE | count |
| Awards unimplemented within the stipulated time (other than those appealed) | count |

| Table B — Top five grounds of complaints | Pending at beginning | Received during year | % change over previous year | Pending at end | …of which pending > 30 days |
|---|---|---|---|---|---|
| Ground 1–5 (mapped from the `grv.categories` taxonomy to the RBI ground list in the rule pack) | count | count | % | count | count |

**FR-P14-31 — Other MIS outputs.** (a) Board/Customer Service Committee quarterly pack: volumes by channel, product, branch/partner (incl. Udofin/LSP/DSA as receiving agent), category and severity; ageing buckets (0–7, 8–15, 16–30, > 30 days); TAT compliance % per ladder step; IO referrals and IO-overturned decisions; RBI Ombudsman references by stage; repeat complainants; compensation paid; root-cause themes and actions; (b) SEBI: SCORES 2.0 action-taken data and the quarterly LODR Reg 13(3) statement (pending at start, received, disposed, pending at end) for listed entities; monthly complaint data for intermediaries that must publish it on their websites [VERIFY per intermediary type]; (c) IRDAI: grievance statistics in the format and frequency prescribed under the PPHI Regulations 2024 and master circular [VERIFY format]; (d) co-operative societies: complaint summary to the Managing Committee and the AGM. Each output is a versioned template (P07 `docgen`) with maker-checker and export (DOCX/XLSX/PDF).

**FR-P14-32 — Regulator TAT matrix (seed, Governed rule pack `grv.tat@1.0`).** All values carry citations in the pack; [VERIFY] values ship advisory-only (NN-38).

| Regime | Acknowledge | Internal resolution / final reply | Mandatory internal escalation | External route and limit |
|---|---|---|---|---|
| RBI REs under RB-IOS 2026 | Promptly (tenant T, default same working day) | 30 days from receipt by the RE | IO review before rejection/partial resolution for covered REs (NN-40) | RBI Ombudsman via CMS; time limit and reference point [VERIFY scheme clause]; appeal to Appellate Authority |
| NBFC covered by IO Directions 2026 | as above | 30 days (cl.14(9)) | Forward to IO by day 20 or ≥ 10 days before any shorter prescribed TAT (cl.14(1)) | as above |
| Failed digital transactions (RBI TAT framework) | — | Auto-reversal within the prescribed T+n per transaction type | — | compensation per day of delay [VERIFY current circular] |
| SEBI-regulated entities (SCORES 2.0) | — | 21 calendar days | — | First review by Designated Body, second by SEBI; SMART ODR |
| Insurers (IRDAI PPHI 2024) | Immediately | 14 days | — | Bima Bharosa; Insurance Ombudsman (Rules 2017) |
| Insurance intermediaries | [VERIFY] | [VERIFY] | — | Bima Bharosa |
| IFSCA REs | [VERIFY instrument] | [VERIFY] | — | IFSCA complaint mechanism |
| Multi-State co-operative societies | per bye-laws (T) | per bye-laws (T) | — | Co-operative Ombudsman (MSCS s.85A) [VERIFY timelines] |
| State co-operative societies | per bye-laws (T) | per bye-laws (T) | — | Registrar / Co-operative Court or Tribunal per State Act |
| E-commerce entities (Consumer Protection (E-Commerce) Rules 2020) | 48 hours | 1 month | — | National Consumer Helpline / e-Jagriti |
| Data Principal grievances (DPDP Rules 2025) | — | within the period the fiduciary publishes, not exceeding ninety days (DPDP Rules 2025 r.14(3) [VERIFY]) | — | Data Protection Board (P12 rights desk) |


### 4I. AI-assisted triage under bounded autonomy *(v1.1)*

**FR-P14-35 — Triage proposals.** On intake Vidhi (Grievance Triage agent, Appendix AA §AA.4.2) proposes: query vs complaint vs grievance (FR-P14-06), tenant category and sub-category, mapped regulator category (for MIS), product and branch, language, urgency, vulnerability cues (elderly, disability, financial distress, bereavement — handled as sealed flags, NN-13), possible duplicates and the ladder template. Proposals appear as chips the agent confirms with one keystroke; confirmation rate and override reasons are tracked as model-quality metrics.

**FR-P14-36 — Deterministic core.** Acknowledgement, reference number, clock start and ladder steps are deterministic and do not wait for AI (if the model is down the desk works unchanged, Appendix K fallback). The clock starts at the earliest receipt time (NN-33) regardless of how long triage takes.

**FR-P14-37 — Autonomy limits.** Default autonomy L1 (propose). A tenant may set L2 for low-risk queries only (e.g., auto-classifying "statement request" queries and sending a template reply with links); complaints and grievances remain L1; closures, decisions, compensation, IO escalations and final replies are always human (NN-47, NN-50). Every AI suggestion is logged with model, version and prompt template id.

**FR-P14-38 — Similar-case answers.** For a new complaint Vidhi shows up to three resolved similar cases (same category/product, anonymised) with the decision and the policy clause relied on (NN-06), so agents resolve consistently.

### 4J. Unified omnichannel thread *(v1.1)*

**FR-P14-39 — One case, many channels.** All channels write into one case thread: web widget/portal, e-mail, WhatsApp (service conversations only; templates pre-approved; never used for recovery or legal notices, X-23), voice/IVR (call recording link and transcript via JioCX or other CPaaS adapter with disclosure; P18 `VOICE_PORT`), branch walk-in (tablet capture with OTP/signature acknowledgement), letters (scanned and OCR'd with type copy, P07), social media mentions (optional connector; converted to a case only when the complainant identifies), API/ecosystem events.

**FR-P14-40 — Identity matching.** Contact matched by verified mobile/e-mail/customer ID token; possible matches shown for agent confirmation; no automatic merge across different identifiers (privacy).

**FR-P14-41 — Channel preference and accessibility.** Replies go on the complainant's chosen channel; final replies always also by e-mail or letter where the regulator expects a written reply; accessible formats (large print, screen-reader friendly PDF, regional language) on request.

### 4K. Customisable taxonomy and SLAs *(v1.1)*

**FR-P14-42 — Tenant taxonomy.** Tenants define their own categories, sub-categories, root-cause codes and priority rules; each tenant category maps once to the regulator taxonomy for MIS (RBI complaint categories, SCORES categories, IRDAI grievance types); unmapped categories block MIS generation with a clear prompt.

**FR-P14-43 — SLAs.** Internal SLAs per category/priority/channel are Tenant settings but can never be later than the statutory ladder (Locked floor); the UI shows both "internal target" and "regulatory due" (NN-33).

**FR-P14-44 — Forms and fields.** Intake forms per channel and product are configurable (P02 form builder) with mandatory regulator fields locked.

### 4L. Regulator MIS and committee packs in one click *(v1.1)*

**FR-P14-45 — One-click MIS.** Each §4H format (RBI annual complaint disclosures — summary and top-five grounds; IO statistics; SCORES/LODR Reg 13(3) quarterly statement; IRDAI grievance returns; co-operative registrar reports) is a P28 report definition: pick period → preview → validation (totals reconcile with case data) → export (XLSX/PDF) → attach to the P04 checkpoint as evidence with act date (NN-48).

**FR-P14-46 — Committee packs.** Quarterly Customer Service Committee / Board pack: trends, TAT distribution, repeat complaints, RCA heatmaps, partner (LSP/DSA/recovery agent) complaint rates, IO overrides (NN-40 Board-review items), actions taken.

### 4M. Speed features *(v1.1)*

**FR-P14-47 — Review next and keyboard flow.** Agents and GROs process the queue with "Review next" (evidence and history preloaded); keyboard shortcuts for classify, reply, escalate, close; target ≤ 3 clicks for a standard query resolution.

**FR-P14-48 — Smart macros.** Macros can set fields, apply a template, attach a KB link and schedule a follow-up; macro usage analytics.

**FR-P14-49 — Bulk with undo.** Bulk actions only for spam, duplicates and misrouted items (merge, reassign, mark spam) with a 24-hour undo (NN-49); never bulk close complaints with a decision (NN-46).

### 4N. Customer human route for AI conversations *(v1.1)*

**FR-P14-50 — Human route.** Where the tenant runs a chatbot/voicebot (its own or Vidhi-assisted), every AI conversation offers "talk to a person" at any point, discloses that the customer is speaking with an AI, and turns an expression of dissatisfaction into a case with clock start at that moment (NN-33). AI conversations used for complaints are logged and linked to the AI system in the P12 `aig` register.

## 5. Workflows and state machines

### 5.1 Ticket (`grv.tickets.status`)
`NEW → ACKNOWLEDGED → (WAITING_ON_CUSTOMER ⇄ IN_PROGRESS) → RESOLVED_PROPOSED → (ACCEPTED → CLOSED) | (NOT_ACCEPTED → ESCALATED_GRO)`; `IN_PROGRESS → ESCALATED_GRO → GRO_REVIEW → (RESOLVED_FULL → FINAL_REPLY_SENT → CLOSED) | (RESOLVED_PARTIAL | REJECTED → IO_REVIEW [covered REs, Locked] → IO_DECIDED → (COMPETENT_AUTHORITY_OVERRULE? → BOARD_REVIEW_ITEM) → FINAL_REPLY_SENT → CLOSED)`; `CLOSED → REOPENED (within window) → IN_PROGRESS`; `CLOSED → EXTERNAL_FILED (declared) → EXTERNAL_OUTCOME_RECORDED`. Service requests use a shorter machine `NEW → IN_PROGRESS → FULFILLED → CLOSED`.

Guards: `FINAL_REPLY_SENT` requires validator-green template (external route block, reasons); `REJECTED` cannot be set by the drafter alone (checker); `CLOSED` blocked while IO review pending for covered REs; `WAITING_ON_CUSTOMER` pauses only clocks whose rule allows pausing.

### 5.2 Clock engine
```
on TicketReceived(t):
  ladder = rulepack('grv.ladder', entity=t.tenant.profile, product=t.product, at=t.received_at)
  for c in ladder.clocks:
     start = t.received_at if c.start == 'RECEIPT' else t[c.start_event]
     due = add(start, c.window, calendar=c.calendar, holidays=t.establishment.holidays if c.working_days)
     clock.start(t, c.key, start, due, owner=c.owner_role, escalations=tenant.cfg('grv.escalation_points'))
on GRODecision(t, outcome in {PARTIAL, REJECTED}) and ladder.io_required:
     forward_by = min(t.received_at + 20d, t.regulator_tat_due - 10d)   # NBFC IO cl.14(1)
     create IOReview(t, due=forward_by); notify IO
```

### 5.3 IO review
`QUEUED → INFO_REQUESTED ⇄ UNDER_REVIEW → DECIDED (UPHOLD | MODIFY | REVERSE) → COMMUNICATED_TO_RE → (RE_ACCEPTS | COMPETENT_AUTHORITY_OVERRULES → BOARD_REVIEW_ITEM)`.

### 5.4 Regulatory report
`SCHEDULED → DRAFTED (auto) → REVIEWED (maker) → APPROVED (checker) → SUBMITTED (human, evidence) → ACKNOWLEDGED`.

---

## 6. Screens and UX

Menu: **Customers & Grievances** — Inbox, Tickets, GRO Desk, IO Desk (IO only), Knowledge Base, Reports & MIS, Settings (ladders, categories, templates, widget). Public: hosted portal `/<tenant>/grievance`, widget, status tracker.

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-GRV-01 | Agent inbox | › Inbox | SLA-sorted, filters (channel, language, category, vulnerable), bulk actions, collision indicators |
| SCR-GRV-02 | Ticket workspace | (drill) | Thread, customer 360 side panel, classification, clocks bar (each regulator clock with remaining time and escalation state), KB suggestions, Vidhi draft, macros, attachments with OCR type copy, internal notes, linked items (privacy, incident, fraud, obligation) |
| SCR-GRV-03 | GRO desk | › GRO Desk | Escalated queue, decision panel (full/partial/reject with reasons library), final-reply composer with validators, IO forwarding countdown |
| SCR-GRV-04 | IO desk | › IO Desk | Independent queue, info requests to business, decision record, overrule log |
| SCR-GRV-05 | Ladder designer | › Settings › Ladders | Visual ladder (steps, clocks, owners) pre-filled from rule pack; tenant can add internal steps/targets but cannot remove Locked steps; simulation ("receipt on 2 Nov → IO forward by …") |
| SCR-GRV-06 | Categories & mapping | › Settings › Categories | Tenant categories ↔ regulator taxonomy mapping |
| SCR-GRV-07 | Widget & portal builder | › Settings › Channels | Branding, languages, fields, identifiers, embed code, CNAME, accessibility checker preview |
| SCR-GRV-08 | Knowledge base | › Knowledge Base | Articles, versions, public/internal, review dates |
| SCR-GRV-09 | MIS dashboard | › Reports & MIS | Volumes, TAT, breaches, maintainability, top categories, partner/branch heatmaps, CSAT, ombudsman outcomes |
| SCR-GRV-10 | Regulatory reports | › Reports & MIS › Regulatory | Report calendar, drafts, submissions, acknowledgements |
| SCR-GRV-11 | Board/CSC pack | › Reports & MIS › Packs | Generates P06 agenda item paper |
| SCR-GRV-PUB-01 | Public complaint form | `/grievance` | ≤ 6 required fields; plain language; language switcher; accessible |
| SCR-GRV-PUB-02 | Status tracker | `/grievance/track` | Reference + OTP; timeline; add info; accept/reject resolution; escalate; rate |
| SCR-GRV-12 | Triage chips panel *(v1.1)* | (inside case) | AI proposals with confidence; one-key confirm; override reason |
| SCR-GRV-13 | Omnichannel thread *(v1.1)* | (inside case) | All channels in one timeline; channel badges; transcript viewer |
| SCR-GRV-14 | Taxonomy and regulator mapping *(v1.1)* | Settings › Grievance › Taxonomy | Tenant categories ↔ regulator categories; unmapped warnings |
| SCR-GRV-15 | One-click MIS *(v1.1)* | Grievance › Reports | Period, preview, reconciliation, export, attach as evidence |

UX targets: agent resolves a standard service request in ≤ 4 clicks with a macro; GRO final reply in ≤ 5 clicks; public form completion median ≤ 2 minutes; every clock chip has text and icon, not colour alone.

---

## 7. Backend design

### 7.1 Modules
`grv` (tickets, ladders, clocks, KB, surveys, reports), using `wf` (clocks via Temporal durable timers, tasks, notifications), `dms` (attachments, OCR, translation), `int` (channels, ecosystem), `cmp`, `erm`, `dpc`, `hr` (positions for GRO/PNO/IO; rosters), `rpt`.

### 7.2 Tables

| Table | Key columns |
|---|---|
| `grv.contacts` | token (pseudonymous), display_name (encrypted), contact_hash, preferred_language, vulnerable_flags (sealed) |
| `grv.tickets` | ref_no (tenant prefix + year + sequence), kind (SR, COMPLAINT, GRIEVANCE), channel, received_at, received_by_entity (RE / LSP / DSA / branch), product, account_ref_token, category_id, regulator_category_code, severity, status, ladder_version_id, parent_ticket_id, duplicate_of_id, language |
| `grv.messages` | ticket_id, direction, channel, body (encrypted), attachments[], sent_by, sent_at, template_id |
| `grv.clocks` | ticket_id, clock_key, start_at, due_at, paused_intervals jsonb, owner_role, status, rule_version_id |
| `grv.decisions` | ticket_id, level (L1, GRO, IO, CA), outcome, reasons, compensation_amount, decided_by, decided_at |
| `grv.io_reviews` | ticket_id, forward_by, decided, overruled bool, board_item_id |
| `grv.external_referrals` | ticket_id, forum, external_ref, declared_at, stage, outcome |
| `grv.ladders` / `grv.ladder_steps` | entity_family, product_scope, steps jsonb, clocks jsonb, locked_steps[] |
| `grv.categories` / `grv.category_maps` | tenant category ↔ regulator code |
| `grv.kb_articles` / `grv.kb_versions` | visibility, review_due |
| `grv.surveys` | ticket_id, csat, ces, comment, submitted_at |
| `grv.rca_tags` | ticket_id, rca_code, third_party_ref |
| `grv.reports` / `grv.report_runs` | report_code, period, file_ids, status, submitted_at, ack_ref |

### 7.3 APIs
Public: `POST /v1/public/grv/{tenant}/complaints` (OTP-verified), `GET /v1/public/grv/{tenant}/complaints/{ref}` (OTP), `POST …/{ref}:add-info|accept|reject|reopen|rate`. Tenant: `/v1/grv/tickets` (CRUD, search), `:classify`, `:assign`, `:escalate`, `:decide`, `:send-final-reply`, `:merge`, `:split`, `/v1/grv/io-reviews/{id}:decide`, `/v1/grv/reports/{code}:draft|approve|record-submission`, `/v1/grv/kb`, `/v1/grv/widget/config`. Machine: `POST /v1/grv/complaints` (API key/OAuth, idempotent), webhook subscriptions for status changes.

### 7.4 Events (reuse Ecosystem names where defined)
`GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated`, `GrievanceReopened`, `GrievanceRated`, `OmbudsmanReferralRecorded` (Ecosystem Spec §6.12), plus `in.lawdocscomply.grv.TicketAcknowledged.v1`, `…ClockWarning.v1`, `…ClockBreached.v1`, `…IOReviewCreated.v1`, `…IODecisionOverruled.v1`, `…FinalReplySent.v1`, `…ReportSubmitted.v1`, `…ConductKRIPublished.v1` (aggregates to P08).

### 7.5 Jobs
`TicketClockWorkflow`, `IOForwardingWorkflow`, `AutoCloseNoResponseJob` (where a rule permits closure after no complainant response, e.g., IRDAI 56 days [VERIFY]), `ReportSchedulerJob`, `DisplayAttestationJob` (quarterly), `KBReviewJob`, `SurveyDispatchJob`, `ConductKRIJob` (monthly).

---

## 8. Integrations

`CHANNEL_PORT` (e-mail via Graph/Gmail/SMTP-in; WhatsApp BSP; SMS via DLT-registered templates through CPaaS (TRAI TCCCPR); voice/CTI — Exotel, Ozonetel, Knowlarity; Jio Business AI voice/messaging after verification, D-14), `CUSTOMER_LOOKUP_PORT` (tenant LMS/LOS/CRM read-only: Finbyx via Ecosystem, third-party LMS via REST/SFTP), `ECOSYSTEM_PORT` (`grievance` events; grievance-host configuration), `SCORES_PORT` (manual/CSV reconciliation until an API is available — flag OFF), `BIMA_BHAROSA_PORT` (format per IRDAI [VERIFY] — flag OFF), `ODR_PORT` (Equator, SEBI SMART ODR signposting links only), `TRANSLATION_PORT`, `OCR_PORT` (P07), `CALENDAR_PORT` (IO/GRO deadlines into M365/Google calendars, P04).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `grv.ladder` (rule pack) | G | by entity family | Locked steps cannot be removed | `plt_content_publisher`; tenant adopts |
| `grv.internal_targets.<step>` | T | e.g., GRO 15 days | ≤ regulatory window | CCO |
| `grv.ack.target_hours` | T | 24 | ≤ regulatory ack window (IRDAI "immediately" → system auto-ack) | CCO |
| `grv.escalation_points` | T | [0.5, 0.75, 0.9] | — | CCO |
| `grv.reopen_window_days` | T | 30 | 0–90 | CCO |
| `grv.io.required` | L (derived) | from entity profile & thresholds | — | — |
| `grv.channels.enabled` | T | web, email | web, email, whatsapp, phone, branch, api | `ten_admin` |
| `grv.widget.languages` | T | en, hi | Eighth Schedule + UN languages for translation | `ten_admin` |
| `grv.dedupe.window_days` | T | 30 | 1–90 | CCO |
| `grv.survey.enabled` | T | ON | — | CCO |
| `grv.vidhi.draft_replies` | T | ON | human send always required | CCO |
| `grv.display_attestation.frequency_months` | T | 3 | 1–12 | CCO |
| `grv.equator_option.enabled` | T | OFF | explicit consent flow only | `ten_admin` + Legal |
| `grv.ai.triage.autonomy_level` *(v1.1)* | T | L1 | L0–L2; L2 only for queries (NN-50) | CCO with checker |
| `grv.channels.enabled` *(v1.1)* | T | WEB, EMAIL | WEB, EMAIL, WHATSAPP, VOICE, BRANCH, LETTER, SOCIAL, API | `ten_admin` |
| `grv.taxonomy.tenant` *(v1.1)* | T | family seed | must map to regulator taxonomy | GRO |
| `grv.sla.internal.<category>.<priority>` *(v1.1)* | T | rule-pack seed | ≤ statutory floor (L) | GRO |
| `grv.bulk.undo_window_hours` *(v1.1)* | T | 24 | 1–72 | GRO |
| `grv.human_route.mandatory` *(v1.1)* | L | ON | — | — |

---

## 10. Security, privacy and audit

Complainant identity and contact are a sealed class for analytics (NN-13): dashboards and Board packs use pseudonymous tokens and aggregates; agents see identity only for assigned tickets. Message bodies and attachments encrypted at rest with tenant keys; attachments malware-scanned and content-disarmed (P07). Public endpoints rate-limited, OTP-verified, bot-protected without inaccessible CAPTCHAs. All decisions, clock events, overrules and final replies ledgered (NN-02); exports with BSA s.63 certificate (NN-09). Retention: complaint records per tenant retention policy and regulator expectations (default 8 years for regulated REs [REC; VERIFY per regulator]); legal holds from P07.

---

## 11. AI touchpoints and guardrails

Vidhi: classify and detect language/sentiment (sentiment used only for priority suggestion, never to deny service); summarise long threads; suggest KB articles; draft replies in the complainant's language grounded in ticket facts, KB and fetched fields (citations to KB article ids); extract data from screenshots/letters (OCR with confidence, editable type copy); draft MIS commentary and Board papers. Prohibited: deciding outcomes, promising compensation, sending without human, telling a complainant not to approach the Ombudsman, using a complainant's complaint data for marketing (NN-14, NN-16-pattern firewall). Every AI suggestion shows "AI draft — review before sending".

---

## 12. Acceptance criteria (`tests/acceptance/p14/*.feature`)

```gherkin
Feature: NBFC IO auto-escalation
  Scenario: Partly resolved complaint is forwarded to IO within 20 days
    Given an NBFC-ND tenant with assets of 6,000 crore and a public customer interface
    And a complaint received on 1 November 2026 with no regulator-prescribed TAT
    When the GRO records "partly resolved" on 12 November 2026
    Then an IO review is created with forward-by date 21 November 2026
    And the ticket cannot be closed until the IO decides

  Scenario: Final reply within 30 days of receipt
    Given the same complaint
    Then the final-reply clock is due on 1 December 2026
    And at 90 percent elapsed the CCO receives an escalation notification

Feature: Final reply validation
  Scenario: Missing external route block blocks sending
    Given a final reply for an NBFC complaint without the RB-IOS route block
    When the GRO clicks Send
    Then the system blocks with LDC-GRV-014 "External escalation route missing"

Feature: Ecosystem intake
  Scenario: Udofin-received complaint starts clock at Udofin receipt time
    Given Udofin emits GrievanceRaised with received_at 2 November 2026 10:00 IST for RE tenant "ABC Finance"
    When LDC creates the ticket at 10:05 IST
    Then all regulatory clocks start at 10:00 IST

Feature: SCORES ladder
  Scenario: Listed company investor complaint 21-day clock
    Given a listed-company tenant
    When an investor complaint is logged with SCORES reference "SEBIE/…"
    Then a 21-calendar-day resolution clock starts and the Compliance Officer owns it

Feature: Insurer timelines
  Scenario: IRDAI insurer 14-day resolution and auto-acknowledgement
    Given an insurer tenant
    When a policyholder complaint arrives by e-mail
    Then an acknowledgement is sent immediately and a 14-day resolution clock starts

Feature: Separation of duties
  Scenario: Drafter cannot reject alone
    Given agent "A" drafted a rejection
    When "A" tries to set status REJECTED
    Then the system requires a checker other than "A"

Feature: Equator referral consent
  Scenario: No referral without consent
    When a GRO attempts to create an Equator referral for a ticket without recorded complainant consent
    Then the system blocks with LDC-GRV-022

Feature: Reports
  Scenario: IO quarterly report
    Given the quarter ending 31 December 2026
    Then a draft IO quarterly report is generated on 1 January 2027 with due date 15 January 2027

Feature: v1.1 triage, omnichannel and MIS
  Scenario: AI triage proposes but the clock starts on receipt
    Given a complaint e-mail received at 10:02 IST
    And the AI model is unavailable
    Then the acknowledgement is sent and the clock start is 10:02 IST
    And triage chips show "AI unavailable — classify manually"

  Scenario: AI cannot close a complaint
    Given grv.ai.triage.autonomy_level = L2
    When Vidhi proposes closure of a complaint (not a query)
    Then the proposal is refused by policy and routed to the agent (NN-47)

  Scenario: Unmapped tenant category blocks regulator MIS
    Given tenant category "App glitch" has no RBI category mapping
    When the GRO generates the annual complaint disclosure
    Then generation stops with a prompt to map "App glitch"

  Scenario: WhatsApp never used for recovery
    Given a case of type "recovery conduct"
    When an agent selects WhatsApp to send a notice
    Then the action is refused with LDC-GRV-023

  Scenario: Chatbot human route creates a case
    Given a customer in the tenant chatbot types "I want to complain"
    Then a case is created with clock start at that message time and the customer is offered a person
```

NN tests: `NN-01_grv_rls`, `NN-02_grv_decision_ledger`, `NN-05_grv_reject_checker`, `NN-08_no_auto_external_filing`, `NN-13_complainant_identity_sealed_in_mis`, `NN-14_vidhi_no_send`, `NN-21_public_form_accessibility`, `NN-31_grv_clocks_owned_escalated`.

---

## 13. Deliverables and exit gate

Deliverables: `grv` module; ladder packs for 14 entity families (table §4B) with citations and verification status; widget, hosted portal, SDK wrappers; channel adapters (e-mail, WhatsApp BSP, CTI logging); GRO and IO desks; MIS and 10 regulatory/governance reports; KB; model Grievance Redressal Policies per entity type (P07); tutorials (P23); documentation.

Exit gate: §12 scenarios green; pilot NBFC tenant runs 30 days of live complaints in parallel with existing process with no clock miss; accessibility audit of public form and tracker; content checker sign-off on each ladder pack (or pack remains DRAFT behind flag).

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P14-01 | RB-IOS 2026 clause numbers, the 90-day reference point, complaint definitions, coverage of co-operative banks | Salient-feature summaries only | Content (RBI CEPD) | Ladder text generic + [VERIFY] |
| OI-P14-02 | Internal Ombudsman Directions 2026 for banks, CICs, PPI issuers — thresholds and timelines | Only NBFC text verified | Content | Bank ladder DRAFT |
| OI-P14-03 | NBFC RBC Directions 2025 grievance paragraphs (GRO display, 30-day rule) | Para numbers to map | Content | Cite instrument without para |
| OI-P14-04 | SCORES 2.0 circular number and Designated Body timelines; LODR Reg 13 timeline | Verify | Content (SEBI) | 21-day clock only |
| OI-P14-05 | IRDAI 56-day closure rule, Bima Bharosa data exchange format, intermediary timelines | Verify | Content (IRDAI) | Manual Bima Bharosa updates |
| OI-P14-06 | IFSCA grievance framework instrument | Not researched | Content (IFSCA) | Generic ladder |
| OI-P14-07 | Co-operative Ombudsman (MSCS s.85A) timelines and procedure rules | Verify | Content (co-op) | Generic co-op ladder |
| OI-P14-08 | RBI annual-report complaint disclosure format per entity type | Verify current circular | Content | MIS export with all common fields |
| OI-P14-09 | Whether receipt by an LSP/DSA/recovery agent starts the RE clock | Interpretation | Counsel | Start at earliest receipt (conservative) |
| OI-P14-10 | WhatsApp policy constraints for regulated communications | Vendor terms | CTO | Channel OFF by default |
| OI-P14-11 *(v1.1)* | Exact CEPD reference numbers for IO Directions per RE category (/380–/385) | Derived from PDF serials | Content checker (RBI) | Cite title + date; number shown with [VERIFY] |
| OI-P14-12 *(v1.1)* | Social-media connector terms for complaint capture | Platform policies vary | CTO | Connector OFF |

---

## 15. Sources (accessed 25 October 2026)

1. RBI (NBFC – Internal Ombudsman) Directions 2026, RBI/CEPD/2025-26/383 or /384 [VERIFY — the v1.1 RBI catalogue lists /383 for NBFCs and /384 for non-bank PPI issuers] (14 Jan 2026): https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=13274
2. RB-IOS 2026 salient features (RE-published annexures): https://www.bandhan.bank.in/sites/default/files/2026-07/Annexure-Salient_features_of_the_Integrated_Ombudsman_Scheme_2026.pdf ; https://www.cibil.com/content/dam/cibil/corporate/documents/Salient-features-of-RB-IOS-2026-English.pdf
3. RBI Internal Ombudsman Directions 2026 (entity coverage note): https://www.outlookmoney.com/banking/rbi-issues-new-internal-ombudsman-directions-for-banks-and-nbfcs
4. SEBI SCORES 2.0: https://investor.sebi.gov.in/sebi_scores.html ; https://cafemutual.com/news/industry/31787-scores-to-resolve-grievances-within-21-days-sebi
5. IRDAI PPHI timelines (Master Circular 5 Sep 2024): https://www.mondaq.com/india/insurance-laws-and-products/1536672/irdai39s-update-on-turnaround-times-for-insurance-companies
6. Infrabyx Ecosystem Integration Specification v1.1 §6.12 (grievance events), §6.9 (ADR referral gates), §9.1 (grievance-host switch).
7. Owner's baseline — LawDocs Comply Architecture Part 1 "Customer Complaint / Grievance Form"; earlier Master Build Prompt "Grievance redressal workspace".
8. Consumer Protection (E-Commerce) Rules 2020: https://consumeraffairs.nic.in

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-33, NN-40; X-01, X-23 (no WhatsApp for recovery or legal notices).

**Added in v1.1:** NN-47, NN-50.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
