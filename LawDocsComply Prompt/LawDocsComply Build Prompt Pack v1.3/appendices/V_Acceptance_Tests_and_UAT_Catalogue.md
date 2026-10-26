# Appendix V — Acceptance Tests and UAT Catalogue

> Binding for every phase. Compiled by the pack lead on 25 October 2026 from each phase file §12 and each stream's test register (`_contrib/S*_tests.md`). The phase file's Gherkin scenarios are the detailed acceptance criteria; this appendix is the index the QA lead uses to build `tests/acceptance/pXX/*.feature`, the NN suite and the UAT plan.

## V.1 How tests are organised

- **NN suite** (`tests/nn/NN-xx_*.spec.ts`): at least one automated test per non-negotiable rule; a failing NN test blocks release (master §4).
- **Acceptance** (`tests/acceptance/pXX/*.feature`): Gherkin scenarios from each phase §12; tagged `@pXX`, `@nn-xx`, `@role-<code>`, `@family-<code>`.
- **Golden fixtures** (`tests/golden/`): returns kernel and risk kernel fixtures shared with Finbyx; golden exports (LDC-EXPORT-1.0); golden template imports (one file per family from `templates/`); payroll fixtures shared with OH10.
- **Contract tests**: every API (OpenAPI 3.1), event (AsyncAPI 3.0) and ecosystem contract (Ecosystem Spec v1.1).
- **Accessibility**: axe in CI on every route; manual screen-reader passes (NVDA + Chrome, JAWS + Edge, VoiceOver + Safari, TalkBack + Chrome) per release for the top 30 journeys (P23).
- **UAT**: per wave, with a pilot tenant per family (Middle-Layer NBFC, private company, IFSCA FC/FU, credit co-operative society, listed company), scripted from the role journeys in Appendix C and the scenarios below; sign-off by the owner and the pilot's CCO.

## V.2 NN test index

| NN | Rule (short) | Test prefix | Primary phases |
|---|---|---|---|
| NN-01 | Tenant isolation | `tests/nn/NN-01_*.spec.ts` | P00,P01 |
| NN-02 | Immutable, hash-chained audit ledger | `tests/nn/NN-02_*.spec.ts` | P00,P02 |
| NN-03 | Base content and tenant overlay are separate | `tests/nn/NN-03_*.spec.ts` | P03 |
| NN-04 | No auto-publish of AI output | `tests/nn/NN-04_*.spec.ts` | P05,P17 |
| NN-05 | Maker ≠ checker | `tests/nn/NN-05_*.spec.ts` | P04,P02 |
| NN-06 | Citations | `tests/nn/NN-06_*.spec.ts` | P03,P17 |
| NN-07 | Bitemporal effective dating | `tests/nn/NN-07_*.spec.ts` | P00,P02 |
| NN-08 | No regulator-connectivity claim and no automated filing | `tests/nn/NN-08_*.spec.ts` | P11,P12,P14 |
| NN-09 | Evidence integrity | `tests/nn/NN-09_*.spec.ts` | P07,P19 |
| NN-10 | Everything is exportable | `tests/nn/NN-10_*.spec.ts` | P19 |
| NN-11 | No manual customer migration | `tests/nn/NN-11_*.spec.ts` | P00,P24 |
| NN-12 | Identity minimisation | `tests/nn/NN-12_*.spec.ts` | P01 |
| NN-13 | Sealed data classes | `tests/nn/NN-13_*.spec.ts` | P12,P13,P14 |
| NN-14 | AI drafts; humans act | `tests/nn/NN-14_*.spec.ts` | P17 |
| NN-15 | No training on tenant content | `tests/nn/NN-15_*.spec.ts` | P17 |
| NN-16 | Payment safety | `tests/nn/NN-16_*.spec.ts` | P20 |
| NN-17 | Credential vault | `tests/nn/NN-17_*.spec.ts` | P22 |
| NN-18 | Regulator view | `tests/nn/NN-18_*.spec.ts` | P01 |
| NN-19 | Claims register | `tests/nn/NN-19_*.spec.ts` | P20,P23 |
| NN-20 | Professional-conduct switches | `tests/nn/NN-20_*.spec.ts` | P21 |
| NN-21 | Accessibility | `tests/nn/NN-21_*.spec.ts` | P23,P24 |
| NN-22 | Deterministic, reproducible calculations | `tests/nn/NN-22_*.spec.ts` | P09,P11,P13 |
| NN-23 | Ecosystem contracts only | `tests/nn/NN-23_*.spec.ts` | P18 |
| NN-24 | India residency | `tests/nn/NN-24_*.spec.ts` | P00,P24 |
| NN-25 | Transparent workforce monitoring | `tests/nn/NN-25_*.spec.ts` | P13 |
| NN-26 | Rule packs for statutory parameters | `tests/nn/NN-26_*.spec.ts` | P13 |
| NN-27 | Updates ≠ Notifications | `tests/nn/NN-27_*.spec.ts` | P04,P05 |
| NN-28 | Configurability tiers | `tests/nn/NN-28_*.spec.ts` | P02 |
| NN-29 | Removal never deletes history | `tests/nn/NN-29_*.spec.ts` | P03 |
| NN-30 | Platform access to tenant data | `tests/nn/NN-30_*.spec.ts` | P01 |
| NN-31 | Grievance clocks owned and signposted | `tests/nn/NN-31_*.spec.ts` | P14 |
| NN-32 | No PII or secrets in logs | `tests/nn/NN-32_*.spec.ts` | P00 |
| NN-33 | Statutory clocks are computed, start at the earliest legally relevant time and never pause | `tests/nn/NN-33_*.spec.ts` | P04,P12,P14 |
| NN-34 | Reviewed release only; code never changes content | `tests/nn/NN-34_*.spec.ts` | P03,P05,P24 |
| NN-35 | Template contract | `tests/nn/NN-35_*.spec.ts` | P03 |
| NN-36 | Sealed governance records | `tests/nn/NN-36_*.spec.ts` | P06 |
| NN-37 | Deterministic documents and numbers | `tests/nn/NN-37_*.spec.ts` | P07,P11,P17 |
| NN-38 | Regulatory floors and supervisory status | `tests/nn/NN-38_*.spec.ts` | P08,P09,P15 |
| NN-39 | One owner per computed regulatory output | `tests/nn/NN-39_*.spec.ts` | P09,P10,P11 |
| NN-40 | Internal Ombudsman independence | `tests/nn/NN-40_*.spec.ts` | P14 |
| NN-41 | AI routing by data class; no standing AI permissions | `tests/nn/NN-41_*.spec.ts` | P17 |
| NN-42 | Never-block list | `tests/nn/NN-42_*.spec.ts` | P20 |
| NN-43 | Delivery staff never check | `tests/nn/NN-43_*.spec.ts` | P22 |
| NN-44 | Honest public surface | `tests/nn/NN-44_*.spec.ts` | P23 |
| NN-45 | Audit in the same transaction; export taxonomy is a contract | `tests/nn/NN-45_*.spec.ts` | P00,P19,P24 |
| NN-46 | No bulk approval of controls with legal effect, money or access | `tests/nn/NN-46_*.spec.ts` | P04 |
| NN-47 | AI never decides a conclusion | `tests/nn/NN-47_*.spec.ts` | P04, P08, P10, P12, P14, P17, P26 |
| NN-48 | Three dates; timeliness on act date | `tests/nn/NN-48_*.spec.ts` | P04, P06, P11, P13, P26, P27 |
| NN-49 | Undo for imports and bulk changes | `tests/nn/NN-49_*.spec.ts` | P02, P03, P04, P19 |
| NN-50 | Bounded autonomy | `tests/nn/NN-50_*.spec.ts` | P02, P17 |
| NN-51 | AI kill switches ≤ 60 s | `tests/nn/NN-51_*.spec.ts` | P17, P24 |
| NN-52 | Protocol edge, contract core (MCP/A2A) | `tests/nn/NN-52_*.spec.ts` | P17, P18 |
| NN-53 | Jurisdiction-pack gate | `tests/nn/NN-53_*.spec.ts` | P03, P15, P25 |
| NN-54 | Official language preserved | `tests/nn/NN-54_*.spec.ts` | P03, P25 |
| NN-55 | No stale citations | `tests/nn/NN-55_*.spec.ts` | P03, P05 |

## V.3 UAT journeys (minimum per wave)

| # | Journey | Roles | Wave |
|---|---|---|---|
| U-01 | Free health check → report → trial → PAN pre-fill → module selection → checkout → first compliance instance | `anon`, `lead`, `ten_admin` | 1 |
| U-02 | Import a family question sheet (Excel) → preview → errors fixed → publish → tenant adopts instrument from catalogue | `plt_content_maker`, `plt_content_checker`, `ten_admin` | 1 |
| U-03 | Maker submits evidence → checker returns → maker resubmits → checker approves → auditor comments → board report | `ten_maker`, `ten_checker`, `ten_internal_auditor`, `ten_board_member` | 1 |
| U-04 | 20:00 IST scan detects an amendment → AI summary and diff → content release → tenant Update with previous vs new actionable → impact tasks | `plt_content_*`, `ten_cco` | 1 |
| U-05 | Board meeting: agenda from due items → board pack → meeting → Vidhi minutes draft → SS-1 checks → signature → register entries | `ten_kmp` (CS), `ten_board_member` | 1 |
| U-06 | Policy review: Vidhi drafts tracked changes against previous version → review → board approval → signed PDF uploaded → attestations | `ten_dept_head`, `ten_cco`, `ten_employee` | 1 |
| U-07 | Full tenant export to BYO OneDrive; open every folder without LDC | `ten_admin` | 1 |
| U-08 | Super admin Correction Entry on a tenant date; tenant sees original and correction | `plt_super_admin`, `ten_admin` | 1 |
| U-09 | Risk register → RCSA → KRI breach from Finbyx feed → issue → RMC pack | `ten_kmp` (CRO) | 2 |
| U-10 | Stress test (adverse scenario) → ICAAP section draft → board approval → export | `ten_kmp` (CRO, CFO) | 2 |
| U-11 | Return Studio: Tally trial balance + LMS dump → mapping → validation → reconciliation → upload-ready file → acknowledgement captured | `ten_maker`, `ten_checker` | 2 |
| U-12 | CIC submission file for a non-Finbyx lender → validation → bureau rejection file re-import | `ten_maker` | 2 |
| U-13 | RBIA plan → engagement → workpapers → findings → management response → audit committee report | `ten_internal_auditor`, `ten_dept_head` | 2 |
| U-14 | Personal-data breach: CERT-In 6-hour and DPB clocks → reports prepared → submitted by a human → evidence | `ten_kmp` (CISO, DPO) | 2 |
| U-15 | Complaint from client website → support desk → GRO → IO → final reply → external route signposted | `ten_support_agent`, `ten_kmp` (GRO, IO) | 2 |
| U-16 | Employee onboarding → employment agreement eSign → payroll run → registers → POSH IC set-up | `ten_hr_admin`, `ten_payroll_maker`, `ten_payroll_checker` | 3 |
| U-17 | Credit co-operative society: member admission → AGM notice → election support records → audit rectification → Registrar return | `coop_office_bearer` | 3 |
| U-18 | Marketplace: non-subscriber buys an ICAAP drafting service → SLA eSigned → delivery → invoice from OH8 | `mkp_buyer`, `mkp_professional` | 3 |
| U-19 | Retainer: RM as maker (delivery grant) → client checker approves → credential reveal logged | `dlv_rm`, `ten_checker`, `ten_admin` | 3 |
| U-20 | Supervisor view: tenant grants 30-day read-only access → supervisor reviews → grant expires automatically | `ten_admin`, `ten_supervisor_view` | 2 |


## V.5 UAT journeys added in v1.1

| # | Journey | Roles | Wave |
|---|---|---|---|
| U-21 | Client admin ticks consolidated RBI directions in the pre-seeded catalogue; placeholders appear; uploaded sheet replaces placeholders with a diff | `ten_admin`, `plt_content_*` | 1 |
| U-22 | Import an existing Excel compliance tracker with AI mapping → approve plan → undo within 24 h | `ten_admin` | 1 |
| U-23 | One control satisfies obligations in three instruments; one evidence upload closes all three instances | `ten_maker`, `ten_checker` | 1 |
| U-24 | Client's own Claude/Copilot queries due items through the LDC MCP server; sealed data never returned | `ten_cco` | 2 |
| U-25 | Agent mission at L2: Returns Preparer drafts a return package; human approves; kill switch tested | `ten_kmp` (CFO), `ten_admin` | 2 |
| U-26 | Legal notice received → matter opened → hearing calendar → provision feed to accounts | `ten_legal_user`, GC | 2 |
| U-27 | Regulator inspection observations tracked to closure with compliance submissions | `ten_cco` | 2 |
| U-28 | BRSR Core data capture → assurance → XBRL-ready output | CSO, `ext_assurer` | 3 |
| U-29 | Board pack assembled in P28 studio, frozen, attached to the P06 meeting | `ten_kmp` (CS) | 2 |
| U-30 | Indian group adds a UAE subsidiary in a linked tenant in the GCC cell; group dashboard aggregates; PILOT pack labelled | `ten_admin`, `prt_content_reviewer` | 4 |

## V.4 Compiled scenario registers by stream

### Tests — stream S11 (P00, P01, P24, App B, Q)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P00-T01 | Cross-tenant read denied for every table | P00 | NN-01 |
| P00-T02 | Missing tenant context fails closed | P00 | NN-01 |
| P00-T03 | Ledger UPDATE by owner fails | P00 | NN-02 |
| P00-T04 | Chain tampering detected; Governed changes frozen | P00 | NN-02 |
| P00-T05 | Super-admin date correction via dual-approved Correction Entry, tenant-visible | P00 | NN-02, NN-05 |
| P00-T06 | Maker cannot approve own correction | P00 | NN-05 |
| P00-T07 | Legal-hold blocks DOCUMENT_VERSION correction | P00 | NN-09 |
| P00-T08 | Bitemporal as-of / as-recorded queries | P00 | NN-07 |
| P00-T09 | Evidence delete within retention denied | P00 | NN-09 |
| P00-T10 | Missing export mapping fails CI | P00 | NN-10 |
| P00-T11 | Migration promotion blocked on mismatch | P00 | — |
| P00-T12 | Log scrubber removes PAN/mobile/email | P00 | NN-32 |
| P00-T13 | No Aadhaar-number columns (schema lint) | P00 | NN-12 |
| P00-T14 | Sealed DB not reachable from non-allow-listed modules | P00 | NN-13 |
| P00-T15 | Region SCP denies non-India resource | P00 | NN-24 |
| P01-T01 | Self-onboarding from health check ≤ 30 min with KYB auto-fill | P01 | — |
| P01-T02 | KYB source failure → manual field, no block | P01 | — |
| P01-T03 | No bureau pull at onboarding | P01 | NN-12 |
| P01-T04 | Maker cannot approve own item | P01 | NN-05 |
| P01-T05 | List endpoints filtered by ABAC (department head) | P01 | NN-01 |
| P01-T06 | Delivery grant approval, visible actor, revocation ≤ 60 s | P01 | NN-30 |
| P01-T07 | LawDocs reviewer cannot be sole checker | P01 | NN-05 |
| P01-T08 | Supervisor grant read-only, watermarked, expiry revokes | P01 | NN-18 |
| P01-T09 | Break-glass tenant notification and report | P01 | NN-30 |
| P01-T10 | HR exit deactivates access | P01 | — |
| P01-T11 | SMS refused as sole second factor for ten_admin | P01 | — |
| P01-T12 | Vidhi token cannot grant roles | P01 | NN-14 |
| P01-T13 | Onboarding axe zero serious; keyboard-only completion | P01 | NN-21 |
| P01-T14 | Onboarding copy has no certification claim | P01 | NN-19 |
| P24-T01 | Deployment without ChangeApproved refused | P24 | — |
| P24-T02 | Golden export detects unintended folder rename | P24 | NN-10 |
| P24-T03 | Release does not alter published content | P24 | NN-03 |
| P24-T04 | Destructive migration in expand release rejected | P24 | NN-11 |
| P24-T05 | Weekly restore test with chain verification | P24 | NN-02 |
| P24-T06 | High vulnerability SLA breach alerts | P24 | — |
| P24-T07 | Incident clocks: client 2 h, CERT-In 6 h | P24 | — |
| P24-T08 | Trust page has no certification claim without certificate | P24 | NN-19 |
| P24-T09 | No card data reaches LDC servers; script inventory match | P24 | NN-16 |

### Tests — stream S12 (P02, App A, C, D, U)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| NN-28_locked_keys_immutable | No API/UI path changes an L key | P02 | NN-28 |
| NN-28_registry_before_use | CI lint fails on unregistered key reads | P02 | NN-28 |
| NN-33_statutory_clock_never_pauses | Waiting state never moves or pauses statutory due date | P02 | NN-28 |
| NN-05_maker_not_checker_cfg | Maker cannot approve G change | P02 | NN-05 |
| NN-05_delegate_inherits_exclusion | Delegate cannot approve delegator's item | P02/P04 | NN-05 |
| NN-02_correction_entry_preserves_original | Corrected value shown; original sealed; tenant sees entry | P02 | NN-02 |
| NN-03_pack_update_preserves_tenant_adaptation | Platform pack update leaves tenant adaptation | P02 | NN-03 |
| NN-07_pinned_instance_unchanged | Rule version change doesn't alter pinned instance | P02 | NN-07 |
| NN-01_cfg_rls_cross_tenant | Tenant A cannot read tenant B settings | P02 | NN-01 |
| NN-32_no_secret_values_in_events | Events/logs omit secret_ref values | P02 | NN-32 |
| NN-21_branding_contrast_enforced | Low-contrast brand colours rejected | P02 | NN-21 |
| NN-14_ai_step_cannot_approve | Workflow validator rejects AI approval step | P02 | NN-14 |
| SOD-12_rm_not_checker | Retainer RM blocked as checker | P02/P22 | NN-05 |
| CFG-T-01 | T change effective ≤ 60 s and undoable | P02 | — |
| CFG-G-01 | Future-dated rule with preview and pins | P02 | NN-07 |
| CFG-G-02 | Golden mismatch blocks submission | P02 | — |
| CFG-FB-01 | Overdue review applies fallback | P02 | — |
| CFG-ORG-01 | Department rename keeps history | P02 | — |
| CFG-ORG-02 | Department merge preview and rollback | P02 | — |
| CFG-TERM-01 | Co-operative terminology pack; statutory names unchanged | P02 | — |
| CFG-WAIT-01 | Chase cadence and escalation | P02 | — |
| CFG-IMP-01 | Config import rejects out-of-bound values | P02 | — |
| CFG-PACK-01 | Setting pack apply with diff preserves later tenant edits | P02 | NN-29 |
| C-INBOX-01 | No bulk approve for High/Medium compliance checks | P04 | NN-05 |
| C-A11Y-01 | Every palette command and menu leaf keyboard reachable; axe clean | P02/P23 | NN-21 |
| D-ABAC-01 | Department-scoped maker cannot read other departments' instances | P01 | NN-01 |
| D-EXT-01 | External grant auto-expires ≤ 90 days | P01 | NN-18 |
| D-JML-01 | Leaver deprovisioned at configured time; items reassigned | P01/P13 | — |

### Tests — stream S1 (P03–P05, App F)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P03-IMP-01 | IFSCA AA sheet fingerprinted without _Template_Info | P03 | — |
| P03-IMP-02 | Header change blocks (V-02) | P03 | — |
| P03-IMP-03 | User columns filled block row (V-04) | P03 | — |
| P03-IMP-04 | Near-miss vocabulary suggestion | P03 | — |
| P03-IMP-05 | Round trip by CompID (3 changed / 117 unchanged) | P03 | NN-05 |
| P03-OVL-01 | Auto-rebase | P03 | NN-03 |
| P03-OVL-02 | Rebase conflict keeps tenant wording; history pinned | P03 | NN-03, NN-07 |
| P03-CAT-01 | Remove applicable instrument needs second approver; history kept | P03 | NN-29 |
| P03-COR-01 | Correction Entry dual approval; old version sealed | P03 | NN-02 |
| NN-01_cross_tenant_overlay_invisible | | P03 | NN-01 |
| NN-06_release_blocks_uncited_rows | | P03 | NN-06 |
| P04-GEN-01 | Quarterly PERIOD_END+21 due date + internal buffer | P04 | — |
| P04-GEN-02 | Event-based director appointment instances | P04 | — |
| P04-GEN-03 | Release spares closed instances | P04 | NN-03 |
| P04-MC-01 | Maker cannot review own | P04 | NN-05 |
| P04-MC-02 | High-risk evidence floor | P04 | — |
| P04-MC-03 | Retainer maker / client checker | P04 | — |
| P04-MC-04 | Delegation on leave | P04 | NN-05 |
| P04-CAL-01 | M365 sync ≤ 15 min | P04 | — |
| P04-CAL-02 | Sealed items MINIMAL in ICS | P04 | NN-13 |
| P04-NOT-01 | Updates not in notifications | P04 | NN-27 |
| P04-NOT-02 | Mandatory floor locked | P04 | — |
| P04-EXP-01 | Register export + WORKSPACE re-import | P04 | — |
| P05-MON-01 | 20:00 IST reconciliation within 30 min; SLA alerts | P05 | — |
| P05-MON-02 | Silent replacement detected via hash | P05 | — |
| P05-MON-03 | Parser drift → PARSER_BROKEN | P05 | — |
| P05-UPD-01 | Amendment → three-part update, old/new actionable, conflict task, calendar | P05 | NN-27 |
| P05-UPD-02 | Unacknowledged HIGH update escalates | P05 | — |
| P05-UPD-03 | Due-date extension applied, original kept | P05 | NN-07 |
| P05-AIS-01 | Studio output conforms to template and methodology; recall ≥95% | P05 | NN-06 |
| P05-AIS-02 | No auto-publish | P05 | NN-04, NN-05 |
| P05-AIS-03 | Tenant-only run visibility | P05 | NN-01 |
| P05-AIS-04 | Re-upload diff recorded in eval set | P05 | — |
| NN-14_studio_model_has_no_side_effect_tools | | P05 | NN-14 |
| NN-15_tenant_docs_not_used_for_training_flag_recorded | | P05 | NN-15 |

### Tests — stream S2 (App E, templates)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| T-P03-TPL-01 | Valid first upload creates NEW draft obligations with sequential CompIDs; not visible until checker publishes | P03 | NN-04, NN-05 |
| T-P03-TPL-02 | Row-2 header edited → LDC-TPL-004 | P03 | — |
| T-P03-TPL-03 | Column `applic_type` (v1.0: D) comma delimiter normalised to "; " (LDC-TPL-016) | P03 | — |
| T-P03-TPL-04 | Out-of-vocabulary value → LDC-TPL-015 with nearest suggestion | P03 | — |
| T-P03-TPL-05 | `Due:` rule parsed to PERIOD_END(quarter)+21; H consistent | P03 | — |
| T-P03-TPL-06 | Round trip: CompIDs preserved; [RETIRED] creates RETIRE; deleted row → LDC-TPL-023 | P03/P05 | NN-29 |
| T-P05-TPL-07 | Substantive update → Updates item with old/new/action; completed instances pinned | P05 | NN-07, NN-27 |
| T-P03-TPL-08 | Tenant overlay isolates T1 change from T2 and base | P03 | NN-01, NN-03 |
| T-P03-TPL-09 | [VERIFY] marker blocks publish until resolved or waived | P03 | NN-06 |
| T-P03-TPL-10 | .xlsm disguised as .xlsx rejected (LDC-TPL-010) before parse | P03 | — |
| T-P03-TPL-11 | Formula in content cell stored as text (LDC-TPL-011); export neutralised | P03 | — |
| T-P05-TPL-12 | AI-authored workbook passes the same validator; rows carry ai_generated, prompt version, clause IDs | P05/P17 | NN-04, NN-14 |
| T-P03-TPL-13 | `_validate_templates_v2.py` PASS for all 29 shipped v2.0 templates in CI (legacy `_validate_templates.py` for the 27 v1.0 workbooks); base value removal fails PR *(v1.2)* | P03 | — |
| T-P03-TPL-14 | Retired template version rejected (LDC-TPL-007 E); deprecated accepted with warning | P03 | NN-11 |
| T-P03-TPL-15 | Import idempotent on (scope, instrument version, file SHA-256) | P03 | — |
| NN-03_tenant_overlay_not_overwritten_by_base_update | Base update creates merge task, never overwrites overlay | P05 | NN-03 |
| NN-06_obligation_without_citation_not_publishable | Unresolvable K blocks publish | P03 | NN-06 |

### Tests — stream S3 (P06–P07)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| p06/blueprint.feature: listed NBFC-ML overlays | Blueprint includes LODR + NBFC Governance Directions lines with citations | P06 | NN-06 |
| p06/blueprint.feature: ID tenure at risk | Tenure ending in warning window → AT_RISK + CS task | P06 | — |
| p06/notice.feature: shorter notice path | <7 days notice forces urgency ground and ratification gate | P06 | — |
| p06/minutes.feature: sealed immutable | Super admin cannot update sealed minutes | P06 | NN-02 |
| p06/minutes.feature: circulation clock | 15-day draft clock escalates at D+13 | P06 | — |
| p06/interest.feature: quorum exclusion | Interested director excluded from item quorum (public co) | P06 | — |
| p06/registers.feature: allotment | Allotment decision → proposed MGT-1 entries + PAS-3 instance | P06 | NN-05 |
| p06/pit.feature: SDD auto entry | Opening UPSI item writes append-only SDD entry | P06 | NN-02 |
| p06/reg30.feature: 30-minute clock | Board outcome clock and delay reason | P06 | — |
| p06/rpt.feature: Schedule XII | ₹30,000 cr turnover → ₹3,500 cr threshold; 80% alert | P06 | NN-22 |
| p06/fitproper.feature: quarterly statement | Statement + MD/CEO certificate generated, task due Q+15 | P06 | — |
| p06/annual_report.feature: lineage | Every Board's report figure traceable | P06 | NN-22 |
| NN-02_sealed_minutes_immutable | — | P06 | NN-02 |
| NN-02_register_correction_preserves_original | — | P06 | NN-02 |
| NN-04_minutes_draft_requires_acceptance | — | P06 | NN-04 |
| NN-05_register_maker_not_checker | — | P06 | NN-05 |
| NN-06_blueprint_lines_cited | — | P06 | NN-06 |
| NN-07_threshold_rule_pack_effective_dated | — | P06 | NN-07 |
| NN-08_no_mca_auto_filing | — | P06 | NN-08 |
| NN-09_sealed_minutes_hash_verified | — | P06 | NN-09 |
| NN-13_board_confidential_excluded_from_analytics | — | P06 | NN-13 |
| NN-14_vidhi_cannot_sign_or_disseminate | — | P06 | NN-14 |
| NN-18_regulator_view_excludes_upsi_by_default | — | P06 | NN-18 |
| p07/redline.feature: align KYC policy | Native w:ins/w:del by "Vidhi AI (draft)" + comments; accept-all equals stored text | P07 | NN-04 |
| p07/redline.feature: unknown citation | Citation not in library flagged; blocks READY_FOR_APPROVAL | P07 | NN-06 |
| p07/approval.feature: signed copy required | EFFECTIVE blocked without signed copy | P07 | — |
| p07/approval.feature: scan similarity | <0.97 similarity requires CS confirmation | P07 | — |
| p07/review.feature: overdue issue | Overdue review → HIGH issue | P07 | — |
| p07/share.feature: share pack | Only ticked docs, watermark, no download, revoke ≤60s | P07 | NN-01 |
| p07/share.feature: sealed class | SEALED_POSH cannot be shared externally | P07 | NN-13 |
| p07/esign.feature: excluded instrument | Power of attorney blocked | P07 | — |
| p07/esign.feature: Aadhaar eSign certificate | Certificate sealed; no Aadhaar/OTP stored | P07 | NN-12 |
| p07/typecopy.feature: WhatsApp | Stitched transcript, highlights, verify, both attached | P07 | — |
| p07/translation.feature: Marathi letter | Detection, aligned translation, MT label | P07 | — |
| p07/intake.feature: re-import export | 100% auto-mapped; link duplicates; no overwrite | P07 | NN-10 |
| p07/search.feature: no snippet leakage | Unpermitted doc not returned | P07 | NN-01 |
| NN-01_search_permission_trimmed | — | P07 | NN-01 |
| NN-02_document_override_is_correction_entry | — | P07 | NN-02 |
| NN-05_policy_reviewer_not_maker | — | P07 | NN-05 |
| NN-06_redline_citations_validated | — | P07 | NN-06 |
| NN-09_sealed_version_object_lock | — | P07 | NN-09 |
| NN-10_canonical_path_from_metadata | — | P07 | NN-10 |
| NN-11_release_does_not_change_paths | — | P07 | NN-11 |
| NN-12_aadhaar_never_stored_esign | — | P07 | NN-12 |
| NN-13_sealed_class_not_shareable | — | P07 | NN-13 |
| NN-14_document_text_untrusted_no_tool_exec | — | P07 | NN-14 |
| NN-15_no_training_flag_on_ai_calls | — | P07 | NN-15 |

### Tests — stream S4 (P08–P09, App H)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| tests/acceptance/p08/applicability.feature | NBFC-ML pack, RMC, CRO-not-mandatory; corporate pack without prudential nodes | P08 | — |
| tests/acceptance/p08/ras_floor.feature | Tier 1 limit 9.5% rejected (LDC-ERM-021) | P08 | NN-22 |
| tests/acceptance/p08/ras_to_finbyx.feature | RasThresholdApproved and GET /v1/grc/kris | P08 | NN-23 |
| tests/acceptance/p08/kri_inbound.feature | Idempotent KriBreached OPEN → CURED single episode | P08 | — |
| tests/acceptance/p08/kri_escalation.feature | No plan in 5 WD escalates to CRO | P08 | — |
| tests/acceptance/p08/residual_guard.feature | LDC-ERM-014 | P08 | — |
| tests/acceptance/p08/rcsa_evidence.feature | Effective self-rating requires evidence | P08 | — |
| tests/acceptance/p08/loss_events.feature | Three dates; recovery versioning | P08 | NN-07 |
| tests/acceptance/p08/acceptance_block.feature | LE breach cannot be accepted | P08 | — |
| tests/acceptance/p08/pack_integrity.feature | Frozen pack hash; addendum on restatement | P08 | NN-02 |
| NN-01_erm_cross_tenant | Tenant A cannot read tenant B risks/KRIs via API, search, export | P08 | NN-01 |
| NN-02_erm_ledger_chain | Every ERM change appends to hash chain; chain verifies | P08 | NN-02 |
| NN-05_erm_maker_checker | Submitter cannot approve register/RAS/KRI threshold | P08 | NN-05 |
| NN-07_erm_bitemporal_assessment | Historic assessment unchanged after re-rating | P08 | NN-07 |
| NN-13_erm_sealed_fraud_event | Sealed loss event invisible to non-named users and in aggregates | P08 | NN-13 |
| NN-14_vidhi_cannot_rate_or_accept | Vidhi tool calls to rate/accept/approve are refused | P08 | NN-14 |
| NN-21_erm_heatmap_text_alternative | Heat map has table alternative and text RAG | P08 | NN-21 |
| NN-22_ras_floor | Regulatory floor enforced for all regulatory metrics per profile | P08 | NN-22 |
| NN-23_risk_feed_no_pii | Inbound events with PII rejected (LDC-ERM-052) | P08 | NN-23 |
| NN-28_erm_settings_registered | All erm.* keys exist in registry before read | P08 | NN-28 |
| NN-29_retired_node_keeps_history | Retiring taxonomy node keeps linked risks and history | P08 | NN-29 |
| tests/acceptance/p09/capital_profiles.feature | Minimums by profile (outline) | P09 | — |
| tests/acceptance/p09/bl_no_crar.feature | BL leverage only; no op-risk RWA | P09 | — |
| tests/acceptance/p09/reproducibility.feature | Recompute certified run identical | P09 | NN-22 |
| tests/acceptance/p09/snapshot_freeze.feature | ICAAP binds to frozen snapshot | P09 | NN-07 |
| tests/acceptance/p09/dq_gate.feature | Reconciliation break blocks certification | P09 | — |
| tests/acceptance/p09/lcr.feature | Inflow cap arithmetic (28.75; 173.91%) | P09 | NN-22 |
| tests/acceptance/p09/fx_sourced.feature | Finbyx CRAR shown with FX badge; no recompute | P09 | NN-23 |
| tests/acceptance/p09/scenario_immutable.feature | Approved scenario edit creates new version | P09 | — |
| tests/acceptance/p09/reverse_stress.feature | Converges ±1 bp | P09 | NN-22 |
| tests/acceptance/p09/icaap_guards.feature | No CRO review without frozen data; tracked changes draft | P09 | NN-04 |
| tests/acceptance/p09/pca_boundaries.feature | 12.0%/11.99%; 6.0%/6.01%; CIC 2.5× | P09 | — |
| tests/acceptance/p09/pca_no_auto.feature | System never places PCA | P09 | NN-08 |
| NN-22_capital_reproducible | Golden fixtures (shared with Finbyx CI) pass | P09 | NN-22 |
| NN-22_decimal_precision | No float arithmetic in kernel paths | P09 | NN-22 |
| NN-12_loan_template_rejects_pii | PAN/mobile/e-mail/Aadhaar patterns rejected | P09 | NN-12 |
| NN-13_icaap_board_confidential | ICAAP drafts restricted until approved | P09 | NN-13 |
| NN-14_vidhi_cannot_certify | Vidhi cannot certify or approve | P09 | NN-14 |
| NN-23_no_formula_push_to_finbyx | No API path sends formula logic to Finbyx | P09 | NN-23 |
| NN-05_certifier_not_preparer | Preparer cannot certify | P09 | NN-05 |
| NN-08_no_auto_submission_icaap | ICAAP submission requires human evidence | P09 | NN-08 |

### Tests — stream S5 (P10–P11, App I–J)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P10-RBIA-01 | Assessment cannot be approved with blank locked IAF para 31 parameter | P10 | NN-28 |
| P10-PLAN-01 | Plan ordered by IAF para 32 matrix; policy-max units always included | P10 | — |
| P10-IAF-39 | Marketplace professional (ia_contributor) cannot sign RBIA report | P10 | NN-05 |
| P10-HIA-43 | HIA cannot be assigned business targets or business reporting line | P10 | NN-05 |
| P10-INCAM-01 | Missing quarterly in-camera ACB–HIA meeting raises exception | P10 | — |
| P10-SAMP-01 | Sample re-run with same seed and snapshot returns identical items | P10 | NN-22 |
| P10-WP-01 | Workpaper with open review note cannot be signed off | P10 | NN-05 |
| P10-WP-02 | Edit after lock creates addendum; original hash unchanged | P10 | NN-02 |
| P10-EV-01 | Source change after linking shows drift; snapshot retained | P10 | NN-09 |
| P10-EV-02 | Verify file detects tampered evidence; P1 alert | P10 | NN-09 |
| P10-FND-01 | Remediator cannot retest | P10 | NN-05 |
| P10-FND-02 | Second High extension needs ACB noting | P10 | — |
| P10-FND-03 | Rating change after issue creates version 2 and re-emits AuditFindingRaised | P10 | NN-02 |
| P10-FND-04 | Regulatory-breach finding risk acceptance needs CCO | P10 | — |
| P10-DNBS10-01 | DNBS10 due date = 5 working days of report signing, capped 31 Dec | P10 | — |
| P10-AUD-01 | AUD para 8 checklist for ML ND NBFC includes CRAR/DNBS03 line with evidence | P10 | — |
| P10-SEC-01 | Late minutes signing flagged by SS-1 check | P10 | — |
| P10-SEC-02 | Infrabyx-linked PCS blocked for listed retainer client | P10 | NN-20 |
| P10-MIR-01 | Finbyx-owned finding read-only in LDC | P10 | NN-23 |
| P10-EXT-01 | External room read-only; expiry ends sessions ≤ 60 s | P10 | NN-18 |
| P10-VAPT-01 | VA overdue after 6 months for critical system (ML+) | P10 | — |
| P10-VAPT-02 | Recurring vulnerability becomes High finding | P10 | — |
| P10-CA-01 | Concurrent auditor tenure > 3 years on one unit blocked | P10 | — |
| P10-COR-01 | Super-admin change to issued report only via Correction Entry | P10 | NN-02 |
| P10-AI-01 | Vidhi cannot issue/rate/close a finding | P10 | NN-14 |
| P10-EXP-01 | Engagement export complete with manifest and hashes | P10 | NN-10 |
| P11-MIR-01 | Finbyx-sourced return: generate disabled, status mirrored | P11 | NN-23 |
| P11-DNBS02-01 | Non-Finbyx BL NBFC DNBS02 from Tally + Excel reconciles to TB | P11 | NN-22 |
| P11-MAP-01 | Unmapped ledger with balance blocks generation | P11 | — |
| P11-DET-01 | Regeneration with same inputs returns same file hash | P11 | NN-22 |
| P11-SEC-01 | No portal credential storage or regulator-domain HTTP clients | P11 | NN-08, NN-17 |
| P11-PII-01 | Aadhaar column rejected at parse | P11 | NN-12 |
| P11-CIC-01 | DPD-only change included in W2 incremental file | P11 | — |
| P11-CIC-02 | MFI loans only in MFI file | P11 | — |
| P11-CIC-03 | Commercial file with ~ rejected/cleaned at source | P11 | — |
| P11-CIC-04 | ME file due 5th; late transmission raises compliance issue | P11 | — |
| P11-GST-01 | No e-invoice for NBFC GSTIN | P11 | — |
| P11-GST-02 | 50% ITC election locks for FY | P11 | — |
| P11-GST-03 | Filed GSTR-3B change redirected to GSTR-1A | P11 | NN-02 |
| P11-TDS-01 | Regime selection by payment date (26Q vs Form 140) | P11 | NN-26 |
| P11-AI-01 | AI commentary with unsupported figure blocked | P11 | NN-14, NN-22 |
| P11-REV-01 | Audited CRAR ≠ filed DNBS03 opens revision assessment (REVISE) | P11 | — |
| P11-FW-01 | Framework resolution: unlisted NBFC NW ₹320 cr (2016) → Ind AS Div III | P11 | — |
| P11-FW-02 | Framework locked mid-year | P11 | — |
| P11-TALLY-01 | Agent refuses non-loopback Tally endpoint | P11 | — |
| P11-WEB-01 | Web-form channel refused above record cap | P11 | — |
| P11-ACK-01 | Run cannot close without acknowledgement hash | P11 | NN-08 |
| P11-EXP-01 | Returns evidence export folder complete | P11 | NN-10 |
| P11-RES-01 | Return files stored only in India region | P11 | NN-24 |

### Tests — stream S6 (P12–P14, App T)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| p12/incident_clocks.feature#outsourced_rbi_clock | RBI 6-hour clock starts at provider detection | P12 | NN-31 |
| p12/incident_clocks.feature#close_blocked | Close blocked with pending DPB report | P12 | NN-08 |
| p12/incident_clocks.feature#lapse_exception | Lapse → Critical exception + Board pack | P12 | NN-31 |
| p12/rights.feature#gdpr_extension_once | One extension only | P12 | — |
| p12/rights.feature#maker_checker | Author cannot approve response | P12 | NN-05 |
| p12/ropa.feature#bitemporal | ROPA as-of reproduces version | P12 | NN-07 |
| p12/outsourcing.feature#non_outsourceable | Para 15 block | P12 | — |
| p12/outsourcing.feature#halfyearly_pack | Board/RMC pack | P12 | — |
| p12/controls.feature#one_test_many_requirements | Mapping coverage | P12 | — |
| p12/packs.feature#disable_keeps_history | Disable CCPA pack | P12 | NN-29 |
| NN-08_no_auto_submission_dpb_certin_daksh | No API path submits to regulators | P12 | NN-08 |
| NN-12_no_full_aadhaar_in_rr_verification | Aadhaar pattern rejected | P12 | NN-12 |
| NN-13_rr_identity_sealed | Identity evidence excluded from search/analytics | P12 | NN-13 |
| NN-14_vidhi_cannot_submit | Vidhi tool registry has no submit tool | P12 | NN-14 |
| p13/thresholds.feature#osh_esi_at_10 | Threshold crossing creates obligations | P13 | — |
| p13/payroll.feature#three_actors | Checker cannot release | P13 | NN-05 |
| p13/payroll.feature#not_confirmed_blocks | NOT_CONFIRMED parameter blocks | P13 | NN-26 |
| p13/payroll.feature#reproducible | Recompute hash equals stored | P13 | NN-22 |
| p13/leave.feature#floor | Policy below floor rejected | P13 | — |
| p13/posh.feature#sealed_access | HR admin denied | P13 | NN-13 |
| p13/posh.feature#ic_composition | Composition validator | P13 | — |
| p13/separation.feature#revoke_and_reassign | Leaver revoked within 15 min; tasks listed | P13 | — |
| p13/regulated_roles.feature#ciso_line | CISO reporting exception | P13 | — |
| NN-25_monitoring_notice_required | Geo attendance needs notice | P13 | NN-25 |
| NN-26_params_from_signed_pack_only | Unsigned pack refused | P13 | NN-26 |
| p14/io.feature#forward_20_days | IO forward-by computation | P14 | NN-31 |
| p14/io.feature#final_reply_30_days | 30-day final-reply clock | P14 | NN-31 |
| p14/final_reply.feature#route_block | Missing route blocks send | P14 | — |
| p14/ecosystem.feature#udofin_receipt_time | Clock starts at Udofin receipt | P14 | NN-23 |
| p14/scores.feature#21_days | SCORES clock | P14 | — |
| p14/irdai.feature#ack_14_days | Insurer ack + 14-day clock | P14 | — |
| p14/sod.feature#reject_checker | Drafter cannot reject alone | P14 | NN-05 |
| p14/equator.feature#consent_required | No referral without consent | P14 | — |
| p14/reports.feature#io_quarterly | IO quarterly report due 15th | P14 | — |
| NN-21_public_form_accessibility | axe + manual AT test on public form | P14 | NN-21 |

### Tests — stream S7 (P15–P16, App G, S)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P15-AC-01 | ML rules apply from date of crossing (SBR para 22) | P15 | NN-07 |
| P15-AC-02 | Downgrade requires dispensation (para 23) | P15 | — |
| P15-AC-03 | UL only on RBI advice | P15 | — |
| P15-AC-04 | Strictest-wins across NBFC + LISTED HVDLE | P15 | — |
| P15-AC-05 | Column `conditions` (v1.0: S) unstructured condition shown | P15 | NN-04 |
| P15-AC-06 | Narrowing Locked obligation needs legal basis + second approver | P15 | NN-05, NN-28 |
| P15-AC-07 | Back-dated classification correction → Correction Entry, gap report, closed items untouched | P15 | NN-02, NN-07 |
| P15-AC-08 | Co-operative vocabulary everywhere | P15 | — |
| P15-AC-09 | AIF 10% monitor on imported register | P15 | NN-22 |
| P15-AC-10 | Jurisdiction pack gate | P15 | NN-19 |
| P15-AC-11 | What-if does not change live data | P15 | — |
| P15-AC-12 | Pack update preserves overlays | P15 | NN-03 |
| P15-GOLD-G1…G12 | Golden profiles 100% precision/recall | P15 | NN-22 |
| NN-03_pack_update_preserves_overlay | — | P15 | NN-03 |
| NN-07_classification_bitemporal_replay | — | P15 | NN-07 |
| NN-22_applicability_reproducible | — | P15 | NN-22 |
| NN-28_locked_floor_not_loosened | — | P15 | NN-28 |
| NN-29_instrument_removal_keeps_history | — | P15 | NN-29 |
| NN-19_jurisdiction_pack_claim_gate | — | P15 | NN-19 |
| P16-AC-01 | MSCS deemed refusal of membership | P16 | NN-31 |
| P16-AC-02 | Bye-law cannot loosen Act (LDC-COOP-001) | P16 | NN-28 |
| P16-AC-03 | AGM default triggers disqualification watch | P16 | NN-31 |
| P16-AC-04 | CEA notice 6 months before term | P16 | NN-31 |
| P16-AC-05 | Finbyx SoR: LDC edit refused, projection sync | P16 | NN-23 |
| P16-AC-06 | Deposit-eligibility exception mirrored to board | P16 | — |
| P16-AC-07 | MSCS appropriation validation incl. CRRD | P16 | NN-22 |
| P16-AC-08 | Maharashtra Form O clock | P16 | NN-31 |
| P16-AC-09 | RBI Ombudsman not offered to society members | P16 | NN-31 |
| P16-AC-10 | No "bank" in name | P16 | NN-28 |
| P16-AC-11 | STUB State pack keeps operations open | P16 | — |
| NN-02_coop_register_immutable | — | P16 | NN-02 |
| NN-07_register_as_at_replay | — | P16 | NN-07 |
| NN-12_no_aadhaar_in_member_record | — | P16 | NN-12 |
| NN-23_finbyx_sor_no_edit | — | P16 | NN-23 |
| NN-28_coop_guardrails_locked | — | P16 | NN-28 |
| NN-31_coop_clock_owned | — | P16 | NN-31 |

### Tests — stream S8 (P17–P19, App K–M)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| T-P17-01 | Scope intersection limits retrieval | P17 |  |
| T-P17-02 | Delegating user is suspended mid-schedule | P17 |  |
| T-P17-03 | Prohibited tool is not exposed | P17 |  |
| T-P17-04 | Cited answer from the current version | P17 |  |
| T-P17-05 | Out-of-corpus question is declined | P17 |  |
| T-P17-06 | Superseded source is flagged | P17 |  |
| T-P17-07 | Personal data never leaves India | P17 |  |
| T-P17-08 | Low-confidence lines are highlighted and versioned | P17 |  |
| T-P17-09 | Policy update against previous approved version | P17 |  |
| T-P17-10 | Hard stop at budget | P17 |  |
| T-P17-11 | Instruction inside an uploaded document is ignored | P17 |  |
| T-P17-12 | AI disabled tenant still completes minutes | P17 |  |
| NN-01_ai_retrieval_isolation | NN automated test | P17 | NN-01 |
| NN-04_ai_no_autopublish | NN automated test | P17 | NN-04 |
| NN-05_ai_maker_checker_separation | NN automated test | P17 | NN-05 |
| NN-06_ai_citation_required | NN automated test | P17 | NN-06 |
| NN-13_ai_sealed_exclusion | NN automated test | P17 | NN-13 |
| NN-14_ai_prohibited_tools_* | NN automated test | P17 | NN-14 |
| NN-15_ai_no_training_export | NN automated test | P17 | NN-15 |
| NN-22_ai_figure_binding | NN automated test | P17 | NN-22 |
| NN-24_ai_india_routing | NN automated test | P17 | NN-24 |
| NN-32_ai_no_content_in_logs | NN automated test | P17 | NN-32 |
| T-P18-01 | ObligationPublished uses the ecosystem type | P18 |  |
| T-P18-02 | Duplicate inbound event is harmless | P18 |  |
| T-P18-03 | Personal data without consentref is rejected | P18 |  |
| T-P18-04 | Hub subject rejects personal data | P18 |  |
| T-P18-05 | EMBEDDED to LDC_EXTERNAL | P18 |  |
| T-P18-06 | No machine channel to RBI portals | P18 |  |
| T-P18-07 | CIN pre-fill with consent | P18 |  |
| T-P18-08 | No bureau pull | P18 |  |
| T-P18-09 | ICS feed respects role scope | P18 |  |
| T-P18-10 | Statutory dates are not changed from the calendar | P18 |  |
| T-P18-11 | Replay requires a second approver | P18 |  |
| T-P18-12 | Complaint from client website | P18 |  |
| NN-01_int_tenant_isolation_clients | NN automated test | P18 | NN-01 |
| NN-05_int_dlq_replay_checker | NN automated test | P18 | NN-05 |
| NN-08_int_no_portal_machine_channel | NN automated test | P18 | NN-08 |
| NN-12_int_no_aadhaar_storage | NN automated test | P18 | NN-12 |
| NN-23_int_contracts_only | NN automated test | P18 | NN-23 |
| NN-24_int_storage_residency | NN automated test | P18 | NN-24 |
| NN-30_int_no_ops_hub_tenant_data | NN automated test | P18 | NN-30 |
| NN-32_int_no_bodies_in_logs | NN automated test | P18 | NN-32 |
| T-P19-01 | Full tenant export reconciles and verifies offline | P19 |  |
| T-P19-02 | Export never blocked for non-payment | P19 |  |
| T-P19-03 | Release with schema change keeps paths | P19 |  |
| T-P19-04 | Department rename does not break mapping | P19 |  |
| T-P19-05 | CI blocks an unmapped record type | P19 |  |
| T-P19-06 | Non-India bucket refused for regulated data | P19 |  |
| T-P19-07 | Google Drive limited to non-regulated data | P19 |  |
| T-P19-08 | Missed backups escalate | P19 |  |
| T-P19-09 | Round-trip of an LDC package | P19 |  |
| T-P19-10 | Nothing is overwritten | P19 |  |
| T-P19-11 | HR folder needs DPO approval | P19 |  |
| T-P19-12 | Exit with deletion certificate | P19 |  |
| NN-10_export_coverage | NN automated test | P19 | NN-10 |
| NN-10_golden_path_stability | NN automated test | P19 | NN-10 |
| NN-11_no_destructive_migration | NN automated test | P19 | NN-11 |
| NN-09_export_hash_integrity | NN automated test | P19 | NN-09 |
| NN-12_no_aadhaar_in_exports | NN automated test | P19 | NN-12 |
| NN-17_no_credentials_in_exports | NN automated test | P19 | NN-17 |
| NN-24_target_residency | NN automated test | P19 | NN-24 |
| NN-29_detach_keeps_history | NN automated test | P19 | NN-29 |
| NN-05_full_export_second_approver | NN automated test | P19 | NN-05 |

### Tests — stream S9 (P20–P22, App N, O, X)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| p20/configurator.feature:dependency_prompt | Running total with dependency prompt; no pre-ticked paid item | P20 | NN-19 |
| p20/configurator.feature:prior_price | Prior price = lowest in last 30 days | P20 | NN-19 |
| p20/configurator.feature:gst_before_pay | GST-inclusive total before Pay | P20 | NN-16 |
| p20/trial.feature:health_check_to_trial | ≤ 12 clicks; TenantSelfServeCreated once | P20 | — |
| p20/trial.feature:one_trial_per_org | Duplicate CIN refused LDC-BIL-011 | P20 | — |
| p20/trial.feature:no_auto_conversion | Trial expiry → read-only, no charge | P20 | NN-19 |
| p20/trial.feature:extension_checker | > 14 days needs checker | P20 | NN-05 |
| p20/entitlements.feature:restricted_statutory | RESTRICTED never blocks statutory work/export/auditors | P20 | NN-29 |
| p20/entitlements.feature:mismatch_no_downgrade | Reconciliation break keeps generous state | P20 | — |
| p20/checkout.feature:redirect_not_proof | Redirect without event stays pending | P20 | NN-16 |
| p20/studio.feature:claim_without_evidence | LDC-BIL-033 blocks | P20 | NN-19 |
| p20/studio.feature:price_change_oh8 | Price change via OH8 change request | P20 | NN-05 |
| p20/streams.feature:kill_switch_5min | Stream hidden within 5 min | P20 | — |
| p20/savings.feature:roi_excludes_modelled | ROI excludes modelled exposure | P20 | NN-22 |
| p20/savings.feature:stale_rule_excluded | Penalty rule > 180 days excluded | P20 | NN-22 |
| NN-01_billing_rls | Billing tables RLS | P20 | NN-01 |
| NN-16_saq_a_no_payment_script | No payment JS on LDC origins | P20 | NN-16 |
| NN-29_entitlement_never_blocks | Never-block list | P20 | NN-29 |
| NN-32_no_pii_in_usage_aggregate | Usage payload schema rejects identifiers | P20 | NN-32 |
| p21/public.feature:browse_without_login | No login to browse/search | P21 | — |
| p21/public.feature:ranking_disclosure | Ranking parameters link | P21 | — |
| p21/profession.feature:advocate_rule36 | Rule 36 schema only | P21 | NN-20 |
| p21/profession.feature:ca_listing_off | LDC-MKP-012 | P21 | NN-20 |
| p21/profession.feature:counsel_ref_required | LDC-MKP-015 | P21 | NN-20 |
| p21/re_guardrails.feature:vcco_support_only | Notice + acknowledgement | P21 | — |
| p21/independence.feature:certification_wall | LDC-MKP-020 | P21 | — |
| p21/no_saas.feature:buy_fixed_service | Invoice, Engagement Room, no tenant | P21 | NN-16 |
| p21/retainer.feature:sla_credit | Breach → ServiceCreditIssued 5% | P21 | — |
| p21/retainer.feature:grant_revoked_on_end | RetainerEnded revokes grants | P21 | NN-30 |
| p21/academy.feature:stale_feed | Prices hidden after 7 days | P21 | — |
| p21/academy.feature:certificate_consent | No consent → not imported | P21 | NN-12 |
| NN-20_profession_render_allowlist | Fixed schemas per mode | P21 | NN-20 |
| NN-20_no_commission_regulated_professions | Commission impossible for regulated professions | P21 | NN-20 |
| NN-13_posh_engagement_sealed | POSH engagement content sealed | P21 | NN-13 |
| p22/grants.feature:propose_approve | Client admin approval with checker bound | P22 | NN-30 |
| p22/grants.feature:never_checker | LDC-SDC-007 | P22 | NN-05 |
| p22/grants.feature:super_admin_cannot_approve | LDC-SDC-008 | P22 | NN-30 |
| p22/grants.feature:leaver_sweep_15min | Grants suspended, rotation prompts | P22 | — |
| p22/vault.feature:rbi_client_only | LDC-SDC-012 | P22 | NN-17 |
| p22/vault.feature:reveal_logged_notified | 30 s reveal, ledger, notify | P22 | NN-17 |
| p22/vault.feature:no_bulk_export | Export metadata only | P22 | NN-17 |
| p22/oh.feature:no_compliance_content | Contract corpus check | P22 | NN-23 |
| p22/deliverables.feature:reviewer_differs | LDC-SDC-020 | P22 | NN-05 |
| p22/deliverables.feature:lands_in_dms | DMS version + export path | P22 | NN-10 |
| p22/masterdata.feature:correction_entry | Applied only as Correction Entry | P22 | NN-02 |
| NN-25_no_covert_monitoring | No keystroke/screen capture code paths | P22 | NN-25 |
| NN-32_no_secrets_in_logs | Vault secrets never logged | P22 | NN-32 |

### Tests — stream S10 (P23, App P, R)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P23-AT-01 | Crawlers see full content without JavaScript (h1, ≥300 words, JSON-LD) | P23 | — |
| P23-AT-02 | llms.txt served as text/plain | P23 | — |
| P23-AT-03 | Legacy sitemap URLs return 200/301, never 404 | P23 | — |
| P23-AT-04 | NBFC Base Layer health check end-to-end → lead to Hub ≤ 60 s → trial pre-fill | P23 | NN-12 |
| P23-AT-05 | Critical-gap cap on band | P23 | NN-22 |
| P23-AT-06 | Report reproducible after scoring-model change | P23 | NN-22 |
| P23-AT-07 | No lead record or marketing pixel before consent | P23 | NN-15 |
| P23-AT-08 | Share-link revocation returns 410 | P23 | — |
| P23-AT-09 | Expired claim removed and page republished | P23 | NN-19 |
| P23-AT-10 | Prohibited phrase blocks review (LDC-WEB-012) | P23 | NN-19 |
| P23-AT-11 | Glossary coverage = 100% of keys in release build | P23 | — |
| P23-AT-12 | "i" popover keyboard/screen-reader behaviour (1.4.13) | P23 | NN-21 |
| P23-AT-13 | Serious axe violation blocks promotion | P23 | NN-21 |
| P23-AT-14 | Focus not obscured by sticky bars (2.4.11) | P23 | NN-21 |
| P23-AT-15 | Sign-in without cognitive tests; OTP paste (3.3.8) | P23 | NN-21 |
| P23-AT-16 | Tutorial stale after UI change | P23 | — |
| P23-AT-17 | Capture refuses non-demo tenant (LDC-HLP-004) | P23 | NN-01 |
| P23-AT-18 | PDF reports pass PDF/UA check | P23 | NN-21 |
| P23-AT-19 | Health-check PAN masked, not stored without trial | P23 | NN-12 |
| P23-AT-20 | AI narrative labelled, fallback when model down | P23 | NN-04, NN-14 |
| NN-19_claims_block_publish, NN-19_prohibited_phrases, NN-19_hc_disclaimer_present | Claims Register gates | P23 | NN-19 |
| NN-21_axe_gate, NN-21_contrast_tokens, NN-21_focus_not_obscured, NN-21_pdfua_templates | Accessibility gates | P23 | NN-21 |
| NN-12_hc_pan_masked_not_stored | Identity minimisation in health check | P23 | NN-12 |
| NN-22_hc_score_reproducible | Deterministic scoring | P23 | NN-22 |
| NN-04_ai_content_requires_approval_web | No auto-publish of AI content on public site | P23 | NN-04 |
| NN-15_no_lead_data_to_unapproved_provider | Provider/region approval | P23 | NN-15 |

## V.6 Compiled v1.1 scenario registers

#### Tests — v1.1 G1 (P25, App Y)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P25-AC-01 | INTL-GEN row without reviewer line blocked (LDC-TPL-041) | P25 | G1-NN-A |
| P25-AC-02 | Two-key publication required | P25 | NN-05 |
| P25-AC-03 | Machine-unreviewed translation blocks publication | P25 | G1-NN-C |
| P25-AC-04 | Stale monitoring suspends pack, instances continue | P25 | NN-19, NN-29 |
| P25-AC-05 | Foreign entity onboarding with registry data; calendar in local TZ/holidays; India link | P25 | NN-33 |
| P25-AC-06 | Foreign register entries append-only | P25 | NN-36 |
| P25-AC-07 | Structure chart as-at date (bitemporal) | P25 | NN-07 |
| P25-AC-08 | EU entity data stays in EU cell; group view aggregates only | P25 | G1-NN-B |
| P25-AC-09 | Indian entity cannot change home cell without basis | P25 | G1-NN-B |
| P25-AC-10 | Cross-cell replication needs transfer basis | P25 | G1-NN-B |
| P25-AC-11 | Partner query SLA breach escalates and scores | P25 | — |
| P25-AC-12 | Partner expert cannot act as checker | P25 | NN-43 |
| P25-AC-13 | Arabic RTL calendar passes WCAG 2.2 AA | P25 | NN-21 |
| P25-AC-14 | EU client invoice wording; no card data | P25 | NN-16 |
| P25-AC-15 | Bulk entity import with duplicates | P25 | — |
| P25-AC-16 | Default home cell by jurisdiction; deferred activation if cell closed | P25 | — |
| P25-AC-17 | Licensed signal needs primary source | P25 | NN-34 |
| P25-AC-18 | Escalation on entity-local working week | P25 | NN-33 |
| P25-AC-19 | Client-authored foreign content labelled and excluded from coverage | P25 | NN-19 |
| NN-01_cell_isolation_canary | Synthetic PII canary never leaves home cell | P25 | NN-01 |
| NN-41_ai_route_per_cell | AI calls route in-cell, no failover outside permitted regions | P25 | NN-41 |

#### Tests — v1.1 G3 (P17, App AA, K)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P17-V11-01 | L1 agent cannot execute INTERNAL_WRITE; proposal created instead | P17 | NN-14, NN-41 |
| P17-V11-02 | Effective autonomy = minimum of platform, tenant, agent, skill, mission, sealed | P17 | NN-41 |
| P17-V11-03 | Auto-demotion after two material undo events in 7 days | P17 | — |
| P17-V11-04 | MCP read returns only the user's scoped items; ExternalAiAccessed logged | P17/P18 | NN-01, NN-41 |
| P17-V11-05 | MCP write requires URL-mode elicitation and approval in LDC | P18 | NN-14 |
| P17-V11-06 | Prohibited tools not listed to MCP clients | P18 | NN-14 |
| P17-V11-07 | External MCP tool drift suspends the tool | P17 | — |
| P17-V11-08 | Tenant kill switch pauses missions and runs within 60 s | P17 | — |
| P17-V11-09 | Mission hand-off evaluated with delegator scope (confused deputy prevented) | P17 | NN-41 |
| P17-V11-10 | Memory candidate from untrusted upload is quarantined | P17 | NN-14 |
| P17-V11-11 | A2A task without mapped Ecosystem contract rejected | P18 | NN-23 |
| P17-V11-12 | Sealed classes never returned by ldc-mcp; PII masked without client basis | P18 | NN-13, NN-24 |
| P17-V11-13 | Sponsor leaver pauses L2 agent | P17 | — |
| P17-V11-14 | CCM narrative numbers match test run (number fidelity) | P17 | NN-37 |
| P12-AIG-01 | AI risk classification proposed by VA-15 cannot be saved without officer approval | P12 | NN-05 |
| P12-AIG-02 | Kill-switch test record overdue raises CCM exception | P12 | — |
| NN-41_autonomy_filter_* | Tool list filtered by effective autonomy before model call | P17 | NN-41 |

#### Tests — v1.1 F1 (P00–P02, P24, App A, B, D, Q, U)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P00-V11-01 | No query crosses cells (two-cell probe) | P00 | NN-24 |
| P00-V11-02 | Partial undo lists later-changed items | P00 | NN-49 |
| P00-V11-03 | Act date drives timeliness (filed on time, approved late) | P00 | NN-48 |
| P00-V11-04 | Kill switch propagates ≤ 60 s | P00 | NN-51 |
| P01-V11-01 | Profile ≤ 12 questions, ≥ 6 pre-filled with source, reasons shown | P01 | — |
| P01-V11-02 | Applicability challenge creates CCO task and reversible overlay | P01 | NN-03 |
| P01-V11-03 | Indian entity cannot choose foreign cell | P01 | NN-24 |
| P01-V11-04 | Tracker import create-only and undoable within 24 h | P01 | NN-49, NN-47 |
| P01-V11-05 | Agent refused without delegation grant (LDC-IAM-090) | P01 | NN-41 |
| P01-V11-06 | J-01 usability: ≤ 12 clicks, ≤ 10 minutes p75 | P01 | — |
| P02-V11-01 | Custom register built and exported without code release | P02 | NN-10 |
| P02-V11-02 | Publish blocked until simulation reviewed | P02 | NN-05 |
| P02-V11-03 | Effective autonomy is the minimum across scopes | P02 | NN-50 |
| P02-V11-04 | Tenant kill switch stops missions ≤ 60 s | P02 | NN-51 |
| P02-V11-05 | Template application undo within window | P02 | NN-49 |
| P24-V11-01 | Evaluation gate blocks AI regression | P24 | NN-14 |
| P24-V11-02 | Cell release lag respected unless security override | P24 | — |
| P24-V11-03 | Region migration preserves ids and audit chain | P24 | NN-11, NN-02 |

#### Tests — v1.1 F2 (P03–P05, App E, F)

| Test | Feature file | Phase | Rule |
|---|---|---|---|
| RBI catalogue and coverage (placeholders, reference gate) | `tests/acceptance/p03/catalogue.feature` | P03 | D-39, NN-55 |
| Tracker import and undo | `p03/tracker_import.feature` | P03 | NN-04, NN-49 |
| Common controls | `p03/controls.feature` | P03 | NN-50 |
| Applicability (≤ 12 questions; incremental re-evaluation; reason strings) | `p03/applicability.feature` | P03 | IMP-001/002/006 |
| Foreign packs (pack lifecycle, reviewer line, translations) | `p03/foreign_packs.feature` | P03 | NN-53, NN-54 |
| Three dates and timeliness | `p04/timeliness.feature` | P04 | NN-48 |
| Placeholders | `p04/placeholders.feature` | P04 | D-39 |
| Automated checks | `p04/automated_checks.feature` | P04 | NN-47 |
| Event bundles | `p04/event_bundles.feature` | P04 | — |
| Notification budget | `p04/notification_budget.feature` | P04 | G5 E-19 |
| Bulk edit with undo | `p04/bulk_edit.feature` | P04 | NN-46, NN-49 |
| Compliance testing | `p04/testing.feature` | P04 | — |
| Working Register export keeps the v2.0 contract and key hash; Period in `_LDC_System` *(v1.2)* | `p04/exports.feature` | P04 | LDC-TPL-005 |
| RBI category pages | `p05/rbi_pages.feature` | P05 | AB.8 |
| Content incident | `p05/content_incident.feature` | P05 | — |
| Updates noise control | `p05/updates_noise.feature` | P05 | NN-27 |
| v1.1 importer rules (withdrawn citation, placeholder replacement, reviewer line, undo, validator with both samples) | `p03/template_import_v11.feature` | App E §E.16 | NN-49, 53, 55 |
| Validator CI: 26 templates PASS with both owner samples; shared row-2 hash | CI job | App E | — |
| Catalogue drift = 0 after weekly reconciliation; SRC-RBI-30…52 row-set hash skip | `p05/rbi_pages.feature` (add) | App F | — |
| Licensed signal never becomes Update without primary source | `p05/foreign_sources.feature` | App F §F.12B | LDC-CHG-121 |

NN tests added: P03 `NN-49_import_batch_undo_compensates`, `NN-52_mcp_obligation_tools_respect_rls`, `NN-53_unpublished_pack_not_offered`, `NN-54_machine_translation_blocks_publish`, `NN-55_withdrawn_citation_blocked`; P04 `NN-47_agent_cannot_set_status`, `NN-48_three_dates_recorded`, `NN-49_bulk_edit_undo`, `NN-50_coordinator_autonomy_bounded`, `NN-52_mcp_instance_tools_scoped`; P05 `NN-47_agent_cannot_triage_not_relevant`, `NN-50_regulatory_analyst_autonomy_bounded`, `NN-52_mcp_updates_tools_scoped`, `NN-54_foreign_translation_labelled`, `NN-55_studio_rows_citing_withdrawn_blocked`; App E `NN-49_tenant_import_undo_restores_state`, `NN-53_intl_row_without_reviewer_blocked`, `NN-54_unreviewed_machine_translation_not_publishable`, `NN-55_withdrawn_citation_blocks_commit`, `NN-50_authoring_agent_never_publishes`.

#### Tests — v1.1 F3 (P06, P07, P10, P26, P27, App J)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P06-V11-01 | Annotations re-anchored after paper replacement (≥ 90%) | P06 | — |
| P06-V11-02 | Prompts hidden until CS release | P06 | NN-50 |
| P06-V11-03 | Decisions become tasks; ATR auto-generated | P06 | — |
| P06-V11-04 | Annual-report assembly blocked on missing disclosure | P06 | — |
| P06-V11-05 | Post-freeze change creates variance, not edit | P06 | NN-22 |
| P06-V11-06 | Transmission clock unchanged while awaiting docs | P06 | NN-33 |
| P06-V11-07 | RPTx route; no /rpt/ under gov | P06 | — |
| P07-V11-01 | Baton nudge and cooldown | P07 | — |
| P07-V11-02 | Parallel lanes consolidate comments | P07 | — |
| P07-V11-03 | Drift item creation, no status change | P07 | NN-47 |
| P07-V11-04 | Bulk roll-forward undo | P07 | NN-49 |
| P07-V11-05 | Forms published without capturing customer data | P07 | NN-23 |
| P10-V11-01 | Scope share includes new evidence, excludes sealed | P10 | NN-13 |
| P10-V11-02 | Existing evidence suggested for PBC item | P10 | — |
| P10-V11-03 | Sample expansion on deviation | P10 | NN-22 |
| P10-V11-04 | Inspection closure requires verification test | P10 | — |
| P10-V11-05 | Workpaper lock on review | P10 | NN-05 |
| P10-V11-06 | VA-07 cannot issue findings | P10 | NN-50 |
| P26-01 – P26-12 | Notice handling, approval block, clock no pause, directions to tasks, provision class, observation verification, recovery projection, recovery-notice block, auto-renew alert, licence expiry, gift pre-clearance, counsel isolation | P26 | NN-01, 05, 08, 13, 22, 33, 39, 47 |
| P27-01 – P27-09 | Applicability, evidence + checker, GHG factor stamp, CSR transfer clock, CSR-1 block, BRSR freeze, restatement proposal, value-chain 2% selection | P27 | NN-05, 22, 33, 37, 38 |

#### Tests — v1.1 F4 (P08, P09, P11, P28, App H, I)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P08-v11-01 | Methodology re-rating keeps history | P08 | NN-07 |
| P08-v11-02 | AI-suggested risk accepted without rating | P08 | NN-47 |
| P08-v11-03 | Autonomy ceiling above L2 rejected | P08 | NN-50 |
| P08-v11-04 | KRI breach opens one linked compliance issue | P08 | NN-33 |
| P08-v11-05 | Failed automated test flags control, residual unchanged | P08 | NN-47 |
| P08-v11-06 | Starter kit install and undo | P08 | NN-49 |
| P08-v11-07 | Group view shows GCC entity aggregates only | P08 | NN-24 |
| P09-v11-01 | Edited figure blocks result-card export | P09 | NN-37 |
| P09-v11-02 | Re-run as at reproduces outputs | P09 | NN-22 |
| P09-v11-03 | Internal metric cannot reuse R1 | P09 | NN-38 |
| P09-v11-04 | Sandbox excluded from packs | P09 | NN-22 |
| P09-v11-05 | Capital-plan EWS raised | P09 | NN-38 |
| P11-v11-01 | Second period auto-maps from memory | P11 | — |
| P11-v11-02 | Kernel rule without plain message fails CI | P11 | — |
| P11-v11-03 | Prepare due returns stops before human steps | P11 | NN-08 |
| P11-v11-04 | Returns Preparer cannot package | P11 | NN-50 |
| P11-v11-05 | Supervisory Returns Direction amendment opens kernel CR and Update | P11 | NN-34 |
| P28-AC-01 | Ungoverned widget fails CI | P28 | NN-22 |
| P28-AC-02 | Uncertified regulatory metric labelled indicative | P28 | NN-38 |
| P28-AC-03 | Re-run as at equals original hash | P28 | NN-22 |
| P28-AC-04 | Re-run mismatch raises Critical incident | P28 | NN-22 |
| P28-AC-05 | CCO builds and schedules report without support | P28 | — |
| P28-AC-06 | Formula column cannot redefine regulatory metric | P28 | NN-38 |
| P28-AC-07 | Frozen pack immutable; addendum offered | P28 | NN-09 |
| P28-AC-08 | Unbound figure blocks freeze | P28 | NN-37 |
| P28-AC-09 | Board pack delivered to P06 meeting, no e-mail attachment | P28 | NN-13 |
| P28-AC-10 | Author cannot approve own report | P28 | NN-05 |
| P28-AC-11 | Sealed fields absent from builder | P28 | NN-13 |
| P28-AC-12 | Aggregates only from other regional cells | P28 | NN-24 |
| P28-AC-13 | 50k-row report async < 2 min | P28 | — |
| P28-AC-14 | Vidhi drafts definitions without figures | P28 | NN-41, NN-50 |

#### Tests — v1.1 F5 (P12–P16, App G, S, T)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P12-V11-01 | Unregistered AI use raises issue, no auto-class | P12 | NN-47 |
| P12-V11-02 | EU-scope credit scoring → high-risk proposal + FRIA prompt | P12 | NN-38 |
| P12-V11-03 | Validator independence | P12 | NN-05 |
| P12-V11-04 | Kill-switch test overdue issue | P12 | NN-51 |
| P12-V11-05 | Import LDC vendor AI assurance pack | P12 | — |
| P12-V11-06 | Third Schedule retention and 48-h pre-erasure timer | P12 | NN-07 |
| P12-V11-07 | Phase flip produces approved diff only | P12 | NN-34 |
| P12-V11-08 | Processor-only tenant has no notice obligations | P12 | — |
| P12-V11-09 | Certificate expiry triggers reassessment | P12 | — |
| P12-V11-10 | Materiality rule-computed | P12 | NN-47 |
| P12-V11-11 | Inbound DDQ answers cite evidence and need approval | P12 | NN-14 |
| P13-V11-01 | Auto-approval excludes sensitive-position block | P13 | NN-05 |
| P13-V11-02 | Wage-definition warning at design time | P13 | NN-26 |
| P13-V11-03 | What-if does not post | P13 | NN-22 |
| P13-V11-04 | Contractor upload closes checkpoint with act date | P13 | NN-48 |
| P13-V11-05 | Branch adds State packs | P13 | — |
| P13-V11-06 | Registers reproducible from HRMS data | P13 | — |
| P14-V11-01 | Clock starts on receipt even if AI down | P14 | NN-33 |
| P14-V11-02 | AI cannot close complaint | P14 | NN-47 |
| P14-V11-03 | Unmapped category blocks MIS | P14 | — |
| P14-V11-04 | WhatsApp refused for recovery | P14 | — |
| P14-V11-05 | Chatbot human route creates case | P14 | NN-33 |
| P15-V11-01 | ≤ 12 applicability questions | P15 | — |
| P15-V11-02 | Why-it-applies card | P15 | NN-06 |
| P15-V11-03 | Multi-licence merge with provenance | P15 | NN-03 |
| P15-V11-04 | Placeholder replaced via diff | P15 | NN-34 |
| P15-V11-05 | PFRDA coming-soon, no empty catalogue | P15 | — |
| P15-V11-06 | Foreign subsidiary without published pack | P15 | NN-53 |
| P16-V11-01 | Notice delivery evidence with act date | P16 | NN-48 |
| P16-V11-02 | Audit memo → para tracker | P16 | — |
| P16-V11-03 | Inspection request redaction | P16 | NN-13 |
| P16-V11-04 | AI cannot decide disqualification | P16 | NN-47 |

#### Tests — v1.1 F6 (P18–P23, App C, L, M, N, O, P, X)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P18-V11-01 | MCP never returns sealed data (canary) | P18 | NN-52, NN-13 |
| P18-V11-02 | No prohibited MCP tools listed | P18 | NN-14, NN-52 |
| P18-V11-03 | MCP parity with REST permissions | P18 | NN-52 |
| P18-V11-04 | Changed external tool description suspends tool | P18 | NN-50 |
| P18-V11-05 | Unmapped A2A task rejected | P18 | NN-52 |
| P18-V11-06 | Wrong-cell request redirected, no cross-cell serving | P18 | NN-24 |
| P18-V11-07 | Connector import undo within window | P18 | NN-49 |
| P18-V11-08 | FX snapshot travels with value | P18 | NN-22 |
| P19-V11-01 | New module records land in folders 25–29; 01–24 unchanged | P19 | NN-10, NN-45 |
| P19-V11-02 | Per-cell packages and aggregate-only group index | P19 | NN-24 |
| P19-V11-03 | Indian entity migration blocked without basis | P19 | NN-24 |
| P19-V11-04 | Migration auto-rollback on hash mismatch | P19 | NN-09 |
| P19-V11-05 | Intake undo with approved-item confirmation | P19 | NN-49 |
| P19-V11-06 | AI cannot obtain export link | P19 | NN-14, NN-52 |
| P20-V11-01 | Foreign price book and OH8 tax preview; no FX-derived price | P20 | NN-16, X-02 |
| P20-V11-02 | Statutory work continues at AI budget zero | P20 | NN-42 |
| P20-V11-03 | Free seats not counted | P20 | — |
| P20-V11-04 | Renewal price shown before payment | P20 | NN-44 |
| P20-V11-05 | Cancellation ≤ 3 clicks | P20 | NN-44 |
| P20-V11-06 | Auditor seats expire with engagement | P20 | NN-30 |
| P21-V11-01 | Foreign commercial switch needs counsel reference | P21 | NN-20 |
| P21-V11-02 | Preparer cannot assure same BRSR | P21 | — |
| P21-V11-03 | Firm plan creates no listing | P21 | NN-20 |
| P21-V11-04 | Gap suggestion labelled and dismissible | P21 | NN-44 |
| P22-V11-01 | Firm user maker-only | P22 | NN-43 |
| P22-V11-02 | Break-glass visible on transparency page ≤ 1 min | P22 | NN-30 |
| P22-V11-03 | Partner professional limited to jurisdiction | P22 | NN-24 |
| P22-V11-04 | RM-started agent output needs client approval | P22 | NN-43, NN-50 |
| P23-V11-01 | No country page without PUBLISHED pack | P23 | NN-53 |
| P23-V11-02 | Generic group check labelled | P23 | NN-19 |
| P23-V11-03 | Locale pages server-rendered | P23 | NN-44 |
| P23-V11-04 | Inline regulatory help panel | P23 | — |
| C-V11-01 | Click budgets J-01–J-26 within 20% of target | C/P24 | — |
| C-V11-02 | Tenant kill switch pauses all agents ≤ 60 s | C/P17 | NN-51 |

## V.7 Compiled v1.2 scenario registers *(v1.2)*

*(v1.2)* Compiled by the pack lead from the v1.2 editors' registers (T1 templates and Appendix E; T3 P04 list, RAG, conversations and accountability; T4 P03 CompID generation, P05, P23; T5 business-ID registry, P01 onboarding, P06, P08, P09, P18). Where a v1.2 entry amends an earlier code, the v1.2 entry prevails.

#### NN test index additions *(v1.2)*

| NN | Rule (short) | Test prefix | Primary phases |
|---|---|---|---|
| NN-56 | Business IDs are permanent | `tests/nn/NN-56_*.spec.ts` | P00, P03, P06, P08, P09 |
| NN-57 | Audit trail by business ID | `tests/nn/NN-57_*.spec.ts` | P00, P04, P18 |
| NN-58 | Deterministic RAG; predictions labelled | `tests/nn/NN-58_*.spec.ts` | P04, P02 |
| NN-59 | Conversations are records | `tests/nn/NN-59_*.spec.ts` | P04 |
| NN-60 | Responsibility from the ledger | `tests/nn/NN-60_*.spec.ts` | P04 |

#### UAT journeys added in v1.2

| # | Journey | Phases |
|---|---|---|
| UAT-V12-01 | Content maker uploads a new RBI direction sheet on the v2.0 template with CompID blank → preview shows reserved CompIDs → checker publishes → CompIDs assigned; re-upload of the exported sheet updates the same CompIDs | P03 |
| UAT-V12-02 | Owner's existing v1.0 NBFC sheet imports through the legacy map; instrument confirmed; downloaded as v2.0 | P03 |
| UAT-V12-03 | Compliance officer opens the 9-column list, filters High risk + Due in 30 days, groups by Department → Function, stars three CompIDs, exports to Excel and PDF | P04 |
| UAT-V12-04 | CCO raises an Explanation Request on a Red item; maker answers within SLA; accountability report shows the computed timeline and the explanation | P04 |
| UAT-V12-05 | Super admin builds an NBFC health-check set by choosing sections, 25 questions by CompID and weights; checker publishes; a prospect's answers pre-fill the tenant baseline on conversion | P23 |
| UAT-V12-06 | New NBFC onboards by PAN/CIN; provider and public-register look-ups pre-fill fields with provenance and confidence; tenant organisation code assigned and locked at first ID | P01, P18 |
| UAT-V12-07 | CRO imports the Risk Register template; RiskIDs issued; a risk is linked to three CompIDs and a GovID; history tab shows every event | P08, P06 |

#### T1 — Tests (v1.2; for Appendix V)

| ID | Test | Phase | Automated by |
|---|---|---|---|
| V12-T1-01 | Template validator T01–T15 on all 29 v2.0 workbooks → 29/29 PASS (sheets; identity; headers; header/key hash + contract_json; contract table; bands; base/extension keys; vocabularies; named ranges; DV rows 3–5000 with alert style; function matrix; outline; freeze/AutoFilter; print set-up; protection/no data/RAG CF/Read Me) | P03 | `templates/_validate_templates_v2.py` |
| V12-T1-02 | Negative tests: changed header → T03 fail; removed DV → T10 fail; unhidden column → T12 fail; data row → T15 fail; workbook re-saved by openpyxl → T14 fail (print area lost) | P03 | build session 25-Oct-2026; add to CI |
| V12-T1-03 | Dependent dropdown formula evaluates in LibreOffice: Department "Compliance" → 5 functions; Function "Supervisory Returns" → 5th sub-function "Return validation and sign-off" | P03 | headless LibreOffice recalc (build session) |
| V12-T1-04 | Sample Working Register export check X01–X05 (headers, closed-list values, dependent lists, event trigger, date logic, CompID grammar/uniqueness, sheet set, RAG CF) | P04 | `_validate_templates_v2.py` (sample section) |
| V12-T1-05 | PDF sample: cover + RAG summary + department sections with subtotals; page rendered to PNG and checked legible (no wrapped CompIDs/dates) | P04 | `v12_build_samples.py` + `pdftoppm` (manual visual) |
| V12-T1-06 | Legacy regression: 27 v1.0 workbooks still pass the v1.0 validator with both owner samples (27/27) | P03 | `_validate_templates.py` |
| V12-T1-07 | Legacy owner sheet imports through the map; Column Z rule (LDC-TPL-088); instrument confirmation step; Function completion required before publish | P03 | Appendix E §A.15 scenario "Legacy owner sheet" |
| V12-T1-08 | Event Based row without trigger → LDC-TPL-057; "Other: …" → warning | P03 | §A.15 |
| V12-T1-09 | Function not in Department → LDC-TPL-054 | P03 | §A.15 |
| V12-T1-10 | Per-row date later than instrument last-amended date → LDC-TPL-075 | P03 | §A.15 (note T1_crossfile item 1) |
| V12-T1-11 | Grouped PDF export: cover table Department × RAG, sections with subtotal, export ID footer, ledger event per CompID | P04 | §A.15 |
| V12-T1-12 | Template opens in list view (A–I visible; D3 frozen); outline level 3 shows all columns | P03 | §A.15; manual check in Excel desktop and Excel for the web (OI-E-V12-05) |
| V12-T1-13 | Appendix E tables regenerate byte-identical from `v12_contract.py` | P03 | `v12_appendix_tables.py` diff in CI |

#### T3 — Tests (v1.2; P04 §12 `tests/acceptance/p04/*.feature`)

| Test ID | Scenario | Phase | NN / D |
|---|---|---|---|
| P04-V12-01 | Default list shows nine columns + Next Due, Days to Due, RAG; ≥ 12 rows at 1366×768 | P04 | D-50 |
| P04-V12-02 | Column chooser adds a v2.0 field; shared view reproduces columns/filters/sort/grouping | P04 | D-50 |
| P04-V12-03 | Floor columns cannot be hidden in tenant default (LDC-CMP-213) | P04 | D-50 |
| P04-V12-04 | NL filter shown before it runs; nothing changes until Apply | P04 | NN-47 |
| P04-V12-05 | NL filter never widens ABAC scope | P04 | NN-01, NN-47 |
| P04-V12-06 | Multi-key sort RAG ↓, Days ↑, Risk ↓ | P04 | — |
| P04-V12-07 | Three-level grouping with RAG/status counts; fourth level refused (LDC-CMP-212) | P04 | — |
| P04-V12-08 | Click CompID opens drawer ≤ 800 ms with nine tabs; list position kept | P04 | D-50 |
| P04-V12-09 | Deep link with legacy alias opens canonical CompID | P04 | NN-56 |
| P04-V12-10 | History tab shows per-ID ledger in order, exportable | P04 | NN-57 |
| P04-V12-11 | Star is one click, private, no side effects | P04 | — |
| P04-V12-12 | Responsible user cannot unwatch (LDC-CMP-218) | P04 | D-53 |
| P04-V12-13 | RAG default windows outline (Monthly 3/6/9 d; Quarterly 7/25 d; Immediately 2 d) | P04 | NN-58, D-54 |
| P04-V12-14 | High risk widens windows by 50 % (quarterly due in 10 d = Red) | P04 | D-54 |
| P04-V12-15 | Returned item inside Amber window = Red | P04 | D-54 |
| P04-V12-16 | Event-based awaiting trigger = Blue; not applicable = Grey | P04 | D-54 |
| P04-V12-17 | Tenant cannot narrow RAG floor (LDC-CMP-205); widening shows impact preview | P04 | D-54 |
| P04-V12-18 | Prediction never changes RAG, status, dates or owner | P04 | NN-58 |
| P04-V12-19 | Newly Red item reaches widget, calendar, Inbox and digest ≤ 15 min | P04 | D-54 |
| P04-V12-20 | Ask maker for explanation in 3 clicks; SLA 2 business days | P04 | D-53 |
| P04-V12-21 | Unanswered explanation escalates to manager at 150 % SLA | P04 | D-53 |
| P04-V12-22 | Message edit after 5 minutes refused (LDC-WF-200) | P04 | NN-59 |
| P04-V12-23 | Peer cannot raise Explanation Request (LDC-CMP-206) | P04 | D-53 |
| P04-V12-24 | Acceptance lapse escalates and starts maker clock | P04 | NN-60 |
| P04-V12-25 | Time-in-hand computed from ledger only; delay reason does not change it; named party notified | P04 | NN-60 |
| P04-V12-26 | Owner of record never blank on exit; manual blanking refused (LDC-CMP-211) | P04 | D-53 |
| P04-V12-27 | Accountability report facts-only statement, hash, no AI ranking | P04 | NN-47, NN-60 |
| P04-V12-28 | Export filtered list grouped by department in 4 clicks; rows equal screen | P04 | — |
| P04-V12-29 | Sheet-per-group Excel and grouped PDF with RAG icon + word | P04 | NN-21 |
| P04-V12-30 | Export is a ledger event on each included CompID | P04 | NN-57 |
| P04-V12-31 | Scheduled export drops recipient who lost access (LDC-CMP-214) | P04 | NN-01 |

NN test names added: `NN-56_compid_alias_deep_link`, `NN-57_compid_history_complete`, `NN-58_rag_deterministic_prediction_labelled`, `NN-59_thread_append_only_after_5_min`, `NN-60_time_in_hand_from_ledger_only`, `NN-21_rag_never_colour_alone`, `NN-47_nl_filter_shown_before_run`.
Appendix C release gates: J-27–J-31 click budgets measured per §C.11.2.

#### T4 — Acceptance tests (v1.2; Gherkin in the phase files' §12)

| Test ID | Scenario | Phase | NN |
|---|---|---|---|
| P03-V12-01 | v2.0 columns read by machine key with family extension columns present | P03 | NN-35 |
| P03-V12-02 | Blank instrument reference blocks the row (LDC-TPL-073) | P03 | — |
| P03-V12-03 | Legacy v1.0 sheet routed to map; Confirm instrument; Download as v2.0 | P03 | NN-35 |
| P03-V12-04 | 20+ concurrent imports on one instrument produce disjoint reserved blocks, zero duplicates | P03 | NN-56 |
| P03-V12-05 | Reserved → ASSIGNED on release publication; CompIdAssigned emitted | P03 | NN-56 |
| P03-V12-06 | Rejected job voids reservations; numbers never reused | P03 | NN-56 |
| P03-V12-07 | Re-import with substantive change updates same CompID (version 2.0, Amended, previous actionable kept) | P03 | NN-02 |
| P03-V12-08 | Omitted CompIDs require retire/keep/move decision | P03 | NN-56 |
| P03-V12-09 | Split retires parent with lineage to children | P03 | NN-56 |
| P03-V12-10 | v1.1 dotted ID resolves via alias in deep link and search | P03 | NN-56 |
| P03-V12-11 | Tenant question receives `T<TENANT4>-<INST>-<NNNN>` on overlay approval | P03 | NN-01 |
| P03-V12-12 | CompID History shows import, amendment, overlay and export events | P03 | NN-57 |
| P05-V12-01 | Studio fills all Author keys; deterministic instrument fields; user/system groups not generated | P05 | NN-04 |
| P05-V12-02 | Studio reserves CompIDs at DRAFT_READY and assigns on publication | P05 | NN-56 |
| P05-V12-03 | Amendment run updates existing CompID with regulator's date; no new CompID | P05 | NN-56 |
| P05-V12-04 | Near-duplicate NEW row becomes proposed update | P05 | — |
| P05-V12-05 | Client-admin run creates tenant CompIDs visible only to the tenant | P05 | NN-01 |
| P23-V12-01 | Super admin binds four CompIDs to one item with citation built from them | P23 | — |
| P23-V12-02 | Section weights ≠ 100 block submission | P23 | NN-22 |
| P23-V12-03 | Branching preview for sample entity hides deposit questions | P23 | — |
| P23-V12-04 | Maker cannot approve own set version | P23 | NN-05 |
| P23-V12-05 | Retired bound CompID flags set; publish blocked until resolved | P23 | NN-56 |
| P23-V12-06 | Placeholder resolves to CompIDs and becomes alias | P23 | NN-56 |
| P23-V12-07 | Baseline pre-fill by CompID never marks Compliant or fills Date of Compliance | P23 | NN-57 |
| P23-V12-08 | All outputs labelled "Health Check Score" | P23 | — |

NN test names added: `NN-56_compid_never_reused_after_void`, `NN-56_alias_resolves_and_never_deleted`, `NN-56_split_merge_lineage_append_only`, `NN-57_history_tab_by_compid`, `NN-35_v2_contract_immutable_within_major`, `NN-56_studio_cancelled_run_voids_reservations`, `NN-56_amendment_keeps_compid`, `NN-57_ai_row_edit_in_compid_history`, `NN-50_risk_gov_links_are_suggestions`.

#### T5 — Tests (v1.2)

| Test ID | Scenario | Phase | NN / D |
|---|---|---|---|
| P00-V12-01 | CompIDs reserved in S. No. order at preview; rejected rows VOID; next added row takes the next number | P00 | NN-56, D-52 |
| P00-V12-02 | 20 parallel allocations with 5 rollbacks: no duplicate, no reuse | P00 | NN-56 |
| P00-V12-03 | Re-cited provision keeps CompID; succeeding obligation records CONTINUED_AS; History follows lineage | P00 | NN-56, NN-57 |
| P00-V12-04 | Assign, star, discuss, evidence, approve, export → all six events in `/v1/history/{CompID}` with CompID and instance ref | P00 | NN-57 |
| P00-V12-05 | Tenant code locks after first tenant ID (LDC-CORE-125) | P00, P01 | NN-56 |
| P00-V12-06 | Hidden ID returns the same LDC-CORE-031 as a missing one | P00 | D-51 |
| NN-56_bizid_immutable_never_reused | Property test over 10,000 allocate/rollback/retire/void sequences | P00 | NN-56 |
| NN-56_alias_never_issued · NN-56_lineage_acyclic · NN-56_tenant_code_locked | Registry invariants | P00 | NN-56 |
| NN-57_every_event_has_bizid | Walks the action catalogue; any ledger row of an ID-bearing aggregate without business_ids fails CI | P00 | NN-57 |
| NN-57_history_tab_complete | Every §B.12.6 category appears for a seeded CompID, RiskID and GovID | P00 | NN-57 |
| bizid_parser_roundtrip · bizid_alloc_sheet_order · bizid_recited_keeps_compid | Parser, ordering, re-citation | P00 | D-52 |
| P01-V12-01..07 | CIN discovery with provenance; NBFC from RBI register snapshot; slow provider; struck-off block; partner request needs client confirmation; director change at re-verification; practitioner bulk | P01 | D-56 |
| P18-V12-01 | Hedged provider call without double billing | P18 | D-56 |
| P18-V12-02 | Register snapshot with > 5 % diff is HELD; onboarding uses previous snapshot | P18 | D-56 |
| P18-V12-03 | `GET /v1/compliances/{compId}/instances/{period}` returns biz_id, instance_ref, status, next due, RAG | P18 | D-51 |
| P18-V12-04 | Alias request returns Content-Location of canonical ID | P18 | NN-56 |
| P18-V12-05 | > 50 not-found lookups/min → LDC-INT-163 + SIEM alert | P18 | — |
| P18-V12-06 | MCP `draft_conversation_message` creates a draft only | P18 | NN-52, NN-59 |
| NN-52_mcp_parity (extended) | New ID tools return nothing a user cannot read via REST | P18 | NN-52 |
| P08-V12-01 | Re-classification keeps RiskID; History shows it | P08 | NN-56 |
| P08-V12-02 | Template import adds an assessment row, never rewrites history | P08 | D-57 |
| P08-V12-03 | Overdue review → Red; CRO Explanation Request with SLA; Accountability shows holder | P08 | NN-58–NN-60 |
| P08-V12-04 | Export grouped by Risk Category then Department, one sheet per group + Summary heat map; EXPORTED history entries | P08 | NN-57 |
| P09-V12-01 | Approved ICAAP keeps merged RiskID as approved; next ICAAP shows movement | P09 | NN-56 |
| P06-V12-01 | Meeting gets GOV-…-MTG ID, EVIDENCES link; signed minutes offer one-click evidence hand-off (no auto-submit) | P06 | NN-14 |
| P06-V12-02 | Event-based MGT-14 requirement Blue → dated on special resolution → Red 2 days before due | P06 | D-54 |
| P06-V12-03 | Notice window closing → Red with "issue by" date | P06 | D-54 |
| P06-V12-04 | History load: 40 resolutions get RES GovIDs; client numbers stored as TRACKER aliases | P06 | NN-56 |
| D-V12-01 | SoD-27 to SoD-32 enforced at action time (block) | App D | — |
| D-V12-02 | Explanation Request allowed only down the resolved hierarchy (§D.19.3); peer refused | App D | D-53 |
| D-V12-03 | Personal stars invisible to admins; auditors see counts only | App D | — |
