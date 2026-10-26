# Phase P23 — Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (monorepo, `apps/public` scaffold, audit ledger, object storage, observability);
> - **P01** (identity, consent ledger, company lookup through PAN/CIN adapters, trial tenant provisioning);
> - **P02** (settings registry, terminology overrides, menu registry — the "i" keys and help keys are registered there);
> - **P03/P05** (regulatory content library and Updates feed — the public Regulatory Updates hub reads a published, human-summarised subset);
> - **P15** (entity families and applicability — the health check selects its question set per family);
> - **P18** (integration gateway: MCA/PAN lookup adapters, Operations Hub CRM events, Brevo through the Hub);
> - **P20** (pricing catalogue and configurator — this phase renders the public pricing page; P20 owns its data and checkout);
> - **P21** (public marketplace and FinLegal Academy listings — this phase renders the public entry points and SEO for them).
>
> **Sequencing:** the marketing site shell, CMS, claims register and accessibility foundation (§4A–4D, §4L) start as soon as P00/P01 exit and can run in parallel with P03–P10 on a growth squad. The health check (§4E) needs P15's entity taxonomy and P01's lookup adapters. Tutorials (§4K) start once the first tenant modules (P03–P04) are stable and are refreshed every release thereafter. The accessibility release gate (NN-21) applies to **every** phase from P01 onwards; this phase owns the standard, the tooling and the conformance report.
>
> **Binding appendices:** Appendix P (copy deck, health-check question bank, tutorial and video catalogue, SEO/GEO clusters and schema), Appendix R (competitive research), Appendix C (information architecture of the authenticated apps), Appendix N (pricing data), Appendix O (marketplace catalogue), Appendix Q (security and privacy), Appendix U (settings catalogue).
>
> **Requirements covered:** R-016, R-020, R-022, R-028, R-030 (public surfaces), R-032, R-034 (pricing presentation), R-036 (public marketplace and academy entry), R-037 (benefit explanation), R-045 (marketing funnel surfaces, with the Hub as system of record), R-069 (health check → trial entry), R-070 (pricing page rendering), R-100 (memorable client experience), R-101 (verification of published claims).
>
> **Estimated effort:** 7 two-week sprints for a growth squad of 7 (2 front-end, 1 back-end, 1 content engineer, 1 accessibility specialist (IAAP CPACC/WAS), 1 designer, 1 QA), plus a content team of 3 (regulatory writer, technical writer, video producer) that continues after the phase as a standing function. *(v1.1: +3 sprints for v1.1 scope (markets and locales, global health check, new module pages, tutorials, help improvements) — 10 in total)* *(v1.2: +1 for the Health Check Studio — 11 in total)*


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §4Q global website: locales `en-IN` (default), `hi-IN`, `en-GB`, `en-US`, later `ar-AE` (RTL); market subfolders `/ae/`, `/sg/`, `/uk/`, `/eu/`, `/us/` with hreflang; country solution pages generated from the jurisdiction-pack registry so only PUBLISHED packs are advertised and PILOT packs are labelled (NN-53) (FR-P23-177–FR-P23-183).
- New §4R global health-check variant for foreign subsidiaries and multi-country groups (20 questions, Appendix P §P.7) with jurisdiction-aware scoring and no bureau or registry pulls beyond licensed, consented look-ups (X-07) (FR-P23-184–FR-P23-188).
- New §4S pages and tutorials for the v1.1 modules and the AI agent workforce: Legal & Contracts, ESG & BRSR, AI Governance, Global Entities, Reports Studio, Vidhi agents, MCP connection (FR-P23-189–FR-P23-193).
- New §4T help improvements from client feedback: Hindi coverage of the top 20 maker/checker screens (IMP-097), contextual 60-second videos and first-visit tours on every screen (IMP-098), inline 'i' help with regulation snippet and plain-language explainer (IMP-099) (FR-P23-194–FR-P23-197).
- Appendix P extended: copy deck for global and new-module pages (§P.7), INTL health-check bank (§P.8), tutorials T-45–T-62 (§P.9), global keyword clusters and schema (§P.10).

**v1.2 changes (25 October 2026)** *(v1.2)*

- New §4U **Health Check Studio** (D-55): the super admin builds health-check **sets** (`HC-SET-<NNNN>`, versioned) by selecting library questions **by CompID** with search and filters (family, authority, instrument, section, department, function, compliance type, risk), sets questions per section and in total, weights, order, plain-language wording, answer options and scoring, and branching; previews as a sample entity; publishes through maker-checker; runs A/B comparisons; and reads drop-off analytics (FR-P23-198–210).
- Each health-check item binds to one or more CompIDs, or to a **library placeholder ID** (`LPH-…`) where the question sheet is not yet written; bindings follow CompID lineage and resolve automatically when sheets publish (FR-P23-206).
- Answers **pre-fill the tenant baseline by CompID** on conversion — self-declared, never "Compliant" (FR-P23-207); the existing 50-question bank and the 20-question global bank are seeded as `HC-SET-0001` and `HC-SET-0002` with the CompID map in Appendix P §P.11 (FR-P23-208).
- The result stays labelled **Health Check Score** everywhere, including Studio previews, experiments and analytics (X-46; FR-P23-210). New errors LDC-WEB-040–052.

---

**v1.3 changes (26 October 2026)** *(v1.3; IPB-04, IPB-05, IPB-06, IPB-07 adoption — D-66, D-71–D-74, D-76; audit findings for LDC)*

- New §4V **Public Brand Studio, standard pages and binding footer** (IPB-04 §04.3.2, §04.3.7, §04.3.8): the public site reads one `brand_pack` (theme tokens, logo, favicon, OG image, `brand.app_name`, host map, email identity, footer social links) edited in `apps/console › Studio › Brand` with maker-checker and rollback; Team and Leadership pages from `team_member` items with photo consent; **Investors page behind `web.investors.enabled` (default OFF)** with the locked disclaimer block and a legal-review gate; Careers, Press and Partners pages; Contact with Delhi, Noida and Jaipur offices; Documentation and Changelog; `Organization` JSON-LD with `sameAs` (FR-P23-211–FR-P23-219). FR-P23-12 is amended: the footer follows the IPB binding specification including social links and the officers line.
- New §4W **Blog toggle, bulk Word import and user posts; Vlog; Resources library; policy pages; feedback widget; marketing tooling; tutorial captions** (IPB-04 §04.3.4–§04.3.6, §04.3.10–§04.3.11; IPB-05; IPB-06): blog ON/OFF without 404s, bulk import of `.docx` articles through the LawDocs `DocxImportWorkflow` pattern (preview, diff, undo), **user posts** behind `web.blog.user_posts.enabled` (default OFF) with pre-moderation and the "Author's view" label (NN-64, D-73); vlog with mandatory captions and transcripts; a Resources library (reports, presentations, templates, checklists) with versions, optional gating and the Resources Download Terms; the IPB-05 policy set rendered from Appendix AD instances with version archive and re-consent; the feedback widget and idea board (IMP-142 absorbed); `TAG_MANAGER_PORT` option with consent gating (NN-62); captions, live captions and visual alerts explicit for every tutorial video (FR-P23-220–FR-P23-235).
- §4H "i" registry confirmed as the group seed: key format `hlp.<module>.<term>`, CI lint, regulatory-reference panel; LDC publishes `in.infrabyx.content.GlossaryEntryPublished.v1` (FR-P23-233).
- §4L accessibility extended: dyslexia-friendly font option (`a11y.text.font`), captions/live captions/visual alerts as release gates, `gov_facing` mode (FR-P23-230–FR-P23-232).
- New state machines §5.8 brand-pack version, §5.9 user post, §5.10 resource version, §5.11 policy instance; screens SCR-WEB-56–SCR-WEB-63; tables, APIs, events, settings keys (`brand.*`, `web.blog.*`, `web.vlog.*`, `web.resources.*`, `web.investors.*`, `fb.*`, `mkt.*`, `pol.*`), errors LDC-WEB-053–LDC-WEB-062, acceptance tests P23-AT-29–P23-AT-40, open items OI-P23-34–OI-P23-38.
- Health Check Studio (§4U) and the Claims Register (§4D) are unchanged and are referenced by the IPB as the ecosystem pattern for every product's free funnel and claims lint.
- Companion content: `content/LawDocsComply_Website_Content_v1.0.md` (full copy deck for every standard page, written to the Claims Register rules) and `design/UI_UX_Design_Brief_v1.3.md` (palette, typography, placeholders) — both binding on tone and placement; Appendix P keeps the copy system, health-check bank and tutorial catalogue.

---

## 1. Objective and business outcome

LawDocsComply is sold self-serve to thousands of NBFCs, co-operative societies, intermediaries and companies that will not take a sales call before they trust the product. The public website, the free Compliance Health Check and the learning surfaces are therefore the first product most buyers use. This phase delivers a fast, accessible, search- and AI-discoverable public site; a free health check that gives a genuinely useful, indicative result and converts into a 7-day trial; a help centre, "i" glossary and tutorial library that let users understand regulatory terms and features without calling support; and an accessibility programme that makes every LawDocsComply surface usable by people who are blind, low-vision, deaf, hard of hearing, motor-impaired or neurodivergent — which is also a regulatory obligation that many LawDocsComply customers themselves now carry (SEBI digital-accessibility circular of 31 July 2025; draft RPwD (Amendment) Rules 2026).

| Outcome | Exit-gate measure |
|---|---|
| Content visible to crawlers and AI retrieval | Every public page returns its full primary content in the initial HTML response (no client-side-only rendering); `curl` of `/`, `/pricing`, `/solutions/nbfc`, `/health-check`, `/glossary/crar` shows headline, body and structured data. `/llms.txt` is served as `text/plain`. (Fixes the 25 Oct 2026 finding that the live site returns an empty SPA shell — Appendix R §R.9.) |
| Fast and stable | Core Web Vitals at the 75th percentile on mobile (CrUX or RUM): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; Lighthouse performance ≥ 90 on the five template types |
| Free health check works end to end | An anonymous visitor completes the check for any of the 12 launch families (Appendix P §P.3) in ≤ 12 minutes median; receives an on-screen result immediately, a PDF and a share link; the lead reaches the Operations Hub CRM within 60 seconds with consent flags; the visitor can start a 7-day trial with the entity profile pre-filled in ≤ 2 clicks |
| Honest results | Every report carries the D-15 disclaimer; every score is reproducible from the stored answers, question-bank version and scoring-model version (NN-22); no report says "compliant", "certified" or "audit-ready" (NN-19) |
| Claims governed | 100% of numeric claims, logos, testimonials, certifications and regulatory-recognition statements on published pages link to an approved, unexpired Claims Register entry; the build fails otherwise |
| Self-help reduces support | Every menu item, column header and form label in the tenant app that names a regulatory or product term has an "i" key resolving to a published glossary entry (coverage report = 100% of registered keys); help panel opens contextually from every screen; ≥ 40 tutorial videos with captions and transcripts published (Appendix P §P.5) |
| Accessible | WCAG 2.2 Level AA conformance of the public site and of every authenticated screen shipped to date, evidenced by automated checks in CI (zero serious/critical axe violations), a manual assistive-technology test cycle and an independent IAAP-certified audit; an Accessibility Conformance Report (ACR) published in human- and machine-readable form; an accessibility grievance channel live (NN-21) |
| Measurable discoverability | Search Console and Bing Webmaster verified; IndexNow pings on publish; a monthly "AI answer panel" of 30 fixed buyer prompts runs and reports named/cited presence separately (§4M.12) |

---

## 2. Scope (in / out)

**In scope**
- `apps/public` (Next.js 16, App Router, static generation with incremental revalidation) for the marketing site, solutions pages, pricing page rendering, marketplace and academy public entry pages, resources, regulatory updates hub, glossary, blog, case studies, trust centre, legal pages and the health check.
- The `web` module: headless CMS (pages, blocks, versions, locales, redirects, experiments), Claims Register, health-check engine (question banks, scoring models, sessions, reports, share links), leads and marketing consents, public regulatory-update summaries.
- The `hlp` module: glossary and "i" key registry, help-centre articles, contextual help, product tours and checklists, tutorial library and learning paths, media assets (images, diagrams, screenshots, videos, captions, transcripts, sign-language renditions), release notes.
- The accessibility programme across all apps: design-token corrections, component rules, user accessibility preferences, document and chart accessibility, the test plan, the accessibility statement and ACR, the accessibility grievance channel, the CI gate.
- Technical SEO/GEO: rendering, metadata, structured data, sitemaps, robots and AI-crawler policy, `llms.txt`, internal linking, redirects from the current site, measurement.
- Ethical funnel and nurture surfaces: landing-page variants, webinar registration, paid "expert review" tripwire hand-off to P20/P21, trial onboarding checklist; the Hub (Appendix X) remains the system of record for leads, campaigns and sends.

**Out of scope (owned elsewhere)**
- Pricing catalogue, configurator logic, checkout, invoices (P20). This phase renders and tests the page.
- Marketplace listings, provider onboarding, orders (P21); academy course delivery (trainings.lawdocs.in LMS).
- CRM, campaign automation, Brevo/Adobe Express sends, social calendar, PR, staff performance (Infrabyx Operations Hub; Appendix X).
- Tenant onboarding wizard internals and trial provisioning (P01); this phase hands over a pre-fill payload.
- Authenticated-app information architecture and screen inventory (Appendix C, P02) — this phase supplies help, glossary and accessibility layers into it.
- A native mobile app (D-01: PWA only in v1.0).

---

## 3. Personas and permissions touched

| Role code | What they do in this phase |
|---|---|
| `anon` | Browses the public site, runs the health check, reads glossary/help/tutorials, registers for webinars, starts a trial |
| `lead` | A visitor who has given contact details and consent; can reopen their health-check report through a magic link, retake the check, manage marketing preferences, request deletion |
| `ten_admin`, all `ten_*` users | Use contextual help, the "i" glossary, tours, tutorials and accessibility preferences; report accessibility problems; the tenant admin may add tenant terminology overrides (P02) that change "i" labels, never the underlying legal definition |
| `plt_content_maker` (scope `web` / `hlp`) | Drafts pages, blocks, glossary entries, help articles, tutorials, health-check questions and claims |
| `plt_content_checker` | Reviews and approves drafts (maker ≠ checker, NN-05); approves claims evidence |
| `plt_content_publisher` | Publishes approved versions and schedules releases; rolls back |
| `plt_super_admin` | Configures settings in §9; cannot bypass the Claims Register or the accessibility gate except through a recorded Correction Entry with dual approval (D-02) |
| `plt_security_officer` | Owns trust-centre content, `security.txt`, sub-processor list |
| `plt_support` | Reads help analytics, triages accessibility grievances with the accessibility nodal officer |
| OH marketing staff (Hub users) | Do not log into LDC; they receive leads and events from LDC through the Integration Gateway and manage campaigns in the Hub. Web editors who are Hub staff are provisioned in LDC `apps/console` with `plt_content_maker` scope `web` only |

Proposed (master notes): split `plt_web_editor` / `plt_web_publisher` from the regulatory-content roles so marketing staff never hold regulatory-content publishing rights.

---

## 4. Functional requirements

### 4A. Public application, rendering and performance

- **FR-P23-01** `apps/public` is a separate Next.js 16 application deployed behind the CDN, sharing the design-token package (`packages/ui-tokens`) and component library (`packages/ui`) with the tenant app so that the public site and the product look and behave alike.
- **FR-P23-02** Rendering: every content route is statically generated at build or on first request with incremental revalidation (`revalidate` per page type: home/solutions 1 h; blog/glossary 24 h; regulatory updates hub 10 min; pricing on catalogue publish event). Interactive islands (health check, pricing configurator, search) hydrate progressively; the primary text of the page is always present in the server HTML.
- **FR-P23-03** No route serves an empty shell to non-JavaScript clients. A CI check fetches every sitemap URL without JavaScript and fails if the `<main>` element has fewer than 50 words or lacks the page `<h1>`.
- **FR-P23-04** Performance budgets per template: JS ≤ 150 kB compressed on content pages, ≤ 300 kB on the health check; hero images AVIF/WebP with explicit dimensions; fonts self-hosted, subset (Latin + Devanagari first), `font-display: swap`; third-party scripts only after consent and only from an allow-list (§4O).
- **FR-P23-05** Internationalisation: English at launch; Hindi as the second locale for solutions pages, glossary, health check and help articles (flag `web.locale.hi.enabled`); locale-prefixed routes (`/hi/...`), `hreflang` pairs, locale switcher reachable by keyboard and announced to screen readers; translated pages pass the same review workflow (AI draft → human reviewer, NN-04). Further Indian languages (Tamil, Telugu, Marathi, Bengali, Gujarati, Kannada, Malayalam, Punjabi, Odia) are content additions, not code changes.
- **FR-P23-06** Preserve every current URL: the 15 URLs in the live sitemap (Appendix R §R.9) either keep their slug or receive a 301 to the new page; `web.redirects` holds the map; a CI test asserts no 404 for the legacy list.
- **FR-P23-07** Status and incident page at `status.lawdocscomply.com` (static, hosted independently of the main stack) showing component status and maintenance windows; linked from footer, trust centre and the tenant app's help panel.

### 4B. Information architecture of the public site

- **FR-P23-10** Top navigation (desktop) — maximum seven items, each opening an accessible disclosure menu (not hover-only):
  1. **Solutions** — by entity family: NBFCs (all layers and types), Banks and Small Finance Banks, Urban and Rural Co-operative Banks, Credit Co-operative Societies, Other Co-operative Societies, Asset Reconstruction Companies, SEBI-regulated entities (listed companies, mutual funds, AIFs, REITs/InvITs, intermediaries), IFSCA entities (GIFT City), IRDAI insurers and intermediaries, Companies and LLPs, Data protection and cyber security, Labour, HR and POSH. Each family page lists applicable regulators and instrument packs pulled from the content library (P03/P15), the modules most used by that family, the free health check pre-set to that family, relevant marketplace services and academy courses.
  2. **Platform** — module pages: Compliance Workspace, Regulatory Change, Governance and Company Secretarial, Policies and Documents, Risk Management, Risk Assessment Lab (ICAAP, stress testing), Audit, Return Studio, Data Protection and Cyber, HRMS and Labour, Grievance Redressal, Vidhi AI, Integrations and API, Data Portability.
  3. **Pricing** — rendered from the P20 catalogue (three packages, add-on components, configurator, services-only checkout entry, FAQs).
  4. **Marketplace** — public catalogue entry (P21): categories, featured services, "Hire a virtual CFO/CS/CISO/CCO", retainers, certification-readiness services, academy courses.
  5. **Resources** — Regulatory Updates hub, Glossary, Blog/Insights, Guides and checklists, Webinars, Tutorials and videos, Release notes, Case studies.
  6. **Free Health Check** — primary call to action, styled as a button in the nav.
  7. **Company** — About, Trust Centre, Careers, Contact, Partners (CA/CS/law-firm partner programme, subject to D-06), Press.
  Utility links: Log in, Start free trial, language switcher, accessibility preferences.
- **FR-P23-11** Mobile navigation: a single accessible menu button opens a full-height dialog with the same tree as nested disclosure lists; focus is trapped while open and returned on close; the free health check and trial buttons remain visible in a sticky footer bar that does not obscure focused content (WCAG 2.4.11).
- **FR-P23-12** Footer: full sitemap columns, regulators covered, legal pages (Privacy Notice, Terms, Cookie Notice, Cancellation and Refund, Grievance Officer details as required by IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 r.3(2) where applicable [VERIFY applicability to LDC as an intermediary], DPDP contact for the Data Protection Officer or designated person, Accessibility Statement), company identity (legal name, CIN, registered office, GSTIN — values from Company Secretary, master README decision list), security.txt link, status page.

- *(v1.3)* **FR-P23-12 amended** — the footer follows the IPB-04 §04.3.8 binding specification: (1) product column (modules, solutions, pricing, health check); (2) company column (About, Team, Leadership, Careers, Press, Partners, Contact, Investors when enabled); (3) resources column (Resources library, Blog, Vlog, Help, Documentation, Changelog, Regulatory Updates, Status page); (4) legal column (every Appendix AD policy instance by its IPB-05 key, plus Accessibility statement and Sitemap); (5) officers line — Grievance Officer and DPO names with emails, hours; (6) entity line from the legal-entity record — legal name, CIN, GSTIN, registered office; (7) social links from `brand_pack.social` (LinkedIn, YouTube, X, Instagram, WhatsApp channel) rendered as labelled icons with `rel="me noopener"` and mirrored into `Organization.sameAs`; (8) language switch and cookie-settings link; (9) boundary statement "LawDocsComply provides compliance-management software and curated regulatory information. It does not provide legal, secretarial or audit opinions." Social links and the officers line were missing in v1.2; both are mandatory before the public site goes live.
- **FR-P23-13** Page types (each with its own template, schema and editorial checklist — Appendix P §P.6): Home; Solution (family); Module; Pricing; Marketplace landing / category / service (public render of P21 data); Academy course card (links out to trainings.lawdocs.in); Regulatory update (single item) and Regulatory updates index (by regulator, entity family, date); Glossary term and Glossary index; Guide/Checklist; Blog article; Webinar/Event; Case study; Tutorial (article + video); Release note; Trust Centre; Legal page; Landing page (campaign variant); Health-check flow and report.
- **FR-P23-14** Every Solution page has a "What applies to you" block that is generated from the content library: the list of instruments (title, authority, date, last updated) that the base content packs map to that family, with counts of obligations, so the page is always current and doubles as a public instrument catalogue (R-087). Counts render only from the published library; a page shows "coverage in preparation" rather than a fabricated number when a pack is not yet published (NN-19).
- **FR-P23-15** Cross-sell rules: Solution pages link the family-preset health check, the two most relevant marketplace services and academy courses; Module pages link the tutorial playlist for that module; Glossary terms link the module where the term is used and the instrument where it is defined.

### 4C. Headless CMS (`web` module)

- **FR-P23-20** Content model: `page` (type, slug, locale, status), `page_version` (immutable snapshot of blocks and metadata), `block` (typed: hero, rich text, feature grid, comparison table, FAQ, CTA, testimonial, logo strip, stats, video, image, code, instrument list, pricing embed, health-check embed, marketplace embed, form), `asset`, `redirect`, `experiment`, `author` (person record with permitted professional details only — see FR-P23-27). Blocks are validated against JSON Schema 2020-12; unknown block types are rejected at save.
- **FR-P23-21** Editorial workflow: Draft → In review → Approved → Scheduled → Published → Superseded / Unpublished (§5.2). Maker ≠ checker; the publisher may be the checker. Every transition writes an audit-ledger event (NN-02). Publishing triggers revalidation of affected routes and an IndexNow ping.
- **FR-P23-22** Preview: draft preview URLs are signed, expire in 24 h, are `noindex` and carry a visible "Preview — not published" banner; preview renders the exact production template.
- **FR-P23-23** Pre-publish checks (blocking): broken internal links; missing alt text on informative images (decorative images must be explicitly marked); heading order; reading level warning (Flesch–Kincaid grade > 12 on solution and help pages, warning only); every numeric claim, logo, testimonial, certification, award, customer name or regulator reference bound to an approved Claims Register entry (§4D); meta title ≤ 60 characters and description ≤ 160; structured data validates; axe-core scan of the rendered preview has zero serious/critical violations; Hindi pages have a human reviewer.
- **FR-P23-24** Scheduling and embargo: publish-at and unpublish-at timestamps (IST shown, UTC stored); regulatory-update summaries may carry an embargo until the platform Update is released to tenants (setting `web.reg_updates.public_delay_minutes`, default 0).
- **FR-P23-25** A/B and multivariate experiments for landing pages and CTAs only (never for legal pages, pricing amounts or disclaimers): deterministic bucketing by first-party cookie after analytics consent; without consent, the control variant is served; results exported to the Hub. Experiments may not test dark patterns (§4F.6).
- **FR-P23-26** Versioning and rollback: any published page can be rolled back to a prior version in one action, which itself is a new published version with a reason.
- **FR-P23-27** Authorship and expertise signals: articles show the named author and a named reviewer (e.g., "Reviewed by: Company Secretary, LawDocs") with date reviewed. Author bios for advocates contain only what the Bar Council of India Rules (Part VI, Chapter II, Section IV, r.36, as amended) permit on websites — name, address, contact, enrolment number, date of enrolment, professional and academic qualifications, areas of practice — and no solicitation, success claims or testimonials; similar restraint for CA and CS members under the ICAI and ICSI codes [VERIFY current text with counsel]. Setting `web.authors.advocate_bio_mode = RULE36_FIELDS_ONLY` is Locked.
- **FR-P23-28** Content reuse: product facts (module names, feature lists, counts of instruments/obligations, integrations list) are pulled from the platform registries (P02 module registry, P03 library, P18 connector catalogue) rather than typed into the CMS, so marketing copy cannot drift from what the product does.

### 4D. Claims Register (NN-19)

- **FR-P23-30** `web.claims` records every external-facing assertion that could mislead if untrue: statistics ("X obligations mapped", "Y hours saved"), customer names and logos, testimonials, case-study outcomes, certifications and attestations (ISO/IEC 27001, SOC 2 Type 1/2, PCI DSS), awards, regulator references, integration partnerships, uptime figures, savings calculators' assumptions, competitor comparisons.
- **FR-P23-31** Fields: claim text, claim type, evidence (document in DMS with hash, or a live query against a platform metric), owner, approver (maker ≠ checker), valid-from, expiry (default 12 months; certifications use the certificate validity; live metrics re-evaluate nightly), permitted surfaces (website, health-check report, sales deck, social), status (Draft, Approved, Expired, Withdrawn).
- **FR-P23-32** Blocking rules: a page block referencing an unapproved or expired claim cannot be published; on expiry, the page is automatically republished with the claim replaced by its fallback text (or the block hidden) and the owner is notified. Live metric claims (e.g., count of instruments in the library) render from the metric at build time and never exceed the measured value.
- **FR-P23-33** Locked prohibitions (cannot be configured away): "RBI-approved", "SEBI-approved", "IFSCA-approved", "IRDAI-approved" or any implication of regulator endorsement; "100% compliant"; "guaranteed compliance"; "certified" or "SOC 2 compliant/ISO certified" before the certificate or attestation report is held and recorded; "audit-ready" as a promise; "connected to RBI/CIMS/DAKSH/PRAVAAH" (NN-08, D-13); "AI lawyer", "AI auditor" (Appendix K); testimonials or endorsements from advocates; fabricated or composite testimonials; competitor claims not supported by a dated public source.
- **FR-P23-34** Testimonials and reviews require a signed consent from the person and the organisation (eSign envelope via P07), record whether any consideration was given, and display that disclosure where consideration exists (Consumer Protection Act 2019 misleading-advertisement provisions; CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements 2022 [VERIFY]). Beta customers (e.g., Branch International) appear only with written permission recorded in the register.
- **FR-P23-35** Health-check reports and savings dashboards (P20) draw every benchmark statement from the register (e.g., "penalty under s.92(5) Companies Act for late annual return is …" must cite the section and the register entry).

### 4E. Free Compliance Health Check

The health check is LawDocsComply's lead magnet and the start of self-serve onboarding (R-016, R-069). *(v1.1, X1)* Its result is always labelled **Health Check Score** (Appendix B §B.1.1) — never "Compliance Score", which is the in-product, instance-based score of P04. It must give a credible, personalised, indicative picture in about ten minutes, explain each gap in plain language, and point to the specific LawDocsComply module or marketplace service that would close it — without claiming to be an audit (D-15).

**4E.1 Entry and profile**
- **FR-P23-40** Entry points: nav button; family Solution pages (pre-set family); campaign landing pages (UTM retained); in-app for existing tenants (re-run as a "pulse check" for a new legal entity); partner links with a partner code (D-06 rules apply to any partner reward).
- **FR-P23-41** Step 1 — "Who are you checking?": choose **entity family** (12 launch families, Appendix P §P.3.1) and then **type/layer** from the family's list (e.g., NBFC → Base/Middle/Upper Layer and NBFC type such as ICC, MFI, HFC, CIC, P2P, AA, Factor, IDF; UCB → Tier 1–4; Credit co-operative → State Act / Multi-State; SEBI → listed entity / MF / AIF category / REIT / InvIT / stockbroker / IA / RA / PMS; IFSCA → entity type list per Appendix E; IRDAI → insurer life/general/health/reinsurer, broker, corporate agent, web aggregator, IMF, TPA; Company → private, public unlisted, listed, OPC, Section 8, small company; LLP). A "Not sure which applies?" helper asks three plain questions (Do you lend money? Are you registered with RBI/SEBI/IFSCA/IRDAI/Registrar of Co-operative Societies? Are your shares listed?) and suggests the family; the visitor confirms.
- **FR-P23-42** Step 2 — "Find your organisation" (optional but encouraged): the visitor types the organisation name, CIN/LLPIN or PAN. The page calls `POST /v1/public/org-lookup` which routes through the P18 company-data adapter (MCA master data via a licensed data provider; PAN verification through an authorised provider) [VERIFY provider terms permit lead-generation use]. Returned fields (legal name, constitution, date of incorporation, registered state, status, authorised/paid-up capital, ROC, listed status, NBFC registration where public) pre-fill the profile and refine applicability (e.g., paid-up capital → small-company test under Companies Act 2013 s.2(85) as amended; listed flag → SEBI LODR set). PAN is used transiently for verification, displayed masked, stored only as a keyed token and only if the visitor proceeds to a trial (NN-12); no credit bureau pull is ever made in the health check (D-12 principle, Ecosystem Spec).
- **FR-P23-43** Lookup safety: rate limit (5 lookups per IP per hour, 20 per day; setting), accessible bot protection (privacy-preserving challenge with an audio-free, cognitive-test-free fallback: email one-time link — WCAG 3.3.8), lookup results not cached across visitors, a clear notice that public registry data is being fetched and why (DPDP notice, FR-P23-48).
- **FR-P23-44** Step 3 — profile refiners (≤ 6 questions, family-specific): size band (employees, AUM or balance-sheet size, turnover), states of operation, whether deposits are accepted (co-operatives, NBFC-D), digital lending/LSP use, number of branches, listed securities type. These drive question applicability and segment weights.

**4E.2 Questionnaire**
- **FR-P23-45** *(v1.2: the question set is now the published Health Check Studio set version for the visitor's family, channel and locale — §4U; the bank below is seeded as `HC-SET-0001`.)* The question set is assembled from the versioned **health-check bank** (`web.hc_questions`, Appendix P §P.3.2): 50 questions in 10 segments (Governance and board; Registration, licensing and fit-and-proper; Compliance function and calendar; Policies and procedures; Risk management and capital; Audit and assurance; Returns and regulatory reporting; Customer protection and grievance redressal; Data protection and cyber security; People, labour and POSH). Each question has family variants, an applicability rule (JSON Logic over the profile), a weight (1–3 by consequence severity), a plain-language "why this matters" text with citation, and a mapping to the LDC module and marketplace service that addresses it. Where a variant does not apply, the engine substitutes the family's reserve question so every visitor answers about 50 relevant questions (minimum 40).
- **FR-P23-46** Answer scale: **Yes / Partly / No / Not sure / Not applicable**. "Not applicable" requires a one-tap reason from a short list (e.g., "we do not accept deposits") and is excluded from the denominator; "Not sure" scores zero and lowers the confidence indicator. Each question shows an "i" explanation (glossary key) and the citation.
- **FR-P23-47** UX: one segment per screen with progress ("Segment 3 of 10 — Policies"), save-and-resume through a magic link sent to email after the first segment (the gate is placed after value is shown, not at entry), keyboard-operable radio groups with visible focus, no time limit, no auto-advance that moves focus unexpectedly, error summary at the top on validation, autosave every answer, "Back" never loses answers (WCAG 3.3.7 Redundant Entry: profile data is never asked twice).
- **FR-P23-48** Consent and notice (DPDP Act 2023 s.5–6; DPDP Rules 2025 r.3): before any personal data is collected (email, phone, name), a short layered notice states the data collected, purpose (deliver the report; optionally contact you about LawDocsComply), retention, rights (access, correction, erasure, grievance, nomination), how to withdraw, and the Data Protection Officer/contact; separate unticked checkboxes for (a) report delivery (required to email the report), (b) marketing by email, (c) marketing by WhatsApp/SMS/phone (DLT-registered templates only), (d) sharing the result with a named LawDocs relationship manager for a free call. Consent artefacts are written to the P01 consent ledger with notice version. EU/UK/California visitors (by self-declared country, with IP only as a hint) receive the GDPR/CCPA-aligned variant (lawful basis consent/legitimate interest disclosure; "Do Not Sell or Share" link) [VERIFY whether CCPA thresholds apply to LDC].

**4E.3 Scoring model (deterministic, NN-22)**
- **FR-P23-50** For question *q* with weight *wq* ∈ {1,2,3} and answer score *sq* (Yes = 1, Partly = 0.5, No = 0, Not sure = 0, N/A = excluded): segment score *S* = 100 × Σ(*wq*·*sq*) / Σ(*wq*) over applicable questions. Overall score = Σ(*Wseg*·*S*) / Σ(*Wseg*), where *Wseg* are family-specific segment weights (Appendix P §P.3.3; e.g., Returns and reporting weighted higher for NBFCs and banks, Labour/POSH higher for companies with large workforces).
- **FR-P23-51** Bands: **85–100 Strong foundation**, **70–84 Adequate, with gaps**, **50–69 Needs attention**, **0–49 At risk**. Band names are configurable text; thresholds are Governed settings (§9).
- **FR-P23-52** **Critical-gap override**: any weight-3 question answered No or Not sure creates a "Critical gap" flag listed first in the report, whatever the overall score; three or more critical gaps cap the displayed band at "Needs attention".
- **FR-P23-53** **Confidence indicator** = share of applicable questions answered other than "Not sure" (High ≥ 90%, Medium 70–89%, Low < 70%), shown beside the score so a high score with low confidence is not over-read.
- **FR-P23-54** Peer comparison (flag `web.hc.peer_benchmark.enabled` = OFF until ≥ 30 completed checks exist for the family and the methodology is approved): shows the visitor's segment scores against the anonymised median of the same family and size band; k-anonymity ≥ 30; never shows another organisation's identity.
- **FR-P23-55** The scoring model is versioned (`web.hc_scoring_models`); every report stores bank version, model version, answers and the computed result, so a report can be re-rendered identically years later and a changed model never silently alters an old report.

**4E.4 Report**
- **FR-P23-56** On-screen result page: overall score dial with band text (not colour alone), confidence indicator, radar/bar chart of the ten segments with an adjacent data table (accessible alternative), top critical gaps, a prioritised 30-60-90-day action plan generated deterministically from gaps (ordered by weight × segment weight), and for each gap: what the requirement is (plain language, citation), why it matters (consequence from the Claims-Register-backed penalty library), how LDC helps (module link, tutorial video), whether a marketplace service exists (e.g., "Policy drafting — NBFC Fair Practices Code"), and a "Discuss with an expert" option.
- **FR-P23-57** PDF report (Gotenberg, PDF/UA-tagged, A4): cover with organisation name (as entered or fetched), family, date, report ID and QR verification link; one-page **board-ready summary** (score, band, confidence, top five gaps, recommended actions, disclaimer) suitable for tabling before the Board or management; segment pages with charts and tables; methodology appendix (question bank version, scoring model, bands, limitations); disclaimer on every page footer: "Indicative self-assessment based on your answers. Not legal advice, an audit, an assurance report or a certificate of compliance." (D-15). The PDF is watermarked "Self-assessment" and carries a SHA-256 hash recorded against the report ID.
- **FR-P23-58** Share link: `https://lawdocscomply.com/hc/r/<token>` with a 128-bit random token; default expiry 90 days (setting); owner can revoke or set a password; viewers see the same report read-only with a banner "Shared by …, self-assessed on …"; share views are counted (not identified) for the owner; `noindex`; the PDF can be emailed to colleagues from the page (rate-limited) with the sender's name.
- **FR-P23-59** Narrative summary: an optional two-paragraph plain-language summary may be drafted by Vidhi AI strictly from the computed scores, flags and the bank's explanation texts through a fixed template prompt (Appendix K); it is labelled "AI-drafted summary of your answers", cannot introduce facts not in the inputs, cannot state that the organisation is or is not compliant, and falls back to a deterministic template if the model is unavailable (§11).

**4E.5 Lead hand-off, conversion and nurture**
- **FR-P23-60** On completion, `HealthCheckCompleted` and (if contact consent exists) `LeadCaptured` are emitted through the Integration Gateway to the Operations Hub CRM (Ecosystem Spec scope `crm.request:write`), carrying: lead contact, consent flags and artefact ids, family, type, size band, overall band (not raw answers unless consent (d) is given), top gap segments, UTM/referrer, partner code, report ID. Raw answers stay in LDC; the Hub receives a link that an authorised RM can open only if consent (d) exists (NN-30 analogue for leads).
- **FR-P23-61** "Start your 7-day trial" on the report creates a trial through P01 with a **pre-fill payload**: family, type/layer, fetched organisation master data, profile refiners, and a suggested set of instrument packs and modules derived from the gaps; the onboarding wizard opens at the "Confirm your profile" step. The trial tenant can import the health-check answers as a "baseline assessment" record (one click) *(v1.2: keyed by CompID per FR-P23-207)*, which seeds the compliance dashboard's starting point and the savings ledger baseline (P20).
- **FR-P23-62** Retake: a lead may retake the check at any time; reports are listed in their magic-link portal with trend lines; a tenant can run the check for each legal entity in a group.
- **FR-P23-63** Paid "expert review" upsell: the report may offer a fixed-fee marketplace service (e.g., "45-minute review of your health-check results with a LawDocs compliance professional" or the deeper paid diagnostic "Compliance Health Check — expert-led applicability and gap matrix" priced per Appendix N/O). Checkout runs through P20/P21; this phase only renders the offer. Price and availability come from the catalogue.

### 4F. Ethical growth funnel ("autopilot" with human approval)

The owner asked for the business to run "on autopilot" and pointed to a video-sales-letter funnel (Appendix R §R.10). LawDocsComply adopts the mechanics that respect buyers — a single clear promise, a short video, low-friction entry, source-specific landing variants, an affordable first step and timely follow-up — and rejects those that break law or accessibility.

- **FR-P23-70** Landing-page variants per traffic source and family (e.g., `/lp/nbfc-compliance-video?src=yt`): headline that names the audience and the job ("For NBFC compliance officers: see every RBI obligation that applies to your layer, with owners and due dates"), a 90–180-second explainer video **with player controls enabled, captions on by default, a transcript below and an ISL rendition link where produced**, three proof points from the Claims Register, one primary CTA (free health check or trial), a secondary CTA (book a demo / webinar), a short FAQ, and the full footer. Forms ask for at most name, work email, phone (optional), organisation (or lookup) and consent checkboxes.
- **FR-P23-71** Webinar and masterclass registration (free or low-ticket paid through P20 checkout with GST invoice): registration page, calendar file (ICS) on confirmation, reminders through the Hub, replay page with captions and chapters; attendance data flows to the Hub.
- **FR-P23-72** Nurture sequences are defined and sent in the Hub (Brevo adapter); LDC supplies events and personalisation tokens (family, top gaps, report link). Default sequence templates (Appendix P §P.2.9) are educational first: the report recap, "how to close your top gap" with a tutorial, a regulatory-update digest for the family, a case study, a trial nudge, an expert-review offer. Every message carries the sender identity, unsubscribe/stop, and respects consent channels.
- **FR-P23-73** Retargeting and advertising pixels (Google Ads, Meta, LinkedIn) load **only** after explicit marketing-cookie consent; server-side conversion APIs send only hashed identifiers of consented leads; no health-check answers, scores or regulatory profile are sent to ad platforms (purpose limitation; NN-13 analogue).
- **FR-P23-74** Trial conversion inside the product (in-app, P01/P20): an onboarding checklist with five value moments (profile confirmed → first instrument pack added → first obligation assigned to a maker → first evidence approved by a checker → first board-ready compliance report exported); day-3 and day-6 in-app and email nudges; a clear trial-end page showing what the plan selection will cost and what happens to data if not converted (retained read-only for 30 days, then export offered and deletion scheduled — P19/P20 settings).
- **FR-P23-75** Prohibited patterns (Locked; tested): no fake countdown timers or "only 2 seats left" unless true and evidenced; no pre-ticked consent; no confirm-shaming copy; no hidden costs revealed only at checkout (GST shown inclusive or clearly stated); no forced registration to see the result summary (email gate only for PDF/report storage); no subscription trap (cancellation as easy as sign-up); no disguised ads; no nagging pop-ups that obscure content; no basket sneaking — aligned to the Central Consumer Protection Authority's Guidelines for Prevention and Regulation of Dark Patterns, 2023 (30 November 2023), which list 13 specified dark patterns [VERIFY current list and any 2025–26 amendments or self-audit advisories]. A dark-pattern self-audit checklist runs before every campaign launch and is stored as evidence.

### 4G. Help centre and contextual help (`hlp` module)

- **FR-P23-80** Help centre at `help.lawdocscomply.com` (public articles) and in-app help panel (authenticated articles, tenant-specific notes). Article types: Getting started, How-to (task-based), Concept (what is X), Troubleshooting, Reference (field-by-field), Regulatory explainer (links to glossary and instrument), Release note.
- **FR-P23-81** Contextual help: every screen registers a `help_key` (P02 screen registry; Appendix C). The help panel (shortcut `?` or `Shift+/`, and a persistent "Help" button in the same location on every screen — WCAG 3.2.6 Consistent Help) shows: articles mapped to the screen, the tutorial video for the screen, the glossary terms visible on the screen, "Ask Vidhi" in help mode (answers only from published help and glossary content, with citations — Appendix K), and "Contact support" (P14 support desk for LDC's own customers through the Hub).
- **FR-P23-82** Search: one search box across articles, glossary, tutorials and release notes, with typo tolerance, synonyms (e.g., "CRAR" ↔ "capital adequacy ratio", "GRO" ↔ "grievance redressal officer"), Hindi transliteration, and results filtered by the user's role and entity family.
- **FR-P23-83** Article quality: each article has an owner, last-reviewed date, applicable product version, applicable roles and families, and feedback ("Was this helpful?" with optional comment). Articles not reviewed in 180 days, or tied to a screen whose UI changed (screenshot diff, §4K.7), are flagged stale.
- **FR-P23-84** Tenant notes: a tenant admin can attach internal guidance to any help key (e.g., "In our company, the CCO approves all exceptions"), shown in the help panel beneath LDC's article with a "Your organisation's note" label. Tenant notes are tenant data (RLS, NN-01) and are included in the export package (P19).

### 4H. "i" glossary and term registry

- **FR-P23-90** Every regulatory or product term that appears in a menu, page heading, table column, form label, status chip or report heading is registered as an **"i" key** (`hlp.term.<slug>`, e.g., `hlp.term.crar`, `hlp.term.maker_checker`, `hlp.term.scale_based_regulation`, `hlp.term.icaap`, `hlp.term.kmp`). Developers cannot ship a UI string tagged `term=` without a registered key; a lint rule enforces it.
- **FR-P23-91** Term record: canonical term; abbreviation(s); plain-language definition (≤ 40 words, reading grade ≤ 9); detailed explanation (≤ 200 words); legal/regulatory definition with citation (instrument, section/para, version, date) when the term is defined in law; example; "where you see it in LDC" (screens); related terms; applicable families; authority; status; locale versions. Legal definitions are quoted, not paraphrased, and are linked to the content-library clause so an amendment flags the term for review (P05 change impact).
- **FR-P23-92** UI behaviour: an "i" button (accessible name "About <term>") next to the label opens a non-modal popover on click, Enter or Space (not hover-only); the popover is dismissible with Escape without moving focus, persistent while hovered or focused, and does not obscure the triggering control (WCAG 1.4.13 Content on Hover or Focus); it contains the plain definition, "Learn more" (glossary page), and "Watch" (tutorial) links. On touch devices the target is at least 24 × 24 CSS px (WCAG 2.5.8). Screen readers receive the definition through `aria-describedby` only when the user opens it, so routine navigation is not verbose.
- **FR-P23-93** A user setting "Show term explanations inline" (for new users and for users who prefer it) renders the plain definition beneath the label instead of in a popover.
- **FR-P23-94** Tenant terminology overrides (P02, R-086): if a tenant renames "Department" to "Function" or "Checker" to "Reviewer", the "i" popover shows the tenant label as the heading and "LawDocsComply term: Checker" beneath it, so help articles still match. Overrides never change the legal definition text.
- **FR-P23-95** Public glossary pages (`/glossary/<slug>`) are generated from published terms, each with DefinedTerm structured data, its citation, related terms and an internal link to the solution or module page; the glossary index groups by regulator and topic. Initial coverage target: 400 terms at launch (Appendix P §P.4 lists the first 152 by priority).

### 4I. Product tours and onboarding checklists

- **FR-P23-100** Tours are defined as data (`hlp.tours`: steps with target `data-tour-id`, text, media, roles, families, trigger) and played by an accessible tour component: each step is a dialog announced to screen readers, focus moves to the dialog and back to the target, Escape exits, "Skip tour" and "Show me later" are always present, and no step depends on drag gestures (WCAG 2.5.7). Tours never block the user from working.
- **FR-P23-101** Role-based first-run tours: tenant admin (setup), CCO (dashboard and calendar), maker (task → evidence → submit), checker (review queue → approve/reject), department head, board member (board pack, read-only), auditor, CRO, CFO (ratios dashboard), HR admin, GRO. Each tour ≤ 7 steps.
- **FR-P23-102** Feature announcements: when a release adds or changes a feature for a role, a one-step "What's new" card appears once with a link to the release note and video; frequency capped at one per session (setting).

### 4J. Learning paths

- **FR-P23-105** Role-based learning paths combine help articles, tutorials and short knowledge checks (not graded for employment purposes) — "CCO in your first week", "Maker essentials", "Checker essentials", "Board member orientation", "CRO: running your first stress test", "CS: first board meeting on LDC", "HR admin: labour registers", "GRO: handling a complaint end to end". Progress is stored per user (tenant data) and visible to the tenant admin only in aggregate unless the tenant enables per-user reporting with notice to users (NN-25).
- **FR-P23-106** Certified courses (CPD, DSA/DMA, CISO, POSH IC training, etc.) live on **FinLegal Academy (trainings.lawdocs.in)**; LDC shows academy cards (P21 data) and deep links; completions can be imported back as training evidence for the relevant obligation (e.g., POSH awareness programme evidence; KYC/AML training evidence) through the P18 academy connector with user consent.

### 4K. Tutorial library: text, images, diagrams, screenshots, videos

- **FR-P23-110** Tutorial unit = one task for one role (e.g., "Maker: submit evidence for a quarterly obligation"). Each unit has: written steps (numbered, with expected result per step), annotated screenshots, one diagram where a flow is involved (e.g., the maker-checker cycle), a video (60–240 s), captions (WebVTT, English; Hindi second), a full transcript, alt text for every image, a downloadable one-page PDF quick card, applicable roles/families/plan tiers, product version, and links to the "i" terms and help articles it uses.
- **FR-P23-111** **Seeded demo tenant**: tutorials are produced only from `demo-ldc` tenants seeded with clearly fictional organisations ("Asha Finvest Private Limited — NBFC-ICC Base Layer", "Sahyog Urban Co-operative Credit Society", "Northstar Capital Markets Limited — listed") and synthetic people and data. No customer data ever appears in a tutorial, screenshot or video; the seed script is versioned in the repository and re-run on each release; a lint step blocks capture if the tenant id is not on the demo allow-list.
- **FR-P23-112** **Screenshot automation**: Playwright scripts (`tools/tutorials/*.spec.ts`) drive the demo tenant to each step and capture screenshots at 1440 × 900 (desktop) and 390 × 844 (mobile) in light and high-contrast themes; callouts and numbered markers are applied from a JSON overlay, not baked into images by hand, so screenshots can be regenerated each release.
- **FR-P23-113** **Diagrams** are authored as Mermaid or SVG source in the repository, rendered to accessible SVG (with `<title>` and `<desc>`) and PNG; each has a text equivalent ("This diagram shows …") beneath it.
- **FR-P23-114** **Video production pipeline**: (1) script drafted from the written steps (Vidhi may draft; a technical writer approves); (2) screen recording by Playwright with scripted cursor movement and deliberate pacing (≥ 1.5 s per step) at 1920 × 1080; (3) voice-over by a human narrator or a licensed text-to-speech voice (English and Hindi) through the P18 speech adapter, with the voice disclosed in credits if synthetic; (4) captions generated by speech recognition then corrected by a human to ≥ 99% accuracy, with speaker identification and non-speech cues; (5) audio description track or described-video version where on-screen action is not narrated (WCAG 1.2.5); (6) optional Indian Sign Language interpreter picture-in-picture for priority videos (the 12 "getting started" videos and all accessibility/grievance videos), produced with a qualified ISL interpreter [REC]; (7) review by product owner, accessibility specialist and a regulatory reviewer for any legal statement; (8) publish with chapters, transcript and download.
- **FR-P23-115** **Social cut-downs** for marketing (R-020): each long-form tutorial yields up to three derivative assets — 9:16 vertical (Instagram Reels, YouTube Shorts; ≤ 60 s, burned-in open captions sized for mobile, safe-area aware), 1:1 square (LinkedIn feed; ≤ 90 s), 16:9 (YouTube, website). Derivatives inherit the Claims Register checks of their source, carry the brand end-card and a link to the full tutorial, and are handed to the Hub's social calendar (Appendix X) as assets with metadata (title, description, hashtags, alt text, transcript). LDC never posts to social networks directly.
- **FR-P23-116** Hosting: public tutorial videos on a video platform with adaptive streaming and captions support (YouTube for reach plus a self-hosted or India-region streaming service for in-app playback without third-party tracking; adapter `VIDEO_PORT`) [REC]; the in-app player is accessible (keyboard controls, caption toggle, speed 0.5–2×, transcript panel synced to time, no autoplay with sound).
- **FR-P23-117** **Staleness detection**: on every release, the screenshot suite re-runs; a perceptual-diff above threshold (setting `hlp.tutorials.diff_threshold`, default 2%) on any step marks the tutorial `STALE`, notifies its owner and shows a "This tutorial shows an earlier version of the screen" notice until refreshed. Release notes list stale tutorials. Target: no tutorial stale for more than two releases.
- **FR-P23-118** Tutorial catalogue at launch: ≥ 40 videos (Appendix P §P.5) covering every role's first-week tasks; the catalogue grows by module as phases ship (each phase's §13 deliverables must include its tutorials).

### 4L. Accessibility programme (NN-21)

**4L.1 Standard and scope**
- **FR-P23-120** Conformance target: **WCAG 2.2 Level AA** for every LawDocsComply surface (public site, tenant app, console, delivery console, generated documents and reports, emails, PDFs, the health check and the help centre), which also satisfies **IS 17802 (Part 1): 2021** requirements for web content and software [VERIFY clause mapping] and the accessibility chapter of **GIGW 3.0** where customers in the public sector or regulators ask for it. The programme also tracks the **draft RPwD (Amendment) Rules 2026** (S.O. 3962(E), 16 July 2026): if notified, LDC must publish an Accessibility Conformance Report (human- and machine-readable), retest after major changes and review at least every two years, within 12–18 months of notification depending on turnover (flag the obligation in LDC's own `LDC_GROUP` compliance instance).
- **FR-P23-121** Customers' own obligations: because SEBI-regulated entities must make their digital platforms accessible (SEBI circular of 31 July 2025, revised 29 August 2025: annual audit by an IAAP-certified professional, accessible documents including ISL and captions, a nodal officer and an accessibility grievance mechanism) and RBI/IRDAI/IFSCA entities face similar expectations after *Pragya Prasun* (SC, 30 April 2025), LDC (a) supports customers' compliance by publishing its own ACR (customers will request it in vendor due diligence), (b) carries an "Accessibility compliance" instrument pack in the content library (P03/P15, Appendix G), and (c) lists IAAP-certified accessibility audits as a marketplace service category (P21, Appendix O).

**4L.2 Design tokens and components**
- **FR-P23-122** Correct the owner's palette where it fails contrast (computed 25 October 2026, Appendix R §R.11): Gold `#C9A961` on white is 2.25:1 — it may be used only for decorative fills or as an accent on navy; text in gold uses **Gold-700 `#8A6D2B`** (4.88:1); the **focus indicator is two-tone** — 2 px `#0A2540` navy outline plus 2 px `#C9A961` gold offset — giving ≥ 3:1 against both light and dark surfaces (WCAG 1.4.11; meets 2.4.13 Focus Appearance (AAA) as a stretch). Amber `#D97706` on white is 3.19:1 — status text and icons in amber use **Amber-700 `#B45309`** (5.02:1; 4.51:1 on Amber-Light `#FEF3C7`). Grey-400 `#94A3B8` (2.56:1) is reserved for disabled controls; placeholder text uses Grey-600 `#475569`. The token package exports a contrast test that runs in CI over every foreground/background token pair used by components.
- **FR-P23-123** Status is never conveyed by colour alone: every status chip has text and an icon shape (✓ Compliant, ◷ Due soon, ! Overdue, ✕ Rejected, ⓘ Info), and charts use patterns/markers in addition to colour (WCAG 1.4.1).
- **FR-P23-124** Component contract (enforced in `packages/ui` with Storybook a11y tests): semantic HTML first (buttons are `<button>`, links are `<a>`); ARIA only where native semantics are insufficient and following the ARIA Authoring Practices patterns (disclosure, menu button, combobox, listbox, tabs, dialog, grid, tree, tooltip); every interactive control has a visible label and an accessible name that contains the visible label (WCAG 2.5.3); targets ≥ 24 × 24 CSS px with spacing (2.5.8); focus never hidden behind sticky headers, footers or chat widgets (2.4.11 — components use `scroll-padding` and the sticky bars reserve space); no drag-only interactions — Kanban boards, risk heat-map placement, dashboard widget arrangement and file upload all offer button/keyboard alternatives (2.5.7); dialogs trap focus and restore it; toasts are announced via polite live regions and stay ≥ 10 s or until dismissed, with "View all notifications" history (2.2.1).
- **FR-P23-125** Data grids (obligation registers, risk registers, audit findings — the densest screens): implemented as ARIA grid or native table with sortable column headers announced (`aria-sort`), row headers, keyboard navigation (arrow keys, Home/End, Page Up/Down), a "Table settings" control for column visibility, density and frozen columns, a "Read row" summary for screen readers, and an alternative "List view" that reflows at 320 CSS px width without horizontal scrolling for two-dimensional content exceptions only (1.4.10 Reflow).
- **FR-P23-126** Forms: labels persistent (no placeholder-only labels), required fields marked in text, inline errors linked by `aria-describedby`, an error summary on submit with links to fields, input purpose (`autocomplete`) attributes for personal data fields (1.3.5), no re-entry of information already provided in the same process (3.3.7), confirmation step for legally significant actions (submitting a return package for filing evidence, approving a policy, signing) with review and the ability to correct (3.3.4).
- **FR-P23-127** Authentication accessibility (WCAG 3.3.8): no cognitive function tests — no puzzles, no transcription of distorted characters; password managers and paste allowed in every credential and OTP field; passkeys (WebAuthn) and magic links offered; OTP inputs accept paste of the whole code; session-timeout warning at least 2 minutes before expiry with "Extend" (2.2.1), and unsaved work preserved on re-authentication (2.2.5 as a stretch).
- **FR-P23-128** Time-bound tasks: regulatory deadlines are content, not interaction time limits; no LDC interaction expires while a user is typing; the health check has no timer.

**4L.3 User accessibility preferences (per user, synced across devices)**
- **FR-P23-129** "Accessibility and display" settings page (also reachable from the public site's footer via a non-overlay preferences panel stored in a first-party cookie): text size (100–200%, layout reflows), line and paragraph spacing presets (meets 1.4.12), dyslexia-friendly font option (e.g., OpenDyslexic or Atkinson Hyperlegible [REC]), high-contrast theme and dark theme (both passing 4.5:1), Windows forced-colours support, reduced motion (also honours `prefers-reduced-motion`; disables parallax, auto-animations and animated charts), captions on by default for all videos, transcript panel open by default, audio descriptions on, simplified layout (hides secondary widgets and shows one primary action per screen), keyboard shortcut list and customisation (single-character shortcuts can be turned off or remapped — 2.1.4), "Show term explanations inline" (FR-P23-93), screen-reader optimised tables (adds row summaries), and read-aloud (text-to-speech of the current article or document through the browser's Speech Synthesis API or the P18 speech adapter, with highlighting). Preferences are user settings in the P02 registry (tier T) and are honoured in generated emails where possible (e.g., plain-text alternative). **No third-party accessibility overlay widget** is used; accessibility is built into the code.
- **FR-P23-130** Voice input: all text fields work with operating-system dictation; Vidhi chat offers a microphone button (speech-to-text through the P18 speech adapter with on-device fallback) and read-aloud of answers; speech in Hindi and English at launch.

**4L.4 Documents, charts, email and media**
- **FR-P23-131** Generated PDFs (reports, board packs, health-check reports, invoices, exports) are tagged (PDF/UA-1 target): logical reading order, real headings, table headers, alternative text for charts with the underlying data table appended, document language set, bookmarks for documents over 9 pages. Generated DOCX uses Word heading styles, table header rows, alt text on images and no text in images. A post-generation check (veraPDF for PDF/UA) runs on every template in CI.
- **FR-P23-132** Charts (dashboards, health check, risk heat maps, ratio trends): each chart has a text summary ("CRAR fell from 22.4% to 19.8% between Q1 and Q2, still above the 15% minimum"), a toggle to show the data table, keyboard-reachable data points with tooltips that meet 1.4.13, and patterns/markers. The summary sentence is generated deterministically from the data.
- **FR-P23-133** Emails: semantic HTML, `lang` attribute, logical heading, descriptive link text, alt text, minimum 14 px body, dark-mode safe colours, plain-text alternative part.
- **FR-P23-134** Uploaded customer documents are the customer's responsibility, but DMS (P07) offers OCR text layers and "Check accessibility" on PDF uploads, and tells the uploader when a board pack PDF has no text layer so a screen-reader user on the board can still read it.

**4L.5 Testing, conformance and grievance**
- **FR-P23-135** Automated: axe-core (via Playwright) on every route and component story in CI — zero "serious" or "critical" violations is a merge gate; Pa11y CI nightly on the public sitemap; Lighthouse accessibility ≥ 95; colour-contrast token test; ESLint `jsx-a11y`; heading-order and landmark checks; PDF/UA check.
- **FR-P23-136** Manual: before each release that changes UI, an accessibility specialist runs the scripted assistive-technology test matrix — NVDA + Firefox and JAWS + Chrome on Windows, VoiceOver + Safari on macOS and iOS, TalkBack + Chrome on Android, keyboard-only, Windows high-contrast/forced colours, 200% and 400% zoom (reflow at 320 CSS px), Dragon NaturallySpeaking or Voice Access voice control, and a cognitive walkthrough of the top ten tasks — and records results against WCAG 2.2 success criteria in the conformance register (`hlp.a11y_conformance`).
- **FR-P23-137** User testing: at least two sessions per year with users with disabilities (including a blind screen-reader user and a deaf ISL user), recruited and paid fairly, consent recorded.
- **FR-P23-138** Independent audit: annual audit by an IAAP-certified (CPACC/WAS/CPWA) auditor before the ACR is renewed; findings tracked as defects with severity and target dates (critical ≤ 14 days, serious ≤ 30, moderate ≤ 90).
- **FR-P23-139** Accessibility Conformance Report: VPAT 2.5 INT format (covering WCAG 2.2, EN 301 549 and Section 508 tables) plus an IS 17802 mapping table; published at `/accessibility/acr` as HTML (human-readable) and JSON/XML (machine-readable), versioned per product release, with known exceptions and remediation dates. The Accessibility Statement (`/accessibility`) states the target, the status, the date of last audit, the feedback channel, the response time and the escalation route (Appendix P §P.2.8).
- **FR-P23-140** Accessibility grievance channel: a form (accessible itself; also email and phone; also a voice/video option for ISL users through a scheduled call) for any user or visitor; tickets go to the LDC support desk with category "Accessibility" and to the designated accessibility nodal officer; acknowledgement within 1 working day, resolution or workaround within 15 working days (settings), escalation to the CTO; tracked in the accessibility issue register; trend reported quarterly.
- **FR-P23-141** Release gate (NN-21): a release cannot be promoted to production if (a) any serious/critical automated violation exists on changed routes, (b) the manual matrix for changed flows is not signed off, or (c) the conformance register shows an open critical defect past its target date without an approved exception (dual approval, recorded, visible in the ACR).

### 4M. SEO, GEO and AI-search technical specification

- **FR-P23-150** **Rendering for retrieval**: full content in server HTML (FR-P23-02/03); semantic landmarks; one `<h1>`; descriptive headings that match buyer questions ("Which RBI returns does a Middle Layer NBFC file?"); answer-first paragraphs (the first 40–60 words of each section answer the heading's question); short sections that make sense when extracted alone; tables for comparisons; dates of last review visible on every regulatory page.
- **FR-P23-151** **URLs**: lowercase natural-language slugs (`/solutions/nbfc-compliance-software`, `/glossary/capital-adequacy-ratio-crar`, `/regulatory-updates/rbi/2026/…`), no query-string content, trailing-slash policy consistent, canonical tags on every page, pagination with self-canonical pages.
- **FR-P23-152** **Metadata**: unique title (≤ 60 characters, primary phrase first, brand last), meta description (≤ 160), Open Graph and Twitter/X cards with 1200 × 630 images carrying text alternatives, `article:modified_time` on articles.
- **FR-P23-153** **Structured data** (JSON-LD, validated in CI against schema.org and Google's documented features): `Organization` (with legal name, logo, `sameAs` to LinkedIn, YouTube, X, Crunchbase, Wikidata when created; contact points), `WebSite` with `SearchAction`, `SoftwareApplication` on the home and module pages (`applicationCategory` "BusinessApplication", `operatingSystem` "Web", `offers` only when a public price exists), `Product`/`Offer` (or `OfferCatalog`) on the pricing page with INR prices and `priceValidUntil` derived from the catalogue, `Service` and `OfferCatalog` for marketplace services, `Course` for academy cards, `Article`/`NewsArticle` for insights and regulatory updates (with `author`, `reviewedBy`, `dateModified`), `Legislation` (schema.org type for laws and regulations) referenced from regulatory-update pages via `about`/`mentions` with `legislationIdentifier`, `legislationDate` and `legislationPassedBy`, `DefinedTerm`/`DefinedTermSet` for the glossary, `BreadcrumbList` everywhere, `Event` for webinars, `VideoObject` with `transcript` and `hasPart` clips for tutorials, `HowTo` markup kept in source for tutorial pages even though Google no longer shows HowTo rich results on mobile (harmless, useful to other consumers), `FAQPage` only where a page genuinely has Q&A — Google stopped showing FAQ rich results on 7 May 2026, so FAQ markup is not relied on for search appearance. No `Review`/`AggregateRating` markup for LDC's own product (self-serving reviews are not eligible and risk misleading).
- **FR-P23-154** **Sitemaps**: `sitemap-index.xml` with per-type sitemaps (pages, solutions, glossary, regulatory updates, blog, tutorials/video sitemap, locales), `lastmod` from the page version, regenerated on publish; IndexNow submission (Bing, Yandex, Seznam, Naver) and Search Console sitemap ping.
- **FR-P23-155** **robots.txt and AI-crawler policy** (Governed settings, one line per agent): allow `Googlebot`, `Bingbot`, `OAI-SearchBot` (ChatGPT search), `PerplexityBot`, `Claude-SearchBot`/`ClaudeBot` [VERIFY current agent names], `Applebot`; a separate, owner-decided policy for training crawlers (`GPTBot`, `Google-Extended`, `CCBot`, `Applebot-Extended`) — default **allow on public marketing and glossary pages, disallow on `/hc/`, `/preview/`, `/api/`, `/account/` and share links** [REC; owner decision recorded in 02]. Note that blocking `Google-Extended` does not remove pages from Google's AI Overviews. Authenticated apps (`app.`, `console.`, `delivery.`) are `noindex` and disallowed.
- **FR-P23-156** **`/llms.txt`** (served as `text/plain; charset=utf-8`, with `/llms-full.txt`): H1 product name; one-paragraph definition ("LawDocsComply is an India-first governance, risk and compliance (GRC) SaaS for RBI-, SEBI-, IFSCA- and IRDAI-regulated entities, co-operative societies, companies and LLPs …"); entity facts (legal operator, group, website, launch year — from the Claims Register); module list with one URL each; entity families with one URL each; pricing page; marketplace; academy; trust centre; key glossary hubs; disambiguation (LawDocsComply vs LawDocs vs Finbyx vs Udofin vs Equator); a citation sentence; last-updated date. Generated from the CMS and registries at build time, never hand-edited, reviewed by the checker like any page. (Treat as low-cost hygiene: most requests to llms.txt files are rare; its value is mainly for documentation and developer content.)
- **FR-P23-157** **Developer documentation** (P18 developer portal) is public, static and crawlable, with OpenAPI specs downloadable — the main audience for which `llms.txt` is genuinely used.
- **FR-P23-158** **Entity consistency**: one canonical description of LawDocsComply and of each group product used across the site, `llms.txt`, Organization schema, LinkedIn, YouTube, Crunchbase, partner and marketplace listings; a quarterly check that third-party profiles match (AI engines rely heavily on third-party mentions).
- **FR-P23-159** **Programmatic pages with quality gates**: regulatory-update pages, glossary terms and instrument summary pages may be generated at scale only when each has human-written summary text (≥ 120 words), a primary-source link, a reviewer and a review date; pages without these are `noindex` until completed. No auto-spun content.
- **FR-P23-160** **Internal linking**: every regulatory update links the affected entity families, glossary terms and the solution page; every glossary term links its instrument and module; hub pages per regulator; breadcrumbs.
- **FR-P23-161** **Freshness**: solution and pillar pages carry "Last reviewed" dates and are reviewed at least every 6 months or when a mapped instrument changes (P05 change-impact event `InstrumentVersionPublished` creates a review task for every page that references it).
- **FR-P23-162** **Measurement** (monthly, exported to the Hub): Search Console and Bing Webmaster data; Core Web Vitals RUM; an **AI answer panel** of 30 fixed buyer prompts in the buyers' words (e.g., "best compliance software for NBFC in India", "how to file RBI CIMS returns for NBFC", "SEBI LODR compliance calendar software", "credit cooperative society compliance software", "DPDP compliance tool India") run across Google AI Overviews/AI Mode, ChatGPT search, Perplexity, Copilot and Gemini, recording separately whether LDC is **named** and whether an LDC page is **cited**, and which sources were cited instead; results trended for 90 days before content decisions.

### 4N. Public Regulatory Updates hub

- **FR-P23-165** A public index of regulatory developments for the families LDC serves, fed from P05: only items that a platform content reviewer has published as an Update, with a human-written plain-language summary ("What changed / who it applies to / what to do / effective date / source link"), the authority, instrument and date. Never the full tenant-specific impact analysis.
- **FR-P23-166** Filters: regulator, entity family, type (new instrument, amendment, FAQ, consultation, enforcement), date; RSS/Atom feeds per regulator and per family; an email digest subscription (consented, Hub-sent).
- **FR-P23-167** Each update page ends with: "Track this in LawDocsComply" (trial CTA), "Applies to you? Run the free health check" (family preset), and related academy course or marketplace service. Pages show `NewsArticle` + `Legislation` structured data (FR-P23-153).
- **FR-P23-168** Disclaimer on every update: "Summary for information. Read the source instrument; LawDocsComply does not provide legal advice." The summary never paraphrases a legal obligation more strongly or weakly than the source; a reviewer checks against the source.

### 4O. Analytics, cookies and consent

- **FR-P23-170** Cookie/consent management: first-party consent banner and preferences centre (accessible, no pre-ticked boxes, "Reject all" as prominent as "Accept all"), categories Strictly necessary / Preferences / Analytics / Marketing; consent stored with version and timestamp and mirrored to the P01 consent ledger for identified leads; Global Privacy Control honoured for California visitors [VERIFY CCPA applicability].
- **FR-P23-171** Analytics: first-party, privacy-preserving analytics hosted in India (self-hosted Matomo or Plausible-compatible [REC]) for page views and funnel steps without consent where the configuration is cookieless and aggregated [VERIFY under DPDP — default requires consent for any identifier]; event-level product analytics only after consent. Tag management server-side; no third-party script without an entry in the sub-processor list and the allow-list.
- **FR-P23-172** Attribution: UTM parameters and referrer are captured into the lead record (first-touch and last-touch), and conversion events (health check completed, trial started, plan purchased, marketplace order) are sent to the Hub.

### 4P. Trust Centre

- **FR-P23-175** `/trust` presents: security overview (encryption, tenant isolation, India data residency, backups, access control, vulnerability management, incident response, AI data use — no training on tenant data, NN-15), data-protection overview (DPDP role of LDC as data processor for tenant data and data fiduciary for account and lead data; DPA download), sub-processor list (name, purpose, location, data categories) with change-notification subscription, certification and attestation status **only as recorded in the Claims Register** (e.g., "SOC 2 Type 1 readiness assessment in progress" is allowed if true; "SOC 2 certified" is not), policies available on request under NDA, penetration-test summary letters when available, uptime history from the status page, accessibility statement and ACR, responsible disclosure policy and `/.well-known/security.txt` (RFC 9116) with contact, expiry and policy URLs.
- **FR-P23-176** Gated documents (SOC reports, VAPT summaries) are requested through a form; access is granted after NDA eSign (P07) by `plt_security_officer`, watermarked per recipient and logged.

### 4Q. Global website, locales and country pages *(v1.1; Appendix Y §Y.9.3, §Y.12)*

**FR-P23-177 — Locales.** `en-IN` default; `hi-IN` for health check, glossary, solution pages and help (D-30); `en-GB` and `en-US` copy variants for market pages (spelling, date and currency formats); `ar-AE` with RTL layout only when the GCC cell and a reviewed Arabic copy deck exist (flag `web.locale.ar.enabled` = OFF). Translations of marketing copy are professional with glossary; machine pre-translation allowed with human review; regulatory text is never machine-translated on the public site (NN-54).

**FR-P23-178 — Market subfolders.** `/ae/`, `/sg/`, `/uk/`, `/eu/`, `/us/` subfolders (not separate domains) with `hreflang` alternates and `x-default` to the India site; market pages show the market's price book (P20 FR-P20-70), seller entity, data-residency options and published packs.

**FR-P23-179 — Country solution pages.** `/<market>/solutions/<country>-compliance` pages are generated from the jurisdiction-pack registry (P25): coverage statement (authorities, instruments, last update, reviewer of record firm), sample checkpoints, filing calendar highlights, delivery partners available, price; pages for countries without a PUBLISHED pack are not generated; PILOT packs show "Pilot — coverage being completed" (NN-53, NN-19).

**FR-P23-180 — Group and MNC pages.** "For Indian groups with overseas subsidiaries" and "For multinational subsidiaries in India" pages explain group views, home-region residency (Indian entities stay in India), partner network and pricing per jurisdiction.

**FR-P23-181 — RTL readiness.** Logical CSS properties, `dir` attribute, mirrored icons where directional, bidirectional isolation; tested with Arabic screen readers before `ar-AE` is enabled (NN-21).

**FR-P23-182 — Trust Centre per cell.** The Trust Centre lists live cells, sub-processors per cell, transfer mechanisms and AI routes per cell (P18 FR-P18-81).

**FR-P23-183 — SSR for all locales.** Every locale and market page returns its primary content in server-rendered HTML (NN-44); sitemaps per locale.

### 4R. Global health-check variant *(v1.1)*

**FR-P23-184 — Entry.** "Check a foreign subsidiary" or "Check my group" options on the health-check start page; the visitor chooses country, entity form and size band; licensed company-registry look-ups only where the provider's terms allow anonymous, rate-limited lead-flow use (P18 FR-P18-90) — otherwise manual entry; never credit-bureau data (X-07).

**FR-P23-185 — Question bank.** *(v1.2: seeded as set `HC-SET-0002`, bindings in Appendix P §P.11.3.)* 20 questions (Appendix P §P.8) covering annual returns, registered office/agent, beneficial ownership, economic substance, audit, tax and VAT filings, payroll and social security, licences, local data protection, records, board meetings, AML registration where applicable, transfer pricing, and India-side FEMA reporting by the Indian parent.

**FR-P23-186 — Scoring and caveats.** Scores per segment; jurisdiction-specific explanations shown only from PUBLISHED packs; for other countries the report is labelled "generic group check — local rules not yet reviewed" (NN-19, NN-53).

**FR-P23-187 — Output.** Report with charts, prioritised actions, the matching Global Pack and partner services, and an India-parent FEMA/ODI section where relevant; share link and PDF as for the domestic check.

**FR-P23-188 — Lead routing.** Lead carries `jurisdiction`, `entity_form`, `group_size` to the OH CRM corridor queue (Appendix X §X.15.2) with consent.

### 4S. Pages and tutorials for the v1.1 modules and agents *(v1.1)*

**FR-P23-189 — Module pages.** `/legal-matters-and-contracts`, `/esg-brsr`, `/ai-governance`, `/global-entity-management`, `/reports-and-board-packs`, `/vidhi-ai-agents`, `/connect-your-ai-assistant` (MCP) — copy in Appendix P §P.7, every claim claims-registered.

**FR-P23-190 — Agent transparency page.** A public page explains what Vidhi agents do and do not do (drafts and proposals; humans approve; autonomy levels; kill switches; India routing; no training on client data) with links to the AI policy and LDC's own AI assurance pack (D-38).

**FR-P23-191 — Tutorials.** Tutorials T-45–T-62 (Appendix P §P.9) with captions, transcripts and ISL priority flags; screenshots generated from the seeded demo tenant (no real data).

**FR-P23-192 — Interactive demos.** Click-through demos (no sign-up) for the agent workforce, MCP connection and global group view, built on the demo tenant.

**FR-P23-193A — Public RBI Directions Tracker (lead magnet; G4 AB.9).** A public page `/rbi-directions-tracker` lists the RBI consolidated Directions of 28 Nov 2025, later amendments and the DoS directions of 31 Jul 2026 from the pre-seeded catalogue (D-39; `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`) by RE category, with title, reference, date, amendments and a "question sheet available in LawDocsComply" badge; no paid content is exposed; rows still marked [VERIFY] show "reference being verified"; a CTA offers the health check and trial. SSR (NN-44); claims-gated (NN-19).

**FR-P23-193 — Glossary additions.** "i" terms for the new modules and global terms (e.g., BRSR Core, limitation period, economic substance, registrable controller, autonomy level, MCP, agent sponsor), scoped by jurisdiction where needed.

### 4T. Help improvements from client feedback *(v1.1; Appendix Z §Z.9.10)*

**FR-P23-194 — Hindi for daily work (IMP-097).** Hindi UI strings for the top 20 maker and checker screens (Work Inbox, instance drawer, submit, review, evidence upload, calendar, notifications, profile) and their help articles; regional languages for co-operative member screens by demand (D-30).

**FR-P23-195 — Contextual video and tours (IMP-098).** Every primary screen has a 60-second contextual video and a first-visit tour (skippable, replayable from the help menu); tours respect reduced motion and are keyboard-operable.

**FR-P23-196 — Inline regulatory help (IMP-099).** The "i" panel on a checkpoint shows the clause snippet (official text), the plain-language explainer (Column `explanation` (v1.0: L)) and the evidence expectation side by side without leaving the screen.

**FR-P23-197 — Help-key coverage gate.** CI fails if a primary screen lacks a help key, tour or video reference (link with P24 click-budget gate, IMP-101).


### 4U. Health Check Studio *(v1.2; D-55)*

The Studio lets the super admin decide **which sections, how many questions and which questions** each health check shows, chosen from the compliance library by CompID, and govern every change like regulated content. Roles: maker = `plt_super_admin` or a `plt_content_maker` holding the `web.hc_studio` permission; checker = `plt_content_checker` or a second super admin (maker ≠ checker, NN-05); publisher = `plt_content_publisher` (or `plt_web_publisher` once split).

**FR-P23-198 — Sets and versions.** A health-check **set** has a business ID `HC-SET-<NNNN>` issued by the P03 `IdService` (immutable, never reused, NN-56) and immutable versions `HC-SET-<NNNN>/v<n>`. Attributes: name, health-check family (Appendix P §P.3.1) and the template families it draws from, entity types/layers, channel (PUBLIC, IN_APP pulse check, PARTNER), locale(s), scoring model, status `DRAFT → IN_REVIEW → APPROVED → PUBLISHED → RETIRED`. At most one PUBLISHED version per (family, channel, locale) outside an experiment. Question codes keep the bank form `HC-<SEG>-<NN>`; `SET` is reserved and never used as a segment code, so set IDs and question codes cannot be confused.

**FR-P23-199 — Select by CompID.** The library picker searches the published library by CompID (or alias), question text, instrument and clause, with filters on family, authority, instrument, instrument section/chapter, department, function and sub-function, compliance type, risk level and risk type, frequency, Change Status and coverage state, and shows each candidate's list-view fields, applicability and current question version. Only ASSIGNED CompIDs, library placeholder IDs (FR-P23-206) and existing bank questions can be selected (LDC-WEB-040 for RESERVED, VOID or RETIRED CompIDs). One health-check item may bind **several CompIDs** (a plain-language question that rolls up, for example, the four CCO-appointment rows of the Compliance Function Directions) with one marked primary; the item's citation is built from the bound CompIDs.

**FR-P23-200 — Sections, counts, weights and order.** Sections default to the ten segments of Appendix P §P.3.2 and can be added, renamed, merged or reordered. Per section the maker sets: questions shown (fixed list, or *n* drawn from a pool by priority rule — risk level, then weight — never at random for the public check, so two visitors with the same profile see the same set), section weight (Σ = 100, LDC-WEB-041), item weights 1–3, order (fixed or "critical first"), and per set a total cap (default 50, bounds `web.hc.studio.max_questions`) with an estimated completion time at 20 seconds per question (warning above 12 minutes, LDC-WEB-042).

**FR-P23-201 — Plain-language wording.** Each item has a visitor wording (≤ 35 words, reading-ease lint, banned-jargon list, defined terms linked to the glossary) shown beside the library question of the primary CompID; Vidhi may propose a rewording at L1 (NN-04, NN-50) which the maker accepts or edits; Hindi and other locale wordings need a reviewed translation (NN-54); the citation and "why it matters" text are derived from the bound CompIDs and never typed free-hand.

**FR-P23-202 — Answer options and scoring.** Default options Yes / Partly / No / Not sure / Not applicable with scores 1 / 0.5 / 0 / 0 / excluded (FR-P23-50). Per item the maker may choose Yes/No, a numeric answer with scoring bands (e.g. "How many board meetings last year?" → ≥ 4 = 1, 3 = 0.5, ≤ 2 = 0), or a multi-select with partial credit; N/A can be disabled or limited to a reason list; the critical flag drives the critical-gap override (FR-P23-52). Scoring stays deterministic (NN-22); the scoring model version is pinned to the set version (FR-P23-55).

**FR-P23-203 — Branching.** Display rules in JSONLogic on profile refiners and earlier answers (e.g. hide deposit questions when "deposit-taking = No"; PPL-01 becomes N/A below 10 employees; ask the three CCO follow-ups only when the entity is Middle Layer or above). The editor checks for cycles, unreachable items and contradictory rules (LDC-WEB-043) and shows, per sample entity, which items apply.

**FR-P23-204 — Preview as a sample entity.** Saved sample entities (e.g. "NBFC Middle Layer, ₹2,000 crore, digital lending, 180 staff"; "UCB Tier 2, Maharashtra") render the set exactly as the public or in-app page would, with applicable count, estimated time, and a scoring test harness (all-Yes = 100, all-No = 0, each critical rule triggers, bands and confidence computed) that must pass before submission (LDC-WEB-044).

**FR-P23-205 — Maker-checker publish and versioning.** Submission locks the version; the checker sees a diff to the previous published version by item and by CompID (added, removed, re-worded, re-weighted, re-scored, branching changed) and the test-harness results; approval and publication are separate actions; publication can be scheduled; sessions pin the set version and experiment arm at PROFILED (§5.1), so old reports re-render identically. Copy with numbers or claims passes the Claims Register lint (NN-19).

**FR-P23-206 — Bindings, placeholders and lineage.** Where a question sheet does not yet exist, an item binds to a **library placeholder ID** `LPH-<AUTH>-<FAM>-<INST>-<NNNN>` (issued by `IdService`; five segments, so it can never be mistaken for a CompID) that names the expected instrument scope. When P03 publishes the sheet, the content maker links the placeholder to the CompIDs that cover it; the placeholder becomes a P03 alias (type `HC_PLACEHOLDER`) of the primary CompID and draft sets update automatically, published sets at their next version. `CompIdRetired` / `CompIdLineageRecorded` on a bound CompID flags the set "needs review" (LDC-WEB-045) and the successor is shown in the citation until a new version is published; a set cannot be published with an unresolved retired binding (LDC-WEB-046).

**FR-P23-207 — Baseline pre-fill on conversion.** When a visitor converts to a trial or a tenant runs an in-app check, the answers are sent to P01/P04 as a `hc_baseline` payload keyed by CompID: for every bound CompID that is applicable to and adopted by the new tenant — Yes → "Self-declared in place (unverified)", Partly → "Self-declared partial", No → "Self-declared gap" with a suggested task to the mapped department, Not sure → "To verify", N/A → an applicability-challenge suggestion with the reason (applicability is never changed automatically). The baseline never sets a compliance instance to Compliant, never fills Date of Compliance, never creates evidence, and is labelled "from Health Check on <date>" in the CompID History (NN-57). Placeholder bindings are held as instrument-level baseline notes and attach to CompIDs when the sheet publishes. P04 owns how the baseline is displayed and used.

**FR-P23-208 — A/B comparison.** Two published versions (or a version and a variant) can run as an experiment through `web.experiments` with allocation by session, guard metrics (completion rate, drop-off by question, median time, "Not sure" rate, conversion to trial, score distribution), minimum 300 completed sessions per arm before a result is shown (setting), and stop rules. Scores from different arms are never presented as comparable to the visitor; each report states its set version. The winner is promoted through FR-P23-205.

**FR-P23-209 — Drop-off analytics.** Per set version and arm: funnel started → profiled → each section → completed → report shared → trial; abandonment and median time per question; "Not sure", N/A and back-navigation rates per item; items breaching `web.hc.studio.dropoff_alert_pct` or a "Not sure" rate above 30 % are flagged for rewording. Analytics are aggregate, use only consented analytics (§4O) and are shown only for cohorts of ≥ 30 sessions.

**FR-P23-210 — Naming and seeding.** The output is always called **Health Check Score** (X-46) in the Studio, previews, experiments, analytics and exports; "Compliance Score" stays reserved for P04. At go-live the Studio holds `HC-SET-0001` (Core v1.0 — the 50 questions and 10 reserve questions of Appendix P §P.3.2 with family variants and the §P.3.3 weights) and `HC-SET-0002` (Global v1.0 — Appendix P §P.8), with the CompID and placeholder bindings of Appendix P §P.11.

### 4V. Public Brand Studio, standard pages and the binding footer *(v1.3; IPB-04 §04.3.2, §04.3.7, §04.3.8; D-66, D-72; owner decision #29)*

The public site, the tenant app and the console read **one `brand_pack`** (shared object, IPB-D-10, D-68). The platform layer is edited by the super admin in `apps/console › Studio › Brand`; the tenant layer is P02 §4M (FR-P02-62) and may only override within the contrast guard-rails; a white-label add-on (Appendix N) gets its own `brand_pack` with a host map. Nothing in this section creates a second theme editor.

- **FR-P23-211 — `brand_pack` for the public site.** Fields: `app_name` (application display name shown in the title bar, emails, PDFs and the "About" node — default "LawDocsComply"), `legal_entity_ref`, `tokens` (light, dark, high-contrast light and dark; semantic token set of IPB-07 §07.4.1 with LDC defaults `--color-primary #0F4C3A`, `--color-accent #C9A227`, fonts IBM Plex Sans / IBM Plex Mono, self-hosted), `logo` (SVG + PNG renditions, light and dark variants), `favicon` set, `og_image`, `email_identity` (from name, from address, reply-to; SPF/DKIM/DMARC verified before activation), `hosts[]` (primary and aliases; verification token; certificate status), `social{}` (platform → URL), `terminology{}` (incl. `vidhi` display-name override, white-label plans only — IPB-D-03), `footer_regions` overrides, `status_page_url`, `docs_url`. Every colour pair is contrast-checked at save (text ≥ 4.5:1, UI ≥ 3:1, focus ≥ 3:1); a failing pair blocks publish with `LDC-WEB-053` and the nearest passing shade is suggested. Versions are immutable; publish needs a second `plt_super_admin` or `plt_release_manager` as checker; rollback is one click to any prior version and is itself a version.
- **FR-P23-212 — Host map and host-header safety.** Requests are served only for hosts present in a published `brand_pack.hosts[]`; an unknown `Host` header receives a static 421 page and is logged (`LDC-WEB-054`); redirects, canonical URLs, OIDC redirect URIs and cookie domains are derived from the matched host, never from the request. Certificates are issued through `DNS_CDN_PORT` after a DNS TXT or CNAME verification; a host that fails verification cannot publish. White-label hosts get their own CMP consent scope and sitemap.
- **FR-P23-213 — Standard pages shipped from day one.** Every page in IPB-04 §04.3.7 exists in the CMS with its template and required block slots; toggled pages (Investors, blog, vlog, compare) are hidden by setting, never absent (`IPB-04-65`). LDC-specific pages (Solutions by family, Modules, Regulatory Updates hub, Health Check, Marketplace and Academy entries, Country pages) keep FR-P23-13. Each standard page carries `BreadcrumbList` JSON-LD, a visible "last reviewed" date and the site-level `Organization` JSON-LD with legal name, logo, `sameAs` (from `brand_pack.social`) and `contactPoint` (support, grievance).
- **FR-P23-214 — About.** Required blocks: story as dated milestones (`timeline`), mission, **what we do not do** (the boundary statement of FR-P23-12 item 9), group context ("Part of the Infrabyx Group"), leadership teaser, contact. Every date and number is a Claims Register entry (§4D) at evidence class E2 or better.
- **FR-P23-215 — Team and Leadership.** `team_member` items (`group` = team | leadership | advisory | board; name, role, bio, photo, LinkedIn, DIN optional for board, `photo_consent` flag with date and source). A photo without consent recorded cannot publish (`LDC-WEB-055`). Names and roles are text, never only in images. An empty advisory or board group renders nothing — no placeholder "advisory board" block. Placeholder entries in the content deck are replaced from Studio before go-live; the publish queue lists remaining placeholders.
- **FR-P23-216 — Investors (toggle; default OFF).** `web.investors.enabled` (L tier until owner decision #29; then G). When ON: sections vision, market (E2-sourced), products, governance, leadership, milestones, documents (gated `login` or `email_gate` with NDA flag, served from the Vendor Assurance Room `financial_statements` and `incorporation_docs` types through `TRUST_PORT`, never uploaded to the CMS), IR contact (named person, direct email), and the **locked disclaimer block** (copy from Appendix AD §AD.19, not editable in Studio) stating that the page is information only and is not an offer or invitation to subscribe to securities (Companies Act 2013 s.42 private-placement regime, s.23 and s.26 public-offer rules [LAW]; SEBI (ICDR) Regulations 2018 where applicable [LAW]) **[COUNSEL]**. Every publish requires `plt_legal_reviewer` approval; numeric claims need E2+; the words "guarantee", "assured return", "will achieve", "projected", "returns" fail the claims lint (`LDC-WEB-056`). No forward-looking statements.
- **FR-P23-217 — Careers, Press, Partners.** Careers: culture block, open roles (`job` items with department, location — Delhi, Noida, Jaipur, remote — type, `validThrough`), benefits as facts, equal-opportunity statement, application form posting server-side to Operations Hub HR through `HR_PORT.createApplication` with the consent text `consent.careers` and ledger receipt; closed roles return 410 with a link to open roles; `JobPosting` JSON-LD. Press: dated releases, coverage items each with date and article URL (no outlet-homepage links, no undated "coverage walls"), media kit (SVG/PNG logos from the brand pack, boilerplate, leadership photos with consent, product screenshots), named spokesperson. Partners: partner types (content partners and reviewers of record per Appendix Y, implementation partners, auditors and practitioners of Appendix O, technology partners), logo wall where each logo has a `claims_ref` permission record, "become a partner" form → `CRM_PORT`; no implied endorsement by any regulator or court.
- **FR-P23-218 — Contact, Documentation, Changelog.** Contact: form (name, work email, phone optional, entity type, message, `consent.contact_form` notice; optional unticked `consent.marketing.email`) → `CRM_PORT` with the consent version and receipt id; CMS stores submission id and status only (`IPB-04-67`); offices block from CMS-managed addresses (Delhi, Noida, Jaipur, plus brand-pack additions) with a static click-to-load map image (no map-provider request before consent); WhatsApp CTA opens `wa.me` only after an explicit click on a labelled button and shows the `consent.marketing.whatsapp` notice; support hours; Grievance Officer and DPO with emails on the page as well as the footer. Documentation: link-out to the developer portal (P18 §4M, shares the brand pack and CMP), help centre, API status, changelog. Changelog: `changelog_entry` list filtered by product area with RSS; public audience only — tenant-only entries render inside `apps/web` What's new (§4W).
- **FR-P23-219 — Pricing and Compare.** Pricing page copy, comparison table, FAQ references, banners and thresholds are edited in `Studio › Pricing` per brand pack; prices, GST treatment and plan limits are read from the OH8 catalogue through `BILLING_PORT` (X-02) and never typed; the Payment & Subscription Terms and Refund Policy links sit above the CTA (IPB-05-02); Compare pages name a competitor only after `plt_legal_reviewer` sign-off with dated, sourced rows (Appendix R).

### 4W. Blog, Vlog, Resources, policy pages, feedback, marketing tooling and tutorial captions *(v1.3; IPB-04 §04.3.4–§04.3.6, §04.3.10–§04.3.11; IPB-05; IPB-06; D-71, D-73, D-74; NN-62–NN-64; owner decision #30)*

- **FR-P23-220 — Blog toggle.** `web.blog.enabled` (G; default ON). OFF hides the blog from navigation, footer, sitemap and feeds and serves 410 for post URLs with a link to Resources; nothing is deleted; turning ON restores every published post with its original URL and dates. Categories, tags, authors (`team_member` or `user`), reading time, `Article` JSON-LD with `author`, `datePublished`, `dateModified`, canonical, RSS/Atom and `llms.txt` are unchanged from §4C.
- **FR-P23-221 — Bulk Word import (LawDocs `DocxImportWorkflow` pattern).** `Studio › Blog › Bulk import` accepts a zip of `.docx` files (≤ 200 files, ≤ 25 MB each; type-sniffed, AV-scanned, macros stripped, embedded objects dropped, images re-encoded and alt text queued); a Temporal workflow converts each file to the block schema (headings, lists, tables, images, footnotes → citations), proposes slug, excerpt, category and tags, flags every number and badge for Claims Register references (`IPB-04-102`), and produces a **preview and diff** against any existing post with the same slug. The editor accepts, edits or rejects per item; accepted items enter the normal DRAFT → REVIEW → PUBLISH pipeline (never auto-publish). The whole job is one change set with a 24-hour undo (NN-49). Import logs are kept 90 days.
- **FR-P23-222 — User posts (D-73; NN-64).** `web.blog.user_posts.enabled` (G; default OFF; owner decision #30). Eligible authors (tenant users with `author` permission, verified practitioners from Appendix O, invited guests) write in a restricted editor (no raw HTML, no scripts, no iframes; images through the media pipeline; links `rel="ugc nofollow"`), accept the Blog & UGC Terms (`consent.ugc.terms` with version), declare conflicts of interest and AI assistance, and submit. Pre-moderation by `plt_content_checker` within `web.blog.user_posts.moderation_sla_days` (default 5) with reasons on decline; advocate authors are screened for BCI Rule 36 solicitation [LAW]; the published post carries the **"Author's view — not advice"** label, the author profile and the Terms version; comments, where enabled, are pre-moderated too. Takedown follows the Grievance Redressal Policy timelines (intermediary complaints 24 h / 15 d; unlawful synthetic media 3 h [LAW; VERIFY]); the author is notified with reasons and a route to respond. Each user post emits `in.infrabyx.cms.BlogPostPublished.v1` with `author_type = user`.
- **FR-P23-223 — Vlog.** `web.vlog.enabled` (G; default OFF until the first captioned video). Items hold a self-hosted or privacy-enhanced embedded video (click-to-load, consent-gated), **mandatory English captions (WebVTT), Hindi captions where `web.locale.hi.enabled`, a transcript and an audio-description note**; an item without captions and transcript cannot publish (`LDC-WEB-057`). Chaptered videos expose chapters as text. Vlog items are tutorials' public twins; the tutorial library (§4K) links each.
- **FR-P23-224 — Resources library.** Artefacts: reports, presentations, guides, templates, checklists, whitepapers, sample board packs (synthetic), the LDC Vendor Assurance public summaries. Each resource has type, version, date, review-due date, licence (`pol.resources.default_licence` = personal_internal unless stated), optional gate (`none` | `email_gate` | `login`), file renditions (PDF/A with the Resources Download Terms and version in the footer; PPTX/DOCX where offered), alt text and a plain-language summary. Bulk upload with a manifest; download reports (aggregate); review-due queue; `in.infrabyx.cms.ResourcePublished.v1` on publish. A gated download uses `consent.resource_gate`; marketing contact needs the separate unticked control. Files are type-sniffed, AV-scanned and size-limited (≤ 100 MB); SVG is rasterised for display; no executable or macro-enabled formats.
- **FR-P23-225 — Media library hardening (applies to §4C, §4W).** Every upload (CMS, blog, resources, vlog thumbnails, brand assets): extension and MIME type sniffed and matched; AV scan; image re-encoding (EXIF stripped); SVG sanitised and served with a strict CSP or rasterised; size limits per type; "where used" before delete; soft delete with 30-day restore. Embeds (video, maps, forms) are allow-listed providers only, click-to-load, consent-gated; arbitrary iframes and scripts are not insertable (`LDC-WEB-059`). Server-side fetches for link previews and imports use an SSRF allow-list (no private ranges, no redirects to other hosts).
- **FR-P23-226 — Policy pages from Appendix AD (IPB-05).** `/legal/{slug}` renders `policy_instance` items created from the Appendix AD drafts: Privacy Notice, Terms of Use, Payment & Subscription Terms, Refund & Cancellation Policy, Cookie Policy, AI Use & Transparency Policy, Grievance Redressal Policy, Acceptable Use Policy, Data Retention & Deletion Schedule, Accessibility Statement, Security & Responsible Disclosure, Blog & UGC Terms (when user posts ON), Resources Download Terms, Data Processing Agreement, SLA, Vendor Assurance Statement, consent texts. Each instance shows title, `version_label`, effective date, last reviewed, "what changed", prior-version links (`/legal/{slug}/v/{version}` with a superseded banner), a PDF with hash, `en-IN` and `hi-IN` (summary at minimum). Publication: `plt_legal_reviewer` maker, `plt_super_admin` checker, `plt_dpo` co-approver for privacy-class; unresolved parameters, banned words, stale citations (Appendix G as `LAW_REGISTER_PORT`) and missing mandatory sections block publish (`IPB-POL-001…004`, surfaced as `LDC-WEB-060`). MAJOR changes to Terms-class documents set `reconsent_required` and respect `pol.notice_days` (30); refusal enters read-only mode with export, never silent lock-out. `/legal/index.json` is published for tenants' GRC tooling and the OH compliance calendar. The CMP vendor table and the Cookie Policy read the same registry (one source).
- **FR-P23-227 — Feedback widget and idea board (IPB-04 §04.3.11; absorbs IMP-142 and §4T article feedback).** A persistent "Feedback" control in `apps/web`, `apps/public` (help and docs pages) and the console: types bug, idea, accessibility problem, content error, praise; captures page, module, release, locale, viewport and optional screenshot (user-initiated, PII blur offered); never captures form values or sealed data. Items go to `Studio › Feedback inbox` and emit `in.infrabyx.feedback.FeedbackSubmitted.v1` to the Operations Hub backlog; the submitter sees status in Settings › Feedback. The **idea board** (`fb.ideas.enabled`, G; default ON for tenants) lets users propose and vote; votes are per user, moderated titles, no personal data in public text; roadmap statuses (Considering, Planned, Shipped) are set by `ops_product`. Article "was this helpful" stays and feeds the same inbox.
- **FR-P23-228 — Marketing tooling (IPB-04 §04.3.10; NN-62).** `TAG_MANAGER_PORT` adapters: `none` (default), `gtm_web` (web container), `server_side` (first-party server tagging). `ANALYTICS_PORT`: first-party analytics (Plausible/Umami/Matomo-class, hosted in India) — FR-P23-171 stands. Rules: every tag, pixel and embed is mapped to a consent category and fires only after consent for that category; nothing fires on authenticated routes (`apps/web`, `apps/console`) or on sensitive routes (health-check answers, grievance, legal pages' forms) regardless of consent; the sensitive-route list is locked (L); UTM capture (FR-P23-172) continues without cookies; a test mode shows the tag inventory and fires in a sandbox. `Studio › Analytics & Tags` is maker-checker for `plt_super_admin` with `plt_dpo` veto. Choosing `gtm_web` or `server_side` is owner decision #30; until then `none`.
- **FR-P23-229 — WhatsApp and Meta.** Public-site WhatsApp entry points and the tenant notification channel use the existing `MESSAGING_PORT` WhatsApp adapter with the super-admin toggle `msg.whatsapp.enabled` (default OFF) and Meta template categories (utility, authentication, marketing) mapped to consent purposes; marketing templates send only with `consent.marketing.whatsapp`; templates are approved through the OH registry and the group listens to `in.infrabyx.messaging.WhatsAppTemplateApproved.v1`; never for collection, recovery or legal notices (master §11).
- **FR-P23-230 — Captions, live captions and visual alerts (IPB-06 §06.3.3; amends §4K and §4L).** Every published tutorial, vlog item and webinar recording has English captions (WebVTT), a transcript and, where `web.locale.hi.enabled`, Hindi captions; live webinars and Academy sessions offer live captions (auto-generated, labelled "automatic captions") and an Indian Sign Language interpreter slot on request with 3 working days' notice; every audible alert in `apps/web` has a visual equivalent (badge, banner or focus move) and every timed notification is also available in the Work Inbox. Captions and transcripts are release gates — the accessibility CI job fails on a video asset without them.
- **FR-P23-231 — Dyslexia-friendly font and reading aids (IPB-06 §06.3.4).** Settings › Accessibility offers `a11y.text.font` (default | OpenDyslexic | Atkinson Hyperlegible; self-hosted), letter and line spacing steps, reading ruler, and text-to-speech of the current pane through `SPEECH_PORT` (`bhashini` or `azure_speech_in`, India-resident) — all per user, remembered across devices, applied to `apps/public` through the same preference cookie (necessary category).
- **FR-P23-232 — `gov_facing` mode (IPB-06-04).** For government or listed-company tenants, `a11y.gov_facing` (G) enables the GIGW 3.0 checklist in the accessibility conformance report, the IS 17802 clause map in the Accessibility Statement and the ACR export in the format the tenant's regulator asks for [VERIFY RPwD (Amendment) Rules 2026 final text, OI-P23-01].
- **FR-P23-233 — "i" registry as the group seed (IPB-07 §07.3.4).** Keys follow `hlp.<module>.<term>` (lower-snake term; module codes of master §5.3); CI lint fails a build that ships a user-visible term tagged `glossary` without a registered key or with a key whose law citation is not in Appendix G; every entry with a `[LAW]` citation names a reviewer of record (`plt_legal_reviewer` backfills); the "i" popover shows the plain-language definition, the regulatory reference panel (instrument, clause, link, last verified date), related terms and "report a problem". LDC publishes `in.infrabyx.content.GlossaryEntryPublished.v1` so sibling products reuse entries. Seed target: 400 terms at Wave 1 GA, 1,200 by Wave 3 (Appendix P §P.4 priorities).
- **FR-P23-234 — What's new.** Release cards in `apps/web` (Settings › What's new and a bell entry) from the P24 release-notes pipeline: tenant-facing entries with `reg:*` tags approved by `plt_legal_reviewer`, per-release articles in the help centre, suppression level per tenant (`tut.whats_new.level`: all | regulatory only | none); the public Changelog shows only public entries (FR-P23-218).
- **FR-P23-235 — Health Check as the ecosystem funnel pattern.** No change to §4E, §4F or §4U; the IPB names LDC's free Health Check, Claims Register and Health Check Studio as the pattern for the other products. The hand-off to the Hub (§5.7) now uses `in.infrabyx.crm.LeadCaptured.v1` with the consent receipt id; the synthetic sample report and the "Health Check Score" label (X-46) are unchanged.

### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P23-X01 — Tracker feed and co-operative locale.** The public RBI Directions Tracker (FR-P23-193A) consumes `cnt.CoverageStateChanged` and `chg.InstrumentCatalogued` (metadata only) and shows coverage states (Planned / In preparation / Available / Superseded); co-operative notice templates and the member-portal UI ship in Hindi with the second-locale programme (D-30).

---

## 5. Workflows and state machines

### 5.1 Health-check session

States: `STARTED` → `PROFILED` → `IN_PROGRESS` → `COMPLETED` → (`REPORT_SHARED`)* → `CONVERTED` | `EXPIRED` | `ERASED`.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | Visitor selects family | — | STARTED | `HealthCheckStarted` (anonymous session id, family, UTM) |
| STARTED | Profile confirmed (with or without lookup) | family + type chosen | PROFILED | Applicability evaluated; question set frozen with bank version |
| PROFILED | First answer saved | — | IN_PROGRESS | Autosave; resume token offered after segment 1 |
| IN_PROGRESS | Submit | ≥ 90% of applicable questions answered (remaining treated as Not sure, shown before submit) | COMPLETED | Score computed with model version; report rendered; `HealthCheckCompleted`; `LeadCaptured` if contact consent |
| COMPLETED | Share link created | owner verified by magic link | REPORT_SHARED | `HealthCheckReportShared` (count only) |
| COMPLETED/REPORT_SHARED | Trial started from report | P01 provisioning success | CONVERTED | `TrialStartedFromHealthCheck`; baseline import offered |
| any (not CONVERTED) | Retention timer (setting `web.hc.retention_days`, default 365) | no active trial/tenant | EXPIRED → ERASED | Personal data deleted; anonymised scores retained for benchmarks (k ≥ 30) |
| any | Erasure request by lead | identity verified | ERASED | Hub notified (`LeadErasureRequested`), consents withdrawn, share links revoked |

Abandoned sessions (`IN_PROGRESS` with no answer for 30 days) are purged unless a resume token was issued to a verified email, in which case one reminder is allowed with marketing consent only.

*(v1.2)* At PROFILED the session also pins `set_version_id` (`HC-SET-<NNNN>/v<n>`) and, where an experiment runs, the arm; at CONVERTED the `hc_baseline` payload of FR-P23-207 is emitted (`web.HcBaselinePrefillRequested`).

### 5.1A Health-check set version *(v1.2)*

`DRAFT` → (submit; test harness green; no unresolved retired bindings) → `IN_REVIEW` → (checker ≠ maker) → `APPROVED` → (publisher; optional schedule) → `PUBLISHED` → (superseded or withdrawn) → `RETIRED`. `IN_REVIEW` → `DRAFT` on return with comments. A PUBLISHED version flagged "needs review" (FR-P23-206) stays live with successor citations until the next version publishes; retirement never deletes sessions or reports.

### 5.2 CMS page version

`DRAFT` → `IN_REVIEW` → (`CHANGES_REQUESTED` → `DRAFT`) → `APPROVED` → `SCHEDULED` → `PUBLISHED` → `SUPERSEDED` (by a newer published version) or `UNPUBLISHED`. Guards: maker ≠ checker for `APPROVED`; pre-publish checks (FR-P23-23) green for `SCHEDULED`/`PUBLISHED`; legal pages (privacy, terms, refund, accessibility statement) additionally require `plt_super_admin` or legal approver. Every transition is a ledger event; rollback creates a new `PUBLISHED` version referencing the restored one.

### 5.3 Claim

`DRAFT` → `EVIDENCE_ATTACHED` → `APPROVED` → (`EXPIRING` at T-30 days) → `EXPIRED` | `RENEWED` | `WITHDRAWN`. On `EXPIRED`/`WITHDRAWN`: all bound blocks are re-rendered with fallback text and pages republished automatically; owner and publisher notified; the event is visible in the CMS audit view.

### 5.4 Glossary term ("i" key)

`REGISTERED` (key created by a developer with a placeholder) → `DRAFTED` → `REVIEWED` (regulatory reviewer if the term has a legal definition) → `PUBLISHED` → `REVIEW_DUE` (when the linked clause changes, P05 impact, or 12 months elapse) → `PUBLISHED` (new version) | `DEPRECATED` (term no longer used; key kept for old references). A UI build fails if any registered key used in the build is still `REGISTERED` in a release branch (placeholder text is allowed only on feature branches).

### 5.5 Tutorial asset

`PLANNED` → `SCRIPTED` → `CAPTURED` (screenshots/recording from demo tenant) → `CAPTIONED` (human-corrected) → `REVIEWED` (product + accessibility + regulatory where needed) → `PUBLISHED` → `STALE` (diff detected or product version mismatch) → `REFRESHED` → `PUBLISHED` | `RETIRED`. Social derivatives follow the parent and are re-issued to the Hub on refresh.

### 5.6 Accessibility issue

`REPORTED` (grievance, audit, automated, internal test) → `TRIAGED` (WCAG criterion, severity, affected flows) → `IN_PROGRESS` → `FIXED` → `VERIFIED` (re-test by specialist, and by the reporter where the issue came from a user) → `CLOSED`; or `EXCEPTION_APPROVED` (time-boxed, dual-approved, listed in the ACR) → back to `IN_PROGRESS` on expiry. SLA timers per severity (FR-P23-138, FR-P23-140) with escalation to the CTO at breach.

### 5.7 Lead hand-off (to the Hub)

`CAPTURED` (LDC) → `DELIVERED` (Hub ack, ≤ 60 s; retries with exponential back-off, dead-letter after 24 h and alert) → `ACCEPTED` (Hub dedupe/merge) → owned by the Hub thereafter. LDC keeps only the consent artefacts, the report and a pointer; marketing status lives in the Hub. Consent changes made in either system propagate by events (`MarketingConsentChanged`).

---

### 5.8 Brand-pack version *(v1.3)*

`DRAFT → CONTRAST_CHECKED → IN_REVIEW → PUBLISHED → SUPERSEDED` (and `ROLLED_BACK` as a new PUBLISHED version pointing at an earlier snapshot). Contrast check is automatic at save; a failing pair stays `DRAFT` (`LDC-WEB-053`). Publish needs a checker different from the maker; the CDN cache for every host in the pack is purged on publish; `tenancy.BrandPackPublished` emitted; hosts added in the version must be verified before the version can publish (`LDC-WEB-054`).

### 5.9 User post *(v1.3; NN-64)*

`DRAFT (author) → SUBMITTED → IN_MODERATION → APPROVED → PUBLISHED → (UNPUBLISHED | TAKEN_DOWN)`; `DECLINED` from `IN_MODERATION` with reasons; `WITHDRAWN` by the author from any pre-publish state. Only `PUBLISHED` is routable. A complaint moves `PUBLISHED → UNDER_COMPLAINT` with the Grievance timers; `TAKEN_DOWN` keeps the record for the Transparency Report and the author's appeal window (7 days). Terms version and author declarations are frozen at `SUBMITTED`.

### 5.10 Resource version *(v1.3)*

`DRAFT → SCANNED → IN_REVIEW → PUBLISHED → REVIEW_DUE → (REPUBLISHED as new version | WITHDRAWN)`; `QUARANTINED` from `SCANNED` when the AV or type check fails (file never served). Gated downloads record the consent receipt; a version past its review-due date shows a "check for a newer version" banner and is listed in the review-due queue.

### 5.11 Policy instance *(v1.3; IPB-05 §05.4.19)*

`DRAFT → LINTED → APPROVED (maker-checker, DPO where privacy-class) → SCHEDULED (effective_at ≥ now + pol.notice_days for MAJOR) → EFFECTIVE → SUPERSEDED`; `REVIEW_DUE` flag by cadence. `PolicyEffective` triggers the re-consent or acknowledgement flow; `AcceptanceRefused` puts the user in read-only mode with export; the prior version stays reachable at its archive URL.

## 6. Screens and UX

Public site screens (prefix `SCR-WEB`), help/learning screens (prefix `SCR-HLP`). Every screen ships with empty, loading, error and offline states, keyboard map and "i" keys. Design principle: one primary action per screen, visible progress, nothing hidden behind hover, and no more than three clicks from the home page to the health check, pricing, any solution page or any glossary term.

| Screen ID | Name | Route / menu path | Key content and behaviour |
|---|---|---|---|
| SCR-WEB-01 | Home | `/` | Audience-led hero ("GRC for India's regulated entities — RBI, SEBI, IFSCA, IRDAI, co-operatives, companies"), two CTAs (Free health check; Start 7-day trial), family selector tiles, module overview, "how it works" (3 steps), live counts from the library (Claims-bound), Vidhi AI explainer, marketplace and academy strip, trust strip, latest regulatory updates, footer |
| SCR-WEB-02 | Solution (family) | `/solutions/<family>` | Pain → outcome; "What applies to you" instrument list (live); module highlights for the family; family-preset health check; returns covered (Return Studio, P11) for financial families; marketplace services; academy courses; FAQs; case study when claim-approved |
| SCR-WEB-03 | Module | `/platform/<module>` | What it does, for whom, key workflows with screenshots from demo tenant, integrations, tutorial playlist, plan availability (from P20 entitlements), related glossary |
| SCR-WEB-04 | Pricing | `/pricing` | Rendered from P20: three packages, monthly/annual toggle, GST note, add-on configurator (running total, Apple-style step summary), comparison table (accessible table with row headers, sticky header that does not obscure focus), services-only path, FAQs, "talk to us" for enterprise |
| SCR-WEB-05 | Marketplace entry | `/marketplace`, `/marketplace/<category>`, `/marketplace/<service>` | Public render of P21 catalogue without login; filters; provider profile within D-06 rules; "Buy" → P21 checkout |
| SCR-WEB-06 | Academy | `/academy` | Course cards from trainings.lawdocs.in (P21 sync), deep links, CPD info where applicable |
| SCR-WEB-07 | Regulatory updates index | `/regulatory-updates` | Filters (regulator, family, type, date), RSS links, digest subscribe |
| SCR-WEB-08 | Regulatory update item | `/regulatory-updates/<regulator>/<yyyy>/<slug>` | Summary blocks, source link, effective date, affected families, related terms, CTAs |
| SCR-WEB-09 | Glossary index | `/glossary` | A–Z, by regulator, by topic, search |
| SCR-WEB-10 | Glossary term | `/glossary/<slug>` | Plain definition, legal definition with citation, example, related terms, where used in LDC, video |
| SCR-WEB-11 | Insights / blog | `/insights`, `/insights/<slug>` | Articles with author and reviewer, last reviewed date, table of contents, related |
| SCR-WEB-12 | Guides & checklists | `/guides/<slug>` | Downloadable checklists (accessible PDF + DOCX + XLSX) with optional email gate (configurable per guide) |
| SCR-WEB-13 | Webinars | `/webinars`, `/webinars/<slug>` | Registration, ICS, replay with captions/chapters |
| SCR-WEB-14 | Case studies | `/customers/<slug>` | Only claim-approved; outcome metrics bound to claims |
| SCR-WEB-15 | Trust Centre | `/trust` | §4P |
| SCR-WEB-16 | Accessibility statement & ACR | `/accessibility`, `/accessibility/acr` | §4L.5 |
| SCR-WEB-17 | About / Company | `/about` | Group context (Infrabyx ecosystem, disambiguation), leadership (permitted bio fields), contact, legal identity |
| SCR-WEB-18 | Contact & book demo | `/contact`, `/book-demo` | Accessible form, calendar booking (Hub), WhatsApp click-to-chat (DLT-compliant), phone, office addresses (Delhi, Noida, Jaipur) [VERIFY] |
| SCR-WEB-19 | Legal pages | `/privacy`, `/terms`, `/cookies`, `/refund-policy`, `/grievance-officer`, `/dpa` | Versioned; change log |
| SCR-WEB-20 | Campaign landing | `/lp/<slug>` | Variant template (FR-P23-70) |
| SCR-WEB-21 | Health check — start | `/health-check` | Family tiles, "Not sure?" helper, what you'll get, time estimate, privacy note |
| SCR-WEB-22 | Health check — organisation lookup | `/health-check/organisation` | Name/CIN/PAN search, results list, confirm, skip |
| SCR-WEB-23 | Health check — profile | `/health-check/profile` | ≤ 6 refiners |
| SCR-WEB-24 | Health check — segment | `/health-check/s/<n>` | 4–6 questions, "i" help, citation, answer scale, progress, save & resume |
| SCR-WEB-25 | Health check — review & consent | `/health-check/review` | Unanswered list, consent checkboxes, notice |
| SCR-WEB-26 | Health check — result | `/health-check/result/<id>` | Score, band, confidence, segment chart + table, critical gaps, action plan, CTAs (trial, expert review, share, download) |
| SCR-WEB-27 | Health check — shared report | `/hc/r/<token>` | Read-only, banner, `noindex` |
| SCR-WEB-28 | Lead portal | `/my/reports` (magic link) | Past reports, trend, retake, consent preferences, delete my data |
| SCR-WEB-29 | Status page | `status.lawdocscomply.com` | Component status, incidents, maintenance |
| SCR-WEB-30 | Console — CMS pages | `apps/console` → Website → Pages | List, filters by status/type/locale, bulk actions (schedule, unpublish), preview |
| SCR-WEB-31 | Console — page editor | Website → Pages → Edit | Block editor with schema validation, live preview, pre-publish check panel, claims binding, SEO panel (title, description, canonical, schema preview), accessibility panel (axe results) |
| SCR-WEB-32 | Console — Claims Register | Website → Claims | Register, evidence, expiry calendar, bound pages |
| SCR-WEB-33 | Console — Health-check studio | Website → Health check | Question bank by family (versioned), weights, applicability rules (JSON Logic editor with test profiles), scoring model, band texts, report template, analytics (completion funnel, drop-off by question) |
| SCR-WEB-34 | Console — Redirects & SEO | Website → SEO | Redirect map, sitemap status, robots/AI-crawler policy (Governed), llms.txt preview, structured-data validator, AI answer panel results |
| SCR-WEB-35 | Console — Experiments | Website → Experiments | Variants, allocation, results, guard (no experiments on legal/pricing amounts) |
| SCR-HLP-01 | Help panel (in-app) | `?` from any screen | Context articles, video, terms on screen, Ask Vidhi (help mode), contact support, tenant notes |
| SCR-HLP-02 | Help centre home | `help.lawdocscomply.com` | Search, role paths, popular, what's new, status |
| SCR-HLP-03 | Article | `/articles/<slug>` | Steps, screenshots, video, feedback, last reviewed |
| SCR-HLP-04 | Tutorials library | `/tutorials` | Filters: role, module, family, length, language; playlists |
| SCR-HLP-05 | Tutorial player | `/tutorials/<slug>` | Accessible player, transcript panel, chapters, quick card download, ISL toggle where available |
| SCR-HLP-06 | Learning paths | `/learn/<path>` | Steps, progress, knowledge checks |
| SCR-HLP-07 | Release notes | `/releases` | By version, by module, "what changed for my role", stale-tutorial notes |
| SCR-HLP-08 | Accessibility & display preferences | Profile → Accessibility and display | §4L.3 |
| SCR-HLP-09 | Report an accessibility problem | Footer / Help panel | Form + alternatives |
| SCR-HLP-10 | Console — Glossary studio | Console → Help → Glossary | Keys registry, coverage report (keys used in build vs published), review queue, legal-definition links, locales |
| SCR-HLP-11 | Console — Help articles | Console → Help → Articles | Editor, mapping to help keys, staleness queue, feedback |
| SCR-HLP-12 | Console — Tutorials | Console → Help → Tutorials | Pipeline board (Planned → Published), capture runs, diff results, caption QA, social derivatives hand-off |
| SCR-HLP-13 | Console — Tours | Console → Help → Tours | Step editor, targeting, analytics |
| SCR-HLP-14 | Console — Accessibility | Console → Quality → Accessibility | Conformance register by WCAG SC, issues, audits, ACR builder, grievance queue |
| SCR-HLP-15 | Tenant — help notes | Settings → Help & guidance | Tenant notes per help key, tenant tours on/off, learning-path reporting setting |

Keyboard shortcuts (all remappable/disable-able, FR-P23-129): `?` help panel, `/` focus search, `g h` go home, `g t` my tasks, `Esc` close popover/dialog; the public site uses no single-key shortcuts.

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-WEB-40 | Market selector and market home | Public header → Market | Market subfolders, currency, seller |
| SCR-WEB-41 | Country solution page | `/<market>/solutions/<country>-compliance` | Generated from pack registry |
| SCR-WEB-42 | Global health check — start | `/health-check/global` | Country, form, size |
| SCR-WEB-43 | Global health check — report | `/health-check/global/report/<id>` | Generic vs pack-backed labelling |
| SCR-WEB-44 | Vidhi agents page | `/vidhi-ai-agents` | Agent transparency |
| SCR-WEB-45 | Connect your AI assistant | `/connect-your-ai-assistant` | MCP set-up guide |

**Screens added in v1.2** *(v1.2)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-WEB-50 | Health Check Studio — sets | Console › Website › Health Check Studio | Sets by family/channel/locale, versions, status, live arm, needs-review flags |
| SCR-WEB-51 | Set editor | Studio › *set* › *version* | Sections, counts, weights (Σ check), order, per-item wording, options, scoring, branching, bindings panel |
| SCR-WEB-52 | Library picker by CompID | Set editor › Add questions | Search by CompID/alias/text; filters family, authority, instrument, section, department, function, compliance type, risk; multi-bind |
| SCR-WEB-53 | Preview as sample entity | Set editor › Preview | Sample entity selector, public/in-app rendering, applicable count, time estimate, test harness |
| SCR-WEB-54 | Version diff and approval | Work Inbox › Health-check review | Diff by item and CompID, harness results, approve/return, publish/schedule |
| SCR-WEB-55 | Experiments and drop-off | Studio › Analytics | Funnel per version/arm, per-question abandonment and time, Not sure/N/A rates, guard metrics, promote winner |

---

**Screens added in v1.3** *(v1.3)*: SCR-WEB-56 Studio › Brand (brand-pack editor with live preview, contrast report, host map, publish/rollback); SCR-WEB-57 Studio › Blog › Bulk import (upload, conversion progress, per-item preview and diff, accept/reject, undo); SCR-WEB-58 Studio › Blog › Moderation queue (user posts, declarations, Rule 36 screen, decision with reasons); SCR-WEB-59 Studio › Resources (artefacts, versions, gating, review-due queue, download report); SCR-WEB-60 Studio › Policies (policy set per brand pack, parameter block, lint results, diff, effective-date scheduler, re-consent flag); SCR-WEB-61 Studio › Feedback inbox and idea board moderation; SCR-WEB-62 Studio › Analytics & Tags (adapter, container id, consent mapping, locked sensitive routes, pixel inventory, test mode); SCR-WEB-63 Public Investors page (toggle preview with locked disclaimer and legal-review banner). Tenant-side: Settings › Feedback, Settings › What's new, Settings › Accessibility (font, spacing, captions) and Settings › Security & trust are specified in Appendix C §C.3.6A.

## 7. Backend design

### 7.1 Modules touched

`web` (owner), `hlp` (owner), `iam`/`core` (consent ledger, magic links, audit), `cfg` (settings, terminology, help-key registry), `cnt`/`chg` (library counts, update summaries), `pack` (families, applicability), `bil` (pricing render), `mkp` (marketplace render), `int` (Hub events, lookup adapters), `ai` (narrative summaries, drafting), `dms` (claims evidence, PDF rendering), `rpt` (charts).

### 7.2 Tables (schema `web` and `hlp`; tenant-scoped tables carry `tenant_id` with RLS, platform tables do not)

| Table | Key columns |
|---|---|
| `web.pages` | id, type, slug, locale, current_version_id, status, owner_id, noindex, created_at |
| `web.page_versions` | id, page_id, version_no, blocks jsonb, meta jsonb (title, description, canonical, og), schema_jsonld jsonb, claim_ids[], status, maker_id, checker_id, publisher_id, publish_at, unpublish_at, content_hash, created_at |
| `web.redirects` | from_path, to_path, code (301/308), reason, created_by |
| `web.experiments` | id, page_id, variants jsonb, allocation, status, guard_checks jsonb |
| `web.claims` | id, text, type, evidence_dms_id, evidence_hash, live_metric_key, owner_id, approver_id, valid_from, expires_at, surfaces[], fallback_text, status |
| `web.authors` | id, person_name, profession, rule_mode, permitted_fields jsonb, reviewer_flag |
| `web.hc_banks` | id, family, version, status, published_at, checker_id |
| `web.hc_questions` | id, bank_id, code (e.g., `HC-GOV-01`), segment, text, variant_of, applicability jsonlogic, weight, why_text, citation jsonb, module_link, service_link, glossary_keys[], reserve_for |
| `web.hc_scoring_models` | id, version, segment_weights jsonb (per family), bands jsonb, critical_rules jsonb, confidence_rules jsonb |
| `web.hc_sessions` | id, anon_id, family, type, profile jsonb, org_lookup_ref, bank_id, model_id, status, utm jsonb, partner_code, started_at, completed_at, expires_at |
| `web.hc_answers` | session_id, question_id, answer, na_reason, answered_at |
| `web.hc_reports` | id, session_id, overall, band, confidence, segment_scores jsonb, critical_gaps jsonb, action_plan jsonb, narrative jsonb (ai flag), pdf_dms_id, pdf_hash, created_at |
| `web.hc_share_links` | token_hash, report_id, expires_at, password_hash, revoked_at, view_count |
| `web.hc_sets` *(v1.2)* | set_id (`HC-SET-<NNNN>`), name, hc_family, template_families[], channel, locales[], current_published_version_id, status |
| `web.hc_set_versions` *(v1.2)* | version_id, set_id, version_no, scoring_model_id, total_cap, est_minutes, status, maker_id, checker_id, publisher_id, publish_at, harness_result jsonb, content_hash |
| `web.hc_set_sections` *(v1.2)* | version_id, section_code, title, order_no, weight, show_mode (FIXED/POOL), show_n |
| `web.hc_set_items` *(v1.2)* | item_id, version_id, section_code, question_code (`HC-<SEG>-<NN>`), order_no, weight, critical bool, wording jsonb (per locale), answer_type, options jsonb (label, score), na_policy, branch_rule jsonlogic |
| `web.hc_item_bindings` *(v1.2)* | item_id, target_type (COMP_ID/PLACEHOLDER/BANK), target_id, primary bool, family_scope, state (LIVE/NEEDS_REVIEW/RESOLVED) |
| `web.hc_sample_entities` *(v1.2)* | id, name, profile jsonb, created_by |
| `web.hc_funnel_daily` *(v1.2)* | date, version_id, arm, step, item_id nullable, entered, exited, median_seconds, not_sure, na (aggregates only) |
| `web.hc_baseline_exports` *(v1.2)* | session_id, tenant_id, items jsonb ([comp_id, answer, baseline_state]), placeholders jsonb, sent_at, ack_at |
| `web.hc_sessions` — added columns *(v1.2)* | set_version_id, experiment_arm |
| `web.leads` | id, email_hash, email_enc, phone_enc, name_enc, org_name, family, consents jsonb (artefact ids), source jsonb, hub_lead_ref, status, erased_at |
| `web.reg_update_summaries` | id, chg_update_id, slug, summary blocks, reviewer_id, published_at |
| `hlp.terms` | key, slug, canonical, abbreviations[], plain, detail, legal_definition jsonb (clause_id, version), example, related[], families[], authority, status, version, review_due |
| `hlp.term_locales` | key, locale, fields jsonb, reviewer_id |
| `hlp.help_keys` | help_key, screen_id, module, roles[], article_ids[], tutorial_ids[] |
| `hlp.articles` | id, slug, type, body, roles[], families[], product_version, owner_id, last_reviewed_at, status |
| `hlp.tenant_notes` | tenant_id, help_key, body, author_id, updated_at (RLS) |
| `hlp.tours` | id, steps jsonb, roles[], families[], trigger, status |
| `hlp.tutorials` | id, slug, role, module, steps jsonb, video_asset_id, captions[], transcript, isl_asset_id, audio_desc_asset_id, product_version, status, stale_reason |
| `hlp.media_assets` | id, kind, storage_key, hash, alt_text, long_desc, locale, source (demo tenant id / design), rights |
| `hlp.learning_paths`, `hlp.learning_progress` | path, steps; tenant_id, user_id, step, completed_at (RLS) |
| `hlp.a11y_conformance` | release, criterion (e.g., `2.4.11`), surface, result, evidence, tester, date |
| `hlp.a11y_issues` | id, source, criterion, severity, surface, description, reporter_contact_enc, status, due_at, exception jsonb |
| `iam.user_preferences` (P01) | user_id, a11y jsonb (text_scale, spacing, font, theme, motion, captions, shortcuts, inline_terms, simplified_layout, read_aloud) |

**Tables added in v1.3** *(v1.3; schema `web` per IPB-DEV-01, IPB-04 column names)*: `web.brand_packs` (id, scope platform|tenant|white_label, app_name, legal_entity_ref, current_version_id, status), `web.brand_pack_versions` (id, brand_pack_id, tokens jsonb, logo refs, favicon refs, og_image_ref, email_identity jsonb, hosts jsonb, social jsonb, terminology jsonb, contrast_report jsonb, state, maker_id, checker_id, published_at), `web.hosts` (host, brand_pack_id, verification_token, verified_at, cert_status), `web.team_members` (id, group, name, role, bio, photo_ref, photo_consent, photo_consent_at, linkedin, din, sort), `web.posts` gains `author_type` (staff|user), `author_user_id`, `moderation_state`, `ugc_terms_version`, `declarations jsonb`; `web.bulk_import_jobs` (id, kind docx|resources, file_count, state, change_set_id, undo_until, log_ref); `web.resources` (id, type, title, slug, licence, gate, review_due_at, state) and `web.resource_versions` (id, resource_id, version, file_refs jsonb, scan_result, summary, published_at); `web.policy_instances` (id, key, template_version, version_label, params jsonb, rendered_hash, pdf_ref, locale, effective_at, last_reviewed_at, reconsent_required, state, maker_id, checker_id, dpo_id) and `web.policy_acceptances` (user_id, key, version_label, kind accept|acknowledge|refuse, ui_version, at); `web.consent_texts` (key, version, locale, text); `web.feedback_items` (id, tenant_id nullable, type, module, page, release, severity, state, oh_ref, screenshot_ref) and `web.ideas` / `web.idea_votes`; `web.tag_inventory` (tag_id, adapter, consent_category, routes_excluded, state); `web.changelog_entries` (id, release_id, audience public|tenant, areas, body_ref, published_at). All platform tables are append-only versioned; tenant-scoped rows (`feedback_items`, `idea_votes`, `policy_acceptances`) carry `tenant_id` with RLS (NN-01).

### 7.3 APIs (public APIs under `/v1/public/*`, rate-limited, no auth; console APIs under `/v1/console/*`, platform roles only)

| Method & path | Purpose |
|---|---|
| `GET /v1/public/pages/{slug}?locale=` | Published page (used by ISR) |
| `POST /v1/public/org-lookup` | Name/CIN/PAN lookup via P18 adapter (returns masked, minimal fields) |
| `POST /v1/public/health-checks` | Start session (family, type, utm) |
| `PUT /v1/public/health-checks/{id}/profile` | Save profile and refiners |
| `GET /v1/public/health-checks/{id}/questions?segment=` | Applicable questions |
| `PUT /v1/public/health-checks/{id}/answers` | Save answers (idempotent per question) |
| `POST /v1/public/health-checks/{id}/submit` | Compute and render report |
| `POST /v1/public/health-checks/{id}/consents` | Record consents (writes P01 ledger) |
| `POST /v1/public/health-checks/{id}/share-links` / `DELETE …/{token}` | Create/revoke share link |
| `POST /v1/public/health-checks/{id}/trial` | Hand-off to P01 trial with pre-fill payload |
| `POST /v1/public/magic-links` | Lead portal / resume |
| `GET /v1/public/glossary/{slug}`, `GET /v1/public/glossary?query=` | Terms |
| `GET /v1/public/help/search?q=&role=&family=` | Help search |
| `POST /v1/public/a11y-issues` | Accessibility report |
| `GET /llms.txt`, `/llms-full.txt`, `/robots.txt`, `/sitemap-index.xml`, `/.well-known/security.txt` | Generated files |
| `GET /v1/help/context/{help_key}` (authenticated) | Help panel payload incl. tenant notes |
| `PUT /v1/tenant/help-notes/{help_key}` | Tenant note (ten_admin) |
| `PUT /v1/me/preferences/accessibility` | User accessibility preferences |
| `/v1/console/pages/*`, `/claims/*`, `/hc-banks/*`, `/hc-models/*`, `/glossary/*`, `/articles/*`, `/tutorials/*`, `/tours/*`, `/a11y/*`, `/redirects/*`, `/experiments/*` | Console CRUD and workflow transitions (maker/checker/publisher) |
| `/v1/console/hc-sets/*` *(v1.2)* — `GET/POST /hc-sets`, `POST /hc-sets/{id}/versions`, `PUT /hc-sets/{id}/versions/{v}` (sections, items, bindings), `POST …/{v}/preview` (sample entity), `POST …/{v}/harness`, `POST …/{v}/submit|approve|return|publish`, `GET …/{v}/diff?against=`, `GET /hc-library/search?q=&family=&authority=&instrument=&section=&department=&function=&compliance_type=&risk=`, `GET /hc-sets/{id}/analytics?version=&arm=` | Health Check Studio (platform roles only; maker ≠ checker enforced server-side) |
| `GET /v1/public/health-check/set?family=&type=&locale=&channel=` *(v1.2)* | Resolves the published set version (and experiment arm) for the visitor; returns items with wording, options and branching, never CompID internals beyond the citation |

### 7.4 Domain events (CloudEvents; `type` `in.lawdocscomply.<module>.<Name>.v1`)

`web.HealthCheckStarted`, `web.HealthCheckCompleted`, `web.HealthCheckReportShared`, `web.LeadCaptured` (→ Hub CRM), `web.MarketingConsentChanged` (↔ Hub), `web.LeadErasureRequested` (→ Hub), `web.TrialStartedFromHealthCheck` (→ P01, Hub), `web.PagePublished`, `web.PageUnpublished`, `web.ClaimApproved`, `web.ClaimExpired`, `web.ExperimentConcluded`, `web.WebinarRegistered` (→ Hub), `hlp.GlossaryTermPublished`, `hlp.GlossaryTermReviewDue`, `hlp.TutorialPublished`, `hlp.TutorialStale`, `hlp.SocialAssetReady` (→ Hub social calendar), `hlp.AccessibilityIssueReported`, `hlp.AccessibilityIssueBreached`, `hlp.AcrPublished`. Consumed: `cnt.InstrumentVersionPublished` (page/term review tasks), `chg.UpdatePublished` (public summary task), `bil.CatalogueVersionPublished` (pricing revalidation), `mkp.ServicePublished` (marketplace page revalidation), `core.ReleaseDeployed` (tutorial diff run).

*(v1.2)* `web.HcSetVersionSubmitted`, `web.HcSetVersionPublished` (set_id, version, family, channel), `web.HcSetNeedsReview` (set_id, comp_id, reason; consumes P03 `cnt.CompIdRetired` / `cnt.CompIdLineageRecorded`), `web.HcPlaceholderResolved` (placeholder_id, comp_ids; consumes `cnt.CompIdAliasAdded`), `web.HcExperimentConcluded`, `web.HcBaselinePrefillRequested` (→ P01, P04; tenant_id, session_id, [comp_id, answer, baseline_state]); all carry `business_id` = the set ID or CompID (NN-57).

**Cross-product publication (X-01).** Events marked → Hub or ↔ Hub (`LeadCaptured`, `MarketingConsentChanged`, `LeadErasureRequested`, `TrialStartedFromHealthCheck`, `WebinarRegistered`, `SocialAssetReady`, and the band-only projection of `HealthCheckCompleted`) leave LDC only through the `int` module with Ecosystem Spec types `in.infrabyx.ops.<EventName>.v1` and `source = urn:infrabyx:ldc:<tenantid or public>`; the internal `in.lawdocscomply.*` types above stay inside LDC. These are new contracts and are added to the Ecosystem Spec v1.2 change request (master §19 item 7) before go-live; until approved, leads reach OH3 through the existing `POST /v1/crm/requests` contract (§6.29).

*(v1.3)* `tenancy.BrandPackPublished` (brand_pack_id, version, hosts[]), `web.PostSubmittedForModeration`, `web.PostModerated` (post_id, decision), `web.BulkImportCompleted` (job_id, accepted, rejected, undo_until), `web.ResourcePublished`, `web.ResourceReviewDue`, `cms.PolicyDrafted`, `cms.PolicyApproved`, `cms.PolicyEffective`, `cms.PolicyReviewDue`, `pol.AcceptanceRecorded`, `pol.AcknowledgementRecorded`, `pol.AcceptanceRefused`, `fb.FeedbackSubmitted`, `fb.IdeaVoted`, `mkt.TagInventoryChanged`, `hlp.GlossaryEntryPublished`. Cross-product (through `int`, X-01): `in.infrabyx.cms.BlogPostPublished.v1`, `in.infrabyx.cms.ResourcePublished.v1`, `in.infrabyx.feedback.FeedbackSubmitted.v1`, `in.infrabyx.crm.LeadCaptured.v1` (replaces the ad-hoc `LeadCaptured` payload once Spec v1.2 registers it), `in.infrabyx.consent.MarketingConsentUpdated.v1`, `in.infrabyx.grc.PolicyEffective.v1`, `in.infrabyx.grc.PolicyAttested.v1`, `in.infrabyx.content.GlossaryEntryPublished.v1`; consumed: `in.infrabyx.trust.VendorAssuranceDocumentPublished.v1` (Trust Centre), `in.infrabyx.messaging.WhatsAppTemplateApproved.v1`.

### 7.5 Jobs and Temporal workflows

`HealthCheckReportWorkflow` (score → narrative (optional) → PDF → hash → email → Hub event, with compensation if Hub delivery fails); `LeadDeliveryWorkflow` (retry, dead-letter, alert); `RetentionSweep` (daily 02:00 IST: expire/erase sessions and leads past retention); `ClaimExpiryJob` (daily: T-30 warnings, expiry republish); `RevalidationDispatcher` (on publish events); `SitemapAndIndexNow` (on publish); `TutorialCaptureRun` (on `ReleaseDeployed`: Playwright capture on demo tenant, perceptual diff, mark stale); `A11yNightly` (Pa11y over sitemap, axe on console/app smoke routes, PDF/UA templates); `AiAnswerPanelMonthly` (operator-assisted run of the 30 prompts — results entered or captured through approved tools; no scraping that breaches terms); `GlossaryCoverageCheck` (on build); `TermReviewDue` (on instrument change).

---

## 8. Integrations (ports and adapters)

| Port | Adapter(s) | Notes |
|---|---|---|
| `COMPANY_DATA_PORT` (P18) | Licensed MCA master-data providers; PAN verification via an authorised provider | Health-check lookup; terms must allow lead-flow use [VERIFY]; masked output; no bureau |
| `CRM_PORT` (to Hub) | Infrabyx Operations Hub (Ecosystem Spec §6.29 `ops`; scopes `crm.request:write`) | Leads, consents, webinar registrations, conversion events; Hub owns Brevo |
| `CONSENT_PORT` | P01 consent ledger | Artefacts with notice versions |
| `PAYMENT_PORT` | P20 (Razorpay hosted checkout) | Paid webinars, expert review tripwire |
| `VIDEO_PORT` | YouTube (public reach), India-region streaming service for in-app | Captions/transcripts uploaded; no autoplay |
| `SPEECH_PORT` | Licensed TTS/ASR providers (English, Hindi; Indian languages later) incl. Jio/Sarvam/ElevenLabs-class vendors after evaluation (D-14) | Voice-over, captions draft, read-aloud, voice input |
| `TRANSLATION_PORT` | Claude API through the AI adapter; human reviewer | Hindi first |
| `SEARCH_ENGINE_PORT` | Google Search Console API, Bing Webmaster API, IndexNow | Sitemap submission, performance data |
| `ANALYTICS_PORT` | Self-hosted first-party analytics (India) | Consent-aware |
| `ESIGN_PORT` (P07) | ESPs (D-20) | Testimonial consents, NDA for trust documents |
| `ACADEMY_PORT` (P21) | trainings.lawdocs.in | Course cards, completions (with consent) |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `web.locale.hi.enabled` | G | true for glossary/health check; false elsewhere until reviewed | — | plt_content_publisher |
| `web.hc.families_enabled` | G | 12 launch families | subset of P15 families with a published bank | plt_content_publisher |
| `web.hc.min_questions` | G | 40 | 30–60 | plt_content_checker |
| `web.hc.bands` | G | 85/70/50 | ascending, 0–100 | plt_content_checker (maker ≠ checker) |
| `web.hc.critical_cap_count` | G | 3 | 1–10 | plt_content_checker |
| `web.hc.peer_benchmark.enabled` | G | OFF | requires k ≥ 30 per family | plt_super_admin + plt_content_checker |
| `web.hc.peer_benchmark.k_min` | L | 30 | — | — |
| `web.hc.retention_days` | G | 365 | 90–730 | plt_super_admin (DPO consulted) |
| `web.hc.share_link_expiry_days` | G | 90 | 1–365 | plt_content_publisher |
| `web.hc.narrative_ai.enabled` | G | ON | — | plt_super_admin |
| `web.hc.lookup.rate_limit_per_ip_hour` | G | 5 | 1–50 | plt_security_officer |
| `web.hc.email_gate_position` | G | AFTER_SEGMENT_1 | {AFTER_SEGMENT_1, AT_RESULT_PDF} (never at entry) | plt_content_publisher |
| `web.reg_updates.public_delay_minutes` | G | 0 | 0–10,080 | plt_content_publisher |
| `web.claims.default_expiry_days` | G | 365 | 30–730 | plt_content_checker |
| `web.claims.prohibited_phrases` | L | list in FR-P23-33 | append-only via release | — |
| `web.authors.advocate_bio_mode` | L | RULE36_FIELDS_ONLY | — | — |
| `web.robots.ai_training_crawlers` | G | ALLOW_PUBLIC_MARKETING | {ALLOW_PUBLIC_MARKETING, DISALLOW_ALL} | plt_super_admin (owner decision) |
| `web.robots.ai_search_crawlers` | G | ALLOW | {ALLOW, DISALLOW} | plt_super_admin |
| `web.experiments.enabled` | G | ON | never on legal/pricing amounts (L guard) | plt_content_publisher |
| `web.cookies.marketing_pixels.enabled` | G | OFF until consent banner live | — | plt_super_admin |
| `web.funnel.dark_pattern_audit_required` | L | true | — | — |
| `hlp.term.inline_default_for_new_users_days` | T (tenant) | 14 | 0–90 | ten_admin |
| `hlp.tours.enabled` | T | ON | — | ten_admin |
| `hlp.whats_new.max_per_session` | G | 1 | 0–3 | plt_content_publisher |
| `hlp.tutorials.diff_threshold` | G | 0.02 | 0.005–0.1 | plt_content_checker |
| `hlp.learning.per_user_reporting` | T | OFF | requires user notice (NN-25) | ten_admin |
| `hlp.a11y.grievance_ack_hours` | G | 24 (working) | 4–48 | plt_super_admin |
| `hlp.a11y.grievance_resolve_days` | G | 15 (working) | 5–30 | plt_super_admin |
| `hlp.a11y.release_gate` | L | ON | — | — |
| `user.a11y.*` (text_scale, spacing, font, theme, motion, captions, shortcuts, inline_terms, simplified_layout, read_aloud) | T (user) | system defaults | per FR-P23-129 | each user |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `web.markets.enabled` | G | IN | IN, AE, SG, UK, EU, US | `plt_web_publisher` + checker |
| `web.locale.ar.enabled` | G | false | requires reviewed copy and GCC cell | `plt_web_publisher` |
| `web.locale.en_gb.enabled`, `web.locale.en_us.enabled` | G | false | — | `plt_web_publisher` |
| `web.hc.global.enabled` | G | false until one Global Pack is PUBLISHED | — | `plt_web_publisher` |
| `hlp.hindi.maker_checker.enabled` | G | true after review | — | `plt_content_publisher` |
| `hlp.tours.first_visit` | T | on | — | `ten_admin` (per user override) |
| `web.hc.studio.max_questions` *(v1.2)* | G | 50 | 10–80 | super admin |
| `web.hc.studio.max_minutes_warning` *(v1.2)* | G | 12 | 5–20 | super admin |
| `web.hc.studio.wording_max_words` *(v1.2)* | G | 35 | 20–50 | content lead |
| `web.hc.studio.publish_requires_checker` *(v1.2)* | L | true | — (NN-05) | — |
| `web.hc.studio.ab_min_sessions_per_arm` *(v1.2)* | G | 300 | 100–5,000 | super admin |
| `web.hc.studio.dropoff_alert_pct` *(v1.2)* | G | 8 % per question | 3–25 % | super admin |
| `web.hc.studio.analytics_min_cohort` *(v1.2)* | L | 30 | — | — |
| `web.hc.baseline.prefill_on_conversion` *(v1.2)* | G | ON | ON/OFF | super admin |
| `web.hc.baseline.states` *(v1.2)* | L | self-declared states only (FR-P23-207) | — | — |

---

**Settings keys added in v1.3** *(v1.3; IPB tier in brackets; full definitions in Appendix U §U.15)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `brand.app_name` | G [PLATFORM; tenant/white-label override in `brand_pack`] | LawDocsComply | 2–40 chars; claims-lint | plt_super_admin (maker-checker) |
| `brand.tokens.*` | G [PLATFORM/ORG] | IPB-D-11 LDC values (`#0F4C3A`, `#C9A227`, IBM Plex) | contrast guard-rails | plt_super_admin; tenant `ten_admin` within guard-rails |
| `brand.hosts` | G [PLATFORM] | lawdocscomply.com, app., console. | verified hosts only | plt_super_admin (maker-checker) |
| `brand.social` | G [PLATFORM] | empty | https URLs on allow-listed platforms | plt_content_publisher |
| `brand.terminology.vidhi` | G [ORG, white-label plans only] | Vidhi | 2–24 chars | ten_admin (white-label) |
| `web.investors.enabled` | L → G after owner decision #29 | OFF | — | plt_super_admin + plt_legal_reviewer |
| `web.blog.enabled` | G | ON | — | plt_content_publisher |
| `web.blog.user_posts.enabled` | G | OFF | — | plt_super_admin + plt_content_checker |
| `web.blog.user_posts.moderation_sla_days` | G | 5 | 1–15 | plt_content_checker |
| `web.blog.user_posts.eligible_groups` | G | [] | tenant_authors, verified_practitioners, invited | plt_super_admin |
| `web.blog.bulk_import.max_files` | G | 200 | 1–500 | plt_super_admin |
| `web.vlog.enabled` | G | OFF | requires captions on every item | plt_content_publisher |
| `web.resources.gate_default` | G | none | none, email_gate, login | plt_content_publisher |
| `web.resources.max_file_mb` | G | 100 | 1–250 | plt_security_officer |
| `web.resources.review_cadence_months` | G | 12 | 3–24 | plt_content_checker |
| `web.media.svg_mode` | L | rasterise | rasterise, sanitise_strict | — |
| `web.embeds.allowlist` | L | [youtube-nocookie, vimeo, static maps] | — | plt_security_officer (ADR) |
| `fb.widget.enabled` | G [USER view] | ON | — | plt_super_admin |
| `fb.ideas.enabled` | G | ON | — | ten_admin (tenant), plt_super_admin (public) |
| `fb.screenshot.enabled` | G | ON (user-initiated, blur offered) | — | ten_admin |
| `mkt.tag_manager.adapter` | G | none | none, gtm_web, server_side | plt_super_admin + plt_dpo (owner decision #30) |
| `mkt.sensitive_routes` | L | health-check answers, grievance, legal forms, all authenticated apps | — | — |
| `mkt.utm.capture` | G | ON (cookieless) | — | plt_super_admin |
| `msg.whatsapp.enabled` | G | OFF | — | plt_super_admin |
| `pol.notice_days` | G | 30 | 30–90 | plt_legal_reviewer |
| `pol.full_hindi` | G | false | — | plt_legal_reviewer (owner) |
| `pol.dpa_clickwrap` | G | true | — | plt_legal_reviewer |
| `pol.refund.rule` / `pol.refund.window_days` | G (per plan) | full_within_window / 7 | — | plt_legal_reviewer |
| `pol.dispute.odr_mandatory` / `pol.dispute.arbitration` | G | false / true (B2B) | — | plt_legal_reviewer [COUNSEL] |
| `a11y.text.font` | T [USER] | default | default, opendyslexic, atkinson | self |
| `a11y.captions.required` | L | true | — | — |
| `a11y.gov_facing` | G | OFF | — | ten_admin |
| `hlp.lint.enforce` | L | true | — | — |
| `tut.whats_new.level` | G [ORG] | all | all, regulatory_only, none | ten_admin |

## 10. Security, privacy and audit

- **Data minimisation in the health check:** questions ask about practices, never about named individuals, customers, borrowers, complaints, health or financial account details; free-text fields are not offered in the questionnaire (only fixed answers and N/A reasons) to prevent accidental personal data. Contact data is collected only with notice and consent (FR-P23-48); PAN is transient and masked (NN-12).
- **Purpose limitation:** answers are used to compute the report and, only with consent (d), to brief the RM; aggregated, anonymised (k ≥ 30) scores may be used for benchmarks and published research — stated in the notice.
- **Retention and erasure:** §5.1; erasure propagates to the Hub; the audit ledger records the erasure event without the erased data.
- **Share links:** 128-bit tokens stored hashed; optional password; expiry; revocation; `noindex`, `X-Robots-Tag: noindex`; no organisation name in the URL.
- **Abuse controls:** rate limits on lookup, submission, email sending; accessible bot challenge with non-cognitive fallback (FR-P23-43); WAF rules; input validation; CSP with nonces; SRI on any third-party script; `Permissions-Policy` restricting camera/microphone except on the voice-input route after user action.
- **CMS security:** console behind SSO + phishing-resistant MFA (P01), role scopes `web`/`hlp`, maker ≠ checker, signed preview URLs, sanitisation of rich text (no inline script), asset malware scan (P07), audit ledger on every publish.
- **Claims and legal exposure:** NN-19 enforcement (§4D); testimonial consents; dark-pattern prohibitions (FR-P23-75); advertising and endorsement rules; trust-centre statements governed by the register.
- **Children:** the public site is not directed at children; health check and forms require a declaration that the user acts for an organisation; no age-gating data collected.
- **Audit events:** page/claim/term/tutorial transitions, health-check submissions (session id, model version, result hash), consents, lead deliveries, share-link creation/revocation, accessibility exceptions — all in the hash-chained ledger (NN-02).

---

## 11. AI touchpoints and guardrails

| Touchpoint | What AI does | Guardrails |
|---|---|---|
| Health-check narrative (FR-P23-59) | Drafts a 2-paragraph summary from computed scores and bank texts | Template prompt; inputs only; no compliance verdicts; label "AI-drafted"; deterministic fallback; logged with model/version (NN-14) |
| Glossary drafting | Drafts plain definitions and examples from the clause text | Legal definition is quoted from the library, never generated; regulatory reviewer approves (NN-04, NN-06) |
| Help articles and tutorial scripts | Drafts from release notes, screen registry and written steps | Technical writer approves; no customer data in prompts (demo tenant only) |
| Alt text and long descriptions | Drafts for screenshots and diagrams | Human reviewer; decorative vs informative decision by human |
| Captions and transcripts | ASR draft | Human correction to ≥ 99% accuracy before publish |
| Translation (Hindi first) | Drafts | Human reviewer fluent in the language; legal terms from a controlled bilingual termbase |
| "Ask Vidhi" help mode | Answers how-to questions from published help/glossary only, with links | Retrieval restricted to `hlp` published content; no regulatory advice in help mode; hands off to the full Vidhi (Appendix K) inside the tenant app |
| Regulatory update summaries | Drafts "what changed" from the source instrument | Platform reviewer compares with source; summary never stronger/weaker than source; published only via P05 workflow |
| SEO assistance | Suggests titles, descriptions, internal links | Editor accepts; no auto-generated pages (FR-P23-159) |

No AI output on the public site is published without human approval (NN-04). Prompts and outputs are logged under platform retention; no lead or tenant data is sent to a model provider unless the provider/region is recorded and approved (NN-15, NN-24).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p23/*.feature`)

```gherkin
Feature: Server-rendered public content
  Scenario: Crawlers see full content without JavaScript
    Given the public site is deployed
    When a client without JavaScript requests "/solutions/nbfc-compliance-software"
    Then the HTML contains exactly one h1
    And the main element contains at least 300 words
    And the response contains valid JSON-LD of types "SoftwareApplication" and "BreadcrumbList"

  Scenario: llms.txt is plain text
    When a client requests "/llms.txt"
    Then the content type is "text/plain; charset=utf-8"
    And the first line starts with "# LawDocsComply"

Feature: Free Compliance Health Check
  Scenario: NBFC Base Layer visitor completes the check and starts a trial
    Given an anonymous visitor selects family "NBFC" and type "NBFC-ICC" layer "Base Layer"
    And looks up the organisation by CIN and confirms the result
    When the visitor answers all applicable questions and gives report-delivery consent only
    Then a report is shown with an overall score, a band, a confidence indicator and ten segment scores
    And the report shows the disclaimer "Indicative self-assessment"
    And a "LeadCaptured" event is delivered to the Operations Hub within 60 seconds with marketing consent = false
    When the visitor clicks "Start your 7-day trial"
    Then the onboarding wizard opens at "Confirm your profile" with the family, type and organisation pre-filled

  Scenario: Critical gap caps the band
    Given a completed session where three weight-3 questions are answered "No"
    And the computed overall score is 88
    Then the displayed band is "Needs attention"
    And the three critical gaps are listed first

  Scenario: Reports are reproducible
    Given a report generated with bank version 1.0 and scoring model 1.0
    When scoring model 1.1 is published
    Then re-opening the old report shows the original score and model version 1.0

  Scenario: No personal data before consent
    Given a visitor on segment 1 who has not entered an email
    Then no lead record exists
    And no marketing pixel has loaded

  Scenario: Share link revocation
    Given a lead has created a share link
    When the lead revokes it
    Then requests to the link return 410 and no report data

Feature: Claims Register (NN-19)
  Scenario: Expired claim is removed automatically
    Given a published home page binding claim "obligations mapped" that expires today
    When the claim expiry job runs
    Then the home page is republished with the fallback text
    And the claim owner receives a notification

  Scenario: Prohibited phrase blocks publishing
    Given an editor writes "RBI-approved compliance software" in a hero block
    When the editor submits for review
    Then the pre-publish check fails with error "LDC-WEB-012"

Feature: "i" glossary
  Scenario: Every registered term on a screen has a published definition
    Given the release build of apps/web
    When the glossary coverage check runs
    Then every "i" key used in the build has status "PUBLISHED"

  Scenario: Popover is keyboard and screen-reader accessible
    Given a maker on the obligation register
    When the maker tabs to the "i" button beside "CRAR" and presses Enter
    Then a popover opens with the plain definition and a citation link
    And pressing Escape closes it and focus remains on the "i" button

Feature: Accessibility release gate (NN-21)
  Scenario: Serious violation blocks promotion
    Given a release candidate where axe reports a "serious" violation on a changed route
    When promotion to production is requested
    Then promotion is refused with reason "NN-21 accessibility gate"

  Scenario: Focus is never obscured
    Given the mobile public site with the sticky CTA bar visible
    When a keyboard user tabs through the pricing comparison table
    Then each focused element is fully visible in the viewport

  Scenario: Authentication without cognitive tests
    Given the sign-in page
    Then no CAPTCHA puzzle or character-transcription test is presented
    And pasting a 6-digit OTP into the first OTP field fills all fields

Feature: Tutorials
  Scenario: Tutorial marked stale after UI change
    Given a published tutorial for "Checker: approve evidence"
    When a release changes the review screen beyond the diff threshold
    Then the tutorial status becomes "STALE" and shows the earlier-version notice

  Scenario: Tutorial capture refuses non-demo tenants
    Given a capture script configured with a customer tenant id
    When the capture run starts
    Then it fails with error "LDC-HLP-004"
```

NN tests owned by this phase: `NN-19_claims_block_publish`, `NN-19_prohibited_phrases`, `NN-19_hc_disclaimer_present`, `NN-21_axe_gate`, `NN-21_contrast_tokens`, `NN-21_focus_not_obscured`, `NN-21_pdfua_templates`, `NN-12_hc_pan_masked_not_stored`, `NN-22_hc_score_reproducible`, `NN-04_ai_content_requires_approval_web`, `NN-15_no_lead_data_to_unapproved_provider`.

```gherkin
Feature: v1.1 — global site, global health check, new pages

  Scenario: No country page without a published pack
    Given the UAE pack is PILOT and the Singapore pack is DRAFT
    Then /ae/solutions/uae-compliance shows "Pilot — coverage being completed"
    And no Singapore country page exists

  Scenario: Generic group check is labelled
    Given a visitor checks a Kenyan subsidiary and no Kenya pack is PUBLISHED
    Then the report states "generic group check — local rules not yet reviewed"

  Scenario: Locale pages are server-rendered
    When a crawler without JavaScript fetches /uk/solutions/
    Then the primary content is present in the HTML

  Scenario: Inline regulatory help
    When a maker opens the "i" panel on a checkpoint
    Then the clause text, plain-language explainer and evidence expectation appear without navigation

Feature: Health Check Studio (v1.2)
  Scenario: Super admin builds a set by CompID
    Given the super admin opens the Studio for the NBFC family
    When she filters the library by instrument "Compliance Function Directions 2026" and department "Compliance"
    And binds RBI-NBFC-CMPF26-0001 to RBI-NBFC-CMPF26-0004 to one plain-language question in section "Compliance function"
    Then the item shows four bound CompIDs with RBI-NBFC-CMPF26-0001 as primary and a citation built from them

  Scenario: Section weights must total 100
    Given a draft set whose section weights total 95
    When the maker submits it
    Then submission is blocked with LDC-WEB-041

  Scenario: Branching hides deposit questions
    Given a sample entity "NBFC Middle Layer, non-deposit-taking"
    When the maker previews the set
    Then no deposit question is shown and the applicable count and time estimate are displayed

  Scenario: Maker cannot publish own set
    Given a set version submitted by user A
    When user A tries to approve it
    Then the action is refused (NN-05)

  Scenario: Retired CompID flags the set
    Given a published set binding RBI-NBFC-GOV25-0020
    When RBI-NBFC-GOV25-0020 is split and retired
    Then the set is flagged "needs review" with the successor CompIDs shown
    And a new version cannot be published until the binding is resolved (LDC-WEB-046)

  Scenario: Placeholder resolves when the sheet is published
    Given item HC-GOV-01 is bound to LPH-MCA-CO-CA13-0001
    When the Companies Act board-meeting rows are published as MCA-CO-CA13-0101 and MCA-CO-CA13-0102
    And the content maker links the placeholder to them
    Then the draft set binds the two CompIDs and the placeholder becomes an alias of MCA-CO-CA13-0101

  Scenario: Answers pre-fill the baseline without marking compliance
    Given a visitor answered "Partly" to the item bound to RBI-NBFC-CMPF26-0001
    When the visitor starts a trial from the report
    Then the tenant baseline shows RBI-NBFC-CMPF26-0001 as "Self-declared partial" from the Health Check
    And no compliance instance is marked Compliant and no Date of Compliance is filled

  Scenario: Reports keep the Health Check Score label
    When any report, preview or experiment result is rendered
    Then the score is labelled "Health Check Score" and never "Compliance Score"
```

---

```gherkin
# v1.3 — IPB-04/05/06/07 adoption (P23-AT-29 … P23-AT-40)
Feature: Brand pack and host safety (P23-AT-29)
  Scenario: A failing contrast pair cannot publish
    Given a brand-pack draft with --color-primary "#7FA38F" on --color-on-primary "#FFFFFF"
    When the editor saves
    Then the response is LDC-WEB-053 with the measured ratio and a suggested passing shade
    And the version state stays DRAFT
  Scenario: Unknown Host header is refused
    Given published hosts "lawdocscomply.com" and "app.lawdocscomply.com"
    When a request arrives with Host "evil.example"
    Then the response is a static 421 page and an LDC-WEB-054 log line with the host
    And no redirect, canonical or cookie uses the unknown host

Feature: Standard pages and footer (P23-AT-30)
  Scenario: Footer carries officers, entity line and social links
    Given the public home page
    Then the footer shows the Grievance Officer and DPO names with emails
    And the legal entity name, CIN, GSTIN and registered office
    And every brand_pack.social URL as a labelled link
    And the Organization JSON-LD sameAs array equals the social URL list

Feature: Team photos need consent (P23-AT-31)
  Scenario: Publish blocked without photo consent
    Given a team_member with a photo and photo_consent = false
    When the Team page is published
    Then the response is LDC-WEB-055 naming the member

Feature: Investors toggle and disclaimer (P23-AT-32)
  Scenario: Page hidden by default
    Given web.investors.enabled = OFF
    Then /investors returns 404 with the standard not-found page and is absent from sitemap and footer
  Scenario: Forward-looking wording fails lint
    Given web.investors.enabled = ON and a draft containing "projected ARR"
    When submitted for publish
    Then the response is LDC-WEB-056 and the legal-review queue shows the item
  Scenario: Disclaimer block is locked
    When an editor tries to edit the disclaimer block text
    Then the editor is read-only and shows "Locked copy — Appendix AD §AD.19"

Feature: Blog toggle, bulk import and user posts (P23-AT-33)
  Scenario: Blog OFF serves 410 and keeps data
    Given 40 published posts and web.blog.enabled set to OFF
    Then /blog/<slug> returns 410 with a link to /resources, the sitemap omits posts and no row is deleted
    When web.blog.enabled is set to ON
    Then every post is served at its original URL with original dates
  Scenario: Bulk import previews and never auto-publishes
    Given a zip of 25 .docx files including one with a macro and one with an existing slug
    When imported
    Then the macro file is rejected with reason, the duplicate shows a diff, 23 items are DRAFT after acceptance
    And no item is PUBLISHED and the job shows undo_until 24 hours ahead
  Scenario: User post is pre-moderated and labelled
    Given web.blog.user_posts.enabled = ON and a submitted user post
    Then the URL is not routable until moderation_state = APPROVED
    And on publish the page shows "Author's view — not advice", the author profile and the UGC Terms version
    And in.infrabyx.cms.BlogPostPublished.v1 is emitted with author_type "user"
  Scenario: Script in a user post is stripped
    Given a user post body containing "<script>" and an iframe
    When saved
    Then the stored blocks contain neither and the editor shows LDC-WEB-059

Feature: Vlog captions (P23-AT-34)
  Scenario: Video without captions cannot publish
    Given a vlog item with a video and no WebVTT file
    When published
    Then the response is LDC-WEB-057

Feature: Resources (P23-AT-35)
  Scenario: Quarantine on failed scan
    Given a resource upload whose declared type is PDF but whose bytes are an executable
    Then the version state is QUARANTINED and the file is never served
  Scenario: Gated download records consent
    Given a resource with gate = email_gate
    When a visitor submits the gate form with the marketing box unticked
    Then the download link is emailed, the ledger records consent.resource_gate v1 and no marketing consent

Feature: Policy pages (P23-AT-36)
  Scenario: Unresolved parameter blocks publish
    Given the Privacy Notice instance with {{dpo_email}} unset
    When published
    Then the response is LDC-WEB-060 citing IPB-POL-001
  Scenario: MAJOR Terms change respects notice and re-consent
    Given Terms v2.0 approved on 1 Feb with effective_at 10 Feb
    Then the response is LDC-WEB-060 citing IPB-POL-005
    Given effective_at 3 Mar
    Then account owners receive notice.policy.change, a banner shows until 3 Mar, and a user who refuses on 4 Mar is in read-only mode with export and AcceptanceRefused is emitted
  Scenario: Stale citation detected
    Given a Retention Schedule draft citing the 2017 NBFC outsourcing directions
    When submitted
    Then LAW_REGISTER_PORT (Appendix G) marks the instrument superseded and the response is LDC-WEB-060 citing IPB-POL-004

Feature: Feedback and ideas (P23-AT-37)
  Scenario: Screenshot never captures form values
    Given a user on a form with a typed PAN
    When they submit feedback with a screenshot
    Then the capture is user-initiated, the PAN field is blurred by default and no form value is in the payload
  Scenario: Feedback reaches the Hub
    When a tenant user submits a bug
    Then in.infrabyx.feedback.FeedbackSubmitted.v1 is emitted without any sealed data and the item shows in Settings › Feedback with status

Feature: Tags fire only after consent (P23-AT-38; NN-62)
  Scenario: No third-party request before consent
    Given mkt.tag_manager.adapter = gtm_web and a first visit to /pricing
    When the page loads and the banner is shown
    Then the network log contains first-party requests only
    When the visitor rejects all
    Then no tag fires for the session and the choice is honoured on every page
  Scenario: Authenticated routes never fire tags
    Given a logged-in user with analytics consent granted on the public site
    When they open app.lawdocscomply.com
    Then no tag-manager or pixel request is made

Feature: Captions and dyslexia font (P23-AT-39; IPB-06)
  Scenario: Tutorial without transcript fails CI
    Given a tutorial video asset without a transcript
    When the accessibility CI job runs
    Then the build fails naming the asset
  Scenario: Font preference applies across apps
    Given a user sets a11y.text.font = opendyslexic in Settings › Accessibility
    When they open the public help centre
    Then body and heading fonts are OpenDyslexic (self-hosted) and the preference cookie is in the necessary category

Feature: "i" registry lint (P23-AT-40; IPB-07)
  Scenario: Unregistered glossary term fails the build
    Given a screen that renders the term "Net Owned Fund" tagged glossary without a key hlp.cmp.net_owned_fund
    When CI runs
    Then the build fails with the missing key
  Scenario: LAW-cited entry needs a reviewer
    Given an "i" entry citing RBI SBR Directions without reviewer_of_record
    Then the entry cannot publish until plt_legal_reviewer records a review
```

## 13. Deliverables and exit gate

1. `apps/public` with all page types, server-rendered, on the CDN, with the legacy redirect map applied.
2. `web` and `hlp` modules with console screens (SCR-WEB-30…35, SCR-HLP-10…15), APIs, events and jobs.
3. Health check live for 12 families with published banks and scoring model v1.0 (Appendix P §P.3), PDF and share links, Hub hand-off, trial pre-fill.
4. Claims Register populated for every live claim; prohibited-phrase lint.
5. Glossary ≥ 400 published terms (first 152 per Appendix P §P.4 reviewed by a regulatory reviewer), coverage check = 100%.
6. Help centre with ≥ 120 articles mapped to help keys; help panel on every shipped screen.
7. ≥ 40 tutorial videos with corrected captions, transcripts and quick cards; ISL renditions for the 12 getting-started videos; social derivatives handed to the Hub.
8. Accessibility: token corrections merged; component contract; preferences page; CI gates; manual AT matrix signed; independent IAAP audit report; ACR (VPAT 2.5 INT + IS 17802 map) and Accessibility Statement published; grievance channel live.
9. SEO/GEO: structured data per page type, sitemaps, robots/AI-crawler policy approved by the owner, llms.txt, Search Console/Bing verified, AI answer panel baseline recorded.
10. Trust Centre and security.txt.
11. Documentation: `docs/phases/P23-plan.md`, content style guide, accessibility playbook, tutorial production guide, health-check methodology note (public).
12. *(v1.2)* Health Check Studio (SCR-WEB-50–55) live with maker-checker publish, preview, test harness, A/B experiments and drop-off analytics; `HC-SET-0001` and `HC-SET-0002` seeded with the Appendix P §P.11 bindings; baseline pre-fill by CompID accepted by P04.

**Exit gate:** all §12 scenarios and NN tests green; Core Web Vitals and Lighthouse budgets met; no serious/critical accessibility defects open; owner sign-off on health-check methodology, band texts and disclaimer; DPO sign-off on the health-check notice and retention; claims reviewed by the Company Secretary.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P23-01 | Draft RPwD (Amendment) Rules 2026 (S.O. 3962(E)) final notification, ACR format and deadlines | Draft as of 25 Oct 2026 | DPO / CTO | Build ACR now (VPAT + IS 17802 map); track as obligation in `LDC_GROUP` |
| OI-P23-02 | SEBI digital-accessibility circular 31 Jul 2025 / 29 Aug 2025 exact number, paras and current deadlines | Taken from secondary source | Content team | Pack content marked [VERIFY]; dates not shown publicly until verified |
| OI-P23-03 | IS 17802 Part 1 clause-to-WCAG 2.2 mapping (IS 17802 tracks WCAG 2.1/EN 301 549) | Standard text purchase/review needed | Accessibility specialist | Treat WCAG 2.2 AA as superset; record IS 17802 clauses as [VERIFY] in ACR |
| OI-P23-04 | Company-data provider terms for lead-flow lookups and PAN verification in an anonymous flow | Vendor contract | CTO / counsel | `web.hc.lookup.enabled` OFF → manual entry only |
| OI-P23-05 | CCPA applicability to LDC (thresholds) and GDPR Art. 27 representative need for EU visitors | Depends on volumes and targeting | DPO / counsel | Serve GDPR/CCPA-style notices to self-declared EU/UK/US visitors; no EU targeting campaigns until decided |
| OI-P23-06 | CCPA (India) Dark Patterns Guidelines 2023 — any 2025–26 amendments/advisories (self-audit) | Re-check source | Counsel | Apply 13-pattern checklist |
| OI-P23-07 | BCI r.36 website content, ICAI/ICSI rules on member bios and articles | Counsel opinion | General counsel | `web.authors.advocate_bio_mode` Locked to Rule-36 fields |
| OI-P23-08 | Owner decision on AI training crawlers (`GPTBot`, `Google-Extended`, `CCBot`) | Business choice | Owner | Default ALLOW_PUBLIC_MARKETING |
| OI-P23-09 | Current lawdocscomply.com page content and pricing (site not readable without JS on 25 Oct 2026) | Fetch returned SPA shell | Owner / growth squad | Export current copy from the existing repo in P00; preserve slugs |
| OI-P23-10 | Company identity particulars for footer/legal pages (legal entity operating LDC, CIN, GSTIN, registered office, DPO, grievance officer) | Not provided | Company Secretary | Placeholders block publishing of legal pages |
| OI-P23-11 | ISL interpreter sourcing and cost for priority videos | Vendor | Content lead | Captions + transcripts mandatory; ISL for 12 videos as target |
| OI-P23-12 | IAAP-certified auditor engagement | Vendor | CTO | Internal audit by in-house specialist; external before ACR v1.0 publication |
| OI-P23-13 | Whether first-party cookieless analytics can run before consent under DPDP Rules 2025 | Interpretation | DPO | Default: no analytics identifiers before consent |
| OI-P23-14 | Grievance Officer obligation for LDC under IT Rules 2021 (is LDC an intermediary for user content?) | Interpretation | Counsel | Publish a grievance officer page anyway (also needed under DPDP and consumer law) |
| OI-P23-15 | Penalty library values used in health-check "why it matters" texts | Each must be cited and current | Regulatory reviewer | Show citation only (no amount) where unverified |

**Open items added in v1.1** *(v1.1)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P23-21 | Arabic copy deck and RTL accessibility testing | Needs GCC cell and translator | Marketing | `web.locale.ar.enabled = OFF` |
| OI-P23-22 | Foreign registry look-up terms for anonymous lead flow | Provider terms | CTO | Manual entry |
| OI-P23-23 | Market-specific advertising and comparison-claim rules (UK ASA, EU UCPD, UAE) | Counsel | Marketing | India copy only abroad, no comparisons |

**Open items added in v1.2** *(v1.2)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P23-31 | Final CompIDs for the bank bindings | Most question sheets are not yet published; only the nine NBFC DoS sheets exist in draft | Content lead | Placeholder IDs (`LPH-…`) per Appendix P §P.11; resolution tracked on SCR-WEB-50 |
| OI-P23-32 | Whether the in-app pulse check may use a different set from the public check | Product choice | Product owner | Same set per family; channel `IN_APP` allowed but OFF |
| OI-P23-33 | A/B testing of a regulatory self-assessment and consumer-protection rules on dark patterns | Counsel review of experiment designs | Counsel | Only wording, order and length are tested; never scoring of a live report |
| OI-P23-34 | *(v1.3)* Investors page: publish for LDC; gated documents; disclaimer wording under Companies Act 2013 s.42, s.23, s.26 and SEBI ICDR 2018 | Owner decision #29; counsel | Board / counsel | `web.investors.enabled` OFF; locked disclaimer from Appendix AD §AD.19 |
| OI-P23-35 | *(v1.3)* User-post programme: eligible author groups, moderation roster, BCI Rule 36 screening owner for advocate authors | Owner decision #30 | Owner / content lead | `web.blog.user_posts.enabled` OFF |
| OI-P23-36 | *(v1.3)* Tag management choice (none / GTM web / server-side) and the consent-category mapping | Owner decision #30; DPO | Owner / DPO | `mkt.tag_manager.adapter = none` |
| OI-P23-37 | *(v1.3)* IT Rules 2021 synthetic-media labelling amendment (notified 10 Feb 2026, effective 20 Feb 2026 per IPB research) — rule numbering and the 3-hour takedown clock for UGC | [VERIFY] | plt_legal_reviewer | Label every AI-assisted or synthetic asset; apply 3-hour clock voluntarily |
| OI-P23-38 | *(v1.3)* Dyslexia font licences (OpenDyslexic — SIL OFL; Atkinson Hyperlegible — licence terms) and self-hosting rights | [VERIFY] | Accessibility specialist | Offer OpenDyslexic only until verified |


---

## 15. Sources (accessed 25 October 2026)

Primary and official
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2, W3C Recommendation (5 Oct 2023; updated 12 Dec 2024) — https://www.w3.org/TR/WCAG22/
- Rights of Persons with Disabilities Act, 2016 (ss. 40, 42, 46, 89) and RPwD Rules, 2017 r.15 — https://www.indiacode.nic.in/ (Act No. 49 of 2016) [VERIFY link]
- Draft RPwD (Amendment) Rules, 2026, S.O. 3962(E), 16 Jul 2026 — summarised at https://www.indialaw.in/blog/regulatory/rpwd-amendment-rules-2026/pdf/ [VERIFY against Gazette]
- *Rajive Raturi v Union of India*, Supreme Court, 8 Nov 2024; *Pragya Prasun v Union of India*, Supreme Court, 30 Apr 2025 — summarised at https://www.azbpartners.com/bank/bridging-the-digital-divide-indias-evolving-accessibility-framework/
- SEBI circular on digital accessibility for regulated entities, 31 Jul 2025 (revised 29 Aug 2025) — summarised at https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/ [VERIFY on sebi.gov.in]
- Guidelines for Indian Government Websites and Apps (GIGW 3.0) — https://guidelines.india.gov.in/
- Bureau of Indian Standards, IS 17802 (Part 1): 2021 and (Part 2): 2022 — Accessibility for the ICT products and services [VERIFY]
- Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E), 13 Nov 2025) — https://www.meity.gov.in/
- Central Consumer Protection Authority, Guidelines for Prevention and Regulation of Dark Patterns, 2023 (30 Nov 2023) [VERIFY]
- Bar Council of India Rules, Part VI, Chapter II, Section IV, r.36 (as amended) [VERIFY]
- RFC 9116, A File Format to Aid in Security Vulnerability Disclosure (security.txt) — https://www.rfc-editor.org/rfc/rfc9116
- schema.org types `Legislation`, `DefinedTerm`, `SoftwareApplication`, `Service`, `Course`, `VideoObject` — https://schema.org/

Secondary (benchmarks and practice)
- Search Engine Journal, "Google drops FAQ rich results" (2026) — https://www.searchenginejournal.com/google-drops-faq-rich-results/574429/
- Pepper, "How to optimise for AI search results in 2026" (vendor guide; indicative) — https://www.pepper.inc/blog/how-to-optimize-for-ai-search-results-in-2026-the-complete-guide-to-ai-search-optimisation/
- Aparajitha llms.txt (example structure) — https://www.aparajitha.com/llms.txt ; TeamLease RegTech llms-full.md — https://teamleaseregtech.com/llms-full.md
- PTSTDM VSL funnel page (owner reference) — https://ptstdm.co.in/vsl-yt-v2/
- Dupple, "Interactive lead magnet examples 2026" — https://dupple.com/learn/interactive-lead-magnet-examples
- Competitive sources: Appendix R §R.14.

---

## 16. Master integration notes (pack lead, v1.1 and v1.2, 25 October 2026)

**From v1.0 integration:** NN-44; X-07 (no bureau pulls in the health check), X-18, X-20 (corrected tokens), X-21, X-22, X-39 (Hindi), X-40 (AI-crawler default).

**Added in v1.1:** NN-54; X-46.

**Added in v1.2:** D-55; NN-56 (Health Check Studio selects library questions by CompID; `LPH-` placeholders until sheets publish; Appendix P §P.11).

**Added in v1.3:** D-66, D-71–D-74, D-76; NN-62–NN-64; X-67 (IPB precedence), X-69 (CMS stays in schema `web`); IPB-04 (Brand Studio, standard pages, footer, blog/vlog/resources, feedback, marketing tooling), IPB-05 (policy set from Appendix AD), IPB-06 (captions, dyslexia font, `gov_facing`), IPB-07 ("i" registry format and lint). The Health Check Studio, Claims Register and Health Check funnel are referenced by the IPB as the ecosystem pattern and are unchanged. Copy for every standard page is in `content/LawDocsComply_Website_Content_v1.0.md`; visual rules in `design/UI_UX_Design_Brief_v1.3.md`.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
