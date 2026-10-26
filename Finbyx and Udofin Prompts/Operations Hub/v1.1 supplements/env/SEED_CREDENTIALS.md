# SEED_CREDENTIALS — OH (Infrabyx Operations Hub) — issued 26 October 2026 by the pack lead (v1.1; seed run id to be recorded by `pnpm seed:credentials --import` on first use)

> **Gitignored and blocked by the repository ruleset (`**/SEED_CREDENTIALS.md`).** Do not paste into chats, tickets, wikis, commit messages or pull requests. Store a copy only in the seed vault (`SEED_VAULT_PREFIX`) and the team password manager (IPB-11-36).
> **Valid for environments: local, dev, test, demo, staging. Production never uses this file.** `pnpm seed` and `pnpm seed:credentials` refuse when `APP_ENV` is `prod` or `dr` or when `SEED_ENABLED != true` (IPB-11-14, IPB-11-22). The production super admin is created by the identity bootstrap with a one-time invitation link, forced password change and mandatory MFA enrolment on first login (IPB-11-32; IPB-D-04).
> **Passwords:** 26 characters, CSPRNG, unique per persona and per product, never derived from the email (IPB-11-34). **First-login rotation:** in staging and demo every account has `must_change_password=true` and `mfa_required=true`; in local, dev and test MFA is disabled for personas except the super admin, who always requires TOTP (seeded secret in the vault) (IPB-11-37). Credentials rotate automatically on every demo or staging reseed and on demand with `pnpm seed:credentials --rotate` (IPB-11-38).
> Email domain `opshub.test` is a reserved `.test` TLD (RFC 2606); mail never leaves. Product-scope assignments shown are seed data for the IPB-D-12 isolation tests.

## Human personas

| Persona | Role (Hub) | Email | Password | Tenant | Product scope(s) | Environments |
|---|---|---|---|---|---|---|
| Super admin (owner) | `PLT_SUPER_ADMIN` | rjnprajapati@gmail.com | `s@sV-*1-KUA5os4yU@Chj74DFn` | platform (Infrabyx) | GRP (all, aggregate) | local, dev, test, demo, staging (prod: invitation link, not seeded) |
| Operations admin | `OPS_ADMIN` (Hub administrator, workspace P) | test.ops_admin@opshub.test | `JsBveaC7WOmv^Ef8dnMAq7g+KP` | platform | GRP | local, dev, test, demo, staging |
| Relationship manager | `OPS_SALES` (workspace I; account executive) | test.rm@opshub.test | `!BMyKX7WTFj&_RY*hawgZgsnK+` | platform | **FBX only** (used in the "FBX RM cannot read an LD ticket" test) | local, dev, test, demo, staging |
| Support agent | `OPS_SUPPORT` (workspace E; L1–L2) | test.support_agent@opshub.test | `BCUaW_c_eWa#OjvwlOOpT4WSR=` | platform | **LD only** | local, dev, test, demo, staging |
| HR administrator | `OPS_HR` (workspace K; HR maker and checker roles split in tests) | test.hr_admin@opshub.test | `69AcqOnGd&_2MM%jIVFKthwiFK` | platform | GRP (HR is scoped by employing entity, not product) | local, dev, test, demo, staging |
| Payroll maker | `OPS_PAYROLL_MAKER` (workspace K) | test.payroll_maker@opshub.test | `tl-FcMlN*=Juo83-LnYxtyvsav` | platform | GRP | local, dev, test, demo, staging |
| Payroll checker | `OPS_PAYROLL_CHECKER` (HR head or CFO delegate; never releases the bank file) | test.payroll_checker@opshub.test | `M^9iEo=VmFWnL9VClvq7wsxTcQ` | platform | GRP | local, dev, test, demo, staging |
| Marketing | `OPS_MARKETING` (workspaces F–H) | test.marketing@opshub.test | `-Pb#^eGVoBn^nf2FAb9VSy#MFJ` | platform | LD, LDC (two scopes, for switcher tests) | local, dev, test, demo, staging |
| Intern | `OPS_INTERN` (employee self-service; intern programme persona, OH10.11) | test.intern@opshub.test | `dGuO1Um@AMn^1=xOC!R!DqY&4z` | platform | UDF | local, dev, test, demo, staging |
| Employee | `OPS_EMPLOYEE` (employee self-service; delivery team member, workspace B/Q) | test.employee@opshub.test | `HfjI&D1Xp_l@3W4aqYJ&D2Y9*g` | platform | FBX | local, dev, test, demo, staging |
| Internal auditor (read-only) | `PLT_AUDITOR_RO` (workspace O) | test.auditor_ro@opshub.test | `TGUeXAENjgkyOHMKinLJVQqp7+` | platform | GRP (aggregate; read-only) | local, dev, test, demo, staging |

Notes: the eleven personas above are the lead-supplied set and are the only human logins seeded. Where the IPB-11 §11.4.5 template names further platform personas (`plt_security`, `plt_release`, `plt_content`, `plt_legal`, `plt_dpo`, `plt_grievance`), the seed assigns those **roles** to the super admin in `local`, `dev` and `test` and to `test.ops_admin` in `demo` and `staging` for maker-checker tests, with the checker role always on a different account from the maker. No additional passwords are invented. The product-scope column drives the seeded `staff_product_assignment` rows; the demo client "Demo Co" (an NBFC-ML, IPB-11 §11.4.8) is seeded under `FBX` and `LDC`, and the five sibling products are seeded as customers.

## Service accounts (no passwords; client credentials in the vault only — IPB-11-39)

| Identity | Role | Client ID | Vault path |
|---|---|---|---|
| Vidhi agent (OH16) | `AGT_VIDHI` | oh-agt-vidhi | `<SEED_VAULT_PREFIX>/agt-vidhi` |
| Equator conflict-check machine client (OH1.6) | `SVC_EQ_CONFLICT` | oh-svc-eq-conflict | `<SEED_VAULT_PREFIX>/svc-eq-conflict` |
| Product billing links (OH8 server side) | `SVC_BILLING` | oh-svc-billing-{ld,ldc,eq,fbx,udf} | `<SEED_VAULT_PREFIX>/svc-billing-*` |
| Product trust mirrors (OH18.4) | `SVC_TRUST_MIRROR` | oh-svc-trust-{ld,ldc,eq,fbx,udf} | `<SEED_VAULT_PREFIX>/svc-trust-*` |
| Feedback and CRM intake from product public sites | `SVC_INTAKE` | oh-svc-intake | `<SEED_VAULT_PREFIX>/svc-intake` |
| Payroll provider adapter (only if `OH_PAYROLL_ENGINE_MODE=provider`) | `SVC_PAYROLL_PROVIDER` | oh-svc-payroll-provider | `<SEED_VAULT_PREFIX>/svc-payroll-provider` (empty in non-prod; mock adapter) |

## Production refusal and first-login rules (binding)

1. `APP_ENV=prod|dr` with `SEED_PROFILE` set or `SEED_ENABLED=true` → boot exits 78 (`EX_CONFIG`) naming the variable; `pnpm seed*` refuses.
2. Any attempt to log in to production with a `*.test` address is refused at the IdP (realm policy) and raised as a security alert.
3. The production super admin (`rjnprajapati@gmail.com`) is created by the identity bootstrap, receives a one-time invitation link (24-hour validity), must set a new password (never one in this file) and enrol a passkey or TOTP before the first session; the Hub additionally requires a passkey for `PLT_SUPER_ADMIN` from go-live (IPB-02 OH note).
4. In `staging` and `demo`, first login forces a password change and MFA enrolment; the values in this file therefore work exactly once per reseed.
5. A credential from this file found in any log, trace, commit, pull request or chat is treated as compromised: rotate with `pnpm seed:credentials --rotate` and record the incident in OH13.

## Rotation log

| Date | Run id | Rotated by | Reason |
|---|---|---|---|
| 2026-10-26 | (lead issue; run id assigned on first `--import`) | Pack lead | Initial issue for OH v1.1 |
