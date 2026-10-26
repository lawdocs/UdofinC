# Appendix B — Data Model, Events and Error Codes (binding)

> LawDocs Build Prompt Pack v1.0 · 25 October 2026 · Compiled by X1 from §5, §7 and §13 of phases P00–P23, conventions §5, the cross-file resolutions X-01…X-30 and Appendices I, K, R, S and Y. Owner of conventions: P00 (`core`, `packages/ids`, `packages/audit`); owner of each table, event and error code: the phase that introduces it.
>
> **Precedence.** Master §18 → `02` decisions → this appendix for **names, prefixes, envelope, event and error-code registries and class codes** → the owning phase for **columns** of its own tables (the phase prevails for a column; this appendix is corrected at the next integration) → other appendices. Where two phases claim the same name, prefix or code, the resolution recorded here governs and the files listed in §B.7 are corrected.

---

## B.0 Purpose

Twenty-four phases built by different squads must produce one coherent database that isolates tenants (NN-01), never edits history (NN-02), exports everything (NN-11), evolves without manual re-filing (NN-12) and exchanges data with group products only through registered contracts (NN-24). This appendix fixes the shared vocabulary: identifiers (§B.1), the table catalogue per schema (§B.2), canonical ownership against the Ecosystem Spec (§B.3), the event register (§B.4), the error-code register (§B.5) and data and retention classes (§B.6).

---

## B.1 Identifiers

### B.1.1 Naming and storage rules

- **Schema = module code** (conventions §4). Kernel schemas `gov`, `hr`, `hr_posh` are owned by `@infrabyx/governance-kernel` and `@infrabyx/hrms-kernel` (NN-47); LawDocs extends them only through `gov_ext_*` and `hr_ext_*` tables. Sealed material lives in `ld_sealed` (P01) and `hr_posh` (separate KMS keys). Consumer Help runs in its own logical database cell with the same schema names (X-17).
- **Physical tables are plural snake_case.** Where a phase §7.2 writes a singular name (P06 `tpl.template`, P07 `clm.agreements`, P10 `pld.project`, P14 `bsv.order`, P15 `chp.case`, P11 §5 `lit.matter`), the physical table is the plural (`tpl.templates`, `clm.agreements`, `pld.projects`, `bsv.orders`, `chp.cases`, `lit.matters`) and the singular is the logical record name. The **export-map record type** is the Appendix K bare snake_case name (`agreement`, `court_case`, `consumer_case`) with `module` as a separate field (Appendix K §K.11 governs; X-07); phase forms such as `clm.agreements`, `bsv_order`, `chp_case` or `ai_conversation` are accepted aliases in the YAML loader.
- Columns snake_case; booleans `is_`/`has_`; timestamps `_at` (UTC `timestamptz`); dates `_on`/`_date`; foreign keys `<entity>_id`; encrypted columns `<field>_enc` with `<field>_bidx` blind index and `<field>_masked` (P00 FR-P00-32). Enumerations are `text` with `CHECK` or a code table (`<schema>.code_<name>` or `core.code_values`); PostgreSQL `ENUM` is not used (expand-contract friendly, NN-12).
- Money `NUMERIC(20,4)` + `currency char(3)`; JSON money `{"amount": "1499.0000", "currency": "INR"}` (P00 FR-P00-42; Ecosystem Spec §5.1). Rates as percent per annum.
- API JSON snake_case fields; enum values `UPPER_SNAKE_CASE`.

### B.1.2 Standard columns (every tenant-scoped business table)

| Column | Rule |
|---|---|
| `id` | `<prefix>_` + ULID (26 Crockford base32), `text`, `CHECK (id ~ '^<prefix>_[0-9A-HJKMNP-TV-Z]{26}$')`, generated only by `packages/ids` (FR-P00-40); never reused; never encodes location |
| `tenant_id`, `legal_entity_id` | NOT NULL on tenant rows (`legal_entity_id` nullable for Personal workspaces); RLS deny-by-default policies on both (NN-01) |
| `created_at`, `created_by`, `updated_at`, `updated_by`, `on_behalf_of` | `on_behalf_of` carries the delegation (`dlg_`) or delivery grant (`grt_`) |
| `version` | Optimistic lock; `If-Match` on PATCH |
| `state`, `state_version` | Canonical state per Appendix A; tenant label in `tenant_status_code` where configurable |
| `ledger_ref` | Pointer to the `core.audit_events` row written in the same transaction (NN-45) |
| `owner_system` | `LD` unless the row is a projection (`RS`, `LDC`, `OH`, `EQ`); projections are read-only (X-06) |
| `source_refs[]` | Origins (import, ecosystem message, legacy alias) |

Platform tables (`*_definitions`, content registries) carry `brand_code` or none and are exempt from tenant RLS but readable per policy. Event ids are UUIDv7 (CloudEvents `id`); audit events use `aev_`.

### B.1.3 ID prefix registry

Source column: **C** conventions §5; **X** X-01; **X1** added by this appendix to remove a collision (phase files edited where noted).

| Prefix | Entity | Owner table | Src | Prefix | Entity | Owner table | Src |
|---|---|---|---|---|---|---|---|
| `ten_` | Tenant | `core.tenants` | C | `ent_` | Legal entity | `core.legal_entities` | C |
| `brd_` | Brand | `core.brands` | X | `ope_` | Operating entity | `core.operating_entities` | X |
| `usr_` | User | `iam.users` | C | `prs_` | Person (party) | `iam.persons` | C |
| `mbr_` | Membership | `iam.memberships` | X | `ivt_` | Invitation (incl. guest) | `iam.invitations` | X |
| `dev_` | Device (all clients; mobile extension `mob.devices`) | `iam.devices` | X | `onb_` | Onboarding invitation | `iam.onboarding_invitations` | X |
| `org_` | Organisation profile | `org` / `iam` org profile | C | `brn_` | Branch | `org.branches` | X |
| `dep_` | Department (HR kernel uses the same ids) | `org.departments` | C | `tem_` | Team | `org.teams` | X |
| `pos_` | Position (shared with HR kernel) | `org.positions` | C | `grt_` | Grant (all non-ROLE types; delivery extension 1:1) | `iam.grants` (+ `sdc.delivery_grants`) | C |
| `dlg_` | Delegation | `iam.delegations` | X | `apr_` | Approval request | `wf.approval_requests` | X |
| `cns_` | Consent artefact | `kyc.consents` | C | `ntv_` | Notice version | `kyc.notice_versions` | X |
| `kyc_` | Verification run | `kyc.verifications` | C | `pcr_` | Professional credential | `kyc.professional_credentials` | X |
| `gdn_` | Guardianship | `kyc.guardianships` | X | `nom_` | Nominee designation (vault view keyed alike) | `kyc.nominations` (+ `dms.nominees`) | X |
| `aev_` | Audit event | `core.audit_events` | X | `anc_` | Audit anchor | `core.audit_anchors` | X |
| `cor_` | Correction Entry | `core.correction_entries` | X | `mig_` | Migration run | `core.migration_runs` | X |
| `bkf_` | Backfill run | `core.backfill_runs` | X | `fld_` | Folder | `dms.folders` | C |
| `doc_` | Document | `dms.documents` | C | `ver_` | Version | `dms.versions` | C |
| `drv_` | Derived rendition | `dix.renditions` (read model `dms.renditions`) | C | `shr_` | Share pack / data room | `dms.shares` | X |
| `hld_` | Legal hold | `dms.legal_holds` | X | `svw_` | Saved view | `dms.saved_views` | X |
| `dxj_` | DIX job | `dix.jobs` | X1 (P05 edited) | `tpl_` | Template | `tpl.templates` | C |
| `cls_` | Clause | `tpl.clauses` | C | `drf_` | Draft | `drf.drafts` | C |
| `agr_` | Agreement | `clm.agreements` | C | `neg_` | Negotiation round | `clm.rounds` | C |
| `rlc_` | Redline change record | `clm.changes` | X1 (P07 edited) | `obl_` | Obligation | `clm.obligations` | C |
| `sgr_` | Signing request | `sgn.signing_requests` | C | `sig_` | Signature event | `sgn.signature_events` | C |
| `stp_` | Stamp instrument | `sgn.stamp_instruments` | C | `evp_` | Evidence pack (execution) | `sgn.evidence_packs` | C |
| `sgb_` | Bulk signing batch | `sgn.bulk_batches` | X | `pld_` | Pleading project | `pld.projects` | C |
| `ntc_` | Notice (incl. tax notices, `domain = TAX`) | `pld.notices` | C | `mat_` | Matter | `lit.matters` | C |
| `cas_` | Court case | `lit.cases` | C | `hrg_` | Hearing | `lit.hearings` | C |
| `odr_` | Order | `lit.orders` | C | `clk_` | Legal clock | `lit.clocks` | X |
| `cnl_` | Counsel (panel) | `lit.counsel_panel` | X | `lsi_` | Legal spend invoice | `lit.spend_invoices` | X |
| `exa_` | Exposure assessment | `lit.exposure_assessments` | X | `tmk_` | Trademark / IP asset | `ipm.assets` | C |
| `mtg_` | Governance meeting | `gov.meetings` | C | `res_` | Resolution | `gov.resolutions` | C |
| `lrq_` | Legal request | `lgo.requests` | X | `tsk_` | Task | `wf.tasks` (R-A-08) | C |
| `itm_` | Open / interim / waiting item | `wf.items` | C | `tfl_` | Tax filing | `tax.filings` | X |
| `svc_` | Catalogue service | `mkp.services` | C | `ofr_` | Offer | `mkp.offers` | C |
| `eng_` | Engagement (incl. business-service orders) | `mkp.engagements` | C | `ecr_` | Engagement change request | `mkp.change_requests` | X1 (P16 edited) |
| `rtn_` | Retainer | `mkp.retainers` | C | `sla_` | SLA schedule | `mkp.sla_schedules` | C |
| `pro_` | Professional | `mkp.professionals` | C | `rev_` | Review (LawDocs services only) | `mkp.reviews` | C |
| `pln_` | Plan (mirror) | `bil.plans` | C | `etl_` | Entitlement applied | `bil.entitlements_applied` | C |
| `inv_` | Invoice / credit note mirror | `bil.documents_mirror` | C | `pay_` | Payment mirror | `bil.payments_mirror` | C |
| `grv_` | Consumer case | `chp.cases` | C | `chl_` | Challan record | `chp.challans` | C |
| `veh_` | Vehicle record | `chp.vehicles` | C | `agt_` | Tenant agent (also Keycloak client id) | `agt.tenant_agents` | C |
| `msn_` | Agent mission | `agt.missions` | C | `run_` | AI / agent run | `ai.runs` | C |
| `nbk_` | AI notebook | `ai.notebooks` | X | `qrv_` | Qualified review (AI output) | `ai.qrg_reviews` | X |
| `aic_` | Vidhi conversation | `ai.conversations` | X1 (P09 edited) | `aim_` | Vidhi message | `ai.messages` | X1 (P09 edited) |
| `cnv_` | Conversation / thread / channel | `msg.channels` | C | `msg_` | Message | `msg.messages` | C |
| `exp_` | Export job | `xpt.export_jobs` | C | `imp_` | Import job (all sources) | `xpt.import_jobs` | C |
| `stg_` | Storage target | `xpt.storage_targets` | C | `cvl_` | Credential entry | `cvl.entries` | C |
| `dlv_` | Deliverable | `sdc.deliverables` | X | `dls_` | Delivery session | `sdc.sessions` | X |
| `tme_` | Time entry | `sdc.time_entries` | X | `mdc_` | Master-data change request | `sdc.masterdata_requests` | X1 (P18 edited) |
| `pg_` | CMS page | `web.pages` | C | `pst_` | Blog post | `web.posts` | C |
| `vid_` | Video | `web.videos` | C | `trm_` | Glossary term | `hlp.terms` | C |
| `tut_` | Tutorial | `hlp.tutorials` | C | `chg_` | Engineering change record | `eng.change_records` | C |
| `rel_` | Release | `eng.releases` | C | `dmt_` | Delivery meeting | `sdc.meetings` | X1 (P18 edited) |

**Prefix collisions found and resolved (X1).**

| Collision | Found in | Resolution |
|---|---|---|
| `chg_` used for four different entities | P07 `clm.change` (redline change), P16 `mkp.change_requests`, P18 `sdc.masterdata_requests`, P23 `eng.change_records` | `chg_` stays with engineering change records (conventions pair it with `rel_`); new `rlc_`, `ecr_`, `mdc_`. P07 §7.2, P16 FR-P16-42 and §7.2, P18 §7.2/§7.3 edited |
| `run_` for DIX jobs and AI runs | P05 `dix.jobs.run_id`; P09 `ai.runs` | `dxj_` for DIX jobs; AI-engine stages reference their `run_` in `engine_ids`. P05 §7.2 edited (column name `run_id` kept for API compatibility; P05 may rename to `job_id` at the next integration) |
| `cnv_`/`msg_` for Vidhi chats and message threads | P09 `ai.conversations/messages`; P07/P18 `msg` | `aic_`/`aim_` for Vidhi; `cnv_`/`msg_` for `msg`. P09 §7.2 edited |
| `itm_` allocated by `lgo.waiting_items` | P13 §7.2 | View over `wf.items` (X-09); P13 §7.2 edited |
| `grt_` in two tables | P02 `iam.grants`, P18 `sdc.delivery_grants` | Single ID space; `sdc.delivery_grants.grt_id` is a 1:1 FK to `iam.grants.id` |
| `dev_` devices in two tables | P01 `iam.devices`, P22 `mob.devices` | Single ID space; `mob.devices` extends `iam.devices` 1:1 |
| `dep_`/`pos_` in `org` and HR kernel | P02, P13 | `org` allocates; HR kernel rows reference the same ids (P13 already says "shared with org") |
| `imp_` used by four modules | P04, P11, P12, P20 | One `xpt.import_jobs` ID space with `source_kind` (R-A-10) |
| `mtg_` in `gov.meetings` and `sdc.meetings` | P13, P18 | `mtg_` stays with governance meetings (statutory semantics); delivery calls use `dmt_`. P18 §7.2 edited |
| `evp_` vs `eng.evidence_packs` | P08, P23 | `evp_` is execution evidence only; `eng.evidence_packs` (audit evidence packs) use plain `id` with no public prefix (platform-internal) |

### B.1.4 Business reference IDs (human-readable, permanent)

Format `LD-<FAMILY>-<YYYY>-<NNNNNN>`, regex `^LD-(AGR|MAT|CAS|TMK|ENG|GRV|NTC|ORD|LRQ|DOC)-\d{4}-\d{6}$`. Allocated by `core.allocate_business_ref(family, n)` inside the creating transaction; series never decreases; rollback leaves a gap, never a duplicate; the year is the allocation year and never changes (FR-P00-41). Resolver `/r/<ref>` opens the record if visible, otherwise returns the same "not found" as a non-existent reference. Legacy identifiers are aliases in `core.ref_aliases`.

| Family | Record | Owner | Shown on |
|---|---|---|---|
| `AGR` | Agreement | P07 `clm.agreements` | Repository, signing, exports, Appendix Y #46 |
| `MAT` | Matter | P11 `lit.matters` | Litigation, LDC projection (#49) |
| `CAS` | Court case | P11 `lit.cases` | Litigation, folder names (#50) |
| `TMK` | IP asset (all IP types) | P12 `ipm.assets` | IP portfolio (#51) |
| `ENG` | Engagement, retainer, business-service order | P16 `mkp.engagements`; P14 `bsv.orders` | Marketplace, services (#52) |
| `GRV` | Consumer case | P15 `chp.cases` | Consumer Help brand only |
| `NTC` | Notice | P10 `pld.notices` | Notices register |
| `ORD` | OH8 order mirror and legacy orders | P00/P17 `bil.order_mirror` | Billing; legacy migration |
| `LRQ` | Legal request | P13 `lgo.requests` | Legal desk |
| `DOC` | Vault document display reference (optional) | P04 | Vault |

Other human series (not `LD-` business refs): `CHG-YYYY-NNNNNN` engineering change (P23); GST invoice and credit-note numbers (issued by OH8, never by LawDocs); tenant display references from `cfg.numbering_schemes` (P03; searchable, exported beside the permanent id, never a substitute for it).

---

## B.2 Table catalogue per schema (compiled from every phase §7.2)

Columns: **Table** (physical, plural) · **Id** · **Key columns** (abridged; the owning phase §7.2 is canonical) · **RLS** (T = tenant RLS on `tenant_id`+`legal_entity_id`; P = platform-scoped; U = user-scoped; S = sealed store; X = exempt reference data) · **Retention** (class code, §B.6.2) · **Export** (Appendix K record type; `—` = `x-export: excluded` or derived, with reason; † = record type proposed by X1 for Appendix K).

### B.2.1 `core` (owner P00)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `core.tenants` | `ten_` | kind, brand_code, operating_entity_id, status, year_basis, slug | P + self-row | TENANT_LIFE_8Y | `organisation_profile` |
| `core.brands`, `core.operating_entities` | `brd_`, `ope_` | code, legal identifiers, officers | X | PERMANENT | — (platform) |
| `core.legal_entities` | `ent_` | tenant_id, constitution, ids (enc/bidx/masked), valid_period | T | TENANT_LIFE_8Y | `legal_entity` |
| `core.tenant_domains` | — | host, tenant_id, verified_at | P | TENANT_LIFE_8Y | — |
| `core.data_classes`, `core.id_prefixes` | — | code | X | PERMANENT | — |
| `core.sequences`, `core.business_refs`, `core.ref_aliases` | — | family, year, n; alias_type, alias_value | T (refs), P (series) | PERMANENT | dataset in `99 …/` (aliases) |
| `core.idempotency_keys` | — | tenant_id, key, route, request_hash | T | TRANSIENT_24H | — |
| `core.side_effects` | — | port, provider, ext_ref, status, reconciled_at | T | OPS_8Y | — |
| `core.outbox`, `core.inbox` | UUIDv7 | CloudEvents columns; (subject, seq) | T | OUTBOX_90D | — |
| `core.audit_events` (partitioned) | `aev_` | chain_id, seq, event_id, business_refs (GIN) | T chain; platform chains P | LEDGER (≥ 8 y, Object Lock export) | `audit_event` |
| `core.audit_anchors` | `anc_` | chain_id, date, merkle_root, signature | as ledger | LEDGER | `audit_event` |
| `core.correction_entries`, `core.correction_acknowledgements` | `cor_` | target kind, field, before/after, state, approvals | T + P | LEDGER | `audit_event` |
| `core.access_log`, `core.break_glass_events` | — | actor, purpose, object, at | T | LEDGER | `access_log` |
| `core.migration_runs`, `core.migration_lineage`, `core.backfill_runs` | `mig_`, `bkf_` | run_id, source refs, hashes | T rows tenant-scoped | OPS_8Y | — (platform) |

**Resolution R-B-01 (heads created by P00, owned by P03):** P00 `cfg.settings_registry` is created as `cfg.setting_definitions`; P00 `core.feature_flags` / `core.feature_flag_approvals` / `core.kill_switches` are created as `cfg.flags` / `cfg.flag_targets` (+ approvals in `wf`) / `cfg.kill_switches`. P00 §7.2/§7.4 now use these names (aligned by F1, 25 Oct 2026); P00 emits only `cfg.FlagChanged`, `cfg.KillSwitchEngaged` and `cfg.KillSwitchReleased`.

### B.2.2 `iam` (owners P01, P02)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `iam.persons` | `prs_` | names, contact points (enc/bidx/masked), language, a11y prefs, is_minor, deceased_at | T views; master P (logged) | TENANT_LIFE_8Y | `user` |
| `iam.users` | `usr_` | keycloak_sub, realm, person_id, status, brand | P | ACCOUNT_LIFE_1Y | `user` |
| `iam.memberships` | `mbr_` | person_id, tenant_id, kind, status, valid_period | T | TENANT_LIFE_8Y | `role_grant` |
| `iam.invitations` | `ivt_` | token_hash, kind, contact (enc), ttl, status | T | ROLLING_1Y | — |
| `iam.devices` | `dev_` | user_id, platform, attestation, last_seen | P | ACCOUNT_LIFE_1Y | `mob_device`† |
| `iam.sso_connections`, `iam.scim_tokens`, `iam.domain_verifications` | — | protocol, metadata, token_hash | T | TENANT_LIFE_8Y | — (secrets) |
| `iam.onboarding_invitations` | `onb_` | origin, requester ref, subject hash, snapshot ref, consentref/legalbasis, status | P | ROLLING_3Y | — |
| `iam.roles` | — | code, group, capabilities, ceilings | X | PERMANENT | — |
| `iam.custom_roles` | — | base_role, capabilities, version, state | T | TENANT_LIFE_8Y | `role_grant` |
| `iam.grants` (supertype) | `grt_` | grantee, grant_type, roles, scopes, valid_period, basis, state | T | TENANT_LIFE_8Y | `role_grant` |
| `iam.delegations` | `dlg_` | delegator, delegate, scope, valid_period, reason | T | OPS_8Y | `role_grant` |
| `iam.sod_rules` | — | pair definition, enforcement | X + tenant overrides | PERMANENT | — |
| `iam.access_reviews`, `iam.access_review_items` | — | campaign, reviewer, decision | T | OPS_8Y | `access_log` |
| `iam.access_transparency_log` (append-only) | — | grant_id, actor, action, object, at | T | LEDGER | `access_log` |

### B.2.3 `kyc` and `ld_sealed` (owner P01)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `kyc.verifications` | `kyc_` | person/org ref, purpose, method, provider, result, notice_id, consent_id | T + sealed ref | OPS_8Y (result); attributes PER_PURPOSE | `verification` |
| `ld_sealed.kyc_artefacts` | — | verification_id, attributes_enc, last4, signature evidence | S | PER_PURPOSE (deleted on revocation) | — (sealed; masked summary only) |
| `kyc.identity_levels` | — | person_id, level, method, valid_until | P (logged) | ACCOUNT_LIFE_1Y | `verification` |
| `kyc.digilocker_records` | — | uri, doc_type, issuer, verified_at, name_match | S ref | PER_PURPOSE | `verification` |
| `kyc.kyb_cases`, `kyc.kyb_facts` | — | legal_entity_id, field, value_enc, source, confidence, snapshot_hash | T | TENANT_LIFE_8Y | `verification` |
| `kyc.signatory_authorities` | — | person_id, basis, doc_id, scope, limit, valid_period, status | T | TENANT_LIFE_8Y | `signatory_authority`† |
| `kyc.professional_credentials` | `pcr_` | profession, numbers (enc), body, COP dates, status, desk | T (PRO_FIRM) | TENANT_LIFE_8Y | `professional` |
| `kyc.guardianships` | `gdn_` | guardian, ward, basis, evidence ref (sealed), status | T | handover + 8 y (OPS_8Y) | `guardianship`† |
| `kyc.nominations` | `nom_` | owner, nominee, scope, waiting_days, status, release refs | T + sealed evidence | TENANT_LIFE_8Y | `nominee`† |
| `kyc.consent_purposes`, `kyc.notice_versions` | `ntv_` | code, basis, version, hash, languages, reviewer | P (per operating entity/brand) | PERMANENT | — |
| `kyc.consents` | `cns_` | person_id, purpose, notice_id, status, captured_by | T | TENANT_LIFE_8Y (proof) | `consent_artefact` |
| `kyc.rights_requests` | — | type, status, due_at, forwarded_to | P/brand | OPS_8Y | `consent_artefact` |

### B.2.4 `org` (owner P02)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `org.branches` | `brn_` | legal_entity_id, code, state, valid_period | T | TENANT_LIFE_8Y | `legal_entity` |
| `org.departments` | `dep_` | parent_id, path ltree, canonical_function, valid_period | T | TENANT_LIFE_8Y | `department` |
| `org.teams`, `org.positions` | `tem_`, `pos_` | department_id, holder_person_id, kmp_type, valid_period | T | TENANT_LIFE_8Y | `position` |
| `org.restructures` | — | change set, effective_at, batch_id | T | OPS_8Y | `change_request` |

### B.2.5 `cfg` and `rul` (owner P03)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `cfg.setting_definitions` | — | key, tier, scopes, control class, type, schema, default, bounds, maker_checker, effective_dating, sensitivity | X | PERMANENT | — |
| `cfg.setting_values` (bitemporal) | — | scope_tier, scope_id, key, value, valid_from/to, change_id | T (tenant scopes) | PERMANENT | `setting_value` |
| `cfg.setting_changes` | — | key, before, after, actor, on_behalf_of, via, batch_id | T | ROLLING_7Y | `change_request` |
| `cfg.change_requests` | — | items, state, citation, effective_from, approvals | T | ROLLING_7Y | `change_request` |
| `cfg.change_batches`, `cfg.tenant_controls` | — | kind, undo_until; require_approval_keys | T | OPS_8Y | `customisation` |
| `cfg.brands` | — | brand_code, legal_entity_profile_id, tokens, domains, verticals | X | PERMANENT | — |
| `cfg.widget_catalogue`, `cfg.dashboard_layouts`, `cfg.nav_items`, `cfg.nav_overrides`, `cfg.quick_actions`, `cfg.terminology` | — | codes; tenant/user overrides | X / T | TENANT_LIFE_8Y | `customisation` |
| `cfg.custom_field_defs`, `cfg.status_sets`, `cfg.status_defs`, `cfg.reason_code_lists`, `cfg.reason_codes` | — | object_type, code, labels, canonical_state | T | TENANT_LIFE_8Y | `customisation` |
| `cfg.numbering_schemes`, `cfg.number_sequences` | — | pattern, reset_rule, next_value | T | PERMANENT | `customisation` |
| `cfg.form_defs`, `cfg.form_versions`, `cfg.letterheads` | — | layout, conditions, assets, version | T | TENANT_LIFE_8Y | `customisation` |
| `cfg.flags`, `cfg.flag_targets` | — | key, purpose, owner, expiry, verify_ref | P | OPS_8Y | — |
| `cfg.kill_switches`, `cfg.kill_switch_events` | — | code, scope, state, engaged_by, released_by, probe_result | P / T (tenant scope) | ROLLING_7Y | — |
| `cfg.config_templates`, `cfg.template_applications`, `cfg.config_bundles`, `cfg.fallback_events` | — | content, batch_id, signature, diff | T | ROLLING_3Y | `customisation` |
| `rul.rule_sets`, `rul.rule_set_versions` | — | code, jurisdiction, version, state, JDM content, citations, reviewer_of_record, effective dates | X | PERMANENT | — (content) |
| `rul.golden_cases` | — | inputs, expected | X / T | PERMANENT | — |
| `rul.evaluations` (partitioned) | — | rule_set_version_id, input_hash, output, object_ref | T | FOLLOWS_PARENT (min 7 y for signing decisions) | `rule_evaluation` |
| `rul.adoptions`, `rul.adaptations`, `rul.challenges` | — | mode, pinned_version, params | T | TENANT_LIFE_8Y | `customisation` |
| `rul.content_kinds`, `rul.content_versions` | — | kind, version, jurisdiction, reviewer, hash | X | PERMANENT | — |

### B.2.6 `wf` (owners P02 approvals, P03 items and tasks)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `wf.mc_actions` | — | action_code, platform_mode, defaults, nn_ref | X | PERMANENT | — |
| `wf.mc_policies` | — | action_code, scope, mode, selector, count, aal, expiry | T (bitemporal) | PERMANENT | `customisation` |
| `wf.approval_requests`, `wf.approval_decisions` | `apr_` | action, maker refs, payload_digest, route, state; checker, decision, digest_seen, aal | T | OPS_8Y | `change_request` |
| `wf.doa_tables` | — | legal_entity_id, version, ZEN rules, effective_from, state | T | PERMANENT | `customisation` |
| `wf.tasks` (R-A-08; P03 §7.2) | `tsk_` | parent ref, title, state (`OPEN`, `IN_PROGRESS`, `DONE`, `CANCELLED`), assignee user/team, assigned_by, due_at, priority, checklist, depends_on[], evidence_rule, evidence_refs, linked_item_id, source | T | FOLLOWS_PARENT | `task` (`item` family) |
| `wf.item_types` | — | code, parent types, owner rule, evidence rule, waiting party types, chase/SLA policy, formalities | X / T | PERMANENT | `customisation` |
| `wf.items` | `itm_` | item_type_code, parent, canonical_state, owner, due_at, visibility, external_label | T | FOLLOWS_PARENT | `item` |
| `wf.item_waits`, `wf.item_clocks`, `wf.item_interims` | — | party, expected_by, sla_paused; clock kind, due_at, paused_intervals; interim outcome | T | FOLLOWS_PARENT | `item_wait`, `item_clock` |
| `wf.chase_policies`, `wf.chase_log` | — | cadence, max_chases, channels, confirm_mode; seq, channel, template_version, idempotency_key | T | FOLLOWS_PARENT | `chase` |
| `wf.escalation_ladders`, `wf.sla_policies`, `wf.business_calendars` | — | levels; targets; State holidays | X / T | PERMANENT | `customisation` |

### B.2.7 `dms` (owner P04; ingest heads P00)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `dms.documents` | `doc_` | doc_type_code, category_code, state, confidentiality_class, owner, current_ver_id, is_executed, on_legal_hold, retention_class, eligibility_family | T | per class (§B.6.2) | `document` |
| `dms.versions` | `ver_` | seq, object_key, sha256, pre_mask_sha256, object_lock_mode, retain_until | T | per class | `version` |
| `dms.renditions` (read model of `dix.renditions`) | `drv_` | source_ver_id, kind, status, label | T | FOLLOWS_PARENT | `rendition` |
| `dms.metadata_values`, `dms.tags`, `dms.doc_tags`, `dms.doc_links`, `dms.relationships` | — | schema_version, values; record links; typed relationships | T | FOLLOWS_PARENT | `document` (datasets) |
| `dms.doc_types`, `dms.view_packs`, `dms.retention_classes` | — | content versions with reviewer of record | X | PERMANENT | — |
| `dms.folders`, `dms.folder_members`, `dms.saved_views` | `fld_`, `svw_` | parent, kind (MANUAL, SMART), query | T | TENANT_LIFE_8Y | `document` (folder view) |
| `dms.checkouts` | — | holder, expires_at, broken_by | T | ROLLING_1Y | — |
| `dms.shares`, `dms.share_items`, `dms.share_recipients` | `shr_` | kind, state, access_mode, watermark, expires_at, max_opens | T | ROLLING_7Y [REC] | `share`† |
| `dms.share_access_log` (append-only) | — | recipient, event, page, ip_prefix, ua_hash | T | ROLLING_7Y | `share`† |
| `dms.legal_holds`, `dms.disposals`, `dms.purge_records` | `hld_` | scope, reason, mat_id, state; basis, maker, checker, certificate | T | PERMANENT | `legal_hold`† |
| `dms.reminder_facts` | — | fact_code, date, rule_version | T | FOLLOWS_PARENT | `document` |
| `dms.nominees` (view keyed by `nom_`), `dms.nominee_claims`, `dms.delegates` | `nom_` | scope, trigger, waiting_days, access_days; claim state, evidence | T | until revoked + 7 y / PERMANENT (claims) | `nominee`† |
| `dms.digilocker_refs` | — | uri, issuer, verification, cns_id, retained_copy_ver_id | T | PER_PURPOSE | `document` |
| `dms.intake_mappings`, `dms.email_in_addresses`, `dms.health_findings`, `dms.offline_grants` | — | proposals; tokens; rule findings; device keys | T | ROLLING_1Y | — / `document` (findings dataset) |
| `dms.upload_intents`, `dms.document_hashes` (P00) | — | sha256, prev_hash (hash chain per tenant) | T | TENANT_LIFE_8Y | `version` |

### B.2.8 `dix` (owner P05)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `dix.jobs` | `dxj_` | ver_id, kind, state, engine_ids, settings_hash, credits | T | ROLLING_2Y | — |
| `dix.renditions` | `drv_` | kind (OCR_TEXT, OCR_PDF, TYPE_COPY, CHAT_TRANSCRIPT, TRANSLATION, TRANSLATION_CERTIFIED, REDACTED, MASKED), status, lang pair, object_ref, sha256, supersedes | T | FOLLOWS_PARENT | `rendition` |
| `dix.lines`, `dix.corrections`, `dix.attestations`, `dix.disputes` | — | page, bbox, confidence band; corrections; attestor capacity, hashes | T | FOLLOWS_PARENT | `rendition` |
| `dix.wa_chats`, `dix.wa_messages`, `dix.counter_diffs` | — | locale resolution, tz, counts; message rows | T | FOLLOWS_PARENT | `rendition` |
| `dix.lid_results`, `dix.translation_segments`, `dix.glossary_terms` (tenant overlay) | — | language id; segment scores; terms | T / X | FOLLOWS_PARENT / PERMANENT | `rendition` |
| `dix.certified_requests` | — | eng_id, pair, purpose, cert_type, state | T | ROLLING_7Y | `engagement` |
| `dix.extractions`, `dix.redaction_suggestions` | — | field, anchor, confidence, state | T | FOLLOWS_PARENT / ROLLING_1Y | `document` (confirmed only) |
| `dix.aadhaar_events` | — | stage, count, pre_mask_sha256, action (no digits) | T | PERMANENT | — |
| `dix.languages`, `dix.engines`, `dix.eval_sets`, `dix.eval_runs`, `dix.quality_tiers` | — | routes, residency, metrics | X | PERMANENT | — |

### B.2.9 `tpl` and `drf` (owner P06)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `tpl.categories`, `tpl.subcategories` | — | code (D12, D12.7), slug, title, upcoming | X / T | PERMANENT | — |
| `tpl.templates` | `tpl_` | canonical_doc_id, owner_scope, audience, lane_eligibility, alias_of | X / T | PERMANENT | `template_use` (tenant templates → `06 Policies and Registers/Contract Templates and Playbooks/`, X-12) |
| `tpl.template_versions`, `tpl.questionnaire_versions`, `tpl.state_variants`, `tpl.language_versions`, `tpl.golden_tests` | — | semver, status, effective dates, variable schema, formalities, eligibility_row_id, reviewer_of_record, content_hash | X / T | PERMANENT | as above |
| `tpl.clauses`, `tpl.clause_versions` | `cls_` | key, status, body per locale, positions, sources | X / T | PERMANENT | as above |
| `tpl.playbooks`, `tpl.playbook_versions` | — | scope, positions, approver rules | T | TENANT_LIFE_8Y | as above |
| `tpl.backlog_items` | — | type, scope_ref, evidence, owner, status, sla_due | P | PERMANENT | — |
| `drf.drafts` | `drf_` | owner, tpl_version_id, answers_enc, lane, ai_touched, review_state, agr_id | T | ANON_DRAFT_7D (anonymous); until deleted (account) | `draft` |
| `drf.draft_revisions`, `drf.reviews`, `drf.exports` | — | producer, ops, run_id; version_hash, reviewer, decision; format, watermark | T | FOLLOWS_PARENT (reviews permanent with draft) | `draft` |
| `drf.analytics_counters` | — | metric, bucket_date, value (k-anonymised) | P | ROLLING_3Y | — |

### B.2.10 `clm` and `msg` (owner P07)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `clm.intake_requests` | — | type, requester, department, answers_enc, status, sla_due, agr_id, lrq_id | T | CONTRACT_STD (10 y or tenant policy) | `legal_request` |
| `clm.agreements` | `agr_` (`LD-AGR-…`) | type_code, paper, status, owner, value, term, governing_law, confidentiality, parent_agr_id | T + ABAC | CONTRACT_STD | `agreement` |
| `clm.agreement_parties` | — | party_ref, role, side, signatory_refs | T | CONTRACT_STD | `agreement` |
| `clm.deal_rooms`, `clm.room_participants`, `clm.mirror_links` | — | controls, connected tenants; principal, side, rights | T (mirror rows service-only) | CONTRACT_STD | `negotiation_round` |
| `clm.version_meta` | — | ver_id, number, side, producer, visibility, docx/text sha256, round_no, locked | T (visibility-filtered for guests) | CONTRACT_STD | `negotiation_round` |
| `clm.rounds` | `neg_` | number, opened_by_side, shared/returned ver, status | T | CONTRACT_STD | `negotiation_round` |
| `clm.comparisons`, `clm.changes`, `clm.change_decisions` | `rlc_` | base/target, engine_version; type, source, anchors, hashes; decision, actor, seq | T (decisions internal only) | CONTRACT_STD | `negotiation_round` |
| `clm.issues`, `clm.deviations`, `clm.approval_steps` | — | clause anchor, visibility; position, approver; ver_hash, step, status | T (internal only) | CONTRACT_STD | `agreement` |
| `clm.obligations`, `clm.key_dates` | `obl_` | party_side, type, schedule, amount, owner, status, verified_by | T | CONTRACT_STD | `obligation` |
| `msg.channels` | `cnv_` | room_id or parent ref, kind (INTERNAL, SHARED, PARTY_PRIVATE), party_scope | T (channel-scoped) | FOLLOWS_PARENT | `thread` |
| `msg.messages` | `msg_` | author, body_enc, anchor, attachments, edited_at, withdrawn | T | FOLLOWS_PARENT | `message` |

**Resolution R-B-02:** P18 refers to `msg.conversations`/`msg.messages`; the physical names are `msg.channels`/`msg.messages` (P07 owns `msg`).

### B.2.11 `sgn` (owner P08)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `sgn.providers`, `sgn.esp_licences` | — | kind, asp_mode, esps, methods, contract_to, asp_cert_to, status; licence_to, renewal_evidence_ref | P | PERMANENT | — |
| `sgn.provider_health` | — | method, window, success_rate, p95, error classes | P | ROLLING_400D | — |
| `sgn.eligibility_evaluations` | — | doc/ver, family, facts, decision, flags, rule versions, row ids | T | EXECUTED_INSTRUMENT_EVIDENCE | `rule_evaluation` |
| `sgn.signing_requests` | `sgr_` | ver_id, frozen_sha256, state, order_mode, expires_at, eval_id, approval_ref, idempotency_key | T | EXECUTED_INSTRUMENT_EVIDENCE | `signing_request` |
| `sgn.participants`, `sgn.fields` | — | seq_group, role (incl. non-signing `HELPER`, `INTERPRETER`), prs_id, capacity, authority_ref, state, name_match_score | T | EXECUTED_INSTRUMENT_EVIDENCE | `signing_request` |
| `sgn.signing_assistance` (append-only; P08 FR-P08-57) | — | participant, mode, helper, witness, language, assistance_consent_ref, helper_declaration_ref, interpreter_session_ref (no disability or health data) | T | EXECUTED_INSTRUMENT_EVIDENCE | `signing_assistance` |
| `sgn.consent_versions` | — | method, lang, text_ref, approved_by | X | PERMANENT | — |
| `sgn.consent_records`, `sgn.signature_events`, `sgn.provider_evidence` (append-only) | `sig_` | consent at/ip/ua_hash; provider txn, ESP, cert serial, UTC/IST, response code (never OTP or Aadhaar data) | T | EXECUTED_INSTRUMENT_EVIDENCE | `signature_event` |
| `sgn.stamp_instruments`, `sgn.duty_quotes`, `sgn.exemption_declarations` | `stp_` | route, State, article, UIN (unique), amount, verification, doc_id, state | T | EXECUTED_INSTRUMENT_EVIDENCE | `stamp_instrument` |
| `sgn.formalities`, `sgn.appointments` | — | kind, status, wf_item_id, evidence, waiver reason | T | EXECUTED_INSTRUMENT_EVIDENCE / ROLLING_7Y | `evidence_pack` |
| `sgn.evidence_packs` | `evp_` | doc_id, manifest, pack_sha256, addenda, sealed_at | T (compliance-mode lock) | EXECUTED_INSTRUMENT_EVIDENCE | `evidence_pack` |
| `sgn.bsa63_certificates`, `sgn.validation_reports` | — | subject docs, part A, part B status; LTV status | T | EXECUTED_INSTRUMENT_EVIDENCE | `evidence_pack` |
| `sgn.bulk_batches` | `sgb_` | template_ver, rows, state, report | T | ROLLING_7Y | `signing_request` |
| `sgn.public_verifications` | — | sha256 prefix, result | P | ROLLING_180D | — |

### B.2.12 `ai` and `agt` (owner P09)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `ai.models`, `ai.prompt_templates`, `ai.eval_sets`, `ai.eval_runs` | — | provider, model_id, region pairs, approved data classes; prompt hash | X | PERMANENT | — |
| `ai.runs`, `ai.run_steps`, `ai.citations` | `run_` | user/agent, skill, route decision, model_id, prompt_hash, data_class, state, credits, output_hash; steps; resolved citations | T | AI_RUN_7Y (metadata); content AI_CONTENT | `ai_output`; `ai_run_ledger_extract`† |
| `ai.conversations`, `ai.messages` | `aic_`, `aim_` | folder, language, problem_card | T | User-controlled; legal hold aware | `ai_conversation` |
| `ai.notebooks`, `ai.notebook_sources`, `ai.chunks` | `nbk_` | scope, source version, locator, embedding (pgvector, per-tenant partition) | T | FOLLOWS_PARENT | `ai_notebook` |
| `ai.qrg_reviews` | `qrv_` | run_id, draft_ver_id, reviewer, eligibility basis, attestation, decision, sla_due | T | OPS_8Y | `ai_qrg_review`† |
| `ai.guardrail_events` | — | guardrail_id, severity, action | T | AI_GUARDRAIL_1Y | — |
| `ai.memory_items` | — | scope, owner, text, source_run, status | T | until deleted | `ai_memory_item`† |
| `ai.usage_meter` | — | credits, bucket | T | BOOKS_8FY | `statement` |
| `agt.catalogue` | — | code `AGT_…` (Appendix H roster, X-27), card, version | X | PERMANENT | — |
| `agt.tenant_agents`, `agt.envelopes`, `agt.autonomy_changes` | `agt_` | sponsor, scope, autonomy, budget, state; envelope version; from/to, checker | T | TENANT_LIFE_8Y / PERMANENT | `agent_mission` |
| `agt.missions`, `agt.mission_steps`, `agt.schedules` | `msn_` | template, owner, budget, state; step owner, checkpoint; rrule, grant_id | T | OPS_8Y | `agent_mission` |
| `agt.activity_log` (append-only) | — | agent, run, record_ref, action_class, outcome, undo_until, ledger_hash | T | OPS_8Y | `agt_activity_log` |
| `agt.kill_switches` | — | view over `cfg.kill_switches` scope `AI_AGENT` (R-A-09) | T | — | — |
| `agt.mcp_clients`, `agt.mcp_tool_admissions`, `agt.a2a_cards` | — | client basis, tool hash, card JWS | T / P | PERMANENT while active | `connector` |

### B.2.13 `pld` (owner P10)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `pld.projects` | `pld_` | tpl_version_id, drf_id, profile_code, forum, State, who_files, status, cas_id | T | LIT_RECORD | `pleading` |
| `pld.render_profiles`, `pld.limitation_rules`, `pld.court_fee_rules` | — | tokens, status, source, verified_by/on | X / T | PERMANENT | — |
| `pld.component_instances`, `pld.annexure_maps`, `pld.validation_runs`, `pld.filing_packs`, `pld.affidavits` | — | kind, order; label, source ver, kind, pages; findings; manifest; jurat, sworn scan, similarity | T | LIT_RECORD | `pleading` |
| `pld.notices`, `pld.dispatches` | `ntc_` (`LD-NTC-…`) | kind, sender_mode, recipient_enc, doc_ver_id, status, delivered_at; mode, tracking, evidence | T | LIT_RECORD (≥ 8 y) | `notice` |

### B.2.14 `lit` (owner P11)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `lit.matters` | `mat_` (`LD-MAT-…`) | type, title, our_role, owner, claim, status, stage, confidentiality, privilege_default, exposure_class, owner_system, sor_mode | T | LIT_RECORD | `matter` |
| `lit.cases`, `lit.case_identifiers` | `cas_` (`LD-CAS-…`) | matter_id, forum_code, case_type, filing_date, stage, status, next_date, disposal, parent_case_id; CNR and schemes | T | LIT_RECORD | `court_case` |
| `lit.case_field_provenance` | — | field, value, source, fetched_at | T | closure + 3 y | `court_case` (dataset) |
| `lit.forums` | — | code, class, State, calendar, id schemes, coverage | X | PERMANENT | — |
| `lit.matter_parties` | — | party_ref, role, advocate_text, variants, mask_in_reports | T | LIT_RECORD | `matter` |
| `lit.docket_entries` (append-only) | — | seq, entry_type, document_version_id, corrects_entry_id | T | LIT_RECORD | `matter` |
| `lit.hearings`, `lit.cause_list_matches` | `hrg_` | date, session, court/item no, purpose, mode, outcome, next_date, state | T | LIT_RECORD / ROLLING_2Y | `hearing` |
| `lit.orders`, `lit.order_directions` | `odr_` | date, type, source, document_version_id, digest_drv_id, certified copy; direction owner, due, task, clock, status | T | PERMANENT (orders) [REC] / LIT_RECORD | `order` |
| `lit.clocks` | `clk_` | subject, rule_code, version, start, due, internal target, outer cap, owner, state, verified | T | LIT_RECORD | `item_clock` |
| `lit.counsel_panel`, `lit.counsel_people`, `lit.assignments` | `cnl_` | firm, enrolment text, areas, rate card, status; case/eng, role, vakalatnama status | T | panel exit + 8 y / LIT_RECORD | `matter` (06 Counsel and Costs) |
| `lit.budgets`, `lit.spend_invoices`, `lit.accruals` | `lsi_` | amounts, GST/TDS treatment, validation, state, approver | T | BOOKS_8FY | `matter` (06 Counsel and Costs) |
| `lit.exposure_assessments`, `lit.exposure_schedules` | `exa_` | quarter, class, best estimate, range, rationale; snapshot_hash, frozen_at | T | BOOKS_8FY | `matter` (Exposure Schedule) |
| `lit.bundles`, `lit.bundle_items` | — | kind, version, page map, locked_hash | T | LIT_RECORD | `court_case` (09 Bundles) |
| `lit.party_watches`, `lit.party_watch_hits` | — | terms, forums, adapter; minimal payload, decision | T | ROLLING_1Y (hits); 90 d dismissed | `matter`† dataset |
| `lit.adr_referrals` | — | process, provider, prechecks, pack hash, consentref, channel, state, outcome | T | LIT_RECORD | `matter` (07 Settlement and ADR) |
| `lit.projections_rs` | — | rs_case_ref, fields, seq | T (read-only mirror) | per RS retention notice | `matter` (labelled mirror) |
| `lit.alert_subscriptions`, `lit.sync_runs` | — | user, event, channel, consent; adapter counts | T / P | ACCOUNT_LIFE_1Y / SEC_LOG_1Y (180 d in India) | — |

### B.2.15 `ipm` (owner P12)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `ipm.assets` | `tmk_` (`LD-TMK-…`) | type, title, owner_ref, joint owners, jurisdiction, status, status_raw, source, business owner | T | IP_ASSET (life + 8 y after lapse) | `ip_asset` |
| `ipm.trademarks`, `ipm.copyrights`, `ipm.designs`, `ipm.patents`, `ipm.domains`, `ipm.confidential_items` | — | type-specific fields (mark, classes, application no., dates, valid_until) | T | IP_ASSET | `ip_asset` |
| `ipm.status_events` (append-only) | — | seq, state, raw label, published_on, source, evidence, corrects_seq | T | IP_ASSET | `ip_asset` |
| `ipm.field_provenance`, `ipm.screenings` | — | field, source; query, results, score | T | ROLLING_3Y | `ip_asset` (datasets) |
| `ipm.data_sheets`, `ipm.watch_profiles`, `ipm.watch_hits` | — | TM-A payload, validation, state; classes, sensitivity; score, opposition last date, decision | T | OPS_8Y / while active / ROLLING_3Y | `ip_asset` |
| `ipm.journals`, `ipm.journal_entries` | — | journal no., file hash, parse quality; entry fields | X (public publication) | PUBLIC_PUBLICATION / ROLLING_5Y | — |
| `ipm.ip_agreements_links`, `ipm.use_evidence`, `ipm.valuation_notes`, `ipm.enforcement_log` | — | agr_id, role, recordal status; year, docs; cost basis; sightings | T | IP_ASSET | `ip_asset` |
| Clocks | — | reuse `lit.clocks` (`subject_type = IPM_ASSET`) | T | IP_ASSET | `item_clock` |

### B.2.16 `lgo`, `gov`, `hr`, `hr_posh` (owner P13; kernels NN-47)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `lgo.requests`, `lgo.request_events` | `lrq_` (`LD-LRQ-…`) | channel, requester, department, category, priority, state, owner, SLA dues, converted_ref, outcome, rating | T | OPS_8Y (after closure) [REC] | `legal_request` |
| `lgo.categories`, `lgo.routing_rules`, `lgo.sla_policies`, `lgo.sla_timers` | — | form, priority rule, SLA, routing ref, self-service; timers | T | while active + 3 y | `legal_request` |
| `lgo.waiting_items` | view | over `wf.items` (X-09) | T | — | `item` |
| `lgo.licences`, `lgo.doa_matrix`, `lgo.budgets`, `lgo.duty_assignments`, `lgo.digests` | — | type, number, authority, valid_to; bands, approvers, board_ref; FY budgets; duties; digests | T | expiry + 8 y / PERMANENT / BOOKS_8FY / OPS_8Y / ROLLING_3Y | `legal_request` / `policy_version` |
| `lgo.calendar_items` | materialised view | source, due_on, verified, owner | T | rebuilt | — |
| `gov.*` (kernel: `entity_profiles`, `blueprint_lines`, `bodies`, `body_members`, `meetings` `mtg_`, `agenda_items`, `packs`, `attendance`, `decisions`, `minutes`, `resolutions` `res_`, `register_events` append-only, `officer_roles`, `declarations`) | kernel | per kernel; minutes sealed hash | T | MINUTES_AND_REGISTERS (permanent) | `meeting`, `resolution`, `register` |
| `hr.*` (kernel: `persons`, `employments`, `establishments`, `departments` (`dep_` shared), `positions` (`pos_` shared), `leave_*`, `attendance_events`, `pay_runs`, `payslips`, `documents`, `acknowledgements`) | kernel | per kernel | T (restricted class HR) | EMPLOYEE_RECORDS [VERIFY] | `employee`, `kmp_record` (`07 People and HR/ [R]`) |
| `hr_posh.ics`, `hr_posh.cases`, `hr_posh.case_events` | kernel | separate KMS key | S | EMPLOYEE_RECORDS | `hr_posh_case`† (IC-only export) |

In `ldc_sor` mode `gov`/`hr` are not populated; read-through facts come from LDC (FR-P19-29, FR-P19-33).

### B.2.17 `bsv` and `tax` (owner P14)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `bsv.service_profiles`, `bsv.fee_schedules` | `svc_` + version | entity types, questionnaire, checklist, authority, forms, performer class, renewal rule; fee formula, source URL, verified_at | X | PERMANENT | — |
| `bsv.orders` | `eng_` (`LD-ENG-…`) | svc_id + version, state, answers, SLA started/paused, application refs | T | OPS_10Y [VERIFY] | `service_order` |
| `bsv.order_fee_lines`, `bsv.checklist_items`, `bsv.milestones`, `bsv.assignments` | — | line type, supplier, amount, GST treatment, receipt; item, party, status; milestone dates, evidence; performer, credential snapshot | T | FOLLOWS_PARENT | `service_order` |
| `tax.profiles` | — | taxpayer `prs_`/`ent_`, pan_hash, pan_masked, regime by year | T | TENANT_LIFE_8Y | `tax_filing` |
| `tax.filings`, `tax.computations` | `tfl_` | tax_year, governing act, form, state, data_hash, ack_no, everified_at; versioned lines, rule pack | T | TAX_8Y | `tax_filing` |
| `tax.section_map` | — | concept, 1961 ref, 2025 ref, status, reviewer | X | PERMANENT | — |
| `tax.calendar_items` | — | entity, duty, period, due_at, source (LOCAL/LDC) | T | TAX_8Y | `tax_filing` |

### B.2.18 `chp` (owner P15; Consumer Help cell, X-17)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `chp.cases` | `grv_` (`LD-GRV-…`) | vertical, issue, opposite_party_norm, opp_identifiers_hmac, state, forum_step, amounts, fee_plan_id, conflict_result | T + staff entity scope + wall | CHP_CASE | `consumer_case` |
| `chp.case_deadlines` | — | rule_row_id, version, inputs, due_at | T | CHP_CASE | `consumer_case` |
| `chp.evidence_items`, `chp.harassment_incidents` | — | doc_id, sha256, channel; occurred_at, caller_hash, agency, breach flags | T | CHP_CASE / CHP_THIRD_PARTY | `consumer_case` |
| `chp.authorities`, `chp.consent_links`, `chp.fee_plans` | — | representative, forum, scope, valid_to; cns_id; model, caps, disclosure | T | CHP_CASE / consent rule / CHP_FEES | `consumer_case` |
| `chp.conflict_check_logs` | — | identifiers_hmac, epoch, result, category (no consumer data) | T | CHP_CONFLICT_LOG | — |
| `chp.challans`, `chp.vehicles`, `chp.vehicle_sales` | `chl_`, `veh_` | challan no., offence, amount, State, state, receipt; reg no., RC, hypothecation; sale dates, Vahan no. | T | OPS_8Y / account life / OPS_8Y | `challan_record`, `vehicle_record` |
| `chp.wall_breach_logs` | — | actor, attempted resource, rule | T | ROLLING_5Y [REC] | — |

### B.2.19 `mkp` and `aca` (owner P16)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `mkp.categories`, `mkp.services`, `mkp.service_packages` | `svc_` | code, version, service_class, delivering party type, seller entity, scope, exclusions, deliverables, price model, OH8 SKU ref, stream code, SLA template, status | X (public read LIVE) | PERMANENT (versions) | — |
| `mkp.offers` | `ofr_` | engagement, version, lines (supplier, stream, amount ref), validity, letter, hash, status | T | OPS_8Y | `engagement` |
| `mkp.engagements` | `eng_` (`LD-ENG-…`) | buyer, service+version, model (M1/M2/M3, X-21), supplier_pro_id, state, scope/price snapshots, OH8 refs, letter, conflict_check_id, independence | T (practitioner via grant) | OPS_8Y [REC]; legal hold aware | `engagement` |
| `mkp.milestones`, `mkp.change_requests` | `ecr_` | seq, due, state, deliverables, accepted, deemed; delta scope/price/timeline, state | T | OPS_8Y | `engagement` |
| `mkp.retainers`, `mkp.sla_schedules`, `mkp.sla_events`, `mkp.time_entries` | `rtn_`, `sla_` | package, basket, hour bank, cycle, term, state; metrics, credit rule; events; hours (NUMERIC) | T | OPS_8Y | `retainer` |
| `mkp.professionals` | `pro_` | kind, profession codes, OH9 ref, KYC ref, practice areas, capacity, PI cover, Route linked account, status | P (self-read) | OPS_8Y; DPDP erasure for unused profiles | `professional` (own) |
| `mkp.profession_rules` | — | switch values, counsel_opinion_ref, maker, checker, effective_from | P | PERMANENT | — |
| `mkp.assignments`, `mkp.conflict_checks` | — | offered_at, response, basis, seed; party hashes, result, cleared_by | T | OPS_8Y | `engagement` |
| `mkp.reviews`, `mkp.private_feedback` | `rev_` | target LAWDOCS_SERVICE only, rating, consent_ref, status; internal scores | public read PUBLISHED / delivery only | ROLLING_3Y after display | `review`† (own) |
| `mkp.disputes`, `mkp.payout_instructions` | — | category, state, outcome, credit note ref; Route transfer ref, amount ref, TDS, idempotency key, reconciled_at | T / P + practitioner own | OPS_8Y (tax) | `engagement` |
| `aca.courses`, `aca.feed_runs`, `aca.certificates` | — | course fields, feed hash; run status; certificate no., file, consent | X / T | PERMANENT / per vault | `aca_certificate`† |

### B.2.20 `bil` and `sav` (owner P17; engine OH8)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `bil.catalogue_versions`, `bil.presentation_versions`, `bil.plans`, `bil.feature_rows`, `bil.price_history` | `pln_` | signed OH8 catalogue copy; presentation (maker/checker); plan mirror; rows; 30-day prior price | X | PERMANENT | — |
| `bil.subscriptions_mirror`, `bil.trials` | — | OH8 subscription ref, plan, state, term, renewal, auto_renew; trial dates | T | BOOKS_8FY | `statement` |
| `bil.entitlements_applied` | `etl_` | version, modules, limits, JWS, applied_at | T | BOOKS_8FY | `statement` |
| `bil.credit_lots`, `bil.credit_ledger` | — | type, qty (NUMERIC), source, expires_at, state; delta, reason, source_event_id unique | T | BOOKS_8FY | `statement` (`credit_ledger`) |
| `bil.meter_events`, `bil.usage_statements` | — | meter, qty, source_event_id; period, quantity, hash, dispute_state | T | BOOKS_8FY | `statement` |
| `bil.billing_profiles` | — | legal name, GSTINs, place of supply, PAN, contacts, PO rules, LUT, TDS | T (RESTRICTED) | TENANT_LIFE_8Y | `organisation_profile` |
| `bil.documents_mirror` | `inv_` | type (invoice, credit note, receipt, statement), number, supplier, FY, amounts ref, pdf_doc_id, hash | T | TAX_8Y | `invoice_mirror`, `credit_note`, `receipt`, `statement`, `tds_certificate` |
| `bil.payments_mirror`, `bil.order_mirror` (P00) | `pay_` | Razorpay payment id, method class, amount ref (no card data); business_ref `LD-ORD-…`, OH8 ref | T | TAX_8Y | `receipt` |
| `bil.stream_registry`, `bil.stream_switch_history` | — | RS-LD-01…45 fields; switch from/to, maker, checker, effective_from | P | PERMANENT | — |
| `bil.saved_configs` | — | token_hash, config, expires_at | P | short (expiry) | — |
| `sav.methodologies`, `sav.baselines`, `sav.benchmarks`, `sav.penalty_bindings` | — | versions; source, date, last_verified_at | X / T overrides | PERMANENT | — |
| `sav.tenant_inputs`, `sav.snapshots` | — | hourly bands, replaced costs, evidence; period, methodology version, tiles (value, class, inputs), hash | T | BOOKS_8FY | `savings_entry`, `value_report` |

### B.2.21 `sdc` and `cvl` (owner P18)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `sdc.staff_projection` | — | usr_id, OH employee id, brand scope, roles, practice, manager, status, scim_id | staff plane | OPS_8Y | — |
| `sdc.assignments` | — | tenant, usr, role, refs, start/end, capacity | T + staff | OPS_8Y | — |
| `sdc.delivery_grants` (1:1 with `iam.grants`) | `grt_` | grantee, kind, scope, actions, data_class_max, purpose, basis, checker_binding, valid period, state, standing_auth_id, version | T | OPS_8Y | `delivery_grant` |
| `sdc.standing_authorisations` | — | scope, max makers, role filter, valid_to, approved_by, evidence | T | OPS_8Y | `delivery_grant` |
| `sdc.sessions` | `dls_` | grt_id, kind (DELIVERY, SUPPORT, BREAK_GLASS), started/ended, ip, device hash, reason | T | SEC_LOG_1Y + ledger | `access_log` |
| `sdc.deliverables` | `dlv_` | engagement_ref, type, version, doc_id, sha256, status, author, reviewer, client decision | T | OPS_8Y | `deliverable` |
| `sdc.drive_links`, `sdc.meetings`, `sdc.notes` | `dmt_` (meetings) | provider, kind, URL, residency class, delegated consent; join URL, attendees, agenda/notes docs; notes body_enc | T | OPS_8Y | `sdc_meeting` |
| `sdc.masterdata_requests` | `mdc_` | field key, class, current/proposed (enc), evidence, raised_by, client decision, checker, state, correction_entry_id, review window | T + console | LEDGER | `change_request` |
| `sdc.sla_clocks` | — | sla_id, subject, started, paused intervals, due, state, breach | T | OPS_8Y | `retainer` (SLA reports) |
| `sdc.time_entries`, `sdc.metrics_monthly`, `sdc.health_snapshots` | `tme_` | minutes, billable, category; monthly KPIs (NN-33: outcome and SLA only); health score | staff + T / staff / T | OPS_8Y / OPS_8Y / ROLLING_3Y | `retainer` (client-visible hours only) |
| `sdc.practitioner_links` | — | pro_org_id, grt_ids, billing mode | T + practitioner org | OPS_8Y | `delivery_grant` |
| `cvl.vault_settings`, `cvl.entry_types` | — | enabled, enabled_by, checked_by, per-reveal default, allowed hours; type code, URL allow-list, delegation route, client_only, blocked | T / X | OPS_8Y / versioned | `credential_entry` (metadata) |
| `cvl.entries` | `cvl_` | type, URL, username_enc, secret_enc (per-tenant DEK), owner, custodians, rotation, expiry | T (sealed class) | until archived + 1 y; secrets crypto-shredded on archive | `credential_entry` (metadata only, never secrets) |
| `cvl.grants`, `cvl.reveal_events` (append-only), `cvl.rotation_tasks` | — | grantee, mode, valid period, per-reveal approval; purpose, approved_by, outcome, revealed_at, anomaly flags; reason | T | OPS_8Y / LEDGER / OPS_8Y | `credential_entry` (reveal log) |

### B.2.22 `int` (owner P19)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `int.clients`, `int.client_tenant_consents`, `int.api_keys` | — | type, purpose, scopes, data_class_max, auth method, JWKS, cert thumbprint, redirect URIs, expiry; consent `cns_`; key prefix, Argon2id hash | T | ROLLING_7Y | `connector` |
| `int.idempotency_keys` | — | client, key, body_hash, status, response_ref | T | TRANSIENT_24H (≤ 7 d) | — |
| `int.webhook_subscriptions`, `int.deliveries` | — | URL, event types, data class max, secrets refs, status; attempt, status, latency | T | life + 1 y / 90 d metadata | `connector` |
| `int.inbox`, `int.dlq`, `int.replay_requests` | — | source, event_id, subject, seq; reason, attempts; filter, requested_by, approved_by | T | INBOX_365D / DLQ_90D / ROLLING_7Y | — |
| `int.event_type_map`, `int.connectors`, `int.mapping_packs` | — | internal ↔ ecosystem type, direction, ceiling, contract status; manifest, residency, certification, kill switch key; YAML packs | X | versioned | — |
| `int.mapping_overrides`, `int.connector_instances` | — | patch version, maker, checker; connector, version, state, owner, health | T | life + 1 y | `connector` |
| `int.links` | — | kind, counterpart product/org/tenant, purposes, data classes, contracts, valid period, approvals, state | T | TENANT_LIFE_8Y | `ecosystem_share` |
| `int.sharing_ledger` (append-only, hash-chained) | — | direction, link, counterparty, contract, purpose, consentref, legalbasis, record ids, payload sha256, data class, outcome | T / U | LEDGER (8 y) | `ecosystem_share` |
| `int.partners`, `int.onboarding_batches`, `int.onboarding_invitations` | — | partner type, agreement, regulated_professional flag; batch rows; invitation (contact enc) | P / partner | life + 8 y / ROLLING_3Y (contact erased 90 d after EXPIRED/DECLINED) | — |
| `int.sor_switches`, `int.reconciliation_reports` | — | kernel, from/to product, state, report doc; business date, counts, hashes, breaks | T | OPS_8Y | `ecosystem_share` |
| `int.deposit_links` | — | user, client, folder, pairwise ref, state | U | life + 1 y | `ecosystem_share` |
| `int.rate_limit_overrides`, `int.sandbox_tenants`, `int.lookup_costs` (P01) | — | tier, limits; sandbox persona; provider, unit cost, purpose | P | ROLLING_3Y / 30 d after last use / OPS_8Y | — |

### B.2.23 `xpt` (owner P20; registry head P00)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `xpt.export_map` | — | record_type, profile, profile_version, module, path_template, file templates, dataset columns, restricted_class, retention_class, stability_key, legacy_path_template | X (loaded from YAML) | PERMANENT | — |
| `xpt.folder_policies` | — | version, options | T | PERMANENT | `setting_value` |
| `xpt.export_jobs`, `xpt.export_files` | `exp_` | scope, filters, profile, as_of, state, approvals, checkpoints, archive_id; path, sha256, record ref | T | ROLLING_7Y | `export_job` |
| `xpt.storage_targets`, `xpt.target_writes`, `xpt.target_conflicts` | `stg_` | provider, config (no secrets), secret_ref, region, residency result, data classes, key mode, write_once, state; idempotency key, path, sha256; conflicts | T | life + 1 y / ROLLING_7Y / ROLLING_3Y | `storage_target` (metadata) |
| `xpt.import_jobs`, `xpt.import_files` | `imp_` | source_kind, source_ref, state, counts, rules, batch_id, undo_until, report; source path, sha256, proposal, confidence, decision | T | ROLLING_7Y | `import_job` |
| `xpt.exit_requests`, `xpt.restore_tests` | — | state, dates, exceptions, certificate; target, result, report | T | PERMANENT / ROLLING_7Y | `export_job` (`00 Start Here/`) |
| `xpt.golden_runs` | — | release, profile, diff, result | X | PERMANENT | — |

### B.2.24 `web` and `hlp` (owner P21; redirects head P00)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `web.pages`, `web.page_versions`, `web.posts`, `web.videos`, `web.landings`, `web.entities` | `pg_`, `pst_`, `vid_` | brand, type, slug, locale group, state; blocks, SEO, summary answer, reviewer, next review, legal flag, claims, citations, hash | P | PERMANENT (immutable versions) | — (platform content) |
| `web.leads` | — | brand, contact (enc), consent refs, UTM, sensitivity, status, OH lead id | P (restricted role) | LEAD_30D (after ACKNOWLEDGED) | — |
| `web.redirects` | — | brand, from_path, to_path, code (301/410), state, hits | P | PERMANENT | — |
| `web.import_jobs`, `web.import_files`, `web.geo_checks` | — | status, warnings, error code; prompt, engine, cited | P | ROLLING_1Y / ROLLING_3Y | — |
| `web.testimonials` | — | order_ref, consent_ref, text, display name, consideration_disclosed, state | P | consent + 1 y | `testimonial`† (own) |
| `hlp.articles`, `hlp.article_versions`, `hlp.terms`, `hlp.term_locales`, `hlp.tours`, `hlp.tutorials`, `hlp.clips` | `trm_`, `tut_` | help keys, roles, locale, state; key `hlp.<module>.<term>`, legal ref; steps; script, assets | P | PERMANENT | — |
| `hlp.tenant_notes`, `hlp.user_prefs` | — | help_key, body, author; theme, text scale, motion, captions | T | tenant life / account life | `customisation` |
| `hlp.a11y_issues` | — | surface, severity, state, reporter contact (enc, optional), SLA due | P (restricted) | ROLLING_3Y | `a11y_issue`† (own) |

**Resolution R-B-03:** P00 `web.redirects (source_host, source_path, target_url, status)` and P21 `web.redirects (brand, from_path, to_path, code, state)` describe one table; P21 columns govern (owning phase); P00's `source_host` maps to `brand` via `core.tenant_domains`.

### B.2.25 `mob` (owner P22)

| Table | Id | Key columns | RLS | Retention | Export |
|---|---|---|---|---|---|
| `mob.devices` (extends `iam.devices`) | `dev_` | platform, model, OS/app version, public key, attestation verdict, integrity, state | U | 1 y after revoke | `mob_device`† |
| `mob.push_tokens` | — | provider, token (enc), categories, quiet hours | U | until pruned | `mob_push_preferences`† |
| `mob.deep_link_tokens` | — | token_hash, purpose, target, contact, expiry, max uses | T | 90 d after expiry | — |
| `mob.upload_jobs`, `mob.capture_metadata` | — | manifest (hashes, sizes), status; page hashes, pdf hash, device model (optional) | T | 30 d after DONE / FOLLOWS_PARENT | `version` (capture metadata beside the document) |
| `mob.app_versions`, `mob.ota_releases` | — | min supported, recommended; channel, runtime version, change ref, rollout pct | P | PERMANENT | — |
| `mob.store_receipts` | — | product, original transaction id, state, verified_at, entitlement ref | U | TAX_8Y [TAX MEMO] | `receipt` |

### B.2.26 `eng` (owner P23; platform scope, staff-only RLS)

All `eng` tables are platform records excluded from tenant exports (`x-export: excluded`, reason "platform engineering records"); tenant-visible release notes and maintenance notices map to `platform_notice`. Retention `PLATFORM_ENG_8Y` unless noted: `eng.change_records` (`chg_`, `CHG-YYYY-NNNNNN`; class, PRs, commits, risk score, plans, approvals, OH13 change id, approval version, window, state, PIR), `eng.releases` (`rel_`; version, tag, digests, SBOM, rings, state, regulatory impact), `eng.deployments`, `eng.freeze_windows` and `eng.change_calendar` (3 y), `eng.vulnerabilities`, `eng.risk_acceptances`, `eng.eos_register`, `eng.service_catalogue` (RPO/RTO), `eng.restore_tests`, `eng.dr_drills`, `eng.vapt_engagements`, `eng.vapt_findings`, `eng.incidents` (clocks, notifications), `eng.control_evidence`, `eng.evidence_packs` (audit packs; not `evp_`), `eng.access_reviews` (staff), `eng.claims_register` (PERMANENT; NN-20 claims gate), `eng.golive_checklists`, `eng.golive_items` (PERMANENT), and P00's `eng.disposition_register`, `eng.decommission_certificates`.

---

## B.3 Canonical entity ownership against the Ecosystem Spec (owner code `LD`)

LawDocs registers as owner code **`LD`** (Appendix Y §Y.3.5; NN-24). Principle 2 of the Spec allows one owner per entity per tenant; `owner_system` on every row records it.

### B.3.1 Entities LawDocs owns (Appendix Y §Y.5.1)

| Spec # | Entity | LawDocs source | Projection rules (copies) | Data class ceiling |
|---|---|---|---|---|
| 46 | `agreement` | `clm.agreements` (+ versions, stamp refs) | LDC under `legal_sor_link`; FX when linked to a recovery case; EQ only inside a referral pack. Status projection R-A-14 | `LEGAL` (privileged fields `x-privileged`) |
| 47 | `signing_request` | `sgn.signing_requests` (LawDocs as hosting ASP) | Requesting product receives status and evidence by reference only (principle 15); never consent logs or ESP XML | `PII` |
| 48 | `stamp_instrument` | `sgn.stamp_instruments` | Requesting product; EQ inside a referral pack | `FINANCIAL` |
| 49 | `legal_matter` | `lit.matters` | LDC projection; LDC P26 owns only where no LD tenant exists (X-06; `lit.sor.mode`) | `LEGAL` |
| 50 | `court_case` | `lit.cases` (+ hearings, orders as children) | LDC projection; linked by reference to #24 `litigation_case` where the same proceeding is a recovery case (RS wins for recovery fields) | `LEGAL` |
| 51 | `ip_asset` | `ipm.assets` | LDC opt-in projection | `CONFIDENTIAL` |
| 52 | `engagement` | `mkp.engagements` (+ `bsv.orders`) | OH commercial fields only; scope and deliverables stay `CONFIDENTIAL` in LD | `INTERNAL` to OH |
| 53 | `retainer` | `mkp.retainers` | OH commercial fields only | `INTERNAL` to OH |
| 54 | `contract_obligation` | `clm.obligations` | LDC projection | `CONFIDENTIAL` |

### B.3.2 Existing Spec entities amended for LawDocs (Appendix Y §Y.5.2)

| Spec # | Entity | LawDocs role | LawDocs source |
|---|---|---|---|
| 20 | `notice` | Producer for non-recovery instruments only (`GENERAL_LEGAL_NOTICE`, `CONTRACT_NOTICE`, `REPLY_NOTICE`, `CONSUMER_NOTICE`) | `pld.notices` |
| 23 | `adr_case` | Referrer (non-loan disputes) and party-view consumer | `lit.adr_referrals` |
| 24 | `litigation_case` | Read-only consumer for the RE's own legal department (`finbyx_legal_link`) | `lit.projections_rs` |
| 25 | `hearing`, `order` | Children of #50 in LawDocs | `lit.hearings`, `lit.orders` |
| 28 | `document` | Producer; adds `origin`, `vault_scope`, `rendition_of`, `evidence_pack_ref`, `privileged`, `bsa63_certificate_ref` (reconciles "vault_document") | `dms.documents`, `dms.versions`, `dix.renditions` |
| 29 | `consent_artefact` | Capturer; methods `IN_APP_AUTHORISATION`, `CONSENT_MANAGER`; new purpose codes | `kyc.consents` |
| 38 | `plan`, `entitlement`, `invoice`, `subscription_payment` | Consumer (copies) | `bil.*_mirror`, `bil.entitlements_applied` |
| 39 | `usage_aggregate` | Producer | `bil.usage_statements` |
| 40, 41 | `export_job`, `archive`, `storage_target` | Producer; profiles `ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1` (X-08) | `xpt.*` |
| 42 | `professional`, `matter_allocation` | Consumer of `professional` (Rule 36 fields only); producer of `matter_allocation` (`CLIENT_CHOICE`, counts-only) | `mkp.professionals`, `mkp.engagements` |
| 44 | `group_grant` | Consumer (SCIM to `ld-staff`) | `iam.grants` (group type) |

### B.3.3 Entities LawDocs consumes but never owns

Governance facts and KMP (LDC or FX as governance SoR; read on demand under `governance.resolution:read` / `governance.kmp:read`, no caching beyond the request); minimal people projection (HRMS SoR, `hr.employee:read.minimal`); tenant provisioning, catalogue, plans, entitlements, invoices and payments (OH, OH8); professional empanelment (OH9); recovery litigation (RS); ADR case states (EQ). LawDocs stores only the projection fields it needs, labelled with `owner_system`.

### B.3.4 Data that never leaves LawDocs

Consumer Help case data (class `CONSUMER_HELP`, principle 14; NN-23); credential vault entries and reveal logs (NN-16); AI conversations, notebooks and memory (NN-15); drafts and their answers; internal negotiation comments and decisions (NN-37); delivery-staff metrics at person level (NN-33); anything to the Operations Hub beyond aggregates and commercial records (NN-19; X-13 billing-identity exception for `CONTRACT_PERFORMANCE_CUSTOMER`).

---

## B.4 Event register

### B.4.1 Envelope and delivery rules (both families)

- CloudEvents 1.0; `id` UUIDv7; `type` `in.lawdocs.<module>.<EventName>.v<n>` (internal and tenant webhooks) or `in.infrabyx.<domain>.<EventName>.v<n>` (ecosystem, published only by `int`); `source` `urn:lawdocs:<module>` internally and `urn:infrabyx:lawdocs:<tenantid>` for ecosystem; `subject` the aggregate id; `seq` per subject; `dataclass` = highest field class; `consentref` or `legalbasis` on every ecosystem message carrying personal data (NN-24); `traceparent`.
- Transactional outbox in the same database transaction as the state change (NN-45); idempotent inbox keyed `(source, id)`; FIFO per subject; gap → park 15 minutes → catch-up `GET /v1/events?after=` (FR-P00-45, P19 §5.4).
- Payloads are **thin**: IDs, business refs, codes, hashes, dates, counts. Never document content, answers, Aadhaar, OTPs, secrets or full PAN (NN-32). Names PascalCase past tense.
- Tenant webhooks may subscribe only to events marked **W** below; data class `INTERNAL` unless the subscription is raised to `PII`, never `LEGAL` (Appendix I §I.7). Consumer Help (`chp`) events are never subscribable and never mapped by `int` (NN-23).

### B.4.2 Internal events `in.lawdocs.*` by module

Column **Consumers** uses module codes; `ntf` notifications, `rpt` reports, `xpt` exports, `int` (ecosystem mapping in §B.4.4) and **W** (tenant webhook). Every event is also written to the audit ledger by its producer. Events marked **(+X1)** were named in a phase §5 but missing from its §7.4 and are registered here (owning phase adds them at the next integration).

**`core` (P00)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `core.TenantProvisioned` | Provisioning READY; tenant_id, kind, brand, created_via | `cfg`, `int` (OH ack), `bil` |
| `core.TenantStatusChanged` | Status change; from, to | `iam`, `bil`, `int` |
| `core.LegalEntityRegistered`, `core.LegalEntityAmended` | Entity created/changed; entity_id, fields changed | `kyc`, `org`, `gov` |
| `core.CorrectionSubmitted`, `core.CorrectionApplied`, `core.CorrectionReversed` | A.1; correction_id, target kind, target ref | `ntf`, `rpt`, module owning the target |
| `core.AuditAnchorPublished`, `core.AuditChainBroken` | Daily anchor; chain broken alert | `eng` (incident), `rpt` |
| `core.BreakGlassStarted`, `core.BreakGlassEnded` | Break-glass session; tenant, actors, reason | `ntf` (client ≤ 24 h), `sdc` |
| `core.MigrationRunPromoted`, `core.LegacySystemDecommissioned` | A.63 | `eng`, `rpt` |

Aliases retired (R-A-09): `core.FeatureFlagChanged` → `cfg.FlagChanged`; `core.KillSwitchChanged` → `cfg.KillSwitchEngaged`/`Released`.

**`iam` (P01, P02)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `iam.UserRegistered`, `iam.ContactPointVerified`, `iam.MfaFactorChanged`, `iam.SessionsRevoked`, `iam.AccountRecovered` | A.3 account lifecycle | `ntf`, `mob`, `rpt` |
| `iam.MembershipChanged`, `iam.InvitationSent`, `iam.GuestUpgraded` | Membership and invitations | `ntf`, `org` |
| `iam.SsoConfigured`, `iam.ScimUserDeprovisioned` | SSO/SCIM | `sdc` (leaver), `ntf` |
| `iam.OnboardingInvitationActivated` | A.2 ACTIVATED | `int` (→ `int.OnboardingInvitationAccepted` W partner; `ops.TenantRegistered`) |
| `iam.RoleGranted`, `iam.RoleRevoked`, `iam.CustomRolePublished` | Roles | `rpt`, `ntf` |
| `iam.GrantProposed`, `iam.GrantActivated`, `iam.GrantEnded` | A.9 (non-delivery grants) | `ntf`, `dms` (nominee), `rpt` |
| `iam.DelegationStarted`, `iam.DelegationEnded`, `iam.SodViolationBlocked`, `iam.AccessReviewCompleted` | A.10 | `ntf`, `rpt`, `int` (counts to OH, PLATFORM scope) |

**`kyc` (P01)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `kyc.VerificationCompleted`, `kyc.VerificationRevoked`, `kyc.IdentityLevelChanged` | A.4; verification_id, method, level (no attributes) | `iam`, `sgn`, `mkp` |
| `kyc.KybCaseVerified`, `kyc.KybStatusChanged` | A.4; legal_entity_id, status | `core`, `org`, `ntf` |
| `kyc.SignatoryAuthorityChanged` | A.4; authority_id, state, limit band | `wf` (DoA), `sgn` |
| `kyc.ProfessionalCredentialChanged` | A.5 | `mkp`, `bsv`, `drf` (reviewer eligibility) |
| `kyc.GuardianshipChanged`, `kyc.NominationChanged`, `kyc.NomineeReleased` | A.8 | `dms`, `ntf` |
| `kyc.ConsentRecorded`, `kyc.ConsentWithdrawn` | A.7; cns_id, purpose | `int` (→ `privacy.Consent*`), every consent-gated module |
| `kyc.NoticeVersionPublished`, `kyc.RightsRequestChanged` | Notice versions; DPDP rights | `iam` (re-consent), `int` (`privacy.DataPrincipalRequest`) |

**`org` (P02)**: `org.UnitCreated`, `org.UnitChanged`, `org.RestructureApplied`, `org.PositionHolderChanged` — unit or position changes; consumers `wf` (owner re-resolution), `iam`, `rpt`, `hr` (kernel projection).

**`cfg` and `rul` (P03)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `cfg.SettingChanged` | OPEN change; key, scope (never values of confidential keys) | cache invalidation (all modules) |
| `cfg.ConfigChangeRequested`, `cfg.ConfigChangeApproved`, `cfg.ConfigChangeActivated` | A.13 | `wf`, `ntf`, cache |
| `cfg.ConfigTemplateApplied`, `cfg.ConfigBundleExported`, `cfg.ConfigBundleImported`, `cfg.FallbackActivated` | A.16; fallback to default | `rpt`, `ntf` |
| `cfg.FlagChanged` | A.17 flag | all modules (flag cache) |
| `cfg.KillSwitchEngaged`, `cfg.KillSwitchReleased` (W, tenant scope) | A.17; scope, target, actor | `agt`, `ai`, `int`, `bil`, `chp`, `ntf`, `cvl` |
| `rul.RuleSetVersionSubmitted`, `rul.RuleSetVersionActivated`, `rul.RuleSetReviewDue`, `rul.RuleSetRetired`, `rul.RuleSetEmergencyBlocked`, `rul.ContentVersionPublished` | A.14 | `lit`/`ipm`/`chp` (deadline recompute), `tpl` (law-change sweep), `sgn` (eligibility), `web` (law-change flag) |

**`wf` (P02, P03)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `wf.ApprovalRequested` (W), `wf.ApprovalDecided` (W), `wf.ApprovalInvalidated`, `wf.ApprovalExecuted`, `wf.ApprovalExpired` | A.11; apr_id, action code, object ref | owning module, `ntf`, `mob` (push) |
| `wf.DoaTablePublished`, `wf.McPolicyChanged` | A.12 | `wf` engine, `rpt` |
| `wf.ItemOpened`, `wf.ItemWaitingStarted`, `wf.ItemWaitingEnded`, `wf.ItemChased`, `wf.ItemEscalated`, `wf.ItemInterimRecorded`, `wf.ItemResolved`, `wf.ItemWaived` (W `wf.Item*`) | A.15; itm_id, type, parent, party type | parent module gates, `ntf`, `rpt`, `sdc` (inbox) |
| `wf.LegalClockWarning` | A.15 legal clock warning | `ntf`, `lgo` |
| `wf.TaskCreated` **(+F1)**, `wf.TaskAssigned` (W) **(+X1)**, `wf.TaskCompleted` **(+F1)** | Task lifecycle (R-A-08; P03 §5.4, §7.4); tsk_id, parent ref, assignee ref, due | `ntf`, `sdc`, `mob`, `rpt` |

**`dms` (P04; ingest P00)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `dms.DocumentUploaded` (W), `dms.DocumentIngested`, `dms.DocumentRejected` | A.18 pipeline; doc_id, ver_id, sha256, origin | `dix`, `rpt`, `bil` (storage meter) |
| `dms.DocumentVersionCreated`, `dms.DocumentMetadataChanged`, `dms.DocumentClassified` | Version/metadata | `dix`, `clm`, search indexer |
| `dms.DocumentArchived`, `dms.DocumentDeleted`, `dms.DocumentRestored`, `dms.DocumentPurged` | A.18 | `xpt` (mirror), indexer |
| `dms.DocumentCheckedOut`, `dms.DocumentCheckedIn`, `dms.CoeditSessionCheckedIn` | Check-out and co-edit | `ntf` |
| `dms.RelationshipLinked`, `dms.RelationshipUnlinked` | Typed relationships | `clm`, `sgn` |
| `dms.AadhaarMaskedAtIngest` | Masking count (no digits) | `rpt`, `eng` (assurance) |
| `dms.DigiLockerDocumentLinked` | URI linked with consent | `kyc` |
| `dms.ShareCreated`, `dms.ShareApprovalRequested`, `dms.ShareAccessed`, `dms.ShareRevoked` (W), `dms.ShareExpired` | A.19 | `ntf`, `int` (`documents.DocumentShared` only on consent) |
| `dms.RedactedCopyCreated`, `dms.IntakeJobCommitted` | Redaction; intake commit | `xpt` |
| `dms.LegalHoldPlaced`, `dms.LegalHoldReleased` | A.20 | `xpt`, `lit`, `ntf` |
| `dms.DisposalApproved`, `dms.HealthFindingRaised`, `dms.HealthFindingResolved`, `dms.ReminderFactSet` | Retention; health rules; reminders | `ntf`, `rpt` |
| `dms.NomineeDesignated`, `dms.NomineeClaimRaised`, `dms.NomineeAccessReleased`, `dms.NomineeClaimCancelled` | A.8 | `kyc`, `ntf` |
| `dms.OfflineCacheWiped` | Device wipe | `mob` |
| `dms.DocumentDeposited` **(+X1)** | A.58 deposit stored | `int` (→ `documents.DocumentDeposited`) |

Appendix I §I.7 webhook names re-keyed: `dms.BulkImportCompleted` → `dms.IntakeJobCommitted`; `dms.DocumentShared` (internal) → `dms.ShareCreated`; `dms.LegalHoldChanged` → `dms.LegalHoldPlaced`/`Released`.

**`dix` (P05)**: `dix.DixJobQueued`, `dix.DixInputRequested`, `dix.DixJobSucceeded`, `dix.DixJobFailed`, `dix.OcrCompleted`, `dix.ChatExportParsed`, `dix.LocaleAmbiguityResolved`, `dix.TypeCopyGenerated` (W; webhook alias `dix.TypeCopyReady`), `dix.TypeCopyCorrected`, `dix.TypeCopyVerified`, `dix.TypeCopyDisputed`, `dix.LanguageDetected`, `dix.TranslationGenerated` (W; alias `dix.TranslationReady`), `dix.TranslationReviewed`, `dix.BacktranslationFlagged`, `dix.CertifiedTranslationRequested`, `dix.CertifiedTranslationDelivered`, `dix.ExtractionProposed`, `dix.ExtractionConfirmed`, `dix.EligibilitySuspectFlagged` (→ `sgn`), `dix.RedactionSuggested`, `dix.AadhaarMaskedLate` (→ `eng` incident), `dix.EngineRegressionBlocked`, `dix.QualityTierChanged`. Payload: job or rendition id, kind, confidence band, language pair; never text. Consumers: `dms`, `pld`, `chp`, `clm` (obligation proposals), `mkp` (certified orders), `bil` (credits), `ntf`.

**`tpl` and `drf` (P06)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `tpl.TemplateVersionSubmitted`, `tpl.TemplateVersionApproved`, `tpl.TemplateVersionReturned`, `tpl.TemplateVersionPublished`, `tpl.TemplateVersionDeprecated`, `tpl.TemplateRetired` | A.26 | `web` (page update), `drf` (holder notices), search |
| `tpl.ClauseVersionPublished`, `tpl.PlaybookVersionPublished`, `tpl.BacklogItemOpened`, `tpl.BacklogItemClosed` | A.26 | `clm` (playbook review), `web` (`noindex`) |
| `drf.DraftStarted` (W alias `drf.DraftCreated`), `drf.DraftCompleted`, `drf.DraftLaneEscalated`, `drf.DraftExported`, `drf.ReviewRequested`, `drf.ReviewDecided`, `drf.DraftHandedOff` | A.27, A.28; drf_id, tpl version, lane | `mkp` (review SKU), `bil` (quota), `clm`/`sgn`/`dms` (hand-off), `rpt` |

**`clm` and `msg` (P07)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `clm.IntakeRequestSubmitted` (W alias `clm.ContractRequestCreated`), `clm.IntakeConverted` | A.29 | `lgo`, `ntf` |
| `clm.AgreementCreated`, `clm.DealRoomOpened`, `clm.ParticipantInvited`, `clm.ParticipantRevoked` | A.30 | `ntf` (NN-34 caps), `rpt` |
| `clm.VersionShared` (W alias `clm.NegotiationRoundShared`), `clm.CounterpartyVersionReceived`, `clm.SilentEditDetected`, `clm.ChangeDecided`, `clm.RoundClosed`, `clm.PlaybookReviewCompleted` | A.30 rounds and changes | `ntf`, `rpt` |
| `clm.ApprovalRequested`, `clm.ApprovalDecided` (W alias `clm.AgreementApproved` when the last step decides), `clm.ApprovalsInvalidated` | Notifications mirroring `wf.*` (R-A-06) | `ntf` |
| `clm.AgreedVersionConfirmed`, `clm.VersionLocked`, `clm.VersionUnlocked`, `clm.HandedOffToSigning` | Lock and hand-off | `sgn` |
| `clm.AgreementExecuted` (W), `clm.AmendmentInitiated`, `clm.RenewalDecisionRecorded`, `clm.AgreementTerminated`, `clm.AgreementExpired`, `clm.AgreementCancelled` | A.30 | `int` (→ `legal.Agreement*`), `rpt`, `sav` |
| `clm.ObligationVerified`, `clm.ObligationOverdue` (W alias `clm.ObligationDue` for the lead-time reminder), `clm.KeyDateApproaching` (W alias `clm.RenewalDue`) | Obligations and key dates | `int` (→ `legal.ContractObligation*`), `ntf`, `lgo` calendar |
| `msg.MessagePosted`, `msg.MessageWithdrawn` | Threads | `ntf`, `mob` |

Consumed: `sgn.SigningCompleted`, `sgn.SigningRequestVoided`.

**`sgn` (P08)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `sgn.EligibilityEvaluated` | Gate decision; doc, family, decision, row ids, rule versions | `rul`, evidence pack |
| `sgn.SigningRequestCreated`, `sgn.SigningRequestSent` (W), `sgn.SignerViewed`, `sgn.SignerConsented`, `sgn.SignatureApplied` (W alias `sgn.SignerSigned`), `sgn.SignerDeclined` (W alias `sgn.SigningDeclined`), `sgn.ChangesRequested`, `sgn.SigningHeld` | A.31 | `clm`, `ntf`, `int` (hand-off events), `bil` (meters) |
| `sgn.SigningCompleted` (W), `sgn.SigningRequestExpired` (W alias `sgn.SigningExpired`), `sgn.SigningRequestVoided` | A.31 | `clm`, `dms`, `mkp`, `chp`, `int` (`esign.SigningRequestCompleted/Expired/Withdrawn`) |
| `sgn.StampQuoted`, `sgn.StampOrdered`, `sgn.StampIssued`, `sgn.StampVerified` (W alias `sgn.StampAttached`), `sgn.StampVerificationFailed`, `sgn.StampMerged`, `sgn.StampCancellationRequested` | A.32 | `bil` (duty line items), `int` (`esign.StampInstrumentVerified`) |
| `sgn.FormalityResolved`, `sgn.FormalityWaived`, `sgn.DocumentExecuted`, `sgn.DocumentSuperseded` | A.33 | `clm`, `dms`, `wf` |
| `sgn.EvidencePackSealed` (W alias `sgn.EvidencePackReady`), `sgn.Bsa63CertificateDrafted`, `sgn.SignatureValidationFailed`, `sgn.LtvRefreshed` | A.33 | `dms`, `pld`, `xpt` |
| `sgn.ProviderHealthChanged`, `sgn.ProviderLicenceExpiring`, `sgn.ProviderRoutingBlocked`, `sgn.BulkBatchCompleted` | A.34; bulk | `eng`, `ntf`, `rpt` |
| `sgn.SigningAssistanceRecorded` **(+F1)** | Assisted signing: mode, helper and witness refs, declarations (P08 FR-P08-57; no health data) | evidence pack, `rpt` (counts only) |

**`ai` and `agt` (P09)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `ai.RunReceived` **(+X1)**, `ai.PlanApproved` **(+X1)**, `ai.RunCompleted`, `ai.RunFailed`, `ai.RunPaused` | A.35; run_id, skill, route, data class, credits | `agt`, `bil` (credits), `rpt` |
| `ai.GuardrailTriggered`, `ai.CitationUnverified`, `ai.AiIncidentOpened` | Validation failures | `eng`, `rpt` |
| `ai.QualifiedReviewRequested`, `ai.QualifiedReviewCompleted` | A.28 | `mkp`, `ntf` |
| `ai.CreditsDebited`, `ai.BudgetThresholdReached` | Credits | `bil`, `ntf` |
| `ai.RouteAttestationDrifted`, `ai.ModelPinChanged`, `ai.ExternalAiAccessed` | Routing and model governance | `eng`, `ntf` (admins) |
| `agt.AgentHired`, `agt.AgentRetired`, `agt.AgentAutonomyChanged`, `agt.AgentDemoted` | A.36 | `ntf`, `rpt` |
| `agt.ActionProposed`, `agt.ActionApproved`, `agt.ActionExecuted`, `agt.ActionUndone` | A.35, A.36 | owning module, `ntf` |
| `agt.MissionStarted`, `agt.MissionCheckpointReached`, `agt.MissionCompleted`, `agt.DigestSent` | A.36 | `ntf` |

Aliases retired: `agt.KillSwitchActivated`/`Released` → `cfg.KillSwitchEngaged`/`Released` (scope `AI_AGENT`).

**`pld` (P10)**: `pld.PleadingProjectCreated`, `pld.PleadingValidated`, `pld.PleadingReviewed`, `pld.FilingPackBuilt`, `pld.PleadingFiled` (→ `lit` case), `pld.AffidavitSworn`, `pld.NoticeDrafted`, `pld.NoticeDispatched` (W), `pld.NoticeDelivered` (W alias `pld.NoticeDeliveryUpdated` for tracking events), `pld.NoticeReturnedUndelivered`, `pld.RenderProfileVerified`, `pld.LimitationRuleVerified`. Consumers `lit` (clocks), `ntf`, `rpt`. No cross-product event (Recovery Suite owns `LegalNoticeIssued`).

**`lit` (P11)**

| Event | Trigger / key payload | Consumers |
|---|---|---|
| `lit.MatterOpened` (W), `lit.MatterUpdated`, `lit.MatterSettled` **(+X1)**, `lit.MatterClosed` | A.39 | `int` (→ `legal.LegalMatter*`), `lgo`, `dms` (hold offer), `rpt` |
| `lit.CaseRegistered`, `lit.CaseStatusChanged` (W), `lit.CaseDataRefreshed`, `lit.CaseDataStale`, `lit.CaseDataConflictDetected`, `lit.CourtDataAdapterDegraded` | A.40 | `int` (→ `legal.CourtCase*`), `bil` (meter), `ntf` |
| `lit.HearingScheduled` (W), `lit.CauseListMatched`, `lit.HearingOutcomeRecorded`, `lit.HearingOutcomeMissing` | A.40 | `int` (→ `legal.CourtHearingScheduled`), `ntf`, `mob` |
| `lit.OrderUploaded` (W), `lit.OrderFetched` **(+X1)**, `lit.OrderConfirmed`, `lit.DirectionTaskCreated` | A.41 | `int` (→ `legal.CourtOrderRecorded`), `wf` |
| `lit.ClockCreated`, `lit.ClockDueSoon`, `lit.ClockBreached`, `lit.ClockClosed` | A.42 | `ntf`, `lgo` (exceptions), `rpt` |
| `lit.CounselAssigned`, `lit.CounselUpdateSubmitted`, `lit.SpendInvoiceApproved`, `lit.BudgetThresholdCrossed` | Counsel and spend | `lgo` (spend roll-up), `ntf` |
| `lit.ExposureAssessed`, `lit.ExposureScheduleFrozen`, `lit.BundleLocked` | Exposure; bundles | `rpt` |
| `lit.ImportCommitted`, `lit.ImportUndone`, `lit.PartyWatchHitReceived`, `lit.AdrReferralSubmitted` | A.21; party watch; A.43 | `xpt`, `int` (→ `adr.ADRReferralCreated`) |

**`ipm` (P12)**: `ipm.AssetCreated` (alias in Appendix I `ipm.AssetRegistered`), `ipm.DataSheetReady` **(+X1)**, `ipm.TrademarkFiled`, `ipm.StatusChanged` (W), `ipm.ExaminationReportReceived`, `ipm.HearingScheduled`, `ipm.TrademarkAdvertised`, `ipm.OppositionReceived`, `ipm.TrademarkRegistered`, `ipm.RenewalWindowOpened` (W alias `ipm.DeadlineApproaching` for lead-time alerts), `ipm.TrademarkRenewed`, `ipm.AssetLapsed`, `ipm.StatusRefreshProposed`, `ipm.StatusRefreshConfirmed`, `ipm.ScreeningCompleted`, `ipm.DataSheetHandedOff`, `ipm.JournalIngested`, `ipm.WatchHitCreated`, `ipm.WatchHitDecided`, `ipm.OwnershipGapDetected`, `ipm.RecordalEvidenced`. Consumers `lit` (OPPOSED → matter; clocks), `mkp` (filing SKU), `ntf`, `int` (v1.2 `ip.IpAssetRegistered/StatusChanged`, opt-in), `bil` (usage counts).

**`lgo`, `gov`, `hr` (P13)**

| Event | Consumers |
|---|---|
| `lgo.RequestSubmitted` (W alias `lgo.IntakeRequestCreated`), `lgo.RequestTriaged`, `lgo.RequestConverted`, `lgo.RequestResolved`, `lgo.SlaAtRisk`, `lgo.SlaBreached`, `lgo.SelfServiceCompleted`, `lgo.LicenceRenewalDue`, `lgo.LicenceExpired`, `lgo.DoaChanged`, `lgo.DigestApproved`, `lgo.DutyGapDetected` | `ntf`, `rpt`, target modules on conversion |
| `gov.MeetingScheduled`, `gov.NoticeIssued`, `gov.PackPublished`, `gov.MeetingConcluded`, `gov.MinutesCirculated`, `gov.MinutesSealed`, `gov.ResolutionPassed`, `gov.CircularResolutionReferred`, `gov.RegisterEntryRecorded`, `gov.KmpChanged`, `gov.KmpVacancyOpened`, `gov.DeclarationSubmitted`, `gov.BlueprintGapOpened`, `gov.SorModeChanged` | `sgn` (formalities), `wf` (DoA), `ntf`, `rpt`; tenant-internal only (§6.23 rule 1) |
| `hr.EmployeeOnboarded`, `hr.EmployeeOffboarded`, `hr.PositionChanged`, `hr.LeaveApproved`, `hr.PayRunApproved`, `hr.PolicyAcknowledged`, `hr.PoshCaseCountChanged` (counts only) | `org`, `lgo` (duty holders), `ntf`; never to OH (NN-19) |

**`bsv` and `tax` (P14)**: `bsv.ServiceQuoted`, `bsv.ServiceOrderPlaced`, `bsv.InputsCompleted`, `bsv.PerformerAssigned`, `bsv.ProfessionalCertified`, `bsv.ApplicationFiled`, `bsv.GovernmentQueryRaised`, `bsv.DeliverablesDelivered`, `bsv.ServiceOrderClosed`, `bsv.ServiceOrderCancelled`, `bsv.RenewalDue`, `bsv.ServiceDefinitionPublished`; `tax.ComputationDrafted`, `tax.ReturnUploaded`, `tax.ReturnEVerified`, `tax.NoticeReceived`, `tax.DeadlineApproaching`, `tax.RulePackVerified`. Consumers `mkp` (engagement mirror), `bil` (credit notes), `ntf`, `rpt`, `int` (LDC order status write-back — proposal, §B.4.5).

**`chp` (P15; internal only, never mapped by `int`)**: `chp.CaseOpened`, `chp.CaseTriaged`, `chp.ConflictChecked` (P18's `chp.ConflictCheckCompleted` is an alias), `chp.CaseAccepted`, `chp.CaseAssigned` **(+X1; named by P18)**, `chp.LetterApproved`, `chp.LetterDispatched`, `chp.DeadlineApproaching`, `chp.CaseEscalated`, `chp.AwardRecorded`, `chp.CaseClosed`, `chp.AuthorityRevoked`, `chp.ChallanImported`, `chp.ChallanPaidOnOfficial`, `chp.VehicleSaleSigned`, `chp.RcTransferDue`, `chp.WallBreachBlocked`. Payloads carry IDs and codes only. Consumers `sdc` (queue), `ntf`, `rpt` (counts), `bil` (commercial records under the Consumer Help selling entity).

**`mkp` and `aca` (P16)**: `mkp.ServiceRequested`, `mkp.OfferIssued`, `mkp.OfferAccepted`, `mkp.EngagementContracted` (W alias `mkp.EngagementCreated`), `mkp.MilestoneDelivered` (W alias `mkp.DeliverableSubmitted`), `mkp.DeliverableAccepted`, `mkp.ChangeRequestApproved`, `mkp.ChangeRequestRejected` **(+X1)**, `mkp.EngagementClosed` (W alias `mkp.EngagementCompleted`), `mkp.EngagementCancelled`, `mkp.RetainerActivated`, `mkp.RetainerHourBankThresholdReached`, `mkp.RetainerSLABreached`, `mkp.ServiceCreditRequested`, `mkp.RetainerRenewed`, `mkp.RetainerEnded`, `mkp.DisputeRaised`, `mkp.DisputeResolved`, `mkp.ProfessionalActivated`, `mkp.ProfessionalSuspended`, `mkp.ProfessionRuleChanged`, `mkp.ServicePublished`, `mkp.ConflictCheckFailed`, `mkp.PayoutReleaseRequested`, `mkp.PayoutReconciled`, `mkp.ReviewPublished`; `aca.CatalogueSynced`, `aca.CertificateImported`. Consumers `sdc` (grants on retainer events), `bil` (OH8 quotes, credit notes), `int` (v1.2 `engagement.*`, `directory.MatterAllocated` counts), `ntf`, `web` (catalogue pages).

**`bil` and `sav` (P17)**: `bil.TrialStarted`, `bil.TrialEnded`, `bil.QuoteRequested`, `bil.CheckoutStarted`, `bil.SubscriptionActivated`, `bil.PlanChangeScheduled`, `bil.EntitlementApplied` (W alias `bil.EntitlementChanged`), `bil.LimitThresholdReached`, `bil.CreditsGranted`, `bil.CreditsConsumed`, `bil.CreditsReturned`, `bil.CreditsExpired`, `bil.CreditsLow`, `bil.UsageStatementClosed`, `bil.UsageDisputed`, `bil.InvoiceFiled` (W alias `bil.InvoiceAvailable`), `bil.CancellationRequested`, `bil.AutoRenewToggled`, `bil.BillingProfileChanged`, `bil.StreamSwitchChanged`, `bil.CommercialOverrideApplied`, `bil.PresentationPublished`; `sav.SnapshotComputed`, `sav.MethodologyPublished`, `sav.ValueReportGenerated`. Consumers every metered module (entitlement cache), `ntf`, `web` (pricing pages), `int` (→ `billing.UsageRecorded`, `platform.ModuleAttached/Detached`).

**`sdc` and `cvl` (P18)**: `sdc.DeliveryGrantProposed`, `sdc.DeliveryGrantActivated`, `sdc.DeliveryGrantRenewed`, `sdc.DeliveryGrantSuspended`, `sdc.DeliveryGrantRevoked`, `sdc.DeliveryGrantExpired` (W, all six under the alias `sdc.DeliveryGrantChanged` with `state`), `sdc.StandingAuthorisationChanged`, `sdc.DelegatedMakerCreated`, `sdc.DeliverySessionStarted`, `sdc.DeliverySessionEnded`, `sdc.BreakGlassOpened`, `sdc.DeliverableReleased`, `sdc.DeliverableAccepted`, `sdc.DeliverableReturned`, `sdc.MasterDataChangeRequested`, `sdc.MasterDataChangeClientDecided`, `sdc.MasterDataChangeApplied`, `sdc.MasterDataChangeRevertRequested`, `sdc.SlaThresholdReached`, `sdc.SlaBreached`, `sdc.TimeEntryLogged`, `sdc.DeliveryAnomalyDetected`; `cvl.VaultEnabled`, `cvl.VaultDisabled`, `cvl.CredentialEntryCreated`, `cvl.CredentialGrantChanged`, `cvl.CredentialRevealRequested`, `cvl.CredentialRevealed` (sealed payload; tenant-only), `cvl.CredentialRotated`, `cvl.CredentialRotationPrompted`, `cvl.VaultAnomalyDetected`. Consumers `iam` (sessions), `ntf` (client transparency), `rpt`, `int` (proposed OH aggregates, §B.4.5).

**`int` (P19)**: `int.ApiClientRegistered`, `int.ApiClientApproved`, `int.ApiClientRevoked`, `int.ApiKeyIssued`, `int.SecretRotated`, `int.WebhookSubscriptionCreated`, `int.WebhookEndpointPaused`, `int.WebhookDeliveryFailed`, `int.DlqReplayRequested`, `int.DlqReplayApproved`, `int.ConnectorInstanceStateChanged`, `int.EcosystemLinkStateChanged`, `int.SharingLedgerEntryRecorded`, `int.OnboardingBatchSubmitted`, `int.OnboardingInvitationSent`, `int.OnboardingInvitationAccepted` (W partner), `int.OnboardingInvitationDeclined` (W partner), `int.OnboardingInvitationExpired` (W partner), `int.SorSwitchStateChanged`, `int.DepositLinkCreated`, `int.DepositLinkRevoked`, `int.ReconciliationBreakDetected`, `int.RateLimitTierChanged`, `int.WebhookTest` (W). Alias retired: `int.KillSwitchToggled` → `cfg.KillSwitch*`.

**`xpt` (P20)**: `xpt.ExportRequested`, `xpt.ExportApproved`, `xpt.ExportCompleted` (W), `xpt.ExportFailed`, `xpt.StorageTargetConnected`, `xpt.StorageTargetDegraded`, `xpt.StorageTargetPaused`, `xpt.MirrorIncrementDelivered`, `xpt.TargetConflictDetected`, `xpt.ImportCommitted`, `xpt.ImportUndone`, `xpt.ExitRequested`, `xpt.DeletionCertified`, `xpt.RestoreTested`, `xpt.ExportMapVersionPublished`. Consumers `ntf`, `rpt`, `int` (→ `portability.*`, counts and status only).

**`web` and `hlp` (P21)**: `web.PageVersionPublished`, `web.PageUnpublished`, `web.DocxImportCompleted`, `web.RedirectMapPublished` (also emitted by P00 cut-over tooling), `web.LeadCaptured` (internal; OH CRM hand-off is an API call via `int`), `web.ContentReviewDue`, `web.LawChangeFlagged`, `web.TestimonialApproved`; `hlp.TermPublished`, `hlp.TutorialPublished`, `hlp.TutorialStale`, `hlp.ClipExported`, `hlp.HelpArticleFlaggedStale`, `hlp.AccessibilityFeedbackReceived`. No cross-product events.

**`mob` (P22)**: `mob.DeviceBound`, `mob.DeviceRevoked`, `mob.IntegrityFailed`, `mob.ScreenCaptureDetected`, `mob.OfflineCacheWiped`, `mob.DeepLinkClaimed`, `mob.StorePurchaseVerified` (→ `bil`), `mob.OtaReleasePublished`, `mob.OtaRolledBack`, `mob.AppVersionPolicyChanged`. No cross-product events.

**`eng` (P23)**: `eng.ChangeSubmitted`, `eng.ChangeImplemented`, `eng.DeploymentRefused`, `eng.ReleasePromoted`, `eng.VulnerabilitySlaBreached`, `eng.RestoreTestFailed`, `eng.IncidentDeclared`, `eng.IncidentClockWarning`, `eng.GoLiveSigned`. Consumers `ntf` (staff), `rpt`, `int` (→ `ops.ReleasePublished`, `ops.ControlEvidenceCollected`, `portability.BackupCompleted/RestoreTested`).

### B.4.3 Aliases and re-keying of Appendix I

Appendix I §I.7 states that the producing phase's §7.4 is canonical. The webhook and mapping names below are re-keyed to the canonical names (Appendix I to align in the same release):

| Appendix I name | Canonical | Appendix I name | Canonical |
|---|---|---|---|
| `bil.UsageAggregated` | `bil.UsageStatementClosed` | `core.ModuleEnabled` / `ModuleReadOnly` | `bil.EntitlementApplied` (module list diff) |
| `org.TenantCreated` | `core.TenantProvisioned` (self-service) / `iam.OnboardingInvitationActivated` (partner) | `iam.ConsentRecorded` / `ConsentWithdrawn` | `kyc.ConsentRecorded` / `kyc.ConsentWithdrawn` |
| `clm.ObligationCreated` / `ObligationStatusChanged` | `clm.ObligationVerified` / `clm.ObligationOverdue` (+ `wf.ItemResolved` on DONE) | `clm.AgreementAmended` | `clm.AmendmentInitiated` (executed child) |
| `sgn.SigningDeclined` / `SigningExpired` / `SigningWithdrawn` | `sgn.SignerDeclined` / `sgn.SigningRequestExpired` / `sgn.SigningRequestVoided` | `sgn.StampAttached` | `sgn.StampVerified` |
| `ipm.AssetRegistered` | `ipm.AssetCreated` | `mkp.EngagementCreated` / `EngagementStatusChanged` | `mkp.EngagementContracted` / any `mkp.Engagement*` |
| `mkp.AdvocateEngaged` | `mkp.EngagementContracted` where supplier type ADVOCATE and client is an organisation | `xpt.ExportJobStateChanged`, `StorageTargetVerified`, `BackupCopyConfirmed`, `RestoreTestCompleted` | `xpt.ExportRequested`/`ExportCompleted`, `xpt.StorageTargetConnected`, `xpt.MirrorIncrementDelivered`, `xpt.RestoreTested` |
| `eng.ReleaseDeployed`, `eng.ControlEvidenceStored` | `eng.ReleasePromoted`; control evidence is collected by `EvidenceCollector-*` jobs and mapped directly by `int` (no internal event) | `wf.TaskAssigned` | registered (+X1) |

### B.4.4 Cross-product events (published or consumed only by `int`)

| Ecosystem event | Direction | Internal source / sink | Status |
|---|---|---|---|
| `billing.UsageRecorded` | LD → OH8 | `bil.UsageStatementClosed` | v1.1 (LD added to scope row) |
| `platform.ModuleAttached` / `ModuleDetached` | LD → OH8 | `bil.EntitlementApplied` | v1.1 |
| `ops.TenantProvisioned`; `billing.PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled` | OH → LD | `core`, `bil` | v1.1 (LD as consumer) |
| `ops.SupportTicketOpened/Resolved`, `ops.ImplementationMilestoneReached`, `ops.ChangeApproved` | OH → LD | `sdc`, `eng` | v1.1 |
| `directory.ProfessionalEmpanelled` / `ProfessionalSuspended` | OH9 → LD | `kyc`, `mkp` | v1.1 (LD consumer, Y §Y.7.8) |
| `documents.DocumentShared` | LD → FX, LDC, EQ | `dms.ShareCreated` with consent | v1.1 |
| `privacy.ConsentRecorded` / `ConsentWithdrawn` / `DataPrincipalRequest`; `privacy.LegalHoldChanged` | LD ↔ recipients | `kyc`, `dms` | v1.1 |
| `platform.ReconciliationBreakRaised`; `ConnectorCertified` | LD ↔ counterpart | `int` | v1.1 |
| `portability.ExportRequested/ExportCompleted/StorageTargetConnected/BackupCompleted/RestoreTested` | LD → OH13 (counts, status) | `xpt`, `eng` | v1.1 |
| `ops.ReleasePublished`, `ops.ControlEvidenceCollected`, `AccessReviewCompleted` (PLATFORM), `SecurityIncidentNotified` copies | LD → OH13/OH14 | `eng`, `iam` | v1.1 [VERIFY domain segment and incident event name in Spec v1.1] |
| `legal.AgreementExecuted/Amended/Terminated`, `ContractObligationRegistered/StatusChanged`, `LegalMatterOpened/Updated/Closed`, `CourtCaseRegistered/Updated`, `CourtHearingScheduled`, `CourtOrderRecorded` | LD → LDC (and FX when linked) | `clm`, `lit` | v1.2 proposed (Y §Y.7.1); organisation-internal only |
| `esign.SigningRequestCreated/Completed/Declined/Expired/Withdrawn`, `esign.StampInstrumentVerified` | LD → requesting product | `sgn` (API-initiated only) | v1.2 proposed (Y §Y.7.2) |
| `ip.IpAssetRegistered/StatusChanged` | LD → LDC (opt-in) | `ipm` | v1.2 proposed |
| `engagement.EngagementCreated/StatusChanged`, `RetainerActivated/Ended` | LD → OH (commercial fields) | `mkp` | v1.2 proposed |
| `directory.MatterAllocated` (counts-only) | LD → OH9 | `mkp` | v1.2 proposed |
| `adr.ADRReferralCreated` (LD producer, non-loan) | LD → EQ | `lit.AdrReferralSubmitted` | v1.2 proposed (Y §Y.7.4) |
| `adr.ADRCaseStatusChanged/HearingScheduled/NeutralAppointed/OutcomeRecorded` (party view) | EQ → LD | `lit` | v1.2 proposed |
| `litigation.LitigationCaseOpened/Updated/Closed`, `HearingScheduled`, `OrderRecorded` (`.legal` projection) | RS → LD | `lit.projections_rs` | v1.2 proposed (Y §Y.7.5) |
| `governance.BoardMeetingScheduled`, `ResolutionPassed`, `KmpChanged` (to legal SoR) | LDC/FX → LD | `sgn` formalities, `wf` DoA | v1.2 proposed (Y §Y.7.6) |
| `ops.TenantRegistered`; `platform.SystemOfRecordSwitched`; `documents.DocumentDeposited`; `billing.MarketplacePayoutSettled` (OH → LD) | as named | `iam`, `int`, `dms`, `mkp` | v1.2 proposed (Y §Y.7.7) |

Everything marked "proposed" is inert in production until the Spec v1.2 contract is approved (`LD-INT-033`); interim channels are manual (`MANUAL_INTERIM`).

### B.4.5 Proposed cross-product events — resolved at integration review

All cross-product events proposed by phases are now registered in Appendix Y (after review F2, 25 Oct 2026); the names below are canonical and the earlier drafts are aliases the gateway accepts but never emits.

| Canonical event | Producer → consumer | Appendix Y | Former draft name |
|---|---|---|---|
| `in.infrabyx.ops.ServiceOrderRouted.v1` | LD → LDC | §Y.7.9 | `in.infrabyx.services.ServiceOrderRouted` (P16 draft) |
| `in.infrabyx.ops.ServiceOrderStatusChanged.v1` | LDC ↔ LD | §Y.7.9 | `in.infrabyx.compliance.ServiceOrderStatusChanged` (P14 draft) |
| `in.infrabyx.billing.MarketplaceTransferInstructed.v1` | LD → OH8 | §Y.7.7 (instruction on an on-hold Route transfer created from `route_transfers[]`: RELEASE / REVERSE / EXTEND_HOLD) | — |
| `in.infrabyx.ops.TenantSelfServeCreated.v1`, `ClientHealthSignal.v1`, `TimesheetAggregated.v1`, `DeliveryMetricsMonthly.v1`, `SurveyResponseRecorded.v1`, `ContentPublished.v1`, `GrievanceStatusChanged.v1`; `in.infrabyx.billing.ServiceCreditIssued.v1` | LD → OH | §Y.7.10 | Appendix X only (before review) |
| `UsageRecorded` (LawDocs as producer); `EmployeeOffboarded` (LawDocs as consumer) | LD → OH; OH → LD | §Y.7.7 | — |
| `in.infrabyx.legal.AgreementExecuted.v1`; ADR party-initiated referral | LD → subscribers | §Y.7.1, §Y.7.4 | "agreement executed summary" (P07 draft) |

---

## B.5 Error-code register

### B.5.1 Scheme

`LD-<MODULE>-<NNN>`; RFC 9457 problem details (`type` `https://api.lawdocs.in/problems/<code>`, `title`, `status`, `detail` without personal data, `instance`, `code`, `correlation_id`, `retryable`, `errors[]` JSON Pointers; FR-P00-48). Ecosystem-facing problems also carry the Spec problem code (`consent-missing`, `dataclass-not-permitted`, `regulatory-guard`, …; Appendix I §I.10). Every code has an actionable user message in all launch languages (D-07) and an "i" help key (`hlp.<module>.err_<nnn>` or the named key). A code is never reused for a different meaning; retired codes stay reserved. Codes are registered here **and** in the owning phase; CI fails on an unregistered code (`packages/errors` registry test).

### B.5.2 Module ranges

| Module | Range | Owner | Module | Range | Owner |
|---|---|---|---|---|---|
| `CORE` | 001–099 | P00 | `IAM` | 001–099 P01 · 101–199 P02 · 500–509 Appendix D (authorisation fail-closed) | P01, P02 |
| `AUTH` (namespace of `iam`, authentication edge) | 001–099 | P01 | `KYC` | 001–099 | P01 |
| `ORG` | 001–099 | P02 | `WF` | 001–099 P02 (approvals, DoA) · 100–149 P03 (items engine) (X-28) | P02, P03 |
| `CFG` | 001–099 | P03 | `RUL` | 001–049 | P03 |
| `DMS` | 001–040 | P04 | `DIX` | 001–040 | P05 |
| `TPL`, `DRF` | 001–040 each | P06 | `CLM` · `MSG` | 001–060 · 001–020 | P07 |
| `SGN` | 001–050 | P08 | `AI`, `AGT` | 001–099 each | P09 |
| `PLD` | 001–040 | P10 | `LIT` | 001–026 (to 099 reserved) | P11 |
| `IPM` | 001–016 (to 099 reserved) | P12 | `LGO`, `GOV`, `HR` | 001–010, 001–014, 001–010 | P13 |
| `BSV`, `TAX` | 001–012, 001–006 | P14 | `CHP` | 001–012 | P15 |
| `MKP`, `ACA` | 001–050, 001–003 | P16 | `BIL`, `SAV` | 001–050, 001–004 | P17 |
| `SDC`, `CVL` | 001–026, 001–011 | P18 | `INT` | 001–099 | P19 |
| `NTF` | 001–099 (041–045 used by Appendix J) | P19 channel adapters / Appendix J | `XPT` | 001–099 | P20 |
| `WEB` · `HLP` | `WEB` 001–040 P21 · 090–099 Appendix O (legal pages) · `HLP` 001–020 P21 | P21, Appendix O | `MOB` | 001–030 | P22 |
| `ENG` | 001–060 | P23 | | | |

### B.5.3 Codes (every code defined or used in the pack)

Format: `NNN` meaning (source). Codes not listed inside a range are reserved.

**CORE (P00 §7.6):** 001 ledger is append-only · 002 missing tenant context · 003 cross-tenant reference rejected · 010 correction requester cannot approve · 011 justification too short · 012 supporting document required · 013 target under legal hold · 014 live provider call from non-production · 015 unregistered setting key · 016 flag blocked by open verification (also P01 AVC test) · 017 kill switch engaged · 020 idempotency key reuse (422) · 030 business reference not found · 031 invalid business reference format · 040 migration reconciliation failed · 041 money delta not zero · 042 disposition evidence missing.

**IAM (P01 §7.6, P02 §7.6, Appendix D):** 001 invalid context (400) · 003 not a member (403) · 010 invitation expired · 011 invitation addressed to another contact · 020 SSO enforced for this domain · 101 role requires approval · 102 grant scope exceeds grantor's own scope · 103 role not valid for this workspace type · 104 grantee identity level below role minimum · 110 grant expired · 111 grant not approved by client · 120 custom role exceeds base-role ceiling · 121 custom role combines conflicting capabilities · 130 delegation not allowed for this role · 131 delegate lacks the role on this scope · 500 authorisation service unreachable — request refused (fail closed; Appendix D).

**AUTH (P01):** 001 code incorrect · 002 code expired · 003 too many attempts · 010 step-up required (401 with `required_acr`, `max_age`) · 020 request blocked by abuse protection.

**KYC (P01):** 001 verification method unavailable (flag off) · 002 signature on QR/e-Aadhaar invalid · 003 name match below threshold · 004 provider unavailable — try another method · 010 identifier format invalid · 011 individual PAN used for organisation onboarding · 012 organisation status blocks verification · 020 discovery quota reached · 030 age requirement not met · 031 guardianship evidence required · 040 signatory authority expired or exceeded · 041 signatory not verified to L2 · 050 professional credential not verified · 060 nominee release cancelled by owner · 070 consent required for this purpose · 071 notice re-acceptance required · 080 partner request lacks consentref or legal basis.

**ORG (P02):** 001 unit code already used · 002 restructure leaves open items without an owner · 010 master-data field requires the change workflow (A.56).

**WF (P02, P03):** 001 action requires approval · 010 maker cannot approve own request · 011 checker conflicts by SoD rule · 012 approval invalidated by change · 013 request expired · 014 tenant cannot relax a locked action · 015 solo-approval cooling-off in progress · 020 agents cannot check or approve · 030 no DoA row matches — routed to owner · 031 DoA step has no current holder · 100 item type not allowed for this parent · 101 item owner cannot be resolved · 102 waiting party type not allowed · 103 expected-by date required · 110 chaser deferred (quiet hours or business calendar) · 111 chaser stopped — stop condition met · 112 LawDocs never contacts courts, registries or regulators automatically · 113 counterparty reminder cap reached (NN-34) · 114 pre-approved series exceeds the maximum reminders (5) · 120 formality pending — cannot mark executed · 121 agents cannot waive an item · 122 evidence required to resolve · 123 a checker must resolve this item type · 130 task has open dependencies · 131 task evidence missing (P03 §13).

**CFG (P03 §13):** 001 value type or schema invalid · 002 child-direction rule violated (narrow/raise/lower-only) · 003 text contrast below 4.5:1 · 004 value outside platform/brand/plan bounds or below a floor (also P23 log-retention floor test) · 005 plan limit reached · 006 value locked at a parent tier · 010 setting is locked · 012 governed key — create a change request · 013 citation required for this key · 014 impact preview older than 24 hours · 015 effective date earlier than the key's lead time · 020 cannot approve own change · 021 checker not eligible (delegated from maker or same SoD group) · 022 change request expired · 030 numbering token duplicate · 031 numbering token invalid · 040 custom form fails the accessibility check · 050 kill switch cannot be released by the person who engaged it · 051 kill-switch drill overdue (warning) · 060 sandbox promotion conflicts with live changes · 070 imported row rejected (locked or out of bounds) · 071 configuration bundle signature invalid · 080 support session needs tenant approval · 081 emergency override expired — automatically reverted. (Validator order in P03 §5.1 now names each code; E-06 closed.)

**RUL (P03 §13):** 001 rule set not found or not active for this jurisdiction and date · 002 rule content (JDM/CEL) invalid · 003 golden suite failed — mismatches not accepted · 004 citations incomplete · 005 source hash does not match the cited source · 006 rule unverified — advisory only (NN-38) · 007 pinned version expired · 008 adaptation outside permitted parameters · 009 evaluation input incomplete · 010 emergency block in force · 011 reviewer must differ from maker · 012 reviewer of record lacks the required qualification · 013 cannot retire a rule set still adopted without a replacement · 014 challenge already open · 015 a code release cannot change published legal content (NN-30). 016–049 reserved.

**DMS (P04 §13; P00 references):** 001 file type not allowed · 002 malware detected · 003 storage quota reached · 004 encrypted/password-protected file · 005 unsafe archive · 006 Aadhaar number detected (info; masked copy stored) · 007 document checked out · 008 version conflict (saved as new version) · 009 legal hold — cannot delete · 010 retention floor — archive instead · 011 share expired · 012 share revoked · 013 OTP failed · 014 class guard on external share · 015 nominee waiting period · 016 DigiLocker consent/session expired · 017 retained DigiLocker copy not permitted · 018 duplicate — linked instead · 019 intake mapping conflict · 020 metadata validation · 021 recycle-bin item already purged · 022 maker-checker required · 023 offline not allowed for this class · 024 email-in sender not allowed (generic bounce) · 025 WhatsApp channel disabled · 026 relationship cycle · 027 check-out expired · 028 co-edit connector not connected · 029 download/print disabled by sharer · 030 item kind not shareable · 031 delegate scope exceeded · **032 checksum mismatch at ingest (new; replaces P00's conflicting use of 003)**.

**DIX (P05 §13):** 001 unsupported content (e.g., encrypted) · 002 insufficient credits · 003 no permitted engine for this data class — queued · 004 page image too low resolution · 010 WhatsApp date format ambiguous · 011 not a recognised WhatsApp export · 012 sender mapping incomplete · 015 low-confidence lines not reviewed · 016 verification not permitted for this role or agent · 017 type copy disputed — resolve before filing · 020 language undetermined · 021 locked term lost in translation · 022 back-translation flags unreviewed · 025 s.63 certificate not available for paper-document scans · 026 s.63 feature not yet enabled · 030 certified translation required by the forum · 031 no certified translator available — waitlisted · 035 engine regression gate failed.

**TPL (P06):** 001 template version not published · 002 a different reviewer must approve · 003 reviewer of record required before publishing · 004 open legal-update item blocks publishing · 005 variable schema invalid · 006 rule refers to an unknown answer · 007 golden test failed · 008 cited source could not be verified · 009 State-specific terms not verified (warning) · 010 language version not reviewed · 011 template retired · 012 neutrality checklist incomplete · 016 clause not allowed for this document type.

**DRF (P06; reused by P08, P09, P10 with the same meaning):** 001 answers still blank — clean copy blocked · 002 change makes the document an AI draft needing review · 003 AI draft must be reviewed before signing or clean download · 004 free downloads used · 005 only a reviewed language version can govern · 007 no AI credits left · 008 draft locked during review · 010 anonymous draft expired · 011 unverified legal citations must be fixed before review.

**CLM (P07 §13 "Error codes (initial set)"):** 001 request type not configured · 011 cannot invite participants to this room · 013 invitation limit reached for this person (NN-34) · 014 guest link expired · 021 sharing blocked — internal content found (NN-37) · 022 can compare only visible versions · 024 acknowledge untracked changes first · 031 cannot approve an agreement you prepared or under a delivery grant · 032 approval is for an older version · 041 agreement cannot go for signing — failed checks listed · 042 signed version cannot be unlocked — create an amendment · 051 verify key dates before reminders.

**MSG (P07 §13 "Error codes (initial set)"; range 001–020):** 001 not a member of this channel · 004 message can no longer be edited. 002–003, 005–020 reserved.

**SGN (P08 §13):** 001 document not frozen · 002 document changed after freezing — request voided · 003 stamp required before signing · 004 stamp UIN verification failed · 005 stamp certificate mismatch or already used · 006 eStamp not available for this State · 007 duty estimate not verified (info) · 008 signing provider unavailable · 009 provider blocked (licence/contract lapse) · 010 consent not given · 011 signing attempt failed at the provider · 012 name mismatch — held for review · 013 signer lacks authority under DoA · 014 instrument not eligible for electronic signature · 015 classification needed or suspect · 016 electronic witnessing not permitted · 017 notarisation required · 018 registration required — cannot mark executed · 019 formalities incomplete · 020 formality cannot be waived · 021 signing request expired · 022 declined by signer · 023 signing request cancelled · 024 bulk row invalid · 025 insufficient eSign credits · 026 stamp duty payment pending · 027 Aadhaar number present — mask before signing · 028 signature validation failed · 029 LTV refresh failed · 030 DSC agent not detected · 031 DSC certificate expired or revoked · 032 DSC class not accepted · 033 electronic acceptance not permitted · 034 signing on behalf of another application not permitted (NN-06) · 035 signer must be an adult (or guardian) · 036 changes requested — new round required · 037 exemption must be chosen from the cited list · 038 physical stamp paper cannot be combined with eSign · 039 assisted operator cannot act for a signer · 040 sandbox provider credentials in production blocked · 041 assistance consent and helper declaration required before assisted signing · 042 signer cannot perform the signing step personally — wet-ink route with signature by mark and witnesses (P08 FR-P08-57).

**AI (P09 §7.6):** 001 Vidhi unavailable — queued · 003 private data must be processed in India; India service unavailable · 004 sealed item — Vidhi cannot read it · 007 AI credits used · 011 date or number mismatch — held back · 012 citation could not be verified · 015 needs qualified review before final delivery (drafts use DRF-003) · 020 cannot create documents that look like official records · 025 external assistant not allowed.

**AGT (P09 §7.6; range 001–099):** 001 agent needs a human sponsor · 004 action above autonomy level — approval needed · 007 agents cannot approve, check, sign or pay (gateway code for any agent token on `*.approve`, `*.check`, `sgn.*` write and `bil.pay*` endpoints; P08, P09, Appendix H) · 009 agent paused by kill switch · 010 agent budget exhausted · 012 cross-product request has no approved contract · 015 automated calls blocked — number not declared or no consent (agent-facing wrapper of `LD-NTF-041`/`043`/`045`; Appendix J). All other codes in 001–099 reserved.

**PLD (P10):** 001 choose the forum · 010 facts without source · 012 amounts or dates do not match chronology · 014 legal reference could not be verified · 015 annexure index and text references inconsistent · 016 s.63(4) certificate missing for an electronic record · 018 certified translation required · 021 page reference unresolved · 025 layout does not match the court profile · 031 confirm dispatch details to send · 035 sworn affidavit does not match the approved text.

**LIT (P11):** 001 identifier format invalid · 002 duplicate case · 003 plan case limit reached · 004 court-data source unavailable — manual mode · 005 refresh credits exhausted · 006 forum not covered by a licensed source · 007 case managed in Recovery Suite (read-only) · 008 clock rule unverified — advisory · 009 open clock blocks closure · 010 open direction blocks closure · 011 contingency/success fee not permitted for advocates · 012 counsel not assigned to this matter · 013 invoice exceeds budget · 014 exposure values must be entered by a person · 015 exposure schedule frozen · 016 ADR pre-check failed · 017 ADR contract not live — use the interim signed pack · 018 import row errors · 019 undo window expired · 020 channel consent missing · 021 privileged document not shareable under this grant · 022 matter SoR is LawDocsComply · 023 agents cannot perform external actions · 024 party watch needs a licensed adapter · 025 prohibited claim wording · 026 bundle exceeds forum size limit.

**IPM (P12):** 001 application number format invalid · 002 duplicate asset · 003 plan asset limit · 004 watch limit · 005 source not enabled for screening · 006 status change needs evidence or reason · 007 confidence too low for bulk confirm · 008 rule unverified — advisory · 009 data sheet incomplete · 010 fee-category evidence missing · 011 only the engaged professional can record a filing · 012 journal parse failed · 013 agents cannot file or contact third parties · 014 recordal evidence required before owner change · 015 import row errors · 016 undo window expired.

**LGO (P13):** 001 category inactive · 002 required form fields missing · 003 self-service guardrail exceeded · 004 SLA pause reason not permitted · 005 conversion target unavailable · 006 routing rule conflict · 007 action exceeds your delegation · 008 licence register managed in LawDocsComply · 009 digest to directors needs CLO approval · 010 duty has no position holder.

**GOV (P13 §13 "Error codes"; range 001–014):** 001 blueprint rule unverified — advisory · 002 composition rule failed · 003 notice period shorter than required without the urgency path · 004 quorum not present · 005 matter cannot be passed by circulation (s.179(3)) · 006 interested director cannot vote · 007 minutes clock breached · 008 minutes sealed — no edits · 009 ratification pending · 010 register entries are event-based — use the source action · 011 declaration campaign closed · 012 filing task needs SRN · 013 system of record (LawDocsComply) unavailable — draft only · 014 mode change blocked while migration runs.

**HR (P13 §13 "Error codes"; range 001–010):** 001 labour pack version mismatch · 002 pay run needs a different checker · 003 wage payment date beyond statutory limit · 004 leave below statutory floor · 005 geo capture needs notice and consent · 006 prohibited monitoring field (NN-33) · 007 POSH area restricted · 008 appointment letter missing before joining · 009 position vacant for regulated role · 010 HR record managed in LawDocsComply.

**BSV (P14):** 001 service not available for entity type · 002 eligibility not met · 003 checklist incomplete · 004 fee version expired — re-quote · 005 variance above threshold — re-approval · 006 performer class mismatch · 007 credential or COP invalid · 008 independence conflict · 009 filing approval missing or stale · 010 government-fee mode not permitted (X-18) · 011 formalities incomplete · 012 claims or copied-text lint failure.

**TAX (P14 §12 "Errors introduced"; range 001–006):** 001 rule pack unverified · 002 ERI disabled · 003 taxpayer approval stale · 004 OTP or credential input blocked · 005 GSP consent missing · 006 notice deadline passed.

**CHP (P15):** 001 vertical disabled · 002 out of forum scope · 003 not yet eligible (date shown) · 004 representative not permitted for this forum · 005 authority letter missing or expired · 006 conflict policy blocks managed service · 007 banned phrase · 008 evidence hash mismatch · 009 rule row unverified (advisory) · 010 payment to third-party beneficiary not permitted · 011 consent missing for purpose · 012 wall policy denied.

**MKP (P16):** 001 service not found · 002 service not LIVE · 003 category invalid · 004 price card incomplete · 005 prohibited claim phrase · 006 exclusions missing · 010 reserved class supplied by LawDocs · 011 profession mode forbids model · 012 stream not allowed for service class · 015 counsel opinion reference required · 016 field not configurable · 017 maker cannot be checker · 020 conflict check failed · 021 independence check failed · 022 group conflict service unavailable · 025 offer expired · 026 DoA exceeded (sent to OH8 approval) · 030 inputs incomplete · 031 work outside approved scope · 033 SLA schedule not executed · 035 hour bank exhausted · 040 payout release blocked by dispute · 041 Route linked account not active · 045 review target invalid · 050 grievance clock breached (alert).

**ACA (P16 §12 "Error codes introduced"; range 001–003):** 001 feed signature invalid · 002 feed stale · 003 certificate import without consent.

**BIL (P17):** 001 signed artefact invalid · 002 catalogue version unknown · 005 OH8 unavailable (quote queued) · 010 disposable e-mail domain · 011 duplicate trial · 012 GSTIN invalid · 015 quote expired · 016 approval required · 020 credit type not applicable (credits cannot pay third parties) · 021 credits expired · 022 credit cap reached · 025 usage statement contains prohibited identifier · 026 dispute window closed · 030 missing price · 031 unevidenced claim · 032 popularity badge without basis · 033 unknown entitlement key · 034 orphan dependency · 035 missing incl.-GST total · 036 strike-through without price history · 037–039 reserved (publish lint) · 040 stream gate not ACTIVE · 041 prohibited stream · 042 checker equals maker · 050 never-block violation (internal alert).

**SAV (P17 §12 "Error codes"; range 001–004):** 001 methodology version missing · 002 benchmark out of date · 003 penalty rule unverified · 004 input evidence missing.

**SDC (P18):** 001 not assigned to this client · 002 grant expired · 003 action outside grant scope · 004 grant duration exceeds maximum · 005 name a client checker · 006 LawDocs makers cannot hold checker, approver, signatory, director or auditor roles · 007 delegated-maker work must be checked by the client · 008 only the client can approve access · 009 standing authorisation does not cover this scope · 010 session ended because the grant changed · 011 conflict found — reassignment · 012 break-glass needs two approvers · 015 different reviewer must approve deliverable · 016 field needs client approval · 017 raiser cannot apply the change · 018 evidence required · 020 Consumer Help staff cannot work for lender or insurer clients · 021 payment links only through LawDocs checkout · 025 storage location not approved for this data · 026 message blocked — contains a password, Aadhaar number or full PAN.

**CVL (P18 §12 "Error codes introduced"; range 001–011):** 001 vault switched off · 002 vault changes need a second administrator · 003 secret type cannot be stored · 004 link a task or purpose · 005 client-only regulator portal · 006 no access to this credential · 007 waiting for client approval · 008 reveals not allowed at this time · 009 vault paused pending security review · 010 reveals temporarily disabled (kill switch) · 011 URL not allowed for this portal type.

**INT (P19 §7.6; Appendix I §I.10):** 001 client not authorised for tenant (`tenant-unknown`) · 002 scope insufficient · 003 step-up required · 010 token expired or wrong audience · 011 signature verification failed · 012 client certificate mismatch · 020 Idempotency-Key missing · 021 key reused with a different body (422) · 022 request in progress (409) · 030 data class above ceiling · 031 consent or legal basis missing · 032 no active ecosystem link (`grant-expired`) · 033 contract not yet approved (Appendix Y pending) · 034 residency blocked · 035 ethical-wall block (Consumer Help) · 040 quota exhausted · 041 rate limited (429) · 050 webhook endpoint rejected · 051 deposited document hash or JWS mismatch · 052 deposit link inactive or folder missing · 060 eSign route requested by a non-LawDocs application · 061 instrument not eligible for eSign (hand-off) · 062 framing of signing page refused · 070 partner batch row invalid · 071 partner not permitted (regulated-professional revenue share) · 072 bulk onboarding of individuals refused · 080 connector suspended · 081 connector certification lapsed · 082 vendor dependency unavailable · 090 regulator/portal domain blocked by egress policy (NN-05) · 091 automation action not permitted (irreversible).

**NTF (Appendix J):** 041 no active A2P declaration · 042 outside calling window · 043 no channel consent · 044 counterparty not opted in · 045 DND or preference block (agent-facing wrapper `LD-AGT-015`).

**XPT (P20):** 012 a second person must approve · 015 export scope not permitted under a delivery grant (logged to the client's access log) · 031 residency blocked for this data class. Other codes 001–099 are reserved; P20 has not enumerated them (§B.7).

**WEB (P21 §7.3; Appendix O):** 001 page cannot be indexed without a reviewer of record · 002 claim not approved or expired · 003 similarity above threshold · 004 slug conflict · 005 redirect chain or loop · 006 structured data invalid · 007 accessibility check failed · 008 DOCX contains tracked changes or comments · 009 State variant fails materiality · 010 embed blocked until consent · 011 testimonial lacks consent or verified purchase · 012 testimonial about an advocate not allowed · 013 lead consent missing · 014 scheduled time in the past · 015 maker cannot review own content · 016 citation unresolved · 017 outdated law reference without mapping · 018 competitor brand or prohibited link · 019 template minimum content not met · 020 price must come from the catalogue · 021 urgency element not bound to a real event · 022 locale page lacks human review · 023 crawler policy change needs checker · 024 advertising slot not permitted on this page type · 090 review and accept updated Terms · 091 legal page has placeholders or review tags · 092 policy version needs reviewer and DPO approval · 093 translation not yet reviewed — showing English (090–099 Appendix O; OI-O-10 closed by this registration).

**HLP (P21 §7.3 "Errors"; range 001–020):** 001 UI term has no registered "i" key · 002 plain definition missing for an enabled locale · 003 video lacks captions · 004 video lacks transcript · 005 tour target not found · 006 tutorial capture used a non-synthetic tenant · 007 help key not registered for screen · 008 accessibility feedback rate limit (offers phone/email). 009–020 reserved.

**MOB (P22):** 001 update required · 002 device limit reached · 003 integrity check failed (restricted mode) · 004 attestation unavailable (degraded) · 005 step-up required · 006 biometric enrolment changed · 007 certificate validation failed · 008 offline copy not permitted · 009 saving to device not permitted · 010 upload incomplete — resume available · 011 file type not accepted · 012 WhatsApp export could not be parsed · 013 link not available · 014 link expired · 015 payment confirmation pending · 016 purchase not available in the app · 017 store receipt could not be verified · 018 feature needs a computer · 019 Vidhi needs a connection · 020 voice language not supported · 021 OTA update signature invalid · 022 account deletion blocked by legal hold · 023 screen capture blocked on this screen.

**ENG (P23):** 010 change not approved (deploy gate) · 011 approver authored changes in this release. Other codes 001–060 reserved; P23 has not enumerated them (§B.7).

### B.5.4 Collisions and inconsistencies found

| # | Finding | Resolution | Files |
|---|---|---|---|
| E-01 | **Collision:** P00 used `LD-DMS-003` for "checksum mismatch" and `LD-DMS-004` for "type not allowed"; P04 (owner) defines 003 "storage quota" and 004 "encrypted file" | P00 now uses `LD-DMS-032` (new: checksum mismatch) and `LD-DMS-001` (type not allowed); P04 table extended with 032 | **Fixed:** P00 FR-P00-54 and §7.6; P04 §13 |
| E-02 | `LD-AUTH-*` is not a module code (conventions §5 requires `LD-<MODULE>`) | Registered as an authentication namespace of `iam`, owned by P01 | — |
| E-03 | Appendix O uses `LD-WEB-090…093` outside P21's declared 001–040 | Range 090–099 allocated to Appendix O legal-page rendering | — |
| E-04 | Appendix D uses `LD-IAM-500` outside P01/P02 ranges | Range 500–509 allocated to authorisation fail-closed | — |
| E-05 | Appendix J uses `LD-NTF-041…045`; no phase declares an `NTF` range | `NTF` 001–099 registered; owner P19 channel adapters with Appendix J | — |
| E-06 | P03 validator-order text (001–006) disagrees with P03 test codes (003 contrast, 004 bounds, 005 plan limit) | **Closed (F1):** P03 §5.1 now names each code (001 type/schema, 004 bounds, 005 plan limit, 002 child direction, 006 parent lock, 003 contrast) consistent with its tests | P03 §5.1, §13 (edited) |
| E-07 | Overlapping meanings: `LD-AGT-007`, `LD-WF-020`, `LD-LIT-023`, `LD-IPM-013`, `LD-DIX-016`, `LD-WF-121` all express "agents cannot …" | Not a collision: the gateway returns `LD-AGT-007` for agent tokens on approve/check/sign/pay endpoints; module codes are returned by in-module guards with module-specific help | — |
| E-08 | `LD-DRF-003` returned by P08, P09 and P10 | Same meaning; owner P06; reuse permitted | — |
| E-09 | Ranges declared but not enumerated: `XPT` (only 012, 015, 031), `ENG` (010, 011), `RUL` (011), `CFG` partial | `CFG`, `RUL` and `WF` 100–149 enumerated by P03 §13 (F1); `XPT` and `ENG` remain for P20 §13 and P23 §13; CI registry test fails on any unregistered use | P20 §13, P23 §13 |
| E-10 | Help-key form for error codes: P03, P04, P16, P17 and §B.5.1 use `hlp.<module>.err_<nnn>`; P11 (`hlp.lit.err.<nnn>`), P12 (`hlp.ipm.err.<nnn>`) and P13 (`hlp.<module>.err.<nnn>`) use a dot | §B.5.1 form `hlp.<module>.err_<nnn>` is canonical (registry convention); the `packages/errors` registry accepts the dotted form as an alias until P11/P12/P13 align (registry review G4) | P11 §13, P12 §13, P13 §13 (hand-back; not edited by the registry maintainer) |
| E-11 | Registry review (G4, 25 Oct 2026): every `LD-<MODULE>-<NNN>` code referenced in phases, appendices, master, `02`, condensed editions and the content deck was checked by script against this section | 570 codes enumerated across 39 module namespaces (incl. `AUTH`); every referenced code is enumerated; the only unmatched strings are range endpoints (`LD-ENG-001`/`060`, `LD-XPT-001`/`099`, `LD-INT-099`, `LD-MOB-030`, `LD-RUL-049`, `LD-WEB-040`/`099`, `LD-HLP-020`), which are not codes. `AGT`, `CVL`, `GOV`, `HR`, `HLP`, `MSG`, `SAV`, `TAX`, `ACA` are enumerated in full from their owning phases (P09 §7.6, P18, P13 §13, P21 §7.3, P07 §13, P17, P14, P16); codes used in Appendix A/D (e.g., `LD-GOV-003…014`, `LD-HR-001/002/003/007`, `LD-TAX-001…004`) all have phase definitions, so no code needed to be defined at registry review | — |

---

## B.6 Data classes and retention classes

### B.6.1 Data classes (three vocabularies, one mapping)

LawDocs uses three related vocabularies; each field carries `x-dataclass` (Spec class) and each document a confidentiality class; AI routing computes its own class from inputs. The mapping below is binding.

| Ecosystem Spec class (§13.2; `x-dataclass`) | LawDocs confidentiality class (P04 FR-P04-64) | AI routing class (P09 FR-P09-02) | Keyring (P00 FR-P00-32) | Handling in LawDocs |
|---|---|---|---|---|
| `PUBLIC` | `PUBLIC` | `PUBLIC` | — | May use Anthropic API (global) for public content only |
| `INTERNAL` | `INTERNAL` | `INTERNAL` | — | Authenticated; India-only AI route; OH ceiling for product sources |
| `CONFIDENTIAL` | `CONFIDENTIAL` | `CONFIDENTIAL` | — | Need-to-know; encrypted at rest; India-only AI |
| `PII` | (any class with personal data) | `PERSONAL` | `pii` | Consent or legal basis; role masking; never logged (NN-32) |
| `SPI` | `RESTRICTED_PERSONAL` (health, matrimonial, custody, DV, criminal) | `SENSITIVE` | `spi`, `kyc_artefact` | Field encryption; sealed roles; AI only on the sensitive allow-list (`LD-AI-004`); Aadhaar never stored in clear (NN-04, X-14) |
| `FINANCIAL` | `CONFIDENTIAL` | `CONFIDENTIAL` | `financial` | Stamp duty, money, bank data masked + token |
| `LEGAL` (+ `x-privileged`) | `CONFIDENTIAL_LEGAL` (privileged), `BOARD_CONFIDENTIAL` | `CONFIDENTIAL` (`SENSITIVE` when sealed) | `legal`, `legal_privileged` | Legal-hold aware; privileged fields leave LD only with `ORG_CLO`/individual per-record approval (Y §Y.6.3) |
| `HR` | `CONFIDENTIAL` (HR documents), restricted export folder `[R]` | `CONFIDENTIAL`; POSH `SENSITIVE` | `hr` | Employer system only; never to OH; never for AI training |
| `WELLNESS` | — | — | — | Rejected by LawDocs gateways (Udofin only); a deposit carrying it ends `REJECTED` (P19 §5.7; `LD-INT-030` at the gateway) |
| `CONSUMER_HELP` (new, Y §Y.6.3) | Consumer Help cell classes | `CONFIDENTIAL`/`SENSITIVE` | per field | Never in any cross-product schema; counts only to OH (NN-23) |
| Credentials (LawDocs-internal) | sealed | never sent to AI | `credential` | `cvl` envelope encryption with client-scoped keys (NN-16) |

The envelope `dataclass` is the highest field class; gateways reject messages above the consumer's ceiling (`LD-INT-030`). Search indices carry `confidentiality_class` and ACL principals for engine-side filtering (P04).

### B.6.2 Retention classes (registry `dms.retention_classes` content rows; settings `dms.retention.*`, Appendix R §R.9)

Tenants may lengthen, never shorten below a floor (FR-P04-49). Legal hold suspends every disposal (A.20). Floors marked [VERIFY] ship advisory until verified (NN-38).

| Code | Floor / period | Trigger | Basis | Aliases in phases |
|---|---|---|---|---|
| `LEDGER` | Permanent; append-only; Object Lock export | — | NN-02 | R-LEDGER (P18) |
| `PERMANENT` | Permanent | — | Content and registry versions (NN-30); immutable page versions | "Permanent" |
| `MINUTES_AND_REGISTERS` | Permanent | — | Companies Act 2013 ss.118, 88 [VERIFY rule numbers] | — |
| `TENANT_LIFE_8Y` | Life of tenant/account + 8 years | Tenant or account closure | [REC] aligned to s.128(5) horizon | "Life + 8 y" |
| `ACCOUNT_LIFE_1Y` | Life of account + 1 year | Account closure | [REC] | "Life + 1 y" |
| `OPS_8Y` | 8 years after relationship end or record closure | Closure | [REC] | R-OPS-8Y (P18), "8 y" |
| `OPS_10Y` | 10 years after close | Order closure | [VERIFY] (P14 `bsv.orders`) | — |
| `BOOKS_8FY` | 8 years from end of the relevant FY | FY end | Companies Act 2013 s.128(5) | `COMPANY_BOOKS_AND_VOUCHERS` (P04), "8 FY" |
| `TAX_8Y` | Longest of: GST 72 months from the annual-return due date (CGST Act s.36); income-tax period under the Income-tax Act 2025 [VERIFY]; 8 FY | Return/FY | CGST s.36; IT Act 2025 [VERIFY] | `GST_RECORDS`, `INCOME_TAX_RECORDS` (P04) |
| `CONTRACT_STD` | Default term + limitation + buffer, ≥ 8 years after end; floor 7 years after expiry | Agreement end | Limitation Act 1963 (R3 LG-092); Appendix R `dms.retention.contract_min_years` | — |
| `EXECUTED_INSTRUMENT_EVIDENCE` | ≥ 7 years after the later of signing and account closure (compliance-mode lock) | Signing / closure | eSign API log archival (R3 LG-008); LG-092; `sgn.evidence.retention_years_after_closure` | SGN_EVIDENCE |
| `LIT_RECORD` | Default closure + 12 years; floor closure + limitation for appeal/execution + 3 years | Matter closure | Spec §13.3 (12-year execution period); Limitation Act [REC] | `LITIGATION_FILE` (P04) |
| `IP_ASSET` | Life of asset + 8 years after lapse | Lapse | [REC] | — |
| `EMPLOYEE_RECORDS` | Per Labour Codes and rules | Separation | [VERIFY] (P13; LDC is SoR when present) | — |
| `PERSONAL_USER_CONTENT` | Until the user deletes or closes the account (+ grace `dms.closure.grace_days`, 90) | User action | DPDP Act 2023 s.8(7) [INTERP] | `dms.retention.individual_default` |
| `PER_PURPOSE` | Until the consented purpose ends or consent is revoked | Revocation | DPDP; DigiLocker requester terms [VERIFY with NeGD] (NN-42) | — |
| `CHP_CASE` · `CHP_THIRD_PARTY` · `CHP_HEALTH` · `CHP_FEES` · `CHP_CONFLICT_LOG` | Closure + 8 y [VERIFY] · closure + 36 months · closure + 36 months or deletion request · 8 y · 3 y | Case closure | Appendix S §S.17.3 | — |
| `AI_RUN_7Y` · `AI_CONTENT` · `AI_GUARDRAIL_1Y` | Run metadata 7 years · content per `ai.retention.content_days` · guardrail events ≥ 1 year | Run | P09; DPDP Rules r.6(e) (guardrail logs) [VERIFY] | — |
| `SEC_LOG_1Y` | 180 days hot in India; 1 year total; personal-data logs 365 days (`eng.logs.retention_days_india` default 400) | Event | CERT-In Directions 2022 (NN-27) | R-SEC-1Y |
| `PLATFORM_ENG_8Y` | 8 years | Record closure | [REC] | — |
| `PUBLIC_PUBLICATION` | Permanent | — | Public Trade Marks Journal (stored once, no tenant data) | — |
| `MARKETING_AND_TRANSIENT` | 2 years | Creation | [REC] | — |
| `ROLLING_nY` / `ROLLING_nD` | Fixed rolling periods stated in the table (e.g., 1, 2, 3, 5, 7 years; 180, 400 days) | Creation | Operational | "1 year", "3 years" |
| `LEAD_30D` | 30 days after OH acknowledgement | Hand-off | NN-19 | — |
| `ANON_DRAFT_7D` | 7 days | Creation | `drf.draft.retention_days_anonymous` | — |
| `TRANSIENT_24H` · `OUTBOX_90D` · `INBOX_365D` · `DLQ_90D` | 24 h (≤ 7 d for `int`) · ≥ 90 days · 365 days · 30/90 days | Creation | P00, P19 | — |
| `FOLLOWS_PARENT` | As the parent record | Parent | — | "as parent", "with order" |

---

## B.7 Files that need alignment (hand-back list) and open items

**Edited by X1 in this pass:** P00 (FR-P00-54, §7.6 DMS codes), P03 (§7.4 `CorrectionApplied`), P04 (§13 DMS 032; reserved range), P05 (§7.2 `dxj_`), P07 (§7.2 `rlc_`), P09 (§7.2 `aic_`/`aim_`), P13 (§7.2 `lgo.waiting_items` view), P16 (FR-P16-42 and §7.2 `ecr_`), P18 (§7.2 `mdc_`, `dmt_`; §7.3 `{mdc}` paths).

**To align at the next integration (not edited):**

| File | Item |
|---|---|
| P00 §7.2/§7.4 | **Done (F1)** — heads renamed; `cfg.*` events only |
| P01 §5.7/§5.9, §7.2 | **Done (F1)** — canonical nominee and invitation states; OVSE keys `kyc.ovse.qr.enabled` / `kyc.ovse.avc.enabled` (Appendix R aligned) |
| P02 §5.1 | **Done (F1)** — A.9 pointer, DECLINED/WITHDRAWN, standing authorisation |
| P03 §5.1, §7.2, §13 | **Done (F1)** — CFG codes named; `wf.tasks` added; `LD-RUL-001…015` and `LD-WF-100…131` enumerated |
| P05 §7.2/§7.3 | Optionally rename `run_id` → `job_id` |
| P07 §5.4, §7.2 | **Done (F1)** |
| P09 §7.2/§7.4 | **Done (F1)** |
| P11 §7.4 | **Done (F1)** |
| P12 §7.4 | Add `ipm.DataSheetReady` |
| P14 §7.4 | Cross-product proposal name (`compliance.` vs `ops.ServiceOrderStatusChanged`) |
| P15 §7.4 | Add `chp.CaseAssigned` |
| P16 §7.4 | Done at review: `mkp.ChangeRequestRejected` added; `ops.ServiceOrderRouted` and `billing.MarketplaceTransferInstructed` registered in Appendix Y |
| P18 §5.5, §7.4 | Queue mapping (R-A-19); `chp.ConflictCheckCompleted` → `chp.ConflictChecked`; refer to `msg.channels` |
| P19 §5.8, §7.4 | ADR referral is P11's machine (R-A-15); retire `int.KillSwitchToggled` (internal `dms.DocumentDeposited` now in P04 §7.4 — F1) |
| P20 §13 | Enumerate `LD-XPT-*` |
| P23 §13 | Enumerate `LD-ENG-*` |
| Appendix I §I.7, §I.8 | Re-key internal names per §B.4.3 |
| Appendix K §K.11 | **Done (F1)** — † record types plus `task`, `signing_assistance`, `tax_notice`, `tenant_template`, `clause`, `playbook`, `intake_form` |
| Appendix Y | Register the P18/Appendix X `ops` events and one name for service-order status (§B.4.5) |

**Open items (registered in Appendix W §W.4 at registry review G4: OI-B-01 with OI-P04-08 in §W.4.5, OI-B-02 and OI-B-04 in §W.4.1, OI-B-03 in §W.4.6):** OI-B-01 counsel/DPO confirmation of retention floors marked [VERIFY] (`TAX_8Y`, `EMPLOYEE_RECORDS`, `CHP_CASE`, `OPS_10Y`, minutes rule numbers); OI-B-02 Spec domain segment for `ReleasePublished`/`ControlEvidenceCollected` and the incident-notification event name; OI-B-03 owner confirmation of `NTF` range ownership; OI-B-04 Appendix Y registration of OH-addendum events.


