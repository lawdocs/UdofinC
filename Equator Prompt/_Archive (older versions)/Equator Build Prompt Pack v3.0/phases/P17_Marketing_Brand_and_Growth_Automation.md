# Phase P17 — Marketing, Brand and Growth Automation

> Paste after `01_MASTER_PROMPT.md`. **Reference specification: Appendix Y** (binding for every catalogue, rule and setting named here). **Dependencies (must be done first):** **P13** (public website, Payload CMS, Claims Register `growth.claims_register`, copy lint LINT-001–LINT-050, analytics taxonomy, web experiments, neutrality firewall FR-P13-26); **P15** (Appendix V deliverables — in particular the NN-33 configuration service, tier badges, maker-checker for G-tier settings and the settings UI that §9 registers into); **P16** (Appendix X — the Operations Platform shell `apps/ops`, Keycloak client `eq-portal-ops`, the CRM (contacts, accounts, opportunities, contact segments, the consent mirror `ops.crm_comm_prefs`/`ops.crm_marketing_view`, partner records and the `partnership` pipeline, tickets), the single Brevo webhook ingress and the generic automation engine that §4G builds on). Interface names are those of Appendix X (`/v1/ops/crm/*`, `/v1/ops/automations`, `ops.crm_marketing_view`, `OPS_*` engine codes) and Appendix V (configuration service); master X-53. Also reads from P01 (consent ledger `core.consent_records`), P05 (published fee schedules, promotion ledger), P07 (`MESSAGING_PORT`, DLT templates, SES domains) and P11 (AI gateway). Estimated effort: 6 sprints (2-week) for a squad of 7 (3 full-stack engineers, 1 integrations engineer, 1 designer, 1 QA, 0.5 legal reviewer embedded, 0.5 analytics engineer).

---

## 1. Objective and business outcome

Give Equator (and, under NN-38 controls, each group company) one governed workspace in which marketing, brand, social media, PR and partnerships are planned, approved, executed and measured — while the tools that send or publish (Brevo, Adobe Express, social platforms, ad platforms) remain replaceable executors (NN-40, D3-25).

Outcomes:

1. **One calendar, one truth.** Every campaign, post, newsletter, webinar, press release and partner asset has an owner, an approved version with a frozen hash, claims resolved against the Claims Register (NN-17) and evidence of publication — including posts published manually in Adobe Express Content Scheduler, which has no publishing API (D3-26; [RD] F3.2).
2. **Compliant by construction.** Prohibited funnel techniques (fake scarcity, resetting timers, locked video players, unverified testimonials, outcome promises) cannot be built (D3-28); dark patterns DP-01–DP-13 stay linted (NN-29); case data never enters marketing (NN-16, ML-01); served respondents are suppressed everywhere (FR-P13-26(c)); no referral rewards reach advocates, CAs, CSs or CMAs (D3-27; NN-34).
3. **Autopilot with human checkpoints.** Thirty-one live marketing automations (MA-01–MA-32; MA-30 retired in favour of Appendix X OA-11) run on the Appendix X engine; public claims, pricing claims, testimonials, sensitive targeting and mass sends always stop for a human approval (R-56).
4. **Measured honestly.** Versioned attribution models, CAC/LTV by segment, budget versus ROI, and outcome-based contribution metrics for marketing staff that feed Appendix Z appraisal without surveillance (NN-35; D3-29).

Exit-gate outcomes: zero published items without evidence older than 24 h in UAT; 100% of sends pass suppression and consent checks (seeded respondent test across every executor); every automation with an outbound public action has an approval node; Brevo migration rehearsal passed; NN-16, NN-17, NN-29, NN-34, NN-35, NN-38, NN-40 test packs green.

---

## 2. Scope (in / out)

**In:** marketing workspace in `apps/ops` (schema `mkt` in the isolated business database, Appendix X D3-20); objectives/OKRs, market segments (SEG-*), ICPs, messaging houses; campaigns, budgets, spend, UTM link builder, experiments register; content and social calendar for non-web channels with brand and compliance review, risk tiers R0–R3, channel lint SL-01–SL-20; Adobe Express hand-off package and optional Embed SDK route (flag OFF); `SOCIAL_PORT` adapters (`linkedin_cm`, `meta_graph`, `x_v2`, `youtube_data`, all OFF) and the default `manual_handoff`; publication evidence; engagement inbox and triage E1–E10; brand asset library with rights and consent records, boilerplates, co-branding approvals; marketing email through `MARKETING_PORT` (`brevo`, `ses_marketing` fallback), promotional SMS and WhatsApp marketing through `MESSAGING_PORT`; send-time consent checks over the Appendix X consent mirror, marketing suppression, list hygiene, sender-domain authentication, frequency caps, quiet hours, mass-send approval; lead magnets registry, landing-page block library (in the P13 CMS, FR-P13-V3-Y01), nurture sequences, webinar funnel, events, referral programmes RP-01–RP-05, training cross-sell gate; marketing automations MA-01–MA-32; PR (media list, releases, coverage, spokespersons, crisis room); partnerships, MoUs, obligations, joint events; SEO/GEO planning objects; touchpoints, attribution model registry, dashboards D-01–D-12, economics; contribution metrics feed to Appendix Z; marketing settings registration (Appendix Y §Y.12); exports (NN-37) and migration rehearsal; phase addenda from Appendix Y §Y.20 for P13, P11 and P14.

**Out:** website pages, CMS workflow and Claims Register internals (P13); CRM data model, contact segments, consent mirror, partner records and pipeline, lead routing, tickets, the Brevo webhook ingress and the automation runtime (P16 / Appendix X); transactional and case communications (P07); revenue-stream registry and kill switches (D3-08 owner phase); Private Practice Marketplace and sponsored placement (`mkp`, NN-34); professional registry (`dir`, NN-39); appraisal cycles and ratings (Appendix Z / P18); paid-media buying strategy and agency selection (business activity; P17 only records budgets and results); ad-platform API adapters beyond read-only spend sync (MA-29, OFF).

---

## 3. Personas and permissions touched

| Actor | Role code (conventions) | Can | Cannot |
|---|---|---|---|
| Marketing manager | `marketing_manager` | Own strategy, campaigns, budgets within limits, brand review, approve mass sends (as second approver for staff), configure T-tier marketing settings, propose G-tier changes | Approve own items; approve legal review; lower a risk tier; see case data |
| Content writer | `content_writer` (P13 `cms_editor` maps here) | Draft content, request AI drafts, attach claims and boilerplates, build sequences | Approve; publish; send |
| Designer | `designer` | Create assets and templates, upload Adobe exports, manage rights evidence | Approve own assets for brand |
| Social media executive | `social_media_executive` | Schedule approved items, confirm publication with evidence, triage engagement, use approved response bank | Publish unapproved content; reply on E3–E8 outside the response bank |
| PR manager | `pr_manager` | Media list, releases, coverage, crisis statements (draft), spokesperson register | Distribute without approvals; comment on cases |
| Partnerships manager | `partnerships_manager` | Partnership pipeline, MoUs (draft), obligations, joint events, referral programmes | Approve MoUs; approve payouts |
| Legal reviewer | `legal_reviewer` | Compliance review of R2/R3 items, claims, MoUs, crisis statements; checker for legal G-tier settings | Author items they review |
| Compliance officer | `compliance_officer` | R3 second review; sensitive targeting approval; evidence sampling; checker for compliance settings | — |
| DPO | `dpo` | Consent purposes, suppression administration, DSRs, privacy settings, media-list basis | — |
| Finance ops | `finance_ops` | Budget approvals per authority matrix, spend reconciliation, referral payout approval, attribution model co-approval | Create payees and approve their payment (NN-36) |
| Department head | `department_head` | Higher budget approvals; second approver where the maker is the marketing manager | — |
| Ops director | `ops_director` | Crisis lead; top budget tier; government/regulator announcements | — |
| Sales / BD | `sales_executive`, `bd_manager` | Read campaigns; receive leads (Appendix X) | Edit marketing content |
| Support agent | `support_agent` | Receive E2/E4 tickets | See marketing data beyond the ticket |
| IT admin | `it_admin` | Sender domains, adapter tokens (vault), social account security | Approve content |
| Group admin | `group_admin` | Group-scope settings, cross-company grants with DPO | Bypass NN-38 |
| Internal auditor | `internal_auditor` | Read everything incl. audit trails | Write |
| HR manager / employee | `hr_manager`, `employee` | Consume contribution metrics (Appendix Z); employees view and dispute their own | Edit metric values |

All roles sign in through `eq-portal-ops` with phishing-resistant MFA. No marketing bundle carries any case-services permission (Appendix Y §Y.13).

---

## 4. Functional requirements

### 4A. Foundation and boundaries

**FR-P17-01 — Workspace shell and module registration.** Register the Marketing area in the Operations Platform navigation (Strategy · Campaigns · Calendar · Brand · Messaging · Growth · PR · Partnerships · SEO · Analytics · Settings) with the eleven `mkt-*` modules of Appendix Y §Y.1.1, company-scoped (D3-02). Every screen shows the active company and blocks cross-company records without a grant (`MKT_GROUP_SCOPE_NOT_GRANTED`). *Acceptance:* a user of Equator's workspace cannot list Finbyx campaigns; switching company re-scopes every query (RLS test).

**FR-P17-02 — Database plane and neutrality firewall.** Create schema `mkt` in the isolated business database with `growth` and `ops` (Appendix X D3-20; master X-53); DB role `eq_mkt` has `USAGE` on `mkt` and `SELECT` only on `ops.crm_marketing_view`; no grants from core roles, no grants to core; cross-boundary data only via the outbox with the FR-P13-26(b) schema validator; inbound events limited to the allow-list in Appendix Y §Y.1.2. A `MarketingIngressGuard` rejects payloads carrying case identifiers, party names, pleadings or offers with `MKT_CASE_DATA_REJECTED` and raises a security alert. *Acceptance:* the `NN-16_mkt_ingress` test injects an event with a case number and a party name; it is rejected, logged and alerted; a DB-role test proves `eq_mkt` has no privilege on `core.*`.

**FR-P17-03 — System-of-record and sync framework.** Register the Appendix Y §Y.1.3 rows in `cfg.system_of_record` (Appendix AC §AC.12.1; no marketing-local copy), with per-executor sync jobs (batched, queue-based, idempotent), conflict rules (Equator wins; withdrawal anywhere wins everywhere) and a daily reconciliation report per executor (counts of contacts, list memberships, suppressions; diffs > 0.5% raise a task). *Acceptance:* editing a Brevo contact attribute that Equator owns is overwritten at the next sync and logged; a suppression present in Equator but missing in Brevo is re-pushed and reported.

**FR-P17-04 — Settings registration.** Register every key in Appendix Y §Y.12 with tier (L/G/T), default, bounds, who may change, approval rule, help text and source citation in the P15 configuration service; the settings screen shows the tier badge and approval requirement (NN-33). *Acceptance:* a T-tier change applies immediately with audit and one-click rollback; a G-tier change stays `pending` until a different authorised checker approves; L-tier keys render read-only with their source.

### 4B. Strategy

**FR-P17-05 — Objectives and key results.** CRUD for objectives and key results per Appendix Y §Y.2.1; key results must reference a metric in `mkt.metric_definitions`; prohibited targets (settlement rate, outcomes, allocation, respondent conversion) are rejected (`VALIDATION_FAILED` with rule `MKT-OKR-PROHIBITED`); quarterly close with attainment snapshot. *Acceptance:* a key result on "settlement rate" cannot be saved; closing a quarter freezes values and versions later edits.

**FR-P17-06 — Segments, ICPs and messaging houses.** Seed market segments (`mkt.market_segments`) SEG-LEN…SEG-PAR with their locked restrictions (Appendix Y §Y.2.2) and the seed houses MH-LEN-01, MH-IND-01, MH-NEU-01, MH-EMP-01 (status `draft`, legal review required). Messaging pillars require at least one claim key; approval needs `marketing_manager` + `legal_reviewer` (≠ author). Claim expiry flags every house that lists the claim and holds dependent scheduled content (MA-07). *Acceptance:* a pillar without a claim key cannot be approved; expiring `svc.explorer_free` flags MH-IND-01 and holds its scheduled items within 5 minutes.

### 4C. Campaigns

**FR-P17-07 — Campaign briefs and lifecycle.** Campaign brief fields and state machine per Appendix Y §Y.3.1–§Y.3.2; offers must reference a published plan, fee schedule or lead magnet and a revenue stream `live` in scope (D3-08; Appendix AB AB-R1); SEG-IND campaigns inherit risk floor R2 and Track A rules; automatic `paused` on claim expiry, flag OFF, revenue-stream kill or pause (`equator.rev.stream.killed.v1`, `equator.rev.stream.status_changed.v1`), crisis C1/C2 or budget exhaustion. *Acceptance:* disabling the revenue stream behind a campaign's offer pauses the campaign and its scheduled items and notifies the owner.

**FR-P17-08 — Budgets and spend (NN-36).** Budgets and budget lines in INR minor units with GST treatment; approval through the `ctl` authority matrix using the §Y.3.3 default limits; spend entries linked to budget lines with weekly unlinked-spend exceptions; 90% alert and 100% pause (MA-12); payees only through the `ctl` payee workflow; `paid_partnership` flag on influencer or publication spend forces the SL-13 label on related content; payees with `professional_class` set cannot receive referral or promotion payments. *Acceptance:* a ₹6,00,000 budget cannot be approved by the marketing manager alone; the same user cannot approve the budget and approve the vendor's payment; spend reaching 100% pauses the line's paid channels.

**FR-P17-09 — UTM link builder and short links.** Generate links per the Appendix Y §Y.3.4 convention with registry-validated source and medium, campaign code mapping, content/variant IDs, optional short link and QR (SVG/PNG); reject personal data in parameters and links into authenticated or case routes (`MKT_UTM_INVALID`). *Acceptance:* `utm_content=ravi@example.com` is rejected; a link to `/app/cases/...` is rejected; generated links resolve and carry the expected parameters.

**FR-P17-10 — Experiments register.** One register for web (mirrored from P13 FR-P13-24) and non-web experiments with mandatory hypothesis, primary metric, MDE, sample-size calculation, variants that are approved content versions, prohibited surfaces (Appendix Y §Y.3.5) and harm-based early stopping; decision `adopt | reject | iterate` recorded. *Acceptance:* an experiment targeting `/fees` or a consent form is rejected with `MKT_EXPERIMENT_PROHIBITED_SURFACE`; an email experiment auto-stops when the unsubscribe rate in a variant exceeds the threshold.

### 4D. Content and social calendar

**FR-P17-11 — Calendar and item lifecycle.** Calendar views (month, week, list; filter by channel, account, campaign, segment, owner, status, risk tier) and the item state machine of Appendix Y §Y.4.2 with system-enforced gates; web items (WEB, BLOG) link to the P13 CMS page version and take status from CMS events instead of running a second review (X-53); any edit after approval creates a new version and re-enters review. *Acceptance:* editing one character of an approved caption returns the item to `brand_review`; a WEB item shows `published` only after `equator.cms.page.published.v1` for its page version.

**FR-P17-12 — Risk tiering.** Compute R0–R3 per Appendix Y §Y.4.3 from type, segment, detected entities (statute, regulator, price, person, competitor, sensitive topic), claims, lint hits and audience size; the computed tier is a floor; reviewers may raise but not lower (`MKT_REVIEW_REQUIRED`); R0/R1 sampling queues for legal review at the configured percentages. *Acceptance:* a post mentioning "RBI" is R2 at minimum; an attempt to set it to R1 fails; 10% of R1 items in a month appear in the legal sampling queue.

**FR-P17-13 — Channel lint.** Run LINT-001–LINT-050 plus SL-01–SL-20 and MT checks (FR-P13-V3-Y02 profiles) on save and on submit; B-rules block submission (`MKT_LINT_BLOCKED`); W-rules show in the reviewer panel; overrides allowed only on non-† rules by `legal_reviewer` with reason, audited. *Acceptance:* the fixture corpus (one violating item per rule per channel profile) yields exactly the expected rule IDs; `#RBIApproved` blocks (SL-02 †) with no override option.

**FR-P17-14 — Claims and boilerplates in content.** Inline claim nodes and boilerplate inserts in every channel editor; claim status checked at submit, at approval and at scheduled time; on expiry the item moves to `held` (or the claim's approved fallback text is used if the item's owner pre-selected "use fallback" and the fallback is approved for that surface). Usage written to `growth.claim_usages` (FR-P13-V3-Y03). *Acceptance:* scheduling a post whose claim expires before the scheduled time is blocked with `MKT_CLAIM_UNRESOLVED`.

**FR-P17-15 — Adobe Express hand-off.** On approval generate the hand-off package of Appendix Y §Y.4.7 (screen + ZIP with `handoff.json`); designs created through the Embed SDK (flag `mkt.adobe_embed.enabled`, OFF) save back to the DAM; native Adobe designs are uploaded as exports with SHA-256. The DAM copy is the approved asset. *Acceptance:* a package missing alt text, captions file (video) or caption for a target platform fails with `MKT_HANDOFF_INCOMPLETE`; the ZIP's `handoff.json` contains the approved hash and claim keys with expiry.

**FR-P17-16 — `SOCIAL_PORT` adapters.** Implement adapters `linkedin_cm`, `meta_graph` (Instagram and Facebook), `x_v2`, `youtube_data` and the default `manual_handoff` per Appendix Y §Y.4.6 and [RD] F3.3: each behind its flag (OFF), enabled only by `marketing_manager` (maker) + `legal_reviewer` (checker) per Appendix AC §AC.17 after the access-grant evidence is uploaded and `it_admin` has recorded the token-storage review; tokens in the secrets vault; per-account counters (Instagram daily cap default 50; YouTube 100 uploads/day ceiling; X monthly credit budget); payload hash compared with the approved hash before publish; failures fall back to a manual hand-off task. *Acceptance:* with `meta_graph` OFF an Instagram item routes to manual hand-off; with it ON in sandbox the 51st API post in 24 h fails with `MKT_PLATFORM_LIMIT_REACHED`; a payload differing from the approved hash is not sent and raises an incident.

**FR-P17-17 — Publication evidence.** Capture evidence per route (Appendix Y §Y.4.8): API post IDs and permalinks; for manual routes, post URL, IST timestamp, screenshot (PNG/JPEG ≤ 5 MB, SHA-256, Object Lock) and attestation; `evidence_overdue` at T+24 h (MA-08) with escalation at T+48 h; monthly sample verification by `compliance_officer`; mobile capture (camera roll upload) supported. *Acceptance:* an item scheduled at 10:00 without evidence by 10:00 next day shows `evidence_overdue` and notifies owner and marketing manager; evidence objects cannot be deleted (Object Lock test).

**FR-P17-18 — Engagement inbox and triage.** Ingest comments, mentions and DMs from read adapters (when ON) or manual logging; classify E1–E10 (P11 `social_triage_classifier` proposes; human confirms); route E1 to the CRM as a lead with consent capture link (MA-03), E2/E4 to Appendix X support tickets (E4 as category `case_procedure` routed to Case Services, with no case link and no content copied into `mkt`), E3 to a ticket converted to an `EQ_SERVICE` grievance (Appendix X §X.8; 48-hour acknowledgement), E5 to PR, E6/E7 to moderation and safety; response bank templates for E3–E8; auto-acknowledgement for E1/E2/E9 only when enabled; DM content purged after the retention period. *Acceptance:* a comment "my hearing with Mr X is tomorrow, why is the mediator biased" is routed E4, the public reply template is offered, no case content is stored in `mkt`, and the ticket reaches the case-services queue in Appendix X.

**FR-P17-19 — Takedown and corrections.** Take-down action on any published item with reason, correction note and SLA (legal-effect or safety errors within 24 hours; others within 7 days — App. P §7.6); the operator records removal evidence for manual routes; corrections of material public statements are added to `/about/corrections` through the P13 workflow. *Acceptance:* a takedown opened at 10:00 for a legal-effect error alerts at 10:00 next day if removal evidence is missing.

### 4E. Brand

**FR-P17-20 — Brand asset library (DAM).** Asset classes, metadata, versions, S3 storage, Object Lock for rights evidence, search by tag, segment, channel and rights status; templates carry identity-line and disclosure slots; legacy Equa material quarantined (U.12; SL-18). *Acceptance:* an asset without a rights record cannot be attached to a content item; a quarantined legacy logo cannot be downloaded except by `marketing_manager` with a reason.

**FR-P17-21 — Rights and consent expiry.** `AssetRightsExpiryJob` (daily) raises T-30/T-7/expiry events, removes expired assets from templates, holds scheduled items and lists published items for review; consent withdrawal by a person in an asset triggers immediate hold and a takedown task within the configured hours (default 72). Neutral and staff consent is never a condition of empanelment or employment; minors are never used. *Acceptance:* withdrawing a staff member's photo consent holds three scheduled posts and creates takedown tasks for two published ones due within 72 h.

**FR-P17-22 — Boilerplate register.** BP-01–BP-10 seeded from App. P with versions and locale texts; content inserts by reference so updates propagate to unscheduled drafts and flag scheduled items for re-approval; BP-04 operator footer mandatory on landing and paid-webinar pages (FR-P13-V3-Y08). *Acceptance:* publishing a new BP-03 version marks every scheduled email using BP-03 for re-approval.

**FR-P17-23 — Co-branding approvals.** Records per Appendix Y §Y.5.5 (partner, asset, scope, expiry, evidence, approver); PTN items cannot be approved without an active co-brand approval (`MKT_COBRAND_NOT_APPROVED`); government or regulator-related co-branding is R3 with `ops_director` approval. *Acceptance:* a university co-branded poster cannot reach `approved` until the university's written approval is attached and recorded.

### 4F. Email and messaging marketing

**FR-P17-24 — `MARKETING_PORT` and executors.** Implement `MARKETING_PORT` (campaign create/schedule, static list sync, marketing-class email) with adapters `brevo` (flag `mkt.brevo.enabled` OFF until DPA and transfer-register row `BREVO_EU`) and `ses_marketing` (separate SES configuration set on the marketing subdomain); promotional SMS and WhatsApp marketing through P07 `MESSAGING_PORT` (MSG91/Gupshup) with DLT promotional templates and Meta marketing templates; Brevo SMS/WhatsApp behind `mkt.brevo.sms_whatsapp.enabled` (OFF). Brevo sync respects the shared account budget `tenant.mkt.brevo.max_requests_per_hour` (default 80/h; one token bucket with the Appendix X CRM sync), uses bulk import above 50 records and treats 429 as `RATE_LIMITED` with back-off. The port is never used for case notices or OTPs (locked). *Acceptance:* a case-notice template cannot be selected in a marketing send; with Brevo OFF a newsletter dispatches through `ses_marketing`; a sync of 5,000 contacts completes within the hourly budget using bulk import.

**FR-P17-25 — Consent checks and propagation.** Read consent state by purpose, channel and company scope from `ops.crm_marketing_view` (Appendix X mirror of `core.consent_records`; no second projection in `mkt`) at audience snapshot and again per dispatch batch; propagate withdrawals to MSG91, Gupshup and `ses_marketing` within 15 minutes (MA-01; Brevo's blocklist is updated once by `CRM_PORT.brevo.applyOptOut`); executor-originated opt-outs (Brevo `unsubscribed`, SMS STOP, WhatsApp opt-out) arrive through the single Appendix X ingress and are re-fetched from the executor API before the consent ledger changes; if the re-fetch fails, an immediate send hold (`mkt.suppressions` reason `pending_verification`) applies until confirmation (fail-safe without rewriting consent on unverified data); 90-day re-ask cooldown; double opt-in for newsletters; preference centre via signed link (FR-P13-22). *Acceptance:* an unsubscribe webhook from Brevo creates a withdrawal in Equator and removes the contact from MSG91 and Gupshup marketing lists within 15 minutes; a webhook with an invalid bearer token is rejected and does not change consent.

**FR-P17-26 — Suppression and list hygiene.** Implement the suppression lists and hygiene rules of Appendix Y §Y.6.3 (respondent hashes read from `growth.suppression_hashes`, pending-verification holds, withdrawals, bounces, complaints, DND/preference mismatch, minors, legal hold, DSR erasure hashes, inactivity sunset); bulk imports require a consent artefact per row; purchased or scraped lists are rejected (ML-09). *Acceptance:* `NN-16_mkt_suppression` seeds a served respondent and proves exclusion from Brevo sends, SMS, WhatsApp, ad audience exports and `mkt` audiences; a CSV import row without consent source is rejected with `MKT_CONSENT_MISSING`.

**FR-P17-27 — Sender domains and authentication.** Marketing subdomain separate from transactional; SPF, DKIM (2048-bit, rotation ≤ 12 months), DMARC alignment and progression to `p=reject` after 30 clean days; RFC 8058 one-click unsubscribe headers on every marketing email; daily DNS/auth checks; sends blocked if checks failed in the last 24 h (`MKT_SENDER_DOMAIN_UNVERIFIED`); deliverability guard pauses sends at the complaint threshold (MA-13). *Acceptance:* removing the DKIM record in staging blocks the next send; a seeded 0.31% complaint rate pauses the send and alerts.

**FR-P17-28 — Frequency caps and quiet hours.** Per-contact counters across campaigns and channels with the Appendix Y §Y.6.5 defaults and bounds, a group-wide cap where consents overlap, stricter caps for SEG-IND/SEG-NRI, and quiet hours for SMS/WhatsApp in the recipient's local time; transactional and case messages are excluded from counting. *Acceptance:* a contact who received 4 marketing emails in 30 days is skipped with `MKT_FREQUENCY_CAP` in the send report; an SMS scheduled at 20:00 is deferred to the next window.

**FR-P17-29 — Mass-send approval.** Sends above the mass threshold or to SEG-IND/SEG-NRI audiences require a frozen audience snapshot (counts by suppression reason), a seed-list test send and a second approver per Appendix Y §Y.6.6; the approval screen shows audience after suppression, purposes, caps skipped, claims and expiry, sender-domain status and estimated cost. *Acceptance:* dispatch without a second approval fails with `MKT_MASS_SEND_APPROVAL_REQUIRED`; the maker cannot be the approver.

### 4G. Growth funnels and autopilot

**FR-P17-30 — Funnel technique register enforcement.** Load MT-01–MT-24 (Appendix Y §Y.7.1) into the lint and block validators; class P techniques are blocked in every builder (CMS blocks, email builder, ads) with `MKT_PROHIBITED_TECHNIQUE`, and class R techniques require their bindings (event/offer record, capacity record, stored prior price, claim record). *Acceptance:* a countdown configured "24 hours from first visit" is rejected with `MKT_COUNTDOWN_NOT_FIXED`; a "12 seats left" block without a cohort capacity binding fails with `MKT_SCARCITY_UNBOUND`; an "original price" without a stored prior price fails with `MKT_PRICE_CLAIM_UNBOUND`.

**FR-P17-31 — Lead magnets and landing pages.** Registry of LM-01–LM-10 with owner, gate type, claim keys and consent purposes; core tool results never email-gated (P13 §4E); landing pages are P13 CMS documents using the FR-P13-V3-Y01 block library and must link to a campaign code; orphan check (MA-24) after campaign end. *Acceptance:* a landing page without an `OperatorFooter` or campaign link cannot publish; a page 31 days past its campaign end is flagged for redirect or unpublish.

**FR-P17-32 — Nurture sequences.** Sequence builder over the Appendix X automation engine with versioned sequences NS-LEN … NS-REE (Appendix Y §Y.7.4), step content as approved content versions, entry and exit conditions (meeting booked, opportunity created, reply, unsubscribe, case filed by the contact), caps and suppression checked at each step; each sequence version approved by marketing + legal (R3 for NS-IND). *Acceptance:* a contact who books a meeting exits NS-LEN before the next step; NS-IND cannot exceed 3 touches in 14 days; editing a step creates a new sequence version requiring approval.

**FR-P17-33 — Webinars and events.** Event records (type, mode, capacity, revenue stream for paid tickets via the registry, sponsors with the App. O X-10 check, speakers with disclosures, photography notice, accessibility options, attendee retention); webinar funnel stages (registration, confirmation with calendar file, T-24 h/T-1 h reminders as service messages, live session via the workspace connector, recording labelled "Recorded on {date}", replay, survey, B2B offer); paid B2B webinars show total incl. GST, refund terms and BP-04 before payment. *Acceptance:* a replay page without the recorded-on label fails MT-22; a sponsor flagged as a repeat-player enterprise cannot be attached to a neutral CPD event.

**FR-P17-34 — Referral and partner programmes (D3-27; X-54).** Programmes RP-01–RP-05 with rules per Appendix Y §Y.7.5; professional-class checks at code creation, attribution and payout; RP-03 rewards locked; RP-04 disabled; reward approval by `finance_ops`; approved RP-01 rewards handed to P05 by Appendix X OA-20, which pays through `PAYOUT_PORT` with TDS (Income-tax Act 2025 s.393(1) Table Sl. 1(ii), 2%, ₹20,000 threshold) and GST invoice capture under `accounts_maker`/`accounts_checker` (NN-36); disclosure of the partner relationship on the referred tenant and to counterparties (NN-16). *Acceptance:* attempting to create a reward for a partner whose contact is flagged `professional_class = 'ca'` fails with `MKT_ADVOCATE_REWARD_BLOCKED`; a payout cannot be approved by the user who created the programme or the payee.

**FR-P17-35 — Training cross-sell gate.** All Institute promotions and equatoradr.com links are blocked while `academy.institute_referral` is OFF, and the flag cannot be ON until corrections C1–C20 (Appendix AF §AF.4.3, FR-P10-V3-AF01) are recorded as corrected; when ON, promotions must render ≥ 3 providers in seeded-random order, BP-05 disclosure and no empanelment or appointment language; never sent to parties in a case or to respondents; contact sharing with the Institute only under a consent purpose naming it; RS-22 referral fees stay OFF until s.188/s.184 records exist. *Acceptance:* with the flag OFF, an email containing an equatoradr.com link fails lint (SL-15 + flag check); with it ON, a promotion listing only the Institute fails.

**FR-P17-36 — Marketing automation catalogue and approval nodes.** Implement MA-01–MA-32 (Appendix Y §Y.7.8; MA-30 retired in favour of Appendix X OA-11) as versioned Appendix X workflows with the eight required attributes (trigger, action, data, permissions, exception, audit, stop, owner); marketing pause `tenant.mkt.automation.global_pause` (Appendix X `tenant.ops.automation.global_pause` stops all) and crisis pause (MA-21); the engine refuses to activate a workflow whose actions include public publishing, price change, testimonial publication, targeting change or mass send without an approval node matching the §Y.7.9 matrix (`OPS_AUTOMATION_APPROVAL_REQUIRED`, the Appendix X engine code); locked automations (MA-01, MA-02, MA-07, MA-13, MA-19, MA-21, MA-31) cannot be disabled by tenants. *Acceptance:* a draft workflow "on webinar end, post attendee count to LinkedIn" cannot be activated without an approval node; disabling MA-02 is refused with the L-tier reason.

**FR-P17-37 — Targeting rules and audiences.** Audience builder limited to allowed attributes (Appendix Y §Y.7.10); prohibited attributes and lookalikes rejected (`MKT_SENSITIVE_TARGETING_BLOCKED`); individual-facing paid ads require R3, SignpostCard landing pages and non-impersonation copy; competitor brand bidding OFF; B2B ad audiences exported only as firmographic definitions or consented contact lists (never respondents). *Acceptance:* an audience rule "health insurance claim rejected in last 90 days" is rejected; an ad set targeting "RBI Ombudsman" keywords cannot be approved unless its landing page includes the SignpostCard and the copy passes LINT-003.

### 4H. PR, crisis and partnerships

**FR-P17-38 — Media list, releases and coverage.** Media contacts with basis and source (Appendix Y §Y.8.1), opt-outs honoured group-wide; press-release workflow with fact-check, legal, Company Secretary (topic-based), CEO approval, embargo enforcement (`MKT_EMBARGO_ACTIVE`) and distribution receipt; BP-01 mandatory; spokesperson register; coverage log with type labelling and correction requests. *Acceptance:* a release scheduled for 09:00 embargo cannot be distributed at 08:59; a release containing a number outside a claim node fails lint; paid coverage cannot be tagged "earned".

**FR-P17-39 — Crisis room.** Crisis incidents C1–C4 per Appendix Y §Y.8.4 with lead, team, timeline, holding-statement clocks (C1 2 h, C2 4 h), statement bank and approvals, automatic pause of scheduled posts and sends at C1/C2 (MA-21), dark-site page publication through the P13 CMS with legal approval, links to the DPDP breach and CERT-In workflows (Appendix Q) without duplicating them, impersonation playbook tasks (pinned notice, platform takedown requests, cybercrime.gov.in report), and post-incident review. *Acceptance:* opening a C1 incident pauses every scheduled item and send within 1 minute and starts the 2-hour holding-statement clock; resuming requires the crisis lead.

**FR-P17-40 — Partnerships, MoUs and obligations.** Partner types and rules (Appendix Y §Y.9.1), the Appendix X `partnership` pipeline (no separate marketing pipeline), MoU templates with the mandatory clauses (no role in neutral selection, no case data, publicity clause, data protection, non-exclusivity, anti-bribery, no fee-sharing with advocates), legal review gate (`MKT_MOU_LEGAL_REVIEW_REQUIRED`), approval by authorised signatory through `ctl`, obligations tracker with MA-18 reminders, joint events and co-branding linkage; any public mention of a partner requires a signed instrument with a publicity clause. *Acceptance:* an MoU without the "no role in selecting neutrals" clause cannot leave `legal_review`; a social post naming a partner whose MoU is unsigned fails approval.

### 4I. SEO and GEO planning

**FR-P17-41 — SEO/GEO planner.** Intent clusters (seeded from App. P §6.13), briefs with answer-first drafts, citations, internal links, author and legal reviewer; programmatic governance register mirroring P13 templates and kill switches; AI-visibility backlog from FR-P13-V2-17 runs (MA-25); monthly SEO report from growth data only. Briefs hand off to the P13 CMS as draft pages. *Acceptance:* creating a programmatic brief for a POSH subtype is refused (App. P §6.7 exclusions); a backlog item links to the panel run that produced it.

### 4J. Analytics, attribution and contribution

**FR-P17-42 — Touchpoints and attribution.** Collect touchpoints from consented analytics events, executor events, event attendance, referrals and CRM activities; model registry (first, last non-direct, position-based 40/20/40 default, linear, time-decay) with maker-checker approval (`marketing_manager` + `finance_ops`); nightly attribution (MA-22); published monthly snapshots never overwritten by a model change (comparison report instead). *Acceptance:* changing the default model to linear from 1 March does not alter the January and February snapshots; selecting an unapproved model for a published report fails with `MKT_ATTRIBUTION_MODEL_UNAPPROVED`.

**FR-P17-43 — Dashboards D-01–D-12.** Build the dashboards of Appendix Y §Y.11.4 on the reporting read model; k ≥ 10 for any SEG-IND cell; group sharing only under NN-38 grants (time-limited, purpose-bound); export of dashboard data as XLSX/CSV with a README sheet. *Acceptance:* a cell with 7 individuals renders "< 10"; a Finbyx user without a grant cannot open Equator's D-10.

**FR-P17-44 — Economics.** CAC (fully loaded), LTV (recurring and transactional), LTV:CAC, payback, campaign ROI and budget variance per the Appendix Y §Y.11.3 formulas; staff cost enters only as cost-centre totals from HR/finance; spend net of eligible input tax credit as recorded by finance. *Acceptance:* a fixture month reproduces the expected CAC and LTV values to the rupee; no individual salary is queryable from `mkt`.

**FR-P17-45 — Contribution metrics feed (Appendix Z).** Monthly snapshot (MA-23) of role metrics per Appendix Y §Y.11.7 with sources; context metrics capped at the configured weight; prohibited inputs blocked at schema level; employee view (SCR-P17-26) with sources and a "dispute" action that opens an Appendix Z dispute record; snapshot approved by `marketing_manager` before publication to Appendix Z. *Acceptance:* the feed schema rejects a metric `online_hours`; an employee's dispute freezes the disputed metric value in Appendix Z until resolved.

### 4K. Exports and migration

**FR-P17-46 — Marketing workspace export (NN-37, D3-07, D3-41).** Request an `OPS_DEPARTMENT` export (Appendix AC §AC.13.3) through the P21 export service; the package follows the Appendix AC taxonomy as placed for marketing in Appendix Y §Y.18 (`06_Marketing/` subfolders; `00_README.pdf`/`.html`, `00_Contents.xlsx`, `99_Manifest/` with manifest CSV + JSON and SHA-256), Office formats, root ≤ 40 and paths below root ≤ 140 characters (AC §AC.13.7); contact-level consent artefacts only in a DPO-scoped export; exports of personal data are maker-checker. *Acceptance:* the export validates against the D3-07 validator; every file in the manifest hash-matches; the longest path is under the configured limit.

**FR-P17-47 — Migration in and out.** Importers for Brevo (contacts with consent evidence, lists, campaign statistics), Adobe Express (asset exports with rights metadata entered by the designer), HubSpot/Zoho marketing data via Appendix X; annual migration rehearsal MA-32 from Brevo to `ses_marketing` in staging with count comparison; rehearsal report stored as audit evidence (NN-40). *Acceptance:* the rehearsal sends to the seed list through the fallback with identical suppression counts; an import file lacking consent evidence for any row is rejected row by row with a downloadable error report.

---

## 5. Workflows and state machines

### 5.1 Content item

| From | Event | To | Guard / side effect |
|---|---|---|---|
| `idea` | Brief attached | `briefed` | Campaign and channel set |
| `briefed` | Draft saved | `drafting` | — |
| `drafting` | Submit | `brand_review` | Lint B-rules pass; alt text, captions; claims resolved; UTM valid |
| `brand_review` | Approve | `compliance_review` or `approved` | R0/R1 go to `approved` (sampling queue for R0/R1) |
| `brand_review` / `compliance_review` | Request changes | `drafting` | Reason required |
| `compliance_review` | Approve | `approved` | R2: legal; R3: legal + compliance (or ops director for crisis); reviewer ≠ author |
| `approved` | System | `handoff_ready` | Hash frozen; hand-off package generated |
| `handoff_ready` | Schedule | `scheduled` | Inside validity window; adapter or manual route chosen; no crisis pause |
| `scheduled` | Publish confirmed / adapter success | `published` | Evidence captured |
| `scheduled` | Scheduled time + 24 h without evidence | `evidence_overdue` | MA-08 |
| `evidence_overdue` | Evidence recorded | `published` | Late flag kept |
| `published` | +7 days (default) | `tracking` | Metrics pull |
| `tracking` | Campaign closed | `archived` | — |
| any pre-publish | Claim expired / flag OFF / rights expired / crisis / kill switch | `held` | Owner notified; resume requires re-check; content change → new version |
| `published`, `tracking` | Take down | `taken_down` | Reason; SLA; removal evidence |

### 5.2 Campaign

`draft → in_review → approved → scheduled → live ⇄ paused → completed → closed | cancelled`. Guards: approval requires budget approval per authority matrix; `live → paused` automatic on the FR-P17-07 triggers; `completed → closed` requires a results record.

### 5.3 Marketing send

`draft → content_locked → audience_snapshotted → test_sent → awaiting_approval (if mass/SEG-IND) → approved → queued → dispatching → completed | paused_deliverability | cancelled`. At `queued` and again per batch at dispatch: consent, suppression, frequency cap, quiet hours, sender-domain check; skipped recipients logged by reason. `paused_deliverability` resumes only by `marketing_manager` + `it_admin` after review.

### 5.4 Crisis incident

`opened (level set) → holding_statement_due → holding_statement_published → managing → resolved → review_due → closed`. Level changes are logged; C1/C2 apply the global pause on `opened`; `resolved` requires the crisis lead; `closed` requires the post-incident review record.

### 5.5 Partnership and MoU

Stages up to `active` are the Appendix X `partnership` pipeline (`identified → researched → contacted → exploring → proposal → term_sheet → legal_review → approval → mou_signed → active`, `ops.crm_stages`); the MoU record (`mkt.mous`) then runs `active → renewal_due → renewed | expired | terminated`. `legal_review → approval` requires mandatory clauses present; `approval → mou_signed` requires the authorised signatory per `ctl`; `active` enables publicity only where the publicity clause permits.

### 5.6 Referral reward

`pending (attributed) → eligibility_check → approved | blocked → payable → paid | reversed`. `eligibility_check` re-verifies professional class, programme status, partner agreement, KYB and disclosure; `blocked` emits `equator.mkt.referral.reward_blocked.v1`; `approved` requires `finance_ops` (≠ creator, ≠ payee owner); `reversed` on refund or cancellation within the clawback window in the agreement.

### 5.7 Asset rights

`draft → rights_pending → active → expiring (T-30) → expired | renewed`; `active → withdrawn` on consent withdrawal (immediate hold and takedown tasks).

---

## 6. Screens and UX (web + mobile)

All screens are in `apps/ops` (responsive web, WCAG 2.2 AA, en and hi UI). The mobile app exposes only approvals, engagement triage and publication-evidence capture for ops roles (P12 parity rules apply to those three flows).

| ID | Route (`/ops/mkt/...`) | Roles | Purpose and key elements |
|---|---|---|---|
| SCR-P17-01 | `/` | All marketing roles | Home (D-01): OKR progress, items due for review, held items, evidence overdue, sends awaiting approval, crisis banner |
| SCR-P17-02 | `/strategy/okrs` | Marketing manager, dept head | Objectives and key results; metric picker from the dictionary; quarterly close |
| SCR-P17-03 | `/strategy/market-segments` | Marketing manager | Market-segment catalogue (SEG-*) with locked restrictions shown as read-only chips; ICP criteria |
| SCR-P17-04 | `/strategy/messaging` | Marketing manager, legal | Messaging houses: roof, pillars with claim chips (status, expiry), never-say, approval panel |
| SCR-P17-05 | `/campaigns` | Marketing roles | Board and list by state; filters; budget burn bars |
| SCR-P17-06 | `/campaigns/{id}` | Campaign team, finance | Brief, channels, timeline, budget lines and spend, UTM set, experiments, results; approval timeline |
| SCR-P17-07 | `/calendar` | Marketing roles | Month/week/list calendar by channel and account; colour by status; risk-tier badges; drag to reschedule (re-validates window) |
| SCR-P17-08 | `/content/{id}` | Authors, reviewers | Item editor per channel and locale with live lint panel, claim and boilerplate inserts, AI draft panel (labelled), asset picker (rights status), version history and diff, review checklist, **hand-off package** tab with ZIP download |
| SCR-P17-09 | `/reviews` | Brand and compliance reviewers | Queues by tier; sampling queue; side-by-side diff; checklist; decision with reason |
| SCR-P17-10 | `/publications` | Social exec, marketing manager, compliance | Evidence capture (URL, time, screenshot upload, attestation); overdue list; monthly sample verification |
| SCR-P17-11 | `/social/accounts` | Marketing manager, IT admin | Accounts, admin roster, MFA attestation, adapter status and access-tier evidence, counters |
| SCR-P17-12 | `/social/inbox` | Social exec, PR | Engagement inbox: category proposals, confirm and route, response bank, SLA timers, safety escalation button |
| SCR-P17-13 | `/brand/assets` | Designer, marketing | DAM grid with rights badges (active, expiring, expired, consent withdrawn) |
| SCR-P17-14 | `/brand/assets/{id}` | Designer, DPO | Versions, rights records, consent records, usages, expiry actions |
| SCR-P17-15 | `/brand/boilerplates` | Marketing, legal | Boilerplate register and co-branding approvals |
| SCR-P17-16 | `/messaging/audiences` | Marketing manager, compliance, DPO | Audience builder (allowed attributes only), sensitive approval, snapshot counts by suppression reason |
| SCR-P17-17 | `/messaging/sends` | Marketing roles | Compose (approved content only), test send, approval screen (§4F FR-P17-29), dispatch report |
| SCR-P17-18 | `/messaging/consent` | DPO | Consent-mirror read health (Appendix X), send holds, propagation latency, executor reconciliation, suppression lists, DSR propagation log |
| SCR-P17-19 | `/messaging/deliverability` | IT admin, marketing manager | Sender domains, SPF/DKIM/DMARC status, DMARC report summary, complaint and bounce trends |
| SCR-P17-20 | `/growth/magnets` | Marketing | Lead magnets and landing-page registry (links to CMS), orphan flags |
| SCR-P17-21 | `/growth/sequences` | Marketing, legal | Sequences and automations: versions, steps, approval nodes, kill switches, locked automations marked |
| SCR-P17-22 | `/growth/events` | Event owners | Events and webinars: capacity, registrations, sponsors check, speakers' disclosures, recordings |
| SCR-P17-23 | `/growth/referrals` | Partnerships, finance | Programmes, codes, pending rewards, blocked rewards with reasons, payouts |
| SCR-P17-24 | `/pr` | PR manager, legal, CS | Media list, releases with approvals and embargo, coverage log, spokespersons |
| SCR-P17-25 | `/pr/crisis/{id}` | Crisis team | Crisis room: level, clocks, statement bank, approvals, pause status, linked statutory workflows, tasks |
| SCR-P17-26 | `/me/contribution` | Employee (own), manager | Own contribution metrics with sources, context-weight note, dispute action |
| SCR-P17-27 | `/partners` | Partnerships, legal | MoU detail with clause checklist, obligations calendar, joint events (the pipeline board is Appendix X `/crm/pipeline` for pipeline `partnership`) |
| SCR-P17-28 | `/seo` | SEO lead, content | Intent clusters, briefs, programmatic governance, AI-visibility backlog |
| SCR-P17-29 | `/analytics` | Marketing, finance, leadership | D-02–D-12, attribution model registry and comparison reports, economics |
| SCR-P17-30 | `/settings` | Per tier | Marketing settings with tier badges, pending G-tier approvals, history and rollback |
| SCR-P17-31 | mobile `ops://mkt/approvals`, `/inbox`, `/evidence` | Reviewers, social exec | Approve/reject with checklist; triage; camera-roll screenshot upload for evidence |

UX rules: every blocking error shows the rule ID and a plain explanation (App. P §4.6 style); claim chips show expiry; AI-drafted text is visibly labelled until edited and approved; no upgrade or cross-sell prompts appear in any case-related view (App. O X-15).

---

## 7. Backend design

### 7.1 Modules

NestJS bounded context `mkt` in `apps/api` with modules `mkt-strategy`, `mkt-campaigns`, `mkt-content`, `mkt-social`, `mkt-brand`, `mkt-messaging`, `mkt-growth`, `mkt-pr`, `mkt-partners`, `mkt-seo`, `mkt-analytics` (Appendix Y §Y.1.1), plus shared packages: `packages/content-lint` (LINT, SL and MT profiles; shared with P13), `packages/mkt-domain` (types, state machines, validators), `packages/integrations/social` (`SOCIAL_PORT`), `packages/integrations/marketing` (`MARKETING_PORT`). Workflows run on the Appendix X automation engine (Temporal). Authorisation: Cerbos/OPA policies per permission bundle (Appendix Y §Y.13) with company scope; RLS on `company_id`.

### 7.2 Tables (key columns; schema `mkt`)

Common columns on every table: `id uuid PK DEFAULT uuidv7()`, `company_id uuid NOT NULL` (RLS), `created_at`, `created_by`, `updated_at`, `version int`, `status text`. Money: `amount_minor bigint` + `currency char(3)`.

| Table | Key columns |
|---|---|
| `market_segments`, `icp_profiles` | `code`, `name`, `track` (A/B/C), `restrictions jsonb` (locked), `fit_criteria jsonb` |
| `messaging_houses`, `messaging_pillars` | `segment_id`, `roof_text_by_locale jsonb`, `approved_by`; pillar `headline_by_locale`, `claim_keys text[] CHECK (cardinality(claim_keys) > 0)`, `never_say jsonb` |
| `objectives`, `key_results` | `period`, `owner_id`, `approver_id` (≠ owner); `metric_key` FK `metric_definitions`, `baseline`, `target`, `direction` |
| `campaigns`, `campaign_channels` | `code`, `key_result_id`, `segment_ids uuid[]`, `messaging_house_version_id`, `offer_type`, `offer_ref`, `stream_code` (REFERENCES `rev.streams(code)`, Appendix AB), `audience_id`, `attribution_model_id`, `risk_floor`, `paused_reason` |
| `budgets`, `budget_lines`, `spend_entries` | `amount_minor`, `gst_treatment`, `approval_chain jsonb`; line `cost_type`, `channel`; spend `invoice_ref`, `payee_ref` (from `ctl`), `paid_partnership bool` |
| `utm_links` | `campaign_id`, `content_item_id`, `source`, `medium`, `utm_campaign`, `utm_content`, `utm_term`, `target_url`, `short_url`, `qr_object_key` |
| `experiments`, `experiment_variants` | `hypothesis`, `primary_metric_key`, `mde`, `alpha`, `power`, `min_sample`, `surface`, `p13_experiment_id`, `decision`; variant `content_version_id`, `allocation_pct` |
| `content_items`, `content_versions` | `type`, `channel`, `social_account_id`, `campaign_id`, `cms_page_version_id`, `risk_tier_computed`, `risk_tier_effective`, `scheduled_at`, `valid_until`; version `body jsonb`, `approved_hash char(64)`, `ai_generated`, `synthetic_media`, `prompt_version_id` |
| `content_reviews` | `content_version_id`, `stage`, `reviewer_id`, `checklist jsonb`, `decision`, `reason` |
| `content_claim_refs` | `content_version_id`, `claim_key`, `claim_status_at_approval`, `claim_expires_at` |
| `handoff_packages` | `content_version_id`, `design_link`, `assets jsonb` (id, sha256), `captions jsonb`, `alt_texts jsonb`, `captions_file_key`, `zip_object_key` |
| `publications` | see DDL below |
| `social_accounts`, `social_adapter_state` | `platform`, `handle`, `owner_id`, `admins jsonb`, `mfa_attested_at`; `adapter`, `access_tier`, `grant_evidence_key`, `daily_counter`, `monthly_spend_usd_minor` |
| `engagement_items` | `platform`, `external_ref`, `category`, `confidence`, `confirmed_by`, `routed_ref`, `routed_type`, `first_response_at`, `content_enc bytea`, `content_purge_at` |
| `assets`, `asset_versions`, `asset_rights`, `asset_consents`, `asset_usages` | `class`, `tags`; version `s3_key`, `sha256`; rights `licence_type`, `licensor`, `expires_at`, `evidence_key`; consent `person_ref`, `scope jsonb`, `notice_version`, `withdrawn_at`; usage `content_version_id` |
| `boilerplates`, `cobrand_approvals` | `code`, `text_by_locale`, `approved_version`; `partner_ref`, `asset_id`, `scope`, `expires_at`, `evidence_key`, `approver_id` |
| `audiences`, `audience_snapshots` | `definition jsonb`, `sensitive bool`, `approvals jsonb`; snapshot `counts jsonb` (by suppression reason), `members_object_key` (hashes), `frozen_at` |
| `sends`, `send_approvals` | see DDL below |
| `suppressions` | see DDL below |
| `frequency_counters` | `contact_hash`, `channel`, `window_start date`, `count int` |
| `sender_domains` | `domain`, `executor`, `spf_ok`, `dkim_ok`, `dmarc_policy`, `alignment_ok`, `last_checked_at` |
| `lead_magnets`, `landing_pages` | `code`, `gate_type`, `claim_keys`, `consent_purposes`; `cms_page_id`, `campaign_id`, `page_tags text[]`, `orphan_since` |
| `sequences`, `sequence_steps` | `segment_id`, `version`, `x_workflow_id`, `approvals jsonb`, `max_touches`, `window_days`; step `order`, `channel`, `delay_hours`, `content_version_id`, `exit_conditions jsonb` |
| `events`, `event_registrations` | `type`, `mode`, `starts_at`, `capacity`, `stream_code` (REFERENCES `rev.streams(code)`), `sponsors jsonb`, `speakers jsonb`, `recording_label`; registration `contact_ref`, `consent_refs uuid[]`, `attended` |
| `referral_programmes`, `referral_codes`, `referral_rewards` | see DDL below |
| `media_contacts`, `press_releases`, `coverage_items`, `spokespersons` | `basis`, `source_url`, `source_date`, `opt_out_at`; release `embargo_at`, `approvals jsonb`, `distributed_at`; coverage `url`, `coverage_type`, `accuracy`, `correction_requested`; spokesperson `topics`, `languages`, `trained_at` |
| `crisis_incidents`, `crisis_statements` | `level`, `lead_id`, `opened_at`, `pause_applied_at`, `holding_due_at`, `linked_workflows jsonb`; statement `text_by_locale`, `approvals`, `published_at` |
| `partnerships`, `mous`, `mou_obligations`, `joint_events` | `type`, `crm_partner_ref`, `crm_opportunity_ref` (Appendix X, by value; the stage lives on the CRM opportunity), `participating_companies uuid[]`; MoU `template_version`, `clause_checklist jsonb`, `instrument_key`, `signatory_ref`, `publicity_clause bool`, `expires_at`; obligation `text`, `owner_side`, `due_at`, `recurrence`, `evidence_key` |
| `seo_intent_clusters`, `seo_briefs`, `programmatic_governance`, `ai_visibility_backlog` | Appendix Y §Y.10 fields |
| `touchpoints` | `contact_hash`, `account_ref`, `channel`, `utm jsonb`, `occurred_at`, `consent_ref`, `source`; partitioned monthly |
| `attribution_models`, `attribution_results` | `type`, `params jsonb`, `lookback jsonb`, `approved_by` (2), `effective_from`; result `opportunity_ref`, `model_id`, `touchpoint_id`, `credit numeric(6,5)` |
| `metric_definitions`, `metric_snapshots` | `key`, `formula`, `source`, `privacy_class`; snapshot `period`, `values jsonb`, `approved_by`, `published_at` |
| `contribution_metrics` | `employee_ref`, `period`, `metric_key`, `value`, `is_context bool`, `source_ref`, `disputed bool`; CHECK `metric_key` in the allowed role-metric list |

```sql
CREATE TABLE mkt.publications (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  company_id uuid NOT NULL,
  content_version_id uuid NOT NULL REFERENCES mkt.content_versions(id),
  route text NOT NULL CHECK (route IN ('adobe_scheduler','native_app','equator_social_port',
        'marketing_port','messaging_port','newswire','cms')),
  approved_hash char(64) NOT NULL,
  payload_hash char(64),                          -- API routes: must equal approved_hash
  post_url text, platform_post_id text,
  published_at timestamptz,
  screenshot_key text, screenshot_sha256 char(64), -- manual routes (S3 Object Lock)
  attested_by uuid, attested_at timestamptz,
  verification_status text NOT NULL DEFAULT 'pending'
     CHECK (verification_status IN ('pending','auto_verified','sample_verified','mismatch','not_sampled')),
  CHECK (route NOT IN ('adobe_scheduler','native_app') OR published_at IS NULL
         OR (post_url IS NOT NULL AND screenshot_sha256 IS NOT NULL AND attested_by IS NOT NULL)),
  CHECK (route <> 'equator_social_port' OR payload_hash IS NULL OR payload_hash = approved_hash)
);

CREATE TABLE mkt.sends (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  company_id uuid NOT NULL,
  content_version_id uuid NOT NULL REFERENCES mkt.content_versions(id),
  audience_snapshot_id uuid NOT NULL REFERENCES mkt.audience_snapshots(id),
  channel text NOT NULL CHECK (channel IN ('email','sms','whatsapp')),
  port text NOT NULL CHECK (port IN ('marketing_port','messaging_port')),
  executor text NOT NULL,                          -- brevo | ses_marketing | msg91 | gupshup
  purpose text NOT NULL,                           -- consent purpose used
  sender_domain_id uuid REFERENCES mkt.sender_domains(id),
  recipient_count int NOT NULL, mass boolean NOT NULL,
  created_by uuid NOT NULL, approved_by uuid,
  status text NOT NULL,
  CHECK (NOT mass OR status NOT IN ('approved','queued','dispatching','completed') OR approved_by IS NOT NULL),
  CHECK (approved_by IS NULL OR approved_by <> created_by),
  CHECK (channel <> 'email' OR sender_domain_id IS NOT NULL)
);

CREATE TABLE mkt.suppressions (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  company_id uuid,                                 -- NULL = applies to every company (respondent, legal hold)
  contact_hash text NOT NULL,                      -- HMAC-SHA256 with the growth key (FR-P13-26(c))
  reason text NOT NULL CHECK (reason IN ('respondent','withdrawn','hard_bounce','soft_bounce','complaint',
        'dnd','minor','legal_hold','dsr_erasure','inactive','role_address','pending_verification')),
                                                   -- 'respondent' rows are a send-time copy of growth.suppression_hashes (P13 is SoR)
  channel_scope text[] NOT NULL DEFAULT '{email,sms,whatsapp,ads}',
  expires_at timestamptz,                          -- only soft_bounce, inactive and pending_verification may expire
  source text NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (reason IN ('soft_bounce','inactive','pending_verification') OR expires_at IS NULL)
);

CREATE TABLE mkt.referral_rewards (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  company_id uuid NOT NULL,
  programme_id uuid NOT NULL REFERENCES mkt.referral_programmes(id),
  code_id uuid NOT NULL REFERENCES mkt.referral_codes(id),
  payee_ref uuid NOT NULL,                         -- ctl payee
  professional_class text CHECK (professional_class IN ('advocate','ca','cs','cma')),
  reward_type text NOT NULL CHECK (reward_type IN ('revenue_share','service_credit')),
  amount_minor bigint NOT NULL, currency char(3) NOT NULL DEFAULT 'INR',
  tds_minor bigint, gst_invoice_ref text,
  status text NOT NULL CHECK (status IN ('pending','eligibility_check','approved','blocked','payable','paid','reversed')),
  approved_by uuid, created_by uuid NOT NULL,
  CHECK (professional_class IS NULL OR status IN ('blocked','reversed')),
  CHECK (approved_by IS NULL OR approved_by <> created_by)
);
```

### 7.3 APIs (`/v1/ops/mkt`; OpenAPI 3.1; `Equator-Context`; Idempotency-Key required where marked)

| Method / path | Purpose | Permission | Idempotency |
|---|---|---|---|
| CRUD `/objectives`, `/key-results`; POST `/objectives/{id}/close` | OKRs | `mkt.strategy.*` | keyed |
| CRUD `/market-segments`, `/icp-profiles`, `/messaging-houses`; POST `/messaging-houses/{id}/{submit,approve}` | Strategy | `mkt.strategy.*` | keyed |
| CRUD `/campaigns`; POST `/campaigns/{id}/{submit,approve,schedule,pause,resume,complete,close,cancel}` | Campaigns | `mkt.campaign.*` | keyed |
| CRUD `/budgets`, `/budget-lines`; POST `/budgets/{id}/approve`; POST `/spend-entries` | Budgets and spend | `mkt.campaign.*`; finance | **required** |
| POST `/utm-links`; GET `/utm-links?campaign=` | Link builder | `mkt.campaign.write` | keyed |
| CRUD `/experiments`; POST `/experiments/{id}/{start,stop,decide}` | Experiments | `mkt.campaign.*` | keyed |
| CRUD `/content-items`; POST `/content-items/{id}/versions`; POST `/content-versions/{id}/{submit,brand-approve,compliance-approve,request-changes,schedule,confirm-publication,take-down}` | Calendar and review | `mkt.content.*` | **required** on approve/confirm/take-down |
| GET `/content-versions/{id}/lint`; GET `/content-versions/{id}/handoff` (JSON or ZIP) | Lint report; hand-off package | `mkt.content.draft` | — |
| CRUD `/social-accounts`; POST `/social-adapters/{adapter}/{enable,disable}` | Accounts and adapters | `mkt.settings.G` (maker `marketing_manager`, checker `legal_reviewer`); `it_admin` security review on file | **required** |
| GET/POST `/engagement-items`; POST `/engagement-items/{id}/{confirm-category,route,respond}` | Inbox | `mkt.engagement.triage` | keyed |
| CRUD `/assets`, `/assets/{id}/versions`, `/assets/{id}/rights`, `/assets/{id}/consents`; POST `/asset-consents/{id}/withdraw` | DAM | `mkt.asset.*`; DPO for consents | keyed |
| CRUD `/boilerplates`, `/cobrand-approvals` | Brand | `mkt.asset.manage`; legal | keyed |
| CRUD `/audiences`; POST `/audiences/{id}/{approve-sensitive,snapshot}` | Audiences | `mkt.audience.*` | keyed |
| CRUD `/sends`; POST `/sends/{id}/{test,submit,approve,dispatch,cancel}`; GET `/sends/{id}/report` | Sends | `mkt.send.*` | **required** |
| GET `/consent-status?contact=` (reads `ops.crm_marketing_view`); GET `/suppressions/stats`; POST `/suppressions` (DPO) | Consent and suppression | DPO; read for marketing (counts only) | keyed |
| GET `/sender-domains`; POST `/sender-domains/{id}/check` | Deliverability | `it_admin` | — |
| CRUD `/lead-magnets`, `/landing-pages`, `/sequences`, `/sequence-steps`; POST `/sequences/{id}/{submit,approve,activate,pause}` | Growth | `mkt.content.*`; legal | keyed |
| CRUD `/events`, `/event-registrations` | Events | `mkt.campaign.write` | keyed |
| CRUD `/referral-programmes`, `/referral-codes`; GET `/referral-rewards`; POST `/referral-rewards/{id}/{approve,reverse}` | Referrals | `mkt.partner.*`; finance | **required** on approve |
| CRUD `/media-contacts`, `/press-releases`, `/coverage-items`, `/spokespersons`; POST `/press-releases/{id}/{approve,distribute}` | PR | `mkt.pr.*` | **required** on distribute |
| CRUD `/crisis-incidents`; POST `/crisis-incidents/{id}/{set-level,pause,resume,resolve,close}`; CRUD `/crisis-incidents/{id}/statements` | Crisis | crisis team | **required** |
| CRUD `/partnerships`, `/mous`, `/mou-obligations`, `/joint-events`; POST `/mous/{id}/{submit-legal,approve,sign}` | Partnerships | `mkt.partner.*`; legal; `ctl` signatory | **required** on approve/sign |
| CRUD `/seo/clusters`, `/seo/briefs`; GET `/seo/programmatic`, `/seo/ai-visibility` | SEO/GEO | `mkt.content.*` | keyed |
| CRUD `/attribution-models`; POST `/attribution-models/{id}/approve`; GET `/dashboards/{code}`; GET `/economics?segment=&period=` | Analytics | `mkt.analytics.view`; approvals | keyed |
| GET `/me/contribution`; POST `/me/contribution/{metric}/dispute` | Contribution (employee) | `employee` (own) | keyed |
| POST `/exports`; GET `/exports/{id}` | Exports | `marketing_manager` + checker for personal data | **required** |
| POST `/webhooks/social/{adapter}` (Brevo events arrive at the Appendix X `/webhooks/brevo` ingress and reach `mkt` through the outbox) | Executor events | platform signature where offered | event ID dedupe |

### 7.4 Events

Produced: the `equator.mkt.*` set in Appendix Y §Y.16 (CloudEvents, payloads carry IDs and counts only). Consumed: `equator.notices.respondent.served.v1` (hash only), `equator.consent.consent.withdrawn.v1`, `equator.consent.consent.given.v1` (P01), `equator.cms.page.published.v1`, `equator.cms.page.unpublished.v1`, `equator.cms.claim.expired.v1`, `equator.rev.stream.killed.v1`, `equator.rev.stream.status_changed.v1` (Appendix AB), `equator.cfg.setting.changed.v1` (Appendix V), `equator.ops.connector.engagement_received.v1` and `equator.ops.opportunity.{stage_changed,won,lost,closed}.v1` (Appendix X), Appendix Z dispute-resolved events.

### 7.5 Jobs and Temporal workflows

`ContentApprovalWorkflow` (per version; human signals) · `ScheduledPublishWorkflow` (adapter publish or manual hand-off task; evidence timer) · `EvidenceChaseJob` (hourly) · `ClaimHoldJob` (event-driven + hourly sweep) · `AssetRightsExpiryJob` (daily) · `ConsentPropagationWorkflow` (event-driven; SLA monitor 15 min) · `ExecutorReconciliationJob` (daily per executor) · `SendDispatchWorkflow` (batching, checks per batch, deliverability guard) · `SenderDomainCheckJob` (daily) · `SunsetJob` (weekly) · `SequenceRunner` (Appendix X engine) · `EngagementIngestJob` (every 15 min per enabled read adapter) · `EngagementPurgeJob` (daily) · `BudgetGuardJob` (hourly) · `ReferralEligibilityWorkflow` · `PartnerObligationJob` (daily) · `CrisisPauseWorkflow` (event-driven) · `AttributionJob` (nightly) · `MetricsSnapshotWorkflow` (monthly; approval signal) · `ContributionFeedWorkflow` (monthly → Appendix Z) · `LandingOrphanJob` (daily) · `MigrationRehearsalWorkflow` (annual) · `ExportWorkflow` (on request).

---

## 8. Integrations (ports and adapters)

| Need | Port / adapter | Default | Gate | Failure behaviour |
|---|---|---|---|---|
| Marketing email | `MARKETING_PORT` → `brevo`, `ses_marketing` | `ses_marketing` until `mkt.brevo.enabled` | Brevo DPA, sub-processor list, transfer-register row `BREVO_EU` (EU hosting [RD] F3.1) | Queue + retry; switch to fallback by setting; never bypass consent |
| Promotional SMS, WhatsApp marketing | `MESSAGING_PORT` → `msg91`, `gupshup` (P07) | MSG91 (SMS), Gupshup (WhatsApp) | DLT promotional templates; Meta marketing templates | Per P07 fallback; skipped recipients logged |
| Brevo SMS/WhatsApp | `MARKETING_PORT` → `brevo` | OFF | Written DLT support confirmation | — |
| CRM sync | `CRM_PORT` (Appendix X) | Per Appendix X | — | Appendix X rules |
| Social publishing and reads | `SOCIAL_PORT` → `linkedin_cm`, `meta_graph`, `x_v2`, `youtube_data`, `manual_handoff` | `manual_handoff` | Access grant evidence per platform; security review | Fallback to manual hand-off task |
| Design | Adobe Express (manual) ; Embed SDK | Manual export/upload | `mkt.adobe_embed.enabled` after Adobe review | Manual route |
| Meetings/webinars | Workspace connector (D3-04; Microsoft Teams) | Teams | SKU features confirmed | Manual link entry |
| Payouts | Via P05 (`PAYOUT_PORT`: RazorpayX/Cashfree Payouts) after the Appendix X OA-20 hand-off | P05 default | Reward approval by `finance_ops`; P05 maker-checker | Per P05 (manual NEFT with maker-checker) |
| Analytics | `ANALYTICS_PORT` (PostHog self-hosted, GA4) | PostHog | Consent | Drop events, never block |
| Ad platforms (spend/results read) | `ADS_PORT` (new; read-only) | OFF (MA-29) | Platform API access | Manual spend entry |
| Newswire / media distribution | `PR_DISTRIBUTION_PORT` (new; email default) | Email to media list | — | Manual |
| Short links and QR | Internal service on Equator domain | ON when domain registered | Domain registration | Full UTM link |
| Translation drafts | `TRANSLATION_PORT` (P13) | Sarvam | Human translator review (NN-23) | Human translation |

Every adapter documents field mapping, rate limits, import/export and its migration path (NN-40); adapter credentials live in the secrets vault and are rotated per Appendix Q.

---

## 9. Configuration surface

All settings of Appendix Y §Y.12 are registered in the P15 configuration service with tier badges. Phase-specific seeds and editors:

| Item | Tier | Editor / checker | Default | Guardrail |
|---|---|---|---|---|
| Segment catalogue and restrictions | T (catalogue) / L (restrictions) | `marketing_manager` | Appendix Y §Y.2.2 | Restrictions read-only |
| Messaging houses | T with legal approval | `marketing_manager` / `legal_reviewer` | Seeds MH-* (draft) | Pillars need claims |
| Risk-tier rules | G | `marketing_manager` / `legal_reviewer` | §Y.4.3 | Floors cannot drop |
| Lint profiles (SL/MT severities) | G | `legal_reviewer` / `compliance_officer` | §Y.4.5, §Y.7.1 | † rules fixed |
| Authority-matrix budget limits | G (`ctl`) | `finance_ops` / `ops_director` | §Y.3.3 | — |
| Adapter flags | G | `marketing_manager` / `legal_reviewer` (Appendix AC §AC.17) | OFF | Access-grant evidence and `it_admin` security review required |
| Consent purposes per company | G | DPO / `legal_reviewer` | FR-P13-22 six purposes × companies | Itemised notice per language |
| Frequency caps, quiet hours, mass threshold | T/G | Per §Y.12 | §Y.6.5–§Y.6.6 | Bounds |
| Referral programme switches | G | `partnerships_manager` / `finance_ops` | RP-01, RP-02 ON | RP-03 rewards locked; RP-04 OFF |
| Attribution default model | G | `marketing_manager` / `finance_ops` | Position-based v1 | Approved versions |
| Crisis clocks | G | `ops_director` / `legal_reviewer` | 2 h / 4 h | Upper bounds |
| Contribution context-weight cap | G | `hr_manager` / `department_head` | 15% | ≤ 25% |

---

## 10. Security, privacy and audit

- **Isolation:** `mkt` in the isolated business database (Appendix X D3-20); no grants with core; outbox validator; `MarketingIngressGuard` (FR-P17-02); RLS by `company_id`; cross-company access only through `grp` grants (NN-38).
- **Identity:** `eq-portal-ops` with phishing-resistant MFA; step-up for approvals, adapter enablement, G-tier changes, exports and payout approvals.
- **Secrets:** adapter tokens, Brevo API keys and webhook bearer tokens in the vault; bearer tokens rotated ≤ 90 days; Brevo IP allow-list on ingress; no secrets in `mkt` tables or logs.
- **Social accounts:** owner of record, MFA attestation, business-manager roles instead of shared passwords, quarterly admin-roster review, removal within the leaver SLA (FR-P14-V3-Y04).
- **Personal data:** contact references are CRM IDs or HMAC hashes; engagement content encrypted (`content_enc`) and purged after the retention period; media contacts with recorded basis; DSR propagation (MA-31) to every executor; consent artefacts exportable to the DPO; retention per §Y.12.
- **Evidence:** screenshots, rights evidence and signed MoUs in S3 with Object Lock (compliance mode), SHA-256 in the audit chain (NN-22); evidence retention 8 years.
- **Audit (NN-22):** hash-chained events for every approval, override, tier raise, publication confirmation, takedown, send dispatch, audience snapshot, suppression and send-hold change, setting change, adapter flag change, payout approval, crisis action and MoU approval; `internal_auditor` read-only access.
- **Financial controls (NN-36):** budgets and payouts through `ctl`; maker ≠ checker; payee and bank-detail changes in the `ctl` workflow with cooling-off and out-of-band confirmation; exceptions reported monthly.
- **Content security:** no third-party ad scripts on Equator pages (DP-13); pixels only after consent and never on restricted tags; CSP and SRI per P13.
- **Workforce data (NN-35):** contribution metrics only from outcome and quality sources; no activity surveillance inputs; employee access and dispute.

---

## 11. AI touchpoints and guardrails

| Touchpoint | Agent (P11 addendum, Appendix Y §Y.20) | Guardrails |
|---|---|---|
| Caption, subject-line and variant drafts | `marketing_copy_assistant` | Inputs limited to messaging house, active claims, boilerplates, brief; output validator strips numbers, comparisons, legal effects and names not in inputs; O2 zero-tolerance classifiers (merits, outcome, regulator endorsement, superlatives, urgency); `ai_generated = true`; normal review tier; no egress without approval (NN-01 GX-7) |
| Engagement classification | `social_triage_classifier` | Proposes E1–E10 only; never replies; E4/E6/E7 to humans immediately; GX-5 handoff for distress; content not used for training |
| Alt text, captions, subtitles | `marketing_copy_assistant` (accessibility mode) | Suggestions only; human acceptance required for SL-06/SL-07 |
| Translation drafts | `translation_agent` | Human translator and legal review for legal content (NN-23); parity check |
| SEO briefs and answer-first drafts | `marketing_copy_assistant` (SEO mode) | Citations from the Legal Rules Register only; human author and legal reviewer (App. P §6.7) |
| Analytics narratives | `analytics_narrator` | Aggregates only (k ≥ 10); no case data; no neutral outcome framing |
| Image/video generation | (flag `mkt.ai.image_generation.enabled`, OFF) | No real or realistic people as customers, parties, neutrals or staff; no courts presented as real; no emblems; `synthetic_media = true` |

Gateway stage I3 is extended with an `mkt` context guard that rejects CRM personal data and any case data in prompts. Kill switch per agent; deterministic fallback is "no draft" (authors write manually).

---

## 12. Acceptance criteria (Gherkin)

```gherkin
Feature: Marketing, brand and growth automation (P17)

  Scenario: NN-17_claim_expiry_holds_scheduled_post
    Given a LinkedIn post scheduled for tomorrow uses claim "panel.count"
    When the claim expires today
    Then the post moves to "held" within 5 minutes
    And its owner is notified and the post cannot be scheduled until the claim is renewed or replaced

  Scenario: Maker cannot approve own content
    Given content_writer "A" drafted item CI-100
    When "A" calls brand-approve on CI-100
    Then the response is 403 "MKT_SELF_APPROVAL"

  Scenario: Risk tier floor cannot be lowered
    Given an Instagram caption mentions "RBI"
    Then the computed risk tier is "R2"
    When the brand reviewer sets the tier to "R1"
    Then the response is 409 "MKT_REVIEW_REQUIRED"

  Scenario: SL-01_case_identifier_blocks_submission
    Given a caption contains "EQR-FIN-2026-000123"
    When the author submits it
    Then the response is 422 "MKT_LINT_BLOCKED" with rule "SL-01"
    And no override option is offered

  Scenario: Adobe hand-off requires evidence within 24 hours
    Given item CI-200 was handed off for Adobe Content Scheduler at 10:00 on 2 March
    And no post URL or screenshot is recorded by 10:00 on 3 March
    Then CI-200 shows status "evidence_overdue"
    And the owner and the marketing_manager receive an alert

  Scenario: Social adapter disabled falls back to manual hand-off
    Given flag "mkt.social.meta_graph.enabled" is OFF
    When an approved Instagram item reaches its scheduled time
    Then a manual hand-off task is created for the social_media_executive
    And no API call is made to Meta

  Scenario: API payload must equal the approved hash
    Given flag "mkt.social.linkedin_cm.enabled" is ON in sandbox
    And the outgoing payload hash differs from the approved hash of the version
    Then the post is not sent
    And an incident "publication_hash_mismatch" is opened

  Scenario: NN-16_respondent_suppressed_in_every_executor
    Given a person was served as respondent in any case
    When a marketing audience containing their email and phone is snapshotted
    Then the snapshot excludes them with reason "respondent"
    And no Brevo, MSG91, Gupshup or ad-audience payload contains their identifiers

  Scenario: Brevo unsubscribe propagates and fails safe
    Given a contact unsubscribes in a Brevo campaign
    When the Brevo webhook arrives with a valid bearer token and the re-fetch API call times out
    Then the contact is placed on a send hold for every marketing channel within 15 minutes
    And no marketing message is sent to the contact while the hold is active
    And the consent withdrawal is recorded in core.consent_records when the retried re-fetch confirms it

  Scenario: Webhook without valid token changes nothing
    Given a POST to /webhooks/brevo with an invalid bearer token
    Then the response is 401 and the contact's consent state is unchanged

  Scenario: Frequency cap skips contact
    Given contact C received 4 marketing emails in the last 30 days
    When a newsletter is dispatched
    Then C is skipped and the send report lists C under "MKT_FREQUENCY_CAP"

  Scenario: Mass send needs a second approver
    Given a send to 5,000 recipients created by marketing_manager "M"
    When "M" tries to dispatch without another approval
    Then the response is 409 "MKT_MASS_SEND_APPROVAL_REQUIRED"

  Scenario: Unverified sender domain blocks sending
    Given the DKIM check for "news.equatorresolution.in" failed in the last 24 hours
    When any marketing email send is dispatched
    Then the response is 409 "MKT_SENDER_DOMAIN_UNVERIFIED"

  Scenario: D3-28_resetting_countdown_rejected
    Given a landing page CountdownBlock configured as "24 hours from first visit"
    When the editor saves the page
    Then the response is 422 "MKT_COUNTDOWN_NOT_FIXED"

  Scenario: Scarcity must be bound to capacity
    Given a webinar landing page shows "12 seats left"
    And the block is not bound to the event capacity record
    Then publish fails with "MKT_SCARCITY_UNBOUND"

  Scenario Outline: D3-27_no_referral_rewards_to_professionals
    Given a referral code owned by a partner whose contact has professional_class "<class>"
    When a referred business subscribes
    Then the reward is created with status "blocked"
    And the event "equator.mkt.referral.reward_blocked.v1" is emitted
    Examples:
      | class    |
      | advocate |
      | ca       |
      | cs       |
      | cma      |

  Scenario: Sensitive targeting blocked
    Given an audience rule "visited /disputes/family-and-property in the last 30 days"
    When the marketing_manager saves the audience
    Then the response is 403 "MKT_SENSITIVE_TARGETING_BLOCKED"

  Scenario: Case data rejected at ingress
    Given an event arrives for mkt with field "case_id"
    Then it is rejected with "MKT_CASE_DATA_REJECTED" and a security alert is raised

  Scenario: Crisis pause
    Given 14 items are scheduled and 2 sends are queued
    When the ops_director opens a crisis at level "C1"
    Then all 14 items move to "held" and both sends pause within 1 minute
    And a holding-statement clock of 2 hours starts

  Scenario: Embargo enforced
    Given a press release embargoed until 09:00 IST
    When distribution is requested at 08:59 IST
    Then the response is 409 "MKT_EMBARGO_ACTIVE"

  Scenario: MoU needs mandatory clauses and legal review
    Given an MoU draft without the "no role in selecting neutrals" clause
    When the partnerships_manager submits it for approval
    Then the response is 409 "MKT_MOU_LEGAL_REVIEW_REQUIRED"

  Scenario: Attribution model change does not restate history
    Given monthly snapshots for January and February are published under position_based v1
    When linear v1 is approved effective 1 March
    Then the January and February snapshots are unchanged
    And a comparison report labelled "restated under linear v1" is available

  Scenario: NN-35_contribution_metrics_exclude_activity_surveillance
    Given the contribution feed receives metric "online_hours" for a social_media_executive
    Then the metric is rejected at schema validation
    And the employee's SCR-P17-26 view shows only outcome and quality metrics with sources

  Scenario: NN-38_company_scoped_consent
    Given contact C consented to "newsletter" for Equator only
    When a Finbyx marketing audience is snapshotted
    Then C is not included

  Scenario: Asset consent withdrawal
    Given a staff member withdraws consent for photo asset A-55
    Then every scheduled item using A-55 moves to "held"
    And takedown tasks for published items using A-55 are due within 72 hours

  Scenario: Experiment on fees page rejected
    Given an experiment targeting "/fees"
    When it is created
    Then the response is 422 "MKT_EXPERIMENT_PROHIBITED_SURFACE"

  Scenario: NN-01_AI_draft_cannot_bypass_review
    Given a caption drafted by marketing_copy_assistant with ai_generated = true
    When a user attempts to schedule it without approval
    Then scheduling fails with "MKT_REVIEW_REQUIRED"

  Scenario: Institute promotion blocked while flag is OFF
    Given flag "academy.institute_referral" is OFF
    When an email containing a link to equatoradr.com is submitted
    Then submission fails with "MKT_LINT_BLOCKED" with rule "SL-15"

  Scenario: Automation without approval node cannot activate
    Given a workflow "on webinar end, post attendee count to LinkedIn" with no approval node
    When the marketing_manager activates it
    Then the response is 422 "OPS_AUTOMATION_APPROVAL_REQUIRED"

  Scenario: NN-37_marketing_export_package
    Given the marketing_manager requests a workspace export and a checker approves it
    Then a ZIP named "Equator_Export_<OrgSlug>_<YYYY-MM-DD>.zip" is produced with one top-level root folder of at most 40 characters
    And it contains 00_README.pdf, 00_Contents.xlsx, 06_Marketing/ and 99_Manifest/ with manifest.csv and manifest.json
    And every manifest entry's SHA-256 matches its file

  Scenario: NN-40_Brevo_migration_rehearsal
    Given MigrationRehearsalWorkflow runs in staging
    Then lists, consent states and suppressions are exported and imported into ses_marketing
    And a seed-list send succeeds with identical suppression counts
```

---

## 13. Deliverables and exit gate

- [ ] `mkt` schema and migrations; Operations Platform DB-plane isolation proven (role-grant test, outbox validator, `MarketingIngressGuard`); RLS by company.
- [ ] Settings of Appendix Y §Y.12 registered with tier badges; G-tier maker-checker and rollback tested.
- [ ] Strategy, campaigns, budgets (with `ctl` authority matrix), UTM builder and experiments register live.
- [ ] Calendar, item lifecycle, risk tiers, lint profiles (LINT + SL + MT) with fixture corpus green; claim holds; boilerplates.
- [ ] Adobe Express hand-off package and ZIP; manual-handoff evidence capture (web and mobile); evidence overdue alerts; monthly sample verification.
- [ ] `SOCIAL_PORT` adapters built and tested in sandbox, all flags OFF in production until access grants are recorded.
- [ ] Engagement inbox with E1–E10 routing into Appendix X tickets, CRM leads and the grievance track.
- [ ] DAM with rights and consent records, expiry and withdrawal flows; legacy quarantine.
- [ ] `MARKETING_PORT` (`ses_marketing` live; `brevo` ready behind flag), consent checks over the Appendix X mirror and propagation (≤ 15 min), suppression (respondent test across every executor), sender-domain authentication with RFC 8058 headers, caps, quiet hours, mass-send approvals.
- [ ] Lead-magnet registry, landing-page block library (FR-P13-V3-Y01), sequences NS-*, webinar funnel, events, referral programmes with professional block, training gate.
- [ ] MA-01–MA-32 (MA-30 retired) deployed on the Appendix X engine with approval nodes and kill switches; locked automations non-disableable.
- [ ] PR workflow, crisis room with pause, partnerships and MoU clause checks, obligations tracker.
- [ ] SEO/GEO planner wired to P13 CMS and the AI-visibility panel.
- [ ] Touchpoints, attribution registry, dashboards D-01–D-12, economics; contribution feed to Appendix Z with employee view and dispute.
- [ ] Export package (NN-37) and Brevo migration rehearsal (NN-40) passed.
- [ ] Phase addenda for P13, P11 and P14 (Appendix Y §Y.20) implemented and their acceptance tests green.
- [ ] Test packs green: `NN-16_*` (incl. `mkt`), `NN-17_*`, `NN-29_*` (DP + MT), `NN-34_*`/D3-27 rewards, `NN-35_*` contribution, `NN-36_*` budgets and payouts, `NN-38_*` company scope, `NN-40_*` migration.
- [ ] Error codes `MKT_*` registered in Appendix F §F.10.4; events registered in Appendix F.
- [ ] `docs/phases/P17-demo.md`; ADRs: `mkt` DB plane, Adobe hand-off pattern, attribution default model, Brevo activation.
- [ ] Go-live gate FR-P14-V3-Y01 signed by `compliance_officer` and DPO.

---

## 14. Open items and legal verification flags

1. **[VERIFY — open (counsel):** institution-run neutral features and BCI r.36 (OI-03); speaker honoraria to advocates (Appendix Y §Y.3.3(5)); emblem and government-name use in programme partnerships (§Y.5.5); reliance on DPDP s.3(c)(ii) for media lists (§Y.8.1).]
2. **[VERIFY — open:** TCCCPR promotional SMS hours, header suffix letters and digital consent acquisition; Brevo support for Indian DLT template IDs ([RD] F3.1) — `mkt.brevo.sms_whatsapp.enabled` stays OFF until written confirmation.]
3. **[VERIFY — open:** mailbox-provider bulk-sender requirements and complaint thresholds; defaults 0.1% alert / 0.3% pause are configurable.]
4. **[VERIFY — open:** Consumer Protection (E-Commerce) Amendment Rules 2026 Gazette text and commencement — reference-price and self-audit rules used by MT-11 and SL-17 ([RB] OP-06).]
5. **[VERIFY — open:** Meta `pages_manage_posts` review; Instagram daily API post limit (50 vs 100); LinkedIn Community Management API approval for Equator's use cases; X pay-per-use pricing at activation ([RD] F3.3).]
6. **[VERIFY — open:** Teams webinar registration/recording features on the confirmed Microsoft 365 SKU (D3-04).]
7. **[VERIFY — open:** labelling rules for synthetically generated content applicable to marketing imagery; image generation stays OFF.]
8. **[VERIFY — open:** Equator trade-mark filings; registration of the short-link domain.]
9. Brevo DPA, sub-processor list, INR pricing and transfer-register row `BREVO_EU` before `mkt.brevo.enabled` ([RD] open point 5).
10. Interface names follow Appendix X (CRM, segments, consent mirror, partner records, Brevo ingress, automation engine API and `OPS_*` engine codes) and Appendix V (configuration service); no alignment item remains open (master X-53).
11. Default department mapping for marketing roles (D3-06) to be confirmed by management, which has not yet described its departmental structure; the defaults are configurable.

## v3 Addendum (23 October 2026)

The requirements below come from the v3.0 appendices and are part of this phase's scope and exit gate.

### From Appendix AC — Workspace Suites, Open Integrations and Data Portability

**FR-P17-V3-AC01 — Marketing and social adapter conformance.** The `MARKETING_PORT` adapter `brevo` and the `SOCIAL_PORT` adapters built in P17 (FR-P17-16, FR-P17-24) meet AC.11.2–AC.11.4 and are registered in the integrations catalogue with fallback, SoR rows, approved mapping sets and a migration rehearsal (AC.12). *Acceptance:* AC-T07, AC-T09; each adapter appears on SCR-P21-05 with its flag and approver.

