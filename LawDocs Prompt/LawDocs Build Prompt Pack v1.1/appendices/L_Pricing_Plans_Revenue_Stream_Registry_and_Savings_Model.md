# Appendix L — Pricing, Plans, Revenue-Stream Registry and Savings Model

**Status:** Binding for structure, codes, rules, formulas and defaults of switches; **Reference** for every price (all prices are indicative seeds from R6, ex-GST, INR, `[OWNER TO SET]` until the owner approves catalogue v1 in OH8).
**Used by:** P17 (primary), P16, P14, P15, P18, P21 (pricing page copy), P09 (AI credit rates), P22 (mobile display).

**How to use.** P17 builds the presentation catalogue, credits, meters, stream registry and Savings & Value from this appendix. Prices, SKUs, coupons and stream gates are commercial data owned by OH8 (Ecosystem Spec §6.27; OH8.2–OH8.3): the coding agent loads the tables below as **seed data** for the presentation catalogue and as **catalogue change requests** to OH8, never as constants in code. Where a row says [VERIFY], [TAX MEMO], [COUNSEL] or [OWNER], the related switch stays OFF or the related copy stays hidden until the item is closed (NN-38). Benchmarks carry the R6 IDs (B-xx) so the Savings model can cite them.

---

## L.0 Precedence and conventions

1. OH8 prevails on price, tax, SKU, coupon and gate status; this appendix prevails on presentation, feature rows, credit semantics, savings methodology and LawDocs-side switch defaults; Appendix M prevails on marketplace service definitions and professional rules; conventions §7 (NN) prevail over everything here.
2. Prices are ex-GST unless marked "incl. GST". GST shown at 18% is a tax hint for LawDocs's own supplies pending the tax memo; pass-through amounts (stamp duty, government, court and registry fees) are never taxed by LawDocs and never discounted.
3. "Monthly" = annual ÷ 12 × 1.2, rounded down to a ₹9 ending (R6 §R6.2.1 principle 5).
4. Codes: plans `PLN-FREE`, `PLN-PERSONAL`, `PLN-PRO`, `PLN-BUSINESS`, `PLN-ENTERPRISE`; add-ons `LD-ADD-*`; credit packs `LD-CRD-*`; meters UPPER_SNAKE; streams `RS-LD-nn`; feature rows `F-nnn`; activities `ACT-LD-nn`; benchmarks `BM-nn`; exposure bindings `PX-nn`; refund rules `RF-nn`; FAQs `FAQ-nn`; notification templates `NT-BIL-nn`.

## L.1 Pricing principles

| # | Principle | Source |
|---|---|---|
| PP-LD-01 | Free plan vault within its storage limit (no perpetual-storage claim [OWNER]); export never paywalled | R6 §R6.2.1(1); NN-11 |
| PP-LD-02 | Software and services are separate; anyone can buy a service without a plan; plans add allowances and member prices | R-040; R6 §R6.2.1(2) |
| PP-LD-03 | Meter only what has a unit cost (Aadhaar eSign, eStamp facilitation, AI-heavy jobs, licensed court-data refresh, storage overage); reading, storing, sharing, reminders and deterministic tools are free | R6 §R6.2.1(3) |
| PP-LD-04 | No per-minute advocate billing; consultations are flat fixed-duration slots by practice area | R6 LD-X01; R1 §3.7 |
| PP-LD-05 | Annual default; monthly carries a disclosed +20% uplift | R6 §R6.2.1(5) |
| PP-LD-06 | Landed price before payment: fee + platform fee (if any) + government fee estimate + GST = total | R1 IMP-079; NN-22, NN-50 |
| PP-LD-07 | Credits are prepaid units of LawDocs's own services, never a rupee wallet; one expiry rule everywhere; failed services return credits | R1 IMP-085; P17 FR-P17-36 |
| PP-LD-08 | No trial auto-conversion, no countdown timers, no anchor prices, no pre-ticked add-ons; cancel as easy as buy | OH8.9; R3 LG-142 |
| PP-LD-09 | No money from regulated professionals for listing, ranking, leads, badges or a share of fees; no referral rewards to them | NN-21; R6 RS-LD-27–29 |
| PP-LD-10 | Group neutrality: regulated-entity customers may be referred to LawDocsComply; no tying, no bundle discount that links products unless OH8 legality gate approves | R6 §R6.2.2 note; OH8.2 |
| PP-LD-11 | Price changes only at renewal with ≥ 30 days' notice | OH8.4 |
| PP-LD-12 | Every value claim (savings, "worth ₹x") cites a dated benchmark and passes the claims gate | NN-20, NN-36 |

## L.2 Plan summary (pricing-page cards)

| Attribute | Free | Personal | Pro | Business | Enterprise |
|---|---|---|---|---|---|
| For | Anyone | Individuals and families | Professionals, freelancers, sole proprietors, startups | Companies, LLPs, NBFCs, groups | Banks, large NBFCs, groups, platforms |
| Annual (ex-GST) | ₹0 | ₹1,499 | ₹9,999 per workspace | ₹59,999 | from ₹3,00,000 or quote |
| Annual incl. 18% GST | ₹0 | ₹1,768.82 | ₹11,798.82 | ₹70,798.82 | from ₹3,54,000 |
| Monthly (ex-GST / incl. GST) | — | ₹149 / ₹175.82 | ₹999 / ₹1,178.82 | ₹5,999 / ₹7,078.82 | quote |
| Annual saving vs monthly | — | ₹289 (16%) | ₹1,989 (16.6%) | ₹11,989 (16.7%) | — |
| Seats / members | 1 | Owner + 4 family members | 3 working seats | 10 working seats + unlimited free viewer/approver/board/auditor seats | Bands |
| Vault storage | 1 GB | 10 GB | 50 GB | 250 GB | 1 TB+ and BYO storage |
| Vidhi AI credits / month | 30 | 300 | 1,500 | 6,000 | 25,000+ |
| Aadhaar eSign credits included | 0 (₹29 per use) | 2 / month | 10 / month | 50 / month | Contracted volume |
| Electronic (OTP) signatures | 5 / month | Unlimited (fair use) | Unlimited | Unlimited | Unlimited |
| eStamp facilitation | Per use | Per use at member price | 2 / month (duty extra) | 10 / month (duty extra) | Volume |
| Litigation tracker | 1 case | 5 cases | 50 matters | 300 matters | Bands |
| Trademark tracker | 1 application | 3 applications | 10 marks + journal watch | 50 marks + watch | Unlimited |
| Documentation-team consult allowance (LawDocs team; advocate consultations are billed separately by the advocate [COUNSEL]; CH-08, NN-21) | — | 1 × 15-min / year | 2 × 30-min / year | 6 × 30-min / year | Retainer |
| Member price on LawDocs services | — | 5% off | 5% off | 10% off | Contract |
| Support | Help centre, Vidhi | E-mail and chat | Priority chat | Phone + onboarding manager (30 days) | Named CSM, SLA |
| Trial | — | 14 days | 14 days | 14 days or guided pilot | Pilot |
| CTA | "Start free" | "Start 14-day trial" | "Start 14-day trial" | "Start 14-day trial" / "Book a demo" | "Talk to us" |

**Evidence anchors (R6 §R6.2.2).** Personal at ₹1,499/yr is about one-eighth of Rocket Lawyer Standard ($149/yr, B-04) and about 50 LegalKart chat minutes (B-02); its 24 included Aadhaar eSigns are worth ₹360–₹600 at published per-signatory retail of ₹15–₹25 (B-16, B-25). Pro sits below one Clio EasyStart seat for a year (B-29). Enterprise starts where Leegality enterprise contracts are reported (₹25,000–₹50,000/month, B-19, secondary). These anchors may appear in "Benefits explained" only with the source date and claims-gate PASS.

## L.3 Full feature lists per plan (comparison-table seed; 110 rows)

Legend: ✓ included · — not available · number = limit · "add-on" = available for a price (L.4) · "credits" = uses credits (L.5). Every row has an "i" explainer key `hlp.bil.f<nnn>`.

| Code | Feature | Free | Personal | Pro | Business | Enterprise |
|---|---|---|---|---|---|---|
| **A. Account and workspaces** ||||||| 
| F-001 | Personal workspace for the account holder | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-002 | Company workspace | Buyer-only (services) | — | 1 | 1 | Groups |
| F-003 | Legal entities per Company workspace | — | — | 1 | 3 | Bands |
| F-004 | Family members | — | 5 incl. owner (+5 add-on) | — | — | — |
| F-005 | Working seats | 1 | Owner + family | 3 | 10 | Bands |
| F-006 | Free viewer, approver, board and auditor seats | — | — | 5 | Unlimited | Unlimited |
| F-007 | Free counterparty guests (negotiate, sign, witness) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-008 | Login by OTP, passkey, password + MFA | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-009 | Google / Microsoft sign-in | — | ✓ | ✓ | ✓ | ✓ |
| F-010 | SAML/OIDC SSO and SCIM provisioning | — | — | — | add-on | ✓ |
| F-011 | Personal ↔ Company context switcher | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-012 | Ten Indian UI languages + English (D-07) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-013 | Mobile apps (iOS, Android) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-014 | Accessibility: screen-reader support, captions, keyboard, high contrast | ✓ | ✓ | ✓ | ✓ | ✓ |
| **B. Legal Vault and DMS** ||||||| 
| F-020 | Vault storage | 1 GB | 10 GB | 50 GB | 250 GB | 1 TB+ |
| F-021 | Originals locked and hashed (SHA-256) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-022 | Folders, tags, metadata, full-text search, filters | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-023 | Version history | 10 per document | Unlimited | Unlimited | Unlimited | Unlimited |
| F-024 | Selective sharing (expiry, watermark, view-only) | View links | ✓ | ✓ | ✓ | ✓ |
| F-025 | DigiLocker document pull (URI + verification) | — | ✓ | ✓ | ✓ | ✓ |
| F-026 | Bulk upload by folder structure | — | 500 files / batch | 2,000 / batch | 10,000 / batch | Unlimited |
| F-027 | Nominee and emergency access | ✓ | ✓ | n/a | n/a | n/a |
| F-028 | Printed-document OCR (deterministic) | 20 pages / month | 300 / month | 1,500 / month | 7,500 / month | Contracted |
| F-029 | Handwriting and WhatsApp-screenshot typed copy (labelled) | credits | credits | credits | credits | credits |
| F-030 | Translation to English (labelled machine translation) | credits | credits | credits | credits | credits |
| F-031 | Retention schedules and legal hold | — | — | ✓ | ✓ | ✓ |
| F-032 | Encrypted offline vault on mobile | — | ✓ | ✓ | ✓ | ✓ |
| F-033 | Advanced DMS pack (bulk extraction, classification rules, batch translation) | — | add-on | add-on | ✓ | ✓ |
| **C. Drafting and Vidhi AI** ||||||| 
| F-040 | Vetted template library (template automation) | Unlimited drafts | Unlimited | Unlimited | Unlimited | Unlimited |
| F-041 | Watermark-free downloads | 3 / month | Unlimited | Unlimited | Unlimited | Unlimited |
| F-042 | Vidhi AI credits included per month | 30 | 300 | 1,500 | 6,000 | 25,000+ |
| F-043 | AI-customised drafts labelled "AI draft — not reviewed" with one-click paid review | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-044 | Vidhi answers with sources and dates; unverified citations flagged | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-045 | Clause library | — | — | ✓ | ✓ + custom clauses | ✓ |
| F-046 | Company templates and playbooks | — | — | 10 | Unlimited | Unlimited |
| F-047 | Vidhi role-agent seats (e.g., Contract Clerk) | — | — | add-on | add-on | 3 included |
| F-048 | Co-authoring in your Microsoft 365 or Google Workspace | — | — | ✓ | ✓ | ✓ |
| **D. Negotiation and CLM** ||||||| 
| F-050 | Share for comment | View-only | ✓ | ✓ | ✓ | ✓ |
| F-051 | Track changes, redlines, versions per round | — | ✓ | ✓ | ✓ | ✓ |
| F-052 | Deal-room messaging with counterparties | — | ✓ | ✓ | ✓ | ✓ |
| F-053 | Approval workflows (maker-checker, DoA) | — | — | 1 step | Multi-step | Custom |
| F-054 | Contract repository with key dates | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-055 | Renewal and expiry reminders | 3 active | Unlimited | Unlimited | Unlimited | Unlimited |
| F-056 | Obligation extraction and renewal desk | — | — | Basic | ✓ | ✓ |
| F-057 | Advanced CLM (playbook review, clause analytics) | — | — | add-on | add-on | ✓ |
| F-058 | Bulk agreement generation from a sheet | — | — | 50 / batch | 1,000 / batch | API |
| F-059 | Virtual data room | — | — | add-on | add-on | ✓ |
| **E. eSign, eStamp and execution** ||||||| 
| F-060 | Aadhaar eSign credits included | 0 | 24 / year (2 / month) | 10 / month | 50 / month | Contracted |
| F-061 | Electronic (OTP / e-mail) signatures | 5 / month | Fair use | Unlimited | Unlimited | Unlimited |
| F-062 | DSC signing with the signer's token | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-063 | Instrument eligibility check and wet-ink / notary / registration packs | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-064 | eStamp facilitation (duty at actuals) | Per use | Member price | 2 / month | 10 / month | Volume |
| F-065 | Stamp-duty calculator by State | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-066 | Signing order, reminders, parallel signing | Basic | ✓ | ✓ | ✓ | ✓ |
| F-067 | Evidence pack and BSA 2023 s.63(4) certificate draft | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-068 | Witness, notary and registration tracker (formalities gate) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-069 | Bulk signing and signing by API | — | — | — | ✓ | ✓ |
| **F. Litigation** ||||||| 
| F-070 | Case tracker (user-entered CNR / case numbers) | 1 | 5 | 50 | 300 | Bands |
| F-071 | Hearing alerts and calendar | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-072 | Licensed court-data refreshes included per month [OWNER TO SET] | Manual only | 30 | 300 | 2,000 | Contracted |
| F-073 | "What this status means" explainers for litigants | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-074 | Limitation calculator | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-075 | Pleadings and notices studio | Templates | ✓ | ✓ | ✓ | ✓ |
| F-076 | Order and judgment OCR and summary | credits | credits | credits | credits | credits |
| F-077 | Matter management (tasks, counsel, documents, spend) | — | — | ✓ | ✓ | ✓ |
| F-078 | Contingent-liability and litigation MIS | — | — | — | ✓ | ✓ |
| F-079 | Litigation pack (+100 matters, extra forums) | — | — | add-on | add-on | ✓ |
| **G. Trademarks and IP** ||||||| 
| F-080 | Trademark portfolio tracker | 1 | 3 | 10 | 50 | Unlimited |
| F-081 | Deadline engine (renewals, replies, oppositions) | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-082 | Pre-filing knock-out search (advisory) | 1 / month | 5 / month | 25 / month | 100 / month | Contracted |
| F-083 | Journal similarity watch | — | — | 10 marks | 50 marks | ✓ |
| F-084 | Reply and opposition drafting templates | — | ✓ | ✓ | ✓ | ✓ |
| F-085 | Trademark watch pack (+25 marks) | — | — | add-on | add-on | ✓ |
| **H. Company Legal Department OS** ||||||| 
| F-090 | Legal intake desk for departments | — | — | ✓ | ✓ | ✓ |
| F-091 | Legal calendar and task assignment | Personal | Personal | ✓ | ✓ | ✓ |
| F-092 | CLO dashboard | — | — | Lite | ✓ | ✓ |
| F-093 | Counsel panel and legal spend | — | — | — | ✓ | ✓ |
| F-094 | Departments, positions and delegations | — | — | Basic | ✓ | ✓ |
| F-095 | Maker-checker with segregation of duties | — | — | ✓ | ✓ | ✓ |
| F-096 | Open, interim and waiting items (customisable) | ✓ | ✓ | ✓ | ✓ | ✓ |
| **I. Governance and HRMS-lite** ||||||| 
| F-100 | Board, committees, meetings, minutes, resolutions | — | — | Lite (1 entity) | ✓ (3 entities) | Groups |
| F-101 | Statutory registers | — | — | Lite | ✓ | ✓ |
| F-102 | Board and secretarial pro pack | — | — | add-on | add-on | ✓ |
| F-103 | HRMS-lite (people, KMP, directors, duties) | — | — | add-on | add-on | ✓ |
| F-104 | Single sign-on with LawDocsComply when you use both | — | — | ✓ | ✓ | ✓ |
| **J. Tax and business services** ||||||| 
| F-110 | ITR document checklist | ✓ | Self-prep checklist | — | — | — |
| F-111 | GST / TDS / ROC calendars | — | — | GST, TDS | GST, TDS, ROC | Custom |
| F-112 | Startup kit (founders' agreement, ESOP, SHA, NDA packs) | — | — | ✓ | — | — |
| F-113 | Member price on business services | — | 5% off | 5% off | 10% off | Contract |
| **K. Consumer Help (separate brand)** ||||||| 
| F-120 | Track your own complaints (loans, insurance, challans) | ✓ | ✓ | ✓ | — | — |
| F-121 | Grievance templates and official escalation paths | Basic | ✓ | ✓ | — | — |
| F-122 | Challan status with official payment deep-links | ✓ | ✓ | ✓ | — | — |
| **L. Marketplace and Academy** ||||||| 
| F-130 | Buy any service without a plan | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-131 | Documentation-team consult allowance (advocate consultations billed separately by the advocate [COUNSEL]) | — | 1 × 15 min / year | 2 × 30 min / year | 6 × 30 min / year | Retainer |
| F-132 | Member price on LawDocs services | — | 5% off | 5% off | 10% off | Contract |
| F-133 | Retainers (Startup Legal Officer, SME Legal Desk, NBFC Retainer, Managed Legal Department) | — | — | Available | Available | Available |
| F-134 | FinLegal Academy seats included | — | — | — | 2 / year | 5 / year |
| **M. Integrations and API** ||||||| 
| F-140 | Export push to OneDrive / SharePoint / Google Drive | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-141 | Webhooks | — | — | ✓ | ✓ | ✓ |
| F-142 | API access tier | — | — | add-on | add-on | ✓ |
| F-143 | Group connectors (LawDocsComply, Equator, Finbyx, Udofin) with consent | — | — | ✓ | ✓ | ✓ |
| F-144 | Bring-your-own storage and scheduled export | — | — | — | add-on | ✓ |
| F-145 | White-label practice workspace (firms serving clients) | — | — | add-on | — | ✓ |
| F-146 | Embedded agreement + eSign + eStamp (B2B2C) | — | — | — | — | ✓ |
| **N. Security and administration** ||||||| 
| F-150 | MFA and passkeys | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-151 | Audit trail | Own activity | ✓ | ✓ | ✓ full | ✓ + SIEM export |
| F-152 | Access-transparency log for LawDocs staff and professionals | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-153 | Client-owned credential vault (off until you enable it) | — | — | — | ✓ | ✓ |
| F-154 | IP allow-lists and device policies | — | — | — | ✓ | ✓ |
| F-155 | Data stored in India | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-156 | Dedicated environment (monthly rental) | — | — | — | — | Option |
| **O. Export and portability** ||||||| 
| F-160 | Full export in human-readable folders (LD-EXPORT-1.0), any time | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-161 | Scheduled exports | — | — | — | With BYO add-on | ✓ |
| F-162 | Data escrow | — | — | — | — | Option |
| **P. Support and onboarding** ||||||| 
| F-170 | Help centre, tutorials, "i" glossary, Vidhi help | ✓ | ✓ | ✓ | ✓ | ✓ |
| F-171 | Human support | — | E-mail and chat | Priority chat | Phone | Named CSM |
| F-172 | Onboarding manager | — | — | — | 30 days | ✓ |
| F-173 | Premium support (4-hour response) | — | — | add-on | add-on | ✓ |
| F-174 | Implementation and migration package | — | — | — | Paid option | Quote |
| F-175 | Savings & Value dashboard | ✓ | ✓ | ✓ | ✓ + quarterly value report | ✓ |

## L.4 Add-ons (per year unless stated; ex-GST; `[OWNER TO SET]`)

| Code | Add-on | Personal | Pro | Business | Ent. | Indicative price | Dependencies / note | Stream |
|---|---|---|---|---|---|---|---|---|
| LD-ADD-FAM | Family extension (+5 members) | A | — | — | — | ₹999 / yr | — | RS-LD-05 |
| LD-ADD-SEAT | Extra working seat | — | A | A | band | ₹1,999 / yr (Pro); ₹4,999 / yr (Business) | Provakil ₹500/user/month benchmark (B-27) | RS-LD-06 |
| LD-ADD-LIT | Litigation pack (+100 matters, NCLT/DRT/consumer coverage, order OCR) | — | A | A | ✓ | ₹2,500 / month | Licensed court-data provider live | RS-LD-05, RS-LD-12 |
| LD-ADD-TMW | Trademark watch (+25 marks, weekly journal similarity) | — | A | A | ✓ | ₹1,500 / month | Licensed TM data route [VERIFY] | RS-LD-13 |
| LD-ADD-CLM | Advanced CLM | — | A | ✓ | ✓ | ₹3,000 / month | — | RS-LD-05 |
| LD-ADD-DMSX | Advanced DMS | A | A | ✓ | ✓ | ₹499 / month (Personal); ₹2,000 / month (Pro) + AI credits | — | RS-LD-05 |
| LD-ADD-DR | Virtual data room | — | A | A | ✓ | ₹4,999 per room / 90 days; ₹1,999 per extra month | — | RS-LD-14 |
| LD-ADD-GOV | Board and secretarial pro | — | A | A | ✓ | ₹2,500 / month | Where tenant uses LDC, LDC is SoR (NN-47) | RS-LD-05 |
| LD-ADD-HR | HRMS-lite | — | A | A | ✓ | ₹40 per employee / month, minimum ₹1,500 | Labour rulepack (shared kernel) | RS-LD-05 |
| LD-ADD-SSO | SSO + SCIM | — | — | A | ✓ | ₹1,500 / month | — | RS-LD-05 |
| LD-ADD-API | API access tier | — | A | A | ✓ | ₹5,000 / month + overage (L.8) | API terms accepted | RS-LD-16 |
| LD-ADD-BYO | BYO storage / scheduled export | — | — | A | ✓ | ₹2,000 / month | P20 storage targets | RS-LD-42 |
| LD-ADD-SUP | Premium support | — | A | A | ✓ | ₹5,000 / month | — | RS-LD-15 |
| LD-ADD-WL | White-label practice workspace | — | A | — | ✓ | ₹4,999 / month + ₹299 per client workspace | No client-solicitation features; never creates a marketplace listing | RS-LD-18 |
| LD-ADD-AGT | Vidhi role-agent seat (400 credits/month) | — | A | A | ✓ | ₹1,500 per agent / month | Agent sponsor required (NN-43) | RS-LD-11 |
| LD-ADD-STO | Storage pack (+100 GB) | A (+20 GB ₹499/yr) | A | A | ✓ | ₹1,000 / month per 100 GB | — | RS-LD-05 |

## L.5 Credits and credit packs (prepaid service units; P17 §4H)

### L.5.1 Packs (one-time; valid 12 months; no auto top-up by default)

| Code | Pack | Units | Price | Unit price | Cost basis / evidence | Guard-rail |
|---|---|---|---|---|---|---|
| LD-CRD-ES1 | Aadhaar eSign — single | 1 | ₹29 | ₹29.0 | Leegality ₹25 (B-16); SignYu ₹15 (B-25); wholesale est. ₹8–20 (B-20) | Unit cost ≤ 60% of price |
| LD-CRD-ES10 | Aadhaar eSign — 10 | 10 | ₹249 | ₹24.9 | — | — |
| LD-CRD-ES50 | Aadhaar eSign — 50 | 50 | ₹999 | ₹20.0 | — | — |
| LD-CRD-ES250 | Aadhaar eSign — 250 | 250 | ₹4,499 | ₹18.0 | — | — |
| LD-CRD-ES1K | Aadhaar eSign — 1,000 (Business) | 1,000 | ₹15,999 | ₹16.0 | Needs negotiated wholesale ≤ ₹10 | — |
| LD-CRD-OTP100 | Electronic OTP/e-mail signatures beyond fair use | 100 | ₹499 | ₹5.0 | Leegality non-Aadhaar ₹15 (B-17) | — |
| LD-CRD-STP | eStamp facilitation | per stamp | ₹49 + duty at actuals; bulk series order fee ₹299 (≥ 10 stamps) | — | Leegality ₹45 + ₹500/order (B-18); Digio est. ₹30–50 (B-20) | Duty is pure agent, never a credit |
| LD-CRD-PHY | Physical stamp paper / franking courier | per order | ₹199 + duty + courier | — | State availability (P08) | — |
| LD-CRD-AI500 | Vidhi AI credits — 500 | 500 | ₹499 | ₹1.00 | Claude cost per credit measured monthly | AI cost ≤ 40% of credit price |
| LD-CRD-AI2K | Vidhi AI credits — 2,000 | 2,000 | ₹1,499 | ₹0.75 | — | — |
| LD-CRD-AI10K | Vidhi AI credits — 10,000 | 10,000 | ₹5,999 | ₹0.60 | — | — |
| LD-CRD-CRT100 | Court-data refreshes | 100 | ₹299 | ₹2.99 | Licensed aggregator PAYG (R6 §R6.6) | Pass-through + disclosed margin ≤ 20% |
| LD-CRD-CCOPY | Certified copy / order retrieval service (RS-LD-43 OFF) | per order | ₹99 + court fee at actuals | — | — | Advocate-only where rules require |

### L.5.2 Vidhi credit rate card (seed; R6 §R6.2.4; P09 owns runtime)

| Action | Credits |
|---|---|
| Standard chat turn | 1 |
| First draft from a vetted template (with AI customisation) | 5 |
| Full bespoke contract draft | 20 |
| Contract review with redlines | 15 per 10 pages |
| Handwriting / WhatsApp screenshot OCR + typed copy | 3 per page |
| Translation to English | 2 per page |
| Litigation order summary | 3 per order |
| Obligation extraction | 10 per contract |
| Notice / pleading first draft | 10 |
| Deterministic features (reminders, search, calendar, CNR display, stamp-duty calculator, limitation calculator) | 0 |

### L.5.3 Credit rules (one statement used everywhere)

"Credits are prepaid units of specific LawDocs services. They are not money, cannot be transferred or withdrawn and cannot pay professionals, stamp duty or government fees. Plan credits renew each period and do not roll over. Purchased credits are valid for 12 months; we remind you 30 and 7 days before expiry and will extend once by 6 months if you ask. Unused purchased credits are refundable pro rata within 30 days of purchase and when you close your account. If a service fails, the credit comes back automatically." [OWNER TO SET refund windows; COUNSEL/TAX MEMO per OI-P17-03.]

## L.6 One-time products (catalogue seeds; full definitions in Appendix M §M.2)

| Product | Indicative price (fee ex-GST; government fees at actuals) | Market evidence | Delivered by | Appendix M code |
|---|---|---|---|---|
| AI-drafted agreement from template (rent, sale, NDA, employment, vehicle sale, loan between individuals) | Free draft; ₹99 premium export | Owner hook; LegalKart charges for drafting | Vidhi (software) | SVC-AGR-01 |
| Professional review of a self-drafted agreement | ₹499 (≤ 5 pages) / ₹999 (≤ 15) / ₹1,999 (≤ 40) | Market ₹500–₹2,000; LegalKart ₹100/page (R1 IMP-030) | Panel advocate (M2) or LawDocs documentation review (M1) | SVC-REV-01 |
| Bespoke drafting by professional | ₹1,999–₹9,999 by complexity | — | Panel advocate / CS | SVC-AGR-10 |
| Legal notice drafting and dispatch | ₹1,499–₹2,999 + speed post at actuals | — | Advocate only (M2) | SVC-NTC-01 |
| Flat-fee consultation slot | 15 min ₹299–₹599; 30 min ₹599–₹1,499; 60 min ₹999–₹2,999 | LegalKart ₹31–₹69/min (B-01); LawRato ₹399/15 min (R1 §4.1) | Advocate / CA / CS (M2) | SVC-CON-01…03 |
| Private limited company incorporation | ₹2,999 + government fees + DSC | IndiaFilings ₹2,899 (B-06); LegalWiz ₹2,999 (B-10) | CS / CA | SVC-FIL-01 |
| LLP / partnership / proprietorship registration | ₹2,499–₹4,999 | IndiaFilings partnership ₹2,899 (B-09) | CS / CA | SVC-FIL-02…04 |
| Trademark search + filing (per class) | ₹1,999 + government fee ₹4,500 / ₹9,000 | Vakilsearch ₹1,499 (B-11); market ₹1,500–₹10,000 (B-15); fee B-13 | TM agent / advocate (M2) | SVC-TMK-01 |
| TM objection reply / opposition | ₹3,999 / ₹9,999+ | — | TM agent / advocate | SVC-TMK-03, -04 |
| GST registration / monthly return | ₹1,499 / ₹999 per month | IndiaFilings ₹1,499 / ₹998 (B-08) | CA / GST practitioner | SVC-FIL-10, -11 |
| ITR — CA-assisted (salaried / capital gains / business) | ₹999 / ₹2,499 / ₹4,999 | JioFinance ₹999; TaxBuddy ₹2,999 (B-14) | CA (taxpayer verifies) | SVC-FIL-20…22 |
| Income-tax / GST notice reply | ₹2,999–₹14,999 | — | CA / advocate | SVC-FIL-25 |
| Annual ROC compliance (small company) | ₹14,999 / year | IndiaFilings ₹19,899 bundle (B-07) | CS | SVC-GOV-05 |
| Policy drafting (HR, POSH, privacy, NBFC policies) | ₹4,999–₹49,999 per policy | — | LawDocs GRC professionals (M1) | SVC-POL-* |
| Annual report / board report drafting | ₹24,999–₹1,49,999 | — | LawDocs CS team (M1) | SVC-ARM-01, -02 |
| Stress testing, scenario analysis, risk assessment, compliance testing | ₹50,000–₹5,00,000 per engagement | LDC Risk Lab ADD-RAL ₹12,000/month as software alternative | LawDocs GRC professionals (M1) | SVC-RSK-*, SVC-CMP-* |
| Challan contest (court-referred traffic challan) | ₹999–₹2,999 + fine at actuals paid by the user on the official channel | ChallanPay/ChallanWallah model [VERIFY] | Advocate only (M2) | SVC-CHP-20 |

## L.7 Retainer packages (Appendix M category 09; P16 §4G)

**Structure rule for all retainers.** Legal advice and opinions are supplied by the LawDocs Panel advocates' firm in its own name (M2; invoice: advocate's bill — RCM for business clients, Notification 13/2017-CT(R) Sl. 2); coordination, documentation, compliance, secretarial support and RM services are supplied by LawDocs (M1; 18% forward charge). The client signs one envelope with two documents (P08). RS-LD-20/21 stay OFF until OI-P16-01 closes; until then retainers run with **M1 scope only** (no legal advice) and say so.

| Package | For | Monthly inclusions (seed) | Hour bank | Key SLAs (seed) | Roles | Exclusions | Indicative fee / month | Term / notice |
|---|---|---|---|---|---|---|---|---|
| **Startup Legal Officer** (RTN-SLO) | Pre-Series A startups, 1–50 staff | Contract reviews (up to 6 contracts ≤ 15 pages), founders/ESOP/SHA support, NDA desk, TM filings at member price, monthly compliance calendar, board-meeting kit (2/yr), Pro plan included | 6 h | Acknowledge 4 business hours; NDA turnaround 1 BD; contract review 3 BD; monthly report by 7th BD | RM (maker), panel advocate (advice), CS (ROC) | Litigation, fundraising negotiation beyond 2 rounds, attest work, filings with client credentials | ₹14,999–₹24,999 | 6 months min; 30 days |
| **SME Legal Desk** (RTN-SME) | SMEs, LLPs, family businesses | Vendor/customer contracts (up to 10), notices and replies (2), litigation tracking and counsel coordination, HR policies refresh, POSH IC support, monthly MIS | 10 h | Acknowledge 4 BH; contract review 3 BD; notice reply draft 5 BD; hearing-prep pack 2 BD before date | RM, panel advocate, LawDocs documentation team | Court appearance (separate engagement), attest work | ₹24,999–₹49,999 | 12 months; 60 days |
| **NBFC Legal & Compliance Retainer** (RTN-NBFC) | NBFC-BL/ML, HFCs, co-operative credit societies, IFSCA units | Loan-document and policy reviews, SARFAESI/IBC notice packs (drafting support), board-meeting support and minutes drafts, regulatory-change notes, returns calendar, dedicated RM as **maker user**, client officer as **checker** (R-064) | 20 h | Acknowledge 2 BH; policy review 10 BD; regulatory note 5 BD after a change; board pack 3 BD before meeting | RM (maker under grant), panel advocate (advice), LawDocs CS/GRC | Core management functions (policy approval, compliance function, KYC decisions — outsourcing directions [VERIFY current paras]); recovery agency work; attest | ₹50,000–₹2,50,000 | 12 months; 90 days |
| **Managed Legal Department** (RTN-MLD; RS-LD-21 OFF until structure memo) | Mid-size companies without in-house legal | Named legal manager (panel advocate), CLM operations, litigation management with external counsel panel, monthly board-ready legal MIS, intake desk run for the client, Business plan included | 40 h + named manager | Intake triage same BD; contract review 2 BD; MIS by 5th BD; SLA eSigned in tool | Legal manager (panel firm), RM, LawDocs paralegal team | Representation unless separately engaged; client's board decisions | ₹75,000–₹3,00,000 | 12 months; 90 days |
| **Custom retainer** (RTN-CUS) | Any | As scoped | As scoped | As scoped | As scoped | As scoped | Quote | As agreed |
| **Hour-bank top-up** (RS-LD-22) | Any retainer | Extra hours | — | — | — | — | ₹2,500–₹6,000 per hour by seniority | — |

Service credits (all packages): 5% of the monthly LawDocs fee per breached SLA category, capped at 20%; issued as OH8 credit notes; never a cash payment `[OWNER TO SET]`. Unused hours roll over one month. Utilisation target 70–85% (internal).

### L.7.1 Retainer SLA schedule seed (eSigned schedule; P16 FR-P16-47)

| Metric | Startup Legal Officer | SME Legal Desk | NBFC Legal & Compliance | Managed Legal Department | Credit on breach |
|---|---|---|---|---|---|
| Acknowledge a request | 4 business hours | 4 BH | 2 BH | 2 BH | Reported only |
| NDA / standard contract turnaround (≤ 15 pages, complete inputs) | 1 BD | 2 BD | 2 BD | 1 BD | 5% |
| Non-standard contract review | 3 BD | 3 BD | 5 BD | 2 BD | 5% |
| Legal notice reply draft | 5 BD | 5 BD | 3 BD | 3 BD | 5% |
| Policy review | — | 10 BD | 10 BD | 7 BD | 5% |
| Regulatory-change note after a relevant change | — | — | 5 BD | 5 BD | 5% |
| Board-meeting pack / minutes draft | 3 BD before / 5 BD after | 3 / 5 | 3 / 3 | 3 / 3 | 5% |
| Hearing-preparation pack | — | 2 BD before date | 2 BD | 2 BD | 10% |
| Statutory deadline support (inputs complete ≥ 7 BD before due) | Submission-ready ≥ 2 BD before due | same | same | same | 10% |
| Monthly service report | 7th BD | 7th BD | 5th BD | 5th BD | 2.5% |
| Cap per month | 20% | 20% | 20% | 20% | — |

Measurement: clocks on the IST business calendar of the client's State; client-caused delays and force majeure pause the clock; every breach is an `RetainerSLABreached` event visible to the client.

### L.7.2 Retainer pricing logic

Monthly fee = Σ (basket item × LawDocs unit price × expected monthly quantity) × (1 − retainer discount 10–20%) + hour bank × blended hourly rate + panel advocate fee schedule for advice hours (separate supplier line). Discounts above the delivery lead's DoA go to OH8 approval. Annual prepayment may carry a further disclosed discount (default 5%). Renewal pricing changes need ≥ 30 days' notice (PP-LD-11).

## L.8 Metered usage (API, white-label, enterprise and overage)

| Meter | Producer | Unit | Indicative price | Notes |
|---|---|---|---|---|
| `ESIGN_AADHAAR` | sgn | successful signatory | credits / ₹16–₹22 by commitment (API) | Failed = no charge |
| `SIGN_ELECTRONIC` | sgn | signature beyond fair use | ₹5 | — |
| `ESTAMP_FACILITATION` | sgn | stamp | ₹35–₹49 + duty (API) | Duty pure agent |
| `VIDHI_CREDITS` | ai | credit | ₹1.00 (B2C), ₹2.50 (B2B) beyond allowance | Hard stop by default |
| `COURT_DATA_REFRESH` | lit | matter refresh | ₹1.5–₹3 | Licensed provider |
| `TM_WATCH_MARKS` | ipm | mark-month | in add-on | — |
| `STORAGE_GB_MONTH` | dms | GB-month above quota | ₹1,000 per 100 GB-month | Overage opt-in only |
| `WHATSAPP_NOTIFY` | ntf | message | Meta India rate + ≤ 20% | Utility templates only |
| `API_CALLS` | int | 1,000 calls above tier | ₹100 | Rate limits separate |
| `API_AGREEMENT_GENERATE` | int | document | ₹10–₹25 by volume | Lenders, proptech, HR-tech |
| `MKP_CONSULT_ALLOWANCE` | mkp | consult | allowance only | Not billed |
| `SEATS_PEAK`, `FAMILY_MEMBERS` | iam/org | count | per add-on | Statement only |

## L.9 Revenue-stream registry (RS-LD-01 … RS-LD-45)

Columns follow P17 FR-P17-57. **Owner** codes: OWN project owner · REV revenue operations (OH8) · PRD head of product · DLV head of delivery · MKP marketplace lead · ACA Academy lead · PTN partnerships lead · CHB Consumer Help brand head · MKT marketing lead. **Effective** = earliest wave in which the stream may be activated (actual `effective_from` is set at OH8 activation). **Tax**: FC = forward charge 18% by the LawDocs selling entity [TAX MEMO for SAC]; PA = pure-agent lines (CGST Rules r.33); PRO = supplied by the professional in own name (advocate → individual: exempt; → business: RCM — R6 T-01/T-02); TCS/TDS = ECO obligations (CGST s.52; ITA 2025 s.393(1) Sl. 8(v) — R6 T-05/T-07). **Refund** codes in L.13.2. **Legal** Y = [COUNSEL]/[TAX MEMO] before ON. Kill-switch scope for every stream: stream × segment × channel × brand × profession (NN-39). Every ON/OFF change is maker-checker (NN-18).

| Code | Stream | Segment | Model / unit | OH8 type | Default | Owner | Effective | Disclosure (where, what) | Tax | Refund | Legal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RS-LD-01 | Personal membership | Individuals, families | Annual / monthly | SUBSCRIPTION | ON | PRD | W1 | Pricing card; renewal and cooling-off terms before payment | FC | RF-01, RF-02, RF-03 | N |
| RS-LD-02 | Pro subscription | Professionals, freelancers, startups | Per workspace + seats | SUBSCRIPTION | ON | PRD | W1 | Pricing card | FC | RF-01, RF-03 | N |
| RS-LD-03 | Business subscription | Companies, LLPs, NBFCs | Per workspace + band | SUBSCRIPTION | ON | PRD | W1 | Pricing card; order form | FC | RF-01, RF-03 | N |
| RS-LD-04 | Enterprise contracts incl. dedicated-environment rental | Banks, NBFCs, groups, platforms | Annual licence / monthly rental | SUBSCRIPTION / MONTHLY_RENTAL | ON | REV | W2 | MSA, DPA, RE outsourcing addendum | FC | RF-10 | Y |
| RS-LD-05 | Add-on components (L.4) | All paid | Monthly / annual add-on | SUBSCRIPTION | ON | PRD | W1–W2 | Add-on card with dependencies | FC | RF-01, RF-03 | N |
| RS-LD-06 | Extra seats | Pro, Business | Per seat | SUBSCRIPTION | ON | PRD | W1 | Seat page; proration preview | FC | RF-01 | N |
| RS-LD-07 | Aadhaar eSign credit packs | All | Prepaid credits | CREDIT_PACK (new, App. X) | ON | PRD | W1 | Credit rules statement (L.5.3) | FC [TAX MEMO voucher] | RF-04 | Y (ESP contract; PPI view) |
| RS-LD-08 | Electronic / OTP signature packs | All | Prepaid credits | CREDIT_PACK | ON | PRD | W1 | L.5.3 | FC | RF-04 | N |
| RS-LD-09 | eStamp facilitation | All | Per stamp + duty PA | PASS_THROUGH | ON per State rule pack | PRD | W1 | Facilitation fee line separate from duty (NN-08) | FC + PA | RF-08 | Y (State Acts; provider terms) |
| RS-LD-10 | Vidhi AI credit packs | All | Prepaid credits | CREDIT_PACK | ON | PRD | W1 | L.5.3; AI disclosure | FC | RF-04 | N |
| RS-LD-11 | Vidhi role-agent seats | Pro, Business, Ent. | Per agent / month | SUBSCRIPTION | ON | PRD | W3 | Agent card: sponsor, autonomy ceiling | FC | RF-01 | N |
| RS-LD-12 | Court-data refresh (pass-through + margin) | Pro, Business, Ent. | Per refresh / matter-month | PASS_THROUGH | ON (licensed provider only) | PRD | W2 | "Data from licensed provider; not real-time" (NN-20) | FC [TAX MEMO] | RF-04 | Y (provider licence; DPDP) |
| RS-LD-13 | Trademark watch | Pro, Business | Add-on | SUBSCRIPTION | ON | PRD | W2 | Coverage statement; advisory results | FC | RF-01 | N |
| RS-LD-14 | Virtual data room | Pro, Business, Ent. | Per room / period | ONE_TIME_SERVICE | ON | PRD | W2 | Room term and extension price | FC | RF-05 | N |
| RS-LD-15 | Premium support | All paid | Monthly | SUBSCRIPTION | ON | REV | W1 | Response targets | FC | RF-01 | N |
| RS-LD-16 | API access tier and overage | Platforms, lenders | Monthly + per call | PAYG | ON | PTN | W2 | API terms; rate card | FC | RF-10 | Y (API terms) |
| RS-LD-17 | Embedded / white-label agreement + eSign + eStamp (B2B2C) | Lenders, proptech, HR-tech | Per document / per sign | PAYG | ON | PTN | W2 | Contract; end-user notice that LawDocs is the processor | FC + PA | RF-10 | Y (RE outsourcing directions; ASP not sublet — NN-06) |
| RS-LD-18 | White-label practice workspace | Law / CA / CS firms | Monthly + per client workspace | SUBSCRIPTION | ON | PTN | W2 | "Software only; no listing; no client solicitation" | FC | RF-01 | Y |
| RS-LD-19 | One-time services by LawDocs (non-reserved) | All, no plan needed | Per order | ONE_TIME_SERVICE / PROFESSIONAL_SERVICES | ON | DLV | W1 | Landed price card; "LawDocs is not a law firm" | FC + PA | RF-05, RF-06 | Y (*A.K. Balaji* boundary — OI-P16-03) |
| RS-LD-20 | Retainers (Startup, SME, NBFC) | Startups, SMEs, FIs | Monthly / annual | RETAINER (new) | ON (M1 scope) | DLV | W2 | SLA schedule; split-supply statement | FC + PRO | RF-07 | Y (panel structure; RCM) |
| RS-LD-21 | Managed Legal Department | Mid-size companies | Monthly | MANAGED_SERVICES | OFF until structure memo | DLV | W2 | As RS-LD-20 + named manager | FC + PRO | RF-07 | Y |
| RS-LD-22 | Hour-bank top-ups | Retainer clients | Per hour | PROFESSIONAL_SERVICES | ON | DLV | W2 | Rate by seniority; approval before work | FC (+ PRO for panel hours) | RF-07 | N |
| RS-LD-23 | Buyer platform fee — flat per booking | Marketplace buyers | Flat ₹49–₹199 | MARKETPLACE_PLATFORM_FEE (new) | ON with M2 | MKP | W2 | Separate line "LawDocs platform fee"; not part of professional's fee | FC; TCS/TDS on professional supplies [TAX MEMO] | RF-05, RF-06 | Y (E-Commerce Rules 2020; any 2026 amendment [VERIFY]) |
| RS-LD-24 | Buyer platform fee as % of order (separate line) | Marketplace buyers | % | MARKETPLACE_PLATFORM_FEE | OFF | MKP | — | Separate line; % disclosed | FC | RF-05 | Y |
| RS-LD-25 | Take rate on non-regulated providers (translators, couriers, typists) | Providers | 10–20% | MARKETPLACE_REFERRAL | ON with third parties | MKP | W3 | Provider terms; seller details on listing | FC on fee; TCS | RF-05 | N |
| RS-LD-26 | Take rate on non-CA tax preparers / GST practitioners | Providers | ≤ 15% | MARKETPLACE_REFERRAL | OFF | MKP | — | Provider terms | FC; TCS | RF-05 | Y |
| RS-LD-27 | Commission / share of advocates', CAs', CSs', CMAs' fees | — | — | — | **PROHIBITED** | — | — | — | — | — | Deny |
| RS-LD-28 | Listing, featured, ranking, lead or badge fees from regulated professionals | — | — | — | **PROHIBITED** | — | — | — | — | — | Deny |
| RS-LD-29 | Referral rewards to regulated professionals | — | — | — | **PROHIBITED** | — | — | — | — | — | Deny |
| RS-LD-30 | Professional SaaS (Pro plan bought by a professional) | Professionals | Subscription | SUBSCRIPTION | ON | PRD | W1 | "Buying a plan does not list you or affect assignment" | FC | RF-01 | Y (never in ranking features) |
| RS-LD-31 | Academy courses (B2C) | Learners | Per course | TRAINING | ON (Academy merchant) | ACA | W1 | Academy terms; refund policy shown | Academy entity [TAX MEMO] | RF-09 | N |
| RS-LD-32 | Academy corporate licences and in-house batches | Companies, FIs | Per seat / annual | TRAINING | ON | ACA | W2 | Quote; seat terms | FC | RF-05 | N |
| RS-LD-33 | Events and webinars (paid) | Professionals, companies | Per ticket / sponsorship | TRAINING / ADVERTISING_SPONSORSHIP | OFF | MKT | — | Real dates, replay policy, no false urgency (R4 §11.3) | FC | RF-05 | Y (no repeat-player sponsors on consumer-help pages) |
| RS-LD-34 | Advertising on public content pages | Non-legal B2B vendors | Per slot / CPM | ADVERTISING_SPONSORSHIP | **OFF** | OWN | — | "Sponsored" label; contextual; public pages only (NN-35) | FC | — | Y (no advocates/CAs/CSs/lenders/insurers; no third-party ad scripts) |
| RS-LD-35 | User referral credits (user → user) | Individuals, SMEs | Credits to both | REFERRAL_CREDIT (new) | ON | MKT | W1 | Terms; endorsement disclosure | [TAX MEMO] | Credits per L.5.3 | N |
| RS-LD-36 | Affiliate programme (creators, bloggers, non-professional partners) | Affiliates | % of first-year subscription | AFFILIATE (new) | OFF | MKT | — | "#ad"/affiliate disclosure; ASCI rules | Affiliate's own | — | Y (no regulated professionals) |
| RS-LD-37 | Partner / reseller (software vendors, chambers, banks' SME desks) | Partners | Revenue share / wholesale | PARTNER_RESALE (new) | ON | PTN | W2 | Partner disclosure on co-branded pages | FC | RF-10 | Y (partner not a regulated professional) |
| RS-LD-38 | Group cross-referral (LDC, Finbyx, Udofin, Equator) | Group companies | Arm's-length flat fee per converted B2B account | MARKETPLACE_REFERRAL | OFF | OWN | — | Group relationship disclosed | FC | — | Y (Companies Act s.188; DPDP purpose limitation; Equator neutrality) |
| RS-LD-39 | Consumer Help flat fee (separate brand / entity) | Individuals | Per complaint | ONE_TIME_SERVICE | OFF until memo | CHB | W3 | "No outcome promised"; official-portal payment statement (NN-23) | FC (brand entity) | RF-05 | Y |
| RS-LD-40 | Consumer Help success fee (separate non-advocate entity) | Individuals | % of recovery, capped | ONE_TIME_SERVICE | **OFF** | CHB | — | Upfront cap and basis; no fee on regulator-ordered refunds | FC | — | Y (high risk; never where an advocate acts — CH-31) |
| RS-LD-41 | Implementation, migration and onboarding packages | Business, Ent. | Fixed fee | IMPLEMENTATION / DATA_MIGRATION | ON | DLV | W1 | SOW; acceptance criteria | FC | RF-05 | N |
| RS-LD-42 | Data escrow / scheduled export to client storage | Business, Ent. | Monthly | SUBSCRIPTION | ON | PRD | W2 | Storage target and schedule | FC | RF-01 | N |
| RS-LD-43 | Certified copy / court document retrieval | Litigants | Per order + court fee | PROFESSIONAL_SERVICES + PASS_THROUGH | OFF | DLV | — | Court fee at actuals | FC + PA | RF-08 | Y (court rules; advocate-only where required) |
| RS-LD-44 | Notarisation / registration appointment facilitation | Individuals | Per instrument | PASS_THROUGH | OFF | DLV | — | Notary/registration fees at actuals; facilitation fee separate | FC + PA | RF-08 | Y (Notaries Act 1952) |
| RS-LD-45 | Aggregated anonymised legal-market reports | Media, policy | Per report | ONE_TIME_SERVICE | OFF | OWN | — | Method; k-anonymity ≥ 10; no matter-level data | FC | — | Y (DPDP; confidentiality) |

### L.9.1 Deny list (no write path; CI-tested)

RS-LD-27, RS-LD-28, RS-LD-29, plus: **LD-X01** per-minute pricing set by ranked named advocates; **LD-X02** sale of user, matter or document data to lenders, insurers or marketers; **LD-X03** pre-ticked bundles or auto-renewing hidden subscriptions in checkout (the bundled-attorney-plan pattern noted in R6 B-05); **LD-X04** credit-bureau report marketing; **LD-X05** [REC] rupee-denominated stored-value wallet or any balance usable for third-party payments; **LD-X06** [REC] lead fees from lenders or insurers for routing consumer complaints (R6 C-6); **LD-X07** success fee where an advocate acts (BCI r.20 — R6 C-4). Inherits the OH8.2 hard-coded deny list.

## L.10 Segment-wise revenue models

| Segment | Entry (free / low-friction) | Core recurring | Transactional | Services / retainers | Expansion path | Indicative ARPA / year (seed) | Risks and guard-rails |
|---|---|---|---|---|---|---|---|
| Individuals | Free vault; free template drafts; stamp-duty and limitation calculators; challan status | Personal ₹1,499 | eSign ₹29; eStamp ₹49 + duty; AI packs | Review ₹499+; consult ₹299+; notice ₹1,499+ | Free → paid eSign (target ≥ 15% — R4 §11.10) → Personal | ₹300–₹2,500 | Distress intents excluded from retargeting (R4-MKT-10); AI drafts labelled (NN-14) |
| Families | Nominee access on Free | Personal + family extension ₹999 | Property and succession documents (wet-ink packs for wills — NN-07) | Property document review; registration appointment (OFF until RS-LD-44) | Personal → family pack → property bundle | ₹1,500–₹6,000 | Children's data only with guardian consent (NN-26) |
| Freelancers / sole proprietors | Free + invoice-agreement templates | Personal or Pro | eSign packs; GST registration | Consult slots; GST returns | Pro on first employee | ₹2,000–₹15,000 | Clear workspace choice (Personal vs Company) |
| Startups | Legal Health Check; founder kit; TM knock-out search (R4 §11.2) | Pro ₹9,999 | TM filing; incorporation; data room | Startup bundles; Startup Legal Officer retainer | Pro → Business at Series A; retainer | ₹25,000–₹3,00,000 | Bundles without hidden auto-renewal (LD-X03) |
| MSMEs | Free Company workspace via service purchase | Pro or Business | Bulk eSign; notices | SME Legal Desk; policy packs; annual ROC | Business + litigation pack | ₹15,000–₹6,00,000 | Purchase approvals; landed prices |
| Mid-market | Demo; pilot | Business + add-ons (CLM, litigation, governance, HRMS-lite) | API overage | Managed Legal Department (when ON); implementation | Enterprise band | ₹1,00,000–₹40,00,000 | MLD supplied by advocates' firm only (OI-P16-01) |
| NBFCs / regulated entities | Compliance gap snapshot → LawDocsComply referral (no tying) | Business; Enterprise for large NBFCs | Embedded eSign/eStamp for loan documents (RS-LD-17) | NBFC Legal & Compliance Retainer | LDC for GRC; LawDocs for legal ops | ₹2,00,000–₹50,00,000 | No core management functions outsourced; RE addendum; ASP never sublet (NN-06) |
| Professionals (advocates, CAs, CSs) | Free tools; templates | Pro; white-label practice workspace | eSign/eStamp for clients | — (they may deliver panel work; never pay for listing) | Practice workspace for client tenants | ₹10,000–₹1,50,000 | NN-21: no listing/lead/commission/badge fees; plan never affects assignment |
| Enterprises / group companies | Pilot | Enterprise licence; dedicated environment rental | API, embedded, PAYG | Implementation, migration, managed services | Multi-entity bands; data escrow | ₹3,00,000–₹1,00,00,000 | Contracted SLAs; residency attestations; maker-checker on overrides |

## L.11 Unit-economics guard-rails (pricing committee; private)

| Metric | Guard-rail | Source |
|---|---|---|
| Subscription gross margin | ≥ 75% after hosting, AI inference, ESP/stamp allowances, support | R6 §R6.7 |
| Included eSign allowance cost | ≤ 15% of plan price (Personal: 24 × ₹12 wholesale = ₹288 ≈ 19% — renegotiate to ≤ ₹9 or cut allowance to 18) | R6 §R6.7 |
| AI credit cost | ≤ 40% of credit price at blended model mix; Free-plan AI cost ≤ ₹10 per active user per month [REC] | R6 §R6.7; LDC N.13 |
| Pass-through margin | Disclosed; ≤ 20% over cost | R6 §R6.7 |
| Buyer platform fee | Covers PG fee (2.36% all-in, B-30) + Route transfer fee [VERIFY] + support; never hidden | R6 §R6.7 |
| M1 service contribution margin | ≥ 35% after professional time at loaded cost [REC] | — |
| Retainer utilisation | 70–85% of hour bank; retainer gross margin ≥ 45% [REC] | R6 §R6.7 |
| CAC payback | ≤ 6 months Personal; ≤ 12 months Pro/Business (R4 target ≤ 4 months SME) | R6 §R6.7; R4 §11.10 |
| Refund rate | ≤ 3% of service orders; consult no-show refunds ≤ 1% [REC] | — |
| Dispute rate | ≤ 1% of engagements [REC] | — |
| Support cost | ≤ ₹100 per Personal subscriber per year [REC] | — |

## L.12 Savings model (P17 §4R; NN-36)

### L.12.1 Evidence classes

| Class | Definition | Display | May feed "Return on spend"? |
|---|---|---|---|
| MEASURED | Facts recorded by LawDocs (counts, timestamps, amounts paid from OH8 documents) or entered by the user with evidence | Solid tile | Yes — Measured return |
| ESTIMATED | Uses default baselines or market benchmarks not measured for this user | Dotted tile, "estimate" chip, hideable | Only the separately labelled Estimated return (people-cost); never market-benchmark savings |
| MODELLED | Computed from a published rule with recorded inputs and stated assumptions (exposure) | Solid tile with "Modelled" chip and assumptions | Never |

### L.12.2 Formulas (decimal arithmetic; snapshot stores inputs, methodology version and hash)

```
HoursSaved(p)        = Σ_a max(0, B_a − M_a) × N_a ÷ 60
   a = activity code (L.12.3); B_a = baseline minutes (methodology v, or user override with history)
   M_a = median measured minutes in period p (workflow first-open → completion, excluding waiting-on-others)
   N_a = completed count in p (MEASURED)
   If M_a is unavailable (no timestamps) → M_a = LawDocs median for a across all workspaces (labelled)

MarketValueOfUsage(p) = Σ_i Q_i × BM_i            (ESTIMATED; BM from L.12.4; only benchmarks verified ≤ 180 days)
PaidForUsage(p)       = Σ_i (direct price paid for i) + PlanCost(p) × w_i          (MEASURED inputs)
   w_i = (Q_i^incl × BM_i) ÷ Σ_j (Q_j^incl × BM_j)  — share of plan cost allocated to included usage of i
MoneySavedVsMarket(p) = MarketValueOfUsage(p) − PaidForUsage(p)    (ESTIMATED; may be negative — shown)
   Excludes stamp duty, government, court and registry fees on both sides.

Spend(p)              = Σ subscription + add-ons + credits + services invoiced in p     (MEASURED)
PeopleCostSaved(p)    = Σ_band HoursSaved_band × HourlyCost_band     (ESTIMATED; hidden until bands entered)
OutsideSpendAvoided(p)= Σ user-entered replaced costs × months in p  (MEASURED if evidence attached)
DeadlinesMet(p)       = count of obligations/hearings/limitation/renewal/filing dates completed before due   (MEASURED)
ExposureAvoided(p)    = Σ_o [completed_before_due_o] × Penalty(rule_o, d)                   (MODELLED)
   shown as a range for d ∈ {1 day, 30 days} unless the user entered a historical late rate L_f for family f,
   then expected value = L_f × Penalty(rule_o, d_median_hist); rules with last_verified_at > 180 days excluded.
MeasuredReturn(p)     = OutsideSpendAvoided ÷ Spend(p)                          (MEASURED; evidenced inputs only)
EstimatedReturn(p)    = (PeopleCostSaved + OutsideSpendAvoided) ÷ Spend(p)      (ESTIMATED; labelled; hideable)
   Neither return ever includes ExposureAvoided (MODELLED) or MoneySavedVsMarket (ESTIMATED benchmarks).
```

### L.12.3 Activity baselines (seed minutes per instance; `[OWNER TO SET]` after the time-and-motion study OI-P17-07)

| Code | Activity | Seed B (min) | Measured from |
|---|---|---|---|
| ACT-LD-01 | Draft a standard agreement (rent, NDA, employment) from scratch | 120 | Draft created → finalised |
| ACT-LD-02 | Find and adapt a template found online | 60 | Same |
| ACT-LD-03 | Arrange physical stamp paper (travel and queue) | 120 | Stamp requested → certificate linked |
| ACT-LD-04 | Collect wet-ink signatures from two parties in one city | 180 | Signing request → completed |
| ACT-LD-05 | Collect signatures from parties in different cities (courier) | 4,320 (3 days elapsed; 90 min effort) | Same (effort minutes used for hours; elapsed shown separately) |
| ACT-LD-06 | One negotiation round by e-mail with tracked changes and consolidation | 90 | Round opened → round closed |
| ACT-LD-07 | Retrieve a stored document when needed | 15 | Search → open |
| ACT-LD-08 | Check one case's status manually on a court portal | 15 | Automated refresh (per refresh) |
| ACT-LD-09 | Maintain a hearing calendar entry and reminder | 10 | Automated |
| ACT-LD-10 | Check a trademark's status manually | 15 | Automated refresh |
| ACT-LD-11 | Type a handwritten or WhatsApp-screenshot page | 20 | Upload → approved typed copy |
| ACT-LD-12 | Translate a one-page vernacular document | 30 | Upload → approved translation |
| ACT-LD-13 | Prepare a section 63(4) certificate draft and hash record | 60 | Evidence pack generated |
| ACT-LD-14 | Draft a legal notice first version | 90 | Studio draft → approved |
| ACT-LD-15 | Draft a reply to a legal notice | 120 | Same |
| ACT-LD-16 | Prepare a contract review summary (≤ 15 pages) | 120 | Review opened → summary approved |
| ACT-LD-17 | Extract obligations and key dates from a contract | 45 | Extraction → confirmed |
| ACT-LD-18 | Set up a renewal reminder and chase | 20 | Automated |
| ACT-LD-19 | Route an internal legal request and approval by e-mail | 40 | Intake → decision |
| ACT-LD-20 | Prepare a board-meeting notice and agenda | 120 | Meeting created → notice issued |
| ACT-LD-21 | Draft minutes of a board meeting | 240 | Meeting held → minutes approved |
| ACT-LD-22 | Update a statutory register entry | 15 | Event → register updated |
| ACT-LD-23 | Compile a litigation MIS for management | 240 | Generated |
| ACT-LD-24 | Bulk-generate 50 agreements from a sheet | 1,500 | Batch generated |
| ACT-LD-25 | Assemble an export of all records for a departing client/auditor | 480 | Export completed |
| ACT-LD-26 | Prepare a stamp-duty computation for an instrument | 20 | Calculator |
| ACT-LD-27 | Prepare a TM objection-reply first draft | 180 | Draft → approved |
| ACT-LD-28 | Prepare a consumer complaint to a regulated entity with annexures | 90 | Draft → filed by user |

### L.12.4 Benchmark price table (market reference; ESTIMATED tiles only)

Rule: BM = median of the published retail prices listed, verified on the date shown; recheck every 180 days (`sav.benchmark.max_age_days`); competitor names are not shown to users — the tile says "median of n published prices, checked DD-MM-YYYY" (NN-20).

| Code | Item | Published prices (R6 / R1 IDs) | BM (₹) | Verified |
|---|---|---|---|---|
| BM-01 | Aadhaar eSign per signatory | ₹25 (B-16), ₹15 (B-25) | 20 | 25-10-2026 |
| BM-02 | Electronic (non-Aadhaar) signature | ₹15 (B-17) | 15 | 25-10-2026 |
| BM-03 | eStamp facilitation per stamp (excl. duty) | ₹45 (B-18), ₹48 (Zoho, R1 §1) | 46.5 | 25-10-2026 |
| BM-04 | 15-minute legal consultation | ₹399 (LawRato, R1 §4.1), ₹465 (LegalKart lowest named rate × 15, B-01) | 432 | 25-10-2026 |
| BM-05 | Expert document review per page | ₹100 (LegalKart, R1 IMP-030) | 100 | 25-10-2026 |
| BM-06 | Private limited incorporation (professional fee) | ₹2,899 (B-06), ₹2,999 (B-10) | 2,949 | 25-10-2026 |
| BM-07 | Partnership firm registration | ₹2,899 (B-09) | 2,899 | 25-10-2026 |
| BM-08 | Trademark filing professional fee (per class) | ₹1,499 (B-11), ₹1,899, ₹1,999 (R1 §4.1) | 1,899 | 25-10-2026 |
| BM-09 | GST registration | ₹1,499 (B-08) | 1,499 | 25-10-2026 |
| BM-10 | GST monthly return | ₹998 (B-08), ₹799 (LegalWiz, R1 §4.1) | 898.5 | 25-10-2026 |
| BM-11 | CA-assisted ITR (salaried) | ₹999 (JioFinance), ₹1,274 (Tax2Win), ₹2,999 (TaxBuddy) (B-14, dated Aug 2025) | 1,274 | [VERIFY] dated source |
| BM-12 | Annual ROC compliance bundle (small company) | ₹19,899 incl. accounting (B-07) | 19,899 | 25-10-2026 (bundle not like-for-like — show note) |
| BM-13 | Litigation software per user per month | ₹500 (B-27) | 500 | 19-10-2026 |
| BM-14 | Handwritten/screenshot typing per page | — (no published benchmark) | not used | — |
| BM-15 | Translation per page (non-certified) | — | not used | [VERIFY] |
| BM-16 | Legal notice drafting | — | not used | [VERIFY] |

Items without a verified benchmark contribute only to Hours saved, never to Money saved.

### L.12.5 Exposure bindings (each lives in the `rul` register with citation and `last_verified_at`; all [VERIFY] before MODELLED tiles switch on — NN-38)

| Code | Obligation family | Consequence of lateness | Penalty function | Source |
|---|---|---|---|---|
| PX-01 | MCA e-forms (AOC-4, MGT-7/7A, ADT-1, DIR-12 etc.) | Additional fee | ₹100 × days late per form | Companies Act 2013 s.403; Companies (Registration Offices and Fees) Rules 2014 [VERIFY] |
| PX-02 | DIR-3 KYC | Late fee | ₹5,000 flat | Companies (Appointment and Qualification of Directors) Rules 2014 r.12A [VERIFY] |
| PX-03 | GSTR-1 / GSTR-3B | Late fee | ₹50/day (₹20 nil return), capped by turnover band | CGST Act s.47; Notifications 19/2021-CT, 20/2021-CT [VERIFY] |
| PX-04 | GST payment | Interest | 18% p.a. on tax due | CGST Act s.50(1) [VERIFY] |
| PX-05 | TDS statement (quarterly) | Late fee per day | Per Income-tax Act 2025 successor of s.234E | [VERIFY section and amount] |
| PX-06 | Trademark renewal | Surcharge for renewal after expiry; removal risk | Fee difference (renewal with surcharge − on-time renewal) per class | Trade Marks Act 1999 s.25; Trade Marks Rules 2017 First Schedule [VERIFY] |
| PX-07 | Lease > 1 year presented for registration | Late-presentation fine | Up to the multiple of registration fee allowed for delay | Registration Act 1908 ss.17, 23, 25 [VERIFY; State variations] |
| PX-08 | Cheque-bounce demand notice | Right to prosecute lost | Non-monetary — count only | NI Act 1881 s.138 proviso (b) (30 days) [VERIFY] |
| PX-09 | Limitation period for a suit or appeal | Claim time-barred | Non-monetary — count only | Limitation Act 1963 Schedule [VERIFY article per matter] |
| PX-10 | Consumer complaint filing window | Complaint time-barred | Non-monetary — count only | Consumer Protection Act 2019 s.69 [VERIFY] |
| PX-11 | TM examination report / opposition response | Application abandoned | Non-monetary — count only | Trade Marks Rules 2017 [VERIFY rule and period] |
| PX-12 | Hearing date attended / document filed by date | Adverse order risk | Non-monetary — count only | — |

### L.12.6 Worked example (Personal, FY view; for testing)

A Personal user (₹1,499/yr) signed 18 documents with Aadhaar eSign (18 of 24 included), bought 1 eStamp facilitation (₹49 + duty), and had 1 professional review (₹499). MarketValueOfUsage = 18 × ₹20 + 1 × ₹46.5 + (review: no benchmark for "review ≤ 5 pages"; BM-05 × 5 pages = ₹500) = ₹906.5. PaidForUsage = ₹1,499 × w (only eSign is included usage → w_eSign = 1) + ₹49 + ₹499 = ₹2,047. MoneySavedVsMarket = −₹1,140.5 → the tile shows "You paid ₹1,140.50 more than the market median for this usage; your plan also includes vault storage, unlimited drafts and reminders, which have no market price in this model." Hours saved: ACT-LD-04 (180 − 12 measured) × 18 ÷ 60 = 50.4 hours (ESTIMATED). This honesty is deliberate (NN-20, NN-36).

### L.12.7 Worked example (Business, quarter view; for testing)

A Business workspace (₹59,999/yr → ₹14,999.75 per quarter) used 120 Aadhaar eSigns (all included), filed 9 MCA forms on time and 2 three days late (late fees ₹600 paid and recorded), tracked 40 matters with 380 automated refreshes, and generated 60 agreements in bulk. The tenant entered hourly cost bands (legal executive ₹600/h) and a prior outside-drafting spend of ₹15,000/month with invoices.

- **Spend (MEASURED)** = ₹14,999.75 + add-ons ₹7,500 (litigation pack) = ₹22,499.75.
- **Hours saved (ESTIMATED)** = eSign collection ACT-LD-04 (180 − 10) × 120 ÷ 60 = 340 h; case checks ACT-LD-08 15 × 380 ÷ 60 = 95 h; bulk generation ACT-LD-24 (1,500 − 30) × 60/50 ÷ 60 = 29.4 h → **464.4 h**.
- **People-cost saved (ESTIMATED)** = 464.4 × ₹600 = ₹2,78,640.
- **Outside spend avoided (MEASURED, evidenced)** = ₹15,000 × 3 = ₹45,000.
- **Deadlines met (MEASURED)** = 9 of 11 MCA forms on time; 2 late with ₹600 recorded.
- **Exposure avoided (MODELLED)** = 9 forms × PX-01 (₹100 × d) → ₹900 (d = 1) to ₹27,000 (d = 30), shown in its own tile, excluded from savings and ROI.
- **Money saved vs market (ESTIMATED)** = 120 × BM-01 ₹20 = ₹2,400 market value vs plan cost allocated to eSign (w = share of included usage value) — shown with its allocation note.
- **Measured return (MEASURED)** = ₹45,000 ÷ ₹22,499.75 = 2.0×.
- **Estimated return (ESTIMATED)** = (₹2,78,640 + ₹45,000) ÷ ₹22,499.75 = 14.4× — dotted tile; it states that hours are estimates against default baselines until the tenant's own time-and-motion figures replace them.

## L.13 Tax notes and refund rules

### L.13.1 GST, TDS and TCS notes [TAX MEMO — CFO and tax adviser sign before go-live]

| # | Topic | Position for the build | Citation / status |
|---|---|---|---|
| TX-01 | LawDocs's own supplies (SaaS, credits, facilitation, platform fee, M1 services) | Forward charge at 18%; SAC per SKU from the tax memo (candidates: 998314/998315/997331 SaaS; 998599 facilitation; 998214 only if LawDocs itself supplies legal documentation) | R6 T-04 [TAX MEMO]; OH8.6 |
| TX-02 | Advocates' legal services to business entities | Recipient pays GST under reverse charge; advocate's bill shows "Tax payable under reverse charge"; LawDocs never adds GST to it | Notification 13/2017-CT(R) Sl. 2; CGST Act s.9(3) (R6 T-01) |
| TX-03 | Advocates' services to individuals and small businesses | Exempt | Notification 12/2017-CT(R) [VERIFY entry number and threshold wording] (R6 T-02) |
| TX-04 | Stamp duty, government, court and registry fees | Pure-agent reimbursement shown as separate non-taxable lines; facilitation fee taxable | CGST Rules r.33 [TAX MEMO] (R6 T-08) |
| TX-05 | E-commerce operator TCS | 0.5% on net value of taxable supplies made through LawDocs by other suppliers where LawDocs collects consideration (M2); exclude RCM and exempt supplies [TAX MEMO]; GSTR-8 via OH8; mandatory ECO registration | CGST Act s.52; Notification 15/2024-CT (R6 T-05) |
| TX-06 | Income-tax TDS by ECO | 0.1% of gross amount of services facilitated (M2 payouts); threshold exemption for resident individuals/HUF ≤ ₹5 lakh with PAN/Aadhaar | Income-tax Act 2025 s.393(1) Table Sl. 8(v) [VERIFY] (R6 T-07) |
| TX-07 | TDS by business buyers on LawDocs fees | 2% (technical) or 10% (professional/royalty) depending on characterisation; ₹50,000 threshold; publish LawDocs's position in Settings → Tax documents | s.393(1) Table Sl. 6(iii).D(a)/(b) [VERIFY] (R6 T-06) |
| TX-08 | Credit packs | Whether a credit pack is a voucher (CGST Act s.2(118)) and its time of supply and breakage treatment | [TAX MEMO]; [VERIFY current voucher provisions and CBIC clarifications] |
| TX-09 | E-invoicing | Applies per selling entity once AATO exceeds ₹5 crore | Notification 10/2023-CT; OH8.6 [VERIFY AATO] |
| TX-10 | Place of supply | Registered recipient's location; otherwise address on record; intra-State CGST + SGST, inter-State IGST | IGST Act s.12(2) |
| TX-11 | SEZ / IFSC units, exports | Zero-rated with LUT reference captured | IGST Act ss.13, 16 [VERIFY IFSC treatment] |
| TX-12 | Credit notes | For proration, service credits, refunds and disputes, referencing the original invoice, within the s.34 time limit | CGST Act s.34 |
| TX-13 | Invoice record retention | ≥ 72 months from annual-return due date | CGST Act s.36 [VERIFY] |
| TX-14 | Revenue recognition | Ind AS 115 or AS 9 per selling entity (owner decision) — subscriptions over time; credits on redemption/expiry; services on acceptance | OH8.8 |

### L.13.2 Refund and cancellation rules (codes used in L.9)

| Code | Applies to | Rule (seed `[OWNER TO SET]`) |
|---|---|---|
| RF-01 | Annual subscriptions and add-ons | Pro-rata refund if cancelled within 30 days of the first term's start; afterwards no refund, access to term end; downgrade at term end |
| RF-02 | Personal first purchase | 14-day cooling-off: full refund less credits consumed valued at the single-pack price |
| RF-03 | Monthly plans | Cancel any time, effective end of the paid month; no partial-month refunds |
| RF-04 | Credit packs | Pro-rata refund of unused purchased credits within 30 days of purchase and on account closure; failed service returns credit automatically; promotional credits not refundable |
| RF-05 | Fixed-price services and bundles | Before work: full refund (incl. platform fee); after scoping, before work: refund less disclosed scoping fee; after inputs: delivered milestones payable, undelivered refunded (Appendix M §M.10) |
| RF-06 | Consult slots | Professional no-show: automatic full refund; buyer cancels ≥ 4 hours before: full refund; < 4 hours: 50% refund; one free reschedule |
| RF-07 | Retainers | Notice period per package; prepaid months beyond notice refunded; hour-bank balance not refundable unless LawDocs terminates |
| RF-08 | Pass-through (stamp duty, court, government fees) | Refundable only if not yet paid to the authority or vendor; once paid, refund only as the authority's rules allow [VERIFY State e-stamp refund rules] |
| RF-09 | Academy courses | As published by FinLegal Academy; R5 found "non-refundable" — review under the Consumer Protection Act 2019 [COUNSEL] |
| RF-10 | Enterprise and contract streams | Per contract |

All refunds go to the original payment method with a credit note; no refund creates a stored balance (LD-X05).

## L.14 Pricing-page FAQs (seed; 30; visible HTML)

| Code | Question | Answer (seed) |
|---|---|---|
| FAQ-01 | Is LawDocs really free to start? | Yes. The Free plan keeps your documents within its 1 GB storage limit [OWNER], lets you draft from vetted templates and sign with OTP up to 5 times a month. You pay only for things that cost us money, such as Aadhaar eSign. |
| FAQ-02 | Do I need a plan to hire a professional? | No. You can buy any service on the marketplace with a Free account. Plans add allowances and member prices. |
| FAQ-03 | What does "incl. GST" mean on the cards? | We show our price before GST and the total you will pay with 18% GST. Your invoice confirms the exact tax. |
| FAQ-04 | Why is monthly more expensive? | Monthly billing costs about 20% more than paying yearly. The card shows how much you save on annual billing. |
| FAQ-05 | Will my trial turn into a paid plan automatically? | No. Trials need no card and never convert on their own. When the trial ends you go back to Free and keep everything. |
| FAQ-06 | What happens to my documents if I stop paying? | Nothing is deleted. You can always read, download and export everything. Only new paid features stop. |
| FAQ-07 | How do I cancel? | Settings → Billing → Cancel or change plan. It takes no more steps than buying. |
| FAQ-08 | Can I get a refund? | Annual plans: pro-rata within 30 days of first purchase. Personal: 14-day cooling-off on first purchase. Credits: unused purchased credits within 30 days. See the refund policy. |
| FAQ-09 | What is an eSign credit? | One credit is one successful Aadhaar eSign by one signer. If the eSign fails, the credit comes back. |
| FAQ-10 | Is my money stored in a wallet? | No. We do not keep a money balance. Credits are units of specific LawDocs services. |
| FAQ-11 | Do credits expire? | Plan credits renew every period. Purchased credits last 12 months; we remind you before expiry and extend once on request. |
| FAQ-12 | Is stamp duty included? | No. Stamp duty is paid at actuals to the State through an authorised channel and shown separately. Our facilitation fee is shown on its own line. |
| FAQ-13 | Which documents cannot be eSigned? | Wills, trusts, ordinary powers of attorney and most negotiable instruments. LawDocs prepares a wet-ink, notary or registration pack for these. |
| FAQ-14 | Is Aadhaar eSign legally valid? | Electronic signatures through licensed eSign providers are recognised under the IT Act 2000 for documents not excluded by its First Schedule. Some documents also need stamping or registration. |
| FAQ-15 | Can my family share my Personal plan? | Yes, up to 5 people in all. Each person's vault is private unless they share. |
| FAQ-16 | How many people can use Pro or Business? | Pro includes 3 working seats; Business includes 10 plus unlimited free viewer, approver, board and auditor seats. |
| FAQ-17 | Does Vidhi give legal advice? | No. Vidhi helps you draft and find information, shows sources, and labels AI drafts. For advice, book a professional. |
| FAQ-18 | Who are the professionals? | LawDocs's own team for documentation and compliance work, and advocates enrolled with a State Bar Council and other professionals for work only they may do. We check enrolment and membership records before anyone works on your matter. |
| FAQ-19 | Can I choose my advocate? | We assign a verified professional by practice area, language and availability. You may ask for a different one once before work starts. |
| FAQ-20 | Why is there a separate platform fee? | When a regulated professional does your work, their fee goes to them in full. Our platform fee pays for verification, secure workspace, payments and support. |
| FAQ-21 | Do you show lawyer ratings? | No. Advocates may not advertise, so we do not rate or rank them. You can review LawDocs's service. |
| FAQ-22 | Is court-case tracking real-time? | No. We refresh case data through licensed providers and show when it was last updated. |
| FAQ-23 | Will I get a GST invoice? | Yes. Every payment produces a GST tax invoice e-mailed to you and saved in your vault. |
| FAQ-24 | Can my company deduct TDS? | Yes. Upload your TDS certificate in Settings → Billing → Tax documents. |
| FAQ-25 | Can I pay by UPI AutoPay or bank transfer? | Yes. UPI, cards, netbanking, UPI AutoPay and e-mandates; Business and Enterprise can also pay by bank transfer. |
| FAQ-26 | Do you store my card details? | No. Payments run on Razorpay's hosted pages. LawDocs never sees or stores card data. |
| FAQ-27 | Where is my data stored? | In India. You can export everything any time in folders you can open without LawDocs. |
| FAQ-28 | What does Enterprise add? | Higher volumes, SSO, APIs, BYO storage, dedicated environment options, contracted SLAs and a named success manager. |
| FAQ-29 | Is LawDocs a law firm? | No. LawDocs is a legal-technology and services platform. Legal advice and representation come from advocates in their own name. |
| FAQ-30 | Can I see how much I have saved? | Yes. Settings → Savings & Value shows hours saved, money saved against published market prices and deadlines met, with the formula behind every figure. |

## L.15 Benefits explained (seed copy for cards, configurator and Settings)

| Plan | "What you get over Free" | "What this replaces" | "Not for you if" |
|---|---|---|---|
| Personal | 24 Aadhaar eSigns a year, 10 GB vault, 300 Vidhi credits a month, negotiation with the other party, DigiLocker document pull, 5 family members, one 15-minute documentation-team session a year | Printing, couriering and meeting to sign; buying eSigns one by one (published retail ₹15–₹25 each — BM-01, checked 25-10-2026) | You sign fewer than 3 documents a year — use Free and pay per eSign |
| Pro | 3 seats, 10 eSigns a month, clause library, approvals, 50 tracked matters, 10 marks with journal watch, startup kit, GST/TDS calendars, 2 documentation-team sessions a year (advocate consultations billed separately by the advocate) | Separate eSign, case-tracking and template tools; ad-hoc drafting fees for routine NDAs | You are an individual without a business — choose Personal |
| Business | 10 seats + free approver/board seats, 50 eSigns a month, full CLM, 300 matters, litigation MIS, governance for 3 entities, 6 documentation-team sessions a year (advocate consultations billed separately by the advocate), 10% off services, onboarding manager | A legal-ops stack of CLM, litigation and governance tools plus courier and stamp runs | You are a regulated entity that needs a full GRC suite — see LawDocsComply alongside |
| Subscription vs one-time | "Buy one service any time without a plan. A plan is worth it if you sign or draft more than a few documents a year or want reminders and tracking working for you." | — | — |

## L.16 Billing notification templates (codes)

`NT-BIL-01` trial started · `-02` trial T-3 · `-03` trial T-1 · `-04` trial ended (back to Free) · `-05` quote ready · `-06` payment received · `-07` payment failed with retry · `-08` invoice issued · `-09` mandate pre-debit courtesy (T-48 h) · `-10` usage 80% · `-11` usage 100% · `-12` credits low · `-13` credits expiring T-30 · `-14` credits expiring T-7 · `-15` renewal T-30 · `-16` renewal T-7 · `-17` monthly renewal T-3 · `-18` price-change notice (≥ 30 days) · `-19` plan changed · `-20` add-on added/removed · `-21` restriction notice (7 days' notice) · `-22` termination notice · `-23` reverted to Free · `-24` LawDocs override applied · `-25` savings/value report ready · `-26` refund processed with credit note · `-27` purchase approval requested · `-28` TDS certificate received. Mandatory (cannot be muted): 06, 07, 08, 09, 15–18, 21, 22, 26. All templates DLT-registered where sent by SMS (NN-34).

## L.17 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-L-01 | Approve price points, monthly rounding, GST-inclusive display for B2C | Owner | Seeds |
| OI-L-02 | Court-data refresh allowances per plan (F-072) and provider cost | Owner + integration lead | Manual refresh only |
| OI-L-03 | Benchmarks BM-11, BM-15, BM-16 re-verification; benchmark refresh owner | Product analyst | Excluded from Money saved |
| OI-L-04 | PX-01…PX-12 legal verification (sections, amounts, periods) | `PLT_LEGAL_REVIEWER` | MODELLED tiles OFF; counts only |
| OI-L-05 | Tax memo TX-01…TX-14 | CFO + tax adviser | Tax hints labelled "confirmed on invoice" |
| OI-L-06 | New OH8 stream types (CREDIT_PACK, MARKETPLACE_PLATFORM_FEE, RETAINER, REFERRAL_CREDIT, AFFILIATE, PARTNER_RESALE) — Appendix X | OH lead | Nearest existing type |
| OI-L-07 | Refund windows RF-01…RF-09 and Academy refund policy | Owner + [COUNSEL] | Seeds |

