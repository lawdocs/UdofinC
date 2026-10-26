# F1 integration review log — LawDocs Build Prompt Pack v1.0

Reviewer: F1 (integration). Date: 25 October 2026. Scope owned: `phases/P00…P11`, `appendices/A, B, D, K, R`. Governing files read: `_research/00_Agent_Brief_Common.md`, `00_Authoring_Conventions.md`, `00_Cross_File_Resolutions.md`, `01_MASTER_PROMPT.md` (§4 incl. amended NN-06, §5, §18), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.

## 1. Kill switches — one registry (P03), canonical `cfg` events (R-A-09)

| File | Section | Change |
|---|---|---|
| P00 | §2 (scope), §2 out-of-scope table, FR-P00-49/50/51, §5.6, §7.2, §7.3, §7.4, §7.5, §9 | `core.feature_flags` / `core.kill_switches` / `cfg.settings_registry` replaced by P03-owned heads `cfg.setting_definitions`, `cfg.setting_values`, `cfg.flags`, `cfg.kill_switches`, `cfg.kill_switch_events`; events `core.FeatureFlagChanged` / `core.KillSwitchChanged` replaced by `cfg.FlagChanged`, `cfg.KillSwitchEngaged.v1`, `cfg.KillSwitchReleased.v1`; API gains `:request-release`; probe job renamed `KillSwitchProbeJob`; §5.6 pointer to A.17; setting `ai.kill_switch.propagation_slo_seconds` → `cfg.kill_switch.propagation_seconds` (R §R.9.5) |
| P03 | §2, FR-P03-84, §5.5, §7.4 | Single-registry statement; scopes listed (A.17); only `cfg.KillSwitch*` events platform-wide; aliases retired |
| P09 | FR-P09-45, §7.2, §7.3, §7.4, §7.5, @P09-AT-08 | Levels mapped to `cfg.kill_switches` scopes; `agt.kill_switches` is a view; release by second person; emits/consumes `cfg.KillSwitchEngaged/Released`; `agt.KillSwitch*` retired; agent-specific `agt.killswitch.*` settings kept; test asserts the `cfg` event |
| D | §D.7 | `core.kill_switch.release` → `cfg.kill_switch.release` (`LD-CFG-050`); `core.flag.enable_gated` → `cfg.flag.enable_gated` |
| B | R-B-01, §B.7 | Marked aligned |

## 2. Machines described in two phases — pointers and wording (Appendix A governs)

| File | Section | Change |
|---|---|---|
| P01 | §5.5 | Pointer A.5 (R-A-03) |
| P01 | §5.7 | Rewritten to canonical A.8 states (CLAIMED, IDENTITY_VERIFIED, EVIDENCE_VERIFIED, WAITING, CANCELLED_BY_OWNER, OBJECTED, REJECTED, RELEASED, EXPIRED); pointer R-A-04 |
| P01 | §5.9 | Pointer A.2 (R-A-02); intermediate states IDENTITY_VERIFIED, KYB_CONFIRMED, TERMS_ACCEPTED added |
| P02 | §5.1, §5.2, §7.3 | Pointers A.9 (R-A-05), A.11 (R-A-06), A.56 (R-A-21); DECLINED/WITHDRAWN row; standing-authorisation path; delivery grants = `iam.grants` + `sdc.delivery_grants` extension |
| P03 | §5.4, §5.5, §5.7 | Pointers A.15 (R-A-07/08), A.17 (R-A-09), A.1 (R-A-01); task machine stated |
| P04 | §5.3 | Pointer A.21 (R-A-10) with state-name mapping (`source_kind = DMS_FOLDER`) |
| P04 | §5.4, FR-P04-60/61, §7.2, §9 | Pointer A.8 (R-A-04); EVIDENCE_VERIFIED added; reviewer corrected to `OPS_ONBOARDING` maker → `PLT_DPO`/`OPS_DELIVERY_LEAD` checker (was `PLT_GRIEVANCE_OFFICER` queue); `dms.nominees` marked projection; duplicate `dms.nominee.waiting_days`/`access_days` replaced by P01 `iam.nominee.release_waiting_days`/`iam.nominee.access_days` |
| P06 | §5.3 | Pointer A.28 (R-A-12); canonical names (REQUESTED, ACCEPTED, REJECTED added) |
| P07 | FR-P07-05, §5.1, §5.2, §5.4, §7.2 | One front door per Company tenant (A.29, R-A-13); A.30/R-A-14 pointer; approval step as projection of `wf` (A.11, R-A-06); `clm.approval_step` gains `apr_id` |
| P08 | §5.2 | Pointer A.31–A.34 |
| P09 | §5.2 | Pointer A.28 (R-A-12); `RETURNED_TO_USER` → `RETURNED`; ACCEPTED, RESUBMITTED, CLOSED added |
| P11 | §5.6 | Rewritten to A.21 (`xpt.import_jobs`, `source_kind = LIT_REGISTER`); checker approval now before COMMITTING (contradiction removed) |
| P11 | §5.7 | Pointer A.43 (R-A-15); APPROVED step (`ORG_CLO`/step-up) and WITHDRAWN wording added |
| A | A.15, A.31, A.65, A.66 | R-A-08 status updated; G-ASSIST guard for assisted signing; A.65 events marked added; F1 integration status note in A.66 |

## 3. Tasks

P03 §2, §5.4, §7.2 (`wf.tasks` table with columns and indexes), §7.3 (`/v1/wf/tasks` API), §7.4 (`wf.TaskCreated`, `wf.TaskAssigned`, `wf.TaskCompleted`). B §B.2.6 row expanded; B §B.4.2 events added. K §K.3.5 `tasks.csv`; K §K.11 `task`.

## 4. Events missing from §7.4

P09 §7.4 `ai.RunReceived`, `ai.PlanApproved`; P11 §7.4 `lit.MatterSettled`, `lit.OrderFetched`; P04 §7.4 `dms.DocumentDeposited`; P03 §7.4 `wf.TaskAssigned` (+ Created/Completed). Script check of §5 vs §7.4 for P00–P11: no gaps remain.

## 5. Error codes

| File | Section | Change |
|---|---|---|
| P03 | §5.1 | Validator order now names each code (001 type/schema, 004 bounds, 005 plan limit, 002 child direction, 006 parent lock, 003 contrast) — matches tests |
| P03 | §13 | Full enumeration: `LD-CFG-001…081` (24 codes), `LD-RUL-001…015`, `LD-WF-100…131` (items and tasks) |
| P08 | FR-P08-57, §13 | `LD-SGN-041`, `LD-SGN-042` |
| B | §B.5.3, §B.5.4 | CFG/RUL/WF/SGN entries rewritten to match; † note removed; E-06 closed; E-09 narrowed to XPT/ENG |

Pack-wide grep of `LD-[A-Z]+-[0-9]{3}` against §B.5.3: every referenced code is defined; remaining non-matches are range endpoints (`001`/`099`) and business references (`LD-AGR-2026…`).

## 6. Appendix R

| Section | Change |
|---|---|
| §R.9.3 | `kyc.flag.ovse_offline_verification` → `kyc.ovse.qr.enabled` + `kyc.ovse.avc.enabled`; `kyc.digilocker.retain_copy` → `kyc.digilocker.retain_copy.enabled` default false (X-11) |
| §R.9.4 | `org.master_data.change_policy` without `owner_only` (`maker_checker` / `maker_checker_plus_owner`) |
| §R.9.21/§R.9.22 | `gov.mode`, `hr.mode` retired; §R.9.33 adds `int.eco.ldc.sor_mode.governance` / `.hrms` (`LOCAL`/`LDC`) |
| §R.9.15 | `sgn.methods` → `sgn.methods.allowed` (P08 definition) |
| §R.9.35 | `web.crawl.ai_search_bots_allowed` per P21 (bool true; checker `PLT_SECURITY_OFFICER`); added `web.crawl.ai_training_bots_allowed`, `web.crawl.google_extended_allowed`; `web.testimonials.photos` → `web.testimonials.photos_enabled` |
| §R.9.36 | `hlp.video.captions_default_on` per P21 (PLT→USR); `hlp.tours.auto_start_first_use` → `auto_start_first_run` |
| §R.9.38 | `mob.nav.tab_order` (USER) and `mob.bottom_bar.items` (TENANT, exactly 2 Company middle slots, `[Contracts, Matters]`) per P22 FR-P22-03 and P22 §9 |
| §R.14 | Removed every row duplicating §R.9 (15 keys) and stale aliases (`iam.login.methods_enabled`, `ai.kill_switch.propagation_slo_seconds`, `dms.nominee.waiting_days`, `dms.nominee.access_days`); `iam.nominee.waiting_days` → `release_waiting_days`; added four `sgn.accessibility.*` keys; intro text updated; section counts recomputed |

Script check: 0 duplicate key rows in Appendix R; every settings key in P00–P11 §9 exists in Appendix R.

## 7. Appendix K

§K.0 reconciliation note cites X-07 (`00 Start Here/`, `owner_readable` confirmed; profiles `ld_professional_v1`, `ld_consumer_help_v1` already present). §K.1 root lists `01 … 12`. §K.3.1 adds `06 Policies and Registers/Contract Templates and Playbooks/` and company `12 Tax/` (Income Tax, GST per GSTIN, TDS and TCS, Professional Tax, Notices/Assessments/Appeals, tax register); `09 Services and Engagements/Tax and Filings/` limited to working papers. §K.3.2 `09 Tax/Tax Year <YYYY-YY>/` with legacy `AY` alias. §K.10.2 synonyms updated. §K.11 rows added for `task`, `share`, `legal_hold`, `nominee`, `signatory_authority`, `guardianship`, `signing_assistance`, `ai_qrg_review`, `ai_memory_item`, `ai_run_ledger_extract`, `hr_posh_case` (sealed, IC-only archive), `review`, `aca_certificate`, `testimonial`, `a11y_issue`, `mob_device`, `mob_push_preferences`, `tax_notice`, `tenant_template`, `clause`, `playbook`, `intake_form`. OI-K-01 closed; OI-K-06 updated. §K.10.4 NN-13 reference corrected to G-HUMAN/NN-12.

## 8. Appendix D

§D.2.1 `PLT_AUDITOR_RO` strengthened. §D.2.3 `ORG_BOARD_OBSERVER`, `ORG_AUDITOR_RO` (`auditor_type`, s.143(1)) strengthened; new `ORG_HR_ADMIN`, `ORG_HR_MAKER`, `ORG_PAYROLL_MAKER`, `ORG_PAYROLL_CHECKER`, `ORG_POSH_IC_PRESIDING`, `ORG_POSH_IC_MEMBER` with P13 label mapping (closes OI-P13-08 on the D side). New §D.2.6 partners and developers (`PRT_ADMIN`, `PRT_OPERATOR`, `DEV_ACCOUNT`); agents renumbered §D.2.7. New §D.5.1 HRMS/payroll/POSH matrix, §D.5.2 board and audit access, §D.6.5 partner/developer matrix. §D.7 five new actions. §D.9 SoD-31…36. §D.10 `AUDITOR` row extended, new `BOARD_OBSERVER` and `POSH_IC_EXTERNAL` grant types, storage note aligned to R-A-05. §D.13 four review rows.

## 9. P08 — assisted eSign, NN-06 as amended, Appendix F §9

Header binding appendices add A, B, U and the X-02 note. FR-P08-02/03: `asp_mode` (`VENDOR` / `LAWDOCS`) per NN-06 as amended (X-15). FR-P08-05: `LD-SGN-009`, X-16. FR-P08-08: Appendix F §9 governs, R5 flags superseded (agreements for sale, conveyances, affidavits, vakalatnamas/pleadings, adoption). FR-P08-53: hosted hand-off (X-05) with `LD-INT-060/061/062`. New §4Q FR-P08-56 (accessible signer journey) and FR-P08-57 (assisted signing with helper, interpreter, witness; assistance consent and helper declaration; signer must act personally; wet-ink signature-by-mark fallback; no health data stored). SCR-P08-17; `sgn.signing_assistance` table; `participants.role` adds HELPER/INTERPRETER; `providers.a11y_conformance`; event `SigningAssistanceRecorded`; four `sgn.accessibility.*` settings; `LD-SGN-041/042`; Gherkin @P08-AT-26 (disability, helper + witness, consent recorded), @P08-AT-27 (cannot act → wet ink), @P08-AT-28 (agreement for sale via Appendix F), @P08-AT-29 (hosted hand-off).

## 10. Environment names (P00)

§1 outcome table, §2 scope, FR-P00-14 catalogue (adds `test`, `pre-prod`; removes `uat`; `mig` is a zone), FR-P00-16 accounts (`ld-test`, `ld-preprod`), §13 checklist. P23 FR-P23-07 cited as governing.

## 11. General sweep (P00–P11, A, B, D, K, R)

- All twelve phases have §1–§13 headings.
- Binding-appendices header lines: A and B added to P00, P01, P02, P04, P05, P06, P07, P09, P10, P11 (P03, P08 edited individually); every letter cited exists.
- No reference to a non-existent appendix or phase (only external LDC "Appendix AA" and LDC "P26", both labelled as LDC).
- NN spot-check: P02 FR-P02-27 NN-29 → NN-18; P02 §11 NN-13 → NN-18, NN-43; K §K.10.4 NN-13 → G-HUMAN/NN-12. Others consistent.
- Table column-count check: no malformed rows. P00 crawler setting now marked P21-owned (P21 definition).
- P04 DigiLocker retained-copy key clarified against the P01 key.
