# Review R2 — P03, P04, P05, Appendices E and F, part2_prompts, templates (25 October 2026)

## Fixes made

| File | Fix |
|---|---|
| `templates/_build/family_vocab.py` + all 24 workbooks (rebuilt) | Removed `[VERIFY]` from 10 dropdown values (a marker inside a list value would block every row selecting it, App E §E.4.7): COOP-CCS, IRDAI-INS, IRDAI-INT, RBI-ARC, SEBI-AIF (2), SEBI-INT, SEBI-MF (2), LAB-POSH. SEBI-MF instruments and worked example moved from MF Regulations 1996 to MF Regulations 2026 (notified 14 Jan 2026, in force 1 Apr 2026). RBI-SCB supervisory-returns entry now cites RBI/DoS/2026-27/415 and /424 (X-12). |
| `templates/_build/build_templates.py` | `_Template_Info` file-naming instruction aligned with the master command (`<Family code> - <Instrument> <Year>.xlsx`); base-layout text now names the Appointed Actuary sample (X-38). |
| `templates/_validate_templates.py` | Re-run with both owner samples: 24/24 PASS (T01–T11); `_validation_report.md` refreshed. Checked: rows 1–2 identical to the owner sample, named ranges resolve, list validations on C, D, H, M, O, P, R (rows 3–2000), `_Template_Info` present and protected, Sheet1 empty below row 2, no `[VERIFY]` in any `Rough` list. |
| `templates/_build/appendix_tables.py` | Department codes switched to master X-10 codes (GOV, FIN, LEG … plus the 12 added codes); every family department name now resolves through an explicit alias map (KeyError if a name is missing from Appendix U §U.9.0). Attestation setting key aligned. |
| `templates/_build/family_commands.py`, new `final_instruments.py`; regenerated `part2_prompts/01–24` | Instrument inventories (§4 of each family command) were concatenations of two lists with near-duplicates (e.g., LODR listed twice, MF Regulations 1996 twice); replaced with curated, de-duplicated lists. Added DoS supervisory-returns directions for UCB (/442) and ARC (/469) [VERIFY numbers]. |
| `part2_prompts/00_Part2_Master_Command.md` | Column C/D headers written exactly as row 2 ("General Applicability(Layer)"); explicit rule that every [VERIFY] must be resolved before upload (importer keeps such rows as draft); prompt-template location corrected to `ai.prompt_templates` `QUESTION_GEN/question_authoring_v1`. Self-containment checked: usable in a fresh chat with the template and source PDFs attached plus the family command. |
| `part2_prompts/99_QA_Checklist…` | Added D6 ([VERIFY] resolved before publication). |
| `appendices/E_…` | §E.13.2 department codes replaced with X-10 codes; §E.15 vocabularies re-synced from the build; frequency table points to `cmp.ongoing.attestation_frequency` (P04 key); new paragraph on REGISTER/WORKSPACE exports (A–AD only; period and instance ref in `_LDC_System`, X-28); prompt-template location fixed; open items OI-P03-E90/E91 added. |
| `phases/P03_…` | Frequency, compliance-type and risk codes aligned with Appendix E §E.13 (EVENT, CONTINUOUS, DAILY, EVERY_nY; POLICY, RETURN_REPORT, INTERNAL, SUGGESTIVE; no CRITICAL risk, NN-35); department code per X-10; V-05 required columns aligned with §E.3 (B, P, S required; N optional); V-04 user columns dropped with warning LDC-TPL-013 (was "block") and its Gherkin updated; V-11 and column D delimiter per X-08; OI-P03-02 resolved; checker review "Review next" with bulk only for Editorial/NOCHANGE rows (NN-46); `_Template_Info` description aligned with §E.5. |
| `phases/P04_…` | Frequency codes EVENT/CONTINUOUS and a DAILY row (App E precedence); mapping table workflow state → canonical status (master §6.3, X-11); register export no longer appends columns after AD (NN-35, LDC-TPL-005) — period/instance ref go to `_LDC_System`; CompID example corrected to `RBI-NBFC.GOV25.0012`; bulk approval removed except `bulk_approvable` items (NN-46) incl. Work Inbox bulk actions and setting `cmp.review.bulk_approve_enabled` (OFF); calendar two-way sync never changes LDC dates (X-24); work digest default 08:30 (NN-27). |
| `phases/P05_…` | AI routing per X-03/NN-41 (tenant runs only via Bedrock India, no non-India failover); ecosystem event published by `int` as `in.infrabyx.grc.ObligationPublished.v1` (X-01); regulatory digest default 20:30 IST (NN-27); seed prompt profile linked to `part2_prompts/00–24` and the QA checklist. |
| `appendices/U_…`, `_contrib/S1_settings.md`, `_contrib/S2_settings.md`, `_compiled_settings.md` | Removed duplicate key `cmp.continuous.attest_frequency` (kept P04's `cmp.ongoing.attestation_frequency`); updated `cmp.review.bulk_approve_enabled`, `chg.updates.digest_time` (20:30 IST), `notify.digest.default` (08:30). |

## Checked, no change needed

Appendix F structure, URLs and table syntax; Markdown table integrity across all R2 files (scripted lint: no column-count mismatches, no placeholders); IFSCA-GEN vocabulary byte-identical to the owner's sample (validator T10); every template department name present in Appendix U §U.9.0.

## Unresolved (for the lead)

1. Composite insurer licensing after the 2025 Amendment Act, ARC NOF threshold for additional activities and State concurrent-audit thresholds remain to be verified (OI-P03-E90).
2. SEBI MF Regulations 2026 regulation numbers are unverified; the MF worked example cites "[VERIFY regulation number]".
3. `_LDC_System` export sheet (X-28) is now relied on by both P03 exports and the P04 REGISTER export — owner confirmation (02 §4 item 7) has become more important.
4. Appendix F: roughly half of the non-RBI source URLs still carry [VERIFY] and should be test-fetched in P05 sprint 1 (unchanged).
