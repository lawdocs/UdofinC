# Phase P20 — Chambers Workspace v3 and Practice HR

> Paste after `01_MASTER_PROMPT.md`. Specification: **Appendix W** (`appendices/W_Private_ADR_Chambers_Workspace_v3_and_Practice_HR.md`); bare § references in this file point to Appendix W unless stated.
> **Dependencies (must be done first):** **P10** (Private ADR Chambers module, signup, branding, domains, rules/fee validators, run-off); **P15** (configuration framework, NN-33 tiers, settings UI and rule-pack store, Appendix V); **P18** (payroll engine and Appendix Z rule packs); **P19** (Equator Marketplace surface `mkp`, ranking and sponsorship). Also uses P01 (identity, Keycloak clients `eq-portal-chambers-{slug}`), P02 (case core, forms, tracker), P03 (blind conflict check), P04 (hearings), P05 (billing, Route, tax invoices), P06 (e-sign, e-stamp), P07 (communications), P12 (mobile), P13 (SSR site, CMS lint, sitemaps).
> **Estimated effort (planning estimate):** 6 two-week sprints for a squad of 9 (tech lead, 4 full-stack, 1 mobile, 1 QA automation, 1 payroll domain analyst, 1 designer shared with P13).

---

## 1. Objective and business outcome

Turn the v2 Private ADR Chambers workspace into a complete **practice operating system** for independent mediators, arbitrators and ADR chambers on Equator:

1. **Public practice pages** at `/chambers/{slug}`, on tenant sub-domains and on custom domains, built with a page builder whose blocks, themes and copy are checked for accessibility, naming, professional-conduct and truth-in-marketing rules, and kept entirely separate from Equator's institutional neutral directory (D3-15; NN-34).
2. **Practice configuration** that lets the chambers run proceedings its own way — rules, fees, templates, intake, notices, numbering, letterheads, e-sign, its own GST invoicing and payment collection, status labels and client-portal branding — inside Locked guardrails, with tenant-governed approvals rather than Equator super-admin involvement (NN-33; D3-16).
3. **Staff management** with role templates, case-level access, delegation, queues, SLAs and workload views, and a confidentiality wall that keeps HR and accounts staff out of case content (D3-19).
4. **Practice HR** (add-on): staff records, onboarding/offboarding, attendance and leave, salary records, monthly payroll on the Appendix Z rule packs, payslips and maker-checked disbursal from the chambers' own bank account, with sole-practitioner compensating controls (D3-17, D3-18; NN-35, NN-36).
5. **Practice dashboards and reports**, a complete settings catalogue (§W.8), plan hooks to the Appendix AB revenue registry, full portability (NN-37) and a clean tenant offboarding with domain release.

**Business outcome:** higher conversion and retention of Chambers plans (Appendix AB RS-09), a new HR add-on stream (RS-10, OFF until payroll UAT passes), eligible practices feeding the Equator Marketplace (RS-18; sponsored placement RS-19 OFF until Board and counsel), and a visible contrast with competitors whose marketplace directories are login-gated, unpriced and silent on ranking [RA F8 W1–W4].

---

## 2. Scope (in / out)

**In:** `chm` schema and module (pages, sites, domains, versions, lint, themes, marketplace projection and eligibility, enquiries, settings catalogue, approvals, templates, numbering, status labels, invoice profiles, staff assignments, delegations, queues, tasks, declarations, HR records, compliance wizard, attendance, leave, salary, bank accounts, pay runs, payslips, disbursal batches, consultant payments, goals, reviews, policies, control exceptions, offboarding); `chambers_practice` lint profile; theme validator; SSR renderer for practice pages; the `bank_file` adapter of `PAYOUT_PORT` and chambers use of `ACCOUNTING_PORT` (Appendix AC) and `PAYROLL_EXCHANGE_PORT` (Appendix Z); practice dashboards; exports `CHAMBERS_TENANT` (alias `CHAMBERS_PRACTICE`), `EMPLOYEE_FILE`, `EMPLOYEE_SELF`, `PAYROLL_FY` (Appendix AC §AC.13); phase addenda in P03, P05, P10, P12, P13 (§W.18).

**Out:** payroll calculation logic and rule-pack authoring (P18 / Appendix Z — consumed here); marketplace ranking, sponsorship, rate cards and labels (P19 — consumed here); Equator's own HRMS and payroll for its staff and group companies (the Equator HRMS and payroll phases on the `hr`/`pay` schemas — never used for chambers data, X-49); the settings framework itself (P15 — this phase registers chambers keys into it); POSH IC workspaces (P09 — linked only); case engines (P02–P06 — reused unchanged); public marketing page `/private-adr-chambers` beyond the copy addendum (P13).

---

## 3. Personas and permissions touched

| Role | P20 capabilities | Key restrictions |
|---|---|---|
| `chambers_owner` (new) | All practice settings; privileged role grants; G approvals if holding `chm.config.approve.legal`; pay-run checker; disbursal hold release; sensitive exports; offboarding | No checker on own maker action except under D3-18; no caucus access |
| `chambers_admin` | Pages, branding, domain (with owner for custom domain), T settings, G maker, staff invites (non-privileged), queues and SLAs | No salary access; no privileged grants without owner |
| `chambers_case_manager` (renamed from v2 seat) | Assigned matters; queues | No HR, no salary, no caucus |
| `chambers_staff` (new; sub-templates `assistant`, `tribunal_secretary`, `front_desk`) | Function-limited case support; enquiries; scheduling | Tribunal secretary only on instructed cases; never deliberation or reasons |
| `chambers_hr` (new) | HR records, onboarding/offboarding, leave, attendance, salary structures, pay-run maker | **No case content (DENY)**; cannot approve own run |
| `chambers_accounts` (new; sub-template `external_checker`) | Invoices, receivables, consultant fees, pay-run checker, disbursal file and reconciliation | **No case content (DENY)**; cannot change bank details or approve own payee |
| `neutral_*` (tenant scope) | Own person page (consent), own ESS if a staff record exists | As Appendix S |
| `employee` (tenant ESS) | Own attendance, leave, payslips, bank change, goals, acknowledgements, own export | Own data only |
| Equator `support_agent`, `platform_admin`, `auditor` | Ticketed read, JIT elevation, scoped audit | Never HR or salary data |

Matrix and hard denials: §W.14.

---

## 4. Functional requirements

### 4A. Practice pages

**FR-P20-01 — Sites and slugs.** Each chambers tenant has one `chm.sites` row with slug, regime, default locale, theme and tokens. Slug rules and reserved slugs per §W.3.2; slug changes ≤ 2 per year with 301s kept 12 months; released slugs quarantined 12 months. Errors `CHM_SLUG_RESERVED`, `CHM_SLUG_TAKEN`, `CHM_LABEL_PROHIBITED`.

**FR-P20-02 — Page kinds and routes.** Implement page kinds `practice_home`, `person`, `rules`, `fees`, `faq`, `contact`, `publications`, `legal`, `custom` at the routes in §W.3.1, with plan limits from §W.9. A sole practitioner's `practice_home` is their individual page.

**FR-P20-03 — Canonical hosts.** Serve pages on `equatorresolution.in/chambers/{slug}`, the tenant sub-domain (page routes 301 to canonical; portal routes served) and a verified custom domain (canonical when active) per X-48. `/chambers` (bare) keeps the 301 to `/private-adr-chambers`.

**FR-P20-04 — Block catalogue.** Implement the 21 blocks of §W.3.3 with Zod schemas, SSR renderers, lint profiles and regime availability; deny-listed blocks (testimonials, ratings, client logos, outcome statistics, paid labels, auto-opening widgets, third-party pixels) do not exist in the catalogue. `process_feedback` is behind `tenant.chm.pages.process_feedback_block` (OFF; n ≥ 10).

**FR-P20-05 — Professional-conduct regimes.** Derive `regime` per subject (`general`, `bci_r36`, `icai`, `icsi`, `icmai`) from verification records and declarations; enforce the block and field allow-lists of §W.3.7, `noindex` default for `bci_r36`, and sponsored ineligibility for restricted regimes. Error `CHM_BLOCK_NOT_ALLOWED_FOR_REGIME`.

**FR-P20-06 — Themes and accessibility.** Platform themes, brand tokens, fonts allow-list and the WCAG 2.2 contrast validator of §W.3.4; every version stores an axe report; failing palettes are rejected with the failing pairs and ratios (`CHM_THEME_CONTRAST_FAIL`, `CHM_FONT_NOT_ALLOWED`).

**FR-P20-07 — Custom domain and TLS.** TXT ownership, CNAME, CAA pre-check, ACM certificate on the multi-tenant CloudFront distribution, HSTS on confirmation, daily health check, `degraded` after 72 hours of DNS loss, release on downgrade or offboarding (§W.3.5, §W.15.5). Entitlement `chambers.custom_domain`.

**FR-P20-08 — SEO and structured data.** Titles, metas, canonicals, per-practice sitemaps, hreflang and JSON-LD per §W.3.6; prohibited types blocked (CHM-LINT-07); JSON-LD parity (LINT-046).

**FR-P20-09 — Multilingual pages.** English and Hindi on every plan; other NN-23 languages by configuration; machine drafts labelled; no locale publishes until reviewed; `legal` and `rules` translations need the D3-16 legal approver; locale parity (LINT-025). Error `CHM_LOCALE_NOT_REVIEWED`.

**FR-P20-10 — Copy lint profile.** `chambers_practice` profile running LINT-001–LINT-050 (as applicable) and CHM-LINT-01–12 (§W.3.9) on save, publish and nightly crawl; † rules cannot be overridden; other blocking rules only by the legal approver with a reason; nightly regressions unresolved for 7 days → `suspended_lint` with the last passing version restored.

**FR-P20-11 — Versioning and publishing.** Page version state machine of §W.3.11 with snapshot hashes, diff view, scheduled publish, rollback, approver ≠ editor when ≥ 2 publishers, single-person step-up approval (D3-18). Error `CHM_PUBLISH_APPROVAL_REQUIRED`.

**FR-P20-12 — Legal footer and intermediary duties.** Render the non-removable footer (CHL-L02) and a "Report this page" link on every page; reports open a P09 desk ticket routed to Equator's grievance officer under IT Rules 2021 timelines [RE F3.3].

**FR-P20-13 — Equator panel status line.** Implement the fixed sentence of §W.3.8 behind the platform flag `chambers.pages.show_equator_panel_status` (OFF); never in restricted regimes; any other reference to Equator endorsement is blocked by CHM-LINT-02.

**FR-P20-14 — Enquiries.** Enquiry form block (general regime) with the chambers' DPDP notice, CAPTCHA and rate limits; enquiry lifecycle `received → acknowledged → conflict_check → qualified | declined → converted_to_matter | closed`; conflict check against the tenant's matters and, with consent, the P03 blind index; conversion pre-fills P02 intake; retention per `tenant.chm.enquiry.retention_days`.

**FR-P20-15 — Marketplace projection and sponsored eligibility.** Owner opt-in, per-person consent, projected-field allow-list by regime; `chm` computes `sponsored_eligible` with reason codes (§W.3.10) and publishes `equator.chm.marketplace.eligibility_changed.v1`; P19 reads only `chm.marketplace_projection` through a `machine` identity. No sponsorship data is stored or displayed in `chm`.

### 4B. Practice configuration

**FR-P20-16 — Settings catalogue registration.** Register every key in §W.8 with the P15 framework: tier badge, who may change, approval need, bounds, default, history and rollback. G keys follow D3-16 (`chm.config.approve.legal`); L keys render read-only with reason and source.

**FR-P20-17 — Rules of procedure.** Adopt, fork or upload rules per §W.4.1; clause flags `locked`/`bounded`/`free`; validator per FR-P10-07 and CHL-L07; G approval; publication on the `rules` page; pinning per matter (NN-21).

**FR-P20-18 — Fee schedules.** §W.4.2 elements with NN-18/NN-29 validation, platform refund floor, regulated schedules applied exactly; rendered via `FeeToken`s only. Error `CHM_FEE_PROHIBITED_STRUCTURE`.

**FR-P20-19 — Templates.** Template families of §W.4.3 with locked blocks, award checks against A&C Act s.31(1)–(4), s.31(7) and s.31A, settlement lint, merge-field dictionary checks, per-language legal review, DOCX + PDF/A outputs. Errors `CHM_TEMPLATE_LOCKED_BLOCK_REMOVED`, `CHM_AWARD_TEMPLATE_INCOMPLETE`.

**FR-P20-20 — Intake forms and notifications.** Tenant extensions to P02 intake with locked fields (§W.4.4); notification templates per channel with NN-12 and NN-16 locks (§W.4.5); procedural templates G, courtesy templates T.

**FR-P20-21 — Numbering and letterheads.** Numbering tokens and rules of §W.4.6 (immutable once issued; `CHM_NUMBERING_IMMUTABLE`, `CHM_NUMBERING_FORMAT_INVALID`); letterheads per legal entity/office with the locked footer (§W.4.7).

**FR-P20-22 — E-sign and e-stamp settings.** Defaults per document class and NN-08/NN-09 locks (§W.4.8).

**FR-P20-23 — Chambers invoicing.** Invoice profiles per GSTIN and FY (CGST Rules r.46(b) series rule), registered/unregistered status, SAC map, RCM rules, e-invoice enablement, TDS-on-receipts tracking, credit notes under maker-checker (§W.4.9). Errors `CHM_INVOICE_SERIES_INVALID`, `CHM_GSTIN_INVALID`.

**FR-P20-24 — Payment collection.** Route linked account in the chambers' name, methods, link expiry, deposit requests, refund maker-checker; settlement money never through the linked account (§W.4.10; NN-13).

**FR-P20-25 — Status labels and client portal branding.** Label maps per state and locale with deny-list and meaning checks (G; `CHM_STATUS_LABEL_PROHIBITED`); party/counsel portal branding with locked disclosures (§W.4.11).

### 4C. Staff management and work

**FR-P20-26 — Role templates and migration.** Implement the six chambers roles and sub-templates (§W.2.1), ABAC attributes (§W.2.2) and the matrix and hard denials (§W.14). Migrate v2 `case_manager` seats to `chambers_case_manager`; the first admin of each existing tenant becomes `chambers_owner` (X-47).

**FR-P20-27 — Invitations and provisioning.** Invite flow with owner approval and step-up for privileged roles, acceptance of staff code, confidentiality undertaking and monitoring notice, seat checks (`CHM_SEAT_LIMIT`), `chm.access_events` logging, immediate revocation at exit (§W.5.1).

**FR-P20-28 — Case-level access and tribunal secretaries.** Assignment model and conflict blocks (§W.5.2; `CHM_STAFF_CONFLICT_DECLARED`); tribunal-secretary access only with an instruction artefact and party disclosure notice (`tenant.chm.staff.tribunal_secretary_instruction_required`, G, ON).

**FR-P20-29 — Delegation.** Time-bound delegation ≤ 90 days within the delegator's scope; never `chm.config.approve.legal`, owner capabilities or salary access; "on behalf of" stamping (§W.5.3; `CHM_DELEGATION_SCOPE_EXCEEDED`).

**FR-P20-30 — Queues, tasks, calendars and SLAs.** Queues of §W.5.4 with SLA policies, warnings at 75% and breach events; tasks linked to objects without duplicating documents across case and HR stores; statutory clocks shown as read-only items from the clocks engine; calendars with busy/free-only external sync through `WORKSPACE_PORT` (§W.5.5).

**FR-P20-31 — Workload and SoD engine.** Workload views with NN-35 visibility limits; SoD rules evaluated at grant, delegation, submission and nightly (§W.5.6; `CHM_ROLE_SOD_CONFLICT`); staff conduct declarations feeding assignment blocks (§W.5.7).

### 4D. Practice HR

**FR-P20-32 — Activation and disclaimer.** `tenant.chm.hr.enabled` only when the Appendix AB stream RS-10 (Chambers HR-lite and payroll add-on) is `live` and the entitlement is present; the fixed disclaimer of §W.6.1 appears on employer screens and output cover sheets; payslips carry the rule-pack version line.

**FR-P20-33 — Compliance wizard.** Headcount-by-class wizard at activation and monthly, switching duties by the thresholds of §W.6.2 read from Appendix Z parameters, with source and verification status shown per duty and State registration evidence captured.

**FR-P20-34 — Staff records and engagement types.** Records per §W.6.3 with masked identifiers, `worker_class` reviews, dual State fields, HR document store on a separate S3 prefix and KMS key; misclassification checklist (`CHM_ENGAGEMENT_MISCLASSIFICATION_WARNING`); advocates default to `professional_engagement`.

**FR-P20-35 — Onboarding and offboarding.** Checklists of §W.6.4 with locked items; offboarding revokes all access at the exit timestamp, reassigns work, and starts the F&F (2 working days) and gratuity (30 days) clocks.

**FR-P20-36 — Attendance and hours.** Capture methods, regularisation, self-view and dispute, monitoring notice, retention and overtime/night-work rules per §W.6.5; prohibited monitoring settings absent — the Appendix Z platform set `platform.hr.monitoring.prohibited_set` (`CHM_MONITORING_PROHIBITED` → `HR_MONITORING_PROHIBITED`).

**FR-P20-37 — Leave.** Two-layer leave model with the floor validator (`CHM_LEAVE_POLICY_BELOW_FLOOR`), Appendix Z templates `leave.statutory_minimum@2026.1` and `leave.equator_standard@2026.1` with the §Z.8.3 State uplift, leave types, State holiday calendars with locked national holidays (§W.6.6).

**FR-P20-38 — Salary structures and restricted access.** Component classes from Appendix Z, statutory wage calculator with the MoLE golden test, effective-dated structures and assignments under maker-checker, field-level encryption and access logging (§W.6.7; `CHM_SALARY_ACCESS_DENIED`).

**FR-P20-39 — Monthly payroll.** `ChambersPayRunWorkflow` implementing the 12 steps of §W.6.8, calling the P18 engine (`packages/rules/payroll`, X-58) with Appendix Z rule packs under the §Z.2.4 rule-pack map names; blocks on `NOT_CONFIRMED` parameters; per-run acknowledgement of `SECONDARY_ONLY` parameters; 50% deduction cap with deferral; ghost checks; statutory outputs; period lock with un-disableable edit log. Errors `CHM_PAYRUN_PARAM_UNCONFIRMED`, `CHM_PAYRUN_DEDUCTION_CAP`, `CHM_PAYRUN_GHOST_HIT_UNRESOLVED`, `CHM_PAYRUN_DEADLINE`, `CHM_STATUTORY_DUES_WAIVER` (sub-codes mapping to the Appendix Z / F canonical codes per §W.13).

**FR-P20-40 — Payslips.** PDF/A payslips per §W.6.9, released on or before payment; ESS download on web and mobile; optional employee-password email.

**FR-P20-41 — Disbursal and bank details.** `PAYOUT_PORT` (X-49 naming; Appendix Z) with the shared `bank_file` adapter (default) and `payout_api` (provider adapter, flag OFF, tenant-owned account only); bank-change protocol with penny-drop, 3-working-day cooling (1–7), out-of-band notifications and reversal link, pre-pay freeze; authority matrix (releaser ≠ maker; ≠ checker where a third money-role holder exists; reconciler ≠ releaser where ≥ 2 users); acknowledgement reconciliation (§W.6.10). Errors `CHM_BANK_CHANGE_COOLING`, `CHM_BANK_NAME_MISMATCH`, `CHM_DISBURSAL_FILE_HASH_MISMATCH`, `CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED`.

**FR-P20-42 — Single-person controls.** D3-18 controls (separate session ≥ 10 minutes after submission with passkey step-up; no in-window bank override; 24-hour anomaly holds; free external checker; `SINGLE_PERSON_SOD` exceptions and monthly summary; 7-day cooling to return to single-person mode). Errors `CHM_SINGLE_PERSON_GAP`, `CHM_MAKER_CHECKER_SAME_USER`, `CHM_STEP_UP_REQUIRED`.

**FR-P20-43 — Consultant fees with TDS.** Professional engagements, fee notes with GST/RCM flags, TDS per ITA 2025 s.393(1) Table Sl. 6(iii) above ₹50,000 per tax year, Form 131/140 data, maker-checked payment through `PAYOUT_PORT` (`bank_file`) (§W.6.11).

**FR-P20-44 — Goals, reviews and policies.** Outcome-based goals, simple reviews with employee acknowledgement and response, no AI ratings; versioned policy acknowledgements (§W.6.12).

**FR-P20-45 — Accounting and payroll exports.** `ACCOUNTING_PORT` (Appendix AC) journals and `PAYROLL_EXCHANGE_PORT` (Appendix Z) payroll exports; CSV imports of employee masters and opening YTD balances with dry-run (§W.6.13).

### 4E. Dashboards, plans, portability

**FR-P20-46 — Practice dashboards and reports.** The 11 dashboards and scheduled reports of §W.7, each metric with a definition and role visibility; replaces the v2 health dashboard on SCR-S-D10.

**FR-P20-47 — Plans and entitlements.** Read the §W.9 entitlement keys and stream states from the Appendix AB registry; no price is hard-coded; add-ons purchasable only when their Appendix AB stream (RS-09, RS-10, RS-37, RS-38) is `live`; upgrade prompts only in Settings and pricing pages (`CHM_ENTITLEMENT_REQUIRED`).

**FR-P20-48 — Exports.** `CHAMBERS_TENANT` (alias `CHAMBERS_PRACTICE`), `EMPLOYEE_FILE`, `EMPLOYEE_SELF` and `PAYROLL_FY` exports under `EQ-EXPORT-1.0` with the Appendix AC §AC.13 taxonomy as placed for chambers in §W.15.3 (root ≤ 40 and paths below root ≤ 140 characters, AC §AC.13.7), built by the P21 export service, owner approval and step-up for sensitive scopes, employee self-export of their own file, free at any time.

**FR-P20-49 — Tenant offboarding.** State machine of §W.15.4 with full export, run-off for open matters, staff export links, domain and slug release (§W.15.5), erasure 30 days after closure unless under legal hold, erasure certificate.

**FR-P20-50 — Firewall tests.** CI tests `NO_PAID_PLACEMENT` (extended to `chm`), `NO_CHM_READ_IN_ALLOCATION`, `CHM_CONFIDENTIALITY_WALL_MATRIX` and `CHM_LINT_PROFILE` are mandatory and block merges.

---

## 5. Workflows and state machines

### 5.1 Page version

As §W.3.11: `draft → in_review → approved → published → superseded | unpublished | suspended_lint`, with `rollback` creating a new version from a superseded snapshot. Guards: blocking lint findings, theme validator, locale review, approver ≠ editor (or D3-18 step-up), legal approver for `legal`/`rules` pages.

### 5.2 Custom domain

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| — | add host | Entitlement; label validator; host unused | `pending` | TXT token and CNAME target issued |
| `pending` | verify | TXT and CNAME found; CAA permits Amazon CA | `verified` | ACM request (DNS validation) |
| `verified` | certificate issued | — | `active` | Alternate domain on CloudFront; canonical switches; sitemap and canonical tags updated; `equator.chm.domain.verified.v1` |
| `active` | DNS lost > 72 h or certificate renewal failed | — | `degraded` | Canonical reverts to Equator host; admin alerted |
| `degraded` | checks pass | — | `active` | — |
| any | remove / downgrade / offboarding | — | `released` | §W.15.5 steps; `equator.chm.domain.released.v1` |

### 5.3 Enquiry

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| — | submitted | CAPTCHA; consent captured; rate limit | `received` | Routed to `enquiries` queue; auto-acknowledgement to the enquirer |
| `received` | acknowledged | — | `acknowledged` | SLA clock stops for first response |
| `acknowledged` | run conflict check | — | `conflict_check` | Tenant search + P03 blind index (if consented) |
| `conflict_check` | clear | No hit or hit resolved with disclosure | `qualified` | — |
| `conflict_check` / `qualified` | decline | Reason (neutral template) | `declined` | Enquirer informed |
| `qualified` | convert | Party data confirmed | `converted_to_matter` | P02 intake pre-filled; `equator.chm.enquiry.converted.v1` |
| any open | retention expiry | Not converted | `closed` | Personal data erased; counts kept |

### 5.4 Bank-detail change

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| — | request | Employee session (MFA) or HR-initiated | `requested` | Penny-drop name match |
| `requested` | name match ≥ threshold | — | `awaiting_employee_confirmation` (HR-initiated) or `pending_cooling` | Notifications to registered email, phone and previous channel with reversal link |
| `awaiting_employee_confirmation` | employee confirms in app | — | `pending_cooling` | `cooling_until` = +3 working days (T 1–7) |
| `pending_cooling` | reversal link used | — | `frozen` | Previous account stays active; HR and owner alerted |
| `pending_cooling` | cooling elapsed | Not within pre-pay freeze, or owner approved in-window exception (not in single-person mode) | `active` | Previous account `retired`; `equator.chm.bank_change.activated.v1` |
| `requested` | name mismatch | — | `rejected` | `CHM_BANK_NAME_MISMATCH` |

### 5.5 Pay run

`open → inputs_frozen → calculated → submitted → approved → (on_hold →) disbursal_generated → disbursed → reconciled → payslips_released → locked`; `cancelled` from any state before `disbursal_generated`. Guards per §W.6.8: deadline; unconfirmed parameters block `approved`; ghost hits; deduction cap; maker ≠ checker or D3-18 (gap ≥ 10 minutes, step-up, anomaly hold 24 hours → `on_hold`); releaser ≠ maker; acknowledgement hash match for `reconciled`. Off-cycle and F&F runs use the same machine with `kind` set; the F&F 2-working-day clock is owned by HR and escalates to the owner at 50% and 100% of the period.

### 5.6 Delegation

`active` (from start time) → `ended` (end time reached) or `revoked` (by delegator, owner or on either party's exit). Every action under a delegation stores `delegation_id`.

### 5.7 Tenant offboarding

As §W.15.4: `active → offboarding_requested → export_ready → runoff → domain_release → closed → erased`, with `legal_hold` suspending erasure and cancellation back to `active` before run-off.

---

## 6. Screens and UX (web + mobile)

WCAG 2.2 AA; en-IN and hi-IN at launch; tenant branding in chambers portals; one primary action per screen; empty, loading and error states per the design system; no upsell in case, hearing or approval views (Appendix O X-15).

| ID | Route | Persona | Purpose and key components | Notes |
|---|---|---|---|---|
| SCR-P20-01 | `/chambers/{slug}` and sub-pages | public | Rendered practice pages with legal footer and "Report this page" | SSR; canonical host logic |
| SCR-P20-02 | `/chambers/admin/site` | owner, admin | Site settings: slug, regime (read-only with reason), locales, theme, marketplace opt-in | Reserved-slug check inline |
| SCR-P20-03 | `/chambers/admin/pages` | admin | Page list with status chips, version history, scheduled publishes | Filter by locale and status |
| SCR-P20-04 | `/chambers/admin/pages/{id}/edit` | admin, staff with `page_scope` | Block editor: add/reorder blocks (only regime-allowed blocks offered), inline lint, live preview (mobile/desktop, light/dark, locale) | Autosave; presence lock |
| SCR-P20-05 | `/chambers/admin/pages/{id}/review` | approver | Diff view, lint and axe reports, approve/reject with reason | Step-up in single-person mode |
| SCR-P20-06 | `/chambers/admin/theme` | admin | Tokens, fonts, contrast matrix with pass/fail per pair, logo upload | Shows WCAG ratio per pair |
| SCR-P20-07 | `/chambers/admin/domains` | owner | Custom domain wizard: TXT, CNAME, CAA status, certificate status, HSTS toggle | Copy-able DNS records |
| SCR-P20-08 | `/chambers/admin/people` | admin | Person records, consent per field, regime, person-page link | Consent request flow to each person |
| SCR-P20-09 | `/chambers/admin/enquiries` | front desk, admin | Enquiry queue with conflict-check panel and convert-to-matter | SLA timers |
| SCR-P20-10 | `/chambers/admin/settings` | per tier | Settings catalogue browser (§W.8) with tier badges, "who may change", approval status, history, rollback | Search by key and label |
| SCR-P20-11 | `/chambers/admin/approvals` | legal approver, owner | G approvals queue with validator reports | — |
| SCR-P20-12 | `/chambers/admin/rules` | admin, legal approver | Rulebook (adopt/fork/upload), clause flags, validator results, publish | Extends SCR-P10-04 |
| SCR-P20-13 | `/chambers/admin/templates` | admin, legal approver | Template families, locked blocks shown, preview with synthetic data, language versions | — |
| SCR-P20-14 | `/chambers/admin/numbering`, `/status-labels`, `/letterheads` | admin | Pattern builder with live sample; label map per locale; letterhead editor | Immutability warning |
| SCR-P20-15 | `/chambers/admin/invoicing` | accounts, owner | Invoice profiles per GSTIN/FY, series checker, SAC map, e-invoice status | r.46(b) live check |
| SCR-P20-16 | `/chambers/admin/staff` | owner, admin | Members, roles, sub-templates, case-access mode, invitations, privileged-grant approvals | Step-up for privileged grants |
| SCR-P20-17 | `/chambers/admin/delegations` | any user | Create/revoke delegations | — |
| SCR-P20-18 | `/chambers/work` | case managers, staff | Queues, tasks, SLA badges, read-only clock items, calendar | Mobile tab "Work" |
| SCR-P20-19 | `/chambers/workload` | owner, admin, managers | Workload per person and team, capacity | Individual data only to permitted viewers |
| SCR-P20-20 | `/chambers/hr` | HR, owner | HR home: compliance wizard result, duties on/off with sources, disclaimer, tasks | Disclaimer fixed |
| SCR-P20-21 | `/chambers/hr/people/{id}` | HR | Staff record tabs: profile, engagement, documents, checklists, attendance, leave, salary (scope-gated), declarations | Salary tab hidden without scope |
| SCR-P20-22 | `/chambers/hr/leave`, `/attendance` | HR, managers | Policy editor with floor validator, calendars, approvals, regularisations | — |
| SCR-P20-23 | `/chambers/hr/payroll` | HR, accounts, owner | Pay runs list, run detail (inputs, calculation, variance, ghost hits, parameter status), submit/approve/disburse/reconcile/release/lock | WYSIWYS approval summary |
| SCR-P20-24 | `/chambers/hr/payroll/{id}/disbursal` | accounts | Generate bank file (hash shown), upload acknowledgement, reconciliation results | No file edit |
| SCR-P20-25 | `/chambers/hr/consultants` | accounts | Engagements, fee notes, TDS tracker, certificates | — |
| SCR-P20-26 | `/chambers/hr/performance`, `/policies` | HR, managers, employees | Goals, reviews, acknowledgements | — |
| SCR-P20-27 | `/chambers/me` | employee | ESS: attendance check-in, leave, payslips, bank change, tax declarations, goals, policies, own export | Mobile tab "Me" |
| SCR-P20-28 | `/chambers/controls` | owner, external checker | Control exceptions, single-person log, bank-change events, ghost hits | Exportable |
| SCR-P20-29 | `/chambers/dashboards/{code}` | per §W.7 | Practice dashboards | Replaces SCR-S-D10 tiles |
| SCR-P20-30 | `/chambers/admin/export`, `/offboarding` | owner | Export scopes, approval, download; offboarding wizard with run-off status and domain release | Step-up |

**Mobile (Expo; P12 addendum §W.18):** tabs "Work" (SCR-P20-18), "Me" (SCR-P20-27) and "Approvals" (owner/checker approvals with WYSIWYS summary and passkey step-up in the system browser). Payslip views use Tier-High screen protection (`FLAG_SECURE` on Android; blur in the iOS app switcher). Attendance check-in works offline and syncs with a server timestamp and a device timestamp shown side by side.

---

## 7. Backend design

### 7.1 Modules touched

New NestJS module **`chm`** (owner) with sub-modules `chm-pages`, `chm-config`, `chm-work`, `chm-hr`, `chm-payroll`, `chm-reports`, `chm-offboarding`. Consumes: `chambers` (workspace state), `tenancy` (domains), `rules` (validators), `forms`, `cases`, `clocks`, `hearings` (calendars), `billing`/`payments` (invoices, Route), `esign`/`estamp`, `comms`, `documents`, `audit`, `reporting`, `cms` (lint package), `cfg` (settings and rule packs, P15), the **P18 payroll engine** package (pure functions; no DB access of its own in chambers mode) and the **P19 marketplace** interface (projection read). `chm-hr` and `chm-payroll` run under a separate DB role (`chm_hr_svc`) that has grants on HR tables; the `cases` DB role has none (D3-19).

### 7.2 Tables

Full inventory: §W.10.1. Binding DDL for the tables with the strongest invariants:

```sql
CREATE TABLE chm.page_versions (
  id               uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id        uuid NOT NULL,
  page_id          uuid NOT NULL REFERENCES chm.pages(id),
  version_no       int  NOT NULL,
  status           text NOT NULL CHECK (status IN ('draft','in_review','approved','published','superseded','unpublished','suspended_lint')),
  blocks           jsonb NOT NULL,
  snapshot_sha256  char(64),
  lint_report      jsonb,
  axe_report       jsonb,
  edited_by        uuid NOT NULL REFERENCES core.users(id),
  approved_by      uuid REFERENCES core.users(id),
  approval_single_person boolean NOT NULL DEFAULT false,
  published_at     timestamptz,
  UNIQUE (page_id, version_no),
  CONSTRAINT approver_differs CHECK (approved_by IS NULL OR approved_by <> edited_by OR approval_single_person),
  CONSTRAINT snapshot_when_reviewed CHECK (status = 'draft' OR snapshot_sha256 IS NOT NULL)
);

CREATE TABLE chm.numbering_formats (
  id              uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id       uuid NOT NULL,
  pattern         text NOT NULL CHECK (pattern ~ '\{PFX\}' AND pattern ~ '\{SEQ:[4-7]\}' AND length(pattern) <= 60),
  reset_basis     text NOT NULL CHECK (reset_basis IN ('never','calendar_year','financial_year')),
  first_issued_at timestamptz,           -- set by trigger on first issue; trigger blocks UPDATE of pattern when NOT NULL
  active          boolean NOT NULL DEFAULT true
);

CREATE TABLE chm.invoice_profiles (
  id              uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id       uuid NOT NULL,
  gstin           char(15) CHECK (gstin ~ '^[0-9]{2}[A-Z0-9]{10}[0-9A-Z]Z[0-9A-Z]$'),
  gst_status      text NOT NULL CHECK (gst_status IN ('registered','unregistered')),
  state_code      char(2) NOT NULL,
  fy              char(7) NOT NULL,      -- e.g. 2026-27
  series_prefix   text NOT NULL,
  next_serial     int  NOT NULL DEFAULT 1,
  serial_width    int  NOT NULL,
  CONSTRAINT r46_length CHECK (length(series_prefix) + serial_width <= 16),
  CONSTRAINT r46_chars  CHECK (series_prefix ~ '^[A-Z0-9/-]*$'),
  CONSTRAINT gstin_when_registered CHECK (gst_status = 'unregistered' OR gstin IS NOT NULL),
  UNIQUE (tenant_id, gstin, fy, series_prefix)
);

CREATE TABLE chm.bank_accounts (
  id               uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id        uuid NOT NULL,
  staff_record_id  uuid REFERENCES chm.staff_records(id),
  payee_id         uuid,                 -- consultant payee
  account_enc      bytea NOT NULL,
  ifsc             char(11) NOT NULL CHECK (ifsc ~ '^[A-Z]{4}0[A-Z0-9]{6}$'),
  holder_name      text NOT NULL,
  name_match_score numeric(3,2) NOT NULL CHECK (name_match_score BETWEEN 0 AND 1),
  status           text NOT NULL CHECK (status IN ('pending_cooling','active','frozen','retired')),
  cooling_until    timestamptz NOT NULL,
  requested_via    text NOT NULL CHECK (requested_via IN ('employee_session','hr_initiated_employee_confirmed','payee_link_confirmed')),
  confirmed_by_holder_at timestamptz,   -- employee (staff) or consultant payee confirmation via the out-of-band link
  activated_at     timestamptz,
  CONSTRAINT owner_one CHECK ((staff_record_id IS NULL) <> (payee_id IS NULL)),
  CONSTRAINT payee_link_only_for_payees CHECK (requested_via <> 'payee_link_confirmed' OR payee_id IS NOT NULL),
  CONSTRAINT active_after_cooling CHECK (status <> 'active' OR (activated_at >= cooling_until AND confirmed_by_holder_at IS NOT NULL))
  -- trigger trg_bank_activation sets activated_at = now() and rejects activation before cooling_until (no volatile functions in CHECK)
);

CREATE TABLE chm.pay_runs (
  id                 uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id          uuid NOT NULL,
  pay_group          text NOT NULL,
  period_start       date NOT NULL,
  period_end         date NOT NULL,
  pay_date           date NOT NULL,
  kind               text NOT NULL CHECK (kind IN ('regular','off_cycle','full_and_final')),
  status             text NOT NULL CHECK (status IN ('open','inputs_frozen','calculated','submitted','approved','on_hold','disbursal_generated','disbursed','reconciled','payslips_released','locked','cancelled')),
  rule_pack_versions jsonb NOT NULL DEFAULT '{}',
  unconfirmed_params int NOT NULL DEFAULT 0,
  secondary_params_ack_by uuid,
  maker_id           uuid,
  checker_id         uuid,
  releaser_id        uuid,
  single_person      boolean NOT NULL DEFAULT false,
  hold_until         timestamptz,
  CONSTRAINT deadline CHECK (kind <> 'regular' OR pay_date < (date_trunc('month', period_end) + interval '1 month' + interval '6 days')::date),
  CONSTRAINT no_unconfirmed_on_approve CHECK (status NOT IN ('approved','disbursal_generated','disbursed','reconciled','payslips_released','locked') OR unconfirmed_params = 0),
  CONSTRAINT maker_checker CHECK (checker_id IS NULL OR checker_id <> maker_id OR single_person),
  CONSTRAINT releaser_not_maker CHECK (releaser_id IS NULL OR releaser_id <> maker_id OR single_person)
);
```

The `deadline` constraint encodes "before the 7th day of the following month" for monthly wage periods (CoW s.17(1)); weekly or fortnightly pay groups use their own deadline function in the engine. A trigger on `chm.pay_runs` asserts the D3-18 conditions (step-up assertion reference, ≥ 10-minute gap, anomaly hold) whenever `single_person = true`, and rejects `releaser_id = checker_id` when the tenant has a third active holder of a money role (W §W.5.6). A trigger on `chm.bank_accounts` writes `chm.control_exceptions` for in-window owner overrides.

### 7.3 APIs

`/v1`, OpenAPI 3.1; Idempotency-Key on every POST that creates money, pay runs, payees, exports or publications; RFC 9457 errors with the `CHM_*` codes of §W.13.

| Method & path | Purpose | Auth (scope) |
|---|---|---|
| `GET /v1/public/chambers/{slug}` · `GET …/{path}` | Rendered page JSON for SSR (published only) | public; rate-limited |
| `POST /v1/public/chambers/{slug}/enquiries` | Submit enquiry (CAPTCHA, consent) | public |
| `GET/POST /v1/chm/{tenantId}/sites` · `PATCH …/sites/{id}` | Site, slug, theme, tokens, fonts | `page_scope=edit`; slug change owner |
| `POST /v1/chm/{tenantId}/pages` · `POST …/pages/{id}/versions` · `PATCH …/versions/{v}` | Pages and versions | `page_scope=edit` |
| `POST …/versions/{v}/submit` · `…/approve` · `…/reject` · `…/publish` · `…/rollback` · `POST …/pages/{id}/unpublish` | Page workflow | `publish`; step-up for single-person approve |
| `POST /v1/chm/{tenantId}/lint` | Lint a draft (profile `chambers_practice`) | `page_scope=edit` |
| `POST /v1/chm/{tenantId}/themes/validate` | Contrast and font validation | `page_scope=edit` |
| `POST /v1/chm/{tenantId}/domains` · `POST …/domains/{id}/verify` · `DELETE …/domains/{id}` | Custom domain lifecycle | owner |
| `GET/PUT /v1/chm/{tenantId}/marketplace/projection` | Marketplace opt-in and fields | owner |
| `GET /v1/chm/{tenantId}/marketplace/eligibility` | Sponsored eligibility and reasons (read by P19 service identity) | owner; `machine` (P19) |
| `GET /v1/chm/{tenantId}/settings` · `PUT …/settings/{key}` · `POST …/settings/{key}/approve` · `POST …/settings/{key}/rollback` | Settings catalogue §W.8 | per key tier |
| `POST /v1/chm/{tenantId}/rules/import` · `POST …/rules/{id}/versions/{v}/submit` · `…/approve` | Rules (validator, D3-16) | admin maker; legal approver |
| `POST /v1/chm/{tenantId}/templates` · `…/{id}/submit` · `…/{id}/approve` · `POST …/templates/{id}/preview` | Templates | admin; legal approver |
| `PUT /v1/chm/{tenantId}/numbering` · `PUT …/status-labels` · `PUT …/invoice-profiles/{id}` | Numbering, labels, invoice profiles | admin / accts; legal for labels |
| `POST /v1/chm/{tenantId}/staff/invitations` · `POST …/invitations/{id}/approve` · `DELETE …/members/{userId}` | Invite, approve privileged grant, revoke | admin; owner (step-up) |
| `POST /v1/chm/{tenantId}/cases/{caseId}/assignments` · `DELETE …/assignments/{id}` | Case-level access | admin / owner |
| `POST /v1/chm/{tenantId}/delegations` · `DELETE …/delegations/{id}` | Delegation | delegator |
| `GET /v1/chm/{tenantId}/queues/{code}/items` · `POST /v1/chm/{tenantId}/tasks` · `PATCH …/tasks/{id}` | Work queues, tasks | role-scoped |
| `PATCH /v1/chm/{tenantId}/enquiries/{id}` · `POST …/enquiries/{id}/conflict-check` · `POST …/enquiries/{id}/convert` | Enquiry workflow | front desk / admin |
| `POST /v1/chm/{tenantId}/hr/staff` · `PATCH …/hr/staff/{id}` · `POST …/hr/staff/{id}/exit` | Staff records | `hr_scope=records` |
| `POST /v1/chm/{tenantId}/hr/compliance-wizard/run` | Size-aware duties | HR / owner |
| `GET/POST /v1/chm/{tenantId}/hr/attendance` · `POST …/attendance/regularisations` | Attendance | employee; manager |
| `POST /v1/chm/{tenantId}/hr/leave-policies/validate` · `POST …/leave-requests` · `POST …/leave-requests/{id}/decide` | Leave | HR; employee; approver |
| `POST /v1/chm/{tenantId}/hr/salary-structures` · `POST …/salary-assignments` · `POST …/salary-assignments/{id}/approve` | Salary | `records_and_salary`; owner checker |
| `POST /v1/chm/{tenantId}/hr/bank-accounts` · `POST …/bank-accounts/{id}/confirm` · `POST /v1/public/chm/bank-change/{token}/freeze` | Bank details; reversal link | employee; HR; public token |
| `POST /v1/chm/{tenantId}/payroll/runs` · `…/runs/{id}/freeze` · `…/calculate` · `…/submit` · `…/approve` · `…/disbursal` · `…/acknowledgement` · `…/release-payslips` · `…/lock` | Pay-run workflow | HR maker; owner/accts checker (step-up); accts releaser |
| `GET /v1/chm/{tenantId}/payroll/runs/{id}/statutory-outputs` | Registers, ECR, ESI, PT, TDS data | HR; accts |
| `GET /v1/chm/{tenantId}/me/payslips` · `GET …/me/payslips/{id}.pdf` | ESS payslips | employee |
| `POST /v1/chm/{tenantId}/consultants/{id}/payments` · `…/approve` | Consultant fees with TDS | accts; owner |
| `POST /v1/chm/{tenantId}/performance/goals` · `POST …/reviews` · `POST …/reviews/{id}/acknowledge` | Goals and reviews | manager; employee |
| `POST /v1/chm/{tenantId}/policies/{code}/acknowledge` | Policy acknowledgement | employee |
| `GET /v1/chm/{tenantId}/dashboards/{code}` · `POST …/reports/{code}/run` | Dashboards and reports | per §W.7 |
| `POST /v1/chm/{tenantId}/exports` · `POST …/exports/{id}/approve` | `CHAMBERS_TENANT` (alias `CHAMBERS_PRACTICE`), `EMPLOYEE_FILE`, `EMPLOYEE_SELF`, `PAYROLL_FY` exports (EQ-EXPORT-1.0); alias of `POST /v1/exports` (Appendix AC §AC.13.3) | owner (step-up); employee for own file |
| `POST /v1/chm/{tenantId}/offboarding` · `GET …/offboarding/{id}` | Tenant offboarding | owner (step-up) |

### 7.4 Domain events

Catalogue and payload rules: §W.12 (context `chm`; IDs, versions and counts only — never salary amounts, bank details, enquiry text or case content). Outbox → CloudEvents; consumers idempotent. **No subscription from `neutrals`, allocation or the institutional directory** (CI `NO_CHM_READ_IN_ALLOCATION`).

### 7.5 Temporal workflows and jobs

| Workflow / job | Trigger | Steps and timers |
|---|---|---|
| `PagePublishWorkflow` | Approve / scheduled publish | Render per locale → store renditions and hashes → CDN invalidation (≤ 60 s) → sitemap update → event |
| `NightlyPracticeLintJob` | Daily 02:00 IST | Crawl published pages → lint → open findings → day-7 `suspended_lint` with restore |
| `DomainLifecycleWorkflow` | Add host | Poll TXT/CNAME/CAA (every 10 min for 72 h, then hourly up to 14 days) → ACM request → attach → daily health → T-30/14/7 renewal alerts → release |
| `MarketplaceEligibilityJob` | On relevant change + daily | Recompute `sponsored_eligible` and reasons → event to P19 |
| `EnquiryRetentionJob` | Daily | Erase unconverted enquiries past retention |
| `ConfigApprovalWorkflow` | G submit | Validators → legal approver signal → publish version → pin for new matters |
| `StaffProvisioningWorkflow` | Invitation | Owner approval signal for privileged roles → acceptance of undertakings → grants → access event |
| `StaffExitWorkflow` | Exit recorded | Revoke sessions, grants, delegations at exit timestamp → reassign tasks and assignments → F&F clock (2 working days) → gratuity clock (30 days) → service certificate clock |
| `ComplianceWizardJob` | Monthly (1st working day) + on headcount change | Headcount by class → duties on/off → tasks for new duties → event |
| `ChambersPayRunWorkflow` | Period open | Steps 1–12 of §W.6.8 with human signals for submit, approve, release; D3-18 gap timer and 24 h anomaly hold; deadline alerts at D-5, D-2 before pay date |
| `BankChangeWorkflow` | Bank change request | Penny-drop → notifications → confirmation signal → working-day cooling timer → activation or freeze |
| `ConsultantTdsJob` | Each payment + quarter-end | YTD threshold tracking → TDS lines → Form 140 data → Form 131 certificates |
| `GhostCheckJob` | Weekly + every run | Integrity checks of §W.6.8 step 5 |
| `ControlExceptionDigestJob` | Monthly | Summary of `chm.control_exceptions` to owner and external checker |
| `PracticeExportWorkflow` | Export request | Approval signal (sensitive scopes) → bag build → validation → delivery link (7-day bucket lifecycle) |
| `TenantOffboardingWorkflow` | Offboarding request | §W.15.4 states with 14-day download timer, 90-day run-off, domain release, 30-day erasure timer, legal-hold signal |

---

## 8. Integrations (ports and adapters)

| Port | Use in P20 | Default adapter | Fallback / failure behaviour |
|---|---|---|---|
| `PAYOUT_PORT` (Appendix D §D.4.2; renamed from draft `DISBURSAL_PORT` under X-49) | Salary and consultant disbursal | `bank_file` (generic NEFT/RTGS CSV + bank templates as data; shared with Appendix Z payroll) | `payout_api` adapter on a chambers-owned account behind flag OFF **[VERIFY — W-OI-06]**; on API failure, the run falls back to bank file with a new hash |
| `ACCOUNTING_PORT` (Appendix AC) | Payroll, invoice and receipt journals | Generic CSV/XLSX mapping; `tally_file`, `zoho_books` | Named-package adapters behind flags **[VERIFY — vendor import formats]** |
| `PAYROLL_EXCHANGE_PORT` (Appendix Z) | Employee master, pay register and YTD exchange with specialist payroll tools | `generic_csv` | Import rejected with row-level difference report |
| `KYC_PORT` | Penny-drop bank verification; PAN validation | P01/P05 provider | Manual verification with document evidence; payment blocked until verified |
| `TAX_INVOICE_PORT` | IRN for chambers invoices when e-invoicing applies | P05 provider | Queue with 20-day IRN alert (P05) |
| `PAYMENTS_PORT` | Chambers fee collection via Route linked account | Razorpay Route (P05) | Cashfree Easy Split (P05) |
| `ESIGN_PORT` | Offer letters, appointment letters, policy acknowledgements (click-wrap allowed for non-legal acknowledgements), templates | P06 provider | Fallback ESP (P06) |
| `EMAIL_PORT`, `MESSAGING_PORT`, `PUSH_PORT` | Bank-change out-of-band notices, approvals, payslip availability, enquiry acknowledgements | P07 defaults | Fallback per P07; out-of-band bank notices must reach at least one channel or the change stays in cooling |
| `TRANSLATION_PORT` | Machine drafts of page locales | Sarvam | Manual translation; locale stays unpublished |
| `WORKSPACE_PORT` / `STORAGE_PORT` | Calendar busy/free sync (`WORKSPACE_PORT`); export push to SharePoint/OneDrive/Drive (`STORAGE_PORT`, Appendix AC §AC.11.8) | Microsoft 365 (Graph) / Google Workspace (per RD) | Sync disabled with banner; exports downloadable |
| DNS / ACM / CloudFront | Custom domains | AWS ACM DNS validation, multi-tenant distribution (P10) | Equator host stays canonical |
| P18 engine interface | Payroll calculation | `packages/rules/payroll` and `packages/rules/leave` (X-58) with Appendix Z rule packs from `cfg` | No fallback: run cannot be calculated; incident raised |
| P19 marketplace interface | Projection and eligibility read | Internal (`machine` identity) | Projection hidden on P19 until healthy |
| P03 blind-check interface | Enquiry and assignment conflict checks | Internal | Manual declaration required; enquiry stays in `conflict_check` |

Every port declares a system of record per data category, a field mapping, import/export and a migration rehearsal (NN-40).

---

## 9. Configuration surface

The complete chambers catalogue (≈ 170 keys with tier, who may change, default and bounds) is §W.8 and is registered in the P15 framework. Items with the highest risk:

| Item | Tier | Default | Approver / guardrail |
|---|---|---|---|
| Label deny-list, lint rules, theme validator, schema allow-list | L | Platform | Equator `legal_reviewer` (platform rule packs) |
| `chambers.court_label_override` | G (per tenant) | OFF | Equator counsel opinion |
| `chambers.pages.show_equator_panel_status` | L platform flag | OFF | Counsel + Transparency sub-committee |
| `marketplace.paid_placement` | G platform flag (P19); not tenant-editable (`.advocates` is L, always OFF) | OFF | Board + counsel (NN-34; Appendix AA §AA.15) |
| `tenant.chm.pages.r36_indexing` | G | `noindex` | Counsel (W-OI-01) |
| `tenant.chm.pages.process_feedback_block` | G | OFF | Legal approver; n ≥ 10 |
| Rules, fee schedules, award/settlement templates, status labels, procedural notices | G | Templates | D3-16 legal approver after validators |
| `tenant.chm.hr.enabled` | T (entitlement-gated) | OFF | Appendix AB stream RS-10 must be `live` |
| `tenant.chm.payroll.rule_packs` | L | Latest approved | Appendix Z owner; `NOT_CONFIRMED` blocks runs |
| `tenant.chm.payroll.payout_api` | G | OFF | Owner; tenant-owned account; W-OI-06 |
| `tenant.chm.bank_change.cooling_working_days` | T | 3 | 1–7 (L bounds) |
| `tenant.chm.control.single_person_min_gap_minutes` / `anomaly_hold_hours` | L | 10 / 24 | D3-18 |
| `tenant.chm.attendance.prohibited_monitoring` | L | Not available | NN-35 |
| `tenant.chm.offboarding.runoff_days` | L | 90 | ≥ 60 |

Blank parameters (prices of add-ons, included counts, GST thresholds, TDS due dates, State forms): unset → the dependent feature is unavailable or the calculation is blocked, never silently defaulted.

---

## 10. Security, privacy and audit

- **Tenancy and walls:** RLS on every `chm` table; HR tables require `app.hr_scope`; separate DB role for HR services; Cerbos hard denials of §W.14; Equator staff never read HR or salary data (processor access to encrypted storage only; break-glass with tenant notification and DPO review).
- **Encryption:** per-tenant data keys (KMS envelope) for salary amounts, bank accounts, tax declarations and payslips; HR documents on a separate S3 prefix and key; Aadhaar never stored in full (NN-14); PAN masked in UI and logs.
- **Authentication:** MFA mandatory for all chambers roles; passkey step-up for privileged grants, pay-run approvals, disbursal, bank-change exceptions, sensitive exports, domain changes and offboarding; sessions revoked immediately at exit.
- **Fiduciary roles:** the chambers is data fiduciary for its matters, enquiries, practice pages and staff; Equator is processor under the DPA (Appendix N §8.5 cl.1, cl.7); Equator is an intermediary for hosted page content (IT Rules 2021 r.3). Staff privacy notice and monitoring notice generated from enabled sources (DPDP Act s.5 format; NN-35).
- **Data minimisation:** enquiries hold only what is needed for a conflict check and reply; marketplace projection only consented fields; events carry IDs only.
- **Audit:** hash-chained events for every material action; un-disableable edit logs on billing, ledger and payroll tables (NN-36); salary reads logged and visible to the employee on request; page snapshots and DNS evidence retained.
- **Retention:** §W.15.2; erasure 30 days after tenant closure unless legal hold; employer's own statutory retention duties stated in the export README.
- **Security testing:** VAPT scope includes the page renderer (stored XSS through blocks, SVG sanitiser, link handling), custom-domain takeover (dangling CNAME after release — mitigated by releasing the alternate domain before removing records and by TXT re-verification), CSV/formula injection in bank files and exports (cells beginning with `=`, `+`, `-`, `@` escaped), IDOR across `chm` endpoints, and the HR/case wall.

---

## 11. AI touchpoints and guardrails

| Touchpoint | What AI may do | Guardrails |
|---|---|---|
| Page copy assistant | Suggest plain-language rewrites of tenant-authored text; suggest FAQ wording from the tenant's rules | Runs lint on every suggestion; never generates credentials, statistics, fees or outcome language; suggestions labelled; human accepts each change (NN-01) |
| Translation drafts | Draft locale versions via `TRANSLATION_PORT` | Labelled draft; human review before publish; legal pages need the legal approver |
| Rules import | Segment uploaded DOCX into clauses and label clause types | Human confirms every clause; validator runs on the confirmed text; original preserved (NN-32) |
| Enquiry triage | Classify dispute type and language for routing | No merits assessment, no advice, no prediction (NN-01 GX-1–GX-3); enquirer sees no AI output |
| HR summaries | Summarise an employee's own goal notes for the manager on request | Never proposes ratings, never uses attendance telemetry; excluded from payroll calculations entirely |
| Payroll | None | Payroll is computed only by the deterministic P18 engine |

All AI calls run through the AI Gateway (Bedrock India, P11 policies), with no case content in page-assistant prompts, no HR data in any prompt except the HR-summary feature (tenant opt-in, T, default OFF), per-feature kill switches and logging.

---

## 12. Acceptance criteria (Gherkin)

```gherkin
Feature: Phase P20 — Chambers workspace v3 and Practice HR (tests/acceptance/p20/)

Scenario: Court naming blocked on a practice page
  Given a chambers_admin edits the hero of "/chambers/jaipur-adr"
  When the H1 is set to "Jaipur Private Arbitration Court"
  Then publish fails with code "CHM_COPY_LINT_BLOCKED" citing "CHM-LINT-01"
  And no override control is offered

Scenario: Outcome statistic blocked
  Given a draft bio says "92% of my mediations settle"
  When the version is submitted
  Then the response is 422 with code "CHM_COPY_LINT_BLOCKED" citing "CHM-LINT-03"

Scenario: Advocate-neutral page runs in BCI r.36 mode
  Given a person verified as enrolled with a State Bar Council
  When the person page is rendered
  Then only Schedule fields appear in the bio
  And the fee_schedule, availability and enquiry_form blocks are unavailable with code "CHM_BLOCK_NOT_ALLOWED_FOR_REGIME"
  And the page carries robots "noindex"
  And marketplace eligibility is false with reason "REGIME_RESTRICTED"

Scenario: Institutional profile never links to a practice page
  Given neutral N is empanelled with Equator and owns a published practice page
  When "/neutrals/{N}" renders
  Then the HTML contains no link to any "/chambers/" path or the tenant's custom domain

Scenario: Theme contrast enforced
  Given brand.primary "#7FB3D5" on surface "#FFFFFF" for body text
  When the theme is validated
  Then the response is 422 with code "CHM_THEME_CONTRAST_FAIL" listing the failing pair and ratio

Scenario: Custom domain blocked by CAA
  Given a CH-PRO tenant adds "www.example-adr.in" whose CAA record allows only another CA
  When verification runs
  Then the status stays "pending" with code "CHM_DOMAIN_CAA_BLOCKS_ISSUANCE" and the CAA line to add

Scenario: HR role cannot open case content
  Given user H holds only chambers_hr
  When H requests a document in matter CH/COM/2026/00012
  Then the response is 403 with code "CHM_CONFIDENTIALITY_WALL"
  And the denial is written to audit.access_log

Scenario: Case manager cannot read salary
  Given user C holds chambers_case_manager
  When C requests the salary assignment of staff record S
  Then the response is 403 with code "CHM_SALARY_ACCESS_DENIED"

Scenario: Pay run blocked by an unconfirmed parameter
  Given the tenant has 22 employees and bonus is due
  And the rule pack parameter "cow.bonus.eligibility_wage_ceiling" is NOT_CONFIRMED
  When HR calculates the run
  Then approval is blocked with code "CHM_PAYRUN_PARAM_UNCONFIRMED" naming the parameter

Scenario: No professional tax for a Delhi establishment
  Given establishment_state "IN-DL" and pt_state_rule "establishment_state"
  When the run is calculated
  Then no professional tax line is produced for any employee

Scenario: Deduction cap
  Given wages of ₹20,000 and requested deductions of ₹12,500 in the period
  When the run is calculated
  Then deductions of ₹10,000 are applied and ₹2,500 is deferred to the next period with a schedule visible to the employee

Scenario: Bank change cooling and reversal
  Given employee E changes their bank account on Monday with a name match of 0.93
  Then the account is "pending_cooling" until the end of the third working day
  And E's registered email and phone receive a reversal link
  When the link is used
  Then the account becomes "frozen" and the previous account remains active

Scenario: Sole practitioner approves a pay run
  Given a tenant with one natural person holding all roles
  When the owner submits a run and tries to approve it 3 minutes later
  Then the response is 409 with code "CHM_SINGLE_PERSON_GAP"
  When the owner approves after 10 minutes with a passkey step-up
  Then the run is "approved" with single_person = true
  And a "SINGLE_PERSON_SOD" control exception is recorded

Scenario: Two-person tenant cannot self-check
  Given users H (chambers_hr) and O (chambers_owner)
  When H submits a run and H attempts to approve it
  Then the response is 403 with code "CHM_MAKER_CHECKER_SAME_USER"

Scenario: Leave policy below floor rejected
  Given a 12-worker establishment and a custom policy granting earned leave of 1 day per 25 days worked
  When the policy is validated
  Then the response is 422 with code "CHM_LEAVE_POLICY_BELOW_FLOOR" citing OSH Code s.32

Scenario: Prohibited monitoring cannot be enabled
  When an owner calls PUT settings "tenant.chm.attendance.keystroke_logging"
  Then the response is 403 with code "CHM_MONITORING_PROHIBITED" and canonical_code "HR_MONITORING_PROHIBITED"

Scenario: Invoice series respects CGST Rules r.46
  When accounts sets the series prefix "JAIPURADR/2026-27/" with a 5-digit serial
  Then the response is 422 with code "CHM_INVOICE_SERIES_INVALID"

Scenario: Numbering format immutable after first issue
  Given matter numbers have been issued under "{PFX}/{VERT}/{YYYY}/{SEQ:5}"
  When the admin edits that format
  Then the response is 409 with code "CHM_NUMBERING_IMMUTABLE"

Scenario: Payout API needs a chambers-owned account
  Given payout_api is enabled and the payout account KYC name is a different entity
  When a disbursal is attempted
  Then the response is 422 with code "CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED"

Scenario: Offboarding export is complete and valid
  Given a tenant with 40 matters, 6 staff and 14 payroll months
  When the owner starts offboarding
  Then an EQ-EXPORT-1.0 bag is produced whose manifest verifies
  And data/ contains 00_Contents.xlsx and the Appendix AC folders 01_Organisation_Profile, 02_People_and_Roles, 03_Cases, 04_Billing_and_Subscriptions, 05_Operations, 07_HR_and_Payroll, 08_Reports and 09_Settings_and_Configuration
  And the root folder name is at most 40 characters and every path below the root is at most 140 characters

Scenario: Allocation never reads chm
  When the CI test "NO_CHM_READ_IN_ALLOCATION" runs
  Then no import, query or event subscription from the neutrals or allocation modules to schema "chm" or context "chm" exists

Scenario: Reserved slug refused
  When a prospect registers the slug "admin"
  Then the response is 409 with code "CHM_SLUG_RESERVED"

Scenario: Sponsored eligibility stays false while the platform flag is OFF
  Given a general-regime chambers has opted into the marketplace and meets every other condition
  And "marketplace.paid_placement" is OFF
  When MarketplaceEligibilityJob runs
  Then sponsored_eligible is false with reason "FLAG_OFF"
  And no page of the chambers renders any sponsorship label

Scenario: Locale cannot publish unreviewed
  Given a Hindi rendition was machine-drafted and not marked reviewed
  When the approver publishes the version
  Then the response is 409 with code "CHM_LOCALE_NOT_REVIEWED"

Scenario: Tribunal secretary needs an instruction
  Given user T holds chambers_staff with sub-template "tribunal_secretary"
  And no instruction artefact exists for matter M
  When the admin assigns T to M
  Then the assignment is refused until the presiding arbitrator's instruction is uploaded and the party disclosure notice is sent

Scenario: Delegation cannot carry salary access
  When the owner delegates "salary.read" to the admin
  Then the response is 403 with code "CHM_DELEGATION_SCOPE_EXCEEDED"

Scenario: ESI switches on at ten employees
  Given a chambers with 9 employees and ESI off
  When a tenth employee joins and ComplianceWizardJob runs
  Then the ESI duty is on with a registration task showing its source and verification status
  And for an employee with statutory wages of ₹18,000 the run shows employee ESI ₹135 and employer ESI ₹585

Scenario: EPF ceiling split month
  Given an EPF-covered employee with statutory wages of ₹30,000 for September 2026
  And the rule pack applies calendar-day pro-rating for the ceiling change on 17 September 2026
  When the run is calculated
  Then the EPF wage ceiling applied is ₹19,666.67 (₹15,000 × 16/30 + ₹25,000 × 14/30)
  And the owner must acknowledge the SECONDARY_ONLY parameter before approval

Scenario: Consultant TDS threshold
  Given consultant K was paid ₹30,000 earlier in the tax year
  When a fee note of ₹25,000 is approved
  Then TDS under ITA 2025 s.393(1) Table Sl. 6(iii) is computed as the rule pack version in force specifies
  And K appears in the next Form 140 data set

Scenario: Full and final clock
  Given employee E resigns with exit date 12 January 2027
  Then an F&F run is opened with a deadline of two working days after the exit date
  And the owner is alerted when half of that period has passed without approval

Scenario: HR add-on unavailable while its stream is draft
  Given the Appendix AB stream "RS-10" has status "draft"
  When an owner tries to set "tenant.chm.hr.enabled" to ON
  Then the response is 403 with code "CHM_ENTITLEMENT_REQUIRED"

Scenario: Domain release leaves no dangling host
  Given a tenant with an active custom domain completes run-off
  When the domain release step runs
  Then the alternate domain is removed from the distribution before the owner is shown the DNS records to delete
  And "/chambers/{slug}" serves the tombstone page for 90 days and then 410
  And the slug is quarantined for 12 months

Scenario: Payslips released only on or before payment
  Given an approved run with pay date Friday 29 January 2027 (last working day)
  When disbursal is reconciled on 29 January 2027
  Then payslips are released no later than that date
  And an employee who opens ESS sees the payslip with the rule-pack version line
```

---

## 13. Deliverables and exit gate

- [ ] Migrations for schema `chm` (§W.10.1) with RLS, HR-scope policies, separate `chm_hr_svc` DB role, field-level encryption, triggers (numbering immutability, bank activation, D3-18 assertions, control exceptions) and grant tests proving the `cases` and `neutrals` DB roles have no `chm` HR grants.
- [ ] `chm` module and sub-modules; OpenAPI for §7.3; `CHM_*` codes registered in Appendix F §F.10.4; events registered in the Appendix F catalogue.
- [ ] Practice page renderer (SSR/SSG), 21 blocks + flag-gated `process_feedback`, regime engine, theme validator, domain lifecycle, sitemaps, JSON-LD, hreflang, tombstones; `chambers_practice` lint profile in `packages/content-lint`.
- [ ] Settings catalogue §W.8 registered in P15 with tier badges, approvals and rollback; D3-16 legal-approver capability.
- [ ] Rules, fees, templates, intake, notifications, numbering, letterheads, e-sign, invoicing, payments, status labels and portal branding configuration (§W.4).
- [ ] Role templates, migration of v2 seats, invitations, case assignments, delegations, queues, tasks, calendars, SLAs, workload, SoD engine (§W.5).
- [ ] Practice HR: compliance wizard, staff records, checklists, attendance, leave, salary, pay-run workflow on the P18 engine, payslips, `PAYOUT_PORT` `bank_file` adapter, bank-change protocol, single-person controls, consultant TDS, goals, reviews, policies, accounting exports (§W.6).
- [ ] Dashboards and reports (§W.7); entitlements from the Appendix AB registry (§W.9).
- [ ] Exports `CHAMBERS_TENANT` (alias `CHAMBERS_PRACTICE`), `EMPLOYEE_FILE`, `EMPLOYEE_SELF`, `PAYROLL_FY` (EQ-EXPORT-1.0, Appendix AC §AC.13 taxonomy) and the offboarding workflow with domain and slug release (§W.15).
- [ ] Phase addenda implemented in P03, P05, P10, P12 and P13 (§W.18).
- [ ] Mobile tabs "Work", "Me", "Approvals" with screen protection on payslips.
- [ ] Seed data: 6 chambers tenants (sole general-regime mediator in Delhi; advocate-neutral sole practice in Jaipur — `bci_r36`; CA-neutral practice — `icai`; 4-person arbitration chambers in Mumbai with 3 staff; 12-person institution-style centre in Bengaluru with 12 employees; chambers with a custom domain), synthetic matters, 3 months of synthetic payroll per HR-enabled tenant.
- [ ] `docs/phases/P20-demo.md`; all Gherkin green; axe clean on SCR-P20-01/04/06/23/27; VAPT findings (renderer, SVG, domain takeover, CSV injection, IDOR, HR wall) closed or risk-accepted by the CTO and DPO.

**Exit gate:**

1. A CH-SOLO sole practitioner signs up, publishes a lint-clean bilingual practice page and receives a test enquiry in one session; the same neutral's institutional profile shows no link to it (crawl evidence).
2. The advocate-neutral seed tenant cannot add a fee block, enquiry form or photo, its pages are `noindex`, and its marketplace eligibility is false with `REGIME_RESTRICTED`.
3. The Mumbai chambers runs two consecutive monthly payrolls end to end — calculation, two-person approval, bank file, acknowledgement reconciliation, payslips, statutory outputs — with the rule-pack versions recorded on every line, and an F&F run within 2 working days.
4. The Delhi sole practitioner runs a payroll under D3-18 controls with the exception log exported; an attempted self-approval inside 10 minutes is refused.
5. `CHM_CONFIDENTIALITY_WALL_MATRIX` (every HR/accounts role × every case resource = 403), `NO_CHM_READ_IN_ALLOCATION` and extended `NO_PAID_PLACEMENT` pass in CI.
6. A full `CHAMBERS_TENANT` export of the Bengaluru tenant validates (bag valid, hashes match, root ≤ 40 and paths below root ≤ 140 characters, AC §AC.13.7) and opens in Microsoft Office without repair prompts; offboarding of the custom-domain tenant completes with the domain released and the slug quarantined.
7. The RS-10 stream stays `draft` until payroll UAT sign-off by the Company Secretary and the chambers' CA reviewer for the pilot tenant.

---

## 14. Open items and legal verification flags

Appendix W §W.17 lists W-OI-01 to W-OI-18 with defaults, approvers and dispositions; they gate this phase as follows:

| ID | Gate in P20 |
|---|---|
| W-OI-01, W-OI-02 | `bci_r36` restricted mode ships as default; `tenant.chm.pages.r36_indexing` stays `noindex` until counsel |
| W-OI-03 | `chambers.pages.show_equator_panel_status` stays OFF |
| W-OI-04 | Tribunal-secretary instruction and disclosure required |
| W-OI-05, W-OI-13 | GST and TDS parameters flagged `SECONDARY_ONLY` or unset; composition blocked; contractor TDS disabled |
| W-OI-06, W-OI-07 | `payout_api` OFF; only the generic bank file ships until bank templates pass UAT |
| W-OI-08, W-OI-09, W-OI-10, W-OI-11, W-OI-12 | Payroll pilot limited to Delhi and Maharashtra establishments whose parameters are `VERIFIED` or acknowledged; wizard captures registration evidence |
| W-OI-14, W-OI-15 | 8-year default retention; verification stubs retained minimally |
| W-OI-16 | Add-ons not purchasable until the Board approves prices |
| W-OI-17 | Marketplace projection labels comply in full from launch |
| W-OI-18 | No referral rewards to advocate tenants in any P20 flow |

Phase-specific items:

- **P20-OI-01** Interface contracts with P15 (settings registration API), P18 (engine function signatures, rule-pack resolution by jurisdiction and date) and P19 (projection schema, eligibility attributes) must be frozen before sprint 2. **[VERIFY — open: owners W1, W5, W6]**
- **P20-OI-02** Resolved in review (23 Oct 2026): Appendix Z uses `PAYOUT_PORT` with a shared `bank_file` adapter; the draft `DISBURSAL_PORT` name is withdrawn (X-49). Appendix D §D.4.2 to list the `bank_file` adapter.
- **P20-OI-03** Mobile payslip screen protection on iOS relies on app-switcher blur only (no OS-level screenshot block); disclose in the employee privacy notice.
- **P20-OI-04** The effort estimate assumes P18 delivers a stable engine package by P20 sprint 3; otherwise Practice HR moves to a follow-on release while pages, configuration and staff management ship.
