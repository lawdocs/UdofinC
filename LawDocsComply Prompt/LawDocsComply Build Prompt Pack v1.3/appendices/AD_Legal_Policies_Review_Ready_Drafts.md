# Appendix AD — Legal Policies: Review-Ready Drafts for LawDocsComply (IPB-05 instances)

> LawDocsComply Build Prompt Pack v1.3 · 26 October 2026 · Owner: Company Secretary, Infrabyx Group · Status: **DRAFT FOR COUNSEL REVIEW** (owner decision #28; D-71) · Binding on: P23 §4W FR-P23-226 (policy pages), P20 (checkout links), P01 (sign-up consent controls), P24 §4M (Vendor Assurance Statement), P07 (internal policy hosting) · Source templates: `docs/ipb/IPB-05_Legal_Policy_Templates.md` (Templates 1–13, 15–18; Template 14 not adopted — D-71).
>
> **How to read this appendix.** Each section below is the LawDocsComply **instance** of an IPB-05 template: the LDC parameter values, the product inserts written into the body, the clauses counsel must settle (**[COUNSEL]**), facts to confirm before publication (**[VERIFY]**), and commercial positions for the owner (**[OWNER]**). The text is plain English, second person, numbered clauses, Indian spelling. Nothing here is published until the P23 publish pipeline records `plt_legal_reviewer` (maker), `plt_super_admin` (checker) and, for privacy-class documents (Templates 1, 5, 9, 15, 18), `plt_dpo` approval, and the lint passes (unresolved parameters, banned words, stale citations against Appendix G, mandatory sections — `IPB-POL-001…007`, surfaced as `LDC-WEB-060`). Parameters still shown as `{{…}}` are filled from the brand pack's legal-entity record (owner decision #10/#28); no particular has been invented.
>
> **Drafting rules applied (IPB-05 §05.1, §05.4.19).** One obligation per sentence; defined terms in Title Case; statutory references name the instrument and provision; alternatives shown as `[Option A | Option B]`; banned words avoided ("guarantee", "assured", "risk-free", "fully compliant", "100% secure", "RBI-approved", "ISO certified" unless held — NN-19); English prevails over the Hindi summary **[COUNSEL]**; version `1.0` with `effective_at` to be set at publication; review cadence 6 months for Templates 1, 5, 6, 9 and 12 months for the rest.

---

## AD.0 LDC parameter block (values and sources)

| Parameter | LDC value | Source / status |
|---|---|---|
| `{{entity_name}}`, `{{entity_type}}`, `{{cin}}`, `{{gstin}}`, `{{registered_office}}` | `{{…}}` — operating entity of LawDocsComply | Brand pack legal-entity record; owner decision #10/#28 **[OWNER]** |
| `{{entity_short}}` | LawDocsComply | — |
| `{{selling_entity_name}}`, `{{selling_entity_cin}}`, `{{selling_entity_gstin}}`, `{{selling_entity_address}}`, `{{selling_entity_short}}` | `{{…}}` — merchant of record (D-27) | OH8; owner decision #3 **[OWNER]** |
| `{{product_name}}` | LawDocsComply (white-label packs: `brand.app_name`) | `brand_pack` |
| `{{product_code}}` | LDC | — |
| `{{domain}}` | lawdocscomply.com | — |
| `{{app_url}}` | https://app.lawdocscomply.com | — |
| `{{support_email}}`, `{{support_phone}}`, `{{support_hours}}` | support@lawdocscomply.com **[VERIFY mailbox]**; `{{phone}}`; Monday–Friday 09:30–18:30 IST excluding national holidays **[OWNER]** | Footer |
| `{{dpo_name}}`, `{{dpo_email}}`, `{{dpo_address}}` | `{{…}}`; privacy@lawdocscomply.com **[VERIFY mailbox]** | Policy set; board/management appointment **[OWNER]** |
| `{{grievance_officer}}`, `{{grievance_email}}`, `{{grievance_phone}}`, `{{grievance_address}}` | `{{…}}`; grievance@lawdocscomply.com **[VERIFY mailbox]** | Appointed under IT Rules 2021 r.3(2) and DPDP Act s.13; named consistently across footer, `/grievance` and this appendix |
| `{{escalation_officer}}` | `{{…}}` — Head of Compliance or Company Secretary | **[OWNER]** |
| `{{nodal_officer}}` | not applicable (LDC is not a regulated lender or LSP) | Template 7 switch OFF |
| `{{security_email}}` | security@lawdocscomply.com **[VERIFY mailbox]** | Template 11; `security.txt` |
| `{{a11y_email}}` | accessibility@lawdocscomply.com **[VERIFY mailbox]** | Template 10 |
| `{{refund_rule}}`, `{{refund_window_days}}` | `full_within_window`; 7 days (self-serve plans) | Appendix N; `pol.refund.*` **[OWNER]** |
| `{{refund_timeline_days_min}}` / `{{refund_timeline_days_max}}` | 5 / 7 working days | `pol.refund.timeline_days_*` |
| `{{trial_days}}`, `{{trial_auto_convert}}` | 14 **[OWNER]**; `false` (D-26: trials never auto-convert) | Appendix N |
| `{{renewal_notice_days}}` | 7 | `pol.billing.renewal_notice_days` |
| `{{billing_cycles}}` | monthly and annual (enterprise: per order form) | Appendix N |
| `{{currency_list}}` | INR; USD for customers outside India (other currencies per cell, P25) | Appendix N §N.16 |
| `{{gateway_names}}` | Razorpay (reference; RBI-authorised payment aggregator) through the Operations Hub billing engine; Stripe for international payments **[VERIFY live adapters at go-live]** | X-02 |
| `{{emandate_enabled}}` | true for card and UPI recurring payments where offered **[OWNER]** | OH8 |
| `{{credits_expiry_months}}` | 12 (AI credits and prepaid usage) **[OWNER]** | Appendix N |
| `{{dunning_days}}`, `{{grace_days}}` | 3, 7, 14; 14 | OH8 configuration |
| `{{governing_law_city}}`, `{{arbitration_seat}}` | New Delhi **[COUNSEL]** | Policy set |
| `{{odr_provider_name}}`, `{{odr_rules_url}}` | Equator Resolution (a group company — disclosed); https://equator.example/rules **[VERIFY URL]** | **[COUNSEL]** on group-company disclosure and consumer enforceability |
| `{{min_age}}` | 18 | — |
| `{{liability_cap}}` | fees paid by you for the service in the 12 months before the event giving rise to the claim | `pol.liability_cap_formula` **[OWNER]** |
| `{{retention_schedule_url}}` | https://lawdocscomply.com/legal/retention-schedule | Template 9 instance |
| `{{sub_processor_list_url}}` | https://lawdocscomply.com/trust#sub-processors | Trust Centre (from the Vendor Assurance Room mirror) |
| `{{status_page_url}}` | https://status.lawdocscomply.com **[VERIFY]** | brand pack |
| `{{ai_display_name}}` | Vidhi (white-label: `brand.terminology.vidhi`) | IPB-D-03 |
| `{{llm_providers}}` | Anthropic Claude via Amazon Bedrock (India); Anthropic API (public content only); further providers listed in the Trust Centre as and when enabled (Azure OpenAI Central India, Google Vertex AI asia-south1, Sarvam, Bhashini, self-hosted models) | P17 §4Y; model registry |
| `{{human_review_list}}` | regulatory filings and returns; board and committee minutes and resolutions; compliance certificates and attestations; policy documents adopted by a board; notices or submissions to a regulator, auditor or counter-party; any change to a compliance status | P17 FR-P17-73 |
| `{{regulator_refs}}` | Consumer Commission under the Consumer Protection Act 2019; Data Protection Board of India | IPB-05 Template 7 LDC insert |
| `{{consent_manager_name}}` | none at present (DPDP Consent Manager integration planned after 13 November 2026 — `fut.dpdp-consent-manager-api`) **[VERIFY]** | P12 |
| `{{transfer_countries}}` | none for regulated and confidential data; for public or non-personal content processed by global AI endpoints: United States **[VERIFY processor list]** | Trust Centre |
| `{{analytics_adapter_names}}` | first-party analytics hosted in India (Plausible-compatible or Matomo) **[VERIFY vendor]** | P23 FR-P23-171 |
| `{{certifications_held}}` | none at the date of this draft; the Trust Centre lists certifications when certificates exist (NN-19) | Vendor Assurance Room |
| `{{pgp_key_url}}` | https://lawdocscomply.com/.well-known/pgp-key.txt **[VERIFY]** | Template 11 |
| `{{bounty}}` | `none` — "We do not run a paid bounty programme at present; we acknowledge researchers publicly with their consent." **[OWNER]** | `pol.vdp.bounty` |
| `{{ugc_licence}}`, `{{attribution_rule}}`, `{{moderation_sla_days}}` | non-exclusive, perpetual; "by [author name], [designation], published on LawDocsComply"; 5 | `pol.ugc.*`; `web.blog.user_posts.moderation_sla_days` |
| `{{resource_licence}}` | personal_internal | `pol.resources.default_licence` |
| `{{audit_frequency}}`, `{{exit_assistance_days}}` | once in any 12 months; 90 days | `pol.dpa.*` |
| `{{rpo_hours}}`, `{{rto_hours}}` | 1 / 4 (Enterprise); 4 / 8 (Business) **[VERIFY against P24 DR targets]** | P24 §4F |

**Mandatory set for LDC (IPB-05-01).** Before the public site goes live: Templates 1, 2, 5, 6, 7, 8, 9, 10, 11, 18. Because LDC sells online: 3 and 4. Because business customers are onboarded: 15, 16, 17. Template 12 only when `web.blog.user_posts.enabled = true`; Template 13 when any resource is gated. Template 14 is not adopted (D-71).

**Footer legal column (binding order, P23 FR-P23-12 item 4).** Privacy Notice · Terms of Use · Payment & Subscription Terms · Refund & Cancellation Policy · Cookie Policy · AI Use & Transparency Policy · Grievance Redressal Policy · Acceptable Use Policy · Data Retention & Deletion Schedule · Accessibility Statement · Security & Responsible Disclosure · Blog & UGC Terms (when enabled) · Resources Download Terms · Data Processing Agreement · Service Level Agreement · Vendor Assurance Statement · Sitemap.

---

## AD.1 Privacy Notice — LawDocsComply (Template 1 instance)

**Displayed at:** footer; sign-up (`consent.signup.privacy_notice`); CMP preference centre link; Settings › Privacy & consents; every form with personal fields (deep link to clause 3). **Class:** privacy (DPO approval). **Review cadence:** 6 months.

> # Privacy Notice — LawDocsComply
> Version 1.0 · Effective {{effective_date}} · Last reviewed {{last_reviewed}} · [Prior versions]
>
> **Summary.** {{entity_name}} ("we") operates LawDocsComply at lawdocscomply.com and app.lawdocscomply.com. We process your personal data to provide the service you ask for, to meet legal duties, and — only with your consent — for the other purposes listed below. You can withdraw consent, access and correct your data, ask for erasure, nominate someone to act for you, and complain to us or to the Data Protection Board of India. This notice is available in English and Hindi; the English text prevails **[COUNSEL]**.
>
> **1. Who we are (Data Fiduciary).** {{entity_name}}, {{entity_type}}, CIN {{cin}}, registered office {{registered_office}}. Contact for privacy questions: {{dpo_name}}, {{dpo_email}}, {{dpo_address}} (Digital Personal Data Protection Act 2023 s.8(9)). Grievance Officer: {{grievance_officer}}, {{grievance_email}} (s.13). {{#if white_label}}{{product_name}} is provided to you by {{entity_name}} using technology from Infrabyx Group; Infrabyx entities act as our Data Processors under contract.{{/if}}
>
> **2. What this notice covers.** Visitors to lawdocscomply.com; people who create accounts or take the free Compliance Health Check; people whose data a customer uploads into LawDocsComply (where our customer is the Data Fiduciary and we are its Data Processor — see clause 12); job applicants; people who contact us or attend our webinars.
>
> **3. Personal data we process and why.**
>
> | Purpose | Personal data | Basis | Retention | Who receives it |
> |---|---|---|---|---|
> | Create and secure your account; provide the service | Name, work email, phone, designation, organisation, authentication data (passkeys and MFA metadata), activity logs | Consent (s.6) at sign-up; legitimate use for the service you asked for (s.7(a)) | Account life + 30 days export window (Retention Schedule row 1) | Our hosting and identity processors (Trust Centre list) |
> | Free Compliance Health Check | Entity identifiers you enter (name, type, regulator, CIN/LLPIN where you choose to give it), answers, contact details if you ask for the report | Consent (s.6) | 365 days or earlier on request (`web.hc.retention_days`) | Our hosting processor; our group CRM (Operations Hub) only if you ask to be contacted |
> | Billing and invoicing | Billing name, GSTIN, address, tokenised payment reference (we never hold card numbers) | Contract; legal duty (CGST Act 2017 s.31, s.36) | 8 years from financial year end (Retention Schedule) | Payment gateway (Razorpay or as listed); our selling entity's finance team |
> | Support, grievances and data requests | Your messages, account identifiers, outcome | Legitimate use (s.7(a)); legal duty (s.13) | 3 years after closure | Our support tooling processor |
> | Product updates and marketing | Email, name, organisation, preferences | **Consent only** (separate, unticked control) | Until withdrawal or 24 months of inactivity | Our email processor; our group marketing team |
> | Security, fraud prevention and legal compliance | IP address class, device data, logs | Legal duty (CERT-In Directions 2022; s.7(i)) | 180 days (security logs); 8 years (audit ledger) | None outside our processors unless required by law |
> | Compliance data uploaded by customers (filings, evidence, officer names, DINs, board papers) | As decided by the customer | We act as Data Processor on the customer's instructions (clause 12) | As the customer instructs and the law requires | The customer's administrators; sub-processors listed in the Trust Centre |
> | Job applications | CV, contact details, interview notes | Consent | 12 months if unsuccessful | Our group HR team (Operations Hub) |
>
> Each purpose is itemised; we do not bundle purposes. Consent for one purpose is not a condition for another unless the service cannot be provided without it.
>
> **4. Categories of personal data.** Identity and contact; account and authentication (including passkeys and MFA metadata); billing (tokenised payment reference only); usage and device data; communications; content you upload; **compliance calendars, filings, officer names and DINs, board and committee records, uploaded evidence** (as Processor for our customers). We do not ask for Aadhaar numbers and our systems reject them (NN-12). We do not obtain credit-information reports about you or your organisation (X-07).
>
> **5. How we collect.** Directly from you; automatically through our service (logs, first-party cookies — see the Cookie Policy); from our customers who use LawDocsComply to process your data; from public registers where the law allows (Ministry of Corporate Affairs company master data, GST portal taxpayer search, RBI/SEBI/IRDAI/IFSCA public lists, GLEIF) through licensed providers, only to pre-fill the organisation profile you confirm **[VERIFY provider terms, owner decision #24]**; from identity verification providers you authorise.
>
> **6. Consent and how to withdraw.** Where we rely on consent, it is free, specific, informed, unconditional and unambiguous, given by a clear affirmative action (s.6(1)). You may withdraw at any time at Settings › Privacy & consents, through the Cookie settings link, by email to {{dpo_email}}, or through a registered Consent Manager where we support one ({{consent_manager_name}}). Withdrawal is as easy as giving consent (s.6(4)) and does not affect processing already done lawfully (s.6(5)). After withdrawal we stop the processing and erase the data unless retention is required by law (s.6(6)).
>
> **7. Children.** LawDocsComply is for persons aged 18 and above acting for an organisation. We do not knowingly process data of children or of persons with disabilities who have a lawful guardian without verifiable consent of the parent or guardian (s.9; DPDP Rules 2025 r.10 **[VERIFY]**). We do not track or target advertising at children (s.9(3)). If you believe a child has provided data, contact {{dpo_email}}.
>
> **8. Sharing and processors.** We share personal data with: our Data Processors (hosting in India, identity, email, payment gateway, support tooling, first-party analytics where consented, AI model providers under zero-retention contracts) listed at {{sub_processor_list_url}}; our customers' administrators (for data they control); our group companies in the Infrabyx Group for billing, support and CRM (each bound by an intra-group processing agreement); auditors, regulators and courts where required by law; successors in a merger (with notice). **Regulatory filings data is shared with an authority only on the customer's instruction.** We do not sell personal data.
>
> **9. Retention and erasure.** We keep personal data only as long as the purpose requires or the law demands, then erase it and cause our processors to erase it (s.8(7)). The schedule is at {{retention_schedule_url}}. Where the law sets a minimum (tax records, audit logs, books and records under the Companies Act 2013 s.128 **[VERIFY applicability]**) we state it there. Before erasing data for inactivity we will notify you where the Rules require (DPDP Rules 2025 r.8 and Third Schedule **[VERIFY applicability]**).
>
> **10. Your rights (Data Principal).** Access a summary of your data and processing (s.11); correction, completion, updating and erasure (s.12); grievance redressal (s.13) — see our Grievance Redressal Policy; nominate a person to exercise your rights if you die or are incapacitated (s.14) at Settings › Privacy & consents › Nominee. We respond within the period stated in the Grievance Redressal Policy. You have duties too: do not impersonate, suppress material information, or make false complaints (s.15).
>
> **11. Security and breach notice.** We apply reasonable security safeguards (s.8(5); DPDP Rules 2025 r.6 **[VERIFY]**): encryption in transit and at rest, tenant isolation, access control with multi-factor authentication for administrators, logging, backups, and tested incident response. If a personal data breach occurs we will inform the Data Protection Board and each affected Data Principal without delay in the form and timelines the Rules require (s.8(6); r.7 **[VERIFY]**). We report cyber incidents to CERT-In within six hours of noticing them where the CERT-In Directions of 28 April 2022 apply [LAW]. Where you are a regulated entity we notify your designated contact within the window stated in your Data Processing Agreement so that you can meet your own reporting duties.
>
> **12. When we act as a Processor.** When a customer uses LawDocsComply to process your data, the customer is the Data Fiduciary. We process only on its instructions under a Data Processing Agreement. Direct your requests to that customer; we will help it respond.
>
> **13. Cross-border transfer.** Our primary systems are in India (Mumbai; disaster recovery in Hyderabad). Confidential, financial, legal and regulated data — including everything our customers upload — is processed only on India-resident systems and AI endpoints. For public or non-personal content we may use processors outside India in countries not restricted by the Central Government under s.16 and the Rules (r.14 **[VERIFY]**), under contract. Current list: {{transfer_countries}}.
>
> **14. Cookies and similar technologies.** See the Cookie Policy. We ask for consent before any non-essential cookie and honour the Global Privacy Control signal.
>
> **15. Automated decisions and AI.** See the AI Use & Transparency Policy. We do not make legally significant decisions about you solely by automated means, and we do not use your content to train AI models. **Vidhi, our AI assistant, drafts and summarises; it does not certify compliance or file anything with a regulator.**
>
> **16. Changes to this notice.** We publish every version with its effective date. Material changes are notified in the app or by email at least 7 days before they take effect where practicable.
>
> **17. Contact and complaints.** {{dpo_name}}, {{dpo_email}}. Grievance Officer: {{grievance_officer}}, {{grievance_email}}, {{grievance_address}}. If unresolved, you may complain to the Data Protection Board of India (s.27) as notified by the Board **[VERIFY portal]**.
>
> **Annex A (GDPR/UK) and Annex B (CCPA/CPRA)** are not rendered for the India brand pack (`pol.gdpr_annex = false`, `pol.ccpa_annex = false`); they are switched on for a P25 regional brand pack after counsel review **[COUNSEL]**.

**Review checklist (LDC).** ☐ Entity, CIN, office, DPO and Grievance Officer verified against MCA and board records ☐ Purposes table matches the consent ledger purposes (P01) ☐ s.7(a) and s.7(i) reliance confirmed by counsel ☐ Health Check retention matches `web.hc.retention_days` ☐ Sub-processor list live from the Vendor Assurance Room ☐ Transfer list matches actual AI adapters enabled ☐ Breach timelines match P24 incident runbook ☐ Hindi summary reviewed ☐ No pre-DPDP language ☐ Statement "we do not obtain credit reports" consistent with X-07.

---

## AD.2 Terms of Use — LawDocsComply (Template 2 instance)

**Displayed at:** footer; sign-up acceptance (`consent.signup.terms`); Settings › About; checkout (linked). **Class:** terms (re-consent on MAJOR; 30-day notice). **Extra parameters:** `{{service_description}}` = "a multi-tenant compliance-management platform with a reviewed regulatory content library, compliance workflows, governance and board tools, risk and audit modules, regulatory returns preparation, document management and the Vidhi AI assistant"; `{{professional_boundary}}` below; `{{plan_terms_url}}` = /pricing.

> # Terms of Use — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Agreement.** These Terms are between you and {{entity_name}} (CIN {{cin}}, {{registered_office}}). By creating an account, clicking "I agree", or using LawDocsComply, you accept them. If you act for an organisation, you confirm you are authorised to bind it. The Privacy Notice, Payment & Subscription Terms, Refund & Cancellation Policy, Acceptable Use Policy, AI Use & Transparency Policy, Data Processing Agreement (for organisations) and any order form are part of this agreement. In a conflict, an executed order form prevails, then these Terms, then the policies.
>
> **2. The service.** LawDocsComply is {{service_description}}. We may improve or change features; we will not remove a material feature of a paid plan during its term without notice and a pro-rata remedy. Availability commitments are in the Service Level Agreement where your plan includes one. Regulatory content in the library is reviewed and cited; we tell you the source, the version and the date of review for every obligation, and we show you what changed when a regulation changes.
>
> **3. Eligibility and accounts.** You must be 18 or older and able to contract (Indian Contract Act 1872 s.11 [LAW]). Keep credentials confidential; use multi-factor authentication where we require it; tell us promptly at {{security_email}} of unauthorised use. You are responsible for activity under your account unless caused by our breach. Each user has their own login; sharing a login is a breach of these Terms and of the Acceptable Use Policy.
>
> **4. Professional-services boundary.** **LawDocsComply provides compliance-management software and curated regulatory information. It does not provide legal, secretarial, tax or audit opinions.** Using LawDocsComply does not create an advocate–client, adviser–client or fiduciary relationship with us. Where you engage an independent professional through our Marketplace, your engagement is with that professional under a separate engagement letter; we are not a party to it and we do not invoice for the professional's services (Appendix O rules). Content on lawdocscomply.com, including blog posts, resources, templates, health-check reports and AI outputs, is general information, not advice. **You remain responsible for your organisation's compliance, for every filing you make and for the accuracy of what you upload.** Our regulatory-change feed is compiled with care from official sources; where we find an error we correct it and notify affected customers, but we do not warrant that the feed is complete or that it reflects every regulatory action on the day it happens.
>
> **5. Acceptable use.** You will comply with the Acceptable Use Policy and with the Information Technology (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 r.3(1)(b) content restrictions [LAW]. We may remove content and suspend access as the AUP describes. You must not file knowingly false regulatory information through or with the help of the service.
>
> **6. Your content and our licence.** You own content you upload. You grant us a non-exclusive, worldwide, royalty-free licence to host, process, display and transmit it only to provide the service, to prevent abuse, and as the law requires. We do not use your content to train AI models. You warrant you have the rights to upload it, including the rights of the individuals whose data it contains.
>
> **7. Our intellectual property.** LawDocsComply, its software, designs, documentation, templates, the Excel question-sheet templates and their contract, the regulatory content library's structure and curation, and our trade marks belong to {{entity_name}} or its licensors. You receive a limited, revocable, non-transferable right to use them for your internal business purposes for the term of your plan. Regulatory texts themselves are public documents; our curation, mapping and annotations are ours. No reverse engineering except as permitted by law (Copyright Act 1957 s.52(1)(ab)–(ad) [LAW]). Feedback you give may be used freely without obligation.
>
> **8. AI-generated content.** Vidhi and other AI features generate outputs that may be inaccurate or incomplete. Outputs are labelled and dated. You must review them before relying on them, and a qualified human must approve any output used in a legal, financial or regulatory filing, in board minutes or in a compliance status change. See the AI Use & Transparency Policy. We disclaim warranties as to AI outputs to the extent the law allows.
>
> **9. Fees.** Fees, taxes, billing cycles, renewals and refunds are governed by the Payment & Subscription Terms and the Refund & Cancellation Policy. Regulatory filing fees, stamp duty and eSign charges we pay on your behalf are passed through at cost unless stated. Enterprise customers are invoiced on their order form.
>
> **10. Third-party services.** Payment gateways, eSign providers, company-data providers, your Microsoft 365 or Google Workspace, and any system you connect act under their own terms. We are not responsible for their services except as our contract with you states.
>
> **11. Suspension and termination.** We may suspend for non-payment (after notice and a cure period of at least 7 days), security risk, legal demand, or material breach. You may terminate at any time from Settings › Plans & subscription; cancellation is as easy as sign-up. On termination you may export your data in the `LDC-EXPORT-1.0` format for at least 30 days (90 days for enterprise plans and regulated entities); after that we delete it per the Retention Schedule, except what the law requires us to keep. Clauses that by nature survive, survive.
>
> **12. Warranties and disclaimers.** We provide the service with reasonable skill and care. Except as expressly stated, the service is provided "as is", and we exclude implied warranties to the extent permitted. Nothing excludes liability that cannot be excluded under the Consumer Protection Act 2019 where you are a consumer [LAW].
>
> **13. Limitation of liability.** To the extent permitted by law, neither party is liable for indirect, consequential or punitive loss, loss of profit, or regulatory penalties imposed on you (other than where caused by our breach of this agreement), and our aggregate liability is capped at {{liability_cap}}. The cap does not apply to death or personal injury caused by negligence, fraud, wilful misconduct, breach of confidentiality or data-protection obligations to the extent the law does not permit a cap **[COUNSEL]**.
>
> **14. Indemnity.** You indemnify us against third-party claims arising from your content or your unlawful use. We indemnify you against third-party claims that the service, used as permitted, infringes Indian intellectual property rights, subject to notice, control of defence and mitigation.
>
> **15. Confidentiality.** Each party protects the other's confidential information with reasonable care and uses it only for this agreement. Disclosure compelled by law is permitted with notice where lawful. Your compliance data is confidential information.
>
> **16. Governing law and dispute resolution.** Indian law governs. Courts at New Delhi have exclusive jurisdiction, subject to this clause. Before any claim, the parties will attempt resolution through the Grievance Redressal Policy. Either party may then refer the dispute to online mediation administered by Equator Resolution under its rules ({{odr_rules_url}}) [Option A: mandatory step | Option B: optional — default B]. Unresolved disputes between business customers and us [Option A: are referred to arbitration by a sole arbitrator seated at New Delhi under the Arbitration and Conciliation Act 1996, conducted online; language English | Option B: may be brought in the courts named above — default A for business customers, B for consumers]. **Equator Resolution is a company in the Infrabyx Group; its neutrals are independent and are appointed under its rules.** Nothing prevents a consumer from approaching a consumer commission under the Consumer Protection Act 2019 or a regulator's ombudsman [LAW] **[COUNSEL: enforceability of pre-dispute arbitration against consumers; adequacy of group-company disclosure]**.
>
> **17. Notices.** To us: {{support_email}} and {{registered_office}}. To you: your account email and in-app notices.
>
> **18. General.** Entire agreement; severability; no waiver; assignment only with consent except to an affiliate or successor; force majeure; electronic records and signatures are valid (Information Technology Act 2000 s.4, s.5, s.10A [LAW]); English version prevails; we publish prior versions.

**Review checklist (LDC).** ☐ Boundary clause approved by counsel ☐ Liability cap position set [OWNER] ☐ Consumer carve-outs present ☐ Arbitration/ODR option chosen; Equator group-company disclosure present ☐ Export period (30 / 90 days) matches P19 ☐ Cure period ≥ 7 days ☐ No conflict with the Refund Policy ☐ Marketplace statement consistent with Appendix O (no invoicing for practitioners' services) ☐ Hindi summary ☐ `pol.notice_days = 30`.

---

## AD.3 Payment & Subscription Terms — LawDocsComply (Template 3 instance)

**Displayed at:** footer; pricing page (above the fold, linked above the CTA); plan selection; checkout; invoice footer link. **Class:** terms (MAJOR → 30-day notice).

> # Payment & Subscription Terms — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Who you pay.** Plans for LawDocsComply are sold and invoiced by {{selling_entity_name}} (CIN {{selling_entity_cin}}, GSTIN {{selling_entity_gstin}}, {{selling_entity_address}}) ("Seller"), the merchant of record. {{#if selling_entity_differs}}The Seller is a group company of {{entity_name}}, which operates the service.{{/if}} Your statement will show "{{selling_entity_short}}".
>
> **2. Prices and taxes.** Prices are shown in INR for customers in India and in USD (or another listed currency) for customers outside India. For customers in India prices are shown exclusive of GST with the applicable rate stated beside each price, and the total payable including GST is shown before you confirm payment. GST is charged at the rate in force on information technology and software services (CGST Act 2017 and the rate notifications; SAC code and rate per plan line **[VERIFY — OI-IPB-13]**). Provide your GSTIN to receive a tax invoice with input credit details. Prices may change; changes apply to existing subscriptions only from the next renewal after at least 7 days' notice.
>
> **3. No hidden charges.** All mandatory fees are shown on the pricing page and at checkout before payment. Optional add-ons (additional entities, seats, AI credits, white-label, regulatory feeds, premium support) are never pre-selected. Pass-through statutory fees (government filing fees, stamp duty, eSign charges) are displayed as separate line items at cost before you confirm.
>
> **4. Billing cycles and renewal.** Self-serve plans bill monthly or annually in advance; enterprise plans bill per the order form. Subscriptions renew automatically for the same term unless you cancel before the renewal date. We send a renewal reminder at least 7 days before each renewal showing the amount, date and how to cancel. You can cancel in Settings › Plans & subscription in as few steps as it took to subscribe.
>
> **5. Free trials.** Trials last {{trial_days}} days where offered. **Your trial does not convert to a paid plan unless you expressly choose a plan and authorise payment.** At the end of the trial your account moves to read-only with export available for 30 days. We do not collect payment details for a trial.
>
> **6. Recurring payments and e-mandates (India).** Where you authorise recurring card or UPI payments, we and our payment gateway follow the Reserve Bank of India framework for e-mandates on recurring transactions: additional factor of authentication at registration; a pre-debit notification at least 24 hours before each debit with the amount and date; a simple way to pause, modify or cancel the mandate; and additional authentication for any debit above the limit the RBI permits without it [LAW: RBI circular DPSS.CO.PD.No.447/02.14.003/2019-20 of 21 August 2019 and subsequent circulars; **VERIFY current limit**]. UPI Autopay mandates follow NPCI rules **[VERIFY]**. We never store your card number; the gateway tokenises it under RBI card-on-file tokenisation rules [LAW; **VERIFY circular**].
>
> **7. Payment methods and gateways.** Payments are processed by {{gateway_names}}. We use hosted or tokenised checkout only; your card data never touches our servers (PCI DSS v4.0.1 SAQ A). Accepted methods are shown at checkout.
>
> **8. Failed payments and dunning.** If a payment fails we retry and notify you on days 3, 7 and 14. Your service continues for a grace period of 14 days. After that, paid features are suspended (read-only with export) until payment; we do not delete your data for non-payment before the Retention Schedule period for suspended accounts. Reactivation restores the same plan.
>
> **9. Invoices and credit notes.** A GST-compliant tax invoice (CGST Act 2017 s.31; CGST Rules r.46 [LAW]) is issued for every charge and available in Settings › Invoices; credit notes are issued for refunds and adjustments (s.34). E-invoicing applies where the Seller's turnover requires it **[VERIFY threshold]**. The service is activated immediately on payment and the invoice is emailed.
>
> **10. Currency and international payments.** Customers outside India may be charged in USD or other listed currencies; your bank may apply conversion charges. Export-of-services treatment for GST and FEMA compliance is handled by the Seller [LAW; **VERIFY**].
>
> **11. Chargebacks and disputes.** Contact {{support_email}} before raising a chargeback; most issues resolve within 7 working days. We respond to gateway disputes with transaction records. A chargeback found to be without basis may lead to suspension until resolved.
>
> **12. Credits and prepaid usage.** AI credits and prepaid usage expire 12 months after purchase unless the plan says otherwise, are non-transferable, and are refundable only as the Refund & Cancellation Policy states. Credit balances and usage are shown in Settings › Plans & subscription and Settings › AI & Vidhi.
>
> **13. Seats, entities and usage tiers.** Plans are priced by seats and by legal entities covered; usage above plan limits is shown in the app before it is charged and is never charged without your prior confirmation or an order form. Downgrades take effect at the next renewal; upgrades are pro-rated.
>
> **14. Refunds and cancellation.** See the Refund & Cancellation Policy, which forms part of these terms.
>
> **15. Changes.** Material changes take effect after 30 days' notice and never mid-term for a prepaid period without your consent.
>
> **16. Contact.** Billing queries: {{support_email}}, {{support_phone}} ({{support_hours}}). Grievances: see the Grievance Redressal Policy.

**Review checklist (LDC).** ☐ Selling entity and GST registration verified (D-27) ☐ SAC codes and rate confirmed by tax adviser ☐ GST display mode matches P20/P23 pricing page ☐ Trial position = never auto-convert (D-26) ☐ E-mandate clause matches current RBI limits ☐ Dunning and grace match OH8 ☐ Gateway names match live adapters ☐ No drip-pricing wording ☐ Links from pricing and checkout present.

---

## AD.4 Refund & Cancellation Policy — LawDocsComply (Template 4 instance)

> # Refund & Cancellation Policy — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Cancelling is as easy as signing up.** Cancel any time at Settings › Plans & subscription › Cancel, or by email to {{support_email}}. No phone call, retention screen or hidden step is required. Cancellation stops future renewals; you keep access until the end of the paid period unless you request immediate closure.
>
> **2. Refund windows (self-serve plans).** If you cancel within 7 days of a first purchase or renewal, we refund the full amount. Plan-specific rules are shown on the pricing page beside each plan and prevail where stricter in your favour. **Enterprise contracts:** refunds are per the order form.
>
> **3. Non-refundable items.** Statutory fees paid to third parties on your behalf (government filing fees, stamp duty), eSign charges, completed professional services engaged through the Marketplace (payable to the professional under your engagement with them), used AI credits and prepaid usage, and completed Academy courses once more than one module has been accessed **[OWNER]**. Where a statutory fee is itself refundable by the authority, we assist you in applying.
>
> **4. Service failure.** If we fail to meet an SLA commitment or a material feature is unavailable for a prolonged period, you may claim service credits under the SLA or, where the failure is material and uncured for 30 days, terminate and receive a pro-rata refund of prepaid fees.
>
> **5. Mistaken or duplicate payments.** Report within 30 days; we refund in full after verification.
>
> **6. How and when we refund.** Approved refunds are issued to the original payment instrument within 5–7 working days of approval. Your bank or card issuer may take additional time to show the credit. We issue a credit note for every refund. We do not refund to a different instrument except where the original is closed, on verification.
>
> **7. Trials.** No charge is made during a trial and trials never convert automatically to a paid plan.
>
> **8. Consumer rights.** Nothing in this policy limits your rights under the Consumer Protection Act 2019 or any regulator's rules [LAW].
>
> **9. Contact.** {{support_email}}, {{support_phone}}. Unresolved refund complaints go to the Grievance Officer: {{grievance_officer}}, {{grievance_email}}.

**Review checklist (LDC).** ☐ Refund rule per plan [OWNER] ☐ 5–7 working days achievable with the gateway refund API through OH8 ☐ Non-refundable list accurate (Academy position [OWNER]) ☐ Cancellation flow tested for step parity with sign-up ☐ Credit-note process confirmed with finance.

---

## AD.5 Cookie Policy — LawDocsComply (Template 5 instance)

**Class:** privacy (DPO). The cookie table is generated from the CMP vendor registry (`Studio › Cookie & Consent`), never typed; the policy and the banner read one source (P23 FR-P23-226).

> # Cookie Policy — LawDocsComply
> Version 1.0 · Effective {{effective_date}} · [Open cookie settings]
>
> **1. What cookies are.** Small files or similar identifiers (local storage, pixels, SDK identifiers) placed on your device.
>
> **2. How we ask.** On your first visit to lawdocscomply.com we show a banner with Accept all, Reject all and Manage of equal prominence. We set no non-essential cookie before you choose. Closing the banner without choosing means Reject. We honour the Global Privacy Control browser signal. You can change your choice at any time from the Cookie settings link in the footer. Your choice is recorded with a receipt identifier so we can prove what you agreed to.
>
> **3. Categories.** *Necessary* — needed for the site and app to work (session, security, consent record, load balancing, your accessibility preferences such as font and contrast); cannot be switched off. *Functional* — remember preferences (language, click-to-load video). *Analytics* — help us understand use of the public site through first-party analytics hosted in India ({{analytics_adapter_names}}); on logged-in pages we use only first-party, cookieless measurement. *Marketing* — measure campaigns on third-party platforms; used only on the public site, never on logged-in pages, the Health Check answer pages, the grievance form or legal pages, and never without your consent.
>
> **4. Cookies we use.** {{cookie_table}} — Name · Provider · Category · Purpose · Duration · First/third party.
>
> **5. Third-party content.** Embedded videos and maps load only after you click and, where needed, consent. Once loaded, the provider's own policy applies (we use privacy-enhanced modes where available).
>
> **6. Mobile and desktop apps.** LawDocsComply has no mobile advertising SDK. Any future app will use device identifiers only for security, crash reporting and, with consent, first-party analytics.
>
> **7. Changes.** We update this policy when our cookies change; the banner re-asks when a change is material.
>
> **8. Contact.** {{dpo_email}}.

**Review checklist (LDC).** ☐ Table generated from the registry ☐ Every third party has a DPA or terms reference ☐ GPC behaviour true in code ☐ `mkt.sensitive_routes` list matches clause 3 ☐ Accessibility preference cookie classified Necessary.

---

## AD.6 AI Use & Transparency Policy — LawDocsComply (Template 6 instance)

**Displayed at:** footer; first use of any AI feature (`consent.ai.first_use`); Settings › AI & Vidhi. **Class:** notice (acknowledgement on MAJOR). **Source text:** Appendix K §K.12 (LawDocsComply AI Use Statement, claims-registered).

> # AI Use & Transparency Policy — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Our AI assistant.** LawDocsComply includes an AI assistant called {{ai_display_name}} (built on the Infrabyx "Vidhi AI" system). It drafts, summarises, classifies, extracts, translates and suggests. It does not decide. Every action with external or irreversible effect requires a human to confirm it.
>
> **2. Where AI is used.**
>
> | Feature | What it does | Data it uses | Human review required | How to opt out |
> |---|---|---|---|---|
> | Regulatory change digest | Summarises what changed in a regulation and which of your obligations are affected | Published regulatory texts; your applicability profile | Yes — a compliance officer accepts each re-mapping | Settings › AI & Vidhi (per tenant) |
> | Obligation extraction and question authoring | Drafts compliance questions from a regulation for review | Regulatory texts | Yes — maker-checker before publication | Platform feature; outputs never publish without review |
> | Drafting Studio | Drafts policies, minutes, agendas, letters and reports with tracked changes | Your templates and records you select | Yes — nothing is sent, filed or adopted without a person | Settings › AI & Vidhi |
> | Document intelligence | Reads uploaded PDFs, images, letters and spreadsheets; produces type copies and translations | Documents you upload | Yes — figures are never typed by AI into a return or calculation | Settings › AI & Vidhi |
> | Knowledge notebooks | Answers questions over curated regulatory sources and your own documents, with citations | Sources in the notebook | Yes — citations shown; "no source" stated when none | Per notebook |
> | Evidence and control gap summaries | Lists missing evidence and suggests requests | Your compliance register | Yes — requests are sent by a person | Settings › AI & Vidhi |
> | Board-pack narrative | Drafts narrative sections from approved figures | Approved reports | Yes — Company Secretary approves | Settings › AI & Vidhi |
> | Scheduled tasks and missions | Runs recurring internal tasks (reminders, draft digests, data checks) within limits your administrator sets | As each task defines | Yes — autonomy limits; locked actions always need a person | Settings › AI & Vidhi › Schedules |
> | Health Check narrative (public site) | Writes the plain-language explanation of your Health Check Score | Your answers | Reviewed templates; score is deterministic | Decline the narrative on the result page |
> | Marketing imagery (our website) | Generates illustration images for our own site and blog | Prompts written by our staff | Yes — a named reviewer approves and every image is labelled | Not applicable to your data |
>
> **3. Labelling.** Content produced or materially altered by AI is labelled "AI-generated — review before use", carries the generation date and the model family, and, for images, carries visible and embedded provenance markers as required for synthetically generated information under the IT Rules 2021 as amended in 2026 [LAW; **VERIFY rule numbering**]. We do not remove such labels and you must not remove them when sharing within the platform.
>
> **4. Limits.** AI outputs may be wrong, outdated or incomplete. They may cite law that has changed. They are not legal, secretarial, tax, audit or regulatory advice and do not replace a qualified professional. **{{ai_display_name}} does not certify compliance and does not file anything with a regulator.** It never changes a compliance status, closes a finding, changes an owner or submits a return on its own.
>
> **5. Human review.** The following always require a qualified human's approval before use: {{human_review_list}}.
>
> **6. Your data and AI.** Your content is processed by AI providers only to produce the output you asked for. We contractually require zero retention and no training on your data. We do not use your content to train our or anyone's models. Confidential, financial, legal, HR and regulated data classes are processed only on India-resident endpoints; if none is available the feature fails closed rather than sending data abroad. Aadhaar numbers are never sent to any model.
>
> **7. Providers.** We use multiple model providers ({{llm_providers}}) through a routing layer; the provider for each run is shown in the output's details panel. The list is updated here and at {{sub_processor_list_url}}.
>
> **8. Automated decisions.** We do not make decisions that produce legal or similarly significant effects about you solely by automated processing. Where AI assists a decision (for example flagging an obligation as possibly affected by a regulatory change), a human makes the decision and you may ask for an explanation and a review.
>
> **9. Opt-out and controls.** You may turn off AI features at Settings › AI & Vidhi (organisation administrators may do so for all users and may tighten autonomy limits per skill). Some features are then unavailable. You may delete AI run history from Settings; audit copies required by law are retained per the Retention Schedule.
>
> **10. Agents.** Where {{ai_display_name}} runs multi-step tasks ("missions"), each step is logged, visible to you, and bounded by autonomy limits set by your administrator. Agents cannot approve, sign, pay, file or change a compliance status.
>
> **11. Misuse.** You may not use AI features to generate unlawful, deceptive, defamatory or infringing content, to impersonate, to fabricate evidence or regulatory submissions, or to produce unlabelled synthetic media. See the Acceptable Use Policy.
>
> **12. Feedback and incidents.** Report harmful or incorrect outputs through the in-app feedback control; we review and may suspend a feature. Serious incidents are handled under our incident process, recorded in our AI system register and reported where the law requires.
>
> **13. Contact.** {{dpo_email}}.

**Review checklist (LDC).** ☐ Feature table matches shipped skills (Appendix K) ☐ Provider list matches the model registry ☐ Zero-retention contracts on file per adapter (OI-IPB-05) ☐ Labelling and C2PA tested ☐ Human-review list = P17 FR-P17-73 locked actions ☐ Opt-out and ceilings exist in Settings › AI & Vidhi.

---

## AD.7 Grievance Redressal Policy — LawDocsComply (Template 7 instance)

> # Grievance Redressal Policy — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Grievance Officer.** {{grievance_officer}}, {{grievance_email}}, {{grievance_phone}}, {{grievance_address}}. Hours: {{support_hours}}.
>
> **2. How to complain.** In-app: Help › Raise a grievance (gives you a reference number); web form at lawdocscomply.com/grievance; email; post. Include your account email, what happened, when, and what outcome you seek. You may complain about content, privacy, service, billing, accessibility, our AI features or conduct.
>
> **3. Timelines.** We acknowledge within 48 hours with a reference number. We resolve within 30 days. Where the law sets a shorter time we follow it: complaints about unlawful content as an intermediary (for example a user-authored blog post) are acknowledged within 24 hours and disposed of within 15 days; certain classes of content are removed within 72 hours or, for unlawful synthetically generated content, within 3 hours of a complaint or order [LAW: IT Rules 2021 r.3(2) as amended; **VERIFY current text and the 2026 amendment**]. Data-principal requests under the DPDP Act are answered within the period the Rules prescribe (**VERIFY**; default 30 days). Accessibility problems are acknowledged within 2 working days and fixed or given an alternative within 10 working days.
>
> **4. Escalation.** If you are not satisfied: (a) ask for review by {{escalation_officer}} within 7 days; (b) use mediation through Equator Resolution, a company in our group, at no cost to you for consumer disputes — participation is voluntary, the mediator is an independent panel neutral and not our employee, and this route never limits your right to approach the bodies below **[OWNER]** **[COUNSEL: group-company neutrality disclosure; Mediation Act 2023 s.4–5 voluntariness]**; (c) approach the external bodies below.
>
> | Matter | External body |
> |---|---|
> | Consumer matters | Consumer Commission under the Consumer Protection Act 2019 |
> | Personal data | Data Protection Board of India (DPDP Act 2023 s.27) as notified **[VERIFY portal]** |
> | Accessibility | Chief Commissioner for Persons with Disabilities or the State Commissioner (RPwD Act 2016) |
> | Content as intermediary | Grievance Appellate Committee under IT Rules 2021 r.3A **[VERIFY]** |
>
> **5. Records.** We keep a register of grievances, actions and outcomes and report aggregate numbers in our half-yearly Transparency Report in the Trust Centre. Personal data in complaints is processed under the Privacy Notice.
>
> **6. No retaliation.** Making a complaint in good faith will never affect your service.

**Review checklist (LDC).** ☐ Officer appointed by board resolution; named consistently in footer, `/grievance`, `/contact` and MCA filings where applicable ☐ Timelines match P14 ticket SLAs and `pol.grievance.*` ☐ Reference-number generation tested ☐ Hindi version ☐ Transparency Report cadence set (half-yearly).

---

## AD.8 Acceptable Use Policy — LawDocsComply (Template 8 instance)

> # Acceptable Use Policy — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Prohibited content.** Content that belongs to another person without right; is defamatory, obscene, pornographic, paedophilic, invasive of privacy including bodily privacy, insulting or harassing on the basis of gender, racially or ethnically objectionable, relating to or encouraging money laundering or gambling, or otherwise unlawful; harmful to children; infringes any patent, trade mark, copyright or other proprietary right; deceives or misleads about the origin of a message or communicates information that is patently false or misleading and is published to cause injury; impersonates another; threatens the unity, integrity, defence, security or sovereignty of India, friendly relations with foreign States, or public order, or incites an offence; contains software viruses or malicious code; or is patently false and untrue and published to mislead or harass for financial gain or injury (IT Rules 2021 r.3(1)(b)(i)–(xi) [LAW; **VERIFY current list**]).
>
> **2. Prohibited conduct.** Unauthorised access; credential sharing beyond licence (one login per person); scraping beyond published API limits (developers.lawdocscomply.com/limits); security testing outside the Security & Responsible Disclosure Policy; circumventing usage limits; reselling without a reseller or white-label agreement; using the service to provide a competing service; sending unsolicited commercial messages; removing AI labels; uploading unlabelled synthetic media; processing data you have no right to process; using the service for a purpose that violates sanctions or export laws.
>
> **3. Regulated-use limits.** **You must not file, or prepare for filing, knowingly false regulatory information** through or with the help of LawDocsComply; you must not record a compliance status, evidence or attestation you know to be untrue; you must not use the Health Check, the regulatory library or AI outputs to represent to any regulator, auditor or counter-party that LawDocsComply has certified or verified your compliance; you must not upload Aadhaar numbers or biometric data; you must not use the Marketplace to solicit professional work in breach of the Bar Council of India Rules, ICSI, ICAI or ICMAI codes of conduct [LAW].
>
> **4. Enforcement.** Warning; content removal; feature restriction; suspension; termination; referral to law enforcement. We notify you with reasons and a route to the Grievance Officer except where notice is prohibited or would frustrate an investigation. Content removal timelines follow the Grievance Redressal Policy.
>
> **5. Reporting.** Report abuse at {{grievance_email}} or in-app.

**Review checklist (LDC).** ☐ Rule 3(1)(b) list verbatim-checked ☐ Enforcement ladder matches P23 moderation and P01 suspension tooling ☐ Professional-conduct references consistent with Appendix O.

---

## AD.9 Data Retention & Deletion Schedule — LawDocsComply (Template 9 instance)

**Class:** privacy (DPO). The schedule table is rendered from the retention registry (P19 FR-P19-62; `dat.*`), with the IPB baseline rows plus LDC rows below. Floors are locked in the product.

> # Data Retention & Deletion Schedule — LawDocsComply
> Version 1.0 · Effective {{effective_date}}
>
> **1. Principle.** We keep personal data only as long as needed for the stated purpose or as the law requires, then delete it securely and instruct processors to do the same. "Delete" means removal from live systems and backups within the backup rotation period stated below; cryptographic erasure is used for immutable storage.
>
> **2. Schedule.** The IPB baseline rows (account profile; authentication logs 180 days; hash-chained audit ledger 8 years; tax invoices and payment records 8 years; consent ledger life of consent + 3 years; support tickets 3 years; marketing leads 24 months; first-party analytics 14 months aggregate / 90 days raw; server logs 90 days; backups 35-day rotation; job applications 12 months; grievance register 3 years; AI run logs 90 days user-visible; inactive account data 3 years with notice) apply. **LawDocsComply-specific rows:**
>
> | Record type | Basis | Trigger | Period | Method | Exceptions |
> |---|---|---|---|---|---|
> | Compliance register, instances, evidence and filings (as Processor) | Customer instruction; Companies Act 2013 s.128 books and records **[VERIFY applicability per record type]**; sector directions (Appendix G) | Financial year end or account closure | 8 years, or the statute-specific period if longer; customer may set longer | Object Lock then delete; export offered before deletion | Legal hold |
> | Board and committee records, minutes, registers (as Processor) | Companies Act 2013 (minutes: permanently under SS-1 and s.118 **[VERIFY]**) | Account closure | Exported to the customer; deleted 90 days after the export window unless a longer period is instructed | Export then delete | Legal hold |
> | Regulatory returns working files | Customer instruction; regulator record-keeping periods (Appendix I) | Return filed | 8 years or regulator period | Archive then delete | — |
> | Health Check sessions (public site) | Consent | Completion | 365 days (`web.hc.retention_days`) or earlier on request | Delete | Converted sessions move to the tenant baseline |
> | Policy acceptance ledger (your acceptance of our Terms and notices) | Proof of acceptance | Account closure | 8 years | Archive | — |
> | Vendor Assurance Room download logs (acknowledgement log) | Customer's due-diligence evidence | Download | 8 years | Archive | — |
> | Vidhi notebooks and outputs (tenant) | Contract | Notebook deletion or closure | Deleted with the notebook; outputs retained as records only where filed by a person | Delete | Legal hold |
> | Agent memory | Contract | Last use | 90 days (`vidhi.memory.retention_days`) | Delete | Sealed classes never stored |
> | Suspended-account data (non-payment) | Contract | Suspension | 180 days then the account-closure row applies | Read-only, export, then delete | — |
>
> **3. Legal hold.** Deletion is suspended for records subject to litigation, regulatory inquiry or a lawful request; the hold is logged in the audit ledger and lifted when the reason ends. Customers may place and release legal holds on their own records in Settings › Storage & data.
>
> **4. Your requests.** Erasure requests under DPDP Act s.12 are honoured within the Grievance Redressal timeline unless a listed retention duty applies, in which case we tell you which.

**Review checklist (LDC).** ☐ Every row maps to a job or a documented process (P19) ☐ Statutory minima verified (OI-IPB-09) ☐ Backup rotation matches P24 configuration ☐ Legal-hold tooling exists ☐ Processor deletion instructions in DPA Annex 2.

---

## AD.10 Accessibility Statement — LawDocsComply (Template 10 instance)

**Displayed at:** footer "Accessibility"; `/accessibility`; Settings › Accessibility. Generated with the known-issues table from the accessibility backlog (P23 §4L); `conformance_status` is set from the last audit — never over-claimed.

> # Accessibility Statement — LawDocsComply
> Version 1.0 · Last reviewed {{last_reviewed}}
>
> **1. Commitment.** {{entity_name}} wants everyone to use LawDocsComply, including people who use assistive technology. We design to the Web Content Accessibility Guidelines (WCAG) 2.2 Level AA, Indian Standard IS 17802 and, where deployed for government bodies or listed companies that require it, the Guidelines for Indian Government Websites (GIGW) 3.0.
>
> **2. Conformance status.** LawDocsComply web (lawdocscomply.com, app.lawdocscomply.com) is {{conformance_status}} conformant with WCAG 2.2 AA as at {{last_audit_date}}, assessed by {{audit_method}} (automated testing with axe-core on every build, manual testing with NVDA/Firefox, JAWS/Chrome, VoiceOver/Safari and TalkBack, keyboard-only testing, 200% zoom, high-contrast and reduced-motion modes).
>
> **3. What we do.** Keyboard access to every function; visible focus; skip links; text alternatives for images; captions (English and, where offered, Hindi) and transcripts for every video; live captions for webinars; colour contrast of at least 4.5:1 enforced by our design tooling — status is always shown with an icon and a word, never colour alone; resizable text and a dyslexia-friendly font option; no time limits without extension; error messages in text; consistent navigation; language tags; accessible PDFs or an accessible alternative on request; compliance registers and dashboards that work at 320 px width with a column chooser and a data-table view of every chart.
>
> **4. Known limitations.** {{known_issues_table}} — Area · Issue · WCAG criterion · Workaround · Target fix date. Third-party content (payment gateway pages, embedded videos, maps) may not fully conform; we choose vendors that commit to accessibility and provide alternatives.
>
> **5. Feedback and requests.** Email {{a11y_email}} or use the "Report a problem" control on any page (works without JavaScript). We acknowledge within 2 working days and aim to fix or provide an alternative within 10 working days. For documents, ask for an accessible format and we will provide one free of charge.
>
> **6. Enforcement.** If you are not satisfied, use the Grievance Redressal Policy. You may also approach the Chief Commissioner for Persons with Disabilities or the State Commissioner under the Rights of Persons with Disabilities Act 2016 [LAW].
>
> **7. Technical.** Relies on HTML, WAI-ARIA, CSS, JavaScript (progressive enhancement; core content works without it), WebVTT. Tested on current versions of major browsers and screen readers.

**Review checklist (LDC).** ☐ Known-issues table generated from the backlog and dated ☐ Audit date within 6 months ☐ Mailbox monitored ☐ Claims match axe/CI results ☐ Hindi version ☐ IS 17802 clause map [VERIFY] (OI-P23-03).

---

## AD.11 Security & Responsible Disclosure — LawDocsComply (Template 11 instance)

> # Security & Responsible Disclosure — LawDocsComply
> **1. Our posture.** We follow OWASP ASVS 5.0 Level 2 (Level 3 for identity, the credential vault, payments and exports), encrypt data in transit (TLS 1.2+) and at rest, isolate every tenant with database-level policies, enforce MFA for administrators, log and monitor access, test our code and dependencies on every build, and run independent penetration tests by a CERT-In empanelled auditor at least annually. Certifications and audit reports we actually hold are listed in the Trust Centre with issuer, scope and validity: {{certifications_held}}. **We do not claim certifications we do not hold.**
>
> **2. Reporting a vulnerability.** Email {{security_email}} (PGP: {{pgp_key_url}}) or use the form at lawdocscomply.com/security/report. Include steps to reproduce, affected URL or component, and impact. We acknowledge within 2 working days, give an initial assessment within 7 days, and keep you informed until resolution. Critical issues are triaged within 24 hours.
>
> **3. Scope.** lawdocscomply.com, app.lawdocscomply.com, console.lawdocscomply.com, developers.lawdocscomply.com, our public APIs and the `ldc-mcp` server. Out of scope: third-party services (payment gateway pages, eSign providers, company-data providers), social engineering, physical attacks, denial of service, rate-limit findings without impact, best-practice findings without a demonstrated vulnerability.
>
> **4. Rules of engagement.** Do not access, modify or exfiltrate data that is not yours; use the sandbox or your own test account; stop and report at the first sign of personal data exposure; no automated scanning that degrades service; no public disclosure before we fix or 90 days pass, whichever is earlier, unless we agree otherwise.
>
> **5. Safe harbour.** If you follow these rules we will not pursue civil action or a complaint under the Information Technology Act 2000 (including s.43 and s.66) and will not report you to law enforcement for your research; we will support you if a third party does **[COUNSEL: wording — Indian law has no statutory safe harbour; this is a contractual undertaking]**. We will credit you in our acknowledgements if you wish.
>
> **6. Rewards.** {{bounty}}.
>
> **7. Incidents.** We report cyber incidents to CERT-In within six hours of noticing them (CERT-In Directions, 28 April 2022 [LAW]), notify affected users and the Data Protection Board as the DPDP framework requires, notify regulated customers within the contractual window in their Data Processing Agreement, and publish a post-incident summary in the Trust Centre where appropriate.
>
> **8. security.txt.** Canonical: https://lawdocscomply.com/.well-known/security.txt — Contact, Expires (≤ 1 year), Encryption, Acknowledgments, Preferred-Languages: en, hi, Canonical, Policy.

**Review checklist (LDC).** ☐ security.txt served with correct Expires ☐ Mailbox monitored, PGP key valid ☐ Scope matches live hosts in the brand pack ☐ Certifications from the Vendor Assurance Room only ☐ Safe-harbour wording approved ☐ Bounty position [OWNER].

---

## AD.12 Blog & User-Generated Content Terms — LawDocsComply (Template 12 instance; published only when `web.blog.user_posts.enabled = true`)

> # Blog & User-Generated Content Terms — LawDocsComply
> **1. Eligibility.** You may submit posts if your account meets the eligibility shown in the editor (tenant users with the author permission, verified practitioners, or invited guests). Submissions are reviewed before publication; we may decline without reasons where the law permits, and we tell you the decision within 5 days.
>
> **2. Your content, your responsibility.** You confirm the content is yours or licensed to you, is accurate to your knowledge, does not infringe rights, is not defamatory, and complies with the Acceptable Use Policy and IT Rules 2021 r.3(1)(b) [LAW]. You must disclose conflicts of interest and any paid relationship. You must label AI-assisted writing where it is material and never submit unlabelled synthetic media. **You must not present regulatory-filing instructions as official or as the position of any regulator.**
>
> **3. Not professional advice.** Posts express the author's view. They are not legal, secretarial, financial, tax or regulatory advice from {{entity_name}} or the author to any reader. We display an "Author's view — not advice" label and this notice on every user post. Authors who are advocates must comply with the Bar Council of India Rules, Part VI, Chapter II, Rule 36 [LAW]; posts that solicit work will be declined. Authors who are company secretaries, chartered accountants or cost accountants in practice must comply with their institutes' advertising guidelines **[VERIFY ICSI/ICAI/ICMAI guidelines]**.
>
> **4. Licence.** You grant {{entity_name}} a non-exclusive, perpetual, worldwide, royalty-free licence to publish, reproduce, adapt (for format, length and accessibility), translate, and distribute the content on lawdocscomply.com, in our newsletters, feeds and social channels, with attribution "by [author name], [designation], published on LawDocsComply". You keep ownership and may republish elsewhere after publication with a canonical link to lawdocscomply.com. You may ask us to unpublish at any time; copies in feeds, caches and archives may persist.
>
> **5. Moderation and edits.** We may edit for style, accessibility, legal compliance and accuracy of citations (our law register checks every cited instrument), and will show material edits to you before publication. We may add editor's notes, corrections and dates.
>
> **6. Takedown and complaints.** Anyone may complain about a post through the Grievance Redressal Policy. We may remove content on complaint, legal order or our own judgement, within the timelines that policy states, and will notify you with the reason and a route to respond. Repeated violations end eligibility.
>
> **7. Defamation and indemnity.** You indemnify {{entity_name}} against claims arising from your content. We may disclose your identity when lawfully required.
>
> **8. Comments.** Where comments are enabled, they are pre-moderated, must follow these Terms, and may be closed on any post.
>
> **9. Our role.** {{entity_name}} acts as an intermediary for user content under the IT Act 2000 s.79 and observes due diligence under the IT Rules 2021 [LAW; INTERP as to our status for our own editorial content].

**Review checklist (LDC).** ☐ Licence scope agreed [OWNER] ☐ Advocate and institute screening process defined (OI-P23-35) ☐ Takedown SLA matches Template 7 ☐ "Author's view" label implemented (NN-64) ☐ Terms version captured at acceptance (`consent.ugc.terms`).

---

## AD.13 Resources Download Terms — LawDocsComply (Template 13 instance)

> # Resources Download Terms — LawDocsComply
> **1. Licence.** Unless an item states a different licence, you may download, store and use the resource for your personal or internal business purposes, and share unmodified copies with attribution and a link to the source page. You may not sell it, remove notices, present it as your own, or use it to train AI models. Templates, checklists and sample registers may be adapted for your own internal use. The Excel question-sheet templates (`LDC-TPL-*`) are licensed for use with LawDocsComply and for your internal compliance work; they may not be redistributed as a product.
>
> **2. Currency.** Each resource shows its version, date and review date. Law and regulation change; check the source page for the current version and do not rely on an item past its review date. Regulatory summaries cite the instrument and the date we last checked it.
>
> **3. No advice.** Resources are general information, not legal, secretarial, financial, tax or regulatory advice. Seek professional advice for your situation. Sample board packs and registers are synthetic illustrations.
>
> **4. Accuracy.** We take care but give no warranty of completeness; report errors to {{support_email}} and we will correct and re-version.
>
> **5. Gated items.** Where we ask for your name and email, we use them as the notice on the form states and under the Privacy Notice; marketing contact needs your separate, unticked consent.
>
> **6. Citation.** Cite as shown on the item page.

---

## AD.14 Template 14 — not adopted (D-71)

LawDocsComply does not publish Marketplace / Professional Terms as a public legal page. Practitioner conduct, listing rules, engagement letters and the rule that LDC never invoices for a practitioner's services are governed by Appendix O and the Marketplace module (P21); the Terms of Use cl. 4 states the platform's role. If the owner later enables fee-bearing professional engagements through LDC with an escrow arrangement, Template 14 is adopted as a new instance after the counsel opinion recorded in `02` §5 question 2 **[COUNSEL]**.

---

## AD.15 Data Processing Agreement — LawDocsComply (Template 15 instance)

**Displayed at:** Trust Centre (DPA request → signed copy); enterprise order forms; self-serve acceptance at organisation creation (`consent.dpa.clickwrap`, `pol.dpa_clickwrap = true`). **Class:** privacy (DPO). `{{regulated_customer}}` switch ON for RBI/SEBI/IRDAI/IFSCA entities and co-operative banks; Annex 4 renders for them.

> # Data Processing Agreement — LawDocsComply
> **1. Roles.** Customer is the Data Fiduciary (or Data Processor to its own principals); {{entity_name}} is the Data Processor (DPDP Act 2023 s.8(2) [LAW]). Infrabyx group companies and listed sub-processors act as sub-processors.
>
> **2. Instructions.** We process personal data only on Customer's documented instructions, including through the product's settings, workflows and APIs, and as the law requires (with notice unless prohibited). Vidhi processes Customer data only within the autonomy limits Customer sets and never takes a locked action without a person.
>
> **3. Confidentiality and personnel.** Staff bound by confidentiality; access on need-to-know with product-scope segregation (Infrabyx staff with scope on another product cannot see Customer's data); background checks per our HR policy; support access to a tenant only through a time-boxed grant the Customer can see and revoke in Settings.
>
> **4. Security.** Measures in Annex 2 (ASVS 5.0 L2/L3, encryption, tenant isolation, MFA, logging, backups, Object Lock, vulnerability management, annual penetration testing by a CERT-In empanelled auditor, incident response). We maintain certifications listed in the Trust Centre and notify Customer of loss of any.
>
> **5. Sub-processors.** Current list at {{sub_processor_list_url}}. We give at least 30 days' notice of additions or replacements by email and Trust Centre subscription; Customer may object on reasonable data-protection grounds; if unresolved Customer may terminate the affected service with a pro-rata refund. Sub-processors are bound by equivalent terms; we remain liable for them. AI model providers are sub-processors bound to zero retention and no training.
>
> **6. Data Principal requests and assistance.** We forward requests received directly and assist Customer with access, correction, erasure, nomination and grievance obligations through product features or within 10 working days.
>
> **7. Personal data breach.** We notify Customer without undue delay and in any case within **2 hours** of confirming a breach affecting its data where Customer is a regulated entity (24 hours otherwise), with the information needed for Customer's notification to the Data Protection Board, its regulator and Data Principals (DPDP Act s.8(6); Rules r.7 **[VERIFY]**), followed by updates and a root-cause report within 72 hours where available. We report to CERT-In within 6 hours as the Directions require [LAW].
>
> **8. Audits.** Customer (or its appointed auditor, under confidentiality) may audit once in any 12 months on 30 days' notice, and after a breach. We provide reports, penetration-test summaries and completed questionnaires through the Vendor Assurance Room (Settings › Security & trust) first; on-site or remote audits where reports do not suffice. {{#if regulated_customer}}Customer's regulator (the Reserve Bank of India, SEBI, IRDAI, IFSCA or the Registrar of Co-operative Societies as applicable) has the right to access our premises, systems, records and personnel relating to Customer's data and to conduct or commission audits, and we will co-operate at no additional charge [LAW: RBI (NBFC – Managing Risks in Outsourcing) Directions 2025 and the commercial-bank equivalent of 28 November 2025 — audit and access clauses; **VERIFY paragraph numbers**].{{/if}}
>
> **9. Location and transfers.** Data stored and processed in India (Mumbai; DR Hyderabad). Transfer outside India only with Customer's prior written approval and to permitted countries (DPDP Act s.16). {{#if regulated_customer}}Regulated data stays in India as the RBI requires; AI processing of Customer data uses India-resident endpoints only.{{/if}}
>
> **10. Business continuity.** Documented BCP/DR tested at least annually; RPO and RTO as the SLA states; results summarised in the Vendor Assurance Room. {{#if regulated_customer}}Aligned to ISO 22301 and RBI IT Governance Direction 2023 expectations [REC].{{/if}}
>
> **11. Sub-contracting chain and concentration.** We disclose material sub-contractors and their locations; we inform Customer of changes that could create concentration risk at Customer's level; our cloud concentration statement is in the Vendor Assurance Room.
>
> **12. Return and deletion; exit assistance.** On termination Customer may export all data in `LDC-EXPORT-1.0` format for 90 days; we then delete and certify deletion within 30 days, except what the law requires us to keep (Retention Schedule). {{#if regulated_customer}}We provide reasonable exit assistance, including transition support, data migration and continued service for up to 90 days, so that Customer's services to its own customers and its regulatory reporting are not disrupted (RBI outsourcing exit-strategy requirements [LAW; **VERIFY**]).{{/if}}
>
> **13. Liability.** As in the main agreement; data-protection breaches are not excluded from liability to the extent the law requires.
>
> **14. Term.** Co-terminous with the service agreement; survives for data still held.
>
> **Annex 1** — Processing details (categories: compliance records, officer and director data, board papers, evidence files, HR and labour records where the HRMS module is used, grievance records; purposes: compliance management; data classes per Appendix Q §Q.3). **Annex 2** — Security measures (from IPB-02 and Appendix Q). **Annex 3** — Sub-processors (generated from the Vendor Assurance Room). **Annex 4** — RBI/SEBI/IRDAI outsourcing clauses for regulated customers: access for the regulated entity and its regulator; confidentiality; sub-contracting only with consent; monitoring and reporting; BCP; exit; dispute resolution; India law governing; no transfer of the outsourced activity without consent; cyber-incident notification within the contractual window so the regulated entity can meet its own six-hour reporting duty **[VERIFY paragraphs — OI-IPB-08]**.

**Review checklist (LDC).** ☐ Breach timelines consistent with P24 runbook and `trust.incidents.contractual_window_hours` ☐ Sub-processor notice automation live ☐ Annex 4 paragraphs verified against the 28 Nov 2025 Directions ☐ Export format implemented (P19) ☐ Deletion certificate template exists ☐ Clickwrap captures signatory authority (`consent.dpa.clickwrap`).

---

## AD.16 Service Level Agreement — LawDocsComply (Template 16 instance)

| Element | LawDocsComply content |
|---|---|
| Measurement | Monthly uptime % = (minutes in month − downtime minutes) ÷ minutes in month, measured by our external monitoring published at {{status_page_url}}; downtime = core functions (login, compliance register, calendar, evidence upload) unavailable for all users of a region for ≥ 5 consecutive minutes |
| Tiers (defaults; OH8 catalogue prevails — Appendix N) | Free trial and Essentials: no SLA, best effort · Professional (Business): 99.5% · Enterprise: 99.9% · **Regulated Enterprise** (RBI/SEBI/IRDAI/IFSCA entities and co-operative banks): 99.9% with RPO {{rpo_hours}} h and RTO {{rto_hours}} h **[VERIFY against P24 §4F]** |
| Credits | Professional: 5% of monthly fee per 0.5% below target, cap 25%; Enterprise and Regulated Enterprise: 10% per 0.5%, cap 50%; claimed within 30 days; applied to the next invoice; sole remedy for availability except the termination right after three consecutive months of breach |
| Support | Response targets by severity: S1 (service down, regulatory deadline today) 15 minutes 24×7 for Enterprise and Regulated Enterprise, 1 hour business hours otherwise; S2 1 hour business hours; S3 1 business day; S4 3 business days; channels in-app, email, phone (Enterprise); Hindi and English |
| Regulatory-deadline protection | During the last 3 working days before a statutory due date recorded in Customer's calendar, planned maintenance is not scheduled, and S1 applies to any defect that prevents a filing-related export **[OWNER]** |
| Maintenance | Scheduled windows announced ≥ 72 h ahead on the status page, outside 09:00–21:00 IST, excluded from downtime up to 4 h/month |
| Exclusions | Customer-caused; third-party services outside our control (payment gateway, eSign providers, regulator portals, company-data providers); force majeure; suspension under the Terms; beta features; Customer's own Microsoft 365 or Google Workspace |
| Reporting | Monthly availability report in Settings › Security & trust and the Vendor Assurance Room (`uptime_report`); incident post-mortems for S1 within 5 business days |

---

## AD.17 Vendor Assurance Statement — LawDocsComply (Template 17 instance)

**Displayed at:** Trust Centre; DPA Annex; RFP responses. The table is rendered from the Vendor Assurance Room mirror (P24 FR-P24-51), never typed.

> # Vendor Assurance Statement — LawDocsComply
> {{entity_name}} publishes the following to customers through the Vendor Assurance Room (Settings › Security & trust › Vendor documents). Each document shows issuer, scope, period and next-review date. We publish only documents we hold; items marked "planned" are not certifications.
>
> | Document | Cadence | Audience |
> |---|---|---|
> | ISO/IEC 27001:2022 certificate and Statement of Applicability summary (when held) | Annual (surveillance), on change | All customers |
> | ISO/IEC 27701, 42001, 22301 certificates (when held) | Annual | All customers |
> | SOC 2 Type II report (or bridge letter) (when held) | Annual; bridge letter quarterly | Under NDA |
> | Penetration test executive summary and closure status | Half-yearly and after major release | All customers |
> | VAPT certificate / attestation (CERT-In empanelled auditor) | Half-yearly | All customers |
> | Vulnerability management and patch statistics | Monthly | All customers |
> | Availability and SLA performance | Monthly | All customers |
> | Business continuity and DR test summary | Quarterly | All customers |
> | Sub-processor list and change log | Continuous; notice 30 days | Public |
> | Data-flow and architecture overview | Annual | Under NDA |
> | DPIA summary | Annual | Under NDA |
> | Insurance certificates (cyber, professional indemnity) | Annual | Login |
> | Board-approved information security, outsourcing, AI and acceptable-use policies (summaries) | Annual | All customers; summaries public |
> | Incorporation documents, PAN, GST, MSME/Udyam | Annual confirmation | Login |
> | Affidavits and undertakings for regulated customers (no sub-contracting without consent, data localisation, non-disclosure, no adverse regulatory action, beneficial ownership) | Annual or ad hoc | Regulated customers |
> | Financial standing summary (for RBI/SEBI/IRDAI due diligence) | Annual | Regulated customers under NDA |
> | Management attestation of control operation | Quarterly | Under NDA |
> | Compliance mapping sheets (RBI outsourcing, RBI IT governance, SEBI CSCRF, IRDAI, DPDP → our controls) | Half-yearly | All customers |
> | Transparency report (grievances, takedowns, law-enforcement requests, AI incidents) | Half-yearly | Public |
> | Accessibility audit report | Per release | Public summary |
> | SBOM / AIBOM for delivered software (CERT-In BOM guidelines v2.0, July 2025 [REC]) | Each release; quarterly snapshot | Under NDA |
> | Exit and transition plan summary; cloud concentration statement | Annual | Under NDA |
> | Completed standard questionnaires (CAIQ, SIG Lite) and regulator-specific questionnaires | Annual / on request within 10 working days | Under NDA |
> | Regulator-ready vendor file for a customer | Quarterly / on demand | That customer |
>
> Regulated customers may request additional documents required by their regulator; we respond within 10 working days. We notify customers of any material adverse change (certification loss, significant incident, change of control) within 5 working days, and of a security incident affecting their data within the contractual window in their Data Processing Agreement.

---

## AD.18 Consent Manager and notice texts — LawDocsComply (Template 18 instance)

Versioned strings in `web.consent_texts` (P23); the consent ledger records key, version and exact text shown (P01). Unticked boxes; one purpose per control; link to the Privacy Notice section; no bundling with Terms acceptance; plain Hindi versions reviewed before publication.

| Key | Text (English) | Notes |
|---|---|---|
| `consent.signup.terms` | "I have read and agree to the Terms of Use and the Payment & Subscription Terms (v{{version_label}})." | Required; acceptance, not consent |
| `consent.signup.privacy_notice` | "I have read the Privacy Notice. My account data will be used to provide LawDocsComply, secure my account and meet legal duties." | Notice acknowledgement |
| `consent.signup.org_authority` | "I am authorised to create this organisation's account and to accept the Data Processing Agreement on its behalf." | Organisation creation |
| `consent.dpa.clickwrap` | "I am authorised to accept the Data Processing Agreement (v{{version_label}}) on behalf of {{org_name}}." | `pol.dpa_clickwrap = true` |
| `consent.marketing.email` | "Send me regulatory updates, product news and offers by email. I can unsubscribe any time." | Optional, unticked |
| `consent.marketing.whatsapp` | "Contact me on WhatsApp at {{phone}} for updates about my enquiry or account. WhatsApp's own terms apply. Reply STOP to opt out." | Optional, unticked; utility vs marketing template category recorded **[VERIFY Meta policy text]** |
| `consent.contact_form` | "We will use your details to respond to your enquiry. See our Privacy Notice (Contact enquiries)." | Notice |
| `consent.hc.start` | "Your answers are used to compute your Health Check Score and are kept for 365 days unless you delete them sooner. We do not pull credit reports or contact your regulator. See the Privacy Notice (Health Check)." | Health Check start; X-07 statement |
| `consent.hc.report_email` | "Email me my Health Check report at {{email}}." plus optional `consent.marketing.email` | Report delivery is a separate, specified purpose |
| `consent.resource_gate` | "We will email you the download link. Your details are used as described in the Privacy Notice (Resources)." plus optional `consent.marketing.email` | — |
| `consent.careers` | "Your application will be processed by {{entity_name}} HR for recruitment and kept for 12 months if unsuccessful. See Privacy Notice (Job applicants)." | — |
| `consent.cookie.banner` | "We use cookies to run this site and, with your consent, to understand usage and measure campaigns. Choose Accept all, Reject all or Manage. You can change your choice any time." | Equal buttons |
| `consent.ai.first_use` | "{{ai_display_name}} is an AI assistant. Outputs may be wrong and are labelled; review before use. It does not certify compliance or file anything. Your content is not used to train models. See the AI Use & Transparency Policy." | Shown once per user; `vidhi.disclosure.first_use_text_key` |
| `consent.ugc.terms` | "I accept the Blog & User-Generated Content Terms (v{{version_label}}) and confirm this post is my own work and not professional advice." | Required for user posts |
| `consent.rights.nominee` | "I nominate {{nominee_name}} to exercise my data rights if I die or cannot act (DPDP Act s.14)." | Settings › Privacy & consents |
| `consent.auditor_grant` | "I grant {{auditor_name}} read access to our Vendor documents and evidence pack until {{expires_at}}. I can revoke this at any time." | Settings › Security & trust (maker-checker) |
| `consent.beta_ring` | "Our organisation joins the beta ring. Beta features are labelled, may change, and we can leave at any time from Settings › Plans & subscription." | P24 FR-P24-56 **[COUNSEL beta terms]** |
| `notice.breach.user` | Subject: "Important: a security incident affecting your LawDocsComply data" — what happened, data involved, when, what we did, what you should do, contact, reference | Rules r.7 intimation **[VERIFY content list]** |
| `notice.breach.regulated_customer` | Subject: "Incident notice under your Data Processing Agreement — reference {{ref}}" — facts known, systems affected, data classes, containment, next update time, our CERT-In reference | Within `trust.incidents.contractual_window_hours` |
| `notice.policy.change` | "We have updated our {{policy_name}} (v{{version_label}}), effective {{effective_date}}. Summary of changes: … Read the full text. {{#if reconsent}}Please review and accept to continue.{{/if}}" | Re-consent notice |

---

## AD.19 Investors page disclaimer (locked copy; P23 FR-P23-216) **[COUNSEL]**

> This page is published for information only. It is not a prospectus, an offer document, an invitation or a solicitation to subscribe to, purchase or deal in any securities of {{entity_name}} or any company in the Infrabyx Group, and it is not an advertisement for any such offer. No securities are offered to the public through this website. Any issue of securities by a private company is made only by private placement to identified persons under the Companies Act 2013 (including s.42) and the rules made under it, and nothing on this page constitutes such an offer. Information here is as at the date shown, is not a forecast and must not be relied on as a basis for any investment decision. Documents made available on request are shared under confidentiality terms with persons the company chooses, at its discretion. Statements about regulation, markets and products are sourced where shown and may change. [LAW: Companies Act 2013 s.23, s.26, s.42; SEBI (Issue of Capital and Disclosure Requirements) Regulations 2018 where applicable] **[COUNSEL to settle wording; owner decision #29]**

---

## AD.20 Publication plan, review and open items

| Step | Action | Owner | When |
|---|---|---|---|
| 1 | Owner approves this appendix for counsel review (decision #28) and supplies entity particulars (decision #10) | Company Secretary | Before P23 legal-pages sprint |
| 2 | Counsel review of [COUNSEL] items: boundary clause, liability cap, ODR/arbitration and Equator disclosure, VDP safe harbour, Investors disclaimer, beta terms, English-prevails clause | Counsel | 2 weeks |
| 3 | Tax adviser confirms SAC codes and GST rate per plan line (OI-IPB-13); OH8 confirms selling entity (D-27) | OH finance | Before pricing page go-live |
| 4 | DPO confirms DPDP Rules 2025 rule numbers and in-force dates (OI-IPB-06); replaces [VERIFY] tags | plt_dpo | Before publication; re-check before 13 May 2027 |
| 5 | Instances created in `Studio › Policies` from this appendix with parameters bound; lint passes; Hindi summaries reviewed; PDFs generated with hash | plt_legal_reviewer | P23 sprint |
| 6 | Maker-checker and DPO approvals; `effective_at` set; footer and placement tests (P23-AT-36) | plt_super_admin, plt_dpo | Go-live |
| 7 | Payment-gateway onboarding checklist (IPB-05 §05.4.20) ticked with evidence links before the gateway application | plt_release_manager | Before first paid plan |

| Open item | Owner | Default |
|---|---|---|
| OI-AD-01 Liability cap formula and consumer carve-outs | Owner / counsel | fees of 12 months |
| OI-AD-02 Pre-dispute ODR mandatory or optional; arbitration for business customers; group-company disclosure | Counsel | ODR optional; arbitration B2B only |
| OI-AD-03 Refund rule per plan; Academy non-refundable position | Owner | full refund within 7 days of first purchase |
| OI-AD-04 Full Hindi text for all policies or summary only | Owner | summary (`pol.full_hindi = false`) |
| OI-AD-05 Regulatory-deadline protection clause in the SLA | Owner | included for Enterprise and Regulated Enterprise |
| OI-AD-06 Mailboxes (support@, privacy@, grievance@, security@, accessibility@) created and monitored | CTO | before publication |
| OI-AD-07 Template 14 adoption if fee-bearing marketplace engagements with escrow are enabled | Owner / counsel | not adopted |
