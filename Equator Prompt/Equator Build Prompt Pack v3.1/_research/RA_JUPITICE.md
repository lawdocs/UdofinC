# RA_JUPITICE — Jupitice and the Jupitice ADR Marketplace

**Competitor research for the Equator Marketplace (Equator Resolution v3.0)**
Prepared 23 October 2026 · Research assistant note · Inputs: public web pages opened on 23 Oct 2026; pack v2.1 Appendices T and H (read-only).

**Tagging convention (applies to every statement about Jupitice):**
- **[C]** company self-description: what Jupitice says about itself on its own sites, in press releases or in sponsored posts. This is the default. Read every Jupitice number, feature and recognition as [C] unless another tag is shown.
- **[V]** independently verified against a primary or official source (regulator website).
- **[3P]** third-party secondary source (press, directory, review or analyst site), labelled as such. Press items that are company-supplied are shown as [C/3P].
- **[U]** not confirmed or not accessible.
- **[R]** our recommendation, not a fact.

**Method and limits.** Each page was opened individually with WebFetch, which renders the page as text; nothing was scraped in bulk. `www.jupitice.com` and `app.jupitice.com` refuse automated fetching (robots_disallowed), and those refusals were respected. The bare host `jupitice.com` returned its homepage and two shell pages. Several marketplace pages are client-rendered (Next.js), so some content (FAQ answers, consultation form, product menu) did not render as text. Those gaps are recorded as [U] and are not taken to mean the content is absent. No login was attempted. Jupitice's text is summarised and never reproduced. WebSearch was used 15 times, within the 30-call budget.

---

## Sources

All accessed **23 October 2026**.

| # | Title / page | URL | Type |
|---|---|---|---|
| 1 | Jupitice ADR Marketplace, home | https://jupiticeadrmarketplace.com/ | Company self-description |
| 2 | ADR Service Providers (provider landing, empanelment) | https://jupiticeadrmarketplace.com/adr-service-providers | Company self-description |
| 3 | Online ADR (buyer journey) | https://jupiticeadrmarketplace.com/online-adr | Company self-description |
| 4 | Online ADR Services | https://jupiticeadrmarketplace.com/online-adr-services | Company self-description |
| 5 | Jupitice ADR Platform | https://jupiticeadrmarketplace.com/jupitice-adr-platform | Company self-description |
| 6 | For Enterprises | https://jupiticeadrmarketplace.com/for-enterprises | Company self-description |
| 7 | Why Jupitice | https://jupiticeadrmarketplace.com/why-jupitice | Company self-description |
| 8 | About Us | https://jupiticeadrmarketplace.com/about-us | Company self-description |
| 9 | Leadership Team | https://jupiticeadrmarketplace.com/leadership-team | Company self-description |
| 10 | Leadership bio page (co-founder & CSO) | https://jupiticeadrmarketplace.com/mansi-omar | Company self-description |
| 11 | Leadership bio page (co-founder) | https://jupiticeadrmarketplace.com/shrey-aggarwal | Company self-description |
| 12 | Empanelment Rules | https://jupiticeadrmarketplace.com/empanelment-rules | Company self-description (rules) |
| 13 | Undertaking & Declaration | https://jupiticeadrmarketplace.com/undertaking-and-declaration | Company self-description (rules) |
| 14 | Escrow Services | https://jupiticeadrmarketplace.com/escrow-services | Company self-description (terms) |
| 15 | Buyer Protection | https://jupiticeadrmarketplace.com/buyers-protection | Company self-description |
| 16 | Seller Protection | https://jupiticeadrmarketplace.com/sellers-protection | Company self-description |
| 17 | Best Practices | https://jupiticeadrmarketplace.com/best-practices | Company self-description |
| 18 | Dispute Format | https://jupiticeadrmarketplace.com/dispute-format | Company self-description |
| 19 | Mediation Rules | https://jupiticeadrmarketplace.com/mediation-rules | Company self-description (rules) |
| 20 | Online Administered Arbitration Rules | https://jupiticeadrmarketplace.com/online-administered-rules | Company self-description (rules) |
| 21 | Online Expedited Arbitration Rules | https://jupiticeadrmarketplace.com/online-expedited-rules | Company self-description (rules) |
| 22 | Online Regular Arbitration Rules | https://jupiticeadrmarketplace.com/online-regular-rules | Company self-description (rules) |
| 23 | FAQs (questions rendered; answers did not render) | https://jupiticeadrmarketplace.com/faqs | Company self-description |
| 24 | Consultation (empty client-rendered shell) | https://jupiticeadrmarketplace.com/consultation | Company self-description |
| 25 | Contact | https://jupiticeadrmarketplace.com/contact | Company self-description |
| 26 | Terms of Use | https://jupiticeadrmarketplace.com/term-of-use | Company self-description (terms) |
| 27 | Privacy Policy | https://jupiticeadrmarketplace.com/privacy-policy | Company self-description (policy) |
| 28 | Cookie Policy | https://jupiticeadrmarketplace.com/cookie-policy | Company self-description (policy) |
| 29 | Sitemap (28 URLs, lastmod 14 Sep 2026) | https://jupiticeadrmarketplace.com/sitemap.xml | Company site metadata |
| 30 | robots.txt (returned 404 page) | https://jupiticeadrmarketplace.com/robots.txt | Company site metadata |
| 31 | Jupitice corporate homepage | https://jupitice.com/ | Company self-description |
| 32 | Schedule a demo | https://jupitice.com/schedule-demo | Company self-description |
| 33 | Contact us (shell; body did not render) | https://jupitice.com/contact-us | Company self-description |
| 34 | `www.jupitice.com` and `app.jupitice.com/authentication/default/login`: both refused (robots_disallowed) | https://www.jupitice.com/ ; https://app.jupitice.com/authentication/default/login | Not accessed [U] |
| 35 | SEBI investor website, SMART ODR: list of ODR institutions | https://investor.sebi.gov.in/smart_orr.html | Primary / official |
| 36 | Bar & Bench, "Jupitice's Integrated E-Stamping and Digital Signing Solution…" (1 Aug 2026; marked sponsored) | https://www.barandbench.com/news/jupitices-integrated-e-stamping-and-digital-signing-solution-for-enterprises-financial-institutions-and-legal-teams | Company self-description (sponsored) |
| 37 | Bar & Bench Viewpoint, "The missing infrastructure for India's eCourts vision…" (25 Aug 2025; sponsored) | https://www.barandbench.com/amp/story/law-firms/view-point/the-missing-infrastructure-for-indias-ecourts-vision-how-jupitice-fills-the-gap | Company self-description (sponsored) |
| 38 | Bar & Bench, "Jupitice reimagines Digital Justice Infrastructure with an Ironclad 'Trust Layer'…" (8 Jul 2026; reads as company-supplied) | https://www.barandbench.com/news/jupitice-reimagines-digital-justice-infrastructure-with-an-ironclad-trust-layer-for-ai-native-legal-operations | Company self-description |
| 39 | CXO Digital Pulse, "Jupitice's AI-powered ODR Platform Crosses 1.16 Lakh Resolved Disputes…" (16 Sep 2026; agency press release) | https://www.cxodigitalpulse.com/?p=62145 | Company self-description (press release) |
| 40 | India Legal, second Digital Lok Adalat (9 Nov 2022) | https://www.indialegallive.com/top-news-of-the-day/news/second-digital-lok-adalat-jupitice/ | Secondary press |
| 41 | Verdictum, "Rajasthan Gets AI-Powered Tool For Fast Disposal Of Cases At Lok Adalat" (18 Jul 2022) | https://www.verdictum.in/news/rajasthan-gets-ai-powered-tool-for-fast-disposal-of-cases-at-lok-adalat-1379641 | Secondary press |
| 42 | LiveLaw, MSME digital court (18 Oct 2021; PR-tagged) | https://livelaw.in/law-firms/deals/digital-court-jupitice-msme-digital-court-slough-pr-183844 | Company self-description (PR) |
| 43 | AffairsCloud, "Startup 'Jupitice' develops World's 1st Private Digital Court…" (18 May 2021) | https://affairscloud.com/startup-jupitice-develops-indias-1st-private-digital-platform-for-online-dispute-resolution | Secondary press |
| 44 | YourStory "Startup Bharat" profile (2021, per URL; undated in text) | https://cwv.yourstory.com/2021/06/startup-bharat-legal-tech-entrepreneur-digital-private-courts | Secondary press (founder interview) |
| 45 | Inc42, "Legaltech Startup Jupitice Raises $4 Mn…" (23 Dec 2021) | https://inc42.com/?p=272045 | Secondary press |
| 46 | Unlock Blockchain, Almas Capital investment (23 Dec 2021) | https://www.unlock-bc.com/en/uae-almas-capital-invests-in-blockchain-justice-tech-platform | Secondary press |
| 47 | Entrepreneur India, "Jupitice Launches AI-Backed Chatbot 'Saya'" (21 Mar 2023) | https://india.entrepreneur.com/news-and-trends/jupitice-launches-ai-backed-chatbot-saya/448028 | Secondary press (company statement) |
| 48 | Stanford CodeX TechIndex, Jupitice entry (reviewed Jul 2026) | https://techindex.law.stanford.edu/companies/jupitice | Secondary directory |
| 49 | FitGap, Jupitice product page (undated; source of fee figures not stated) | https://us.fitgap.com/products/042200/jupitice | Secondary directory |
| 50 | Gartner Peer Insights, Jupitice ODR Platform ("No Reviews Yet") | https://www.gartner.com/reviews/product/jupitice-odr-platform | Secondary review site |
| 51 | SoftwareOne Marketplace, Jupitice ODR Platform | https://platform.softwareone.com/product/online-dispute-resolution-odr-platform/PCP-5054-1960 | Reseller listing (vendor-supplied) |
| 52 | SoftwareOne Marketplace, Jupitice vendor page (9 products) | https://platform.softwareone.com/vendor/jupitice/VND-0803-3482 | Reseller listing (vendor-supplied) |
| 53 | IndiaLaw blog, Consumer Protection (E-Commerce) Amendment Rules 2026 (16 Sep 2026) | https://www.indialaw.in/blog/consumer/consumer-protection-e-commerce-amendment-rules-2026/pdf/ | Secondary legal commentary |
| 54 | SCC Online blog, Consumer Protection (E-Commerce) Amendment Rules 2026 (14 Sep 2026) | https://www.scconline.com/blog/post/2026/09/14/consumer-protection-e-commerce-amendment-rules-2026/ | Secondary legal commentary |
| 55 | Mondaq, "The Consumer Protection (E-Commerce) Rules 2020" | https://mondaq.com/india/dodd-frank-consumer-protection-act/985606/the-consumer-protection-e-commerce-rules-2020 | Secondary legal commentary |
| 56 | Equator pack v2.1, Appendix T §1.1.1, §1.4–§1.6 (Jupitice benchmark) | /home/claude/eqr/v4/pack/appendices/T_Benchmarks_Competitors_Institutions_Training_Jio_AI.md | Internal |
| 57 | Equator pack v2.1, Appendix H §1.1–§1.2 | /home/claude/eqr/v4/pack/appendices/H_Competitive_Differentiation_GTM_and_Website_Corrections.md | Internal |
| 58 | Equator pack v2.1, Appendices N §2 and §8, O (X-03, X-04, O-R2), B §B.7.7, G (LR-PAY-001/002), Q (DPDP), master NN-17 and NN-28 | /home/claude/eqr/v4/pack/ | Internal |

---

## Findings

### F1. Site map of what was visited (23 Oct 2026)

**Domains and entities.** Jupitice runs three web properties:
- `jupiticeadrmarketplace.com`, the marketplace marketing site (Next.js; sitemap lastmod 14 Sep 2026; footer © 2025);
- `jupitice.com`, the corporate "JusticeTech" site, most of it closed to automated fetching;
- `app.jupitice.com`, the login-gated application, closed to automated fetching.

Every "Get Started", "Join Now", "View More", "Ask Saya", "Raise a Ticket", "Manuals & Guides" and "Walk Through Video" button leads to the same login page [1][2][3]. The Terms of Use name the contracting parties as "Jupitice ADR Private Limited & Jupitice Justice Technologies Private Limited". Elsewhere they name only Jupitice Justice Technologies Pvt. Ltd. The registered office is in Rajiv Gandhi Chandigarh Technology Park and the corporate office is in Gurugram [26]. The contact page also lists a Jaipur regional office [25].

| URL (path on jupiticeadrmarketplace.com unless stated) | What it shows | Src |
|---|---|---|
| `/` | Hero ("Online ADR Marketplace"); a 4-step journey (Find → Transact → Perform → Resolve); 10 dispute tiles (loan defaults, contract, consumer, property, family, workplace, insurance, IP, personal injury, e-commerce); Saya AI co-pilot; enterprise block; testimonials (Angel One, Tata AMC, ICICI Securities); "trusted by" logos (Federal Bank, RBL, IndusInd, Ninjacart, TVS Credit, L&T Finance); headline numbers (F6). No search box, no prices | [1] |
| `/adr-service-providers` | Provider landing. Who can list (independent neutrals, ADR institutions, ecosystem service providers, law firms); 4-step empanelment (register → upload credentials → get verified → receive client invites); 19 "featured" expert cards (photo, name, title such as Judge/Arbitrator/Mediator); "View More" leads to login; growth claims (10x revenue, 20x clients, 40% less fee bad debt…) | [2] |
| `/online-adr` | Buyer journey: initiate case → browse and hire a neutral (algorithmic recommendation or choice from a "verified panel") → online resolution → enforceable outcome in "30–90 days"; comparison with courts; legal framework list (Mediation Act 2023, Singapore Convention, A&C Act 1996, New York Convention, UNCITRAL ODR Technical Notes 2016, APEC ODR 2019) | [3] |
| `/online-adr-services` | Four services (online negotiation, mediation, arbitration, a 3-tier "UN & APEC-based ODR") with step flows; ad hoc vs institutional explainer; "add Jupitice ADR services to your cart" (no prices) | [4] |
| `/jupitice-adr-platform` | Platform features by module (built-in video "not Zoom", caucus room, MoM, transcription/translation, template gallery, OTP e-signature, blockchain storage, analytics, escrow, marketplace access); on-premise/cloud/hybrid deployment; "pay-as-you-go pricing" | [5] |
| `/for-enterprises` | Bulk upload, **auto-assignment of neutrals**, dedicated case managers, analytics dashboard, workflow automation, blockchain-backed files; sectors served; claims (78% success, 60% faster, 80% lower cost, 20+ countries) | [6] |
| `/why-jupitice` | Differentiators; "pay-as-you-go SaaS"; numbers (5,000+ providers, 96% satisfaction…); **advisory board claim: 9 former Supreme Court judges and 23 former High Court judges**; claimed ISO 27001 and SOC 2; claimed recognitions (NITI Aayog, ICODR, NIC, Digital India, NCTDR) | [7] |
| `/about-us` | Origin (2018 mapping exercise; incorporated 2019); vision "Justice at your doorsteps"; two products: Justice Technology ERP and ADR Marketplace; Marketplace and Academy named as capacity-building aims | [8] |
| `/leadership-team`, `/mansi-omar`, `/shrey-aggarwal` | 13 leaders (founder & CEO, two co-founders, product, engineering, legal-domain, ODR-services leads); the CEO's government advisory roles (e.g. consulted by NITI Aayog in 2021). The two slug pages are **leadership bios, not provider profiles**. One bio claims 3,000+ practitioners onboarded, 30+ former SC/HC judges empanelled and the "Digital Lok Adalat" launch | [9][10][11] |
| `/empanelment-rules` | Neutral eligibility (11 pathways, mostly ≥ 10 years), ₹6 lakh income test, norms, assessment factors, 3-member Screening Committee, 3-year tenure, exemptions, confidential feedback, removal at discretion | [12] |
| `/undertaking-and-declaration` | Neutral undertakings (timeliness, court appearance, performance review) and a declaration (fit and proper, independence, confidentiality, reasoned awards, adjournments only with reasons) | [13] |
| `/escrow-services` | "Hourly agreement" escrow instructions: weekly billing, work diary, 5-day dispute period, release triggers, practitioner protection capped at USD 2,500 / 50 hours, Jupitice decides billing disputes | [14] |
| `/buyers-protection` | Escrow released on approval; milestone payments; "rated & reviewed" practitioners; refund of the "delivery platform subscription" on non-delivery; no caps or time limits | [15] |
| `/sellers-protection` | Three labels: guaranteed payment through escrow, a dispute mechanism, professional indemnity cover. No detail | [16] |
| `/best-practices` | 16 practices, identical for buyers and sellers. Item 1 says the platform is **desktop-only**. Claims GDPR/CCPA alignment and "flexible pricing plans" | [17] |
| `/dispute-format` | 8 relationship formats: B2B e-commerce, B2C e-commerce, G2C, G2G, G2B, government-to-investor, personal, traditional business and consumer | [18] |
| `/mediation-rules` | Mediation Rules effective 14 May 2021 (F4) | [19] |
| `/online-administered-rules` | Online Administered Arbitration Rules effective 14 May 2021; schedules not visible (F4) | [20] |
| `/online-expedited-rules` | Online Expedited Arbitration Rules effective 1 Sep 2022 (F4) | [21] |
| `/online-regular-rules` | Online Regular Arbitration Rules (1 Sep 2022 and, in Art. 1.7, 1 Jan 2025) (F4) | [22] |
| `/faqs` | 8 FAQ categories. Only the questions under "Case Handling Process" rendered, and no answers rendered [U] | [23] |
| `/consultation` | Client-rendered shell; page metadata reads "Generated by create next app"; no visible form [U] | [24] |
| `/contact` | Name/phone/email/message form; "Complaint Matrix for Securities Market Matters" (complaints against conciliators/arbitrators); grievance e-mail; three offices | [25] |
| `/term-of-use` | Terms of Use (F7) | [26] |
| `/privacy-policy`, `/cookie-policy` | Privacy Policy effective 4 Nov 2022; Cookie Policy with two conflicting effective dates (F7) | [27][28] |
| `/sitemap.xml`, `/robots.txt` | 28 URLs, but every `<loc>` begins with the literal "undefined" in place of the domain; robots.txt returns a 404 page | [29][30] |
| `jupitice.com/` | Corporate homepage. "Builders and Modules" no-code meta-platform; FAQ names Litigation Management, CLM, Compliance Management, Legal Notice Management, **Bharat Online Dispute Resolution Platform**, **SARFAESI Management**, Digital Law Office; claims ISO 9001 and ISO 27001 certification plus DPDP and HIPAA compliance, 2–4-week deployment, enforceability in "171 countries"; dashboard mock-up figures are all zero; the product menu shows "Loading Products…" | [31] |
| `jupitice.com/schedule-demo`, `/contact-us` | 30-minute Google Meet demo booking (10:00–19:00 slots); the contact page did not render | [32][33] |
| `www.jupitice.com`, `app.jupitice.com` | Refused (robots_disallowed); not accessed | [34] |

**Footer links that do not resolve** [1][2]: "Arbitration Rules" (no link, in both Buyer and Seller Centre); "Data Privacy Practices", "Blogs", "Newsletters" and "In News" (all `#`). Three rule sets in the sitemap (administered, expedited, regular) are not linked from the footer at all, so a party cannot easily find which arbitration rules apply.

### F2. Corporate identity, status and history

| Item | Finding | Tag |
|---|---|---|
| SEBI SMART ODR | "Jupitice" appears among the seven ODR institutions listed on SEBI's investor website, alongside CORD, CADRE, Webnyay, Presolv360, Sama and JustAct [35] | **[V]** |
| Founding | 2018 mapping exercise; incorporated 2019; Chandigarh [8][48] | [C]/[3P] |
| Funding | USD 4 million pre-Series A led by Almas Capital (UAE), 23 Dec 2021 [45][46]. TechIndex records total funding of USD 4 million and a "subscription" revenue model [48] | [3P] |
| Marketplace launch | A global ADR-professionals "Marketplace" was reported in May 2021 [43]. LiveLaw (PR-tagged) reported 7,000+ cases filed since the May 2021 launch, the MSME "digital court" and an MoU with TCIL [42] | [3P]/[C] |
| Early business model | In a 2021 founder interview: free for dispute-seekers, a percentage fee per transaction charged to "justice providers", percentage undisclosed, 300+ professionals on the platform [44] | [3P quoting founder] |
| Lok Adalat | Technology partner of the Rajasthan State Legal Services Authority for the "first AI-powered digital Lok Adalat", launched at the 18th All-India Legal Services Authorities' meet in Jaipur (reported 18 Jul 2022). Features: e-notices, settlement templates, custom video, voice chatbot, BI dashboards [41]. Second Digital Lok Adalat in Nov 2022 (Rajasthan and Maharashtra) [40]. Later claim: 25 million+ cases across six Lok Adalats [37] | [3P] / [C] |
| AI | "Saya" chatbot launched Mar 2023 at the ODR Forum, Bengaluru [47]; "Trust Layer" QA framework announced 8 Jul 2026, method not described [38] | [C] |
| e-Stamp / e-Sign | Sponsored post of 1 Aug 2026: three modes ("Jupitice Stamp Inventory" for physical stamp paper scanned and linked; Operational e-Stamp; Financial e-Stamp with loan fields), NeSL integration for the operational and financial flows, Aadhaar e-KYC, "15 digital signature types", API integration, transaction reference per attempt [36] | [C] |
| Scale claim (Sep 2026) | 1.16 lakh cases resolved; 80,000+ hearings; 3,000+ arbitrators and conciliators; 22 clients (14 enterprises, 8 institutions); 99% closure, 80% settlement, 75% "success" (undefined) [39] | [C] |
| Product catalogue | Nine products listed with a reseller: Compliance Management, CLM, Digital Law Office, Legal Notice Management, Litigation ERP (corporates), Litigation ERP (government), ODR Platform, **SARFAESI Management System**, **Smart Debt Collection ERP**. No public prices [52] | [C via reseller] |
| Review footprint | Gartner Peer Insights: "No Reviews Yet" [50]. No independent user-review corpus was found | [3P] |

### F3. Marketplace feature inventory (all [C] unless tagged)

| Dimension | What is publicly visible | Assessment |
|---|---|---|
| **Who lists** | Independent neutrals (negotiators, mediators, conciliators, arbitrators), ADR institutions, "ecosystem service providers" and law firms [2]. Featured cards show former judges, arbitrators and mediators [2]. Enterprise copy adds "industry specialists" [6] | Advocates appear only through law firms. Other professionals (valuers, CAs, CSs, translators, process agents) are not named as listing types |
| **What is sold** | Online negotiation (direct or assisted), mediation, arbitration, a 3-tier ODR package [4]; consultation booking [24]; the enterprise programme [6]; the underlying SaaS ("pay-as-you-go") [5][7] | Services are sold as "add to cart" products [4], but no price is shown anywhere |
| **Dispute taxonomy** | 10 consumer-facing tiles [1]; 8 "dispute formats" by relationship type, including government-to-X [18] | Two taxonomies that do not map to each other; no sub-types and no eligibility notes |
| **Search / filter** | No public search or filters [1][3]. The journey promises "algorithm recommendation" or choice from a verified panel [3]. FAQ questions mention finding a professional, availability and multi-neutral selection, but no answers rendered [23] | **Directory is login-gated.** Only 19 curated "featured" cards are public, and "View More" leads to login [2]. Search parameters and ranking logic are undisclosed [U] |
| **Booking** | Behind login. Mediation and arbitration rules let parties jointly nominate from the "Global Online Marketplace" panel, or from outside it for 3-member tribunals; otherwise the Administrator appoints with the Jupitice Advisory Board (JAB) [19][20][22] | Marketplace choice sits inside an institutional framework. In the enterprise lane, neutrals are **auto-assigned** [6] |
| **Payment** | "Jupitice Escrow", which may act through subsidiaries or affiliates; no bank or escrow agent is named. Hourly-contract model with a weekly billing cycle, Monday invoice generation by Jupitice "as the practitioner's agent", a 5-day client review and dispute window, and release on approval or deemed approval. Charges are irrevocable and non-refundable once taken. Jupitice adjudicates billing disputes and calls its decision final, though its "Dispute Assistance" is described as non-binding. A 30-day look-back applies [14] | The terms use the vocabulary of general freelance marketplaces (hourly contracts, work diaries, screenshots, weekly limits) rather than ADR fee structures such as registration, session and award fees or Fourth-Schedule-style fees. Internal contradictions: §2.2 says "four additional days" and §7.1 says five days [14] |
| **Buyer protection** | Release only on approval; milestones; "no service, no payment"; full refund of the "**delivery platform subscription**" if the practitioner does not deliver [15] | Implies buyers pay a platform subscription or fee, which conflicts with "free for seekers" [44]. No caps, time limits or decision-maker stated |
| **Seller protection** | Guaranteed payment through escrow, a dispute mechanism, professional indemnity cover [16]. Commission waiver on unpaid legitimate hours, up to USD 2,500 or 50 hours per client relationship [14] | Confirms a **commission exists**, though no rate is published. The insurer and limits of the "PI cover" are not stated [U] |
| **Onboarding / verification** | 4 steps: register → upload credentials → verified → client invites [2]. The Empanelment Rules require an application form, proof of qualifications, a CV, references, a background check and conflict screening; a Screening Committee of ≥ 3 is appointed by the CEO of the "Jupitice ADR Centre", with an optional interview and 3-year tenure [12]. Retired government employees need vigilance clearance. Professionals must show declared net professional income ≥ ₹6 lakh per year for the two preceding assessment years [12] | Rigorous on paper, but arbitration-centric: one set of criteria for every role, and "10 years in commercial and arbitration law" applied to mediators too. No mediation training hours, no mediator registration under the Mediation Act 2023, no published verification sources |
| **Exemptions / invitation** | SC/HC judges, judicial officers and designated Senior Advocates are empanelled on application; "eminent persons" by invitation [12] | Fast track for marquee names supports the advisory-board story [7] |
| **Ranking / featured** | "Featured" expert cards [2]; no ranking disclosure; recommendation algorithm undisclosed [3] | **Whether featured placement is paid is not disclosed [U].** No "sponsored" label anywhere |
| **Reviews / ratings** | Buyer page says practitioners are "Rated & Reviewed" [15]. Privacy Policy lists "moderating ratings and reviews" as a purpose [27]. ToU §9: first-hand reviews only; competitor affiliates may not post negative reviews; Jupitice may accept, reject or remove reviews at its sole discretion and takes a perpetual, sublicensable licence [26]. Empanelment Rules: party feedback is **confidential**, kept in a register for internal quality only [12] | No public ratings were seen. "Rated & reviewed" (public-facing) and "confidential feedback" (rules) conflict, and moderation is discretionary and unpublished |
| **Fees and commissions** | No amount on any page opened [1]–[28]. The rules defer to Schedules 1–3 (registration and administrative fees, hourly rates, sum-in-dispute), which did not render [20][22]. FitGap reports a practitioner commission of **18% (≤ USD 20,000 / ≤ ₹1.5 lakh), 15% (to USD 100,000 / ₹75 lakh), 14% (above)** per engagement relationship, invoiced fortnightly, plus a **3% client processing fee**, and "free to find and hire" [49]. FitGap does not say where these figures come from | **[3P], unverified.** The ₹ and USD band edges in [49] are not equivalent (₹1.5 lakh is far below USD 20,000), which suggests a copied or approximated table |
| **Provider subscription** | None advertised. Provider benefits include a "tailored profile", AI workflow and office tools, and "free escrow" [1][2]. The corporate SaaS is pay-as-you-go [5][7]. TechIndex records "subscription" [48] | Unknown whether listing is free [U] |
| **Revenue model (inferred [R])** | (i) commission on practitioner fees; (ii) possible client processing fee; (iii) institutional administration fees under the rule sets; (iv) enterprise SaaS and programme fees (BFSI bulk, auto-assignment); (v) government and Lok Adalat platform contracts; (vi) adjacent products (e-stamp/e-sign, LNMS, SARFAESI, debt-collection ERP) | The marketplace looks like a **top-of-funnel and credibility layer** (marquee judges, "10 Mn users"). Revenue appears to come mainly from enterprise and government deals [6][37][39] |
| **AI in the marketplace** | Saya "AI legal co-pilot" for ADR questions and in-process help [1]; for providers, "decision-making recommendations" and workflow help [2] | "Decision-making recommendations" to neutrals sits awkwardly with the requirement that the decision belongs to the human neutral. Guardrails are not published |
| **Support** | WhatsApp, phone, e-mail, tickets (login); a securities-market complaint matrix [25] | The grievance officer for the marketplace is not named in the ToU or Privacy Policy [26][27] |

### F4. Rules of procedure published on the marketplace (summary of structure, not text)

| Rule set | Effective | Key structural features | Defects visible |
|---|---|---|---|
| Mediation Rules [19] | 14 May 2021 | Administrator-run; joint nomination or Administrator appointment or list; JAB approves panel and advises; disclosure; confidentiality with no recording; target 120 days plus up to 60 by consent; 7-day response and objection windows; non-refundable filing fee; deposits; costs shared equally; e-signature allowed | Dated 2021 yet says mediation is "governed by the Mediation Act 2023"; jurisdiction clause conflict (Art. 13.1 "courts of the state" vs Art. 25.1 "courts of India"); Art. 24 incomplete; Art. 15.1 physical signing vs 15.2 e-signature |
| Online Administered Arbitration Rules [20] | 14 May 2021 | Administrator is a "technology-based intermediary" that administers but does not decide; sole arbitrator by default; 7-day joint-nomination window, then Administrator + JAB appoint; Administrator's appointment decisions final; choice of fee method (hourly, sum-in-dispute or agreed; hourly default); costs follow the event; award due 90 days from constitution; consent-based anonymised publication | Cross-reference errors; inconsistent terms ("ODR Service Provider", "Jupitice Provider"); Art. 9.7 incomplete; schedules not visible |
| Online Expedited Arbitration Rules [21] | 1 Sep 2022 | Sole arbitrator; documents-only default; tight business-day timetable; award within 45 days; no discovery or expert reports; opt-out allowed | No claim-value threshold stated; Art. 9.3 garbled ("within end days"); fee schedule not visible; payment by bank transfer |
| Online Regular Arbitration Rules [22] | 1 Sep 2022 / 1 Jan 2025 | "Intermediate" track between "Comprehensive" and "Fast Track" rules; switching by consent before oral argument; 45-day award; court-referred matters covered | Two effective dates; the "Comprehensive" and "Fast Track" rules referred to were not found on the site [U]; schedules not visible |

**Read-across.** Jupitice has a full rules library, but it is scattered: the footer "Arbitration Rules" link is dead and three arbitration rule sets are reachable only through the sitemap. Each set gives the Administrator and the JAB a strong default appointment role. For enterprise-originated consumer and borrower disputes, that default role, together with "auto-assigning of neutrals" [6], is exactly where appointment-defensibility risk sits (pack Appendix H §1.2 threat 1; NN-03). No public safeguard was found that stops an enterprise client from shaping the panel used for its own counterparties.

### F5. Jupitice platform and enterprise offering (all [C])

| Area | Self-described capability | Src |
|---|---|---|
| Positioning | A "Meta Product Platform": a no-code set of "Builders" and "Modules" for courts, tribunals, quasi-judicial bodies, government, corporates, law firms and ADR bodies; deployment in 2–4 weeks; modules customised in 30–60 days | [31][37][38] |
| ODR platform | Negotiation, conciliation, mediation and arbitration; case management; automated notice creation and tracking; digital hearing rooms; witness management; appointment of neutrals; execution of agreements and awards; back-office allocation, roles and scheduling; stakeholder dashboards; blockchain-backed records; digital signatures; audit trails; AI for document analysis, drafting, summarisation, transcription and translation, with "humans keep decision-making" | [39][5] |
| Hearings | Built-in audio and video; private sessions and caucus room; smart calendar; MoM creation; transcription and translation | [5] |
| Documents | Template gallery; smart document generation; submission-agreement generator (FAQ mentions an international version); settlement deed and MSA drafting and execution | [4][5][23] |
| Enterprise lane | Bulk case upload; **auto-assignment of neutrals** by expertise, jurisdiction and dispute type; dedicated ADR case managers; custom analytics; workflow automation; sectors: banks and NBFCs, insurers, e-commerce, MSMEs, logistics, tech/SaaS | [6] |
| Courts and government | E-filing, scrutiny, bench rostering, cause lists, bulk scheduling, payments, virtual hearings; Digital Lok Adalat; deployments claimed for state governments, regulatory commissions, the UN, Seychelles and Saudi Arabia | [37][41] |
| Corporate legal | Litigation ERP, Compliance Management, CLM, Legal Notice Management, Digital Law Office, SARFAESI Management, Smart Debt Collection ERP | [31][38][52] |
| e-Stamp / e-Sign | Three stamping modes, NeSL, Aadhaar e-KYC e-sign, 15 signature types, API, per-attempt transaction reference, auto-download of stamped PDF | [36] |
| AI governance | "Trust Layer": pre-release QA for AI outputs and workflows, "third-party-enhanced" testing; no method, metrics or audit published | [38] |
| Security / compliance | Claims vary by page: ISO 27001 and SOC 2 [7]; ISO 9001 and ISO 27001 plus "DPDP and HIPAA compliance" [31]; "GDPR and CCPA" [17]. No certificate number, certifying body or scope shown on any page opened | [7][17][31] |
| Deployment | On-premise, cloud or hybrid [5]; hosted in India [26] | [5][26] |
| Pricing | No public price list. Pay-as-you-go [5][7]; enterprise and reseller listings say "Enquire now" [51][52] | — |
| Channels | Reminders by e-mail, SMS, WhatsApp, registered post and in-app [17] | [17] |
| Mobile | Platform "accessible only on desktops" [17], although [5] says "from any device" | [5][17] |

### F6. Claims register: Jupitice's own numbers disagree across pages

| Metric | Values found (source) | Comment |
|---|---|---|
| Users | 10 Mn+ users worldwide; "10,000,000+ clients" [1]; 10,000,000+ users [7] | Not reconcilable with 1.16 lakh resolved cases [39] unless Lok Adalat traffic-challan registrations are counted [40] |
| Neutrals / providers | 4,000+ certified professionals [1]; 5,000+ empanelled providers [7]; 3,000+ practitioners onboarded [10]; 3,000+ arbitrators and conciliators [39]; 300+ in 2021 [44] | Three different "current" figures on the same family of sites |
| Cases | 100,000+ filed and processed [1]; 100,000+ closed in 2 years [7]; 1.16 lakh resolved [39]; 25 Mn+ in six Lok Adalats [37] | ODR and Lok Adalat volumes are mixed |
| Hearings | 83,000+ [1]; 80,000+ [39] | — |
| Speed | 45-day average [1]; 30–90 days [3]; "8X faster" [1]; "up to 90% faster" [5]; "60% faster" [6] | — |
| Cost | "85%+ lower" [1]; "80% reduced costs" [6]; "over 80%" [31]; "85% faster and cheaper" [4] | — |
| Outcomes | 78% success [6]; 99% closure / 80% settlement / 75% success [39]; 96%+ satisfaction [7] | Metrics are not defined |
| Enforceability | "More than 166 countries" [3]; "over 171 countries" [31] | A marketing simplification. Enforcement abroad depends on the seat, the enforcing state's Convention status and its reservations |
| Recognition | "Ranked #1 and featured by NITI Aayog and the Global ODR Forum; member of ICODR and NCTDR" [1]; NITI Aayog, ICODR, NIC, Digital India, NCTDR [7] | **Not verified [U].** The only verifiable government link found is the SEBI ODRI listing [35] and the CEO's stated NITI Aayog consultation in 2021 [9] |
| Clients | 22 clients (14 enterprises, 8 institutions) [39]; logos of six lenders and agri/fintech firms [1][6]; pack T records "180+ institutions group-wide" from an earlier source [56] | Inconsistent: 22 vs 180+ |

**Implication [R].** Jupitice sells on scale and prestige, but none of the metrics is defined, dated or tied to evidence. Equator's NN-17 Claims Register is a real differentiator if Equator publishes **fewer numbers, each defined, dated and evidenced**. Equator should not publicly comment on Jupitice's figures (defamation, comparative-advertising and CCPA misleading-advertisement risk); the value is in its own transparency.

### F7. Terms, privacy and data portability (as published)

| Topic | Jupitice position | Src |
|---|---|---|
| Intermediary status | Refers to Rule 3(1) of the IT (Intermediaries Guidelines) Rules **2011**, which were superseded by the IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 | [26] |
| Governing law / disputes | ToU §19.4 cross-refers to a "Paragraph 22 Governing Law and Dispute Resolution" whose body text is missing; numbering does not match | [26] |
| Amendments | Changes at any time without prior notice; the "Last updated" date is not shown | [26] |
| Content licences | Perpetual, irrevocable, sublicensable licence over user contributions and over submitted names, logos and brand material; feedback becomes Jupitice's property | [26] |
| Data loss / deletion | Users are "solely responsible" for their data; backups taken but no liability for loss; accounts and content may be deleted at any time without warning | [26] |
| Refunds | No refund if access is terminated for breach; no general refund policy; escrow charges non-refundable; mediation filing fee non-refundable | [14][19][26] |
| Privacy law basis | Effective 4 Nov 2022; names no statute (no DPDP Act 2023, no IT Act/SPDI Rules); refers to Indian law generally | [27] |
| Data collected | Includes PAN, TIN, **Aadhaar** (for identity verification) and **the user's contacts' details** | [27] |
| Sharing | With counterparties and practitioners after contract; service providers; affiliates and "guardian" company; **advertising and analytics partners** using tracking technology; contests and sweepstakes | [27] |
| Retention | ID-verification data 30 days; other data at least 5 years; backups longer | [27] |
| Rights | Access, correction, deletion and deactivation; **no portability**; no named Grievance Officer or DPO in the policy | [27] |
| Cookies | Consent implied by use; browser-only opt-out; "Do Not Track" not honoured; two conflicting effective dates | [27][28] |
| Age | 18+ only | [26][27] |

**Portability assessment [R].** No export function was described for parties, neutrals or institutions, and the ToU place the data-loss risk on the user. A neutral who leaves keeps no assured copy of their profile, reviews, fee history or case records. This is the clearest **anti-lock-in** opening for Equator, and it lines up with the v3 "portable data" requirement (self-explanatory folders of Word, Excel and PDF files).

### F8. Gaps and weaknesses visible publicly

| # | Weakness | Evidence | Equator opening |
|---|---|---|---|
| W1 | **No public directory.** Only 19 curated cards; search, profiles, fees and availability sit behind login | [2] | Public, no-login, filterable directory with fee bands and availability |
| W2 | **No published prices** for any service, commission or schedule; the FAQ "Fees & Payments" category is empty | [1]–[28]; [49] is 3P only | Calculator-driven, GST-inclusive public quotes (pack D7) |
| W3 | **Paid status of "featured" profiles undisclosed**; recommendation algorithm undisclosed | [2][3] | Published ranking parameters; any paid slot labelled and capped |
| W4 | **Review regime is discretionary and contradictory** (public "rated & reviewed" vs confidential feedback; sole-discretion removal) | [12][15][26] | Verified-engagement process reviews with a published moderation policy |
| W5 | **Escrow designed for hourly freelancing**, operated by Jupitice or affiliates with no regulated escrow bank named; Jupitice decides billing disputes; charges non-refundable | [14] | Bank escrow with trustee; ADR-milestone release; independent fee-dispute route |
| W6 | **Delisting at discretion without reasons**; arbitration-only eligibility applied to mediators; ₹6 lakh income test | [12][13] | Due-process delisting; role-specific, Mediation-Act-aware criteria; no income gate |
| W7 | **Enterprise auto-assignment of neutrals** with no published independence safeguard | [6] | Allocation engine with lender-trigger block (NN-03) |
| W8 | **Legal-document quality**: missing governing-law text, superseded 2011 Rules cited, conflicting dates and jurisdiction, broken cross-references | [19]–[22][26][28] | Versioned, QA-checked rules and terms with change logs |
| W9 | **Privacy policy predates the DPDP Act**; data shared with ad partners; no named Grievance Officer; no portability; implied cookie consent | [27][28] | DPDP-native notices, named officers, export-anything |
| W10 | **Site hygiene**: dead footer links, empty consultation shell, FAQ answers not rendered as text, sitemap URLs prefixed "undefined", robots.txt 404 | [1][23][24][29][30] | Server-rendered FAQ, rules and profiles, which help SEO/GEO and accessibility |
| W11 | **Unreconciled and undefined metrics**; recognitions not verified; prominence of sponsored press | F6; [36][37][39] | NN-17 Claims Register |
| W12 | **Desktop-only** (company statement) | [17] | Mobile-first, vernacular (pack D9, P12) |
| W13 | **No user-review footprint** on Gartner; no independent satisfaction evidence | [50] | Published party-feedback statistics (process items only) |
| W14 | **Breadth over focus**: 9+ products across courts, CLM, SARFAESI and collections; the ODR marketplace appears secondary to enterprise and government sales | [31][37][52] | Neutral-supply depth and institution-grade governance |

**Real strengths to respect (all [C] unless tagged):** SEBI ODRI listing [V][35]; the claimed advisory board of 9 former Supreme Court and 23 former High Court judges [7]; Lok Adalat credentials with the Rajasthan SLSA [3P][41]; a full rules library; BFSI logos; e-stamp and e-sign plus LNMS, SARFAESI and collections adjacency [36][52]; long-standing multichannel notices; an enterprise case-manager service model.

### F9. Corrections and extensions to the pack (Appendix T §1.1.1, §1.6; Appendix H §1.1; Appendix B §B.7.7)

| Pack statement | Correction / extension | Basis |
|---|---|---|
| T §1.1.1: dispute catalogue "not capturable (robots.txt blocks automated fetch)" | **Partly capturable.** `jupiticeadrmarketplace.com` is fetchable; `www.jupitice.com` and `app.jupitice.com` are robots-disallowed. Captured: 10 consumer tiles [1] and 8 relationship "formats" [18]. Update **OI-T-01 / OI-S3-01** to "partially closed; sub-types are in-app only" | [1][18][34] |
| T §1.1.1 Marketplace: tiered take-rate 18/15/14% + 3% [3P FitGap] | Keep [3P] but add "FitGap gives no source; the ₹/USD band edges are inconsistent." A 2021 founder interview confirms only "free for seekers; percentage per transaction from providers; rate undisclosed" [44]. The marketplace itself confirms that a commission exists (escrow commission waiver) [14]. Buyer protection mentions a buyer "delivery platform subscription" [15], so "free for resolution seekers" is **not confirmed** | [14][15][44][49] |
| B §B.7.7: "below Jupitice 18% (R1 §8.3)" | Internal rationale only. **Never use publicly** (NN-17): the figure is unverified 3P | [49] |
| T §1.1.1 Offering | Add: **SARFAESI Management System, Smart Debt Collection ERP, Litigation ERP (Govt), "Bharat Online Dispute Resolution Platform"**, no-code "Builders/Modules"; e-stamp modes as in F2 (NeSL; physical "Stamp Inventory"; "Stamp Wallet" is not mentioned in [36], so keep that from the pack's earlier source only) | [31][36][52] |
| T §1.1.1 Scale claims | Add the marketplace-site figures (4,000+ / 5,000+ providers; 10 Mn users; 83,000 hearings) and flag the 22-vs-180+ client conflict | F6 |
| T §1.1.1 Weaknesses | Add W1, W3–W10, W12 | F8 |
| T §1.6.1 F13 (public directory) Jupitice ◐ "marketplace" | Change to ◐ "**login-gated; 19 featured cards public; paid status undisclosed**" | [2] |
| T §1.6.1 F14 (code, complaints, feedback) Jupitice ○ | Change to ◐: Empanelment Rules and Undertaking & Declaration published; securities-market complaint matrix; feedback confidential | [12][13][25] |
| H §1.1 "ISO/IEC 27001" Jupitice ○ | Change to ◐ "**claimed** (ISO 27001, SOC 2, ISO 9001), not verified" | [7][31] |
| H §1.1 "Mobile apps" Jupitice ○ | Change to ✖ "desktop-only per company" (conflicting "any device" copy noted) | [5][17] |
| H §1.1 "Settlement-money collection" Jupitice ◐ | Clarify: the marketplace escrow covers **practitioner fees** (hourly model), not settlement sums. Equator's D2 differentiation stands | [14] |
| H §1.1 "Regulator recognition" Jupitice "SEBI ODRI" | Re-confirmed **[V]** on investor.sebi.gov.in (23 Oct 2026) | [35] |
| H §1.1 read-across: advisory council credited to Presolv360 | Add: **Jupitice claims 9 former SC and 23 former HC judges** on its advisory board [C] [7], plus a JAB with a formal role in appointments [19][20][22]. Equator's Advisory Council item (H §1.2 rank 4) applies to Jupitice too | [7] |
| T §1.5 Jupitice "Representation —" and "Pleadings —" | Marketplace lists law firms [2]; templates and submission-agreement generator [5][23] | [2][5] |
| Master §1 benchmark: "Lok Adalat-as-a-service" | Confirmed as RSLSA technology partner (2022) [3P]; later volume claims [C] | [40][41][37] |
| New | Funding USD 4 M pre-Series A, Almas Capital, Dec 2021 [3P]; Gartner shows no reviews [3P] | [45][50] |

### F10. Indian legal framework that shapes an Equator Marketplace (secondary unless stated; counsel to verify)

1. **Consumer Protection (E-Commerce) Rules 2020** (G.S.R. 462(E), 23 Jul 2020, per [53]). Rule 4 sets general duties (grievance officer to acknowledge within 48 hours and redress within one month); Rule 5 sets marketplace duties, including disclosure of seller details and of ranking parameters; Rule 6 sets seller duties [53][55].
2. **E-Commerce Amendment Rules 2026**: notified 9 Sep 2026, **commencing 1 Jan 2027** [54]. Reported changes [53]:
   - a technology-neutral definition of "ranking" (r.3(1)(j));
   - **plain-language disclosure of main ranking parameters in descending order of significance** (r.5(3)(f));
   - **sponsored listings to be clearly and prominently identified** (new sub-rule after r.4(11); number not given);
   - no manipulation of search results relative to the query (r.4(11)(c));
   - Dark Patterns Guidelines compliance with an **annual self-audit and a displayed certificate**;
   - no use of collected data to favour related sellers;
   - no bundled fees for unrelated services.
   **[VERIFY against the Gazette text; whether Equator's Marketplace is a "marketplace e-commerce entity" for services is open item Q-O1 in Appendix O.]**
3. **CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023** (30 Nov 2023), including "disguised advertisement" (pack LR-CONS-008, X-03; status UNVERIFIED in pack).
4. **Bar Council of India Rules, Part VI, Ch. II, Section IV, r.36**: advocates may not solicit or advertise beyond permitted website particulars (pack O S-15, X-03). Paid placement or referral fees for advocates are therefore OFF.
5. **RBI (Regulation of Payment Aggregators) Directions 2025** and the tripartite bank-escrow rule (pack LR-PAY-001/002): marketplace fees and neutral fees only; no settlement sums on the merchant account.
6. **DPDP Act 2023 and DPDP Rules 2025** (G.S.R. 846(E), 13 Nov 2025, per pack Q): notices, rights, grievance and consent. Portability is not a DPDP right, but Equator offers it as policy (pack Q PC-39).
7. **A&C Act 1996 s.12(5) and the Seventh Schedule**; *CORE v ECI-SPIC-SMO-MCML* (SC, 8 Nov 2024) as recorded in pack O X-05: no appointment influence for paying parties.

---

## Design implications for Equator

All items are **[R]**. "Locked" means super-admin and governance change only (ADR plus Board or counsel); "Tenant-configurable" means changeable in settings without a super admin. Build these as original Equator content: do not reuse Jupitice wording, page structure or rule text.

**A. Architecture: two surfaces, one firewall**

- **EQM-01 Two separate surfaces.** (a) The **Equator Panel Directory**: neutrals for Equator-administered matters, governed by NN-28, D2-14 and X-03, with no paid placement ever (locked). (b) The **Equator Marketplace**: private-practice neutrals, Private ADR Chambers tenants and listed professionals, for **non-administered** engagements booked party-direct. The CI test `NO_PAID_PLACEMENT` is extended so that no join path exists from the Panel Directory, the allocation service or any live-case screen to `mkt.sponsorships`. **Pack change required:** Appendix O X-03 and N §2 currently ban paid visibility everywhere; the v3 "preference placement" stream must be scoped to surface (b) only.
- **EQM-02 Listing types, each with its own schema and verification**:
  - neutral (mediator, conciliator, arbitrator, negotiator, expert determiner, POSH external member);
  - institution or Chambers;
  - advocate (BCI information-only profile);
  - other professionals (CA, CS, CMA, IBBI-registered valuer, translator or ISL interpreter, stenographer, process agent).
  The all-India advocates-and-professionals directory shared with Finbyx and Udofin is the **master record**. Equator Marketplace visibility is a per-company, consented projection of it.
- **EQM-03 Public, no-login search** (Jupitice gates it, W1). Filters: mechanism, dispute type, language, state and district, online or physical, fee band, earliest availability, accessibility (ISL, screen-reader), credentials, years of practice. Users can compare up to 3 profiles. Profiles are server-rendered for SEO/GEO (W10).

**B. Verification and onboarding**

- **EQM-04 Evidence-backed badges only.** Each badge shows its source, verification date and expiry: bar-roll or certificate of practice, ICAI/ICSI/ICMAI membership, IBBI registration, judicial-service record, mediator registration once the Mediation Act 2023 registration regime is operative [VERIFY commencement], and training credentials (pack N). Badges cannot be bought (locked).
- **EQM-05 Role-specific eligibility.** Mediator criteria rest on training and accreditation, not "10 years of arbitration law" (W6). There is **no income threshold** by default (Jupitice's ₹6 lakh test excludes regional and early-career practitioners). Tenants (Chambers) may add stricter criteria (tenant-configurable), but never fewer than the Equator floor (locked).
- **EQM-06 Due-process delisting.** Published grounds, notice, reasons, a 15-day reply window and appeal to a committee independent of sales. Categorised delisting statistics appear in the transparency report (contrast W6: "without reasons").

**C. Ranking and governed paid "preference placement"**

- **EQM-07 Organic ranking published.** A plain-language page lists the main parameters in descending order of weight (E-Com Rules r.5(3)(f) as amended, from 1 Jan 2027 [VERIFY]). Default order: relevance filter → seeded-random rotation within tiers. Outcome, settlement or "who won" metrics are never used (locked). Each result has a "Why am I seeing this?" link.
- **EQM-08 Sponsored slots: flag `mkt.sponsored_placement` OFF until counsel and Board sign-off.** When ON:
  - slots are separated from organic results and labelled "Sponsored — paid placement; not a recommendation by Equator";
  - default maximum is 2 slots per results page and never more than 20% of results shown;
  - sponsors rotate;
  - published flat rate card (no auctions at launch);
  - no slots for advocate listings (BCI r.36; locked OFF);
  - no slots on the Panel Directory, allocation, enterprise auto-assignment, AI assistant answers, live-case screens or e-mails to a respondent (locked).
  Sponsorship never changes badges, grades, reviews or organic rank (locked). Tenants cannot sell sponsored slots on Equator's surfaces.
- **EQM-09 AI assistant neutrality.** The marketplace assistant (Equator's answer to "Saya") explains processes and filters but never ranks or recommends a named provider on the basis of sponsorship, fees paid or plan. It gives no "decision recommendations" to neutrals in live matters (NN-01, NN-25). All prompts and answers are logged.

**D. Reviews**

- **EQM-10 Process-only verified reviews.** Only after a closed engagement; both sides are invited equally; items cover punctuality, clarity, courtesy, accessibility and timeliness, and never outcome. Public display needs n ≥ 10 (pack N §7.6). The moderation policy is published, with categorised removal statistics. Providers have a right of reply. Neither providers nor sponsors can remove reviews. Equator takes only a licence limited to display and does not take ownership of reviews (contrast [26] §9). Align with BIS IS 19000:2022 on online consumer reviews [VERIFY].

**E. Fees, payments and escrow**

- **EQM-11 Published take-rate and price breakup.** Take-rate by Chambers plan (Appendix O O-R2: 15/15/12/10%, Board pending) on a public page. Before payment the buyer sees: neutral fee, platform fee, GST and any processing fee as a separate line (no hidden 3%). 0% take on Equator-administered matters (unchanged).
- **EQM-12 ADR-native escrow.** Bank escrow with a trustee (LR-PAY-002) and release on ADR milestones (registration, each session, settlement or award signed), not hourly work diaries (W5). Stage-based refunds are published per service.
- **EQM-13 Independent fee disputes.** Fee disputes between buyer and provider go to a published fee-dispute mechanism handled by a neutral who is not on the provider's Chambers panel, with Equator staff recused. Equator is never the "final" decider of a provider's fees.
- **EQM-14 Provider economics.** Provider statements show GST and TDS treatment (Appendix B). Payout SLA defaults to T+3 after release (tenant-configurable within locked bounds). Any professional indemnity cover is shown with insurer, limits and exclusions, or not advertised at all (contrast [16]).

**F. Independence**

- **EQM-15 Conflict firewall across group companies.** If a professional acts as counsel for a lender, for example in Finbyx or Udofin NPA recovery suits or in execution and registration of awards, an automatic Seventh Schedule-style conflict check blocks their selection as a neutral in any matter involving that lender. The check runs on booking and on appointment (locked). Enterprise "auto-assignment" uses only the Equator allocation engine (NN-03), never sponsored lists (contrast W7).
- **EQM-16 No appointment influence for money.** No plan, sponsorship or training purchase buys priority, preference or a veto (X-05; locked).

**G. Portability and terms**

- **EQM-17 Export everything, any time, free.** A self-explanatory folder containing `README.pdf`, profile (DOCX/PDF), reviews (XLSX), engagements and invoices (XLSX plus PDF copies), fee notes, documents the user is entitled to, and a machine-readable JSON mirror. Delivered within 7 days, available on account closure with a 30-day grace period, never blocked for unpaid fees (pack NN-29).
- **EQM-18 Fair licences.** Licence over profile and brand material lasts only for the listing period plus 30 days. Feedback is not appropriated. Deletion only with notice, except for legal or safety reasons. Data-loss risk is not shifted to users (contrast [26]).
- **EQM-19 DPDP-native privacy.** Named Grievance Officer and DPO; granular cookie consent (no "consent by use"); no case data to advertising partners (locked); Aadhaar only through OVSE and DigiLocker flows (pack S); contact-list upload OFF.

**H. Trust, quality and transparency**

- **EQM-20 Claims Register on every marketplace number.** One canonical figure per metric, with definition, as-of date and evidence link (NN-17). No "#1", "world's first" or country-count enforceability claims (contrast F6).
- **EQM-21 Rules and terms QA.** Every rule set and terms page has a version, effective date, change log and redline. A CI linter checks cross-references, a present governing-law clause, a named grievance officer and live links (contrast W8, W10).
- **EQM-22 Quarterly Marketplace Transparency Report.** Listings by type; verification rejections; delistings by category; sponsored revenue as a share of marketplace revenue; review removals by reason; median payout time; fee disputes and outcomes.
- **EQM-23 Mobile-first and vernacular.** Marketplace, booking and payment work on mobile and in at least the launch languages (pack P12, D9). Minimum standard: WCAG 2.1 AA.

**I. Settings matrix (v3 rule engine)**

| Setting | Who changes | Default |
|---|---|---|
| Filters shown, profile sections, listing categories per tenant | Tenant admin | All on |
| Organic ranking weights | Locked (governance ADR) | Published default |
| `mkt.sponsored_placement` | Super admin after counsel + Board | OFF |
| Sponsored slot count / share cap | Super admin within locked max (2 / 20%) | 2 / 20% |
| Advocate sponsored slots | Locked | OFF |
| Take-rate by plan | Board-approved schedule | App. O |
| Client processing fee | Board + counsel | OFF |
| Review threshold n | Locked minimum 10; tenant may raise | 10 |
| Payout SLA | Tenant within T+2 to T+7 | T+3 |
| Export formats | Locked floor (DOCX/XLSX/PDF/JSON) | All |

**OFF pending counsel:** sponsored placement (E-Com Rules 2026 characterisation; Dark Patterns self-audit); any client processing fee; cross-border neutral payouts (FEMA and GST); listing of foreign neutrals for India-seated matters; e-commerce-operator TCS/TDS (Appendix O Q-O4).

---

## Open points

1. **Commission and fee figures.** No Jupitice page states a commission, client fee or rule-schedule amount. FitGap's 18/15/14% + 3% remains unverified and unsourced [49]. A manual capture of rule Schedules 1–3 (for example a PDF download or a demo call) is needed.
2. **Whether "featured" profiles are paid** [2]: not confirmed.
3. **FAQ answers, the consultation form and the product menu** did not render as text [23][24][31]. Manual browser capture is needed (extends OI-T-01).
4. **`www.jupitice.com` and `app.jupitice.com`** were not accessed (robots_disallowed). Product pages for LNMS, SARFAESI, Bharat ODR and the justice clock were not reviewed. **No public evidence of a "justice clock" product was found.**
5. **Certifications** (ISO 27001, SOC 2, ISO 9001) and **recognitions** (NITI Aayog "#1", ICODR, NCTDR) are not verified; certificate numbers and bodies are not shown.
6. **Advisory board** (9 former SC and 23 former HC judges) is a company claim only [7]. Not cross-checked.
7. **Training/Academy.** About Us names an "Academy" aim [8], but no training product page was found.
8. **E-Commerce Amendment Rules 2026.** Exact sub-rule numbers for sponsored-listing labelling and the dark-pattern self-audit, and the G.S.R. number, come from secondary commentary [53][54] and must be checked against the Gazette (notification reported 9 Sep 2026; commencement 1 Jan 2027).
9. **Mediation Act 2023 mediator-registration provisions**: commencement status not checked here.
10. **IS 19000:2022** (online consumer reviews): cited from background knowledge, not opened in this research. Verify before writing it into a specification.
