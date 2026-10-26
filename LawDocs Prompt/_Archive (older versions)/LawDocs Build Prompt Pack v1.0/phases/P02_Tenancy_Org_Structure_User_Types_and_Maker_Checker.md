# Phase P02 — Tenancy, Organisation Structure, User Types and Maker-Checker

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenants, legal entities, ledger, settings heads, flags), P01 (persons, users, memberships, invitations, verification levels, signatory authorities). External: Cerbos; Operations Hub OH10 (staff SCIM and `group_grant` memberships), OH4 (onboarding milestones); `@infrabyx/governance-kernel` for director/KMP designations when mounted (P13) or LawDocsComply when it is system of record (D-10).
> **Sequencing:** Starts in P01 sprint 2 (persons/users/memberships frozen). Sprints 1–2: org model, workspace types, context switcher, role grants, Cerbos policy framework. Sprints 3–4: maker-checker engine, DoA tables, SoD engine, delegation and out-of-office. Sprints 5–6: custom roles, group and cross-functional grants, delivery-grant interface, access reviews, role-based homes and navigation. P03 (Configuration Studio) consumes the maker-checker and DoA schemas from sprint 4; P18 builds the Delivery Console UI on the grant model frozen at the end of sprint 5.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, permission matrix, maker-checker action catalogue, SoD pairs, Cerbos conventions, grant types), P (access-control and privileged-access controls), R (settings), K (export folders for organisation and access records), W (open items), X (Operations Hub additions: group-grant feed and access-review event).
> **Requirements covered:** R-026, R-027, R-028, R-030, R-047 (configurable approvals; item types in P03), R-048 (separation of operations from super admin), R-051 (maker-checker, anti-fraud), R-058, R-059 (organisation structure foundations), R-060 (one-CLO operating model), R-064, R-065 (client section access model), R-066, R-067.
> **Decisions applied:** D-02, D-03, D-06, D-10, D-17 · **Challenges applied:** CH-14, CH-16, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-17, NN-18, NN-19, NN-23, NN-28, NN-29, NN-33, NN-43, NN-45, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 3 backend engineers, 2 frontend engineers, 1 security/authorisation engineer, 1 QA engineer).

---

## 1. Objective and business outcome

The owner wants many user types — super admin, an operations team serving clients, company admins, makers and checkers, departmental users, individuals — each with its own features, fewer clicks and an anti-fraud design where "employees cannot cheat". P02 gives LawDocs one authorisation model that serves every workspace type, without special-case code:

- **Structure:** tenant → legal entities → branches → departments → teams → positions, renameable and effective-dated, for a one-person startup and for a listed group with forty subsidiaries.
- **Workspaces:** Personal, Company, Professional firm and the Consumer Help brand, with a context switcher that always shows *where* and *as whom* the user is acting.
- **Roles:** the binding role codes (master §1.4; Appendix D), scoped grants, a custom-role builder and positions, so that a company can model "Head – Legal (Delhi)" without asking LawDocs.
- **Approvals:** a configurable maker-checker engine per action type and a delegation-of-authority (DoA) matrix by value, document type and department, with segregation of duties enforced at person level.
- **Controlled outsiders:** LawDocs relationship managers as delegated makers, engaged professionals, external counsel, auditors, counterparties, family members, delegates and nominees — each through a scoped, time-bound grant the customer controls; Infrabyx cross-functional staff through purpose-bound group grants that are never inherited (Ecosystem Spec §4.6).
- **Integrity without surveillance:** maker ≠ checker, approvals bound to the exact version approved, quarterly access reviews and immutable logs — not keystroke or screen monitoring (NN-33; CH-24, CH-32).

| Outcome | Exit-gate measure |
|---|---|
| One model, every workspace | All persona journeys in §4L pass with the same policy engine; no `if (tenant.kind === …)` authorisation branches in handlers (Semgrep rule) |
| Maker ≠ checker everywhere | `NN-18_*` suite: for every action in the Appendix D catalogue with mode REQUIRED/LOCKED, the maker (and the maker's delegator, linked staff identity or agent sponsor) cannot approve |
| Approvals bind to content | Changing a payload after approval invalidates the approval (`LD-WF-012`) in 100% of catalogue actions |
| Outsiders are scoped | `NN-17_*`: delivery and engagement grants require client approval, expire, revoke within 60 s; break-glass needs two approvers and a client report ≤ 24 h |
| Group roles never inherited | `NN-17_group_grant_not_inherited`: membership in a parent tenant or another Infrabyx company never yields access to a child tenant without an explicit grant |
| Fewer clicks | Role-based home screens meet the click budgets of §4L in moderated tests |
| Customisation without LawDocs | A company owner creates a custom role, a new department and a DoA rule, and enables maker-checker on external sharing, without any LawDocs staff action (NN-29) |

---

## 2. Scope (in / out)

**In scope:** organisation model (`org`); workspace types and the context switcher; role grants, scopes and positions; custom roles; the Cerbos policy framework, derived roles and query plans; the maker-checker engine (`wf.approvals`) and action catalogue wiring; DoA decision tables (schema, defaults, evaluator call through `RULES_PORT`, simulator); SoD engine; delegation and out-of-office; individual sharing roles (family, delegate) and their scopes; professional-firm roles; group tenants and cross-entity grants; Infrabyx `group_grant` enforcement; grant types for delivery, engagement, onboarding, external counsel, auditor, nominee and break-glass (model, lifecycle, enforcement); access reviews; master-data change of a client by LawDocs staff (CH-26); role-based home dashboards and navigation.

**Out of scope**

| Item | Owner phase |
|---|---|
| Configuration Studio UI, rule-pack authoring, open/interim/waiting item types | P03 (P02 provides the approval and DoA schemas it edits) |
| Delivery Console screens, client sections, RM workbench, access-transparency log UI | P18 (P02 provides the grant model, enforcement and APIs) |
| Board, committees, KMP registers, client HRMS | P13 (governance and HRMS kernels; LDC when SoR) |
| Agent workforce, autonomy ceilings, sponsors | P09 (P02 enforces "agents are makers only") |
| Seat counting and plan limits | P17 (P02 exposes counts by role class) |

---

## 3. Personas and permissions touched

| Role code | What they can do in P02 (full matrix: Appendix D §D.5–D.6) |
|---|---|
| `ORG_OWNER` | Everything in the tenant's org and access settings; approve privileged grants (not their own); define DoA; enable or tighten maker-checker; appoint access reviewers |
| `ORG_ADMIN` | Manage users, departments, teams, positions, custom roles (publishing a custom role needs a second admin/owner); cannot grant `ORG_OWNER` or approve own elevation |
| `ORG_CLO` | Manage legal department structure, legal approval routes, legal DoA rows; approve delivery and external-counsel grants for legal scopes |
| `ORG_LEGAL_MAKER`, `ORG_DELEGATED_MAKER` | Submit items for approval; cannot approve own items |
| `ORG_CHECKER`, `ORG_APPROVER` | Approve per DoA; authorised signatory limits from P01 |
| `ORG_DEPT_HEAD` | Manage own department's teams and members (if delegated); approve departmental rows; review access for own department |
| `ORG_MEMBER` | Raise requests; see own items |
| `ORG_DIRECTOR`, `ORG_KMP`, `ORG_BOARD_OBSERVER` | Board/KMP homes; approvals routed to them by DoA |
| `ORG_EXT_COUNSEL`, `ORG_AUDITOR_RO` | Act within engagement or audit grants only |
| `IND_OWNER` | Invite family members and delegates with scopes; manage nominees (P01); approve delegate actions where set |
| `IND_FAMILY_MEMBER`, `IND_DELEGATE`, `IND_GUARDIAN`, `IND_NOMINEE` | Act within scope |
| `PRO_FIRM_ADMIN`, `PRO_FIRM_MEMBER`, `PRO_*` | Firm structure; engagement-grant work in client tenants |
| `CP_GUEST` | Shared items only |
| `OPS_DELIVERY_LEAD`, `OPS_RM`, `OPS_ONBOARDING`, `OPS_PROFESSIONAL` | Propose delivery/onboarding grants; act under approved grants |
| `PLT_SUPER_ADMIN`, `PLT_SECURITY_OFFICER` | Platform role ceilings, locked catalogue actions, break-glass approvals; master-data changes only via Correction Entry with client approval |
| `PLT_AUDITOR_RO` | Read access-review evidence and grant logs |
| `AGT_<NAME>` | Maker-only principals under a sponsor (NN-43) |

---

## 4. Functional requirements

### 4A. Organisation model

**FR-P02-01 — Hierarchy.** `org` owns: `org.branches` (`brn_`; legal entity, name, code, State, address, GSTIN link from P01 FR-P01-32, valid_period), `org.departments` (`dep_`; legal entity, parent department, name, code, `canonical_function` from a platform list — LEGAL, FINANCE, HR, COMPLIANCE, SECRETARIAL, SALES, PROCUREMENT, OPERATIONS, IT, RISK, ADMIN, BOARD, OTHER — so a tenant's "Legal & Secretarial" still receives routing meant for LEGAL, valid_period), `org.teams` (`tem_`; department, name, lead position), `org.positions` (`pos_`; title, department, branch, reports_to position, `kmp_type` (MD, CEO, WTD, CFO, CS, CLO, MANAGER) when applicable, holder person, valid_period). Paths are `ltree` for descendant queries. Every object is renameable without affecting history, because history references IDs (NN-12). Legal entities (`ent_`) remain owned by `core` (P00).

**FR-P02-02 — Templates.** Department templates by constitution and size (seeded, versioned data): *Startup* (Founders, Legal & Compliance, Finance, Operations), *SME* (adds HR, Sales, Procurement), *NBFC / regulated finance company* (Board, Legal, Compliance, Secretarial, Credit, Risk, Collections, Operations, IT/Information Security, Internal Audit, Grievance Redressal, HR, Finance — names editable; the governance and compliance specifics come from P13/LDC, D-10), *Professional firm* (Partners, Associates, Clerks/Paralegals, Accounts), *Listed group* (per entity). Applied in the P01 wizard; editable later.

**FR-P02-03 — Group structures.** Two supported shapes: (a) **one COMPANY tenant with several legal entities** (simple groups sharing staff, settings and a vault, each record carrying `legal_entity_id`); (b) a **GROUP tenant** umbrella with child COMPANY tenants (groups needing separate administration, separate exports or separate operating policies). In both, access to an entity or child tenant requires an explicit grant scoped to it; membership in the parent or umbrella never implies access to a child (FR-P02-44). Group views show aggregates computed from child read models unless the viewer holds grants in each child.

**FR-P02-04 — Effective dating and moves.** Restructures (merge two departments, move a team, close a branch) are change sets with an effective date and a preview of affected people, open items, approval rules and grants; open items move per a selectable rule (stay with the old unit until closed / move to the new unit / route to the department head). Restructures run as one change batch with a 24-hour undo where nothing has been executed externally (P03 FR-P03-21 change batches; Appendix A G-BATCH).

**FR-P02-05 — Directors and KMP.** When the governance kernel is mounted locally (LawDocs-only company, P13) or LawDocsComply is SoR (D-10, NN-47), directors and KMP designations come from that source; P02 links persons to `ORG_DIRECTOR`/`ORG_KMP` roles with `kmp_type` and never maintains a competing register.

**FR-P02-06 — Customisation hooks.** Tenants rename every unit, choose which levels they use (a startup may skip branches and teams), set a department head, define department codes used in business references and export folders (`02 Agreements and Contracts/{<Entity>/}<FY>/{<Department>/}…` — Appendix K §K.3.1), and choose whether department heads may administer their own members (`org.dept_head.can_manage_members`).

### 4B. Workspace types and the context switcher

**FR-P02-07 — Workspace types.**

| Type | Tenant kind | App | Who | What it is for |
|---|---|---|---|---|
| Personal | `PERSONAL` | my.lawdocs.in, mobile | One individual (`IND_OWNER`) plus invited family members, delegates, guardians' wards, nominees | Life-event Legal Vault, drafts, signing, disputes, tax, consumer matters |
| Company | `COMPANY` (optionally under `GROUP`) | my.lawdocs.in, mobile (approvals, signing, vault) | Company users, directors, KMP, outsiders by grant | Legal department OS, CLM, litigation, IP, governance/HRMS mounts |
| Professional firm | `PRO_FIRM` | work.lawdocs.in (practitioner workspace), mobile | Independent professionals and their firm members | Own practice records; client work only inside client tenants via engagement grants |
| Consumer Help | `PERSONAL` under brand `CONSUMER_HELP`; brand operating tenant `CONSUMER_HELP` for case managers | `[Consumer Help Brand domain]`; delivery for case managers | Consumers; `OPS_CONSUMER_CASE_MANAGER` | Loan/insurance grievances, challans, vehicles (P15); ethical wall (NN-23) |

**FR-P02-08 — Context switcher** (SCR-P02-01). Header control listing every active membership and grant the person holds: "Personal — Ananya", "Alpha Pvt Ltd — Legal maker", "Beta Finance Ltd — via LawDocs retainer (delegated maker, until 31 Mar 2027)", "Rao & Associates — Firm admin". Each entry shows workspace type icon, colour band (configurable per tenant, contrast-checked), role summary and, for grants, the expiry. Recent contexts first; search when more than seven; keyboard shortcut (Ctrl/⌘ + K then "switch"). Switching re-issues `ld_ctx` (P01 FR-P01-03), is audited, clears client caches for the previous tenant, and opens the role-based home (FR-P02-55). The current context is shown persistently on every screen and on every outbound action confirmation ("Send as Alpha Pvt Ltd?"). Consumer Help opens on the brand's own origin; the switcher shows it only if the person linked sign-in (P01 FR-P01-69).

**FR-P02-09 — Notifications by context.** Every in-app, push and email notification carries the workspace label; a push tap opens the right context; "quiet hours" are per context.

**FR-P02-10 — Default context.** Last used, or a pinned default; a person with exactly one workspace never sees the switcher (fewer clicks).

### 4C. User types and scoped individual roles

**FR-P02-11 — Role catalogue.** The binding role codes of master §1.4 (Appendix D) are seeded in `iam.roles` with: code, group, workspace types where valid, description, capability set (Appendix D §D.4 capability families), ceilings (what can never be added — e.g., `ORG_DELEGATED_MAKER` can never hold approve capabilities), MFA requirement, minimum identity level (P01), whether granting needs approval (`grant_requires_approval`), seat class for P17 (`FULL`, `LIGHT`, `FREE_GUEST`).

**FR-P02-12 — Family members** (`IND_FAMILY_MEMBER`). Invited by the owner to shared folders (e.g., "Property – Noida flat", "Parents' documents"), with `READ` or `READ_UPLOAD` per folder; never sign, share outside, delete originals or export the whole vault; see only shared folders; can leave at any time.

**FR-P02-13 — Delegates** (`IND_DELEGATE`). A trusted helper (a CA friend, an adult child helping a parent) with a time-bound scope (`valid_to` ≤ 365 days, renewable) over named folders and a chosen set of capabilities from: upload, organise, draft, prepare signing requests (the owner sends), message counterparties as "on behalf of", book marketplace services for the owner (payment by owner). Never: sign, accept, pay, delete, share externally or export everything. Each delegate action shows "by Rohan for Ananya" and the owner receives a weekly digest. Owner may require approval for each delegate-prepared send (`wf.mc` action `dms.share.external` in Personal workspace = OPTIONAL).

**FR-P02-14 — Guardians and nominees.** As P01 (FR-P01-47, FR-P01-49); P02 enforces their scopes through grant types `GUARDIAN` and `NOMINEE`.

**FR-P02-15 — Counterparties** (`CP_GUEST`). Access only through share grants on specific documents/versions/deal rooms (P07); no folder browsing; no search beyond their shared items.

**FR-P02-16 — Professionals and firms.** `PRO_FIRM_ADMIN` manages firm members and their own practice workspace; `PRO_FIRM_MEMBER` acts in the firm workspace per assigned matters; access to a client tenant only through an **engagement grant** created when an engagement is accepted in P16 and approved by the client (same rules as delivery grants, FR-P02-47). A firm member never sees another client's tenant data in the firm workspace except what the professional chose to store there for their own records under their professional obligations [COUNSEL: professional record-keeping vs client data ownership].

**FR-P02-17 — Delegated makers** (R-064). `ORG_DELEGATED_MAKER` is a role inside a client tenant held by a LawDocs RM (`OPS_RM` under a delivery grant) or an engaged professional (under an engagement grant). Both sides can create makers: the client creates one (invites an external professional or approves a LawDocs-proposed RM) and the LawDocs side can propose one (`OPS_DELIVERY_LEAD` proposes; client approves). Multiple makers per scope are allowed. The checker for delegated-maker items is always a client user: LawDocs staff and engaged professionals can never be checker, approver, signatory, director or auditor in a client tenant (SoD-12, Appendix D; P18 `NN-17_delivery_never_checker`). An `OPS_QA_REVIEWER` may review a deliverable on the LawDocs side before the maker submits it; that review is internal quality control, never a checker step in the client's route.

### 4D. Role grants, positions and custom roles

**FR-P02-18 — Role grants.** `iam.role_grants` (`grt_` with `grant_type = ROLE`): membership × role × scope (`TENANT`, `LEGAL_ENTITY`, `BRANCH`, `DEPARTMENT` (with or without descendants), `TEAM`, `MATTER`, `AGREEMENT`, `FOLDER`) × valid_period × granted_by × approval (for roles with `grant_requires_approval`: `ORG_OWNER`, `ORG_ADMIN`, `ORG_CLO`, `ORG_CHECKER`, `ORG_APPROVER`, `ORG_DELEGATED_MAKER`, `ORG_AUDITOR_RO`, `ORG_EXT_COUNSEL`, `PRO_FIRM_ADMIN`). A person may hold several roles; SoD rules block toxic combinations (FR-P02-36).

**FR-P02-19 — Position-based grants.** A role may be granted to a **position** rather than a person (e.g., `ORG_APPROVER` up to ₹50 lakh to position "Head – Legal"). The holder inherits the grant while holding the position; a change of holder transfers it only after the new holder meets the role's identity level and, for approval-required roles, after approval. DoA rules (FR-P02-23) reference positions, so people changes never require rewriting approval rules.

**FR-P02-20 — Custom roles builder** (SCR-P02-08). A company or firm admin composes a role from the capability catalogue (Appendix D §D.4) — e.g., "Contract Manager" = CLM create/update/submit + vault read in own department + negotiation messaging — choosing a base role code (custom roles always map to a base code for policy and seat purposes), capabilities (only those within the base role's ceiling), default scope, MFA and identity level (≥ base), and description. The builder blocks capability sets that would violate SoD within one role (e.g., `submit` and `approve` on the same object type) and shows a plain-language summary ("People with this role can create and edit contracts in their department, submit them for approval, and message counterparties. They cannot approve, sign or export."). Publishing is maker-checker (action `iam.custom_role.publish`); roles are versioned; changing a published role creates a new version that applies to all holders after approval, with a preview of affected people.

**FR-P02-21 — Platform ceilings.** `PLT_SECURITY_OFFICER` maintains platform ceilings (capabilities that no tenant role may include: e.g., approving one's own correction, reading sealed artefacts outside purpose) and the list of locked catalogue actions; ceilings are versioned policy code (FR-P02-22), not data.

**FR-P02-22 — Cerbos policies.** Policies in `policies/cerbos/` (conventions in Appendix D §D.8): resource kinds `ld:<module>:<resource>` (e.g., `ld:clm:agreement`), derived roles (`owner_of_record`, `assigned_maker`, `department_member`, `grant_holder`, `checker_eligible`), principal attributes from memberships, grants, positions, identity level and AAL; resource attributes from the record (tenant, legal entity, department, owner, maker of current version, confidentiality, state, legal hold, engagement). `packages/authz` exposes `@Authorize(action, resolver)` and `planQuery()` that turns Cerbos query plans into SQL fragments so lists never return rows the user cannot open; the same plan filters search and AI retrieval (P09). A Semgrep rule fails any controller method without `@Authorize` or `@Public(reason)`. Policy tests are generated from the Appendix D matrices and run in CI; every decision for privileged actions is logged with policy version.

### 4E. Delegation-of-authority (DoA) matrix

**FR-P02-23 — DoA tables.** A DoA table is a versioned decision table (GoRules ZEN through `RULES_PORT`; P03 provides the Studio editor) owned by the tenant (or entity), with inputs and outputs:

| Inputs | Outputs |
|---|---|
| `action_code` (catalogue), `document_type` (template family), `value_inr` (contract value or exposure; NUMERIC), `term_months`, `counterparty_type` (individual, company, government, related party flag), `department_id`, `legal_entity_id`, `risk_flags[]` (from P07 clause analysis: non-standard indemnity, unlimited liability, exclusivity, data transfer abroad), `jurisdiction`, `is_renewal` | `approvals[]` (sequence of steps; each step = role or position or named person, count, ANY/ALL), `signatory_required` (authorised signatory with authority limit ≥ value — P01 FR-P01-35), `board_or_shareholder_approval_flag` (route to governance — P13; e.g., related-party transactions under Companies Act 2013 s.188 [LAW; thresholds VERIFY in P13]), `legal_review_required`, `escalation_hours`, `explanation` (plain-language reason string) |

**FR-P02-24 — Default DoA by template.** Seeded examples (tenant edits values; every row cites "tenant policy" as the source): *Startup*: any agreement → founder approval; signatory = any director. *SME*: ≤ ₹5 lakh → department head; ₹5–50 lakh → CLO + CFO; > ₹50 lakh → MD; any non-standard indemnity → CLO. *Regulated finance company*: outsourcing and IT vendor agreements → CLO + CRO/CISO step + board-approved policy check flag; related party → board/audit committee flag [REC; content from P13/LDC].

**FR-P02-25 — Evaluation.** When a maker submits an item whose action is DoA-driven, `wf` calls `rules.evaluate(doa_table_version, inputs)` and stores the result (`wf.approval_requests.route`) with the table version and inputs digest, so the route is reproducible and explainable ("Needs CLO and CFO because value ₹18 lakh is between ₹5 lakh and ₹50 lakh — DoA v7 row 3"). Changing the DoA table never re-routes in-flight requests unless the owner chooses "apply to pending" (each affected request then restarts with notice).

**FR-P02-26 — Simulator** (SCR-P02-10). "Who approves…?" form: pick inputs; see the route, the people currently holding each step and whether any is out of office or conflicted. Also runs a **gap check**: values or departments with no matching row, steps with no current holder, steps where the only holder would conflict with the typical maker.

**FR-P02-27 — Publication.** Publishing a DoA version is maker-checker (`wf.doa.publish`, REQUIRED, checker `ORG_OWNER` or `ORG_CLO` ≠ maker) with an effective date (NN-18).

### 4F. Maker-checker engine (NN-18)

**FR-P02-28 — Action catalogue.** Every action that can require a second person is registered in `wf.mc_actions` from `cfg/registry/mc-actions.yaml` (published as Appendix D §D.7): `action_code` (`<module>.<object>.<verb>`), description, owning module, workspace types, **platform mode** (`LOCKED` — always required, tenant cannot relax; `REQUIRED` — on by default, tenant may make stricter only; `DEFAULT_OFF` — tenant may enable), default checker selector, minimum AAL, evidence requirements, and the NN rule it implements. The NN-18 set is `LOCKED` for company tenants and platform staff: payments/refunds/credits, access grants and role elevation, data exports of a company tenant, critical configuration, master-data changes of a client, template/rule publication, price and revenue-stream switches, bulk deletes, agent autonomy changes. A module cannot perform a catalogue action except through `wf.approvals.execute(action_code, payload)`; a Semgrep rule and `NN-18_catalogue_coverage` (calls each catalogue action's service method directly and expects refusal) enforce this.

**FR-P02-29 — Tenant configuration** (SCR-P02-11). Per action (and optionally per entity, department or document type): mode (cannot go below the platform mode), checker selector (roles, positions, named people, or "DoA table"), number of approvals (1–3), order (`ANY`, `ALL`, `SEQUENCE`), minimum AAL (≥ platform), evidence required (comment, attachment, checklist), request expiry (`wf.approval.expiry_days`, default 14; Appendix R), escalation ladder (after N working hours to the next position up, then the owner), self-service rules for small tenants (FR-P02-34). Changes are themselves maker-checker (`cfg.mc_policy.change`, LOCKED).

**FR-P02-30 — Request object.** `wf.approval_requests` (`apr_`): action, tenant, entity, maker (person, user, actor type, grant, on-behalf-of), payload (encrypted per class), **payload digest** (SHA-256 of canonical JSON plus the digests of referenced document versions), route (from config or DoA), steps and decisions, state, expiry, linked items. Decisions (`wf.approval_decisions`): checker, decision (`APPROVE`, `REJECT`, `RETURN_FOR_CHANGES`), reason code, comment, AAL and `auth_time` at decision, digest seen.

**FR-P02-31 — Binding to content.** Execution recomputes the digest; any change to the payload or a referenced document version after any approval invalidates all approvals (`LD-WF-012`) and returns the request to the maker. A checker always sees a diff from the last approved version where one exists (P07 redlines for agreements).

**FR-P02-32 — Execution.** On final approval the engine executes the action in the same transaction where possible (internal effects) or hands it to the owning workflow with the approval reference (external side effects — sending, signing, paying, exporting — run with an idempotency key and remain subject to their own NN gates, e.g., NN-07 eligibility, NN-08 stamp-before-sign). The ledger records maker, each checker and the executor.

**FR-P02-33 — Inbox and fewer clicks.** Checkers work from one approvals inbox (SCR-P02-12) across actions: grouped by urgency and type, "Review next" flow, side-by-side diff and context, one-tap approve with step-up only where the AAL requires, bulk approval only for actions marked `bulk_allowed` (never for exports, grants, payments or master data). Email and push approvals open the review screen; there is no "approve from email" link (phishing-resistant design).

**FR-P02-34 — Small tenants and the solo-owner rule.** A company tenant with only one eligible user cannot satisfy a LOCKED action's second person. Rules: (a) the wizard and the home screen prompt the owner to add a second approver (a co-director, a partner, or an engaged professional as additional reviewer); (b) until then, LOCKED actions of the tenant's own data (export of the tenant, bulk delete, critical configuration) may proceed only with AAL2 step-up, a 24-hour cooling-off, notification to every contact point of the owner and of any other director on record, and a "solo approval" mark on the ledger event [REC — interprets NN-18 for one-person companies; recorded as a pack-lead conflict to confirm]; (c) actions affecting third parties or money (refund requests, price changes) are never solo-approvable. PERSONAL workspaces: exports and deletions of the individual's own data are the individual's right and need no second person (NN-11); delegates' sends may require the owner's approval (FR-P02-13).

**FR-P02-35 — Expiry and escalation.** Requests not decided by expiry move to `EXPIRED` and the maker is told; escalation steps notify the next holder and, finally, the owner; out-of-office routing applies (FR-P02-40). Statutory or contractual deadlines linked to a request (e.g., notice reply due) raise the priority automatically.

### 4G. Segregation of duties

**FR-P02-36 — SoD engine.** `iam.sod_rules` (Appendix D §D.9) with enforcement `BLOCK` or `WARN` (tenant may upgrade WARN → BLOCK, never downgrade). Checks run at: grant time (toxic role combinations on overlapping scopes), request time (maker ≠ any checker in the route), decision time (checker ≠ maker, ≠ maker's delegator, ≠ the maker's other identity across realms via `person_link`, ≠ the sponsor of the agent that drafted it where the tenant sets `wf.sod.agent_sponsor_cannot_check`), nightly (drift report) and in access reviews.

**FR-P02-37 — Person-level identity.** SoD compares **persons**, not accounts: a LawDocs RM who also has a customer account, or a professional who is also a director of the client, is the same person (P01 `person_link`, plus a declared-relationship check at grant time: "Are you related to or employed by this client?").

**FR-P02-38 — Agents.** `AGT_*` principals hold maker capabilities only; any catalogue action routed to an agent as checker or approver is refused (`LD-WF-020`; NN-43); agent-prepared items carry the agent's sponsor and the mission ID.

### 4H. Delegation and out-of-office

**FR-P02-39 — Delegation.** A user may delegate approval and/or task authority to another person holding the same role on the same scope, for ≤ `iam.delegation.max_days` (default 30, tenant ≤ 90), depth 1, with reason. Delegation never creates permissions; the delegate inherits the delegator's SoD exclusions; actions read "approved by B for A (delegation DLG-…)" and both receive an end-of-delegation summary. Not delegable: `ORG_OWNER` powers, authorised-signatory authority (a signatory must hold authority in their own right — P01 FR-P01-35), nominee status, and any role marked `non_delegable`.

**FR-P02-40 — Out-of-office.** A user sets "Away" with dates and an optional delegate; incoming approvals route to the delegate, else to the escalation ladder after `wf.away.escalation_hours` (default 8 working hours). Away status is a self-declared availability signal, never a monitoring metric (NN-33; CH-32); it is not used in performance measures.

**FR-P02-41 — RM handover.** When a LawDocs RM under a delivery grant is away or leaves, `OPS_DELIVERY_LEAD` proposes a replacement grant; the client approves; open items transfer per the grant's handover rule; the client sees the change in the access-transparency log (P18).

**FR-P02-42 — Leaver handling.** SCIM deactivation, membership end or HR exit (P13) ends grants within 60 seconds, reassigns open items per rule (default: department head), cancels pending requests the leaver made (with notice to checkers) and keeps all history.

### 4I. Group companies and cross-functional staff roles (Ecosystem Spec §4.6)

**FR-P02-43 — Client groups.** Cross-entity roles for client groups (a group CLO, a shared-services legal team) are explicit grants per entity or child tenant; the admin can bulk-create them, but each is a separate grant record with its own scope, approval and expiry. Group dashboards aggregate across entities the viewer holds grants for.

**FR-P02-44 — Never inherited.** No grant, membership or role in a parent tenant, group umbrella, or another Infrabyx product confers any access to a LawDocs tenant or entity. `NN-17_group_grant_not_inherited` seeds a GROUP tenant, two children and a user with umbrella admin only, and asserts zero access to child data.

**FR-P02-45 — Infrabyx cross-functional staff.** Staff of any Infrabyx company authenticate through the group IdP (`ld-staff`), but authorisation stays per product and per legal entity (Ecosystem Spec §4.6). A staff member gets LawDocs staff roles (`OPS_*`, `PLT_*`) only through (a) employment by the LawDocs operating entity (OH10 provisioning) or (b) a `group_grant` received as a SCIM group membership carrying `role` (from LawDocs' catalogue), `entity_scope`, `purpose` (e.g., `SHARED_SUPPORT`, `IMPLEMENTATION_DELIVERY`, `ENGINEERING_OPS`), `data_class_max` and `valid_to` ≤ 90 days. LawDocs enforces expiry itself (no dependency on OH availability) and ends sessions within 60 seconds of `valid_to` or revocation; every use is logged; grants appear in the quarterly staff access review. A group grant gives staff-app roles; it never gives access to customer tenant data, which still requires a client-approved delivery grant or break-glass (NN-17).

**FR-P02-46 — Walls.** SoD rules block: any group grant combining an Equator case-level role with a LawDocs client-facing delivery role on overlapping customers (Ecosystem Spec §4.6 neutrality wall); any Consumer Help case-manager role together with any role serving lender or insurer clients of the group (NN-23); any LawDocs staff role in a tenant together with the client's checker role on the same scope (SoD-12).

### 4J. Grant types: delivery, engagement, onboarding, counsel, auditor, nominee, break-glass (NN-17)

**FR-P02-47 — Common grant model.** One grant contract, one supertype register (Appendix A §A.9, R-A-05). Every non-ROLE grant is a row in `iam.grants` (`grt_`) owned by P02. **Delivery-side grants** — LawDocs staff and independent practitioners acting inside a client tenant (types `DELIVERY`, `ENGAGEMENT`, `ONBOARDING`, `SUPPORT_SESSION`) — additionally have a 1:1 extension row in `sdc.delivery_grants` keyed by the same `grt_` and owned by P18 (FR-P18-11: grantee kinds `LAWDOCS_STAFF`, `PRACTITIONER`, `PRACTITIONER_FIRM_MEMBER`; purposes `RETAINER_DELIVERY`, `ENGAGEMENT_DELIVERY`, `IMPLEMENTATION`, `SUPPORT_SESSION`; tenant role `ORG_DELEGATED_MAKER` only) and emit `sdc.DeliveryGrant*` events instead of `iam.Grant*`. `packages/authz` reads the register and its extension through one `GrantResolver` interface defined here, so policies, expiry enforcement, SoD checks and the transparency log treat them identically. `grant_type` ∈ {`ROLE`, `DELIVERY`, `ENGAGEMENT`, `ONBOARDING`, `EXTERNAL_COUNSEL`, `AUDITOR`, `SHARE`, `DELEGATE`, `FAMILY`, `GUARDIAN`, `NOMINEE`, `AGENT_DELEGATION`, `GROUP`, `BREAK_GLASS`, `SUPPORT_SESSION`}, grantee (person, staff identity or agent), tenant, roles granted, scopes, `data_class_max`, capabilities excluded, `valid_from`/`valid_to`, basis (engagement ID, retainer, order, audit engagement letter, ticket/incident), proposed_by, approved_by (client side), state, revoke reason. Lifecycle §5.1. Enforcement: Cerbos principal attributes include active grants; every request under a grant sets `app.grant_id`; every read and write under a grant appears in the client's **access-transparency log** (P18 renders it; P02 writes it).

**FR-P02-48 — Delivery grants** (LawDocs staff in a client tenant; D-02, R-064, R-065). Created by the client admin or proposed by `OPS_DELIVERY_LEAD` and approved by the client (`iam.grant.delivery.approve`, LOCKED). Role `ORG_DELEGATED_MAKER` only, for named departments, functions or matter types; never any checker, approver, signatory, director, auditor or admin role (P18 FR-P18-11); valid for the retainer term (≤ 12 months per grant, renewable). Staff act under their `ld-staff` identity through token exchange; the UI marks them "LawDocs" everywhere; exports only through deliverable workflows (P18); credential-vault access only per credential and per client approval (P18, NN-16). Revocation by the client or at term end takes effect within 60 seconds.

**FR-P02-49 — Engagement grants** (independent professionals; P16). Same rules and store as delivery grants (grantee kind `PRACTITIONER`, purpose `ENGAGEMENT_DELIVERY`) with basis = engagement ID; scope limited to the engagement's matter, documents and deal room; ends at engagement close plus a configurable read-only tail (default 30 days) for final deliverables.

**FR-P02-50 — Onboarding, external counsel and auditor grants.** Onboarding grants (`OPS_ONBOARDING`, ≤ 30 days, set-up screens and import tools only). External counsel (`ORG_EXT_COUNSEL`): matters and documents explicitly assigned; privileged material labelled. Auditor (`ORG_AUDITOR_RO`): read-only datasets and periods, watermarked exports, ≤ 90 days per grant (Ecosystem Spec §4.7 pattern).

**FR-P02-51 — Break-glass and support sessions.** Support sessions (read-only, screens named in the ticket, ≤ 60 minutes) need the client's in-app approval. Break-glass (access without client approval, for a declared security incident or a legal order) needs two staff approvers at AAL3 (`PLT_SECURITY_OFFICER` + one other), a justification ≥ 30 characters and a reference, is limited to `core.break_glass.max_minutes`, is recorded screen by screen, and produces a client report within 24 hours (NN-17; P00 schema). The client may set `iam.break_glass.prior_consent` = true, in which case break-glass for non-security reasons is impossible.

### 4K. Access reviews

**FR-P02-52 — Campaigns.** `iam.access_reviews`: scope (tenant, entity, department, grant types), cadence (company tenants quarterly by default; delivery, engagement, auditor and external-counsel grants monthly; PERSONAL workspaces: an annual "who can see my vault" reminder), reviewers (department heads for their units, owner for privileged roles, CLO for legal outsiders), items (memberships, role grants, privileged roles, delegations, all non-ROLE grants, active guests, API clients, SSO group mappings), decisions (`KEEP`, `REVOKE`, `MODIFY`, `ESCALATE`) with reason. Non-response: reminder at 50% and 90% of the window, escalation to owner, optional auto-revoke at close for guests, delivery and engagement grants (`iam.access_review.auto_revoke_unreviewed`, default true for those types).

**FR-P02-53 — Evidence.** Each completed campaign produces an evidence pack (who reviewed what, decisions, revocations executed, timestamps) exportable as XLSX + PDF and stored in the tenant's `99 System Data (CSV and JSON)/Access Reviews/` (Appendix K). Platform and staff campaigns emit `AccessReviewCompleted` to the Operations Hub through `int` (counts only; Ecosystem Spec §6.23) and feed SOC 2 CC6.2/CC6.3 and ISO/IEC 27001:2022 A.5.18 evidence (Appendix P).

**FR-P02-54 — Drift.** Nightly job flags: grants past expiry not yet ended (should be zero — alert), dormant privileged users (no sign-in 60 days), SoD WARN combinations, roles granted outside SCIM mapping, delivery grants without an active retainer in OH8 (via entitlement mirror).

### 4L. User-type homes and navigation (fewer clicks; R-028, R-030)

**FR-P02-55 — Role-based homes.** The home screen is assembled from widgets chosen by the active role set; users may rearrange, hide and pin (per user, per context); the owner may set the default layout for a role in the tenant.

| User type | Home widgets (default) | Primary navigation | Key click budgets |
|---|---|---|---|
| `IND_OWNER` | "Draft something", Continue drafts, Waiting for you (signatures, replies), Vault life-event folders (Property, Family, Work, Money, Vehicle, Disputes, Tax), upcoming renewals/expiries, Vidhi ask box | Home · Vault · Drafts · Sign · My matters · Help | Start a new document ≤ 2 taps; sign a pending request ≤ 3 taps; find a document by search ≤ 2 taps |
| `IND_DELEGATE` / `IND_FAMILY_MEMBER` | Shared folders, tasks from owner | Shared · Tasks | Upload to a shared folder ≤ 3 taps |
| `ORG_OWNER` / `ORG_ADMIN` | Setup checklist until done; people and roles; approvals pending; plan and usage; changes made by LawDocs | Home · Legal desk · Contracts · Vault · Matters · People · Settings | Invite a user ≤ 3 clicks; change a DoA value ≤ 4 clicks |
| `ORG_CLO` | Legal risk dashboard (contracts expiring, high-risk clauses pending, matters by stage, hearings this week, legal spend), intake queue, team workload (assigned counts, not surveillance) | Legal desk · Contracts · Matters · IP · Notices · Reports | Assign an intake request ≤ 2 clicks; see all agreements expiring in 90 days ≤ 2 clicks |
| `ORG_LEGAL_MAKER` / `ORG_DELEGATED_MAKER` | My queue (assigned requests, drafts, negotiations awaiting me), returned items, due dates | Queue · Contracts · Drafting · Vault | Submit a draft for approval ≤ 2 clicks from the draft |
| `ORG_CHECKER` / `ORG_APPROVER` | Approvals inbox with "Review next", signing requests | Approvals · Sign · Contracts | Approve next item ≤ 2 clicks (+ step-up where needed) |
| `ORG_DEPT_HEAD` / `ORG_MEMBER` | "Request legal help" (intake form), my requests and their status, contracts of my department | Requests · Contracts | Raise a contract request ≤ 3 clicks |
| `ORG_DIRECTOR` / `ORG_KMP` | Items awaiting my approval or signature, board items (P13), legal risk summary | Approvals · Board · Reports | Sign a board-approved document ≤ 3 taps on mobile |
| `ORG_EXT_COUNSEL` / `ORG_AUDITOR_RO` | Assigned matters / audit scope only | Assigned | Open an assigned matter ≤ 2 clicks |
| `CP_GUEST` | Single task page (review, comment, sign) | — | Complete the requested action from the invitation ≤ 3 taps + OTP |
| `PRO_*` / `PRO_FIRM_ADMIN` | Client engagements, deliverables due, messages, calendar | Engagements · Calendar · Messages · Firm | Open the next deliverable ≤ 2 clicks |
| `OPS_RM` | Clients list with health and items due per client (P18) | Clients · Queue · Messages | Switch into a client's context ≤ 2 clicks |
| `PLT_SUPER_ADMIN` | Console home (P00 SCR-P00-01) | Console | — |

**FR-P02-56 — Navigation rules.** Menus show only what the role can use (UI trimming is convenience; the server still enforces); a module the tenant has not licensed appears once in "Discover" with a plain explanation, never as disabled clutter; deep links preserve context; every menu label has a help key (`hlp.<module>.<term>`).

**FR-P02-57 — Quick actions.** Command palette (Ctrl/⌘ + K) with role-filtered actions ("New NDA", "Approve next", "Invite", "Switch to Alpha Pvt Ltd").

**FR-P02-58 — Mobile.** Bottom navigation per P22 FR-P22-03 (workspace tab sets; P22 governs); approvals and signing optimised for one-hand use; protected screens block screenshots (NN-44).

### 4M. Master-data changes of a client by LawDocs (CH-26)

**FR-P02-59 — Client master data.** Fields designated master data (legal name, constitution, registered office, PAN/GSTIN/CIN, authorised signatories, owner account, plan-critical attributes) change only (a) by the client through `org.master_data.change` (LOCKED maker-checker inside the tenant; solo-owner rule applies), or (b) by LawDocs staff through a P00 Correction Entry of scope `MASTER_DATA` with the client's prior approval (`core.correction.tenant_ack_mode = PRIOR`), reason code and supporting document, two staff persons (maker ≠ checker) and client notification. The fast path for the owner's "super admin changes crucial client details" is SCR-P02-17: the RM raises the change from the client section, the client approves in-app in one tap, the checker approves, and the change applies — typically within one working day, fully visible.

**FR-P02-60 — Notification.** Every master-data change notifies all owners and admins of the tenant and appears in "Changes made by LawDocs" (P00 SCR-P00-08) when staff-initiated.

---

## 5. Workflows and state machines

### 5.1 Grant lifecycle (all non-ROLE grants)

State machine: Appendix A §A.9 governs (Resolution R-A-05): P02 and P18 describe one machine. `iam.grants` is the supertype register; a delivery grant (P18) is an `iam.grants` row plus a 1:1 `sdc.delivery_grants` extension on the same `grt_` and emits `sdc.DeliveryGrant*` events instead of `iam.Grant*`. `APPROVED` is transient (only while `valid_from` is in the future). A delivery grant may also go `PROPOSED → ACTIVE` under a client-approved standing authorisation (X-20; OFF by default; activation notice to the client ≤ 1 h).

| State | Entry | Next | Actor | Guard | Events |
|---|---|---|---|---|---|
| `PROPOSED` | Proposed by OPS lead, professional engagement acceptance, owner invitation | `ACTIVE` (or `APPROVED` while `valid_from` is in the future), `DECLINED`, `WITHDRAWN` | Client approver | Approver ≠ grantee; AAL2; SoD check passes | `in.lawdocs.iam.GrantProposed.v1` |
| `APPROVED` | Client approves | `ACTIVE` (at `valid_from`) | System | Grantee identity level meets role minimum | — |
| `ACTIVE` | Valid period starts | `SUSPENDED`, `REVOKED`, `RENEWAL_PENDING` | Client, system | — | `…GrantActivated.v1`; transparency log entries |
| `RENEWAL_PENDING` | 14 days before `valid_to` | `ACTIVE` (renewed by fresh approval), `SUSPENDED`, `REVOKED`, `EXPIRED` (at `valid_to`) | Client, system | Fresh approval, never automatic | — |
| `SUSPENDED` | Client or security action | `ACTIVE`, `REVOKED` | Client, security | — | Sessions ended ≤ 60 s |
| `DECLINED` / `WITHDRAWN` | Client declines / proposer withdraws | — | Client / proposer | — | Ledger entry |
| `REVOKED` / `EXPIRED` | — | — | — | — | Sessions ended ≤ 60 s; open items reassigned; `…GrantEnded.v1` |

### 5.2 Approval request

State machine: Appendix A §A.11 governs (Resolution R-A-06: `wf` is the only approval engine; P07 `clm.approval_step` is a projection).

`DRAFT → SUBMITTED (route computed) → IN_REVIEW (step n) → {APPROVED → EXECUTING → EXECUTED | EXECUTION_FAILED (retry or return) } | REJECTED | RETURNED (to maker; digest reset) | EXPIRED | CANCELLED (maker or leaver)`. Any payload change after the first decision → `RETURNED` with `LD-WF-012`.

### 5.3 Custom role and DoA publication

`DRAFT → IN_REVIEW (maker-checker) → PUBLISHED (version n, effective date) → SUPERSEDED`; DoA "apply to pending" restarts affected requests with notice.

### 5.4 Delegation

`SCHEDULED → ACTIVE → ENDED (date) | CANCELLED`; on `ENDED` both parties receive a summary.

### 5.5 Group grant (Infrabyx staff)

Mirrors OH: `RECEIVED (SCIM membership with valid_to) → ACTIVE → EXPIRED | REVOKED`; LawDocs enforces `valid_to` locally; usage logged; quarterly review.

### 5.6 Access review campaign

`SCHEDULED → OPEN → (reminders, escalation) → CLOSING (auto-revoke where configured) → COMPLETED (evidence pack) | OVERDUE`.

---

## 6. Screens and UX

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P02-01 | all | Context switcher | Memberships and grants with type icon, role, expiry; search; recent | Single context → hidden | Full-screen sheet | Combobox pattern; announces new context |
| SCR-P02-02 | web | Organisation structure | Tree of entities, branches, departments, teams, positions; drag to move (with change-set preview) | Template picker | Read-only tree | Tree is keyboard-operable; move also by form |
| SCR-P02-03 | web | Department detail | Head, members, positions, approval rules in effect | — | Yes | — |
| SCR-P02-04 | web | People | Members, roles, grants, identity level, MFA state, last active (sign-in date only) | Invite CTA | Yes | — |
| SCR-P02-05 | web | Person access detail | All roles and grants with scopes and expiries; SoD warnings | — | Yes | — |
| SCR-P02-06 | web | Invite / grant wizard | Role templates, scope picker, expiry, approval need, SoD preview | Conflict → explanation | Yes | — |
| SCR-P02-07 | web | Roles catalogue | Base roles, custom roles, holders | — | — | — |
| SCR-P02-08 | web | Custom role builder | Capability picker by module, ceiling indicator, plain-language summary, affected people preview | Blocked combination explained | — | Capability list grouped with headings |
| SCR-P02-09 | web | DoA tables | Rows with inputs → steps; versions; effective dates | — | — | Table view with row headers |
| SCR-P02-10 | web | "Who approves?" simulator + gap check | Inputs form; route with current holders; gaps | — | Yes | — |
| SCR-P02-11 | web | Maker-checker settings | Catalogue actions with platform mode, tenant mode, checker selector, AAL, expiry | LOCKED rows show the NN reason | — | — |
| SCR-P02-12 | web/mobile | Approvals inbox | Grouped list, "Review next", diff, context, approve/reject/return | "Nothing to approve" | Optimised | Diff has text alternative |
| SCR-P02-13 | web | Delegation and away | Dates, delegate, scope | — | Yes | — |
| SCR-P02-14 | web | Outsider access (grants) | Delivery, engagement, counsel, auditor, onboarding grants; approve/renew/revoke; transparency log link | — | Yes | — |
| SCR-P02-15 | web | Access reviews | Campaigns, my review items, decisions, evidence download | — | Yes | — |
| SCR-P02-16 | web (Personal) | Who can see my vault | Family, delegates, guardians/wards, nominees, shares, guests | "Only you" | Yes | — |
| SCR-P02-17 | delivery / web | Master-data change request | RM raises; client approves; checker; status | — | Yes | — |
| SCR-P02-18 | web | Home (role-based) | Widgets per §4L; customise layout | First-run checklist | Bottom nav | Landmarks; widgets are regions with headings |

**Help keys:** `hlp.org.legal_entity`, `hlp.org.department`, `hlp.org.position`, `hlp.org.workspace_type`, `hlp.iam.role_grant`, `hlp.iam.custom_role`, `hlp.iam.delivery_grant`, `hlp.iam.engagement_grant`, `hlp.iam.group_grant`, `hlp.iam.break_glass`, `hlp.iam.access_review`, `hlp.wf.maker_checker`, `hlp.wf.doa`, `hlp.wf.sod`, `hlp.wf.delegation`, `hlp.wf.solo_approval`.

---

## 7. Backend design

### 7.1 Modules

`org` (structure, templates, restructures); `iam` (roles, custom roles, grants, delegations, SoD rules, access reviews, transparency log writes); `wf` (maker-checker actions, policies, requests, decisions, DoA tables and evaluation, inbox); `rul` (DoA evaluation through `RULES_PORT`; P03 owns the editor); `int` (group-grant intake from OH10 SCIM; `AccessReviewCompleted` out); `packages/authz` and `policies/cerbos/`.

### 7.2 Tables

| Table | Key columns | Indexes | RLS | Retention |
|---|---|---|---|---|
| `org.branches` (`brn_`) | tenant_id, legal_entity_id, code, state, valid_period | (tenant_id, code) | Tenant | Life + 8 y |
| `org.departments` (`dep_`) | tenant_id, legal_entity_id, parent_id, path ltree, canonical_function, valid_period | GiST path | Tenant | Life + 8 y |
| `org.teams` (`tem_`), `org.positions` (`pos_`) | department_id, holder_person_id, kmp_type, valid_period | — | Tenant | Life + 8 y |
| `org.restructures` | change set, effective_at, batch_id | — | Tenant | 8 y |
| `iam.roles` | code, group, capabilities, ceilings, flags | code unique | Exempt (platform) | Permanent |
| `iam.custom_roles` | tenant_id, base_role, capabilities, version, state | (tenant_id, name, version) | Tenant | Life + 8 y |
| `iam.role_grants` / `iam.grants` (`grt_`) — delivery-side grants add a 1:1 P18 `sdc.delivery_grants` extension row on the same `grt_` | grantee, grant_type, roles, scopes, valid_period, basis, state | (tenant_id, grantee), (state, valid_to) | Tenant | Life + 8 y |
| `iam.delegations` (`dlg_`) | delegator, delegate, scope, valid_period, reason | — | Tenant | 8 y |
| `iam.sod_rules` | code, pair definition, enforcement | — | Exempt + tenant overrides | Permanent |
| `iam.access_reviews`, `iam.access_review_items` | campaign, reviewer, decision | — | Tenant | 8 y |
| `iam.access_transparency_log` | tenant_id, grant_id, actor, action, object, at | (tenant_id, at) | Tenant (append-only) | ≥ 8 y |
| `wf.mc_actions` | action_code, platform_mode, defaults, nn_ref | unique | Exempt | Permanent |
| `wf.mc_policies` | tenant_id, action_code, scope filter, mode, selector, count, order, aal, expiry | (tenant_id, action_code) | Tenant | Bitemporal |
| `wf.approval_requests` (`apr_`) | action, maker refs, payload_enc, payload_digest, route, state, expires_at | (tenant_id, state), (approver queue) | Tenant | 8 y |
| `wf.approval_decisions` | request_id, checker, decision, digest_seen, aal, auth_time | — | Tenant | 8 y |
| `wf.doa_tables` | tenant_id, legal_entity_id, version, rules (ZEN JSON), effective_from, state | — | Tenant | Permanent versions |
| `rpt.home_layouts` | tenant_id, role or user, widgets | — | Tenant | Life |

### 7.3 APIs (selected)

| Method and path | Purpose | Role / scope | Idempotent |
|---|---|---|---|
| `GET /v1/contexts` | List switchable contexts for the person | user | — |
| `POST /v1/contexts:switch` | Switch active context | user | Yes |
| `GET/POST/PATCH /v1/org/units` | Branches, departments, teams, positions | `ORG_ADMIN`, `ORG_DEPT_HEAD` (own, if allowed) | Yes |
| `POST /v1/org/restructures` / `:preview` / `:apply` / `:undo` | Restructure | `ORG_ADMIN` + checker | Yes |
| `POST /v1/iam/grants` / `:approve` / `:decline` / `:revoke` / `:renew` | Grants (all types) | per Appendix D | Yes |
| `GET /v1/iam/grants?grantee=&type=` | List | admin, CLO, owner | — |
| `POST /v1/iam/custom-roles` / `:submit` / `:publish` | Custom roles | `ORG_ADMIN` maker, owner/admin checker | Yes |
| `POST /v1/iam/delegations` / `:cancel` | Delegation | user | Yes |
| `POST /v1/wf/approval-requests` (internal via `wf.approvals.execute`) | Create request | modules | Yes |
| `GET /v1/wf/inbox` | Approvals inbox | checker roles | — |
| `POST /v1/wf/approval-requests/{id}:approve` / `:reject` / `:return` | Decide | route members; step-up per AAL | Yes |
| `GET/PUT /v1/wf/mc-policies/{action}` | Configure maker-checker | `ORG_OWNER`, `ORG_ADMIN` (+ checker) | Yes |
| `POST /v1/wf/doa-tables` / `:publish`; `POST /v1/wf/doa:simulate` | DoA | `ORG_CLO`, `ORG_OWNER`; simulate: admins, CLO, dept heads | Yes |
| `POST /v1/iam/access-reviews` / `GET …/{id}/items` / `POST …/items/{id}:decide` | Access reviews | owner, reviewers | Yes |
| `GET /v1/iam/transparency-log` | Outsider access log | owner, admin, CLO | — |
| `POST /v1/org/master-data-changes` / `:client-approve` | Master-data change by LawDocs — tenant-side entry point to the single master-data machine (Appendix A §A.56, wrapping A.1; Resolution R-A-21; P18 §5.3 is the same machine) | `OPS_RM` maker; client owner; staff checker | Yes |
| `/scim/v2/Groups` (staff realm) | Group-grant memberships from OH10 | OH SCIM client | — |

### 7.4 Domain events

`in.lawdocs.org.UnitCreated.v1`, `…org.UnitChanged.v1`, `…org.RestructureApplied.v1`, `…org.PositionHolderChanged.v1`, `…iam.RoleGranted.v1`, `…iam.RoleRevoked.v1`, `…iam.CustomRolePublished.v1`, `…iam.GrantProposed.v1`, `…iam.GrantActivated.v1`, `…iam.GrantEnded.v1`, `…iam.DelegationStarted.v1`, `…iam.DelegationEnded.v1`, `…iam.SodViolationBlocked.v1`, `…iam.AccessReviewCompleted.v1`, `…wf.ApprovalRequested.v1`, `…wf.ApprovalDecided.v1`, `…wf.ApprovalInvalidated.v1`, `…wf.ApprovalExecuted.v1`, `…wf.ApprovalExpired.v1`, `…wf.DoaTablePublished.v1`, `…wf.McPolicyChanged.v1`. Ecosystem mapping by `int`: staff `AccessReviewCompleted` (counts only) to OH (Ecosystem Spec §6.23).

### 7.5 Jobs and workflows

`GrantExpiryEnforcer` (every minute; ends sessions ≤ 60 s after `valid_to`); `GrantRenewalReminder` (daily); `ApprovalEscalation` (every 15 min); `ApprovalExpiry` (hourly); `DelegationScheduler` (every 5 min); `SodDriftScan` (nightly); `AccessReviewScheduler` (daily); `AccessReviewAutoRevoke` (at campaign close); `RestructureApplyWorkflow` (Temporal; batch + undo); `GroupGrantReconciler` (hourly against OH10 SCIM state; local expiry wins); `DormantPrivilegedUserScan` (weekly).

### 7.6 Error codes

`LD-ORG-001` unit code already used · `LD-ORG-002` restructure leaves open items without an owner · `LD-ORG-010` master-data field requires the change workflow · `LD-IAM-101` role requires approval · `LD-IAM-102` grant scope exceeds grantor's own scope · `LD-IAM-103` role not valid for this workspace type · `LD-IAM-104` grantee identity level below role minimum · `LD-IAM-110` grant expired · `LD-IAM-111` grant not approved by client · `LD-IAM-120` custom role exceeds base-role ceiling · `LD-IAM-121` custom role combines conflicting capabilities · `LD-IAM-130` delegation not allowed for this role · `LD-IAM-131` delegate lacks the role on this scope · `LD-WF-001` action requires approval · `LD-WF-010` maker cannot approve own request · `LD-WF-011` checker conflicts by SoD rule · `LD-WF-012` approval invalidated by change · `LD-WF-013` request expired · `LD-WF-014` tenant cannot relax a locked action · `LD-WF-015` solo approval cooling-off in progress · `LD-WF-020` agents cannot check or approve · `LD-WF-030` no DoA row matches — route to owner · `LD-WF-031` DoA step has no current holder.

---

## 8. Integrations

| Port / source | Use | Failure behaviour |
|---|---|---|
| `RULES_PORT` (GoRules ZEN + CEL) | DoA evaluation | Fail closed: route to `ORG_OWNER` with `LD-WF-030`; never skip approval |
| Cerbos PDP | Every authorisation decision and query plan | Fail closed (deny); health alarm |
| OH10 SCIM (staff realm) | Staff identities and `group_grant` memberships | Local expiry enforcement continues; new grants wait |
| OH4 | Onboarding grant milestones (counts only) | Queue |
| Governance kernel / LDC contracts | Directors and KMP designations | Use last confirmed snapshot; flag staleness |
| P18 Delivery Console | Renders grants, transparency log, RM workbench | — |
| P17 billing mirror | Seat counts by class; delivery grant ↔ active retainer check | Drift flag only |

---

## 9. Settings and configuration (Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `org.levels_enabled` | TENANT | set | ENTITY, DEPARTMENT (+ BRANCH, TEAM optional) | `ORG_ADMIN` | N |
| `org.dept_head.can_manage_members` | TENANT | bool | false | `ORG_OWNER` | Y |
| `org.department_template` | TENANT | enum | by constitution/size | `ORG_ADMIN` (at setup) | N |
| `org.context.colour_band` | TENANT | colour token | brand default | `ORG_ADMIN` (contrast-checked) | N |
| `iam.grant.delivery.max_months` | PLATFORM | int | 12 | `PLT_SECURITY_OFFICER` | Y |
| `iam.grant.engagement.read_tail_days` | TENANT | int (0–90) | 30 | `ORG_OWNER` | N |
| `iam.grant.auditor.max_days` | PLATFORM | int | 90 | locked | — |
| `iam.grant.renewal_notice_days` | TENANT | int | 14 | `ORG_ADMIN` | N |
| `iam.break_glass.prior_consent` | TENANT | bool | false | `ORG_OWNER` | Y |
| `iam.support_session.max_minutes` | PLATFORM | int | 60 | `PLT_SECURITY_OFFICER` | Y |
| `iam.delegation.max_days` | TENANT (≤ 90) | int | 30 | `ORG_OWNER` | N |
| `iam.delegate.max_days` (Personal) | USER (≤ 365) | int | 180 | owner | N |
| `iam.access_review.cadence.<grant_type>` | TENANT | enum | QUARTERLY (roles), MONTHLY (outsider grants) | `ORG_OWNER` (tighten only for outsiders) | Y |
| `iam.access_review.auto_revoke_unreviewed` | TENANT | bool | true for guests, delivery, engagement | `ORG_OWNER` | Y |
| `iam.sod.<rule>.enforcement` | TENANT (WARN → BLOCK only) | enum | per Appendix D | `ORG_OWNER` | Y |
| `wf.mc.<action>.mode` | TENANT (≥ platform mode) | enum | per catalogue | `ORG_OWNER`/`ORG_ADMIN` | Y (LOCKED action `cfg.mc_policy.change`) |
| `wf.mc.<action>.approvals_required` | TENANT | int (1–3) | 1 | same | Y |
| `wf.mc.<action>.min_aal` | TENANT (≥ platform) | enum | per catalogue | same | Y |
| `wf.approval.expiry_days` | TENANT | int (3–30) | 14 | `ORG_ADMIN` | N |
| `wf.mc.solo_owner.cooling_off_hours` | PLATFORM | int | 24 | `PLT_SECURITY_OFFICER` | Y |
| `wf.mc.payment_threshold_inr` | TENANT | money | 0 (all company-initiated payments) | `ORG_OWNER` | Y |
| `wf.away.escalation_hours` | TENANT | int | 8 working hours | `ORG_ADMIN` | N |
| `wf.doa.apply_to_pending_default` | TENANT | bool | false | `ORG_CLO` | N |
| `wf.sod.agent_sponsor_cannot_check` | TENANT | bool | true | `ORG_OWNER` | Y |
| `rpt.home.default_layout.<role>` | TENANT | json | platform default | `ORG_ADMIN` | N |

---

## 10. Security, privacy and audit

- **Threats (Appendix P §P.2):** privilege escalation by an admin granting themselves checker (SoD-09 block; second admin); collusion between maker and checker (two-step routes for high values; DoA; access reviews; anomaly flags such as one checker approving > 90% of one maker's items within minutes); approval of a different version than reviewed (payload digest binding); RM misuse under a delivery grant (client approval, scopes, transparency log, no export, monthly reviews); staff using group roles to reach tenant data (group grants never confer tenant data access); stale access after leavers (SCIM ≤ 60 s, nightly drift); phishing approvals by email (no approve-by-link).
- **Monitoring is proportionate (NN-33):** last sign-in date, approval counts and SLA metrics are visible to admins; no keystroke, screen, webcam, browsing or idle-time capture; "Away" is self-declared; workload widgets show assigned counts and due dates, not activity traces.
- **Data classes:** org structure `INTERNAL`; grants and decisions `CONFIDENTIAL`; payloads per their source class (encrypted).
- **Audit:** every grant, revoke, role change, custom-role publication, delegation, approval decision (with digest and AAL), DoA publication, maker-checker policy change, access-review decision, restructure, master-data change and context switch.
- **Export map (NN-11):** `org.*` → `01 Company Profile/Organisation Structure.xlsx`; `iam.role_grants` + `iam.grants` → `01 Company Profile/People and Access/Access Register.xlsx`; `iam.access_transparency_log` → `99 System Data (CSV and JSON)/access_transparency/Outsider Access Log.csv` (Appendix K §K.3.5); `wf.approval_requests` + decisions → `99 System Data (CSV and JSON)/Approvals Register.xlsx` (and per-agreement copies under the agreement folder `01 Drafts/Approvals.pdf` via P07); `wf.doa_tables` → `06 Policies and Registers/Delegation of Authority (v<n>).xlsx`; `iam.access_reviews` → `99 System Data (CSV and JSON)/Access Reviews/`; Personal: `iam.grants` (family, delegates, nominees) → `03 Family and Succession/Who Can See My Vault.xlsx`.

---

## 11. AI touchpoints and guardrails

- Agents (P09) are principals with maker capabilities only; the engine refuses agent decisions (`LD-WF-020`; NN-43); agent-prepared submissions show "Prepared by Vidhi Contracts agent for Neha (sponsor)".
- Vidhi may **suggest** a DoA table from the tenant's uploaded policy document, a custom role from a plain-language description, or a department structure from an org chart image (P05); suggestions are drafts that follow normal publication maker-checker (NN-18, NN-43).
- Vidhi explains a route ("why does this need the CFO?") from the stored DoA explanation, never by re-deriving it.
- No AI in SoD decisions, grant approvals or access-review decisions.

---

## 12. Acceptance criteria (`tests/acceptance/p02/*.feature`)

```gherkin
@P02-AT-01 @NN-18
Scenario: A maker cannot approve their own agreement
  Given "Neha" (ORG_LEGAL_MAKER and ORG_CHECKER in Legal) submits agreement LD-AGR-2026-000123 for approval
  When Neha opens the approvals inbox
  Then the request is not listed for her
  And a direct API call to approve returns "LD-WF-010"

@P02-AT-02 @NN-18
Scenario: Approval is bound to the version reviewed
  Given CFO "Arjun" approved step 1 of an agreement with payload digest D1
  When the maker edits clause 9 and the digest becomes D2
  Then all approvals are invalidated with "LD-WF-012" and the request returns to the maker
  And the next reviewer sees a redline from the last approved version

@P02-AT-03
Scenario: DoA routes by value and explains why
  Given DoA v7 says ₹5–50 lakh needs CLO then CFO
  When a ₹18,00,000 vendor agreement is submitted in Procurement
  Then the route is CLO → CFO
  And the explanation reads "Needs CLO and CFO because value ₹18 lakh is between ₹5 lakh and ₹50 lakh — DoA v7 row 3"

@P02-AT-04
Scenario: No DoA row matches
  Given DoA v7 has no row for document type "Franchise agreement"
  When such an agreement is submitted
  Then it routes to ORG_OWNER with "LD-WF-030" and the gap appears in the simulator's gap check

@P02-AT-05 @NN-29
Scenario: A tenant tightens maker-checker without LawDocs
  Given action "dms.share.external" is DEFAULT_OFF on the platform
  When owner "Kavita" sets it REQUIRED with checker "ORG_CLO" and a second admin approves the policy change
  Then external shares by makers wait for CLO approval from the effective time
  And no LawDocs staff action was needed

@P02-AT-06 @NN-18
Scenario: A tenant cannot relax a locked action
  When an owner tries to set "xpt.tenant_export.run" to OFF
  Then the change is refused with "LD-WF-014" and the NN-18 reason is shown

@P02-AT-07
Scenario: Solo-owner company exports with cooling-off
  Given "Startup One Pvt Ltd" has a single user, its owner
  When the owner requests a full tenant export with AAL2 step-up
  Then the export is scheduled after 24 hours, every contact point of the owner is notified
  And the ledger event is marked "solo approval"

@P02-AT-08 @NN-17
Scenario: Delivery grant needs client approval and ends within 60 seconds of revocation
  Given OPS_DELIVERY_LEAD proposes a delivery grant for RM "Vikram" as ORG_DELEGATED_MAKER in Legal of "Beta Finance Ltd"
  Then Vikram has no access until owner "Meera" approves
  When Meera revokes the grant
  Then Vikram's sessions in Beta Finance end within 60 seconds and his open drafts are reassigned to the Legal head

@P02-AT-09 @NN-17
Scenario: LawDocs staff can never be a checker in a client tenant
  Given Vikram acts as delegated maker in Beta Finance
  When the admin tries to add Vikram's colleague RM "Asha" as a checker for Legal
  Then the configuration is refused citing SoD-12
  And Asha may only review Vikram's draft as OPS_QA_REVIEWER before submission, outside the client's route

@P02-AT-10 @NN-17
Scenario: Break-glass needs two approvers and is reported within 24 hours
  Given a declared security incident affecting tenant "Gamma LLP"
  When PLT_SUPER_ADMIN requests break-glass read access with a justification
  Then access starts only after PLT_SECURITY_OFFICER and a second staff approver approve at AAL3
  And Gamma LLP's owner receives a report of screens and records viewed within 24 hours

@P02-AT-11 @NN-17
Scenario: Group-umbrella admin does not inherit child access
  Given "Holdco Group" (GROUP) with child tenants "Sub A" and "Sub B"
  And user "Raj" is ORG_ADMIN of the umbrella only
  When Raj requests any record of Sub A
  Then the response is 404
  And Raj sees Sub A only as an aggregate count on the group dashboard

@P02-AT-12 @NN-17
Scenario: Infrabyx staff group grant expires locally
  Given an Equator support engineer receives a group grant to LawDocs role OPS_SUPPORT_AGENT with valid_to 30 Nov 2026
  When the Operations Hub is unavailable on 1 Dec 2026
  Then LawDocs ends the engineer's LawDocs staff sessions within 60 seconds of valid_to
  And the grant never conferred access to any customer tenant's data

@P02-AT-13 @NN-23
Scenario: Consumer Help case manager cannot also serve lender clients
  Given "Pooja" holds OPS_CONSUMER_CASE_MANAGER
  When a lead proposes a delivery grant for Pooja in a tenant flagged as a group lender or insurer client
  Then the proposal is blocked by the ethical-wall SoD rule

@P02-AT-14 @NN-43
Scenario: Agents cannot approve
  Given the Vidhi Contracts agent prepared an NDA under sponsor "Neha"
  When the route would include the agent as a checker through a misconfigured position
  Then the engine refuses with "LD-WF-020"
  And Neha cannot check it either when "wf.sod.agent_sponsor_cannot_check" is true

@P02-AT-15
Scenario: Custom role cannot exceed its base ceiling
  Given an admin builds "Contract Manager" on base ORG_LEGAL_MAKER
  When they add the capability "clm.agreement.approve"
  Then the builder blocks it with "LD-IAM-120" and explains the ceiling

@P02-AT-16
Scenario: Delegation inherits exclusions
  Given checker "Rahul" delegates approvals to "Priya" while away
  And Priya made agreement LD-AGR-2026-000200
  When that agreement reaches Rahul's step
  Then it routes past Priya to the escalation holder

@P02-AT-17
Scenario: Position-based approver survives a personnel change
  Given DoA step "Head – Legal" held by "Amit"
  When "Sara" becomes holder of the position and reaches L2
  Then new requests route to Sara without any DoA change, after the privileged-role approval

@P02-AT-18 @NN-02
Scenario: Super admin's master-data change is client-approved and visible
  Given RM "Vikram" raises a registered-office change for "Beta Finance Ltd" with the client's request letter
  When owner Meera approves in-app and a staff checker approves
  Then the change applies as a Correction Entry and is listed under "Changes made by LawDocs"

@P02-AT-19
Scenario: Access review auto-revokes unreviewed outsider grants
  Given a monthly review includes an engagement grant for advocate "Rao"
  When the reviewer does not decide by close
  Then the grant is revoked, Rao is notified, and the evidence pack records "auto-revoked: not reviewed"

@P02-AT-20 @NN-33
Scenario: No surveillance data exists
  Given the people and workload screens
  Then they show sign-in dates, assigned counts and SLA metrics only
  And the schema contains no keystroke, screenshot, webcam or idle-time tables

@P02-AT-21 @NN-01
Scenario: Context switch changes the data wall
  Given "Ananya" is IND_OWNER of her Personal workspace and ORG_LEGAL_MAKER at "Alpha Pvt Ltd"
  When she switches from Alpha to Personal
  Then Alpha records are no longer returned by any list or search
  And the header reads "Personal — Ananya"

@P02-AT-22 @NN-28
Scenario: Organisation tree is usable by keyboard and screen reader
  Given SCR-P02-02 with 40 departments
  When a screen-reader user expands, moves and renames a department using only the keyboard
  Then every action is announced and the move is possible through the form alternative

@P02-AT-23
Scenario: Role-based home meets click budgets
  Given ORG_CHECKER "Rahul" with 6 pending approvals
  When he opens the app
  Then "Review next" opens the first item in one click and approval completes in a second click plus step-up where required

@P02-AT-24 @NN-11
Scenario: Access records are exportable
  Given a company tenant export
  Then "01 Company Profile/People and Access/Access Register.xlsx", "Approvals Register.xlsx" and "Outsider Access Log.csv" are present with readable names instead of IDs
```

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] `org` model with templates, restructures (batch + undo), positions; directors/KMP linked to the kernel or LDC.
- [ ] Workspace types and the context switcher across web and mobile; notifications labelled by context.
- [ ] Role catalogue seeded; custom-role builder; position-based grants; Cerbos policies with generated tests and query plans; Semgrep rule for `@Authorize`.
- [ ] Maker-checker engine with the Appendix D catalogue, LOCKED NN-18 set, digest binding, inbox, solo-owner rule; DoA tables, simulator and gap check.
- [ ] SoD engine (person-level), delegation, away routing, leaver handling.
- [ ] Grant model and enforcement for all grant types; transparency log writes; break-glass with dual approval; group-grant intake with local expiry.
- [ ] Access-review campaigns with evidence packs; drift scans.
- [ ] Role-based homes and navigation meeting §4L budgets in moderated tests (8 personas × 3 participants).
- [ ] NN tests in the header ACTIVE; settings, help keys, error codes, events, export-map entries registered.

**Demo script.** Ananya switches between Personal and Alpha; Neha submits an ₹18 lakh agreement routed CLO → CFO with an explanation; an edit invalidates approval; Kavita tightens external sharing without LawDocs; Vikram's delivery grant approved, used, revoked within 60 seconds; break-glass dual approval and the client report; an umbrella admin denied child data; a custom role blocked at its ceiling; access review auto-revokes an engagement grant; master-data change approved by the client in one tap.

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P02-01 | Confirm the solo-owner interpretation of NN-18 for one-person company tenants (cooling-off + notifications) | Pack lead / [OWNER] |
| OI-P02-02 | Professional record-keeping vs client data ownership in firm workspaces | [COUNSEL] |
| OI-P02-03 | Related-party and other board-approval triggers for DoA flags (Companies Act s.188 thresholds and rules) | P13 / [COUNSEL] |
| OI-P02-04 | Operations Hub additions: group-grant SCIM attributes for LawDocs roles; `AccessReviewCompleted` for LawDocs scope (Appendix X) | Integration Spec owner |
| OI-P02-05 | Default DoA rows for regulated finance-company tenants aligned with LDC rule packs | P13 / LDC owner |
| OI-P02-06 | Seat classes by role for pricing (FULL/LIGHT/FREE_GUEST) | P17 / [OWNER] |
