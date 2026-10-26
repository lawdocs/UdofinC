# Appendix AD — Group Companies and Cross-Functional Operations (v3.0, 23 October 2026)

> **Binding** for P21 (Group Operations, Integrations and Portability) and for the v3 addenda it lists for P00, P01, P03, P09, P14, P16 and P18. Read with master NN-03, NN-15, NN-16, NN-22, NN-28 and the v3 rules NN-33, NN-35, NN-36, NN-37, **NN-38 (group boundaries)**, NN-39 and NN-40; decisions D3-02 (Operations Platform as the group-ready "Infrabyx Work OS" engine, Equator first), D3-03 (HRMS and payroll), D3-05 (professional registry as a group shared service under a Group Data-Sharing Agreement), D3-06 (default departments); Appendix D §D.7 (group-company connectors), Appendix O §2.10 and LR-CORP-001 (related-party referral), Appendix Q (fiduciary roles, processors, transfer register), Appendix S §6 (RBAC/ABAC, conflict index, SoD). Companion: **Appendix AC** (workspace, integrations, portability).

## AD.0 Purpose, sources, precedence

### AD.0.1 Purpose
Management said staff "work cross-functionally for Finbyx and Udofin" and that "dashboards, content and data should be shareable under controls". This appendix turns that into a model the coding agent can build without weakening Equator's neutrality: a **group** of separate **legal entities**, each a separate data fiduciary and employer, using **shared services** (Operations Platform engine, HRMS, professional registry, knowledge base, IT workspace) with **per-entity data partitions**; cross-company access only through **purpose-bound, time-limited role grants** under a **Group Data-Sharing Agreement (GDSA)**; employment through one **employer of record** with recorded secondments; related-party and inter-company agreements tracked for Companies Act 2013 s.188; **ethical walls** so a person who works on the lender side never touches an Equator case involving that lender; and a **referral model** between Equator, Finbyx, Udofin and registry advocates that always runs on the party's own authorisation. **Case and allocation data are never shared with Finbyx or Udofin** (NN-38).

### AD.0.2 Sources
**[RE]** F4.4 (directory across group companies; no intra-group exemption under DPDP), F5.1 (employee data across group entities; s.7(i) is the employer's ground; s.8(2) processors), F5.2 (s.2(76), G.S.R. 464(E), s.188 mechanics, inter-company service agreements, GST on secondment — *CCE v Northern Operating Systems*, CBIC Instruction 05/2023-GST), F5.3 (Labour Codes in force 21 Nov 2025; secondment letter contents; ethical walls), design implications D17–D23 and E24–E27. **[RC]** E-31 (one legal employer per contract; one PAN cannot have two active employments within the group without a secondment record), F3 (EPF wage ceiling and rates — parameters owned by P18). **[RD]** F7.3 (books accessible in India, audit trail; internal audit and CARO thresholds per company — configurable facts), DI-F36 (Compliance Cockpit per group company). **[RB]** RB-23 (marketing consent per channel and per group company). Pack: Appendix D §D.7; Appendix O §2.10 and master X-29 (related-party treatment of the Institute referral); Appendix S §1.3, §6.5, §6.7.

### AD.0.3 Precedence
Master → Appendix G → Appendix F (names; `grp` DDL here is additive) → Appendix A → P21 → this appendix → others. Where this appendix and P18 (HRMS) both describe secondment, **P18 is canonical for HR and payroll columns and calculations**; this appendix is canonical for the group-facing columns (host entity, cost recharge, grant linkage) and adds them by additive migration if P18 has already created `hr.secondments`. Where this appendix and Appendix D §D.7 differ on what may flow to Finbyx or Udofin, X-64 applies.

### AD.0.4 Registrations for 02 and master §15

| Kind | ID | Text | Where specified | Status |
|---|---|---|---|---|
| Requirement | **R-68** | Multi-company group operations: staff working cross-functionally for Equator, Finbyx, Udofin and other group companies; dashboards, content and data shareable under controls; separate data, exports and audit per legal entity; handoffs and referrals (e.g., award execution, NPA recovery suits) between group businesses and registry professionals | App. AD; P21 §4E–4H | S+L (CS to confirm shareholding chain and related-party status) |
| Decision | **D3-42** | **Group model.** Schema `grp`: group → legal entities → brands, billing profiles, policies, administrators; `group_admin` (group scope, no data access by default) vs `entity_admin` (one entity); shared services run by a named provider entity as **processor** for the consuming entities under an intra-group processing agreement, with every shared-service row partitioned by `legal_entity_id` and RLS; cross-company access only by `grp.cross_company_grants` (purpose, data categories, scope, default 90 days with a per-role maximum ≤ 365, approver from the target entity, auto-expiry, access log) under an active GDSA; one employer of record per employee with `hr.secondments` for host-entity work; inter-company agreements and related-party flags tracked for s.188; ethical walls enforced at grant and assignment; referrals only on the party's authorisation; Equator case, neutral and allocation data never leave Equator's partition for a group company | App. AD | Decided (counsel and CS items open) |
| Cross-file | **X-64** | **NN-38 versus Appendix D §D.7 Finbyx/Udofin connectors.** D.7 sends case-status, settlement, award and escrow events to "Finbyx". Resolution: those events go only to the **lender tenant's own endpoint** (the lender is a party and is entitled to its own case data, as with any enterprise API, P09); where the lender's LOS/LMS is hosted by Finbyx, Finbyx receives them **as the lender's processor** under the lender–Finbyx contract, not as an Infrabyx group company: the payload is limited to the lender's own case, the subscription is created and owned by the lender tenant admin, Finbyx staff access is governed by the lender's processor terms, and no Finbyx group dashboard, analytics or other client may read it (CI test `GROUP_SHARE_SCOPE`); allocation, neutral-selection and counter-party data are never in the payload (already D.7). The same applies to Udofin as an LSP for a regulated entity | App. D §D.7; App. AD §AD.11 | Resolved |

### AD.0.5 Reconciliations with sibling v3 appendices (apply; record in `docs/adr/`)

| # | Topic | Conflict | Resolution |
|---|---|---|---|
| AD-R1 | Entity registry names | Appendix X uses `grp.companies` / `company_id` (Equator = `company_code 'EQR'`); Appendix Z uses `hr.legal_entities` / `legal_entity_id`; Appendix AE uses `grp.legal_entities` | **`grp.legal_entities` is the single registry.** `grp.companies` is a view over it (`company_code` = `short_code`; Equator's short code is `EQR`); `company_id` (X, Y) and `legal_entity_id` (Z, AE, AC) both hold `grp.legal_entities.id`. `hr.legal_entities` (Z) is the employer profile of the same entity (TAN, EPF establishment code, ESI code): its `id` is a foreign key to `grp.legal_entities.id` and identity columns (legal name, CIN, PAN, GSTIN, registered office) are read from `grp`. Because P18 runs before P21, the P21 migration creates `grp.legal_entities` rows with the existing `hr.legal_entities` IDs and then adds the foreign key |
| AD-R2 | Entity RLS helper | Appendix Z defines `rls.enable_entity_rls(p_schema, p_table)`, setting `app.entity_ids` and policy `entity_scope`; Appendix X defines `ops_company_isolation` in the Operations Platform database | Both are kept and are canonical for their schemas. This appendix adds no second helper: cross-company grants work by the policy engine **computing** `app.entity_ids` (and X's acting company) per request from the home entity plus the target entities of active grants whose `modules` cover the module being served (AD §AD.4.2) |
| AD-R3 | Secondment columns | Appendix Z `hr.secondments` already holds `host_entity_id`, `recharge_basis`, `s188_ref`, `gst_review_status`, `signed_document_id`; `hr.assignments.allocation_pct` holds allocations | Z is canonical; this appendix adds only `icsa_id`, `grant_template`, `wall_schedule` (additive migration) and uses Z's allocations and timesheets for recharges |
| AD-R4 | Grant duration | Appendix X §X.2.4 allows shared-queue grants of ≤ 12 months, renewable | Default 90 days; per-role maximum in `grp.grantable_roles.max_duration_days` up to **365** for shared-desk purposes, with monthly review |
| AD-R5 | Ethical-wall error codes | Appendix X uses `OPS_ETHICAL_WALL` for support tickets | `OPS_ETHICAL_WALL` is the Operations Platform specialisation of `GRP_ETHICAL_WALL_CONFLICT`; both read the same wall data (AD §AD.10) |
| AD-R6 | Books of record | D3-30 (Appendix Z) places the general ledger in Tally or Zoho Books | `grp.legal_entities.books_sor` records the tool per entity; Equator ledgers are sub-ledgers (Appendix AC §AC.11.5) |

## AD.1 Principles

| # | Principle | Source | Enforcement |
|---|---|---|---|
| GP-01 | **Each company is a separate legal person, employer and data fiduciary.** Group membership grants no data access. | NN-38; RE F4.4, F5.1 (DPDP Act has no intra-group exemption; s.7 lists specific legitimate uses only) | RLS by `legal_entity_id`; default-deny |
| GP-02 | **Shared services are processing, not pooling.** A service run by one entity for others processes each entity's data on that entity's instructions in its own partition. | DPDP s.8(2) (processor under a valid contract) [RE F4.3] | `grp.shared_services` + `grp.processing_agreements`; partition key mandatory |
| GP-03 | **Cross-company access is an exception with a purpose, an end date and an approver from the data-owning entity.** | NN-38 | `grp.cross_company_grants`; Cerbos `grant` condition |
| GP-04 | **Equator's neutrality outranks group convenience.** Case, neutral, allocation, caucus and Equator party data never reach Finbyx, Udofin or any other group company; lender-side professional performance notes never reach Equator's neutral systems. | NN-16, NN-28, NN-38; RE F4.4 D23 | CI test `GROUP_SHARE_SCOPE`; no join path between `grp` sharing views and `core` case tables |
| GP-05 | **People carry walls.** A person exposed to a lender's or employer's affairs in a group company cannot handle Equator matters involving that organisation. | RE F5.3; Appendix S §6.5 | `grp.ethical_walls` → `ConflictIndex` |
| GP-06 | **One employer of record.** Work for another entity is a recorded secondment with a cost recharge, never a second payroll. | RC E-31; RE F5.3 | `hr.secondments`; payroll only in the employing entity |
| GP-07 | **Related-party transactions are visible to the Board.** Every inter-company service, cross-charge and data-sharing arrangement with consideration is in the register with its s.188 status. | Companies Act 2013 s.2(76), s.188 [RE F5.2] | `grp.intercompany_agreements`, `grp.related_parties`; Compliance Cockpit |
| GP-08 | **Parties decide referrals.** No referral, handoff or data package moves between group businesses without the party's (or the regulated tenant's) recorded authorisation, and the party chooses any professional. | NN-39; RE F1.4, D14–D16 | `grp.referrals.authorisation_id` NOT NULL |
| GP-09 | **Separate exports and audit by entity.** Each entity can export and audit its own partition; consolidated group reporting uses aggregates only. | NN-37; NN-38 | Export scope `GROUP_COMPANY` (Appendix AC); `grp_consolidated` views (k ≥ 5) |
| GP-10 | **Configuration follows NN-33.** Group structure, purposes and grant limits are governed settings; routine entity settings are tenant tier. | NN-33 | Settings catalogue P21 §9 |

## AD.2 Group structure model

### AD.2.1 Hierarchy
```
Group (grp.groups)                         e.g. INFRABYX
 └─ Legal entity (grp.legal_entities)      one row per company; separate fiduciary, employer, GSTIN, books
     ├─ Brands (grp.brands)                public names, domains, design tokens, website
     ├─ Billing profiles (grp.billing_profiles)   GSTIN per State, invoice series, bank accounts (NN-36 controls), books SoR (Appendix AC §AC.11.5)
     ├─ Policies (grp.entity_policies)     privacy notice, HR policies, code of conduct, retention overrides, authority matrix reference
     ├─ Administrators (grp.entity_role_assignments)  entity_admin, it_admin, hr_manager, finance_ops, dpo, grievance_officer
     ├─ Platform tenants (core.tenants)    e.g. Equator institution tenant; an Operations Platform workspace per entity
     └─ Workspace connection (cfg.workspace_connections, Appendix AC)
```

### AD.2.2 Seed legal entities (configurable; CS to supply particulars)

| Short code | Legal entity | Business | Role in the platform | Particulars |
|---|---|---|---|---|
| `EQR` | **Equator Resolution Service Private Limited** | ODR institution and SaaS (Equator Resolution) | Operating entity of the Equator platform (master X-15); first company on the Operations Platform (D3-02); data fiduciary for Equator users, parties and neutrals | CIN, registered office, GSTIN, DPO, Grievance Officer from `tenant.legal_entity` (X-15) **[VERIFY — open: CS]** |
| `ICOPC` | **Infrabyx Consultancy (OPC) Private Limited** | Training (equatoradr.com is presented as its brand — D2-17) | Separate entity for training; any referral between Equator and the training business is a related-party matter (X-29) | **[VERIFY — open: CS to confirm the Equator ADR Institute operating entity, D2-17]** |
| `FINBYX` | Finbyx (legal entity name to be supplied) | LOS/LMS software for NBFCs | Lender-side software vendor; processor for its lender clients | **[VERIFY — open: CS — legal name, CIN]** |
| `UDOFIN` | Udofin (legal entity name to be supplied) | Digital lending platform / LSP | Lender-side service provider to regulated entities | **[VERIFY — open: CS]** |
| `LAWDOCS` | LawDocs (legal entity name to be supplied) | Legal documents and eSign | Template and e-sign connector (Appendix D §D.7) | **[VERIFY — open: CS]** |
| `OTHER_*` | Any further group company | Configurable | Added by `group_admin` with CS approval | — |

Each row records: `entity_type` (`private_limited`, `opc`, `llp`, `public_unlisted`, `public_listed`, `nbfc`, `other`), `regulated_by[]` (e.g. RBI for an NBFC), `holding_entity_id` and shareholding chain (**[VERIFY — open: CS — RE open point 8]**), directors (DIN hashes) for related-party detection, `books_sor`, `audit_applicability` facts (`group.audit.applicability.*`, Appendix AE §AE.8.2: internal audit under s.138/r.13, CARO 2020 exemption tests — configurable, CS-owned, reviewed each April [RD F7.3, DI-F36]), DPDP role notes, workspace topology (AD.13).

### AD.2.3 Brands, billing and policies
- **Brands** never imply that one entity's services are another's. A group brand shown on an Equator page carries "related to Equator" and, where Consumer Protection (E-Commerce) Amendment Rules 2026 r.5(6) applies to the marketplace, is never favoured through platform data and is presented as associated with Equator only as that rule permits (commencement 1 Jan 2027 per one source **[VERIFY — open]**) [RE F3.1].
- **Billing profiles** belong to one entity; invoices are issued only by the entity that supplies; a shared service is billed by the provider entity to the consuming entity under its inter-company agreement (AD.9).
- **Policies** are versioned per entity. A group policy template (e.g., information security, anti-bribery) is adopted by each entity's own approval; the adoption record is `grp.entity_policies` (`template_id`, `adopted_version`, `approved_by`, `board_resolution_ref`).

## AD.3 Administration model — group admin versus entity admin

| Role | Scope | Can | Cannot |
|---|---|---|---|
| `group_admin` (exists in v3 role list) | Group | Create entities (with CS approval), define shared services, maintain the GDSA and inter-company registers, approve cross-company grant **templates**, view consolidated aggregates (k ≥ 5), run the group access review | Read any entity's records by default; approve a grant into an entity's data alone (the target entity's approver is always needed); see Equator case data at all |
| `entity_admin` (new role code; register in Appendix S §6.2 v3) | One legal entity | Manage the entity's settings, users, departments, brands, billing profiles; approve grants **into** its own partition; approve its exports (`GROUP_COMPANY`) | Change another entity's settings; approve grants into another entity |
| `group_hr` (exists) | Group, HR only | Maintain group HR policy templates, approve secondments (with both entities' HR), run group headcount aggregates | Read another entity's employee files without a grant |
| `it_admin` | One entity's workspace connection | JML, groups, licences (Appendix AC) | Grant platform roles |
| `dpo` (per entity) | Entity | DSRs, breach workflow, GDSA privacy terms, processor contracts | — |
| `internal_auditor` | Entity or group (by engagement) | Read-only, time-boxed access per audit engagement | Change data |
| `compliance_officer` | Entity | Related-party flags, ethical-wall attestations, SoD exceptions | — |

Equator's institutional roles (`registrar`, `case_manager`, `panel_manager`, etc.) exist **only in EQR's Equator tenant** and can never be granted by a cross-company grant (Locked; `GRP_ROLE_NOT_GRANTABLE`, 422).

## AD.4 Shared services and per-entity data partitions

### AD.4.1 Shared-service catalogue

| Service code | What it is | Provider entity (default) | Processing role | Partition rule | Cross-entity visibility |
|---|---|---|---|---|---|
| `ops_platform_engine` | "Infrabyx Work OS" engine running the Operations Platform (P16): CRM, onboarding, customer success, tickets, marketing calendar, PR, partnerships | EQR (D3-02) | Processor for each consuming entity | Every `ops` and `mkt` row carries `company_id` (= `grp.legal_entities.id`, AD-R1); separate workspace per entity | None unless a grant or shared artefact (AD.7) |
| `hrms` | HRMS and payroll (P18) | EQR or the entity the Board designates **[VERIFY — open: CS]** | Processor for each employing entity (s.8(2)) | `employing_entity_id` on every `hr`/`pay` row | `group_hr` aggregates only; files by grant |
| `professional_registry` | All-India directory of advocates and professionals (`dir`) | The **Directory Owner** entity designated by the Board (D3-05) | **Fiduciary** for collection, verification and publication; each consuming entity or lender tenant is an independent fiduciary for its own engagement use [RE F4.4] | Registry records are owned by `dir`; consuming tenants hold their own panel and engagement notes | Allow-listed fields and verification status only, under the GDSA (AD.8) |
| `knowledge_base` | Policies, how-to articles, templates, training content | EQR | Processor / content owner per article | Each article has `owner_entity_id` and `share_scope` | Per AD.7 sharing rules |
| `it_workspace` | Microsoft 365 or Google Workspace administration | Per AD.13 topology | Processor where shared | Per tenant or per domain | — |
| `finance_shared` (optional) | Shared accounts team preparing books for several entities | Designated entity | Processor; each entity remains responsible for its books (Companies (Accounts) Rules r.3) | `legal_entity_id`; separate ledgers | None |

### AD.4.2 Partition design (implementable)
1. Every table in a shared service carries the entity key: `legal_entity_id` in `hr`, `pay`, `ctl` (Appendix Z), `cfg` entity-specific tables, `xpt`, `eng` (Appendix AE) and `dir` consumer tables (Appendix AA); `company_id` in `ops` and `mkt` (Appendices X, Y). Both reference `grp.legal_entities.id` (AD-R1).
2. Database enforcement uses the sibling helpers unchanged: `rls.enable_entity_rls()` with session setting `app.entity_ids` and RESTRICTIVE policy `entity_scope` (Appendix Z), and `ops_company_isolation` with the acting company in `Equator-Context` (Appendix X). Both AND with tenant RLS (Appendix F §F.2).
3. **How a grant becomes access.** For each request, the policy engine (Cerbos, Appendix S §6) computes `app.entity_ids` = the principal's home entity plus the `target_entity_id` of every active grant whose `modules` include the module the endpoint serves, and sets `app.grant_ids` for logging. A grant for `ops.crm` therefore never widens `hr` or `pay` reads. A SECURITY DEFINER helper supplies the list:
```sql
CREATE FUNCTION grp.active_grant_entities(p_user uuid, p_module text) RETURNS uuid[]
  LANGUAGE sql STABLE SECURITY DEFINER SET search_path = grp, pg_temp AS $$
  SELECT coalesce(array_agg(DISTINCT g.target_entity_id), '{}')
  FROM grp.cross_company_grants g
  WHERE g.grantee_user_id = p_user AND g.status IN ('active','expiring')
    AND p_module = ANY (g.modules) AND now() BETWEEN g.starts_at AND g.expires_at
$$;
```
4. CI: the `db:rls-catalogue` extension of Appendix Z (entity scope required on every `hr`/`pay`/`ctl` table) is widened to `cfg` entity tables, `xpt` and `dir` consumer tables; Appendix X's check covers `ops` and `mkt`.
5. Field-level restriction inside a grant (e.g., a Finbyx analyst granted read of Equator's CRM accounts but not contact phone numbers) is enforced in the API by the grant's `field_policy` (allow-list) and in exports; read models `grp_v_<table>` project only allow-listed columns for grant-based reads.
6. Equator case schemas (`core` case tables, vertical schemas, sealed schemas) are **never** in any grant's module list: they stay under tenant + case RLS only (`GRP_MODULE_NOT_SHAREABLE`, 422; DB CHECK on `grp.cross_company_grants.modules`).

### AD.4.3 Shareable and non-shareable modules

| Module code | Shareable by grant? | Notes |
|---|---|---|
| `ops.crm`, `ops.onboarding`, `ops.customer_success` | Yes | Typical cross-functional sales and onboarding work |
| `ops.tickets`, `ops.knowledge_base` | Yes | Ticket content may include customer personal data — purpose and field policy required |
| `mkt.calendar`, `mkt.assets`, `mkt.pr` | Yes | Brand content |
| `mkt.contacts` | Yes, with consent scope check | Marketing consent is per group company (RB-23); a contact consented only to Equator marketing is not visible to Finbyx |
| `hr.directory` (name, role, department, work contact) | Yes | Internal staff directory |
| `hr.employee_file`, `pay.*` | Only to `group_hr` / host-entity manager for seconded staff, limited fields | Secondment-linked grants only (AD.6) |
| `dir.registry_view` | Through the GDSA consumer channel, not by role grant | AD.8 |
| `reports.dashboards` | Through shared artefacts (AD.7) | Aggregates only for cross-entity |
| `core.*` cases, `neutrals`, `allocation`, `proceedings`, `documents` (case), sealed | **Never** | NN-38 Locked |

## AD.5 Cross-company role grants

### AD.5.1 What a grant is
A **cross-company grant** lets a user whose home entity is A act in entity B's partition for a stated purpose, within named modules, data categories and fields, for a limited time. It is the only way a person reaches another entity's data (GP-03). A grant **never** carries an Equator institutional role, a neutral role, a sealed scope or any `core` case module (AD.3, AD.4.3).

### AD.5.2 Grant fields

| Field | Rule |
|---|---|
| `grantee_user_id`, `home_entity_id` | Grantee must be an active employee or contractor of the home entity (or seconded to it) |
| `target_entity_id` | ≠ home entity |
| `role_code` | From the target entity's grantable role list (`grp.grantable_roles`: e.g. `sales_executive`, `onboarding_specialist`, `support_agent`, `content_writer`, `designer`, `social_media_executive`, `finance_ops` read-only, `hr_executive` for seconded staff only) |
| `purpose_code` | From `grp.purposes` (AD.7.2), e.g. `purpose.shared_sales_pipeline`, `purpose.shared_support_desk`, `purpose.brand_content`, `purpose.secondment_management`, `purpose.group_mis` |
| `modules[]`, `data_categories[]`, `field_policy` | Within the purpose's allowed modules and fields; field policy is an allow-list |
| `record_filter` | Optional (e.g. only accounts tagged `joint_campaign_2027`) |
| `gdsa_id` | Required when the grant exposes personal data of the target entity's customers, employees or professionals; GDSA must be `active` and list the purpose |
| `secondment_id` | Required for HR-file access to seconded staff |
| `starts_at`, `expires_at` | `expires_at − starts_at` ≤ the lower of `group.grants.max_duration_days` (G, default 90) and the role's `grp.grantable_roles.max_duration_days` (≤ 365 for shared-desk purposes, AD-R4); renewals are new grants |
| `requested_by`, `approved_by_target` | Approver is the target entity's `entity_admin` or a delegated `department_head` in the target entity; never the grantee, never the requester (`GRP_GRANT_SELF_APPROVAL`, 409) |
| `second_approver` | Required when the purpose is `restricted` (HR files, finance, consent-bearing contacts): target entity's `dpo` or `compliance_officer` |
| `status` | `requested → approved → active → expiring → expired`; `rejected`, `revoked`, `suspended` |
| `review_due` | Monthly for grants > 30 days; included in the quarterly access review (Q §7.3) |
| `wall_check_result` | Result of the ethical-wall check at request and at activation (AD.10) |

### AD.5.3 Lifecycle and automation

| Event | System behaviour |
|---|---|
| Request (SCR-P21-21) | Validates role, purpose, modules, GDSA, duration; runs SoD and ethical-wall checks (AD.10); shows the target approver exactly what fields will be visible |
| Approval | Target approver (and second approver where required) at aal2-pr; `equator.grp.grant.approved.v1` |
| Activation at `starts_at` | Policy cache refreshed; grantee sees a "Working for {entity}" switcher with a coloured banner naming the entity and purpose (no blended views) |
| During | Every read and write under the grant writes `audit.access_log` with `grant_id`, `purpose_code` and entity; weekly digest to the target approver ("what your grantee did") |
| T-7 days | Notification to grantee and approver; renewal requires a fresh request |
| Expiry | `CrossCompanyGrantExpiryJob` (every 5 minutes) sets `expired`, refreshes the policy cache, ends sessions bound to the grant within 60 s |
| Revocation | Any approver, the grantee's manager, `dpo`, `group_admin` or `compliance_officer` may revoke at once with a reason |
| Grantee leaves or moves | HRMS leaver or mover event revokes all grants (AC §AC.2.4) |
| GDSA suspended or terminated | All dependent grants suspended immediately |

### AD.5.4 Limits (Locked unless stated)
- No standing grants: every grant has an expiry (bound in AD.5.2).
- Maximum concurrent target entities per grantee: `group.grants.max_concurrent_entities` (G, default 2).
- Export under a grant is not allowed; exports of the target entity's data are run by the target entity (`GROUP_COMPANY` scope, Appendix AC §AC.13.3).
- A grant cannot be delegated (Appendix S §6.4: delegation depth 1; grants excluded).
- Break-glass does not apply to cross-company access (Appendix S §6.6 remains case-scoped inside Equator).

## AD.6 Employment model — employer of record, secondment and deputation

### AD.6.1 Rules
1. **One employer of record per employee** (`employing_entity_id`), who issues the appointment letter, pays wages, deducts and deposits PF, ESI, professional tax, LWF and TDS, and holds the lien and the right to terminate [RE F5.3; RC E-31].
2. Work for another group entity is either (a) a **secondment/deputation** recorded in `hr.secondments` with a signed secondment letter, or (b) **separate part-time appointments** with each entity, each paying and contributing on its share of wages — option (b) needs payroll and PF advice to avoid ceiling and under-contribution issues **[VERIFY — open: payroll adviser, RE F5.3]**; default is (a).
3. **One PAN cannot have two active employments within the group without a secondment record** (`GRP_DUPLICATE_EMPLOYMENT`, 409) [RC E-31].
4. Payroll, PF and ESI run **only in the employing entity**; the host entity is charged through the inter-company recharge (AD.9), never through a second payroll. Statutory parameters (EPF wage ceiling, ESI threshold, rates) are P18 rule packs (e.g., `rulepack.IN.payroll.epf@2026.2`) and are not restated here.
5. **Substance over labels:** if the host directs day-to-day work, controls pay and can terminate, it may be treated as the real employer (*CCE v Northern Operating Systems*, SC, 19 May 2022) or as a principal employer of contract labour (OSH Code thresholds **[VERIFY — open]**); the secondment letter therefore records control, lien, termination and return clearly [RE F5.2, F5.3].
6. **GST:** a secondment may be a supply of manpower services by the employer to the host; CBIC Instruction 05/2023-GST (13 Dec 2023) says the judgment is not to be applied mechanically; each secondment carries `gst_review_status` (Appendix Z column; tax adviser) **[VERIFY — open: tax adviser]** [RE F5.2].
7. **Remote work across India:** the employing entity's State registrations (Shops and Establishments, professional tax) for the employee's work location are P18 items; the secondment does not change them **[VERIFY — open: RE open point 9]**.

### AD.6.2 Secondment letter (template `HR-SEC-01`, DOCX + PDF/A, e-signed by employee, employer and host)
Clauses: parties and employee; host entity and role; start and end dates; **lien retained by the employer**; day-to-day supervision (named host manager) within the employer's policies; **right to terminate retained by the employer**; working hours and location; leave approval (employer, after host input); performance input (host provides input; employer runs the appraisal — NN-35 transparency); cost-recharge basis (actual cost, cost plus mark-up, or time-based allocation) and invoicing frequency; confidentiality owed to both entities; **ethical-wall undertaking** (AD.10) naming the walls; data protection (host processes the employee's data on the employer's instructions or on its own basis where it independently directs work **[VERIFY — open: counsel, RE F5.1]**); IP; return on expiry; termination of secondment; governing policies; signatures.

### AD.6.3 Secondment lifecycle

| State | Entry condition | Effects |
|---|---|---|
| `draft` | HR of employing entity creates | — |
| `pending_signatures` | Both HR managers and `group_hr` approve (maker-checker) | Letter sent for e-sign (`ESIGN_PORT`) |
| `active` | All signatures; start date reached | Auto-creates a cross-company grant template for the host role (still needs the host approver per AD.5); time allocation codes enabled; recharge schedule starts |
| `extended` | New letter addendum signed | New end date |
| `ended` | End date, early termination or employee exit | Grants revoked; final recharge; return-to-employer task |

### AD.6.4 Time and cost allocation
- Allocation comes from Appendix Z: planned `hr.assignments.allocation_pct` by host entity, replaced by timesheet actuals where the role keeps timesheets. Allocation is for recharge and costing only, not for monitoring (NN-35: disclosed, purpose-limited).
- `IntercompanyChargeRunWorkflow` (monthly) computes recharges per agreement (AD.9) from payroll cost (P18 cost lines, including employer PF/ESI contributions and benefits) × allocation, applies the mark-up method, and creates draft inter-company invoices in the provider entity's billing profile with GST treatment per the agreement; maker (`accounts_maker`) and checker (`accounts_checker`) per NN-36.

## AD.7 Shared dashboards and content — field-level sharing and data-purpose labels

### AD.7.1 Shared artefacts
A **shared artefact** is a dashboard, report, saved view, knowledge-base article, template, brand asset or content item that its owner entity shares with other entities. Table `grp.shared_artifacts`:

| Field | Rule |
|---|---|
| `artifact_kind` | `dashboard`, `report`, `saved_view`, `kb_article`, `template`, `brand_asset`, `content_item` |
| `owner_entity_id`, `owner_user_id` | Owner remains accountable |
| `shared_with_entities[]` | Explicit list; "all group entities" is a list, not a wildcard |
| `purpose_codes[]` | Data-purpose labels (AD.7.2); the artefact is visible only to users whose role in the recipient entity is allowed for that purpose |
| `data_class_max` | `public`, `internal`, `aggregate`, `personal` (personal requires a GDSA) |
| `field_policy` | Allow-list of fields/columns; disallowed columns are removed server-side, not hidden in the UI |
| `aggregation_min_k` | For aggregate dashboards, cells with n < k suppressed (default 5; X-28 pattern) |
| `refresh_mode` | `live` (query-time, policy-checked) or `snapshot` (static, timestamped) |
| `expires_at` | Optional; default 12 months for personal-data artefacts |
| `approval` | Owner entity's `department_head` (content) or `dpo` (personal data) |

### AD.7.2 Data-purpose labels (seed of `grp.purposes`, tier G)

| Purpose code | Meaning | Allowed data classes | Example |
|---|---|---|---|
| `purpose.group_mis` | Group management information | aggregate | Group revenue by entity, headcount by department |
| `purpose.shared_sales_pipeline` | Joint selling to the same prospect | personal (business contacts) with GDSA | A joint Equator–Finbyx pitch to an NBFC |
| `purpose.shared_support_desk` | One support desk answering for several brands | personal (ticket requesters) with GDSA | Level-1 support for LawDocs and Equator |
| `purpose.brand_content` | Reuse of marketing and knowledge content | public, internal | Blog articles, templates, brand assets |
| `purpose.secondment_management` | Managing a seconded employee | personal (limited HR fields) | Host manager sees leave calendar of secondee |
| `purpose.training_content` | Shared training material | public, internal | Staff induction modules |
| `purpose.professional_engagement` | Engaging registry professionals for a client matter | registry allow-list fields | Lender tenant engages an advocate for execution |
| `purpose.conflict_and_disclosure` | Ethical-wall and NN-16 disclosure checks | minimal identifiers (keyed hashes) | Group client list for wall checks (AD.10) |

Purposes **not available** (Locked): case analytics, allocation, neutral performance, borrower or respondent profiling, credit scoring of professionals, marketing to respondents, cross-selling based on dispute data.

### AD.7.3 Rendering rules
- A shared dashboard shows a header "Shared by {owner entity} for {purpose}; data as of {time}".
- Drill-through from a shared aggregate to records is disabled unless the viewer also holds a grant covering those records.
- Equator's case-related dashboards (caseload, SLA, outcome mix) may be shared with group entities **only** as `aggregate` artefacts with k ≥ 10 for any outcome-related cell (X-28 public threshold), and never broken down by a client organisation that is also a group company's client (prevents inference about a lender's disputes).

## AD.8 Group Data-Sharing Agreement (GDSA) registry

### AD.8.1 When a GDSA is required
A GDSA is required before any personal data of one entity's data principals becomes accessible to another entity — through a cross-company grant, a shared artefact of class `personal`, the professional registry consumer channel, or a referral data package. **The DPDP Act has no intra-group exemption**; sharing is a disclosure to another fiduciary for a new purpose and needs consent that names recipients and purpose, or a processor structure [RE F4.4]. The DPDP Act's substantive duties commence on 13 May 2027 (G.S.R. 843(E); Rules G.S.R. 846(E)); until then IT Act s.43A and the SPDI Rules apply (X-37) — the registry is built to DPDP now [RE F4.1].

### AD.8.2 GDSA contents (template `GRP-GDSA-01`) and registry fields

| Clause / field | Content |
|---|---|
| Parties and roles | Each entity's role per data flow: independent fiduciary, joint use, or processor (role matrix) |
| Purpose schedule | Allowed purposes from AD.7.2 (e.g., for the registry: execution, registration and recovery engagement only; no marketing, no credit scoring of professionals) [RE D21] |
| Data categories and field allow-list | Minimum fields per purpose (e.g., registry: allow-list fields + verification status only) |
| Lawful basis per flow | Consent (with the consent purpose code that names recipients, e.g. `consent_group_share`), employment (s.7(i), employer only), contract, or processor instruction |
| Onward transfer | Banned without written consent of the disclosing entity |
| Correction and erasure propagation | ≤ 72 h after the source change (DPDP s.8(7) erasure including processors; s.8(3) accuracy when disclosed to another fiduciary) [RE F4.3, D21] |
| Security | Group security baseline (Appendix Q SC set), access logging, breach notice ≤ 24 h to the disclosing entity |
| Breach cooperation | Joint incident handling; each fiduciary's own notification duties |
| Audit rights | Disclosing entity may audit the recipient's use; `internal_auditor` engagement |
| Retention and deletion | Recipient deletes on purpose end, termination or withdrawal |
| Consideration and s.188 | Whether consideration exists; s.188 status (AD.9) |
| Term, review, termination | Annual review; termination triggers deletion and grant suspension |
| Signatures | Authorised signatories of each entity (e-sign) |

Registry table `grp.data_sharing_agreements` holds the structured version: `parties[]`, `role_matrix jsonb`, `purposes[]`, `data_categories[]`, `field_allow_list jsonb`, `lawful_basis jsonb`, `propagation_sla_hours` (default 72), `onward_transfer_allowed` (false), `consideration` (bool), `s188_status`, `document_id` (signed original in the evidence store), `status` (`draft → legal_review → signature → active → suspended → terminated`), `version`, `effective_from/to`, `review_due`.

### AD.8.3 Professional registry under the GDSA
- The Directory Owner (D3-05) publishes `equator.dir.record.updated.v1`, `…withdrawn.v1`, `…erased.v1`; every consuming tenant applies them; `RegistryPropagationReconcileJob` (daily) reports drift; any drift older than 72 h is a GDSA breach ticket [RE D22].
- A professional's consent `consent_group_share` names the recipient entities (e.g., "Make my professional profile available to lender clients of Infrabyx group companies Finbyx and Udofin, for engaging me in execution, registration and recovery matters") — separate toggle, revocable [RE F4.4]. Without it, the record is not visible outside the Directory Owner's own surfaces.
- Lender-side panel performance notes stay in the lender tenant and never flow back into the registry or Equator's neutral systems [RE F4.4].
- Advocate fields stay within the BCI r.36 Schedule; no paid placement, ratings, fee display, "featured" labels or referral rewards for advocates, CAs, CSs or CMAs (NN-34, NN-39) [RE F1.4–F1.5].

## AD.9 Inter-company service agreements, related parties and s.188

### AD.9.1 Related-party determination
- **Companies Act 2013 s.2(76)** includes, among others, clause (iv) "a private company in which a director or manager is a member or director" and clause (viii) holding, subsidiary or associate company and fellow subsidiary [RE F5.2, RE 43].
- **Private-company exemption (G.S.R. 464(E), 5 Jun 2015):** for s.188, clause (viii) does not apply to a private company's holding, subsidiary, associate or fellow subsidiary; from 13 Jun 2017 the exemption applies only to a company with no default in filing financial statements (s.137) or annual returns (s.92); **clause (iv) is not exempted**, so Infrabyx sister companies with common directors are usually still related parties for s.188; the exemptions are not available to a private company that is a subsidiary of a public company [RE F5.2, RE 42–43].
- The likely position for EQR, Finbyx and Udofin is "related parties under clause (iv)", but the shareholding chain and directorships are **not confirmed** **[VERIFY — open: CS — RE open point 8]**.
- `grp.related_parties` records each pair: `entity_a`, `entity_b`, `clauses[]` (e.g. `2(76)(iv)`), `basis` (common directors by DIN hash, shareholding), `exemption_464E_available` (bool, with filing-default check date), `subsidiary_of_public` (bool), `verified_by_cs`, `verified_at`, `effective_from/to`. A nightly job recomputes candidate relationships from director data and opens a CS review task on any change.

### AD.9.2 Inter-company service agreement (ICSA) register
`grp.intercompany_agreements` — one row per agreement:

| Field | Content |
|---|---|
| `provider_entity_id`, `recipient_entity_id` | Supplier and recipient |
| `services[]` | Shared-service codes (AD.4.1), secondments, office space, brand licence, data sharing with consideration |
| `scope_and_slas` | Document section reference + structured SLAs |
| `cost_base` | `actual_cost`, `cost_plus`, `fixed_fee`, `time_based`, `per_unit` |
| `markup_pct` | `numeric(9,6)`; benchmark document reference (arm's-length support) |
| `invoicing_frequency`, `gst_treatment` | Monthly default; forward charge between distinct GSTINs; valuation rules for related persons **[VERIFY — open: tax adviser, RE F5.2]** |
| `ordinary_course` and `arms_length` | Booleans with the CS's reasoning; transactions in the ordinary course **and** at arm's length are outside s.188 [RE F5.2] |
| `s188_status` | `exempt_ordinary_course_arms_length`, `board_approved`, `shareholder_approved`, `pending`, `not_related` |
| `board_resolution_ref`, `shareholder_resolution_ref` | Required by status; r.15(3) thresholds **[VERIFY — open: CS — proviso numbering and thresholds]** |
| `s184_disclosures[]` | Interested directors' disclosures (MBP-1 refs); `mbp4_register_ref` (s.189 register) |
| `aoc2_required` | Flag for the Board's report disclosure (s.134(3)(h)) |
| `audit_committee_ref` | s.177(4)(iv) only where an Audit Committee is mandatory |
| `data_protection` | Link to processing agreement or GDSA |
| `confidentiality_and_walls` | Ethical-wall schedule reference |
| `ip`, `non_solicitation`, `audit_rights`, `termination_and_transition` | Clause references [RE F5.2] |
| `tax_review_status` | `not_required`, `pending`, `cleared` (secondments always `pending` until cleared) |
| `status` | `draft → cs_review → approvals → active → expired/terminated` |

### AD.9.3 Workflow (`RelatedPartyApprovalWorkflow`)
1. Maker (`finance_ops` or `entity_admin`) drafts the ICSA from template `GRP-ICSA-01`.
2. CS review (role `compliance_officer` held by the CS, or `legal_reviewer`): related-party check against `grp.related_parties`; ordinary-course and arm's-length assessment with benchmark.
3. If not exempt: Board approval recorded (meeting date, resolution number, interested directors abstaining as applicable); shareholder approval where thresholds are crossed (the second proviso barring interested members from voting does not apply to private companies [RE F5.2]).
4. Signatures (e-sign by authorised signatories of both entities).
5. Activation: recharges may be invoiced only under an `active` ICSA (`GRP_ICSA_NOT_ACTIVE`, 409); secondment recharges link to the ICSA.
6. Annual review in April with the `group.audit.applicability.*` facts review (Appendix AE §AE.8.2) [RD DI-F36]; AOC-2 extract generated for the Board's report.

The existing Institute-referral rule (master X-29; Appendix O §2.10; LR-CORP-001) is one instance of this workflow; P21 migrates its approval record into `grp.intercompany_agreements`.

### AD.9.4 Inter-company charges
`grp.intercompany_charges`: `agreement_id`, `period`, `basis_lines jsonb` (cost lines with sources), `amount_minor`, `currency` (INR), `gst_lines` (CGST/SGST/IGST per Appendix F), `invoice_id` (provider entity's billing), `status` (`draft → checked → invoiced → settled`), `variance_note`. Each charge exports to the provider's and the recipient's books (Appendix AC §AC.11.5). NN-36: maker ≠ checker; amounts above the authority-matrix limit need the finance head of both entities.

## AD.10 Conflicts of interest and ethical walls

### AD.10.1 The risk
Infrabyx group companies serve lenders (Finbyx: LOS/LMS vendor to NBFCs; Udofin: digital lending platform) who will be repeat claimants in Equator NPA matters. A person who handles a lender's collections or onboarding in a group company, and then administers that lender's Equator cases, creates an apparent-bias argument (s.12(3) A&C Act; *CORE* principle that equality applies at appointment) and breaches NN-16 [RE F2.2, F5.3].

### AD.10.2 Data needed (minimal)
- `grp.group_client_relationships`: for each group entity, the organisations it serves as clients — identified only by keyed hashes of CIN, LLPIN, GSTIN, PAN and normalised legal name (`*_hmac`), with `relationship_type` (`software_client`, `lending_partner`, `lsp_for_re`, `services_client`), `from`, `to`, `source`. Shared under GDSA purpose `purpose.conflict_and_disclosure`; no commercial terms, no volumes.
- `grp.user_client_exposures`: for each user, the client organisations they work on in each entity (derived from CRM account ownership, collections queues, onboarding projects, support assignments) with `exposure_kind` (`account_owner`, `collections`, `onboarding`, `support`, `implementation`, `management`) and `last_exposed_at`.

### AD.10.3 Wall rules (Locked unless stated)

| # | Rule | Check point | Effect |
|---|---|---|---|
| EW-01 | A user with exposure to client organisation C in a group company during the last `group.walls.cooling_off_months` (G, default 12, minimum 6) may not be assigned to, or access, any Equator case in which C (or its group, by declared relationships) is a party | Equator case assignment; `ConflictIndex` (Appendix S §6.5) | Case added to the user's `conflicts[]`; `GRP_ETHICAL_WALL_CONFLICT` (409); no override for workforce |
| EW-02 | A user holding an Equator case-handling role (`case_manager`, `registrar`, `deputy_registrar`, `case_counsel`, `quality_officer`, `panel_manager`, `escrow_officer`) cannot receive a cross-company grant whose purpose involves lender-side client work (`collections`, `onboarding`, `account management` for lenders) | Grant request | Request blocked; alternative: a different person, or the user gives up the Equator role first (then EW-01 applies) |
| EW-03 | Equator `panel_manager` and allocation-system administrators cannot hold any role in Finbyx or Udofin | Membership grant (SoD trigger) | Blocked (Appendix S §6.7 extended) |
| EW-04 | Neutrals on Equator's panel who also provide services to a group company or its clients disclose it; the allocation engine treats a group-company client relationship as a conflict input for that client's cases | Neutral disclosure (P03) | Exclusion or disclosure per NN-03 rules |
| EW-05 | Counterparties in an Equator case see Equator's group relationships with any party (e.g., "The claimant is a software client of Finbyx, a company in the same group as Equator") | Case disclosure panel (P03/P04) | NN-16 extended [RE D10] |
| EW-06 | Annual attestation by every user with roles in more than one entity | `WallAttestationCampaign` (annually; T-30 reminder) | Non-attestation suspends cross-company grants |
| EW-07 | Wall breaches (access attempt blocked by EW-01) are logged and reviewed by the `compliance_officer` within 5 working days | `audit.access_log` | Investigation ticket if repeated |

Appendix X's `OPS_ETHICAL_WALL` applies EW-01 to Operations Platform tickets and matter-status rows (AD-R5).

### AD.10.4 Example
Priya is employed by Finbyx (employer of record) and seconded part-time to EQR's Operations Platform as a `support_agent`. In Finbyx she manages collections queues for NBFC "Alpha Finance". Alpha Finance files 400 NPA cases on Equator. EW-01 places all Alpha Finance cases in Priya's `conflicts[]`; the support desk router never assigns her tickets tagged to those cases; her support-desk view hides ticket content for those cases (ticket metadata says "assigned elsewhere — conflict"). If EQR wanted her as a case manager, EW-02 would block the Finbyx collections grant first.

## AD.11 Handoff and referral model

### AD.11.1 Referral types

| Referral type | From → to | Typical trigger | Authorising party | Data package (minimum) |
|---|---|---|---|---|
| `award_execution` | Equator party → professional of the party's choice | Award or settlement not complied with; execution petition (A&C s.36; Appendix R execution pack) | The party (award-holder) | Execution pack the party already holds (Appendix R), case number, certified copy reference — exported by the party from its own case (Appendix AC `PARTY_IN_CASE`) |
| `registration_support` | Equator party → professional | Settlement touching immovable property needing physical execution, stamping and registration (NN-08) | The parties to the instrument | Registration checklist, instrument rendition, appointment details |
| `npa_recovery_suit` | Lender tenant (in Finbyx/Udofin or Equator) → registry advocate chosen by the lender | NPA account where the lender decides to sue (civil suit, DRT, SARFAESI steps) rather than or after ODR | The lender (regulated entity) | Loan-account facts from the lender's own system; Equator award or settlement only if the lender itself attaches it from its Equator case |
| `odr_referral` | Finbyx/Udofin lender client → Equator | Default/dispute referral under a clause (Appendix D §D.7 bulk/clause APIs) | The lender (claimant), with clause evidence | D.7 payloads only (no arbitrator choice field — NN-03) |
| `grievance_escalation` | Udofin GRM desk → Equator ODR | Borrower grievance unresolved (D.7) | Borrower's escalation choice | D.7 payload |
| `lead_referral` | Any entity → another entity's sales | A prospect asks about another group business | The prospect (consent naming the recipient entity) | Business contact details only (consent per group company, RB-23) |

### AD.11.2 Rules (Locked)
1. **Party authorisation first.** `grp.referrals.authorisation_id` references a consent or instruction record of the party (or the regulated tenant's authorised signatory) naming the recipient, the purpose and the data package; without it the referral cannot be created (`GRP_REFERRAL_AUTHORISATION_MISSING`, 409).
2. **The party chooses the professional** from its own panel register or the registry; the choice is recorded with the list shown (NN-39); Equator and group companies never assign, rank, feature or recommend advocates.
3. **No fees, commissions or rewards to or from advocates, CAs, CSs or CMAs** for referrals (BCI Rules Part VI Ch. II r.36 and Ch. III r.2; ICMAI referral-network bar) [RE F1.4–F1.5, D12–D13]; any group-company fee to the party is only for its own non-legal services, priced the same whatever professional is chosen [RE D14].
4. **Equator never pushes case data to Finbyx or Udofin.** An award-holding lender exports its own case material from Equator and attaches it in its own system; the Equator → lender webhook channel (X-64) is the lender's own channel. A referral from Equator's side is a **signpost** to the party ("You may engage an advocate for execution; your execution pack is ready to download"), not a data transfer.
5. **No borrower profiling.** Referral data packages exclude Equator's communication logs, voice recordings, vulnerability flags, screening outcomes and offers.
6. **Disclosure:** where the referred professional or service belongs to a group company, the party sees "This service is provided by {entity}, a company in the same group as Equator" before authorising (CCPA material-connection principle [RE F3.2]; E-Commerce r.5(6) where the marketplace applies).

### AD.11.3 Referral lifecycle
`draft → authorised → sent → accepted | declined → in_progress → closed`; `withdrawn` by the party at any time before `accepted` (and data access ends where the recipient is a group company processing under the GDSA). Each transition writes `equator.grp.referral.<verb>.v1`; payloads carry IDs and codes only. Closed referrals are retained per the recipient's own retention policy; the referral record itself is retained 3 years (`grp_referral` class, tier G).

## AD.12 Separate exports, audit and consolidated reporting

| Need | Mechanism |
|---|---|
| Entity exports its own data | Appendix AC export scope `GROUP_COMPANY` (archival bag), partition-filtered; never another entity's partition; never Equator case data for a non-Equator entity |
| Entity leaves the group or a shared service | `GROUP_COMPANY` export + migration out (Appendix AC §AC.14 in reverse, i.e. a documented import into the entity's new systems) + termination of processing agreements, GDSAs and ICSAs + deletion certificate from the provider entity (DPDP s.8(7)) |
| Entity audit | Audit views `audit.v_entity_events` filtered by `legal_entity_id`; `internal_auditor` engagement per entity; Compliance Cockpit per entity shows internal-audit and CARO applicability facts (configurable, CS-owned) [RD DI-F36] |
| Group consolidated reporting | `grp_consolidated` schema of views over aggregates only (k ≥ 5; outcome-related ≥ 10); no personal data; `group_admin` and Board pack |
| Cross-company access evidence | `grant_access_report` collector (weekly): grants active, expired, revoked, accesses per grant, wall blocks; quarterly group access review |
| Related-party evidence | AOC-2 extract; ICSA register export; Board resolution references |

## AD.13 Workspace topology across the group
`group.workspace.topology` (G; approver CS + `group_admin`):

| Option | Description | Pros | Cons / controls |
|---|---|---|---|
| `tenant_per_entity` (**default**) | Each legal entity has its own Microsoft 365 (or Google) tenant and domain; cross-entity collaboration uses guest access | Clean fiduciary separation; separate audit logs; exports per entity | More licences and admin; guest access governance |
| `shared_tenant_multi_domain` | One tenant hosts several entities' domains | Lower admin cost | Mailboxes and files of several fiduciaries in one tenant; tenant admins see all; Information Barriers or similar segmentation may need higher licences **[VERIFY — open (vendor): licensing for segmentation features]**; Equator requires per-entity admin units or equivalent **[VERIFY — open]**, per-entity audit export, and a processing agreement naming the tenant-owning entity as processor |

Under either option: one `cfg.workspace_connections` row per entity and domain; JML for a seconded employee happens in the **employing** entity's tenant, with guest access in the host's tenant if needed; Equator case work never happens in any workspace (Appendix AC IP-06).

## AD.14 Data model (`grp` schema, canonical)

```sql
CREATE SCHEMA grp;

CREATE TABLE grp.groups (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL UNIQUE, name text NOT NULL,
  status text NOT NULL CHECK (status IN ('active','inactive')), std_cols);

CREATE TABLE grp.legal_entities (
  id uuid PRIMARY KEY DEFAULT uuidv7(), group_id uuid NOT NULL REFERENCES grp.groups(id),
  short_code text NOT NULL UNIQUE, legal_name text NOT NULL,
  entity_type text NOT NULL CHECK (entity_type IN ('private_limited','opc','llp','public_unlisted','public_listed','nbfc','other')),
  cin text, llpin text, pan_hmac char(64), gstins text[] NOT NULL DEFAULT '{}', registered_office jsonb,
  holding_entity_id uuid REFERENCES grp.legal_entities(id), shareholding jsonb, director_din_hmacs char(64)[] NOT NULL DEFAULT '{}',
  regulated_by text[] NOT NULL DEFAULT '{}', books_sor text CHECK (books_sor IN ('tally','zoho_books','equator_ledger','other')),   -- D3-30: general ledger tool per entity
  audit_applicability jsonb NOT NULL DEFAULT '{}',           -- group.audit.applicability.* facts with source and effective date (Appendix AE §AE.8.2)
  dpo_person_id uuid, grievance_officer_person_id uuid, privacy_notice_version text,
  platform_tenant_ids uuid[] NOT NULL DEFAULT '{}',          -- core.tenants owned by this entity
  status text NOT NULL CHECK (status IN ('draft','active','suspended','exited')), particulars_verified_at timestamptz, std_cols);

CREATE TABLE grp.brands (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  code text NOT NULL UNIQUE, display_name_i18n jsonb NOT NULL, domains text[] NOT NULL DEFAULT '{}', design_tokens_ref text,
  related_to_equator_label boolean NOT NULL DEFAULT true, std_cols);

CREATE TABLE grp.billing_profiles (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  gstin text NOT NULL, state_code char(2) NOT NULL, invoice_series text NOT NULL, bank_account_ref uuid,   -- NN-36 bank-detail change controls apply
  e_invoicing boolean NOT NULL DEFAULT false, std_cols, UNIQUE (legal_entity_id, gstin, invoice_series));

CREATE TABLE grp.entity_policies (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  policy_code text NOT NULL, template_id uuid, adopted_version text NOT NULL, document_id uuid,
  approved_by uuid NOT NULL, board_resolution_ref text, effective_from date NOT NULL, effective_to date, std_cols);

CREATE TABLE grp.entity_role_assignments (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid REFERENCES grp.legal_entities(id),  -- NULL = group scope (group_admin, group_hr)
  user_id uuid NOT NULL REFERENCES core.users(id), role_code text NOT NULL,
  granted_by uuid NOT NULL, approved_by uuid NOT NULL CHECK (approved_by <> granted_by),
  starts_at timestamptz NOT NULL, ends_at timestamptz, status text NOT NULL CHECK (status IN ('active','ended','revoked')), std_cols);

CREATE TABLE grp.shared_services (
  id uuid PRIMARY KEY DEFAULT uuidv7(), service_code text NOT NULL UNIQUE,
  provider_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), consumer_entity_ids uuid[] NOT NULL,
  processing_role text NOT NULL CHECK (processing_role IN ('processor','fiduciary_owner','content_owner')),
  processing_agreement_document_id uuid, icsa_id uuid, status text NOT NULL CHECK (status IN ('draft','active','suspended','retired')), std_cols);

CREATE TABLE grp.purposes (
  code text PRIMARY KEY, label_i18n jsonb NOT NULL, allowed_data_classes text[] NOT NULL,
  allowed_modules text[] NOT NULL, restricted boolean NOT NULL DEFAULT false, requires_gdsa boolean NOT NULL,
  version int NOT NULL, change_request_id uuid REFERENCES core.config_change_requests(id));

CREATE TABLE grp.grantable_roles (
  target_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), role_code text NOT NULL,
  allowed_purposes text[] NOT NULL, max_duration_days int NOT NULL CHECK (max_duration_days BETWEEN 1 AND 365),
  PRIMARY KEY (target_entity_id, role_code));

CREATE TABLE grp.data_sharing_agreements (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL, version int NOT NULL,
  party_entity_ids uuid[] NOT NULL, role_matrix jsonb NOT NULL, purposes text[] NOT NULL, data_categories text[] NOT NULL,
  field_allow_list jsonb NOT NULL, lawful_basis jsonb NOT NULL, propagation_sla_hours int NOT NULL DEFAULT 72,
  onward_transfer_allowed boolean NOT NULL DEFAULT false, consideration boolean NOT NULL DEFAULT false,
  s188_status text, icsa_id uuid, document_id uuid,
  status text NOT NULL CHECK (status IN ('draft','legal_review','signature','active','suspended','terminated')),
  effective_from date, effective_to date, review_due date NOT NULL, std_cols, UNIQUE (code, version));

CREATE TABLE grp.cross_company_grants (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  grantee_user_id uuid NOT NULL REFERENCES core.users(id),
  home_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), target_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  role_code text NOT NULL, purpose_code text NOT NULL REFERENCES grp.purposes(code),
  modules text[] NOT NULL, data_categories text[] NOT NULL, field_policy jsonb NOT NULL, record_filter jsonb,
  gdsa_id uuid REFERENCES grp.data_sharing_agreements(id), secondment_id uuid,
  starts_at timestamptz NOT NULL, expires_at timestamptz NOT NULL,
  requested_by uuid NOT NULL, approved_by_target uuid, second_approver uuid,
  wall_check_result jsonb, status text NOT NULL CHECK (status IN ('requested','approved','active','expiring','expired','rejected','revoked','suspended')),
  revoked_by uuid, revoked_reason text, review_due date, std_cols,
  CHECK (home_entity_id <> target_entity_id),
  CHECK (expires_at > starts_at),
  CHECK (approved_by_target IS NULL OR (approved_by_target <> grantee_user_id AND approved_by_target <> requested_by)),
  CHECK (NOT (modules && ARRAY['core','cases','neutrals','allocation','proceedings','documents','posh_sealed','health_sealed','safety_sealed'])));
-- Trigger grp.enforce_grant_limits(): duration ≤ grantable_roles.max_duration_days and ≤ group.grants.max_duration_days;
-- purpose allows every module; gdsa active and lists the purpose when purpose.requires_gdsa; concurrent-entity limit.

CREATE TABLE grp.related_parties (
  id uuid PRIMARY KEY DEFAULT uuidv7(), entity_a uuid NOT NULL REFERENCES grp.legal_entities(id), entity_b uuid NOT NULL REFERENCES grp.legal_entities(id),
  clauses text[] NOT NULL, basis jsonb NOT NULL, exemption_464e_available boolean, subsidiary_of_public boolean,
  verified_by_cs uuid, verified_at timestamptz, effective_from date NOT NULL, effective_to date, std_cols, CHECK (entity_a <> entity_b));

CREATE TABLE grp.intercompany_agreements (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL UNIQUE,
  provider_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), recipient_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  services text[] NOT NULL, cost_base text NOT NULL CHECK (cost_base IN ('actual_cost','cost_plus','fixed_fee','time_based','per_unit')),
  markup_pct numeric(9,6), benchmark_document_id uuid, invoicing_frequency text NOT NULL DEFAULT 'monthly', gst_treatment jsonb NOT NULL,
  ordinary_course boolean, arms_length boolean, s188_status text NOT NULL CHECK (s188_status IN
    ('exempt_ordinary_course_arms_length','board_approved','shareholder_approved','pending','not_related')),
  board_resolution_ref text, shareholder_resolution_ref text, s184_disclosures jsonb, mbp4_register_ref text,
  aoc2_required boolean NOT NULL DEFAULT false, audit_committee_ref text, processing_agreement_id uuid, gdsa_id uuid,
  tax_review_status text NOT NULL DEFAULT 'not_required' CHECK (tax_review_status IN ('not_required','pending','cleared')),
  document_id uuid, status text NOT NULL CHECK (status IN ('draft','cs_review','approvals','active','expired','terminated')),
  effective_from date, effective_to date, std_cols,
  CHECK (s188_status NOT IN ('board_approved','shareholder_approved') OR board_resolution_ref IS NOT NULL));

CREATE TABLE grp.intercompany_charges (
  id uuid PRIMARY KEY DEFAULT uuidv7(), agreement_id uuid NOT NULL REFERENCES grp.intercompany_agreements(id),
  period_start date NOT NULL, period_end date NOT NULL, basis_lines jsonb NOT NULL,
  amount_minor bigint NOT NULL CHECK (amount_minor >= 0), currency core.currency_code NOT NULL DEFAULT 'INR',
  cgst_minor bigint NOT NULL DEFAULT 0, sgst_minor bigint NOT NULL DEFAULT 0, igst_minor bigint NOT NULL DEFAULT 0,
  invoice_id uuid, maker uuid NOT NULL, checker uuid CHECK (checker IS NULL OR checker <> maker),
  status text NOT NULL CHECK (status IN ('draft','checked','invoiced','settled','reversed')), variance_note text, std_cols);
-- Append-only after 'invoiced' (core.deny_mutation on UPDATE of amount columns); corrections by reversal (NN-36).

CREATE TABLE grp.group_client_relationships (
  id uuid PRIMARY KEY DEFAULT uuidv7(), legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id),
  org_cin_hmac char(64), org_gstin_hmac char(64), org_pan_hmac char(64), org_name_norm_hmac char(64) NOT NULL,
  relationship_type text NOT NULL CHECK (relationship_type IN ('software_client','lending_partner','lsp_for_re','services_client')),
  from_date date NOT NULL, to_date date, source text NOT NULL, std_cols);

CREATE TABLE grp.user_client_exposures (
  id uuid PRIMARY KEY DEFAULT uuidv7(), user_id uuid NOT NULL REFERENCES core.users(id),
  legal_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), client_relationship_id uuid NOT NULL REFERENCES grp.group_client_relationships(id),
  exposure_kind text NOT NULL CHECK (exposure_kind IN ('account_owner','collections','onboarding','support','implementation','management')),
  first_exposed_at timestamptz NOT NULL, last_exposed_at timestamptz NOT NULL, source_ref text NOT NULL, std_cols);

CREATE TABLE grp.ethical_wall_attestations (
  id uuid PRIMARY KEY DEFAULT uuidv7(), user_id uuid NOT NULL REFERENCES core.users(id), campaign_year int NOT NULL,
  entities uuid[] NOT NULL, walls_acknowledged jsonb NOT NULL, signed_document_id uuid, attested_at timestamptz, std_cols,
  UNIQUE (user_id, campaign_year));

CREATE TABLE grp.shared_artifacts (
  id uuid PRIMARY KEY DEFAULT uuidv7(), artifact_kind text NOT NULL CHECK (artifact_kind IN
    ('dashboard','report','saved_view','kb_article','template','brand_asset','content_item')),
  artifact_ref uuid NOT NULL, owner_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), owner_user_id uuid NOT NULL,
  shared_with_entities uuid[] NOT NULL, purpose_codes text[] NOT NULL, data_class_max text NOT NULL CHECK (data_class_max IN ('public','internal','aggregate','personal')),
  field_policy jsonb NOT NULL, aggregation_min_k int NOT NULL DEFAULT 5 CHECK (aggregation_min_k >= 5),
  refresh_mode text NOT NULL CHECK (refresh_mode IN ('live','snapshot')), gdsa_id uuid, expires_at timestamptz,
  approved_by uuid NOT NULL, status text NOT NULL CHECK (status IN ('active','expired','withdrawn')), std_cols,
  CHECK (data_class_max <> 'personal' OR gdsa_id IS NOT NULL));

CREATE TABLE grp.referrals (
  id uuid PRIMARY KEY DEFAULT uuidv7(), referral_type text NOT NULL CHECK (referral_type IN
    ('award_execution','registration_support','npa_recovery_suit','odr_referral','grievance_escalation','lead_referral')),
  from_entity_id uuid NOT NULL REFERENCES grp.legal_entities(id), to_entity_id uuid REFERENCES grp.legal_entities(id),
  to_professional_record_id uuid,                       -- dir record chosen by the party (NN-39)
  authorising_party_ref jsonb NOT NULL, authorisation_id uuid NOT NULL,   -- core.consent_records or signed instruction
  choice_record jsonb,                                   -- list shown and selection (NN-39)
  data_package jsonb NOT NULL,                           -- manifest of items (IDs and hashes), never case data pushed by Equator
  group_relationship_disclosed boolean NOT NULL DEFAULT false,
  status text NOT NULL CHECK (status IN ('draft','authorised','sent','accepted','declined','in_progress','closed','withdrawn')),
  retention_class text NOT NULL DEFAULT 'grp_referral', std_cols);
```
Secondment columns added to `hr.secondments` (Appendix Z canonical; additive migration, AD-R3): `icsa_id uuid REFERENCES grp.intercompany_agreements(id)`, `grant_template jsonb`, `wall_schedule jsonb`. View `grp.companies` (AD-R1): `CREATE VIEW grp.companies AS SELECT id, short_code AS company_code, legal_name, status FROM grp.legal_entities;`. All `grp` tables: tenant RLS is replaced by group-scope policies (`group_admin` read; `entity_admin` read/write own entity rows; grantee reads own grants); `core.deny_mutation()` on `grp.intercompany_charges` amounts after invoicing and on `audit` rows.

## AD.15 APIs, events and errors

### AD.15.1 APIs (`/v1/group/…`; problem+json; Idempotency-Key on creating POSTs; step-up aal2-pr for approvals)

| Method and path | Purpose | Roles |
|---|---|---|
| `GET/POST /v1/group/entities`, `PATCH /v1/group/entities/{id}` | Maintain legal entities (CS approval for create and particulars) | `group_admin` (maker), CS (`compliance_officer`) checker |
| `GET/POST /v1/group/entities/{id}/brands`, `/billing-profiles`, `/policies`, `/admins` | Entity sub-objects | `entity_admin` |
| `GET/POST /v1/group/shared-services` | Shared-service catalogue | `group_admin` |
| `GET /v1/group/purposes`; `POST /v1/group/purposes` (change request) | Purpose labels (tier G) | `group_admin` + `dpo` |
| `POST /v1/group/grants` | Request a cross-company grant | Any user (for self) or manager (for report) |
| `POST /v1/group/grants/{id}/approve` · `/reject` · `/revoke` | Decide or end a grant | Target `entity_admin` / delegated `department_head`; second approver where restricted |
| `GET /v1/group/grants?status=&entity=` | List grants (own, as approver, entity-wide for admins) | Per role |
| `GET /v1/group/grants/{id}/access-report` | What the grantee did | Target approver, `dpo`, `internal_auditor` |
| `POST /v1/group/gdsas` · `PATCH …/{id}` · `POST …/{id}/activate` · `/suspend` · `/terminate` | GDSA registry | `dpo` of each party entity, `legal_reviewer`, signatories |
| `POST /v1/group/icsas` · `POST …/{id}/submit` · `POST …/{id}/record-approval` | Inter-company agreements and s.188 record | `finance_ops`, CS, `entity_admin` |
| `GET /v1/group/related-parties`; `POST …/{id}/verify` | Related-party register | CS |
| `POST /v1/group/charges/run` · `POST /v1/group/charges/{id}/check` | Monthly recharge run and checking | `accounts_maker`, `accounts_checker` |
| `POST /v1/group/secondments` · `POST …/{id}/submit` · `/end` | Secondments (with P18) | `hr_manager` of both entities, `group_hr` |
| `GET/POST /v1/group/client-relationships` (hashes only) · `GET /v1/group/walls/check?userId=&orgRef=` | Wall data and checks | `compliance_officer`; check endpoint used internally by assignment and grant services |
| `POST /v1/group/attestations/campaigns` · `POST /v1/me/attestations/{id}/sign` | Annual wall attestation | `compliance_officer`; each user |
| `POST /v1/group/shared-artifacts` · `PATCH …/{id}` · `POST …/{id}/withdraw` | Share dashboards and content | Owner; approver per AD.7.1 |
| `POST /v1/group/referrals` · `POST …/{id}/authorise` · `/send` · `/withdraw` | Referral lifecycle | Party or regulated tenant signatory (authorise); `ops` user (prepare) |
| `GET /v1/group/consolidated/{report}` | Consolidated aggregates | `group_admin` |

### AD.15.2 Events (`equator.grp.<entity>.<verb>.v1`; payloads IDs and codes only)
`grp.entity.created`, `grp.entity.status_changed`, `grp.grant.requested`, `grp.grant.approved`, `grp.grant.activated`, `grp.grant.expiring`, `grp.grant.expired`, `grp.grant.revoked`, `grp.gdsa.activated`, `grp.gdsa.suspended`, `grp.gdsa.terminated`, `grp.icsa.activated`, `grp.related_party.changed`, `grp.charge.invoiced`, `grp.secondment.activated`, `grp.secondment.ended`, `grp.wall.conflict_detected`, `grp.attestation.overdue`, `grp.shared_artifact.published`, `grp.shared_artifact.withdrawn`, `grp.referral.authorised`, `grp.referral.sent`, `grp.referral.withdrawn`, `grp.referral.closed`. Consumers: policy cache (grants, walls), `ConflictIndex`, HRMS, billing, audit, notifications, Compliance Cockpit.

### AD.15.3 Error codes (register in Appendix F §F.10.4 v3)

| Code | HTTP | Message (en) |
|---|---|---|
| `GRP_ENTITY_ACCESS_DENIED` | 403 | This record belongs to another company in the group. |
| `GRP_GRANT_REQUIRED` | 403 | Access to another company's data needs an approved, current grant. |
| `GRP_GRANT_SELF_APPROVAL` | 409 | You cannot approve your own access request. |
| `GRP_GRANT_DURATION_EXCEEDED` | 422 | Access can be granted for a limited period only. |
| `GRP_GDSA_REQUIRED` | 409 | A current data-sharing agreement is needed for this purpose. |
| `GRP_PURPOSE_NOT_ALLOWED` | 422 | This purpose does not allow the requested data. |
| `GRP_MODULE_NOT_SHAREABLE` | 422 | Case, neutral and allocation data are never shared across companies. |
| `GRP_ROLE_NOT_GRANTABLE` | 422 | This role cannot be granted across companies. |
| `GRP_ETHICAL_WALL_CONFLICT` | 409 | You cannot work on this matter because of a conflict of interest. |
| `GRP_DUPLICATE_EMPLOYMENT` | 409 | This person is already employed in the group; record a secondment instead. |
| `GRP_ICSA_NOT_ACTIVE` | 409 | No active inter-company agreement covers this charge. |
| `GRP_RELATED_PARTY_APPROVAL_PENDING` | 409 | Related-party approval is pending for this agreement. |
| `GRP_REFERRAL_AUTHORISATION_MISSING` | 409 | The party's authorisation is required before this referral. |
| `GRP_SHARED_ARTIFACT_FIELD_BLOCKED` | 422 | This field cannot be shared for the selected purpose. |
| `GRP_ATTESTATION_OVERDUE` | 403 | Complete your annual conflict attestation to continue cross-company work. |

## AD.16 Settings (selected; full catalogue in P21 §9)

| Key | Tier | Default | Approver |
|---|---|---|---|
| `group.grants.max_duration_days` | G (1–365) | 90 | `group_admin` + `dpo` |
| `group.grants.max_concurrent_entities` | G (1–4) | 2 | `group_admin` |
| `group.grants.review_interval_days` | T (7–90) | 30 | `entity_admin` |
| `group.walls.cooling_off_months` | G (min 6) | 12 | `compliance_officer` + `legal_reviewer` |
| `group.walls.attestation_month` | T | April | `compliance_officer` |
| `group.gdsa.propagation_sla_hours` | G (≤ 72) | 72 | `dpo` |
| `group.shared_artifacts.default_expiry_months` | T (1–24) | 12 | `entity_admin` |
| `group.consolidated.min_k` | L (≥ 5; outcome cells ≥ 10) | 5 / 10 | — |
| `group.workspace.topology` | G | `tenant_per_entity` | CS + `group_admin` |
| `group.referrals.retention_years` | G | 3 | `dpo` |
| `platform.grp.modules.never_shareable` | L | `core`, `cases`, `neutrals`, `allocation`, `proceedings`, `documents`, sealed | — |
| `group.purposes` (catalogue) | G | AD.7.2 | `group_admin` + `dpo` |

## AD.17 Acceptance tests
Gherkin scenarios AD-T01 to AD-T18 are in P21 §12 (`tests/acceptance/appendix-AD.feature`): entity RLS isolation (T01), grant requires target approver and expires automatically (T02), no grant can include `cases` (T03), GDSA required for personal-data purposes (T04), field policy strips disallowed columns (T05), ethical-wall block on assignment (T06), EW-02 grant block (T07), duplicate employment blocked (T08), secondment creates grant template but not access (T09), recharge run maker-checker and append-only (T10), ICSA not active blocks invoice (T11), related-party change opens CS task (T12), shared dashboard k-suppression (T13), referral needs party authorisation and records professional choice (T14), Equator never pushes case data to Finbyx (T15 — CI `GROUP_SHARE_SCOPE`), group relationship disclosed to counterparty (T16), `GROUP_COMPANY` export excludes other partitions (T17), registry withdrawal propagates within 72 h (T18).

## AD.18 Open items and verification flags
1. **Shareholding chain and directorships** of EQR, ICOPC, Finbyx, Udofin and LawDocs; whether any is a subsidiary of a public company; filing-default status for G.S.R. 464(E) — CS [RE open point 8].
2. **s.188 proviso numbering and r.15(3) thresholds** — CS.
3. **Legal names and CINs** of Finbyx, Udofin and LawDocs entities; the Equator ADR Institute operating entity (D2-17) — CS.
4. **Directory Owner** entity (D3-05) and **HRMS provider** entity — Board.
5. **Secondment GST** (*Northern Operating Systems*; CBIC Instruction 05/2023-GST) and **domestic transfer-pricing successors** under the Income-tax Act 2025 — tax adviser [RE open point 7].
6. **Part-time multiple appointments** — PF/ESI treatment; OSH Code contract-labour thresholds for intra-group deputation — payroll adviser and counsel [RE open point 9].
7. **Host entity's own s.7(i) basis** where it independently directs a secondee's work — counsel [RE F5.1].
8. **Shared M365 tenant** segmentation features and licensing — vendor.
9. **E-Commerce (Amendment) Rules 2026** commencement and r.5(6) application to group-affiliated sellers — counsel [RE open point 6].

## AD.19 Phase addenda

### For P00
**FR-P00-V3-AD01 — `grp` schema and grant-aware entity scope.** Create schema `grp` (AD.14), view `grp.companies`, helper `grp.active_grant_entities`, and the policy-engine step that computes `app.entity_ids` and the acting company from the home entity plus module-matching active grants (AD.4.2); widen the entity-scope CI catalogue to `cfg` entity tables, `xpt` and `dir` consumer tables. *Acceptance:* AD-T01; RLS lint passes.
**FR-P00-V3-AD02 — `GROUP_SHARE_SCOPE` CI test.** Static and runtime test that no query path from a `grp` sharing view, cross-company grant or group webhook subscription reaches `core` case tables, `neutrals`, allocation, proceedings, case documents or sealed schemas. *Acceptance:* AD-T03, AD-T15.

### For P01
**FR-P01-V3-AD01 — Cross-company grants in the policy engine.** Cerbos derived role `cross_company_grantee` with condition `grant` (Appendix S §6.3) extended to `target_entity_id`, `modules`, `field_policy`; entity switcher and banner; grant-bound sessions end within 60 s of expiry or revocation. *Acceptance:* AD-T02, AD-T05.
**FR-P01-V3-AD02 — Entity admin role.** Register `entity_admin` in Appendix S §6.2 (v3) with the AD.3 permissions; SoD: `entity_admin` cannot approve grants for itself. *Acceptance:* role matrix test.

### For P03
**FR-P03-V3-AD01 — Group relationships in conflict checks and disclosures.** `ConflictIndex` ingests `grp.user_client_exposures` (EW-01) and `grp.group_client_relationships` (EW-04); the case disclosure panel shows group relationships with any party (EW-05). *Acceptance:* AD-T06, AD-T16.

### For P09
**FR-P09-V3-AD01 — Finbyx/Udofin connectors as the lender's processor channel.** Webhook subscriptions to Finbyx- or Udofin-hosted endpoints are owned by the lender tenant admin, scoped to that lender's cases, labelled "processor for {lender}", and excluded from every group dashboard (X-64). *Acceptance:* AD-T15.
**FR-P09-V3-AD02 — Referral signposting.** After an award or settlement, the party sees execution and registration signposts with its export ready (Appendix R), and may authorise a referral to a professional it chooses (AD.11). *Acceptance:* AD-T14.

### For P14
**FR-P14-V3-AD01 — Group go-live gate.** Before any group company uses a shared service: entity rows verified by the CS; processing agreements and GDSAs active for each flow; ICSAs active with s.188 status recorded; wall data loaded; first attestation campaign complete; `grant_access_report` collector green. *Acceptance:* go-live checklist items `GRP-01…GRP-06` pass.

### For P16
**FR-P16-V3-AD01 — Grants in the Operations Platform.** `ops_company_isolation` (Appendix X) honours grant-computed acting companies for the modules a grant names; company switcher shows the grant banner; support-desk routing applies EW-01 (`OPS_ETHICAL_WALL`) to tickets linked to Equator cases. *Acceptance:* AD-T01, AD-T06.

### For P18
**FR-P18-V3-AD01 — Group columns for secondments and cross-entity employment guard.** Additive `hr.secondments` columns (AD-R3); `hr.legal_entities.id` foreign key to `grp.legal_entities` (AD-R1); `GRP_DUPLICATE_EMPLOYMENT` extends Appendix Z's one-active-employment-per-PAN index across entity tenants; Appendix Z allocations feed `IntercompanyChargeRunWorkflow`; payroll runs only in the employing entity. *Acceptance:* AD-T08, AD-T09, AD-T10.
