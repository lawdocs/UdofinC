# Appendix D — Roles, Personas and Access Control Matrix

> **Status:** Binding. LawDocs Build Prompt Pack v1.0 · 25 October 2026.
> **Used by:** P00 (coarse platform roles), P01 (identity levels, assurance, grant types), P02 (engine, catalogue, SoD), and every functional phase that adds resources (P04–P23). P09 (agents), P13 (governance, HRMS, payroll and POSH roles), P16 (engagement grants), P18 (delivery grants and transparency log), P19 (partner and developer roles, API scopes) and P23 (platform auditors) extend it.
>
> **How to use.** Role codes are binding (conventions §6). Authorisation is enforced server-side on every API call, export, background job, search query, AI retrieval and object-storage presign through Cerbos (D-01); UI trimming is convenience only. The matrices below are the source for generated Cerbos policy tests (§D.8): when a phase adds a resource or action, it adds rows here and in `policies/cerbos/`, and CI fails if a resource kind has no matrix row. Maker-checker actions (§D.7) and SoD rules (§D.9) are registered as data and enforced by the P02 engine. Any change to this appendix is a REGULATED change (P23) reviewed by security and the domain owner.

---

## D.0 Principles

1. **Deny by default; least privilege.** A principal gets only the capabilities of roles granted **in a scope** (tenant, legal entity, branch, department, team, matter, agreement, folder) plus attribute conditions.
2. **RBAC + ABAC.** Roles grant capability families; attributes narrow them (department, assignment, owner, confidentiality, workflow state, legal hold, engagement, identity level, AAL).
3. **Authentication ≠ identity ≠ signing** (NN-03). AAL (how strongly you signed in) and identity level L0–L3 (how well we know who you are) are separate attributes; signing authority comes from P01 signatory authorities and the ESP ceremony (P08).
4. **Separation of duties at person level.** Make and check on the same object version are always different persons, across realms and identities (NN-18; §D.9).
5. **Outsiders by grant only.** LawDocs staff, professionals, external counsel, auditors, counterparties, family, delegates, nominees and agents act only under scoped, time-bound grants the customer controls (NN-17; §D.10). No standing staff access to tenant data.
6. **Never inherited.** No role in a parent tenant, group umbrella or another Infrabyx product confers access to a LawDocs tenant (Ecosystem Spec §4.6).
7. **Agents are makers only** (NN-43); every agent action is on behalf of a sponsor and within the sponsor's rights.
8. **Everything logged.** Grants, role changes, decisions, delegations, reveals, exports, denials of privileged actions and context switches go to the audit ledger (NN-02, NN-45).
9. **Reviewable.** Periodic access reviews with evidence (SOC 2 CC6.2/CC6.3; ISO/IEC 27001:2022 A.5.15–A.5.18; §D.13).
10. **Proportionate, not surveillant.** Access control and outcome metrics, never keystroke, screen, webcam or browsing monitoring (NN-33).

---

## D.1 Personas

| Persona | Role(s) | Context | Success looks like |
|---|---|---|---|
| Ananya, salaried professional renting a flat in Noida | `IND_OWNER` | Needs a rent agreement, keeps property and family papers | First draft in under two minutes on her phone; landlord signs as a guest; stamped and signed copy in her vault's Property folder with renewal reminder |
| Ramesh, retired teacher | `IND_OWNER` with daughter Kavya as `IND_DELEGATE` | Low digital confidence; Hindi first | Kavya uploads and organises; Ramesh approves sends with one tap; large text and voice OTP |
| Kavya | `IND_DELEGATE` (for Ramesh), `IND_OWNER` (own), `IND_GUARDIAN` (son's ward profile) | Manages three spaces | Context switcher always shows whose vault she is in |
| Asha, Ramesh's nominee | `IND_NOMINEE` | Needs papers after an emergency | Release after verified evidence and waiting period; read-only access to the folders Ramesh chose |
| Ravi, landlord | `CP_GUEST` | Signs one agreement | Opens the link, enters an OTP, reviews, comments, signs through the ESP; optional free account |
| Neha, legal executive at an SME | `ORG_LEGAL_MAKER` | Drafts and negotiates 30 contracts a month | Intake queue, templates, redlines, one-click submit; never approves her own |
| Arjun, CFO | `ORG_KMP` (CFO), `ORG_APPROVER` (≤ ₹50 lakh) | Approves commercial terms | Approvals inbox with "Review next", diff, step-up on phone |
| Meera, Head – Legal and the company's only lawyer | `ORG_CLO` | "One CLO instead of a legal team" (D-17, CH-14) | Legal risk dashboard, Vidhi agents preparing drafts as makers, retained advocates for representation |
| Kavita, founder of a startup | `ORG_OWNER` | Sets up the workspace in ten minutes | Discovery from GSTIN, departments from a template, one co-founder added as second approver |
| Rahul, director | `ORG_DIRECTOR`, `ORG_APPROVER` | Signs as the company | Signature requests on mobile; authority recorded from MCA data |
| Sales manager | `ORG_DEPT_HEAD` / `ORG_MEMBER` | Needs an NDA today | "Request legal help" form; status visible; no access to other departments' contracts |
| Advocate Rao, external counsel | `ORG_EXT_COUNSEL` (grant) or `PRO_ADVOCATE` (engagement) | Handles two matters for the company | Sees only assigned matters; privileged labels; time-bound |
| Statutory auditor | `ORG_AUDITOR_RO` (grant) | Contract register and obligations review | Read-only scope, watermarked exports, 90-day grant |
| Vikram, LawDocs relationship manager | `OPS_RM` → `ORG_DELEGATED_MAKER` (delivery grant) | Serves twelve retainer clients | Works as maker in each client; client checker approves; transparency log visible to client |
| Pooja, consumer case manager | `OPS_CONSUMER_CASE_MANAGER` (Consumer Help brand) | Drafts loan and insurance grievances | Ethical wall; never touches lender-client tenants; no outcome promises (NN-23) |
| Sam, onboarding specialist | `OPS_ONBOARDING` | Reviews board resolutions and credentials | KYB queue with maker-checker; SLA 8 working hours |
| Content editor | `PLT_CONTENT_EDITOR` with `PLT_LEGAL_REVIEWER` | Publishes templates and rules | Maker-checker publication; reviewer of record (NN-30) |
| Security officer | `PLT_SECURITY_OFFICER` | Approves break-glass and corrections | AAL3; dual approval; reports to clients within 24 hours |
| Vidhi Contracts agent | `AGT_CONTRACTS` | Prepares first drafts and redline summaries | Maker only; sponsor named; kill switch |

---

## D.2 Role catalogue

**Columns:** Realm (`ld` customer, `ld-staff` staff) · App · MFA (Mandatory = AAL2 for every privileged action; Default = AAL2 offered, required by step-up) · Min level (identity level floor, P01) · Approval (granting needs approval) · Delegable · Seat class [REC to P17].

### D.2.1 Platform (apps/console; realm `ld-staff`)

| Role | Purpose | MFA | Approval | Delegable |
|---|---|---|---|---|
| `PLT_SUPER_ADMIN` | Tenants, providers, platform settings, flags (maker); Correction Entry requests; never approves own | Phishing-resistant passkey (AAL3 for approvals) | Yes (security officer + owner of operating entity) | No |
| `PLT_SECURITY_OFFICER` | Break-glass, Correction approvals, policy ceilings, key policies, access reviews of staff | AAL3 | Yes | No |
| `PLT_SRE` | Infrastructure, migrations, incident operations; no tenant data except via break-glass | AAL3 | Yes | No |
| `PLT_RELEASE_MANAGER` | Promotes signed digests; change records (P23) | AAL3 | Yes | No |
| `PLT_CONTENT_EDITOR` | Templates, clauses, rules, glossary, eligibility rows (maker) | AAL2 | Yes | No |
| `PLT_LEGAL_REVIEWER` | Reviewer of record for legal content (advocate/CS/CA); publishes (checker) | AAL2 | Yes | No |
| `PLT_DPO` | Notices, consent purposes, rights requests, DPIAs, breach decisions | AAL3 | Yes | No |
| `PLT_GRIEVANCE_OFFICER` | Grievance queue and clocks (IT Rules; E-Commerce Rules) | AAL2 | Yes | Yes (to a named deputy) |
| `PLT_AUDITOR_RO` | External or internal auditor of the platform (SOC 2, ISO/IEC 27001/27701/42001, CERT-In-empanelled IS audit and VAPT, DigiLocker annual audit, internal audit): read-only platform audit chains, control evidence (P23 `eng.control_evidence`), access-review packs and configuration snapshots for a named engagement; never tenant content (samples are DPO-redacted metadata); exports watermarked and logged; grant ends with the engagement (`AUDITOR` grant, platform scope); cannot hold any other `PLT_*` role (SoD-34) | AAL2 (AAL3 for exports) | Yes (security officer + owner of operating entity) | No |

### D.2.2 LawDocs delivery and operations (apps/delivery; realm `ld-staff`)

| Role | Purpose | Acts in client tenants through |
|---|---|---|
| `OPS_RM` | Relationship manager; delegated maker for retainer clients | Delivery grant → `ORG_DELEGATED_MAKER` |
| `OPS_PROFESSIONAL` | In-house advocate/CS/CA/tax professional delivering non-reserved services (NN-41) | Delivery grant |
| `OPS_DELIVERY_LEAD` | Assigns RMs and professionals, proposes grants, reviews deliverables, handovers | Proposes; no tenant access without own grant |
| `OPS_ONBOARDING` | Assisted set-up, KYB and credential review queues | Onboarding grant (≤ 30 days) |
| `OPS_CSM` | Customer success; sees aggregates and plan data; no tenant content | None by default; support session on request |
| `OPS_SUPPORT_AGENT` | Tickets (in OH), assisted recovery steps | Support session (client-approved, ≤ 60 min) |
| `OPS_CONTENT_PUBLISHER` | Blog, vlog, landing pages without developers (P21) | None (public content only) |
| `OPS_CONSUMER_CASE_MANAGER` | Consumer Help brand cases (P15) | Case grants inside consumers' PERSONAL tenants under the brand only |
| `OPS_QA_REVIEWER` | Quality review of deliverables; never the client's checker | Delivery grant (read + comment) |

All staff roles: MFA phishing-resistant; approval required; not delegable except `OPS_RM` handover by grant replacement (P02 FR-P02-41).

### D.2.3 Company workspace (apps/web; realm `ld`)

| Role | Purpose | MFA | Min level | Approval | Delegable | Seat |
|---|---|---|---|---|---|---|
| `ORG_OWNER` | Ultimate tenant authority; billing; approves privileged grants; master data | Mandatory | L2 | Yes (second owner or, solo, cooling-off) | No | FULL |
| `ORG_ADMIN` | Users, structure, settings (not owner powers) | Mandatory | L1 | Yes | No | FULL |
| `ORG_CLO` | Chief legal officer: legal routes, legal DoA rows, outsider grants for legal scope, legal dashboards | Mandatory | L2 | Yes | Approvals only (≤ 30 days) | FULL |
| `ORG_LEGAL_MAKER` | Drafts, negotiates, files, submits | Default | L1 | No | Tasks only | FULL |
| `ORG_CHECKER` | Reviews and approves per configured actions | Mandatory | L1 | Yes | Approvals (same role holder) | FULL |
| `ORG_APPROVER` | Authorised signatory / DoA approver within recorded limits | Mandatory | L2 | Yes | **No** (authority is personal, P01) | FULL |
| `ORG_DEPT_HEAD` | Department requests, departmental approvals, own-department access reviews | Default | L1 | No | Approvals | FULL |
| `ORG_MEMBER` | Raises requests, sees own and shared items | Default | L1 | No | — | LIGHT |
| `ORG_DIRECTOR` | Director: approvals and signatures routed by DoA/board; board items (P13) | Mandatory | L2 | Yes | No | LIGHT |
| `ORG_KMP` (+ `kmp_type`) | MD, CEO, WTD, CFO, CS, CLO alias, Manager | Mandatory | L2 | Yes | Approvals | FULL |
| `ORG_BOARD_OBSERVER` | Board or committee observer or invitee (e.g., investor-nominated observer): reads only papers released to observers for a named meeting (`BOARD_OBSERVER` grant); no vote, not counted for quorum, cannot move, second, annotate shared copies or sign minutes; items marked in-camera, interested-director or UPSI-restricted are withheld unless the chair releases them; confidentiality undertaking accepted before first access; view-only and watermarked by default; for listed companies, each UPSI release is recorded in the structured digital database (SEBI (Prohibition of Insider Trading) Regulations 2015, reg. 3(5)) **[LAW] [VERIFY current wording]** | Mandatory | L1 | Yes | No | FREE_GUEST |
| `ORG_EXT_COUNSEL` | Assigned matters/documents (guest grant) | Mandatory | L2 | Yes | No | FREE_GUEST |
| `ORG_AUDITOR_RO` (+ `auditor_type`: `STATUTORY`, `INTERNAL`, `SECRETARIAL`, `COST`, `TAX`, `IS_AUDITOR`, `OTHER`) | Read-only datasets and periods named in an `AUDITOR` grant; watermarked exports; no restricted, privileged, sealed, POSH or credential-vault content unless the owner and `ORG_CLO` release named items; every view logged and visible to the tenant; independence and confidentiality acknowledgement at first sign-in; a statutory auditor's right of access to books of account and vouchers (Companies Act 2013 s.143(1)) is met by granting the requested datasets, and any refusal is a recorded owner decision **[LAW]** | Mandatory | L2 | Yes | No | FREE_GUEST |
| `ORG_DELEGATED_MAKER` | LawDocs RM or engaged professional acting as maker under a grant; ceiling: no approve, sign-as-entity, export, admin | Mandatory | L2 | Yes (client) | No | (counted on delivery side) |
| `ORG_HR_ADMIN` | HR administration in the local HRMS kernel mount (P13 FR-P13-51): establishments, positions, employments, leave policies, HR documents, policy acknowledgements; no pay-run approval; never POSH case content | Mandatory | L1 | Yes | No | FULL |
| `ORG_HR_MAKER` | Prepares HR records and letters (appointment, onboarding, exit) for checking | Default | L1 | No | Tasks only | FULL |
| `ORG_PAYROLL_MAKER` | Prepares pay runs through `infrabyx-labour-rulepack` (components, statutory deductions, arrears); cannot approve | Mandatory | L1 | Yes | No | FULL |
| `ORG_PAYROLL_CHECKER` | Checks and approves pay runs and payroll changes; always ≠ maker (`LD-HR-002`; SoD-31) | Mandatory | L2 | Yes | No | FULL |
| `ORG_POSH_IC_PRESIDING` | Presiding Officer of an Internal Committee (Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 s.4(2)(a)): sealed case area (`hr_posh`), inquiry record, recommendations, annual report | Mandatory (AAL2 every session) | L2 | Yes (owner + one more admin) | No | FULL |
| `ORG_POSH_IC_MEMBER` (+ `ic_member_type`: `EMPLOYEE`, `EXTERNAL`) | Internal Committee member (s.4(2)(b)–(c)); the external member from an NGO or association joins by a `POSH_IC_EXTERNAL` guest grant; sealed area for cases before that IC only | Mandatory | L2 | Yes | No | FULL / FREE_GUEST (external) |

**HR, payroll and POSH roles.** They exist only while `int.eco.ldc.sor_mode.hrms = LOCAL` (the `local_kernel` mount; X-11; P13 FR-P13-51). When LawDocsComply is system of record, these roles are held in LDC and LawDocs shows read-only projections (NN-47, D-10). P13's provisional kernel labels map 1:1 — `HR_ADMIN` → `ORG_HR_ADMIN`, `HR_MAKER` → `ORG_HR_MAKER`, `PAYROLL_MAKER` → `ORG_PAYROLL_MAKER`, `PAYROLL_CHECKER` → `ORG_PAYROLL_CHECKER`, `IC_PRESIDING_OFFICER` → `ORG_POSH_IC_PRESIDING`, `IC_MEMBER` → `ORG_POSH_IC_MEMBER` (closes OI-P13-08). IC composition (senior woman Presiding Officer, at least half women members, one external member; s.4) is a kernel rule, not a role rule. No other role — including `ORG_OWNER`, `ORG_ADMIN`, `ORG_HR_ADMIN`, `ORG_AUDITOR_RO`, LawDocs staff and agents — reads POSH case content (s.16 bars publication or disclosure of complaint and inquiry contents) **[LAW]**; LawDocs staff support the module only on metadata (SoD-33).

### D.2.4 Personal workspace (apps/web, mobile; realm `ld`)

| Role | Purpose | MFA | Min level | Notes |
|---|---|---|---|---|
| `IND_OWNER` | Owns the Personal workspace | Default | L0 to draft, L1 to save | Exports and deletions of own data need no second person (NN-11) |
| `IND_FAMILY_MEMBER` | Shared folders, read or read+upload | Default | L1 | Never sign, share out, delete originals, export all |
| `IND_GUARDIAN` | Acts for a ward profile | Mandatory for changes | L2 + evidence | P01 FR-P01-47 |
| `IND_NOMINEE` | Time-locked read access after release | Mandatory | L2 | P01 FR-P01-49–51 |
| `IND_DELEGATE` | Trusted helper with capability subset | Mandatory | L1 | ≤ 365 days; never sign/pay/delete/share out/export all |

### D.2.5 Counterparties and professionals

| Role | Realm / app | Purpose |
|---|---|---|
| `CP_GUEST` | `ld` guest session | Invited negotiator, signer or witness; shared items only; upgrade to account |
| `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER` | `ld` / work.lawdocs.in practitioner workspace | Independent professionals; credentials verified (P01); client work only via engagement grants |
| `PRO_FIRM_ADMIN` | same | Firm structure, members, firm settings |
| `PRO_FIRM_MEMBER` | same | Firm work per assignment |

### D.2.6 Partners and developers (realm `ld`; P19)

| Role | App | Purpose | MFA | Min level | Notes |
|---|---|---|---|---|---|
| `PRT_ADMIN` | Partner portal (api.lawdocs.in) | Administers a partner organisation (bank, CA/CS network, incubator, channel partner): partner users, partner API clients, onboarding batches; sees invitation outcomes (status only) | Mandatory | L2 (partner KYB, P01) | No tenant data after activation; no revenue share with regulated professionals (`LD-INT-071`); `PARTNER` grant per contract |
| `PRT_OPERATOR` | Partner portal | Submits onboarding batches and tracks invitation status | Mandatory | L1 | Cannot create users or credentials; batches of individuals refused (`LD-INT-072`) |
| `DEV_ACCOUNT` | Developer portal | Docs, sandbox clients, webhook test tools | Mandatory | L0 (verified email) | Production clients only against a tenant owner's maker-checked approval (`int.api_client.create`); the account itself never reads tenant data |

A partner user never acquires a role in a tenant it onboarded except through an ordinary grant that the client approves (SoD-36).

### D.2.7 Agents

`AGT_<NAME>` (roster in Appendix H): service principals per tenant with no standing permissions; act only through `AGENT_DELEGATION` grants from a sponsor with autonomy ceiling L0–L4 set by the tenant within plan limits; capabilities intersect with the sponsor's; never checker, approver or signer (NN-43).

---

## D.3 KMP and director sub-types

`kmp_type` on `ORG_KMP` and positions: `MD`, `CEO`, `WTD`, `CFO`, `CS`, `CLO` (alias of `ORG_CLO` capabilities), `MANAGER` (Companies Act 2013 s.2(53) manager), `OTHER_KMP`. Director type on `ORG_DIRECTOR`: `EXECUTIVE`, `NON_EXECUTIVE`, `INDEPENDENT`, `NOMINEE`, `ALTERNATE`. Designations come from the governance kernel (P13) or LawDocsComply when it is system of record (D-10, NN-47); LawDocs does not keep a competing register. Default homes: MD/CEO executive summary; CFO approvals and spend; CS board items and filings (P13); CLO legal risk dashboard.

---

## D.4 Capability families (used by roles and the custom-role builder)

Capabilities are `<module>.<resource>.<verb>`; verbs: `read`, `create`, `update`, `submit`, `approve`, `sign`, `share_internal`, `share_external`, `send`, `export`, `delete`, `admin`. Custom roles (P02 FR-P02-20) pick from these within their base role's ceiling.

| Module | Resources (examples) | Notes |
|---|---|---|
| `org` | unit, position, restructure | `admin` = structure changes |
| `iam` | member, role_grant, grant, custom_role, delegation, access_review, sso, scim | Grants of approval-required roles need `approve` by a second person |
| `cfg` | setting (by tier), mc_policy, doa_table | Critical settings are catalogue actions |
| `lgo` | intake_request, legal_calendar, legal_spend, counsel_panel | Legal desk |
| `tpl` | tenant_template, clause, questionnaire | Platform templates are read-only to tenants |
| `drf` | draft, ai_draft | AI drafts labelled (NN-14) |
| `clm` | agreement, obligation, renewal | `approve` follows DoA |
| `msg` | thread, deal_room, external_message | `send` external = outside tenant |
| `sgn` | signing_request, stamp_order, evidence_pack | `sign` as entity needs signatory authority |
| `dms` | folder, document, version, share, legal_hold, retention_rule, bulk_import | Originals never `update`/`delete` within retention |
| `dix` | ocr_job, translation, type_copy | Derived renditions only |
| `pld` | pleading, notice | `send` notice is external |
| `lit` | matter, case, hearing, order | — |
| `ipm` | trademark, watch | — |
| `gov` | meeting, resolution, register | Mounted kernel or LDC |
| `hr` | employee, duty, payroll | Mounted kernel or LDC |
| `bsv`, `tax`, `chp` | service order, filing record, consumer case | — |
| `mkp` | order, engagement, retainer, review | Professional rules (NN-21) |
| `bil` | plan, invoice_mirror, payment, refund_request | Engine is OH8 |
| `sav` | value_ledger | — |
| `ai`, `agt` | vidhi_session, agent, mission, autonomy | Autonomy changes are catalogue actions |
| `cvl` | credential_entry, reveal | P18; OFF by default (NN-16) |
| `int` | api_client, webhook, connector, ecosystem_share | — |
| `xpt` | export_job, byo_target, import_job | Tenant export is a catalogue action |
| `core` | audit_view, correction_view, integrity | — |
| `rpt` | dashboard, report | — |

---

## D.5 Permission matrix — Company workspace

**Codes:** R read · C create · U update (draft/own) · S submit · K check/approve · G sign as entity (within authority) · E share/send externally · X export · D delete (soft, non-original) · A administer/configure · — none. **Qualifiers:** *(d)* own department(s) · *(a)* assigned items · *(o)* own items · *(s)* grant scope only · *(lim)* within recorded limits · *(mc)* subject to maker-checker.

| Module / object | OWNER | ADMIN | CLO | LEGAL_MAKER | CHECKER | APPROVER | DEPT_HEAD | MEMBER | DIRECTOR | KMP | BOARD_OBS | EXT_COUNSEL | AUDITOR_RO | DELEGATED_MAKER |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organisation structure | A | A | A (Legal) | R | R | R | A *(d, if allowed)* | R *(d)* | R | R | — | — | R | R *(s)* |
| People, roles, grants | A, K | A *(mc)* | K (legal outsiders) | — | — | — | R *(d)* | — | R | R | — | — | R | — |
| Settings (tenant/entity/dept tiers) | A | A *(mc for critical)* | A (legal areas) | — | — | — | A *(d, delegated)* | — | — | — | — | — | — | — |
| Maker-checker policies, DoA | A, K | C, S | C, S, K (legal rows) | — | — | — | C, S *(d)* | — | R | R | — | — | R | — |
| Legal intake requests | R | R | A, K | C, U *(a)* | R | R | C, R *(d)* | C, R *(o)* | R | R | — | R *(a)* | R | C, U *(s)* |
| Tenant templates and clauses | K (publish) | R | C, U, S, K | C, U, S | K | R | R | R | R | R | — | R *(a)* | R | C, U, S *(s)* |
| Drafts (incl. AI drafts) | R | R | C, U, S | C, U, S *(a)* | R, K *(a)* | R | C *(d)* | C *(o)* | R *(a)* | R *(a)* | — | C, U *(a)* | R | C, U, S *(s)* |
| Agreements (CLM) | R, X | R | C, U, S, K | C, U, S *(a)* | R, K | R, K *(lim)*, G *(lim)* | R *(d)*, K *(d)* | R *(o)* | R, K, G *(lim)* | R, K *(lim)* | — | R, C *(a)* | R | C, U, S *(s)* |
| Negotiation, deal rooms, external messages | R | R | C, U, E | C, U, E *(a, mc if set)* | R | R | R *(d)* | R *(o)* | R *(a)* | R *(a)* | — | C, E *(a)* | R | C, U, E *(s, mc)* |
| Signing requests, eStamp orders | R | R | C, S | C, S *(a)* | K | G *(lim)* | R *(d)* | — | G *(lim)* | G *(lim)* | — | — | R | C, S *(s)* (never G) |
| Legal Vault / DMS (non-restricted) | A, X | A | R, C, U, E | R, C, U *(d)* | R *(d)* | R | R, C *(d)* | R, C *(o)* | R (shared) | R (shared) | R (board folder) | R *(a)* | R *(s)* | R, C, U *(s)* |
| Restricted and privileged folders | A | — (unless member of audience) | A | R *(audience)* | R *(audience)* | — | — | — | R *(audience)* | R *(audience)* | — | R *(a, privileged label)* | — (unless granted) | — |
| Legal holds, retention rules | A *(mc)* | — | C, K | — | — | — | — | — | — | — | — | — | R | — |
| Bulk import (folders) | A | A | C | C *(d)* | — | — | C *(d)* | — | — | — | — | — | — | C *(s)* |
| Document intelligence (OCR, translation, type copy) | R | R | C, U | C, U *(a)* | R | R | C *(d)* | C *(o)* | — | — | — | C *(a)* | R | C, U *(s)* |
| Pleadings and notices | R | R | C, U, S, K, E | C, U, S *(a)* | K | R | R *(d)* | — | R | R | — | C, U, E *(a)* | R | C, U, S *(s)* |
| Litigation matters, cases, hearings | R | R | A | C, U *(a)* | R | R | R *(d)* | R *(o)* | R (summary) | R (summary) | R (summary) | C, U *(a)* | R | C, U *(s)* |
| IP portfolio | R | R | A | C, U *(a)* | R | R | R *(d)* | — | R | R | — | C, U *(a)* | R | C, U *(s)* |
| Governance (meetings, resolutions, registers) — kernel/LDC | R | R | R | — | — | — | — | — | R, K (via meeting) | C, U, S (CS) | R | — | R | C, U *(s, if engaged)* |
| HRMS (client) — kernel/LDC | R | R (directory) | — | — | — | — | R *(d team)* | R *(o)* | R (summary) | R | — | — | R (sample) | — |
| Business services and tax orders | A | R | R | C *(a)* | — | — | C *(d)* | C *(o)* | R | R (CFO: K) | — | — | R | C, U *(s)* |
| Marketplace purchases, engagements | A, K *(mc above threshold)* | C | C, K | C *(a)* | — | K *(lim)* | C *(d)* | — | R | K (CFO) | — | — | R | — |
| Billing, plan, invoices (mirror) | A | R | R | — | — | — | — | — | R | R (CFO: A) | — | — | R | — |
| Savings and value dashboard | R | R | R | R *(d)* | R | R | R *(d)* | — | R | R | R | — | R | R *(s)* |
| Vidhi and agents (use) | U | U | U | U | U | U | U | U | U | U | — | U *(a)* | — | U *(s)* |
| Agents: create, autonomy, kill switch | A, K *(mc)* | C, S | C, S, K (legal agents) | — | — | — | C, S *(d)* | — | — | — | — | — | R | — |
| Credential vault (P18; OFF by default) | A (enable), K (reveal approvals) | — | C (legal portals) | — | — | — | — | — | — | — | — | — | — | Reveal only per credential grant + client approval |
| Integrations, API clients, webhooks | A *(mc)* | C, S | R | — | — | — | — | — | — | — | — | — | R | — |
| Ecosystem sharing (per product, per data type) | A, K *(mc)* | C, S | C, S | — | — | — | — | — | — | — | — | — | R | — |
| Exports and BYO storage | A, K | C, S *(mc)* | C, S (legal scope) *(mc)* | X *(o)* | X *(a)* | X *(a)* | X *(d)* | X *(o)* | X (packs) | X | — | X *(a, watermark)* | X *(s, watermark)* | — (deliverables via P18 only) |
| Audit trail, access log, transparency log | R | R | R | R *(o)* | R *(a)* | R *(a)* | R *(d)* | R *(o)* | R | R | — | — | R *(s)* | R *(o)* |
| Changes made by LawDocs (corrections register) | R, K (acknowledge) | R | R | — | — | — | — | — | R | R | — | — | R | R |
| Reports and dashboards | R | R | R | R *(d)* | R *(d)* | R | R *(d)* | — | R | R | R (board pack) | R *(a)* | R *(s)* | R *(s)* |

**Notes.** (0) `BOARD_OBS` and `AUDITOR_RO` never hold C, U, S, K, G, E or A on any row (SoD-24); their R is limited to the grant's meetings, datasets and periods, and every read is in the tenant's access log. (1) Directors approve via meetings and circular resolutions (P13) unless the tenant configures an inbox step. (2) `ORG_DELEGATED_MAKER` capabilities exist only inside an active delivery or engagement grant and only for the grant's scopes (§D.10); the ceiling excludes K, G, X (except deliverables) and A. (3) `ORG_APPROVER` G is bounded by the signatory authority record (P01 FR-P01-35) and by the DoA route; signing itself happens in the ESP ceremony (NN-06). (4) Every E (external share or send) is an irreversible external action: never executed by an agent without a per-action human confirmation (NN-13).

### D.5.1 HRMS, payroll and POSH (local kernel mount only)

| Object | OWNER | HR_ADMIN | HR_MAKER | PAYROLL_MAKER | PAYROLL_CHECKER | POSH_IC_PRESIDING | POSH_IC_MEMBER | DEPT_HEAD | MEMBER | AUDITOR_RO |
|---|---|---|---|---|---|---|---|---|---|---|
| Establishments, positions, employments | A | A *(mc)* | C, U, S | R | R | — | — | R *(d)* | R *(o)* | R *(s)* |
| Leave, attendance (declared sessions only; NN-33) | R | A | C, U | R | R | — | — | K *(d)* | C *(o)* | R *(s, sample)* |
| HR letters and documents | R | K | C, U, S | — | — | — | — | R *(d)* | R *(o)* | R *(s)* |
| Pay runs and payroll changes | R | R | — | C, U, S | K | — | — | — | R (own payslip) | R *(s)* |
| POSH IC constitution | A *(mc)* | C, S | — | — | — | R | R | — | R (published IC details) | R (constitution only) |
| POSH cases (sealed) | — | — | — | — | — | A *(a)* | R, C, U *(a)* | — | Complainant: own complaint status | — |
| POSH annual report (s.21) | R | R | — | — | — | C, S | C | — | — | R |

### D.5.2 Board and audit access (company)

| Object | BOARD_OBS | AUDITOR_RO (STATUTORY) | AUDITOR_RO (INTERNAL / SECRETARIAL / COST / TAX / IS) |
|---|---|---|---|
| Meeting papers | R *(released items of the granted meeting; view-only, watermarked)* | R *(s)* | R *(s)* (secretarial: all board and committee papers in the period) |
| Minutes and resolutions | R *(granted meeting, after signing; no draft minutes)* | R *(s)* | R *(s)* |
| Statutory registers | — | R *(s)* | R *(s)* |
| Books, invoices, billing mirror | — | R *(s)* (s.143(1)) | R *(s)* |
| Contracts, matters, IP | — | R *(s; privileged items only if released)* | R *(s)* |
| Exports | — | X *(s, watermark)* | X *(s, watermark)* |
| Comments | — | Audit queries in the audit room only | Same |

---

## D.6 Permission matrices — Personal workspace, counterparties, professionals, delivery staff and console

### D.6.1 Personal workspace

| Object | IND_OWNER | IND_FAMILY_MEMBER | IND_DELEGATE | IND_GUARDIAN (ward data) | IND_NOMINEE (after release) | CP_GUEST |
|---|---|---|---|---|---|---|
| Profile, verification, consents | A | — | — | A (ward profile) | — | Own guest record only |
| Vault folders and documents | A, E, X, D | R or R+C *(shared folders)* | R, C, U *(scope)* | A *(ward folder)* | R + download *(scope)* | R *(shared versions only)* |
| Originals | R, download; never overwrite | R *(shared)* | R *(scope)* | R | R *(scope)* | R *(shared)* |
| Drafts and AI drafts | C, U | — | C, U *(scope)* | C, U (ward) | — | — |
| Sharing outside LawDocs / sending | E | — | Prepare only; owner sends (or owner-approval mode) | E (ward, representative capacity) | — | — |
| Signing | Sign own (ESP) | — | — | Sign in representative capacity where the instrument permits [COUNSEL] | — | Sign the shared document (ESP) |
| Payments, marketplace bookings | A | — | Book; owner pays | A (ward) | — | Pay own share if invited to split [P17] |
| Export everything | X (no second person; NN-11) | — | — | X (ward folder) | Download released scope | — |
| Delete | D (non-original; originals per retention) | — | — | — | — | — |
| Who can see my vault | A | R (own access) | R (own access) | R | R | — |

### D.6.2 Professionals (practitioner workspace and client tenants)

| Object | PRO_FIRM_ADMIN | PRO_FIRM_MEMBER | `PRO_*` in a client tenant (engagement grant) |
|---|---|---|---|
| Firm profile, members, firm settings | A | R | — |
| Rule-36 / professional profile fields (if listing ever ON) | A (own) | U (own) | — |
| Engagements list, deliverables, calendar, messages | A | R, C, U *(a)* | R, C, U *(s)* |
| Client documents | — (not in firm workspace by default) | — | R, C, U *(s)*; E only through the client's maker-checker settings |
| Client approvals | — | — | Never K for own deliverables (SoD-13) |
| Invoices and payouts (OH8 via Route) | R | R *(o)* | — |

### D.6.3 Delivery staff (apps/delivery)

| Area | OPS_RM | OPS_PROFESSIONAL | OPS_DELIVERY_LEAD | OPS_ONBOARDING | OPS_CSM | OPS_SUPPORT_AGENT | OPS_CONTENT_PUBLISHER | OPS_CONSUMER_CASE_MANAGER | OPS_QA_REVIEWER |
|---|---|---|---|---|---|---|---|---|---|
| Client list and health (aggregates) | R (own clients) | R (own) | R (team) | R (onboarding) | R | R (ticket context) | — | R (brand cases) | R (assigned) |
| Client tenant content | Only under delivery grant *(s)* | Only under delivery grant *(s)* | Only under own grant | Only under onboarding grant | Support session only | Support session only | — | Case grants (brand) | Delivery grant read + comment |
| Propose delivery/onboarding grants | — | — | C, S | C, S (onboarding) | — | — | — | — | — |
| KYB / credential review queue | — | — | K | C (maker), K (if different person) | — | — | — | — | — |
| Master-data change request (CH-26) | C, S | — | C, S, K (staff checker ≠ maker) | — | — | — | — | — | — |
| Deliverable QA | — | S | K | — | — | — | — | — | K |
| Public content (blog, vlog, pages) | — | — | — | — | — | — | C, U, S (publish per P21 workflow) | — | — |
| Consumer cases (P15) | — | — | — | — | — | — | — | C, U, S *(s)*; never E on the consumer's behalf without the consumer's confirmation | — |
| Credential vault | Reveal per credential grant + client approval only | Same | — | — | — | — | — | — | — |

### D.6.4 Console (apps/console)

| Area | SUPER_ADMIN | SECURITY_OFFICER | SRE | RELEASE_MANAGER | CONTENT_EDITOR | LEGAL_REVIEWER | DPO | GRIEVANCE_OFFICER | AUDITOR_RO |
|---|---|---|---|---|---|---|---|---|---|
| Tenants directory (metadata, masked) | A | R | R | — | — | — | R | R | R |
| Correction Entries | C, S | K | — | — | C (content errata) | K (content errata) | K (privacy) | — | R |
| Break-glass | C (request) | K | C (request) | — | — | — | K (second approver for personal data) | — | R |
| Platform settings and ceilings | C, S | K (security keys) | C, S (infra) | — | — | — | K (privacy keys) | — | R |
| Flags and kill switches | C, S; engage | K; engage | Engage (vendor adapters) | — | — | — | K (privacy-gated) | — | R |
| Templates, clauses, rules, glossary, eligibility rows | R | — | — | — | C, U, S | K (publish; reviewer of record) | R | — | R |
| Notices and consent purposes | R | — | — | — | C (drafting help) | R | A, K | R | R |
| Rights requests and grievances | — | — | — | — | — | — | A | A | R |
| Providers (KYC/KYB, ESP, eStamp, comms, AI) | C, S | K | R | — | — | — | K (data protection review) | — | R |
| Releases, backups, VAPT evidence (P23) | R | A | A | A | — | — | R | — | R |
| Redirect map, website settings | C, S | — | — | — | K | — | — | — | R |
| Professional-rule switches (NN-21) | C, S (counsel opinion attached) | — | — | — | — | K (+ counsel opinion) | — | — | R |
| Revenue-stream and price switches | C, S | — | — | — | — | — | — | — | R (OH8 approver is checker, D-02) |

No console role can read sealed tenant content outside a purpose-specific workflow; no console role can approve its own request.

### D.6.5 Partners and developers

| Area | PRT_ADMIN | PRT_OPERATOR | DEV_ACCOUNT |
|---|---|---|---|
| Partner users and API clients | A | — | — |
| Onboarding batches and invitation status | C, S, R | C, S, R | — |
| Sandbox clients, docs, webhook tester | R | — | A (own) |
| Production API clients | Request only (tenant owner approves) | — | Request only (tenant owner approves) |
| Tenant data | — | — | — |

---

## D.7 Maker-checker action catalogue

**Platform modes:** `LOCKED` (always required; tenant cannot relax; NN-18) · `REQUIRED` (on by default; tenant may tighten) · `DEFAULT_OFF` (tenant may enable). **Checker default** applies unless DoA or tenant policy says otherwise; checker ≠ maker always (SoD-01). AAL minimum is the platform floor.

| Action code | What | Mode | Default checker | AAL | NN / CH |
|---|---|---|---|---|---|
| `bil.refund.request` | Refund to a customer (platform side) | LOCKED | `PLT_SUPER_ADMIN` ≠ maker, then OH8 approver | AAL3 | NN-18, NN-22 |
| `bil.credit_note.request` | Credit or goodwill credit | LOCKED | same | AAL3 | NN-18 |
| `bil.payment.initiate` | Company-initiated payment above `wf.mc.payment_threshold_inr` (marketplace, services, stamp duty pass-through) | LOCKED (company) | `ORG_APPROVER` / CFO | AAL2 | NN-18, NN-22 |
| `bil.price.change` | Catalogue price change (presentation; OH8 engine) | LOCKED | OH8 approver | AAL3 | NN-18 |
| `bil.revenue_stream.switch` | Turn a revenue stream on/off | LOCKED | `PLT_SECURITY_OFFICER` + OH8 | AAL3 | NN-18, NN-39 |
| `mkp.professional_rule_switch.change` | Any commission, fee-share, listing, ranking or % model switch per profession | LOCKED + counsel opinion attached | `PLT_LEGAL_REVIEWER` | AAL3 | NN-21, CH-08, CH-09 |
| `iam.role.grant_privileged` | Grant of an approval-required role | LOCKED | `ORG_OWNER` (≠ grantee, ≠ maker) | AAL2 | NN-18 |
| `iam.role.self_change` | Any change to one's own roles | LOCKED (blocked; second admin) | Another `ORG_ADMIN`/`ORG_OWNER` | AAL2 | SoD-09 |
| `iam.grant.delivery.approve` | Delivery grant for LawDocs staff | LOCKED | Client `ORG_OWNER`/`ORG_CLO` | AAL2 | NN-17 |
| `iam.grant.engagement.approve` | Engagement grant for an independent professional | LOCKED | Client `ORG_OWNER`/`ORG_CLO` | AAL2 | NN-17 |
| `iam.grant.auditor.approve` / `iam.grant.ext_counsel.approve` | Auditor / external-counsel grant | LOCKED | `ORG_OWNER`/`ORG_CLO` | AAL2 | NN-17 |
| `iam.break_glass.start` | Break-glass access | LOCKED (two approvers) | `PLT_SECURITY_OFFICER` + one more | AAL3 | NN-17 |
| `iam.support_session.start` | Support session | LOCKED | Client owner/admin in-app | AAL1 client / AAL3 staff | NN-17 |
| `iam.custom_role.publish` | Publish or change a custom role | LOCKED | Second `ORG_ADMIN`/`ORG_OWNER` | AAL2 | NN-18 |
| `iam.sso.enforce_for_domain` / `iam.scim.enabled` | Enforce SSO, enable SCIM | REQUIRED | `ORG_OWNER` | AAL2 | NN-18 (critical config) |
| `cfg.critical.change` | Any setting marked `maker_checker = Y` in Appendix R | LOCKED | Per registry | AAL2 | NN-18, NN-29 |
| `cfg.mc_policy.change` | Change a maker-checker policy | LOCKED | `ORG_OWNER` | AAL2 | NN-18 |
| `wf.doa.publish` | Publish DoA version | LOCKED | `ORG_OWNER`/`ORG_CLO` | AAL2 | NN-18 |
| `org.master_data.change` | Client master data (name, constitution, registered office, PAN/GSTIN/CIN, signatories, owner) | LOCKED | `ORG_OWNER` (solo rule) | AAL2 | NN-18, CH-26 |
| `core.correction.apply` | Platform Correction Entry | LOCKED | `PLT_SECURITY_OFFICER` (+ client ack for master data) | AAL3 | NN-02, NN-18 |
| `xpt.tenant_export.run` | Full or bulk export of a company tenant | LOCKED (solo rule) | `ORG_OWNER`/`ORG_ADMIN` ≠ requester | AAL2 | NN-11, NN-18 |
| `xpt.byo_target.add` | Add a BYO storage target | REQUIRED | `ORG_OWNER` | AAL2 | NN-18 |
| `dms.bulk_delete` | Delete > `dms.delete.bulk_threshold` items (non-originals) | LOCKED | `ORG_ADMIN`/`ORG_CLO` | AAL2 | NN-18 |
| `dms.legal_hold.release` | Release a legal hold | REQUIRED | `ORG_CLO` | AAL2 | — |
| `dms.retention_rule.change` | Change retention rule | REQUIRED | `ORG_CLO`/`ORG_OWNER` | AAL2 | NN-26 |
| `dms.share.external` | Share outside the tenant | DEFAULT_OFF | `ORG_CLO`/`ORG_CHECKER` | AAL2 | NN-13 |
| `tpl.template.publish` (tenant) | Publish a tenant template or clause | LOCKED | `ORG_CLO`/`ORG_CHECKER` | AAL2 | NN-18, NN-30 |
| `tpl.platform_template.publish` / `rul.rule.publish` / `hlp.term.publish` / `sgn.eligibility_row.publish` | Platform content | LOCKED | `PLT_LEGAL_REVIEWER` (reviewer of record) | AAL2 | NN-18, NN-30 |
| `clm.agreement.approve_for_signature` | Agreement ready for signature | REQUIRED (DoA) | DoA route | AAL2 | — |
| `sgn.request.send_as_entity` | Send a signing request on behalf of the entity | REQUIRED | DoA route / `ORG_APPROVER` | AAL2 | NN-07, NN-08 |
| `sgn.formality.waive` | Waive a required formality (witness, notarisation, registration, board approval) | LOCKED | `ORG_CLO` + reason | AAL2 | NN-40 |
| `pld.notice.send` | Send a legal notice | REQUIRED (company) | `ORG_CLO` | AAL2 | NN-13 |
| `lit.filing.mark_filed` | Record a filing as made | DEFAULT_OFF | `ORG_CLO` | AAL1 | — |
| `agt.autonomy.change` | Change an agent's autonomy level, tools or budget | LOCKED | `ORG_OWNER` (tenant) / `PLT_SECURITY_OFFICER` (platform ceiling) | AAL2 | NN-18, NN-43 |
| `agt.agent.create` | Create an agent | REQUIRED | `ORG_OWNER`/`ORG_CLO` | AAL2 | NN-43 |
| `int.api_client.create` / `int.webhook.create` | Machine access to tenant data | REQUIRED | `ORG_OWNER` | AAL2 | NN-18 |
| `int.ecosystem_share.enable` | Turn on sharing with an ecosystem product | LOCKED | `ORG_OWNER` + DPO contact acknowledgement | AAL2 | NN-24, CH-16 |
| `cvl.enable` / `cvl.reveal` | Enable credential vault; reveal a credential | LOCKED | Enable: a second client admin (`ORG_OWNER`/`ORG_ADMIN` ≠ maker; `LD-CVL-002`; P18 §9 `cvl.enabled`); reveal: client approver where `cvl.per_reveal_approval.default` applies (`LD-CVL-007`) | AAL2 (+5 min) | NN-16, CH-07 |
| `kyc.authority.verify` | Approve authority evidence (staff) | LOCKED | Second `OPS_ONBOARDING`/`OPS_DELIVERY_LEAD` | AAL2 | NN-18 |
| `kyc.nominee.release` | Approve nominee release evidence (staff) | LOCKED | `PLT_DPO`/`OPS_DELIVERY_LEAD` | AAL3 | NN-18 |
| `kyc.notice.publish` | Publish a notice version | LOCKED | `PLT_DPO` | AAL2 | NN-26, NN-30 |
| `cfg.kill_switch.release` | Release (switch back on) a kill switch in the P03 registry `cfg.kill_switches` (R-A-09) | LOCKED | Registry approver ≠ engager (`LD-CFG-050`) | AAL2 | NN-39 (engaging is single-person and immediate) |
| `cfg.flag.enable_gated` | Enable a verification-gated flag (`cfg.flags`) | LOCKED | Flag approver + verification row VERIFIED | AAL3 | NN-38 |
| `web.legal_page.publish` | Publish Terms, Privacy Notice, Grievance, Refund pages | LOCKED | `PLT_LEGAL_REVIEWER` | AAL2 | NN-30 |
| `web.redirect_map.change` (after freeze) | Change redirect map | REQUIRED | `PLT_CONTENT_EDITOR` | AAL2 | NN-31 |
| `org.restructure.apply` | Apply a restructure | REQUIRED | `ORG_OWNER`/`ORG_ADMIN` | AAL2 | — |
| `hr.payrun.approve` | Approve a pay run or payroll change | LOCKED | `ORG_PAYROLL_CHECKER` ≠ maker | AAL2 | NN-18 |
| `hr.posh.ic.constitute` | Constitute or change an Internal Committee | LOCKED | `ORG_OWNER` + second admin | AAL2 | NN-18 |
| `iam.grant.board_observer.approve` | Board-observer grant for a meeting | LOCKED | `ORG_KMP` (CS) or chair's delegate | AAL2 | NN-17 |
| `iam.grant.posh_ic_external.approve` | Guest grant for the external IC member | LOCKED | `ORG_OWNER` | AAL2 | NN-17 |
| `iam.grant.partner.approve` | Partner grant to a tenant | LOCKED | `ORG_OWNER` | AAL2 | NN-24 |
| `gov.papers.release_to_observer` | Release a withheld item to observers | REQUIRED | Chair / `ORG_KMP` (CS) | AAL2 | — |

Phases add rows here with the same columns before their exit gate; `NN-18_catalogue_coverage` fails if a service exposes an action with a catalogue code that has no row.

---

## D.8 Cerbos policy conventions

**Layout.**

```
policies/cerbos/
├─ _schemas/               principal.json, resources/<module>.<resource>.json (JSON Schema; Cerbos schema enforcement ON)
├─ derived_roles/          common.yaml (owner_of_record, assigned_maker, department_member, grant_holder,
│                          checker_eligible, audience_member, guest_of_share, agent_on_behalf)
├─ resources/<module>/     <resource>.yaml  (one resource policy per resource kind)
├─ principals/             (rarely used; break-glass and agent caps only)
├─ scoped/<tenant_id>/     generated from published custom roles (never hand-edited)
└─ tests/                  generated from Appendix D matrices + hand-written edge cases
```

**Naming.** Resource kind `ld:<module>:<resource>` (e.g., `ld:clm:agreement`, `ld:dms:document`); actions = capability verbs (§D.4); policy `version: default`; derived-role names snake_case.

**Principal attributes** (built by `packages/authz` from P01/P02 data on every request, cached ≤ 60 s): `tenant_id`, `brand`, `workspace_type`, `person_id`, `roles[]` with scopes (`{role, scope_type, scope_ids[], valid_to}`), `positions[]`, `departments[]` (with descendants), `legal_entities[]`, `grants[]` (`{grant_id, type, roles, scopes, data_class_max, valid_to}`), `kmp_type`, `identity_level` (L0–L3), `aal`, `auth_age_seconds`, `delegations_received[]` (with delegator person and exclusions), `actor_type` (user, guest, delivery, professional, agent, platform), `agent_sponsor_person_id`, `linked_person_ids[]` (other identities of the same person), `break_glass_id`.

**Resource attributes** (resolved by each module's resolver): `tenant_id`, `legal_entity_id`, `department_id`, `owner_person_id`, `assignee_person_ids[]`, `maker_person_id` (of current version), `version_digest`, `state`, `confidentiality` (`NORMAL`, `RESTRICTED`, `PRIVILEGED`, `BOARD_ONLY`, `SEALED`), `audience_ids[]`, `legal_hold`, `is_original`, `engagement_id`, `value_inr`, `shared_with_share_ids[]`, `brand`.

**Rules of style.**

1. Every resource policy ends with an explicit deny for `SEALED` outside `audience_member` and a deny for writes on `is_original` (NN-09).
2. SoD conditions are expressed once in derived roles (`checker_eligible` = `P.attr.person_id != R.attr.maker_person_id && !(R.attr.maker_person_id in P.attr.linked_person_ids) && !(delegator of P is maker)`) and reused.
3. Grant-scoped access uses the `grant_holder` derived role with `now() < grant.valid_to` — expiry is enforced in policy as well as by the expiry job.
4. Guests (`CP_GUEST`) match only `guest_of_share` on the exact `share_id` and `version`.
5. Agents use `agent_on_behalf`: allowed actions = sponsor's allowed actions ∩ agent tool scope; `approve`, `sign`, `admin` always denied (NN-43).
6. AAL and auth age are conditions on privileged actions (`P.attr.aal >= 2 && P.attr.auth_age_seconds <= 1800` for approve).
7. No policy reads data the principal could not otherwise see; list endpoints use `PlanResources` query plans converted to SQL by `planQuery()`; search and AI retrieval use the same plan (P09).
8. Custom roles compile into tenant-scoped policies under `scoped/<tenant_id>/` from the published role definition; the compiler refuses capabilities above the base role's ceiling [VERIFY Cerbos scoped-policy behaviour for the pinned version; fallback: custom roles expand to base-role + attribute conditions].

**Example (abridged).**

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  resource: "ld:clm:agreement"
  version: default
  importDerivedRoles: [common]
  rules:
    - actions: ["read"]
      effect: EFFECT_ALLOW
      derivedRoles: [department_member, assigned_maker, grant_holder, owner_of_record]
    - actions: ["approve"]
      effect: EFFECT_ALLOW
      derivedRoles: [checker_eligible]
      condition:
        match:
          all:
            of:
              - expr: R.attr.state == "IN_REVIEW"
              - expr: P.attr.aal >= 2 && P.attr.auth_age_seconds <= 1800
              - expr: P.attr.actor_type != "agent"                      # NN-43
    - actions: ["sign_as_entity"]
      effect: EFFECT_ALLOW
      roles: [ORG_APPROVER, ORG_DIRECTOR, ORG_KMP]
      condition:
        match:
          expr: R.attr.value_inr <= P.attr.signatory_limit_inr && P.attr.identity_level >= 2
    - actions: ["*"]
      effect: EFFECT_DENY
      roles: ["*"]
      condition:
        match:
          expr: R.attr.confidentiality == "SEALED" && !(P.id in R.attr.audience_ids)
```

**Testing and change.** Tests are generated from §D.5–§D.6 (one allow and one deny case per cell), plus SoD, expiry, AAL and agent cases; CI runs `cerbos compile` and the test suite; CODEOWNERS = security engineer + domain owner; every privileged decision is logged with policy version and decision ID (Cerbos audit log shipped to the India log store). The PDP runs as a sidecar per API task; if unreachable, requests fail closed (`LD-IAM-500`).

---

## D.9 Separation-of-duties rules

| # | Conflict | Enforcement |
|---|---|---|
| SoD-01 | Maker and checker of the same approval request or object version | **Block** (NN-18) |
| SoD-02 | Delegate approving an item made by the delegator; delegate being the maker | **Block** |
| SoD-03 | Same person through two identities (staff and customer accounts; professional and client director) as maker and checker | **Block** (person-level link) |
| SoD-04 | Correction Entry requester and approver | **Block** |
| SoD-05 | Content maker and publisher of the same template, clause, rule, glossary term or eligibility row | **Block** (NN-30) |
| SoD-06 | Custom-role maker and publisher | **Block** |
| SoD-07 | DoA table maker and publisher | **Block** |
| SoD-08 | Grantee approving their own grant; proposer approving a privileged grant they proposed | **Block** |
| SoD-09 | User changing their own roles (self-elevation) | **Block**; second admin |
| SoD-10 | Maker-checker policy change maker and approver | **Block** |
| SoD-11 | Refund, credit or payout requester and approver | **Block** (NN-22) |
| SoD-12 | LawDocs staff or an engaged practitioner holding any checker, approver, signatory, director or auditor role in a client tenant (delivery-side grants are `ORG_DELEGATED_MAKER` only) | **Block** (D-02, R-064; P18 `NN-17_delivery_never_checker`) |
| SoD-13 | Engaged professional checking or approving their own deliverable | **Block** |
| SoD-14 | Authorised signatory signing as the entity a document they made, above `wf.sod.self_sign_threshold_inr` | **Warn** (tenant may block) |
| SoD-15 | Export requester and approver (company tenant) | **Block** (solo rule P02 FR-P02-34) |
| SoD-16 | Bulk-delete requester and approver | **Block** |
| SoD-17 | Price, revenue-stream or professional-rule switch maker and checker; switch without counsel opinion attached | **Block** (NN-21) |
| SoD-18 | Agent sponsor checking an item the sponsored agent prepared | **Block** by default (`wf.sod.agent_sponsor_cannot_check`) |
| SoD-19 | Agent autonomy change maker and approver | **Block** (NN-43) |
| SoD-20 | Consumer Help case manager role together with any role serving the group's lender or insurer clients | **Block** (NN-23) |
| SoD-21 | Equator case-level role together with a LawDocs client-facing delivery role on overlapping customers (group grant) | **Block** (Ecosystem Spec §4.6) |
| SoD-22 | KYB or credential reviewer maker and checker; reviewer reviewing their own or a declared-related application | **Block** |
| SoD-23 | Nominee-release evidence maker and checker; nominee as reviewer | **Block** |
| SoD-24 | External auditor or board observer with any write capability | **Block** |
| SoD-25 | `ORG_ADMIN` also holding `ORG_AUDITOR_RO` | **Warn**; access-review flag |
| SoD-26 | Release author and production release approver (P23) | **Block** |
| SoD-27 | Kill-switch release maker and checker | **Block** |
| SoD-28 | Credential-vault reveal requester and client approver | **Block** (NN-16) |
| SoD-29 | Professional or RM with a declared relationship (employment, directorship, family) with the client acting as checker or approver | **Block** |
| SoD-30 | Legal-hold release by the person who placed the hold where the matter is contentious | **Warn** (tenant may block) |
| SoD-31 | Payroll maker and payroll checker of the same pay run or change | **Block** (NN-18; `LD-HR-002`) |
| SoD-32 | IC member who is the complainant, respondent, witness or a declared relative of either in a case | **Block** (recusal recorded) |
| SoD-33 | Any non-IC role (owner, admin, HR admin, auditor, LawDocs staff, agent) reading POSH case content | **Block** (`LD-HR-007`) |
| SoD-34 | `PLT_AUDITOR_RO` holding any other `PLT_*` role; `ORG_AUDITOR_RO` holding any maker, checker or approver role in the same tenant | **Block** |
| SoD-35 | Board observer counted for quorum or voting | **Block** |
| SoD-36 | Partner user (`PRT_*`) acting inside a tenant it onboarded without a client-approved grant | **Block** |

Checks run at grant time, request time, decision time, nightly (drift) and in access reviews (P02 FR-P02-36). Tenants may upgrade Warn → Block, never downgrade.

---

## D.10 Grant types

| Type | Grantor / approver | Grantee | Scope | Max duration | Special rules |
|---|---|---|---|---|---|
| `ROLE` | Admin; approval for approval-required roles | Member | Tenant / entity / branch / department / team / matter / agreement / folder | Open or dated | SoD at grant time |
| `DELIVERY` | Client owner/CLO (proposed by `OPS_DELIVERY_LEAD` or created by client) | LawDocs staff (`ld-staff`) | Departments, matter types, agreements | 12 months, renewable by fresh approval | Ceiling: delegated maker; no export except deliverables; transparency log; revocation ≤ 60 s (NN-17) |
| `ENGAGEMENT` | Client owner/CLO on engagement acceptance (P16) | Independent professional | Engagement matter, documents, deal room | Engagement term + read tail (≤ 90 days) | As delivery; never checker of own work |
| `ONBOARDING` | Client owner | `OPS_ONBOARDING` | Set-up screens, imports | 30 days | No document content beyond imports |
| `SUPPORT_SESSION` | Client owner/admin in-app | `OPS_SUPPORT_AGENT` | Named screens, read-only | 60 minutes | Recorded; client notified |
| `BREAK_GLASS` | Two staff approvers at AAL3 | Staff | Declared scope | `core.break_glass.max_minutes` (default 240) | Client report ≤ 24 h; impossible for non-security reasons if `iam.break_glass.prior_consent` |
| `EXTERNAL_COUNSEL` | Owner/CLO | `ORG_EXT_COUNSEL` | Assigned matters/documents | 12 months | Privileged labels |
| `AUDITOR` | Owner (company); `PLT_SECURITY_OFFICER` + owner of operating entity (platform) | `ORG_AUDITOR_RO` / `PLT_AUDITOR_RO` | Datasets, periods (company); evidence room for a named engagement (platform) | 90 days per grant, renewable by fresh approval | Read-only; watermarked exports; `auditor_type`; independence acknowledgement; no sealed, privileged, POSH or vault-credential content unless released per item |
| `BOARD_OBSERVER` | `ORG_KMP` (CS) or chair's delegate | `ORG_BOARD_OBSERVER` | Named meeting(s), released papers | Meeting + 30 days | Confidentiality undertaking; view-only; UPSI release logging for listed companies |
| `POSH_IC_EXTERNAL` | `ORG_OWNER` | `ORG_POSH_IC_MEMBER` (`EXTERNAL`) | IC sealed area | IC term (s.4(3): up to 3 years) | Guest realm `ld`; AAL2 every session |
| `SHARE` | Document owner or authorised maker (maker-checker if set) | `CP_GUEST` or member | Specific versions, deal room | Invitation TTL; until revoked | Shared versions only (NN-37) |
| `FAMILY` | `IND_OWNER` | `IND_FAMILY_MEMBER` | Named folders, R or R+C | Until revoked | — |
| `DELEGATE` | `IND_OWNER` | `IND_DELEGATE` | Folders + capability subset | 365 days | Never sign/pay/delete/share out/export all |
| `GUARDIAN` | Staff evidence review (maker-checker) | `IND_GUARDIAN` | Ward profile | Until ward's majority + handover | — |
| `NOMINEE` | Owner designates; staff verify release | `IND_NOMINEE` | Named scope, read-only | 180 days after release, renewable | Waiting period; owner can cancel |
| `AGENT_DELEGATION` | Sponsor (+ owner for autonomy ≥ L2) | `AGT_*` | Mission scope, tool allow-list, budget | Mission duration | Maker only (NN-43); kill switch |
| `GROUP` | Operations Hub (`group_grant`, both entity heads + DPO) | Infrabyx staff | LawDocs staff-app role; never tenant data | 90 days | Local expiry enforcement; quarterly review |
| `PARTNER` (P19) | Owner | Partner machine client | API scopes | Contract term | `consentref`/`legalbasis` on every call |

All grants: `grt_` IDs, ledgered lifecycle (Appendix A §A.9; P02 §5.1), visible to the tenant owner in "Outsider access" or "Who can see my vault". Storage (Resolution R-A-05): every non-ROLE grant is a row in the supertype register `iam.grants` (P02); `DELIVERY`, `ENGAGEMENT`, `ONBOARDING` and `SUPPORT_SESSION` grants add a 1:1 extension row in `sdc.delivery_grants` on the same `grt_` (P18 FR-P18-11; purposes `RETAINER_DELIVERY`, `ENGAGEMENT_DELIVERY`, `IMPLEMENTATION`, `SUPPORT_SESSION`) and emit `sdc.DeliveryGrant*` events instead of `iam.Grant*`; `packages/authz` resolves both through one interface.

---

## D.11 Assurance requirements by action (platform floors)

| Action class | Min AAL (max auth age) | Min identity level | Notes |
|---|---|---|---|
| Read own workspace, draft, template automation | AAL1 | L0 (L1 to save) | — |
| Share inside LawDocs; negotiate; message | AAL1 | L1 | — |
| Share or send outside the tenant; send signing requests | AAL2 (12 h) | L1 | Agents need per-action human confirmation (NN-13) |
| Sign personally | Per ESP (signer authenticated by ESP) | L1 (tenant may require L2) | NN-06 |
| Sign as the entity | AAL2 (30 min) | L2 + active authority | P01 FR-P01-35 |
| Approve (checker/approver) | AAL2 (30 min) | L1 (L2 for `ORG_APPROVER`) | — |
| Grant roles / approve grants | AAL2 (10 min) | L2 for owner | — |
| Tenant export / BYO target / bulk delete | AAL2 (10 min) | L1 | Solo rule |
| Nominee designation, guardian changes | AAL2 (10 min) | L2 | — |
| Credential reveal (P18) | AAL2 (5 min) | L2 | Client approval |
| Staff privileged approvals, corrections, break-glass, gated flags | AAL3 (5 min) | Staff realm | Phishing-resistant passkeys |

Tenants may tighten any row (Appendix R `iam.stepup.*`), never loosen.

---

## D.12 AI principals and agents

- Vidhi in a user's session acts by token exchange (RFC 8693): `sub` = user, `act` = `svc_vidhi`; permissions = user's ∩ tool scope; retrieval filtered by the user's query plan (P09).
- Agents (`AGT_*`) are per-tenant service principals; each mission runs under an `AGENT_DELEGATION` grant with sponsor, autonomy ceiling (L0–L4), tool allow-list, budget and expiry; agents never hold K, G, A or E without per-action human confirmation (NN-13, NN-43).
- Agents cannot be members of DoA steps, positions with approver roles or access-review reviewer lists (validation at configuration time).
- Kill switches: platform, tenant, agent, mission (NN-39).

---

## D.13 Access reviews and assurance evidence

| Review | Cadence (default) | Reviewer | Evidence |
|---|---|---|---|
| Company tenant roles and members | Quarterly | Department heads; owner for privileged roles | Campaign pack in `99 System Data (CSV and JSON)/Access Reviews/` |
| Delivery, engagement, auditor, counsel grants | Monthly | Owner/CLO | Same; auto-revoke unreviewed |
| Personal workspace sharing | Annual reminder | Owner | "Who can see my vault" acknowledgement |
| LawDocs staff roles (`ld-staff`) | Quarterly | Line managers + `PLT_SECURITY_OFFICER` | `AccessReviewCompleted` to OH (counts); SOC 2 CC6.2/CC6.3; ISO 27001 A.5.18 |
| Group grants | Quarterly | Entity heads + DPO | As staff |
| Break-glass and support sessions | Monthly | `PLT_SECURITY_OFFICER` + `PLT_AUDITOR_RO` | Session reports |
| Privileged console roles | Monthly | Owner of operating entity + security officer | Attestation |
| API clients and webhooks | Quarterly | Tenant owner; platform for partner clients | Client inventory |
| Auditor and board-observer grants | At each grant end and monthly while open | Owner / CS | Grant list with views per auditor; auto-revoke at end date |
| POSH IC roles | On IC term change and annually | Owner + Presiding Officer | Constitution record (no case content) |
| `PLT_AUDITOR_RO` engagements | Monthly | `PLT_SECURITY_OFFICER` | Evidence-room access report |
| Partner and developer accounts | Quarterly | P19 integration owner | Partner user and client inventory |

---

## D.14 Seat classes (recommendation to P17)

`FULL` (makers, checkers, approvers, CLO, admins, owners, KMP), `LIGHT` (members raising requests, directors signing, department heads with limited use), `FREE_GUEST` (counterparties, board observers, external counsel, auditors), `NONE` (agents — metered by AI credits; delivery staff — counted on the retainer). Seat class never changes permissions; plans may limit counts by class [OWNER].

---

## D.15 Sources (accessed 25 October 2026 unless stated)

- Infrabyx Ecosystem Integration Specification v1.1, §4.2 (staff access, SCIM), §4.5 (scopes), §4.6 (group identity, `group_grant`, neutrality wall), §4.7 (external access), §6.23 (`AccessReviewCompleted`).
- LawDocs conventions §6 (role codes), §7 (NN-01…NN-50), §9 (CH-xx).
- R3 LG-007 (no sub-letting of ASP), LG-021–031 (Aadhaar), LG-111–117 (professional rules), LG-167 (proportionate monitoring).
- OWASP ASVS 5.0 access-control requirements [VERIFY chapter numbering]; SOC 2 Trust Services Criteria CC6.1–CC6.3; ISO/IEC 27001:2022 Annex A 5.15–5.18, 8.2.
- Cerbos documentation for derived roles, query planning and scoped policies [VERIFY for the pinned version].
