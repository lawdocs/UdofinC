# Phase 21 — Public Website, Super-Admin Studio, Blog, Resources and Policies

**Finbyx Master Prompt v1.6 supplement** · 26 October 2026 · Product code FBX · *(v1.6)*

**Primary outcome:** Finbyx's public website (`apps/public`) and the super-admin Studio (`apps/console`) on the shared headless CMS (`packages/cms`), with Brand Studio and white-label brand packs (`packages/brand`), Pricing Studio bound to the Operations Hub OH8 catalogue, Blog (toggle, bulk import, moderated user posts), Vlog toggle, Resources library, the IPB-04 standard pages plus Finbyx product and solution pages, the Security & Trust centre fed by the Vendor Assurance Room mirror (Part 10.7), the IPB-05 policy set with Finbyx inserts, cookie CMP and consent ledger, the binding footer, consent-gated marketing tooling, the feedback widget, tutorials and tours, What's new, the Claims Register lint, and the tenant-visible settings nodes that come with them.

**Depends on:** Phase 2 (identity, tenancy, RLS) for the site and Studio; Phase 16e and Operations Hub O6 for the Pricing Studio binding; Phase 20b and Operations Hub O12/OH14.6 for the Trust Centre data; Phase 1 (`packages/hlp`, tokens); Phase 18A for "Ask Vidhi" in help (optional). **Binding appendices and files:** master prompt Part 3.3.1, Part 10.7, Part 10.8, M18 v1.6 pointer, Appendix G.2.4, G.7.4, G.9, Appendix B items 57–63; `docs/ipb/IPB-04` (every `IPB-04-nn` applies), IPB-05, IPB-08, IPB-02 (uploads, SSRF, host headers, CSP), IPB-06, IPB-07 (help centre, tours, tutorials, What's new), IPB-09 (release notes → changelog), IPB-10 (webhooks). Content: `docs/supplements/v1.6/content/Finbyx_Website_Content_v1.0.md`; design: `docs/supplements/v1.6/design/UI_UX_Design_Brief_v1.6.md`. **Branch:** `cc/21-public-website-studio`. **Precedence:** this file over the condensed Part 12 section; master prompt and IPB over this file where stricter.

---

## 1. Scope and boundaries

**Builds:** `apps/public` (Next.js 16, server-rendered, per-host brand resolution), `apps/console` Studio (platform roles only), `packages/cms` (schema `cms`), `packages/brand` (schema `brand`), `packages/consent-ui` and the consent ledger (`CONSENT` port), `packages/marketing` (`TAG_MANAGER`, `ANALYTICS` ports; UTM capture), `packages/feedback` (`fb` schema; `SUPPORT`/`BACKLOG` ports), the `packages/trust` tenant screens (Part 10.7), `packages/hlp` help-centre rendering, the tutorial pipeline, the IPB-05 policy pages, the Claims Register, the sitemap, robots and JSON-LD, the Changelog consumer of the Part 10.8 pipeline, the Careers (`HR` port) and Contact (`CRM` port) forms.

**Never builds:** any processing of borrower or loan data on the public site; payments or payment webhooks (OH8 hosted checkout only; CM4); WhatsApp templates or marketing messages (servicing-only rule 7A.0.6); a public API beyond the sitemap, RSS and status link; tenant-specific content in the platform CMS (tenant content stays in `apps/web`); anything that claims a certification, attestation or regulatory status that the IPB-08 registry does not hold as `PUBLISHED`.

**Tenant-facing by-products:** `Settings › Customisation › Brands`, `Settings › Feedback`, `Settings › Tutorials & help`, `Settings › What's new`, `Settings › About`, and the Part 10.7 screens under `Settings › Security and trust` (G.7.4 nodes 7, 16, 17, 18, 19, 20).

---

## 2. Definitions (Finbyx additions to IPB-04 §04.2)

| Term | Meaning |
|---|---|
| Content item | A typed CMS record (`page`, `product_page`, `solution_page`, `article`, `user_post`, `resource`, `legal_page`, `changelog_entry`, `team_member`, `office`, `job`, `press_item`, `partner`, `case_study`, `faq`, `nav_menu`, `footer`, `redirect`) with revisions, blocks, SEO fields and a publish state. |
| Claims Register | The IPB-04 register of factual marketing claims with evidence level E0 (none) to E3 (certificate or audited document); lint `IPB-CMS-012` blocks publish of a claim without the required level. Finbyx adds a banned-phrase list (§3.1). |
| Brand pack | The IPB-04 §04.3.2 object; the product default pack plus white-label packs per Part 3.3.1. |
| Regulatory text block | A KFS, APR table, cooling-off notice, grievance-officer block, penal-charge disclosure, recovery-agent notice or RBI-mandated disclosure rendered in the platform's locked layout and wording (`FBX-BRD-001`). |
| User post | A blog article authored by an eligible external author (tenant admin or verified professional) that passes moderation before publication. |
| Gating | Resource access level: `public`, `email` (name, work e-mail, consent), `login` (Finbyx account), `nda` (Trust documents only; via IPB-08). |
| Consent category | `necessary`, `functional`, `analytics`, `marketing` (IPB-04 §04.3.9); every third-party request is mapped to one category and fires only after that category is granted. |

---

## 3. Functional requirements

Tier **M** mandatory for exit, **S** should, **O** optional. Every row names its acceptance test (§9).

### 3.1 CMS core, Studio and publishing

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-01 | Build on `packages/cms` (IPB-04 §04.3.1): content types above with JSON-Schema-validated blocks, revisions (immutable), locales `en` and `hi`, SEO fields (title ≤ 60, description ≤ 160, canonical, OG image, `noindex`), scheduled publish, preview links (signed, expiring 24 h), redirects (301/410) and a sitemap generator. | M | AT-01 |
| FBX-21-02 | Studio information architecture per IPB-04 §04.3.12: CMS · Brand Studio · Pricing Studio · Blog · Vlog · Resources · Footer & Contact · CMP · Marketing · Feedback · Tutorials & tours · What's new · Claims Register · Compliance Documents (IPB-08 mirror admin) · Tenants & plans (link to workspace O). Platform roles only (`PLT_*`); never visible in `apps/web`. | M | AT-02 |
| FBX-21-03 | Roles: `PLT_CONTENT_EDITOR` makes; a second content editor or `PLT_LEGAL_REVIEWER` checks; `PLT_LEGAL_REVIEWER` is the only checker for `legal_page`, the Investors page, any page carrying an E3 claim, and competitor comparisons; `PLT_SUPER_ADMIN` cannot bypass the checker (no self-approval). | M | AT-04 |
| FBX-21-04 | **Publish is maker-checker** for every content type, brand pack, pricing table, footer, CMP configuration and marketing tag; the maker cannot approve; the checker sees the rendered diff; publish, unpublish and rollback are audited with before/after revision ids. | M | AT-04 |
| FBX-21-05 | Legal pages (`/legal/{slug}`) carry version label, effective date, "what changed" summary and a link to every prior version; versions are immutable; publish requires `PLT_LEGAL_REVIEWER` and a counsel sign-off record for the first version of each template. | M | AT-06 |
| FBX-21-06 | **Claims Register lint** (`IPB-CMS-012` plus Finbyx list): publish is blocked when the body contains, in any case or spacing, "RBI-approved", "RBI-compliant", "RBI-certified", "approved by RBI", "ISO certified" (unless the registry holds a `PUBLISHED` certificate and the sentence names scope and certificate id), "SOC 2 certified" (same rule; SOC 2 is a report, never a certification), "PCI certified", "guaranteed", "100% secure", "unhackable", "bank-grade" (without an E2 claim), "zero risk", "assured", "fastest", "largest", "only", "first" (without an E2 claim), "no NPA", "eliminates fraud". Permitted form: "designed to support compliance with <instrument>" backed by an E2/E3 claim id. Numbers need E2+. | M | AT-03 |
| FBX-21-07 | Word (DOCX) and Markdown **bulk import** (LD cross-pollination): zip of files → draft items with headings, images (re-encoded), tables and links mapped; plagiarism check through `PLAGIARISM` (internal shingling plus optional Copyscape) with a similarity report; imports never publish. | S | AT-07 |
| FBX-21-08 | Every public page is server-rendered with one `h1`, `BreadcrumbList` and site-level `Organization` JSON-LD (legal name, logo, `sameAs`, `contactPoint` support and grievance), a visible last-reviewed date, canonical URL, hreflang for `en`/`hi`, and passes Lighthouse accessibility 100 and performance ≥ 90 (budgets in `infra/policy/budgets.json`; `apps/public` initial JS ≤ 150 KB gzipped). | M | AT-08 |
| FBX-21-09 | Caching: static generation with revalidation on publish events; per-host cache keys (brand pack); no cache poisoning by `Host` (FBX-21-22); `Vary` on consent cookie only for the CMP shell. | M | AT-22 |
| FBX-21-10 | Media: uploads through `MEDIA` (sharp/ffmpeg): re-encode, strip EXIF/GPS, responsive variants, focal crop, alt text mandatory; videos only as hosted files with captions (FBX-21-75) or click-to-load embeds through `EGRESS`. | M | AT-30 |
| FBX-21-11 | Platform scope: CMS items hold no tenant or borrower data; the `cms` schema has no tenant foreign keys except `user_post.author_tenant_id` and `fb.feedback.tenant_id`, which are RLS-protected. | M | AT-05 |
| FBX-21-12 | **User posts, feedback and brand packs are tenant-scoped with RLS**: a tenant admin sees and edits only own-tenant drafts; `PLT_*` moderation roles see all; direct-id probes return 404 and are logged. | M | AT-05 |

### 3.2 Brand Studio and white-label brand packs (Part 3.3.1; IPB-04 §04.3.2)

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-13 | Product default pack seeded from IPB-D-11 (slate blue `#1E3A8A`, emerald `#10B981`, Inter, JetBrains Mono, `compact` for back office / `comfortable` public) with the four theme files; editable within the contrast guard. | M | AT-20 |
| FBX-21-14 | Brand pack object exactly per IPB-04 §04.3.2 (hosts, status, `app_name`, terminology incl. `vidhi`, legal entity with CIN/GSTIN/registered office/entity type, logo SVG + PNG set + dark variant, favicon set, OG default, tokens, `fonts_self_hosted`, email identity, policy set, consent banner, footer, sitemap, store identity, analytics adapters, published revision, created/approved by) plus Finbyx fields `regulatory_text_locked: true` (read-only), `powered_by_visible`, `brand_scope` (`tenant_default` \| `additional`), `borrower_portal_enabled`, `field_app_variant`. | M | AT-20 |
| FBX-21-15 | Multi-brand per tenant: `brand.packs.max_per_tenant` (plan; default 1; white-label 5); loan products, branches, borrower records and documents carry `brand_id`; a borrower sees only the brand of the loan's `brand_id` in portal, e-mails, SMS sender name and documents. | M | AT-21 |
| FBX-21-16 | Logo upload: SVG sanitised server-side with the IPB-04-21 allow-list (no `<script>`, `<foreignObject>`, event attributes, external `href`/`use`, `<style>` with `url()`, `<a>`); re-serialised; original discarded; PNG fallbacks 32/64/192/512 generated; favicon set and `site.webmanifest` per host (IPB-04-22). | M | AT-24 |
| FBX-21-17 | Colour tokens with live preview of the six IPB reference screens **plus** Finbyx's KFS, sanction letter and statement renditions; **contrast guard** blocks publish with `IPB-BRD-003` for any text/background pair below 4.5:1 (normal) or 3:1 (large text, UI), computed for light, dark, hc_light and hc_dark. | M | AT-23 |
| FBX-21-18 | Fonts self-hosted WOFF2 from the allow-list (Inter, IBM Plex Sans, Plus Jakarta Sans, Manrope, Noto families; JetBrains Mono fixed for numerals); licence note mandatory; no third-party font CDN on any route (CI network assertion). | M | AT-50 |
| FBX-21-19 | `app_name` is the display name in browser title, manifest, e-mail subject prefix, PDF headers, login screen and store listing; `terminology.vidhi` renders as "<name>, an AI assistant"; kernel identifiers unchanged (IPB-04-27, IPB-03-58). | M | AT-25 |
| FBX-21-20 | E-mail identity per pack: from name, address, reply-to; SPF, DKIM (2048-bit; selector rotated yearly) and DMARC (`p=quarantine` minimum) verified through the `EMAIL` port before publish (`IPB-BRD-005`); exact DNS records shown; daily re-verification; failure reverts to the platform domain with a banner. Borrower SMS keeps the tenant's DLT entity and headers. | M | AT-27 |
| FBX-21-21 | Custom domains: hosts added only after a DNS TXT proof of control; TLS issued through `DNS_CDN`; a host in two packs is a save-time error; removing a host sets 410 for its routes after a grace period. | M | AT-22 |
| FBX-21-22 | **Per-host brand map and host-header defence**: the edge and the server validate `Host` and `X-Forwarded-Host` against the published host allow-list; unknown or spoofed hosts receive the product default pack with `noindex` and never a tenant brand; absolute URLs are built from the pack, never from request headers; cache keys include the resolved pack id, not the raw header. | M | AT-22 |
| FBX-21-23 | Each pack carries its own legal entity, policy set, footer, consent banner, sitemap, robots and store identity; the policy set must be published before the pack can publish (IPB-04-30). | M | AT-26 |
| FBX-21-24 | Brand pack publish is maker-checker with signed preview URLs and one-click rollback to any prior published revision; rollback is audited and maker-checker (IPB-04-31). | M | AT-04 |
| FBX-21-25 | **Regulatory-text guard-rail (`FBX-BRD-001`)**: the KFS, APR table, cooling-off notice, grievance-officer block, penal-charge disclosure, recovery-agent notice and every RBI-mandated disclosure keep the platform's locked layout, order, prominence and wording under every pack; a pack may change logo, colours and typeface only; the rendition test compares the extracted text of these blocks byte-for-byte with the platform rendition. | M | AT-26 |
| FBX-21-26 | Borrower portal (M23) and borrower-facing screens render the pack of the loan's `brand_id`; the field app (M22) builds as a store variant per pack only where the tenant holds developer accounts (`store_identity` complete), otherwise the default field app with in-app brand switching. | S | AT-21 |
| FBX-21-27 | Resale model: each pack footer and About page carry the tenant's legal entity, CIN, GSTIN, registered office, grievance officer and DPO; "Powered by Finbyx" shown unless `brand.powered_by.visible=false` by contract; Infrabyx never appears as the lender; provisioning emits `WhiteLabelTenantProvisioned` (proposed Ecosystem event) **[LAW/COUNSEL: resale contract and OUT para 82 consent wording]**. | M | AT-21 |
| FBX-21-28 | Tenant layer of Brand Studio at `Settings › Customisation › Brands` (G.7.4 node 7): brand admins (tenant role `brand_admin`) edit; tenant admin checks; platform roles can view and suspend a pack for a published-claims or security reason with notice. | M | AT-20 |

### 3.3 Uploads, XSS, SSRF, CSP (IPB-02)

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-29 | Every upload (CMS media, resources, blog images, brand assets, vendor-document mirror, feedback attachments) is type-sniffed by magic bytes (extension must agree), size-capped per type (images 10 MB, PDF 25 MB, video 500 MB, DOCX 20 MB), scanned through `AV` before storage, and stored in `STORAGE_BUCKET_PUBLIC` (public) or the docs bucket (gated) with a content-hash name; executable, script, HTML and archive types are refused for public media. | M | AT-30 |
| FBX-21-30 | A file whose magic bytes disagree with its extension (for example ZIP bytes named `.pdf`), or that fails the AV scan, is refused with `FBX-CMS-004` and the attempt logged; polyglot and oversized files are rejected before being written. | M | AT-30 |
| FBX-21-31 | Rich text is stored as a constrained document model and rendered through a sanitiser allow-list (no inline scripts, event handlers, `javascript:` URLs, `<iframe>`, `<object>`, `<form>`); CSP with per-request nonces, `strict-dynamic`, Trusted Types, `frame-ancestors 'none'`; CSP violation reports collected; the Studio editor cannot insert raw HTML. | M | AT-32 |
| FBX-21-32 | Embeds (YouTube, Vimeo, maps, social posts) and link previews are fetched server-side only through the `EGRESS` allow-list (SSRF guard: no private ranges, link-local, metadata endpoints or redirects off-list), rendered as click-to-load placeholders until the user consents to the mapped category; webhooks and form posts go only to the configured OH endpoints. | M | AT-33 |
| FBX-21-33 | Forms (Contact, Careers, resource gating, feedback, newsletter) have rate limits per IP and per e-mail, honeypot fields, server-side validation, no file uploads except Careers CV (PDF/DOCX, sniffed, AV-scanned, forwarded to OH `HR`, never stored in CMS), and consent text version recorded with the submission id. | M | AT-34 |
| FBX-21-34 | Previews are signed, expire in 24 hours, `noindex`, and never expose draft content to anonymous users without the signature; Studio sessions require MFA and step-up for publish. | M | AT-04 |

### 3.4 Standard pages and Finbyx pages (IPB-04 §04.3.7)

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-35 | Ship every IPB-04 standard page with its template and required sections: Home, About, Team, Leadership, Governance, Investors (toggle), Careers, Press, Partners, Contact, Documentation, Trust Centre, Help, Tutorials, Pricing, Compare (gated by legal review), Case studies, Changelog, Accessibility statement, Sitemap, Legal pages, Grievance, Status (external). Toggled pages exist in the CMS from day one and are hidden by setting (IPB-04-65). | M | AT-10 |
| FBX-21-36 | Finbyx **Products** pages (`/products/{slug}`): LOS, LMS, Collections, Recovery Suite, Regulatory Reporting, Risk & ICAAP, Co-lending; each with hero, capabilities grid (from the master prompt module list, plain language), screenshot placeholders (synthetic data only), "what it does not do" boundary (e.g. "Finbyx prepares returns; your authorised officer files them"), related solutions, FAQ, CTA. | M | AT-10 |
| FBX-21-37 | Finbyx **Solutions** pages (`/solutions/{slug}`): NBFC (BL/ML/UL), Bank and SFB, UCB and co-operative lenders, MFI, HFC, ARC, IFSC; each with the institution-profile story, applicable modules, regulatory context phrased as "designed to support compliance with …", and a boundary statement (co-operative societies are not REs; no co-lending with NBFCs). | M | AT-10 |
| FBX-21-38 | **Security & Trust** (`/trust`): certifications, sub-processors, VAPT summary, data-residency statement, uptime link, DPA request, `security.txt` and responsible-disclosure links, incident-notice policy, exit-assistance statement, Vendor Assurance Room entry (login) — **all read from the IPB-08 registry through `TRUST`** (Part 10.7), never typed; a standard in progress is labelled "in progress"; every badge links to its registry entry (IPB-04-68). | M | AT-40 |
| FBX-21-39 | **Pricing** (`/pricing`): pricing table and comparison table rendered from the **signed OH8 catalogue** (CM1.1; `PAYMENTS_CATALOGUE_SIGNING_PUBKEY_REF`), FAQ, terms links (Payment & Subscription Terms, Refund & Cancellation), "contact sales"; prices, limits and SKU names are never typed into the CMS; the Pricing Studio may only choose which plans to show, their order, highlights and copy; a stale or unsigned catalogue hides prices and shows "contact sales". | M | AT-45 |
| FBX-21-40 | **Investors** (`/investors`): `web.investors.enabled` default false; sections vision, market (E2 sourced), products, governance, leadership, milestones, documents (gated `login` or `email_gate` with NDA flag, served from the IPB-08 room), IR contact (named person), **locked disclaimer block** (IPB-05 Annex; informational, not an offer or invitation to subscribe to securities — Companies Act 2013 s.42, s.23, s.26; SEBI (ICDR) 2018 [LAW]) **[COUNSEL]**; legal-review gate before every publish; words "guarantee", "assured return", "will achieve", "projected" fail lint; when disabled the route returns 404 and the CMS keeps the page. | M | AT-11 |
| FBX-21-41 | **Careers**: open roles (`job` items; department, location, type), benefits (facts only), apply form → OH `HR.createApplication` with consent text; closed roles 410 with link to open roles; `JobPosting` JSON-LD with `validThrough`; equal-opportunity statement. | M | AT-34 |
| FBX-21-42 | **Contact**: form → OH `CRM` with consent receipt; offices Delhi, Noida, Jaipur as `office` records (editable, not deletable) with static click-to-load map images; WhatsApp CTA opens `wa.me` only after an explicit click on a labelled button and shows the WhatsApp opt-in notice (IPB-05 template 18); support hours; grievance officer and DPO named with e-mail. | M | AT-52 |
| FBX-21-43 | **Team and Leadership**: `team_member` items with `photo_consent`; a photo without recorded consent cannot publish; names and roles as text; LinkedIn optional; `group=board` with DIN optional. | M | AT-09 |
| FBX-21-44 | **Changelog** (`/changelog`): entries from the Part 10.8 release-notes pipeline (`ReleaseNotePublished`), filter by product area, RSS, a **Regulatory changes** section driven by the EO1 regulatory-impact tag with REQ-IDs; tenant-only entries render in `apps/web` What's new only. | M | AT-12 |
| FBX-21-45 | **No payment handling on the public site**: checkout links go to the OH8 hosted page; the site holds no payment key, receives no payment webhook, and the CSP blocks any payment-provider script; CM4 webhook signature verification stays in `apps/api` only. | M | AT-45 |
| FBX-21-46 | **Documentation** (`/docs`): link-out to the developer portal (`web.docs.url`) and help centre; API status and changelog links; the portal shares brand pack and CMP. | M | AT-10 |
| FBX-21-47 | **Accessibility statement** (`/accessibility`): IPB-05 template 10 with the known-issues table from the a11y backlog, feedback channel, `last_reviewed_at` ≤ 6 months. | M | AT-10 |
| FBX-21-48 | **Grievance** (`/grievance`): Grievance Officer name, designation, e-mail, postal address, hours, form → OH support (`grievance` destination), escalation path; references IT Rules 2021 r.3(2), DPDP Act 2023 s.13 and, for Finbyx as a software vendor, a statement that borrower grievances about a loan go to the lender's GRO (Part 10.6 item 28) **[COUNSEL on applicability per rule]**. | M | AT-10 |
| FBX-21-49 | Compare pages only after `PLT_LEGAL_REVIEWER` sign-off with dated, sourced rows; case studies name a client only with a permission document id (claims_ref E2/E3). | S | AT-03 |

### 3.5 Trust Centre and Vendor Assurance Room mirror (Part 10.7; IPB-08)

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-50 | Tenant screens under `Settings › Security and trust ›` Vendor documents, Sub-processors, Certifications, Status and uptime, DPA, Incident notices, Evidence pack, Auditor grants, Questionnaires; `vad_mirror_*` tables mirrored from OH14.6 through `TRUST`; **gated documents are tenant-scoped** (`per_tenant`, `nda`) with RLS and acknowledgement (`vada_`) records; a direct-id probe for another tenant's document returns 404 and is logged. | M | AT-41 |
| FBX-21-51 | Cadence status per type (due, overdue, expired) from the Part 10.7 table; expired documents flip the Trust Centre claim to its fallback and raise a reminder to the Hub. | M | AT-42 |
| FBX-21-52 | Evidence pack builder: presets `RBI-OUT-2025-NBFC`, `RBI-OUT-2025-BANK`, `RBI-OUT-2025-UCB`, `IS-AUDIT`, `STATUTORY-AUDITOR`, `CUSTOM`; signed manifest (ed25519), `mapping.csv` (document → OUT/CYB paragraph → tenant control id), per-tenant watermark, hashes before and after watermarking, `verify_url`; download logged `VendorDocumentDownloaded`. | M | AT-43 |
| FBX-21-53 | Auditor grants (AU7.2; ≤ 90 days) scoped `vendor_documents` allow the tenant's auditor or RBI inspector to download gated documents without any loan data; every download in the AU7 log and the tenant audit trail. | M | AT-44 |
| FBX-21-54 | Questionnaire responder: tenant uploads SIG-Lite/CAIQ; Infrabyx answers from the registry; released response becomes `questionnaire_response` (per_tenant). | S | AT-46 |
| FBX-21-55 | Mirror availability: if OH14.6 is unreachable the mirror serves the last published set read-only with the mirror age shown; publish events refresh within 5 minutes. | M | AT-46 |
| FBX-21-56 | Trust Centre never shows a certification, attestation or compliance status without a `PUBLISHED` registry record; "SOC 2" is described as a report; the claims gate (Part 10.6 item 12) applies to every Trust Centre sentence. | M | AT-40 |

### 3.6 Blog, Vlog, Resources, user posts

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-57 | Blog: global toggle `web.blog.enabled` (default false until the owner decides, Appendix B item 57); categories (RBI circular briefs, product, engineering, lending operations); authors; reading time; RSS; related items; `Article` JSON-LD; bulk import (FBX-21-07); scheduled publish; all under the Claims Register lint. | M | AT-13 |
| FBX-21-58 | **User posts**: eligible authors are tenant admins (`ORG_OWNER`/`ORG_ADMIN` of an active tenant) and **verified professionals** (CA, CS, CMA, advocates with enrolment or membership number verified by a platform editor against the institute or Bar Council record and recorded on the author profile); submission → moderation queue (`PLT_CONTENT_EDITOR`; SLA default 2 working days; legal review if the post carries a regulatory claim) → publish with a disclosure line ("Views are the author's; <firm> is a Finbyx customer/partner") → unpublish on complaint; plagiarism and claims lint on submission; rate limit 5 submissions per author per month; author can edit drafts only; published edits re-enter moderation. | M | AT-14 |
| FBX-21-59 | A post from a non-verified or inactive author is refused `FBX-CMS-006`; a published post whose author's tenant becomes inactive is unpublished with notice; user posts never include borrower, loan or client-identifiable data (lint on PAN/mobile/account patterns and tenant names without permission). | M | AT-14 |
| FBX-21-60 | Vlog: toggle `web.vlog.enabled`; videos as hosted files with captions and transcripts (FBX-21-75) or click-to-load embeds; same lint and moderation. | O | AT-13 |
| FBX-21-61 | Resources library (`/resources`): types report, RBI circular brief, template (DOCX/XLSX; synthetic data only), webinar (recording with captions), checklist; gating `public`/`email`/`login`; e-mail gating records name, work e-mail, consent text version and a consent receipt in the ledger; download ledger with hash; resources carry an as-of date and a review date; expired RBI briefs show a "superseded" banner with the newer item. | M | AT-15 |
| FBX-21-62 | Content calendar and review: every article and resource has `review_due_at`; overdue items show in the Studio dashboard; RBI circular briefs cite the circular number, date and the official URL and never paraphrase a paragraph as a quotation. | S | AT-15 |

### 3.7 Footer, CMP, consent, marketing tooling

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-63 | Footer per IPB-04 §04.3.8 on every public route and public shell route: brand block with "Part of the Infrabyx Group", Product, Solutions, Resources, Company and Legal columns, Contact (registered office, offices, phone, WhatsApp button with notice, support and sales e-mails), **entity line** "{legal name} · CIN {cin} · GSTIN {gstin}" (Companies Act 2013 s.12(3)(c) [LAW]), **officers line** (Grievance Officer; DPO) (DPDP Act 2023 s.8(9), s.13; IT Rules 2021 r.3(2) [LAW]), social links with labels, utilities (status, language, cookie settings, accessibility, sitemap, report a problem), **disclaimer** "Finbyx is a software provider and not a regulated entity; it does not lend, collect or decide on loans" **[COUNSEL]**, copyright. `pnpm cms:validate-footer` fails CI when any mandatory field is empty for any published pack (IPB-04-71). | M | AT-16 |
| FBX-21-64 | Legal column lists every adopted IPB-05 template plus Finbyx extras (Digital Lending disclosures where a tenant powers digital lending — rendered per brand pack; KFS sample; LSP/partner list where applicable). | M | AT-16 |
| FBX-21-65 | Cookie CMP (`packages/consent-ui`): categories necessary/functional/analytics/marketing; region default IN with EU and US-CA variants; bottom-sheet style from the pack; equal-prominence accept/reject; granular toggles; "Cookie settings" reopens it; consent record (categories, region, notice version, timestamp, hashed id) written to the consent ledger through `CONSENT`; re-consent on notice change; DPDP consent-manager hook behind `fut.dpdp-consent-manager-api`. | M | AT-50 |
| FBX-21-66 | **Nothing third-party loads before consent**: tag manager, analytics, pixels, embeds, maps, fonts (self-hosted anyway), chat widgets; each script is mapped to a category and injected only after grant; a CI network assertion fails if any request leaves to a non-first-party host on first load; pixels and analytics **never** load on `/app/*`, the Studio, the borrower portal or any authenticated route. | M | AT-50, AT-51 |
| FBX-21-67 | Marketing tooling (`packages/marketing`): `TAG_MANAGER` adapter `none` by default (GTM web or server-side only after Appendix B item 57); `ANALYTICS` adapter Plausible self-hosted (IN) by default, Matomo alternative; pixels (Meta, LinkedIn, Google Ads) as individually toggled, consent-gated tags; UTM parameters captured first-party and attached to Contact/Careers submissions as attribution only (no cross-site identifiers); webhooks to OH3 CRM via Standard Webhooks. | M | AT-51 |
| FBX-21-68 | WhatsApp on the public site is a CTA only (FBX-21-42); no template, broadcast or marketing message is created from Phase 21 surfaces; the channel itself is enabled per tenant only after `mkt.whatsapp.enabled` (super-admin toggle, default off) and a Meta business verification record (Appendix B item 60); servicing-only rule 7A.0.6 unchanged. | M | AT-52 |
| FBX-21-69 | Newsletter (optional): double opt-in; consent record; unsubscribe link in every mail; sender identity of the pack; no borrower lists ever imported. | O | AT-51 |

### 3.8 Feedback, tutorials, tours, What's new, help centre (IPB-04 §04.3.11; IPB-07)

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-70 | Feedback widget (`packages/feedback`) on public pages ("Report a problem") and in `apps/web` (Settings node 16, help menu): categories bug, idea, accessibility problem, content error; optional screenshot (sniffed, scanned; PII blur reminder); correlation id and screen attached automatically, never record data unless the user attaches it; **tenant-scoped** with RLS; routed to OH `SUPPORT` (bugs, accessibility) or `BACKLOG` (ideas) with no PII in the payload; status visible to the submitter; tenant admin sees own-tenant items. | M | AT-55 |
| FBX-21-71 | Beta-tenant feedback links to the flag and release (IPB-09-46); a `mod.` flag cannot graduate with unresolved P1 feedback (Part 10.8). | S | AT-55 |
| FBX-21-72 | Tutorials pipeline (IPB-07 §07.4.5): tutorial items (video with captions and transcript, step list, article) tied to help keys and `nav_item`s; learning paths per role (credit officer, collector, accounts, compliance, tenant admin); progress per user; tenant-curated "Start here". | M | AT-56 |
| FBX-21-73 | Tours: in-app guided tours per screen (first visit; re-launch from Tutorials & help); keyboard-operable; dismissible; never block a regulated action; content from the CMS so copy fixes need no deploy. | M | AT-56 |
| FBX-21-74 | What's new (Settings node 19): release cards from the Part 10.8 pipeline with the **Regulatory changes** section (EO1 tag, REQ-IDs), per-release article link, ORG suppression level; the public Changelog shows the public subset. | M | AT-12 |
| FBX-21-75 | **Captions**: every published video (tutorial, tour, vlog, webinar, resource recording) requires a human-reviewed VTT caption file and a transcript; publish is blocked with `IPB-TUT-003` otherwise; audio-only items require a transcript (G.9). | M | AT-56 |
| FBX-21-76 | Help centre (`/help`): articles from the CMS keyed to `help.fbx.*`, glossary from `packages/hlp` (`hlp.fbx.*`, public entries only), search, "Ask Vidhi" entry point when AI is enabled for the viewer (authenticated only), contact support. | M | AT-56 |

### 3.9 Policies (IPB-05) and product inserts

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-77 | Adopt all eighteen IPB-05 templates as `legal_page` items per brand pack: Privacy Notice, Terms of Use, Payment & Subscription Terms, Refund & Cancellation, Cookie Policy, AI Use & Transparency, Grievance Redressal, Acceptable Use, Data Retention, Accessibility Statement, Security & Responsible Disclosure, User Content, Resources Terms, Marketplace (hidden until a marketplace exists), DPA (request form + template), SLA, Vendor Assurance Statement, Consent Texts (incl. WhatsApp opt-in, cookie banner, e-mail gating, Careers). | M | AT-06 |
| FBX-21-78 | Finbyx product-insert table (filled before counsel review): Privacy — the public site processes no borrower data; tenant data processing is governed by the DPA and the tenant's own notices; Terms — software subscription; the tenant is the regulated entity of record for every loan; Payment and Refund — per OH8 and CM4; hosted checkout; export and read access never stop for non-payment (CM1.4); AI Use — Vidhi disclosure, locked actions, no credit decisions by AI; Grievance — software-vendor grievance officer plus routing of borrower grievances to the lender's GRO; User Content — blog user posts; Resources — templates are samples with synthetic data, not advice; DPA — sub-processors from the IPB-08 registry; SLA — targets from Part 10.3 and the uptime report type; Vendor Assurance Statement — Part 10.7 room; Consent texts — WhatsApp servicing opt-in only. **[COUNSEL: every insert]**. | M | AT-06 |
| FBX-21-79 | Footer policy list and `/legal` index are generated from the adopted set; an adopted template missing a published version blocks the pack's publish (IPB-04-30). | M | AT-16 |
| FBX-21-80 | Policy versions emit `PolicyVersionPublished` internally; `apps/web` shows a re-acceptance prompt for Terms and Privacy changes where the IPB-05 template requires it; consent texts are versioned and referenced by id in every consent record. | M | AT-06 |

### 3.10 Settings, help keys, Appendix G

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-81 | Settings keys per IPB-04 §04.5 (`web.*`, `cms.*`, `brand.*`, `mkt.*`, `fb.*`) and IPB-07 §07.5 (`tut.*`, `hlp.*`) plus Finbyx keys (§6) registered in `packages/config` before code reads them; floors marked. | M | AT-17 |
| FBX-21-82 | Tenant nodes built: Customisation › Brands (7), Feedback (16), Tutorials & help (17), Security & trust additions (18), What's new (19), About (20); platform nodes in `apps/console`; every `nav_item` carries `ipb_node`; the Appendix G navigation test walks each role. | M | AT-17 |
| FBX-21-83 | Help registry: `hlp.fbx.web.*` (≥ 10: brand pack, host, e-mail identity, claims register, consent category, user post, moderation, gating, evidence pack, acknowledgement) and `hlp.fbx.set.*` additions published; every Studio field carries an "i". | M | AT-17 |
| FBX-21-84 | About node (20): product and display name, version and build, licences (open-source notices generated from SBOM), provider legal entity, Vidhi kernel version, terms and privacy links, support contact, grievance officer, data residency. | M | AT-17 |

### 3.11 Operations, SEO, i18n, observability

| ID | Requirement | Tier | AT |
|---|---|---|---|
| FBX-21-85 | SEO: sitemap.xml and HTML sitemap, robots per pack (previews and unknown hosts `noindex`), canonical and hreflang, OG images per page (auto-generated 1200×630 through `IMAGE_GEN` or deterministic SVG→PNG with alt text; human review before publish of any synthetic image, Appendix B item 57), structured data validated in CI. | M | AT-08 |
| FBX-21-86 | Localisation: `en` and `hi` for the public site shell, footer, CMP, legal page titles and the Home/Pricing/Contact pages at launch; other pages fall back to `en` with a visible language note; Indic fonts self-hosted. | S | AT-08 |
| FBX-21-87 | Observability: public-site errors to self-hosted error tracking with no PII; CMP events as aggregate counts only; uptime of `apps/public` on the status page; Studio actions in the platform audit ledger. | M | AT-02 |
| FBX-21-88 | Backups and export: CMS content exported nightly as Markdown + JSON with media manifest to `STORAGE_BUCKET_EXPORTS` (platform scope), restorable without the Studio (Part 7J archive standard spirit). | S | AT-01 |
| FBX-21-89 | Preview environments render `apps/public` with the demo brand pack, mocked OH ports, no analytics adapters, and `noindex`; the Lighthouse, axe and network-assertion checks run against the preview (Part 10.8). | M | AT-08 |
| FBX-21-90 | Documentation: `docs/web/` holds the content model, template list with required blocks, Studio IA, brand-pack schema with the guard-rail, policy insert table, marketing consent matrix, Claims Register rules and the state machines of §7. | M | exit gate |

---

## 4. Screens

### 4.1 Public site (`apps/public`)

| Route | Template | Required blocks | Notes |
|---|---|---|---|
| `/` | home | hero; feature_grid (7 products); audience strip (7 entities); proof (logo_wall or sourced stats); steps; trust teaser; pricing teaser; resources teaser; CTA; FAQ | one h1; no autoplay |
| `/products/{los,lms,collections,recovery-suite,regulatory-reporting,risk-icaap,co-lending}` | product_page | hero; capabilities; boundary; screenshots (synthetic); related solutions; FAQ; CTA | module list from master prompt |
| `/solutions/{nbfc,bank-sfb,ucb-cooperative,mfi,hfc,arc,ifsc}` | solution_page | hero; profile story; modules; regulatory context ("designed to support …"); boundary; CTA | institution profile language (IP1) |
| `/trust` | trust | registry-driven blocks (FBX-21-38) | server-rendered from `TRUST` |
| `/pricing` | pricing | pricing_table (signed catalogue); comparison_table; FAQ; terms links; contact sales | prices never typed |
| `/resources`, `/resources/{slug}` | resources | filters; cards; gating dialog; download ledger | as-of and review dates |
| `/blog`, `/blog/{slug}`, `/blog/authors/{slug}` | blog | list; article; author box with disclosure line for user posts; RSS | toggle |
| `/about`, `/team`, `/leadership`, `/governance` | about, team_grid, governance | per IPB-04 | photo consent |
| `/investors` | investors | per FBX-21-40 | toggle; locked disclaimer |
| `/careers`, `/careers/{slug}` | careers | roles; benefits; apply form | HR port |
| `/partners`, `/press`, `/case-studies` | per IPB-04 | logo_wall with permissions; dated releases; permissioned case studies | |
| `/contact` | contact | form; offices (static maps); WhatsApp CTA; hours; officers | CRM port |
| `/docs`, `/help`, `/tutorials`, `/changelog`, `/status` (external), `/accessibility`, `/grievance`, `/sitemap`, `/legal`, `/legal/{slug}` | per IPB-04 and IPB-07 | | |

### 4.2 Studio (`apps/console`)

Dashboard (drafts awaiting check, overdue reviews, lint failures, expired trust documents, moderation queue, feedback triage), CMS (types, items, revisions, redirects, media, import), Brand Studio (packs list, editor with preview strip and contrast report, hosts and DNS proofs, e-mail identity, policy set binding, publish/rollback), Pricing Studio (catalogue sync status, plan selection and copy), Blog (posts, categories, authors, user-post moderation with author verification records), Vlog, Resources, Footer & Contact (offices, officers, social, entity line), CMP (categories, regions, texts, ledger stats), Marketing (adapters, tags, consent mapping, UTM report), Feedback (triage, routing, status), Tutorials & tours (items, captions check, learning paths), What's new (release drafts from Changesets, regulatory section), Claims Register (claims, evidence level, documents, lint rules), Compliance Documents (IPB-08 mirror admin view; publish is in OH14.6).

### 4.3 Tenant settings (`apps/web`)

`Settings › Customisation › Brands` (packs, editor, preview incl. KFS, publish request, rollback), `Settings › Feedback` (submit, mine, tenant list), `Settings › Tutorials & help` (paths, tours, tutorials, shortcuts, glossary, Start here), `Settings › What's new`, `Settings › About`, `Settings › Security and trust › …` (Part 10.7 screens).

---

## 5. Events and error codes

**Internal events** (`in.fbx.cms.*`, `in.fbx.brand.*`, `in.fbx.mkt.*`, `in.fbx.fb.*`, `in.fbx.trust.*`): `ContentDrafted`, `ContentSubmitted`, `ContentApproved`, `ContentPublished`, `ContentUnpublished`, `ContentRolledBack`, `ClaimsLintFailed`, `UserPostSubmitted`, `UserPostModerated`, `ResourceDownloaded`, `BrandPackDrafted`, `BrandPackPublished`, `BrandPackRolledBack`, `BrandHostVerified`, `EmailIdentityVerified`, `ContrastGuardFailed`, `ConsentRecorded`, `TagFired` (aggregate), `FeedbackSubmitted`, `FeedbackRouted`, `TutorialPublished`, `ReleaseNoteRendered`, `VendorDocumentMirrored`, `VendorDocumentAcknowledged`, `VendorDocumentDownloaded`, `EvidencePackGenerated`, `PolicyVersionPublished`. Payloads carry ids, hashes, versions and categories — never personal data.

**Proposed Ecosystem events** (Appendix E.6.4): `WhiteLabelTenantProvisioned`, `BrandPackPublished`, `ContentPublished`, `UserPostModerated`, `FeedbackSubmitted`, `ConsentRecorded`, `VendorAssuranceDocumentPublished`, `VendorAssuranceAcknowledged`, `VendorEvidencePackGenerated`, `HelpTermPublished`. *(v1.6 review)* Emit only the canonical Spec v1.2 names: `tenancy.WhiteLabelTenantProvisioned`, `tenancy.BrandPackPublished`, `cms.BlogPostPublished` / `cms.ResourcePublished` (for `ContentPublished`), `feedback.FeedbackSubmitted`, `consent.MarketingConsentUpdated` (cookie, marketing, WhatsApp) or `privacy.ConsentRecorded` (product consents), `trust.VendorAssuranceDocumentPublished`, `trust.VendorAssuranceDocumentAcknowledged` (`action = ACKNOWLEDGED` or `PACK_EXPORTED`); `UserPostModerated` and `HelpTermPublished` stay `in.fbx.*` until registered (Appendix E.6.4 canonical-names note).

**Error codes** (additive to IPB `IPB-CMS-*`, `IPB-BRD-*`, `IPB-TUT-*`):

| Code | Meaning | HTTP | Help key |
|---|---|---|---|
| `FBX-BRD-001` | Regulatory text block altered by a brand pack | 422 | `hlp.fbx.web.regulatory_text` |
| `FBX-BRD-002` | Host not proven by DNS TXT record | 422 | `hlp.fbx.web.host_proof` |
| `FBX-BRD-003` | Pack count above plan limit | 403 | `hlp.fbx.web.brand_pack` |
| `FBX-BRD-004` | Brand pack publish without a published policy set | 409 | `hlp.fbx.web.policy_set` |
| `FBX-BRD-005` | Store identity incomplete for a field-app variant | 422 | `hlp.fbx.web.store_identity` |
| `FBX-CMS-001` | Banned phrase (Finbyx list) in content | 422 | `hlp.fbx.web.claims_register` |
| `FBX-CMS-002` | Numeric claim without E2+ evidence | 422 | `hlp.fbx.web.claims_register` |
| `FBX-CMS-003` | Legal page publish without `PLT_LEGAL_REVIEWER` | 403 | `hlp.fbx.web.legal_review` |
| `FBX-CMS-004` | Upload refused: type mismatch, size, or AV positive | 415/413/422 | `hlp.fbx.web.upload` |
| `FBX-CMS-005` | Embed or link preview host not on the egress allow-list | 422 | `hlp.fbx.web.embed` |
| `FBX-CMS-006` | User post author not eligible or not verified | 403 | `hlp.fbx.web.user_post` |
| `FBX-CMS-007` | User post contains identifier-like data or an unpermitted client name | 422 | `hlp.fbx.web.user_post` |
| `FBX-CMS-008` | Video published without captions or transcript | 422 | `hlp.fbx.web.captions` |
| `FBX-CMS-009` | Pricing catalogue unsigned or stale | 409 | `hlp.fbx.web.pricing` |
| `FBX-CMS-010` | Trust claim without a PUBLISHED registry record | 422 | `hlp.fbx.web.trust_claim` |
| `FBX-CMS-011` | Tag or script mapped to no consent category | 422 | `hlp.fbx.web.consent_category` |
| `FBX-CMS-012` | Footer mandatory field empty (build-time) | build | `hlp.fbx.web.footer` |

---

## 6. Settings keys (Finbyx additions; IPB-04 §04.5 and IPB-07 §07.5 apply in full)

| Key | Tier | Type | Default | Who | MC | Class |
|---|---|---|---|---|---|---|
| `web.investors.enabled` | PLATFORM | bool | false | `PLT_SUPER_ADMIN` + `PLT_LEGAL_REVIEWER` | yes | commercial |
| `web.blog.enabled`, `web.vlog.enabled` | PLATFORM | bool | false | `PLT_CONTENT_EDITOR` | yes | commercial |
| `web.blog.user_posts.enabled` | PLATFORM | bool | false | `PLT_CONTENT_EDITOR` | yes | commercial |
| `web.blog.user_posts.eligible_roles` | PLATFORM | json | `["ORG_OWNER","ORG_ADMIN","VERIFIED_PROFESSIONAL"]` | `PLT_CONTENT_EDITOR` | yes | commercial |
| `web.blog.user_posts.moderation_sla_days` | PLATFORM | int | 2 | `PLT_CONTENT_EDITOR` | no | commercial |
| `web.blog.user_posts.rate_limit_per_month` | PLATFORM | int | 5 | `PLT_CONTENT_EDITOR` | no | commercial |
| `web.claims.banned_phrases` | PLATFORM | json | Finbyx list (FBX-21-06) | `PLT_LEGAL_REVIEWER` | yes | floor (may only grow) |
| `web.pricing.require_signed_catalogue` | PLATFORM | bool | true | — | — | floor |
| `web.trust.registry_only` | PLATFORM | bool | true | — | — | floor |
| `web.footer.disclaimer_text` | BRAND | string | Finbyx boundary statement | `PLT_LEGAL_REVIEWER` | yes | commercial [COUNSEL] |
| `brand.packs.max_per_tenant` | PLAN | int | 1 (white-label 5) | `PLT_SUPER_ADMIN` | yes | commercial |
| `brand.custom_domain.enabled` | PLAN | bool | false | `PLT_SUPER_ADMIN` | yes | commercial |
| `brand.email_identity.required_dmarc` | PLATFORM | enum | `quarantine` | `PLT_SECURITY_OFFICER` | yes | floor (tighten to `reject`) |
| `brand.regulatory_text.locked` | PLATFORM | bool | true | — | — | floor (read-only) |
| `brand.powered_by.visible` | PLAN | bool | true | `PLT_SUPER_ADMIN` (contract) | yes | commercial |
| `brand.field_app_variant.enabled` | PLAN | bool | false | `PLT_SUPER_ADMIN` | yes | commercial |
| `mkt.tag_manager.adapter` | PLATFORM | enum | `none` | `PLT_SUPER_ADMIN` | yes | commercial (Appendix B 57) |
| `mkt.analytics.adapter` | BRAND | enum | `plausible_self` | `PLT_CONTENT_EDITOR` | yes | commercial |
| `mkt.pixels.<key>.enabled` | BRAND | bool | false | `PLT_CONTENT_EDITOR` | yes | commercial (consent-gated) |
| `mkt.authenticated_routes.block_tags` | PLATFORM | bool | true | — | — | floor |
| `mkt.whatsapp.enabled` | PLATFORM (per tenant grant) | bool | false | `PLT_SUPER_ADMIN` | yes | commercial; servicing-only rule is a floor |
| `fb.widget.public.enabled`, `fb.widget.app.enabled` | PLATFORM / TENANT | bool | true | editors / tenant admin | no | commercial |
| `fb.route.bug`, `fb.route.idea` | PLATFORM | enum | `SUPPORT`, `BACKLOG` | `PLT_RELEASE_MANAGER` | no | commercial |
| `tut.captions.required` | PLATFORM | bool | true | — | — | floor |
| `tut.whats_new.suppression_level` | TENANT | enum | `all` | tenant admin | no | commercial |
| `trust.pack.default_preset` | TENANT | enum | by institution profile | tenant admin | no | commercial |
| `trust.exit_plan.pinned` | PLATFORM | bool | true | — | — | floor |
| `cms.preview.ttl_hours` | PLATFORM | int | 24 | `PLT_RELEASE_MANAGER` | no | commercial |
| `cms.upload.max_mb.<type>` | PLATFORM | int | image 10, pdf 25, video 500, docx 20 | `PLT_SECURITY_OFFICER` | yes | commercial (lower only) |

---

## 7. State machines and scenario tables

### 7.1 Content item

`DRAFT → IN_REVIEW → APPROVED → SCHEDULED → PUBLISHED → UNPUBLISHED | ARCHIVED`; `PUBLISHED → ROLLED_BACK(to revision n)`; lint runs on `DRAFT → IN_REVIEW`.

| Scenario | Expected |
|---|---|
| Happy | editor drafts → submits (lint clean) → checker approves → scheduled → published; revision immutable; sitemap and cache revalidate |
| Lint failure | submit refused `FBX-CMS-001`/`IPB-CMS-012`; phrase and rule shown; item stays DRAFT |
| Legal page without legal reviewer | approve refused `FBX-CMS-003` |
| Maker approves own item | refused `sod_conflict` |
| Concurrency: two checkers | first approval wins; second `stale_version` |
| Rollback | PUBLISHED → ROLLED_BACK to revision n (maker-checker); the rolled-back revision becomes the published one; audit shows both ids |
| Scheduled item whose catalogue or registry dependency is stale at publish time | publish deferred with alert (pricing/trust blocks render fallbacks) |

### 7.2 Brand pack

`DRAFT → PREVIEW → IN_REVIEW → PUBLISHED → SUPERSEDED | SUSPENDED | RETIRED`; rollback republishes a prior revision.

| Scenario | Expected |
|---|---|
| Happy | tenant brand admin drafts → preview on nine screens (six IPB + KFS, sanction letter, statement) → tenant admin checks → published; hosts resolve; manifest and favicons served |
| Contrast failure | publish blocked `IPB-BRD-003` with the failing pair named |
| Regulatory text altered (template hack) | `FBX-BRD-001`; publish blocked |
| Host unproven | add host refused `FBX-BRD-002`; pack publishable without that host |
| E-mail identity unverified | publish blocked `IPB-BRD-005`; platform sender used meanwhile |
| Policy set not published | `FBX-BRD-004` |
| Concurrency: two packs claim one host | second save refused |
| Platform suspension (claims or security) | PUBLISHED → SUSPENDED; hosts fall back to the tenant default pack with notice; tenant informed with reason |
| Rollback | republish revision n; audited; e-mail identity and hosts re-verified |

### 7.3 User post

`DRAFT → SUBMITTED → IN_MODERATION → (NEEDS_LEGAL) → APPROVED → PUBLISHED → UNPUBLISHED | REJECTED`

| Scenario | Expected |
|---|---|
| Happy | verified author submits → lint and plagiarism clean → moderator approves within SLA → published with disclosure line |
| Non-verified author | submit refused `FBX-CMS-006` |
| Identifier-like data | refused `FBX-CMS-007` with the span |
| Regulatory claim | NEEDS_LEGAL; `PLT_LEGAL_REVIEWER` decides |
| Author tenant inactive | PUBLISHED → UNPUBLISHED with notice |
| Edit after publish | new revision re-enters IN_MODERATION; live version unchanged until approval |
| Concurrency: author edits while moderator approves | `stale_version`; moderator re-reviews |
| Complaint | UNPUBLISHED within one working day pending review; record kept |

### 7.4 Resource gating and download

`REQUESTED → CONSENTED → GRANTED → DOWNLOADED` (email gating) or `LOGIN_REQUIRED → GRANTED` (login).

| Scenario | Expected |
|---|---|
| Email gate | name, work e-mail, consent → receipt id → signed URL (5 min) → download hashed and logged |
| Rate limit | > 10 requests per e-mail per day refused |
| Expired resource | banner; download allowed with "superseded" watermark |
| Login-gated with no account | redirect to sign-in; no partial content |

### 7.5 Vendor document mirror (IPB-08 §08.4.3 — Finbyx mirrors, never edits)

| Scenario | Expected |
|---|---|
| Publish in OH14.6 | mirror row within 5 min; Trust Centre updates; subscribers notified |
| Supersede | old version SUPERSEDED; acknowledgers notified |
| Expire | claim flips to fallback; "in progress"/"expired" label; reminder to Hub |
| Withdraw | downloads blocked except archival copy marked WITHDRAWN for acknowledged tenants |
| Hub unreachable | last set served read-only with mirror age |
| Gating change | re-evaluation; never loosens `per_tenant` financials |

### 7.6 Consent record

`PENDING → GRANTED(categories) | REJECTED → WITHDRAWN → RE_CONSENT_REQUIRED (notice change)`; tags fire only in GRANTED for their category; withdrawal stops tags at next page load and is written to the ledger.

---

## 8. Policies insert table (summary; full in `docs/web/policy-inserts.md`) — all **[COUNSEL]**

| IPB-05 template | Finbyx insert |
|---|---|
| 1 Privacy Notice | Finbyx Technologies (entity per Appendix B 55) is a software provider; the public site processes contact-form, careers, newsletter and cookie data only; borrower data is processed for tenants under the DPA; DPO and Grievance Officer named; DPDP Act 2023 rights and the consent-manager route |
| 2 Terms of Use | software subscription; tenant is the RE of record; no lending, collection or advice by Finbyx; acceptable use; Vidhi outputs are drafts for professionals |
| 3 Payment & Subscription; 4 Refund & Cancellation | OH8 hosted checkout; GST invoices; regulatory-continuity rule (CM1.4): export and read access never stop for non-payment; cancellation as easy as purchase |
| 5 Cookie Policy | categories, retention, CMP, consent ledger |
| 6 AI Use & Transparency | Vidhi disclosure; autonomy ceilings; locked actions; India inference; no training on tenant data; FREE-AI alignment summary |
| 7 Grievance Redressal | software-vendor grievance officer; borrower loan grievances → lender's GRO; IT Rules r.3(2) |
| 8 Acceptable Use | no borrower data in user posts or feedback; no scraping |
| 9 Data Retention | public-site data retention; tenant data per DPA and Part 7J |
| 10 Accessibility Statement | WCAG 2.2 AA; IS 17802; known issues; feedback |
| 11 Security & Responsible Disclosure | `security.txt`; safe-harbour wording; CERT-In alignment |
| 12 User Content | blog user posts terms; disclosure line; moderation; takedown |
| 13 Resources Terms | templates are samples with synthetic data; not advice; no warranty |
| 14 Marketplace | hidden until a connector marketplace is sold |
| 15 DPA | sub-processors from the IPB-08 registry; India residency; audit rights per OUT clauses (Part 10.6 item 1) |
| 16 SLA | Part 10.3 targets; uptime report type; credits per OH8 |
| 17 Vendor Assurance Statement | Part 10.7 room; cadence; evidence packs |
| 18 Consent texts | cookie banner; e-mail gating; Careers; Contact; WhatsApp servicing opt-in (no marketing) |

---

## 9. Acceptance tests (Gherkin; `FBX-21-AT-01` to `-AT-60`)

Test numbers are grouped by feature (01–17 CMS and pages, 20–27 brand packs, 30–34 uploads and injection, 40–46 trust, 50–56 consent and help, 57–60 accessibility and operations); the unused numbers in each group are reserved for tests added during the phase and must not be reassigned.

```gherkin
Feature: CMS core and publishing
  @FBX-21-AT-01
  Scenario: Content types, revisions and export
    When an editor creates and publishes a page in en and hi
    Then two immutable revisions exist, the sitemap lists the route and the nightly export contains the item as Markdown and JSON

  @FBX-21-AT-02
  Scenario: Studio is platform-only and audited
    When a tenant admin requests /console
    Then 403 is returned and no Studio nav_item exists in apps/web
    When a PLT_CONTENT_EDITOR publishes an item
    Then the platform audit ledger holds the action with before and after revision ids

  @FBX-21-AT-03
  Scenario: Claims Register lint blocks banned phrases and unevidenced numbers
    Given a draft containing "Finbyx is RBI-compliant"
    When it is submitted
    Then it is refused with IPB-CMS-012 and FBX-CMS-001 naming the phrase
    Given a draft with "designed to support compliance with the RBI Scale Based Regulation Directions" and claim id CLM-014 at level E2
    Then it passes
    Given a draft with "processes 1 crore loans a month" and no claim
    Then it is refused FBX-CMS-002

  @FBX-21-AT-04
  Scenario: Maker-checker on publish, rollback and previews
    When the maker tries to approve their own item
    Then sod_conflict is returned
    When a checker approves and later rolls back to revision 3
    Then both actions are audited and the live revision is 3
    When an anonymous user opens an expired preview link
    Then 401 is returned

  @FBX-21-AT-05
  Scenario: Tenant scoping of user posts, feedback and brand packs
    Given tenant A's draft user post, feedback item and brand pack ids
    When tenant B's admin requests them by id
    Then 404 is returned for each and the probes are logged

  @FBX-21-AT-06
  Scenario: Legal pages need the legal reviewer and keep versions
    When a content editor approves a legal_page
    Then FBX-CMS-003 is returned
    When PLT_LEGAL_REVIEWER approves version 2
    Then version 1 remains reachable from the page with its effective dates and the consent text ids remain valid

  @FBX-21-AT-07
  Scenario: Bulk import never publishes and reports similarity
    When a zip of DOCX files is imported
    Then draft items exist with a plagiarism report and none is published

  @FBX-21-AT-08
  Scenario: Rendering, SEO and budgets
    When Lighthouse runs on Home, Pricing, Trust and an article in the preview
    Then accessibility is 100 and performance at least 90
    And each page has one h1, BreadcrumbList and Organization JSON-LD and a last-reviewed date
    And apps/public initial JS is at most 150 KB gzipped

  @FBX-21-AT-09
  Scenario: Photo consent
    When a team_member with a photo and no photo_consent is published
    Then publish is refused

Feature: Standard and Finbyx pages
  @FBX-21-AT-10
  Scenario: Every standard page exists and toggled pages are hidden not absent
    Then every route in §4.1 responds 200 or, for toggled-off pages, 404 while the CMS item exists
    And each Products and Solutions page carries a boundary statement block

  @FBX-21-AT-11
  Scenario: Investors toggle, disclaimer and lint
    Given web.investors.enabled false
    Then /investors returns 404 and the CMS holds the page
    Given the toggle true and the disclaimer block removed
    Then publish is refused
    Given the text "projected returns"
    Then lint fails IPB-CMS-012

  @FBX-21-AT-12
  Scenario: Changelog and What's new from the release pipeline
    Given a ReleaseNotePublished event with regulatory_impact true and REQ-IDs
    Then /changelog shows the entry in the Regulatory changes section with the REQ-IDs
    And Settings › What's new shows the tenant card with the same section

  @FBX-21-AT-13
  Scenario: Blog toggle and RSS
    Given web.blog.enabled false
    Then /blog returns 404 and the footer omits Blog
    Given it is true
    Then /blog renders with RSS and Article JSON-LD

  @FBX-21-AT-14
  Scenario: User posts eligibility and moderation
    When a user without verification submits a post
    Then FBX-CMS-006 is returned
    When a verified CS submits a post containing a 10-digit mobile number
    Then FBX-CMS-007 is returned naming the span
    When a verified author's clean post is submitted
    Then it waits in moderation, is never public before approval, and publishes with the disclosure line
    When the author's tenant becomes inactive
    Then the post is unpublished with notice

  @FBX-21-AT-15
  Scenario: Resource gating and ledger
    When a visitor requests an email-gated resource
    Then a consent receipt is written, a 5-minute signed URL is issued and the download hash is logged
    When the eleventh request from one e-mail arrives in a day
    Then it is refused

  @FBX-21-AT-16
  Scenario: Footer validator and legal list
    Given a published pack whose grievance officer e-mail is empty
    When pnpm cms:validate-footer runs
    Then CI fails with FBX-CMS-012
    Then the Legal column lists every adopted IPB-05 template and the entity and officers lines are text nodes mirrored in JSON-LD

  @FBX-21-AT-17
  Scenario: Settings nodes, keys and help
    Then Settings nodes 7, 16, 17, 18, 19 and 20 render with ipb_node set, every web./cms./brand./mkt./fb./tut. key is registered and hlp.fbx.web.* has at least 10 published terms

Feature: Brand packs
  @FBX-21-AT-20
  Scenario: Default pack and tenant brand admin
    Then the product default pack carries #1E3A8A, #10B981, Inter and JetBrains Mono and passes the contrast guard in four themes
    When a tenant brand_admin edits a pack
    Then the tenant admin must check before publish

  @FBX-21-AT-21
  Scenario: Multi-brand per tenant and borrower view
    Given a white-label plan with two packs and loans carrying each brand_id
    When the borrower of brand B opens the portal and receives a statement
    Then only brand B appears in portal, e-mail sender and PDF header
    And WhiteLabelTenantProvisioned was emitted at provisioning
    When a third pack is added on a plan limited to two
    Then FBX-BRD-003 is returned

  @FBX-21-AT-22
  Scenario: Host-header defence
    When a request arrives with Host app.evil.example not in any pack
    Then the default pack renders with noindex and no tenant brand or cache entry keyed to that host
    When X-Forwarded-Host is spoofed to a tenant host from an untrusted hop
    Then the header is ignored and the default pack renders
    When a host is added without a DNS TXT proof
    Then FBX-BRD-002 is returned

  @FBX-21-AT-23
  Scenario: Contrast guard
    Given a pack with text #94A3B8 on #FFFFFF (3.9:1)
    When publish is requested
    Then IPB-BRD-003 names the pair and the pack stays unpublished

  @FBX-21-AT-24
  Scenario: SVG sanitiser and favicon set
    When an SVG logo containing <script> and an external <use> is uploaded
    Then the stored SVG has neither, the original is discarded and favicons 16/32/180/192/512 and site.webmanifest are served per host

  @FBX-21-AT-25
  Scenario: Display name and Vidhi terminology
    Given app_name "Arth Lending" and terminology.vidhi "Arth"
    Then browser title, manifest, e-mail subject prefix, PDF header and login show "Arth Lending" and the AI label reads "Arth, an AI assistant"; audit rows show vidhi

  @FBX-21-AT-26
  Scenario: Regulatory text locked under a pack
    Given a white-label pack with a serif heading font and emerald replaced by teal
    When the KFS and sanction letter render
    Then the extracted text of the KFS, APR table, cooling-off notice, grievance block and penal-charge disclosure is byte-identical to the platform rendition and their order and prominence unchanged
    When a template edit attempts to shorten the cooling-off notice
    Then FBX-BRD-001 is returned
    Given a pack whose policy set is unpublished
    Then publish is refused FBX-BRD-004

  @FBX-21-AT-27
  Scenario: E-mail identity verification
    Given a pack domain without DKIM
    When publish is requested
    Then IPB-BRD-005 is returned with the exact DNS records to add
    Given SPF, DKIM and DMARC quarantine pass
    Then the pack publishes and daily re-verification is scheduled; on a later failure sending reverts to the platform domain with a banner

Feature: Uploads, XSS, SSRF, forms
  @FBX-21-AT-30
  Scenario: Upload sniffing, size and AV
    When a file named report.pdf whose bytes are a ZIP is uploaded
    Then FBX-CMS-004 is returned and the attempt is logged
    When a 600 MB video is uploaded
    Then it is refused before being written
    When the EICAR test file is uploaded as an image
    Then it is refused by the AV scan
    When a JPEG with GPS EXIF is uploaded
    Then the stored variants carry no EXIF

  @FBX-21-AT-31
  Scenario: Public media types
    When an HTML or SVG file is uploaded as a resource
    Then it is refused for public media and SVG is accepted only through the logo sanitiser path

  @FBX-21-AT-32
  Scenario: XSS defences
    Given rich text containing <img onerror=alert(1)> and a javascript: link
    When it is saved and rendered
    Then the attributes and link are stripped and the CSP report shows no inline-script violation on any page

  @FBX-21-AT-33
  Scenario: SSRF guard on embeds and previews
    When an embed URL points to 169.254.169.254 or an off-list host
    Then FBX-CMS-005 is returned and no request leaves the egress proxy
    When a YouTube embed is placed
    Then it renders click-to-load and loads only after functional consent

  @FBX-21-AT-34
  Scenario: Forms and Careers
    When fifty contact submissions arrive from one IP in a minute
    Then rate limiting applies and the honeypot catches bot entries
    When a CV in DOCX is submitted
    Then it is sniffed, scanned, forwarded to the HR port and not stored in the CMS; the consent text version and receipt id are recorded

Feature: Trust Centre and Vendor Assurance Room
  @FBX-21-AT-40
  Scenario: Registry-driven claims only
    Given the IPB-08 registry holds cert_iso27001 in REVIEW and soc2_report PUBLISHED
    When /trust renders
    Then ISO/IEC 27001 shows "in progress" and SOC 2 shows "report available on request (NDA)"; no certification badge is shown for ISO
    When an editor types "ISO 27001 certified" into the trust page copy
    Then FBX-CMS-010 is returned

  @FBX-21-AT-41
  Scenario: Gated vendor documents are tenant-scoped
    Given a per_tenant document published to tenant A
    When tenant B's auditor requests it by id
    Then 404 is returned and the probe is logged
    When tenant A's CCO acknowledges it
    Then a vada_ record exists

  @FBX-21-AT-42
  Scenario: Cadence and expiry
    Given a bcp_dr_test_report older than its quarterly cadence
    Then the tenant screen shows "overdue" and the Trust Centre claim shows its fallback

  @FBX-21-AT-43
  Scenario: Evidence pack
    When a tenant generates the RBI-OUT-2025-NBFC pack
    Then the zip contains the manifest, mapping.csv with OUT paragraph references, watermarked PDFs with both hashes and a valid ed25519 signature verifiable at verify_url

  @FBX-21-AT-44
  Scenario: Auditor grant
    Given a 30-day AU7 grant scoped vendor_documents
    When the auditor downloads a gated document
    Then the download appears in the AU7 log and the tenant audit trail and the auditor cannot open any loan screen

  @FBX-21-AT-45
  Scenario: Pricing from the signed catalogue and no payment handling
    Given a signed OH8 catalogue
    Then /pricing shows its plan names, prices and limits and no CMS-typed price exists
    Given the catalogue signature fails
    Then prices are hidden and "contact sales" shows with FBX-CMS-009 in the Studio
    When a POST resembling a Razorpay webhook hits any apps/public route
    Then 404 is returned and the CSP blocks payment-provider scripts

  @FBX-21-AT-46
  Scenario: Mirror fallback and questionnaire
    Given OH14.6 unreachable
    Then the tenant screens serve the last published set read-only with the mirror age
    When a tenant uploads a SIG-Lite questionnaire
    Then the released response becomes a per_tenant questionnaire_response

Feature: Consent, marketing, WhatsApp, feedback, tutorials
  @FBX-21-AT-50
  Scenario: Nothing third-party before consent
    When Home loads with no consent decision
    Then the network log shows only first-party hosts and no font, map, analytics or pixel request
    When analytics consent is granted
    Then only the analytics adapter loads
    When marketing is rejected
    Then no pixel loads and a consent record exists in the ledger

  @FBX-21-AT-51
  Scenario: Tags never on authenticated routes and UTM first-party
    Given marketing consent granted on the public site
    When the user signs in and opens /app
    Then no tag manager, analytics or pixel script is present
    When a visitor arrives with utm_source and submits Contact
    Then the submission carries the UTM fields and no third-party identifier

  @FBX-21-AT-52
  Scenario: WhatsApp CTA only
    When the WhatsApp button is clicked
    Then the opt-in notice shows before wa.me opens
    When an editor tries to create a WhatsApp template or broadcast from the Studio
    Then no such function exists and mkt.whatsapp.enabled is false by default

  @FBX-21-AT-55
  Scenario: Feedback widget routing and scope
    When a tenant user reports a bug with a screenshot
    Then the item is tenant-scoped, the payload to SUPPORT carries no PII beyond the reporter's work e-mail, the correlation id is attached and the submitter sees its status
    When tenant B's admin lists feedback
    Then tenant A's items are absent

  @FBX-21-AT-56
  Scenario: Tutorials, tours, captions and help centre
    When a tutorial video without a VTT file is published
    Then IPB-TUT-003 and FBX-CMS-008 are returned
    When a tour runs on the Origination screen
    Then it is keyboard-operable, dismissible and does not block the sanction action
    Then /help renders articles, the public glossary from hlp.fbx.* and an Ask Vidhi entry only for authenticated users with AI enabled

Feature: Accessibility and operations
  @FBX-21-AT-57
  Scenario: axe and assistive technology
    When axe-core runs on every public template and Studio screen
    Then zero critical issues remain
    And the keyboard-only and screen-reader scripts complete Contact, resource download and a Studio publish

  @FBX-21-AT-58
  Scenario: Localisation
    When /pricing?hl=hi loads
    Then shell, footer, CMP and page copy render in Hindi with self-hosted Indic fonts

  @FBX-21-AT-59
  Scenario: Preview environment parity
    When the PR preview builds apps/public
    Then it uses the demo pack, mocked OH ports, no analytics adapters and noindex, and the Lighthouse, axe and network assertions run against it

  @FBX-21-AT-60
  Scenario: Policy versions and re-acceptance
    When PLT_LEGAL_REVIEWER publishes Terms v2 flagged re-acceptance
    Then apps/web prompts users on next sign-in and the consent records reference the new text id
```

---

## 10. Exit gate

- [ ] All M requirements FBX-21-01…90 evidenced; AT-01…60 pass in CI with output in the PR.
- [ ] Claims Register lint, legal-review gate, footer validator, contrast guard, SVG sanitiser, upload sniffing/AV, SSRF guard, CSP, host-header defence and consent gating each demonstrated with a failing fixture.
- [ ] Regulatory-text guard-rail test (`FBX-BRD-001`) byte-identical under the demo white-label pack for KFS, sanction letter and statement.
- [ ] Trust Centre and Pricing read from registries only; Investors default off with the locked disclaimer; WhatsApp CTA only.
- [ ] All eighteen IPB-05 pages published with Finbyx inserts and counsel sign-off records (or an open item per unsigned template with owner and default-off visibility).
- [ ] Lighthouse accessibility 100 and performance ≥ 90; axe zero critical; captions on every video; Hindi shell.
- [ ] Settings nodes 7, 16, 17, 18, 19, 20 registered with `ipb_node`; all keys registered; `hlp.fbx.web.*` published; Appendix G navigation test passes.
- [ ] Owner decisions recorded: Appendix B items 57–63; `[COUNSEL]` items (footer disclaimer, Investors disclaimer, policy inserts, resale wording, grievance applicability) logged as open items with owners if unresolved.
- [ ] `docs/web/` complete; `docs/plans/fbx/21.md` linked from the `cc/21-public-website-studio` PR with the IPB files read; docs/status and ADRs (CMS, brand resolution, consent ledger) updated.
