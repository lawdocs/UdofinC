# Phase P21 — Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `apps/public` scaffold, CDN, legacy-site inventory and the seed 301 map, host decision `https://www.lawdocs.in`); P01 (consent ledger and notice versions, OTP sign-up, account creation from the drafter); P02 (roles, maker-checker engine, screen and menu registry that carries `help_key` and `data-tour-id`); P03 (settings registry, rules register `rul` used for citations, stamp-duty and jurisdiction facts); P06 (published templates and questionnaires behind the "Draft free with Vidhi" block); P08 (instrument eligibility gate, Appendix F, for the eSign badge; State stamp registry); P09 runtime (Vidhi help mode and the content-drafting agent); P16 (marketplace catalogue, service tiers and professional rules rendered on public pages); P17 (plans, prices, credit packs, trial rules rendered on the pricing page); P19 core (`int` gateway for Operations Hub CRM, support desk, claims gate and asset library calls). External: Operations Hub OH3 (CRM), OH7 (marketing, social calendar, asset library), OH14 (claims gate); YouTube; Google Search Console and Bing Webmaster Tools; IndexNow; a plagiarism-check provider; `TRANSLATE_PORT` providers.
> **Sequencing:** Wave 1 delivers §4A–§4H core (site shell, rendering, multi-brand theming, 301 map, legal policies from Appendix O, pricing page, marketplace storefront shell, the top 50 content pages from Appendix N §N.9 wave 1, the CMS with DOCX import and blog, 150 glossary terms, the help panel framework and the accessibility statement). Wave 2 adds vlog, tutorials pipeline, guided tours, landing-page builder, Hindi plus four further D-07 languages and 350 glossary terms. Wave 3 completes the ≈626 manual-derived pages, the remaining D-07 languages, 500+ glossary terms, ISL tutorial renditions and the Consumer Help brand site. **First slice for the P00 cut-over:** the SSR shell, host rules and the redirect-target pages P00 needs (P00 §5.5, T−28 d) depend only on P00 and do not wait for P06; the "Draft free with Vidhi" blocks attach when P06 publishes templates, and until P16 exits (Wave 2) the storefront shell renders the P17 presentation catalogue (OH8 feed). Freeze points: the URL scheme (§4B) and the block schema (§4I) freeze at the end of sprint 2; after that, changes go through expand → migrate → contract (NN-12) with redirects.
> **Binding appendices:** N (website copy system, SEO/GEO, tutorials and video plan), O (legal policies), U (accessibility specification), M (marketplace professional rules), F (instrument eligibility), R (settings registry), D (roles), K (`LD-EXPORT-1.0`), H (agent roster), X (Operations Hub addendum: CRM, funnels, social calendar, asset library), Y (Ecosystem Spec v1.2 change request), W (open items).
> **Requirements covered:** R-004, R-008, R-016, R-019, R-020, R-025, R-030, R-032, R-036 (pricing page rendering), R-041 (open marketplace and academy entry), R-056 (funnel surfaces; OH is system of record), R-070, R-071, R-072, R-073, R-074, R-075 (public pages for added services), R-082 (startup section), R-086 (competitor-informed IA), R-087, R-088, R-089, R-090, R-091.
> **Decisions applied:** D-01, D-02, D-04, D-05, D-06, D-07, D-08, D-11, D-13, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-11, CH-12, CH-14, CH-20, CH-21, CH-30 · **Non-negotiables tested:** NN-02, NN-07, NN-11, NN-14, NN-18, NN-19, NN-20, NN-21, NN-22, NN-26, NN-28, NN-29, NN-30, NN-31, NN-32, NN-35, NN-38, NN-45, NN-48, NN-49, NN-50
> **Estimated effort:** 10 two-week sprints, squad of 8 (2 front-end, 1 back-end, 1 content engineer, 1 SEO/technical-content lead, 1 accessibility specialist (IAAP CPACC or WAS), 1 product designer, 1 QA), plus a standing content team of 4 (two legal writers, one technical writer, one video producer) and a reviewer of record (`PLT_LEGAL_REVIEWER`) for legal pages. Wave split: Wave 1 = 4 sprints, Wave 2 = 3, Wave 3 = 3.

---

## 1. Objective and business outcome

The live lawdocs.in is a client-side single-page application. A crawler or AI engine sees only a `<head>`: one title and one meta description on every URL, no H1, no body and no links (R5 §1.1). The sitemap lists non-www URLs that fail, `robots.txt` blocks `/buy/` while the sitemap lists 20 `/buy/*` URLs, and the positioning is compliance-first rather than documents, eSign and Vidhi. The manuals hold about 626 usable pages of content after de-duplication, but 21 sections contain copied competitor or Wikipedia text, the testimonials look adapted from proposal software, and much of the law is out of date (CrPC/IPC/Evidence Act, CPA 1986, Udyog Aadhaar, Income-tax Act 1961, pre-Code labour statutes) (R5 §3–§5).

This phase replaces that site with a server-rendered, multi-brand public website and a no-code content system, and builds the help layer that every authenticated app uses.

**Who benefits**

| Audience | Outcome |
|---|---|
| Individuals and small businesses | Find the right document, pleading or service in plain language; draft free from a vetted template; see whether eSign is legally valid for that instrument; see the full price before paying; hire a professional at a fixed price. |
| Companies and legal teams | Clear module, pricing and marketplace pages; tutorials and tours that shorten onboarding; contextual "i" explanations of legal and product jargon. |
| Search engines and AI answer engines | Unique, indexable, citable pages with answer-first summaries, visible FAQs, valid structured data, named reviewers and dated citations. |
| Users with disabilities | WCAG 2.2 AA and IS 17802 conformant pages, captions, transcripts, Indian Sign Language (ISL) renditions of core tutorials, easy-read summaries, a working feedback channel (Appendix U). |
| LawDocs operations (`OPS_CONTENT_PUBLISHER`) | Publish a blog post from a categorised Word file in under 10 minutes, with maker-checker and legal review, without a developer (R-089). |

**KPIs (measured from go-live of each wave)**

| KPI | Target |
|---|---|
| Indexable routes returning server HTML with a unique title, meta description, one H1 and ≥ 150 words of main content | 100% (CI-enforced) |
| Legacy URLs (186 sitemap URLs plus known indexed URLs) resolving 200 or a single-hop 301/410 | 100% |
| URLs passing Core Web Vitals at p75 on mobile (field data, Search Console) | ≥ 90% within 90 days of each wave |
| Published legal pages with a reviewer of record and a last-reviewed date | 100%; pages without one are `noindex` automatically |
| Pages failing the plagiarism gate at publication | 0 |
| Pages citing superseded law without a "(formerly …)" mapping | 0 (outdated-law linter) |
| DOCX → published blog post median time (publisher + checker) | ≤ 10 minutes of hands-on time |
| Lead captured → visible in Operations Hub CRM | ≤ 60 seconds p95 |
| Glossary coverage | 150 terms (Wave 1), 350 (Wave 2), ≥ 500 (Wave 3), each with plain definitions in all enabled D-07 languages |
| UI strings tagged as jargon without a registered "i" key | 0 (lint) |
| Automated axe-core serious or critical violations on any public template | 0; manual audit per Appendix U §U.8 each release |
| Free draft → paid action (eSign, eStamp, clean download or professional review) | ≥ 15% [target to calibrate — R4 §11.10] |

**Done for users** means: a visitor lands on `/documents/property-transactions/rent/rent-agreement-residential`, reads a 50-word answer, sees that eSign is valid, drafts the agreement in five to eight questions, sees the State stamp duty with its source and verification date, and either pays to eStamp and eSign or hires a professional, in ≤ 3 clicks from the page and with every fee shown separately before payment.

## 2. Scope (in / out)

**In scope**

1. `apps/public` (Next.js 16 App Router, SSR/SSG with incremental revalidation), multi-brand: **LawDocs** (`www.lawdocs.in`) and **`[Consumer Help Brand]`** (own host, own legal entity profile, D-06/NN-23).
2. Information architecture: the four manual sections (`/documents`, `/pleadings`, `/compliance`, `/start-a-business`), the fifth section `/regulated-entities` carried over from the live sitemap, `/advisory` practice areas, product pages (Vidhi, eSign and eStamp, Legal Vault, contracts and negotiation, litigation tracker, trademark tracker, company legal department), marketplace storefront, pricing, startup section, FinLegal Academy entry, Consumer Help entry, blog, vlog, help centre, glossary, free tools, legal policies (Appendix O), About, Partnership, Careers, Contact, Trust.
3. Page templates with the embedded **"Draft free with Vidhi"** and **"Hire a professional"** blocks (R-087), eSign eligibility badge, key-facts box, State variations, visible FAQs, testimonials without photos (NN-49), E-E-A-T footer.
4. Technical SEO: canonical host, sitemaps, robots and AI-crawler policy (NN-31), structured data, hreflang, Core Web Vitals budgets, IndexNow, the 301 migration map (seeded in P00, owned here from P21 onwards), optional `llms.txt`.
5. GEO for AI answers: definitions first, entity consistency, original data assets, citations, AI-answer monitoring.
6. No-code CMS (`web` module, Content Studio in `apps/console`): pages, blog posts from DOCX, categories, tags, authors, scheduling, SEO fields, maker-checker, legal-review flag, preview, rollback; vlog with YouTube privacy-enhanced embeds; landing-page builder for campaigns; lead capture to Operations Hub CRM with consent.
7. Help centre (`hlp` module): public help articles, in-app help panel for all apps, the "i" glossary registry, guided tours, the tutorial pipeline (text, annotated screenshots, diagrams, interactive artefacts, short captioned videos with ISL option) that also produces social-ready clips (R-020).
8. Accessibility statement, conformance report and feedback channel for the public site; the accessibility specification itself is Appendix U (binding on every phase).

**Out of scope (owner phase)**

| Item | Owner |
|---|---|
| Template content, questionnaires, assembly engine, AI Drafting Studio | P06 (this phase embeds them) |
| Vidhi runtime, guardrails, agent roster | P09, Appendix H |
| Instrument eligibility rules and State stamp registry data | P08, Appendix F |
| Plan, price, credit and trial data; checkout; GST invoices | P17 and OH8 (this phase renders) |
| Marketplace catalogue, engagements, professional registry, academy feed | P16 (this phase renders the storefront) |
| CRM, nurture sequences, Brevo, social calendar and posting, PR | Operations Hub (Appendix X); this phase hands off leads and assets through `int` |
| Consumer Help case flows (grievances, challans, vehicles) | P15 (this phase builds the brand site and its content pages) |
| Mobile app store listing copy and in-app help rendering on native | P22 (reuses `hlp` content and APIs) |
| Legal policy texts | Appendix O (this phase publishes and versions them) |
| Legacy platform decommissioning and data migration | P00 |
| Advertising stream (OFF by default) | P17 revenue-stream switch; placement rules here (NN-35) |

## 3. Personas and permissions touched

| Role code | What they can do in this phase (Appendix D governs) |
|---|---|
| Anonymous visitor | Browse every public page, search, use free tools, run a template questionnaire and see an on-screen preview, browse the marketplace (D-11), submit a lead or accessibility feedback with consent. |
| `IND_OWNER`, `ORG_*` (signed in) | All of the above plus: save a free draft to the vault, download a watermarked PDF (free plan), open the AI-custom lane, buy unlocks, open in-app help and tours, set accessibility and "i" preferences, submit verified testimonials. |
| `ORG_ADMIN` | Add tenant help notes to any `help_key`; set tour defaults for the tenant; view tenant terminology overrides in "i" popovers. |
| `OPS_CONTENT_PUBLISHER` | Maker for pages, posts, videos, landing pages, help articles, tutorials and tours: create, import DOCX, edit, set SEO fields, schedule, submit for review. Cannot approve own content (NN-18). Cannot edit legal policy pages, glossary legal definitions or price data. |
| `PLT_CONTENT_EDITOR` | Maker for glossary terms, legal page drafts, redirect rules, structured-data templates, entity registry; checker for publisher content that has no legal-review flag. |
| `PLT_LEGAL_REVIEWER` | Reviewer of record for content with the legal-review flag; approves glossary legal definitions, policy pages, document/pleading/service pages; their name and credential appear in the E-E-A-T footer. |
| `PLT_DPO` | Approves cookie/consent banner text, privacy notice versions, analytics vendor list; checker for consent-category changes. |
| `PLT_GRIEVANCE_OFFICER` | Receives escalated accessibility and content grievances; publishes Grievance Officer page details (D-08 values). |
| `PLT_SUPER_ADMIN` | Brand and host configuration, AI-crawler policy (maker; checker = `PLT_SECURITY_OFFICER` or a second super admin), kill switches for the drafter, lead capture and video embeds. |
| `PLT_SECURITY_OFFICER` | Checker for CSP/script allow-list, crawler policy and third-party embeds. |
| `OPS_SUPPORT_AGENT` | Reads accessibility feedback and help-article feedback; links them to support tickets in OH. |
| `OPS_QA_REVIEWER` | Runs the release accessibility audit and tutorial-staleness review; signs the conformance report. |
| `PRO_*` | Appear only as reviewers or authors through `ProfilePage` records with permitted fields (advocates: BCI Rule 36 fields only, NN-21). |
| `AGT_CONTENT_STUDIO` (Appendix H; X-27) | Maker only (NN-43): drafts rewrites, FAQs, metadata, translations and tutorial scripts into Draft state; never submits, approves or publishes. |

## 4. Functional requirements

### 4A. Public application, rendering, brands and hosts

- **FR-P21-01** `apps/public` is a separate Next.js 16 App Router application behind the CDN. It shares `packages/ui`, `packages/tokens`, `packages/i18n` and `packages/a11y` with the authenticated apps so the site and product look and behave alike.
- **FR-P21-02** Rendering: every indexable route is statically generated or server-rendered with incremental revalidation. Defaults (setting `web.render.revalidate_seconds`): home, product and section landings 3,600 s; hubs, document, pleading and service pages 86,400 s or on publish; blog and glossary 86,400 s or on publish; pricing and marketplace on catalogue-publish event from P16/P17. Interactive islands (drafter, tools, search, pricing toggle) hydrate progressively; all text, links, FAQs, tables and the H1 are in the server HTML.
- **FR-P21-03** No-JS gate: CI fetches every sitemap URL with JavaScript disabled and fails the build when `<main>` has fewer than 150 words (50 for tool and checkout-entry pages), lacks exactly one `<h1>`, repeats another URL's title or meta description, or lacks a self-referencing canonical.
- **FR-P21-04** Canonical host is `https://www.lawdocs.in` (setting `web.host.canonical`). Every request to `lawdocs.in`, `http://` or a trailing-slash variant 301s in one hop to the canonical form. Sitemaps, canonicals and hreflang use the same host. `lastmod` is the true last published-version timestamp, never a batch date (R5 §1.1).
- **FR-P21-05** Multi-brand: brand is resolved from the host (`web.brand.host_map`). Each brand has its own token set, logo, legal-entity profile (D-08 placeholders: CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer), policy set (Appendix O), analytics property, consent banner, sitemap, robots file and Organization schema. The `[Consumer Help Brand]` site (flag `web.brand.consumer_help.enabled`, default OFF) never renders LawDocsComply, Finbyx, Udofin or Equator product content, never cross-links to lender-facing products, and its lead hand-off carries the Consumer Help entity's `legal_entity_id` (NN-23).
- **FR-P21-06** Preview and staging hosts are `noindex, nofollow`, password- or SSO-protected and excluded from sitemaps. Authenticated hosts (`my.`, `work.`, `admin.`) send `X-Robots-Tag: noindex` on every response (NN-31).
- **FR-P21-07** Status page at `status.lawdocs.in` (built and operated by P19 FR-P19-82, hosted independently of the main stack — P00 FR-P00-19); this phase links it from the footer, help centre and in-app help panel.
- **FR-P21-08** Security headers: strict CSP with nonces, no inline event handlers, `frame-ancestors 'none'` except embeddable widgets on an explicit allow-list, SRI on any CDN script, HSTS preload, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` denying camera/microphone/geolocation on public pages. Third-party scripts load only from the allow-list approved by `PLT_SECURITY_OFFICER` and only after the matching consent (§4L). These controls also support PCI DSS SAQ A eligibility for pages that link to hosted checkout (R3 LG-148).
- **FR-P21-09** Kill switches (NN-39): `web.kill.drafter`, `web.kill.lead_capture`, `web.kill.video_embeds`, `web.kill.landing_pages` — each takes effect within 60 s, shows a graceful fallback block and writes an audit event.

### 4B. Information architecture and navigation

- **FR-P21-10** URL rules (R5 §2): lower-case, hyphens only, no underscores, no trailing hyphens, no stop-word sentences, typos corrected (`promissory-note`, `questionnaire`, `vakalatnama`). One canonical leaf per document; a document listed in two hubs is linked, not duplicated. Slugs are stable keys on canonical IDs (`pg_`), so renaming a category changes the breadcrumb label, not the URL (NN-12); a slug change creates a 301 automatically.
- **FR-P21-11** Site tree (counts from R5 §8.5; content in Appendix N):

| Section | Path pattern | Pages (recommended) |
|---|---|---|
| Documents | `/documents` → 18 category hubs → 134 sub-category hubs → 327 canonical document pages `/documents/{category}/{sub-category}/{document}` (duplicates are aliases with a 301 — P06 FR-P06-02, Appendix E) | 480 |
| Pleadings | `/pleadings` → 13 area hubs → 70 consolidated pleading pages `/pleadings/{area}/{pleading}` (variants as toggles; X-23) | 84 |
| Compliance services | `/compliance` → 7 group hubs → 22 service pages | 30 |
| Start a Business | `/start-a-business` → 6 group hubs → 26 service pages | 33 |
| Regulated entities | `/regulated-entities/{regulator}/{service}` (RBI, SEBI, IRDAI, other registrations, reporting) | ≈ 50 (carried from live sitemap) |
| Advisory practice areas | `/advisory/{area}` (banking and finance, capital markets, energy, fintech, insurance, sports) | 6 + hub |
| Product | `/vidhi-ai`, `/esign`, `/estamp`, `/legal-vault`, `/contracts`, `/litigation-tracker`, `/trademark-tracker`, `/legal-department`, `/for-individuals`, `/for-companies`, `/integrations`, `/data-portability`, `/security` | ≈ 15 |
| Marketplace storefront | `/marketplace`, `/marketplace/{category}`, `/marketplace/{category}/{service}`, `/marketplace/retainers`, `/marketplace/academy` | rendered from P16 |
| Pricing | `/pricing`, `/pricing/enterprise`, `/pricing/credits` | 3 |
| Startups | `/startups` (registration, founder kit, legal officer on retainer, trademarks, funding documents — R-082) | 1 hub + 6 guides |
| Consumer Help entry | `/consumer-help` on lawdocs.in (one explainer + link to the separate brand host when enabled); full site on brand host | 1 (+ brand site) |
| Blog, vlog | `/blog`, `/blog/{category}`, `/blog/{category}/{slug}`, `/videos`, `/videos/{slug}` | CMS |
| Help, glossary, tutorials | `/help`, `/help/{topic}/{slug}`, `/glossary`, `/glossary/{slug}`, `/tutorials/{slug}` | CMS/`hlp` |
| Free tools | `/tools/{tool}` (stamp-duty estimator, eSign eligibility checker, limitation-period calculator, notice-period and gratuity calculator, trademark class finder, old→new criminal-law section finder) | 6 |
| Company and legal | `/about`, `/team`, `/partnership`, `/careers`, `/contact`, `/press`, `/trust`, `/accessibility`, `/legal/{policy}` (Appendix O), `/grievance-officer`, `/ranking-parameters` | ≈ 20 |

- **FR-P21-12** Launch triage (R5 §2): pages with body copy and a defined document list are published in their wave; the 63 sub-hubs with undefined document lists publish as hubs with a Vidhi "describe your situation" box and a "Hire a professional" strip until documents are defined; the 48 stubs and "(upcoming)" placeholders are not published (no `noindex` thin pages in the sitemap). A page cannot publish below the minimum content rule for its type (Appendix N §N.3).
- **FR-P21-13** Top navigation, maximum seven items, each an accessible disclosure menu (click/Enter/Space; never hover-only): **Documents**, **Court & Notices** (pleadings, notices, litigation tracker), **Business** (start a business, compliance, regulated entities, advisory, startups), **Product** (Vidhi, eSign/eStamp, vault, contracts, trackers, legal department), **Marketplace**, **Pricing**, **Resources** (blog, videos, help, glossary, tools, tutorials). Utility bar: Search, language switcher, accessibility preferences, Log in, "Start free".
- **FR-P21-14** Issue-first entry tiles on home and section landings (R1 §3.7): plain-language situations ("Renting out a flat?", "Cheque bounced?", "Starting a company?", "Received a legal notice?", "Trademark objection?") mapped to the canonical page, configurable by `OPS_CONTENT_PUBLISHER` without code.
- **FR-P21-15** Mobile navigation: one menu button opens a full-height dialog with the same tree as nested disclosure lists; focus trapped while open and restored on close; a sticky bottom bar with "Draft free" and "Hire a pro" never obscures focused content (WCAG 2.4.11).
- **FR-P21-16** Footer: section columns, legal pages, Grievance Officer details (IT Rules 2021 r.3(2) as amended [VERIFY current text and the 20 Feb 2026 amendment — R3]), DPO or designated contact (DPDP), entity identity (D-08 values), one public phone number (setting `web.contact.public_phone` [OWNER]: R5 found three numbers in use), `security.txt`, status page, accessibility statement, ranking-parameters page for the marketplace (Consumer Protection (E-Commerce) Rules 2020 r.5 [VERIFY sub-rule], R3 LG-141).
- **FR-P21-17** Breadcrumbs on every page below a landing, as visible links and `BreadcrumbList`.
- **FR-P21-18** Site search (OpenSearch public index containing published public content only; PostgreSQL FTS fallback): typo tolerance, Indic analyzers and transliteration for D-07 languages, synonyms including old→new law pairs ("CrPC 438" ↔ "BNSS 482", "Section 65B" ↔ "BSA 63"), result types (document, pleading, service, guide, video, glossary, help), keyboard-operable results with a live-region count. Search result pages are `noindex`.
- **FR-P21-19** Cross-linking rules (hub-and-spoke model, Appendix N §N.6): every leaf links up to its hub, sideways to 4–6 related leaves, across to the matching pleading/service/document and to one guide and one video; every hub links to all of its leaves; orphan detection fails the publish of a hub change that would leave a leaf with zero inbound links.

### 4C. Page templates

Each template is a typed block schema (§4I) with its own minimum content rule, structured-data mapping (§4E) and editorial checklist (Appendix N §N.3). Word counts are minima for the original body, excluding FAQs.

- **FR-P21-20 Document page** (blocks in order; R5 §7.2): breadcrumb; owner one-liner as eyebrow (not the H1); H1 `[Document name] — Draft Free, eSign Online` or `— Draft Free, Print and Register` when not eSign-eligible; answer-first summary 40–60 words (what it is + which law + who uses it); key-facts box (governing law, stamp duty pointer, registration required, witnesses, notarisation, **eSign valid: Yes / Check / No** from Appendix F, typical time, law as of); **Draft free with Vidhi** (§4D); **Hire a professional** (§4D); what's included (8–15 clause bullets with purposes; "Neutral by design"); requirements table; process steps (ordered list); State variations table (top 10 States, each row with source link and verified-on date, plus a State selector); stamp and registration consequences; FAQs (5–8, visible); related links; testimonials (if any qualify, §4D); E-E-A-T footer; disclaimer and grievance links. Minimum original body 400 words.
- **FR-P21-21 Pleading page** (R5 §7.3): H1 with current statute and the former provision in brackets (e.g., "Anticipatory Bail Application under Section 482 BNSS (formerly Section 438 CrPC)"); answer-first summary; key facts (court/forum, statute, limitation, court fee pointer, annexures, e-filing portal); variant toggles (forum, State, religion or personal law, petitioner type) that switch content without creating URLs; **Draft free with Vidhi** ("Prepare a first draft"); **File through an advocate** variant of the hire block — pleadings are signed and verified by the party and filed through an advocate where the forum requires it (NN-41); partial draft preview; annexure checklist; old→new section mapping box (R5 §5); savings-clause note for pre-1 July 2024 proceedings (BNSS s.531); FAQs; related documents (vakalatnama, affidavit, surety); litigation-tracker CTA; E-E-A-T footer. Minimum 450 words.
- **FR-P21-22 Service page** (compliance, start a business, regulated entities, advisory): H1 `[Service] Online` with the outcome; one-liner; answer-first summary; **price card rendered from P16/P17** with professional fee, LawDocs platform fee, government fee or stamp duty at actuals and GST shown separately, and the total before payment (NN-22); timeline; eligibility; documents required; process; post-service compliance calendar where relevant; comparison table where relevant (Pvt Ltd vs LLP vs OPC); FAQs; matching document packs; reviewed-by (CS, CA or advocate as appropriate). Minimum 400 words.
- **FR-P21-23 Category hub**: H1; one-liner; 60–80-word category definition; sub-category grid (one-liner and one-line description each); "Most used" eight documents (ordered by published popularity metric, never paid placement); Vidhi "describe your situation" box; hire strip; 4–6 hub FAQs; guides and videos; related services; reviewed-by.
- **FR-P21-24 Sub-category hub**: H1; one-liner; answer-first explainer 150–300 words; document list with a one-line "use this when…" each; requirements table; comparison table where useful; FAQs; related pleadings and services.
- **FR-P21-25 Comparison page** (`/compare/{a}-vs-{b}`, e.g., rent agreement vs leave and licence vs lease; Pvt Ltd vs LLP vs OPC; Aadhaar eSign vs DSC; LawDocs plans): a factual table with a citation per legal row; an "If you…, choose…" decision list; no competitor brand comparisons unless every claim cites a dated public source and passes the claims gate (NN-20). Minimum 500 words.
- **FR-P21-26 Glossary term page** (`/glossary/{slug}`): term, abbreviation, plain definition (≤ 40 words, reading grade ≤ 8), detailed explanation (≤ 250 words), legal definition quoted with citation when defined in law, example, related terms, "Where you see it in LawDocs", related page links; `DefinedTerm` in a `DefinedTermSet`. Generated from `hlp` (§4N), not typed into the CMS.
- **FR-P21-27 State variant page** (`/documents/{…}/{document}/{state}`): permitted **only** when the variant passes the materiality test: at least `web.state_variant.min_distinct_facts` (default 3) legally material facts that differ from the national page and are recorded as structured facts with sources in `rul` (for example a State-specific statute such as the Maharashtra leave and licence regime, a distinct stamp-duty article, a mandatory State form, a distinct registration rule), plus ≥ 250 words of original State-specific copy. The CMS blocks publication otherwise (`LD-WEB-009`). Variants without a material difference stay as rows in the national page's State table. Never create 36 State clones of each page (scaled-content abuse; R5 §7.1).
- **FR-P21-28 City page**: OFF (`web.city_pages.enabled`). When enabled, a city page needs a real office or a genuinely local fact set (local forum addresses, registration office practice) and the same materiality test; "lawyer in {city}" pages are prohibited because LawDocs does not advertise individual advocates (BCI Rule 36; R3 LG-111, LG-113; CH-08). The six live `/compliance-services/consult-lawyer/{city}` URLs 301 to `/marketplace/legal-consultation` (§4E).
- **FR-P21-29 Marketplace storefront**: renders the P16 catalogue (D-11): categories, service cards with fixed scope, turnaround, professional type, full fee breakdown, provider identity and GSTIN where the provider is a third party (E-Commerce Rules r.5 [VERIFY]), retainers, FinLegal Academy course cards that link out to `trainings.lawdocs.in` (D-16; no paid course content copied), and LawDocsComply services. Browsing needs no login. No advocate ratings, rankings, testimonials, photos or "book this advocate" (NN-21; Appendix M); neutral ordering (alphabetical or a logged seeded random); the ranking-parameters page explains ordering.
- **FR-P21-30 Pricing page**: renders P17 data — three plans (Personal, Pro, Business) with feature lists, plus Free and Enterprise links; monthly vs annual toggle with the formula shown; credit packs (eSign, AI, eStamp facilitation); renewal and cancellation terms and the cancellation path shown before payment (NN-50); GST treatment stated; "services without a subscription" entry (R-040); plan-benefit explainer (R-042); FAQs. Prices never typed in the CMS. No countdown timers, no pre-selected add-ons, no "most popular" label unless backed by a claims-register metric.
- **FR-P21-31 Startup section** (`/startups`): founder journey (idea → entity → registrations → IP → founder documents → funding documents → first-year compliance), each step linking to the canonical service or document page; "Legal officer on retainer" offer from P16; founder kit (founders' agreement, ESOP plan and grant letter, NDA, term sheet) as template-lane drafts; startup FAQs.
- **FR-P21-32 Company pages**: About (entity facts from D-08 profile, mission, Infrabyx Group relationship stated plainly), Team (consented profiles; advocates Rule 36 fields only), Partnership (CA/CS/law-firm, incubator, dealer and broker programmes as described in Appendix X; no referral reward on advocates' fees — NN-21), Careers (jobs feed from OH; equal-opportunity and accessibility statement for applicants), Contact (one phone number, email, office addresses with `LegalService` per real office, accessible map alternative text, contact form → OH CRM), Press, Trust (security, privacy, sub-processors, data residency, certification status phrased through the claims gate).
- **FR-P21-33 Free tool page** (`/tools/{tool}`): deterministic calculators whose rules come from `rul`/P08 (stamp-duty estimator with source and verified-on date per State, eSign eligibility checker from Appendix F, limitation calculator from the Limitation Act 1963 Schedule rows held in `rul` [VERIFY rows at build], gratuity and notice-period calculators from the labour rulepack, trademark class finder from the Nice classification held in `ipm`, old→new criminal-law section finder from R5 §5 mappings). Each tool shows "General information, not legal advice", its inputs, formula and sources, and an accessible text result. No AI in tools.
- **FR-P21-34 Legal policy page** (`/legal/{policy}`): renders Appendix O texts with version, effective date, change summary and prior versions; material changes trigger consent re-prompts in the apps through the P01 consent ledger; policy pages are edited only by `PLT_CONTENT_EDITOR` with `PLT_LEGAL_REVIEWER` (and `PLT_DPO` for privacy and cookie notices) as checker.

### 4D. Embedded conversion and trust blocks

- **FR-P21-35 "Draft free with Vidhi" block** (R-087, CH-30). Two lanes, always labelled:
  1. **Template lane (free, template automation):** a 5–8-question questionnaire from the P06 published template bound to the page (`tpl_` id in page metadata). Anonymous visitors see an on-screen preview; a free account saves the draft to the Legal Vault and downloads a watermarked PDF; paid unlocks (clean DOCX/PDF, eStamp, eSign, negotiation) follow P17 entitlements. This is assembly of a vetted template from the user's answers, not AI advice (NN-14). Each clause has an "i" explanation.
  2. **AI-custom lane (signed in):** "Ask Vidhi to adapt this" opens the P06 Drafting Studio with the template preloaded. The output is labelled **"AI draft — not reviewed by a professional"** until a qualified reviewer approves, with a one-click paid review offer; AI use is disclosed at the start (NN-14; Anthropic Usage Policy high-risk legal use [VERIFY effective date — R4 §6.4]).
  If the page has no published template, the block shows the Vidhi "describe your situation" box (AI-custom lane only) plus the hire block. If the template is withdrawn in P06, the block hides within one revalidation cycle and shows the hire block only. Click budget: page → first question ≤ 1 tap; questionnaire → preview ≤ 8 answers; preview → saved in vault ≤ 2 taps (OTP sign-up inline). Anonymous use is rate-limited (`web.drafter.anon_runs_per_day`, default 3 per device/IP) with an accessible, non-visual challenge fallback (no image-only CAPTCHA — WCAG 3.3.8).
- **FR-P21-36 eSign eligibility badge**: every document page reads Appendix F through P08's API: **Valid** (Aadhaar eSign available), **Check** (interest in immovable property or stamping requirement — show the condition), **Not valid** (IT Act 2000 s.1(4) and First Schedule as amended — wills, trusts, ordinary powers of attorney, negotiable instruments other than cheques, and any other excluded entry [VERIFY entries — R3 §1]). For **Not valid**, the eSign CTA is replaced with "Print, sign, stamp and register" and the wet-ink/notary/registration pack offer (NN-07, CH-12). The R5 CSV flags (250 valid, 62 check, 35 not valid) seed page metadata, but the live badge always comes from Appendix F at render.
- **FR-P21-37 "Hire a professional" block**: 2–3 fixed-price tiers from P16 (e.g., Review · Draft and review · Draft, stamp and registration assistance) with turnaround, professional type (advocate, CS, CA, tax practitioner), what is included, and a fee breakdown (professional fee, LawDocs platform fee, government fee or stamp duty at actuals, GST, total) before payment (NN-22). The professional is assigned by LawDocs as a service; no individual advocate is named, pictured, rated or advertised (NN-21, Appendix M). Pleading pages use the "File through an advocate" wording. CA/CS-delivered tiers appear only when P16's professional switches allow them. A secondary "Talk to us about a retainer" link opens the lead form.
- **FR-P21-38 Testimonials** (NN-49, CH-20, R-088): only from verified purchasers (linked to a completed order or signed document), about **LawDocs or its product**, never about an advocate or a specific advocate's work; consent captured and stored (P01 consent artefact) with the displayed text; displayed as plain text with first name and initial, city, role ("tenant, Jaipur"), month and year, and a "verified customer" tag; **no photos** (`web.testimonials.photos_enabled` default OFF; Locked OFF on any page that mentions advocates or court work); no star markup; any consideration given is disclosed; negative reviews are not suppressed from the testimonials pool (IS 19000:2022 principles; CCPA Misleading Advertisements and Endorsements Guidelines 2022 — R3 LG-143). A page shows testimonials only when relevant approved ones exist; no filler. The 10 adapted testimonials found in the manuals are never published (R5 §4 row 12).
- **FR-P21-39 FAQ block**: 5–8 questions per leaf, each answer ≤ 60 words, answer-first, cites a provision where legal, links to the canonical page; rendered as visible HTML (`<h3>` question + `<p>` answer, or `<details>` with the answer present in the DOM and expanded for no-JS and print). Questions are sourced from Search Console, People Also Ask, Vidhi chat logs (aggregated, de-identified) and support tickets. Placeholder FAQs ("Educate on what is ?") are blocked at publish.
- **FR-P21-40 Key-facts and State-variation tables** are bound to structured data in `rul`/P08 (stamp duty article, rate, registration fee, e-stamping availability, source URL, verified-on date). A row whose verification is older than `web.facts.max_age_days` (default 180) shows "Verification due" and the page enters the review queue.
- **FR-P21-41 E-E-A-T footer**: "Reviewed by {name}, {credential} ({enrolment or membership number where the professional consents}); last reviewed {date}; next review {date}"; author; change log (date, what changed); "Legal basis" list linking to India Code or the regulator's primary source; disclaimer ("General information, not legal advice"); grievance and privacy links.
- **FR-P21-42 Related block**: 4–6 related leaves, the matching pleading/service/document, one guide, one video, one glossary term; computed from the hub-and-spoke model with editorial overrides.
- **FR-P21-43 Owner one-liners**: each page carries one approved line from the one-liner bank (Appendix N §N.2) as an eyebrow and an optional CTA line in the "[Verb] [object], now." formula. Borrowed or quoted lines are blocked (R5 §6.1).
- **FR-P21-44 Advertising slots** exist in the block schema but render nothing unless the P17 advertising stream is ON (D-13, NN-35); when ON, slots render only on blog, vlog and learning pages, labelled "Sponsored", contextual only, never on document, pleading, service, pricing, marketplace, help, Consumer Help or legal pages, and never for advocates.
- **FR-P21-45** Every block that shows a number, certification, partner logo, customer name or comparative statement resolves it through the claims gate (OH14 `GET /v1/claims-gate/check` via `int`, cached per build) and the local claims register; unapproved claims block publication (`LD-WEB-002`; NN-20). Locked phrases include "government-approved", "verified lawyers" (unless the verification record exists and the wording is approved), "real-time court data", "best lawyer", "100% legal", "guaranteed outcome".

### 4E. Technical SEO, structured data and the 301 map

- **FR-P21-46** Metadata rules per page (Appendix N §N.7): title ≤ 60 characters, unique, `[Primary intent] — [qualifier] | LawDocs`; meta description ≤ 155 characters, unique; one H1; Open Graph and X/Twitter cards with a generated social image (title + one-liner, brand tokens, alt text); `robots` meta from page state.
- **FR-P21-47** Structured data is generated from page data, never hand-typed, and must match visible content. Matrix:

| Page type | JSON-LD types |
|---|---|
| Sitewide | `Organization` (legal name, logo, `sameAs`, `contactPoint`), `WebSite` |
| Document page | `WebPage`, `BreadcrumbList`; `Product` + `Offer` only where the page sells a fixed-price downloadable template with a real price; `Service` + `Offer` for each hire tier with a fixed price; `FAQPage` only per FR-P21-49 |
| Pleading, service, regulated-entity, advisory page | `WebPage`, `BreadcrumbList`, `Service` (`provider` = Organization; `serviceType`; `areaServed` = India) + `Offer` for fixed prices |
| Hub | `CollectionPage`, `BreadcrumbList`, `ItemList` |
| Office/contact | `LegalService` (LocalBusiness subtype) per real office with name, address and phone matching the Google Business Profile; never for virtual or city pages |
| Blog post | `BlogPosting` or `Article` with `author` and `reviewedBy` linked to `ProfilePage` |
| Vlog/tutorial video | `VideoObject` (name, description, thumbnailUrl, uploadDate, duration, embedUrl, `creator`, transcript reference) |
| Glossary | `DefinedTerm`, `DefinedTermSet` |
| Author/reviewer | `ProfilePage` + `Person` (advocates: BCI Rule 36 fields only) |
| Pricing | `WebPage` + `Offer` per plan with price and `priceCurrency` INR |

  Never emit `Review`, `AggregateRating` or star markup for LawDocs itself (self-serving; R5 §7.1), `HowTo`, or `Course` (retired; R5 §1.3). CI validates every template against schema.org and the Rich Results Test API equivalents; invalid markup blocks publish (`LD-WEB-006`).
- **FR-P21-48** Answer-first summaries are stored as a distinct field (`summary_answer`, 40–60 words) so they render first under the H1, feed the meta description fallback and feed `llms.txt` and the AI-answer monitor.
- **FR-P21-49** FAQPage markup: setting `web.schema.faqpage_mode` ∈ {`OFF`, `VISIBLE_ONLY`}, default `VISIBLE_ONLY`: emitted only when the same Q&A is visible on the page. Google stopped showing FAQ rich results from 7 May 2026 (R5 §7.1 [VERIFY on Search Central at build]); the markup is kept for other engines at no cost. Visible FAQs remain mandatory.
- **FR-P21-50** Sitemaps: index sitemap per brand with child sitemaps by section and locale (≤ 10,000 URLs each), only `index`-state canonical URLs with true `lastmod`; video sitemap for `/videos` and `/tutorials`; submitted to Search Console and Bing Webmaster; IndexNow ping on publish, update and unpublish (`web.indexnow.enabled`).
- **FR-P21-51** `robots.txt` per brand generated from settings: allow Googlebot and Bingbot; AI search-retrieval bots (OAI-SearchBot, PerplexityBot, Claude-SearchBot and equivalents) per `web.crawl.ai_search_bots_allowed` (default allow); AI training bots (GPTBot, ClaudeBot, CCBot and equivalents) per `web.crawl.ai_training_bots_allowed` (default disallow [OWNER — board decision, R5 §7.4]); `Google-Extended` per `web.crawl.google_extended_allowed` (default disallow [OWNER]); disallow `/checkout`, `/account`, `/preview`, search results, API paths. Changing any crawler setting is maker-checker (NN-18, NN-31). The user-agent list is data, refreshed quarterly [VERIFY current bot names].
- **FR-P21-52** `llms.txt` (optional, `web.llms_txt.enabled` default ON): a short Markdown index of section landings, top hubs, pricing, policies and contact, generated at build. It is not a ranking lever (Google says it does not use it — R5 §7.1).
- **FR-P21-53** 301 migration map (`web.redirects`): seeded by P00 from the legacy inventory; owned here thereafter. Rules (R5 §1.2, §2): non-www → www; `/smartdrafts/{a}/{b}` → `/documents/{a'}/{b}`; `/compliance-services/business-registration/*` → `/start-a-business/*`; `/compliance-services/roc/*` → `/compliance/roc-compliances/*`; underscore slugs (`/compliance-services/rbi_*`, `irdai_*`, `sebi_*`) → `/regulated-entities/{regulator}/{service}`; 18 feature-bullet URLs under `business-legal-consultation`, `personal-…`, `property-…` → parent page (301) or 410 where no equivalent exists; `/compliance-services/audit/*` sentence slugs → `/compliance/audit/{service}`; `/compliance-services/consult-lawyer/*` → `/marketplace/legal-consultation`; `/mortgage/`, `/services/consult-lawyer`, `/legal`, `/talk-to-lawyer` → canonical equivalents; `/buy/*` → `noindex` checkout entries removed from sitemaps, with 301 to the matching document page for any indexed `/buy/*` URL; `/terms/Disclaimer` → `/legal/disclaimer`. Single hop only; chains and loops are rejected (`LD-WEB-005`). CI asserts every legacy URL resolves 200, 301 or 410. Redirect changes are maker-checker and emit `in.lawdocs.web.RedirectMapPublished.v1`.
- **FR-P21-54** Faceted and filter URLs (marketplace filters, blog tag combinations) are `noindex, follow` and canonicalise to the unfiltered page; only curated tag pages with ≥ 5 posts and an intro are indexable.
- **FR-P21-55** Core Web Vitals budgets (p75 mobile, field data; lab gates in CI with Lighthouse CI on a throttled mid-range profile): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, TTFB ≤ 0.8 s. Asset budgets: content-page JavaScript ≤ 150 kB compressed; drafter island ≤ 250 kB lazy-loaded below the fold on desktop and on interaction on mobile; images AVIF/WebP with explicit dimensions and `srcset`; fonts self-hosted Noto subsets per script loaded only for the active locale, `font-display: swap`; no layout-shifting consent banner (reserved space or overlay that does not shift content). A budget regression fails CI.
- **FR-P21-56** Images: alt text required for informative images; decorative images explicitly marked; generated diagrams have a text alternative or adjacent data table; no text baked into images except logos.
- **FR-P21-57** Monitoring: Search Console (including the generative-AI performance report where available [VERIFY]), Bing Webmaster, server-log analysis of crawler and AI-bot hits by user agent and path (aggregated, no IP retention beyond the CERT-In log policy — NN-27, NN-32), 404 and soft-404 reports, redirect-hit counts so stale redirects can be reviewed after 12 months.
- **FR-P21-58** Pages in `HOLD`, `DRAFT`, `IN_REVIEW` or without a reviewer of record are `noindex` and excluded from sitemaps automatically (`web.review.auto_noindex_without_reviewer`, Locked ON).

### 4F. E-E-A-T, legal accuracy and content governance

- **FR-P21-59** Reviewer of record: every page of type document, pleading, service, regulated-entity, advisory, comparison, tool and every blog post flagged legal carries `reviewed_by` (a `PLT_LEGAL_REVIEWER` or an engaged `PRO_*` with a `ProfilePage`), `reviewed_at`, `next_review_at` (setting `web.review.max_age_days.<type>`: document 365, pleading 180, service 180, regulated-entity 120, blog 365). Overdue pages enter the review queue; 30 days after overdue they show "Review due" and, after 60 days, revert to `noindex` until reviewed.
- **FR-P21-60** Citation resolver: legal citations in page bodies are entered as structured references (`{instrument, provision, version}`) and resolved against the rules register (`rul`, P03) or a primary-source URL (India Code, RBI, SEBI, MCA, CBIC, CBDT, IRDAI, e-Courts). Unresolved citations render as "unverified" and block publication of legal page types (`LD-WEB-016`; NN-14 principle applied to content).
- **FR-P21-61** Outdated-law linter (R5 §5): a dictionary of superseded instruments and section mappings (CrPC → BNSS, IPC → BNS, Evidence Act → BSA, CPA 1986 → CPA 2019, Companies Act 1956 → 2013, Listing Agreement → SEBI LODR 2015, Udyog Aadhaar → Udyam, GSTR-2/3 → current returns, s.35(5) CGST audit → omitted, Income-tax Act 1961 → Income-tax Act 2025 with dual citation during transition [VERIFY new section numbers], pre-Code labour statutes → the four Labour Codes) flags each occurrence with the suggested replacement and requires either the current provision with "(formerly …)" or an explicit reviewer note (e.g., savings clause). Blocking for legal page types.
- **FR-P21-62** Plagiarism gate (`PLAGIARISM_PORT`): every legal page body and blog post is checked before review; similarity above `web.plagiarism.max_similarity_pct` (default 10% excluding quotations of statutes and properly attributed quotes) blocks submission (`LD-WEB-003`). A competitor-brand and link detector (Vakilsearch, Corpbiz, Provenience, LegalWiz, LegalRaasta, ebizfiling, Registrationwala, enterslice, toppr, eximguru, upcounsel, legaldocs.co.in and Wikipedia links — R5 §4, list held as data) blocks publication until removed. Outbound links to non-primary sources need editor justification.
- **FR-P21-63** Law-change sweeps: when a rules-register item linked to a page changes (P03 event), the page and linked glossary terms enter the review queue with the diff (`in.lawdocs.web.LawChangeFlagged.v1`). Quarterly sweep reports list pages by instrument (RBI master directions, Labour Code rules, Income-tax Act 2025 rules, Stamp Acts).
- **FR-P21-64** Practice notes and original data: page types support "What we see go wrong" practice notes (from the in-house team), anonymised platform statistics (from the claims register only, with k-anonymity ≥ 30), original State stamp-duty matrices and old→new law maps. These are the non-commodity assets AI engines cite (R5 §7.4).
- **FR-P21-65** Machine translation of legal text (NN-48): translations are drafted through `TRANSLATE_PORT`, labelled "Machine-translated draft" in the CMS, and published only after a human reviewer for that language approves; legal policy translations state that the English version prevails [COUNSEL]. A locale page without an approved translation does not exist (no hreflang to it).
- **FR-P21-66** Content audit trail: every create, edit, import, review decision, publish, unpublish, rollback and redirect change writes the audit ledger in the same transaction (NN-02, NN-45).

### 4G. GEO for AI answers

- **FR-P21-67** Definitions first: the first sentence under the H1 states what it is, which law governs it and who uses it; each H2 section opens with a self-contained answer sentence so passages can be quoted out of context.
- **FR-P21-68** Entity consistency registry (`web.entities`): canonical names and descriptions for "LawDocs", "Vidhi AI", "Infrabyx Group", "FinLegal Academy", "Equator", "LawDocsComply", `[Consumer Help Brand]`, each office, and each product; used by copy lint (flags variants such as "Law Docs", "Vidhi bot"), by `Organization.sameAs` and by social profiles.
- **FR-P21-69** Semantic HTML only: headings in order, real tables with `<th scope>`, ordered lists for steps, `<dfn>` for defined terms, `<abbr>` with expansions on first use, short paragraphs (≤ 4 sentences).
- **FR-P21-70** AI-answer monitoring: a fixed panel of prompts per cluster (Appendix N §N.8) is run monthly against major answer engines by the SEO lead (manually or through a licensed monitoring tool [VERIFY terms]); results (cited or not, accuracy of the answer about LawDocs) are logged to `web.geo_checks`; inaccuracies create content tasks. No automated scraping of answer engines that breaches their terms.
- **FR-P21-71** Freshness signals: "Law as of {date}" in key facts; visible "Updated {date}: {what changed}" in the change log; `dateModified` only on substantive changes (typo fixes do not bump it).

### 4H. Internationalisation (D-07)

- **FR-P21-72** Locales: `en-IN` (default, unprefixed), `hi`, `bn`, `mr`, `te`, `ta`, `gu`, `kn`, `ml`, `pa` as path prefixes (`/hi/documents/...`). Slugs stay English for stability (NN-12); the H1, title, body and breadcrumb labels are translated. Each locale is enabled per section by `web.locale.<code>.sections` once the section's translation completeness is ≥ 95% and human review is complete.
- **FR-P21-73** hreflang clusters (`en-IN`, `hi-IN`, …, `x-default` → English) only among pages that exist and are reviewed in each locale; reciprocal tags validated in CI; language switcher keeps the user on the equivalent page or explains that the page is not yet available in that language (no silent redirect to home).
- **FR-P21-74** Fonts: Noto Sans and Noto Serif subsets for Devanagari, Bengali, Gurmukhi, Gujarati, Tamil, Telugu, Kannada and Malayalam scripts, loaded only for the active locale; line-height and font-size tokens tuned per script; no text in images.
- **FR-P21-75** Locale priority by wave: Wave 1 English; Wave 2 Hindi for home, product, pricing, top 50 pages, legal policies, glossary plain definitions, help top 50 articles, plus Bengali, Marathi, Tamil and Telugu for glossary and help; Wave 3 all ten D-07 languages for glossary, help, top 150 pages and policies.
- **FR-P21-76** Number, date and currency formatting through `packages/i18n` (Indian digit grouping, ₹, DD MMM YYYY); legal citations are not translated (section numbers and instrument names stay as enacted, with a translated gloss).

### 4I. No-code CMS — Content Studio (`web` module)

The Content Studio is a route group in `apps/console` (`admin.lawdocs.in/content`). `OPS_CONTENT_PUBLISHER` holds a scoped console membership that exposes only the Content Studio (Cerbos policy `web.content_studio`); platform administration stays hidden. Rationale: glossary, template and policy editors (`PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER`) already work in the console, and one review queue spans their content and the publisher's.

- **FR-P21-77 Content model**: `page` (type, brand, canonical slug, locale, state), `page_version` (immutable snapshot of blocks, metadata, SEO fields, structured-data inputs, reviewer), `block` (typed, validated against JSON Schema 2020-12; unknown types rejected at save), `post` (blog; extends page with category, tags, authors, reading time), `video` (`vid_`), `landing` (campaign page with variants), `asset` (media with alt text, credit, licence, hash), `author` (ProfilePage person), `category`, `tag`, `redirect`, `claim_ref`, `experiment`. Block library: hero, rich text, answer summary, key facts, drafter embed, hire embed, eSign badge, requirements table, process steps, State table, comparison table, FAQ, testimonial, related, CTA, video, image, diagram (Mermaid/SVG source), callout, quote (with attribution), pricing embed, marketplace embed, tool embed, form, practice note, ad slot (inert unless NN-35 allows).
- **FR-P21-78 Editorial workflow** (§5.1): `DRAFT → IN_REVIEW → (LEGAL_REVIEW) → APPROVED → SCHEDULED → PUBLISHED → SUPERSEDED | UNPUBLISHED`, plus `HOLD`. Maker ≠ checker, enforced (`LD-WEB-015`; NN-18). The legal-review flag inserts the `LEGAL_REVIEW` step with `PLT_LEGAL_REVIEWER` as checker; it is set automatically for page types document, pleading, service, regulated-entity, advisory, comparison, tool and policy, and for any post where the linter detects statutory citations, legal-advice phrasing or a category marked legal; a publisher may add it but cannot remove an automatic flag.
- **FR-P21-79 DOCX import** (R-073, R-089): the publisher uploads one `.docx` or a `.zip` of a categorised folder tree (the owner's Word-file folders). Pipeline (Temporal workflow `DocxImportWorkflow`):
  1. Virus scan, size check (`web.cms.docx_import.max_mb`, default 25), macro and external-object stripping; `.doc` files are converted to `.docx` through Gotenberg/LibreOffice first.
  2. Tracked changes and comments: if present, the import stops with `LD-WEB-008` and the options "Accept all changes and drop comments" or "Cancel" (the choice is logged).
  3. Semantic conversion: Word styles map to blocks (Title/Heading 1 → H1 candidate, Heading 2–4 → H2–H4, lists → lists, tables → semantic tables with the first row as headers after confirmation, footnotes → endnotes with back-links, hyperlinks kept, images → media library with **required alt text** before submit). Inline styles, fonts, colours and empty paragraphs are discarded; output is sanitised HTML on an allow-list, then mapped to blocks.
  4. Folder → taxonomy: the folder path maps to blog category and tags through `web.cms.folder_category_map` (Appendix N §N.11 [OWNER to supply folder list]); unmapped folders are proposed as new categories for `PLT_CONTENT_EDITOR` approval, never created silently.
  5. Lint pass: single H1, heading order, link check, outdated-law linter (FR-P21-61), competitor-brand detector and plagiarism gate (FR-P21-62), claims detection (numbers, "certified", "best"), reading-level warning (grade > 10 for consumer categories), placeholder text detection.
  6. Draft creation: one `post` per document in `DRAFT`, original file stored in the platform content bucket with SHA-256 (not in any tenant vault), import report listing every warning with a link to the block.
  Bulk imports of up to 200 files run in parallel with a progress screen; re-importing a file with the same hash is a no-op; re-importing a changed file creates a new draft version of the same post (matched by stored source path), never a duplicate.
- **FR-P21-80 Editor**: block editor with keyboard operation for every action (insert, move up/down without drag, delete with undo), live accessibility checks (alt text, heading order, link text, table headers, contrast of any custom callout), a mobile and no-JS preview toggle, word counts per block against the template minimum, and side panels for SEO, schema preview, claims, citations, related links and translations.
- **FR-P21-81 SEO fields** per page/post: title, meta description, canonical override (restricted to `PLT_CONTENT_EDITOR`), `robots` (index/noindex — `index` disabled until reviewer rules pass), OG image (generated or uploaded), primary keyword cluster (from Appendix N §N.5 registry), FAQ source tags, `summary_answer`, structured-data overrides limited to permitted fields. Live counters for title and description length and duplicate detection across the site.
- **FR-P21-82 Authors and reviewers**: `author` records link to a staff or professional identity; advocates' public bios use `web.authors.advocate_bio_mode = RULE36_FIELDS_ONLY` (Locked): name, address, contact, enrolment number and date, State Bar Council, qualifications, practice areas, with the Rule 36 disclaimer — no photos, testimonials, success claims or fees (NN-21; R3 LG-111). CA and CS bios follow ICAI and ICSI website guidance [VERIFY current text]. A byline of "LawDocs Editorial Team" is allowed for non-legal posts only.
- **FR-P21-83 Scheduling**: publish-at and unpublish-at in IST (UTC stored); scheduled items re-run all blocking checks at publish time (a claim may have expired); embargoed posts are invisible to search and preview links. Scheduling in the past is rejected (`LD-WEB-014`).
- **FR-P21-84 Preview**: signed preview URLs (24 h expiry, `noindex`, visible "Preview — not published" banner) render the exact production template, including no-JS and each enabled locale.
- **FR-P21-85 Rollback**: any published page or post can be rolled back to a prior version in one action; the rollback is itself a new version with a reason and passes the same checks (a rollback cannot restore an expired claim or a removed reviewer).
- **FR-P21-86 Publish effects**: on publish, revalidate affected routes (page, hubs, related pages, sitemaps, RSS), ping IndexNow, update the public search index, refresh `llms.txt`, emit `in.lawdocs.web.PageVersionPublished.v1`, and offer "Send to social calendar" which pushes an asset bundle (title, one-liner, summary, OG image, URL with UTM) to the OH7 asset library through `int` (Appendix X) — LawDocs does not post to social networks itself.
- **FR-P21-87 Categories and tags**: hierarchical categories (max depth 2), each with an intro (≥ 120 words before the category page is indexable), owner and legal flag; tags flat, curated; RSS/Atom per category; tag pages `noindex` until they meet FR-P21-54.
- **FR-P21-88 Content reuse from registries**: product facts (module names, features, counts of templates, languages, integrations) are pulled from platform registries (template library counts from P06, connector catalogue from P19, plan features from P17) as tokens (`{{tpl.count.published}}`), so copy cannot drift from the product; a token that resolves to zero or null hides its sentence (no "0 templates" counters — R1 §3.6).
- **FR-P21-89 Experiments**: A/B tests on landing pages and CTA wording only; never on legal pages, prices, fee breakdowns, disclaimers, consent text or eligibility badges; bucketing only after analytics consent (control served otherwise); dark-pattern self-audit checklist required to start an experiment (NN-50).
- **FR-P21-90 Content AI assistance** (§11): the content agent may propose rewrites of manual text, FAQs from question sources, metadata, translations and tutorial scripts into `DRAFT`, labelled "AI-drafted"; humans review every change; the agent never submits for review or publishes (NN-13, NN-43).
- **FR-P21-91 CMS export** (portability of LawDocs' own content): `GET /v1/console/web/export` produces a ZIP of all published and draft content as Markdown + JSON (blocks, metadata, versions), assets, redirects and taxonomy, so the CMS can be replaced without loss (OP-1, NN-12 principle).
- **FR-P21-92** Click budgets: DOCX upload → draft ready ≤ 2 clicks and ≤ 60 s for a 5,000-word file; draft → submitted ≤ 3 clicks once checks pass; checker approve → scheduled ≤ 2 clicks.

### 4J. Vlog (R-074)

- **FR-P21-93** Videos are hosted on LawDocs' YouTube channel and registered in `web.videos` by URL or video ID; `VIDEO_PORT` (YouTube Data API) imports title, description, duration, thumbnails, chapters and caption tracks; editors add the transcript, summary, related pages, category and ISL rendition link.
- **FR-P21-94** Embeds use the privacy-enhanced domain `youtube-nocookie.com` behind a **click-to-load facade**: the page shows a self-hosted thumbnail, title, duration and a play button; no request goes to YouTube until the user activates the player, and if the user has not consented to the "embedded media" category, activation first shows a short consent prompt with "Play once" and "Always allow" [VERIFY current privacy-enhanced-mode cookie behaviour — R6 note]. Without consent the transcript and a "Watch on YouTube" link remain available. Player controls, captions and keyboard operation are always enabled (never a locked player — WCAG 2.1.1, 2.2.2).
- **FR-P21-95** Every video page has: a visible full transcript (machine draft corrected by a human), chapters with timestamps as links, captions in English and Hindi at minimum (WebVTT stored by LawDocs, also uploaded to YouTube), an ISL rendition for videos in the core tutorial set (Appendix N §N.10), audio description or a descriptive transcript where visuals carry information not in the narration (WCAG 1.2.3/1.2.5), `VideoObject` markup, and a video sitemap entry.
- **FR-P21-96** AI-generated or synthetic media (AI voice-over, avatars) carries a visible on-screen label and a description label, consistent with the IT Rules synthetic-content labelling amendment (R3; [VERIFY 2026 text]) and R4-MKT-07.
- **FR-P21-97** Vlog index by category and playlist; Shorts embedded in vertical format with the same facade; no autoplay with sound.
- **FR-P21-98** A video referencing law follows the same reviewer-of-record and citation rules as a page (FR-P21-59–61); a video whose linked rule changes is flagged for review and can be marked "Partly outdated — see updated guide" without deleting it.

### 4K. Landing-page builder, funnels and lead capture

- **FR-P21-99** Landing pages (`/lp/{campaign}/{variant}`, `noindex` by default) are assembled from blocks by `OPS_CONTENT_PUBLISHER` per intent and traffic source (PTSTDM pattern adopted lawfully — R4 §10–§11): headline naming the audience and job, a 60–180-second VSL or explainer video **with controls, captions on by default and a transcript below**, three claim-gated proof points, one primary CTA (free draft, free tool, free Legal Health Check, webinar seat, ₹99 or ₹499 paid audit call), a secondary CTA, a short FAQ and the full footer.
- **FR-P21-100** Funnel types (Appendix X defines the OH side): (a) tool/magnet funnel (stamp-duty estimator, eSign eligibility checker, challan check deep-link explainer, TM availability guide); (b) VSL → webinar (free or ₹99, real dates, replay provided to registrants within 48 h, seat caps only if enforced); (c) tripwire → paid audit call credited against a purchase; (d) founder kit; (e) Legal Health Check for SMEs (20 questions, deterministic report; general information, not legal advice). Payments run through P17 checkout; this phase renders only.
- **FR-P21-101** Truthful-urgency engine: countdowns and seat counts are allowed only when bound to a real event record (date, cap, registrations) and disappear when false; anchor prices only from the P17 price book; bonuses only with real list prices; enforced by the claims gate and the dark-pattern checklist (CCPA Dark Patterns Guidelines 2023 — R3 LG-142; R4-MKT-08; NN-50).
- **FR-P21-102** Presenters: LawDocs as a company (founder, CS, product lead). An advocate may present educational content only, without soliciting work, naming their fees or offering their own services (R4-MKT-01; NN-21).
- **FR-P21-103** Lead forms: ≤ 5 fields (`web.lead.form.max_fields`): name, email or mobile, organisation (optional), interest, consent checkboxes; layered DPDP notice before submission; separate **unticked** consents per purpose (respond to this request; email marketing; WhatsApp/SMS/RCS; phone calls) with notice version (DPDP Act 2023 s.5–6; Rules 2025 [VERIFY rule numbers]); telecom consents recorded for DLT and TCCCPR (NN-34); no pre-ticked boxes (E-Commerce Rules r.4 [VERIFY]). Children: no lead capture from users who declare they are under 18.
- **FR-P21-104** Lead hand-off: on submit, `web` writes `web.leads` (minimal, 30-day retention locally) and `int` calls the Operations Hub CRM (`POST /v1/crm/requests`, scope `crm.request:write`, Ecosystem Spec Part 6.29) with: brand, `legal_entity_id`, contact, consent artefact references, interest, landing page, UTM and click identifiers, sensitivity class, and timestamp. LawDocs as a caller of this API is proposed in Appendix Y §Y.8/§Y.9 (Ecosystem Spec v1.2 change request; OI-P21-05). Retries with an idempotency key (NN-46); failures queue for 72 h with an alert. **Never sent:** drafter answers, draft content, vault data, case facts (NN-19). Speed-to-lead SLAs and nurture live in OH (Appendix X).
- **FR-P21-105** Sensitive intents (criminal, matrimonial, domestic violence, debt distress, health-insurance claims, consumer grievances) set `sensitivity = HIGH` on the lead: excluded from ad-platform conversion APIs, retargeting and lookalike audiences (R4-MKT-10), and routed to a human, not the AI SDR, by default.
- **FR-P21-106** Attribution capture (UTM, gclid/gbraid/wbraid, fbclid, referrer, first and last touch) is stored server-side on the lead; ad-platform conversion calls happen in OH only for leads with marketing-measurement consent (Appendix X; R4 §11.9).

### 4L. Consent, cookies and analytics

- **FR-P21-107** Consent banner per brand: "Accept all", "Reject all" with equal prominence, and "Manage"; categories: strictly necessary (no consent), preferences, analytics, embedded media, marketing; no pre-ticked categories; the choice is stored as a consent artefact (P01) for signed-in users and as a first-party cookie for visitors; withdrawal from a persistent "Cookie settings" footer link is as easy as giving (DPDP s.6(4) [VERIFY]; NN-26, NN-50). Text approved by `PLT_DPO`.
- **FR-P21-108** Analytics: a first-party, India-resident analytics service (self-hosted) loads only after analytics consent; server-side aggregate counts (page views by URL, no identifiers) run without consent as an operational log [INTERP — COUNSEL to confirm that aggregate, non-identifying server logs need no DPDP consent]. Marketing pixels (Google Ads, Meta, LinkedIn) load only after marketing consent and never on document, pleading, Consumer Help, help-centre or legal pages that reveal a sensitive intent (FR-P21-105).
- **FR-P21-109** No third-party trackers on authenticated surfaces (OH7.8); no session replay on any surface that shows personal data; no data from the drafter questionnaire is sent to any analytics or ad tool (NN-32).
- **FR-P21-110** GDPR/CCPA variants switch on by jurisdiction flag (NN-26, CH-18): self-declared country with IP only as a hint; "Do Not Sell or Share" link where CCPA applies [VERIFY thresholds].

### 4M. Help centre and contextual help (`hlp` module)

- **FR-P21-111** Public help centre at `www.lawdocs.in/help` (and the brand host for Consumer Help) and an in-app **help panel** shared by `apps/web`, `apps/delivery`, `apps/console` and `apps/mobile` (P22 renders natively from the same API). Article types: Getting started, How-to (task), Concept, Troubleshooting, Reference (field-by-field), Legal explainer (links to glossary and rules), Release note, Accessibility guide.
- **FR-P21-112** Contextual help: every screen registers a `help_key` in the P02 screen registry; the help panel (keyboard shortcut `?`, plus a persistent Help button in the same position on every screen — WCAG 3.2.6) shows mapped articles, the screen's tutorial video, the glossary terms on that screen, "Ask Vidhi" in **help mode** (answers only from published help and glossary content with citations; says "I don't know" otherwise — §11), and "Contact support" (creates an OH support ticket through `int`, scope `ops.ticket:write`, carrying screen, app version and help key, never document content — NN-19, NN-32).
- **FR-P21-113** Help search across articles, glossary, tutorials and release notes with typo tolerance, synonyms, transliteration and role-aware ranking (an `ORG_CHECKER` sees approval articles first).
- **FR-P21-114** Article governance: owner, last-reviewed date, applicable app version, roles and plans; "Was this helpful?" with an optional comment (no personal data requested); stale after `hlp.article.stale_after_days` (default 180) or when the mapped screen's UI changes (screenshot diff, FR-P21-136).
- **FR-P21-115** Tenant notes: `ORG_ADMIN` can attach internal guidance to any `help_key` ("In our company, Legal approves all NDAs above ₹10 lakh"), shown under LawDocs' article with "Your organisation's note"; tenant data under RLS (NN-01), included in exports (§13 export map).
- **FR-P21-116** Easy-read layer: legal explainer and getting-started articles carry an optional easy-read version (short sentences, one idea per line, supporting icons with text) and a "Listen" control (TTS of the approved text; Appendix U §U.6).
- **FR-P21-117** Assisted help: an "I need help using LawDocs because of a disability" route offers a callback, a WhatsApp chat or an ISL video call on request (scheduled through OH support), plus the accessibility feedback form (§4Q).
- **FR-P21-118** Help content is versioned like CMS content (maker-checker, audit) and exportable (FR-P21-91).

### 4N. "i" glossary registry (R-019)

- **FR-P21-119** Every legal, compliance or product term that appears in a menu, page heading, table column, form label, status chip, error message or report heading is registered as an "i" key `hlp.<module>.<term>` (module = the bounded context whose screens primarily use the term, e.g., `hlp.sgn.estamp_certificate`, `hlp.lit.cnr_number`, `hlp.drf.template_automation`, `hlp.wf.maker_checker`; general legal jargon not tied to a module uses `hlp.gen.<term>`, e.g., `hlp.gen.indemnity`, `hlp.gen.consideration`). A lint rule fails the build when a UI string tagged `term=` has no registered key (`LD-HLP-001`).
- **FR-P21-120 Term record**: canonical term; abbreviations and synonyms; plain-language definition (≤ 40 words, reading grade ≤ 8) **in every enabled D-07 language**; detailed explanation (≤ 250 words); legal definition **quoted** with citation (instrument, provision, version, date) when defined in law, linked to the `rul` item so an amendment flags the term (FR-P21-63); example; "Where you see it" (screens via `help_key`); related terms; audience (individual, company, professional); status; reviewer; audio pronunciation for terms in Latin legal phrases and Indic terms.
- **FR-P21-121 UI behaviour**: an "i" button (accessible name "About {term}") beside the label opens a non-modal popover on click, Enter or Space (never hover-only); dismissible with Escape without moving focus; persistent while hovered or focused; does not obscure the trigger (WCAG 1.4.13); target ≥ 24 × 24 CSS px (WCAG 2.5.8), 44 × 44 pt/48 × 48 dp on mobile; content: plain definition, "Listen", "Learn more" (glossary page), "Watch" (tutorial). Screen readers get the definition through `aria-describedby` only after opening so routine navigation is not verbose.
- **FR-P21-122** User setting `hlp.inline.explanations` (USER tier; default OFF, suggested ON in the first-run checklist for individuals) renders plain definitions inline beneath labels.
- **FR-P21-123** Tenant terminology overrides (P02): when a tenant renames "Checker" to "Reviewer", the popover heading uses the tenant label with "LawDocs term: Checker" beneath; legal definitions never change.
- **FR-P21-124** Coverage: ≥ 150 terms in Wave 1 (product, eSign/eStamp, vault, drafting), ≥ 350 in Wave 2 (contracts, litigation, IP, governance), ≥ 500 in Wave 3 (business services, tax, Consumer Help), priority list in Appendix N §N.12. Term counts are shown internally only.
- **FR-P21-125** Public glossary pages render published terms (FR-P21-26) in each reviewed locale; the index groups by topic and by A–Z per script.
- **FR-P21-126** Machine-translated plain definitions follow NN-48: labelled until a human reviewer for that language approves; unapproved locales fall back to English with a notice.
- **FR-P21-127** Terms used in error messages: every `LD-<MODULE>-<NNN>` error carries its help key; the error UI shows the "i" link (Appendix B §B.5).

### 4O. Guided tours and onboarding checklists

- **FR-P21-128** Tours are data (`hlp.tours`: steps with target `data-tour-id`, text, media, roles, plans, trigger, locale) played by an accessible tour component: each step is a dialog announced to screen readers; focus moves to the dialog and back to the target; Escape exits; "Skip" and "Show me later" always present; no drag gestures (WCAG 2.5.7); tours never block work and respect reduced motion.
- **FR-P21-129** First-run tours (≤ 7 steps each): `IND_OWNER` (first document → eSign → vault), `ORG_ADMIN` (company setup, users, makers and checkers, delivery grants), `ORG_LEGAL_MAKER` (intake → draft → send for negotiation), `ORG_CHECKER` (review queue → approve/return), `ORG_CLO` (legal calendar, matter dashboard), `OPS_RM` (client sections, delivery grant, RM-as-maker), `PRO_ADVOCATE` (engagement → deliverable), `CP_GUEST` signer (3 steps: review, comment, sign).
- **FR-P21-130** Onboarding checklists per persona with five value moments (e.g., individual: profile → first draft → first signature → first folder → export tried) shown in the app; completion events feed product analytics in aggregate only.
- **FR-P21-131** "What's new" cards: one per session maximum (`hlp.tours.whats_new_per_session`, default 1), linked to the release note and video; dismissible permanently.

### 4P. Tutorial pipeline and social-ready clips (R-020)

- **FR-P21-132** A tutorial (`tut_`) is a structured script: goal, audience, prerequisites, steps (each bound to a `data-tour-id` and screen), narration text per step, callouts, diagram source, related help keys, locales. The script is the single source for the text article, annotated screenshots, interactive artefact, video and social clips.
- **FR-P21-133 Screenshots**: captured automatically by Playwright against a seeded **demo tenant with synthetic data only** (never customer data; NN-15, NN-32) at desktop and 360 px mobile widths, per locale; annotations (numbered callouts, highlight boxes, arrows) are an overlay spec rendered at build, so a UI change re-renders them without manual editing; every screenshot has generated alt text reviewed by the writer and a step caption.
- **FR-P21-134 Diagrams**: Mermaid or SVG source in the script; rendered with a text alternative or adjacent table; brand tokens; dark-mode safe.
- **FR-P21-135 Interactive artefacts**: click-through demos generated from the captured screens (HTML, keyboard operable, screen-reader labelled hotspots, no timing), embeddable in help articles and landing pages.
- **FR-P21-136 Staleness**: on each release, the pipeline re-captures screenshots and compares them with the published set; a difference above `hlp.tutorial.screenshot_diff_threshold_pct` (default 2%) flags the tutorial for review and blocks auto-republish until a writer approves.
- **FR-P21-137 Videos**: generated from the script as a screen recording of the scripted Playwright run plus voice-over (human recording preferred for the core set; TTS allowed with the synthetic-media label, FR-P21-96), captions (WebVTT from the narration text, so captions are exact), chapter markers per step, optional ISL interpreter picture-in-picture for the core set (recorded by a qualified ISL interpreter — LG-137).
- **FR-P21-138 Export presets** (Appendix N §N.10): YouTube 16:9 1080p with chapters; YouTube Shorts and Instagram Reels 9:16 1080 × 1920, ≤ 60 s by default [VERIFY current maximum lengths]; LinkedIn 1:1 or 4:5; each with burned-in captions for social, a separate SRT/VTT, safe-area-aware text, brand end card with the canonical URL, and a claims-gated caption text. Clips are pushed to the OH7 asset library and social calendar (FR-P21-86); posting happens in OH.
- **FR-P21-139** Tutorial publication follows maker-checker; legal statements inside tutorials follow the reviewer-of-record rule; every tutorial page shows "Applies to version {x}" and last-verified date.
- **FR-P21-140** Launch tutorial catalogue and feature-video list: Appendix N §N.10.

### 4Q. Accessibility statement and feedback channel (NN-28, R-025)

- **FR-P21-141** `/accessibility` per brand renders the Appendix U §U.10 statement template: standards targeted (WCAG 2.2 AA, IS 17802 Parts 1–2, GIGW 3.0 where applicable — R3 LG-133–LG-134), conformance status per surface, known limitations with dates for fixes, assistive features (captions, transcripts, ISL, easy-read, TTS, voice input, high-contrast and large-text themes), how to contact, response times, escalation to the Grievance Officer, date of last audit and the auditor.
- **FR-P21-142** Feedback channel: an accessible form (no CAPTCHA; honeypot and rate limiting instead), email, phone, WhatsApp and ISL video call on request; fields: page or screen (auto-filled), what happened, assistive technology used (optional), preferred contact; acknowledgement within `hlp.a11y.feedback_ack_hours` (default 48) and resolution or a dated plan within `hlp.a11y.feedback_resolve_days` (default 30) [REC; aligned with E-Commerce Rules r.4 grievance clocks]; tracked as an issue in `hlp.a11y_issues` with severity per Appendix U §U.9; emits `in.lawdocs.hlp.AccessibilityFeedbackReceived.v1`; the submitter gets status updates.
- **FR-P21-143** A conformance report (IS 17802 and WCAG 2.2 checklist per template, with test dates and tools) is published per release, signed by `OPS_QA_REVIEWER` and the accessibility specialist.
- **FR-P21-144** Accessibility preferences (site and apps): theme (default, high contrast, dark), text size (100–200%), line spacing, reduced motion, dyslexia-friendly font option, inline "i" explanations, captions default, easy-read default — stored per user (USER tier) and, for visitors, in a first-party preference cookie (strictly necessary).
- **FR-P21-145** No accessibility overlays or "fix-it" widgets (NN-28). The public site passes the Appendix U release gate before each wave go-live.

## 5. Workflows and state machines

### 5.1 Page / post version (`web.page_versions.state`)

| State | Entry | Allowed transitions | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| DRAFT | Create, import, rollback draft, agent proposal | → IN_REVIEW, → HOLD | Maker | Blocking checks pass (template minimum, alt text, links, claims, citations, plagiarism, outdated-law linter, structured data, axe) | — |
| IN_REVIEW | Submit | → LEGAL_REVIEW (if flag), → APPROVED, → DRAFT (return with comments) | Checker (`PLT_CONTENT_EDITOR` or a second publisher for non-legal posts) | Checker ≠ maker | Notification to maker |
| LEGAL_REVIEW | Legal flag set | → APPROVED, → DRAFT | `PLT_LEGAL_REVIEWER` | Reviewer ≠ maker; reviewer credential on file | Reviewer of record stamped |
| APPROVED | Approval | → SCHEDULED, → PUBLISHED | Maker or checker | Checks re-run | — |
| SCHEDULED | Publish-at set | → PUBLISHED (job), → APPROVED (unschedule) | System / maker | Checks re-run at publish time | — |
| PUBLISHED | Publish | → SUPERSEDED (new version published), → UNPUBLISHED | System / checker | — | Revalidate, IndexNow, search index, sitemap; `in.lawdocs.web.PageVersionPublished.v1` |
| UNPUBLISHED | Unpublish | → DRAFT | Checker | Redirect or 410 chosen for the URL | `in.lawdocs.web.PageUnpublished.v1`; redirect created |
| HOLD | Stub/upcoming/law-change hold | → DRAFT | Editor | — | `noindex`; excluded from sitemap |

Review-overdue and law-change events move a PUBLISHED page into the review queue without changing its state; after 60 days overdue the page switches to `noindex` (FR-P21-59).

### 5.2 DOCX import job (`web.import_jobs.status`)

`QUEUED → SCANNING → (BLOCKED_TRACKED_CHANGES ⇄ awaiting decision) → CONVERTING → LINTING → DRAFTS_CREATED | FAILED`. Each file has its own row; the job completes when all rows are terminal. `FAILED` carries an `LD-WEB-0xx` code per file. Emits `in.lawdocs.web.DocxImportCompleted.v1` with counts only.

### 5.3 Glossary term (`hlp.terms.state`)

`DRAFT → IN_REVIEW → (LEGAL_REVIEW if legal definition present) → PUBLISHED → REVIEW_DUE (rule change or age) → PUBLISHED | DEPRECATED`. Locale versions have their own `MT_DRAFT → HUMAN_REVIEWED → PUBLISHED` sub-state (NN-48). Publishing emits `in.lawdocs.hlp.TermPublished.v1`; a deprecated key stays resolvable (shows "This term is no longer used; see {new}") so old UI builds never break.

### 5.4 Tutorial asset (`hlp.tutorials.state`)

`SCRIPTED → CAPTURED → ANNOTATED → NARRATED → CAPTIONED → (ISL_ADDED) → IN_REVIEW → PUBLISHED → STALE (screenshot diff or rule change) → re-CAPTURED`. Clip exports (`hlp.clips`) are children; pushing a clip to OH emits `in.lawdocs.hlp.ClipExported.v1`.

### 5.5 Lead hand-off

`CAPTURED (web.leads) → SENT (int → OH CRM 2xx) → ACKNOWLEDGED (OH lead id stored) → PURGED (local copy deleted after 30 days)`; on failure `RETRYING` (exponential backoff, 72 h) → `DEAD_LETTER` (alert to `PLT_SRE`, manual replay). Consent withdrawal before SENT cancels the hand-off.

### 5.6 Accessibility issue (`hlp.a11y_issues.state`)

`RECEIVED → ACKNOWLEDGED (≤ 48 h) → TRIAGED (severity S1–S4, Appendix U §U.9) → IN_FIX → FIXED → VERIFIED (by reporter where possible) → CLOSED`, or `WONT_FIX` only with an approved alternative and a statement entry. S1 (blocker) issues on a core journey block the next release (Appendix U release gate).

### 5.7 Redirect rule

`DRAFT → APPROVED (maker-checker) → ACTIVE → RETIRED` (retirement only after 12 months with zero hits, and never for legacy URLs that still have backlinks).

## 6. Screens and UX

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility notes |
|---|---|---|---|---|---|---|
| SCR-P21-01 | public | Home | Hero ("Draft it. Sign it. Keep it."), issue tiles, section cards, drafter entry, proof points (claims-gated), how it works, pricing teaser, marketplace teaser, help/videos, footer | Claim expired → block hidden | Single column; sticky bottom bar | One H1; tiles are links, not buttons |
| SCR-P21-02 | public | Section landing (Documents, Pleadings, Compliance, Start a Business, Regulated entities) | Definition, category grid, top documents, Vidhi box, hire strip | — | Accordion categories | Disclosure pattern |
| SCR-P21-03 | public | Category hub | FR-P21-23 | Sub-hub without leaves shows Vidhi + hire | Grid → list | CollectionPage headings |
| SCR-P21-04 | public | Sub-category hub | FR-P21-24 | — | — | Table headers scoped |
| SCR-P21-05 | public | Document page | FR-P21-20, drafter, eSign badge, hire, State selector | Template withdrawn → hire only; badge "Not valid" → wet-ink pack | Drafter above the fold | Badge text not colour-only; State selector is a native select |
| SCR-P21-06 | public | Pleading page | FR-P21-21, variant toggles, old→new map | Variant without content → hidden toggle | Toggles as segmented control | Toggles announce content change via live region |
| SCR-P21-07 | public | Service page | FR-P21-22, price card | Price unavailable → "Get a quote" (never ₹0) | Price card sticky | Fee table readable by screen reader |
| SCR-P21-08 | public | Comparison page | Table, decision list | — | Horizontal scroll inside table region only | Table caption and scope |
| SCR-P21-09 | public | Glossary index and term | FR-P21-26 | Locale missing → English with notice | — | `<dfn>`, Listen control |
| SCR-P21-10 | public | State variant page | FR-P21-27 | — | — | — |
| SCR-P21-11 | public | Marketplace storefront (landing, category, service, retainers, academy) | P16 data, fee breakdown, ranking-parameters link | Service paused → "Temporarily unavailable" | Filters in a dialog | Filters as fieldsets; result count live region |
| SCR-P21-12 | public | Pricing | Three plans, toggle, credits, renewal terms | Catalogue unavailable → cached last version with timestamp | Plans as stacked cards | Toggle is a radio group |
| SCR-P21-13 | public | Startups hub | Journey steps, founder kit | — | Stepper → list | Ordered list semantics |
| SCR-P21-14 | public | Blog index, category, post | Cards, author, reviewer, related | No posts in category → category not indexable | — | Reading time text |
| SCR-P21-15 | public | Vlog index and video page | Facade player, transcript, chapters | No consent → transcript + link | Vertical Shorts | Captions default on |
| SCR-P21-16 | public | Help centre home and article | Search, topics, article, feedback | No results → suggestions + contact | — | Consistent help location |
| SCR-P21-17 | public | Legal policy page | Version, effective date, change log | — | — | Long-page table of contents |
| SCR-P21-18 | public | About, Team, Partnership, Careers, Contact, Press, Trust | FR-P21-32 | — | — | Map has text alternative |
| SCR-P21-19 | public | Campaign landing page | FR-P21-99 | Event ended → page shows replay or next date | — | No locked player |
| SCR-P21-20 | public | Accessibility statement and feedback form | FR-P21-141–142 | Submission error summary at top | — | No CAPTCHA; error summary |
| SCR-P21-21 | public | Search results | Typed results | Zero results → glossary/help suggestions | — | Live-region result count |
| SCR-P21-22 | public | Free tools hub and tool page | Deterministic calculator, sources | Rule unverified → tool disabled with note (NN-38) | — | Results in text, not only charts |
| SCR-P21-23 | console | Content Studio — content list | Filters by type, state, owner, review due | — | Responsive | Data table pattern (Appendix U §U.5) |
| SCR-P21-24 | console | Page/post block editor | Blocks, side panels (SEO, schema, claims, citations, translations) | Check failures inline with links | — | Keyboard block moves |
| SCR-P21-25 | console | DOCX import wizard | Upload, folder mapping, report | Tracked changes decision | — | Progress announced |
| SCR-P21-26 | console | Review queue | Diff view, approve/return, legal review | — | — | Diff readable without colour |
| SCR-P21-27 | console | Redirect manager | Rules, test URL, hit counts | Loop/chain error | — | — |
| SCR-P21-28 | console | SEO and GEO dashboard | Coverage, CWV, crawler/AI-bot logs, AI-answer checks, review-due list | — | — | Charts with tables |
| SCR-P21-29 | console | Glossary studio | Term record, locales, rule links | Missing locale flags | — | — |
| SCR-P21-30 | console | Tutorial studio and clip exporter | Script, captures, overlays, narration, captions, ISL, presets | Stale flag | — | Caption editor keyboard-operable |
| SCR-P21-31 | console | Tour builder | Steps bound to `data-tour-id`, preview | Target missing (`LD-HLP-005`) | — | — |
| SCR-P21-32 | console | Landing-page builder | Variants, event binding, dark-pattern checklist | Checklist incomplete blocks publish | — | — |
| SCR-P21-33 | console | Media and video library | Assets, alt text, licences, YouTube import | — | — | — |
| SCR-P21-34 | console | Accessibility issues board | Issues, severity, SLA clocks | — | — | — |
| SCR-P21-35 | web/delivery/console/mobile | In-app help panel and "i" popover | Articles, video, terms, Vidhi help mode, contact support, tenant note | Offline → cached articles | Bottom sheet | Non-modal; Escape closes |

## 7. Backend design

### 7.1 Modules

`web` (pages, posts, videos, landing pages, leads, redirects, SEO, entities, claims references, experiments) and `hlp` (help articles, terms, tours, tutorials, clips, tenant notes, accessibility issues, preferences). Both are NestJS modules in `apps/api` with their own PostgreSQL schemas. Public reads go through a read-optimised projection and the CDN; `apps/public` never queries the write model directly.

### 7.2 Tables (platform tables carry `brand_id`; tenant tables carry `tenant_id` + `legal_entity_id` with RLS, NN-01)

| Table | Key columns | Indexes | RLS | Retention class |
|---|---|---|---|---|
| `web.pages` | `pg_` id, brand, type, canonical_slug, locale_group_id, state, current_version_id | unique (brand, locale, slug) | platform | permanent |
| `web.page_versions` | id, page_id, version_no, blocks_jsonb, seo_jsonb, summary_answer, reviewed_by, reviewed_at, next_review_at, legal_flag, claims[], citations[], content_hash | (page_id, version_no) | platform | permanent (immutable) |
| `web.posts` | `pst_` id, page_id, category_id, tags[], authors[], reading_minutes, source_docx_hash, source_path | category, published_at | platform | permanent |
| `web.videos` | `vid_` id, youtube_id, duration, chapters_jsonb, transcript_ref, captions[], isl_ref, synthetic_label | youtube_id unique | platform | permanent |
| `web.landings` | id, campaign, variant, source, event_id, checklist_ref | campaign | platform | 3 years after end |
| `web.leads` | id, brand, legal_entity_id, contact (encrypted), consent_refs[], utm_jsonb, sensitivity, status, oh_lead_id | status, created_at | platform (restricted role) | 30 days after ACKNOWLEDGED |
| `web.redirects` | id, brand, from_path, to_path, code (301/410), state, hits, last_hit_at | unique (brand, from_path) | platform | permanent |
| `web.entities` | id, canonical_name, variants[], same_as[] | — | platform | permanent |
| `web.import_jobs`, `web.import_files` | job, file, status, warnings_jsonb, error_code | job_id | platform | 1 year |
| `web.geo_checks` | prompt_id, engine, run_at, cited, accuracy_note | prompt_id | platform | 3 years |
| `web.testimonials` | id, order_ref, consent_ref, text, display_name, city, role, consideration_disclosed, state | state | platform | while consent valid + 1 year |
| `hlp.articles`, `hlp.article_versions` | id, help_keys[], type, roles[], locale, state, reviewed_at | help_keys GIN | platform | permanent |
| `hlp.terms`, `hlp.term_locales` | `trm_` id, key (`hlp.<module>.<term>`), legal_ref, state; locale, plain_def, detail, mt_flag, reviewer | key unique | platform | permanent |
| `hlp.tours` | id, steps_jsonb, roles[], trigger | — | platform | permanent |
| `hlp.tutorials`, `hlp.clips` | `tut_` id, script_jsonb, assets[], state; clip preset, file_ref, pushed_at | — | platform | permanent |
| `hlp.tenant_notes` | id, tenant_id, legal_entity_id, help_key, body, author | (tenant_id, help_key) | tenant RLS | tenant lifetime |
| `hlp.a11y_issues` | id, brand, surface, url_or_screen, severity, state, reporter_contact (encrypted, optional), sla_due_at | state, sla_due_at | platform (restricted) | 3 years |
| `hlp.user_prefs` | user_id, tenant_id, theme, text_scale, motion, inline_terms, captions_default, easy_read | user_id | tenant RLS | account lifetime |

### 7.3 APIs

| Method | Path | Scope | Idempotency |
|---|---|---|---|
| GET | `/v1/public/pages/{brand}/{locale}/{slug*}` | public, cached | — |
| GET | `/v1/public/search?q=&type=&locale=` | public, rate-limited | — |
| POST | `/v1/public/drafter/sessions` | public, rate-limited (anonymous template lane) | Idempotency-Key |
| POST | `/v1/public/leads` | public, rate-limited, consent required | Idempotency-Key |
| POST | `/v1/public/a11y-feedback` | public, rate-limited | Idempotency-Key |
| GET | `/v1/public/glossary/{key}?locale=` | public, cached | — |
| GET | `/v1/help/panel?help_key=&locale=` | authenticated (any app) | — |
| PUT | `/v1/help/tenant-notes/{help_key}` | `ORG_ADMIN` | If-Match |
| PUT | `/v1/me/accessibility-preferences` | authenticated | If-Match |
| POST | `/v1/console/web/imports` | `OPS_CONTENT_PUBLISHER` | Idempotency-Key |
| POST | `/v1/console/web/pages/{id}/versions/{v}/transitions` | role per §5.1 | Idempotency-Key |
| POST | `/v1/console/web/redirects` | `OPS_CONTENT_PUBLISHER` or `PLT_CONTENT_EDITOR` (maker); a `PLT_CONTENT_EDITOR` ≠ maker approves (P00 FR-P00-75) | Idempotency-Key |
| POST | `/v1/console/hlp/terms/{id}/transitions` | per §5.3 | Idempotency-Key |
| POST | `/v1/console/hlp/tutorials/{id}/capture` | `OPS_CONTENT_PUBLISHER` | Idempotency-Key |
| POST | `/v1/console/hlp/clips/{id}/push` | `OPS_CONTENT_PUBLISHER` | Idempotency-Key |
| GET | `/v1/console/web/export` | `PLT_CONTENT_EDITOR` + checker | — |

Errors (range **`LD-WEB-001`–`LD-WEB-040`**, **`LD-HLP-001`–`LD-HLP-020`**; each with a help key): `LD-WEB-001` Page cannot be indexed without a reviewer of record · `002` Claim not approved or expired · `003` Similarity above threshold · `004` Slug conflicts with an existing canonical URL · `005` Redirect would create a chain or loop · `006` Structured data invalid or does not match visible content · `007` Accessibility check failed (serious/critical) · `008` DOCX contains tracked changes or comments · `009` State variant fails the materiality test · `010` Embed blocked until consent · `011` Testimonial lacks consent or verified-purchase link · `012` Testimonial about an advocate is not allowed · `013` Lead consent missing · `014` Scheduled time is in the past · `015` Maker cannot review own content · `016` Citation unresolved · `017` Outdated law reference without mapping · `018` Competitor brand or prohibited link detected · `019` Template minimum content not met · `020` Price must come from the catalogue · `021` Urgency element not bound to a real event · `022` Locale page lacks human review · `023` Crawler policy change requires checker approval · `024` Advertising slot not permitted on this page type. `LD-HLP-001` UI term has no registered "i" key · `002` Plain definition missing for an enabled locale · `003` Video lacks captions · `004` Video lacks transcript · `005` Tour target not found · `006` Tutorial capture used a non-synthetic tenant · `007` Help key not registered for screen · `008` Accessibility feedback rate limit reached (offers phone/email).

### 7.4 Domain events (CloudEvents; internal `in.lawdocs.<module>.<EventName>.v1`)

`in.lawdocs.web.PageVersionPublished.v1`, `in.lawdocs.web.PageUnpublished.v1`, `in.lawdocs.web.DocxImportCompleted.v1`, `in.lawdocs.web.RedirectMapPublished.v1`, `in.lawdocs.web.LeadCaptured.v1` (internal; the cross-product hand-off is the OH CRM API call via `int`), `in.lawdocs.web.ContentReviewDue.v1`, `in.lawdocs.web.LawChangeFlagged.v1`, `in.lawdocs.web.TestimonialApproved.v1`, `in.lawdocs.hlp.TermPublished.v1`, `in.lawdocs.hlp.TutorialPublished.v1`, `in.lawdocs.hlp.TutorialStale.v1`, `in.lawdocs.hlp.ClipExported.v1`, `in.lawdocs.hlp.HelpArticleFlaggedStale.v1`, `in.lawdocs.hlp.AccessibilityFeedbackReceived.v1`. No new cross-product events are produced by `web`/`hlp` directly; `int` maps `web.PageVersionPublished`, `hlp.TutorialPublished` and `hlp.ClipExported` for items linked to an OH7 calendar item to the proposed `in.infrabyx.ops.ContentPublished.v1`, and state changes of this phase's content and accessibility grievance queue to the proposed `ops.GrievanceStatusChanged.v1` (metadata only; X.6 mirror) — Appendix Y §Y.7.10, inert until merged. The CRM and asset-library calls are APIs registered in Appendix Y §Y.8.

### 7.5 Jobs and workflows

Temporal: `DocxImportWorkflow`, `PublishWorkflow` (checks → snapshot → revalidate → IndexNow → search index → events), `TranslationReviewWorkflow`, `TutorialCaptureWorkflow` (seed demo tenant → Playwright capture per locale and viewport → diff → overlay render → video assembly → caption render), `LeadHandoffWorkflow`. BullMQ: sitemap regeneration, `llms.txt` build, redirect hit aggregation, review-due sweep (daily), claims expiry sweep (nightly), CWV and Search Console import (daily), AI-bot log aggregation (daily), stale-help sweep (weekly).

## 8. Integrations

| Port / adapter | Default | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `int` → OH3 CRM (`POST /v1/crm/requests`) | Operations Hub | — (Brevo only via OH) | Retry 72 h, dead-letter alert | Export CSV of `web.leads` in DEAD_LETTER for manual upload by OH |
| `int` → OH support desk (`ops.ticket:write`) | Operations Hub | — | Queue; show email/phone | Email support address |
| `int` → OH14 claims gate | Operations Hub | Local claims register only (degraded: blocks new claims) | Cached last PASS for 24 h; new claims blocked | `PLT_CONTENT_EDITOR` removes claim |
| `int` → OH7 asset library / social calendar | Operations Hub | — | Retry; clip stays downloadable | Manual download |
| `VIDEO_PORT` | YouTube Data API | Vimeo (adapter) | Use cached metadata | Manual metadata entry |
| `PLAGIARISM_PORT` | Licensed API (Copyscape-type) [VERIFY terms and India data handling] | Quetext/Turnitin-type | Block legal submissions; allow drafts | Manual check by reviewer with evidence upload |
| `TRANSLATE_PORT` | Per P05 (Bhashini [VERIFY], Google/Azure fallback) | — | Keep English | Human translation |
| `TTS_PORT` | Per P05/P09 Indic TTS adapter | On-device TTS (mobile) | Hide Listen control | — |
| Search Console, Bing Webmaster, IndexNow | Official APIs | — | Skip ping; retry | Manual submission |
| Gotenberg/LibreOffice | `.doc` → `.docx`, PDF of policies | — | Reject `.doc` with message | Ask publisher to save as `.docx` |
| `PAYMENTS` | Not called here; checkout links to P17 | — | — | — |

## 9. Settings and configuration (register in Appendix R before use — NN-29)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `web.host.canonical` | BRAND | url | `https://www.lawdocs.in` | `PLT_SUPER_ADMIN` | Y |
| `web.brand.host_map` | PLATFORM | map | lawdocs + consumer-help placeholder | `PLT_SUPER_ADMIN` | Y |
| `web.brand.consumer_help.enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` | Y |
| `web.render.revalidate_seconds` | PLATFORM | map by page type | per FR-P21-02 | `PLT_SRE` | N |
| `web.crawl.ai_search_bots_allowed` | BRAND | bool | true | `PLT_SUPER_ADMIN` | Y (checker `PLT_SECURITY_OFFICER`) |
| `web.crawl.ai_training_bots_allowed` | BRAND | bool | false [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.crawl.google_extended_allowed` | BRAND | bool | false [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.llms_txt.enabled` | BRAND | bool | true | `PLT_CONTENT_EDITOR` | N |
| `web.indexnow.enabled` | BRAND | bool | true | `PLT_CONTENT_EDITOR` | N |
| `web.schema.faqpage_mode` | BRAND | enum OFF/VISIBLE_ONLY | VISIBLE_ONLY | `PLT_CONTENT_EDITOR` | N |
| `web.cwv.budgets` | PLATFORM | object | LCP 2500 ms, INP 200 ms, CLS 0.1, TTFB 800 ms | `PLT_SRE` | Y |
| `web.js_budget_kb` | PLATFORM | map | content 150, drafter 250 | `PLT_SRE` | Y |
| `web.state_variant.min_distinct_facts` | PLATFORM | int | 3 | `PLT_CONTENT_EDITOR` | Y (checker `PLT_LEGAL_REVIEWER`) |
| `web.city_pages.enabled` | BRAND | bool | false | `PLT_CONTENT_EDITOR` | Y |
| `web.review.max_age_days` | PLATFORM | map by type | document 365, pleading 180, service 180, regulated-entity 120, blog 365 | `PLT_LEGAL_REVIEWER` | Y |
| `web.review.auto_noindex_without_reviewer` | PLATFORM | bool | true (Locked) | — | — |
| `web.facts.max_age_days` | PLATFORM | int | 180 | `PLT_LEGAL_REVIEWER` | Y |
| `web.plagiarism.max_similarity_pct` | PLATFORM | int | 10 | `PLT_LEGAL_REVIEWER` | Y |
| `web.testimonials.photos_enabled` | BRAND | bool | false (Locked OFF on advocate/court pages) | `PLT_CONTENT_EDITOR` | Y |
| `web.testimonials.advocate_related_allowed` | PLATFORM | bool | false (Locked) | — | — |
| `web.authors.advocate_bio_mode` | PLATFORM | enum | RULE36_FIELDS_ONLY (Locked) | — | — |
| `web.locale.<code>.sections` | BRAND | list | en: all; others: none until reviewed | `PLT_CONTENT_EDITOR` | Y |
| `web.mt.publish_requires_human_review` | PLATFORM | bool | true (Locked, NN-48) | — | — |
| `web.cms.docx_import.max_mb` | PLATFORM | int | 25 | `PLT_CONTENT_EDITOR` | N |
| `web.cms.folder_category_map` | BRAND | map | [OWNER to supply] | `PLT_CONTENT_EDITOR` | Y |
| `web.cms.legal_review.auto_types` | PLATFORM | list | document, pleading, service, regulated-entity, advisory, comparison, tool, policy | `PLT_LEGAL_REVIEWER` | Y |
| `web.drafter.anon_runs_per_day` | BRAND | int | 3 | `PLT_SUPER_ADMIN` | N |
| `web.lead.form.max_fields` | BRAND | int | 5 | `PLT_CONTENT_EDITOR` | N |
| `web.lead.local_retention_days` | PLATFORM | int | 30 | `PLT_DPO` | Y |
| `web.consent.categories` | BRAND | list | necessary, preferences, analytics, embedded_media, marketing | `PLT_DPO` | Y |
| `web.video.embed_host` | PLATFORM | string | `www.youtube-nocookie.com` | `PLT_SECURITY_OFFICER` | Y |
| `web.experiments.enabled` | BRAND | bool | true (never on excluded types) | `PLT_CONTENT_EDITOR` | N |
| `web.contact.public_phone` | BRAND | string | [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.kill.drafter` / `.lead_capture` / `.video_embeds` / `.landing_pages` | BRAND | bool | false | `PLT_SUPER_ADMIN`, `PLT_SRE` | N (audited) |
| `hlp.inline.explanations` | USER | bool | false | user | N |
| `hlp.tours.auto_start_first_run` | TENANT, USER | bool | true | `ORG_ADMIN`, user | N |
| `hlp.tours.whats_new_per_session` | PLATFORM | int | 1 | `PLT_CONTENT_EDITOR` | N |
| `hlp.tenant_notes.enabled` | TENANT | bool | true | `ORG_ADMIN` | N |
| `hlp.article.stale_after_days` | PLATFORM | int | 180 | `PLT_CONTENT_EDITOR` | N |
| `hlp.tutorial.screenshot_diff_threshold_pct` | PLATFORM | int | 2 | `PLT_CONTENT_EDITOR` | N |
| `hlp.video.captions_default_on` | PLATFORM, USER | bool | true | user | N |
| `hlp.video.isl_required_for_core` | PLATFORM | bool | true | `PLT_CONTENT_EDITOR` | Y |
| `hlp.vidhi_help_mode.enabled` | PLATFORM, TENANT | bool | true | `PLT_SUPER_ADMIN`, `ORG_ADMIN` | N |
| `hlp.a11y.feedback_ack_hours` | PLATFORM | int | 48 | `PLT_GRIEVANCE_OFFICER` | Y |
| `hlp.a11y.feedback_resolve_days` | PLATFORM | int | 30 | `PLT_GRIEVANCE_OFFICER` | Y |

Customisation hooks without code: issue tiles, nav labels (within the seven-item rule), one-liners, hub ordering overrides, related-link overrides, landing pages, tours, tenant help notes, user accessibility preferences.

## 10. Security, privacy and audit

| Threat / duty | Control |
|---|---|
| Private content indexed (NN-31) | `noindex` headers on authenticated hosts; signed URLs; previews protected; sitemap generator reads only PUBLISHED public pages; CI crawler test against staging asserts no private path is reachable. |
| Script injection on public pages (SAQ A) | CSP with nonces, SRI, script inventory, allow-listed third parties after consent; CMS HTML sanitised on an allow-list; no raw HTML block. |
| Malicious DOCX | Virus scan, macro/OLE stripping, conversion in an isolated Gotenberg container without network. |
| Personal data in leads (DPDP) | Minimal fields, purpose-wise consent artefacts, 30-day local retention, encrypted columns, restricted role, hand-off only to OH (NN-19, NN-26). |
| Analytics leakage (NN-32) | No drafter answers, document text, OTPs, PAN or Aadhaar in analytics, logs or support tickets; OpenTelemetry scrubber; search queries logged in aggregate with PII patterns removed. |
| Tutorial captures leaking customer data | Captures run only against the synthetic demo tenant; job fails if the tenant is not flagged synthetic (`LD-HLP-006`). |
| Defamation, copyright | Plagiarism gate, competitor-brand detector, quotation attribution, takedown request route to the Grievance Officer (IT Rules 2021 timelines [VERIFY 2026 amendment]). |
| Unlawful professional promotion (NN-21) | Locked advocate bio mode; no advocate testimonials; claims gate; marketplace rendering rules from Appendix M. |
| Audit (NN-02, NN-45) | Every CMS, glossary, redirect, crawler, consent-text and kill-switch change written to the ledger in-transaction; review decisions store reviewer identity and credential. |

DPDP items: notices per purpose on lead forms, consent withdrawal, retention schedules (§7.2), children (no lead capture under 18), grievance route, Consumer Help brand privacy notice separate (NN-23).

## 11. AI touchpoints and guardrails

| Feature | Agent / runtime | Autonomy | Human confirmation | Guardrails and evaluation |
|---|---|---|---|---|
| Rewrite manual text into page drafts; FAQs from question sources; metadata; one-liner suggestions | `AGT_CONTENT_STUDIO` (Appendix H #25; X-27; R4 LV-20) via P09 | L1 (drafts only) | Maker edits, checker approves, legal reviewer for legal types | Must not copy source phrasing (plagiarism gate), must cite from `rul` (unresolved → "unverified"), no invented sections or cases (NN-14); evaluation set of 50 manual sections scored for accuracy, originality and reading level each model change |
| Translations of pages, glossary and help | `TRANSLATE_PORT` + content agent post-edit suggestions | L1 | Human reviewer per language (NN-48) | Labelled MT; legal citations untranslated |
| Vidhi help mode in the help panel | Vidhi runtime (P09) | L0 (answers) | — | Retrieval only from published help and glossary; citations to articles; refuses legal advice and points to the drafter or a professional; AI disclosure at start; no tenant data used unless the user is in a tenant session and asks about their own screen |
| Draft free with Vidhi — AI-custom lane | P06 Drafting Studio | L0–L1 | User decides; professional review offered | "AI draft — not reviewed by a professional" label (NN-14); AUP disclosures; customer data not used for training (NN-15) |
| Tutorial narration TTS, caption drafts | TTS/ASR adapters | L1 | Writer approves | Synthetic-media label |
| Alt text suggestions | Vision model via `packages/ai` | L1 | Writer approves | Never auto-published |

No AI in free tools, eligibility badges, prices, testimonials or crawler policy.

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p21/*.feature`)

```gherkin
@P21-AT-01 @NN-31
Scenario: Every sitemap URL renders without JavaScript
  Given the production build of apps/public
  When CI fetches each sitemap URL with JavaScript disabled
  Then each response has one h1, a unique title and meta description, a self-canonical and at least 150 words in main
  And no URL on my., work. or admin. hosts is present in any sitemap

@P21-AT-02
Scenario: Legacy URLs resolve in one hop
  Given the legacy URL list from P00 including https://lawdocs.in/buy/rent and /compliance-services/rbi_compliance/icaap-policy
  When each URL is requested
  Then the response is 200, a single 301 to a canonical www URL, or 410
  And no redirect chain or loop exists

@P21-AT-03 @NN-07
Scenario: Non-eligible instrument shows a wet-ink pack instead of eSign
  Given the document page for "General power of attorney"
  And Appendix F marks it not eligible under the IT Act First Schedule
  When the page renders
  Then the eSign badge reads "Not valid" with the reason
  And the primary CTA reads "Print, sign, stamp and register"
  And no eSign checkout link is present

@P21-AT-04 @NN-14
Scenario: AI-custom lane output is labelled
  Given a signed-in individual on the residential rent agreement page
  When they choose "Ask Vidhi to adapt this" and Vidhi returns a draft
  Then the draft is labelled "AI draft — not reviewed by a professional"
  And a paid professional review offer is shown
  And the template-lane draft from the questionnaire carries no such label

@P21-AT-05 @NN-21 @NN-49
Scenario: Testimonial about an advocate is rejected
  Given a verified customer testimonial that praises a named advocate
  When a publisher attaches it to the "Hire a professional" block
  Then publication fails with LD-WEB-012
  And no photo field is available on any testimonial

@P21-AT-06 @NN-22
Scenario: Fee breakdown is shown before payment
  Given the service page "Private Limited Company Registration Online"
  When the price card renders from the catalogue
  Then professional fee, LawDocs platform fee, government fee and GST are shown as separate lines with a total
  And the CMS editor has no field to type a price

@P21-AT-07 @NN-20
Scenario: Unapproved claim blocks publication
  Given a draft home page block stating "10,000+ agreements signed"
  And no approved claims-register entry exists for that number
  When the publisher submits for review
  Then submission fails with LD-WEB-002

@P21-AT-08 @NN-18
Scenario: Maker cannot approve own post
  Given a publisher created a post from a DOCX import
  When the same publisher tries to approve it
  Then the action fails with LD-WEB-015

@P21-AT-09
Scenario: DOCX import from categorised folders creates drafts
  Given a zip with folders "Property/Rent" and "Startups/Funding" containing 12 .docx files
  And the folder-category map maps both folders
  When the publisher imports the zip
  Then 12 posts are created in DRAFT with mapped categories
  And images without alt text are listed as blocking warnings
  And re-importing the same zip creates no duplicates

@P21-AT-10
Scenario: Outdated law is flagged
  Given a draft pleading page citing "Section 438 CrPC" without a current provision
  When the linter runs
  Then submission fails with LD-WEB-017 suggesting "Section 482 BNSS (formerly Section 438 CrPC)"

@P21-AT-11
Scenario: Copied competitor content is blocked
  Given a draft service page containing the text "consult Vakilsearch"
  When the publisher submits it
  Then submission fails with LD-WEB-018

@P21-AT-12
Scenario: State variant without material differences is blocked
  Given a draft Rajasthan variant of the residential rent agreement with one recorded State fact
  When the editor submits it
  Then submission fails with LD-WEB-009

@P21-AT-13 @NN-30
Scenario: Page without a reviewer is not indexed
  Given a published document page whose reviewer record was removed
  When the page renders
  Then the robots meta is "noindex" and the URL is absent from the sitemap

@P21-AT-14 @NN-26 @NN-19
Scenario: Lead hand-off carries consent and no draft content
  Given a visitor completes the drafter questionnaire and submits the lead form with only "respond to my request" ticked
  When the lead is sent to the Operations Hub CRM
  Then the payload includes the consent artefact reference and UTM data
  And the payload contains no questionnaire answers or draft text
  And no marketing consent is recorded

@P21-AT-15
Scenario: Sensitive intent is excluded from ad conversions
  Given a lead captured on a domestic-violence document page
  Then the lead sensitivity is HIGH
  And no ad-platform conversion is queued for it

@P21-AT-16 @NN-50
Scenario: Countdown without a real event is blocked
  Given a landing page with a countdown block not bound to an event record
  When the publisher submits it
  Then submission fails with LD-WEB-021

@P21-AT-17
Scenario: Video loads nothing from YouTube before activation
  Given a visitor who rejected embedded-media cookies opens a vlog page
  Then no request is made to any YouTube domain
  And the full transcript and chapters are visible
  When the visitor activates "Play once"
  Then the player loads from youtube-nocookie.com with captions on

@P21-AT-18 @NN-48
Scenario: Machine-translated page is not published without review
  Given a Hindi machine translation of the rent agreement page
  When the editor tries to publish it without a Hindi reviewer approval
  Then publication fails with LD-WEB-022 and no hreflang points to it

@P21-AT-19 @NN-28
Scenario: "i" popover meets content-on-hover rules
  Given a form label "eStamp certificate" with key hlp.sgn.estamp_certificate
  When a keyboard user presses Enter on the "i" button
  Then a non-modal popover opens with the plain definition
  And Escape closes it with focus remaining on the button

@P21-AT-20
Scenario: Untagged jargon fails the build
  Given a UI string tagged term="CNR number" without a registered help key
  When the lint step runs
  Then the build fails with LD-HLP-001

@P21-AT-21
Scenario: Tutorial capture refuses a real tenant
  Given the capture workflow configured with a non-synthetic tenant id
  When the workflow starts
  Then it fails with LD-HLP-006 and no screenshot is stored

@P21-AT-22
Scenario: Stale tutorial is flagged after a UI change
  Given a published tutorial whose screen changed by more than 2%
  When the release capture runs
  Then the tutorial state becomes STALE and the help article shows "Being updated"

@P21-AT-23 @NN-35
Scenario: Advertising slot stays empty when the stream is OFF
  Given the advertising revenue stream is OFF
  When any blog page renders
  Then no ad slot markup or ad script is present

@P21-AT-24 @NN-11
Scenario: Tenant help notes and accessibility preferences are exported
  Given a tenant with 3 help notes and users with saved accessibility preferences
  When the tenant runs a full LD-EXPORT-1.0 export
  Then "99 System Data (CSV and JSON)/Help Notes.csv" and "Accessibility Preferences.csv" are present and listed in manifest.json

@P21-AT-25 @NN-28
Scenario: Accessibility feedback is acknowledged on time
  Given a visitor submits the accessibility feedback form without a CAPTCHA
  Then an acknowledgement is sent within 48 hours
  And the issue appears on the accessibility board with an SLA due date

@P21-AT-26 @NN-38
Scenario: Free tool with an unverified rule stays disabled
  Given the limitation-period calculator depends on a rules-register row marked [VERIFY]
  When the tool page renders
  Then the calculator is disabled with the note "Being verified" and the page shows the method only

@P21-AT-27 @NN-32
Scenario: Drafter answers never reach analytics or logs
  Given a visitor with analytics consent completes the rent agreement questionnaire
  Then analytics events contain only the step names and counts
  And no questionnaire answer, party name or address appears in analytics, traces or logs

@P21-AT-28 @NN-45 @NN-02
Scenario: Publishing writes the audit ledger in the same transaction
  Given a checker approves and publishes a page version
  When the database transaction commits
  Then an audit-ledger entry for the publish exists in the same transaction
  And a simulated failure after the version insert leaves neither the version nor the audit entry

@P21-AT-29 @NN-29
Scenario: Unregistered setting cannot be read
  Given code reads the key "web.drafter.new_limit" that is not registered in Appendix R
  When the API starts in CI
  Then the settings registry check fails the build
```

## 13. Exit gate, deliverables and open items

**Exit checklist (per wave)**

- [ ] No-JS crawl gate green for every sitemap URL; legacy URL suite green (P21-AT-01/02).
- [ ] Lighthouse CI and field CWV within budgets for every template; JS budgets enforced.
- [ ] Structured-data validation green; no `Review`/`AggregateRating`/`HowTo` emitted.
- [ ] Wave content published: Wave 1 top 50 pages (Appendix N §N.9) + home, product, pricing, marketplace shell, legal policies (Appendix O), accessibility statement; Wave 3 ≈626 manual-derived pages, each with reviewer of record, plagiarism pass and outdated-law pass.
- [ ] Content Studio: DOCX import, maker-checker, legal review, scheduling, rollback, preview, export demonstrated by `OPS_CONTENT_PUBLISHER` without developer help.
- [ ] Glossary coverage met for the wave; lint enforced in all apps.
- [ ] Tutorials and tours for the wave's core journeys published with captions; ISL renditions for the core set by Wave 3.
- [ ] Appendix U release gate passed (axe zero serious/critical; manual NVDA, JAWS, VoiceOver, TalkBack, keyboard-only and 400% zoom audits; user testing round with disabled users); conformance report published.
- [ ] Lead hand-off to OH CRM verified end to end with consent artefacts; Appendix Y entry for LawDocs as CRM caller submitted.
- [ ] Settings registered in Appendix R; help keys registered; error codes registered with help keys.
- [ ] **Help-key registry (owned here; X-10).** Help keys and settings are separate registries: a help key is `hlp.<module>.<term>`, and terms not tied to one module use `hlp.gen.<term>`; no key uses the form `hlp.hlp.<term>`, and help-centre and website terms are registered as `hlp.gen.*` or `hlp.web.*`. Seeded in this phase: `hlp.gen.indemnity`, `hlp.gen.consideration`, the Appendix U keys `hlp.gen.accessibility_preferences`, `hlp.gen.easy_read`, `hlp.gen.listen`, `hlp.gen.isl_video`, `hlp.gen.assisted_signing`, `hlp.gen.assisted_kyc`, `hlp.gen.accessibility_feedback`, and the Appendix N §N.12 priority list. Registered for other phases at integration review: `hlp.chp.vehicle_loan` (P15 FR-P15-70 — "My vehicle loan": what papers to keep, NOC and Form 35 on closure, where to complain about recovery conduct; Consumer Help brand locale set). The registry lint (`LD-HLP-001`) also fails any key using the `hlp.hlp.` form.
- [ ] Export-map entries registered in `xpt.export_map` (below).

**Demo script:** (1) open `/documents/property-transactions/rent/rent-agreement-residential` with JS off and show full content; (2) draft in 7 answers, sign up inline, save to vault; (3) open the power-of-attorney page and show the wet-ink pack; (4) import a categorised DOCX folder, fix a flagged CrPC citation, submit, approve as a second user, schedule; (5) show the post live with reviewer footer, IndexNow log and OH asset-library push; (6) open the help panel on the signing screen, open "i" for "eStamp certificate", play the tutorial with captions; (7) submit accessibility feedback and show the SLA clock.

**Export-map entries (`xpt.export_map`, NN-11)**

| Record type | Folder in `LD-EXPORT-1.0` |
|---|---|
| `hlp.tenant_note` | `99 System Data (CSV and JSON)/Help Notes.csv` (company) |
| `hlp.user_pref` | `99 System Data (CSV and JSON)/Accessibility Preferences.csv` (company, professional; individual: `99 System Data/` — Appendix K §K.3.2, §K.3.5) |
| `web.testimonial` (the user's own, with consent record) | `99 System Data (CSV and JSON)/Testimonials and Consents.json` (individual: `99 System Data/`) |
| `hlp.a11y_issue` (submitted by the signed-in user) | `99 System Data (CSV and JSON)/Accessibility Feedback.csv` (individual: `99 System Data/`) |
| Platform content (LawDocs' own CMS, not tenant data) | Platform export via FR-P21-91 (Markdown + JSON + assets) |

**Open items (Appendix W candidates)**

| OI | Item | Owner |
|---|---|---|
| OI-P21-01 | Public phone number and contact identity for the site (three numbers in use — R5 §1.3) | [OWNER] |
| OI-P21-02 | AI training-bot and `Google-Extended` policy | [OWNER] board decision |
| OI-P21-03 | Folder list and category mapping for the owner's blog Word files | [OWNER] |
| OI-P21-04 | `[Consumer Help Brand]` name, domain and entity profile (D-06) | [OWNER] |
| OI-P21-05 | LawDocs as caller of OH CRM (`POST /v1/crm/requests`, `/v1/crm/leads`, `/v1/crm/activities`), ticket and asset-library APIs — now proposed in Appendix Y §Y.8/§Y.9 and Appendix X §X.22; asset-library path to be fixed by the OH owner (OI-Y-10) | Pack lead / OH owner |
| OI-P21-06 | **Resolved by X-22:** Content Studio is an `apps/console` area restricted to `OPS_CONTENT_PUBLISHER`, `PLT_CONTENT_EDITOR` and `PLT_LEGAL_REVIEWER`; Super Admin not required | Pack lead (closed) |
| OI-P21-07 | Verify Google FAQ rich-result deprecation, Shorts/Reels length limits, YouTube privacy-enhanced-mode behaviour and current AI crawler user agents at build | SEO lead [VERIFY] |
| OI-P21-08 | Plagiarism provider terms and data handling | `PLT_DPO` [VERIFY] |
| OI-P21-09 | Counsel view on cookieless aggregate analytics under DPDP and on "English prevails" clause for translated policies | [COUNSEL] |
| OI-P21-10 | Verify IT Rules 2021 grievance and synthetic-media labelling text as amended 20 Feb 2026 for site footer and video labels | [VERIFY] / [COUNSEL] |
| OI-P21-11 | Engage ISL interpreters and a disabled-user testing panel (Appendix U §U.8) | `OPS_QA_REVIEWER` |
