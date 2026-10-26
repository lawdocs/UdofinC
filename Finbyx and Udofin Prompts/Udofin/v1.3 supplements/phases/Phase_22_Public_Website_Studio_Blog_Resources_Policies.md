# Phase 22 — Public Website, Super-Admin Studio, Blog, Resources and Policies

**Udofin Master Prompt v1.3 · Part 7I IB2 (with IB4, IB5.4, IB6) · 26 October 2026 · Product code UDF**

**Binding files:** Udofin Master Prompt v1.3 (Part 7I IB2, IB4, IB5, IB6, IB9; Part 10.4; Part 7C UB4; Part 7G RV4; Part 7H RA4.4; Appendix G); IPB-04 (Public Website and Super-Admin Studio) in full; IPB-05 (Legal Policy Templates); IPB-06 (Accessibility); IPB-07 ("i" registry, tours, tutorials, What's new); IPB-08 (public Trust Centre); IPB-02 (uploads, SSRF, CSP); IPB-10 (events). Content: `docs/content/Udofin_Website_Content_v1.0.md`. Design: `docs/design/UI_UX_Design_Brief_v1.3.md`. Help seed: `docs/help/i_registry_seed_terms_v1.3.md`. Precedence: master prompt → IPB → Ecosystem Spec → this file → appendices; Part 8A prevails on regulatory points.

**Branch:** `cc/p22-public-site` · **Depends on:** 1 (tokens), 3 (catalogue), 3c (DLA register), 14b (help centre), 16c (release notes); may start after Phase 3 with placeholders · **Position in order:** after 17, before P (pilot prerequisite).

---

## 1. Purpose and scope

Udofin's public website is a regulated disclosure surface as much as a marketing one. The NBFC Credit Facilities Directions, 2025 require the LSP and its partner REs to publish the partner list and DLA details, the grievance officer, the privacy and storage policy, the ranking metric and the monthly DLG disclosure (CF paras 9(4)–(5), 12(2), 14(2), 15, 18, 28 [VERIFY]). The site therefore goes live before the pilot (Phase P), and every claim on it is evidenced, dated and reviewable.

This phase builds `apps/public` on the shared `packages/cms` (IPB-04), the super-admin Studio in `apps/console` (channel F), the blog with verified-educator posts, the Resources library, the eighteen IPB-05 legal pages as Udofin instances, the cookie CMP, the binding footer, the Claims Register publish gate, the feedback widget, tours and tutorials, What's new, the app-store listing copy as a gated CMS item, the completion of the "i" registry in 12 locales (IB4), the public Trust Centre and accessibility statement (IB5.4, IB6), and the Brand Studio and Pricing Studio for the default Udofin pack. White-label packs are Phase 23; this phase makes `apps/public` host-aware so that Phase 23 adds packs without changing the renderer.

**Tone.** Consumer-friendly, calm, trustworthy, low-literacy-aware: short sentences, one idea per paragraph, reading age 12, icons always labelled, no urgency, no "instant", no "guaranteed", no superlatives. Udofin is named as a Lending Service Provider on every page; the lender decides.

**Out of scope.** Advertising (RV4; S10 gate), consumer plan purchase (RV2; S09 gate), Investors documents beyond the toggle and template (owner decision 47), white-label packs (Phase 23).

## 2. Functional requirements

### 2.1 Site, pages and rendering

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-01 | `apps/public` (Next.js 16, App Router, ISR with tag revalidation) renders every page from `cms` items through the IPB-04 templates; no page content is hard-coded except the error pages and the health route. | M | AT-22-01 |
| FR-22-02 | The page set of master prompt IB2.1 exists from day one: Home, How it works, Lenders, Products, Safety & your data, Pricing, Resources, Blog, About, Team, Leadership, Governance, Investors (toggle), Careers, Press, Partners, Contact, Documentation, Help, Changelog, Status (external link), Trust Centre, Accessibility statement, Grievance, Legal (18 instances), Sitemap. Toggled pages are hidden by setting and return 404, never 500. | M | AT-22-02 |
| FR-22-03 | **Lenders page and footer partner list** render only from the DLA register and `ProductCatalogPublished` (registered RE name, RE type, RBI registration reference, RE website disclosure link, GRO name and contacts, DLAs on which the RE is present); the CMS may add a plain description per RE after legal review; alphabetical order; equal logo size; no "featured". An RE whose deal is `SUSPENDED` or `TERMINATED` disappears within the cache TTL (≤ 15 minutes) and the change is logged for the CF para 18(2) notice. | M | AT-22-03 |
| FR-22-04 | **Safety & your data** page contains the required blocks: Udofin's LSP role; the lender decides; what Udofin never accesses on the phone (contacts, SMS, call logs, files, installed apps) and what it may access (camera at KYC, approximate location once); data stays in India; KFS sample (resource); cooling-off explained; how to complain and the escalation path (RE GRO → Internal Ombudsman where applicable → RBI Ombudsman within 90 days); how to verify the app (store links, package id, checksum, CIMS list link); RBI Sachet; the "Is this loan app safe?" health check (IB9). Publish blocks if any required block is empty. | M | AT-22-04 |
| FR-22-05 | **Products** page shows loan types neutrally (what the product is, who typically uses it, what the lender will ask for) with no rates, no "from X%", no lender names; "Offers come from lenders; Udofin shows them side by side". | M | AT-22-05 |
| FR-22-06 | **Pricing** page: "Free for borrowers, always. Udofin never charges you for a loan" (CF para 10(4)) with the "i"; RE plan names from the Pricing Studio mirror with "Lender pricing is available after login" (IPB-DEV-05); S09 consumer plans section hidden until `ACTIVE`. | M | AT-22-06 |
| FR-22-07 | **How it works**: four steps (Tell us what you need → Lenders check and make offers → Read the KFS, accept, sign → Repay the lender), each with the explain-why "i" and the statement that the lender decides at steps 2–3. | M | AT-22-07 |
| FR-22-08 | **Documentation** links the RE and partner API portal (`web.docs.url`), the help centre, the API status page and the changelog; the external portal shares the brand pack and CMP. | S | AT-22-08 |
| FR-22-09 | **Investors** page exists behind `web.investors.enabled` (default false); when enabled it requires the locked disclaimer block, legal review on every publish, E2+ evidence on every number, and refuses the words "guarantee", "assured return", "will achieve", "projected" (IPB-04-66) [COUNSEL]. | M | AT-22-09 |
| FR-22-10 | **Careers**, **Contact**, **Partners** forms post server-side to the Operations Hub through `HR_PORT` and `CRM_PORT` with the consent text version and ledger receipt; the CMS stores only submission ids; Contact lists the Delhi, Noida and Jaipur offices as CMS-managed address blocks with click-to-load static maps. | M | AT-22-10 |
| FR-22-11 | **Grievance** page (IT Rules 2021 r.3(2)): Udofin nodal grievance officer name, designation, email, postal address, hours, the form (→ OH6 `grievance` destination for non-loan matters; loan complaints are routed to the in-app UB3 flow with a login prompt), and the escalation path. | M | AT-22-11 |
| FR-22-12 | **Footer** (IB2.6): legal entity and CIN; LSP statement; partner-RE list with RE disclosure links and GROs; Udofin nodal grievance officer; privacy, storage and destruction policy; ranking metric link; monthly DLG disclosure link (when U14 publishes); RBI Sachet and CMS portal links; cookie settings; accessibility statement; status; sitemap; language switch; "Part of the Infrabyx Group". Every link resolves (CI link check). | M | AT-22-12 |
| FR-22-13 | SEO and structured data: one h1 per page; `Organization`, `BreadcrumbList`, `FAQPage` (FAQ bank) and `Article` JSON-LD; visible last-reviewed date on every standard page; sitemap.xml and HTML sitemap; RSS for blog and changelog; `noindex` on toggled-off and preview hosts. | M | AT-22-13 |
| FR-22-14 | 12 locales for the public site (en, hi at launch; the other ten behind the i18n completeness gate with an acceptance record per locale); `hreflang`; locale switch in the header and footer; regulatory text only from approved translations. | M | AT-22-14 |
| FR-22-15 | Performance and accessibility budgets: Lighthouse performance ≥ 85 on a mid-range Android profile, accessibility ≥ 95, axe-core clean; self-hosted WOFF2 fonts only (Plus Jakarta Sans and Indic families) with licence notes; no third-party font or map request before consent. | M | AT-22-15 |

### 2.2 Studio (channel F) and content governance

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-20 | Studio information architecture (IPB-04 §04.3.12): `CMS › Pages`, `› Blog`, `› Resources`, `› Media`, `› Navigation and footer`, `› Legal pages`, `› Claims Register`, `› Review queue`, `› Redirects`; `Brand Studio › Packs`; `Pricing Studio`; `Feedback › Inbox`; `Tutorials › Library`, `› Tours`; `Changelog`; roles `PLT_CONTENT_EDITOR` (draft, propose), `PLT_LEGAL_REVIEWER` (approve regulated pages and claims), `PLT_SUPER_ADMIN` (publish, rollback), `PLT_SECURITY_OFFICER` (embed allow-list, CSP). | M | AT-22-20 |
| FR-22-21 | Every item has the lifecycle DRAFT → IN_REVIEW → APPROVED → PUBLISHED → (UNPUBLISHED \| ARCHIVED), with immutable published revisions, diff view, scheduled publish and one-click rollback (audited, maker-checker). | M | AT-22-21 |
| FR-22-22 | **Legal review gate:** Safety & your data, Lenders, Pricing, Investors, Grievance, every legal page, the footer, the app-store listing copy and any page with a LAW-tagged "i" require `PLT_LEGAL_REVIEWER` approval on every publish; the approver cannot be the author (two-person rule). | M | AT-22-22 |
| FR-22-23 | **Claims Register** (`cms_claim`): every numeric, comparative or certification claim in any item is a claim record with evidence tier (E1 internal statement, E2 sourced external fact, E3 signed permission or certificate), evidence reference, as-of date, owner and expiry; publish is blocked (`UDF-CMS-CLAIM-001`) while any claim is unevidenced or expired; APR examples carry the formula text and as-of date; `cms.claims.block_on_unevidenced` is FIXED on. | M | AT-22-23 |
| FR-22-24 | **Copy linter** (RA4.4 extended): blocks publish on banned phrases — "RBI approved", "RBI registered app", "approved by RBI", "instant loan", "guaranteed approval", "lowest rate", "100% secure", "no documents", "ISO certified" or "SOC 2 certified" before issue, "Udofin loan", "approved by Udofin", "best lender", "limited time", "hurry"; a dictionary maintained by the legal reviewer with an audited change log; findings shown inline with the rule and the alternative wording. | M | AT-22-24 |
| FR-22-25 | **Bulk import** from `.docx` and Markdown into blocks with the plagiarism check (`PLAGIARISM` port), the copy linter and claim extraction run on import; imported items start as DRAFT. | S | AT-22-25 |
| FR-22-26 | **Brand Studio** for the default Udofin pack: tokens (IPB-D-11 palette seed: primary `#4338CA`, accent `#F59E0B`, Plus Jakarta Sans), logo (SVG sanitised; PNG set generated), favicon set and manifest, OG image template, display name `brand.app_name`, email identity verification, six-screen live preview, contrast guard (`IPB-BRD-003`), maker-checker publish, rollback. Regulatory text is excluded from theming (G.1 rule 6). | M | AT-22-26 |
| FR-22-27 | **Pricing Studio**: mirror of the OH8 plan catalogue (RE plans; S09 consumer plans), plain-language plan explainers, the fixed statement "Fees are paid by the lender to Udofin and are never charged to borrowers" (RV2), gating of RE prices behind lender login, placeholders until prices are approved. | M | AT-22-27 |
| FR-22-28 | **Redirects and 410s**: closed roles and removed pages return 410 with a helpful page; renamed slugs keep 301s; the DLA list page never 404s. | S | AT-22-28 |

### 2.3 Media, uploads and embeds (security)

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-30 | Every upload (Studio media, educator post attachments, resource files) is type-sniffed server-side (magic bytes, not extension), limited by type (images 10 MB, PDF 25 MB, video 500 MB via resumable upload to the `MEDIA` worker), scanned by the `AV` port before it is readable, and stored in `STORAGE_BUCKET_PUBLIC` with metadata stripped (`MEDIA` port). Executables, HTML, SVG-with-script and office macros are refused. | M | AT-22-30 |
| FR-22-31 | SVG logos and icons are sanitised with an allow-list (no `<script>`, `<foreignObject>`, event attributes, external `href`, external `<use>`, `<style>` with `url()`, `<a>`); the sanitised output is re-serialised and stored; the original is discarded (IPB-04-21). | M | AT-22-31 |
| FR-22-32 | Video items require a human-reviewed VTT caption file in the video's language and a transcript before publish (IB6-01); autoplay is disabled; a poster image with alt text is mandatory. | M | AT-22-32 |
| FR-22-33 | Images require alt text (or an explicit "decorative" flag) before publish; focal-point crops are generated by the `MEDIA` port; no third-party image CDN for non-public assets. | M | AT-22-33 |
| FR-22-34 | Resources files (PDF guides, KFS sample) are served through signed URLs with a 15-minute TTL for gated items and public URLs for ungated items; downloads are counted without identifiers. | S | AT-22-34 |
| FR-22-35 | Embeds are allowed only from the provider allow-list (`UDF_CMS_EGRESS_ALLOWLIST`, default YouTube and Vimeo in privacy-enhanced mode) and load only after cookie consent for the relevant category; all server-side fetches (link previews, oEmbed, imports) go through the `EGRESS` port, which refuses private, link-local and metadata addresses, follows no more than two redirects and re-validates DNS on each hop (SSRF guard). | M | AT-22-35 |
| FR-22-36 | Content Security Policy with nonces on every public route; no inline scripts outside the nonce; Markdown and rich text are sanitised server-side (no raw HTML blocks for `PLT_CONTENT_EDITOR`; raw HTML only for `PLT_SUPER_ADMIN` with legal review and a CSP-compatible sanitiser). | M | AT-22-36 |
| FR-22-37 | Forms have rate limits, honeypot plus a privacy-preserving challenge (no third-party CAPTCHA before consent), server-side validation and no PII logging. | M | AT-22-37 |

### 2.4 Blog, educator posts and Resources

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-40 | Blog (`web.blog.enabled`, default on): staff posts by `PLT_CONTENT_EDITOR` with the review gate; categories limited to financial education, product news, safety, company; tags; RSS; reading time; author bios (team items with photo consent). | M | AT-22-40 |
| FR-22-41 | **Educator posts** (`web.blog.user_posts.enabled`, default off; owner decision 46): an external author applies with identity verification (DigiLocker or document review by the content team), a signed declaration of no lender, DSA, collection-agency or LSP affiliation and no compensation from lenders, and a short sample; approved authors submit drafts that are pre-moderated by the content editor and, where the post mentions any regulated concept, the legal reviewer; the post carries the author's name, declaration badge, publication date and the "AI-assisted" label where applicable; comments are off by default. | M | AT-22-41 |
| FR-22-42 | **Educator content rules** (moderation checklist, enforced by the copy linter and the reviewer): no lender, product, rate or offer mention; no outbound links to lenders, DSAs, aggregators or app stores; no affiliate codes; no personal finance advice phrased as instruction ("you should take"); no testimonials; sources cited for figures; plain language; the Claims Register applies. A post failing any rule cannot pass moderation. | M | AT-22-42 |
| FR-22-43 | Author lifecycle: APPLIED → VERIFIED → ACTIVE → SUSPENDED → REMOVED; a suspended author's posts are unpublished (not deleted) pending review; removal purges personal data after the retention period. | M | AT-22-43 |
| FR-22-44 | **Resources library**: KFS explainer (annotated sample KFS), financial-education guides (EMI, APR, cooling-off, credit reports, complaints), safety guides, reports (monthly DLG disclosure archive when U14 publishes; transparency report), downloadable in PDF/A with alt text and tagged structure; gated resources require email with consent and feed OH3 as leads; no gating on anything a regulation requires to be public. | M | AT-22-44 |
| FR-22-45 | `BlogPostPublished` and `ResourcePublished` Ecosystem events are emitted on publish (no personal data). | S | AT-22-45 |

### 2.5 Cookie CMP, marketing tooling and privacy

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-50 | Cookie CMP (`packages/consent-ui`): bottom-sheet banner with categories necessary, functional, analytics, marketing; "Reject all" and "Accept all" of equal weight and size; granular toggles; the choice is stored in the consent ledger (`CONSENT` port) with notice version, locale and timestamp (hashed principal); re-prompt on notice change; "Cookie settings" in the footer reopens it; necessary cookies only before a choice. | M | AT-22-50 |
| FR-22-51 | Marketing tooling (`mkt.*`): tag manager, analytics and pixels load only after the matching consent category is granted and only on `apps/public` routes; `apps/borrower-web`, `apps/mobile`, `apps/portal` and `apps/console` are sensitive routes where `mkt.*` is hard-disabled at build time (no SDK in the bundle) — IPB-DEV-03; a network test asserts zero third-party requests before consent and zero on sensitive routes. | M | AT-22-51 |
| FR-22-52 | UTM parameters are captured server-side into the lead record (OH3) only when a form is submitted with consent; they are never written to a borrower profile or passed into the app deep link beyond the campaign id. | M | AT-22-52 |
| FR-22-53 | Analytics default adapter is self-hosted in India (Plausible or Matomo; owner decision 52); IP addresses are truncated; no cross-site identifiers; a public privacy-preserving stats page is optional. | S | AT-22-53 |
| FR-22-54 | Privacy notice (IPB-05 template 1 instance) is linked from every form and the CMP; the notice version is recorded with every consent. | M | AT-22-54 |

### 2.6 Legal pages (IPB-05 instances with Udofin inserts)

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-60 | The eighteen IPB-05 templates are instantiated for Udofin with the product insert table below; each legal page carries version label, effective date, "what changed" summary, prior-version archive, last-reviewed date and the legal reviewer's approval; regulatory floors in the inserts are not editable from the Studio. | M | AT-22-60 |
| FR-22-61 | Tenancy and roles: CMS objects are platform-scoped; feedback items carry the submitter's tenant and are visible only to the submitter and `ORG_ADMIN` of that tenant; educator author records are platform-scoped with PII class; RLS and permission tests cover every new table. | M | AT-22-61 |

**Udofin insert table (IPB-05).**

| Template | Udofin insert (summary; counsel reviews wording [COUNSEL]) |
|---|---|
| 1 Privacy policy | LSP role and the RE as fiduciary for loan data; minimal data held by Udofin (CF 14(1)); India storage (14(4)); third-party list; permissions never requested (13(1)); consent per purpose (13); retention and destruction policy (14(2)); data-principal rights and the Data Protection Board route; conversation data for Vidhi |
| 2 Terms of use | Udofin does not lend; the lender decides; no fee to borrowers (10(4)); offers are the lender's; store-policy filters; device and security rules; AI assistant terms |
| 3 Payment and subscription | Applies only to consumer plans (S09) when active; never to loans; cancel in one tap; never auto-convert |
| 4 Refund | Consumer plans only; proration rules (RV2.5) |
| 5 Cookie policy | CMP categories; public site only; no tracking in the app |
| 6 AI use policy | Vidhi disclosure; what it never does; provenance labels; human handover; data use and retention |
| 7 Grievance policy | Udofin nodal officer; RE GRO; 30-day RE period; IO; RB-IOS 90 days; CIR complaint clocks; recovery-conduct priority |
| 8 Acceptable use | Educator posts rules; no scraping of lender data |
| 9 Data retention | Per data class; RE-controlled vault; post-exit windows (UP5) |
| 10 Accessibility statement | Generated per release (IPB-06) |
| 11 Responsible disclosure | Security contact; safe harbour; CERT-In coordination |
| 12 User content | Educator posts licence, moderation, takedown |
| 13 Resources terms | Educational only; not advice |
| 14 Marketplace terms | Partner REs: LSP agreement reference; neutrality; DLA register duties |
| 15 DPA | Udofin as processor for RE data; sub-processors; India |
| 16 SLA | RE-facing; mirrors UP2 service levels |
| 17 Vendor assurance statement | Trust Centre summary (IB5) |
| 18 Consent texts | Cookie, marketing, WhatsApp utility, DPDP purposes, educator declaration |

### 2.7 Feedback, tours, tutorials, What's new, app-store copy, "i" registry, Trust Centre

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-22-70 | Feedback widget (`packages/feedback`) on every public page and in every authenticated surface (borrower `Account › Feedback`; staff `Settings › Feedback`): categories bug, idea, accessibility problem, content error; optional screenshot (auto-redacted of text fields); events to the OH backlog (`FeedbackSubmitted`); CSAT/NPS entry permanent (Udofin's existing pattern). | M | AT-22-70 |
| FR-22-71 | Tours: first-run tour per area (Home, Loans, Pay, Help, Account; ops Work Inbox; lender Home), skippable, re-launchable from Tutorials & help, never over a sensitive control, respecting reduced motion. | M | AT-22-71 |
| FR-22-72 | Tutorials: library of short videos with captions and transcripts and picture tutorials for low literacy (one step per picture, icon plus label), mapped to journeys; completion tracked per user without PII. | M | AT-22-72 |
| FR-22-73 | What's new: release cards per audience from the release-notes pipeline (IB7) — borrower cards plain-language; RE cards with the regulatory section (REQ-IAF-23); public changelog page with RSS. | M | AT-22-73 |
| FR-22-74 | App-store listing copy (Play and App Store) is a CMS item type with fields for the short and long descriptions, screenshots with alt text, the Google Play personal-loan declaration fields, the partner-RE list, privacy labels and the data-safety answers; publish requires legal review and a cross-check against the DLA register and each RE's CIMS confirmation (RA4.2); the release pipeline reads the published revision. | M | AT-22-74 |
| FR-22-75 | "i" registry completion (IB4): 262 seed keys published in 12 locales (hidden locales rule applies) with regulatory references and legal review on LAW items; `hlp-lint` and `hlp-coverage` pass (100% KFS, consent, acceptance; ≥ 90% other borrower screens). | M | AT-22-75 |
| FR-22-76 | Public Trust Centre `/trust` renders only `public`-gated documents from the Vendor Assurance Room mirror through the `TRUST` port (certifications held, sub-processors, VAPT summary date, accessibility statement, LSP disclosure summary); the Studio may reorder and describe only (IPB-04-68). | M | AT-22-76 |
| FR-22-77 | Accessibility statement generated per release from the a11y backlog (IPB-06 §06.4.9), published at `/accessibility`, `last_reviewed_at` ≤ 6 months. | M | AT-22-77 |

## 3. Page inventory with required blocks (binding)

| Page | Route | Required blocks (publish blocks until filled) | Review |
|---|---|---|---|
| Home | `/` | hero (one h1, one primary CTA "See how it works"; secondary "Get the app"); what Udofin is (LSP statement); how it works (4 steps); lenders teaser (from register); safety teaser; resources teaser; FAQ (8); footer | Content + legal (LSP statement) |
| How it works | `/how-it-works` | 4 steps with "i"; "the lender decides" callout; cooling-off callout; what you need; FAQ | Legal |
| Lenders | `/lenders` | generated list; intro paragraph; how we work with lenders; "ranking metric" link; CIMS list link | Legal |
| Products | `/products` | product cards (neutral); "offers come from lenders"; store availability note | Legal |
| Safety & your data | `/safety` | FR-22-04 blocks; health check; permissions table; data in India; KFS sample; complaints path; verify the app; Sachet | Legal |
| Pricing | `/pricing` | borrower statement; RE plan names; login gate; FAQ | Legal |
| Resources | `/resources` | filters by type and topic; featured KFS explainer; download rules | Content |
| Blog | `/blog` | list, categories, educator badge legend, RSS | Content |
| About | `/about` | story timeline; mission; "what we do not do" (not a lender; no fees to borrowers; no contacts access); group context; leadership teaser; contact | Legal |
| Team / Leadership / Governance | `/team`, `/leadership`, `/governance` | team grid with photo consent; bios; policies list (adopted or "available on request"); auditor | Content + legal (governance) |
| Investors | `/investors` | toggle; locked disclaimer; vision; market (E2); products; governance; milestones; gated documents; IR contact | Legal, every publish |
| Careers | `/careers` | culture; roles from OH10; benefits (facts); apply form; equal-opportunity statement | Content |
| Press | `/press` | dated releases; coverage (dated, outlet named); media kit (brand pack assets, boilerplate) | Content |
| Partners | `/partners` | partner types (REs, connectors, ODR, GRC); logo wall with permission claims; "become a partner" form | Legal (claims) |
| Contact | `/contact` | form; offices (Delhi, Noida, Jaipur placeholders); click-to-load maps; grievance link | Content |
| Documentation | `/docs` | links; API status; changelog; help | Content |
| Help | `/help` | UB4 content model; search; "Ask Vidhi" entry (Phase 20A) | Content |
| Changelog | `/changelog` | entries by area; RSS | Content + legal (regulatory tags) |
| Trust Centre | `/trust` | from TRUST port; descriptions | Security officer + legal |
| Accessibility | `/accessibility` | generated statement; known issues; feedback | Accessibility lead |
| Grievance | `/grievance` | officer block; form; escalation path; regulator references | Legal |
| Legal | `/legal/{slug}` | 18 instances with version blocks | Legal |
| Sitemap | `/sitemap` | generated | — |
| Status | external | from brand pack | — |

## 4. Data model (schema `cms`, `brand`, `consent`, `fb`, `hlp`; additions to IPB-04 §04.4.1)

| Table | Udofin fields and notes |
|---|---|
| `cms.page`, `cms.block`, `cms.revision` | as IPB-04; `requires_legal_review bool` derived from the page type list (FR-22-22) |
| `cms.lender_listing` (view) | generated from `dla_register` × `product_catalogue`; `description_id` → `cms.block` (legal-reviewed); never editable fields: RE name, registration, GRO, disclosure URL |
| `cms.post` | `author_type` (staff, educator), `author_id`, `ai_assisted bool`, `moderation_state`, `declaration_badge bool`, `comments_enabled bool` (default false) |
| `cms.educator_author` | `state` (APPLIED, VERIFIED, ACTIVE, SUSPENDED, REMOVED), identity verification ref (hash, no document), declaration version and signature ref, `affiliation_declared bool`, `pii_class`, `retention_until` |
| `cms.resource` | `type` (kfs_explainer, guide, safety, report, sample), `gated bool`, `pdfa bool`, `alt_text`, `download_count` (no identifiers) |
| `cms.media` | `sniffed_mime`, `av_status`, `sanitised bool`, `captions_ref`, `transcript_ref`, `alt_text`, `decorative bool` |
| `cms.claim` | `item_id`, `text`, `tier` (E1, E2, E3), `evidence_ref`, `as_of`, `expires_at`, `owner_id`, `state` (OPEN, EVIDENCED, EXPIRED, WITHDRAWN) |
| `cms.lint_rule` | banned phrase, rule id, alternative wording, owner, change log |
| `cms.store_listing` | platform, fields of FR-22-74, `dla_register_check_at`, `cims_confirmations jsonb`, published revision |
| `cms.legal_page_version` | template id, version label, effective date, change summary, approver, prior version link |
| `cms.changelog_entry` | release id, audience, regulatory tags, approved_by |
| `consent.cookie_record` | principal hash, categories, notice version, locale, occurred_at, host |
| `fb.item` | category, tenant_id?, submitter principal, screenshot ref (redacted), state, backlog ref |
| `hlp.entry`, `hlp.locale`, `hlp.review` | as IPB-07 §07.4.3 |
| `brand.pack` (default only in this phase) | IPB-04 shape; Phase 23 adds Udofin fields |

## 5. Claims Register rules (binding)

1. A claim is any statement containing a number, a comparison, a certification, a regulator's name, or a promise about outcome or time. The extractor flags candidates on save; the editor confirms or dismisses with a reason (audited).
2. Tiers: **E1** internal fact that Udofin can evidence from its own systems (for example "lenders on Udofin: 4", generated from the register, auto-evidenced daily); **E2** external fact with a dated source URL or document (for example market size, RBI figures); **E3** a signed permission or certificate (client names, logos, certifications). An APR example is E1 with the formula text, the input assumptions and the as-of date rendered beside it.
3. Expiry: E1 auto-refreshes; E2 expires after 12 months or when the source changes; E3 expires with the document. An expired claim blocks republish and raises a Studio task.
4. Banned claims regardless of evidence: "RBI approved", "RBI registered app", "approved by RBI", "guaranteed approval", "lowest rate", "100% secure", "no documents", any certification before issue, "Udofin loan", "approved by Udofin", "best lender", any fee-free statement other than the exact CF 10(4) sentence approved by legal.
5. The lender list and the DLA details are not claims; they are generated facts and cannot be typed.
6. The copy linter runs on save, on import and on publish; publish is blocked on any OPEN or EXPIRED claim or any banned phrase (`UDF-CMS-CLAIM-001`, `UDF-CMS-LINT-001`).

## 6. State machines and scenario tables

### 6.1 CMS item

DRAFT → IN_REVIEW → APPROVED → PUBLISHED → UNPUBLISHED | ARCHIVED; APPROVED → DRAFT on edit; PUBLISHED → PUBLISHED (new revision) only through the same path; ROLLBACK creates a new PUBLISHED revision pointing to a prior body.

| Scenario | Expected |
|---|---|
| Happy: editor drafts Safety page, legal reviewer approves, super admin publishes | PUBLISHED; revision immutable; cache tag revalidated ≤ 60 s |
| Author approves own item | Refused (two-person rule) |
| Publish with an OPEN claim | Blocked `UDF-CMS-CLAIM-001`; claim list shown |
| Two editors save concurrently | Optimistic lock; second sees conflict diff |
| Rollback after a bad publish | New PUBLISHED revision from a prior body; audited; maker-checker |
| Scheduled publish while legal approval lapses (claim expires) | Scheduler re-checks gates at fire time; blocked and task raised |

### 6.2 Educator post moderation

SUBMITTED → IN_MODERATION → (CHANGES_REQUESTED → SUBMITTED) → APPROVED → PUBLISHED → UNPUBLISHED; author SUSPENDED → all PUBLISHED posts UNPUBLISHED.

| Scenario | Expected |
|---|---|
| Happy | Verified author submits; linter clean; moderator approves; published with badge and date |
| Post names a lender | Linter blocks; CHANGES_REQUESTED with the rule |
| Author later found affiliated | SUSPENDED; posts unpublished within 15 minutes; notice to author; appeal path |
| Moderator and author are the same person (staff who is also an educator) | Refused |
| Rollback | Unpublish; post history kept |

### 6.3 Educator author

APPLIED → VERIFIED (identity + declaration) → ACTIVE (first approved post) → SUSPENDED → REMOVED (data purged after retention).

### 6.4 Vendor-document cadence (IB5 mirror, rendered on `/trust`)

CURRENT → DUE_SOON (30 days before) → OVERDUE → CURRENT (new version acknowledged); OVERDUE items disappear from `/trust` if `public` and raise `trust.CadenceOverdue` to the Work Inbox.

### 6.5 Cookie consent

NONE → CHOSEN(categories, notice v) → RE_PROMPT (notice change) → CHOSEN; withdrawal at any time from footer; scripts load only in CHOSEN with the category granted.

## 7. Screens (Studio, channel F; public site described in §3)

| Path | Content and actions | States |
|---|---|---|
| `CMS › Pages` | List by state, template, locale coverage, last reviewed; create from template; edit blocks with live preview; claims side panel; linter findings; submit for review | Empty, loading, permission-denied, conflict |
| `CMS › Review queue` | Items awaiting legal or content review with diff, claims and lint; Approve / Request changes; two-person rule | — |
| `CMS › Claims Register` | All claims by state, tier, expiry; evidence upload; bulk re-evidence; export | — |
| `CMS › Blog` | Staff posts; educator applications queue (verify, declaration view, approve, suspend); moderation queue | — |
| `CMS › Resources`, `› Media` | Upload with gate results (sniff, AV, sanitise, captions), alt text editor, focal point | Upload rejected states with reason |
| `CMS › Navigation and footer` | Header, footer blocks (required blocks locked), partner list preview (generated) | — |
| `CMS › Legal pages` | 18 templates, insert fields, version publish, archive | — |
| `CMS › Store listing` | Platform tabs, declaration fields, DLA cross-check result, CIMS confirmations, legal approval | Blocked state with missing confirmations |
| `Brand Studio › Packs` | Default pack editor (tokens with contrast guard, logo, favicon, OG, display name, email identity), six-screen preview, publish (maker-checker), rollback | `IPB-BRD-003`, `IPB-BRD-005` states |
| `Pricing Studio` | OH8 mirror, explainers, gating, placeholders | Stale mirror banner |
| `Feedback › Inbox` | Items by category and surface; triage to backlog; accessibility problems SLA view | — |
| `Tutorials › Library`, `› Tours` | Video with captions status, picture tutorials, tour steps editor with sensitive-control guard | — |
| `Changelog` | Release notes drafts (from IB7 pipeline), audiences, regulatory tags, approve, publish | — |

## 8. Settings keys

| Key | Default | Nature | Notes |
|---|---|---|---|
| `web.investors.enabled` | false | GATE (counsel note; App B 47) | |
| `web.blog.enabled` | true | COMMERCIAL | |
| `web.blog.user_posts.enabled` | false | GATE (moderation roster; App B 46) | |
| `web.blog.comments.enabled` | false | COMMERCIAL [REC off] | |
| `web.lenders_page.source` | catalogue | FIXED | |
| `web.docs.url` | — | COMMERCIAL | |
| `web.locales.enabled` | en, hi | FLOOR (12 at exit; hidden until accepted) | |
| `web.cache.lenders_ttl_s` | 900 | CEILING | CF 18(2) |
| `cms.publish.legal_review_pages` | fixed list (FR-22-22) | FIXED | |
| `cms.claims.block_on_unevidenced` | true | FIXED | |
| `cms.claims.e2_expiry_months` | 12 | CEILING | |
| `cms.lint.dictionary_version` | v1 | COMMERCIAL (legal reviewer) | |
| `cms.upload.max_mb.image/pdf/video` | 10 / 25 / 500 | CEILING | |
| `cms.embeds.allowlist` | youtube, vimeo | COMMERCIAL (security officer) | |
| `cms.video.captions_required` | true | FIXED | IB6-01 |
| `consent.cmp.style` | bottom_sheet | COMMERCIAL | |
| `consent.cmp.equal_weight_buttons` | true | FIXED | |
| `mkt.pixels.enabled` | false | COMMERCIAL (public routes only — scope FIXED) | IPB-DEV-03 |
| `mkt.tag_manager.adapter` | none | GATE (App B 52) | |
| `mkt.analytics.adapter` | none | COMMERCIAL | |
| `fb.widget.enabled` | true | COMMERCIAL | |
| `fb.accessibility_sla_days` | 10 | FLOOR [REC] | |
| `tut.tours.enabled` | true | USER_CHOICE (re-launch) | |
| `tut.whats_new.suppression` | none | COMMERCIAL (ORG) | |
| `brand.app_name` | Udofin | COMMERCIAL per pack | |
| `hlp.locales.required` | en, hi → 12 | FLOOR | |
| `hlp.coverage.min_pct.kfs_consent` | 100 | FIXED | |
| `trust.public.show_lsp_disclosure` | true | FIXED | |

## 9. Events and error codes

**Internal (`in.udf.cms.*`, `in.udf.brand.*`, `in.udf.mkt.*`, `in.udf.fb.*`, v1):** `PageRevisionPublished`, `PageRolledBack`, `ClaimBlocked`, `ClaimExpired`, `LintBlocked`, `LenderListingChanged` (RE added or removed; feeds the CF 18(2) notice), `EducatorApplied`, `EducatorVerified`, `EducatorSuspended`, `PostModerated`, `MediaRejected` (reason class), `EmbedRefused`, `StoreListingPublished`, `LegalPageVersionPublished`, `CookieConsentRecorded` (no identifiers), `MarketingScriptLoaded` (category; public route only), `FeedbackSubmitted`, `TourCompleted`, `HlpCoverageBelowFloor`, `TrustCadenceOverdue`.

**Ecosystem:** `in.infrabyx.cms.BlogPostPublished.v1`, `in.infrabyx.cms.ResourcePublished.v1`, `in.infrabyx.feedback.FeedbackSubmitted.v1`, `in.infrabyx.crm.LeadCaptured.v1`, `in.infrabyx.consent.MarketingConsentUpdated.v1`, `in.infrabyx.lending.LenderDisclosurePublished.v1 [PROPOSED for Spec v1.3]` (proposed; IB8), `in.infrabyx.eng.ReleaseNotePublished.v1`.

**Errors:** `UDF-CMS-CLAIM-001` (422; unevidenced or expired claim), `UDF-CMS-LINT-001` (422; banned phrase), `UDF-CMS-REVIEW-403` (two-person rule), `UDF-CMS-UPLOAD-001` (415; type refused), `UDF-CMS-UPLOAD-002` (422; AV failed), `UDF-CMS-UPLOAD-003` (422; captions or alt text missing), `UDF-CMS-EMBED-001` (403; provider not allowed), `IPB-EGRESS-001` (403; private address), `IPB-BRD-003` (contrast), `IPB-BRD-005` (email identity), `UDF-CMS-TOGGLE-404` (page disabled), `UDF-CMS-LENDER-GEN` (409; attempt to type a generated field), `UDF-HLP-001` (plain text over 40 words), `UDF-HLP-002` (LAW citation without reviewer).

## 10. Acceptance tests (Gherkin; representative)

```gherkin
Feature: Regulated publication and claims

  Scenario: AT-22-03 Suspended RE leaves the public site
    Given RE_B is listed on /lenders and in the footer
    When RE_B's deal enters SUSPENDED at 10:00
    Then by 10:15 RE_B is absent from /lenders and the footer on every locale
    And LenderListingChanged is recorded for the CF para 18(2) notice

  Scenario: AT-22-23 Unevidenced APR example
    Given a Home page draft containing "For example, a ₹50,000 loan at 18% APR costs ₹4,560 a month"
    When the editor submits for review
    Then a claim of tier E1 is created in state OPEN
    And publish is refused with UDF-CMS-CLAIM-001 until the formula, assumptions and as-of date are attached

  Scenario: AT-22-24 Banned phrase
    Given a draft containing "RBI approved lending partners"
    When the editor saves
    Then the linter shows the rule, the CF para 18(6) basis and the alternative wording
    And publish is refused with UDF-CMS-LINT-001

  Scenario: AT-22-22 Two-person rule
    Given a legal reviewer authored a change to /safety
    When the same user tries to approve it
    Then the approval is refused with UDF-CMS-REVIEW-403

  Scenario: AT-22-09 Investors toggle off
    When an anonymous visitor requests /investors
    Then the response is 404 with the standard not-found page and noindex

Feature: Uploads, embeds and injection

  Scenario: AT-22-31 SVG with script
    Given an editor uploads a logo SVG containing <script>alert(1)</script> and an onload attribute
    Then the stored SVG contains neither, the PNG set is generated from the sanitised file
    And the original upload is not retained anywhere

  Scenario: AT-22-30 Executable disguised as PDF
    Given a file named guide.pdf whose magic bytes are an executable
    When uploaded to Resources
    Then it is refused with UDF-CMS-UPLOAD-001 and MediaRejected is logged

  Scenario: AT-22-35 SSRF through link preview
    Given an editor pastes http://169.254.169.254/latest/meta-data/ as an embed
    Then the EGRESS port refuses with IPB-EGRESS-001 and no request leaves the cluster

  Scenario: AT-22-36 Stored XSS through rich text
    Given a content editor pastes <img src=x onerror=alert(1)> into a block
    Then the sanitiser strips the handler and the rendered page has no inline script outside the CSP nonce

Feature: Consent-gated marketing

  Scenario: AT-22-51 No pixel before consent
    Given a first-time visitor on /how-it-works
    Then the network log contains no request to any third-party analytics, tag manager or pixel host
    When the visitor chooses "Reject all"
    Then still no such request is made on any page
    When another visitor grants "analytics" only
    Then only the analytics adapter loads, and no marketing pixel loads

  Scenario: AT-22-51b Sensitive routes
    Given a signed-in borrower on /app/home and a lender user on the portal
    Then the bundles contain no marketing SDK and the network log has no third-party request
    And the mobile app bundle contains no analytics or pixel SDK (static scan)

Feature: Educator posts

  Scenario: AT-22-42 Post naming a lender
    Given an ACTIVE educator submits a post mentioning "XYZ Finance offers 12%"
    Then the linter blocks with the educator rule and the post returns CHANGES_REQUESTED

  Scenario: AT-22-43 Affiliated author discovered
    Given an ACTIVE educator with three published posts
    When the content editor sets the author to SUSPENDED with reason "affiliation"
    Then all three posts are UNPUBLISHED within 15 minutes and the author is notified with an appeal path

Feature: Accessibility and locales

  Scenario: AT-22-32 Video without captions
    Given a tutorial video uploaded without a VTT file
    Then publish is refused with UDF-CMS-UPLOAD-003

  Scenario: AT-22-15 Lighthouse and axe
    Then every published page scores accessibility >= 95 and axe-core reports zero violations in light and dark schemes

  Scenario: AT-22-75 "i" coverage
    Then hlp-coverage reports 100% for KFS, consent and acceptance screens and >= 90% for other borrower screens
    And hlp-lint reports zero entries over 40 words and zero LAW entries without a reviewer

Feature: Tenancy

  Scenario: AT-22-61 Feedback item isolation
    Given feedback submitted by a lender user of RE_A
    When an ORG_ADMIN of RE_B lists feedback
    Then RE_A's item is absent (RLS) and a direct id fetch returns 404
```

Further tests: AT-22-01 no hard-coded page content (grep gate); AT-22-04 Safety page required blocks; AT-22-06 Pricing statement and gated RE prices; AT-22-10 forms post to OH with consent receipt and the CMS stores only ids; AT-22-12 footer links resolve and required blocks locked; AT-22-13 JSON-LD valid; AT-22-14 hreflang and hidden locales; AT-22-21 rollback audited and maker-checker; AT-22-26 contrast guard blocks `#F59E0B` on white for body text and allows it for large text or as an accent on indigo (documented pairings); AT-22-27 Pricing Studio mirror stale banner at 24 h; AT-22-44 gated resource lead reaches OH3 with consent; AT-22-50 CMP equal-weight buttons and ledger record; AT-22-52 UTM never on borrower profile; AT-22-70 feedback events to OH backlog without PII; AT-22-71 tour never overlays an OTP field; AT-22-74 store listing cross-check fails when an RE's CIMS confirmation is missing; AT-22-76 Trust Centre shows only `public` documents; AT-22-77 statement regenerated per release.

## 11. Exit gate

- [ ] Every page of §3 published (toggled pages hidden by setting) in English and Hindi, with the other ten locales either published with acceptance records or hidden; footer complete; Lenders page generated; Safety & your data complete with the health check.
- [ ] Claims Register and copy linter blocking; legal-review two-person rule enforced; all claims EVIDENCED; store listing copy published with DLA and CIMS cross-check.
- [ ] Upload, SVG, embed, CSP and SSRF tests pass; captions and alt text gates enforced.
- [ ] CMP live with ledger records; zero third-party requests before consent on public routes and zero on authenticated and mobile routes (test output attached).
- [ ] 18 legal pages published with versions and inserts approved by the legal reviewer [COUNSEL sign-off recorded].
- [ ] Feedback widget, tours, tutorials, What's new, changelog live; "i" registry at 262 keys with coverage floors met; Trust Centre and accessibility statement rendered from their sources.
- [ ] Regulatory register updated (CF 9(4)–(5), 10(4), 12(2), 14(2), 15, 18, 28; IT Rules r.3(2); DPDP notice; ASCI; CCPA) with FR-22 mappings; docs/status and ADRs merged; runbook review gate evidenced.
