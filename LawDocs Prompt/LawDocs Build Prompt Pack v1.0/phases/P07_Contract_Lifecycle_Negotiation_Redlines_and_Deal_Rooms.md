# Phase P07 — Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Vault/DMS: `doc_`/`ver_`, Object Lock, sharing, bulk intake); P06 (templates, clause library, position ladders, tenant playbooks, drafts); P02 (org structure, positions, DoA attributes, maker-checker engine, delivery grants); P03 (settings, `RULES_PORT` decision tables); P01 (accounts, `CP_GUEST` magic-link + OTP, step-up MFA); P09 runtime (Vidhi gateway, credit metering); P05 (OCR of scanned counterparty paper — Wave 2; until then PDF intake is text-layer only). Hand-off: P08 (eSign, eStamp, formalities, evidence). Later consumers: P11 (disputes from contracts), P13 (CLO dashboard, governance approvals, legal intake desk), P20 (export).
> **Sequencing:** Sprint 1–2: agreement record, deal room, guest access, messaging, version sharing. Sprint 3–4: `packages/redline` compare/accept/reject, rounds, silent-edit detection. Sprint 5: approvals/DoA, version lock, P08 hand-off. Sprint 6: obligations, key dates, renewals, amendments. Sprint 7: intake (form, email, Teams), repository views, legacy import, CLO dashboard. Sprint 8: company-to-company rooms, Office/Google co-editing, AI playbook redlines, hardening. **Freeze point:** the version/visibility model and change-record schema (§4F) freeze at the end of sprint 3 — P08 signs locked hashes from it.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (taxonomy for agreement types), F (instrument eligibility gate, owned by P08), H (agent roster), K (`LD-EXPORT-1.0`), R (settings), W (open items), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-006, R-007, R-011, R-018 (CLO/KMP agents, contract part), R-026, R-027, R-030, R-043, R-047, R-053, R-055, R-060, R-064, R-067, R-077, R-086 (SpotDraft/Ironclad/Leegality parity), R-091.
> **Decisions applied:** D-02, D-10, D-12, D-17 · **Challenges applied:** CH-12, CH-14, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-24, NN-28, NN-34, NN-37, NN-40, NN-43, NN-45, NN-46
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, redline/OOXML 1, integrations 1, QA 1).

---

## 1. Objective and business outcome

Two parties — two people, two companies, or one of each — must agree a text, know exactly what changed in every round, keep their internal discussion private, get the right internal approvals, and send the one agreed version to signature. After signing, the company must never miss a renewal, a notice window or a payment obligation. P07 delivers this as LawDocs' contract lifecycle (Ironclad's Create → Review → Approve → Sign → Store → Fulfil → Analyse, adapted — R1 §8), with deal rooms where parties message while negotiating (R-077) and a **deterministic** redline engine (NN-37).

The brief says "the tool sufficient instead of a legal team". We build the legal-operations layer a single CLO can run — intake, playbooks, approvals, obligations — with Vidhi as a maker and professionals on demand (CH-14, D-17). We do not claim it replaces advocates.

| Outcome | Exit-gate measure |
|---|---|
| Faster cycle | Median intake → locked version for NDAs ≤ 1 working day in pilot tenants; TAT measured per type |
| Every change accountable | 100% of changes between any two shared versions are listed with author, round and decision; accept/reject logged per change (NN-37) |
| No silent edits | 100% of untracked differences in a counterparty-returned DOCX are detected and shown (test corpus of 200 files) |
| Internal stays internal | 0 internal comments, internal versions or internal metadata in any file or view available to a counterparty (automated test on every share) |
| Right approvals | No version reaches signing without the approvals the DoA matrix requires for that version hash |
| Nothing lapses | Every executed agreement has verified key dates; renewal and notice-window reminders fire at configured offsets |
| Low friction for counterparties | A guest can review, comment, upload a redline and confirm the agreed version without creating an account, ≤ 3 taps from the invitation |

---

## 2. Scope (in / out)

**In scope:** contract intake (web form, mobile, email-in, Microsoft Teams app); agreement record and matter linkage; authoring from P06 templates, tenant templates or third-party paper; deal rooms with internal and counterparty participants (`CP_GUEST`); secure messaging, threads and clause-anchored comments with internal vs shared channels; negotiation rounds; deterministic compare of any two versions; accept/reject per change; silent-edit detection; playbook-based AI redline suggestions (maker-only); approval workflows (DoA matrix, maker-checker, delegation); version lock and hand-off to P08; post-signature repository; obligation and key-date extraction with human verification; renewals, terminations, amendments, novations; repository views and legacy import; CLM dashboards for the CLO; company-to-company contracting where both parties are on LawDocs; optional co-editing in the customer's own Microsoft 365 or Google Workspace; bulk contracting from a spreadsheet.

**Out of scope (owner phase):** eSign, eStamp, signing order, evidence packs, wet-ink execution recording — **P08**. Template and clause authoring, playbook authoring UI — **P06**. Litigation and dispute management arising from a contract — **P11** (and Equator via `int`). Board/committee approvals as governance records — **P13** (`gov` kernel; LDC is SoR where the tenant uses LDC — NN-47). OCR of scans — **P05**. Legal spend and counsel panel — **P13**. CRM (deal pipeline of the customer's sales team) — not LawDocs; CRM connectors are P19.

---

## 3. Personas and permissions touched

| Role code | P07 permissions (full matrix: Appendix D) |
|---|---|
| `ORG_MEMBER` | Raise intake requests; view own requests and agreements shared with them; comment internally; cannot share externally unless granted |
| `ORG_LEGAL_MAKER` | Triage intake; create agreements; open deal rooms; invite counterparties; share versions; accept/reject changes; request approvals; lock version (after approvals); verify obligations |
| `ORG_DELEGATED_MAKER` | Same as maker within a delivery grant (RM-as-maker, D-02); never approver for the same agreement (NN-17, NN-18) |
| `ORG_CHECKER` | Review maker's work where the DoA requires a legal check; cannot be the maker of that version |
| `ORG_APPROVER` | Approve per DoA (authorised signatory / budget owner); approval bound to the version hash |
| `ORG_DEPT_HEAD` | Department approvals; department dashboards |
| `ORG_CLO` | All legal-maker rights; configure playbooks, DoA matrix (with checker), intake forms; CLO dashboard; override with recorded reason (except NN-gated steps) |
| `ORG_KMP`, `ORG_DIRECTOR` | Approvals where DoA routes to them; dashboards; board-approval routing to P13 |
| `ORG_EXT_COUNSEL` | Guest internal counsel: internal channel access to assigned agreements only |
| `ORG_AUDITOR_RO` | Read-only repository, audit and approvals |
| `IND_OWNER` | Personal deal rooms: invite the other party, negotiate, lock, hand off to signing |
| `CP_GUEST` | View shared versions, comment in shared channel, upload a revised DOCX, propose changes in the clause editor, confirm agreed version; upgrade to an account |
| `OPS_RM`, `OPS_PROFESSIONAL` | Through delivery grants only: act as maker or reviewer for retainer clients (NN-17) |
| `AGT_*` (CLM agents per Appendix H) | Maker-only: draft redline suggestions, extract obligations, prepare summaries, chase approvals internally; never share, accept on behalf of a human, approve, lock or sign (NN-13, NN-43) |

---

## 4. Functional requirements

### 4A. Contract intake

**FR-P07-01 — Intake channels.** Business users request a contract through: (a) the web/mobile intake form; (b) email to the tenant's intake alias (`contracts+<tenant-slug>@in.lawdocs.in`, configurable custom domain alias via forwarding); (c) the Microsoft Teams app ("Request a contract" message extension and bot with an Adaptive Card form; requires the customer's M365 admin consent — CH-29 notes the owner's own M365 plan name must be confirmed, but the client-side Teams app works with any M365 business plan that includes Teams [VERIFY]); (d) a P19 API for the customer's own systems. Google Chat follows when Google Workspace support lands (R-055).

**FR-P07-02 — Intake form designer.** Tenants build intake forms per request type (NDA, vendor agreement, customer agreement, employment, lease, consultancy, "review counterparty paper", "other") with fields: requester (auto), department (auto from P02), counterparty (search or new), purpose, value (INR, NUMERIC), term, start date, data processing involved (Y/N → DPA module), cross-border (Y/N), deadline, attachments (counterparty draft, quote, email), confidentiality class. Conditional fields (CEL). Click budget: Teams/email user → submitted request ≤ 3 interactions.

**FR-P07-03 — Auto-template selection and triage.** On submission the rules engine maps request type + answers to: a P06 template (or tenant template), the playbook, the assignee pool (legal maker by department/type/load), priority and target TAT. Low-risk standard requests (e.g., mutual NDA on own paper, value ≤ threshold, no deviations) may be configured for **self-serve**: the requester completes the template interview and the agreement goes straight to approvals without a legal maker (`clm.intake.self_serve_types`). Counterparty-paper requests always go to a legal maker.

**FR-P07-04 — Email-in hygiene.** SPF/DKIM/DMARC evaluation; only senders whose address belongs to a tenant user (or approved domain) create requests; others are held for maker review; attachments pass P04 malware/active-content scanning before use; the email body becomes the first internal message; no auto-reply discloses tenant information to unknown senders.

**FR-P07-05 — Intake queue.** Queue with SLA badges, assignment, bulk assign, "need more info" (sends a message to the requester), duplicate detection (same counterparty + type within 30 days), conversion to agreement in 1 tap. A Company tenant has **one front door** (Appendix A §A.29, Resolution R-A-13): when `lgo` (P13 Company Legal Department OS) is enabled for the tenant, contract requests are raised as legal requests (`lrq_`, A.46) and conversion creates the `clm.intake_request` directly in `TRIAGED` with the `lrq_` link; when `lgo` is not enabled, this CLM intake stands alone. Web, mobile, Teams and email-in channels post to whichever front door is active. IDs and history carry over without migration when a tenant enables `lgo` (NN-12).

### 4B. Agreement record and matter linkage

**FR-P07-06 — Agreement record.** `clm.agreements` (`agr_`, business ref `LD-AGR-YYYY-NNNNNN`): title, type (Appendix E canonical doc ID or tenant type), paper (OWN / COUNTERPARTY / JOINT), parties (`prs_`/`org_` with roles), internal owner, department, entity (`ent_`), value and currency, term, governing law, dispute-resolution clause summary, confidentiality class, status (§5.2), linked intake request, linked matter(s), parent agreement (for amendments/renewals), tags, custom fields (tenant-defined, typed).

**FR-P07-07 — Matter linkage.** An agreement can link to one or more matters (`mat_`): a transaction matter (e.g., "Series A financing" with SHA, SSA, disclosure letter), a dispute matter in P11, or an advisory engagement in P16. Matter views list linked agreements with status; access follows the stricter of the two scopes.

**FR-P07-08 — Counterparty record.** Counterparty organisations and individuals are tenant-scoped contacts (verified by P01 KYB/KYC where the counterparty chose to verify). Show agreement history, open negotiations, obligations owed and owing, and related-party flag (Companies Act 2013 s.188 — flag for P13/LDC governance routing, not a legal determination [INTERP]).

### 4C. Authoring paths

**FR-P07-09 — From a template.** Creating from a P06 template or tenant template opens the P06 interview; the completed draft becomes version 1 (`ver_`, visibility `INTERNAL`). Lane and review state travel with it (NN-14).

**FR-P07-10 — Third-party paper.** Upload DOCX (preferred) or PDF. DOCX is normalised (existing tracked changes preserved as-is and listed; comments preserved as internal unless the maker marks them shared). PDF with a text layer is converted to DOCX with a fidelity warning; scanned PDF goes to P05 OCR (Wave 2) and is labelled "Converted from scan — verify against original" (NN-09: the original stays immutable). Vidhi may run a playbook review (§4G) and a "what's missing" check (P06 FR-P06-32).

**FR-P07-11 — Version model.** Every saved state is a version `ver_` with: number (v1, v2 …), author side (OURS / THEIRS / JOINT), producer (USER, TEMPLATE, AI_SUGGESTION_ADOPTED, COUNTERPARTY_UPLOAD, CO_EDIT_CHECKIN, REVIEWER), visibility (`INTERNAL` or `SHARED` with a list of counterparty parties), parent version, SHA-256 of the DOCX and of the normalised text, round number, lock state. Versions are immutable (NN-09); "edit" creates a new version.

### 4D. Deal rooms and guest access

**FR-P07-12 — Deal room.** Each agreement under negotiation has a deal room: participants panel (internal team, each counterparty party's members), versions timeline, changes view, shared thread and internal thread, documents (supporting files such as quotes, annexures, KYC documents — each with its own visibility), tasks, approvals panel (internal only), and the "agreed version" status. Individuals get the same room in a simplified layout.

**FR-P07-13 — Inviting a counterparty.** The maker invites by email and/or mobile. The invitation is one LawDocs-originated message plus at most `clm.dealroom.invite_reminders_max` (default 2) reminders, which the recipient can stop; no automated calls (NN-34). The invite shows the inviting party's verified name and the agreement title only — never the content in the email body.

**FR-P07-14 — Guest authentication.** `CP_GUEST` access: magic link (single-use, TTL `clm.dealroom.guest_link_ttl_days`, default 14) + OTP to the invited email or mobile (locked ON); session bound to device; re-authentication after 12 hours idle; optional upgrade to a full account (keeps history). A guest from a company may add colleagues only if the inviting maker allows (`clm.dealroom.guest_can_add_members`, default OFF) and each added colleague is OTP-verified.

**FR-P07-15 — Room controls.** Per room: download allowed (Y/N), watermark (guest name, email, timestamp on every page of viewed/downloaded PDFs; DOCX downloads carry a custom property with the guest ID), print allowed, expiry date, NDA click-through before first view (template from P06, acceptance logged as an e-contract event under IT Act s.10A — R3 LG-002), IP allow-list (enterprise). Defaults per tenant; overridable per room by the maker.

**FR-P07-16 — Access log.** Every view, download, upload, message and confirmation by every participant is logged and visible to the room owner; guests see their own log (transparency). Revoking a participant takes effect within 60 seconds on all sessions.

**FR-P07-17 — Multi-party rooms.** Rooms support more than two parties (e.g., tripartite agreements, lender–borrower–guarantor). Each version's visibility lists exactly which parties may see it; a party never sees another party's private thread.

### 4E. Secure messaging (`msg`)

**FR-P07-18 — Channels.** Each room has: **Internal** channel (own team only — never shared, NN-37), **Shared** channel (all parties), and optional **party-private** channels in multi-party rooms. Every message composer shows a persistent coloured banner with text: "Internal — only [Company A] can see this" or "Shared with [Company B]". Switching channel requires an explicit tap; pasting text from the internal channel into the shared composer triggers a confirmation (text-similarity check ≥ 0.8).

**FR-P07-19 — Clause-anchored comments.** Comments attach to a clause/paragraph range in a version (anchor survives into later versions by paragraph alignment; orphaned anchors are shown as "comment on removed text"). Comment visibility = channel. In shared DOCX exports, only shared comments are written as Word comments; internal comments are written only into internal exports.

**FR-P07-20 — Message features.** Mentions (internal only can mention internal users), attachments (scanned, versioned in P04), reactions, edit within 5 minutes with "edited" marker and history, delete only as a correction entry (NN-02) with "message withdrawn" placeholder, read receipts (configurable), translation of a message on request (P09, labelled machine translation — NN-48), voice notes on mobile (transcribed on request).

**FR-P07-21 — Notifications.** In-app, push, email digest; per-user quiet hours; counterparties receive notifications only for shared-channel activity and version shares, within the NN-34 caps; no WhatsApp for negotiation content (R6 D-31 rule: WhatsApp never for legal notices — we extend it to negotiation content by default; `clm.notify.whatsapp_enabled` default OFF and only for status pings without content).

**FR-P07-22 — Messaging while signing.** During P08 signing, the room's shared channel stays open so parties can message ("where do I sign?"); messages after lock cannot change the locked text — any agreed change requires unlocking (FR-P07-43).

### 4F. Negotiation rounds and the deterministic redline engine

**FR-P07-23 — Rounds.** A round (`neg_`) opens when a side shares a version with the other side and closes when the other side returns a version, confirms it as agreed, or withdraws. The room shows "ball in court" (whose turn), round number, days in round, and round summary (changes proposed / accepted / rejected / open; clauses touched). Round SLAs are informational (`clm.negotiation.round_nudge_days`, default 5).

**FR-P07-24 — Sharing a version.** The maker selects an internal version → "Share with [party]". The engine produces the shared artefact: clean DOCX or DOCX with tracked changes against the last version that party saw (maker's choice), only shared comments, sanitised metadata (docProps author/company/manager, custom XML, revision IDs that reveal internal authors are rewritten to "[Company A]"; hidden text, document variables and personal information removed), and a PDF view. A pre-share check lists anything that would leak (internal comments, hidden text, tracked changes from internal-only versions, file properties) and blocks until resolved (LD-CLM-021). This check is an NN-37 test fixture.

**FR-P07-25 — Receiving a version.** The counterparty uploads a DOCX (or edits in the clause editor, FR-P07-29). The engine compares the upload with the **exact version last shared to that party** and classifies differences:
- `TRACKED` — present as Word revisions (insert/delete/move/format) with author/date;
- `UNTRACKED` — text differs but no revision mark exists ("silent edit");
- `COMMENT` — new or changed comments;
- `STRUCTURE` — numbering, tables, headers/footers, sections, fields.
Untracked changes are highlighted in red with the banner "Changes made without track changes" and must each be acknowledged before the version can be accepted or locked (LD-CLM-024). Event `in.lawdocs.clm.SilentEditDetected.v1`.

**FR-P07-26 — Compare any two versions.** Any participant can compare any two versions they are allowed to see (internal users: all; guests: shared versions only). Output: side-by-side and inline views, change list with filters (by clause, author side, type, round), statistics, export as redline DOCX (native `w:ins`/`w:del`) and redline PDF.

**FR-P07-27 — Engine algorithm (packages/redline).** Deterministic, versioned (`redline_engine_version` stored with every comparison):
1. Parse both DOCX files into a document model (paragraphs, runs, tables, lists with computed numbering, fields, footnotes, headers/footers); resolve existing tracked changes into a "proposed" view and a "base" view.
2. Normalise: Unicode NFC, whitespace folding, smart-quote and dash equivalence (configurable), numbering compared as computed values, field results compared by code.
3. Align paragraphs with an LCS over paragraph fingerprints plus move detection (paragraphs with similarity ≥ 0.85 at a different position are moves).
4. Within aligned paragraphs, word-level Myers diff; character-level within a word only for numbers and defined terms.
5. Tables: align rows by header + first-cell fingerprint; cell-level diff.
6. Emit change records `chg` (id, type, location anchors in both versions, old text, new text, author side, round, source = TRACKED/UNTRACKED).
7. Golden-corpus regression (≥ 300 real-world-style DOCX pairs including Indian legal formats, Devanagari and other Indic scripts) runs in CI; any output change requires a new engine version (old comparisons keep their recorded engine version).

**FR-P07-28 — Accept/reject per change.** On a received version, the maker decides per change: accept, reject, or counter (edit). Bulk accept/reject by filter (e.g., "accept all formatting"). Each decision is a logged event with user, time, change ID, and rationale (optional; mandatory for rejecting a counterparty change if `clm.negotiation.reject_reason_required`). The resulting text is computed deterministically from base + decisions and saved as a new internal version; the decision set is stored so the result can be recomputed and verified. Accepting all changes yields exactly the counterparty's proposed text (CI property test).

**FR-P07-29 — Clause editor (in-browser).** For parties without Word, an in-browser editor on the parsed model (ProseMirror/Tiptap-class editor [REC]) edits text at paragraph/clause level and writes every edit as a tracked revision under the editor's identity; complex formatting is preserved but not editable (banner: "For layout changes, use Word"). Guests propose changes here; their edits arrive as `TRACKED` changes.

**FR-P07-30 — Issues list.** Open points can be raised per clause (internal or shared), with owner, status (open / agreed / dropped) and link to changes; the round summary lists open issues. The agreed version cannot be confirmed while shared issues are open unless both sides mark them closed.

**FR-P07-31 — Negotiation history export.** One click produces the "Negotiation and Redlines" bundle for the agreement: every shared version, every comparison, the decision log, the shared thread and (for internal exports only) the internal thread — feeding the `02 Negotiation and Redlines` export folder (NN-11).

### 4G. Playbook-based AI redline suggestions (maker-only)

**FR-P07-32 — Playbook review.** On a counterparty version (or third-party paper), the maker can run "Review against playbook". Vidhi maps clauses to playbook clause keys (P06 FR-P06-51), compares each to the company's position ladder, and returns per clause: classification (matches STANDARD / within FALLBACK_n / beyond WALK_AWAY / missing / unusual), risk note, and a suggested redline using the library text of the target position (retrieval first; free generation only where no library text fits, marked "AI-written"). Credits: 15 per 10 pages (R6 seed).

**FR-P07-33 — Suggestions stay internal.** Suggestions are rendered as tracked changes authored **"Vidhi AI (suggestion)"** in an **internal** working version only. Nothing reaches the counterparty until a human adopts each suggestion and shares a version (NN-13, NN-43). The share-time leakage check (FR-P07-24) re-authors adopted suggestions to the adopting user's side label and removes the "Vidhi" author tag from shared files (the internal audit keeps the provenance).

**FR-P07-34 — Deviation tracking.** Each accepted counterparty position outside STANDARD becomes a `deviation` record (clause key, position, approver required per playbook); deviations feed the DoA (§4H) and the CLO dashboard.

**FR-P07-35 — Individual users.** For `IND_*` users, "Review the other party's draft" produces a plain-language risk summary (general information) and offers paid professional review (P16); AI-written counter-clauses follow the P06 AI-custom lane and review gate (NN-14).

### 4H. Approval workflows (DoA, maker-checker)

**FR-P07-36 — DoA matrix as a decision table.** Tenants configure (with maker-checker, NN-18) a GoRules ZEN table: inputs — agreement type, value band, term, department, entity, paper (own/counterparty), deviations (by clause key and position), data processing, cross-border, related-party flag, counterparty risk rating (tenant-entered), AI-custom/reviewed flag; outputs — ordered approval steps (role, position, named user, or group), parallel vs sequential, quorum (any 1 / all), legal check required, board/committee approval required (routes to P13), stamp/registration reminder. Templates of matrices are offered for SMEs (two-step: legal check + authorised signatory).

**FR-P07-37 — Segregation of duties.** Maker ≠ checker ≠ approver for the same version (where the matrix requires distinct steps); a delegated maker (RM) can never approve; delegation for leave goes to a named deputy, never to the maker (LD-CLM-031). Agents never approve (NN-43).

**FR-P07-38 — Approvals bound to a version hash.** Each approval records the version hash, the change summary since the previous approved version, deviations and the approver's comment. Any later change invalidates approvals according to `clm.approval.reapprove_on_change` (default `ALL`; option `MATERIAL_ONLY` where only changes in operative clauses re-open approvals, with the classification shown to the approver).

**FR-P07-39 — Approver experience.** Approvers act from web, mobile push (approve/reject with step-up for value above `clm.approval.stepup_value_inr`), email links that open the review screen after sign-in (never approve-from-email; P02 FR-P02-33) and Teams Adaptive Cards (same authentication and step-up). The approval card shows: summary, value, term, deviations with risk notes, what changed since last approval, and a link to the full redline. Click budget: push → decision ≤ 2 taps.

**FR-P07-40 — SLA and escalation.** Per step SLA (`clm.approval.sla_hours`, default 24 working hours), reminders, escalation to the step's escalation role, audit of overrides by `ORG_CLO` (reason mandatory; NN-gated checks cannot be overridden).

### 4I. Version lock and hand-off to signing (P08)

**FR-P07-41 — Agreed version.** The maker proposes a version as "agreed". Each counterparty party confirms ("This is the version we agree to sign") with OTP step-up; the internal side's confirmation requires all approvals complete for that hash. On full confirmation the version is **locked**: hash sealed, Object Lock applied to the DOCX and PDF (NN-09), status `LOCKED_FOR_SIGNATURE`.

**FR-P07-42 — Pre-sign gates (enforced again by P08).** (1) Instrument eligibility per Appendix F (NN-07) — wet-ink-only instruments get the print-sign-stamp-register pack; (2) stamp-before-sign requirement recorded (NN-08); (3) formalities list (witnesses, notary, registration, board approval) created for NN-40 tracking; (4) approvals complete for the locked hash; (5) AI-custom drafts for individuals reviewed (NN-14); (6) no unacknowledged untracked changes; (7) no open shared issues. Failure → LD-CLM-041 with the failing gate listed.

**FR-P07-43 — Unlock.** Unlocking needs a reason, the internal maker's request and the agreement owner's approval; it cancels any pending P08 signing request (P08 voids it with reason), notifies all parties and opens a new round. A signed version can never be unlocked; changes after execution go through amendment (§4K).

**FR-P07-44 — Hand-off.** "Send for signing" creates the P08 signing request with: locked version hash, party/signatory mapping from P06 signature blocks, signing order suggestion, stamp requirements, and the room's shared channel link. P08 returns `in.lawdocs.sgn.SigningCompleted.v1`; P07 moves the agreement to `EXECUTED` only after NN-40 formalities are recorded or waived by an authorised user (P08 owns the gate; P07 reflects the status).

### 4J. Obligations and key dates

**FR-P07-45 — Extraction.** On execution (or on import of a legacy agreement), Vidhi extracts candidate obligations and key dates from the executed text: party, obligation type (payment, delivery, reporting, insurance, compliance, confidentiality survival, audit right, SLA, exclusivity, non-solicit, IP assignment, data deletion), trigger, frequency, amount, due dates, clause anchor; key dates (effective date, expiry, renewal type — auto/option/none, renewal notice deadline, lock-in end, termination notice period, escalation dates, warranty end). Credits 10 per contract (R6 seed).

**FR-P07-46 — Human verification.** Candidates are `PROPOSED` until the agreement owner (or delegate) verifies each one: confirm, edit, reject (`clm.obligations.verify_required`, locked ON for key dates). Only verified items create reminders, tasks (`tsk_` in `wf`) and calendar entries. Deterministic date arithmetic (no model computes dates): e.g., `renewal_notice_deadline = expiry_date − notice_period`, with business-day rules from the tenant calendar.

**FR-P07-47 — Obligation tracking.** Each obligation has owner, status (upcoming / due / done / overdue / waived), evidence of performance (upload or link — e.g., insurance certificate, payment reference), and history. Overdue obligations raise items in the open/interim/waiting register (P03/`wf`, R-047) and on the CLO dashboard.

**FR-P07-48 — Reminders.** Default offsets T-90/T-60/T-30/T-7 for renewal and notice deadlines (`clm.renewal.reminder_offsets_days`), routed to owner, department head and CLO per settings; channels per user preference.

**FR-P07-49 — Savings evidence.** Avoided auto-renewals and on-time notices are logged as events for the P17 savings ledger with formula, inputs and evidence class (NN-36); "penalty avoided" is shown only where a verified obligation, due date and on-time completion exist.

### 4K. Renewals, terminations, amendments

**FR-P07-50 — Renewal decision.** Before the renewal notice deadline, the owner chooses: renew as is, renegotiate (opens a new deal room linked to the parent), let expire, or terminate. The decision is recorded and drives tasks.

**FR-P07-51 — Amendment flow.** "Amend" creates a child agreement from the P06 "Amendment agreement" template (D1.2.1) pre-filled with the parent's parties and references, or a variation letter; negotiation, approvals, lock and signing as usual. After execution, the repository shows an "as amended" consolidated reading view (derived, labelled "Consolidated for convenience — the signed documents prevail") and the parent's obligations/key dates are updated through verification.

**FR-P07-52 — Termination and other notices.** Termination notice (D1.2.5), revocation (D1.2.6), novation, assignment consent: generated from templates, approved per DoA, and **sent only by a human** (NN-13) through P10's notice dispatch (proof of delivery) or recorded as sent outside LawDocs with evidence.

**FR-P07-53 — Supersession chain.** Agreements show parent/child chains (original → amendments → renewal → termination), with effective dates and the currently operative set.

**FR-P07-54 — Expiry.** On expiry without renewal the status becomes `EXPIRED`; survival obligations (confidentiality, indemnities) remain tracked until their own end dates.

### 4L. Repository views and legacy import

**FR-P07-55 — Repository.** Views: all agreements; by status, type, counterparty, department, entity, owner, value band, governing law, expiry window, renewal type, signed method (eSign/DSC/wet-ink), paper; saved views per user and shared views per department; column chooser; export of view to XLSX. Full-text search across executed text (OCR text for scans via P05) with permission trimming. Folder paths are views over canonical IDs mirroring `LD-EXPORT-1.0` (NN-12).

**FR-P07-56 — Legacy import.** Bulk import through P04 folder intake: the user maps folders to agreement types/counterparties; Vidhi proposes metadata (parties, dates, value, type, renewal terms) per file; a verification queue lets staff (or the RM under a delivery grant) confirm in bulk with keyboard shortcuts; originals stay immutable; duplicates detected by hash and near-duplicate text.

**FR-P07-57 — Access control.** Agreement visibility: department, named users, confidentiality class (e.g., "Board-restricted"), ethical walls (users excluded from a matter); Cerbos ABAC; IDOR tests.

### 4M. CLM dashboards for the CLO

**FR-P07-58 — CLO dashboard.** Tiles and drill-downs: intake backlog and SLA; pipeline by stage; median/p90 TAT by type and by stage (bottleneck stage highlighted); approvals pending/overdue by approver; rounds per agreement; deviations accepted by clause key (top 10) and by approver; own vs counterparty paper ratio; renewals and notice deadlines in 30/60/90 days; value at risk (expiring without decision); overdue obligations; AI usage and credits; professional reviews ordered. Each chart has a data table (accessibility) and export.

**FR-P07-59 — Department and KMP views.** Department heads see their department; KMPs/board see a quarterly contracts summary (feeds the P13 board MIS); no individual-level productivity surveillance (NN-33) — metrics are agreement and SLA outcomes.

**FR-P07-60 — Customisation.** Tenants choose tiles, thresholds (e.g., "value at risk" threshold), fiscal year, and which custom fields appear in reports.

### 4N. Company-to-company contracting (both parties on LawDocs)

**FR-P07-61 — Connected rooms.** When an invited counterparty email belongs to an existing LawDocs tenant, the invitee may join as that tenant ("Join as [Company B]") instead of as a guest. Company B then gets a **mirror agreement** `agr_` in its own tenant linked to the room. Each side keeps its own internal channel, internal versions, approvals, playbook and DoA — none of which crosses (NN-37).

**FR-P07-62 — Replication, not shared rows.** When a version is shared, the platform copies the shared artefact (bytes + hash) into the receiving tenant's DMS under that tenant's keys; both tenants hold hash-identical copies. Shared-channel messages are replicated the same way. There is no cross-tenant RLS exception; replication runs in the `clm` service with an audit entry in both tenants (NN-01, NN-02).

**FR-P07-63 — Signing and evidence.** P08 runs one ceremony; each tenant receives the sealed signed copy and the evidence pack into its own vault. Obligations are extracted separately by each tenant (each verifies its own).

**FR-P07-64 — Exit.** If either tenant leaves LawDocs, its copies and history are in its export (NN-11); the other side's copies are unaffected.

### 4O. Office and Google co-editing option

**FR-P07-65 — Edit in Word (Microsoft 365).** Optional per tenant (`clm.coedit.provider = M365`): "Edit in Word" checks out the version, places the DOCX in the user's OneDrive/SharePoint app folder through Microsoft Graph (delegated permission scoped to the app folder [VERIFY permission name at build]), opens Word (desktop or web) for co-authoring with internal colleagues, and "Check in" pulls the file back as a new internal version, then runs the compare against the checked-out version so untracked co-authoring edits are surfaced (FR-P07-25). The temporary copy is deleted on check-in (`clm.coedit.delete_temp_copy`, default ON). The file lives in the customer's own suite (D-01 stack note).

**FR-P07-66 — Google Workspace.** `clm.coedit.provider = GOOGLE`: open the DOCX in Google Docs Office-editing mode via the Drive API, keeping the .docx format; check-in as above. Fidelity of tracked changes ↔ suggestions round-trip is **[VERIFY at build]**; until verified, the UI warns "Use Word for tracked-change negotiation" and the compare step still catches every difference.

**FR-P07-67 — Counterparties.** Counterparties never edit inside the customer's M365/Google tenant through LawDocs; they use download/upload or the clause editor. (Inviting external users into the customer's SharePoint is the customer's own choice outside LawDocs.)

**FR-P07-68 — WOPI option.** ONLYOFFICE/Collabora behind WOPI is an optional, licence-gated adapter (D-01) decided by ADR; off by default.

### 4P. Bulk contracting

**FR-P07-69 — Bulk generate.** From a P06 template and an XLSX/CSV (one row per counterparty — e.g., offer letters, NDAs, DSA agreements), generate agreements in bulk with per-row validation, preview of 3 random rows, approvals per DoA (batch approval allowed when every row is within STANDARD positions and the value band), and bulk hand-off to P08 (IMP-048). Errors per row are downloadable.

**FR-P07-70 — Bulk limits.** `clm.bulk.max_rows` (default 2,000 per batch); each row has its own `agr_`; invitations follow NN-34 caps per recipient.

---

## 5. Workflows and state machines

### 5.1 Intake request

State machine: Appendix A §A.29 governs (Resolution R-A-13: one front door per Company tenant; with `lgo` enabled the request enters here already `TRIAGED`, linked to its `lrq_`).

| State | Transitions | Actor | Guard / side effects |
|---|---|---|---|
| `SUBMITTED` | → `TRIAGED`, → `NEEDS_INFO`, → `REJECTED` | Legal maker / rules | Auto-triage; SLA starts |
| `NEEDS_INFO` | → `SUBMITTED` | Requester | Message thread |
| `TRIAGED` | → `IN_DRAFTING` (agreement created), → `SELF_SERVE` | Maker / rules | Template + playbook chosen |
| `SELF_SERVE` | → `IN_APPROVAL` | Requester | Only for configured low-risk types |
| `IN_DRAFTING` | → closed when agreement status ≥ `IN_NEGOTIATION` | — | `IntakeConverted` |
| `REJECTED` | terminal | Maker | Reason mandatory |

### 5.2 Agreement

State machine: Appendix A §A.30 governs; the ecosystem projection to Appendix Y #46 statuses follows Resolution R-A-14.

| State | Entry | Allowed transitions | Guard | Events |
|---|---|---|---|---|
| `DRAFT` | Created | → `IN_NEGOTIATION`, → `IN_APPROVAL`, → `CANCELLED` | — | `AgreementCreated` |
| `IN_NEGOTIATION` | First share | → `IN_APPROVAL`, → `CANCELLED` | — | `VersionShared`, `CounterpartyVersionReceived` |
| `IN_APPROVAL` | Approval requested | → `IN_NEGOTIATION` (changes), → `APPROVED` | DoA steps complete for hash | `ApprovalRequested`, `ApprovalDecided` |
| `APPROVED` | All approvals | → `LOCKED_FOR_SIGNATURE`, → `IN_NEGOTIATION` | All parties confirm agreed version | — |
| `LOCKED_FOR_SIGNATURE` | Lock | → `IN_SIGNATURE`, → `IN_NEGOTIATION` (unlock) | Pre-sign gates (FR-P07-42) | `VersionLocked` |
| `IN_SIGNATURE` | P08 request created | → `SIGNED_PENDING_FORMALITIES`, → `LOCKED_FOR_SIGNATURE` (void) | P08 | `HandedOffToSigning` |
| `SIGNED_PENDING_FORMALITIES` | `SigningCompleted` | → `EXECUTED` | NN-40 formalities recorded/waived (P08) | — |
| `EXECUTED` | Formalities complete | amendment marker (stays `EXECUTED` with an executed child — A.30), → `RENEWED`, → `TERMINATED`, → `EXPIRED` | — | `AgreementExecuted` |
| `TERMINATED` / `EXPIRED` | Notice/expiry | terminal (survival obligations continue) | — | `AgreementTerminated` / `AgreementExpired` |
| `CANCELLED` | Before signature | terminal | Reason | `AgreementCancelled` |

### 5.3 Change record (per change in a received version)

`PROPOSED → ACCEPTED | REJECTED | COUNTERED`; `UNTRACKED` changes start in `NEEDS_ACKNOWLEDGEMENT` → `PROPOSED`. Decisions are append-only; reversing a decision writes a new decision event.

### 5.4 Approval step

State machine: Appendix A §A.11 governs (Resolution R-A-06): `clm.approval_step` is a projection of the `wf` approval request bound to the agreement version hash — each step is a route step of one `apr_`; `INVALIDATED` = request `RETURNED`; `DELEGATED` = step reassigned under an active delegation; `clm.Approval*` events are notifications emitted after the corresponding `wf.*` event.

`PENDING → APPROVED | REJECTED | DELEGATED → (APPROVED | REJECTED) | INVALIDATED (version changed) | ESCALATED`.

### 5.5 Obligation

`PROPOSED → VERIFIED → UPCOMING → DUE → DONE | OVERDUE → DONE | WAIVED (reason, authorised role)`; `REJECTED` from PROPOSED.

### 5.6 Redline application (pseudo-code)

```ts
function applyDecisions(base: DocModel, proposed: DocModel, decisions: Map<ChangeId, Decision>, engineVersion: string): DocModel {
  const changes = redline.compare(base, proposed, { engineVersion });       // deterministic, versioned
  assert(changes.filter(c => c.source === 'UNTRACKED').every(c => decisions.get(c.id)?.acknowledged));
  let out = base.clone();
  for (const c of changes.sortedByAnchor()) {
    const d = decisions.get(c.id);
    if (d?.kind === 'ACCEPT') out = out.apply(c);
    if (d?.kind === 'COUNTER') out = out.apply(c).replaceRange(c.newAnchor, d.counterText, { tracked: true, author: d.userSide });
    // REJECT or undecided: keep base text
  }
  return out;                                                              // saved as new INTERNAL version with decision-set hash
}
```

---

## 6. Screens and UX

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P07-01 | web/mobile | Intake form | Request type picker, dynamic fields, attachments, deadline | Unknown type → "Other" with free text | Single column | Labelled fields; error summary at top |
| SCR-P07-02 | Teams | Teams app card | Adaptive Card form, status card, approval card | Admin consent missing → link to setup guide | Teams mobile | Card text readable by screen readers |
| SCR-P07-03 | web | Intake queue | SLA badges, assign, bulk, duplicate flag | Empty → "No requests" + share intake link | List | Table semantics |
| SCR-P07-04 | web/mobile | Agreement overview | Status stepper (Draft → Negotiate → Approve → Sign → Executed), parties, key facts, next action | — | Stepper collapses to current step | Stepper announced as list |
| SCR-P07-05 | web/mobile | Deal room | Versions timeline, shared/internal tabs with banners, documents, issues, agreed-version panel | Guest without rights → explanation | Tabs; sticky composer with channel banner | Channel state in text, not colour only |
| SCR-P07-06 | web | Compare view | Side-by-side / inline, change list with filters, accept/reject/counter, untracked banner | Engine error → retry; never partial results | Inline only; change-by-change cards | Changes navigable by keyboard (n/p); insertions/deletions announced as "inserted"/"deleted" |
| SCR-P07-07 | web | Share dialog + leakage check | Party selector, clean/tracked option, pre-share checklist | Leak found → block with fix list (LD-CLM-021) | Sheet | — |
| SCR-P07-08 | web/mobile | Clause editor | Paragraph editing as tracked changes, comment anchors | Unsupported structure → "Use Word" | Simplified | Edits announced |
| SCR-P07-09 | web | Playbook review results | Clause cards with classification, risk note, suggestion (internal), adopt/dismiss | No playbook → offer P06 setup | Cards | AI label on every suggestion |
| SCR-P07-10 | web/mobile/Teams/email | Approval card | Summary, value, deviations, changes since last approval, approve/reject | Invalidated → "version changed, re-review" | Push → 2 taps | — |
| SCR-P07-11 | web | DoA matrix editor | Decision-table grid, test inputs, maker-checker submit | Conflicting rows → lint | Desktop only | Grid with headers |
| SCR-P07-12 | web/mobile | Agreed version and lock | Confirmation per party, gate checklist, send for signing | Gate failure list (LD-CLM-041) | Checklist | — |
| SCR-P07-13 | web/mobile | Obligations and key dates | Proposed vs verified list with clause anchors, owners, reminders | — | List | — |
| SCR-P07-14 | web | Repository | Saved views, filters, columns, search | Empty → import CTA | Search + filters sheet | Table semantics |
| SCR-P07-15 | web | Legacy import verification queue | File preview, proposed metadata, keyboard confirm | — | — | Shortcut legend |
| SCR-P07-16 | web | CLO dashboard | Tiles, drill-downs, data tables | Small data → "not enough data" | Summary tiles | Every chart has a table |
| SCR-P07-17 | web | Renewal decision | Options, deadline countdown, linked negotiation | — | Card | — |
| SCR-P07-18 | web | Bulk contracting | Upload, mapping, preview, errors | Row errors downloadable | — | — |
| SCR-P07-19 | public (guest) | Guest landing | OTP, NDA click-through, room view | Expired link → request new | Mobile-first | WCAG 2.2 AA |

Click budgets: invitation email → guest sees the shared version ≤ 3 taps (link, OTP, view); maker: received version → first change decided ≤ 2 clicks; approver: push → decision ≤ 2 taps; CLO: home → renewals due in 30 days ≤ 2 clicks.

"i" help keys: `hlp.clm.deal_room`, `hlp.clm.internal_channel`, `hlp.clm.shared_channel`, `hlp.clm.round`, `hlp.clm.tracked_change`, `hlp.clm.untracked_change`, `hlp.clm.agreed_version`, `hlp.clm.version_lock`, `hlp.clm.doa`, `hlp.clm.deviation`, `hlp.clm.playbook`, `hlp.clm.obligation`, `hlp.clm.renewal_notice_deadline`, `hlp.clm.auto_renewal`, `hlp.clm.novation`, `hlp.clm.related_party`, `hlp.msg.read_receipt`.

---

## 7. Backend design

### 7.1 Modules

`clm` (intake, agreements, rooms, rounds, changes, approvals, obligations, renewals, dashboards) · `msg` (channels, threads, messages, anchors, receipts) · `dms` (versions, Object Lock, sharing artefacts) · `wf` (approval engine, tasks, SLAs, open/interim/waiting items) · `rul` (DoA decision tables, date rules) · `ai` (playbook review, extraction) · `ntf` (notifications with NN-34 caps) · `int` (Teams app backend, email-in, Graph/Drive adapters, P19 API) · `packages/redline` (compare/apply engine).

### 7.2 Tables (schema `clm`, `msg`; all tenant rows carry `tenant_id`, `legal_entity_id`; RLS deny-by-default)

| Table | Key columns | Indexes | RLS / scope | Retention |
|---|---|---|---|---|
| `clm.intake_request` | `id`, `type`, `requester_user_id`, `department_id`, `answers_enc`, `status`, `sla_due`, `agr_id` | (`tenant_id`,`status`,`sla_due`) | Tenant; requester sees own | 10 years or tenant policy |
| `clm.agreements` | `agr_id`, `ref`, `type_code`, `paper`, `status`, `owner_user_id`, `department_id`, `value numeric(20,4)` (P00 FR-P00-42), `currency`, `term`, `governing_law`, `confidentiality`, `parent_agr_id`, `matter_ids` | (`tenant_id`,`status`), (`tenant_id`,`counterparty_id`), (`tenant_id`,`expiry_date`) | Tenant + ABAC | Term + limitation + buffer, ≥ 8 years after end (R3 LG-092) |
| `clm.agreement_party` | `agr_id`, `party_ref`, `role`, `side`, `signatory_refs` | (`agr_id`) | as agreement | as agreement |
| `clm.deal_room` | `room_id`, `agr_id`, `controls jsonb`, `connected_tenant_ids`, `status` | (`agr_id`) | Owner tenant; connected tenants via mirror | as agreement |
| `clm.room_participant` | `room_id`, `principal` (user / guest), `party_side`, `rights`, `invited_at`, `revoked_at` | (`room_id`) | Owner tenant | as agreement |
| `clm.version_meta` | `ver_id`, `agr_id`, `number`, `side`, `producer`, `visibility jsonb`, `docx_sha256`, `text_sha256`, `round_no`, `locked` | (`agr_id`,`number`) | Visibility-filtered views for guests | as agreement |
| `clm.round` | `neg_id`, `agr_id`, `number`, `opened_by_side`, `shared_ver_id`, `returned_ver_id`, `status` | (`agr_id`,`number`) | as agreement | as agreement |
| `clm.change` | `rlc_id` (prefix `rlc_` redline change; `chg_` is reserved for engineering change records — Appendix B §B.1), `comparison_id`, `type`, `source`, `anchors jsonb`, `old_text_hash`, `new_text_hash`, `round_no` | (`comparison_id`) | as version visibility | as agreement |
| `clm.comparison` | `id`, `base_ver_id`, `target_ver_id`, `engine_version`, `stats jsonb`, `artifact_doc_ver_id` | (`base_ver_id`,`target_ver_id`,`engine_version`) unique | as versions | as agreement |
| `clm.change_decision` | `rlc_id`, `decision`, `actor`, `reason`, `decided_at`, `seq` | (`rlc_id`,`seq`) | Internal only | as agreement |
| `clm.issue` | `id`, `agr_id`, `clause_anchor`, `visibility`, `status`, `owner` | (`agr_id`,`status`) | Visibility | as agreement |
| `clm.deviation` | `agr_id`, `clause_key`, `position`, `approver_rule`, `approved_by` | (`agr_id`) | Internal only | as agreement |
| `clm.approval_step` (projection of `wf.approvals`, `apr_`; R-A-06) | `id`, `apr_id`, `agr_id`, `ver_hash`, `step_no`, `role/user`, `status`, `decided_by`, `comment`, `sla_due` | (`agr_id`,`ver_hash`) | Internal only | as agreement |
| `clm.obligation` | `obl_id`, `agr_id`, `party_side`, `type`, `schedule jsonb`, `amount`, `owner`, `status`, `anchor`, `verified_by` | (`tenant_id`,`status`,`next_due`) | Tenant | as agreement |
| `clm.key_date` | `agr_id`, `kind`, `date`, `rule`, `verified_by` | (`tenant_id`,`date`) | Tenant | as agreement |
| `msg.channel` | `cnv_id`, `room_id`, `kind` (INTERNAL/SHARED/PARTY_PRIVATE), `party_scope` | (`room_id`) | Channel-scoped | as agreement |
| `msg.message` | `msg_id`, `cnv_id`, `author`, `body_enc`, `anchor`, `attachments`, `edited_at`, `withdrawn` | (`cnv_id`,`created_at`) | Channel-scoped; guests only SHARED/own PARTY_PRIVATE | as agreement |
| `clm.mirror_link` | `room_id`, `owner_tenant_id`, `mirror_tenant_id`, `mirror_agr_id` | unique (`room_id`,`mirror_tenant_id`) | Service-only table; each side sees own row | as agreement |

### 7.3 APIs (`/v1/clm`, `/v1/msg` on api.lawdocs.in, P00 FR-P00-19; Idempotency-Key on POST — NN-46)

| Method | Path | Scope | Notes |
|---|---|---|---|
| POST | `/clm/intake-requests` | tenant user / Teams / email-in service | Creates request; returns triage |
| POST | `/clm/agreements` | legal maker | From template, tenant template or upload |
| POST | `/clm/agreements/{agrId}/rooms` | maker | Open deal room |
| POST | `/clm/rooms/{roomId}/participants` | maker | Invite (NN-34 caps enforced) |
| POST | `/clm/agreements/{agrId}/versions` | maker / guest (upload) | Upload/save version; triggers compare |
| POST | `/clm/versions/{verId}:share` | maker | Runs leakage check; produces shared artefact |
| POST | `/clm/comparisons` | participant | `{baseVerId, targetVerId}` → change list (cached by engine version) |
| POST | `/clm/changes/{chgId}/decisions` | maker | ACCEPT/REJECT/COUNTER/ACKNOWLEDGE |
| POST | `/clm/agreements/{agrId}/playbook-review` | maker (credits) | Internal suggestions only |
| POST | `/clm/agreements/{agrId}/approvals` | maker | Starts DoA evaluation for current hash |
| POST | `/clm/approval-steps/{id}:decide` | approver (step-up above threshold) | Bound to hash |
| POST | `/clm/versions/{verId}:propose-agreed` / `:confirm-agreed` | maker / each party | OTP for guests |
| POST | `/clm/agreements/{agrId}:send-for-signing` | maker | Gates; creates P08 request |
| POST | `/clm/agreements/{agrId}:unlock` | maker + owner approval | Voids P08 request |
| GET/PATCH | `/clm/agreements/{agrId}/obligations` | owner | Verify/edit |
| POST | `/clm/agreements/{agrId}:amend` / `:renew` / `:terminate` | maker | Child flows |
| GET | `/clm/repository` | tenant users (permission-trimmed) | Views, filters |
| POST | `/msg/channels/{cnvId}/messages` | channel member | Channel banner state echoed in response |
| POST | `/clm/bulk-jobs` | maker | XLSX/CSV bulk generate |

### 7.4 Domain events (internal; payloads IDs/codes only)

`in.lawdocs.clm.IntakeRequestSubmitted.v1` · `IntakeConverted.v1` · `AgreementCreated.v1` · `DealRoomOpened.v1` · `ParticipantInvited.v1` · `ParticipantRevoked.v1` · `VersionShared.v1` · `CounterpartyVersionReceived.v1` · `SilentEditDetected.v1` · `ChangeDecided.v1` · `RoundClosed.v1` · `PlaybookReviewCompleted.v1` · `ApprovalRequested.v1` · `ApprovalDecided.v1` · `ApprovalsInvalidated.v1` · `AgreedVersionConfirmed.v1` · `VersionLocked.v1` · `VersionUnlocked.v1` · `HandedOffToSigning.v1` · `AgreementExecuted.v1` · `ObligationVerified.v1` · `ObligationOverdue.v1` · `KeyDateApproaching.v1` · `RenewalDecisionRecorded.v1` · `AmendmentInitiated.v1` · `AgreementTerminated.v1` · `AgreementExpired.v1` · `AgreementCancelled.v1` (all prefixed `in.lawdocs.clm.`); `in.lawdocs.msg.MessagePosted.v1`, `in.lawdocs.msg.MessageWithdrawn.v1`. Consumed: `in.lawdocs.sgn.SigningCompleted.v1`, `in.lawdocs.sgn.SigningRequestVoided.v1` (P08; Appendix B §B.4.2).

**Cross-product.** No new `in.infrabyx.*` event is improvised. Both change requests are drafted in Appendix Y (v1.2 proposed; Appendix B §B.4.4–§B.4.5): (1) LD as producer of `in.infrabyx.adr.ADRReferralCreated.v1` for non-loan disputes (Y §Y.7.4; emitted by `int` from P11 `lit.AdrReferralSubmitted` when a contract dispute becomes a matter); (2) `in.infrabyx.legal.AgreementExecuted.v1` mapped by `int` from `clm.AgreementExecuted` (Y §Y.7.1), carrying IDs, hashes and dates only. Until Appendix Y is accepted (`int.ecosystem.proposed_subjects.enabled` OFF), "Refer to ADR" lists ODR providers through `ODR_PORT` (P19; Equator is one option, never the default) and hands off only with the user's explicit consent and no data transfer.

### 7.5 Jobs and workflows (Temporal)

| Workflow | Behaviour |
|---|---|
| `NegotiationRoundWorkflow` | Opens on share; nudges per settings; closes on return/confirm/withdraw; computes round summary |
| `ComparisonJob` (BullMQ) | Runs engine; caches by (base, target, engine version); large documents (> 200 pages) chunked |
| `ApprovalWorkflow` | Evaluates DoA; creates steps; SLAs; escalations; invalidation on version change |
| `LockAndHandoffWorkflow` | Collects confirmations; applies Object Lock; runs gates; creates P08 request; waits for P08 outcome |
| `ObligationExtractionWorkflow` | On execution/import: extraction → proposals → verification tasks → reminders |
| `KeyDateScheduler` (daily) | Fires reminders T-90/60/30/7; marks overdue |
| `MirrorReplicationWorkflow` | Copies shared artefacts/messages to connected tenants; idempotent by artefact hash |
| `CoEditCheckoutWorkflow` | Graph/Drive checkout, timeout reminders, check-in, compare, temp-copy deletion |
| `BulkContractingWorkflow` | Row validation, generation, approvals, hand-off |

---

## 8. Integrations

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| Microsoft Graph (`int.m365`) | Edit in Word, Teams app/bot, Adaptive Card approvals | — | Disable co-edit button; Teams cards fall back to email links | Download/upload DOCX |
| Google Drive API (`int.gws`) | Edit in Google Docs (Office mode) | — | As above | Download/upload |
| Email-in (SES inbound or equivalent) | Intake, replies to threads ("reply to this email to post in the shared channel" — off by default) | — | Bounce with help link | Web form |
| P08 `sgn` | Signing hand-off, outcomes | — | Agreement stays `LOCKED_FOR_SIGNATURE`; retry | Wet-ink execution recording in P08 |
| P06 `tpl`/`drf` | Templates, playbooks, amendment templates | — | — | Upload own DOCX |
| P09 `ai` | Playbook review, extraction, summaries | — | Features hidden; manual review | Human review |
| P05 `dix` (Wave 2) | OCR of scanned paper | — | Mark "scan — text not available" | Manual metadata |
| P10 notice dispatch | Termination/renewal notices with proof of delivery | — | Record external dispatch with evidence | — |
| P19 `int` API/webhooks | Customer systems (ERP/CRM) create intake requests, receive status webhooks `in.lawdocs.clm.*` | — | Retries with backoff; dead-letter | — |
| CRM connectors (P19, Salesforce/Zoho — Ironclad pattern) | Create intake from an opportunity | — | — | Web form |

---

## 9. Settings and configuration (register in Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `clm.intake.channels` | TENANT | list | [WEB, MOBILE, EMAIL] (+TEAMS when consented) | `ORG_ADMIN` | N |
| `clm.intake.email_alias` | TENANT | string | `contracts+<slug>@in.lawdocs.in` | `ORG_ADMIN` | N |
| `clm.intake.allowed_sender_domains` | TENANT | list | tenant verified domains | `ORG_ADMIN` | Y |
| `clm.intake.self_serve_types` | TENANT | list | [] | `ORG_CLO` | Y |
| `clm.intake.sla_hours.<type>` | TENANT | int | NDA 8; others 24 (working) | `ORG_CLO` | N |
| `clm.doa.matrix` | ENTITY | decision table | SME 2-step template | `ORG_CLO` | **Y** (NN-18) |
| `clm.approval.reapprove_on_change` | TENANT | enum | ALL | `ORG_CLO` | Y |
| `clm.approval.sla_hours` | TENANT | int | 24 | `ORG_CLO` | N |
| `clm.approval.stepup_value_inr` | TENANT | decimal | 10,00,000 | `ORG_CLO` | Y |
| `clm.dealroom.guest_otp_required` | PLATFORM | bool (locked) | true | — | — |
| `clm.dealroom.guest_link_ttl_days` | TENANT | int | 14 (1–30) | `ORG_ADMIN` | N |
| `clm.dealroom.guest_can_add_members` | TENANT | bool | false | `ORG_ADMIN` | N |
| `clm.dealroom.invite_reminders_max` | PLATFORM | int | 2 (max 3) | `PLT_SUPER_ADMIN` | Y |
| `clm.dealroom.download_default` | TENANT | bool | true | `ORG_ADMIN` | N |
| `clm.dealroom.watermark_default` | TENANT | bool | true | `ORG_ADMIN` | N |
| `clm.dealroom.nda_clickthrough_default` | TENANT | bool | false | `ORG_ADMIN` | N |
| `clm.negotiation.silent_edit_detection` | PLATFORM | bool (locked) | true | — | — |
| `clm.negotiation.reject_reason_required` | TENANT | bool | false | `ORG_CLO` | N |
| `clm.negotiation.round_nudge_days` | TENANT | int | 5 | `ORG_CLO` | N |
| `clm.redline.normalise_quotes_dashes` | TENANT | bool | true | `ORG_CLO` | N |
| `clm.redline.ai_suggestions_enabled` | PLAN → TENANT | bool | true (Pro+) | `ORG_CLO` | N |
| `clm.redline.ai_author_label` | PLATFORM | string (locked) | "Vidhi AI (suggestion)" | — | — |
| `clm.lock.require_all_party_confirmation` | PLATFORM | bool (locked) | true | — | — |
| `clm.obligations.extraction_enabled` | TENANT | bool | true | `ORG_CLO` | N |
| `clm.obligations.verify_required` | PLATFORM | bool (locked for key dates) | true | — | — |
| `clm.renewal.reminder_offsets_days` | TENANT / USER | list | [90, 60, 30, 7] | `ORG_CLO` / user | N |
| `clm.coedit.provider` | TENANT | enum | NONE (M365 / GOOGLE) | `ORG_ADMIN` | Y |
| `clm.coedit.delete_temp_copy` | TENANT | bool | true | `ORG_ADMIN` | N |
| `clm.coedit.wopi_enabled` | PLATFORM | bool | false (ADR) | `PLT_SUPER_ADMIN` | Y |
| `clm.notify.whatsapp_enabled` | TENANT | bool | false (status-only if ON) | `ORG_ADMIN` | Y |
| `clm.bulk.max_rows` | PLAN | int | 2,000 | P17 | N |
| `clm.repository.fiscal_year_start` | ENTITY | month | April | `ORG_ADMIN` | N |
| `msg.read_receipts` | TENANT / USER | bool | true | `ORG_ADMIN` / user | N |
| `msg.edit_window_minutes` | PLATFORM | int | 5 | `PLT_SUPER_ADMIN` | N |
| `msg.paste_guard_similarity` | PLATFORM | decimal | 0.8 | `PLT_SECURITY_OFFICER` | N |

---

## 10. Security, privacy and audit

| Threat / duty | Control |
|---|---|
| Internal content leaking to counterparty (NN-37) | Separate channel tables and visibility-filtered views; share-time sanitiser and leakage check; property test on every share in CI; paste guard; banner |
| Guest account takeover / forwarding of links | Single-use magic link + OTP to invited address; device binding; watermark; revocation ≤ 60 s; access log visible to owner |
| Counterparty tampering (silent edits) | Compare against exact last-shared version; untracked changes must be acknowledged; hashes on every version |
| Approval forgery or stale approvals | Approvals bound to version hash; step-up above threshold; invalidation on change; audit |
| Cross-tenant data (company-to-company) | Replication of shared artefacts only; no cross-tenant queries; mirror table service-only; tests (NN-01) |
| Email-in spoofing | SPF/DKIM/DMARC; sender allow-list; quarantine |
| Malicious DOCX (macros, external relationships, OLE) | Strip macros/external targets on ingest; render previews server-side; Gotenberg sandbox |
| Teams/Graph token misuse | Delegated scopes minimal; tokens per user, encrypted; no app-only access to customer files |
| Data retention | Agreement data retained ≥ term + limitation + buffer (R3 LG-092); legal hold honoured (P04) |
| DPDP | Counterparty personal data processed for contract performance; notice shown on guest landing; access/erasure requests routed per P01; retention schedule shown |

Audit (ledger, same transaction — NN-45): intake create/triage; agreement create/status; participant invite/revoke; every share (with leakage-check result hash); every received version; every change decision; approvals; lock/unlock; send for signing; obligation verify/waive; settings and DoA changes (with maker-checker IDs).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Agent | Autonomy | Human confirmation | Evaluation |
|---|---|---|---|---|
| Playbook review and suggested redlines | `AGT_REDLINE_NEGOTIATOR` (Appendix H; X-27) | L1 (internal suggestions) | Adopt per suggestion; share is a separate human action | Clause-mapping accuracy ≥ 90% on labelled set; 0 suggestions in shared artefacts without adoption (test) |
| Third-party paper "what's missing" and risk summary | Same | L1 | — | Recall of missing standard clauses ≥ 90% on test set |
| Obligation and key-date extraction | `AGT_OBLIGATION_TRACKER` | L2 (creates PROPOSED items) | Verification per item; key dates locked to human verification | Precision/recall ≥ 90% on test set; date arithmetic deterministic |
| Negotiation summaries ("what changed this round") | Same | L1 | — | Faithfulness check vs change list |
| Approval chasing (internal reminders) | Ops agent | L3 for internal reminders only (within NN-34 not relevant internally) | — | — |
| Never | — | — | Agents never share externally, accept a change, confirm agreed version, approve, lock, unlock, send for signing or message counterparties (NN-13, NN-43) | NN tests |

Data: Bedrock India for contract content (NN-15); counterparty-supplied text treated as untrusted data (prompt-injection defence).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p07/*.feature`)

```gherkin
Feature: Intake

  @P07-AT-01
  Scenario: Business user requests an NDA from Teams
    Given tenant "Acme" has consented to the LawDocs Teams app
    When ORG_MEMBER "Neha" submits "Request a contract" with type "Mutual NDA" and counterparty "Beta Pvt Ltd"
    Then an intake request is created with SLA 8 working hours
    And the rules engine selects template "D1.2.3" and the Acme NDA playbook

  @P07-AT-02
  Scenario: Email from an unknown sender is held
    When an email from "someone@unknown.example" reaches the intake alias
    Then no intake request is created automatically
    And the email is placed in the maker review hold with attachments scanned

Feature: Deal room and confidentiality

  @P07-AT-03 @NN-37
  Scenario: Internal comments never reach the counterparty
    Given version v3 has 4 internal comments and 2 shared comments
    When the maker shares v3 with "Beta Pvt Ltd"
    Then the shared DOCX contains exactly 2 comments
    And the shared DOCX properties contain no internal author names
    And the guest view of v3 shows no internal thread

  @P07-AT-04 @NN-37
  Scenario: Guest sees only shared versions
    Given versions v1 (shared), v2 (internal), v3 (shared)
    When CP_GUEST "Ravi" opens the versions timeline
    Then he sees v1 and v3 only
    And comparing v1 with v2 returns 404

  @P07-AT-05 @NN-34
  Scenario: Invitation limits
    Given a counterparty was invited and reminded twice
    When the maker tries to send a third reminder
    Then the system refuses with "LD-CLM-013"

  @P07-AT-06
  Scenario: Paste guard
    When the maker pastes text copied from the internal channel into the shared composer
    Then a confirmation "This text came from the internal channel" is shown before sending

Feature: Redlines

  @P07-AT-07
  Scenario: Silent edits are detected
    Given v3 was shared with Beta
    When Beta uploads v4 in which clause 9.2 was changed without track changes
    Then clause 9.2 is flagged UNTRACKED in red
    And event "in.lawdocs.clm.SilentEditDetected.v1" is published
    And v4 cannot be locked until the change is acknowledged

  @P07-AT-08
  Scenario: Accept all yields the counterparty text
    Given a comparison between v3 and v4 with 27 tracked changes
    When the maker accepts all changes
    Then the resulting version's normalised text equals v4's proposed text

  @P07-AT-09 @NN-37
  Scenario: Each decision is logged
    When the maker rejects change "rlc_01" with reason "Liability cap below fallback"
    Then a change decision with actor, time and reason is stored
    And the decision is visible in the internal negotiation history only

  @P07-AT-10
  Scenario: Deterministic, versioned comparison
    Given engine version "redline-1.4.0"
    When v3 and v4 are compared twice
    Then both change lists are identical
    And the comparison records engine version "redline-1.4.0"

Feature: AI playbook suggestions

  @P07-AT-11 @NN-13 @NN-43
  Scenario: Suggestions stay internal until adopted
    Given Vidhi suggested 5 redlines on v4
    When the maker shares v5 having adopted 2 suggestions
    Then the shared DOCX contains the 2 adopted changes authored by "Acme"
    And contains no change authored "Vidhi AI (suggestion)"
    And the internal audit records the suggestion provenance

Feature: Approvals

  @P07-AT-12 @NN-18
  Scenario: DoA routes by value and deviation
    Given the DoA requires CFO approval above ₹25,00,000 and CLO approval for any liability-cap deviation
    When an agreement of ₹40,00,000 with a liability-cap FALLBACK_2 is submitted
    Then approval steps for CLO and CFO are created

  @P07-AT-13
  Scenario: Change invalidates approval
    Given CFO approved version hash H1
    When the maker saves a new version with hash H2
    Then the CFO approval is marked INVALIDATED
    And the agreement returns to IN_NEGOTIATION and approval must be requested again for hash H2

  @P07-AT-14 @NN-17 @NN-18
  Scenario: Delegated maker cannot approve
    Given OPS_RM "Karan" acts as ORG_DELEGATED_MAKER for "Acme"
    When Karan attempts to approve a step on an agreement he made
    Then the action is rejected with "LD-CLM-031"

Feature: Lock and hand-off

  @P07-AT-15 @NN-07
  Scenario: Excluded instrument cannot go to eSign
    Given the locked document is a general power of attorney not in favour of a regulated entity
    When the maker taps "Send for signing"
    Then P08 eSign is not offered and the wet-ink pack is produced

  @P07-AT-16 @NN-08 @NN-40
  Scenario: Gates checked before signing
    Given a Maharashtra leave and licence agreement locked for signature
    When the maker sends for signing
    Then the gate list includes "Stamp duty to be paid before signing" and "Registration required"
    And the agreement cannot become EXECUTED until registration is recorded or waived with reason

  @P07-AT-17
  Scenario: All parties confirm the agreed version
    Given Acme approvals are complete for hash H5
    When Beta's guest confirms H5 with OTP
    Then the version is locked with Object Lock and status LOCKED_FOR_SIGNATURE

  @P07-AT-18
  Scenario: Unlock voids pending signing
    Given a P08 signing request exists for hash H5
    When the maker unlocks with reason "Typo in annexure" and the owner approves
    Then the P08 request is voided and all parties are notified

Feature: Obligations

  @P07-AT-19
  Scenario: Key dates need human verification
    Given Vidhi proposed expiry 31-03-2028 and auto-renewal with 60 days' notice
    Then no reminder exists until the owner verifies
    When the owner verifies
    Then the renewal notice deadline is computed as 31-01-2028 and reminders are scheduled at T-90, T-60, T-30, T-7

Feature: Company to company

  @P07-AT-20 @NN-01
  Scenario: Connected rooms replicate only shared artefacts
    Given Acme and Beta are both LawDocs tenants in one connected room
    When Acme shares v3
    Then Beta's tenant holds a copy of v3 with the same SHA-256
    And no Acme internal version, comment or approval is readable by any Beta user

Feature: Co-editing

  @P07-AT-21
  Scenario: Word check-in catches untracked co-authoring edits
    Given the maker checked out v6 to Word via Microsoft Graph
    When a colleague edits clause 4 without track changes and the maker checks in
    Then v7 is created and clause 4 is flagged UNTRACKED

Feature: Portability and audit

  @P07-AT-22 @NN-11
  Scenario: Agreement export folder
    When the tenant exports
    Then agreement LD-AGR-2026-000123 appears under "02 Agreements and Contracts/FY 2026-27/Procurement/Beta Pvt Ltd - Supply Agreement (LD-AGR-2026-000123)/"
    And sub-folders "01 Drafts", "02 Negotiation and Redlines", "03 Signed and Stamped", "05 Amendments and Renewals", "06 Correspondence" are populated

  @P07-AT-23 @NN-02 @NN-45
  Scenario: Messages are corrected, not deleted
    When a user withdraws a shared message
    Then a "message withdrawn" placeholder is shown
    And the ledger keeps the original with a correction entry
```

---

## 13. Exit gate, deliverables and open items

**Exit checklist**
- [ ] `packages/redline` compare/apply engine at v1.x with ≥ 300-pair golden corpus (incl. Indic scripts), property tests (accept-all, reject-all, determinism) green.
- [ ] Deal rooms with guest access, internal/shared channels, leakage check and paste guard; NN-37 test suite green.
- [ ] DoA decision tables with maker-checker; approvals bound to hash; invalidation working.
- [ ] Lock and P08 hand-off with all gates; unlock path; wet-ink route for excluded instruments.
- [ ] Obligations/key dates with verification and reminders; renewal, amendment, termination flows.
- [ ] Intake via web, mobile, email-in and Teams app (pilot tenant consented); repository views; legacy import queue.
- [ ] CLO dashboard with data tables; company-to-company connected rooms; Word co-edit (M365) live; Google co-edit behind [VERIFY] warning.
- [ ] Settings (§9) registered in Appendix R; help keys registered; errors LD-CLM-001…060 and LD-MSG-001…020 registered.
- [ ] Export-map entries registered: `clm.agreements` + versions → `02 Agreements and Contracts/{<Entity>/}<FY>/{<Department>/}<Counterparty> - <Agreement title> (LD-AGR-…)/01 Drafts` (Appendix K §K.3.1) (internal drafts), `/02 Negotiation and Redlines` (shared versions, comparisons as redline DOCX/PDF, decision log CSV, issues list), `/05 Amendments and Renewals` (child agreements, renewal decisions), `/06 Correspondence` (shared thread as PDF + JSON; internal thread in a sub-folder "Internal (not shared)"); obligations and key dates → `Obligations.xlsx` at the agreement folder root (Appendix K §K.3.1) and `99 System Data (CSV and JSON)/Datasets/`; Individual equivalents under `08 Agreements/<Year>/<Category>/<Counterparty> - <Title> (LD-AGR-…)/` or the life-area folder (Appendix K §K.3.2). `<FY>` is the Indian FY label (`FY 2026-27`) for companies.
- [ ] Accessibility audit of SCR-P07-05/06/10/12/19 (NN-28).

**Demo script:** NDA request from Teams → auto-template → share with guest → guest edits without track changes → silent edit flagged → accept/reject per change → Vidhi playbook suggestions adopted → DoA approvals on mobile → both sides confirm → lock → P08 signing → obligations verified → renewal reminder in the CLO dashboard.

**Error codes (initial set)**

| Code | Message |
|---|---|
| LD-CLM-001 | This request type is not configured. Choose another or "Other". |
| LD-CLM-011 | You cannot invite participants to this room. |
| LD-CLM-013 | Invitation limit reached for this person. |
| LD-CLM-014 | This guest link has expired. Ask for a new invitation. |
| LD-CLM-021 | Sharing blocked: internal content found. Fix the listed items. |
| LD-CLM-022 | You can only compare versions you are allowed to see. |
| LD-CLM-024 | Acknowledge changes made without track changes first. |
| LD-CLM-031 | You cannot approve an agreement you prepared or under a delivery grant. |
| LD-CLM-032 | This approval is for an older version. Review the latest version. |
| LD-CLM-041 | This agreement cannot go for signing yet. See the failed checks. |
| LD-CLM-042 | A signed version cannot be unlocked. Create an amendment. |
| LD-CLM-051 | Verify key dates before reminders can be set. |
| LD-MSG-001 | You are not a member of this channel. |
| LD-MSG-004 | This message can no longer be edited. |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P07-01 | Microsoft Graph delegated permission set for app-folder co-editing and Teams app publishing (store vs org-only) [VERIFY] | Integrations lead |
| OI-P07-02 | Google Docs tracked-change ↔ suggestion round-trip fidelity [VERIFY] | Integrations lead |
| OI-P07-03 | Appendix Y change requests (drafted in Y §Y.7.1, §Y.7.4): LD as producer of `ADRReferralCreated` for non-loan disputes; `legal.AgreementExecuted` — awaiting Ecosystem Spec v1.2 acceptance | Pack lead / Ecosystem Spec owner |
| OI-P07-04 | Default DoA templates for SMEs and NBFC clients (align with LDC delegation registers where tenant uses LDC — NN-47) | `[OWNER]` |
| OI-P07-05 | WOPI editor licence ADR (ONLYOFFICE/Collabora) | Architecture |
| OI-P07-06 | Retention period for negotiation data beyond executed agreements (abandoned deals) | `PLT_DPO` / `[COUNSEL]` |
| OI-P07-07 | In-browser clause editor component choice and licence [REC ProseMirror/Tiptap-class] | Frontend lead |

