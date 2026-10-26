# `env/` — environment template and seed credentials (LawDocs v1.1; IPB-11)

**What is here**

| File | Purpose | Commit? |
|---|---|---|
| `.env.example` | The annotated environment template for LawDocs (217 variables: the IPB-11 group set that LawDocs uses plus `LD_*` product ports). Every line states description, `req:` (which environments need it) and `sens:` (S secret · C config · P browser-exposed). | Yes — it is the reference; the repository regenerates it with `pnpm env:example` from `env.schema.ts` and CI fails if the two differ. |
| `SEED_CREDENTIALS.md` | Seed personas, their LawDocs roles and the passwords issued by the pack lead for non-production environments, plus service accounts and the rotation log. | **Never.** Gitignored and blocked by the repository ruleset and push protection. Keep it in the seed vault (`SEED_VAULT_PREFIX`). |
| `README.md` | This note. | Yes |

**How to use**

1. Copy `.env.example` to `.env.local` for a developer machine. Fill only the variables marked `req:all` or `req:nonprod`; leave adapters at their local defaults (`LD_ESIGN_ADAPTER=self`, `STORAGE_ADAPTER=s3` against MinIO, `SEARCH_ADAPTER=pg_fts`, `MSG_EMAIL_ADAPTER=smtp` → MailHog).
2. For `staging`, `pre-prod`, `prod` and `dr`, values are injected by the deployment (Helm values + the SECRETS port). Every `sens:S` variable must be a `secret://` reference; a literal secret fails boot. `SEED_*` must be absent in `prod` and `dr` — the API refuses to start otherwise (IPB-D-04; P23-AT-32).
3. Boot validation (`env.schema.ts`, IPB-11 §11.4.1) checks types, required-by-environment rules, residency constraints (`AI_BEDROCK_REGION=ap-south-1`, `AI_AZURE_OPENAI_REGION=centralindia`, `AI_VERTEX_REGION=asia-south1`, `IPB_DATA_RESIDENCY=IN`) and forbidden values (`PAYMENTS_HOSTED_CHECKOUT_ONLY` must be `true`; `DB_RLS_BYPASS_ROLE` must be empty in prod; `rzp_test_` keys refused in prod).
4. Run seeds only in non-production: `pnpm seed --profile dev|demo|test|load`. The `demo` profile builds the narrative described in `SEED_CREDENTIALS.md`. All data is synthetic (OP-7); the `test` environment scans for real-looking PAN, Aadhaar and phone numbers and fails the job if any appear.
5. First sign-in with a seeded account in `staging` or `pre-prod` forces a password change and MFA enrolment. Rotate with `pnpm seed:credentials --rotate <persona>`; append-only rotation log.
6. Node.js is **24.22.1** (IPB-D-01): `.nvmrc`, `package.json#engines`, the Dockerfiles and the CI matrix must agree; `pnpm env:check` verifies the pin along with the template.

**Never**: commit real values; paste `SEED_CREDENTIALS.md` into a chat, ticket or wiki; reuse a seed password in production; load production or customer data into any non-production environment; run seeds against a database whose `APP_ENV` is `prod` or `dr`.

**Related**: IPB-11 (`docs/ipb/IPB-11_Environment_and_Seed_Standard.md`), master prompt §5.1 and §21, P00 (seed framework), P23 FR-P23-07/08 (environments and secrets), `02` D-21.
