# Phase P07 — Policy Lifecycle and Document Management System

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, object storage with SSE-KMS, versioning and Object Lock, outbox);
> - **P01** (identity, step-up MFA, external-party identities for signers and share recipients, ABAC attributes `confidentiality_class`, `department_id`);
> - **P02** (settings registry, retention-class rule packs, terminology, custom metadata);
> - **P04** (tasks, approvals, calendar, Notifications; evidence linkage to compliance instances);
> - **P06** (Board/committee approval of policies through agenda items and decisions; SDD writes for UPSI sharing).
>
> **Sequencing:** the DMS core (§4H–§4M, §4S, §4W) is a platform service and is built **first, in P07 sprint 1–3, before P06 needs it**; the policy lifecycle follows. P17 (Vidhi) provides the model adapters for drafting, OCR of handwriting and translation; P07 owns the document pipeline, UX and storage. P18 delivers the storage and eSign adapters; P19 consumes the folder taxonomy for export and bring-your-own storage.
>
> **Binding appendices:** A (state machines), B (data model), C (screens), K (Vidhi — drafting, vision, translation guardrails), L (eSign, storage, Microsoft 365/Google adapters), M (LDC-EXPORT-1.0 folder taxonomy — the DMS folder tree mirrors it), Q (security), U (settings).
>
> **Requirements covered:** R-091, R-038, R-021 (folder intake, preserved structure), R-027 (reads documents, screenshots, WhatsApp chats, PDFs, letters, e-mail; eSign where required), R-043, R-076, R-081, R-082; contributes to R-013 (evidence), R-017, R-053.
>
> **Estimated effort:** 9 two-week sprints *(v1.1: +1 for §4Y)*, squad of 8 (DMS core 3, policy lifecycle 2, document intelligence 2, eSign and sharing 1), plus a part-time legal-drafting analyst for model templates and UAT.
>
> **v1.1 changes (25 October 2026)**
> - New §4Y (FR-P07-54 – FR-P07-70): baton tracker and parallel review lanes (IMP-064, IMP-065); policy–practice drift detection (IMP-066); attestation campaigns with quizzes, reminders and department dashboards (IMP-067); AI extraction on policy upload proposing owner, review cycle and control links (IMP-068); progressive rendering and text-layer checks (IMP-069); one-click "policy pack" for a newly adopted direction; bulk review-date roll-forward with undo (NN-49); model-template forms library (customer onboarding individual and non-individual, KYC checklists, DPDP consent, grievance and incident forms) as compliance-owned templates — data capture stays in Finbyx/Udofin (NN-23); jurisdiction-aware policies for foreign subsidiaries (official-language original + reviewed translation, NN-54); Policy Drafter agent (VA-05) and Board Pack Agent hand-offs under autonomy levels (NN-50).
> - DMS: contract repository hand-off to P26 (CLM), litigation privilege tags reused by P26, document classes for ESG evidence (P27).
> - New screens SCR-POL-12 – SCR-POL-16 and SCR-DMS-16 – SCR-DMS-17, tables, settings, Gherkin scenarios and open items OI-P07-12 – OI-P07-17.

---

## 1. Objective and business outcome

Regulated entities run on documents: board-approved policies that must be reviewed on time, evidence that proves each compliance, signed agreements, scanned letters from regulators, WhatsApp screenshots of customer complaints, handwritten registers in a branch. P07 gives LawDocsComply one governed document layer and one policy lifecycle, so that (a) every policy is drafted from the right model, redlined against its last approved version in real Word tracked changes, approved by the right body and evidenced by the signed copy; and (b) every document in the platform is stored once, found in seconds, shared selectively, signed lawfully, read by OCR and translated where needed, retained for as long as the law requires and exported in a folder structure a beginner can understand.

| Outcome | Exit-gate measure |
|---|---|
| Policies never silently lapse | Every policy has an owner, approver body, effective date and next-review date; an overdue review opens a compliance issue on day +1; dashboard shows 100% of policies with a computed status |
| Real tracked changes | A Vidhi-assisted revision of a 40-page KYC policy opens in Microsoft Word with every change as a native tracked insertion/deletion attributed to "Vidhi AI (draft)" and a comment citing the regulatory clause or model clause behind it; accepting all changes in Word yields exactly the approved text |
| Approval evidenced | A policy cannot move to `EFFECTIVE` without a P06 decision reference and an uploaded signed or certified copy (PDF); the system compares the scanned copy with the approved text and flags material differences |
| Attestations measured | Acknowledgement campaigns reach the HRMS-derived audience with reminders; completion rate and defaulters are reportable per department |
| Find anything fast | Permission-trimmed full-text and metadata search returns results in ≤ 1.5 s at p95 on 1 million documents per tenant, including OCR text of scans |
| Selective, controlled sharing | A user can assemble a share pack choosing exactly which documents to include, with view-only, watermark, expiry and OTP; every open is logged; revocation takes effect within 60 s |
| Lawful e-signature | Aadhaar eSign (through CCA-empanelled ESPs) and DSC flows complete with a certificate of completion; documents excluded by the IT Act First Schedule are blocked from e-signature with an explanation |
| Handwriting and screenshots usable | Handwritten letters, WhatsApp screenshots and photographed registers produce an editable type copy side by side with the original, with low-confidence words highlighted; the verified type copy and the original are attached together to the record |
| Translation | Documents in any of the six UN official languages or the 22 Eighth Schedule languages are detected and translated into English with segment alignment and confidence, labelled machine translation until reviewed |
| Folder intake | A 5,000-file folder tree is uploaded in one action with a mapping preview, duplicate detection and a commit report; nothing is overwritten |
| Structure survives releases | Canonical document paths are derived from metadata and the LDC-EXPORT-1.0 taxonomy (Appendix M), not from code; a schema release changes no customer-visible path (NN-10, NN-11) |

---

## 2. Scope (in / out)

**In scope — Policy lifecycle**

- Policy register, required-policy catalogue per entity (from the P06 Governance Blueprint and P03/P15 content packs), gap list.
- Model templates (platform, by entity family and regulator) and tenant templates (house style), with clause-to-obligation citation maps.
- Vidhi-assisted drafting: new from model, alignment to the previous version, alignment to a regulatory change, gap check against mandatory contents.
- Deterministic redline engine producing native OOXML tracked changes and comments.
- Review and approval workflow, Board/committee approval via P06, signed-copy evidence, publication, attestations and acknowledgements, review calendar, versions, superseded and retired policies, policy-to-control-to-obligation mapping.

**In scope — Document management**

- Repository with metadata-driven canonical paths mirroring LDC-EXPORT-1.0; virtual folders and saved searches; records linkage (one document, many records).
- Versioning, check-in/check-out, locks, compare.
- Office editing: desktop round-trip; Microsoft 365 co-authoring when the tenant connects SharePoint/OneDrive; optional embedded WOPI-compatible editor (flag).
- Search (full text including OCR, facets, filters, saved searches; semantic search through P17).
- Selective sharing (internal and external), share packs, view-only viewer, watermarking, expiry, OTP, revocation.
- eSign envelopes: Aadhaar eSign through CCA-empanelled ESPs (via application-service-provider adapters), DSC, simple electronic acknowledgement; certificate of completion.
- Document intelligence: OCR (printed, handwriting), WhatsApp/chat screenshot extraction, e-mail parsing, type copies with human verification, translation to English.
- Retention classes, legal hold, disposal with approval; WORM sealing.
- Folder/zip intake with mapping preview; connector intake; e-mail-in.
- Malware scanning, active-content stripping, prompt-injection screening.
- Document generation services (DOCX/PDF/PDF-A) used by every module.

**Out of scope**

- Contract lifecycle management and agreement drafting for counterparties beyond policies and internal documents — handed to LawDocs (lawdocs.in) through P18; P07 stores and signs the resulting documents.
- Board meeting management (P06) — P07 supplies pack PDFs and signatures.
- Records owned by Finbyx/Udofin (loan files) — referenced, not copied, unless the tenant imports them (NN-23).
- Human translation and certified translation services — offered through the marketplace (P21).
- E-stamping — handed to a stamp-duty adapter (P18) where an instrument requires stamping; flag `dms.estamp.enabled = OFF` until the adapter and state matrix exist.

---

## 3. Personas and permissions touched

| Role code | Policy lifecycle | DMS |
|---|---|---|
| `ten_admin` | Configures policy types, approval routes, templates, retention classes | Configures metadata, folders, sharing defaults, connectors |
| `ten_dept_head` | Policy owner for the department; approves drafts for submission | Manages departmental folders |
| `ten_maker` | Drafts and revises policies; prepares evidence | Uploads, edits, shares within permissions |
| `ten_checker` | Reviews drafts (maker ≠ checker); verifies type copies on request | Approves evidence; verifies intake mappings |
| `ten_cco` | Compliance review; owns required-policy gap list; runs attestations | Oversees evidence vault |
| `ten_kmp` (CS) | Places policies on Board/committee agenda; records approval | Owns governance folders |
| `ten_kmp` (CRO, CISO, DPO, CFO, HIA) | Domain reviewer for their policies | Domain folders |
| `ten_board_member` / `ten_committee_member` | Approve via P06; read published policies | Read-only access to policies and their packs |
| `ten_employee` | Reads and acknowledges policies | Own documents and documents shared with them |
| `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor` | Read policy history and approvals in scope | Read evidence in scope, watermarked |
| `ten_supervisor_view` | Read approved policies and evidence granted (D-12) | Read-only, logged |
| `dlv_professional` | Drafts policies as retainer maker (R-072) under a client-approved delivery grant | Delivers documents into the tenant's folders; never reviewer, approver or checker of the policy (NN-43) |
| `plt_content_maker` / `plt_content_checker` / `plt_content_publisher` | Author, check and publish model templates | — |
| External signer / share recipient | — | Signs or views only what was sent, authenticated by OTP or eSign |
| `svc_vidhi` | Drafts revisions, gap checks, summaries | OCR, classification, translation, extraction — on behalf of a named user |

---

## 4. Functional requirements — Policy lifecycle

### 4A. Policy register and required-policy catalogue

**FR-P07-01 — Policy record.** Fields: policy ID (tenant-prefixed, e.g. `POL-KYC-001`); title; type (`REGULATORY_MANDATED`, `REGULATORY_RECOMMENDED`, `INTERNAL`, `PROCEDURE`, `SOP`, `CHARTER`, `TERMS_OF_REFERENCE`, `CODE`, `MANUAL`, `FRAMEWORK`); legal entity(ies); owner department and owner person (HRMS); drafter; reviewers; approver body (Board, named committee, MD/CEO, department head) and approval level; current version (major.minor); status; board/committee approval date and P06 decision reference; effective date; next review date and review rule (e.g. annual, or as prescribed by the instrument); applicable regulators and instruments; mapped obligations (`cnt.obligations`) and controls; linked risks (P08); audience for acknowledgements; confidentiality class; language(s); publication channels (intranet, website — e.g. LODR Reg 46 website policies; RBI requirement to publish Fair Practices Code and grievance policy on the website **[VERIFY per pack]**); related policies; superseded-by and supersedes.

**FR-P07-02 — Required-policy catalogue.** For each legal entity, the catalogue lists the policies required or recommended by the governance blueprint (P06 FR-P06-03) and by the tenant's enabled content packs (P03, P15), each with its legal basis, required approver, prescribed review frequency, mandatory contents checklist (where the instrument prescribes contents) and the model template available. Examples (illustrative; the authoritative list is pack data with citations): for NBFCs — fit-and-proper policy (NBFC Governance Directions 2025 para 12), compensation policy (paras 29–37), CCO role policy (para 25), whistle-blower mechanism (para 38), internal governance guidelines (para 40), KYC policy, Fair Practices Code, interest-rate model, grievance redressal, outsourcing, IT and cyber security, information security, business continuity, ICAAP, liquidity risk, credit, collateral valuation, recovery and collection agent conduct, fraud risk, digital lending; for listed entities — RPT policy (LODR Reg 23(1)), materiality of events (Reg 30(4)(ii)), archival (Reg 30(8)), preservation of documents (Reg 9), dividend distribution (Reg 43A, top 1,000), board diversity and NRC policy (Reg 19 read with Part D of Schedule II), familiarisation programme (Reg 25(7)), code of fair disclosure and code of conduct (PIT Reg 8 and Reg 9), whistle-blower/vigil mechanism (Reg 22; s.177(9)); for all companies — CSR policy (s.135), vigil mechanism where applicable, POSH policy (POSH Act s.19 duties), DPDP privacy notice and internal data-protection policy (P12), information-security policy (CERT-In and sector frameworks). Missing required policies appear as `GAP` with a "Draft from model" button.

**FR-P07-03 — Policy hierarchy and mapping.** Policies may contain or reference procedures and SOPs; each clause of a policy can be mapped to obligations and controls (`pol.clause_mappings`), so that a regulatory change (P05) finds every affected clause, and auditors (P10) can test controls back to the policy text.

### 4B. Model templates (platform) and tenant templates

**FR-P07-04 — Model template library.** Platform content team (`plt_content_*`) maintains model templates per entity family and regulator (e.g., "NBFC-ML — KYC Policy — model v3.2"), each a DOCX with: defined styles; numbered clauses with stable clause IDs (bookmarks `cl_<id>`); a citation map (clause → instrument, paragraph, obligation IDs); drafting notes for the user (as Word comments, stripped on publication); variables (`{{entity.name}}`, `{{policy.owner}}`, thresholds). Publishing follows maker ≠ checker ≠ publisher (NN-05); every published version is immutable; a new version posts a regulatory-style **Update** (NN-27) to tenants that use the template, with a clause-level diff and "what changed / why / what to do".

**FR-P07-05 — Tenant templates.** A tenant can upload its own house-style template (cover page, header/footer, logo, numbering scheme, fonts, approval block, document control table) and its own policy templates. The system extracts styles and maps model content into the tenant style on generation. Tenant templates are tenant overlays (NN-03); platform updates never overwrite them.

**FR-P07-06 — Document control table.** Every generated policy carries a document-control block (version, date, owner, reviewer, approver, approval date and reference, effective date, next review date, change summary), auto-filled and updated on each version.

### 4C. Vidhi-assisted drafting and the deterministic redline engine

**FR-P07-07 — Drafting modes.** The user directs Vidhi (from the policy page, or as a task assigned to Vidhi, R-095) in one of five modes:

| Mode | Input | Base for redline | Output |
|---|---|---|---|
| New from model | Model template + entity profile + user instructions | Model template (merged with variables) | Draft v0.1 with tracked changes vs model showing tenant-specific deviations |
| Align to previous version | Current approved policy + latest model and/or regulatory change items | Current approved version | Draft vN+0.1 with tracked changes vs the approved version |
| Align to regulatory change | Approved policy + change item(s) from P05 | Current approved version | Tracked changes limited to affected clauses, each with the change item cited |
| Redraft from instructions | Approved policy + free-text instructions (e.g., "add co-lending section") | Current approved version | Tracked changes; new sections inserted |
| Gap check | Policy + mandatory-contents checklist from the pack | — | Report: each mandatory element present/partial/missing with clause location; optional draft insertions |

**FR-P07-08 — Deterministic redline (AI never writes OOXML).** Vidhi returns structured revised text per clause (`{clause_id, revised_text, rationale, citations[]}`) — never a Word file. The redline engine (`packages/redline`) then:

1. parses the base DOCX into a clause/paragraph/run model, preserving styles, numbering, tables, headers and footers;
2. computes a word-level diff per clause between base text and revised text (Myers diff with move detection for paragraphs);
3. writes native OOXML revisions: `w:ins` and `w:del` runs with `w:author="Vidhi AI (draft)"` and `w:date`, `w:pPrChange`/`w:rPrChange` for formatting changes, inserted paragraphs and table rows as tracked insertions, deleted ones as tracked deletions;
4. attaches a `w:comment` to each changed clause with the rationale and citations (instrument, paragraph, model clause ID) — comments authored "Vidhi AI (draft)";
5. validates the package (schema validation, round-trip open in LibreOffice headless and the OOXML SDK validator in CI), and stores it as a new draft version.

Users edit in Word (or co-author, §4K); their own edits appear under their names; accepting all changes yields exactly the intended text. The engine also produces a PDF "comparison view" for reviewers who do not use Word.

**FR-P07-09 — Alignment rules.** Vidhi must: keep tenant-specific provisions unless instructed or unless contrary to a mandatory requirement (then flag, not delete silently); not weaken any obligation present in the model or the regulation; cite every substantive change; mark uncertain points as comments "Needs owner decision"; never invent regulatory references (NN-06) — the citations are validated against `cnt` before the redline is written; unresolved citations are flagged in red.

**FR-P07-10 — Quality checks on every draft.** Defined-term consistency; cross-reference integrity (clause numbers); mandatory-contents checklist coverage; prohibited phrases (e.g., "guarantee of compliance"); readability score for employee-facing policies; inconsistent figures vs entity data (e.g., a threshold in the policy that differs from the configured threshold).

### 4D. Review and approval workflow

**FR-P07-11 — Configurable route.** Default route: `DRAFT → OWNER_REVIEW → COMPLIANCE_REVIEW → (DOMAIN_REVIEW: Risk / IT / Legal / DPO as mapped) → READY_FOR_APPROVAL → COMMITTEE_RECOMMENDED (optional) → BOARD_APPROVED (or approver-level approval) → EFFECTIVE`. Routes are tenant-configurable per policy type (tier T within guard: regulatory-mandated policies must end with the approver body the instrument requires — tier G/L). Parallel reviewers, review due dates, delegation when the reviewer is on leave (never to the maker), comment threads anchored to clauses, reviewer checklist.

**FR-P07-12 — Version lock.** On `READY_FOR_APPROVAL`, the version is locked and its hash recorded; any change creates a new version and restarts the review from the configured stage.

**FR-P07-13 — Board/committee approval.** `READY_FOR_APPROVAL` auto-creates an agenda item in the next meeting of the approver body (P06 FR-P06-22) with the clean version, the redline vs previous version, the change summary and the reviewer sign-offs. The P06 decision (approved / approved with modifications / deferred / rejected) updates the policy. "Approved with modifications" requires a new version reflecting the modifications, checked by the CS against the minutes.

**FR-P07-14 — Signed-copy evidence (R-091).** Moving to `EFFECTIVE` requires: (a) the P06 decision reference; (b) the approved DOCX (sealed, NN-09); and (c) an uploaded signed/certified copy — a scanned PDF of the approved policy signed by the authorised signatory, or a certified true copy of the resolution with the policy annexed, as configured. The system OCRs the scanned copy and computes text similarity with the approved version; similarity below `pol.scan_match.min_similarity` (default 0.97) raises a mandatory CS confirmation with the differences shown. Policies approved by circular resolution follow the same rule.

**FR-P07-15 — Publication.** On `EFFECTIVE`: the policy is published to the configured channels (employee policy portal in LDC; tenant intranet/SharePoint via connector; website URL list for publicly required policies — LDC produces the PDF and records the URL the tenant publishes); the audience is notified; acknowledgement campaigns start; linked compliance instances receive the evidence automatically (e.g., "Has the NBFC adopted a Board-approved fit-and-proper policy?" → evidence: approved policy + decision reference + signed copy).

### 4E. Attestations and acknowledgements

**FR-P07-16 — Campaigns.** Audience rules from HRMS (department, role, grade, location, legal entity, new joiners automatically within N days of joining), external audiences (vendors, agents, DSAs) through share links. Modes: read-and-acknowledge; acknowledge with declaration text; quiz (configurable question bank, pass mark); annual re-attestation (e.g., code of conduct affirmation under LODR Reg 26(3); PIT code). Reminders and escalation to the manager; completion dashboards by department; certificates per person; evidence pack per campaign (list, timestamps, policy version hash).

### 4F. Review calendar and change-driven updates

**FR-P07-17 — Review calendar.** Next-review dates produce tasks (P04) for the owner at T-60/T-30/T-7 (configurable) and calendar entries; overdue review on day +1 opens a compliance issue with severity from the policy type. A review can end with "No change" — still requiring the approver's confirmation (and a P06 noting where the approver is the Board) and resetting the review date.

**FR-P07-18 — Regulatory change impact.** When a P05 change item affects obligations mapped to a policy's clauses, the policy shows "Update required" with the change item; the owner can launch "Align to regulatory change" (FR-P07-07) in one click. Model-template updates (FR-P07-04) do the same with the model diff.

### 4G. Versions, history and retirement

**FR-P07-19 — History.** Every version keeps: DOCX, PDF, redline vs previous, approvals, decision reference, signed copy, attestations, hash. Any two versions can be compared (visual diff and generated DOCX redline). Retirement requires approval at the same level as adoption (or as configured) and records the superseding policy; retired policies remain readable for the retention period.

---

## 4 (continued). Functional requirements — Document management system

### 4H. Repository structure and canonical paths

**FR-P07-20 — One document, many records.** A document (`dms.documents`) is stored once and linked to any number of records (compliance instance, evidence request, meeting, agenda item, policy, audit finding, grievance, risk event, return, employee file) through `dms.document_links`. Deleting a link never deletes the document; documents are disposed of only through retention (§4Q).

**FR-P07-21 — Canonical path from metadata.** Each document has a canonical path computed from its metadata by the taxonomy rules of Appendix M (LDC-EXPORT-1.0), for example:

`<Top-level area>/<Legal Entity>/<Financial Year>/<Department or body>/<Record>/<file name>` (Appendix M §M.3; top-level area names are authoritative, X-27), e.g. `05 Governance - Board, Committees and Meetings/Alpha Finance Ltd/FY 2025-26/Board of Directors/2025-08-12 - Board Meeting 3 of FY 2025-26/04 Minutes - SIGNED.pdf`. Single-entity tenants omit the entity level.

The path is **data, not code**: the taxonomy is a versioned rule pack; a code release cannot change a customer-visible path. If the taxonomy itself changes, a migration plan maps old paths to new with aliases, and exports carry both (NN-10, NN-11). Folder names use plain English, numbered top-level areas for ordering, ISO-like dates (`YYYY-MM-DD`) and no internal IDs (IDs live in the manifest).

**FR-P07-22 — Folders, virtual folders and saved searches.** Users browse the canonical tree, department "working folders" (tenant-created, tier T), and virtual folders (saved searches such as "All evidence awaiting checker — Compliance dept"). Moving a document in the UI changes its metadata (and therefore its canonical path), never its identity.

### 4I. Metadata

**FR-P07-23 — Core metadata.** Document type (taxonomy, e.g. Policy, SOP, Board Minutes, Notice, Register Extract, Return, Acknowledgement, Regulator Letter, Inspection Report, Evidence, Agreement, Certificate, Correspondence, Chat Screenshot, Handwritten Note, Translation, Type Copy); legal entity; FY and period; department; module and record links; confidentiality class (`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `BOARD_CONFIDENTIAL`, `UPSI`, `SEALED_*` for NN-13 classes); retention class; language(s) and script; source (`UPLOAD`, `EMAIL_IN`, `CONNECTOR`, `GENERATED`, `VIDHI_DRAFT`, `FOLDER_INTAKE`, `ECOSYSTEM`); OCR status and confidence; checksum SHA-256; size and MIME type (sniffed, not trusted from extension); author, owner, uploaded-by; captured-at (for evidence: when the fact happened) and uploaded-at; version; tags.

**FR-P07-24 — Custom metadata.** Tenants add fields per document type (text, number, date, picklist, person, record link) with validation; tier T, registered in P02; included in exports as manifest columns.

**FR-P07-25 — Auto-classification.** On ingest, rules (folder name patterns, e-mail address used, source module) and Vidhi classification (P17) propose type, entity, FY, department and links with confidence; the uploader confirms; high-confidence rule matches can auto-apply where the tenant enables it (`dms.autoclassify.auto_apply_threshold`).

### 4J. Versioning, check-in/check-out and compare

**FR-P07-26 — Versions.** Major/minor versions; every upload of the same document creates a version; restore creates a new version (history never rewritten); version labels and comments; compare any two versions (text diff for Office/PDF text; visual diff for images).

**FR-P07-27 — Check-out.** Optional exclusive lock with expiry (`dms.checkout.max_hours`, default 24); admin can break a lock with reason (audited); co-authoring sessions (§4K) replace locks for connected M365 libraries.

### 4K. Office editing (R-043)

**FR-P07-28 — Three editing paths.**

| Path | When | How |
|---|---|---|
| Desktop round-trip (default) | Any tenant | "Edit in Word/Excel" downloads with check-out; re-upload as new version; the add-in-free flow works with any Office version |
| Microsoft 365 co-authoring | Tenant connects its SharePoint/OneDrive (P19 bring-your-own storage) | A working copy is placed in the tenant's connected library via Microsoft Graph; users co-author in Word for the web or desktop under their own M365 identities; on "Check in to LawDocsComply" the system pulls the file, versions it, hashes it and re-links; the M365 copy is optionally removed or kept as the tenant chooses |
| Embedded editor (flag) | Tenants without M365 that want in-browser editing | A self-hosted WOPI-compatible editor (Collabora Online or ONLYOFFICE Docs, licence ADR in P00) hosted in-region; `dms.embedded_editor.enabled = OFF` until the ADR and DOCX tracked-changes fidelity tests pass |

Direct WOPI integration with Microsoft 365 for the web is available only to members of Microsoft's Cloud Storage Partner Program, which is open to independent software vendors whose business is cloud storage; LDC therefore uses the Graph-based co-authoring path above and does not claim native Office-for-the-web hosting **[VERIFY eligibility at P00 ADR]**. Google Workspace (Docs/Sheets) editing follows the same pattern via the Google Drive adapter when enabled (D-10), with conversion back to DOCX/XLSX on check-in so that records remain in Office formats.

### 4L. Search

**FR-P07-29 — Search.** OpenSearch index (PostgreSQL FTS fallback) over title, metadata, extracted text, OCR text, type-copy text and translations; facets (type, entity, FY, department, module, status, owner, language, confidentiality, source, date ranges); filters combinable; saved searches; results **permission-trimmed at query time** using the same ABAC attributes as the API (NN-01) — no snippet from a document the user cannot open; BOARD_CONFIDENTIAL and sealed classes are excluded from the general index and searched only inside their own scoped index for authorised users. Semantic and question-style search ("show the board resolution approving the outsourcing policy in 2025") is delegated to P17 with the same permission filter.

### 4M. Selective sharing

**FR-P07-30 — Internal sharing.** Share with a user, role, department, committee or group with permission level (view, comment, edit, manage); time-limited where required; inheritance from folder rules with explicit overrides; "who has access" panel per document.

**FR-P07-31 — External sharing and share packs.** The user builds a **share pack** — ticking exactly which documents (and which versions) to include, previewing what the recipient will see, and excluding everything else (R-038). Options per pack: recipient(s) by e-mail/mobile; authentication (OTP to e-mail/mobile, optional password); access mode (view-only in the secure viewer; download permitted; print permitted); dynamic watermark (recipient identity, timestamp, "Confidential — shared by <entity>"); expiry date/time; maximum opens; IP/country restriction (optional); message; request-for-upload slot (recipient can return documents into a designated folder after malware scan). Revocation takes effect within 60 s. Every open, page view, download and failed authentication is logged and visible to the sharer.

**FR-P07-32 — Guards.** Sharing of `BOARD_CONFIDENTIAL` requires the CS's approval; `SEALED_*` classes (POSH, whistle-blower, complainant identity, credentials) cannot be shared externally from the DMS at all — only through their own modules' controlled disclosure flows (NN-13, NN-17); `UPSI` sharing writes an SDD entry (P06 FR-P06-49) and asks for the purpose; personal-data-heavy documents prompt a DPDP purpose/basis confirmation (P12).

### 4N. eSign envelopes (R-027)

**FR-P07-33 — Envelope model.** An envelope holds one or more documents, signers (internal users, external parties), roles (signer, approver, witness, CC), order (sequential, parallel, mixed), signature fields placed on pages (drag-and-drop or anchor text), signature method per signer, reminders, expiry and a completion action (seal, file to folder, update record status).

**FR-P07-34 — Signature methods.**

| Method | Legal basis | Implementation |
|---|---|---|
| Aadhaar eSign (OTP or biometric) | IT Act 2000 s.3A and the Second Schedule (electronic authentication technique — eSign); CCA eSign guidelines and eSign API specification v2.1 | Through an application-service-provider adapter (e.g., Leegality, Digio, SignDesk, Surepass, Protean) connecting to CCA-empanelled eSign Service Providers (eMudhra, C-DAC, Capricorn Identity Services, Protean eGov Technologies, Verasys, CSC e-Governance Services, CDSL Ventures as listed by CCA); consent screen text per CCA guidelines; LDC never receives the Aadhaar number or OTP (NN-12); the signed PDF carries the ESP certificate |
| DSC (Class 3) | IT Act s.3 (digital signature) | Signing on the holder's USB token through a local signer utility/browser extension, or a cloud-HSM DSC where the holder uses one; LDC never holds private keys |
| Simple electronic acknowledgement | Contract Act and IT Act s.10A (electronic contracts) for internal acknowledgements | Click/typed acceptance with authenticated session, timestamp and document hash — used for policy acknowledgements, not for statutory documents requiring a signature |

**FR-P07-35 — Excluded documents.** The IT Act First Schedule excludes from its electronic-record provisions: negotiable instruments other than cheques; powers of attorney; trusts; wills and other testamentary dispositions; contracts for sale or conveyance of immovable property or interests in it. Documents typed as any of these are blocked from e-signature with an explanation and a "physical execution checklist" (print, sign, stamp, notarise/register as applicable, upload scan) **[VERIFY current First Schedule text]**. Instruments liable to stamp duty show a stamping step before signature (flag `dms.estamp.enabled`).

**FR-P07-36 — Certificate of completion.** For each envelope: document hash before and after signing, each signer's authenticated identity attributes (masked), method, ESP transaction ID/certificate serial, timestamps (IST and UTC), IP and user agent, consent captured, sequence of events. The certificate and signed PDF are sealed (NN-09) and exported together. Signed PDFs preserve embedded signatures (PAdES where supplied by the ESP) and validation data for long-term verification where available.

**FR-P07-37 — Use across modules.** Minutes and declarations (P06), employment agreements and offer letters (P13), service-level agreements for retainers (P21), DPAs and NDAs (P12, P21), certificates (P10, P11), policy signed copies (§4D) all use this envelope service.

### 4O. OCR, handwriting, screenshots and type copies (R-038)

**FR-P07-38 — Ingestion pipeline.** `UPLOADED → SCANNED (malware) → SNIFFED (true type) → NORMALISED (PDF/A or image normalisation, deskew, denoise, rotation, page split) → TEXT_EXTRACTED (native text where present) → OCR (printed text engine; handwriting/complex layout via Vidhi vision, P17) → STRUCTURED (layout, tables, chat bubbles, e-mail headers) → INDEXED`. Each stage is idempotent and retried; failures surface in the document's processing panel.

**FR-P07-39 — Content types handled.**

- **Printed scans and photos** (letters, regulator notices, inspection reports, certificates) — OCR with per-word confidence; tables extracted to grids.
- **Handwritten documents** (registers, notes, complaint letters, attendance sheets) — handwriting recognition through Vidhi vision with per-line confidence; illegible regions marked `[illegible]` rather than guessed.
- **WhatsApp and other chat screenshots** — layout-aware extraction into a transcript: chat/group name where visible, sender label (as displayed, e.g. contact name or number masked per NN-12 policy), timestamp (with the screenshot's date context), message text, quoted/replied message, attachment indicators, deleted-message markers; multiple screenshots of one chat are stitched in order with overlap de-duplication. The transcript records that it is derived from a screenshot and does not assert authenticity.
- **E-mail** (`.eml`, `.msg`, forwarded e-mail-in) — headers (from, to, cc, date, subject, message-ID), body (HTML sanitised), attachments as child documents.
- **Office and PDF documents** — native text extraction; embedded images OCR'd.

**FR-P07-40 — Type copy.** For scanned, handwritten and screenshot documents the system produces a **type copy** (DOCX and searchable PDF) and shows it **side by side** with the original: region-to-line alignment (hover a line to highlight the source region), low-confidence words underlined, `[illegible]` markers, page sync. The user corrects text inline; every correction is tracked (who, when, old → new). Statuses: `AI_DRAFT → USER_CORRECTED → VERIFIED` (verification by a named user with a declaration "I have compared this type copy with the original"). A verified type copy is attached to the record **together with the original**; the original remains the primary evidence; the type copy carries a footer "Type copy prepared with machine assistance and verified by <name> on <date>; the original is attached". Bharatiya Sakshya Adhiniyam 2023 s.63 certificates for exports are generated by P19 from the evidence ledger (NN-09).

**FR-P07-41 — Field extraction.** For known document types (regulator letters, CIC notices, GST notices, inspection reports, invoices, KYC documents uploaded as evidence — with NN-12 masking), Vidhi extracts key fields (reference number, date, authority, subject, due date, amounts) into a review form; on confirmation, P04 creates tasks (e.g., "Reply to RBI letter by 15 Nov 2026"). Extraction is a suggestion until confirmed (NN-14).

### 4P. Translation (R-038)

**FR-P07-42 — Language coverage.** Source languages: the six official languages of the United Nations — Arabic, Chinese, English, French, Russian and Spanish — and the 22 languages of the Eighth Schedule to the Constitution of India — Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu and Urdu. Target: English (default). Reverse translation (English → Hindi or another listed language) for notices and employee-facing policies is available behind `dms.translation.reverse.enabled = OFF` with mandatory human review.

**FR-P07-43 — Detection and scripts.** Automatic language and script detection per segment (documents can be mixed, e.g., Hindi-English); scripts handled include Latin, Devanagari, Bengali-Assamese, Gurmukhi, Gujarati, Odia, Tamil, Telugu, Kannada, Malayalam, Perso-Arabic (Urdu, Kashmiri, Sindhi), Ol Chiki (Santali), Meetei Mayek and Bengali script (Manipuri), Arabic, Cyrillic and Chinese (Simplified/Traditional). OCR and translation quality differ by script and language; the platform publishes a per-language quality tier (`A` reliable, `B` usable with review, `C` low-resource — review mandatory) measured on an evaluation set in P17 **[VERIFY per-language results before enabling tier A]**.

**FR-P07-44 — Output.** Translated DOCX with paragraph alignment to the source (two-column view in the app; optional bilingual DOCX), segment confidence, glossary application (tenant terminology and a legal/regulatory glossary — e.g., "निदेशक मंडल" → "Board of Directors"), untranslatable items preserved (names, numbers, citations), and the label "Machine translation — not verified" until a named reviewer verifies it (`MT_DRAFT → REVIEWED`). Certified translation is a marketplace service (P21).

**FR-P07-45 — Engines.** Primary: Claude via the P17 provider adapter — Amazon Bedrock India route for every personal, confidential, financial, legal or HR document, never failing over outside India (D-14 as amended by X-03; NN-41); low-confidence highlighting uses the P17 setting `ai.typecopy.low_confidence_threshold` (default 0.85). Secondary candidates evaluated in P17: Bhashini (Government of India language platform) and commercial MT APIs — subject to data-residency, retention and terms review (NN-15, NN-24) **[VERIFY]**.

### 4Q. Retention, legal hold and disposal

**FR-P07-46 — Retention classes.** Rule-pack data with legal floor, citation and trigger event; tenants can lengthen but not shorten below the floor (tier G). Seed examples (each **[VERIFY]** before go-live):

| Class | Floor | Basis |
|---|---|---|
| Minutes books (Board, committee, GM) | Permanent | s.118 read with Rule 25/26 Management & Administration Rules; SS-1/SS-2 |
| Statutory registers | Permanent / as per Rules (e.g., some eight years after cessation) | s.88; Rule 15 Management & Administration Rules |
| Books of account and vouchers | 8 years from the relevant FY | s.128(5) Companies Act |
| Annual returns and copies of certificates | 8 years from filing | Rule 15 |
| KYC and transaction records | 5 years after end of relationship / transaction | PML Act s.12; PML Rules; RBI KYC Master Direction |
| GST records | 72 months from due date of annual return | CGST Act s.36 |
| Income-tax records | As per Income-tax Act 2025 and rules | **[VERIFY]** |
| Listed-entity disclosures | ≥ 5 years on website; archival per policy | LODR Reg 30(8); Reg 9 preservation policy (permanent or ≥ 8 years) |
| SDD (PIT) | ≥ 8 years | PIT Reg 3(6) |
| Employee records and registers | As per Labour Codes and rules (P13) | **[VERIFY]** |
| Personal data not covered by a legal retention | Until purpose served, then erase | DPDP Act s.8(7) and Rules |

**FR-P07-47 — Legal hold.** CS/CCO/legal can place holds by matter (litigation, inspection, investigation) over documents, folders or saved searches; holds suspend disposal and are listed on each document; release requires a second approver.

**FR-P07-48 — Disposal.** A monthly job lists documents past retention; the owner and a checker approve disposal; sealed/WORM objects are deleted only after the Object Lock period and only if no hold exists; a disposal certificate (what, when, who approved, basis) is kept permanently; DPDP erasure requests (P12) use the same path with the legal-retention check.

### 4R. Folder upload intake (R-021)

**FR-P07-49 — Bulk intake.** Drag-and-drop a folder tree in the browser (directory upload) or upload a ZIP (up to `dms.intake.max_zip_gb`, default 10 GB, resumable chunked upload), or pull from a connected OneDrive/SharePoint/Google Drive/S3/SFTP location (P18/P19).

**FR-P07-50 — Mapping preview.** Before anything is committed, the system shows a grid of every file with: proposed document type, entity, FY, department, module and record link — derived from folder-name pattern rules (tenant-editable, e.g. `FY {yyyy}-{yy}` → FY; `Compliance/RBI/KYC*` → department Compliance, instrument "KYC Master Direction"), from LDC-EXPORT-1.0 path recognition (re-importing an LDC export maps 100% automatically using its manifest), and from Vidhi classification; confidence; duplicates (same SHA-256 already in the tenant — default "link existing, do not duplicate"); conflicts (same canonical path, different content — choose "new version" or "skip", never overwrite); unsupported, encrypted, password-protected, oversized or infected files (quarantined). Users edit mappings in bulk (select rows → set FY), save mapping rules for next time, and commit.

**FR-P07-51 — Commit job and report.** The commit runs as a background workflow with progress; produces an intake manifest (file, hash, mapped metadata, links created, result) as XLSX/CSV and an exception list; the evidence linkages created can be reviewed in P04. The job is resumable and idempotent (re-running does not duplicate).

### 4S. Malware, active content and AI safety

**FR-P07-52 — Scanning.** Every file is scanned (ClamAV in-cluster plus a commercial engine where licensed) before any processing; macro-enabled Office files are quarantined unless the tenant allows them for a folder; PDFs are sanitised of JavaScript and launch actions for the viewer copy; archive bombs and path-traversal names are rejected; images are re-encoded for the viewer.

**FR-P07-53 — Prompt-injection defence.** Text extracted from documents is untrusted data: it is passed to Vidhi only inside delimited data blocks with instructions to ignore embedded directives; tool calls proposed while processing a document require the user's confirmation; documents with detected injection patterns are flagged (NN-14).

### 4T. E-mail-in

**FR-P07-54 — Ingest addresses.** Per tenant and per record (e.g., `evidence+<token>@in.lawdocscomply.com`, `letters+<entity-code>@in.lawdocscomply.com`); SPF/DKIM/DMARC evaluation; sender allowlist per address; size limits; body and attachments stored as linked documents; auto-classification; acknowledgement e-mail optional. Outlook/Gmail add-ins are a later enhancement (flag).

### 4U. Document generation service

**FR-P07-55 — Generation.** Shared service (`dms.generate`) for every module: DOCX from templates (docxtemplater) with tenant branding; PDF via Gotenberg (LibreOffice) and PDF/A-2b for archival copies; XLSX via a typed writer; consistent document-control block; generated documents are linked to their source records and versioned; generation inputs (data snapshot hash) recorded for reproducibility (NN-22).

### 4V. Viewer, annotation and redaction

**FR-P07-56 — Secure viewer.** In-browser viewer for PDF, images, Office (converted renditions), e-mail; zoom, search in document, thumbnails, page rotation (view only); annotations (private/shared); dynamic watermark; print/download controls by permission.

**FR-P07-57 — Redaction.** Permanent redaction on a **new derived copy** (original preserved), with area and text-pattern redaction (PAN, Aadhaar, account numbers, phone numbers — pattern library), redaction reason codes, and a redaction log; used before external sharing and for regulator submissions.

### 4W. Evidence vault

**FR-P07-58 — Evidence specifics.** Evidence items link documents to compliance instances (P04) and audit tests (P10) with: captured-at (when the fact occurred), period covered, submitted-by, checker decision and comments, hash; after checker approval the evidence version is sealed (NN-09) — later corrections are new versions with the earlier one preserved and visible. Evidence requests to other users or external parties use request-for-upload slots (FR-P07-31).

### 4X. Export

**FR-P07-59 — Portability.** All documents, versions, type copies, translations, signatures, certificates, metadata and links are exported in LDC-EXPORT-1.0 (Appendix M) with manifests; sealed objects include their hashes and the s.63 certificate; P19 owns packaging and BYO-storage sync.


### 4Y. v1.1 enhancements — faster policy cycles, measurable adherence *(v1.1)*

**FR-P07-54 — Baton tracker (IMP-064).** Every policy version in review shows a "baton" strip: current holder (person or body), time held, next step, review SLA, and a **Nudge** button (one reminder per 24 h per holder, logged). Batons held beyond SLA turn amber/red and appear in the CCO's Work Inbox and the owner's dashboard. The baton also shows on the policy card in lists.

**FR-P07-55 — Parallel review lanes (IMP-065).** The route designer (P02 workflow designer) allows stages to run in parallel lanes (e.g., Risk, IT, Legal, DPO simultaneously) where independence is not required; comments from all lanes consolidate into one comment set per clause; the version moves on when all mandatory lanes sign off. Lanes required by law or policy to be sequential (e.g., committee recommendation before Board approval) are Locked sequential in the rule pack.

**FR-P07-56 — Policy–practice drift detection (IMP-066).** Policy clauses carry structured parameters where applicable (frequency, owner role, threshold, limit, approving authority, time window) captured as clause tags during drafting or by VA-05 proposal confirmed by the owner. A nightly job compares them with operational evidence: compliance-instance frequencies and owners (P04), approval chains actually used (P02/P04 logs), limits in the risk appetite (P08), returns cadence (P11) and grievance TATs (P14). A mismatch creates a **drift item** ("Policy says quarterly review by RMC; last two reviews were six months apart") routed to the policy owner with options: correct practice (task), amend policy (opens "Redraft from instructions" with the drift cited), or accept with reason. Drift items never change status or ratings by themselves (NN-47).

**FR-P07-57 — Attestation campaigns v2 (IMP-067).** Campaign builder adds: optional quiz (3–10 questions drafted by VA-05 from the policy, owner-approved; pass mark; retries; question bank rotation), reminder ladder (setting), manager escalation, completion dashboards by department, legal entity, location and grade, exportable certificates per person, and automatic re-attestation on material change (only when the change summary is marked material by the owner). External audiences (DSAs, agents, vendors) attest through share links with OTP. Completion statistics feed P13 (training records) and P28 board reports.

**FR-P07-58 — AI extraction on upload (IMP-068).** When an existing policy is uploaded (single file or folder intake), VA-05 proposes: title, type, owner department, approver body, approval date, version, effective date, next review date, the required-policy catalogue line it satisfies (P07 FR-P07-02), clause-to-checkpoint and clause-to-control links, and missing mandatory contents. Each proposal is accepted or rejected per field/link in a review grid with keyboard shortcuts (`a` accept, `r` reject, `n` next); nothing is applied without acceptance (NN-04). Acceptance measure: proposals for 20 policies reviewed in ≤ 15 minutes.

**FR-P07-59 — Progressive rendering (IMP-069).** The viewer renders the first page of any PDF up to 500 pages in < 2 s (p95) by streaming page images and text layers progressively; large DOCX are rendered from cached PDF renditions; a text-layer check flags image-only PDFs and queues OCR (§4O) with a banner "Not searchable yet".

**FR-P07-60 — Policy pack for an adopted direction.** When a client admin adopts a direction from the catalogue (P03, R-087) that requires policies, the required-policy catalogue lines are created and a one-click **"Generate policy pack"** launches "New from model" (or "Align to previous version" where a policy exists) for all of them as a batch assigned to VA-05 under the owner's supervision; drafts arrive in the owners' queues with the direction cited.

**FR-P07-61 — Bulk roll-forward with undo.** Owners or the CCO can select many policies and: roll next-review dates forward after a "No change" review cycle, reassign owners, or change review routes — each bulk operation shows an impact preview and is reversible for `pol.bulk.undo_hours` (default 24) through a compensating change (NN-49). Bulk approval of policy versions is not available (NN-46).

**FR-P07-62 — Forms and model templates library (G5, TM-098/099).** The compliance function maintains versioned model **forms** linked to the policies that require them: customer onboarding (individual), customer onboarding (non-individual — company, LLP, partnership, trust, society, HUF), KYC document checklists by customer type and risk category, beneficial-ownership declaration, CKYC consent text, DPDP notice and consent form (itemised purposes, withdrawal, grievance contact; Appendix Q/P12), customer complaint/grievance form (P14), cyber/operational incident reporting form (P12), vendor onboarding questionnaire (P12 TPRM), and conflict-of-interest and gifts declarations (P26). Forms are published as DOCX/PDF templates and as JSON form definitions consumed by P14/P12/P26 and by Finbyx/Udofin through the ecosystem template feed; **LDC does not capture borrower or customer onboarding data** — Finbyx/Udofin do (NN-23). A form's version change raises a review task wherever it is used.

**FR-P07-63 — Policy families across legal entities.** A group policy can be adopted by several legal entities with entity-specific annexures (delegations, limits) and separate approvals; the register shows one policy family with per-entity status; a group change propagates as linked draft versions to each entity, each approved by its own Board (no cross-entity approval shortcut).

**FR-P07-64 — Foreign-subsidiary policies (P25).** For entities in other jurisdictions, policies can be drafted from that jurisdiction's model templates (where a published pack exists, NN-53) in the official language, with an English working translation; the official-language text is the approved version; machine translations are labelled until reviewed by the reviewer of record (NN-54).

**FR-P07-65 — Policy Drafter agent (VA-05).** VA-05 runs the five drafting modes (FR-P07-07), gap checks, upload extraction (FR-P07-58), quiz drafting and drift explanations. Default autonomy: L1 (draft for review) — it may create a draft version and assign it to the owner but cannot move a version beyond `DRAFT`, launch campaigns, publish or retire (NN-14, NN-50). Each output lists the instruments and model clauses it relied on (NN-06).

**FR-P07-66 — Contract documents (P26 hand-off).** Documents classified as contracts (`doc_type = CONTRACT*`) get a "Manage in Contracts" action that creates or links a P26 contract record; the redline engine, eSign envelopes and e-stamping checklists are shared services used by P26 CLM.

**FR-P07-67 — Privilege tags (P26).** Document metadata gains `privilege` (PRIVILEGED, CONFIDENTIAL, NON_PRIVILEGED) and `producible` flags; documents tagged PRIVILEGED are excluded from regulator-view grants, auditor rooms and AI retrieval for non-legal users unless the General Counsel grants access per matter; downgrading privilege needs GC approval and is a ledger event.

**FR-P07-68 — Evidence classes for ESG (P27).** Retention classes and metadata for utility bills, meter readings, emission-factor sources, assurance working papers and CSR utilisation certificates are added so P27 lineage can point to DMS documents.

**FR-P07-69 — Saved searches and smart folders.** Users save searches (filters + query) as smart folders shown in the left rail; tenant admins publish smart folders to roles (e.g., "Policies due in 60 days", "Evidence awaiting OCR", "Documents shared externally this week").

**FR-P07-70 — Faster capture from Microsoft 365/Google.** "Save to LDC" actions from Outlook/Gmail and from SharePoint/OneDrive/Drive (P18 add-ins, flag per suite) file an e-mail or document into a chosen record with metadata pre-filled; duplicates are detected by hash and linked rather than re-stored.

---

## 5. Workflows and state machines

### 5.1 Policy version

`DRAFT → OWNER_REVIEW → COMPLIANCE_REVIEW → DOMAIN_REVIEW* → READY_FOR_APPROVAL (locked, hashed) → COMMITTEE_RECOMMENDED? → APPROVED → EFFECTIVE → (SUPERSEDED | RETIRED)`; side states `RETURNED_FOR_REVISION` (from any review or approval stage → new minor version in DRAFT), `REJECTED` (by approver), `APPROVED_WITH_MODIFICATIONS` (→ new version → CS check → APPROVED).

| Transition | Guard | Timer |
|---|---|---|
| DRAFT → OWNER_REVIEW | Quality checks run (FR-P07-10); no unresolved citation errors | — |
| Review stage → next | All mandatory reviewers signed off; maker ≠ checker | Review SLA `pol.review_sla_days` (default 5 working days), escalation to department head |
| READY_FOR_APPROVAL → APPROVED | P06 decision recorded (or authorised approver's approval for non-Board policies) | Agenda auto-created for next meeting of approver body |
| APPROVED → EFFECTIVE | Signed copy uploaded and matched (FR-P07-14); effective date reached | Effective-date scheduler |
| EFFECTIVE → review due | Next review date | T-60/T-30/T-7 tasks; issue at T+1 |

### 5.2 Model template version (platform)

`DRAFT → CHECKED (plt_content_checker) → PUBLISHED (plt_content_publisher) → (DEPRECATED)`; publication creates an Update with clause diff to every subscribed tenant; deprecation never alters tenant copies.

### 5.3 Document

`INGESTING → AVAILABLE → (CHECKED_OUT ↔ AVAILABLE) → (SEALED) → (ON_HOLD) → DISPOSAL_PENDING → DISPOSED (metadata stub + certificate retained)`; `QUARANTINED` from INGESTING if malware/active content; `PROCESSING_FAILED` with retry.

### 5.4 Type copy

`AI_DRAFT → USER_CORRECTED → VERIFIED`; `VERIFIED` requires a named user and declaration; re-opening a verified type copy creates a new version and resets to `USER_CORRECTED`.

### 5.5 Translation

`MT_DRAFT → REVIEWED` (named reviewer) ; optional `CERTIFIED` when a marketplace translator uploads a certified translation.

### 5.6 eSign envelope

`DRAFT → SENT → (per signer: PENDING → VIEWED → SIGNED | DECLINED | EXPIRED) → COMPLETED (sealed + certificate) | VOIDED (reason) | EXPIRED`. Guard at DRAFT → SENT: excluded-document check (FR-P07-35); stamp step done where required; signature fields assigned to every signer.

### 5.7 Folder intake job

`UPLOADING → SCANNING → MAPPING_PROPOSED → USER_REVIEW → COMMITTING → COMPLETED | COMPLETED_WITH_EXCEPTIONS | CANCELLED`; resumable from `COMMITTING` checkpoints.

### 5.8 External share

`ACTIVE → (EXPIRED | REVOKED | MAX_OPENS_REACHED)`; each access attempt logged with result.

### 5.9 Redline generation (pseudo-code)

```ts
async function generateRedline(baseDocId: string, revisions: ClauseRevision[], actor: User): Promise<DocVersion> {
  const base = await docx.parse(await dms.read(baseDocId));          // clause/paragraph/run model, styles kept
  await citations.validate(revisions.flatMap(r => r.citations));    // NN-06: unknown citation -> flagged, not written
  const pkg = base.clone();
  for (const rev of revisions) {
    const clause = pkg.findClause(rev.clauseId) ?? pkg.insertClauseAfter(rev.anchorClauseId, { tracked: true });
    const ops = diffWords(clause.text, rev.revisedText, { detectMoves: true });
    clause.applyTracked(ops, { author: 'Vidhi AI (draft)', date: now() });            // w:ins / w:del / w:rPrChange
    clause.addComment({ author: 'Vidhi AI (draft)', text: rev.rationale, citations: rev.citations });
  }
  ooxml.validate(pkg);                                               // schema + round-trip test in CI
  return dms.saveVersion(baseDocId, pkg.toBuffer(), { source: 'VIDHI_DRAFT', onBehalfOf: actor.id });
}
```


### 5.10 Drift item *(v1.1)*

`DETECTED` → `UNDER_REVIEW` (owner) → one of `PRACTICE_CORRECTED` (task closed with evidence), `POLICY_AMENDMENT_STARTED` (linked draft version) → `RESOLVED` when the version becomes effective, or `ACCEPTED_WITH_REASON` (CCO approval required for High-risk policies). Re-detection of the same mismatch within 90 days reopens the item.

### 5.11 Attestation campaign *(v1.1)*

`DRAFT` → `SCHEDULED` → `RUNNING` (reminders, escalations, quiz attempts) → `CLOSED` (completion snapshot, certificates) or `CANCELLED`. A material change to the policy during `RUNNING` offers to close and relaunch.

---

## 6. Screens and UX

Menu roots: **Policies** and **Documents** in the tenant app; **Model Templates** in the platform console; **Sign** and **Shared with me** in every user's personal menu.

| Screen ID | Name | Menu path | Key content |
|---|---|---|---|
| SCR-POL-01 | Policy Register | Policies › Register | Grid: ID, title, owner, version, status, approval date, effective, next review (RAG), mapped instruments; filters; bulk "start review", "assign owner" |
| SCR-POL-02 | Required Policies | Policies › Required | Catalogue per entity with GAP/OK; "Draft from model" |
| SCR-POL-03 | Policy Page | Policies › {policy} | Tabs: Overview, Current version (viewer), Versions & redlines, Reviews, Approvals (P06 links, signed copy), Attestations, Mappings (clauses → obligations/controls/risks), Updates required |
| SCR-POL-04 | Draft with Vidhi | inside SCR-POL-03 | Mode picker (5 modes), instructions box, sources panel (model, change items), run; result shows clause list with rationale/citations; "Open in Word" |
| SCR-POL-05 | Review Workspace | Policies › Reviews (my queue) | Side-by-side clean/redline, clause comments, checklist, approve/return |
| SCR-POL-06 | Approval Evidence | inside SCR-POL-03 | Upload signed copy; similarity result with differences; confirm |
| SCR-POL-07 | Attestation Campaigns | Policies › Attestations | Create (audience builder from HRMS), progress by department, reminders, certificates |
| SCR-POL-08 | My Policies | Personal › My policies | Policies to read/acknowledge; quiz |
| SCR-POL-09 | Review Calendar | Policies › Calendar | Month/quarter view of reviews due; drag to reschedule with reason |
| SCR-POL-10 | Model Template Studio (platform) | Console › Content › Model templates | Author, citation map editor, variables, publish with diff |
| SCR-POL-11 | Tenant Templates | Policies › Templates | Upload house style; preview merge |
| SCR-DMS-01 | Documents Home | Documents | Recent, favourites, tasks (evidence to check, type copies to verify, shares expiring), quick upload |
| SCR-DMS-02 | Browser | Documents › Browse | Canonical tree and working folders; list/grid; metadata columns; multi-select bulk actions (tag, move metadata, share, export, hold) |
| SCR-DMS-03 | Document Page | Documents › {doc} | Viewer; metadata panel; links; versions; activity log; sharing; signatures; processing (OCR, translation) |
| SCR-DMS-04 | Type Copy Workbench | inside SCR-DMS-03 | Original and type copy side by side, alignment highlight, low-confidence highlights, inline correct, verify |
| SCR-DMS-05 | Translation View | inside SCR-DMS-03 | Two-column source/English, confidence, glossary hits, mark reviewed |
| SCR-DMS-06 | Search | global search bar + Documents › Search | Facets, filters, saved searches, results with permitted snippets |
| SCR-DMS-07 | Share Pack Builder | Documents › Share › New | Tick documents, preview recipient view, options (view-only, watermark, expiry, OTP, max opens), send |
| SCR-DMS-08 | Shares & Access Log | Documents › Shares | Active shares, opens, revoke |
| SCR-DMS-09 | eSign Envelope Builder | Sign › New envelope | Documents, signers, order, fields placement, method per signer, excluded-document check |
| SCR-DMS-10 | My Signatures | Sign › Inbox | Documents awaiting my signature |
| SCR-DMS-11 | Folder Intake | Documents › Import | Drop folder/ZIP or choose connector; mapping grid; duplicates/conflicts; commit; report |
| SCR-DMS-12 | Retention & Holds | Documents › Retention | Classes, holds, disposal queue, certificates |
| SCR-DMS-13 | E-mail-in Addresses | Documents › Settings › E-mail-in | Addresses, allowlists, routing rules |
| SCR-DMS-14 | External Viewer | external shell (no app chrome) | OTP login, view-only viewer, upload slot |
| SCR-DMS-15 | Redaction Tool | inside SCR-DMS-03 | Area/pattern redaction on derived copy, reason codes |
| SCR-POL-12 *(v1.1)* | Review Baton Board | Policies › In review | Kanban by stage with baton holder, time held, SLA chips, Nudge; parallel lanes shown side by side |
| SCR-POL-13 *(v1.1)* | Drift Items | Policies › Drift | List of policy–practice mismatches with evidence links and three resolution buttons |
| SCR-POL-14 *(v1.1)* | Attestation Campaign Builder | Policies › Attestations › New | Audience rules, quiz editor (AI draft + owner approval), reminder ladder, preview |
| SCR-POL-15 *(v1.1)* | Upload Extraction Review | Policies › Import | Grid of AI-proposed fields and links with accept/reject; keyboard review |
| SCR-POL-16 *(v1.1)* | Forms & Model Templates | Policies › Forms library | Form list by use (onboarding, consent, grievance, incident, vendor, ethics); versions; where-used |
| SCR-DMS-16 *(v1.1)* | Smart Folders | DMS › left rail | Saved searches; publish to roles |
| SCR-DMS-17 *(v1.1)* | Save to LDC (add-in pane) | Outlook / Gmail / SharePoint side pane | Pick record; pre-filled metadata; duplicate warning |

UX rules: upload anywhere by drag-and-drop with metadata pre-filled from context (uploading inside a compliance instance pre-links it); "i" help keys `hlp.pol.*` and `hlp.dms.*` explain *type copy*, *legal hold*, *canonical path*, *tracked changes*, *Aadhaar eSign*; keyboard: `u` upload, `/` search, `s` share, `e` edit in Word.

---

## 7. Backend design

### 7.1 Modules touched

`pol` and `dms` (owners); `ai` (drafting, vision OCR, classification, translation); `gov` (approvals, SDD); `wf` (tasks, approvals, campaigns, calendar); `cmp` (evidence linkage, issues); `cnt` (obligations, citations, model template content); `hr` (audiences); `int` (eSign, storage, Graph, e-mail-in); `xpt` (export); `core` (ledger, Correction Entries).

Shared packages (master OP-1, X-26): approvals, maker-checker, escalations and SLAs use `packages/workflow`; reminders, digests and the Work Inbox use `packages/notify`; calendar entries and external sync use `packages/calendar` (all owned by P04); settings via `packages/config` (P02); documents via `packages/docgen` and `packages/redline` (P07); AI via `packages/ai` (P17); exports via `packages/export` (P19). This phase builds no parallel implementation.

### 7.2 Tables

| Table | Key columns |
|---|---|
| `pol.policies` | id, tenant, legal_entity_ids[], code, title, type, owner_dept_id, owner_person_id, approver_body, approval_level, status, current_version_id, review_rule, next_review_on, confidentiality, publication jsonb |
| `pol.policy_versions` | policy_id, version, base_version_id, document_id (DOCX), pdf_document_id, redline_document_id, hash, status, locked_at, change_summary |
| `pol.reviews` | version_id, stage, reviewer_id, decision, comments_ref, due_on, decided_at |
| `pol.approvals` | version_id, body, gov_decision_id, approved_on, signed_copy_document_id, scan_similarity, cs_confirmation |
| `pol.clause_mappings` | version_id, clause_id, obligation_ids[], control_ids[], risk_ids[] |
| `pol.required_policies` | legal_entity_id, requirement_key, lr_ids[], model_template_id, status |
| `pol.model_templates` / `pol.model_template_versions` | family, regulator, title; version: document_id, citation_map jsonb, status, published_at |
| `pol.tenant_templates` | style_document_id, mapping jsonb |
| `pol.attestation_campaigns` / `pol.attestations` | campaign: policy_version_id, audience_rule, mode, deadline; attestation: person_id, status, acknowledged_at, quiz_score, evidence hash |
| `dms.documents` | id, tenant, legal_entity_id, doc_type, title, confidentiality, retention_class, canonical_path (computed, stored), language[], source, status, current_version_id, custom jsonb |
| `dms.document_versions` | document_id, version, object_key, sha256, size, mime, created_by, created_at, sealed_at |
| `dms.document_links` | document_id, record_module, record_id, link_role (EVIDENCE, ATTACHMENT, SOURCE, OUTPUT) |
| `dms.extractions` | version_id, kind (TEXT, OCR, CHAT_TRANSCRIPT, EMAIL, TABLES, FIELDS), engine, engine_version, confidence, payload_ref |
| `dms.type_copies` | source_version_id, document_id (DOCX/PDF), status, corrections jsonb, verified_by, verified_at |
| `dms.translations` | source_version_id, source_lang, target_lang, document_id, segments_ref, confidence, status, reviewed_by |
| `dms.shares` / `dms.share_items` / `dms.share_access_log` | share: type, recipients, options jsonb, expires_at, status; items: document_version_id; log: event, at, ip, ua, result |
| `dms.envelopes` / `dms.envelope_signers` / `dms.envelope_events` | envelope: documents, status, certificate_document_id; signer: method, order, status, esp_txn_ref; events |
| `dms.retention_classes` / `dms.legal_holds` / `dms.disposal_batches` | — |
| `dms.intake_jobs` / `dms.intake_items` / `dms.mapping_rules` | job: source, status, counts; item: path, sha256, proposed jsonb, final jsonb, result |
| `dms.inbound_addresses` | address, routing jsonb, allowlist[] |
| `pol.review_lanes` *(v1.1)* | version_id, lane_key, mandatory, assignee_ids[], state, signed_off_at |
| `pol.batons` *(v1.1)* | version_id, holder_ref, since, sla_due, nudges jsonb |
| `pol.clause_parameters` *(v1.1)* | version_id, clause_id, parameter_type (FREQUENCY, OWNER_ROLE, THRESHOLD, LIMIT, APPROVER, WINDOW), value jsonb, confirmed_by |
| `pol.drift_items` *(v1.1)* | policy_id, clause_id, parameter_type, expected, observed, evidence_refs[], state, resolution, resolved_by |
| `pol.quizzes` / `pol.quiz_attempts` *(v1.1)* | campaign_id, questions jsonb (approved), pass_mark; attempt: person_id, score, passed, attempted_at |
| `pol.forms` / `pol.form_versions` *(v1.1)* | form_key, use_type, linked_policy_ids[]; version: docx_id, json_schema, status, published_at |
| `dms.smart_folders` *(v1.1)* | owner, query jsonb, published_role_ids[] |
| `dms.documents` (extended *v1.1*) | + privilege, producible, contract_record_id, jurisdiction, official_language |

Object storage keys are opaque (`t/<tenant>/d/<doc>/v/<ver>`), independent of the canonical path; the canonical path is recomputed from metadata (so infrastructure moves never change paths; NN-10/NN-11).

### 7.3 APIs (`/api/v1/pol/...`, `/api/v1/dms/...`)

Policies: `GET /policies`, `POST /policies`, `GET /policies/required?entity=`, `POST /policies/{id}/versions:draft-with-vidhi` (async job), `POST /policies/{id}/versions/{v}:submit`, `POST /reviews/{id}:decide`, `POST /policies/{id}/versions/{v}:ready-for-approval`, `POST /policies/{id}/versions/{v}/signed-copy`, `POST /policies/{id}:retire`, `POST /attestation-campaigns`, `POST /attestations/{id}:acknowledge`, `GET /policies/{id}/versions/{a}/compare/{b}`.
DMS: `POST /documents` (multipart/resumable `tus` upload), `GET /documents/{id}`, `POST /documents/{id}/versions`, `POST /documents/{id}:checkout`, `POST /documents/{id}:checkin`, `POST /documents/{id}/links`, `GET /search`, `POST /shares`, `DELETE /shares/{id}`, `POST /envelopes`, `POST /envelopes/{id}:send`, `POST /envelopes/{id}:void`, `POST /documents/{id}/type-copy:generate`, `PATCH /type-copies/{id}` (corrections), `POST /type-copies/{id}:verify`, `POST /documents/{id}/translations`, `POST /intake-jobs`, `POST /intake-jobs/{id}:commit`, `POST /legal-holds`, `POST /disposal-batches/{id}:approve`, `POST /documents/{id}/redactions`.
Webhooks in: ESP/ASP callbacks (signed, verified, idempotent), Graph change notifications for co-authored working copies.

### 7.4 Domain events (internal `in.lawdocscomply.pol.*`, `in.lawdocscomply.dms.*`; the Ecosystem Spec events `PolicyAttested` and `EvidenceSubmitted` are re-published by `int` as `in.infrabyx.grc.<EventName>.v1`, X-01)

`PolicyDrafted`, `PolicySubmittedForReview`, `PolicyReviewDecided`, `PolicyReadyForApproval`, `PolicyApproved`, `PolicyEffective`, `PolicyReviewDue`, `PolicyReviewOverdue`, `PolicyRetired`, `PolicyAttested` (Ecosystem Spec name), `AttestationCampaignCompleted`, `ModelTemplatePublished`, `DocumentUploaded`, `DocumentVersioned`, `DocumentSealed`, `DocumentQuarantined`, `TypeCopyVerified`, `TranslationReviewed`, `ShareCreated`, `ShareAccessed`, `ShareRevoked`, `EnvelopeSent`, `EnvelopeCompleted`, `EnvelopeDeclined`, `IntakeJobCompleted`, `LegalHoldPlaced`, `LegalHoldReleased`, `DocumentsDisposed`, `EvidenceSubmitted` (Ecosystem Spec name).

### 7.5 Jobs and Temporal workflows

`PolicyVersionWorkflow`, `PolicyReviewScheduler` (daily 06:00 IST), `AttestationCampaignWorkflow`, `DocumentIngestionWorkflow` (scan → OCR → index), `TypeCopyWorkflow`, `TranslationWorkflow`, `EnvelopeWorkflow` (with ESP callbacks and expiry), `FolderIntakeWorkflow` (resumable), `ShareExpiryJob`, `RetentionDisposalMonthly`, `SealVerificationDaily` (re-hash sample + chain check), `GraphWorkingCopySync`.

---

## 8. Integrations (ports and adapters; Appendix L)

| Port | Adapter(s) | Use |
|---|---|---|
| `ESIGN_PORT` | ASP adapters (Leegality, Digio, SignDesk, Surepass, Protean) → CCA-empanelled ESPs | Aadhaar eSign |
| `DSC_PORT` | Local signer utility / browser extension; cloud-HSM DSC providers | DSC signing |
| `STORAGE_PORT` | S3-compatible (primary); tenant BYO: SharePoint/OneDrive (Graph), Google Drive, Azure Blob, GCS, SFTP (P19) | Storage and intake |
| `WORKSPACE_PORT` | Microsoft 365 (Graph: drive items, co-authoring, change notifications); Google Workspace (later, D-10) | Co-authoring and publishing to intranet |
| `EDITOR_PORT` | Collabora Online / ONLYOFFICE (WOPI host implemented by LDC) — flag | Embedded editing |
| `OCR_PORT` | Tesseract (printed, in-cluster); Vidhi vision (P17) for handwriting/screenshots; optional cloud OCR in-region | OCR |
| `MT_PORT` | Claude via P17; Bhashini and others after evaluation | Translation |
| `AV_PORT` | ClamAV; commercial AV | Malware scanning |
| `MAIL_IN_PORT` | Inbound mail service (SES inbound or equivalent in-region) | E-mail-in |
| `ESTAMP_PORT` | e-stamping providers (flag OFF) | Stamp duty |
| `CONVERT_PORT` | Gotenberg/LibreOffice | PDF, PDF/A, renditions |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `pol.review.default_frequency_months` | T | 12 | ≤ instrument-prescribed frequency | CCO |
| `pol.review.reminder_offsets_days` | T | [60, 30, 7] | — | CCO |
| `pol.review_sla_days` | T | 5 | 1–30 | CCO |
| `pol.route.<policy_type>` | T (G for regulatory-mandated end approver) | default route | must include required approver | Admin + CCO |
| `pol.signed_copy.required` | G | true for Board-approved policies | — | CCO + checker |
| `pol.scan_match.min_similarity` | T | 0.97 | 0.90–1.00 | CCO |
| `pol.redline.author_label` | L | "Vidhi AI (draft)" | — | — |
| `pol.attestation.reminder_days` | T | [3, 7, 14] | — | HR/CCO |
| `pol.attestation.new_joiner_days` | T | 15 | 1–60 | HR |
| `pol.baton.nudge_cooldown_hours` *(v1.1)* | T | 24 | 4–72 | CCO |
| `pol.review.parallel_lanes_enabled` *(v1.1)* | T | ON | sequential lanes Locked by rule pack | CCO |
| `pol.drift.enabled` *(v1.1)* | T | ON | — | CCO |
| `pol.drift.parameters` *(v1.1)* | T | all | multi-select | CCO |
| `pol.quiz.pass_mark_pct` *(v1.1)* | T | 70 | 50–100 | HR/CCO |
| `pol.quiz.max_attempts` *(v1.1)* | T | 3 | 1–10 | HR/CCO |
| `pol.bulk.undo_hours` *(v1.1)* | T | 24 | 1–72 | CCO (NN-49) |
| `pol.ai.va05.autonomy_ceiling` *(v1.1)* | T | L1 | L0–L1 | CCO (NN-50) |
| `dms.render.progressive` *(v1.1)* | L | ON | — | — |
| `dms.addins.m365.enabled` / `dms.addins.google.enabled` *(v1.1)* | T | OFF | requires admin consent in the client suite | Admin |
| `dms.checkout.max_hours` | T | 24 | 1–168 | Admin |
| `dms.autoclassify.auto_apply_threshold` | T | 0.95 (OFF until enabled) | 0.8–1.0 | Admin |
| `dms.share.external.enabled` | T | ON | — | Admin |
| `dms.share.default_expiry_days` | T | 14 | 1–365 | Admin |
| `dms.share.require_otp` | T | ON | cannot be OFF for CONFIDENTIAL | Admin |
| `dms.share.watermark` | T | ON | — | Admin |
| `dms.share.board_confidential_requires_cs` | L | true | — | — |
| `dms.esign.methods_allowed` | T | [AADHAAR_ESIGN, DSC, SIMPLE_ACK] | SIMPLE_ACK only for acknowledgement doc types | Admin |
| `dms.esign.excluded_types` | L | First Schedule list | — | — |
| `dms.estamp.enabled` | G | OFF | requires adapter + state matrix | Platform |
| `dms.embedded_editor.enabled` | G | OFF | requires ADR + fidelity tests | Platform |
| `dms.intake.max_zip_gb` | T | 10 | 1–50 | Admin |
| `dms.intake.duplicate_policy` | T | LINK_EXISTING | LINK_EXISTING / KEEP_BOTH | Admin |
| `dms.translation.target_default` | T | en | — | Admin |
| `dms.translation.reverse.enabled` | G | OFF | human review mandatory | Platform |
| `dms.ocr.handwriting.enabled` | T | ON | requires AI provider consent (NN-15) | Admin |
| `dms.macro_files.allowed_folders` | T | [] | — | Admin + CISO |
| `dms.retention.<class>.years` | G | floor per rule pack | ≥ floor | CCO + checker |
| `dms.email_in.enabled` | T | ON | — | Admin |

---

## 10. Security, privacy and audit

- Encryption: SSE-KMS per tenant; separate keys for `BOARD_CONFIDENTIAL` and each `SEALED_*` class (NN-13); envelope encryption for external share renditions.
- WORM: sealed versions (approved evidence, signed documents, signed minutes, approved policies) in Object Lock compliance mode for their retention period (NN-09).
- Access: RLS and ABAC on every API, search and export (NN-01); pre-signed URLs short-lived (≤ 5 minutes) and bound to the user session; no public buckets.
- External recipients: OTP authentication, device fingerprint, rate limiting, generic error messages; their access is logged with IP and user agent.
- Personal data: identity numbers masked in previews and type copies by default (NN-12) with reveal permission; DPDP purpose capture on external shares of personal data; data-principal erasure flows through P12 with legal-retention checks.
- AI: tenant opt-in for AI processing per feature; no training on tenant content (NN-15); provider and region recorded on every extraction/translation (NN-24); untrusted-text handling (FR-P07-53).
- Audit: every view, download, print, share, sign, version, metadata change, hold, disposal and AI processing event is a ledger event (NN-02); per-document activity log visible to authorised users.
- Super-admin overrides on documents (R-071) follow D-02: replacing an evidence document creates a Correction Entry with reason and dual approval; the original version stays sealed and visible to the tenant.

---

## 11. AI touchpoints and guardrails (Appendix K)

| Touchpoint | Vidhi does | Guardrail |
|---|---|---|
| Policy drafting (5 modes) | Revised clause text with rationale and citations | Deterministic redline writes OOXML; citations validated; draft until approved (NN-04, NN-06) |
| Gap check | Mandatory-contents coverage report | Checklist is pack data; AI maps text to items, user confirms |
| Summaries | Policy summaries for employees, change summaries for the Board | Labelled AI; Board summary reviewed by owner |
| Classification | Type, entity, FY, department, links | Suggestions; auto-apply only above tenant threshold and never for sealed classes |
| OCR (handwriting/screenshots) | Text with confidence; `[illegible]` markers | Never guesses illegible text; human verification for `VERIFIED` |
| Field extraction | Reference numbers, dates, deadlines | Creates tasks only after user confirmation |
| Translation | English translation with segment confidence | MT label until reviewed; low-resource languages flagged |
| Search Q&A | Answers over permitted documents with citations (P17) | Permission-trimmed retrieval; no source → says so |
| Upload extraction *(v1.1)* | VA-05 proposes metadata and links for uploaded policies | Field-by-field acceptance; nothing applied automatically (NN-04) |
| Drift explanation *(v1.1)* | Explains the mismatch and drafts options | Never changes status, rating or policy (NN-47) |
| Quiz drafting *(v1.1)* | Drafts questions and answers from the approved policy text | Owner approves the quiz; questions cite clauses |
| Privileged documents *(v1.1)* | — | Excluded from AI retrieval for non-legal users (FR-P07-67) |

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p07/*.feature`)

```gherkin
Feature: Real tracked changes
  Scenario: Align KYC policy to an amended direction
    Given the approved "KYC Policy v3.0" and a published change item amending paragraph 38 of the KYC Master Direction
    When the CCO runs "Align to regulatory change"
    Then a new version v3.1 is created whose DOCX contains w:ins and w:del revisions authored "Vidhi AI (draft)"
    And each changed clause has a Word comment citing the change item and paragraph
    And accepting all revisions in Word produces text equal to the stored revised text

  Scenario: Unknown citation is never written
    Given Vidhi proposes a revision citing a paragraph that does not exist in the content library
    Then the redline marks the comment "Citation not found — review" in red
    And the version cannot move to READY_FOR_APPROVAL until the citation is fixed or removed

Feature: Approval evidence
  Scenario: Policy cannot become effective without signed copy
    Given policy version v3.1 is APPROVED with P06 decision BM-2026-09/item 7
    When the CCO tries to set it EFFECTIVE without uploading the signed copy
    Then the transition is rejected with LDC-POL-014

  Scenario: Scanned copy differs from approved text
    Given an uploaded signed scan with similarity 0.91 to the approved version
    Then the CS must review the highlighted differences and confirm before EFFECTIVE

Feature: Review calendar
  Scenario: Overdue review raises a compliance issue
    Given policy "Outsourcing Policy" next review date was yesterday and no review is in progress
    When the daily scheduler runs
    Then a compliance issue is opened for the owner department with severity HIGH

Feature: Selective sharing
  Scenario: Share pack contains only ticked documents
    Given a user ticks 3 of 12 documents in a folder and creates a view-only share with OTP and 7-day expiry
    When the recipient authenticates
    Then only the 3 documents are visible, watermarked with the recipient e-mail
    And downloads are not offered
    And revoking the share blocks access within 60 seconds

  Scenario: Sealed class cannot be shared externally
    Given a document of class SEALED_POSH
    Then the "Share externally" action is not available and the API returns LDC-DMS-021

Feature: eSign
  Scenario: Excluded instrument blocked
    Given a document typed "Power of Attorney"
    When a user adds it to an eSign envelope
    Then the system blocks e-signature and shows the physical execution checklist

  Scenario: Aadhaar eSign completion certificate
    Given an envelope with two external signers using Aadhaar eSign
    When both sign
    Then the signed PDF and a certificate of completion with document hashes and ESP transaction IDs are sealed
    And no Aadhaar number or OTP is stored anywhere in LawDocsComply

Feature: Type copy
  Scenario: WhatsApp screenshot to verified type copy
    Given three overlapping WhatsApp screenshots uploaded to a grievance record
    When processing completes
    Then a single transcript with sender, timestamp and message text is produced without duplicate messages
    And low-confidence words are highlighted
    And after a user corrects and verifies it, the original screenshots and the verified type copy are both attached

Feature: Translation
  Scenario: Marathi letter translated
    Given a scanned Marathi letter from a co-operative registrar
    Then the language is detected as Marathi and an English translation with segment alignment is produced
    And it is labelled "Machine translation — not verified" until a reviewer marks it REVIEWED

Feature: Folder intake
  Scenario: Re-import of an LDC export maps automatically
    Given an LDC-EXPORT-1.0 package exported from another tenant environment
    When it is uploaded through Folder Intake
    Then 100% of files are mapped using the manifest with no manual mapping
    And duplicates already present are linked, not duplicated, and nothing is overwritten

Feature: Search permission trimming
  Scenario: No snippet leakage
    Given a document a user cannot open contains the word "embezzlement"
    When the user searches "embezzlement"
    Then the document does not appear and no snippet is returned
```

NN tests: `NN-01_search_permission_trimmed`, `NN-02_document_override_is_correction_entry`, `NN-04_policy_draft_not_effective_without_approval`, `NN-05_policy_reviewer_not_maker`, `NN-06_redline_citations_validated`, `NN-09_sealed_version_object_lock`, `NN-10_canonical_path_from_metadata`, `NN-11_release_does_not_change_paths`, `NN-12_aadhaar_never_stored_esign`, `NN-13_sealed_class_not_shareable`, `NN-14_document_text_untrusted_no_tool_exec`, `NN-15_no_training_flag_on_ai_calls`.


```gherkin
# v1.1 scenarios
Feature: Policy cycle speed
  Scenario: Baton shows holder and allows a nudge
    Given policy version "POL-KYC-001 v4.1" has been with reviewer "Head – Risk" for 6 days and the SLA is 5 days
    When the CCO opens the review baton board
    Then the card shows "Head – Risk · 6 days · overdue" in red
    And pressing Nudge sends one reminder and disables Nudge for 24 hours

  Scenario: Parallel lanes consolidate comments
    Given lanes Risk, IT and DPO are configured as parallel for the Information Security Policy
    When all three lanes sign off
    Then the version moves to READY_FOR_APPROVAL
    And the comment pane shows comments from all three lanes per clause

Feature: Policy–practice drift
  Scenario: Frequency mismatch creates a drift item
    Given clause 7.2 of the Outsourcing Policy is tagged FREQUENCY = quarterly with owner role RMC
    And the last two RMC reviews of outsourcing were 182 days apart
    When the nightly drift job runs
    Then a drift item is created for the policy owner citing both meetings
    And no compliance status or risk rating changes

Feature: Bulk roll-forward is reversible
  Scenario: Undo within window
    Given the CCO rolled forward next-review dates of 25 policies
    When she clicks Undo within 24 hours
    Then all 25 dates return to their previous values through a compensating change
    And the ledger shows both the bulk change and the reversal

Feature: Forms library boundary
  Scenario: Onboarding form published without capturing customer data in LDC
    Given the non-individual onboarding form v2 is published
    Then Finbyx receives the form definition through the ecosystem template feed
    And LDC stores no customer onboarding submissions
```

NN tests added *(v1.1)*: `NN-46_no_bulk_policy_approval`, `NN-47_drift_never_changes_status`, `NN-49_policy_bulk_undo`, `NN-50_va05_cannot_advance_beyond_draft`, `NN-54_foreign_policy_official_language_is_approved_text`.

---

## 13. Deliverables and exit gate

**Deliverables:** `pol` and `dms` modules with migrations; `packages/redline` (with CI round-trip validation); ingestion, OCR, type-copy and translation pipelines; eSign envelope service with at least one ASP adapter in sandbox; share service and external viewer; folder intake with mapping rules; retention rule pack seed; model templates for the first 20 required policies of NBFC-ML and listed entities (legal analyst signed); tenant template merge; Microsoft 365 co-authoring adapter (sandbox tenant); Appendix M mapping implemented; acceptance and NN tests; `docs/phases/P07-plan.md`, `docs/phases/P07-handover.md`.

**Exit gate:**

1. All Gherkin and NN tests green; redline round-trip suite passes on 50 real-world policy documents (tables, numbering, headers, footnotes).
2. Pilot tenant runs one policy end to end: model → Vidhi draft → reviews → P06 Board approval → signed copy → effective → attestation campaign with ≥ 90% completion.
3. Search p95 ≤ 1.5 s on a 1-million-document synthetic tenant; permission-trimming penetration test passed.
4. eSign: Aadhaar eSign and DSC flows completed in sandbox with certificate of completion; excluded-document block verified.
5. OCR/translation evaluation report from P17 attached, with per-language quality tiers published; tier A enabled only where evaluation passes.
6. Folder intake of 5,000 files with mapping preview and zero overwrites; re-import of an LDC export maps 100%.
7. WCAG 2.2 AA audit of viewer, type-copy workbench and share builder passed (NN-21); screen-reader reading order verified for type copies.
8. *(v1.1)* Drift job produces the expected items on the golden tenant; an attestation campaign with quiz completes with certificates; 20 uploaded legacy policies are mapped through the extraction review in ≤ 15 minutes; 100-page PDF first-page render < 2 s.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P07-01 | Microsoft CSPP eligibility for WOPI-based Office for the web | Program limited to cloud-storage ISVs | CTO | Graph co-authoring via tenant SharePoint/OneDrive; embedded editor flag OFF |
| OI-P07-02 | Licence choice for embedded editor (Collabora Online vs ONLYOFFICE) and tracked-changes fidelity | Licence/fidelity | CTO | `dms.embedded_editor.enabled = OFF` |
| OI-P07-03 | ASP vs ESP contracting (Leegality/Digio/SignDesk/Surepass are application service providers over CCA-empanelled ESPs) and commercial terms | Vendor | CTO/Procurement | Sandbox only |
| OI-P07-04 | Current IT Act First Schedule list and any amendments | Statute check | Legal analyst | Seed list in §4N; block-by-default |
| OI-P07-05 | State-wise e-stamping matrix and adapter | Varies by state | Legal analyst | `dms.estamp.enabled = OFF`; manual stamping checklist |
| OI-P07-06 | Retention floors (Income-tax Act 2025 records, Labour Codes registers, RBI record retention post-2025 consolidation) | Statute check | CCO/legal | Conservative floor (8 years) applied to unverified classes |
| OI-P07-07 | Per-language OCR/MT quality for low-resource scripts (Ol Chiki, Meetei Mayek, Kashmiri, Sindhi, Dogri, Bodo, Santali) | Evaluation | P17 | Tier C (review mandatory) |
| OI-P07-08 | Bhashini API terms, residency and retention | Vendor terms | CTO | Not enabled |
| OI-P07-09 | Mandatory-contents checklists for each required policy (per pack) | Content work in P15 / Part 2 | Content team | Gap check shows "checklist not available" |
| OI-P07-10 | Website-publication requirements per regulator for policies (Fair Practices Code, grievance policy etc.) after 2025 consolidation | Content check | P15 | Publication flag per policy without legal assertion |
| OI-P07-11 | BSA 2023 s.63 certificate format for type copies vs originals (Part A/B) | Legal interpretation | Legal analyst | Type copy footer + original attached; certificate from P19 for exports |
| OI-P07-12 *(v1.1)* | Ecosystem template feed for forms to Finbyx/Udofin (contract name and payload) | Ecosystem Spec v1.2 change request | Integration lead | Manual DOCX/JSON download |
| OI-P07-13 *(v1.1)* | Outlook/Gmail add-in distribution and admin-consent requirements per M365 plan (D-10) | Vendor policies | CTO | Add-ins OFF; e-mail-in (§4T) remains |
| OI-P07-14 *(v1.1)* | DPDP consent-form model text after the 13 Nov 2026 phase (consent managers) | Rule phase | DPO analyst | Current Rule 3 notice template |
| OI-P07-15 *(v1.1)* | KYC checklist alignment with RBI (KYC) Directions in the 2025 consolidated set (catalogue lookup) | Content | Content team | Model forms marked [VERIFY] |
| OI-P07-16 *(v1.1)* | Quiz question quality evaluation set for VA-05 | P17 eval | AI lead | Quizzes owner-authored only |
| OI-P07-17 *(v1.1)* | Jurisdiction model templates for foreign subsidiaries | P25 pack coverage | Global content lead | Tenant-uploaded templates only |

---

## 15. Sources (accessed 25 October 2026)

1. Information Technology Act, 2000 — ss.3, 3A, 10A, First Schedule and Second Schedule (as amended) — https://www.indiacode.nic.in
2. Controller of Certifying Authorities — External empanelled eSign Service Providers — https://cca.gov.in/service-providers.html
3. CCA — eSign API Specifications v2.1 — https://www.cca.gov.in/sites/files/pdf/ACT/eSign-APIv2.1.pdf ; eSign Empanelment Guidelines — https://www.cca.gov.in/sites/files/pdf/esign/CCA-ESP.pdf
4. Microsoft Learn — Microsoft 365 Cloud Storage Partner Program (Office for the web / WOPI eligibility) — https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online ; WOPI requirements — https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/online/wopi-requirements
5. ECMA-376 / ISO/IEC 29500 Office Open XML — revision marks (`w:ins`, `w:del`, `w:rPrChange`, `w:pPrChange`) and comments.
6. Companies Act, 2013 ss.88, 118, 128(5) and Companies (Management and Administration) Rules, 2014 (retention and electronic records) — https://www.mca.gov.in
7. SEBI LODR Regulations 2015, Reg 9, Reg 30(8), Reg 46; SEBI PIT Regulations 2015, Reg 3(5)–(6) — https://www.sebi.gov.in
8. Prevention of Money-laundering Act, 2002 s.12 and PML (Maintenance of Records) Rules, 2005 — record retention.
9. CGST Act, 2017 s.36 — retention of accounts.
10. Digital Personal Data Protection Act, 2023 s.8(7) and DPDP Rules, 2025 — https://www.meity.gov.in
11. Constitution of India, Eighth Schedule (22 languages); United Nations official languages (Arabic, Chinese, English, French, Russian, Spanish).
12. RBI (NBFC – Governance) Directions, 2025 (policy requirements: paras 7, 12, 25, 29–37, 38, 40) — https://taxguru.in/rbi/rbi-non-banking-financial-companies-governance-directions.html
13. NAVEX PolicyTech product page (benchmark only) — https://www.navex.com/products/policytech-policy-procedure-management-software
14. Owner's baseline: LawDocs Comply Architecture Part 1 (Document Management (DMS) screen spec; Board Pack Builder; Forms — customer onboarding individual and non-individual, DPDP consent, grievance, incident) and Part 2 (Documents & Forms Library).
15. *(v1.1)* Appendix Z (G2 feedback: PolicyTech reviews on hand-offs and attestation chasing; Vanta policy onboarding and drift; Diligent large-PDF complaints) — internal.

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-37 (deterministic redline engine), X-04 (ESP/ASP terms), X-06 (Graph co-authoring default).

**Added in v1.1:** NN-47, NN-50.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
