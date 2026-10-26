# R1 — Competitors and Reverse Engineering (LawDocs)

> Research stream R1 for the LawDocs build-prompt pack. Research date: **25 October 2026**. Every competitor statement here comes from the competitor's own website, app-store listing, press release or sponsored article, so treat it as **self-published marketing material** until a demo or test purchase confirms it. Third-party comparison pages written by a rival vendor are labelled as such. Claims I could not confirm from a first-party page are marked **[VERIFY]**. Competitor text is paraphrased; short quotes are in quotation marks. Do not reuse competitor copy, taxonomies, screenshots or lawyer names in LawDocs material.

**Access notes (what could not be fetched):**
- `signdesk.com/in/` was blocked by robots.txt. A SignDesk comparison URL redirected to `melento.ai` (SignDesk is now **Melento**), and that page was read.
- `onlinelegalindia.com/trademark-registration/` returned a client error. Only the homepage was read.
- `zoho.com/in/sign/` and the Zoho e-stamping blog returned client errors. The `zoho.com/en-in/sign` page and the Zoho help-centre article were read.
- Google Play listings could not be retrieved. App data comes from the Apple App Store listings.
- The shared web-search budget ran out near the end of the stream. MyAdvo, Corpbiz's trademark-watch detail page, Nyay/NyayGPT-type tools and the current status of the Supreme Court Rule 36 matter were therefore not researched further. They are marked [VERIFY].
- No curl, scripts or proxies were used to get around a block.

---

## 1. Key findings (one page)

1. **LegalKart is a pay-per-minute consultation marketplace with a wallet.** Its other products (AI document review, expert review, property, startup services, challans, court-data API) feed that core. Revenue comes from three places: user wallet top-ups ("LegalKart Cash", ₹1 = 1 credit, non-refundable), a commission of **15–45%** on services (YourStory, 2022), and lawyer-side fees (₹1,499–4,999 a year in 2022; the iOS lawyer app now lists in-app tiers of **₹5,900 / ₹17,900 / ₹24,900**). [App Store; YourStory]
2. **The weak points are the wallet and lawyer quality.**
   - The homepage says credits are "valid one year". The LegalKart Cash Terms say credits expire after **30–180 days** and are forfeited.
   - Purchases are non-refundable.
   - The Terms of Use say LegalKart "does not separately verify" lawyer qualifications, while the marketing says "verified advocates".
   - App reviews complain that a recharged balance showed zero, that a lawyer stopped responding, and that a lawyer paid for a subscription and received no cases.
   - LawDocs can win on **transparent pricing, refundable or clearly stated balances, verified professionals and SLA-backed delivery**.
3. **Regulatory risk applies to every lawyer directory.**
   - On **3 July 2024** the Madras High Court (P.N. Vignesh) held that platforms listing, rating, pricing and categorising advocates (Sulekha, Justdial, Quikr) facilitate solicitation under **BCI Rule 36**. It also held they lose **s.79 IT Act** safe harbour.
   - The Supreme Court issued notice in the Sulekha SLP (Nov 2024). I found no stay. [VERIFY current status]
   - BCI followed with a press release on 17 March 2025.
   - **Consequence for LawDocs:** design the marketplace as **LawDocs-sold, fixed-scope services delivered by empanelled professionals that LawDocs assigns**, not as a ranked, per-minute directory of advocates.
4. **LegalKart's SEO is wide but thin.**
   - It runs programmatic `/en/find-{practice}-lawyer-in-{city}` pages in 9 language prefixes.
   - Content mismatches: a "Trademark & Copyright Lawyers in Kakinada" page shows family and criminal lawyers.
   - No JSON-LD was visible. FAQ questions have no answers on the page. Stat counters render as 0.
   - Lawyer counts disagree across its own pages: 500+, 1,000+, 3,500+ and 10K+.
   - This is a real opening for LawDocs content that is high quality, consistent and schema-marked.
5. **Indian service aggregators all quote "starting at" professional fees and keep government fees separate,** usually without itemising them:
   - LegalWiz: trademark ₹1,999+, Pvt Ltd ₹2,999+
   - IndiaFilings: trademark ₹1,899+ GST, government fee "payable directly"; expedited ₹9,899+ GST
   - Vakilsearch: "from ₹999" business registration, "from ₹1,499" IP
   - None shows a full landed price up front. LegalZoom's "you will always know the full price before you begin" is the pattern to adopt.
6. **On eSign and eStamp, the Indian leaders compete on reliability and fraud controls, not on signing itself.**
   - Leegality offers 15+ eSign methods, auto-switch to the eSign Service Provider (ESP) with best uptime, a non-Aadhaar fallback, face match, geofencing, and BharatStamp in 31 States/UTs with a serial number on every page.
   - Melento (ex-SignDesk) offers a stamp-duty calculator, a master wallet and second-party payment.
   - Zoho Sign resells e-stamping from Melento and eDrafter at a **₹48 / ₹24 processing fee** per transaction.
   - LawDocs should use several vendors behind one abstraction.
7. **LegalOps benchmark: Provakil.**
   - Litigation module: updates from 19K+ forums, alerts when a new case is filed against the company, daily cause lists, counsel spend and contingent-liability MIS.
   - CLM: AI review with playbook redlines, Word collaboration, eSign and eStamp.
   - Collections: bulk notices with India Post proof of delivery.
   - LegitQuest Patrol offers a similar "Suggestion Alert" for new cases filed against a client.
8. **Trademark tools are fragmented.**
   - IP India offers eRegister status behind an OTP, public search, the weekly Journal and e-filing. Registry emails go only to the address for service.
   - Aggregators sell "TM tracking software" and annual watch subscriptions.
   - Nobody combines **portfolio tracking + deadline engine + journal similarity watch + one-click reply drafting** for an SME at a low price.
9. **Global patterns worth copying:**
   - Rocket Lawyer: annual membership ($149 / $249 / $349) bundling AI Q&A, unlimited documents, eSign, a quota of attorney questions and calls, and add-ons.
   - LegalZoom: free tools as lead magnets, an accurate-filing guarantee, recurring compliance.
   - Clio: features grouped by job-to-be-done, plus a client portal.
   - Ironclad: Draft → Review → Approve → Sign → Store → Fulfil → Analyse lifecycle.
   - DigiLocker and Entity Locker: issued versus uploaded documents, consent-based sharing, Aadhaar-verified authorised persons, 10 GB entity storage.
10. **Biggest open gap in the market:** no Indian player joins **draft → negotiate → stamp → eSign → store → track (litigation, TM, obligations) → get professional help** in one consumer-grade app that an individual keeps the way they keep DigiLocker. LegalKart is consult-first, Leegality and Digio are B2B infrastructure, Provakil is enterprise and Vakilsearch is a services catalogue.

---

## 2. Market map

| Segment | Players reviewed | Core model | Relevance to LawDocs |
|---|---|---|---|
| B2C consult marketplaces | LegalKart, LawRato, (MyAdvo [VERIFY — not researched]) | Pay-per-minute or fixed-block consults, lawyer directory, free Q&A | Direct competitor for advisory and Consumer Help; Rule 36 exposure |
| Business-services aggregators | Vakilsearch, IndiaFilings, OnlineLegalIndia, LegalWiz, Corpbiz | Fixed-fee services + government fee, CA/CS/lawyer back office, some compliance software | Competes with Business Services, Startup Desk and TM filing |
| DIY legal documents | LegalDesk, LegalKart documents, Rocket Lawyer, LegalZoom | Questionnaire templates, stamp paper print/deliver | Competes with Drafting; LawDocs adds AI + eSign + Vault |
| eSign / eStamp infrastructure | Leegality, Digio, Melento (ex-SignDesk), Zoho Sign, DocuSign, Setu | API / dashboard, per-transaction or licence pricing | Vendors and benchmarks for the eSign/eStamp module |
| CLM | SpotDraft, Provakil CLM, Ironclad | Enterprise SaaS, AI review, workflows | Benchmark for the CLM module for companies |
| Litigation / ELM | Provakil, LegitQuest Patrol, Manupatra, eCourts (official) | Court-data aggregation + workflow | Benchmark for the Litigation module |
| Indian legal AI / research | CaseMine (AMICUS AI), Bharat.law, Indian Kanoon Prism, SCC Online, Jhana | Research subscriptions; AI drafting and summaries | Vidhi AI benchmark; possible data partners |
| Trademark tools | IP India portals, IndiaFilings TM software, Corpbiz TM Watch, StartupGrantsIndia watch, Iolite watch software | Filing + status tracking + journal watch | Benchmark for the IP/TM module |
| Government lockers | DigiLocker, Entity Locker | Issued documents, consent sharing | UX model for the LawDocs Vault; integration targets |

---

## 3. LegalKart — deep dive and reverse engineering

### 3.1 Profile

| Attribute | Finding | Source |
|---|---|---|
| Legal entity | Black Coat Technologies Pvt Ltd (developer on App Store) | App Store |
| Founded / HQ | 2018, Gurugram | About page; YourStory 2022 |
| Leadership | Dr Arvind Singhatiya (Founder & CEO), Partha Sen (Co-founder & CTO) | About page |
| Funding | Seed ~₹3.5 Cr (Oct 2019); ₹4 Cr pre-Series A (Jan 2022, Mumbai Angels et al.); ₹6.5 Cr (Nov 2024: IIM Udaipur IC, Aevitas, ShiftAlt) | YourStory; Entrackr |
| Scale claims | "5M+ users" (About); "50,000+ clients", "1,000+ verified advocates", "Trusted by over Million Users" (home); "10K+ lawyers" (talk page); "500+ verified expert lawyers" (ask page); 3,500 lawyers in 300 cities (iOS listing) | Own pages — internally inconsistent |
| Positioning | "Preventive Legal Care Ecosystem"; describes itself as an AI-powered technology platform, "not a law firm", "does not solicit" | About; footer |
| Segments | B2C (individuals); lawyers (practice-management app and lead portal); B2B (court-data API; "compliance and legal services"; 2025 international expansion, Dubai firm tie-up) | About; Open Magazine (sponsored, Dec 2024) |
| Languages | Site switcher: EN, HI, BN, TA, TE, ML, GU, MR, PA (9). Talk page says "8 languages including Kannada" (Kannada missing from switcher) | Home; talk page |
| Support | 24×7 phone, WhatsApp, email | Footer |
| Growth claim | "453% jump in business topline" over 8 months (2024) — no absolute revenue disclosed | Entrackr |

### 3.2 Reverse-engineered sitemap

```
legalkart.com
├── /{lang}/  (en, hi, bn, ta, te, ml, gu, mr, pa)   ← language-prefixed paths
│   ├── (home)  hero: Chat with a lawyer | Talk now; popular services; 3-step chat explainer;
│   │           advocate preview cards (₹/min); buy chat credits; testimonials; media; FAQ
│   ├── /talk-to-lawyer           problem-area tiles → buy LegalKart Cash → choose expert → call/video
│   ├── (chat with a lawyer)      credit packs (₹299 = 10 min), any advocate, written advice  [marked "New"]
│   ├── /ask-a-lawyer             "Describe your issue" (20–500 chars, Write with AI, voice, pincode)
│   │                              + public enquiry list (status: Answered / Pending / Resolved)
│   ├── /products                 Consult a Lawyer | AI Document Review (<60 s) | Lawyer Document Review
│   ├── /property                 verification, documentation, registration, Property Report
│   ├── /startup                  formation, contracts, licences, compliance, IP (no prices)
│   ├── /lawyer-in-cities         36 States/UTs → /lawyer-in-cities/{state-slug} (~231 cities)
│   ├── /find-{practice}-lawyer-in-{city}   programmatic SEO pages (e.g., trademark-&-copyright … kakinada)
│   ├── /legal-blog               Trending | Latest → /legal-blog/{slug}; author "LegalKart Editor"
│   ├── /about  /advisors  /careers  /contact-us
│   └── /privacy-policy  /terms-of-use  /legalkart-cash-terms-of-use
├── services.legalkart.com       Court-data API (CNR, case status, orders, cause lists; SC/HC/DC; prepaid wallet)
├── lawyers.legalkart.com/login  Lawyer Management Portal (noindex)
├── challanwala.com              Traffic challan check/pay, RC details, vehicle reports, court challans via lawyers
└── Apps: "LegalKart" (client) and "Legalkart-Lawyer" (iOS/Android)
```

### 3.3 User flows

**F1 — Chat consult (core B2C funnel)**
1. The landing page shows advocate preview cards: name, practice area, ₹/min, rating, experience, chat count.
2. The user buys chat credits. 1 credit = ₹1; packs start at ₹299 for 10 minutes; bigger top-ups get bonus credits; UPI, cards and net banking are accepted.
3. Credits can be used with any advocate.
4. Chat is billed per minute. The lowest advertised rate is ₹22/min.
5. Written advice stays in the chat.

Hooks: ₹199 free credits for new app users; the page describes the service as "India's first" chat with a lawyer, private and anonymous.

**F2 — Talk now / video**
1. The user picks a problem tile: cheque bounce, starting a business, online blackmail, insurance claim, family, child custody, buying property.
2. The user buys LegalKart Cash.
3. The user chooses an expert. Cards show rating with review count, years of experience, languages, ₹/min "call charges", and call and video icons.
4. The call runs over an internet call or a dial-in number. The caller's number is hidden from the lawyer (2020 press release).
5. The page lists no filters (practice, language, price or rating).
6. The hero says "from ₹31/min", but the cheapest featured lawyer is ₹42/min.
7. Historical pricing: Talk Now launched in May 2020 at ₹499 for 15 minutes, discounted to ₹99. A 15-minute minimum applied in 2022.

**F3 — Ask a lawyer (lead capture and SEO)**
1. The user describes the issue in 20–500 characters, can use "Write with AI" or a voice recording, and must enter a pincode.
2. The question becomes a public enquiry card with city, category and status.
3. The Terms of Use say free questions and answers "become LegalKart's property" and go into a public database.
4. The page shows "2 mins" average response time and "12 lawyers active now".
5. The page does not say whether asking is free. [VERIFY]

**F4 — Instant AI document review**
1. The user uploads a document.
2. The AI flags risks, red flags and missing clauses in "under 60 seconds".
3. No price is shown. [VERIFY by test purchase]

**F5 — Lawyer document review (expert review)**
1. The user enters details, uploads a PDF and picks talk time; the system counts the pages.
2. The user schedules a call.
3. A senior property or corporate lawyer sends a written report and a follow-up call.
4. Pricing per the G2 vendor description: from **₹100 per page**, feedback in a minimum of 3 hours, 12 languages.

**F6 — Property**
1. The user fills details (an existing mobile number auto-fills them) and uploads documents.
2. The user schedules an expert call.
3. The user receives a Property Report (title chain, encumbrances, liens, taxes, leases) plus drafting, registration and stamp-paper support.
4. Updates come by WhatsApp and SMS.
5. 2022 price band: ₹2,999–9,999.

**F7 — Startup**
1. The user chooses a product and pays.
2. The user fills details on the success page and uploads documents.
3. Updates come by SMS and WhatsApp.
4. The product is delivered.
5. Buying two products gets an unquantified discount. 2022 price band: ₹1,999–25,000. No FAQs on the page.

**F8 — Challan (ChallanWala)**
1. The user searches by vehicle number, driving licence or challan number.
2. Challans are listed.
3. The user pays with a convenience fee (amount not stated).
4. The site says it facilitates court challans "through its network of lawyers".
5. The page describes no contest or virtual-court workflow.

**F9 — Lawyer side**
- Practice-management app: cases, clients, teams, finances, calendar sync, voice notes, case updates to clients, collaboration network.
- Lead allocation: lawyers are notified when a case is allocated, can call customers in-app, send payment links, raise invoices at case close, and view earnings, withdrawals and pending amounts.
- iOS in-app purchases list "Lite ₹5,900 / Plus ₹17,900 / Prime ₹24,900"; whether these recur is not stated. [VERIFY]
- The iOS lawyer app is rated 3.7 from 20 ratings. One 2023 reviewer paid a monthly subscription and got no cases.

**F10 — B2B court-data API (services.legalkart.com)**
1. Register and verify email.
2. Make a prepaid wallet recharge; a one-time setup fee applies.
3. Create and rotate API keys.
4. Call 27+ typed endpoints (CNR search, case status, orders, cause lists, registry lookups; SC / 10+ HCs / DCs).
5. Pay per successful call; failed provider calls are not billed; no monthly subscription. The page claims 99.9% uptime.

### 3.4 Business model (reconstructed)

| Revenue stream | Mechanism | Evidence |
|---|---|---|
| Consultation wallet | Prepaid closed-loop credits; per-minute burn; non-refundable; credits expire after 30–180 days per the Terms | Home; LKC Terms |
| Service commission | 15–45% take rate on consult and service fees | YourStory 2022 |
| Fixed-fee products | Property, startup and documentation (2022 bands ₹999–35,000) | YourStory 2022 |
| AI and expert document review | AI review (price not shown); expert review from ₹100/page | Products page; G2 |
| Lawyer-side monetisation | Empanelment fee ₹1,499–4,999/yr (2022) → iOS in-app tiers ₹5,900–24,900 | YourStory; App Store |
| API | Setup fee + pay-per-successful-call wallet | services.legalkart.com |
| Adjacent vertical | ChallanWala convenience fees | challanwala.com |
| Breakage (inferred) | Expired or forfeited credits, non-refundable top-ups | LKC Terms [inference] |

**Unit-economics reading (inference):** the per-minute meter plus a prepaid wallet with short expiry maximises cash collected up front and breakage. The lawyer subscription monetises supply whether or not demand reaches each lawyer. Both are efficient for the platform, and both are behind the visible complaints.

### 3.5 Trust, safety and terms — what LegalKart actually commits to

- **Verification:** marketing says "Bar Council registered" and "verified". The Terms say LegalKart "does not separately verify" qualifications and users should do their own due diligence.
- **Liability:** capped at the amount paid to LegalKart. Claims about a lawyer's advice must go to the lawyer.
- **Refunds:**
  - Wallet top-ups: "No refunds on LegalKart Cash purchases".
  - Booked appointments: cancellation by email 24 hours ahead, with a 10% processing deduction.
- **Negative balance:** a failed payment creates a negative balance that is carried to the next transaction.
- **Privacy:** user details are hidden and shared with the lawyer only after a paid booking. The Terms include consent to cross-border transfer.
- **Anti-leakage:** lawyers may not exchange contact details outside the platform.
- **Housekeeping:** the Terms say "Last updated: January 1, 2019" and have cross-reference errors. The client iOS app says it collects no data, which is implausible for a consult app.

### 3.6 SEO structure

- **URLs:** language-prefixed (`/en/`, `/gu/` …). `og:locale` is en_IN with pa_IN as alternate. No hreflang cluster was confirmed. [VERIFY]
- **Programmatic pages:** `/{lang}/find-{practice}-lawyer-in-{city}`. The H1 is generic ("Online Legal Consultation Anytime, Anywhere"), the H2 is dynamic, and the listed lawyers do not match the practice in the URL.
- **Meta and markup:** robots index/follow, max-image-preview large, OG and Twitter cards. **No JSON-LD seen** on blog, directory or SEO pages.
- **Blog:** `/en/legal-blog/{slug}`; topical posts (BNSS s.144 maintenance, e-Khata, 12-year rule, Vakalatnama); every post credited to "LegalKart Editor"; lead form embedded in every post.
- **Quality gaps:** unanswered FAQs, counters showing 0, repeated testimonials, unexplained "₹199 FREE" in the header, stats that disagree across pages.

### 3.7 What to copy, what to avoid

| Copy (adapt) | Avoid |
|---|---|
| Issue-first entry tiles in plain language ("Cheque bounced?") | A public, ranked, per-minute directory of advocates (Rule 36 risk) |
| Voice-note intake in local languages; "Write with AI" | Non-refundable wallets with short, inconsistent expiry |
| Masked phone numbers / anonymity | Claiming "verified" without verifying |
| AI review in under 60 s → paid expert review funnel | Charging professionals for leads without delivery assurance |
| WhatsApp/SMS milestone updates | Thin programmatic pages, empty FAQs, zero counters |
| Pay-per-call API wallet for B2B data | Stale Terms (2019) and data-collection declarations that don't match the app |
| Adjacent consumer verticals (challans, property reports) | Unpriced services ("contact us") |

### 3.8 Regulatory overlay for any LawDocs marketplace (must read)

- **Rule 36, BCI Rules (Part VI, Ch. II)** bars advocates from soliciting or advertising, directly or indirectly. The 2008 amendment lets an advocate's website show only name, qualifications, areas of practice and contact details.
- **Madras HC, P.N. Vignesh (W.P. 31281 & 31428 of 2019), 3 July 2024:**
  - Listing, rating, categorising and showing fees of advocates on Sulekha, Justdial and Quikr facilitates solicitation.
  - Those platforms cannot claim **s.79 IT Act** safe harbour.
  - The court cited **Rule 3(1)(d), IT Rules 2021**.
  - Platforms were ordered to remove such content within 4 weeks.
- **Supreme Court, Sulekha.com v. P.N. Vignesh (SLP (C) 25794/2024):** notice to BCI, tagged with SLP (C) 17844/2024. No stay was reported. [VERIFY current status]
- **BCI press release, 17 March 2025:** directs State Bar Councils to withdraw Rule 36-violating content and stop influencer promotion of legal services. It warns that platforms "actively facilitating" such content may lose safe harbour.
- **CA and CS professionals:** advertising is governed by ICAI and ICSI rules, which differ from BCI's. [VERIFY current ICAI/ICSI advertisement guidelines]
- **Design consequence for LawDocs:**
  - Sell **LawDocs services** with fixed scope and fixed price.
  - LawDocs assigns the professional.
  - Show Rule 36-permitted facts only on any advocate profile.
  - Do not show public star ratings or rankings for advocates. Rate the *service* instead.
  - Keep advocate fees out of the listing and price the SKU.
  - Keep per-profession feature flags, so CA/CS profiles can follow their own rules.
  - Get legal sign-off before launch. (LegalKart's own model carries this risk today.)

---

## 4. Indian services aggregators and directories

### 4.1 Profiles

| | **Vakilsearch** | **IndiaFilings** | **OnlineLegalIndia** | **LegalWiz** | **Corpbiz** | **LegalDesk** | **LawRato** |
|---|---|---|---|---|---|---|---|
| Segment | SMEs, startups, individuals | SMEs (compliance-heavy) | SMEs, NGOs | Startups, SMEs | SMEs, regulated sectors | Individuals (DIY docs) | Individuals (lawyer finding) |
| Catalogue structure | Consult an Expert / Business Setup / Tax & Compliance / Trademark & IP / Documentation / Others (e-FIR, consumer complaint, marriage) | Registration / GST / MCA / Income Tax / Trademark (incl. watch) / HR-payroll; LEDGERS platform | TM & copyright / Company registration / Company compliance / Licences / Tax / Payroll / Legal Dispute (ODR) / IT & Virtual CXO | Start / TM & IP / Manage / Tax & Filings / Legal Docs / Accounting | Startup / IP & TM (TM Watch) / Compliance / Regulatory (RBI, SEBI, IRDA, FEMA…) / Environmental | Property / Personal / Business documents (200+), stamp paper print & deliver | Directory by city / practice / court; free Q&A; law reference ("indian-kanoon" section); forms |
| Pricing seen | From ₹999 registration; ₹399 GST; ₹1,499 IP; ₹4,999 accounts; ₹999 licences | TM ₹1,899+GST (instant filing); ₹2,988+GST (search + filing); expedited TM ₹9,899+GST | None shown; "platform fee" | TM ₹1,999+; Pvt Ltd ₹2,999+; LLP ₹3,999+; proprietorship ₹1,999+; GST return ₹799+ | None shown | None shown | Quick Consult ₹399 / 15-min phone; "up to 30% off" first consult |
| Govt fee treatment | Not shown on home | "Government fee payable directly to Government" (excluded) | Not shown | "+ government fees" (not itemised) yet claims "price you see is the price you pay" | Not addressed | n/a (stamp duty implied) | n/a |
| Software / AI | "Product Suite" free trial: case alerts, hearings, 5M+ judgments, display board, compliance reminders | AI automation for GST, payroll, reminders, audit trails; APIs and webhooks; TM tracking software | "AI Solutions" listed, nothing specific | Progress tracker (% complete) | Search; TM Watch listed | Real-time document preview | Lawyer search, free Q&A |
| Distinctive UX | Book-a-callback on every category | Package cards with inclusions | Huge catalogue, ODR | Order status tracker | Regulatory-sector depth | Fill → preview → download or doorstep delivery | 150,000+ answered questions; NALSA pro-bono tie-up |
| Weaknesses seen | Voxya: 13 complaints, 3 resolved, "refund not received", "negligence / false commitments"; TM page still cites appeals to **IPAB**, abolished in 2021 (appeals now go to the High Court) | No prices on home; duplicated package descriptions | Says it is "not taking requests for legal consultancy"; placeholder modal text; rebranding notice; "Recognised by Govt" next to a "not affiliated" disclaimer | Govt fees not itemised | No prices; unverified "#1" claim | No prices; dated; no eSign or AI | Inconsistent lawyer counts (10,000 vs 15,000); Rule 36 exposure as a directory with ratings |

Other notes:
- A competitor-authored comparison (Tax Garden, Aug 2026) cites Vakilsearch Pvt Ltd registration at ₹7,000–15,000, trademark at ₹3,000–15,000 "all-in", and retainers at ₹25,000–1,00,000+/yr. Treat as [VERIFY].
- MyAdvo was not researched [VERIFY].
- For Kanoon-based tools, see §5 (Indian Kanoon Prism).

### 4.2 Pricing patterns observed (to design the LawDocs price card)

1. **"Starting at ₹X+"** headline professional fee (LegalWiz, Vakilsearch, IndiaFilings).
2. **"+ GST"** shown separately (IndiaFilings).
3. **Government fee excluded**, "paid directly to government" (IndiaFilings), or simply "+ govt fees" (LegalWiz).
4. **Tiered packages** set apart by add-ons such as search, class advice or Form 48 (IndiaFilings).
5. **Expedited tier** at roughly 5× base (IndiaFilings).
6. **Fixed time-block consults** (LawRato ₹399/15 min) versus **per-minute metering** (LegalKart).
7. **Membership bundles** (Rocket Lawyer, global): a quota of attorney questions and calls, unlimited documents, discounted add-ons.

**LawDocs recommendation:** one price card per SKU with four lines: **Professional fee**, **Government / statutory fee (estimate, with basis)**, **GST**, and **Total payable now**. Then show what is *not* included, the refund rule and the SLA. For trademarks, the government fee on TM-A e-filing is ₹4,500 per class for individuals, startups and small enterprises and ₹9,000 for others, under the Trade Marks Rules 2017 First Schedule. [VERIFY current schedule] The TM-O opposition fee is ₹2,700 e-filing (StartupGrantsIndia FAQ). [VERIFY]

---

## 5. Litigation, LegalOps and legal AI

### 5.1 Profiles

| | **Provakil** | **LegitQuest Patrol** | **eCourts (official)** | **Manupatra / SCC Online** | **CaseMine (AMICUS AI)** | **Bharat.law** | **Jhana** |
|---|---|---|---|---|---|---|---|
| Segment | Banks/NBFCs (collections), enterprise legal, law firms | Corporate legal | Citizens, advocates | Research subscribers | Lawyers | Lawyers, corporates | Courts, govt, lawyers |
| Offerings | Legal Collections (notice automation with India Post proof, SARFAESI/s.138/arbitration workflows); ELM (litigation, IPR, tasks, legal spend, MIS); AI CLM; Practice mgmt; Case mgmt | AI case tracking, dashboards, auto status sync (SC/HC/DC/tribunals, "10,000+ forums"), Suggestion Alert for new cases against client, documents, scoring | CNR search; search by case no., filing no., party, advocate, FIR, Act; My Cases diary; cause list; calendar; QR code per case; email updates; eFiling, ePay, virtual courts, NJDG | Research databases; Manupatra AI (research, case mgmt, compliance, contracts, IPR — per vendor comparison) | Conversational research, drafting, multi-document analysis (Advanced model, Mar 2026) | Court tracking "15,000+ courts", 10,000-page documents, citations traced (self-claim) | AI audit/review; property-title anomaly flags; claims 16,150+ lawyers and 650 judges |
| Pricing seen | Demo + ROI calculator | Demo | Free | SCC ~₹18,999/yr; Manupatra demo (per vendor comparison) | USD 499 / 1,499.99 per yr (per vendor comparison) [VERIFY] | Free start | Not published |
| AI features | Risk detection, summaries, obligation extraction, playbook redlines | Case scoring, risk analysis | None | Nascent (per vendor comparison) | Drafting, summarisation | Document interrogation | Review |
| Distinctive UX | 100+ multilingual notice templates; stage-based counsel billing; cloud or on-prem; SOC/ISO 27001 claims; GeM-listed | Portfolio-wide reporting | QR per case; personal case diary | Headnotes | AI inside research | Citation tracing | — |
| Weaknesses | Enterprise sales cycle; no public price | Limited public detail | No alerts push; no cross-court portfolio; court-complex selection friction | Expensive, research-centric | 100 MB upload cap; no court tracking (per vendor comparison) | Vendor-authored claims | Pivoting positioning |

Notes:
- Indian Kanoon Prism: AI summarisation, ₹15,000/yr + GST per the Bharat.law comparison [VERIFY].
- The Bharat.law comparison is vendor-authored and ranks itself first.

### 5.2 Design implications for the LawDocs Litigation module

- **Data source:**
  - Prefer a **licensed court-data API** (for example LegalKart's API, Provakil-type data partners, or Bharat.law) behind a provider abstraction.
  - Fall back to user-entered CNR and documents uploaded by the user.
  - Do not build a scraper that breaks on every portal change, and check the terms of the eCourts portal. [VERIFY]
- **Two personas:**
  - *Individual litigant:* plain-language status, what happens next, documents needed, nearest legal-aid option.
  - *Company:* portfolio, counsel, spend, contingent liability, board MIS.
- **Must-haves at parity:** add a case by CNR or by case no./party/advocate; My Cases; cause list; calendar; orders archive; QR/share link (all available in eCourts already).
- **Differentiators:**
  - New-case-filed-against-us alerts (Provakil, LegitQuest).
  - AI hearing brief.
  - Notice → litigation pipeline linked to Finbyx (recovery) and Equator (ODR/arbitration).

---

## 6. eSign, eStamp and CLM

### 6.1 Profiles

| | **Leegality** | **Digio** | **Melento (ex-SignDesk)** | **Zoho Sign (India)** | **DocuSign (India)** | **Setu eSign/eStamp** | **SpotDraft** |
|---|---|---|---|---|---|---|---|
| Segment | BFSI, enterprise | BFSI, fintech | BFSI, brokers, enterprise | SMB to enterprise | Global enterprise | Developers/fintech | Mid-market/enterprise legal |
| Signature types | 15+ methods incl. Aadhaar eSign, DSC; virtual sign, quick eSign, clickwrap (Tier 2) | Aadhaar eSign, USB DSC, document signer cert, electronic sign | eSign [details VERIFY — site blocked] | Aadhaar eSign (incl. eMudhra eKYC), USB token, certificate signing | Aadhaar eKYC-based and CA-issued digital signatures recognised (legality page) | Aadhaar eSign | ESIGN/eIDAS-style e-signature |
| eStamp | BharatStamp: 31 States/UTs, stamp serial number on each page | Multi-denomination eStamp via DigiDocs (not all states, per Melento) | 25+ States/UTs; direct SHCIL in 5; stamp-duty calculator; master wallet; second-party payment; automated pre-order | Through Melento (DL, GJ, KA, MH, RJ, TN) or eDrafter (wider); ₹48 / ₹24 processing fee; 1 credit = ₹6; RJ +30% surcharge; physical copy couriered quarterly | Notes several states amended stamp acts for e-records | 17 of 20 listed states; merge eStamp PDF at start or end of the signed document | — |
| Workflows / bulk | No-code dashboard workflows, templates, unlimited signers, Excel-driven scale | DigiStudio no-code journeys; DigiDocs templates, versioning, forms | Bulk stamping (Upstox case: 4,000+/month) | Bulk send, templates, signing order, branding | — | API flows, templates, signature positions | Conditional templates, approvals by deal value |
| Audit / fraud | Audit trail (name, email, timestamps, IP, eSign type, certificate, geo, face capture); eSign Verifier; AI face match; geofencing; auto-switch to best ESP; non-Aadhaar routing during UIDAI downtime | ISO 27001, SOC 2; RBI-authorised PA | Image capture, GPS, geofencing | AES-256, PKI, India data centres | — | — | — |
| Other | NeSL, eBG, Consentin (DPDP consent manager), licence-free basic plan for < ₹3 lakh/yr budgets | eNACH/UPI mandates; KYC (DigiLocker, OCR, CKYC/KRA, video KYC); CoTrust DPDP consent | CLM | Zoho CRM/Books/Teams integrations | — | — | VerifAI review in Word ("up to 15× faster"), negotiation in Word/Slack, repository, renewals, analytics |

### 6.2 Legal guardrails surfaced by this research (to bake into product logic)

- **IT Act Second Schedule:** lists the recognised eSign techniques (Aadhaar eKYC-based eSign; CA-issued digital signatures). These make a signature "reliable" under s.3A, and a party disputing one must prove it invalid.
- **IT Act First Schedule (via s.1(4)):** documents to which the Act does not apply, so an eSign is not effective. As summarised by Leegality and DocuSign: negotiable instruments other than cheques (Leegality notes carve-outs for RBI/NHB/SEBI/IRDAI/PFRDA-regulated entities); powers of attorney (Leegality notes a carve-out for POAs empowering regulated entities); trusts; wills and other testamentary dispositions; and contracts for sale or conveyance of immovable property (listed by DocuSign, not by Leegality). [VERIFY current First Schedule text and any 2024–25 MeitY amendments before coding the rule table]
  - **Product impact:** LawDocs' "Agreement to Sell (property)", "Gift Deed", "Will" and "General POA" templates need a **wet-sign / registration route**, not an eSign CTA.
- **Stamp duty:** state law decides it. Several states have amended their stamp acts for electronic records. Leegality lists stamp-paper hygiene rules: deface the physical paper, the first party's name on both versions, one paper per document, authorised vendors only.
- **Registration Act s.17:** leases above 11 months and most immovable-property instruments must be registered. An eSign does not replace Sub-Registrar registration. [VERIFY state e-registration schemes]

---

## 7. Trademark tools

### 7.1 Landscape

| Tool | What it does | Gaps |
|---|---|---|
| IP India eRegister (tmrsearch.ipindia.gov.in/estatus) | Status by application no. after OTP to any email/mobile; certificate copy marked "not for legal use" | No portfolio view, no alerts; Registry email goes only to the address for service |
| IP India Public Search | Wordmark / phonetic / Vienna code search | Phonetic search described as weak (Vakilsearch page) |
| Trade Marks Journal | Published every Monday; starts the 4-month opposition clock (s.21(1); not extendable under TM Rules 2017) | No similarity alerts |
| IP India e-filing | TM-A, replies, TM-O, TM-R renewals, TM-M | Professional UX; no guidance |
| IndiaFilings | TM packages with "TM tracking software" and monitoring | Software depth unknown [VERIFY] |
| Corpbiz | "TM Watch", "Trademark Monitoring" | No public detail [VERIFY] |
| StartupGrantsIndia | Weekly Journal watch, adjacent classes, phonetic/visual/transliteration filters, domains, social handles, marketplaces, Madrid; attorney review of each alert; annual subscription priced per scope | Service-led, not self-serve |
| Iolite TM Watch software | Journal scanning, similarity alerts, side-by-side reports | Vendor tool for attorneys; no pricing |
| Intepat (guide) | Says watch reports typically arrive 5–7 working days after each Monday Journal | — |

### 7.2 Status taxonomy and deadline engine for the LawDocs IP/TM module

These are the IP India status labels with the next action and deadline LawDocs should compute (per the Intepat guide; confirm against the Act and Rules).

| IP India status | LawDocs user label | Next action | Deadline rule |
|---|---|---|---|
| New Application | Filed | Check particulars | — |
| Send to Vienna Codification | Logo being classified | None | — |
| Formalities Chk Pass / Fail | Paperwork OK / defect | Cure defect | 1 month from notice (else abandoned) |
| Marked for Exam | Waiting for examiner | Collect evidence of use | — (12–14 months typical) |
| Exam Report Issued / Objected | Examiner objected | Draft reply (AI + professional) | 1 month from receipt |
| Ready for Show Cause Hearing | Hearing fixed | Prepare and attend | Hearing date |
| Accepted / Advertised bef Acc / Accepted and Advertised | Published in Journal | Monitor oppositions | 4 months from Journal date |
| Opposed | Someone opposed | Counter-statement | 2 months from receipt of notice copy |
| Registered | Registered ® | Download certificate; set renewal | 10 years from application date |
| Removed | Lapsed (non-renewal) | Renew with surcharge / restore | 6 months after expiry; restoration up to 1 year |
| Refused | Refused | Appeal to High Court or refile | 3 months from order |
| Abandoned / Withdrawn / Cancelled / Rectification Filed | Closed / challenged | Advice | As directed |

Indicative end-to-end time: 18–24 months uncontested, 3–5 years contested. Expedited examination (TM-M) takes about 3 months, but the opposition window still runs in full.

---

## 8. Global reference patterns

| Reference | Pattern | LawDocs adaptation |
|---|---|---|
| **Rocket Lawyer** | Annual plans $149 / $249 / $349 after a 7-day free trial. All plans include unlimited AI legal Q&A, unlimited contract reviews (key terms and red flags), unlimited documents and RocketSign e-signatures, and legal reminders. Plans differ by Ask-an-Attorney quota (12 / 36 / unlimited), live consult quota (0 / 12 / unlimited) and premium add-ons (4 / 7 / 10). One-off advice sessions cost $149 / 30 min. | LawDocs Individual and Business memberships with quotas of professional questions, calls and document reviews; one-off SKUs for non-members |
| **LegalZoom** | Guided self-service with optional attorney tier. Recurring services (registered agent, compliance coverage, virtual mail). Free tools as lead magnets (name search, Compliance Health Check, Estate Plan Check). "Full price before you begin". 100% accurate-filing guarantee. Clear "not a law firm / no privilege" disclosure. | Free tools hub; landed price card; filing guarantee; recurring Company Legal OS |
| **Clio** | Features grouped by job-to-be-done; client portal; intake/CRM (Grow); court docket tracking; trust accounting; AI drafting in Word; 300+ integrations; "New" badges | Professional workspace for empanelled professionals; client portal = the user's LawDocs app |
| **Ironclad** | Lifecycle Create → Review → Approve → Sign → Store → Fulfil → Analyse; AI agent; CRM-embedded contracting | CLM navigation and state machine; Salesforce/Zoho CRM connectors (P2) |
| **SpotDraft** | Review inside Word; negotiation in Word/Slack; approvals by deal value | Word add-in and approval matrix |
| **DigiLocker** | 4-step Register → Verify → Fetch → Share; issued (authentic) vs uploaded documents; 900+ crore issued documents; 70+ crore users (self-reported) | Vault home: "Issued" (from DigiLocker / LawDocs-executed, verifiable) vs "Uploaded" (self-attested) |
| **Entity Locker** (NeGD, Jan 2025) | 10 GB for businesses; MCA/GSTN/DGFT integration; consent page with revocation; nodal admin with authorisation letter adds Aadhaar-verified users; role-based access; audit of all document actions | Company Vault roles and consent sharing; integrate if APIs become available [VERIFY API] |

---

## 9. Feature-gap matrices

Legend: ● strong / shipped · ◐ partial / basic · ○ absent · ? not verified. The **LawDocs** column is the *target* defined by the owner brief, not current state.

### 9.1 Consumer and services competitors

| Capability | LawDocs (target) | LegalKart | Vakilsearch | IndiaFilings | LegalWiz | Corpbiz | OnlineLegalIndia | LegalDesk | LawRato | Rocket Lawyer |
|---|---|---|---|---|---|---|---|---|---|---|
| AI drafting from conversation | ● | ◐ | ? | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Questionnaire templates + live preview | ● | ◐ | ● | ◐ | ● | ◐ | ◐ | ● | ◐ | ● |
| AI document review | ● | ● | ? | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| Paid expert review | ● | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ◐ | ● |
| Aadhaar eSign in-flow | ● | ○ | ? | ○ | ○ | ○ | ○ | ○ | ○ | ◐ (non-Aadhaar) |
| eStamp purchase in-flow | ● | ◐ (stamp support) | ? | ○ | ○ | ○ | ○ | ◐ (print/deliver) | ○ | n/a |
| Counterparty negotiation / track changes | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ◐ |
| Personal legal vault (DigiLocker-like) | ● | ◐ ("store documents") | ◐ dashboard | ◐ | ◐ | ○ | ○ | ○ | ○ | ◐ |
| Consult: chat / call / video | ● | ● | ● (callback) | ◐ | ◐ | ◐ | ○ ("not taking") | ○ | ● | ● |
| Rule 36-safe marketplace design | ● | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | n/a | ○ | n/a |
| Litigation tracking (individual) | ● | ○ (API only) | ◐ (product suite) | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| TM filing | ● | ◐ | ● | ● | ● | ● | ● | ○ | ○ | ● |
| TM portfolio + deadline engine + watch | ● | ○ | ◐ | ◐ | ○ | ◐ | ○ | ○ | ○ | ◐ |
| Company compliance calendar | ● (via LawDocsComply) | ○ | ● | ● | ◐ | ◐ | ◐ | ○ | ○ | ◐ |
| Retainer / membership plans | ● | ○ | ? | ? | ○ | ○ | ○ | ○ | ○ | ● |
| Transparent landed price | ● | ◐ | ◐ | ◐ | ◐ | ○ | ○ | ○ | ◐ | ● |
| Consumer grievance (bank/insurer/e-com) | ● | ◐ | ● (consumer complaint) | ○ | ○ | ○ | ● (ODR) | ○ | ◐ | ○ |
| Challan check / pay / contest | ● | ● (ChallanWala) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | n/a |
| Multilingual UI (9+ Indian languages) | ● | ● | ◐ (content) | ○ | ○ | ○ | ○ | ○ | ◐ | n/a |
| Voice intake | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Native apps | ● | ● | ? | ? | ○ | ○ | ○ | ○ | ? | ● |
| Structured data / FAQ schema | ● | ○ (none seen) | ? | ? | ? | ? | ? | ? | ? | ? |
| Public API for partners | ● | ● (court data) | ○ | ● (APIs/webhooks) | ○ | ○ | ○ | ○ | ○ | ○ |

### 9.2 LegalOps and eSign competitors

| Capability | LawDocs (target) | Provakil | LegitQuest | Leegality | Digio | Melento | Zoho Sign | SpotDraft | Ironclad |
|---|---|---|---|---|---|---|---|---|---|
| Templates + clause library | ● | ● | ○ | ◐ | ◐ | ? | ◐ | ● | ● |
| AI review + playbook redlines | ● | ● | ○ | ○ | ○ | ? | ○ | ● | ● |
| Approval matrix (maker-checker) | ● | ● | ○ | ◐ | ◐ | ? | ◐ | ● | ● |
| Negotiation room (track changes + chat) | ● | ◐ (Word) | ○ | ◐ (Deal Collaboration) | ○ | ? | ○ | ● | ● |
| Obligation / renewal tracking | ● | ● | ○ | ○ | ○ | ? | ○ | ◐ (renewals) | ? |
| Aadhaar eSign + DSC + fallback routing | ● | ◐ (integrations) | ○ | ● | ● | ● | ● | ○ | ○ |
| Multi-state eStamp + duty calculator | ● | ● (e-stamping) | ○ | ● (no calculator) | ◐ | ● | ◐ (via vendors) | ○ | ○ |
| Signer fraud controls (face / geo) | ● | ? | ○ | ● | ● | ● | ○ | ○ | ○ |
| Audit trail certificate | ● | ? | ○ | ● | ● | ● | ● | ● | ● |
| Bulk send / bulk stamp | ● | ● (notices) | ○ | ● | ● | ● | ● | ◐ | ◐ |
| Court tracking (multi-forum) | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| New-case-against-entity alerts | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| Counsel / spend management | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| IP portfolio management | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Legal notices with proof of delivery | ● | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| DPDP consent manager | ◐ (integrate) | ? | ○ | ● (Consentin) | ● (CoTrust) | ? | ○ | ○ | ○ |
| SMB self-serve pricing | ● | ○ | ○ | ◐ (licence-free basic) | ○ | ○ | ● | ○ | ○ |
| Individuals as first-class users | ● | ○ | ○ | ○ | ○ | ○ | ◐ | ○ | ○ |

**Reading the matrices:**
- LawDocs' defensible position is the **union**: an individual-grade vault and consult experience (LegalKart / DigiLocker) on top of enterprise-grade eSign/eStamp (Leegality / Melento) and LegalOps (Provakil), at SMB self-serve prices.
- Do not try to beat Leegality on eSign infrastructure. Integrate two ESP and eStamp vendors and win on UX and the legal-workflow wrapper.

---

## 10. Improvement backlog

Priority: **P0** = MVP / launch-blocking · **P1** = phase 2 · **P2** = later. "Source" names the competitor or reference that informed the item.

| ID | Module | Improvement | Source / rationale | Pri |
|---|---|---|---|---|
| IMP-001 | Marketplace | Sell fixed-scope, fixed-price **service SKUs** ("Consult 30 min – Property", "Legal notice – cheque bounce"), not a per-advocate per-minute directory | Rule 36 / P.N. Vignesh; LawRato assigns a lawyer after payment | P0 |
| IMP-002 | Marketplace | Rule 36-safe advocate profile schema (name, qualifications, enrolment no., areas, languages); no public advocate ratings or rankings; feature flags per profession (Advocate / CA / CS) | BCI Rule 36 (2008 amendment); BCI 17 Mar 2025 | P0 |
| IMP-003 | Marketplace | Assignment engine (area × language × state × load × SLA history) with "request a different professional" | LawRato quick consult; avoids directory ranking | P0 |
| IMP-004 | Marketplace | Real verification at empanelment: Bar Council enrolment, COP/ID, ICAI/ICSI membership, PAN, bank; yearly re-verification; badge only after checks | LegalKart Terms admit no separate verification | P0 |
| IMP-005 | Marketplace | Consult modes: async chat with response SLA, scheduled audio/video, instant call; masked numbers both ways | LegalKart chat/talk; 2020 anonymity feature | P0 |
| IMP-006 | Billing | Block pricing (15 / 30 / 60 min) shown before payment; overrun only with explicit in-call consent; no hidden meter | LegalKart per-minute; LawRato ₹399/15 min | P0 |
| IMP-007 | Vidhi AI | Consult summary and action list generated from the transcript with consent, approved by the professional, filed to the Vault | Gap at all competitors | P1 |
| IMP-008 | Marketplace | 48-hour free follow-up chat after each consult | Complaint: lawyer stops responding | P1 |
| IMP-009 | Marketplace | Refund engine: auto-refund on professional no-show or dropped call; partial refunds; grievance officer SLA displayed | App review "LK balance zero"; Consumer Protection (E-Commerce) Rules 2020 [VERIFY clauses] | P0 |
| IMP-010 | Mobile | Professional app: request inbox, calendar, deliverables, earnings, payouts, auto invoice, TDS (s.194J) and GST capture | LegalKart lawyer app; Clio | P1 |
| IMP-011 | Billing | Professional monetisation by commission per delivered SKU; optional practice-tools subscription **without lead promises** | Review: "paid subscription, no cases" | P1 |
| IMP-012 | Marketplace | QA layer: sample peer review, client delivery confirmation, SLA breach auto-escalation to ops hub | Vakilsearch "false commitments" complaints | P1 |
| IMP-013 | Marketplace | Off-platform leakage detection (phone/email patterns in chat) with friendly warnings | LegalKart Terms anti-leakage clause | P2 |
| IMP-014 | Consumer Help | Issue-first tiles (cheque bounce, online fraud/blackmail, loan-recovery harassment, insurance rejection, employer dues, property purchase, custody) → triage → DIY / notice / consult / complaint | LegalKart talk page tiles | P0 |
| IMP-015 | Vidhi AI | Voice-note intake in 10+ Indian languages with transcription, translation and an editable summary | LegalKart 30-second voice note | P0 |
| IMP-016 | Vidhi AI | "Help me describe my problem" writing assistant with prompts for missing facts (dates, amounts, parties) | LegalKart "Write with AI" | P1 |
| IMP-017 | Consumer Help | Challan check & pay with the convenience fee shown; court/virtual-court challans → assign an advocate SKU | ChallanWala | P1 |
| IMP-018 | Consumer Help | Consumer-complaint builder for the national e-filing portal, with a pecuniary-jurisdiction calculator | Vakilsearch "File a consumer complaint" [VERIFY e-Jagriti/e-Daakhil current] | P1 |
| IMP-019 | Consumer Help | Grievance tracker for RBI CMS / Integrated Ombudsman, IRDAI Bima Bharosa, NCH, with escalation timers | Owner brief (FREED / Insurance Samadhan type) [VERIFY timelines] | P1 |
| IMP-020 | Litigation | Legal-notice SKU with multilingual templates and proof of delivery (India Post tracking, email, WhatsApp) | Provakil notice automation | P0 |
| IMP-021 | Website/SEO | Every document/service page embeds a "Draft free with Vidhi" widget, with an upsell to professional review | Owner brief; LegalKart AI review → expert review funnel | P0 |
| IMP-022 | Drafting | Live document preview updating as the questionnaire is answered | LegalDesk | P0 |
| IMP-023 | eSign/eStamp | State × instrument **stamp-duty calculator** built into drafting and checkout | Melento has it; Leegality lacks it | P0 |
| IMP-024 | Drafting | **eSign-eligibility checker**: blocks the eSign CTA for First Schedule instruments (will, POA, trust, immovable-property sale) and routes to wet-sign/registration | IT Act s.1(4) First Schedule; DocuSign/Leegality summaries | P0 |
| IMP-025 | Drafting | Registration-required flag (Registration Act s.17; leases > 11 months) with Sub-Registrar checklist | Legal guardrail | P1 |
| IMP-026 | eSign/eStamp | Physical stamp paper print-and-deliver for uncovered states | LegalDesk | P2 |
| IMP-027 | Drafting | Bilingual execution copy (English + regional), side by side, with a governing-language clause | LegalKart vernacular positioning | P1 |
| IMP-028 | Drafting | Conditional templates with clause variants, fallbacks and explanations ("i" button) | SpotDraft conditional templates | P1 |
| IMP-029 | Vidhi AI | Instant AI review (risks, missing clauses, red flags, plain-language summary) in < 60 s; free quota then paid | LegalKart AI review; Rocket Lawyer unlimited reviews | P0 |
| IMP-030 | Marketplace | Expert review SKU priced per page band, with written report + follow-up call; turnaround SLA | LegalKart (₹100/page, ≥ 3 h) | P0 |
| IMP-031 | Vidhi AI | Legal Q&A grounded in bare acts (BNS/BNSS/BSA updated), with section-level citations and an "ask a professional" escalation | Rocket Lawyer AI Q&A; LegalZoom disclosure | P0 |
| IMP-032 | CLM | Company playbooks → automatic redlines and fallback positions | Provakil, SpotDraft | P1 |
| IMP-033 | Vidhi AI | Citation verifier: every cited section or judgment resolved against the corpus; unresolved ones flagged; never fabricate | Indian AI tools' citation-reliability concerns (vendor comparison) | P0 |
| IMP-034 | Pleadings | OCR of handwritten notes and WhatsApp screenshots → typed copy + translation, editable, attached as annexure | Owner brief; gap at all competitors | P1 |
| IMP-035 | Vidhi AI | Agent jobs: chase signatures, watch hearings, draft TM replies, renewal reminders, weekly legal digest to the CLO/board | Ironclad agent; owner brief | P1 |
| IMP-036 | CLM | Business-user intake forms (request NDA / vendor contract) with auto-template selection | Ironclad launch forms | P1 |
| IMP-037 | CLM | Approval matrix by contract type, value and department, with maker-checker and delegation | SpotDraft routing by value | P0 |
| IMP-038 | CLM | Negotiation room: track changes, comments, version compare, counterparty chat, all logged to the audit trail | Owner brief; SpotDraft/Leegality Deal Collaboration | P0 |
| IMP-039 | CLM | Obligation, renewal and expiry extraction → calendar and owners | Provakil AI | P1 |
| IMP-040 | CLM | MS Word add-in and Google Docs add-on for review and redlines | SpotDraft VerifAI; Provakil Word | P2 |
| IMP-041 | Vault/DMS | Bulk import of legacy contracts through the folder structure, with AI metadata extraction | Owner brief; Ironclad repository | P1 |
| IMP-042 | CLM | Contract analytics: TAT, bottleneck step, renewals due, value at risk | Provakil TAT; SpotDraft analytics | P2 |
| IMP-043 | eSign/eStamp | Multi-ESP routing with auto-failover and non-Aadhaar fallback (DSC / DocSigner) | Leegality | P0 |
| IMP-044 | eSign/eStamp | Optional signer controls: face match, geofence, ID check, OTP to registered mobile | Leegality, Melento | P1 |
| IMP-045 | eSign/eStamp | Audit-trail certificate appended to the signed PDF (names, mobiles, timestamps, IP, method, certificate, geo) | Leegality audit trail | P0 |
| IMP-046 | eSign/eStamp | eStamp vendor abstraction (SHCIL / Melento / eDrafter / Setu) with coverage map and expected processing time per state | Zoho Sign vendor table; Setu | P0 |
| IMP-047 | eSign/eStamp | Split or second-party stamp-duty payment and "who pays" clause sync | Melento second-party payment | P1 |
| IMP-048 | eSign/eStamp | Bulk send from Excel/CSV (offer letters, NDAs, DSA agreements) | Zoho, Leegality | P1 |
| IMP-049 | eSign/eStamp | Signing order, reminders, expiry, decline-with-reason, reassign signer | Zoho Sign workflows | P0 |
| IMP-050 | eSign/eStamp | Stamp certificate number printed on every page | Leegality BharatStamp | P1 |
| IMP-051 | Billing | Business credits wallet for eSign/eStamp with per-unit price list and no expiry on paid credits | Zoho credits (1 credit = ₹6); contrast LegalKart | P1 |
| IMP-052 | Vault/DMS | Public verification page / QR for any LawDocs-executed document (hash check) | eCourts case QR; DigiLocker verification | P1 |
| IMP-053 | Vault/DMS | "Issued" vs "Uploaded" document classes; pull issued documents from DigiLocker | DigiLocker model | P0 |
| IMP-054 | Vault/DMS | Consent-based, time-bound, revocable sharing with an access log the owner can see | Entity Locker consent page | P0 |
| IMP-055 | Company Legal OS | Company vault roles: nodal admin (authorisation letter), Aadhaar-verified members, department scopes | Entity Locker | P1 |
| IMP-056 | Vault/DMS | Nominee / legal-heir access with verification and waiting period | DigiLocker-type expectation [VERIFY DigiLocker nominee feature] | P2 |
| IMP-057 | Vault/DMS | Life-event smart folders (Property, Vehicle, Family, Work, Litigation, Tax, Business) with auto-filing | DigiLocker 8 categories; owner brief | P1 |
| IMP-058 | Vault/DMS | One-click export in human-readable folders + manifest CSV + PDF/A copies | Owner brief (data preservation) | P0 |
| IMP-059 | Vault/DMS | Expiry and renewal reminders on any document (lease end, insurance, licences, TM) | LegalZoom reminders; Rocket Lawyer legal reminders | P1 |
| IMP-060 | Litigation | Add a case by CNR / case no. / party / advocate / FIR; auto-sync status, next date and orders | eCourts app parity | P0 |
| IMP-061 | Litigation | New-case-filed-against-entity alerts by party-name variants | Provakil; LegitQuest Suggestion Alert | P1 |
| IMP-062 | Litigation | Personalised daily cause list across all tracked courts, with push at 7 am | Provakil daily causelists | P1 |
| IMP-063 | Litigation | External counsel management: stage-based fee schedules, invoices, performance, spend | Provakil legal spend | P1 |
| IMP-064 | Company Legal OS | Contingent-liability register and board MIS pack generated quarterly | Provakil MIS | P1 |
| IMP-065 | Vidhi AI | Hearing brief before each date: last order, pending compliance, documents, questions for counsel | Gap; CaseMine summarisation | P1 |
| IMP-066 | Litigation | Bulk case import (Excel template) with dedupe on CNR | Enterprise onboarding need | P0 |
| IMP-067 | Litigation | Lender recovery pipeline (demand notice → s.138 / SARFAESI / arbitration) with hand-offs to Finbyx and Equator | Provakil Legal Collections | P1 |
| IMP-068 | Litigation | Individual-litigant explainer: "what this status means", "what happens next", legal-aid link | eCourts lacks explanation; owner brief | P0 |
| IMP-069 | Litigation | Court-data provider abstraction (licensed API first, user-entered fallback); no fragile scraping | LegalKart API; Bharat.law | P0 |
| IMP-070 | IP/TM | TM portfolio tracker mapped to the full IP India status taxonomy (§7.2) | Intepat status guide | P0 |
| IMP-071 | IP/TM | Deadline engine: exam reply 1 month, opposition 4 months, counter-statement 2 months, renewal 10 years, removal/restoration windows; rule table editable without code | TM Act s.21, s.25; Rules 2017 | P0 |
| IMP-072 | IP/TM | Weekly Journal watch with phonetic, visual, conceptual and transliteration similarity, adjacent classes, professional review queue | StartupGrantsIndia; Iolite | P1 |
| IMP-073 | IP/TM | AI Nice-class finder from a business description | IndiaFilings "Class Finder" | P0 |
| IMP-074 | IP/TM | Pre-filing knock-out search with a conflict score and an explanation | Vakilsearch notes weak phonetic search | P1 |
| IMP-075 | Business Services | TM price card that shows the government fee by applicant type separately | IndiaFilings/LegalWiz opacity [VERIFY fee schedule] | P0 |
| IMP-076 | IP/TM | Digital brand watch: domains, marketplaces (Amazon/Flipkart/Meesho), social handles | StartupGrantsIndia; Intepat | P2 |
| IMP-077 | Website/SEO | Legal-content QA: no obsolete forums or laws (IPAB → HC; IPC → BNS); "law as of" date on every page | Vakilsearch IPAB reference | P0 |
| IMP-078 | Business Services | Catalogue organised by life stage: Start / Run / Protect / Resolve / Exit (individuals: Home / Family / Money / Work / Vehicle) | Clio job-to-be-done grouping | P0 |
| IMP-079 | Billing | Landed price card (professional fee + govt fee + GST = total), exclusions, refund rule, SLA | LegalZoom "full price before you begin" | P0 |
| IMP-080 | Business Services | Order tracker with milestones and % complete, plus WhatsApp/SMS/email updates | LegalWiz tracker; LegalKart alerts | P0 |
| IMP-081 | Company Legal OS | Compliance calendar auto-built from the entity profile (CIN/GSTIN), linked to LawDocsComply for regulated entities | Vakilsearch / IndiaFilings LEDGERS | P1 |
| IMP-082 | Billing | Memberships for individuals, startups and SMEs with quotas (questions, calls, reviews, notices) and add-on discounts | Rocket Lawyer plans | P0 |
| IMP-083 | Business Services | "Accurate filing guarantee": rework free if LawDocs erred | LegalZoom | P2 |
| IMP-084 | Business Services | Startup Desk bundles (incorporation + founders' agreement + ESOP + TM + website policies) with a quantified bundle discount | LegalKart startup page (unquantified discount) | P1 |
| IMP-085 | Billing | Wallet policy: paid balance refundable on request (or never expiring), bonus credits labelled separately, one expiry rule stated identically everywhere; no dark patterns | LegalKart inconsistency; CCPA Dark Patterns Guidelines 2023 [VERIFY] | P0 |
| IMP-086 | Billing | 7-day free trial on memberships; first AI review free | Rocket Lawyer trial | P1 |
| IMP-087 | Billing | Professional payouts with auto TDS, GST invoices (self-billing where allowed) and payout statements | LegalKart lawyer earnings view | P1 |
| IMP-088 | Billing | Developer API wallet (pay per successful call, failed calls free) for partner apps | services.legalkart.com | P2 |
| IMP-089 | Website/SEO | Programmatic pages (service × city × language) only where real content matches; JSON-LD for Service, FAQPage, BreadcrumbList, HowTo, Organization | LegalKart mismatch and no schema | P0 |
| IMP-090 | Website/SEO | FAQ answers rendered server-side in HTML, with questions mined from search and Q&A data | LegalKart empty FAQs | P0 |
| IMP-091 | Website/SEO | Server-rendered stats from a claims register; never show 0 or placeholder text | LegalKart zero counters; OnlineLegalIndia placeholder modal | P0 |
| IMP-092 | Website/SEO | Single claims register for all public numbers (users, professionals, documents), reviewed monthly | LegalKart 500 / 1,000 / 3,500 / 10K inconsistency | P0 |
| IMP-093 | Website/SEO | Language-prefixed URLs with a full hreflang cluster and translated, not machine-only, pillar pages | LegalKart `/hi/`, `/gu/` pattern | P1 |
| IMP-094 | Website/SEO | Public Q&A library only with explicit opt-in, PII redaction, professional review; no advocate promotion inside answers | LawRato 150k answers; LegalKart Terms; Rule 36 | P1 |
| IMP-095 | Website/SEO | Free tools hub: stamp-duty, TM class finder, limitation period, notice period/gratuity, rent-agreement cost, eSign eligibility | LegalZoom free tools | P1 |
| IMP-096 | Website/SEO | Named, credentialed reviewer + "reviewed on" date on every guide (E-E-A-T) instead of a generic editor byline | LegalKart "LegalKart Editor" | P1 |
| IMP-097 | Mobile | App: biometric lock, offline Vault cache (encrypted), push for hearings, deadlines and sign requests | eCourts My Cases; DigiLocker app | P0 |
| IMP-098 | Mobile | In-app VoIP consult with automatic PSTN fallback and masked numbers | LegalKart internet call + dial-in | P1 |
| IMP-099 | Mobile | Accurate app-store privacy labels and data-safety forms; payments flow reviewed against store rules for real-world services | LegalKart "no data collected" claim [VERIFY store rules] | P1 |
| IMP-100 | Mobile | WhatsApp Business channel (opt-in) for status, document delivery and payment links | LegalKart / ChallanWala WhatsApp updates | P1 |
| IMP-101 | Pleadings | Court-specific pleading templates with format rules (paper, margins, font, line spacing) per HC/DC rules | Gap at consumer players [VERIFY per-court rules] | P1 |
| IMP-102 | Pleadings | Annexure builder: auto index, pagination, typed copies, translations, true-copy endorsement, PDF bundling | Owner brief; Provakil digital case workspace | P1 |
| IMP-103 | Pleadings | Vakalatnama and memo-of-appearance generator; e-filing-ready PDF/A output | LegalKart blog topic demand; eCourts eFiling | P2 |
| IMP-104 | Company Legal OS | IP/TM, litigation, contracts and notices rolled into one "Legal risk dashboard" for KMPs and the board | Provakil ELM + MIS | P1 |
| IMP-105 | Consumer Help | Property-purchase pack: title search request, encumbrance check, draft agreement, stamp-duty estimate, registration checklist | LegalKart Property Report | P1 |

---

## 11. Strategic recommendations

1. **Lead with "keep" rather than "consult".** LegalKart users arrive for one consult and leave. LawDocs should make the Vault, Litigation tracker, TM tracker and reminders the reason to keep the app, with consults as paid add-ons. That is the DigiLocker behaviour the owner wants.
2. **Turn compliance into a selling point.**
   - Publicly commit to: verified professionals, a Rule 36-safe marketplace, a refundable or non-expiring paid balance, a landed price card, SLA refunds and a named grievance officer.
   - Each of these answers a visible competitor complaint.
3. **Integrate rather than build infrastructure.**
   - eSign: two ESPs.
   - eStamp: two or more vendors.
   - Court data: one or two licensed providers.
   - KYC: DigiLocker/CKYC.
   - Spend the effort on workflow, AI and UX.
4. **Use AI review as the conversion engine.**
   - Free AI review → paid expert review → membership. LegalKart already proves the first two steps.
   - Rocket Lawyer proves the membership step.
5. **Make SEO a quality moat.**
   - Fewer, better pages: real content, matching listings, answered FAQs, schema, named reviewers, "law as of" dates.
   - Make these pages the citation source for AI and generative search.
6. **Price B2B separately from B2C.**
   - Companies: seat-plus-usage SaaS (eSign/eStamp credits, case-tracking slots, TM marks under watch).
   - Individuals: memberships and one-off SKUs.
   - Professionals: commission plus optional tools subscription.

---

## 12. Sources (all accessed 25 October 2026)

**LegalKart and related**
1. LegalKart home — https://www.legalkart.com/ (→ /en)
2. Talk to a lawyer — https://www.legalkart.com/en/talk-to-lawyer
3. Property — https://www.legalkart.com/en/property
4. Startup — https://www.legalkart.com/en/startup
5. Ask a lawyer — https://www.legalkart.com/en/ask-a-lawyer
6. City directory — https://www.legalkart.com/en/lawyer-in-cities
7. Programmatic SEO page — https://www.legalkart.com/en/find-trademark-%26-copyright-lawyer-in-kakinada
8. Products — https://legalkart.com/products
9. Blog — https://www.legalkart.com/en/legal-blog
10. About — https://www.legalkart.com/en/about
11. Advisors — https://www.legalkart.com/en/advisors
12. Terms of use — https://www.legalkart.com/en/terms-of-use
13. LegalKart Cash terms — https://www.legalkart.com/en/legalkart-cash-terms-of-use
14. API services — https://services.legalkart.com/
15. Lawyer portal — https://lawyers.legalkart.com/login
16. ChallanWala — https://www.challanwala.com
17. App Store, LegalKart (client) — https://apps.apple.com/us/app/-/id1588394544
18. App Store, Legalkart-Lawyer — https://apps.apple.com/in/app/legalkart-lawyer/id1470835386
19. G2 listing — https://www.g2.com/products/legalkart/discuss
20. YourStory (15 Jun 2022) — https://yourstory.com/2022/06/gurugram-based-legalkart-aims-democratise-legal-access-legaltech/amp
21. Entrackr (14 Nov 2024) — https://entrackr.com/snippets/legaltech-startup-legalkart-raises-rs-65-cr-in-fresh-round-7580531
22. Open Magazine (sponsored, Dec 2024) — https://openthemagazine.com/open-avenues/legalkart
23. StartupTalky profile — https://startuptalky.com/legalkart-success-story/
24. Asia Law Portal interview (Nov 2019) — https://asialawportal.com/indias-mobile-app-for-lawyers-an-interview-with-dr-arvin-singhatiya-ceo-legalkart/
25. The Tech Outlook (May 2020, Talk Now) — https://www.thetechoutlook.com/new-release/software-apps/instant-legal-consultation-on-legalkarts-24x7-talk-now-technology/

**Services aggregators and directories**
26. Vakilsearch home — https://vakilsearch.com/
27. Vakilsearch trademark registration — https://vakilsearch.com/trademark-registration
28. Voxya, Vakilsearch complaints — https://voxya.com/company/vakilsearch.com-complaints/17336
29. Tax Garden vs Vakilsearch (competitor-authored) — https://taxgarden.in/blog/taxgarden-vs-vakilsearch-compliance-registration-comparison-2026
30. OnlineLegalIndia home — https://www.onlinelegalindia.com/ (TM page: fetch failed)
31. IndiaFilings home — https://www.indiafilings.com/
32. IndiaFilings TM pricing — https://www.indiafilings.com/trademark-registration/pricing
33. IndiaFilings expedited TM pricing — https://www.indiafilings.com/expedited-trademark-registration/pricing
34. LegalWiz — https://www.legalwiz.in/
35. Corpbiz — https://corpbiz.io/
36. LegalDesk — https://www.legaldesk.com/
37. LawRato — https://lawrato.com/
38. LawRato Quick Consult — https://lawrato.com/quickconsult

**Litigation, LegalOps, legal AI**
39. Provakil — https://www.provakil.com/
40. LegitQuest Patrol corporate — https://www.legitquest.com/patrol-corporate
41. LegitQuest court case status — https://www.legitquest.com/product/litigation-management-system/court-case-status
42. eCourts Services Mobile App manual (Orissa HC) — https://orissahighcourt.nic.in/ecourts-mobile-app/eCourts_Services_Mobile_App_English.pdf
43. Vikaspedia, citizen-centric judiciary services (metadata only) — https://en.vikaspedia.in/viewcontent/e-governance/online-legal-services/citizen-centric-online-services-in-indian-judiciary?lgn=en
44. Bharat.law, best AI legal research tools 2026 (vendor-authored) — https://bharat.law/resources/best-ai-legal-research-tools-india-2026
45. Bar & Bench, CaseMine AMICUS AI Advanced (sponsored, 10 Mar 2026) — https://www.barandbench.com/news/casemine-launches-amicus-ai-advanced-its-most-powerful-ai-model-for-legal-work
46. Jhana — https://jhana.ai/

**eSign, eStamp, CLM**
47. Leegality eSign — https://leegality.com/esign
48. Leegality eSign & eStamp FAQs — https://www.leegality.com/blog/esign-estamp-faqs
49. Digio — https://www.digio.in/
50. Melento (ex-SignDesk) eStamp comparison (vendor-authored) — https://melento.ai/en-in/alternatives/signdesk-estamp-vs-competitors (redirected from signdesk.com; signdesk.com/in/ blocked by robots)
51. Zoho Sign India — https://www.zoho.com/en-in/sign
52. Zoho Sign e-stamping help — https://help.zoho.com/portal/en/kb/zoho-sign/integrations/e-stamping/articles/e-stamping-in-zoho-sign
53. DocuSign India legality — https://www.docusign.com/products/electronic-signature/legality/india
54. Setu eStamp docs — https://docs.setu.co/data/esign/estamp
55. SpotDraft — https://www.spotdraft.com/
56. Ironclad — https://ironcladapp.com/

**Trademark**
57. Intepat, trademark application status — https://intepat.com/blog/trademark-application-status-india
58. Intepat, trademark watch guide — https://www.intepat.com/blog/trademark-watch-in-india-guide
59. StartupGrantsIndia trademark watch — https://www.startupgrantsindia.com/services/trademark-watch-monitoring
60. Iolite TM watch tool — https://iolitesoftwares.com/trademark-watch-tool.html

**Global and government references**
61. Rocket Lawyer pricing — https://www.rocketlawyer.com/pricing
62. LegalZoom — https://www.legalzoom.com/
63. Clio features — https://www.clio.com/features/
64. DigiLocker — https://www.digilocker.gov.in/
65. MediaNama, Entity Locker explainer (22 Jan 2025) — https://www.medianama.com/2025/01/223-explainer-what-is-entity-locker-difference-digi-locker/

**Regulatory (marketplace)**
66. MediaNama, Madras HC on platforms advertising legal services (6 Jul 2024) — https://www.medianama.com/2024/07/223-no-safe-harbor-for-platforms-advertising-legal-service-madras-hc/
67. Verdictum, SC notice in Sulekha v. P.N. Vignesh (13 Nov 2024) — https://www.verdictum.in/court-updates/supreme-court/sulekhacom-new-media-private-limited-v-pn-vignesh-ors-special-leave-to-appeal-c-nos-257942024-1557830
68. Gala Law blog, BCI crackdown (17 Mar 2025 release) — https://blog.galalaw.com/post/102k6nx/bar-council-of-india-cracks-down-on-legal-advertising-and-influencer-culture
69. Bar & Bench column on Rule 36 (3 Jun 2025, opinion) — https://www.barandbench.com/columns/lawyers-not-vendors-why-rule-36-still-matters-in-a-digital-india

**Open [VERIFY] items carried forward**
- MyAdvo and Nyay/NyayGPT-type tools (not researched).
- Current Supreme Court status of the Rule 36 SLP.
- Current IT Act First Schedule text.
- TM-A / TM-O fee schedule.
- e-Jagriti consumer-portal status.
- ICAI/ICSI advertising rules.
- Google Play ratings for LegalKart.
- LegalKart AI-review price.
- Whether LegalKart's lawyer in-app tiers recur.
- Corpbiz TM Watch scope.
- Entity Locker API availability.
