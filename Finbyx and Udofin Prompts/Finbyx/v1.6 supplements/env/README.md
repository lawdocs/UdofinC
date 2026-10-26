# Finbyx v1.6 — environment and seed files (IPB-11)

*(v1.6; 26 October 2026)* This folder holds the Finbyx-specific environment template and the seed credentials the lead supplied. It is the reference until Phase 1 generates the same files from `env.schema.ts`; the generated `.env.example` must match this one variable for variable (the `pin-check`/`env-check` CI job diffs them).

| File | Purpose | Commit to the repository? |
|---|---|---|
| `.env.example` | Annotated template, 163 variables (IPB-11 §11.4.3 template reduced to what Finbyx uses, plus the `FBX_*` adapter keys). Every line carries description, `req:` environments and `sens:` class. | **Yes** — at `/.env.example` (and `docs/supplements/v1.6/env/.env.example` for the record). Placeholders only. |
| `SEED_CREDENTIALS.md` | Seed personas with the exact credentials supplied by the lead; service-account vault paths; rotation log. | **Never.** Gitignored and blocked by the `secret-scan` ruleset and `.git/info/exclude`. Copy it to the developer's machine at `SEED_CREDENTIALS_PATH` (mode `0600`) and import it into the seed vault with `pnpm seed:credentials --import`. |
| `README.md` | This guide. | Yes. |

## How to use

1. **Local:** `cp .env.example .env`, keep the local defaults, run `pnpm env:validate` (boot validator from `env.schema.ts`: every `req:all` variable present, `sens:S` literals allowed only when `APP_ENV=local`), then `pnpm db:migrate`, `pnpm seed --profile dev`, `pnpm seed:credentials --import ./SEED_CREDENTIALS.md`. Sign in as `test.tenant_admin@finbyx.test`; the super admin is `rjnprajapati@gmail.com`.
2. **dev / test / preview:** CI writes `.env` from the `preview` secrets scope; adapters are `mock` (`FBX_*_ADAPTER=mock`), e-mail goes to a catch-all, SMS/WhatsApp/voice are suppressed, `SEED_PROFILE=demo` for previews (`FBX_SEED_LOAN_COUNT=20000`), `test` for CI (`pnpm seed:credentials --no-file`: passwords live only in the job's ephemeral vault).
3. **staging / demo:** every `sens:S` value is a `secret://` reference resolved through the `SECRETS` port (AWS Secrets Manager reference adapter); `DB_SSL_MODE=verify-full`; `CACHE_REDIS_TLS=true`; seeded personas get `temporary=true` so first login forces a password change and MFA.
4. **prod / dr:** `SEED_ENABLED` unset, `SEED_PROFILE` unset, `AUTH_BREAK_GLASS_ENABLED=false`, `DB_RLS_BYPASS_ROLE` empty, `AI_OBS_CAPTURE_CONTENT=false`, `PAYMENTS_HOSTED_CHECKOUT_ONLY=true`, no Supabase host anywhere, no `rzp_test_` key, no `.finbyx.test` identity. Boot refuses otherwise (`IPB-ENV-001`, `IPB-ENV-002`). The super admin is invited by link and completes MFA before any role is granted.

## Rules (never relax)

- Never commit real values. Never put a secret in a `NEXT_PUBLIC_*` or `EXPO_PUBLIC_*` variable (they ship to browsers and phones).
- Never echo, `cat` or paste a credential into a transcript, PR, commit message, log or test fixture; tests fetch credentials from the vault at runtime.
- Seeds are synthetic (`TEST` identifier prefixes; Verhoeff-invalid Aadhaar-like numbers never used; IPB-11-25) and never derived from a real borrower, bureau file or bank statement.
- Production refuses seeds, seed identities and this file's personas; the refusal is tested in CI (IPB-11 §11.8) and in the Phase 1 review gate.
- Finbyx tightening: `IPB_GLOBAL_ADAPTER_MAX_CLASS=PUBLIC` and `AI_REGULATED_BAND_LOCK=in_zero` are read-only in every environment above `local`.
- Rotation: seeded passwords every 90 days in `staging`/`demo` and on suspected exposure; DKIM selectors yearly; audit hash-chain key never rotated without a chain-anchor record (AC7).

## Variables that exist only for Finbyx

`FBX_CIC_*` (four CICs), `FBX_AA_*`, `FBX_ULI_ENABLED`, `FBX_DISBURSEMENT_*`, `FBX_ENACH_*`, `FBX_KYC_*` and `FBX_KYC_VCIP_*`, `FBX_CKYC_CREDS_REF`, `FBX_ESIGN_*`, `FBX_GL_EXPORT_FORMAT`, `FBX_CONNECTOR_AGENT_CA_REF`, `FBX_RETURN_PORTAL_MODE` (always `guided`: Finbyx prepares, a human files; no portal credential is ever an environment variable), `FBX_SEED_LOAN_COUNT`, `STORAGE_BUCKET_RETURNS`, `STORAGE_BYOS_ALLOWED_RESIDENCY`, `KMS_AADHAAR_VAULT_KEY_REF`, `KMS_FIELD_ENCRYPTION_KEY_REF`, `PAYMENTS_CATALOGUE_SIGNING_PUBKEY_REF`, `WORKFLOW_PAYLOAD_CODEC_KEY_REF`, `AI_REGULATED_BAND_LOCK`, `AI_MCP_RESOURCE_INDICATOR`, `IPB_GLOBAL_ADAPTER_MAX_CLASS`, `EXPO_PUBLIC_OFFLINE_SYNC_HOURS`.

Open item for the owner: the seed vault path and the preview database provider (Appendix B items 53 and 65).
