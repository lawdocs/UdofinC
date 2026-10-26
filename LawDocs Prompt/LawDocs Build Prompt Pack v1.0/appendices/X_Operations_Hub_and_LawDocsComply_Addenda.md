# Appendix X — Operations Hub and LawDocsComply Addenda

**Status:** Binding for the LawDocs build; each "Add" or "Decide" item is a change request to a companion product. · **Used by:** P02, P13, P14, P15, P16, P17, P18, P19, P20, P21, P23. · LawDocs Build Prompt Pack v1.0, 25 October 2026.

> **How to use.** Part 1 is addressed to the Infrabyx Operations Hub (OH) build (Master Prompt v1.0): commit it to the OH repository as `docs/ecosystem/lawdocs-addendum.md`. Part 2 is addressed to the LawDocsComply (LDC) build (Pack v1.2). Part 3 records the Finbyx, Udofin and Equator touchpoints. Item types: **Confirm** = already in the companion spec, needs LawDocs configuration only; **Add** = new requirement; **Decide** = owner decision needed. Any item that adds or changes a cross-product contract goes through the Ecosystem Spec change process (Spec §14.2) via Appendix Y — no contract is improvised (NN-24). LawDocs never rebuilds an OH function (D-02) and OH never receives tenant documents, matters, cases, credentials or personal content (NN-19; OH Part 2.3).

## X.0 Summary of requests

| # | Area | Type | OH / LDC module | LawDocs phase |
|---|---|---|---|---|
| X.1 | Legal entities, brands, workspaces, merchant of record | Confirm / Decide | OH1, OH8 | P02, P15, P17 |
| X.2 | CRM pipelines, fields, lead sources, activity API | Add | OH3 | P17, P18, P21 |
| X.3 | Autopilot marketing engine | Add | OH7, OH3, OH14 | P21 |
| X.4 | Onboarding factory playbooks and datasets | Add / Decide | OH4 | P18, P20 |
| X.5 | After-sales and customer-success playbooks | Add | OH5, OH2 | P18 |
| X.6 | Support desk and grievance redressal | Add / Decide | OH6 | P18, P21, P23 |
| X.7 | Catalogue, streams, meters, billing | Add / Decide | OH8 | P16, P17 |
| X.8 | Staff HRMS, payroll, leave, attendance, appraisal, anti-embezzlement | Add | OH10, OH11 | P18 |
| X.9 | Employee email IDs and workplace (M365 now, Google later) | Confirm / Decide | OH12 | P18, P19 |
| X.10 | Cross-company deployment and conflict service | Confirm / Add | OH1 | P18 |
| X.11 | Revenue-stream analytics | Add | OH2, OH8.10 | P17 |
| X.12 | Professional directory | Confirm / Add | OH9 | P16 |
| X.13–X.17 | LDC: kernels, SoR handover, storefront, template supply, register | Add / Decide | LDC | P13, P16, P19 |
| X.18–X.21 | Finbyx, Udofin, Equator touchpoints | Confirm / Add | FX, UD, EQ | P11, P15, P19 |
| X.22 | Interface and event register | Add | Spec Part 6 | All |
| X.23 | Acceptance tests (companion side) | Add | — | — |
| X.24 | Open items | — | — | — |

---

# PART 1 — What the Operations Hub must add or configure for LawDocs

## X.1 Legal entities, brands, workspaces and merchant of record (OH1, OH8)

1. **Confirm** an OH1 `legal_entity` for `[LawDocs Operating Entity]` (D-08) with PAN, GSTIN per State of registration, invoice series, e-invoice flag (AATO test), revenue framework, Razorpay merchant account, DPO, Grievance Officer and Nodal Officer contacts (shown on lawdocs.in; R3 LG-077).
2. **Add** a separate OH1 `legal_entity` for the **`[Consumer Help Brand]`** (D-06, NN-23) with its own GSTIN, bank account, Razorpay merchant id, privacy policy and grievance officer (R2 §5.6). OH must treat it like Equator's scope (OH Part 4.4): default deny from every lender-side entity; no cross-entity grant except group finance/HR shared services limited to `HR`/`FINANCE` data classes; CRM, tickets and dashboards of this entity are invisible to Finbyx, Udofin and LDC staff.
3. **Decide** the **affiliated advocates' firm** structure for reserved legal services (retainers with legal advice, LDaaS; R6 §R6.2.7 [LEGAL]). The firm is an external partner, not a group company, unless counsel advises otherwise. OH holds it as a `partner_firm` (PRM objects, LDC Addendum §X.15.1) and its advocates in OH9; its invoices are its own (RCM where the client is a business entity [TAX MEMO]).
4. **Confirm** workspace N (group-company users) for LawDocs staff: sales, onboarding, CS, support, marketing, finance, HR within the LawDocs entity scope. Delivery work happens in LawDocs `apps/delivery`; HR, timesheet approval, CRM and marketing happen in OH.
5. **Add** to OH8 `selling_entity`: `products = [LD]`, `service_lines = [SAAS_INDIVIDUAL, SAAS_BUSINESS, MARKETPLACE_PLATFORM_FEE, FIRST_PARTY_SERVICES, RETAINERS, ACADEMY_REFERRAL]`. FinLegal Academy courses stay with the Academy merchant on Graphy (D-16) unless the owner moves them.
6. **Decide** one entity or two for LawDocs SaaS and LawDocs services (separate GSTIN/invoice series; bundles become two invoices) — OI-X-01.
7. **Correct (OH Master Prompt v1.0 adapter table):** remove "`ESignProvider`: LawDocs eSign (group)". LawDocs' eSign capability is never offered to the Hub or any group product as a provider (NN-06 as amended; X-05, X-15). Infrabyx group companies that need MSAs, DPAs, HR letters or vendor contracts signed do so **as LawDocs customers in their own LawDocs tenants** through a LawDocs-hosted ceremony; OH receives document and evidence references only (Appendix Y principle 15). [COUNSEL] confirms (OI-Y-02).

## X.2 CRM pipelines, objects and lead sources (OH3)

1. **Add five pipelines** (OH3.2), each with its own stages, SLAs and consent rules:

| Pipeline | Who | Stages (seed) | Owner team | Specific rules |
|---|---|---|---|---|
| `LD_INDIVIDUAL` | Individuals, families | Lead → Activated (first document) → Paid (first eSign/eStamp or plan) → Member → Advocate (referrer) | Growth (automated) | Self-serve; no outbound calls unless the person asked for a call (R4-MKT-06: inquiry-based follow-up ≤ 7 days); sensitive intents excluded from retargeting (R4-MKT-10) |
| `LD_SME_STARTUP` | Startups, SMEs, LLPs, professionals | Lead → Qualified → Health-check done → Consultation → Proposal → Won/Lost | Inside sales | Legal Health Check band only (A–D) reaches OH, never the answers |
| `LD_ENTERPRISE_FI` | Mid/large companies, NBFCs, HFCs, co-operative societies, IFSCA units | Account → Discovery → Solution → Proposal → Legal/DPA/RE addendum → Won/Lost | Account executives | MSA + DPA (+ RE outsourcing addendum where applicable); LDC cross-sell only under OH3.8 and the client's recorded authorisation |
| `LD_PROFESSIONAL_PARTNER` | Prospective empanelled professionals; partners/resellers; affiliates | Prospect → Verification (OH9) → Agreement → Active | Partnerships | Advocates: no fee of any kind, no lead promises (NN-21); CA/CS: institute switches; affiliates exclude regulated professionals (RS-LD-36) |
| `CHP_CONSUMER_HELP` | Consumer Help users | Intake → Eligible → Self-serve / Managed → Closed | Consumer Help entity only | Separate entity scope; no lender, insurer or Udofin access; no lead sale (LD-X02); no outcome language |

2. **Add** account/contact fields (OH3.1 custom fields): `ld_segment`, `ld_plan`, `ld_tenant_state`, `ld_rm_staff_id`, `ld_retainer_codes[]`, `ld_entities_count`, `ld_preferred_language`, `ld_workplace_suite` (M365/GOOGLE/OTHER), `ld_lead_magnet`, `ld_health_band`, `ld_marketplace_buyer` (bool), `cross_group_authorisation_ref` (null default).
3. **Add** lead sources: `LD_FREE_DRAFT`, `LD_LEGAL_HEALTH_CHECK`, `LD_TOOL_STAMP_DUTY`, `LD_TOOL_ESIGN_ELIGIBILITY`, `LD_TOOL_TM_CLASS`, `LD_TOOL_LIMITATION`, `LD_WEBINAR`, `LD_VSL_<source>`, `LD_REFERRAL`, `LD_AFFILIATE`, `LD_PARTNER`, `LD_MARKETPLACE_BUYER`, `LD_CONTACT_SALES`, `CHP_INTAKE`. The draft text, uploaded documents and health-check answers stay in LawDocs (`drf`, `web`); OH receives magnet id, segment, band, language, UTM/click ids and consent records only.
4. **Rule (Add):** signing counterparties and negotiation guests are never leads (R4-MKT-12; NN-34). LawDocs never sends `CP_GUEST` contacts to OH3.
5. **Confirm** `POST /v1/crm/requests` for "Talk to sales", enterprise quotes and marketplace quotes from non-subscribers; **reuse** the LDC-proposed `POST /v1/crm/activities` (LDC Addendum §X.2.3) for LawDocs RM activity logging with the same commercial-only classifier, extended with a block-list for matter terms (CNR patterns, case numbers, "FIR", party names from the tenant's open matters — checked LawDocs-side before sending).
6. **Add** speed-to-lead routing: inbound web/phone leads for SME/Enterprise pipelines are acknowledged within 5 minutes (R4 §11.10); the AI SDR (Vidhi LV-19 in R4) calls only on an inbound request, from a pre-declared A2P CLI, inside calling windows, with AI and recording disclosure and human hand-off (NN-34; TCCCPR Third Amendment 2026 Reg. 4 [VERIFY commencement — R4 OI-R4-02]).
7. **Confirm** Brevo as OH's executor (OH3.6) and the no-lock-in export (OH3.7); LawDocs integrates with OH only, never with Brevo directly.

## X.3 Autopilot marketing engine (OH7, OH3, OH14; R-056)

"Autopilot" means automated, consented, truthful funnels run from OH with LawDocs content; it does not mean unsupervised sending. Every mass send, claim and new automation has a human approver (OH7.2).

### X.3.1 Architecture

```
Content (LawDocs CMS: blog, vlog, help, tools)  ─┐
Paid (Google, Meta, YouTube, JioAds)            ─┼─► Intent landing pages (LawDocs `web`, SSR, one per intent)
Referral / affiliate / partner links            ─┘        │  "Draft free" widget (template lane) + "Hire a professional"
                                                          ▼
                Lead magnet (free draft, Legal Health Check, calculators, checkers)
                                                          ▼
                OH3 lead + consent objects (DPDP purpose; telecom preference)  ◄─ LawDocs sends ids, band, consent only
                                                          ▼
     ┌─ AI SDR (inbound only, ≤ 5 min) → booking (OH scheduler / Microsoft Bookings) ─┐
     ▼                                                                                ▼
  Nurture: Brevo email + WhatsApp (opt-in) + RCS         Webinar / explainer-video track (SMEs, startups, FIs)
     ▼                                                                                ▼
  Purchase on LawDocs (OH8 Razorpay checkout; GST invoice auto-emailed)
     ▼
  Onboarding automation (P01 profile pre-fill; first document ≤ 10 min) → activation → review request → referral prompt → expansion
```

### X.3.2 Funnel technique register (adopt EQ Appendix Y §Y.7.1 classes; LawDocs deltas)

| Technique | Class for LawDocs | Condition |
|---|---|---|
| Explainer video (VSL-style), 6–9 min per intent | Restricted | Player controls, captions and transcript always on; **no locked player** (the reference page's disabled controls are prohibited — interface interference, accessibility; NN-28, NN-50) |
| Tripwire paid webinar (₹0–₹99) or ₹499 "Legal health audit" call credited to any purchase | Restricted | SMEs, startups, finance companies only; never individuals in distress (debt, criminal, matrimonial); total incl. GST shown; refund rule; replay to registrants within 48 h |
| Countdown / scarcity | Restricted | Bound to a real event record; same for every visitor; never on Consumer Help, litigation or advocate pages |
| Value stack | Restricted | Only real deliverables at actual list prices from the OH8 price book; no invented "values" (R4 §10.3) |
| Testimonials | Restricted | NN-49: genuine, consented, verified purchase, about LawDocs services only, never about advocates, no photos by default |
| Per-source landing pages and form names | Allowed | Attribution by UTM/click id; consent banner first |
| Outcome guarantees, "waiver", "100% success", fake scarcity, anchor prices never charged | Prohibited | CCPA Dark Patterns Guidelines 2023; Consumer Protection Act 2019 (R3 LG-140, LG-142) |

### X.3.3 Lead magnets (each an OH7 `lead_magnet` row with owner, claim keys, gate, consent purposes)

| Magnet | Segment | Gate | Compliance note |
|---|---|---|---|
| **Free AI-assisted draft** (template lane: vetted template filled from answers) | Individuals, SMEs | Download watermarked PDF free without login; account to save or eSign | Template automation, not AI advice (NN-14). The AI-custom lane for individuals is labelled "AI draft — not reviewed by a professional" with one-click paid review (CH-30; Anthropic AUP [VERIFY effective date — R4 D-R4-09]) |
| **Free Legal Health Check** (20 questions → band A–D + list of missing agreements, registrations and filings) | Startups, SMEs | Result on screen without email; email copy optional with consent | General information, not legal advice; answers stay in LawDocs |
| Stamp-duty calculator, eSign-eligibility checker, TM class finder, limitation and notice-period calculators | All | Never gated | Deterministic tools; "law as of" date; reviewer of record (NN-30) |
| Challan check | Individuals (Consumer Help brand) | Not gated | Deep link to the official portal; LawDocs never collects fines (NN-23) |
| Compliance gap snapshot | NBFCs/FIs | Business email | Hand-off to LDC under neutrality |
| Founder kit (founders' agreement, NDA, ESOP templates) + TM availability search | Startups | Account | TM search advisory only |

### X.3.4 Nurture via Brevo (OH3.6) with migration and two-way sync

1. Contacts, consents and segments are mastered in OH3; Brevo executes email, SMS and WhatsApp campaigns. Sync rules: identity fields OH wins; consent and suppression most-restrictive wins; engagement Brevo wins (OH3.6).
2. Rate limits to design for: contacts endpoints 10 requests/second; most other non-email endpoints (likely including CRM objects) 100 requests/hour on standard plans (R6 D-30) — batch and back off on HTTP 429.
3. Sequences (seed; content from LawDocs, approved in OH7): **Individuals** — D0 magnet, D1 "sign in 5 minutes", D3 consented story, D7 vault tips, D21 re-engage, monthly newsletter; **SMEs** — D0 health-check recap, D2 what your band means, D5 webinar invite, D10 consultation offer, D21 case study; **Enterprise/FI** — account-based, human-led; **Trial/onboarding** — activation checklist, no countdown language.
4. WhatsApp only with explicit opt-in (unticked box), utility vs marketing templates distinguished; never used for legal notices or recovery (R6 D-31).
5. Exit path: weekly full Brevo export archived; OH3.7 round-trip test in every release.

### X.3.5 Social calendar with Adobe Express scheduling metadata (OH7.4)

1. The social calendar lives in OH7, not in Adobe Express (owner brief). Each calendar item holds: channel, account, format, caption per locale, assets (DAM ids + SHA-256), alt text, captions file, disclosures (paid partnership, AI-content label), UTM short link, approvals, claim keys, scheduled time (IST + UTC), do-not-publish-after, crisis-pause status.
2. **Adobe Express hand-off package** (adopt EQ Appendix Y §Y.4.7 fields) is generated when an item is approved. Add LawDocs fields: `adobe_express_design_link`, `adobe_express_schedule_ref` (entered by the designer after scheduling in Adobe Express), `scheduled_by`, `scheduled_at`. Do not assume an Adobe scheduling API — scheduling happens in Adobe Express premium and the scheduler records the reference [VERIFY any Adobe Express scheduling API before automating].
3. **Evidence of publication:** post URL and screenshot recorded within 24 hours; un-evidenced items flag on the calendar.
4. **Employee reporting:** marketing staff log deliverables and outcomes in OH7 (contribution metrics feed OH10 appraisal, team-level only; NN-33).

### X.3.6 Content operations: blog, vlog, shorts

1. OH7 calendar item → linked **LawDocs CMS draft** (P21 `web`; `pg_`, `pst_`, `vid_`) created through a LawDocs API; the draft is written/edited and published in the LawDocs Content Studio (`apps/console`, X-22) by `OPS_CONTENT_PUBLISHER` without developers (R-089), after OH14 claims-gate check (`GET /v1/claims-gate/check`) and reviewer-of-record sign-off for legal content (NN-30).
2. Owner's categorised Word files → Vidhi editorial draft (labelled) → editor → reviewer → publish; "law as of" date and named reviewer on every guide (IMP-077, IMP-096).
3. Vlog: YouTube-hosted; LawDocs embeds with a click-to-load privacy facade (R6 D-32 [VERIFY]); captions mandatory (NN-28); AI-generated audio/video/avatars labelled per IT Rules 2026 [VERIFY — R3 LG-077].
4. Shorts: 3–5 scripts per tutorial or article; each short is its own calendar item with the hand-off package.
5. Publication status flows back to OH7 by event: internal `in.lawdocs.web.PageVersionPublished.v1` (or `hlp.TutorialPublished` / `hlp.ClipExported` for tutorials and clips) for an item linked to an OH7 calendar item → `int` → proposed `in.infrabyx.ops.ContentPublished.v1` (Appendix Y §Y.7.10). Asset bundles (title, one-liner, summary, OG image, UTM URL, clips with captions) are pushed by `int` to the OH7 asset library (LawDocs as caller of the asset-library API, Appendix Y §Y.8; P21 FR-P21-86).

### X.3.7 PR and collaborations (OH7.7)

Confirm OH7.7 pipelines. LawDocs collaboration targets: startup incubators, chambers of commerce, NBFC and co-operative associations, legal-tech media, universities (legal-aid clinics), CA/CS firms as software partners. Rules: no co-marketing that promotes an individual advocate; bar-association collaborations limited to education; press releases pass the claims gate (no "verified lawyers", "real-time court data", certification or "government-approved" claims — NN-20).

### X.3.8 Referral and affiliate

| Programme | Stream | Default | Rules |
|---|---|---|---|
| User → user referral (credits both sides on referee's first paid action) | RS-LD-35 | ON | Credits, not cash, for consumers; T&C disclosure |
| Affiliate (creators, bloggers, non-professional partners), % of first-year subscription | RS-LD-36 | OFF | No regulated professionals; "#ad" disclosure; counsel review |
| Partner / reseller (software vendors, chambers, banks' SME desks, incubators) | RS-LD-37 | ON | Partner is not a regulated professional; revenue share on software only |
| Group cross-referral | RS-LD-38 | OFF | s.188 Companies Act arm's length; DPDP purpose limitation |

**Conflict resolved:** R4 §11.6 suggests advocates pay a flat listing fee. That is superseded by D-05 and NN-21: no listing, lead, ranking or badge fee from advocates (RS-LD-28 prohibited).

### X.3.9 Review generation within NN-49

Trigger a review request only after a verified purchase and a completed outcome (document signed, order delivered); ask for a review of **LawDocs (the company) or the service**, never of an advocate; no incentive conditional on a positive review; no suppression of negative reviews; display without photos by default; moderation per IS 19000:2022 and the E-Commerce Rules 2020 (R3 LG-141, LG-143); review records keep consent and purchase reference.

### X.3.10 Attribution and KPIs

Server-side conversions (Google Enhanced Conversions, Meta CAPI) only for consented users; sensitive-intent exclusion list (criminal, matrimonial, debt distress, health claims, Consumer Help pages) applied to retargeting and lookalikes (R4 §11.9). KPIs (calibrate in 90 days, R4 §11.10): speed-to-lead ≤ 5 min for 90%; tool page → magnet ≥ 20%; free draft → paid eSign/eStamp ≥ 15%; webinar show-up ≥ 35%; CAC payback ≤ 6 months (Personal), ≤ 12 months (Pro/Business) (R6 §R6.7); upheld UCC complaints = 0.

## X.4 Onboarding factory (OH4)

1. **Add** methodology templates:

| Template | Segment | Stages | Human involvement |
|---|---|---|---|
| `LD_SELF_SERVE` | Individuals, small SMEs | Sign-up → profile pre-fill (P01) → first document → first eSign | None; D+2 support check-in for paid plans |
| `LD_SME_STANDARD` | Pro/Business | Kick-off → org set-up (departments, makers, checkers) → template import → contract migration → training → go-live → 30-day hypercare | Onboarding coordinator |
| `LD_ENTERPRISE` | Enterprise, FIs | Discovery → design workbook → build → migration → integrations (M365/Google, CRM, HRMS) → UAT → training → cut-over → hypercare | Implementation manager |
| `LD_RETAINER` / `LD_LDAAS` | Retainer clients | Above + RM assignment + grant proposals + SLA activation + vault decision | RM + delivery lead |
| `LD_PRACTITIONER_FIRM` | Third-party firms | Verification (OH9) → firm workspace → client links | Partnerships |

2. **Add** migration dataset types (counts and control totals only in OH4 `migration_run`): `LD_CONTRACT_FOLDERS` (folder intake, P04/P20), `LD_CASE_LIST` (Excel; dedupe on CNR — IMP-066), `LD_TM_PORTFOLIO` (application numbers), `LD_TEMPLATES` (client's own templates), `LD_USERS_ORG` (users, departments, positions), `LD_NOTICES_REGISTER`, `LD_OBLIGATIONS`.
3. **Add** RM assignment at kick-off: OH4 calls `POST /v1/delivery/assignments` (signed machine client) with staff ids; LawDocs then proposes delivery grants to the client admin (P18 §4C).
4. **Add** `in.infrabyx.ops.TenantSelfServeCreated.v1` (reuse the LDC-proposed contract, LDC Addendum §X.3.1) with `product = LD`, `origin ∈ {FREE_DRAFT, PRICING, MARKETPLACE, HEALTH_CHECK, RM_INVITE, MOBILE_APP}`; OH creates/matches the account and opens a `SELF_SERVE` onboarding case without emitting `TenantProvisioned`.
5. **Decide (deviation from OH8.9):** LawDocs Free and Personal accounts are production accounts holding the user's own documents from day one (the product is a vault); OH8.9's sandbox-only trial rule cannot apply to them. Business trials may be production-grade under click-wrap ToS + DPA, with no auto-conversion (NN-50) — OI-X-02.
6. **Add** workplace-migration runbook use (OH12.7) for clients that engage LawDocs to move legal files from Google Drive/OneDrive into the LawDocs vault (folder intake keeps folder names as metadata).

## X.5 After-sales and customer-success playbooks (OH5, OH2)

| Playbook | Trigger | Actions | Guard-rails |
|---|---|---|---|
| Activation | Account created, no document in 3 days | In-app tour, one email, optional call for Business | No more than one call attempt without a reply |
| Adoption | Low vault/CLM usage at day 30 | Feature tips by role; webinar invite | — |
| Retainer QBR | Quarterly | QBR pack from P18 (SLA, deliverables, hours, savings only if the client allows) | Savings figures follow NN-36 |
| Renewal | 90/30/7 days before renewal | Renewal notice with price and cancellation path | No auto-renew traps; cancel as easy as buy (NN-50) |
| Expansion | Usage at 80% of entitlement; new legal need | Add-on or service quote via OH8 | No pressure copy; LDC cross-sell only with authorisation |
| Risk | Detractor NPS ≤ 6, SLA breach, unresolved complaint | CSM task; service credit review | — |
| Exit | Cancellation requested | Export assistance (`LD-EXPORT-1.0`), data-return certificate, survey | Export never blocked by dunning (NN-11; Spec §6.27) |

**Add** `in.infrabyx.ops.ClientHealthSignal.v1` for LawDocs (reuse LDC-proposed contract) with fields: `tenantid`, `date`, `active_users`, `entitled_seats`, `documents_created_30d`, `signatures_completed_30d`, `matters_tracked`, `tm_marks_tracked`, `vault_storage_gb`, `sla_breaches_30d`, `open_change_requests`, `retainer_hours_used_pct`, `last_meeting_at`, `renewal_risk_flag` (fixed reason codes). **Excluded by schema:** document titles, counterparties, matter or case data, consumer-case data. **Add** `in.infrabyx.ops.SurveyResponseRecorded.v1` (score, survey type, sentiment class; no free text unless the respondent ticks "share my comment with the account team").

## X.6 Support desk and grievance redressal (OH6; LawDocs console)

1. **Add** ticket categories: `LD_ACCESS_LOGIN`, `LD_KYC_ONBOARDING`, `LD_DRAFTING_TEMPLATE`, `LD_ESIGN`, `LD_ESTAMP`, `LD_VAULT_DMS`, `LD_LITIGATION_DATA`, `LD_TM_DATA`, `LD_VIDHI_AI`, `LD_MARKETPLACE_SERVICE`, `LD_BILLING_DISPUTE`, `LD_DATA_EXPORT`, `LD_ACCESSIBILITY`, `LD_SECURITY_REPORT`, `LD_CONTENT_ACCURACY`, `CHP_CASE_SERVICE` (Consumer Help entity scope only).
2. **Add** severity uplift: `LD_ESIGN`/`LD_ESTAMP` with a signing deadline ≤ 24 h, `LD_LITIGATION_DATA` with a hearing ≤ 48 h, and `LD_TM_DATA` with a statutory deadline ≤ 7 days get P1 handling.
3. **Add** routing: `LD_CONTENT_ACCURACY` creates a content-review task in LawDocs (`tpl`/`rul` maker-checker); OH never edits LawDocs content (NN-30). `LD_BILLING_DISPUTE` with an invoice ref pauses dunning for that invoice (OH8.7).
4. **Grievance redressal ownership (Decide; recommended split):**

| Grievance | Owner and system | OH role | Clock [VERIFY current text] |
|---|---|---|---|
| User/intermediary grievance about content, accounts or platform conduct (IT Rules 2021 as amended 2026) | `PLT_GRIEVANCE_OFFICER` desk in LawDocs `apps/console` (holds user content) | Metadata mirror (category, clocks, status) for MIS | Acknowledge ≤ 24 h; resolve ≤ 7 days; order-based takedown ≤ 3 h; prohibited-content complaints ≤ 36 h (R3 LG-077) |
| Consumer complaint about a purchase (E-Commerce Rules 2020 r.4) | LawDocs grievance desk | Mirror | Acknowledge ≤ 48 h; redress ≤ 1 month (R3 LG-141); the stricter clock wins where both apply |
| DPDP data-principal grievance | LawDocs DPO desk | Mirror | Per DPDP Rules (NN-26) |
| Business client complaint about LawDocs services or retainers | OH6 `client_complaint` | Full handling | OH6.5 |
| Consumer Help user complaint | Consumer Help entity's own grievance officer (separate desk) | Mirror inside that entity's scope only | As above |
| Complaint about an engaged advocate's professional conduct | Advocate's State Bar Council remains the forum; LawDocs records the service complaint and may suspend allocation | — | — |

5. **Confirm** published grievance officer details (name, contact, response times) on lawdocs.in and in-app (D-08); role mailbox `grievance@` (X.9).

## X.7 Catalogue, streams, meters and billing (OH8)

1. **Add** LawDocs SKUs: plans `LD-FREE`, `LD-PERSONAL`, `LD-PRO`, `LD-BUSINESS`, `LD-ENTERPRISE` (seed prices R6 §R6.2.2 [OWNER TO SET]); add-ons (R6 §R6.2.3); credit packs (eSign, OTP-sign, AI, court-data refresh; valid 12 months, no auto top-up by default); one-time products (R6 §R6.2.5); retainers and hour banks (R6 §R6.2.7); marketplace buyer platform fee (flat, separate line).
2. **Add** stream codes RS-LD-01…RS-LD-45 (R6 §R6.5) with the defaults stated there; **hard-deny** in the OH8.3 legality gate: RS-LD-27 (share of advocates'/CAs'/CSs'/CMAs' fees), RS-LD-28 (listing, featured, ranking, lead or badge fees from regulated professionals), RS-LD-29 (referral rewards to regulated professionals), plus LD-X01…X04. Streams RS-LD-24, 26, 33, 34, 36, 38, 39, 40, 43, 44, 45 start OFF and need [LEGAL]/[TAX MEMO] references before `ON`; RS-LD-34 advertising also follows NN-35.
3. **Add** meters (`meter_kind = USAGE`): `ESIGN_AADHAAR`, `ESIGN_OTP`, `ESTAMP_FACILITATION`, `AI_CREDITS`, `AGENT_SEATS`, `COURT_DATA_REFRESH`, `TM_WATCH_MARKS`, `STORAGE_GB_MONTH`, `API_CALLS`, `EXTRA_SEATS_PEAK`, `DATA_ROOMS`.
4. **Add** pass-through invoice lines: stamp duty and government/statutory fees as pure-agent recoveries shown separately from professional and LawDocs fees, total incl. GST before payment (NN-22) [TAX MEMO].
5. **Add** Razorpay Route linked accounts for empanelled professionals and Consumer Help panel advocates (professional fee → professional; LawDocs fee → LawDocs); Route `on_hold` released on deliverable acceptance per P16; LawDocs never pools third-party money (RBI PA Directions 2025; R3 LG-145).
6. **Add** invoices to buyers without a tenant (marketplace buyers, D-11) and to individuals at scale (B2C tax invoices; e-invoice applicability [VERIFY]); RCM flag on advocate-to-business invoices issued in the advocate's name (Notification 13/2017-CT(R) [VERIFY]).
7. **Add** `in.infrabyx.billing.ServiceCreditIssued.v1` (reuse LDC contract) for retainer SLA credits; `order_context = MARKETPLACE_ENGAGEMENT | CONSUMER_HELP_CASE` with `eng_` or `grv_` reference only.
8. **Add** catalogue change requests `POST /v1/catalogue/change-requests` with `product = LD` (reuse LDC §X.8.4); the person who drafts a price change can never approve it.
9. **Confirm** dunning never blocks read access or export (Spec §6.27).
10. **Decide** LOCAL billing adapter if OH8 is not live when P17 ships (LDC Addendum §X.8.10 pattern) — OI-X-03.
11. **Add** consumer billing identity on OH8 (X-13): for individual buyers — including buyers of the `[Consumer Help Brand]` entity — LawDocs sends only the closed field list name, email, phone, optional GSTIN and billing address, amounts and tax lines, SKU and quantity, under legal basis `CONTRACT_PERFORMANCE_CUSTOMER` (Appendix Y §Y.6.2). No case content, respondent institution, grievance narrative or document data; Consumer Help SKUs are generic service codes. OH8 rejects any other PII field from LawDocs. DPO sign-off before the first B2C invoice (OI-Y-03).
12. **Add** execution of `in.infrabyx.billing.MarketplaceTransferInstructed.v1` (RELEASE / REVERSE / EXTEND_HOLD of on-hold Route transfers; Appendix Y §Y.7.7) and publication of `MarketplacePayoutSettled` back to LawDocs; release only on the instruction, never on a staff action alone (X.8 control table).

## X.8 Staff HRMS, payroll, leave, attendance, appraisal and anti-embezzlement (OH10, OH11)

1. **Add** job architecture for LawDocs mapped to role codes (Conventions §6): Relationship Manager / Senior RM → `OPS_RM`; Legal Associate, Company Secretarial Executive, Tax Associate → `OPS_PROFESSIONAL`; Quality Reviewer → `OPS_QA_REVIEWER`; Delivery Lead → `OPS_DELIVERY_LEAD`; Onboarding Coordinator → `OPS_ONBOARDING`; Customer Success Manager → `OPS_CSM`; Support Agent → `OPS_SUPPORT_AGENT`; Content Publisher → `OPS_CONTENT_PUBLISHER`; Consumer Case Manager (Consumer Help entity) → `OPS_CONSUMER_CASE_MANAGER`.
2. **Confirm** WFH and pan-India hiring (OH10.2, OH10.5): the **State of work** drives Shops and Establishments registration, professional tax, labour welfare fund, holidays and leave (higher of Code and State law), using the shared `infrabyx-labour-rulepack` (Four Labour Codes in force 21 Nov 2025; Central Rules 8 May 2026 — R3 LG-162…LG-165). Appointment letters state WFH terms.
3. **Confirm** attendance from IdP sign-in/sign-out plus declared work sessions (CH-32); prohibited with no setting: keystroke or mouse scores, screenshots, webcam/microphone capture, browsing history, AI productivity scores for discipline or pay (OH10.5; NN-33; R3 LG-167).
4. **Add** appraisal inputs: LawDocs `DeliveryMetricsMonthly` (P18 FR-P18-69) and OH7 contribution metrics; calibration by manager + HR; no automated people decisions.
5. **Add** LawDocs delegation-of-authority and anti-embezzlement controls in OH11:

| Control | Rule |
|---|---|
| Refunds, credits, write-offs, discounts beyond DoA | Maker-checker in OH8; maker ≠ checker; thresholds per role |
| Route payout holds/releases to professionals | Release only on P16 acceptance event; manual release needs two approvers |
| Professional or vendor bank-account change | Penny-drop verification, 48-hour cooling-off, dual approval, notice to the old contact |
| Payment collection | Only via OH8 checkout/links; no staff UPI or personal accounts; client-facing notice (P18 FR-P18-52) |
| Fraud analytics (counts only from LawDocs) | Refunds to the same instrument cluster; discount clustering per RM; credits soon after tickets; bank changes before payouts; reveal anomalies count from P18 |
| Rotation | RMs on the same retainer rotated or reviewed every 24 months [REC] |
| Gifts and hospitality | OH7.7/OH11 register; PCA 1988 s.9 adequate procedures [VERIFY guidance] |
| Whistle-blower | OH11.5 channel available to LawDocs staff and empanelled professionals |
| POSH | Internal Committee for the LawDocs entity (POSH Act 2013 s.4; R3 LG-166) |

## X.9 Employee email IDs and workplace suites (OH12)

1. **Confirm** M365 provisioning via Entra ID (OH12.3): `first.last@lawdocs.in` (and the Consumer Help brand domain for that entity); role mailboxes `grievance@`, `dpo@`, `nodal@`, `security@`, `billing@`, `support@`, `careers@`, `legal@` with named owners; addresses never reissued; licence pool and leaver steps as OH12.3.
2. **Add** SCIM provisioning from Entra ID to LawDocs Keycloak realm `ld-staff`; groups map to LawDocs role codes; `EmployeeOffboarded` delivered to LawDocs within 5 minutes (P18 FR-P18-02).
3. **Add** collaboration structure for delivery: Teams team "LawDocs Delivery" with a channel per retainer client; SharePoint working site `LawDocs-Clients/<client-code>` (Default Geography India only, OH12.1); guests only named client contacts with 90-day expiry; final deliverables always filed in the client's LawDocs vault (P18 FR-P18-42).
4. **Decide** the Microsoft 365 SKU actually held (CH-29: "Business Starter" is a Google Workspace edition; Microsoft offers Business Basic/Standard/Premium) and whether Intune/conditional access is available — OI-X-04.
5. **Confirm** Google Workspace later through the same `WorkplaceProvider` interface with OH12.1 residency limits (non-regulated data only until India residency exists) and the OH12.7 migration runbook; LawDocs design keeps canonical files in its DMS so a suite switch needs no client-data migration (NN-12).

## X.10 Cross-company deployment and conflict service (OH1; Spec §4.6)

1. **Confirm** one staff identity, separate product roles; cross-entity work (for example a Finbyx implementation consultant helping a LawDocs NBFC retainer) uses an OH `group_grant` with purpose `IMPLEMENTATION_DELIVERY` or `CUSTOMER_SUCCESS`, ≤ 90 days, renewal as fresh approval; client delivery grants in LawDocs are still required.
2. **Add** LawDocs as a machine client of `POST /v1/conflicts/check` (today EQ-only) with input `professional_id | person_ref`, `counterparty org_id or hashed identifier`, and new categories `CONSUMER_HELP_ADVERSE` and `LENDER_CLIENT`; answers are counts and flags only.
3. **Add** wall rules: (a) no person holds a Consumer Help role and a lender-side client role in any group product; (b) Equator case-level roles block delivery grants for lenders with Equator matters (Spec §8.6); (c) group dashboards show aggregates across entities, drill-down only within the user's entity (OH Part 3.3).
4. **Confirm** shared operations content (playbooks, templates, training) can be shared across group companies through OH7/OH12 purpose-bound spaces; LawDocs tenant data never is (NN-19).

## X.11 Revenue-stream analytics (OH2, OH8.10)

**Add** a LawDocs revenue view: MRR/ARR by plan and segment; one-time revenue by SKU family; marketplace **GMV shown separately from LawDocs platform-fee revenue** (third-party professional fees are not LawDocs revenue); pass-through duty and government fees excluded from revenue; stream status board (DRAFT / LEGAL_REVIEW / ON / OFF / KILLED) for RS-LD-01…45 with kill-switch history (NN-39); unit-economics guard-rails (R6 §R6.7: subscription gross margin ≥ 75%, eSign allowance cost ≤ 15% of plan price, AI credit cost ≤ 40% of credit price, retainer utilisation 70–85%); cohort retention; CAC payback by channel; Consumer Help entity reported separately; group consolidation only as aggregates.

## X.12 Professional directory (OH9)

1. **Confirm** OH9 as credential source; LawDocs consumes `ProfessionalEmpanelled`/`ProfessionalSuspended` and suspends allocation and grants within 1 hour.
2. **Add** non-profession provider categories needed by the marketplace (translators, typists, process servers, document couriers, valuers, notary facilitators) in a separate partition (`mkp_providers`) — they are not BCI Rule 36 professions; take rates allowed only per RS-LD-25.
3. **Confirm** ICAI's aggregator restriction (23 Oct 2019) and ICSI analogues: practising CA/CS listing and any percentage model OFF until counsel and checker approval (D-05, CH-09) [VERIFY 2026 position].
4. **Confirm** directory API ordering is randomised per call with seed logged (Spec §6.29) wherever LawDocs shows professionals; no ranking parameter exists.

---

# PART 2 — What LawDocsComply must add

## X.13 Shared kernels (D-10, NN-47)

| Kernel | LawDocs use | LDC obligation |
|---|---|---|
| `@infrabyx/governance-kernel` | Local Governance mount for LawDocs-only companies (P13) | Publish semver releases with migration notes; contract tests runnable in LawDocs CI; no LDC-only fields in the kernel core |
| `@infrabyx/hrms-kernel` + `infrabyx-labour-rulepack` | Local HRMS mount for LawDocs-only companies | Same; State rule updates published as data (NN-30) |
| `@infrabyx/docgen`, `@infrabyx/redline` | Drafting, CLM redlines | Shared bug fixes; deterministic output tests (NN-37) |
| `@infrabyx/archive-standard` | `LD-EXPORT-1.0` profile | LDC's `LDC-EXPORT-1.0` and LawDocs' profile share the manifest schema so an export from one imports into the other |

Rule: kernels are used, never forked; a LawDocs-needed change is raised as a kernel pull request with both products' contract tests green.

## X.14 System-of-record handover when a tenant has both products

1. **Detect:** the OH tenant map (Spec §4.1) shows the same `org_id` with an LDC tenant; LawDocs shows the tenant admin a "Connect LawDocsComply" card.
2. **Consent and switch:** tenant admin (maker) + second admin (checker) set `int.eco.ldc.sor_mode.governance` and/or `int.eco.ldc.sor_mode.hrms` to `LDC` (default `LOCAL`; X-11 replaces the former `gov.mode`/`hr.mode`/`gov.sor_mode` keys) — NN-18 critical configuration; the state machine is Appendix A §A.48.
3. **Migrate:** LawDocs exports local governance and HRMS records (board, committees, meetings, minutes, resolutions, registers, directors/KMP, people, positions, duties) in the archive standard; LDC imports with reconciliation counts; LawDocs keeps a read-only snapshot for 90 days.
4. **Operate:** governance and HRMS become read-through views in LawDocs (e.g., authorised signatories for signing, KMP list for approval matrices, board approval status for CLM); writes go through contracts — a contract needing board approval creates an agenda-item request in LDC; the passed resolution returns as an event referenced in the CLM record. SSO between products; no double entry.
5. **Reverse:** if the client leaves LDC, LDC exports the same profile and LawDocs re-mounts locally.
6. **Delivery and vault (Decide; recommended):** one credential vault per client — when LDC is present, regulator-portal credentials live in the LDC vault and LawDocs `cvl` is disabled for that tenant with a deep link; no credential crosses products (NN-16, CH-16) — OI-X-05. RMs use each product's own delivery console with a product switcher.
7. **LDC must add:** the connect/handover API (`POST /v1/sor-handover/requests`, status events), governance agenda-request intake from LawDocs, and resolution/approval events to LawDocs — all via Appendix Y.

## X.15 Marketplace listings into the group storefront (D-11)

1. LDC services and FinLegal Academy courses appear at lawdocs.in/marketplace from the OH8 catalogue (`product = LDC`/`ACADEMY`), browsable without login or subscription (R-041).
2. **LDC must supply** per listing: category, audience, deliverables, SLA, price basis, required inputs, fulfilment product (`LDC`), reviewer of record for descriptions; **consume** `in.infrabyx.ops.ServiceOrderRouted.v1` (LawDocs → LDC, with the buyer's consent artefact; P16 FR-P16-76) and **emit** order-status events back (`in.infrabyx.ops.ServiceOrderStatusChanged.v1`) so the buyer sees status in LawDocs if they bought there. Both use the `ops` domain (Appendix Y §Y.7.9; the earlier `compliance.` and `services.` drafts are superseded).
3. Orders, quotes, GST invoices and Razorpay run on OH8; fulfilment happens in the LDC delivery console; LawDocs never fulfils LDC SKUs.
4. LDC in-app shows the same listings from the same catalogue version; prices and copy are never forked.
5. Reviews follow NN-49 (verified purchase, non-advocate services only).

## X.16 Template supply

1. **LawDocs → LDC:** contract and document templates LDC clients need (outsourcing agreements, DSA/LSP agreements, NDAs, vendor contracts, employment documents) through a signed, versioned feed `GET /v1/templates/feed?product=LDC` with jurisdiction, effective dates, reviewer of record and licence terms (NN-30).
2. **LDC → LawDocs:** policy and governance templates for regulated entities that LawDocs sells as one-time services or uses in retainers, through the same feed format.
3. An intra-group licence between the entities records ownership and pricing at arm's length [TAX MEMO; Companies Act 2013 s.188 where applicable].
4. Neither product copies the other's rules register; templates reference rule IDs, and the consuming product resolves them locally or marks them "unverified" (NN-14).

## X.17 LDC contracts register (LawDocs side)

| Contract | Direction | Status |
|---|---|---|
| SSO between LDC and LawDocs (group IdP for staff; product IdPs for clients) | both | Add |
| `POST /v1/sor-handover/requests`; `SorHandoverCompleted` | LD ↔ LDC | Add (Appendix Y) |
| Governance agenda request; `ResolutionPassed` read event | LD → LDC; LDC → LD | Add |
| `GET /v1/templates/feed` | both | Add |
| `ServiceOrderRouted` (`ops`) | LD → LDC (via OH8 order context; buyer consent) | Add |
| `ServiceOrderStatusChanged` (`ops`) | LDC → LD (via OH8 order context) | Add |
| Token-exchange launch (RFC 8693) for the same organisation's customers (Appendix Y §Y.3.6) | both | Add |
| **Correct** LDC P18 FR-P18-22 and FR-P18-40: "LawDocs eSign (group)" as an `ESignProvider` and LawDocs eSign envelopes are replaced by the hosted signing hand-off (`POST /v1/signing-requests` in the organisation's own LawDocs tenant under `signing_handoff_link`; status and evidence by reference) | LDC → LD | Correct (X-05; NN-06) |
| `DocumentShared` (Spec §6.13) for signed contracts LDC needs as compliance evidence, with consent ref | LD → LDC | Confirm |

---

# PART 3 — Finbyx, Udofin and Equator touchpoints

## X.18 Finbyx

1. **Litigation:** a lender tenant using Finbyx Recovery Suite keeps recovery litigation there (Spec §6.10 events are produced by RS). LawDocs consumes `LitigationCaseOpened/Updated`, `HearingScheduled`, `OrderRecorded`, `LitigationCaseClosed` only if the tenant opts in, to show recovery cases in its legal-risk dashboard (IMP-104) — a new consumer registration (Appendix Y). Non-recovery litigation of the same company stays in LawDocs.
2. **Notices and templates:** LawDocs may supply notice templates (s.138 NI Act demand notice, SARFAESI s.13(2) notice drafts) to Finbyx through the template feed; Finbyx generates and sends them in its own product.
3. **eSign:** LawDocs never sublets its ASP arrangement to Finbyx (NN-06); Finbyx uses its own ESP contracts.
4. **Professionals:** OH9 is shared; Finbyx's `MatterAllocated` flows to OH9, never to LawDocs.

## X.19 Udofin

1. Udofin is a lending service provider for partner REs; its borrowers' grievances belong to the RE and Udofin (OH6.5). **Consumer Help must never source cases, leads or data from Udofin**, and Udofin must never refer distressed borrowers to Consumer Help (wall; RS-LD-38 OFF; R2 §5.6).
2. Udofin's own legal team may use LawDocs as a normal B2B tenant (CLM for LSP-RE agreements, notices, vault) under ordinary terms; no special data path exists.
3. Loan documents of REs are the RE's; LawDocs does not draft or eSign borrower loan agreements on Udofin's behalf through any embedded flow (NN-06).

## X.20 Equator

1. **Referral to ODR:** a LawDocs user may refer a non-loan contract dispute or a consumer matter to an ODR institution of their choice, with explicit consent, through LawDocs' provider-neutral `ODR_PORT` (Appendix I §I.2.4). **Equator is one provider among several, never pre-selected, default or mandatory**; every screen discloses "Equator Resolution is an Infrabyx group company" and lists the other configured providers in neutral order. For Equator, LawDocs becomes a registered producer of `ADRReferralCreated`-type referrals (Spec §6.9 today lists RS as producer) — Appendix Y §Y.7.4; payload limited to what the user chose to share (NN-24). The referral machine is P11's (Appendix A §A.43; R-A-15).
2. **Mediators and arbitrators** are never listed in the LawDocs marketplace; LawDocs routes to the institution the user chooses (R6 §R6.3).
3. **Clause supply:** Equator's model dispute-resolution clauses are supplied to the LawDocs clause library via the template feed with Equator as reviewer of record.
4. **Neutrality:** no LawDocs staff member or empanelled advocate acting for a party may be an Equator neutral in a matter involving that party; OH1.6 check applies; Equator case data never appears in LawDocs.
5. **eSign (Correct, EQ Appendix AC):** the optional `lawdocs_esign` route on Equator's `ESIGN_PORT` is withdrawn (NN-06 as amended; X-05). Equator signs awards and settlement agreements through its own ESP; where a LawDocs user executes a settlement agreement in LawDocs, it is a LawDocs-hosted ceremony in the user's own tenant and Equator receives evidence by document reference only.
6. **Consumer Help vs Equator grievance SaaS:** where a lender against whom a Consumer Help user complains is an Equator grievance-SaaS client, the conflict check returns a flag and the case proceeds self-serve only.

## X.21 Common ecosystem items

Register LawDocs as owner code `LD` with CloudEvents source `urn:infrabyx:lawdocs:<tenantid>`; LawDocs `int` is the only publisher/consumer of cross-product events; product switcher deep links between OH, LDC, Finbyx, Udofin, Equator and LawDocs consoles, each under its own authentication and logging.

---

## X.22 Interface and event register (LawDocs ↔ OH / LDC / FX / UD / EQ)

| Contract | Direction | Status | Section |
|---|---|---|---|
| `TenantProvisioned`; `PUT /v1/provisioning-requests/{id}` | OH ↔ LD | Existing (§6.29) | X.4 |
| `TenantSelfServeCreated` | LD → OH | New (reuse LDC proposal) | X.4 |
| `POST /v1/delivery/assignments` | OH4 → LD | New | X.4 |
| `ImplementationMilestoneReached` | OH ↔ LD | Existing | X.4 |
| `POST /v1/crm/requests` | LD → OH3 | Existing | X.2 |
| `POST /v1/crm/activities` | LD → OH3 | New (reuse LDC proposal) | X.2 |
| Lead capture with consent objects (`POST /v1/crm/leads`) | LD `web` → OH3 | New | X.2, X.3 |
| OH7 asset-library bundle upload (LD as caller; path per OH owner) | LD → OH7 | New | X.3.6 |
| `ContentPublished` | LD → OH7 | New | X.3.6 |
| `GET /v1/claims-gate/check` | LD → OH14 | Existing | X.3 |
| `ClientHealthSignal`, `SurveyResponseRecorded` | LD → OH5 | New | X.5 |
| `POST /v1/support/tickets`; `SupportTicketOpened/Resolved` | LD ↔ OH6 | Existing | X.6 |
| Grievance metadata mirror (`GrievanceStatusChanged`) | LD → OH6 | New | X.6 |
| `GET /v1/catalogue/versions/{v}`; quotes, orders, invoices, entitlements, usage disputes | LD ↔ OH8 | Existing | X.7 |
| `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPayment*`, `SubscriptionCancelled` | OH8 → LD | Existing | X.7 |
| `UsageRecorded` (LD added as producer), `ModuleAttached/Detached` | LD → OH8 | Existing event; LD producer registration in Appendix Y §Y.7.7 | X.7 |
| `MarketplaceTransferInstructed` (signed); `MarketplacePayoutSettled` | LD → OH8; OH8 → LD | New | X.7 |
| Billing identity under `CONTRACT_PERFORMANCE_CUSTOMER` (closed field list; consumer and Consumer Help buyers) | LD → OH8 | New legal basis | X.7 item 11 |
| `ServiceCreditIssued`; catalogue change requests | LD → OH8 | New (reuse LDC proposals) | X.7 |
| `TimesheetAggregated`, `DeliveryMetricsMonthly` | LD → OH4/OH10/OH11 | New | X.8 |
| SCIM 2.0; `EmployeeOffboarded` consumer | Entra/OH10 → LD | New for LD | X.9 |
| `POST /v1/conflicts/check` (LD client; new categories) | LD → OH1.6 | Extend | X.10 |
| `ProfessionalEmpanelled/Suspended`; `GET /v1/directory/professionals` | OH9 → LD | Existing | X.12 |
| `ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected` | LD ↔ OH13/OH14 | Existing | P23 |
| SoR handover, agenda request, `ResolutionPassed`, template feed, `ServiceOrderRouted`, `ServiceOrderStatusChanged`, token-exchange launch | LD ↔ LDC | New | X.14–X.17 |
| §6.10 litigation events (consumer) | FX RS → LD | New consumer | X.18 |
| ADR referral (producer; Equator as one `ODR_PORT` provider) | LD → EQ | New producer | X.20 |
| Hosted signing hand-off (replaces "LawDocs eSign as provider") | OH, LDC, EQ, FX → LD | Correct | X.1 item 7, X.17, X.20 |

All new contracts follow Ecosystem Spec Part 3 (CloudEvents 1.0, JWS for financial and entitlement events, Idempotency-Key, outbox/inbox, India residency, business-contact data only with a recorded legal basis) and are proposed in Appendix Y with domains `ops`, `billing`, `governance`, `documents`, `adr`, `litigation`, `legal`, `esign`, `ip`, `engagement`, `platform`, `directory` and `privacy`.

## X.23 Acceptance tests (companion side)

1. A `TenantSelfServeCreated` with `product = LD` for an existing `org_id` creates no duplicate account and opens one `SELF_SERVE` onboarding case.
2. A `CHP_CONSUMER_HELP` lead is invisible to every user outside the Consumer Help entity scope, including group leadership drill-down.
3. A `POST /v1/crm/activities` payload containing a CNR-pattern string is rejected with a reason.
4. A `ClientHealthSignal` containing an unknown field (e.g., `document_titles`) is rejected by schema.
5. An attempt to set any stream of the RS-LD-27/28/29 class to `ON` is refused by the OH8 legality gate.
6. A refund above DoA is not executed until a different approver checks it; a professional's bank-account change waits 48 hours and needs two approvers.
7. No OH10 setting exists that enables keystroke, screenshot, webcam or browsing monitoring.
8. An `EmployeeOffboarded` for a LawDocs RM reaches LawDocs within 5 minutes and LawDocs acknowledges the sweep.
9. A marketplace order for a buyer without a LawDocs tenant produces a GST invoice with the buyer's GSTIN and place of supply, and the advocate's fee and LawDocs' fee on separate documents.
10. The Brevo round-trip test (export → re-import → compare counts, relationships, consent states) passes in every OH release.
11. A social calendar item cannot move to `PUBLISHED` without a post URL and screenshot evidence.
12. LDC: setting `int.eco.ldc.sor_mode.governance = LDC` without a second admin's approval is refused; after handover, a LawDocs governance write is redirected to an LDC agenda request.
13. LDC: a template from the feed without a reviewer of record is rejected by LawDocs `tpl` import.
14. OH8: a B2C billing payload from LawDocs carrying any field outside the `CONTRACT_PERFORMANCE_CUSTOMER` list (e.g., a respondent institution name on a Consumer Help purchase) is rejected with `dataclass-not-permitted`.
15. OH8: a `MarketplaceTransferInstructed` RELEASE replayed with the same idempotency key releases once; a RELEASE for a line under an open dispute is refused.
16. LDC: a `ServiceOrderRouted` without a buyer consent reference is rejected; LDC emits `ServiceOrderStatusChanged` on each fulfilment status change.
17. EQ/LDC/OH: no adapter in any companion product calls LawDocs as an eSign provider; signing requests are created only through the hosted hand-off.

## X.24 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-X-01 | One or two LawDocs selling entities (SaaS vs services) | [OWNER] / Company Secretary | Single entity, two invoice series |
| OI-X-02 | Production-grade Free/Personal accounts and Business trials (deviation from OH8.9) | [OWNER] + OH product head | Business trials as sandboxes; Free/Personal unchanged (vault product) |
| OI-X-03 | LOCAL billing adapter if OH8 is not live for P17 | CTO | Delay paid plans; Free tier only |
| OI-X-04 | Microsoft 365 SKU held; Intune availability (CH-29) | [OWNER] | Design for Business Standard without Intune |
| OI-X-05 | Single vault per client when LDC is present | [OWNER] + LDC product head | LawDocs `cvl` disabled for LDC-connected tenants |
| OI-X-06 | Affiliated advocates' firm structure for reserved services | [COUNSEL] | Engaged panel advocates under direct engagement terms only |
| OI-X-07 | Grievance ownership split (LawDocs desk vs OH6 mirror) | [OWNER] + [COUNSEL] | LawDocs desk owns all user grievances |
| OI-X-08 | Adobe Express scheduling API availability | Marketing ops [VERIFY] | Manual scheduling with recorded reference |
| OI-X-09 | Consumer Help entity incorporation, brand and domain | [OWNER] | `chp.brand.enabled` stays OFF |
| OI-X-10 | Ecosystem Spec v1.2 acceptance of the new contracts in X.22 | Spec owner | REST polling via `int` with local outbox |
