# R5 — LawDocs Site Inventory, Manual Analysis and Content Strategy

**Stream:** R5 (content strategy) · **Prepared for:** LawDocs build-prompt pack · **As of:** 25 October 2026
**Inputs:** Owner_Brief_25Oct2026.md; Manual_Documents.md, Manual_Pleadings.md, Manual_Compliance.md, Manual_Start_a_Business.md (Markdown conversions of the owner's Word manuals); live fetches of www.lawdocs.in and trainings.lawdocs.in; Google Search Central documentation.
**Method:** The manuals were parsed by script (headings, one-liners, FAQs, tables, templates, links, statutes). Web pages were fetched with WebFetch only. L = line numbers in `/home/claude/ldpack/src/`.

---

## 0. Executive summary

| Metric | Count |
|---|---|
| Manual sections parsed (H1 + H2, excl. TOC) | **Documents** 18 H1 / 134 H2 · **Pleadings** 13 H1 / 89 H2 (+2 empty H2 placeholders) · **Compliance** 8 H1 / 22 H2 · **Start a Business** 7 H1 / 26 H2 |
| Document template entries listed under "Templates" | 347 (→ **330 unique document pages** after removing 17 cross-hub repeats) |
| Documents sub-categories that are "(upcoming)" or sit in an upcoming category | 50 |
| Documents sub-categories that are stubs or empty (≤150 words) | 48 |
| Documents sub-categories with body copy but **no template list** (doc pages still to be defined) | 63 |
| FAQs in the manuals | Documents 673 · Compliance 179 · Start a Business 184 (Pleadings: none) |
| Requirement tables (Documents) | 60 sub-categories |
| Raw page count derived from the manuals | **666** (Documents 500, Pleadings 103, Compliance 30, Start a Business 33) |
| Recommended page count after de-duplication | **≈626** (Documents 483, Pleadings 82, Compliance 30, Start a Business 33) |
| Pleadings after consolidating duplicates | 89 → **68 canonical** pleading pages |
| Sections with copied third-party content (linked/branded) | **21 sections** across Compliance and Start a Business, plus 10 adapted testimonials (see §4) |
| Live site sitemap URLs | 186 (lawdocs.in) · Trainings store: 16 courses |

**Five findings that must shape the build:**

1. **The live site is effectively invisible to non-JavaScript crawlers and AI engines.** Every URL tested on www.lawdocs.in returns the same `<title>` ("LawDocs | NBFC & RBI Compliance, Legal Consultation Services"), the same meta description, and **no body content, no H1 and no links** to a non-rendering fetcher. AI crawlers mostly do not run JavaScript, so the new site must use server-side rendering or static generation (SSR/SSG).
2. **Host and sitemap conflicts.** The sitemap (`/lawdocs-sitemap.xml`) lists only non-www URLs, but deep non-www URLs return a client error, so only the www host serves pages. `robots.txt` disallows `/buy/`, yet the sitemap lists 20 `/buy/*` URLs. Every URL carries the same `lastmod` (2026-07-01). Old URLs that are still indexed (`/mortgage/`, `/services/consult-lawyer`) need 301 redirects.
3. **The manuals contain copied competitor content and fabricated-looking testimonials.** These include text that names Vakilsearch, Corpbiz, Provenience, LegalWiz, LegalRaasta, ebizfiling and Registrationwala; Wikipedia definitions; and proposal-software-style testimonials ("reduced the creation time of each proposal by 700%"). None of this can be published as it stands.
4. **Much of the legal content is out of date.** The criminal-law pleadings and the family sections cite CrPC, IPC and the Evidence Act, which BNSS, BNS and BSA replaced on 1 July 2024. Other stale references: Consumer Protection Act 1986, Udyog Aadhaar, Companies Act 1956, Listing Agreement, the GSTR-2/3 regime, CA-certified GST audit, the Income-tax Act 1961 (replaced from 1 April 2026), and pre-Code labour statutes (Codes in force from 21 November 2025).
5. **Google no longer shows FAQ rich results anywhere.** They were limited to authoritative government and health sites in August 2023, deprecated on 7 May 2026, and their documentation was removed on 15 June 2026. Google also says llms.txt is not used by Google Search. Keep FAQs for users, People Also Ask and other AI engines, but drop the rich-result goal.

---

## 1. Live site inventory

### 1.1 www.lawdocs.in — what a crawler sees

| Item | Observation (fetched 25 Oct 2026) |
|---|---|
| Rendering | Client-side rendered SPA. Fetcher receives `<head>` only: title, meta description, `google-site-verification`, viewport. No H1, body copy, nav, footer, CTAs, FAQs, testimonials or JSON-LD visible. |
| Title (all URLs) | "LawDocs \| NBFC &amp; RBI Compliance, Legal Consultation Services" (HTML entity double-encoded). |
| Meta description (all URLs) | "Expert NBFC compliance, RBI compliance, CKYC, CERSAI, NeSL registration, legal advisory and lawyer consultation services across India." |
| Positioning implied | Compliance-first (NBFC/RBI); does not match the brief's documents + eSign + Vidhi AI positioning. |
| robots.txt | `Allow: /`; disallows `/addblogs`, `/edit-blog/`, `/buy/`, `/payment-success`, `/payment-fail`; `Sitemap: https://lawdocs.in/lawdocs-sitemap.xml`. |
| sitemap.xml | `/sitemap.xml` does not serve a sitemap. `/lawdocs-sitemap.xml` (www) lists **186 URLs**, all non-www, all `lastmod 2026-07-01`. |
| llms.txt | Not present (the SPA shell is returned). |
| Schema markup | None detectable in served HTML. |
| Legacy indexed URLs | `/mortgage/`, `/services/consult-lawyer`, `/legal` appear in search results. Redirect these to the new architecture. |
| Third-party profile | Stanford CodeX TechIndex: founded 2020, New Delhi; templates, e-signature, compliance, AI chatbot. |

### 1.2 Sitemap URL groups (186 URLs)

| Group (prefix) | # | Leaf slugs | Purpose / gap |
|---|---|---|---|
| Core (`/`, about, team, career, contact, partnership, registration, legal, retainers, schedule-meeting, talk-to-lawyer, documentation-drafting, startup-services, compliance-services) | 14 | — | Company and conversion pages. `/legal` and `/talk-to-lawyer` overlap with `/compliance-services/consult-lawyer`. |
| `/advisory/*` | 6 | banking-and-finance, capital-markets, energy-law, fintech, insurance, sports-law | Practice-area pages. No equivalent in the manuals. Keep and expand. |
| `/buy/*` | 20 | adoption, adr, banking-finance, building-contract, companies, copyright, exchange-deed, family-settlement, gift-deed, lease, mortgage, partition, patent, power-of-attorney, pre-litigation, property-notice, release-noc, rent, sale-purchase, trademark, will | Purchase funnels. **Blocked by robots.txt but listed in the sitemap.** Make them noindex and drop them from the sitemap. |
| `/smartdrafts/*` | 19 | ipr (3), pleadings (adr, pre-litigation), property-matters (8), succession-and-inheritance (6) | Only about 14% of the manual's Documents tree is live. Redirect each one 301 to `/documents/...`. |
| `/compliance-services/agreements-contracts-drafting/*` | 7 | business, employment, licensing, service, settlement, vendor-supply | Service versions of document pages. Canonicalise against the document pages. |
| `/compliance-services/audit/*` | 6 | long sentence-slugs (e.g., `review-of-compliances-under-rbi-companies-act-fema-irdai-and-sebi`) | Bullet points published as URLs. Thin. Merge them into one Audit page. |
| `/compliance-services/business-legal-consultation/*`, `personal-…/*`, `property-…/*` | 3 + 18 | feature bullets as URLs (`100-confidential-secure`, `verified-senior-advocates`, …) | **18 thin, near-duplicate URLs.** Fold them into their parent pages and 301 or 410 them. |
| `/compliance-services/business-registration/*` | 17 | copyright, esi, fssai, gst, iec, llp, msme-udyam, opc, partnership, pvt-ltd, tm-objection, shops, startup-india, trade-licence, tm-registration, tm-renewal | Overlap with the Start a Business manual. Slugs have trailing hyphens (`fssai-licence-food-licence-`, `one-person-company-opc-`). |
| `/compliance-services/consult-lawyer/*` | 7 | bangalore, chennai, delhi-ncr, hyderabad, mumbai, other-cities | City pages. Risk of doorway pages unless each has genuinely local content. |
| `/compliance-services/irdai_*`, `rbi*`, `sebi_*`, `other_registration`, `reporting`, `roc` | 50 | IRDAI (10), RBI (17), reporting (6), SEBI (7), other registrations (CERSAI, CICs, CIMS, CKYC, CMS, Daksh, FIU-IND, NeSL, Pravaah) (10) | **The real differentiator: regulated-entity compliance.** The manuals do not cover it. Slugs use underscores. |
| `/compliance-services/property-real-estate-documents/*` | 7 | construction, gift deed, lease, partition, sale deed, title search | Duplicates the Documents property pages. |
| `/resources/*`, `/blogs` | 4 | laws-and-regulations, regulatory-updates | Thought-leadership hubs. No content reaches crawlers. |
| `/terms/*`, `/privacy-policy` | 3 | Disclaimer, refund-policy | `Disclaimer` is capitalised. There is no Terms of Use URL, no Grievance Officer page (IT Rules 2021 r.3(2)) and no DPDP notice. |

### 1.3 trainings.lawdocs.in (training academy)

| Item | Observation |
|---|---|
| Platform | Graphy storefront (footer "Launch your Graphy", `/s/store`, `/courses/<slug-id>`). Android app package `com.wPractical.courses`. |
| Title / H1 / meta | Title "LawDocs". H1 "LawDocs Trainings". Meta description "LawDocs training"; course pages use keyword lists as meta descriptions. |
| Brand | **"FinLegal Academy" appears nowhere.** The "Explore all THE TRAININGS" CTA links to **wpractical.com**, and the social links point to wPractical accounts: brand leakage. |
| Taglines | "Trainings for the legal professionals, students, entrepreneurs, corporates etc."; "The Practicals to make you Better."; "Meet those who became industry-ready."; "What would like to learn today?" (grammar); meta keyword "Learn to earn". |
| Categories | Paralegal; eMitra Trainings; Legal; Corporate Law; Information Technology. Audience pages: Lawyers, Entrepreneurs, Students, Businesses (corporate training lists no programmes and no prices). |
| Catalogue (16) | Free: Training for Customers and Borrowers; Legal Training for E-Mitra. Paid (sale/MRP ₹): International Paralegal 14,999/17,999; Drafting for Junior Counsels 7,999/10,000; Paralegal for Professionals 7,999/10,000; Paralegal for Students 5,999/8,000 (30 h, live Zoom weekly); Arbitration Practice & Procedure 14,999/18,000; PG CLAT 21,999/28,000; AoR Exam 21,999/28,000; Competition Law 8,000/12,000; Divorce by Mutual Consent 6,000/8,000; Securities Laws/SEBI Litigation 8,000/12,000; Consumer Protection 6,000/8,000; Smart Contracts & Blockchain 8,000/12,000; NBFC KMP Training 14,999/17,999; IT Training for NBFC Directors 14,999/17,999. Cashback "100 LawDocs Coins". |
| Gaps vs brief | No CISO, DSA/DMA (recovery agent) or compliance-officer tracks yet. The curriculum sections are empty, "Know the Mentors" shows **lorem ipsum**, every course page shows the same two reviews, and the "Who it's for" copy is generic (it lists "government decision-makers" for the NBFC KMP course). Fees are described as non-refundable. Contact: +91 9468774000 / 9468773000, trainings@lawdocs.in, Statesman House, Barakhamba Road, New Delhi. The manuals use +91 9468776000. **Choose one public number.** |
| Schema | Course info rich results were retired (docs removed 9 Sep 2025). Course/Offer markup is low value for Google but harmless for other engines. |

---

## 2. Manual-derived page architecture (summary; full table in §8)

**URL rules (recommended):**
- Section landings: `/documents`, `/pleadings`, `/compliance`, `/start-a-business`.
- Hubs: `/documents/{category}/{sub-category}`. Document leaf: `/documents/{category}/{sub-category}/{document}`. Pleading leaf: `/pleadings/{area}/{pleading}`. Service leaf: `/compliance/{group}/{service}` and `/start-a-business/{group}/{service}`.
- Lower-case, hyphens only: no underscores, no trailing hyphens, no stop-word sentences. Correct typos in slugs (`promissory-note`, `questionnaire`, `vakalatnama`).
- When a document appears in two hubs, publish **one canonical leaf** and link to it from the other hub. Do not create a second URL.
- Redirect existing URLs with 301s: `/smartdrafts/{a}/{b}` → `/documents/{a'}/{b}`; `/compliance-services/business-registration/*` → `/start-a-business/*`; `/compliance-services/roc/*` → `/compliance/roc-compliances/*`. Keep the RBI/SEBI/IRDAI/other-registration trees as a fifth section, `/regulated-entities/*`, because no manual covers them.

**Page types:** category hub (18 + 13 + 7 + 6), sub-category hub (134), document page (330 unique), pleading page (68 canonical), service page (48).

**Launch triage:**
- **Wave 1:** the 86 Documents sub-hubs with body copy, the 71 that have template lists, all 48 service pages, and the 68 canonical pleadings.
- **Wave 2:** the 63 sub-hubs whose document lists are still undefined (e.g., Formal Proposals, Senior Citizens Protection, Website Policies, Affidavits, RERA).
- **Hold:** the 48 stubs and "(upcoming)" placeholders. Keep them **noindex** until they have content, so the site does not publish thin pages.

---

## 3. Duplicates, mis-filing and heading errors

### 3.1 Duplicates
| Where | Issue | Action |
|---|---|---|
| D1.3 Distributorship & Agencies / D1.4 Franchise and License | Identical 10-item template lists and shared description blocks. The TOC calls the section "Distributorship, Franchise and License". | Keep two hubs with distinct copy and one canonical leaf per document. Move "Leave and license agreement" and "License to use immovable property" to Property > Rent/Lease. |
| D1.5 Mergers & Acquisitions / D5.4 Investment Support | M&A lists "Business Plan; Founders Agreement; Fund raising", which are wrong for M&A. | Give M&A real documents: share purchase agreement, business transfer agreement, term sheet, scheme of arrangement, due-diligence checklist. |
| D3.2 Banking & Finance / D3.3 Bonds | Installment bond and Loan bond appear in both. | Canonical location is Bonds. |
| D3.12 Release Deeds / D12.6 Release and NOCs | Release of right of way; release of interest in immovable property. | Canonical location is Property > Release and NOCs. |
| D3.4 Compromise / D12.2 Exchange & Settlement / D2.4 Maintenance | Three "compromise/settlement" drafts. | Differentiate them by context (debt, partition, matrimonial). |
| D10.10 Job Application and Offers / D16.2 Students > Application | Application for Job. | One canonical page. |
| D4.7 Proprietorship | Contains "Rent Agreement or Lease Agreement". | Link to Property > Rent. |
| D10.8 Job Agreements "ESOP" / D10.5 ESOP Schemes (upcoming) / C6.4 ESOP service | Three ESOP touchpoints. | Hub: the ESOP service page. The document: ESOP plan and grant letter. |
| D11.3 Mediation and D11.2 Arbitration | Same one-liner, "Conflict is inevitable, but combat is optional." This is a widely circulated quotation, not original. | Replace with an original line (see §6). |
| Documents vs Pleadings (Family) | Judicial separation, nullity, RCR and maintenance petitions exist in both manuals. | Documents keeps agreements and applications; Pleadings keeps court petitions. Cross-link them. |
| Documents vs Start a Business / Compliance | Trademark/Patent/Copyright, Partnership, Trust, Society, MSME, GST and Income Tax appear as both "documents" and "services". | Keep both intents with distinct H1s ("Trademark Assignment Deed" vs "Trademark Registration") and cross-link them. |
| Pleadings | 1 exact duplicate (Foreign Bill of Exchange); 10 duplicate-intent clusters (RCR ×3, judicial separation ×3, mutual consent ×3, nullity ×4, bail ×5, cheque bounce ×4, written statement ×2, specific performance ×2, civil appeal ×2, consumer ×5). | Consolidate 89 → 68 pages, with variants offered as toggles inside each page (forum, religion, petitioner). |
| Pleadings mis-filing | DV Act complaint filed under "Consumer Law"; three consumer complaints under "Corporate Law"; "Award by an Arbitral Tribunal" filed as a pleading. | Re-file under the correct area. Write a real Corporate Law (NCLT) set: s.241–242 oppression/mismanagement, IBC s.7/9 applications, s.252 restoration. |
| Pleadings intro promises | The intro promises Constitutional (writ), Energy Law, Arbitration (SoC/SoD) and NCLT drafts, but **no drafts follow**. | Content gap. Commission these drafts or remove the promises. |

### 3.2 Heading typos and style errors (fix in H1/H2 and slugs)
Documents: "Promisory Note" → Promissory; "Questionaire" → Questionnaire; "License to use Traemark" → Trademark; "Blank Vakalatmanama…" ×12 → Vakalatnama; "Deed or retirement" → Deed of retirement; "Article of association" → Articles of Association; "Agreement for under writing shares" → underwriting; "Import- Export" → Import-Export; "Purchase er" (requirements table); "Equal Favours" → "Equal favour"; "Sale the Goods" → "Sell the goods"; "collaboration makes as better" → "us"; "Reach to the consumers" → "Reach consumers"; "Sign of the Deal, now." → "Sign off". Leading or trailing spaces on "Legal", "Mergers and Acquisitions" and "Food Processing". Placeholder FAQs ("Educate on what is ?") and empty numbered template lists in 30+ upcoming sections.
Pleadings: "Defamantion"; "Consumet Protection Act"; "Adultry"; "apperance"; "Bailer" → Bailor; "Negotiable Instrument Act" → Instruments; "Complaint Under of The…"; "Section. 311 Cr.P.C.for"; "437CrPC"; "Court of Sessions Court"; "Child Custody-"; "OF CRPC"; ALL-CAPS "SAMPLE COMPLAINT PETITION" and "THE COMPLAINT"; inconsistent Title Case; stray `"​` (zero-width space) characters in 20 headings.
Start a Business: "Copy Right" → Copyright; "Protect you Intellectual Property" (TOC); "Private Limited Company (PLC)" (PLC normally means *public* limited company, so use "Pvt Ltd"); "Limited liability Partnership" casing. Compliance: escaped "\[ESOP\]".

---

## 4. Copied third-party content (must be rewritten, not edited)

Copied text exposes LawDocs to copyright claims (Copyright Act 1957, s.51) and passing-off. It also signals duplicate content to search engines, and Google's AI-optimisation guide ranks originality as the most influential long-term factor. **Treat every section listed below as "rewrite from scratch".** The web-search quota ran out during this stream, so exact-phrase checks of the remaining text (for example the JV and share-transfer FAQs in Documents) could not be completed. Run a full plagiarism scan (Copyscape, Quetext or Turnitin) over all four manuals before any copy is reused; the visible links are only the detectable tip.

| # | Manual > Section | Source / signal | Evidence (line) | Type |
|---|---|---|---|---|
| 1 | Compliance > Closure of Business (hub) | en.wikipedia.org | Wikified definition of "Business closure" (L614) | Linked text |
| 2 | Compliance > Closure of LLP | LegalWiz.in | FAQ "Whether LegalWiz.in will provide the stamp duty…" (L958) | Competitor brand in FAQ |
| 3 | Compliance > ITR Filing | Vakilsearch | "…consult Vakilsearch." (L1634) | Competitor brand |
| 4 | Compliance > TDS Return Filing | Corpbiz; Vakilsearch | "With Corpbiz, TDS Return filing becomes easy…" (L1792); "Vakilsearch's Google Calendar…" (L1936) | Competitor brands |
| 5 | Compliance > Professional Tax Registration | corpbiz.io | 4 FAQ headings hyperlinked to `corpbiz.io/professional-tax-registration#collapse…` (L2058–2104) | Scraped FAQ accordion |
| 6 | Compliance > Accounting (hub) | Provenience | "Provenience can help startups…" (L2116) | Competitor brand |
| 7 | Compliance > Accounting & Book-keeping | provenience.in | 11 FAQ headings hyperlinked to `provenience.in/bookkeeping-accounting-services/#collapse_n`; "We at Provenience" (L2292–2370) | Scraped FAQ accordion |
| 8 | Compliance > Payroll Maintenance | Vakilsearch | "How do I ensure my data remains confidential with Vakilsearch?" (L2502) | Competitor FAQ |
| 9 | Compliance > PF Registration | Vakilsearch | "…handled by the efficient team at Vakilsearch" (L2754) | Competitor brand |
| 10 | Compliance > Shops & Establishments | Vakilsearch | "At Vakilsearch, the processing of your online application…" ×3 (L3106) | Competitor brand |
| 11 | Compliance > Audit (hub) / Company Audit | Registrationwala | "Registrationwala's audit services can help…" (L3379) | Competitor brand |
| 12 | Compliance > 7 hub pages | Unattributed testimonials | "Customer experiences" (L120–140, repeated at L652, 1158, 1598, 2178, 2650, 3477). Quotes talk about "proposals", "cold call to closed deal", "reduced creation time by 700%", "web design agency": proposal-software testimonials with the brand name swapped in. | **Fabricated or adapted reviews** |
| 13 | Start > LLP | toppr.com | Two hyperlinks inside body text (L1133) | Linked text |
| 14 | Start > Nidhi Company | enterslice.com | "[NBFC](https://enterslice.com/nbfc-registration)" (L1261) | Competitor link |
| 15 | Start > Patent | LegalRaasta; upcounsel.com | "We, at LegalRaasta act as patent agent…" (L1417); 2 upcounsel links (L1521) | Competitor brand and US source |
| 16 | Start > Trademark | Wikipedia; ebizfiling | Wikipedia definition with 6 links (L1846); "IP experts at ebizfiling… info@ebizfiling.com" (L1880) | Linked text and competitor email |
| 17 | Start > FSSAI | legaldocs.co.in | FAQ hyperlinked to a legaldocs.co.in blog (L2380) | Scraped FAQ |
| 18 | Start > IEC | eximguru.com | DGFT link via eximguru (L2452) | Linked text |
| 19 | Start > Spices Board | Wikipedia | Spices Board definition (L3178) | Linked text |
| 20 | Start > Hallmark Certification | Wikipedia (17 links), Wiktionary (2), business-standard.com | Wikified definition; Business Standard topic link; outdated date (L3704–3804) | Linked text |
| 21 | Start > Agmark | dmi.gov.in | Official source (L3564). Acceptable as a citation, but rewrite the text. | Government source |

**Policy for the rebuild:** (a) No sentence goes from the manuals to the website without a rewrite and a plagiarism check. (b) Outbound links point only to primary sources: India Code, MCA, CBIC, CBDT, RBI, SEBI, BIS, FSSAI, DGFT, e-Courts. (c) Testimonials: publish only verified customer feedback, with consent records kept, in line with IS 19000:2022 (online consumer reviews) and the CCPA Guidelines on Misleading Advertisements 2022.

---

## 5. Outdated law references (cross-manual)

| Old reference (in manuals) | Current law / position | Where found | Rewrite instruction |
|---|---|---|---|
| CrPC 1973 | **Bharatiya Nagarik Suraksha Sanhita 2023 (BNSS)**, in force 1 Jul 2024 | Pleadings: 11 criminal and family drafts. Documents: Divorce, Maintenance (×10), Marriage, Senior Citizens, Bonds | Map sections: 125→**144**, 167(2)→**187**, 200→**223** (pre-cognizance hearing of accused), 205→228, 256→279, 311→348, 317→355, 320→359, 437→**480**, 438→**482**, 439→**483**. For proceedings pending before 1 Jul 2024, the BNSS s.531 savings clause applies. Show "(formerly CrPC s.x)" in brackets for search demand. |
| IPC 1860 | **Bharatiya Nyaya Sanhita 2023 (BNS)** | Pleadings: 9 drafts. Documents: Contracts, Domestic Violence (498A ×4), Dishonour of Cheques, Advertisements, Legal Notices | 498A→BNS **85/86**; 406→316; 420→318; 499/500→356; 506→351. Offences committed before 1 Jul 2024 remain under IPC. |
| Indian Evidence Act 1872 | **Bharatiya Sakshya Adhiniyam 2023 (BSA)** | Documents: Affidavits, Legal Notices, Student Affidavits, Power of Attorney | s.65B certificate → BSA **s.63**, with the new certificate format in the Schedule. |
| Consumer Protection Act 1986; "District Forum"; s.24-A | **CPA 2019** (in force 20 Jul 2020); District/State/National **Commissions**; limitation s.69 | Pleadings: Consumer ×1 plus Corporate Law ×3. Documents: Consumer, Banking & Finance, Advertisements | Pecuniary limits (2021 Rules): District ≤₹50 lakh; State ₹50 lakh–₹2 crore; National >₹2 crore. e-Daakhil filing. Product-liability chapter. |
| Companies Act 1956 (s.25, s.292) | Companies Act 2013 (s.8, s.179/180) | Documents: Banking & Finance, Clubs, Companies, Mortgage. Start: Section 8 | Replace citations; keep "formerly s.25" only as context. |
| Listing Agreement (BSE/NSE), Clause 49 | **SEBI (LODR) Regulations 2015** | Documents: Companies (2 templates), Secretarial | Retire the "Listing agreement BSE/NSE" templates. Replace them with LODR policy packs (Reg 23 RPT, Reg 30 materiality, Reg 46 website). |
| Udyog Aadhaar (UAM) | **Udyam Registration** (1 Jul 2020). Revised MSME limits from 1 Apr 2025: micro ₹2.5 cr investment/₹10 cr turnover; small ₹25 cr/₹100 cr; medium ₹125 cr/₹500 cr | Documents: MSME. Start: MSME Registration (×5) | Rewrite completely; remove the udyogaadhaar.gov.in link. |
| GSTR-2 / GSTR-3 matching | Suspended since 2017. The current regime is GSTR-1/1A, 3B, 2B and the **Invoice Management System** (from Oct 2024) | Compliance: GST Return Filing | Rewrite the procedure. Add GST 2.0 rate rationalisation (5%/18%/40%, effective 22 Sep 2025). |
| GST audit u/s 35(5) and CA-certified GSTR-9C | s.35(5) omitted w.e.f. 1 Aug 2021. GSTR-9C is now self-certified | Compliance: GST Audit (21 refs), Audit hub | Re-scope the page as "GST Annual Return & Reconciliation (GSTR-9/9C)" plus departmental audit (s.65) support. |
| Income-tax Act 1961; "assessment year"; s.44AB, 12A/80G | **Income-tax Act 2025** (in force 1 Apr 2026; Income-tax Rules 2026 notified 20 Mar 2026). It introduces "tax year" and renumbers sections | Compliance: ITR, TDS, Tax Audit, Accounting. Documents: M&A, Partnership, Partition. Start: Section 8, Trust, Society | Dual-cite during transition (returns for FY 2025-26 still run under the 1961 Act). Tax-audit threshold: ₹1 crore → ₹10 crore where cash ≤5%; professionals ₹50 lakh unchanged. Verify new section numbers against the official Act text. |
| Payment of Wages, Minimum Wages, Bonus, ESI Act, EPF/Gratuity, Industrial Disputes, Factories, Contract Labour, Standing Orders | **Four Labour Codes** in force 21 Nov 2025 (Wages 2019; IR 2020; SS 2020; OSH 2020). The old rules continue on a transitional basis until Code rules are notified | Compliance: Labour hub, PF, ESI, Payroll, S&E. Documents: Labour Agreements, Hotel & Tourism | Cite the Codes; note that state S&E Acts continue; add the "wages" definition (50% rule) and fixed-term employment. |
| Hallmarking "mandatory from 15 Jan 2020 at one go" | Mandatory from **16 Jun 2021** in phased districts; HUID-only from 1 Apr 2023 | Start: Hallmark | Rewrite. |
| Nidhi (pre-2022) | Nidhi (Amendment) Rules 2022: NDH-4 declaration and approval before accepting deposits | Start: Nidhi | Update the procedure. |
| OPC restrictions (pre-2021) | 2021 liberalisation: NRIs allowed; residency 120 days; no mandatory conversion threshold | Start: OPC | Update. |
| Mutual-consent 6-month wait as fixed | Waivable (Amardeep Singh v Harveen Kaur, 2017); SC Art.142 power (Shilpa Sailesh, 2023) | Documents: Divorce. Pleadings: mutual consent ×3 | Add "waiver of cooling-off" application. |
| Specific Relief Act pre-2018 | SRA (Amendment) 2018: specific performance is the rule (s.10) | Pleadings: Written Statement, Specific Performance; Documents: Contracts | Update the grounds and prayers. |
| Money suits without pre-litigation mediation | Commercial Courts Act s.12A mandatory pre-institution mediation (Patil Automation, 2022) | Pleadings: Money Recovery ×6 | Add a s.12A compliance paragraph and Order XXXVII variant. |
| Adoption by court order (if referenced) | JJ (Amendment) Act 2021 and Adoption Regulations 2022: District Magistrate issues orders (CARA). HAMA deeds remain valid | Documents: Adoption | Distinguish the HAMA deed from the JJ Act route. |
| Data protection (IT Act s.43A/SPDI) | **DPDP Act 2023 and DPDP Rules 2025** (notified 13 Nov 2025; core duties from 13 May 2027) | Documents: Website Policies, Privacy & Cookie Policy, Cyber Security (upcoming) | Build DPDP-aligned privacy notice and DPA templates. |
| eSign on every document | **IT Act s.1(4) and First Schedule**: e-signature is not valid for negotiable instruments other than cheques, powers of attorney, trusts, wills and contracts for sale/conveyance of immovable property | Documents: POA, Will, Trusts, Sale & Purchase, Promissory Note, Gift (immovable) | Product rule: show "eSign not legally valid; print-sign-stamp-register workflow" on these pages. |

Section 138 NI Act formats remain valid. Note that High Courts have considered whether the BNSS s.223 pre-cognizance hearing applies to cheque complaints, so verify the current position in each state.

---

## 6. Brand voice and one-liner bank

### 6.1 The owner's voice (from 131 Documents one-liners plus 48 service one-liners)

| Trait | Evidence from manuals | Keep / fix |
|---|---|---|
| **Ultra-short, full-stop rhythm** (2–6 words) | "Team up." · "Take care." · "Strike off." · "Pay. Save." · "File. Smile." | Keep. This is the signature. |
| **Triads of verbs** | "Create. Negotiate. Associate." · "Calculate. Integrate. Regulate." · "Execute. Intimate. Comply." · "Agree. Accept. Acknowledge." · "Create. Maintain. Preserve." | Keep. Avoid repeating "Negotiate. Associate." |
| **Puns and double meanings** | "Cheque. Check. Checkmate." · "Trade a Mark. Trade with Mark." · "Get the Trust." · "Raise a bar." (barcode) · "Get trusted" · "Host the guest." (FSSAI) · "Rent happiness." · "Lease with ease." | Keep. Strongest lines. |
| **Law plus human value** | "Gift with Love and Law." · "Write your family story, in legal language." · "Seniority at priority." · "Divide with Rules." | Keep. Ideal for the personal categories. |
| **"…, legally." kicker** | "Maintain your life, legally." · "Release it legally." · "Take a Pledge. Legally." · "Bounce back. Legally." | Use sparingly (it currently appears in more than 12 lines). |
| **Neutrality promise** | "Neutral drafts. Equal Favours." · "Drafts that don't take sides." | Make it a brand pillar ("Neutral by design"). Fix the grammar. |
| **Humour and edge** | "Write everything except love-letters." · "Get out of the trouble. Or say it, 'Get out'." · "Fold your business and double the money." | Review case by case. "Fold" means *close down*, so the M&A line misfires. The divorce line is risky in a sensitive category. |
| **CTA formula "[Verb] [object], now."** | "Collaborate now." · "Proceed for Custody, now." · "Note a Promise, now." (58 variants) | Keep the formula. Standardise the comma ("Draft it, now."). |
| **Borrowed lines (originality risk)** | "Conflict is inevitable, but combat is optional." (widely attributed to Max Lucado) · "Competition makes us faster, collaboration makes us better." (circulating quote) · "Win the workplace to win the marketplace." (close to Doug Conant) · "do or do not, there is no try" (Yoda, *Star Wars*) | Replace or attribute them. Short phrases are rarely protected by copyright, but they weaken originality and Yoda is a trademark-sensitive franchise. |
| **Grammar slips** | "Sale the Goods." · "Equal Favours." · "Reach to the consumers" · "collaboration makes as better" · "Add salt to your business" (Spices Board) | Fix them all. |
| **Body copy vs taglines** | The taglines are crisp, but the body copy is generic, third-person, and partly copied. | Rewrite the body in the same voice: second person, short sentences, one idea per line. |

**Voice in one sentence:** *LawDocs talks like a sharp senior associate who is also good with puns. It says the legal point in three words, adds a human reason, and ends with an action.*

**Comparable taglines (inspiration only, not copied):** LegalZoom, "Legal solutions trusted by millions, designed for you"; Rocket Lawyer, "Legal protection on your terms"; Docusign, "AI-powered agreement management"; Vakilsearch, "Expert lawyer + CA + CS in your pocket!"; LegalKart, "Trusted lawyers. Instant access. 24×7." The competitors sell **trust and scale**. LawDocs should sell **wit, brevity and neutrality**, with each line paired with one verifiable proof point (documents drafted, signatures executed, professionals empanelled).

### 6.2 New one-liner bank (82 lines, original, in the owner's voice)

| # | Page / category | One-liner | CTA ("…, now.") |
|---|---|---|---|
| 1 | Homepage hero | Draft it. Sign it. Keep it. | Start a document, now. |
| 2 | Homepage sub | Your agreements, in your pocket. For life. | Open your locker, now. |
| 3 | Brand pillar | Neutral by design. Fair by default. | — |
| 4 | Brand pillar | Paperwork, minus the paper. | — |
| 5 | Aadhaar eSign | One OTP. One binding deal. | eSign, now. |
| 6 | eSign | Signed in seconds. Valid for years. | — |
| 7 | Vidhi AI | Ask Vidhi. Then decide. | Ask, now. |
| 8 | Vidhi AI | First draft free. Final word yours. | Draft free, now. |
| 9 | Vidhi AI | Speak your terms. Vidhi writes them. | — |
| 10 | Vidhi + expert | AI drafts. Experts check. You sign. | — |
| 11 | Hire a professional | Expert eyes. Fixed price. | Hire a pro, now. |
| 12 | Hire a professional | A lawyer when it matters. Not before. | — |
| 13 | DMS / locker | Store once. Find forever. | — |
| 14 | DMS | Every deed, one drawer. | — |
| 15 | Data export | Leave anytime. Take everything. | — |
| 16 | Deals & Agreements | Deal fair. Draft fairer. | Strike the deal, now. |
| 17 | Contracts | Terms first. Trust follows. | — |
| 18 | Collaboration / JV | Two logos. One rulebook. | Partner up, now. |
| 19 | Statement of Work | Scope it. Then ship it. | — |
| 20 | Family Matters | Settle hearts. Then settle papers. | — |
| 21 | Marriage | Two families. One record. | Register, now. |
| 22 | Divorce (mutual) | Part ways. Keep the peace. | — |
| 23 | Child custody | The child first. Always. | — |
| 24 | Senior citizens | Respect, with remedies. | — |
| 25 | Financial Transactions | Money talks. Paper proves. | — |
| 26 | Loans / bonds | Lend with proof. Borrow with clarity. | — |
| 27 | Receipts | Every rupee, on record. | — |
| 28 | Guarantee / indemnity | Promise the risk. Price the risk. | — |
| 29 | Hire-purchase | Use it now. Own it later. | — |
| 30 | Operations & Management | Run the firm by the book. Literally. | — |
| 31 | Companies | Board-ready. Auditor-ready. | — |
| 32 | Partnership | Shake hands. Then sign hands. | — |
| 33 | Trusts | Give with purpose. Govern with rules. | — |
| 34 | Planning / start-up | Idea today. Entity tomorrow. | Plan it, now. |
| 35 | Founders | Founders agree first. Investors follow. | — |
| 36 | Funding | Raise money. Not disputes. | — |
| 37 | Marketing & Sales | Promise in ads. Prove in contracts. | — |
| 38 | Invoices | Bill right. Get paid. | — |
| 39 | Industries | Your industry. Your clauses. | — |
| 40 | IPR hub | Own the idea. Officially. | — |
| 41 | Copyright | Create. Register. Royalty. | — |
| 42 | Trademark registration | Your brand. Nobody else's. | File, now. |
| 43 | Trademark tracker | Filed. Tracked. Registered. | Track, now. |
| 44 | Patent | Invent once. Earn often. | — |
| 45 | IT & Websites | Code ships. Contracts protect. | — |
| 46 | Website policies | Collect data. Not liability. | — |
| 47 | Cookie / privacy | Consent, clearly. | — |
| 48 | HR & Service | Hire on paper. Part by the book. | — |
| 49 | Offer letters | Offer clearly. Retain gladly. | — |
| 50 | Labour agreements | Fair wage. Firm terms. | — |
| 51 | Work from home | Remote work. Real terms. | — |
| 52 | Legal notices | Say it once. Say it in a notice. | Send the notice, now. |
| 53 | Reply to notice | Answer back. On record. | — |
| 54 | Affidavits | Swear by it. Properly. | — |
| 55 | RTI | Ask the State. In writing. | — |
| 56 | Consumer | Paid for it? Claim for it. | — |
| 57 | Mediation / Equator | Talk it out. Sign it off. | — |
| 58 | Arbitration | Private forum. Binding award. | — |
| 59 | Property hub | Own the land. Own the papers. | — |
| 60 | Building contracts | Brick by brick. Clause by clause. | — |
| 61 | Rent | Rent right. Live light. | — |
| 62 | Sale & purchase | Buy the house. Not the dispute. | — |
| 63 | RERA (buyers) | Booked a flat? Book your rights. | — |
| 64 | RERA (builders) | Register first. Sell faster. | — |
| 65 | Secretarial | Minutes that matter. | — |
| 66 | Resolutions | Resolve. Record. Report. | — |
| 67 | NBFC / RBI compliance | RBI-ready, every quarter. | — |
| 68 | Students | Paperwork done. Back to books. | — |
| 69 | Succession hub | Pass the legacy, not the litigation. | — |
| 70 | Will | Your wishes. Your words. Your Will. | — |
| 71 | Power of attorney | Hand over power. Not control. | — |
| 72 | Pleadings hub | Your case, in the court's language. | Draft the plaint, now. |
| 73 | Criminal pleadings | Liberty deserves good drafting. | — |
| 74 | Civil suits | Plead it right the first time. | — |
| 75 | Compliance hub | Comply quietly. Grow loudly. | — |
| 76 | Compliance calendar | Due dates, never overdue. | — |
| 77 | GST / tax | File on time. Sleep on time. | — |
| 78 | Closure | Close the books. Close the chapter. | — |
| 79 | Start a Business | Register today. Rule tomorrow. | Incorporate, now. |
| 80 | Licences / quality marks | Licensed to grow. Certified to be trusted. | — |
| 81 | NGO / Section 8 | Do good. Register well. | — |
| 82 | Litigation tracker | Every hearing, on your radar. | — |

Additional lines for the new verticals in the brief: **Marketplace**, "Pick a pro. Pay per job."; **Retainership**, "A legal team on retainer. Not on payroll."; **FinLegal Academy**, "Practise before you practise."; **Loan/insurance grievances**, "Rejected? Not the final word."; **Challans**, "Challan today. Cleared today."; **Vehicle sale**, "Sell the car. Keep the proof."; **Savings page**, "Hours saved. Penalties avoided. Counted."

---

## 7. SEO / GEO page templates

### 7.1 Current Google position (verified 25 Oct 2026)

| Topic | Position | Implication for LawDocs |
|---|---|---|
| FAQ rich results | Limited to well-known authoritative government and health sites in Aug 2023. **Deprecated and no longer shown from 7 May 2026.** Documentation removed 15 Jun 2026. | FAQs no longer produce SERP rich results. Keep **visible** FAQs: they answer People Also Ask style queries and help retrieval by AI engines (Google AI Overviews and AI Mode use normal indexing; ChatGPT Search, Perplexity, Copilot and Claude read page text). FAQPage JSON-LD is optional. Emit it from the CMS only if it costs nothing, and never mark up FAQs that are not visible on the page. |
| HowTo | Rich result deprecated in 2023 (desktop-only, then removed). | Use plain ordered lists for process steps. No HowTo markup. |
| AI Overviews / AI Mode | "No additional requirements… nor other special optimizations." Pages must be indexed and snippet-eligible. Originality is the most influential long-term factor. Avoid scaled content. JavaScript sites need JS-SEO care. | **SSR or SSG is mandatory.** Do not create 36 state clones of each of 330 documents; that is the scaled-content-abuse pattern. |
| llms.txt | Google, 15 Jun 2026: llms.txt files "aren't needed for Google Search (and won't negatively or positively impact your visibility)". | Optional. Publish a short `/llms.txt` (sections, top hubs, policies, contact) for third-party LLM tools. Low cost, no Google benefit. |
| Structured data generally | Not required for AI features. Still useful for eligible rich results. Must match visible content. | Use Organization, WebSite, BreadcrumbList, Article/BlogPosting, VideoObject, ProfilePage and Product/Offer (real prices only). Use Service and LegalService for entity clarity. |
| Reviews | Self-serving reviews for an Organization or LocalBusiness are not eligible for star snippets. A 24 Jul 2026 guideline bars fake or undisclosed incentivised reviews. | Show testimonials as plain text with no star markup. Use verified customers only. |
| Search generative AI control | Documented 21 Oct 2026 under "Control what you share". | Keep LawDocs opted in to generative AI features, and decide separately on `Google-Extended` (training and grounding outside Search). |

### 7.2 Document page template (e.g., `/documents/property-transactions/rent/rent-agreement-residential`)

| # | Block | Specification |
|---|---|---|
| 1 | Breadcrumb | Home › Documents › Property Transactions › Rent › Residential Rent Agreement (BreadcrumbList). |
| 2 | **H1** | "Residential Rent Agreement — Draft Free with AI, eSign Online". Pattern: `[Document name] — [primary action]`. One H1 only. Title tag ≤60 chars. Meta description ≤155 chars and unique for each URL. |
| 3 | Owner one-liner | "Rent right. Live light." Shown as a styled eyebrow above the H1 in the design; it is not the H1. |
| 4 | **Answer-first summary** (40–60 words) | Entity-rich definition: "A residential rent agreement is a contract under the Transfer of Property Act 1882 (s.105) and the applicable state rent law in which a landlord lets a home to a tenant for rent. Agreements over 11 months generally need stamping and registration (Registration Act 1908, s.17)." |
| 5 | **Key facts box** | Governing law · Stamp duty (by state, see block 11) · Registration required? · Witnesses · **eSign valid? (Yes / No: IT Act First Schedule)** · Typical time · Last legal update. |
| 6 | **"Draft free with Vidhi AI"** (above the fold on mobile) | 5–8 question wizard (parties, property, rent, deposit, term, lock-in, escalation, notice). Output: editable DOCX/PDF preview, clause explanations behind the "i" button, multilingual output. Disclaimer: "Vidhi is an AI drafting assistant, not a lawyer; review recommended." Free draft, with paid unlocks (no watermark, eStamp, eSign, locker). |
| 7 | **"Hire a professional"** | 2–3 fixed-price tiers (Review ₹X · Draft & review ₹Y · Draft, stamp & register assistance ₹Z), with turnaround time, professional type (advocate/CS/CA) and SLA eSigned inside the tool. Display professionals as a platform-assigned service; do not advertise individual advocates (BCI Rule 36 prohibits solicitation). |
| 8 | What's included | Clause list (8–15 bullets) with one-line purposes. Covers neutral and both-party protections ("Neutral by design"). |
| 9 | **Requirements table** | Built from the manual's requirement tables: documents and information needed per party (ID, PAN, address proof, photographs, property papers, board resolution/POA for companies). |
| 10 | Process steps | Ordered list: Draft → Negotiate (track changes, in-app chat) → eStamp → eSign/print → Register (if needed) → Store in locker → Reminders (renewal, rent escalation). |
| 11 | **State variations** | Table of stamp duty, registration fee and e-stamping availability for the top 10 states, plus a "your state" selector. Each row shows a source link (state IGR/stamp portal) and a "verified on" date. Create separate state pages only where the law materially differs (for example, Maharashtra leave and licence). |
| 12 | Stamp and registration note | Plain-language consequences of under-stamping (inadmissible as evidence until duty and penalty are paid) and of non-registration. |
| 13 | **FAQs** (5–8) | Real user questions (from Vidhi chat logs, Search Console, PAA). Each answer is ≤60 words, leads with the answer, cites a section, and links to the canonical page. Visible HTML. JSON-LD optional (no Google rich result). |
| 14 | Related | 4–6 related documents, the matching pleading (e.g., eviction suit), the matching service (registration assistance), one guide or blog post, one video. |
| 15 | Testimonials (no photos) | First name + initial, city, role ("tenant, Jaipur"), date, "verified user" tag, 1–2 sentences. Plain text, no star markup. Consent stored. |
| 16 | **E-E-A-T footer** | "Reviewed by [Name], Advocate (Enrolment No. D/xxxx/20xx) / ACS [No.]; last reviewed [date]; next review [date]". Change log. "Legal basis" list linking to India Code sections. Author ProfilePage for each reviewer. |
| 17 | Disclaimer and grievance | "Information, not legal advice"; Grievance Officer link (IT Rules 2021); DPDP privacy notice link. |

**Hard rules:** one canonical URL per document; SSR HTML contains all copy and links; no infinite filter URLs indexed; images carry alt text; core content is not loaded behind tabs that only render on click; page passes Core Web Vitals on mobile (LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1); WCAG 2.2 AA.

### 7.3 Other templates

| Page type | Required blocks (in order) |
|---|---|
| **Category hub** (`/documents/property-transactions`) | H1 "Property Documents & Agreements"; one-liner; 60–80-word definition of the category; sub-category grid (one-liner + 1-line description each); "Most used" top-8 documents; Vidhi prompt box ("Describe your situation"); "Hire a professional" strip; 4–6 hub FAQs; guides and videos; related services; reviewed-by footer. CollectionPage + BreadcrumbList. |
| **Sub-category hub** (`…/rent`) | H1; one-liner; answer-first explainer (150–300 words, original); document list with a 1-line "use this when…" for each; requirements table (if any); comparison table (e.g., rent vs leave and licence vs lease); FAQs; related pleadings and services. |
| **Pleading page** (`/pleadings/criminal/anticipatory-bail-application`) | H1 "Anticipatory Bail Application under Section 482 BNSS (formerly s.438 CrPC)"; answer-first summary; key facts (court, statute, limitation, court fee, annexures, e-filing portal); Vidhi "prepare first draft"; **"File through an advocate"** CTA (pleadings must be signed and verified by the party and filed by an advocate); variant toggles (forum, offence, state); draft preview (partial, gated); checklist of annexures; old→new section mapping box; FAQs; related documents (vakalatnama, affidavit, surety); litigation-tracker CTA; reviewed-by. |
| **Service page** (`/start-a-business/incorporate-your-business/private-limited-company`) | H1 "Private Limited Company Registration Online"; one-liner; answer-first summary; price card (government fee vs professional fee vs GST, shown separately); timeline; eligibility; benefits; documents required; process (SPICe+ steps); post-incorporation compliance calendar; comparison (Pvt Ltd vs LLP vs OPC); FAQs; the matching document packs (MoA/AoA, founders' agreement); reviewed-by (CS). Service + Offer + BreadcrumbList. |
| **Professional profile** (marketplace) | ProfilePage + Person: credentials, enrolment or membership number (verifiable), practice areas, languages, cities, services offered at platform prices. No "best lawyer" claims. |
| **Blog / guide** | Article or BlogPosting with an author ProfilePage; answer-first opening; dated updates; citations; "Related documents" block. |
| **Vlog** | YouTube embed + VideoObject (name, description, thumbnailUrl, uploadDate, duration, `creator`), with the transcript on the page. |
| **Office / contact** | Organization (sitewide) + LegalService (LocalBusiness subtype) per real office (Delhi, Noida, Jaipur) with NAP that matches the Google Business Profile. One public phone number. |

### 7.4 GEO / LLM-readiness checklist

1. **Rendering:** SSR/SSG for every indexable route. Test with a no-JS fetch, and confirm each URL returns a unique title, meta description, H1 and body.
2. **Host hygiene:** choose `https://www.lawdocs.in`, 301 all non-www traffic to it, and make the sitemap, canonical tags and hreflang use the same host. Keep a real `lastmod`.
3. **Definitions first:** the first sentence of every page states *what it is + which law + who uses it*. Use consistent entity names ("LawDocs", "Vidhi AI", "Infrabyx Group", "FinLegal Academy", "Equator") across the site, schema `sameAs` and social profiles.
4. **Non-commodity content:** add practice notes from the in-house team ("What we see go wrong in rent agreements"), anonymised platform statistics, original state-wise stamp-duty matrices, and old→new law maps. These are the assets AI engines cite.
5. **Citations:** link to India Code, RBI, SEBI, MCA, CBIC/CBDT and e-Courts. Add "verified on" dates.
6. **Structure:** use semantic HTML (h2/h3, tables, ordered lists), concise paragraphs, and a self-contained answer under each H2.
7. **Crawler policy:** allow Googlebot and Bingbot. Decide explicitly on OAI-SearchBot/GPTBot, PerplexityBot, ClaudeBot/Claude-SearchBot and Google-Extended (recommend allowing the search-retrieval bots and deciding training bots at board level). Submit sitemaps and use IndexNow for Bing.
8. **llms.txt:** a short markdown index of the section landings, top 50 hubs, pricing, policies and contact. Treat it as optional and not a ranking lever.
9. **Measurement:** Search Console (including the generative AI performance report), Bing Webmaster, and log-file analysis of AI-bot hits.
10. **Governance:** a CMS workflow with draft → legal review → publish; a mandatory "reviewed by" field; automatic noindex for pages without a reviewer; and quarterly law-change sweeps (RBI master directions, Codes rules, Income-tax Act 2025 rules).

---

## 8. Complete manual-derived page inventory

**Legend:** L = live sub-category; U = "(upcoming)" in the manual or inside an upcoming category. Body words = words in the section, including FAQs and tables ("stub" ≤150 words, "empty" ≤20). FAQs = count of real FAQ entries; placeholder "Educate on what is ?" entries are excluded. Req. table = the section contains a document-requirements table. Document pages = template list as it appears in the manual, and each item becomes a leaf at `…/{sub-category}/{document-slug}`. "—" = none listed, so the documents still need to be defined. Typos are corrected in the slugs.

### 8.1 Documents manual — section landing `/documents` · 18 category hubs · 134 sub-category hubs · 347 template entries (330 unique)

The leaf-level list of all **347 document entries** has its own file: `/home/claude/ldpack/pack/_research/R5_Document_Page_Inventory.csv`. For each entry it gives the id, category, sub-category, document name, proposed URL, canonical/duplicate status (330 canonical, 17 duplicates) and an **eSign-validity flag**: 250 valid for Aadhaar eSign; 62 "check" (interest in immovable property or stamping); 35 not valid under IT Act s.1(4) and the First Schedule (wills, POAs, trusts, promissory notes, agreements for sale or conveyance of immovable property, mortgages). The Documents table below gives the number of document pages per sub-category hub.

**D1. Deals & Agreements** — category hub `/documents/deals-and-agreements`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D1.1 | Collaboration and Joint Venture | `/documents/deals-and-agreements/collaboration-and-joint-venture` | L | 1545 | Team up. / Neutral drafts. Equal Favours. | 14 | Y | 5 |
| D1.2 | Contracts and Agreements | `/documents/deals-and-agreements/contracts-and-agreements` | L | 2091 | Agree with the terms when you actually are. / Take care. | 7 | Y | 7 |
| D1.3 | Distributorship & Agencies | `/documents/deals-and-agreements/distributorship-and-agencies` | L | 1165 | Created in minutes. Approved in seconds. / Create with ease, terminate with peace. / Legitimate. Facilitate. Accelerate. | 10 | Y | 10 |
| D1.4 | Franchise and License | `/documents/deals-and-agreements/franchise-and-license` | L | 1183 | Evolve, enhance your business. / Created in minutes. Approved in seconds. / Create with ease, terminate with peace. / Legitimate. Facilitate. Accelerate. | 10 | Y | 10 |
| D1.5 | Mergers and Acquisitions | `/documents/deals-and-agreements/mergers-and-acquisitions` | L | 1541 | Fold your business and double the money. / Calculate. Integrate. Regulate. | 10 | Y | 3 |
| D1.6 | Formal Proposals | `/documents/deals-and-agreements/formal-proposals` | L | 435 | Propose to win. | 5 | — | 0 (to define) |
| D1.7 | Quotes | `/documents/deals-and-agreements/quotes` | L | 407 | Quote like a quotation. | 4 | — | 1 |
| D1.8 | Statement of Work | `/documents/deals-and-agreements/statement-of-work` | L | 478 | Define & decide the Scope of Work. | 5 | — | 4 |
| D1.9 | Shipping agreements (upcoming) | `/documents/deals-and-agreements/shipping-agreements` | U | 409 | — | 4 | Y | 0 (to define) |
| D1.10 | Sign off | `/documents/deals-and-agreements/sign-off` | L | 1048 | Create, negotiate & Sign off. | 9 | — | 0 (to define) |

**D2. Family Matters** — category hub `/documents/family-matters`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D2.1 | Child Custody | `/documents/family-matters/child-custody` | L | 2461 | Take the custody, yourself. | 14 | — | 2 |
| D2.2 | Divorce | `/documents/family-matters/divorce` | L | 4287 | Get out of the trouble. Or say it, 'Get out'. | 37 | — | 7 |
| D2.3 | Domestic Violence | `/documents/family-matters/domestic-violence` | L | 1822 | Raise your voice through writing. | 10 | — | 3 |
| D2.4 | Maintenance | `/documents/family-matters/maintenance` | L | 3328 | Maintain your life, legally. | 14 | — | 6 |
| D2.5 | Marriage | `/documents/family-matters/marriage` | L | 1260 | Write everything except love-letters. | 5 | — | 1 |
| D2.6 | Mutual Divorce (upcoming) | `/documents/family-matters/mutual-divorce` | U | 45 (stub) | Get separated peacefully. | 0 | — | 0 (to define) |
| D2.7 | Senior Citizens Protection | `/documents/family-matters/senior-citizens-protection` | L | 1505 | Seniority at priority. | 10 | — | 0 (to define) |

**D3. Financial Transactions** — category hub `/documents/financial-transactions`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D3.1 | Acknowledgement | `/documents/financial-transactions/acknowledgement` | L | 456 | Agree. Accept. Acknowledge. | 4 | — | 6 |
| D3.2 | Banking and Finance | `/documents/financial-transactions/banking-and-finance` | L | 2934 | Communicate with Bank in writing. | 13 | — | 3 |
| D3.3 | Bonds | `/documents/financial-transactions/bonds` | L | 1147 | Bond with the force of law. | 9 | Y | 6 |
| D3.4 | Compromise | `/documents/financial-transactions/compromise` | L | 383 | Take mature decision. Compromise. | 4 | Y | 3 |
| D3.5 | Dishonour of Cheques | `/documents/financial-transactions/dishonour-of-cheques` | L | 1642 | Cheque. Check. Checkmate. | 9 | — | 1 |
| D3.6 | Hire-Purchase | `/documents/financial-transactions/hire-purchase` | L | 1285 | Hire-Purchase. Anything with ease. | 4 | Y | 6 |
| D3.7 | Hypothecation and Pledge | `/documents/financial-transactions/hypothecation-and-pledge` | L | 578 | Take a Pledge. Legally. | 5 | Y | 5 |
| D3.8 | Indemnity and Guarantee | `/documents/financial-transactions/indemnity-and-guarantee` | L | 586 | Indemnification from risks. Guaranteed. | 4 | Y | 7 |
| D3.9 | Insurance | `/documents/financial-transactions/insurance` | L | 2020 | Take, claim and process Insurance. / It works when prayers fail. | 9 | — | 2 |
| D3.10 | Promisory Note | `/documents/financial-transactions/promissory-note` | L | 622 | Make a Promise. Fill, fulfil. | 5 | — | 4 |
| D3.11 | Receipts | `/documents/financial-transactions/receipts` | L | 1490 | Send receipt. Receive credibility. | 10 | Y | 4 |
| D3.12 | Release Deeds | `/documents/financial-transactions/release-deeds` | L | 923 | Release it legally. | 4 | Y | 4 |
| D3.13 | Sale of Goods | `/documents/financial-transactions/sale-of-goods` | L | 2135 | Sale the Goods. Receive the dues. | 11 | Y | 5 |

**D4. Operations & Management** — category hub `/documents/operations-and-management`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D4.1 | Clubs and Societies | `/documents/operations-and-management/clubs-and-societies` | L | 628 | Manage your Club or Society, as per rules. | 6 | — | 6 |
| D4.2 | Companies | `/documents/operations-and-management/companies` | L | 1458 | Run your company. Professionally. Legally. | 16 | Y | 13 |
| D4.3 | Limited Liability Partnership | `/documents/operations-and-management/limited-liability-partnership` | L | 496 | Partner for limited liability, unlimited scope. | 3 | Y | 4 |
| D4.4 | MSME | `/documents/operations-and-management/msme` | L | 493 | Make a firm basis to grow big. | 6 | Y | 0 (to define) |
| D4.5 | Office Management (upcoming) | `/documents/operations-and-management/office-management` | U | 47 (stub) | Run your office professionally. | 0 | — | 0 (to define) |
| D4.6 | Partnership Firm | `/documents/operations-and-management/partnership-firm` | L | 871 | Build your partnership, on firm foundation. | 7 | Y | 11 |
| D4.7 | Proprietorship | `/documents/operations-and-management/proprietorship` | L | 468 | Manage your business & paperwork, yourself. | 3 | Y | 3 |
| D4.8 | Trusts and Wakfs | `/documents/operations-and-management/trusts-and-wakfs` | L | 3628 | Get the Trust. | 14 | Y | 6 |

**D5. Planning & Execution** — category hub `/documents/planning-and-execution`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D5.1 | Start-up (upcoming) | `/documents/planning-and-execution/start-up` | U | 46 (stub) | Plan & start running. | 0 | — | 0 (to define) |
| D5.2 | Budgeting (upcoming) | `/documents/planning-and-execution/budgeting` | U | 46 (stub) | Plan your business finances. | 0 | — | 0 (to define) |
| D5.3 | Partnership and Founders | `/documents/planning-and-execution/partnership-and-founders` | L | 1504 | Drafts that don't take sides. / Collaborate. Negotiate. Associate. | 6 | Y | 5 |
| D5.4 | Investment Support and Business Funding (upcoming) | `/documents/planning-and-execution/investment-support-and-business-funding` | U | 515 | Infuse blood in your business. Escalate. / Start, raise and grow faster. | 7 | Y | 3 |
| D5.5 | Business Plan (upcoming) | `/documents/planning-and-execution/business-plan` | U | 54 (stub) | Create business plan. | 0 | — | 0 (to define) |
| D5.6 | Business Process (upcoming) | `/documents/planning-and-execution/business-process` | U | 50 (stub) | Use professional processes. | 0 | — | 0 (to define) |
| D5.7 | Business Analysis (upcoming) | `/documents/planning-and-execution/business-analysis` | U | 42 (stub) | Analyse, evaluate & make it better. | 0 | — | 0 (to define) |
| D5.8 | Strategy (upcoming) | `/documents/planning-and-execution/strategy` | U | 52 (stub) | Prepare a winning strategy. | 0 | — | 0 (to define) |

**D6. Marketing & Sales** — category hub `/documents/marketing-and-sales`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D6.1 | Advertisements and Media | `/documents/marketing-and-sales/advertisements-and-media` | L | 1927 | Advertise, expand & market with clarity. | 15 | Y | 2 |
| D6.2 | Marketing (upcoming) | `/documents/marketing-and-sales/marketing` | U | 46 (stub) | Go to the market. Sell. | 0 | — | 0 (to define) |
| D6.3 | Email and Newsletters (upcoming) | `/documents/marketing-and-sales/email-and-newsletters` | U | 44 (stub) | Reach to the consumers | 0 | — | 0 (to define) |
| D6.4 | Sales (upcoming) | `/documents/marketing-and-sales/sales` | U | 47 (stub) | Sell for guaranteed payment. | 0 | — | 0 (to define) |
| D6.5 | Invoice (upcoming) | `/documents/marketing-and-sales/invoice` | U | 45 (stub) | Prepare receipts. Sign, store, share. | 0 | — | 0 (to define) |
| D6.6 | Business Letters (upcoming) | `/documents/marketing-and-sales/business-letters` | U | 48 (stub) | Communicate professionally. | 0 | — | 0 (to define) |
| D6.7 | Tracker Sheets (upcoming) | `/documents/marketing-and-sales/tracker-sheets` | U | 49 (stub) | Track performance & then decide. | 0 | — | 0 (to define) |
| D6.8 | Feedback Forms (upcoming) | `/documents/marketing-and-sales/feedback-forms` | U | 44 (stub) | Get the feedback. | 0 | — | 0 (to define) |
| D6.9 | Questionaire (upcoming) | `/documents/marketing-and-sales/questionnaire` | U | 40 (stub) | Get answers. | 0 | — | 0 (to define) |

**D7. Industries (upcoming)** — category hub `/documents/industries`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D7.1 | Construction | `/documents/industries/construction` | U | 70 (stub) | — | 0 | Y | 0 (to define) |
| D7.2 | Education | `/documents/industries/education` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D7.3 | Electricity and Power Sector | `/documents/industries/electricity-and-power-sector` | U | 15 (empty) | — | 0 | — | 0 (to define) |
| D7.4 | Food Processing | `/documents/industries/food-processing` | U | 66 (stub) | — | 0 | Y | 0 (to define) |
| D7.5 | Healthcare and Pharma | `/documents/industries/healthcare-and-pharma` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D7.6 | Hotel and Tourism | `/documents/industries/hotel-and-tourism` | U | 1955 | — | 8 | Y | 5 |
| D7.7 | Import- Export and Customs | `/documents/industries/import-export-and-customs` | U | 63 (stub) | — | 0 | Y | 0 (to define) |
| D7.8 | Media and Entertainment | `/documents/industries/media-and-entertainment` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D7.9 | Oil and Gas | `/documents/industries/oil-and-gas` | U | 17 (empty) | — | 0 | — | 0 (to define) |

**D8. Intellectual Property Rights** — category hub `/documents/intellectual-property-rights`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D8.1 | Copyright | `/documents/intellectual-property-rights/copyright` | L | 1524 | Write your Copy. Earn from Right. | 7 | Y | 5 |
| D8.2 | Patents | `/documents/intellectual-property-rights/patents` | L | 1921 | Protect your innovation. Manage & Earn. | 13 | Y | 3 |
| D8.3 | Trademark | `/documents/intellectual-property-rights/trademark` | L | 1289 | Trade a Mark. Trade with Mark. | 5 | Y | 3 |

**D9. IT and Websites** — category hub `/documents/it-and-websites`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D9.1 | IT and Net related Contracts | `/documents/it-and-websites/it-and-net-related-contracts` | L | 1222 | Code your legal Contracts. / Few clicks as you do. | 7 | Y | 4 |
| D9.2 | Software Contracts | `/documents/it-and-websites/software-contracts` | L | 605 | Create a fair software agreement. | 5 | Y | 0 (to define) |
| D9.3 | Hardware Contracts | `/documents/it-and-websites/hardware-contracts` | L | 424 | Contract for hardware transactions. | 4 | Y | 0 (to define) |
| D9.4 | Maintenance Agreements | `/documents/it-and-websites/maintenance-agreements` | L | 320 | Maintain relationships. | 3 | Y | 0 (to define) |
| D9.5 | Website Policies & Documents | `/documents/it-and-websites/website-policies-and-documents` | L | 1401 | Create with clicks. Comply with rules. | 8 | Y | 0 (to define) |
| D9.6 | Cyber Security & Data Protection (upcoming) | `/documents/it-and-websites/cyber-security-and-data-protection` | U | 51 (stub) | Secure the data, legally. | 0 | — | 0 (to define) |
| D9.7 | Mobile App (upcoming) | `/documents/it-and-websites/mobile-app` | U | 50 (stub) | Create agreement. Develop App. | 0 | — | 0 (to define) |
| D9.8 | Privacy & Cookie Policy | `/documents/it-and-websites/privacy-and-cookie-policy` | L | 28 (stub) | — | 0 | — | 0 (to define) |

**D10. HR and Service** — category hub `/documents/hr-and-service`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D10.1 | Agents and Broker | `/documents/hr-and-service/agents-and-broker` | L | 904 | Involve the people. Revolve the business. | 5 | Y | 4 |
| D10.2 | Apprenticeship | `/documents/hr-and-service/apprenticeship` | L | 684 | Communicate, deal with the prospects, legally. | 4 | Y | 3 |
| D10.3 | Consultants (upcoming) | `/documents/hr-and-service/consultants` | U | 31 (stub) | — | 0 | — | 0 (to define) |
| D10.4 | Employer-Employee Communication | `/documents/hr-and-service/employer-employee-communication` | L | 866 | Communicate formally. Protect legally. | 8 | — | 6 |
| D10.5 | ESOP Schemes (upcoming) | `/documents/hr-and-service/esop-schemes` | U | 42 (stub) | Win the workplace to win the marketplace. | 0 | — | 0 (to define) |
| D10.6 | HR Operations (upcoming) | `/documents/hr-and-service/hr-operations` | U | 52 (stub) | Manage the HR operations, professionally. | 0 | — | 0 (to define) |
| D10.7 | HR Policies (upcoming) | `/documents/hr-and-service/hr-policies` | U | 895 | Create HR Policies with clarity. | 3 | — | 0 (to define) |
| D10.8 | Job Agreements | `/documents/hr-and-service/job-agreements` | L | 647 | Agree on paper. Always. | 3 | Y | 4 |
| D10.9 | Work from Home | `/documents/hr-and-service/work-from-home` | L | 19 (empty) | Work from home. Now. | 0 | — | 0 (to define) |
| D10.10 | Job Application and Offers | `/documents/hr-and-service/job-application-and-offers` | L | 495 | Apply professionally. Offer legally. | 3 | — | 3 |
| D10.11 | Labour Agreements | `/documents/hr-and-service/labour-agreements` | L | 1021 | Agree to conform to labour compliances. | 4 | Y | 4 |

**D11. Legal** — category hub `/documents/legal`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D11.1 | Affidavits | `/documents/legal/affidavits` | L | 760 | Man of words? Put it in writing as well. / You for yourself. | 4 | — | 0 (to define) |
| D11.2 | Arbitration | `/documents/legal/arbitration` | L | 1363 | State the claims. Or, file objections. / Conflict is inevitable, but combat is optional. | 9 | Y | 6 |
| D11.3 | Mediation | `/documents/legal/mediation` | L | 34 (stub) | Conflict is inevitable, but combat is optional. | 0 | — | 0 (to define) |
| D11.4 | Negotiation | `/documents/legal/negotiation` | L | 2 (empty) | — | 0 | — | 0 (to define) |
| D11.5 | Consumer | `/documents/legal/consumer` | L | 1307 | Write to claim your Rights. Now. | 4 | — | 5 |
| D11.6 | Motor Vehicles | `/documents/legal/motor-vehicles` | L | 923 | Write & Claim on papers, driven by Law. | 4 | — | 1 |
| D11.7 | Notices | `/documents/legal/notices` | L | 854 | Get noticed! | 5 | — | 0 (to define) |
| D11.8 | RTI | `/documents/legal/rti` | L | 926 | Empower yourself with information. | 6 | — | 2 |
| D11.9 | Legal Notices | `/documents/legal/legal-notices` | L | 596 | Take the first step to raise any grievance. | 4 | — | 8 |
| D11.10 | Reply to Legal Notices | `/documents/legal/reply-to-legal-notices` | L | 444 | Bounce back. Legally. | 3 | — | 1 |
| D11.11 | Service Agreement with Lawyer | `/documents/legal/service-agreement-with-lawyer` | L | 1048 | Advice for preventive protection. | 6 | Y | 2 |
| D11.12 | Vakalatnama | `/documents/legal/vakalatnama` | L | 931 | Authorise the Lawyer to fight for you. | 4 | — | 14 |

**D12. Property Transactions** — category hub `/documents/property-transactions`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D12.1 | Building Contracts | `/documents/property-transactions/building-contracts` | L | 1982 | Create the real, legal foundation. | 5 | Y | 9 |
| D12.2 | Exchange Deeds and Settlement | `/documents/property-transactions/exchange-deeds-and-settlement` | L | 1657 | Write it down for permanent settlement. | 7 | Y | 2 |
| D12.3 | Lease | `/documents/property-transactions/lease` | L | 3143 | Lease with ease. | 9 | Y | 7 |
| D12.4 | Mortgage (upcoming) | `/documents/property-transactions/mortgage` | U | 1709 | Mortgage with clarity & Law. | 3 | Y | 2 |
| D12.5 | Notices regarding Property Transactions | `/documents/property-transactions/notices-regarding-property-transactions` | L | 837 | Raise your voice. Respond to the odds. | 5 | — | 5 |
| D12.6 | Release and NOCs | `/documents/property-transactions/release-and-nocs` | L | 1841 | Release your title, legally. | 7 | Y | 4 |
| D12.7 | Rent | `/documents/property-transactions/rent` | L | 1175 | Rent happiness. | 7 | Y | 7 |
| D12.8 | Sale and Purchase | `/documents/property-transactions/sale-and-purchase` | L | 2081 | Sale and purchase with security of Law. | 6 | Y | 7 |

**D13. RERA** — category hub `/documents/rera`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D13.1 | For Builders and Developers | `/documents/rera/for-builders-and-developers` | L | 4121 | — | 48 | Y | 0 (to define) |
| D13.2 | For Consumers | `/documents/rera/for-consumers` | L | 2281 | Act legal. Get real. | 29 | Y | 1 |
| D13.3 | For Agents | `/documents/rera/for-agents` | L | 1764 | Help really. Get legally. | 17 | Y | 0 (to define) |

**D14. SEBI (upcoming)** — category hub `/documents/sebi`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D14.1 | Insider Trading | `/documents/sebi/insider-trading` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D14.2 | Listing Regulation | `/documents/sebi/listing-regulation` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D14.3 | Takeover | `/documents/sebi/takeover` | U | 17 (empty) | — | 0 | — | 0 (to define) |

**D15. Secretarial (upcoming)** — category hub `/documents/secretarial`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D15.1 | Secretarial Compliances | `/documents/secretarial/secretarial-compliances` | U | 1357 | — | 4 | Y | 0 (to define) |
| D15.2 | Board Meeting | `/documents/secretarial/board-meeting` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.3 | Company Meetings | `/documents/secretarial/company-meetings` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.4 | Directors or KMP | `/documents/secretarial/directors-or-kmp` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.5 | General Meeting | `/documents/secretarial/general-meeting` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.6 | Misc. Drafts | `/documents/secretarial/misc-drafts` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.7 | NBFCs | `/documents/secretarial/nbfcs` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.8 | Policies and Codes | `/documents/secretarial/policies-and-codes` | U | 17 (empty) | — | 0 | — | 0 (to define) |
| D15.9 | Resolutions | `/documents/secretarial/resolutions` | U | 17 (empty) | — | 0 | — | 0 (to define) |

**D16. Students** — category hub `/documents/students`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D16.1 | Affidavits for Students | `/documents/students/affidavits-for-students` | L | 727 | Online. On time. | 4 | — | 7 |
| D16.2 | Application | `/documents/students/application` | L | 480 | To the Principal . . . And beyond. | 4 | — | 4 |
| D16.3 | CV | `/documents/students/cv` | L | 542 | First impression. First class. | 4 | — | 6 |

**D17. Succession and Inheritance** — category hub `/documents/succession-and-inheritance`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D17.1 | Adoption | `/documents/succession-and-inheritance/adoption` | L | 1342 | Adopt the legal procedure. | 8 | Y | 4 |
| D17.2 | Family Agreement and Settlement | `/documents/succession-and-inheritance/family-agreement-and-settlement` | L | 991 | Write your family story, in legal language. | 5 | Y | 5 |
| D17.3 | Gift Deed | `/documents/succession-and-inheritance/gift-deed` | L | 824 | Gift with Love and Law. | 4 | Y | 8 |
| D17.4 | Partition | `/documents/succession-and-inheritance/partition` | L | 1361 | Divide with Rules. | 4 | Y | 7 |
| D17.5 | Power of Attorney | `/documents/succession-and-inheritance/power-of-attorney` | L | 1426 | Transfer the Power, with Law. | 5 | Y | 6 |
| D17.6 | Will | `/documents/succession-and-inheritance/will` | L | 2301 | Create your Will today. / It will be needed one day. | 7 | Y | 5 |

**D18. Accounting & Tax (upcoming)** — category hub `/documents/accounting-and-tax`

| # | Sub-category hub (H2) | Proposed URL | L/U | Body words | Manual one-liner(s) | FAQs | Req. table | Doc pages |
|---|---|---|---|---|---|---|---|---|
| D18.1 | GST | `/documents/accounting-and-tax/gst` | U | 77 (stub) | — | 0 | Y | 0 (to define) |
| D18.2 | Income Tax | `/documents/accounting-and-tax/income-tax` | U | 73 (stub) | — | 0 | Y | 0 (to define) |
| D18.3 | Finance (upcoming) | `/documents/accounting-and-tax/finance` | U | 12 (empty) | — | 0 | — | 0 (to define) |
| D18.4 | Accounting (upcoming) | `/documents/accounting-and-tax/accounting` | U | 12 (empty) | — | 0 | — | 0 (to define) |

### 8.2 Pleadings manual — section landing `/pleadings` · 13 area hubs · 89 pleadings (→ 68 canonical)

The intro (L195–245) also promises Matrimonial, Constitutional (writ), Arbitration, Company Law (NCLT) and Energy Law sets. Constitutional, Energy and NCLT have **no drafts**, so they are a content gap. The manual has no FAQs, one-liners or requirement tables for pleadings; write them using the §7.3 pleading template.

**P1. Civil Pleadings** — hub `/pleadings/civil-pleadings`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P1.1 | Affidavit for Civil Matters | `/pleadings/civil-pleadings/affidavit-for-civil-matters` | 262 | — |
| P1.2 | Suit for Permanent Injunction | `/pleadings/civil-pleadings/suit-for-permanent-injunction` | 1535 | — |
| P1.3 | Application for Temporary Injunction | `/pleadings/civil-pleadings/application-for-temporary-injunction` | 518 | — |
| P1.4 | Application under Order XXXIX Rule 2-A | `/pleadings/civil-pleadings/application-under-order-xxxix-rule-2-a` | 708 | — |
| P1.5 | Application to Sue as an Indigent Person | `/pleadings/civil-pleadings/application-to-sue-as-an-indigent-person` | 414 | — |
| P1.6 | Suit for Ejectment and Damages | `/pleadings/civil-pleadings/suit-for-ejectment-and-damages` | 1146 | — |
| P1.7 | Suit for Specific Performance of Contract | `/pleadings/civil-pleadings/suit-for-specific-performance-of-contract` | 806 | Canonical; update to Specific Relief (Amendment) Act 2018 |
| P1.8 | Model Draft for Written Statement | `/pleadings/civil-pleadings/model-draft-for-written-statement` | 1117 | Canonical WS page; check Commercial Courts Act Order VIII timelines |
| P1.9 | Caveat under Section 148-A of CPC | `/pleadings/civil-pleadings/caveat-under-section-148-a-of-cpc` | 487 | — |
| P1.10 | Transfer Petition under Section 25 of CPC | `/pleadings/civil-pleadings/transfer-petition-under-section-25-of-cpc` | 2272 | — |
| P1.11 | Format of a Plaint claiming compensation for Defamantion | `/pleadings/civil-pleadings/format-of-a-plaint-claiming-compensation-for-defamation` | 623 | Typo 'Defamantion'; IPC 499/500 → BNS s.356 if criminal limb cited |
| P1.12 | Format of a Plaint by a Minor or a person of Unsound Mind in a Civil Suit | `/pleadings/civil-pleadings/format-of-a-plaint-by-a-minor-or-a-person-of-unsound-mind-in-a-civil-s` | 478 | — |
| P1.13 | Format of a Written Statement | `/pleadings/civil-pleadings/format-of-a-written-statement` | 564 | Duplicate intent with 'Model Draft for Written Statement' |
| P1.14 | Format of an application to set aside a decree passed ex parte | `/pleadings/civil-pleadings/format-of-an-application-to-set-aside-a-decree-passed-ex-parte` | 546 | — |
| P1.15 | Format of an appeal against a decree | `/pleadings/civil-pleadings/format-of-an-appeal-against-a-decree` | 646 | — |
| P1.16 | Format of Civil Appeal | `/pleadings/civil-pleadings/format-of-civil-appeal` | 765 | Overlaps 'appeal against a decree' |
| P1.17 | Format of a Suit for Specific Performance of a contract | `/pleadings/civil-pleadings/format-of-a-suit-for-specific-performance-of-a-contract` | 865 | Duplicate intent with 'Suit for Specific Performance of Contract'; post-2018 SRA amendment (s.10 mandatory relief) |

**P2. Family Law Pleadings** — hub `/pleadings/family-law-pleadings`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P2.1 | Petition for Restitution of Conjugal Rights | `/pleadings/family-law-pleadings/petition-for-restitution-of-conjugal-rights` | 659 | Title DUPLICATED (2 pages) + 'Suit For Restitution…' — consolidate into HMA s.9 page + Muslim-law variant |
| P2.2 | Suit For Divorce By Muslim Wife (Talaq-Tafweez) | `/pleadings/family-law-pleadings/suit-for-divorce-by-muslim-wife-talaq-tafweez` | 517 | — |
| P2.3 | Suit For Restitution Of Conjugal Rights | `/pleadings/family-law-pleadings/suit-for-restitution-of-conjugal-rights` | 630 | Near-duplicate of RCR petitions; Title Case inconsistent |
| P2.4 | Petition for Judicial Separation | `/pleadings/family-law-pleadings/petition-for-judicial-separation` | 724 | 91% overlap with 'Dissolution… Decree of Divorce'; 3 judicial-separation drafts in total |
| P2.5 | Petition for Dissolution of Marriage by a Decree of Divorce | `/pleadings/family-law-pleadings/petition-for-dissolution-of-marriage-by-a-decree-of-divorce` | 784 | — |
| P2.6 | Format of Mutual Consent Divorce | `/pleadings/family-law-pleadings/format-of-mutual-consent-divorce` | 1534 | Duplicate intent (mutual consent) — make this the canonical page |
| P2.7 | Petition for Dissolution of Marriage by a Decree of Divorce by Mutual Consent | `/pleadings/family-law-pleadings/petition-for-dissolution-of-marriage-by-a-decree-of-divorce-by-mutual` | 608 | Duplicate intent: 3 mutual-consent drafts — merge (s.13B HMA; cooling-off waivable: Amardeep Singh 2017) |
| P2.8 | Draft Affidavit in Matrimonial Pleadings | `/pleadings/family-law-pleadings/draft-affidavit-in-matrimonial-pleadings` | 419 | — |
| P2.9 | Petition by  Wife for Judicial Separation on the Ground of her Husband's Adultry | `/pleadings/family-law-pleadings/petition-by-wife-for-judicial-separation-on-the-ground-of-her-husbands` | 364 | — |
| P2.10 | Petition by Girl for a Decree of Nullity of Marriage | `/pleadings/family-law-pleadings/petition-by-girl-for-a-decree-of-nullity-of-marriage` | 566 | Rename ('Girl' → 'Wife (minor at marriage)'); duplicate intent |
| P2.11 | Suit For Contribution By A Member Of A Joint Hindu Family Against Other Members | `/pleadings/family-law-pleadings/suit-for-contribution-by-a-member-of-a-joint-hindu-family-against-othe` | 641 | — |
| P2.12 | Petition by Wife for Divorce | `/pleadings/family-law-pleadings/petition-by-wife-for-divorce` | 476 | — |
| P2.13 | Petition by Wife for Decree of Nullity of Marriage | `/pleadings/family-law-pleadings/petition-by-wife-for-decree-of-nullity-of-marriage` | 397 | Duplicate intent with 'Petition by Girl…' and 'Annulment of Void Marriage' |
| P2.14 | Petition by Wife for Alimony during the pendency of Suit | `/pleadings/family-law-pleadings/petition-by-wife-for-alimony-during-the-pendency-of-suit` | 378 | — |
| P2.15 | Petition by Wife for Judicial Separation | `/pleadings/family-law-pleadings/petition-by-wife-for-judicial-separation` | 517 | Duplicate intent (3rd judicial-separation draft) |
| P2.16 | Petition for seeking Decree of Divorce by Mutual Consent | `/pleadings/family-law-pleadings/petition-for-seeking-decree-of-divorce-by-mutual-consent` | 531 | — |
| P2.17 | Petition for Restitution of Conjugal Rights | `/pleadings/family-law-pleadings/petition-for-restitution-of-conjugal-rights` | 551 | — |
| P2.18 | Petition by Wife for Annulment of Void Marriage | `/pleadings/family-law-pleadings/petition-by-wife-for-annulment-of-void-marriage` | 528 | — |
| P2.19 | Petition by Husband for Annulment of Voidable Marriage | `/pleadings/family-law-pleadings/petition-by-husband-for-annulment-of-voidable-marriage` | 687 | — |
| P2.20 | Petition for Removal of Guardian of a Child | `/pleadings/family-law-pleadings/petition-for-removal-of-guardian-of-a-child` | 439 | — |
| P2.21 | Petition for Permission to Sell Minor's Property | `/pleadings/family-law-pleadings/petition-for-permission-to-sell-minors-property` | 751 | — |
| P2.22 | Format of Application for Child Custody- | `/pleadings/family-law-pleadings/format-of-application-for-child-custody` | 573 | — |
| P2.23 | Application for Maintenance under Section 125 OF CRPC, 1973 | `/pleadings/family-law-pleadings/application-for-maintenance-under-section-125-of-crpc-1973` | 857 | CrPC 125 → BNSS s.144; casing 'OF CRPC' |

**P3. Succession and Inheritance** — hub `/pleadings/succession-and-inheritance`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P3.1 | Petition for Grant of Probate | `/pleadings/succession-and-inheritance/petition-for-grant-of-probate` | 875 | — |
| P3.2 | Petition for Grant of Letters of Administration | `/pleadings/succession-and-inheritance/petition-for-grant-of-letters-of-administration` | 901 | 92% overlap with Probate — fine (template family) but differentiate copy |
| P3.3 | Petition for the Grant of Succession Certificate | `/pleadings/succession-and-inheritance/petition-for-the-grant-of-succession-certificate` | 709 | — |

**P4. Criminal Law Pleadings** — hub `/pleadings/criminal-law-pleadings`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P4.1 | Application for Grant of Bail | `/pleadings/criminal-law-pleadings/application-for-grant-of-bail` | 618 | CrPC → BNSS s.480/483; generic duplicate of regular-bail drafts |
| P4.2 | Application for the Grant of Anticipatory Bail | `/pleadings/criminal-law-pleadings/application-for-the-grant-of-anticipatory-bail` | 774 | CrPC 438 → BNSS s.482; merge with s.438 version |
| P4.3 | Application seeking exemption from personal apperance of Complainant/Accused | `/pleadings/criminal-law-pleadings/application-seeking-exemption-from-personal-appearance-of-complainant` | 312 | Typo 'apperance'; cite BNSS s.228/355 (old CrPC s.205/317) |
| P4.4 | Regular Bail Application before Court of Metropolitan Magistrate u/s 437CrPC | `/pleadings/criminal-law-pleadings/regular-bail-application-before-court-of-metropolitan-magistrate-u-s-4` | 595 | CrPC 437 → BNSS s.480; 96% overlap with Sessions version — merge into one page with forum toggle |
| P4.5 | Regular bail Application before Court of Sessions Court u/s 439 CrPC | `/pleadings/criminal-law-pleadings/regular-bail-application-before-court-of-sessions-court-u-s-439-crpc` | 599 | CrPC 439 → BNSS s.483; 'Court of Sessions Court' redundant |
| P4.6 | Application for anticipatory bail under Section 438 CrPC | `/pleadings/criminal-law-pleadings/application-for-anticipatory-bail-under-section-438-crpc` | 321 | CrPC 438 → BNSS s.482; duplicate intent with 'Application for the Grant of Anticipatory Bail' |
| P4.7 | Application seeking Bail Under Section 167 CrPC | `/pleadings/criminal-law-pleadings/application-seeking-bail-under-section-167-crpc` | 314 | CrPC 167(2) → BNSS s.187 (default bail) |
| P4.8 | Application Under Section 320 CrPC for Compounding of Case | `/pleadings/criminal-law-pleadings/application-under-section-320-crpc-for-compounding-of-case` | 236 | CrPC 320 → BNSS s.359; IPC offences table → BNS |
| P4.9 | Affidavit of Surety in support of Bail Bond | `/pleadings/criminal-law-pleadings/affidavit-of-surety-in-support-of-bail-bond` | 186 | — |
| P4.10 | Application Under Section. 311 Cr.P.C.for Recalling of Witness | `/pleadings/criminal-law-pleadings/application-under-section-311-cr-p-c-for-recalling-of-witness` | 302 | CrPC 311 → BNSS s.348; punctuation 'Section. 311 Cr.P.C.for' |
| P4.11 | Application seeking adjournment under Sec. 256 of Cr. P.C. | `/pleadings/criminal-law-pleadings/application-seeking-adjournment-under-sec-256-of-cr-p-c` | 244 | CrPC 256 → BNSS s.279 (title is about non-appearance of complainant, verify) |
| P4.12 | Format of a Criminal Complaint before the Court of Metropolitan Magistrate | `/pleadings/criminal-law-pleadings/format-of-a-criminal-complaint-before-the-court-of-metropolitan-magist` | 350 | CrPC s.200 → BNSS s.223 (pre-cognizance hearing of accused); IPC → BNS |

**P5. Rent & Property** — hub `/pleadings/rent-and-property`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P5.1 | Suit for Eviction of Licensee | `/pleadings/rent-and-property/suit-for-eviction-of-licensee` | 587 | — |
| P5.2 | Suit for Contribution Against Joint Owner for Expenses on The Repairs | `/pleadings/rent-and-property/suit-for-contribution-against-joint-owner-for-expenses-on-the-repairs` | 617 | — |
| P5.3 | Suit for Cancellation of Sale Deed on Account of Fraud | `/pleadings/rent-and-property/suit-for-cancellation-of-sale-deed-on-account-of-fraud` | 627 | — |
| P5.4 | Suit For Partition In Hindu Family | `/pleadings/rent-and-property/suit-for-partition-in-hindu-family` | 749 | — |

**P6. Consumer Law** — hub `/pleadings/consumer-law`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P6.1 | Complaint under Consumet Protection Act | `/pleadings/consumer-law/complaint-under-consumer-protection-act` | 949 | Typo 'Consumet'; CPA 1986 — repealed 20 Jul 2020; DUPLICATE of CPA 2019 complaint — retire |
| P6.2 | Complaint under the Consumer Protection Act, 2019 | `/pleadings/consumer-law/complaint-under-the-consumer-protection-act-2019` | 1446 | Canonical consumer complaint; pecuniary limits ₹50 lakh / ₹2 crore (2021 Rules); e-Daakhil filing |
| P6.3 | Complaint Under of The Protection of Women from Domestic Violence Act, 2005 | `/pleadings/consumer-law/complaint-under-of-the-protection-of-women-from-domestic-violence-act` | 1034 | Mis-categorised (Consumer Law → Family); grammar 'Under of' |

**P7. Cheque Bounce Matters** — hub `/pleadings/cheque-bounce-matters`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P7.1 | Complaint under Section 138, The Negotiable Instruments Act | `/pleadings/cheque-bounce-matters/complaint-under-section-138-the-negotiable-instruments-act` | 874 | 4 cheque-bounce complaints — consolidate to 1 canonical + variants; BNSS s.223 cognizance note |
| P7.2 | Complaint against Cheque Dishonour | `/pleadings/cheque-bounce-matters/complaint-against-cheque-dishonour` | 858 | — |
| P7.3 | Dishonour of Cheques | `/pleadings/cheque-bounce-matters/dishonour-of-cheques` | 622 | Vague title; duplicate intent |
| P7.4 | Format of Complaint Under section 138 and 142 of the Negotiable Instrument Act, 1881 | `/pleadings/cheque-bounce-matters/format-of-complaint-under-section-138-and-142-of-the-negotiable-instru` | 766 | — |
| P7.5 | Affidavit | `/pleadings/cheque-bounce-matters/affidavit` | 147 | Vague title (cheque-bounce evidence affidavit, s.145 NI Act) |

**P8. Suit for Damages** — hub `/pleadings/suit-for-damages`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P8.1 | Suit For Damages Of Trespass | `/pleadings/suit-for-damages/suit-for-damages-of-trespass` | 688 | — |
| P8.2 | Suit For Damages By Bailer Against Bailee | `/pleadings/suit-for-damages/suit-for-damages-by-bailor-against-bailee` | 739 | Typo 'Bailer' → Bailor |
| P8.3 | Suit For Damages Of Trespass & Illegal Attachments | `/pleadings/suit-for-damages/suit-for-damages-of-trespass-and-illegal-attachments` | 773 | — |
| P8.4 | Suit For Damages Against Public Servant/Police Officer For Wrongful Acts | `/pleadings/suit-for-damages/suit-for-damages-against-public-servant-police-officer-for-wrongful-ac` | 860 | — |
| P8.5 | Suit For Damages Against Doctors For Negligence | `/pleadings/suit-for-damages/suit-for-damages-against-doctors-for-negligence` | 833 | — |
| P8.6 | Suit For Damages By Landlord Against His Tenants For Injury Caused | `/pleadings/suit-for-damages/suit-for-damages-by-landlord-against-his-tenants-for-injury-caused` | 719 | — |
| P8.7 | Suit For Damages For Wrongful Sale Of Plaintiff's House | `/pleadings/suit-for-damages/suit-for-damages-for-wrongful-sale-of-plaintiffs-house` | 950 | — |
| P8.8 | Suit For Damages For Breach Of Contract To Serve | `/pleadings/suit-for-damages/suit-for-damages-for-breach-of-contract-to-serve` | 754 | — |
| P8.9 | Suit For Damages For Malicious Prosecution/False Case | `/pleadings/suit-for-damages/suit-for-damages-for-malicious-prosecution-false-case` | 857 | IPC refs → BNS |

**P9. Money Recovery & Financial Matters** — hub `/pleadings/money-recovery-and-financial-matters`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P9.1 | Suit for Money Recovery | `/pleadings/money-recovery-and-financial-matters/suit-for-money-recovery` | 1082 | Add Order XXXVII summary-suit variant; Commercial Courts pre-institution mediation (s.12A) |
| P9.2 | Suit For Refund Of Money Advanced For Due Performance Of Contract | `/pleadings/money-recovery-and-financial-matters/suit-for-refund-of-money-advanced-for-due-performance-of-contract` | 764 | — |
| P9.3 | Suit For Recovery Of Money For Goods Sold | `/pleadings/money-recovery-and-financial-matters/suit-for-recovery-of-money-for-goods-sold` | 785 | — |
| P9.4 | Suit For Promissory Note | `/pleadings/money-recovery-and-financial-matters/suit-for-promissory-note` | 749 | — |
| P9.5 | Suit For Foreign Bill Of Exchange | `/pleadings/money-recovery-and-financial-matters/suit-for-foreign-bill-of-exchange` | 751 | EXACT DUPLICATE (98% overlap) — keep one |
| P9.6 | Suit For Foreign Bill Of Exchange | `/pleadings/money-recovery-and-financial-matters/suit-for-foreign-bill-of-exchange` | 751 | EXACT DUPLICATE (98% overlap) — keep one |

**P10. Alternative Dispute Resolution** — hub `/pleadings/alternative-dispute-resolution`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P10.1 | Award by an Arbitral Tribunal | `/pleadings/alternative-dispute-resolution/award-by-an-arbitral-tribunal` | 542 | Not a pleading — move to ADR documents / Equator cross-link |

**P11. Intellectual Property Rights** — hub `/pleadings/intellectual-property-rights`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P11.1 | Suit For Injunction In The Matter Of Copyright | `/pleadings/intellectual-property-rights/suit-for-injunction-in-the-matter-of-copyright` | 890 | — |
| P11.2 | Suit For Damages For Infringement Of Copyright | `/pleadings/intellectual-property-rights/suit-for-damages-for-infringement-of-copyright` | 867 | — |

**P12. Corporate Law** — hub `/pleadings/corporate-law`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P12.1 | Complaint Petition | `/pleadings/corporate-law/complaint-petition` | 702 | Mis-categorised: consumer complaint under 'Corporate Law'; CPA 1986 |
| P12.2 | SAMPLE COMPLAINT PETITION For deficient service | `/pleadings/corporate-law/sample-complaint-petition-for-deficient-service` | 967 | ALL-CAPS title; consumer complaint mis-filed under Corporate Law; 'District Forum' → District Commission |
| P12.3 | THE COMPLAINT | `/pleadings/corporate-law/the-complaint` | 1105 | Non-descriptive ALL-CAPS title; CPA 1986 — rewrite under CPA 2019 |

**P13. MACT & Insurance** — hub `/pleadings/mact-and-insurance`

| # | Pleading (H2) | Proposed URL | Words | Flags / action |
|---|---|---|---|---|
| P13.1 | Suit against Insurance Company | `/pleadings/mact-and-insurance/suit-against-insurance-company` | 809 | Consider Insurance Ombudsman (Rules 2017) route; MACT claims under MV Act s.166 |

### 8.3 Compliance manual — section landing `/compliance` · 7 group hubs · 22 service pages

**C0. Compliances** — section landing `/compliance` (538 words; one-liners: Customer experiences / Save yourself. Get legal protection for everything you do. Right now.)

**C1. ROC Compliances** — hub `/compliance/roc-compliances` (182 words; one-liner: —)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C1.1 | Corporate Compliances | `/compliance/roc-compliances/corporate-compliances` | 625 | Execute. Intimate. Comply. | Y/Y/Y | 0 | Verify current DIR-3 KYC periodicity, ADT-1, MGT-7A |
| C1.2 | Companies and OPC Annual Filings | `/compliance/roc-compliances/companies-and-opc-annual-filings` | 1614 | Take care, it's an annual affair. | Y/Y/Y | 18 | Check AOC-4/MGT-7/7A, DIR-3 KYC; MCA V3 forms |
| C1.3 | LLP Annual Filing | `/compliance/roc-compliances/llp-annual-filing` | 855 | Make it an annual celebration. | Y/Y/Y | 6 | Form 8/11 dates OK; audit threshold ₹40 lakh / ₹25 lakh OK |

**C2. Closure of Business** — hub `/compliance/closure-of-business` (237 words; one-liner: Close. Lock. Forget. / Business Conversion Services)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C2.1 | Closing of Company | `/compliance/closure-of-business/closing-of-company` | 1139 | Let us wind up. | Y/Y/Y | 10 | Add C-PACE (STK-2 centralised processing, 2023) |
| C2.2 | Closure of LLP | `/compliance/closure-of-business/closure-of-llp` | 1341 | Strike off. | Y/Y/Y | 9 | COPIED: 'Whether LegalWiz.in will provide…' FAQ (LegalWiz brand) |
| C2.3 | Closing an OPC | `/compliance/closure-of-business/closing-an-opc` | 1374 | Let it go, in one go. | Y/Y/Y | 8 | — |

**C3. GST** — hub `/compliance/gst` (87 words; one-liner: Experience a good service. / Benefits of GST)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C3.1 | GST Registration | `/compliance/gst/gst-registration` | 2135 | Feel it simple, good. | Y/Y/Y | 23 | Update for GST 2.0 slabs (22 Sep 2025) and biometric Aadhaar authentication |
| C3.2 | GST Return Filing | `/compliance/gst/gst-return-filing` | 1433 | Filing. Smiling. | Y/Y/Y | 10 | OUTDATED: GSTR-2/GSTR-3 matching regime (never operationalised; replaced by GSTR-1/3B/2B, IMS from Oct 2024) |

**C4. Taxation** — hub `/compliance/taxation` (58 words; one-liner: Pay. Save.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C4.1 | Income Tax Return (ITR) Filing | `/compliance/taxation/income-tax-return-itr-filing` | 1144 | File. Smile. | Y/Y/Y | 8 | COPIED: 'consult Vakilsearch'; OUTDATED: IT Act 1961 → Income-tax Act 2025 (tax year) from 1 Apr 2026 |
| C4.2 | TDS Return Filing | `/compliance/taxation/tds-return-filing` | 1596 | Get it back. | Y/Y/Y | 9 | COPIED: 'With Corpbiz…', 'Vakilsearch's Google Calendar'; update section refs to IT Act 2025 |
| C4.3 | Professional Tax Registration | `/compliance/taxation/professional-tax-registration` | 982 | A State mandate. | Y/Y/Y | 9 | COPIED: 4 FAQs hyperlinked to corpbiz.io/professional-tax-registration |

**C5. Accounting** — hub `/compliance/accounting` (385 words; one-liner: Make a balance. / Advantages of Online Accounting)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C5.1 | Accounting and Book keeping | `/compliance/accounting/accounting-and-book-keeping` | 1529 | Create. Maintain. Preserve. | Y/Y/Y | 16 | COPIED: 11 FAQs hyperlinked to provenience.in; 'We at Provenience' |
| C5.2 | Payroll Maintenance | `/compliance/accounting/payroll-maintenance` | 1172 | Infuse high morale. | Y/—/Y | 6 | COPIED: 'confidential with Vakilsearch?'; update to Code on Wages 2019 / SS Code 2020 |

**C6. Labour Law Compliances** — hub `/compliance/labour-law-compliances` (457 words; one-liner: Get the feel good factory. / Services and Consultations / Consultation on labour matters)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C6.1 | Provident Fund (PF) Registration | `/compliance/labour-law-compliances/provident-fund-pf-registration` | 867 | A fair care. | Y/Y/Y | 5 | COPIED: 'team at Vakilsearch'; EPF Act → Code on Social Security 2020 (21 Nov 2025; schemes continue) |
| C6.2 | ESI Registration | `/compliance/labour-law-compliances/esi-registration` | 931 | Give the support to get it. | Y/Y/Y | 5 | ESI Act 1948 → Code on Social Security 2020 |
| C6.3 | Shops and Establishments License | `/compliance/labour-law-compliances/shops-and-establishments-license` | 1508 | Provide a happy shopping experience. | Y/Y/Y | 9 | COPIED: 'At Vakilsearch…' (×3); state S&E Acts continue |
| C6.4 | Employee Stock Option Plan [ESOP] | `/compliance/labour-law-compliances/employee-stock-option-plan-esop` | 1686 | Rise together. | Y/Y/— | 8 | — |

**C7. Audit** — hub `/compliance/audit` (750 words; one-liner: Catch it now. / Due diligence and audit services / Our Audit Services Include / Types)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| C7.1 | Secretarial Audit | `/compliance/audit/secretarial-audit` | 1256 | Check the compliances. | Y/Y/Y | 15 | Update for SEBI LODR Reg 24A amendments (Dec 2024: auditor appointment/tenure) |
| C7.2 | Tax Audit | `/compliance/audit/tax-audit` | 2268 | Get a tax assessment. | Y/Y/Y | 0 | OUTDATED: business ₹1 crore → ₹10 crore if cash ≤5% (professionals ₹50 lakh unchanged); IT Act 2025 numbering |
| C7.3 | GST Audit | `/compliance/audit/gst-audit` | 1828 | Recheck the accuracy. | Y/Y/Y | 0 | OUTDATED: s.35(5) CA audit + certified GSTR-9C omitted w.e.f. 1 Aug 2021 (self-certified 9C) — rewrite as 'GST annual return & reconciliation' |
| C7.4 | Company Audit | `/compliance/audit/company-audit` | 1004 | Identify problems. Increase credibility. | Y/Y/Y | 2 | Hub-level text names 'Registrationwala' (COPIED) |
| C7.5 | Internal Audit | `/compliance/audit/internal-audit` | 945 | Get introspection. | Y/Y/— | 3 | s.138 Companies Act thresholds — verify |

### 8.4 Start a Business manual — section landing `/start-a-business` · 6 group hubs · 26 service pages

All 26 service pages end with "Get assistance / Call now. 9468776000". Replace this with the unified contact number and with "Hire a professional" and Vidhi blocks.

**S0. Start a Business** — section landing `/start-a-business` (157 words; one-liners: Start your own business. / Get a little extra to become extraordinary. / Confused about how to start your business? / Get a healthy start for a bright future.)

**S1. Incorporate your Business** — hub `/start-a-business/incorporate-your-business` (708 words; one-liner: Convert your idea into reality. / Choose the right formation / How we do it. / Get straight to the finish line.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S1.1 | Private Limited Company (PLC) | `/start-a-business/incorporate-your-business/private-limited-company-plc` | 1357 | Chase dreams with Private Limited Company. | Y/Y/Y | 16 | 'PLC' ambiguous (→ 'Pvt Ltd'); SPICe+ (INC-32) refs; phone CTA |
| S1.2 | One Person Company | `/start-a-business/incorporate-your-business/one-person-company` | 1456 | Get a business face. | Y/Y/Y | 14 | Update OPC liberalisation (2021: no ₹50 lakh cap, NRI allowed) |
| S1.3 | Sole Proprietorship | `/start-a-business/incorporate-your-business/sole-proprietorship` | 756 | Run the one man show. | Y/Y/Y | 9 | — |
| S1.4 | Partnership Firm | `/start-a-business/incorporate-your-business/partnership-firm` | 897 | Multiply power. | Y/Y/Y | 8 | — |
| S1.5 | Limited liability Partnership | `/start-a-business/incorporate-your-business/limited-liability-partnership` | 1033 | Dream unlimited with limited risks. | Y/Y/Y | 12 | COPIED links: toppr.com (×2); casing |
| S1.6 | Nidhi Company | `/start-a-business/incorporate-your-business/nidhi-company` | 1009 | Get a company of money, for money. | Y/Y/Y | 7 | COPIED link: enterslice.com; update Nidhi (Amendment) Rules 2022 (NDH-4 pre-approval) |

**S2. Protect your Intellectual Property** — hub `/start-a-business/protect-your-intellectual-property` (428 words; one-liner: Protect your intellectual property. / LawDocs Assurance.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S2.1 | Patent | `/start-a-business/protect-your-intellectual-property/patent` | 1356 | Get protection and appreciation. | Y/Y/Y | 10 | COPIED: 'We, at LegalRaasta act as patent agent'; upcounsel.com links; Patents (Amendment) Rules 2024 |
| S2.2 | Copy Right | `/start-a-business/protect-your-intellectual-property/copyright` | 1290 | Register your copy, create a right. | Y/Y/Y | 12 | Heading typo → 'Copyright' |
| S2.3 | Trademark | `/start-a-business/protect-your-intellectual-property/trademark` | 1603 | Get identified. | Y/Y/Y | 19 | COPIED: Wikipedia definition (6 links); 'IP experts at ebizfiling… info@ebizfiling.com' |
| S2.4 | Geographical Indications | `/start-a-business/protect-your-intellectual-property/geographical-indications` | 704 | Get GI. Get pride. | Y/Y/Y | 2 | — |
| S2.5 | Logo Designing & Branding | `/start-a-business/protect-your-intellectual-property/logo-designing-and-branding` | 564 | Get a distinct identity. | Y/—/— | 4 | No Procedure/Docs blocks |

**S3. Get a License** — hub `/start-a-business/get-a-license` (194 words; one-liner: Fulfill eligibility. / Choose to proceed, now.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S3.1 | FSSAI | `/start-a-business/get-a-license/fssai` | 900 | Host the guest. | Y/Y/Y | 5 | COPIED FAQ hyperlinked to legaldocs.co.in blog |
| S3.2 | Import Export Code IEC | `/start-a-business/get-a-license/import-export-code-iec` | 767 | Cross the border. | Y/Y/Y | 10 | COPIED link: eximguru.com; add annual IEC update (Apr–Jun) |

**S4. Registrations for Business** — hub `/start-a-business/registrations-for-business` (170 words; one-liner: Get the necessary registrations)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S4.1 | MSME Registration | `/start-a-business/registrations-for-business/msme-registration` | 866 | Register for benefits. | Y/Y/Y | 4 | OUTDATED: Udyog Aadhaar (UAM) → Udyam (1 Jul 2020); revised limits from 1 Apr 2025 |
| S4.2 | Industrial Design Registration | `/start-a-business/registrations-for-business/industrial-design-registration` | 670 | Protect your industrial design. | Y/Y/Y | 6 | — |
| S4.3 | APEDA Registration | `/start-a-business/registrations-for-business/apeda-registration` | 609 | Export the food. | Y/Y/Y | 6 | — |
| S4.4 | Pollution Registration | `/start-a-business/registrations-for-business/pollution-registration` | 786 | Save the environment. | Y/Y/Y | 2 | — |
| S4.5 | Spices Board Registration | `/start-a-business/registrations-for-business/spices-board-registration` | 609 | Add salt to your business | Y/Y/Y | 4 | COPIED: Wikipedia definition |
| S4.6 | Barcode Registration | `/start-a-business/registrations-for-business/barcode-registration` | 606 | Raise a bar. | Y/Y/Y | 3 | — |

**S5. Quality certification** — hub `/start-a-business/quality-certification` (167 words; one-liner: Answer the doubts.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S5.1 | Agmark Certification | `/start-a-business/quality-certification/agmark-certification` | 1323 | Get a mark of standards. | Y/Y/Y | 0 | Links dmi.gov.in (official — acceptable as citation) |
| S5.2 | Hallmark Certification | `/start-a-business/quality-certification/hallmark-certification` | 1049 | Get the name in Golden letters. / Conditions | —/Y/Y | 3 | COPIED: Wikipedia (17 links) + wiktionary + business-standard; OUTDATED date (mandatory from 16 Jun 2021, HUID from 1 Apr 2023) |
| S5.3 | ISI Certification | `/start-a-business/quality-certification/isi-certification` | 769 | Get the standards of India. | Y/Y/Y | 6 | — |
| S5.4 | ISO Certification | `/start-a-business/quality-certification/iso-certification` | 1281 | Get an international recognition. / ISO Certification - An Overview | Y/Y/Y | 8 | — |

**S6. NGO and Society Registration** — hub `/start-a-business/ngo-and-society-registration` (772 words; one-liner: Do something beyond self.)

| # | Service page (H2) | Proposed URL | Words | One-liner | Benefits/Procedure/Docs | FAQs | Flags |
|---|---|---|---|---|---|---|---|
| S6.1 | Section 8 Company Registration | `/start-a-business/ngo-and-society-registration/section-8-company-registration` | 1088 | Get a company, for charity. | Y/Y/Y | 4 | Mentions s.25 Companies Act 1956 (context only); IT Act 2025 for 12A/80G equivalents |
| S6.2 | Trust Registration | `/start-a-business/ngo-and-society-registration/trust-registration` | 1170 | Get trusted | Y/Y/Y | 6 | 12A/80G → IT Act 2025 equivalents |
| S6.3 | Society Registration | `/start-a-business/ngo-and-society-registration/society-registration` | 1448 | Register an NGO | Y/Y/Y | 4 | — |

### 8.5 Page-count roll-up

| Section | Landing | Hubs | Leaf pages (raw) | Leaf pages (recommended) | Total recommended |
|---|---|---|---|---|---|
| Documents | 1 | 18 + 134 | 347 | 330 | 483 |
| Pleadings | 1 | 13 | 89 | 68 | 82 |
| Compliance | 1 | 7 | 22 | 22 | 30 |
| Start a Business | 1 | 6 | 26 | 26 | 33 |
| **Total** | **4** | **178** | **484** | **446** | **≈626** (raw 666) |

Pages beyond the manuals that the build also needs: about 50 regulated-entity pages carried over from the live sitemap (RBI, SEBI, IRDAI, other registrations, reporting), 6 advisory practice areas, the marketplace, Vidhi AI, eSign, the locker/DMS, the litigation and trademark trackers, pricing (3 plans), FinLegal Academy, grievance (loans and insurance), challans, vehicle, the blog and vlog hubs, and legal policies (Terms, Privacy/DPDP notice, Cookie, Refund, Disclaimer, Grievance Officer, Acceptable Use, eSign terms, Marketplace terms, Professional code).

---

## 9. Sources (accessed 25 Oct 2026)

| Source | URL |
|---|---|
| LawDocs homepage (head only served) | https://www.lawdocs.in/ |
| LawDocs robots.txt | https://www.lawdocs.in/robots.txt |
| LawDocs sitemap (186 URLs) | https://www.lawdocs.in/lawdocs-sitemap.xml |
| LawDocs llms.txt (absent; SPA shell) | https://www.lawdocs.in/llms.txt |
| LawDocs sample inner pages (head only) | https://www.lawdocs.in/about · /smartdrafts/property-matters/rent · /compliance-services/rbi_compliance/icaap-policy · /mortgage/ · /services/consult-lawyer · /blogs |
| Non-www host (deep URLs fail) | https://lawdocs.in/about · https://lawdocs.in/buy/rent |
| Search index check | WebSearch `site:lawdocs.in` (25 Oct 2026) |
| LawDocs Trainings home / store / course list | https://trainings.lawdocs.in/ · https://trainings.lawdocs.in/s/store · https://trainings.lawdocs.in/s/store/courses |
| Course pages | https://trainings.lawdocs.in/courses/Paralegal-Training-for-Students-621a57010cf2a8ffb53ce3fb · https://trainings.lawdocs.in/courses/Training-for-NBFC-Key-Managerial-Personnel-65bb5740e4b04112bd822020 |
| Corporate training page | https://trainings.lawdocs.in/s/pages/corporates-training |
| Stanford CodeX TechIndex — LawDocs | https://techindex.law.stanford.edu/companies/lawdocs |
| Google: Changes to HowTo and FAQ rich results (Aug 2023) | https://developers.google.com/search/blog/2023/08/howto-faq-changes |
| Google Search Central documentation updates (FAQ deprecation 7 May 2026; FAQ docs removed and llms.txt clarification 15 Jun 2026; review guideline 24 Jul 2026; VideoObject `creator` 24 Sep 2026; control-what-you-share 21 Oct 2026) | https://developers.google.com/search/updates |
| Google: Optimizing for generative AI features (updated 10 Jul 2026) | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide |
| Google: AI features and your website | https://developers.google.com/search/docs/appearance/ai-features |
| Google: Simplifying the search results page (Jun 2025) and update (Nov 2025) | https://developers.google.com/search/blog/2025/06/simplifying-search-results · https://developers.google.com/search/blog/2025/11/update-on-our-efforts |
| Search Engine Land on the Nov 2025 feature removals | https://searchengineland.com/google-to-remove-more-search-features-including-practice-problems-nutrition-facts-nearby-offers-and-more-464255 |
| Google: Control what you share | https://developers.google.com/search/docs/crawling-indexing/control-what-you-share |
| schema.org LegalService | https://schema.org/LegalService |
| Labour Codes in force 21 Nov 2025 (Khaitan & Co ERGO) | https://www.khaitanco.com/sites/default/files/2025-11/ERGO%20-%20Enforcement%20of%20Labor%20Codes%20-%2022%20November%202025.pdf |
| Labour Codes (KPMG flash) | https://www.in.kpmg.com/taxflashnews/KPMG-Flash-News-GOI-notifies-implementation-of-Labour-Codes.pdf |
| Income-tax Act 2025 in force 1 Apr 2026 (TaxGuru, citing CBDT) | https://taxguru.in/income-tax/income-tax-act-2025-force-1st-april-2026.html |
| DPDP Rules 2025 phased commencement (AZB & Partners) | https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/ |
| DPDP Rules (PIB document) | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf |
| GST 2.0 rates effective 22 Sep 2025 | https://taxguru.in/goods-and-service-tax/56th-gst-council-meeting-overview.html |
| LegalKart homepage (taglines, pricing) | https://www.legalkart.com/ |
| Vakilsearch homepage | https://vakilsearch.com/ |
| Rocket Lawyer homepage | https://www.rocketlawyer.com/ |
| Docusign homepage | https://www.docusign.com/ |
| LegalZoom homepage | https://www.legalzoom.com/ |
| Owner manuals (local) | /home/claude/ldpack/src/Manual_Documents.md · Manual_Pleadings.md · Manual_Compliance.md · Manual_Start_a_Business.md |

**Limitations:**
- The live site's body content could not be inventoried. It is a client-rendered SPA, and WebFetch receives only `<head>`. The H1s, copy, CTAs and FAQs of the live pages therefore remain unknown and should be exported from the site's CMS or codebase.
- The web-search quota ran out before exact-phrase plagiarism checks of the remaining manual text could be done.
- Verify the Income-tax Act 2025 and Labour Code section mappings against the Gazette.
