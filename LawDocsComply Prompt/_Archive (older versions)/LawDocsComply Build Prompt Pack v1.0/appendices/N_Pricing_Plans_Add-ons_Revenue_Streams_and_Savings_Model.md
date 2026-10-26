# Appendix N — Pricing, Plans, Add-ons, Revenue Streams and Savings Model

**LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Binding for P20, P21, P22, P23 (pricing page copy) · Owner of commercial values: the project owner (all figures marked `[OWNER TO SET]` are indicative seeds, not decisions)**

## N.0 Purpose, precedence and conventions

1. This appendix seeds the **presentation catalogue** (packages, components, feature rows, FAQs, explainers), the **commercial catalogue proposals** submitted to Operations Hub OH8 (SKUs, price books, coupons, trial policy), the **LawDocsComply revenue-stream registry** (RS-LDC-01…RS-LDC-30) and the **savings methodology** for the Savings Dashboard.
2. **Precedence.** OH8 is the source of truth for prices, tax, coupons, stream gates, quotes and invoices (Ecosystem Spec §6.27). Where this appendix and an approved OH8 catalogue version differ, OH8 prevails and this appendix is updated at the next pack revision. Legal and professional-conduct limits in Appendix G and Appendix O prevail over any commercial value here.
3. **Prices** are in INR, exclusive of GST, per month unless stated, "billed annually" by default; monthly billing carries a monthly-billing uplift (seed +15%) shown transparently. Every price is `[OWNER TO SET]` until the owner approves the first catalogue version (OI-P20-06).
4. **Continuity with the live site (observed 25 Oct 2026):** Basic "from ₹10,000 / month", Pro "from ₹30,000 / month" (badge "Most popular"), Custom. The pack renames them **Essentials**, **Professional**, **Enterprise** (clearer for buyers and SEO; the old names redirect) and keeps the starting price points. The live page calls the assistant "Nidhi AI Assistant"; the product name is **Vidhi AI** (D-14).

## N.1 Pricing principles

| # | Principle | Consequence in product |
|---|---|---|
| PP-1 | Show the price before the sales call | Every package and add-on has a visible "from" price or a stated basis; only Enterprise components that need scoping say "on quote" |
| PP-2 | Base + components | Buyers pay for what applies to them (regulator packs, modules); no "everything" bundle forced on a small LLP |
| PP-3 | Price on value drivers the buyer understands | Legal entities, users, entity size band (turnover/AUM/members), regulator packs, modules; not opaque "points" |
| PP-4 | Never charge to read or export your own data | Export, read and auditor access are free and survive non-payment (P20 FR-P20-43) |
| PP-5 | No dark patterns | No pre-ticked paid add-ons, no countdowns, no anchor prices, cancellation as easy as purchase (OH8.9; CCPA Dark Patterns Guidelines 2023) |
| PP-6 | AI is metered honestly | Credits, not tokens; included allowance per package; deterministic compliance logic never consumes credits |
| PP-7 | Services are separate and optional | Implementation, retainers and drafting are marketplace items (P21), purchasable without SaaS; software price never depends on buying services |
| PP-8 | Group neutrality | No bundle ties Equator fees to LDC/Finbyx/Udofin (OH8.2); LDC compliance insights are never used for group cross-sell without written authorisation (OH Part 4.5) |
| PP-9 | Regulated-function continuity | Dunning restricts only new non-regulated units (OH8.7) |
| PP-10 | Every number explainable | The configurator and invoices show basis, quantity, unit price, period and GST separately |

## N.2 Packages (seed)

| Attribute | **Essentials** | **Professional** | **Enterprise** |
|---|---|---|---|
| Positioning (pricing-page line) | "Everything a growing company needs to stay compliant and board-ready." | "For regulated entities that need maker-checker depth, policies, board and risk on one platform." | "For banks, large NBFCs, groups and conglomerates that need scale, control and custom integration." |
| Typical buyers | Private/public unlisted companies, LLPs, Section 8 companies, small NBFC-BL, credit co-operative societies (small), IFSCA units in set-up, insurance brokers (small), AIF managers (small) | NBFC-BL (large) / ML / UL, HFCs, MFIs, UCBs (Tier 1–3), listed SMEs and mid-caps, AMCs/AIF managers, IFSCA FC/FU and FMEs, insurers' subsidiaries, insurance brokers, ARCs (small) | Scheduled commercial banks, SFBs, UCB Tier 4, NBFC-UL/TL, large ARCs, insurers, listed large-caps, financial conglomerates and groups |
| Indicative price (annual billing) `[OWNER TO SET]` | from ₹10,000 / month | from ₹30,000 / month | from ₹75,000 / month, or on quote |
| Size band basis | Up to ₹100 crore turnover or AUM (or ≤ 5,000 members for co-operatives) | Up to ₹5,000 crore AUM / turnover (or ≤ 50,000 members) | Any; priced by band |
| Legal entities included | 1 | 3 | 5 (more by band) |
| Named users included | 10 | 40 | 150 (more by band) |
| Regulator packs included | 1 primary (e.g., MCA Companies, or RBI-NBFC, or IFSCA, or SEBI, or IRDAI, or Co-op State Act) + Data Protection Essentials + Labour basics checklist | 3 (any combination) + Data Protection & Cyber core | Unlimited |
| Storage included | 25 GB | 200 GB | 1 TB + |
| Vidhi AI credits / month included | 300 | 1,500 | 6,000 + |
| Support | E-mail and in-app, business hours; knowledge base; onboarding webinar | Priority in-app and phone; named onboarding manager for 30 days; quarterly check-in | Premium 24×7 for Sev 1; named CSM; QBRs; custom SLA |
| Deployment | Multi-tenant SaaS, India region | Multi-tenant SaaS, India region | SaaS, or dedicated environment (monthly rental), India region; BYO storage; customer-managed keys option |
| Contract | Click-wrap (RE Addendum for regulated entities) | Click-wrap or eSigned MSA | eSigned MSA, DPA, RE Addendum, custom SLA |
| Trial | 7-day trial (Professional features) | 7-day trial | Guided pilot (sales-led; trial extension policy) |

## N.3 Components (add-ons) catalogue

Legend: ✓ included · A add-on (price shown) · E Enterprise-only · — not available. Prices are per month, annual billing, `[OWNER TO SET]`.

| Code | Component | Modules / entitlement keys | Ess. | Pro. | Ent. | Indicative price | Requires / notes | Recommended for |
|---|---|---|---|---|---|---|---|---|
| ADD-REG | Additional regulator pack (each) | `cnt.pack.<code>` | A | A (after 3) | ✓ | ₹2,500 per pack | Packs (codes follow the Appendix E template families, X-09): RBI-NBFC, RBI-SCB, RBI-UCB, RBI-RCB, RBI-ARC, RBI-OTH (AIFI, payment systems, CICs, AD-II/FFMC), SEBI-LISTED, SEBI-MF, SEBI-AIF, SEBI-REIT-INVIT, SEBI-INT, IFSCA-GEN / IFSCA-FCFU / IFSCA-FME, IRDAI-INS, IRDAI-INT, MCA-CO, MCA-LLP, COOP-CCS / COOP-GEN (by State or MSCS), DATA-PRIV, CYBER, LAB-POSH, TAX-GST; overlays without a v1.0 template (FEMA, PMLA/FIU) when published, International packs (GDPR, CCPA/CPRA, UAE, Singapore — when available, D-19) | Multi-regulated entities |
| ADD-LAB | Labour Codes & POSH Suite | `lab.*` | A | A | ✓ | ₹4,000 (≤ 100 employees) / ₹8,000 (≤ 500) / band | Standalone SKU available (ADD-LAB-S) | All employers |
| ADD-HRMS | HRMS & Payroll | `hr.*` | A | A | A | ₹60 per employee per month, min ₹3,000 | Includes employee master used by ADD-LAB; payroll disbursal via bank file/payout partner (D-11) | Companies managing staff in-tool |
| ADD-ERM | Enterprise Risk Management | `erm.*` | A | ✓ | ✓ | ₹6,000 | — | NBFC, UCB, banks, insurers, listed |
| ADD-RAL | Risk Assessment Lab (ICAAP, stress testing, scenario analysis, capital & ratio engine, ALM) | `ral.*` | — | A | ✓ | ₹12,000 | Requires ADD-ERM (Pro has ERM included) | NBFC-ML/UL, banks, UCB, HFC, ARC |
| ADD-AUD | Audit Management (internal, RBIA, IS, secretarial audit support) | `aud.*` | A | A | ✓ | ₹6,000 | — | All regulated entities; listed companies |
| ADD-RET | Return Studio (RBI supervisory returns, CIC files, data preparation from Tally/Excel/LMS) | `ret.*`, `acc.*` | — | A | ✓ | ₹10,000 (+ PAYG per return run above allowance if switched on) | Uses shared returns kernel (D-05); free consumption of Finbyx return runs for Finbyx clients | NBFC, UCB, banks, ARC |
| ADD-TAX | Tax Data Exports (GST/TDS data preparation, reconciliations) | `ret.tax.*` | A | A | ✓ | ₹2,500 | — | All |
| ADD-DPC | Data Protection & Cyber (DPDP, GDPR, CCPA, CERT-In, ISMS controls, breach workflows) | `dpc.*` | A (Essentials includes DP Essentials checklist only) | ✓ core / A advanced | ✓ | ₹5,000 (advanced) | Standalone SKU (ADD-DPC-S) | All |
| ADD-TPR | Third-Party & Outsourcing Risk | `tpr.*` | A | A | ✓ | ₹4,000 | Requires ADD-ERM for risk scoring linkage (optional) | REs (outsourcing directions) |
| ADD-BRD | Board Portal & Company Secretarial Pro (board packs, electronic approval of resolutions by circulation (Companies Act s.175), minutes with SS-1/SS-2 checks, registers, MCA filing tracker) | `gov.board_portal.*` | A | ✓ | ✓ | ₹5,000 | Standalone SKU (ADD-BRD-S) | Companies with active boards |
| ADD-LODR | Listed Company Pack (LODR, PIT, SAST, structured digital database, disclosures calendar) | `pack.sebi_listed.*` | A | A | ✓ | ₹8,000 | Requires ADD-BRD | Listed entities |
| ADD-COOP | Co-operative Society Suite (membership, elections, AGM, registers, audit rectification, State Act packs) | `coop.*` | A | A | ✓ | ₹3,000 (≤ 5,000 members) / band | Credit operations stay in Finbyx (D-16) | Co-operative societies |
| ADD-GRV | Grievance Redressal & Support Desk | `grv.*` | A | ✓ | ✓ | ₹4,000 | Standalone SKU (ADD-GRV-S) | NBFC, UCB, banks, insurers, listed (investor grievances) |
| ADD-DMSX | Advanced DMS (OCR incl. handwriting, WhatsApp/screenshot type copies, translation, bulk folder intake) | `dms.advanced.*` | A | ✓ | ✓ | ₹3,000 + AI credits for heavy OCR/translation | Uses Vidhi credits | All |
| ADD-ENT | Additional legal entity | `limits.entities` | A | A | ✓ (band) | ₹3,000 per entity | — | Groups |
| ADD-USR10 / 25 / 50 | User packs | `limits.users` | A | A | ✓ (band) | ₹2,000 / ₹4,500 / ₹8,000 | — | — |
| ADD-STO | Storage pack (100 GB) | `limits.storage_gb` | A | A | A | ₹1,500 | — | Document-heavy tenants |
| ADD-BYO | Bring-your-own storage connector (S3/Azure/GCS/SharePoint/OneDrive/Google Drive/SFTP/on-prem agent) | `xpt.byo.*` | — | A | ✓ | ₹4,000 | P19 | Enterprises, banks |
| ADD-CONN | Third-party connector (each: other LOS/LMS, HRMS, accounting, core banking) | `int.connector.<code>` | — | A | ✓ | ₹3,000 per connector | Finbyx/Udofin native connectors included free for their clients | Non-Finbyx lenders |
| ADD-API | API access tier (higher rate limits, webhooks, sandbox) | `int.api.tier` | — | ✓ (Standard) / A (High) | ✓ | ₹5,000 (High) | — | Integrators |
| ADD-SSO | SSO (SAML/OIDC) and SCIM | `iam.sso` | A | ✓ | ✓ | ₹2,000 | — | Firms with IdP |
| ADD-DED | Dedicated environment (monthly rental) | `deploy.dedicated` | — | — | E | on quote (seed ₹1,50,000) | Separate DB/cluster, CMK | Banks |
| ADD-CMK | Customer-managed keys | `sec.cmk` | — | — | E | on quote | AWS KMS external key store or BYOK [VERIFY design] | Banks |
| ADD-SUPP | Premium support (24×7 Sev 1, named CSM) | `support.tier` | A | A | ✓ | ₹10,000 | — | — |
| ADD-AI-1K / 5K / 20K | Vidhi AI credit packs | `ai.credits` | A | A | A | ₹2,500 / ₹11,000 / ₹40,000 (one-time; valid 12 months) | — | Heavy AI users |
| ADD-RV | Regulator / supervisor view grants (time-boxed read-only) | `iam.regulator_view` | — | A | ✓ | ₹0 (feature, no charge) — listed for clarity | D-12 | REs |
| ADD-WL | White-label / practice edition (for CA/CS/law firms managing multiple client entities) | `tenant.practice_mode` | — | — | E | on quote; per client-entity band | Professional-firm buyer; the firm is the customer (not a marketplace listing) | Professional firms |

**Standalone SKUs** (no compliance base needed; R-014): ADD-LAB-S (Labour & POSH), ADD-HRMS-S (HRMS & Payroll + Labour basics), ADD-GRV-S (Grievance Desk), ADD-BRD-S (Board Portal), ADD-DPC-S (Data Protection & Cyber). Each provisions the same tenant type with only those modules; adding the compliance base later is an upgrade (P20 FR-P20-08).

**Bundles** (`BUNDLE` rule; bundle discount seed 10–15% `[OWNER TO SET]`): *Lender Pack* (ERM + Risk Lab + Return Studio + Grievance), *People Pack* (HRMS + Labour & POSH), *Board & Listed Pack* (Board Portal + LODR), *Trust Pack* (Data Protection advanced + TPR + Audit).

## N.4 Feature rows (comparison table seed — 126 rows)

Legend per column: ✓ included · A add-on · — not available · text = limit.

| # | Group | Feature row | "i" explainer (short) | Ess. | Pro. | Ent. |
|---|---|---|---|---|---|---|
| 1 | Compliance | Obligation register by regulator and entity type | Every applicable requirement as an actionable checkpoint with citation | ✓ | ✓ | ✓ |
| 2 | Compliance | Instrument catalogue with add/remove checkboxes | Choose which master directions, regulations and circulars apply to you | ✓ | ✓ | ✓ |
| 3 | Compliance | Excel question-bank import (LDC templates) | Upload compliance questions in the LDC Excel format | ✓ | ✓ | ✓ |
| 4 | Compliance | Edit question text and add your own questions (tenant overlay, audit-trailed) | Your changes apply only to your company; history kept | ✓ | ✓ | ✓ |
| 5 | Compliance | Maker-checker workflow | Every compliance is submitted by a maker and approved by a checker | Single level | Multi-level | Multi-level + custom |
| 6 | Compliance | Department/function hierarchy, rename departments | Map compliance to your own structure | ✓ | ✓ | ✓ |
| 7 | Compliance | Evidence upload with hash and version | Proof of compliance stored tamper-evident | ✓ | ✓ | ✓ |
| 8 | Compliance | Exceptions, waivers, extensions with approvals | Record and approve deviations | — | ✓ | ✓ |
| 9 | Compliance | Attestations (quarterly certifications by owners) | Department heads certify compliance | — | ✓ | ✓ |
| 10 | Compliance | Compliance calendar with due-date engine | Statutory dates and frequencies computed automatically | ✓ | ✓ | ✓ |
| 11 | Compliance | Calendar sync (Microsoft 365, Google, Outlook.com, Gmail, Apple) | See deadlines in your own calendar | ✓ | ✓ | ✓ |
| 12 | Compliance | Tasks, assignments and escalations | Assign work by hierarchy with reminders | ✓ | ✓ | ✓ |
| 13 | Compliance | Scheduled and recurring tasks | Create tasks that repeat or run on a date | ✓ | ✓ | ✓ |
| 14 | Compliance | Compliance reports (CCO, board, department) | Status, overdue, risk-weighted reports | Standard | Standard + custom | Custom + scheduled |
| 15 | Compliance | Board compliance certificate drafts | Draft quarterly compliance report to the board | — | ✓ | ✓ |
| 16 | Compliance | Bulk actions with preview and undo | Assign, re-date or close many items at once safely | ✓ | ✓ | ✓ |
| 17 | Compliance | Compliance health score and heatmap | See where you are exposed | ✓ | ✓ | ✓ |
| 18 | Regulatory change | Regulatory Updates feed (RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, MoLE, co-op departments) | Daily 8 PM scan plus intraday feeds | ✓ | ✓ | ✓ |
| 19 | Regulatory change | "What changed" view: previous vs new actionable | Side-by-side old and new requirement with audit trail | ✓ | ✓ | ✓ |
| 20 | Regulatory change | Impact assessment workflow | Decide applicability, owners and actions for each change | — | ✓ | ✓ |
| 21 | Regulatory change | AI question authoring from a new master direction (tenant) | Upload a regulation; Vidhi drafts questions in your template for review | A (credits) | ✓ | ✓ |
| 22 | Regulatory change | Push, e-mail and calendar alerts for updates | Never miss a change | ✓ | ✓ | ✓ |
| 23 | Governance | Directors, KMP and committee registers | Who holds which role, tenure and eligibility | ✓ | ✓ | ✓ |
| 24 | Governance | Statutory registers (MBP-1, MBP-2, MBP-4, MGT-1, CHG-7, SBO, etc.) | Maintained from your data | Core | Full | Full |
| 25 | Governance | Board and committee meetings: notices, agenda, quorum, attendance | Secretarial Standards checks | Basic | ✓ | ✓ |
| 26 | Governance | Minutes drafting with SS-1/SS-2 checks | Vidhi drafts; CS approves | A (credits) | ✓ | ✓ |
| 27 | Governance | Board portal (secure board packs, annotations, e-approval) | Directors review papers securely | A | ✓ | ✓ |
| 28 | Governance | Resolutions by circulation with e-approval | Collect approvals and record them | — | ✓ | ✓ |
| 29 | Governance | MCA/ROC filing tracker | Forms, due dates, SRNs, challans | ✓ | ✓ | ✓ |
| 30 | Governance | Fit & proper declarations and KMP documents | Generate and track declarations | — | ✓ | ✓ |
| 31 | Governance | Listed-company disclosures calendar (LODR) | Intimations and disclosures due | A | A | ✓ |
| 32 | Governance | Structured digital database for PIT | Insider-trading compliance | A | A | ✓ |
| 33 | Governance | Co-operative governance (elections, AGM, office bearers) | For societies under State Acts or MSCS Act | A | A | ✓ |
| 34 | Policies & documents | Policy register with versions, owners, board approval and review dates | Never miss a policy review | ✓ | ✓ | ✓ |
| 35 | Policies & documents | Model policy templates by regulator | Start from a vetted template | 10 templates | Full library | Full library + custom |
| 36 | Policies & documents | Vidhi drafts policies in Word with tracked changes | Aligned to template and your previous version | A (credits) | ✓ | ✓ |
| 37 | Policies & documents | Policy acknowledgements by staff | Staff confirm they read the policy | — | ✓ | ✓ |
| 38 | Policies & documents | Document management (folders, tags, search, sharing, retention) | All compliance documents in one place | ✓ | ✓ | ✓ |
| 39 | Policies & documents | Selective external sharing with expiry and watermark | Share only what you choose | ✓ | ✓ | ✓ |
| 40 | Policies & documents | eSign (Aadhaar eSign, DSC) | Sign policies, agreements, minutes | Pay per use | Pay per use | Pay per use / bundle |
| 41 | Policies & documents | OCR of scanned and handwritten documents with editable type copy | AI reads it; you correct it | A | ✓ | ✓ |
| 42 | Policies & documents | WhatsApp / screenshot / e-mail evidence capture | Turn chats and e-mails into evidence | A | ✓ | ✓ |
| 43 | Policies & documents | Translation to English (UN languages and major Indian languages) | Understand documents in any language | A | ✓ | ✓ |
| 44 | Policies & documents | Bulk folder intake | Upload a folder tree; we map it | A | ✓ | ✓ |
| 45 | Risk | Risk register, taxonomy, appetite | All risk types incl. Basel Pillar 2 risks | A | ✓ | ✓ |
| 46 | Risk | RCSA and control testing | Self-assess risks and controls | A | ✓ | ✓ |
| 47 | Risk | Key risk indicators with thresholds | Early warnings | A | ✓ | ✓ |
| 48 | Risk | Loss events and incidents | Record operational losses | A | ✓ | ✓ |
| 49 | Risk | CRO dashboard | One view for the risk officer | A | ✓ | ✓ |
| 50 | Risk | ICAAP workspace and document generator | Prepare ICAAP with reproducible numbers | — | A | ✓ |
| 51 | Risk | Stress testing and scenario analysis library | Baseline, adverse, severe; sensitivity | — | A | ✓ |
| 52 | Risk | Capital adequacy and financial ratio engine | CRAR, leverage, NPA, liquidity ratios | — | A | ✓ |
| 53 | Risk | ALM and liquidity gaps | Structural liquidity and IRS | — | A | ✓ |
| 54 | Risk | KMP dashboards (CEO, MD, CFO, CCrO, CRO, CCO, IA, Board) | Each leader sees what matters | Basic | ✓ | ✓ + custom |
| 55 | Audit | Audit universe and risk-based audit plan | Plan audits by risk | A | A | ✓ |
| 56 | Audit | Workpapers, findings, remediation tracking | Close audit points on time | A | A | ✓ |
| 57 | Audit | Draft internal-audit report with Vidhi | Report drafts from findings | A | A | ✓ |
| 58 | Audit | Auditor workspace (internal, external, secretarial, IS) | Time-boxed auditor access | ✓ (view-only auditor) | ✓ | ✓ |
| 59 | Returns & data | RBI returns calendar and status | All applicable returns tracked | ✓ | ✓ | ✓ |
| 60 | Returns & data | Return Studio: prepare upload-ready RBI return files | From Tally, Excel or your LMS | — | A | ✓ |
| 61 | Returns & data | CIC data files (consumer and commercial) | For CIBIL, CRIF, Experian, Equifax | — | A | ✓ |
| 62 | Returns & data | Tally Prime / Excel import with mapping | Bring your books and loan data | — | A | ✓ |
| 63 | Returns & data | Finbyx and Udofin native data connectors | Pull return-ready data from the ecosystem | — | ✓ | ✓ |
| 64 | Returns & data | GST and TDS data exports | Prepare data for your returns | A | A | ✓ |
| 65 | Returns & data | Filing acknowledgement capture | Proof of filing stored with the return | ✓ | ✓ | ✓ |
| 66 | People & labour | Labour Codes registers and returns | Wages, OSH, SS, IR codes | A | A | ✓ |
| 67 | People & labour | POSH Internal Committee workspace (sealed) | Confidential complaints handling | A | A | ✓ |
| 68 | People & labour | Employment agreements with eSign | Issue and sign offer and employment documents | A | A | ✓ |
| 69 | People & labour | HRMS: employees, org chart, leave, attendance | Manage your people | A | A | A |
| 70 | People & labour | Payroll with statutory deductions | Payroll on versioned rule packs | A | A | A |
| 71 | People & labour | People-risk data to risk module | People metrics feed risk analysis | A | A | ✓ |
| 72 | Data protection & cyber | DPDP readiness and records of processing | Know what data you hold and why | Checklist | ✓ | ✓ |
| 73 | Data protection & cyber | Consent and notice management | DPDP-compliant notices | — | ✓ | ✓ |
| 74 | Data protection & cyber | Data-principal rights requests | Handle access/correction/erasure requests | — | ✓ | ✓ |
| 75 | Data protection & cyber | Breach workflow (DPDP 72-hour report, CERT-In 6-hour report) | Two clocks, two destinations | — | ✓ | ✓ |
| 76 | Data protection & cyber | GDPR and CCPA overlays | For organisations serving EU or California residents | — | A | ✓ |
| 77 | Data protection & cyber | ISMS control library (ISO 27001:2022 Annex A, SOC 2 TSC) | Track security controls | — | A | ✓ |
| 78 | Data protection & cyber | Vendor and outsourcing risk | Due diligence and monitoring | A | A | ✓ |
| 79 | Grievance | Customer grievance desk with website link | Complaints from your website handled here | A | ✓ | ✓ |
| 80 | Grievance | GRO workspace with escalation and Ombudsman tracking | Regulatory timelines enforced | A | ✓ | ✓ |
| 81 | Grievance | Support tickets for your customers | Close tickets from LDC | A | ✓ | ✓ |
| 82 | Vidhi AI | Ask Vidhi (regulatory Q&A with citations) | Answers from official texts with paragraph citations | ✓ | ✓ | ✓ |
| 83 | Vidhi AI | Knowledge notebooks (your documents + regulations) | NotebookLM-style research | 3 notebooks | 25 | Unlimited |
| 84 | Vidhi AI | Vidhi as an AI employee: tasks, reminders, drafts | Assign tasks to Vidhi | ✓ | ✓ | ✓ |
| 85 | Vidhi AI | Included AI credits per month | Credits for AI actions | 300 | 1,500 | 6,000 |
| 86 | Vidhi AI | No training on your data | Your content is never used to train models | ✓ | ✓ | ✓ |
| 87 | Integrations | Microsoft 365 / Google Workspace (calendar, storage, mail) | Work where you already work | ✓ | ✓ | ✓ |
| 88 | Integrations | Website and app grievance widget | Embed on your site | A | ✓ | ✓ |
| 89 | Integrations | Public API and webhooks | Connect your systems | — | ✓ | ✓ |
| 90 | Integrations | Third-party LOS/LMS/HRMS/accounting connectors | Bring data from other systems | — | A | ✓ |
| 91 | Integrations | PAN/CIN/GSTIN auto-fetch at onboarding | Fewer forms | ✓ | ✓ | ✓ |
| 92 | Data & exit | Full data export in folders of Word, Excel and PDF | Leave any time with your data | ✓ | ✓ | ✓ |
| 93 | Data & exit | Scheduled exports to your storage | Automatic backups to your drive or bucket | — | A | ✓ |
| 94 | Data & exit | Bring-your-own storage | Keep documents in your own storage | — | A | ✓ |
| 95 | Data & exit | Data stays in India | Primary and DR in Indian regions | ✓ | ✓ | ✓ |
| 96 | Security & admin | MFA for all users | Mandatory | ✓ | ✓ | ✓ |
| 97 | Security & admin | SSO (SAML/OIDC) and SCIM | Use your identity provider | A | ✓ | ✓ |
| 98 | Security & admin | Role-based and attribute-based access | Fine-grained access | ✓ | ✓ | ✓ |
| 99 | Security & admin | Immutable audit trail with correction entries | Tamper-evident history | ✓ | ✓ | ✓ |
| 100 | Security & admin | Regulator/supervisor read-only access grants | Time-boxed, logged | — | ✓ | ✓ |
| 101 | Security & admin | IP allow-listing and session policies | Restrict access | — | ✓ | ✓ |
| 102 | Security & admin | Customer-managed keys | Control your encryption keys | — | — | E |
| 103 | Security & admin | Dedicated environment | Isolated deployment | — | — | E |
| 104 | Security & admin | Accessibility (WCAG 2.2 AA) | Usable with screen readers and keyboard | ✓ | ✓ | ✓ |
| 105 | Customisation | Custom fields, statuses and forms | Make it yours | Limited | ✓ | ✓ |
| 106 | Customisation | Custom dashboards and widgets | Each user arranges their view | ✓ | ✓ | ✓ |
| 107 | Customisation | Terminology and menu customisation | Rename menus and terms | — | ✓ | ✓ |
| 108 | Customisation | Workflow designer (approval levels, SLAs, escalations) | Configure without code | Basic | ✓ | ✓ |
| 109 | Customisation | Branding (logo, colours) on reports and portal | Your brand on outputs | ✓ | ✓ | ✓ |
| 110 | Customisation | Sandbox for configuration changes | Test before you apply | — | — | ✓ |
| 111 | Support & services | Help centre, tutorials, videos, "i" help | Learn as you go | ✓ | ✓ | ✓ |
| 112 | Support & services | Onboarding | How we get you live | Webinar + guides | Named manager 30 days | Implementation project |
| 113 | Support & services | Support hours | When you can reach us | Business hours | Priority + phone | 24×7 Sev 1 |
| 114 | Support & services | Named customer success manager | One person accountable for your success | — | — | ✓ |
| 115 | Support & services | Quarterly business reviews | Review value and plans each quarter | — | Check-in | ✓ |
| 116 | Support & services | Marketplace: retainers, drafting, ICAAP, certification readiness | Buy expert help when you need it | Available | Available | Available + preferred rates |
| 117 | Support & services | FinLegal Academy trainings | Courses for your teams | Available | Available | Corporate bundles |
| 118 | Value | Savings & value dashboard | Hours saved, penalties avoided, transparently calculated | ✓ | ✓ | ✓ |
| 119 | Value | Value report for the board | Quarterly value summary | — | ✓ | ✓ |
| 120 | Value | Free compliance health check (re-run any time) | Benchmark yourself | ✓ | ✓ | ✓ |
| 121 | Scale | Legal entities included | — | 1 | 3 | 5+ |
| 122 | Scale | Users included | — | 10 | 40 | 150+ |
| 123 | Scale | Storage included | — | 25 GB | 200 GB | 1 TB+ |
| 124 | Scale | Regulator packs included | — | 1 | 3 | Unlimited |
| 125 | Commercial | Monthly or annual billing | Annual saves the uplift | ✓ | ✓ | ✓ |
| 126 | Commercial | Cancel any time; read and export continue | No lock-in | ✓ | ✓ | ✓ |

## N.5 Meters (usage at source; `UsageRecorded` aggregates)

| Meter | Unit | Included | Overage default | Notes |
|---|---|---|---|---|
| `AI_CREDITS` | credit | per package (N.2) | Blocks AI features at zero unless pack bought or overage opt-in (₹3 per credit seed) | 1 credit ≈ one standard Vidhi request; long-document OCR/translation = credits per page (seed: OCR 1/page, translation 2/page, policy draft 20/document, minutes draft 15/meeting, ICAAP narrative 100/run) — table versioned in `ai.credit_rates` |
| `STORAGE_GB_MONTH` | GB-month | per package | Uploads blocked except deadline evidence (P20 FR-P20-44) unless pack bought | — |
| `ESIGN_PASS_THROUGH` | signature | 0 | Pass-through at cost + disclosed margin (stream RS-LDC-09) | Per ESP |
| `KYC_VERIFICATION_PASS_THROUGH` | check | PAN/CIN fetch at onboarding free | Pass-through | Never CIC bureau pulls (CICRA; OH8.2) |
| `SMS_WHATSAPP_PASS_THROUGH` | message | reminders by e-mail/in-app free | Pass-through | DLT templates |
| `API_CALLS` | 1,000 calls | tier allowance | ₹50 per 1,000 above allowance (seed) | — |
| `RETURN_RUNS` | return package | 50/month with ADD-RET | ₹200 per run (only if PAYG switched on) | Finbyx-sourced runs not metered |
| `EXTRA_USERS_PEAK` | user | per package | Users beyond allowance blocked (no surprise charge) unless overage opt-in | — |
| `EXTRA_ENTITIES` | entity | per package | Blocked unless add-on | — |

## N.6 LawDocsComply revenue-stream registry (RS-LDC)

Each stream maps to an OH8 stream code, starts at the default state below, and can be switched by market × segment × channel (P20 FR-P20-57). "HI" = high-impact (checker required for the kill switch).

| Code | Stream | OH8 stream | Default | Payer | Basis | Dependencies / guard-rails | Kill-switch scope |
|---|---|---|---|---|---|---|---|
| RS-LDC-01 | Essentials subscription | SUBSCRIPTION | ON | Organisation | Monthly/annual | Export always included | market, segment (HI) |
| RS-LDC-02 | Professional subscription | SUBSCRIPTION | ON | Organisation | Monthly/annual | — | market, segment (HI) |
| RS-LDC-03 | Enterprise subscription | SUBSCRIPTION | ON | Organisation | Contract | MSA, DPA, RE Addendum | market (HI) |
| RS-LDC-04 | Module add-on subscriptions | SUBSCRIPTION | ON | Organisation | Per component | Dependencies (N.3) | component |
| RS-LDC-05 | Standalone products (Labour, HRMS, Grievance, Board, DP) | SUBSCRIPTION | ON | Organisation | Per product | — | product |
| RS-LDC-06 | Dedicated environment rental | MONTHLY_RENTAL | ON (Enterprise only) | Organisation | Monthly | Notice period; exit process | market |
| RS-LDC-07 | Vidhi AI credit packs | PAYG | ON | Organisation | Prepaid | No credits for deterministic compliance logic | global |
| RS-LDC-08 | Overage (users, storage, API, return runs) | PAYG | OFF | Organisation | Metered | Opt-in only; never surprise billing | global (HI) |
| RS-LDC-09 | Pass-through eSign/KYC/messaging | PASS_THROUGH | ON | Organisation | At cost + disclosed margin | Never credit-bureau resale (CICRA) | provider |
| RS-LDC-10 | Implementation packages | IMPLEMENTATION | ON | Organisation | Fixed/milestone | Milestone acceptance (OH4) | segment |
| RS-LDC-11 | Data migration (question banks, trackers, documents) | DATA_MIGRATION | ON | Organisation | Per batch | Reconciliation sign-off | segment |
| RS-LDC-12 | Compliance retainers (managed compliance) | MANAGED_SERVICES | ON | Organisation | Monthly/annual | RE core-function guard-rails (P21 FR-P21-13) | segment (HI) |
| RS-LDC-13 | Drafting services (policies, agreements documentation, annual reports, minutes) | PROFESSIONAL_SERVICES | ON | Organisation | Fixed/per unit | Service class rules (Appendix O §O.5) | category |
| RS-LDC-14 | Risk & capital services (ICAAP, stress testing, RCSA facilitation) | PROFESSIONAL_SERVICES | ON | Organisation | Fixed/milestone | Ownership of ICAAP stays with the board | category |
| RS-LDC-15 | Return preparation support | PROFESSIONAL_SERVICES | ON | Organisation | Per return / retainer | Human filing by RE (D-13) | category |
| RS-LDC-16 | Certification readiness (SOC 2, ISO, PCI DSS) and VAPT | PROFESSIONAL_SERVICES | ON | Organisation | Fixed/milestone | Certification wall (P21 FR-P21-14) | category |
| RS-LDC-17 | Virtual leadership support (vCFO, vCISO, vDPO, vCCO-support) | MANAGED_SERVICES | ON | Organisation | Monthly | Designated officers remain the RE's employees | category (HI) |
| RS-LDC-18 | Marketplace listing subscriptions for permitted professions/firms | SUBSCRIPTION (provider) | OFF | Provider | Monthly | Profession modes; never advocates/CAs/CSs/CMAs in practice by default; OH8 deny list | profession (HI) |
| RS-LDC-19 | Marketplace commission (Model M3) | MARKETPLACE_COMMISSION (new; Appendix X) | OFF | Provider | % of fee | Counsel + tax; TCS s.52; never regulated professions by default | profession (HI) |
| RS-LDC-20 | Corporate training bundles (Academy) | TRAINING | ON | Organisation | Per seat/batch | — | category |
| RS-LDC-21 | Individual Academy courses (referral to trainings.lawdocs.in) | TRAINING (Academy entity) | ON | Individual | Per course | Merchant per OI-P21-07 | global |
| RS-LDC-22 | Health-check deep-dive report (paid expert review of the free health check) | PROFESSIONAL_SERVICES | ON | Organisation | Fixed | Disclaimer: not an audit | global |
| RS-LDC-23 | API access high tier | SUBSCRIPTION | ON | Organisation | Monthly | — | global |
| RS-LDC-24 | White-label / practice edition for professional firms | PERPETUAL_LICENCE_AMC or SUBSCRIPTION | OFF (pilot) | Professional firm | Per client-entity band | The firm is the customer; no client referral fees | global (HI) |
| RS-LDC-25 | Reseller / channel partner programme | SUBSCRIPTION (partner pricing) | OFF | Partner | Margin on resale | Partners cannot be advocates/CAs receiving referral fees; written agreements | partner |
| RS-LDC-26 | Regulatory-pack customisation (custom question banks for a tenant) | PROFESSIONAL_SERVICES | ON | Organisation | Per instrument | Tenant-only overlay; AI drafts reviewed | global |
| RS-LDC-27 | Premium support | SUBSCRIPTION | ON | Organisation | Monthly | — | global |
| RS-LDC-28 | Benchmark & insight reports (aggregate, anonymised) | ONE_TIME_SERVICE | OFF | Organisation | Per report | ≥ 20 tenants; DPDP and confidentiality review; tenant opt-in to contribute | global (HI) |
| RS-LDC-29 | Event and newsletter sponsorship (public website/webinars only) | ADVERTISING_SPONSORSHIP | OFF | Sponsor | Per event | Never inside the tenant app or regulated workflows; labelled; ASCI/CCPA review | global (HI) |
| RS-LDC-30 | In-app advertising | ADVERTISING_SPONSORSHIP | OFF (L-locked off for tenant app) | — | — | Not offered: ads inside a compliance tool damage trust and may be unlawful steering [REC] | — |

**Why some streams are OFF by default.** Listing fees and commissions for regulated professions conflict with BCI r.36, ICAI clauses (2)/(3)/(6)/(7) of Part I of the First Schedule and similar codes (Appendix O §O.5). Benchmark reports need a DPDP/contractual basis for aggregate use. In-app ads are excluded for trust and conflict reasons; public-site sponsorship may be piloted with labelling.

## N.7 Trial, discounts, promotions and partner rules

| Item | Seed | Rule |
|---|---|---|
| Trial length | 7 days | Professional features; caps (P20 FR-P20-25); one per organisation; never auto-converts |
| Self extension | once, ≤ 7 days | In-product request |
| LawDocs extension | ≤ 14 days cumulative without checker | Reason-coded; beyond needs checker |
| Annual billing benefit | monthly price × 12 vs annual = ~13% saving (monthly uplift 15%) `[OWNER TO SET]` | Shown as amount and % |
| Multi-year | 2-year 5% / 3-year 8% additional `[OWNER TO SET]` | Price-lock for term |
| Segment discounts | Co-operative societies 20%; Section 8/NGO 25%; startups (DPIIT-recognised, < 3 years) 30% first year `[OWNER TO SET]` | Evidence required (registration, DPIIT certificate) |
| Ecosystem bundle | Finbyx/Udofin clients: LDC Return Studio connector free; 10% on LDC `[OWNER TO SET]` | Never bundled with Equator (OH8.2); disclosed |
| Promo codes | Types per P20 FR-P20-63 | Not stackable by default; first purchase only by default |
| Referral credits | Non-professional referrers (existing customers) get a service credit | No referral rewards to advocates, CAs, CSs, CMAs (NN-20) |
| Partner programme | Resellers/implementers (technology firms, consultancies) | Written agreement; disclosed margins; no professional-referral fees |
| Price changes | ≥ 30 days' notice, at renewal | Grandfathering per price-book version (OH8.4) |
| Refunds | Annual plans: pro-rata within first 30 days of first term; otherwise none; services per Appendix O §O.6 `[OWNER TO SET]` | Credit notes via OH8 |

## N.8 Business model and revenue streams by segment (narrative)

1. **Land with the free health check, expand by modules.** The ~50-question health check (P23) is the lead magnet; it recommends a package and components grounded in the entity type, which pre-fills the configurator. Expansion comes from regulator packs, Risk Lab, Return Studio, Labour/HRMS and seats as the client sees value.
2. **Segments and primary streams.**

| Segment | Entry package | Expansion levers | Services pull-through |
|---|---|---|---|
| Private/public companies, LLPs | Essentials (MCA pack) | Labour & POSH, HRMS, Data Protection, Board Portal | Secretarial retainer, annual report drafting, POSH external member |
| Listed companies | Professional + LODR | Board Portal, PIT database, audit | Secretarial retainer, disclosures support |
| NBFC-BL | Essentials or Professional (RBI-NBFC pack) | Return Studio, Grievance, Data Protection | Compliance retainer, policy pack, return support |
| NBFC-ML/UL, HFC, MFI | Professional | Risk Lab (ICAAP, stress tests), Audit, TPR, Return Studio | ICAAP preparation, RBIA design, vCISO |
| UCBs, RCBs | Professional | Return Studio, Risk Lab, Audit, Grievance | Return support, audit readiness |
| Banks, SFBs | Enterprise | Dedicated environment, CMK, connectors | Large implementations |
| ARCs | Professional/Enterprise | Return Studio, Risk Lab | Policy and governance support |
| Co-operative societies | Essentials + Co-op Suite | HRMS, Labour | AGM/election support, audit rectification |
| SEBI intermediaries, AMCs, AIF managers | Professional (SEBI packs) | Data Protection & Cyber (CSCRF), Audit | Cyber readiness, policy packs |
| IFSCA units | Essentials/Professional (IFSCA pack) | Data Protection, multi-entity | Registration and compliance retainers |
| Insurers, insurance intermediaries | Professional (IRDAI packs) | Grievance, Data Protection, Audit | Compliance retainers |
| Professional firms (CA/CS/law) | Practice edition (pilot) | Per client-entity band | — (the firm is the buyer) |

3. **Recurring revenue mix target** `[OWNER TO SET]`: ≥ 70% subscription (incl. add-ons) · ≤ 20% recurring services (retainers) · ≤ 10% one-time (implementation, drafting, trainings).
4. **What not to monetise:** data export, read access after cancellation, regulator-view grants, basic regulatory Updates for held packs, accessibility features, security baseline (MFA, audit trail).

## N.9 Savings model (methodology registry seed)

### N.9.1 Evidence levels

| Level | Definition | Display |
|---|---|---|
| Recorded | Facts captured in LDC or entered by the client with evidence (receipts, invoices) | Solid tile |
| Modelled | Computed from Recorded inputs and a published rule (penalty library) with stated assumptions | Solid tile with "Modelled" chip and assumptions |
| Estimated | Uses baselines not measured for this client (time-and-motion defaults) | Dotted tile with "Estimate" chip; hideable |

### N.9.2 Formulas (decimal arithmetic; snapshot stores inputs, versions and hash — NN-22)

```
HoursSaved(period)        = Σ_a max(0, B_a − M_a) × N_a ÷ 60
   a = activity code; B_a = baseline minutes (methodology version v); M_a = median measured minutes in period
   (task first-open → maker submit, excluding waiting-on-client and checker queue time); N_a = completed count
PeopleCostSaved           = Σ_band HoursSaved_band × HourlyCost_band          (hidden until bands set)
LateFeesPaid(period)      = Σ recorded late fees/penalties linked to filings in period (Recorded)
LateFeeReductionYoY       = LateFeesPaid(prior comparable period) − LateFeesPaid(period)   (Recorded; may be negative)
PenaltyExposureManaged    = Σ_o [OnTime_o] × P_late(o) × Penalty(rule_o, d_ref)            (Modelled)
   P_late(o) = client's pre-LDC late rate for obligation family of o (entered/imported); if absent → show range with
               P_late = 1 and d_ref ∈ {1 day, 30 days} labelled "if each filing had been 1 / 30 days late"
   Penalty(rule, d) from Appendix G penalty library (e.g., s.403 ₹100 × d; GST ₹50 × d capped by AATO band)
ToolCostAvoided           = Σ client-entered replaced costs × months in period (Recorded if evidenced)
ReturnOnSubscription      = (PeopleCostSaved + ToolCostAvoided + max(0, LateFeeReductionYoY)) ÷ SubscriptionCost(period)
   — excludes PenaltyExposureManaged by rule; shown only when all inputs are Recorded or client-entered
```

### N.9.3 Activity baselines (seed; minutes per instance; `[OWNER TO SET]` after a time-and-motion study)

| Code | Activity | Seed baseline (min) | Measured from |
|---|---|---|---|
| ACT-01 | Identify applicability of a new circular/master direction | 180 | Update received → impact assessment submitted |
| ACT-02 | Prepare a compliance checklist for a new instrument (per 10 checkpoints) | 240 | AI question authoring + review time |
| ACT-03 | Track and chase a routine compliance item | 30 | Task open → submit |
| ACT-04 | Prepare evidence pack for an audit (per obligation) | 20 | Auditor request → evidence shared |
| ACT-05 | Prepare quarterly board compliance report | 960 | Report generation → approval |
| ACT-06 | Draft a board meeting agenda and notice | 120 | Meeting created → notice issued |
| ACT-07 | Draft minutes of a board meeting | 240 | Meeting held → draft approved |
| ACT-08 | Draft / revise a regulatory policy | 600 | Draft start → approval |
| ACT-09 | Annual policy review cycle (per policy) | 120 | Review task → completion |
| ACT-10 | Prepare an RBI return from books/LMS (per return) | 300 | Data import → package approved |
| ACT-11 | Prepare CIC submission file | 240 | Data import → file validated |
| ACT-12 | Respond to a customer grievance (admin effort) | 45 | Intake → closure (handling time only) |
| ACT-13 | Maintain statutory registers (per entry) | 15 | Event → register updated |
| ACT-14 | MCA form preparation tracking (per form) | 60 | Task → SRN captured |
| ACT-15 | Labour register update (per month per establishment) | 180 | Period → registers generated |
| ACT-16 | DPDP rights request handling | 90 | Request → closure |
| ACT-17 | Risk & control self-assessment (per unit) | 480 | Campaign → submission |
| ACT-18 | Stress-test run and report | 1,440 | Scenario set-up → report approved |
| ACT-19 | ICAAP document compilation | 4,800 | Workspace open → board draft |
| ACT-20 | Internal-audit report drafting | 960 | Fieldwork close → draft report |
| ACT-21 | Translation of a 5-page vernacular document | 150 | Upload → approved type copy |
| ACT-22 | Typing a handwritten/WhatsApp evidence page | 20 | Upload → approved type copy |
| ACT-23 | Calendar maintenance for statutory dates (per month) | 240 | Automated |
| ACT-24 | Committee charter/ToR update | 120 | Draft → approval |

### N.9.4 Penalty library bindings (seed; each rule lives in Appendix G with citation and `last_verified_at`; all [VERIFY])

| Rule ref | Obligation family | Penalty function | Source |
|---|---|---|---|
| LR-MCA-PEN-01 | Late MCA e-forms (AOC-4, MGT-7/7A, ADT-1, DIR-12 etc.) | ₹100 × days late per form (no cap) | Companies Act 2013 s.403; Companies (Registration Offices and Fees) Rules 2014 |
| LR-MCA-PEN-02 | DIR-3 KYC | ₹5,000 flat | Companies (Appointment and Qualification of Directors) Rules 2014 r.12A [VERIFY] |
| LR-MCA-PEN-03 | LLP Form 8/11 | Multiple of normal fee by delay band | LLP (Amendment) Rules 2022 [VERIFY] |
| LR-GST-PEN-01 | GSTR-1/GSTR-3B late | ₹50/day (₹20 nil) capped ₹2,000 / ₹5,000 / ₹10,000 by AATO band | CGST Act s.47; Notifications 19/2021-CT, 20/2021-CT [VERIFY] |
| LR-GST-PEN-02 | Late tax payment | 18% p.a. interest | CGST Act s.50(1) |
| LR-SEBI-PEN-01 | LODR SOP fines (Reg 6(1), 17–21 per day; 13(3), 23(9), 24A, 27(2), 29, 31, 33, 34, 44(3) per instance) | Per annexure amounts | SEBI Master Circular SEBI/HO/CFD/PoD2/CIR/P/0155 (11 Nov 2024) [VERIFY amounts] |
| LR-SEBI-PEN-02 | Minimum public shareholding | ₹5,000/day; ₹10,000/day after 1 year | Same |
| LR-IT-PEN-01 | Late TDS returns | Fee per day under the Income-tax Act 2025 (successor of s.234E) | Income-tax Act 2025 [VERIFY section/amount] |
| LR-RBI-PEN-01 | RBI monetary penalties (NBFC, banks, UCBs) | Not modelled per day — show public penalty cases as context only (aggregate) | RBI Act s.58G; BR Act s.47A [VERIFY caps] |
| LR-MOLE-PEN-01 | Labour Code register/return defaults | Fine bands per Code; modelled only as "exposure range" | Code on Wages s.54; OSH Code; SS Code; IR Code [VERIFY; Appendix T] |

Rules unverified for more than 180 days are excluded from Modelled tiles (P20 FR-P20-67).

## N.10 Pricing-page FAQs (seed; 28)

1. *Is there a free trial?* Yes — 7 days with Professional features. No card needed. It never turns into a paid plan unless you choose one.
2. *What happens when my trial ends?* Your workspace becomes read-only for 30 days. You can export everything or choose a plan to continue.
3. *Are prices inclusive of GST?* Prices exclude GST. The GST amount and total appear before you pay and on your tax invoice.
4. *Can I pay monthly?* Yes. Annual billing costs less; both are shown.
5. *Which package is right for an NBFC?* Base Layer NBFCs usually start with Essentials plus the RBI-NBFC pack; Middle and Upper Layer NBFCs usually need Professional with Risk Lab and Return Studio. The configurator recommends based on your entity type.
6. *Can I buy only labour-law compliance or only HRMS?* Yes — standalone Labour & POSH, HRMS, Grievance Desk, Board Portal and Data Protection products are available.
7. *Can I add regulator packs later?* Yes, any time. You pay the prorated amount for the rest of your term.
8. *Do you file returns with RBI or other regulators for us?* LawDocsComply prepares and validates upload-ready files and records the acknowledgement. Submission is done by your authorised officer on the regulator's portal.
9. *Is my data stored in India?* Yes. Primary and disaster-recovery copies are in Indian regions.
10. *Do you train AI on our data?* No.
11. *What are Vidhi AI credits?* Credits measure AI actions like drafting minutes or translating a document. Each package includes a monthly allowance. Deadline calculations and compliance logic never use credits.
12. *Can we leave and take our data?* Yes. Export everything as folders of Word, Excel and PDF files with an index, at any time, including after cancellation for 30 days.
13. *Do you offer discounts for co-operative societies, NGOs or startups?* Yes, with documentary proof. See the discount note under each package.
14. *Can our auditors and the regulator get access?* You can give time-limited, read-only access to auditors and, if you choose, to a regulator's inspecting officer. It is logged and you can revoke it.
15. *Can our CA/CS firm use LawDocsComply for our company?* Yes. You can give your consultant a maker account with a contract end date. LawDocs' own relationship managers can also work for you under a retainer.
16. *What is the difference between the software and the marketplace?* The software is a subscription. The marketplace sells expert services (retainers, drafting, ICAAP, certification readiness, trainings). You can buy either or both.
17. *Do you integrate with Tally Prime?* Yes, through Return Studio's import (Professional and Enterprise).
18. *Do you integrate with Microsoft 365 and Google Workspace?* Yes — calendar, storage links and e-mail.
19. *How do upgrades and downgrades work?* Upgrades apply immediately with a prorated charge. Downgrades apply at the end of your term.
20. *How do I cancel?* Settings › Billing › Cancel. It takes the same number of steps as buying.
21. *Will non-payment stop us from meeting a deadline?* No. Read, export, auditor access and work already started for a statutory deadline continue. Only new users and new modules are restricted.
22. *Can we get an invoice with our GSTIN?* Yes. Add GSTINs for each State in your billing profile.
23. *Do you support e-invoicing?* Invoices carry IRN and QR code where e-invoicing applies to our selling entity.
24. *Can we pay by bank transfer or PO?* Yes, for annual and Enterprise plans.
25. *Is LawDocsComply SOC 2 or ISO 27001 certified?* We show certifications only when we hold them. See the Trust page for current status.
26. *What does "regulator pack" mean?* A curated set of obligations, questions and calendars for one regulator and entity type, kept current by our content team.
27. *Can we customise the questions?* Yes. Edit text, add questions and change owners; your changes apply only to your company and are audit-trailed.
28. *Is the health check really free?* Yes. It gives an indicative score and report; it is not legal advice or an audit.

## N.11 Billing notification templates (codes)

`BIL-N-01` trial started · `BIL-N-02` trial T-3 · `BIL-N-03` trial T-1 · `BIL-N-04` trial expired · `BIL-N-05` deletion notice · `BIL-N-06` trial extended by LawDocs · `BIL-N-07` quote ready · `BIL-N-08` purchase approval needed · `BIL-N-09` payment received · `BIL-N-10` payment failed · `BIL-N-11` invoice issued · `BIL-N-12` courtesy pre-debit notice · `BIL-N-13` usage 80% · `BIL-N-14` usage 100% · `BIL-N-15` AI credits 20% · `BIL-N-16` AI credits 5% · `BIL-N-17` renewal T-90 · `BIL-N-18` renewal T-30 · `BIL-N-19` renewal T-7 · `BIL-N-20` price-change notice · `BIL-N-21` plan changed · `BIL-N-22` component attached · `BIL-N-23` component scheduled for removal · `BIL-N-24` past due · `BIL-N-25` restriction notice (7 days) · `BIL-N-26` restricted · `BIL-N-27` termination notice · `BIL-N-28` cancellation confirmed · `BIL-N-29` savings report ready · `BIL-N-30` add-on requested by a user. Mandatory (non-mutable): 08, 10, 24, 25, 26, 27.

## N.12 Benefit explanations (R-037) — short copy used in configurator cards and settings

| Choice | Benefit statement |
|---|---|
| Annual billing | "Pay less than monthly and lock your price for the year." |
| Professional over Essentials | "Multi-level maker-checker, policy drafting with Vidhi, board portal and risk register — what regulated entities are inspected on." |
| Risk Assessment Lab | "Run ICAAP, stress tests and capital ratios with numbers you can reproduce for the board and the inspector." |
| Return Studio | "Turn Tally, Excel or LMS data into upload-ready return files, with validations before you file." |
| Labour & POSH | "All Labour Code registers and returns, and a confidential POSH committee workspace." |
| HRMS & Payroll | "One employee master for HR, payroll, labour registers and people-risk analysis." |
| Data Protection & Cyber | "DPDP notices, rights requests and breach clocks, plus CERT-In and ISO control tracking." |
| Board Portal | "Board packs, minutes and resolutions with Secretarial Standards checks — in one secure place." |
| Grievance Desk | "Customer complaints from your website, handled with regulatory timelines and Ombudsman tracking." |
| BYO storage | "Keep your documents in your own storage; LawDocsComply keeps the index and workflow." |
| AI credit packs | "More drafting, translation and OCR when you need it; unused purchased credits last 12 months." |
| Retainer (marketplace) | "A LawDocs relationship manager works as your maker; your team stays the checker." |

## N.13 Unit-economics guard-rails (for the pricing committee; private)

| Metric | Guard-rail `[OWNER TO SET]` |
|---|---|
| Gross margin per package | ≥ 75% after hosting, AI inference, support allocation |
| AI cost per credit | ≤ 40% of credit price at blended model mix; review monthly |
| Pass-through margin | Disclosed; ≤ 20% over cost |
| Implementation margin | ≥ 30% |
| Retainer utilisation | 70–85% of hour bank |
| Discount authority | Per OH11 DoA; > 25% to CEO (OH8 acceptance test) |
| CAC payback | ≤ 12 months for Essentials; ≤ 18 months for Professional |

## N.14 Sources (accessed 25 October 2026)

1. LawDocsComply pricing page (observed 25 Oct 2026). 2. Operations Hub v1.0 OH8.2–OH8.10. 3. Ecosystem Spec v1.1 §6.27. 4. Companies Act 2013 s.403; SEBI Master Circular SEBI/HO/CFD/PoD2/CIR/P/0155 (11 Nov 2024); CGST Act ss.47, 50, 52. 5. Vanta pricing observations (benchmark) — https://soc2auditors.org/insights/vanta-pricing/ . 6. Razorpay Subscriptions update docs. 7. CCPA Dark Patterns Guidelines 2023; Consumer Protection (E-Commerce) (Amendment) Rules 2026.

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular X-02 — prices, tax, quotes, orders, invoices, credit notes, payments and dunning are the Operations Hub OH8 billing engine's; LDC holds the presentation catalogue, configurator rules, entitlements, meters, trials and savings. Seed prices are owner decisions (`02` §4 item 5). Where text above conflicts with them, the master prevails.
