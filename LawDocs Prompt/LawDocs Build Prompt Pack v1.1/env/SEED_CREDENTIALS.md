# SEED_CREDENTIALS — LawDocs (LD) — issued 26 October 2026 by the pack lead (LawDocs Build Prompt Pack v1.1; IPB-11 §11.4.6 shape; IPB-D-04 / D-21)

> **Handling.** This file is **gitignored** and blocked by the repository ruleset and push protection. Do not paste it into chats, tickets, wikis or screenshots. Store a copy only at the seed vault path `SEED_VAULT_PREFIX` (`secret://env/infrabyx/ld/<env>/seed`).
> **Valid for environments:** `local`, `dev`, `test`, `demo`, `staging`, `pre-prod` (synthetic data only — OP-7). **Production and DR never use this file:** the API refuses to boot with `SEED_ENABLED=true` or any `SEED_PROFILE` when `APP_ENV` is `prod` or `dr` (P23-AT-32); the super admin is created in production by invitation link, not by seed.
> **Passwords** below were supplied by the pack lead (24+ characters, CSPRNG, unique per persona and per product; IPB-11 §11.4.7). They are **not** to be regenerated, shortened or reused for another product. **On first login in `staging`, `pre-prod` and `prod`** the platform forces a password change and MFA enrolment (passkey or TOTP) before any other screen; in `local`/`dev`/`test` MFA may be deferred by `AUTH_MFA_REQUIRED_ROLES`.
> **Role mapping (IPB-DEV-02).** IPB-11 persona names are mapped to LawDocs' binding role codes (Appendix D); the lead-supplied persona set is kept as issued.

## Personas

| Persona | LawDocs role (Appendix D) | IPB-11 persona | Email | Password | Tenant / workspace | Environments |
|---|---|---|---|---|---|---|
| Super admin (owner) | `PLT_SUPER_ADMIN` | `super_admin` | rjnprajapati@gmail.com | `^qkiDA!WC8jrxc##i88PU30L=M` | platform (`apps/console`) | local, dev, test, demo, staging, pre-prod (prod: invitation link, not seeded) |
| Tenant admin | `ORG_OWNER` (also holds `ORG_ADMIN`) | `test.admin` | test.tenant_admin@lawdocs.test | `un8%OZ8pHD=Ek^xG1o*tayJ1NO` | demo Company workspace `ten_demo_acme` ("Acme Legal Pvt Ltd", `WS_COMPANY`) | local, dev, test, demo, staging, pre-prod |
| Maker | `ORG_LEGAL_MAKER` | `test.maker` | test.maker@lawdocs.test | `gkX4lO6hCma7ZH2UV_JY&lN8o4` | `ten_demo_acme` | as above |
| Checker | `ORG_CHECKER` (also `ORG_APPROVER`) | `test.checker` | test.checker@lawdocs.test | `^BOG%5l%lN0gULbatYswaMU2L1` | `ten_demo_acme` | as above |
| Individual | `IND_OWNER` | `test.member` (LD: Personal workspace owner) | test.individual@lawdocs.test | `hOSSLS5nTNAv*_5VQ^8Y%f#08s` | demo Personal workspace `ten_demo_individual` (`WS_PERSONAL`, family vault) | as above |
| Professional (advocate) | `PRO_ADVOCATE` (practitioner workspace, `apps/delivery`) | `test.advocate` | test.professional@lawdocs.test | `d-yGthAw!sXW&G47aLA4*!#eTF` | demo practice workspace `ten_demo_pro` (`WS_PRO_FIRM`); advocate profile with Rule 36 fields so reserved-advice behaviour (IPB-03) can be tested | as above |
| Counterparty | `CP_GUEST` | `test.party` | test.counterparty@lawdocs.test | `j$g4YLd*J=%9O%8fyYJzMg-xk*` | guest shell; signer on the three demo eSign envelopes | as above |
| Auditor (read-only) | `ORG_AUDITOR_RO` | `test.auditor` | test.auditor_ro@lawdocs.test | `kScMP6gWUi+yqIOJ$*mJB+xUGh` | `ten_demo_acme` (also granted a 30-day `vadg_` auditor grant for the Vendor Documents demo) | as above |
| Content editor | `PLT_CONTENT_EDITOR` (console Website Studio and Document Studio; `OPS_CONTENT_PUBLISHER` scope) | `plt_content` | test.content_editor@lawdocs.test | `!Dan8__7iijDOYAVq$J3aI92%8` | platform (`apps/console` Content Studio) | as above |

Personas not supplied by the lead (`PLT_SECURITY_OFFICER`, `PLT_RELEASE_MANAGER`, `PLT_LEGAL_REVIEWER`, `PLT_DPO`, `PLT_GRIEVANCE_OFFICER`, `OPS_RM`, `OPS_CONSUMER_CASE_MANAGER`, sandbox `ORG_OWNER`) are **not** seeded with passwords in this issue; `pnpm seed:credentials --append` generates them on first run (24+ characters, CSPRNG) and appends rows here with a rotation-log entry. They are never shared with the rows above.

## Demo narrative (seed profile `demo`; synthetic data only)

`ten_demo_acme`: 40 agreements across stages (12 executed, 8 in negotiation, 20 drafts), 12 legal notices, 3 eSign envelopes signed by `test.counterparty@lawdocs.test` through the mock signer (`LD_ESIGN_ADAPTER=self`), 6 matters with hearings, 4 trademarks, one BYO-storage target (MinIO), one Vidhi agent hired (`AGT_OBLIGATION_TRACKER`, L1, sponsor = tenant admin), one Monday-digest schedule (off), Settings › Security & trust seeded with three placeholder vendor documents (watermark demo). `ten_demo_individual`: family vault with 25 documents, one rent agreement drafted and signed, one trademark watched. `ten_demo_pro`: 3 marketplace engagements, 1 retainer. Public site: 15 flagship pages, 150 glossary terms, 6 resources (2 e-mail-gated), 10 blog posts (1 guest post in review). All names, PANs, phone numbers and addresses are synthetic and pass the `test` environment's real-identifier scan.

## Service accounts (no passwords; client credentials in the vault only)

| Identity | Role | Client ID | Vault path |
|---|---|---|---|
| Vidhi agent runtime | `AGT_*` (Keycloak client per hired agent, private-key JWT) | `ld-agt-<agent>` | `<SEED_VAULT_PREFIX>/agt-vidhi` |
| OH billing link (BILLING_PORT) | `SVC_BILLING` | `ld-svc-billing` | `<SEED_VAULT_PREFIX>/svc-billing` |
| OH CRM / support / backlog / trust link | `SVC_OPS_HUB` | `ld-svc-ops-hub` | `<SEED_VAULT_PREFIX>/svc-ops-hub` |
| Ecosystem bus (int module) | `SVC_ECOSYSTEM` | `ld-svc-eco` | `<SEED_VAULT_PREFIX>/svc-eco` |
| Migration job | `app_migrator` (DB role) | — | `<SEED_VAULT_PREFIX>/db-migrator` |

## Rules enforced by the seed framework (IPB-11 §11.3.C–E; P23 FR-P23-07)

1. `APP_ENV=prod|dr` + any `SEED_*` → boot fails (`P23-AT-32`).
2. Seeded accounts carry `must_change_password = true` and `mfa_enrolment_required = true`; the first sign-in in `staging`, `pre-prod` or `prod` completes both before any other route.
3. Seeded e-mail domain `@lawdocs.test` is blocked from receiving real mail (MailHog in local/dev; suppression list elsewhere).
4. Rotation: `pnpm seed:credentials --rotate <persona>` writes a new password, updates the vault and appends to the log; the old password is invalid immediately.
5. This file's SHA-256 is recorded in the seed run (`seed_run_id`) so a changed file is detected.

## Rotation log

| Date | Run id | Rotated by | Reason |
|---|---|---|---|
| 2026-10-26 | `seed-ld-v1.1-initial` | Pack lead (manual issue) | Initial issue with the v1.1 pack; passwords as supplied by the lead |
