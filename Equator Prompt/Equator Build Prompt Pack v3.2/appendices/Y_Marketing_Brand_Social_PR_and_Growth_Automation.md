# Appendix Y — Marketing, Brand, Social Media, PR and Growth Automation (v3.0, 23 October 2026)

> **Binding reference specification** for the Marketing, Brand, Social Media, PR and Partnerships workspace of the Operations Platform (`apps/ops`, schema `mkt`) and for Phase P17. Read with `01_MASTER_PROMPT.md` (NN-01, NN-12, NN-15–NN-17, NN-20, NN-23, NN-26, NN-28, NN-29, NN-33–NN-40), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (D2-17, D2-18, D2-20; D3-01–D3-09), Appendix P (copy deck, voice, SEO/GEO, copy lint LINT-001–LINT-050, content governance), Appendix H §5–§6 (website corrections, safe-claims library), Appendix O (revenue streams S-01–S-17, deny-list X-01–X-16 of that appendix, dark patterns DP-01–DP-13), Appendix U §U.12 (Equa remediation register E-01–E-17), Phase P13 (CMS, Claims Register `growth.claims_register`, lead capture, partner portal, analytics, experiments, neutrality firewall FR-P13-26), Appendix X (Operations Platform engine, CRM and generic automation engine) and Appendix Z (appraisal). Research base: [RA] Jupitice; [RB] business models, funnels and automation; [RD] Brevo, Adobe Express and social platform APIs; [RE] directory, advertising and marketplace law.

---

## Y.0 Purpose, sources, precedence

### Y.0.1 What this appendix owns

| Owns | Does not own (owner) |
|---|---|
| Marketing strategy objects (objectives, OKRs, segments, ICPs, messaging houses); campaigns, budgets and experiments; the content and social calendar and its review workflow for non-web channels; Adobe Express hand-off and publication evidence; social engagement triage; brand asset library, rights and consent records, boilerplates and co-branding approvals; marketing email/SMS/WhatsApp sends, send audiences and frozen snapshots (built on Appendix X CRM segments), send-time consent checks, marketing suppression lists, sender-domain authentication and frequency caps; lead magnets, landing-page block rules, nurture sequences, webinar funnel, referral programmes, events and re-engagement; the marketing automation catalogue (MA-01–MA-32); PR, media list, coverage log and crisis communications; partnerships, MoUs and obligations; SEO/GEO planning objects; attribution, marketing dashboards and marketing-role contribution metrics | Website copy, voice, SEO/GEO rules and copy-lint rules LINT-001–LINT-050 (Appendix P); the CMS, Claims Register, website lead forms and web experiments engine (P13); CRM contacts, accounts, opportunities, contact segments (`ops.crm_segments`), the consent and preference mirror (`ops.crm_comm_prefs`, `ops.crm_marketing_view`), partner organisation records and the `partnership` pipeline, tickets, the Brevo webhook ingress and the generic automation engine (Appendix X); transactional and case communications (P07); fee figures (Appendix B); revenue-stream registry and kill switches (D3-08; Appendix AB); Private Practice Marketplace and sponsored placement (NN-34, D3-01, schema `mkp`); professional registry (NN-39, schema `dir`); appraisal cycles and ratings (Appendix Z); export package convention (D3-07) |

### Y.0.2 Sources and evidence labels

Research findings are cited as [RA], [RB], [RD], [RE] with the section number of the research file; primary instruments are cited as the research file cites them. Where research marks a fact as not confirmed, this appendix keeps the value as a configurable parameter and marks it **[VERIFY — open: …]**. Vendor capabilities (Brevo, Adobe, LinkedIn, Meta, X, YouTube) are vendor statements as at 23 October 2026 and are re-checked at each adapter spike.

### Y.0.3 Precedence

1. Master prompt (NN rules, §15 resolutions) → Appendix G (legal rules) → Appendix B (fee figures) → Appendix F (names, events, errors) → this appendix for marketing objects.
2. For public copy and lint rules Appendix P prevails; this appendix adds channel-specific rules (SL-01–SL-20, §Y.4.5) and funnel-technique rules (MT-01–MT-24, §Y.7.1) that are **additive** to LINT-001–LINT-050. Where two rules differ, the stricter applies.
3. For CRM records and the automation engine, Appendix X prevails on structure and runtime; this appendix prevails on what a marketing automation may do (§Y.7.8) and on marketing approvals.
4. For paid placement this appendix never creates a paid-visibility surface; NN-34 and D3-01 govern.
5. The Claims Register stays single (`growth.claims_register`, FR-P13-10). Every marketing surface references `claim_key`; no surface keeps a private copy of a claim.

### Y.0.4 Register entries made by this appendix

**Requirements (02 §2):**

| ID | Requirement (management brief, 23 Oct 2026) | Where specified | Status |
|---|---|---|---|
| R-55 | A full marketing, brand, social media, PR and partnerships architecture inside Equator (Operations Platform), with the campaign and social calendar kept in Equator even where Brevo, Adobe Express or social tools send or publish (brief item 3, item 7) | App. Y §Y.1–§Y.9; P17 | S+V |
| R-56 | "Autopilot" growth: funnels, lead magnets, nurture, webinars, referral and partner programmes, events and re-engagement automated with human approval of public claims, pricing, testimonials, sensitive targeting and mass sends (brief item 7; Expanded Prompt "autopilot with human approval") | App. Y §Y.7; P17 FR-P17-30–FR-P17-37 | S+L |
| R-57 | Open, replaceable marketing tools with Equator as system of record for segments, consent and campaign results; analytics, attribution, budget/ROI and outcome-based contribution metrics for marketing staff feeding appraisal (brief items 3, 4, 7; NN-35, NN-40) | App. Y §Y.6, §Y.11; P17 FR-P17-24–FR-P17-29, FR-P17-42–FR-P17-47 | S+V |

**Decisions (02 §3):**

| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| D3-25 | **Equator is the system of record** for segments (Appendix X `ops.crm_segments`) and send audiences, consent (platform consent ledger, mirrored once by Appendix X) and suppression, content approvals, publication evidence and **reported** campaign results (frozen `mkt.metric_snapshots`); Brevo remains system of record only for the raw engagement events it generates (Appendix X D3-22). Brevo, Adobe Express, social platforms and ad platforms are executors behind ports; their data is synchronised back and never authoritative | NN-40; [RD] F3.1, DI-B 8–11 | §Y.1.3, §Y.6 |
| D3-26 | **Adobe Express = asset hand-off, not an integration for publishing.** Adobe Express Content Scheduler has no public publishing API; Equator produces a hand-off package, the operator publishes in Adobe (or the native app), and records the post URL and screenshot as publication evidence. Equator's own `SOCIAL_PORT` adapters publish only where platform access is granted, each behind a flag that defaults OFF; `manual_handoff` is the default adapter | [RD] F3.2, F3.3, DI-B 12–14 | §Y.4.6–§Y.4.8 |
| D3-27 | **No referral rewards of any kind to advocates, CAs, CSs or CMAs** (individuals or their firms) — no cash, commission, credits, discounts, gifts or priority. Professionals may be "relationship partners" (co-hosted education, content) without reward. Cash referral fees are paid only to non-professional partners under a written, disclosed agreement | NN-34; BCI Rules Part VI Ch. II r.36 and Ch. III r.2 [RE] F1.2, F1.4; ICAI Website Advisory 14 Oct 2020 and ESB view 23 Oct 2019, ICSI Advertisement Guidelines 2020, ICMAI Guidelines 2025 [RE] F1.5; [RB] Implications A.5 (X-17) | §Y.7.5; supersedes App. O X-11 credits and FR-P13-20(b) credits (master X-54) |
| D3-28 | **Funnel technique register.** Video-sales-letter players with locked controls, resetting or per-visitor timers, scarcity not bound to a real capacity record, fictitious reference prices, unverified testimonials, outcome or saving promises and "evergreen presented as live" webinars are **prohibited**; paid low-ticket ("tripwire") webinars are allowed for B2B education only, with total price incl. GST, refund terms and operator identity shown | [RB] §4.1, Implications E; CCPA Misleading Advertisements Guidelines 2022; Dark Patterns Guidelines 2023; NN-17, NN-29 | §Y.7.1–§Y.7.3 |
| D3-29 | **Attribution and contribution.** Marketing reports use a documented, versioned attribution model registry; the default reporting model is position-based (40/20/40) with first-touch and last-touch views; model changes are maker-checker and never silently restate history. Marketing-role contribution metrics are outcome- and quality-based, visible to the employee and disputable, and never use activity surveillance, case outcomes or vanity counts as primary measures | NN-35; [RB] §5; Appendix Z | §Y.11 |

**Cross-file resolutions (master §15):**

| # | Topic | Resolution |
|---|---|---|
| X-53 | P13 `growth` tables, Appendix X CRM and the `mkt` schema | Appendix X's CRM is the system of record for contacts, accounts, opportunities and lead routing; the P13 website forms write leads into it (P13 FR-P13-19 tables migrate or become views as Appendix X specifies). `growth.claims_register`, `growth.claim_usages`, CMS pages and web experiments stay in P13. `mkt` holds campaigns, content calendar items for non-web channels, assets, sends, audiences, PR, partnerships and attribution, and references CRM and CMS records by ID (by value across databases). Contact segments are `ops.crm_segments`; `mkt` adds send audiences and snapshots over them and a strategy catalogue of market segments (`mkt.market_segments`, SEG-*), which are not contact lists; partner organisations and the partnership pipeline are Appendix X records. `mkt` lives in the isolated business database together with `growth` and `ops` (Appendix X D3-20): DB role `eq_mkt` holds `USAGE` on `mkt` and `SELECT` only on `ops.crm_marketing_view`; no grants to or from the core case database; only allow-listed events cross (FR-P13-26). Web content (pages, articles, landing pages) is authored and approved in the P13 CMS; the `mkt` calendar item links to the CMS page version and does not run a second review for it. |
| X-54 | Advocate and professional referral rewards | Appendix O deny-list X-11 ("non-cash credits only") and P13 FR-P13-20(b) (platform credits for advocates) are **amended**: no referral reward of any kind to advocates, CAs, CSs or CMAs or their firms (D3-27). RS-29 is registered in Appendix AB as Prohibited (N4). Partner types "CA, CS, law firm/advocate" in FR-P13-20 become relationship partners with `reward_eligible = false` (locked). Consistent with master X-62 (Appendix AB AB-R4, AB-R8), which records the same supersession for Appendix O S-15, Appendix B Card CH and §B.10. |
| X-55 | Flag and setting names | CRM objects have one system of record, `ops.crm_*` (Appendix X X-51); `growth.leads` is only the web capture inbox and any other `growth.*` CRM name (`growth.accounts`, `growth.opportunities`, `growth.contacts`) is an alias or compatibility view only, never written by v3 code. Flags named `growth.*` in P13 and [RD] for marketing tools are aliased (Appendix V X-44 alias table) to the `mkt.*` flag names registered by the connector owner in Appendix AC §AC.17 (`growth.brevo.sms_whatsapp.enabled` → `mkt.brevo.sms_whatsapp.enabled`; `ops.adobe_embed.enabled` → `mkt.adobe_embed.enabled`); the seed loader accepts the old names for one release. [RA]'s `mkt.sponsored_placement` and `mkt.sponsorships` are **not** marketing objects: sponsored placement is `marketplace.paid_placement` in schema `mkp` (NN-34). Feature flags that gate a vendor, legal or Board dependency keep the form `mkt.<module>.<flag>` (G, `core.feature_flags` store per V X-44); every other marketing setting follows `<scope>.mkt.<module>.<key>`. |

### Y.0.5 Locked marketing rules (tier L; summary of the rules this appendix enforces)

| ID | Rule | Source |
|---|---|---|
| ML-01 | No case, grievance, POSH, HR, payroll, health or family-safety data enters `mkt`, any marketing tool, audience, prompt or report; case lifecycle reaches marketing only as allow-listed aggregate counts or as a consented filer's own conversion event | NN-07, NN-16; FR-P13-23, FR-P13-26; [RB] X-20 |
| ML-02 | Served respondents are suppressed from every marketing channel, audience upload and CRM import unless they gave separate, revocable marketing consent outside the case flow | NN-16; FR-P13-26(c) |
| ML-03 | Every public statistic, badge, logo, testimonial, comparison, price statement and legal-effect statement on any marketing surface resolves to an active Claims Register record or a fee token | NN-17; FR-P13-10 |
| ML-04 | No paid or sponsored visibility for neutrals in any marketing content (the only paid visibility is the labelled Private Practice Marketplace slot under NN-34, which marketing never amplifies or describes as a ranking); no "top", "best", "premium", "featured", "recommended" or ranking language about any neutral or professional | NN-28, NN-34; X-03 (App. O); [RB] X-18 |
| ML-05 | No referral reward to advocates, CAs, CSs or CMAs (D3-27); Equator never helps an advocate solicit work | BCI r.36, r.37; NN-34 |
| ML-06 | No prohibited funnel technique (MT register §Y.7.1, class P); no dark pattern (DP-01–DP-13) | NN-29; Dark Patterns Guidelines 2023 |
| ML-07 | No AI-generated copy, image, video, caption or reply is published or sent without human approval; synthetic people are never shown as customers, parties, neutrals or staff | NN-01 GX-7; §Y.4.4 |
| ML-08 | Marketing consent is never inferred from a case, grievance, support or transactional interaction, and is never bundled with service consent | DPDP Act 2023 s.6; DPDP Rules 2025 r.3; FR-P13-22 |
| ML-09 | No purchased, scraped or rented contact lists; no bulk import without a consent artefact per contact; no scraping of Bar Council rolls or institute directories | NN-39; DPDP s.6 |
| ML-10 | No lookalike or custom audiences built from customer, case, party or neutral lists; no retargeting pixels on case, hearing, grievance, POSH, payment or sealed pages, or on FAM/POSH/health topic pages | FR-P13-26(d); NN-16 |
| ML-11 | Equator never comments publicly on an individual case or party, and never confirms that a person is a party, even if the person posts about it | A&C Act 1996 s.42A; NN-26; Appendix U ESC-2026.1 |
| ML-12 | No marketing statement that Equator, a training provider or a partner is approved, recognised, endorsed or certified by a regulator, court or government body unless a `regulatory_status` claim is active | NN-17; LINT-003 |
| ML-13 | Mass sends, public claims, pricing claims, testimonials and sensitive targeting require the human approvals in §Y.7.9; a user cannot approve their own item | NN-36 (maker ≠ checker) |
| ML-14 | Every external marketing tool sits behind a port with a declared system of record and a fallback; switching off a vendor never stops consent withdrawal, suppression or evidence retention | NN-40 |

---

### Y.0.6 v3.2 — Tag management and marketing tooling under IPB-04 *(v3.2, 26 October 2026)*

The IPB-04 §04.3.10 marketing tooling is adopted through P13 FR-P13-V32-10: a `TAG_MANAGER_PORT` with adapters `none` (default), `gtm_web` (GTM web container with Consent Mode v2 defaults denied) and `gtm_server` (server-side container on Equator infrastructure, first-party endpoint, IP truncation, redaction of personal fields), one adapter per brand pack, pending the owner's decision (IPB README §7 item 5; Appendix J V32-OI-09); `ANALYTICS_PORT` adapters `posthog` (self-hosted, current default), `ga4`, `matomo`, `plausible`, `none`; server-side UTM and click-id capture keyed to the anonymous consent id; lead forms through `CRM_PORT.upsertLead` with consent receipts; `mkt.webhooks` fan-out with Standard Webhooks signatures. **ML-10 is unchanged and remains L**: pixels load only in the `marketing` consent category, only on public marketing routes, and never on routes tagged `case`, `hearing`, `grievance`, `posh`, `payment`, `sealed`, `fam` or `health` (`platform.mkt.pixels.blocked_route_tags`); no lookalike or custom audiences from case, party or neutral lists (NN-16); a tag manager never changes this — the consent-mode defaults deny all storage until the CMP grants a category, and the route-tag block is enforced server-side before any tag is injected. Social clip export from the tutorials pipeline (IPB-07-54) enters the Y §Y.4 calendar as a content item of type `clip` with the same lint and approval. GrowthBook experiments continue (§Y.3.5) with the IPB-04-90 prohibited-route list. Brand assets move to the `brand_pack` (D3-57); the DAM (§Y.5.1) references pack media IDs.

## Y.1 Workspace architecture

### Y.1.1 Placement

The workspace is the **Marketing** area of the Operations Platform (`apps/ops`, Keycloak client `eq-portal-ops`, phishing-resistant MFA mandatory). It is company-scoped: Equator Resolution Service Private Limited is the first company; Finbyx and Udofin may run their own marketing workspaces on the same engine (D3-02), each isolated by legal entity (NN-38). Default owning departments (D3-06): **Marketing, Brand and Content**; **Social Media and PR**; **Partnerships and Collaborations**; with **Sales and Business Development** consuming leads through the Appendix X CRM.

| Module (NestJS bounded context `mkt` in `apps/api`) | Purpose | Main tables |
|---|---|---|
| `mkt-strategy` | Objectives, key results, market segments (SEG-*), ICPs, messaging houses | `mkt.objectives`, `mkt.key_results`, `mkt.market_segments`, `mkt.icp_profiles`, `mkt.messaging_houses`, `mkt.messaging_pillars` |
| `mkt-campaigns` | Briefs, budgets, channels, timelines, approvals, UTM links, experiments | `mkt.campaigns`, `mkt.campaign_channels`, `mkt.budgets`, `mkt.budget_lines`, `mkt.spend_entries`, `mkt.utm_links`, `mkt.experiments`, `mkt.experiment_variants` |
| `mkt-content` | Content and social calendar, reviews, hand-off, publication evidence | `mkt.content_items`, `mkt.content_versions`, `mkt.content_reviews`, `mkt.content_claim_refs`, `mkt.handoff_packages`, `mkt.publications` |
| `mkt-social` | Social accounts, adapters, engagement triage | `mkt.social_accounts`, `mkt.social_adapter_state`, `mkt.engagement_items` |
| `mkt-brand` | Asset library (DAM), rights, consents, boilerplates, co-branding | `mkt.assets`, `mkt.asset_versions`, `mkt.asset_rights`, `mkt.asset_consents`, `mkt.asset_usages`, `mkt.boilerplates`, `mkt.cobrand_approvals` |
| `mkt-messaging` | Send audiences (over Appendix X segments), sends, send-time consent checks (reading `ops.crm_marketing_view`), marketing suppression, frequency caps, sender domains | `mkt.audiences`, `mkt.audience_snapshots`, `mkt.sends`, `mkt.send_approvals`, `mkt.suppressions`, `mkt.frequency_counters`, `mkt.sender_domains` |
| `mkt-growth` | Lead magnets, landing-page registry, nurture sequences, webinars and events, referral programmes | `mkt.lead_magnets`, `mkt.landing_pages`, `mkt.sequences`, `mkt.sequence_steps`, `mkt.events`, `mkt.event_registrations`, `mkt.referral_programmes`, `mkt.referral_codes`, `mkt.referral_rewards` |
| `mkt-pr` | Media list, releases, coverage, spokespersons, crisis | `mkt.media_contacts`, `mkt.press_releases`, `mkt.coverage_items`, `mkt.spokespersons`, `mkt.crisis_incidents`, `mkt.crisis_statements` |
| `mkt-partners` | Collaboration records on Appendix X partners and pipeline, MoUs, obligations, joint events | `mkt.partnerships`, `mkt.mous`, `mkt.mou_obligations`, `mkt.joint_events` |
| `mkt-seo` | Intent clusters, briefs, programmatic template governance, AI-visibility backlog | `mkt.seo_intent_clusters`, `mkt.seo_briefs`, `mkt.programmatic_governance`, `mkt.ai_visibility_backlog` |
| `mkt-analytics` | Touchpoints, attribution models and results, dashboards, contribution feed | `mkt.touchpoints`, `mkt.attribution_models`, `mkt.attribution_results`, `mkt.metric_snapshots`, `mkt.contribution_metrics` |

### Y.1.2 Data flows (text diagram)

```
P13 public site (apps/web) ──forms/tools──▶ Appendix X CRM (ops.*) ◀──sync──▶ CRM_PORT (HubSpot/Zoho/Brevo CRM)
       │ page/claim events                         │ contact/account IDs (by value)
       ▼                                           ▼
 growth.claims_register ◀──claim_key lookups── mkt.* (Operations Platform DB plane) ──MARKETING_PORT──▶ Brevo (email)
       ▲                                           │            └─MESSAGING_PORT──▶ MSG91/Gupshup (DLT SMS, WhatsApp)
 P13 CMS (pages, landing pages) ◀──page_version_id─┤            └─SOCIAL_PORT────▶ LinkedIn / Meta / X / YouTube (flags OFF)
                                                   │            └─manual_handoff─▶ Adobe Express Content Scheduler (operator)
 core platform (cases)  ──allow-listed aggregate events only──▶ mkt-analytics          └─ANALYTICS_PORT─▶ PostHog/GA4 (consented)
 core consent ledger (core.consent_records) ──events──▶ ops.crm_comm_prefs (Appendix X mirror) ──▶ ops.crm_marketing_view (read by eq_mkt)
```

Rules: (a) the core case database never reads `mkt`; (b) `mkt` receives from core only `equator.notices.respondent.served.v1` (as a suppression hash, held in `growth.suppression_hashes`) and the FR-P13-23 allow-listed aggregates; consent state is read from `ops.crm_marketing_view` and is not mirrored a second time; (c) the outbox schema validator (FR-P13-26(b)) runs on every event entering `mkt` and rejects case identifiers, party names, pleadings and offers (`MKT_CASE_DATA_REJECTED`).

### Y.1.3 System of record per data category (NN-40; D3-25)

| Data category | System of record | Executors / copies | Sync direction | Conflict rule |
|---|---|---|---|---|
| Contact, account, opportunity | Appendix X CRM | Brevo contacts/companies/deals; HubSpot/Zoho | Equator → tool (batched); tool → Equator for engagement events only | Equator wins; tool edits to core fields are overwritten and logged |
| Marketing consent and withdrawal | Platform consent ledger (`core.consent_records`, purposes per FR-P13-22, per company scope), mirrored once in `ops.crm_comm_prefs` (Appendix X) | Brevo list membership and blocklist; MSG91/Gupshup opt-out lists; WhatsApp opt-out | Both ways for withdrawal (≤ 15 min); grant only from Equator | Withdrawal anywhere wins everywhere |
| Suppression | Respondent hashes: `growth.suppression_hashes` (P13; read by `ops` and `mkt`); channel suppressions (bounces, complaints, DND results, minors, legal holds, sunset, pending verification): `mkt.suppressions`; the contact flag `ops.crm_contacts.suppressed` is derived from both | Brevo blocklist; provider suppression lists | Equator → tool before every send | Union of all lists |
| Segments and audiences | Contact segments: `ops.crm_segments` (Appendix X); send audiences and frozen snapshots: `mkt.audiences`, `mkt.audience_snapshots` | Brevo static lists (pushed by `MARKETING_PORT`); ad platform audiences (B2B firmographic only) | Equator → tool | Tool-side segments are not used for sends |
| Partner organisations and partnership pipeline | Appendix X (`ops.crm_partners`, pipeline `partnership`) | — | — | Equator wins |
| Content, approvals, publication evidence | `mkt.content_*`, `mkt.publications`; CMS for web | Adobe Express designs; social platforms | Equator → tool (hand-off); tool → Equator (URL, metrics) | Approved content hash is authoritative |
| Brand assets and rights | `mkt.assets` (S3, Object Lock for rights evidence) | Adobe Express libraries | Equator → tool; designer uploads exports back | Asset without rights record is unusable |
| Campaign results and engagement | Raw events: the executor that generated them (Brevo, platform); normalised touchpoints: `mkt.touchpoints`; reported figures: frozen `mkt.metric_snapshots` | Brevo reports; platform analytics | Tool → Equator (daily pull or webhook via the Appendix X ingress) | Raw-event disputes resolve to the executor; the frozen Equator snapshot is the reported figure |
| Spend | `mkt.spend_entries` reconciled to accounts payable | Ad platform invoices | Tool → Equator; finance reconciles | Accounts ledger wins |

These rows are registered in `cfg.system_of_record` (Appendix AC §AC.12.1, tier G); no marketing-local copy of the matrix exists.

### Y.1.4 Neutrality and group boundaries applied to marketing

1. Marketing teams see no case content. The `mkt` roles have no grants in the core database, and the Operations Platform's case-services views (Appendix X) are not in any marketing permission bundle.
2. Cross-company marketing (Equator ↔ Finbyx ↔ Udofin) requires (a) a consent purpose that names the receiving company, (b) a Group Data-Sharing Agreement row in `grp`, and (c) a time-limited grant (NN-38). Group cross-sell automation MA-26 stays OFF until the group consent design is approved ([RB] AU-26).
3. Borrower, policyholder or employee data held by Finbyx or Udofin is never a marketing source for Equator, and Equator case data is never a source for them (NN-38 last sentence).
4. Disclosure of commercial relationships (NN-16) applies to marketing: co-branded material with an enterprise customer carries the relationship statement from the boilerplate register (§Y.5.4), and partner status never implies influence over neutral selection.

---

## Y.2 Marketing strategy objects

### Y.2.1 Objectives and key results

`mkt.objectives` (company, period `YYYY-Qn` or `FYyyyy`, title, owner, department, status `draft → approved → active → closed`, approver ≠ owner) and `mkt.key_results` (objective, metric key from the metric dictionary §Y.11.5, baseline, target, direction, data source, confidence, owner). Rules:

1. A key result must use a metric from the dictionary; free-text metrics are rejected (`VALIDATION_FAILED`).
2. Prohibited key results (tier L): any target on settlement rate, award outcome, number of cases decided for a party type, neutral allocation, or respondent "conversion"; any target that can only be met with a prohibited technique (MT class P).
3. Key results roll up to department dashboards and feed Appendix Z only as team context unless an individual owner is named (§Y.11.7).
4. Quarterly close records attainment and a short narrative; edits after close are versioned.

### Y.2.2 Segment and ICP catalogue (defaults; tenant-configurable, tier T, with locked restrictions)

| Code | Segment | Buying centre / audience | Main pains (from App. P §1.5) | Offers (Appendix AB streams) | Permitted channels | Locked restrictions | Proof keys (claims) |
|---|---|---|---|---|---|---|---|
| SEG-LEN | Lenders: banks, NBFCs, HFCs, MFIs, fintechs | CEO, CRO, Head of Collections/Legal, Compliance, Company Secretary | RBI conduct rules, award challenge risk (CORE), volume and cost, grievance clocks | Lender programme (RS-03), GRM SaaS (RS-06), API (RS-08), clause registry | LinkedIn, email, webinars, events, industry bodies | Never "recover more/faster", "collections" framing (App. P §1.5); never borrower targeting; disclosure banner RA-7 | `ind.appointment_policy`, `svc.independence_pack`, `svc.regulator_clocks`, `host.india` |
| SEG-INS | Insurers | Head of Claims, Grievance Officer, Compliance | IRDAI grievance timelines, Ombudsman load | Insurer programme (RS-04), GRM | LinkedIn, email, events | No retail-arbitration copy (IRDAI copy limited per RV6); free Ombudsman first for policyholder content | `svc.regulator_clocks`, `ind.disclosures` |
| SEG-EMP | Employers | CHRO, ER head, POSH IC Presiding Officer, Company Secretary | POSH compliance, workplace conflict, Labour Codes | Employer programme (RS-05), POSH SaaS (RS-07), GRM | LinkedIn, email, webinars | Nothing discouraging a POSH complaint (LINT-016); no employee targeting | POSH checker results (aggregate) |
| SEG-HEI | Universities and higher-education institutions | Registrar, VC office, IQAC, ICC | UGC grievance regulations, POSH for HEIs | GRM (HEI variant), POSH SaaS, student programmes | Email, events, partnerships | Student data never a marketing source; minors excluded (DPDP s.9) | `svc.regulator_clocks` |
| SEG-LST | Listed companies | Company Secretary, Investor Relations, Legal | Investor grievance handling; SEBI ODR | GRM, enterprise contracts; SEC explainer only when `sec.smart_odr.enabled` | LinkedIn, email | No SEBI claim unless `reg.sebi_odri` active | `reg.sebi_odri` (gated) |
| SEG-MSM | MSMEs | Owner/founder, finance head | Unpaid invoices, contract disputes, cost | Business Assure (RS-12; OFF until AB-R6 clears), pay-per-case, clause kit | Search, social, email, chambers of commerce | No MSEFC referral claims while `com.msefc_referral_msp` OFF (MSMED s.18 referral to a mediation service provider not commenced — D2-26); no s.12A claims (LINT-007) | `fee.published`, `svc.explorer_free` |
| SEG-IND | Families and individuals | Individuals (18+) | Cost, deadlines, fear of court | Explorer (free), pay-per-case, one-time products | Search (contextual), owned content, WhatsApp only on request | Track A rules: calm voice, free forum first (NN-20), no urgency, no fear framing, no outcome language; no targeting by distress, health, religion, caste, family status or financial distress (§Y.7.10); respondents suppressed | `svc.free_forum_first`, `law.free_forums_exist`, `fee.b2c_total_incl_gst` |
| SEG-NRI | Non-resident Indians | Individuals abroad with Indian family property or family disputes | Distance, documents, registration | FAM and INT services, video hearings | Owned content, search, community partnerships | NN-08 property rules stated; no claims about foreign enforceability beyond `law.singapore_status`; GDPR/UK GDPR notices where targeted (NN-30) | `law.property_registration`, `law.singapore_status` |
| SEG-INT | International businesses | GC, legal ops, trade bodies | Neutral seat, enforceability, language | INT arbitration and mediation | LinkedIn, events, embassies/trade bodies | No "Singapore Convention enforceable" (LINT-008); no foreign office claims (E-03) | `law.singapore_status` |
| SEG-NEU | Neutrals (mediators, conciliators, arbitrators, experts) | Professionals, retired judges | Fair allocation, admin burden, practice building | Panel (₹0 listing), EQAP (RS-21), Private ADR Chambers (RS-09), memberships (RS-13) | LinkedIn, email, events, training partners | Never imply training, membership or Chambers purchase leads to appointments (E-14; NN-28); no paid-placement content in institutional-panel material; RS-19 sponsored listing is offered only to non-advocate private-practice neutrals and chambers on the Private Practice Marketplace surface while `marketplace.paid_placement` is ON, with the NN-34 label text, and never to advocates (NN-34; D3-01) | `grade.policy_published`, `alloc.published_rules`, `dir.no_paid_listing`, `ch.trial_14d` |
| SEG-ADV | Advocates and law firms | Advocates as users of the Counsel workspace | Matter admin across cases | Counsel workspace (RS-11) | LinkedIn, email, bar-association education | Equator advertises its own software only; no solicitation features, no lead sale, no rewards (D3-27); no "top advocate" content (ML-04) | `rep.loa_revocable` |
| SEG-TRN | Trainees and students | Law and management students, early-career professionals | Skills, credentials | Student Associate membership (₹0), moots, training referral (≥ 3 providers) | Universities, social, events | Institute promotion only with `academy.institute_referral` ON and disclosure (D2-17); no minors; no claim that training leads to empanelment | `qap.not_yet_imi_approved` |
| SEG-CHM | Private ADR Chambers prospects | Independent neutrals, small institutions | White-label practice | CH-LITE…CH-IAAS (RS-09, RS-36), staff/HR add-on (RS-10, OFF until UAT) | LinkedIn, email, webinars | "Court" naming forbidden (D2-16); no appointment influence | `ch.trial_14d` |
| SEG-PAR | Partners (non-professional) | HRMS/LOS vendors, chambers of commerce, industry associations, resellers | Revenue share, member value | Partner/reseller programme (RS-28) | Email, events | Written agreement; disclosure on referred tenant; professionals excluded from rewards (D3-27) | — |

`mkt.icp_profiles` adds firmographic fit criteria per B2B segment (industry codes, size bands, regulated-entity type, geography, volume band from FR-P13-19) used by the CRM fit score (Appendix X) and by B2B paid-media targeting. ICP fields may use only public company data (MCA, GSTIN, regulator lists) and data the contact supplied ([RB] AU-02).

### Y.2.3 Messaging houses tied to approved claims

A **messaging house** is the approved message architecture for one segment (or product × segment). Structure in `mkt.messaging_houses` and `mkt.messaging_pillars`:

| Element | Rule |
|---|---|
| Roof (umbrella message) | One sentence drawn from the locked lines in App. P §1.2 or a P-D02-compliant variant; no number |
| Pillars (3–4) | Each pillar has a headline, a two-sentence explanation and **at least one `claim_key`** (active or gated) as its proof; a pillar with no claim cannot be approved |
| Foundation | Identity line (`id.private_institution`), neutrality promise, free-forum promise where the segment includes individuals |
| Never-say | Inherits App. P §1.4 and the segment's locked restrictions (§Y.2.2); adds segment-specific banned frames |
| CTA verbs | From App. P §1.5 for the audience track |
| Locales | en-IN master; hi-IN and others only through the P13 FR-P13-25 workflow with legal-translator review (NN-23) |
| Status | `draft → in_review → approved → active → retired`; approval: `marketing_manager` + `legal_reviewer` (≠ author) |

Content items reference a messaging house version; the content linter warns (W) when a content item uses a pillar headline not in the referenced house, and blocks (B) when it cites a claim key that the house does not list for that segment. When a claim expires, every house listing it is flagged and every scheduled content item using it is held (`MKT_CLAIM_UNRESOLVED`) until the claim is renewed or its fallback text is approved.

**Seed houses (examples; legal review required before activation).**

| House | Roof | Pillars → claim keys |
|---|---|---|
| MH-LEN-01 Lender programme | "Fair to your customers. Defensible to your regulator." (process aspiration; never next to a regulator name — App. P §1.5) | Appointment independence → `ind.appointment_policy`, `svc.independence_pack`; Regulator-mapped clocks and MIS → `svc.regulator_clocks`; Integration → (gated) API availability claim; Honest disclosure → `ind.disclosures` |
| MH-IND-01 Individuals | "Understand your options free, see the free public forum first, and settle only if you agree." | Free information first → `svc.explorer_free`, `svc.free_forum_first`; You decide → `law.mediation_voluntary`; Published fees incl. GST → `fee.b2c_total_incl_gst`; Your language → `lang.live` |
| MH-NEU-01 Neutrals | "Resolve disputes. Build your practice. On your terms." (WC-42) | Merit-based allocation → `alloc.published_rules`, `grade.policy_published`; No paid ranking or appointments in the Equator panel → `dir.no_paid_listing` (claim text scoped to the institutional directory and allocation, NN-34); Admin removed → (gated) feature claims; Fair assessment → `qap.not_yet_imi_approved` |
| MH-EMP-01 Employers | "Workplace disputes and POSH duties, handled on the record." | POSH compliance → POSH SaaS feature claims (gated); Confidentiality → `conf.caucus_sealed`; Regulator clocks → `svc.regulator_clocks` |

---

## Y.3 Campaign management

### Y.3.1 Campaign brief (required fields before `in_review`)

| Field | Rule |
|---|---|
| Name and code | Code generated `CMP-{yyyy}-{seq}`; name ≤ 80 characters |
| Objective / key result | FK to `mkt.key_results` (mandatory) |
| Segment(s) and messaging house | FKs; a campaign targeting SEG-IND inherits Track A rules (§Y.2.2) and risk tier floor R2 (§Y.4.3) |
| Offer | Lead magnet, event, product or plan; product offers must reference a published plan or fee schedule (no price typed into the brief) and a revenue stream that is `live` in the campaign's scope (D3-08; Appendix AB AB-R1) |
| Channels | From the channel catalogue (§Y.4.1); each channel row has owner, dates, budget line and adapter |
| Audience definition | FK to `mkt.audiences`; sensitive-targeting check runs at save (§Y.7.10) |
| Timeline | Start, end, key milestones; content items generated as calendar placeholders |
| Owner and team | Owner (`marketing_manager` or delegate), contributors; approver ≠ owner |
| Budget | Budget lines by channel and cost type (paid media, production, tools, events, agency, sponsorship, printing); currency INR, amounts in minor units, GST treatment stated (input tax credit eligibility recorded by finance) |
| Measurement plan | Primary metric (from dictionary), secondary metrics, attribution model version, UTM set |
| Risk and compliance notes | Auto-filled: claims used, risk tier, flags depended on (e.g., `academy.institute_referral`), counsel items |

### Y.3.2 Campaign states

`draft → in_review → approved → scheduled → live → paused → completed → closed (results recorded) | cancelled`. Transitions: `in_review → approved` needs `marketing_manager` approval plus a budget approval per the authority matrix (§Y.3.3); `live → paused` is automatic when a dependent claim expires, a flag turns OFF, a kill switch fires, a crisis at level C1/C2 opens (§Y.8.4) or spend reaches 100% of the approved budget; `completed → closed` requires a results record (metrics snapshot, learnings, decision on reuse).

**Clone and campaign templates.** *(v3.1)* `Clone` copies the brief, channels, budget lines (amounts reset for fresh approval), UTM set (new codes), audience definition (never the old snapshot), linked sequences and checklists, shifts all dates by a chosen offset and re-validates every claim, flag and stream. Seed templates by segment and offer (`CT-<SEG>-<OFFER>`, e.g., `CT-LEN-WEBINAR`, `CT-EMP-POSHCHECK`, `CT-NEU-EQAP`) pre-fill channel mix, risk floor, measurement plan and the matching TPL-MKT automations (§Y.7.8).

### Y.3.3 Budgets and spend (NN-36)

1. **Authority matrix** (`ctl`, NN-36) sets approval limits by role and amount. Defaults (tier G for limits, editable by `finance_ops` + `ops_director` within platform bounds): campaign budget ≤ ₹50,000 → `marketing_manager`; ≤ ₹5,00,000 → `marketing_manager` + `department_head` (Marketing); > ₹5,00,000 → + `ops_director` (or the CFO role named in `ctl`). Amounts exclusive of GST; the approval screen shows GST and the total.
2. **Separation of duties:** the person who approves a budget cannot create the vendor/payee, approve the vendor invoice and record the payment (NN-36). Agency and influencer payees are created through the Appendix X/`ctl` payee workflow with cooling-off and out-of-band confirmation for bank details.
3. **Spend entries** come from ad-platform invoices, vendor invoices and card statements; each entry links to a budget line; unlinked spend is an exception reported weekly. Spend above 90% of a line sends an alert; 100% pauses the line's paid channels (configurable, tier T: `tenant.mkt.budget.pause_at_pct`, default 100).
4. **No payments to journalists for coverage, and no undisclosed paid endorsements.** Any paid influencer, creator or publication placement is recorded as `paid_partnership = true`, and the content carries the disclosure label (SL-13; CCPA Misleading Advertisements Guidelines 2022, material-connection disclosure [RB] §3.2(5)).
5. **Payments to professionals:** a payee flagged `professional_class ∈ {advocate, ca, cs, cma}` cannot receive any referral or promotion payment (D3-27). Fees for genuine services (for example, a CA firm engaged for audit work, an advocate engaged as a webinar speaker for an honorarium) are allowed only through a services contract that does not depend on work or users referred, and are recorded with `purpose = 'services'` and reviewed by `compliance_officer` **[VERIFY — open (counsel): speaker honoraria to advocates and r.36]**.

### Y.3.4 UTM and tracking conventions

| Parameter | Convention | Validation |
|---|---|---|
| `utm_source` | Platform or publisher, lowercase: `linkedin`, `instagram`, `facebook`, `x`, `youtube`, `brevo`, `whatsapp`, `sms`, `partner-{code}`, `event-{code}`, `press-{outlet}` | Must be in the source registry |
| `utm_medium` | `organic-social`, `paid-social`, `email`, `sms`, `whatsapp`, `cpc`, `display`, `referral`, `partner`, `event`, `pr`, `qr`, `video` | Enum |
| `utm_campaign` | `{yyyy}{q}-{segment}-{offer}` e.g. `2027q1-len-grm-webinar` | Must match an approved campaign code mapping |
| `utm_content` | Content item ID or variant ID (`ci-000123-v2`) | Must exist |
| `utm_term` | Paid search keyword (only for `cpc`) | Free text, ≤ 100 chars |

Links are generated by the link builder (`mkt.utm_links`) with an optional short link on an Equator-owned domain (`go.equatorresolution.in` — **[VERIFY — open: domain to be registered by IT]**) and a QR code for print/events. Hand-typed UTM links fail SL-08 (W) and the attribution job buckets unknown values as `unattributed`. UTM values never carry personal data (no email or phone in any parameter; validator rejects `@` and digit runs ≥ 8 — `MKT_UTM_INVALID`). Links into authenticated or case routes are rejected (no tracking parameters on `/app`, `/verify`, `/track`, `/r/*`).

### Y.3.5 Experiments

Experiments on the public website run in the P13 engine (FR-P13-24); experiments on email, social and ads are registered in `mkt.experiments`. One register covers both: P13 experiments are mirrored by ID so results sit beside campaign data.

| Field / rule | Detail |
|---|---|
| Hypothesis | "If {change} for {audience}, then {metric} will {direction} by ≥ {MDE}, because {reason}" — mandatory |
| Primary metric | One metric from the dictionary, declared before start; secondary metrics optional |
| Audience and allocation | Audience FK; split ratio; minimum sample per variant computed from baseline, MDE and power (defaults: α = 0.05, power 0.8, tier T) |
| Variants | Each variant is an approved content version (all variants pass the same review tier); fee figures, legal-effect statements, free-forum blocks and consent wording cannot vary (FR-P13-24) |
| Prohibited surfaces (tier L) | `/fees`, rules, legal pages, free-forum blocks, consent forms' purpose text, cancellation flows, any page or message to individuals that varies urgency, fear or price framing; respondents |
| Stop rules | Fixed horizon by default; early stop only for harm (complaint rate, unsubscribe rate or spam-complaint rate above threshold) — `tenant.mkt.experiment.harm_stop_unsub_pct` default 1.0 |
| Result and decision | Result record (effect, CI, sample, guardrail metrics), decision `adopt`, `reject` or `iterate`, decided by `marketing_manager`; adopted variant becomes the default content version |
| Audit | Exposure logged (`experiment_exposed`), start/stop/decision hash-chained |

---

## Y.4 Content and social calendar

### Y.4.1 Content item types and channel catalogue

| Type code | Item | Authored in | Review route | Publish route | Evidence |
|---|---|---|---|---|---|
| WEB | Web page, landing page | P13 CMS | CMS legal workflow (FR-P13-09) | CMS publish | CMS publish event |
| BLOG | Article, explainer, guide | P13 CMS | CMS legal workflow | CMS publish | CMS publish event |
| NEWS | Newsletter issue | `mkt-content` (email builder) | §Y.4.3 tier ≥ R1 | `MARKETING_PORT` (Brevo) or SES fallback | Send record + rendered HTML hash |
| EML | Campaign or nurture email | `mkt-content` | §Y.4.3 | `MARKETING_PORT` | Send record |
| SMS / WAM | Promotional SMS; WhatsApp marketing template | `mkt-content` | ≥ R2 (DLT/Meta template text is fixed) | `MESSAGING_PORT` (DLT promotional route; Meta marketing template) | Provider message IDs |
| LI / IG / FB / XP | LinkedIn, Instagram, Facebook, X post (image, carousel, text, link) | `mkt-content`; design in Adobe Express | §Y.4.3 | Adobe Content Scheduler (manual), native app, or `SOCIAL_PORT` | §Y.4.8 |
| YTV / SRT | YouTube video; Shorts / Reels | `mkt-content`; edit in Adobe Express or video tool | ≥ R1; captions mandatory | YouTube upload (manual or `youtube_data` adapter); Reels via Adobe/IG | §Y.4.8 |
| WBN | Webinar (and its promotion set) | `mkt-growth` event | ≥ R2 for speaker content | Event tool + promotion items | Event record, recording |
| EVT | Event (conference, roundtable, workshop, moot) | `mkt-growth` event | ≥ R1; sponsorship check | Promotion items | Event record |
| TRP | Training promotion (Equator modules; referral to ≥ 3 providers) | `mkt-content` | R2; D2-17 checks | As channel | As channel |
| PTN | Partner or co-branded content | `mkt-content` | R2 + co-brand approval (§Y.5.5) | As channel | As channel + partner approval |
| PRS | Press release, statement | `mkt-pr` | R3 (§Y.8.2) | Newswire/email to media list | Release record |
| ADS | Paid ad (search, social, display) | `mkt-content` | ≥ R2; R3 for individual-facing | Ad platform (manual entry or adapter, flags OFF) | Ad ID, screenshots |

### Y.4.2 Calendar and item lifecycle

```
idea → briefed → drafting → brand_review → compliance_review → approved → handoff_ready → scheduled → published → tracking → archived
                     ▲           │                 │                                  │            │
                     └─changes_requested◀──────────┘                                  ├─ held (claim expired / flag OFF / crisis pause / rights expired)
                                                                                      ├─ taken_down (correction or removal)
                                                                                      └─ evidence_overdue (no URL/screenshot after T+24h)
```

| Transition | Who | Gate (system-enforced) |
|---|---|---|
| `drafting → brand_review` | Author (`content_writer`, `social_media_executive`, `designer`) | All lint B-rules pass (LINT and SL); every image has alt text; every video has captions; claims resolved; UTM links valid |
| `brand_review → compliance_review` | `marketing_manager` or brand reviewer (≠ author) | Brand checklist ticked (§Y.5.2); asset rights valid through the scheduled date + `tenant.mkt.asset.rights_buffer_days` |
| `compliance_review → approved` | `legal_reviewer` for R2; `legal_reviewer` + `compliance_officer` for R3; skipped for R0/R1 unless sampled | Legal checklist (App. P §7.3 items applicable to the channel + §Y.4.5); reviewer ≠ author ≠ brand reviewer for R3 |
| `approved → handoff_ready` | System | Approved content hash frozen; hand-off package generated (§Y.4.7) |
| `handoff_ready → scheduled` | `social_media_executive` (or system for API adapters) | Scheduled time inside the item's validity window and outside crisis pause; adapter enabled or manual route selected |
| `scheduled → published` | Operator confirmation (manual) or adapter callback | Evidence captured (§Y.4.8) |
| any → `held` | System | Claim expiry, flag change, crisis pause, rights expiry, kill switch; owner notified; resumes only after re-approval if content changed |
| `published → taken_down` | `marketing_manager`, `legal_reviewer`, `pr_manager` | Reason, correction note; App. P §7.6 SLA (legal-effect/safety errors within 24 h; others within 7 days) |

**Review SLAs and lead time.** *(v3.1)* Each review stage has a target in business hours (`tenant.mkt.review.sla_hours.<stage>.<tier>`, T): brand review 8 h for every tier; compliance review 16 h (R2) and 24 h (R3); crisis statements 1 hour, 24×7 (G). **Minimum lead time** = the sum of stage targets for the computed tier + `tenant.mkt.review.buffer_hours` (8); an item may be scheduled inside its lead time only through an "expedite" request that the reviewer accepts (reason logged), otherwise the scheduler offers the earliest feasible slot (CC-05). Review queues are **deadline-ordered** (scheduled time minus remaining SLA) with timers; reminder at 50 %, escalation to the Marketing `department_head` at 100 %. The SLA clock pauses only in `changes_requested` and restarts on resubmission; reviewer absence never pauses it — the queue moves to the reviewer's delegate (same bundle, never the author; Appendix X §X.3.5). KPIs: review cycle time by tier, first-pass approval rate, SLA attainment, expedite rate.

Any edit to an approved item creates a new version and returns it to `brand_review` (or to `compliance_review` if the risk tier is R2+). The approved hash is computed over caption text per channel, hashtags, mentions, link targets, asset SHA-256 values and alt texts.

### Y.4.3 Risk tiers (review routing)

| Tier | Typical content | Review | Sampling |
|---|---|---|---|
| R0 Routine | Reposting already-approved content unchanged; event logistics; holiday greetings without product or legal reference | Brand review only | 5% monthly by `legal_reviewer` |
| R1 Standard | Product features using only active claim nodes and approved boilerplates; recruitment posts (careers copy approved by HR) | Brand review + automated lint | 10% monthly |
| R2 Legal-sensitive | Any statute, regulator, legal effect, process explanation or vertical content; pricing or fees; testimonials, case studies, logos; partner or co-branded content; neutral or advocate features; statistics; training promotion; all SMS/WhatsApp templates; paid ads | Brand + `legal_reviewer` | 100% |
| R3 High-risk | FAM, POSH, health, safety or child-related topics; individual-facing paid ads; crisis statements; comparative statements naming a competitor; government or regulator partnership announcements; mass sends above the threshold; any content in a new language for the first time | Brand + `legal_reviewer` + `compliance_officer` (or `ops_director` for crisis) | 100% |

The tier is computed by rules (type, segment, detected entities, lint hits, claims used, audience size) and is a **floor**: a reviewer may raise it, never lower it below the computed tier (`MKT_REVIEW_REQUIRED`).

### Y.4.4 AI-assisted drafting in the calendar

AI drafts (P11 addendum, §Y.20) are allowed for captions, variants, alt text, subtitles, summaries and translation drafts. Rules: drafts carry `ai_generated = true` and the prompt version; the model receives only the messaging house, approved claim texts, boilerplates and the brief (no CRM personal data, no case data — ML-01); every AI draft passes lint and the normal review tier; generated images or video are labelled internally `synthetic = true` and must not depict a real person, a realistic customer, party, neutral or staff member, a court or hearing scene presented as real, or a regulator's emblem; public synthetic imagery carries the platform's AI-content label where the platform provides one **[VERIFY — open: platform labelling requirements and any Indian rule on synthetically generated content in force]**.

### Y.4.5 Social and channel lint rules (SL-01–SL-20; additive to LINT-001–LINT-050)

Severity **B** blocks submission; **W** warns; † non-overridable. Implemented in `packages/content-lint` as a channel profile `social`, `email`, `sms`, `whatsapp`, `ads`, `press`.

| ID | Rule | Detection / check | Sev. |
|---|---|---|---|
| SL-01 | Case-identifying content | Case number patterns (`EQR-[A-Z]{3}-\d{4}-\d+`), "my case", "hearing today with", award/settlement screenshots, party names on the respondent suppression list (HMAC match on handles/emails in mentions) | B† |
| SL-02 | Regulator, court or government tag implying endorsement | Mentions or hashtags of regulators, courts, ministries (`@RBI`, `#SEBIApproved`, `#GovtApproved`) unless the item is an R3 announcement backed by an active `regulatory_status` claim | B† |
| SL-03 | Neutral or professional promotion | Named neutral or professional without a consent record (§Y.5.3); any outcome statistic; "top/best/leading/expert/specialist" about a person; advocate content beyond the BCI r.36 Schedule facts | B† |
| SL-04 | Testimonial or endorsement without claim | Quotation marks + person/organisation attribution outside a `testimonial` claim node | B† |
| SL-05 | Engagement bait and urgency | "comment YES", "tag 3 friends", "only today", "last chance", "hurry", countdown emoji runs | B |
| SL-06 | Alt text | Image without alt text (≥ 15 characters, not the file name) | B |
| SL-07 | Captions and transcript | Video without captions (SRT/VTT) or, for videos > 60 s, without a transcript link | B |
| SL-08 | Tracking | Link without a link-builder UTM | W |
| SL-09 | Link target | Link to a domain not on the allow-list (`tenant.mkt.link.allowed_domains`) or into authenticated/case routes | B |
| SL-10 | Hashtags and mentions | More hashtags than `tenant.mkt.social.max_hashtags.<platform>`; mention of an account not on the approved handle list | W |
| SL-11 | Brand neutrality | Political, religious or communal content; commentary on pending cases or judges | B (R3 route) |
| SL-12 | Comparative claims | Competitor named or identifiable with a comparative or disparaging statement | B unless R3 approved; never about competitors' figures ([RA] F6 implication) |
| SL-13 | Paid partnership disclosure | `paid_partnership = true` without "Paid partnership" / "Sponsored" label on first screen / first line | B† |
| SL-14 | People in images | Asset depicting an identifiable person without an active consent record; any minor | B† |
| SL-15 | Related-entity disclosure | Equator ADR Institute, Infrabyx group companies or Equa Trainings mentioned without the relationship disclosure (D2-17; [RE] F3.1 r.5(6) note) | B |
| SL-16 | "Free" | "free" without a `svc.*` or `fee.*` claim showing the user pays nothing (CCPA Misleading Advertisements Guidelines 2022, free claims [RB] §3.2(5)) | B |
| SL-17 | Price | Any price not from a fee token or published plan; strike-through price without stored prior price (lowest in prior 30 days — 2026 amendment as reported [RB] §3.2(3) **[VERIFY — open: Gazette text]**) | B† |
| SL-18 | Legacy brands and remediation | U.12 patterns E-01–E-17; "Equa", "Equa.Law", "Private ADR Court", legacy domains and phone numbers | B† |
| SL-19 | Fear and distress framing to individuals | "before it's too late", "you could lose everything", "they will take your house", shame language, in SEG-IND/SEG-NRI items | B† |
| SL-20 | Sensitive-topic hashtags and imagery | Hashtags or imagery about domestic violence, sexual harassment, divorce or illness used to promote a paid service | B (R3 route) |

### Y.4.6 Publication routes by platform (defaults)

| Platform | Default route | API adapter (flag; default) | Access gate and limits ([RD] F3.3) | Notes |
|---|---|---|---|---|
| LinkedIn company page | Adobe Content Scheduler or native app (manual) | `linkedin_cm` (`mkt.social.linkedin_cm.enabled`; OFF) | Community Management API is a vetted product: development tier then Standard tier after a screencast per use case; new developer app with no other API product; versioned APIs with sunsets | Page analytics pull via the same adapter when ON |
| Instagram professional account | Adobe Content Scheduler (manual) | `meta_graph` (`mkt.social.meta_graph.enabled`; OFF) | Content Publishing with `instagram_business_content_publish` / `instagram_content_publish`; media at a public URL at publish time; 100 API posts per 24 h stated (50 stated elsewhere) — counter default 50 (`tenant.mkt.social.ig_daily_cap`) | JPEG only for images; carousels ≤ 20 |
| Facebook Page | Adobe Content Scheduler or native (manual) | `meta_graph` | `pages_manage_posts` with App Review and Business Verification **[VERIFY — open: not fetched]** | — |
| X | Adobe Content Scheduler (manual) | `x_v2` (`mkt.social.x_v2.enabled`; OFF) | Pay-per-use credits: post create USD 0.015; with URL USD 0.200 (as stated by X) | Monthly credit budget `tenant.mkt.social.x_monthly_budget_usd` |
| YouTube (videos, Shorts) | YouTube Studio (manual) — Adobe scheduler does not list YouTube | `youtube_data` (`mkt.social.youtube_data.enabled`; OFF) | `videos.insert` uses a separate upload bucket, 100 calls/day; ≤ 256 GB | Captions uploaded with the video |
| Others (TikTok, Pinterest) | Not used by default | — | — | Enable only by D3 decision |

Each adapter's flag may be turned ON only by `marketing_manager` (maker) + `legal_reviewer` (checker) per Appendix AC §AC.17, after the platform's access grant is recorded (document upload) and `it_admin` has recorded a security review of token storage (secrets in the vault; tokens never in `mkt` tables). Publishing through an adapter still requires the item to be `approved`; adapters never publish AI copy that has not been approved (ML-07).

### Y.4.7 Adobe Express hand-off package (D3-26)

Generated on `approved → handoff_ready`, shown on SCR-P17-08 and exportable as a ZIP (`HANDOFF_{item}_{yyyymmdd}.zip` containing `README.txt`, `caption_{platform}_{locale}.txt`, assets and `handoff.json`).

| Field | Content |
|---|---|
| Item and version | Content item ID, version number, approved content hash (SHA-256) |
| Target | Platform, account handle, post type (single image, carousel, video, Reel/Short, text), aspect ratio and size spec |
| Design | Adobe Express design share link (`design_link`); template ID from the brand library; "do not change text in the design" note when text is in the image |
| Assets | Final exported files (PNG/JPEG/MP4) with SHA-256 and DAM IDs; rights expiry dates |
| Caption | Final approved caption per platform and locale (character counts shown against platform limits) |
| Hashtags and mentions | Approved list; mentions only from the approved handle list |
| Link | Short link with UTM; first-comment link where the platform penalises links (optional) |
| Accessibility | Alt text per image; captions file (SRT/VTT) for video; transcript link |
| Disclosures | Paid partnership label, related-entity disclosure, AI-content label if applicable |
| Schedule | Date and time (IST, with UTC), validity window (do-not-publish-after), crisis-pause status |
| Approvals | Reviewer names, roles, timestamps, risk tier; claim keys used and their expiry |
| Return instructions | "After publishing, record the post URL and upload a screenshot in Equator within 24 hours" |

Designs created through the Adobe Embed SDK inside the Operations Platform (flag `mkt.adobe_embed.enabled`, OFF; requires Adobe Developer Console project and Adobe review [RD] F3.2) are saved back to the DAM with their design link (design only — the SDK offers no scheduling or publishing [RD] F3.2); designs made natively in Adobe Express are exported and uploaded by the designer. In both cases the DAM copy, not the Adobe copy, is the approved asset.

### Y.4.8 Evidence of publication

| Route | Evidence captured | Verification |
|---|---|---|
| API adapter | Platform post ID, permalink, published timestamp, payload hash | Payload hash = approved hash (automatic); mismatch → incident |
| Adobe Content Scheduler / native app (manual) | Post URL, published timestamp (operator-entered, IST), screenshot upload (PNG/JPEG ≤ 5 MB, SHA-256, stored with Object Lock), operator attestation "Published exactly as approved" | Where a read adapter is enabled, caption text is fetched and compared; otherwise `compliance_officer` reviews a monthly sample (`tenant.mkt.evidence.sample_pct`, default 10%) by comparing screenshot and approved version |
| Email/SMS/WhatsApp | Send ID, provider message IDs, rendered content hash, recipient count, suppression report | Automatic |
| Press release | Distribution list snapshot (counts), newswire receipt, PDF of release | Automatic |

An item without evidence 24 hours after its scheduled time moves to `evidence_overdue` and alerts its owner and `marketing_manager`; repeated overdue evidence is a quality metric for the role (§Y.11.7). Evidence is retained for 8 years (aligned with the FR-P13-02 remediation evidence retention), or longer under legal hold.

### Y.4.9 Engagement and response tracking

Engagement items (comments, mentions, DMs, reviews) enter `mkt.engagement_items` from read adapters (when enabled) or manual logging by `social_media_executive`. Content of DMs is stored only as long as needed for routing (`tenant.mkt.engagement.retention_days`, default 90) and then reduced to category, timestamps and outcome.

| Category | Examples | Route | First response target (tier T) | Public reply rule |
|---|---|---|---|---|
| E1 Sales interest | "Do you work with NBFCs?" | Lead in Appendix X CRM (source `social_engagement`, MA-03), with consent capture link | 1 business day | Generic reply with contact link; no personal data in public |
| E2 Product/support question | Login, how to respond to a notice | Support ticket (Appendix X) | 4 business hours | Move to private channel; no case details |
| E3 Complaint about Equator's service | "Your team never replied" | Ticket converted to an `EQ_SERVICE` grievance (Appendix X §X.8; EGP-2026.1, Appendix U §U.6.4): acknowledgement within 48 h; resolution by the strictest applicable rule pack (Appendix X §X.8.3; E-Commerce Rules 2020 r.4(5): one month) | 4 business hours (acknowledge); grievance clock from the time the comment was received (triage rule 6) | Acknowledge publicly with grievance link; resolve privately |
| E4 Case-related | A party discusses their case, the other side or a neutral | Appendix X support ticket, category `case_procedure`, routed to the Case Services queue; no case link unless the requester later links one of their own cases in `/app/help`; nothing copied into `mkt` beyond category and ticket reference | 4 business hours | Template: "We can't discuss any matter publicly. Please contact us through {secure channel}." Never confirm a person is a party (ML-11) |
| E5 Media enquiry | Journalist question | PR queue (§Y.8) | 2 business hours | "Our communications team will respond." |
| E6 Abuse, harassment, threats | Threats to staff or neutrals | Moderation (hide/report per platform), safety log, security team | Immediate | No engagement |
| E7 Distress or safety | Self-harm, violence, child risk | Safety protocol: human responder, helpline information per App. E GX-5 handoff template | Immediate (staffed hours) | Private message with helpline information; escalate |
| E8 Misinformation or impersonation | Fake Equator accounts, false claims about Equator | PR + legal; impersonation playbook (§Y.8.4) | Same day | Correction from approved statement bank |
| E9 Careers | Job questions | HR (Appendix Z) | 2 business days | Link to `/careers` |
| E10 Spam | — | Hide/ignore | — | — |

Auto-classification (P11 `social_triage_classifier`) proposes a category; a human confirms before any reply; auto-replies are limited to acknowledgement templates for E1, E2 and E9 and are OFF by default (`tenant.mkt.engagement.auto_ack_enabled`). Replies on E3–E8 are always human-written from the approved response bank. Review sites (Google Business Profile and similar): Equator never offers incentives for reviews, never posts reviews itself, and replies factually; reviews are not imported as testimonials unless a `testimonial` claim with the reviewer's consent exists.


**Triage rules** *(v3.1)* (`tenant.mkt.engagement.triage_rules`, T within the locked order):

1. **Priority order (locked):** E7 > E6 > E3 > E4 > E5 > E8 > E2 > E1 > E9 > E10; the inbox sorts by priority, then by SLA remaining.
2. **Out of staffed hours** (`tenant.mkt.engagement.staffed_hours`, default 09:00–19:00 IST on business days): E7 pages the on-call `safeguarding_lead` and E6 the security on-call; other categories queue with business-hour SLAs.
3. **Threading:** items from one author on one post within 24 h merge into a thread; a repeat of the same complaint on another platform links to the existing ticket.
4. **Public-reply guard:** a public reply containing an email address, phone number, case-number pattern (SL-01) or a name on the suppression list is blocked and the "move to a private channel" template is offered.
5. **Hide, do not delete:** spam (E10) and abuse (E6) are hidden with platform moderation tools; deletion only for unlawful content or impersonation of Equator, with a screenshot kept as evidence.
6. **E3 clock:** the grievance `received_at` is the time the comment or message was received on the platform (or logged, if earlier capture is impossible) — Appendix X §X.8.2.
7. **Language:** routed to staff with that language skill; replies from the approved bank in that language, or English.
8. **Reclassification** into or out of E3, E4, E6 or E7 records a reason and is sampled weekly by `compliance_officer`.

### Y.4.10 Calendar conflict detection *(v3.1)*

Conflict checks run on save, on scheduling, on every drag-to-reschedule and nightly over the next 60 days; results show as badges on SCR-P17-07 and feed D-03 and the weekly review (§Y.11.8). **B** blocks scheduling (`MKT_CALENDAR_CONFLICT`); **W** needs an acknowledgement reason, which is logged.

| ID | Conflict | Detection | Sev. | Resolution offered |
|---|---|---|---|---|
| CC-01 | Audience over-messaging | forecast messages per contact across scheduled sends exceed a §Y.6.5 cap for > `tenant.mkt.calendar.overlap_pct` (10 %) of the snapshot | W (B for SEG-IND/SEG-NRI) | shift, merge sends or exclude the overlap |
| CC-02 | Same-account slot collision | two posts on one social account within `tenant.mkt.calendar.min_gap_minutes` (120) | W | next free slot |
| CC-03 | Embargo | item references a release or announcement before its `embargo_at` | B | move after embargo |
| CC-04 | Expiry before publish | a claim, asset right or co-brand approval expires before the scheduled time or validity window ends | B | renew, replace or reschedule |
| CC-05 | Review lead time | scheduled inside the minimum lead time (§Y.4.2) | B unless expedite accepted | earliest feasible slot |
| CC-06 | Blackout dates | `tenant.mkt.calendar.blackouts` (national mourning, open crisis, silent periods set by the Company Secretary) | B promotional; W informational | move outside the blackout |
| CC-07 | Quiet hours | SMS or WhatsApp outside the §Y.6.5 window | B | next window |
| CC-08 | Offer validity | promotes an offer, plan or event outside its validity or after capacity is full | B | correct or cancel |
| CC-09 | Competing campaigns | two live campaigns target one market segment with different primary offers within 7 days | W | sequence or merge |
| CC-10 | Owner or reviewer away | owner or required reviewer out of office that day with no delegate | W | assign a delegate |

**Bulk calendar actions.** *(v3.1)* Multi-select on SCR-P17-07: reschedule by offset, hold, release, reassign owner or reviewer; every selected item is re-validated against CC-01–CC-10 and its claim, rights and flag state, and items that fail stay unchanged with the reason shown; a bulk action is one audit event listing each item.
---

## Y.5 Brand management

### Y.5.1 Brand asset library (DAM)

Assets live in S3 (ap-south-1) under `mkt/assets/{company}/{asset_id}/{version}`; rights evidence (licences, releases, consents) is stored with Object Lock (compliance mode) and hashed into the audit chain (NN-22).

| Asset class | Metadata required | Rights record required | Notes |
|---|---|---|---|
| Logos and lock-ups | Variant, colour mode, minimum size, clear space, file formats (SVG, PNG 512 × 512 for `Organization.logo`) | Ownership (trade-mark application/registration number **[VERIFY — open: Equator trade-mark filings]**) | App. C §E.1 tokens prevail over Marketing Playbook palette (P-D09) |
| Colours and typography | Token names from App. C §E.1; font files and licence (Noto Sans Devanagari and script fonts per FR-P13-25) | Font licence (OFL or commercial) | Fonts outside the allow-list cannot be attached to templates |
| Templates | Channel, size, locked layers, editable fields, Adobe Express template ID | — | Templates include identity line slot and disclosure slot |
| Photographs and video | Subject type (people, place, object), location, date, photographer/creator | Licence (own, commissioned, stock licence ID and terms) **and** a consent record for each identifiable person | Minors: not used (tier L) |
| Illustrations and icons | Source, licence | Licence | — |
| Third-party marks (client, partner, media logos) | Owner, permitted use, expiry | Written permission (`client.logo` claim) | Expiry job removes from templates and holds items |
| Legacy (Equa) material | Legacy flag | — | Quarantined; cannot be attached (U.12, SL-18) |

**Usage-rights expiry.** `AssetRightsExpiryJob` (daily) raises `equator.mkt.asset.rights_expiring.v1` at T-30 and T-7 and on expiry: the asset is marked `expired`, removed from templates, scheduled items using it move to `held`, and published items using it are listed for review (remove, replace or renew). Consent withdrawal by a person in a photograph triggers the same flow immediately, and published items are taken down within `tenant.mkt.asset.consent_takedown_hours` (default 72; tier G, max 168).

### Y.5.2 Brand voice guide and brand review checklist

The voice is App. P §1.3 (Plain, Honest, Neutral, Calm, Specific, Humble) and the brand test (App. P §7.3 item 9). For social channels add: one idea per post; no slang that trivialises disputes; emoji only from the approved list and never in FAM/POSH/health content; no memes about litigants, courts, lawyers or judges; first person plural ("we") for Equator, never "our lawyers" (LINT-014). The brand reviewer ticks: (1) brand line and lock-up correct; (2) tokens and template unaltered; (3) voice anchors met; (4) accessibility (contrast ≥ 4.5:1 for text in images, alt text, captions); (5) correct disclosures; (6) no legacy material; (7) the brand test.

### Y.5.3 People in marketing: consent records

`mkt.asset_consents`: person reference (staff, neutral, partner representative, event attendee, model), scope (channels, purposes, territories), duration, withdrawal method, evidence (signed release PDF or e-sign record), DPDP itemised notice version. Rules: neutrals and staff are never required to appear in marketing as a condition of empanelment or employment (consent must be free — DPDP s.6); a neutral featured in marketing content gets no allocation, grading or directory advantage (NN-28; ML-04), and the content must not describe outcomes or settlement rates; advocate-neutrals are featured only with Schedule facts (name, qualifications, areas of practice) and only in institutional content (for example "meet our panel" explainers), never as promotion of their practice **[VERIFY — open (counsel): institution-run neutral features and r.36 — OI-03]**; event photography uses a notice at entry, a no-photo lanyard option and per-person consent for close-up use.

### Y.5.4 Approved boilerplates (register)

`mkt.boilerplates` holds versioned, approved text blocks sourced from App. P; content items insert them by ID so that updates propagate.

| ID | Use | Source |
|---|---|---|
| BP-01 | Press boilerplate: descriptor + identity line + entity particulars (`{{entity.legal_name}}`, CIN, registered office) | App. P §1.2 (A-03), §6.2 |
| BP-02 | Social bios (LinkedIn, Instagram, X, YouTube) — brand line + descriptor + identity line, within platform limits | App. P §1.2 |
| BP-03 | Email signature and footer: legal entity, CIN, address, grievance officer, privacy and unsubscribe links | App. O §6.3; [RB] Implications E.21 |
| BP-04 | Operator footer for landing pages and paid-webinar pages: legal entity, CIN, GSTIN, registered address, grievance officer, privacy, terms, refund links | [RB] Implications E.21 |
| BP-05 | Relationship disclosure — Equator ADR Institute (separate entity) | D2-17; P-D08 |
| BP-06 | Relationship disclosure — enterprise customer or partner co-branding | NN-16 |
| BP-07 | "Not legal advice" and identity notice for explainer content | App. P §1.7, LINT-014 |
| BP-08 | Paid partnership / Sponsored label text (en/hi) | SL-13; DP-09 |
| BP-09 | Webinar notices: recording, Q&A rule ("we cannot discuss individual matters"), recorded-on date for replays | §Y.7.4 |
| BP-10 | Mediation Act status note (FlagSwap while `mediation_statutory_mode` OFF) | App. P §7.4 |

### Y.5.5 Co-branding approvals (partners, customers, chambers)

| Case | Rule | Approvals |
|---|---|---|
| Partner co-branded content (university, chamber of commerce, industry body) | Signed MoU or letter with a publicity clause; partner's written approval of the specific asset; no statement implying the partner endorses Equator's neutrals or outcomes; Equator's identity line present | `partnerships_manager` + `marketing_manager`; `legal_reviewer` for R2+ |
| Enterprise customer case study or logo | `client.logo` / `case_study` claim with written permission and expiry; case studies are aggregate, anonymised, consented, and never describe a specific dispute's outcome for a party (NN-26; [RB] §4.1 social proof) | Claims owner + `legal_reviewer` |
| Private ADR Chambers tenant using Equator brand | "Powered by Equator" / "Room hosted on Equator" marks only, per brand rules; no "Court" (D2-16); chambers' own marketing is their responsibility under their plan terms, but Equator marks used by them must follow this appendix; Equator never markets a chambers' neutrals as Equator panel members | `marketing_manager`; `legal_reviewer` for any new mark usage |
| Government programme or public body | Use of names, emblems or logos only with written authorisation; never "approved/recognised" wording without a `regulatory_status` claim; emblem use subject to the State Emblem of India (Prohibition of Improper Use) Act 2005 and the Emblems and Names (Prevention of Improper Use) Act 1950 **[VERIFY — open (counsel): application to programme logos]** | R3: `legal_reviewer` + `compliance_officer` + `ops_director` |
| Group companies (Finbyx, Udofin) | Group brand architecture approved by the Company Secretary; `parentOrganization` markup only if approved (App. P §6.2); no cross-promotion to data subjects of another company without that company's consent scope (NN-38) | `group_admin` + Company Secretary |

`mkt.cobrand_approvals` stores partner, asset, scope, expiry, evidence and approver; expiry holds dependent items.

---

## Y.6 Email and messaging marketing

### Y.6.1 Channel matrix

| Channel | Executor (port → adapter) | Consent purpose (FR-P13-22) | Regulatory controls | Default |
|---|---|---|---|---|
| Marketing email, newsletters | `MARKETING_PORT` → `brevo`; fallback `ses_marketing` (separate SES configuration set and subdomain) | `marketing_email`, `newsletter`, `event_updates`, `partner_communications` | DPDP consent; unsubscribe in every message; List-Unsubscribe headers (§Y.6.4) | ON through `ses_marketing`; Brevo only when `mkt.brevo.enabled` (OFF until DPA and transfer-register row `BREVO_EU`, [RD] DI-B 11) |
| Promotional SMS | `MESSAGING_PORT` → `msg91` / `gupshup` (DLT promotional route) | `marketing_sms` | TCCCPR 2018 as amended (TRAI PR 11/2025): DLT-registered header and template in the promotional category, scrubbing against customer preferences, opt-out in each message, no re-ask for 90 days after opt-out [RB] §4.1 **[VERIFY — open: header suffix letters and permitted hours]** | ON |
| Brevo SMS / WhatsApp | `MARKETING_PORT` → `brevo` | — | DLT template-ID support not confirmed [RD] F3.1 | `mkt.brevo.sms_whatsapp.enabled` OFF |
| WhatsApp marketing | `MESSAGING_PORT` → `gupshup` (Meta marketing-category templates) | `marketing_whatsapp` | Opt-in per Meta WhatsApp Business policy; opt-out keyword honoured; template approval by Meta | ON (opt-in only) |
| Promotional voice calls | — | — | 140-series for promotional calls; AI/robo calls are A2P calls (TCCCPR (Third Amendment) Regulations 2026) | `mkt.voice.promotional.enabled` OFF; AI promotional calls tier L OFF |
| Push / in-app | Not used for marketing in case apps (App. O deny X-15) | — | Upgrade prompts only in settings and pricing pages (DP-10) | L |

Case notices, OTPs and service messages never use `MARKETING_PORT` (locked; [RD] DI-B 9). Event reminders to registered attendees are service messages tied to the registration and carry no promotional content; anything promotional in them needs the marketing purpose.

### Y.6.2 Consent model for marketing

1. Purposes are the six FR-P13-22 purposes, each **per company** (`company_scope`: Equator, Finbyx, Udofin, Institute where separate) and per channel; a grant for Equator never covers another company (NN-38).
2. Capture: itemised notice per DPDP Rules 2025 r.3 shown at the point of capture; unticked checkboxes (LINT-032); double opt-in for newsletters (`tenant.mkt.email.double_optin`, default ON, tier T).
3. Age: forms ask "Are you 18 or older?"; marketing consent is blocked if not (DPDP s.9; P13 §10).
4. Withdrawal: one click in every message; preference centre via signed link (FR-P13-22); propagation to every executor within 15 minutes (SLA monitored as metric `mkt.consent.propagation_latency`; breach alerts the DPO). An opt-out received by an executor (Brevo `unsubscribed`, SMS STOP, WhatsApp opt-out) arrives through the single Appendix X ingress (`/webhooks/brevo`: per-subscription bearer token + IP allow-list, because Brevo documents no HMAC signature [RD] F3.1); its state is re-fetched from the executor API before the consent ledger changes (Appendix AC §AC.11.2 control 4). If the re-fetch fails, the contact is placed at once on a send hold for every marketing channel (`mkt.suppressions` reason `pending_verification`) and the re-fetch is retried; the withdrawal is recorded when confirmed. No marketing message is sent meanwhile (fail-safe), and a forged call cannot rewrite the consent ledger.
5. Re-permission: no request for consent on the same channel within 90 days of an opt-out (`tenant.mkt.consent.reask_cooldown_days`, tier G, minimum 90).
6. Evidence: consent artefacts exportable per person (DPDP rights; [RB] Implications E.23).

### Y.6.3 Suppression and list hygiene

| List | Source | Effect | Removal |
|---|---|---|---|
| Respondent hashes | `equator.notices.respondent.served.v1` (HMAC with growth key, FR-P13-26(c)), held in `growth.suppression_hashes` (P13) | All marketing channels, audiences, ad uploads, CRM import | Only by separate marketing consent outside the case flow |
| Unsubscribed / withdrawn | Consent ledger | Channel and company scope | New consent after cooldown |
| Hard bounce | Executor events | Email suppressed immediately | Manual verification by the contact |
| Soft bounce | 3 consecutive (tier T) | Suppressed 30 days | Automatic |
| Spam complaint | Executor events | Permanent marketing suppression | Only by new double opt-in |
| DND / preference mismatch | DLT scrubbing result | SMS promotional | Per DLT preference |
| Minors / unknown age | Age check | All marketing | Age confirmation |
| Staff of competitors, regulators, journalists | Tag | Excluded from promotional sends unless they opted in to the newsletter | — |
| Legal hold / DSR erasure | DPO workflow | All | Per DSR outcome (erasure leaves a hash-only suppression row so the person is not re-added) |
| Inactive | No click or site visit in `tenant.mkt.email.sunset_days` (default 180) | One re-permission email, then suppressed | New consent |
| Pending verification | Executor opt-out awaiting re-fetch (§Y.6.2(4)) | All marketing channels | Re-fetch result: withdrawal recorded, or hold lifted if the executor shows no opt-out |

Bulk imports require a consent artefact per row (source, date, notice version, purpose); rows without it are rejected (`MKT_CONSENT_MISSING`); role addresses (`info@`, `admin@`) and disposable domains are flagged and excluded from promotional sends by default. Opens are not used as an engagement signal for sunsetting because mailbox privacy features make them unreliable; clicks, site visits and replies are used.

### Y.6.4 Sending domains and authentication

| Item | Default (tier) |
|---|---|
| Marketing subdomain | `news.equatorresolution.in` for marketing; transactional mail stays on the P07 SES domains so reputations are separate (T for name, L for separation) |
| SPF | Include only the active executor(s); ≤ 10 DNS lookups; `-all` on the marketing subdomain (G) |
| DKIM | 2048-bit keys per executor; rotation ≤ 12 months (G) |
| DMARC | Organisational domain `p=quarantine` minimum (P07 FR-P07-08); marketing subdomain aligned (`adkim=s; aspf=s`); progress to `p=reject` after 30 days of clean aggregate reports (G); `rua` to the DMARC reporting mailbox owned by `it_admin` |
| Unsubscribe headers | `List-Unsubscribe` (mailto and https) and `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058) on every marketing email (L) |
| Mailbox-provider thresholds | Spam-complaint alert at 0.1%, automatic pause at 0.3% per send and per rolling 7 days (G) **[VERIFY — open: current Gmail, Yahoo and Outlook bulk-sender requirements and thresholds]** |
| Verification gate | A send is blocked unless SPF, DKIM and DMARC alignment checks pass in the last 24 h (`MKT_SENDER_DOMAIN_UNVERIFIED`) (L) |

### Y.6.5 Frequency caps and quiet hours (per contact, across campaigns; group-wide caps add up across companies where consents overlap)

| Setting | Default | Tier and bounds |
|---|---|---|
| `tenant.mkt.freq.email_per_30d` | 4 (and not more than 1 per 48 h) | T; max 8 |
| `tenant.mkt.freq.whatsapp_per_30d` | 2 | T; max 4 |
| `tenant.mkt.freq.sms_per_30d` | 2 | T; max 4 |
| `group.mkt.freq.all_channels_per_30d` | 8 | G |
| `tenant.mkt.quiet_hours.sms_whatsapp` | Send only 10:00–19:00 recipient local time | G; never wider than 09:00–21:00 **[VERIFY — open: TCCCPR permitted window]** |
| `tenant.mkt.freq.individuals_per_30d` (SEG-IND/SEG-NRI) | 2 across all channels | G; max 4 |

Transactional and case messages are not counted and never suppressed by marketing caps. A send that would breach a cap skips the contact and records `MKT_FREQUENCY_CAP` in the send report.

### Y.6.6 Mass-send approval

A send to more than `tenant.mkt.send.mass_threshold` recipients (default 1,000; tier T, min 100) or any send to SEG-IND/SEG-NRI audiences needs: approved content (R2 floor), audience snapshot frozen with counts by suppression reason, test send to the seed list, and a second approver (`marketing_manager` if the maker is a staff member; `department_head` if the maker is the `marketing_manager`). The approval screen shows: audience size after suppression, segment, consent purposes used, caps skipped, claims used and expiry, sender-domain status and estimated cost.

### Y.6.7 Brevo as executor (NN-40)

**Dispatch reliability.** *(v3.1)* Every recipient in a send carries the idempotency key `(send_id, contact_hash, channel)`, so a retried batch never re-sends to a recipient the executor has accepted; a send whose batches partly fail ends `partially_completed` with a per-batch report, and "Retry failed batches" re-checks consent, suppression, caps and quiet hours before resending only the failed recipients; cancelling mid-dispatch stops the remaining batches and records the count already sent.

Static send lists (from `mkt.audience_snapshots`) and list memberships are pushed in batches using bulk import endpoints (contacts, companies and deals are pushed by the Appendix X `CRM_PORT.brevo`); the Brevo request budget defaults to 80 requests per hour for the whole account (`tenant.mkt.brevo.max_requests_per_hour`, Appendix AC §AC.17, shared with the Appendix X CRM sync through one token bucket; under the 100/h catch-all for non-Enterprise plans [RD] F3.1, DI-B 8); contacts endpoints use the 10 rps class; 429 → `RATE_LIMITED` with exponential back-off; Brevo-side segments are never used as send audiences (Equator snapshots are pushed as static lists); campaign statistics and webhook events (delivered, opened, click, bounces, spam, unsubscribed) come back to `mkt.metric_snapshots` and `mkt.touchpoints`. **Migration rehearsal** (exit test) each year: export lists, consent and suppression from Equator to a CSV bundle, import into the fallback (`ses_marketing`) in staging, send to seed list, compare counts.

---

## Y.7 Growth funnels and autopilot

### Y.7.1 Funnel technique register (MT; D3-28)

Class **A** allowed; **R** restricted (conditions enforced); **P** prohibited (tier L).

| ID | Technique | Class | Conditions / reason |
|---|---|---|---|
| MT-01 | Audience call-out headline | A (B2B); R (individuals) | No fear or shame framing to individuals (SL-19) |
| MT-02 | Single big promise | R | Claims Register-backed; no dispute-outcome promise (X-12 App. O) |
| MT-03 | Lead magnet (tool, checklist, template, guide) | A | "Free" means free (CCPA 2022); core tool results never email-gated (P13 §4E) |
| MT-04 | Explainer video (VSL-style) | R | Player controls, captions and transcript mandatory; no forced linear viewing |
| MT-05 | Video with locked controls | P | Interface interference; accessibility |
| MT-06 | Tripwire paid webinar or workshop | R | B2B education only; total incl. GST, refund terms, recording access, operator footer BP-04 |
| MT-07 | Countdown timer | R | Server-fixed end time bound to an event/offer record; same for every visitor; blocked on `case`, `neutral`, `grievance`, `posh`, `fees_case` and SEG-IND pages |
| MT-08 | Countdown that resets per visitor or session | P | False urgency (DP-01) |
| MT-09 | Scarcity ("12 seats left") | R | Bound to the live capacity of a cohort/event record; never on case-fee or neutral-related pages |
| MT-10 | Unbound scarcity or "only today" | P | False urgency |
| MT-11 | Strike-through / reference price | R | Stored prior price and date; lowest price in the prior 30 days as reported for the 2026 amendment **[VERIFY — open]**; never on case fees |
| MT-12 | Fictitious anchor price | P | CCPA reference-price risk ([RB] §1.4 C15) |
| MT-13 | Testimonials and logos | R | Claims Register `testimonial`/`client.logo` with consent, date, material-connection disclosure; no party outcome testimonials; no enterprise endorsement of neutrals (repeat-player risk) |
| MT-14 | Fabricated or AI-generated testimonials, synthetic "customers" | P | CCPA 2022; ML-07 |
| MT-15 | Result/saving claims ("saved 60%") | R | Only Claims Register aggregates with methodology; never settlement rates (NN-28) |
| MT-16 | Outcome guarantees or money-back on outcome | P | X-12 (App. O) |
| MT-17 | Service-level credit guarantee | R | Defined terms, Claims Register entry, finance approval |
| MT-18 | Offer stack / bundle | R | Each item priced or marked included; no basket sneaking (DP-02) |
| MT-19 | Multiple CTAs on one page | A | No nagging; no exit-intent or auto-open modals (LINT-034) |
| MT-20 | Retargeting | R | Consent; B2B pages only; never from FAM/POSH/health/case/payment pages (ML-10) |
| MT-21 | Webinar funnel | A | Recordings labelled with recording date; real attendee counts only |
| MT-22 | Evergreen webinar presented as live | P | Misleading |
| MT-23 | Drip sequences | A | Consent per channel; caps; opt-out every message |
| MT-24 | Pay-per-lead or referral fees to professionals; "top" badges | P | D3-27; [RB] X-17, X-18 |

### Y.7.2 Lead magnets (catalogue; each is an `mkt.lead_magnets` row with owner, claim keys, gate type and consent purposes)

| ID | Lead magnet | Segment | Gate | Notes |
|---|---|---|---|---|
| LM-01 | Dispute Explorer report | SEG-IND, SEG-MSM | None for the result; optional email/WhatsApp copy with separate marketing consent | NN-01: process and pathways only; free forum first (NN-20) |
| LM-02 | Clause builder (FR-P13-17) | SEG-LEN, SEG-MSM, SEG-EMP, SEG-INT | Download free; "adopt" needs organisation sign-up | Prohibited variants never offered |
| LM-03 | Fee calculator and comparator (FR-P13-16) | All | None | Fees and statutory periods only |
| LM-04 | Templates: self-help letters, model clauses EMC-2026.1 | SEG-IND, SEG-MSM | None | Neutral wording; "not legal advice" (BP-07) |
| LM-05 | Checklists: POSH checker, grievance SLA health check, GRM readiness | SEG-EMP, SEG-LEN, SEG-HEI | Result on page; report PDF by email optional | Browser-side CSV parsing (FR-P13-18) |
| LM-06 | Webinars and workshops | B2B segments, SEG-NEU, SEG-CHM | Registration (name, work email, organisation, segment) | §Y.7.4 |
| LM-07 | Explainer videos (process, mechanisms, how to respond) | All | None | MT-04 rules |
| LM-08 | Guides and reports (India ADR Report — free; practitioner guides — paid RS-24) | B2B, SEG-NEU | Optional email for long-form PDF; free version always available as web page | k ≥ 10 suppression in statistics |
| LM-09 | Limitation checker | SEG-IND, SEG-MSM | None | "Confirm with an advocate" notice |
| LM-10 | Private ADR Chambers 14-day trial | SEG-CHM, SEG-NEU | Sign-up | `ch.trial_14d`; no automatic conversion (DP-12) |

### Y.7.3 Landing-page builder blocks (P13 CMS content type `landing_page`; block rules enforced at save and publish)

| Block | Compliance properties |
|---|---|
| `Hero` | Headline from messaging house; lint B-rules; identity line slot mandatory on individual-facing pages |
| `PriceBlock` | Fee tokens or published plan only; total incl. GST for consumers (DP-08); strike-through only with stored prior price (MT-11) |
| `ComparisonTable` | Equator's own plans only; competitor columns blocked unless R3 approved (SL-12) |
| `TestimonialBlock`, `LogoWall`, `StatBand` | Claim nodes only (ML-03); expiry → fallback or removal |
| `VideoBlock` | Controls, captions, transcript mandatory (MT-04/05) |
| `CountdownBlock` | Server-fixed end time from an event/offer record; blocked on restricted page tags (MT-07/08) |
| `CapacityBlock` | Bound to cohort/event capacity (MT-09) |
| `FormBlock` | Minimal fields; itemised notice; separate unticked purpose checkboxes; age check; CAPTCHA (Turnstile) |
| `SignpostCard` | Mandatory on individual-facing pages where the vertical has a free forum (NN-20; LINT-021) |
| `DisclosureBlock` | Relationship or sponsorship disclosures (BP-05, BP-06, BP-08) |
| `GuaranteeBlock` | Service-level credits only (MT-17) |
| `EventBlock` | Date, time (IST), mode, "live" vs "recorded on {date}" label, real capacity |
| `PartnerBlock` | Co-brand approval ID required (§Y.5.5) |
| `OperatorFooter` | Mandatory on every landing page (BP-04) |

Page-level rules: no auto-open modal or exit-intent popup (LINT-034); no third-party ad scripts (DP-13); pixels only after consent and never on restricted tags (ML-10); every landing page links to a campaign code and carries its UTM mapping; a landing page cannot outlive its campaign by more than `tenant.mkt.landing.max_orphan_days` (default 30) without being redirected or unpublished.

### Y.7.4 Nurture sequences and webinar funnel

| Sequence | Entry trigger | Steps (default) | Exit | Approvals |
|---|---|---|---|---|
| NS-LEN Lender programme | B2B lead SEG-LEN, no meeting | 8 touches / 30 days (FR-P13-22): regulatory explainer, independence pack explainer, GRM clocks, webinar invite, clause kit, case-study (claim), demo offer, final check-in | Meeting booked; opportunity created; unsubscribe; 30 days | Marketing + legal per version |
| NS-INS / NS-EMP / NS-HEI / NS-LST | Segment lead | 6 touches / 30 days, segment content | Same | Same |
| NS-MSM MSMEs | Lead with marketing consent | 5 touches / 21 days: fee calculator, clause kit, Business Assure, Explorer, contact | Same | Same |
| NS-IND Individuals | Only after an explicit request for follow-up and marketing consent | 3 educational touches / 14 days maximum (reduced from FR-P13-22's 5/10 for Track A calm-voice rules); free forum named in each; no urgency; no price promotion | Any reply; unsubscribe; case filed (stop marketing to filers on that matter) | R3 |
| NS-NEU Neutral applicants | Applicant or interested neutral | 5 touches / 30 days: grading policy, EQAP, training options (≥ 3 providers), Chambers trial, Code of Conduct | Application submitted; unsubscribe | Marketing + legal |
| NS-ADV Advocates (Counsel workspace) | Advocate who signed up or asked | 3 touches / 21 days, product only | Same | Legal (r.36) |
| NS-TRN Trainees | Student/early career with consent | 3 touches / 30 days | Same | Marketing |
| NS-REE Re-engagement | 60 days inactive (lead) | Max 2 messages ([RB] AU-20) | Engagement or sunset | Marketing |

**Touches and caps.** *(v3.1)* A sequence "touch" is either a message or an owner task created in the Appendix X CRM (call, LinkedIn message by the owner, meeting offer). Sequence emails, SMS and WhatsApp count toward the §Y.6.5 caps; by default NS-LEN delivers 4 emails within the 4-per-30-days email cap and 4 owner tasks, and the 6-touch sequences 4 emails and 2 tasks. A message step that would breach a cap is deferred to the next permitted day inside the sequence window, otherwise skipped and logged with `MKT_FREQUENCY_CAP`; caps are never raised for a sequence alone.

**Webinar funnel** (MT-21): registration (minimal fields; marketing purpose separate) → confirmation with calendar file → reminders T-24 h and T-1 h (service messages) → live session on the meeting tool through the workspace connector (Microsoft Teams per D3-04; licence features on Business Basic **[VERIFY — open: webinar registration and recording features on the confirmed SKU]**) → recording published labelled "Recorded on {date}" (BP-09) → replay email → feedback survey → B2B offer (no offers to individuals) → close. Q&A moderation: questions about individual matters are not answered (template BP-09); speakers file a disclosure of material connections; CPD or credit statements only with an accreditation claim.

### Y.7.5 Referral and partner programmes (D3-27; X-54)

| Programme | Who | Reward | Controls |
|---|---|---|---|
| RP-01 Non-professional partner/reseller (RS-28) | HRMS/payroll/LOS vendors, chambers of commerce and industry associations, technology resellers | Revenue share on first-year subscription per written agreement | KYB; GST invoice; TDS under Income-tax Act 2025 s.393(1) Table Sl. 1(ii) (formerly s.194H; 2%, ₹20,000) as in FR-P13-20; disclosure on referred tenant and to counterparties (NN-16); `finance_ops` approves the reward; payout executed by P05 through `PAYOUT_PORT` with `accounts_maker`/`accounts_checker` (Appendix X OA-20; NN-36) |
| RP-02 B2B customer referral | Existing business customers (not professional firms of the four classes) | Service credit on the referring account, published terms | Disclosed; no reward linked to any case or neutral |
| RP-03 Relationship partners (professionals) | Advocates, law firms, CAs, CSs, CMAs and their firms; bar associations | **None** (`reward_eligible = false`, tier L) | Co-hosted education and content only; Equator never sends them leads or work (r.36, r.37) |
| RP-04 Individuals | Parties and the public | **None** (programme type disabled, tier G OFF) | A referral reward to people in disputes looks like soliciting litigants and invites misuse |
| RP-05 Group cross-sell | Group company account managers | None (internal) | MA-26 OFF until group consent design approved (NN-38) |

The payout engine checks `professional_class` on the payee and the partner record at code creation, at attribution and at payout; any professional flag blocks the reward (`MKT_ADVOCATE_REWARD_BLOCKED`, applies to all four classes).

### Y.7.6 Events

`mkt.events`: type (webinar, roundtable, conference, workshop, training promotion, moot or student competition, partner event), mode, venue, capacity, ticketing (revenue stream RS-23 via the registry; prices incl. GST), sponsors (sponsorship register; repeat-player sponsorship of neutral CPD, empanelment or assessment prohibited — App. O X-10), speakers (disclosures), photography notice, accessibility (ISL interpreter on request, captions), data retention for attendees (`tenant.mkt.events.attendee_retention_days`, default 365). Student events with minors are not marketing-enabled (no marketing consent captured).

### Y.7.7 Training cross-sell to equatoradr.com

Gated by `academy.institute_referral` (OFF; approver `legal_reviewer` + Company Secretary) until corrections C1–C20 (Appendix AF §AF.4.3, which renumbers Appendix T's C11/C12 as C19/C20) are closed and evidenced, and the Institute's legal entity, CIN, GSTIN, INR prices incl. GST, refund policy and grievance officer are displayed ([RB] D.13–D.14). When ON: every promotion shows at least three recognised providers in seeded-random order (P-D08); BP-05 disclosure; no copy implying training leads to empanelment, grade or appointments (E-14; NN-28); promotions never go to parties in a case or to respondents; learner data never flows from the Institute into Equator case systems; contacts are shared with the Institute only under a consent purpose naming it (NN-38); referral fees (RS-22) stay OFF until a Companies Act 2013 s.188 related-party approval and the s.184 disclosures are recorded.

### Y.7.8 Marketing automation catalogue (built on the Appendix X engine)

Every automation is a versioned Appendix X workflow with the attributes below; `stop` names the kill switch (all marketing automations also stop on `tenant.mkt.automation.global_pause`, on Appendix X's `tenant.ops.automation.global_pause` and on a C1/C2 crisis). Per-automation switches are `tenant.mkt.automation.<id>.enabled`.

| ID | Automation | Trigger | Action | Data used | Permissions (runs as / approves) | Exception handling | Audit | Stop | Owner | Default |
|---|---|---|---|---|---|---|---|---|---|---|
| MA-01 | Consent sync | Consent event | Push withdrawals to marketing executors not covered by the Appendix X connector (MSG91, Gupshup, `ses_marketing` suppression); Brevo's blocklist is updated once by `CRM_PORT.brevo.applyOptOut` (Appendix X §X.4.7) | Consent ledger via `ops.crm_marketing_view` | System / DPO owns purposes | Retry; withdrawal fail-safe | Hash-chained | Never stops for withdrawal | DPO | ON (L) |
| MA-02 | Respondent suppression | `respondent.served` | Add hash to suppressions; purge from audiences | HMAC only | System | Alert on executor failure | Yes | Never (L) | DPO | ON (L) |
| MA-03 | Lead hand-off from marketing captures | `mkt` capture with consent (event or webinar registration, E1 engagement, referral code); website forms use Appendix X OA-01 | Create/merge CRM lead via `POST /v1/ops/crm/leads` (Appendix X dedupe D1–D6) with UTM and campaign code | Capture fields | System | Dedupe queue | Yes | `tenant.mkt.automation.ma03.enabled` | `marketing_manager` | ON |
| MA-04 | Nurture enrolment | Lead in segment, no meeting | Enrol in sequence version | Segment, consent | System / sequence approved by marketing + legal | Skip if cap/suppressed | Yes | Sequence kill switch | `marketing_manager` | ON |
| MA-05 | Sequence exit | Meeting, opportunity, reply, unsubscribe, case filed | Remove from sequence | CRM events | System | — | Yes | — | `marketing_manager` | ON |
| MA-06 | Webinar reminders | Registration | T-24 h, T-1 h service reminders; replay | Registration | System | Provider fallback | Yes | Event switch | Event owner | ON |
| MA-07 | Content expiry hold | Claim expired / flag OFF / rights expired | Hold scheduled items; notify | Claim, flag, rights | System | — | Yes | — | Content owner | ON (L) |
| MA-08 | Evidence chase | No evidence T+24 h | Task + reminder; escalate T+48 h | Publication record | System | — | Yes | — | `marketing_manager` | ON |
| MA-09 | Social schedule (API) | Item scheduled, adapter ON | Publish via `SOCIAL_PORT` | Approved version | System / item approved | Fail → manual hand-off task | Payload hash | Adapter flag | `social_media_executive` | OFF |
| MA-10 | Engagement triage | New engagement item | Classify (AI), route E1–E10 | Comment/DM text | System / human confirms | Unknown → human queue | Yes | `tenant.mkt.automation.ma10.enabled` | `social_media_executive` | ON |
| MA-11 | Auto-acknowledge | E1/E2/E9 confirmed | Send acknowledgement template | Handle | System | — | Yes | `tenant.mkt.engagement.auto_ack_enabled` | `social_media_executive` | OFF |
| MA-12 | Budget guard | Spend ≥ 90% / 100% | Alert / pause paid channels | Spend | System | — | Yes | — | Budget owner | ON |
| MA-13 | Deliverability guard | Complaint rate ≥ threshold | Pause sends; alert | Executor events | System | — | Yes | — | `marketing_manager` | ON (L) |
| MA-14 | Sunset and re-permission | Inactive ≥ sunset days | One re-permission email; suppress | Engagement | System / template approved | — | Yes | Switch | `marketing_manager` | ON |
| MA-15 | Regulatory-deadline campaign | Calendar date (e.g., POSH annual report) | Draft campaign tasks (not sends) | Legal Rules Register dates | System / legal approves content | — | Yes | Switch | `marketing_manager` | ON |
| MA-16 | Event follow-up | Event closed | Survey; B2B offer email | Attendance | System / templates approved | — | Yes | Switch | Event owner | ON |
| MA-17 | Referral attribution | Referral code used | Attribute; create pending reward | Code, CRM | System / `finance_ops` approves reward; P05 pays (Appendix X OA-20) | Professional flag → block | Yes | Programme switch | `partnerships_manager` | ON (RP-01/02) |
| MA-18 | Partner obligation reminders | MoU obligation due T-30/T-7 | Tasks | MoU | System | Overdue → escalate | Yes | — | `partnerships_manager` | ON |
| MA-19 | Co-brand / rights expiry | Expiry T-30/T-7 | Hold items; tasks | Approvals, rights | System | — | Yes | — | `marketing_manager` | ON (L) |
| MA-20 | Coverage logging | Media monitoring hit (manual or feed) | Create coverage item for review | Public articles | System / PR reviews | — | Yes | Switch | `pr_manager` | ON |
| MA-21 | Crisis pause | Crisis C1/C2 opened | Pause all scheduled posts and sends | Crisis record | System | — | Yes | Crisis lead resumes | `ops_director` | ON (L) |
| MA-22 | Attribution run | Nightly | Compute touches and results | Consented touchpoints | System / model approved | — | Yes | — | `marketing_manager` | ON |
| MA-23 | Dashboard snapshot | Monthly | Freeze metrics; feed Appendix Z contribution | Aggregates | System / `marketing_manager` approves | — | Yes | — | `marketing_manager` | ON |
| MA-24 | Landing-page orphan check | Daily | Flag pages past campaign end | CMS, campaigns | System | — | Yes | — | `marketing_manager` | ON |
| MA-25 | AI visibility backlog | Monthly panel (FR-P13-V2-17) | Create content tasks | Panel results | System | — | Yes | Switch | SEO lead | ON |
| MA-26 | Group cross-sell suggestion | B2B account in another group company | Suggest to account manager | Consented B2B data | System / account manager decides | — | Yes | `group.ops.cross_sell.enabled` (Appendix X) | `group_admin` | OFF |
| MA-27 | Win-back | Cancelled > 60 days | One offer within approved band ([RB] AU-20) | Subscription | System / bands approved by finance | — | Yes | Switch | `customer_success_manager` | ON |
| MA-28 | B2B review/case-study request | Renewal or milestone | Request email | Account | System / legal approves publication | Never to parties about outcomes | Yes | Switch | `marketing_manager` | ON |
| MA-29 | Paid-media sync | Daily | Pull spend and results | Ad platform | System | — | Yes | Adapter flag | `marketing_manager` | OFF |
| MA-30 | Expansion signal to CSM — **retired**: provided once by Appendix X OA-11 (no duplicate automation) | — | — | — | — | — | — | — | — | — |
| MA-31 | DSR propagation | Erasure/correction request | Apply to `mkt` and executors | DSR | System / DPO | Failure → DPO task | Yes | Never (L) | DPO | ON (L) |
| MA-32 | Brevo migration rehearsal | Annual | Export and test import to fallback | Lists, consent | System / `it_admin` | Report | Yes | — | `it_admin` | ON |

No automation may publish public content, change a price, publish a testimonial, change targeting or send a mass campaign without the approvals in §Y.7.9 (ML-13); the Appendix X engine refuses to activate a workflow whose action set includes such a step without an approval node (`OPS_AUTOMATION_APPROVAL_REQUIRED`, Appendix X §X.12.6 and EOP-L07; the engine's code applies to marketing automations).

**Marketing automation templates (safe defaults).** *(v3.1)* New marketing automations start from the Appendix X template library (§X.12.7) and these templates. Each starts as a draft, runs in shadow mode first, sends nothing externally until its §Y.7.9 approval nodes are satisfied, checks consent, suppression, caps and quiet hours at every step, and stops on unsubscribe and on case filing by the contact; locked steps cannot be removed (`OPS_AUTOMATION_APPROVAL_REQUIRED`).

| ID | Template | Safe defaults pre-set |
|---|---|---|
| TPL-MKT-01 | Webinar promotion and reminders | consented B2B audiences only; reminders as service messages; replay labelled "Recorded on {date}" |
| TPL-MKT-02 | B2B nurture sequence | touches and window from the segment's NS-* row; messages within caps (touches-and-caps rule, §Y.7.4); exit on meeting, opportunity or reply; R2 review per step |
| TPL-MKT-03 | Newsletter cadence | double opt-in; sunset rule; 1 issue per 30 days |
| TPL-MKT-04 | Event follow-up | survey first; B2B offer only; nothing to individuals |
| TPL-MKT-05 | Content expiry watch | hold on claim or rights expiry; owner task |
| TPL-MKT-06 | Capture-to-CRM hand-off | MA-03 pattern; dedupe; UTM and campaign code required |
| TPL-MKT-07 | Re-engagement | ≤ 2 messages, then suppress |
| TPL-MKT-08 | Social engagement triage | classify → human confirms → route; auto-acknowledgement OFF |

### Y.7.9 Human approval matrix

| Action | Maker | Approver(s) (≠ maker) | Evidence |
|---|---|---|---|
| Public claim (new or renewed) | Claims owner | `legal_reviewer` for legal_effect/regulatory_status; approver ≠ owner (FR-P13-10) | Evidence object |
| Pricing claim or price promotion | `marketing_manager` | `finance_ops` + `legal_reviewer` | Published fee schedule/plan; promo ledger |
| Testimonial, logo, case study | `marketing_manager` | Claims owner + `legal_reviewer` | Written consent, material-connection disclosure |
| Sensitive or individual-facing targeting | `marketing_manager` | `compliance_officer` + DPO | Targeting record (§Y.7.10) |
| Mass send | Maker | §Y.6.6 second approver | Audience snapshot |
| Paid media budget | Campaign owner | Authority matrix (§Y.3.3) | Budget record |
| MoU, co-branding, government announcement | `partnerships_manager` | `legal_reviewer` + authorised signatory (`ctl`) | Signed instrument |
| Crisis statement | `pr_manager` | `legal_reviewer` + crisis lead (`ops_director`) | Statement record |
| Automation version with outbound action | `marketing_manager` | `department_head` or `compliance_officer` | Workflow version |

### Y.7.10 Targeting rules

Prohibited targeting attributes (tier L): case, grievance, POSH, HR or payroll data; health; religion, caste, sexual orientation, political opinion; financial distress signals (for example, "people with loan defaults" or "recently denied claims"); minors; respondents; visitors of FAM/POSH/health/case pages; customer-list lookalikes. Allowed: B2B firmographics and job functions; geography and language; professional interests for SEG-NEU/SEG-ADV (Equator advertising its own software, not their services); contextual search keywords for individual-facing ads, provided the ad (a) does not imply Equator is the public forum searched for (GX-4, LINT-003), (b) lands on a page with the SignpostCard, and (c) is R3-approved. Bidding on competitors' brand names is OFF by default (`tenant.mkt.ads.competitor_brand_bidding`, tier G).

---

## Y.8 PR and communications

### Y.8.1 Media list

`mkt.media_contacts`: outlet, beat, professional email/phone, source of the contact data, basis (`consent` or `self_published_professional_contact`), opt-out status, last contacted. Professional contact details that a journalist has published for press enquiries may be stored with the source URL and date (DPDP s.3(c)(ii) — data made publicly available by the data principal — **[VERIFY — open (counsel): reliance on s.3(c)(ii) for media lists ([RE] F4.2 limits)]**); any other contact needs consent; purchased media databases are not imported unless the vendor warrants a lawful basis and counsel approves; every pitch includes an opt-out; opt-outs are honoured across the group.

### Y.8.2 Press releases and statements

Workflow: `draft → fact_check (claims resolved) → legal_review → company_secretary (for corporate, group, Board, funding, listed-company or regulator topics) → approved (CEO or delegate) → embargoed → distributed → archived`. Rules: every number is a claim node; no statement about any case or party (ML-11); published outcomes referenced only through the `/decisions` Library with consent (NN-26); partner names only with a signed instrument permitting publicity; embargo times enforced (distribution job waits; `MKT_EMBARGO_ACTIVE`); BP-01 boilerplate mandatory; Hindi version through the translation workflow. Neutrals and staff speak to media only as registered spokespersons (`mkt.spokespersons`: topics, languages, media training date, approval scope); neutrals never comment on their matters.

### Y.8.3 Coverage log

`mkt.coverage_items`: outlet, URL, date, type (earned, owned, paid, sponsored), sentiment (reviewed), accuracy check, correction requested, claim keys mentioned, reach estimate (source labelled). Paid or sponsored coverage is labelled and never reported as earned. Inaccurate coverage triggers a correction request with the approved fact sheet.

### Y.8.4 Crisis communication playbook

| Level | Examples | Lead | First holding statement | Social/sends |
|---|---|---|---|---|
| C1 Critical | Personal data breach; impersonation or phishing campaign using Equator's name; serious allegation against the institution's independence; platform outage during hearings | `ops_director` (crisis lead) with `pr_manager`, `legal_reviewer`, DPO, security lead, Company Secretary | Within 2 hours of opening (`tenant.mkt.crisis.c1_holding_hours`, tier G) | All scheduled posts and sends paused (MA-21) |
| C2 High | Allegation against a named neutral; misleading Equator claim found live; viral complaint; regulator or government notice | `pr_manager` + `legal_reviewer` | Within 4 hours | Paused |
| C3 Medium | Negative press with factual errors; partner dispute | `pr_manager` | Within 1 business day | Review queue |
| C4 Low | Isolated complaints, trolling | `social_media_executive` | Per E-category SLA | Normal |

Rules: statutory tracks run first and are not replaced by PR — a personal data breach follows the DPDP breach workflow and CERT-In reporting owned by the DPO and security (Appendix Q), and public statements say only what those owners clear; statements come from the approved statement bank and are approved per §Y.7.9; no admission of liability without legal sign-off; no comment on individual cases (ML-11); impersonation: pinned notice on `/verify` and social profiles listing official numbers and domains, takedown requests to platforms, report on the National Cyber Crime Reporting Portal (cybercrime.gov.in); a dark-site page template (`/notice/{slug}`) can be published by the crisis lead with legal approval; post-incident review within 10 business days with actions tracked. A tabletop exercise is run twice a year (P14 addendum).

**Resuming after a C1/C2 pause.** *(v3.1)* The crisis lead reviews the held list grouped by campaign and releases, reschedules or cancels each item; bulk release is allowed only for R0/R1 items that do not match the crisis keyword set recorded on the incident; R2 and R3 items return to compliance review; sends paused mid-dispatch resume only through "Retry failed batches" after the same checks.

---

## Y.9 Partnerships and collaborations

### Y.9.1 Partner types and rules

| Type | Typical collaboration | Rules |
|---|---|---|
| Universities and law schools | Moots, clinics, internships, research, guest lectures, student memberships | No student data as a marketing source; minors excluded; no implication that participation leads to empanelment |
| Bar associations | Education (CLE/CPD) on ODR practice, Counsel workspace demos | No referral arrangements or rewards (D3-27); Equator does not promote members' services |
| Chambers of commerce and industry bodies | MSME outreach, co-hosted events, member pricing | Member pricing through the promotion ledger (Appendix O) with published terms; revenue share only under RP-01 with disclosure |
| Government programmes and public bodies | Awareness, MSME, digital-justice initiatives | Written instrument; no "approved/recognised" claims without `regulatory_status` claim; emblem rules (§Y.5.5); procurement rules handled by legal |
| International ADR bodies | MoUs on training, cross-referral of knowledge | Claims only after signed MoU and within its publicity clause (avoid E-03-type overstatement) |
| Technology partners | LOS/HRMS integrations, marketplaces | Finbyx/Udofin as group companies follow NN-38; data-sharing clauses reviewed by DPO |
| Legal aid and NGOs | Pro bono mediation days, awareness | No marketing use of beneficiaries' data |

Mandatory MoU clauses (template library, legal-owned): no role for the partner in selecting, grading or allocating neutrals (NN-03, NN-16, NN-28); no case data exchange; publicity and logo-use clause with approval steps; data protection clause (DPDP processor/fiduciary roles); non-exclusivity; anti-bribery (gifts and hospitality register, NN-36 spirit); termination and run-off; no fee-sharing with advocates (BCI Ch. III r.2).

### Y.9.2 Pipeline and obligations

Stages are the Appendix X `partnership` pipeline (`ops.crm_stages`: identified → researched → contacted → exploring → proposal → term sheet → legal review → approval (authority matrix) → MoU signed → active; Appendix X §X.4.2), and the partner organisation is the CRM record `ops.crm_partners`. `mkt.partnerships` holds the collaboration record (CRM partner and opportunity IDs by value), and `mkt.mous` carries the post-signature lifecycle `active → renewal_due → renewed | expired | terminated`. `mkt.mou_obligations`: obligation text, owner (Equator or partner), due date, recurrence, evidence required, status; MA-18 reminders; overdue obligations reported monthly. Joint events link to `mkt.events`; joint content needs co-brand approval. Partnerships are company-scoped; a group-wide partnership is recorded once with participating companies and a data-sharing annex.

---

## Y.10 SEO, GEO and AI-discovery planning

`mkt-seo` is the planning layer over App. P §6 and P13 execution: `mkt.seo_intent_clusters` (seeded from App. P §6.13; vertical, locale, intent, priority, owner), `mkt.seo_briefs` (cluster, answer-first block draft, citations required, internal links, author and legal reviewer, target URL, refresh date), `mkt.programmatic_governance` (template ID, owner, legal reviewer, last 5% sample audit, error count, kill-switch state `seo.programmatic.<template>.enabled`, App. P §6.7), `mkt.ai_visibility_backlog` (from FR-P13-V2-17 runs: prompt, engine, cited yes/no, accuracy, free-forum mention, fix task). Rules: no link buying, private blog networks or undisclosed guest posts; sponsored or guest content labelled; no AI-generated pages published without human authorship and legal review (App. P §6.7); an inaccurate AI answer leads to a clearer answer-first block or citation on Equator's page, never to a new claim (App. P §6.14); monthly SEO report shows indexation, clicks, programmatic page health and AI-visibility trend from the growth database only (NN-16).

---

## Y.11 Analytics and attribution (D3-29)

### Y.11.1 Definitions

| Term | Definition (default; windows tier T) |
|---|---|
| Touchpoint | A consented, recorded interaction attributable to a channel: web session with UTM (consented analytics), email click, social click, event attendance, webinar registration, partner referral, sales activity logged in CRM |
| Sourced | The opportunity's originating lead has a marketing touch as its first touch within 180 days before lead creation |
| Influenced | Any contact of the account had a marketing touch within 90 days before opportunity creation and before close |
| Converted | Stage progression lead → MQL → SQL → opportunity → won (Appendix X stage definitions); conversion credit is assigned by the active model |
| Individuals' conversions | Only when the filer is the lead and holds analytics consent (FR-P13-23); respondents never |

### Y.11.2 Attribution model registry

`mkt.attribution_models`: version, type (`first_touch`, `last_non_direct`, `position_based`, `linear`, `time_decay`), parameters (position-based 40/20/40; time-decay half-life 7 days), lookback windows, channel taxonomy version, approval (`marketing_manager` + `finance_ops`), effective_from. Default reporting model: position-based; dashboards always show first-touch and last-non-direct beside it. A new model version applies from its effective date; history is re-run only into a labelled comparison report, never overwriting published monthly snapshots (`MKT_ATTRIBUTION_MODEL_UNAPPROVED` if an unapproved version is selected for a published report).

### Y.11.3 Economics

| Metric | Formula (per segment, per period) |
|---|---|
| CAC (fully loaded) | (paid media + production + tools + events + agencies + sponsorships + allocated marketing and sales staff cost from HR cost-centre totals) ÷ new customers won |
| LTV (recurring streams) | ARPA × gross margin % ÷ monthly logo churn (capped at 60 months) |
| LTV (transactional/individual) | 12-month contribution margin per customer |
| LTV:CAC; payback | LTV ÷ CAC; CAC ÷ (monthly ARPA × gross margin %) |
| Campaign ROI | (attributed gross margin − campaign spend) ÷ campaign spend |
| Budget variance | Actual spend − approved budget, by line |

Staff cost enters only as cost-centre totals (no individual salary visible to marketing; Appendix Z/`pay` boundary). GST: spend recorded net of eligible input tax credit as determined by finance.

### Y.11.4 Dashboards (Operations Platform; shareable across group companies only under NN-38 grants)

D-01 Marketing overview (OKRs, pipeline sourced/influenced, spend vs budget) · D-02 Channel performance · D-03 Content calendar health (on-time, held, evidence overdue, review cycle time) · D-04 Email and messaging (deliverability, complaint rate, unsubscribes, consent growth by purpose and company) · D-05 Social (reach, engagement rate, response SLA by E-category) · D-06 Funnel (lead magnet → lead → MQL → SQL → won, by segment) · D-07 Events and webinars (registrations, show-up, follow-up conversion) · D-08 Partnerships (pipeline, obligations, partner-sourced ARR) · D-09 PR (coverage, accuracy corrections, crisis log) · D-10 Economics (CAC, LTV, payback by segment) · D-11 Compliance (lint overrides, held items, takedowns, SL-01/SL-13 hits, suppression effectiveness tests) · D-12 SEO/GEO (indexation, programmatic health, AI visibility). Individual-level statistics for SEG-IND are shown only at k ≥ 10 per cell.

### Y.11.5 Metric dictionary

`mkt.metric_definitions`: key, name, formula, source, grain, owner, privacy class, version. Only dictionary metrics can be OKR targets, dashboard tiles or appraisal inputs.

### Y.11.6 Data rules

No case events except FR-P13-23 allow-listed aggregates; no POSH or sealed data; analytics scripts only after consent and never on `/app`, `/verify`, case or payment pages; offline conversion exports to ad platforms only for consented filers, never respondents (FR-P13-23); retention of touchpoints 25 months (`tenant.mkt.touchpoints.retention_months`, tier G, max 36).

### Y.11.7 Contribution metrics for marketing roles (feed to Appendix Z; NN-35)

| Role | Outcome and quality metrics (examples) | Context only (capped weight ≤ 15%) |
|---|---|---|
| `marketing_manager` | OKR attainment; budget variance within ±10%; compliance incidents (negative); campaign close-out completeness | Pipeline sourced |
| `content_writer` | On-time delivery vs calendar; first-pass approval rate; lint B-hits per item; corrections attributable (negative); peer-review quality rubric | Organic performance of owned pieces |
| `designer` | Turnaround vs SLA; brand-review pass rate; accessibility pass (alt text, contrast, captions) | — |
| `social_media_executive` | Calendar adherence; evidence completeness within 24 h; E-category response SLA; correct routing rate | Engagement rate |
| `pr_manager` | Coverage accuracy; correction turnaround; embargo breaches (target 0); crisis statement timeliness | Share of voice |
| `partnerships_manager` | MoU obligations on time; legal-review cycle completeness; partner-sourced pipeline | Number of MoUs |

Prohibited inputs (tier L): login or online hours, keystrokes, screen activity, raw post counts or follower counts as primary measures, any measure derived from case outcomes or neutral allocation, leads obtained by a prohibited technique. Metrics are visible to the employee on SCR-P17-26 with their sources and can be disputed through Appendix Z; team outcomes are credited to the team unless an item has a named owner.


### Y.11.8 Weekly review feed *(v3.1)*

Every Monday the analytics module publishes the marketing section of the Appendix X weekly management review pack (OA-21, §X.19.1) and the same view as SCR-P17-01 "This week": approvals ageing and review-SLA breaches by tier; held items with reasons; evidence overdue; open calendar conflicts (CC-01–CC-10) for the next 14 days; completed sends with suppression counts and complaint rate; consent-propagation incidents; budget lines ≥ 90 %; crisis log. Figures are frozen snapshots (D3-25); individual-level cells need k ≥ 10.
---

## Y.12 Settings catalogue (NN-33)

Scope prefix: `platform` (L), `group`, `tenant` (company), `user`. "Who" = role allowed to change; "Approval" = second approver for G-tier changes (maker ≠ checker, version history, rollback).

| Key | Tier | Default | Bounds / guardrail | Who / approval |
|---|---|---|---|---|
| `platform.mkt.locked_rules` (ML-01–ML-14) | L | ON | Not editable | — |
| `platform.mkt.funnel.prohibited_techniques` (MT class P) | L | Register §Y.7.1 | Additions only, by ADR | — |
| `platform.mkt.rewards.professional_classes_blocked` | L | advocate, ca, cs, cma | Not editable | — |
| `platform.mkt.targeting.prohibited_attributes` | L | §Y.7.10 | Additions only | — |
| `tenant.mkt.review.tier_rules` | G | §Y.4.3 | Cannot lower floors | `marketing_manager` / `legal_reviewer` |
| `tenant.mkt.review.sampling_pct.r0`, `.r1` | T | 5, 10 | ≥ 5 | `marketing_manager` |
| `tenant.mkt.social.lint_profile` (SL rules severities) | G | §Y.4.5 | † rules fixed | `legal_reviewer` / `compliance_officer` |
| `tenant.mkt.link.allowed_domains` | T | Equator domains | No case routes | `marketing_manager` |
| `tenant.mkt.social.max_hashtags.<platform>` | T | LI 5, IG 10, X 3, FB 5 | — | `social_media_executive` |
| `mkt.social.linkedin_cm.enabled`, `.meta_graph.enabled`, `.x_v2.enabled`, `.youtube_data.enabled` (flags; Appendix AC §AC.17) | G | OFF | Access grant document and `it_admin` token-storage review required | `marketing_manager` / `legal_reviewer` |
| `tenant.mkt.social.ig_daily_cap` | T | 50 | ≤ 100 | `social_media_executive` |
| `tenant.mkt.social.x_monthly_budget_usd` | T | 50 | Budget line required | `marketing_manager` |
| `mkt.adobe_embed.enabled` | G | OFF | Adobe review evidence | `marketing_manager` / `it_admin` |
| `tenant.mkt.evidence.deadline_hours` | T | 24 | ≤ 72 | `marketing_manager` |
| `tenant.mkt.evidence.sample_pct` | T | 10 | ≥ 5 | `compliance_officer` |
| `tenant.mkt.engagement.auto_ack_enabled` | T | OFF | E1/E2/E9 only | `marketing_manager` |
| `tenant.mkt.engagement.sla.<category>` | T | §Y.4.9 | E3 ack ≤ 48 h (G floor) | `marketing_manager` |
| `tenant.mkt.engagement.retention_days` | G | 90 | ≤ 180 | DPO |
| `tenant.mkt.asset.rights_buffer_days` | T | 14 | ≥ 7 | `marketing_manager` |
| `tenant.mkt.asset.consent_takedown_hours` | G | 72 | ≤ 168 | DPO |
| `tenant.mkt.email.double_optin` | T | ON | — | `marketing_manager` |
| `tenant.mkt.email.sunset_days` | T | 180 | 90–365 | `marketing_manager` |
| `tenant.mkt.consent.reask_cooldown_days` | G | 90 | ≥ 90 | DPO |
| `tenant.mkt.freq.*` and `group.mkt.freq.all_channels_per_30d` | T/G | §Y.6.5 | Bounds in §Y.6.5 | `marketing_manager`; group: `group_admin` |
| `tenant.mkt.quiet_hours.sms_whatsapp` | G | 10:00–19:00 | Within 09:00–21:00 | `compliance_officer` |
| `tenant.mkt.send.mass_threshold` | T | 1,000 | ≥ 100 | `marketing_manager` |
| `tenant.mkt.deliverability.complaint_pause_pct` | G | 0.3 | ≤ 0.3 | `marketing_manager` / `it_admin` |
| `tenant.mkt.sender.marketing_subdomain` | T | `news.equatorresolution.in` | Separate from transactional | `it_admin` |
| `tenant.mkt.dmarc.target_policy` | G | reject after 30 clean days | ≥ quarantine | `it_admin` |
| `mkt.brevo.enabled` | G | OFF until DPA + transfer register | Fallback configured | `marketing_manager` / DPO |
| `mkt.brevo.sms_whatsapp.enabled` | G | OFF | DLT support confirmed in writing | `marketing_manager` / `compliance_officer` |
| `tenant.mkt.brevo.max_requests_per_hour` | T | 80 | ≤ 95 % of plan limit; one budget shared by `CRM_PORT` and `MARKETING_PORT` (Appendix AC §AC.17) | `marketing_manager` |
| `mkt.voice.promotional.enabled` | G | OFF | AI promotional calls locked OFF | `compliance_officer` / counsel |
| `tenant.mkt.budget.approval_limits` | G | §Y.3.3 | Via `ctl` authority matrix | `finance_ops` / `ops_director` |
| `tenant.mkt.budget.pause_at_pct` | T | 100 | ≤ 110 | budget owner |
| `tenant.mkt.experiment.alpha`, `.power`, `.harm_stop_unsub_pct` | T | 0.05, 0.8, 1.0 | Prohibited surfaces fixed | `marketing_manager` |
| `tenant.mkt.landing.max_orphan_days` | T | 30 | ≤ 90 | `marketing_manager` |
| `tenant.mkt.ads.competitor_brand_bidding` | G | OFF | Legal approval | `legal_reviewer` |
| `tenant.mkt.referral.programmes_enabled` | G | RP-01, RP-02 ON; RP-04 OFF | RP-03 reward locked OFF | `partnerships_manager` / `finance_ops` |
| `group.ops.cross_sell.enabled` (Appendix X §X.13 key; listed for reference — no separate marketing key) | G | OFF | Group consent design + GDSA | `group_admin` / DPO |
| `academy.institute_referral` | G | OFF | Corrections closed | `legal_reviewer` / Company Secretary |
| `tenant.mkt.events.attendee_retention_days` | T | 365 | ≤ 730 | DPO |
| `tenant.mkt.crisis.c1_holding_hours`, `.c2_holding_hours` | G | 2, 4 | ≤ 4, ≤ 8 | `ops_director` |
| `tenant.mkt.automation.global_pause` | T | OFF | Marketing automations only; Appendix X `tenant.ops.automation.global_pause` stops all | Crisis lead, `marketing_manager` |
| `tenant.mkt.automation.<id>.enabled` | T | §Y.7.8 Default column | L-marked automations cannot be disabled | `marketing_manager` |
| `mkt.ai.image_generation.enabled` | G (flag) | OFF | §Y.4.4 and FR-P11-V3-Y05 rules | `marketing_manager` / `legal_reviewer` |
| `tenant.mkt.attribution.default_model` | G | position_based v1 | Approved versions only | `marketing_manager` / `finance_ops` |
| `tenant.mkt.attribution.lookback_days` | T | sourced 180, influenced 90 | 30–365 | `marketing_manager` |
| `tenant.mkt.touchpoints.retention_months` | G | 25 | ≤ 36 | DPO |
| `tenant.mkt.contribution.context_weight_cap_pct` | G | 15 | ≤ 25 | `hr_manager` / `department_head` |
| `user.mkt.notifications.*` | T | Role defaults | — | user |
| `tenant.mkt.review.sla_hours.<stage>.<tier>`, `tenant.mkt.review.buffer_hours` | T | §Y.4.2; buffer 8 | crisis statement 1 h is G | `marketing_manager` *(v3.1)* |
| `tenant.mkt.calendar.overlap_pct`, `.min_gap_minutes` | T | 10; 120 | 0–50; ≥ 30 | `marketing_manager` *(v3.1)* |
| `tenant.mkt.calendar.blackouts` | T | none | entries added by the Company Secretary are locked for marketing | `marketing_manager` *(v3.1)* |
| `tenant.mkt.engagement.triage_rules`, `.staffed_hours` | T | §Y.4.9 rules; 09:00–19:00 IST business days | priority order L | `marketing_manager` *(v3.1)* |

---

## Y.13 RBAC (permission bundles; roles per conventions)

| Permission | mktg mgr | content writer | designer | social exec | PR mgr | partnerships mgr | legal reviewer | compliance officer | DPO | finance ops | dept head | internal auditor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `mkt.strategy.write` / approve | W / A | R | R | R | R | R | R | R | — | R | A | R |
| `mkt.campaign.write` / approve | W / A | R | R | R | W | W | R | R | — | R (budget A) | A | R |
| `mkt.content.draft` | W | W | W | W | W | W | — | — | — | — | — | R |
| `mkt.content.brand_review` | A | — | — | — | A (PR items) | — | — | — | — | — | A | R |
| `mkt.content.compliance_review` | — | — | — | — | — | — | A | A (R3) | — | — | — | R |
| `mkt.content.publish_confirm` | W | — | — | W | W | — | — | — | — | — | — | R |
| `mkt.asset.manage` / rights | W | R | W | R | R | R | R | R | R (consents) | — | — | R |
| `mkt.send.create` / approve | W / A | W | — | W | — | — | R | R | R | — | A | R |
| `mkt.audience.define` / sensitive approve | W | — | — | — | — | — | — | A | A | — | — | R |
| `mkt.engagement.triage` | W | — | — | W | W | — | — | — | — | — | — | R |
| `mkt.pr.*` | R | W | W | R | W / A | — | A | R | — | — | A | R |
| `mkt.partner.*` | R | — | — | — | R | W | A (MoU) | R | R | R | A | R |
| `mkt.referral.payout_approve` | — | — | — | — | — | R | — | R | — | A | — | R |
| `mkt.analytics.view` | W | R | R | R | R | R | R | R | R | R | R | R |
| `mkt.settings.T` / `.G` | W / M | — | — | — | — | — | C (legal keys) | C | C (privacy keys) | C (budget keys) | C | R |

W = write, A = approve, R = read, M = maker for G-tier, C = checker for G-tier. `cms_editor`, `growth_manager` (P13) map to `content_writer` and `marketing_manager` bundles in the Operations Platform; `sales_executive` and `bd_manager` read campaigns and receive leads; `support_agent` receives E2/E4 tickets only. No marketing bundle includes any case-services permission (Appendix X), and `internal_auditor` has read-only access to everything including audit trails.

---

## Y.14 Data model (`mkt`)

Tables per module are listed in §Y.1.1; key columns and DDL are in P17 §7.2. No `mkt` table duplicates an Appendix X object: contact segments, the consent mirror, partner records and the partnership pipeline are read from `ops` by ID. Binding conventions: every table carries `id uuid` (uuidv7), `company_id` (legal entity; row-level security key, NN-38), `created_at`, `created_by`, `updated_at`, `version`, `status`; money as integer minor units + ISO-4217; no column may hold case identifiers, party names or case content (schema validator, ML-01); contact references are CRM IDs or HMAC hashes, never raw email or phone outside the consent projection and send executor payloads; binding constraints include `approver_id <> created_by` on every approval table, `cardinality(claim_keys) > 0` on messaging pillars, `reward_eligible = false` whenever `professional_class` is set, and `approved_hash` immutable once `status = 'approved'`.

---

## Y.15 APIs (summary; full table in P17 §7.3)

All under `/v1/ops/mkt/…` (OpenAPI 3.1; `Equator-Context` header; `Idempotency-Key` on every POST that creates a send, publication, payout or approval; step-up for G-tier changes and approvals). One resource per §Y.14 aggregate, with state-transition sub-resources (`/{id}/submit|approve|request-changes|schedule|confirm-publication|take-down|dispatch|pause|resume|close`). Inbound webhooks: Brevo events arrive at the single Appendix X ingress `/webhooks/brevo` (bearer token + IP allow-list; re-fetch before consent changes), which forwards engagement events to `mkt-analytics` through the outbox (`equator.ops.connector.engagement_received.v1`); `/webhooks/social/{adapter}` (platform signature where offered) is owned here.

---

## Y.16 Events (CloudEvents `equator.mkt.<entity>.<verb>.v1`; payloads carry IDs, never personal data)

`campaign.approved` · `campaign.paused` · `campaign.closed` · `content.submitted` · `content.approved` · `content.held` · `content.scheduled` · `content.published` · `content.evidence_overdue` · `content.taken_down` · `asset.rights_expiring` · `asset.consent_withdrawn` · `send.approved` · `send.dispatched` · `send.completed` · `send.paused_deliverability` · `suppression.added` · `engagement.routed` · `experiment.decided` · `budget.threshold_crossed` · `referral.reward_blocked` · `referral.reward_approved` · `pr.release_distributed` · `crisis.opened` · `crisis.closed` · `partnership.mou_signed` · `obligation.due` · `attribution.model_published` · `contribution.snapshot_published` · (v3.1) `calendar.conflict_detected` · `review.sla_breached`. Consumed: `equator.notices.respondent.served.v1` (hash only), `equator.consent.consent.withdrawn.v1` (P01), `equator.cms.page.published.v1`, `equator.cms.claim.expired.v1`, `equator.rev.stream.killed.v1` and `equator.rev.stream.status_changed.v1` (Appendix AB; kill or pause → pause dependent campaigns), `equator.cfg.setting.changed.v1` (Appendix V; flag and setting changes), `equator.ops.connector.engagement_received.v1` (Appendix X Brevo ingress).

---

## Y.17 Error codes (`MKT_`; register in Appendix F §F.10.4)

| Code | HTTP | Message (en) |
|---|---|---|
| `MKT_CLAIM_UNRESOLVED` | 422 | A claim in this content is missing, inactive or expired. |
| `MKT_LINT_BLOCKED` | 422 | This content breaks a publishing rule. See the lint report. |
| `MKT_REVIEW_REQUIRED` | 409 | This item needs the review shown before it can move on. |
| `MKT_SELF_APPROVAL` | 403 | You cannot approve an item you created or reviewed earlier. |
| `MKT_CASE_DATA_REJECTED` | 422 | Case data cannot be used in marketing. |
| `MKT_CONSENT_MISSING` | 409 | No valid marketing consent for this contact and purpose. |
| `MKT_SUPPRESSED_RECIPIENT` | 409 | This contact is suppressed from marketing. |
| `MKT_FREQUENCY_CAP` | 409 | This contact has reached the message limit for this period. |
| `MKT_QUIET_HOURS` | 409 | Messages cannot be sent at this time. |
| `MKT_DLT_TEMPLATE_UNREGISTERED` | 422 | The SMS template is not registered for promotional use. |
| `MKT_SENDER_DOMAIN_UNVERIFIED` | 409 | The sending domain failed authentication checks. |
| `MKT_MASS_SEND_APPROVAL_REQUIRED` | 409 | A second approver is needed for this send. |
| `MKT_BUDGET_APPROVAL_REQUIRED` | 409 | This budget needs approval at a higher level. |
| `MKT_BUDGET_EXHAUSTED` | 409 | The budget line is fully used. |
| `MKT_ASSET_RIGHTS_EXPIRED` | 409 | An asset's usage rights have expired. |
| `MKT_ASSET_CONSENT_MISSING` | 409 | A person shown in this asset has not consented. |
| `MKT_COBRAND_NOT_APPROVED` | 409 | Co-branding for this partner is not approved. |
| `MKT_PROHIBITED_TECHNIQUE` | 422 | This marketing technique is not allowed. |
| `MKT_COUNTDOWN_NOT_FIXED` | 422 | Countdowns must use a fixed end time from an event or offer. |
| `MKT_SCARCITY_UNBOUND` | 422 | Availability claims must come from a real capacity record. |
| `MKT_PRICE_CLAIM_UNBOUND` | 422 | Prices must come from a published fee schedule or plan. |
| `MKT_TESTIMONIAL_UNVERIFIED` | 422 | Testimonials need a verified, consented claim record. |
| `MKT_ADVOCATE_REWARD_BLOCKED` | 403 | Referral rewards cannot be given to advocates, CAs, CSs or CMAs. |
| `MKT_SENSITIVE_TARGETING_BLOCKED` | 403 | This targeting attribute is not allowed. |
| `MKT_EXPERIMENT_PROHIBITED_SURFACE` | 422 | Experiments are not allowed on this surface. |
| `MKT_UTM_INVALID` | 400 | The tracking link does not follow the convention. |
| `MKT_HANDOFF_INCOMPLETE` | 422 | The hand-off package is missing required fields. |
| `MKT_PUBLISH_EVIDENCE_REQUIRED` | 409 | Record the post URL and screenshot to complete publication. |
| `MKT_SOCIAL_ADAPTER_DISABLED` | 409 | Publishing through this platform connection is switched off. |
| `MKT_PLATFORM_LIMIT_REACHED` | 429 | The platform's posting limit has been reached. |
| `MKT_CRISIS_PAUSE_ACTIVE` | 409 | Publishing is paused while a crisis is open. |
| `MKT_EMBARGO_ACTIVE` | 409 | This release is under embargo. |
| `MKT_MOU_LEGAL_REVIEW_REQUIRED` | 409 | This agreement needs legal review before approval. |
| `MKT_GROUP_SCOPE_NOT_GRANTED` | 403 | No cross-company grant covers this data. |
| `MKT_ATTRIBUTION_MODEL_UNAPPROVED` | 409 | This attribution model version is not approved. |
| `MKT_COMPETITOR_FIGURE_BLOCKED` | 422 | A competitor figure that is self-reported, third-party or past its re-verification date cannot be published (Appendix AF FR-P13-V3-AF02). |
| `MKT_CALENDAR_CONFLICT` | 409 | This schedule conflicts with a blocking calendar rule. See the conflict list. *(v3.1)* |

---

## Y.18 Audit and exports

**Audit (NN-22):** hash-chained events for every approval, override (lint, tier raise), publication confirmation, takedown, send dispatch, audience snapshot, suppression and send-hold change, setting change, adapter flag change, payout approval, crisis open/close and MoU approval; screenshots and rights evidence under Object Lock. **Exports (NN-37, D3-07, D3-41):** the marketing workspace exports through `POST /v1/exports` with scope `OPS_DEPARTMENT` (the Marketing, Brand and Content department of one legal entity; Appendix AC §AC.13.3) as an `EQ-EXPORT-1.0` package with the Appendix AC taxonomy and naming: root `Equator_Export_<OrgSlug>_<YYYY-MM-DD>` (≤ 40 characters; ZIP `<root>.zip`), `00_README.pdf` and `.html`, `00_Contents.xlsx`, `99_Manifest/` (manifest CSV + JSON, SHA-256, schemas), paths below the root ≤ 140 characters (AC §AC.13.7). Marketing records sit in `06_Marketing/` with the AC §AC.13.6 minimum files plus subfolders `Strategy/` (OKRs, market segments, messaging houses — DOCX/XLSX), `Campaigns/` (briefs DOCX, budgets and spend XLSX), `Content_and_Social/` (per item: approved version PDF, assets, publication evidence), `Brand_Assets/` (assets with rights and consent PDFs), `Email_and_Messaging/` (sends XLSX, suppression counts — no hashes of other companies), `Funnels_and_Automations/` (sequences, automation definitions JSON + readable DOCX), `PR/` (releases PDF/A, coverage XLSX), `Partnerships/` (MoUs PDF/A, obligations XLSX); analytics snapshots and attribution model definitions go to `08_Reports/Marketing_Analytics/` and the audit extract (CSV/JSON) to `08_Reports/Audit_Trail/`. Contact-level consent artefacts are exported only to the DPO; exports of personal data are maker-checker (NN-36).

---

## Y.19 Open items and legal verification flags

1. **[VERIFY — open (counsel):** whether institution-run neutral features (meet-the-panel content) are "advertising" by advocate-neutrals under BCI r.36 (OI-03); speaker honoraria to advocates (§Y.3.3(5)).]
2. **[VERIFY — open:** TCCCPR promotional SMS permitted hours, header suffix letters and digital consent acquisition steps; whether Brevo supports Indian DLT template IDs ([RD] F3.1).]
3. **[VERIFY — open:** current mailbox-provider bulk-sender requirements and complaint thresholds (§Y.6.4).]
4. **[VERIFY — open:** Consumer Protection (E-Commerce) Amendment Rules 2026 Gazette text and commencement (reference-price rule, sponsored labelling, self-audit) ([RB] OP-06; [RE] F3.1).]
5. **[VERIFY — open:** Meta `pages_manage_posts` review requirements; Instagram 50 vs 100 daily API post limit; LinkedIn Community Management API approval for Equator's use cases ([RD] F3.3).]
6. **[VERIFY — open (counsel):** DPDP s.3(c)(ii) reliance for media lists (§Y.8.1).]
7. **[VERIFY — open:** rules on synthetically generated content labelling applicable to marketing imagery (§Y.4.4).]
8. **[VERIFY — open:** Teams webinar features on the confirmed Microsoft 365 SKU (D3-04).]
9. **[VERIFY — open:** trade-mark filings for Equator marks; short-link domain registration.]
10. **[VERIFY — open (counsel):** emblem and government-name rules for programme partnerships (§Y.5.5).]
11. Brevo DPA, sub-processor list and INR pricing before `mkt.brevo.enabled` ([RD] open point 5).

---

## Y.20 Phase addenda

### For P13

**FR-P13-V3-Y01 — Landing-page block library.** Add the CMS content type `landing_page` with the §Y.7.3 blocks and page-level rules; `CountdownBlock`, `CapacityBlock`, `PriceBlock` and `VideoBlock` validate their bindings at save and publish. *Acceptance:* a countdown without an event/offer end time fails with `MKT_COUNTDOWN_NOT_FIXED`; a video without captions cannot publish.

**FR-P13-V3-Y02 — Lint profiles for channels.** Extend `packages/content-lint` with SL-01–SL-20 and MT checks as profiles `social`, `email`, `sms`, `whatsapp`, `ads`, `press`, shared with the Operations Platform. *Acceptance:* the fixture corpus yields exactly the expected SL IDs.

**FR-P13-V3-Y03 — Claims across surfaces.** `growth.claims_register.permitted_surfaces` gains `social`, `email`, `sms`, `whatsapp`, `press`, `ads`, `event`; `growth.claim_usages` records `mkt` content versions; claim expiry emits events consumed by MA-07. *Acceptance:* expiring a claim holds every scheduled `mkt` item using it within 5 minutes.

**FR-P13-V3-Y04 — Partner portal amendment (X-54).** Partner types CA, CS, law firm/advocate become relationship partners with `reward_eligible = false`; platform credits for advocates removed. *Acceptance:* creating a reward for a professional-class partner fails with `MKT_ADVOCATE_REWARD_BLOCKED`.

**FR-P13-V3-Y05 — Company-scoped consent purposes.** Website forms capture marketing purposes per company scope and channel; double opt-in for newsletters. *Acceptance:* a consent for Equator does not appear in a Finbyx audience.

**FR-P13-V3-Y06 — Lead hand-off to Appendix X CRM with UTM first/last touch and campaign code (X-53).** *Acceptance:* a form submission creates one CRM lead with the campaign code resolved from UTM.

**FR-P13-V3-Y07 — Experiment register mirroring.** P13 experiments are mirrored into `mkt.experiments` with hypothesis and decision fields mandatory. *Acceptance:* an experiment without a hypothesis cannot start.

**FR-P13-V3-Y08 — Operator footer.** BP-04 on every landing and paid-webinar page. *Acceptance:* LINT check fails when absent.

### For P11

**FR-P11-V3-Y01 — `marketing_copy_assistant`.** Drafts captions, variants, subject lines and summaries only from the referenced messaging house, active claim texts, boilerplates and brief; cannot introduce numbers, comparisons, legal effects or names not in its inputs (output validator); outputs `ai_generated = true` and pass the normal review tier. *Acceptance:* a request for "India's leading ODR platform" is refused and an approved line from the house is offered; any number not in the inputs is stripped and flagged.

**FR-P11-V3-Y02 — `social_triage_classifier`.** Classifies engagement items into E1–E10 with confidence; never replies; E4, E6 and E7 detections route to a human immediately; distress cues use the GX-5 handoff template. *Acceptance:* the eval set (≥ 300 labelled items, en/hi) reaches the precision/recall thresholds set in Appendix E; no automatic reply is sent.

**FR-P11-V3-Y03 — Accessibility drafting.** Alt-text and caption/subtitle drafts for assets, human-approved. *Acceptance:* drafts stored as suggestions; SL-06/SL-07 still require human acceptance.

**FR-P11-V3-Y04 — Marketing guardrail evals.** Eval suites for superlatives, urgency, fear framing, merits/outcome language, regulator endorsement and case references in marketing outputs; gateway I3 extended with an `mkt` context guard rejecting CRM personal data and case data in prompts. *Acceptance:* zero-tolerance categories at 0 failures on the release eval.

**FR-P11-V3-Y05 — Synthetic media rules.** Image/video generation, if enabled (`mkt.ai.image_generation.enabled`, OFF), cannot depict real or realistic people as customers, parties, neutrals or staff, courts presented as real, or official emblems; outputs flagged `synthetic_media = true`. *Acceptance:* prompt classifier blocks the listed subjects.

### For P14

**FR-P14-V3-Y01 — Marketing go-live gate.** Launch of marketing sends requires: SPF/DKIM/DMARC alignment green on the marketing subdomain; RFC 8058 headers present; suppression test `NN-16_*` extended to Brevo, MSG91/Gupshup, ad exports and `mkt` audiences; consent propagation ≤ 15 min proven; Brevo DPA and transfer-register row on file; migration rehearsal MA-32 passed. *Acceptance:* gate checklist signed by `compliance_officer` and DPO.

**FR-P14-V3-Y02 — Dark-pattern self-audit scope.** The quarterly `DarkPatternAuditJob` (App. O §6.2) samples live landing pages, campaign emails and paid ads. *Acceptance:* audit report lists marketing samples and findings.

**FR-P14-V3-Y03 — Crisis tabletop.** Two tabletop exercises a year using §Y.8.4 (one data-breach scenario, one impersonation scenario). *Acceptance:* exercise reports with actions tracked to closure.

**FR-P14-V3-Y04 — Social account security.** Every social and executor account: owner of record, MFA, no shared passwords (vault or platform business manager roles), quarterly admin-roster review, removal within the leaver SLA. *Acceptance:* quarterly attestation stored; a leaver retains no social admin role after the SLA.

**FR-P14-V3-Y05 — Marketing data retention and DSR.** Retention jobs for engagement content, attendees and touchpoints; DSR propagation MA-31 tested end to end. *Acceptance:* an erasure request removes the contact from `mkt` and every executor and leaves a suppression hash.
