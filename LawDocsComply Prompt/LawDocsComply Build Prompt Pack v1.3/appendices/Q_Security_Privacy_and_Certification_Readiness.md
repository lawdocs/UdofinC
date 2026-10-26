# Appendix Q — Security, Privacy and Certification Readiness

> Binding on all phases. Owner: stream S11. Phases P00, P01 and P24 implement the platform controls; every functional phase applies §Q.3 (data handling), §Q.5 (logging), §Q.15 (secure SDLC and AI security) and adds its controls to §Q.6. LawDocsComply makes **no certification, attestation or regulator-endorsement claim** until the certificate or report exists and is recorded in the claims register (NN-19).

> **v1.1 changes (25 October 2026)**
> - Region-cell residency controls SC-60–SC-65 and data-transfer rules by law (§Q.18.1–Q.18.2; D-42, D-46)
> - Agentic-AI threat model additions (§Q.18.3; NN-41, NN-50–NN-52)
> - ISO/IEC 42001 readiness map, policy-set and client-assurance additions (§Q.18.4–Q.18.6; D-38)

---

## Q.0 Purpose and scope

LawDocsComply holds some of the most sensitive records a regulated entity has: board papers, supervisory correspondence, compliance failures, internal audit findings, POSH complaints, payroll, credentials to regulatory portals, and returns data drawn from loan books. Clients will buy it only if they can show their regulators, auditors and boards that the vendor is controlled. This appendix sets the security and privacy architecture, the control set mapped to the frameworks clients and auditors ask about, the policy set the owner must write, and the path to SOC 2 and ISO certifications.

Scope: the LawDocsComply platform (all apps, APIs, workers, data stores, integrations, AI gateway), the delivery operations of the LawDocs team working in client tenants, and the supporting cloud, source-control and workplace environments. The Operations Hub, Finbyx, Udofin and Equator have their own controls; interfaces with them are in scope.

---

## Q.1 Security principles

1. **Tenant isolation first** — RLS as the database wall, Cerbos as the room-level control, tenant-scoped keys, indices, caches, object prefixes and workflow IDs (NN-01).
2. **Tamper-evident history** — append-only hash-chained ledger, daily signed anchors, Correction Entries instead of edits (NN-02, D-02).
3. **Least privilege and separation of duties** — server-side authorisation on every path; maker ≠ checker; developers without standing production data access; break-glass visible to the tenant (NN-05, NN-30).
4. **Encryption everywhere** — TLS 1.2+ (1.3 preferred) in transit; AES-256 at rest; field-level envelope encryption for SPI, HR, SEALED, CREDENTIAL and REGULATOR_CONFIDENTIAL classes.
5. **India residency** — tenant data, backups, logs and sub-processing in India (NN-24); exceptions recorded with legal basis.
6. **Minimise identity data** — no Aadhaar numbers, no bureau pulls, no card data (NN-12, NN-16).
7. **Assume compromise** — monitoring, immutable logs, backups in a separate account, tested restores, rehearsed incident response.
8. **AI is a governed component** — AI never acts without a human where NN-14 requires; retrieval is permission-filtered; prompts and outputs are logged; no training on tenant data (NN-14, NN-15).
9. **Evidence by design** — every control produces dated, hashed evidence automatically (P24 §4H).
10. **Truth in claims** — security and certification statements only with evidence (NN-19).

---

## Q.2 Threat model

Method: STRIDE per component plus abuse cases; OWASP ASVS 5.0 Level 2 as the default verification level for all apps and Level 3 for authentication, session, access control, cryptography and audit logging of the console, the credential vault, supervisor workspace and sealed workspaces [VERIFY chapter numbering of ASVS 5.0]; OWASP Top 10 for LLM Applications for the AI gateway. Each phase updates `docs/security/threat-model-<module>.md` using the template below.

### Q.2.1 Top threats and mitigations

| # | Threat | Asset | Mitigations | Residual / test |
|---|---|---|---|---|
| T1 | Cross-tenant data leakage via missing filter, cache key, search index or object path | All tenant data | RLS with FORCE; fail-closed context; tenant in every cache/index/object key; Cerbos query plans; `NN-01_*` generated tests over every table; search adapter enforces tenant filter | Pen-test cross-tenant cases each VAPT |
| T2 | Malicious or careless super admin alters client records | Compliance history, evidence | No in-place edits; Correction Entries dual-approved, tenant-visible; anchors; break-glass with tenant notice; console on separate origin with AAL3 | Quarterly review of corrections and break-glass by security lead and `plt_auditor` |
| T3 | Insider DBA tampers with database directly | Ledger, history | Ledger triggers; hash chain verification; signed anchors in Object Lock and optional TSA; DBA access only via break-glass with session recording; separate backup account | Chain verify daily; anchors downloadable by tenants |
| T4 | Account takeover of a client admin or checker | Tenant configuration, approvals | Passkeys/TOTP; no SMS as second factor for privileged roles; step-up; session limits; anomaly alerts; admin changes notify all admins | Credential-stuffing tests |
| T5 | LawDocs RM misuses delivery access (data exfiltration, false approvals) | Client data | Delivery grants approved by client; LawDocs cannot be sole checker; export only via deliverables; vault reveal per credential with MFA; activity reports to client; OH internal controls (OH11) | Monthly delivery-access report to client |
| T6 | Theft of regulatory-portal credentials from the vault | RBI/MCA/GST/CIC portal access | Envelope encryption with dedicated vault key per tenant; client-owned entries; per-credential grants; AAL2/AAL3 reveal; reveal logged and notified to owner; no bulk export; rotation reminders; RBI portal entries client-only by default; clipboard auto-clear; reveal watermark | Pen-test vault; red-team exercise |
| T7 | Prompt injection through uploaded documents, emails or WhatsApp screenshots causing data exfiltration or unauthorised actions | Tenant data, actions | Retrieval filtered by the user's permissions; untrusted-content labelling; tool allow-lists; no external send without human action (NN-14); output filters; AI red-team suite in CI | P17 evaluation suite thresholds |
| T8 | Malicious file upload (malware, macro, polyglot, zip bomb) | Users, workers | Quarantine bucket; magic-byte validation; AV; macro policy; isolated converters; size and decompression limits | Fuzzing of converters |
| T9 | Supply-chain compromise (dependency, CI action, image) | Codebase, production | Pinned actions by SHA; signed images; SBOM; provenance; dependency review; Dependabot; private registry mirror | SLSA target level 3 |
| T10 | Supervisor credential misuse or over-collection | Client data | Named accounts on authority domains; read-only replicas; masking default; watermarking; anomaly alerts; 90-day cap | Daily activity report to CCO |
| T11 | Webhook/event spoofing from ecosystem or third parties | Integrity of imported data | RFC 9421 signatures; mTLS; replay protection; schema validation; idempotency; data-class ceilings | Contract tests |
| T12 | Ransomware or cloud account compromise | Availability, integrity | SCPs; separate backup account with vault lock; Object Lock; immutable logs; tested restores; least-privilege IAM; GuardDuty | DR drills |
| T13 | Payment fraud and card-data exposure | Revenue, PCI scope | Hosted/tokenised checkout; signed webhooks; idempotent order state; script inventory on payment-referring pages; no card data on servers | PCI SAQ A self-assessment |
| T14 | Data-scraping abuse of public KYB lookup or health check | Third-party data, reputation | Verified email, rate limits, bot challenge, minimal fields | Abuse monitoring |
| T15 | POSH/whistle-blower confidentiality breach | Complainants, respondents | Sealed database and keys; IC-only access; no analytics/AI; minimum necessary disclosure; access log reviewed by presiding officer | Access review per matter |
| T16 | Leakage of board-confidential or regulator-confidential papers via sharing links or exports | Board packs, inspection reports | Confidentiality labels; sharing disabled by default for BOARD_ONLY/REGULATOR_CONFIDENTIAL; watermarked viewer; download controls; expiry on links | DLP checks on export |
| T17 | Misleading compliance output (wrong due date, wrong applicability, wrong ratio) leading to penalties | Client compliance | Deterministic engines with golden tests; REGULATED change class; citations; maker-checker on content; "explain why applicable"; Processing Integrity controls | Golden-case suites |

### Q.2.2 Abuse cases to test

Tenant admin grants themselves checker on their own items (SoD block); a maker back-dates a date of compliance (allowed only as user-entered value with recorded time; post-approval change only via correction with checker); an RM approves their own made item through a second identity (identity uniqueness checks; person-level SoD across realms); a supervisor tries to export full PII (blocked by grant level); a user asks Vidhi to email a board paper to an external address (blocked; draft only); bulk export by a departing employee (thresholds, step-up, alerts to admin).

---

## Q.3 Data classification and handling

| Class | Examples in LDC | At rest | In logs | Exports | AI | Sharing links |
|---|---|---|---|---|---|---|
| PUBLIC | Published regulatory text, public website | Standard | Allowed | Allowed | Allowed | Allowed |
| INTERNAL | Settings, aggregates, task titles | Standard | IDs only | Allowed | Allowed | Within tenant |
| CONFIDENTIAL | Compliance status, findings, risk scores, commercial terms | Standard + RLS | IDs only | Allowed with audit | Within permissions | Tenant policy |
| PII | Names, emails, mobiles of users, directors, employees | Field encryption for contact values; masking | Never | Allowed, logged | Within permissions; minimised | Tenant policy |
| SPI | Clear PAN, bank accounts, KYC images | Field encryption, tenant key | Never | Restricted folder; step-up | Never by default; tenant opt-in for specific tools | Disabled |
| FINANCIAL | Balance sheets, loan data from Finbyx, return data | Standard + RLS; encrypted backups | Never values | Allowed, logged | Within permissions | Tenant policy |
| LEGAL | Litigation, legal opinions, privileged advice | Standard; privileged flag | Never content | Restricted if privileged | Within permissions; privileged excluded by default | Restricted |
| HR | Employee master, payroll, attendance, appraisal | Field encryption for pay and bank; HR key | Never | Restricted `HR` folder | Only HR roles' Vidhi; never training | Disabled |
| SEALED | POSH matters, whistle-blower, sealed complainant identity, health HR data | Separate database, separate keys | Never | Separate sealed export with IC approval | Never | Disabled |
| BOARD_CONFIDENTIAL | Board/committee papers flagged confidential, unpublished price-sensitive information (UPSI) | Document encryption with board key | Never | Board-pack export only; watermark | Within board/committee permissions; tenant opt-in | Watermarked viewer only |
| REGULATOR_CONFIDENTIAL | Inspection reports, risk-assessment reports, MAPs, supervisory letters | Field/document encryption; access list | Never | Restricted folder | Off by default; tenant opt-in per document | Disabled |
| LEGAL_PRIVILEGED *(v1.1, X1; P26)* | Communications with advocates and counsel opinions protected by professional communication privilege (Bharatiya Sakshya Adhiniyam 2023 ss.132–134 [VERIFY section numbers]); matter folders `06 Counsel Opinions (Privileged)` and `10 Internal Notes (Privileged)` | Document encryption with a separate legal key (as BOARD_CONFIDENTIAL); access list of GC, `ten_legal_user` and assigned `ext_counsel` | Never content | Restricted `26 Legal Matters, Contracts and Licences/…/Privileged` sub-folder; step-up; excluded from partial exports unless GC approves | L0 by default (VA-16 only if the GC opts in for a matter); never training | Disabled; never included in delivery, auditor or supervisor grants unless the GC grants that document |
| CREDENTIAL | Portal passwords, API secrets, DSC PINs (never stored — see §Q.4.4) | Vault, per-tenant vault key | Never | Never (metadata only) | Never | Never |

UPSI note: listed clients' board papers may contain unpublished price-sensitive information under SEBI (Prohibition of Insider Trading) Regulations 2015; the platform supports the structured digital database requirement of Reg 3(5) by logging who received UPSI and when (P06) and keeps UPSI documents in BOARD_CONFIDENTIAL with access logs [VERIFY regulation reference].

---

## Q.4 Cryptography and key management

### Q.4.1 Key hierarchy

AWS KMS (FIPS 140-2/140-3 validated HSMs [VERIFY current validation level]) in ap-south-1 with multi-Region replicas in ap-south-2 for DR. Customer-managed keys per environment and data class: `documents`, `evidence`, `pii-field`, `spi-field`, `hr-field`, `legal`, `board`, `regulator-confidential`, `sealed` (separate key policy; usable only by the sealed service role), `vault-kek` (credential vault key-encryption key), `audit-anchor` (asymmetric ECC_NIST_P256 signing), `backup` (backup account), `export-signing` (package manifest signing). Per-tenant data keys derived under the class keys; tenants with `dedicated_key = true` get their own CMKs; BYOK (customer-supplied key material or customer-managed key in the customer's AWS account via cross-account grant) available for enterprise tier (P19), with the documented consequence that revoking the key makes data unreadable.

### Q.4.2 Rotation and custody

Automatic annual rotation for symmetric CMKs; data keys cached ≤ 5 minutes / 1,000 messages; key administrators (SRE + security) are not key users; key policy changes require two-person approval and are alerted; quarterly key inventory review; TLS certificates via ACM with automated renewal; ecosystem mTLS certificates ≤ 397 days with automated rotation (Ecosystem Spec §3.6); signing keys for RFC 9421 in KMS with JWKS publication.

### Q.4.3 Hashing and signatures

SHA-256 for content integrity, chains and manifests; HMAC-SHA-256 with per-tenant keys for blind indices; Argon2id for passwords (Keycloak); ECDSA P-256 for anchors and export manifests; detached JWS (RFC 7515/7797) for documents travelling between products; PAdES for PDF signatures applied by eSign providers; BSA 2023 s.63(4) certificate generated for exports (Part A by the tenant's authorised person, Part B by LawDocsComply as the system operator) [VERIFY form under BSA 2023 Schedule].

### Q.4.4 Credential vault design (D-04, NN-17; built in P22)

- Storage in `ldc_sealed` (or a dedicated vault schema in it): each credential entry = metadata (portal, user ID, owner person, legal entity, purpose, DSC holder name if any, last rotated, rotation interval, MFA method on the portal, recovery contact) + secret ciphertext encrypted with a per-entry data key wrapped by the tenant vault key under `vault-kek`.
- **Never stored:** DSC PINs/tokens and private keys (DSCs stay on hardware tokens held by the named signatory), OTP seeds of the client's officers, Aadhaar-linked credentials of individuals. The vault holds passwords and API keys only.
- Ownership: the client admin (or designated credential owner) creates and owns entries; access is granted per entry to named persons (tenant users or delivery staff), optionally time-boxed; reveal requires AAL2 with `auth_time` ≤ 5 minutes (AAL3 for RBI CIMS/DAKSH/PRAVAAH entries), shows the secret for 30 seconds with copy-to-clipboard that clears after 30 seconds, watermarks the reveal view, and notifies the owner; every reveal writes `core.access_log` with purpose.
- RBI portal entries default to `client_only = true` with the warning: "RBI issues portal credentials to named officers of your organisation. Sharing them with a service provider may breach the portal's terms and your IT outsourcing obligations. Prefer creating a separate user for the service provider where the portal allows it." The client may override per entry with a recorded reason [INTERP; VERIFY portal terms].
- Rotation: reminders at the interval; when delivery staff change the password while working, they record it immediately (an unsaved change after reveal triggers a follow-up task); a "credential changed" event notifies the owner.
- Break-glass cannot reveal vault secrets; platform staff cannot decrypt vault entries (key policy denies platform roles `Decrypt` on `vault-kek` grants except through the delivery-reveal path with a valid per-entry grant).
- Export: metadata only; secrets never exported, never sent to AI, never logged.

---

## Q.5 Logging, monitoring and retention

| Log | Content | Retention | Location |
|---|---|---|---|
| Audit ledger (`core.audit_events`) | Material actions (P00 FR-P00-30) | ≥ 8 years (tenant may extend) | Database + Object Lock archive, India |
| Access log (`core.access_log`) | Sensitive reads, reveals, exports | ≥ 8 years | Same |
| Application logs | Structured, PII-scrubbed | 400 days (≥ 180 days floor, CERT-In) | India log store |
| Infrastructure logs | CloudTrail, VPC flow logs, WAF, ALB, Config | 400 days hot/warm; CloudTrail archive 8 years | `ldc-log-archive` with Object Lock |
| Identity logs | Keycloak events, login, MFA, step-up | 400 days | India log store |
| Security monitoring | GuardDuty, Security Hub, Inspector findings | 400 days | Security account |
| AI logs | Prompt, model, version, retrieval sources, tool calls, outputs, approvals (P17) | Tenant retention (default 2 years; content subject to tenant deletion) | India; tenant-scoped |
| Source control | GitHub audit log streaming | 400 days | Log archive |

Time synchronisation: NTP sources of NIC/NPL or traceable to them (CERT-In Directions item (i)). Alerting: authentication anomalies, privilege changes, break-glass, chain verification failure, vault reveal spikes, supervisor anomalies, export spikes, WAF blocks surge, GuardDuty High, KMS policy change, CloudTrail stop attempts. On-call with escalation.

---

## Q.6 Control set and framework mapping

Legend: SOC 2 TSC (CC = Common Criteria, A = Availability, C = Confidentiality, PI = Processing Integrity, P = Privacy); ISO/IEC 27001:2022 Annex A control numbers; 27701 = ISO/IEC 27701 privacy controls; 42001 = ISO/IEC 42001 Annex A; 22301 = ISO 22301 clauses; PCI = PCI DSS v4.0.1 SAQ A; CERT = CERT-In Directions 2022 / audit guidelines 2025; DPDP = DPDP Act 2023 / Rules 2025. Mapping references are indicative and verified by the readiness assessor [VERIFY].

| ID | Control | Implementation (phase) | SOC 2 | ISO 27001:2022 | Other | Evidence (automated unless noted) |
|---|---|---|---|---|---|---|
| SC-01 | Information security policy set approved and reviewed annually | Owner; P07 hosts | CC1.1, CC5.3 | 5.1 | 27701, 42001 | Policy versions, Board approval records (manual) |
| SC-02 | Roles and responsibilities, segregation of duties | Appendix D; P01; OH10 | CC1.3, CC5.1 | 5.2, 5.3 | 42001 | SoD rule set, violations report |
| SC-03 | Asset inventory (systems, data stores, repositories, vendors) | P24 `eng.service_catalogue`, OH13 register | CC6.1 | 5.9 | — | Inventory export |
| SC-04 | Data classification and labelling | P00 data catalogue | C1.1 | 5.12, 5.13 | 27701 | CI check of tagged columns |
| SC-05 | Access control policy; least privilege; Cerbos policies | P01 | CC6.1–CC6.3 | 5.15, 5.18, 8.2, 8.3 | PCI 7, 8 (SAQ A subset) | Policy tests, access review results |
| SC-06 | MFA and strong authentication | P01 | CC6.1 | 5.17, 8.5 | PCI 8 | MFA coverage report |
| SC-07 | Joiner-mover-leaver for staff and tenant users | P01, OH10 | CC6.2 | 5.16, 5.18, 6.5 | — | JML reconciliation |
| SC-08 | Quarterly access reviews | P24 | CC6.2, CC6.3 | 5.18 | — | Attestation records |
| SC-09 | Privileged access, break-glass, session recording | P01, P00 | CC6.1, CC6.3 | 8.2, 8.18 | — | Break-glass reports |
| SC-10 | Tenant isolation (RLS, keys, indices) | P00 | CC6.1, C1.1 | 8.3 | — | NN-01 test results |
| SC-11 | Encryption in transit and at rest; key management | P00, §Q.4 | CC6.1, CC6.7 | 8.24 | PCI 4 | Config snapshots, KMS rotation status |
| SC-12 | Secure development lifecycle, code review, CODEOWNERS | P00, P24 | CC8.1 | 8.25–8.29 | 42001 | PR approvals sample, rulesets export |
| SC-13 | Change management with approvals and CAB | P24, OH13 | CC8.1 | 8.32 | — | Change records ↔ deployments reconciliation |
| SC-14 | Vulnerability management and patch SLAs | P24 | CC7.1 | 8.8 | PCI 6.3, 11.3 (as applicable) | SLA report |
| SC-15 | Penetration testing (CERT-In empanelled) | P24 | CC4.1, CC7.1 | 8.8 | CERT | VAPT reports (manual) |
| SC-16 | Secure configuration baselines (CIS AWS) | P00, P24 | CC7.1 | 8.9 | — | Security Hub score |
| SC-17 | Malware protection for uploads | P00 | CC6.8 | 8.7 | — | AV signature freshness |
| SC-18 | Logging, monitoring, alerting; 180-day logs in India | P00, P24 | CC7.2 | 8.15, 8.16, 8.17 | CERT | Log retention probe |
| SC-19 | Incident management and notification clocks | P24 | CC7.3–CC7.5 | 5.24–5.28, 6.8 | CERT 6 h; DPDP | Incident register, tabletop reports |
| SC-20 | Backup, restore testing | P24 | A1.2, A1.3 | 8.13 | 22301 | Restore test results |
| SC-21 | Business continuity and DR | P24 | A1.2, A1.3 | 5.29, 5.30 | 22301 cl. 8 | DR drill reports |
| SC-22 | Capacity and performance monitoring | P24 | A1.1 | 8.6 | — | Capacity reports |
| SC-23 | Supplier/sub-processor management | §Q.9, OH14 | CC9.2 | 5.19–5.23 | 27701; DPDP s.8(2) | Vendor reviews (manual), DPAs |
| SC-24 | Cloud services security | P00 | CC9.2 | 5.23 | — | Cloud posture |
| SC-25 | Physical security (inherited from AWS; offices of LawDocs) | Cloud SOC reports; OH | CC6.4 | 7.1–7.14 | — | Carve-out evidence (manual) |
| SC-26 | Security awareness and privacy training | OH (group LMS) | CC1.4, CC2.2 | 6.3 | 27701 | Completion reports |
| SC-27 | Screening and confidentiality agreements for staff | OH10 | CC1.4 | 6.1, 6.2, 6.6 | — | HR records (manual) |
| SC-28 | Remote working controls (device management, VPN-less zero trust) | OH12 | CC6.1, CC6.7 | 6.7, 8.1 | — | Device compliance report |
| SC-29 | Data retention, deletion and legal hold | P19, P00 | C1.2, P4 | 8.10 | 27701; DPDP s.8(7) | Retention job logs |
| SC-30 | Data-subject rights handling (own users) | P01 | P5, P6 | — | 27701; DPDP s.11–14; GDPR Art. 15–22 | Request register |
| SC-31 | Privacy notices and consent records | P01, P23 | P2, P3 | — | 27701; DPDP s.5–6; Rules notice | Consent ledger |
| SC-32 | Processor obligations for client data (DPA, instructions, sub-processor notice, assistance) | §Q.8 | P1–P8, C1 | 5.34 | 27701; DPDP s.8(2) | Signed DPAs (manual) |
| SC-33 | Cross-border transfer controls | P00 SCPs, P19 | C1.1 | 5.14 | DPDP s.16 | Residency tests |
| SC-34 | Audit ledger integrity and correction governance | P00 | PI1.4, CC7.2 | 8.15 | — | Chain verification, corrections report |
| SC-35 | Processing integrity of calculations (golden tests, REGULATED changes) | P04, P09, P11, P13, P20 | PI1.1–PI1.5 | 8.29 | — | Golden test reports |
| SC-36 | Content governance (maker-checker-publisher, citations) | P03, P05 | PI1.2 | 5.37 | — | Publication approvals |
| SC-37 | AI governance: model inventory, risk assessment, evaluation, human oversight, logging | P17 | CC3.2, PI1 | 5.8 (project), 8.25 | 42001 A.2–A.10 | Model cards, eval results |
| SC-38 | AI data protection: no training on tenant data; provider terms | P17, §Q.9 | C1.1 | 5.20 | 42001; DPDP | Provider contracts (manual) |
| SC-39 | Payment security: hosted checkout, script inventory, webhook signatures | P20, P24 | CC6.7 | 8.26 | PCI SAQ A eligibility; 2.x/8.x/9.x/12.x subset | Script inventory diff, SAQ A (manual) |
| SC-40 | Email and domain security (SPF/DKIM/DMARC, DNSSEC) | P00 | CC6.6 | 8.20, 8.21 | — | DNS checks |
| SC-41 | Web application protections (WAF, CSP, headers, rate limits) | P24 | CC6.6 | 8.20–8.23 | PCI SAQ A eligibility (site protected from script attacks) | Header scan |
| SC-42 | Secrets management | P00 | CC6.1 | 8.24 | — | Secret scanning results |
| SC-43 | Source code protection and mirrors | P24 | CC8.1 | 8.4 | — | Rulesets, mirror restore test |
| SC-44 | Test data management (no production data in non-prod) | P00 | C1.1 | 8.33 | 27701 | Provider-routing guard tests |
| SC-45 | Credential vault controls | P22, §Q.4.4 | CC6.1, C1.1 | 5.17, 8.5 | — | Reveal logs, rotation status |
| SC-46 | Supervisor and auditor access governance | P01 | CC6.2, C1.1 | 5.15 | Client regulatory expectations | Grant reports |
| SC-47 | Delivery staff access governance | P01, P22, OH11 | CC6.2 | 5.18 | — | Delivery access reports |
| SC-48 | Sealed data controls (POSH etc.) | P00, P13 | C1.1 | 5.34 | POSH Act confidentiality s.16 | Sealed access logs |
| SC-49 | Export controls and s.63 certificates | P19 | C1.1, PI1.5 | 8.10 | BSA 2023 s.63 | Export register |
| SC-50 | Compliance with legal and contractual requirements register | P03 (LDC_GROUP tenant) | CC2.3 | 5.31, 5.36 | — | LDC_GROUP compliance status |
| SC-51 | Threat intelligence intake (CERT-In advisories, vendor advisories) | P24 | CC7.1 | 5.7 | CERT | Advisory triage log |
| SC-52 | Information security in project management | P24 PR template | CC8.1 | 5.8 | — | PR template compliance |
| SC-53 | Clock synchronisation | P00 | CC7.2 | 8.17 | CERT item (i) | NTP config |
| SC-54 | Customer communication of incidents and changes | P24 | CC2.3 | 5.24 | Client contracts | Notices log |

---

## Q.7 Compensating controls register (initial)

| ID | Gap | Compensating control | Owner | Review |
|---|---|---|---|---|
| RISK-ENG-001 | GitHub environment protection/paid scanners not licensed | `ReleaseApprovalWorkflow`; OSS scanners | CTO | Quarterly |
| RISK-HOST-001 | Supabase beta lacks ap-south-2 DR and Object Lock | Daily logical backups to ap-south-2; evidence in AWS S3 Object Lock; disclosed RPO 24 h | CTO | Before first paid RE tenant |
| RISK-TSA-001 | No RFC 3161 TSA | KMS-signed anchors in Object Lock; tenant-downloadable anchors | Security lead | Semi-annual |
| RISK-OBS-001 | Observability vendor residency unverified | Self-hosted LGTM in ap-south-1 | SRE | On vendor change |

---

## Q.8 Privacy architecture

### Q.8.1 Roles

| Processing | LawDocsComply's role | Legal anchor |
|---|---|---|
| Client tenant data (employees, directors, customers/borrowers in grievance records, members of societies, complainants, vendors) | **Data processor** for the client (data fiduciary) | DPDP s.8(2) (fiduciary may engage processor under a valid contract); GDPR Art. 28 where applicable |
| LawDocsComply user accounts, leads, health-check users, marketplace buyers, website visitors | **Data fiduciary** (controller) | DPDP s.4–6 (consent or legitimate uses), Rules 2025 notice |
| Marketplace engagements where LawDocs professionals deliver services | LawDocs as service provider/fiduciary for engagement data per engagement terms; processor where acting on client instructions inside the tenant | Engagement letter / SLA (P21) |
| Third-party marketplace professionals | Independent fiduciaries for their engagement data; LawDocsComply processor for platform hosting | Provider terms (P21) |
| Group sharing (Finbyx, Udofin, Equator, OH) | Per Ecosystem Spec data-sharing matrix; group data-sharing agreement | Ecosystem Spec §7, §13 |

Significant Data Fiduciary: not expected for LawDocsComply itself; the platform supports clients that are SDFs (DPIA, audit, algorithmic due diligence records — P12) [VERIFY notification status].

### Q.8.2 Processor commitments (DPA template points, P21/P20 contract artefacts)

Process only on documented instructions (the tenant's configuration and use are instructions); confidentiality of personnel; security per this appendix; sub-processor list with prior notice of changes (≥ 30 days) and objection right; assistance with data-principal requests (P12 workflows) and breach notification (P24 clocks); deletion or return at end (P19 export, then deletion with certificate); audit rights (provider-assurance room, P24); India residency; no use of tenant data for training models or for any purpose of LawDocsComply's own (except aggregated, anonymised service metrics); cross-border transfer only per DPDP s.16 and contract.

### Q.8.3 International privacy overlays (D-19)

For clients serving EU data subjects or Californian consumers, the platform's processor terms include GDPR Art. 28 clauses and Standard Contractual Clauses where needed, and CCPA/CPRA "service provider" contract terms (Cal. Civ. Code §1798.100(d), §1798.140(ag); CPPA regulations) [VERIFY current regulation sections]. LawDocsComply's own processing of EU residents' data (e.g., a European visitor) follows a GDPR-aligned notice and cookie consent. The tenant-facing privacy compliance features for clients (ROPA, DPIA, consent, DSR, breach registers) are in P12.

### Q.8.4 Privacy by design checklist for every phase

Purpose for each personal-data field; minimisation; retention class; access roles; masking; whether exported and where; whether AI may read it; whether sent to the ecosystem (with `consentref`/`legalbasis`); notice text impact; DPIA needed? (new tracking of employees, new sensitive processing, AI decisions affecting people) — recorded in the PR template privacy section and `docs/privacy/<module>.md`.

---

## Q.9 Sub-processor register (initial; maintained in OH14 and published on the trust page)

| Sub-processor (candidate) | Purpose | Data classes | Region | Contract / status |
|---|---|---|---|---|
| Amazon Web Services | Hosting, storage, KMS, email (SES), backups | All | ap-south-1, ap-south-2 | Customer agreement + DPA [VERIFY] |
| Supabase | PostgreSQL for non-prod and beta | Beta tenant data | ap-south-1 | DPA [VERIFY]; beta only |
| AWS Bedrock (Claude, India geographic cross-Region inference ap-south-1 ⇄ ap-south-2) | Vidhi AI — default route for personal, confidential, financial, legal and HR data | Tenant content per AI settings | India only; no failover outside India (NN-41) | D-14 as amended by X-03 [VERIFY model list, retention terms and DPA] |
| Anthropic (Claude API, first-party) | Vidhi AI — public or non-personal content only | Non-personal content | Global/US (no India option) | X-03; never for regulated data classes |
| Jio (JioCX SMS/voice/RCS/WhatsApp, SIP trunk; Haptik bots) | Optional channel and calling adapters; no LLM use (no public enterprise LLM API found, master §7) | Per feature | India [VERIFY] | Not active until verified |
| Razorpay | Payments, subscriptions (through the OH8 group merchant account, X-02) | Billing contact, payment status (no card data) | India | Merchant agreement held by the Operations Hub billing entity |
| eSign providers (Leegality, Digio, SignDesk, Surepass) | Aadhaar eSign, DSC flows | Signer identity data | India | Per selection |
| KYB data providers (Probe42, Signzy, Surepass, Perfios/Karza) | Organisation data | Public company data, director names/DIN | India | Per selection |
| GSP/ASP | GSTIN search | Public GSTIN data | India | Per selection |
| SMS/WhatsApp providers | OTP and notifications | Mobile numbers, message content | India | Per selection |
| Microsoft (Microsoft 365, Entra ID) | Staff identity, delivery workspace; client calendar/storage connectors | Staff data; client data the client chooses to sync | India geo where configured [VERIFY tenant geography] | Group agreement |
| Google (Workspace APIs) | Client connectors | Client-chosen data | Per client | Client's own agreement |
| GitHub | Source control | Code (no production data) | Global (code only) | GHEC agreement |
| Observability/status/paging vendors | Operations | Logs (scrubbed), staff contacts | India or self-hosted | [VERIFY] |

A sub-processor is activated only when its row is approved by the DPO and security lead, with region verified and DPA signed; P18 adapters check `int.connectors.subprocessor_approved` before live use.

---

## Q.10 Records of processing (LawDocsComply as fiduciary) — structure

Processing activity; purpose; data principals; data categories; legal basis (consent / legitimate use under DPDP s.7 / contract); source; recipients; sub-processors; retention; security measures; cross-border; DPIA reference. Maintained in the `LDC_GROUP` tenant's P12 module (dog-fooding) and exportable.

---

## Q.11 Policy and procedure set (owner to write; templates hosted in P07)

| # | Document | Owner | Review |
|---|---|---|---|
| 1 | Information Security Policy | CISO | Annual, Board |
| 2 | Acceptable Use Policy | CISO / HR | Annual |
| 3 | Access Control Policy (incl. privileged access, break-glass) | CISO | Annual |
| 4 | Cryptography and Key Management Policy | CISO | Annual |
| 5 | Data Classification and Handling Policy | DPO / CISO | Annual |
| 6 | Data Retention and Disposal Policy (incl. legal hold) | CS / DPO | Annual |
| 7 | Privacy Policy (external notice) and Cookie Policy | DPO | Annual |
| 8 | Data Protection (internal) Policy and DPA template | DPO | Annual |
| 9 | Data Subject Rights Procedure | DPO | Annual |
| 10 | Personal Data Breach Response Procedure | DPO / CISO | Annual |
| 11 | Incident Response Plan (incl. CERT-In 6-hour reporting, client 2-hour notices) | CISO | Annual + after incidents |
| 12 | Business Continuity Plan and DR Plan | CTO | Annual + after drills |
| 13 | Backup and Restore Procedure | SRE | Annual |
| 14 | Change Management Procedure | CTO | Annual |
| 15 | Secure Software Development Policy (incl. code review, dependencies, SBOM) | CTO | Annual |
| 16 | Vulnerability and Patch Management Procedure | CISO | Annual |
| 17 | Logging and Monitoring Standard | CISO | Annual |
| 18 | Asset Management Policy | CTO | Annual |
| 19 | Supplier and Sub-processor Management Policy | CISO / Procurement | Annual |
| 20 | Cloud Security Standard | CTO | Annual |
| 21 | Remote Working and Device Policy | CISO / HR | Annual |
| 22 | Human Resources Security (screening, onboarding, offboarding, disciplinary) | HR | Annual |
| 23 | Security Awareness and Training Plan | CISO | Annual |
| 24 | Risk Management Methodology and Risk Register procedure (ISMS) | CISO | Annual |
| 25 | AI Governance Policy (model inventory, evaluation, human oversight, acceptable AI use) | CTO / DPO | Annual (ISO 42001) |
| 26 | Payment Security Procedure (PCI SAQ A scope, script inventory) | CFO / CISO | Annual |
| 27 | Credential Vault Usage Policy (client and delivery staff) | CISO / Delivery head | Annual |
| 28 | Content Governance Policy (regulatory content maker-checker-publisher, corrections, AI-generated content) | Company Secretary | Annual |

Plus the Statement of Applicability (ISO 27001), system description (SOC 2), and the Correction Entry governance procedure (D-02).

---

## Q.12 Certification roadmap and audit evidence

| Step | Timing [REC] | Prerequisites | Output |
|---|---|---|---|
| Readiness assessment (external) | GA − 2 months | Controls SC-01…SC-54 implemented; policies drafted | Gap report |
| SOC 2 Type 1 (Security, Availability, Confidentiality; Processing Integrity for calculation/returns modules) | GA + 2 months | Gaps closed; system description | Type 1 report (point-in-time design) |
| ISO/IEC 27001:2022 Stage 1 → Stage 2 | GA + 3–6 months | ISMS operating ≥ 3 months; internal audit; management review | Certificate |
| SOC 2 Type 2 (first window 6 months) | Window starts after Type 1 | Evidence collectors running | Type 2 report |
| ISO/IEC 27701:2025 | After 27001 | PIMS operating | Certificate [VERIFY transition rules] |
| ISO/IEC 42001:2023 | When AI features are material — readiness artefacts from GA (§Q.18.4) *(v1.1)* | AI management system; vendor AI assurance pack | Certificate |
| ISO 22301:2019 | For bank/enterprise demand | BCMS operating | Certificate |
| PCI DSS v4.0.1 SAQ A | Before paid launch | Hosted checkout; eligibility confirmation | Self-assessment with acquirer |
| CERT-In comprehensive audit | Annually | Empanelled auditor | Audit report |

Evidence catalogue: P24 §4H; evidence items are stored in `eng.control_evidence` and mirrored to OH14, where auditors access them through the provider-assurance room.

---

## Q.13 Client assurance pack (what regulated clients receive)

Security overview and architecture diagram; data-flow diagram per module; sub-processor list; data residency statement (India); encryption and key management summary; access control and SoD summary; audit-trail and correction design (D-02) — the feature clients value most; BCP/DR summary with latest drill result; latest VAPT executive summary (CERT-In empanelled auditor); incident notification commitments (≤ 2 hours to client); standard questionnaire answers; DPA; right-to-audit clause and provider-assurance room process; once issued, SOC 2 reports (under NDA) and ISO certificates. This pack supports the client's own outsourcing and IT-vendor due diligence obligations (RBI, SEBI CSCRF third-party requirements, IRDAI and IFSCA cyber guidelines) [VERIFY paragraph references in P12].

---

## Q.14 Incident and breach notification matrix

| Event | Who LawDocsComply notifies | Clock | Channel | Content |
|---|---|---|---|---|
| Specified cyber incident affecting LawDocsComply systems | CERT-In | ≤ 6 hours of noticing | CERT-In reporting format | Per Directions annexure |
| Incident affecting a regulated client's data or service | Client (`ten_admin`, CCO, CISO contacts on file) | ≤ 2 hours of detection | Phone tree + email + Updates feed "Security notice" | What, when, systems, data classes, tenants, containment, next update time, contact |
| Personal-data breach of client data (LDC as processor) | Client (data fiduciary) | Without delay; first notice within the 2-hour client clock | Same | Facts the fiduciary needs for DPDP Rule 7 intimation and 72-hour report |
| Personal-data breach of LDC's own users' data (LDC as fiduciary) | Data Protection Board and affected principals | Without delay; detailed report within 72 hours (DPDP Rules 2025) | Board portal; email/in-app | Per Rules [VERIFY form] |
| EU personal data (if any) | Client (as controller) / supervisory authority where LDC is controller | GDPR Art. 33: 72 hours (controller) | — | — |
| Service outage (no data impact) | All affected tenants | Status page within 30 minutes (Sev-1/2) | Status page, in-app banner | Status and updates |
| Group product affected (Finbyx/Udofin/Equator integration) | Product owners via OH13 | ≤ 2 hours | OH13 incident | Counts and classes only |

---

## Q.15 Secure SDLC and AI security

- Threat modelling per phase; security requirements from ASVS 5.0; security review for REGULATED and auth-related changes; SAST/SCA/secrets/IaC/container/DAST/fuzz per P24; dependency policy (no unmaintained packages for security-relevant functions; licence policy); SBOM per release; signed artefacts; reproducible builds where feasible.
- AI security (OWASP Top 10 for LLM Applications): prompt-injection defences (content provenance tags, instruction hierarchy, tool allow-lists, output validation); sensitive-information disclosure controls (permission-filtered retrieval, data-class filters, redaction); excessive agency limits (NN-14 human gates, scoped tool tokens, rate limits, kill switch `ai.agents.enabled`); supply chain of models (provider inventory, version pinning, evaluation before switching); misinformation controls (citations required for regulatory answers, "no source → say so", confidence labels); denial-of-wallet controls (per-tenant token budgets, P20 metering).
- Evaluation: P17 maintains an evaluation set per agent and a red-team suite; model/provider/prompt changes need passing thresholds and are REGULATED changes.

---

## Q.16 Open items

| OI ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-Q-01 | ASVS 5.0 chapter numbering and level mapping per app | Security lead | Use ASVS 5.0 categories as published |
| OI-Q-02 | Indicative framework mappings in §Q.6 to be validated by readiness assessor | CISO | Treat as working mapping |
| OI-Q-03 | BSA 2023 s.63 certificate form (Schedule) and who signs Part B for SaaS-generated records | Counsel | Generate certificate with system-operator statement; counsel review |
| OI-Q-04 | RBI portal terms on credential sharing with service providers | Compliance | Client-only default with warning |
| OI-Q-05 | AI provider terms: Claude models and retention/DPA terms on Bedrock India geographic cross-Region inference (available since 29 Sep 2026, master §7); Anthropic API used only for non-personal content | CTO / DPO | Regulated-data AI features off until the Bedrock contract and DPA are on file |
| OI-Q-06 | SEBI PIT Reg 3(5) structured digital database support scope | CS | P06 implements logging of UPSI sharing |
| OI-Q-07 | DPDP Rules 2025 breach intimation form and Board portal process | DPO | Manual intimation procedure |
| OI-Q-08 | AWS KMS FIPS validation level statement for client questionnaires | SRE | Quote AWS documentation at time of answer |

---

## Q.18 v1.1 additions — region cells, data transfers, agentic AI security and ISO/IEC 42001 *(v1.1)*

### Q.18.1 Region cells and residency (D-42; NN-24 amended)

| Control | Implementation | Evidence |
|---|---|---|
| SC-60 Home-cell residency | `core.tenants.home_region` immutable; routing by directory; no cross-cell queries (CI test `NN-24_cells_isolated`) | Test report; directory audit |
| SC-61 Per-cell keys | Separate KMS key hierarchy per cell; no cross-cell key grants | KMS policy diff |
| SC-62 Per-cell sub-processors | Sub-processor register rows carry cell; a cell cannot be released (P24 FR-P24-46) with an out-of-date row | Register, release gate log |
| SC-63 Content-plane replication | Signed content bundles (no personal data) replicated from IN; signature verified in the receiving cell | Bundle signatures |
| SC-64 Cross-cell group views | Aggregates only, minimum cohort size, computed in the source cell and pushed as numbers | Aggregation job logs |
| SC-65 Region migration | P24 FR-P24-45 runbook with consent and transfer basis | Migration record, deletion certificate |

### Q.18.2 Data-transfer controls by law (for cross-border flows the product enables)

| Law | Transfer rule (summary; counsel to confirm per case) | Product control |
|---|---|---|
| India — DPDP Act 2023 s.16 | Transfer permitted except to countries notified as restricted (no list notified as of Mar 2026 [VERIFY]); sectoral rules prevail (e.g., RBI payment-data storage directions; sectoral localisation) | `IN` cell default; sector flags block transfer of payment-system data and other localised classes; transfer register per tenant |
| EU/EEA — GDPR Chapter V (Arts. 44–49) | Adequacy decision, SCCs (2021/914) with transfer impact assessment, BCRs or derogations; India has no adequacy decision [VERIFY] | EU tenants hosted in `EU` cell; SCC module 2/3 in DPA; TIA template; no EU personal data routed to IN except under SCCs and a TIA |
| UK — UK GDPR / Data (Use and Access) Act 2025 | IDTA or UK Addendum to EU SCCs [VERIFY post-2025 changes] | UK tenants in `EU` cell unless a UK cell opens; UK Addendum in DPA |
| UAE — PDPL (Federal Decree-Law 45/2021); DIFC DP Law 2020 (amended effective 15 Jul 2025); ADGM DPR 2021 | Transfers to adequate jurisdictions or with safeguards; PDPL Executive Regulations still unpublished (Feb 2026) [VERIFY] | `GCC` cell for UAE tenants; free-zone selection drives the applicable regime |
| Saudi Arabia — PDPL and Transfer Regulations | Restrictive; draft amendments (consultation to 5 Nov 2026) propose localisation and registration | Saudi personal data deferred (D-46); non-personal entity calendars only |
| Singapore — PDPA s.26 and Transfer Limitation Obligation | Recipient bound by comparable protection (contract, BCR, certification) | `SG` cell; contractual clauses |
| United States — state laws (CCPA/CPRA and others) | No general transfer restriction; service-provider contracts; sector rules | `US` cell when opened; CCPA service-provider terms |
| China — PIPL | Security assessment / standard contract / certification | Not offered for personal data (D-46); non-personal entity calendars only |

Every tenant has a **transfer register** (P12) listing flows, legal basis, safeguard document and review date; LDC's own transfers are in Appendix Q §Q.10 records.

### Q.18.3 Agentic AI threat model additions (Appendix AA; NN-41, NN-50–NN-52)

| Threat | Mitigation | Test |
|---|---|---|
| Indirect prompt injection through uploaded documents, emails, WhatsApp exports, web pages | Provenance tags; instructions in content are data; tool calls need user-intent match; L2 default | Red-team suite RT-01…RT-35 (Appendix K) |
| Tool misuse / excessive agency | Tools filtered by effective autonomy level; external-effect tools never exposed (NN-14); per-skill allow-lists | `NN-50_*` tests |
| MCP server data exfiltration by a client's external AI | Calling user's permissions only; sealed classes never returned; personal/confidential data only with tenant basis recorded; rate limits and anomaly detection | `NN-52_mcp_no_sealed` |
| A2A impersonation of a group-product agent | mTLS + signed agent cards; every A2A task mapped to an Ecosystem contract | Contract tests |
| Memory poisoning (persistent agent memory) | Memory writes are typed, attributed, reviewable and expire; no memory from sealed contexts | Memory audit job |
| Model or provider drift | Nightly evaluations; automatic demotion of autonomy; AI change classes (P24 FR-P24-47) | Drift reports |
| Runaway cost | Per-tenant credit budgets, per-mission ceilings, kill switches | FinOps alerts |
| Inability to stop AI | Kill switches ≤ 60 s, drilled quarterly (NN-51) | Drill evidence |

### Q.18.4 ISO/IEC 42001:2023 readiness map (LDC's own AI management system; D-38)

| 42001 area | LDC artefact |
|---|---|
| Clause 4 Context; 5 Leadership | AI policy; roles (AIO, `eng_ai_lead`, sponsors); scope statement covering Vidhi, MCP server and A2A |
| Clause 6 Planning | AI risk assessment and AI system impact assessment per skill (template in P12 `OV_AI`); objectives (evaluation targets) |
| Clause 7 Support | Competence records for AI staff; documented information in `docs/ai/` |
| Clause 8 Operation | Model registry, AI change classes, evaluation gates, data provenance for notebooks, supplier controls for model providers (no training, region, retention) |
| Clause 9 Performance evaluation | Nightly evals, quarterly kill-switch drills, internal audit of the AIMS, management review |
| Clause 10 Improvement | AI incident register, corrective actions, technology radar (P24 FR-P24-50) |
| Annex A control areas (A.2–A.10: policies, internal organisation, resources, impact assessment, life cycle, data, information for interested parties, use, third-party relationships) | Mapped row-by-row in `docs/compliance/iso42001-soa.xlsx` [VERIFY control numbering against the standard text] |

### Q.18.5 Policy set additions (extend §Q.11)

AI use and governance policy; agent autonomy and sponsorship standard; model and prompt change standard; data-transfer and residency policy; partner security requirements (content and delivery partners, P25); legal-privilege handling standard (P26); ESG data and assurance-evidence standard (P27).

### Q.18.6 Client assurance pack additions (extend §Q.13)

Region-cell statement per tenant; transfer register extract; vendor AI assurance pack (P24 FR-P24-49); autonomy defaults and kill-switch drill evidence; MCP server security summary.

---

## Q.20 IPB-02 Security Baseline — relationship to this appendix *(v1.3; pointer; D-59–D-70)*

From v1.3 the control library, the control-to-framework matrix (CERT-In, ISO/IEC 27001:2022, 27701, 42001, 22301, SOC 2, PCI DSS v4.0.1 SAQ A, DPDP Act and Rules, RBI outsourcing and IT directions, SEBI CSCRF, OWASP ASVS 5.0 / LLM / Agentic), identity and isolation design, data-protection tiers, secrets, supply chain, upload pipeline, logging, incident runbook, backup/DR targets, vulnerability management, AI security, the "cannot be demolished" list and the threat-model and red-team templates are **IPB-02** (`docs/ipb/IPB-02_Security_Baseline_and_Certification_Map.md`). This appendix remains the **LDC overlay**: where §Q.1–§Q.18 and IPB-02 differ, the stricter rule applies and the difference is recorded as `IPB-DEV-nn`; none is recorded at v1.3.

LDC-specific positions that IPB-02 names and this appendix keeps: (1) LDC hosts the **AI system register** (IPB-02-79; `aig`, P12 §4P) used by all six products and the group's own ISO/IEC 42001 evidence (§Q.18.4); (2) LDC receives the group **vulnerability register** export (IPB-02-71) and `in.infrabyx.grc.VulnerabilityRecorded.v1` (canonical name in Ecosystem Spec v1.2 §6.15; the IPB-02 working name `security.VulnerabilityRecorded` is superseded per Spec §6.17) as GRC evidence; (3) LDC's consent ledger and consent-manager-shaped API (`/v1/consent/*`, `fut.dpdp-consent-manager-api` OFF until 13 Nov 2026 [VERIFY]) are the reference implementation other products reuse (IPB-02-26); (4) regulated-client incident notification within the contractual window, default `trust.incidents.contractual_window_hours = 2`, so RBI/SEBI/IRDAI tenants can meet their own six-hour duty (IPB-02-59; P24 FR-P24-53) [LAW; VERIFY paragraph]; (5) `trust.ai.residency_floor = IN-ZR` on regulated plans; (6) evidence collectors (IPB-02-87) are implemented as LDC controls so the group's certification evidence runs on the product; (7) the Vendor Assurance Room mirror (IPB-08; P24 §4M) replaces §Q.13's "client assurance pack" description — §Q.13 stays as the list of what regulated clients receive, now served from the room; (8) §Q.11 (board-approved internal policies, hosted in P07) is distinct from the **public legal policy set** drafted in Appendix AD (IPB-05); both are owner items (#11, #28). Open items of IPB-02 that name LDC: `IPB-OI-02-12` (SEBI CSCRF applicability and evidence pack).

## Q.19 Sources (checked 25 October 2026 unless stated; renumbered in v1.1)

1. CERT-In Directions under s.70B(6) IT Act 2000 (28 Apr 2022); CERT-In Comprehensive Cyber Security Audit Policy Guidelines (25 Jul 2025) — summary: https://www.azbpartners.com/bank/strengthening-indias-cyber-defence-cert-ins-new-cyber-security-audit-guidelines-decoded/ [VERIFY original]
2. Digital Personal Data Protection Act 2023; Digital Personal Data Protection Rules 2025 (notified 13 Nov 2025) — https://www.meity.gov.in/
3. Bharatiya Sakshya Adhiniyam 2023, s.63.
4. SEBI (Prohibition of Insider Trading) Regulations 2015, Reg 3(5) [VERIFY].
5. PCI DSS v4.0.1 and SAQ A (Jan 2025 revision) — https://www.akamai.com/blog/security/pci-dss-v4-0-1-changes-qualify-saq-a [VERIFY with PCI SSC]
6. ISO/IEC 27001:2022; ISO/IEC 27701:2025 (https://www.kiwa.com/en/nl/about-kiwa/news/isoiec-277012025-published-updated-privacy-standard-offers-organizations-more-guidance); ISO/IEC 42001:2023; ISO 22301:2019.
7. AICPA 2017 Trust Services Criteria (revised points of focus 2022).
8. OWASP ASVS 5.0; OWASP Top 10 for LLM Applications.
9. Infrabyx Ecosystem Integration Specification v1.1 — §3.6, §3.8, §4.7, §13.2.
10. Infrabyx Operations Hub Master Prompt v1.0 — OH13, OH14.
11. GDPR (Regulation (EU) 2016/679) Art. 28, 33; California Consumer Privacy Act as amended by CPRA, and CPPA regulations [VERIFY sections].
