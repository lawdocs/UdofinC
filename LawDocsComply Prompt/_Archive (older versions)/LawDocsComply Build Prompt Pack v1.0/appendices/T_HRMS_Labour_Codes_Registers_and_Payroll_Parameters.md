# Appendix T — HRMS, Labour Codes, Registers and Payroll Parameters

> Binding for P13 (client HRMS and labour compliance) and referenced by P04 (labour obligations), P06 (committees, KMP), P12 (employee privacy), P14 (employee routes away from customer desk), P20 (People & Labour SKU entitlements). Prepared 25 October 2026.
>
> **Precedence.** For any statutory value, the signed shared rule pack `infrabyx-labour-rulepack` (Infrabyx Ecosystem Integration Specification v1.1 §12.3) and its companion `ita25-salary-tds` prevail over this appendix; this appendix is the seed and the LDC-side contract for consuming the pack. Where this appendix and the Equator Pack v3.1 Appendix Z differ, the rule pack decides and both are corrected through the pack's change process (maker-checker by Infrabyx labour-law reviewer and payroll lead).
>
> **Status markers.** `VERIFIED` (gazette/official guidance checked), `SECONDARY_ONLY` (reputable secondary source only — usable with per-run acknowledgement), `NOT_CONFIRMED` (cannot drive a statutory output; run blocked until resolved or a dated professional opinion is recorded). Seed statuses below are as recorded in the Equator v3.1 research (23–24 October 2026) and the Ecosystem Specification, re-stated for LDC; they must be re-verified at LDC go-live (OI-P13-01–06).

---

## T.0 How LDC consumes the rule pack

1. `contracts.lock` pins `infrabyx-labour-rulepack@<semver>` and `ita25-salary-tds@<semver>`. At load, LDC verifies the detached JWS signature (HSM-backed Infrabyx rule-pack key) and the per-file SHA-256 in `pack.json`; an unsigned or tampered pack is refused (`LDC-CFG-031`).
2. Pack documents (JSON Schema-validated YAML + CEL expressions) are materialised into `cfg.rule_params` with `param_code`, `jurisdiction` (`IN`, `IN-DL`, `IN-UP`, `IN-RJ`, `IN-MH`, `IN-KA`, …), `sphere` (`central`/`state`), `applies_to` (`worker`, `non_worker`, `fte`, `international_worker`, `apprentice`, `all`), `value` (scalar / slab table / formula ref), `unit`, `effective_from`, `effective_to`, `source_instrument`, `source_url`, `source_type` (`gazette`, `official_guidance`, `secondary`), `verification_status`, `verified_by`, `verified_on`, `review_due`.
3. Tenants may override only fields marked `x-tenant-overridable`, and only in the more-generous direction (validator `LDC-HR-021`).
4. Every payslip line, register row and statutory file stores the `param_version_id`s used (NN-22). Approved versions are immutable; a correction is a new version (NN-07).
5. CI runs the pack's golden fixtures; LDC output must equal Finbyx GV6 and OH10 outputs for the same fixtures (Ecosystem Spec §14.3 conformance).

---

## T.1 Legal baseline (as of 25 October 2026)

| Instrument | Status | Notes for the engine |
|---|---|---|
| Code on Wages 2019 (CoW) | In force 21 Nov 2025 (S.O. 5322(E)) | Wage definition s.2(y) with 50 % exclusion add-back; minimum wages; payment of wages (s.17 timelines); deductions (s.18, 50 % cap); bonus (Ch. IV); equal remuneration |
| Industrial Relations Code 2020 (IRC) | In force 21 Nov 2025 (S.O. 5320(E)) | Works Committee (s.3), Grievance Redressal Committee (s.4, ≥ 20 workers), standing orders (s.28–30, ≥ 300 workers), fixed-term employment, lay-off/retrenchment/closure (Ch. IX, X), re-skilling fund |
| Code on Social Security 2020 (CoSS) | In force 21 Nov 2025 (S.O. 5319(E), substantially) | EPF/EPS/EDLI (Schemes 2026), ESI, gratuity (ss.53–58), maternity, employees' compensation, crèche, gig/platform workers (not in LDC v1.0 scope) |
| Occupational Safety, Health and Working Conditions Code 2020 (OSH) | In force 21 Nov 2025 (S.O. 5321(E)) | Registration (≥ 10 workers), appointment letters (s.6(1)(f)), hours, overtime, annual leave (s.32), women night work, contract labour (Ch. XI), inter-State migrant workers, welfare |
| Central Rules 2026 | Notified 8 May 2026: Wages G.S.R. 343(E), IR G.S.R. 342(E), CoSS G.S.R. 344(E), OSH G.S.R. 345(E) [VERIFY OSH number]; corrigendum G.S.R. 629(E) of 15 Jul 2026 | Central sphere establishments; State-sphere establishments follow State rules |
| EPF/EPS/EDLI Schemes 2026 | Notified; corrigenda G.S.R. 703–705(E), 4 Aug 2026 | Wage ceiling change from 17 Sep 2026 (S.O. 5109(E)) [VERIFY gazette text] |
| State rules under the Codes | Most pending; old State rules continue so far as consistent (MoLE FAQ Q1) | `state_rule_status` per State and Code drives obligation text ("pending State rules") |
| State Shops and Establishments Acts | Continue | Hours, leave, holidays, registration, women night work per State |
| POSH Act 2013 and Rules 2013 | In force | IC/LC, timelines, annual report; Board-report disclosure (Companies (Accounts) Rules r.8(5)(x)) |
| Apprentices Act 1961 | In force | Apprentice classification; stipend; contract registration |
| Income-tax Act 2025 | In force 1 Apr 2026 | Salary TDS s.392; Income-tax Rules 2026 forms and due dates (several `NOT_CONFIRMED`) |
| Companies Act 2013 | In force | s.177(9)–(10) vigil mechanism; s.203 KMP; Sch. V remuneration; CSR staff; Board-report HR disclosures |
| Sector instruments affecting people controls | Various | e.g., RBI NBFC Cyber Directions 2026 paras 81–82 (CISO independence), RBI NBFC IO Directions 2026 cl.5, 8 (IO eligibility and tenure), compliance-function directions (CCO), PMLA Rules (Principal Officer, Designated Director) |

Engine rule (MoLE Additional FAQ Q25 approach): per employee per day, evaluate the union of applicable floors (Code + State S&E Act + contract + tenant policy) and apply the most favourable per entitlement.

---

## T.2 Applicability thresholds

Evaluated monthly on actual headcount per employing entity and establishment (counting basis per rule).

| Duty | Threshold | Source | Engine behaviour |
|---|---|---|---|
| Appointment letter to every employee | All employees; existing staff within 3 months | OSH s.6(1)(f) | Always issued; clock `osh_appointment_letter_existing_3m` |
| Minimum wage, timely payment, deductions cap, equal pay, wage slips, registers | All employees incl. managers (CoW s.2(k)) | CoW ss.3, 5, 15–18, 50 | Always on |
| OSH establishment registration; s.32 annual leave with wages | ≥ 10 workers | OSH ss.2(1)(v), 3, 32 | Auto-on at 10; registration task |
| ESI coverage | ≥ 10 persons; wage threshold ₹21,000/month | CoSS; MoLE FAQ | Auto-on at 10 |
| Gratuity | ≥ 10 employees | CoSS ss.53–58 | Provision always; statutory payout rules at 10 |
| POSH Internal Committee | ≥ 10 employees (below: Local Committee) | POSH Act ss.4, 6 | IC module required; validator |
| EPF/EPS/EDLI | ≥ 20 employees (voluntary below) | CoSS; Schemes 2026 | Auto-on at 20; voluntary switch |
| Bonus | ≥ 20 persons on any day in the accounting year | CoW s.41(2) | Auto-on at 20; ceilings `NOT_CONFIRMED` |
| Grievance Redressal Committee | ≥ 20 workers | IRC s.4 | Committee template (P06/P13) |
| Works Committee | ≥ 100 workers where appropriate Government orders | IRC s.3 | Task on order receipt |
| Crèche (or allowance ≥ ₹500/child/month) | ≥ 50 employees | CoSS; Central Rules | Task + allowance component |
| Standing orders | ≥ 300 workers | IRC s.28 | Certification workflow; below 300 model standing orders as template |
| Retrenchment prior permission (Ch. X) | ≥ 300 workers | IRC Ch. X | Workflow gate on retrenchment |
| Vigil mechanism (statutory) | Listed; accepts public deposits; or borrowed > ₹50 crore from banks/PFIs | Companies Act s.177(9)–(10); Companies (Meetings of Board) Rules r.7 | Derived flag; voluntary channel always available |
| Internal auditor (private company) | Turnover ≥ ₹200 crore or borrowings > ₹100 crore | Companies (Accounts) Rules r.13 | Fact for P10 |
| Internal Ombudsman (NBFC) | NBFC-D ≥ 10 branches; NBFC-ND ≥ ₹5,000 crore with public customer interface | RBI NBFC IO Directions 2026 cl.3 | Regulated-role vacancy check (P13) |

---

## T.3 Hours, overtime, leave and night work

### T.3.1 Central parameters

| `param_code` | Seed value | Effective | Status |
|---|---|---|---|
| `osh.daily_hours` / `osh.weekly_hours` | 8 / 48 | 21 Nov 2025 / 8 May 2026 | VERIFIED / SECONDARY_ONLY |
| `osh.overtime.rounding` | 15–30 min → 30 min; > 30 min → 1 h | 8 May 2026 | SECONDARY_ONLY |
| `osh.overtime.quarterly_cap_hours` | not set centrally (State values) | — | NOT_CONFIRMED (Central) |
| `cow.overtime_multiplier` | 2.0 | 21 Nov 2025 | VERIFIED |
| `osh.leave.eligibility_days` | 180 days worked in a calendar year | 21 Nov 2025 | VERIFIED |
| `osh.leave.accrual_ratio` | 1 day per 20 days worked | 21 Nov 2025 | VERIFIED |
| `osh.leave.carry_forward_cap` | 30 days | 21 Nov 2025 | VERIFIED |
| `osh.leave.encashment_timeline` | 2 working days (discharge, dismissal, quitting); 2 months (superannuation, death) | 21 Nov 2025 | VERIFIED |
| `osh.women_night_window` | before 06:00 / after 19:00 needs consent and safeguards | 21 Nov 2025 | VERIFIED |
| `osh.supervisory_wage_cap` | ₹18,000 per month (supervisory persons above are not "workers") | 21 Nov 2025 | VERIFIED |
| `coss.maternity.weeks` / `eligibility_days` / `medical_bonus` | 26 / 80 / ₹3,500 | 21 Nov 2025 | VERIFIED |

### T.3.2 Launch-State parameters (seed; all `SECONDARY_ONLY` unless noted; verify against State Gazette before first pay run)

| Item | Delhi | Uttar Pradesh | Rajasthan | Maharashtra | Karnataka |
|---|---|---|---|---|---|
| Daily / weekly hours | 9 / 48 | 9 / 48 (Amendment Act 2025, eff. 19 Nov 2025) | 10 / 48 (Bill No. 5 of 2026) | 10 / 48 (Ordinance 2025, eff. 1 Oct 2025; Act status NOT_CONFIRMED) | 9 / 48 |
| Overtime quarterly cap | NOT_CONFIRMED | 144 h | 144 h | 144 h per 3 months | NOT_CONFIRMED |
| Overtime rate | 2× | 2× | 2× (CoW s.14 supersedes S&CE 1.5× for covered employees [REC]) | 2× | 2× |
| Earned/privilege leave | 15 days/yr after 12 months; accumulate 45 | 15 days; accumulate 45 (NOT_CONFIRMED) | 1 per 12 days after 240 days; carry 30 | 1 per 20 days (18 after 240 days); accumulate 45 | 18 days/yr; carry 30 |
| Casual / sick leave | CL 12 + SL 12 (NOT_CONFIRMED) | CL 15; SL 5 or 15 (NOT_CONFIRMED) | none separate | CL 8 per calendar year, credited quarterly | SL 12 |
| Women night work | restricted (relaxation NOT_CONFIRMED) | 19:00–06:00 with consent and safeguards | check exemption notifications | 21:30–07:00 with consent | allowed |
| Professional tax | none | none | none | Men: nil ≤ ₹7,500; ₹175 (₹7,501–10,000); ₹200 above (₹300 in February); Women: nil ≤ ₹25,000 (older sources ₹10,000 — conflict), ₹200 above (₹300 Feb) | nil < ₹25,000; ₹200 (₹300 in February) |
| LWF | ₹1 / ₹2 monthly — applicability conflict (NOT_CONFIRMED) | no active private-sector LWF | NOT_CONFIRMED | ₹25 employee / ₹75 employer, half-yearly (June, December) | ₹50 / ₹100 annual (31 Dec); applies at 10 employees |
| S&E registration | conflict (NOT_CONFIRMED) | 20+ employees | within 30 days (small-establishment exemption NOT_CONFIRMED) | 20+ non-managerial; below 20 intimation | electronic, deemed in 7 days; 10+ OSH-registered workers excluded (Act 38/2026) |
| Service certificate | — | — | — | — | within 7 days |

Other States: PT and LWF rows seeded `SECONDARY_ONLY` from the shared pack's research table (WB, TN, GJ, TS/AP and others); States without PT (DL, UP, RJ, HR, UK, HP, …) seeded `value = none`. Locked validator: no PT slab may exceed ₹2,500 per person per year (Constitution Art. 276(2)).

**T.3.3 Additional State PT and LWF candidates (all `NOT_CONFIRMED` — candidate values to check against the State Act/Gazette; a pay run using them is blocked until verified, §T.4 run gate).**

| State | Professional tax (monthly salary slabs, candidate) | LWF (employee / employer, candidate) |
|---|---|---|
| Gujarat | nil up to ₹12,000; ₹200 above | ₹6 / ₹12 half-yearly (June, December) |
| West Bengal | nil up to ₹10,000; ₹110 (₹10,001–15,000); ₹130 (₹15,001–25,000); ₹150 (₹25,001–40,000); ₹200 above | ₹3 / ₹15 half-yearly |
| Telangana | nil up to ₹15,000; ₹150 (₹15,001–20,000); ₹200 above | ₹2 / ₹5 annual |
| Andhra Pradesh | nil up to ₹15,000; ₹150 (₹15,001–20,000); ₹200 above | ₹30 / ₹70 annual |
| Tamil Nadu | half-yearly slabs on half-yearly income, revised by local bodies (Chennai revision 2024) — load from the local-body notification | ₹20 / ₹40 annual (31 January) |
| Madhya Pradesh | annual: nil up to ₹2.25 lakh; ₹1,500 (₹2.25–3 lakh); ₹2,000 (₹3–4 lakh); ₹2,500 above | ₹10 / ₹30 half-yearly |
| Haryana | none | 0.2% of wages subject to a monthly cap, employer twice the employee share |
| Punjab | ₹200 per month above the threshold | ₹5 / ₹20 monthly |
| Kerala | half-yearly slabs levied by local bodies | per Kerala LWF Board schemes |

These rows exist so the State packs are not empty at launch; they are not seeds for computation until a reviewer changes their status with the Gazette reference (`02` §6; Appendix W).


---

## T.4 Payroll parameter seed

| Rule pack / `param_code` | Seed value | Effective | Status |
|---|---|---|---|
| `rulepack.IN.payroll.wage_definition` · `cow.wage_definition.exclusion_cap_pct` | 50 | 21 Nov 2025 | VERIFIED |
| `cow.in_kind_cap_pct` | 15 | 21 Nov 2025 | VERIFIED |
| `cow.monthly_pay_deadline_day` | before the 7th of the following month | 21 Nov 2025 | VERIFIED |
| `cow.separation_pay_working_days` | 2 | 21 Nov 2025 | VERIFIED |
| `cow.deduction_cap_pct` | 50 per wage period; excess carried forward | 21 Nov 2025 | VERIFIED (carry-forward SECONDARY_ONLY) |
| `cow.min_wage.daily_to_monthly_factor` | × 26; hourly = daily ÷ 8 | 8 May 2026 | SECONDARY_ONLY |
| `cow.bonus.min_pct` / `max_pct` / `min_amount` | 8.33 / 20 / ₹100 | 21 Nov 2025 | VERIFIED |
| `cow.bonus.eligibility_wage_ceiling` / `calc_ceiling` | not set | — | NOT_CONFIRMED (CoW s.26 ceilings not notified) |
| `cow.records.retention_years` | 5 after last entry | 8 May 2026 | SECONDARY_ONLY |
| `coss.epf.wage_ceiling` | ₹15,000 to 16 Sep 2026; ₹25,000 from 17 Sep 2026 | 17 Sep 2026 | SECONDARY_ONLY (S.O. 5109(E)) |
| `coss.epf.ee_rate` / `er_rate` | 12 / 12 (employer: EPS 8.33 on wages up to ceiling + EPF 3.67); 10 % classes as notified | 2026 Schemes | SECONDARY_ONLY |
| `coss.edli.rate` / `coss.epf.admin_rate` | 0.50 / 0.50 | 2026 Schemes | SECONDARY_ONLY |
| `coss.epf.split_month_method` | Sep 2026: ₹15,000 for 1–16 Sep, ₹25,000 for 17–30 Sep, pro rata by calendar day | 1 Sep 2026 | SECONDARY_ONLY (EPFO guidance awaited) |
| `coss.epf.iw_ceiling_applies` | false (International Workers: 12 % of entire wages) | 2026 Schemes | SECONDARY_ONLY |
| `coss.esi.wage_threshold` | ₹21,000 | 21 Nov 2025 | VERIFIED |
| `coss.esi.ee_rate` / `er_rate` | 0.75 / 3.25 | — | SECONDARY_ONLY |
| `coss.gratuity.days_per_year` / `divisor` / `ceiling` | 15 / 26 / ₹20,00,000 | 21 Nov 2025 | VERIFIED (ceiling notification to verify) |
| `coss.gratuity.min_service_years` / `fte_min_service_years` | 5 / 1 | 21 Nov 2025 | VERIFIED |
| `coss.creche.threshold` / `allowance_min` | 50 / ₹500 per child per month | 8 May 2026 | VERIFIED / SECONDARY_ONLY |
| `irc.grc_threshold` / `standing_orders_threshold` | 20 / 300 | 21 Nov 2025 | VERIFIED |
| `irc.retrenchment.notice_months` / `comp_days_per_year` / `reskilling_days` | 1 (Ch. IX, 50–299) / 3 (Ch. X, 300+); 15; 15 | 21 Nov 2025 | VERIFIED |
| `itax.salary_tds_section` | Income-tax Act 2025 s.392 | 1 Apr 2026 | VERIFIED |
| `itax.default_regime.slabs` (TY 2026-27) | 0–4 L 0 %; 4–8 L 5 %; 8–12 L 10 %; 12–16 L 15 %; 16–20 L 20 %; 20–24 L 25 %; > 24 L 30 % | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.standard_deduction.default` / `.old` | ₹75,000 / ₹50,000 | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.rebate.default` | income ≤ ₹12,00,000 → min(tax, ₹60,000), marginal relief above (s.156(2)) | 1 Apr 2026 | VERIFIED |
| `itax.cess_pct` | 4 | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.employer_nps_deduction_pct` | 14 (s.124) | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.form123_salary_threshold` | ₹1,50,000 (perquisite statement) | 1 Apr 2026 | VERIFIED (r.204(2)) |
| `itax.deposit_due_dates`, `itax.late_fee` | per Income-tax Rules 2026 | — | NOT_CONFIRMED |
| `minwage.central.*` (from 1 Oct 2026) | Area A daily: unskilled ₹840; semi-skilled ₹933; skilled/clerical ₹1,024; highly skilled ₹1,111 | 1 Oct 2026 | SECONDARY_ONLY (central sphere only) |
| `minwage.IN-<ST>.*` | load from State notifications (VDA cycles 1 Apr / 1 Oct) | — | NOT_CONFIRMED until loaded |

**Run gate (Locked).** A pay run cannot be checked or finalised if any parameter it uses is `NOT_CONFIRMED` (`LDC-HR-040`); `SECONDARY_ONLY` parameters require the named Payroll Compliance Officer's acknowledgement per run (`LDC-HR-041`). A legally required `NOT_CONFIRMED` value is resolved only by verification against the Gazette or a dated professional opinion — the system never invents a value.

### T.4.1 Statutory component classes (Locked logic)

| Class | Counted in CoW wages (s.2(y))? | Examples |
|---|---|---|
| `WAGE_CORE` | Yes | Basic, dearness allowance, retaining allowance |
| `WAGE_EXCLUDED_50` | Excluded, subject to 50 % add-back | HRA, conveyance, overtime allowance, commission, statutory bonus, employer PF/pension contribution [VERIFY treatment list] |
| `NOT_REMUNERATION` | Excluded entirely | Gratuity on termination, retrenchment compensation, value of house accommodation/amenities as specified [VERIFY], reimbursements of actual expenses |
| `IN_KIND` | Counted up to 15 % cap | Specified in-kind benefits |
| `DEDUCTION_STATUTORY` | — | Employee PF, ESI, PT, LWF, TDS |
| `DEDUCTION_PERMITTED` | — | Advances, loans, fines (with procedure), society dues — within 50 % cap |

`wage_code_base()` is a pure function with golden fixtures; formula: `base = WAGE_CORE + IN_KIND_capped + max(0, WAGE_EXCLUDED_50 − 0.5 × total_remuneration)`.

---

## T.5 Statutory registers, returns and displays

Formats come from the Central Rules 2026 (central sphere) and State rules (State sphere) — form numbers are recorded in the pack once verified (`form_no` [VERIFY] below). LDC generates each as a view over source data, with version, hash and signatory.

### T.5.1 Registers

| Register | Code / rule | Data source in LDC | Frequency | Retention |
|---|---|---|---|---|
| Register of employees/workers (unified) — **Form I** Employee Register under the Wages (Central) Rules (central sphere) | OSH Code + Central/State Rules; CoW (Central) Rules 2026 r.51; S&E Act | `hr.employments`, `hr.assignments` | Continuous | per rule (default 5 years after last entry — SECONDARY_ONLY) |
| Register of wages (incl. deductions, advances, overtime) — **Form IV** (central sphere) | CoW + Code on Wages (Central) Rules 2026 r.51 | `hr.pay_lines` | Each wage period | 5 years (SECONDARY_ONLY) |
| Muster roll / attendance register — **Form IX** Attendance Register-cum-Muster Roll (central sphere) | CoW (Central) Rules 2026 r.51; OSH rules | `hr.attendance_days` | Daily | 5 years |
| Overtime register | OSH + CoW | `hr.attendance_days.ot_minutes`, consent records | Each period | 5 years |
| Leave register (annual leave with wages) | OSH s.32 + rules | `hr.leave_balances`, `hr.leave_requests` | Continuous | 5 years |
| Register of fines and deductions for damage/loss | CoW s.18 + rules (show-cause 7 days; impose and intimate 15 days — r.16 [VERIFY]) | `hr.pay_lines` (deduction codes), disciplinary records | As occurs | 5 years |
| Register of advances | CoW rules | `hr.loans` | As occurs | 5 years |
| Bonus register (computation of allocable/available surplus, bonus paid) | CoW Ch. IV + rules | bonus run | Annual | 5 years |
| Maternity benefit register | CoSS + rules | leave + payroll | As occurs | per rules |
| Gratuity nomination register / nominations | CoSS + gratuity rules | `hr.nominations` | As occurs | life of employment + |
| Register of accidents and dangerous occurrences | OSH + rules (where applicable) | incident intake (P12) for workplace incidents | As occurs | per rules |
| Contractor and contract-labour register (principal employer) | OSH Ch. XI + rules | `lab.contractors_deployments` | Continuous | per rules |
| Register of complaints (GRC) | IRC s.4 + rules | P13 GRC committee module | As occurs | per rules |
| Register of Internal Committee complaints (sealed; counts outside IC) | POSH Act + Rules | `lab_posh.cases` | As occurs | tenant policy, default 8 years [REC] |
| Register of apprentices | Apprentices Act | `hr.employments` (type apprentice) | Continuous | per Act |

**Additional central-rule points (secondary sources, 12 May 2026; `SECONDARY_ONLY` until the Gazette text is read).**

| Item | Rule (Central Rules 2026) | LDC behaviour |
|---|---|---|
| Wage slip | **Form V**, issued on or before payment of wages (Wages r.52) | Payslip template conforms to Form V fields |
| Other Wages forms | Form II (single claim application s.45(5)), III (appeal s.49(1)), VI (composition), VII (nomination for undisbursed dues), VIII (notices) | Generated on demand from the claims/appeals register |
| Wage returns | Filed electronically in the forms under the OSH Code (Wages r.48) — no separate wage return | One annual-return data set feeds both |
| Rest day | One per week; no more than 10 consecutive days without rest (Wages r.6) | Roster validator (P13) |
| Fines | Notice, 7 days to show cause, impose and intimate within 15 days (Wages r.16) | Disciplinary workflow clocks |
| Service record | **Form (ii)** under IR (Central) Rules, electronic or manual, updated with the worker's knowledge | Service-book view of `hr.employments` |
| Displays | Working hours, shifts, holidays, pay days and wage rates in Hindi, English and the local language (IR Central Rules) | Notice generator in three languages (P07 translation, human-reviewed) |
| Re-skilling fund | 15 days' last-drawn wages per retrenched worker, transferred within 10 days to the prescribed account; credited to the worker within 45 days of separation | Retrenchment settlement clock and payment task |
| Gig/platform workers | Aggregators register workers on the designated portal within 45 days (CoSS Central Rules) | Applies only to tenants flagged as aggregators |
| Health examination | Free annual examination for employees over 40 in notified establishments (OSH Central Rules) | Task generator where the establishment type is notified |
| Appointment letter | Prescribed format (OSH Central Rules) | Employment-document template EMP-01 aligned (§T.12) |
| Model Standing Orders | Establishments with ≥ 300 workers align with the Model Standing Orders for manufacturing, mines or services (IR Central Rules) | Standing-orders task at threshold |

### T.5.2 Returns and statutory files

| Return / file | Authority / portal | Frequency / due | LDC output |
|---|---|---|---|
| EPF Electronic Challan-cum-Return (ECR) | EPFO Unified Portal | Monthly, by the 15th of the following month | ECR text file per EPFO layout + reconciliation |
| ESIC contributions | ESIC portal | Monthly contribution by the 15th [VERIFY]; half-yearly returns where applicable | Upload file + challan data |
| Professional tax returns | State portals (MH, KA, WB, TN, GJ, …) | per State | Return data sheet per State layout |
| LWF returns | State boards | per State (e.g., MH June/December; KA annual 31 Dec) | Data sheet |
| Annual return under OSH/CoW/CoSS Rules | Shram Suvidha / State portal | Annual (format status `FORMAT_PENDING` until mapped) | Data sheet + PDF |
| Bonus annual return | Per CoW rules | Annual [VERIFY form] | Data sheet |
| POSH annual report | District Officer (POSH Rules r.14) and in employer's annual report | Annual (calendar year [VERIFY]) | DOCX/PDF from counts |
| Salary TDS quarterly statement | Income-tax (TRACES / e-filing) | Quarterly (Income-tax Rules 2026 form — Form 138 per research [VERIFY]) | Data file for official validation utility |
| Annual salary TDS certificate to employees | Income-tax | Annual (Form 130 by 15 June [VERIFY]) | Certificates PDF |
| Contract labour returns (principal employer) | Per OSH rules | Annual [VERIFY] | Data sheet |
| Apprenticeship returns | Apprenticeship portal | per rules | Data sheet |

### T.5.3 Notices to be displayed

Abstracts of the Codes and rules (as prescribed), working hours and rest intervals, weekly holidays, wage periods and date of payment, name and address of the inspector-cum-facilitator, IC composition and contact (POSH Act s.19(b)), penal consequences of sexual harassment (s.19(b)), GRC composition, holiday list. LDC generates printable notices and an intranet page, and records "displayed on <date> at <establishment>" with photo evidence.

---

## T.6 Statutory clocks owned by HR and payroll

| Clock key | Period | Start | Owner | Source |
|---|---|---|---|---|
| `pay_monthly_wage_deadline` | before the 7th of the following month | wage-period end | `ten_payroll_checker` | CoW s.17(1) |
| `wrk_wages_2wd` (F&F wages) | 2 working days | removal, dismissal, retrenchment, resignation | `ten_hr_admin` | CoW s.17(2) |
| `osh_leave_encash_2wd` / `_2m` | 2 working days / 2 months | separation (by type) | `ten_hr_admin` | OSH s.32(1)(vi) |
| `coss_gratuity_30d` | 30 days | gratuity becoming payable | `ten_hr_admin` | CoSS s.56 |
| `osh_appointment_letter_existing_3m` | 3 months | commencement / joining | `ten_hr_admin` | OSH s.6(1)(f) |
| `cow_fine_show_cause_7d` / `cow_fine_impose_15d` | 7 days / 15 days | notice | `ten_hr_admin` | Wages (Central) Rules r.16 [VERIFY] |
| `cow_absence_reply_7d` | 7 days | intimation of absence deduction | `ten_hr_admin` | r.17 [VERIFY] |
| `epf_ecr_monthly` | 15th of following month | wage month | `ten_payroll_checker` | EPF Scheme |
| `esic_monthly` | 15th of following month [VERIFY] | wage month | `ten_payroll_checker` | ESI regulations |
| `itax_salary_tds_quarterly` | per Income-tax Rules 2026 (NOT_CONFIRMED) | quarter end | `ten_payroll_checker` | Income-tax Rules 2026 |
| `itax_annual_certificate` | by 15 June after tax year [VERIFY] | tax-year end | `ten_payroll_checker` | Income-tax Rules 2026 |
| `posh_ic_constitution` | before the 10th employee joins | headcount crossing | `ten_hr_admin` | POSH Act s.4 |
| `posh_complaint_window` | 3 months (+3 with reasons) | last incident | IC Presiding Officer (info) | POSH s.9(1) |
| `posh_inquiry_90d` | 90 days | inquiry start | IC Presiding Officer | POSH s.11(4) |
| `posh_report_10d` | 10 days | inquiry completion | IC Presiding Officer | POSH s.13(1) |
| `posh_employer_action_60d` | 60 days | report receipt | employer designated officer | POSH s.13(4) |
| `posh_ic_term` | ≤ 3 years | member appointment | `ten_hr_admin` | POSH s.4(3) |
| `kmp_change_filing` | per Companies Act form timelines (e.g., DIR-12 within 30 days [VERIFY]) | KMP/director change | `ten_kmp` (CS) | Companies Act s.170, s.203 + rules |
| `io_appointment_intimation_5wd` | 5 working days | IO/Dy. IO appointment | `ten_kmp` (CS/CCO) | RBI NBFC IO Directions 2026 cl.16(1) |
| `io_vacancy_10wd` / `io_replacement_3m` | 10 working days / 3 months | vacancy | `ten_kmp` (CS/CCO) | cl.8(6) |
| `service_certificate` | default 7 days (T; Karnataka 7 days) | exit effective | `ten_hr_admin` | State rules |
| `leaver_access_revoke` | default 15 minutes (T) | exit effective | `ten_admin` | P01/P13 [REC] |

Clock breach → red alert to HR head and Company Secretary, exception in `cmp.exceptions`, Board-pack entry if statutory (NN-31 pattern).

---

## T.7 Rule-watch feed

`RuleWatchWorkflow` (owner: tenant Payroll Compliance Officer; reviewer: Company Secretary) consumes the shared pack's release notes and the P05 Updates feed for: VDA cycles (1 April, 1 October), Union Budget and Finance Act changes, State budgets (PT), EPFO/ESIC circulars, State S&E amendments, State rules under the Codes, bonus-ceiling and floor-wage notifications, Income-tax Rules due dates, DPDP phase dates (13 Nov 2026; 13 May 2027) affecting employee data processing. New pack versions are previewed against the tenant's last finalised run (diff by employee and component) before adoption; adoption is a Governed change (maker-checker).

---

## T.8 HR record retention schedule (seed; tenant may lengthen)

| Record | Default retention | Basis |
|---|---|---|
| Registers and wage records | 5 years after last entry | Wages (Central) Rules 2026 (SECONDARY_ONLY) |
| Payroll and TDS records | 8 years | Income-tax Act 2025 / Companies Act s.128 books [VERIFY] |
| Employee personnel file | Employment + 8 years | Limitation, tax and regulator inspection [REC] |
| Unsuccessful candidates | 6 months | DPDP purpose limitation [REC] |
| POSH case files | 8 years after closure (sealed) | Tenant policy [REC]; appeals and litigation |
| Attendance raw punches | 3 years | Proportionality; registers retain derived data [REC] |
| Geo-location at check-in (if enabled) | 90 days | Data minimisation (NN-25) [REC] |
| Fit-and-proper declarations | 8 years after cessation | Regulator inspection [REC] |
| Training records (mandatory) | 8 years | Regulator inspection [REC] |
| Disciplinary records | 8 years after closure | [REC] |

---

## T.9 Employee master field dictionary (minimised)

| Field | Required | Class | Notes |
|---|---|---|---|
| employee_code | Yes | Internal | Tenant format |
| legal_name, preferred_name | Yes / No | Personal | — |
| date_of_birth | Yes | Personal | Statutory computations; child-labour check |
| gender | Conditional | Personal | Only for statutory entitlements; "prefer not to say" allowed otherwise |
| work_email, mobile | Yes | Contact | — |
| residential address, state | Yes | Personal | PT/LWF where policy follows residence |
| PAN | Yes (payroll) | Identifier | Tokenised, masked |
| UAN / ESIC IP | Conditional | Identifier | — |
| Aadhaar | Never stored | — | DigiLocker verification flag only (NN-12) |
| bank account | Yes (payroll) | Financial | Tokenised; last 4 visible; change hold |
| nominee(s) | Conditional | Personal (third party) | Statutory nominations |
| emergency contact | Optional | Personal (third party) | — |
| qualifications | Conditional | Personal | Fit-and-proper, KMP eligibility |
| disability self-declaration | Optional | Sealed | Accommodations only |
| worker_class, employment_type | Yes | Employment | Drives entitlements |
| position, department, establishment, manager | Yes | Employment | Org model |
| regulated_role_code | Conditional | Employment | CCO, CRO, CISO, PNO, GRO, IO, PO (PMLA), DD (PMLA), DPO |

---

## T.10 Default department structures

See P13 FR-P13-03 for the eight entity-family templates; each department carries `compliance_dept_code` mapping to the Department vocabulary of the tenant's Excel question template (Appendix E, column M). For the IFSCA family the vocabulary is: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management (owner's IFSCA `Rough` sheet). For RBI/SEBI/IRDAI/co-op/company families the vocabulary is defined per family in Appendix E; renaming a department never changes its mapping.

---

## T.11 Golden fixtures required for conformance (minimum set)

1. Employee with excluded components > 50 % → add-back computed.
2. EPF split month September 2026 (ceiling change on 17 Sep).
3. ESI threshold crossing mid-contribution-period (continuation rules) [VERIFY].
4. Maharashtra woman employee PT at ₹24,000 and ₹26,000 gross; February ₹300 instalment.
5. Karnataka PT nil below ₹25,000.
6. Overtime 25 minutes → 30 minutes rounding; 2× rate on CoW wage rate.
7. Annual leave accrual for 200 days worked; carry-forward cap at 30.
8. F&F for resignation with 12 days encashable leave — 2-working-day clock with holiday in between.
9. Gratuity at 5 years 7 months (rounding rule of > 6 months [VERIFY CoSS rule]) and fixed-term employee at 1 year.
10. Deduction cap breach — excess carried forward.
11. Default-regime TDS at ₹12,00,000 (rebate) and ₹12,10,000 (marginal relief).
12. International worker EPF on full wages.

---


## T.12 Employment documents and clause library (seed)

| Document | Mandatory? | Signing | Key clauses / fields |
|---|---|---|---|
| Offer letter | Tenant policy | eSign or click-wrap acceptance | Position, grade, CTC breakdown showing CoW wage base, joining date, conditions precedent (BGV, documents), validity |
| Appointment letter | Yes — every employee (OSH s.6(1)(f)) | Employer signatory (eSign/DSC); employee acknowledgement | Prescribed particulars per OSH Central/State rules [VERIFY form]: name, designation, category/skill, wages, date of joining, social-security entitlements, working hours, leave |
| Employment agreement | Tenant policy (recommended for KMP, senior, sensitive roles) | Aadhaar eSign via ESP; stamping per State [VERIFY] | Duties; probation; confidentiality; data-protection obligations and employee privacy notice reference; IP assignment; conflict of interest; insider-trading code (listed); code of conduct; notice period; garden leave; non-solicitation; post-employment non-compete flagged void (Indian Contract Act s.27) with warning; governing law; dispute resolution (internal grievance → GRC → statutory forums; arbitration not suitable for statutory labour disputes [INTERP]) |
| KMP appointment letter | Yes for KMP under s.203 | Board resolution reference (P06) + eSign | Terms per Board approval; Sch. V remuneration where applicable; regulator fit-and-proper conditions |
| Fixed-term employment contract | When FTE | eSign | Term; parity of wages/benefits with permanent employees (IRC FTE provisions); gratuity eligibility after 1 year |
| Apprenticeship contract | When apprentice | Portal registration + signature | Per Apprentices Act |
| Consultant / retainer agreement | When non-employee | eSign | Independent-contractor status test checklist (control, integration, economic dependence) [REC] to avoid misclassification |
| Policy acknowledgement | Yes per policy | Click acknowledgement with version hash | Code of conduct, POSH policy, information security, AML/KYC, whistle-blower, PIT code |
| Relieving letter / service certificate | On exit | Employer eSign | Dates, designation; service certificate within State-specified time (e.g., Karnataka 7 days) |

## T.13 Fit-and-proper and regulated-role checks (seed rule set)

| Check | Applies to | Rule (seed) | Status |
|---|---|---|---|
| DIR-8 non-disqualification declaration | Directors | Companies Act s.164; annual at Board meeting | VERIFIED |
| s.184 disclosure of interest (MBP-1) | Directors | first Board meeting of FY and on change | VERIFIED |
| RE-specific F&P declaration and deed of covenants | Directors of NBFCs (and other REs per pack) | RBI F&P directions in the consolidated NBFC governance directions [VERIFY current instrument]; NRC scrutiny before appointment and annually | SECONDARY_ONLY |
| Senior management F&P | Specified roles (CEO, CFO, CRO, CCO, CTO/CISO per tenant policy) | Tenant policy aligned to regulator expectations [REC] | — |
| CISO independence | NBFC (Ch. IV/V scope) | Not reporting directly to Head of IT; no business targets; permanent invitee to ITSC (RBI NBFC Cyber Directions 2026 paras 81–82) | VERIFIED (text summary) |
| Internal Ombudsman eligibility and tenure | NBFCs in scope of IO Directions 2026 | GM-level (IO) / DGM-level (Dy. IO) or equivalent; ≥ 7 / ≥ 5 years experience; < 70 years at end of tenure; ≥ 3 years fixed term, ≤ 5 years total (cl.5, 6, 8(4)) | VERIFIED (text summary) |
| Principal Officer and Designated Director | Reporting entities under PMLA | PMLA Rules 2005 (as amended) r.7 [VERIFY]; FIU-IND registration of PO/DD | SECONDARY_ONLY |
| CCO tenure and reporting | NBFC-ML/UL; banks | RBI compliance-function directions (2026 NBFC series per owner's earlier MD sheets) [VERIFY para] | SECONDARY_ONLY |
| Company Secretary (whole-time) | Listed and specified companies | Companies Act s.203 + Rule 8A (paid-up capital ≥ ₹10 crore) | VERIFIED |
| Compliance Officer (listed) | Listed entities | LODR Reg 6 (must be the CS) | VERIFIED |

## T.14 Payroll outputs — layouts and accounting map

**Bank/payout layouts (adapters).** NEFT/RTGS bulk CSV (generic), SBI CMP/CINB bulk upload [VERIFY layout], HDFC ENet, ICICI CIB, Axis Power Access, Kotak FYN, YES Bank, IDFC First — each layout versioned in `int.layouts`; file contains only beneficiary name, account, IFSC, amount, narration, unique reference; file hash recorded at issue; bank response file mapped back to `hr.disbursal_results`. RazorpayX Payroll/Payouts adapter behind `hr.payout.razorpayx.enabled` (OFF). LDC never holds or routes salary money (D-11).

**Journal voucher map (default; tenant-editable).** Dr Salaries and Wages (by component and cost centre) / Dr Employer PF, ESI, LWF contribution expense / Dr Gratuity and leave-encashment provision expense / Cr Salary payable / Cr PF payable / Cr ESI payable / Cr PT payable / Cr LWF payable / Cr TDS on salary payable / Cr Loans and advances recovery. On disbursal: Dr Salary payable / Cr Bank. Export as Tally Prime XML (vouchers), CSV for other ledgers, and Ecosystem `finance` events for Finbyx GL tenants. Ind AS 19 / AS 15 actuarial valuation inputs (gratuity, leave) exported for the actuary; actuarial results imported as journal (P11 `acc`).

## T.15 POSH annual report template (fields)

Per POSH Rules r.14 [VERIFY exact wording]: (a) number of complaints of sexual harassment received in the year; (b) number of complaints disposed of during the year; (c) number of cases pending for more than ninety days; (d) number of workshops or awareness programmes against sexual harassment carried out; (e) nature of action taken by the employer or District Officer. Plus LDC fields for the Board report: statement of compliance with IC constitution (Companies (Accounts) Rules r.8(5)(x)); IC composition as on year end; training of IC members. Generated from `lab_posh` counts only; narrative drafted by Vidhi from counts (no case content).

## T.16 People-risk KRI definitions (seed, aggregates only)

| KRI | Formula | Default threshold (amber / red) |
|---|---|---|
| Voluntary attrition (annualised) | leavers_voluntary_12m ÷ average headcount | 18 % / 25 % |
| Critical-role attrition | as above for regulated/critical positions | 10 % / 20 % |
| Regulated-role vacancy days | days vacant per regulated role | 30 / 60 |
| Key-person approval concentration | max share of approvals by one person in a workflow class (from P02 authority matrix logs) | 40 % / 60 % |
| Mandatory-leave compliance (sensitive positions) | positions with required block taken ÷ sensitive positions | 90 % / 75 % (lower is worse) |
| Mandatory training completion | completed ÷ assigned (overdue excluded window 30 days) | 95 % / 85 % |
| Overtime cap breaches | count per quarter | 1 / 5 |
| BGV pending > 30 days after joining | count | 1 / 5 |
| Contractor statutory-challan gaps | contractors without monthly PF/ESI evidence | 1 / 3 |
| POSH cases pending > 90 days | count (sealed source) | 1 / 2 |

KRIs publish to P08 as `risk_metric_value` with metric id and version; sharing to Finbyx/Udofin only under `hr.kri.share_with_ecosystem` (aggregates; no individual identifiers).


## T.17 Open items

Tracked in P13 §14 (OI-P13-01 to OI-P13-12) and consolidated in Appendix W.

## T.18 Sources

Equator Pack v3.1 Appendix Z §Z.2 and research note RC_LABOUR_PAYROLL (23–24 Oct 2026); Infrabyx Ecosystem Integration Specification v1.1 §12.3; Ministry of Labour and Employment Labour Codes portal https://labour.gov.in/labour-codes ; POSH Act 2013 and Rules; RBI NBFC IO Directions 2026 https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=13274 ; RBI NBFC Cyber Directions 2026 https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13592 ; Companies Act 2013 and Rules https://www.mca.gov.in ; Income-tax Act 2025 https://www.incometax.gov.in (all accessed 25 Oct 2026).
