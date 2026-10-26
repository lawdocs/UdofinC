# R6 — Pricing, Revenue Streams and Data Sources for Integrations

**LawDocs (lawdocs.in) Build Prompt Pack · Research stream R6 · 25 October 2026 · Owner of commercial values: the project owner. Every price below is an indicative seed (`[OWNER TO SET]`) until the owner approves the first catalogue version.**

---

## R6.0 Purpose, method and how to read this file

1. **What this file does.** It gives evidence for (a) the LawDocs pricing page and catalogue (three public plans, Enterprise, add-ons, credit packs, meters, one-time products, retainers, marketplace fees, academy, API/white-label and other streams), (b) a revenue-stream registry with default switches and legal-review flags, and (c) a catalogue of data sources and integration routes for onboarding, litigation, trademark, company, tax, eSign, eStamp, workplace, CRM, messaging, video and payments.
2. **Method.** Live web sources were read through WebSearch and WebFetch on 25 October 2026. Nothing was fetched with curl or scripts. Several vendor pricing pages render prices client-side or hide them behind "contact sales" (Zoho Sign, SignDesk/Melento, Digio, Cashfree, SpotDraft, Probe42 INR). For those, the best available secondary figure is shown and labelled. **The shared web-search budget for this session ran out near the end of the work.** As a result, the items below were not re-checked live and are marked **[VERIFY]**: Jio as a WhatsApp BSP, YouTube privacy-enhanced embed behaviour, Microsoft Graph and Google Drive permission names (carried from sister pack LDC Appendix L §L.5.5), Legitquest/CaseMine/Manupatra/Kleop API terms, CKYC access rules, ICAI/ICSI fee-sharing clause text, and consumer-help success-fee benchmarks.
3. **Status tags.** **VERIFIED** means a live page read today supports the statement, with the source cited in §R6.9. **[VERIFY]** means the statement comes from prior research, the sister packs or secondary sources and needs confirmation before build or go-live. **[LEGAL]** means counsel must sign off before the stream or feature is switched on. **[TAX MEMO]** means the CFO and tax adviser must sign a tax memo before go-live.
4. **Conventions.** Prices are in INR, exclusive of GST, unless stated otherwise. USD figures are converted at an assumed ₹88/USD for orientation only. That rate is not a quote, and billing never uses daily FX.
5. **Relationship to sister packs.** The format follows LawDocsComply (LDC) Appendix N (packages, components, meters, registry) and Equator (EQ) Appendix AB (stream registry with governance view, deny-list). Their findings were re-checked rather than copied. The professional-conduct deny-list in EQ AB.3.3 (no referral rewards to advocates, no paid badges, no share of advocates' fees) is **re-confirmed** below and applies to LawDocs with greater force, because LawDocs lists advocates directly.

---

## R6.1 Competitive and price benchmarks (Part A)

### R6.1.1 Consumer legal consultation and legal memberships

| # | Provider / product | Model | Observed price (INR unless stated) | Notes for LawDocs | Source (accessed 25 Oct 2026) | Status |
|---|---|---|---|---|---|---|
| B-01 | LegalKart — Talk to a Lawyer (audio/video) | Per-minute, prepaid wallet ("LegalKart Cash") | "From ₹31/min". Named-advocate rates are ₹42–₹69/min (consumer ₹42, property ₹45, family ₹49, criminal ₹59, corporate ₹69) | The main competitor prices **per advocate per minute**. Named advocates set their own rates on a ranked list. "110+ experts online", "10K+ lawyers", 8 consultation languages | legalkart.com/en/talk-to-lawyer | VERIFIED |
| B-02 | LegalKart — Chat with a Lawyer | Per-minute chat credits | "From ₹22/min". Starter pack ₹299 for 10 minutes; "1 credit = ₹1". Named rates ₹22–₹55/min. Credits valid 1 year. New-user offer: ₹199 free credits in app | Wallet plus first-use incentive. Bigger top-ups earn bonus credits (amounts not shown) | legalkart.com | VERIFIED |
| B-03 | LegalKart — lawyer-side fees | Not disclosed | No published lawyer subscription or commission | The disclaimer says it "is not a law firm". The lawyer app was launched separately (press). LegalKart's revenue share with advocates is undisclosed, so LawDocs must not copy any per-minute fee split with advocates (see §R6.1.7) | legalkart.com; businessworld.in | VERIFIED (absence) |
| B-04 | Rocket Lawyer membership (US) | Annual membership | Standard $149/yr ($12.41/mo), Plus $249/yr, Pro $349/yr. 7-day trial. Legal Advice Session $149/30 min, $249/60 min. Add-ons: trademark from $350, EIN $70 | Unlimited documents, eSign and AI Q&A in **every** tier. Attorney access scales by tier (12/36/unlimited written questions; live consults on Plus/Pro). This is the model for the LawDocs Personal and Pro allowances | rocketlawyer.com/membership | VERIFIED |
| B-05 | LegalZoom (US) | Attorney plans plus formation packages | Personal attorney plan $199/yr. Business attorney plan $469/yr (unlimited 30-min consults). LLC packages $0 / $249 / $299 + state fee. The $249 package bundles an attorney subscription that renews at $49/mo after 30 days. Registered agent $249/yr | The auto-renewing bundled subscription is a dark-pattern risk under the CCPA Dark Patterns Guidelines 2023 (subscription trap, basket sneaking). LawDocs must not copy it | ailawyer.pro comparison (prices as of 6 Jun 2026) | VERIFIED (secondary) |

**Reading.** Indian consumers expect **pay-per-use with a small wallet top-up** (₹199–₹299 entry). US players have moved to **annual memberships** that include document, eSign and AI usage, with human advice rationed by tier. LawDocs should combine the two: a free vault, a low-priced annual membership that includes eSign and AI allowances, and **flat-fee professional consultations at fixed durations** (not per-minute ranked advocates; see §R6.1.7).

### R6.1.2 Registrations, filings and compliance services (one-time and subscription)

| # | Provider | Service | Observed price | Inclusions / exclusions | Source | Status |
|---|---|---|---|---|---|---|
| B-06 | IndiaFilings | Private limited company incorporation | ₹2,899 + GST | Unlimited name attempts, MoA/AoA, 3 DINs. **Government fees and DSC extra** | indiafilings.com/company-registration/pricing | VERIFIED |
| B-07 | IndiaFilings | Incorporation + compliance (annual) | ₹19,899 + GST | Adds compliance and accounting support | same | VERIFIED |
| B-08 | IndiaFilings | GST registration + monthly filing / GST return filing / GST consultation | ₹1,499 / ₹998 / ₹1,988 + GST | GSTR-1 and 3B. LEDGERS software bundled | indiafilings.com/gst-registration/pricing | VERIFIED |
| B-09 | IndiaFilings | Partnership firm (deed) / + GST / + GST & ITR | ₹2,899 / ₹10,899 / ₹14,899 + GST | Govt fee, stamp paper and notary extra | indiafilings.com/partnership/pricing | VERIFIED |
| B-10 | LegalWiz.in | Private limited company registration | "Starting at ₹2,999 + Govt fees" | DSC, name, MoA/AoA, DIN, SPICe+, PAN/TAN. Govt fee and stamp duty at actuals | legalwiz.in/private-limited-company-registration | VERIFIED |
| B-11 | Vakilsearch (now "Zolvit") | Trademark registration | "Starts from ₹1,499" | Search, filing, PoA, class advice, tracking, objection support. Govt fee treatment not stated | vakilsearch.com/online-trademark-registration | VERIFIED |
| B-12 | RestTheCase | Private limited (Standard) | ₹15,999 (struck ₹20,000); also "from ₹999 professional fee" | Inconsistent page. Shows the wide range in the market | restthecase.com | VERIFIED |
| B-13 | IP India (official) | Trademark TM-A e-filing fee per class | ₹4,500 (individual, sole proprietor, MSME, DPIIT startup); ₹9,000 (others). Renewal ₹9,000/class | Govt fee is pass-through (pure agent) on LawDocs invoices | disytax.com (14 May 2026) citing Trade Marks Rules 2017; renewal per vakilsearch.com | VERIFIED (secondary) |
| B-14 | ITR filing market | Self-file / CA-assisted | JioFinance ₹24 / ₹999; Tax2Win ₹49 / ₹1,274–₹7,968; TaxBuddy ₹699 / ₹2,999; ClearTax ₹2,540 basic, ₹25,000 "Luxe" | Jio has pushed self-file prices close to zero. LawDocs should compete on CA-assisted and notice-handling work, not self-file | businesstoday.in (22 Aug 2025) | VERIFIED (secondary; dated) |
| B-15 | Practice/firm market rate for TM filing professional fee | — | ₹1,500–₹10,000 per application (initial filing ₹2,000–₹10,000) | Generic range | disytax.com | VERIFIED (secondary) |

**Reading.** Professional fees for commodity filings have settled at **₹1,499–₹2,999 + GST + government fees**. Annual compliance bundles sit at **₹15,000–₹20,000** for small companies. LawDocs should price commodity filings at market and win on (i) a free AI-drafted first version, (ii) documents stored in the vault for life, and (iii) bundling filings into the Pro/Business plans as allowances.

### R6.1.3 eSign, eStamp and agreement-execution platforms

| # | Provider | Unit / plan | Observed price | Notes | Source | Status |
|---|---|---|---|---|---|---|
| B-16 | Leegality — Basic plan (budgets < ₹3 lakh/yr) | Aadhaar eSign | **₹25 per signatory** | Pay only for successful eSigns. Minimum 100 credits | leegality.com/pricing | VERIFIED |
| B-17 | Leegality — Basic | Non-Aadhaar (electronic) eSign | **₹15 per signatory** | — | same | VERIFIED |
| B-18 | Leegality — Basic | Digital stamping (BharatStamp) | **₹45 per stamp paper + stamp duty + ₹500 per stamp order**. Minimum 30 stamp papers | 29–31 States/UTs (page inconsistent). No duty charged if signer does not sign | same; leegality.com/blog/estamping | VERIFIED |
| B-19 | Leegality — Premium / Scale / Enterprise | Custom | Quote only. A competitor page cites ₹25,000–₹50,000/month for Leegality enterprise | Add-ons: NeSL DDE, automated doc signer, payment collect | leegality.com/pricing; cashfree.com/aadhaar-esign | VERIFIED (custom) / secondary |
| B-20 | Digio | eSign / eStamp | Not published ("on request"; pricing page checked 17 Oct 2026 by a third party). Estimates: **₹8–20 per sign** (₹15–20 under 1,000/month); eStamp facilitation **₹30–50/document** + duty; full loan journey ₹80–150 | Wholesale-to-retail gap explains margin room | productgrowth.in/tools/kyc-identity/digio | VERIFIED (secondary estimate) |
| B-21 | SignDesk → **Melento** (rebrand; signdesk.com/pricing redirects to melento.ai) | Plans Individual (free: 3 docs/month, 30-day storage), SMB (Aadhaar), Corporate (DSC, audit trail), Enterprise (API, PAN-India stamping, SSO) | No INR prices rendered | Aadhaar packs sold on top of plans | melento.ai/en-in/pricing | VERIFIED (no prices) |
| B-22 | Zoho Sign | Free / Standard / Professional / Enterprise / API | Prices not rendered. Free 5 docs/user/month; Standard 25; Professional/Enterprise unlimited. Yearly saves 20%. Aadhaar eSign via identity providers sold as credits in 500s. Enterprise gets 50 credits/user/month (cap 2,500/org) | Credits are a separate meter from seats. This is the model for LawDocs | zoho.com/sign/pricing.html | VERIFIED (no amounts) |
| B-23 | DocuSign | Personal $10/mo (5 envelopes), Standard $25/user/mo, Business Pro $40/user/mo (~₹880 / ₹2,200 / ₹3,520 at ₹88) | USD. Aadhaar eSign support stated; Aadhaar price not published | Seat-plus-envelope model, expensive for Indian SMEs | esign.ai (competitor blog, 9 Oct 2026) | VERIFIED (secondary) |
| B-24 | emSigner (eMudhra) Bharat eSign | Per envelope | ₹75 per envelope (Aadhaar). "Pay & Sign" single-transaction plan for India | Per-envelope pricing is friendly to consumers | hyperverge.co blog; docs.emsigner.com | VERIFIED (secondary) |
| B-25 | SignYu (SignSetu) | Pay-per-use Aadhaar eSign | **₹15 per signature**, no subscription | Price floor for consumer pay-per-use | producthunt.com/p/signsetu/signyu | VERIFIED |
| B-26 | Cashfree Aadhaar eSign | API | Contact sales. Built on eMudhra and NSDL (Protean) | No digital stamping | cashfree.com/aadhaar-esign | VERIFIED |

**Reading and unit economics.** Retail Aadhaar eSign sits between **₹15 and ₹25 per signatory**, with ₹75 per envelope at eMudhra retail. Wholesale ESP/aggregator cost is estimated at **₹8–20**. Electronic (OTP/email) signatures retail at ₹15. eStamp facilitation is **₹30–50 per stamp** plus an order fee and duty at actuals. LawDocs should sell **eSign credits at ₹19–₹29 retail** (cheaper in larger packs), include a small monthly allowance in every paid plan, and **pass stamp duty through at actuals** as pure agent with a visible facilitation fee.

### R6.1.4 Practice-management, litigation and CLM software (enterprise pricing signals)

| # | Provider | Observed price | Notes | Source | Status |
|---|---|---|---|---|---|
| B-27 | Provakil (India; litigation and legal ops) | From **₹500 per user per month** (Basic); free trial | Case and docket management. Enterprise priced on quote | capterra.com/p/209812/Provakil (updated 19 Oct 2026) | VERIFIED (directory) |
| B-28 | SpotDraft (India-origin CLM) | Custom, contract-based; not published | Rated "$$$" relative to HyperStart "$$" and Ironclad "$$$$". Implementation included in base | spendflo.com; hyperstart.com (competitor, 9 Jul 2026) | VERIFIED (no figures) |
| B-29 | Clio (global practice management) | EasyStart $49 / $39 annual; Essentials $89 / $79; Advanced $119 / $109; Complete $149 / $139 per user/month (~₹3,400–₹13,100) | AI drafting only in Complete | costbench.com (verified 29 Aug 2026) | VERIFIED (secondary) |

**Reading.** Indian litigation software starts around **₹500/user/month**. Global practice tools are 7–25× that. LawDocs's litigation and CLM modules for companies should be **priced per workspace by matter band**, not per seat, with seats generous (as the LDC ADD-LIT band ₹6,000 for ≤ 100 matters). That undercuts per-seat tools for legal teams of 3–10 people.

### R6.1.5 Payments: Razorpay fees, Subscriptions, Route, Smart Collect, and the PA Directions 2025

| # | Item | Observed | Source | Status |
|---|---|---|---|---|
| B-30 | Standard plan, domestic cards, netbanking, wallets, RuPay debit | 2% platform fee + 18% GST on the fee (2.36% all-in) | razorpay.com blog "pricing explained" (13 Feb 2026, updated 11 Oct 2026) | VERIFIED |
| B-31 | UPI | Listed at **2% platform fee** under the standard plan. Govt MDR on UPI is 0%. A ₹2,000 / 0.4% NPCI MDR proposal is "deferred". Credit card on UPI 2.15% | razorpay.com blog; softwaresuggest.com (updated 23 Oct 2026) | VERIFIED (conflicting; **[VERIFY]** negotiated UPI rate with Razorpay before launch) |
| B-32 | Amex, Diners, corporate cards, international cards | 3% (international chargeback protection +1%) | razorpay.com blog | VERIFIED |
| B-33 | International bank transfers / MoneySaver Export Account | 1% + GST, zero FX markup, free FIRA | razorpay.com blog; skydo.com | VERIFIED |
| B-34 | Subscriptions (recurring) | ~0.99% per transaction **on top of** the method fee | razorpay.com blog; softwaresuggest.com | VERIFIED |
| B-35 | Route (split settlements) | Two fees: (1) gateway fee on the full amount collected; (2) **transfer fee on each amount transferred** to a linked account, per the agreed plan + GST. Reversals possible (INR only). Transfers can wait for post-payment approval. Penny-test validation of linked accounts | Razorpay Route FAQs (axisbank-docs.razorpay.com) | VERIFIED (rates **[VERIFY]**) |
| B-36 | Smart Collect | Customer identifiers (NEFT/RTGS/IMPS) and VPA receivers. TPV supported. MCC must not be "Individuals". Pricing on a separate page | razorpay.com/docs/payments/smart-collect | VERIFIED (rate **[VERIFY]**) |
| B-37 | Setup / AMC | None on standard plan. A 0% platform-fee offer for new merchants from 1 Jul 2026 is reported | razorpay.com blog | VERIFIED (offer **[VERIFY]**) |
| B-38 | **RBI (Regulation of Payment Aggregators) Directions, 2025** | Issued **15 Sep 2025**, effective immediately. They consolidate the 2020/2021/2023 guidelines. **A PA cannot also run marketplace business; that must sit in a separate entity.** Marketplaces onboarded by PAs may "accept payments only for sellers registered on their platforms". PAs may credit funds only to the merchant's own accounts. Third-party payouts on merchant direction only for merchants with turnover > ₹40 lakh (export > ₹5 lakh). Escrow with an SCB is mandatory for non-bank PAs. Settlement timelines are agreed bilaterally (the T+1 suggestion was removed). Merchant KYC via CKYCR first | medianama.com (Sep 2025); Vinod Kothari highlights PDF | VERIFIED (secondary; **[VERIFY]** against the RBI text) |

**What the PA Directions mean for LawDocs.**
1. LawDocs is a **merchant and an e-commerce marketplace**. It is **not** a payment aggregator, and it must not hold professionals' money in its own current account and pay out manually. That pattern looks like unauthorised PA activity.
2. Use **Razorpay Route**: each empanelled professional (or their firm) is a **KYC'd linked account**. The buyer pays once, and Route splits the professional's fee to the linked account and LawDocs's own fee (platform or facilitation) to LawDocs. Use `on_hold` transfers until delivery acceptance or an SLA milestone, then release. Refunds go through reversals.
3. Professionals below ₹40 lakh turnover are fine as **linked accounts** (Route credits their own account). The ₹40 lakh threshold applies to *third-party payouts on a merchant's direction*, which LawDocs avoids by design. **[LEGAL]** Get a Razorpay confirmation letter that Route is enabled for a legal-services marketplace MCC.
4. Cash-on-delivery-style "pay the lawyer later outside the platform" flows are not tracked. Off-platform payment is the professional's own matter. LawDocs records only the engagement.

### R6.1.6 Tax rules that shape pricing and invoices

| # | Rule | Effect on LawDocs | Citation | Status |
|---|---|---|---|---|
| T-01 | **GST reverse charge on legal services by advocates to business entities** | When an **individual advocate (incl. senior advocate) or a firm of advocates** supplies legal services (advice, consultancy, assistance in any branch of law, representation) to a **business entity located in the taxable territory**, the **recipient pays 100% GST under RCM**. The advocate charges no GST to that client. LawDocs's invoice engine must issue (or show) the advocate's bill of supply / RCM-marked invoice, not add GST | Notification No. 13/2017-Central Tax (Rate), 28 Jun 2017, **Sl. No. 2**; s.9(3) CGST Act. SAC heading **9982** (998211–998216) | VERIFIED (notification and entry); sub-SAC mapping **[VERIFY]** |
| T-02 | Exemption for advocates' services to non-business persons and small businesses | Advocates' services to (a) another advocate or firm, (b) **any person other than a business entity** (individual consumers), or (c) a business entity with aggregate turnover up to the registration threshold in the preceding FY are **exempt** | Notification No. 12/2017-CT(R), **Entry 45** (as widely cited); GST Council decision 11 Jun 2017 | **[VERIFY]** entry number and current threshold wording |
| T-03 | Advocates' GST registration | Advocates whose supplies are wholly RCM/exempt are exempted from registration (s.23(2) CGST Act notification) | itatonline.org article on the GST Council decision | VERIFIED (secondary) |
| T-04 | LawDocs's own services (SaaS, drafting by LawDocs Pvt Ltd staff, facilitation, platform fees) | **Forward charge at 18%**. RCM does **not** apply because LawDocs is not an advocate or firm of advocates. Candidate SACs: 998314/998315/997331 for SaaS (per tax memo); 998214 (legal documentation) only if LawDocs itself supplies documentation; 998599 for facilitation; 998431 online information content at 18% (rate table shows 18% before and after 22 Sep 2025) | busy.in SAC 998431; CGST rate notifications | 18% VERIFIED for 998431; others **[TAX MEMO]** |
| T-05 | GST TCS by e-commerce operator | **0.5%** on net value of taxable supplies made through LawDocs by other suppliers, where LawDocs collects the consideration. Mandatory GST registration for the ECO. **Exclude** RCM supplies (advocates to businesses) and exempt supplies, because TCS applies to taxable supplies on which the supplier pays tax | Notification No. 15/2024-Central Tax (10 Jul 2024), s.52 CGST Act | Rate VERIFIED; RCM exclusion **[TAX MEMO]** |
| T-06 | Income-tax TDS on professional fees (old s.194J) | From **1 Apr 2026** under the Income-tax Act 2025: **s.393(1) Table Sl. 6(iii).D(b)** professional services / royalty **10%**; **Sl. 6(iii).D(a)** technical services **2%**; threshold **₹50,000**; 20% without PAN. Business buyers of LawDocs SaaS will deduct either 2% (technical) or 10% (royalty/professional) depending on characterisation. Publish LawDocs's position and TDS certificate workflow in Settings → Billing → Tax documents | tdsman.com (May 2026) | VERIFIED (secondary) |
| T-07 | Income-tax TDS by e-commerce operator (old s.194O) | **s.393(1) Table Sl. 8(v)**: **0.1%** of gross amount of services facilitated through the platform. No TDS where a resident individual/HUF participant's annual gross ≤ ₹5 lakh with PAN/Aadhaar. Effective 1 Apr 2026. Applies to professionals paid through Route | tdsman.com (Jul 2026) | VERIFIED (secondary) |
| T-08 | Stamp duty | Duty and government fees are **pure-agent reimbursements** (Rule 33 CGST Rules), shown as separate non-taxable lines. Facilitation fee is taxable at 18% | Rule 33 CGST Rules; EQ AB RS-45 | **[TAX MEMO]** |

### R6.1.7 Professional-conduct limits on monetising professionals

| # | Rule / development | Consequence for LawDocs | Source | Status |
|---|---|---|---|---|
| P-01 | **BCI Rules, Part VI, Chapter II, Rule 36**: "An advocate shall not solicit work or advertise, either directly or indirectly" | No paid listing, featured placement, ranking boost, "top lawyer" or "verified pro" badges for advocates. Directory pages show factual information only (name, enrolment, practice areas, languages, years), in the format allowed by Rule 36's proviso. No ratings-for-money | medianama.com (18 Mar 2025) summarising BCI notices | VERIFIED |
| P-02 | **Madras High Court (2024)**: Quikr, Sulekha, Just Dial and Grotal held to violate the Advocates Act 1961 and BCI Rules 36/37, and denied IT Act s.79 safe harbour. **BCI cease-and-desist notices (17 Mar 2025)** required removal within four weeks, with disciplinary action against advocates and contempt referrals | A marketplace that advertises advocates for a fee is exposed directly. LawDocs's advocate marketplace must be designed as a **consent-based professional directory plus engagement and payment workflow**, with fees charged to the **buyer** for LawDocs's own services | medianama.com; EQ AB deny X-18 (P.N. Vignesh, 3 Jul 2024) | VERIFIED |
| P-03 | BCI Rules Ch. II Rule 20 (no contingent or result-based fees) and Rule 2 Ch. III / Advocates Act s.45A themes (no fee-sharing with non-advocates) | **No percentage commission on advocates' fees. No success fee paid to or through advocates. No per-lead or pay-to-bid charges to advocates** (EQ deny X-17, X-22) | EQ AB.3.3; BCI Rules | Carried; **[VERIFY]** rule numbering against the BCI Rules text |
| P-04 | ICAI (CA Act 1949, First Schedule Part I, clauses on sharing fees, commission and brokerage with non-members, and on soliciting) and ICSI (CS Act 1980, First Schedule, parallel clauses); ICMAI 2025 referral-network bar (EQ [RE] F1.5) | CAs, CSs and CMAs may **not pay** LawDocs a share or commission of their professional fees. They may pay a **flat SaaS subscription** for tools, as any business does. Referral rewards to CAs/CSs/CMAs are prohibited | EQ AB deny X-21, X-22 | **[VERIFY]** clause text with ICAI/ICSI current Code of Ethics |
| P-05 | Advocates Act ss.29, 33; *Bar Council of India v. A.K. Balaji* (SC, 2018) | Only enrolled advocates may practise law, including non-litigious advice as the Court read "practice". **LawDocs Pvt Ltd itself must not give legal advice or appear.** "LawDocs legal team" retainers and advisory must be supplied by **advocates or a firm of advocates** contracted by or affiliated with LawDocs, who invoice the client (RCM for business clients). LawDocs supplies technology, drafting tools, coordination and non-advocacy compliance (CS/CA work through those professionals) | Statute; SC judgment | **[LEGAL]** structure memo required |

---

## R6.2 Recommended plan architecture (pricing page: three public plans plus Enterprise)

### R6.2.1 Principles (adapted from LDC N.1 and EQ AB, confirmed against the benchmarks)

1. **Free forever vault.** Individuals keep their documents for life on a free account. This is the "keep it like DigiLocker" requirement in the owner brief. Export is never paywalled (LDC PP-4).
2. **Software and services are separate.** Anyone can buy a service without a subscription (owner brief). Subscribers get included allowances and member prices.
3. **Credits for metered costs only.** Aadhaar eSign, eStamp facilitation, AI-heavy jobs (OCR of handwriting, translation, bulk extraction) and court-data refresh are metered because they carry unit costs. Reading, storing and sharing are not metered.
4. **No per-minute advocate billing, no ranked paid listings.** Consultations are sold as **fixed-duration, flat-price slots by practice area** (15/30/60 min). Price bands are set by the professional within LawDocs-published bands. The buyer sees the professional's fee and LawDocs's separate platform fee (§R6.3).
5. **Annual default with transparent monthly uplift.** Annual billing is default and monthly carries a **+20% uplift** (Zoho's published "save 20%" yearly norm). Cancellation is as easy as purchase, with no bundled auto-renewing extras (the LegalZoom pattern is denied).
6. **GST shown separately; pure-agent lines separate.** Duty, government fees and stamp duty are shown at actuals.

### R6.2.2 Plan table (indicative, INR, ex-GST) `[OWNER TO SET]`

| Attribute | **Free** (account) | **Personal** — individuals & families | **Pro** — professionals, freelancers & startups | **Business** — companies, LLPs, NBFCs | **Enterprise / Custom** |
|---|---|---|---|---|---|
| Pricing-page line | "Your legal documents, safe for life." | "Draft, sign and keep every agreement your family needs." | "Run your startup's or practice's legal work in one place." | "A legal department in a box, with maker-checker and audit trail." | "For banks, NBFCs, groups and platforms that need scale, APIs and a managed legal team." |
| Annual price | ₹0 | **₹1,499 / year** (≈ ₹125/mo) | **₹9,999 / year** per workspace (≈ ₹833/mo) | **₹59,999 / year** (≈ ₹4,999/mo) | from **₹3,00,000 / year** or quote |
| Monthly price (+20%) | ₹0 | ₹149 / month | ₹999 / month | ₹5,999 / month | quote |
| Family / seat model | 1 person | Up to **5 family members** (Family add-on ₹999/yr for 5 more) | 3 seats (extra seat ₹1,999/yr) | 10 working seats; unlimited free viewer/approver/board seats (LDC N.18) | Bands |
| Login | Mobile OTP / email; DigiLocker sign-in | + DigiLocker document pull | + Google/Microsoft SSO | + SSO (SAML/OIDC) add-on, SCIM | Included |
| Vault storage | 1 GB | 10 GB | 50 GB | 250 GB | 1 TB+; BYO storage |
| Vidhi AI credits / month | 30 (light Q&A, first draft) | 300 | 1,500 | 6,000 | 25,000+ |
| Free AI-drafted documents (template library) | Unlimited drafts; download PDF with watermark-free first 3/month | Unlimited | Unlimited | Unlimited | Unlimited |
| Aadhaar eSign credits included | 0 (buy per use ₹29) | **2 / month** (24/yr) | **10 / month** | **50 / month** | Contracted volume |
| Electronic (OTP) signatures | 5 / month | Unlimited fair use | Unlimited | Unlimited | Unlimited |
| eStamp facilitation | Per use | Per use, member price | 2 stamps/month included (duty extra) | 10 stamps/month included (duty extra) | Volume |
| Negotiation (track changes, comments, messaging between parties) | View-only | ✓ | ✓ | ✓ + approval workflows | ✓ |
| Litigation tracker (CNR, cause list alerts) | 1 case | 5 cases | 50 matters | 300 matters (band) | Unlimited by band |
| Trademark tracker / watch | 1 application | 3 applications | 10 marks + journal watch | 50 marks + watch | Unlimited |
| CLM (repository, obligations, renewals) | — | Renewal reminders | Basic CLM | Full CLM + obligation extraction | + custom |
| Professional consult allowance | — | 1 × 15-min consult / year | 2 × 30-min / year | 6 × 30-min / year + 10% member price on services | Retainer |
| Consumer help desk (grievance tracking for loans, insurance, challans) | Track own complaints | ✓ + templates | ✓ | — | — |
| Tax module | ITR document checklist | ITR self-prep checklist; CA-assisted at member price | GST/TDS calendar | GST/TDS/ROC calendars | Custom |
| Startup kit | — | — | Founders' agreement, ESOP, SHA, NDA packs; incorporation at member price | — | — |
| Company governance (board, minutes, registers, HRMS-lite) | — | — | Lite (1 entity) | Full (3 entities) | Groups |
| Data export (folder-structured ZIP, M365/Google Drive push) | ✓ | ✓ | ✓ | ✓ + scheduled export to SharePoint/Drive/S3 | ✓ + escrow option |
| Support | Help centre, Vidhi | Email/chat | Priority chat | Phone + onboarding manager 30 days | Named CSM, SLA |
| Trial | — | 14 days (cooling-off for individuals) | 14 days | 14 days or guided pilot | Pilot |

**Evidence anchors.** Personal at ₹1,499/yr is roughly one-eighth of Rocket Lawyer Standard ($149 ≈ ₹13,100) and roughly the price of 50 LegalKart chat minutes, which keeps it an easy yes. The included 24 eSigns at a ₹15–25 retail value are worth ₹360–₹600. Pro at ₹9,999/yr sits below one CA-assisted complex ITR plus one TM filing, and below one seat of Clio EasyStart ($39 × 12 ≈ ₹41,000). Business at ₹59,999/yr equals the bottom of the LDC Essentials band (from ₹10,000/month) divided by two, because LawDocs Business is a legal-ops tool, not a regulatory GRC suite. Business customers that are regulated entities are cross-referred to LawDocsComply under the group neutrality rule (LDC PP-8). Enterprise starts where Leegality enterprise contracts are reported (₹25,000–₹50,000/month).

### R6.2.3 Add-ons (per month, annual billing) `[OWNER TO SET]`

| Code | Add-on | Personal | Pro | Business | Ent. | Indicative price | Evidence / note |
|---|---|---|---|---|---|---|---|
| LD-ADD-FAM | Family extension (+5 members) | A | — | — | — | ₹999/yr | Family-vault positioning |
| LD-ADD-SEAT | Extra working seat | — | A | A | band | ₹1,999/yr (Pro); ₹4,999/yr (Business) | Provakil ₹500/user/mo benchmark (₹6,000/yr) |
| LD-ADD-LIT | Litigation pack (+100 matters, NCLT/DRT/consumer coverage, order OCR) | — | A | A | ✓ | ₹2,500/mo | Court-data pass-through via licensed aggregator (§R6.6) |
| LD-ADD-TMW | Trademark watch (+25 marks, weekly journal similarity) | — | A | A | ✓ | ₹1,500/mo | WIPO Brand DB route ~$0.05/record (§R6.6) |
| LD-ADD-CLM | Advanced CLM (obligation extraction, renewal desk, clause library) | — | A | ✓ | ✓ | ₹3,000/mo | SpotDraft "$$$" signal |
| LD-ADD-DMSX | Advanced DMS (handwriting OCR, WhatsApp/screenshot type copies, translation to English, bulk folder intake) | A | A | ✓ | ✓ | ₹499/mo (Personal); ₹2,000/mo (Pro/Business) + AI credits | Owner brief DMS requirement |
| LD-ADD-DR | Virtual data room (per room, 90 days, watermarking, Q&A, access log) | — | A | A | ✓ | ₹4,999 per room / 90 days; ₹1,999 per extra month | Fundraising, M&A, lender due diligence |
| LD-ADD-GOV | Board & secretarial pro (minutes SS-1/SS-2 checks, registers, MCA filing tracker) | — | A | A | ✓ | ₹2,500/mo | Use LDC ADD-BRD where the tenant is a regulated entity |
| LD-ADD-HR | HRMS-lite for client companies (people, KMP, departments, policies acknowledgement) | — | A | A | ✓ | ₹40 per employee/mo, min ₹1,500 | LDC ADD-HRMS ₹60/emp |
| LD-ADD-SSO | SSO + SCIM | — | — | A | ✓ | ₹1,500/mo | LDC ADD-SSO ₹2,000 |
| LD-ADD-API | API access tier (webhooks, sandbox, higher limits) | — | A | A | ✓ | ₹5,000/mo + per-call overage (§R6.2.6) | LDC ADD-API |
| LD-ADD-BYO | Bring-your-own storage / scheduled export (SharePoint, OneDrive, Google Drive, S3, SFTP) | — | — | A | ✓ | ₹2,000/mo | Owner data-preservation brief |
| LD-ADD-SUP | Premium support (phone, 4-hour response, named CSM) | — | A | A | ✓ | ₹5,000/mo | LDC ADD-SUPP ₹10,000 |
| LD-ADD-WL | White-label workspace (own domain, logo) for law/CA/CS firms managing clients | — | A | — | ✓ | ₹4,999/mo + ₹299 per client workspace | LDC practitioner plans from ₹15,000/mo |
| LD-ADD-AGT | Vidhi role agent seat (e.g., "Contract Clerk", "Litigation Clerk") with 400 credits | — | A | A | ✓ | ₹1,500/agent/mo | LDC ADD-AGT ₹2,000 |

### R6.2.4 Credit packs (one-time purchase, valid 12 months, no auto top-up by default)

| Pack | Units | Price | Effective unit price | Cost basis / evidence | Margin guard-rail |
|---|---|---|---|---|---|
| **Aadhaar eSign — single** | 1 | ₹29 | ₹29 | Leegality ₹25; SignYu ₹15; wholesale est. ₹8–20 | Unit cost ≤ 60% of price |
| Aadhaar eSign — 10 | 10 | ₹249 | ₹24.9 | — | — |
| Aadhaar eSign — 50 | 50 | ₹999 | ₹20.0 | — | — |
| Aadhaar eSign — 250 | 250 | ₹4,499 | ₹18.0 | — | — |
| Aadhaar eSign — 1,000 (Business) | 1,000 | ₹15,999 | ₹16.0 | Requires negotiated wholesale ≤ ₹10 | — |
| Electronic OTP/email signature (beyond fair use) | 100 | ₹499 | ₹5 | Leegality non-Aadhaar ₹15 | — |
| DSC signing (signer's own token) | — | ₹0 | — | No ESP cost | — |
| **eStamp facilitation** | per stamp | ₹49 + duty at actuals; no order fee under 10 stamps; ₹299 order fee for bulk series | — | Leegality ₹45 + ₹500/order; Digio est. ₹30–50 | Duty is pure agent |
| Physical stamp paper / franking courier | per order | ₹199 + duty + courier | — | State availability | — |
| **Vidhi AI credits — 500** | 500 | ₹499 | ₹1.00 | Claude API cost per credit to be measured; LDC prices ₹2.5/credit for B2B | AI cost ≤ 40% of credit price (LDC N.13) |
| Vidhi AI credits — 2,000 | 2,000 | ₹1,499 | ₹0.75 | — | — |
| Vidhi AI credits — 10,000 | 10,000 | ₹5,999 | ₹0.60 | — | — |
| Court-data refresh credits (beyond plan) | 100 refreshes | ₹299 | ₹2.99 | eCourtsIndia API PAYG 3× base; subscription base lower (§R6.6) | Pass-through + disclosed margin ≤ 20% |
| Certified-copy / order download service | per order | ₹99 + court fee at actuals | — | Official copy fees vary | — |

**Credit rates (seed, Vidhi):** standard chat turn 1; first draft from template 5; full bespoke contract draft 20; contract review with redlines 15 per 10 pages; handwriting/WhatsApp screenshot OCR + type copy 3 per page; translation to English 2 per page; litigation order summary 3 per order; obligation extraction 10 per contract (LDC N.17 parity). Deterministic features (reminders, search, calendar, CNR tracking) use 0 credits.

### R6.2.5 One-time products (catalogue seeds; professional fee ex-GST, government fees at actuals)

| Product | Indicative price | Market evidence | Delivered by |
|---|---|---|---|
| AI-drafted agreement (rent, sale, NDA, employment, vehicle sale, loan between individuals) | Free draft; ₹99 premium template export | LegalKart and others charge for drafting; free AI draft is the owner's hook | Vidhi (software) |
| Professional review of a self-drafted agreement | ₹499 (≤ 5 pages), ₹999 (≤ 15), ₹1,999 (≤ 40) | Market ₹500–₹2,000 | Empanelled advocate (consumer = exempt GST; business = RCM) |
| Bespoke drafting by professional | ₹1,999–₹9,999 by complexity | — | Advocate / CS |
| Legal notice drafting and dispatch | ₹1,499–₹2,999 (+ speed post at actuals) | — | Advocate only |
| Flat-fee consultation slots | 15 min ₹299–₹599; 30 min ₹599–₹1,499; 60 min ₹999–₹2,999 | LegalKart ₹31–₹69/min (= ₹465–₹1,035 for 15 min at upper rates) | Advocate / CA / CS |
| Private limited company incorporation | ₹2,999 + govt fees + DSC | IndiaFilings ₹2,899; LegalWiz ₹2,999 | CS / CA |
| LLP / partnership / proprietorship registration | ₹2,499–₹4,999 | IndiaFilings partnership ₹2,899 | CS / CA |
| Trademark search + filing (per class) | ₹1,999 + govt fee ₹4,500 / ₹9,000 | Vakilsearch ₹1,499; market ₹1,500–₹10,000 | TM agent / advocate |
| TM objection reply / opposition | ₹3,999 / ₹9,999+ | — | TM agent / advocate |
| GST registration / monthly return | ₹1,499 / ₹999 per month | IndiaFilings ₹1,499 / ₹998 | CA / GST practitioner |
| ITR — CA-assisted (salaried / capital gains / business) | ₹999 / ₹2,499 / ₹4,999 | JioFinance ₹999; TaxBuddy ₹2,999 | CA |
| Income-tax / GST notice reply | ₹2,999–₹14,999 | — | CA / advocate |
| Annual ROC compliance (small company) | ₹14,999/yr | IndiaFilings ₹19,899 bundle | CS |
| Policy drafting (HR, POSH, privacy, NBFC policies) | ₹4,999–₹49,999 per policy | — | LawDocs GRC professionals |
| Annual report / board report drafting | ₹24,999–₹1,49,999 | — | CS |
| Stress testing, scenario analysis, risk assessment, compliance testing | ₹50,000–₹5,00,000 per engagement | LDC Risk Lab ADD-RAL ₹12,000/mo as software alternative | GRC professionals (non-advocacy) |
| Challan contest (court-referred traffic challan) | ₹999–₹2,999 + court fine at actuals | ChallanPay/ChallanWallah model **[VERIFY]** | Advocate only |

### R6.2.6 Metered usage (API, white-label and enterprise)

| Meter | Unit | Indicative price | Notes |
|---|---|---|---|
| `API_AGREEMENT_GENERATE` | per document generated from template via API | ₹10–₹25 by volume | For lenders, proptech, HR platforms |
| `API_ESIGN_AADHAAR` | per successful signatory | ₹16–₹22 by commitment | Pass-through ESP cost + margin |
| `API_ESTAMP` | per stamp | ₹35–₹49 + duty | Pure-agent duty |
| `API_CALLS_OVERAGE` | per 1,000 calls above tier | ₹100 | Rate limits separate from billing |
| `COURT_DATA_REFRESH` | per matter-refresh | ₹1.5–₹3 | Licensed provider pass-through |
| `STORAGE_OVERAGE` | per 100 GB-month | ₹1,000 | — |
| `WHATSAPP_NOTIFY` | per message | Meta India rate + ≤ 20% | Meta per-message pricing since 1 Jul 2025; INR billing migration by 31 Dec 2026 |
| `AI_CREDITS` | per credit beyond allowance | ₹1.00 (B2C), ₹2.50 (B2B) | No surprise overage: hard stop by default |

### R6.2.7 Retainers and managed legal department (LDaaS)

| Retainer | Who it is for | Inclusions (seed) | Indicative fee / month | Structure note |
|---|---|---|---|---|
| **Startup Legal Officer** | Pre-Series A startups | Hour bank 6 h; contract reviews; founders/ESOP/SHA; TM filings at member price; monthly compliance calendar; Business plan included | ₹14,999–₹24,999 | Advocate-led for legal advice; CS for ROC. Invoice split: advocate fee (RCM for companies) + LawDocs SaaS (18%) |
| **SME Legal Desk** | SMEs, LLPs | Hour bank 10 h; notices; vendor contracts; litigation tracking; HR policies | ₹24,999–₹49,999 | Same |
| **NBFC / FI Regulatory Retainer** | NBFC-BL/ML, HFCs, co-op societies, IFSCA units | RBI/SEBI/IFSCA advisory; policy reviews; board-meeting support; returns calendar; dedicated RM as **maker user**, client **checker** (owner brief) | ₹50,000–₹2,50,000 | Cross-sell LawDocsComply under the group neutrality rule; never bundle-tie |
| **Managed Legal Department (LDaaS)** | Mid-size companies without in-house legal | Named legal manager (advocate), CLM operations, litigation management with external counsel panel, monthly board-ready legal MIS, SLA eSigned in tool | ₹75,000–₹3,00,000 | **[LEGAL]** must be supplied by an advocates' firm (contracted or affiliated), not LawDocs Pvt Ltd. LawDocs bills SaaS and coordination only |
| **Hour bank top-up** | Any retainer | Extra hours | ₹2,500–₹6,000/h by seniority | Utilisation target 70–85% (LDC N.13) |

### R6.2.8 Academy (FinLegal Academy, trainings.lawdocs.in)

Courses are publicly visible without login (owner brief). Indicative price ladder `[OWNER TO SET]`: micro-course (1–2 h) ₹499–₹999; certificate course (DSA/DMA, KYC/AML, POSH, DPDP) ₹2,999–₹9,999; professional programme (CISO, compliance officer, drafting masterclass) ₹14,999–₹49,999; corporate seat licences 20–40% off list; Business/Enterprise plans include 2–5 seats/year of compliance micro-courses. Certificates carry verification URLs. Live competitor prices for Indian compliance courses were not re-checked in this stream **[VERIFY]**.

---

## R6.3 Marketplace fee structure by profession (with legality notes)

**Design rule.** LawDocs charges **the buyer** a disclosed **platform/facilitation fee** for LawDocs's own service (discovery, scheduling, secure workspace, payment handling, escrow-style hold, invoicing, vault). It **never takes a share of a regulated professional's fee**, never charges a regulated professional for listing, ranking, leads or badges, and never pays them referral rewards. Professionals may optionally buy the **Pro plan (software)** on the same terms as any customer. Their plan status is never readable by ranking or allocation (EQ RS-57 pattern).

| Profession | Listing fee | Commission on professional's fee | Buyer platform fee (LawDocs supply) | Professional's SaaS | Payment flow | GST treatment | Legality notes | Default |
|---|---|---|---|---|---|---|---|---|
| **Advocates / law firms** | **₹0 (prohibited to charge)** | **0% (prohibited)** | Flat ₹49–₹199 per booking, or ≤ 10% of order value shown as a **separate line** (flat preferred) | Optional Pro plan; no visibility effect | Route: advocate's fee → advocate's linked account; LawDocs fee → LawDocs | Advocate → individual: exempt; → business: RCM (recipient pays); LawDocs fee: 18% forward; TCS s.52 not on RCM/exempt **[TAX MEMO]**; TDS Sl. 8(v) 0.1% | BCI r.36; Madras HC 2024; BCI notices Mar 2025; Rule 20 (no contingent fee). Directory: factual, consent-based, neutral ordering (relevance, language, availability, distance; never paid). No reviews that act as advertising **[LEGAL]** | ON (flat buyer fee); % variant OFF |
| **Chartered accountants** | ₹0 | 0% (CA Act First Schedule bars sharing fees with non-members **[VERIFY]**) | Same as above | Optional | Route | CA services 18% forward (by the CA); TCS 0.5% on taxable supplies where LawDocs collects; TDS 0.1% | ICAI advertisement and online-platform guidelines **[VERIFY]** | ON |
| **Company secretaries** | ₹0 | 0% (CS Act First Schedule **[VERIFY]**) | Same | Optional | Route | 18% forward by CS; TCS/TDS as above | ICSI guidelines **[VERIFY]** | ON |
| **Cost accountants** | ₹0 | 0% | Same | Optional | Route | 18% | ICMAI 2025 referral-network bar | ON |
| **Trademark agents (non-advocate)** | ₹0 recommended (Trade Marks Act agent conduct rules **[VERIFY]**) | 0% recommended | Same | Optional | Route | 18% | Treat as regulated | ON |
| **Tax return preparers / GST practitioners (non-CA)** | Permitted commercially | Up to 15% **[LEGAL]** | Same | Optional | Route | 18%; TCS 0.5% | Not governed by a professional-conduct statute equal to BCI/ICAI; still apply CCPA endorsement rules | OFF until legal review |
| **Notaries (facilitation only)** | ₹0 | 0% | Facilitation fee per instrument | — | Notary fee pure agent | 18% on facilitation | Notaries Act 1952; remote notarisation not permitted **[VERIFY]** | OFF |
| **Translators, typists, process servers, document couriers, valuers, investigators** | Permitted | 10–20% take | — | Optional | Route | 18% | Ordinary commercial services; E-Commerce Rules 2020 seller disclosures | ON |
| **Mediators / arbitrators** | Route to **Equator** (separate platform, neutrality rules) | — | — | — | — | — | EQ Appendix AB governs; LawDocs only refers on the user's choice | Referral only |
| **LawDocs in-house GRC professionals** | n/a | n/a | n/a (LawDocs is the supplier) | — | LawDocs account | 18% forward | Non-advocacy compliance services only, or supplied via the affiliated advocates' firm for legal advice | ON |

**Disclosures on every booking page:** professional's own fee; LawDocs platform fee (separate line); GST per supplier; that LawDocs "is not a law firm and does not give legal advice"; grievance officer (E-Commerce Rules 2020); cancellation and refund code.

---

## R6.4 Consumer-help (grievance) desk: legality of success fees

**Context (owner brief).** A consumer-help desk modelled on FREED, ClaimBuddy and Insurance Samadhan, covering loans, lending, insurance and challans, with "a dedicated legal team" approaching companies. The brief also notes that separate entities may be formed.

| Option | Description | Legal position | Recommendation |
|---|---|---|---|
| C-1 Free self-help | Templates, regulator escalation paths (RBI CMS, IRDAI Bima Bharosa, consumer e-Jagriti), status tracker in vault | No issue | **ON** in Free/Personal |
| C-2 Flat fee for drafting and escalation by **non-advocate** case managers | Fixed ₹499–₹2,999 per complaint, no outcome link | Permissible as a documentation and facilitation service if it does not amount to practising law (A.K. Balaji risk if advice or representation) **[LEGAL]** | ON after legal memo; separate entity per owner brief |
| C-3 Flat fee **plus success fee** charged by a **non-advocate entity** (e.g., 10–20% of amount recovered) | Insurance Samadhan/FREED-style **[VERIFY current fee levels]** | No express ban for non-advocates, but there are four risks: (i) the IRDAI position on unregistered claim-assistance entities **[VERIFY]**; (ii) RBI concern about debt-relief/settlement firms and their effect on borrowers' credit records **[VERIFY]**; (iii) the CCPA unfair-trade-practice and Dark Patterns Guidelines 2023 (drip pricing, false urgency); (iv) DPDP consent and purpose limitation | **OFF by default.** If switched on: separate entity, success fee capped (e.g., ≤ 10%) and disclosed upfront, no fee on regulator-ordered refunds the consumer could get free, written opinion from counsel |
| C-4 Success fee where an **advocate** acts | Contingent fee | **Prohibited** (BCI Rules Ch. II r.20) | **Deny-list** |
| C-5 Challan contest via advocate | Flat fee | Permissible if flat and not result-linked | ON (flat) |
| C-6 Lead fees from lenders/insurers for routing complaints | — | Conflict of interest with the consumer; possible inducement | **Deny-list** |

---

## R6.5 Revenue-stream registry (RS-LD-01 … RS-LD-45)

Columns: stream; segment; model; default at launch; legal review needed ("Y" = [LEGAL]/[TAX MEMO] before ON). Kill-switch scope follows EQ AB.2.5 (stream, segment, jurisdiction, profession).

| Code | Stream | Segment | Model / unit | Default | Legal review |
|---|---|---|---|---|---|
| RS-LD-01 | Personal membership | Individuals, families | Annual/monthly subscription | ON | N (cooling-off copy) |
| RS-LD-02 | Pro subscription | Professionals, freelancers, startups | Per workspace + seats | ON | N |
| RS-LD-03 | Business subscription | Companies, LLPs, NBFCs | Per workspace + band | ON | N |
| RS-LD-04 | Enterprise contracts (incl. dedicated environment rental) | Banks, NBFCs, groups, platforms | Annual licence / monthly rental | ON | Y (MSA, DPA, RE outsourcing addendum) |
| RS-LD-05 | Add-on components (§R6.2.3) | All paid | Monthly add-on | ON | N |
| RS-LD-06 | Extra seats | Pro, Business | Per seat | ON | N |
| RS-LD-07 | Aadhaar eSign credit packs | All | Prepaid credits | ON | Y (ESP contract; IT Act Second Schedule eSign) |
| RS-LD-08 | Electronic / OTP signature packs | All | Prepaid credits | ON | N |
| RS-LD-09 | eStamp facilitation | All | Per stamp + duty pure agent | ON per state rule pack | Y (state stamp Acts; provider terms) |
| RS-LD-10 | Vidhi AI credit packs | All | Prepaid credits | ON | N (AI disclosure) |
| RS-LD-11 | Vidhi role-agent seats | Pro, Business, Ent. | Per agent/month | ON | N |
| RS-LD-12 | Court-data refresh (pass-through) | Pro, Business, Ent. | Per refresh / matter-month | ON (licensed provider only) | Y (provider licence; DPDP) |
| RS-LD-13 | Trademark watch | Pro, Business | Add-on | ON | N |
| RS-LD-14 | Data room | Pro, Business, Ent. | Per room / period | ON | N |
| RS-LD-15 | Premium support tiers | All paid | Monthly | ON | N |
| RS-LD-16 | API access tier and overage | Platforms, lenders | Monthly + per call | ON | Y (API terms) |
| RS-LD-17 | Embedded / white-label agreement + eSign + eStamp (B2B2C) | Lenders, proptech, HR-tech | Per document / per sign | ON | Y (RE outsourcing directions where client is an RE) |
| RS-LD-18 | White-label practice workspace | Law/CA/CS firms | Monthly + per client workspace | ON | Y (no client solicitation features) |
| RS-LD-19 | One-time services by LawDocs (non-advocacy: drafting tools, compliance, filings via CS/CA) | All, no subscription needed | Per order | ON | Y (A.K. Balaji boundary) |
| RS-LD-20 | Retainers (Startup Legal Officer, SME Desk, NBFC Retainer) | Startups, SMEs, FIs | Monthly / annual | ON | Y (advocate-firm structure; RCM invoicing) |
| RS-LD-21 | Managed Legal Department (LDaaS) | Mid-size companies | Monthly | OFF until structure memo | Y |
| RS-LD-22 | Hour-bank top-ups | Retainer clients | Per hour | ON | N |
| RS-LD-23 | Buyer platform fee on marketplace bookings (flat) | Marketplace buyers | Flat per booking | ON | Y (E-Commerce Rules 2020; Amendment 2026 **[VERIFY]**) |
| RS-LD-24 | Buyer platform fee as % of order (separate line) | Marketplace buyers | % | OFF | Y |
| RS-LD-25 | Take rate on non-regulated service providers (translators, couriers etc.) | Providers | 10–20% | ON | N |
| RS-LD-26 | Take rate on non-CA tax preparers / GST practitioners | Providers | ≤ 15% | OFF | Y |
| RS-LD-27 | Commission / share of advocates', CAs', CSs', CMAs' fees | — | — | **Prohibited** | — |
| RS-LD-28 | Listing, featured, ranking, lead or badge fees from regulated professionals | — | — | **Prohibited** | — |
| RS-LD-29 | Referral rewards to regulated professionals | — | — | **Prohibited** | — |
| RS-LD-30 | Professional SaaS (Pro plan bought by a professional) | Professionals | Subscription | ON | Y (never affects ranking) |
| RS-LD-31 | Academy courses (B2C) | Learners | Per course | ON | N |
| RS-LD-32 | Academy corporate licences | Companies, FIs | Per seat / annual | ON | N |
| RS-LD-33 | Events and webinars (paid) | Professionals, companies | Per ticket / sponsorship | OFF | Y (no repeat-player sponsors on consumer-help pages) |
| RS-LD-34 | Advertising on public content pages | Non-legal B2B vendors | Per slot / CPM | **OFF** | Y (no ads by advocates/CAs/CSs, lenders, insurers; no third-party ad scripts) |
| RS-LD-35 | User referral credits (user → user) | Individuals, SMEs | Credits to both | ON | N (CCPA endorsement disclosure) |
| RS-LD-36 | Affiliate programme (bloggers, creators, non-professional partners) | Affiliates | % of first-year subscription | OFF | Y (no regulated professionals; disclosure #ad) |
| RS-LD-37 | Partner / reseller (software vendors, chambers of commerce, banks' SME desks) | Partners | Revenue share / wholesale | ON | Y (partner not a regulated professional) |
| RS-LD-38 | Group cross-referral (Finbyx, Udofin, Equator, LawDocsComply) | Group companies | Arm's-length flat fee per converted B2B account | OFF | Y (s.188 Companies Act; DPDP purpose limitation) |
| RS-LD-39 | Consumer-help flat fee (separate entity) | Individuals | Per complaint | OFF until memo | Y |
| RS-LD-40 | Consumer-help success fee (separate non-advocate entity) | Individuals | % of recovery, capped | **OFF** | Y (high risk) |
| RS-LD-41 | Implementation, migration and onboarding packages | Business, Ent. | Fixed fee | ON | N |
| RS-LD-42 | Data escrow / scheduled export to client storage | Business, Ent. | Monthly | ON | N |
| RS-LD-43 | Certified copy / court document retrieval service | Litigants | Per order + court fee | OFF | Y (court rules; advocate-only where required) |
| RS-LD-44 | Notarisation facilitation | Individuals | Per instrument | OFF | Y |
| RS-LD-45 | Aggregated anonymised legal-market reports | Media, policy | Per report | OFF | Y (k-anonymity ≥ 10; no matter-level data) |

**Deny-list additions for LawDocs (extend EQ AB.3.3):**
- **LD-X01.** No per-minute pricing set by ranked named advocates. Use fixed-slot flat fees with neutral ordering instead.
- **LD-X02.** No sale of user, matter or document data to lenders, insurers or marketers.
- **LD-X03.** No pre-ticked bundles or auto-renewing hidden subscriptions in checkout (the LegalZoom LLC-bundle pattern).
- **LD-X04.** No credit-bureau report marketing (see §R6.6 D-21).

---

## R6.6 Integration source catalogue (Part B)

Legend for **Official API?**: **Yes-open** = public API for anyone; **Yes-restricted** = official API for an eligible class only; **No** = web portal only. **Adapter** names follow the LDC Appendix L port style (`CourtDataProvider`, `TrademarkDataProvider`, etc.).

### R6.6.1 Courts, tribunals and litigation data

| # | Source | Data | Official API? | Vendor routes | Legality / terms | LawDocs adapter recommendation | Status |
|---|---|---|---|---|---|---|---|
| D-01 | **eCourts district and taluka courts** (services.ecourts.gov.in; eCourts Services mobile app; UMANG) | CNR search, case status by number/party/advocate/FIR/Act, cause lists, orders/judgments, caveat | **Yes-restricted.** NIC's eCourts "Open APIs" are published for **institutional litigants and government departments** to build monitoring tools. Nationwide data: apply to the **e-Committee, Supreme Court** in the prescribed format. State-only data: apply to the **High Court**. Credentials issued on approval. Published on "Bharat API", with 19 central and 55 state users (NJA deck). Shared with LIMBS (DoLA), CSCs, land records, UMANG | Third-party aggregators (D-08) | Portal is captcha-gated and built for one-case-at-a-time use. Automated scraping risks IT Act s.43 (unauthorised access/download), breach of site terms and DPDP issues for party names. Not explicitly prohibited by statute, but **do not scrape** | `CourtDataProvider` with three adapters: (1) **eCourtsOfficialApi**: apply for institutional-litigant access *on behalf of Enterprise clients that are institutional litigants* (banks, NBFCs) or explore whether a platform can apply **[VERIFY]**; (2) **LicensedAggregator** (default); (3) **ManualCNR**, where the user enters CNR and uploads orders and the system sets reminders | VERIFIED (API existence and process); platform eligibility **[VERIFY]** |
| D-02 | **NJDG** (njdg.ecourts.gov.in) | Pendency/disposal statistics by court, age, stage | No case-level API. Aggregate dashboards are public | — | Open aggregate data | Use for public "court delay" explainer content only | VERIFIED |
| D-03 | **High Courts** (hcservices.ecourts.gov.in and individual HC sites) | Case status, cause lists, orders | Same eCourts channel for HCs on the CIS platform; some HCs run their own systems | Aggregators | As D-01 | Via aggregator; manual fallback | VERIFIED (platform); per-HC coverage **[VERIFY]** |
| D-04 | **Supreme Court of India** (sci.gov.in) | Case status, cause lists, judgments | No public API | Aggregators cover SC | Judgments are public documents; respect site terms | Aggregator; judgments link-out | **[VERIFY]** |
| D-05 | **NCLT / NCLAT** (nclt.gov.in, efiling.nclt.gov.in; NCLAT e-filing portal) | Case status, cause lists, daily orders, judgments | No public API found | Aggregators (eCourtsIndia claims NCLT coverage) | Public portal | Aggregator; manual CNR/diary number | VERIFIED (portals); API absence **[VERIFY]** |
| D-06 | **DRT / DRAT** (e-DRT, drt.gov.in) | Case status, cause lists, orders (SARFAESI s.17, RDB Act OAs) | No public API found **[VERIFY]** | Aggregators | Public portal | Aggregator; important for NBFC Enterprise clients | **[VERIFY]** (search budget exhausted) |
| D-07 | **Consumer commissions: e-Jagriti** | Filing, case status for NCDRC/SCDRC/DCDRC. Replaced e-Daakhil, OCMS, CMS and CONFONET from **1 Jan 2025**; available in all states/UTs | No public API documented | Aggregators claim "Consumer Forums" | Public portal | Consumer-help desk deep-links to e-Jagriti filing. Status via aggregator or manual | VERIFIED (launch, scope); API **[VERIFY]** |
| D-08 | **Third-party court-data aggregators** | **eCourtsIndia API** (non-government): 30 REST endpoints; 600+ district courts, 25 HCs, SC, NCLT/CAT/consumer; order PDFs; AI summaries; MCP server (22 tools); PAYG packs ₹1,000–₹5,000 at 3× base; Enterprise from ₹10,000/month; ₹200 free; cause-list CNR batch check ₹0.30 / ₹0.10 per CNR; refresh is async re-scrape (2–10 min); no webhooks; limits 100/min, 3,000/h, 50,000/day; terms allow storing and displaying to your users but **no resale as a competing data service**. **Surepass eCourts API** (party-name search, CNR search API, bulk). **Claw** (25 HCs 1990–2026, SC 1950–2026, 9,102 courts claimed). **Perfios** (litigation background-check reports). Legitquest, CaseMine, Manupatra (research databases/APIs), Provakil (in-product tracking), "Kleop" **[VERIFY]** | n/a | All are private; sources are official portals | Aggregators re-collect public court data. LawDocs's risk is contractual (provider licence, accuracy, DPDP processor terms) and reputational. Contract must include: lawful-collection warranty, indemnity, India data residency, DPDP processor clauses, no resale restriction conflict, SLA, deletion | `CourtDataProvider.LicensedAggregator` with **two vendors** (primary + fallback) for coverage and continuity. Watch-list sync via scheduled diff (vendor has no webhooks). Meter `COURT_DATA_REFRESH` passes cost through. Never display "official" or "certified" for vendor data | VERIFIED (eCourtsIndia, Surepass, Claw claims); others **[VERIFY]** |
| D-09 | **Other tribunals** (ITAT, CESTAT, GSTAT, NGT, RERA authorities, Labour courts, state VAT tribunals) | Status / orders | Mostly no API | Partial aggregator coverage | Public portals | Manual matter type with reminder engine; aggregator where covered | **[VERIFY]** |
| D-10 | **eChallan / Parivahan** (traffic challans; court-referred challans to virtual courts) | Challan status, payment | Official consumer portal; API access via API Setu limited to authorised entities **[VERIFY]** | Vendors used by ChallanPay-type apps **[VERIFY]** | DPDP; Motor Vehicles Act data | Deep-link to official payment. Track in vault. Advocate contest via marketplace | **[VERIFY]** |

### R6.6.2 Intellectual property (trademarks)

| # | Source | Data | Official API? | Vendor routes | Legality / terms | Adapter recommendation | Status |
|---|---|---|---|---|---|---|---|
| D-11 | **IP India TM e-Register / Application status** (tmrsearch.ipindia.gov.in/estatus; eregister) | Status, examination report, hearing notices, certificate, renewal dates | **No** public API. JavaScript-heavy portal hosted by the IT Office, O/o CGPDTM | Filing-assistance vendors scrape or check manually | Respect site terms; avoid scraping | `TrademarkDataProvider`: **ManualAppNo** (user enters application number; LawDocs reminds and lets the user upload status PDFs) plus **WipoBrandDb** for status sync | VERIFIED (no API visible) |
| D-12 | **WIPO Global Brand Database** (branddb.wipo.int, India office slice) | Mark, owner, status, filing/registration dates, Nice classes, goods/services, images | Web database; third-party actors (e.g., Apify "india-trademark-search") at ~$0.05/record; watch mode $0.05/run | Apify actor; direct WIPO terms **[VERIFY]** | WIPO terms of use govern reuse **[VERIFY]**; screening, not legal clearance | Adapter **WipoBrandDb** for (a) pre-filing similarity screen, (b) weekly status-change watch. Label "screening aid, confirm with TM counsel" | VERIFIED (vendor); WIPO terms **[VERIFY]** |
| D-13 | **Trade Marks Journal** (weekly PDF on IP India) | Advertised marks for opposition | No API; public PDFs | Watch vendors | Public document | Ingest PDF → OCR → similarity against client marks (AI credits) → opposition deadline (4 months) reminders | **[VERIFY]** (journal format) |
| D-14 | Govt fees | TM-A ₹4,500 / ₹9,000 per class; renewal ₹9,000 | — | — | Trade Marks Rules 2017 | Fee table in rule pack with `last_verified_at` | VERIFIED (secondary) |

### R6.6.3 Company, tax-ID and identity data (onboarding and KYB)

| # | Source | Data | Official API? | Vendor routes | Legality / terms | Adapter recommendation | Status |
|---|---|---|---|---|---|---|---|
| D-15 | **MCA21 V3 master data** | CIN/LLPIN, status, capital, incorporation, address, email, AGM/BS dates, **signatories with DIN**, **index of charges**; View Public Documents ₹100 per company, certified copies ₹25/page | **No** public API for third parties; free master-data view with captcha | Licensed aggregators: **Probe42** (Corporates plan ~$44/month listed; API on quote), **Signzy**, **Surepass**, **Perfios-Karza**, **Qorpiq**, **InstaFinancials**, **Tofler** **[VERIFY each API price]** | No MCA scraping (LDC L.5.4). Aggregators' licences and collection methods must be warranted | `CompanyRegistryProvider` (primary Probe42 or Signzy; fallback Surepass). Store minimal fields with attribution and fetch date. Never store directors' PAN/DOB | VERIFIED (MCA view and fees); vendor pricing **[VERIFY]** |
| D-16 | **GSTIN search** | Legal name, trade name, status, constitution, registration and cancellation dates, jurisdiction, addresses, nature of business, e-invoice status | **Yes-restricted**: GSTN "Search Taxpayer" common API (`/commonapi/v1.3/search?gstin=…`) via a **GSP** (Vayana, Quicko, IRIS, others) with GSP auth tokens | GSPs | GSP contract; public taxpayer data | `TaxIdProvider.GstinViaGsp`; cache 30 days; multiple GSTINs per PAN | VERIFIED |
| D-17 | **PAN verification (Protean / NSDL)** | Name match, status | **Yes-restricted**: Protean Online PAN Verification for ~37 eligible categories (banks, NBFCs, insurers, SEBI intermediaries, govt, TDS/TCS filers with > 500 deductees/quarter). ₹12,000 + GST per year; screen 750 free/day; file/API 30p → 5p per PAN by annual volume; DSC login | KYC aggregators (Signzy, Surepass, HyperVerge, Gridlines, Karza) | **LawDocs is likely not eligible** in its own right (unless it qualifies as a TDS/TCS filer > 500 deductees per quarter). Use an aggregator, and contractually confirm the aggregator's lawful upstream access | `TaxIdProvider.PanViaAggregator`; store masked PAN + token. Enterprise REs may plug in their own Protean credentials | VERIFIED (Protean terms); aggregator lawfulness **[VERIFY]** |
| D-18 | **DigiLocker** (Requester / Authorized Partner APIs via NeGD, API Setu) | Issued documents (Aadhaar XML, PAN, DL, RC, marksheets, etc.) with user consent | **Yes-restricted**: Requester Organisation onboarding by a senior representative with official email domain; NeGD verifies. **No platform charges currently** (future charges notified in advance). Explicit informed consent per access. No caching beyond the permitted duration. No storage outside India without authorisation. Sub-entities need NeGD prior written approval. Requester liable for all use | Aggregators (HyperVerge, Signzy, Didit) | DigiLocker Terms of Use — Requester (June 2025) | `DigiLockerProvider` **direct** (LawDocs as Requester). Use it for "Login/verify with DigiLocker" and document pull into vault with consent. Aggregator as fallback only | VERIFIED |
| D-19 | **Aadhaar authentication / eKYC** | Yes/No or eKYC (demographics, photo) | **Yes-restricted**: AUA/KUA licence via UIDAI. Private entities may now seek permission under the **Aadhaar Authentication for Good Governance (Social Welfare, Innovation, Knowledge) Amendment Rules, 2025** (PIB, 31 Jan 2025): apply to the relevant ministry via portal → UIDAI examines → MeitY approves → ministry notifies | Licensed KUAs and aggregators (sub-AUA arrangements) **[VERIFY]** | Do not collect or store Aadhaar numbers. For signing, **eSign does Aadhaar authentication at the ESP**: the ASP may not send the Aadhaar number, which is captured on the ESP page (Protean FAQ) | **Do not become an AUA/KUA in v1.** Use (a) **DigiLocker** for identity documents, (b) **Aadhaar Paperless Offline eKYC (XML + share code)** or **Secure QR** for optional verification, (c) **eSign via ESP** for Aadhaar-backed signatures. Consider a 2025-Rules application later for "Login with Aadhaar" **[LEGAL]** | VERIFIED |
| D-20 | **Aadhaar offline verification (OVSE)** | Offline XML, Secure QR, Aadhaar Verifiable Credential (AVC), offline face verification | Aadhaar (Authentication and Offline Verification) Amendment Regulations, 2025: registered OVSEs (Reg. 13A application to UIDAI) for Paperless Offline e-KYC and AVC; Secure QR display-only without registration | — | Lawful purpose; consent; output storage per law | `IdentityProvider.AadhaarOffline` (QR display check; XML with share code). Register as OVSE only if a lawful purpose is established **[LEGAL]** | VERIFIED (secondary; Vinod Kothari, Dec 2025) |
| D-21 | **Credit bureaus** (TransUnion CIBIL, Experian, Equifax, CRIF) | Consumer credit reports | CICRA 2005 specified users. RBI 2022 eligibility for non-RE specified users (₹2 crore net worth, Indian ownership, 3 years' experience, IS audit). RBI has discouraged fintech access; Working Group recommended only REs act as consumers' agents | Consumer partner programmes of bureaus **[VERIFY current]** | High regulatory sensitivity; marketing use restricted | **Do not integrate in v1.** User uploads own report into vault (owner brief "CIBIL" onboarding item challenged). LDC P18 FR-P18-33 parity | VERIFIED (secondary, 2022 basis); current RBI position **[VERIFY]** |
| D-22 | **CKYC (CERSAI CKYCR)** | KYC records | Only REs (banks, NBFCs etc.) may search/download | — | PML Rules | **Not available to LawDocs.** For Enterprise RE clients, LawDocs can store the client-provided CKYC number only | Carried **[VERIFY]** |
| D-23 | **Account Aggregator** | Financial information | REs/FIUs only | — | RBI NBFC-AA Directions | **Not needed** for LawDocs. Udofin/Finbyx own it | Carried |

### R6.6.4 eSign and eStamp

| # | Source | Data / service | Official API? | Vendor routes | Legality / terms | Adapter recommendation | Status |
|---|---|---|---|---|---|---|---|
| D-24 | **CCA-empanelled ESPs**: eMudhra; **C-DAC**; **Capricorn Identity Services**; **Protean eGov Technologies**; **Verasys (vSign)**; **CSC e-Governance Services**; **CDSL Ventures (CVL)**. (n)Code Solutions not on the list viewed **[VERIFY]** | Aadhaar-OTP/biometric eSign (eSign API 2.1 online; 3.x offline with signer ID valid 2 years, offline KYC XML valid 3 months) | **Yes-restricted**: become an **ASP** with an ESP. Protean: application + agreement, DSC from a licensed CA, ≥ 50 successful UAT cases, audit compliance and go-live checklist, **advance payment**. Price on request | Aggregators: Leegality, Digio, SignDesk/Melento, Surepass SureSign, Signzy, Cashfree, emSigner | IT Act s.3A and Second Schedule (eSign); First Schedule exclusions (negotiable instruments other than cheques, powers of attorney, trusts, wills, contracts for sale/conveyance of immovable property) **[VERIFY current text]** | `ESignProvider` with **aggregator first** (fast launch: Leegality or Digio) and **direct ASP with one ESP later** (Protean or eMudhra) once volume justifies, to cut unit cost to wholesale. Block First-Schedule document types from Aadhaar eSign flows | VERIFIED (ESP list, Protean ASP steps) |
| D-25 | **eStamp — SHCIL** (Central Record Keeping Agency; ACCs) | e-Stamp certificates with UIN; verification portal | No public API for third parties; corporate/ACC arrangements | **Leegality BharatStamp** (procures series from authorised vendors; 25–31 States/UTs); **Surepass e-Stamping API** (SHCIL; 16 states); **emSigner** (NeSL + SHCIL routing, 29+ states claimed); **Digio**, **Legistify**, **Signzy Contract360** | Indian Stamp Act 1899 + state Acts; provider terms. Duty pure agent | `EStampProvider` with state rule pack (`state`, `article`, `duty formula`, `provider`, `last_verified_at`). Primary Leegality (widest coverage), secondary Surepass/Digio | VERIFIED (vendor claims) |
| D-26 | **eStamp — NeSL Digital Document Execution (DDE)** | eStamp + eSign + record for financial documents | Via NeSL partners | Leegality (NeSL DDE add-on), emSigner | IBC information utility context | Enterprise lender use cases only (loan agreements), via aggregator | VERIFIED (vendor claims) |
| D-27 | **Physical stamp paper / franking** | Paper stamps | — | Local vendors | State rules | Courier fulfilment product (§R6.2.4) | Carried |

### R6.6.5 Workplace, CRM, messaging, video, payments, AI

| # | Source | Data / service | Official API? | Terms / constraints | Adapter recommendation | Status |
|---|---|---|---|---|---|---|
| D-28 | **Microsoft Graph** (OneDrive, SharePoint, Teams, Outlook, Entra ID) | Files, sites, calendars, online meetings, mail, SSO, SCIM | Yes-open (OAuth; admin consent) | Least-privilege scopes: `Sites.Selected` for libraries, delegated `Calendars.ReadWrite`, `OnlineMeetings.ReadWrite`, application access policy for mailboxes | `WorkplaceProvider.M365`: SSO, export to SharePoint/OneDrive folders preserving the LawDocs folder taxonomy, "Open in Word", Teams meeting for consultations (LawDocs internal team is on M365 Business per owner brief) | Carried from LDC L.5.5 **[VERIFY]** scope names |
| D-29 | **Google Workspace** (Drive, Calendar, Meet, Gmail, Admin SDK) | Same | Yes-open | Drive `drive.file` scope preferred (per-file) to avoid restricted-scope verification **[VERIFY]** | `WorkplaceProvider.Google`; same folder taxonomy; Docs export as .docx | **[VERIFY]** |
| D-30 | **Brevo** (contacts, lists, campaigns, transactional email/SMS, events, CRM deals/companies) | Marketing and transactional messaging | Yes-open (API v3). Rate limits: transactional email 3.6M RPH / 1,000 RPS (all plans); contacts 36,000 RPH / 10 RPS; events 36,000 RPH; other SMTP endpoints 300 RPH; **all other endpoints (likely incl. CRM) 100 RPH** (higher on Pro/Enterprise) | Marketing consent separate from service consent (DPDP); 429 handling | `CrmMarketingProvider.Brevo` **behind LawDocs's own CRM** (system of record stays in LawDocs per owner brief). Sync contacts/consents one-way out, events back. Batch CRM-deal sync to respect 100 RPH. Migration kit: export contacts with consent provenance | VERIFIED (limits) |
| D-31 | **WhatsApp Business Platform** (Meta Cloud API; BSPs incl. JioCX) | Template and service messages | Yes-open (Cloud API) | **Per-message pricing since 1 Jul 2025**. India marketing rates rose 1 Jan 2026. 1,000 free service messages/number/month. **From 1 Oct 2026 utility templates inside the service window and service messages beyond the free tier are charged**. India INR billing from 1 Jan 2026; **non-INR accounts must migrate by 31 Dec 2026, or delivery stops from 1 Jan 2027**. Volume tiers for utility/authentication | `WhatsAppProvider` Cloud API direct (lowest cost) with BSP alternate (JioCX **[VERIFY BSP status]**). Opt-in only. Never for legal notices or debt recovery. Create the account in INR | VERIFIED (Meta doc) |
| D-32 | **YouTube embeds** (vlog section, tutorials) | Video | Embed via `youtube-nocookie.com` (privacy-enhanced mode) | Privacy-enhanced mode avoids setting cookies until the user plays, but local storage/identifiers may still be used on play **[VERIFY]**. Use click-to-load facade with consent notice (DPDP/GDPR/CCPA) | `VideoEmbed`: facade thumbnail → load nocookie iframe on click; captions on (accessibility) | **[VERIFY]** |
| D-33 | **Razorpay APIs** | Orders, Payments, Payment Links, **Subscriptions** (plans, add-ons, plan change), **Invoices** (not used as GST tax invoice; LawDocs issues its own), **Route** (linked accounts, transfers, `on_hold`, reversals), **Smart Collect** (customer identifiers, VPA, TPV), Refunds, UPI Autopay/e-mandate, webhooks with `X-Razorpay-Signature` HMAC-SHA256 | Yes-open (merchant) | PA Directions 2025 (§R6.1.5). Route for marketplace splits. No card data stored (PCI-DSS SAQ-A scope). Server-side fetch before marking paid. Idempotency by event id | `PaymentGateway.Razorpay` (group account owned by Ops Hub billing per ecosystem spec). Route ON for marketplace. Smart Collect for Enterprise/retainer invoices by bank transfer | VERIFIED (Route, Smart Collect, fees); event list **[VERIFY]** |
| D-34 | **Claude API** (Vidhi) | LLM | Yes-open | Regulated classes India-resident route (Bedrock ap-south-1/2 per LDC L.5.1) **[VERIFY]** | `LlmProvider` per LDC | Carried |
| D-35 | **Jio Business** (JioCX SMS/WhatsApp/Voice, Haptik AI agents) | CPaaS, AI agents | Commercial APIs | Flags OFF until contract, residency and no-training terms | Per LDC L.6 mapping | Carried **[VERIFY]** |

### R6.6.6 Build sequence for adapters (recommended)

1. **v1 launch:** DigiLocker (direct), eSign + eStamp via aggregator (Leegality primary, Digio fallback), GSTIN via GSP, PAN and company data via one KYB aggregator, court data via one licensed aggregator plus manual CNR, TM via manual application number plus WIPO Brand DB screening, Razorpay (Orders, Subscriptions, Route, webhooks), M365 export and SSO, WhatsApp Cloud API (utility only), YouTube facade.
2. **v1.1:** second court-data vendor; TM Journal watch; Brevo sync; Google Workspace; Smart Collect; data room.
3. **v2:** direct ASP with an ESP (unit-cost reduction); eCourts official API for Enterprise institutional litigants (client-credentialed); Aadhaar 2025-Rules application (if a "Login with Aadhaar" purpose is approved); OVSE registration if warranted.

---

## R6.7 Unit-economics guard-rails (private; pricing committee)

| Metric | Guard-rail |
|---|---|
| Gross margin (subscriptions) | ≥ 75% after hosting, AI inference, ESP/stamp allowances, support |
| eSign included allowance cost | ≤ 15% of plan price (e.g., Personal 24 × ₹12 wholesale = ₹288 ≈ 19% of ₹1,499. **Renegotiate wholesale to ≤ ₹9 or reduce allowance to 18**) |
| AI credit cost | ≤ 40% of credit price at blended model mix (LDC N.13) |
| Pass-through margin (court data, duty-adjacent services) | Disclosed; ≤ 20% over cost |
| Marketplace buyer fee | Covers PG fee (2.36% all-in) + Route transfer fee + support; never hidden |
| Retainer utilisation | 70–85% of hour bank |
| CAC payback | ≤ 6 months Personal; ≤ 12 months Pro/Business |

---

## R6.8 Open items for the owner and counsel

1. **[LEGAL]** Structure for "LawDocs legal team" advisory, retainers and LDaaS: affiliated advocates' firm vs contracted panel. Invoicing (advocate bill with RCM vs LawDocs SaaS invoice).
2. **[LEGAL]** Marketplace directory design against BCI r.36, the Madras HC 2024 judgment and the BCI March 2025 notices. Review policy (whether to show reviews of advocates at all).
3. **[TAX MEMO]** SAC for SaaS and platform fee. TCS s.52 exclusion for RCM/exempt advocate supplies. TDS characterisation guidance for buyers (s.393 Sl. 6(iii).D(a) vs D(b)). Pure-agent treatment of duty and government fees.
4. **[VERIFY]** Razorpay negotiated rates (UPI, Route transfer fee, Smart Collect, Subscriptions). MCC approval for a legal-services marketplace.
5. **[VERIFY]** eCourts official API eligibility for a platform vs institutional litigant clients. Aggregator contracts with lawful-collection warranties.
6. **[LEGAL]** Consumer-help desk entity and fee model (success fee OFF by default). IRDAI and RBI positions on claim-assistance and debt-relief intermediaries.
7. **[VERIFY]** ICAI/ICSI current fee-sharing and advertisement guidelines for online platforms.
8. **[OWNER TO SET]** All price points in §R6.2–§R6.3.

---

## R6.9 Sources (all accessed 25 October 2026 unless a different page date is noted)

| # | URL | Title / description | Page date (if shown) |
|---|---|---|---|
| S-01 | https://www.legalkart.com/ | LegalKart home: chat/talk rates, starter pack | — |
| S-02 | https://www.legalkart.com/en/talk-to-lawyer | LegalKart — Talk to a Lawyer Online | — |
| S-03 | https://businessworld.in/article/legalkart-launches-mobile-app-for-law-professionals-176563 | LegalKart launches app for law professionals | — |
| S-04 | https://www.g2.com/products/legalkart/pricing | G2 — LegalKart pricing (not listed) | — |
| S-05 | https://www.rocketlawyer.com/membership | Rocket Lawyer membership plans | — |
| S-06 | https://ailawyer.pro/blog/rocket-lawyer-vs-legalzoom | Rocket Lawyer vs LegalZoom 2026 (current prices) | prices as of 6 Jun 2026 |
| S-07 | https://www.indiafilings.com/company-registration/pricing | IndiaFilings — Private limited company pricing | — |
| S-08 | https://www.indiafilings.com/gst-registration/pricing | IndiaFilings — GST registration pricing | — |
| S-09 | https://www.indiafilings.com/partnership/pricing | IndiaFilings — Partnership pricing | — |
| S-10 | https://www.legalwiz.in/private-limited-company-registration | LegalWiz — Private limited company registration | — |
| S-11 | https://vakilsearch.com/online-trademark-registration | Vakilsearch (Zolvit) — Trademark registration | — |
| S-12 | https://restthecase.com/services/company-registration/private-limited-company | RestTheCase — Private limited plans | — |
| S-13 | https://disytax.com/?p=23139 | Trademark registration cost in India 2026 (govt and professional fees) | 14 May 2026 |
| S-14 | https://www.businesstoday.in/amp/personal-finance/tax/story/jiofinance-rs24-itr-filing-plan-vs-cleartax-taxbuddy-tax2win-how-they-stack-up-490599-2025-08-22 | JioFinance ₹24 ITR plan vs ClearTax, TaxBuddy, Tax2Win | 22 Aug 2025 |
| S-15 | https://leegality.com/pricing | Leegality pricing | — |
| S-16 | https://leegality.com/blog/estamping | Leegality — What is digital stamping in India | — |
| S-17 | https://melento.ai/en-in/pricing | Melento (formerly SignDesk) pricing (redirect from signdesk.com/pricing) | — |
| S-18 | https://productgrowth.in/tools/kyc-identity/digio/ | Digio profile and pricing estimates | updated Feb 2026; checked 17 Oct 2026 |
| S-19 | https://www.zoho.com/sign/pricing.html | Zoho Sign pricing | — |
| S-20 | https://www.esign.ai/blog/india-docusign-subscription-rates-inr | DocuSign subscription rates India | 9 Oct 2026 |
| S-21 | https://hyperverge.co/blog/e-signature-pricing-models/ | E-signature pricing models 2026 (emSigner ₹75/envelope) | — |
| S-22 | https://docs.emsigner.com/signing-up-for-a-subscription/user-plans/for-individual-single-user/pay-and-sign | emSigner Pay & Sign | — |
| S-23 | https://www.producthunt.com/p/signsetu/signyu | SignYu — Aadhaar eSign ₹15/use | — |
| S-24 | https://www.cashfree.com/aadhaar-esign/ | Cashfree Aadhaar eSign | — |
| S-25 | https://www.capterra.com/p/209812/Provakil/ | Capterra — Provakil pricing | 19 Oct 2026 |
| S-26 | https://spendflo.com/vendors/spotdraft | Spendflo — SpotDraft pricing | — |
| S-27 | https://www.hyperstart.com/blog/spotdraft-pricing/ | SpotDraft pricing guide 2026 (competitor) | 9 Jul 2026 |
| S-28 | https://costbench.com/software/ai-legal-tools/clio/ | Clio plans and pricing | verified 29 Aug 2026 |
| S-29 | https://www.capterra.com/p/105428/Clio/pricing | Capterra — Clio pricing | — |
| S-30 | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ | Razorpay payment gateway pricing explained | 13 Feb 2026; updated 11 Oct 2026 |
| S-31 | https://www.softwaresuggest.com/blog/razorpay-payment-gateway-charges/ | Razorpay payment gateway charges | 17 Mar 2026; updated 23 Oct 2026 |
| S-32 | https://www.skydo.com/compare/razorpay-pricing | Razorpay pricing (export) — Skydo | 2026 |
| S-33 | https://axisbank-docs.razorpay.com/payments/route/faqs/ | Razorpay Route FAQs | — |
| S-34 | https://Razorpay.com/docs/payments/smart-collect/ | Razorpay Smart Collect docs | — |
| S-35 | https://www.medianama.com/2025/09/223-explained-rbi-master-direction-payment-aggregators/ | Explained: RBI Master Direction on Payment Aggregators | Sep 2025 |
| S-36 | https://vinodkothari.com/wp-content/uploads/2025/09/Key-Highlights-of-PA-2025-2.pdf | Key highlights of PA Directions 2025 | Sep 2025 |
| S-37 | https://amlegals.com/reverse-charge-gst-advocate-lawyer/ | Legal services under reverse charge (PIB release text; Notification 13/2017-CT(R) Sl. 2) | 2017 |
| S-38 | https://itatonline.org/articles_new/?p=4216 | Liability of advocates to register for and pay GST | Jun 2017 |
| S-39 | https://www.taxmann.com/post/blog/ecos-to-collect-0-5-tcs-on-net-value-of-taxable-supplies-made-through-it-by-other-suppliers-notification/ | Notification 15/2024-CT: ECO TCS 0.5% | 10 Jul 2024 |
| S-40 | https://blog.tdsman.com/2026/05/tds-on-fees-for-professional-and-technical-services-section-3931-194j/ | TDS on professional/technical fees — s.393(1) | May 2026 |
| S-41 | https://blog.tdsman.com/2026/07/tds-on-e-commerce-transactions-section-3931-194o/ | TDS on e-commerce transactions — s.393(1) Sl. 8(v) | Jul 2026 |
| S-42 | https://busy.in/sac-code-998431/ | SAC 998431 — rate 18% before/after 22 Sep 2025 | — |
| S-43 | https://busy.in/sac-code-998212 | SAC 998212 — legal advisory (page inconsistent on rate) | — |
| S-44 | https://www.medianama.com/2025/03/223-the-bar-council-of-india-warns-against-legal-advertising-online/ | BCI warns against legal advertising online | 18 Mar 2025 |
| S-45 | https://nja.gov.in/Concluded_Programmes/2022-23/P-1300_PPTs/1.eCourts.pdf | NJA — eCourts (NIC SDU Pune): Open APIs for institutional litigants | 2022–23 |
| S-46 | https://informatics.nic.in/uploads/infocus/1df267ad_21_28_inf_ecourts__web.pdf | Informatics — eCourts (Open APIs for departments; UMANG; NJDG) | Jul 2019 |
| S-47 | https://ecourtsindia.com/api | eCourtsIndia API (non-government) | — |
| S-48 | https://blogs.ecourtsindia.com/2026/04/16/ecourts-india-api-developer-guide/ | eCourtsIndia API developer guide (pricing, limits, terms) | 16 Apr 2026 |
| S-49 | https://surepass.io/ecourts-api/ | Surepass eCourts API | — |
| S-50 | https://clawlaw.in/blog/court-records-api-in-india-what-it-is-and-how-it-works | Court records API in India (Claw) | 2026 |
| S-51 | https://openjustice-in.github.io/ecourts/ecourts.html | Open Justice India — ecourts toolkit (unofficial) | — |
| S-52 | https://en.wikipedia.org/wiki/E-Jagriti | E-Jagriti (launch 1 Jan 2025) | — |
| S-53 | https://nclt.gov.in/ | NCLT portal (cause lists, case status) | — |
| S-54 | https://tmrsearch.ipindia.gov.in/estatus | IP India — e-Register and application status | — |
| S-55 | https://apify.com/nexgendata/india-trademark-search.md | India Trademark Search — WIPO Brand DB actor | — |
| S-56 | https://startupflora.com/post/mca-master-data-v3 | MCA master data V3 — fields and fees | — |
| S-57 | https://www.softwaresuggest.com/probe42/pricing | Probe42 pricing | — |
| S-58 | https://docs.gsp.vayana.com/GSTN/searchTaxpayer-get-api/ | Vayana GSP — Search Taxpayer API | — |
| S-59 | https://tinpan.proteantech.in/faqs/online-pan-verification/faq-pan-verify-general.html | Protean — Online PAN verification FAQs | — |
| S-60 | https://cf-media.api-setu.in/resources/DigiLocker-Terms-of-User-Requester-june-2025.pdf | DigiLocker Terms of Use — Requester (June 2025) | Jun 2025 |
| S-61 | https://negd.gov.in/wp-content/uploads/2025/02/PIB2098223-1.pdf | PIB — Aadhaar Authentication for Good Governance Amendment Rules 2025 | 31 Jan 2025 |
| S-62 | https://authbridge.com/blog/aadhaar-authentication-amendment-2025 | AuthBridge — Aadhaar authentication amendment 2025 | 3 Feb 2025 |
| S-63 | https://gridlines.io/blogs/?p=5214 | Gridlines — Aadhaar offline verification and OVSE | — |
| S-64 | https://vinodkothari.com/2025/12/a-new-way-to-verify-aadhaar-offline-introduction-of-face-matching/ | Vinod Kothari — Aadhaar offline face matching (2025 amendments) | 10 Dec 2025 |
| S-65 | https://cca.gov.in/service-providers.html | CCA — Empanelled eSign Service Providers | — |
| S-66 | https://www.proteantech.in/services/esign | Protean eSign | — |
| S-67 | https://cms.proteantech.in/sites/default/files/2023-09/FAQ_1.pdf | Protean (NSDL e-Gov) eSign FAQ — ASP onboarding, API 2.1/3.0 | Sep 2023 |
| S-68 | https://emudhra.com/en/emsigner/feature-bharat-estamping-details | emSigner Bharat eStamping (NeSL and SHCIL) | — |
| S-69 | https://surepass.io/suresign/e-stamping-api/ | Surepass e-Stamping API | — |
| S-70 | https://www.bajajhousingfinance.in/resources/buying-e-stamp-online | Buying e-stamp online (SHCIL process) | — |
| S-71 | https://law.asia/credit-access-data/ | Giving credit greater access to data (CICRA specified users) | c. 2022 |
| S-72 | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing | Meta — WhatsApp Business Platform pricing | — |
| S-73 | https://baat.ai/blog/whatsapp-api-pricing-india | What the WhatsApp Business API costs in India (2026) | 2026 |
| S-74 | https://developers.brevo.com/docs/api-limits/llms.txt | Brevo API rate limits | — |
| S-75 | /home/claude/ldpack/ref/LDC/appendices/N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model.md | LDC Appendix N (sister pack; re-verified, not copied) | 25 Oct 2026 |
| S-76 | /home/claude/ldpack/ref/EQ/appendices/AB_Revenue_Architecture_v3_and_Stream_Registry.md | EQ Appendix AB (deny-list and governance model) | 23 Oct 2026 |
| S-77 | /home/claude/ldpack/ref/LDC/appendices/L_Integration_Adapters_and_API_Catalogue.md | LDC Appendix L (adapter conventions; M365, Razorpay, Jio) | 25 Oct 2026 |
| S-78 | /home/claude/ldpack/src/Owner_Brief_25Oct2026.md | Owner brief | 25 Oct 2026 |

**Access note.** All web sources were read through WebSearch/WebFetch, with no curl or scripts. The shared WebSearch budget for the session ran out before Jio BSP status, YouTube privacy-enhanced embed behaviour, Google Drive scope rules, DRT/Supreme Court API checks, ICAI/ICSI clause text and consumer-help success-fee benchmarks could be searched. Those rows are marked [VERIFY] and should be checked in a follow-up pass.
