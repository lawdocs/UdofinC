# Appendix Q — Competitive Research and Improvement Backlog

**Status:** §Q.1–§Q.5 Reference; **§Q.6 (backlog IMP-001…IMP-105) and §Q.7 (governance) Binding.** · **Used by:** P01, P04–P17, P18, P19, P20, P21, P22. · LawDocs Build Prompt Pack v1.0, 25 October 2026. Sources: research note R1 (competitors and reverse engineering) and R2 (consumer-help verticals), with pricing context from R6 and funnel lessons from R4.

> **How to use.** Read §Q.2–§Q.4 to understand who LawDocs competes with and where the gaps are. Build from §Q.6: every backlog item names its module (Conventions §4) and owning phase; each phase file lists the IMP items it implements, and the phase exit gate checks them. Where an R1 item conflicts with a non-negotiable, the **conformance adjustment** in §Q.6 replaces the original wording. Competitor facts are self-published marketing material accessed 25 October 2026 unless stated; treat them as claims, not findings, until a demo or test purchase confirms them. Never copy competitor copy, taxonomies, screenshots or professional names into LawDocs material (R1 preamble).

---

## Q.1 Method and evidence rules

| Rule | Application |
|---|---|
| Evidence class | First-party page, app-store listing, press release or sponsored article = self-published; rival-authored comparisons labelled "vendor-authored"; unconfirmed items carry **[VERIFY]** |
| Access limits recorded | signdesk.com/in blocked by robots (Melento page read instead); OnlineLegalIndia TM page and Zoho India pages returned errors; Google Play not retrievable; claimbuddy.in blocked; MyAdvo, NyayGPT-type tools and the current Supreme Court status of the Rule 36 SLP not researched (R1 access notes; R2 limitations) |
| No circumvention | No scraping, scripts or proxies used; LawDocs must not use any either (NN-05) |
| Re-verification | Before any public comparison, the claims gate (OH14; NN-20) requires a dated, substantiated source; comparisons naming competitors also need counsel review [COUNSEL; VERIFY ASCI code chapter on comparative advertising] |
| Refresh cadence | Quarterly competitor review by product + marketing in OH7's competitor-intelligence register; changes to §Q.6 follow §Q.7 |

---

## Q.2 Competitor profiles (summary)

### Q.2.1 Market map

| Segment | Players | Core model | LawDocs relevance |
|---|---|---|---|
| B2C consult marketplaces | LegalKart, LawRato, (MyAdvo [VERIFY]) | Pay-per-minute or fixed-block consults; lawyer directory; free Q&A | Advisory and marketplace competitor; Rule 36 exposure |
| Business-services aggregators | Vakilsearch, IndiaFilings, OnlineLegalIndia, LegalWiz, Corpbiz | Fixed fee + government fee; back-office professionals | Business Services, Startup Desk, TM filing |
| DIY legal documents | LegalDesk, LegalKart documents, Rocket Lawyer, LegalZoom | Questionnaire templates, stamp paper print and delivery | Drafting; LawDocs adds AI, eSign, vault |
| eSign / eStamp infrastructure | Leegality, Digio, Melento (ex-SignDesk), Zoho Sign, DocuSign, Setu | API/dashboard; per-transaction or licence | Vendors behind LawDocs adapters (D-12) and benchmarks |
| CLM | SpotDraft, Provakil CLM, Ironclad | Enterprise SaaS, AI review, workflows | Company CLM benchmark |
| Litigation / ELM | Provakil, LegitQuest Patrol, eCourts (official), Manupatra/SCC Online | Court data + workflow | Litigation module benchmark |
| Legal AI / research | CaseMine AMICUS AI, Bharat.law, Indian Kanoon Prism, Jhana | Research subscriptions, AI drafting | Vidhi benchmark; possible data partners |
| Trademark tools | IP India portals, IndiaFilings TM software, Corpbiz TM Watch, StartupGrantsIndia watch, Iolite | Filing, status tracking, Journal watch | IP/TM module benchmark |
| Government lockers | DigiLocker, Entity Locker | Issued documents, consent sharing | Vault UX model; integration targets |
| Debt and loan help (R2) | FREED, SingleDebt, Settle Loan, CredSettle-type firms, AMA Legal Solutions | Settlement/consolidation programmes; anti-harassment | Consumer Help Vertical A |
| Insurance claims help (R2) | Insurance Samadhan, ClaimBuddy, broker help desks, Bima Bharosa (IRDAI) | Registration fee + success fee; hospital-side claims | Consumer Help Vertical B |
| Challans and vehicles (R2) | ChallanPay (Lawyered), Park+, Spinny, Challan Sathi, CarInfo/Cars24, API vendors | Lookup, pay, court-challan service fees | Consumer Help Verticals C–D |

### Q.2.2 Profiles

| Player | Model and pricing signals (self-published) | Strengths | Weaknesses observed | LawDocs response |
|---|---|---|---|---|
| **LegalKart** (Black Coat Technologies Pvt Ltd, Gurugram, 2018) | Prepaid wallet "LegalKart Cash" (₹1 = 1 credit); chat from ₹22/min, call from ₹31/min (named rates ₹42–₹69/min); commission 15–45% (YourStory 2022); lawyer-side app tiers ₹5,900 / ₹17,900 / ₹24,900 (iOS); court-data API pay-per-call | Issue-first tiles; voice and "Write with AI" intake; 9 language prefixes; masked numbers; AI review → expert review funnel; adjacent verticals (property, startup, ChallanWala); B2B court-data API | Credit validity contradicts across pages (1 year vs 30–180 days); non-refundable top-ups; Terms say it "does not separately verify" lawyers while marketing says "verified"; per-minute ranked advocate directory (Rule 36 exposure); thin programmatic SEO, empty FAQs, zero counters, inconsistent lawyer counts; Terms dated 2019 | Fixed-scope SKUs with assigned professionals; landed price card; refundable or non-expiring paid balance; real verification; vault-first retention; quality SEO (§Q.3) |
| **LawRato** | Directory by city/practice/court; free Q&A (150,000+ answered); Quick Consult ₹399 / 15 min | Fixed time-block consults; large Q&A corpus; NALSA pro-bono tie-up | Directory with ratings (Rule 36); inconsistent counts (10,000 vs 15,000) | Block pricing (IMP-006); opt-in, reviewed Q&A library without advocate promotion (IMP-094) |
| **Vakilsearch** | "From ₹999" registration; ₹399 GST; ₹1,499 IP; ₹4,999 accounts | Book-a-callback everywhere; product suite trial (case alerts, compliance reminders) | Complaint-site reports of refunds not received; TM page cites IPAB (abolished 2021) | Order tracker, refund engine, legal-content QA with "law as of" date (IMP-077) |
| **IndiaFilings** | TM ₹1,899 + GST (government fee payable directly); expedited ₹9,899 + GST; LEDGERS platform; APIs/webhooks | Package cards; compliance software; TM tracking software | No prices on home; duplicated descriptions | Landed price card with government fee itemised (IMP-075, IMP-079) |
| **OnlineLegalIndia** | Large catalogue; ODR listed | Breadth | States it is "not taking requests for legal consultancy"; placeholder text; "Recognised by Govt" beside "not affiliated" | Claims register; no placeholders (IMP-091, IMP-092) |
| **LegalWiz** | TM ₹1,999+; Pvt Ltd ₹2,999+; LLP ₹3,999+ | Progress tracker | Government fees not itemised despite "price you see is the price you pay" | Four-line price card |
| **Corpbiz** | Regulatory-sector depth (RBI, SEBI, IRDA, FEMA); TM Watch | Regulated-sector catalogue | No prices; unverified "#1" claim | LDC hand-off for regulated entities; NN-20 |
| **LegalDesk** | 200+ templates; stamp paper print and deliver | Live preview | No prices; no eSign or AI | Live preview (IMP-022) + eSign + vault |
| **Provakil** | Demo + ROI calculator; legal collections, ELM, AI CLM | 19K+ forums claimed; new-case alerts; daily cause lists; counsel spend; notices with India Post proof | Enterprise sales cycle; no public price | SMB self-serve pricing with the same jobs (IMP-060–IMP-067) |
| **LegitQuest Patrol** | Demo | AI case tracking; "Suggestion Alert" for new cases against a client | Limited public detail | New-case alerts via licensed data (IMP-061) |
| **eCourts (official)** | Free | CNR search, My Cases, cause list, QR per case, eFiling, ePay, virtual courts | No push alerts; no cross-court portfolio; court-complex selection friction | Parity features + explanations; licensed aggregators; never "real-time" (NN-20) |
| **Leegality** | Licence-free basic plan for small budgets | 15+ signing methods; ESP auto-switch; non-Aadhaar fallback; face match; geofencing; BharatStamp in 31 States/UTs with serial number per page | No stamp-duty calculator; B2B only | Primary aggregator candidate; add calculator and consumer UX (IMP-023, IMP-043) |
| **Digio** | API/licence | eSign, DSC, eNACH/UPI mandates, KYC, DPDP consent product | B2B infrastructure | Fallback vendor (D-12) |
| **Melento (ex-SignDesk)** | Vendor-authored comparison | 25+ States/UTs; stamp-duty calculator; master wallet; second-party payment | Site blocked for review | Split duty payment pattern (IMP-047) |
| **Zoho Sign** | ₹48 / ₹24 e-stamp processing fee; 1 credit = ₹6 | Bulk send, templates, Zoho integrations | Resells eStamp from Melento/eDrafter | Credits wallet without expiry (IMP-051) |
| **DocuSign / Setu** | Global / developer | Legality guidance; eStamp merge at start or end of PDF | — | Adapter options |
| **SpotDraft** | Mid-market/enterprise | Review in Word; negotiation in Word/Slack; approvals by deal value | — | Word add-in, approval matrix (IMP-037, IMP-040) |
| **Ironclad** | Enterprise | Create → Review → Approve → Sign → Store → Fulfil → Analyse; AI agent | — | CLM lifecycle navigation |
| **CaseMine / Bharat.law / Indian Kanoon Prism / Jhana** | Research subscriptions (some prices vendor-authored [VERIFY]) | AI research and summaries | Citation reliability concerns | Citation verifier, rules-register grounding (IMP-033; NN-14) |
| **Rocket Lawyer** | $149 / $249 / $349 per year; 7-day trial; unlimited documents, eSign, AI Q&A in every tier; attorney access by tier | Membership bundling | US market | Personal/Pro memberships with quotas (IMP-082) |
| **LegalZoom** | Attorney plans; formation packages; free tools as lead magnets; "full price before you begin" | Transparency; filing guarantee | Auto-renewing bundled subscription after 30 days (dark-pattern risk) | Free tools hub, landed price; never bundle-trap (NN-50) |
| **Clio** | Practice management | Job-to-be-done grouping; client portal | — | Practitioner workspace (P18) |
| **DigiLocker / Entity Locker** | Government | Issued vs uploaded; consent sharing with revocation; nodal admin; audit of document actions | API availability for Entity Locker [VERIFY] | "Issued/Uploaded" classes, consent sharing (IMP-053–IMP-055); vault is not a DLSP (R3 LG-036) |
| **TM tools** (IP India eRegister, StartupGrantsIndia, Iolite, IndiaFilings, Corpbiz) | Status by OTP; weekly Journal; service-led watch subscriptions | Journal watch with similarity filters (service-led) | No portfolio + deadline engine + watch + reply drafting for SMEs | IP/TM module (IMP-070–IMP-076) |
| **FREED** (R2) | Fees only on successful settlement (blog); no public rate card | Debt programmes; "Stop Harassment" | Conflicting customer numbers; 12–36 months; credit-score harm; category unregulated (its own statement) | Documented, user-controlled grievance workflow; no "waiver" claims (NN-23) |
| **SingleDebt / Settle Loan / CredSettle-type** (R2) | ₹599 enrolment; undisclosed fees; generic 10–15% success fees [VERIFY] | Consolidated plans | Legal advice by non-law-firm entities; no entity disclosure (Settle Loan) | Separate Consumer Help entity; flat fees; success fee OFF (CH-31) |
| **Insurance Samadhan** (R2) | ₹999 registration; 20% + GST success fee (22% at legal level); withdrawal charges | Escalation ladder GRO → Bima Bharosa → Ombudsman → consumer court | No IRDAI status or entity on site; selective intake | Flat-fee drafting and tracking; user files or non-advocate representative where allowed |
| **ClaimBuddy** (R2) | Not published (site blocked) | Hospital B2B2C claims | IRDAI status unclear [VERIFY] | Not a model for LawDocs B2C |
| **ChallanPay (Lawyered)** (R2) | Not disclosed; fleet focus | Pan-India consolidation; LOTS advocate network; Cars24 partnership | Data-source questions industry-wide | Official-portal deep links; contest via engaged advocate SKU |
| **Park+** (R2) | ₹199 legal fee (online challan); ₹1,999 (court challan) | Simple pricing | No lawyer credentials or refund policy shown; penalty forwarding unexplained | Never collect fines; LawDocs fee only (NN-23) |
| **Spinny / Challan Sathi / CarInfo / Cars24** (R2) | OTP lookup; "nominal convenience fee"; content-led funnels | Vehicle-sale context | Amount/date mismatches vs official portal; unclear representatives; Vahan data-source scrutiny | Vehicle sale = agreement + RC-transfer deadline engine (CH-23) |

---

## Q.3 LegalKart reverse engineering

### Q.3.1 Reverse-engineered sitemap (R1 §3.2, paraphrased)

```
legalkart.com
├── /{lang}/  (en, hi, bn, ta, te, ml, gu, mr, pa)
│   ├── home: chat with a lawyer | talk now; popular services; advocate preview cards (₹/min); credit packs; testimonials; FAQ
│   ├── /talk-to-lawyer         problem tiles → buy wallet credits → choose expert → call/video
│   ├── chat with a lawyer      credit packs (₹299 = 10 min), any advocate, written advice
│   ├── /ask-a-lawyer           20–500 chars, "Write with AI", voice, pincode → public enquiry list
│   ├── /products               consult | AI document review (< 60 s) | lawyer document review
│   ├── /property               verification, documentation, registration, property report
│   ├── /startup                formation, contracts, licences, compliance, IP (no prices)
│   ├── /lawyer-in-cities       36 States/UTs → ~231 cities
│   ├── /find-{practice}-lawyer-in-{city}   programmatic SEO pages
│   ├── /legal-blog             trending | latest; author "LegalKart Editor"
│   └── about, advisors, careers, contact; privacy, terms, wallet terms
├── services.legalkart.com     court-data API (CNR, status, orders, cause lists; prepaid wallet)
├── lawyers.legalkart.com      lawyer management portal (noindex)
├── challanwala.com            challan check/pay, RC details, court challans via lawyers
└── apps: client app and lawyer app (iOS/Android)
```

### Q.3.2 Flows and the LawDocs counter-design

| # | LegalKart flow (observed) | Risk or weakness | LawDocs design | Phase | Click budget |
|---|---|---|---|---|---|
| F1 | Chat consult: advocate cards with ₹/min, rating, chat count → buy credits → per-minute chat | Ranked, priced advocate listing (Rule 36; Madras HC 3 Jul 2024); meter anxiety; wallet breakage | Pick an issue and a fixed slot (15/30/60 min) → pay landed price → LawDocs assigns a verified professional by area × language × State × load (IMP-001, IMP-003, IMP-006); overrun only with in-call consent | P16 | Issue → paid booking ≤ 4 taps |
| F2 | Talk now / video: problem tile → wallet → choose expert → masked call | Hero "from ₹31/min" vs cheapest featured ₹42/min; no filters | Masked VoIP with PSTN fallback (IMP-098); price shown before payment equals price charged (NN-50) | P16, P22 | ≤ 4 taps |
| F3 | Ask a lawyer: public enquiry cards; free Q&A becomes the platform's property | Users' questions published; unclear pricing | Private by default; public Q&A only with opt-in, PII redaction and professional review, no advocate promotion (IMP-094) | P21 | — |
| F4 | AI document review in under 60 s; price not shown | Unpriced | Free first AI review then credits; labelled AI output; one-click paid expert review (IMP-029, NN-14) | P06, P09 | Upload → result ≤ 2 taps |
| F5 | Expert review from ₹100/page, ≥ 3 h | — | Page-band SKU with written report, follow-up call and SLA (IMP-030) | P16 | ≤ 3 taps |
| F6 | Property: details → documents → expert call → property report | Report scope unclear | Property-purchase pack: title search request, encumbrance check, draft agreement, stamp-duty estimate, registration checklist; eSign gate blocks ineligible instruments (IMP-105, IMP-024) | P14, P08 | — |
| F7 | Startup: pick product → pay → details after payment; unquantified bundle discount | No FAQs; no prices | Startup Desk bundles with quantified discount and landed price (IMP-084, IMP-079) | P14 | ≤ 3 taps to checkout |
| F8 | ChallanWala: search → list → pay with unstated convenience fee | Convenience fee undisclosed; collects government dues | User-initiated lookup that deep-links to the official portal; LawDocs never collects fines; contest via engaged advocate SKU (IMP-017 adjusted; NN-23) | P15 | ≤ 3 taps to official portal |
| F9 | Lawyer side: lead allocation; subscription tiers; earnings | Professionals pay without assured demand; app review "paid, no cases" | No fees from advocates; assignment by objective rules; practitioner workspace with engagements, payouts, TDS/GST capture (IMP-010, IMP-087; NN-21) | P16, P18 | — |
| F10 | B2B court-data API: wallet, keys, pay per successful call | — | Developer portal with pay-per-successful-call wallet for partner apps (IMP-088); LawDocs' own court data comes from licensed providers (IMP-069) | P19 | — |

### Q.3.3 Business model and what LawDocs does instead

| LegalKart stream | Mechanism | LawDocs position |
|---|---|---|
| Consultation wallet | Prepaid closed-loop credits, short expiry, non-refundable | Paid balance refundable on request or never-expiring; bonus credits labelled; one expiry rule everywhere (IMP-085) |
| Service commission 15–45% | Take rate on professional fees | **No share of advocates', CAs', CSs' fees** (RS-LD-27 prohibited); buyer-side flat platform fee (RS-LD-23) |
| Lawyer subscriptions | ₹5,900–₹24,900 tiers | **No listing/lead/ranking fees** (RS-LD-28 prohibited); optional Pro plan as ordinary software, never affecting allocation (RS-LD-30) |
| Fixed-fee products | Property, startup, documentation | Same, with landed price and SLA |
| API | Setup + pay per call | RS-LD-16 API tier |
| Breakage | Forfeited credits | Not a revenue design goal (NN-50) |

### Q.3.4 SEO and trust gaps to exploit

1. Programmatic pages whose listings do not match the URL; no JSON-LD; unanswered FAQs; counters showing 0 → LawDocs builds fewer, better pages: SSR, matching content, answered FAQs in HTML, valid schema, named reviewer, "law as of" date (IMP-089–IMP-096; Conventions key fact 17–18).
2. Inconsistent public numbers (500+ / 1,000+ / 3,500+ / 10K+ lawyers) → one claims register reviewed monthly, wired to the OH14 claims gate (IMP-092).
3. "Verified" claims without verification → LawDocs badge only after empanelment checks (IMP-004).
4. Stale Terms (2019) and an app-store "no data collected" declaration → accurate store labels and versioned legal pages (IMP-099; P21).

---

## Q.4 Feature-gap matrices (condensed)

Legend: ● strong · ◐ partial · ○ absent · ? not verified. The LawDocs column is the target (owner brief), not current state.

### Q.4.1 Consumer and services competitors

| Capability | LawDocs | LegalKart | Vakilsearch | IndiaFilings | LegalWiz | LegalDesk | LawRato | Rocket Lawyer |
|---|---|---|---|---|---|---|---|---|
| AI drafting from conversation (labelled) | ● | ◐ | ? | ○ | ○ | ○ | ○ | ● |
| Questionnaire templates + live preview | ● | ◐ | ● | ◐ | ● | ● | ◐ | ● |
| AI document review → paid expert review | ● | ● | ? | ○ | ○ | ○ | ◐ | ● |
| Aadhaar eSign in flow (eligibility-gated) | ● | ○ | ? | ○ | ○ | ○ | ○ | ◐ |
| eStamp in flow + duty calculator | ● | ◐ | ? | ○ | ○ | ◐ | ○ | n/a |
| Counterparty negotiation with track changes | ● | ○ | ○ | ○ | ○ | ○ | ○ | ◐ |
| Personal legal vault | ● | ◐ | ◐ | ◐ | ◐ | ○ | ○ | ◐ |
| Rule 36-safe marketplace | ● | ○ | ◐ | ◐ | ◐ | n/a | ○ | n/a |
| Litigation tracking for individuals | ● | ○ | ◐ | ○ | ○ | ○ | ○ | ○ |
| TM portfolio + deadline engine + watch | ● | ○ | ◐ | ◐ | ○ | ○ | ○ | ◐ |
| Transparent landed price | ● | ◐ | ◐ | ◐ | ◐ | ○ | ◐ | ● |
| Memberships with quotas | ● | ○ | ? | ? | ○ | ○ | ○ | ● |
| Multilingual UI (10 Indian languages at launch) | ● | ● | ◐ | ○ | ○ | ○ | ◐ | n/a |
| Voice intake | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Native apps | ● | ● | ? | ? | ○ | ○ | ? | ● |
| Structured data / answered FAQs | ● | ○ | ? | ? | ? | ? | ? | ? |
| Public partner API | ● | ● | ○ | ● | ○ | ○ | ○ | ○ |

### Q.4.2 LegalOps and eSign competitors

| Capability | LawDocs | Provakil | LegitQuest | Leegality | Digio | Melento | Zoho Sign | SpotDraft | Ironclad |
|---|---|---|---|---|---|---|---|---|---|
| Templates + clause library | ● | ● | ○ | ◐ | ◐ | ? | ◐ | ● | ● |
| AI review + playbook redlines | ● | ● | ○ | ○ | ○ | ? | ○ | ● | ● |
| Maker-checker approval matrix | ● | ● | ○ | ◐ | ◐ | ? | ◐ | ● | ● |
| Negotiation room | ● | ◐ | ○ | ◐ | ○ | ? | ○ | ● | ● |
| Obligations and renewals | ● | ● | ○ | ○ | ○ | ? | ○ | ◐ | ? |
| Multi-ESP routing + DSC fallback | ● | ◐ | ○ | ● | ● | ● | ● | ○ | ○ |
| Multi-State eStamp + calculator | ● | ● | ○ | ● (no calculator) | ◐ | ● | ◐ | ○ | ○ |
| Audit-trail certificate + BSA s.63 draft | ● | ? | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | ◐ |
| Multi-forum court tracking (licensed data) | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| New-case-against-entity alerts | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Counsel and spend management | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| IP portfolio | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Notices with proof of delivery | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| SMB self-serve pricing | ● | ○ | ○ | ◐ | ○ | ○ | ● | ○ | ○ |
| Individuals as first-class users | ● | ○ | ○ | ○ | ○ | ○ | ◐ | ○ | ○ |

### Q.4.3 Consumer Help verticals (R2)

| Capability | LawDocs Consumer Help (target) | FREED | SingleDebt | Insurance Samadhan | ChallanPay | Park+ | Spinny |
|---|---|---|---|---|---|---|---|
| Separate entity + ethical wall disclosed | ● | ○ | ○ | ○ | ? | ? | n/a |
| Self-serve, user-controlled workflow with evidence locker | ● | ○ | ○ | ○ | ◐ | ◐ | ◐ |
| Forum rules enforced (who may represent where) | ● | ? | ○ | ? | ? | ? | n/a |
| Deadline engine ("waiting on" chips) | ● | ◐ | ◐ | ◐ | ◐ | ○ | ○ |
| Published, flat fees | ● | ○ | ◐ | ◐ (success-fee model) | ○ | ● | ● |
| No outcome or waiver promises | ● | ◐ | ? | ? | ◐ (98% resolution claim) | ? | ● |
| Never collects fines or dues | ● | n/a | ? | n/a | ? | ○ | ○ |
| Vehicle sale with RC-transfer deadlines | ● | n/a | n/a | n/a | ○ | ○ | ◐ |

**Reading.** LawDocs' defensible position is the **union**: an individual-grade vault and consult experience (LegalKart, DigiLocker) on top of enterprise-grade eSign/eStamp (Leegality, Melento) and LegalOps (Provakil), at SMB self-serve prices, with a lawful marketplace and a walled Consumer Help brand. Do not try to beat Leegality on eSign infrastructure: integrate two ESP/eStamp vendors and win on workflow, AI and UX (R1 §9).

---

## Q.5 Differentiation strategy

### Q.5.1 Positioning

**One app for everything legal you keep: vault + sign + case + TM + professionals.** Expressed per D-17 as **legal operations + AI + on-demand professionals** — never as a replacement for advocates (CH-14). For companies: "your legal department in one place — one CLO, Vidhi and engaged professionals". For individuals: "the app you keep for every agreement, notice, case and certificate".

### Q.5.2 Five pillars

| Pillar | What it means | Proof inside the product | Main IMP items |
|---|---|---|---|
| **Keep** (retention, not one-off consults) | Vault with issued/uploaded classes, life-event folders, reminders, export any time | Users return for reminders, hearings and renewals | IMP-053–IMP-059, IMP-097 |
| **Sign right** | Draft → negotiate → stamp → eSign with eligibility and formalities gates and evidence packs | Ineligible instruments never reach eSign; BSA s.63 certificate draft | IMP-023–IMP-025, IMP-043–IMP-050 |
| **Track** | Litigation and TM portfolios with deadline engines and plain-language explanations | Hearing briefs, Journal watch, renewal clocks | IMP-060–IMP-076 |
| **Get help lawfully** | Fixed-scope services by verified professionals assigned neutrally; transparent fees | No per-minute ranked directory; refund engine | IMP-001–IMP-012, IMP-030 |
| **Trust by design** | Landed prices, refundable balances, named grievance officer, claims register | Every competitor complaint has a counter-commitment | IMP-079, IMP-085, IMP-091, IMP-092 |

### Q.5.3 Public trust commitments (each answers a visible competitor complaint; each needs a claims-register entry before publication — NN-20)

| Commitment | Answers | Control |
|---|---|---|
| "You see the full price before you pay" | Hidden government fees, unstated convenience fees | Landed price card (IMP-079); NN-22 |
| "Your paid balance never silently expires" | Wallet expiry contradictions | Wallet policy (IMP-085) |
| "Every professional is checked before they work for you" | "Verified" without verification | Empanelment checks (IMP-004); OH9 |
| "If a professional does not show up, you get your money back automatically" | Lawyer stops responding | Refund engine (IMP-009) |
| "We never rank or sell advocates" | Rule 36 exposure | NN-21 |
| "A named grievance officer replies within the legal timelines" | Unresolved complaints | P21/Appendix X §X.6 |
| "Leave any time with all your data, in folders you can read" | Lock-in | NN-11 (IMP-058) |

### Q.5.4 Pricing differentiation (R6)

Free vault and template-lane drafting; low-priced annual Personal membership with eSign and AI allowances; Pro/Business seat-plus-usage SaaS; flat-fee fixed-slot consultations instead of per-minute ranked advocates; buyer-side platform fee shown as a separate line; retainers with eSigned SLAs and hour banks (R6 §R6.2; seeds [OWNER TO SET]).

### Q.5.5 Channel strategy

SEO and GEO as a quality moat (fewer, better, reviewed pages that AI answers can cite); free tools hub as lead magnets; AI review as the conversion engine (free AI review → paid expert review → membership; R1 §11); explainer-video and webinar funnels for SMEs only, without false urgency (Appendix X §X.3.2); partners (incubators, chambers, CA/CS firms as software partners) without fee-sharing on professional fees.

### Q.5.6 What LawDocs will not copy

Per-minute ranked advocate lists; advocate ratings, testimonials or paid placement; non-refundable short-expiry wallets; success fees for advocates; collection of fines or dues; "waiver" or "settlement guarantee" marketing; locked-player videos, fake scarcity and anchor prices; unpriced "contact us" services for standard SKUs; public Q&A published without consent; scraping any portal (NN-05, NN-21, NN-23, NN-50; LD-X01…X04).

### Q.5.7 Segment battlecards (for OH7 sales enablement; internal only)

| Segment | Main alternative today | Their pitch (paraphrased) | LawDocs pitch | Proof to show in a demo | Typical objection → answer |
|---|---|---|---|---|---|
| Individuals with a one-off need (rent, vehicle sale, notice) | LegalKart consult; LegalDesk template; local typist + stamp vendor | Talk to a lawyer now; download a template | Draft free, stamp and eSign in one flow, keep it safe for years | Rent agreement drafted, duty computed, eStamp ordered, both parties sign on phones, copy in vault, renewal reminder set | "A consult is faster" → book a fixed 15-minute slot from the same screen at a shown price |
| Individuals in a dispute (cheque bounce, property, family) | LegalKart / LawRato consults; local advocate | Many lawyers online | Notice → case tracker → hearing reminders → documents in one place; professional on a fixed scope | Notice SKU with proof of delivery; case added by CNR with plain-language status | "I already have a lawyer" → invite your advocate as a guest to the matter; LawDocs is the file, not the lawyer |
| Startups | Vakilsearch, LegalWiz, IndiaFilings | Cheapest registration | Startup Desk bundle + founders' documents + TM tracking + legal officer retainer | Bundle price card with government fees itemised; TM deadline engine | "Aggregators are cheaper" → compare the landed price, not "starting at" |
| SMEs | Aggregators + email + shared drives | Filing services | One CLO + Vidhi + approval matrix + vault + litigation and TM tracking | Contract request → approval → negotiation → eSign → obligations calendar | "We use SharePoint" → keep it; LawDocs files the signed version, links your folders and exports to them |
| Mid/large companies | Provakil, SpotDraft, in-house trackers | Enterprise legal ops | Same jobs at SMB pricing, with individuals' signatures and consumer-grade UX for business users | Board MIS pack; new-case alerts (licensed data); counsel spend | "We need on-prem" → Enterprise dedicated environment (RS-LD-04) in India |
| NBFCs / FIs | Corpbiz-type consultants; LDC for compliance | Regulatory expertise | NBFC Regulatory Retainer: RM as maker, your staff as checker; LDC for compliance under SSO | Delivery grant approval on mobile; access transparency log | "Can your team hold our portal passwords?" → yes, in your own vault, OFF by default, delegation first, every reveal logged |
| Professionals and firms | LegalKart lawyer app; Clio-type tools | Leads and practice tools | Practitioner workspace with engagements assigned on objective rules, payouts and no fees to be listed | Payout statement with TDS; Rule 36 profile editor | "Will I get leads?" → LawDocs does not sell leads; work is assigned by rule, never by payment |
| Consumers with loan/insurance/challan problems | FREED, Insurance Samadhan, Park+ | We handle everything; success fee | Your case, your control: drafts, deadlines and evidence; flat fees; you pay fines only on official portals | Waiting-on chips, Ombudsman timeline, evidence locker export | "Can you get my loan waived?" → nobody can promise that; here is what the rules let you ask for and when |

### Q.5.8 Strategy risks and mitigations

| Risk | Why it matters | Mitigation |
|---|---|---|
| Slower marketplace supply without per-minute earnings or paid visibility | Professionals may prefer platforms that send leads | Assured engagement flow from LawDocs SKUs; fast payouts; practitioner tools; transparent assignment statistics shown to each professional privately |
| Higher price perception against "starting at" competitors | Landed prices look higher than headline fees | Show side-by-side "what you actually pay" explainer without naming competitors unless substantiated (§Q.1) |
| Court and TM data dependency on licensed vendors | Vendor outages or terms changes | Two vendors behind the abstraction; user-entered fallback; staleness labels (IMP-069) |
| AI drafting regulated as high-risk legal use for individuals | Free AI drafts could breach the provider policy | Two-lane drafting (template lane free; AI-custom lane labelled with paid review) (NN-14, CH-30) |
| Consumer Help reputational spill-over to lender-side group products | Group conflict perception | Separate brand, entity, staff and data; hashed conflict checks; published ethical-wall statement (NN-23) |
| Competitors copying the "keep" model | Low switching costs early | Data portability as a feature (users can leave, so they trust staying); depth of life-event folders and reminders; integrations with DigiLocker and workplace suites |

---

## Q.6 Binding improvement backlog (IMP-001 … IMP-105)

Priority (from R1): **P0** launch-blocking for its wave · **P1** phase 2 · **P2** later. Module codes per Conventions §4. "Phase" is the owning phase; a second phase in brackets contributes. **Adj.** = conformance adjustment that replaces R1's wording.

| ID | Module | Improvement (binding wording) | Source | Pri | Phase |
|---|---|---|---|---|---|
| IMP-001 | `mkp` | Sell fixed-scope, fixed-price service SKUs; never a per-advocate per-minute directory | Rule 36; P.N. Vignesh | P0 | P16 |
| IMP-002 | `mkp` | Rule 36-safe advocate profile (name, qualifications, enrolment no. and State Bar Council, areas, languages, contact); no public advocate ratings or rankings; per-profession switches; directory OFF by default | BCI r.36 (2008); BCI 17 Mar 2025 | P0 | P16 (P18) |
| IMP-003 | `mkp` | Assignment engine (area × language × State × load × SLA history, rotation) with "request a different professional"; never paid or rating-based | LawRato assignment | P0 | P16 |
| IMP-004 | `mkp` | Real verification at empanelment (enrolment, COP/ID, ICAI/ICSI membership, PAN, bank) via OH9; yearly re-verification; badge only after checks | LegalKart Terms | P0 | P16 |
| IMP-005 | `mkp` | Consult modes: async chat with response SLA, scheduled audio/video, instant call; masked numbers both ways; recording OFF by default | LegalKart chat/talk | P0 | P16 (P22) |
| IMP-006 | `bil` | Block pricing (15/30/60 min) shown before payment; overrun only with explicit in-call consent; no hidden meter | LegalKart per-minute; LawRato | P0 | P16 (P17) |
| IMP-007 | `ai` | Consult summary and action list from the transcript with consent, approved by the professional, filed to the vault | Gap at all competitors | P1 | P09 (P16) |
| IMP-008 | `mkp` | 48-hour free follow-up chat after each consult | "Lawyer stops responding" | P1 | P16 |
| IMP-009 | `bil` | Refund engine: auto-refund on professional no-show or dropped call; partial refunds; grievance officer SLA displayed | App reviews; E-Commerce Rules 2020 [VERIFY clauses] | P0 | P17 (P16) |
| IMP-010 | `mob` | Professional app/workspace: request inbox, calendar, deliverables, earnings, payouts, auto invoice, TDS and GST capture | LegalKart lawyer app; Clio | P1 | P18 (P22) |
| IMP-011 | `bil` | **Adj.** No commission on advocates', CAs' or CSs' fees and no lead promises; take rates only on non-regulated providers (RS-LD-25); professionals may buy the Pro plan as ordinary software that never affects allocation (RS-LD-30) | Review "paid subscription, no cases"; NN-21, D-05 | P1 | P17 |
| IMP-012 | `sdc` | QA layer: sample peer review, client delivery confirmation, SLA breach auto-escalation to the delivery lead and OH | Vakilsearch complaints | P1 | P18 (P16) |
| IMP-013 | `msg` | **Adj.** Off-platform leakage warnings on in-platform chat only (phone/email patterns), disclosed in terms, friendly prompt, no penalties without human review; no monitoring outside the platform (NN-33) | LegalKart anti-leakage clause | P2 | P16 |
| IMP-014 | `chp` | Issue-first tiles (cheque bounce, online fraud/blackmail, recovery harassment, insurance rejection, employer dues, property purchase, custody) → triage → DIY / notice / consult / complaint | LegalKart tiles | P0 | P15 (P21) |
| IMP-015 | `ai` | Voice-note intake in the D-07 launch languages with transcription, translation and an editable summary (machine translation labelled; NN-48) | LegalKart voice note | P0 | P09 (P05) |
| IMP-016 | `ai` | "Help me describe my problem" assistant prompting for missing facts (dates, amounts, parties) | LegalKart "Write with AI" | P1 | P09 |
| IMP-017 | `chp` | **Adj.** Challan lookup by user-initiated official-portal deep link or uploaded challan SMS/PDF; payment only on the official portal; LawDocs never collects fines; court/virtual-court challans → engaged advocate fixed-fee SKU (NN-23, CH-22) | ChallanWala; R2 decision 7–8 | P1 | P15 |
| IMP-018 | `chp` | Consumer-complaint builder for the national e-filing portal with a pecuniary-jurisdiction calculator [VERIFY e-Jagriti current] | Vakilsearch consumer complaint | P1 | P15 |
| IMP-019 | `chp` | Grievance tracker for RBI CMS/Integrated Ombudsman, IRDAI Bima Bharosa, NCH with escalation timers; the user files or a non-advocate representative where the scheme allows [VERIFY timelines] | Owner brief; R2 | P1 | P15 |
| IMP-020 | `pld` | Legal-notice SKU with multilingual templates and proof of delivery (India Post tracking, email, opt-in WhatsApp) | Provakil notices | P0 | P10 (P16) |
| IMP-021 | `web` | **Adj.** Every document/service page embeds "Draft free with Vidhi" (template lane free; AI-custom lane labelled "AI draft — not reviewed by a professional") plus "Hire a professional" (NN-14, CH-30) | Owner brief; LegalKart funnel | P0 | P21 (P06) |
| IMP-022 | `drf` | Live document preview updating as the questionnaire is answered | LegalDesk | P0 | P06 |
| IMP-023 | `sgn` | State × instrument stamp-duty calculator in drafting and checkout (rule tables, effective-dated; NN-30) | Melento has it | P0 | P08 (P21) |
| IMP-024 | `sgn` | eSign-eligibility checker (Appendix F) blocks the eSign CTA for IT Act First Schedule instruments and routes to wet-sign/notary/registration packs (NN-07) | IT Act s.1(4) | P0 | P08 (P06) |
| IMP-025 | `sgn` | Registration-required flag (Registration Act 1908 s.17; leases > 11 months) with Sub-Registrar checklist (NN-40) | Legal guardrail | P1 | P08 |
| IMP-026 | `sgn` | Physical stamp paper print-and-deliver for uncovered States through authorised vendors only (NN-08) | LegalDesk | P2 | P08 |
| IMP-027 | `drf` | Bilingual execution copy side by side with a governing-language clause; translations labelled and reviewed (NN-48) | Vernacular positioning | P1 | P06 |
| IMP-028 | `tpl` | Conditional templates with clause variants, fallbacks and "i" explanations | SpotDraft | P1 | P06 |
| IMP-029 | `ai` | Instant AI review (risks, missing clauses, red flags, plain summary) < 60 s; free quota then credits; labelled | LegalKart; Rocket Lawyer | P0 | P06 (P09) |
| IMP-030 | `mkp` | Expert review SKU priced by page band, written report + follow-up call, turnaround SLA | LegalKart ₹100/page | P0 | P16 |
| IMP-031 | `ai` | Legal Q&A grounded in bare acts (BNS/BNSS/BSA current) with section-level citations and "ask a professional" escalation; general information only for individuals (NN-14) | Rocket Lawyer; LegalZoom | P0 | P09 |
| IMP-032 | `clm` | Company playbooks → automatic redlines and fallback positions | Provakil, SpotDraft | P1 | P07 |
| IMP-033 | `ai` | Citation verifier: every section or judgment resolved against the rules register or retrieved source; unresolved shown "unverified" | Citation-reliability concerns | P0 | P09 |
| IMP-034 | `dix` | OCR of handwritten notes and WhatsApp screenshots → typed copy + translation, editable, attached as annexure; originals immutable (NN-09, CH-28) | Owner brief | P1 | P05 (P10) |
| IMP-035 | `agt` | Agent jobs: chase signatures, watch hearings, draft TM replies, renewal reminders, weekly legal digest — maker-only, human confirmation for external actions (NN-13, NN-43) | Ironclad agent | P1 | P09 |
| IMP-036 | `clm` | Business-user intake forms (request an NDA/vendor contract) with auto-template selection | Ironclad launch forms | P1 | P07 (P13) |
| IMP-037 | `clm` | Approval matrix by contract type, value and department with maker-checker and delegation | SpotDraft routing | P0 | P07 (P02) |
| IMP-038 | `clm` | Negotiation room: track changes, comments, version compare, counterparty chat, all in the audit trail (NN-37) | Owner brief; SpotDraft/Leegality | P0 | P07 |
| IMP-039 | `clm` | Obligation, renewal and expiry extraction → calendar and owners | Provakil AI | P1 | P07 |
| IMP-040 | `clm` | MS Word add-in and Google Docs add-on for review and redlines | SpotDraft; Provakil | P2 | P07 (P19) |
| IMP-041 | `dms` | Bulk import of legacy contracts through the folder structure with AI metadata extraction | Owner brief; Ironclad | P1 | P04 (P20) |
| IMP-042 | `rpt` | Contract analytics: TAT, bottleneck step, renewals due, value at risk | Provakil; SpotDraft | P2 | P07 |
| IMP-043 | `sgn` | Multi-ESP routing with auto-failover and non-Aadhaar fallback (DSC/document signer) via aggregators (D-12) | Leegality | P0 | P08 |
| IMP-044 | `sgn` | **Adj.** Optional signer controls (face match, geofence, ID check, OTP to registered mobile) only through the ESP/aggregator's own features; LawDocs performs no Aadhaar face authentication (NN-03, NN-04) | Leegality, Melento | P1 | P08 |
| IMP-045 | `sgn` | Audit-trail certificate appended to the signed PDF + evidence pack + BSA s.63(4) certificate draft (NN-10) | Leegality | P0 | P08 |
| IMP-046 | `sgn` | eStamp vendor abstraction (SHCIL / Melento / eDrafter / Setu-type) with State coverage map and expected processing time | Zoho Sign; Setu | P0 | P08 |
| IMP-047 | `sgn` | Split or second-party stamp-duty payment and "who pays" clause sync; duty passed through via Route (NN-22) | Melento | P1 | P08 (P17) |
| IMP-048 | `sgn` | Bulk send from Excel/CSV (offer letters, NDAs, DSA agreements) | Zoho, Leegality | P1 | P08 |
| IMP-049 | `sgn` | Signing order, reminders (NN-34 limits), expiry, decline-with-reason, reassign signer | Zoho Sign | P0 | P08 |
| IMP-050 | `sgn` | Stamp certificate number printed on every page | Leegality BharatStamp | P1 | P08 |
| IMP-051 | `bil` | Business credits wallet for eSign/eStamp with per-unit price list and no expiry on paid credits | Zoho credits | P1 | P17 |
| IMP-052 | `dms` | Public verification page/QR for LawDocs-executed documents (hash check; no content disclosed) | eCourts QR; DigiLocker | P1 | P04 (P08) |
| IMP-053 | `dms` | "Issued" vs "Uploaded" document classes; DigiLocker pull under requester terms (NN-42) | DigiLocker | P0 | P04 (P01) |
| IMP-054 | `dms` | Consent-based, time-bound, revocable sharing with an owner-visible access log | Entity Locker | P0 | P04 |
| IMP-055 | `org` | **Adj.** Company vault roles: nodal admin with authorisation letter, members verified by OTP and, where needed, Aadhaar offline verification (never Aadhaar login or full-number storage; NN-03, NN-04), department scopes | Entity Locker | P1 | P02 (P04) |
| IMP-056 | `dms` | Nominee/legal-heir access with verification and waiting period (`IND_NOMINEE`) | DigiLocker-type expectation [VERIFY] | P2 | P04 |
| IMP-057 | `dms` | Life-event smart folders (Property, Vehicle, Family, Work, Litigation, Tax, Business) with auto-filing as views over canonical ids (NN-12) | DigiLocker categories | P1 | P04 |
| IMP-058 | `xpt` | One-click export in human-readable folders + manifest + PDF/A (`LD-EXPORT-1.0`; NN-11) | Owner brief | P0 | P20 |
| IMP-059 | `dms` | Expiry and renewal reminders on any document | LegalZoom, Rocket Lawyer | P1 | P04 |
| IMP-060 | `lit` | **Adj.** Add a case by CNR/case no./party/advocate/FIR; status, next date and orders from licensed aggregators or user entry with manual refresh; staleness labelled; never "real-time" (NN-05, NN-20) | eCourts parity | P0 | P11 |
| IMP-061 | `lit` | New-case-filed-against-entity alerts by party-name variants via a licensed provider [VERIFY provider terms] | Provakil; LegitQuest | P1 | P11 |
| IMP-062 | `lit` | Personalised daily cause list across tracked courts, push at 07:00 | Provakil | P1 | P11 |
| IMP-063 | `lit` | External counsel management: stage-based fee schedules, invoices, performance, spend | Provakil | P1 | P11 (P13) |
| IMP-064 | `lgo` | Contingent-liability register and quarterly board MIS pack | Provakil MIS | P1 | P13 |
| IMP-065 | `ai` | Hearing brief before each date: last order, pending compliance, documents, questions for counsel | Gap | P1 | P11 (P09) |
| IMP-066 | `lit` | Bulk case import (Excel template) with dedupe on CNR | Enterprise onboarding | P0 | P11 |
| IMP-067 | `lit` | Lender recovery pipeline (demand notice → s.138 / SARFAESI / arbitration) with hand-off to the Finbyx Recovery Suite through Ecosystem contracts only (Appendix X §X.18); loan-dispute ADR referrals are made only by the RE through the Recovery Suite — LawDocs never refers a loan dispute (Appendix Y §Y.7.4) | Provakil Legal Collections | P1 | P11 (P19) |
| IMP-068 | `lit` | Individual-litigant explainer: "what this status means", "what happens next", legal-aid link | Owner brief | P0 | P11 |
| IMP-069 | `int` | Court-data provider abstraction (licensed API first, user-entered fallback); no scraping (NN-05) | R1 §5.2 | P0 | P19 (P11) |
| IMP-070 | `ipm` | TM portfolio tracker mapped to the IP India status taxonomy (R1 §7.2) | Intepat guide | P0 | P12 |
| IMP-071 | `ipm` | TM deadline engine (exam reply, opposition 4 months, counter-statement 2 months, renewal 10 years, removal/restoration) as editable rule tables (Trade Marks Act 1999 ss.21, 25; Rules 2017 [VERIFY periods]) | R3 LG-170 | P0 | P12 |
| IMP-072 | `ipm` | Weekly Journal watch (phonetic, visual, conceptual, transliteration; adjacent classes) via licensed partner, with professional review queue | StartupGrantsIndia; Iolite | P1 | P12 |
| IMP-073 | `ipm` | AI Nice-class finder from a business description (advisory) | IndiaFilings class finder | P0 | P12 |
| IMP-074 | `ipm` | Pre-filing knock-out search with conflict score and explanation (advisory) | Weak phonetic search | P1 | P12 |
| IMP-075 | `bsv` | TM price card showing the government fee by applicant type separately [VERIFY Trade Marks Rules 2017 First Schedule] | IndiaFilings/LegalWiz opacity | P0 | P14 (P17) |
| IMP-076 | `ipm` | **Adj.** Digital brand watch (domains, marketplaces, social handles) only through licensed or official data sources; no scraping | StartupGrantsIndia; Intepat | P2 | P12 |
| IMP-077 | `web` | Legal-content QA: no obsolete forums or laws (IPAB → High Court; IPC → BNS); "law as of" date on every page | Vakilsearch IPAB reference | P0 | P21 (P06) |
| IMP-078 | `bsv` | Catalogue by life stage: Start / Run / Protect / Resolve / Exit; individuals: Home / Family / Money / Work / Vehicle | Clio grouping | P0 | P14 (P21) |
| IMP-079 | `bil` | Landed price card: professional fee + government/statutory fee (basis) + GST = total; exclusions, refund rule, SLA (NN-22) | LegalZoom | P0 | P17 (P21) |
| IMP-080 | `bsv` | Order tracker with milestones and % complete, updates by email/in-app and opt-in WhatsApp/SMS (NN-34) | LegalWiz; LegalKart | P0 | P14 |
| IMP-081 | `lgo` | Compliance calendar from the entity profile (CIN/GSTIN), linked to LDC for regulated entities (D-10) | Vakilsearch; IndiaFilings | P1 | P13 (P19) |
| IMP-082 | `bil` | Memberships for individuals, startups and SMEs with quotas (questions, calls, reviews, notices) and add-on discounts | Rocket Lawyer | P0 | P17 |
| IMP-083 | `bsv` | **Adj.** "Accurate filing" rework commitment: free rework if LawDocs erred, with defined terms and a claims-register entry; never an outcome guarantee (NN-20) | LegalZoom | P2 | P14 |
| IMP-084 | `bsv` | Startup Desk bundles (incorporation + founders' agreement + ESOP + TM + website policies) with quantified bundle discount | LegalKart startup page | P1 | P14 |
| IMP-085 | `bil` | Wallet policy: paid balance refundable on request or never expiring; bonus credits labelled; one expiry rule stated identically everywhere (NN-50) | LegalKart inconsistency | P0 | P17 |
| IMP-086 | `bil` | **Adj.** 7-day free trial on memberships with no automatic conversion unless the user opted in at checkout and receives a pre-charge reminder; first AI review free (NN-50) | Rocket Lawyer | P1 | P17 |
| IMP-087 | `bil` | Professional payouts via Route with TDS capture, GST invoices in the professional's name (self-billing only where permitted) and payout statements [TAX MEMO] | LegalKart earnings | P1 | P17 (P16, P18) |
| IMP-088 | `int` | Developer API wallet (pay per successful call; failed calls free) for partner apps (RS-LD-16) | services.legalkart.com | P2 | P19 (P17) |
| IMP-089 | `web` | Programmatic pages (service × city × language) only where real content matches; valid JSON-LD (Service, BreadcrumbList, Organization; FAQPage/HowTo only where valid) | LegalKart mismatch | P0 | P21 |
| IMP-090 | `web` | FAQ answers rendered server-side in HTML; questions mined from search and consented Q&A data | LegalKart empty FAQs | P0 | P21 |
| IMP-091 | `web` | Server-rendered stats from the claims register; never show 0 or placeholder text | Zero counters; placeholders | P0 | P21 |
| IMP-092 | `web` | Single claims register for public numbers, reviewed monthly, enforced via the OH14 claims gate | Inconsistent counts | P0 | P21 |
| IMP-093 | `web` | Language-prefixed URLs with full hreflang cluster; translated (not machine-only) pillar pages | LegalKart `/hi/`, `/gu/` | P1 | P21 |
| IMP-094 | `web` | Public Q&A library only with explicit opt-in, PII redaction and professional review; no advocate promotion | LawRato; Rule 36 | P1 | P21 |
| IMP-095 | `web` | Free tools hub: stamp duty, TM class finder, limitation period, notice period/gratuity, rent-agreement cost, eSign eligibility | LegalZoom tools | P1 | P21 |
| IMP-096 | `web` | Named, credentialed reviewer + "reviewed on" date on every guide (E-E-A-T) | "LegalKart Editor" byline | P1 | P21 |
| IMP-097 | `mob` | App: biometric lock, encrypted offline vault cache, push for hearings, deadlines and signing requests (NN-44) | eCourts; DigiLocker apps | P0 | P22 |
| IMP-098 | `mob` | In-app VoIP consult with PSTN fallback and masked numbers; recording OFF by default | LegalKart internet call | P1 | P22 (P16) |
| IMP-099 | `mob` | Accurate app-store privacy labels and data-safety forms; payments flow reviewed against store rules for real-world services [VERIFY store rules] | LegalKart "no data collected" | P1 | P22 |
| IMP-100 | `ntf` | WhatsApp Business channel (opt-in) for status, document delivery and payment links; never for legal notices or recovery (NN-34; R6 D-31) | LegalKart/ChallanWala | P1 | P19 (P22) |
| IMP-101 | `pld` | Court-specific pleading templates with format rules (paper, margins, font, spacing) per High Court/district rules [VERIFY per court] | Gap | P1 | P10 |
| IMP-102 | `pld` | Annexure builder: auto index, pagination, typed copies, translations, true-copy endorsement, PDF bundling | Owner brief; Provakil | P1 | P10 |
| IMP-103 | `pld` | Vakalatnama and memo-of-appearance generator; e-filing-ready PDF/A | eCourts eFiling | P2 | P10 |
| IMP-104 | `lgo` | Legal risk dashboard (IP/TM, litigation, contracts, notices) for KMPs and the board | Provakil ELM + MIS | P1 | P13 |
| IMP-105 | `bsv` | **Adj.** (reclassified from R1 "Consumer Help" to Business Services) Property-purchase pack: title search request via engaged advocate, encumbrance check, draft agreement, stamp-duty estimate, registration checklist; sale deeds routed to registration, not eSign (NN-07) | LegalKart Property Report | P1 | P14 (P08) |

### Q.6.1 Backlog by phase (counts)

| Phase | IMP items | P0 count |
|---|---|---|
| P01 | (053 contributing) | — |
| P02 | 055 | 0 |
| P04 | 041, 052, 053, 054, 056, 057, 059 | 2 |
| P05 | 034 (015 contributing) | 0 |
| P06 | 022, 027, 028, 029 | 2 |
| P07 | 032, 036, 037, 038, 039, 040, 042 | 2 |
| P08 | 023, 024, 025, 026, 043–050 | 6 |
| P09 | 007, 015, 016, 031, 033, 035 | 3 |
| P10 | 020, 101, 102, 103 | 1 |
| P11 | 060–063, 065–068 | 3 |
| P12 | 070–074, 076 | 3 |
| P13 | 064, 081, 104 | 0 |
| P14 | 075, 078, 080, 083, 084, 105 | 3 |
| P15 | 014, 017, 018, 019 | 1 |
| P16 | 001–006, 008, 013, 030 | 7 |
| P17 | 009, 011, 051, 079, 082, 085, 086, 087 | 4 |
| P18 | 010, 012 | 0 |
| P19 | 069, 088, 100 | 1 |
| P20 | 058 | 1 |
| P21 | 021, 077, 089–096 | 6 |
| P22 | 097, 098, 099 | 1 |

(Counts reflect owning phases; contributing phases are noted in the table above.)

### Q.6.2 Wave alignment

P0 items in Wave-1 phases (P01–P04, P06–P08, P09 runtime, P17, P19 core, P20 core, P21 core) are Wave-1 launch blockers. P0 items owned by Wave-2/3 phases (e.g., IMP-001–IMP-005 in P16, IMP-060 in P11, IMP-070 in P12, IMP-014 in P15, IMP-097 in P22) block that phase's exit, not Wave 1. Wave 1 sells marketplace services only as LawDocs first-party fixed-scope SKUs with the minimum of IMP-001, IMP-006, IMP-079 and IMP-085 in place [REC].

---

## Q.7 Backlog governance (binding)

1. **Ownership.** Each IMP item is implemented in its owning phase; the phase file's "Requirements covered" or FR text cites the IMP id; the phase exit gate lists IMP items delivered, deferred (with reason) or adjusted.
2. **Acceptance.** Each implemented item has at least one Gherkin scenario tagged with the IMP id alongside the phase tag (e.g., `@P16-AT-07 @IMP-006`).
3. **Conformance first.** No IMP item may be implemented in a way that breaches an NN rule; where wording conflicts, the **Adj.** text governs, and new conflicts are raised as change requests to this appendix.
4. **New items.** IDs IMP-106 onwards are reserved for items found in quarterly reviews, test purchases or customer feedback (OH5 feedback loop); each needs source, module, priority and phase, approved by the product owner and checked by a second reviewer.
5. **Claims.** Any public statement derived from §Q.2–§Q.4 (e.g., "only app that…") needs a claims-register entry with dated evidence and passes the OH14 claims gate (NN-20). Internal matrices are never published as-is.
6. **Test purchases.** Before go-live of P16 and P15, run test purchases on LegalKart (AI review price, wallet terms), one TM aggregator and one challan service to confirm the [VERIFY] items below; record results in `docs/compliance/verification-log.md`.

## Q.8 Carried [VERIFY] items

| Item | Needed by | Fallback |
|---|---|---|
| Current Supreme Court status of the Rule 36 SLPs (Sulekha; JustDial) | P16 | Assume the Madras HC position applies |
| IT Act First Schedule current text and any amendments | P08 (Appendix F) | Block all doubtful instruments from eSign |
| Trade Marks Rules 2017 fee schedule (TM-A, TM-O) and response periods | P12, P14 | Show "government fee at actuals" with link |
| e-Jagriti current status and consumer-commission pecuniary limits | P15 | Link to official portal only |
| ICAI/ICSI advertisement and aggregator guidelines (2026) | P16 | CA/CS listings OFF |
| LegalKart AI-review price; whether lawyer-app tiers recur; Google Play ratings | Q refresh | Exclude from public comparisons |
| MyAdvo, NyayGPT-type tools | Q refresh | Not compared |
| Entity Locker API availability | P04 | Manual upload |
| Corpbiz TM Watch scope; IndiaFilings TM software depth | P12 | — |
| "ChallanWallah" brand name intended by the owner (likely ChallanPay or Challan Sathi — R2) | P15 | Benchmark ChallanPay and Park+ |
| IRDAI position on claim-assistance entities; RB-IOS 2026 representation clause text | P15 | User self-files; non-advocate representation OFF until counsel confirms |
