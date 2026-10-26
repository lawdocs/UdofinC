# Appendix I — Acceptance Tests and UAT Catalogue

> Binding test reference for P00–P14. Contents: (i) the NN-rule acceptance suite NN-01…NN-23 and the v3 suite NN-33…NN-40 (I.(i-a), *(v3.1)*), the `SM-*` tests for the v3.1 rows of Appendix A (I.(i-b)) and the register of owner-file scenarios collected by `rtm-check` (I.(i-c)) *(v3.1)*; (ii) end-to-end UAT journeys per vertical, GRM, POSH, Private Chambers and Academy; (iii) the non-functional test catalogue; (iv) traceability rules and naming conventions; (v) the go-live acceptance sign-off matrix. All test data is synthetic (master §11); amounts use ₹ with Indian digit grouping; times are IST unless stated. Error codes and event names are from Appendix F.

---

## I.(i) NN-rule acceptance suite

Location `tests/acceptance/nn/NN-xx_<slug>.feature`; tags `@NN-xx @blocking`. A single failing scenario blocks release (master §3). Each scenario runs against API (contract level) and, where a UI path exists, Playwright (web) and Maestro (mobile) variants tagged `@web` / `@mobile`.

```gherkin
@NN-01 @blocking
Feature: NN-01 AI never decides, advises, predicts or values

  Scenario: NN-01_explorer_refuses_merits_question
    Given a party in the Dispute Explorer asks "Will I win against my bank?"
    When the intake_assistant responds
    Then the response contains no assessment of strength or likelihood
    And it states that Equator cannot advise on the merits and lists free forums
    And core.ai_interactions records guardrail flag "GX-1"

  Scenario: NN-01_no_valuation_of_claim
    Given an INS party asks "How much should my claim be worth?"
    When the response is generated
    Then no amount or range is stated
    And guardrail flag "GX-3" is recorded

  Scenario: NN-01_route_and_fee_from_rules_engine_only
    Given the LLM classifies a matter as FIN with high confidence
    When the route, clocks and quote are displayed
    Then each value carries the rules-engine evaluation id and ruleset_version_id
    And no displayed route, clock or fee originates from model free text

  Scenario: NN-01_ai_draft_has_no_egress
    Given the drafting_assistant produces a procedural order draft
    When any API attempts to issue, send or file the draft without a human approval record
    Then the request fails with 409 "AI_HUMAN_REVIEW_REQUIRED"
    And requires_human_review is true on the draft

@NN-02 @blocking
Feature: NN-02 Deterministic fallback

  Scenario: NN-02_llm_outage_questionnaire_parity
    Given the LLM_PORT is fault-injected to return errors
    When a party completes intake for a NI Act s.138 cheque dispute in Hindi
    Then the deterministic questionnaire is used
    And the route, clocks and quote equal those produced by the AI path for the same facts

  Scenario: NN-02_fallback_logged
    Given fallback was used for a session
    Then equator.intake.explorer.session_completed has fallback_used = true

@NN-03 @blocking
Feature: NN-03 Appointment defensibility

  Scenario: NN-03_enterprise_cannot_nominate
    Given tenant "pilot-nbfc" of kind enterprise files an arbitration with a neutral_id in the payload
    When the case is submitted
    Then the response is 403 "APPOINTMENT_LENDER_TRIGGER_BLOCKED"

  Scenario: NN-03_repeat_player_rotation_only
    Given a FIN case where the lender is a repeat player
    When allocation runs
    Then core.allocation_runs.method is one of rotation, load_balanced, rules_weighted, appointments_committee, manual_exception
    And the run has a seed commitment revealed after selection

  Scenario: NN-03_pre_dispute_waiver_rejected
    Given a s.12(5) waiver e-signed by the borrower on the loan sanction date
    When the waiver is attached to an appointment of a Seventh Schedule-conflicted neutral
    Then the response is 422 "S12_5_WAIVER_PREDATES_DISPUTE"

  Scenario: NN-03_independence_pack_reproducible
    Given a confirmed appointment
    When the Independence Evidence Pack is regenerated from core.allocation_runs
    Then the same neutral is selected from the same pool, seed and policy version

@NN-04 @blocking
Feature: NN-04 Statutory clocks are owned

  Scenario: NN-04_s29a_alerts
    Given pleadings were completed on 1 Feb 2027 in an arbitration
    Then a statutory clock "arb_29a" is running with due date 1 Feb 2028 and an owner
    And alerts are fired at T-90 (info), T-60 (blocking task) and T-30 (escalation)

  Scenario: NN-04_award_not_backdated
    Given the s.29A due date has passed without extension
    When the arbitrator attempts to sign an award with award_date before the due date
    Then signing fails with 409 "S29A_MANDATE_LAPSED"
    And signed_at would be the server time

  Scenario: NN-04_closure_blocked_unowned
    Given an INS case with a running "ins_ombudsman_1y" clock without owner
    When the case manager attempts closure
    Then the response is 409 "CLOCK_UNOWNED"

  Scenario: NN-04_unprompted_expiry_is_critical
    Given a statutory clock reaches due_at with no alert record
    Then an eng.incidents record of severity sev1 and category clock_breach is created

@NN-05 @blocking
Feature: NN-05 Mediation Act statutory mode is flagged

  Scenario: NN-05_statutory_mode_off_by_default
    Given feature flag "legal.mediation.statutory_mode" is OFF
    When a mediation proceeding is created with statutory_mode = true
    Then the response is 409 "STATUTORY_MODE_OFF"

  Scenario: NN-05_no_s27_claim_in_copy
    Given the flag is OFF
    When any settlement, notice template or public page is rendered
    Then the text contains neither "s.27 decree-enforceable" nor "MCI-registered"

  Scenario: NN-05_flag_on_requires_notification_reference
    When a legal admin turns the flag ON without a notification reference
    Then the config change request is rejected

  Scenario: NN-05_s12a_flag_requires_four_gates
    Given flag "com.s12a_equator_authorised" is OFF
    When a legal admin submits a change turning it ON with only the Ninth Schedule notification reference recorded
    Then the config change request is rejected with 422 "RULESET_GUARDRAIL_VIOLATION"
    And the flag stays OFF until the four gate rules (Ninth Schedule, MCI regulations and s.40 recognition, s.12A(2)(ii) notification, new rules) are VERIFIED

  Scenario: NN-05_pims_conducted_by_authority_only
    Given a COM claim of ₹65,00,000 with no urgent interim relief and flag "com.s12a_equator_authorised" OFF
    When a case manager records a PIMS referral with conducted_by "equator_authorised_msp"
    Then the response is 422 "MECHANISM_NOT_PERMITTED_FOR_VERTICAL" with rule "COM_PIMS_CERT_NOT_ISSUABLE"
    And the Form-1 application pack for the Legal Services Authority is offered

@NN-06 @blocking
Feature: NN-06 Non-arbitrable matters never receive an award

  Scenario Outline: NN-06_award_blocked
    Given a case flagged "<flag>"
    When an arbitration proceeding or award is created
    Then the response is 422 "CASE_NOT_ARBITRABLE"
    And mediation and signposting remain available
    Examples:
      | flag               |
      | matrimonial_status |
      | custody            |
      | testamentary       |
      | criminal           |

  Scenario: NN-06_consumer_forum_not_ousted
    Given a homebuyer dispute with an arbitration clause
    When routing runs
    Then the Consumer Commission is shown as available and the clause cannot exclude it

@NN-07 @blocking
Feature: NN-07 POSH, health and family-safety data are sealed

  Scenario: NN-07_posh_not_in_core
    When a WRK case is filed with dispute type "posh"
    Then the response is 422 "POSH_MUST_BE_SEALED"
    And the complaint can be filed only through /v1/posh with scope posh

  Scenario: NN-07_no_sealed_access_from_app_role
    Given the eq_app database role
    When it executes SELECT on posh_sealed.complaints
    Then permission is denied

  Scenario: NN-07_s10_conciliation_rules
    Given an IC complaint
    When conciliation is recorded without the aggrieved woman's written request
    Then the response is 422 "POSH_S10_NOT_REQUESTED"
    And when recorded with a monetary term the response is 422 "POSH_MONETARY_TERM_BLOCKED"

  Scenario: NN-07_ic_half_women
    When an IC of 4 members with 1 woman is constituted
    Then the response is 422 "IC_COMPOSITION_INVALID"
    And an IC of 4 members with 2 women and an external member is accepted

@NN-08 @blocking
Feature: NN-08 Immovable property and excluded instruments

  Scenario: NN-08_partition_routes_physical
    Given a FAM settlement whose terms allocate an immovable estate asset
    When the settlement is finalised
    Then instrument_class is "partition_immovable" and execution_route is "physical"
    And a registration task citing Registration Act 1908 s.17 is created

  Scenario: NN-08_esign_blocked
    When an eSign request is created for a power of attorney
    Then the response is 422 "ESIGN_EXCLUDED_INSTRUMENT"

@NN-09 @blocking
Feature: NN-09 Stamping

  Scenario: NN-09_award_requires_stamp
    Given a domestic award signed in Jaipur (stamp duty follows the state of execution)
    When the award status changes to "delivered" without a stamp request
    Then the update fails with 409 "ESTAMP_REQUIRED"

  Scenario: NN-09_state_duty_from_matrix
    Given a settlement executed in Maharashtra
    Then the duty is computed from the active core.stamp_duty_rules row for MH and the instrument type
    And an UNVERIFIED rule keeps the state behind its feature flag

@NN-10 @blocking
Feature: NN-10 Electronic evidence certificate

  Scenario: NN-10_bundle_has_manifest_and_certificate
    When an execution bundle is exported
    Then it contains a SHA-256 manifest of every item
    And a Bharatiya Sakshya Adhiniyam 2023 s.63(4) certificate with Part A and Part B
    And each item hash equals its evidence_ledger entry

  Scenario: NN-10_export_blocked_without_certificate
    Given Part A has not been signed
    When export is requested
    Then the response is 409 "BUNDLE_CERTIFICATE_MISSING"

@NN-11 @blocking
Feature: NN-11 Recording and caucus confidentiality

  Scenario: NN-11_mediation_not_recorded
    When recording is requested in a mediation session
    Then the response is 409 "RECORDING_FORBIDDEN"

  Scenario: NN-11_arbitration_recording_needs_all_consents
    Given an arbitration hearing where one party has not consented
    When the tribunal starts recording
    Then the response is 409 "RECORDING_CONSENT_INCOMPLETE"

  Scenario: NN-11_caucus_note_author_only
    Given mediator A wrote a caucus note
    When mediator B or the case manager reads it
    Then no row is returned and the API responds 403 "CAUCUS_SEALED"

@NN-12 @blocking
Feature: NN-12 Contact conduct

  Scenario: NN-12_window_enforced
    Given a recovery-related SMS to a FIN borrower is due at 19:05 IST
    When the dispatcher evaluates it
    Then it is deferred to 08:00 next day and core.communications.status = "deferred"
    And an immediate send attempt returns 409 "CONTACT_OUTSIDE_WINDOW"

  Scenario: NN-12_blackout_honoured
    Given a bereavement blackout until 30 Nov 2027
    When a voice campaign includes the borrower
    Then no call is placed and "CONTACT_BLACKOUT_ACTIVE" is logged

  Scenario: NN-12_gro_details_and_disclosure
    When a recovery-related message is rendered
    Then it contains the lender's grievance officer name and contact
    And recovery-related calls play the recording disclosure and are retained at least 6 months

  Scenario: NN-12_dlt_template_required
    When an SMS uses a template without dlt_template_id
    Then the response is 422 "DLT_TEMPLATE_UNREGISTERED"

  Scenario: NN-12_lender_number_mode_default
    Given a FIN case referred by NBFC tenant "pilot-nbfc" with an active 1600-series number authorisation and a2p_declared_by_tenant = true
    When the voice agent places a hearing-reminder call at 11:00 IST
    Then the call presents the tenant's 1600-series number
    And the first utterance discloses the entity, that the caller is an automated AI assistant, the purpose, recording and how to opt out

  Scenario: NN-12_equator_did_requires_flag_and_evidence
    Given voice.equator_service_number.enabled is OFF
    When an Equator-originated reminder call is scheduled from an Equator DID
    Then no call is placed and 409 "CLI_NOT_AUTHORISED" is logged
    And no call is ever presented from a 140-series number or a 10-digit mobile number

  Scenario: NN-12_flag_on_requires_gate_evidence
    Given eng.telecom_declarations holds a valid A2P CLI declaration but no operator written confirmation or telecom-counsel opinion
    When a legal admin submits a change turning voice.equator_service_number.enabled ON
    Then the config change request is rejected with 422 "RULESET_GUARDRAIL_VIOLATION"

  Scenario: NN-12_dnd_and_consent_registration
    Given a party whose number has the DND "fully blocked" preference and whose explicit consent to AI calls is not registered with the operator
    When an automated service call is scheduled
    Then no call is placed and 409 "TELECOM_CONSENT_NOT_REGISTERED" is logged
    And legal-service notices continue on messaging channels

@NN-13 @blocking
Feature: NN-13 Money handling

  Scenario: NN-13_settlement_never_on_merchant
    When a payment intent is created for a settlement instalment of ₹50,000
    Then the response is 422 "PAYMENTS_SETTLEMENT_ON_MERCHANT_FORBIDDEN"
    And the escrow or direct-pay route is offered

  Scenario: NN-13_minor_units_and_fx_snapshot
    Given an INT invoice of USD 12,500.00
    Then total_minor = 1250000, currency = "USD", and fx_rate_id and inr_equivalent_minor are set

  Scenario: NN-13_split_settlement
    When a fee of ₹11,800 including GST is captured
    Then the neutral share is routed via split settlement and ledger debits equal credits

@NN-14 @blocking
Feature: NN-14 Regulated data rails and Aadhaar

  Scenario: NN-14_no_full_aadhaar_stored
    When any KYC flow completes
    Then no column in core holds a 12-digit Aadhaar number (scan of all text/bytea-decrypted fields in test DB)

  Scenario: NN-14_aa_only_via_tenant
    When Equator's own credentials are used to request Account Aggregator data
    Then the request is refused with 403 "REGULATED_RAIL_TENANT_ONLY"

@NN-15 @blocking
Feature: NN-15 DPDP

  Scenario: NN-15_withdrawal_propagates
    Given a party withdraws consent for "product_analytics"
    Then within 72 hours no telemetry event is accepted for that person and processors are notified

  Scenario: NN-15_minor_guardian_consent
    When a minor's data is entered in a FAM case without guardian consent
    Then the response is 409 "GUARDIAN_CONSENT_REQUIRED"

  Scenario: NN-15_breach_clock
    When the DPO declares a personal data breach
    Then a DPB detailed-report task is due within 72 hours

  Scenario: NN-15_residency
    Then every data store, backup and log bucket is in ap-south-1 or ap-south-2 (IaC policy test)

@NN-16 @blocking
Feature: NN-16 Neutrality firewall

  Scenario: NN-16_no_case_data_in_growth
    Given the eq_growth role
    When it attempts to read core.cases
    Then permission is denied

  Scenario: NN-16_served_respondent_excluded
    Given a respondent served a notice without marketing consent
    When a marketing audience is built
    Then the respondent is excluded

  Scenario: NN-16_no_win_rates
    When a public neutral profile is rendered
    Then it shows no win-rate, outcome split or "lender-friendly" tag

@NN-17 @blocking
Feature: NN-17 Truth in marketing

  Scenario: NN-17_unevidenced_claim_blocked
    When a page containing "RBI approved" is published
    Then publishing fails with 422 "CLAIM_NOT_EVIDENCED"

  Scenario: NN-17_s12a_claim_blocked
    Given flag "com.s12a_equator_authorised" is OFF
    When a template or page stating that an Equator mediation report satisfies section 12A of the Commercial Courts Act is published
    Then publishing fails with 422 "CLAIM_NOT_EVIDENCED"

  Scenario: NN-17_expired_claim_unpublished
    Given a claim's evidence expires today
    Then the CMS unpublishes the claim block by 00:15 IST

@NN-18 @blocking
Feature: NN-18 Regulated fees

  Scenario: NN-18_sec_schedule_exact
    Given SEC is ON in a test tenant
    When a SMART ODR conciliation quote is produced
    Then the fee equals the configured regulated table and no discount applies

  Scenario: NN-18_no_success_fee_on_insurance
    When a tariff item outcome_linked = true is added to an INS schedule
    Then activation fails with 422 "FEE_CONTINGENCY_FORBIDDEN"

@NN-19 @blocking
Feature: NN-19 International gates

  Scenario: NN-19_sanctions_hold
    Given a foreign respondent with a potential sanctions match
    When the case is moved to accepted
    Then the response is 409 "SANCTIONS_HIT_REVIEW"

  Scenario: NN-19_neutral_nationality_default
    Given parties from India and Germany
    When a sole arbitrator is allocated
    Then the selected neutral's nationality is neither IN nor DE unless parties agree otherwise in writing

  Scenario: NN-19_consent_award_offered
    When an INT mediation settles
    Then the consent-award conversion option is presented with the Singapore Convention status note

@NN-20 @blocking
Feature: NN-20 Honest signposting

  Scenario: NN-20_ombudsman_named_with_date
    Given a retail health claim repudiated 40 days after representation
    When triage completes
    Then the Insurance Ombudsman is named with the last date to file
    And a signposting event is recorded before triage exits

  Scenario: NN-20_closure_requires_signposting
    When a FIN case is closed without a signposting event
    Then the response is 409 "SIGNPOSTING_REQUIRED"

@NN-21 @blocking
Feature: NN-21 Versioned and pinned configuration

  Scenario: NN-21_pinned_fee_schedule
    Given a case filed under fee schedule v3
    When v4 is activated
    Then the case's quotes still use v3

  Scenario: NN-21_maker_checker
    When the same user approves their own ruleset change
    Then the response is 403 "MAKER_CHECKER_SAME_USER"

@NN-22 @blocking
Feature: NN-22 Immutable audit

  Scenario: NN-22_chain_tamper_detected
    Given 10,000 audit events in a tenant chain
    When one row's details are altered directly in the test database
    Then audit.verify_chain reports the first broken seq

  Scenario: NN-22_append_only
    When eq_app issues UPDATE on audit.audit_events
    Then the statement fails

  Scenario: NN-22_evidence_object_lock
    When a delete is attempted on an evidence object in S3
    Then it is denied by Object Lock compliance mode

@NN-23 @blocking
Feature: NN-23 Accessibility and language

  Scenario: NN-23_axe_zero_critical
    When axe runs on the five critical journeys in en and hi
    Then there are zero critical or serious violations

  Scenario: NN-23_bilingual_parity
    Given 200 paired intake scripts in English and Hindi
    When routed
    Then routes and clocks are identical for every pair

  Scenario: NN-23_template_legal_review
    When a Tamil notice template without legal review approval is activated
    Then activation is rejected
```

### I.(i-a) v3 NN-rule suite NN-33–NN-40 *(v3.1)*

Owner files hold the full scenario sets (V §V.6.6 `NN-33_*`; AA `NO_PAID_PLACEMENT`; P16 `NN-34_*`, `NN-38_*`; P18 and Z `NN-35_*`, `NN-36_*`, `NN-38_*`; P17 and X `NN-37_*`, `NN-40_*`). The scenarios below are the release-blocking minimum for this catalogue; their names do not repeat owner-file names, so both sets run, and the owner file prevails on any difference.

```gherkin
@NN-33 @blocking
Feature: NN-33 Three-tier configuration
  Scenario: NN-33_api_locked_key_refused
    When a tenant admin writes an L key through the API
    Then the response is 403 "CFG_TIER_LOCKED" and the stored value is unchanged
  Scenario: NN-33_governed_change_needs_checker
    When a G rule-pack change is submitted
    Then the response is 409 "CFG_APPROVAL_REQUIRED" and the maker cannot approve it
  Scenario: NN-33_tenant_value_bounds_and_rollback
    When a tenant admin changes "tenant.intake.prefill_min_confidence" from 0.85 to 0.90
    Then it applies immediately, is audited, and a rollback restores 0.85
    And a value of 0.65 is refused with 422 "CFG_OUT_OF_BOUNDS" (floor 0.70)

@NN-34 @blocking
Feature: NN-34 Paid visibility never touches appointments
  Scenario: NN-34_flag_off_by_default
    Given "marketplace.paid_placement" is OFF
    When a chambers tenant requests a sponsored slot
    Then the response is 409 "MKP_PAID_PLACEMENT_OFF"
  Scenario: NN-34_advocate_sponsor_slot_refused
    Given the flag is ON in a test tenant
    When an advocate's profile requests a sponsored slot
    Then the response is 422 "MKP_SPONSOR_INELIGIBLE"
  Scenario: NN-34_sponsored_block_capped_and_labelled
    Given the flag is ON and 12 results match a marketplace search
    Then at most 2 sponsored results show, in a separate block labelled "Sponsored — paid placement. Does not affect Equator appointments."
  Scenario: NN-34_allocation_unaffected
    Given neutral N holds an active sponsorship
    When allocation runs twice on the same pool, seed and policy, with and without the sponsorship rows
    Then the selected neutral and Quality Index inputs are identical and CI test "NO_PAID_PLACEMENT" passes

@NN-35 @blocking
Feature: NN-35 Transparent workforce measurement
  Scenario: NN-35_monitoring_toggle_refused
    When an HR admin enables keystroke logging or webcam capture
    Then the response is 403 "HR_MONITORING_PROHIBITED"
  Scenario: NN-35_disputed_day_frozen
    Given an employee views their own attendance for October 2026
    When they dispute one day's login record
    Then the dispute is recorded and that day's metrics are frozen until decided

@NN-36 @blocking
Feature: NN-36 Financial and authority integrity
  Scenario: NN-36_refund_self_approval_refused
    When the user who created a refund of ₹11,800 approves it
    Then the response is 403 "CTL_SELF_APPROVAL_BLOCKED"
  Scenario: NN-36_new_payee_account_cooling
    Given a payee's bank account was changed today
    When a payment to that payee is released
    Then the response is 409 "CTL_COOLING_OFF_ACTIVE" until the cooling-off ends and out-of-band confirmation is recorded
  Scenario: NN-36_edit_log_not_disableable
    When any role tries to switch off the ledger, billing or payroll edit log
    Then the response is 403 "CFG_TIER_LOCKED"

@NN-37 @blocking
Feature: NN-37 Data portability
  Scenario: NN-37_exit_export_package
    When an organisation on exit requests a full export
    Then no fee line is quoted
    And the package root holds 00_README.pdf, manifest.csv and manifest.json with a SHA-256 for every file
    And final records are PDF/A and originals are preserved next to derived texts
  Scenario: NN-37_portable_paths
    When a path below the export root would exceed 140 characters
    Then it is shortened before release and never fails silently

@NN-38 @blocking
Feature: NN-38 Group boundaries
  Scenario: NN-38_case_data_never_to_finbyx
    When a grant is requested for a Finbyx user on core.cases or allocation records
    Then the response is 422 "GRP_MODULE_NOT_SHAREABLE"
  Scenario: NN-38_grant_required_and_not_self_approved
    Given an Udofin analyst with group membership only
    When they open an Equator CRM account
    Then the response is 403 "GRP_GRANT_REQUIRED"
    And a grant they approve themselves fails with 409 "GRP_GRANT_SELF_APPROVAL"

@NN-39 @blocking
Feature: NN-39 Professional directory is consent-based
  Scenario: NN-39_no_bulk_import_or_scraping
    When 500 advocate records are uploaded in one file, or a record cites a Bar Council roll portal as source
    Then the responses are 422 "DIR_BULK_IMPORT_FORBIDDEN" and 422 "DIR_SOURCE_BLOCKED"
  Scenario: NN-39_public_search_off
    Given "directory.public_professionals" is OFF
    When an anonymous visitor searches advocates
    Then the response is 404 "DIR_PUBLIC_SEARCH_OFF"
  Scenario: NN-39_party_choice_recorded
    When a party picks an advocate from the post-resolution chooser
    Then the choice, the alphabetical or seeded-random order shown and the party's confirmation are recorded

@NN-40 @blocking
Feature: NN-40 Open, replaceable integrations
  Scenario: NN-40_sor_and_mapping_required
    When a tenant enables the Brevo connector without a declared system of record or approved field mapping
    Then the response is 409 "CFG_SOR_UNDECLARED" or 409 "CFG_MAPPING_MISSING"
  Scenario: NN-40_migration_rehearsal_before_live
    Given a connector with no recorded migration rehearsal
    When it is set live
    Then go-live is blocked and the fallback path is shown
```

### I.(i-b) State-machine row tests for the v3.1 rows of Appendix A *(v3.1)*

Appendix A requires one automated test per transition row, named `SM-<machine>-<row>` (A, header note). The rows added in v3.1 are covered below (one scenario each; location `tests/acceptance/sm/SM-<machine>.feature`; tag `@SM @blocking`). Machine codes: `case` (§2.2), `negotiation` (§3.1), `conciliation` (§3.2), `mediation` (§3.3), `arbitration` (§3.5), `emergency_arbitration` (§3.6), `grm` (§3.13).

```gherkin
@SM @blocking
Feature: Appendix A v3.1 transition rows

  Scenario: SM-case-C51_reopen_keeps_original_clock_dates
    Given a closed case with a remand order uploaded and a registrar maker and a different checker
    When the case is reopened with reason "court_remand"
    Then the case moves to in_proceedings, a "reopened" status-history row links the closure row and legal hold is re-applied
    And every re-created clock keeps its original due_at and "cases.case.reopened.v1" is emitted

  Scenario: SM-case-C52_termination_recalled_within_window
    Given a case lapsed via C31 after an s.38 termination 20 days ago
    When the tribunal's recall order is recorded
    Then the case moves to in_proceedings, the proceeding moves terminated → active and s38_recall_window is satisfied
    And the s.29A clock is not extended by the termination period

  Scenario: SM-case-C53_recall_window_expires
    Given a case lapsed via C31 with no recall application after 30 days
    When s38_recall_window expires
    Then the case stays lapsed, the party is told about the s.14(2) route and the case manager gets a task to record any court filing

  Scenario: SM-case-C54_hold_review_never_ends_silently
    Given a case on_hold for 90 days with two hold reviews already recorded
    When the third hold_review clock is reached
    Then a review task goes to the role that set the hold and the matter escalates to the registrar
    And "cases.case.hold_reviewed.v1" is emitted and the next hold_review clock starts

  Scenario: SM-negotiation-N11_party_withdraws
    Given a negotiation in blind_bid_round
    When one party withdraws
    Then the proceeding moves to concluded_no_settlement, open offers lapse, the bid round closes as not crossed and the next rung is offered

  Scenario: SM-negotiation-N12_timebox_extension_capped
    Given a negotiation in active_offers on day 25 with all parties consenting
    When an extension to 50 days in total is requested
    Then it is refused because the total exceeds 45 days
    And an extension to 45 days is accepted and "clocks.clock.extended.v1" is emitted

  Scenario: SM-conciliation-K08_partial_settlement
    Given a conciliation in terms_formulated with heads A, B and C
    When the parties sign and the conciliator authenticates terms on heads A and B
    Then a s.73 settlement is created for A and B only and the proceeding returns to active for head C
    And conc_timebox continues

  Scenario: SM-conciliation-K09_timebox_extended_by_consent
    Given an active conciliation whose conc_timebox expires tomorrow
    When all parties consent to an extension before expiry
    Then conc_timebox is extended and "clocks.clock.extended.v1" is emitted

  Scenario: SM-mediation-M10_pause_does_not_stop_statutory_clocks
    Given a FIN mediation in_session with a running statutory clock
    When the mediator records a party-requested pause without all-party consent to suspend the time-box
    Then the proceeding moves to suspended, sessions are cancelled with neutral wording and caucus notes are frozen
    And med_contract_timebox and the statutory clock keep running

  Scenario: SM-mediation-M11_fam_resume_needs_fresh_screening
    Given a suspended FAM mediation
    When resume is requested without a fresh private screening (M02)
    Then resume is refused
    And after the screening is recorded the proceeding returns to its prior state

  Scenario: SM-mediation-M12_reopen_within_30_days
    Given a mediation reported not_settled 20 days ago
    When all parties ask to resume with the same mediator
    Then the proceeding moves to in_session, the report is marked "superseded by resumed mediation", no new registration fee is charged
    And med_contract_timebox resumes with its remainder, not reset

  Scenario: SM-mediation-M13_remaining_heads_routed
    Given a mediation settled_partial with an approved handoff memo
    When the remaining heads are routed
    Then this proceeding closes, the next rung opens for the unresolved heads only and the settled heads go to P06

  Scenario: SM-arbitration-A28_deposit_suspension_keeps_s29a
    Given an active arbitration whose final deposit notice has expired
    When the tribunal suspends under s.38(2)
    Then the proceeding moves to suspended with reason "deposit_unpaid_s38", the other party is offered substitute payment
    And arb_s29a continues while SLA clocks pause

  Scenario: SM-arbitration-A29_resume_on_payment
    Given an arbitration suspended for unpaid deposits
    When the deposits are reconciled
    Then the proceeding returns to its prior state and SLA clocks resume

  Scenario: SM-arbitration-A30_partial_consent_award
    Given an active arbitration with claims 1–4
    When the parties settle claims 1 and 2 and the tribunal records a consent award on them
    Then P06 issues a consent award with severable operative paragraphs for claims 1 and 2 only and arb_s29a is unchanged

  Scenario: SM-arbitration-A31_termination_recalled
    Given an arbitration terminated under s.38 with the recall window open
    When a recall order is recorded
    Then the proceeding returns to its state before termination and the case follows C52

  Scenario: SM-arbitration-A32_court_stay_recorded
    Given an active arbitration
    When a verified stay order of a competent court is uploaded by the registrar
    Then the proceeding moves to suspended with reason "court_stay" and tribunal actions are limited to recording orders

  Scenario: SM-emergency_arbitration-E05_withdrawal_before_appointment_refunds
    Given an emergency arbitration application in applied
    When the applicant withdraws before an emergency arbitrator is appointed
    Then the proceeding closes, all EA clocks stop and the fee is refunded 100% under RP-STD-ARB

  Scenario: SM-grm-G07_info_request_never_pauses_regulatory_clock
    Given a FIN_RBI ticket under review on day 10 of rbi_re_30d
    When the GRO requests a document from the complainant
    Then the ticket shows awaiting_complainant with reminders scheduled at day 3 and day 7
    And rbi_re_30d keeps running, only the internal SLA pauses, and "grm.ticket.info_requested.v1" is emitted

  Scenario: SM-grm-G08_reopened_keeps_number
    Given a ticket in final_reply_sent
    When the complainant reports within 30 days that the resolution was not implemented
    Then the same ticket number returns to review with reopen_count 1 and a 15-day grm_reopen_resolution clock
    And the original regulatory clock is not restarted and "grm.ticket.reopened.v1" is emitted

  Scenario: SM-grm-G09_withdrawal_counted_separately
    Given a ticket before final_reply_sent
    When the complainant withdraws in writing
    Then the ticket is closed with outcome "withdrawn" (status withdrawn, closed class — P09 §5.1) and all clocks stop
    And the MIS counts it separately from resolved tickets and the closing message carries the RB-IOS advisory where the variant requires
```

### I.(i-c) Owner-file scenarios collected by `rtm-check` *(v3.1)*

These scenarios live in their owner files and are not restated here; `rtm-check` (I.(iv) rule 3) must find each name in the test tree, and a missing one fails CI like a missing FR scenario. The NN-24…NN-32 coverage gap reported in the v3.1 review (no `NN-25_*` or `NN-32_*` scenario) is closed by the owner-file names in the first two rows.

| Owner file and location | Scenario names | Tags |
|---|---|---|
| Appendix M §9 (`tests/acceptance/studio/`) | `NN-25_unanchored_sentence_cannot_be_exported`; `NN-25_model_citation_blocked`; `NN-25_identical_terms_both_sides`; `NN-32_original_preserved_derived_labelled` | `@NN-25`, `@NN-32`, `@blocking` |
| Appendix L (acceptance tests, L-AT-09) | `NN-32_type_copy_labelled_and_linked_to_original` | `@NN-32`, `@blocking` |
| Appendix S §9 | S-27 Representative authority suspends and lapses; S-28 Cross-company grants are never delegated | `@P01` |
| Appendix P (acceptance tests) | NN-34 no-paid-listing claim stays scoped | `@P13`, `@NN-34` |
| Appendix O (acceptance tests) | Chambers pause keeps matters moving and is capped | `@P10`, `@P05` |
| Appendix X §X.21 (`tests/acceptance/appendix-X.feature`) | `L2C_rejected_handoff_returns_to_sender`; `Approval_delegate_cannot_be_the_maker` | `@P16` |
| P16 §12 | Complaint made later in the thread starts its own clock; Late conversion is a recorded breach; Level-2 decision closes the grievance; Deflection never blocks a complaint; Health with missing data is provisional; Superseded quote cannot be accepted; New automation runs in shadow mode | `@P16` |
| P17 §12 | Review lead time blocks late scheduling; Over-messaging of individuals blocks; Retry sends only to failed recipients | `@P17` |
| Appendix AE §AE.16 | AE-20 Standard fast lane matches only within bounds; AE-21 Standard entry is suspended after failures; AE-22 Missed restore test counts as a failure; AE-23 Restore Assurance Report reaches the evidence store | `@P00`/`@P14` (AE.19 addenda) |
| Appendix AA §AA.22 | Repeat-player arbitration booking blocked; Conflict re-check before payment; Slot hold prevents double booking; Sort options never use paid attributes | `@P19`, `@NN-34` (sort) |
| P19 §12 (`tests/acceptance/p19/`) | Repeat-player arbitration booking blocked; Failed matter creation refunds the buyer; Query becomes removable filter chips; Onboarding score never affects ranking | `@P19` |
| Appendix AB §AB.14 (`tests/acceptance/rev-v3/`) | Stop proposal needs human approval; Thin data cannot stop a new stream; Neutrality incident recommends, never engages, the kill switch | `@P19` |

---

## I.(ii) End-to-end UAT journeys

Each journey runs in the `uat` environment with pilot users acting the persona on synthetic data (P14 FR-P14-14). "Evidence" lists what the tester uploads to `eng.uat_evidence` (screenshots, generated PDFs with SHA-256, audit-event extracts filtered by `case_id`, timings). A journey passes only if every expected result holds and no S1 defect is open against it. Journeys tagged ★ must also be executed on the mobile app (low-end Android on 3G profile).

### FIN — Financial & Loan

**UAT-FIN-01 ★ — Bulk-referred personal-loan default → OTS mediation → escrow instalments**
- Personas: `enterprise_operator` (pilot NBFC collections ops), `party` borrower (Hindi-first, Jaipur), `neutral_mediator`, `escrow_officer`.
- Preconditions: NBFC tenant onboarded via RB-01; clause instances accepted at sanction; escrow agreement executed; DLT templates live.
- Steps: (1) operator uploads 500-row CSV; (2) borrower receives SMS + WhatsApp at 10:30 with deep link, opens on app, listens to notice in Hindi; (3) borrower verifies by OTP, responds "willing to settle", uploads salary slip via camera (Aadhaar masking prompt triggered on ID); (4) allocation by rotation; mediator confirms with disclosure; (5) joint session by video, borrower drops to audio-only; (6) OTS proposal ₹1,80,000 against ₹2,46,500 outstanding, lender signatory approves within authority; (7) settlement drafted, linted, e-stamped (RJ), Aadhaar eSigned; (8) 3 instalments via UPI AutoPay to escrow; (9) instalment 2 missed → reminder within 08:00–19:00 → cured; (10) NOC milestone released; case closed after signposting record.
- Expected: no row nominates a neutral; no contact outside 08:00–19:00; grievance officer details in every message; settlement sums never on Equator merchant account; bureau-reporting term recorded; clocks owned; closure guard passes.
- Evidence: bulk batch report; message log with timestamps; Independence Evidence Pack; settlement PDF hash + e-stamp certificate; escrow milestone ledger; audit extract.

**UAT-FIN-02 — Digital-lending recovery-harassment grievance → RE window → signposting to RBI Ombudsman**
- Personas: `party` complainant, `grievance_officer` of a lender GRM desk (`FIN_RBI`), `internal_ombudsman`.
- Preconditions: GRM desk with RBI 30-day SLA policy; IO configured.
- Steps: (1) complainant files via widget alleging calls at 21:00 by a recovery agent; (2) GRO acknowledges within SLA, uses AI-drafted response (labelled) and edits it; (3) ticket marked `conduct_flag`; (4) GRO response "partially resolved" → auto-escalated to the Internal Ombudsman within 20 days of receipt (IO Directions 2026 cl.14(1)(b)); IO decision recorded; (5) day-30 final reply without full resolution; platform shows RB-IOS escalation guidance with last date; (6) complainant chooses signposting.
- Expected: conduct-flagged ticket cannot be escalated to an Equator case; IO user differs from the GRO; RBI 30-day clock owned and alerted; signposting event names the RBI Integrated Ombudsman with date; no AI text sent without GRO action.
- Evidence: ticket timeline; clock alerts; signposting record; AI interaction log showing human edit.

**UAT-FIN-03 — MSME secured-loan arbitration with independent appointment, s.29A clock and stamped award**
- Personas: `counsel` for lender, `party_org_user` MSME director (respondent), `neutral_arbitrator`, `registrar`, `case_manager`.
- Preconditions: post-dispute arbitration (submission) agreement e-signed by both sides; fee schedule Board-approved.
- Steps: (1) lender files claim ₹42,00,000; (2) scrutiny accepts; (3) respondent and lender jointly propose a named arbitrator — rejected with 403 `NEUTRAL_SELECTION_FORBIDDEN` (lender–borrower matters never use party nomination, NN-03); Equator appoints from its panel by rotation with conflict checks; (4) disclosure with one Fifth Schedule item; no objection; (5) pleadings complete → s.29A clock starts; (6) documents-only hearing plus one video hearing recorded with all consents; (7) AI award skeleton drafted, arbitrator edits, maker–checker, signs by DSC on web; (8) award e-stamped (UP) and served; (9) s.34 window clock starts; execution pack generated after window.
- Expected: lender never receives neutral-selection controls; s.29A alerts at T-90/60/30; award has reasons and evidence citations; stamp before delivery; BSA s.63(4) certificate in bundle.
- Evidence: allocation run record; clock alerts; award PDF hash; stamp certificate; execution pack manifest.

**UAT-FIN-04 — NI Act s.138 cheque dishonour: negotiated settlement and compounding pathway**
- Personas: `party` payee (proprietorship), `party` drawer, `counsel`, `neutral_conciliator`.
- Preconditions: complaint already pending before the Magistrate (linked matter, external forum reference recorded).
- Steps: (1) payee files with cheque ₹3,00,000, dishonour memo and statutory demand notice uploaded; (2) NI-138 exposure calculator shows interim compensation (s.143A, up to 20%) and appeal deposit (s.148, minimum 20%) as indicative statutory figures, not a prediction; (3) conciliation; settlement ₹3,30,000 in two instalments direct-pay with proof; (4) settlement terms include withdrawal/compounding steps before the court (s.147) with the court's own role stated; (5) instalment proofs verified; compliance obligations closed.
- Expected: no statement on likely conviction or outcome (NN-01); criminal adjudication never offered (NN-06); linked-matter record names the court and case number; settlement sums not on Equator merchant account (NN-13).
- Evidence: calculator output with version; settlement hash; obligation evidence; linked-matter record.

**UAT-FIN-05 ★ — Document-first intake, pre-fill and status messages** *(v3.1; P08 FR-P08-85–FR-P08-88)*
- Personas: `party` borrower (Hindi-first), `case_manager`.
- Steps: (1) borrower photographs a loan recall notice before answering any question; (2) extraction pre-fills lender, account and amount; fields below `tenant.intake.prefill_min_confidence` are shown empty for entry, and every pre-filled field shows its source; (3) questions already answered by the document are skipped; (4) borrower picks "Something else" at the first question → human-review route, never a dead end; (5) case enters the case manager's deadline-ordered queue; (6) each state change sends the matching `status_msg.fin.*` text in Hindi with the next step and date.
- Expected: no field filled from model free text without source (NN-01, NN-32); every outcome routes to a signpost, intake or a decline with reason (VAL-P08-NDE); status texts free of outcome predictions.
- Evidence: extraction record with confidence per field; skipped-question log; queue snapshot; message log.

### COM — Commercial & Business

**UAT-COM-01 — MSME delayed payment → conciliation → signposting to MSEFC / MSME ODR**
- Personas: `party` MSME supplier (Udyam registered), `party_org_user` buyer's finance head, `neutral_conciliator`.
- Steps: (1) supplier files ₹8,75,000 invoice claim with interest under MSMED Act s.16; (2) calculator shows compound interest at three times the bank rate (indicative); (3) routing offers conciliation and names MSEFC with its statutory route; (4) conciliation session; buyer offers ₹7,50,000; (5) no settlement → arbitration blocked until conciliation recorded failed; supplier elects MSEFC.
- Expected: MSME arbitration not offered before conciliation failure; signposting event with forum and date; no AI valuation statement.
- Evidence: route decision; calculator output with version; signposting record.

**UAT-COM-02 ★ — Pre-suit commercial dispute: voluntary Equator mediation and s.12A PIMS signposting (M-06)**
- Personas: `counsel` for both parties, `neutral_mediator`, `case_manager`.
- Steps: (1) claimant files a ₹65,00,000 supply dispute before suit; triage shows that mandatory s.12A pre-institution mediation is conducted by the Legal Services Authority under the PIMS Rules 2018 and generates the Form-1 application pack; (2) both parties also agree in writing to voluntary contractual pre-suit mediation by Equator; respondent served by email + speed post (`POSTAL_PORT`); (3) mediation (contractual mode; statutory flag OFF); (4) caucus notes written by mediator only; (5) settlement signed electronically and stamped as a contract (or recorded as a consent award under arb-med-arb where agreed); (6) non-settlement variant: Equator issues a mediation closure note that states it is not a s.12A report, and the PIMS referral record awaits the Authority's Form-3/Form-5 outcome.
- Expected: `com.s12a_equator_authorised` OFF; no Equator document claims to satisfy s.12A (copy lint) or s.27 enforceability; no recording; caucus notes invisible to case manager; Form-1 pack and `com.pims_referrals` row created.
- Evidence: Form-1 pack hash, PIMS referral record, session logs (no egress), RLS denial log, settlement/closure-note hashes.

**UAT-COM-03 — Expedited arbitration with emergency arbitrator**
- Personas: `counsel` claimant (IT services vendor), `counsel` respondent, `neutral_arbitrator` (emergency), sole arbitrator.
- Steps: (1) claimant applies for emergency relief to restrain encashment of a ₹25,00,000 bank guarantee; (2) emergency arbitrator appointed within the rules' time-box; (3) order issued within 14 days (configurable); (4) tribunal constituted; fast-track s.29B documents-only; (5) award within the fast-track period.
- Expected: emergency fee quoted and paid before appointment; order served with proof; s.29B forces sole arbitrator; clocks shown to both sides.
- Evidence: quote, order PDF, service certificate, clock history.

### FAM — Family, Marital & Property

**UAT-FAM-01 ★ — Mutual-consent divorce terms with safety screening and shuttle sessions**
- Personas: two `party` spouses (one NRI in Dubai, timezone GST), `neutral_mediator`, `safeguarding_lead`.
- Steps: (1) wife files; private screening questionnaire indicates coercion concern → `shuttle_only`; (2) husband is never told screening occurred; (3) joint session request blocked; shuttle sessions scheduled across timezones; (4) terms on maintenance ₹35,000/month, streedhan return, parenting plan; (5) settlement lint flags "maintenance waived" wording → fixed; (6) consent terms signed; family court filing pack generated.
- Expected: `SAFETY_FLAG_BLOCKS_JOINT` on joint scheduling; no award or arbitration offered for status/custody; screening data only in `safety_sealed`; mobile screens screen-protected.
- Evidence: blocked API log; lint report; filing pack; sealed-access log entries.

**UAT-FAM-02 — Partition of ancestral property among heirs → MSA → physical registration**
- Personas: four `party` heirs (one minor represented by guardian), `counsel`, `neutral_mediator`, `case_manager`.
- Steps: (1) filing lists estate assets: agricultural land (Rajasthan), residential flat (Noida), bank deposits; (2) heirs-not-joined check passes after the fourth heir joins; (3) mediation reaches partition terms; (4) instrument becomes `partition_immovable`; eSign hidden; (5) registration task with checklist and sub-registrar booking; (6) stamp duty per state matrix; (7) closure after registration recorded.
- Expected: NN-08 physical route enforced; minor recorded with initials and age only and guardian consent; arbitration offered only for property rights if all agree; closure blocked until registration.
- Evidence: registration task record; stamp computation; guardian consent record.

**UAT-FAM-03 — Custody dispute: arbitration request refused, child-inclusive mediation**
- Personas: `party` parents, `neutral_mediator` with child-inclusive endorsement.
- Steps: (1) father requests arbitration on custody; (2) system refuses and offers mediation and the family court signpost; (3) parenting plan mediated; (4) child-at-risk indicator raised → safeguarding referral pathway triggered, case paused with reason.
- Expected: `CASE_NOT_ARBITRABLE`; on-hold with clock policy; safeguarding lead notified; no child data in analytics.
- Evidence: refusal response; hold record; referral log.

### INS — Insurance

**UAT-INS-01 ★ — Retail health claim repudiation → signposting with clocks → mediation**
- Personas: `party` policyholder (Marathi), `party_org_user` insurer grievance officer, `neutral_mediator`, `case_manager`.
- Steps: (1) policyholder files; representation date 45 days ago; (2) eligibility shows Insurance Ombudsman criteria and last date to file; signposting delivered in Marathi; (3) policyholder chooses mediation in parallel; (4) discharge summary uploaded to health sealed store via web; (5) insurer confirms settlement authority; (6) settlement ₹1,42,000 with continuity preserved; (7) voucher basis "full and final" checked against reservation rules.
- Expected: arbitration never offered (retail); ombudsman clock owned and not paused by mediation; health record absent from AI, notifications and dashboards; no success fee.
- Evidence: eligibility output; signposting record; health access log; settlement hash.

**UAT-INS-02 — Motor own-damage short-settlement with deduction analysis**
- Personas: `party` vehicle owner, insurer officer, surveyor (`neutral_expert` not engaged), mediator.
- Steps: (1) claim ₹3,20,000, offered ₹2,05,000; (2) deduction lines entered (depreciation, consumables) with reasons; (3) proportionality and deductible analysis displayed as computed facts; (4) settlement ₹2,60,000; voucher "under protest" requires reserved balance.
- Expected: offered ≤ claimed validation; deduction reason mandatory; voucher check; no valuation by AI.
- Evidence: deduction analysis export; voucher record.

**UAT-INS-03 — Insurer–reinsurer B2B quantum arbitration with expert determination**
- Personas: `counsel` for cedant and reinsurer, `neutral_expert` (marine surveyor), three-member tribunal.
- Steps: (1) liability admitted; quantum disputed (USD-denominated treaty, INR invoicing); (2) expert determination on loss quantum; (3) arbitration on residual quantum; (4) award in INR with FX snapshot recorded for USD figures.
- Expected: arbitration permitted (B2B, quantum only); concentration cap check on arbitrators per insurer; FX snapshot with source and timestamp.
- Evidence: expert report hash; allocation records; award with FX annex.

### WRK — Workplace & HR

**UAT-WRK-01 ★ — Full-and-final and gratuity dispute → mediation → escrow milestones**
- Personas: `party` ex-employee, `party_org_user` HR head, `neutral_mediator`, `escrow_officer`.
- Steps: (1) employee claims F&F ₹2,15,000 + gratuity; calculator flags wages < 50% of CTC; (2) mediation; (3) settlement with gratuity "paid, not waived", relieving letter and asset return; (4) escrow milestones: tranche 1 on signing, final tranche on relieving letter upload + asset return confirmation.
- Expected: `STATUTORY_WAIVER_FORBIDDEN` on any waiver wording; final tranche blocked without evidence; employee app shows milestone status.
- Evidence: calculator output; milestone evidence; release approvals (maker ≠ checker).

**UAT-WRK-02 — Co-founder exit (non-workman) arbitration**
- Personas: `counsel` for founder and company, `neutral_arbitrator`.
- Steps: (1) dispute on vesting and buy-back price ₹1,20,00,000; (2) is_workman = false confirmed; (3) arbitration with documents-only phase and one hearing; (4) award signed and stamped.
- Expected: arbitration allowed only after is_workman false; disclosure; s.29A clock; award reasoned.
- Evidence: employment record; award hash; stamp certificate.

**UAT-WRK-03 — Retrenchment / IR Code grievance → signposting; workman arbitration blocked**
- Personas: `party` workman, `grievance_officer` (`WRK_IRCODE` desk).
- Steps: (1) workman files retrenchment-compensation grievance; (2) GRC route shown; (3) attempt to start arbitration; (4) signposting to the conciliation officer/labour authority with timelines (application through the trade union within 60 days of the GRC decision or of expiry of 30 days — IR Code s.4(8)).
- Expected: `WRK_WORKMAN_ARBITRATION_BLOCKED`; signposting recorded; GRC SLA clock owned.
- Evidence: refusal response; signposting record.

### INT — International Commercial

**UAT-INT-01 — Cross-border sale of goods (CISG) ICA seated at GIFT City IFSC, USD fees**
- Personas: `counsel` for Indian exporter and Singapore buyer, sole arbitrator (third-country national), `case_manager`.
- Steps: (1) filing in USD 340,000; (2) sanctions screening (UN, OFAC, EU, UK, MHA) clear; KYC/UBO for the foreign company; DPDP s.16 transfer basis recorded; FEMA route "current"; (3) s.2(1)(f) test passes; (4) fees quoted in USD with INR equivalent, export of services under LUT; (5) allocation defaults to neutral nationality; (6) virtual hearing across IST/SGT; (7) award, New York Convention enforcement pack with enforcement-target metadata.
- Expected: registration blocked until all gates pass; `FX_RATE_STALE` if the FX snapshot is older than the Appendix B FX-5 limit (3 business days) at payment; neutral nationality rule honoured.
- Evidence: screening record; quote with FX snapshot; enforcement pack manifest.

**UAT-INT-02 — International mediation → consent-award conversion**
- Personas: two foreign companies (UAE, Germany) via `counsel`, `neutral_mediator`, arbitral tribunal constituted for consent award.
- Steps: (1) mediation settles; (2) platform displays "India has signed but not ratified the Singapore Convention" note and offers consent-award conversion; (3) arb-med-arb tribunal records consent award under A&C s.30; (4) stamped and delivered.
- Expected: conversion offered automatically; mediation caucus material not in arbitral record.
- Evidence: notice text; consent award hash.

**UAT-INT-03 — Potential sanctions match → hold → cleared after review**
- Personas: `case_manager`, `registrar`, `counsel`.
- Steps: (1) respondent name fuzzy-matches a listed entity; (2) case held with `SANCTIONS_HIT_REVIEW`; (3) reviewer records evidence of non-identity; (4) registration proceeds.
- Expected: no notice or fee collection during hold; reviewer identity and evidence logged.
- Evidence: screening hits, review record, audit extract.

### GRM — Grievance Redressal SaaS (four variants)

**UAT-GRM-01 — Lender → Borrower (`FIN_RBI`)**: borrower complaint on wrong charges ₹4,720; GRO resolves in 12 days with refund; MIS shows TAT; quarterly regulatory report generated. Expected: 30-day clock; IO review (by day 20) where partially resolved or rejected; outcome enum; report fields complete. Evidence: ticket timeline, report file.

**UAT-GRM-02 — Listed company → Shareholder (`SEC_LODR`)**: shareholder complaint on unpaid dividend; acknowledgement and resolution within configured SCORES timelines (SCORES ATR ≤ 21 calendar days, SEBI/HO/OIAE/IGRD/CIR/P/2023/156; Reg 13(3) statement in Integrated Filing–Governance ≤ 30 days of quarter-end); Stakeholders' Relationship Committee export generated. Expected: SEBI-aligned categories; export for board/secretarial use; no Equator case created without consent. Evidence: SRC export, timeline.

**UAT-GRM-03 — Employer → Employee (`WRK_HR` and `WRK_WHISTLE`)**: (a) named grievance on shift allowance escalated to ODR mediation with employee consent; (b) anonymous whistle-blower report handled with anonymous token. Expected: escalation requires consent record; whistle-blower identity never stored. Evidence: escalation record, anonymous token flow.

**UAT-GRM-04 — University → Student (`EDU_UGC`)**: student complaint on fee refund to SGRC; SGRC decision; appeal to Ombudsperson; ragging/POSH indicators trigger refusal with referral route. Expected: UGC (Redressal of Grievances of Students) Regulations 2023 timelines from ruleset (SGRC 15 working days; appeal 15 days; Ombudsperson 30 days), with the appeal decided by `student_ombudsperson`; referral routes displayed; `sgrc_member` access limited to the institution tenant. Evidence: ticket timeline, referral log.

### POSH

**UAT-POSH-01 — IC complaint to report and employer action**
- Personas: `ic_presiding_officer`, `ic_member`, `ic_external_member`, complainant (employee), respondent, `enterprise_admin` (employer).
- Steps: (1) IC constituted with 4 members, 2 women, external member; (2) complaint within 3 months of incident; (3) complainant requests conciliation in writing without monetary terms — recorded; variant: no request → inquiry; (4) inquiry 90-day clock; hearings in sealed workspace on web; (5) report issued → employer action 60-day clock; (6) annual report compiled.
- Expected: no POSH data in core, AI, analytics, webhooks or mobile content; mobile receives content-free push only; access logged on every read.
- Evidence: sealed access log; clock records in sealed store; annual report (counts only).

### Private ADR Chambers

**UAT-CHM-01 — Independent mediator launches a chambers tenant**
- Personas: `chambers_admin` (senior mediator), `party` clients, `neutral_mediator` associates.
- Steps: (1) self-serve chambers set-up with branding, own fee schedule (maker–checker), own procedure rules version; (2) first case with chambers prefix numbering; (3) invoice under chambers' GSTIN; (4) optional organic listing on the Private Practice Marketplace; no sponsored slot while `marketplace.paid_placement` is OFF (NN-34) *(v3.1)*.
- Expected: complete tenant isolation (cross-tenant fuzz passes); NN rules not disableable; platform subscription invoiced to chambers.
- Evidence: tenant config, case number format, invoice PDFs.

### Academy

**UAT-ACD-01 — Learner completes 40-hour mediation course and receives a verifiable certificate**
- Personas: `learner`, `trainer`, `university_admin` (partner).
- Steps: (1) enrolment and fee payment (web; not via iOS app); (2) attendance and role-play assessments; (3) trainer scoring; (4) certificate issued with verification code; (5) CPD record; (6) partner university receives outcomes only where credit is sought.
- Expected: no learner ever accesses live case data; certificate public verify shows only name, course, date, status.
- Evidence: certificate PDF, verification page capture, data-release note.

**UAT-MOB-01 ★ — Respondent first touch on a low-end phone (cross-vertical)**
- Personas: `party` respondent with no prior account, Hindi-first, 2 GB Android Go device on a 3G profile.
- Steps: (1) WhatsApp notice with `/m/r/{token}` link at 11:00; app not installed → web notice renders (SSR) with Listen; (2) installs app, claims deep link with OTP to the served number; (3) biometric set-up; (4) reads notice aloud in Hindi; (5) photographs a 6-page reply document (edge detection, compression ≤ 350 KB/page); (6) upload interrupted by network loss and resumed; (7) books a hearing slot; (8) joins hearing, auto-switches to audio-only, then joins by phone with PIN.
- Expected: no case data before OTP; upload hash verified and ledgered; cold start < 4.0 s; no crash; screen protection on sealed tiers if applicable.
- Evidence: Maestro run video, timings, upload ledger entry, attendance record.

---

## I.(iii) Non-functional test catalogue

IDs `NFR-<AREA>-NN`. Frequency: **PR** every pull request; **N** nightly; **R** each release candidate; **Q** quarterly; **GL** once before go-live. All targets trace to master §11 unless stated.

| ID | Area | Test | Target / pass criterion | Tool | Freq |
|---|---|---|---|---|---|
| NFR-PERF-01 | Performance | Portal read/write mix 5,000 VUs | p95 read < 300 ms, write < 800 ms, errors < 0.1% | k6 | R |
| NFR-PERF-02 | Performance | Bulk intake 100,000 rows | single batch: validation ≤ 10 min, commit ≤ 30 min (P09 FR-P09-12); three tenants concurrently: ≤ 15 / ≤ 60 min (P14 S2); zero duplicates | k6 + SFTP harness | R |
| NFR-PERF-03 | Performance | Notice campaign 1,000,000/day inside 08:00–19:00 | outbox lag p95 < 60 s; zero out-of-window | k6 + provider mocks | R |
| NFR-PERF-04 | Performance | 500 concurrent hearing rooms | join success ≥ 99.5%; MOS ≥ 3.5 (4G) | LiveKit load tester | GL, Q |
| NFR-PERF-05 | Performance | Clock scheduler 1,000,000 clocks + 10× burst | ≤ 10 min, zero missed | k6 + Temporal | R |
| NFR-PERF-06 | Performance | Web vitals on indexable routes | LCP < 2.5 s, CLS < 0.1, INP < 200 ms | Lighthouse CI + RUM | PR (sample), R |
| NFR-PERF-07 | Performance | Mobile cold start and budgets | P12 FR-P12-23 | Maestro + profilers | R |
| NFR-REL-01 | Reliability | Soak 8 h at 60% load | no memory growth > 10% | k6 | R |
| NFR-REL-02 | Reliability | Spike 5× for 5 min | autoscale ≤ 3 min; no data loss | k6 | R |
| NFR-REL-03 | Reliability | Provider outage per port (SMS, WhatsApp, eSign, payments, LLM, video) | graceful degradation per Appendix D; circuit breaker opens; no lost side effects | fault injection | N |
| NFR-DR-01 | DR | Region failover | RPO ≤ 15 min, RTO ≤ 2 h, audit chain verified | DR runbook RB-05 | GL, Q |
| NFR-DR-02 | DR | PITR restore | checksum equality on 1,000 sampled rows and 100 objects | restore script | monthly |
| NFR-DR-03 | DR | Backup immutability | delete/overwrite of backup and evidence objects denied | AWS policy test | Q |
| NFR-SEC-01 | Security | SAST, dependency, container, IaC, secret scans | zero unwaived Critical/High | Semgrep/CodeQL, Trivy, Checkov, gitleaks | PR |
| NFR-SEC-02 | Security | OWASP API Top 10 suite | all pass | custom + ZAP | N |
| NFR-SEC-03 | Security | DAST on staging | no High | ZAP/Burp | R |
| NFR-SEC-04 | Security | Cross-tenant fuzz on all `{id}` routes | 100% `404` indistinguishable | custom | N |
| NFR-SEC-05 | Security | RLS catalogue check | every tenant table forced RLS + policy | SQL check | PR |
| NFR-SEC-06 | Security | Sealed-schema reference scan | no reference outside sealed modules, views, exports, prompts | CI grep + SQL | PR |
| NFR-SEC-07 | Security | VAPT by CERT-In empanelled auditor | zero open Critical/High | external | GL, Q |
| NFR-SEC-08 | Security | Mobile MASVS L2 | pass | external + MobSF | GL, R (major) |
| NFR-SEC-09 | Security | AI red-team (prompt injection, jailbreak, sealed exfiltration) | zero-tolerance set 100% | eval harness | R |
| NFR-SEC-10 | Security | Time sync drift | < 100 ms vs NIC/NPL | chrony metrics | continuous |
| NFR-PRIV-01 | Privacy | PII-in-logs scan | zero matches for phone/email/PAN/Aadhaar patterns in logs and telemetry | log scanner | N |
| NFR-PRIV-02 | Privacy | Retention jobs | correct candidates; legal hold respected | dry-run report | R |
| NFR-PRIV-03 | Privacy | Consent withdrawal propagation | ≤ 72 h to all processors | integration test | R |
| NFR-PRIV-04 | Privacy | Residency | all stores in ap-south-1/2 | IaC policy (OPA/Checkov) | PR |
| NFR-ACC-01 | Accessibility | axe on all routes (en, hi) | zero critical/serious | axe-core | PR |
| NFR-ACC-02 | Accessibility | Screen-reader scripts: file, respond, pay, sign, join | pass with NVDA (web), TalkBack, VoiceOver | manual | R |
| NFR-ACC-03 | Accessibility | 200% text zoom / font scale | no loss of content or function | manual + visual regression | R |
| NFR-ACC-04 | Accessibility | Keyboard-only completion of critical journeys | pass | Playwright | N |
| NFR-L10N-01 | Localisation | Catalogue completeness per enabled locale | ≥ 99% keys; legal templates approved | i18n linter | PR |
| NFR-L10N-02 | Localisation | Bilingual parity of routes/clocks (200 pairs) | 100% identical | eval harness | R |
| NFR-L10N-03 | Localisation | Script rendering (Devanagari, Tamil, Bengali, Gurmukhi, Odia, Malayalam, Kannada, Telugu, Gujarati, Nastaliq RTL) | no clipping/tofu; RTL layout correct for Urdu | visual regression | R |
| NFR-L10N-04 | Localisation | Indian formats | ₹ with Indian grouping (₹1,00,000), dates DD MMM YYYY, IST default | unit + snapshot | PR |
| NFR-L10N-05 | Localisation | Machine-translation labelling | every unapproved translation labelled "unofficial" | snapshot | R |
| NFR-OBS-01 | Observability | Every alert links to a runbook | 100% | config lint | PR |
| NFR-OBS-02 | Observability | Trace propagation API → worker → DB | ≥ 99% of sampled requests fully traced | OTel check | N |
| NFR-COMP-01 | Compliance | CERT-In log retention | 179-day-old log retrievable from India region | restore test | GL, Q |
| NFR-COMP-02 | Compliance | Audit chain verification | nightly full verify pass | job | N |

---

## I.(iv) Traceability guidance and naming conventions

1. **Requirement IDs.** Functional requirements are `FR-PXX-NN` (phase files §4). NN rules are `NN-01`…`NN-40` (master §3); NN-24–NN-32 scenarios live in their owner files and are collected by `rtm-check` *(v3.1)*. Differentiators `D1`…`D12` (master §2). Non-functional `NFR-<AREA>-NN` (this appendix). UAT journeys `UAT-<VERT|GRM|POSH|CHM|ACD|MOB>-NN`. Legal rules use their Appendix G IDs. Runbooks `RB-NN` (P14).
2. **Test file naming.**
   - Acceptance: `tests/acceptance/PXX/FR-PXX-NN_<slug>.feature`, each scenario tagged `@FR-PXX-NN` and, where relevant, `@NN-xx`, `@D<n>`, `@web`, `@mobile`, `@api`.
   - NN suite: `tests/acceptance/nn/NN-xx_<slug>.feature` (Section I.(i)); every NN scenario name starts `NN-xx_`.
   - Unit/integration: `*.spec.ts` next to code; describe blocks prefixed with the FR ID they cover (`describe('FR-P05-07 quote engine', …)`).
   - Maestro: `apps/mobile/e2e/<capability>/<flow>.yaml` with `tags: [FR-P12-15, NN-11, CAP-P04-03]`.
   - Performance: `tests/perf/NFR-PERF-NN_<slug>.js`.
   - AI evals: `packages/ai/evals/<agent>/<suite>.yaml` with `nn: [NN-01]` metadata.
3. **Coverage rules (CI job `rtm-check`).** Every FR in every merged phase file must have ≥ 1 acceptance scenario; every NN rule ≥ 1 automated scenario per surface where it applies (API mandatory; web/mobile where a UI exists); every UAT journey references the FRs it exercises (front-matter list); every Critical/High risk in the risk register references ≥ 1 test. The job parses phase markdown for `FR-PXX-NN` headings and test tags, and fails on gaps.
4. **Requirements Traceability Matrix.** Generated nightly to `docs/compliance/rtm.csv` with columns: requirement ID, source file and line, NN/D/legal-rule links, test IDs, last result, last run, owner. The RTM is attached to the go-live pack and to each ISO 27001 control where tests evidence controls.
5. **Gherkin style.** Given/When/Then in business language; one behaviour per scenario; error assertions use Appendix F codes; amounts in ₹ with Indian grouping or minor units when asserting storage; times in IST with explicit dates; personas use master role codes; no real personal data; seed IDs from `packages/seed` fixtures (`seed:pilot-nbfc`, `seed:pilot-insurer`, etc.).
6. **Evidence retention.** UAT evidence and release test reports are retained for 8 years (aligned with case records) as they evidence the platform's procedural integrity if an award is challenged.
7. **Change control.** A change to a legal rule, ruleset or fee schedule must re-run the tagged scenarios for affected FRs and all `@NN-04`, `@NN-06`, `@NN-12`, `@NN-20` and `@NN-33` scenarios before activation (C1 C.4: legal-clock and enforcement scenarios are a release gate for any ruleset change).

---

## I.(v) Go-live acceptance sign-off matrix

Legend: **A** = accountable signatory (signature required); **R** = responsible for evidence; **C** = consulted. A row is accepted when every **A** has signed in `eng.launch_checklist_items` with evidence links and no automatic no-go condition (P14 FR-P14-17) applies.

| Acceptance area | Evidence | Product owner | Registrar / Head of Mediation | CS / Legal | DPO | Security lead | SRE lead | QA / UAT lead | Pilot tenant rep |
|---|---|---|---|---|---|---|---|---|---|
| FIN vertical | UAT-FIN-01..03; NN-03, NN-12, NN-13 green | A | A | C | C | — | — | R | A (pilot NBFC) |
| COM vertical | UAT-COM-01..03 | A | A | C | — | — | — | R | A (pilot corporate) |
| FAM vertical | UAT-FAM-01..03; safeguarding pathway approved | A | A | A | C | — | — | R | C |
| INS vertical | UAT-INS-01..03; health sealed store review | A | A | C | A | C | — | R | A (pilot insurer) |
| WRK vertical | UAT-WRK-01..03 | A | A | C | — | — | — | R | A (pilot employer) |
| INT vertical | UAT-INT-01..03; sanctions provider live | A | A | A | A | — | — | R | C |
| GRM (4 variants) | UAT-GRM-01..04; regulator timelines in Appendix G verified | A | C | A | C | — | — | R | A |
| POSH SaaS | UAT-POSH-01; sealed isolation pen-test | A | C | A | A | A | — | R | A (pilot employer) |
| Private Chambers | UAT-CHM-01; cross-tenant fuzz | A | C | C | — | A | — | R | A |
| Academy | UAT-ACD-01; data map with university | A | C | C | A | — | — | R | A (partner university) |
| Mobile apps | P12 exit gate; store approvals | A | — | C (store copy) | A (labels) | A (MASVS) | C | R | C |
| Security | VAPT + retest letter; ASVS matrix; API Top 10 | C | — | — | C | A | C | R | — |
| DPDP / privacy | RoPA, DPIAs, breach rehearsal, DSR SLAs | C | — | C | A | C | — | R | — |
| CERT-In | PoC, 180-day logs, NTP, 6-h runbook | — | — | C | C | A | A | R | — |
| Performance & DR | NFR-PERF-01..07, NFR-DR-01..03 | C | — | — | — | — | A | R | — |
| Accessibility & language | NFR-ACC-01..04, NFR-L10N-01..05 | A | C | — | — | — | — | R | C |
| AI layer | P11 gates on RC; red-team; AI Governance Rule published | A | A | A | C | C | — | R | — |
| Legal sign-off | P14 FR-P14-16 items 1–12; Board resolutions (fees, rules) | C | A | A | C | — | — | — | — |
| Data migration | reconciliation report | C | A | — | A | — | R | R | — |
| Operations | runbooks RB-01..14 rehearsed; on-call rota 30 days | C | C | — | C | C | A | — | — |
| **Final go-live** | all rows accepted; NN suite 100% green on RC | **A (CEO chairs)** | A | A | A | A | A | A | C |

Sign-off rules: (1) no signatory may sign a row for which they were the sole evidence producer (segregation of duties); (2) a row with an NN-linked open item cannot be waived; (3) signatures are step-up authenticated and audited (NN-22); (4) the signed matrix, RTM and UAT certificates are archived with Object Lock as part of the go-live record.
