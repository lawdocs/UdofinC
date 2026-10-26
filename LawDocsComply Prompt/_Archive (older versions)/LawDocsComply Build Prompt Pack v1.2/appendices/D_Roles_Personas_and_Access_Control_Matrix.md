# Appendix D — Roles, Personas and Access Control Matrix (binding)

> LawDocsComply Build Prompt Pack v1.1 · 25 October 2026 (v1.0 of the same date) · Owner: S12 with P01 (identity) and P02 (configuration). Role codes are binding (conventions §6). Authorization is enforced server-side on every API, export, job, AI retrieval and object-storage request through the policy decision point (Cerbos or OPA, D-01); UI trimming is convenience only.

> **v1.2 changes (25 October 2026)**
> - §D.19 v1.2 access rules for business-ID collaboration: principles; permission-matrix rows for stars, team watch, typed conversations (Query, Explanation Request, Guidance Request, Note, Decision), accountability tab and reports, export builder, History tab categories and history export, business-ID lifecycle actions, organisation code, risk register (RiskID), governance register (GovID) and onboarding discovery (§D.19.2; D-51, D-53, D-56)
> - Hierarchy resolution for explanation and guidance requests (§D.19.3); console permissions for Health Check Studio (super admin maker, content checker), business-ID registry, onboarding providers and register snapshots (§D.19.4; D-55); SoD-27 to SoD-32 (§D.19.5)

> **v1.1 changes (25 October 2026)**
> - KMP sub-types GC, MLRO_PO/DD, CSO, CHRO, COO, AA, TREASURER, AIO (§D.16.1; G5 E-05)
> - Roles `ten_legal_user`, `ten_model_validator`, `ten_approving_authority`, `ext_counsel`, `ext_assurer`, practitioner roles; partner roles with alias map to P25 (§D.16.2–D.16.3; D-48)
> - Agent principals with delegation grants and human sponsors (§D.16.4; D-34, NN-41, NN-50)
> - Permission-matrix additions for P25–P28, `OV_AI`, autonomy and custom registers (§D.16.5); SoD-17 to SoD-24 (§D.17)

---

## D.0 Principles

1. **Deny by default; least privilege.** A user gets only the permissions of the roles assigned **in a scope** (tenant, legal entity, department, function) plus attribute conditions.
2. **RBAC + ABAC.** Roles grant action families; attributes narrow them (legal entity, department, function, assignment, sensitivity, workflow stage, period, engagement).
3. **Separation of duties.** Make and check on the same object version are always different people (NN-05); toxic role combinations are blocked or flagged (D.7).
4. **Human accountability.** AI acts only on behalf of a named user and never beyond that user's rights (D.12; NN-14).
5. **No standing privileged access to tenant data** for LawDocs staff; access only via tenant grant (retainer, support session) or break-glass (NN-30).
6. **Time-bound external access** for auditors and supervisors (D-12).
7. **Everything logged.** Grants, role changes, delegations, reveals, exports and denials go to the audit ledger (NN-02).
8. **Reviewable.** Periodic access reviews with evidence (SOC 2 CC6.2/CC6.3; ISO 27001:2022 A.5.15–A.5.18).

---

## D.1 Personas

| Persona | Role(s) | Context | What success looks like |
|---|---|---|---|
| Priya, Compliance Executive at an NBFC-ML | `ten_maker` (Compliance, Returns) | Handles 120 obligations a quarter across RBI, MCA, DPDP | Opens Home, sees 6 items due this week, uploads evidence from email, submits in two clicks; Vidhi pre-fills control notes from last quarter |
| Rahul, Manager – Compliance | `ten_checker` | Reviews submissions of 4 makers | "Review next" flow, side-by-side evidence and actionable, returns with reason codes; never approves his own items |
| Meera, Chief Compliance Officer | `ten_cco` | Reports to Board and RBI | Acknowledges RBI updates the morning after the 20:00 scan, assigns impact; board compliance report in one click |
| Arjun, CEO | `ten_kmp` (CEO) | Wants a 5-minute weekly view | Executive dashboard; KRIs; overdue statutory items; board pack preview |
| Kavita, Independent Director | `ten_board_member` (+ Audit Committee member) | Uses iPad, reads packs | Secure pack, private annotations, eSign circular resolution, annual disclosures with reminders |
| Sanjay, Chief Risk Officer | `ten_kmp` (CRO) | Runs ICAAP and stress tests | Data from Finbyx flows in; runs adverse scenario; exports ICAAP draft to Word for RMC |
| Neha, Company Secretary | `ten_kmp` (CS) | Meetings, minutes, MCA, LODR | Meeting wizard enforces notice rules; Vidhi drafts minutes; registers auto-update |
| Farhan, HR Head | `ten_hr_admin` | 300 employees in 3 States | Payroll maker-checker, labour registers generated, PT/LWF by State rule packs |
| Ritu, GRO | `ten_kmp` (GRO) | Borrower complaints from website widget and Udofin | Clock-driven queue; IO escalation for proposed rejections |
| Vikram, LawDocs Relationship Manager | `dlv_rm` | Serves 12 retainer clients | Works as maker inside each client under grant; client checker approves; messages and drive links per client |
| Ananya, LawDocs Content Analyst | `plt_content_maker` | Converts new directions into question banks | Uploads instrument, Vidhi drafts rows in the family template, edits, sends to checker |
| Ramesh, Statutory Auditor (CA firm) | `ten_external_auditor` | 3-week audit engagement | Time-boxed read access, PBC requests, watermarked exports |
| RBI inspection team member | `ten_supervisor_view` | On-site/off-site inspection support | Read-only scoped view granted by the RE; every access logged |
| Sunita, Secretary of a credit co-operative society | `coop_office_bearer` + `ten_admin` | Small society, limited staff | Society pack terminology; AGM/election calendar; registrar returns |
| Employee | `ten_employee` | Self-service | Payslips, leave, policy acknowledgement, POSH complaint channel |

---

## D.2 Role catalogue

### D.2.1 Tenant roles

| Role code | Description | Shell | HRMS link | Paid seat [REC to P20] | MFA |
|---|---|---|---|---|---|
| `ten_admin` | Client company admin: users, roles, settings, packs, billing | tenant | Optional | Yes | Mandatory (AAL2) |
| `ten_cco` | Chief Compliance Officer / Head of Compliance; tenant legal reviewer | tenant | Required if HRMS on | Yes | Mandatory |
| `ten_maker` | Prepares compliance, uploads evidence, drafts | tenant | Required if HRMS on (internal staff) | Yes | Default on |
| `ten_checker` | Reviews makers' submissions | tenant | Required if HRMS on | Yes | Default on |
| `ten_dept_head` | Department head / VP; assigns, monitors, may check | tenant | Required if HRMS on | Yes | Default on |
| `ten_kmp` (+ subtype) | CEO, MD, WTD, CFO, CRO, CCrO, CCO (alias), CS, CISO, CTO, CIO, DPO, GRO, PNO, IO | tenant / board | Required (designation in HRMS or governance master) | Yes | Mandatory |
| `ten_board_member` | Director (executive, non-executive, independent, nominee) | board | Linked to director master (P06), not HR | Free or low-cost seat [REC] | Mandatory |
| `ten_committee_member` | Member of a committee (may be non-director, e.g., RMC external expert) | board | Director or employee master | Free [REC] | Mandatory |
| `ten_internal_auditor` | Internal audit function (employee or outsourced firm) | tenant | Optional | Yes | Mandatory |
| `ten_external_auditor` | Statutory/concurrent/other external auditor | assurance | No | Free, time-boxed | Mandatory |
| `ten_secretarial_auditor` | Secretarial auditor (s.204) / scrutiniser | assurance | No | Free, time-boxed | Mandatory |
| `ten_is_auditor` | IS/cyber auditor | assurance | No | Free, time-boxed | Mandatory |
| `ten_supervisor_view` | Regulator supervisor read-only (D-12) | assurance | No | Free | Mandatory (strong auth) |
| `ten_hr_admin` | HRMS and labour compliance administrator | tenant | Required | Yes (HR SKU) | Mandatory |
| `ten_payroll_maker` / `ten_payroll_checker` | Payroll preparation / approval | tenant | Required | Yes (HR SKU) | Mandatory |
| `ten_employee` | Employee self-service | selfservice | Required | Per-employee HR pricing | Default on |
| `ten_ic_member` | POSH Internal Committee member (presiding officer flag) | sealed IC workspace | Required (or external member record) | Included | Mandatory |
| `ten_support_agent` | Client support desk agent (L1 tickets) | tenant | Optional | Yes (Grievance SKU) | Default on |
| `ten_viewer` | Read-only management or staff viewer | tenant | Optional | Low-cost [REC] | Default on |
| `ten_integration_admin` | Delegable subset of admin for connectors, webhooks, API clients and storage targets (X-19) | tenant | Optional | Included | Mandatory |
| `ia_contributor` | Co-sourced internal-audit expert (marketplace or firm) who performs assigned steps and workpapers but never owns or signs the audit report (X-19, X-30) | assurance | No | Free, time-boxed | Mandatory |

### D.2.2 Co-operative and marketplace roles

| Role | Description |
|---|---|
| `coop_office_bearer` | President, vice-president, secretary, treasurer, managing-committee member; designation codes `PRESIDENT`, `VICE_PRESIDENT`, `SECRETARY`, `TREASURER`, `MC_MEMBER` *(v1.1, X1)*; term dates from elections (P16) |
| `coop_member` | Society member (self-service: notices, voting, complaints, share records) |
| `coop_returning_officer` | Election officer for society elections (only where by-laws/State rules allow the society to conduct; otherwise the State election authority's officer is recorded as an external party) |
| `mkp_provider_admin` | Marketplace provider firm admin (LawDocs team or third-party firm) |
| `mkp_professional` | Individual professional delivering engagements |
| `mkp_buyer` | Buyer of services (may be non-subscriber) |
| `anon` | Public visitor (website, marketplace browse, health check without account) |
| `lead` | Visitor who has given contact consent (health-check report, enquiry) — CRM record in OH |
| `ext_developer` | Developer-portal account: documentation, sandbox tenant, API keys for sandbox only; no tenant data (X-19) |

### D.2.3 Platform and delivery roles (LawDocsComply operating entity)

| Role | Description | MFA |
|---|---|---|
| `plt_super_admin` | Tenant administration, overrides via Correction Entries, entitlements | Phishing-resistant (FIDO2/passkey), IP allow-list |
| `plt_content_maker` / `plt_content_checker` / `plt_content_publisher` | Regulatory content pipeline | Phishing-resistant |
| `plt_support` | Support desk; support sessions on tenant grant | Phishing-resistant |
| `plt_security_officer` | Security, break-glass approvals, emergency blocks, access reviews | Phishing-resistant |
| `plt_finance` | Reviews Pricing Studio change requests before submission to OH8 (the OH8 approver is the checker, D-28), raises refund/credit-note requests and marketplace payout instructions to OH8; LDC issues no invoices (X-02) | Phishing-resistant |
| `plt_auditor` | Internal assurance of LDC (read-only platform logs, evidence) | Phishing-resistant |
| `dlv_lead` | Delivery team lead (assigns RMs, reviews deliverables) | Phishing-resistant |
| `dlv_rm` | Relationship manager; maker in retainer tenants under grant | Phishing-resistant |
| `dlv_professional` | CA/CS/advocate/analyst delivering engagements | Phishing-resistant |
| `dlv_reviewer` | Internal quality reviewer of deliverables (LawDocs side; never the tenant checker) | Phishing-resistant |
| `plt_web_editor` / `plt_web_publisher` | Website, help-centre and glossary content (scope `web`, `hlp`); no regulatory-content publishing rights (X-19) | Phishing-resistant |
| `eng_cto`, `eng_sre`, `eng_release_manager`, `eng_developer`, `eng_qa`, `eng_compliance_reviewer` | Engineering staff (staff realm, OH13/OH14 role model; P24); developers have no standing production data access | Phishing-resistant |
| `svc_vidhi` | AI service principal (D.12) | n/a (acts on behalf) |

---

## D.3 KMP subtypes

| Subtype | Default dashboard (Appendix C §C.6.2) | Extra permissions |
|---|---|---|
| CEO, MD, WTD | Executive | Approve items routed to "CEO" step; read all modules; board pack |
| CFO | CFO | Return approvals (authorised signatory where designated), ratio and capital module write (assumptions), GST/TDS |
| CRO | CRO | Risk Lab full, risk appetite proposals, KRI thresholds proposals (G tenant) |
| CCrO | Credit | Credit compliance, concentration, CIC submissions approval |
| CCO | CCO | Same as `ten_cco` (alias) |
| CS | CS | Governance full, meeting notices issue, minutes, registers, MCA filings |
| CISO / CTO / CIO | CISO | Data Protection & Cyber full; incident declarations; IS audit responses |
| DPO | DPO | DSR, DPIA, breach workflows |
| GRO, PNO | GRO | Grievance full |
| IO (Internal Ombudsman) | IO | Grievance IO-scope only; independent of handlers |

KMP designation comes from the governance master (P06: appointments with dates, Form DIR-12/MGT-14 references) and HRMS (employee record), and drives role assignment suggestions; the role is granted by `ten_admin` (two-person for KMP roles where tenant enables "privileged role approval").

---

## D.4 ABAC attributes and policy model

**Subject attributes:** `tenant_id`, `roles[]` with `scope` (tenant / legal_entity / department / function), `employee_id`, `department_ids[]`, `function_ids[]`, `kmp_subtypes[]`, `committee_memberships[]`, `sealed_audiences[]` (e.g., `posh_ic:<tenant>`, `vigil:<tenant>`), `delegations[]`, `external_grant` (`basis`, `scope`, `valid_to`, `pii_level`, `export_level`), `engagement_grants[]` (for `dlv_*`), `auth_level` (AAL1/2/3), `session_flags` (support session, break-glass).

**Resource attributes:** `tenant_id`, `legal_entity_id`, `department_id`, `function_id`, `owner_id`, `assignee_ids[]`, `maker_id` (of current version), `sensitivity` (`public`, `internal`, `confidential`, `restricted`, `sealed`), `stage` (workflow state), `risk_rating`, `period`, `regulator`, `is_board_confidential`, `legal_hold`, `engagement_id`.

**Example policy (Cerbos-style, abridged):**

```yaml
resourcePolicy:
  resource: compliance_instance
  version: default
  rules:
    - actions: [read]
      effect: EFFECT_ALLOW
      roles: [ten_maker, ten_checker, ten_dept_head]
      condition:
        match:
          any:
            of:
              - expr: R.attr.department_id in P.attr.department_ids
              - expr: P.id in R.attr.assignee_ids
    - actions: [check_accept, return]
      effect: EFFECT_ALLOW
      roles: [ten_checker, ten_dept_head, ten_cco]
      condition:
        match:
          all:
            of:
              - expr: R.attr.stage == "submitted_for_review"
              - expr: R.attr.maker_id != P.id                      # NN-05
              - expr: not (R.attr.maker_id in P.attr.delegators)  # delegate inherits exclusion
              - expr: R.attr.risk_rating != "High" || P.attr.auth_level >= 2
    - actions: ["*"]
      effect: EFFECT_DENY
      roles: ["*"]
      condition:
        match:
          expr: R.attr.sensitivity == "sealed" && !(R.attr.sealed_audience in P.attr.sealed_audiences)
```

Policies are versioned in the repository, unit-tested (`policy-tests/`), and every decision for privileged actions is logged with policy version.

---

## D.5 Permission matrix — tenant shell

Codes: **R** read · **C** create · **U** update (own/draft) · **S** submit · **K** check/approve · **A** administer/configure · **X** export · **—** none · *(d)* department/assignment-scoped · *(s)* scope-limited by grant · *(o)* own records only.

| Module / object | admin | cco | maker | checker | dept_head | CEO/MD | CFO | CRO | CS | CISO | DPO | GRO | HR admin | IA | ext aud | board | superv. | employee | viewer | dlv_rm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Settings (cfg) T values | A | A (compliance areas) | — | — | A *(d, delegated)* | — | — | — | — | — | — | — | A (HR areas) | — | — | — | — | — | — | — |
| Settings G (tenant) | C,S | K | — | — | C,S *(d)* | — | — | C,S (risk) | C,S (gov) | C,S (cyber) | C,S (privacy) | C,S (grievance) | C,S (HR) | — | — | — | — | — | — | — |
| Users & roles (iam) | A | R | — | — | R *(d)* | R | — | — | — | R | — | — | R (employees) | R | — | — | — | — | — | — |
| Instrument catalogue (add/remove) | C,S | K | R | R | R | R | R | R | R | R | R | R | R | R | R *(s)* | — | R *(s)* | — | R | R *(s)* |
| Tenant overlays (question edits) | C,S | C,S,K | C (propose) | R | C (propose) *(d)* | R | R | R | R | R | R | R | R | R | R *(s)* | — | R *(s)* | — | — | C (propose) *(s)* |
| Upload direction → AI questions (tenant) | C,S | C,S,K | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | C *(s)* |
| Compliance instances | R,X | R,K,X | C,U,S *(d)* | R,K *(d)* | R,K,X *(d)* | R | R *(finance)* | R | R *(gov)* | R *(IT)* | R *(privacy)* | R *(grievance)* | R *(HR)* | R,X | R *(s)* | R (summary) | R *(s)* | — | R | C,U,S *(s)* |
| Evidence | R | R,K | C,U *(d)* | R,K *(d)* | R,K *(d)* | R | R | R | R | R | R | R | R | R | R *(s)*, X *(watermark)* | — | R *(s)* | — | — | C,U *(s)* |
| Exceptions / NA | R | K | C (request) | K (if delegated) | C,K *(d)* | R | — | — | — | — | — | — | — | R | R *(s)* | — | R *(s)* | — | — | C *(s)* |
| Updates (chg) | R | R, ack, assign | R *(d)* | R *(d)* | R, ack *(d)* | R | R | R | R | R | R | R | R | R | — | R (critical) | — | — | R | R *(s)* |
| Tasks (wf) | R (all) | C,R (all) | C,U *(o, assigned)* | C,U | C,U *(d)* | C | C | C | C | C | C | C | C | C | — | — | — | C *(o)* | — | C,U *(s)* |
| Governance: meetings, minutes | R | R | — | — | — | R,K (as chair) | R | — | C,U,S,K (issue) | — | — | — | — | R | R *(s)* | R, sign (as chair), vote | R *(s)* | — | — | C,U *(s)* |
| Statutory registers | R | R | — | — | — | R | R | — | A | — | — | — | — | R | R *(s)* | R (own entries) | R *(s)* | — | — | U *(s)* |
| Policies | R | C,U,K | C (as owner) | K (as reviewer) | C,U *(d)* | R,K (if configured) | — | — | R | — | — | — | — | R | R *(s)* | R, approve via meeting | R *(s)* | R, attest | R | C,U *(s)* |
| DMS | A | R (all non-sealed) | C,U *(d)* | R *(d)* | R,U *(d)* | R | R | R | R | R | R | R | R | R | R *(s)* | R (packs) | R *(s)* | R *(o)* | R (shared) | C,U *(s)* |
| Risk register / RCSA / KRIs | R | R | C (RCSA input) *(d)* | K (RCSA) *(d)* | C,U *(d)* | R | R | A,K | — | C (IT risks) | C (privacy risks) | — | C (people risks) | R | R *(s)* | R (summary) | R *(s)* | — | R | — |
| Risk Lab (capital, ICAAP, stress) | R | R | — | — | — | R,K (approve ICAAP to board) | C,U,K | A,K | — | — | — | — | — | R | R *(s)* | R | R *(s)* | — | — | C,U *(s, if engaged)* |
| Audit (plans, findings) | R | R | R (own findings) | — | R,U (responses) *(d)* | R | R | R | R | R | R | R | R | A | R *(s)* | R (AC members) | R *(s)* | — | — | — |
| Returns & filings | R | R,K | C,U,S (returns team) | K | K *(d)* | R | K (signatory) | R | R | — | — | — | — | R | R *(s)* | — | R *(s)* | — | — | C,U,S *(s)* |
| Data protection & cyber | R | R | C *(d)* | K *(d)* | R *(d)* | R | — | R | — | A | A | — | — | R | R *(s)* | R (summary) | R *(s)* | C (raise DSR on own data) | — | — |
| TPRM / outsourcing | R | R,K | C *(d)* | K *(d)* | C,U *(d)* | R | R | R,K | — | R,K (IT vendors) | R (processors) | — | — | R | R *(s)* | — | R *(s)* | — | — | — |
| HRMS employees | R (directory) | — | R (directory) | — | R *(d team)* | R | R (cost) | — | R (KMP) | — | — | — | A | R (sample) | — | — | — | R *(o)* | — | — |
| Payroll | — | — | — | — | — | R (summary) | R,K (disbursal file) | — | — | — | — | — | A (payroll_maker / payroll_checker roles split) | R (audit sample) | R *(s)* | — | — | R *(o payslip)* | — | — |
| Labour registers & returns | R | R | — | — | — | R | — | — | — | — | — | — | A | R | R *(s)* | — | R *(s)* | — | — | C,U *(s)* |
| POSH IC (sealed) | — | — (counts only, if IC presiding officer shares) | — | — | — | — | — | — | — | — | — | — | — (unless IC member) | — | — | — | — | C (complaint) | — | — |
| Grievance & support | R | R | C (as agent) | — | R *(d)* | R | — | — | — | — | — | A | — | R | R *(s)* | R (stats) | R *(s)* | — | R (stats) | — |
| Vidhi AI | U | U | U | U | U | U | U | U | U | U | U | U | U | U | — | U (board notebook) | — | U (help only) | U | U *(s)* |
| Integrations & API keys | A | R | — | — | — | — | — | — | — | R | — | — | — | R | — | — | — | — | — | — |
| Exports (xpt) | A,X | X (compliance) | X *(o)* | X *(d)* | X *(d)* | X | X | X | X | X | X | X | X (HR, with checker) | X | X *(watermark)* | X (packs) | X *(per grant)* | X *(o)* | — | X *(s)* |
| Billing & plan | A | R | — | — | — | R | R | — | — | — | — | — | — | — | — | — | — | — | — | R *(s)* |
| Audit log viewer | R | R | R *(o)* | R *(d)* | R *(d)* | R | — | — | — | R (security) | — | — | — | R | R *(s)* | — | R *(s)* | — | — | R *(s)* |
| Changes made by LawDocs | R | R | — | — | — | R | — | — | — | — | — | — | — | R | R *(s)* | — | R *(s)* | — | — | R |

Notes: (1) Board members approve via meetings and circular resolutions (P06), not via inbox checker steps, unless the tenant configures a board step. (2) `dlv_rm` permissions exist only inside an active engagement grant and only for the scopes listed in the grant (D.10). (3) Supervisor view never has write, AI or bulk export unless the grant's export level allows watermarked PDFs.

## D.6 Permission matrix — console (platform)

| Area | super_admin | content_maker | content_checker | content_publisher | support | security_officer | finance | plt_auditor |
|---|---|---|---|---|---|---|---|---|
| Tenants directory / 360 | A | — | — | — | R (masked) | R | R (billing) | R |
| Tenant overrides (Correction Entries) | C (request), K (approve others') | — | — | — | — | K | K (billing-related) | R |
| Content: instruments, question banks | R | C,U,S | K | K (publish) | — | — | — | R |
| Excel template registry | A | C,U | K | K | — | — | — | R |
| Regulatory monitor & triage | R | C,U | K | K (broadcast) | — | — | — | R |
| Rule packs | R | C,U,S | K | K (permissive/publish) | — | K (emergency) | — | R |
| Platform settings & bounds | C,S | — | — | — | — | K (security keys) | K (money keys) | R |
| Pricing catalogue | C,S | — | — | — | — | — | K | R |
| Marketplace admin | A | — | — | — | R | — | K (payouts) | R |
| Support sessions | R | — | — | — | C (request) | K (break-glass) | — | R |
| Break-glass | C (request) | — | — | — | C (request) | K | — | R |
| Releases, backups, VAPT | R | — | — | — | — | A | — | R |
| Claims register (NN-19) | C | — | — | — | — | — | — | K (assurance check) |
| Partner network and partner agreements (P25) *(v1.1)* | C,S | — | — | — | R | — | K (commercials) | R |
| Jurisdiction packs (pilot/publish) *(v1.1)* | R | C,U,S | K | K (publish; reviewer-of-record sign-off required) | — | — | — | R |
| AI model registry, platform autonomy ceiling, platform kill switches *(v1.1)* | C,S | — | — | — | — | K (with `eng_ai_lead`) | — | R |
| Region cells for sale and region migrations *(v1.1)* | C,S | — | — | — | — | K | K (commercial) | R |

No console role can read sealed tenant content; no console role can approve its own request.

---

## D.7 Separation-of-duties (SoD) rules

| # | Conflict | Enforcement |
|---|---|---|
| SoD-01 | Maker and checker of the same compliance instance version | **Block** (L, NN-05) |
| SoD-02 | Delegate approving an item made by the delegator, or delegate being the maker | **Block** |
| SoD-03 | Content maker and checker/publisher of the same release | **Block** |
| SoD-04 | Correction Entry requester and approver | **Block** |
| SoD-05 | Payroll maker and payroll checker on the same run; payroll checker and disbursal-file approver (CFO) on runs above threshold | **Block** (four distinct actors where configured, G) |
| SoD-06 | Return preparer and approver/authorised signatory | **Block** |
| SoD-07 | Internal auditor auditing a function they own or worked in during the review period (cooling-off, default 12 months) | **Block** at engagement staffing; warning in profile |
| SoD-08 | Vendor onboarding approver and vendor payment approver (where TPRM links to payments) | **Warn**, tenant may block |
| SoD-09 | `ten_admin` also holding `ten_internal_auditor` | **Warn**; access review flag |
| SoD-10 | IC member who is the respondent or a witness in a POSH case | **Block** for that case (recusal) |
| SoD-11 | Grievance handler acting as Internal Ombudsman for the same grievance | **Block** |
| SoD-12 | RM (`dlv_rm`) as checker in a retainer tenant | **Block** (D-03) |
| SoD-13 | User administering their own roles (self-elevation) | **Block**; second admin required |
| SoD-14 | External auditor with write permissions | **Block** |
| SoD-15 | Same person as policy drafter and final compliance reviewer of the policy | **Block** |
| SoD-16 | Risk owner accepting their own above-appetite risk | **Block** (approver above owner) |

Toxic-combination check runs at role assignment (blocks or warns with reason capture), nightly (drift), and in quarterly access reviews.

---

## D.8 Delegation rules

- Delegation is per user, per source (approvals, tasks, both), time-bound (≤ 90 days, G), depth 1 (a delegate cannot re-delegate).
- The delegate must already hold the permission and scope; delegation never creates new permissions.
- The delegate inherits the delegator's SoD exclusions (SoD-02).
- Actions are recorded as "by {delegate} on behalf of {delegator}"; both receive a summary when the delegation ends.
- HRMS leave approval prompts the employee to set delegation and Away; never automatic.
- Without a delegate, items follow the escalation ladder after `tenant.inbox.away_escalation_hours` (T, default 8 working hours; P1: 1 hour).
- Statutory signatory roles (authorised signatory for a return, DSC holder) cannot be delegated through the app; the alternate signatory must be designated in governance (P06) and hold the role in their own right.

---

## D.9 HRMS link: user ↔ employee ↔ director

- **Users** (`iam.users`) are login identities. **Employees** (`hr.employees`, P13) are people on payroll or contract. **Directors / KMPs** (`gov.persons`, P06) are governance persons (directors are often not employees).
- A user may link to at most one employee record and/or one governance person per tenant. When the HRMS module is enabled, internal-staff roles (`ten_maker`, `ten_checker`, `ten_dept_head`, `ten_kmp`, `ten_hr_admin`, payroll roles) **require** an employee link (G-tenant setting `iam.require_employee_link`, default true when HRMS on).
- **Joiner:** HR creates employee → invites user with suggested roles from department/designation templates → `ten_admin` approves.
- **Mover:** department or designation change in HRMS raises an access-review task: suggested role/scope changes, open items to reassign (preview), effective date.
- **Leaver:** last working day triggers deprovisioning at end of day (T time), reassignment of open items (preview), transfer of ownership of policies/risks, revocation of delegations; account disabled, never deleted (audit).
- **KMP & committees:** designation and committee membership come from governance (P06) and drive board/committee shell access; cessation (resignation, DIR-12) revokes on the effective date.
- **Org data sharing:** people-risk metrics flow from HRMS to ERM (P08) as aggregates; identity-level HR data stays in `hr` (NN-13 for sensitive fields).

---

## D.10 Retainer RM-as-maker and delivery access (D-03, R-072, R-073)

| Element | Rule |
|---|---|
| Activation | A signed retainer engagement (P21) with scope (legal entities, departments, functions, modules, period) creates an **engagement grant**; the tenant `ten_admin` confirms the RM(s) named by LawDocs |
| Role inside tenant | Each named `dlv_rm`/`dlv_professional` receives tenant role `ten_maker` (and optionally `ten_viewer` for wider read) scoped to the grant; badge "LawDocs" on every action and in the Users list |
| Multiple makers | Client may create its own makers for the same items; LawDocs `dlv_lead` may **propose** further makers from the delivery console within the grant scope; each takes effect only after the tenant `ten_admin` approves it (NN-43); the tenant sees and can remove any of them |
| Checker | Always a tenant user (`ten_checker`, `ten_dept_head`, `ten_cco`); workflow validator blocks RM as checker (SoD-12) |
| Admin rights | Never `ten_admin`; may propose settings (`cfg:propose`) if granted |
| Credential vault | Separate per-entry grants by the client admin (D-04); not implied by maker role |
| Messages, drive link, deliverables, invoices | In the delivery console client workspace and mirrored in the tenant's Services area (invoices are issued by OH8 and shown read-only, X-02) |
| Termination | Retainer end or tenant revocation removes access immediately; open items assigned to RMs are reassigned (preview) to tenant users |
| Logging | Every RM action is logged with engagement ID; monthly delivery report generated from the log (P22) |

---

## D.11 External auditor and regulator scopes (D-12)

| Grant field | Values |
|---|---|
| Grantee type | statutory auditor, concurrent auditor, internal auditor (outsourced), secretarial auditor, IS auditor, tax auditor, RBI/SEBI/IFSCA/IRDAI/NHB/NABARD/Registrar inspector |
| Basis code | `STAT_AUDIT`, `CONC_AUDIT`, `SEC_AUDIT_S204`, `IS_AUDIT`, `RBI_INSPECTION`, `SEBI_INSPECTION`, `IFSCA_INSPECTION`, `IRDAI_INSPECTION`, `REGISTRAR_AUDIT`, `OTHER` (with text) |
| Scope | Modules, legal entities, periods, departments; optionally specific folders |
| PII level | `none` (masked), `limited`, `full` (only where basis requires; reason) |
| Export level | `none`, `watermarked_pdf`, `full` (rare; checker approval) |
| Validity | ≤ 90 days; renewal creates a new grant |
| Approval | `ten_admin` + `ten_cco` (two-person) |
| Visibility | Banner "Read-only access for {grantee} until {date}"; grantee sees an access log of their own activity; tenant sees all |
| AI | Disabled for supervisor view by default; auditors may use Vidhi only over the granted scope if the tenant allows |

---

## D.12 AI principal (`svc_vidhi`) scope

- Every AI action executes **on behalf of** a named user with that user's current permissions intersected with the AI tool's allowed actions (NN-14). If the user lacks access, the tool call is denied and Vidhi says so.
- Tool families: `read/search` (permission-trimmed retrieval), `draft` (creates drafts in the owning module), `extract/classify/translate` (on documents the user can read), `schedule` (creates scheduled AI tasks owned by the user). Forbidden: approve, check, sign, file, pay, publish, close, change roles or settings, send external communications (drafts only; a human sends), access sealed data unless the user is in the sealed audience and the tenant enables AI for that class (default off).
- Scheduled agent runs re-evaluate permissions at run time; if the owner is deactivated or loses rights, the schedule suspends and notifies `ten_admin`.
- Tenant-level AI enablement and per-module toggles (G-tenant); per-user opt-out of AI suggestions (T).
- All prompts, retrieved sources, tool calls and outputs are logged (P17) under tenant retention; no training on tenant data (NN-15).

---

## D.13 Seats and licensing interface (recommendation to P20)

Paid seats: `ten_admin`, `ten_cco`, `ten_maker`, `ten_checker`, `ten_dept_head`, `ten_kmp`, `ten_internal_auditor`, `ten_hr_admin`, payroll roles, `ten_support_agent`. Free or included: board and committee members (cap per plan), external auditors and supervisors (time-boxed), IC members, employees in self-service (priced per employee in the HR SKU), viewers (low-cost bundle). Delivery staff in retainer tenants do not consume the client's seats. Final rules are P20's (pricing catalogue data, D-21).

---

## D.14 Access reviews and assurance

| Review | Frequency | Reviewer | Evidence |
|---|---|---|---|
| Privileged tenant roles (`ten_admin`, KMP, payroll, IA) | Quarterly | `ten_cco` + `ten_admin` (other than reviewee) | Signed review record, changes made |
| All tenant users | Semi-annual | Department heads | Attestation per user |
| External grants | At expiry and monthly for active grants | `ten_cco` | Grant log |
| Console roles | Quarterly | `plt_security_officer` + CTO | SOC 2 CC6 evidence |
| Delivery engagement grants | Monthly | `dlv_lead` + client admin attestation (annual) | Grant list |
| SoD drift report | Nightly automated; monthly review | Security / CCO | Exceptions closed or accepted |

Authentication assurance: console and all `dlv_*` users — phishing-resistant MFA (FIDO2/passkeys), device posture where available; tenant admins and KMPs — MFA mandatory (TOTP, passkey, or SMS OTP fallback flagged weaker); others — MFA on by default (tenant may not disable for privileged roles; G bound). Step-up (AAL2 within 10 minutes) for approvals, signing, exports of sensitive scope, credential reveals, Correction Entries and payroll approval. SSO (SAML/OIDC) with SCIM provisioning for enterprise tenants (P01).

---

## D.16 v1.1 role catalogue additions *(v1.1; D-34, D-48)*

### D.16.1 New KMP sub-types (extend §D.3)

| Subtype | Default dashboard | Extra permissions |
|---|---|---|
| GC (General Counsel / Head Legal) | Legal (P26) | Legal matters, notices, counsel engagement and approvals within the authority matrix; privilege downgrade approver (L); Reg 30 litigation materiality proposal |
| MLRO_PO (Principal Officer under PMLA) and DD (Designated Director) | AML | STR/CTR filing tracker (human filing via FIU-IND, NN-08), AML/KYC checkpoints, sealed access to STR working notes (NN-13) |
| CSO (Chief Sustainability Officer) | ESG (P27) | Materiality, ESG KPIs, BRSR disclosure builder, assurance workspace coordination |
| CHRO | People | HR policies, people-risk aggregates, labour compliance approvals (with `ten_hr_admin`) |
| COO | Operations | Operations checkpoints, outsourcing and BCP approvals, branch/establishment register |
| AA (Appointed Actuary — insurers, IFSC Insurance Offices) | Actuarial | Actuarial checkpoints, certifications workflow (human sign), solvency inputs read |
| TREASURER (co-operatives: designation of `coop_office_bearer` per by-laws, §D.2.2; treasury heads elsewhere) | Treasury | Funds and investment register (P16), reserve transfers checklist |
| AIO (AI Officer) | AI governance (P12 `OV_AI`) | AI use-case and model inventory, autonomy-level approvals (with `ten_admin`), kill switches and drills (P02), AI incident register |

### D.16.2 New tenant and external roles

| Role code | Description | Shell | Seat [REC to P20] | MFA |
|---|---|---|---|---|
| `ten_legal_user` | In-house legal team member: notices, matters, contracts (P26) | tenant | Paid (Legal SKU) | Mandatory |
| `ten_model_validator` | Independent validator of models and AI use-cases (RBI draft MRM; `OV_AI`); may not own or develop the model validated | tenant | Paid | Mandatory |
| `ten_approving_authority` | Named approver in an authority/delegation matrix (value-limited approvals for legal spend, contracts, CSR projects, write-offs of legal costs) — an approval capability with value limits, never a checker of their own drafts | tenant | Included with role holder's seat | Mandatory |
| `ext_counsel` | External advocate/firm: sees only assigned matters, exchanges documents, enters hearing updates; no other module (P26) | counsel portal (assurance shell) | Free, per matter | Mandatory |
| `ext_assurer` | ESG / BRSR Core assurance provider: time-boxed, scope-limited read of KPI lineage and evidence; comments; uploads assurance report (P27) | assurance | Free, time-boxed | Mandatory |
| `ext_contractor` *(v1.1, X1)* | Contractor or contract-labour agency user: uploads wage, attendance, PF/ESI challans and licences for its workers at the principal employer's establishments (P13 contractor portal); sees only its own contracts and workers | contractor portal (selfservice shell) | Free, per contract | Mandatory |
| `practitioner_admin` / `practitioner_user` | CS/CA firm managing many client tenants through client-approved grants; maker only (NN-43 applies as for delivery staff); flag `iam.practitioner.enabled` OFF until counsel clears (OI-P01-13) | practitioner workspace | Practitioner plan | Phishing-resistant |

### D.16.3 Partner roles (P25; separate partner organisation type)

| Role code | Description | Access |
|---|---|---|
| `prt_admin` | Partner firm administrator (country content or delivery partner) | Partner workspace: users, agreements, SLAs, scorecard |
| `prt_content_author` *(v1.1, X1)* | Author of jurisdiction-pack content (checkpoints, translations, coverage statements) for a partner firm; formerly P25 `prt_author` | Content plane for assigned jurisdictions only; drafts only; no tenant data |
| `prt_content_reviewer` | Reviewer of record for a jurisdiction pack (formerly P25 `prt_reviewer`); may not review a pack version they authored (SoD-20) | Content plane for assigned jurisdictions only; no tenant data |
| `prt_delivery_professional` | Local professional delivering services to a client (formerly P25 `prt_expert`) | Tenant data only through a client-approved delivery-style grant; maker only (NN-43) |
| `prt_viewer` | Read-only partner staff | Partner workspace read |

### D.16.4 Agent principals (D-34; NN-41, NN-50)

Each Vidhi role agent (VA-01…VA-17 *(v1.1, X1: VA-16 Legal Matters Assistant, VA-17 Sustainability Analyst)*, P17/Appendix AA) is a tenant-scoped principal (`agp_` id; `agt_` remains the id of an agent run) with **no standing permissions**. It acts only through an active `iam.delegation_grants` row (grantor user, skills, scopes, autonomy level, expiry, sponsor) and token exchange; effective permission = grantor's current permissions ∩ skill scopes ∩ autonomy level. Agents at L2+ have a named human **sponsor** (`ten_kmp` or `ten_dept_head` of the area) accountable for their use; sponsor departure suspends the agent's grants. Agents never hold checker, approver, admin, board, auditor or supervisor roles (G-AI, NN-47).

### D.16.5 Permission matrix additions (tenant shell)

Codes as §D.5. Columns: GC · legal_user · MLRO · CSO · AIO · model_validator · approving_auth · ext_counsel · ext_assurer · practitioner · agent (on behalf).

| Module / object | GC | legal_user | MLRO | CSO | AIO | model_validator | approving_auth | ext_counsel | ext_assurer | practitioner | agent |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Legal matters, notices (P26) | A,K | C,U,S | R (AML-related) | — | — | — | K (value-limited) | R,U *(assigned matters)* | — | C,U *(s)* | C (draft only) |
| Contracts & licences (P26) | A,K | C,U,S | — | — | — | — | K (value-limited) | R *(assigned)* | — | C,U *(s)* | C (draft, extraction) |
| Ethics registers (COI, gifts) | R,K | C | R | — | — | — | K | — | — | — | — |
| ESG & CSR (P27) | R | — | — | A,K | — | — | K (CSR projects) | — | R *(s)*, comment, upload report | C,U *(s)* | C (draft, compute via tools) |
| Reports & MIS (P28) | C,X (legal) | C *(d)* | C,X (AML) | C,X (ESG) | C,X (AI) | R | R | — | R *(s)* | C *(s)* | C (draft narrative) |
| AI governance `OV_AI` (P12) | R | — | — | — | A,K | C,U (validation reports), K (validation sign-off) | — | — | — | — | — |
| Autonomy levels & kill switches (P02) | — | — | — | — | A (with ten_admin) | R | — | — | — | — | — |
| Custom registers (P02) | per register | per register | per register | per register | per register | — | per register | — | — | per grant | per skill |
| Global entities `gem` (P25) | R | R | — | — | — | — | — | — | — | R *(s)* | R |

*(v1.1, X1)* **Permission set `rpt.*` (P28 §3).** `rpt.view` (all tenant roles, scoped by data access of the underlying datasets), `rpt.author` (report and pack composers: `ten_cco`, `ten_kmp`, `ten_dept_head`, `ten_internal_auditor`), `rpt.approve` (approver tier configured per report class; never the author — SoD-25), `rpt.freeze` (CS/committee secretary for board and committee packs), `rpt.schedule` (`ten_admin`, report owners), `rpt.embed` (`ten_integration_admin`), `rpt.dataset_admin` (`ten_admin` with P28 semantic layer). Agents hold `rpt.view` and draft-only `rpt.author` on behalf of a user (NN-37, NN-41).

### D.16.6 Persona additions (TM-139, TM-140)

| Persona | Role(s) | Context | What success looks like |
|---|---|---|---|
| Aditi, General Counsel of a listed NBFC | `ten_kmp` (GC) + `ten_legal_user` team | 140 live matters, 300 notices a year, 40 counsel firms | Notice inbox triaged the same day; zero missed limitation dates; quarterly Ind AS 37 provisioning schedule and Reg 30 log generated; counsel scorecards |
| Mohan, branch compliance maker (Jaipur branch) | `ten_maker` scoped to legal entity + location | Shops & Establishments, labour registers, local licences, branch audit points | Sees only branch items; uploads evidence from mobile; licence renewals 60 days ahead |
| Shalini, Chief Sustainability Officer | `ten_kmp` (CSO) | BRSR and CSR for a top-1,000 listed company | KPI owners submit on time; lineage complete for the assurer; BRSR draft generated |
| Imran, AI Officer | `ten_kmp` (AIO) + `ten_model_validator` colleague | Bank-owned NBFC using Vidhi and its own credit models | Model and AI use-case inventory current; autonomy approvals evidenced; quarterly kill-switch drill passed |

## D.17 v1.1 SoD additions *(v1.1)*

| # | Conflict | Enforcement |
|---|---|---|
| SoD-17 | Model developer/owner validating the same model or AI use-case | **Block** |
| SoD-18 | Legal-spend invoice approver who engaged the same counsel for the same matter above the value limit | **Warn**; tenant may block |
| SoD-19 | ESG KPI data owner checking the same KPI value | **Block** |
| SoD-20 | Partner author and reviewer of record on the same jurisdiction-pack version | **Block** |
| SoD-21 | Practitioner or partner professional holding checker/approver/admin in a client tenant | **Block** (NN-43) |
| SoD-22 | Agent sponsor approving the autonomy promotion of their own sponsored agent | **Block** (second approver required) |
| SoD-23 | Person who undoes a change batch they did not create, above 100 items, without CCO approval | **Block** |
| SoD-24 | Applicability challenger deciding their own challenge | **Block** |
| SoD-25 *(v1.1, X1)* | Report or pack author approving the same report definition or pack (P28 `rpt.approve`); person who composed a board pack freezing it | **Block** (author ≠ approver; composer ≠ freezer) |
| SoD-26 *(v1.1, X1)* | Leave requester approving own leave; employee approving own gift/COI declaration (P13, P26) | **Block** |

---

## D.18 Sources (accessed 25 October 2026; renumbered in v1.1)

Companies Act 2013 ss.2(51) (KMP), 203, 204; SEBI LODR 2015 (committee composition); RBI governance directions for NBFCs/banks (CCO, CRO roles) [VERIFY current consolidated instruments]; POSH Act 2013 s.4 (IC composition); RBI Integrated Ombudsman Scheme 2026 and Internal Ombudsman directions [VERIFY]; AICPA SOC 2 Trust Services Criteria CC6 (logical access); ISO/IEC 27001:2022 Annex A 5.15–5.18, 8.2, 8.5; NIST SP 800-63B (authenticator assurance levels); Cerbos documentation (policy model); Infrabyx Ecosystem Integration Specification v1.1 §§4.2, 4.6, 4.7.

---

## D.19 v1.2 access rules for business-ID collaboration *(v1.2; D-51, D-53, D-55, D-56; NN-56–NN-60)*

### D.19.1 Principles

1. **Access follows the item.** Stars, conversations, accountability, history and exports for a CompID, RiskID, GovID, KRI or Control are visible only to principals who can read that item (or instance) under §D.4–§D.5; a business ID the user cannot read behaves as if it did not exist (LDC-CORE-031).
2. **Hierarchy decides who may ask for an explanation.** An Explanation Request flows down the reporting line; a Guidance Request flows up (§D.19.3).
3. **Records, not chat.** Messages are append-only (NN-59); computed accountability timelines can be changed by nobody — a wrong underlying fact (e.g. a wrong assignment date) is fixed only by a Correction Entry (Appendix A §A.2), which then recomputes the timeline with an annotation (NN-60).
4. **No automated people decisions.** Accountability outputs inform human decisions; no role, agent or rule can apply a disciplinary or HR outcome (NN-47).

### D.19.2 Permission matrix additions (tenant shell)

Codes as §D.5. "Item readers" = every principal with **R** on the underlying item.

| Object / action | admin | cco | maker | checker | dept_head | CEO/MD | CRO | CS | IA | ext aud | board | superv. | viewer | dlv_rm | agent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Star / bookmark by ID, labels, personal reminder | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o)* | C,U *(o, s)* | C,U *(o)* | — | C,U *(o)* | C,U *(o, s)* | — |
| Team watch (notify a team on an ID) | C | C | — | — | C *(d)* | C | C (risk) | C (gov) | — | — | — | — | — | C *(s)* | — |
| Conversation — read thread | R | R | R *(d)* | R *(d)* | R *(d)* | R | R | R | R | R *(s)* | R (Board items, summary) | R *(s)* | R | R *(s)* | R (to draft) |
| Conversation — Query, Note | C | C | C *(d)* | C *(d)* | C *(d)* | C | C | C | C | C (Query only) *(s)* | C (via CS) | — | — | C *(s)* | — (drafts only) |
| Conversation — raise Explanation Request | — | C | — | C (to own makers) | C *(d)* | C | C (risk) | C (gov) | C (audit queries) | — | C (via Chair/CS) | — | — | — | — |
| Conversation — raise Guidance Request | C | C | C | C | C | — | C | C | — | — | — | — | — | C *(s)* | — |
| Conversation — Decision message | — | C | — | — | C *(d)* | C | C (risk) | C (gov) | — | — | C (Board decisions, via CS) | — | — | — | — |
| Respond to an Explanation Request addressed to me | C | C | C | C | C | C | C | C | — | — | — | — | — | C *(s)* | — (drafts only) |
| Resolve / accept an explanation | — | K | — | — | K *(d)* | K | K (risk) | K (gov) | K (audit) | — | — | — | — | — | — |
| Accountability tab (instance timeline) | R | R | R *(o)* | R *(o)* | R *(d)* | R | R (risk) | R (gov) | R | R *(s)* | — | R *(s)* | — | R *(o, s)* | — |
| Add explanation to my own accountability record | C *(o)* | C *(o)* | C *(o)* | C *(o)* | C *(o)* | C *(o)* | C *(o)* | C *(o)* | — | — | — | — | — | C *(o)* | — |
| Non-compliance / risk / governance accountability report | R,X | R,X,A | — | — | R,X *(d)* | R,X | R,X (risk) | R,X (gov) | R,X | R *(s)* | R (summary in pack) | R *(s)* | — | — | — |
| Export builder (list exports, grouping, schedule) | X,A | X,A | X *(d)* | X *(d)* | X,A *(d)* | X | X (risk) | X (gov) | X | X *(s)* | — | X *(s)* | — | X *(s)* | — |
| History tab — content, status, evidence, review categories | R | R | R *(d)* | R *(d)* | R *(d)* | R | R | R | R | R *(s)* | R (summary) | R *(s)* | R (content and status only) | R *(s)* | — |
| History tab — assignment, conversation, export, AI categories; actor names | R | R | R *(d)* | R *(d)* | R *(d)* | R | R (risk) | R (gov) | R | R *(s)*, names per grant | — | R *(s)*, roles not names unless grant allows | — | R *(s)* | — |
| History export (with optional s.63 certificate) | X | X | — | — | X *(d)* | — | X (risk) | X (gov) | X | X *(s)* | — | X *(s)* | — | — | — |
| Retire / merge / split / alias a tenant business ID | K | K | — | — | C,S *(d)* | — | C,S (risk) | C,S (gov) | — | — | — | — | — | — | — |
| Organisation code (before lock) | A | R | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Risk register (RiskID) — list, drawer, import | R,X | R,X | R *(d)* | R *(d)* | C,U *(d)*, X | R | A,K | R | R,X | R *(s)* | R (Board risk view) | R *(s)* | R | C,U *(s)* | C (draft) |
| Governance register (GovID) — list, drawer, import | R,X | R,X | C,U *(d)* | K *(d)* | R *(d)* | R | R | A,K | R,X | R *(s)* | R (Board items) | R *(s)* | R | C,U *(s)* | C (draft) |
| Onboarding discovery and prefill confirmation (P01 §4H) | A | R | — | — | — | — | — | — | — | — | — | — | — | C (assisted onboarding) *(s)* | — |

Personal stars are private: no role, including `ten_admin`, can see another user's stars; external auditors and supervisors with a grant see star *counts* only, never who starred.

### D.19.3 Hierarchy resolution for conversations

"Superior" of the person who holds an item is resolved in this order, and the first non-empty set is used: (1) the HRMS manager chain (P13) when the user is linked to an employee record; (2) the head of the user's org unit and the heads of its parent units (`core.org_units`); (3) the department head of the item's department; (4) the accountable owner on the item's RACI. In every case the CCO and the CEO/MD are superiors for compliance items, the CRO for risk items and the CS for governance items. Board members and committee chairs raise requests through the CS (the CS posts on their behalf, labelled "on behalf of the Chair"). Explanation Requests may be addressed only to people below the requester in this hierarchy or to people on the item's RACI; Guidance Requests may be addressed to any superior, the item's checker, the CCO, the CRO (risk) or the CS (governance); the default route for a Guidance Request is checker → department head → CCO (tenant-configurable, `cmp.conversation.guidance_route`). Delivery staff (`dlv_rm`) appear in the hierarchy only within their delivery grant and never as superiors of tenant staff.

### D.19.4 Console permissions (platform)

| Object / action | plt_super_admin | plt_content_maker | plt_content_checker | plt_content_publisher | plt_security_officer | plt_web_editor | plt_auditor |
|---|---|---|---|---|---|---|---|
| Health Check Studio — build sets by CompID (sections, number of questions, which CompIDs, weights, order, plain-language wording, family) | C,U,S (maker) | C,U (wording proposals) | K (checker) | publish after K | — | U (page copy only) | R |
| Health-check set versions, retire, roll back | C,S | — | K | publish | — | — | R |
| Business-ID registry (platform IDs): instrument codes, retire/merge/split/alias | R | C,S | K | — | — | — | R |
| Organisation codes (all tenants) | R; change before lock only on tenant request | — | — | — | R | — | R |
| Onboarding provider order and enablement (`int` ports) | C,S | — | — | — | K | — | R |
| Register snapshot sign-off (held snapshots) | — | C (upload, review) | K | — | — | — | R |
| History of platform IDs (content chain) | R | R | R | R | R | — | R,X |

### D.19.5 SoD additions

| # | Conflict | Enforcement |
|---|---|---|
| SoD-27 | Person who built or edited a health-check set version publishing (checking) the same version | **Block** (super admin is maker; `plt_content_checker` checks) |
| SoD-28 | Requester and approver of the same retire, merge, split or alias action on a business ID | **Block** |
| SoD-29 | Addressee of an Explanation Request accepting or resolving that request | **Block** (requester or a superior resolves) |
| SoD-30 | Person attributed in an accountability record deciding the outcome for that record | **Block** (decision by a superior or the CCO) |
| SoD-31 | Content maker who uploaded a held register snapshot signing it off | **Block** |
| SoD-32 | Person who proposed an onboarding provider-order change approving it | **Block** (`plt_security_officer` approves) |
