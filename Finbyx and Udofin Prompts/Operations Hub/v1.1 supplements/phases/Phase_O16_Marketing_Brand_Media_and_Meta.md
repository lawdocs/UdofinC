# Phase O16 — Marketing, Brand, Media and Meta (module OH17) *(v1.1)*

**Infrabyx Operations Hub — phase file v1.1 · 26 October 2026** · Companion to `Infrabyx_Operations_Hub_Master_Prompt_ClaudeCode_v1.1.md` (Part 9 Phase O16; module section reproduced below) and `Infrabyx_Operations_Hub_Phase_Runbook_v1.1.md` (paste block for Phase O16). Product code `OH`. Precedence: master prompt → IPB v1.0 → Ecosystem Specification v1.2 → this phase file → appendices. This file restates the module so one Claude Code session can work from a single document; where this file and the master prompt differ, the master prompt prevails and this file is corrected in the same pull request.

## 1. Phase card

| Item | Value |
|---|---|
| Phase | O16 |
| Module | OH17 |
| Depends on | O3, O7, O15 |
| Branch | `cc/o16-marketing-meta` (Claude Code convention `cc/<phase>-<slug>`, IPB-09) |
| Binding IPB files | IPB-04 §04.3.10 (marketing tooling) and §04.3.9 (CMP), IPB-05 Template 18 (WhatsApp notice), IPB-10 (webhooks, proposed events), IPB-03 (IMAGE_GEN, content skills), IPB-01 (SOCIAL, ADS, WHATSAPP, TAG_MANAGER, ANALYTICS ports) |
| Binding master-prompt sections and appendices | Master prompt Parts 4.4, 4.6, 4.13, 4.14; OH3.3–3.4, OH7, OH14.6; Appendices B (decisions 12, 24, 27, 28), D, E; Ecosystem Spec v1.2 Part 14.2 |
| Owner decisions needed | See Appendix B rows named above; defaults apply where undecided and are listed in the specification |
| Session rule | Read `docs/ipb/00_README.md` first; write the specification; stop for approval; build in small commits; never claim an unrun test |
| Product scope | Every table in this phase carries `legal_entity_id` and `product_scope` with forced RLS and Cerbos policies (Part 3.3A); the acceptance test "an FBX-scoped RM cannot read an LD client ticket" is part of every review gate |

## 2. Module specification (verbatim from the master prompt) — OH17. Marketing, Brand, Media and Meta (calendar, publishing, WhatsApp and Meta Business, ads, DAM, attribution, SEO, reputation, lead routing) *(v1.1)*

**Purpose.** Complete the marketing operating system that OH7 began. OH7 keeps the brand library, content approval workflow, claims gate, influencer register, PR and the ads register; OH17 adds the execution layer: a group content calendar across products, social publishing through adapters, **WhatsApp and Meta Business** behind a super-admin toggle, campaign and ads management through Meta, Google and LinkedIn adapters, a digital asset manager with image generation behind the `IMAGE_GEN` port, webhooks, tag management, UTM capture and attribution, SEO tooling, review and reputation monitoring, lead routing to product scopes, and marketing analytics. Every asset passes the OH7.5 and OH14.6 claims gate and the IPB-08 Claims Register rule; every send passes the OH3.4 send gate; all of it respects product-scope segregation (Part 3.3A) and the Equator commercial separation (Part 4.4).

**Users.** Marketing, design and content staff per product scope; social media managers; PR; performance marketers; brand owners (approvers); legal reviewer (claims); DPO (consent); sales (lead routing); leadership (aggregate analytics); Vidhi (`oh.content_draft`, `oh.social_caption`, L1).

**Requirement codes.** `DPDP` ss.5–8 (consent; withdrawal; notice); `TRAI` TCCCPR 2018 as amended 2025 (SMS and voice; OTT policy stance in Part 4.13); `ASCI` Code and influencer guidelines; `CCPA` Guidelines 2022 and Dark Patterns 2023; Copyright Act 1957 (licensed assets) [REC]; Trade Marks Act 1999 (brand marks) [REC]; Meta, Google, LinkedIn, X and YouTube developer and advertising policies [VEND; VERIFY each]; `OUT` paras 46, 49–50 and RBC Directions Chapter IIIA for RE-facing content (Part 4.6); SEBI restrictions where content touches investments [VERIFY]. Identifiers `REQ-OH17-nn`.

**Data owned.** Content items, calendar, assets and licences, campaign and ad metadata and spend aggregates, template registry (WhatsApp), consent references (the consent ledger itself is OH3), attribution records keyed to anonymous consent ids, review and mention metadata. Never: borrower or client-customer data, scraped profiles, hashed identifiers without marketing consent.

### OH17.1 Data model (additions to OH7.1)

| Entity | Key fields |
|---|---|
| `content_calendar_entry` | legal entity, `product_scope`, brand, channel(s), content item ref, campaign ref, planned at, owner, state (IDEA, PLANNED, IN_PRODUCTION, IN_REVIEW, APPROVED, SCHEDULED, PUBLISHED, FAILED, RETIRED), claims check result |
| `channel_account` (OH7.1 reuse) | platform (LINKEDIN, X, INSTAGRAM, FACEBOOK, YOUTUBE, WHATSAPP_CHANNEL, GOOGLE_BUSINESS), brand, product scope, owner (company-owned, Appendix B decision 12), OAuth token ref (SECRETS), scopes granted, health, quality rating (WhatsApp) |
| `publish_job` (OH7.1 reuse) | content item, channel account, scheduled at, adapter, state, platform post id, error class, retries |
| `waba` | Meta Business id, WhatsApp Business Account id, phone number ids, display names, brand, product scope, BSP or Cloud API, verification state, messaging limit tier, quality rating |
| `message_template` | WABA, name, language, category (MARKETING, UTILITY, AUTHENTICATION), components (header, body with variables, footer, buttons), state (DRAFT → INTERNAL_REVIEW → SUBMITTED → APPROVED \| REJECTED (reason) → PAUSED \| DISABLED), Meta template id, quality, claims check, owner, legal reviewer, version |
| `broadcast` | WABA, template, audience snapshot (consent-filtered, DND-scrubbed), scheduled at, state, counts (sent, delivered, read, replied, opted out, failed), cost class |
| `conversation` | WABA, contact ref (OH3), direction, window state (customer-service 24-hour), category, assignment (support or sales queue by scope), last message at; message bodies retained per OH3 class |
| `ctwa_ad` and `lead_form` | ad account ref, campaign, destination WABA or form, consent text version, fields, leads received, routing rule |
| `whatsapp_channel` | channel id, brand, admins, posts (content items), follower count (aggregate only) |
| `ad_account` | platform (META, GOOGLE, LINKEDIN), account id, brand, product scope, owner, token ref, currency, spend cap |
| `campaign` (OH7.1 reuse) | plus objective, budget, flight dates, UTM set, audiences (saved, consent-filtered custom audiences only where consent recorded), ad sets or groups, creatives (asset refs), status, spend to date (aggregate), results (aggregate) |
| `asset` (DAM) | file (hash, AV, type), kind (image, video, audio, document, logo, template), brand, product scope, licence (source, rights, expiry, model release flag), tags, alt text, variants (sizes), `synthetic` flag with generator, prompt hash and C2PA manifest ref, approval state, usage log |
| `image_gen_request` | prompt (scrubbed), adapter, cost, output asset refs, reviewer, decision, labelling applied |
| `webhook_endpoint` and `webhook_delivery` | event types, URL (EGRESS allow-list), secret ref, Standard Webhooks signature, retries, DLQ |
| `tag_container` | adapter (`none`, `gtm_web`, `gtm_server`), container id, consent mode defaults, tags inventory, approval |
| `touch_record` | anonymous consent id, first-touch and last-touch (`utm_*`, `gclid`, `fbclid`, `li_fat_id`, `msclkid`), landing route, timestamp, brand, product scope |
| `attribution_result` | lead or sign-up ref, model (first touch, last touch, linear), touches, campaign refs, computed at |
| `seo_check_run` and `seo_issue` | route, issue class, severity, owner, state |
| `review_source` and `review_item` | platform (Google Business, app stores, G2-type directories, social mentions via official APIs), brand, rating, text (public), sentiment (Vidhi suggestion), response draft, state, assignee |
| `lead_routing_rule` | conditions (product interest, form, UTM, geography, size), target product scope and queue, SLA, fallback |
| `marketing_metric_snapshot` | campaign, channel, period, aggregates (reach, engagement, clicks, leads, cost, pipeline influenced from OH3) |

### OH17.2 Content calendar and social publishing

- **REQ-OH17-01 Group calendar** with lanes per product scope and brand, channel filters, campaign colour, and claims status; a group marketer under `GRP` sees all lanes as aggregates and opens items only in scopes held; Equator's lane is visible only within Equator and never shares a campaign, discount or bundle with another product (Part 4.4).
- **REQ-OH17-02 Workflow** uses OH7.2 (brief → draft → review → legal and claims → approved → scheduled → published) with maker-checker and the claims gate as a blocking step; a content item with a `BLOCKED` claims result cannot be scheduled; an approved item re-enters review if its text changes.
- **REQ-OH17-03 Publishing adapters** (`SocialPublisher` port, IPB-01): LinkedIn (organisation pages), X, Instagram and Facebook (Meta Graph API), YouTube (uploads and community posts), Google Business Profile posts, WhatsApp Channels (OH17.3); official APIs only, company-owned accounts with OAuth tokens in SECRETS, token health monitored; no scraping, no personal accounts, no automation that violates platform terms [VEND; VERIFY each platform's current API access and terms].
- **REQ-OH17-04 Scheduling** respects a brand's publishing window; a failed publish retries with back-off and then alerts the owner with the platform error class; a post published outside the Hub is imported as a `PUBLISHED` item for completeness (metrics only, not editable).
- **REQ-OH17-05 Social inbox** (OH7.4 reuse) classifies comments and messages (lead, support, complaint, spam, press) and routes to the right queue by product scope; commenter data limited to handle and public text; a complaint about a product client's customer (for example a borrower) is forwarded under OH6.5 rules and never answered publicly.
- **REQ-OH17-06 Vidhi** (`oh.content_draft`, `oh.social_caption`, L1) drafts from a brief, the brand voice guide and the Claims Register; drafts carry the AI label internally; publication is always human (locked list).
- **REQ-OH17-07 Accessibility of content:** alt text on every image, captions on every video (IPB-06), no text-only-in-image claims, contrast-checked brand templates.

### OH17.3 WhatsApp and Meta Business (behind `mkt.meta.enabled`)

- **REQ-OH17-08 Toggle.** `mkt.meta.enabled` (Platform, default `false`, super admin with CISO checker) gates every Meta capability: WABA onboarding, templates, broadcasts, conversations, Click-to-WhatsApp ads, lead forms, WhatsApp Channels, Meta pixel and conversions API. Off means no outbound action, no template submission, no ad sync; inbound conversations stay readable for 30 days. Per-brand WABA mapping; a brand without a verified WABA cannot send.
- **REQ-OH17-09 Templates with approval workflow.** `DRAFT → INTERNAL_REVIEW (claims gate, brand, legal) → SUBMITTED (to Meta) → APPROVED | REJECTED (reason) → PAUSED | DISABLED`; category is chosen by content, with the rule "any promotional element = MARKETING"; utility templates may not contain promotion; the template registry is the group's single source and emits the proposed `in.infrabyx.messaging.WhatsAppTemplateApproved.v1` so other products using the WABA see status (IPB-10); Meta's quality rating and pacing changes are mirrored and a `PAUSED` template is blocked from broadcasts.
- **REQ-OH17-10 Consent-based broadcasts.** Audience = contacts with a current WhatsApp marketing opt-in in the OH3 consent ledger (channel-specific), minus opt-outs, DND policy scrub and frequency cap (`mkt.whatsapp.max_marketing_per_week`, default 1 [REC]); the send gate (OH3.4) evaluates every recipient and records refusals; broadcasts need maker-checker; utility messages (ticket update, invoice link, meeting reminder) go to existing clients and users only and carry no promotion; every message carries an opt-out instruction where Meta requires it; STOP replies write a withdrawal to the ledger within one minute and propagate `MarketingConsentUpdated` (proposed IPB-10 event).
- **REQ-OH17-11 Conversations.** Inbound messages open or continue a conversation routed by product scope to support (OH6) or sales (OH3) queues; the 24-hour customer-service window is tracked; free-form replies only inside the window; outside it, approved utility templates only; agents never request Aadhaar, PAN, card or account details on WhatsApp (DLP on outbound; refusal with reason); media attachments are AV-scanned; conversation retention per OH3 class.
- **REQ-OH17-12 Click-to-WhatsApp ads and lead forms.** Ads created through the Meta ads adapter with the destination WABA; lead forms carry the IPB-05 Template 18 WhatsApp notice and purpose-specific consent checkboxes (unticked by default; no dark patterns); leads land in OH3 with consent receipt, source and UTM, and route by `lead_routing_rule` (OH17.8).
- **REQ-OH17-13 WhatsApp Channels.** Channel posts are content items through the OH7.2 workflow and the claims gate; follower analytics are aggregate only.
- **REQ-OH17-14 Meta pixel and conversions API** fire only after `marketing` consent (CMP), only on public marketing routes, never with hashed personal identifiers unless the lead gave marketing consent recorded in the ledger (IPB-04-87); server-side events pass through the tag container with IP truncation.
- **REQ-OH17-15 Cost and compliance.** Conversation-category costs are metered to the product scope and brand (OH8 intra-group recharge); Meta policy violations, quality drops and account restrictions are incidents on the marketing dashboard with an owner and a 2-working-day review [REC].
- **REQ-OH17-16 Abuse controls.** Template variables are validated against a schema (no free-text injection of links or claims); a template body cannot be changed after approval (new version); broadcast audiences are frozen snapshots; rate limits per WABA follow Meta tiers; a broadcast exceeding the tier is split or refused; an agent cannot send a marketing template inside a service conversation.

### OH17.4 Campaign and ads management

- **REQ-OH17-17 Adapters** for Meta Marketing API, Google Ads API and LinkedIn Marketing API (`AdsProvider` port; mock first, then sandbox; official APIs, company ad accounts, OAuth tokens in SECRETS) read campaigns, ad sets, ads, spend and results, and **write** only approved campaign structures and status changes (pause, resume) under maker-checker; creative publication goes through the claims gate and brand approval.
- **REQ-OH17-18 Audiences.** Saved audiences by interests and geography; custom audiences from Hub contacts only where each contact has recorded marketing consent for the channel (hash upload after consent check; IPB-04-87); lookalike audiences allowed from consented seeds only; no audience built from client-customer data (borrowers, members) ever (Part 2.3).
- **REQ-OH17-19 Budget controls.** Spend caps per account and campaign; alerts at 80% and 100%; a campaign without a DoA-approved budget cannot be activated; spend reconciles to vendor invoices in OH8 and OH11.
- **REQ-OH17-20 RE-facing content.** Any campaign naming a client RE or promoting a loan product needs that RE's written approval record attached and follows RBC Chapter IIIA (Part 4.6) [VERIFY]; the Hub never runs borrower marketing on behalf of an RE.
- **REQ-OH17-21 Experiments.** A/B variants are approved revisions with an owner, hypothesis, end date and one primary metric; no experiment on consent text, pricing figures or legal pages (IPB-04-90).

### OH17.5 Digital asset management and image generation

- **REQ-OH17-22 DAM.** Assets with hash, AV scan, type sniffing (SVG sanitised), size limits, EXIF stripped (MEDIA port), brand and scope, licence record (source, rights, expiry, model or property release), alt text mandatory, variants generated, usage log (where published); expired licences block new use and flag live uses; the OH7.3 brand library becomes the `logo` and `template` kinds of the DAM.
- **REQ-OH17-23 Image generation** through the `IMAGE_GEN` port (reference `gemini_imagen`; alternatives per IPB-03; Appendix B decision 28; IPB README open item 6): prompts are scrubbed of personal data, brand prompts come from approved templates; outputs are `synthetic = true`, carry a C2PA manifest where the adapter supports it [VERIFY], an invisible provenance marker and a visible "AI-generated image" label where published in marketing (ASCI synthetic-media expectations [VERIFY: ASCI guidance on AI-generated advertising content]); **human approval is mandatory before any synthetic image is published** (default and floor); no generation of real people's likenesses, regulator logos, certification marks or client marks; prompts and outputs are logged with cost to the scope.
- **REQ-OH17-24 Brand consistency.** Templates for each brand (colour tokens from Brand Studio, OH18.2) with contrast guard; a creative outside brand tokens needs brand-owner approval.

### OH17.6 Webhooks, tag management, UTM and attribution

- **REQ-OH17-25 Webhooks.** Standard Webhooks v1 signatures on outbound events (`lead.created`, `content.published`, `campaign.status_changed`, `whatsapp.template_status`), endpoints on the EGRESS allow-list, retries with back-off and a DLQ in `Marketing › Integrations`; inbound webhooks (Meta, Google, LinkedIn, Brevo) verified by signature or app secret and de-duplicated.
- **REQ-OH17-26 Tag management** through `TAG_MANAGER` (adapters `none` default, `gtm_web` with Consent Mode v2 defaults denied, `gtm_server` first-party with IP truncation and redaction); one container per brand pack; every tag has an owner, purpose, consent category and approval; a tag that fires before consent fails the CI consent test (IPB-04-79, IPB-04-85). Owner decision: Appendix B decision 27 (IPB README open item 5).
- **REQ-OH17-27 UTM and click ids** captured server-side on first request, stored against the anonymous consent id under the `functional` category, attached to leads and sign-ups, flowing to OH3 (IPB-04-88); UTM taxonomy enforced by a builder (source, medium, campaign, content, term) with a registry per product scope.
- **REQ-OH17-28 Attribution** models (first touch, last touch, linear) computed in the Hub from touch records and OH3 lead and opportunity stages; reports are aggregate; no cross-device identity stitching without consent; pipeline influence shown by campaign and channel.

### OH17.7 SEO tooling and review or reputation monitoring

- **REQ-OH17-29 SEO** nightly checks on the group site and, by adapter, product sites (broken links, orphans, missing alt, duplicate titles, canonical, thin pages, Core Web Vitals lab and field, sitemap and robots, structured data, redirect chains) with owner assignment (IPB-04-91); keyword and ranking data through an official search-console adapter per brand (read-only); content briefs for OH16 notebooks; no link schemes or scraped SERP data.
- **REQ-OH17-30 Reviews and mentions** from official sources only (Google Business Profile API, app stores where applicable, directories that provide an API, owned social accounts); public text and rating stored; Vidhi suggests sentiment and a response draft (L1); responses go through the OH7.2 workflow; a review alleging a client-customer issue is treated as a complaint under OH6.5; no incentivised or fabricated reviews (ASCI; CCPA); review solicitation only to consented contacts.
- **REQ-OH17-31 Reputation incidents** (viral complaint, press enquiry, impersonation) open an OH13 incident or OH7.7 PR case with a comms owner.

### OH17.8 Lead routing and marketing analytics

- **REQ-OH17-32 Routing rules** evaluate form, product interest, UTM, geography and size to assign a lead to a product scope and queue (sales or partnerships) with an SLA (`mkt.lead.first_touch_sla_hours`, default 4 working hours [REC]) and a fallback; the lead carries consent receipt, touches and brand; Equator leads never route to lender-side sales and never inform any other product's pipeline (Part 4.4); a lead for a product the Hub does not sell (a group company without a scope) goes to `GRP` triage.
- **REQ-OH17-33 Analytics** (OH2 metric layer): reach, engagement, publish cadence, campaign spend and results by channel, cost per lead, lead-to-opportunity by source, template approval times, WhatsApp quality and opt-out rates, consent coverage, SEO health, review sentiment trend; all by product scope with group aggregates; no per-person marketing performance metric outside the team view.
- **REQ-OH17-34 Events (`oh` scope):** `in.oh.mkt.ContentPublished.v1`, `in.oh.mkt.BroadcastSent.v1` (counts), `in.oh.mkt.LeadRouted.v1`, `in.oh.mkt.TemplateStateChanged.v1`; proposed Ecosystem: `WhatsAppTemplateApproved`, `MarketingConsentUpdated` (consumer and producer), `BlogPostPublished` (consumer), `LeadCaptured` (consumer) — Part 6.2A.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| `mkt.meta.enabled` | Platform | `false` | Commercial (super admin maker, CISO checker); off stops all Meta actions |
| `mkt.meta.waba_map` | Brand | None | Regulated (legal, DPO) |
| `mkt.whatsapp.max_marketing_per_week` | Brand | 1 [REC] | Floor (maximum; may lower) |
| `mkt.whatsapp.utility_recipients` | Platform | Existing clients and users only | Floor |
| `mkt.template.category_rule` | Platform | Any promotion = MARKETING | Floor |
| `mkt.social.publishing_window` | Brand | 09:00–21:00 IST | Commercial |
| `mkt.social.accounts` | Brand | Company-owned only (Appendix B decision 12) | Floor |
| `mkt.ads.spend_cap` | Account, campaign | DoA budget | Floor: no activation without budget |
| `mkt.audience.custom_requires_consent` | Platform | `true` | Floor |
| `mkt.image_gen.human_approval` | Platform | `true` | Floor |
| `mkt.image_gen.adapter` | Platform | Per Appendix B decision 28 | Commercial |
| `mkt.image_gen.label_text` | Brand | "AI-generated image" | Regulated (legal) |
| `mkt.tag_manager.adapter` | Brand pack | `none` | Commercial (decision 27); consent gating is a Floor |
| `mkt.utm.taxonomy` | Scope | Registry per scope | Commercial |
| `mkt.attribution.models` | Platform | first, last, linear | Commercial |
| `mkt.lead.first_touch_sla_hours` | Scope | 4 working hours [REC] | Commercial |
| `mkt.reviews.sources` | Brand | Official APIs only | Floor |
| Claims gate on assets and templates | Platform | On | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Marketing › Calendar` (extends OH7) | Group calendar by scope, brand and channel; drag to reschedule (re-review if text changed); claims status badges | Marketing per scope; `GRP` aggregate |
| `Marketing › Publishing` | Channel accounts and token health; publish queue; failures and retries; imported posts | Social media managers |
| `Marketing › WhatsApp and Meta` (visible only when `mkt.meta.enabled`) | WABA status and quality; template registry with workflow and Meta status; broadcasts with audience preview and send-gate refusals; conversations inbox by scope with window timer; Channels; Click-to-WhatsApp and lead forms; cost by scope | Marketing, support and sales (conversations), legal (templates), super admin (toggle) |
| `Marketing › Campaigns and ads` | Campaign builder with objective, budget (DoA), UTM set, audiences (consent-checked), creatives (claims-gated); ad account sync; spend alerts; experiments | Performance marketers, brand owners, finance (budgets) |
| `Marketing › Assets` (DAM) | Library by brand and scope; upload with sanitisation; licences and expiry; alt text; variants; image-generation studio with approval queue and labelling; usage log | Design, marketing, brand owners |
| `Marketing › Integrations` | Webhooks (endpoints, deliveries, DLQ); tag containers and tag inventory with consent categories; UTM builder and registry; attribution settings | Marketing operations, CISO (allow-list) |
| `Marketing › SEO` | Nightly check results with owners; search-console data; content brief hand-off to Knowledge | Content, SEO |
| `Marketing › Reputation` | Review and mention inbox; sentiment suggestions; response drafts through workflow; complaint forwarding | Marketing, support |
| `Marketing › Leads` | Routing rules; routed leads with SLA; fallbacks; Equator separation check | Marketing operations, sales leads |
| `Marketing › Analytics` | Dashboards by scope and channel; attribution; consent coverage; template quality | Marketing leads, leadership (aggregate) |

Empty and error states: with `mkt.meta.enabled` off, the WhatsApp menu is hidden and any API call returns `meta_disabled` with the decision reference; a broadcast with refusals lists each refusal reason (no consent, opted out, DND, frequency cap, template paused); a synthetic image without approval cannot be attached to a content item.

### Acceptance tests

- With `mkt.meta.enabled = false`, no template submission, broadcast, ad sync or pixel event occurs (negative API and UI tests); turning it on requires a CISO checker; turning it off mid-broadcast stops remaining sends.
- A template containing a discount sentence cannot be submitted as `UTILITY`; an approved template's body cannot be edited in place; a template `PAUSED` by Meta is excluded from broadcasts.
- A broadcast audience excludes a contact who opted out of WhatsApp marketing yesterday, a contact with only e-mail consent, and a contact who received a marketing message this week; a STOP reply writes a withdrawal within one minute and the contact is excluded from the next broadcast.
- An agent cannot send a marketing template inside a service conversation; an outbound message asking for a PAN is refused with `dlp_blocked`.
- A custom audience upload is refused for contacts without channel marketing consent; a lookalike seed containing a non-consented contact is refused; an attempt to build an audience from a client's borrower list fails schema validation (no such source exists).
- A Meta pixel on a public page fires no request before consent (CI test loads every public route with no consent and asserts zero third-party requests); hashed identifiers are sent only for consented leads.
- A synthetic image cannot be published without human approval; the published image carries the visible label and provenance marker; a prompt naming a real public figure is refused.
- An Equator lead never routes to a lender-side queue and never appears in any other scope's pipeline report; an FBX marketer cannot open an LD campaign.
- UTM parameters on a first request create a first-touch record keyed to the anonymous consent id without any client-side storage before consent; the resulting lead in OH3 shows first and last touch.
- A content item whose text changes after approval returns to review; an item with a `BLOCKED` claims result cannot be scheduled; "RBI approved" in a caption is blocked.
- A review that alleges a borrower's grievance is forwarded under OH6.5 and never answered publicly from the Hub.


## 3. Instruction to Claude (from master prompt Part 9)

> **Instruction to Claude:** "Read docs/ipb/00_README.md, then IPB-04 §04.3.10 (marketing tooling), IPB-05 Template 18 and IPB-10 before the plan. Verify first: (i) Meta WhatsApp Business Platform policies, template categories, pacing and quality rules, Cloud API versus BSP (Appendix B decision 24); (ii) Meta Marketing API, Google Ads API and LinkedIn Marketing API access tiers and review requirements; (iii) the platform APIs for LinkedIn, X, Instagram, Facebook, YouTube and Google Business Profile publishing; (iv) ASCI guidance on AI-generated content and the C2PA support of the chosen image adapter (decision 28); (v) GTM Consent Mode v2 and server-side tagging options (decision 27); (vi) TRAI's current position on OTT commercial communications.
>
> On branch `cc/o16-marketing-meta` build OH17 (master prompt OH17; phase file `Phase_O16_Marketing_Brand_Media_and_Meta.md`):
>
> - **Calendar and publishing:** group calendar by scope and brand; OH7.2 workflow with blocking claims gate and re-review on text change; `SocialPublisher` adapters (LinkedIn, X, Instagram, Facebook, YouTube, Google Business Profile, WhatsApp Channels), mock first; publish queue, retries, imports; social inbox routing by scope; Vidhi `oh.content_draft` and `oh.social_caption` at L1.
> - **WhatsApp and Meta behind `mkt.meta.enabled` (default off; CISO checker):** WABA registry, template workflow with category rule and Meta status mirror, consent-based broadcasts through the OH3 send gate with frequency cap and frozen audiences, STOP handling within a minute, conversations with the 24-hour window and outbound DLP, Click-to-WhatsApp ads and lead forms with Template 18 notice, Channels, pixel and conversions API consent-gated, cost metering by scope, abuse controls (schema-validated variables, immutable approved bodies, tier limits).
> - **Campaigns and ads:** `AdsProvider` adapters (Meta, Google, LinkedIn) with read of spend and results and maker-checker writes; consent-checked custom audiences; DoA budgets and spend alerts; RE-facing approvals; experiments rules.
> - **DAM and image generation:** assets with sanitisation, licences, alt text and variants; `IMAGE_GEN` port with scrubbed prompts, synthetic labelling, C2PA where supported, mandatory human approval (floor), prohibited subjects; brand templates with contrast guard.
> - **Webhooks, tags, UTM, attribution:** Standard Webhooks out, verified webhooks in, DLQ; `TAG_MANAGER` adapters (`none` default) with per-tag consent category and the zero-third-party-request CI test; server-side UTM and click-id capture under `functional` consent; attribution models.
> - **SEO and reputation:** nightly checks with owners; search-console adapter; official review sources only; Vidhi sentiment and response drafts; complaint forwarding under OH6.5.
> - **Lead routing and analytics:** rules by scope with SLA and Equator separation; marketing dashboards on the OH2 metric layer by scope with group aggregates.
> - **Menus, screens and settings:** the `Marketing` menu additions and OH17 settings exactly as the OH17 tables specify (the WhatsApp menu hidden while the toggle is off); `hlp.oh.mkt.*` keys.
>
> Tests and acceptance evidence: every OH17 acceptance test, including toggle-off negative tests, template category and immutability rules, broadcast exclusions and STOP propagation, no marketing template in a service conversation, consent-gated audiences and pixels (CI zero third-party requests before consent), synthetic-image approval and labelling, Equator lead separation, UTM first-touch without pre-consent storage, claims-gate blocks.
>
> Show me the adapter list and mock plan, the template and broadcast state machines, the consent evaluation flow, the tag and pixel consent design and the asset licence model for approval before coding."

**Exit gate:** OH17 tests green; `mkt.meta.enabled` off at close; consent CI test in the required checks; DPIA for marketing data; claims-gate coverage report for every asset path.

## 4. Build notes for Claude Code

### 4.1 Sub-module plan (one session each)

| Session | Scope | Depends on | Exit evidence |
|---|---|---|---|
| O16a | `mkt` schema additions; group calendar; OH7.2 workflow binding with blocking claims gate and re-review on text change; `SocialPublisher` port with mock adapter and the LinkedIn, X, Instagram, Facebook, YouTube, Google Business Profile and WhatsApp Channels adapters (sandbox where available); publish queue; social inbox routing by scope; `oh.content_draft` and `oh.social_caption` manifests | O7, O15 | Calendar scope tests; workflow re-review test; adapter contract tests against mocks |
| O16b | WhatsApp and Meta behind `mkt.meta.enabled`: WABA registry, template workflow, Meta webhook verification (`X-Hub-Signature-256`), broadcasts with send-gate evaluation and frozen audiences, STOP handling and `MarketingConsentUpdated`, conversations with window timer and outbound DLP, CTWA and lead forms, Channels, pixel and conversions API consent gating, cost metering, abuse controls | O16a, O3 | Toggle-off negative suite; template and broadcast state tests; consent exclusion tests |
| O16c | Campaign and ads: `AdsProvider` port with Meta, Google and LinkedIn adapters (read spend and results; maker-checker writes), consent-checked audiences, DoA budgets and alerts, RE-facing approval attachment, experiments | O16a, O6 | Audience consent tests; budget activation block |
| O16d | DAM and image generation: asset model with sanitisation, licence and alt text; `IMAGE_GEN` port (mock and `gemini_imagen`), scrubbed prompts, synthetic labelling, C2PA where supported, approval queue, prohibited-subject filter; brand templates with contrast guard | O16a | Upload abuse tests; approval floor test; label render test |
| O16e | Webhooks (Standard Webhooks out; verified in; DLQ), `TAG_MANAGER` adapters with consent categories, server-side UTM and click-id capture, attribution models | O16a, O17 CMP (or the OH18 CMP stub) | CI zero-third-party test; UTM first-touch test |
| O16f | SEO checks and search-console adapter; reviews and mentions from official sources with Vidhi sentiment; reputation incidents; lead routing rules with SLA and Equator separation; marketing metrics on the OH2 layer | O16a–O16e | Routing tests; metric scope tests |

### 4.2 API surface (`/v1/mkt/...`)

| Method and path | Purpose | Authorisation |
|---|---|---|
| `GET/POST /v1/mkt/calendar` | Calendar entries by scope, brand, channel, state | Marketing per scope; `GRP` aggregate |
| `POST /v1/mkt/content/{id}:schedule`, `:publish`, `:retire` | Scheduling and publishing through adapters (claims gate must be PASS) | Approved items; maker-checker |
| `GET/POST /v1/mkt/channel-accounts`, `POST …/{id}:reauthorise` | Company-owned accounts and token health | Social managers; CISO for allow-list |
| `GET /v1/mkt/inbox`, `POST /v1/mkt/inbox/{id}:route` | Social inbox classification and routing | Marketing, support |
| `GET/POST /v1/mkt/wabas`, `GET/POST /v1/mkt/templates`, `POST /v1/mkt/templates/{id}:transition` | WABA registry; template workflow (submit to Meta on `SUBMITTED`) | Requires `mkt.meta.enabled`; legal reviewer at INTERNAL_REVIEW |
| `POST /v1/mkt/broadcasts`, `POST /v1/mkt/broadcasts/{id}:freeze`, `:send`, `:stop` | Broadcasts with send-gate evaluation and refusal list | Maker-checker; `mkt.meta.enabled` |
| `GET /v1/mkt/conversations`, `POST /v1/mkt/conversations/{id}/messages` | Conversations within the 24-hour window; outbound DLP; template-only outside the window | Support and sales by scope |
| `POST /v1/mkt/webhooks/meta`, `/google`, `/linkedin`, `/brevo` | Verified inbound webhooks (signature, de-duplication) | Public endpoint with verification |
| `GET/POST /v1/mkt/campaigns`, `POST /v1/mkt/campaigns/{id}:activate\|pause` | Campaigns and ads (DoA budget required to activate) | Performance marketers; finance for budgets |
| `POST /v1/mkt/audiences`, `POST /v1/mkt/audiences/{id}:sync` | Consent-checked audiences; hash upload after consent check | Marketing; DPO visibility |
| `GET/POST /v1/mkt/assets`, `POST /v1/mkt/assets/{id}:approve` | DAM with sanitisation and licences | Design, brand owners |
| `POST /v1/mkt/image-gen`, `POST /v1/mkt/image-gen/{id}:approve\|reject` | Image generation with mandatory approval | Design; brand owner approval |
| `GET/POST /v1/mkt/webhook-endpoints`, `GET /v1/mkt/webhook-deliveries` | Outbound webhooks and DLQ | Marketing operations; CISO allow-list |
| `GET/POST /v1/mkt/tags` | Tag inventory with consent categories and approvals | Marketing operations, DPO |
| `POST /v1/mkt/touch` (server-side, from `apps/public`) | UTM and click-id capture against the consent id | Internal |
| `GET /v1/mkt/attribution` | Attribution results (aggregate) | Marketing leads |
| `GET /v1/mkt/seo/issues`, `GET/POST /v1/mkt/reviews`, `POST /v1/mkt/reviews/{id}:respond` | SEO issues; reviews with workflow responses | Content, SEO, marketing |
| `GET/POST /v1/mkt/lead-routing-rules` | Routing rules with SLA and fallback | Marketing operations, sales leads |
| `GET /v1/mkt/metrics` | Governed marketing metrics by scope | Marketing leads; leadership aggregate |

Errors: `mkt/meta_disabled`, `mkt/template_category_invalid`, `mkt/template_immutable`, `mkt/template_paused`, `mkt/consent_missing`, `mkt/opted_out`, `mkt/frequency_cap`, `mkt/dnd_scrubbed`, `mkt/window_closed`, `mkt/marketing_in_service_conversation`, `mkt/dlp_blocked`, `mkt/audience_consent_missing`, `mkt/audience_source_invalid`, `mkt/budget_required`, `mkt/spend_cap_reached`, `mkt/re_approval_required`, `mkt/claims_blocked`, `mkt/asset_licence_expired`, `mkt/synthetic_unapproved`, `mkt/prohibited_subject`, `mkt/tag_consent_category_missing`, `mkt/webhook_signature_invalid`, `mkt/egress_not_allowed`, `mkt/equator_separation`.

### 4.3 Settings keys registered in this phase

`mkt.meta.enabled` (false; super admin maker, CISO checker), `mkt.meta.waba_map`, `mkt.whatsapp.max_marketing_per_week` (1), `mkt.whatsapp.utility_recipients` (existing clients and users), `mkt.template.category_rule`, `mkt.social.publishing_window`, `mkt.social.accounts` (company-owned only), `mkt.ads.spend_cap`, `mkt.audience.custom_requires_consent` (true, floor), `mkt.image_gen.human_approval` (true, floor), `mkt.image_gen.adapter`, `mkt.image_gen.label_text`, `mkt.tag_manager.adapter` (none), `mkt.utm.taxonomy`, `mkt.attribution.models`, `mkt.lead.first_touch_sla_hours` (4), `mkt.reviews.sources` (official APIs), `mkt.webhooks.allowlist` (via EGRESS), `vidhi.skill.oh.content_draft.autonomy_level` (L1).

### 4.4 Events

Internal: `in.oh.mkt.ContentPublished.v1`, `in.oh.mkt.BroadcastSent.v1` (counts), `in.oh.mkt.LeadRouted.v1`, `in.oh.mkt.TemplateStateChanged.v1`, `in.oh.mkt.AssetApproved.v1`, `in.oh.mkt.SeoIssueOpened.v1`. Proposed Ecosystem (emit internally until registered): `messaging.WhatsAppTemplateApproved`, `consent.MarketingConsentUpdated` (producer and consumer), consumers `cms.BlogPostPublished`, `cms.ResourcePublished`, `crm.LeadCaptured`.

### 4.5 Help keys (minimum set)

`hlp.oh.mkt.meta_toggle`, `hlp.oh.mkt.template_category`, `hlp.oh.mkt.service_window`, `hlp.oh.mkt.channel_consent`, `hlp.oh.mkt.frequency_cap`, `hlp.oh.mkt.dnd_scrub`, `hlp.oh.mkt.custom_audience_consent`, `hlp.oh.mkt.synthetic_label`, `hlp.oh.mkt.asset_licence`, `hlp.oh.mkt.consent_mode`, `hlp.oh.mkt.utm_taxonomy`, `hlp.oh.mkt.attribution_model`, `hlp.oh.mkt.claims_gate`, `hlp.oh.mkt.equator_separation`, `hlp.oh.mkt.lead_sla`.

## 5. Acceptance tests (Gherkin)

```gherkin
Feature: Meta toggle
  @REQ-OH17-08
  Scenario: Everything Meta is inert while the toggle is off
    Given mkt.meta.enabled is false
    When any client calls POST /v1/mkt/templates, /broadcasts, /campaigns:activate for a Meta account, or a public page would load the Meta pixel
    Then the API responds 423 with type "mkt/meta_disabled" and the page makes no request to Meta hosts
    When the super admin turns the toggle on without a CISO checker
    Then the change stays pending and no Meta action is possible
  Scenario: Turning the toggle off mid-broadcast stops sends
    Given a broadcast in SENDING with 1,000 of 5,000 messages sent
    When mkt.meta.enabled is set to false
    Then the broadcast state is STOPPED and no further message is sent

Feature: Templates
  @REQ-OH17-09 @REQ-OH17-16
  Scenario: Category rule and immutability
    When a template body containing "Get 20% off" is submitted as UTILITY
    Then the response is 422 with type "mkt/template_category_invalid"
    Given an APPROVED template
    When its body is edited in place
    Then the response is 409 with type "mkt/template_immutable" and a new version is required
    Given Meta pauses the template
    When a broadcast using it is frozen
    Then every recipient is refused with "mkt/template_paused"

Feature: Consent-based broadcasts
  @REQ-OH17-10
  Scenario: Exclusions and STOP
    Given contact A opted out of WhatsApp marketing yesterday, contact B holds e-mail consent only, contact C received a marketing message this week, and contact D holds WhatsApp marketing consent
    When the audience is frozen
    Then only D is included and A, B and C appear in the refusal list with reasons opted_out, consent_missing and frequency_cap
    When D replies "STOP"
    Then a withdrawal is written to the consent ledger within 60 seconds, MarketingConsentUpdated is emitted, and D is excluded from the next freeze

Feature: Conversations
  @REQ-OH17-11
  Scenario: No marketing in a service conversation; DLP on outbound
    Given an open service conversation inside the 24-hour window
    When an agent attempts to send a MARKETING template
    Then the response is 422 with type "mkt/marketing_in_service_conversation"
    When an agent types "Please share your PAN"
    Then the message is refused with type "mkt/dlp_blocked"

Feature: Audiences
  @REQ-OH17-18
  Scenario: Consent required and no client-customer source exists
    Given a custom audience of 100 contacts of whom 3 lack channel marketing consent
    When the audience is synced
    Then 97 hashed identifiers are uploaded and 3 are refused with "mkt/audience_consent_missing"
    When an audience is requested from source type "borrower_list"
    Then the response is 422 with type "mkt/audience_source_invalid"

Feature: Pixels and tags
  @REQ-OH17-14 @REQ-OH17-26 @IPB-04-79
  Scenario: Zero third-party requests before consent
    When CI loads every public route with no consent cookie
    Then no network request leaves to any host other than the first-party CDN
    When a tag is created without a consent category
    Then the response is 422 with type "mkt/tag_consent_category_missing"

Feature: Image generation
  @REQ-OH17-23
  Scenario: Approval floor, label and prohibited subjects
    When an image is generated and attached to a content item without approval
    Then the attach fails with "mkt/synthetic_unapproved"
    When the image is approved and published
    Then the rendered asset carries the visible label and a provenance marker
    When a prompt names a real public figure or a certification mark
    Then generation is refused with "mkt/prohibited_subject"

Feature: Lead routing and Equator separation
  @REQ-OH17-32 @Part-4.4
  Scenario: Equator lead never reaches lender-side sales
    When a lead with product interest "Equator Resolution" arrives
    Then it routes to the EQ queue and appears in no other scope's pipeline report
    When a rule is created that would route EQ leads to the FBX queue
    Then the rule is refused with "mkt/equator_separation"

Feature: UTM capture
  @REQ-OH17-27 @IPB-04-88
  Scenario: Server-side first touch without pre-consent storage
    When a first request arrives with utm_source=linkedin&gclid=abc and no consent
    Then a first-touch record is stored server-side against the anonymous consent id and no client-side storage is written
    When the visitor later submits a contact form
    Then the OH3 lead shows first touch "linkedin" and last touch from the final session
```

## 6. Exit gate

- Gherkin scenarios and the OH17 acceptance list pass; the consent zero-third-party test and the toggle-off suite are required CI checks.
- `mkt.meta.enabled` is off at close; WABA, ad and social adapters are certified against mocks and sandboxes; no live credential in any non-production environment.
- DPIA for marketing data and the WhatsApp channel in `docs/privacy/`; claims-gate coverage report shows every publish path gated; `docs/status` updated; pull request merged after owner approval.

## 7. Data model sketch (schema `mkt`, additions to OH7)

```
mkt.calendar_entry(cal_id pk, legal_entity_id, product_scope, brand_id, channels text[], content_id fk, campaign_id null, planned_at, owner_id, state, claims_check jsonb)
mkt.waba(waba_id pk, meta_business_id, phone_number_ids text[], brand_id, product_scope, provider check in ('meta_cloud','bsp'), verification_state, tier, quality)
mkt.template(tpl_id pk, waba_id fk, name, language, category, components jsonb, variables_schema jsonb, state, meta_template_id null, quality, claims_check jsonb, owner_id, legal_reviewer_id, version int)   -- body immutable after APPROVED
mkt.broadcast(bc_id pk, waba_id fk, tpl_id fk, audience_snapshot_id, scheduled_at, state, counts jsonb, cost_class, maker_id, checker_id)
mkt.conversation(cv_id pk, waba_id fk, contact_ref, direction, window_opens_at, window_closes_at, category, queue_ref, product_scope, last_message_at)
mkt.message(msg_id pk, cv_id fk, direction, tpl_id null, body_ref, dlp_result jsonb, status, at)
mkt.ad_account(acc_id pk, platform, external_id, brand_id, product_scope, owner_id, token_ref, currency, spend_cap numeric)
mkt.campaign_ext(campaign_id fk oh7.campaign, objective, budget numeric, doa_request_id, flight daterange, utm_set jsonb, spend_to_date numeric, results jsonb)
mkt.audience(aud_id pk, kind check in ('saved','custom','lookalike'), definition jsonb, consent_checked_at, refused_count int)
mkt.asset(ast_id pk, brand_id, product_scope, kind, object_key, sha256, av_status, licence jsonb, alt_text not null, variants jsonb, synthetic bool, generator, prompt_hash, c2pa_ref, approval_state, approved_by)
mkt.image_gen_request(igr_id pk, prompt_scrubbed, adapter, cost, asset_ids uuid[], reviewer_id, decision, labelled bool)
mkt.webhook_endpoint(we_id pk, product_scope, url, event_types text[], secret_ref, state)
mkt.webhook_delivery(wd_id pk, we_id fk, event_id, attempt int, status, response_code, next_retry_at)
mkt.tag_container(tc_id pk, brand_pack_id, adapter, external_id, consent_defaults jsonb, approved_by)
mkt.tag(tag_id pk, tc_id fk, name, purpose, consent_category not null, owner_id, approved_by)
mkt.touch_record(tr_id pk, consent_id, kind check in ('first','last'), params jsonb, landing_route, at, brand_id, product_scope)
mkt.attribution_result(ar_id pk, lead_ref, model, touches jsonb, campaign_refs uuid[], computed_at)
mkt.review_item(rv_id pk, source_id fk, brand_id, rating, text_public, sentiment_suggestion, response_draft_id null, state, assignee_id)
mkt.lead_routing_rule(lr_id pk, conditions jsonb, target_scope, target_queue, sla_hours, fallback_queue, position)
```

All tables carry `legal_entity_id` and `product_scope` with forced RLS; `mkt.audience.definition` is validated against a schema that admits only Hub contact sources with consent predicates — no source type for client-customer data exists, which is how REQ-OH17-18 is enforced structurally rather than by policy alone.
