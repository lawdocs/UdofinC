# Phase O17 — Group website, CMS, Vendor Assurance publishing, feedback and tutorials (module OH18) *(v1.1)*

**Infrabyx Operations Hub — phase file v1.1 · 26 October 2026** · Companion to `Infrabyx_Operations_Hub_Master_Prompt_ClaudeCode_v1.1.md` (Part 9 Phase O17; module section reproduced below) and `Infrabyx_Operations_Hub_Phase_Runbook_v1.1.md` (paste block for Phase O17). Product code `OH`. Precedence: master prompt → IPB v1.0 → Ecosystem Specification v1.2 → this phase file → appendices. This file restates the module so one Claude Code session can work from a single document; where this file and the master prompt differ, the master prompt prevails and this file is corrected in the same pull request.

## 1. Phase card

| Item | Value |
|---|---|
| Phase | O17 |
| Module | OH18 |
| Depends on | O6, O12, O15, O16 |
| Branch | `cc/o17-website-trust` (Claude Code convention `cc/<phase>-<slug>`, IPB-09) |
| Binding IPB files | IPB-04 (whole file), IPB-05 (templates, inserts, footer policy list), IPB-07 §07.3.4–07.3.5 (help, tutorials, What's new), IPB-08 (whole file), IPB-06 (accessibility statement), IPB-10 (proposed trust and feedback events) |
| Binding master-prompt sections and appendices | Master prompt Parts 4.11, 4.14; OH4, OH8.9, OH14.5–14.7; Appendices B (decisions 29, 30, 31), D, E; content deck `content/OpsHub_Website_Content_v1.0.md`; design brief `design/UI_UX_Design_Brief_v1.1.md` |
| Owner decisions needed | See Appendix B rows named above; defaults apply where undecided and are listed in the specification |
| Session rule | Read `docs/ipb/00_README.md` first; write the specification; stop for approval; build in small commits; never claim an unrun test |
| Product scope | Every table in this phase carries `legal_entity_id` and `product_scope` with forced RLS and Cerbos policies (Part 3.3A); the acceptance test "an FBX-scoped RM cannot read an LD client ticket" is part of every review gate |

## 2. Module specification (verbatim from the master prompt) — OH18. Group public website, CMS, Vendor Assurance publishing, client onboarding Studio, feedback hub and tutorials *(v1.1)*

**Purpose.** Give the Infrabyx group its public face and the super-admin Studio behind it, exactly as IPB-04 prescribes, and make the Hub the **system of record for vendor assurance** (IPB-08) that every product mirrors. OH18 covers: the headless CMS for the group site (group home, about, group companies, careers, contact, trust, policies and the other IPB-04 standard pages — lean, because each product runs its own public site), Brand Studio and brand packs, Pricing Studio (group-level view of the OH8 catalogue), cookie CMP, footer and legal pages, the Vendor Assurance Room (OH14.6 extended with document types, cadences, reminders, tenant publication, evidence packs, auditor grants, questionnaire responder and the cadence dashboard), the client onboarding, trials and discounts super-admin UI (over OH4 and OH8), the group feedback intake hub and product backlog, and tutorials, tours and What's new (IPB-07). Shared packages: `packages/cms`, `brand`, `consent-ui`, `marketing`, `feedback`, `hlp`, `trust` (IPB-01).

**Users.** `PLT_SUPER_ADMIN` (owner), `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER` (Company Secretary's office), `PLT_SECURITY_OFFICER`, `PLT_DPO`, `PLT_GRIEVANCE_OFFICER`, product heads (publication targets, pricing, trials), HR (careers), marketing (OH17), support (feedback bugs), product managers (backlog), tutorial authors; externally: website visitors, prospects (NDA click-through), tenants (vendor documents through product mirrors), auditors and regulators (grants), applicants.

**Requirement codes.** `CA13` s.12(3)(c) (name, registered office, CIN, contact on publications) [LAW]; `DPDP` ss.5–8, 13 (consent, notice, grievance); IT Rules 2021 rr.3(2), 4 [LAW; COUNSEL on applicability]; `CERTIN` (security.txt, VDP) [REC]; Consumer Protection (E-Commerce) Rules 2020 where applicable [COUNSEL]; `ASCI`, `CCPA` (dark patterns in CMP and pricing); RPwD Act 2016 and GIGW 3.0 for accessibility statement [LAW; REC]; `OUT`, RBI IT Governance Directions 2023, SEBI CSCRF, IRDAI outsourcing (frameworks for assurance documents) [VERIFY references]; `ISO`, `SOC2`; Companies Act 2013 ss.23, 26, 42 and SEBI ICDR for the Investors page [LAW; COUNSEL]. Identifiers `REQ-OH18-nn`.

**Data owned.** CMS content and revisions, brand packs, offices, footer, legal pages and versions, consent texts (the ledger is OH3), assurance documents and publications, acknowledgements, grants, requests, questionnaire answers library, Claims Register, feedback items and backlog, tutorials and tours, release cards. Never: client regulated data; raw VAPT reports on the public site; unregistered claims.

### OH18.1 Headless CMS for the group site (IPB-04 §04.3.1, §04.3.7)

- **REQ-OH18-01 Content model.** `packages/cms` items: `page`, `block` (hero, feature_grid, steps, logo_wall, stats with claims refs, timeline, team_grid, faq, cta, pricing_table, comparison_table, legal_page, office, footer, nav_menu, job, press_item, case_study, changelog_entry, resource, blog_post (toggle, default off), vlog (off)), with revisions, drafts, scheduled publication, locale variants (`en`, `hi`), SEO fields, JSON-LD, redirects; one brand pack for the group site and optional packs for TRN and HSP (Appendix B decision 29) [OWNER].
- **REQ-OH18-02 Standard pages (lean set for the group site):** Home; About (dated milestones, mission, boundary statement "a software and professional-services group; not a regulated entity, law firm or lender" [COUNSEL]); Group companies (one card per product scope with link to its own site; Equator described as independent); Team and Leadership (consent-flagged photos); Governance (policies list, grievance and DPO identities); Investors (toggle `web.investors.enabled`, default off, locked disclaimer, legal review per publish [COUNSEL]); Careers (open roles from OH10 requisitions and intern intakes; apply → `HR` port with consent; closed roles 410; `JobPosting` JSON-LD); Press and media kit; Partners; Contact (form → `CRM` port; Delhi, Noida, Jaipur offices; click-to-load static map; WhatsApp button with opt-in notice); Trust Centre (OH18.4; rendered from the SoR, never typed); Help and Tutorials routes; Resources library (group-level, `email_gate` as the only lead magnet mechanism); Changelog (group release feed from `ReleaseNotePublished`); Accessibility statement (IPB-05 Template 10; known issues from the a11y backlog); Sitemap; Legal pages (`/legal/{slug}`); Grievance (`/grievance` → OH6 `grievance` destination); Status (external link). Pricing and Compare are not published on the group site (products own pricing); Pricing Studio is internal (OH18.2).
- **REQ-OH18-03 Publishing workflow.** `DRAFT → REVIEW → LEGAL_REVIEW (when the item has claims, legal text or is a standard page) → APPROVED → SCHEDULED → PUBLISHED → ARCHIVED`; maker-checker on publish (editor maker; a second editor or legal reviewer checker; **the super admin cannot publish without a checker**); claims lint (IPB-08-24) and the OH14.6 claims gate block publication; every published revision is immutable and diffable; rollback publishes a prior revision as a new one.
- **REQ-OH18-04 Security of the CMS.** Uploads: type sniffing, size limits, AV scan, SVG sanitisation, EXIF stripping (MEDIA, AV ports); rich text sanitised server-side (allow-list; no inline scripts or event handlers); embeds only from an allow-list through EGRESS with link previews fetched server-side (SSRF guard: no private ranges, DNS rebinding check); CSP with nonces and no inline third-party scripts; host-header validation against the brand pack host map (white-label hosts refused unless registered and verified); per-item RLS by brand pack and scope; rate limits and anti-automation on forms; preview URLs signed and short-lived.
- **REQ-OH18-05 Word-to-CMS bulk import** (cross-pollinated from LD): DOCX import into blocks with a dry run, plagiarism and duplicate check (PLAGIARISM port), claims lint and an editor review before any publication.
- **REQ-OH18-06 Rendering.** Server-rendered Next.js public app, ISR with purge on publish, edge caching, `BreadcrumbList` and `Organization` JSON-LD, visible last-reviewed date, sitemap and robots, hreflang for `hi`, Lighthouse budgets (LCP ≤ 2.5 s, CLS ≤ 0.1, INP ≤ 200 ms) in CI.
- **REQ-OH18-07 Group Studio dashboards (IPB-04 OH note):** leads by product, feedback by product, policy versions in force per brand pack, vendor-document cadence status, careers funnel; `OPS_*` roles see only their product scope.

### OH18.2 Brand Studio, brand packs and Pricing Studio

- **REQ-OH18-08 Brand Studio** (`packages/brand`): logo (sanitised SVG and PNG), favicon, colour tokens with the WCAG 2.2 AA contrast guard (IPB-D-11), typography (Inter), application display name, e-mail sender identity, social links, boundary disclaimer, legal entity line (legal name, CIN, GSTIN), officers (Grievance Officer, DPO); the group pack `infrabyx-group` is the Hub's own; product packs are owned by the products and **read** by the Hub for group pages and invoices (`IPB_BRAND_PACK_SOURCE`); white-label packs for Udofin and Finbyx resale (IPB-D-10) are provisioned through `WhiteLabelTenantProvisioned` (OH4 and OH8 billing set-up) and never edited here.
- **REQ-OH18-09 Pricing Studio (internal).** Group view of the OH8 signed catalogue: plans, SKUs, price books, discount authority (DoA), trial rules; changes are OH8 maker-checker actions; the Studio publishes **no public pricing** for the group site; product sites render their own pricing from the catalogue through the BILLING port.
- **REQ-OH18-10 Terminology and display names.** `vidhi.brand.display_name` overrides for white-label plans are product settings; the Hub shows the kernel name `vidhi` in audit (IPB-03-58).

### OH18.3 Cookie CMP, footer and legal pages

- **REQ-OH18-11** CMP per IPB-04-75 to IPB-04-84 and Part 4.14; consent texts versioned from `legal_page` strings; re-prompt on substantive change; GPC honoured; authenticated Hub routes never ask for marketing consent.
- **REQ-OH18-12** Footer per IPB-04-71 to IPB-04-74: brand block with "Part of the Infrabyx Group"; Product (group companies), Resources, Company, Legal (all adopted IPB-05 templates), Contact (registered office; Delhi, Noida, Jaipur offices as `office` records), entity line, officers line, social with labels, utilities (status, language, cookie settings, accessibility, sitemap, report a problem), disclaimer, copyright; `pnpm cms:validate-footer` fails CI on any empty mandatory field.
- **REQ-OH18-13** Legal pages: Templates 1, 2, 5, 6, 7, 8, 9, 10, 11, 18 for the group site; master instances of 3, 4, 15, 17 held by the Hub for the selling entities (IPB-05 OH note); each with version, effective date, what changed, archive; `PolicyEffective` and `PolicyReviewDue` consumed into the group compliance calendar (OH14.5); counsel review before first publication [COUNSEL].
- **REQ-OH18-14** `security.txt`, VDP page (Template 11), `/.well-known/` files, status link.

### OH18.4 Vendor Assurance Room — system of record (IPB-08; extends OH14.6)

OH14.6 established the provider-assurance room with 90-day grants. v1.1 makes it the group's **Compliance Documents** system of record (IPB-D-09): every assurance document for every Infrabyx entity and product lives here once; products hold read-only mirrors and serve their tenants from them.

- **REQ-OH18-15 Catalogue.** Document types seeded from IPB-08 §08.4.1 (`cert_iso27001`, `cert_iso27701`, `cert_iso42001`, `cert_iso22301`, `soc2_report`, `soc2_bridge`, `vapt_report`, `vapt_summary`, `cert_in_auditor_cert`, `is_audit_report`, `internal_audit_summary`, `bcp_dr_test_report`, `patch_vuln_status`, `uptime_report`, `sbom`, `access_review`, `incident_summary`, `incident_notice_tenant`, `subprocessor_list`, `data_flow_diagram`, `dpia_summary`, `dpa_template`, `dpa_executed`, `insurance_certificate`, `incorporation_docs`, `affidavit_undertaking`, `policy_board_approved`, `financial_statements`, `management_attestation`, `compliance_mapping`, `rbi_dl_lsp_disclosure`, `accessibility_statement`, `pen_test_attestation_letter`, `exit_plan`, `concentration_statement`, `questionnaire_response`, `vendor_file`), each with cadence (monthly, quarterly, half-yearly, annual, ad hoc or per release), default gating (`public`, `login`, `nda`, `per_tenant`), evidence class, maker and checker roles (security officer; Company Secretary's office as `PLT_LEGAL_REVIEWER`; both for policies), template and framework mappings (`RBI-OUT-2025`, `RBI-ITG-2023`, `RBI-DL-2025`, `SEBI-CSCRF`, `IRDAI-OPS-2024`, `DPDP`, `CERT-IN`, `ISO27001`, `SOC2`, `SIG-LITE`, `CAIQ`) [VERIFY framework references]. New types need `PLT_SECURITY_OFFICER` maker and `PLT_LEGAL_REVIEWER` checker.
- **REQ-OH18-16 Document versions** record type, entity, products in scope, title, version, issuer, issue date, valid-from and valid-to, cadence instance, gating, file (PDF/A preferred) with SHA-256, size, pages, ≤ 120-word plain summary with a help key, related claims, supersedes, maker, checker, approval time and publication records; files are never overwritten (Object Lock; retention 10 years, floor 8 [INTERP; VERIFY]).
- **REQ-OH18-17 State machine** `DRAFT → REVIEW → APPROVED → PUBLISHED → SUPERSEDED | EXPIRED | WITHDRAWN` with publication as a second maker-checker step (publisher plus confirmer, neither the version's maker); the super admin cannot bypass (`IPB-TRUST-005`); Vidhi (`oh.vendor_doc_summary`) drafts metadata and summaries as maker only (IPB-08-12).
- **REQ-OH18-18 Cadence engine.** `next_due_at` from the last approved version and the cadence; reminders at T−30, T−14, T−7, T−1 and daily when overdue to the security officer and super admin (`trust.cadence.reminder_days`); overdue items on the controls dashboard and in the Work Inbox; `CadenceDue` and `CadenceOverdue` events; an expired version flips Trust Centre claims to the register's fallback wording (IPB-08-06, IPB-08-24).
- **REQ-OH18-19 Tenant publication (mirror to each product).** Publication targets: all tenants of a product, plan-gated, or `per_tenant` rows; the Hub emits the proposed `in.infrabyx.trust.VendorAssuranceDocumentPublished.v1` and `in.infrabyx.trust.VendorAssuranceDocumentStateChanged.v1` (canonical names, Spec v1.2 §6.34 *(v1.1 review)*) with the file object key in the shared Object Lock bucket; products build `vad_mirror_*` and serve their tenants' `Settings › Security & trust › Vendor documents` with watermarking, acknowledgements, requests and grants, and send `VendorAssuranceDocumentAcknowledged`, `VendorAssuranceRequestOpened` and `AuditorGrantChanged` back (IPB-08 §08.3.4 fallback when the Hub is offline); a daily mirror digest check raises `IPB-TRUST-009` mismatches to the controls dashboard.
- **REQ-OH18-20 NDA gating and watermarking.** `nda` requires an accepted click-through NDA or a flagged MSA confidentiality clause recorded as a consent-type event; `login`, `nda` and `per_tenant` downloads are watermarked on the fly ("Prepared for <tenant> · <user> · <timestamp IST> · <ack id>") with an XMP stamp; originals are never served directly; download URLs are single-use and ≤ 5 minutes; the delivered checksum is recorded on the acknowledgement.
- **REQ-OH18-21 Evidence packs.** Framework presets ("RBI outsourcing due diligence", "RBI IT Governance IS audit inputs", "SEBI CSCRF vendor", "IRDAI outsourcing", "DPDP processor", "SIG-Lite", "CAIQ") → ZIP with watermarked PDFs, signed `manifest.json`, `mapping.csv` and `README.txt`; pack generation acknowledges each document and emits `VendorAssuranceDocumentAcknowledged` with `action = PACK_EXPORTED` and `pack_id` (Spec v1.2 §6.34; the Hub-internal `in.oh.trust.EvidencePackExported.v1` carries the manifest detail) *(v1.1 review)*.
- **REQ-OH18-22 Auditor and regulator grants.** The OH14.6 `PROVIDER_ASSURANCE` grant becomes `vadg_` (named external person, organisation, role, scoped documents or preset, ≤ 90 days ceiling, default 30, optional read-only without download, magic link plus OTP in an isolated realm, revocable, logged in the tenant's and the Hub's audit trails, maker-checker where `trust.grant.require_mc`); `ExternalAccessGranted`, `ExternalAccessUsed` and `ExternalAccessRevoked` continue to be emitted with the requesting RE's `reid` (Integration Spec 6.21); prospects receive `prospect` grants (≤ 14 days, `login` documents only) from the Trust Centre request form.
- **REQ-OH18-23 Requests and questionnaire responder.** Tenant requests (`vadr_`) open an OH6 ticket to the security officer with SLAs (`trust.request.ack_hours` 24; `trust.request.fulfil_days` 10, 3 when a regulator deadline is flagged); the standard answers library (`vadq_`) with owner, evidence links and review date; Vidhi drafts unmatched answers from the library and published documents only, labelled draft; the security officer approves every answer; the released questionnaire becomes a `questionnaire_response` document.
- **REQ-OH18-24 Reports.** Cadence compliance dashboard (per type and entity: current version, valid-to, next due, status, days overdue, owner, open requests; roll-up "documents in cadence"), per-tenant acknowledgement report (signed PDF or CSV), regulator-ready **vendor file** per client (agreements from OH3, DPA, certifications, VAPT summary, BCP and DR summary, sub-processor list, incident notices, SLA performance from OH8 and the status page, acknowledgement history, open requests; quarterly or on demand), requests and grants reports.
- **REQ-OH18-25 Claims Register.** `clm_` entries link every public, sales, tutorial or social claim about a certification, audit, control, uptime or compliance status to a current `PUBLISHED` document or a `LEDGER` or `COMPUTED` metric; the CMS, Trust Centre renderer and OH7 or OH17 claims gate refuse unregistered claims (`IPB-TRUST-006`); expiry flips wording to the fallback; `ClaimRegisterChanged` is proposed for product CMS renderers (Part 6.2A). The OH14.6 claims gate (`GET /v1/claims-gate/check`) reads the register and the certification registry as one source.
- **REQ-OH18-26 Public Trust Centre** (`/trust` on the group site and, through mirrors, each product): only `public` `PUBLISHED` items; certifications actually held with issuer, scope and validity; VAPT summary (never the report); sub-processor list with change-notice subscription; data residency statement; uptime link; DPA request; VDP; "in progress" items only with a target quarter and no badge; request access form → prospect grant path.
- **REQ-OH18-27 Security, privacy, retention.** RLS on tenant-side tables; grantee realm isolation; acknowledgement personal data minimised and purpose-tagged `vendor_due_diligence_evidence`; retention 10 years for versions and acknowledgements, requests 5 years; every action in the hash-chained audit ledger in the same transaction.

### OH18.5 Client onboarding, trials and discounts (super-admin UI over OH4 and OH8)

- **REQ-OH18-28 Tenants & plans Studio node** (IPB-07 platform node): list of client organisations and tenants per product scope with plan, entitlements, state, trial status, open onboarding gates, provisioning status and billing health; actions deep-link into OH4 (provisioning orders) and OH8 (plans, quotes); the super admin never provisions directly — the OH4 maker-checker gates stand.
- **REQ-OH18-29 Trials.** `trial (tenant, product, plan, start, end, extensions ≤ 1 [REC], conversion offer)`; trials **never auto-convert** to paid (cross-pollinated from UDF); T−7 and T−1 notices to the client admin; at end the tenant moves to the product's read-only or free tier per the catalogue, never to a charge without an explicit order; a trial on PRODUCTION needs the same contract set as any production tenant (OH4.2).
- **REQ-OH18-30 Discounts.** Discount rules from the OH8 catalogue (percentage and amount caps by role, time-bound, stackability rules); a discount above the user's DoA routes upward; every discount has a reason code, approver and expiry; Vidhi never proposes or approves discounts (locked list); Equator pricing is never discounted or bundled with other products (Part 4.4).
- **REQ-OH18-31 Self-serve sign-up controls** (OH8.9): sandbox self-serve on; UAT and production require gates; CAPTCHA and velocity controls; no dark patterns in trial and cancellation flows (CCPA Dark Patterns Guidelines 2023; IPB-07 "as easy to cancel as to buy").

### OH18.6 Feedback intake hub and product backlog

- **REQ-OH18-32 Intake.** Feedback from every product (`FeedbackSubmitted` events; the IPB-04 widget types `bug`, `idea`, `praise`, `nps`, plus `accessibility`) and from the group site lands in `Feedback › Inbox` with route pattern, app version, brand, locale, viewport, trace id and consent or user id — never page content, form values or query strings (IPB-04-95); `bug` and `accessibility` items create OH6 tickets (accessibility with the IPB-06 SLA); `idea`, `praise` and `nps` go to the product backlog; the submitter receives a reference and status (received, triaged, planned, shipped, declined) and `FeedbackStatusChanged` events.
- **REQ-OH18-33 Backlog.** Per product scope: items with votes (one per authenticated user), area, severity, linked OH15 epics and OH13 releases, status; an optional public or tenant-scoped idea board (`fb.idea_board.enabled`, off) with moderation; voting data stays in the Hub; roadmap items published to the group site only through the CMS workflow with no dates promised [REC].
- **REQ-OH18-34 Vidhi** (`oh.feedback_classify`, L1) suggests area and severity; triage staff decide; no auto-close or auto-reply beyond the acknowledgement (IPB-04-99); NPS detractors for a product client route to OH5 as today (OH5.2).
- **REQ-OH18-35 Scope.** `OPS_*` roles see feedback for their product scopes only; group product managers see aggregates and open items in scopes held.

### OH18.7 Tutorials, tours, help and What's new (IPB-07)

- **REQ-OH18-36 Tutorial pipeline** (IPB-07 §07.4.5): `DRAFT → RECORDED (screen capture from seeded demo tenant; captions) → REVIEWED (accessibility and claims lint) → PUBLISHED → STALE (on release change or review date) → RETIRED`; tutorials per product scope and per Hub module; hosted in the Resources library and `/tutorials`; captions and transcripts mandatory (IPB-06); a tutorial that mentions a certification or uptime figure needs a Claims Register entry.
- **REQ-OH18-37 Tours.** In-app tours per module (first visit; re-launchable from Settings › Tutorials & help), built from `hlp.*` keys so a changed term updates the tour; tours never block work and respect reduced motion.
- **REQ-OH18-38 Help centre and "i" registry.** The Hub hosts the group glossary registry editor (`hlp.<product>.<module>.<term>`; the Hub's own keys `hlp.oh.<module>.<term>`), CI lint for missing keys, the regulatory-reference panel (citations through `LAW_REGISTER`), and the content queue (stale tutorials, flagged articles, overdue reviews) (IPB-07 OH note). Seed target: ≥ 400 OH terms at O17 close, ≥ 900 by OP [REC].
- **REQ-OH18-39 What's new.** Release cards generated from OH13 releases and `ReleaseNotePublished` (all products) per audience; shown once per user with suppression levels (ORG); linked changelog on the group site.
- **REQ-OH18-40 Global search** (Part 3.5) indexes CMS pages, tutorials, glossary and vendor documents metadata under the same scope and PII refusal rules.

### OH18.8 Integrations and events

- Provides `CRM`, `HR`, `SUPPORT`, `BACKLOG`, `TRUST` and `CONSENT` ports to the products (IPB-01 supplementary ports); consumes `LeadCaptured`, `FeedbackSubmitted`, `ReleaseNotePublished`, `BlogPostPublished`, `ResourcePublished`, `WhiteLabelTenantProvisioned`, `PolicyEffective`, `PolicyReviewDue`; produces `VendorAssuranceDocumentPublished`, `VendorAssuranceDocumentStateChanged`, `ClaimRegisterChanged`, `FeedbackStatusChanged`, `CadenceDue`, `CadenceOverdue`, `NdaAccepted` (Part 6.2A; emitted cross-product only once registered in the Ecosystem Specification).

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| `cms.publish.require_checker` | Platform | `true`; super admin cannot bypass | Floor |
| `cms.blog.enabled`, `cms.vlog.enabled` | Brand pack | `false` | Commercial |
| `web.investors.enabled` | Brand pack | `false`; locked disclaimer and legal review when on | Commercial; disclaimer Floor |
| `cms.upload.max_mb`, allowed types | Platform | 25 MB; images, PDF, DOCX, SVG (sanitised), MP4 | Floor (may tighten) |
| `cms.embed.allowlist` | Platform | YouTube, Vimeo, LinkedIn (via EGRESS) | Regulated (CISO) |
| `web.consent.*` (CMP keys) | Brand pack | IPB-04 defaults; DPDP wording; GPC honoured | Floor for equal prominence and reject-on-close |
| `web.footer.*` | Brand pack | IPB-04 mandatory fields | Floor (CI validator) |
| `trust.cadence.reminder_days` | Platform | 30, 14, 7, 1, then daily | Floor (may add) |
| `trust.grant.max_days`, `trust.grant.require_mc` | Platform | 90 ceiling, default 30; `true` for `per_tenant` | Floor |
| `trust.request.ack_hours`, `trust.request.fulfil_days` | Platform | 24; 10 (3 with regulator deadline) | Floor (maximum) |
| `trust.retention.years` | Platform | 10 (floor 8) | Floor |
| `trust.mirror.stale_minutes` | Platform | 60 | Technical |
| `trust.financials.gating` | Platform | `per_tenant`; super admin plus CS approval | Floor (never loosened) |
| `trial.auto_convert` | Platform | `false` | Floor |
| `trial.max_extensions` | Product | 1 [REC] | Commercial |
| `discount.caps_by_role` | Entity | OH8 DoA | Floor: DoA applies; Equator never discounted or bundled |
| `fb.widget.floating`, `fb.idea_board.enabled` | Brand pack | `true`; `false` | Commercial |
| `fb.nps.min_interval_days` | Platform | 90; never first session | Floor |
| `tut.whats_new.suppression` | Org | Show once | Personal or Org |
| `hlp.lint.required` | Platform | `true` | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Website › Pages` | Page tree; block editor; revisions and diff; claims lint; legal review; schedule; publish with checker; redirects; SEO fields; `hi` variants | Content editors, legal reviewer |
| `Website › Careers and forms` | Roles from OH10 and intern intakes; applications to `HR` port; contact and partner forms to `CRM` port; consent versions; DLQ | HR, marketing operations |
| `Website › Brand Studio` | Group pack: logo, favicon, tokens with contrast guard, display name, entity line, officers, social; read-only view of product packs | Super admin (maker), legal reviewer (checker for entity and officers) |
| `Website › Pricing Studio` | Group view of OH8 catalogue, discount authority, trial rules (actions in OH8) | Super admin, finance |
| `Website › Footer, contact and legal` | Offices (Delhi, Noida, Jaipur), footer regions, legal pages with versions and what changed, consent texts, CMP settings, `security.txt` | Content editors, legal reviewer, DPO |
| `Trust › Compliance documents` (extends OH14.6) | Catalogue; documents by state; cadence calendar; publications and targets; acknowledgements; grants; requests; questionnaires and answers library; Claims Register; reports (cadence, per-tenant acknowledgements, vendor file) | Security officer, Company Secretary's office (legal reviewer), super admin, product heads (targets), internal audit (read) |
| `Trust › Trust Centre preview` | Rendered public Trust Centre with claims resolution shown | Security officer, content editors |
| `Admin › Tenants and plans` | Tenants per product scope with plan, trial, gates and billing health; links to OH4 and OH8; trial notices; discount approvals queue | Super admin, product heads, finance |
| `Feedback › Inbox` and `Feedback › Backlog` | Items by product scope and type; triage with Vidhi suggestion; ticket or backlog creation; votes; status and submitter notices; idea board moderation | Support, product managers, accessibility lead |
| `Help › Tutorials`, `Help › Tours`, `Help › Glossary registry`, `Help › What's new` | Tutorial pipeline; tour builder from `hlp` keys; registry editor with lint and citations; release cards | Tutorial authors, content editors, release managers |

Empty and error states: a page blocked by the claims lint names the phrase and the missing register entry; a footer with an empty mandatory field cannot be published and CI fails; a document download without an NDA returns `IPB-TRUST-002` with the NDA route; a grant past its end returns `IPB-TRUST-003`.

### Acceptance tests

- The super admin cannot publish a page, a footer or an assurance document without a different checker; an attempt returns `IPB-TRUST-005` or `cms_checker_required`.
- A page containing "ISO 27001 certified" cannot publish while no `PUBLISHED` `cert_iso27001` document and `clm_` entry exist; when the certificate expires, the Trust Centre text flips to "recertification in progress" within the cadence job window.
- An uploaded SVG with a script element is sanitised; an uploaded executable renamed `.png` is refused by type sniffing; an embed from a host outside the allow-list is refused; a link preview to `169.254.169.254` or a private range is refused (SSRF test); a request with a Host header not in the brand pack host map returns 421.
- Every public route loaded with no consent makes zero third-party requests; the banner shows equal Accept all, Reject all and Manage; Escape equals Reject; `Sec-GPC: 1` defaults analytics and marketing to rejected.
- A `per_tenant` financial statement is listed for no other tenant and never on the Trust Centre; a tenant download produces a watermarked PDF, a single-use URL that fails on replay, and an acknowledgement with the delivered checksum.
- An auditor grant of 91 days is refused; a grant revoked mid-session ends access at once; a grantee cannot list documents outside the scope (RLS and Cerbos); magic-link OTP realm has no tenant role.
- A cadence item unpublished at T+1 appears overdue on the controls dashboard and in the Work Inbox; the product mirror digest mismatch raises `IPB-TRUST-009`.
- A trial reaches its end date and the tenant moves to the read-only tier with no invoice created (negative test); a discount above the user's DoA cannot be applied and routes upward; a discount on an Equator SKU is refused.
- A careers application posts to the `HR` port with the consent text version and receipt and the CMS stores only the submission id; a closed role returns 410.
- A feedback item carries no page content or query string; an accessibility item creates an OH6 ticket with the IPB-06 SLA; an `OPS_SUPPORT` user with LD scope sees no LDC feedback.
- A tutorial without captions cannot publish; a tour referencing a missing `hlp` key fails the CI lint; What's new shows a release card once per user.


## 3. Instruction to Claude (from master prompt Part 9)

> **Instruction to Claude:** "Read docs/ipb/00_README.md, then IPB-04, IPB-05, IPB-07 §07.3.4–07.3.5 and IPB-08 in full before the plan. Verify first: (i) the IPB-04 `packages/cms`, `brand`, `consent-ui`, `marketing`, `feedback` and the IPB-08 `trust` package versions; (ii) the IPB-05 templates' parameter blocks and the entity particulars for the group (Appendix B decision 30); (iii) Companies Act 2013 s.12(3)(c) publication particulars and DPDP s.8(9), s.13 officer disclosures; (iv) the OH14.6 provider-assurance implementation to extend without breaking `ExternalAccess*` events; (v) the product mirror contracts (`vad_mirror_*`) agreed with the product agents; (vi) the Investors page toggle decision and counsel wording.
>
> On branch `cc/o17-website-trust` build OH18 (master prompt OH18; phase file `Phase_O17_Group_Website_CMS_and_Vendor_Assurance.md`):
>
> - **CMS and group site:** content model and the lean standard-page set (OH18.2) in `en` and `hi`; publishing workflow with mandatory checker (super admin cannot bypass), claims lint and legal review; upload security (type sniffing, AV, SVG sanitisation, EXIF strip), rich-text sanitisation, embed allow-list via EGRESS with SSRF guard, CSP, host-header validation against the brand-pack host map; Word-to-CMS bulk import with dry run and plagiarism check; ISR rendering, JSON-LD, sitemap, hreflang, Lighthouse budgets; group Studio dashboards by product scope.
> - **Brand Studio and Pricing Studio:** group brand pack with contrast guard, entity line and officers; read-only product packs; white-label packs via `WhiteLabelTenantProvisioned`; internal pricing view over OH8 with no public pricing.
> - **CMP, footer, legal:** IPB-04 CMP with ledger writes and GPC; binding footer with `pnpm cms:validate-footer` in CI; legal pages from IPB-05 templates with versions and re-consent mechanics; `security.txt`, VDP.
> - **Vendor Assurance Room as system of record:** catalogue seed (37 types), versions with checksums and Object Lock, the `DRAFT → … → PUBLISHED → SUPERSEDED | EXPIRED | WITHDRAWN` machine with two maker-checker steps, cadence engine and reminders, publication targets and mirror events (internal form until registered), NDA gating, on-the-fly watermarking, single-use URLs, evidence packs with signed manifests, auditor and prospect grants in an isolated realm continuing `ExternalAccess*`, requests with SLAs, questionnaire responder with Vidhi drafts (maker only), Claims Register unified with the OH14.6 claims gate, reports (cadence dashboard, acknowledgements, vendor file), retention 10 years.
> - **Tenants and plans Studio node, trials and discounts:** read views over OH4 and OH8 with deep links; trials that never auto-convert with T−7 and T−1 notices; discount rules under DoA with reason codes; Equator never discounted or bundled.
> - **Feedback hub and backlog:** intake from `FeedbackSubmitted` and the group widget; bug and accessibility items to OH6 with SLAs; ideas and NPS to the backlog with votes; status notices; idea board off; Vidhi classification at L1; scope visibility.
> - **Tutorials, tours, help, What's new:** tutorial pipeline with captions, tours from `hlp` keys, the group glossary registry editor with CI lint and citations, release cards from OH13 and `ReleaseNotePublished`; global search over CMS, tutorials, glossary and document metadata.
> - **Menus, screens and settings:** `Website`, `Trust › Compliance documents`, `Admin › Tenants and plans`, `Feedback` and `Help` menus and OH18 settings exactly as the OH18 tables specify; `hlp.oh.cms.*`, `hlp.oh.trust.*`, `hlp.oh.fb.*`, `hlp.oh.tut.*` keys.
>
> Tests and acceptance evidence: every OH18 acceptance test, including checker enforcement for the super admin, claims lint and expiry flip, upload and SSRF and host-header tests, CMP equal prominence and zero third-party requests, `per_tenant` isolation and watermark and single-use URL, grant ceiling and revocation, cadence overdue and mirror digest mismatch, trial non-conversion and discount DoA, careers consent hand-off, feedback minimisation and scope, tutorial captions and `hlp` lint.
>
> Show me the content model, page templates, CMP and footer configuration, the assurance catalogue seed and state machine, the mirror event contracts, the grant realm design and the feedback and tutorial pipelines for approval before coding."

**Exit gate:** OH18 tests green; footer and consent validators in CI; counsel review recorded for legal pages and the boundary disclaimer before first public publish; Trust Centre renders only registered claims; Ecosystem proposals for the trust events filed.

## 4. Build notes for Claude Code

### 4.1 Sub-module plan (one session each)

| Session | Scope | Depends on | Exit evidence |
|---|---|---|---|
| O17a | `packages/cms` adoption; `cms` schema; content model and blocks; publishing workflow with mandatory checker and claims lint; upload pipeline (sniff, AV, SVG sanitise, EXIF strip, size caps); rich-text sanitiser; embed allow-list via EGRESS with SSRF guard; CSP; host-header validation; signed previews; Word-to-CMS import | O2, O12 (claims gate) | Upload abuse suite; SSRF suite; checker enforcement tests |
| O17b | Standard pages and templates (lean set) in `en` and `hi` from the content deck; Brand Studio group pack with contrast guard; read-only product packs; `WhiteLabelTenantProvisioned` consumer; Pricing Studio read views over OH8 | O17a, O6 | Page render snapshots; contrast-guard tests; JSON-LD validation |
| O17c | CMP (`packages/consent-ui`) with ledger writes, GPC, re-prompt; footer item and `pnpm cms:validate-footer`; legal pages from IPB-05 templates with versions; `security.txt`, VDP, `/grievance` to OH6 | O17a, O3 (consent ledger) | CI consent test; footer validator; legal-page version tests |
| O17d | Vendor Assurance Room SoR: `trust` schema extension of OH14.6, catalogue seed (37 types), version model with checksums and Object Lock, state machine with two maker-checker steps, cadence engine and reminders, publication targets, mirror events (internal form), daily digest check | O12 | State-machine tests; cadence clock tests; replay rebuilds mirror |
| O17e | Gating and NDA, watermarking and single-use URLs, evidence packs with signed manifests, auditor and prospect grants in an isolated realm continuing `ExternalAccess*`, requests with SLAs, questionnaire responder with Vidhi drafts, Claims Register unified with the claims gate, reports (cadence, acknowledgements, vendor file) | O17d, O15 | Isolation adversarial tests; URL replay test; grant lifecycle tests |
| O17f | Tenants and plans Studio node; trials (never auto-convert; notices); discounts under DoA; Equator refusal; self-serve controls | O4, O6 | Trial end test (no invoice); DoA routing |
| O17g | Feedback hub: intake from `FeedbackSubmitted` and the group widget; OH6 tickets for bugs and accessibility with SLAs; backlog with votes; status notices; `oh.feedback_classify` at L1; scope visibility | O5, O15 | Minimisation test; scope test; SLA test |
| O17h | Tutorials pipeline, tours from `hlp` keys, glossary registry editor with CI lint and `LAW_REGISTER` citations, What's new from OH13 and `ReleaseNotePublished`, global search index for CMS, tutorials, glossary and document metadata | O17a, O12 | Caption requirement test; lint test; once-per-user card test |

### 4.2 API surface (`/v1/cms/...`, `/v1/trust/...`, `/v1/fb/...`, `/v1/help/...`)

| Method and path | Purpose | Authorisation |
|---|---|---|
| `GET/POST /v1/cms/items`, `PATCH /v1/cms/items/{id}`, `POST /v1/cms/items/{id}:transition` | Content items and revisions; workflow (checker ≠ maker; claims lint; legal review) | Content editors; legal reviewer; `cms.publish.require_checker` |
| `POST /v1/cms/uploads` | Upload with sniffing, AV, sanitisation; returns asset ref | Editors |
| `POST /v1/cms/import:docx` | Word-to-CMS dry run and import | Editors |
| `GET /v1/cms/preview/{signedToken}` | Signed, short-lived preview | Editors |
| `GET/PATCH /v1/brand/packs/{id}` | Group brand pack with contrast guard; product packs read-only | Super admin maker; legal reviewer checker for entity and officers |
| `GET/POST /v1/cms/offices`, `GET/PATCH /v1/cms/footer` | Offices (Delhi, Noida, Jaipur seeded; edit not delete) and footer regions | Editors; CI validator |
| `GET/POST /v1/cms/legal-pages`, `POST …/{id}:publish` | Legal pages with versions, effective dates, what changed | Legal reviewer checker |
| `POST /v1/consent/choices` | CMP ledger write (receipt id returned) | Public with anonymous consent id |
| `GET/POST /v1/trust/types` | Document types catalogue (maker SO, checker CS) | Security officer, legal reviewer |
| `GET/POST /v1/trust/documents`, `POST /v1/trust/documents/{id}/versions`, `POST …/versions/{vid}:transition` | Versions and the `DRAFT → … → PUBLISHED` machine (two maker-checker steps) | Per-type maker and checker; publisher and confirmer |
| `POST /v1/trust/documents/{id}/versions/{vid}:publish` `{targets}` | Publication targets (product, plan, per_tenant) → mirror events | Publisher + confirmer |
| `GET /v1/trust/cadence` | Due and overdue items; reminders schedule | Security officer, super admin |
| `POST /v1/trust/nda:accept` | NDA click-through (consent-type event) | Tenant owner or admin (via products) |
| `POST /v1/trust/downloads` → single-use URL | Watermarked download and acknowledgement | Tenant users via product mirror; grantees |
| `POST /v1/trust/evidence-packs` | Preset or selected documents → ZIP with signed manifest | Tenant via product; OH staff |
| `GET/POST /v1/trust/grants`, `POST /v1/trust/grants/{id}:approve\|revoke` | Auditor and prospect grants (≤ 90 days; isolated realm) | Tenant owner or admin; maker-checker where required |
| `GET/POST /v1/trust/requests`, `POST …/{id}:fulfil` | Document requests with SLAs (OH6 ticket) | Tenants; security officer |
| `GET/POST /v1/trust/questionnaires`, `POST …/{id}:draft`, `:approve`, `:release` | Questionnaire responder (Vidhi draft, SO approval, release as `per_tenant` document) | Security officer |
| `GET/POST /v1/trust/claims`, `GET /v1/claims-gate/check` | Claims Register and the unified claims gate | Legal reviewer, security officer; any renderer |
| `GET /v1/trust/reports/{cadence\|acknowledgements\|vendor-file}` | Reports and vendor file generation | Security officer; tenants (own) |
| `GET /v1/studio/tenants` | Tenants and plans view over OH4 and OH8 | Super admin, product heads, finance |
| `GET/POST /v1/studio/trials`, `POST /v1/studio/trials/{id}:extend\|end` | Trials (never auto-convert) | Product heads; notices automatic |
| `GET/POST /v1/studio/discount-rules`, `POST /v1/studio/discounts:apply` | Discount rules and applications under DoA; Equator refused | Sales within DoA; approvers |
| `GET/POST /v1/fb/items`, `POST /v1/fb/items/{id}:triage` | Feedback intake and triage (ticket or backlog) | Support, product managers (scope) |
| `GET/POST /v1/fb/backlog`, `POST /v1/fb/backlog/{id}:vote` | Backlog and votes | Staff; authenticated users (idea board if on) |
| `GET/POST /v1/help/tutorials`, `POST …/{id}:transition` | Tutorial pipeline | Tutorial authors; reviewers |
| `GET/POST /v1/help/tours`, `GET/POST /v1/help/glossary` | Tours and glossary registry with lint | Content editors |
| `GET /v1/help/whats-new` | Release cards per audience | All users |

Errors: `cms_checker_required`, `IPB-CMS-012` (prohibited investor wording), `cms/claims_blocked`, `cms/upload_type_refused`, `cms/svg_sanitised` (warning), `cms/embed_not_allowed`, `cms/ssrf_blocked`, `cms/host_not_registered` (421), `cms/stale_revision`, `cms/footer_invalid`, `IPB-TRUST-002` (NDA required), `IPB-TRUST-003` (grant expired or revoked), `IPB-TRUST-004` (expired certification shown as current — renderer refuses), `IPB-TRUST-005` (super admin bypass refused), `IPB-TRUST-006` (unregistered claim), `IPB-TRUST-009` (mirror digest mismatch), `trust/gating_cannot_loosen`, `trust/url_replayed`, `trust/grant_too_long`, `trust/checksum_mismatch`, `studio/trial_cannot_auto_convert`, `studio/discount_exceeds_doa`, `studio/equator_discount_refused`, `fb/content_captured_refused`, `fb/scope_denied`, `help/captions_required`, `help/hlp_key_missing`.

### 4.3 Settings keys registered in this phase

`cms.publish.require_checker` (true, floor), `cms.blog.enabled` and `cms.vlog.enabled` (false), `web.investors.enabled` (false), `cms.upload.max_mb` (25) and allowed types, `cms.embed.allowlist`, `web.consent.*` (IPB-04 defaults; DPDP wording; GPC honoured; reprompt on change), `web.footer.*`, `web.footer.group_url`, `trust.cadence.reminder_days` (30, 14, 7, 1, daily), `trust.grant.max_days` (90) and `trust.grant.require_mc` (true for per_tenant), `trust.request.ack_hours` (24) and `trust.request.fulfil_days` (10; 3 with regulator deadline), `trust.retention.years` (10, floor 8), `trust.mirror.stale_minutes` (60), `trust.financials.gating` (per_tenant), `trial.auto_convert` (false, floor), `trial.max_extensions` (1), `discount.caps_by_role` (OH8 DoA), `fb.widget.floating` (true), `fb.idea_board.enabled` (false), `fb.nps.min_interval_days` (90), `tut.whats_new.suppression`, `hlp.lint.required` (true).

### 4.4 Data model sketch (schema `cms`, `trust`, `fb`, `help`)

```
cms.item(itm_id pk, brand_pack_id, product_scope, type, slug, locale, state, current_rev, legal_review_required bool, claims_lint jsonb)
cms.revision(rev_id pk, itm_id fk, blocks jsonb, seo jsonb, author_id, created_at, published_at null, published_by, checked_by)  -- append-only
cms.office(off_id pk, brand_pack_id, label, lines text[], city, state, pin, country, phone, hours, map_url, is_registered_office)
cms.legal_page(lp_id pk, brand_pack_id, template_no, version, effective_at, what_changed, body_rev fk, prior_version fk)
trust.document_type(type_key pk, cadence, default_gating, evidence_class, maker_role, checker_role, template_ref, frameworks text[])
trust.document_version(vad_id pk, type_key fk, legal_entity_id, products text[], title, version, issuer, issue_date, valid_from, valid_to, cadence_instance, gating, object_key, sha256, bytes, pages, summary, help_key, supersedes fk, maker_id, checker_id, approved_at, state)
trust.publication(pub_id pk, vad_id fk, target_kind check in ('product','plan','tenant'), target_ref, publisher_id, confirmer_id, published_at)
trust.acknowledgement(vada_id pk, vad_id fk, tenant_ref, user_ref, grant_id null, kind, delivered_sha256, watermark_id, ip_class, ua_class, purpose, at)
trust.grant(vadg_id pk, tenant_ref, grantee_email, grantee_org, grantee_role, scope jsonb, starts_at, ends_at check (ends_at <= starts_at + interval '90 days'), read_only bool, state, created_by, approved_by)
trust.request(vadr_id pk, tenant_ref, type_key null, description, purpose, regulator_deadline bool, ticket_id, ack_due_at, fulfil_due_at, state)
trust.claim(clm_id pk, text, evidence_kind check in ('document','ledger','computed'), evidence_ref, fallback_text, state, flagged_at)
trust.nda_acceptance(tenant_ref, nda_version, accepted_by, at)
fb.item(fbk_id pk, product, product_scope, tenant_ref null, user_ref null, consent_id null, type, route_pattern, app_version, brand_pack_id, locale, viewport_class, trace_id, text, status, ticket_id null, backlog_id null)
help.glossary(hlp_key pk, module, term, text_en, text_hi, regulatory_ref jsonb, related text[], tutorial_ref null, reviewed_at)
help.tutorial(tut_id pk, product_scope, module, title, state, video_ref, captions_ref, transcript_ref, claims_lint jsonb, review_due_at)
```

All tenant-side and scoped tables carry RLS deny-by-default; `trust.document_version.object_key` points to the Object Lock bucket shared read-only with product mirrors; originals are never served directly.

### 4.5 Help keys (minimum set)

`hlp.oh.cms.checker_required`, `hlp.oh.cms.claims_lint`, `hlp.oh.cms.legal_review`, `hlp.oh.cms.embed_allowlist`, `hlp.oh.cms.footer_entity_line`, `hlp.oh.cms.officers_line`, `hlp.oh.consent.categories`, `hlp.oh.consent.gpc`, `hlp.oh.trust.cadence`, `hlp.oh.trust.gating_public|login|nda|per_tenant`, `hlp.oh.trust.watermark`, `hlp.oh.trust.single_use_url`, `hlp.oh.trust.evidence_pack`, `hlp.oh.trust.grant_realm`, `hlp.oh.trust.claims_register`, `hlp.oh.trust.vendor_file`, `hlp.oh.studio.trial_no_auto_convert`, `hlp.oh.studio.discount_doa`, `hlp.oh.fb.what_we_capture`, `hlp.oh.tut.captions_required`, `hlp.oh.tut.whats_new`.

## 5. Acceptance tests (Gherkin)

```gherkin
Feature: Checker enforcement
  @REQ-OH18-03 @REQ-OH18-17 @IPB-08-12
  Scenario: Super admin cannot publish alone
    Given "rjnprajapati@gmail.com" is PLT_SUPER_ADMIN and is the maker of page "/about" revision 4
    When the super admin requests PUBLISHED
    Then the response is 403 with type "cms_checker_required"
    Given the super admin is the maker of assurance document version "cert_iso27001 v2"
    When the super admin approves and attempts to publish it
    Then the response is 403 with type "IPB-TRUST-005"

Feature: Claims lint and expiry
  @REQ-OH18-25 @IPB-08-24
  Scenario: Unregistered claim blocked; expired certificate flips wording
    When an editor publishes a page containing "ISO 27001 certified" with no PUBLISHED cert_iso27001 and no clm_ entry
    Then the response is 422 with type "IPB-TRUST-006" naming the phrase
    Given a PUBLISHED cert_iso27001 whose valid_to was yesterday
    When the cadence job runs
    Then the version is EXPIRED and the Trust Centre renders "ISO/IEC 27001 — recertification in progress" with no badge

Feature: Upload, SSRF and host security
  @REQ-OH18-04
  Scenario Outline: Abusive uploads and embeds are refused
    When an editor uploads <file>
    Then the result is <outcome>
    Examples:
      | file | outcome |
      | an SVG containing <script> | stored with the script element removed and a cms/svg_sanitised warning |
      | an .exe renamed to logo.png | refused with cms/upload_type_refused |
      | a 60 MB video | refused with size limit named |
  Scenario: SSRF and host header
    When an editor requests a link preview for http://169.254.169.254/latest/meta-data
    Then the response is 422 with type "cms/ssrf_blocked"
    When a request arrives with Host "evil.example"
    Then the response is 421

Feature: Cookie consent
  @REQ-OH18-11 @IPB-04-75 @IPB-04-79
  Scenario: Equal controls, reject on close, GPC, zero third-party requests
    When CI loads every public route with no consent cookie
    Then zero requests leave to third-party hosts
    And the banner shows Accept all, Reject all and Manage with equal size and tab order
    When the visitor presses Escape
    Then a ledger record with all non-necessary categories rejected is written and a receipt id returned
    When a visitor arrives with header Sec-GPC: 1
    Then analytics and marketing default to rejected and the banner says so

Feature: Vendor Assurance isolation and downloads
  @REQ-OH18-19 @REQ-OH18-20 @IPB-08-34 @IPB-08-35
  Scenario: per_tenant isolation and single-use watermarked download
    Given financial_statements v1 is published per_tenant to tenant A only
    When tenant B lists vendor documents through its product mirror
    Then the document is absent
    And the Trust Centre never lists it
    When tenant A downloads it
    Then the PDF carries "Prepared for Tenant A · user · timestamp IST · ack id" on every page and an XMP stamp
    And an acknowledgement records the delivered checksum
    When the same URL is requested again
    Then the response is 410 with type "trust/url_replayed"

Feature: Auditor grants
  @REQ-OH18-22 @IPB-08-19 @IPB-08-36
  Scenario: Ceiling, revocation and realm isolation
    When a tenant admin creates a grant of 91 days
    Then the response is 422 with type "trust/grant_too_long"
    Given an ACTIVE 30-day grant scoped to the "RBI outsourcing due diligence" preset
    When the grantee lists documents
    Then only preset documents are returned and the grantee token carries no tenant role
    When the tenant admin revokes the grant
    Then the grantee's next request returns IPB-TRUST-003

Feature: Cadence and mirrors
  @REQ-OH18-18 @REQ-OH18-19 @IPB-08-29
  Scenario: Overdue surfaces and digest mismatch alerts
    Given bcp_dr_test_report cadence quarterly with last valid_from 2026-04-01
    When the clock is 2026-07-02
    Then the item is OVERDUE on the controls dashboard and in the security officer's Work Inbox
    When a product mirror digest differs from the OH publication digest
    Then IPB-TRUST-009 is raised on the controls dashboard with product and digests

Feature: Trials and discounts
  @REQ-OH18-29 @REQ-OH18-30
  Scenario: No auto-conversion; DoA; Equator refusal
    Given a trial ending today for tenant "Demo Co" on product FBX
    When the end job runs
    Then the tenant is on the read-only tier and no order or invoice exists
    When a sales user with a 10% discount authority applies 15%
    Then the response is 422 with type "studio/discount_exceeds_doa" and an approval request is created
    When any user applies a discount to an Equator SKU
    Then the response is 422 with type "studio/equator_discount_refused"

Feature: Careers and feedback hand-offs
  @REQ-OH18-02 @REQ-OH18-32 @IPB-04-67 @IPB-04-95
  Scenario: Consent receipts and minimisation
    When an applicant submits the careers form with the consent box ticked
    Then the HR port receives the application with consent_text_version and receipt id and the CMS stores only submission id and status
    When a closed role is requested
    Then the response is 410 with a link to open roles
    When a feedback item arrives from the LDC product with route "/obligations/{id}?q=secret"
    Then the stored route pattern is "/obligations/{id}" with no query string and no page content
    And "test.support_agent@opshub.test" (scope LD) cannot see the item

Feature: Tutorials and help lint
  @REQ-OH18-36 @REQ-OH18-37 @REQ-OH18-39
  Scenario: Captions and hlp keys are mandatory
    When a tutorial without a captions file is moved to PUBLISHED
    Then the response is 422 with type "help/captions_required"
    When a tour references hlp.oh.trust.gating_secret which does not exist
    Then the CI lint fails naming the key
    When a user opens the app after release rel_2026_44
    Then the What's new card shows once and not on the next session
```

## 6. Exit gate

- Gherkin scenarios and the OH18 acceptance list pass; `pnpm cms:validate-footer`, the consent zero-third-party test and the upload and SSRF suites are required CI checks.
- Counsel review recorded for legal pages, the boundary disclaimer and the Investors disclaimer before the first public publish; Claims Register seeded; Trust Centre renders only registered claims.
- Vendor Assurance Room catalogue seeded with 37 types; the state machine, cadence engine and mirror events proven by replay; `ExternalAccess*` events unchanged for grants.
- Ecosystem proposals filed for the trust, feedback and CMS events (Part 6.2A); `docs/status` updated; pull request merged after owner approval.
