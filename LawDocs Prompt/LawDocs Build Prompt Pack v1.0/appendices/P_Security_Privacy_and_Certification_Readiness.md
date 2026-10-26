# Appendix P — Security, Privacy and Certification Readiness

> **Status:** Binding. LawDocs Build Prompt Pack v1.0 · 25 October 2026.
> **Used by:** P00 (platform controls, residency, logging), P01 (authentication, Aadhaar/DigiLocker, consent), P02 (access control, SoD, reviews), P04 (vault, retention, legal hold), P05 (masking of derived text), P08 (eSign/eStamp/evidence), P09 (AI security), P17 (payments, PCI scope), P19 (APIs, webhooks), P20 (export, BYO storage, keys), P22 (mobile), P23 (VAPT, hardening, evidence automation, go-live) and every phase's §10.
>
> **How to use.** Each phase threat-models its modules with §P.2, applies the handling rules of §P.3, meets the ASVS level of §P.4, registers its controls in §P.12 with an evidence collector, and adds its processing to the records of processing (§P.8.9). Legal facts come from R3 (rule IDs `LG-xxx`); anything unverified is `[VERIFY]` and gated by NN-38. LawDocs makes **no certification, attestation, compliance or regulator-endorsement claim** until the report or certificate exists and passes the Operations Hub OH14 claims gate (NN-20; Ecosystem Spec §13.3).

---

## P.0 Purpose, scope and the language of readiness

LawDocs holds agreements, signed originals, evidence packs, court papers, family and property records, identity verification results, consumer grievances and, where a client enables it, portal credentials. Individuals and companies will trust it only if it is controlled and provably so. This appendix sets the security and privacy architecture, the control set mapped to SOC 2, ISO/IEC 27001:2022, 27701, 42001 and 22301, the DPDP programme, the PCI DSS SAQ A position, the CERT-In and IT Rules duties, the VAPT plan, vendor risk and incident response.

**Scope:** all LawDocs apps (public, web, delivery, console, mobile), the API and workers, data stores, integrations and adapters, the AI gateway and agents, the Consumer Help brand, delivery operations of LawDocs staff inside client tenants, and the supporting cloud, source-control and workplace environments. The Operations Hub, Finbyx, Udofin, Equator and LawDocsComply have their own controls; interfaces with them are in scope.

**"Designed for" versus "certified" — binding wording.**

| Situation | Permitted wording | Prohibited wording |
|---|---|---|
| Before any audit | "Built to SOC 2 and ISO/IEC 27001 control requirements"; "Our controls are mapped to SOC 2 and ISO/IEC 27001:2022" | "SOC 2 certified", "ISO certified", "compliant" |
| SOC 2 Type 1 report issued | "SOC 2 Type 1 report (Security, Availability, Confidentiality) as of <date>, available under NDA" | "SOC 2 certified" (SOC 2 is an attestation report, not a certificate) |
| SOC 2 Type 2 report issued | "SOC 2 Type 2 report for <period>" | "Fully SOC 2 compliant" |
| ISO/IEC 27001 certificate issued | "ISO/IEC 27001:2022 certified by <certification body>, certificate <no.>, scope <scope>" | Any wider scope than the certificate |
| PCI DSS | "Payments are processed on our payment partner's hosted checkout; LawDocs never sees or stores your card details"; after attestation: "PCI DSS SAQ A self-assessment completed <date>" | "PCI DSS certified" (CH-19; R3 LG-148) |
| DPDP | "We follow the Digital Personal Data Protection Act 2023 and Rules 2025" with the DPO contact | "DPDP certified", "government-approved" |
| Data location | "Your data is stored in India (Mumbai, with disaster recovery in Hyderabad)" — true by NN-25 | "Never leaves India" if any approved transfer exists (e.g., an AI call outside India for public content) |
| eSign | "Aadhaar eSign through a licensed eSign Service Provider" with the ESP named | "Government eSign", "LawDocs eSign certificate" |

---

## P.1 Security principles

1. **Tenant isolation first:** RLS as the wall; Cerbos as the room; tenant-scoped keys, caches, indices, object prefixes and workflow IDs (NN-01).
2. **Tamper-evident history:** append-only, hash-chained ledger; daily signed anchors; Correction Entries instead of edits (NN-02).
3. **Immutable originals:** S3 Object Lock and SHA-256 at ingest for originals and signed files; derived renditions labelled (NN-09).
4. **Least privilege and separation of duties:** server-side authorisation everywhere; maker ≠ checker at person level; no standing staff access to tenant data (NN-17, NN-18).
5. **Minimise identity data:** no Aadhaar number in any form, no biometric, no OTP, no bureau data, no card data (NN-04, NN-05, NN-22).
6. **India residency:** tenant data, backups and logs in ap-south-1/ap-south-2; any other processing only after a recorded transfer assessment (NN-25).
7. **Assume compromise:** monitoring, immutable logs, separate backup account, tested restores, rehearsed incident response.
8. **AI as a governed component:** human confirmation for irreversible actions, permission-filtered retrieval, no training on customer data, India-resident inference for confidential classes (NN-13, NN-15, NN-43).
9. **Evidence by design:** every control emits dated, hashed evidence automatically (§P.13).
10. **Truth in claims:** §P.0 wording; OH14 claims gate (NN-20).

---

## P.2 Threat model

**Method.** STRIDE per component plus abuse cases; OWASP ASVS 5.0 (§P.4); OWASP MASVS for mobile [VERIFY current version]; OWASP Top 10 for LLM Applications and agentic-AI guidance for `ai`/`agt` [VERIFY current edition]. Each phase writes `docs/security/threat-model-<module>.md` with: assets and data classes; trust boundaries and data-flow diagram; STRIDE table; abuse cases; mitigations mapped to SC-IDs (§P.12); residual risk and tests; review date.

### P.2.1 Top threats

| # | Threat | Asset | Mitigations | Test / residual |
|---|---|---|---|---|
| T1 | Cross-tenant leak via missing filter, cache key, index, object path or AI retrieval | All tenant data | FORCE RLS, fail-closed context, tenant in every key and index, Cerbos query plans for lists, search and retrieval | `NN-01_*` generated tests; pen-test cross-tenant cases every VAPT |
| T2 | Super admin alters client records or impersonates a client | Agreements, master data, history | No in-place edits; Correction Entries dual-approved and tenant-visible; client approval for master data; console on separate origin at AAL3 | Quarterly review of corrections and break-glass |
| T3 | Insider DBA tampers with the database | Ledger, history, originals | Ledger triggers, hash-chain verification, signed anchors under Object Lock; DBA only via break-glass with recording; separate backup account | Daily chain verification; tenants verify anchors offline |
| T4 | Account takeover (SIM swap, OTP interception, phishing, social-login linking) | Vaults, signing requests, company approvals | Passkeys promoted; no SMS as second factor for privileged roles; step-up; OTP-confirmed social linking; new-device alerts; refresh-token reuse detection | Credential-stuffing and SIM-swap tabletop |
| T5 | OTP bombing, SMS pumping, denial of wallet | Cost, availability | Per-number/IP/device caps, +91 allow-list, budgets, anomaly detection, kill switch on `SMS_PORT` | Load tests with abusive patterns |
| T6 | Guest link forwarded; signer impersonation | Agreements, evidence | OTP to the invited contact; device binding; optional L2 for signers; ESP authenticates signers; "not me" control | Signing abuse cases (P08) |
| T7 | Forged board resolution or fake director to gain signing authority | Company identity | Director match with MCA data; evidence review maker-checker; limits; monthly KYB refresh; alerts to all owners on authority changes | Red-team evidence samples |
| T8 | Professional impersonation or lapsed COP | Consumers, compliance with BCI/ICAI rules | Credential desk (OH9/local), annual re-verification, suspension ≤ 1 h, Rule-36-only display | Credential audit sample |
| T9 | RM or professional misuses delegated access | Client data | Client-approved scoped grants, no export, transparency log, monthly reviews, OH internal controls | Monthly access report |
| T10 | Theft of client portal credentials (vault) | MCA, GST, RBI and other portal access | Vault OFF by default, delegation first, client-scoped envelope keys, per-credential reveal with reason and approval, AAL2 ≤ 5 min, clipboard clear, no bulk export, OTPs/DSC PINs never stored (NN-16; CH-07) | Vault pen-test |
| T11 | Prompt injection via uploaded documents, emails, WhatsApp screenshots or web pages | Tenant data, external actions | Untrusted-content tagging, instruction hierarchy, tool allow-lists, per-action human confirmation (NN-13), output filters, retrieval filtered by permission | AI red-team suite in CI (P09) |
| T12 | AI fabricates citations or official-looking records (stamp certificates, orders, IDs) | Users, courts, reputation | Citation resolver (NN-14); refusal rules for official records (IT Rules SGI duty — R3 LG-078); "AI draft — not reviewed" labels; professional review route | Evaluation thresholds per agent |
| T13 | Malicious upload (malware, macro, polyglot, zip bomb) | Workers, users | Quarantine, magic-byte checks, AV, macro policy, sandboxed converters, decompression limits | Converter fuzzing |
| T14 | Supply-chain compromise (dependency, action, image, model) | Code, production | Pinned actions by SHA, signed images, SBOM, provenance, dependency review, model registry and version pinning | SLSA target (P23) |
| T15 | Tampered signed file or evidence pack; hash mismatch disputes | Evidence value in court | Hash at ingest and at export, PKCS7 with timestamp, evidence pack with chain of custody, BSA s.63(4) certificate draft (NN-10; R3 LG-091) | Evidence verification tests |
| T16 | eStamp fraud (reused or mismatched certificate) | Stamp duty compliance | Authorised channels only; UIN verification; certificate linked to document hash; stamp-before-sign gate (NN-08) | P08 tests |
| T17 | Aadhaar number exposure through OCR text, search index, previews, logs, AI context, exports | Aadhaar data (s.29(4)) | No storage; masking hook on all derived text; scrubbers; QR payload discard (NN-04) | `NN-04_*`, log scans |
| T18 | Breach of DigiLocker Requester terms (caching, affiliate use) | Requester status | URI-by-default; retain-copy flag gated; `int` refuses proxying for other products; 24-h NeGD incident clock (NN-42; R3 LG-038) | Annual CERT-In-empanelled audit |
| T19 | Payment fraud, webhook spoofing, price tampering | Revenue, PCI scope | Hosted checkout via OH8; server-side payment fetch; signed webhooks; idempotent order state; script inventory and CSP on payment-referring pages | SAQ A eligibility checks |
| T20 | Private content indexed or exposed through share links; open redirects | Confidential documents | `noindex` + auth on all private routes; signed, expiring links; no user-controlled redirects; redirect map allow-listed hosts (NN-31) | Crawl tests |
| T21 | KYB lookup scraping or cost abuse | Third-party data, cost | Quotas, masking for anonymous, bot controls, metering | Abuse monitoring |
| T22 | Ransomware or cloud account compromise | Availability and integrity | SCPs, separate backup account with vault lock, Object Lock, least-privilege IAM, GuardDuty, tested restores | DR drills (P23) |
| T23 | Fraudulent nominee release | Personal vaults | Nominee L2, evidence review at AAL3 by two staff, waiting period, owner cancellation, logged access | Release abuse cases |
| T24 | Consumer Help ethical-wall breach or conflict of interest | Consumers, group reputation | Separate brand and entity profile, SoD-20, no access to group lender/insurer tenants, conflict check before acceptance (NN-23) | Quarterly wall review |
| T25 | Lost or rooted mobile device | Offline vault cache | Device-bound encrypted cache, biometric unlock local only, root/jailbreak detection, remote session revoke, screenshot blocking on protected screens (NN-44) | MASVS testing |
| T26 | Ecosystem event spoofing or data-class leakage to sister products | Integrity, privacy | Signatures, mTLS, schema validation, data-class ceilings, `consentref`/`legalbasis` checks, `int` as sole publisher (NN-24) | Contract tests |
| T27 | Denial of wallet on anonymous drafting and Vidhi | Cost, availability | Rate limits, per-session token budgets, cheap-model routing for anonymous, kill switches | Load and abuse tests |

### P.2.2 Abuse cases every phase tests where relevant

Admin grants themselves checker (SoD-09); maker edits after approval (digest invalidation); RM approves own item through a second identity (SoD-03); counterparty sees an internal comment (NN-37); delegate tries to sign or export (ceiling); Vidhi asked to email a document to an outside address (blocked without confirmation); departing employee bulk-exports (step-up, maker-checker, alerts); guest replays an expired link; partner tries to call eSign for its own documents (NN-06); attacker uploads an image containing an Aadhaar number and searches for it (masked); attacker requests `/r/<ref>` of another tenant (same "not found").

---

## P.3 Data classification and handling

| Class | LawDocs examples | Encryption | Logging | Export | AI eligibility |
|---|---|---|---|---|---|
| `PUBLIC` | Published templates, blog, help | TLS | Normal | — | Any approved provider |
| `INTERNAL` | Configuration, aggregates, org structure | At rest | Normal | System data | Bedrock India |
| `CONFIDENTIAL` | Agreements, drafts, negotiation, matter notes, grants, approvals | At rest + tenant key | IDs only | Folders per Appendix K | Bedrock India only (NN-15) |
| `PII` | Names, contacts, addresses, masked identifiers | Field-level for contacts (enc + bidx + masked) | Never values (NN-32) | Masked by default | Bedrock India, scrubbed |
| `SPI` | Full PAN, bank details, health-related records in disputes | Field-level, `spi` keyring | Never | Restricted folder | Excluded unless the user explicitly includes the document |
| `KYC_ARTEFACT` | Aadhaar offline attributes, DigiLocker results, guardianship and death/incapacity evidence | `ld_sealed`, `kyc_artefact` keyring | Never | Results only, masked | Excluded |
| `LEGAL` | Pleadings, notices, orders, evidence packs | At rest + tenant key | IDs only | Folder per matter | Bedrock India |
| `LEGAL_PRIVILEGED` | Advice from counsel, privileged communications | Separate keyring | Never content | Restricted folder | Only with explicit user action |
| `HR` | Client HRMS data (kernel/LDC) | `hr` keyring | Never | Restricted | Excluded from training; retrieval only by HR roles |
| `CREDENTIAL` | Vault secrets (P18) | Client-scoped envelope keys in `ld_sealed` | Never | **Never exported** (metadata only) | Never |
| `FINANCIAL` | Order/payment mirrors, stamp-duty amounts | At rest | Amounts only in aggregates | Billing folder | Bedrock India |

Every column is tagged in `db/data-catalogue.yaml` (CI fails on an untagged column, P00). The event envelope `dataclass` is the highest field class; `int` rejects messages above a consumer's ceiling (Ecosystem Spec §13.2); Operations Hub subjects accept at most `INTERNAL` (NN-19).

---

## P.4 OWASP ASVS 5.0 verification levels

**Default: Level 2** for every app and API. **Level 3** for these areas [VERIFY chapter names and numbering in ASVS 5.0 at P00]:

| Area | L3 scope |
|---|---|
| Authentication and session management | `ld-staff` realm and console; customer AAL2/AAL3 flows; passkey ceremonies; recovery |
| Authorisation | Cerbos policies for grants, maker-checker, SoD, break-glass; delivery and engagement grants |
| Cryptography and secrets | KMS integration, envelope encryption, blind indexes, audit-anchor signing, webhook signatures |
| Audit logging and integrity | Ledger, anchors, access log, transparency log |
| Data protection | `ld_sealed`, credential vault, KYC artefacts, nominee release |
| File handling | Ingest pipeline, converters, originals bucket |
| API and web service | Partner onboarding API, ecosystem endpoints, webhooks |

ASVS requirements are mapped per module in `docs/security/asvs-map.md` with status (`MET`, `PARTIAL`, `N/A` with reason, `GAP` with ticket); P23 blocks go-live on any `GAP` at L3 areas.

---

## P.5 Cryptography and key management

**P.5.1 Key hierarchy.** AWS KMS customer-managed keys per environment and data-class keyring (`pii`, `spi`, `kyc_artefact`, `legal`, `legal_privileged`, `hr`, `credential`, `financial`), generating per-tenant data keys (envelope encryption); `dedicated_key` tenants get their own CMK; enterprise BYOK/HYOK through P20 with fail-closed revocation (Ecosystem Spec §12.2). Asymmetric KMS key (ECC_NIST_P256) for audit anchors and export manifests. Separate CMKs in `ld-backup`. KMS is region-bound to ap-south-1 with replicas in ap-south-2 for DR.

**P.5.2 Rotation and custody.** CMKs rotate annually (automatic); blind-index HMAC keys rotate by epoch with re-indexing jobs; webhook secrets every 90 days; OAuth client secrets ≤ 90 days or `private_key_jwt` (Ecosystem Spec §4.2); signing keys with overlapping JWKS; Keycloak realm keys annually. Key policies: no human can decrypt `credential` or `kyc_artefact` keyrings outside approved service roles; key-policy changes are break-glass events reviewed by `PLT_SECURITY_OFFICER`.

**P.5.3 Hashing and signatures.** SHA-256 (and SHA-512 for court evidence on request, R3 LG-091) at ingest and export; RFC 8785 canonical JSON for ledger digests; Argon2id for passwords (Keycloak); HMAC-SHA-256 for OTPs (pepper) and blind indexes; PKCS7/PAdES for signed PDFs per ESP (P08); RFC 3161 timestamps optional (flag).

**P.5.4 Transport.** TLS 1.2 minimum, 1.3 preferred; HSTS; modern cipher suites only; mTLS or signed requests (RFC 9421) for ecosystem and partner endpoints; certificate pinning in mobile apps with a pin-rotation plan.

**P.5.5 Mobile.** Tokens in Keychain/Keystore; encrypted offline vault cache with a device-bound key; biometric unlock device-local (NN-44); no secrets in the app bundle.

---

## P.6 Aadhaar, DigiLocker, eSign and eStamp controls

| Control | Requirement | Source |
|---|---|---|
| AD-01 | No Aadhaar authentication, e-KYC or login; LawDocs is not an AUA/KUA | Aadhaar Act s.4(4), s.57 omitted (R3 LG-022–023); NN-03 |
| AD-02 | Offline verification only (secure QR / e-Aadhaar; AVC after OVSE registration); consent with plain-language information on data shared, uses and alternatives | s.8A(2)–(3); Reg 13A, 3A (R3 LG-025, LG-029–030) |
| AD-03 | Never collect, use or store the Aadhaar number or biometrics; store purpose-limited attributes and last four digits only where required | s.8A(4), s.29(4) (R3 LG-025–026); NN-04 |
| AD-04 | Discard QR payloads, XML, share codes and images after verification; no copy in originals bucket | NN-04 |
| AD-05 | Auto-mask first eight digits in all derived text, search, previews, AI context and exports | s.29(4); NN-04 |
| AD-06 | "Revoke my Aadhaar verification data" with acknowledgement | AOV Regulations 2021 (R3 LG-028) [VERIFY] |
| AD-07 | Aadhaar logo and wording only as UIDAI permits; OVSE surrender duties planned (logs, grievances) | Regs 23A, 251A–253 (R3 LG-029) [VERIFY] |
| AD-08 | Face verification only inside the Aadhaar App; no liveness/biometric capture by LawDocs | R3 LG-029, LG-033–034; CH-17 |
| DL-01 | DigiLocker Requester onboarding by senior authorised representative; explicit, purpose-specific consent per fetch | DigiLocker Requester ToU cl.2, 4(c)–(d), 6(b) (R3 LG-038) |
| DL-02 | Store URI + verification result by default; copy only for a recorded user purpose after NeGD confirmation; nothing outside India | ToU cl.4(d), 6(b), 18 (R3 LG-038); NN-42 |
| DL-03 | Incidents and breaches involving DigiLocker data to NeGD within 24 hours | ToU cl.4(e), 13 |
| DL-04 | Annual audit by a CERT-In-empanelled auditor | ToU cl.14–15 |
| DL-05 | No use by affiliates or sister products without NeGD written approval; no scraping | ToU cl.5, 17; CH-16 |
| DL-06 | Vault named "Legal Vault"; never presented as a DigiLocker or DLSP | DL Rules 2016 (R3 LG-036); CH-15 |
| ES-01 | eSign only through a licensed ESP under LawDocs' own ASP arrangement (direct or via an aggregator whose structure is verified, D-12); never sublet to tenants or sister products | CCA eSign FAQ (R3 LG-007); NN-06 |
| ES-02 | Versioned signer consent screen per document on a LawDocs-hosted page; consent and logs held by the ASP of record for the route (`asp_mode`: the contracted aggregator acting as ASP, or LawDocs' own ASP arrangement — NN-06 as amended, X-15), with LawDocs retaining its evidence copies; never sublet or offered to another product as a provider (X-05) | eSign API v2.1 consent rules (R3 LG-006–007) |
| ES-03 | One SHA-256 hash per request of the final locked PDF; unique transaction ID; timestamp window; PKCS7 with chain, revocation and timestamp | R3 LG-006 |
| ES-04 | Second ESP integrated within one month of the first; multi-ESP failover | eSign API v3.3 (R3 LG-008) [VERIFY applicability through aggregator] |
| ES-05 | Nightly ESP licence-expiry check; block routing to an ESP whose CA licence has lapsed until renewal evidence is recorded (two ESPs shown expiring 15 May 2026 and **26 Oct 2026** — re-check before any Wave 1 signing go-live) | CCA ESP list (R3 LG-005) |
| ES-06 | eSign evidence retained ≥ 7 years after the later of signing and account closure (longer where limitation requires) | eSign API v3.3 (R3 LG-008); Limitation Act (LG-092) |
| ES-07 | Application login (AAL2) before the eSign step; certificate class shown on the signature panel | CCA eSign FAQ (R3 LG-009) |
| ES-08 | Instrument eligibility gate before any signing request (First Schedule exclusions) | IT Act First Schedule as amended 26 Sep 2022 (R3 LG-003); NN-07 |
| ES-09 | DSC: Class 3 only; local signing agent via PKCS#11; private key never leaves the token; chain and revocation validated | R3 LG-011 [VERIFY] |
| ST-01 | eStamp only through authorised channels per State; duty passed through at actuals; fee disclosed separately | R3 LG-100; NN-08, NN-22 |
| ST-02 | Certificate UIN verified and linked to the document hash; stamp before sign | NN-08 |

---

## P.7 Logging, monitoring and retention

| Log class | Content | Store | Floor | Default |
|---|---|---|---|---|
| ICT/system logs (app, infra, WAF, IdP, DNS, VPN) | Events with opaque IDs; no PII values | India log store (ap-south-1), immutable copy in `ld-log-archive` | 180 days in India (CERT-In Directions dir. (iv); R3 LG-079) | 400 days |
| Personal-data processing logs | Access to personal data, decrypts, exports | Same | 1 year (DPDP Rule 6(e) / 8(3); R3 LG-065) from 13 May 2027; applied now | 400 days hot, 8 years cold for access log |
| Audit ledger and access log | `core.audit_events`, `core.access_log` | PostgreSQL + Object Lock exports | 8 years | 8 years (tenant may lengthen) |
| eSign evidence logs | Consent, request/response, codes, txn IDs | Originals bucket (Object Lock) | 7 years after later of signing and account closure (R3 LG-008) | 8 years or limitation + buffer |
| Security monitoring | GuardDuty, Security Hub, SIEM detections | `ld-security` | 1 year | 400 days |
| Cerbos decision logs (privileged) | Decision ID, policy version | India log store | 1 year | 400 days |

**Monitoring.** OpenTelemetry pipeline with PII scrubbing (NN-32); SIEM export (India-resident); detections for: impossible travel and new-device sign-in on privileged roles; mass downloads or exports; repeated authorisation denials; break-glass use; grant use outside business hours (tenant-configurable alert, not a block); OTP abuse; KYB quota abuse; AI tool-call anomalies; ledger verification failures; ESP/eStamp provider errors and licence-expiry alerts. NTP synchronised to NIC/NPL-traceable sources (CERT-In dir. (i); NN-27).

---

## P.8 DPDP programme (NN-26)

**Timeline (R3 LG-061–062).** Act definitions and Board provisions from 13 Nov 2025; consent-manager provisions (s.6(9), Rule 4) from **13 Nov 2026**; main obligations (ss.3–17 incl. notice, consent, safeguards, breach, children, SDF, rights; Rules 3, 5–16) from **13 May 2027**; IT Act s.43A omitted from 13 May 2027 (SPDI Rules 2011 apply until then — R3 LG-075). A proposed acceleration was consulted on in Jan 2026 and not notified as at the latest source [VERIFY before launch]. `dpdp.commencement_date` is a governed parameter so any change ships as a rule-pack update. **LawDocs builds to the full regime from day one.**

**P.8.1 Roles.** LawDocs (the operating entity) is **data fiduciary** for individuals' Personal workspaces, account data of all users, leads, visitors and Consumer Help customers (the Consumer Help entity is a separate fiduciary, D-06); **data processor** for company tenants' content (s.8(2) contract; R3 LG-072), with a DPA template; **joint or independent fiduciary analysis** for counterparty data in agreements (the user who uploads a counterparty's details is the fiduciary for that purpose; LawDocs processes on the user's behalf for the signing ceremony and as fiduciary for the guest's own account and evidence trail) [COUNSEL].

**P.8.2 Notices (s.5; Rule 3).** Itemised notice per purpose set, standalone, in English and launch languages (any Eighth-Schedule language on request — s.5(3) [VERIFY]); purposes, data items, how to withdraw, how to exercise rights, how to complain to the Board; versioned (`ntv_`), reviewer of record `PLT_DPO`, maker-checker publication; re-consent on material change (P01 FR-P01-54).

**P.8.3 Consent (s.6).** Free, specific, informed, unconditional, unambiguous, affirmative, per purpose; no bundling; no pre-ticked boxes (E-Commerce Rules — R3 LG-141); withdrawal as easy as giving (s.6(4)); consent ledger with proof; consent-manager adapter from 13 Nov 2026 (flag-gated) (P01 FR-P01-52–56).

**P.8.4 Legitimate uses (s.7).** Recorded per processing activity in the ROPA (e.g., voluntarily provided data for the service the user asked for; employment purposes in client HRMS — processed for the client) [VERIFY clause letters; R3 LG-064].

**P.8.5 Rights (ss.11–14; Rule 14).** Access, correction and erasure, grievance, nomination; response ≤ 90 days by Rule 14(3), internal SLA 30 days (`kyc.rights.internal_sla_days`); company-tenant content requests forwarded to the tenant (processor role); nomination implemented as nominee release (P01 FR-P01-49–51).

**P.8.6 Retention and erasure (s.8(7); Rule 8).** Retention schedule per record type in `docs/data/retention-schedule.md` (generated from the export map and settings): erase when the purpose ends unless law requires retention or a legal hold applies; pre-erasure notice of 48 hours applied voluntarily to inactive accounts (Rule 8 applies it to Third-Schedule classes — R3 LG-065); inactive-account rule (P00 FR-P00-68 for migrated users; P04 for vault). Erasure workflow writes a ledger event without the erased content; backups age out per schedule; originals under Object Lock past the retention end are deleted by lifecycle at expiry.

**P.8.7 Breach (s.8(6); Rule 7).** Intimate affected principals and the Board without delay; detailed report to the Board within 72 hours (extendable on request) (R3 LG-065); runbook in §P.16.

**P.8.8 Children and persons needing a guardian (s.9; Rules 10–11).** Accounts 18+; ward profiles under guardians with evidence; no tracking, behavioural monitoring or targeted advertising of children; DigiLocker age token adapter from 13 May 2027 (R3 LG-040, LG-066) (P01 FR-P01-46–48).

**P.8.9 Records, DPIA and SDF readiness (s.10; Rule 13).** Records of processing (`docs/privacy/ropa.md`: activity, purpose, basis, data classes, principals, recipients, transfers, retention, safeguards, owner); DPIA before launch of: identity verification, AI drafting and agents, document intelligence on handwriting/screenshots, Consumer Help, marketplace professional sharing, ecosystem sharing, credential vault, mobile offline cache. **Designed as if a Significant Data Fiduciary**: DPO based in India, annual independent data audit, periodic DPIA, algorithmic risk assessment of Vidhi (R3 LG-067) [VERIFY Rule 13 content] — LawDocs may be notified as an SDF given the volume and sensitivity of legal data [INTERP].

**P.8.10 Transfers (s.16; Rule 15).** India hosting by default; transfers allowed except to restricted countries notified by the Government; transfer register entries for any processing outside India (e.g., Anthropic first-party API for **public, non-personal** content only — D-14, NN-15) with minimisation, no-training and zero-retention terms; customer-sector checks (regulated clients may forbid any transfer) [VERIFY current regional processing options of providers].

**P.8.11 Processor obligations (company tenants).** DPA template points: instructions, confidentiality, security measures (this appendix), sub-processor list and notice of changes, assistance with rights and breaches, processor-to-client breach notice ≤ 2 hours of detection [REC], return and deletion at exit (P20 export), audit rights (PROVIDER_ASSURANCE room, Ecosystem Spec §4.7), India residency.

**P.8.12 Penalties (Schedule).** Up to ₹250 crore (failure of security safeguards), ₹200 crore (breach notice; children), lower amounts for other duties (R3 LG-071 [VERIFY rows]) — recorded in the risk register; never used in marketing claims (NN-36).

---

## P.9 IT Act, intermediary duties and CERT-In

**P.9.1 Intermediary status.** LawDocs hosts user content and service listings, so it acts as an intermediary for that content and must meet due diligence to keep safe harbour (IT Act s.79; R3 LG-081); features in which LawDocs itself sells legal services do not enjoy that defence (Madras HC 2024; R3 LG-113).

**P.9.2 IT Rules 2021 as amended 2026** (R3 LG-077–078) [VERIFY post-2026 text]:

| Duty | LawDocs implementation |
|---|---|
| Rules, privacy policy and user agreement published; users reminded every three months (r.3(1)(c)) | Quarterly in-app reminder of terms; reminders logged |
| Takedown on court or government order within 3 hours (r.3(1)(d)) | 24×7 on-call legal-ops rota; takedown workflow with evidence; applies to public content, listings, public share pages |
| Grievance Officer; acknowledge within 24 hours, resolve within 7 days (r.3(2)(a)(i)) | Brand-specific Grievance Officer page; `PLT_GRIEVANCE_OFFICER` queue with clocks; stricter of IT Rules and E-Commerce Rules applies (P01 FR-P01-58) |
| Prohibited-content complaints within 36 hours; intimate imagery within 2 hours | Priority classes in the grievance queue |
| Synthetically generated information: label AI-generated audio/visual content, provenance metadata, refuse unlawful SGI including false documents (r.2(1)(wa), r.3(3)) | Vidhi text drafting is outside SGI; AI voice, avatars and generated images are labelled with visible labels, audio prefix and metadata; refusal rules for fake official records |

**P.9.3 CERT-In Directions (28 Apr 2022; R3 LG-079–080).** Report specified incidents within **6 hours** of noticing (NN-27); point of contact registered (operating entity, D-08); NTP sync; ICT logs 180 days in India; annual comprehensive audit by a CERT-In-empanelled auditor (also required by DigiLocker ToU cl.14–15) [VERIFY applicability of the 2025 audit guidelines].

**P.9.4 Other IT Act provisions.** s.43A/SPDI Rules until 13 May 2027 (privacy policy, consent for SPDI including passwords, reasonable security — R3 LG-075); s.66C and s.72A awareness in staff training and in the credential-vault design (R3 LG-076).

---

## P.10 Foreign privacy triggers (CH-18)

| Law | Trigger | LawDocs response |
|---|---|---|
| EU GDPR | Offering services to, or monitoring, people in the EU (Art. 3(2)) (R3 LG-084) | No EU targeting at launch; jurisdiction flag `EU_RESIDENT` (self-declared or derived from billing address) switches on the GDPR notice, SCC-based transfer terms, Art. 33 72-hour controller breach clock and, at volume, an Art. 27 representative |
| UK GDPR / DPA 2018 | Same territorial test (R3 LG-085) [VERIFY Data (Use and Access) Act 2025 changes] | Same flag `UK_RESIDENT` |
| CCPA/CPRA | Revenue threshold, ≥ 100,000 consumers/households, or ≥ 50% revenue from selling/sharing PI (R3 LG-086) [VERIFY current figures] | Thresholds unlikely at launch; LawDocs never sells or shares PI for cross-context behavioural advertising; no ad-tech pixels on authenticated pages (NN-35) |

Controls are built once (DPDP-first, GDPR-grade): notices, consent, rights, DPIA, breach workflow, processor terms; flags only change notices, clocks and representatives.

---

## P.11 PCI DSS position (CH-19; NN-22)

- **Design:** all card payments on Razorpay-hosted checkout through the Operations Hub OH8 billing engine (D-02, D-11); LawDocs servers never receive, process, store or log card data; tokenisation by the payment aggregator (RBI card-on-file rules — R3 LG-146 [VERIFY]).
- **Scope target:** **PCI DSS v4.0.1 SAQ A** (Jan 2025 revision: requirements 6.4.3 and 11.6.1 removed from SAQ A; merchants confirm the site is not susceptible to attacks from scripts that could affect the payment page — R3 LG-148) [VERIFY with PCI SSC documents and the acquirer]. Whether a given Razorpay integration mode (redirect, hosted page, iframe or JavaScript overlay) qualifies for SAQ A rather than SAQ A-EP must be confirmed with Razorpay and the acquirer before go-live [VERIFY]; prefer the mode that keeps every payment-page element served by the PSP.
- **Controls on LawDocs pages that redirect to or embed checkout:** CSP with strict `script-src`; Subresource Integrity on any third-party script; script inventory with owner and justification; change detection on the payment-referring pages; signed webhooks verified and payment status fetched server-side before an order is marked paid (Ecosystem Spec §13.3); MFA for any admin who can change checkout configuration (OH8 side).
- **Attestation:** annual SAQ A with the acquirer through OH8; LawDocs copy says "LawDocs never sees or stores your card details" (§P.0).

---

## P.12 Control set and framework mapping

Legend: SOC 2 TSC (CC = Common Criteria; A = Availability; C = Confidentiality; PI = Processing Integrity; P = Privacy); ISO/IEC 27001:2022 Annex A controls; 27701 = ISO/IEC 27701 PIMS; 42001 = ISO/IEC 42001:2023 AIMS; 22301 = ISO 22301:2019 BCMS; DPDP; CERT = CERT-In Directions. Mapping is indicative and confirmed by the readiness assessor [REC].

| ID | Control | Phase | SOC 2 | ISO 27001:2022 | Other | Evidence (automated unless noted) |
|---|---|---|---|---|---|---|
| SC-01 | Information security and privacy policy set approved annually | Owner; P04 hosts | CC1.1, CC5.3 | 5.1 | 27701, 42001 | Policy versions, approvals (manual) |
| SC-02 | Roles, responsibilities, SoD | P02, App. D | CC1.3, CC5.1 | 5.2, 5.3 | 42001 | SoD rules, violation report |
| SC-03 | Asset and service inventory | P23 | CC6.1 | 5.9 | — | Inventory export |
| SC-04 | Data classification and labelling | P00 | C1.1 | 5.12, 5.13 | 27701 | Data-catalogue CI result |
| SC-05 | Access control policy, Cerbos, least privilege | P01, P02 | CC6.1–CC6.3 | 5.15, 5.18, 8.3 | — | Policy tests, decision logs |
| SC-06 | Strong authentication, passkeys, step-up | P01 | CC6.1 | 5.17, 8.5 | — | MFA coverage report |
| SC-07 | Joiner-mover-leaver (staff SCIM; tenant SCIM) | P01, OH10 | CC6.2 | 5.16, 6.5 | — | JML reconciliation |
| SC-08 | Access reviews | P02 | CC6.2, CC6.3 | 5.18 | — | Campaign evidence packs |
| SC-09 | Privileged access, break-glass, session recording | P00, P02 | CC6.1, CC6.3 | 8.2, 8.18 | — | Break-glass reports |
| SC-10 | Tenant isolation | P00 | CC6.1, C1.1 | 8.3 | — | NN-01 results |
| SC-11 | Encryption and key management | P00, §P.5 | CC6.1, CC6.7 | 8.24 | PCI 4 (scope) | KMS config, rotation status |
| SC-12 | Secure SDLC, code review, CODEOWNERS | P00, P23 | CC8.1 | 8.25–8.28 | 42001 | PR approvals sample, rulesets |
| SC-13 | Security testing (SAST, SCA, DAST, secrets, IaC) | P00, P23 | CC7.1, CC8.1 | 8.29 | — | Pipeline results |
| SC-14 | Change management, CAB linkage | P23, OH13 | CC8.1 | 8.32 | — | Change ↔ deployment reconciliation |
| SC-15 | Vulnerability and patch SLAs | P23 | CC7.1 | 8.8 | — | SLA report |
| SC-16 | VAPT by CERT-In-empanelled auditor | P23, §P.14 | CC4.1, CC7.1 | 8.8, 5.35 | CERT | Reports (manual) |
| SC-17 | Secure configuration baselines | P00, P23 | CC7.1 | 8.9 | — | Security Hub score |
| SC-18 | Malware protection for uploads | P00 | CC6.8 | 8.7 | — | AV freshness |
| SC-19 | Logging, monitoring, 180-day India logs, NTP | P00 | CC7.2 | 8.15–8.17 | CERT | Retention probe, NTP probe |
| SC-20 | Incident management and notification clocks | P23, §P.16 | CC7.3–CC7.5 | 5.24–5.28, 6.8 | CERT, DPDP | Incident register, tabletop reports |
| SC-21 | Backup and restore testing | P00, P23 | A1.2, A1.3 | 8.13 | 22301 | Weekly restore evidence |
| SC-22 | Business continuity and DR (ap-south-2) | P23 | A1.2, A1.3 | 5.29, 5.30, 8.14 | 22301 | DR drill reports |
| SC-23 | Capacity and performance | P23 | A1.1 | 8.6 | — | Capacity reports |
| SC-24 | Supplier and sub-processor management | §P.15 | CC9.2 | 5.19–5.23 | 27701; DPDP s.8(2) | Vendor reviews, DPAs |
| SC-25 | Separation of environments; synthetic non-prod data | P00 | CC8.1 | 8.31, 8.33 | — | Provider-routing guard tests |
| SC-26 | Network security and segmentation; egress allow-list | P00 | CC6.6 | 8.20–8.22 | — | Config snapshots |
| SC-27 | Secure deletion and retention | P04, P20 | C1.2, P4.2 | 8.10, 5.33 | DPDP s.8(7) | Erasure logs |
| SC-28 | Data masking (Aadhaar, PAN, contacts) | P00, P05 | C1.1 | 8.11 | Aadhaar s.29(4) | NN-04 tests |
| SC-29 | Data-leakage controls on exports and shares | P04, P20 | C1.1 | 8.12 | — | Export audit |
| SC-30 | Tamper-evident audit ledger and anchors | P00 | CC7.2, PI1.4 | 8.15, 5.28 | — | Chain verification results |
| SC-31 | Processing integrity of deterministic engines (eligibility gate, stamp duty, DoA, deadlines) | P03, P08 | PI1.1–PI1.5 | 8.27 | — | Golden-case suites |
| SC-32 | Privacy notice, consent and withdrawal | P01 | P1.1, P2.1, P3.1 | 5.34 | 27701; DPDP ss.5–6 | Consent ledger reports |
| SC-33 | Data-principal rights handling | P01 | P5.1, P5.2 | 5.34 | 27701; DPDP ss.11–14 | Request SLA report |
| SC-34 | DPIA and ROPA | §P.8 | P1.1, CC3.2 | 5.34 | 27701; DPDP s.10 | DPIA register (manual) |
| SC-35 | Children and guardians | P01 | P3.1 | 5.34 | DPDP s.9 | Age-assurance logs |
| SC-36 | Aadhaar and DigiLocker handling (§P.6) | P01 | C1.1, P4.1 | 5.31, 5.34 | Aadhaar Act; DigiLocker ToU | NN-04/NN-42 tests; NeGD audit |
| SC-37 | eSign ASP obligations (§P.6) | P08 | PI1.2, CC9.2 | 5.31 | CCA eSign | ESP licence monitor; evidence packs |
| SC-38 | AI governance: model registry, evaluation, human gates, kill switches, no training | P09 | CC3.2, CC8.1 | 5.1, 8.25 | 42001 Annex A [VERIFY clause mapping] | Eval results, kill-switch tests |
| SC-39 | Agent controls: maker-only, sponsors, autonomy ceilings, tool allow-lists | P09 | CC6.1 | 5.15 | 42001 | NN-43 tests |
| SC-40 | Claims governance | P21, OH14 | CC2.3 | 5.36 | — | Claims-gate log |
| SC-41 | Security awareness and role training (staff; professionals' platform rules) | OH10 | CC1.4, CC2.2 | 6.3 | 42001 | Training records (OH) |
| SC-42 | Background screening of staff with privileged roles | OH10 | CC1.4 | 6.1 | — | Screening records (OH, manual) |
| SC-43 | Remote working and endpoint security for staff | OH, P23 | CC6.8 | 6.7, 8.1 | — | Device-compliance reports (no surveillance, NN-33) |
| SC-44 | Payment-page integrity (SAQ A) | P17, OH8 | CC6.6 | 8.26 | PCI SAQ A | Script inventory, CSP reports |
| SC-45 | Intermediary due diligence and grievance clocks | P21, P01 | CC2.3 | 5.31 | IT Rules 2021 | Grievance SLA report |
| SC-46 | Accessibility gates (WCAG 2.2 AA, IS 17802) | P21, P23 | — | 5.31 | RPwD Act | axe and manual test reports |

---

## P.13 Certification roadmap and evidence model

| Step | Timing [REC] | Prerequisites | Output |
|---|---|---|---|
| Readiness assessment (external) | Wave 1 GA − 2 months | SC-01…SC-46 implemented or with dated plans; policies drafted (§P.18) | Gap report |
| PCI DSS v4.0.1 SAQ A | Before paid launch | Hosted checkout; eligibility confirmed | Self-assessment with acquirer |
| CERT-In-empanelled comprehensive audit | Before DigiLocker go-live, then annually | — | Audit report (also satisfies DigiLocker ToU) |
| SOC 2 Type 1 (Security, Availability, Confidentiality; Processing Integrity for signing and eligibility engines; Privacy optional) | Wave 1 GA + 2 months | Gaps closed; system description | Type 1 report |
| ISO/IEC 27001:2022 Stage 1 → Stage 2 | GA + 3–6 months | ISMS operating ≥ 3 months; internal audit; management review | Certificate |
| SOC 2 Type 2 (first window 6 months) | Starts after Type 1 | Evidence collectors running | Type 2 report |
| ISO/IEC 27701 | After 27001 | PIMS operating | Certificate [VERIFY current edition and transition rules] |
| ISO/IEC 42001:2023 | When Vidhi agents are material (Wave 2) | AI management system, impact assessments | Certificate |
| ISO 22301:2019 | On enterprise or regulated-client demand | BCMS operating, DR drills | Certificate |

**Evidence model.** `eng.controls` (SC-ID, owner, frequency, framework mappings) and `eng.control_evidence` (control, period, collector, artefact URI in the originals bucket, SHA-256, reviewer, status). Collectors run on schedule: CI results, policy tests, access-review packs, MFA coverage, JML reconciliation, backup restore tests, NTP and log-retention probes, chain verification, ESP licence monitor, VAPT tickets and SLA reports, grievance and rights SLA reports, claims-gate logs. Each collected item emits `ControlEvidenceCollected` to OH14 (Ecosystem Spec §6.29) with hashes only; auditors access evidence through a `PROVIDER_ASSURANCE` grant to the OH14 room — never through tenant data (Ecosystem Spec §4.7).

---

## P.14 VAPT plan

| Item | Plan |
|---|---|
| Auditor | CERT-In-empanelled organisation, rotated at least every three years; independence declaration |
| Cadence | Before each wave's go-live (P23 gate); annually; after any major change to authentication, authorisation, cryptography, signing, payments or AI agents; after a Sev-1 incident |
| Method | Grey-box with test accounts per role (Appendix D); source-assisted review for `iam`, `kyc`, `sgn`, `cvl`, `packages/authz`, `packages/crypto`, `packages/audit` |
| Scope | Web apps (public, web, delivery, console), APIs incl. partner, SCIM and webhooks, mobile apps (OWASP MASVS L2 + resilience), cloud configuration review (AWS CIS benchmark), Keycloak and Cerbos configuration, ingest and converters (fuzzing), AI gateway and agents (OWASP LLM Top 10 red-team: prompt injection via documents, data exfiltration through tools, excessive agency) |
| Mandatory test cases | Cross-tenant (IDOR/BOLA) on every endpoint family; SoD bypass attempts; approval digest bypass; grant expiry; break-glass; guest-link replay; Aadhaar data exposure through OCR/search/export; DigiLocker caching; signing evidence tampering; stamp-certificate reuse; payment webhook spoofing; open redirects; SSR leakage of private content |
| Remediation SLAs | Critical (or CISA KEV-listed/exploited) 72 hours; High 7 days; Medium 30 days; Low 90 days — from triage (Ecosystem Spec §13.3); retest by the auditor; exceptions only with a dated compensating control approved by `PLT_SECURITY_OFFICER` |
| Outputs | Full report (restricted); executive summary for the client assurance pack; findings tracked in P23 with SC-16 evidence |

---

## P.15 Vendor risk and sub-processor register (initial)

**Tiering.** Tier 1 — processes tenant content, identity artefacts or signatures (cloud, ESP/aggregator, eStamp, KYB, AI): security questionnaire, SOC 2/ISO reports or equivalent, DPA, India-residency evidence, breach-notice clause (≤ 24 hours to LawDocs), right to audit, exit plan, annual review. Tier 2 — contact data or metadata (SMS, email, WhatsApp): DPA, DLT/TCCCPR compliance, residency finding, annual review. Tier 3 — no personal data: standard terms.

| Sub-processor / recipient | Purpose | Data classes | Region | Tier | Notes |
|---|---|---|---|---|---|
| Amazon Web Services | Hosting, storage, KMS, Bedrock inference | All | ap-south-1 / ap-south-2 | 1 | Bedrock India profiles for confidential classes [VERIFY model availability] |
| eSign aggregator (Leegality / Digio / Melento-type) and ESPs | Aadhaar eSign, DSC flows | Signer identity, document hash, evidence | India [VERIFY] | 1 | ASP structure verified per D-12; licence-expiry monitor (ES-05) |
| eStamp provider (aggregator / SHCIL channel) | e-stamp procurement | Party names, consideration, instrument data | India [VERIFY] | 1 | State coverage registry (P08) |
| KYB vendor (MCA data) primary + secondary | Company discovery | Entity data, director names/DIN | India [VERIFY] | 1 | Lawful-sourcing warranty |
| GSP | GSTIN search | Public taxpayer data | India | 2 | — |
| GLEIF | LEI lookup | Public data | Global (public) | 3 | No personal data sent |
| NeGD DigiLocker / Entity Locker | Issued documents | Identity documents (by consent) | India | Recipient (government service) | Requester ToU obligations (§P.6) |
| UIDAI | — | None sent (offline verification is local) | — | — | OVSE obligations only |
| SMS/voice CPaaS (JioCX or other DLT-registered) | OTP, notices | Mobile, message content (templates) | India | 2 | DLT; NN-34 |
| Meta WhatsApp Business Platform (direct or BSP) | Optional OTP and utility messages | Mobile, template content | [VERIFY] | 2 | Opt-in; never for legal notices or recovery (R6 D-31) |
| Email (Amazon SES / Brevo) | Transactional email | Email, message content | India (SES ap-south-1) / [VERIFY Brevo] | 2 | Marketing via OH only with consent |
| Operations Hub (Infrabyx group entity) | CRM, billing (OH8), support, directory | Business contacts, commercial records, aggregates | India | Intra-group | Intra-group DPA; never tenant content (NN-19) |
| Razorpay (via OH8) | Payments, Subscriptions, Route | Payer details (at PA), order references | India | 1 (group) | PA Directions (R3 LG-145) |
| Anthropic (first-party API) | Public, non-personal content tasks only | PUBLIC class | Outside India [VERIFY] | 2 | Transfer register entry; no customer data (NN-15) |
| Google / Microsoft | Sign-in; optional workplace connectors (user-initiated) | Identity claims; files the user chooses | Per provider | 2 | Minimal scopes (P19) |
| Observability vendor (if not self-hosted) | Telemetry | Scrubbed logs | India required | 1 | [VERIFY] |
| Court-data and trademark data vendors (P11, P12) | Case and mark status | Case numbers, party names | [VERIFY] | 1 | Two vendors for courts (R6) |

The register lives in `docs/privacy/sub-processors.md`, is mastered with OH14 and published on the trust page; customers are notified 30 days before a new Tier 1 sub-processor is added [REC].

---

## P.16 Incident response and notification matrix

**Severity.** Sev-1 (confirmed breach of personal data or tenant content; signing/evidence integrity compromise; widespread outage), Sev-2 (contained security event; partial outage), Sev-3 (minor). Triage ≤ 30 minutes for Sev-1 (Ecosystem Spec §13.3); incident commander from `PLT_SECURITY_OFFICER` rota; legal and DPO engaged for any personal-data event.

| Event | Who LawDocs notifies | Clock | Channel | Content |
|---|---|---|---|---|
| Specified cyber incident affecting LawDocs systems | CERT-In | ≤ 6 hours of noticing (R3 LG-079) | CERT-In reporting format | Per Directions annexure |
| Personal-data breach where LawDocs is fiduciary (individuals, Consumer Help customers via that entity) | Data Protection Board and affected principals | Without delay; detailed Board report ≤ 72 hours (DPDP Rule 7; R3 LG-065) | Board's mechanism [VERIFY]; email, SMS, in-app | Nature, extent, timing, likely consequences, mitigation, safety steps, contact |
| Breach affecting a company tenant's data (LawDocs as processor) | Tenant owners, admins and privacy contact | ≤ 2 hours of detection [REC] | Phone tree, email, in-app security notice | Facts the fiduciary needs for its own notices; updates by sequence number |
| Incident involving DigiLocker-sourced data or the Requester integration | NeGD | ≤ 24 hours (ToU cl.4(e), 13) | As NeGD prescribes | Per ToU |
| Incident involving eSign keys, consent logs or ESP integration | ESP / aggregator per the ASP agreement; CCA where required | Per contract [VERIFY] | Contract channel | — |
| Incident involving Aadhaar offline-verification artefacts | UIDAI where the OVSE terms require; affected holders | [VERIFY under OVSE regulations] | — | — |
| Payment-related compromise | Razorpay/acquirer via OH8 | Per PA/acquirer terms | OH8 | — |
| EU/UK personal data where LawDocs is controller | Supervisory authority | 72 hours (GDPR Art. 33) | Authority portal | — |
| Regulated client's service affected (e.g., an NBFC using LawDocs) | Client; the client notifies its regulator, never LawDocs (Ecosystem Spec §13.3) | ≤ 2 hours | As above | — |
| Group product affected | Product owners via OH13 | ≤ 2 hours | OH13 incident | Counts and classes only |
| Service outage without data impact | Affected tenants | Status page ≤ 30 minutes (Sev-1/2) | status.lawdocs.in, in-app banner | Status and next update |

Runbook `docs/runbooks/incident.md`: detection → triage → containment (kill switches, key revocation, session revocation, grant suspension) → evidence preservation (ledger, logs, Object Lock snapshots) → notification clocks started automatically from the declared time → eradication and recovery → RCA within 10 working days → lessons learned → closure with SC-20 evidence. Tabletop exercises quarterly (one per year covering a DigiLocker incident and one covering signing-evidence integrity).

---

## P.17 Secure SDLC and AI security

- **SDLC:** threat model per phase; ASVS mapping; CODEOWNERS; branch protection; SAST (CodeQL, Semgrep with LawDocs rules), SCA (osv-scanner, Trivy), secrets (gitleaks), IaC (checkov, tflint), container scanning, DAST on staging, fuzzing of converters; SBOM per release; signed images and provenance; licence policy; no production data outside prod/mig; developers without standing production data access (P00, P23).
- **AI security** (OWASP Top 10 for LLM Applications [VERIFY edition]): prompt-injection defences (provenance tags on retrieved and uploaded content, instruction hierarchy, tool allow-lists, output validation); sensitive-information controls (permission-filtered retrieval, data-class routing to Bedrock India, scrubbers, no customer data to non-India endpoints — NN-15); excessive agency limits (per-action human confirmation for irreversible actions — NN-13; scoped tool tokens; budgets; kill switches — NN-39); supply chain of models (model registry, version pinning, evaluation before switching providers — D-14); misinformation controls (citation resolver, unverified labels, "AI draft — not reviewed by a professional" — NN-14); SGI labelling for audio/visual outputs (IT Rules 2026; R3 LG-078); disclosure of AI use to users per the Anthropic Usage Policy for high-risk legal use [VERIFY current text and effective date — R4].
- **Evaluation:** per-agent evaluation sets and red-team suites in CI (P09); thresholds block release; model, prompt or provider changes are REGULATED changes (P23).

---

## P.18 Policy set (owner to write; hosted in the Legal Vault of the platform tenant)

Information security policy; acceptable use; access control and privileged access; identity and authentication; cryptography and key management; secure development; change and release management; vulnerability and patch management; logging and monitoring; incident response and breach notification (with the §P.16 matrix); business continuity and disaster recovery; backup and restore; supplier and sub-processor management; data classification and handling; data retention and disposal (with the generated schedule); privacy notice and policy (DPDP, SPDI until May 2027, GDPR overlay); data-principal rights procedure; children and guardians procedure; Aadhaar handling procedure (offline verification only, masking, revocation); DigiLocker Requester procedure; eSign ASP operations manual (consent, logs, ESP failover, licence monitoring); eStamp procedure; AI use and AI governance policy (ISO/IEC 42001-aligned); staff acceptable AI use; content moderation, takedown and grievance policy (IT Rules); claims and marketing-substantiation policy (NN-20, NN-36); professional-rules compliance policy (BCI, ICAI, ICSI; NN-21); Consumer Help ethical-wall policy (NN-23); remote working and endpoint policy (no surveillance, NN-33); HR security (screening, training, offboarding — OH10); risk management; internal audit; management review; records of processing and DPIA procedure.

---

## P.19 Client assurance pack and trust page

**Trust page (public):** data location statement; security overview; sub-processor list; status page link; responsible-disclosure policy and security contact (`security.txt`); privacy notice; Grievance Officer and DPO details per operating entity; certification and attestation status in §P.0 wording only, gated by OH14.

**Assurance pack (under NDA, company and regulated clients):** architecture and data-flow diagrams; encryption and key management summary; access control, SoD and grant model summary (Appendix D extract); audit-ledger and Correction Entry design; residency statement; BCP/DR summary with latest drill result; latest VAPT executive summary; incident notification commitments (≤ 2 hours to clients); DPA template; standard questionnaire answers (SIG Lite/CAIQ-style [REC]); SOC 2 report or ISO certificate when issued; right-to-audit procedure through a `PROVIDER_ASSURANCE` grant (Ecosystem Spec §4.7).

---

## P.20 Open items

| ID | Item | Owner |
|---|---|---|
| OI-P-01 | ASVS 5.0 chapter numbering and L3 requirement mapping | Security engineer (P00) |
| OI-P-02 | Razorpay checkout mode qualifying for SAQ A vs SAQ A-EP; acquirer confirmation | [OWNER] with OH8 |
| OI-P-03 | DPDP acceleration status and Rule 13 SDF content before launch | [COUNSEL] |
| OI-P-04 | OVSE incident and surrender obligations under the 2025 amendment regulations | [COUNSEL] |
| OI-P-05 | ESP licence status (two CCA list entries expiring 15 May 2026 and 26 Oct 2026) at signing go-live | Tech lead (P08) |
| OI-P-06 | Applicability of CERT-In 2025 audit guidelines; empanelled auditor selection | [OWNER] |
| OI-P-07 | Counterparty data role analysis (fiduciary vs processor) for agreements | [COUNSEL] |
| OI-P-08 | Bedrock India model availability and data-retention terms; Anthropic first-party API region | Tech lead (P09) |
| OI-P-09 | Brevo and WhatsApp data residency findings | Tech lead |
| OI-P-10 | ISO/IEC 27701 current edition and transition | Readiness assessor |

---

## P.21 Sources (accessed 25 October 2026 unless stated)

- R3 Legal and Regulatory Baseline: LG-001–014 (eSign), LG-021–034 (Aadhaar), LG-036–041 (DigiLocker), LG-046–060 (closed data), LG-061–072 (DPDP), LG-075–081 (IT Act, IT Rules, CERT-In), LG-084–086 (GDPR/UK/CCPA), LG-091–092 (evidence, limitation), LG-100 (eStamp), LG-111–117 (professional rules), LG-133–137 (accessibility), LG-141–149 (consumer, payments, PCI, telecom).
- Infrabyx Ecosystem Integration Specification v1.1: §4.2, §4.6, §4.7, §6.14, §6.29, §13.2, §13.3.
- LawDocsComply Pack v1.2 Appendix Q (structure and control-set pattern; reference only).
- OWASP ASVS 5.0; OWASP MASVS; OWASP Top 10 for LLM Applications [VERIFY editions]; AICPA Trust Services Criteria (2017, revised points of focus 2022) [VERIFY]; ISO/IEC 27001:2022 Annex A; ISO/IEC 27701; ISO/IEC 42001:2023; ISO 22301:2019; PCI DSS v4.0.1 SAQ A (Jan 2025 revision) [VERIFY].
