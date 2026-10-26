# SEED_CREDENTIALS — UDOFIN (UDF) — issued by the pack lead on 26 October 2026 (Udofin Master Prompt v1.3; IPB-11 §11.4.6 shape)

> **Gitignored and blocked by the repository ruleset** (`.gitignore` and `.git/info/exclude`; the `secrets-scan` CI check fails on any file containing these values). Do not paste into chats, tickets, pull requests, wikis or logs.
> **Valid for environments:** local, dev, test, demo, staging. **Production and DR never use this file:** boot refuses `SEED_ENABLED=true` or any `SEED_PROFILE` when `APP_ENV` is `prod` or `dr`, and the super admin's production account is created by invitation link, not seeded (IPB-D-04).
> **Passwords:** issued by the lead, 24+ characters, unique per persona and per product (never reuse a Finbyx, LawDocs or Operations Hub value). Also stored at `SEED_VAULT_PREFIX/<persona>`; tests read them from the vault at runtime through the `SECRETS` port, never from this file.
> **First login in staging, demo or production:** a password change and MFA enrolment (TOTP or passkey) are forced before any other action; the seeded value then stops working. Rotation is recorded in the log at the end of this file.
> **Scope:** platform roles are IPB-11 personas mapped to Udofin channels (Part 3.2); test personas live in the `demo` RE tenant (`re_demo_01`, a portal-only RE on synthetic data) except the borrower, who is a consumer with no tenant.

## Personas

| Persona | Role (IPB / Udofin) | Email | Password | Tenant | Channel | Environments |
|---|---|---|---|---|---|---|
| Super admin | `PLT_SUPER_ADMIN` (Udofin platform administration) | rjnprajapati@gmail.com | `jUwAf3i32^9Ien*6ga8NbGO=b6` | platform | F | local, dev, test, demo, staging (prod: invitation link, not seeded) |
| Tenant admin (platform operations owner) | `ORG_OWNER` / Udofin ops admin (`OPS_ADMIN`) | test.tenant_admin@udofin.test | `sY7yD4Do3=&UL3moNm0Ev0&@A3` | udofin (operator) | C | local, dev, test, demo, staging |
| RE admin (lender) | `ORG_ADMIN` of the demo RE (`RE_ADMIN`) | test.re_admin@udofin.test | `Vg^tWe3sKZPKAW6PmDiWobrHu8` | re_demo_01 | D | local, dev, test, demo, staging |
| Borrower | consumer (`BORROWER`); Hindi display name "परीक्षा उधारकर्ता", `plain_language` on, easy-read on | test.borrower@udofin.test | `#HRZyJ2yUL9Jd^xnmD!D#$a%-q` | — (consumer) | A, B | local, dev, test, demo, staging |
| Grievance officer | `ORG_MAKER` with grievance scope (Udofin nodal GRO desk) | test.grievance_officer@udofin.test | `EZimWE0mDN8V-m48MGPLI^ZQv3` | udofin (operator) | C | local, dev, test, demo, staging |
| Ops user | `ORG_MEMBER` (Udofin operations analyst; partner onboarding, Work Inbox) | test.ops@udofin.test | `25X5MWSf+fYfQl0fbwB1IRCHdu` | udofin (operator) | C | local, dev, test, demo, staging |
| Auditor (read-only) | `ORG_AUDITOR_RO` (RE auditor grant on re_demo_01; RA2 30-day grant seeded) | test.auditor_ro@udofin.test | `&=+2*Otn9rwej6TuaOJoV$&Kqk` | re_demo_01 | G | local, dev, test, demo, staging |
| Content editor | `PLT_CONTENT_EDITOR` (Studio: pages, blog, resources; no legal approval right) | test.content_editor@udofin.test | `zxRQ2DzzK6l=^SxYrcei6-oAOp` | platform | F | local, dev, test, demo, staging |

Personas the IPB-11 template lists but the lead has **not** issued credentials for (security officer, release manager, legal reviewer, DPO, platform grievance officer, platform auditor, tenant maker, tenant checker, sandbox owner, second borrower, RE partner read-only) are created by `pnpm seed --profile dev` with **randomly generated** passwords written only to the vault, never to this file, until the lead issues values. The super admin holds every platform role in non-production until then.

## Borrower OTP in non-production

The borrower persona signs in with mobile OTP. In local, dev, test and demo the SMS adapter is `none` and the OTP for seeded numbers is read from the vault key `SEED_VAULT_PREFIX/otp-fixed` (set by the seed run; six digits). No fixed OTP exists in staging; use the MailHog or SMS sandbox capture. The password above is the borrower web-app fallback credential only where `AUTH_BORROWER_PASSWORD_LOGIN_NONPROD=true`.

## Service accounts (no passwords; client credentials in the vault only)

| Identity | Role | Client ID | Vault path |
|---|---|---|---|
| Vidhi agent | `AGT_VIDHI` | udf-agt-vidhi | `SEED_VAULT_PREFIX/agt-vidhi` |
| OH billing link | `SVC_BILLING` | udf-svc-billing | `SEED_VAULT_PREFIX/svc-billing` |
| Finbyx connector (demo RE) | `SVC_LMS_CONNECTOR` | udf-svc-lms-finbyx | `SEED_VAULT_PREFIX/svc-lms-finbyx` |
| LawDocsComply bridge | `SVC_GRC` | udf-svc-grc | `SEED_VAULT_PREFIX/svc-grc` |
| Equator ODR | `SVC_ODR` | udf-svc-odr | `SEED_VAULT_PREFIX/svc-odr` |

## Demo narrative seeded with these personas (IPB-11 §11.4.8; Udofin note)

Two REs (`re_demo_01` portal-only; `re_demo_02` on the Finbyx mock connector) publish catalogues; the borrower has one disbursed loan from `re_demo_01` with the cooling-off period active, one application at `OFFERS_SHOWN` with offers from both REs (ranked APR low to high; one unmatched RE listed with reason), one open grievance at tier T1 (RE clock running), one KFS acknowledged, consents given for two purposes and one withdrawn. The KFS signing key is local self-signed (`UDF_KFS_SIGNING_KEY_REF` → `secret://env/.../kfs-dev`). No real person, PAN, Aadhaar, account or bureau data appears anywhere; all identifiers are synthetic and pass the `pii-scan` fixture check.

## Rules (binding)

1. `pnpm seed` and `pnpm seed:credentials` refuse to run when `APP_ENV` is `prod` or `dr`, when `SEED_ENABLED` is not `true`, or when the database host matches a production host pattern.
2. Seed persona emails (`*@udofin.test`) are on the production invitation deny-list; an attempt to invite one in production is refused and logged.
3. On first login in staging, demo or production the user must change the password and enrol MFA; the seeded password is then invalid.
4. Never echo, `cat` into a transcript, or paste any value from this file into a commit, PR, chat or log. Claude Code reads values from the vault at runtime.
5. Rotation: `pnpm seed:credentials --rotate` regenerates every non-issued password; lead-issued values are rotated only by the lead and recorded below.

## Rotation log

| Date | Run id | Rotated by | Reason |
|---|---|---|---|
| 2026-10-26 | lead-issue-v1.3 | Pack lead | Initial issue for Udofin v1.3 (eight personas) |
