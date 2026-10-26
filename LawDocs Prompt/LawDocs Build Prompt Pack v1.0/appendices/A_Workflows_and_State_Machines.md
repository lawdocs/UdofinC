# Appendix A — Workflows and State Machines (binding)

> LawDocs Build Prompt Pack v1.0 · 25 October 2026 · Compiled by X1 from §5 (and lifecycle FRs) of phases P00–P23 · Owner of the engine: P03 (`wf`, `packages/workflow`); owner of each machine: the phase cited in its header. Every module that stores a lifecycle uses the canonical machine defined here. A phase may add tenant-configurable **labels** (P03 `cfg.status_sets` mapped to canonical states) and **sub-states**, but may not add a transition the canonical graph forbids, remove a guard marked **(L)**, or pause a legal clock. Where a phase file and this appendix differ, this appendix records a **Resolution** and the phase is corrected at the next integration; until then the Resolution governs (precedence per master §18: master → `02` decisions → this appendix for lifecycles → owning phase for columns).

---

## A.0 Conventions

### A.0.1 Notation

**Scope:** 63 numbered machine sections (A.1–A.63). A section may group closely related machines that share an owner phase (for example A.4, A.10, A.36, A.47, A.58, A.60, A.61, A.62); §A.64–§A.66 are cross-machine invariants, event gaps and the resolutions register, not machines.

Each machine gives: **Owner** (phase §, table, ID prefix, Temporal workflow) · **States** (terminal states in **bold**) · a transition table *From · Event/trigger · Actor · Guard · To · Side effects and events* · **Timers/SLA** · **NN enforced** · optional **Resolution**. `*` means any non-terminal state. Event names omit the `in.lawdocs.` prefix and `.v1` suffix (Appendix B §B.4 is the event register). "Ledger" means an audit-ledger row written in the same database transaction as the state change (NN-45).

### A.0.2 Engine

- Machines are explicit transition tables in `packages/workflow` (TypeScript), persisted as `state` + `state_version` (optimistic lock) with one `state_history` row per transition: actor, `on_behalf_of` (delegation or delivery grant), reason code, from, to, guard results, change-batch id, correlation id.
- A transition is accepted only through the owning module's API, which re-evaluates every guard server-side; hiding a button is never a control.
- Long-running timers and multi-step processes run as Temporal workflows named in each section; short timers use BullMQ. Timer callbacks re-check guards before transitioning.
- Tenant labels: `cfg.status_defs.canonical_state` maps each tenant status code to exactly one canonical state; reports, exports (Appendix K `status_canonical`) and NN tests read the canonical state.
- `overdue`, `at_risk` and `stale` are **derived flags**, never stored states.

### A.0.3 Universal guards (L)

| Guard | Rule | NN |
|---|---|---|
| G-TEN | Actor and object share `tenant_id` (and permitted `legal_entity_id`); cross-tenant transitions are impossible except through `int` contracts | NN-01, NN-24 |
| G-AUTH | Actor holds the Cerbos permission for the transition in the object's scope (entity, department, confidentiality class, grant) — Appendix D | NN-01 |
| G-SOD | Actor of a check/approve transition ≠ actor of the make/submit transition on the same object version, at person level across realms; delegates inherit the delegator's exclusion; a delegated maker (`ORG_DELEGATED_MAKER`) is never a checker | NN-17, NN-18 |
| G-STEPUP | Approve, sign, send externally, publish, waive, reveal, export of a tenant, break-glass and release of a kill switch require AAL2 step-up ≤ 10 minutes (AAL3 where the machine says so) | NN-18 |
| G-HUMAN | Irreversible external actions (send, file, submit, sign, pay, share outside the tenant, call, accept, withdraw, delete) need a per-action confirmation by an authorised human; an itemised, bounded send-plan confirmed once satisfies this (X-04) | NN-13, NN-34 |
| G-AGENT | `AGT_*` principals may only create drafts and proposals and perform reversible internal actions within their autonomy envelope; any approve/check/sign/pay/waive/send transition by an agent token is refused (`LD-AGT-007`, `LD-WF-020`) | NN-43 |
| G-HIST | No transition deletes or edits history; corrections use Correction Entries (A.1) | NN-02 |
| G-IDEM | A transition that causes an external side effect carries an idempotency key and is reconciled | NN-46 |
| G-CLOCK | Legal clocks (statutory, court, limitation, regulator) never pause and never move later because of a workflow transition; only a rule-set change or a recorded order/extension changes them | — |
| G-FORM | No document, agreement or deliverable reaches an executed/complete state until every required formality is recorded or waived with reason by an authorised human | NN-40 |
| G-ELIG | Instruments excluded by the IT Act First Schedule never enter an eSign state (Appendix F governs; X-02) | NN-07 |
| G-STAMP | A chargeable instrument cannot enter a signing state until the stamp instrument is `LOCKED_TO_DOCUMENT` | NN-08 |
| G-WALL | Consumer Help objects transition only for actors inside the Consumer Help wall; no cross-brand side effect | NN-23 |
| G-FLAG | A transition that depends on a `[VERIFY]` fact is available only when its flag is ON (A.17) | NN-38 |
| G-KILL | No transition through a killed agent, stream, vendor adapter, vertical or channel; queued work pauses | NN-39 |
| G-BATCH | Bulk or imported transitions belong to a change batch with an undo window; the batch id is on every `state_history` row | NN-12 |

### A.0.4 Clocks and SLAs

A clock is `{kind (LEGAL | CONTRACTUAL | INTERNAL_SLA | CHASE), source, starts_at, due_at, pausable, paused_intervals, rule_version, verification (VERIFIED | UNVERIFIED), owner, warn_offsets[], ladder_id}` (P03 `wf.item_clocks`; P11 `lit.clocks` for legal clocks). Only `INTERNAL_SLA` and `CHASE` clocks may pause, and only for reasons the policy lists. UNVERIFIED legal clocks behave as advisory: they warn and escalate but do not block closure without an `ORG_CLO` acknowledgement (P11 §5.5). Business calendars (`wf.business_calendars`) are per State; "BD" means business day in the object's calendar.

### A.0.5 Events

Every transition writes the ledger. A machine emits the specific events listed in its table; there is no generic `StateChanged` event except the three P19 defines (`int.ConnectorInstanceStateChanged`, `int.EcosystemLinkStateChanged`, `int.SorSwitchStateChanged`). Cross-product events are published only by `int` after mapping (Appendix B §B.4.4). Payloads carry IDs, codes, hashes and dates only (NN-32).

---

## Part I — Platform, identity and access

### A.1 Correction Entry (P00 §5.1; configuration variant P03 §5.7; master-data variant P18 §5.3)

**Owner:** P00 · `core.correction_entries` (`cor_`) · `CorrectionEscalation` (hourly).
**States:** `DRAFT`, `SUBMITTED`, `APPROVED`, `CLIENT_APPROVAL_PENDING`, `APPLIED`, **`REJECTED`**, **`WITHDRAWN`**, **`REVERSED`** (by a new entry), `APPLIED_EMERGENCY`, **`RATIFIED`**, **`AUTO_REVERTED`**.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create | Requester (tenant admin, `OPS_RM`, platform staff) | Target record and field class resolvable | DRAFT | — |
| DRAFT | submit | Requester | Justification ≥ 50 chars; documents attached when the reason requires (`LD-CORE-011/012`) | SUBMITTED | `core.CorrectionSubmitted`; escalation after 3 BD |
| DRAFT / SUBMITTED | withdraw | Requester | — | **WITHDRAWN** | Ledger |
| SUBMITTED | approve | Checker | G-SOD (`LD-CORE-010`); AAL3 for platform corrections | APPROVED | — |
| SUBMITTED | reject | Checker | Reason | **REJECTED** | Ledger |
| APPROVED | request_client_ack | System | `tenant_ack_mode = PRIOR`, or target is a "crucial detail" (P03 §5.7) or class-A master data (P18 §5.3) | CLIENT_APPROVAL_PENDING | Tenant owner/admin task; reminders 24/72 h |
| CLIENT_APPROVAL_PENDING | client_approve / timeout | `ORG_OWNER` (or two `ORG_ADMIN`) / system | Step-up; on timeout (5 BD) the platform checker re-confirms and the tenant is told it proceeded with its objection attached | APPROVED→APPLIED | — |
| APPROVED | apply | System | Target not under legal hold where kind = `DOCUMENT_VERSION` (`LD-CORE-013`) | APPLIED | New target version + history + ledger with `correction_id` in one transaction; `core.CorrectionApplied`; tenant notification |
| APPLIED | reverse | Any authorised requester | A new Correction Entry referencing this one | **REVERSED** | `core.CorrectionReversed` |
| — | emergency_apply | `PLT_SUPER_ADMIN` + `PLT_SECURITY_OFFICER` | Security or legal emergency; reason | APPLIED_EMERGENCY | Tenant notified ≤ 24 h |
| APPLIED_EMERGENCY | ratify / timer 24 h | Tenant owner / system | — | **RATIFIED** / **AUTO_REVERTED** | Ledger |

**NN:** NN-02, NN-18, NN-45. **Resolution R-A-01:** P03 §5.7 (`REQUESTED → PLATFORM_APPROVED → CLIENT_APPROVAL_PENDING → APPLIED → TENANT_NOTIFIED`) is this machine with `target_kind = CONFIGURATION`; `TENANT_NOTIFIED` is a side effect of APPLIED, not a state. P18 §5.3 (A.56) wraps this machine for master data. P03's event name `core.CorrectionEntryApplied` is replaced by `core.CorrectionApplied` (P03 edited).

### A.2 Tenant provisioning and onboarding invitation (P00 §5.2; P01 §5.9; P19 §5.5)

**Owner:** P00 (provisioning), P01 (activation), P19 (partner batches) · `core.tenants`, `iam.onboarding_invitations` (`onb_`), `int.onboarding_invitations` · `TenantProvisionWorkflow` (compensating), `PartnerBatchWorkflow`.

Provisioning: `REQUESTED → RECORDS_CREATED → KEYS_READY → STORAGE_PREFIXES_READY → SEARCH_ALIAS_READY → SETTINGS_DEFAULTED → READY`; READY sets tenant status `TRIAL`, `ACTIVE` or `PENDING_CONFIRMATION` (partner/OH-originated). Each step compensates on failure; idempotent on `(created_via, external_request_id)`. Event `core.TenantProvisioned`; OH-originated requests are acknowledged by `int` (`PUT /v1/provisioning-requests/{id}`).

Invitation (canonical, merging P01 §5.9 and P19 §5.5):

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create | OH provisioning, partner batch row, single invite | consentref or legal basis present (`LD-KYC-080`); CIN/GSTIN not already a tenant (else `ALREADY_CUSTOMER`, no invite) | CREATED | Pre-fill snapshot (unconfirmed) |
| CREATED | send | System | One email per row; SMS only with a DLT template | SENT | `int.OnboardingInvitationSent` |
| SENT | bounce | Provider | — | **BOUNCED** | Partner sees status only |
| SENT | open | Invitee | Token valid | OPENED | — |
| OPENED | verify_identity | Invitee | OTP; signatory verified (P01) | IDENTITY_VERIFIED | — |
| IDENTITY_VERIFIED | confirm_kyb | Invitee | Fields confirmed | KYB_CONFIRMED | — |
| KYB_CONFIRMED | accept_terms | Invitee | Terms and DPA accepted | TERMS_ACCEPTED | — |
| TERMS_ACCEPTED | activate | System | Tenant READY | **ACTIVATED** | Tenant + consent artefact; `iam.OnboardingInvitationActivated`; `TenantRegistered` to OH (Appendix Y §Y.7.7); partner webhook `int.OnboardingInvitationAccepted` |
| * | decline / timer 30 d | Invitee / system | — | **DECLINED** / **EXPIRED** | Snapshot deleted; contact erased 90 d later |

**Resolution R-A-02:** P01 §5.9 (`INVITED → OPENED → ACTIVATED`) is the short form; `IDENTITY_VERIFIED`, `KYB_CONFIRMED` and `TERMS_ACCEPTED` are canonical intermediate states. `iam.onboarding_invitations` is the single record; `int.onboarding_invitations` holds the partner-batch row and references the `onb_` id. **NN:** NN-19, NN-24, NN-26.

### A.3 Account and membership (P01 §5.1)

**Owner:** P01 · `iam.users` (`usr_`), `iam.memberships` (`mbr_`).
Account: `PENDING_OTP → ACTIVE | ABANDONED (24 h)`; `ACTIVE → LOCKED (abuse) → ACTIVE (cool-off or recovery)`; `ACTIVE → SUSPENDED (platform, reason) → ACTIVE`; `ACTIVE → CLOSING (user) → CLOSED (30-day grace; export offered; legal holds respected)`. Activation creates the PERSONAL tenant and emits `iam.UserRegistered`; CLOSED triggers erasure per retention schedule while the ledger keeps pseudonymous events.
Membership: `INVITED → ACTIVE → SUSPENDED ⇄ ACTIVE → ENDED`; ending a membership revokes sessions in that tenant ≤ 60 s (`iam.MembershipChanged`). **Guards:** login methods only per NN-03 (never Aadhaar); LOCKED notifies every known contact. **NN:** NN-03, NN-11, NN-26.

### A.4 Identity verification, KYB, signatory authority (P01 §5.2–§5.4)

**Owner:** P01 · `kyc.verifications` (`kyc_`), `kyc.kyb_cases`, `kyc.signatory_authorities`.

| Machine | States and transitions | Guards / timers | Events |
|---|---|---|---|
| Verification run | `REQUESTED (purpose, notice, consent) → IN_PROGRESS → SUCCEEDED | FAILED | NEEDS_REVIEW → REVIEWED_OK | REVIEWED_REJECTED`; `SUCCEEDED → REVOKED (user) | EXPIRED (validity)` | Method flag ON (`LD-KYC-001`); provider responses hashed, never logged; no Aadhaar number, OTP or e-KYC XML stored (NN-04) | `kyc.VerificationCompleted`, `kyc.VerificationRevoked`, `kyc.IdentityLevelChanged` |
| KYB case | `DRAFT → DISCOVERED → CONFIRMED_BY_CUSTOMER → SIGNATORY_PENDING → UNDER_REVIEW → VERIFIED_AUTO | VERIFIED_REVIEWED | REJECTED | NEEDS_INFO`; `VERIFIED_* → REVERIFY_DUE` (monthly refresh finds strike-off, GST cancellation, director cessation) `→ UNDER_REVIEW` | Reviewer maker ≠ checker; review SLA 8 working hours; lookups only via licensed vendors (NN-05) | `kyc.KybCaseVerified`, `kyc.KybStatusChanged` |
| Signatory authority | `PROPOSED → EVIDENCE_SUBMITTED → VERIFIED → ACTIVE → EXPIRED | REVOKED | SUPERSEDED` | Only ACTIVE authorities let a person sign as the entity (`LD-KYC-040/041`); revocation by owner/admin or board-resolution withdrawal; P02 DoA reads limits | `kyc.SignatoryAuthorityChanged` |

### A.5 Professional credential and professional onboarding (P01 §5.5; P16 FR-P16-24)

**Owner:** P01 (credential), P16 (marketplace onboarding) · `kyc.professional_credentials` (`pcr_`), `mkp.professionals` (`pro_`).
Credential: `DRAFT → SUBMITTED → UNDER_REVIEW (OH9 or LOCAL desk) → VERIFIED → REVERIFY_DUE (12 months) → UNDER_REVIEW`; `VERIFIED → EXPIRED | SUSPENDED (disciplinary order, lapsed COP) → VERIFIED (reinstated) | WITHDRAWN`; `UNDER_REVIEW → REJECTED` (reasons; resubmission).
Onboarding: `INVITED | APPLIED → PROFILE_SUBMITTED → KYC_VERIFIED → CREDENTIALS_VERIFIED → DUE_DILIGENCE → AGREEMENT_SIGNED (eSigned, P08) → ROUTE_LINKED (M2 only) → ACTIVE ⇄ SUSPENDED → REMOVED`; side states `RETURNED` (30-day resubmission), `WITHDRAWN`. Maker `OPS_ONBOARDING`; checker for ACTIVE `PLT_LEGAL_REVIEWER` (G-SOD).
**Resolution R-A-03:** a professional can be ACTIVE in the marketplace only while the credential is VERIFIED; credential SUSPENDED/EXPIRED forces onboarding SUSPENDED (`mkp.ProfessionalSuspended`) and blocks new assignments, reviews and certification steps (`LD-KYC-050`, `LD-BSV-007`). **NN:** NN-21, NN-41.

### A.6 Guest invitation (P01 §5.6)

`CREATED → SENT → OPENED → OTP_VERIFIED → COMPLETED | DECLINED ("not me" or decline) | EXPIRED | REVOKED (initiator)`; `COMPLETED → UPGRADED` when the guest creates an account (`iam.GuestUpgraded`). Counterparties receive at most one LawDocs-originated invitation plus reminders they have not opted out of; no automated calls until they opt in (NN-34). The guest sees only shared versions/channels (NN-37).

### A.7 Consent artefact (P01 §5.8)

**Owner:** P01 · `kyc.consents` (`cns_`). `GIVEN → WITHDRAWN | EXPIRED | SUPERSEDED (new notice version accepted)`. Withdrawal emits `kyc.ConsentWithdrawn` and, via `int`, `privacy.ConsentWithdrawn` to every recipient of that `consentref` within the 1-hour SLO (`ConsentPropagation`). Any machine whose guard cites a consent re-checks it at transition time (`LD-KYC-070`, `LD-LIT-020`, `LD-CHP-011`, `LD-INT-031`). **NN:** NN-24, NN-26.

### A.8 Nominee designation and release (P01 §5.7; P04 §5.4)

**Owner:** P01 (designation, identity, evidence review); P04 (vault-scope claim and access) · `kyc.nominations` (`nom_`, canonical), `dms.nominees` (vault scope view keyed by the same `nom_`), `dms.nominee_claims` · `NomineeReleaseWorkflow`, `NomineeInactivityWorkflow`.
Designation: `DESIGNATED (owner L2, AAL2) → ACCEPTED (nominee OTP) → REVOKED (owner) | ENDED (account closure)`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| ACCEPTED designation | claim (death/incapacity or inactivity trigger) | Nominee | Nominee identity L2; evidence uploaded to `ld_sealed` | CLAIMED | `dms.NomineeClaimRaised`; review task |
| CLAIMED | verify_identity | System | Identity matches designation | IDENTITY_VERIFIED | — |
| IDENTITY_VERIFIED | review_evidence | `OPS_ONBOARDING` maker → checker `PLT_DPO` or `OPS_DELIVERY_LEAD` (AAL3) | G-SOD; required only for death/incapacity triggers | EVIDENCE_VERIFIED | Owner notified on every contact point |
| EVIDENCE_VERIFIED / IDENTITY_VERIFIED (inactivity) | start_wait | System | — | WAITING | Timer `iam.nominee.release_waiting_days` |
| WAITING | owner sign-in or "I am fine" | Owner | — | **CANCELLED_BY_OWNER** | Alert; offer to review nominees and security (`LD-KYC-060`) |
| WAITING | object | Co-nominee or family with standing | Reason and evidence | **OBJECTED** | Human review; no release |
| * | reject | Checker | Reason | **REJECTED** | — |
| WAITING | timer elapses | System | No cancellation | RELEASED | Read-only grant `grt_` type `NOMINEE` for scoped items; every access logged; `kyc.NomineeReleased`, `dms.NomineeAccessReleased` |
| RELEASED | access period ends / nominee closes | System / nominee | — | **EXPIRED** | Grant revoked |

**Resolution R-A-04:** P01 `RELEASE_REQUESTED` = canonical `CLAIMED`; P01 `CLOSED` = canonical `EXPIRED`; P04 `EVIDENCE_REVIEW` is the activity between IDENTITY_VERIFIED and EVIDENCE_VERIFIED. One `nom_` record; `dms.nominees` is a projection. Wording on succession remains OI-P04-02 [COUNSEL]. **NN:** NN-02, NN-17, NN-26.

### A.9 Grant — role, guest, professional, nominee and delivery grants (P02 §5.1; P18 §5.1)

**Owner:** P02 (all grant types; register `iam.grants`, `grt_`), P18 (delivery extension `sdc.delivery_grants`, keyed by the same `grt_`) · `GrantExpiryEnforcer`, `GrantExpiryWorkflow`.
**States:** `PROPOSED`, `APPROVED` (transient; only when `valid_from` is in the future), `ACTIVE`, `RENEWAL_PENDING` (P18 label "Expiring"), `SUSPENDED`, **`REVOKED`**, **`EXPIRED`**, **`DECLINED`** (P18 "Denied"), **`WITHDRAWN`**.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | propose | `OPS_RM`/`OPS_DELIVERY_LEAD`, engagement acceptance, owner invitation | Delivery: grantee role `ORG_DELEGATED_MAKER`, checker bound (`LD-SDC-005`), duration ≤ cap (`LD-SDC-004`), conflict check clear (`LD-SDC-011`), no Consumer Help staff on lender/insurer clients (`LD-SDC-020`) | PROPOSED | Mandatory client notification; `iam.GrantProposed` / `sdc.DeliveryGrantProposed` |
| PROPOSED | approve | Client approver (`ORG_OWNER`/`ORG_ADMIN`) | Approver ≠ grantee; AAL2; SoD; grantee identity level ≥ role minimum (`LD-IAM-104`); only the client may approve (`LD-SDC-008`) | ACTIVE (or APPROVED until `valid_from`) | `iam.GrantActivated` / `sdc.DeliveryGrantActivated`; transparency-log entry |
| PROPOSED | activate_under_standing | `OPS_DELIVERY_LEAD` | Client-approved standing authorisation in force and within scope (X-20; `LD-SDC-009`) | ACTIVE | Activation notice to client ≤ 1 h |
| PROPOSED | decline / withdraw | Client / proposer | — | **DECLINED** / **WITHDRAWN** | Ledger |
| ACTIVE | T−14 d | System | — | RENEWAL_PENDING | Notices to both sides |
| RENEWAL_PENDING | renew | Client | Fresh approval, never automatic | ACTIVE (new version) | `sdc.DeliveryGrantRenewed` |
| ACTIVE / RENEWAL_PENDING | suspend | Client; lead or security (leaver, security alert, conflict hit, retainer suspended, unattested review) | — | SUSPENDED | Sessions end ≤ 60 s; `sdc.DeliveryGrantSuspended` |
| SUSPENDED | reinstate | Client | Cause cleared | ACTIVE | — |
| ACTIVE / SUSPENDED / RENEWAL_PENDING | revoke | Client; lead; `PLT_SUPER_ADMIN` (emergency) | — | **REVOKED** | Sessions end ≤ 60 s; open items reassigned; credential rotation prompts (A.55); `iam.GrantEnded` / `sdc.DeliveryGrantRevoked` |
| RENEWAL_PENDING | `valid_to` reached | System | — | **EXPIRED** | Same as revoke; `sdc.DeliveryGrantExpired` |

**Break-glass:** separate session kind (`sdc.sessions.kind = BREAK_GLASS`), dual approval (`LD-SDC-012`), reported to the client ≤ 24 h (`sdc.BreakGlassOpened`, `core.BreakGlassStarted/Ended`).
**Resolution R-A-05:** P02 and P18 describe one machine. `iam.grants` is the supertype register for every non-ROLE grant; delivery grants add scope, checker binding and standing-authorisation fields in `sdc.delivery_grants` (1:1 on `grt_`). Delivery grants emit `sdc.DeliveryGrant*` events only; other grant types emit `iam.Grant*`. **NN:** NN-17, NN-18, NN-23.

### A.10 Delegation, group grant, access review (P02 §5.4–§5.6)

| Machine | States | Rules |
|---|---|---|
| Delegation (`iam.delegations`, `dlg_`) | `SCHEDULED → ACTIVE → ENDED (date) | CANCELLED` | Delegate must hold the role on the scope (`LD-IAM-131`); some roles not delegable (`LD-IAM-130`); delegate inherits SoD exclusions; both parties get a summary at ENDED; events `iam.DelegationStarted/Ended` |
| Group grant (staff, OH10 SCIM) | `RECEIVED (membership with valid_to) → ACTIVE → EXPIRED | REVOKED` | LawDocs enforces `valid_to` locally (local expiry wins); quarterly review; usage logged |
| Access review campaign | `SCHEDULED → OPEN → CLOSING (auto-revoke where configured) → COMPLETED (evidence pack) | OVERDUE` | Delivery grantees unattested 14 days after close are SUSPENDED (P18); `iam.AccessReviewCompleted` (counts only to OH as `AccessReviewCompleted`, PLATFORM scope) |

### A.11 Maker-checker approval request (P02 §5.2; CLM approval steps P07 §5.4)

**Owner:** P02 · `wf.approval_requests` (`apr_`), `wf.approval_decisions` · `ApprovalEscalation` (15 min), `ApprovalExpiry` (hourly).
**States:** `DRAFT`, `SUBMITTED`, `IN_REVIEW` (step n), `APPROVED`, `EXECUTING`, **`EXECUTED`**, `EXECUTION_FAILED`, **`REJECTED`**, `RETURNED`, **`EXPIRED`**, **`CANCELLED`**.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| DRAFT | submit | Maker (human or agent proposal confirmed by sponsor) | Action in `wf.mc_actions`; payload digest computed; route resolved from DoA (`LD-WF-030` routes to `ORG_OWNER` when no row matches, never skips) | SUBMITTED | `wf.ApprovalRequested` |
| SUBMITTED / IN_REVIEW | approve step | Route member | G-SOD (`LD-WF-010`, `LD-WF-011`); AAL per policy; digest seen = current digest; not an agent (`LD-WF-020`); step holder exists (`LD-WF-031`) | IN_REVIEW (next step) or APPROVED | `wf.ApprovalDecided` |
| SUBMITTED / IN_REVIEW | reject | Route member | Reason | **REJECTED** | `wf.ApprovalDecided` |
| SUBMITTED / IN_REVIEW | payload or referenced version changes | System | — | RETURNED | All approvals invalidated (`LD-WF-012`); `wf.ApprovalInvalidated` |
| RETURNED | resubmit | Maker | — | SUBMITTED | Digest reset |
| APPROVED | execute | System | Re-validate target | EXECUTING → **EXECUTED** | `wf.ApprovalExecuted` |
| EXECUTING | failure | System | — | EXECUTION_FAILED → (retry) EXECUTING or RETURNED | Alert |
| SUBMITTED / IN_REVIEW | `expires_at` | System | — | **EXPIRED** | `wf.ApprovalExpired`; maker notified (`LD-WF-013`) |
| DRAFT…IN_REVIEW | cancel | Maker or leaver sweep | — | **CANCELLED** | — |

**Locked actions (NN-18):** payments/refunds/credits, access grants, tenant exports, role elevation, critical configuration, master-data changes, template/rule publication, price and stream switches, bulk deletes, agent autonomy raises. A tenant cannot relax them (`LD-WF-014`); solo-approval tenants get a cooling-off (`LD-WF-015`).
**Resolution R-A-06:** P07 `clm.approval_step` (`PENDING → APPROVED | REJECTED | DELEGATED → … | INVALIDATED | ESCALATED`) is a projection of this machine bound to the agreement version hash: each step is a route step of one `apr_`; `INVALIDATED` = request RETURNED; `DELEGATED` = step reassigned under an active delegation. `clm.ApprovalRequested/ApprovalDecided/ApprovalsInvalidated` are domain notifications emitted by `clm` after the corresponding `wf.*` event; the engine is `wf` only (OP-1).

### A.12 Custom role and DoA table publication (P02 §5.3; P13 `lgo.doa_matrix`)

`DRAFT → IN_REVIEW (maker-checker) → PUBLISHED (version n, effective date) → SUPERSEDED`. Custom roles cannot exceed the base-role ceiling or combine conflicting capabilities (`LD-IAM-120/121`). DoA "apply to pending" restarts affected approval requests with notice. P13 `lgo.doa_matrix` versions publish through the same machine and cite the board resolution where the delegation derives from one (`LD-LGO-007` blocks actions above delegation). Events `iam.CustomRolePublished`, `wf.DoaTablePublished`, `lgo.DoaChanged`.

### A.13 Setting change — OPEN and GOVERNED (P03 §5.1–§5.2)

**Owner:** P03 · `cfg.setting_changes`, `cfg.change_requests` · `ConfigActivationWorkflow`.
OPEN keys: validate (type, bounds ∩ plan ∩ brand ∩ platform, child direction, parent lock, contrast/schema; `LD-CFG-001…006`) → write value + change row + ledger in one transaction → `cfg.SettingChanged` → cache invalidation ≤ 60 s → "Saved · Undo".
GOVERNED keys (or tenant `require_approval_keys`):

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| DRAFT | submit | Validators green; citation if required; summary; preview ≤ 24 h old; lead time met | SUBMITTED | `cfg.ConfigChangeRequested`; approval item |
| SUBMITTED | open | Checker eligible, ≠ maker, not delegated from maker (`LD-CFG-020`) | IN_REVIEW | — |
| IN_REVIEW | approve | Step-up ≤ 10 min; all steps met | APPROVED | `cfg.ConfigChangeApproved` |
| IN_REVIEW | reject / return | Reason ≥ 20 chars | **REJECTED** / DRAFT | — |
| APPROVED | schedule | `effective_from` > now | SCHEDULED | Timer |
| APPROVED / SCHEDULED | activate | Re-validation green | **ACTIVE** | Previous version SUPERSEDED; cache bust; `cfg.ConfigChangeActivated` |
| non-terminal | withdraw / expiry | Maker / `expiry_days` | **WITHDRAWN** / **EXPIRED** | Timers cancelled |

Direct PATCH of a GOVERNED key returns `LD-CFG-012`. **NN:** NN-18, NN-29.

### A.14 Rule-set and legal-content version (P03 §5.3; NN-30)

**Owner:** P03 · `rul.rule_set_versions`, `rul.content_versions`.
`DRAFT → IN_REVIEW (golden suite green or mismatches accepted with reason; citations complete; reviewer ≠ maker, LD-RUL-011) → APPROVED (reviewer of record signs) → SCHEDULED → ACTIVE → SUPERSEDED → RETIRED`; `REJECTED`, `WITHDRAWN`; `ACTIVE → EMERGENCY_BLOCKED (protective overlay) → ACTIVE` after review. Events `rul.RuleSetVersionSubmitted`, `…Activated`, `…ReviewDue`, `…Retired`, `…EmergencyBlocked`, `rul.ContentVersionPublished`. Activation never needs a code release and a release never changes published content (NN-30). Machines that pin a rule version (signing eligibility, clocks, duty quotes) keep the pinned version; recomputation creates a new clock/quote version (G-CLOCK).

### A.15 Item — open, interim and waiting (P03 §5.4) and task

**Owner:** P03 · `wf.items` (`itm_`), `wf.item_waits`, `wf.item_clocks`, `wf.chase_log` · `ItemClockWorkflow`, `ChasePolicyWorkflow`, `EscalationJob`.
**Canonical states:** `OPEN`, `IN_PROGRESS`, `WAITING`, `INTERIM`, `ON_HOLD`, **`RESOLVED`**, **`WAIVED`**, **`CANCELLED`**, **`SUPERSEDED`**.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create | User, rule, agent, integration, import | Type allowed for parent; owner resolvable | OPEN | Clocks started; `wf.ItemOpened` |
| OPEN | start | Owner | — | IN_PROGRESS | — |
| OPEN / IN_PROGRESS / INTERIM | set_waiting | Owner; agent proposes, owner confirms | Party type allowed; `expected_by` set | WAITING | Chase policy scheduled; internal SLA paused if the type allows; `wf.ItemWaitingStarted` |
| WAITING | response / resume / matching event | System, owner | — | IN_PROGRESS | Chases stopped; `wf.ItemWaitingEnded` |
| WAITING | chase_due | System | `CONFIRM_EACH` → ready-to-send chaser for the owner; `PRE_APPROVED_SERIES` (≤ 5, `LD-WF-114`) → send; never to courts, registries or regulators (`LD-WF-112`; NN-05) | WAITING | `chase_count += 1`; `wf.ItemChased` |
| WAITING | `expected_by` + grace | System | — | WAITING | Escalate L1 → L2; `wf.ItemEscalated` |
| any open | `legal_due − warning_days` | System | Any LEGAL clock | (unchanged) | Escalate L2/L3; banner; `wf.LegalClockWarning` |
| IN_PROGRESS | record_interim | Owner | Interim evidence if required | INTERIM | `wf.ItemInterimRecorded` |
| any open | hold | Authorised user | Reason code | ON_HOLD | Internal SLA paused; legal clocks continue |
| any open | resolve | Owner (or checker where the type requires) | Evidence attached; maker ≠ checker where configured | **RESOLVED** | Parent gates re-evaluated; `wf.ItemResolved` |
| any open | waive | `ORG_CLO` / `ORG_APPROVER` / `IND_OWNER` | Reason from LOCKED list; not an agent (`LD-WF-121`) | **WAIVED** | Formalities gate re-check (`LD-WF-120`); `wf.ItemWaived` |
| any open | cancel / supersede | Owner, system | Parent cancelled or replacement linked | **CANCELLED** / **SUPERSEDED** | — |

**Uses:** formality items (A.33), legal-request waiting (A.46), order directions (A.41), checklist items (A.49), consumer-case waits (A.50), delivery inbox (P18).
**Resolution R-A-07 (X-09):** `lgo.waiting_items` is a read view over `wf.items` + `wf.item_waits` (P13 edited). **Resolution R-A-08 (tasks):** conventions §5 register `tsk_` and P11/P18/Appendix I use "tasks", but P03 §7.2 lists no task table. Tasks are `wf.tasks` (`tsk_`), owned by P03: `OPEN → IN_PROGRESS → DONE | CANCELLED`, with owner, due date, checklist, dependency and evidence rule; a task that waits on someone opens a linked `itm_` in WAITING rather than adding a waiting state. P03 §7.2 now lists `wf.tasks` and §7.4 emits `wf.TaskCreated`, `wf.TaskAssigned` (Appendix I §I.7) and `wf.TaskCompleted` (F1); task error codes `LD-WF-130`/`131`.

### A.16 Configuration template application and import (P03 §5.6)

`SELECTED → DIFF_PREVIEWED → SECTIONS_CHOSEN → APPLYING (job) → APPLIED (batch id; undo window open) → UNDONE | FINALISED (window closed)`; GOVERNED sections branch to A.13; LOCKED or out-of-bound rows rejected per row (`LD-CFG-070`). Events `cfg.ConfigTemplateApplied`, `cfg.ConfigBundleImported`. G-BATCH.

### A.17 Feature flag with verification gate, and kill switch (P00 §5.6; P03 §5.5; P09; P19)

**Owner:** P03 (`cfg.flags`, `cfg.kill_switches`); P00 creates the heads · `KillSwitchProbeJob`, `KillSwitchPropagation`.
Flag: `OFF → ON_PENDING_APPROVAL (verification row VERIFIED + approver evidence) → ON` (maker-checker); a flag tied to an open verification cannot turn ON (`LD-CORE-016`). `ON → OFF` immediately by authorised roles.
Kill switch: `RELEASED → ENGAGED (one authorised person, reason; propagation probe ≤ 60 s) → RELEASE_REQUESTED (cause resolved, evidence) → RELEASED (second person ≠ requester)`. Scopes: `AI_AGENT`, `REVENUE_STREAM`, `VENDOR_ADAPTER`, `CONSUMER_VERTICAL`, `OUTBOUND_CHANNEL`, `CONNECTOR`, `CREDENTIAL_REVEAL`. Engaged switches block transitions (`LD-CORE-017`, `LD-AGT-009`, `LD-INT-080`, `LD-CVL-010`).
**Resolution R-A-09:** one registry and one event pair, `cfg.KillSwitchEngaged` / `cfg.KillSwitchReleased`, with `scope` and `target`. `core.KillSwitchChanged` (P00), `agt.KillSwitchActivated/Released` (P09) and `int.KillSwitchToggled` (P19) are aliases; `agt.kill_switches` is the agent-scope view. Flag events: `cfg.FlagChanged` canonical; `core.FeatureFlagChanged` (P00) alias. **NN:** NN-38, NN-39.

---

## Part II — Documents, intelligence and portability

### A.18 Document and version (P04 §5.1; ingest P00 FR-P00-54)

**Owner:** P04 · `dms.documents` (`doc_`), `dms.versions` (`ver_`) · `DocIngestWorkflow`, `RetentionSweepWorkflow`.
**States:** `PROCESSING`, `QUARANTINED`, `ACTIVE`, `ARCHIVED`, `DELETED` (recycle bin), **`PURGED`**, **`REJECTED`**. Orthogonal flags: `is_executed`, `on_legal_hold`, `health_status`, `superseded`; execution status is A.33.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | upload received | User, agent, integration, mobile (A.61) | Upload intent; checksum header | PROCESSING | `dms.DocumentUploaded` |
| PROCESSING | pipeline passes | System | MIME allow-list; two-engine scan; SHA-256 matches (`LD-DMS-032`); Aadhaar masked before any derived text is stored (NN-04; X-14 keeps only masked rendition + pre-mask hash) | ACTIVE | Original under Object Lock (NN-09); `dms.DocumentIngested`; `dms.AadhaarMaskedAtIngest` when masked |
| PROCESSING | malware / unsafe archive | System | — | QUARANTINED | Bytes in quarantine bucket, never served (`LD-DMS-002`, `-005`) |
| PROCESSING | type not allowed / encrypted | System | — | **REJECTED** | Hash kept, bytes destroyed (`LD-DMS-001`, `-004`); `dms.DocumentRejected` |
| QUARANTINED | false positive | `PLT_SECURITY_OFFICER` | Second-engine re-scan clean | ACTIVE | Ledger |
| QUARANTINED | 7 days | System | — | **REJECTED** | — |
| ACTIVE | new version / metadata | Owner, editors | Check-out lock (`LD-DMS-007`); conflict saved as new version (`LD-DMS-008`) | ACTIVE | `dms.DocumentVersionCreated`, `dms.DocumentMetadataChanged` |
| ACTIVE | archive | Owner | — | ARCHIVED | `dms.DocumentArchived` |
| ARCHIVED | unarchive | Owner | — | ACTIVE | — |
| ACTIVE / ARCHIVED | delete | Owner | No legal hold (`LD-DMS-009`); retention floor passed (`LD-DMS-010`); bulk > threshold → maker-checker (`LD-DMS-022`) | DELETED | `dms.DocumentDeleted` |
| DELETED | restore | Owner | Within `dms.recycle.retention_days` | ACTIVE | `dms.DocumentRestored` |
| DELETED | recycle period ends / disposal approved | System | Hold re-checked at purge; compliance-mode objects only after retain-until | **PURGED** | Crypto-shred; permanent purge record; `dms.DocumentPurged` |

**NN:** NN-02, NN-04, NN-09, NN-11, NN-12 (folders are views over IDs).

### A.19 Share pack (P04 §5.2)

**Owner:** P04 · `dms.shares` (`shr_`) · `ShareLifecycleWorkflow`.
`DRAFT → PENDING_APPROVAL (company, any CONFIDENTIAL_LEGAL item; checker ≠ maker) → ACTIVE`; `DRAFT → ACTIVE` when no approval is needed; `PENDING_APPROVAL → REJECTED`; `ACTIVE → REVOKED | EXPIRED | EXHAUSTED (max opens)`; terminal shares may be cloned. ACTIVE only on a human send (G-HUMAN; agents may prepare DRAFT). Recipient access: OTP (`LD-DMS-013`), watermark, view-only (`LD-DMS-029`). Events `dms.ShareCreated`, `dms.ShareApprovalRequested`, `dms.ShareAccessed`, `dms.ShareRevoked`, `dms.ShareExpired`; to another product only as `documents.DocumentShared` via `int` with consent. **NN:** NN-13, NN-18, NN-37, NN-42.

### A.20 Legal hold (P04 §5.5)

**Owner:** P04 · `dms.legal_holds` (`hld_`) · `LegalHoldReconcileJob` (nightly).
`ACTIVE → RELEASE_REQUESTED → RELEASED` (second approver in company tenants). Placing a hold is immediate (`ORG_CLO`, `IND_OWNER`); S3 legal-hold flags are set by an idempotent job and reconciled nightly (NN-46). A hold blocks A.18 `DELETED→PURGED`, A.23 deletion, A.24 exit deletion and account closure erasure; it does not block access or sharing. Ecosystem `privacy.LegalHoldChanged` is consumed and applied as a hold with source `ECOSYSTEM`. Events `dms.LegalHoldPlaced`, `dms.LegalHoldReleased`.

### A.21 Import job (P20 §5.3 canonical; P04 §5.3; P11 §5.6; P12 imports)

**Owner:** P20 · `xpt.import_jobs` (`imp_`), `xpt.import_files` · `ImportWorkflow`, `ImportUndoWorkflow`.
**States:** `CREATED`, `SCANNING`, `MAPPING`, `CLASSIFYING` (optional), `AWAITING_REVIEW`, `COMMITTING`, `CHECKER_PENDING` (above threshold), `COMMITTED` (undo window open), `ENRICHING` (optional vendor lookups), **`FINALISED`**, **`UNDONE`**, `FAILED` (resumable), **`CANCELLED`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| CREATED | files received | Resumable upload; hashes | SCANNING | Malware scan |
| SCANNING | scan clean | — | MAPPING | Reverse mapping (Appendix K §K.10) |
| MAPPING | classify (optional) | `dix` classification | CLASSIFYING → AWAITING_REVIEW | — |
| AWAITING_REVIEW | commit | Maker; row errors resolved (`LD-LIT-018`, `LD-IPM-015`, `LD-DMS-019`) | COMMITTING, or CHECKER_PENDING if rows > `lit.import.checker_threshold_rows` (100) or tenant rule | Idempotent on (`imp_id`, file SHA-256, target view path) |
| CHECKER_PENDING | approve | G-SOD | COMMITTING | — |
| COMMITTING | done | Crash resumes from last committed file | COMMITTED | Report document; `xpt.ImportCommitted` (+ module `lit.ImportCommitted`, `dms.IntakeJobCommitted`) |
| COMMITTED | enrich | Metered lookups with cost preview | ENRICHING → COMMITTED | — |
| COMMITTED | undo | Within window (`lit.import.undo_hours` 24; else `LD-LIT-019`/`LD-IPM-016`) | **UNDONE** | Created records reversed by Correction Entries; prior values restored; ledger kept; `xpt.ImportUndone` |
| COMMITTED | window closes | — | **FINALISED** | — |
| before COMMITTING | cancel | Requester | **CANCELLED** | Staging purged |
| any | error | — | FAILED → (resume) previous stage | — |

**Resolution R-A-10:** one `imp_` ID space owned by `xpt`; P04 intake (`UPLOADING → EXPANDING → MAPPING_PREVIEW → COMMITTING → COMMITTED | COMMITTED_WITH_EXCEPTIONS | CANCELLED`) and P11/P12 register imports are `xpt.import_jobs` rows with `source_kind` = `DMS_FOLDER`, `LIT_REGISTER`, `IPM_REGISTER`; P04 `EXPANDING` = `SCANNING`, `MAPPING_PREVIEW` = `AWAITING_REVIEW`, `COMMITTED_WITH_EXCEPTIONS` = COMMITTED with exception rows. P03 configuration import (A.16) and P21 DOCX import (A.60) are separate machines. **NN:** NN-02, NN-12, NN-46.

### A.22 Export job (P20 §5.1)

**Owner:** P20 · `xpt.export_jobs` (`exp_`) · `ExportWorkflow` (checkpointed).

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | request | Owner/admin; individual | Scope chosen; step-up | REQUESTED | `xpt.ExportRequested` (+ `portability.ExportRequested` via `int`, counts only) |
| REQUESTED | needs approval | System | Full-tenant or regulated scope (NN-18) | AWAITING_APPROVAL | Approval item |
| AWAITING_APPROVAL | approve | Checker ≠ requester (`LD-XPT-012`) | Step-up | APPROVED | `xpt.ExportApproved` |
| AWAITING_APPROVAL | reject / 72 h | Checker / system | — | **REJECTED** / **EXPIRED** | — |
| REQUESTED (no approval) / APPROVED | start | System | — | SNAPSHOTTING → COLLECTING → RENDERING → PACKAGING → RECONCILING → SIGNING → DELIVERING | Export map per record type; PDF/A gates; control totals; JWS manifest; residency check for BYO target (`LD-XPT-031`) |
| DELIVERING | delivered | System | — | COMPLETED | `xpt.ExportCompleted` |
| COMPLETED | recipient or target verified | System / user | Hashes match | **CONFIRMED** | — |
| any stage | error | System | — | FAILED (resumable) | `xpt.ExportFailed` |
| before SIGNING | cancel | Requester / approver | — | **CANCELLED** | — |

An individual or tenant can always export without staff help; exports are never paywalled (NN-11). Grantees attempting a tenant export get `LD-XPT-015` and appear in the client's access log.

### A.23 Exit and account closure (P20 §5.5; P17 §5.1 EXIT; P01 §5.1 CLOSING)

`EXIT_REQUESTED → APPROVED → EXPORTING (A.22, scope EXIT) → AWAITING_RECEIPT_CONFIRMATION → READ_ONLY (n days; REACTIVATE allowed) → DELETING → DELETION_CERTIFIED → CLOSED`; legal hold or order → `HELD` with listed exceptions. Deletion respects compliance-mode retention (evidence packs, executed instruments) and purges the rest by crypto-shredding; the deletion certificate is filed in the exit package `00 Start Here/`. Events `xpt.ExitRequested`, `xpt.DeletionCertified`. **Resolution R-A-11:** P17 `EXIT → CLOSED` and P01 `CLOSING → CLOSED` are entry points into this machine; billing never blocks read or export during READ_ONLY (FR-P17-31 never-block list).

### A.24 Storage target and mirror increment (P20 §5.2, §5.4)

Storage target (`xpt.storage_targets`, `stg_`): `DRAFT → VERIFYING (describe, verifyResidency, testWrite) → PENDING_APPROVAL (regulated classes; maker-checker) → ACTIVE → DEGRADED (one failed check) → PAUSED (two failures, credential revoked, residency drift, key unavailable) → ACTIVE (re-verified) | DISCONNECTED (credentials deleted; customer copies untouched)`. Events `xpt.StorageTargetConnected/Degraded/Paused`.
Mirror increment: `CHANGE_CAPTURED (outbox) → BATCHED (≤ lag window) → PACKAGED → PUT (idempotent) → VERIFIED (head hashes) → ACKNOWLEDGED`; nightly `RECONCILE → REPAIRED | CONFLICTS_RAISED` (customer-modified files are never overwritten; conflict item opened). Events `xpt.MirrorIncrementDelivered`, `xpt.TargetConflictDetected`. **NN:** NN-12, NN-25, NN-46.

### A.25 Document intelligence (P05 §5.1–§5.5)

| Machine | Owner / table | States and transitions | Guards |
|---|---|---|---|
| DIX job | `dix.jobs` (`dxj_`) | `QUEUED → RUNNING | WAITING_ENGINE | CANCELLED`; `WAITING_ENGINE → RUNNING | FAILED (24 h)`; `RUNNING → NEEDS_INPUT → RUNNING`; `RUNNING → SUCCEEDED | FAILED` | Credits reserved (`LD-DIX-002`); class routing fail-closed to India engines (`LD-DIX-003`; NN-15, NN-25); SUCCEEDED only after the Aadhaar derived-text check; events `dix.DixJobQueued/InputRequested/JobSucceeded/JobFailed` |
| Type copy | `dix.renditions` kind `TYPE_COPY` | `MACHINE_DRAFT → USER_CORRECTED → VERIFIED`; `USER_CORRECTED/VERIFIED → DISPUTED → VERIFIED | SUPERSEDED`; any → SUPERSEDED on regeneration | USER_CORRECTED needs zero unreviewed LOW lines (`LD-DIX-015`); agents cannot move past MACHINE_DRAFT (`LD-DIX-016`; NN-43); disputes need reason; events `dix.TypeCopyGenerated/Corrected/Verified/Disputed` |
| Translation | kind `TRANSLATION` | `MT_DRAFT → BACKTRANSLATION_FLAGGED → MT_DRAFT → REVIEWED` | REVIEWED never becomes certified; locked terms preserved (`LD-DIX-021`); flags reviewed (`LD-DIX-022`); NN-48 |
| Certified translation | `dix.certified_requests` + P16 engagement | `ORDERED → PAID → ASSIGNED → IN_PROGRESS → QA → CERTIFIED → DELIVERED`; side `ON_HOLD`, `CANCELLED` (refund per P16) | Produces a new rendition `TRANSLATION_CERTIFIED`; SLA per step; breach notifies buyer and `OPS_DELIVERY_LEAD` |
| Extraction proposal | `dix.extractions` | `PROPOSED → CONFIRMED | EDITED_AND_CONFIRMED | REJECTED` | Only confirmed values write metadata, reminder facts or `obl_` drafts (NN-13 analogue for internal effects) |

---

## Part III — Drafting, contracts and execution

### A.26 Template version, clause and backlog item (P06 §5.1, §5.4)

**Owner:** P06 · `tpl.template_version`, `tpl.clause_version`, `tpl.playbook_version`, `tpl.backlog_item` · `TemplatePublishWorkflow`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create / clone | Maker (`PLT_CONTENT_EDITOR` / `ORG_LEGAL_MAKER`) | — | DRAFT | — |
| DRAFT | submit | Maker | Lint and golden tests pass (`LD-TPL-005/006/007/016`); mandatory fields and reviewer of record (`LD-TPL-003`) | IN_REVIEW | `tpl.TemplateVersionSubmitted` |
| IN_REVIEW | approve | Checker (`PLT_LEGAL_REVIEWER` / `ORG_CHECKER`) | G-SOD (`LD-TPL-002`); no open `OUTDATED_LAW` backlog item (`LD-TPL-004`); neutrality checklist (`LD-TPL-012`, platform) | APPROVED | `tpl.TemplateVersionApproved` |
| IN_REVIEW | return | Checker | Reason | DRAFT | `tpl.TemplateVersionReturned` |
| APPROVED | `effective_from` | System | — | PUBLISHED | `tpl.TemplateVersionPublished`; P21 page update; draft-holder notices |
| PUBLISHED | deprecate | Checker | Successor published or reason | DEPRECATED | `tpl.TemplateVersionDeprecated` |
| DEPRECATED | retire | Checker | No new starts ≥ 30 days or law repealed | **RETIRED** | `tpl.TemplateRetired`; new drafts refused (`LD-TPL-011`) |

Clause and playbook versions follow the same graph (`tpl.ClauseVersionPublished`, `tpl.PlaybookVersionPublished`); language versions need human review before operative use (`LD-TPL-010`; NN-48).
Backlog item: `OPEN → IN_PROGRESS → FIX_PROPOSED → VERIFIED (PLT_LEGAL_REVIEWER ≠ fixer) → CLOSED`; `WONT_FIX` with reviewer reason; SLA `tpl.backlog.sla_days_outdated_law` (30) and `…_copied` (14); overdue items keep pages `noindex`. Events `tpl.BacklogItemOpened/Closed`. **NN:** NN-18, NN-30.

### A.27 Draft (P06 §5.2)

**Owner:** P06 · `drf.draft` (`drf_`). Lanes are orthogonal: `TEMPLATE` (assembly of vetted content — template automation, not AI advice) and `AI_CUSTOM`.

| State | Meaning | Next | Guard |
|---|---|---|---|
| `IN_PROGRESS` | Interview / editing | COMPLETE (template lane) or AI_UNREVIEWED (AI lane) | All required answers present (`LD-DRF-001` blocks clean export while blanks remain) |
| `COMPLETE` | Template lane ready | REVIEW_REQUESTED, IN_PROGRESS, HANDED_OFF | Accepting an AI suggestion escalates to AI_UNREVIEWED after warning (`LD-DRF-002`; `drf.DraftLaneEscalated`) |
| `AI_UNREVIEWED` | "AI draft — not reviewed by a professional" | REVIEW_REQUESTED, IN_PROGRESS | Individuals: clean export, eSign and "final" sharing blocked (`LD-DRF-003`; NN-14) |
| `REVIEW_REQUESTED` | Paid or company review pending | IN_REVIEW | Payment confirmed (P17) or company reviewer assigned |
| `IN_REVIEW` | Reviewer working; draft locked except comments (`LD-DRF-008`) | REVIEWED, RETURNED | Reviewer holds an active grant (A.9) |
| `RETURNED` | Changes required | IN_PROGRESS | — |
| `REVIEWED` | Review certificate issued; reviewed hash stored | HANDED_OFF, CHANGED_AFTER_REVIEW | — |
| `CHANGED_AFTER_REVIEW` | Edited after review | REVIEW_REQUESTED | AI-custom requires re-review |
| **`HANDED_OFF`** | Moved to P07, P08 or Vault | — | Governing language must be a reviewed version (`LD-DRF-005`) |

Anonymous drafts expire after `drf.draft.retention_days_anonymous` (`LD-DRF-010`). Events `drf.DraftStarted`, `drf.DraftCompleted`, `drf.DraftLaneEscalated`, `drf.DraftExported`, `drf.ReviewRequested`, `drf.ReviewDecided`, `drf.DraftHandedOff`.

### A.28 Qualified review (P06 §5.3; P09 §5.2; fulfilled through P16)

**Owner:** P06 (draft reviews, `drf.review`), P09 (AI-output reviews, `ai.qrg_reviews`, `qrv_`); fulfilment as a P16 SKU engagement · `ReviewFulfilmentWorkflow`, `QualifiedReviewWorkflow`.
**Canonical states:** `REQUESTED` (payment captured or internal reviewer assigned) → `ASSIGNED` → `ACCEPTED` → `IN_REVIEW` → **`APPROVED`** (attestation, reviewer of record and stamp; reviewed hash) | `RETURNED` (questions to user; review clock paused) → `RESUBMITTED` → `IN_REVIEW` | **`REJECTED`** (not suitable for self-help; refund per policy; consult offered) → **`CLOSED`**.
**Timers:** acceptance within `drf.review.accept_sla_hours` (default 4 working hours) else reassign; SKU delivery SLA; breach → `OPS_DELIVERY_LEAD`; auto-refund where the SKU says so (shown before purchase, NN-50).
**Resolution R-A-12:** P06 `PAID` = `REQUESTED`; P06 `ACCEPTED_BY_PROFESSIONAL` = `ACCEPTED`; P09 `RETURNED_TO_USER` = `RETURNED`. One reviewer-eligibility rule set (Appendix M); grant to the draft is time-boxed and revoked at CLOSED. Events `drf.ReviewRequested/ReviewDecided`, `ai.QualifiedReviewRequested/Completed`. **NN:** NN-14, NN-17, NN-41.

### A.29 CLM intake request (P07 §5.1) and its relation to the legal request (A.46)

`SUBMITTED → TRIAGED | NEEDS_INFO | REJECTED (reason)`; `NEEDS_INFO → SUBMITTED`; `TRIAGED → IN_DRAFTING (agreement created; IntakeConverted) | SELF_SERVE (configured low-risk types) → IN_APPROVAL`; IN_DRAFTING closes when the agreement reaches IN_NEGOTIATION. SLA starts at SUBMITTED. Events `clm.IntakeRequestSubmitted`, `clm.IntakeConverted`.
**Resolution R-A-13:** a Company tenant has one front door. When `lgo` is enabled, contract requests are legal requests (A.46) and conversion creates the `clm.intake_request` directly in TRIAGED with `lrq_` link; when `lgo` is not enabled (plans without the Legal Department OS) the CLM intake stands alone. Teams and email-in channels post to whichever front door is active.

### A.30 Agreement, negotiation round, change record and obligation (P07 §5.2–§5.5)

**Owner:** P07 · `clm.agreements` (`agr_`, `LD-AGR-…`), `clm.rounds` (`neg_`), `clm.changes` (`rlc_`), `clm.obligations` (`obl_`) · `NegotiationRoundWorkflow`, `ApprovalWorkflow`, `LockAndHandoffWorkflow`, `ObligationExtractionWorkflow`.

Agreement:

| From | Event | Guard | To | Events |
|---|---|---|---|---|
| — | create | From template, tenant template or upload | DRAFT | `clm.AgreementCreated` |
| DRAFT | first share | Leakage check (`LD-CLM-021`; NN-37) | IN_NEGOTIATION | `clm.VersionShared` |
| DRAFT / IN_NEGOTIATION | request approval | DoA evaluated for current hash (A.11) | IN_APPROVAL | `clm.ApprovalRequested` |
| IN_APPROVAL | all steps approved | Approvals bound to hash (`LD-CLM-032`); delegated maker never approves (`LD-CLM-031`) | APPROVED | `clm.ApprovalDecided` |
| IN_APPROVAL / APPROVED | version changes | — | IN_NEGOTIATION | `clm.ApprovalsInvalidated` |
| APPROVED | lock | All parties confirm the agreed version (OTP for guests); pre-sign gates (`LD-CLM-041`): untracked changes acknowledged (`LD-CLM-024`), no open shared issues, AI drafts reviewed for individuals | LOCKED_FOR_SIGNATURE | `clm.AgreedVersionConfirmed`, `clm.VersionLocked`; Object Lock applied |
| LOCKED_FOR_SIGNATURE | unlock | Maker + owner approval; never after any signature (`LD-CLM-042`) | IN_NEGOTIATION | `clm.VersionUnlocked`; P08 request voided |
| LOCKED_FOR_SIGNATURE | send for signing | A.31 request created | IN_SIGNATURE | `clm.HandedOffToSigning` |
| IN_SIGNATURE | `sgn.SigningCompleted` | — | SIGNED_PENDING_FORMALITIES | — |
| IN_SIGNATURE | `sgn.SigningRequestVoided` | — | LOCKED_FOR_SIGNATURE | — |
| SIGNED_PENDING_FORMALITIES | formalities complete | G-FORM (A.33) | EXECUTED | `clm.AgreementExecuted` (→ `legal.AgreementExecuted` via `int` under `legal_sor_link`) |
| EXECUTED | child executed / renewal / notice / expiry | — | AMENDED (stays EXECUTED with child) / RENEWED / **TERMINATED** / **EXPIRED** | `clm.AmendmentInitiated`, `clm.RenewalDecisionRecorded`, `clm.AgreementTerminated`, `clm.AgreementExpired`; survival obligations continue |
| before signature | cancel | Reason | **CANCELLED** | `clm.AgreementCancelled` |

Round (`neg_`, FR-P07-23): `OPEN (a side shares) → CLOSED_RETURNED (other side returns a version) | CLOSED_AGREED (confirmed as agreed) | CLOSED_WITHDRAWN`; nudges per `clm.negotiation.round_nudge_days` (5, informational); `clm.RoundClosed`.
Change record (`rlc_`): `PROPOSED → ACCEPTED | REJECTED | COUNTERED`; untracked changes start `NEEDS_ACKNOWLEDGEMENT → PROPOSED`; decisions append-only (reversal = new decision row); `clm.ChangeDecided`; application is deterministic (P07 §5.6 pseudo-code; NN-37).
Obligation (`obl_`): `PROPOSED → VERIFIED → UPCOMING → DUE → DONE | OVERDUE → DONE | WAIVED (reason, authorised role)`; `PROPOSED → REJECTED`; reminders T−90/60/30/7 only after key dates are verified (`LD-CLM-051`); `clm.ObligationVerified`, `clm.ObligationOverdue`, `clm.KeyDateApproaching`.
**Resolution R-A-14:** Appendix Y #46 status set (DRAFT, NEGOTIATION, APPROVED, EXECUTED, AMENDED, TERMINATED, EXPIRED) is the ecosystem projection: IN_APPROVAL→NEGOTIATION; LOCKED_FOR_SIGNATURE, IN_SIGNATURE and SIGNED_PENDING_FORMALITIES→APPROVED; CANCELLED is not projected. Obligation statuses project to `ContractObligationStatusChanged` as DUE, MET (=DONE), BREACHED (=OVERDUE past grace), WAIVED.

### A.31 Signing request and participant (P08 §5.1–§5.3; hosted hand-off P19 §5.9; mobile P22 §5.2)

**Owner:** P08 · `sgn.signing_requests` (`sgr_`), `sgn.participants`, `sgn.signature_events` (`sig_`) · `SigningCeremonyWorkflow` (per `sgr_`).

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create | Maker or agent (draft only) | Eligibility decision `ESIGN_OK*` / `DSC_OK` / `E_ACCEPTANCE_OK` (G-ELIG; `LD-SGN-014`, `-015`); AI drafts reviewed (`LD-DRF-003`); never for another application (`LD-SGN-034`, `LD-INT-060`) | DRAFT | `sgn.EligibilityEvaluated`, `sgn.SigningRequestCreated` |
| DRAFT | above tenant threshold | System | — | PENDING_APPROVAL | Approval to `ORG_CHECKER` ≠ maker |
| PENDING_APPROVAL | approve / reject | Checker | G-SOD | READY / DRAFT | — |
| DRAFT | freeze | Maker | PDF/A frozen with stamp merged (G-STAMP; `LD-SGN-003`, `-026`); SHA-256 locked; Aadhaar check (`LD-SGN-027`); signer authority (`LD-SGN-013`); adult signers (`LD-SGN-035`) | READY | — |
| READY | send | Human sender only (G-HUMAN; agent → `LD-AGT-007`) | Frozen hash unchanged (`LD-SGN-002`) | SENT | `sgn.SigningRequestSent`; invitations within NN-34 limits |
| SENT / IN_PROGRESS | participant events | Participants, provider | Turn order; consent shown and accepted (`LD-SGN-010`); assisted operator cannot act for signer (`LD-SGN-039`) | IN_PROGRESS | `sgn.SignerViewed`, `sgn.SignerConsented`, `sgn.SignatureApplied` |
| IN_PROGRESS | name mismatch / validation warning | System | — | HELD_FOR_REVIEW | `sgn.SigningHeld` (`LD-SGN-012`) |
| HELD_FOR_REVIEW | accept / void | Sender | Reason | IN_PROGRESS / **VOIDED** | — |
| IN_PROGRESS | request changes | Participant | — | CHANGES_REQUESTED → **VOIDED** (new round, `LD-SGN-036`) | `sgn.ChangesRequested` |
| IN_PROGRESS | decline | Signer | Reason mandatory | DECLINED → IN_PROGRESS (reassigned) or **CANCELLED** | `sgn.SignerDeclined` |
| SENT / IN_PROGRESS | `expires_at` | System | — | EXPIRED → IN_PROGRESS (one extension if no signature yet) or **CANCELLED** | `sgn.SigningRequestExpired` |
| IN_PROGRESS | last signature validated | System | Signature validation passes (`LD-SGN-028`) | **COMPLETED** | `sgn.SigningCompleted`; A.33 evidence pack; execution status → SIGNED_FORMALITIES_PENDING or EXECUTED |
| any non-terminal | cancel | Sender | — | **CANCELLED** | `sgn.SigningRequestVoided` |

Participant: `PENDING → INVITED → OPENED → CONSENTED → SIGNED | DECLINED | REASSIGNED | SKIPPED (CC/viewer)`; `FAILED_ATTEMPT` retries up to `sgn.esign.max_attempts` (3) then offers a method switch (`LD-SGN-011`).
Hosted hand-off (API-initiated, P19 §5.9): `REQUESTED (idempotent) → ELIGIBILITY_CHECKED (ineligible → WET_INK_PACK_OFFERED, LD-INT-061) → STAMP_PENDING (if chargeable) → READY (LawDocs signing URLs to the tenant's user, never to the calling app as a frame target, LD-INT-062) → [this machine] → COMPLETED | DECLINED | EXPIRED | WITHDRAWN`; outbound `esign.SigningRequestCreated/Completed/Declined/Expired/Withdrawn` (Appendix Y §Y.7.2).
Mobile invite (P22 §5.2) is a client-side journey over this machine: `LINK_OPENED → RESOLVED → OTP_VERIFIED → DOCUMENT_REVIEWED → STAMP_CHECK → CONSENT_SHOWN → ESP_LAUNCHED → RETURNED → SERVER_CONFIRMED → SIGNED | DECLINED | FAILED`; expired or over-used token → `NOT_AVAILABLE` (same response as non-existent).
Assisted signing (P08 FR-P08-56/57) adds no state: guard **G-ASSIST** on `CONSENTED → SIGNED` for a participant with an assistance record requires the assistance consent and helper declaration (`LD-SGN-041`), the witness where required, and that the signing action is performed by the signer's own authentication (`LD-SGN-039`); a signer who cannot act personally moves the request to the wet-ink route (`LD-SGN-042`) and `sgn.SigningAssistanceRecorded` is written to the evidence pack.
**NN:** NN-06 (X-05, X-15), NN-07, NN-08, NN-10, NN-13, NN-28, NN-34, NN-43, NN-46.

### A.32 Stamp instrument (P08 §5.4)

**Owner:** P08 · `sgn.stamp_instruments` (`stp_`; UIN unique platform-wide) · `StampOrderWorkflow`.
Purchase route: `QUOTED → PAYMENT_PENDING → ORDERED → ISSUED → VERIFIED → MERGED → LOCKED_TO_DOCUMENT`. Attach route: `UPLOADED → EXTRACTED → CONFIRMED → VERIFIED → MERGED → LOCKED_TO_DOCUMENT`. Side states `VERIFICATION_FAILED` (`LD-SGN-004`), `MISMATCH` (party, amount or already used, `LD-SGN-005`), `CANCELLATION_REQUESTED → CANCELLED | REFUNDED` (State procedure). Duty is pass-through at actuals and shown separately from LawDocs' facilitation fee (NN-08, NN-22); quotes are advisory until the State table is verified (`LD-SGN-007`); exemptions must be chosen from the cited list (`LD-SGN-037`); physical stamp paper is not combined with eSign while `sgn.stamp.physical_with_esign.enabled = false` (`LD-SGN-038`). Events `sgn.StampQuoted/Ordered/Issued/Verified/VerificationFailed/Merged/CancellationRequested`; to a requesting product as `esign.StampInstrumentVerified`.

### A.33 Formalities, execution status and evidence pack (P08 §5.5, FR-P08-39, FR-P08-44)

Formality item (`sgn.formalities` mirrored as A.15 items): `REQUIRED → IN_PROGRESS → RESOLVED (with evidence) | WAIVED (authorised human, reason from locked list; some formalities cannot be waived, LD-SGN-020) | NOT_APPLICABLE`. Kinds: STAMP, SIGNATURES, WITNESSES, NOTARISATION (`LD-SGN-017`), REGISTRATION (Registration Act s.23 window; `LD-SGN-018`), BOARD_APPROVAL (resolution via `gov` or LDC, `LD-GOV-013` when LDC unreachable), COUNTERPARTY_SIGNATURE, SPECIAL_LAW, INTERNAL_APPROVAL. Events `sgn.FormalityResolved`, `sgn.FormalityWaived`.
Execution status (document; mirrored to P04 and P07): `DRAFT → LOCKED_FOR_SIGNATURE → SIGNING → SIGNED_FORMALITIES_PENDING → EXECUTED`; `EXECUTED → SUPERSEDED (re-execution) | TERMINATED (termination instrument linked)`; `SIGNING → NOT_EXECUTED` (voided/cancelled). Wet-ink route: `PACK_ISSUED → SCAN_UPLOADED → SIGNED_FORMALITIES_PENDING → EXECUTED`. EXECUTED requires G-FORM (`LD-SGN-019`, `LD-WF-120`). Events `sgn.DocumentExecuted`, `sgn.DocumentSuperseded`.
Evidence pack (`sgn.evidence_packs`, `evp_`): `ASSEMBLING → SEALED` (manifest with SHA-256 per file and pack hash in the ledger; compliance-mode Object Lock, retention `EXECUTED_INSTRUMENT_EVIDENCE`) `→ ADDENDUM_SEALED` (each later formality appends a sealed addendum; the original seal never changes). A s.63(4) BSA 2023 certificate draft (Part A, Part B) is generated on request (`sgn.Bsa63CertificateDrafted`; feature flag until verified, `LD-DIX-026`). Events `sgn.EvidencePackSealed`. **NN:** NN-09, NN-10, NN-40.

### A.34 Signing provider status (P08 §5.6)

`ACTIVE → DEGRADED → ACTIVE`; `ACTIVE/DEGRADED → BLOCKED` (licence or contract expiry without renewal evidence, kill switch) `→ ACTIVE` (checker records evidence). `RENEWAL_UNCONFIRMED` is a flag with alerts until evidence is recorded. Routing never selects a BLOCKED provider (X-16: Capricorn lapsed 15 May 2026; Protean expires 26 Oct 2026 unless renewal evidence is recorded [VERIFY]). Events `sgn.ProviderHealthChanged`, `sgn.ProviderLicenceExpiring`, `sgn.ProviderRoutingBlocked`; `LicenceMonitorJob` nightly.

---

## Part IV — Vidhi AI and the agent workforce

### A.35 AI run and individual problem flow (P09 §5.1, §5.3)

**Owner:** P09 · `ai.runs` (`run_`), `ai.run_steps` · `VidhiRunWorkflow`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | request | User, agent, schedule | Budget > estimate (`LD-AI-007`, `LD-AGT-010`); tenant/agent not killed (G-KILL); data class computed from inputs; India route available for non-public classes (`LD-AI-003`); sealed content only for sealed roles (`LD-AI-004`) | RECEIVED | `ai.RunReceived` (added, Appendix B) |
| RECEIVED | plan | Agent | Multi-step or write tool | PLANNING | Plan stored |
| PLANNING | plan has writes | System | Read-only plans skip approval if `ai.plan.auto_approve_read_only` | AWAITING_PLAN_APPROVAL | — |
| AWAITING_PLAN_APPROVAL | approve / cancel | Human with scope | — | EXECUTING / **CANCELLED** | `ai.PlanApproved` (added) |
| EXECUTING | write above autonomy | Agent | — | AWAITING_ACTION_APPROVAL | `agt.ActionProposed` |
| AWAITING_ACTION_APPROVAL | approve / cancel | Human | G-SOD; G-HUMAN for external actions | EXECUTING / **CANCELLED** | `agt.ActionApproved` |
| EXECUTING | output produced | System | Step, time and credit caps | VALIDATING | Tool calls logged in `agt.activity_log` |
| EXECUTING | kill switch, budget, sponsor invalid | System / admin | — | PAUSED → EXECUTING (cause cleared) or **CANCELLED** | `ai.RunPaused` |
| VALIDATING | checks | System | Citations resolved or labelled unverified (`LD-AI-012`; NN-14); numbers and dates match sources (`LD-AI-011`); banned claims; injection; no fake official records (`LD-AI-020`) | DELIVERED, AWAITING_QRG, or **BLOCKED** | `ai.GuardrailTriggered`, `ai.CitationUnverified` |
| AWAITING_QRG | review outcome (A.28) | Eligible reviewer | High-risk legal output for an individual (`LD-AI-015`) | DELIVERED / RETURNED / **CANCELLED** | `ai.QualifiedReviewRequested` |
| DELIVERED | user decision | User | — | **ACCEPTED** / **REJECTED** / CHANGES_REQUESTED | `ai.RunCompleted` |
| any | failure | System | — | **FAILED** | `ai.RunFailed` |

Problem flow (individuals; `ai.problem_flows`): `TRIAGE → EMERGENCY_HANDOFF` (terminal for the AI path; human contacts shown) `| EXPLAINED → OPTIONS_SHOWN → PREPARING (draft linked) → REVIEW_PENDING (A.28) → READY (final, labelled) | PROFESSIONAL_BOOKED`; the user may return to any earlier step; the problem card is versioned. **NN:** NN-13, NN-14, NN-15, NN-43.

### A.36 Agent, autonomy change and mission (P09 §5.4–§5.6; Appendix H)

**Owner:** P09 · `agt.tenant_agents` (`agt_`), `agt.autonomy_changes`, `agt.missions` (`msn_`) · `AgentMissionWorkflow`, `AgentReviewWorkflow` (monthly).

| Machine | States and transitions | Guards |
|---|---|---|
| Agent | `DRAFT → SUPERVISED (hired; L1 only; ≥ supervised_days) → ACTIVE (induction complete + sponsor confirms) ⇄ PAUSED → RETIRED`; DRAFT may be discarded | Human sponsor named (`LD-AGT-001`); scope, tool allowlist, budget; PAUSED on kill switch, budget, sponsor invalid, missed monthly review, S1 incident; re-enable after S1 needs `ORG_ADMIN` + checker; outputs and logs retained at RETIRED; codes from the Appendix H roster only (X-27); events `agt.AgentHired`, `agt.AgentRetired` |
| Autonomy change | `PROPOSED (sponsor; readiness card) → CHECKED (ORG_ADMIN ≠ proposer) → EFFECTIVE (effective-dated) | REJECTED`; lowering is instant and needs no checker; automatic demotion writes `SYSTEM_DEMOTION` with cause | Ceiling ≤ plan limit and Appendix H ceiling (L0–L4); raise is a locked maker-checker action (NN-18); events `agt.AgentAutonomyChanged`, `agt.AgentDemoted` |
| Mission | `DRAFT → PLANNED (steps, owners, checkpoints, budget) → RUNNING ⇄ AT_CHECKPOINT (human) → COMPLETED | PAUSED | CANCELLED | FAILED` | Each step owner is an agent or a human; external actions only at a human checkpoint (G-HUMAN); FAILED lists compensation steps and never auto-reverses external effects; events `agt.MissionStarted`, `agt.MissionCheckpointReached`, `agt.MissionCompleted` |

Agent actions at L3/L4 are reversible internal changes with an undo window (`agt.activity_log.undo_until`; `agt.ActionExecuted`, `agt.ActionUndone`). A2A requests without an approved contract are refused (`LD-AGT-012`); automated calls need a declared number and consent (`LD-AGT-015`, Appendix J). **NN:** NN-13, NN-18, NN-34, NN-39, NN-43.

---

## Part V — Legal work

### A.37 Pleading project and affidavit (P10 §5.1, §5.3; FR-P10-35)

**Owner:** P10 · `pld.project` (`pld_`), `pld.affidavit` · `FilingPackWorkflow`, `AffidavitVerificationJob`.

| From | Event | Guard | To | Events |
|---|---|---|---|---|
| — | create | Forum chosen (`LD-PLD-001`) | DRAFTING | `pld.PleadingProjectCreated` |
| DRAFTING | validate | Required sections answered | VALIDATING | — |
| VALIDATING | findings | Any of V-1…V-10 fails (`LD-PLD-010/012/014/015/016/018/021/025`) | DRAFTING | `pld.PleadingValidated` (with findings) |
| VALIDATING | pass | All validators pass | READY_FOR_REVIEW, or READY (template-only, review not required) | `pld.PleadingValidated` |
| READY_FOR_REVIEW | review ordered | P16 order or company reviewer assigned | IN_REVIEW | — |
| IN_REVIEW | decide | Reviewer grant active | REVIEWED / DRAFTING (returned) | `pld.PleadingReviewed` |
| REVIEWED / READY | build pack | Filing pack built and validated (veraPDF; bookmarks; split) | PACKED | `pld.FilingPackBuilt` |
| PACKED | sign and swear | Verification signed; affidavits sworn and verified | SIGNED_SWORN | `pld.AffidavitSworn` |
| SIGNED_SWORN | mark filed | User records filing details (LawDocs never files; NN-05, NN-41) | **FILED** | `pld.PleadingFiled`; P11 case created |

Validators V-1…V-10 are listed in P10 §5.1 (V-4: no repealed code cited as current unless the pre-1 July 2024 toggle is on; V-6: s.63(4) Part A for each electronic-record annexure; V-7: certified translation for non-court-language annexures, NN-48; V-9: PII lint).
Affidavit: `draft_approved → print_ready (QR + stamp-duty line) → appointment_booked (optional) → sworn_uploaded (scan + jurat fields) → verified (OCR similarity ≥ 0.98 excluding the jurat) → attached`; `REJECTED_MISMATCH → print_ready` with differing pages highlighted (`LD-PLD-035`). The Studio never fills the jurat; affidavits are never eSign-eligible (NN-07; Appendix F; X-02).

### A.38 Notice (P10 §5.2)

**Owner:** P10 · `pld.notice` (`ntc_`, `LD-NTC-…`) · `NoticeDeliveryWorkflow`.
`DRAFT → REVIEWED (where required) → READY_TO_SEND → SENT (dispatch evidence) → DELIVERED | RETURNED_UNDELIVERED | DELIVERY_UNKNOWN → REPLY_RECEIVED (optional) → CLOSED`. SENT needs `confirm=true` + step-up (G-HUMAN; `LD-PLD-031`). Timers from the delivery date (reply window per notice; NI Act s.138 payment window; CPC s.80 two months) create legal clocks (A.42). Events `pld.NoticeDrafted`, `pld.NoticeDispatched`, `pld.NoticeDelivered`, `pld.NoticeReturnedUndelivered`. Recovery-instrument notices are not produced by LawDocs (Appendix Y #20).

### A.39 Matter (P11 §5.1)

**Owner:** P11 · `lit.matters` (`mat_`, `LD-MAT-…`).

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create | `ORG_LEGAL_MAKER` (from intake, notice, import or manual) | Required fields per type | DRAFT | — |
| DRAFT | confirm / discard | Maker | Owner set | ACTIVE / **DISCARDED** | `lit.MatterOpened`; legal-hold offer (A.20) |
| ACTIVE | stay recorded | Maker | Stay order linked | STAYED → ACTIVE | Lower-court clocks marked SUPERSEDED or kept per order |
| ACTIVE | no date for `lit.matter.dormant_days` (180) | Job | — | DORMANT → ACTIVE | Monthly refresh only |
| ACTIVE | settlement recorded | Maker + approver per DoA | Settlement deed executed (G-FORM via P08); compliance tasks created | SETTLED → CLOSED | `lit.MatterSettled` (added) |
| ACTIVE | final order confirmed | Maker; adapter may only propose | Order confirmed (A.41) | DISPOSED → ACTIVE (appeal, remand, review) or CLOSED | Appeal clock created |
| ACTIVE | withdrawal order | Maker | Order linked | WITHDRAWN → CLOSED | — |
| SETTLED / DISPOSED / WITHDRAWN | close | `ORG_CLO` | No OPEN clock (`LD-LIT-009`); no open direction (`LD-LIT-010`); final exposure assessment; lessons note if required | **CLOSED** | `lit.MatterClosed`; retention clock `LIT_RECORD` starts |
| CLOSED | reopen | `ORG_CLO` | Docket entry "Reopened" with reason | ACTIVE | — |

Matters with `owner_system ≠ LD` (Recovery Suite projections, LDC SoR) are read-only (`LD-LIT-007`, `LD-LIT-022`; X-06). Counsel see only assigned matters (`LD-LIT-012`). Events to LDC via `int`: `legal.LegalMatterOpened/Updated/Closed`.

### A.40 Court case status, hearing and court-data sync (P11 §5.2–§5.4)

**Owner:** P11 · `lit.cases` (`cas_`, `LD-CAS-…`), `lit.hearings` (`hrg_`) · `CourtDataSyncWorkflow`, `HearingOutcomeChaser`, `CauseListMatchJob`.
Case status overlay (normalised): `PENDING → LISTED (cause-list match) → HEARD | ADJOURNED | PART_HEARD | NOT_REACHED → PENDING (next date) … → RESERVED → DISPOSED`; side states `TRANSFERRED` (new case linked), `SINE_DIE`, `STAYED_BY_SUPERIOR_COURT`. Vendor status changes that conflict with a human entry become proposals (counsel and user entries prevail; FR-P11-16). Events `lit.CaseRegistered`, `lit.CaseStatusChanged`, `lit.CaseDataConflictDetected`.
Hearing outcome: `SCHEDULED → LISTED (cause-list match) → OUTCOME_DUE (court day ends)`; `SCHEDULED → OUTCOME_DUE (date passed)`; `OUTCOME_DUE → PROPOSED (vendor update or counsel post) → RECORDED (maker accepts)`; `OUTCOME_DUE → CHASED (+24 h) → ESCALATED (+72 h) → RECORDED`. Events `lit.HearingScheduled`, `lit.CauseListMatched`, `lit.HearingOutcomeRecorded`, `lit.HearingOutcomeMissing`.
Sync: select due cases by refresh class → route by coverage and adapter health (A → B → manual; `LD-LIT-004`, `-006`) → call with key `(case_id, adapter, date)` → diff and field provenance → conflicts → new orders (`lit.OrderFetched`, added) → meter `COURT_DATA_REFRESH` (`LD-LIT-005`) → `lit.CaseDataRefreshed` or `lit.CaseDataStale`. Only licensed adapters via `COURT_DATA_PORT`; no scraping or CAPTCHA solving (NN-05; X-29).

### A.41 Order and direction — order compliance (P11 FR-P11-25…27, FR-P11-29)

**Owner:** P11 · `lit.orders` (`odr_`), `lit.order_directions`.
Order: `UPLOADED | FETCHED → DIGEST_PROPOSED (AGT_ORDER_DIGEST; drv_ rendition labelled "AI summary — check against the order") → CONFIRMED (maker, ≤ 3 clicks)`; nothing is created before confirmation. CONFIRMED creates, in one transaction, direction tasks (`tsk_`), appeal and ORDER-COMPLIANCE clocks (A.42) and the hearing update (`lit.OrderConfirmed`, `lit.DirectionTaskCreated`). Original order files are immutable (NN-09).
Direction: `OPEN → IN_PROGRESS → COMPLIED (evidence) | NOT_COMPLIED (clock MISSED) | WAIVED_NO_ACTION (ORG_CLO reason) | SUPERSEDED (later order)`; an open direction blocks matter closure (`LD-LIT-010`). Projected to LDC as `legal.CourtOrderRecorded` with directions and due dates.

### A.42 Legal clock (P11 §5.5; reused by P10, P12, P13, P14, P15)

**Owner:** P11 · `lit.clocks` (`clk_`) · `ClockWatcher` (hourly).
`OPEN → (T−n reminders; lit.ClockDueSoon) → MET (evidence) | MISSED (date passed without evidence → lit.ClockBreached; CLO alert; exception in P13) | CONDONATION_SOUGHT (application linked; stays visible) | WAIVED_NO_ACTION (ORG_CLO, reason) | SUPERSEDED (rule or order change; new clock version)`. Start date is the earliest receipt by the party or its agent, never the logging date; exclusions (certified-copy time), hard caps and condonable extensions per rule (FR-P11-29). UNVERIFIED rules: same states, MISSED shows "advisory" and closure needs CLO acknowledgement (`LD-LIT-008`). Clock-breach alerts cannot be switched off below the tenant floor. Events `lit.ClockCreated`, `lit.ClockDueSoon`, `lit.ClockBreached`, `lit.ClockClosed`. P12 uses `subject_type = IPM_ASSET`; P15 uses `chp.case_deadline` rows computed by the same engine.

### A.43 ADR referral to Equator or another provider (P11 §5.7; P19 §5.8)

**Owner:** P11 · `lit.adr_referrals` · `AdrReferralWorkflow` (P11) using `EquatorReferralWorkflow` transport (P19).
**Canonical states:** `DRAFT` → `PRECHECK_FAILED` | `READY` → `APPROVED` (`ORG_CLO` or the individual with step-up) → `CONSENT_PENDING` (only where the counterparty's consent is captured by the provider) → `SUBMITTED` (`ODR_PORT`, when Appendix Y §Y.7.4 is live) or `MANUAL_INTERIM` (signed pack handed over; `LD-LIT-017`) → provider states projected read-only from `adr.ADRCaseStatusChanged` → `OUTCOME_RECORDED` (award or settlement stored; obligations and advisory clocks created) → **`CLOSED`**; **`WITHDRAWN`** before SUBMITTED by the user with confirmation (G-HUMAN); after SUBMITTED only through the provider.
**Pre-checks (logged; `LD-LIT-016`):** arbitration agreement naming an institution or written post-dispute consent (A&C Act s.7); no unilateral appointment; non-arbitrable categories blocked; pending consumer complaint; IBC moratorium where known; Commercial Courts Act s.12A route; never a lender's loan dispute (`regulatory-guard`).
**Resolution R-A-15:** P19 `DRAFT_PACK` = DRAFT/READY; P19 `OUTCOME_RECEIVED` = OUTCOME_RECORDED. Every screen states "Equator Resolution is an Infrabyx group company" and shows other configured providers (Appendix Y §Y.7.4). Event `lit.AdrReferralSubmitted` → `adr.ADRReferralCreated` via `int` (v1.2).

### A.44 Counsel invoice (P11 §5.8)

`RECEIVED → EXTRACTED → VALIDATED (PASS/WARN/FAIL) → PENDING_APPROVAL → APPROVED (checker ≠ maker; DoA; over budget needs approved overrun, LD-LIT-013) | REJECTED (reason to counsel) → EXPORTED_TO_AP → PAID_CONFIRMED (AP file or manual)`. No contingency or success fee for advocates (`LD-LIT-011`; X-03, NN-21). Event `lit.SpendInvoiceApproved`, `lit.BudgetThresholdCrossed`.

### A.45 Trademark application, assisted refresh, journal watch and renewal (P12 §5.1–§5.4; FR-P12-05)

**Owner:** P12 · `ipm.assets` (`tmk_`, `LD-TMK-…`), `ipm.status_events` (append-only), `ipm.watch_hits`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | clearance or data sheet started | Maker | — | PLANNED | `ipm.AssetCreated` |
| PLANNED | validation passes | Maker (+ checker if `ipm.filing.checker_required`) | Data sheet complete (`LD-IPM-009`); fee-category evidence (`LD-IPM-010`) | DATA_SHEET_READY | `ipm.DataSheetReady` (added) |
| DATA_SHEET_READY | hand off | Maker | Marketplace engagement or own agent | HANDED_OFF | `ipm.DataSheetHandedOff` |
| HANDED_OFF | record filing | Engaged professional only (`LD-IPM-011`) | Application number + receipt | NEW_APPLICATION | `ipm.TrademarkFiled` |
| NEW_APPLICATION … | Registry status (normalised FR-P12-05: VIENNA_CODIFICATION, FORMALITIES_FAIL/PASS, MARKED_FOR_EXAM, EXAM_REPORT_ISSUED, REPLY_FILED, SHOW_CAUSE_HEARING, ADVERTISED, OPPOSED) | Agent, maker or assisted refresh | Source + evidence document, or CLO "no document available" reason (`LD-IPM-006`) | next status | Clocks per state (TM-FORMALITY-CURE, TM-EXAM-REPLY, TM-HEARING, TM-OPPOSITION-WINDOW, TM-COUNTER-STATEMENT); `ipm.StatusChanged`, `ipm.ExaminationReportReceived`, `ipm.HearingScheduled`, `ipm.TrademarkAdvertised`, `ipm.OppositionReceived` (OPPOSED opens a P11 matter) |
| … | certificate recorded | Maker | — | REGISTERED | Renewal clock, non-use watch; `ipm.TrademarkRegistered` |
| REGISTERED | window opens (1 year before expiry) | Job | — | RENEWAL_DUE | Task with SKU option; `ipm.RenewalWindowOpened` |
| RENEWAL_DUE | renewal receipt | Agent | Receipt | REGISTERED (new valid-until) | `ipm.TrademarkRenewed` |
| RENEWAL_DUE | expiry passes | System | — | REMOVED (surcharge, then restoration window) | `ipm.AssetLapsed` |
| REMOVED | restoration order / window ends | Agent / system | — | REGISTERED / **CLOSED** | — |
| any | Registry refusal, abandonment, withdrawal, cancellation | Maker | — | **REFUSED / ABANDONED / WITHDRAWN / CANCELLED** → CLOSED or linked re-filing | Appeal clock where applicable (TM-APPEAL-HC) |

Assisted refresh: `UPLOADED → EXTRACTED (dix; confidence per field) → PROPOSED (AGT_TM_WATCH diff) → CONFIRMED (maker; status, dates and clocks atomically, NN-45) | REJECTED`; fields below `ipm.extract.min_confidence` (0.85) cannot be bulk-confirmed (`LD-IPM-007`). Events `ipm.StatusRefreshProposed/Confirmed`.
Journal watch: `JOURNAL_INGESTED (partner payload or uploaded PDF hashed) → PARSED → MATCHED → REVIEW (per hit: DISMISS | MONITOR | CEASE_AND_DESIST | OPPOSE | ASK_PROFESSIONAL) → CLOSED`; undecided hits escalate to the CLO at T−30 days to the opposition last date and get a final alert at T−7. No WIPO or Registry scraping (NN-05; X-29). Events `ipm.JournalIngested`, `ipm.WatchHitCreated`, `ipm.WatchHitDecided`. **Resolution R-A-16:** Appendix Y `ip_status` is the ecosystem projection of these states (e.g., FORMALITIES_FAIL → FORMALITIES_DEFECT; EXAM_REPORT_ISSUED → OBJECTED; ADVERTISED → ACCEPTED_ADVERTISED).

### A.46 Legal request — Company Legal Department OS (P13 §5.1)

**Owner:** P13 · `lgo.requests` (`lrq_`, `LD-LRQ-…`), `lgo.request_events` · `SlaTimerWorkflow`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | submit | Any tenant user; `AGT_LEGAL_INTAKE_DESK` proposes | Category active (`LD-LGO-001`); required fields (`LD-LGO-002`) | SUBMITTED | First-response and resolution timers; `lgo.RequestSubmitted` |
| SUBMITTED | triage | Triager (P1 or sensitive → human only) | Category, priority, owner confirmed | TRIAGED | `lgo.RequestTriaged` |
| SUBMITTED | guided path completed | Requester | Guardrails pass (else converted to review, `LD-LGO-003`) | SELF_SERVED → CLOSED | `lgo.SelfServiceCompleted` |
| TRIAGED | start / convert / reject | Assignee / triager | Reject needs reason | IN_PROGRESS / CONVERTED / REJECTED → CLOSED | First-response SLA met or breached |
| IN_PROGRESS | wait | Assignee | Reason + linked `itm_` (A.15); SLA pause only for permitted reasons (`LD-LGO-004`) | WAITING → IN_PROGRESS | — |
| IN_PROGRESS | output needs approval | Assignee | DoA band; approver ≠ maker; actions above delegation routed (`LD-LGO-007`) | PENDING_APPROVAL → IN_PROGRESS / RESOLVED | — |
| IN_PROGRESS / TRIAGED | convert | Assignee | Target module available (`LD-LGO-005`) | CONVERTED → RESOLVED (mirrors child) | Child record (agreement intake, notice, matter, TM, board item, HR, LDC, marketplace order); `lgo.RequestConverted` |
| IN_PROGRESS | resolve | Assignee | Outcome text | RESOLVED → CLOSED (auto after 7 days or on rating) or IN_PROGRESS (reopen ≤ 14 days) | `lgo.RequestResolved`; satisfaction prompt |

Statutory and court clocks linked to a request never pause (G-CLOCK). Events `lgo.SlaAtRisk`, `lgo.SlaBreached`.

### A.47 Governance kernel — meeting, minutes, resolution and related kernels (P13 §5.2–§5.7)

**Owner:** `@infrabyx/governance-kernel` and `@infrabyx/hrms-kernel` (used, never forked; NN-47) mounted by P13 in `local_kernel` mode; in `ldc_sor` mode LDC is SoR and these machines run in LDC (A.48).

| Machine | States and transitions | Guards / clocks | Events |
|---|---|---|---|
| Meeting (`gov.meetings`, `mtg_`) | `DRAFT → SCHEDULED → NOTICE_ISSUED (proof of delivery; shorter-notice path) → PAPERS_CIRCULATED → IN_SESSION (attendance, quorum monitor) → CONCLUDED → MINUTES_DRAFTED (≤ 15 days) → MINUTES_CIRCULATED → COMMENTS_CLOSED (7 days) → MINUTES_SIGNED → SEALED (≤ 30 days; s.118)`; side `ADJOURNED` (quorum lost, s.174(4)), `CANCELLED` (reason) | Notice period (`LD-GOV-003`); quorum (`LD-GOV-004`); interested directors cannot vote (`LD-GOV-006`); ratification pending blocks SEALED (`LD-GOV-009`); sealed minutes immutable (`LD-GOV-008`); minutes clock breach (`LD-GOV-007`) [VERIFY SS-1 timelines] | `gov.MeetingScheduled`, `gov.NoticeIssued`, `gov.PackPublished`, `gov.MeetingConcluded`, `gov.MinutesCirculated`, `gov.MinutesSealed` |
| Resolution (`gov.resolutions`, `res_`) | `DRAFT → PROPOSED (agenda item) → PASSED | FAILED | WITHDRAWN → FILING_DUE (where a filing applies; SRN captured, LD-GOV-012) → EFFECTIVE` | Required majority per type (BOARD, COMMITTEE, ORDINARY, SPECIAL, UNANIMOUS); follow-on tasks | `gov.ResolutionPassed` (to LD formalities gate; to LDC SoR via `governance` routing amendment, Appendix Y §Y.7.6) |
| Circular resolution | `DRAFT → BLOCKED (s.179(3) or other meeting-only matter; LD-GOV-005) | CIRCULATED → PASSED (majority of directors entitled to vote) | FAILED | REFERRED_TO_MEETING (≥ one-third require a meeting) → NOTED_AT_NEXT_MEETING` | Response window `gov.circular.response_days` (7 [VERIFY SS-1]) | `gov.CircularResolutionReferred`, `gov.ResolutionPassed` |
| KMP vacancy | `POSITION_FILLED → VACANCY_OPENED (s.203(4) six-month clock) → CANDIDATE_PROPOSED → APPROVALS → APPOINTED (DIR-12/MR-1 tasks) → POSITION_FILLED` | Clock breach → blueprint GAP and CS/CLO alert | `gov.KmpVacancyOpened`, `gov.KmpChanged` |
| POSH complaint (sealed) | `RECEIVED → CONCILIATION_REQUESTED (optional; s.10; no monetary settlement) → INQUIRY (≤ 90 days) → REPORT_ISSUED (≤ 10 days) → EMPLOYER_ACTION (≤ 60 days) → CLOSED`; `APPEAL_NOTED` | IC role + sealed-session step-up (`LD-HR-007`); only counts and ageing leave the seal | `hr.PoshCaseCountChanged` (counts only) |
| Pay run | `INPUTS_OPEN → INPUTS_LOCKED → COMPUTED (labour pack version) → REVIEWED (checker) → APPROVED → PAYSLIPS_PUBLISHED → BANK_FILE_EXPORTED → PAID_CONFIRMED`; corrections create an off-cycle run | Different checker (`LD-HR-002`); pack version (`LD-HR-001`); wage date limit (`LD-HR-003`) | `hr.PayRunApproved` |

**Resolution R-A-17:** the resolution machine is not drawn in P13 §5 (only circular resolutions); it is compiled here from FR-P13-37 and governs until the kernel's own definition is pinned in `docs/kernels.lock`, which then prevails (NN-47).

### A.48 Kernel system-of-record switch (P19 §5.6; P13 §5.4)

**Owner:** P19 · `int.sor_switches` · `SorSwitchWorkflow` (+ P13 `SorSwitchKernelHooks`).
`PROPOSED (ORG_ADMIN; same org_id in both products; impact preview) → APPROVED (ORG_OWNER ≠ maker, and the LDC admin) → EXPORTING (kernel writes frozen; per-record hashes and hash-chain heads) → IMPORTING (LDC reconciles counts and hashes) → DUAL_RUNNING (≥ one board-meeting cycle or 30 days; LawDocs gov/hr screens read-only with deep links; LD-GOV-014 blocks mode changes) → CUTOVER (platform.SystemOfRecordSwitched) → RECONCILED (signed report in the vault; byte equality for sealed minutes) → CLOSED (local tables archived read-only)`; any failure → `ROLLBACK` (LawDocs remains SoR; nothing deleted). Event `int.SorSwitchStateChanged`, `gov.SorModeChanged`. **NN:** NN-12, NN-24, NN-47.

---

## Part VI — Services, consumer help, marketplace and commerce

### A.49 Service order, return filing and renewal obligation (P14 §5.1–§5.3)

**Owner:** P14 · `bsv.order` (keyed `eng_`, business ref `LD-ENG-…`; Resolution R-A-18) · `ServiceOrderWorkflow`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | questionnaire complete | Customer | Eligibility ≠ NOT_ELIGIBLE (`LD-BSV-001/002`); fee lines shown in full (government fee paid on the official portal by default, X-18; `LD-BSV-010`) | QUOTED | `bsv.ServiceQuoted` |
| QUOTED | payment confirmed by OH8 | System | Idempotent payment reference (NN-46) | PAID → INPUTS_PENDING | `bsv.ServiceOrderPlaced`; checklist opened |
| INPUTS_PENDING | all mandatory items accepted | System | Checklist complete (`LD-BSV-003`) | INPUTS_COMPLETE → IN_PREPARATION | SLA clock starts; `bsv.InputsCompleted`; reminders T+2, T+5 |
| IN_PREPARATION | performer assigned | Delivery lead | Performer class and credential gate (`LD-BSV-006/007`); independence (`LD-BSV-008`) | (stays) | `bsv.PerformerAssigned` |
| IN_PREPARATION | preview shared | Performer | — | CUSTOMER_REVIEW | — |
| CUSTOMER_REVIEW | approve / request changes | Customer / `ORG_CHECKER` | Maker ≠ checker | CERTIFICATION (only `CERT_PRO_*`/`ATTEST_*`) or READY_TO_FILE / IN_PREPARATION | — |
| CERTIFICATION | certify | Certifying professional | COP valid today (`LD-BSV-007`; NN-41) | READY_TO_FILE | `bsv.ProfessionalCertified` |
| READY_TO_FILE | file | Customer or performer | Per-action human confirmation (`LD-BSV-009`; NN-13); DSC on the customer's device; no OTP or credential capture (`LD-TAX-004`) | FILED | Acknowledgement (SRN/ARN) uploaded; `bsv.ApplicationFiled` |
| FILED | authority query / approval / rejection | Performer | Query deadline tracked (A.42) | GOVT_QUERY → FILED / APPROVED / REJECTED | `bsv.GovernmentQueryRaised` |
| APPROVED | deliverables in vault | Performer | Certificate uploaded and hashed; G-FORM for instruments (`LD-BSV-011`) | DELIVERED | `bsv.DeliverablesDelivered`; renewal obligations created |
| DELIVERED | accept / auto-accept / rework | Customer / system | — | ACCEPTED → **CLOSED** / IN_PREPARATION | `bsv.ServiceOrderClosed`; CSAT |
| REJECTED | fresh attempt / close | Delivery lead | Refund scale applied | IN_PREPARATION / **CLOSED** | Credit note via P17 |
| QUOTED…INPUTS_PENDING | hold / cancel / expire | Customer / lead | Refunds maker-checker (NN-18) | ON_HOLD / **CANCELLED** / **EXPIRED** | `bsv.ServiceOrderCancelled` |

Return filing (`tax.filing`, `tfl_`): `DATA_COLLECTION → DRAFT_COMPUTED → TAXPAYER_REVIEW → PROFESSIONAL_REVIEW (optional) → APPROVED (rule pack verified, LD-TAX-001) → UPLOADED (ERI; taxpayer approval ≤ 72 h old and unchanged data hash, LD-TAX-003; flag LD-TAX-002) | HANDED_TO_TAXPAYER (guide mode) → AWAITING_EVERIFICATION → VERIFIED → PROCESSED (intimation) → CLOSED | NOTICE_RAISED`. Events `tax.ComputationDrafted`, `tax.ReturnUploaded`, `tax.ReturnEVerified`, `tax.NoticeReceived`.
Renewal obligation: `SCHEDULED → REMINDED → ORDERED (links a new bsv order) | SELF_HANDLED (evidence) → DONE | MISSED` (exposure recorded, never shown as savings; NN-36); `bsv.RenewalDue`.
**Resolution R-A-18:** a service order is an engagement (`eng_`, `LD-ENG-…`) created through `mkp`; `LD-ORD-…` is reserved for OH8 order mirrors and legacy orders (P00 FR-P00-41). The A.49 machine is the `bsv` profile of A.51.

### A.50 Consumer case per vertical, challan and vehicle sale (P15 §5.1–§5.3; queue view P18 §5.5; Appendix S)

**Owner:** P15 · `chp.case` (`grv_`, `LD-GRV-…`) in the Consumer Help logical cell (X-17) · `GrievanceCaseWorkflow`.
Generic spine (all verticals):

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | tile chosen | User | Vertical enabled (`LD-CHP-001`); in scope (`LD-CHP-002`) | INTAKE | `chp.CaseOpened` (no PII) |
| INTAKE | triage stored | System | Rule rows effective today; not yet eligible → date shown (`LD-CHP-003`) | TRIAGED | Deadlines computed; `chp.CaseTriaged` |
| TRIAGED / SELF_SERVE | paid or managed service requested | System | Conflict service answer (group lender/insurer clients; NN-23; Appendix Y §Y.7.8 conflict API) | CONFLICT_CHECK | `chp.ConflictChecked` |
| CONFLICT_CHECK | clear + fee plan agreed + consents | Delivery lead | Fee sheet acknowledged (Appendix S §S.11); policy permits (`LD-CHP-006`) | ACCEPTED | Case manager assigned (`chp.CaseAssigned`); OH8 order (commercial fields only; X-13); `chp.CaseAccepted` |
| CONFLICT_CHECK | conflict | System | — | SELF_SERVE (closure code `SELF_SERVE_ONLY_CONFLICT` if user stops) or DECLINED | — |
| ACCEPTED / SELF_SERVE | evidence | User, case manager | Minimum evidence set per vertical (Appendix S); hash integrity (`LD-CHP-008`) | EVIDENCE | Waiting items (A.15) |
| EVIDENCE | draft approved | User | Per-letter approval (G-HUMAN); banned-phrase lint (`LD-CHP-007`) | FIRST_LETTER_READY → FIRST_LETTER_SENT (dispatch proof hashed) | `chp.LetterApproved`, `chp.LetterDispatched`; wait clock (e.g., 30 days RE, 14 days insurer — Appendix S) |
| FIRST_LETTER_SENT | — | System | — | AWAITING_REPLY | Reminders; `chp.DeadlineApproaching` |
| AWAITING_REPLY | reply uploaded / clock expired | User / system | — | REPLY_RECEIVED / ESCALATION_READY | Window clocks recomputed |
| REPLY_RECEIVED | resolved / not resolved | User | — | RESOLVED / ESCALATION_READY | — |
| ESCALATION_READY | file at next forum | User (self-file) or case manager where the representation matrix allows (`LD-CHP-004`); authority letter valid (`LD-CHP-005`) | — | ESCALATED | `chp.CaseEscalated` (forum code only) |
| ESCALATED | acknowledgement | User / case manager | — | FORUM_PROCEEDING or ESCALATION_READY (next rung) | Hearing reminders |
| FORUM_PROCEEDING | award or order uploaded | User | Window computed | AWARD_OR_ORDER → ACCEPTANCE_WINDOW / APPEAL_WINDOW / COMPLIANCE_WATCH | `chp.AwardRecorded` |
| COMPLIANCE_WATCH | complied / not complied | System | Penalty-per-day tracker where the rule provides | RESOLVED / ESCALATION_READY | — |
| any active | refer to court | Advocate (fixed-fee engagement, P16) | — | REFERRED_TO_COURT → CLOSED | P11 matter opened (closure code `CC_REFERRED`) |
| RESOLVED / WITHDRAWN (24-hour cooling confirmation) / DECLINED / ABANDONED (`chp.case.abandon_days` 90) | close | User / lead / system | Exactly one primary closure code (Appendix S §S.20); refund scale; success fee only if RS-LD-40 ON | **CLOSED** | `chp.CaseClosed` |

Parallel tracks on any case: `SAFETY_TRACK` (police and cyber complaint; Appendix S §S.19), `HARASSMENT_LOG`, `CREDIT_REPORT_DISPUTE`, `SETTLEMENT_CORRESPONDENCE`. LawDocs never collects fines, dues or settlements (`LD-CHP-010`; NN-23) and never promises outcomes.
Vertical stage sets (Appendix S playbooks; labels map to the spine):

| Vertical | First rung (FIRST_LETTER) | Escalation rungs (ESCALATED) | Typical windows |
|---|---|---|---|
| A — Loans and lending (PB-A1…A5) | RE grievance/nodal officer (T-A1, T-A2, T-A8) | Internal Ombudsman → RBI Ombudsman (CMS; T-A3/T-A4) → appeal → consumer commission/civil court via advocate | RBIO window per CHR-A-12; award acceptance/compliance CHR-A-14/15 |
| A2 — Credit-report disputes | CIC + credit institution (T-A5) | RBIO (CICs are covered REs) | CI correction 21 days; CIC 30 days; compensation tracker (CHR-A2-03…05) |
| B — Insurance (PB-B1…B3) | Insurer GRO (T-B1/T-B2) | Bima Bharosa → Insurance Ombudsman (T-B3; user files) → consumer commission | 14-day GRO clock; one month to Ombudsman; mediation 15-day clock (T-B5) |
| C — Challans | — (challan machine below) | Lok Adalat or court contest via advocate | Per State rules (Appendix S §S.8) |
| D — Vehicles | — (vehicle sale machine below) | RTO/Vahan follow-ups | 14/45-day transfer watch; 30-day hypothecation release watch |
| Shared — Consumer commission | — | District/State/National per pecuniary limits (CHR-CC-01) via e-Jagriti | Limitation 2 years (CHR-CC-02 [VERIFY]) |

Challan (`chp.challan`, `chl_`): `DISCOVERED → CLASSIFIED → DECIDED {PAY | LOK_ADALAT | CONTEST} → PAID_ON_OFFICIAL (receipt uploaded) | LOK_ADALAT_BOOKED → LOK_ADALAT_DISPOSED | CONTEST_ADVOCATE_ENGAGED → HEARING → DISPOSED → RECORD_UPDATE_CHECK → CLOSED`; side `DISPUTED_WRONG_OWNER`. Events `chp.ChallanImported`, `chp.ChallanPaidOnOfficial`.
Vehicle sale (`chp.vehicle_sale`): `PRE_SALE_CHECKS → TERMS_AGREED → AGREEMENT_DRAFTED → STAMPED (where duty applies) → SIGNED → PAYMENT_CONFIRMED (both parties confirm; no escrow) → DELIVERED → FORMS_PREPARED → VAHAN_APPLIED → RC_TRANSFERRED → INSURANCE_TRANSFERRED → CLOSED`; branch `HYPOTHECATED → FORECLOSURE_REQUESTED → LOAN_CLOSED → NOC_AND_FORM35_RECEIVED → HYPOTHECATION_REMOVED`; G-FORM before SIGNED is treated as executed. Events `chp.VehicleSaleSigned`, `chp.RcTransferDue`.
**Resolution R-A-19:** P18 §5.5 is a queue view for `OPS_CONSUMER_CASE_MANAGER`: NEW = INTAKE/TRIAGED; CONFLICT_CHECK = CONFLICT_CHECK; CLEAR → ASSIGNED = ACCEPTED; CONFLICT → SELF_SERVE_ONLY = SELF_SERVE; WORKING = EVIDENCE…FORUM_PROCEEDING; WAITING_ON_{USER|BANK|INSURER|OMBUDSMAN|COURT} = a WAITING `itm_` on the case with that party type; CLOSED = CLOSED. P18's `chp.ConflictCheckCompleted` is an alias of `chp.ConflictChecked`. No `chp` event is ever published by `int` (X-26; Appendix Y principle 14). **NN:** NN-13, NN-20, NN-23, NN-50.

### A.51 Marketplace engagement, retainer, service product, dispute and Route payout (P16 §5.1–§5.5)

**Owner:** P16 · `mkp.engagements` (`eng_`, `LD-ENG-…`), `mkp.retainers` (`rtn_`), `mkp.change_requests` (`ecr_`), `mkp.disputes`, `mkp.payout_instructions` · `EngagementWorkflow`, `RetainerCycleWorkflow`, `PayoutReleaseWorkflow`.

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | quote request | Buyer (consent artefact) | — | REQUESTED | `mkp.ServiceRequested`; triage SLA 1 BD |
| REQUESTED | triage accepted / declined | Professional / delivery lead | Conflict check PASS (`LD-MKP-020/022`) | SCOPING / **DECLINED_BY_SUPPLIER** | Scope draft by agent (maker only) |
| SCOPING | offer sent | Supplier | Independence PASS (`LD-MKP-021`); offer validity | OFFERED | `mkp.OfferIssued` |
| OFFERED | accept / decline / validity ends | Buyer | Price lines confirmed by OH8 quote; reserved classes never supplied by LawDocs (`LD-MKP-010`) | ACCEPTED / **DECLINED_BY_BUYER** / **EXPIRED** (`LD-MKP-025`) | `mkp.OfferAccepted` |
| ACCEPTED | engagement letter executed | Buyer + supplier | Letter version hash on all signatures | CONTRACTED | `mkp.EngagementContracted`; letter + evidence pack to vault |
| CONTRACTED | payment received (server-verified, never redirect) | System | — | PAID → INPUTS_PENDING | M2: Route transfers created `on_hold` |
| INPUTS_PENDING | inputs complete | Buyer | `LD-MKP-030` | IN_DELIVERY | Timeline/SLA clocks run; reminders D+3, D+7 |
| IN_DELIVERY | delta proposed | Either side | Approver per threshold; amendment executed | CHANGE_REQUESTED → IN_DELIVERY | `mkp.ChangeRequestApproved` / `mkp.ChangeRequestRejected` (added); OH8 quote amendment; time outside scope refused (`LD-MKP-031`) |
| IN_DELIVERY | milestone released after QA | Supplier | QA passed (M1) | DELIVERED | `mkp.MilestoneDelivered`; deemed-acceptance timer |
| DELIVERED | revise / accept / deemed | Buyer / system | Revisions remaining; deemed only if the letter allows; delivery staff never accept for the buyer | REVISION_REQUESTED → IN_DELIVERY / ACCEPTED_BY_BUYER | `mkp.DeliverableAccepted`; Route release requested |
| ACCEPTED_BY_BUYER | more milestones / all accepted | System | Final invoice issued (OH8) | IN_DELIVERY / CLOSED → REVIEWED | `mkp.EngagementClosed`; review request (LawDocs services only; never about advocates, NN-49) |
| * | hold / cancel / dispute | Supplier, buyer / grievance flow | Reason; refund rule | ON_HOLD (clocks paused) / CANCELLED → REFUNDED / DISPUTED | `mkp.EngagementCancelled`, `mkp.DisputeRaised`; Route holds frozen |

Retainer: `OFFERED → CONTRACTED (letter + SLA schedule eSigned; LD-MKP-033) → ONBOARDING (P18 grants proposed → ORG_ADMIN approves) → ACTIVE (monthly plan → deliver → hour bank → SLA events → report → invoice → service-credit calc) → RENEWAL_DUE (T−60) → RENEWED | NOTICE_GIVEN → WIND_DOWN (hand-over pack; grants revoked at end) → ENDED`; `ACTIVE → SUSPENDED` (OH8 dunning RESTRICTED; statutory items ≤ 30 days continue or are handed over) `→ ACTIVE`; `ACTIVE → AMENDMENT_PENDING → ACTIVE`; hour bank exhausted blocks time entries (`LD-MKP-035`). Events `mkp.RetainerActivated`, `…HourBankThresholdReached`, `…SLABreached`, `mkp.ServiceCreditRequested`, `mkp.RetainerRenewed`, `mkp.RetainerEnded` (→ A.9 revoke).
Service product: `DRAFT → LINTED → IN_REVIEW (OPS_QA_REVIEWER + PLT_LEGAL_REVIEWER for reserved classes) → LIVE → PAUSED → RETIRED`; lint (`LD-MKP-004/005/006/012`). `mkp.ServicePublished`. Profession-rule switches are locked OFF until a counsel opinion is attached and a checker approves (`LD-MKP-015/017`; NN-21).
Dispute: `RAISED → SUPPLIER_RESPONSE (≤ 5 BD) → RESOLVED_BY_AGREEMENT | ESCALATED → LAWDOCS_REVIEW (M1 → OH6 client complaint; M2/M3 → facilitation ≤ 10 BD) → OUTCOME (RE_WORK | PARTIAL_REFUND | FULL_REFUND | NO_ACTION) → CLOSED` (external remedies stated); acknowledge ≤ 48 h, resolve ≤ 1 month (`LD-MKP-050`); Route holds stay until OUTCOME (`LD-MKP-040`). `mkp.DisputeResolved`.
Route payout (M2): `ORDER_PAID → TRANSFER_CREATED (on_hold; idempotency key) → RELEASE_REQUESTED (DeliverableAccepted | deemed | consult window closed | dispute outcome) → RELEASED → SETTLED (Razorpay settlement report matched; MarketplacePayoutSettled from OH) | REVERSED (refund; credit note for LawDocs fee)`; unmatched > 24 h → OH8 billing-operations task; never a manual payout from a LawDocs account (NN-22; `LD-MKP-041`). Events `mkp.PayoutReleaseRequested`, `mkp.PayoutReconciled`.
Academy sync: `FETCH → VALIDATE → DIFF → PUBLISH`; failure keeps the last good catalogue ≤ 7 days, then hides prices and deep-links only (`LD-ACA-001/002`; `aca.CatalogueSynced`).

### A.52 Subscription, plan change, credit lot, stream switch and savings snapshot (P17 §5.1–§5.5)

**Owner:** P17 (mirror of OH8; OH8 is the billing engine) · `bil.subscriptions_mirror`, `bil.credit_lots`, `bil.stream_registry`, `sav.snapshots`.
Subscription: `TRIAL (one per person/org per plan family; LD-BIL-011) → TRIAL_ENDED (day 14; revert to Free, data kept) | PENDING_ACTIVATION (order created) → ACTIVE (server-verified payment or PO; SubscriptionActivated) → RENEWAL_DUE (T−30/T−7; notices) → ACTIVE | CANCELLATION_REQUESTED`; `ACTIVE → PAST_DUE → GRACE → RESTRICTED (7 days' notice) → TERMINATION_NOTICE → ENDED_TO_FREE` per OH8.7, with return to ACTIVE on payment; `CANCELLATION_REQUESTED → ACTIVE (withdrawn) | ENDED_TO_FREE`; `ENDED_TO_FREE → ACTIVE (re-subscribe)`; `EXIT → CLOSED` enters A.23. Read and export are never blocked (never-block list; `LD-BIL-050` internal alert). Cancellation is as easy as sign-up (NN-50).
Plan change: `SELECT → QUOTE (OH8: proration, GST, entitlement diff; valid 7 days, LD-BIL-015) → [PENDING_TENANT_APPROVAL (ORG_APPROVER, step-up; LD-BIL-016)] → ORDER → PAY (or credit) → PlanChanged + EntitlementChanged (signed; verified, LD-BIL-001) → APPLIED (≤ 1 min)`; downgrade `SCHEDULED (term end) → APPLIED`, withdrawable until then. Events `bil.PlanChangeScheduled`, `bil.EntitlementApplied`.
Credit lot: `GRANTED (allowance | pack | promo | referral | service credit) → ACTIVE → CONSUMED (partial/full) → EXPIRED (notices T−30/T−7) | REFUNDED (pro-rata; OH8 credit note) | EXTENDED (once)`; failed-service reversal returns to the originating lot (idempotent on source event id). Events `bil.CreditsGranted/Consumed/Returned/Expired/Low`.
Stream switch: `PROPOSED (maker) → CHECKED (PLT_LEGAL_REVIEWER where legal flag; checker ≠ maker, LD-BIL-042) → [OWNER_APPROVED] → EFFECTIVE (effective_from) → caches invalidated ≤ 5 min`; prohibited streams refused (`LD-BIL-041`); stream gate must be ACTIVE (`LD-BIL-040`); kill switch: PROPOSED + CHECKED in one emergency flow with a second approver within 15 min. `bil.StreamSwitchChanged`.
Savings snapshot: `COLLECT → APPLY methodology v → COMPUTE tiles → SNAPSHOT (inputs, versions, hash, evidence class MEASURED/ESTIMATED/MODELLED) → PUBLISH → (quarterly) VALUE_REPORT`; methodology change creates a new version and never silently recomputes the past (NN-36; `LD-SAV-001…004`). Events `sav.SnapshotComputed`, `sav.MethodologyPublished`, `sav.ValueReportGenerated`.

### A.53 Invoice, credit note and refund mirror (P17 §4K FR-P17-46…50; OH8)

**Owner:** OH8 (issuer); P17 mirrors · `bil.documents_mirror` (`inv_`), `bil.payments_mirror` (`pay_`) · `InvoiceFilingJob`.
Invoice mirror: `ISSUED (InvoiceIssued received; signed artefact verified) → FILED (PDF in vault; hash) → PAID (SubscriptionPaymentReceived or payment mirror) | OVERDUE (derived) | DISPUTED (OH6 BILLING_DISPUTE ticket; dunning paused) → CORRECTED (credit/debit note from OH8, never an edit) | PAID`. Refund: `REQUESTED (customer; rule shown before purchase) → APPROVAL_PENDING (maker-checker in OH8; NN-18) → APPROVED → PROCESSED (Razorpay refund via OH8) → CREDIT_NOTE_ISSUED (mirrored) | REJECTED (reason)`. LawDocs never edits a tax document and never computes GST (OH8 does; NN-22). Events `bil.InvoiceFiled`, `bil.UsageDisputed`.
**Resolution R-A-20:** P17 defines no explicit invoice or refund machine; this mirror is compiled from FR-P17-46…50 and the OH8 contract. It holds commercial fields only (X-13).

---

## Part VII — Delivery console and integration

### A.54 Deliverable (P18 §5.4)

**Owner:** P18 · `sdc.deliverables` (`dlv_`).
`DRAFT (author) → IN_REVIEW (OPS_QA_REVIEWER ≠ author; LD-SDC-015) → RELEASED (filed in client DMS; optional copy to client drive within residency rules, LD-SDC-025) → ACCEPTED (client owner/checker) | RETURNED (comments) → DRAFT (v+1)`. Advocate opinions: `DRAFT (advocate) → RELEASED by the advocate` (LawDocs QA may comment, never edit; NN-41). Work by a delegated maker must be checked by the client (`LD-SDC-007`). Events `sdc.DeliverableReleased`, `sdc.DeliverableAccepted`, `sdc.DeliverableReturned`.

### A.55 Credential entry and reveal (P18 §5.2)

**Owner:** P18 · `cvl.entries` (`cvl_`), `cvl.grants`, `cvl.reveal_events` (append-only), `cvl.rotation_tasks` · `RevealAnomalyDetector`, `VaultRotationPromptJob`.
Vault: `OFF → ENABLE_REQUESTED (client admin) → ON (second client admin approves; LD-CVL-002)`; `ON → OFF` by client admin. Entry: `DRAFT (client) → ACTIVE → ROTATION_DUE → ACTIVE (rotated) | ARCHIVED (client; secrets crypto-shredded)`. Blocked types: OTP, PIN, recovery code, banking (`LD-CVL-003`); URL allow-list (`LD-CVL-011`).

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | request reveal | Grantee | Vault ON (`LD-CVL-001`); credential grant (`LD-CVL-006`); purpose + linked task (`LD-CVL-004`); client-only portal acknowledged (`LD-CVL-005`); allowed hours (`LD-CVL-008`); no anomaly lock (`LD-CVL-009`); delivery grant ACTIVE; kill switch released (`LD-CVL-010`) | REQUESTED | `cvl.CredentialRevealRequested` |
| REQUESTED | step-up | Grantee | Passkey | STEP_UP_OK | — |
| STEP_UP_OK | per-reveal approval configured | System | — | CLIENT_APPROVAL (`LD-CVL-007`) → STEP_UP_OK on approve, **DENIED** on reject | Client task |
| STEP_UP_OK | issue one-time token | System | — | REVEALED (for `cvl.reveal_seconds`; never cached) | `cvl.CredentialRevealed` (sealed, tenant-only) |
| REVEALED | timer | System | — | **LOGGED_AND_NOTIFIED** | Client sees every reveal |
| — | any delivery grant of the grantee ends | System | 180-day look-back | ROTATION_PROMPTED (per credential revealed) | `cvl.CredentialRotationPrompted` |

**NN:** NN-16 (OTPs, DSC PINs and recovery codes never stored; OFF until the client enables it; delegation-first).

### A.56 Master-data change (P18 §5.3; wraps A.1)

**Owner:** P18 · `sdc.masterdata_requests` (`mdc_`) · `MasterDataChangeWorkflow`.
`RAISED (OPS_RM, client ticket or PLT_SUPER_ADMIN as maker; evidence attached, LD-SDC-018; field class A) → AWAITING_CLIENT → CLIENT_APPROVED | CLIENT_REJECTED (ORG_OWNER or two ORG_ADMINs; step-up; not the maker; LD-SDC-016) → APPLIED (PLT_SUPER_ADMIN checker ≠ maker, LD-SDC-017; Correction Entry written in the same transaction) → IN_REVIEW_WINDOW (7 days) → CLOSED | REVERT_REQUESTED`; `CLIENT_APPROVED → RETURNED` (checker). Exceptions: `RECOVERY_HOLD` (owner lost access; identity re-verified; signatory authority uploaded; 72-hour hold → CLIENT_APPROVED path with recovered owner) and `ORDER_COMPELLED` (court or regulator order attached; PLT_SUPER_ADMIN + counsel → checker → APPLIED). A Super Admin never approves on the client's behalf (`LD-SDC-008`); an owner-only policy does not exist (X-11; NN-18). Events `sdc.MasterDataChangeRequested`, `…ClientDecided`, `…Applied`, `…RevertRequested`. **Resolution R-A-21:** P02's `POST /v1/org/master-data-changes` is the tenant-side entry point to this machine (`LD-ORG-010` directs direct edits here); there is one machine.

### A.57 Leaver sweep (P18 §5.6)

`EmployeeOffboarded` (OH10, ≤ 5 minutes) → suspend grants (≤ 15 min) → end sessions (≤ 60 s) → list credentials revealed in 180 days → rotation prompts per tenant → reassign tasks and deliverables to backup RM → propose replacement grants (client approves; A.9) → notify clients → acknowledge to OH. Temporal `LeaverSweepWorkflow`, idempotent per (employee, event id); hourly SCIM reconciliation catches missed events.

### A.58 Integration machines (P19 §5.1–§5.5, §5.7)

| Machine | Owner / table | States and transitions | Guards and events |
|---|---|---|---|
| Connector instance | `int.connector_instances` | `AVAILABLE → REQUESTED (ORG_ADMIN; plan allows) → PREREQUISITES_PENDING → CONFIGURED (maker) → APPROVED (checker ≠ maker; + ORG_CLO for LEGAL outbound; + PLT_DPO for a new PII+ cross-product flow) → TESTING → ACTIVE ⇄ DEGRADED`; `ACTIVE/DEGRADED → SUSPENDED (kill switch, key/link expiry, residency fail, certification lapse; re-enable needs checker)`; any → `DISCONNECTING (drain outbox, final reconciliation, revoke tokens, export mapping history) → DISCONNECTED` | ACTIVE requires valid certification and keys valid ≥ 7 days (`LD-INT-080/081`); probes every 5 min; `int.ConnectorInstanceStateChanged` |
| Ecosystem link | `int.links` | `PROPOSED → APPROVED_LOCAL (tenant maker-checker) → APPROVED_COUNTERPART → CERTIFIED_CHECK → ACTIVE ⇄ PAUSED → EXPIRED | REVOKED → CLOSED` | `valid_to` mandatory (default 12 months; group-grant refs ≤ 90 days); PAUSED queues, never drops; `LD-INT-032/033`; `int.EcosystemLinkStateChanged`; link kinds per Appendix Y §Y.3.3 |
| Outbound delivery | `core.outbox`, `int.deliveries`, `int.dlq` | `OUTBOX → RELAYED → MAPPED (internal → ecosystem; link active; dataclass ≤ ceiling; consentref/legalbasis present) → SIGNED → DELIVERED`; policy reject → `BLOCKED` (policy-reject log; sharing-ledger "blocked" entry when personal data); 408/429/5xx → `RETRY` (exponential back-off, full jitter, ≤ 72 h) → `DLQ`; other 4xx → `FAILED_PERMANENT → DLQ`; `DLQ → REPLAY_REQUESTED (maker) → REPLAY_APPROVED (checker ≠ maker) → OUTBOX (same event id)` | FIFO per subject; `LD-INT-030/031/034/035`; Consumer Help events never mapped (NN-23); `int.WebhookDeliveryFailed`, `int.DlqReplayRequested/Approved`, `int.SharingLedgerEntryRecorded` |
| Inbound message | `int.inbox` | `RECEIVED (mTLS) → VERIFIED (RFC 9421 + timestamp ±5 min + cert ↔ client) → VALIDATED (pinned schema) → AUTHORISED (consent/legal basis, dataclass ≤ ceiling, tenant map, link ACTIVE) → INBOXED (duplicate → 200 no-op) → SEQUENCED (gap → PARKED 15 min → catch-up GET /v1/events → else ReconciliationBreakRaised) → HANDLED → ACKED (2xx after durable write)`; handler failure → retry → `POISON → inbox DLQ` | `LD-INT-011/012`; `int.ReconciliationBreakDetected` |
| Partner batch | `int.onboarding_batches` | `RECEIVED → VALIDATING → VALIDATED (dry run stops here) → PREFILLING → INVITING → COMPLETED | REJECTED` | Rows invalid (`LD-INT-070`); regulated professionals cannot take revenue share (`LD-INT-071`); individuals cannot be bulk-onboarded (`LD-INT-072`); invitations follow A.2; `int.OnboardingBatchSubmitted` |
| Deposit link | `int.deposit_links` | `NOT_LINKED → AUTHORISING (PKCE) → LINKED ⇄ PAUSED → UNLINKED`; per deposit `RECEIVED → FETCHING → VERIFIED (hash and JWS) → STORED | REJECTED` | `LD-INT-051/052`; WELLNESS class rejected; `int.DepositLinkCreated/Revoked`; `documents.DocumentDeposited` to the depositor; internal `dms.DocumentDeposited` (added) |

---

## Part VIII — Website, help, mobile and engineering

### A.59 CMS page and post version (P21 §5.1)

**Owner:** P21 · `web.pages` (`pg_`), `web.page_versions`, `web.posts` (`pst_`) · `PublishWorkflow`. Content Studio sits in `apps/console`, restricted to `OPS_CONTENT_PUBLISHER`, `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER` (X-22).

| From | Event | Actor | Guard | To | Side effects / events |
|---|---|---|---|---|---|
| — | create, import, rollback draft, agent proposal | Maker | — | DRAFT | — |
| DRAFT | submit | Maker | Blocking checks: template minimum (`LD-WEB-019`), alt text, links, claims approved (`LD-WEB-002`; NN-20), citations resolved (`LD-WEB-016`), plagiarism (`LD-WEB-003`), outdated-law linter (`LD-WEB-017`), competitor links (`LD-WEB-018`), structured data (`LD-WEB-006`), axe (`LD-WEB-007`), prices from catalogue (`LD-WEB-020`), urgency bound to a real event (`LD-WEB-021`; NN-50), State variant materiality (`LD-WEB-009`) | IN_REVIEW | Notification to checker |
| IN_REVIEW | approve / return | Checker (`PLT_CONTENT_EDITOR` or a second publisher for non-legal posts) | G-SOD (`LD-WEB-015`) | APPROVED, or LEGAL_REVIEW if the legal flag is set / DRAFT | — |
| LEGAL_REVIEW | approve / return | `PLT_LEGAL_REVIEWER` | Reviewer ≠ maker; reviewer credential on file | APPROVED / DRAFT | Reviewer of record stamped (`LD-WEB-001` blocks indexing without one) |
| APPROVED | publish now / schedule | Maker or checker | Checks re-run; schedule not in the past (`LD-WEB-014`); locale pages human-reviewed (`LD-WEB-022`) | PUBLISHED / SCHEDULED | — |
| SCHEDULED | publish-at / unschedule | System / maker | Checks re-run at publish time | PUBLISHED / APPROVED | — |
| PUBLISHED | new version published / unpublish | System / checker | Unpublish: 301 or 410 chosen | **SUPERSEDED** / UNPUBLISHED | Revalidate, IndexNow, search index, sitemap; `web.PageVersionPublished`; `web.PageUnpublished` with redirect |
| UNPUBLISHED | edit | Checker | — | DRAFT | — |
| DRAFT | stub, upcoming or law-change hold | Editor | — | HOLD → DRAFT | `noindex`; excluded from sitemap |

Review-overdue and law-change events (`web.ContentReviewDue`, `web.LawChangeFlagged`) queue a PUBLISHED page for review without changing its state; after 60 days overdue it switches to `noindex`. Policy pages render from the POL-LD register (X-30) with re-acceptance gating `LD-WEB-090…093` (Appendix O). Advertising slots only where NN-35 allows (`LD-WEB-024`).

### A.60 Other website and help machines (P21 §5.2–§5.7)

| Machine | States | Notes |
|---|---|---|
| DOCX import (`web.import_jobs`) | `QUEUED → SCANNING → BLOCKED_TRACKED_CHANGES ⇄ awaiting decision → CONVERTING → LINTING → DRAFTS_CREATED | FAILED` (per file; job completes when all rows are terminal) | `LD-WEB-008`; `web.DocxImportCompleted` (counts only) |
| Glossary term (`hlp.terms`, `trm_`) | `DRAFT → IN_REVIEW → LEGAL_REVIEW (if legal definition) → PUBLISHED → REVIEW_DUE (rule change or age) → PUBLISHED | DEPRECATED`; locale sub-state `MT_DRAFT → HUMAN_REVIEWED → PUBLISHED` (NN-48) | Deprecated keys stay resolvable; `hlp.gen.<term>` for general jargon (X-10); `LD-HLP-001/002`; `hlp.TermPublished` |
| Tutorial (`hlp.tutorials`, `tut_`) | `SCRIPTED → CAPTURED → ANNOTATED → NARRATED → CAPTIONED → ISL_ADDED (optional) → IN_REVIEW → PUBLISHED → STALE (screenshot diff or rule change) → CAPTURED` | Synthetic tenant only (`LD-HLP-006`); captions and transcript required (`LD-HLP-003/004`); `hlp.TutorialPublished`, `hlp.TutorialStale`, `hlp.ClipExported` |
| Lead hand-off (`web.leads`) | `CAPTURED → SENT (int → OH CRM 2xx) → ACKNOWLEDGED (OH lead id) → PURGED (30 days)`; failure `RETRYING (≤ 72 h) → DEAD_LETTER` | Consent withdrawal before SENT cancels (`LD-WEB-013`); NN-19; `web.LeadCaptured` |
| Accessibility issue (`hlp.a11y_issues`) | `RECEIVED → ACKNOWLEDGED (≤ 48 h) → TRIAGED (S1–S4) → IN_FIX → FIXED → VERIFIED → CLOSED | WONT_FIX (approved alternative + statement entry)` | S1 on a core journey blocks the next release (Appendix U); `hlp.AccessibilityFeedbackReceived` |
| Redirect rule (`web.redirects`) | `DRAFT → APPROVED (maker-checker) → ACTIVE → RETIRED` | Single hop (`LD-WEB-005`); retire only after 12 months with zero hits and never for legacy URLs with backlinks; `web.RedirectMapPublished` |

### A.61 Mobile machines (P22 §5.1, §5.3–§5.5)

| Machine | States | Guards and events |
|---|---|---|
| Device (`mob.devices`, extends `iam.devices` `dev_`) | `PENDING → BOUND | REJECTED`; `BOUND → DEGRADED | RESTRICTED | REVOKED`; `DEGRADED → BOUND | RESTRICTED | REVOKED`; `RESTRICTED → BOUND (re-attest) | REVOKED`; **REVOKED** terminal | Attestation; device limit (`LD-MOB-002`); DEGRADED disables offline cache and forces OTP step-up; RESTRICTED wipes offline cache (`LD-MOB-003`; NN-44); events `mob.DeviceBound`, `mob.IntegrityFailed`, `mob.DeviceRevoked`, `mob.OfflineCacheWiped` |
| Capture and upload job (`mob.upload_jobs`) | `CAPTURED (hashes) → AADHAAR_CHECKED (masked if hit) → QUEUED → UPLOADING ⇄ PAUSED → COMPLETING → SERVER_VERIFIED (hash, malware, MIME) → STORED (original immutable; A.18) → RENDITIONS_REQUESTED (P05) → DONE | FAILED (help key; retry) | QUARANTINED` | `LD-MOB-010/011`; NN-04, NN-09 |
| Store purchase (only `digital_sales_mode = IAP`) | `STOREFRONT_SHOWN → PURCHASE_STARTED → STORE_CONFIRMED (client) → SERVER_VERIFIED (App Store Server API / Play Developer API) → ENTITLEMENT_ISSUED (P17 via BILLING_PORT; OH8 notified) → ACTIVE → RENEWED | CANCELLED | REFUNDED | EXPIRED` | Entitlement changes only on server verification (`LD-MOB-017`); `mob.StorePurchaseVerified` |
| OTA release (`mob.ota_releases`) | `DRAFT → APPROVED (maker-checker) → ROLLING_10 → ROLLING_50 → LIVE`; any rolling state → `ROLLED_BACK` (crash regression or manual) | Allowed only when change classification passes (FR-P22-90); signature valid (`LD-MOB-021`); `mob.OtaReleasePublished`, `mob.OtaRolledBack` |

### A.62 Engineering governance: change, release, vulnerability, incident, VAPT, restore test, go-live (P23 §5.1–§5.7)

**Owner:** P23 · schema `eng` (platform scope; staff-only RLS).

| Machine | States and transitions | Guards, clocks and events |
|---|---|---|
| Change record (`eng.change_records`, `chg_`, human ref `CHG-YYYY-NNNNNN`) | `DRAFT → SUBMITTED → ASSESSED → CAB_REVIEW → APPROVED | REJECTED | DEFERRED → SCHEDULED → IMPLEMENTED → PIR_DONE → CLOSED`; `FAILED → ROLLED_BACK | FORWARD_FIXED → PIR_DONE` | ASSESSED needs deterministic risk score and expand-migrate-contract plan (NN-12); CAB quorum and conditional approvals; IMPLEMENTED needs the deploy gate: OH13 `ChangeApproved` matching `(change_id, approval_version)`, two human prod approvers who authored no commits in the release (`LD-ENG-010/011`; NN-18); PIR within 5 BD for high-risk NORMAL, REGULATED and EMERGENCY; `eng.ChangeSubmitted`, `eng.ChangeImplemented`, `eng.DeploymentRefused` |
| Release (`eng.releases`, `rel_`) | `PLANNED → CUT → STAGING_VERIFIED (e2e, DAST, golden archives, performance smoke) → PREPROD_VERIFIED (UAT, migration rehearsal) → RING0 → RING1 (≥ 24 h, no SLO burn) → RING2 → DONE`; any → `HALTED → FIXED → resume` | Portability CI gates (P20 §5.6) and accessibility gate (NN-28); `eng.ReleasePromoted` → `ops.ReleasePublished` via `int` |
| Vulnerability | `NEW → TRIAGED (severity, owner, SLA due) → IN_PROGRESS → FIXED → VERIFIED → CLOSED`; `TRIAGED → RISK_ACCEPTED (expiry ≤ 90 d) → REOPENED`; `FALSE_POSITIVE` with reviewer | SLA breach → CTO and security; Critical breach → owner; `eng.VulnerabilitySlaBreached` |
| Incident | `DETECTED → TRIAGED (severity; clocks started) → CONTAINED → ERADICATED → RECOVERED → NOTIFICATIONS_COMPLETE (CERT-In ≤ 6 h, DPDP Board and affected users, tenants, NeGD, ESPs as applicable) → PIR_DONE → CLOSED` | Notification clocks never pause (G-CLOCK; NN-26, NN-27); countdowns shown as text; `eng.IncidentDeclared`, `eng.IncidentClockWarning`; `SecurityIncidentNotified` copies without personal data [VERIFY Spec name] |
| VAPT engagement | `PLANNED → ROE_SIGNED (scope, empanelment snapshot hash, NDA, DPA, test accounts) → FIELDWORK → DRAFT_REPORT → REMEDIATION → RETEST → FINAL_REPORT → CLOSED` | Findings feed the vulnerability machine |
| Restore test | `SCHEDULED → RUNNING → PASSED | FAILED → TICKETED → FIX_DONE → RETEST_SCHEDULED (≤ 24 h) → PASSED`; `SCHEDULED → MISSED` (counts as failed) | `eng.RestoreTestFailed`; `portability.RestoreTested` via `int` |
| Go-live wave | `READINESS_REVIEW → GO_NO_GO (signatures) → CUTOVER (DNS, legacy 301 map, migration with reconciliation, flags to ring2 in steps) → HYPERCARE (14 days Waves 1–2; 21 days Wave 3) → STEADY_STATE`; no-go returns to READINESS_REVIEW with the blocking list | STEADY_STATE only when FR-P23-54 exit criteria are met; `eng.GoLiveSigned` |

### A.63 Legacy migration run and asset disposition (P00 §5.3–§5.5)

Migration run (`core.migration_runs`, `mig_`): `PLANNED (disposition register signed; DPO approval for personal-data collections) → SNAPSHOT_TAKEN (PITR restore ID + hash; never the live cluster) → EXTRACTED → TRANSFORMED (golden tests) → LOADED (staging schemas only) → RECONCILED (counts, money sums, orphans, null-rate deltas, source-set hash; money delta 0.00 — LD-CORE-040/041) → REVIEWED (defect rate ≤ core.migration.max_defect_rate; maker-checker) → PROMOTED (owner go/no-go; one transaction per entity batch; core.MigrationRunPromoted) | ROLLED_BACK (staging dropped; evidence retained)`.
Asset disposition (`eng.disposition_register`): `DISCOVERED → DISPOSITION_PROPOSED → APPROVED (owner; DPO for personal data) → MIGRATED | REBUILT | ARCHIVED (restore-tested) | RETIRED → SOURCE_DELETED (only with MIGRATED/ARCHIVED evidence; LD-CORE-042) → CERTIFIED` (`core.LegacySystemDecommissioned`). Cut-over runbook and rollback criteria: P00 §5.5 (governs; A.62 go-live wave reuses it for Wave 1).

---

## A.64 Cross-machine invariants (tested in `tests/nn/` and `tests/acceptance/`)

| # | Invariant | Machines | NN |
|---|---|---|---|
| I-01 | An agreement reaches EXECUTED only after A.31 COMPLETED (or wet-ink route) and every A.33 formality RESOLVED or WAIVED | A.30, A.31, A.33 | NN-40 |
| I-02 | No signing request leaves DRAFT for an instrument whose eligibility row is WET_INK_ONLY | A.31 | NN-07 |
| I-03 | A chargeable instrument's signing request cannot reach READY unless its stamp instrument is LOCKED_TO_DOCUMENT | A.31, A.32 | NN-08 |
| I-04 | Ending a delivery grant ends sessions ≤ 60 s, reassigns open items and raises rotation prompts for credentials revealed under it | A.9, A.15, A.55 | NN-16, NN-17 |
| I-05 | A matter cannot close with an OPEN clock or open direction | A.39, A.41, A.42 | — |
| I-06 | A legal clock's due date never moves later because an item is WAITING or ON_HOLD | A.15, A.42, A.46 | G-CLOCK |
| I-07 | An agent principal never appears as actor on an approve, check, sign, pay, send, waive or reveal transition | all | NN-13, NN-43 |
| I-08 | Every transition row has a ledger row in the same transaction; replaying the ledger reproduces state | all | NN-02, NN-45 |
| I-09 | A tenant export and an exit export always complete for the tenant's own data regardless of subscription state | A.22, A.23, A.52 | NN-11, NN-50 |
| I-10 | No `chp` object or event crosses the Consumer Help wall; no `chp` event is mapped by `int` | A.50, A.58 | NN-23 |
| I-11 | A legal hold blocks every purge, deletion and erasure path | A.18, A.20, A.23 | NN-26 |
| I-12 | Approvals bind to a payload digest or version hash; any change invalidates them | A.11, A.30 | NN-18, NN-37 |
| I-13 | A machine whose guard depends on an unverified fact is unreachable while its flag is OFF | A.17 and dependants | NN-38 |
| I-14 | When `lit.sor.mode` or kernel mode names LDC as SoR, LawDocs-side writes for that scope are refused and shown read-only | A.39, A.47, A.48 | NN-47; X-06 |

## A.65 Event index additions and gaps found while compiling

Events named in a phase §5 but missing from its §7.4, registered by X1 in Appendix B §B.4 (owning phase adds them to §7.4 at the next integration; **F1 added** `ai.RunReceived`, `ai.PlanApproved` to P09, `lit.MatterSettled`, `lit.OrderFetched` to P11, `dms.DocumentDeposited` to P04 and `wf.TaskAssigned` to P03 — the P12, P16, P18/P15 items remain with those owners): `ai.RunReceived`, `ai.PlanApproved` (P09); `lit.MatterSettled`, `lit.OrderFetched` (P11); `ipm.DataSheetReady` (P12); `mkp.ChangeRequestRejected` (P16); `dms.DocumentDeposited` (P19 deposit into P04); `wf.TaskAssigned` (Appendix I §I.7; P03 owns `wf.tasks`); `chp.CaseAssigned` (P18 names it; P15 owns `chp`). Aliases retired: `core.KillSwitchChanged`, `agt.KillSwitchActivated/Released`, `int.KillSwitchToggled` → `cfg.KillSwitchEngaged/Released`; `core.FeatureFlagChanged` → `cfg.FlagChanged`; `core.CorrectionEntryApplied` → `core.CorrectionApplied`; `chp.ConflictCheckCompleted` → `chp.ConflictChecked`.

## A.66 Resolutions register (R-A-01 … R-A-21)

**Integration status (F1, 25 Oct 2026):** pointer lines "State machine: Appendix A §A.x governs (Resolution R-A-yy)" and aligned wording were added to P00 §5.6 (R-A-09), P01 §5.5/§5.7/§5.9 (R-A-03, R-A-04, R-A-02), P02 §5.1/§5.2/§7.3 (R-A-05, R-A-06, R-A-21), P03 §5.4/§5.5/§5.7 (R-A-07/08, R-A-09, R-A-01), P04 §5.3/§5.4 (R-A-10, R-A-04), P06 §5.3 (R-A-12), P07 §5.1/§5.2/§5.4 (R-A-13, R-A-14, R-A-06), P08 §5.2 (A.31–A.34), P09 §5.2 and FR-P09-45 (R-A-12, R-A-09) and P11 §5.6/§5.7 (R-A-10, R-A-15). The P13, P17, P18, P19 and P20 sides remain with their owners.

| ID | Conflict | Resolution | Files to align |
|---|---|---|---|
| R-A-01 | P00 Correction Entry vs P03 configuration correction vs P18 master-data change | One machine (A.1); P03 and P18 are variants; `core.CorrectionApplied` canonical | P03 §5.7 (wording); P03 §7.4 edited |
| R-A-02 | P01 vs P19 onboarding invitation states | Canonical A.2 with IDENTITY_VERIFIED, KYB_CONFIRMED, TERMS_ACCEPTED | P01 §5.9 |
| R-A-03 | Credential vs marketplace onboarding | Credential status drives onboarding SUSPENDED | P16 FR-P16-24 |
| R-A-04 | P01 vs P04 nominee release | One claim machine; `nom_` single record; P04 table is a projection | P01 §5.7, §7.2; P04 §5.4, §7.2 |
| R-A-05 | P02 grant vs P18 delivery grant | One machine; `iam.grants` supertype, `sdc.delivery_grants` 1:1 extension; state labels mapped | P02 §5.1, P18 §5.1 |
| R-A-06 | P07 approval steps vs P02 engine | `wf` is the engine; `clm.approval_step` is a projection; `clm.Approval*` are notifications | P07 §5.4, §7.2 |
| R-A-07 | `lgo.waiting_items` vs `wf.items` (X-09) | Read view | P13 §7.2 edited |
| R-A-08 | `tsk_` tasks without a table | `wf.tasks` owned by P03 | P03 §7.2 |
| R-A-09 | Three kill-switch registries and four event names | `cfg.kill_switches`; `cfg.KillSwitchEngaged/Released` | P00 §7.2/§7.4, P09 §7.2/§7.4, P19 §7.4 |
| R-A-10 | Four import machines | `xpt.import_jobs` single machine with `source_kind` | P04 §5.3, P11 §5.6, P12 imports |
| R-A-11 | P17/P01 exit vs P20 exit | P20 machine; others are entry points | — |
| R-A-12 | P06 review request vs P09 QRG | One qualified-review machine | P06 §5.3, P09 §5.2 |
| R-A-13 | Two intake front doors (P07, P13) | `lgo` front door when enabled | P07 §5.1, P13 §5.1 |
| R-A-14 | Agreement states vs Appendix Y #46 | Projection mapping | Appendix I §I.8 |
| R-A-15 | P11 vs P19 ADR referral | One machine owned by P11 | P19 §5.8 |
| R-A-16 | Trademark states vs Appendix Y `ip_status` | Projection mapping | — |
| R-A-17 | Resolution lifecycle not drawn | Compiled from FR-P13-37; kernel definition prevails once pinned | P13 §5 |
| R-A-18 | Service-order identity | `eng_` / `LD-ENG-…`; `LD-ORD-` for OH8 mirrors only | P14 §7.2 note |
| R-A-19 | P18 consumer queue vs P15 case | Queue view mapping | P18 §5.5, §7.4 |
| R-A-20 | No invoice/refund machine | Mirror compiled from FR-P17-46…50 | P17 §5 |
| R-A-21 | P02 vs P18 master-data endpoints | One machine (A.56) | P02 §7.3 |
