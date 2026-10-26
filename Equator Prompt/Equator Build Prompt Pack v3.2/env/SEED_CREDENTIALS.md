# SEED_CREDENTIALS — EQ (Equator Resolution) — issued 26 October 2026 by the pack lead (run id eq-seed-20261026-01)

> **Gitignored and blocked by the repository ruleset (IPB-11-10, IPB-11-36). Do not paste into chats, tickets or wikis.**
> Valid for environments: `local`, `dev`, `test`, `demo`, `staging`, `uat`. **Production never uses this file**: `pnpm seed` refuses when `APP_ENV` is `prod` or `dr` (IPB-11-14, IPB-11-22) and the boot guard exits 78 if `SEED_PROFILE` is set there.
> Passwords below were supplied by the lead and are the exact seed values (26 characters, CSPRNG, unique per persona — IPB-11-34). They are also stored at `secret://env/infrabyx/eq/<env>/seed/<persona>` and set on Keycloak realm `infrabyx-eq` by `pnpm seed:credentials`; the script prints only the file path and a count, never a password (IPB-11-35).
> **First-login rules (IPB-11-37, IPB-D-04):** in `staging`, `uat`, `demo` and `prod` every seeded human account has `must_change_password = true` and `mfa_required = true` on first login; the super admin always requires TOTP in every environment. In `local`, `dev` and `test` MFA is off for test personas to keep automated tests simple. In production the super admin is created by the identity bootstrap with an invitation link and forced password change plus MFA enrolment — never from this file.
> **Rotation (IPB-11-38):** automatically on every `demo`/`staging` reseed; on demand with `pnpm seed:credentials --rotate`; append a row to the rotation log.

## Human personas (tenant `tnt_platform` for the super admin; `tnt_demo` — "Demo Co", the Equator institution demo tenant — for the rest)

| Persona | Equator role (Appendix S §6) | IPB role class | Email | Password | Tenant | Environments |
|---|---|---|---|---|---|---|
| Super admin | `platform_admin` | PLT_SUPER_ADMIN | rjnprajapati@gmail.com | `DcZYc7@Ida5kqfgXFb-LclJI^r` | tnt_platform | local, dev, test, demo, staging, uat (prod: invitation link, not seeded) |
| Tenant admin (institution) | `institution_admin` | ORG_OWNER | test.tenant_admin@equator.test | `JG7Zbos&kHhn$lT^&#O-UsAPfE` | tnt_demo | local, dev, test, demo, staging, uat |
| Claimant (party) | `party` | ORG_MEMBER (external user) | test.claimant@equator.test | `HZbyfTY%w9qg9DGw@C$d=PcLkf` | tnt_demo | local, dev, test, demo, staging, uat |
| Respondent (party) | `party` | ORG_MEMBER (external user) | test.respondent@equator.test | `O-FN^LIfoFt3B#PKZ_*iKDqVAL` | tnt_demo | local, dev, test, demo, staging, uat |
| Neutral (mediator and arbitrator panels) | `neutral_mediator`, `neutral_arbitrator` | ORG_MEMBER (professional) | test.neutral@equator.test | `mZbvs*K4TSM=ldphJevM3$3xy_` | tnt_demo | local, dev, test, demo, staging, uat |
| Case manager | `case_manager` | ORG_MAKER | test.case_manager@equator.test | `eE#YJQ%Z#Z*v5kO6A0lH3G7=#W` | tnt_demo | local, dev, test, demo, staging, uat |
| Enterprise admin (lender tenant "Demo Lender") | `enterprise_admin` | ORG_ADMIN | test.enterprise_admin@equator.test | `=r5O=xe-Q59Y*@a4-MO%8oZtNR` | tnt_demo_enterprise | local, dev, test, demo, staging, uat |
| Auditor (read-only) | `auditor` | ORG_AUDITOR_RO | test.auditor_ro@equator.test | `$EFf7CJWt_%4GUvZzC&hWvBKxS` | tnt_demo | local, dev, test, demo, staging, uat |
| Content editor (CMS, help registry, platform notebooks) | `content_editor` | PLT_CONTENT_EDITOR | test.content_editor@equator.test | `34gFyh8T@XHE5RsJa-zPwM+Mt3` | tnt_platform | local, dev, test, demo, staging, uat |

Notes: the lead supplied nine personas for EQ; the IPB-11 template rows for platform security officer, release manager, legal reviewer, DPO, platform grievance officer, platform auditor, tenant maker/checker and sandbox owner are **not seeded** in v3.2 (no passwords were issued — do not invent them). Where a test needs those roles, grant them to the super admin or the tenant admin within the test fixture and record the grant in the test. The legal-reviewer and checker functions needed for maker-checker tests are exercised by `test.tenant_admin` (maker) and the super admin (checker), never by the same account (NN-36 CHECK).

## Seeded demo narrative (IPB-11 EQ note; `SEED_DEMO_NARRATIVE=three_cases`)

| Case | Vertical | State | Personas |
|---|---|---|---|
| `EQ/FIN/JAI/2027/00001` | FIN — loan settlement | Settled; settlement e-signed and e-stamped; escrow record `castler` fake | claimant, respondent (Demo Lender), neutral (conciliator), case manager |
| `EQ/COM/DEL/2027/00002` | COM — unpaid invoices | At hearing; arbitration, documents-only track; procedural order 1 issued | claimant, respondent, neutral (arbitrator), case manager |
| `EQ/INT/DEL/2027/00003` | INT — cross-border distribution | Registered; EU-resident party flagged for Annex III assessment (`fut.eu-ai-act-annex3`); Vidhi clerical-only | claimant (EU), respondent, neutral, case manager |

Scheme files at `EQ_SCHEME_CONFIG_PATH` include a SEBI-style scheme marked `DRAFT` (`fut.sebi-odr-v2`, OFF).

## Service accounts (no passwords; client credentials in the vault only — IPB-11-39)

| Identity | Role | Client ID | Vault path |
|---|---|---|---|
| Vidhi agent (P22) | AGT_VIDHI (`acting_as = 'vidhi'`) | eq-agt-vidhi | secret://env/infrabyx/eq/<env>/seed/agt-vidhi |
| OH billing link (OH8) | SVC_BILLING | eq-svc-billing | secret://env/infrabyx/eq/<env>/seed/svc-billing |
| OH trust mirror (OH14.6) | SVC_TRUST | eq-svc-trust | secret://env/infrabyx/eq/<env>/seed/svc-trust |
| Ecosystem bus publisher | SVC_BUS | eq-svc-bus | secret://env/infrabyx/eq/<env>/seed/svc-bus |
| Operations Platform staff client | (Keycloak client) | eq-portal-ops | secret://env/infrabyx/eq/<env>/seed/eq-portal-ops |

## Rotation log

| Date | Run id | Rotated by | Reason |
|---|---|---|---|
| 2026-10-26 | eq-seed-20261026-01 | pack lead | Initial issue for Equator Build Prompt Pack v3.2 |
