# Phase P23 — Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, CI/CD skeleton, AWS accounts, Terraform, audit ledger, Object Lock buckets, OpenTelemetry), P01 (staff realm `ld-staff`, MFA, break-glass), P03 (settings registry, feature flags, kill switches), P20 (export-map contract test, golden archives, move runbooks) and **every functional phase whose scope is being released**. External: GitHub organisation, Operations Hub **OH13** (engineering console and CAB record, `ChangeApproved`) and **OH14** (control library and provider-assurance room), CERT-In-empanelled auditor, certification bodies.
> **Sequencing:** The governance track (§4A–§4F) starts in sprint 1 of P00 in reduced form and is complete before P04 exits, so that every Wave 1 module is built under the final controls. The hardening, evidence and go-live track (§4G–§4M) runs before each wave's general availability. **P23 re-runs once per wave** (Wave 1 "Vault & Sign GA", Wave 2 "Legal Ops for companies", Wave 3 "Services and Consumer") for the scope released in that wave (§13.3).
> **Binding appendices:** P (security, privacy and certification readiness — control set, claims language, log retention), R (settings `eng.*`), D (staff roles and segregation of duties), K (export package — golden archives), W (open items and the `[VERIFY]` census — `ci/verify-census`), X (Operations Hub addendum: OH13/OH14 interfaces), Y (ecosystem events), Z (brief traceability matrix — `ci/trace-check`). Ecosystem Spec §6.29 (`ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`), §6.26 (`BackupCompleted`, `RestoreTested`) and §14 (versioning and certification) prevail on conflict.
> **Requirements covered:** R-057, R-033, R-034, R-031, R-021, R-022, R-067, R-017 (mobile release governance), R-001 (challenge on certification claims).
> **Decisions applied:** D-01, D-02, D-12, D-14 · **Challenges applied:** CH-19, CH-24 (no surveillance of engineers), CH-32 · **Non-negotiables tested:** NN-02, NN-12, NN-18, NN-20, NN-25, NN-27, NN-28, NN-30, NN-32, NN-33, NN-38, NN-39, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints for the first run (governance 2 with a platform squad of 4 in parallel with P02–P04; hardening and go-live 4 with a squad of 8: SRE ×2, security engineer ×2, QA lead, backend ×2, compliance analyst); each later wave re-run 2 sprints.

---

## 1. Objective and business outcome

The owner will push code to GitHub often — patches, features, framework upgrades, infrastructure moves — while individuals rely on LawDocs to keep their property papers and signed agreements for decades, and companies rely on it for evidence they will produce in court. P23 makes change safe and provable:

- every change is reviewed, tested, approved by someone other than its author, traceable to a release and reversible;
- customer data and folder structures survive every release and every infrastructure move (with P20);
- backups are proven by restoring them; disaster recovery is drilled;
- vulnerabilities are fixed within published deadlines;
- the platform is ready for an annual CERT-In-empanelled audit, IS and internal audits, client audits and certification (SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001, ISO 22301, PCI DSS SAQ A for hosted checkout) — **without claiming any certification before the certificate or report exists** (NN-20, R-033);
- each wave goes live through a signed checklist and a hypercare period.

| Outcome | Exit-gate measure |
|---|---|
| Every production change approved and traceable | 100% of production deployments in the trailing 30 days map to a change record with a matching `ChangeApproved` (OH13) and a signed image digest; zero deployments outside the pipeline |
| Releases never disturb customer data | `ci/migrations`, `ci/export-contract` and the golden-archive diff (P20) pass for every release; zero customer migration steps in release notes (NN-12) |
| Recoverability proven | Latest restore test of every T0 store passed within RTO; one full DR failover to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence filed |
| Security debt under control | No open Critical; no High past SLA; CERT-In-empanelled audit report issued after retest with Critical/High closed |
| Certification-ready | ≥ 80% of mapped controls with automated evidence; policy set approved by the Board of `[LawDocs Operating Entity]`; external readiness assessment with no Critical gaps; trust page makes no unevidenced claim |
| Safe go-live | Wave checklist signed by CTO, `PLT_SECURITY_OFFICER`, `PLT_DPO`, Company Secretary (owner) and product owner; hypercare exit criteria met |

---

## 2. Scope (in / out)

**In scope**

- GitHub organisation, repositories, branch model, rulesets, CODEOWNERS, signed commits and tags, PR template, merge queue, required checks.
- Environments: dev, test, staging, pre-prod, prod (+ DR region, backup and log-archive accounts); test-data policy; secrets; infrastructure as code.
- Change management (CAB-lite with OH13), change classes, risk scoring, maker-checker deployment approvals, change calendar and freeze windows, customer notice periods, release notes.
- Database migration governance and data preservation across releases and infrastructure moves (with P20).
- Release management: trains, rings, feature-flag rollouts (P03 registry), mobile store releases (with P22), content releases vs code releases.
- Patch and vulnerability management: intake, severity, SLAs, dependency hygiene and SBOM, OS and container patching, end-of-support register, exceptions.
- Backups (PITR, cross-region, immutable), restore drills, DR (RTO/RPO), business continuity.
- Security testing: SAST, SCA, secrets, IaC, container, DAST, API fuzzing, mobile testing, AI red-team suite; VAPT by a CERT-In-empanelled auditor; ASP/eSign and DigiLocker audits; responsible disclosure.
- Audit readiness: IS audit, internal audit, statutory/external audit support, client audits, evidence rooms, access reviews.
- SOC 2 / ISO evidence automation and certification programme; PCI DSS SAQ A scope control.
- Hardening, performance and resilience testing; incident management and regulatory clocks.
- Go-live checklist per wave and hypercare.

**Out of scope (owner)**

- Group-wide engineering console, CAB tooling and control library: Operations Hub OH13/OH14 (D-02). LawDocs emits events and evidence to them and consumes `ChangeApproved`; where OH13/OH14 are not yet live, the local `eng` records act as the system of record and back-fill OH when it arrives (Appendix X).
- Writing the policies themselves (information security, access control, acceptable use, etc.) — the owner prepares them (brief); P23 lists them, hosts them in LawDocs' own Company workspace (dog-fooding P04/P13) and records Board approvals.
- Tenant-facing security features for client companies (their own incident registers) — P13.

---

## 3. Personas and permissions touched

All staff roles live in the `ld-staff` realm, federated to the group Entra ID and provisioned from OH10 (joiner–mover–leaver). Engineering roles below are staff role codes used by `eng` and GitHub teams; they map to Appendix D.

| Role | Responsibility | SoD limits |
|---|---|---|
| CTO (`PLT_SUPER_ADMIN` holder for engineering, GitHub org owner) | Owns engineering governance; CAB chair; second approver for emergency changes | Cannot approve own change |
| `PLT_SECURITY_OFFICER` (CISO function) | Vulnerability SLAs, VAPT, risk acceptances, security incidents, key management; CAB member | Cannot deploy |
| `PLT_SRE` | Infrastructure, backups, DR, observability, on-call; executes deployments through the pipeline | No standing production data access; break-glass only |
| `PLT_RELEASE_MANAGER` | Trains, freeze windows, rings, release notes, customer notices; deployment approver 2 | Cannot approve a release containing own commits |
| Engineers (GitHub team `engineers`) | Code, tests, PRs | No production access; cannot merge own PR |
| Tech leads (team `tech-leads`) | Code owners; deployment approver 1 | — |
| QA lead | Test strategy, regression and accessibility suites, performance tests | — |
| `PLT_DPO` | Conditional CAB member for changes to personal-data processing, logging, retention, transfers, AI data use | — |
| `PLT_LEGAL_REVIEWER` | Conditional CAB member for `REGULATED` changes touching legal behaviour (eligibility gate, stamp, evidence, consumer clocks, marketplace rules) | — |
| Company Secretary (owner) | Go-live sign-off; policy approvals to the Board; certification programme sponsor | — |
| `PLT_AUDITOR_RO` | Read-only evidence room access (internal and external auditors, IS auditor, certification auditors) | No tenant data |
| AI lead | Model registry, prompt/skill code ownership, evaluation gates, red-team suite | — |
| `ORG_ADMIN` (client) | Receives release notes and notices; may enrol in early-access ring; may request a change freeze (Enterprise) | — |

Workforce measurement of engineers follows NN-33/CH-24: delivery metrics (DORA-style lead time, change failure rate, MTTR) at team level; no keystroke logging, screenshots or individual activity surveillance.

---

## 4. Functional requirements

### 4A. Source control and branching

**FR-P23-01 — GitHub organisation.** Repositories live in a GitHub organisation for `[LawDocs Operating Entity]` under the group's enterprise account. Use a plan that provides environment protection rules, required reviewers, rulesets, CodeQL, secret scanning and push protection on private repositories [VERIFY at P00: current GitHub Enterprise Cloud and security add-on names and INR pricing]. Until licensed, compensating controls apply: Actions build, sign and publish artefacts only; production deployment runs from a Temporal `ReleaseApprovalWorkflow` that assumes the deploy role only with two valid approvals and an OH13 `ChangeApproved`; open-source scanners (Semgrep CE, gitleaks, osv-scanner, Trivy) replace paid ones; the gap is risk `RISK-ENG-001` with a review date. The GitHub audit log streams to the India log-archive account (NN-27).

**FR-P23-02 — Repositories.** `lawdocs` (monorepo, P00), `lawdocs-infra` (Terraform, policy-as-code; apply rights for `PLT_SRE` only), `lawdocs-content` (recommended: reviewed rule sets, templates and help content as signed versioned artefacts, so content history is independent of code history — NN-30), `lawdocs-mobile-config` (store metadata, signing config references; no secrets), `lawdocs-legacy` (archived Vite/Express/MongoDB code after P00 migration, read-only), shared `infrabyx-contracts` and group kernels (`@infrabyx/governance-kernel`, `@infrabyx/hrms-kernel`, `@infrabyx/docgen`, `@infrabyx/redline`, `@infrabyx/archive-standard`, `infrabyx-labour-rulepack`) consumed as pinned versions, never forked (NN-47), `.github` (org templates, reusable workflows pinned by commit SHA).

**FR-P23-03 — Branch model (trunk-based).**

| Ref | Pattern | Rules |
|---|---|---|
| Trunk | `main` | Protected; always releasable; unfinished work hidden behind release flags (P03) |
| Feature | `feat/<LD-1234>-<slug>`, `fix/…`, `chore/…`, `docs/…`, `refactor/…`, `perf/…`, `test/…`, `ci/…` | Short-lived: nag at 2 working days, merge blocked at 5 without `long-lived-approved` label from a tech lead; squash merge |
| Dependency bots | `deps/<ecosystem>/<package>-<version>`, `dependabot/**` | As feature; 7-day cool-down for new non-security versions |
| Release | `release/YYYY.MM.N` | Created only by `PLT_RELEASE_MANAGER` from the release tag; exists to patch a deployed release |
| Hotfix | `hotfix/<release>-<LD-1234>-<slug>` | Fix lands on `main` first, then cherry-picked to `release/*` (never the reverse); tagged `vYYYY.MM.N+1` |
| Tags | `vYYYY.MM.N` (platform), `api-vX.Y.Z`, `mobile-vX.Y.Z`, `pkg-<name>@X.Y.Z`, `rulepack-<code>@<ver>` (content repo) | Signed annotated tags; creation restricted to release managers; immutable |

No long-lived `develop` branch: it adds merge debt without audit value. Auditability comes from signed tags, immutable image digests, change records and the audit ledger. This satisfies the owner's "push code from GitHub with branches" (R-057) while keeping integration continuous. Branch names: lower-case ASCII `[a-z0-9._/-]`, ≤ 80 characters (`branch-name` check).

**FR-P23-04 — Rulesets (organisation level).**

| Rule | `main` | `release/*` | Tags `v*` |
|---|---|---|---|
| Pull request required | ≥ 1 approval; ≥ 2 for CODEOWNERS "critical" paths | ≥ 2 | — |
| Code-owner review | Required | Required | — |
| Dismiss stale approvals on push; require approval of most recent push by someone else | Yes | Yes | — |
| Required checks (stable names) | `ci/lint`, `ci/typecheck`, `ci/test`, `ci/nn`, `ci/migrations`, `ci/rls-lint`, `ci/export-contract`, `ci/golden-archive-diff`, `ci/config-registry`, `ci/openapi-breaking`, `ci/asyncapi-breaking`, `ci/sast`, `ci/sca`, `ci/secrets`, `ci/iac`, `ci/container`, `ci/axe`, `ci/e2e-smoke`, `ci/pr-template`, `ci/sbom`, `ci/trace-check`, `ci/verify-census` | Same + `ci/e2e-full`, `ci/dast-baseline` | — |
| Merge queue | Yes | No | — |
| Linear history, squash only | Yes | Yes | — |
| Signed commits | Required (SSH/GPG or web-flow) | Required | Signed tags only |
| Force push, deletion | Blocked | Blocked | Blocked |
| Bypass | None, admins included; emergency path only via an OH13 `EMERGENCY` change with two approvers, logged | Same | Same |

**Traceability and verification checks (added at integration review).** `ci/trace-check` runs `pnpm trace:check` (Appendix Z §Z.8 rule 1): it fails when a `FR-Pxx-nn` cited in `docs/traceability/` (Appendix Z rows) no longer exists in `docs/phases/`, when an R-xxx in the requirements list has no row, or when a pull request adds, removes or renumbers an FR without updating the rows that cite it. `ci/verify-census` runs the P00 census script `tools/compliance/verify-census.ts` and `verify-lint` (Appendix W §W.1 step 7): it regenerates the `[VERIFY]` census and backlog from source, fails when a new `[VERIFY]` marker has no `V-*` item in `tools/compliance/verify-rules.json`, and warns on unassigned legacy markers; P00 builds the script and rules file, P23 makes the check required. Both run on pull requests to `main` and `release/*` and nightly.

A nightly job exports rulesets, branch protections, environment protections and org settings as JSON to the log archive; drift from the committed baseline opens a Sev-3 incident (`eng.github.drift_check`).

**FR-P23-05 — CODEOWNERS (critical paths need two approvals incl. a named owner).** `db/migrations/**`, `**/rls/**` (RLS policies), `packages/audit/**`, `packages/tenancy/**`, `packages/crypto/**`, `policies/cerbos/**`, `packages/export/**` and `**/export-map/**`, `packages/rules/**`, `apps/api/src/sgn/**` (eSign ASP integration, eligibility gate, evidence — `PLT_LEGAL_REVIEWER` delegate + security), `apps/api/src/cvl/**` (credential vault — security), `apps/api/src/bil/**` (billing UI and entitlements — finance owner), `apps/api/src/mkp/**` fee and directory code (legal reviewer), `apps/api/src/chp/**` (Consumer Help ethical wall — legal reviewer), `packages/ai/guardrails/**` and `packages/ai/skills/**` (AI lead + legal reviewer for legal-output skills), `packages/notify/telecom/**` (DLT/TCCCPR — legal reviewer), `infra/**` (SRE + security), `.github/**` (CTO + security).

**FR-P23-06 — Commits and PR template.** Conventional Commits (commitlint) with scope = module code (`feat(sgn): …`); trailers `Refs: LD-1234` on every commit and `Change-Record: CHG-YYYY-NNNNNN` on release and hotfix merges. The PR template (validated by `ci/pr-template`) has: summary; change type; risk (pre-fills the change-record score); rollout and rollback; **data migration** (expand/migrate/contract step, backfill, verification, reversibility); **export-map impact** (record types and columns added or changed; golden diff attached); **settings impact** (new keys registered in Appendix R; class and maker-checker); privacy impact (new personal data, processor, data class, transfer); NN impact (rules touched, tests added); accessibility impact (new screens; axe and manual check plan); legal impact (yes/no → `PLT_LEGAL_REVIEWER` required); testing evidence; customer-facing release-note text.

### 4B. Environments, test data and secrets

**FR-P23-07 — Environment catalogue.**

| Env | Purpose | Data (LOCKED: never production personal data outside prod) | Deploy | Protection |
|---|---|---|---|---|
| `local` | Developer machines | Seed `dev` | — | — |
| `dev` | Integration of `main`; preview environments per PR for web apps | Seed `demo`, reset weekly | Auto on merge | None |
| `test` | Automated suites: E2E, contract, accessibility, migration rehearsal on synthetic data, DAST baseline | Synthetic fixtures; PAN/Aadhaar/phone regex scan blocks real-looking identifiers | Auto after dev smoke | Team `qa` |
| `staging` | Production-like topology and configuration (Terraform module parity); release-candidate verification; performance smoke; sandbox vendor endpoints (ESP/eStamp/KYC sandboxes) | Synthetic at production shape (generated from production aggregate statistics only) | Tag `rc-*` | Tech leads |
| `pre-prod` | Final rehearsal: the exact image digests and migrations that will reach prod, against a production-sized synthetic dataset; UAT by product owner and legal reviewer; mobile store review builds point here | Curated synthetic | Promotion of the staging digest | Required reviewer: product owner |
| `prod` | Live, AWS ap-south-1 | Real | Promotion of the pre-prod digest | 2 required reviewers (tech lead + release manager), prevent self-review, branches `release/*` and tags `v*` only, custom protection rule `ld-change-gate` |
| `dr` | Warm standby, AWS ap-south-2 | Replicas | Terraform only; app deploys mirror prod | As prod |

Non-prod may use Supabase Postgres (database only) (D-01); prod and DR use RDS/Aurora PostgreSQL. **Migration timing on real volumes** [REC]: a pre-release job restores the latest prod snapshot into an isolated, no-human-access rehearsal VPC inside the prod account, runs the migrations, records duration and lock metrics, verifies the audit chain and destroys the copy; no data leaves the prod account.

**FR-P23-08 — Secrets and credentials.** AWS Secrets Manager only, with rotation; per-environment KMS keys; GitHub Actions authenticate to AWS through OIDC federation (no long-lived keys); vendor credentials (ESPs, eStamp, KYC, DigiLocker, Razorpay is in OH8 only, JioCX, Bedrock) per environment with sandbox credentials outside prod; no secrets in code, images, logs, front-end bundles or Expo config (`ci/secrets`, NN-32). Leaked secret → revoke and rotate within 24 hours.

**FR-P23-09 — Infrastructure as code.** Terraform with remote state (versioned, encrypted, locked), `terraform plan` attached to every infra PR, policy-as-code (Checkov/OPA) blocking public buckets, unencrypted stores, regions outside India for tenant data (NN-25), missing Object Lock on originals buckets (NN-09), missing log retention. Apply only from the pipeline with change approval.

### 4C. Change management (CAB-lite)

**FR-P23-10 — Change classes** (same names as Ecosystem Spec `ChangeApproved` classes):

| Class | Examples | Approval |
|---|---|---|
| `STANDARD` | Pre-approved catalogue: dependency patch with green CI; copy and UI fixes behind a flag; scaling within limits; base-image rebuild | Logged; auto-approved by the catalogue rule |
| `NORMAL` | Features, refactors, non-regulated schema changes, new non-regulated integrations | Low risk score: tech lead + release manager; otherwise CAB |
| `REGULATED` | Anything that changes: instrument eligibility gate logic, stamp computation or eStamp flows, eSign/ASP flows and consent screens, evidence packs and s.63 certificates, audit ledger or correction logic, retention or deletion, residency, encryption, authorisation policies, billing/GST presentation, export package format, consumer-help rules and ethical wall, marketplace professional rules, AI guardrails and labels, telecom compliance, accessibility-critical components | CAB + conditional reviewers (`PLT_LEGAL_REVIEWER`, `PLT_DPO`, finance) + golden suites (rule goldens, export goldens, eSign evidence goldens) |
| `EMERGENCY` | Sev-1 fix; actively exploited vulnerability; legal block (e.g., ESP licence lapse) | Two of CTO, `PLT_SECURITY_OFFICER`, on-call lead; retrospective CAB within 2 working days |

**FR-P23-11 — CAB-lite sized for a small team.** Standing members: CTO (chair), `PLT_SECURITY_OFFICER`, `PLT_RELEASE_MANAGER`, product owner of the affected module; conditional members join when their area is touched and their approval is then required (LOCKED): `PLT_DPO`, `PLT_LEGAL_REVIEWER`, finance controller. Quorum 3 including chair (or deputy) and security (quorum floor GOVERNED). Asynchronous approvals in the change record within 1 working day; weekly 30-minute sync for open high-risk changes, failed changes and post-implementation reviews. Minutes generated from the change record and filed as evidence. A change that `PLT_LEGAL_REVIEWER` or `PLT_DPO` rejects on NN grounds cannot proceed (LOCKED). The CAB record lives in OH13; LawDocs keeps `eng.change_records` linked by `change_id`.

**FR-P23-12 — Change record and risk score.** `eng.change_records`: ID `CHG-YYYY-NNNNNN` (`chg_` ULID), class, title, linked PRs and commits, risk score (deterministic pure function of impact, tenants affected, data migration, reversibility, regulated flag, ring blast radius; 100% branch coverage), expand-migrate-contract plan, rollback or forward-fix plan, test evidence links, tenant communication (text and date), window, approvers, outcome, post-implementation review. States: `DRAFT → SUBMITTED → ASSESSED → CAB_REVIEW → APPROVED | REJECTED | DEFERRED → SCHEDULED → IMPLEMENTED → PIR_DONE → CLOSED`; `FAILED → ROLLED_BACK | FORWARD_FIXED → PIR_DONE`.

**FR-P23-13 — Maker-checker deployment (NN-18).** The production deploy gate (`ld-change-gate` custom protection rule or `ReleaseApprovalWorkflow`) requires: (a) a `ChangeApproved` from OH13 matching `(change_id, approval_version)` — idempotent; (b) two human approvals in the prod environment (tech lead + release manager) neither of whom authored commits in the release; (c) signed image digests matching the pre-prod digests (cosign signature and SLSA provenance verified [REC]); (d) green required checks on the tag; (e) no active freeze window unless the change is `EMERGENCY` or holds a CAB exception. A deployment without all five is refused (`LD-ENG-010`) and alerts the CTO.

**FR-P23-14 — Change calendar and freeze windows.** `eng.change_calendar` shows scheduled changes, maintenance windows, freezes and content activations (P03 content calendar, independent). Default LawDocs freezes (OPEN for CAB to edit; dates set yearly): 28 March–5 April (FY-end renewals and 1 April State stamp-duty revisions — content may still publish); the 5 working days before the income-tax return due date once the `tax` module is live [VERIFY due dates under the Income-tax Act 2025]; Wave go-live weeks except hotfixes; client-requested freezes for Enterprise tenants (tenant stays on the previous ring where isolation permits). Standard deployment window: Tuesday and Thursday 22:00–24:00 IST.

**FR-P23-15 — Customer notice periods.**

| Change | Notice | Channel |
|---|---|---|
| Behaviour change affecting legal workflows (eligibility, formalities, signing flows), or regulatory-impact release | ≥ 5 working days | In-app "What's new", email to `ORG_ADMIN`, release notes |
| Planned maintenance with downtime | ≥ 72 hours | Status page, email, in-app banner |
| Breaking API or webhook change | Announcement + ≥ 12 months parallel support of a superseded public major (ecosystem majors ≥ 90 days); `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers — P19 FR-P19-06 governs | Developer portal, email to API owners |
| Export profile major (P20) | ≥ 30 days | In-app, email |
| New or changed sub-processor or data location | ≥ 30 days, with right to object per DPA | Trust page, email to admins |
| Emergency change | As soon as practicable; post-change notice within 24 hours | Status page, email |

**FR-P23-16 — Release notes.** Generated from Conventional Commits and the PR template's customer text; internal notes (all changes) and customer notes (visible changes only, plain language, no internal identifiers); published in the help centre "What's new" (P21) and the in-app feed; each release emits `in.infrabyx.ops.ReleasePublished.v1` via `int` (version, change IDs, SBOM hash, signature digest, release-notes reference, regulatory-impact flag — Spec §6.29).

### 4D. Database migration governance and data preservation (NN-12; with P20)

**FR-P23-17 — Expand → migrate → contract.** Every schema change is split: **expand** (add nullable columns or new tables; indexes `CONCURRENTLY`; dual-write in code), **migrate** (backfill in batches as a Temporal job with progress, throttling, checkpoints and a verification query), **contract** (remove old columns or paths) in a later release after verification and at least one full release cycle. `ci/migrations` rejects in the same release as the code that stops using them: `DROP`, `RENAME`, type narrowing, `NOT NULL` without default on large tables, non-concurrent index creation on large tables, and any migration touching a column referenced by `xpt.export_map`. Migration scripts set `lock_timeout` and `statement_timeout`. Migrations are forward-only; rollback is a forward fix or flag-off of the new path while the expanded schema stays. (P20 FR-P20-38 refers to this rule.)

**FR-P23-18 — Data preservation guarantees.** (a) Prefixed ULIDs and business references never change; (b) object keys are content-addressed under the tenant prefix, never derived from display names (P20 FR-P20-18); (c) the customer folder taxonomy is generated from the versioned export map, so downloaded and mirrored structures stay the same when code, database engine, storage vendor or region changes; (d) a taxonomy change is a `REGULATED` change with a profile major, compatibility map and notice; (e) golden-archive diff on every release candidate; (f) mirror sync is idempotent and path-stable.

**FR-P23-19 — Infrastructure moves.** Database engine/provider, instance class, region and storage-vendor moves follow the P20 FR-P20-42 runbooks as `REGULATED` changes, each producing a migration evidence pack (row counts and checksums per table, audit-chain verification end to end, golden-archive diff, approvals) filed as control evidence. The audit chain continues unbroken across the move (NN-02).

**FR-P23-20 — Content releases are not code releases (NN-30).** Publishing rule sets, templates, clauses and help content is a governed content workflow (P03) that can happen any day, including freeze windows. A code release must not change published content: the release rehearsal hashes content tables and rule-set versions before and after migrations (`NN-30_release_does_not_touch_content`).

### 4E. Release management and feature-flag rollouts

**FR-P23-21 — Versioning and trains.** Calendar versioning `YYYY.MM.N` for the platform; SemVer for packages, contracts, SDKs and the public API (`api-vX.Y.Z`); weekly train plus a hotfix lane. Release record links change records, SBOM, signatures and notes.

**FR-P23-22 — Rings through flags.** One code version serves all tenants; rings are flag segments (P03 FR-P03-87): `ring0` internal (LawDocs' own Company workspace and staff Personal workspaces), `ring1` opt-in early access and sandbox tenants, `ring2` general. Promotion after 24 h without SLO burn alarms. Schema changes always ship expand-first so all rings run on the same schema. Percentage rollouts hash on `tenant_id` (sticky). Every release flag has an owner and expiry (P03 stale-flag check).

**FR-P23-23 — Mobile releases (with P22).** EAS builds signed with store keys held in the build service's secure storage; internal testing tracks → TestFlight/closed testing → staged rollout (Android percentage rollout; iOS phased release) [VERIFY current store mechanics]; minimum supported version enforced by the BFF (`mob.version.min_supported`, P22 FR-P22-07) for security fixes; over-the-air JavaScript updates only for bug fixes within store policy and never to change permissions, payment flows or primary purpose [VERIFY store policies]; every store submission is a change record.

**FR-P23-24 — Customer sandbox and early access.** Tenants may create a sandbox (P03) that receives `ring1` features early; Enterprise tenants may pin `ring2` for up to 30 days around an audit or inspection.

### 4F. Patch and vulnerability management

**FR-P23-25 — Intake.** Dependabot/Renovate alerts, CodeQL or Semgrep, secret scanning with push protection (or gitleaks), osv-scanner, Trivy (images, IaC), Checkov, AWS Security Hub (CIS AWS Foundations), GuardDuty, Inspector, DAST (OWASP ZAP baseline on every staging deployment; authenticated full scan weekly), API fuzzing from OpenAPI (Schemathesis) nightly, mobile static and dynamic analysis (OWASP MASVS-aligned), CERT-In and vendor advisories, VAPT findings, `security.txt` (RFC 9116) reports. Normalised into `eng.vulnerabilities` (one record per CVE/rule × component × version × environment), mirrored to OH13.

**FR-P23-26 — Severity.** CVSS v4.0 where available, else v3.1, adjusted: CISA KEV-listed or public exploit **and** internet-exposed → Critical; EPSS ≥ 0.5 → raise one level; affects authentication, eSign, credential vault, audit ledger, billing or tenant isolation → environmental requirement High. VAPT findings keep the auditor's rating unless re-rated with auditor concurrence at retest.

**FR-P23-27 — Remediation SLAs** (from triage, as in Appendix P and Ecosystem Spec §13.3; triage within 24 hours for Critical and 3 working days otherwise; defaults GOVERNED, outer limits LOCKED; a stricter client contract wins for reporting).

| Severity | Default SLA | Locked outer limit | Route |
|---|---|---|---|
| Critical (KEV, exploited or internet-exposed) | 72 hours | 72 hours | `EMERGENCY` |
| Critical (other) | 72 hours | 7 days | `EMERGENCY` |
| High | 7 days | 15 days | `NORMAL` (or `EMERGENCY` if exploited) |
| Medium | 30 days | 45 days | `NORMAL`/`STANDARD` |
| Low | Next release, ≤ 90 days | 90 days | `STANDARD` |
| Leaked secret | Revoke and rotate in 24 hours | 24 hours | `EMERGENCY` |

Alerts at 50% and 80% of the SLA; breach pages `PLT_SECURITY_OFFICER` and marks the control failing. Closure needs fix, regression test, verification scan and a check across supported release branches. Exceptions need a risk acceptance by `PLT_SECURITY_OFFICER` with compensating control and expiry ≤ 90 days (`eng.risk_acceptances`); Critical acceptances are reported to the CTO and the owner.

**FR-P23-28 — Dependencies and SBOM.** CycloneDX (or SPDX) SBOM per image and per mobile build (`ci/sbom`), stored with the release; Renovate with grouping and a 7-day cool-down for new non-security releases; licence policy check (deny copyleft licences incompatible with distribution of the mobile apps and the open-source verifier) [REC]; pinned GitHub Actions by SHA; npm provenance verification where available.

**FR-P23-29 — OS, container and platform patching.**

| Layer | Cadence |
|---|---|
| Container base images (distroless Node 24 [VERIFY LTS status]) | Rebuild weekly even without code change; redeploy as `STANDARD` |
| Node.js security releases | Within severity SLA; LTS minors monthly |
| PostgreSQL (RDS/Aurora) minor versions | Within 30 days of availability in ap-south-1, in the Sunday 01:00–04:00 IST window after ≥ 7 days in staging |
| Keycloak, Temporal, OpenSearch, Redis, Gotenberg/LibreOffice, Cerbos | Minor within 30 days; security per SLA |
| Expo SDK and native modules | Each mobile train; security via hotfix train + `mob.version.min_supported` |
| Staff endpoints (via OH12 device management) | OS and browser ≤ 14 days; Critical ≤ 72 h |
| SaaS (GitHub, M365, vendors) | Vendor-managed; admin security settings reviewed quarterly |

**FR-P23-30 — End-of-support register.** `eng.eos_register` lists languages, frameworks, databases, OS images, mobile SDKs and SaaS dependencies with end-of-support dates and upgrade plans started ≥ 6 months before EOL; an item within 6 months without a plan raises a CAB item.

### 4G. Backups, restore drills and disaster recovery

**FR-P23-31 — Recovery tiers (`eng.service_catalogue`).**

| Tier | Systems | RPO | RTO | Mechanism |
|---|---|---|---|---|
| T0 | PostgreSQL core (all tenant schemas), Temporal DB, Keycloak DB; S3 originals, signed files and evidence (Object Lock); audit anchors | ≤ 15 min | ≤ 4 h (target 2 h) | Multi-AZ; cross-region replica or Aurora Global Database to ap-south-2; PITR 35 days; S3 cross-region replication with Object Lock replication; snapshots against logical corruption |
| T1 | Configuration stores (flags, Cerbos policies, Keycloak realm export), export packages in flight, OpenSearch index metadata | ≤ 1 h | ≤ 8 h | Snapshots, nightly config exports, rebuild |
| T2 | OpenSearch indices, pgvector embeddings (rebuildable), Redis, analytics marts | ≤ 24 h | ≤ 24 h | Rebuild from PostgreSQL and object storage |
| T3 | Source code mirror, CI history, staff M365 workspace (OH12) | Daily mirror / vendor-defined | — | Nightly repository mirror to the backup account with Object Lock (400 days) |

Tier assignments are GOVERNED (CAB); T0 targets cannot be loosened (LOCKED). During any Supabase-hosted beta, RPO for region loss is 24 h and is disclosed to beta users.

**FR-P23-32 — Backup policy.** PITR 35 days; daily snapshots 35 days; monthly 13 months; FY-end snapshots 8 years [REC; aligns with tax-record retention, OI-P20-07]; backups in a separate backup account with AWS Backup Vault Lock (compliance mode after grace) and separate credentials; backup-specific KMS keys whose policies deny scheduled deletion except to break-glass; SCPs deny deletion of vaults, recovery points and the backup and log-archive accounts. Customer-held copies via P20 are **in addition** to LawDocs backups, never a substitute.

**FR-P23-33 — Restore drills (`eng.restore_tests`; a missed test counts as failed).**

| Test | Frequency (floor LOCKED) | Pass criteria |
|---|---|---|
| Automated database restore (random point within 7 days) | Weekly (floor monthly) | Completes within the tier RTO; row counts within expected window; `audit.verify_chain()` green; sampled checksums |
| PITR to a timestamp | Monthly | Data at T matches the audit-chain head at T |
| Cross-region snapshot restore in ap-south-2 | Monthly | As above |
| Air-gapped vault restore | Quarterly | Restore via resource share into a clean recovery account |
| S3 originals/evidence sample | Monthly (≥ 50 objects or 0.1%) | SHA-256 equals the vault hash |
| Log-archive oldest-object probe | Monthly | Objects ≥ 179 days and ≥ 364 days retrievable (NN-27; DPDP r.6/r.8(3)) |
| Source-mirror rebuild | Quarterly | Latest tag builds reproducibly; digest matches or difference explained |
| Search rebuild | Quarterly | Full reindex within T2 RTO |
| BYO-target restore test (P20) | Per tenant schedule | Verifier green on customer copy |

Each result records restore seconds vs budget, RPO achieved, checks and an evidence hash; a failure opens a Sev-3 incident (two consecutive → Sev-2) and schedules a retest within 24 hours of the fix. A weekly Restore Assurance Report (PDF/A + XLSX) goes to SRE, security, CTO and auditors and is published as `in.infrabyx.portability.RestoreTested.v1` (type `DR_DRILL` or `INTEGRITY`) and `BackupCompleted` (type `PLATFORM`) through `int` (Spec §6.26).

**FR-P23-34 — DR drills.** Semi-annual regional failover game day to ap-south-2 with measured RPO/RTO, status-page updates rehearsed and failback; annual tabletop exercises for ransomware, malicious insider (rogue super admin — tests NN-02 and Correction Entry controls), cloud account compromise, key loss, ESP outage during signing peaks, and AI provider outage (Vidhi fallbacks). Ransomware runbook restores into a fresh recovery account built from the source mirror and Terraform, never into the compromised account.

**FR-P23-35 — Business continuity.** BCP covers: loss of AWS region; loss of primary ESP (route to second ESP — D-12); loss of eStamp channel in a State (manual stamp-paper route); loss of AI provider (template automation continues; AI features show "temporarily unavailable"); loss of OH8 billing (entitlements cached 30 days; exports never blocked); loss of key staff (runbooks, access via break-glass with dual approval).

### 4H. Security testing, VAPT and specialised audits

**FR-P23-36 — Continuous testing.** SAST, SCA, secrets, IaC and container scans on every PR; DAST baseline on every staging deployment; authenticated DAST weekly; API fuzzing nightly; IDOR/BOLA tests per endpoint (NN-01); mobile MASVS checks per build (certificate pinning, root/jailbreak detection, no sensitive logs or screenshots of protected screens — NN-44); AI red-team suite (prompt injection from uploaded documents and emails, cross-tenant exfiltration, tool misuse, fabricated citations, attempts to bypass the AI label — NN-14) on every change to `packages/ai/**`.

**FR-P23-37 — VAPT and comprehensive audit by a CERT-In-empanelled auditor.** (a) Annual comprehensive cyber-security audit by a CERT-In-empanelled auditor aligned with CERT-In's Comprehensive Cyber Security Audit Policy Guidelines (25 July 2025) [VERIFY applicability and requirements — R3 LG-080]; (b) quarterly external-surface VAPT and authenticated web/API testing; (c) pre-release VAPT for any release that materially changes authentication, authorisation, eSign/eStamp flows, payments, the credential vault, public APIs, mobile apps or the AI gateway — the release stays in `ring1` until Critical/High are closed. Scope: public site, `apps/web`, `apps/delivery`, `apps/console`, `apps/mobile` (iOS and Android), public and partner APIs, webhooks, cloud configuration, GitHub configuration, the staff M365 tenant (with OH12), AI gateway. Testing only on LawDocs test tenants in an agreed non-destructive window; rules of engagement, NDA and DPA filed; an auditor-empanelment snapshot hash stored with the engagement; findings imported into `eng.vulnerabilities`; auditee data held by the auditor only on systems in India.

**FR-P23-38 — eSign ASP and DigiLocker audits.** Budget and schedule the ASP audit required by each ESP contract and CCA guidance (R3 LG-009) [VERIFY frequency in each ESP contract]; maintain eSign logs and consent records for audit (NN-06); for DigiLocker requester onboarding, the annual CERT-In-empanelled audit and 24-hour breach reporting to NeGD required by the requester terms (master §5.5 and §7 DigiLocker row; NN-42; R3 §3) are tracked as obligations in the compliance calendar of LawDocs' own workspace.

**FR-P23-39 — Responsible disclosure.** `security.txt` on every domain; vulnerability disclosure policy with safe harbour; acknowledgement within 3 working days; private bug bounty behind `eng.flag.bug_bounty` = OFF until budget approval.

### 4I. Audit readiness and evidence rooms

**FR-P23-40 — Evidence collectors (`eng.control_evidence`).** Scheduled collectors produce dated, hashed evidence per control: ruleset and environment-protection exports; PR approval samples; change records with approvals; deployment logs with image digests and signatures; access reviews; MFA coverage; joiner–mover–leaver reconciliation (OH10 ↔ Keycloak ↔ GitHub ↔ AWS); break-glass reports; vulnerability SLA report; SBOM inventory; backup and restore results; DR drill reports; encryption and KMS rotation status; log-retention probe; audit-chain verification; Object Lock configuration; kill-switch drills (P03); accessibility audit results (NN-28); training completion (from the group LMS); vendor reviews; incident and risk registers; policy approvals. Each item carries period, collector version, artefact hash and control mapping, and is published as `in.infrabyx.ops.ControlEvidenceCollected.v1` to OH14 (Spec §6.29).

**FR-P23-41 — Audits supported.** (a) **IS audit** of LawDocs' information systems; (b) **internal audit** of LawDocs operations (risk-based plan, findings tracked to closure in LawDocs' own workspace); (c) **statutory and tax audits** of `[LawDocs Operating Entity]` (books in the group accounting system; billing data from OH8; `bil` mirror exportable with s.63 certificate); (d) **certification audits** (SOC 2, ISO); (e) **client audits** — Enterprise and regulated-entity clients may audit LawDocs as their technology provider [INTERP: RBI outsourcing expectations for regulated entities include audit rights; VERIFY current RBI directions and paragraphs]. Auditors use the OH14 **provider-assurance room** (no tenant data) under a `PROVIDER_ASSURANCE` grant (Spec §4.7) and a read-only `PLT_AUDITOR_RO` view of platform-level records (configuration history, audit-chain verification, change records).

**FR-P23-42 — Evidence packs.** One-click packs per audit type (`eng.evidence_packs`): folder structure in archive-standard style, PDF/A + XLSX, hashed, watermarked for the recipient, expiring access; standard questionnaires (SIG Lite/CAIQ-style responses), sub-processor list, architecture and data-flow diagrams, latest VAPT summary, BCP/DR evidence, policy index, and — once issued — SOC 2 reports and ISO certificates.

**FR-P23-43 — Access reviews.** Quarterly staff access review (console, delivery, AWS, GitHub, database break-glass, KMS administrators, vendor consoles) with manager attestations; unattested access auto-revoked after 10 working days [REC]; tenant-facing quarterly access review workflow offered to every company tenant (department heads attest users and delivery grants); results exported as evidence.

### 4J. SOC 2 / ISO evidence automation and certification readiness (NN-20, CH-19)

**FR-P23-44 — Programme** [REC sequence]: (1) readiness assessment against SOC 2 Trust Services Criteria (Security mandatory; Availability and Confidentiality recommended; Processing Integrity for eSign evidence and billing presentation; Privacy optional) and ISO/IEC 27001:2022; (2) SOC 2 Type 1 at about Wave 1 GA + 2 months; (3) ISO/IEC 27001:2022 Stage 1 and 2; (4) SOC 2 Type 2 with a 6-month first window, then 12-month windows; (5) ISO/IEC 27701 (privacy information management) [VERIFY current edition and certification transition rules]; (6) ISO/IEC 42001:2023 (AI management system) once Vidhi features are material to sales; (7) ISO 22301:2019 for Enterprise clients; (8) **PCI DSS v4.0.1 SAQ A** for hosted/tokenised checkout via Razorpay through OH8 — LawDocs never stores, processes or transmits card data (NN-22); SAQ A eligibility includes confirming the site is protected from script attacks that could affect the payment page [VERIFY with the acquirer and a QSA]; the correct claim is "PCI DSS SAQ A self-assessment completed", never "PCI DSS certified" (CH-19); (9) annual CERT-In-empanelled audit (FR-P23-37).

**FR-P23-45 — Control set and mapping.** One control library (from OH14) maps LawDocs controls to SOC 2 criteria (CC1–CC9, A1, C1, PI1, P-series), ISO 27001:2022 Annex A, ISO 27701, ISO 42001 Annex A, ISO 22301 clauses, PCI DSS SAQ A, CERT-In Directions, DPDP Act and Rules, IT Rules 2021, and the eSign/DigiLocker obligations. P23 implements technical controls and evidence; the owner writes policies; LawDocs' own Company workspace hosts them with versioning and Board approval records; the ISMS risk register and Statement of Applicability live there too (dog-fooding).

**FR-P23-46 — Claims register and trust page (NN-20).** `eng.claims_register` lists every public security or compliance statement with its evidence link and expiry; the public trust page (P21) renders only registered claims: data location (India), encryption, sub-processors, security practices, status page, responsible disclosure, and reports/certificates only once issued. Before then: "We are preparing for SOC 2 and ISO/IEC 27001 audits." A CI content check rejects "certified", "compliant", "bank-grade", "government-approved" or similar on public pages unless the claim ID is present (shared with P21).

### 4K. Hardening and performance

**FR-P23-47 — Hardening checklist** (each item has a test or evidence collector):

- Identity: MFA for 100% of staff; phishing-resistant MFA (passkeys/FIDO2) for privileged staff; no shared accounts; service accounts short-lived; Keycloak admin only from staff network and compliant devices; customer authentication per NN-03 (Aadhaar never a login).
- Web: TLS 1.2+ (1.3 preferred), HSTS preload, CSP with nonces (no `unsafe-inline` scripts), `frame-ancestors`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, SRI for any third-party script, script inventory and change detection on all pages (supports SAQ A eligibility), cookies `__Host-`, Secure, HttpOnly, SameSite; no tracking pixels on vault, drafting or consumer-case pages (R3 LG-086).
- API: authorisation on every route (Semgrep rule), schema validation, rate limits per tenant/user/IP, size limits, idempotency keys (NN-46), RFC 9457 problem details without stack traces, CORS allow-list.
- Uploads: magic-byte validation, AV scan, macro neutralisation, sandboxed rendering, zip-bomb and path-traversal protection, prompt-injection labelling for AI.
- Cloud: SCPs, least privilege, IAM Access Analyzer clean, no public buckets, VPC endpoints, egress allow-list (AI calls only to approved endpoints — NN-15), WAF managed rules and bot control, GuardDuty and Security Hub without Critical/High, KMS separation of key administrators and users, organisation CloudTrail immutable.
- Database: RLS lint green (NN-01), no superuser application roles, TLS connections, DDL audit, connection limits.
- Email and DNS: SPF, DKIM, DMARC `p=reject` after monitoring, MTA-STS, TLS-RPT, DNSSEC, CAA.
- Logging: OpenTelemetry with PII scrubbing (NN-32); 180-day minimum log retention in India (default 400 days) and NTP synchronisation to NIC/NPL sources (CERT-In Directions 28 Apr 2022; R3 LG-079; NN-27).
- Mobile: certificate pinning, encrypted offline cache with device-bound keys, biometric unlock local only, screenshot blocking on protected screens, no sensitive logs (NN-44).

**FR-P23-48 — Performance and resilience tests (k6 or Gatling).** (a) Load: 5,000 concurrent users across 2,000 tenants with p95 within P00 budgets; (b) peak: 1,000 signing ceremonies per hour and FY-end renewal spikes; (c) bulk: 10,000-file folder import ≤ 30 minutes; 50 GB export resumable (P20); (d) soak: 24 hours at 60% peak without memory growth; (e) chaos: loss of an AZ, Redis, OpenSearch (fallback to PostgreSQL FTS), primary ESP (failover), AI provider (deterministic fallbacks), a court-data aggregator (staleness labels). Capacity and cost model reviewed monthly; per-tenant cost dashboards (FinOps) include AI token cost against plan credits.

**FR-P23-49 — Accessibility release gate (NN-28).** Every release runs axe on all changed screens (`ci/axe`); each wave release adds a manual audit (NVDA, JAWS, VoiceOver, TalkBack, keyboard-only, 400% zoom, captions and transcripts for new videos) against WCAG 2.2 AA and IS 17802 (Parts 1–2); blocking issues stop promotion to `ring2`.

### 4L. Incident management and regulatory clocks

**FR-P23-50 — Incident process.** Severities Sev-1 (outage, data breach, integrity compromise, evidence-chain break) to Sev-4; incident commander; status-page update within 30 minutes for Sev-1/2; customer communication templates; post-incident review within 5 working days with tracked actions; integrated with the OH13 incident register.

**FR-P23-51 — Regulatory and contractual clocks** (clocks start at detection, have named owners and escalate automatically; implemented with P03 `LEGAL` clocks):

| Clock | Duty | Source |
|---|---|---|
| CERT-In | Report specified cyber incidents within 6 hours of noticing | CERT-In Directions under IT Act s.70B(6), 28 Apr 2022 (R3 LG-079); NN-27 |
| DPDP Board and affected users | Where LawDocs is fiduciary (individual users, leads, visitors): intimate the Data Protection Board and affected principals without delay; detailed report within 72 hours | DPDP Rules 2025 r.7 (R3 LG-065) [VERIFY commencement 13 May 2027 — build now] |
| Company tenants (LawDocs as processor) | Notify the tenant without delay, target ≤ 2 hours of detection, with a structured notice so the tenant can meet its own duties | DPA; Ecosystem Spec §3.8 pattern; R3 LG-072 |
| NeGD (DigiLocker) | Report breaches affecting DigiLocker-integrated flows within 24 hours | DigiLocker requester terms (R3 §3) [VERIFY current terms] |
| ESPs / CCA | Notify ESP partners per contract for incidents affecting eSign flows | ESP contracts [VERIFY] |
| IT Rules grievance and takedown | 3-hour takedown on court/government orders with 24×7 on-call | IT Rules 2021 as amended 2026, r.3(1)(d) (R3 LG-077) [VERIFY] |

### 4M. Go-live checklist per wave and hypercare

**FR-P23-52 — Go-live checklist (`eng.golive_checklists`).** Generated per wave from a template; every item has an owner, evidence link and status; go/no-go requires all **blocking** items done.

| Area | Blocking items (all waves unless stated) |
|---|---|
| Legal and contracts | Terms, privacy policy and other policies published (R-072); grievance officer, DPO and nodal officer details in Super Admin → Legal entities (D-08); DPA and sub-processor list; ASP arrangement and two ESP routes (Wave 1; D-12, NN-06); eStamp channel agreements and State coverage registry (Wave 1; NN-08); DigiLocker requester onboarding (Wave 1, if used); DLT entity, headers and templates registered (NN-34); marketplace counsel opinion for professional rules (Wave 2; NN-21); Consumer Help entity, brand, ethical wall and counsel opinion on success-fee switch (Wave 3; NN-23, CH-31) |
| Verification | `docs/compliance/verification-log.md` reviewed; every flag depending on an open `[VERIFY]` is OFF or advisory (NN-38) |
| Security | VAPT closed for Critical/High; CERT-In audit plan booked; secrets rotated; break-glass tested; kill switches drilled (NN-39) |
| Data | Export-map coverage 100% for wave scope; golden archives green; restore and DR tests within targets; residency attestation |
| Accessibility | Manual audit passed for wave screens; accessibility statement published (NN-28) |
| Product quality | Acceptance suites for wave phases green; NN test suite green; performance targets met |
| Operations | On-call rota; runbooks; status page; support flows through OH6 (D-02); CSM and onboarding playbooks (OH4) |
| Billing | OH8 catalogue live for wave SKUs; GST invoices; Razorpay hosted checkout tested; cancellation as easy as sign-up (NN-50) |
| Mobile (Wave 2) | Store approvals; privacy labels/data-safety forms consistent with the privacy policy [VERIFY store requirements]; minimum version gate |
| Content | Top pages and help articles for wave features published (P21); "i" keys registered |
| Sign-offs | CTO, `PLT_SECURITY_OFFICER`, `PLT_DPO`, Company Secretary (owner), product owner, `PLT_LEGAL_REVIEWER` |

**FR-P23-53 — Cut-over.** `READINESS_REVIEW → GO_NO_GO (signatures) → CUTOVER (runbook: feature flags to `ring2` in steps; Wave 1 only — DNS, the legacy 301 map and the legacy MongoDB migration with reconciliation per P00 §5.5) → HYPERCARE → STEADY_STATE`; no-go returns to readiness with the blocking list.

**FR-P23-54 — Hypercare.** 14 days for Waves 1 and 2; 21 days for Wave 3 (consumer volumes): daily triage at 10:00 IST; freeze on non-critical changes (hotfix lane only); enhanced monitoring of signing success rate, eStamp failures, export success, error budgets, support tickets by category; exit criteria — no open Sev-1/2, error budgets healthy for 7 consecutive days, support backlog within SLA, top-10 user issues triaged, PIR of any incident done.

**FR-P23-55 — Post-go-live cadence.** Monthly engineering and security report to the owner (SLA attainment, incidents, restore tests, vulnerability ageing, DORA metrics at team level, cost); quarterly review of risk register and control evidence freshness; annual policy review and certification surveillance.

### 4N. AI change management

**FR-P23-56 — AI changes are changes.** Model, provider, region, prompt, skill, tool-schema, retrieval-index and guardrail changes follow FR-P23-10 with sub-classes: *AI-minor* (prompt wording, retrieval tuning — peer review + evaluation gate), *AI-major* (new model version or provider, new tool with external effect, autonomy-ceiling change — CAB + evaluation gate + 7-day canary on `ring0`/`ring1` + notice to Enterprise tenants where their policy requires), *AI-emergency* (provider outage or safety issue — fallback route or kill switch, retrospective in 2 working days). The model registry (`ai.models`) records approval, evaluation results, region (Bedrock India for confidential classes — NN-15), data classes and retirement dates; provider deprecation notices create change records automatically.

**FR-P23-57 — Evaluation gates.** PRs touching `packages/ai/**`, skills, retrieval builders or guardrails run golden-set evaluations per skill (accuracy, citation resolution against the rules register — NN-14, refusal when no source, AI-label presence, format), the red-team suite, and cost/latency budgets; merge is blocked on a drop > 2 points on any golden metric or any High red-team failure. Nightly runs on production model versions detect drift; drift opens an incident and may demote autonomy automatically (P09).

**FR-P23-58 — Phase completion report (added at traceability review; ChatGPT prompt "How to work with the owner" items 5 and 7, Appendix Z TC-007, TC-009).** The coding agent closes every phase run with a report filed at `docs/phases/Pxx-completion-report.md` (and attached to the release record `rel_`) containing: scope delivered against the phase's FR list (each FR marked DONE / PARTIAL / DEFERRED with the backlog or OI reference); files, modules, tables, APIs, events and settings added or changed; migrations with their expand/migrate/contract stage and rollback note (FR-P23-17); tests and checks actually run with their results and links to CI runs (the report may not state that a test, integration, legal check, accessibility audit, certification or deployment passed unless the linked evidence shows it — NN-20); NN tests touched and their status; open risks; decisions needed from the owner (`[OWNER]`) and counsel (`[COUNSEL]`); `[VERIFY]` items still open in `docs/compliance/verification-log.md`; out-of-scope discoveries logged as backlog items rather than silently added; and the next phase that is ready. Before a material implementation the agent posts the proposed scope, dependencies, risks and acceptance criteria as an ADR or change record (FR-P00-89, FR-P23-12) and waits for the owner's approval at the phase gate. `PLT_RELEASE_MANAGER` is checker for the report; a wave go-live (FR-P23-52) requires every included phase's report to be approved. A report validator (`pnpm phase-report:check`, run in CI when a `docs/phases/*-completion-report.md` file changes) fails when a claimed pass has no linked CI run or evidence artefact, or when an FR of the phase is missing from the status list; `ci/pr-template` requires an approved proposal reference (ADR or change record) on pull requests labelled `material`.

---

## 5. Workflows and state machines

### 5.1 Change record

As FR-P23-12. Guards: `SUBMITTED → ASSESSED` needs risk score and plans; `CAB_REVIEW → APPROVED` needs quorum and all conditional approvals; `SCHEDULED → IMPLEMENTED` needs the deploy gate (FR-P23-13); `IMPLEMENTED → PIR_DONE` within 5 working days for `NORMAL` high-risk, `REGULATED` and `EMERGENCY`.

### 5.2 Release

`PLANNED → CUT (tag, release branch) → STAGING_VERIFIED (e2e-full, DAST, golden archives, performance smoke) → PREPROD_VERIFIED (UAT, migration rehearsal timing) → RING0 → RING1 (≥ 24 h, no SLO burn) → RING2 → DONE`; any stage → `HALTED` (flag off or rollback) → `FIXED` → resume. Emits `ReleasePublished`.

### 5.3 Vulnerability

`NEW → TRIAGED (severity, owner, SLA due) → IN_PROGRESS → FIXED (PR merged) → VERIFIED (scan or retest) → CLOSED`; `TRIAGED → RISK_ACCEPTED (expiry ≤ 90 d) → REOPENED` on expiry; `FALSE_POSITIVE` with reviewer. SLA breach escalates to CTO and security; Critical breach reported to the owner.

### 5.4 Incident

`DETECTED → TRIAGED (severity; clocks started) → CONTAINED → ERADICATED → RECOVERED → NOTIFICATIONS_COMPLETE (CERT-In, DPDP Board, tenants, NeGD, ESPs as applicable) → PIR_DONE → CLOSED`; clocks shown with countdowns as text.

### 5.5 VAPT engagement

`PLANNED → ROE_SIGNED (scope, empanelment snapshot hash, NDA, DPA, test accounts) → FIELDWORK → DRAFT_REPORT → REMEDIATION → RETEST → FINAL_REPORT → CLOSED`.

### 5.6 Restore test

`SCHEDULED → RUNNING → PASSED | FAILED → (FAILED) TICKETED → FIX_DONE → RETEST_SCHEDULED (≤ 24 h) → PASSED`; `SCHEDULED → MISSED` after grace counts as failed.

### 5.7 Go-live

As FR-P23-53, with `HYPERCARE → STEADY_STATE` only when FR-P23-54 exit criteria are met.

---

## 6. Screens and UX

Staff screens in `apps/console` under `/eng/*` (group-level views live in OH13/OH14). All screens keyboard-accessible with table alternatives for charts.

| Screen ID | Name | Purpose and components | Roles |
|---|---|---|---|
| SCR-P23-01 | Engineering home | Changes awaiting approval, releases in flight, vulnerabilities by SLA, incidents with clocks, restore-test status, evidence freshness | CTO, security, SRE, release manager |
| SCR-P23-02 | Change record | Plans, risk score, approvals, linked PRs, `ChangeApproved` status, PIR | All engineering |
| SCR-P23-03 | Change calendar | Changes, windows, freezes, content activations (read-only from P03) | All; tenants see maintenance only |
| SCR-P23-04 | Release console | Ring progression, error budgets, halt/resume, notes preview | Release manager, SRE |
| SCR-P23-05 | Deploy gate status | Five gate conditions per deployment (FR-P23-13) | Approvers |
| SCR-P23-06 | Vulnerability register | Filters by severity, SLA, component, environment; risk acceptances | Security, tech leads |
| SCR-P23-07 | SBOM and end-of-support | Components, licences, EOL dates, plans | Security, CTO |
| SCR-P23-08 | Backup and restore assurance | Coverage matrix, last pass, next due, RTO headroom, RPO achieved | SRE, security, auditors (read) |
| SCR-P23-09 | DR drills | Plans, results, actions | SRE, CTO |
| SCR-P23-10 | VAPT engagements | Lifecycle, findings import, retest | Security |
| SCR-P23-11 | Incident console | Clocks with countdowns, notification checklist, comms templates | Incident commander, DPO |
| SCR-P23-12 | Control evidence | Controls, collectors, freshness, mapping | Security, compliance analyst, auditors (read) |
| SCR-P23-13 | Evidence packs | Build pack per audit type, recipients, expiry | Security, Company Secretary |
| SCR-P23-14 | Access reviews | Campaigns, attestations, revocations | Managers, security |
| SCR-P23-15 | Claims register | Public claims, evidence, expiry | Company Secretary, `PLT_CONTENT_EDITOR` |
| SCR-P23-16 | Go-live checklist | Items by area, owners, evidence, sign-offs | All signatories |
| SCR-P23-17 | Hypercare dashboard | KPIs, triage list, exit criteria | Product owner, SRE |
| SCR-P23-18 | AI change and model registry | Models, evaluations, canaries, retirement dates | AI lead, CAB |
| SCR-P23-19 | Tenant "What's new" and maintenance notices (`apps/web`) | Release notes, scheduled maintenance, early-access opt-in | `ORG_ADMIN`, all users |

---

## 7. Backend design

### 7.1 Modules

`eng` (owner), `core` (audit ledger), `cfg` (flags, kill switches, settings), `xpt` (golden archives, BYO restore evidence), `ai` (model registry), `int` (ecosystem events to OH13/OH14).

### 7.2 Tables (schema `eng`; platform scope; staff-only RLS policies)

| Table | Key columns | Retention |
|---|---|---|
| `change_records` | id (`chg_`), human_ref, class, sub_class, title, prs[], commits[], risk_score, plans jsonb, approvals jsonb, oh13_change_id, approval_version, window, state, pir jsonb | 8 years |
| `releases` | id (`rel_`), version, tag, digests[], sbom_ref, notes_refs, rings jsonb, state, regulatory_impact | 8 years |
| `deployments` | release_id, environment, digest, gate_result jsonb, approvers[], started_at, finished_at | 8 years |
| `freeze_windows` / `change_calendar` | start, end, scope, reason, exceptions | 3 years |
| `vulnerabilities` | id, source, cve/rule, component, version, environment, severity, sla_due, state, owner, links | 8 years |
| `risk_acceptances` | vuln_id, compensating_control, approver, expires_at | 8 years |
| `eos_register` | component, version, eos_date, plan | — |
| `service_catalogue` | service, tier, rpo_s, rto_s, owner | — |
| `restore_tests` | id, data_store, kind, scheduled_for, result, restore_seconds, rpo_achieved_s, checks jsonb, evidence_hash | 8 years |
| `dr_drills` | id, kind, results, actions | 8 years |
| `vapt_engagements` / `vapt_findings` | auditor, empanelment_hash, scope, state; finding, severity, retest | 8 years |
| `incidents` | id, severity, clocks jsonb, notifications jsonb, state, pir | 8 years |
| `control_evidence` | control_id, period, collector, artefact_hash, object_ref, status | 8 years |
| `evidence_packs` | audit_type, recipients, expiry, manifest_hash | 8 years |
| `access_reviews` | campaign, subject, reviewer, decision, at | 8 years |
| `claims_register` | claim_id, text, evidence_ref, expires_at, status | permanent |
| `golive_checklists` / `golive_items` | wave, state; area, item, blocking, owner, evidence_ref, status, signed_by | permanent |

### 7.3 APIs (staff-only, console; `Idempotency-Key` on POST)

`POST /v1/eng/changes` · `POST /v1/eng/changes/{id}:submit|assess|schedule|implement|pir|close` · `POST /v1/eng/deploy-gate:check` (called by the pipeline; returns pass/fail with reasons) · `GET/POST /v1/eng/releases` · `POST /v1/eng/releases/{id}:promote|halt|resume` · `GET/POST /v1/eng/vulnerabilities` · `POST /v1/eng/vulnerabilities/{id}:triage|accept-risk|verify|close` · `POST /v1/eng/restore-tests/{id}:result` (collector) · `GET /v1/eng/control-evidence` · `POST /v1/eng/evidence-packs` · `GET/POST /v1/eng/incidents` · `POST /v1/eng/incidents/{id}/notifications/{kind}:sent` · `GET/POST /v1/eng/golive/{wave}` · `POST /v1/eng/golive/{wave}/items/{id}:sign`. Tenant-facing: `GET /v1/whats-new`, `GET /v1/maintenance`.

### 7.4 Events

Internal: `in.lawdocs.eng.ChangeSubmitted.v1`, `…ChangeImplemented.v1`, `…DeploymentRefused.v1`, `…ReleasePromoted.v1`, `…VulnerabilitySlaBreached.v1`, `…RestoreTestFailed.v1`, `…IncidentDeclared.v1`, `…IncidentClockWarning.v1`, `…GoLiveSigned.v1`. Cross-product via `int` only: consumes `in.infrabyx.ops.ChangeApproved.v1`; publishes `in.infrabyx.ops.ReleasePublished.v1`, `in.infrabyx.ops.ControlEvidenceCollected.v1`, `in.infrabyx.portability.BackupCompleted.v1` (type `PLATFORM`), `in.infrabyx.portability.RestoreTested.v1`, and incident notifications in the Spec's registered form (`SecurityIncidentNotified`) [VERIFY domain name in Spec v1.1 before coding]. No event carries tenant content (NN-19).

### 7.5 Jobs

`ReleaseApprovalWorkflow`, `DeployGateCheck`, `GithubDriftCheckJob` (nightly), `VulnerabilityIngestJob` (hourly), `SlaWatchJob`, `SbomCollectJob`, `EosScanJob` (monthly), `RestoreTestScheduler` + `RestoreTestWorkflow`, `RestoreAssuranceReportJob` (weekly), `EvidenceCollector-*` (scheduled per control), `AccessReviewCampaignJob` (quarterly), `IncidentClockWorkflow`, `ClaimsExpiryJob`, `GoLiveChecklistGenerator`, `ModelDeprecationWatchJob`, `AiEvalNightlyJob`.

---

## 8. Integrations

| System | Use | Failure behaviour |
|---|---|---|
| GitHub (Actions, rulesets, environments, security features) | Source, CI, approvals, scanning | Pipeline down → no deploys; emergency path documented |
| Operations Hub OH13 | CAB record; `ChangeApproved`; incident register | OH13 unavailable → local `eng.change_records` with dual human approval and back-fill; deploy gate accepts a locally recorded approval signed by two CAB members for `EMERGENCY` only |
| Operations Hub OH14 | Control library; provider-assurance room; evidence | Local evidence store; back-fill |
| OH10/OH12 | Staff identities and devices (joiner–mover–leaver) | Access reviews flag mismatches |
| AWS (Backup, KMS, Security Hub, GuardDuty, Inspector, CloudTrail) | Backups, keys, posture | Alerts; manual checks in runbooks |
| Expo EAS, App Store Connect, Google Play Console | Mobile builds and releases | Hold release; hotfix via store expedited review where justified |
| CERT-In-empanelled auditor | VAPT and comprehensive audit | Booked ≥ 8 weeks before wave GA |
| Status page provider (India-resident or self-hosted) | Customer communication | Fallback to email and in-app banner |

---

## 9. Settings and configuration

Full list in Appendix R §R.9 (`eng`).

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `eng.branch.max_age_days_block` | PLATFORM | GOVERNED | integer 2–10 | 5 | CTO | N |
| `eng.deploy.required_approvers` | PLATFORM | LOCKED (floor 2) | integer | 2 | — | — |
| `eng.deploy.require_change_approved` | PLATFORM | LOCKED | boolean | true | — | — |
| `eng.deploy.windows` | PLATFORM | GOVERNED | RRULE list | Tue, Thu 22:00–24:00 IST | `PLT_RELEASE_MANAGER` | Y |
| `eng.freeze.default_windows` | PLATFORM | GOVERNED | date ranges | FR-P23-14 | CAB | Y |
| `eng.notice.behaviour_change_working_days` | PLATFORM | GOVERNED | integer ≥ 5 | 5 | `PLT_RELEASE_MANAGER` | Y |
| `eng.notice.maintenance_hours` | PLATFORM | GOVERNED | integer ≥ 72 | 72 | `PLT_RELEASE_MANAGER` | N |
| `eng.notice.api_deprecation_months` | PLATFORM | GOVERNED | integer ≥ 12 | 12 (P19 FR-P19-06) | CTO | Y |
| `eng.notice.subprocessor_days` | PLATFORM | GOVERNED-privacy | integer ≥ 30 | 30 | `PLT_DPO` | Y |
| `eng.patch.sla_critical_hours` / `_high_days` / `_medium_days` / `_low_days` | PLATFORM | GOVERNED (outer limits LOCKED) | integer | 72 / 7 / 30 / 90 | `PLT_SECURITY_OFFICER` | Y |
| `eng.patch.dependency_cooldown_days` | PLATFORM | GOVERNED | integer 0–14 | 7 | `PLT_SECURITY_OFFICER` | N |
| `eng.risk_acceptance.max_days` | PLATFORM | LOCKED | integer | 90 | — | — |
| `eng.backup.pitr_days` | PLATFORM | GOVERNED (floor 35 LOCKED) | integer | 35 | `PLT_SRE` | Y |
| `eng.backup.t0_rpo_minutes` / `eng.backup.t0_rto_hours` | PLATFORM | LOCKED | integer | 15 / 4 | — | — |
| `eng.restore_test.db_frequency` | PLATFORM | GOVERNED (floor monthly LOCKED) | enum | weekly | `PLT_SRE` | N |
| `eng.dr.drill_frequency_months` | PLATFORM | GOVERNED | integer 3–12 | 6 | CTO | N |
| `eng.logs.retention_days_india` | PLATFORM | GOVERNED (floor 180 LOCKED; DPDP 365 floor for personal-data logs) | integer | 400 | `PLT_SECURITY_OFFICER` | Y |
| `eng.vapt.external_frequency_months` | PLATFORM | GOVERNED | integer 1–6 | 3 | `PLT_SECURITY_OFFICER` | N |
| `eng.flag.bug_bounty` | PLATFORM | GOVERNED-elevated | boolean | false | CTO | Y |
| `eng.hypercare.days` | PLATFORM | GOVERNED | integer | 14 (W1, W2), 21 (W3) | Product owner | N |
| `eng.claims.require_evidence` | PLATFORM | LOCKED | boolean | true | — | — |
| `eng.ai.eval_max_drop_points` | PLATFORM | GOVERNED | decimal | 2.0 | AI lead | Y |

Customisation hooks for tenants: early-access ring opt-in (`eng.rings.early_access_opt_in`, TENANT, OPEN), audit-period ring pin (Enterprise; `eng.rings.pin_days`, TENANT, GOVERNED), maintenance-notice recipients (TENANT, OPEN).

---

## 10. Security, privacy and audit

| Threat | Control |
|---|---|
| Compromised developer account pushes malicious code | Signed commits, CODEOWNERS two-person rule on critical paths, required review of the latest push by another person, merge queue, signed images and provenance check at deploy |
| Rogue administrator deploys outside the pipeline | Deploy role assumable only by the gate workflow; SCPs; CloudTrail alerts on console changes; drift detection |
| Supply-chain attack via dependency | Cool-down, provenance, SBOM, SCA, pinned Actions |
| Production data in lower environments | LOCKED rule; regex scans of fixtures; isolated rehearsal VPC inside prod with no human access |
| Backups deleted by ransomware or insider | Separate backup account, Vault Lock compliance mode, SCP deny rules, KMS deny-deletion policies, air-gapped monthly copies |
| Unevidenced certification claims | Claims register + CI content check (NN-20) |
| Engineering metrics used for surveillance | Team-level DORA metrics only (NN-33, CH-24, CH-32) |

Audit: every change record transition, deploy gate decision, risk acceptance, break-glass use, evidence pack issue and go-live signature is written to the hash-chained ledger (platform tenant) in the same transaction (NN-02, NN-45). Logs and traces pass PII scrubbing; incident records never copy tenant document content (NN-32).

---

## 11. AI touchpoints and guardrails

| Touchpoint | What AI does | Guardrail |
|---|---|---|
| PR summaries and release-note drafts | Drafts from diffs and PR templates | Author edits; release manager approves customer text |
| Vulnerability triage assist | Suggests reachability and fix versions | Security engineer decides severity and SLA |
| Incident timeline drafting | Drafts PIR timeline from logs and chat | Incident commander owns; no tenant content in prompts |
| Evidence mapping suggestions | Suggests control mappings for new collectors | Compliance analyst confirms |

AI never approves a change, deploys, accepts risk or sends a regulatory notification (NN-13, NN-43). Engineering AI runs on the provider-neutral gateway with the same data-class rules (NN-15).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p23/*.feature`)

```gherkin
@P23-AT-01 @NN-18
Scenario: Deployment without ChangeApproved is refused
  Given release v2026.12.1 with green checks and two approvals
  And no matching ChangeApproved from OH13
  When the pipeline requests production deployment
  Then the deploy gate returns LD-ENG-010 "Change not approved" and the CTO is alerted

@P23-AT-02 @NN-18
Scenario: Author cannot approve own release
  Given engineer "E" authored commits in release v2026.12.1 and is a tech lead
  When "E" approves the production deployment
  Then the approval is rejected with LD-ENG-011 "Approver authored changes in this release"

@P23-AT-03
Scenario: Unsigned commit blocked on main
  When a pull request contains an unsigned commit
  Then the merge is blocked by the ruleset

@P23-AT-04 @NN-12
Scenario: Destructive migration in the same release is blocked
  Given a migration that drops column "clm.agreements.legacy_title" while code still reads it
  When ci/migrations runs
  Then the build fails with "Destructive change must follow contract phase"

@P23-AT-05 @NN-12
Scenario: Migration touching an export-mapped column without mapping update fails
  Given column "lit.cases.forum_code" referenced by xpt.export_map
  When a migration changes its type without an export-map version
  Then ci/export-contract fails

@P23-AT-06 @NN-30
Scenario: Code release does not alter published content
  Given hashes of rul.rule_set_versions and tpl content versions before the rehearsal
  When the release rehearsal runs all migrations
  Then all hashes are unchanged

@P23-AT-07
Scenario: Critical vulnerability follows the emergency lane
  Given a KEV-listed CVE in an internet-exposed component discovered at 10:00 IST
  Then a vulnerability record is created with SLA due within 72 hours
  And alerts fire at 50% and 80% of the SLA
  And a breach pages PLT_SECURITY_OFFICER and marks the control failing

@P23-AT-08
Scenario: Risk acceptance expires
  Given a High vulnerability accepted with expiry 90 days
  When 90 days pass without fix
  Then the vulnerability returns to REOPENED and the owner is notified

@P23-AT-09
Scenario: Weekly restore test proves recoverability
  When the weekly automated restore of the core database runs
  Then it completes within 4 hours, audit.verify_chain() passes on the restored copy
  And a RestoreTested event with the evidence hash is published

@P23-AT-10
Scenario: Missed restore test counts as failed
  Given a restore test scheduled for Monday with 24 hours grace
  When no result is recorded by Tuesday
  Then the test is MISSED, a Sev-3 incident opens and the control is failing

@P23-AT-11 @NN-27
Scenario: Log retention floor is enforced
  When a change tries to set eng.logs.retention_days_india to 120
  Then validation fails with LD-CFG-004 "Below the 180-day floor"

@P23-AT-12 @NN-25
Scenario: Infrastructure outside India is blocked
  When a Terraform plan creates a tenant-data bucket in a non-India region
  Then the policy check fails the plan

@P23-AT-13 @NN-27
Scenario: CERT-In clock starts at detection
  Given a reportable incident detected at 14:00 IST
  Then the incident shows "CERT-In report due by 20:00 IST"
  And escalations fire at 16:00 and 18:00 IST if not marked sent

@P23-AT-14 @NN-20
Scenario: Public page cannot claim certification without evidence
  Given a page draft stating "LawDocs is ISO 27001 certified" without a claim ID
  When the content check runs
  Then publication is blocked with "Unregistered claim"

@P23-AT-15
Scenario: PCI scope stays SAQ A
  Given the checkout uses Razorpay hosted checkout via OH8
  When the card-data scan runs on LawDocs logs, databases and front-end bundles
  Then no PAN, CVV or card track data is found and no LawDocs endpoint receives card fields

@P23-AT-16 @NN-28
Scenario: Accessibility blocks ring2 promotion
  Given a wave release with an axe "serious" violation on the signing screen
  When promotion to ring2 is requested
  Then promotion is blocked until the violation is fixed or waived by the QA lead with reason

@P23-AT-17 @NN-38
Scenario: Go-live blocked by a live VERIFY-dependent flag
  Given flag "chp.flag.rbios_auto_timeline" depends on an open VERIFY entry and is ON in pre-prod
  When the Wave 3 go/no-go is requested
  Then the checklist shows a blocking item "Flag depends on unverified fact"

@P23-AT-18 @NN-39
Scenario: Kill-switch drills are part of go-live
  Given an NN-39 switch not drilled in the last 90 days
  Then the go-live checklist marks "Kill-switch drills" as not done

@P23-AT-19
Scenario: Hypercare exit requires stability
  Given Wave 1 in hypercare day 14 with an open Sev-2
  Then the state stays HYPERCARE until no Sev-1/2 is open and error budgets are healthy for 7 days

@P23-AT-20 @NN-02
Scenario: Region failover keeps the audit chain intact
  When the semi-annual DR drill fails over to ap-south-2 and fails back
  Then audit.verify_chain() passes end to end across both moves
  And the golden-archive diff for sampled tenants is empty

@P23-AT-21
Scenario: AI model change needs evaluation and canary
  Given a proposal to switch the drafting skill to a new model version
  When the evaluation shows a 3-point drop in citation correctness
  Then the merge is blocked and the change cannot enter canary

@P23-AT-22 @NN-32
Scenario: No secrets or Aadhaar in logs
  When the log scanner runs over the last 24 hours of production logs
  Then no secret patterns, OTPs, full PAN or Aadhaar numbers are found

@P23-AT-23 @NN-20
Scenario: Phase completion report cannot claim unevidenced results (FR-P23-58)
  Given the coding agent closes phase P08 and drafts "docs/phases/P08-completion-report.md"
  When the report marks "@P08-AT-07 passed" without a linked CI run that shows it green
  Then the report validator fails with the claim listed as unevidenced
  And the report lists every FR of P08 as DONE, PARTIAL or DEFERRED with a backlog or OI reference
  And it lists migrations with their expand, migrate or contract stage and rollback note, open [VERIFY] items, [OWNER] and [COUNSEL] decisions and the next ready phase
  When PLT_RELEASE_MANAGER approves the report as checker
  Then it is attached to the release record and counts towards the wave go-live checklist

@P23-AT-24
Scenario: Proposal before material implementation (FR-P23-58)
  Given a material change to the signing ceremony is planned
  When implementation starts without an approved ADR or change record stating scope, dependencies, risks and acceptance criteria
  Then the pull request fails "ci/pr-template" with "approved proposal reference missing" and cannot merge

@P23-AT-25
Scenario: Traceability and verification checks are required
  Given a pull request renumbers FR-P15-70 without updating Appendix Z
  Then "ci/trace-check" fails naming the dangling FR reference
  Given a pull request adds a new "[VERIFY: …]" marker with no matching V-* rule
  Then "ci/verify-census" fails and the pull request cannot merge
```

Gherkin `@P23-AT-01…25` green. NN tests added: `NN-18_deploy_maker_checker`, `NN-12_destructive_migration_blocked`, `NN-30_release_does_not_touch_content`, `NN-27_log_retention_floor`, `NN-27_certin_clock`, `NN-25_iac_region_policy`, `NN-20_claims_register`, `NN-28_release_a11y_gate`, `NN-38_golive_verify_flags`, `NN-02_dr_chain_continuity`, `NN-32_log_scanner`.

---

## 13. Exit gate, deliverables and open items

### 13.1 Governance track (before P04 exits)

- [ ] GitHub rulesets, CODEOWNERS, signed commits, PR template, required checks live and exported nightly; drift check running.
- [ ] Environments dev/test/staging/pre-prod/prod/DR provisioned by Terraform with policy checks; OIDC deploy federation; secrets in Secrets Manager.
- [ ] Change records, deploy gate and `ChangeApproved` consumption (or local fallback) working end to end; first `ReleasePublished` emitted.
- [ ] `ci/migrations`, `ci/export-contract`, `ci/golden-archive-diff`, `ci/config-registry`, `ci/axe`, `ci/sbom`, `ci/trace-check` and `ci/verify-census` green on `main` (the census script itself is a P00 deliverable — Appendix W §W.1 step 7).
- [ ] Phase completion report (FR-P23-58) template and validator live; every phase closed in the wave has an approved report.
- [ ] Vulnerability intake and SLA watch running; EOS register seeded.

### 13.2 Go-live track (per wave)

- [ ] Wave go-live checklist complete with all blocking items done and six sign-offs.
- [ ] VAPT for wave scope closed (Critical/High); CERT-In-empanelled annual audit booked or done.
- [ ] Restore tests green for all T0 stores; DR drill within RPO/RTO in the last 6 months.
- [ ] Control evidence ≥ 80% automated (Wave 1 target 60%, Wave 2 80%) [REC]; readiness assessment booked.
- [ ] Manual accessibility audit for wave screens passed.
- [ ] Claims register in force; trust page shows only evidenced claims.
- [ ] Hypercare plan, on-call and status page live.

### 13.3 Re-run per wave

Wave 2 adds: mobile store releases and MASVS testing, litigation data aggregator resilience, marketplace counsel opinion, delivery-console access reviews. Wave 3 adds: Consumer Help entity and ethical-wall tests, telecom (voice/WhatsApp) compliance checks, tax-module freeze windows, longer hypercare.

**Registered:** export-map entries for LawDocs' own platform records are not tenant data and are excluded from tenant exports (`x-export: excluded`, reason "platform engineering records"); tenant-visible artefacts — release notes and maintenance notices — map to `99 System Data (CSV and JSON)/Platform Notices/` in tenant exports. Settings `eng.*` in Appendix R. Help keys `hlp.eng.release_ring`, `hlp.eng.maintenance`, `hlp.eng.early_access`, `hlp.eng.trust_claims`. Errors `LD-ENG-001`–`LD-ENG-060`. Screens SCR-P23-01–19.

**Demo script:** an engineer opens a PR adding a column; CI shows the expand step and export-map update; CAB approves in OH13; two approvers release through rings; a weekly restore test runs and publishes evidence; a simulated KEV vulnerability flows through the emergency lane; the Wave 1 checklist is signed.

| ID | Open item | Owner | Fallback |
|---|---|---|---|
| OI-P23-01 | GitHub plan and security add-on names and pricing | CTO | Compensating controls (FR-P23-01) |
| OI-P23-02 | Applicability details of CERT-In's 2025 audit guidelines to LawDocs | `PLT_SECURITY_OFFICER` | Annual audit by empanelled auditor regardless |
| OI-P23-03 | ESP contract audit frequency and incident-notice terms | P08 lead | Annual ASP audit [REC] |
| OI-P23-04 | Exact Ecosystem Spec domain and type for security-incident notifications | Ecosystem architecture board | Use Spec v1.1 name verbatim once confirmed |
| OI-P23-05 | Store policy limits on over-the-air updates and data-safety declarations | P22 lead | No OTA updates beyond bug fixes |
| OI-P23-06 | PCI DSS SAQ A eligibility confirmation with acquirer/QSA for Razorpay Standard Checkout | OH8 owner | Redirect-only hosted checkout |
| OI-P23-07 | OH13/OH14 availability dates for LawDocs onboarding | Operations Hub programme | Local `eng` system of record with back-fill |
| OI-P23-08 | ITR due dates under the Income-tax Act 2025 for freeze planning | [TAX MEMO] | Freeze configurable by CAB yearly |
