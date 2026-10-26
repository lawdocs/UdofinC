# Appendix Z — Customer Feedback, Reverse Engineering and Improvement Backlog *(v1.1)*

> **New in v1.1 (25 October 2026).** Reference and binding appendix. §Z.1–§Z.8 are reference (evidence and analysis); **§Z.9 (Improvement Backlog) is binding** — each `IMP-nnn` item is a requirement for the target file named, applied by the v1.1 editors and verified at that phase's exit gate. Owner instruction of 25 Oct 2026: *"Explore other GRC platforms, client feedbacks, try to reverse engineer the existing products … improve the logics, make the workflow faster, include the customizations."*
>
> **Rules of use.** Review data is self-reported, often small-sample and sometimes dated; vendor and competitor blogs (Sprinto, 6clicks, ZenGRC comparison pages) are partisan and are used only to locate primary reviews. Nothing here is copied from proprietary products: patterns are described, not reproduced (NN-19; Appendix R preamble). Any statement about a named competitor used in marketing must first pass the Claims Register.

---

## Z.1 Method

| Step | What was done |
|---|---|
| 1. Review mining | Ratings and review text read on Capterra (global and country sites), G2, Gartner Peer Insights, TrustRadius-derived aggregates (rfp.wiki), SaaSworthy, Software Advice/GetApp, Techjockey and SoftwareSuggest, plus competitor-curated summaries of G2/Capterra/Reddit/AWS Marketplace reviews. Accessed 25 Oct 2026. |
| 2. Help-centre and developer-doc reading | Vanta developer docs (tests → controls → frameworks model) and help centre (compliance-program import agent); LogicGate help centre (application/workflow/step/field builder); ServiceNow product docs (Now Assist for IRM agentic workflows; Regulatory Change Management); Secureframe support (AI capability overview). |
| 3. Release and press analysis (2025–26) | Vanta AI Agent; Drata MCP server (Jun 2025) and VRM AI agent (Aug 2025); Secureframe Comply AI; MetricStream AiSPIRE and 2026 agent statements; Diligent AuditAI and Smart Prep 360 (Mar 2026); AuditBoard → **Optro** rebrand (Mar 2026) and AI scoping memos; LogicGate AI agents (2026); OnFinance ComplianceOS/NeoGPT (Sep 2025); Thomson Reuters CoCounsel scale-up (Feb 2026). |
| 4. Implementation-method reverse engineering | TeamLease RegTech's published three-phase method (business discovery → applicability assessment → implementation) and its numbers; Lexplosion's buyer criteria; Lawrbit capability statements (Appendix R §R.2.1). |
| 5. Synthesis | Feedback coded into 14 pain-point families (§Z.3), mapped to capabilities (§Z.4), turned into click budgets (§Z.5), customisation patterns (§Z.6), AI landscape (§Z.7) and 140 backlog items (§Z.9). |

**Confidence grading used below:** **A** = large sample on an independent review site (≥ 100 reviews) or primary vendor documentation; **B** = independent review site with 10–99 reviews or several consistent sources; **C** = small sample (< 10), dated (pre-2023) or competitor-curated.

---

## Z.2 Per-product feedback synthesis

### Z.2.1 Indian compliance tools

| Product | Signal (source, date, grade) | What users like | What users dislike / switching reasons | LDC implication |
|---|---|---|---|---|
| **Lexplosion Komrisk** | Capterra 4.0/5, 15 reviews (Ease of use 3.9, Customer service 4.7); reviews 2019–Sep 2022 (C) | Responsive, hands-on support (most cited); timely reminders and alerts; regular law-change updates with plain-language consequences; broad library "under one umbrella"; affordability | Limited flexibility and customisation; **compliance mapping is tedious and changing one field can force remapping**; repetitive tasks must be deleted manually; hard for factory-level/less technical users; weak incident management; legal updates too long; **a task completed on time is flagged non-compliant if the reviewer approves after the due date** | Separate *date of compliance* (maker) from *date of approval* (checker) — status timeliness is judged on the maker's act date with evidence, not the approval date (IMP-031). Fast re-mapping without loss (IMP-006, IMP-012). Low-literacy "simple mode" for field users (IMP-096). |
| **LexComply** | Capterra 4.9/5, 10 reviews, mostly 2016–2022 (C); starts US$100/month flat (Basic) | "Saviour and alarm clock" regulatory updates; advance reminders; one-page compliance summary; ongoing, due-date and event-based types; management controls | Deleting completed reports one-by-one (no bulk); sometimes too detailed; browser-version dependence | Bulk housekeeping actions (IMP-050); one-page summary for management (IMP-070); summary-first update notes (IMP-024). |
| **Ricago** (Clonect) | Capterra India 5.0/5, 4 reviews 2018–2024 (C) | Broad library with custom event checklists (e.g., AGM); eases secretarial/statutory audits; labour-law reporting | Notification process could be better; **lacks international compliance for multiple countries** | Global packs are a real gap in Indian tools (Appendix Y); notification design (IMP-040–IMP-046). |
| **TeamLease RegTech** | No meaningful public review corpus found on G2/Capterra (G2 "Avantis" listing is an unrelated EAM product) (C). Published case study: automobile client — 5 SMEs × 6 weeks, 100+ Acts, 10 departments, **4,500 compliances incl. 700+ event-based**, 95 users in performer/reviewer/approver/management roles, 10 trainings; litigation module added after go-live (A for the method) | Implementation done *for* the client by SMEs; role-mapped users; real-time compliance-officer dashboards; litigation tracking | Implementation is people-heavy (6 weeks of 5 experts) | LDC's self-onboarding must compress discovery + applicability into hours with PAN/CIN pre-fill and family rules, keeping an optional "white-glove" service from the marketplace (IMP-001–IMP-005). Event-based compliances are ~15% of a large estate — the event trigger catalogue must be first-class (IMP-028). Litigation tracking is expected next to compliance (IMP-121). |
| **Aparajitha (Compfie, Simpliance)** | Techjockey: no ratings; Simpliance listed by "Xcelerate" (C). Compfie marketed as global compliance (Sri Lanka launch) | Labour and statutory depth; multi-location; vendor compliance | No public user feedback; pricing on request | Labour/contractor compliance needs vendor/contractor portals (IMP-113). |
| **Manupatra Manucomply** | SoftwareWorld: no reviews; English only; no listed API (C) | Legal-research parentage | No API; English only | LDC differentiates with open APIs/MCP (IMP-131) and Hindi + regional languages (IMP-097). |
| **Lawrbit GCMS** | G2 listing with no visible reviews; features list includes "AI Copilot" (C) | (From Appendix R) partner network, multi-geography, admin no-data-access promise | No public user corpus | Global partner-network model → Appendix Y; NN-30 trust promise. |
| **OnFinance (ComplianceOS / NeoGPT)** | Press, Sep 2025: US$4.2 m raise; customers NSE, BSE, ICICI Bank, HDFC MF; claims "> 100 hours saved per regulatory release" (B for facts, C for claims) | BFSI-specific LLM; explainability and traceability positioning | — | Regulatory-change analysis per release is the AI battleground for Indian BFSI; LDC must measure and publish (with evidence) hours saved per RBI/SEBI release (IMP-020, NN-19). |

### Z.2.2 Global GRC and assurance tools

| Product | Signal (source, date, grade) | Likes | Dislikes | LDC implication |
|---|---|---|---|---|
| **MetricStream** | Gartner Peer Insights 3.9/5, 48 ratings (75% 4–5★), reviews to Jul 2026 (B); TrustRadius 9/10 summary; pricing signals from US$75k/yr small enterprise (competitor-curated, C) | Breadth across risk, compliance, audit, policy, TPRM, regulatory change; depth for power users; role-based views | **Complex UX and steep learning curve; IT dependence to change reports and workflows**; slow load on large reports; **difficulty importing Excel into workflows**; custom reports need vendor help; long implementations | LDC's promise: breadth without a GRC admin — tenant-configurable workflows and reports (P02), Excel import that "just works" (P03/E), report builder for business users (IMP-074). |
| **ServiceNow IRM** | Gartner 4.3 (163), Capterra 4.5 (361), G2 4.4 (22), TrustRadius 4.7 (51), Trustpilot 2.0 (17) per rfp.wiki aggregation (B) | One platform with ITSM/CMDB data; audit trails; regulatory-change content; executive dashboards | Steep learning curve, heavy admin, unintuitive navigation; high TCO (operator licensing ≈ US$100–300/operator/month indicative G-Cloud figures); rigid customisation; 3–6 month implementations | "Operator vs requester" licensing is hated — LDC seat model should not charge read-only/attesting users (IMP-104). |
| **Archer** | Gartner 4.1 (small sample), critical review Sep 2026: "slow and unhelpful technical support", long contract negotiation for smaller firms (C) | Cross-module integration of GRC data | Support quality; contracting friction | Transparent self-serve pricing and SLA-backed support (P20/P22). |
| **IBM OpenPages** | Gartner 4.2 (small sample) (C) | Inexpensive to implement (per reviewer), analytics, customisable | **Board reports still exported to Excel/PowerPoint** | Board-ready packs generated natively in DOCX/PPTX/PDF (IMP-071). |
| **OneTrust** | G2 4.4 (250+), Capterra 4.3 (50+), Trustpilot 1.5 (20+) (competitor-curated, B/C); median annual spend ≈ US$10.5k (Vendr, 278 transactions, Mar 2026) | All-in-one privacy/GRC; 50+ frameworks; 200+ connectors; flexible TPRM templates; AI model inventory | Weeks of workflow configuration; modular pricing escalation ("paid for functionality we didn't need"); inflexible dashboards; post-sale support for SMBs; annual-only contracts | Configuration must be pre-baked by family packs so value lands in days (P15); clear module pricing with monthly option (P20). |
| **Vanta** | G2 4.6 (2,703); Capterra 4.2 (33), reviews 2020–Dec 2025 (A/B) | Ease of use; automation of evidence; dashboard; integrations; policy templates; Trust Center | Price for small companies; **rigid multi-year contracts, auto-renewal and refund disputes**; **notification overload / "alarm fatigue"**; learning curve; limited integrations/admin API; AI answers sometimes poor; endpoint-agent burden | Ethical renewals and cancellation (NN-44; IMP-108); alert budgets and digests (IMP-040); public API from day one (P18). |
| **Drata** | G2 4.7 (1,337): Ease of use 9.1, Setup 8.9, Admin 9.1, Support 9.5, Product direction 9.6 (A) | Support; ease of use; compliance management; integrations | Limited/unstable integrations; limited customisation; adding frameworks increases cost; ~2-month implementation (G2 average) | Cross-framework mapping so one control serves many instruments (IMP-013). |
| **Hyperproof** | SaaSworthy 4.7 (223); G2 ~4.5 (221) (B) | Easy navigation; centralised evidence; automated recurring tasks; responsive support; **in-platform messaging with auditors** | Price; report customisation; cannot delete requests after bulk-upload errors (only archive); slow evidence downloads; **each file must be marked "shared" before the auditor can download** | Undo window for bulk imports (IMP-008); auditor sharing by scope, not per file (IMP-083). |
| **ZenGRC** | Capterra 4.4 (27), reviews to Jul 2025 (B) | Intuitive; flexible controls/workflows; **cross-framework mapping**; audit evidence requests replacing email | Reporting/visualisation thin; **bulk edits require CSV export → edit → re-import**; few integrations; weak vendor-risk module; licensing tied to user counts | In-grid bulk edit with preview (IMP-047). |
| **LogicGate Risk Cloud** | G2 4.6 (191); avg implementation 4 months; ROI 14 months; perceived cost $$$$$ (A) | 30+ no-code applications; process designer; flexibility | (themes not visible) cost; implementation time | Adopt the "application/workflow/step/field" no-code model inside P02 Studio, with family templates so tenants rarely start from blank (IMP-060). |
| **Optro (formerly AuditBoard)** | Rebranded 9–10 Mar 2026; G2 4.6 (≈ 1,613–1,639) (A) | Audit, SOX, ERM, reporting; AI scoping memos and cross-audit summaries (Mar 2025); acquired FairNow (AI governance, fall 2025) | (Not captured) | AI scoping memo and cross-engagement summary for P10 (IMP-087, IMP-088). |
| **Diligent Boards / Diligent One** | Capterra 4.7 (342), G2 4.5 (497); ~2-month implementation (A) | Secure central board materials; MFA; less printing; support | **Dated/cluttered UI; navigation and dashboard customisation hard; slow large uploads; replacing a file with different page count disrupts directors' notes**; pricing steep for few users | Board portal: annotation-preserving document replace (IMP-077); fast chunked uploads (IMP-076); per-board pricing (P20). AuditAI (Mar 2026) claims audit admin time −70% (120 h → 35 h) — benchmark for P10. |
| **NAVEX PolicyTech** | Capterra 4.2 (28), Value for money 3.5, many reviews 2012–2020 (C) | Central repository; review reminders; assignment reports; search | **Workflow visibility (who holds the document now); many approval hand-offs; one e-mail per notification instead of bulk alerts**; mainly hosting, limited depth | Policy "where is it now" tracker and batched notifications (IMP-064, IMP-041). |
| **Workiva** | G2 4.5 (2,268); 4-month implementation; ROI 10 months (A) | Connected reporting (financial, ESG, SOX) | Cost ($$$$$) | Linked data in board/annual reports — numbers flow from lineage (NN-37) into DOCX (IMP-073). |
| **Riskonnect** | G2 4.3 (172); rfp.wiki sub-score pricing 3.2 (B) | Connected risk; ease of use; integrations | Admin complexity; **many tasks need multiple clicks**; thin API docs; pricing opacity | Click budgets (§Z.5); full OpenAPI catalogue (Appendix L). |
| **Secureframe** | Support docs (Comply AI) (A) | AI test remediation; evidence validation (incl. "dated within 12 months" check); risk-assessment autofill with justification; questionnaire auto-answer with stored sources; vendor-document Q&A with page citations (bulk 50 in parallel); policy writing assistant; MCP/API access | — (no formal AI approval workflow documented) | LDC must match the capabilities and **beat them on governance**: every AI fill is a labelled draft with citation and a named approver (NN-04, NN-14). |

### Z.2.3 What the reviews say in one paragraph

Buyers reward **support quality, ease of use and automation that removes evidence chasing**; they punish **implementation drag, admin dependence, alert floods, rigid workflows/reports, opaque or escalating pricing and contract traps**. Indian tools win on content and support, lose on flexibility, mapping speed and international coverage. Global tools win on depth and integrations, lose on cost, complexity and India-specific content. Nobody in the evidence combines Indian regulator depth (RBI/SEBI/IFSCA/IRDAI clause level), computation (returns, capital, ICAAP), governance (board, SS-1/SS-2) and software-plus-services at mid-market prices — LDC's lane (Appendix R §R.8).

---

## Z.3 Cross-market pain-point catalogue

| # | Pain point | Evidence (product, source) | Root cause | LDC design response (file) |
|---|---|---|---|---|
| PP-01 | **Slow, manual applicability mapping** | Komrisk "mapping is tedious; change one field → remap" (Capterra); TeamLease 6-week SME discovery (case study); Lexplosion's own buyer guide stresses "demo with your own data" | Applicability held as static lists, not rules over an entity profile | Rule-based applicability from the P15 profile with explanations; PAN/CIN pre-fill; re-evaluation is incremental and never destroys history (P15, P03, IMP-001–006) |
| PP-02 | **Alert fatigue / notification overload** | Vanta "alarm fatigue" (Capterra 2022, 2024); PolicyTech one e-mail per notification; Ricago "notification process could be better" | Event-per-email design; no budgets, no priority | Notification budget per user, smart digests, priority tiers, quiet hours, "only what changed for me" (P04, IMP-040–046) |
| PP-03 | **Evidence re-upload and chasing** | Diligent AuditAI positioning (evidence chasing); Hyperproof per-file share flag; ZenGRC evidence requests replacing e-mail | Evidence tied to one task instance | Evidence reuse across periods/instruments with validity windows; PBC-style requests with auto follow-up; scope-level auditor sharing (P04, P10, IMP-032–036, IMP-083) |
| PP-04 | **Poor Excel import / bulk edit** | MetricStream "difficulty importing Excel" (TrustRadius summary); ZenGRC CSV round-trips; Hyperproof cannot delete after bulk-upload error | Import as one-shot, no preview/diff/undo | Preview, row-level errors, diff, **undo window**, in-grid bulk edit (P03, Appendix E, IMP-007–011, IMP-047) |
| PP-05 | **Rigid workflows; IT/admin dependence** | MetricStream, ServiceNow, Riskonnect admin complexity | Workflows in code or expert-only builders | Tenant-tier workflow designer with templates, guard-rails and preview (P02, IMP-060–063) |
| PP-06 | **Weak, inflexible reporting; Excel/PowerPoint still needed** | IBM OpenPages board reports via Excel (Gartner); ZenGRC, OneTrust, Hyperproof report customisation | Fixed reports; no business-user builder | Report builder, scheduled board packs as DOCX/PPTX/PDF, saved views (P04, P06, IMP-070–075) |
| PP-07 | **Implementation time** | LogicGate 4 months; Workiva 4 months; Vanta/Drata ~2 months; ServiceNow 3–6 months; TeamLease 6 weeks | Blank-slate configuration | Family packs, self-onboarding to first value < 30 min, import of existing trackers by AI (P01, P15, IMP-001–005) |
| PP-08 | **Price opacity, module escalation, contract traps** | OneTrust modular escalation; Vanta auto-renew/refund disputes; Riskonnect "pricing opacity"; Drata "frameworks increase cost" | Quote-only pricing; multi-year lock-ins | Public prices, configurator, monthly option, clear renewal notices, self-serve cancellation (P20, NN-44, IMP-104–109) |
| PP-09 | **Learning curve; unusable for non-specialists** | Komrisk factory users; MetricStream, ServiceNow, Vanta learning curve; Diligent dated UI | Expert UI for all users | Role-specific simple modes, "i" help, guided tours, mobile-first maker flows, Hindi (P23, C, IMP-096–100) |
| PP-10 | **Timeliness mis-scored** | Komrisk: on-time completion flagged late when approval after due date | One date for completion | Separate maker act date, evidence date, approval date; timeliness rule configurable but defaulting to maker act date with valid evidence (P04, IMP-031) |
| PP-11 | **Support quality for SMBs** | OneTrust (Capterra, Trustpilot); Archer (Gartner 2026); Vanta small-business reviews | Support tiered by deal size | In-app support with SLA by plan, named RM for retainers, transparent status page (P22, P23, IMP-110–112) |
| PP-12 | **Integration gaps** | Drata/Vanta integration complaints; ZenGRC (JIRA, S3); Manucomply no API | Closed platforms | Public OpenAPI, webhooks, MCP server, connector SDK, CSV/SFTP fallback (P18, IMP-130–134) |
| PP-13 | **Board portal friction** | Diligent: slow uploads; notes lost on file replace; navigation | Document-centric, not item-centric | Agenda-item-centric packs; annotation carry-over; offline (P06, IMP-076–080) |
| PP-14 | **AI trust (hallucination, no approval trail)** | Vanta AI "performs terribly … hallucinated" (AWS Marketplace review via competitor); Secureframe evidence validation "no manual review needed" | AI output treated as final | Citations, confidence, labelled drafts, approval gates, evaluation scores visible to admins (P17, K, IMP-135–140) |

---

## Z.4 Reverse-engineered workflow patterns by capability

Patterns are described generically; each row ends with the LDC decision.

### Z.4.1 Obligation library and applicability

- **Leader pattern (Indian trackers):** expert-curated library by Act → compliance item → frequency, mapped to entity × location × department; applicability decided in a consulting phase (TeamLease: discovery interviews → applicability list by entity/sub-entity/category/equipment/establishment → user-role mapping → training → go-live).
- **Leader pattern (global, Vanta/Drata):** chain **integrations → resources → tests → controls → frameworks**; built-in tests pre-mapped to framework controls; custom tests per record; test status rolls up to every control it maps to (Vanta developer docs). A common control framework lets one control satisfy several frameworks.
- **Import pattern (Vanta agent):** upload existing control/policy/framework files → AI classifies each file and proposes a plan → user approves step by step → creates new items only (never overwrites) → unmatched columns become suggested custom fields → user chooses whether imported controls replace or sit beside defaults.
- **LDC decision:** keep the clause-level checkpoint (Appendix E) as the atomic unit **and** add a *common control* layer: tenant controls can satisfy many checkpoints across instruments and families (one evidence, many obligations) (IMP-013, IMP-014). Adopt the "plan → approve → create-only" AI import for clients' existing Excel trackers (IMP-005).

### Z.4.2 Task, evidence and maker-checker

- **Leader pattern:** performer → reviewer → approver with management view (TeamLease roles); evidence requests with reminders (ZenGRC, Hyperproof); evidence validity windows (Secureframe "dated within 12 months" check).
- **Observed failure:** approval date drives timeliness (Komrisk); per-file share flags (Hyperproof); no bulk delete (LexComply).
- **LDC decision:** three dates on every instance (act date, evidence date, approval date); evidence validity rules per checkpoint (e.g., "certificate valid ≤ 12 months", "board minutes of the period"); AI evidence pre-check produces a *sufficiency note* only (NN-14) (IMP-031–IMP-036).

### Z.4.3 Regulatory change management

- **Leader pattern (ServiceNow Now Assist for IRM):** regulatory alert → *enrichment agent* (adds context via web search) → *recommendation agent* (impacts on citations, policies, control objectives) → *task-planning agent* (action plan compared with similar past alerts) → human triage → tasks.
- **Leader pattern (OnFinance):** per-release analysis with BFSI-specific model; measured hours saved per release.
- **LDC decision:** P05 already has scan → classify → diff → impact → release; add (a) **similar-past-change retrieval** to pre-fill impact and action plans, (b) **per-release effort metric** shown to tenants, (c) a "what changed for *me*" tenant view filtered by adopted instruments, owners and open instances (IMP-020–IMP-027).

### Z.4.4 Issue and remediation

- **Leader pattern (ServiceNow):** issue action-plan agent + remediation-task agent; **Secureframe/Vanta:** remediation snippets for cloud findings.
- **LDC decision:** issue → AI-drafted action plan with owners and dates proposed from org chart and past closures → human approval → tasks; remediation library per checkpoint (IMP-055–IMP-058).

### Z.4.5 Policy lifecycle

- **Leader pattern (PolicyTech):** repository, review reminders, attestation assignments, reports on incomplete assignments. **Failure:** cannot see who holds the document now; too many hand-offs; one e-mail per notice.
- **Leader pattern (Vanta agent):** onboarding policies reads title/SLA/version and recommends controls; flags where written policy and actual system behaviour diverge.
- **LDC decision:** visible "baton" (current holder, time held, next step) on every policy; parallel review where allowed; batched notifications; **policy ↔ practice drift detection** using compliance-instance outcomes (e.g., policy says quarterly review, instances show half-yearly) (IMP-064–IMP-068).

### Z.4.6 Board portal and company secretarial

- **Leader pattern (Diligent):** secure board book, annotations, MFA, archive; AI Smart Prep 360 surfaces anomalies/repeat findings and turns them into director questions; AuditAI converts board signals to audit actions.
- **LDC decision:** agenda-item-centric pack; AI "director question prompts" from compliance, risk and audit data (labelled, cited); annotation carry-over on replacement; resolution tracking to tasks (IMP-076–IMP-082).

### Z.4.7 Audit

- **Leader pattern (Optro/AuditBoard):** AI scoping memos from risks/processes/worksteps; cross-audit executive summaries; formula-based report calculations; dashboards with actions. **Diligent AuditAI:** AI planning (audit names/entities/factors from risk profile), context-aware request lists from scope + prior year, routed follow-ups; claimed audit admin 120 h → 35 h.
- **LDC decision:** P10 adds AI scoping memo, prior-year-aware PBC request list generation, cross-engagement summary, request auto-chasing — all drafts with lineage (IMP-084–IMP-090).

### Z.4.8 Vendor / third-party risk

- **Leader pattern (Drata VRM agent, Aug 2025):** extract criteria from any questionnaire (PDF/DOCX/XLSX) → collect vendor artefacts via trust centre → score against criteria with sourced findings → leadership summary → follow-up questionnaire → auto-reassess on new responses. **Secureframe:** vendor-document Q&A with page citations, 50 questions in parallel.
- **LDC decision:** P12 TPRM adds criteria extraction, cited document review and reassessment triggers, with outsourcing-directions materiality logic kept deterministic (IMP-115–IMP-118).

### Z.4.9 Continuous control monitoring

- **Leader pattern (Vanta/Drata/Secureframe):** connectors pull resource data; tests run on schedule; failures surface on controls.
- **LDC decision:** "automated checkpoints" — checkpoints whose evidence is a machine test over ecosystem data (Finbyx/Udofin events, Microsoft 365 settings, website checks such as grievance-officer details published, KFS present), status computed and refreshed; human still attests where law requires (IMP-015–IMP-018).

### Z.4.10 Integrations and AI access

- **Leader pattern:** Drata MCP server (Jun 2025, permission-scoped, read/write per account rights); Secureframe MCP/API access.
- **LDC decision:** LDC exposes an **MCP server** (tenant-scoped tools: list obligations, due items, evidence status, draft a task) and remains permission-bound (NN-41); public REST + webhooks (IMP-131).

---

## Z.5 Click budgets — top 20 journeys (binding targets for C and the phase files)

"Clicks" = deliberate user actions (click, keyboard command, confirm) after landing on the starting screen; typing in a field counts as one action per field. Times are for a trained user at p50 with seeded data. Benchmarks are inferred from review complaints and vendor claims, not measured in competitor products.

| # | Journey | Starting point | LDC target clicks | LDC target time | Notes / pattern used |
|---|---|---|---|---|---|
| J-01 | Self-onboard to first compliance instance | Health-check report "Start trial" | ≤ 12 | ≤ 10 min | PAN/CIN pre-fill, family pack suggestion, default owners by department |
| J-02 | Adopt an instrument from the catalogue | Regulation Catalogue | ≤ 3 | ≤ 1 min | Checkbox → impact preview → confirm |
| J-03 | Maker submits a routine checkpoint with evidence | Work Inbox item | ≤ 4 | ≤ 90 s | Drag-drop evidence, AI sufficiency note, "Submit & next" |
| J-04 | Checker reviews and approves | Work Inbox (review) | ≤ 2 per item | ≤ 60 s | "Review next" with evidence preloaded (NN-46) |
| J-05 | Reallocate an overdue item | Item drawer | ≤ 3 | ≤ 30 s | Suggested assignee from workload and backup owner |
| J-06 | Import a question sheet (platform) | Content Studio | ≤ 5 to preview | ≤ 3 min for 300 rows | Preview, row errors, diff |
| J-07 | Edit a checkpoint for my company (overlay) | Checkpoint page | ≤ 3 | ≤ 1 min | Inline edit, reason, side-by-side base vs overlay |
| J-08 | Read a regulatory update and accept impact | Updates inbox | ≤ 4 | ≤ 3 min | "What changed for me" summary; one-click create impact tasks |
| J-09 | Create board meeting from template with agenda auto-filled | Governance › Meetings | ≤ 6 | ≤ 5 min | Agenda from due items and standing items |
| J-10 | Generate minutes draft and send for review | Meeting page | ≤ 3 | ≤ 2 min (excl. AI time) | Vidhi draft → SS-1 checks → review route |
| J-11 | Publish policy revision for approval | Policy page | ≤ 4 | ≤ 3 min | Vidhi redline vs previous version |
| J-12 | Raise and assign an issue from a failed checkpoint | Instance drawer | ≤ 3 | ≤ 1 min | AI-proposed action plan (draft) |
| J-13 | Run a stress scenario from library | Risk Lab | ≤ 5 | ≤ 2 min (excl. compute) | Scenario defaults by family |
| J-14 | Prepare a return from uploaded TB + loan dump | Return Studio | ≤ 8 | ≤ 15 min | Saved mappings reused |
| J-15 | Share an audit scope with an external auditor | Audit engagement | ≤ 4 | ≤ 2 min | Scope-level sharing, time-boxed |
| J-16 | Board pack export (DOCX/PDF) | Reports | ≤ 3 | ≤ 1 min | Scheduled packs |
| J-17 | Add a user from HRMS with role | Settings › Users | ≤ 4 | ≤ 1 min | Person picker from HRMS; role templates |
| J-18 | Change a department name and its owners | Settings › Organisation | ≤ 4 | ≤ 2 min | T-tier, audited, instant |
| J-19 | Full export to OneDrive | Settings › Data | ≤ 4 | ≤ 1 min to start | Saved target |
| J-20 | Answer a regulatory question with citations | Vidhi | ≤ 2 | ≤ 30 s | Notebook auto-selected by adopted packs |

**Measurement:** instrument each journey with product analytics events (`journey.start`, `journey.complete`, click count, time) in the demo tenant and in production (aggregated, no PII); P24 gate checks p50/p90 against the targets; a regression of > 20% blocks release of the offending screen (IMP-101).

---

## Z.6 Customisation patterns (what leaders offer, what LDC adopts)

| Pattern | Seen in | LDC adoption (P02 / Appendix U) |
|---|---|---|
| **No-code applications** (application → workflow → steps → fields → records; draft vs live) | LogicGate (help-centre structure) | P02 "Custom Registers": tenants create custom registers (e.g., licence register, insurance-policy register) with fields, steps, roles, draft/live versions and build audit log (IMP-060) |
| **Custom fields and suggested fields on import** | Vanta agent (unmatched columns → custom fields) | Excel/CSV imports propose custom fields for unknown columns, tenant-tier (IMP-009) |
| **Custom controls and custom tests** | Vanta (custom tests immutable; copy to change) | Tenant controls; automated checkpoints use versioned, immutable rule definitions — "copy to change" keeps audit integrity (IMP-016) |
| **Formula fields / calculated columns** | Optro reporting (formula-based calculations) | Report builder supports formula columns with a safe expression language (CEL) (IMP-074) |
| **Workflow designer with templates** | ServiceNow, LogicGate, MetricStream | Approval-chain designer with SoD guard-rails, templates per family, preview and simulation (IMP-061) |
| **Role dashboards and widget catalogue** | Diligent One, ServiceNow | Already in Appendix C; add "copy dashboard to role" and tenant-shared dashboards (IMP-075) |
| **Multi-entity workspaces** | Vanta Workspaces (setup heavy), Lawrbit multi-entity | Group view with entity switcher; group-level obligations rolled down; consolidated reports (IMP-091) |
| **Terminology and menu customisation** | Most enterprise suites (admin-heavy) | T-tier, already in P02 — add live preview and per-role menu hiding (IMP-062) |

---

## Z.7 AI feature landscape 2025–2026 and LDC stance

| Capability | Who ships it (date, source) | LDC must… | Guard-rail |
|---|---|---|---|
| Cited Q&A over the tenant's compliance environment | Vanta AI Agent (2025, product blog Dec 2025); Secureframe KB search | **Match** via Vidhi notebooks over regulations *and* tenant data | NN-06 citations; tenant scoping |
| Evidence validation / sufficiency check | Vanta; Secureframe (incl. 12-month date check) | **Beat**: per-checkpoint sufficiency rules (Appendix E col. U) + AI note + checker decision | AI note never sets status (NN-14) |
| Policy onboarding → control recommendations; policy–practice drift | Vanta | **Beat** using instance outcomes as "practice" signal | Draft only |
| Questionnaire auto-answer with stored sources | Secureframe, Vanta | **Match** for client due-diligence questionnaires (banks auditing NBFCs, co-lending partners) | Answers cite tenant documents |
| Vendor document review and scoring | Drata VRM agent (Aug 2025); Secureframe | **Match** in P12 TPRM | Materiality decision deterministic |
| Regulatory alert enrichment, impact and action planning | ServiceNow Now Assist for IRM | **Beat** with Indian clause-level content and similar-past-change retrieval | Release still human-approved (NN-34) |
| Risk suggestion for entities | ServiceNow risk suggestion agent; Secureframe risk autofill with justification | **Match** in P08 | Labelled draft, justification stored |
| Audit scoping memo; cross-audit summary; request lists | Optro (Mar 2025); Diligent AuditAI (Mar 2026) | **Match** in P10 | Lineage for every number (NN-37) |
| Board materials anomaly surfacing → director questions | Diligent Smart Prep 360 (Mar 2026) | **Match** in P06 | Board-confidential class (NN-13) |
| MCP server to expose GRC data to customer AI tools | Drata (Jun 2025); Secureframe | **Match** in P18 | Account-scoped permissions (NN-41) |
| Domain-specific BFSI LLM | OnFinance NeoGPT (Sep 2025) | Do not train own model; use routed frontier models + retrieval + evaluations; reconsider only with evidence | NN-15 |
| AI governance module (AI inventory, risk) | OneTrust; LogicGate AI agents (2026); Optro via FairNow | **Add** an AI-governance pack for clients (see Appendix AA, stream G3) | — |

**Market lesson:** competitors are shipping AI fast but rarely document human approval (Secureframe's evidence check runs with "no manual review needed"). LDC's regulated-market positioning is *"AI that drafts, cites and waits for your approval"* — every AI action shows source, confidence, model route and approver in the audit trail (IMP-135–IMP-140).

---

## Z.8 How to apply the backlog

1. Each item names one **target file**; the v1.1 editor of that file implements it in place, marks the text *(v1.1, IMP-nnn)*, registers any new settings/screens/events/tests in that phase's sections, and adds the acceptance measure to §12 of the phase file.
2. **Priority:** **Must** = in the phase's v1.1 exit gate; **Should** = in the phase scope, may slip one release with owner approval; **Could** = recorded as an option behind a flag.
3. **Effort:** S ≤ 1 sprint-week of one squad, M ≤ 1 sprint, L > 1 sprint.
4. Items never override an NN rule. Where an item touches AI, NN-04, NN-14, NN-37 and NN-41 apply; where it touches statutory dates, NN-33 applies.
5. Grouping below is by target file; `_contrib/v11/G2_backlog_by_file.md` repeats it for the editors.

---

## Z.9 Improvement backlog (binding) — 142 items

### Z.9.1 P01 Identity, Tenancy, Onboarding and Access

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-001 | Applicability discovery takes weeks of consultant interviews | TeamLease case study (5 SMEs × 6 weeks) | Onboarding wizard asks ≤ 12 profile questions (family, type, layer/tier, size bands, listing, States, activities, customer interface), pre-filled from PAN/CIN/GSTIN and health-check answers, and produces the applicable pack list with "why it applies" | Must | M | J-01 ≤ 12 clicks / ≤ 10 min; ≥ 90% of pilot tenants accept the suggested packs without removal of a mandatory pack |
| IMP-002 | Users fear wrong applicability | Komrisk mapping complaints | Show an **applicability explanation card** per instrument and per checkpoint ("applies because: NBFC-ML, customer interface = yes"); one-click "challenge applicability" creates a review task for the CCO | Must | S | Every adopted checkpoint has a machine-generated reason string |
| IMP-003 | Large estates need discovery help | TeamLease method | Optional **guided discovery call** bookable from the wizard (marketplace "implementation" SKU) that pre-fills the same profile — software first, service optional | Should | S | Booking available in wizard; profile edits by RM recorded as delivery-grant actions |
| IMP-004 | Trial users stall after sign-up | Vanta/OneTrust setup time complaints | **First-value checklist** (5 steps, progress ring): adopt packs → assign owners → import existing tracker → complete one checkpoint → invite checker | Must | S | ≥ 60% of trials complete 3/5 steps within 48 h |
| IMP-005 | Existing trackers (Excel) must be re-keyed | Vanta compliance-program import agent pattern | **AI tracker import**: upload any compliance tracker; Vidhi classifies sheets, proposes mapping to LDC checkpoints/overlays/custom fields, user approves step by step; create-only, never overwrite (NN-04) | Must | M | A 500-row legacy tracker maps ≥ 80% rows automatically in pilot; zero silent overwrites (test) |

### Z.9.2 P03 Regulatory Content Library, Template Registry and Excel Import

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-006 | Changing a profile field forces remapping and loses work | Komrisk (Capterra) | **Incremental re-evaluation**: profile change produces a diff (added/removed/changed checkpoints) with preview; removals keep history (NN-29); owners and overlays carry over by `obligation_ref` | Must | M | Changing layer BL→ML shows diff and preserves all completed instances |
| IMP-007 | Excel import into workflows is hard | MetricStream (TrustRadius summary) | Importer always shows preview, row errors with cell links, and a semantic diff against the current version before commit | Must | M | 300-row sheet → preview in ≤ 10 s |
| IMP-008 | Bulk-upload mistakes cannot be deleted | Hyperproof (SaaSworthy) | **Undo window** (default 24 h, T-tier 1–72 h) for any import or bulk change: one click reverts the batch through a compensating Correction Entry batch | Must | M | Undo restores pre-import state, ledger shows both entries |
| IMP-009 | Unknown columns are dropped | Vanta import agent | Unknown columns in tenant imports become **suggested custom fields** (tenant tier) instead of errors | Should | S | Unknown column → suggestion card |
| IMP-010 | Multi-instrument workbooks rejected | Owner's practice (one sheet per MD) | Accept workbooks with several family-template sheets; each sheet validated separately against its `_Template_Info` | Should | S | 3-sheet workbook imports as 3 instruments |
| IMP-011 | Migrating from competitor tools is slow | Switching reasons (§Z.2) | **Migration adapters** for common competitor exports (CSV/XLSX of compliance registers) mapped through the AI tracker import (IMP-005) | Could | M | Two competitor export formats certified |
| IMP-012 | Obligation re-citation after consolidation is manual | RBI 28 Nov 2025 consolidation | Concordance-driven re-citation keeps checkpoint IDs stable when clause numbers change; tenant sees "re-cited, no change in actionable" vs "changed" | Must | M | Re-cited checkpoint keeps history and owner |
| IMP-013 | Same control evidenced many times | ZenGRC/Drata cross-framework mapping praise | **Common control layer**: tenant controls map to many checkpoints across instruments/families; one evidence submission satisfies all mapped instances for the period (each still reviewed where law requires) | Must | L | One KYC-policy evidence closes mapped RBI, PMLA and IFSCA checkpoints |
| IMP-014 | Duplicate obligations across overlapping instruments | Multi-regulator entities (listed NBFC) | Duplicate detector proposes "same obligation" links between checkpoints (similar text + same authority/topic); content checker confirms | Should | M | Precision ≥ 0.8 on golden pairs |

### Z.9.3 P04 Compliance Workspace — automated checkpoints, tasks, evidence, notifications, issues, reporting

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-015 | Evidence is always manual | Vanta/Drata test model | **Automated checkpoints**: a checkpoint may carry a machine test (rule over ecosystem/connector data) that refreshes status and attaches evidence snapshot | Must | L | 10 automated checkpoints live for NBFC pack (e.g., grievance officer on website, KFS published, DLG disclosure monthly) |
| IMP-016 | Test logic edits break audit trail | Vanta custom tests immutable | Automated-test definitions are versioned and immutable; "copy to change" | Must | S | Edit attempt creates new version |
| IMP-017 | Tests fail silently on data gaps | Integration complaints | Test status includes `INVALID` / `NO_DATA` distinct from fail; data-gap tasks to integration admin | Must | S | Disconnected source shows NO_DATA, not FAIL |
| IMP-018 | Humans still need to attest | Regulatory reality | Automated results feed a human attestation where the checkpoint requires it (flag `requires_attestation`) | Must | S | Attestation step present for flagged checkpoints |
| IMP-028 | Event-based compliances get missed (≈ 15% of estates) | TeamLease 700/4,500 event-based | **Event trigger catalogue** (appointment, resignation, change in shareholding, new branch, breach, fraud detection, change in KMP, new product, new outsourcing) wired to HRMS, governance, Finbyx events and manual "log event" button; each trigger spawns all linked event checkpoints with computed due dates | Must | M | Logging "director appointed" creates DIR-12, MBP-1 index, fit-and-proper and RBI intimation instances |
| IMP-029 | Work piles on absent users | PolicyTech hand-offs | Leave-aware routing: when HRMS shows leave, items route to the backup owner automatically (never to the maker for checks) | Must | S | Leave → backup within 1 min |
| IMP-030 | Workload imbalance | General | Workload view with suggested reassignment (count × risk × due) | Should | S | Suggested assignee shown in J-05 |
| IMP-031 | On-time work scored late when approval is late | Komrisk (Capterra) | Three dates: **act date** (maker, with evidence), **evidence date**, **approval date**; timeliness default = act date ≤ due date and evidence accepted; tenant may choose stricter rule (G-tier) | Must | S | Test: approval after due date does not flip to `complied_late` when act date ≤ due |
| IMP-032 | Evidence re-uploaded every period | Evidence-chasing pain | **Evidence reuse** with validity windows: valid evidence can be linked to the next period's instance with one click; system blocks reuse beyond validity | Must | M | Reuse link records source instance |
| IMP-033 | Weak evidence accepted | Secureframe date check | Per-checkpoint **evidence rules** (type, issuer, date window, signature present, period match) evaluated deterministically before AI note | Must | M | Rule failures shown to maker before submit |
| IMP-034 | Chasing documents by e-mail | ZenGRC/Diligent | **Request lists** (PBC-style) inside compliance work: request → owner → due → automatic reminders → upload portal (also for external parties via secure link) | Must | M | External upload link expires; uploads land on instance |
| IMP-035 | Checkers re-read everything | AI evidence check | AI **sufficiency note** (matches expected evidence? period? signatory?) displayed to checker, never setting status | Must | S | Note shown with citation to document page |
| IMP-036 | Evidence arrives by e-mail | Practice | **E-mail-in per instance** (unique address) and forward-to-LDC parsing with attachment classification | Should | M | Forwarded mail attaches to right instance ≥ 90% |
| IMP-037 | Snooze abuse vs genuine waiting | Alert fatigue | "Waiting on" with named party and follow-up date; internal SLA paused only (NN-33) | Must | S | Statutory date unchanged |
| IMP-038 | No single "my day" | Usability | **My Day** view: today's due, waiting on me, blocked, quick wins | Should | S | J-03 starts from My Day |
| IMP-039 | Field users struggle | Komrisk factory users | **Mobile maker flow** (PWA): camera capture, offline queue, Hindi/regional labels | Should | M | Submit evidence offline, syncs later |
| IMP-040 | Alarm fatigue | Vanta (Capterra) | **Notification budget** per user (default 10 immediate/day); excess folded into digest; priority tiers (Critical/High/Normal/Info) | Must | M | Budget enforced; Critical never folded |
| IMP-041 | One e-mail per notice | PolicyTech | Batched notifications: same type and target grouped into one message with list | Must | S | 20 assignments → 1 e-mail |
| IMP-042 | Irrelevant alerts | Vanta | "Only what changed for me": subscriptions by instrument, entity, department; mute per thread | Must | S | Mute honoured; audit of mutes |
| IMP-043 | Reminders not escalating smartly | Lexplosion buyer guide | Escalation ladder adapts to risk (High risk: earlier and to dept head) — G-tier template, T-tier tuning above floors | Must | S | Ladder differs by risk |
| IMP-044 | Notification channels fragmented | General | Channel preferences (in-app, e-mail, Teams, WhatsApp opt-in, SMS for Critical) per type | Should | S | Preferences matrix saved |
| IMP-045 | Weekend/holiday noise | General | Quiet hours and holiday calendar respected (narrow only; Critical overrides) | Should | S | No non-critical sends in quiet hours |
| IMP-046 | No measure of fatigue | — | Alert-health metric per tenant (notifications per user per day, open rate) with recommendations | Could | S | Dashboard tile |
| IMP-047 | Bulk edits require CSV round trip | ZenGRC | **In-grid bulk edit** (owners, internal dates, tags) with preview and undo (IMP-008) | Must | M | 200 rows edited in ≤ 2 min |
| IMP-048 | Saved filters lost | Usability | Saved views shareable to role/department | Should | S | View shared to role |
| IMP-049 | Bulk actions unsafe | NN-46 | Bulk restricted to non-legal-effect actions; legal-effect items use Review next | Must | S | NN-46 tests |
| IMP-050 | Housekeeping one by one | LexComply | Bulk archive/close of completed reports and obsolete drafts | Should | S | Multi-select archive |
| IMP-051 | Recurring tasks duplicated manually | Komrisk "repetitive tasks deleted manually" | Recurrence engine owns series; ending a series removes only future instances, with confirmation (NN-29) | Must | S | End series keeps history |
| IMP-052 | No dependency between checkpoints | Practice (policy before attestation) | Dependencies: "blocked until checkpoint X complied" with visual chain | Should | M | Blocked items show blocker |
| IMP-053 | Comments lost in e-mail | Hyperproof messaging praise | Threaded comments with @mentions on every instance, visible to auditors per scope | Must | S | Mention notifies |
| IMP-054 | Status vocabulary differs per team | — | Canonical statuses with tenant labels (exists) + **status explainers** ("i") | Must | S | Labels mapped |
| IMP-055 | Issues stall | ServiceNow issue agents | AI-drafted **action plan** for issues (steps, owners suggested from org chart, dates) — approved by issue owner | Must | M | Draft labelled; approval logged |
| IMP-056 | Remediation reinvented each time | Secureframe remediation | Remediation library per checkpoint (typical fixes, templates, evidence) | Should | M | Library entries for top 100 NBFC checkpoints |
| IMP-057 | Repeat findings unseen | Diligent Smart Prep | **Repeat-issue detection** across periods/audits flagged to CCO and board pack | Must | S | Same root cause twice → flag |
| IMP-058 | Issues closed without proof | Audit practice | Closure requires validation evidence and, for High issues, independent validator | Must | S | High issue cannot self-close |
| IMP-070 | Management wants one page | LexComply praise | **One-page compliance summary** per entity/period (score, overdue, high-risk open, upcoming 30 days) | Must | S | PDF in ≤ 5 s |
| IMP-071 | Board reports built in Excel/PPT | IBM OpenPages review | Native **board pack generator** (DOCX/PPTX/PDF) from saved report templates | Must | M | Pack generated without leaving LDC |
| IMP-072 | Reports not reproducible | Audit needs | Every report stores parameters and data snapshot hash; "re-run as at" | Must | S | Re-run equals original |
| IMP-073 | Numbers typed into narrative | Workiva linked data | Linked numbers in DOCX narratives update from lineage (NN-37) | Should | M | Changing source updates draft before approval only |
| IMP-074 | Report customisation needs vendor | MetricStream, ZenGRC, OneTrust | Business-user **report builder** (fields, filters, groupings, charts, formula columns in CEL), shareable templates | Must | L | CCO builds custom report without support |
| IMP-075 | Dashboards rebuilt per user | Diligent dashboard complaints | Copy dashboard to role/department; tenant dashboard library | Should | S | Copy function |

### Z.9.4 P05 Regulatory Change Management and AI Question Authoring

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-019 | Updates arrive without context | ServiceNow enrichment agent | Enrichment step attaches source PDF, prior version, related FAQs, press release and linked consultations to each update before review | Must | M | Every update card shows ≥ 1 linked context item or "none found" |
| IMP-020 | No measure of effort saved | OnFinance "100+ hours per release" claim | Per-release metrics: checkpoints affected, minutes of reviewer time, tenant impact tasks closed — shown internally and, after Claims Register approval, publicly (NN-19) | Should | S | Metrics recorded per release |
| IMP-021 | Impact analysis starts from scratch | ServiceNow task-planning agent (similar past alerts) | **Similar-past-change retrieval** pre-fills impact mapping and action plan from analogous earlier releases | Must | M | Pre-fill shown with "based on" links |
| IMP-022 | Tenants flooded with irrelevant updates | Alert fatigue | Tenant Updates filtered to adopted instruments and families; "not applicable to you" items in a collapsed section | Must | S | Non-adopted updates collapsed |
| IMP-023 | "What changed" unclear | Owner brief R-006 | Three-pane view: previous text / new text / actionable diff, with "what to do" and due date for the tenant | Must | S | Shown for every changed checkpoint |
| IMP-024 | Update notes too long | Komrisk "updates could be more concise" | Summary-first notes: 3-line gist (labelled AI draft until reviewed) + expandable detail | Must | S | Gist ≤ 60 words |
| IMP-025 | Impact tasks created one by one | — | "Accept impact" creates all impact tasks (owners from department map) in one action with preview | Must | S | J-08 ≤ 4 clicks |
| IMP-026 | Missed changes during outages | Source reliability | Source health dashboard with freshness SLA breaches raising platform incidents; back-fill scan on recovery | Must | S | Missed window back-filled |
| IMP-027 | AI-authored question drafts uneven | Quality | Authoring Studio scores each draft row against the Part-2 QA checklist (citation present, one actionable, evidence named) before human review | Must | M | Row score visible; rows failing hard checks cannot be approved |

### Z.9.5 P02 Configuration Studio, Rule Engine and Settings

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-059 | Admin dependence for small changes | MetricStream/ServiceNow | Settings search ("type what you want to change") with direct link to the setting and its tier | Must | S | Search returns setting in ≤ 1 s |
| IMP-060 | Need registers the product lacks | LogicGate no-code apps | **Custom Registers** builder: fields, steps, roles, draft/live versions, build audit log, export mapping auto-registered (NN-10) | Must | L | Tenant builds an "insurance policies register" without code |
| IMP-061 | Workflow changes risky | ServiceNow rigidity | Approval-chain designer with SoD guard-rails, **simulation** ("run last month's items through the new chain") before publish | Must | M | Simulation report before activation |
| IMP-062 | Menus cluttered | Diligent dated UI | Per-role menu hiding/reordering with live preview (T-tier) | Should | S | Preview before save |
| IMP-063 | Configuration hard to reuse across group entities | Multi-entity | Configuration templates: copy settings from entity A to B with diff | Should | S | Diff shown, applied atomically |

### Z.9.6 P07 Policy Lifecycle and Document Management System

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-064 | Nobody knows who holds the policy now | PolicyTech (Capterra) | **Baton tracker**: current holder, time held, next step, SLA, nudge button | Must | S | Visible on policy and in Work Inbox |
| IMP-065 | Serial hand-offs slow approval | PolicyTech | Parallel review lanes where independence is not required; consolidated comments | Must | S | Parallel lanes configurable |
| IMP-066 | Policy says one thing, practice another | Vanta drift flag | **Policy–practice drift** detection: policy clauses tagged to checkpoints; instance outcomes contradicting policy (frequency, owner, threshold) raise a review item | Should | M | Drift item created on golden case |
| IMP-067 | Attestation chasing | PolicyTech reports | Attestation campaigns with quizzes, reminders, completion dashboards by department | Must | S | Campaign report |
| IMP-068 | Policy ↔ control link manual | Vanta policy onboarding | On upload, Vidhi extracts title, owner, review cycle, version and proposes control/checkpoint links (draft) | Should | M | Proposal accepted/rejected per link |
| IMP-069 | Large PDFs slow to open | Diligent | Progressive rendering and text-layer check for all uploads | Should | S | First page < 2 s for 100-page PDF |

### Z.9.7 P06 Governance, Board, Committees and Company Secretarial

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-076 | Slow large uploads | Diligent (Capterra) | Chunked resumable uploads with background conversion | Must | S | 200 MB upload resumes after network drop |
| IMP-077 | Directors lose notes when a paper is replaced | Diligent (Capterra) | **Annotation carry-over**: replacing a paper re-anchors notes by text matching; unmatched notes kept in a side list | Must | M | ≥ 90% notes re-anchored on golden pair |
| IMP-078 | Board materials hard to navigate | Diligent | Agenda-item-centric navigation with "what's new since last view" markers | Must | S | Unread markers per item |
| IMP-079 | Directors miss key issues | Diligent Smart Prep 360 | **Director question prompts**: AI-drafted, cited questions from overdue High checkpoints, repeat findings, KRI breaches, audit observations — CS reviews before release | Should | M | Prompts cite source records |
| IMP-080 | Offline reading needed | Board practice | Encrypted offline pack with remote wipe | Could | M | Wipe test |
| IMP-081 | Resolutions not followed up | Practice | Every decision/action in minutes becomes a tracked task with owner and due date; status reported at next meeting automatically | Must | S | Action-taken report generated |
| IMP-082 | Agenda built manually | Practice | Agenda auto-suggested from standing items, due approvals (policies, returns, ICAAP), committee recommendations | Must | S | J-09 ≤ 6 clicks |

### Z.9.8 P10 Audit Management

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-083 | Auditor access per file | Hyperproof (SaaSworthy) | **Scope-level sharing**: share an engagement scope (instruments, periods, entities) once; all in-scope evidence visible, time-boxed | Must | S | J-15 ≤ 4 clicks |
| IMP-084 | Audit admin heavy | Diligent AuditAI (−70% claim) | Request list generator from scope + prior-year requests + risk; auto-chasing; status board | Must | M | Request list drafted in < 1 min |
| IMP-085 | Auditors re-request evidence already in LDC | Evidence-chasing pain | Auto-link existing compliance evidence to audit requests where it matches | Must | S | Match suggestions with accept/reject |
| IMP-086 | Planning from scratch | AuditAI planning | Audit universe and plan suggestions from risk register, prior findings and regulatory requirements (RBIA) — draft | Should | M | Plan draft with rationale |
| IMP-087 | Scoping memo authored manually | Optro AI scoping memos | AI scoping memo draft from risks, processes and work steps | Should | S | Draft editable, labelled |
| IMP-088 | Cross-audit insight missing | Optro cross-audit summaries | Cross-engagement executive summary for audit committee | Should | S | Summary with links |
| IMP-089 | Findings not linked to compliance | Silos | Findings create or link to compliance issues and checkpoints; closure flows back | Must | S | Bidirectional link |
| IMP-090 | Workpaper sign-off unclear | Audit practice | Preparer/reviewer sign-off with lock and review notes per workpaper | Must | S | Locked after review |

### Z.9.9 P15 Sector Packs and P00 Foundations — multi-entity and group

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-091 | Multi-entity setup heavy | Vanta Workspaces (competitor note) | Group hierarchy with entity switcher; group-level policies rolled down; consolidated reports | Must | M | Group of 5 entities set up in < 1 h |
| IMP-092 | Same person in many entities | Group practice | Person master shared across group entities (one login, entity-scoped roles) | Must | S | One identity, roles per entity |
| IMP-093 | Locations/branches not modelled | TeamLease establishment mapping | Establishment/branch register with State attributes driving labour and shop-establishment packs | Must | M | Adding a Rajasthan branch adds its pack |
| IMP-094 | Pack defaults not explained | — | Family pack "what you get" page (instruments, departments, committees, calendars) before adoption | Should | S | Page per family |
| IMP-095 | International subsidiaries unsupported | Ricago review | Entity jurisdiction attribute enables jurisdiction packs (Appendix Y) | Must | S | Foreign subsidiary entity creatable |

### Z.9.10 P23 Public Website, Help and Accessibility; Appendix C UX

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-096 | Non-specialist users struggle | Komrisk factory users | **Simple mode** per role: only My Day, submit, camera, help; hides advanced menus | Must | S | Toggle per user/role |
| IMP-097 | English-only tools | Manucomply, most competitors | Hindi UI for maker/checker flows and help; regional languages for co-operatives (with D-30) | Should | M | Hindi coverage of top 20 screens |
| IMP-098 | Learning curve | Vanta/MetricStream | Contextual 60-second videos and interactive tours per screen | Must | S | Tour on first visit |
| IMP-099 | Help separate from work | — | "i" help shows the regulation snippet and plain-language explainer inline | Must | S | Help keys on all screens |
| IMP-100 | Search fragmented | — | Global search across checkpoints, documents, meetings, people, settings with filters | Must | M | p95 < 800 ms |
| IMP-101 | UX regressions undetected | Riskonnect "many clicks" | Journey analytics and click-budget gate (§Z.5) | Must | S | P24 gate checks |
| IMP-102 | Dated UI perception | Diligent, Vanta | Design-system refresh with density modes (comfortable/compact) | Should | S | Density toggle |
| IMP-103 | Keyboard power users | — | Keyboard shortcuts for review flows (A approve, R return, N next) with remapping (WCAG 2.1.4) | Should | S | Shortcuts remappable |

### Z.9.11 P20 Pricing, Plans, Subscriptions, Billing, Savings

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-104 | Paying for read-only users | ServiceNow operator licensing | Seat model charges active makers/checkers/admins; viewers, attesting employees, board members, auditors free within fair-use | Must | S | Seat counter excludes free roles |
| IMP-105 | Module escalation surprises | OneTrust, Drata | Configurator shows full-year cost and renewal price; add-ons priced openly | Must | S | Renewal price shown pre-checkout |
| IMP-106 | Annual-only lock-in | OneTrust, Vanta | Monthly and annual options; annual discount explicit | Must | S | Both cycles purchasable |
| IMP-107 | Renewal surprises | Vanta disputes | Renewal reminders at 60/30/7 days with one-click change of plan | Must | S | Reminders logged |
| IMP-108 | Hard to cancel | Vanta (Capterra) | Self-serve cancellation with export reminder (NN-42, NN-44) | Must | S | ≤ 3 clicks to cancel |
| IMP-109 | ROI unproven | Buyers ask ROI | Savings dashboard cites method per figure (exists) + quarterly value report e-mail to admin | Should | S | Report generated |

### Z.9.12 P22 Service Delivery Console and support

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-110 | SMB support neglected | OneTrust, Archer, Vanta | Support SLA by plan published; in-app chat with ticket handoff to OH | Must | S | SLA visible in Settings |
| IMP-111 | Support lacks context | — | Support ticket auto-attaches screen, error code, recent actions (no PII), with tenant consent | Should | S | Context bundle on ticket |
| IMP-112 | Customers fear vendor reading data | Lawrbit "no admin data access" promise | Access transparency log page for tenants (every support/break-glass access) (NN-30) | Must | S | Page lists accesses |

### Z.9.13 P13 HRMS and Labour; P12 Data, Cyber and TPRM

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-113 | Contractor compliance invisible | Aparajitha positioning | Contractor portal: contractors upload wage registers, PF/ESI challans; principal-employer checkpoints auto-evidenced | Should | M | Contractor upload closes linked checkpoint |
| IMP-114 | Labour registers prepared by hand | Labour tools | Registers auto-generated from HRMS data per Code forms | Must | M | Register output per Appendix T |
| IMP-115 | Vendor questionnaires inconsistent | Drata VRM agent | Criteria extraction from any questionnaire file into a standard baseline | Should | M | XLSX/PDF/DOCX parsed |
| IMP-116 | Vendor docs reviewed manually | Drata, Secureframe | Cited vendor-document review (answer with page citations, bulk) | Should | M | 50 questions answered with citations |
| IMP-117 | Reassessment forgotten | Drata | Reassessment triggers: new response, expiry of certificate, incident, materiality change | Must | S | Trigger creates task |
| IMP-118 | Outsourcing materiality subjective | RBI outsourcing directions | Deterministic materiality questionnaire per directions; AI only summarises | Must | S | Materiality rule-computed |
| IMP-119 | Incident clocks mis-started | NN-33 | Incident intake records detection time source (internal, vendor) with immutable timestamp | Must | S | Clock start immutable |
| IMP-120 | Client questionnaires from banks/co-lenders | Secureframe questionnaire automation | Due-diligence questionnaire answering for tenants (draft with citations to tenant evidence) | Should | M | Draft answers cite evidence |

### Z.9.14 Litigation and legal matters (P06 governance scope or new phase if G5 confirms)

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-121 | Clients expect litigation tracking next to compliance | TeamLease (module added post go-live); Lexplosion Komlit; memory of owner's earlier module list | **Legal matters register**: notices, cases, hearings, orders with directions → tasks; consumes Ecosystem litigation events from Finbyx Recovery Suite | Must | M | Order with direction creates due task |
| IMP-122 | Regulator inspections handled ad hoc | RBI/SEBI inspections | Inspection & regulator-correspondence tracker (RBS/inspection observations → compliance plan → closure reports) | Must | M | Observation → action plan → closure |

### Z.9.15 P08 / P09 Risk

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-123 | Risk tools rigid | Vanta risk (Capterra) | Configurable risk methodology per tenant (scales, matrices, formulas) with versioning | Must | S | Methodology v2 coexists with v1 |
| IMP-124 | Risk identification blank-slate | ServiceNow risk suggestion agent | AI risk suggestions per entity/process from taxonomy and incidents (draft, justified) | Should | S | Suggestions with justification |
| IMP-125 | Risk autofill unexplained | Secureframe autofill | Every AI-filled field stores justification and source | Must | S | Justification visible |
| IMP-126 | KRIs disconnected from compliance | Silos | KRI breach can auto-open compliance issue and vice versa | Must | S | Link created |
| IMP-127 | Stress results hard to explain to board | Board practice | Narrative-ready result cards (numbers from lineage, NN-37) | Should | S | Card exported to board pack |

### Z.9.16 P11 Return Studio

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-128 | Mapping redone each period | Data-prep practice | Mapping memory: last period's mapping reused; only new codes need mapping | Must | S | Second period mapping ≥ 95% auto |
| IMP-129 | Validation errors cryptic | Return portals | Validation messages in plain language with fix suggestions and cell links | Must | S | Every rule has a plain message |

### Z.9.17 P18 Integration Gateway

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-130 | Integrations unreliable | Drata/Vanta complaints | Connector health page with last sync, errors, retries; alerts to integration admin | Must | S | Health visible per connector |
| IMP-131 | Closed platforms | Manucomply (no API); Drata MCP | Public OpenAPI + webhooks + **MCP server** exposing tenant-scoped tools | Must | M | MCP tools pass permission tests |
| IMP-132 | Admin API missing | Vanta reviewers | Admin API for users, roles, settings (scoped keys) | Must | S | Admin endpoints documented |
| IMP-133 | Jira/ITSM sync | ZenGRC | Issue sync with Jira/ServiceNow/Freshservice (bi-directional status) | Should | M | Status round trip |
| IMP-134 | Endpoint agents burdensome | Vanta | Prefer API/cloud connectors; no mandatory endpoint agent | Must | S | No agent required for core |

### Z.9.18 P17 Vidhi AI

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-135 | AI hallucination | Vanta AI (AWS review via competitor) | Answers only with retrieved citations; abstain otherwise (NN-06); confidence shown | Must | S | Eval: unsupported answer rate < 2% on golden set |
| IMP-136 | AI acts without approval | Secureframe "no manual review" | Every AI write is a draft with named approver (NN-04, NN-14) | Must | S | No AI write without approval event |
| IMP-137 | Users cannot judge AI quality | — | Per-skill evaluation scores visible to tenant admins; feedback buttons feed eval set | Should | S | Scores page |
| IMP-138 | AI cost surprises | Pricing complaints | AI credit meter with per-skill estimates before running bulk jobs | Must | S | Estimate shown |
| IMP-139 | AI cannot be switched off | Secureframe has global disable | Tenant and skill-level AI on/off and data-sharing controls | Must | S | Disable honoured |
| IMP-140 | AI work invisible in audit | Governance | AI activity log (prompt hash, sources, model route, approver) exportable (folder 18) | Must | S | Export contains log |

### Z.9.19 P24 Engineering, release and measurement

| ID | Problem | Evidence | LDC change | Pri | Eff | Acceptance measure |
|---|---|---|---|---|---|---|
| IMP-141 | Performance complaints on large reports | MetricStream, Diligent | Performance budgets per report size; async generation with notification above thresholds | Must | S | 50k-row report async < 2 min |
| IMP-142 | Feature requests disappear | ZenGRC "vendor acts on suggestions" praise | Public roadmap and in-app idea portal with status; tenants vote; links to release notes | Should | S | Idea → status visible |

---

## Z.10 Sources (accessed 25 October 2026)

- Komrisk reviews, Capterra: https://www.capterra.com/p/172823/Komrisk/reviews/
- LexComply, Capterra: https://capterra.com/p/150384/LexComply/
- Ricago, Capterra India: https://www.capterra.in/software/146346/ricago
- TeamLease RegTech case study (automobile): https://teamleaseregtech.com/case-studies/automobile-industry-regulatory-compliance
- Lexplosion buyer guide: https://lexplosion.in/?p=151538
- Simpliance listing, Techjockey: https://www.techjockey.com/detail/simpliance
- Manucomply, SoftwareWorld: https://www.softwareworld.co/software/manucomply-reviews/
- Lawrbit GCMS, G2: https://www.g2.com/products/lawrbit-global-compliance-management-solution/reviews
- OnFinance AI funding (IBS Intelligence, 29 Sep 2025): https://ibsintelligence.com/ibsi-news/onfinance-ai-raises-4-2m-to-expand-generative-ai-for-bfsi/
- MetricStream, Gartner Peer Insights likes/dislikes: https://www.gartner.com/reviews/market/integrated-risk-management/vendor/metricstream/product/metricstream-enterprise-grc-solution/likes-dislikes ; Sprinto review (competitor-curated): https://sprinto.com/blog/metricstream-review/ ; MetricStream award release (14 Jul 2026): https://www.businesswire.com/news/home/20260714989238/en/
- ServiceNow IRM aggregation: https://www.rfp.wiki/legal-compliance/servicenow-irm ; Now Assist for IRM agentic workflows: https://www.servicenow.com/docs/r/UUPLjuAXTo4SlQO8Ml6ZjQ/SSV8aIIse3GOvp4wnT3Eyw
- Archer, Gartner Peer Insights: https://www.gartner.com/reviews/market/governance-risk-and-compliance-tools-assurance-leaders/vendor/archer
- IBM OpenPages, Gartner Peer Insights: https://www.gartner.com/reviews/market/it-risk-management-solutions/vendor/ibm
- OneTrust (competitor-curated review summary): https://sprinto.com/blog/onetrust-review/
- Vanta vs Drata, G2: https://www.g2.com/compare/vanta-vs-drata ; Vanta, Capterra: https://capterra.com/p/211459/Vanta/reviews/ ; Vanta AI Agent: https://www.vanta.com/resources/how-vanta-ai-agent-transforms-compliance-work ; Vanta tests concept docs: https://developer.vanta.com/docs/concepts/tests.md ; Vanta compliance-program import: https://help.vanta.com/en/articles/11345361-bringing-your-current-compliance-program-into-vanta ; 6clicks on Vanta limitations (competitor-curated): https://www.6clicks.com/resources/blog/understanding-vantas-limitations-insights-from-real-user-experiences
- Drata MCP (12 Jun 2025): https://drata.com/blog/drata-mcp-built-for-ai-native-trust-management ; Drata VRM AI agent (5 Aug 2025): https://drata.com/about/news/drata-reveals-breakthrough-ai-agent-to-redefine-vendor-risk-management
- Secureframe AI capabilities: https://support.secureframe.com/hc/en-us/articles/49655363282323-Overview-of-AI-Capabilities-in-Secureframe
- Hyperproof, SaaSworthy: https://www.saasworthy.com/product/hyperproof/reviews
- ZenGRC, Capterra: https://capterra.com/p/157713/ZenGRC/reviews/
- LogicGate Risk Cloud, G2: https://www.g2.com/products/logicgate-risk-cloud ; help-centre application setup: https://help.logicgate.com/hc/en-us/sections/360012101812-Initial-Application-Setup
- Optro (formerly AuditBoard) rebrand: https://www.corporatecomplianceinsights.com/auditboard-rebrands-to-optro/ ; AI scoping memos (10 Mar 2025): https://optro.ai/blog/auditboard-transforms-internal-audit-with-advanced-ai-capabilities
- Diligent Boards, Capterra: https://capterra.com/p/149069/Diligent-Boards/reviews/ ; G2: https://g2.com/products/diligent-boards/reviews?page=6 ; Diligent AuditAI (10 Mar 2026): https://secure.businesswire.com/news/home/20260310277035/en/Diligent-Debuts-AuditAI-at-IIA-GAM-2026-Bringing-Early-Warning-Signals-to-Internal-Audit-and-the-Boardroom
- NAVEX PolicyTech, Capterra NZ: https://www.capterra.co.nz/reviews/20046/policytech
- Workiva, G2: https://g2.com/products/workiva-workiva/reviews?page=2
- Riskonnect aggregation: https://www.rfp.wiki/vendors/riskonnect/servicenow-irm
- Thomson Reuters CoCounsel scale-up (Feb 2026): https://www.thomsonreuters.com/en/press-releases/2026/february/one-million-professionals-turn-to-cocounsel-as-thomson-reuters-scales-ai-for-regulated-industries
