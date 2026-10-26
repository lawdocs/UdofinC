# Udofin "i" help registry — seed term list v1.3 (26 October 2026)

**Purpose.** The seed list for `packages/hlp` (IPB-07 §07.3.4, §07.4.3; Udofin Master Prompt v1.3 Part 7I IB4). Each row becomes a `hlp.udf.<term>` entry. Claude Code writes the `plain` text (≤ 40 words, reading age 12) and `explanation` in English and Hindi in Phase 1 and in the remaining ten locales in Phase 22; every entry with a LAW tag needs `reviewer_of_record` (legal reviewer) before `published`. Keys are immutable. Module tags map to the Part 7 modules so that coverage reports can be produced per screen.

**Regulatory references.** "CF" = NBFC Credit Facilities Directions, 2025 (digital-lending chapter and Annex-I; the IPB calls the same obligations the "RBI (Digital Lending) Directions, 2025" [VERIFY coexistence]); "RBC" = Responsible Business Conduct Directions, 2025; "KYC" = KYC Directions; "CIR" = Credit Information Reporting Directions; "AA" = Account Aggregator Directions; "OUT" = Outsourcing Directions, 2025; "DPDP" = Digital Personal Data Protection Act, 2023 and Rules, 2025; "RB-IOS" = Reserve Bank – Integrated Ombudsman Scheme, 2026; "IO" = Internal Ombudsman Directions, 2026; "MFI" = Microfinance Directions. Paragraph numbers are as used in Part 8A and carry its [VERIFY] status.

**Counts.** 262 terms: A Core and roles 22 · B Consent and privacy 30 · C Identity and KYC 26 · D Credit data and eligibility 20 · E Offers, KFS and cooling-off 34 · F Documents and signing 14 · G Repayments and mandates 22 · H Loan servicing 16 · I Collections and recovery 16 · J DLG 8 · K Grievance 22 · L Wellness, products and plans 12 · M Accessibility, AI and app 20.

| # | Key (`hlp.udf.`) | Term | Module | Regulatory reference | Tag |
|---|---|---|---|---|---|
| **A** | **Core and roles** | | | | |
| 1 | `lsp` | Lending Service Provider (LSP) | U1, About | CF para 4(1)(xix) | LAW |
| 2 | `regulated_entity` | Regulated entity (RE) / lender | U1 | CF para 4(1)(xxiv) [VERIFY] | LAW |
| 3 | `dla` | Digital lending app (DLA) | U18 | CF para 4(1)(x) | LAW |
| 4 | `udofin_is_not_a_lender` | Udofin is not a lender | About, footer | CF paras 4, 10; Part 4.1 | LAW |
| 5 | `the_lender_decides` | The lender decides | U7, U8 | OUT para 15; CF para 12(3) | LAW |
| 6 | `partner_lender` | Partner lender | Lenders page | CF para 9(4)–(5) | LAW |
| 7 | `lender_strip` | "Loan from [RE] · facilitated by Udofin" | all loan screens | CF paras 9(5), 18(6) | LAW |
| 8 | `nodal_grievance_officer` | Udofin nodal grievance officer | Help, footer | CF para 12(2) | LAW |
| 9 | `grievance_redressal_officer` | Lender's grievance redressal officer (GRO) | UB3 | CF para 12(1) | LAW |
| 10 | `cims_dla_list` | RBI list of digital lending apps (CIMS) | Safety page | CF para 18, Annex-I | LAW |
| 11 | `rbi_sachet` | RBI Sachet portal | Safety page | RBI Sachet (public) | REC |
| 12 | `nbfc` | Non-banking financial company (NBFC) | U1 | RBI Act 1934 s.45-I | LAW |
| 13 | `hfc` | Housing finance company | U1 | NHB/RBI HFC Directions | LAW |
| 14 | `nbfc_mfi` | Microfinance institution (NBFC-MFI) | MG2 | MFI paras 3, 8 | LAW |
| 15 | `cooperative_society` | Credit co-operative society (not an RE) | UP4, MG1 | MSCS Act 2002; State Acts | LAW |
| 16 | `operating_model_portal_only` | Portal-only lender | U1 | Part 5.4 | INTERP |
| 17 | `lender_system_of_record` | Lender's system of record | U12 | Part 5.1; CF para 14(1) | INTERP |
| 18 | `loan_mirror` | Loan mirror (as-of time) | U12 | Part 10.2 principle 28 | INTERP |
| 19 | `as_of_time` | As of (time of last lender update) | U12, U25 | Part 10.2 principle 28 | REC |
| 20 | `maker_checker` | Maker-checker | portals | CYB paras 119–120 | LAW |
| 21 | `infrabyx_group` | Part of the Infrabyx Group | About | Companies Act 2013 disclosure | LAW |
| 22 | `technology_by_udofin` | Technology by Udofin (white-label) | IB3 | CF paras 9(5), 18(6) [VERIFY wording] | INTERP |
| **B** | **Consent and privacy** | | | | |
| 23 | `consent` | Consent | U4 | CF para 13; DPDP s.6 | LAW |
| 24 | `purpose_of_data` | Purpose of this data request | U4 | CF para 13(3); DPDP s.5 | LAW |
| 25 | `notice_version` | Notice version | U4 | DPDP s.5 | LAW |
| 26 | `consent_withdrawal` | Withdrawing consent | U4 | DPDP s.6(4)–(6); CF para 13(4) | LAW |
| 27 | `consequences_of_withdrawal` | What happens if you withdraw | U4 | DPDP s.6(6) | LAW |
| 28 | `data_fiduciary` | Data fiduciary | U4, About | DPDP s.2(i) | LAW |
| 29 | `data_processor` | Data processor | U4 | DPDP s.2(k) | LAW |
| 30 | `data_principal` | Data principal (you) | U4 | DPDP s.2(j) | LAW |
| 31 | `minimal_data` | Basic minimal data kept by Udofin | U4, U25 | CF para 14(1) | LAW |
| 32 | `re_scoped_vault` | Lender-controlled vault | U4, U9 | CF para 14(1); OUT para 97(vii)(b) | INTERP |
| 33 | `data_in_india` | Your data stays in India | U4, Safety | CF para 14(4) | LAW |
| 34 | `retention_period` | How long we keep this | U4 | CF para 14(1)–(2); DPDP s.8(7) | LAW |
| 35 | `data_destruction_policy` | Storage and destruction policy | footer | CF para 14(2) | LAW |
| 36 | `what_udofin_can_access` | What Udofin can access on this phone | U25, Settings | CF para 13(1) | LAW |
| 37 | `no_contacts_access` | We never read your contacts | Safety | CF para 13(1) | LAW |
| 38 | `no_sms_access` | We never read your SMS | Safety | CF para 13(1) | LAW |
| 39 | `camera_one_time` | Camera for KYC only, one time | U5 | CF para 13(1) | LAW |
| 40 | `location_coarse` | Approximate location, once | U3 | CF para 13(1) | INTERP |
| 41 | `biometric_not_stored` | We do not store biometrics | U5 | CF para 14(3) | LAW |
| 42 | `third_party_list` | Who else receives your data | U4, footer | CF para 14(2); DPDP s.5 | LAW |
| 43 | `data_access_request` | Request a copy of your data | UB1 | DPDP s.11 | LAW |
| 44 | `data_correction_request` | Correct or update your data | UB1 | DPDP s.12 | LAW |
| 45 | `data_erasure_request` | Erase your data | UB1 | DPDP s.12(3) | LAW |
| 46 | `nomination_dpdp` | Nominate someone to act for you | UB1 | DPDP s.14 [VERIFY] | LAW |
| 47 | `data_request_clock` | Response time for data requests | UB1 | DPDP Rules r.14 [VERIFY] | LAW |
| 48 | `download_my_data` | Download my data | UB1 | Policy (DPDP has no portability right) | REC |
| 49 | `cookie_consent` | Cookies and tracking consent | public site | DPDP s.6; IT Rules | LAW |
| 50 | `marketing_consent` | Marketing messages consent (default No) | U16 | RBC Second Amendment 101G, 101I [VERIFY]; TCCCPR | LAW |
| 51 | `consent_manager` | Consent manager (DPDP) | U4 | DPDP s.2(g); Rules r.4 [VERIFY] | LAW |
| 52 | `privacy_dashboard` | Consents and privacy dashboard | U25 | CF paras 13–14 | REC |
| **C** | **Identity and KYC** | | | | |
| 53 | `kyc` | Know Your Customer (KYC) | U5 | KYC Directions | LAW |
| 54 | `kyc_decision_by_lender` | The lender completes your KYC | U5 | KYC para 13; OUT para 15 | LAW |
| 55 | `okyc_digilocker` | DigiLocker / offline Aadhaar verification | U5 | KYC paras 16–17 [VERIFY] | LAW |
| 56 | `aadhaar_otp_ekyc` | Aadhaar OTP e-KYC (notified lenders only) | U5 | PML Act s.11A; KYC | LAW |
| 57 | `ckyc` | Central KYC Registry (CKYCR) | U5 | KYC para 56 et seq. [VERIFY] | LAW |
| 58 | `vcip` | Video KYC (V-CIP) | U5 | KYC para 18 [VERIFY] | LAW |
| 59 | `pan_verification` | PAN verification | U5 | KYC; Income-tax Act | LAW |
| 60 | `pan_aadhaar_link` | PAN–Aadhaar link status | U5 | Income-tax Act s.139AA | LAW |
| 61 | `masked_aadhaar` | Masked Aadhaar | U5 | Aadhaar Regulations | LAW |
| 62 | `face_match` | Face match | U5 | KYC V-CIP controls | INTERP |
| 63 | `liveness_check` | Liveness check | U5 | KYC V-CIP | INTERP |
| 64 | `bank_account_verification` | Bank account verification (penny drop) | U5 | KYC; NPCI | INTERP |
| 65 | `periodic_kyc_update` | Periodic KYC update | U5 | KYC para 38 [VERIFY] | LAW |
| 66 | `beneficial_owner` | Beneficial owner (business borrowers) | U5 | PML Rules r.9 | LAW |
| 67 | `mobile_otp` | One-time password (OTP) | U3 | DPS para 68 | LAW |
| 68 | `device_binding` | Device binding | U3 | DPS; MASVS | INTERP |
| 69 | `app_unlock` | App unlock (PIN or biometric) | U3 | DPS para 68 | REC |
| 70 | `passkey` | Passkey | U3 | WebAuthn L3; fut.passkeys-default | REC |
| 71 | `step_up_verification` | Extra verification for sensitive actions | U3, UB1 | DPS | REC |
| 72 | `trusted_devices` | Trusted devices | U3 | DPS | REC |
| 73 | `session_timeout` | Session timeout | U3 | DPS para 67(4) | LAW |
| 74 | `forced_update` | Minimum supported app version | U3 | DPS para 68(2) | LAW |
| 75 | `app_integrity` | App integrity check | U3, U24 | DPS para 68(5); MASVS | INTERP |
| 76 | `verify_this_app` | How to verify this is the real app | Safety | DPS para 68(5); CF para 18 | LAW |
| 77 | `assisted_mode` | Assisted mode (you keep the OTP) | MG4 | KYC; CF para 13 | INTERP |
| 78 | `authorised_signatory` | Authorised signatory | U3 | Companies Act 2013 | LAW |
| **D** | **Credit data and eligibility** | | | | |
| 79 | `credit_bureau` | Credit information company (CIC) | U6 | CIR paras 3–6 | LAW |
| 80 | `credit_report` | Credit report | U6, FW1 | CIR; CICRA 2005 | LAW |
| 81 | `credit_score` | Credit score | U6, FW1 | CIC Regulations | LAW |
| 82 | `bureau_pull_by_lender` | The lender pulls your report | U6 | CIR para 6; CICRA s.17 | LAW |
| 83 | `hard_vs_soft_enquiry` | Enquiry types | U6 | CIC practice | REC |
| 84 | `free_annual_credit_report` | Free full credit report once a year | FW1 | RBI circular 2016 [VERIFY] | LAW |
| 85 | `account_aggregator` | Account Aggregator (AA) | U6 | AA Directions | LAW |
| 86 | `aa_consent_artefact` | AA consent artefact | U6 | AA para 6 | LAW |
| 87 | `fiu` | Financial information user (the lender) | U6 | AA para 3 | LAW |
| 88 | `bank_statement` | Bank statement (via AA or upload) | U6 | AA; CF para 13 | INTERP |
| 89 | `income_assessment` | Income assessment | U6 | CF para 6; MFI para 12 | LAW |
| 90 | `affordability` | Can you afford this loan (FOIR) | U6 | RBC; MFI para 13 (50% cap) | LAW |
| 91 | `household_income` | Household income (microfinance) | MG2 | MFI paras 10–13 | LAW |
| 92 | `eligibility_prefilter` | Eligibility pre-check (lender's rules) | U7 | OUT para 15; Part 10.2 principle 19 | INTERP |
| 93 | `rule_version` | Lender rule version | U7 | Part 10.2 principle 26 | REC |
| 94 | `routing` | Which lenders see your application | U7 | CF para 7 | LAW |
| 95 | `unmatched_lender` | Lenders that did not match, and why | U8 | CF para 7(3) | LAW |
| 96 | `over_indebtedness` | Over-indebtedness | U6, FW | MFI para 13; RBC | LAW |
| 97 | `cic_reporting` | Reporting your loan to credit bureaus | U12 | CIR paras 7–9 | LAW |
| 98 | `credit_dispute` | Disputing your credit report | UB3 | CIR paras 34–35; CICRA s.21 | LAW |
| **E** | **Offers, KFS and cooling-off** | | | | |
| 99 | `offer` | Loan offer | U8 | CF para 7 | LAW |
| 100 | `offer_view_neutral` | Why offers appear in this order | U8 | CF para 7(4) | LAW |
| 101 | `ranking_metric` | Ranking metric (APR low to high) | U8, footer | CF para 7(4) | LAW |
| 102 | `no_sponsored_ranking` | No paid placement | U8 | CF para 7(4); RV4 | LAW |
| 103 | `kfs` | Key Facts Statement (KFS) | U8 | CF para 9; RBC para 29 | LAW |
| 104 | `kfs_validity` | KFS validity period | U8 | RBC para 29(2) | LAW |
| 105 | `apr` | Annual Percentage Rate (APR) | U8 | RBC para 29; Annex KFS | LAW |
| 106 | `apr_computation` | How APR is computed | U8 | RBC Annex (APR formula) | LAW |
| 107 | `interest_rate` | Interest rate | U8 | RBC para 29 | LAW |
| 108 | `fixed_vs_floating` | Fixed or floating rate | U8 | RBC para 30 [VERIFY] | LAW |
| 109 | `processing_fee` | Processing fee | U8 | RBC para 29; KFS | LAW |
| 110 | `insurance_charges` | Insurance charges (optional only) | U8, XP2 | RBC 101V–101W [VERIFY] | LAW |
| 111 | `penal_charges` | Penal charges (not penal interest) | U8 | RBC paras 34–38 [VERIFY] | LAW |
| 112 | `foreclosure_charges` | Foreclosure and prepayment charges | U8, U12 | RBC para 40 [VERIFY] | LAW |
| 113 | `contingent_charges` | Contingent charges | U8 | KFS Annex | LAW |
| 114 | `net_disbursed_amount` | Amount you will receive | U8 | KFS Annex; CF para 10(5) | LAW |
| 115 | `tenor` | Tenor | U8 | KFS | LAW |
| 116 | `emi` | Equated monthly instalment (EMI) | U8 | KFS | LAW |
| 117 | `repayment_schedule` | Repayment schedule | U8, U12 | KFS Annex | LAW |
| 118 | `amount_in_words` | Amount in words | U8 | RBC para 10; IPB-06-44 | REC |
| 119 | `kfs_acknowledgement` | Acknowledging the KFS | U8 | RBC para 29; CF para 9(2) | LAW |
| 120 | `explanation_acknowledged` | "I understand" explanation step | U8 | RBC para 10 | INTERP |
| 121 | `sanction_letter` | Sanction letter | U8, U9 | CF para 9(3) [VERIFY] | LAW |
| 122 | `cooling_off_period` | Cooling-off period | U8 | CF para 11 | LAW |
| 123 | `exit_during_cooling_off` | Exit the loan during cooling-off | U8 | CF para 11(1)–(2) | LAW |
| 124 | `cooling_off_payable` | What you pay if you exit | U8 | CF para 11(2) | LAW |
| 125 | `no_auto_increase` | No automatic credit-limit increase | U8 | CF para 6(2) [VERIFY] | LAW |
| 126 | `look_alike_offer` | Offers are the lender's, not Udofin's | U8 | CF paras 7, 9 | LAW |
| 127 | `store_filtered_offer` | Not available in this app; available on web | U8 | Google Play / App Store policy | REC |
| 128 | `single_lender_pack` | This app shows one lender's products | IB3 | CF para 7 [INTERP: legal opinion] | INTERP |
| 129 | `dark_patterns` | No pressure tactics (dark patterns) | U8 | CCPA Dark Patterns Guidelines 2023; CF para 7(4) | LAW |
| 130 | `offer_expiry_date` | Offer valid until (date, not timer) | U8 | G.1 rule 3 | REC |
| 131 | `loan_agreement` | Loan agreement | U9 | CF para 9(3); Contract Act | LAW |
| 132 | `most_important_terms` | Most important terms and conditions | U8 | RBC para 10 | LAW |
| **F** | **Documents and signing** | | | | |
| 133 | `esign` | eSign (Aadhaar-based electronic signature) | U9 | IT Act s.3A; Sch II | LAW |
| 134 | `estamp` | eStamp | U9 | State Stamp Acts | LAW |
| 135 | `digital_signature_certificate` | Digital signature certificate | U9 | IT Act s.35 | LAW |
| 136 | `signing_evidence` | Signing evidence (audit trail) | U9 | IT Act s.65B; CF para 9(3) | LAW |
| 137 | `document_hash` | Document fingerprint (hash) | U9, UB1 | IT Act s.65B | INTERP |
| 138 | `signed_copy_delivery` | Your signed copy | U9 | CF para 9(3) | LAW |
| 139 | `watermark` | Watermark on web documents | UB1 | Security floor | REC |
| 140 | `signed_url` | Download link validity | UB1 | G.10.2 floor 15 min | REC |
| 141 | `my_documents` | My documents | UB1 | CF para 9(3) | LAW |
| 142 | `statement_of_account` | Statement of account | UB1 | RBC | LAW |
| 143 | `interest_certificate` | Interest certificate | UB2 | Income-tax Act 2025 | LAW |
| 144 | `tds_certificate_form_131` | TDS certificate (Form 131) | UB2 | Income-tax Act 2025 s.393 [VERIFY] | LAW |
| 145 | `gstin_business_details` | GSTIN and business details | UB2 | CGST Act 2017 | LAW |
| 146 | `no_objection_certificate` | No-dues / closure certificate | U12 | RBC para 43 [VERIFY] | LAW |
| **G** | **Repayments and mandates** | | | | |
| 147 | `pay_to_lender_only` | Payments go to the lender, never Udofin | U11 | CF para 10(2)–(3) | LAW |
| 148 | `enach_mandate` | eNACH mandate | U11 | NPCI NACH rules | LAW |
| 149 | `upi_autopay` | UPI AutoPay | U11 | NPCI UPI AutoPay | LAW |
| 150 | `mandate_amount_cap` | Mandate maximum amount | U11 | NPCI | LAW |
| 151 | `afa_threshold` | Extra authentication above ₹15,000 | U11 | RBI e-mandate circulars; [VERIFY NPCI] | LAW |
| 152 | `pre_debit_notification` | Pre-debit notification | U11 | RBI e-mandate framework | LAW |
| 153 | `mandate_pause_cancel` | Pause or cancel a mandate | U11 | NPCI; RBI | LAW |
| 154 | `payment_link` | Payment link (lender's gateway) | U11 | PA Directions 2025 | LAW |
| 155 | `upi_intent_qr` | Pay by UPI | U11 | NPCI | LAW |
| 156 | `payment_status_pending` | Payment pending / under reconciliation | U11 | Part 5.5 | REC |
| 157 | `payment_receipt` | Receipt from the lender | U11 | RBC | LAW |
| 158 | `due_date` | Due date | U12 | KFS | LAW |
| 159 | `grace_period` | Grace period | U12 | Lender policy | INTERP |
| 160 | `part_prepayment` | Part prepayment | U12 | RBC para 40 [VERIFY] | LAW |
| 161 | `foreclosure` | Foreclosure | U12 | RBC para 40 [VERIFY] | LAW |
| 162 | `overdue_amount` | Overdue amount (lender's figure) | UR1 | Part 10.2 principle 28 | INTERP |
| 163 | `dpd` | Days past due (DPD) | U12 | IRACP | LAW |
| 164 | `sma_classification` | SMA-0/1/2 and NPA | U12 | IRACP paras [VERIFY] | LAW |
| 165 | `bounce_charges` | Mandate failure charges | U11 | RBC penal charges | LAW |
| 166 | `reconciliation` | Reconciliation with the lender | U11 | OUT para 39 | LAW |
| 167 | `refund_excess` | Refund of excess payment | U11 | RBC | LAW |
| 168 | `payment_disputes` | Disputed payment | UB3 | PA Directions; RBC | LAW |
| **H** | **Loan servicing** | | | | |
| 169 | `service_request` | Service request | U12 | RBC | REC |
| 170 | `address_change` | Change of address or contact | U12, U3 | KYC | LAW |
| 171 | `disbursement_status` | Disbursement status (UTR) | U10 | CF para 10 | LAW |
| 172 | `utr` | UTR (transaction reference) | U10 | NPCI/RBI | REC |
| 173 | `disbursement_to_your_account` | Disbursed to your bank account only | U10 | CF para 10(1) | LAW |
| 174 | `loan_closure` | Loan closure | U12 | RBC para 43 [VERIFY] | LAW |
| 175 | `security_release` | Release of security documents | U18 | RBC para 43 [VERIFY] | LAW |
| 176 | `restructuring` | Restructuring (lender decision) | U12 | RSA Directions | LAW |
| 177 | `moratorium` | Moratorium | U12 | RBI circulars | LAW |
| 178 | `top_up_not_offered_by_udofin` | Udofin does not offer top-ups | U12 | CF para 6(2); IB1.3 | INTERP |
| 179 | `loan_account_number` | Loan account number | U12 | — | REC |
| 180 | `charges_paid_to_date` | Charges you have paid | U25 | RBC | REC |
| 181 | `financial_dashboard` | Your money overview | U25 | — | REC |
| 182 | `statement_line_explainer` | What this line means | U25, IB1 | — | REC |
| 183 | `servicing_after_exit` | Access after the lender leaves Udofin | UP5 | OUT para 97; UP5 | INTERP |
| 184 | `las_margin_call` | Margin call (loan against securities) | Part 6.5 | RBI LAS norms [VERIFY] | LAW |
| **I** | **Collections and recovery** | | | | |
| 185 | `payment_reminder` | Payment reminder | U13 | RBC para 100 | LAW |
| 186 | `contact_hours` | Contact hours 08:00–19:00 | UR4 | RBC para 100 | LAW |
| 187 | `recovery_agent` | Recovery agent | UR4 | RBC paras 91, 100; CF para 9(6) | LAW |
| 188 | `verify_an_agent` | Verify a recovery agent | UR4 | CF para 9(6) | LAW |
| 189 | `agent_authorisation_letter` | Agent authorisation letter | UR4 | RBC para 100 | LAW |
| 190 | `no_harassment` | Your protection from harassment | UR6 | RBC paras 91, 100 | LAW |
| 191 | `no_third_party_contact` | No contact with your family or contacts | UR6 | RBC para 100; CF para 13(1) | LAW |
| 192 | `call_recording` | Recorded calls | RA5 | RBC pack B para 100P [VERIFY] | LAW |
| 193 | `settlement_offer` | Settlement offer (lender's) | UR1 | RBC; Board policy | LAW |
| 194 | `promise_to_pay` | Promise to pay | UR1 | Lender policy | INTERP |
| 195 | `hardship` | Financial hardship | UR1 | RBC | REC |
| 196 | `legal_notice` | Legal notice from the lender | UR3 | SARFAESI s.13(2); IBC; CPC | LAW |
| 197 | `sarfaesi` | SARFAESI (secured loans) | UR3 | SARFAESI Act 2002 | LAW |
| 198 | `wilful_defaulter` | Wilful defaulter | UR1 | WD Directions | LAW |
| 199 | `cash_receipt_rules` | Cash collection rules | MG4 | CF para 10(5); IT Act s.269ST | LAW |
| 200 | `recovery_complaint` | Complain about recovery conduct | UB3 | RBC para 100; CF para 12 | LAW |
| **J** | **Default loss guarantee (DLG)** | | | | |
| 201 | `dlg` | Default loss guarantee (DLG) | U14 | CF paras 20–28 | LAW |
| 202 | `dlg_cap_5pct` | DLG cap of 5% | U14 | CF para 24 | LAW |
| 203 | `dlg_disclosure_monthly` | Monthly DLG disclosure | U14, footer | CF para 28 | LAW |
| 204 | `dlg_does_not_affect_you` | DLG does not change your loan | U14 | CF para 20 | INTERP |
| 205 | `dlg_provider` | DLG provider | U14 | CF para 20(3) | LAW |
| 206 | `dlg_invocation` | DLG invocation | U14 | CF para 25 | LAW |
| 207 | `dlg_form` | Form of DLG (cash, FD, BG) | U14 | CF para 22 | LAW |
| 208 | `dlg_portfolio` | DLG portfolio (set) | U14 | CF para 23 | LAW |
| **K** | **Grievance** | | | | |
| 209 | `raise_a_complaint` | Raise a complaint | UB3 | CF para 12 | LAW |
| 210 | `complaint_reference` | Complaint reference | UB3 | RBC para 7 | REC |
| 211 | `forwarded_to_lender` | Forwarded to the lender | UB3 | CF para 12(4) | LAW |
| 212 | `lender_30_day_clock` | Lender's 30-day period | UB3 | CF para 12(4) | LAW |
| 213 | `internal_ombudsman` | Internal Ombudsman (IO) | UB3 | IO Directions 2026 [VERIFY] | LAW |
| 214 | `rbi_ombudsman` | RBI Ombudsman | UB3 | RB-IOS 2026 cl.10 [VERIFY] | LAW |
| 215 | `ombudsman_90_day_window` | 90-day window to approach the Ombudsman | UB3 | RB-IOS 2026 [VERIFY] | LAW |
| 216 | `cms_portal` | RBI Complaint Management System | UB3 | RB-IOS 2026 | LAW |
| 217 | `escalation_chain` | Escalation chain | UB3 | CF para 12; RB-IOS | LAW |
| 218 | `priority_tags` | Priority (recovery conduct, fraud, disability) | UB3 | RBC; RPwD | INTERP |
| 219 | `reopen_complaint` | Reopen a complaint | UB4 | RBC para 7 | REC |
| 220 | `rate_resolution` | Rate the resolution | UB4 | — | REC |
| 221 | `case_pack_download` | Download your case pack | UB4 | DPDP s.11 | REC |
| 222 | `equator_odr` | Online dispute resolution (Equator) | UR2 | Arbitration Act; Mediation Act 2023 | LAW |
| 223 | `odr_referral_by_lender` | ODR only on the lender's referral | UR2 | Part 7A UR2 | INTERP |
| 224 | `consumer_commission` | Consumer Commission (e-Daakhil) | UB3 | Consumer Protection Act 2019 | LAW |
| 225 | `data_protection_board` | Data Protection Board of India | UB3 | DPDP s.18 [VERIFY date] | LAW |
| 226 | `insurance_complaint_route` | Insurance complaint route | XP2 | IRDAI; Bima Bharosa | LAW |
| 227 | `credit_information_complaint` | Credit information complaint (21/30 days) | UB3 | CIR paras 34–35 | LAW |
| 228 | `voice_note_complaint` | Complain by voice note | UB4 | RBC para 10 | REC |
| 229 | `complaint_status` | Complaint status meanings | UB3 | — | REC |
| 230 | `grievance_officer_it_rules` | Grievance officer (website) | public | IT Rules 2021 r.3(2) | LAW |
| **L** | **Wellness, products and plans** | | | | |
| 231 | `money_tools_separate` | Money tools are separate from loans | FW4 | CF paras 10(4), 14(1); FW4 | INTERP |
| 232 | `score_simulator_educational` | Score simulator is educational | FW2 | CIC Regulations | INTERP |
| 233 | `expense_tracker_manual` | Expense tracker (manual entry only) | FW3 | CF para 13(1) | INTERP |
| 234 | `consumer_plan` | Consumer plan (optional, not loan-related) | RV2 | CF para 10(4) [INTERP: legal opinion] | INTERP |
| 235 | `free_plan_never_auto_converts` | Trials never auto-convert | RV2 | CCPA Guidelines | REC |
| 236 | `cancel_in_one_tap` | Cancel in one tap | RV2 | CCPA; RBC 101M [VERIFY] | LAW |
| 237 | `proration` | Proration on plan change | RV2 | Contract; GST | INTERP |
| 238 | `gst_on_plan` | GST on plans | RV2 | CGST Act 2017 | LAW |
| 239 | `advertising_label` | Why am I seeing this ad | RV4 | ASCI Code; CCPA | LAW |
| 240 | `insurance_optional` | Insurance is optional, never bundled | XP2 | RBC 101V [VERIFY]; IRDAI | LAW |
| 241 | `free_look_period` | Free-look period (insurance) | XP2 | IRDAI Protection of Policyholders Regs | LAW |
| 242 | `society_membership` | Society membership (co-operatives) | MG1 | MSCS Act; State Acts | LAW |
| **M** | **Accessibility, AI and app** | | | | |
| 243 | `read_aloud` | Read aloud | all | RBC para 10; IPB-06 | REC |
| 244 | `easy_read_mode` | Easy-read mode | all | IPB-06 §06.3.6 | REC |
| 245 | `captions` | Captions | all | IPB-06 hearing | REC |
| 246 | `live_captions_voice` | Live captions during voice support | IB1 | IPB-06 | REC |
| 247 | `visual_alerts` | Visual alerts | all | IPB-06 | REC |
| 248 | `language_switch` | Change language | all | RBC paras 10, 29(1) | LAW |
| 249 | `lite_mode` | Lite mode (low data) | all | G.1 rule 11 | REC |
| 250 | `offline_read_only` | Offline (read-only) | all | G.1 rule 11 | REC |
| 251 | `screenshot_blocked` | Why screenshots are blocked here | all | G.1 rule 12 | REC |
| 252 | `ai_assistant_disclosure` | Vidhi is an AI assistant, not a person | IB1 | RA5.4; FREE-AI; IT Rules (synthetic content) [VERIFY] | LAW |
| 253 | `ai_never_decides` | The AI never decides your loan | IB1 | OUT para 15; U20 | LAW |
| 254 | `talk_to_a_person` | Talk to a person | IB1, RA5 | RA5.5 | REC |
| 255 | `ai_conversation_history` | Your conversation history | IB1 | DPDP s.8 | LAW |
| 256 | `explain_why` | Why we ask for this | all | CF para 13(3) | LAW |
| 257 | `one_primary_action` | One main action per screen | all | Part 3.3 | REC |
| 258 | `resume_banner` | Continue where you left off | U3 | Part 3.3 | REC |
| 259 | `feedback_widget` | Give feedback | IB2 | — | REC |
| 260 | `whats_new` | What's new | IB2 | — | REC |
| 261 | `tutorial` | Tutorials and tours | IB2 | — | REC |
| 262 | `about_this_app` | About this app (version, legal entity) | G.14 | CF para 9(5); Companies Act s.12 | LAW |

**Lint and coverage rules.** `plain` ≤ 40 words; every KFS line item, consent artefact and acceptance control must reference a key in groups B, E or F; every status badge in groups G–K; CI `hlp-coverage` fails below 100% for KFS, consent and acceptance screens and below 90% for other borrower screens at Phase 22 exit. Claude Code may add keys (continuing the sequence under each group) but never renames or deletes a published key; deprecated keys get `superseded_by`.
