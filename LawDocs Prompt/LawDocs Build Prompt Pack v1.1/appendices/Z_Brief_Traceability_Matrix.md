# Appendix Z — Brief Traceability Matrix

**Status:** Binding (traceability record). **Used by:** pack lead (assembly of `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` §8), every phase owner (P00–P23), `PLT_RELEASE_MANAGER` at each wave go-live (P23 FR-P23-52), the owner at each phase gate.

**How to use.** This appendix proves that every ask in the owner's brief of 25 October 2026 (`src/Owner_Brief_25Oct2026.md`), every hard boundary and scope item in the ChatGPT master prompt (`src/ChatGPT_Master_Build_Prompt.txt`) and every category of the four Word manuals has a home in the pack. Read a row left to right: the ask, the brief requirement ID it rolls up to (R-xxx, conventions §11), the functional requirements that build it (`FR-Pxx-nn`), the appendix that holds its data or rules, and its status. Where the pack deliberately builds something different from what was asked, the row says **CHANGED-BY-DECISION** and cites the decision (D-xx), challenge (CH-xx) or non-negotiable (NN-xx) that changed it; the reason is in §Z.1.3 and in `02` §3. When a phase file changes, its owner updates the affected rows here in the same pull request (§Z.8).

---

## Z.0 Method and legend

**Sources split.** The owner brief was split into **398 atomic asks** (one row per distinct wish; compound sentences such as "download/transfer/migrate the data in standard folders … MS Word, Excel, PDF … servers, buckets, drives …" became one row per element). The ChatGPT prompt was split into **125 clause rows** covering its working method, product principles and hard boundaries, research snapshot, scope catalogue A–F, data, integration, security, pricing, UX, source register, phase map and definition of done. The four manuals were mapped at **category/area level (58 rows)**, not per document; per-document rows live in Appendix E and `R5_Document_Page_Inventory.csv`.

**Locating requirements.** FR IDs were taken from the phase files as they stood at review (25 October 2026), after the edits in §Z.6. A range `FR-P11-20…FR-P11-48` means every FR between the two IDs in that phase. Appendix references use the appendix's own section numbers (e.g., "M §M.11"). "content deck" means `content/LawDocs_Website_Content_v1.0.md`.

**Status values.**

| Status | Meaning | Action |
|---|---|---|
| COVERED | One or more FRs (or a binding appendix section) build the ask as asked, possibly with legal guard-rails that do not change the outcome the owner wanted. | None; keep the row current. |
| PARTIAL | The pack builds part of the ask, or the build depends on an output not yet in the pack (assembly item, owner content decision, vendor step). | Fix listed in §Z.5. |
| CHANGED-BY-DECISION (ref) | The pack deliberately builds a lawful or safer alternative recorded as D-xx, CH-xx or NN-xx. | None unless the owner reopens the decision in `02`. |
| MISSING | No FR or appendix section covers the ask. | Fix listed in §Z.5 (none remain after §Z.6). |

**Column legend.** *R* = brief requirement ID (R-001…R-092). *Phase / FR* = phase and the FRs that build the ask (the FR prefix identifies the phase and its §4 sub-section). *Appendix* = the appendix that holds rules, seeds or copy (letters per the pack; "—" where none is needed). *Notes* = constraint, decision text or cross-reference.

**What this appendix does not do.** It does not restate requirements; the FRs are canonical. It does not re-open D-01…D-17, CH-01…CH-32 or X-01…X-30. It does not judge FR quality (that is the `_review` pass); it judges whether each ask has a home.

## Z.1 Summary counts

### Z.1.1 Status by source (after the edits in §Z.6 and the registry review G4 re-check, 25 Oct 2026)

| Source | Rows | COVERED | PARTIAL | CHANGED-BY-DECISION | MISSING |
|---|---|---|---|---|---|
| Owner brief (TM) | 398 | 340 | 1 | 57 | 0 |
| ChatGPT prompt (TC) | 125 | 121 | 0 | 4 | 0 |
| Word manuals, section level (MW) | 58 | 49 | 9 | 0 | 0 |
| **Total** | **581** | **510** | **10** | **61** | **0** |

### Z.1.2 Status before the traceability-review edits

| Source | COVERED | PARTIAL | CHANGED-BY-DECISION | MISSING |
|---|---|---|---|---|
| Owner brief (TM) | 337 | 4 | 57 | 0 |
| ChatGPT prompt (TC) | 117 | 3 | 4 | 1 |
| Word manuals (MW) | 49 | 9 | 0 | 0 |

Five rows moved to COVERED because of the three requirements added at this review (§Z.6). No row is MISSING after the edits. Every remaining PARTIAL row is either an owner content decision or an external vendor step, not a design gap in a phase file (§Z.5). At registry review G4, TM-002 and TM-003 (pack-assembly outputs) moved from PARTIAL to COVERED because the master `01`, the decision log `02` and the Word editions now exist; the remaining PARTIAL rows are TM-296 and nine MW rows.

### Z.1.3 Which decisions changed the brief (TM and TC rows)

| Decision / challenge / rule | Rows | What changed (one line) |
|---|---|---|
| CH-01 | 1 | Aadhaar is not a login; OTP, passkey, password + MFA or SSO; Aadhaar for offline verification and ESP eSign only (NN-03). |
| CH-02 | 1 | No Aadhaar "auto-fetch"; Aadhaar App/QR offline verification (OVSE), DigiLocker, masked storage (NN-04). |
| CH-03 | 1 | CKYC search/download unavailable to a non-RE; DigiLocker/Entity Locker instead (NN-05). |
| CH-04 | 1 | No direct PAN database call; DigiLocker PAN or licensed vendor with lawful upstream. |
| CH-05 | 1 | No bureau pull at registration (CICRA ss.17(4), 22); user-uploaded reports and dispute drafting. |
| CH-06 | 1 | Company data from licensed MCA-data vendors or Entity Locker; no scraping. |
| CH-07 | 3 | Password tracker becomes the client-owned credential vault: OFF by default, delegation first, JIT reveal, client-only portal types (NN-16). |
| CH-08 | 2 | No subscription, percentage or listing fees from advocates; buyer-side platform fee only (NN-21; X-03). |
| CH-10 | 1 | Returns filed through ERI/GSP routes with taxpayer EVC/DSC and practitioner roles, not with client passwords. |
| CH-13 | 2 | Stamp paper bought only through authorised channels (agent procurement via contracted ACC; State registry) (NN-08). |
| CH-14 | 2 | "Instead of a legal team" expressed as legal operations + Vidhi + engaged advocates with a CLO (D-17). |
| CH-15 | 2 | "Like DigiLocker" becomes the branded Legal Vault; DigiLocker requester terms apply; not a DLSP. |
| CH-16 | 5 | Ecosystem sharing is purpose-bound, consented and ledgered through `int`; aggregates only to OH (NN-19, NN-24). |
| CH-17 | 3 | Automated/AI calling only with consent, disclosure, DLT registration and pre-declared numbers (NN-34). |
| CH-18 | 2 | GDPR/CCPA controls switch on by jurisdiction trigger; DPDP-first. |
| CH-19 | 1 | "PCI-DSS certification" becomes SAQ A attestation through hosted checkout. |
| CH-22 | 3 | Challans paid on official portals; grievances self-filed or filed by non-advocate representatives per forum rules; no outcome promises (NN-23). |
| CH-23 | 1 | Vehicle sale = agreement + Vahan checklist; RC transfer stays on Vahan. |
| CH-24 | 1 | "Employees cannot cheat" delivered as controls and outcome KPIs, not surveillance (NN-33). |
| CH-26 | 1 | Super Admin changes to client master data need maker-checker, client approval and notice. |
| CH-27 | 2 | Court and trademark tracking via licensed partners, user-entered numbers and manual refresh; staleness labels. |
| CH-29 | 1 | "Microsoft 365 Business Starter" is a Google Workspace edition name; owner confirms the actual M365 plan. |
| CH-30 | 1 | Free template automation on every page; AI-custom drafts labelled and gated to paid professional review for individuals (NN-14). |
| CH-32 | 1 | Login/logoff recorded for attendance only; productivity measured by outcomes. |
| D-01 | 2 | Stack locked by the owner (Expo React Native mobile, NestJS, Next.js, AWS Mumbai) before discovery. |
| D-02 | 11 | CRM, marketing, social calendar, PR, staff HRMS, payroll and billing engine live in the group Operations Hub; LawDocs supplies the Delivery Console and interfaces. |
| D-04 | 1 | ~15 flagship pages rewritten now (content deck); remaining ~600 manual-derived pages rewritten in P21. |
| D-09 | 1 | 24 phases P00–P23 instead of the ChatGPT prompt's 12. |
| D-10 | 1 | Client HRMS and governance via shared kernels; LDC is system of record when the tenant also uses it. |
| D-13 | 1 | Advertising stream OFF by default; public content pages only. |
| D-14 | 3 | Vidhi runs on Claude through a provider-neutral gateway; no contractable Jio AI model exists. |
| NN-17 | 1 | LawDocs staff act in a client tenant only under a client-approved, scoped, time-bound delivery grant (X-20: standing authorisation OFF). |

### Z.1.4 Requirement-ID coverage

All 92 brief requirement IDs (R-001…R-092, conventions §11) map to at least one TM or TC row; the index is §Z.7. Every TM and TC row cites at least one functional requirement (`FR-Pxx-nn`) or a named appendix section; 737 distinct FR IDs are cited (range endpoints counted), and each cited ID was checked against the phase files at review time and re-checked by script at registry review G4 (25 Oct 2026): every cited FR ID exists; no broken citation.

---

## Z.2 Owner brief traceability (TM-001…TM-398)

Rows follow the order of the brief. Section headings name the brief paragraph (¶) they come from; paragraphs are counted in `src/Owner_Brief_25Oct2026.md` from the first line after the title.

### Z.2.1 Working agreement and pack deliverables (brief ¶1–3)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-001 | "Prepare a prompt for building a SaaS based eSign and legal advisory tool" | R-004 | P00–P23 (24 phase files, conventions §10) | all | COVERED | Phase set complete (D-09); each file follows the §12 template. |
| TM-002 | "Build ms word file" | R-004 | — (pack-assembly output) | — | COVERED | Word editions exist: `LawDocs_Build_Prompt_Pack_v1.0.docx` (pack root; master, `02`, P00–P23 and appendices), `condensed/LawDocs_Master_Prompt_ClaudeCode_v1.0.docx`, `condensed/LawDocs_Phase_Runbook_v1.0.docx`, `content/LawDocs_Website_Content_v1.0.docx`; re-render after each content change (registry review G4). See Z.5. |
| TM-003 | ".md file" (master prompt and requirements map) | R-004 | Every phase header ("Paste after `01_MASTER_PROMPT.md` and `02_…`") | conventions §1 | COVERED | `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` exist in the pack root (master §18 carries X-01…X-30; §19 companion change requests; `02` holds the CH register, D-01…D-17 and R-001…R-092) (registry review G4). See Z.5. |
| TM-004 | "Files for phases the way you built for Finbyx and Equator" | R-004 | Phase template (conventions §12) in P00–P23 | — | COVERED | Depth matches LDC v1.2 pattern; X-25 accepts phases above the length target. |
| TM-005 | Act as Lead Software Architect, Senior Full-Stack Engineer, Mobile Engineer, Database Architect, Security Engineer and Technical Product Partner | R-001 | FR-P00-89 (ADRs), FR-P23-58 (phase report) | — | COVERED | Role statement itself belongs in `01` §role (assembly). |
| TM-006 | Owner defines objectives, approves decisions, instructs module by module | R-001 | §13 exit gate in every phase; FR-P00-07; FR-P23-58 | W | COVERED | Phase-gated execution; owner approval recorded per gate. |
| TM-007 | Translate instructions into architecture, specifications, code, tests and documentation | R-071 | §7 (backend), §12 (Gherkin) in every phase; FR-P00-90 (`docs/`) | — | COVERED |  |
| TM-008 | Do not behave merely as a code generator; challenge assumptions; flag regulatory and security risks; explain trade-offs before implementation | R-001 | "Challenges applied" header line in each phase; FR-P23-58 | P §P.2 | COVERED | CH-01…CH-32 are the recorded challenges. |
| TM-009 | Do not agree automatically; explain and recommend when a request is impractical, insecure, legally questionable or expensive | R-001 | CH register; X-03 (advocate listing fee rejected) | — | COVERED |  |

### Z.2.2 Ecosystem and integration boundaries (brief ¶4–5)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-010 | LawDocsComply (GRC for regulated financial entities) as an integrated product | R-002 | FR-P19-28…FR-P19-34; FR-P13-22…FR-P13-24 | X §X.13–§X.17; Y | COVERED | LDC is SoR for compliance, governance and client HRMS when present (D-10, NN-47). |
| TM-011 | Finbyx (LOS/LMS) integration | R-002 | FR-P19-35…FR-P19-40 | X §X.18 | COVERED | Hosted signing hand-off, not eSign sub-letting (X-05). |
| TM-012 | lawdocs.in: two parties (companies or individuals) enter personal, business or property contracts by Aadhaar-based eSign | R-006 | FR-P07-06…FR-P07-17; FR-P08-13…FR-P08-19 | F | COVERED | Eligibility gate first (NN-07); agreements for sale eSign-eligible, conveyances still registered (X-02). |
| TM-013 | "Will also be available as a mobile app" | R-017 | P22 FR-P22-01…FR-P22-97 | N §N.13 | COVERED |  |
| TM-014 | "Users will be able to draft their contract with AI and make eSign" | R-007 | FR-P06-26; FR-P08-19 | H | COVERED |  |
| TM-015 | Legal services: advisory from legal professionals after payment | R-037 | FR-P16-15 (consult slots); FR-P16-35…FR-P16-44; FR-P09-55 | M §M.3 | COVERED | Reserved services delivered by eligible practitioners (NN-41). |
| TM-016 | Retainership advisory services to businesses and financial companies | R-080 | FR-P16-45…FR-P16-53 | L §L.7; M §M.16 | COVERED |  |
| TM-017 | Expertise in financial-company RBI, SEBI and IFSCA compliance | R-080 | FR-P14-69; FR-P16-76 | M §M.16; X §X.15 | COVERED | Regulated-entity services are LDC listings in the one group storefront (D-11). |
| TM-018 | Udofin (digital lending / LSP) integration | R-002 | FR-P19-41…FR-P19-44; FR-P19-84 | X §X.19 | COVERED | No cross-sell feed; Udofin grievances never routed to Consumer Help (X-26). |
| TM-019 | Equator (mediation, arbitration, ODR) integration | R-002 | FR-P19-45…FR-P19-50; FR-P11-67…FR-P11-69; FR-P10-38 | X §X.20 | COVERED |  |
| TM-020 | "Design clear integration boundaries" with Finbyx, Udofin, Equator, LDC and third parties | R-002 | FR-P19-01…FR-P19-07; FR-P19-24…FR-P19-27 | Y; I §I.4 | COVERED | Cross-product traffic only via `int` (NN-24). |
| TM-021 | "Proper APIs and gateways so that data transfer is easy with third-party applications" | R-003 | FR-P19-01…FR-P19-23; FR-P19-65…FR-P19-77 | I §I.5–§I.7 | COVERED | Developer portal, sandbox, SDKs, iPaaS connectors. |
| TM-022 | "Onboarding of new companies is also easy" (via APIs) | R-003 | FR-P19-58…FR-P19-64; FR-P01-59…FR-P01-62 | I §I.6 | COVERED | Partner bulk onboarding with invitation and consent. |
| TM-023 | "LawDocs is also part of the ecosystem" (registered member) | R-002 | FR-P00-47 | Y §Y.3 | COVERED | Owner code `LD`; events proposed only through Appendix Y. |

### Z.2.3 Sources and research (brief ¶6)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-024 | Go through the attached Word files (web architecture, sections, content) | R-004 | FR-P21-11; FR-P21-12 | E; N §N.9; content deck §5 | COVERED | Section-level mapping in Z.4. |
| TM-025 | Deep research on the internet before preparing the prompt | R-004 | — | Q; research notes R1–R6; source sections of D, H, J, P | COVERED | Sources dated 25 Oct 2026; open facts tagged [VERIFY] (NN-38). |
| TM-026 | Refer to the manuals (reference, not copy) | R-090 | FR-P14-04; FR-P21-62 (plagiarism gate) | E §1 content codes | COVERED | D-04. |

### Z.2.4 Onboarding, identity and Vidhi (brief ¶7–8)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-027 | Tool for individuals and for companies | R-005 | FR-P02-07 (workspace types); FR-P01-63; FR-P01-64 | D §D.1 | COVERED |  |
| TM-028 | "Onboarding shall be easy" | R-005 | FR-P01-63…FR-P01-68 | — | COVERED | ≤ 2 minutes to first draft (individual); ≤ 10 minutes company wizard. |
| TM-029 | Aadhaar-based APIs that "automatically fetch the details" | R-005 | FR-P01-20; FR-P01-23 | P §P.6 | CHANGED-BY-DECISION (CH-02) | Aadhaar App/QR offline verification (OVSE) and DigiLocker; masked storage (NN-04). |
| TM-030 | PAN-based API | R-005 | FR-P01-22 | I §I.2 | CHANGED-BY-DECISION (CH-04) | DigiLocker PAN or licensed vendor with lawful upstream. |
| TM-031 | CKYC-based API | R-005 | FR-P01-23 | — | CHANGED-BY-DECISION (CH-03) | Not available to a non-RE (NN-05). |
| TM-032 | Companies enter into business agreements | R-006 | P07 FR-P07-01…FR-P07-70 | — | COVERED |  |
| TM-033 | Companies make eSign with Aadhaar | R-006 | FR-P08-19; FR-P08-54 | F | COVERED | Company tenants sending to their customers use the hosted LawDocs page (FR-P08-54). |
| TM-034 | Companies draft agreements with an AI employee | R-007 | FR-P06-32…FR-P06-35; FR-P09-34…FR-P09-36 | H §H.2 | COVERED |  |
| TM-035 | "It will support multiple languages" | R-008 | FR-P00-60; FR-P06-36…FR-P06-39; FR-P09-29; FR-P21-72…FR-P21-76; FR-P22-61 | H §H.8 | COVERED | Ten UI languages at launch (D-07). |
| TM-036 | "Individuals will be able to login through Aadhaar" | R-009 | FR-P01-05…FR-P01-12 | P §P.6 | CHANGED-BY-DECISION (CH-01) | OTP, passkey or SSO login; Aadhaar used for verification and ESP eSign only (NN-03). |
| TM-037 | Individuals then create agreements with AI | R-009 | FR-P01-63; FR-P06-16…FR-P06-27 | — | COVERED |  |
| TM-038 | Vidhi helps users in drafting | R-007 | FR-P06-32 | H §H.2 | COVERED | Brand Vidhi (D-15). |
| TM-039 | Vidhi helps users find an answer to their problem | R-010 | FR-P09-27…FR-P09-33 | H §H.6 | COVERED | Cite-or-decline (FR-P09-15; NN-14). |

### Z.2.5 Legal Vault, litigation, trademarks and marketplace (brief ¶9–12)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-040 | "The way people use DigiLocker … users keep it always" | R-011 | FR-P17-08 (free-forever vault); FR-P04-54…FR-P04-61 | P §P.3 (DL-06) | CHANGED-BY-DECISION (CH-15) | Branded "Legal Vault", not a DigiLocker/DLSP. |
| TM-041 | Prepare the agreement | R-011 | P06 | E §2 | COVERED |  |
| TM-042 | Enter into agreements | R-011 | FR-P07-12…FR-P07-17; FR-P07-41…FR-P07-44 | — | COVERED |  |
| TM-043 | Make eSign | R-011 | P08 | F | COVERED |  |
| TM-044 | Make amendments | R-011 | FR-P07-51; FR-P08-50; FR-P08-51 | — | COVERED |  |
| TM-045 | Preserve their documents | R-011 | FR-P04-01…FR-P04-07; FR-P04-49…FR-P04-53 | K | COVERED | Originals immutable (NN-09). |
| TM-046 | "A proper document management system should be there" | R-011 | P04 FR-P04-01…FR-P04-73 | — | COVERED |  |
| TM-047 | Companies track their litigation | R-012 | P11 FR-P11-01…FR-P11-74 | I §I.2 (`COURT_DATA_PORT`) | COVERED |  |
| TM-048 | "Deep research and build the complete system" (litigation) | R-012 | FR-P11-20…FR-P11-48 (hearings, orders, deadlines, counsel, spend, exposure) | Q §Q.4 | COVERED |  |
| TM-049 | Automatic court-status updates (implied by tracking) | R-012 | FR-P11-13…FR-P11-19 | I; X-29 | CHANGED-BY-DECISION (CH-27) | Licensed aggregators + user-entered CNR + manual refresh; staleness labels; no "real-time" claim (NN-05, NN-20). |
| TM-050 | Users track their trademark applications | R-013 | FR-P12-01…FR-P12-12 | I §I.2 (`TRADEMARK_DATA_PORT`) | CHANGED-BY-DECISION (CH-27) | No IP India API; user-entered numbers + assisted refresh. |
| TM-051 | "Design complete functionality after research on the available tools" (trademarks) | R-013 | FR-P12-13…FR-P12-42 | Q §Q.4 | COVERED | Clearance, objections, journal watch, renewals, licences. |
| TM-052 | Marketplace where users avail drafting services by experts | R-014 | FR-P16-01…FR-P16-08; FR-P06-29 | M §M.2 | COVERED |  |
| TM-053 | Empanel advocates | R-014 | FR-P16-23…FR-P16-27 | M §M.5 | COVERED | Rule-36-only rendering; no ratings or fees from advocates (NN-21). |
| TM-054 | Empanel tax assistants | R-014 | FR-P16-23; FR-P14-20 | M §M.5 | COVERED |  |
| TM-055 | Empanel CA, CS etc. | R-014 | FR-P16-18; FR-P14-21 | M §M.5 | COVERED | Practising-member listing locked pending ICAI/ICSI structure (CH-09). |
| TM-056 | "For Vidhi … I shall attach Claude API" | R-015 | FR-P09-01…FR-P09-03 | H §H.9 | COVERED | Bedrock India default for confidential classes (D-14, NN-15). |
| TM-057 | Explore LegalKart and similar tools | R-016 | — | Q §Q.2–§Q.3 | COVERED |  |
| TM-058 | "LegalKart is the main competitor" (match or beat it) | R-016 | FR-P16-15; FR-P16-25; FR-P09-55 | Q §Q.6 (IMP-001…IMP-105); M §M.14 | COVERED |  |
| TM-059 | Web-based application, mobile-view friendly | R-017 | FR-P00-59; FR-P02-58; FR-P21-15 | U | COVERED |  |
| TM-060 | Mobile apps for Play Store and App Store | R-017 | FR-P22-01…FR-P22-05; FR-P22-80…FR-P22-92 | N §N.13 | COVERED |  |

### Z.2.6 Agentic AI, "i" help and tutorials (brief ¶13–14)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-061 | "Explore how we can deploy agentic AI into the tool" | R-018 | FR-P09-37…FR-P09-50 | H | COVERED |  |
| TM-062 | Users are provided AI functionality | R-018 | FR-P09-27…FR-P09-36 | H §H.3 | COVERED |  |
| TM-063 | Make the life of users easy with AI | R-018 | FR-P09-27…FR-P09-33; FR-P07-45; FR-P11-26 | H §H.2 | COVERED |  |
| TM-064 | Make the life of KMPs easy with AI | R-018 | FR-P13-16; FR-P13-61 | H §H.2 | COVERED |  |
| TM-065 | Make the life of boards of companies easy with AI | R-018 | FR-P13-33; FR-P13-61; FR-P09-14 | H §H.2 | COVERED |  |
| TM-066 | "How AI agents can work like their employees within the tool" | R-018 | FR-P09-37…FR-P09-46 (hire, induct, autonomy L0–L4, missions, budgets, digests) | H §H.2 (37 agents; X-27) | COVERED | Agents are makers only (NN-43). |
| TM-067 | 'i' button explaining terms in headings, menus and compliance parts | R-019 | FR-P21-119…FR-P21-127; FR-P00-61; FR-P03-104 | N §N.12 | COVERED | ≥ 150 terms in Wave 1. |
| TM-068 | Plain explanations for users who do not understand legal or compliance language | R-019 | FR-P21-116 (easy-read); FR-P09-30 | U §U.7 | COVERED |  |
| TM-069 | Tutorials as written text | R-020 | FR-P21-132 | N §N.10 | COVERED |  |
| TM-070 | Tutorials with images and screenshots | R-020 | FR-P21-133 | N §N.10 | COVERED | Auto-captured against a seeded demo tenant. |
| TM-071 | Tutorials with diagrams | R-020 | FR-P21-134 | N §N.10 | COVERED |  |
| TM-072 | Tutorials with artefacts | R-020 | FR-P21-135 | N §N.10 | COVERED | Interactive click-through demos. |
| TM-073 | Tutorials as videos | R-020 | FR-P21-137 | N §N.10 | COVERED |  |
| TM-074 | "Feature videos can be posted on social media" | R-020 | FR-P21-138 (export presets) | N §N.10; X §X.3.5 | COVERED |  |

### Z.2.7 Data preservation, portability and bulk intake (brief ¶15)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-075 | On exit the company or user can download the data | R-021 | FR-P20-22; FR-P20-44; FR-P20-45 | K | COVERED | Never blocked, no staff help (NN-11, FR-P20-13). |
| TM-076 | Transfer or migrate the data | R-021 | FR-P20-23; FR-P20-30…FR-P20-34 | K §K.9 | COVERED |  |
| TM-077 | Standard folders and sub-folders | R-021 | FR-P20-03; FR-P20-04 | K §K.3 | COVERED |  |
| TM-078 | Self-explanatory names and categories | R-021 | FR-P20-17; FR-P04-67 | K §K.5 | COVERED | Readable naming mode per X-07. |
| TM-079 | Understandable even when not using the tool | R-021 | FR-P20-02 | K §K.2 (`00 Start Here/`), §K.7 README | COVERED |  |
| TM-080 | File types: MS Word, Excel, PDF or standard formats | R-021 | FR-P20-19; FR-P20-20 | K §K.4 | COVERED |  |
| TM-081 | Categorise by years | R-021 | FR-P20-16 | K §K.3 | COVERED | Calendar year (individuals), FY (companies); "Tax Year" labels (X-12). |
| TM-082 | Categorise by departments or other types | R-021 | FR-P20-16 | K §K.8 | COVERED |  |
| TM-083 | Save on their own servers | R-021 | FR-P20-23 (SFTP pull); FR-P20-30 | K §K.9 | COVERED |  |
| TM-084 | Save on buckets | R-021 | FR-P20-30 | — | COVERED | S3-compatible targets. |
| TM-085 | Save on drives like OneDrive | R-021 | FR-P20-30; FR-P20-32 | — | COVERED | OneDrive/SharePoint/Google Drive adapters. |
| TM-086 | Save on a hard drive | R-021 | FR-P20-22; FR-P22-28 | — | COVERED | Resumable download; mobile "Export everything". |
| TM-087 | Save in a data centre | R-021 | FR-P20-30 | J §J.2 (J-17) | COVERED | S3-compatible/SFTP or Azure Blob in Jio regions. |
| TM-088 | Structure preserved when code changes, patches or features are added | R-022 | FR-P20-37…FR-P20-43; FR-P23-17; FR-P23-18 | K §K.12 | COVERED | NN-12. |
| TM-089 | Structure preserved when code is pushed to GitHub | R-022 | FR-P20-39 (export-map CI gate); FR-P23-03; FR-P23-13 | K §K.11 | COVERED |  |
| TM-090 | Structure preserved when server type changes | R-022 | FR-P20-42; FR-P23-19 | — | COVERED |  |
| TM-091 | Structure preserved when data-centre location changes | R-022 | FR-P20-42; FR-P04-02 (keys never encode region) | — | COVERED | Transfer assessment first (NN-25). |
| TM-092 | "New code should settle the data without disturbing it" | R-022 | FR-P20-38; FR-P04-06 (view-pack migrations) | — | COVERED |  |
| TM-093 | "No manual migration of client data when new features are introduced" | R-022 | FR-P20-43; FR-P23-18 | — | COVERED | Release blockers for customer data. |
| TM-094 | "Design the database so data preservation is easy" | R-022 | FR-P00-40; FR-P04-01; FR-P04-02; FR-P20-18 | K §K.11 | COVERED | Folders are views over stable canonical IDs. |
| TM-095 | Data shareable across ecosystem apps | R-023 | FR-P04-45; FR-P19-26; FR-P20-50 | Y §Y.11 | CHANGED-BY-DECISION (CH-16) | Purpose-bound, consented, ledgered sharing (NN-24). |
| TM-096 | Other apps share data with LawDocs | R-023 | FR-P19-30; FR-P19-41; FR-P19-48; FR-P20-51 | X §X.22 | CHANGED-BY-DECISION (CH-16) |  |
| TM-097 | The folder structure also intakes data | R-024 | FR-P20-25; FR-P20-26; FR-P04-28 | K §K.10 | COVERED | Reverse mapping of the export taxonomy. |
| TM-098 | Bulk upload through the folder structure instead of one by one | R-024 | FR-P20-26…FR-P20-29; FR-P11-63; FR-P12-20 | — | COVERED | Preview, duplicate detection, undo window. |

### Z.2.8 Accessibility, workflows, settings and user types (brief ¶16–19)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-099 | Accessibility for people who cannot hear | R-025 | FR-P21-95 (transcripts); FR-P22-78 (captions) | U §U.6 (ISL renditions of core tutorials) | COVERED |  |
| TM-100 | Accessibility for people who cannot see properly | R-025 | FR-P22-73…FR-P22-77; FR-P21-144 | U §U.5 | COVERED | Screen-reader signing flow (FR-P22-77). |
| TM-101 | "All types of accessibility features" | R-025 | FR-P01-71; FR-P21-116; FR-P21-117; FR-P22-76; FR-P21-145 | U §U.7 | COVERED | WCAG 2.2 AA + IS 17802; no overlays (NN-28). |
| TM-102 | Faster workflows across teams and departments | R-026 | FR-P02-33; FR-P03-76; FR-P13-04…FR-P13-12; FR-P18-05 | T §T.3 | COVERED |  |
| TM-103 | Better logic across the tool | R-026 | FR-P03-51…FR-P03-62 (rule engine); FR-P02-23…FR-P02-27 (DoA) | R §R.6 | COVERED |  |
| TM-104 | Settings provide many customisation options | R-027 | FR-P03-23…FR-P03-50 | R §R.9–§R.10 | COVERED |  |
| TM-105 | Super admin for the developer team | R-028 | FR-P03-98…FR-P03-101 (`apps/console`) | D §D.2 (`PLT_*`) | COVERED |  |
| TM-106 | Operations hub for the operations team for client servicing | R-028 | FR-P18-01…FR-P18-10 | D §D.6; X | COVERED | D-02 split: group OH + LawDocs Delivery Console. |
| TM-107 | Admin users for companies | R-028 | FR-P02-11; FR-P02-18 | D §D.5 | COVERED |  |
| TM-108 | Companies create users such as maker and checker | R-028 | FR-P02-18…FR-P02-22; FR-P02-28…FR-P02-35 | D §D.7 | COVERED | NN-18. |
| TM-109 | Individual users | R-028 | FR-P02-12…FR-P02-14 | D §D.6 | COVERED | Family, delegate, guardian, nominee roles. |
| TM-110 | Separate functionality, design, customisation, options and features for each user type | R-028 | FR-P02-55…FR-P02-58; FR-P03-23…FR-P03-29 | R §R.10 | COVERED |  |
| TM-111 | "Research and build a faster logical workflow" per user type | R-026 | FR-P02-55; FR-P21-129 (first-run tours) | D §D.1 | COVERED |  |

### Z.2.9 Jio research (brief ¶20)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-112 | Deep research on Reliance Jio AI offerings | R-029 | — | J §J.1–§J.2; I §I.12 | COVERED |  |
| TM-113 | Jio agentic AI | R-029 | FR-P09-01 (adapter stub OFF) | J §J.1 | CHANGED-BY-DECISION (D-14) | No contractable Jio LLM; Vidhi stays on Claude. |
| TM-114 | Jio agent calling | R-029 | FR-P09-53; FR-P09-54 | J §J.5–§J.6 | CHANGED-BY-DECISION (CH-17) | Inbound intake agent; outbound AI voice only with consent, disclosure, pre-declared numbers (NN-34). |
| TM-115 | Jio automated calling | R-029 | FR-P09-54; FR-P03-73 | J §J.5 | CHANGED-BY-DECISION (CH-17) |  |
| TM-116 | Jio marketing tools | R-029 | — | J §J.2 (J-05 OH-side); X §X.3 | COVERED | Marketing engine is OH (D-02). |
| TM-117 | Jio AI research | R-029 | FR-P09-09…FR-P09-12 (notebooks) | J §J.1 | CHANGED-BY-DECISION (D-14) |  |
| TM-118 | Jio AI document drafting for parties | R-029 | FR-P06-26 | J §J.1 | CHANGED-BY-DECISION (D-14) |  |

### Z.2.10 UX, onboarding APIs, privacy and SEO (brief ¶21–24)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-119 | Content and features detailed and customisable, including UI/UX | R-030 | FR-P03-31…FR-P03-45 | R §R.10 | COVERED |  |
| TM-120 | Fewer clicks | R-030 | FR-P03-25; FR-P11-74; FR-P13-66; FR-P17-70; FR-P22-04 | — | COVERED | Click budgets in every phase. |
| TM-121 | Mostly automated processes | R-030 | FR-P03-72 (chase policies); FR-P09-41; FR-P09-42 | — | COVERED | Human confirmation for irreversible actions (NN-13; X-04 send-plan). |
| TM-122 | DigiLocker API for registration | R-005 | FR-P01-21; FR-P04-35…FR-P04-38 | P §P.6 | COVERED | Requester terms; URI + verification stored by default (NN-42). |
| TM-123 | Company-registration API for registration | R-005 | FR-P01-26…FR-P01-33 | I §I.2 | CHANGED-BY-DECISION (CH-06) | Licensed MCA-data vendors / Entity Locker; no scraping. |
| TM-124 | CIBIL etc. for registration | R-005 | FR-P01-23; FR-P15-27 | — | CHANGED-BY-DECISION (CH-05) | Prohibited bureau pull; user-uploaded reports only. |
| TM-125 | Quick and secure onboarding | R-005 | FR-P01-16; FR-P01-63; FR-P01-64 | P §P.4 | COVERED |  |
| TM-126 | Built in consonance with GDPR | R-031 | FR-P21-110 | P §P.10 | CHANGED-BY-DECISION (CH-18) | Switched on by jurisdiction trigger. |
| TM-127 | Built in consonance with CCPA | R-031 | FR-P21-110 | P §P.10 | CHANGED-BY-DECISION (CH-18) |  |
| TM-128 | Built in consonance with DPDP | R-031 | FR-P01-52…FR-P01-58; FR-P20-45 | P §P.8; O §O.1 | COVERED | NN-26. |
| TM-129 | Built in consonance with the IT Act and other privacy laws | R-031 | FR-P21-16 (grievance officer); FR-P23-51; FR-P00-32 | P §P.9 | COVERED | NN-27 CERT-In clocks. |
| TM-130 | Website content suitable for SEO | R-032 | FR-P21-46…FR-P21-58 | N §N.5–§N.7 | COVERED |  |
| TM-131 | Website content suitable for GEO | R-032 | FR-P21-67…FR-P21-71 | N §N.8 | COVERED |  |
| TM-132 | Website content suitable for AI search | R-032 | FR-P21-48; FR-P21-52; FR-P21-70 | N §N.8 | COVERED | AI-crawler policy is a setting (NN-31). |
| TM-133 | Clean, minimalistic, modern UI/UX | R-032 | FR-P00-59; FR-P21-13 | content deck §2–§3 | COVERED |  |

### Z.2.11 Certification readiness and payments (brief ¶25)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-134 | PCI-DSS | R-033 | FR-P17-20; FR-P17-21 | P §P.11 | CHANGED-BY-DECISION (CH-19) | SAQ A attestation via hosted checkout (NN-22). |
| TM-135 | SOC 2 Type 1 | R-033 | FR-P23-44; FR-P23-45 | P §P.13 | COVERED | Attestation report, never "certificate" (NN-20). |
| TM-136 | SOC 2 Type 2 | R-033 | FR-P23-40…FR-P23-45 | P §P.13 | COVERED |  |
| TM-137 | ISO certifications | R-033 | FR-P23-45 | P §P.12 | COVERED | ISO/IEC 27001-family mapping. |
| TM-138 | "Develop the SaaS accordingly" (controls designed in) | R-033 | FR-P23-40…FR-P23-47 | P §P.12 | COVERED |  |
| TM-139 | "I will prepare policies later" | R-033 | — | P §P.18 (policy set, owner-authored); O | COVERED |  |
| TM-140 | Payment-gateway security features | R-034 | FR-P17-20…FR-P17-24; FR-P19-80 | P §P.11 | COVERED | Signed callbacks, reconciliation. |
| TM-141 | Razorpay integration | R-034 | FR-P17-21; FR-P16-59…FR-P16-61 | I §I.2 (`BILLING_PORT`) | COVERED | Through OH8. |

### Z.2.12 Plans, subscriptions and pricing page (brief ¶26)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-142 | Payment, billing and subscription features in Settings | R-035 | FR-P17-66…FR-P17-70 | L §L.15 | COVERED |  |
| TM-143 | Choose a plan | R-035 | FR-P17-15; FR-P17-19 | L §L.2 | COVERED |  |
| TM-144 | Upgrade and downgrade | R-035 | FR-P17-27; FR-P17-28 | L §L.13 | COVERED | NN-50 cancellation as easy as sign-up. |
| TM-145 | Research and design the subscription model | R-036 | FR-P17-06…FR-P17-10 | L §L.1–§L.3 | COVERED |  |
| TM-146 | Research and design the business model | R-036 | — | L §L.10 | COVERED |  |
| TM-147 | Revenue streams for different kinds of companies | R-036 | FR-P17-57 | L §L.9; §L.10 | COVERED |  |
| TM-148 | Show 3 plans on the pricing page | R-036 | FR-P17-11; FR-P21-30 | L §L.2 | COVERED | Personal, Pro, Business shown; Free and Enterprise linked. |
| TM-149 | Detailed feature list on the pricing page | R-036 | FR-P17-12 | L §L.3 (110 rows) | COVERED |  |
| TM-150 | Smooth onboarding and subscription for companies | R-036 | FR-P01-64; FR-P17-17…FR-P17-23 | — | COVERED |  |

### Z.2.13 Services, marketplace commercials and Academy (brief ¶27–29)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-151 | LawDocs offers legal and advisory services | R-037 | FR-P16-27; FR-P16-28 | M §M.3 | COVERED | NN-41. |
| TM-152 | "The team can file returns" | R-037 | FR-P14-47; FR-P14-54…FR-P14-57 | — | CHANGED-BY-DECISION (CH-10) | ERI/GSP routes; taxpayer EVC/DSC. |
| TM-153 | Work one-time | R-037 | FR-P16-09 (`FIXED`) | L §L.6 | COVERED |  |
| TM-154 | Work on retainership | R-037 | FR-P16-45…FR-P16-53 | L §L.7 | COVERED |  |
| TM-155 | "Build the marketplace for this" | R-037 | P16 | M | COVERED |  |
| TM-156 | Mechanism for other CAs, CSs and lawyers to offer services | R-037 | FR-P16-23…FR-P16-29; FR-P16-54…FR-P16-58 | M §M.7 | COVERED |  |
| TM-157 | Professionals offer services on a subscription basis | R-037 | FR-P16-17; FR-P16-18; FR-P16-22 | M §M.4–§M.5 | CHANGED-BY-DECISION (CH-08) | CH-09 for CA/CS; switches locked (NN-21). |
| TM-158 | Professionals offer services on a percentage basis | R-037 | FR-P16-18; FR-P17-59 | M §M.5 | CHANGED-BY-DECISION (CH-08) | X-03; hard deny list RS-LD-27. |
| TM-159 | "Research a suitable revenue model" (marketplace) | R-049 | FR-P16-17 | L §L.9; M §M.4 | COVERED | Buyer-side platform fee. |
| TM-160 | Agreements prepared | R-038 | FR-P16-03 | M §M.2 | COVERED |  |
| TM-161 | Policies drafted | R-038 | FR-P16-03 | M §M.2 | COVERED |  |
| TM-162 | Annual reports drafted | R-038 | FR-P16-03 | M §M.2 | COVERED |  |
| TM-163 | Hire professionals for stress testing | R-038 | FR-P16-03 | M §M.2 (category 08 RSK) | COVERED |  |
| TM-164 | Hire professionals for scenario analysis | R-038 | FR-P16-03 | M §M.2 (RSK) | COVERED |  |
| TM-165 | Compliance testing | R-038 | FR-P16-03 | M §M.2 (SVC-CMP-02) | COVERED |  |
| TM-166 | Risk assessment | R-038 | FR-P16-03 | M §M.2 (SVC-RSK-01) | COVERED |  |
| TM-167 | Retainership advisory | R-038 | FR-P16-45 | L §L.7 | COVERED |  |
| TM-168 | Minutes of meetings | R-038 | FR-P13-36; FR-P16-03 | M §M.2 | COVERED |  |
| TM-169 | Initially LawDocs team offers GRC professionals; later other professionals join | R-037 | FR-P16-27; FR-P16-28; P16 sequencing line | M §M.1 | COVERED | Model M1 first (X-21). |
| TM-170 | LawDocs team and others offer customised solutions and pricing | R-039 | FR-P16-12 | M §M.15 | COVERED |  |
| TM-171 | Retainership customised | R-039 | FR-P16-46 | L §L.7 | COVERED |  |
| TM-172 | SLAs eSigned within the tool | R-039 | FR-P16-47 | O §O.15 | COVERED |  |
| TM-173 | Services additional to SaaS subscriptions | R-040 | FR-P16-80 | L §L.6 | COVERED |  |
| TM-174 | Companies can buy services without a software subscription | R-040 | FR-P16-80; FR-P18-10 | — | COVERED | D-11. |
| TM-175 | Billing and invoices | R-040 | FR-P17-46; FR-P16-62 | L §L.13 | COVERED |  |
| TM-176 | Payment gateways | R-040 | FR-P17-21 | — | COVERED |  |
| TM-177 | GST and taxation on invoices | R-040 | FR-P17-48; FR-P16-63; FR-P16-64 | L §L.13 | COVERED | [TAX MEMO] on e-commerce TCS/TDS. |
| TM-178 | Invoices emailed | R-040 | FR-P17-47 | L §L.16 | COVERED |  |
| TM-179 | Razorpay (services) | R-040 | FR-P17-21; FR-P16-59 | — | COVERED |  |
| TM-180 | Marketplace shows training courses linked to trainings.lawdocs.in | R-041 | FR-P16-72…FR-P16-75 | M §M.11 | COVERED | D-16; no copying of paid course content. |
| TM-181 | Compliance trainings, DSA/DMA trainings, CISO trainings | R-041 | FR-P16-72 | M §M.11 (categories); M §M.2 (SVC-ACA-01) | COVERED |  |
| TM-182 | Courses openly available without login or subscription | R-041 | FR-P16-01; FR-P21-29 | — | COVERED |  |
| TM-183 | Categorise services | R-041 | FR-P16-02 | M §M.2 | COVERED |  |
| TM-184 | Multiple revenue streams including recurring | R-042 | FR-P17-57 | L §L.9 | COVERED |  |
| TM-185 | Explain benefits of subscription options | R-042 | FR-P17-13 | L §L.15 | COVERED |  |
| TM-186 | Explain benefits of one-time products | R-042 | FR-P17-13 | L §L.6; §L.15 | COVERED |  |
| TM-187 | Detailed settings pages for billing and membership | R-042 | FR-P17-66…FR-P17-70 | — | COVERED |  |

### Z.2.14 Advanced DMS, type copies and translation (brief ¶30–31)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-188 | Advanced DMS: sharing | R-043 | FR-P04-39…FR-P04-45 | — | COVERED |  |
| TM-189 | Advanced DMS: eSigning from the vault | R-043 | FR-P04-29; FR-P08-13 | — | COVERED |  |
| TM-190 | Advanced DMS: search | R-043 | FR-P04-30…FR-P04-32 | — | COVERED | Keyword + semantic; Indic analysers. |
| TM-191 | Advanced DMS: filter | R-043 | FR-P04-33; FR-P04-34 | — | COVERED |  |
| TM-192 | Parties choose what to share | R-043 | FR-P04-40; FR-P07-24 | — | COVERED | NN-37. |
| TM-193 | Attach typed copies of handwritten documents | R-044 | FR-P05-06; FR-P05-13…FR-P05-15 | — | COVERED | Derived renditions; originals immutable (NN-09). |
| TM-194 | AI reads WhatsApp screenshots | R-044 | FR-P05-07; FR-P05-09…FR-P05-12; FR-P22-35; FR-P22-36 | — | COVERED | Native chat export preferred. |
| TM-195 | Attach them to the petition or claim with the typed copy | R-044 | FR-P05-22; FR-P05-23; FR-P10-26…FR-P10-29 | — | COVERED | CH-28 constraints: labels, s.63 BSA certificate (NN-10). |
| TM-196 | Users can correct AI errors | R-044 | FR-P05-16…FR-P05-18 | — | COVERED |  |
| TM-197 | Translation into English | R-045 | FR-P05-30…FR-P05-34 | — | COVERED | Labelled machine translation (NN-48). |
| TM-198 | Identify and read UN-approved languages | R-045 | FR-P05-28; FR-P05-29 | H §H.8 | COVERED | Six UN official languages accepted as input (D-07). |
| TM-199 | Identify and read the main Indian languages | R-045 | FR-P05-28 | — | COVERED | All 22 Eighth-Schedule languages as input; UI scope phased (CH-11). |
| TM-200 | Claude API for AI | R-015 | FR-P09-01; FR-P09-02 | H §H.9 | COVERED |  |
| TM-201 | "Revise everything, look for errors and fix them" | R-046 | FR-P00-06; FR-P14-03; FR-P21-61 | `00_Cross_File_Resolutions` X-01…X-30; this Appendix Z | COVERED |  |

### Z.2.15 Dynamic rules, open items and settings (brief ¶32)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-202 | Items not closed — make them customisable | R-047 | FR-P03-67…FR-P03-82 | R §R.11 | COVERED |  |
| TM-203 | Rules change (RBI etc.), so the rule engine is configurable | R-047 | FR-P03-51…FR-P03-62 | R §R.6 | COVERED | NN-30. |
| TM-204 | Content and rule engine not static | R-047 | FR-P03-63…FR-P03-66; FR-P23-20 | — | COVERED | Content releases are not code releases. |
| TM-205 | Open, interim and waiting-for-someone-else items customisable | R-047 | FR-P03-68…FR-P03-75 | R §R.8; §R.12 | COVERED | One engine `wf.items` (X-09). |
| TM-206 | Customisation in settings for every user | R-047 | FR-P03-07; FR-P03-29 | R §R.10 | COVERED |  |
| TM-207 | Super admin not needed for small changes | R-047 | FR-P03-15; FR-P11-73; FR-P13-65 | R §R.13 | COVERED | NN-29. |
| TM-208 | "Very complete settings" | R-047 | FR-P03-01…FR-P03-05 | R §R.9 | COVERED |  |

### Z.2.16 Operations, CRM and after-sales (brief ¶33)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-209 | Manage LawDocs operations | R-048 | P18 | X | COVERED | D-02. |
| TM-210 | Service delivery | R-048 | FR-P18-41…FR-P18-48; FR-P18-64…FR-P18-66 | — | COVERED |  |
| TM-211 | After-sales | R-048 | FR-P18-77; FR-P18-78 | X §X.5 | COVERED |  |
| TM-212 | Marketing and brand management | R-048 | FR-P21-99…FR-P21-106 | X §X.3 | CHANGED-BY-DECISION (D-02) | Marketing engine in OH7; LawDocs supplies landing pages and lead hand-off. |
| TM-213 | Customer success | R-048 | FR-P18-78 | X §X.5 | COVERED |  |
| TM-214 | Social media | R-048 | — | X §X.3.5 | CHANGED-BY-DECISION (D-02) | OH7.4 social calendar. |
| TM-215 | PR and collaborations | R-048 | — | X §X.3.7 | CHANGED-BY-DECISION (D-02) | OH7.7. |
| TM-216 | Separate dashboard for the operations team (not super admin) | R-048 | FR-P18-04; FR-P18-05 | D §D.6 | COVERED |  |
| TM-217 | "Like the operations hub for Finbyx and Udofin" | R-048 | FR-P18-73…FR-P18-83 | X §X.0 | COVERED | Same shared group OH. |
| TM-218 | "Explore revenue/business model again" | R-049 | — | L §L.10; §L.11 | COVERED |  |
| TM-219 | Onboarding services | R-050 | FR-P18-75 | X §X.4 | COVERED |  |
| TM-220 | Customer success managers | R-050 | FR-P18-03 (`OPS_CSM`) | X §X.5 | COVERED |  |
| TM-221 | "Own system, not third-party tools" | R-050 | FR-P18-73…FR-P18-83 | X §X.2 | COVERED | Own group OH (D-02); LawDocs never rebuilds OH functions. |
| TM-222 | CRM integrated so the team manages operations, marketing, after-sales, customer success and onboarding | R-050 | FR-P18-74; FR-P19-55 | X §X.2 | COVERED | Consented lead data only (NN-19). |
| TM-223 | Grievance redressal | R-050 | FR-P01-58; FR-P16-68 | X §X.6; O §O.9 | COVERED |  |
| TM-224 | Support tickets | R-050 | FR-P18-76 | X §X.6 | COVERED |  |
| TM-225 | "May use Brevo in future — be able to migrate/integrate; open, not closed" | R-050 | FR-P19-65…FR-P19-68 | I §I.2 (`EMAIL_PORT`); X §X.3 | COVERED |  |

### Z.2.17 Staff HR, anti-fraud and payroll (brief ¶34–35)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-226 | Performance appraisal | R-051 | FR-P18-69 (metrics feed) | X §X.8 item 4 | CHANGED-BY-DECISION (D-02) | Appraisal runs in OH10. |
| TM-227 | Manage the entire employee lifecycle | R-051 | FR-P18-01; FR-P18-02 | X §X.8 | CHANGED-BY-DECISION (D-02) |  |
| TM-228 | Assign email IDs | R-051 | FR-P18-01 | X §X.9 | CHANGED-BY-DECISION (D-02) | OH12. |
| TM-229 | Decentralised decision making | R-051 | FR-P02-23…FR-P02-27; FR-P18-15 | X §X.8 item 5 | COVERED | DoA tables. |
| TM-230 | "Employees cannot cheat management" | R-051 | FR-P18-71; FR-P18-72 | X §X.8 | CHANGED-BY-DECISION (CH-24) | Controls + outcome KPIs, not surveillance. |
| TM-231 | Management tracks performance | R-051 | FR-P18-65; FR-P18-69 | — | COVERED | NN-33. |
| TM-232 | Maker-checker for staff actions | R-051 | FR-P02-28…FR-P02-36 | D §D.7 | COVERED | NN-18. |
| TM-233 | "No corruption or embezzlement (design to minimise)" | R-051 | FR-P18-52; FR-P18-71; FR-P18-72 | X §X.8 (anti-embezzlement table) | COVERED |  |
| TM-234 | Leave management | R-052 | — | X §X.8 | CHANGED-BY-DECISION (D-02) | OH10. |
| TM-235 | Salary management and calculation per Indian labour laws | R-052 | — | X §X.8 item 2 | CHANGED-BY-DECISION (D-02) | Shared `infrabyx-labour-rulepack`. |
| TM-236 | Employees justify their salary and are productive | R-052 | FR-P18-69; FR-P18-70 | — | COVERED | Outcome metrics (CH-24). |
| TM-237 | Work from home | R-052 | — | X §X.8 item 2 | COVERED |  |
| TM-238 | Hire across India | R-052 | — | X §X.8 item 2 | COVERED | State of work drives S&E, PT, LWF, holidays. |
| TM-239 | Login/logoff time noted | R-052 | FR-P18-70 | X §X.8 item 3 | CHANGED-BY-DECISION (CH-32) | Attendance only; never a productivity proxy. |
| TM-240 | Work measured; performance assessed | R-052 | FR-P18-67…FR-P18-69 | — | COVERED | NN-33. |
| TM-241 | RMs work online from home | R-052 | FR-P18-21; FR-P18-90 | X §X.9 | COVERED |  |

### Z.2.18 Workplace suites (brief ¶36, ¶38)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-242 | "Using Microsoft 365 business starter edition" | R-053 | FR-P18-84…FR-P18-88 | X §X.9 | CHANGED-BY-DECISION (CH-29) | Name belongs to Google Workspace; [OWNER] confirm the M365 plan. |
| TM-243 | Team uses MS Teams for video | R-053 | FR-P18-46 | X §X.9 item 3 | COVERED |  |
| TM-244 | Team uses SharePoint for files | R-053 | FR-P18-47; FR-P18-48 | X §X.9 | COVERED |  |
| TM-245 | May subscribe to Google Workspace in future | R-053 | FR-P18-86 | X §X.9 | COVERED |  |
| TM-246 | Smooth migration for the operations team | R-053 | FR-P18-86 (suite-neutral data) | X §X.9 | COVERED |  |
| TM-247 | Smooth migration for clients | R-053 | FR-P18-87; FR-P03-50 | — | COVERED |  |
| TM-248 | Documents openable in MS Office | R-053 | FR-P04-65; FR-P18-88 | K §K.4 | COVERED |  |
| TM-249 | Standard self-explanatory folder structure on download | R-053 | FR-P20-03 | K §K.3 | COVERED |  |
| TM-250 | Client companies may use M365 or Google Workspace; design workflows for both | R-055 | FR-P04-66; FR-P07-65; FR-P07-66; FR-P18-84; FR-P18-87 | I §I.2 (`WORKSPACE_PORT`) | COVERED |  |

### Z.2.19 Revenue streams (brief ¶37)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-251 | Switchable, customisable revenue streams | R-054 | FR-P17-57; FR-P17-58; FR-P17-62…FR-P17-65 | L §L.9 | COVERED | Switches are maker-checker (NN-18). |
| TM-252 | One-time services | R-054 | FR-P16-09 | L §L.6 | COVERED |  |
| TM-253 | Subscriptions | R-054 | FR-P17-26 | L §L.2 | COVERED |  |
| TM-254 | Monthly rental fee | R-054 | FR-P17-57 | L §L.9 (RS-LD-04 `MONTHLY_RENTAL`) | COVERED |  |
| TM-255 | Pay as you go | R-054 | FR-P17-36…FR-P17-40; FR-P17-43 | L §L.8 | COVERED |  |
| TM-256 | Advertisements | R-054 | FR-P17-60; FR-P21-44 | L §L.9 (RS-LD-34) | CHANGED-BY-DECISION (D-13) | OFF by default; public content pages only (NN-35, CH-21). |
| TM-257 | "Explore all revenue and business models for LawDocs" | R-054 | FR-P17-57 | L §L.9 (RS-LD-01…45); §L.10 | COVERED |  |

### Z.2.20 Autopilot growth and marketing architecture (brief ¶39)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-258 | "Business on autopilot — explore the internet and create logic" | R-056 | FR-P21-99…FR-P21-106 | X §X.3 | COVERED |  |
| TM-259 | Example VSL funnel page (ptstdm.co.in/vsl-yt-v2) | R-056 | FR-P21-100…FR-P21-102 | N §N.15 | COVERED | Truthful-urgency engine (FR-P21-101; NN-50). |
| TM-260 | Brevo for email | R-056 | FR-P21-104 | X §X.3; I §I.2 | COVERED |  |
| TM-261 | Adobe Express premium for scheduling posts | R-056 | — | X §X.3.5 | COVERED | Hand-off package; schedule reference recorded. |
| TM-262 | "Information managed here" | R-056 | — | X §X.3.5 | CHANGED-BY-DECISION (D-02) | Managed in OH7 (group), not in the LawDocs app. |
| TM-263 | "Employees report here" | R-056 | — | X §X.3 item 4 | CHANGED-BY-DECISION (D-02) | Team-level contribution metrics (NN-33). |
| TM-264 | "Social post calendar here" | R-056 | — | X §X.3.5 | CHANGED-BY-DECISION (D-02) |  |
| TM-265 | Full marketing architecture | R-056 | FR-P21-99…FR-P21-110 | X §X.3; N §N.15 | COVERED |  |

### Z.2.21 Engineering governance (brief ¶40)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-266 | Patch management | R-057 | FR-P23-25…FR-P23-30 | P §P.14 | COVERED |  |
| TM-267 | Change management | R-057 | FR-P23-10…FR-P23-16 | — | COVERED |  |
| TM-268 | Push code from GitHub with branches | R-057 | FR-P00-21; FR-P00-22; FR-P23-01…FR-P23-06 | — | COVERED |  |
| TM-269 | Data backups | R-057 | FR-P00-24; FR-P23-31…FR-P23-35 | — | COVERED |  |
| TM-270 | VAPT | R-057 | FR-P23-36; FR-P23-37 | P §P.14 | COVERED | CERT-In-empanelled auditor. |
| TM-271 | IS audit | R-057 | FR-P23-37; FR-P23-41 | — | COVERED |  |
| TM-272 | Internal and external audit | R-057 | FR-P23-40…FR-P23-43 | — | COVERED |  |

### Z.2.22 Group companies (brief ¶41)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-273 | Cross-functional roles across group companies | R-058 | FR-P02-45; FR-P18-82 | X §X.10 | COVERED | Never inherited (FR-P02-44). |
| TM-274 | Operations users, dashboards and content shareable with Equator, Finbyx, Udofin | R-058 | FR-P18-82; FR-P18-83; FR-P19-51…FR-P19-57 | X §X.10 | CHANGED-BY-DECISION (CH-16) | Aggregates only to OH (NN-19). |
| TM-275 | Roles changeable | R-058 | FR-P02-18…FR-P02-20; FR-P18-02 | — | COVERED |  |
| TM-276 | Internal data shared | R-058 | FR-P02-44; FR-P19-26 | — | CHANGED-BY-DECISION (CH-16) |  |

### Z.2.23 Client HRMS and governance (brief ¶42)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-277 | HRMS for client companies | R-059 | FR-P13-51…FR-P13-60 | — | COVERED | LDC is SoR when present (D-10). |
| TM-278 | Manage KMPs | R-059 | FR-P13-40; FR-P13-42 | T §T.6 | COVERED |  |
| TM-279 | Manage directors | R-059 | FR-P13-41; FR-P13-43 | — | COVERED |  |
| TM-280 | Assign duties | R-059 | FR-P13-44; FR-P13-45 | — | COVERED |  |
| TM-281 | Allocate departments | R-059 | FR-P13-52; FR-P02-01 | — | COVERED |  |
| TM-282 | Departmental structure for finance companies customisable | R-059 | FR-P13-47; FR-P13-50 | T §T.6 | COVERED |  |
| TM-283 | Internal governance per Companies Act 2013 | R-059 | FR-P13-27…FR-P13-39 | — | COVERED | s.118 minutes; SS-1/SS-2. |
| TM-284 | Aligned with RBI master directions | R-059 | FR-P13-48; FR-P13-49 | T §T.6 | COVERED | Through the shared governance kernel [VERIFY current MD paragraphs]. |
| TM-285 | Assign tasks and get work done in the tool | R-059 | FR-P13-45; FR-P11-53; FR-P03-67 | — | COVERED |  |

### Z.2.24 Legal-team replacement and individual litigants (brief ¶43–44)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-286 | "Tool sufficient instead of a legal team" | R-060 | FR-P13-01…FR-P13-03 | T §T.1 | CHANGED-BY-DECISION (CH-14) | Legal operations + Vidhi + engaged advocates (D-17). |
| TM-287 | "A CLO or one person suffices" | R-060 | FR-P13-14; FR-P07-58 | T §T.2 | CHANGED-BY-DECISION (CH-14) |  |
| TM-288 | For individuals, works like DigiLocker | R-061 | P04 | P §P.3 | CHANGED-BY-DECISION (CH-15) |  |
| TM-289 | Any individual facing litigation can handle everything from advice | R-061 | FR-P11-55…FR-P11-58; FR-P10-23…FR-P10-25; FR-P16-15 | — | COVERED | Party-in-person mode; legal-aid signposting. |
| TM-290 | … to preservation of legal documents | R-061 | FR-P11-49; FR-P11-50; P04 | K | COVERED |  |

### Z.2.25 Jio services for customers and operations (brief ¶45)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-291 | Explore Jio AI services for customers (also for Finbyx and Udofin) | R-062 | — | J §J.8 | COVERED | Pointer only; Finbyx/Udofin packs own their use. |
| TM-292 | Integrate Jio on LawDocs for client companies | R-062 | FR-P10-22 (bulk notices via `packages/notify`) | J §J.2 (tenant-branded mode) | COVERED | DLT profile per tenant. |
| TM-293 | Integrate Jio for internal operations | R-062 | — | J §J.2 (J-05, J-07) | COVERED |  |
| TM-294 | Jio AI research, automated calling, customer service | R-062 | FR-P09-53; FR-P09-54 | J §J.5 | CHANGED-BY-DECISION (CH-17) | D-14 for AI models. |
| TM-295 | Browse jio.com/business thoroughly — services, segments, resources | R-062 | — | J §J.2 (R4) | COVERED |  |
| TM-296 | "Add integration capability after reading developer pages" | R-062 | FR-P19-65…FR-P19-67 | J §J.3; §J.11 (OI-R4-01) | PARTIAL | JioCX endpoint and auth pages sit behind sign-up; adapters stay OFF until OI-R4-01 closes (NN-38). See Z.5. |

### Z.2.26 Savings page (brief ¶46)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-297 | Savings page in Settings | R-063 | FR-P17-73 | L §L.12 | COVERED | Settings → Savings & Value. |
| TM-298 | Money saved | R-063 | FR-P17-72 | L §L.12 | COVERED | Evidence class shown (NN-36). |
| TM-299 | Hours saved | R-063 | FR-P17-72 | L §L.12 | COVERED |  |
| TM-300 | Penalties avoided | R-063 | FR-P17-72 | L §L.12 | COVERED | Shown as avoided exposure only with an evidenced obligation. |
| TM-301 | With practical quantification | R-063 | FR-P17-71; FR-P17-72; FR-P07-49; FR-P14-37; FR-P15-69 | L §L.12 | COVERED |  |

### Z.2.27 RM-as-maker delivery model (brief ¶47)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-302 | Ops hub serves clients with professional, legal, drafting, compliance and returns services | R-064 | FR-P18-41; FR-P16-48 | — | COVERED |  |
| TM-303 | On retainership a dedicated RM acts as Maker User for that company | R-064 | FR-P02-17; FR-P13-62; FR-P18-11…FR-P18-13 | D §D.10 | COVERED | Delivery grants (NN-17). |
| TM-304 | Client employee is Checker | R-064 | FR-P18-17 | — | COVERED |  |
| TM-305 | Multiple maker users possible | R-064 | FR-P18-15 | — | COVERED |  |
| TM-306 | Client can create a maker user for professional services | R-064 | FR-P18-16 | — | COVERED |  |
| TM-307 | Ops hub can also create a maker user for that company | R-064 | FR-P18-13; FR-P18-14 | — | CHANGED-BY-DECISION (NN-17) | Two-way initiation, client approval; standing authorisation OFF by default (X-20). |
| TM-308 | … and assign departmental roles | R-064 | FR-P18-15 | — | COVERED |  |
| TM-309 | Services delivered from the ops hub, which shares data with Finbyx and Udofin | R-064 | FR-P19-35…FR-P19-44 | X §X.18–§X.19 | CHANGED-BY-DECISION (CH-16) | NN-19, NN-24. |

### Z.2.28 Client section in the operations hub (brief ¶48–49)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-310 | Dedicated section per client in the ops hub | R-065 | FR-P18-07…FR-P18-10 | — | COVERED |  |
| TM-311 | Login/password tracker page | R-065 | FR-P18-26…FR-P18-35 | P §P.6 | CHANGED-BY-DECISION (CH-07) | Client-owned credential vault, OFF by default (D-03, NN-16). |
| TM-312 | Tracker entries: CERSAI, MCA, CIBIL, Experian, GST portal, RBI CIMS, Daksh, Pravaah | R-065 | FR-P18-28 | — | CHANGED-BY-DECISION (CH-07) | All seeded as entry types; CIMS, DAKSH, PRAVAAH, CIC portals and CERSAI client-only by default. |
| TM-313 | Tracker shared with the client admin | R-065 | FR-P18-35 | — | COVERED |  |
| TM-314 | Both sides can view, provide and change passwords | R-065 | FR-P18-30…FR-P18-32 | — | CHANGED-BY-DECISION (CH-07) | Delegation first; just-in-time reveal with purpose and client approval; OTPs never stored. |
| TM-315 | Billing and invoices pages feeding the client's billing page | R-065 | FR-P18-49…FR-P18-52 | — | COVERED | Same component, same OH8 data. |
| TM-316 | Data sharing in the client section | R-065 | FR-P18-41; FR-P18-42 | — | COVERED |  |
| TM-317 | Messaging in the client section | R-065 | FR-P18-44; FR-P18-45 | — | COVERED |  |
| TM-318 | Common drive link (Google Drive, OneDrive) openable in the browser | R-065 | FR-P18-47 | — | COVERED |  |
| TM-319 | … to deliver files like policies | R-065 | FR-P18-41; FR-P18-48 | — | COVERED |  |
| TM-320 | Super admin changes crucial client details | R-066 | FR-P02-59; FR-P02-60; FR-P18-36…FR-P18-40 | — | CHANGED-BY-DECISION (CH-26) | Maker-checker with client approval and notice. |
| TM-321 | Ops hub serves files, data, messages, maker role, password tracker and billing | R-066 | FR-P18-07 | — | COVERED |  |
| TM-322 | Transparent, fast workflow | R-066 | FR-P18-13; FR-P18-25; FR-P18-89 | — | COVERED | Client-visible access log. |

### Z.2.29 Audit, downloads and tax (brief ¶50–51)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-323 | Proper audit trail | R-067 | FR-P00-33…FR-P00-39 | P §P.7 | COVERED | NN-02, NN-45. |
| TM-324 | Users can download documents | R-068 | FR-P04-46; FR-P22-27 | — | COVERED |  |
| TM-325 | Users can download data | R-068 | FR-P20-10…FR-P20-14; FR-P22-28 | K | COVERED | NN-11. |
| TM-326 | Taxation functionality for individuals | R-069 | FR-P14-45…FR-P14-51 | — | COVERED | Income-tax Act 2025 transition (FR-P14-63…FR-P14-66). |
| TM-327 | Taxation functionality for companies | R-069 | FR-P14-52…FR-P14-56 | — | COVERED |  |
| TM-328 | Taxation functionality for LLPs | R-069 | FR-P14-54 | — | COVERED |  |
| TM-329 | Internal team dashboard separate from super admin for marketing, operations and after-sales | R-048 | FR-P18-04; FR-P18-65 | X §X.3; §X.5 | COVERED | Marketing views in OH7 (D-02). |

### Z.2.30 Website, content and policies (brief ¶52–55)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-330 | Explore www.lawdocs.in public pages | R-070 | FR-P00-75…FR-P00-82 | content deck §5 | COVERED | SSR fix, 301 map. |
| TM-331 | Reuse content for the fresh website (Word file contains the same content) | R-070 | FR-P21-12 | N §N.9; E | COVERED | D-04. |
| TM-332 | Write missing content | R-070 | FR-P10-04 | E §3; §4.3; content deck | COVERED |  |
| TM-333 | Copywriting | R-070 | FR-P21-20…FR-P21-34 | N §N.1–§N.3; content deck §4 | COVERED |  |
| TM-334 | SEO, GEO and generative-AI suitable copy | R-070 | FR-P21-46…FR-P21-71 | N | COVERED |  |
| TM-335 | Develop frontend and backend both | R-071 | §6 and §7 of every phase | — | COVERED |  |
| TM-336 | … plus frontend content | R-071 | — | content deck; N | COVERED | D-04. |
| TM-337 | Prepare the privacy policy | R-072 | FR-P21-34 | O §O.1 | COVERED | Review-ready draft [COUNSEL]. |
| TM-338 | Prepare terms and conditions | R-072 | FR-P21-34 | O §O.2 | COVERED |  |
| TM-339 | Prepare other policies | R-072 | FR-P21-34 | O §O.3–§O.15 | COVERED | POL-LD-01…17 (X-30). |
| TM-340 | Integrate policies into the website | R-072 | FR-P21-16; FR-P21-34 | O | COVERED |  |
| TM-341 | Blog section | R-073 | FR-P21-77…FR-P21-92 | N §N.11 | COVERED |  |
| TM-342 | Owner supplies categorised Word files for the blog | R-073 | FR-P21-79 (DOCX/ZIP import) | N §N.11 | COVERED | [OWNER] supplies the folder list. |
| TM-343 | Vlog section with YouTube-hosted videos | R-074 | FR-P21-93…FR-P21-98 | N §N.10 | COVERED |  |
| TM-344 | Explore similar products and add their services | R-075 | FR-P16-03 | Q §Q.6; M §M.14 | COVERED |  |

### Z.2.31 Case management, deal rooms, eStamp and pleadings (brief ¶56–59)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-345 | Companies manage multiple court cases the way Provakil works | R-076 | FR-P11-01…FR-P11-12; FR-P11-62…FR-P11-66 | Q §Q.2 | COVERED |  |
| TM-346 | Companies message each other while signing | R-077 | FR-P07-22; FR-P07-61; FR-P08-26…FR-P08-28 | — | COVERED | Connected rooms across tenants. |
| TM-347 | Prepare agreements together | R-077 | FR-P07-09…FR-P07-11 | — | COVERED |  |
| TM-348 | Review in track-changes mode | R-077 | FR-P07-23…FR-P07-29; FR-P07-65 | — | COVERED | Deterministic redline (NN-37). |
| TM-349 | eSign after review | R-077 | FR-P07-41…FR-P07-44; P08 | — | COVERED |  |
| TM-350 | Record and audit trail of the negotiation and signing | R-077 | FR-P07-31; FR-P08-44; FR-P08-45 | — | COVERED | NN-10. |
| TM-351 | eStamp API | R-078 | FR-P08-01…FR-P08-07; FR-P08-31 | F §F.5 | CHANGED-BY-DECISION (CH-13) | Authorised channels only (NN-08). |
| TM-352 | Buy stamp papers online | R-078 | FR-P08-31 | F §F.5 | CHANGED-BY-DECISION (CH-13) | Agent procurement through a contracted ACC; State coverage registry. |
| TM-353 | Or attach stamp papers | R-078 | FR-P08-32…FR-P08-34 | — | COVERED | UIN verified and hash-linked. |
| TM-354 | Then eSign | R-078 | FR-P08-30 | — | COVERED | Stamp before sign. |
| TM-355 | Users draft court pleadings | R-079 | P10 FR-P10-01…FR-P10-38 | E §4 | COVERED |  |
| TM-356 | Legal advisory on retainership and one-time basis — business model | R-080 | FR-P16-09; FR-P16-45 | L §L.7; §L.10 | COVERED |  |
| TM-357 | FinLegal Academy (trainings.lawdocs.in) integration | R-081 | FR-P16-72…FR-P16-75 | M §M.11 | COVERED |  |
| TM-358 | Academy drafting and other trainings | R-081 | FR-P16-72 | M §M.11 ("Drafting and paralegal") | COVERED |  |

### Z.2.32 Startup Desk (brief ¶60)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-359 | Startup section: registration | R-082 | FR-P14-38…FR-P14-41; FR-P21-31 | E §6 | COVERED |  |
| TM-360 | Startup legal advisory | R-082 | FR-P14-43 | M §M.2 | COVERED |  |
| TM-361 | "Act as their legal officer" | R-082 | FR-P14-43 (virtual legal officer retainer) | — | COVERED | Positioned per D-17; reserved work by practitioners (NN-41). |
| TM-362 | Startup trademarks | R-082 | FR-P12-37; FR-P14-39 | — | COVERED |  |
| TM-363 | Startup funding documents | R-082 | FR-P14-40; FR-P14-42 | — | COVERED | Founder documents and data room. |

### Z.2.33 Consumer Help: grievances, challans and vehicles (brief ¶61–62)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-364 | Grievances relating to financial loans and lending | R-083 | FR-P15-21…FR-P15-26 | S §S.3 | COVERED |  |
| TM-365 | Grievances relating to insurance | R-083 | FR-P15-30…FR-P15-34 | S §S.5 | COVERED |  |
| TM-366 | Like FREED, ClaimBuddy, Insurance Samadhan | R-083 | — | Q §Q.2 | COVERED | Competitor study (R2). |
| TM-367 | A dedicated legal team resolves grievances | R-083 | FR-P18-53…FR-P18-58 | S §S.15 | CHANGED-BY-DECISION (CH-22) | Non-advocate case managers; representation per forum rules; no outcome promises (NN-23). |
| TM-368 | … and approaches companies | R-083 | FR-P15-38…FR-P15-40 | S §S.7 | COVERED | Authority letters. |
| TM-369 | Separate entities will be formed | R-083 | FR-P00-26; FR-P15-01; FR-P15-02 | X §X.1 | COVERED | D-06 ethical wall. |
| TM-370 | LawDocsComply may be renamed to avoid conflict of interest | R-083 | FR-P00-26 | Y | COVERED | Brand and entity identity configurable; rename is an [OWNER] decision outside LawDocs. |
| TM-371 | Users maintain documents in the app | R-083 | FR-P15-15; FR-P15-16 | — | COVERED |  |
| TM-372 | Users maintain litigation status | R-083 | FR-P11-55 | — | COVERED |  |
| TM-373 | Users maintain complaint and resolution status | R-083 | FR-P15-63…FR-P15-66; FR-P22-57 | — | COVERED |  |
| TM-374 | Check challans | R-084 | FR-P15-49 | S §S.8 | CHANGED-BY-DECISION (CH-22) | User-initiated lookup on official sources only. |
| TM-375 | Pay challans | R-084 | FR-P15-51 | S §S.8 | CHANGED-BY-DECISION (CH-22) | Official portal; LawDocs never collects fines. |
| TM-376 | If the challan goes to court, hire an advocate to contest | R-084 | FR-P15-52; FR-P15-53 | M §M.13 | COVERED | Rule-36 directory in neutral order. |
| TM-377 | Like ChallanWallah, ChallanPay — reverse-engineer | R-084 | — | Q §Q.2 | COVERED |  |
| TM-378 | Vehicle sale agreements | R-085 | FR-P15-57; FR-P15-58 | content deck FP-04 | COVERED |  |
| TM-379 | Selling vehicles | R-085 | FR-P15-56; FR-P15-59…FR-P15-61 | S §S.9 | CHANGED-BY-DECISION (CH-23) | RC transfer stays on Vahan. |
| TM-380 | Explore vehicle loans | R-085 | FR-P15-60; FR-P15-70 (added at traceability review) | S §S.3 | COVERED | Was PARTIAL (only hypothecation removal); fixed — see Z.6. |
| TM-381 | Vehicle challans etc. | R-085 | FR-P15-48; FR-P15-55 | — | COVERED |  |

### Z.2.34 Competitors and search (brief ¶63–64)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-382 | Explore every section of LegalKart | R-086 | — | Q §Q.3 | COVERED |  |
| TM-383 | Reverse-engineer and add similar functionality | R-086 | FR-P09-55; FR-P16-15 | Q §Q.6 | COVERED |  |
| TM-384 | Explore OnlineLegal, Vakilsearch etc. | R-086 | — | Q §Q.2 | COVERED |  |
| TM-385 | Front-end pages suitable for SEO, GEO, generative AI and advanced search | R-032 | FR-P21-18; FR-P21-46…FR-P21-71 | N | COVERED |  |

### Z.2.35 Process, content quality and conversion blocks (brief ¶65–66)

| ID | Owner ask (quote or paraphrase) | R | Phase / FR | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TM-386 | Use plan mode and ask questions before preparing | R-092 | — | conventions §8 (D-01…D-17) | COVERED | Done 25 Oct 2026. |
| TM-387 | First improve the content of the Word files | R-090 | FR-P21-61; FR-P21-62 | content deck §5 | CHANGED-BY-DECISION (D-04) | ~15 flagship pages now; ~600 pages in P21. |
| TM-388 | Then use it on the website front end | R-090 | FR-P21-12 | N §N.9 | COVERED |  |
| TM-389 | Research one-liners similar to the owner's | R-090 | FR-P21-43 | N §N.2; content deck §2.7–§2.8 | COVERED |  |
| TM-390 | Update FAQs to show in search results | R-090 | FR-P21-39; FR-P21-49 | N §N.4; content deck §6 | COVERED | FAQ rich results discontinued (conventions §13.18 [VERIFY]); visible FAQs, schema only where valid. |
| TM-391 | Minimalistic UI/UX | R-032 | FR-P21-13 | content deck §3 | COVERED |  |
| TM-392 | Every page has a dedicated section to draft the agreement | R-087 | FR-P06-23; FR-P21-35 | content deck §3.4 (GB-04) | COVERED |  |
| TM-393 | The user can draft with AI for free (Claude API) | R-087 | FR-P06-22…FR-P06-27 | H | CHANGED-BY-DECISION (CH-30) | Template automation free; AI-custom drafts use credits and carry the individual review gate (NN-14). |
| TM-394 | If the user wants a professional review, pay and hire a professional | R-087 | FR-P06-29; FR-P21-37 | M §M.17; content deck §3.5 | COVERED |  |
| TM-395 | Testimonials on pages | R-088 | FR-P21-38 | content deck §3.7 | COVERED | CH-20: genuine, consented, verified purchase, never about advocates (NN-49). |
| TM-396 | Testimonials without photos | R-088 | FR-P21-38 | — | COVERED |  |
| TM-397 | Team can upload blogs without the developer team | R-089 | FR-P21-77…FR-P21-92 | — | COVERED | Content Studio (X-22). |
| TM-398 | Consider the attached ChatGPT prompt | R-091 | — | Appendix Z §Z.3 | COVERED |  |

---

## Z.3 ChatGPT master prompt traceability (TC-001…TC-125)

The owner asked the pack to "consider" the ChatGPT prompt (R-091). Its hard boundaries are, almost line for line, already non-negotiables in this pack (NN-03…NN-07, NN-13, NN-16, NN-20, NN-33). Where the two disagree, the pack's owner decisions govern (D-01 stack, D-09 phase count, D-10 HRMS scope); those rows say CHANGED-BY-DECISION. Two of the prompt's working rules (pre-implementation proposals and end-of-phase reports) and one boundary (LawDocs is not automatically a regulated entity or LSP) had no explicit home; they were added at this review (§Z.6).

### Z.3.1 Clause rows

#### Z.3.1a Role and working method ("Your role", "How to work with the owner" 1–7)

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-001 | Role: lead product architect, full-stack and mobile, database, security and privacy, UX/accessibility, technical product partner | R-001 | FR-P00-89; FR-P23-58 | — | COVERED | Role text lives in `01` (assembly). |
| TC-002 | Do not agree automatically; separate verified facts, assumptions, legal questions and recommendations; no final legal opinion | R-001 | Conventions §2 tags in every phase | — | COVERED | [LAW]/[INTERP]/[REC]/[VERIFY]/[COUNSEL]/[TAX MEMO]/[OWNER]. |
| TC-003 | 1 — Start with Phase 00 discovery; inspect repo and materials before proposing a stack | R-092 | FR-P00-01…FR-P00-07 | — | CHANGED-BY-DECISION (D-01) | Owner locked the stack on 25 Oct 2026; P00 discovers the legacy system and verifies runtime versions. |
| TC-004 | 2 — Inventory supplied materials; do not invent missing files | R-004 | FR-P00-02 | E (manuals present in `src/`) | COVERED |  |
| TC-005 | 3 — No implementation before owner approval; stop at each phase gate | R-001 | FR-P00-07; §13 of every phase; FR-P23-58 | — | COVERED |  |
| TC-006 | 4 — Avoid repeat questions; reversible labelled assumptions; small option sets | R-001 | [OWNER] tags; OI-xx register | W | COVERED |  |
| TC-007 | 5 — Show scope, dependencies, risks and acceptance before major work; decision log and ADRs | R-001 | FR-P00-89; FR-P23-12; FR-P23-58 | — | COVERED | Was PARTIAL (no pre-implementation proposal rule); fixed by FR-P23-58. |
| TC-008 | 6 — Preserve working functionality; migrations and compatibility; never reset or relocate tenant data routinely | R-022 | FR-P00-66…FR-P00-74; FR-P20-38; FR-P23-17; FR-P23-18 | K §K.12 | COVERED | NN-12. |
| TC-009 | 7 — End-of-phase report (changes, files, tests, risks, decisions, next phase); never claim unproven success | R-001 | FR-P23-58 (added at traceability review) | — | COVERED | Was PARTIAL; fixed — see Z.6. |

#### Z.3.1b Product, ecosystem and goal

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-010 | India-first web platform, phone-friendly, API-first, future iOS/Android | R-017 | P19; P21; P22 | — | COVERED |  |
| TC-011 | Decide shared versus dedicated mobile UI only after research | R-017 | FR-P00-13; FR-P22-01 | — | CHANGED-BY-DECISION (D-01) | One Expo codebase with brand flavours. |
| TC-012 | Ecosystem products may be separate legal entities | R-002 | FR-P00-26 | X §X.1; Y §Y.3 | COVERED |  |
| TC-013 | LawDocsComply brand may change; keep product and legal-entity identity configurable | R-002 | FR-P00-26 | Y | COVERED | D-08. |
| TC-014 | Define product, tenant, controller, processor and service-provider boundaries | R-002 | FR-P19-12 | M §M.12; Y §Y.6; P §P.8 | COVERED |  |
| TC-015 | No shared database; no silent group-staff cross-tenant access; grants, purpose limitation, audit, revocation, conflict controls | R-058 | FR-P02-44…FR-P02-51; FR-P18-19; FR-P18-73 | D §D.10 | COVERED | NN-17, NN-24. |
| TC-016 | Goal: create, negotiate, sign, store, find, share, export and manage documents and matters | R-011 | P04; P06; P07; P08; P11; P20 | — | COVERED |  |
| TC-017 | Visible workflows: approvals, legal ops, board, litigation, IP, services, support, compliance | R-026 | P02; P11; P12; P13; P16; P18 | — | COVERED | Compliance workflows sit in LDC (D-10). |
| TC-018 | Plain-language interface for legal and compliance terms | R-019 | FR-P21-116; FR-P21-119 | U §U.7 | COVERED |  |
| TC-019 | Sequence of usable releases; secure core first; wider scope through gates | R-001 | Conventions §10 waves | — | COVERED | Wave 1 "Vault & Sign GA". |

#### Z.3.1c Product principles and hard boundaries

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-020 | Assist, never replace, a lawyer; route high-stakes questions to professionals; AI drafts labelled and reviewed | R-060 | FR-P06-27; FR-P06-28; FR-P09-22; FR-P10-33 | H §H.6 | COVERED | D-17, CH-14, NN-14, NN-41. |
| TC-021 | No promise that every document can be eSigned; counsel-reviewed, dated instrument eligibility matrix | R-006 | FR-P08-08…FR-P08-12 | F | COVERED | NN-07; X-02. |
| TC-022 | Aadhaar never the only login; authentication, identity verification and signing separated; accessible alternatives | R-009 | FR-P01-04…FR-P01-12; FR-P01-71 | P §P.6 | COVERED | NN-03. |
| TC-023 | Aadhaar eSign only through an authorised CCA provider within its ASP arrangement; consent and evidence retained; no UIDAI bypass | R-006 | FR-P08-02…FR-P08-05; FR-P08-24; FR-P08-53 | F §F.1 | COVERED | NN-06 as read with X-05, X-15, X-16. |
| TC-024 | Minimise Aadhaar data; dedicated vault only if lawful storage is required | R-005 | FR-P04-22; FR-P05-37; FR-P22-32 | P §P.6 | COVERED | Pack never stores a full Aadhaar number, so no ADV is needed (NN-04, X-14). |
| TC-025 | PAN, CKYC, MCA and bureau data not presumed open; prove authorisation; human-upload fallback | R-005 | FR-P01-26…FR-P01-28 | I §I.15 | COVERED | NN-05; CH-03…CH-06. |
| TC-026 | No shared plaintext password tracker | R-065 | FR-P18-26…FR-P18-35 | P §P.6 | COVERED | NN-16; CH-07. |
| TC-027 | No scraping, CAPTCHA bypass or impersonation; source, timestamp, confidence, last-verified; no "real time" claim | R-012 | FR-P11-15; FR-P12-11 | I §I.14 | COVERED | NN-05, NN-20. |
| TC-028 | No irreversible agent action without per-action human confirmation | R-018 | FR-P09-20; FR-P03-73 | H §H.12 | COVERED | NN-13, NN-43; bounded send-plan per X-04 [OWNER/COUNSEL]. |
| TC-029 | No silent cross-company sharing; shared work queues with separated data; client grants; access visible | R-058 | FR-P18-05; FR-P18-25 | — | COVERED | NN-17, NN-19. |
| TC-030 | No monetisation of confidential data, no ad targeting or model training; ad-free confidential areas; no sale of personal data | R-054 | FR-P17-59; FR-P17-60 | L §L.9 | COVERED | NN-15, NN-35. |
| TC-031 | No premature certification claims; SOC 2 is an attestation; PCI scope via hosted checkout | R-033 | FR-P23-44…FR-P23-46 | P §P.0; §P.11 | COVERED | NN-20; CH-19. |
| TC-032 | Proportionate, disclosed productivity measurement; no covert monitoring or login-hours proxy | R-052 | FR-P13-56; FR-P18-70 | X §X.8 | COVERED | NN-33; CH-24; CH-32. |

#### Z.3.1d Research and legal-source method; research snapshot

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-033 | First-party sources; record authority, title, URL, dates, applicability | R-004 | — | Source sections in D, H, J, P; research notes R1–R6 | COVERED |  |
| TC-034 | Recheck sources immediately before implementation | R-046 | FR-P00-52; FR-P03-57; FR-P03-60 | — | COVERED | NN-38 flags stay OFF until verified. |
| TC-035 | Identify entity type and activity first; map rules to the actual party | R-047 | FR-P03-53; FR-P13-25; FR-P13-26; FR-P14-05…FR-P14-07 | T §T.7 | COVERED |  |
| TC-036 | Qualified lawyer/CA/CS validates conclusions and policy drafts | R-072 | FR-P03-55 (reviewer of record) | O (review-ready status) | COVERED | NN-30. |
| TC-037 | CCA eSign: only CAs act as ESPs; consent and logs with ASP; no sub-letting | R-006 | FR-P08-53; FR-P19-38 | F §F.1 | COVERED | Hosted hand-off model (X-05). |
| TC-038 | Aadhaar Act and UIDAI Aadhaar Data Vault guidance | R-005 | FR-P04-22 | P §P.6 | COVERED |  |
| TC-039 | DPDP phased commencement; foreign regimes only on triggers; no blanket localisation claim | R-031 | FR-P01-52…FR-P01-58; FR-P21-110 | P §P.8; §P.10 | COVERED | India hosting is a design decision (D-01, NN-25), not presented as a DPDP rule. |
| TC-040 | RBI Digital Lending Directions mapped to each client's RE category; LawDocs not automatically an RE or LSP | R-002 | FR-P19-84 (added at traceability review); FR-P13-48; FR-P13-49; FR-P18-20 | — | COVERED | Was MISSING (no explicit regulatory-role statement); fixed — see Z.6. |
| TC-041 | BSA 2023 electronic records; integrity, validation, exportability for evidence | R-067 | FR-P05-24…FR-P05-27; FR-P08-44…FR-P08-49; FR-P20-21 | — | COVERED | NN-10. |
| TC-042 | RB-IOS changes; verify eligibility; consumer controls filing; NCH; Bima Bharosa | R-083 | FR-P15-12; FR-P15-25; FR-P15-32; FR-P15-33; FR-P15-37 | S §S.2 | COVERED | NN-23. |
| TC-043 | Different regulators and professional rules; marketplace review per profession | R-037 | FR-P16-18 | M §M.5 | COVERED | NN-21. |
| TC-044 | WCAG 2.2 AA; real testing; no overlays | R-025 | FR-P21-145; FR-P23-49 | U §U.8 | COVERED | NN-28 adds IS 17802. |
| TC-045 | JioBusiness capabilities verified before becoming dependencies | R-029 | FR-P09-01 | J §J.1–§J.4 | COVERED | NN-38. |
| TC-046 | Competitor claims are self-published; never copy text, design, code or brand | R-086 | FR-P14-04; FR-P21-62 | Q §Q.1 | COVERED |  |

#### Z.3.1e Scope catalogue A — individual and small-business workspace

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-047 | Simple onboarding, account recovery, accessible options, explicit workspace switching | R-005 | FR-P01-15; FR-P01-63; FR-P02-08 | — | COVERED |  |
| TC-048 | Vault: folders, metadata, tags, search, versions, sharing, expiry/revocation, activity, reminders, download, portability | R-043 | FR-P04-01…FR-P04-56; P20 | K | COVERED |  |
| TC-049 | Agreement builder (personal, property, employment, business, vehicle sale) only after legal review of templates, state variants, stamps, exclusions | R-006 | FR-P06-05…FR-P06-07; FR-P06-46; FR-P06-54; FR-P06-55 | E; F | COVERED |  |
| TC-050 | Counterparty invitations, comments, negotiation, redlines, version locking, signing sequence; evidence preserved | R-077 | FR-P07-12…FR-P07-44; FR-P08-14 | — | COVERED |  |
| TC-051 | Legal services purchasable separately from the subscription | R-040 | FR-P16-80 | — | COVERED |  |
| TC-052 | Notices and pleadings as assisted workflows with jurisdiction/limitation prompts and human review; no guarantee | R-079 | FR-P10-11; FR-P10-14…FR-P10-16; FR-P10-31; FR-P10-33 | E §4 | COVERED |  |

#### Z.3.1f Scope catalogue B — company LegalOps and governance

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-053 | Tenant admin, departments, subsidiaries, branches, teams, maker/checker/approver, delegated professionals, client-visible ops staff | R-028 | P02; FR-P18-89 | D | COVERED |  |
| TC-054 | Contract intake, templates, ownership, approvals, renewals, obligations, negotiation, versions, eSign, reporting | R-077 | P07 | — | COVERED |  |
| TC-055 | Board and committee agenda, papers, attendance, minutes, resolutions, actions, KMP/director profiles, duty calendars | R-059 | FR-P13-25…FR-P13-46 | T | COVERED | D-10 kernel. |
| TC-056 | Litigation portfolio with approved court sources; stale and missing updates marked | R-012 | FR-P11-03; FR-P11-10; FR-P11-13…FR-P11-19; FR-P11-39…FR-P11-47 | I | COVERED | CH-27. |
| TC-057 | Trademark/IP portfolio with official or authorised data and a manual path | R-013 | P12 | I | COVERED | CH-27. |
| TC-058 | Compliance obligations and rules versioned, sourced, effective-dated, tenant-configurable, with source and review date shown | R-047 | FR-P03-53…FR-P03-62; FR-P19-34 | R §R.6 | COVERED | Compliance SoR is LDC. |
| TC-059 | Company HR and task features are later-phase and not a replacement for a specialist HR/payroll product until validated | R-059 | FR-P13-51…FR-P13-60 | X §X.13 | CHANGED-BY-DECISION (D-10) | Owner asked for client HRMS (R-059); shared kernel in Wave 2; LDC is SoR when present. |

#### Z.3.1g Scope catalogue C — Vidhi AI and automation

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-060 | Provider-neutral gateway with Claude adapter; keys in a vault, never in code or logs | R-015 | FR-P09-01…FR-P09-03; FR-P23-08 | H §H.9 | COVERED |  |
| TC-061 | Retrieval over approved, versioned sources with citations, jurisdiction, date, uncertainty and staleness warnings | R-010 | FR-P09-09…FR-P09-17 | H §H.6 | COVERED | NN-14. |
| TC-062 | AI features: triage, explanations, clause compare, risk checklist, drafting, task extraction, minutes, classification, OCR, translation, Q&A | R-018 | FR-P07-32; FR-P09-34…FR-P09-36; FR-P05-40…FR-P05-43; FR-P13-36 | H §H.3 | COVERED |  |
| TC-063 | Originals immutable; OCR/translation as derived, anchored, confidence-scored, correctable copies; chain of custody | R-044 | FR-P05-13…FR-P05-21 | — | COVERED | NN-09. |
| TC-064 | English plus owner-selected Indian languages first; MT labelled, versioned, reviewed | R-045 | FR-P21-65; FR-P21-75 | H §H.8 | COVERED | D-07; NN-48. |
| TC-065 | Agents: scoped tools, least privilege, approvals, prompt-injection defence, allowlists, isolation, version tracking, evaluation, kill switch | R-018 | FR-P09-19…FR-P09-26; FR-P09-37…FR-P09-47; FR-P09-56…FR-P09-60; FR-P23-56; FR-P23-57 | H §H.10–§H.12 | COVERED |  |

#### Z.3.1h Scope catalogue D — expert marketplace and Academy

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-066 | Public catalogue without a paid account; buy services, retainers, courses or subscriptions separately | R-041 | FR-P16-01; FR-P16-80 | M §M.1 | COVERED | D-11. |
| TC-067 | Service types; start with LawDocs-delivered services; third parties only after eligibility and conduct controls | R-038 | FR-P16-27; FR-P16-28 | M §M.2 | COVERED | Model M1 first (X-21). |
| TC-068 | Provider onboarding: identity, credentials, licence, practice status, geography, specialties, conflicts, insurance, terms | R-014 | FR-P01-37…FR-P01-41; FR-P16-23…FR-P16-26; FR-P16-32 | M §M.7 | COVERED | PI insurance mandatory for panel firms. |
| TC-069 | Written conduct review before listings, ratings, rankings, commissions, referral fees, reviews, discounts, per-minute advice | R-037 | FR-P16-18; FR-P16-19; FR-P17-59 | M §M.5 | COVERED | NN-21. |
| TC-070 | Proposal/SOW, SLA, payment, invoice, GST, matter room, correspondence, milestones, feedback, disputes; no outcome-based legal fees | R-039 | FR-P16-35…FR-P16-47; FR-P16-65…FR-P16-71 | M §M.9 | COVERED | CH-31. |
| TC-071 | Academy by API, deep link or catalogue feed; no scraping; entitlements preserved | R-081 | FR-P16-72…FR-P16-75 | M §M.11 | COVERED | D-16. |

#### Z.3.1i Scope catalogue E — Operations Hub

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-072 | Separate ops workspace (delivery, onboarding, support, CRM, CS, comms, billing ops, content, marketing calendar, training, after-sales); platform admin separate | R-048 | P18 | X | COVERED | D-02. |
| TC-073 | Client workspaces with scoped grants, tasks, maker/checker, files, messages, approvals, billing, time-bound access and client-visible history | R-065 | FR-P18-07…FR-P18-25; FR-P18-41…FR-P18-52 | — | COVERED |  |
| TC-074 | Employee as maker only with client authorisation; client checker; multiple makers; revocation; internal notes distinct from client-visible records | R-064 | FR-P18-11…FR-P18-18 | D §D.10 | COVERED |  |
| TC-075 | Support, grievance, email/call records and marketing engagement consent-aware; preferences, opt-outs, retention | R-050 | FR-P03-47; FR-P21-103…FR-P21-107 | X §X.2; §X.6 | COVERED | NN-34. |
| TC-076 | Cross-functional employees get scoped roles, never inherited access; separate org context; immutable audit | R-058 | FR-P02-44; FR-P02-45; FR-P18-82 | X §X.10 | COVERED |  |
| TC-077 | Brevo, M365/Teams/SharePoint and Google via adapters, OAuth, narrow scopes; no CRM/file-store duplication without a sync model | R-053 | FR-P18-84…FR-P18-87; FR-P19-65…FR-P19-68; FR-P20-33 | I §I.2 | COVERED |  |
| TC-078 | Staff lifecycle, leave, payroll with State-specific review; outcomes not covert activity; explicit payroll exports and approvals | R-052 | — | X §X.8 | COVERED | In OH10/OH11 (D-02). |

#### Z.3.1j Scope catalogue F — consumer, tax and vehicle workflows

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-079 | Each area is a later release with its own regulatory and operating review | R-083 | P14; P15 (Wave 3) | S §S.21 | COVERED |  |
| TC-080 | Loan grievance: timeline, evidence, lender's own channel, escalation eligibility, authorised submissions, user control | R-083 | FR-P15-21…FR-P15-26 | S §S.3 | COVERED |  |
| TC-081 | Insurance grievance: insurer, IRDAI, Ombudsman routes; no soliciting insurance or implied affiliation | R-083 | FR-P15-30…FR-P15-34 | S §S.5 | COVERED |  |
| TC-082 | Challan lookup/pay/contest via official or approved providers; advocates with proper authority; no custody of payment credentials | R-084 | FR-P15-49…FR-P15-55 | S §S.8 | COVERED | CH-22. |
| TC-083 | Vehicle-loan documents and sale agreements with ownership, encumbrance and registration checks; stamp and transfer caveats | R-085 | FR-P15-56…FR-P15-62; FR-P15-70 (added) | S §S.9 | COVERED | Was PARTIAL for vehicle-loan documents; fixed — see Z.6. |
| TC-084 | Individual, company and LLP tax by tax year, form, taxpayer type, practitioner review; authorised filing routes; labelled calculations | R-069 | FR-P14-45…FR-P14-66 | — | COVERED | CH-10. |
| TC-085 | Startup journey; government fees, professional fees, exclusions and timing shown separately | R-082 | FR-P14-15; FR-P14-16; FR-P14-38…FR-P14-44 | — | COVERED | NN-22. |

#### Z.3.1k Data, documents and portability

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-086 | Canonical identifiers and stable metadata independent of path, vendor and category | R-022 | FR-P00-40; FR-P20-37 | K §K.11 | COVERED | NN-12. |
| TC-087 | Separate metadata DB, object storage, search index, audit log and secrets vault; encryption, rotation, retention, hold, deletion; replaceable adapters | R-022 | FR-P00-18; FR-P00-33; FR-P00-53; FR-P04-30; FR-P04-49…FR-P04-53; FR-P18-26 | P §P.5 | COVERED |  |
| TC-088 | Guided bulk import with preview and correction; never discard unknown files or overwrite duplicates; import report and checksums | R-024 | FR-P20-25…FR-P20-29 | K §K.10 | COVERED |  |
| TC-089 | Beginner-friendly export with README, manifest, dates, hashes and clear labels; tenant-configurable structure | R-021 | FR-P20-01…FR-P20-05; FR-P20-16 | K | COVERED |  |
| TC-090 | DOCX/XLSX/PDF-A/CSV/JSON; originals and provider evidence; do not imply a PDF alone preserves certificates | R-021 | FR-P20-19…FR-P20-21 | K §K.4 | COVERED |  |
| TC-091 | User-directed export to OneDrive/SharePoint/Google Drive/object storage with explicit sync, overwrite, conflict, encryption and revoke semantics | R-021 | FR-P20-30…FR-P20-36 | — | COVERED |  |
| TC-092 | Expand-migrate-contract, backfills, rollback, schema/data versions, migration verification, restore tests | R-022 | FR-P20-38…FR-P20-43; FR-P23-17…FR-P23-19; FR-P23-33 | — | COVERED |  |

#### Z.3.1l Integrations and API architecture

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-093 | Bounded contexts and contracts first; every integration has owner, purpose, class, direction, auth, scopes, retention, failure behaviour, audit | R-002 | FR-P19-02; FR-P19-24; FR-P19-25 | I §I.4 | COVERED |  |
| TC-094 | Gateway, versioned APIs, OpenAPI, OAuth/OIDC, scopes, signed webhooks, idempotency, correlation IDs, rate limits, retries, DLQ, health | R-003 | FR-P19-01…FR-P19-23; FR-P19-78…FR-P19-82 | I §I.1 | COVERED |  |
| TC-095 | Minimal fields; discoverable, revocable, logged grants; manual fallback and export path | R-023 | FR-P19-12; FR-P19-20; FR-P19-26; FR-P19-27 | — | COVERED |  |
| TC-096 | No direct database sharing; APIs/events, mapping, tenant context, per-product service identities, contract tests | R-002 | FR-P19-02; FR-P19-08 | Y | COVERED | NN-24. |
| TC-097 | Vendor adapters (eSign, KYC, eStamp, Razorpay, MCA, courts, IP India, Graph, Drive, Claude, Jio, comms, CRM/HR) | R-003 | FR-P19-65…FR-P19-68 | I §I.2 | COVERED |  |
| TC-098 | Verify API availability, terms, pricing, residency, subprocessors, sandbox; manual workflow when no authorised API | R-003 | FR-P00-52 | I §I.15; P §P.15 | COVERED | NN-38. |

#### Z.3.1m Security, privacy, compliance and release readiness

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-099 | Practical control framework; owner, evidence and procedure per requirement; "designed for" versus "attested" | R-033 | FR-P23-40…FR-P23-46 | P §P.12–§P.13 | COVERED |  |
| TC-100 | Threat modelling, SSDLC, reviews, scanning, SAST/DAST, VAPT, remediation, access reviews, MFA/passkeys, PAM, segregation, KMS, backup/DR, IR, vendor risk, retention, BCP, audit logs, change approvals | R-057 | FR-P02-52…FR-P02-54; FR-P23-04; FR-P23-05; FR-P23-25…FR-P23-43; FR-P23-50; FR-P23-51 | P §P.2; §P.17 | COVERED |  |
| TC-101 | Verify CERT-In obligations and any RBI directions applying to a customer or LSP relationship | R-031 | FR-P18-20; FR-P19-84 | P §P.9 | COVERED | NN-27. |
| TC-102 | Strong tenant isolation; deny by default; IDOR and cross-tenant tests | R-031 | FR-P00-25…FR-P00-31 | — | COVERED | NN-01. |
| TC-103 | Maker/checker and SoD for payments, grants, exports, regulatory submissions, role elevation, critical config | R-051 | FR-P02-28…FR-P02-38 | D §D.7; §D.9 | COVERED | NN-18. |
| TC-104 | Append-only, tamper-evident history with actor, context, time, source, object, action, result; no secrets | R-067 | FR-P00-33…FR-P00-38 | P §P.7 | COVERED | NN-02, NN-32. |
| TC-105 | Hosted/tokenised checkout; signed callbacks; invoice and payment reconciliation | R-034 | FR-P17-20…FR-P17-24; FR-P17-35 | P §P.11 | COVERED | NN-22. |
| TC-106 | India residency where sector rules apply; regional choices only after transfer analysis | R-031 | FR-P00-15; FR-P20-42 | P §P.10 | COVERED | NN-25. |
| TC-107 | Incident handling: isolation, investigation, evidence, notice decisions, recovery, lessons | R-057 | FR-P23-50; FR-P23-51 | P §P.16 | COVERED |  |
| TC-108 | Policies and disclaimers as review-ready drafts, not final approvals | R-072 | FR-P21-34 | O | COVERED |  |

#### Z.3.1n Pricing and commercial model

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-109 | Three configurable plans (individual; professional/startup; company/enterprise) plus separately purchasable services and training | R-036 | FR-P17-06; FR-P17-11; FR-P21-30 | L §L.2 | COVERED | Personal, Pro, Business shown; Free and Enterprise linked. |
| TC-110 | Feature matrix states included, metered, excluded or requires a professional | R-036 | FR-P17-12 | L §L.3 | COVERED |  |
| TC-111 | Indicative prices only with evidence or owner assumptions; statutory fees separate; renewal and cancellation never hidden | R-036 | FR-P17-14; FR-P17-30 | L §L.1 | COVERED | [OWNER TO SET]; NN-22, NN-50. |
| TC-112 | Evaluate seats, storage, eSign, AI usage, templates, one-time, retainers, managed services, implementation, API/white-label, courses | R-054 | FR-P17-41; FR-P17-43 | L §L.4–§L.9 | COVERED |  |
| TC-113 | Revenue options configurable with reason, owner, effective date, disclosure, taxes, refund/credit handling and audit | R-054 | FR-P17-57; FR-P17-58; FR-P17-61 | L §L.9 | COVERED |  |
| TC-114 | No ads or confidential-data monetisation in the legal workspace by default | R-054 | FR-P17-60 | — | COVERED | NN-35. |
| TC-115 | Savings dashboard shows its calculation; measured versus estimated versus modelled; no unevidenced "penalty saved" | R-063 | FR-P17-71; FR-P17-72 | L §L.12 | COVERED | NN-36. |

#### Z.3.1o User experience, content and growth

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-116 | Clean, responsive, low-click navigation with distinct workspaces per user type | R-028 | FR-P02-55…FR-P02-57 | D | COVERED |  |
| TC-117 | Contextual "i" definitions, glossary, tutorials, diagrams, accessible screenshots, captions/transcripts, walkthroughs, short videos | R-019 | FR-P21-111…FR-P21-140 | N §N.10; §N.12 | COVERED |  |
| TC-118 | Public pages from a documented inventory and supplied Word content; owner-approved claims only; accurate labels; privacy/terms drafted for review | R-070 | FR-P21-11; FR-P21-45 | content deck; O | COVERED | NN-20. |
| TC-119 | Blog and video sections; YouTube embeds respect privacy and consent | R-074 | FR-P21-77…FR-P21-98 | — | COVERED | Privacy-enhanced, click-to-load embeds (FR-P21-94). |
| TC-120 | Technical SEO, accurate structured data, performance; private content never exposed to search engines or AI crawlers | R-032 | FR-P21-46…FR-P21-58 | N §N.7; §N.14 | COVERED | NN-31. |
| TC-121 | Measured Indian-language rollout; translations show language and review status | R-008 | FR-P21-65; FR-P21-75 | — | COVERED |  |

#### Z.3.1p Source register, phase map and definition of done

| ID | ChatGPT prompt clause | R | Pack location | Appendix | Status | Notes |
|---|---|---|---|---|---|---|
| TC-122 | Research snapshot and source register (items 8–47) as a starting point, re-checked before coding | R-004 | FR-P00-52 | Research notes R1–R6; appendix source sections | COVERED |  |
| TC-123 | ChatGPT phase map 00–11 | R-091 | Conventions §10 (P00–P23) | — | CHANGED-BY-DECISION (D-09) | Crosswalk in Z.3.2. |
| TC-124 | Definition of done for every phase | R-001 | §13 exit gate in every phase; FR-P23-52; FR-P23-58 | — | COVERED |  |
| TC-125 | Out-of-scope discoveries become backlog items or owner decisions, never silent additions | R-001 | FR-P23-58 | Q §Q.7 | COVERED |  |

### Z.3.2 Phase-map crosswalk (ChatGPT 00–11 → pack P00–P23; D-09)

| ChatGPT phase | Pack phases that deliver it | Wave | Notes |
|---|---|---|---|
| 00 Discovery, product definition and evidence base | P00 §4A (FR-P00-01…FR-P00-07), research notes R1–R6, Appendix Q | 1 | Owner decisions D-01…D-17 already taken; P00 still runs discovery of the legacy site and data. |
| 01 Secure platform foundation and tenant workspaces | P00 (tenancy, audit, events, settings heads), P01, P02, P03 | 1 | |
| 02 Document management, import, export and preservation | P04, P20 (core in Wave 1, full in Wave 2) | 1–2 | |
| 03 Contract lifecycle, negotiation, eSign and stamping | P06, P07, P08 | 1 | |
| 04 Vidhi AI, document intelligence and language support | P09 (runtime Wave 1, workforce Wave 3), P05, P06 §4G | 1–3 | |
| 05 Company LegalOps, governance, litigation and IP | P10, P11, P12, P13 | 2 | |
| 06 Plans, payments, marketplace, services and FinLegal Academy | P16, P17 | 1–2 | |
| 07 Operations Hub, CRM, client delivery and internal workforce | P18 + Appendix X (OH change requests) | 2 | CRM, marketing, staff HRMS are OH scope (D-02). |
| 08 Ecosystem APIs and external integrations | P19 (core Wave 1, full Wave 2) + Appendices I, Y | 1–2 | |
| 09 Mobile experience, accessibility, tutorials and public website | P21, P22, Appendix U | 1–3 | Accessibility is a gate in every phase (NN-28), not a late phase. |
| 10 Consumer grievances, taxation, challans and vehicle workflows | P14, P15 | 3 | Matches the prompt's "substantial later releases". |
| 11 Resilience, audit readiness, security validation and launch | P23 (re-run per wave) | each | |

---

## Z.4 Word manuals traceability (MW-001…MW-058; section level)

The four manuals (`src/Manual_Documents.md`, `Manual_Pleadings.md`, `Manual_Compliance.md`, `Manual_Start_a_Business.md`) supply the website architecture and content the owner asked the pack to reuse (R-004, R-070, R-090). Each row names the category or area, where Appendix E inventories it, which phase builds the templates or services, and where P21 and the content deck publish it. Per-document rows are in Appendix E §2–§6; eSign flags per document are governed by Appendix F §9 (X-02).

Routing rule used in every row: **documents** → P06 templates (type `TA`) or P10 Studio (type `PLD`/`PRO`); **pleadings** → P10; **compliance and start-a-business services** → P14 service definitions sold through the P16 storefront; **pages** → P21 page templates; **flagship copy** → content deck §4; **rewrite and law-correction lists** → content deck §5 and Appendix N §N.9.

### Z.4.1 Documents manual (`src/Manual_Documents.md`) — 18 categories, 134 sub-categories, 347 entries, 327 canonical documents

| ID | Manual area | Inventory (Appendix E / R5) | Build (phase FRs) | Web page / content deck | Status | Notes |
|---|---|---|---|---|---|---|
| MW-001 | Documents manual as a whole | E §2.1–§2.2 (taxonomy, codes TA/PLD/PRO, reviewer, formalities, wave); E §8 load order | P06 FR-P06-01…FR-P06-07 (taxonomy as data, one canonical template, state variants); FR-P06-54; FR-P06-55 (legal-review backlog) | FR-P21-11; FR-P21-20; FR-P21-23; FR-P21-24; content deck §5 | COVERED | Content is data, published without code release (NN-30). |
| MW-002 | D1 Deals & Agreements (10 sub-cats; 40 entries → 27 canonical) | E §2.2 D1 (duplicates with D1.4 resolved; M&A list replaced) | P06; P07 (CLM use) | FR-P21-23; content deck FP-05 (NDA) | COVERED |  |
| MW-003 | D2 Family Matters (7; 19) | E §2.2 D2; E §4.2 (court documents re-filed to pleadings) | P06; P10 FR-P10-01 | FR-P21-20 | COVERED | Outdated CrPC/IPC citations corrected (E content code OL). |
| MW-004 | D3 Financial Transactions (13; 56 → 52) | E §2.2 D3 (bonds canonical) | P06 | FR-P21-23 | COVERED | Promissory notes and most negotiable instruments flagged not eSign-eligible (F §9). |
| MW-005 | D4 Operations & Management (8; 43) | E §2.2 D4 (AoA, SHA, LLP agreement, partnership deed, trusts) | P06; P13 (board resolutions); P14 (service cross-links) | content deck FP-07 (Partnership Deed) | COVERED |  |
| MW-006 | D5 Planning & Execution (8; 1 live / 7 upcoming; 8) | E §2.2 D5; E §3 (proposed starter documents) | P06; P14 FR-P14-40 (founder documents) | content deck FP-08 (Founders' Agreement) | PARTIAL | Seven upcoming sub-categories depend on [OWNER] approval of E §3 starter lists; held noindex until then (FR-P21-12, FR-P21-58). |
| MW-007 | D6 Marketing & Sales (9; 1 live / 8 upcoming; 2) | E §2.2 D6; E §3 | P06 | FR-P21-12 (HOLD) | PARTIAL | Same dependency on E §3 [OWNER]. |
| MW-008 | D7 Industries (upcoming; 9; 5) | E §2.2 D7; E §3 | P06 | FR-P21-12 (HOLD) | PARTIAL | Same dependency on E §3 [OWNER]. |
| MW-009 | D8 Intellectual Property Rights (3; 11) | E §2.2 D8 | P06; P12 FR-P12-32…FR-P12-34 (IP agreements, recordal) | content deck FP-13 | COVERED | Assignment/licence documents cross-linked to S2 services. |
| MW-010 | D9 IT and Websites (8; 4) | E §2.2 D9; E §3 | P06 | FR-P21-23 | COVERED | Website policy templates rebuilt on DPDP (R5 §5). |
| MW-011 | D10 HR and Service (11; 24) | E §2.2 D10 | P06; P13 FR-P13-54 (HR documents from templates); FR-P08-29 (bulk signing) | content deck FP-06 (Offer and Appointment Letter) | COVERED | Labour Codes citations (R5 §5). |
| MW-012 | D11 Legal (12; 39 → 37) | E §2.2 D11; E §4.2 (consumer, motor-vehicle court documents re-filed) | P06; P10 FR-P10-17…FR-P10-22 (notices); P15 (motor vehicles) | content deck FP-09 (Legal Notice) | COVERED | Affidavits route to notary/oath (FR-P10-35; X-02). |
| MW-013 | D12 Property Transactions (8; 43) | E §2.2 D12 | P06 FR-P06-07 (state variants); P08 FR-P08-37 (stamp-duty calculator) | content deck FP-02 (Rent/Lease), FP-03 (Agreement to Sell) | COVERED | Registration and stamp formalities gate (NN-08, NN-40). |
| MW-014 | D13 RERA (3; 1) | E §2.2 D13; E §4.2 (PL-PRP-05 RERA complaint) | P06; P10 | FR-P21-23 | COVERED |  |
| MW-015 | D14 SEBI (upcoming; 3; 0) | E §2.2 D14; E §3 | P06; LDC for regulated-entity work (FR-P14-69) | FR-P21-12 (HOLD) | PARTIAL | No documents in the manual; E §3 starter list [OWNER]; LODR policy packs replace the retired listing-agreement templates (R5 §5). |
| MW-016 | D15 Secretarial (upcoming; 9; 0) | E §2.2 D15; E §3 | P06; P13 FR-P13-36…FR-P13-39 | FR-P21-12 (HOLD) | PARTIAL | Starter list [OWNER]; governance kernel supplies minutes/resolution templates. |
| MW-017 | D16 Students (3; 17 → 16) | E §2.2 D16 | P06 | FR-P21-23 | COVERED |  |
| MW-018 | D17 Succession and Inheritance (6; 35) | E §2.2 D17 | P06 FR-P06-43 (wet-ink pack); P08 FR-P08-08…FR-P08-12 | FR-P21-36 (eSign eligibility badge) | COVERED | Wills excluded from eSign (NN-07). |
| MW-019 | D18 Accounting & Tax (upcoming; 4; 0) | E §2.2 D18; E §3 | P06; P14 FR-P14-45…FR-P14-58 | FR-P21-12 (HOLD) | PARTIAL | Starter list [OWNER]; Income-tax Act 2025 terminology (FR-P14-65). |
| MW-020 | Documents: eSign validity flags in the manual-derived inventory | E §2 eligibility column; F §9 corrections | P08 FR-P08-08…FR-P08-12 | FR-P21-36; content deck §3.8 (GB-08) | COVERED | F §9 supersedes the R5 CSV flags (X-02). |
| MW-021 | Documents: duplicates, mis-filing and heading typos | E §2.2 aliases (301 to canonical); R5 §3 | FR-P00-75 (redirect map as data) | FR-P21-10; FR-P21-53 | COVERED |  |

### Z.4.2 Pleadings manual (`src/Manual_Pleadings.md`) — 13 areas, 89 drafts → 64 canonical + 6 imported = 70 Studio pages (X-23)

| ID | Manual area | Inventory (Appendix E / R5) | Build (phase FRs) | Web page / content deck | Status | Notes |
|---|---|---|---|---|---|---|
| MW-022 | Pleadings manual as a whole | E §4 | P10 FR-P10-01…FR-P10-04 (library, variants as toggles, new-law mapping, commissioned gaps); FR-P10-05…FR-P10-09 (court render profiles) | FR-P21-21 (pleading page) | COVERED |  |
| MW-023 | P1 Civil Pleadings (14 canonical) | E §4.1 PL-CIV | P10 FR-P10-10…FR-P10-16 (interview, forum, limitation prompts) | FR-P21-21 | COVERED |  |
| MW-024 | P2 Family Law Pleadings (15 + PL-FAM-16 imported) | E §4.1 PL-FAM; §4.2 | P10; FR-P10-23…FR-P10-25 (party-in-person mode) | FR-P21-21 | COVERED | RCR, judicial separation, nullity and mutual-consent clusters merged. |
| MW-025 | P3 Succession and Inheritance (3) | E §4.1 PL-SUC | P10 | FR-P21-21 | COVERED |  |
| MW-026 | P4 Criminal Law Pleadings (9 + PL-CRM-10 imported) | E §4.1 PL-CRM (all PLD*, advocate review) | P10 FR-P10-25 (area restrictions); FR-P10-33 | FR-P21-21 | COVERED | BNSS/BNS mapping (R5 §5). |
| MW-027 | P5 Rent & Property (4 + PL-PRP-05 imported) | E §4.1 PL-PRP | P10 | FR-P21-21 | COVERED |  |
| MW-028 | P6 Consumer Law (1 + PL-CON-02/03 imported) | E §4.1 PL-CON; §4.2 | P10; P15 FR-P15-35; FR-P15-36 (e-Jagriti pack) | FR-P21-21 | COVERED | Re-filed DV complaint; CPA 2019 Commissions. |
| MW-029 | P7 Cheque Bounce Matters (2) | E §4.1 PL-CHQ | P10 FR-P10-18 (s.138 timeline helper) | content deck FP-09 | COVERED |  |
| MW-030 | P8 Suit for Damages (8) | E §4.1 PL-DMG | P10 | FR-P21-21 | COVERED |  |
| MW-031 | P9 Money Recovery & Financial Matters (5) | E §4.1 PL-MNY | P10; P11 FR-P11-70…FR-P11-72 (recovery suite) | FR-P21-21 | COVERED | Commercial Courts Act s.12A paragraph added. |
| MW-032 | P10 Alternative Dispute Resolution (0 drafts; hub kept) | E §4.3 PL-ADR-01…03 | P10 FR-P10-04; FR-P10-38 (Equator cross-link) | FR-P21-21 | PARTIAL | Drafts promised by the manual intro are commissioned [OWNER]; hub makes no promise until published (NN-20). |
| MW-033 | P11 Intellectual Property Rights (2) | E §4.1 PL-IPR | P10; P12 FR-P12-29 | FR-P21-21 | COVERED |  |
| MW-034 | P12 Corporate Law (manual drafts were consumer complaints; merged) | E §4.1 note; §4.3 PL-CRP-01…04 (NCLT set) | P10 FR-P10-04 | FR-P21-21 | PARTIAL | NCLT drafts commissioned for Wave 3 [OWNER]. |
| MW-035 | P13 MACT & Insurance (1 + PL-INS-02 imported) | E §4.1 PL-INS; §4.2 | P10; P15 FR-P15-30…FR-P15-34 | FR-P21-21 | COVERED |  |
| MW-036 | Pleadings promised but absent (Constitutional writ, Energy) | E §4.3 PL-CON-04, PL-ENG-01 | P10 FR-P10-04 | — | PARTIAL | Commissioned [OWNER]; advocate-only skeleton for writs. |
| MW-037 | Pleadings: annexures with type copies of handwritten and WhatsApp evidence | E §4 (type copy flag) | P05 FR-P05-22; P10 FR-P10-26…FR-P10-29 | — | COVERED | CH-28. |

### Z.4.3 Compliance manual (`src/Manual_Compliance.md`) — 7 groups, 22 services

| ID | Manual area | Inventory (Appendix E / R5) | Build (phase FRs) | Web page / content deck | Status | Notes |
|---|---|---|---|---|---|---|
| MW-038 | Compliance manual as a whole | E §5 | P14 FR-P14-01…FR-P14-04 (service definition, groups, market corrections, no copied text); P16 storefront | FR-P21-22 (service page); content deck §5.3 | COVERED |  |
| MW-039 | C1 ROC Compliances (3 services) | E §5 C1.1–C1.3 | P14 FR-P14-25…FR-P14-36; P13 (governance facts) | FR-P21-22 | COVERED | MCA V3 forms check [VERIFY]. |
| MW-040 | C2 Closure of Business (3) | E §5 C2.1–C2.3 | P14 | FR-P21-22 | COVERED | Wikipedia/LegalWiz text rewritten (R5 §4 rows 1–2). |
| MW-041 | C3 GST (2) | E §5 C3.1–C3.2 | P14 FR-P14-56 (GST returns via GSP and practitioner) | FR-P21-22 | COVERED | GSTR-2/3 references replaced (R5 §5). |
| MW-042 | C4 Taxation (3) | E §5 C4.1–C4.3 | P14 FR-P14-45…FR-P14-57; FR-P14-63…FR-P14-66 | FR-P21-22 | COVERED | Vakilsearch/Corpbiz text rewritten; Income-tax Act 2025 dual-cite. |
| MW-043 | C5 Accounting (2) | E §5 C5.1–C5.2 | P14 | FR-P21-22 | COVERED | Provenience FAQ accordion rewritten. |
| MW-044 | C6 Labour Law Compliances (4) | E §5 C6.1–C6.4 | P14; P13 FR-P13-55…FR-P13-57 (labour rulepack) | FR-P21-22 | COVERED | Four Labour Codes citations. |
| MW-045 | C7 Audit (5) | E §5 C7.1–C7.5 | P14 FR-P14-20; FR-P14-21 (attest functions by independent practitioners) | FR-P21-22 | COVERED | Re-scoped GST audit page; NN-41. |
| MW-046 | Compliance: copied third-party text and the "StartupSeven" mention | E §5 content codes (CP) | FR-P14-04; FR-P21-62 | content deck §5.3 | COVERED | X-24 adds Compliance manual l.1060 to the rewrite list. |
| MW-047 | Compliance: unattributed "customer experiences" testimonials | E §5 | FR-P21-38; FR-P21-45 | content deck §5.5 | COVERED | Removed; NN-49, NN-20. |

### Z.4.4 Start a Business manual (`src/Manual_Start_a_Business.md`) — 6 groups, 26 services

| ID | Manual area | Inventory (Appendix E / R5) | Build (phase FRs) | Web page / content deck | Status | Notes |
|---|---|---|---|---|---|---|
| MW-048 | Start a Business manual as a whole | E §6 | P14 FR-P14-01…FR-P14-37; FR-P14-38…FR-P14-44 (Startup Desk) | FR-P21-22; FR-P21-31; content deck FP-08 | COVERED |  |
| MW-049 | S1 Incorporate your Business (6) | E §6 S1.1–S1.6 | P14 FR-P14-05…FR-P14-08 (entity chooser, eligibility); FR-P14-14 (DSC) | FR-P21-31 | COVERED | "PLC" label corrected to "Pvt Ltd"; OPC 2021 and Nidhi 2022 updates. |
| MW-050 | S2 Protect your Intellectual Property (5) | E §6 S2.1–S2.5 | P12 FR-P12-13…FR-P12-19 (clearance, TM-A data sheet, filing support); P14 | content deck FP-13 | COVERED | LegalRaasta/ebizfiling/Wikipedia text rewritten. |
| MW-051 | S3 Get a License (2) | E §6 S3.1–S3.2 | P14 FR-P14-36 (renewals and periodic duties) | FR-P21-22 | COVERED |  |
| MW-052 | S4 Registrations for Business (6) | E §6 S4.1–S4.6 | P14 | FR-P21-22 | COVERED | Udyog Aadhaar replaced by Udyam with 2025 limits. |
| MW-053 | S5 Quality certification (4) | E §6 S5.1–S5.4 | P14 | FR-P21-22 | COVERED | Hallmark dates corrected; ISO is certification-body work, not a registry. |
| MW-054 | S6 NGO and Society Registration (3) | E §6 S6.1–S6.3 | P14; P06 (trust deed, by-laws) | FR-P21-22 | COVERED | Trust deeds not eSign-eligible (NN-07). |

### Z.4.5 Cross-manual items

| ID | Manual area | Inventory (Appendix E / R5) | Build (phase FRs) | Web page / content deck | Status | Notes |
|---|---|---|---|---|---|---|
| MW-055 | Owner one-liners (131 document + 48 service lines) | R5 §6 | FR-P21-43 | N §N.2; content deck §2.7–§2.8 | COVERED | Non-original quotation replaced (R5 §3.1). |
| MW-056 | Outdated law across all manuals | R5 §5; E content code OL | FR-P10-03; FR-P14-63…FR-P14-66; FR-P21-61 (outdated-law linter) | content deck §5.4 | COVERED |  |
| MW-057 | Placeholder and template FAQs | R5 §3.2 | FR-P21-39 | N §N.4; content deck §6 (72-question bank) | COVERED |  |
| MW-058 | Live-site trees not covered by any manual (`/regulated-entities/*`) | R5 §2 | FR-P00-77; FR-P21-11 | content deck §5.1 | COVERED | ≈ 50 pages carried from the live sitemap. |

---

## Z.5 PARTIAL and MISSING register with recommended fixes

Rows still PARTIAL after the review, and rows that were PARTIAL or MISSING before it. "Owner of fix" is who acts; "Where" is the file and section that should change.

| Row | Gap | Status now | Recommended fix | Where | Owner of fix |
|---|---|---|---|---|---|
| TM-002 | No DOCX rendition of the pack existed at review. | COVERED (registry review G4) | Applied: Word editions now exist in the pack root, `condensed/` and `content/`. Original fix: at assembly, render `01`, `02`, P00–P23 and the appendices to DOCX (one combined file with a navigable table of contents, plus one DOCX per phase), using the pack styles; check that wide tables (this appendix, Appendices R, L, M) wrap without truncation. | Pack root: `LawDocs_Build_Prompt_Pack_v1.0.docx` and `condensed/` | Pack lead |
| TM-003 | `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` were cited by every phase header but not yet written at review. | COVERED (registry review G4) | Applied: both files now exist in the pack root. Original fix: write `01` (role, operating rules including FR-P23-58, §18 precedence carrying X-01…X-30, §19 companion change requests) and `02` (§3 CH register, decision log D-01…D-17, §8 R-001…R-092 linking to §Z.7 of this appendix). | Pack root | Pack lead |
| TM-296 | JioCX endpoint, authentication, delivery-report and error pages are behind a developer sign-up and were not read (R4 D-R4-01). | PARTIAL | Close OI-R4-01: open a developer.jiocx.com account, read auth, DLR/webhook and error pages, confirm HMAC and India processing; then complete the adapter rows in J §J.3 and I §I.12 and record the verification-log entry before any `ntf.jiocx.*` flag is turned ON (NN-38). | Appendix J §J.3, §J.11; Appendix I §I.12 | Integration lead |
| TM-380 | Before review only hypothecation removal (FR-P15-60) and generic loan grievances touched vehicle loans; no vehicle-loan journey, repossession routing or DSA/LSP exclusion. | COVERED | Applied: FR-P15-70 "Vehicle-loan journeys" (loan papers on the `veh_` record, closure via FR-P15-60, repossession complaints to the vertical A playbook, formalities block on hypothecated sales, no loan sourcing). | P15 §4N (end of §4) | Done at review |
| TC-007 | No phase required a pre-implementation proposal (scope, dependencies, risks, acceptance) before material work. | COVERED | Applied: FR-P23-58 requires the proposal as an ADR or change record and owner approval at the gate. | P23 §4N (end of §4) | Done at review |
| TC-009 | Phase exit gates existed, but no standard end-of-phase report or rule against claiming unproven test, legal-check or deployment success. | COVERED | Applied: FR-P23-58 "Phase completion report" (`docs/phases/Pxx-completion-report.md`; evidence-linked results; checker `PLT_RELEASE_MANAGER`; wave go-live requires approved reports). | P23 §4N (end of §4) | Done at review |
| TC-040 | No phase stated that LawDocs is not a regulated entity or LSP and must not perform lending, sourcing, referral or collection activities. | COVERED | Applied: FR-P19-84 "Regulatory-role boundary for lending" (no lending-adjacent activity; client RE duties mapped in P13/P18/LDC; any such feature needs counsel opinion and owner approval; egress block). | P19 §4P (end of §4) | Done at review |
| TC-083 | Vehicle-loan documents had no explicit handling (sale-side checks were complete). | COVERED | Applied: FR-P15-70 (as above). | P15 §4N | Done at review |
| MW-006 | Seven upcoming sub-categories have no document list in the manual. | PARTIAL | Approve the Appendix E §3 starter lists; P06 opens content-backlog items (FR-P06-54) per approved document; P21 publishes in Wave 3 and keeps the hubs `noindex` until then (FR-P21-12, FR-P21-58). | Appendix E §3; P06 backlog; P21 Wave 3 | Owner, then `PLT_CONTENT_EDITOR` |
| MW-007 | Eight upcoming sub-categories without lists. | PARTIAL | As for MW-006. | Appendix E §3 | Owner |
| MW-008 | Nine upcoming sub-categories without lists. | PARTIAL | As for MW-006. | Appendix E §3 | Owner |
| MW-015 | Category has no documents in the manual. | PARTIAL | Approve the E §3 starter list; prefer LODR policy packs (Reg 23, 30, 46) and route regulated-entity work to LDC listings (FR-P14-69). | Appendix E §3; P06 | Owner |
| MW-016 | Category has no documents in the manual. | PARTIAL | Approve the E §3 starter list; reuse governance-kernel minutes and resolution templates (P13 FR-P13-36, FR-P13-37). | Appendix E §3; P06; P13 | Owner |
| MW-019 | Category has no documents in the manual. | PARTIAL | Approve the E §3 starter list; align terminology with the Income-tax Act 2025 (P14 FR-P14-65). | Appendix E §3; P06; P14 | Owner |
| MW-032 | Manual intro promises ADR drafts; none exist. | PARTIAL | Approve commissioning PL-ADR-01…03 (E §4.3); P10 FR-P10-04 tracks them; hub stays promise-free until published (NN-20). | Appendix E §4.3; P10 | Owner, then `PLT_LEGAL_REVIEWER` |
| MW-034 | No real corporate (NCLT) pleadings in the manual. | PARTIAL | Approve commissioning PL-CRP-01…04 for Wave 3. | Appendix E §4.3; P10 | Owner |
| MW-036 | Constitutional (writ) and Energy drafts promised, not drafted. | PARTIAL | Approve commissioning PL-CON-04 (advocate-only skeleton) and PL-ENG-01. | Appendix E §4.3; P10 | Owner |

## Z.6 Edits applied at traceability review

Each edit is one paragraph, sits at the end of the owning phase's §4 with the next free FR number, and is tagged "(added at traceability review)". No existing FR was renumbered or changed.

| New FR | File | Placement | Closes rows | Summary |
|---|---|---|---|---|
| FR-P15-70 Vehicle-loan journeys | `phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md` | §4N, after FR-P15-69 | TM-380, TC-083 | Vehicle-loan papers filed on the `veh_` record and vault view `06 Vehicles`; closure via FR-P15-60; repossession and recovery-conduct complaints routed to the vertical A playbook with self-file-first; NN-40 block on executing a sale of a hypothecated vehicle until NOC/Form 35 is recorded or waived; no loan sourcing, comparison, referral or DSA/LSP activity; help key `hlp.chp.vehicle_loan`. |
| FR-P19-84 Regulatory-role boundary for lending | `phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | §4P, after FR-P19-83 | TC-040 | LawDocs is not an RE, LSP, DSA/DMA, recovery agent or credit-information user and performs none of their activities; tenant RE obligations mapped in P13/P18 and LDC; any lending-adjacent feature needs a counsel opinion and owner approval under FR-P17-57/58 before a flag exists; egress policy keeps lender-lead and bureau endpoints blocked. |
| FR-P23-58 Phase completion report | `phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md` | §4N, after FR-P23-57 | TC-007, TC-009 | Standard report per phase (FR status, changes, migrations, tests with evidence links, NN status, risks, owner/counsel decisions, open [VERIFY], backlog, next phase); no success claim without linked evidence; pre-implementation proposal as ADR/change record; `PLT_RELEASE_MANAGER` checker; wave go-live needs approved reports. |

**Follow-ups for the owning phase authors** (not applied here because they touch more than one paragraph): add Gherkin scenarios `@P15-AT-nn` (hypothecated vehicle sale blocked from "Executed" until NOC/Form 35 recorded) and `@P19-AT-nn` (no adapter in the connector catalogue can be registered against a lender-lead or bureau endpoint), register `hlp.chp.vehicle_loan` in P21's glossary registry, and add the completion-report template to P00 FR-P00-90 `docs/` structure.

---

## Z.7 Requirement-ID index (R-xxx → rows)

| R | Rows (TM = owner brief; TC = ChatGPT prompt) |
|---|---|
| R-001 | TM-005…TM-006, TM-008…TM-009, TC-001…TC-002, TC-005…TC-007, TC-009, TC-019, TC-124…TC-125 |
| R-002 | TM-010…TM-011, TM-018…TM-020, TM-023, TC-012…TC-014, TC-040, TC-093, TC-096 |
| R-003 | TM-021…TM-022, TC-094, TC-097…TC-098 |
| R-004 | TM-001…TM-004, TM-024…TM-025, TC-004, TC-033, TC-122 |
| R-005 | TM-027…TM-031, TM-122…TM-125, TC-024…TC-025, TC-038, TC-047 |
| R-006 | TM-012, TM-032…TM-033, TC-021, TC-023, TC-037, TC-049 |
| R-007 | TM-014, TM-034, TM-038 |
| R-008 | TM-035, TC-121 |
| R-009 | TM-036…TM-037, TC-022 |
| R-010 | TM-039, TC-061 |
| R-011 | TM-040…TM-046, TC-016 |
| R-012 | TM-047…TM-049, TC-027, TC-056 |
| R-013 | TM-050…TM-051, TC-057 |
| R-014 | TM-052…TM-055, TC-068 |
| R-015 | TM-056, TM-200, TC-060 |
| R-016 | TM-057…TM-058 |
| R-017 | TM-013, TM-059…TM-060, TC-010…TC-011 |
| R-018 | TM-061…TM-066, TC-028, TC-062, TC-065 |
| R-019 | TM-067…TM-068, TC-018, TC-117 |
| R-020 | TM-069…TM-074 |
| R-021 | TM-075…TM-087, TC-089…TC-091 |
| R-022 | TM-088…TM-094, TC-008, TC-086…TC-087, TC-092 |
| R-023 | TM-095…TM-096, TC-095 |
| R-024 | TM-097…TM-098, TC-088 |
| R-025 | TM-099…TM-101, TC-044 |
| R-026 | TM-102…TM-103, TM-111, TC-017 |
| R-027 | TM-104 |
| R-028 | TM-105…TM-110, TC-053, TC-116 |
| R-029 | TM-112…TM-118, TC-045 |
| R-030 | TM-119…TM-121 |
| R-031 | TM-126…TM-129, TC-039, TC-101…TC-102, TC-106 |
| R-032 | TM-130…TM-133, TM-385, TM-391, TC-120 |
| R-033 | TM-134…TM-139, TC-031, TC-099 |
| R-034 | TM-140…TM-141, TC-105 |
| R-035 | TM-142…TM-144 |
| R-036 | TM-145…TM-150, TC-109…TC-111 |
| R-037 | TM-015, TM-151…TM-158, TM-169, TC-043, TC-069 |
| R-038 | TM-160…TM-168, TC-067 |
| R-039 | TM-170…TM-172, TC-070 |
| R-040 | TM-173…TM-179, TC-051 |
| R-041 | TM-180…TM-183, TC-066 |
| R-042 | TM-184…TM-187 |
| R-043 | TM-188…TM-192, TC-048 |
| R-044 | TM-193…TM-196, TC-063 |
| R-045 | TM-197…TM-199, TC-064 |
| R-046 | TM-201, TC-034 |
| R-047 | TM-202…TM-208, TC-035, TC-058 |
| R-048 | TM-209…TM-217, TM-329, TC-072 |
| R-049 | TM-159, TM-218 |
| R-050 | TM-219…TM-225, TC-075 |
| R-051 | TM-226…TM-233, TC-103 |
| R-052 | TM-234…TM-241, TC-032, TC-078 |
| R-053 | TM-242…TM-249, TC-077 |
| R-054 | TM-251…TM-257, TC-030, TC-112…TC-114 |
| R-055 | TM-250 |
| R-056 | TM-258…TM-265 |
| R-057 | TM-266…TM-272, TC-100, TC-107 |
| R-058 | TM-273…TM-276, TC-015, TC-029, TC-076 |
| R-059 | TM-277…TM-285, TC-055, TC-059 |
| R-060 | TM-286…TM-287, TC-020 |
| R-061 | TM-288…TM-290 |
| R-062 | TM-291…TM-296 |
| R-063 | TM-297…TM-301, TC-115 |
| R-064 | TM-302…TM-309, TC-074 |
| R-065 | TM-310…TM-319, TC-026, TC-073 |
| R-066 | TM-320…TM-322 |
| R-067 | TM-323, TC-041, TC-104 |
| R-068 | TM-324…TM-325 |
| R-069 | TM-326…TM-328, TC-084 |
| R-070 | TM-330…TM-334, TC-118 |
| R-071 | TM-007, TM-335…TM-336 |
| R-072 | TM-337…TM-340, TC-036, TC-108 |
| R-073 | TM-341…TM-342 |
| R-074 | TM-343, TC-119 |
| R-075 | TM-344 |
| R-076 | TM-345 |
| R-077 | TM-346…TM-350, TC-050, TC-054 |
| R-078 | TM-351…TM-354 |
| R-079 | TM-355, TC-052 |
| R-080 | TM-016…TM-017, TM-356 |
| R-081 | TM-357…TM-358, TC-071 |
| R-082 | TM-359…TM-363, TC-085 |
| R-083 | TM-364…TM-373, TC-042, TC-079…TC-081 |
| R-084 | TM-374…TM-377, TC-082 |
| R-085 | TM-378…TM-381, TC-083 |
| R-086 | TM-382…TM-384, TC-046 |
| R-087 | TM-392…TM-394 |
| R-088 | TM-395…TM-396 |
| R-089 | TM-397 |
| R-090 | TM-026, TM-387…TM-390 |
| R-091 | TM-398, TC-123 |
| R-092 | TM-386, TC-003 |

---

## Z.8 Maintenance rules

1. **Same pull request.** A change that adds, removes, renumbers or materially narrows an FR updates the rows here that cite it. A CI job `trace:check` [REC: P23 author to add it to the PR checks under FR-P23-04] fails when a cited `FR-Pxx-nn` no longer exists in the phase files or when an R-xxx in conventions §11 has no row.
2. **Status changes need a reason.** Moving a row to CHANGED-BY-DECISION requires a D-, CH- or NN- reference recorded in `02`; moving a row to COVERED from PARTIAL or MISSING cites the FR that closed it.
3. **New owner asks.** Any later owner instruction is split into atomic rows here (next free TM number) before the phase work starts, with a new R-xxx in `02` §8 if no existing ID fits.
4. **Wave gates.** At each wave go-live (P23 FR-P23-52) `PLT_RELEASE_MANAGER` confirms that every row whose FRs belong to the wave is COVERED or CHANGED-BY-DECISION, or carries an approved deferral in Appendix W.
5. **Open items raised by this review** (candidates for Appendix W): OI candidate "DOCX and master files at assembly" (pack lead) — **closed at registry review G4** (files exist; TM-002/TM-003 COVERED); OI-R4-01 (existing, Jio developer pages); OI candidate "Appendix E §3 starter lists for D5, D6, D7, D14, D15, D18" ([OWNER]); OI candidate "commissioned pleadings PL-ADR-01…03, PL-CRP-01…04, PL-CON-04, PL-ENG-01" ([OWNER]); OI candidate "Gherkin and help-key follow-ups for FR-P15-70, FR-P19-84, FR-P23-58" (phase authors) — Gherkin and `hlp.chp.vehicle_loan` done (Appendix V §V.8; P21); the completion-report template in P00 FR-P00-90 `docs/` structure remains with P00.
