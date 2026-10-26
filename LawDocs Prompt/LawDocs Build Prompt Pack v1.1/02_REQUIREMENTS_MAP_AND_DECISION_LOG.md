# LAWDOCS — REQUIREMENTS MAP AND DECISION LOG (v1.1, 26 October 2026)

Companion to `01_MASTER_PROMPT.md`. Paste after the master prompt in every session. Precedence: master §18 *(v1.1: master → IPB v1.0 → Ecosystem Spec v1.2 → this log → appendices)*.

> **What changed in v1.1 (26 October 2026).** *(v1.1)* §2.1 adds D-18…D-29 (the twelve IPB decisions IPB-D-01…12 recorded verbatim for LawDocs); §2.2 adds their effects; new §2.4 records IPB deviations `IPB-DEV-01…03`; §4 adds pending owner decisions 21–25 (Investors page publication, blog contributor programme eligibility, image-generation provider and human review, tag manager, which alternative adapters to contract first); §9 adds the v1.1 review row. No v1.0 entry was removed.

---

## 1. Purpose and sources

This file records (a) every decision the owner has taken, (b) every place the pack challenged the brief and what it builds instead, (c) decisions still pending, (d) questions for counsel and tax advisers, (e) assumptions and external dependencies, and (f) the coverage map from every brief requirement (R-001…R-092) to phases and appendices. The atomic traceability (581 rows: 398 owner-brief rows TM-…, 125 ChatGPT-prompt rows TC-…, 58 manual rows MW-…) is Appendix Z.

Sources: the owner's brief of 25 October 2026; the four Word manuals (Documents; Pleadings and Court Drafts; Compliance; Start a Business); the earlier ChatGPT master prompt; the owner's answers in plan mode on 25 October 2026 (four rounds of questions, D-01…D-13); research streams R1–R6 (`_research/`); and the companion packs (Ecosystem Spec v1.1, Operations Hub v1.0, LawDocsComply v1.2, Equator v3.1).

---

## 2. Decisions

### 2.1 Owner decisions taken on 25 October 2026 (plan mode and pack lead)

| ID | Decision |
|---|---|
| D-01 | Ecosystem stack (master §5.1); migrate off Vite/Express/MongoDB/Railway in P00 with redirects. |
| D-02 | Shared group **Operations Hub** (CRM, onboarding factory, support desk, customer success, marketing and brand, social calendar, PR/collaborations, staff HRMS, payroll, leave, appraisal, internal controls, billing OH8) + a **LawDocs Delivery Console** (`apps/delivery`) for client service delivery. LawDocs never re-builds OH functions; Appendix X lists what OH must add. |
| D-03 | Client portal credentials only in the encrypted, client-owned credential vault (NN-16). |
| D-04 | Website copy: content system + page inventory + ~15 flagship pages rewritten now (content deck); P21 rewrites the remaining ~600 pages from the manuals; all copied third-party text is replaced; outdated law references are corrected (R5). |
| D-05 | Marketplace with **per-profession commercial switches**. Lawful defaults (amended after research, R3/R6): advocates — no listing fee, no commission, no paid ranking; buyer pays a separate disclosed LawDocs platform fee; CA/CS — practising-member listing and any % model OFF pending ICAI/ICSI-compliant structure; LawDocs-employed professionals deliver non-reserved services at LawDocs prices; any percentage/subscription switch for regulated professionals is locked until counsel opinion + checker approval (NN-21). |
| D-06 | **Consumer Help** is a separate configurable brand + entity profile on the same platform with an ethical wall (NN-23). Placeholder brand: `[Consumer Help Brand]`. |
| D-07 | Languages: UI and Vidhi in English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, Malayalam, Punjabi at launch; document OCR/translation input supports all 22 Eighth-Schedule languages + the six UN official languages (Arabic, Chinese, English, French, Russian, Spanish), labelled machine translation (NN-48). |
| D-08 | Operating entity is a placeholder `[LawDocs Operating Entity]` (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer configured in Super Admin). |
| D-09 | 24 phases P00–P23 (master §13). |
| D-10 | LawDocs is system of record for legal work (CLM, eSign/eStamp, vault/DMS, litigation, IP, pleadings, notices, legal advisory engagements, consumer help, startup desk, business-service orders). LawDocsComply is system of record for compliance, governance and client HRMS. Common code in shared kernels; a LawDocs-only company mounts Governance and HRMS locally; when the company also uses LDC, LDC is SoR with SSO and no double entry. |
| D-11 | One group **services storefront** at lawdocs.in/marketplace for LawDocs and LawDocsComply services plus FinLegal Academy courses; catalogue, prices, quotes, orders, GST invoices and Razorpay run on OH8; LDC shows the same listings in-app. Browsing needs no login and no subscription. |
| D-12 | eSign/eStamp/KYC through provider-neutral adapters, **aggregator first** (Leegality / Digio / Melento (formerly SignDesk) / Surepass-type), with a second ESP route as required by the eSign API spec [VERIFY v3.3 two-ESP rule — R3]; P00/P08 verify each vendor's ASP/ESP structure; LawDocs may become its own ASP with a direct ESP later without code change. |
| D-13 | Advertising: switch default OFF; public content pages only (NN-35). |
| D-14 | AI provider: Claude (owner supplies API/Bedrock credentials); provider-neutral gateway; Jio and Indic providers as adapters after verification. |
| D-15 | Brand of the AI employee: **Vidhi** (Vidhi AI). |
| D-16 | Academy brand: **FinLegal Academy** at trainings.lawdocs.in (currently on Graphy — R5); integrate by catalogue feed/deep links/SSO where Graphy supports it; never copy paid course content. |
| D-17 | Positioning: "your legal team in an app" is expressed as **legal operations + AI + on-demand professionals** — never as a replacement for advocates (CH-14). |
| D-18 *(v1.1)* | = IPB-D-01 — Node.js **24.22.1** pinned in every product; 26.12.1 only through a dated ADR after dependency verification (not before Q2 2027). Closes the v1.0 "[VERIFY at P00]" on the runtime. |
| D-19 *(v1.1)* | = IPB-D-02 — Ports + reference stack: PostgreSQL the only database engine; every cloud/vendor capability behind a port with ≥ 2 adapters; container-ready; reference production AWS Mumbai with DR Hyderabad; Supabase database-only in non-production. |
| D-20 *(v1.1)* | = IPB-D-03 — One AI employee brand, Vidhi AI, on a shared kernel (`packages/vidhi`) with product skills and autonomy ceilings; display-name override on white-label plans (not on LawDocs core plans in v1). |
| D-21 *(v1.1)* | = IPB-D-04 — Seed credentials: generated 24+ character passwords in `env/SEED_CREDENTIALS.md`; super admin rjnprajapati@gmail.com everywhere; production refuses seeds; first production login forces password change and MFA. |
| D-22 *(v1.1)* | = IPB-D-05 — All products are NestJS modular monoliths (module = schema = bounded context). |
| D-23 *(v1.1)* | = IPB-D-06 — Multi-provider AI with data-class routing; confidential and regulated classes only to India-resident zero-retention endpoints. D-14 continues: Claude is the reference family. |
| D-24 *(v1.1)* | = IPB-D-07 — Payment-gateway neutral; Razorpay reference; hosted checkout only; OH8 is the billing engine of record. |
| D-25 *(v1.1)* | = IPB-D-08 — Every product ships a public website with super-admin CMS, Brand Studio, Pricing Studio, blog, vlog, resources, cookie CMP, standard footer and pages. |
| D-26 *(v1.1)* | = IPB-D-09 — Vendor Assurance Room with cadenced uploads; OH14.6 system of record; product mirrors (LawDocs: Settings › Security & trust › Vendor documents). |
| D-27 *(v1.1)* | = IPB-D-10 — Shared `brand_pack` object for white-label and multi-brand. |
| D-28 *(v1.1)* | = IPB-D-11 — Distinct visual identity per product within WCAG 2.2 AA contrast guard-rails (LawDocs palette and type: `design/UI_UX_Design_Brief_v1.1.md`). |
| D-29 *(v1.1)* | = IPB-D-12 — Operations Hub staff segregated by product scope in addition to legal entity. |

### 2.2 How each decision changed the pack

| Decision | Effect |
|---|---|
| D-01 | P00 migrates the live Vite/Express/MongoDB/Railway site; every phase uses the locked stack (master §5.1). |
| D-02 | No CRM, HR, payroll, appraisal, marketing or billing engine is built in LawDocs; P18 builds the Delivery Console; Appendix X lists what the Operations Hub adds. |
| D-03 | P18 §credential vault and NN-16; feature OFF by default; delegation-first. |
| D-04 | Content deck (15 flagship pages) now; P21 and Appendix N migrate ≈ 626 pages; Appendix E flags copied/outdated content. |
| D-05 | P16, Appendix M: lawful defaults; locked switches; Route split; buyer-side platform fee. |
| D-06 | P15 + Appendix S; separate brand domain, entity profile, cell and ethical wall. |
| D-07 | P05, P09, P21, P22 language plans; NN-48. |
| D-08 | Every policy, invoice and footer uses `[LawDocs Operating Entity]` placeholders configured in Super Admin. |
| D-09 | 24 phases. |
| D-10 | P13 mounts shared kernels; `int.eco.ldc.sor_mode.*`; X-06 for legal matters. |
| D-11 | P16 storefront serves LawDocs and LDC listings; OH8 catalogue. |
| D-12 | P08 adapters; `asp_mode` per vendor; second-ESP route; licence-expiry monitoring. |
| D-13 | P17 stream registry; NN-35. |
| D-14–D-17 | P09 gateway; Vidhi brand; Academy integration; positioning copy in the content deck. |
| D-18 *(v1.1)* | Master §5.1 runtime row; `.nvmrc`, Dockerfiles, CI matrix; `env/.env.example` header; P00 plan verifies dependency matrix (IPB-01 §01.4.1.3). |
| D-19 *(v1.1)* | Master §21.1 port table; P19 FR-P19-66 extended; P20 §4H portability drills (FR-P20-52…55; renumbered 26 Oct 2026 — 44…47 were already the v1.0 exit/closure/retention/handover requirements); Appendix I §I.2 adapter status gains an "alternative adapter" column. |
| D-20 *(v1.1)* | P09 §4N kernel mapping (FR-P09-64…70); Appendix H §H.15; settings `vidhi.*` in Appendix R §R.9.16A. |
| D-21 *(v1.1)* | `env/SEED_CREDENTIALS.md`, `env/README.md`; P00 seed framework; P23 FR-P23-07 production guard-rail. |
| D-22 *(v1.1)* | No change — already master §5.3. |
| D-23 *(v1.1)* | P09 FR-P09-01 adapter list and FR-P09-02 routing bands; `ai.routing.*` keys. |
| D-24 *(v1.1)* | No change — already NN-22 and P17. |
| D-25 *(v1.1)* | P21 §4R (standard pages, Investors toggle, Resources library), §4I blog toggle and user posts, FR-P21-16 footer social and offices, `brand.app_name`; content deck v1.1. |
| D-26 *(v1.1)* | P23 §4I FR-P23-60…62; P21 FR-P21-150 (Trust Centre from the room); Appendix O POL-LD-21. |
| D-27 *(v1.1)* | P21 FR-P21-05 multi-brand becomes `brand_pack`-based; P03 FR-P03-31A. |
| D-28 *(v1.1)* | Appendix C §C.9 tokens re-stated in the design brief; contrast guard-rails unchanged. |
| D-29 *(v1.1)* | P18/P19 OH calls carry `product_scope = LD` (Appendix X §X.1 note). |

### 2.3 Amendments after research (pack lead; owner may reverse)

| ID | Amendment | Why |
|---|---|---|
| D-05A | Advocates pay no fee of any kind (listing, subscription, commission, lead or ranking); buyer-side platform fee only | BCI Rules 36/37/20; Madras HC 3 Jul 2024 (R1, R3 LG-110–LG-113); R4's flat listing-fee idea rejected (X-03) |
| D-05B | Practising CA/CS listings and any percentage model locked OFF until an ICAI/ICSI-compliant structure and counsel opinion exist | ICAI 23 Oct 2019 aggregator restrictions (R3 LG-114–LG-117) |
| D-12A | eSign capability is never offered to other group products as a provider; hosted hand-off instead | CCA ASP no-sublet rule (R3); X-05 |
| D-12B | ESPs with lapsed or expiring CCA licences are blocked without renewal evidence | R3 found Capricorn lapsed (15 May 2026) and Protean expiring (26 Oct 2026) [VERIFY]; X-16 |
| D-07A | Six UN official languages are for reading/translation input only; court filings use certified translations | CH-11; NN-48 |
| D-11A | Consumer billing data sent to OH8 is limited to billing fields under legal basis `CONTRACT_PERFORMANCE_CUSTOMER` | Ecosystem Spec principle 12; X-13 |

---

### 2.4 IPB deviations (`IPB-DEV-nn`) *(v1.1)*

A deviation is any place where LawDocs differs from the IPB other than by being stricter. Each has a reason and an owner; the IPB owner may fold it back into the standard.

| ID | IPB rule | LawDocs position | Reason | Owner |
|---|---|---|---|---|
| IPB-DEV-01 | IPB-01 §01.7 and IPB-10 §10.7: "LD's eSign becomes the reference ESIGN adapter for every other product" | LawDocs publishes `packages/connectors/esign/lawdocs` as a **hosted hand-off** adapter: other products redirect the signer to a LawDocs-hosted ceremony inside a LawDocs customer relationship and receive status and evidence; they never call eSign as a sublet capability | CCA ASP no-sublet rule; NN-06; D-12A; X-05 [COUNSEL] | LD product lead + `PLT_SECURITY_OFFICER` |
| IPB-DEV-02 | IPB-11 §11.4.5 seed persona role codes (`ORG_MAKER`, `ORG_MEMBER`, `test.advocate`, `test.client`, `test.party`) | LawDocs keeps its binding role codes (Appendix D): `ORG_LEGAL_MAKER`, `ORG_CHECKER`, `IND_OWNER`, `PRO_ADVOCATE`, `CP_GUEST`, `PLT_CONTENT_EDITOR`; `env/SEED_CREDENTIALS.md` maps each IPB persona to the LawDocs role and keeps the lead-supplied persona set | Role codes are referenced by 580+ acceptance scenarios and Cerbos policies; renaming would break traceability | LD architecture lead |
| IPB-DEV-03 | IPB-02 §02.4.3 data classes PUBLIC / INTERNAL / CONFIDENTIAL / REGULATED / SECRET | LawDocs keeps PUBLIC / INTERNAL / PERSONAL / CONFIDENTIAL / SENSITIVE (P09 FR-P09-02) with a fixed mapping for ports and routing: PERSONAL → CONFIDENTIAL; SENSITIVE → REGULATED; credential-vault and signing keys → SECRET | Five-class model is wired into routing, RLS policies and Appendix B; mapping is lossless for residency decisions | `PLT_DPO` + AI lead |

## 3. Challenges to the brief (R-001)

Each row states the owner's wish, why it cannot be built as asked, and what the pack builds instead. Rule references are to Appendix G.

| CH | Brief's wish | Conflict | What the pack builds instead |
|---|---|---|---|
| CH-01 | Individuals "login through Aadhaar" | Aadhaar Act s.4(4): authentication only where Parliamentary law or a prescribed purpose allows; s.57 private-entity use omitted (2019 Amendment Act, after *Puttaswamy* 2018); Aadhaar must be voluntary with alternatives (LG-021–LG-025) | Login by mobile/email OTP, passkey, password + MFA or SSO (NN-03); Aadhaar used only for offline verification as an OVSE [VERIFY] and for ESP eSign (P01, P08) |
| CH-02 | Aadhaar APIs "automatically fetch the details" | LawDocs is not an AUA/KUA; an OVSE may not store the number (s.8A(4)); s.29(4) masking | Aadhaar App credential/QR verification; store only needed signed attributes + last 4 digits; auto-masking in uploads (NN-04, X-14) |
| CH-03 | CKYC-based APIs | CKYCR is for PMLA reporting entities (LG-046) | DigiLocker and Entity Locker with consent; no reuse of a sister RE's CKYC result |
| CH-04 | PAN APIs | Direct PAN verification is limited to enumerated entities (LG-047) | DigiLocker PAN + name match; licensed vendor only with a lawful-upstream warranty |
| CH-05 | CIBIL APIs at registration | CICRA s.17(4) and s.22 (offence); specified users only (LG-056–LG-060) | No bureau pull; users upload their own reports; credit-report dispute drafting in Consumer Help |
| CH-06 | Company-registration APIs | No open MCA API; scraping breaches terms | Licensed MCA-data vendors (Probe42/Signzy/Surepass/Perfios-Karza) or user-initiated lookup; Entity Locker (P01, P19) |
| CH-07 | Password tracker where client and LawDocs staff view and change portal passwords (CERSAI, MCA, CIBIL, Experian, GST, RBI CIMS, Daksh, Pravaah…) | Credentials and DSCs are issued to named officers; sharing defeats attribution required by RBI cyber/outsourcing directions, SOC 2 and ISO 27001; IT Act s.66C/s.72A exposure; acting inside a regulator portal as a client officer is impersonation | Delegation first (practitioner roles, separate named users where portals allow); otherwise a client-owned, envelope-encrypted vault with masked entries, just-in-time reveal with reason + client approval, time-boxing, tamper-evident logs, no OTP/DSC PIN storage; OFF by default (D-03, NN-16, P18) |
| CH-08 | Advocates on subscription or percentage basis; ratings and testimonials | BCI Rules 36, 37, 20 and the fee-sharing bar; Madras HC 2024 (SC pending, no stay) | Fixed-price services fulfilled by assigned professionals; Rule-36-only directory OFF until counsel opinion; buyer-side platform fee; no ratings/testimonials about advocates (D-05A, NN-21) |
| CH-09 | CAs and CSs on subscription or percentage basis | CA Act Schedule I; ICAI 2019 aggregator restrictions; CS Act analogues | LawDocs-employed professionals deliver non-attest services; attest work by independent practitioners engaged directly; switches locked (D-05B) |
| CH-10 | LawDocs team files returns using client passwords | Returns must be verified by the taxpayer; credential sharing defeats verification (LG-125/126) | ERI route with client consent and taxpayer EVC/DSC; GST practitioner roles; TDS by deductor or ERI (P14) |
| CH-11 | Identify and read "UN-approved languages" and all main Indian languages; attach AI translations to petitions | The UN has six official languages; courts need court-language filings and certified translations | D-07 phased languages; UN languages for reading only; labelled machine translation; certified-translation hand-off (NN-48, P05) |
| CH-12 | eSign for all personal, business and property contracts | IT Act First Schedule still excludes wills, trusts, ordinary POAs and most negotiable instruments; sale deeds and long leases need registration; affidavits need oath | Instrument eligibility gate with wet-ink, notary and registration packs (NN-07, NN-40, Appendix F) |
| CH-13 | "Buy stamp papers online" through an eStamp API | Only the CRA, ACCs and licensed vendors issue; coverage differs by State | Agent procurement via a contracted ACC/aggregator; duty passed through at actuals; State coverage registry; stamp-before-sign; UIN checks (NN-08) |
| CH-14 | "The tool shall be sufficient instead of a legal team" | Only advocates practise law and appear in court; a company cannot (LG-110) | Legal-operations platform run by a CLO with Vidhi agents and engaged advocates; party-in-person tools for individuals (D-17, NN-41) |
| CH-15 | Vault "like DigiLocker", kept forever | LawDocs is not a DigiLocker service provider; requester terms bar storage beyond purpose (LG-036–LG-041) | "Legal Vault": DigiLocker URI + verification; copy retained only for a recorded permitted purpose; user uploads stored with hashes (NN-42) |
| CH-16 | Data freely shareable across ecosystem apps | DPDP purpose limitation and consent; DigiLocker terms; eSign no-sublet; CICRA | Purpose-bound, consented, ledgered sharing through registered contracts (NN-24, Appendix Y) |
| CH-17 | Jio automated and AI calling | TCCCPR/DLT, consent, pre-declared numbers (2026 amendment), AI-voice labelling | DLT-registered telemarketer route, consent, calling windows, disclosure and human hand-off (NN-34, Appendix J) |
| CH-18 | "In consonance with GDPR, CCPA" | Apply only when their territorial triggers are met | DPDP-first design with GDPR-grade controls; jurisdiction flags switch on supplements (Appendix O, P) |
| CH-19 | PCI-DSS "certification" | Hosted-checkout merchants self-assess (SAQ A) | Hosted/tokenised Razorpay checkout; SAQ A attestation; copy says "LawDocs never stores card data" (NN-22) |
| CH-20 | Testimonials on every page | BCI Rule 36 for advocates; fake-review rules (IS 19000, E-Commerce Rules) | Genuine, consented, verified-purchase testimonials about LawDocs' own services only, without photos (NN-49) |
| CH-21 | Advertisements as a revenue stream | Advocate advertising barred; targeted ads raise DPDP issues; confidential areas | Switch OFF by default; contextual, labelled ads on public content pages only (NN-35) |
| CH-22 | Check, pay and contest challans; FREED-like loan and insurance grievance resolution | Collecting money for others is payment aggregation; no lawful third-party e-challan API; ombudsman representation rules; no outcome guarantees | Deep links to official portals for lookup and payment; contest via Virtual Courts/Lok Adalat or an engaged advocate; drafting and tracking while the user files; no money handled (NN-23, P15) |
| CH-23 | Sell vehicles through LawDocs | RC transfer happens on Vahan | Sale agreement + delivery note + pre-sale checks + Vahan checklist (P15) |
| CH-24 | "Employees cannot cheat"; login/logoff tracking | DPDP proportionality; productivity is not presence | Maker-checker, segregation, immutable logs, outcome and SLA metrics; sessions recorded for attendance only (NN-33; OH) |
| CH-25 | Marketplace and duty payments through LawDocs; saved cards | RBI PA Directions, card-on-file tokenisation, e-mandate rules | Route split settlement; tokens; e-mandates with pre-debit notices (NN-22) |
| CH-26 | Super Admin changes crucial client details | DPDP accuracy; evidence integrity; processor role | Master-data change requests with maker-checker, client approval, reason codes and client notification (P18) |
| CH-27 | Trademark and Provakil-like case tracking via APIs | No open eCourts/IP India APIs for LawDocs; scraping breaches terms | Licensed partners, user-entered numbers, assisted/manual refresh, staleness labels (P11, P12, NN-05) |
| CH-28 | AI reads WhatsApp screenshots and handwriting and attaches them to petitions | Screenshots are secondary evidence; s.63(4) certificate with hash needed | Native chat exports preferred; originals immutable and hashed at upload; labelled, correctable type copies; s.63 Part A/Part B workflow (NN-09, NN-10, P05) |
| CH-29 | "Microsoft 365 Business Starter" | "Business Starter" is a Google Workspace edition name; Microsoft's plans are Business Basic, Standard and Premium | Suite-neutral `WORKSPACE_PORT`; owner to confirm the actual plan [OWNER] |
| CH-30 | Free AI drafting of agreements on every page for individuals | Anthropic Usage Policy treats legal document preparation for individuals as high-risk: qualified human review before delivery and AI disclosure [VERIFY] | Free **template automation** from vetted templates; AI-customised drafts labelled "AI draft — not reviewed" with one-click paid professional review (NN-14, P06) |
| CH-31 | Success fees in grievance and claim help | Advocates cannot take contingent fees (BCI Rule 20) | Flat fees by default; success fee only in the non-advocate Consumer Help entity, capped, OFF by default [COUNSEL] |
| CH-32 | Login and logoff time as the measure of productivity | Presence is a poor and intrusive proxy | Attendance from declared sessions; productivity from outcomes and SLAs; no covert monitoring (NN-33) |

---

## 4. Owner decisions pending (needed before the phase named)

| # | Decision | Blocks |
|---|---|---|
| 1 | Confirm the Microsoft 365 plan actually held (CH-29) and the timing of any Google Workspace move | P18, P19 |
| 2 | Operating entity particulars: name, CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer (D-08) | P17, P21, Appendix O |
| 3 | Consumer Help brand name, domain and operating entity; separate cell cost (X-17) | P15, P21, P22 |
| 4 | Plan names and prices, monthly premium, trial length, refund window, credit validity, downgrade storage policy (Appendix L seeds) | P17, P21 |
| 5 | Revenue-stream waves; kill-switch approvers; second pricing approver | P17 |
| 6 | eSign/eStamp/KYC vendors (primary and second ESP) and the long-term own-ASP decision (D-12) | P01, P08 |
| 7 | Court-data vendors (two) and TM data partner | P11, P12 |
| 8 | Approve Appendix E starter lists for categories D5, D6, D7, D14, D15, D18 and the commissioned pleadings (Appendix E §4.3) | P06, P10 |
| 9 | Blog folder taxonomy from the owner's Word files; first 20 tutorial videos | P21 |
| 10 | AI-crawler policy for the public site (allow, allow-list, block) | P21 |
| 11 | Default AI autonomy ceilings per plan and human sponsors for agents at L2+ | P09 |
| 12 | Whether one itemised confirmation of a bounded reminder/nudge series satisfies NN-13 (X-04) [COUNSEL] | P03, P09 |
| 13 | SoR when a tenant uses both LawDocs and LDC for legal matters and contracts (X-06) | P11, P13, P19 |
| 14 | ~~Environment names~~ — resolved at review: `dev`, `test`, `staging`, `pre-prod`, `prod` (P23 governs) | — |
| 15 | Public phone number and support hours; support SLAs by plan | P18, P21 |
| 16 | In-app purchase mode on iOS/Android and GST on store sales [TAX MEMO] | P22 |
| 17 | ERI registration route for income-tax filing support; GSP partner | P14 |
| 18 | Professional panel structure for the marketplace (employed, empanelled, direct engagement) | P16 |
| 19 | Remove unevidenced claims from the live site and manuals now (blockchain, home delivery, "produced before any Court", "verified") | P00, P21 |
| 20 | One credential vault per client when the client also uses LDC (OI-X-05); grievance ownership across group products (OI-X-07) | P18 |
| 21 *(v1.1)* | **Investors page**: publish for LawDocs at all; which documents are gated (`login` vs `email_gate` with NDA flag); IR contact; wording of the locked disclaimer [COUNSEL on Companies Act 2013 private-placement (s.42) and SEBI advertisement restrictions — no solicitation of investment on a public page] | P21 §4R (`web.investors.enabled`, default OFF) |
| 22 *(v1.1)* | **Blog contributor programme**: open user-authored posts to verified customers and professionals (`web.blog.user_posts.eligible_roles`), minimum account age, daily limits, advocate authors restricted to Rule 36 fields; moderation staffing | P21 FR-P21-82A/B |
| 23 *(v1.1)* | **Image generation**: provider for marketing/CMS images (Bedrock image models vs Vertex Imagen vs none) and confirmation that human review before publishing any AI-generated image is mandatory (pack default: yes, locked) | P09 FR-P09-71, P21 FR-P21-80A |
| 24 *(v1.1)* | **Tag management**: `none` (default) vs server-side GTM vs web GTM for `apps/public`; `PLT_DPO` veto | P21 FR-P21-108A (`mkt.tag_manager.adapter`) |
| 25 *(v1.1)* | **Alternative adapters to contract first** (one alternative per Tier-0 port must be live in CI): second ESP, second CPaaS, second storage target, second LLM provider for the `in_zero` band | P00, P19 (IPB-01 §01.3.C) |

---

## 5. Questions for counsel and tax advisers

The full list is in Appendix W §W.5 (52 counsel questions, CQ-01…CQ-52) and §W.6 (17 tax-memo points). The most material:

1. Marketplace structure under BCI Rule 36 after the Madras HC 2024 judgment: assigned-professional model, buyer-side platform fee, Rule-36 directory content (NN-21).
2. ICAI/ICSI-compliant structures for CA/CS participation (D-05B).
3. Consumer Help entity: authority letters, representation before RB-IOS 2026 and the Insurance Ombudsman, success-fee legality and caps (CH-31).
4. First Schedule eligibility of agreements for sale after 26 Sep 2022; electronic attestation and witnesses (Appendix F).
5. Hosted eSign hand-off for other group products under the CCA ASP rules (X-05).
6. Aadhaar offline verification as an OVSE and masked-only storage (CH-01, CH-02, X-14).
7. DigiLocker retained copies (NeGD position) (NN-42).
8. DPDP roles: LawDocs as fiduciary or processor for company workspaces; group data sharing (CH-16).
9. Review gate wording for AI drafts and who may review (NN-14, CH-30).
10. Migration of users from the legacy contracting entity: fresh consent or notice (CQ-01).
11. [TAX MEMO] GST on credits and platform fees; RCM on advocates' services; e-commerce TCS/TDS; pure-agent treatment of stamp duty and government fees; Income-tax Act 2025 section mapping.

---

## 6. Assumptions

| # | Assumption | If wrong |
|---|---|---|
| A-1 | The owner supplies Claude credentials (Bedrock India and Anthropic API) | Gateway runs with another approved provider; AI features flagged |
| A-2 | At least one aggregator with ASP status and two ESP routes can be contracted before Wave 1 GA | eSign ships with DSC and wet-ink packs only |
| A-3 | The Operations Hub (OH8 billing, CRM, OH10) is available for Wave 1; otherwise a minimal billing adapter runs behind `BILLING_PORT` and migrates later | P17 builds a temporary adapter (flagged) |
| A-4 | The Consumer Help entity is incorporated before Wave 3 | P15 stays OFF |
| A-5 | Live-site users and orders can be migrated under notice (CQ-01) | Re-consent flow in P00 |
| A-6 | Graphy supports catalogue export and deep links for FinLegal Academy | Manual catalogue sync |

---

## 7. External dependencies

Vendor contracts (Appendix W §W.7, 32 items): AWS (and Bedrock), Anthropic, eSign aggregator(s) and second ESP, eStamp ACC/aggregator, DigiLocker requester onboarding, Aadhaar offline-verification route, MCA-data vendor(s), GSP, licensed court-data aggregators (two), TM data partner, JioCX and other CPaaS (DLT), WhatsApp BSP, Razorpay (via OH8), Microsoft Graph and Google Workspace app registrations, Brevo, translation and speech providers, VAPT auditor (CERT-In empanelled), SOC 2/ISO auditors, app-store developer accounts.

---

## 8. Requirements coverage map

Status counts from Appendix Z (after the traceability-review edits): owner brief 340 covered, 57 changed by decision, 1 partial (TM-296 Jio developer-page reading, OI-R4-01), 0 missing; ChatGPT prompt 121 covered, 4 changed by decision; manuals 49 covered, 9 partial (owner approvals in §4 item 8).

| R | Requirement | Phases | Appendices | Rows by status (Appendix Z) |
|---|---|---|---|---|
| R-001 | working agreement (challenge, don't auto-agree) | P00, P23 | — | COVERED 13; PARTIAL 1 |
| R-002 | ecosystem integration boundaries (Finbyx, Udofin, Equator, LDC, third parties) | P00, P10, P11, P13, P18, P19 | Y | COVERED 12 |
| R-003 | APIs/gateways for data transfer and easy onboarding of new companies | P00, P01, P19 | — | COVERED 5 |
| R-004 | use owner's Word files + deep research; Word/.md/phase files | P00, P21, P23 | — | COVERED 7; PARTIAL 2 |
| R-005 | individuals and companies; easy onboarding via Aadhaar/PAN/CKYC/DigiLocker/MCA/CIBIL APIs | P01, P02, P04, P05, P15, P22 | — | COVERED 8; CHANGED-BY-DECISION 5 |
| R-006 | business agreements + Aadhaar eSign | P06, P07, P08, P19 | — | COVERED 7 |
| R-007 | AI employee drafting (Vidhi) | P06, P08, P09 | — | COVERED 3 |
| R-008 | multi-language | P00, P06, P09, P21, P22 | — | COVERED 2 |
| R-009 | individual "Aadhaar login" and AI agreements | P01, P06 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-010 | Vidhi answers user problems | P09 | — | COVERED 2 |
| R-011 | DigiLocker-like always-kept app: prepare, enter, eSign, amend, preserve; DMS | P04, P06, P07, P08, P11, P17, P20 | — | CHANGED-BY-DECISION 1; COVERED 7 |
| R-012 | litigation tracking for companies | P11, P12 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-013 | trademark application tracking | P12 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-014 | marketplace of advocates, tax assistants, CA, CS | P01, P06, P14, P16 | — | COVERED 5 |
| R-015 | Claude API for Vidhi | P09, P23 | — | COVERED 3 |
| R-016 | explore LegalKart and similar; parity | P09, P16 | — | COVERED 2 |
| R-017 | web app mobile-friendly; iOS/Android apps | P00, P02, P19, P21, P22 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-018 | agentic AI for users, KMPs, boards; agents as employees | P03, P05, P07, P09, P11, P13, P23 | — | COVERED 9 |
| R-019 | "i" buttons/glossary | P00, P03, P09, P21 | — | COVERED 4 |
| R-020 | tutorials (text, images, diagrams, screenshots, videos) reusable on social | P21 | — | COVERED 6 |
| R-021 | data preservation/export/migration in standard folders and formats; BYO storage (servers, buckets, OneDrive, drives, data centre) | P04, P20, P22 | — | COVERED 16 |
| R-022 | structure preserved across code/infra changes; no manual migration | P00, P04, P18, P20, P23 | — | COVERED 11 |
| R-023 | data shareable across ecosystem apps both ways | P04, P19, P20 | — | CHANGED-BY-DECISION 2; COVERED 1 |
| R-024 | bulk intake via folder structure | P04, P11, P12, P20 | — | COVERED 3 |
| R-025 | accessibility for hearing/visually impaired, all types | P01, P21, P22, P23 | — | COVERED 4 |
| R-026 | faster cross-team/department workflows; better logic | P02, P03, P11, P12, P13, P16, P18, P21 | — | COVERED 4 |
| R-027 | extensive customisation in settings | P03 | — | COVERED 1 |
| R-028 | user types: super admin, operations hub, company admin, maker/checker etc., individuals — distinct features per type | P02, P03, P18 | — | COVERED 8 |
| R-029 | Jio AI services (agentic AI, agent calling, automated calling, marketing, research, drafting) | P03, P06, P09 | — | COVERED 3; CHANGED-BY-DECISION 5 |
| R-030 | detailed customisable content/features/UI; fewer clicks; automation | P03, P09, P11, P13, P17, P22 | — | COVERED 3 |
| R-031 | GDPR/CCPA/DPDP/IT Act/privacy compliance | P00, P01, P18, P19, P20, P21, P23 | — | CHANGED-BY-DECISION 2; COVERED 6 |
| R-032 | SEO/GEO/AI-search content; clean minimalist UI | P00, P21 | — | COVERED 7 |
| R-033 | certification readiness (PCI DSS, SOC 2 Type 1/2, ISO) | P17, P23 | — | CHANGED-BY-DECISION 1; COVERED 7 |
| R-034 | payment-gateway security; Razorpay | P16, P17, P19 | — | COVERED 3 |
| R-035 | billing/subscription in settings; plan up/downgrade | P17 | — | COVERED 3 |
| R-036 | subscription/business model and revenue streams per company type; 3-plan pricing page with feature list | P01, P17, P21 | — | COVERED 9 |
| R-037 | LawDocs services (returns, one-time, retainer) on marketplace; third-party professionals on subscription/% | P09, P14, P16, P17 | — | COVERED 9; CHANGED-BY-DECISION 3 |
| R-038 | service types (agreements, policies, annual reports, stress testing, compliance testing, risk assessment, retainer advisory, minutes) | P13, P16 | — | COVERED 10 |
| R-039 | custom solutions/pricing; customised retainers with eSigned SLAs | P16 | — | COVERED 4 |
| R-040 | services purchasable without SaaS subscription; billing, invoices, GST, emailed invoices, Razorpay | P16, P17, P18 | — | COVERED 8 |
| R-041 | FinLegal Academy courses on marketplace; marketplace open without login; categorised | P16, P21 | — | COVERED 5 |
| R-042 | recurring revenue architecture; explain plan benefits; detailed billing/membership settings | P17 | — | COVERED 4 |
| R-043 | advanced DMS (share, eSign, search, filter, selective sharing) | P04, P07, P08, P20 | — | COVERED 6 |
| R-044 | AI type copy of handwritten docs/WhatsApp screenshots attached to petitions; editable | P05, P10, P22 | — | COVERED 5 |
| R-045 | translation to English; UN + Indian languages | P05, P21 | — | COVERED 4 |
| R-046 | revise and fix errors | P00, P03, P14, P21 | Z | COVERED 2 |
| R-047 | customisable open/interim/waiting items; dynamic rule/content engine; settings for every user; no super admin for small changes | P03, P11, P13, P14, P19, P23 | — | COVERED 9 |
| R-048 | operations dashboard separate from super admin (delivery, after-sales, marketing, CS, social, PR, collaborations) | P18, P21 | — | COVERED 8; CHANGED-BY-DECISION 3 |
| R-049 | explore revenue/business model again | P16 | — | COVERED 2 |
| R-050 | own CRM integrated (ops, marketing, after-sales, CS, onboarding, grievances, tickets); open to Brevo migration/integration | P01, P03, P16, P18, P19, P21 | — | COVERED 8 |
| R-051 | performance appraisal; employee lifecycle; email IDs; decentralised decisions; anti-fraud maker-checker | P02, P18 | — | CHANGED-BY-DECISION 4; COVERED 5 |
| R-052 | leave, salary, payroll per Indian labour law; WFH; pan-India hiring; login/logoff; work measurement | P13, P18 | — | CHANGED-BY-DECISION 3; COVERED 7 |
| R-053 | M365 now (Teams, SharePoint), Google Workspace later; smooth migration for ops and clients; Office-openable files; self-explanatory folders | P03, P04, P18, P19, P20 | — | CHANGED-BY-DECISION 1; COVERED 8 |
| R-054 | switchable revenue streams (one-time, subscription, rental, PAYG, ads…) | P16, P17, P21 | — | COVERED 10; CHANGED-BY-DECISION 1 |
| R-055 | clients on M365 or Google Workspace; workflows for both | P04, P07, P18 | — | COVERED 1 |
| R-056 | business on autopilot (VSL-funnel style); marketing architecture (Brevo, Adobe Express, social calendar, employee reporting) | P21 | — | COVERED 5; CHANGED-BY-DECISION 3 |
| R-057 | patch/change management, GitHub branches, backups, VAPT, IS/internal/external audit | P00, P02, P23 | — | COVERED 9 |
| R-058 | cross-functional group roles; shared ops data across group companies | P02, P18, P19 | — | COVERED 5; CHANGED-BY-DECISION 2 |
| R-059 | client-company HRMS: KMPs, directors, duties, departments; finance-company departmental structure; Companies Act 2013 governance aligned with RBI MDs; task assignment | P02, P03, P11, P13 | — | COVERED 10; CHANGED-BY-DECISION 1 |
| R-060 | tool sufficient instead of legal team; one CLO | P06, P07, P09, P10, P13 | — | CHANGED-BY-DECISION 2; COVERED 1 |
| R-061 | individuals: DigiLocker-like; litigant self-help end to end | P04, P10, P11, P16 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-062 | Jio services for customers and ops (research, automated calling, customer service) | P09, P10, P19 | — | COVERED 4; CHANGED-BY-DECISION 1; PARTIAL 1 |
| R-063 | savings page (money, hours, penalties) with quantification | P07, P14, P15, P17 | — | COVERED 6 |
| R-064 | RM as maker for retainer clients; client checker; multiple makers; both sides can create makers | P02, P13, P16, P18, P19 | — | COVERED 7; CHANGED-BY-DECISION 2 |
| R-065 | ops-hub client section: password tracker, billing/invoices feeding client billing, data sharing, messaging, common drive links | P18 | — | COVERED 9; CHANGED-BY-DECISION 3 |
| R-066 | super admin changes crucial client details; transparent fast workflow | P02, P18 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-067 | audit trail | P00, P05, P08, P20 | — | COVERED 3 |
| R-068 | user download of documents and data | P04, P20, P22 | — | COVERED 2 |
| R-069 | taxation for individuals, companies, LLPs | P14 | — | COVERED 4 |
| R-070 | study lawdocs.in public pages; reuse; write missing copy | P00, P10, P21 | — | COVERED 6 |
| R-071 | frontend + backend + frontend content | P00 | — | COVERED 3 |
| R-072 | privacy policy, terms, other policies integrated | P03, P21 | — | COVERED 6 |
| R-073 | blog section from owner's categorised Word files | P21 | — | COVERED 2 |
| R-074 | vlog section with YouTube videos | P21 | — | COVERED 2 |
| R-075 | add services similar products offer | P16 | — | COVERED 1 |
| R-076 | Provakil-like multi-case management | P11 | — | COVERED 1 |
| R-077 | parties message while signing; track-changes review; eSign; records/audit | P07, P08 | — | COVERED 7 |
| R-078 | eStamp API: buy online or attach stamp paper, then eSign | P08 | — | CHANGED-BY-DECISION 2; COVERED 2 |
| R-079 | court pleadings drafting | P10 | — | COVERED 2 |
| R-080 | legal advisory retainer + one-time business model | P14, P16 | — | COVERED 3 |
| R-081 | FinLegal Academy integration | P16 | — | COVERED 3 |
| R-082 | startup section (registration, advisory, legal officer, TM, funding docs) | P12, P14, P21 | — | COVERED 6 |
| R-083 | loan/lending/insurance grievance help (FREED/ClaimBuddy/Insurance Samadhan); separate entities; status tracking | P00, P11, P14, P15, P18, P22 | — | COVERED 13; CHANGED-BY-DECISION 1 |
| R-084 | challans check/pay/contest; hire advocate (ChallanPay-type) | P15 | — | CHANGED-BY-DECISION 2; COVERED 3 |
| R-085 | vehicle sale agreements; vehicle loans/challans | P15 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-086 | reverse-engineer LegalKart, OnlineLegal, Vakilsearch | P09, P14, P16, P21 | — | COVERED 4 |
| R-087 | per-page "Draft with AI free" + "Hire a professional" blocks | P06, P21 | — | COVERED 2; CHANGED-BY-DECISION 1 |
| R-088 | testimonials without photos | P21 | — | COVERED 2 |
| R-089 | team uploads blogs without developers | P21 | — | COVERED 1 |
| R-090 | improve Word-file content; one-liners; FAQs for search | P14, P21 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-091 | consider the ChatGPT prompt | P00, P23 | Z | COVERED 1; CHANGED-BY-DECISION 1 |
| R-092 | ask questions in plan mode (done 25 Oct 2026) | P00, P23 | — | COVERED 1; CHANGED-BY-DECISION 1; PARTIAL 1 |

---

## 9. Review log (v1.0)

| Date | Step | Result |
|---|---|---|
| 25 Oct 2026 | Plan mode: four rounds of owner questions | D-01…D-13 |
| 25 Oct 2026 | Research streams R1–R6 (live web, first-party first) | ~71k words; LG register, IMP backlog, page inventory, pricing and data sources |
| 25 Oct 2026 | Authoring: 24 phases, 26 appendices, content deck | ~600k words |
| 25 Oct 2026 | Integration review: cross-file resolutions X-01…X-30; ID/error collisions fixed (Appendix B §B.7); state machines reconciled (Appendix A, 21 notes); 515 screens catalogued; 582 phase scenarios; NN coverage complete | `_review/` logs |
| 25 Oct 2026 | Traceability: 581 rows; 3 FRs added (FR-P15-70, FR-P19-84, FR-P23-58) | Appendix Z |
| 26 Oct 2026 *(v1.1)* | IPB v1.0 adoption (group upgrade): master §5/§10/§11/§18/§20/§21, this log §2.1–§2.4 and §4, phases P03/P09/P19/P20/P21/P23, appendices C/H/O/R/W/X/Y, new `env/`, `design/`, content deck v1.1, condensed addendum; adversarial self-review in `_review/v1.1_upgrade_review_log.md` | `_review/v1.1_upgrade_review_log.md` |
| 25 Oct 2026 | Second error review (owner instruction "review, look for the errors and fix them"): G1 legal (P01, P04, P05, P08, P10–P12; 37 fixes), G2 legal/commercial (P13–P18; 29), G3 architecture/logic (P00, P02, P03, P06, P07, P09, P19–P23; 91), G4 registries (A, B, C, D, K, R, V, W, Z; 24); lead fixes to master, 02, README, G, K, L, R, W, X and content (trade-mark reply period restored to "one month" per r.33(4); `WORKSPACE_PORT` unified; master §6.2 aligned to Appendix A; P09 L0–L2 slice added to Wave 2; conventions file committed to `docs/reference/`) | `_review/G1…G4_log.md`, `_review/LEAD_second_review_log.md` |
