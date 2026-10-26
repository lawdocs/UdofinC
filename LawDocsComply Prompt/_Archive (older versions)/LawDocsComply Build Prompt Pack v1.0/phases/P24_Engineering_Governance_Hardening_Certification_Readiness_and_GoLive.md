# Phase P24 — Engineering Governance, Hardening, Certification Readiness and Go-Live

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (CI/CD skeleton, audit ledger, buckets, infrastructure), P01 (identity, grants, break-glass), P02 (settings registry), and every functional phase whose scope is being released. The **first P24 run** (general-availability go-live) needs P00–P07, P15 (at least the RBI-NBFC, MCA-CO and DATA-PRIV families), P18 (integration gateway core), P19 (export package) and P20 (billing). Later phases released after go-live each **re-run the P24 checklist for their scope** (§13.3).
>
> **Sequencing:** the engineering-governance part (§4A–§4E) starts in parallel with P02 (sprint 3 of the programme) so that every later phase is built under the final controls; hardening, certification evidence and go-live (§4F–§4K) run before general availability.
>
> **Binding appendices:** Q (security, privacy and certification readiness — control set and evidence catalogue), B (eng tables, error codes), A (change, release, incident, vulnerability state machines), U (settings), V (acceptance catalogue — the go-live regression suite), X (Operations Hub addendum — OH13/OH14 interfaces).
>
> **Requirements covered:** R-033, R-046, R-047 (engineering staff across group repositories), R-031, R-021 (preservation across releases and infrastructure moves), R-075, R-081 (backups and BYO storage evidence), R-101 (final review discipline).
>
> **Decisions applied:** D-01, D-02, D-03 (OH13/OH14 own the group console and provider-assurance room), D-13, D-14, D-21.
>
> **Estimated effort:** governance track 3 sprints (platform squad of 4) running alongside P02–P05; hardening and go-live track 4 sprints (squad of 7: SRE, 2 security engineers, QA lead, 2 backend, compliance analyst) before GA; each later re-run 1 sprint.

---

## 1. Objective and business outcome

The owner will push code to GitHub regularly — patches, new features, framework upgrades, infrastructure moves — while banks, NBFCs, listed companies and co-operative societies rely on LawDocsComply for records that regulators, auditors and boards will inspect. P24 makes change safe and provable: every change is reviewed, tested, approved, traceable to a release and reversible; data and the client's folder structure survive every release and every infrastructure move; backups are tested by restoring them; vulnerabilities are found and fixed within published SLAs; and the platform is ready for independent assurance — SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI), ISO 22301 (continuity) and PCI DSS self-assessment for the payment flow — without making any certification claim before a certificate or report exists (NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Every production change is approved and traceable | 100% of production deployments in the last 30 days map to a change record with `ChangeApproved` (OH13) and a signed image digest; 0 deployments outside the pipeline |
| Releases never break client data or folder structure | Expand-contract checker, export-mapping contract (NN-10) and golden export comparison pass for every release; zero manual customer migration steps in release notes (NN-11) |
| Recoverability proven | Latest restore test of every T0 store succeeded within RTO; a full DR drill to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence stored |
| Security debt under control | No open Critical; no High older than its SLA; VAPT (CERT-In empanelled auditor) final report issued after retest with all Critical/High closed |
| Certification-ready | Appendix Q control set implemented with automated evidence for ≥ 80% of controls; policy set approved by the Board; readiness assessment by an external firm with no Critical gaps; SOC 2 Type 1 audit window can start |
| Go-live safe | Go-live checklist (§4J) signed by CTO, CISO, Company Secretary and product owner; first paid RE tenants live on the AWS production estate (P00 ADR-0006) |

---

## 2. Scope (in / out)

**In scope**

- GitHub organisation, plan, repositories, branch model, rulesets, CODEOWNERS, required checks, merge queue, signed commits, environments and deployment protection.
- Change management: change classes, risk scoring, change records, CAB (via OH13), freeze windows, emergency changes, post-implementation review; tenant notices and API deprecation policy.
- Release management: release trains, versioning, release rings (internal → canary tenants → general), feature flags for progressive delivery, release notes (internal and customer-facing), customer sandbox tenants.
- Content releases vs code releases: regulatory content publication (P05) is governed separately and never requires a code deployment; code releases never alter published content.
- Database migration safety, schema evolution and data-preservation guarantees across releases and infrastructure moves.
- Patch and vulnerability management with SLAs; dependency and image hygiene; end-of-support register.
- Backup, restore testing, disaster recovery, business continuity; BYO-storage backup evidence (P19).
- Security testing: SAST, DAST, SCA, secrets, IaC, container, API fuzzing, AI red-teaming hooks; VAPT and the CERT-In comprehensive audit; responsible disclosure.
- Audit readiness for LawDocsComply itself: IS audit, internal audit, external audit, client audits of LawDocsComply as their service provider; evidence collectors; auditor read-only workspace (provider-assurance room in OH14).
- Certification readiness: SOC 2, ISO 27001/27701/42001/22301, PCI DSS v4.0.1 SAQ A for hosted checkout; policy set; risk register; supplier management; access reviews.
- Hardening: application, cloud, Kubernetes/ECS, database, identity, email, DNS, web headers, CSP, bot and abuse protection.
- Performance, load, soak and chaos tests; capacity planning.
- Incident management, status page, customer communication, regulatory incident clocks (CERT-In 6 hours; client RE notification ≤ 2 hours so the RE can meet its 6-hour duty; DPDP breach intimation and 72-hour report).
- Go-live checklist and post-go-live operations (hypercare, SLO reviews, monthly security report to the Board's committee).

**Out of scope**

- The group-wide engineering-operations console and CAB tooling (OH13) and the certification control library and provider-assurance room (OH14) — built in the Operations Hub; LawDocsComply emits events and evidence to them and consumes `ChangeApproved` (D-03; Appendix X).
- The policies themselves (information security policy, access control, etc.) — the owner prepares them (brief); P24 lists them (Appendix Q §Q.11), provides templates in the policy module (P07) and records approvals.
- Tenant-facing IT governance features for clients (their own ISMS, VAPT tracking, CERT-In incidents) — P12.

---

## 3. Personas and permissions touched

| Role | Responsibility |
|---|---|
| CTO (staff realm, `eng_cto`) | Owns engineering governance; approves NORMAL changes with CAB; second approver for emergency changes |
| Security lead / CISO (`plt_security_officer`) | Vulnerability SLAs, VAPT, risk acceptances, incident command for security incidents, key management |
| SRE (`eng_sre`) | Infrastructure, backups, DR, observability, on-call |
| Release manager (`eng_release_manager`) | Release trains, freeze windows, tenant notices, release notes |
| Developers (`eng_developer`) | Code and tests; **no standing production data access** (SoD); production read through break-glass only |
| QA lead (`eng_qa`) | Test strategy, regression suite (Appendix V), performance tests |
| Compliance reviewer (`eng_compliance_reviewer` — CS or nominee) | Reviews REGULATED changes (calculations, rule packs, returns formats, audit trail, retention, residency, billing) |
| Product owner | Accepts releases, approves customer notices |
| `plt_auditor` and external auditors | Read-only assurance workspace (OH14 provider room) |
| `ten_admin` | Receives release notes and notices; may enrol the tenant in the early-access ring; may run a customer sandbox |

Staff roles live in the `ldc-staff` realm (P01) and in the OH13/OH14 role model.

---

## 4. Functional requirements

### 4A. Source control and branching

**FR-P24-01 — GitHub plan and organisation.** Repositories under the group's GitHub Enterprise account in an organisation for the LawDocsComply legal entity (OH13.1 repository register). Use **GitHub Enterprise Cloud** with **Secret Protection** and **Code Security** for private repositories: environment required reviewers, wait timers and custom deployment protection rules on private repositories, and CodeQL/secret scanning/push protection on private repositories need these paid tiers [VERIFY: current GitHub plan wording and INR pricing]. Until licensed, a compensating control applies: GitHub Actions builds, signs and publishes only; production deployment is executed by a Temporal `ReleaseApprovalWorkflow` in the shared account that assumes the production deploy role only when two valid approvals and an OH13 `ChangeApproved` exist; Semgrep CE, gitleaks, osv-scanner and Trivy replace the paid scanners; the gap is risk `RISK-ENG-001` with a review date. GitHub audit log streams to the log-archive account in India (CERT-In log retention).

**FR-P24-02 — Repositories.** `lawdocscomply` (monorepo, P00), `lawdocscomply-infra` (Terraform and policy-as-code; apply rights for SRE only), `lawdocscomply-content` (optional: reviewed regulatory content packs, Excel templates (Appendix E) and rule packs as versioned artefacts with signed releases — recommended so that content history is independent of code history), `lawdocscomply-legacy` (archived), shared `infrabyx-contracts` (Ecosystem Spec, schemas — consumed as pinned versions), `infrabyx-returns-kernel` (D-05; owned jointly with Finbyx; consumed as pinned version), `infrabyx-labour-rulepack` (shared Labour Code rule pack, Ops Hub item 8; consumed by P13), `.github` (org templates, reusable workflows pinned by SHA).

**FR-P24-03 — Branch model.** Trunk-based development: short-lived feature branches (≤ 2 working days; warning at day 2, merge blocked at day 5 without a tech-lead label), squash merge into `main`, unfinished work dark behind release flags. **Release branches** `release/YYYY.MM.N` are cut at each release tag and exist to patch a deployed release: fixes land on `main` first and are cherry-picked to the release branch, never the reverse. **Hotfix** = cherry-pick + patch tag `vYYYY.MM.N+1`. No long-lived `develop` branch (merge debt without audit benefit). Auditability comes from signed tags, immutable image digests, change records and the audit ledger — not from branch topology. This meets the owner's instruction that "the system should be managed through branches" while keeping integration continuous.

**FR-P24-04 — Rulesets (organisation level, all repositories).**

| Rule | `main` | `release/*` | Tags `v*` |
|---|---|---|---|
| Pull request required | Yes, ≥ 1 approval (≥ 2 for paths in CODEOWNERS "critical": migrations, RLS, audit, crypto, authz policies, calculation packages, export mappings, billing) | Yes, ≥ 2 | — |
| Code-owner review | Required | Required | — |
| Dismiss stale approvals on push | Yes | Yes | — |
| Required status checks | `ci/lint`, `ci/typecheck`, `ci/test`, `ci/nn`, `ci/migrations`, `ci/rls-lint`, `ci/export-contract`, `ci/openapi-breaking`, `ci/sast`, `ci/sca`, `ci/secrets`, `ci/iac`, `ci/axe`, `ci/e2e-smoke`, `ci/pr-template` | Same + `ci/e2e-full` | — |
| Merge queue | Yes | No | — |
| Linear history, squash only | Yes | Yes | — |
| Signed commits | Required (SSH or GPG signing, or GitHub web-flow) | Required | Signed annotated tags only; creation restricted to release managers |
| Force push / deletion | Blocked | Blocked | Blocked |
| Bypass | None (admins included); emergency bypass only through the documented emergency path with an OH13 `EMERGENCY` change | Same | Same |

A nightly job exports rulesets and branch protections as JSON to the log archive and to OH13 for drift detection; drift opens an incident.

**FR-P24-05 — Pull-request template** (validated by `ci/pr-template`): summary; change type (feature, fix, refactor, dependency, infrastructure, content-engine, calculation, security); risk (pre-fills the change-record score); rollout and rollback; **data migration** (expand/migrate/contract step, backfill plan, reversibility); **export mapping impact** (tables/columns added, renamed, removed; mapping updated; golden export diff attached); privacy impact (new personal data, new processor, data class changes); NN impact (which NN rules are touched; tests added); testing evidence; customer-facing release-note text; regulatory impact (yes/no — if yes, compliance reviewer required).

### 4B. Change management

**FR-P24-06 — Change classes** (align with OH13.2 classes):

| Class | Examples | Approval |
|---|---|---|
| `STANDARD` | Pre-approved catalogue: dependency patch with green CI, copy change, UI fix behind a flag, scaling within limits | Logged; auto-approved by the catalogue rule |
| `NORMAL` | Features, refactors, non-regulated schema changes, new integrations | CAB (OH13; weekly; quorum 4 incl. security) or, for low risk score, tech lead + release manager |
| `REGULATED` | Anything that changes: due-date or frequency engines, applicability rules, ratio/capital/stress calculations, return formats or cell maps, CIC layouts, payroll/tax calculations, audit-trail or correction logic, retention or deletion, residency, encryption, authz policies, billing/GST invoicing, export package format | CAB + compliance reviewer + golden-case pass (calculation goldens, return-file goldens, export goldens) |
| `EMERGENCY` | Sev-1 fix; actively exploited vulnerability | Two of CTO, security lead, on-call engineering lead; retrospective CAB within 2 working days |

**FR-P24-07 — Change record** (`eng.change_records`, mirrored to OH13 via events): id, class, title, linked PRs and commits, risk score (deterministic function: impact × likelihood, tenants affected, data migration, reversibility, regulated flag, blast radius by release ring — pure function with 100% branch coverage), expand-migrate-contract plan, rollback or forward-fix plan, test evidence, tenant communication (notice text and date), window, approvers, outcome, PIR. States as OH13.2: `DRAFT → SUBMITTED → ASSESSED → CAB_REVIEW → APPROVED | REJECTED | DEFERRED → SCHEDULED → IMPLEMENTED → PIR_DONE → CLOSED`; `FAILED → ROLLED_BACK | FORWARD_FIXED → PIR_DONE`. A production deployment without a matching `ChangeApproved` (idempotent on change_id + approval version) is refused by the deploy gate.

**FR-P24-08 — Freeze windows.** Default LawDocsComply freezes (configurable): last 3 and first 3 working days of each quarter (board-meeting and quarterly-return season for clients); 25 March–5 April and 25 September–5 October (FY-end and half-year returns); the 7 days before major statutory deadlines selected by the compliance reviewer each year (e.g., AOC-4/MGT-7 filing season, GSTR-9 due dates, RBI annual returns); a client-requested freeze for a scheduled RBI inspection (tenant-specific: deployments proceed but the tenant stays on the previous release ring if isolation permits). A release in a freeze needs an emergency change or a recorded CAB exception.

**FR-P24-09 — Customer notice and API deprecation.** Regulatory-impact releases are notified to affected tenants ≥ 5 working days ahead (OH13.1) through the **Updates** feed (category "Platform release") and email to `ten_admin`; breaking API changes follow: announcement → ≥ 6 months parallel support of the old major version → sunset (headers `Deprecation`, `Sunset` per RFC 9745/8594) [VERIFY RFC numbers]; webhook payload changes are additive within a major version (Ecosystem Spec §3.3 BACKWARD compatibility).

### 4C. Release management

**FR-P24-10 — Versioning and trains.** Calendar versioning `YYYY.MM.N` for the platform; semantic versions for published packages, contracts and SDKs. Weekly release train (Tuesday 22:00 IST deployment window, low-traffic) plus a hotfix lane. Release notes generated from Conventional Commits and the PR template's customer text; published in the help centre "What's new" (P23) and the Updates feed.

**FR-P24-11 — Release rings.** `ring0` internal (LawDocs and Infrabyx `LDC_GROUP` tenant), `ring1` early-access tenants (opt-in by `ten_admin`; sandbox tenants by default), `ring2` general. Ring promotion after error-budget checks (no SLO burn alarm for 24 h). Because the platform is multi-tenant on one code version, rings are implemented by **feature flags per tenant segment**, not by separate deployments; schema changes always ship expand-first so all rings run on the same schema.

**FR-P24-12 — Customer sandbox.** A tenant may create a sandbox (`kind = sandbox`, P02) seeded with synthetic data or a masked copy of its configuration (never its personal data) to test new releases, settings and integrations; sandboxes receive `ring1` features early.

**FR-P24-13 — Content releases are not code releases.** Publishing regulatory content (new master direction, amended actionable — P05) is a governed content workflow with its own maker-checker-publisher approvals and audit trail; it changes data, never code, and can happen any day including freeze windows. Conversely, a code release must not alter published content or tenant overlays: a CI test diffs content tables before and after migrations in the release rehearsal (`NN-03_release_does_not_touch_content`).

### 4D. Database migration and data preservation across releases and infrastructure moves (R-021, NN-10, NN-11)

**FR-P24-14 — Expand-migrate-contract.** Every schema change is split: **expand** (add nullable columns/tables, new indexes concurrently, dual-write in code), **migrate** (backfill in batches as a Temporal job with progress, throttling and resumability; verification query), **contract** (remove old columns/paths) in a later release after verification and at least one release cycle. `ci/migrations` rejects destructive statements (DROP, RENAME, type narrowing, NOT NULL without default on large tables) in the same release as the code that stops using them; locks are bounded (`lock_timeout`, `statement_timeout` in migration scripts); large-table changes use online techniques. Migrations are forward-only; rollback is a forward fix or a flag-off of the new code path while the expanded schema remains.

**FR-P24-15 — Data preservation guarantees.** (a) Stable identifiers never change across releases or moves (prefixed ULIDs, P00); (b) object-storage keys are content-addressed or ID-based (`<tenant>/<module>/<aggregate-id>/<version>/<sha256>`), never derived from display names, so renames do not move files; (c) the client's folder taxonomy is generated from the versioned export mapping (`LDC-EXPORT-1.0`, Appendix M), not from storage paths, so the downloaded or BYO-synced folder structure stays the same when code, server type, database engine or data-centre location changes; (d) a change to the folder taxonomy itself is a `REGULATED` change that bumps the package version (`LDC-EXPORT-1.1`), keeps a compatibility map from old paths to new, and is announced; (e) **golden export test**: for every release, the export of the `demo` seed tenants is generated and compared with the previous release's golden export — any unexpected path, file name, column heading or count difference fails the release; (f) BYO-storage sync (P19) is idempotent and path-stable, so a release never creates duplicate folders in a client's OneDrive, SharePoint, Google Drive, S3 bucket or server.

**FR-P24-16 — Infrastructure moves.** Moving from Supabase to RDS/Aurora, changing instance types, moving regions within India, or moving to a client-dedicated cluster (`isolation_tier = dedicated_cluster`) follows a runbook: logical replication or snapshot restore → dual-run reconciliation (row counts, checksums per table, audit chain verification end-to-end, export golden comparison for sampled tenants) → cut-over in a maintenance window → post-move verification. The audit chain continues unbroken across the move (chains are data; verification after the move must pass). Evidence (reconciliation report, chain verification, golden export diff) is filed under the change record.

### 4E. Patch and vulnerability management

**FR-P24-17 — Intake.** Dependabot alerts and security updates, CodeQL (or Semgrep), secret scanning and push protection (or gitleaks), osv-scanner, Trivy (images, IaC), Checkov, cloud posture (AWS Security Hub with CIS AWS Foundations benchmark, GuardDuty, Inspector), DAST (OWASP ZAP baseline on every staging deployment; authenticated full scan weekly), API fuzzing (OpenAPI-driven, Schemathesis), CERT-In and vendor advisories, VAPT findings, bug reports via `security.txt` (RFC 9116) and the vulnerability disclosure policy. Normalised into `eng.vulnerabilities` and mirrored to OH13.3 (one record per CVE/rule × component × version × environment); severity from CVSS adjusted for EPSS, CISA KEV, reachability, exposure and data class.

**FR-P24-18 — SLAs** (platform floor = OH13.3/Finbyx EO1.6; a stricter client contract wins):

| Severity | Remediation SLA from triage |
|---|---|
| Critical (CVSS 9.0–10.0), KEV-listed or actively exploited | 72 hours (emergency lane) |
| High (7.0–8.9) | 7 days |
| Medium (4.0–6.9) | 30 days |
| Low (0.1–3.9) | 90 days |
| Leaked secret | Revoke and rotate within 24 hours, any severity |

Triage within 24 hours for Critical. Closure needs fix, regression test, verification scan and recurrence check across supported release branches. Exceptions need a security-lead risk acceptance with compensating control and expiry ≤ 90 days. Monthly SLA attainment report to CTO and security lead; quarterly summary to the Board's committee; tenant-facing security summary in the trust centre (counts only).

**FR-P24-19 — Patching cadence.** Base images rebuilt weekly and on critical CVEs; Node.js, PostgreSQL minor, Keycloak, Temporal, OpenSearch, Redis patch releases applied within 30 days (critical security releases within the SLA above); end-of-support register for languages, frameworks, databases, OS images and SaaS dependencies with upgrade plans ≥ 6 months before EOL (Node.js 24 maintenance end-of-life dates tracked [VERIFY]).

### 4F. Backup, restore and disaster recovery

**FR-P24-20 — Tiers.**

| Tier | Systems | RPO | RTO | Mechanism |
|---|---|---|---|---|
| T0 | PostgreSQL `ldc_core` and `ldc_sealed`, Temporal DB, Keycloak DB; S3 evidence and documents; audit anchors | ≤ 15 min | ≤ 4 h (target 2 h) | Multi-AZ; cross-region replica or Aurora Global Database to ap-south-2; PITR 35 days; S3 cross-region replication with Object Lock replication; snapshots for logical corruption |
| T1 | Search index metadata, configuration stores (flags, Cerbos policies, Keycloak realm export), generated exports | ≤ 1 h | ≤ 8 h | Snapshots, nightly config exports, rebuild |
| T2 | OpenSearch indices, Redis, analytics marts | ≤ 24 h | ≤ 24 h | Rebuild from PostgreSQL and object storage (indexers replay) |
| T3 | Source code mirror, CI history, Microsoft 365 workspace of LawDocs staff (OH12) | Vendor-defined / daily mirror | — | Nightly mirror of repositories to the backup account with Object Lock (400 days) |

During the Supabase beta (P00 ADR-0006): PITR in-region plus daily encrypted logical backups to ap-south-2; RPO 24 h for region loss, disclosed to beta tenants.

**FR-P24-21 — Backup policy.** PITR 35 days; daily snapshots 35 days; monthly 13 months; financial-year-end snapshots 8 years (books of account, invoices and evidence retention — Companies Act 2013 s.128(5); client evidence follows its own Object Lock retention); backups in a separate backup account with vault lock and separate credentials (ransomware isolation); encryption with backup-specific KMS keys; sealed-database backups keep sealed keys (multi-Region keys) and are never restored into a shared environment.

**FR-P24-22 — Restore testing.** Weekly automated restore of the latest T0 database snapshot into an isolated account with integrity checks (row counts, audit-chain verification, sampled export comparison) and timing; monthly random sample of evidence objects restored and SHA-256 compared with `dms.evidence_ledger`; quarterly restore of Keycloak realm export and configuration; quarterly restore + build of the latest release tag from the code mirror. Results in `eng.restore_tests`; a failed test is a Sev-2 incident.

**FR-P24-23 — DR drills.** Semi-annual full regional failover drill to ap-south-2 (game day) with measured RPO/RTO, customer-facing status page updates rehearsed, and failback; annual tabletop for ransomware, insider (malicious super admin), cloud account compromise and key loss. Drill reports filed as evidence (ISO 22301, SOC 2 A1).

**FR-P24-24 — Client-held copies.** Clients may keep their own copies through P19 (scheduled export to BYO storage — S3, Azure Blob, Google Cloud Storage, SFTP, SharePoint/OneDrive, Google Drive, on-premise agent). P24 includes these in the business-continuity narrative (clients retain readable records even if LawDocsComply is unavailable) and tests the scheduled export job as part of restore testing.

### 4G. Security testing, VAPT and the CERT-In audit

**FR-P24-25 — Continuous testing in CI/CD.** SAST, SCA, secrets, IaC, container scanning on every PR (P00); DAST on every staging deployment; authenticated DAST weekly; API fuzzing nightly; dependency review on PRs; SBOM per image; AI red-team test suite for Vidhi (prompt injection from uploaded documents and emails, data exfiltration across tenants, tool misuse, jailbreaks of NN-14 guardrails) on every AI-gateway change (P17 provides the suite).

**FR-P24-26 — VAPT and comprehensive audit.** (a) Annual comprehensive cyber-security audit by a **CERT-In empanelled auditor** aligned with CERT-In's Comprehensive Cyber Security Audit Policy Guidelines (25 July 2025: at least annual; after major changes; manual testing beyond tools; CVSS with EPSS and CWE/CVE mapping; final report only after closure and follow-up; auditee data stored only on systems in India; metadata submitted by the auditor to CERT-In within 5 days) [VERIFY against CERT-In original text]; (b) quarterly VAPT of external surface and authenticated web/API; (c) major-release VAPT before any release that materially changes authentication, authorisation, payments/billing, sealed stores, credential vault, public APIs or the AI gateway — the release stays in `ring1` until Critical/High findings are closed. Scope: public site, tenant app, console, delivery console, supervisor and auditor workspaces, APIs (per role), cloud configuration (CIS, IAM, SCPs, KMS, Object Lock, backup account), GitHub organisation configuration, Microsoft 365 tenant of the delivery team (with OH12), AI gateway. Production testing only in a consented, non-destructive window on LawDocs test tenants; a staging-only report says so. Auditor snapshot of the CERT-In empanelled list with hash, rules of engagement, NDA and DPA filed with the engagement. Findings imported into `eng.vulnerabilities`.

**FR-P24-27 — Client-driven audits of LawDocsComply.** Regulated clients must be able to audit LawDocsComply as their technology service provider (RBI IT outsourcing expectations: right to audit for the RE, its auditors and RBI; Ecosystem Spec §4.7 `PROVIDER_ASSURANCE`) [LAW/INTERP: RBI Master Direction on Outsourcing of Information Technology Services, 10 Apr 2023, and successor consolidated directions — VERIFY paragraph references]. P24 provides: the standard information-security questionnaire responses (SIG Lite / CAIQ-style), the sub-processor list, architecture and data-flow diagrams, latest VAPT summary, BCP/DR evidence, policy index and — once issued — SOC 2 reports and ISO certificates, served through the OH14 provider-assurance room under a `PROVIDER_ASSURANCE` grant (no tenant data). Pooled audits (several REs auditing together) are supported by the same room. A client's own VAPT of LawDocsComply follows a rules-of-engagement template and its findings join the platform register.

**FR-P24-28 — Responsible disclosure.** `security.txt` on every domain, a vulnerability disclosure policy with safe harbour and acknowledgement within 3 working days; private bug bounty behind flag `eng.bug_bounty.enabled` = OFF until Board budget approval.

### 4H. Audit readiness of LawDocsComply itself (IS, internal and external audit)

**FR-P24-29 — Evidence collectors** (`eng.control_evidence`, exported to OH14): automated, dated evidence for each control in Appendix Q — e.g., ruleset exports, PR approvals sample, change records with approvals, deployment logs with image digests, access reviews completed, MFA coverage report, joiner-mover-leaver reconciliation (OH10 ↔ Keycloak), break-glass reports, vulnerability SLA report, backup and restore test results, DR drill reports, encryption configuration snapshots, KMS key rotation status, log retention probe (logs ≥ 180 days in India), audit-chain verification results, training completion (security awareness, privacy) from the group LMS, vendor reviews, incident register, risk register, policy approval records. Collectors run on a schedule; each evidence item carries hash, period, collector version and control mapping.

**FR-P24-30 — Audit types supported.** (a) **IS audit** of LawDocsComply's information systems (scope per ISACA/ICAI IS audit practice; the client-facing equivalent for clients is P10); (b) **internal audit** of LawDocsComply's own operations (risk-based plan; findings tracked to closure); (c) **statutory and tax audits** of the operating company (books in the group's accounting system; billing data from `bil` exportable to auditors with s.63 certificate); (d) **certification audits** (SOC 2, ISO); (e) **client audits** (FR-P24-27). The auditor workspace is the OH14 room for (a), (d), (e) and a read-only grant into `ldc-platform` for platform-level records (audit chain, configuration history), never tenant data.

**FR-P24-31 — Access reviews.** Quarterly access review for staff (console, delivery, AWS, GitHub, database break-glass roles, KMS key administrators) with attestations by managers; quarterly tenant-side access review workflow offered to every tenant (SCR-IAM-40): department heads attest their users' roles; unattested users are flagged; results exported as evidence for the tenant's own audits (RBI IT governance expectations for REs) [VERIFY RBI paragraph].

### 4I. Certification readiness (no claims before certificates — NN-19)

**FR-P24-32 — Programme.** Sequence recommended [REC]: (1) readiness assessment against SOC 2 Trust Services Criteria (Security mandatory; Availability and Confidentiality recommended; Processing Integrity for calculation and returns modules; Privacy optional) and ISO/IEC 27001:2022; (2) **SOC 2 Type 1** (design at a point in time) at GA + ~2 months; (3) **ISO/IEC 27001:2022** Stage 1 and Stage 2; (4) **SOC 2 Type 2** with a 6-month first observation window, then annual 12-month windows; (5) **ISO/IEC 27701:2025** (privacy information management — published as a standalone management-system standard in 2025, no longer only an extension of 27001 [VERIFY certification-body transition rules]); (6) **ISO/IEC 42001:2023** (AI management system) once Vidhi features are material to sales; (7) **ISO 22301:2019** (business continuity) for enterprise and bank clients; (8) **PCI DSS v4.0.1 SAQ A** for the hosted/redirect checkout (Razorpay hosted pages or Standard Checkout) — LawDocsComply never stores, processes or transmits card data; under v4.0.1 the SAQ A eligibility criteria require the merchant to confirm the whole site is protected from script-based attacks that could affect the payment page (requirements 6.4.3 and 11.6.1 no longer listed in SAQ A, replaced by this eligibility criterion; effective 31 March 2025) [VERIFY with the acquirer and QSA]; (9) CERT-In audit annually (FR-P24-26); (10) MeitY empanelment of the cloud provider is relied upon for government clients (AWS Mumbai and Hyderabad regions) [VERIFY]. STQC certification only if a government tender requires it.

**FR-P24-33 — Control set and mapping.** Appendix Q §Q.6 maps each product and operational control to SOC 2 criteria (CC1–CC9, A1, C1, PI1, P1–P8), ISO 27001:2022 Annex A (93 controls in 4 themes), ISO 27701, ISO 42001 Annex A, ISO 22301 clauses, PCI DSS SAQ A requirements, CERT-In Directions, DPDP Act/Rules and the RBI vendor expectations clients will ask about. P24 implements the technical controls and evidence; the owner writes the policies (Appendix Q §Q.11 lists 28 policies and procedures with owners); the policy module (P07) hosts them with version control and Board approval records.

**FR-P24-34 — Statement of Applicability and risk register.** The ISMS risk register (assets, threats, vulnerabilities, risk owners, treatment) and the Statement of Applicability live in LawDocsComply's own `LDC_GROUP` tenant (dog-fooding: LawDocsComply uses its own ERM and policy modules for its ISMS) with exports for the certification body.

**FR-P24-35 — Trust centre.** A public trust page (P23) lists, with evidence links from the claims register: data location (India), encryption, sub-processors, security practices, status page, responsible disclosure, and — only when issued — reports and certificates (SOC 2 report available under NDA; ISO certificate number and scope). Until then the page says "We are preparing for SOC 2 and ISO/IEC 27001 audits" — accurate, not "compliant" or "certified".

### 4J. Hardening and performance

**FR-P24-36 — Hardening checklist** (each item has a verification test or evidence):

- Identity: MFA coverage 100% for privileged roles; phishing-resistant MFA for staff; no shared accounts; service accounts with short-lived credentials only; Keycloak admin console reachable only from staff network/device posture.
- Web: TLS 1.2+ (1.3 preferred), HSTS with preload, CSP with nonces (no `unsafe-inline` scripts), `frame-ancestors` restrictions, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, Subresource Integrity for any third-party script; script inventory and change detection on all pages (supports PCI SAQ A eligibility); cookies `__Host-`, Secure, HttpOnly, SameSite.
- API: authz on every route (Semgrep gate), schema validation on every input, rate limits per tenant/user/IP, request size limits, idempotency keys, problem details without stack traces, CORS allow-list.
- Uploads: magic-byte validation, AV scan, macro handling, sandboxed rendering (document previews converted server-side in an isolated container), no direct execution, prompt-injection labelling for AI (P17).
- Cloud: SCPs, least-privilege IAM, IAM Access Analyzer clean, no public buckets, VPC endpoints, egress allow-list, WAF managed rules, GuardDuty and Security Hub findings at zero Critical/High, KMS key policies with separation of key administrators and key users, CloudTrail organisation trail immutable.
- Database: RLS lint green, no superuser application roles, encrypted connections required, audit of DDL, parameter hardening, connection limits, slow-query monitoring.
- Email and DNS: SPF, DKIM, DMARC `p=reject` after monitoring, MTA-STS, TLS-RPT, DNSSEC, CAA records, BIMI optional.
- Secrets: Secrets Manager with rotation; no secrets in logs (NN-32), environment variables, images or front-end bundles.
- Logging: CERT-In 180-day log retention in India; NTP synchronisation; security event monitoring and alerting with on-call.

**FR-P24-37 — Performance and resilience tests.** k6 (or Gatling) suites from Appendix V: (a) load — 2,000 concurrent users across 500 tenants, p95 within P00 budgets; (b) peak — quarter-end board-pack generation and return-package generation for 200 tenants within 30 minutes; (c) bulk — Excel import of 5,000-row question sheets in ≤ 2 minutes with full validation; folder intake of 10,000 files in ≤ 30 minutes; export of a 50 GB tenant package resumable; (d) soak — 24 hours at 60% peak without memory growth; (e) chaos — loss of an AZ, of Redis, of OpenSearch (fallback to PostgreSQL FTS), of the AI provider (deterministic fallbacks, P17), of an integration (queue and retry). Capacity plan and cost model (FinOps) reviewed monthly.

### 4K. Incident management and regulatory clocks

**FR-P24-38 — Incident process.** Severity Sev-1 (outage, data breach, integrity compromise) to Sev-4; incident commander role; status page updates within 30 minutes for Sev-1/2; customer communications templates; post-incident review within 5 working days with corrective actions tracked to closure. Integrated with OH13 incident register.

**FR-P24-39 — Regulatory and contractual clocks.** (a) **CERT-In**: report specified cyber incidents to CERT-In within 6 hours of noticing (Directions of 28 April 2022) — LawDocsComply's own obligation as a body corporate/service provider; (b) **client REs**: notify affected regulated clients within ≤ 2 hours of detection so they can meet their own 6-hour reporting to RBI/CERT-In and contractual duties (Ecosystem Spec §3.8 provider incident to RE ≤ 2 h; client contract), with a structured incident notice (what, when, data classes, tenants, containment, contact) delivered through email, phone tree and the tenant's Updates feed; (c) **DPDP**: for personal-data breaches where LawDocsComply is processor, inform the client (data fiduciary) without delay so it can intimate the Data Protection Board and affected principals and file the detailed report within 72 hours under the DPDP Rules 2025 (core obligations from 13 May 2027; build now) [VERIFY rule numbering]; where LawDocsComply is fiduciary (its own users, leads, staff), it intimates the Board and principals itself; (d) **SEBI/IRDAI/IFSCA-regulated clients** may have their own reporting clocks under CSCRF and sector rules — the client's P12 module tracks them; LawDocsComply's notice gives them what they need. Clocks start at detection, are owned by named people and escalate automatically.

---

## 5. Workflows and state machines

### 5.1 Change record — as FR-P24-07 (Appendix A §A.9).
### 5.2 Release

`PLANNED → CUT (tag, release branch) → STAGING_VERIFIED (e2e-full, DAST, golden exports, performance smoke) → RING0 → RING1 (24 h, no SLO burn) → RING2 → DONE`; any stage → `HALTED` (flag off / rollback) → `FIXED` → resume. Release record links change records, SBOM, signatures, notes; emits `ReleasePublished` to OH13 (version, change ids, SBOM hash, signature digest, release-notes ref, regulatory-impact flag).

### 5.3 Vulnerability

`NEW → TRIAGED (severity, owner, SLA due) → IN_PROGRESS → FIXED (PR merged) → VERIFIED (scan/retest) → CLOSED`; `TRIAGED → RISK_ACCEPTED (expiry ≤ 90 d) → REOPENED on expiry`; `FALSE_POSITIVE` (with reviewer). SLA breach → escalation to CTO and security lead; Critical breach → Board committee notification.

### 5.4 Incident

`DETECTED → TRIAGED (severity, clocks started) → CONTAINED → ERADICATED → RECOVERED → NOTIFICATIONS_COMPLETE (CERT-In, clients, DPDP, others) → PIR_DONE → CLOSED`. Clocks visible on the incident record with countdowns.

### 5.5 VAPT engagement

`PLANNED → ROE_SIGNED → FIELDWORK → DRAFT_REPORT → REMEDIATION → RETEST → CLOSED`; entry to `FIELDWORK` needs empanelment snapshot hash, scope document, time-limited test accounts; `CLOSED` needs retest report, closure memo, CERT-In metadata submission proof where applicable.

### 5.6 Go-live

`READINESS_REVIEW → GO_NO_GO (signatures) → CUTOVER → HYPERCARE (14 days) → STEADY_STATE`; no-go returns to readiness with the blocking items.

---

## 6. Screens and UX

LawDocsComply-specific engineering screens live in the console; group-wide CAB, vulnerability and certification consoles live in OH13/OH14.

| Screen ID | Name | Path | Roles |
|---|---|---|---|
| SCR-ENG-01 | Release calendar and rings | console › Engineering › Releases | release manager, CTO, product owner |
| SCR-ENG-02 | Release detail (changes, SBOM, signatures, notes, ring status, halt button) | same | same |
| SCR-ENG-03 | Change records (LDC view; CAB in OH13) | console › Engineering › Changes | engineering |
| SCR-ENG-04 | Migration monitor (backfills, progress, verification) | console › Engineering › Migrations | SRE, tech lead |
| SCR-ENG-05 | Golden export diff viewer | console › Engineering › Export goldens | tech lead, data owner |
| SCR-ENG-06 | Backups and restore tests | console › Engineering › Resilience | SRE, security |
| SCR-ENG-07 | DR drills | same | SRE, CTO |
| SCR-ENG-08 | Vulnerabilities (LDC filter of OH13.3) | console › Security › Vulnerabilities | security, engineering |
| SCR-ENG-09 | VAPT engagements | console › Security › VAPT | security |
| SCR-ENG-10 | Control evidence status (per framework, per control, freshness) | console › Assurance › Evidence | security, plt_auditor |
| SCR-ENG-11 | Incidents and clocks | console › Security › Incidents | incident commander, security |
| SCR-ENG-12 | Go-live checklist | console › Assurance › Go-live | CTO, CISO, CS, product owner |
| SCR-ENG-20 | What's new (tenant) | app › Help › What's new | all tenant users |
| SCR-ENG-21 | Release preferences (early access ring, sandbox) | app › Settings › Platform & releases | ten_admin |
| SCR-ENG-22 | Security and trust (tenant view: data location, sub-processors, latest summaries, request provider-assurance access) | app › Settings › Security & trust | ten_admin, ten_kmp:CISO |

---

## 7. Backend design

### 7.1 Modules touched

`eng` (owner), `core` (audit, flags), `iam` (staff grants, access reviews), `xpt` (golden exports), `chg` (Updates feed entries for releases and incidents), `int` (OH13/OH14 events).

### 7.2 Tables

`eng.releases`, `eng.release_changes`, `eng.release_rings`, `eng.change_records`, `eng.change_approvals` (mirror of OH13 approvals), `eng.freeze_windows`, `eng.migrations_runs`, `eng.golden_exports`, `eng.vulnerabilities`, `eng.risk_acceptances`, `eng.vapt_engagements`, `eng.vapt_findings`, `eng.backup_policies`, `eng.restore_tests`, `eng.dr_drills`, `eng.incidents`, `eng.incident_clocks`, `eng.incident_notifications`, `eng.control_evidence`, `eng.controls` (catalogue mirror from OH14 with LDC mapping), `eng.access_reviews`, `eng.eos_register` (end-of-support), `eng.service_catalogue` (tiers, RPO/RTO).

### 7.3 APIs (staff-only, console)

`GET/POST /v1/eng/releases`, `POST /v1/eng/releases/{id}:promote|halt`; `GET /v1/eng/changes`; `POST /v1/eng/incidents`, `POST /v1/eng/incidents/{id}/notifications`; `GET /v1/eng/evidence?framework=SOC2&control=CC6.1`; tenant-facing: `GET /v1/trust/summary`, `POST /v1/trust/provider-assurance-requests` (creates the request that OH14 fulfils).

### 7.4 Events

Ecosystem/OH: `ReleasePublished` (to OH13), consumes `ChangeApproved` (from OH13), emits evidence items to OH14 (`ControlEvidenceRecorded`), incidents to OH13 (counts and classes only), `ExternalAccessGranted/Used/Revoked` for `PROVIDER_ASSURANCE` handled by OH14. Internal: `in.lawdocscomply.eng.ReleasePromoted.v1`, `…ReleaseHalted.v1`, `…VulnerabilitySlaBreached.v1`, `…RestoreTestFailed.v1`, `…IncidentDeclared.v1`, `…IncidentClockBreached.v1`.

### 7.5 Jobs

`ReleaseApprovalWorkflow` (compensating control), `RulesetDriftExport` (nightly), `GoldenExportRun` (each release), `RestoreTestWorkflow` (weekly), `EvidenceCollectors` (schedules per control), `VulnSlaMonitor` (hourly), `LogRetentionProbe` (monthly), `EosReminder` (monthly), `AccessReviewCampaign` (quarterly), `IncidentClockMonitor` (minutely during incidents).

---

## 8. Integrations

| Port | Adapter | Notes |
|---|---|---|
| `SCM_PORT` | GitHub REST/GraphQL (rulesets, alerts, environments, audit log) | Read-mostly |
| `OH_ENG_PORT` | Operations Hub OH13 (changes, CAB, vulnerabilities, incidents, releases) and OH14 (evidence, provider-assurance room) via Ecosystem Spec contracts | No OH credential acts inside tenants |
| `STATUS_PORT` | Status page (self-hosted or vendor with India data handling) | Public |
| `PAGER_PORT` | On-call paging (vendor) | Staff contacts only |
| `SCANNER_PORTS` | CodeQL/Semgrep, Dependabot, Trivy, Checkov, ZAP, Schemathesis | CI |
| `CLOUD_SECURITY_PORT` | AWS Security Hub, GuardDuty, Inspector, Config | Findings to `eng.vulnerabilities` |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `eng.branch.max_age_days` | G | 2 | 1–10 | CTO |
| `eng.release.train_day_time` | G | Tue 22:00 IST | — | release manager |
| `eng.release.ring1_soak_hours` | G | 24 | 4–168 | release manager |
| `eng.notice.regulatory_impact_working_days` | G | 5 | ≥ 5 (L floor) | release manager |
| `eng.api.deprecation_months` | G | 6 | ≥ 6 (L floor) | CTO |
| `eng.vuln.sla.critical_hours` | L | 72 | — | — |
| `eng.vuln.sla.high_days` | L | 7 | — | — |
| `eng.vuln.sla.medium_days` | L | 30 | — | — |
| `eng.vuln.sla.low_days` | L | 90 | — | — |
| `eng.vuln.risk_acceptance_max_days` | L | 90 | — | — |
| `eng.backup.pitr_days` | G | 35 | ≥ 35 | SRE |
| `eng.restore_test.frequency_days` | G | 7 | ≤ 7 | SRE |
| `eng.dr.drill_months` | G | 6 | ≤ 6 | CTO |
| `eng.logs.retention_days` | G | 400 | ≥ 180 (L floor, CERT-In) | security |
| `eng.incident.client_notice_hours` | L | 2 | — | — |
| `eng.bug_bounty.enabled` | G (approver: Board) | false | — | Board |
| `eng.vapt.production_window.enabled` | G | false | — | security lead with CAB |
| `ten.release.early_access` | T | false | — | ten_admin |

---

## 10. Security, privacy and audit

- Separation of duties: developers have no standing production data access; production database access only through break-glass with tenant notification (NN-30); deployers cannot approve their own change; KMS key administrators are not data users.
- All engineering records are retained ≥ 8 years (change records and release evidence support clients' audits of historical records).
- Evidence collectors never copy tenant data; evidence naming a tenant is shared only with that tenant.
- AI-assisted code review or generation tools used by engineers are recorded as sub-processors if they receive code; no production data or secrets are sent to them (policy and DLP rule).

---

## 11. AI touchpoints and guardrails

- AI may draft release notes and PIR summaries from structured records (labelled drafts, human-approved).
- AI may summarise vulnerability scanner output for triage; it never sets severity or closes a finding.
- AI-gateway changes are `REGULATED` changes with the P17 red-team suite as a required check; model or prompt changes follow P17's model change management (evaluation set pass thresholds) and are listed in release notes as "AI behaviour changes".

---

## 12. Acceptance criteria (`tests/acceptance/p24/*.feature`)

```gherkin
Feature: Production deployments are approved
  Scenario: Deployment without ChangeApproved is refused
    Given release 2027.01.2 has no ChangeApproved event for change CHG-118
    When the deploy pipeline targets production
    Then the deployment is refused with LDC-ENG-001 and an incident is opened

Feature: Releases preserve client data and folder structure
  Scenario: Golden export detects an unintended folder rename
    Given the previous release's golden export for demo tenant "nbfc-ml"
    When a pull request renames the "Policies & Procedures" export folder without bumping LDC-EXPORT version
    Then ci/export-contract fails with a path diff
  Scenario: Release does not alter published content
    Given published content snapshot S before migration rehearsal
    When the release migrations run
    Then content tables equal snapshot S

Feature: Expand-contract
  Scenario: Destructive migration in the same release is rejected
    Given a migration drops column cmp.compliance_instances.old_status
    And code in the same release still references it in a previous version path
    When ci/migrations runs
    Then it fails with "contract step must ship after verification"

Feature: Recoverability
  Scenario: Weekly restore test
    When RestoreTestWorkflow restores the latest ldc_core snapshot to the isolated account
    Then audit-chain verification passes for all chains
    And sampled export comparison matches
    And restore time is recorded below the RTO

Feature: Vulnerability SLAs
  Scenario: High vulnerability breaches SLA
    Given a High vulnerability triaged 8 days ago and not fixed
    When VulnSlaMonitor runs
    Then VulnerabilitySlaBreached is emitted and CTO and security lead are notified

Feature: Incident clocks
  Scenario: Client REs notified within 2 hours
    Given a Sev-1 security incident affecting 3 RE tenants is declared at 10:00 IST
    Then client notices are due by 12:00 IST and CERT-In report by 16:00 IST
    And the incident record shows countdowns and owners

Feature: No certification claims
  Scenario: Trust centre without a certificate
    Given no ISO 27001 certificate is recorded in the claims register
    When the trust page renders
    Then it does not contain the words "ISO 27001 certified"

Feature: PCI scope
  Scenario: Card data never touches LawDocsComply
    When a payment is made through the hosted checkout
    Then no request to LawDocsComply servers contains a PAN pattern
    And the payment page's scripts match the approved script inventory
```

NN tests: `NN-03_release_does_not_touch_content`, `NN-10_*`, `NN-11_*`, `NN-16_no_card_data`, `NN-19_trust_claims`, `NN-24_*`, `NN-30_*`, `NN-32_*`.

---

## 13. Deliverables and exit gate

### 13.1 Governance track (before P05 ends)
- [ ] GitHub plan decision recorded; rulesets, CODEOWNERS, required checks, merge queue, signed commits live on all repositories; drift export running.
- [ ] Change classes, change record, OH13 integration (`ChangeApproved` gate, `ReleasePublished`), freeze windows, release trains and rings in operation.
- [ ] Expand-contract checker, golden export test, content-untouched test as required checks.
- [ ] Vulnerability intake and SLA monitoring live; EOS register populated.

### 13.2 Go-live track (before GA)
- [ ] Production on AWS ap-south-1 with DR in ap-south-2; RPO/RTO verified by drill.
- [ ] Restore tests green for 4 consecutive weeks.
- [ ] Hardening checklist 100% with evidence.
- [ ] CERT-In empanelled VAPT closed (Critical/High = 0) with retest; DAST/API fuzzing clean of High.
- [ ] Performance suites within budgets; chaos tests passed with documented fallbacks.
- [ ] Incident process rehearsed (tabletop) including CERT-In 6-hour and client 2-hour clocks.
- [ ] Evidence collectors running for ≥ 80% of Appendix Q controls; policy set approved by the Board; readiness assessment completed; SOC 2 Type 1 engagement scheduled.
- [ ] Trust centre content approved through the claims register.
- [ ] Go-live checklist signed (CTO, CISO, Company Secretary, product owner); hypercare roster.

### 13.3 Re-run for later phases
Each phase released after GA runs: threat model update, VAPT scope delta (major-release VAPT if applicable), performance test of its heavy paths, export-mapping and golden export update, evidence collector additions, release notes and tenant notice, and the §13.2 items relevant to its scope. Deferred items are recorded in `docs/phases/P24-deferred.md` and close at the exit of the phase that builds them.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P24-01 | GitHub Enterprise Cloud + Secret Protection + Code Security licensing and price | Budget | CTO / Board | Compensating `ReleaseApprovalWorkflow` and OSS scanners (RISK-ENG-001) |
| OI-P24-02 | CERT-In Comprehensive Cyber Security Audit Policy Guidelines (25 Jul 2025) — original text for scope, frequency and reporting duties | Secondary summary used | Security lead | Apply annual audit + major-change audit; auditor submits metadata |
| OI-P24-03 | RBI IT outsourcing directions paragraphs on service-provider audit rights as consolidated in 2025 | Consolidation renumbered paragraphs | Compliance | Contractual audit-rights clause in client MSA; provider-assurance room |
| OI-P24-04 | PCI DSS v4.0.1 SAQ A eligibility confirmation with the acquirer (Razorpay) and QSA | Merchant-level validation rules | CFO / security | Hosted checkout; script inventory and monitoring anyway |
| OI-P24-05 | ISO/IEC 27701:2025 certification and transition arrangements | Certification-body rules | CS | Plan 27701 after 27001 |
| OI-P24-06 | DPDP Rules 2025 breach-report rule number and commencement (13 May 2027) | Phased commencement | DPO | Build the 72-hour workflow now |
| OI-P24-07 | Status page and paging vendors' data residency | Vendor | SRE | Self-hosted status page |
| OI-P24-08 | Freeze-window calendar for clients' statutory seasons each year | Calendar changes annually | Compliance reviewer | Default windows in FR-P24-08 |
| OI-P24-09 | RFC numbers for `Deprecation`/`Sunset` headers | Standards status | Tech lead | Use `Sunset` (RFC 8594) and document deprecation in changelog |
| OI-P24-10 | MeitY empanelment status of chosen cloud regions for government clients | Tender-specific | CS | Disclose on request |

---

## 15. Sources (checked 25 October 2026 unless stated)

1. Infrabyx Operations Hub Master Prompt v1.0 — OH13 (repository register, release calendar, freeze windows, change classes and states, CAB, emergency changes, vulnerability SLAs) and OH14 (certification readiness, provider-assurance room).
2. Infrabyx Ecosystem Integration Specification v1.1 — §3.3 (compatibility BACKWARD), §3.8 (service levels; provider incident to RE ≤ 2 h), §4.7 (`PROVIDER_ASSURANCE` grants).
3. Equator Build Prompt Pack v3.1 — Appendix AE (GitHub plan, branch model, rulesets, RPO/RTO tiers, backup policy, VAPT programme) — pattern reference.
4. CERT-In, Directions under sub-section (6) of section 70B of the IT Act 2000 (28 Apr 2022) — 6-hour reporting, 180-day logs in India, NTP synchronisation — https://www.cert-in.org.in/
5. CERT-In, Comprehensive Cyber Security Audit Policy Guidelines (25 Jul 2025) — summary: https://www.azbpartners.com/bank/strengthening-indias-cyber-defence-cert-ins-new-cyber-security-audit-guidelines-decoded/ [VERIFY with CERT-In text]
6. PCI Security Standards Council, PCI DSS v4.0.1 and SAQ A (revised January 2025) — summary: https://www.akamai.com/blog/security/pci-dss-v4-0-1-changes-qualify-saq-a [VERIFY with PCI SSC documents]
7. ISO/IEC 27701:2025 publication — https://www.kiwa.com/en/nl/about-kiwa/news/isoiec-277012025-published-updated-privacy-standard-offers-organizations-more-guidance
8. AICPA Trust Services Criteria (2017, revised points of focus 2022); ISO/IEC 27001:2022; ISO/IEC 42001:2023; ISO 22301:2019 — reference.
9. OWASP ASVS 5.0 (released 2025) — https://owasp.org/www-project-application-security-verification-standard/ [VERIFY chapter mapping]
10. RFC 9116 (security.txt), RFC 8594 (Sunset header).
11. Companies Act 2013 s.128(5); DPDP Act 2023 and DPDP Rules 2025.

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-34, NN-45; X-05, X-22; track the master §19 change requests and companion addenda to closure**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

