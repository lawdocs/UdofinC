# G4 registry review log — LawDocs Build Prompt Pack v1.0

Reviewer: G4 (registry maintainer). Date: 25 October 2026. Scope owned: `appendices/A, B, C, D, K, R, V, W, Z`. Governing text read: `01_MASTER_PROMPT.md` §4 (NN-01…NN-50), §5 (architecture, module codes), §18 (precedence, X-01…X-30). All checks were run by script over the current files (phases, appendices, master `01`, decision log `02`, condensed editions, content deck); phases were being edited in parallel, so the final counts are those of the last run.

| ID | File | Change |
|---|---|---|
| G4-01 | B §B.5.3 | `AGT`, `CVL`, `GOV`, `HR`, `HLP`, `MSG`, `SAV`, `TAX`, `ACA` split into their own entries with owning-phase source (P09 §7.6, P18 §12, P13 §13, P21 §7.3, P07 §13, P17 §12, P14 §12, P16 §12) and declared range; wording aligned to the phase text (GOV-001/003/008/010/013/014, HR-008, AGT-007/015 cross-references). Every code was already enumerated; none needed a registry-review definition |
| G4-02 | B §B.5.2 | `WEB`/`HLP` range cell repaired (module labels on each range) |
| G4-03 | B §B.5.4 | E-10 added: error help-key form `hlp.<module>.err_<nnn>` canonical; P11, P12, P13 use the dotted form (hand-back). E-11 added: script result — 570 codes in 39 namespaces; every `LD-<MODULE>-<NNN>` referenced anywhere is enumerated; the only unmatched strings are range endpoints |
| G4-04 | B §B.7 | Open items OI-B-01…04 marked as registered in Appendix W §W.4 |
| G4-05 | R intro | Precedence sentence corrected to master §18/X-11 (owning phase wins; R corrected at next sync); counts updated (§R.14 609 keys; §R.9 586 rows incl. 2 retired; 1,193 active keys; duplicate-key check: none) |
| G4-06 | R §R.9.31 | Added P18 kill switches `sdc.breakglass.enabled`, `sdc.email.bridge.global_enabled`, `sdc.delivery.agent_runs.global_enabled` (P18 §9 names them without table values; values set consistent with @P18-AT-29 and the platform kill-switch rows); note that `sdc.grant.max_days` is capped by P18 `sdc.grants.max_months.*` |
| G4-07 | R §R.9.32 | Added `cvl.reveal.enabled`; `cvl.enabled` changed-by aligned to P18 (maker + second client admin); retired `cvl.reveal.client_approval` → alias of `cvl.per_reveal_approval.default` and `cvl.reveal.max_minutes` → alias of `cvl.reveal_seconds` (contradicted P18 and Appendix A §A.55) |
| G4-08 | R §R.9.32A (new) | `wks.m365.enabled`, `wks.google.enabled`, `wks.residency.allow_regulated_on_google` copied from the P18 §9 table (tier, type, default, changed-by, MC) |
| G4-09 | R §R.9.33, §R.14 intro | `int.kill.<adapter>` row aligned to FR-P19-81 and P11/P12 §9 (`PLT_SUPER_ADMIN` engages, `PLT_SECURITY_OFFICER` checks re-enable, tenant admin may kill own connectors; court/TM adapters start disabled). `int.connectors.kill_switch_key` recorded as a column of `int.connectors` (P19 §7.2), not a setting, so not registered as a key; §R.14 exclusion list no longer wrongly treats `wks` as a host prefix |
| G4-10 | R §R.14 `core` | Added `core.migration.ai_assist.enabled` (new in P00 §9 during this review); heading count 15 → 16 |
| G4-11 | R §R.9.7 | Registered `wf.sod.self_sign_threshold_inr` (read by Appendix D SoD-14; was unregistered, NN-29); P02 to confirm |
| G4-12 | R §R.15 | OI-R-08 added (naming normalisation: `wks.*`, P18 kill-switch names, P11/P12 column citation) |
| G4-13 | V §V.8, §V.8.9 | Rows P08-AT-26…29 added; §V.8 heading 578 → 582; P08 sub-heading 25 → 29 |
| G4-14 | V §V.2, §V.3, §V.1, §V.9 G-06 | NN matrix updated: NN-03 3 → 4 (P08·26; status OK, APPV·01–02 retained), NN-06 6 → 7 (P08·29), NN-07 12 → 14 (P08·27, P08·28), NN-28 12 → 13 (P08·26; 12 phases); untagged scenarios 195 of 582; suite count 582 |
| G4-15 | V §V.8.16, §V.5 U-04 step 7 | P15-AT-14 title made verbatim with P15; UAT step corrected to the phase scenario (District Commission by consideration paid, not State Commission by claim value) |
| G4-16 | W §W.2 | Census re-run by script over phases, appendices (except W), content deck, `01`, `02`; per-file table and totals regenerated; method and domain-table caption state that V-item mapping is as at compilation |
| G4-17 | W §W.4 | Added OI-B-01 (merged with OI-P04-08), OI-B-02 (merged with OI-I-12 row), OI-B-03 and OI-R-08 (§W.4.6), OI-B-04 + OI-Y-11 (new §W.4.1 row), OI-Y-09 and OI-Y-10 (merged into the Y-items row); scope 338 → 346 IDs; script: every OI ID referenced in the pack is in §W.4 |
| G4-18 | W §W.8 | Change-log row v1.0.2 |
| G4-19 | C §C.15 | SCR-P08-17 "Signing assistance" added (P08 §6); P08 count 16 → 17; total 514 → 515; intro now names the three §C.16 R-8 proposed IDs (SCR-P03-33…35) as the only unregistered references |
| G4-20 | C §C.16 R-3, R-10 | R-10 garbled text repaired (same key listed twice) and both marked Done (Appendix R now has one key per concept; R-3 row corrected) |
| G4-21 | Z §Z.2.1, §Z.5, §Z.1.1, §Z.1.4, §Z.8 | TM-002 and TM-003 COVERED (`01`, `02` and Word editions exist); TM counts 340/1/57, totals 510 COVERED / 10 PARTIAL / 61 CBD / 0 MISSING; FR citation re-check by script: 737 distinct FR IDs, none broken; Z.8 item 5 follow-ups marked closed where done |
| G4-22 | A header, §A.0.1 | Wrong precedence reference "X-25" replaced by master §18; scope line added — 63 numbered machine sections A.1–A.63 (matches master §6.3 "63 machines"); §A.64–§A.66 are not machines |
| G4-23 | A §A.18, §A.21 | Broken cross-references fixed: mobile upload → A.61 (was A.60); P21 DOCX import → A.60 (was A.62) |
| G4-24 | D §D.7 | `dms.bulk_delete.threshold` → registered key `dms.delete.bulk_threshold` (P04 §9); `cvl.enable`/`cvl.reveal` checker aligned to P18 |

**Hand-back to phase owners (not edited):** P11/P12/P13 error help-key form (E-10); P18 `wks.*` prefix and kill-switch names, P11/P12 `int.kill.<adapter>` citation (OI-R-08); P02 confirm `wf.sod.self_sign_threshold_inr`; P03 register SCR-P03-33…35 (C §C.16 R-8); P00 completion-report template (Z §Z.8). Word editions predate these edits and need re-rendering.
