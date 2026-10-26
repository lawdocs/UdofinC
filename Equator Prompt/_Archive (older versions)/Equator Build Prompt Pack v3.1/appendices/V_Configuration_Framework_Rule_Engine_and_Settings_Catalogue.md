# Appendix V — Configuration Framework, Rule Engine and Settings Catalogue (v3.0, 23 October 2026)

> **Binding** for P15 (Configuration Studio and tenant settings) and for the v3 addenda in §V.7 (P00, P02, P05, P07, P08, P09, P13, P14). Consumed by P16–P21 and by every v3 appendix that declares settings (W, X, Y, Z, AA, AB, AC, AD, AE).

## V.0 Purpose, sources, precedence

**Purpose.** Equator serves third-party organisations (lenders, insurers, employers, universities, Private ADR Chambers, group companies) and works under laws that regulators change often. This appendix makes every open, interim or externally dependent item **configurable**, so that:
- routine changes are made by the tenant's own administrators or delegated users without a super admin;
- legal and safety values stay governed (NN-33);
- nothing changes silently, and every case keeps the rules it was filed under (NN-21).

It defines:
- the three-tier model and the test for placing a value in a tier (§V.1);
- the Governed rule engine (§V.2);
- the configurability classification of all 469 Appendix J items (§V.3);
- the Settings Catalogue for every persona and module (§V.4);
- the settings UX (§V.5);
- the data model, APIs, events, errors, RBAC and audit (§V.6);
- phase addenda (§V.7).

**Sources.**
- Pack: master §3 (NN-21, NN-33 to NN-40) and §6 (customisability); P00 FR-P00-26 to FR-P00-43 (feature flags, Ruleset Studio, Legal Rules Register); Appendix G §G.1 (fail-safe activation), §G.3 and §G.4 (lifecycle, propagation); Appendix J §J.5 and §J.6 (dispositions, closure rule); Appendix O §5 (billing settings); Appendix S §6 and §7 (RBAC, delegation, common settings).
- v3 siblings and their settings catalogues: Appendix W (chambers; §W.8), X (Operations Platform; §X.13; grievance packs §X.8.3), Y (marketing; §Y.12), Z (HRMS, payroll, controls; parameter seed §Z.2.4–§Z.2.6, settings §Z.15; rule packs in `cfg`, read model `pay.rule_params`, X-56 split of maker-checker engines), AA (marketplace categories as rule packs; §AA.15), AB (revenue stream registry; §AB.8), AC (`cfg.system_of_record`, `cfg.field_mappings`, `cfg.workspace_connections` and the other `cfg` tables listed in §AC.15; settings §AC.17), AD (group companies; §AD.16), AE (CODEOWNERS for rule-pack seeds, §AE.2.6; audit-evidence catalogue, §AE.8.1).
- Research: [RC] design implications A (payroll rule-pack architecture, change-watch feed), C (statutory floor versus company policy), G (what stays OFF or locked); [RD] DI-H (governed, configurable and OFF); [RE] (directory, marketplace and group-data guardrails); [RB] (revenue switches).

**Precedence.**
1. Master NN rules.
2. Appendix G, on the legal status of any rule.
3. This appendix, on:
   - the tier of a value;
   - key naming;
   - scope and inheritance;
   - the change pipeline.
4. The owning appendix, on the detailed settings of its domain (W, X, Y, Z, AA, AB, AC, AD, AE).

If two files give a value different tiers, the **stricter tier applies** until the conflict is resolved under X-45.

**Requirements, decisions and cross-file resolutions introduced here**

| ID | Statement |
|---|---|
| R-44 | Three-tier configuration (NN-33) with a Configuration Studio. Routine tenant changes need no super admin; legal and safety values are governed (brief §1). |
| R-45 | Every Appendix J open item is classified by configurability, with tier, key or rule pack, who may change it and its default or fallback (Expanded Prompt; brief §1). |
| R-46 | A complete settings catalogue for every user type and module, showing what each user can change unaided (brief §2). |
| R-47 | A Governed rule engine with jurisdiction and domain rule packs, effective dating, sandbox testing, impact analysis, rollback, review alerts and a regulatory-watch feed (brief §1: "regulators change rules"). |
| D3-10 | **One configuration plane.** The `cfg` schema holds setting definitions, values, scopes, locks, setting packs and rule-pack metadata. Physical rule-pack versions stay in `core.rulesets` / `core.ruleset_versions` (P00) as config kind `rule_pack`, so PinSets work unchanged. `core.config_change_requests` remains the single approval engine for configuration (X-56). Tier T changes apply immediately through `cfg.setting_changes`, with audit and one-click rollback. |
| D3-11 | **Registry before use.** No code may read a setting or flag that is not registered in `cfg.setting_definitions` with a tier, scope list, type, bounds, default, fallback, owner role and audit class. CI fails on an unregistered read (`CFG_UNREGISTERED_KEY`). |
| D3-12 | **Tenant rule-pack adaptation.** A tenant may adopt a platform pack, adapt it within its overlay bounds (stricter, or inside published ranges), or author tenant contractual rules for its own contracts. It may never relax a statutory or platform floor. An adaptation that affects third parties' legal rights needs the tenant's named `legal_reviewer` (a qualified advocate or in-house counsel, recorded) and carries the tenant-rule disclosure (§V.2.11). |
| D3-13 | **Configured fallback is mandatory.** Every Governed definition declares a fallback. It applies automatically, and visibly, when the rule is unverified, unapproved, past its review date or unavailable. There is never a "no rule" state (§V.2.10). |
| D3-14 | **No super-admin dependency.** `platform_admin` cannot change a tenant's T or tenant-scope G values, except inside a tenant-granted, time-limited support session (≤ 72 h, logged, visible to the tenant). Routine G changes are made by the named functional roles (legal reviewer, CFO, DPO, Company Secretary), not by `platform_admin`. |
| X-43 | **Ruleset Studio and Configuration Studio.** The P00 Ruleset Studio becomes the **Rules and legal** area of the Configuration Studio (P15); its screens SCR-P00-07 onwards are kept and re-skinned. P00 risk classes map to tiers: `standard` → T or G-standard, `elevated` → G-elevated, `legal` → G-legal. L values are not editable in any studio; they change only by a platform release with an ADR and Head of Legal approval (Appendix AE). |
| X-44 | **Key naming and aliases.** Canonical keys follow `<scope>.<module>.<key>`; rule packs follow `rulepack.<jur>.<domain>.<name>@<version>`. Legacy flag names in P00 to P14 and Appendix J (e.g., `fam.s15_prelit`, `wrk_ir_s42_voluntary_arbitration`, `legal.mediation.statutory_mode`) are registered as aliases in `cfg.setting_aliases`. Reads resolve alias → canonical; new code uses canonical keys. A key written in any appendix without a scope prefix (e.g., `marketplace.paid_placement`, `directory.public_professionals`, `mkt.brevo.enabled`, `iam.leaver_revoke_hours`, `billing.eco_withholding`) is registered under its canonical scoped form (`platform.` when `allowed_scopes` is platform only; otherwise the broadest allowed scope, as `tenant.` is implied in §V.4.1), and the written form becomes an alias. Two legacy names for one concept share one canonical key (e.g., `tax.eco_tds` → `billing.eco_withholding`; `tax.eco_gst_tcs` → `billing.eco_gst_tcs`). Legal flags keep `core.feature_flags` as their store (P00), wrapped by a G-tier definition. Release and experiment flags (Unleash) are not tenant settings. |
| X-45 | **Conflict resolution.** The ordering is: L > case PinSet (NN-21) > emergency block > platform G rule > tenant G within bounds > T, with the merge strategy declared per definition (§V.1.4). On a tier disagreement between files, the stricter tier holds until the Head of Legal and CTO record the resolution in this appendix. |
| X-46 | **Open items link to configuration.** `core.open_items` (P00 v2.1) gains `config_category`, `tier`, `cfg_key`, `rule_pack`, `changed_by` and `fallback_text` from §V.3. Closing an item opens a G change request that moves the key from its fallback to its final value. The P14 go-live checklist reads launch gates from both tables. Appendix O §5 and Appendix S §7 remain the screen specifications for billing and personal settings; §V.4 is their index. |

---

## V.1 The three-tier model (NN-33)

### V.1.1 Tiers

| Aspect | **L — Locked** | **G — Governed** | **T — Tenant** |
|---|---|---|---|
| What | Platform guardrails: NN rules, statutory exclusions, safety, security baselines, the neutrality firewall, sealed-data rules, India data region | Legal or regulatory parameters and rule packs: clocks, rates, thresholds, fee schedules, eligibility, mandatory disclosure text, routes, legal flags, vendor integration settings, tax treatment, money controls | Routine operational settings: labels, branding, queues, SLA targets above floors, templates' non-legal text, notification preferences, saved views, custom fields, team structure |
| Who may change | Nobody in the product. Changed by a platform release with an ADR, a passing `NN-*` test and Head of Legal approval (Appendix AE) | Authorised role within platform-defined bounds (§V.4). Platform values: the platform functional owner. Tenant values: the tenant's authorised role; with the tenant `legal_reviewer` when third parties' legal rights are affected | Tenant admin or a delegated user, within the scope delegated |
| Path | Code, migration, release | `core.config_change_requests` (maker ≠ checker; preview; effective date; citation; review date) | `cfg.setting_changes` (immediate; optional tenant-imposed approval) |
| Effect | Next release | At `effective_from` (≥ 24 h lead for `legal` risk class; ≥ 7 days where party-facing notice text changes, unless `urgent_effective` (§V.2.5); 0 for others) | Immediately (≤ 60 s cache) |
| Pinning (NN-21) | n/a | Pinnable kinds are pinned to the case at filing | Not pinned, unless the definition is marked `case_pinned` (e.g., a status-label set used in a served notice) |
| Rollback | Release revert | New change request restoring a prior version | One click; restores the previous value; audited |
| UI badge | 🔒 **Locked** (grey) | ⚖ **Governed** (amber) + "needs approval by …" | ✎ **Tenant** (green) |

### V.1.2 Decision test (apply in order; first "yes" wins)

| # | Question | If yes |
|---|---|---|
| Q1 | Does the value implement an NN rule, a statutory exclusion or prohibition, a safety or security baseline, the neutrality firewall, or a sealed-data rule, so that changing it could make conduct unlawful or unsafe? | **L** |
| Q2 | Does it move money, change a fee, price, refund, payee, bank detail or authority limit, or grant a privileged role (NN-36)? | **G** (elevated; maker-checker always) |
| Q3 | Does it derive from a law, regulation, regulator direction, judgment, tax rule or professional rule, **or** affect a third party's legal rights, deadlines, eligibility, notices or data (clock, threshold, disclosure text, route, retention)? | **G** (legal) |
| Q4 | Does it depend on an external fact not yet confirmed (vendor capability, regulator registration, commencement, Board approval)? | **G**, with the dependent flag **OFF** and a configured fallback. If no runtime behaviour depends on it (a citation or a documentation note), it is **N — not configurable; closes on external evidence** |
| Q5 | Is it operational and reversible, affecting only the tenant's own users and processes without changing anyone's legal rights? | **T** |

**Tie-breaks.**
- If in doubt, choose the higher tier.
- A value with a legal floor and a tenant margin is split. The **floor is G** (or **L** where an NN rule fixes it); the tenant's choice above the floor is T, validated against the floor ("bounded T"). Examples:
  - the contact window (NN-12 fixes the 08:00–19:00 floor, so the floor is L; the tenant may narrow it);
  - leave policy (statutory floor; tenant policy may be more generous);
  - retention (statutory minimum; tenant may keep longer).
- Values used in a served notice, award or settlement are pinned to the case once used.

**Worked examples**

| Value | Tier | Why |
|---|---|---|
| Arbitration of matrimonial status | L | NN-06 exclusion |
| No paid placement in the institutional neutral directory | L | NN-34 |
| Keystroke logging for staff | L (OFF, cannot enable) | NN-35; [RC] D-22 |
| POSH 90-day inquiry clock start | G-legal | Statute silent; counsel item J-047 |
| EPF wage ceiling | G-legal (`rulepack.IN.payroll.epf`) | Statutory; Appendix Z |
| Stamp duty matrix per State | G-legal (`rulepack.IN-<ST>.stamp.duty_matrix`) | NN-09; LG-14 |
| Gupshup callback authentication mode | G-platform integration | Vendor dependency; CTO |
| Payout approval threshold | G-elevated | NN-36 |
| Ticket first-response SLA (stricter than statutory) | T | Internal target above the G floor |
| Status labels, queue names, logo, colours | T | Operational; contrast validated |
| Respondent marketing exclusion | L | NN-16 |
| Bar Council roll lookup per State | G-platform, flag OFF | Needs the Council's written permission (LG-11) |

### V.1.3 Scope hierarchy, inheritance, override and "locked by parent"

```
platform  (Equator platform baseline; one)
  └─ group   (a group of companies, e.g. Infrabyx; Appendix AD; optional)
      └─ tenant  (an organisation: institution, chambers, enterprise, grm_client, university, academy)
          └─ unit    (department, office, team, programme or GRM variant inside a tenant; tree)
              └─ user    (personal preferences only)
```

| Rule | Statement |
|---|---|
| Allowed scopes | Each definition lists `allowed_scopes`. L definitions have only `platform`. G definitions list where a value may be set, e.g., `platform` for a statutory pack and `tenant` for a contract-specific adaptation. User scope is limited to personal preferences (language, accessibility, notification channels within tenant policy). |
| Inheritance | The resolved value is the value at the most specific scope that has one. If no scope has a value, the definition default applies. Unit trees inherit from parent units. |
| Override | Allowed only where the scope is in `allowed_scopes`, the value is within `bounds` and the parent has not locked it. An override records the overriding scope, actor, reason (mandatory for G) and expiry (optional). |
| Locked by parent | Any administrator at a parent scope may lock a T value for all children: e.g., a group locks the MFA policy for every group tenant; a tenant locks quiet hours for all units. Children then see "🔒 Locked by {scope} ({role}, {date})" and a **Request change** button that opens an approval item for the locker. Platform bounds on G values are locks on a range: children choose inside it. |
| Narrow-only and widen-only | A definition may declare `child_direction` = `narrow_only` (e.g., the contact window), `raise_only` (e.g., QA sample rate, retention) or `lower_only` (e.g., attempt caps). The validator enforces it against the parent's resolved value. |
| Group scope (NN-38) | Group-scope values may set policy (security, branding kits, HR policy templates) but never grant data access. Cross-company data access is a `grp` grant, not a setting. |
| Deletion of a scope | Removing a unit re-parents its overrides to the parent after an admin confirms the diff; overrides are never silently dropped. |

### V.1.4 Precedence and conflict resolution

**Resolution order (per read)**
1. **L** platform value.
2. **Case PinSet** (NN-21), for pinnable kinds when a case context exists.
3. **Emergency block** (Appendix G §G.4.2), if one is active for the key.
4. **Platform G** rule-pack value applicable to the case's jurisdiction, dispute type and date.
5. **Tenant G** adaptation within bounds.
6. **T** value at the most specific scope.
7. Definition default.
8. Declared fallback (§V.2.10), if steps 1 to 7 yield an unverified, unapproved or overdue value.

**Merge strategies** (declared per definition as `merge_strategy`)

| Strategy | Used for | Rule |
|---|---|---|
| `most_specific` | Labels, templates, branding | The deepest scope wins |
| `strictest` | Clocks, thresholds, caps, deposits | Direction comes from `protective_direction` (`lower`, `higher`): the most protective value among applicable scopes and packs wins |
| `intersection` | Allowed windows, allowed channels, allowed IP ranges, enabled mechanisms | Only what every applicable layer allows |
| `union` | Block lists, blackout dates, quiet hours, prohibited phrases, mandatory disclosures | Everything any layer requires |
| `longest` | Retention, cooling-off periods | The longest applicable; legal hold overrides deletion |
| `additive` | Tags, custom fields, saved views | Combined; the child cannot delete a parent item, only hide it from its own views |

**Multiple rule packs on one case** (e.g., Central and State labour packs; a platform pack and a tenant contractual rule):
- protective rules are cumulative;
- for computational rules, the pack whose `applicability` predicate is most specific to the case wins (State over Central where State law governs; the tenant contractual rule only where it is stricter);
- if two computational rules tie, the engine refuses with `CFG_RULE_CONFLICT` and opens a task for the `legal_reviewer`. The case uses the fallback until the conflict is resolved.

---

## V.2 The Governed rule engine

### V.2.1 Rule packs

A **rule pack** is a versioned, citable bundle containing:
- rules (enforcement points HB, W, C, D, S or CFG; Appendix G §G.1);
- typed parameters;
- an applicability predicate (jurisdiction, sphere, dispute types, party classes, dates);
- a golden-case suite;
- a declared fallback.

Its identity is `rulepack.<jur>.<domain>.<name>@<YYYY.N>`:
- `jur` ∈ `IN`, `IN-<ST>` (ISO 3166-2:IN), `INTL`, or a country code;
- `YYYY.N` is the Nth approved version in a year.

Each rule cites one or more `core.legal_rules` rows by `rule_code`. A pack cannot activate if a cited row's status or verification forbids it (§V.2.4).

**Rule-pack catalogue (seed)**

| Domain | Packs (examples) | Owns | Owner → checker | Seed status |
|---|---|---|---|---|
| Labour (disputes) | `IN.labour.codes` (IR Code, Code on Wages, Social Security and OSH Code dispute parameters: GRC clocks, s.53 settlements, tribunal and EC dates, retrenchment divisor, settlement forms), `IN-<ST>.labour.grc_forms`, `.settlement_forms`, `.se_termination`, `IN-<ST>.labour.gig_workers` (e.g., `IN-RJ`); legacy flag `wrk_ir_s42_voluntary_arbitration` | WRK routing, GRC clocks, s.42 forms, s.53 dates, retrenchment calculators | Legal counsel → Head of Legal | Central verified (J-001, J-061); State forms watch (J-104) |
| Payroll and HR | `IN.payroll.wage_definition`, `.epf`, `.esi`, `.gratuity`, `.bonus`, `.leave`, `.maternity`, `.income_tax`, `.hours`, `.min_wage`, `.thresholds`; `IN-<ST>.payroll.professional_tax`, `.lwf`, `.se_hours`, `.se_leave`, `.min_wage`, `.holidays` (pack map: Appendix Z §Z.2.4) | Wage base, contributions, TDS, leave floor, gratuity, maternity (also read by WRK calculators: one home per parameter) | Payroll Compliance Officer (`compliance_officer` with responsibility `payroll_compliance`) → Company Secretary or `finance_controller`, with legal-reviewer sign-off where employees' statutory rights are affected (Appendix Z §Z.2.4, §Z.2.6) | Mixed VERIFIED / SECONDARY_ONLY / NOT_CONFIRMED [RC A-4] |
| POSH | `IN.posh.act` (inquiry clock start and other POSH Act clocks; IC composition validation) | POSH tenant clocks and validators (sealed store) | Legal counsel → Head of Legal | Inquiry clock start counsel item (J-047); `conservative_value` fallback |
| Education grievance | `IN.edu.grievance` (UGC and AICTE timelines, equity cell) | University GRM variant | Legal counsel → Head of Legal; tenant `legal_reviewer` for "Equator target" labels | AICTE days tenant-adaptable (J-069) |
| Exclusions and signposts | `IN.exclusions.*` (matrimonial status, BNSS s.514, Waqf s.83, IP registry relief, PWDVA counselling), `IN.signposts.*` (HIV Act, Whistle Blowers Act, National Sports Tribunal) | Intake blocks and signposting (NN-06) | Exclusions: platform release only (L); signposts: Legal counsel → Head of Legal | Exclusions live; signposts provisional |
| Realty and procurement | `IN-<ST>.realty.rera_interest`, `.rera_limitation`; `IN-<ST>.procurement.state_adoption` | Informational interest and limitation; public-procurement signposting | Legal counsel → Head of Legal | No figure for unverified States (J2-136) |
| Payments | `IN.payments.card_data` | No card data stored (NN-31) | Platform release only (L) | Live |
| RBI conduct | `IN.rbi.conduct` (contact window, recovery conduct, grievance, doc release, CIC codes), `IN.rbi.rbios`, `IN.rbi.p2p`, `IN.rbi.card_directions`, `IN.rbi.gold_loans` | FIN contact guard, signposting, compensation calculators | Legal counsel → Head of Legal | LR-RBI-005 corrected (J-056) |
| SEBI | `IN.sebi.odr` (SMART ODR fees, clocks, panel segregation) | SEC connector | Legal → Head of Legal | Flag OFF (J-116, J-137) |
| IRDAI | `IN.irdai.conduct` (Ombudsman caps, centre map, health MC lint, portability TATs) | INS eligibility and letters | Legal → Head of Legal | Provisional (J2-181) |
| Clocks | `IN.clocks.calendars` (working-day calendars, General Clauses Act counting, leap-day rule), plus clocks inside each domain pack | Clock engine (Appendix A §6) | Legal → Head of Legal | Verified core; State holiday lists provisional |
| Stamp duty | `IN-<ST>.stamp.duty_matrix`, `.family_instruments`, `.s33_restamp`, `.arbitral_affidavits`, `IN-ST.stamp.estamp_coverage` | e-stamp calculator and routing (NN-09) | Legal → Head of Legal | DL and RJ OFF (LG-14) |
| Consumer | `IN.consumer.cpa`, `IN.consumer.ecommerce_rules`, `IN.consumer.dark_patterns` | Signposting, billing controls (Appendix O §6) | Legal → Head of Legal | Comply by default (J-109) |
| Privacy | `IN.privacy.dpdp`, `IN.privacy.spdi_dpdp_dual`, `IN.privacy.it_rules`, `INTL.privacy.gdpr`, `.uk_mode`, `.uae_pdpl`, `.ccpa_mode` | Lawful basis, notices, rights SLAs, breach clocks, retention (NN-15, NN-30) | DPO → Head of Legal | DPDP build-to-full; foreign modes conditional |
| Telecom | `IN.telecom.tcccpr` (A2P declarations, CLI hygiene, DLT templates), `IN.telecom.number_series` | Voice and SMS guards (NN-12) | Telecom counsel → Head of Legal | Own-DID calls OFF (LG-03) |
| Arbitration, mediation, conciliation | `IN.arbitration.acta`, `IN.mediation.med_act`, `IN.conciliation.acta_p3` | Clocks (s.29A, s.34), consent awards, statutory-mode flag (NN-05) | Legal → Head of Legal | Mediation statutory mode OFF |
| Family and succession | `IN.family.personal_law`, `IN.family.succession`, `IN-<ST>.family.*`, `IN-UK.family.ucc` | FAM calculators, forum maps, exclusions | Legal → Head of Legal | UCC OFF (J2-160) |
| Insolvency, corporate, MSME | `IN.insolvency.ibc`, `IN.corporate.s442_track`, `IN.msme.msmed` | COM routes, withdrawal windows, MSEFC readiness | Legal → Head of Legal | MSEFC referral OFF (LG-08) |
| Tax | `IN.tax.gst_it` (SAC, rates, ECO TDS and TCS, treaty relief, PAN rules) | Billing and payouts (Appendix B) | CFO → tax adviser | Memo pending (LG-12) |
| International | `IN.intl.s44b_territories` (A&C Act s.44(b) notified territories), `INTL.intl.s74_cross_border`, `INTL.intl.saudi_arbitrator_qual` and other seat qualification rules, Singapore Convention status | INT gates (NN-19) | Legal → Head of Legal | Watch (J-145) |
| Court formats | `IN.court.formats.<profile>`, `IN.court.jurisdiction_rules`, `IN-<ST>.court.*` | Exports and bundles (X-34) | Legal → Head of Legal | SC verified; others unverified |
| Professions and marketplace | `IN.professions.bci`, `rulepack.IN.mkp.category.<code>` (Appendix AA) | Display policy, directory, category law checks (NN-34, NN-39) | Legal → Head of Legal | Advocate public search OFF |
| Grievance | `rulepack.IN.grievance.*` (Appendix X, EOP-L12) | Statutory grievance and DPDP request clocks | Grievance Officer → Head of Legal | Floors locked |

### V.2.2 Lifecycle

`draft → review → approved → scheduled → active → superseded → retired`, with side exits `rejected` and `withdrawn`. These map onto the P00 statuses as follows:

| V.2 state | `core.ruleset_versions.status` |
|---|---|
| `review` | `submitted`, then `in_review` |
| `retired` | New value added by the §V.7 P00 addendum: law repealed or pack withdrawn; never deleted |

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| draft | submit | Schema and semantic validators pass. Every rule cites ≥ 1 `rule_code`; source SHA-256 on file. Golden suite present (≥ 1 case per rule). Fallback declared. `next_review_due` set | review | Notify checkers; event `equator.cfg.rule_pack.submitted.v1` |
| review | approve | Checker ≠ maker. Step-up (aal2, ≤ 10 min). Approvals met (§V.2.3). Preview run within 24 h is green. Impact analysis attached | approved | Audit |
| review | reject / request changes | Reason ≥ 20 characters | rejected / draft | Notify maker |
| approved | schedule | `effective_from` > now (≥ 24 h for `legal`) | scheduled | `ConfigActivationWorkflow` timer |
| scheduled | activate | Validators re-run green; cited rules still eligible | active | Old version → superseded; cache bust; event `…rule_pack.activated.v1`; propagation per mode (§V.2.5) |
| active | supersede | Newer version activated | superseded | Pins unaffected |
| active | retire | Approver = Head of Legal; reason; replacement or explicit "none" | retired | Dependent flags forced OFF; affected definitions fall back (§V.2.10) |
| draft / review / approved / scheduled | withdraw / cancel | Maker, or a checker with `config:approve` | withdrawn | Audit; a scheduled timer is cancelled |

### V.2.3 Approvals by effect class and scope

| Effect (Appendix G §G.1) | Platform pack | Tenant adaptation (within bounds) |
|---|---|---|
| `protective` (blocks, warns, discloses, signposts) | Maker `legal_ops` → checker `legal_reviewer` | Tenant maker → tenant `legal_reviewer`; platform not required |
| `computational` (rates, thresholds, formulas, clocks) | Maker → `legal_reviewer` → owning function (CFO, CS, DPO or Payroll Compliance Officer per domain) | Tenant maker → tenant `legal_reviewer`; values must sit inside platform bounds |
| `permissive` (enables a mechanism, route, claim or fee) | Maker → `legal_reviewer` → **Head of Legal**. Cited rules must be `VERIFIED` and `IN_FORCE` or `PARTIALLY_IN_FORCE` | Not allowed; tenants cannot enable a permissive rule that the platform has not activated |
| `emergency_block` | Head of Legal + `platform_admin`; effective immediately; post-incident review within 5 working days | Not allowed (a tenant may raise an urgent request) |

Money-related packs (fees, payouts, refunds, tax) also follow NN-36. The approver appears in the authority matrix (`ctl`) for the amount band.

### V.2.4 Citations and verification

- Rules cite `core.legal_rules` rows. Parameters carry `verification_status`:
  - `VERIFIED` — primary source;
  - `SECONDARY_ONLY` — maps to Appendix G `VERIFY_PENDING`;
  - `NOT_CONFIRMED` — no adequate source.
- A parameter's status may never be higher than its cited rule's verification (Appendix Z precedence 2).
- **Fail-safe activation** (Appendix G §G.1) is enforced by the validator:
  - `protective` rules may activate while `SECONDARY_ONLY`;
  - `computational` rules may activate while `SECONDARY_ONLY` only if every output is labelled "indicative — figure under legal verification", and, for payroll, a named Payroll Compliance Officer acknowledges each run [RC A-3];
  - `NOT_CONFIRMED` parameters block finalisation;
  - `permissive` rules need `VERIFIED`.
- The citation lint blocks unverified serial numbers, paragraph numbers and G.S.R. numbers in party-facing text (LG-16). Party-facing text cites by instrument title and date until verified.

### V.2.5 Effective dating and future-dated rules

- Every version has `effective_from` and an optional `effective_to`. Future-dated versions sit in `scheduled`. Several can be queued, e.g., a Budget change from 1 April and a State PT change from 1 July.
- **Intra-period splits.** When a parameter changes inside a wage, billing or clock period, the engine pro-rates on a calendar-day basis by default, with a per-parameter override (the EPF ceiling split of 17 Sep 2026 is the golden test) [RC A-2].
- **Transitional rules.** A version may declare `applies_to` = `events_on_or_after` (default), `cases_filed_on_or_after` or `instruments_executed_on_or_after`, and can carry an explicit transition table (e.g., pre-2024 health policies: J2-187, dual computation).
- **Propagation modes** (Appendix G §G.4.2):
  - `prospective` (default);
  - `open_cases_with_notice` (impact list, case tasks, party notice, recorded pin override);
  - `emergency_block`.
- Owned statutory clocks are never shortened silently (NN-04).
- **Lead times:**
  - legal packs: ≥ 24 h between approval and activation;
  - packs that change party-facing notices: ≥ 7 days, unless the law takes effect sooner, recorded as `urgent_effective` with Head of Legal approval.

### V.2.6 Preview, sandbox and golden cases

- **Golden cases** live in `packages/rules/fixtures/rulepacks/<pack>/*.json`, seeded by CODEOWNERS (Appendix AE §AE.2.6), plus tenant-added cases stored in `cfg.golden_cases`. Each case gives inputs (facts, dates, amounts, jurisdiction) and expected outputs (route, clock dates, amounts, blocks, disclosures). Each rule must have ≥ 1 positive and ≥ 1 negative case.
- **Preview** runs the proposed and active versions side by side on the golden suite and produces a diff: changed routes, dates, amounts, newly blocked or unblocked actions. Preview is deterministic and side-effect-free: worker sandbox, no outbox, fake adapters only (FR-P00-42).
- **Sandbox tenant.** Each tenant can open a sandbox copy of its configuration with synthetic data (`is_synthetic = true`) and run its own scenarios. It never contains real case data, sealed data (NN-07) or personal data.
- **Pass rule.** All golden cases match expectations, or every mismatch is accepted by the checker with a reason (which then updates the expected output in the same change request).

### V.2.7 Impact analysis

On submit, and again before activation, `RulePackImpactWorkflow` lists:

1. **Tenants.** Tenants that adopted the pack, split into auto-follow and pinned. For pinned tenants, the deadline by which they must move.
2. **Cases.**
   - Open cases whose PinSet contains the superseded version (count by tenant, vertical, state).
   - Under `open_cases_with_notice`, each affected case and the change to its route or clocks (dry run).
3. **Future clock dates.** Dates that would shift, before and after.
4. **Dependants.** Templates, journeys, notices, calculators and settings that reference the changed rules.
5. **Flags.** Flags whose eligibility changes.
6. **Open items.** Open items (`core.open_items`) closed or opened by the change.

The report is attached to the change request. Tenant admins of affected tenants receive a digest; case managers receive per-case tasks only when the propagation mode requires action. The report contains IDs and counts only; it never contains party PII.

**Tenant "what changed" summary.** Submit is refused without a summary (`CFG_CHANGE_SUMMARY_REQUIRED`). It has four parts:
1. **Plain-language summary** (`change_summary_i18n`, en and hi, ≤ 120 words), written by the maker. The P15 `document_extractor` may draft it from the source; the maker edits and owns it, and the checker approves it with the version (NN-01).
2. **Parameter diff table**, generated automatically from `cfg.rule_params`: code, old value, new value, unit, verification status and citation.
3. **Tenant action**, one of `none`, `review_adaptation` (an overlay must be re-validated), `move_pin` (pinned tenants must move by {date}) or `configure` (a new tenant choice is needed).
4. **Tenant-specific counts** taken from the impact report: open cases pinned, clocks shifting and settings depending on the change.

The summary goes out at `scheduled` and again at `activated`, as a digest (`tenant.cfg.digest.rule_changes`), a "What changed" tab on SCR-P15-11 and a banner for tenant admins of adopting tenants. Where `tenant_action ≠ none`, a named tenant admin must acknowledge it (`cfg.pack_change_acks`). Unacknowledged items escalate to the tenant's `legal_reviewer` after 5 working days and appear on Configuration Health. *(v3.1)*

### V.2.8 Rollback

- **Configuration.** Rollback is a new change request whose content equals a prior version. It needs the same approvals, but preview is waived when restoring the immediately previous version within 7 days.
- **Effects.** Rollback never alters pinned cases. Effects that have already occurred are not undone automatically: a notice sent, a payslip finalised, an invoice issued. The rollback report lists them, and remediation is a business transaction under `ctl` (e.g., a supplementary payslip or a credit note).
- **Emergency rollback.** Head of Legal + `platform_admin`, effective immediately, with post-incident review.

### V.2.9 Review dates, regulatory watch and alerts

**Review dates**
- Default `next_review_due`: 180 days.
- Shorter cycles: 90 days for `SECONDARY_ONLY`; 30 days for `volatile` packs (Mediation Act commencement, DPDP phases, RBI conduct, TCCCPR, Labour Code rules).
- Alerts go out at T−14 days and T−0. On overdue: a banner in the Studio, the owner's dashboard turns red and the fallback rule (§V.2.10) applies to computational values used in new decisions.

**Regulatory-watch feed** (`cfg.reg_watch_items`)
- Sources: e-Gazette; RBI, SEBI, IRDAI, IFSCA, TRAI, MeitY, EPFO and ESIC circulars; MoLE and State labour notifications; Union and State Budgets; Supreme Court and five High Court judgment alerts; PRS bill tracker; vendor changelogs.
- Recurring calendar [RC A-5]:
  - VDA cycles (1 April, 1 October);
  - Union Budget (1 February);
  - State budgets (PT);
  - DPDP dates (13 Nov 2026, 13 May 2027);
  - RBC Third Amendment (1 Jan 2027);
  - TCCCPR declarations (17 Nov 2026).
- Each item is triaged within 5 working days to one of: `no_impact`, `draft_change` (opens a draft pack version), `open_item` (creates or updates a `core.open_items` row) or `flag_review`.
- Watch items in Appendix J (disposition `watch`) are linked rows. When the trigger fires, the item reopens automatically (Appendix J §J.6).
- **Rule and flag links** *(v3.1)*. Every Appendix G §G.4.3 trigger is a `cfg.reg_watch_items` row with `linked_rule_ids` (LR IDs) and `linked_flag_keys` (registered keys). When it fires (`fired_at` set by feed, manual entry or court-alert match): each linked rule gets `next_review_due = today` and an owner task (5 working days, escalating to the Head of Legal on day 6); each linked flag row in the Studio shows "Review due — law may have changed" with the source link; while the review is open a linked flag may be switched OFF but not ON (`CFG_FLAG_REVIEW_OPEN`, protective direction only, G §G.1). Test `CFG-RW-01`.

### V.2.10 Configured fallback (D3-13)

Every G definition and rule pack declares `fallback_kind`. The fallback applies automatically when:
- the value is unapproved;
- the cited rule is not eligible;
- the review is overdue;
- the provider or rule pack is unavailable.

| `fallback_kind` | Behaviour | Example |
|---|---|---|
| `last_approved` | Keep the last approved version; banner "under review" | Overdue review of a verified clock pack |
| `platform_baseline` | Use the platform value instead of the tenant adaptation | Tenant adaptation failed revalidation |
| `conservative_value` | Use the declared safe value | POSH clock from complaint receipt (J-047); wallet GST taxed at receipt (J-158) |
| `informational_only` | Show the figure or clock as information; never block or decide | `mact_6m` (J-060); RERA interest (J2-136) |
| `indicative_label` | Compute, labelled "indicative — under legal verification" | Retrenchment divisor (J-062) |
| `flag_off` | Feature OFF; manual or alternative route shown | `fam.s15_prelit`; `ESCROW_PORT`; `lookupBarRoll` |
| `manual_route` | Block automation and route to a named role with a task | Interstate differential stamp duty (J-091) |
| `block` | Hard block with reason and signposting | Permissive rule unverified |

The fallback in force is shown wherever the value is used. It is recorded in the case or event audit (`fallback_applied = true`, kind, reason) and counted on the Configuration Health dashboard (SCR-P15-14). Event: `equator.cfg.fallback.activated.v1`.

### V.2.11 Tenant adoption, adaptation and override (D3-12)

| Mode | What the tenant does | Who approves | Disclaimer shown to the tenant | Disclosure to counterparties |
|---|---|---|---|---|
| **Adopt — auto-follow** | Subscribes to a platform pack; new versions apply on their effective dates | Tenant admin (T action) | "This organisation follows Equator's {pack} as updated. Equator reviews it against the sources cited; it is not legal advice to your organisation." | None (platform rule) |
| **Adopt — pinned** | Stays on a version; must move within the platform's `max_pin_days` (default 90; 0 for a legal change binding pending matters) | Tenant admin | As above + "You are on an earlier version until {date}." | None |
| **Adapt within bounds** | Changes parameters on the pack's overlay allow-list, only in the stricter direction or inside published ranges (e.g., shorter internal SLA, longer cooling-off, narrower contact window, extra disclosures) | Tenant maker → tenant `legal_reviewer` (named, qualification recorded) if third parties' rights are affected; otherwise tenant checker | "Your adaptation is your organisation's policy. Equator's validators confirm it is within the platform's legal bounds; they do not review its suitability for your organisation." | Where an adaptation changes what a counterparty receives (e.g., a stricter deadline for the tenant's own response), it appears in the counterparty's process notice as "{Tenant} policy" |
| **Tenant contractual rule** | Authors rules for its own contracts (e.g., its grievance escalation matrix, internal appeal levels, programme eligibility) as a tenant pack `rulepack.T-<tenant>.<domain>.<name>` | Tenant maker → tenant `legal_reviewer` | "Tenant rule — authored and approved by {Tenant}; not reviewed by Equator." | Shown as "{Tenant} rule" with its version |
| **Override of a platform rule** | **Not permitted** where it relaxes a statutory or platform floor. A tenant that believes a platform rule is wrong raises a **rule challenge** (`cfg.rule_challenges`) with sources; Equator legal must respond within 10 working days | — | — | — |

### V.2.12 Relationship to Ruleset Studio (P00), legal rules (Appendix G) and NN-21

| Component | Role after v3 | Change |
|---|---|---|
| `core.rulesets` / `core.ruleset_versions` (P00) | Physical store of every pinnable configuration version, including rule packs (new kind `rule_pack`) | Status `retired` added; `effect` and `jurisdiction` columns via `cfg.rule_pack_meta` |
| `core.config_change_requests` (P00) | The only approval engine for G changes (X-56) | Gains `tier`, `scope_kind`, `scope_id`, `impact_report`, `fallback_kind` |
| `core.legal_rules` (Appendix G) | Source of truth for legal status and verification; rule packs cite it | Unchanged; activation validators read it |
| `core.feature_flags` (P00) | Store for legal flags and kill switches | Each flag gets a G definition in `cfg.setting_definitions`; alias table maps legacy names |
| PinSet (FR-P00-41) | Freezes rule-pack versions per case | Rule packs are pinnable. T settings are not pinned unless `case_pinned` |
| Ruleset Studio screens | "Rules and legal" area of the Configuration Studio | X-43 |
| `core.open_items` | Register of open items | Linked to `cfg` keys (X-46) |

---

## V.3 Configurability classification of the 469 Appendix J items

### V.3.1 Method

1. **Script draft.** `tools/cfg/classify_open_items.py` (kept in the repository) read the 469 register rows: `id`, `disposition`, `proposition`, `finding`, `residual`, `owner`, `approver`, `gate` and `recheck`. It drafted a category, tier, key, changer and fallback for each row:
   - category from the disposition, with keyword tests for commencement, documentation and tenant-operational wording;
   - tier from tests for exclusions and prohibitions (L), parameters (G) and labels or templates (T);
   - key from flag names in the gate text, `LR-<AREA>` codes or subject keywords;
   - changer from the owner.
2. **Review by judgment.** Every row was then reviewed. The review changed:

   | Field changed | Rows | Share of 469 |
   |---|---|---|
   | Category | 62 | 13% |
   | Tier | 120 | 26% |
   | Key | 382 | 81% |
   | Changed-by | 183 | 39% |

   Principles applied:
   - statutory exclusions, prohibitions, NN-linked blocks and copy lints stay **L**, even where the underlying item is a counsel question (the interim position is protective and is held in code);
   - rates, thresholds, clocks, forum maps and legal flags are **G**;
   - vendor endpoints, authentication modes and capability facts are **G platform integration settings** owned by the CTO;
   - tenant-supplied texts, calendars and labels are **T**;
   - citation-only and legend items, where no runtime behaviour depends on the answer, are **N**;
   - shared payroll and labour parameters (gratuity, bonus, leave encashment, maternity) have one home in `rulepack.IN.payroll.*` (Appendix Z), and WRK calculators read them.
3. **Loading.** The result is loaded into `core.open_items` (X-46: `config_category`, `tier`, `cfg_key`, `rule_pack`, `changed_by`, `fallback_text`). CI test `CFG-OI-01` fails if any open item lacks a classification, or if a G key in the table is not registered in `cfg.setting_definitions` (D3-11). CI test `CFG-OI-02` fails if one key carries two tiers in the register: where an item has a locked guard and a governed parameter, the guard has its own key (e.g., J-052 `IN.exclusions.agri_land_partition_arbitration` beside `fam_property_arbitration`).
4. **Review of 23 October 2026 (RVA).** Eight rows were re-tiered or re-keyed for consistency: J-052, J2-142 and J2-169 (locked guards given their own keys); J-159 (legacy `tax.eco_tds` mapped to `billing.eco_withholding`); J-168 (threshold item moved from L to G with a conservative fallback); J-170 (Equator's own particulars are platform scope); J2-028 (court exhibit series is a counsel-governed format, G tenant-adaptable); J2-115 (same key as J2-108, so T).

### V.3.2 Legend

| Column | Values |
|---|---|
| **Cat** | **SL** stable legal rule · **PC** pending commencement (or draft or stayed instrument) · **CI** counsel interpretation · **RV** regulator or vendor dependency · **PD** internal product decision · **TC** tenant-configurable value or workflow · **W** watch (no commencement event yet identified) |
| **Tier** | **L** Locked · **G** Governed · **T** Tenant · **N** not configurable: closes on external evidence or a documentation fix |
| **Key / rule pack** | Settings keys `<scope>.<module>.<key>` or legacy flag aliases (X-44). Keys beginning `IN.`, `IN-<ST>.`, `IN-RJ.`, `IN-GA.` or `INTL.` are rule packs `rulepack.<jur>.<domain>.<pack>[.<parameter>]@<current>`; `IN-ST` means one pack per State. Uppercase names are ports or guards from Appendix D or F. `—` = no key |
| **Changed by** | **REL** platform release only (ADR + Head of Legal; L) · **HL** Head of Legal (maker `legal_ops`, checker `legal_reviewer`) · **HL+DPO** · **HL+TC** Head of Legal with telecom counsel · **CTO** platform integration settings (security review) · **CFO+TAX** CFO with tax adviser · **CFO** · **CS** Company Secretary · **REG** Registrar · **PO** product owner · **BRD** Board · **MKT** marketing head via the Claims Register · **TLR** tenant `legal_reviewer` within platform bounds (G tenant-adaptable) · **TA** tenant admin |
| **Default / fallback** | The behaviour in force until the item closes (§V.2.10). "As J-nnn" refers to that row |

### V.3.3 Summary counts

| Category | L | G | T | N | Total |
|---|---|---|---|---|---|
| SL — Stable legal rule | 27 | 135 | 0 | 38 | 200 |
| PC — Pending commencement | 0 | 30 | 0 | 0 | 30 |
| CI — Counsel interpretation | 32 | 104 | 0 | 0 | 136 |
| RV — Regulator / vendor dependency | 1 | 45 | 0 | 0 | 46 |
| PD — Internal product decision | 3 | 21 | 0 | 13 | 37 |
| TC — Tenant-configurable value / workflow | 0 | 0 | 7 | 0 | 7 |
| W — Watch | 2 | 11 | 0 | 0 | 13 |
| **Total** | **65** | **346** | **7** | **51** | **469** |

| Appendix J disposition | L | G | T | N | Total |
|---|---|---|---|---|---|
| verified | 11 | 67 | 0 | 11 | 89 |
| corrected | 8 | 29 | 1 | 2 | 40 |
| provisional | 9 | 52 | 4 | 25 | 90 |
| counsel sign-off | 31 | 104 | 0 | 0 | 135 |
| vendor confirmation | 1 | 45 | 2 | 0 | 48 |
| product decision | 3 | 21 | 0 | 13 | 37 |
| watch | 2 | 28 | 0 | 0 | 30 |

| Changed by | Items |
|---|---|
| HL | 242 |
| CTO | 68 |
| REL | 65 |
| HL+DPO | 22 |
| CFO+TAX | 20 |
| TLR | 17 |
| PO | 15 |
| TA | 7 |
| MKT | 4 |
| CFO | 3 |
| HL+TC | 2 |
| REG | 2 |
| CS | 1 |
| BRD | 1 |

**Reading the counts.**
- **65 items are L.** Their interim positions are protective and are held in code. Examples: advocate profile limits (J-032), no borrower-payable fees in lender programmes (J-058), the s.29A scrutiny guard (J2-157), the IRDAI citation lint (J2-181). Counsel's answer can only *relax* them, by a platform release.
- **346 are G**, of which 17 are tenant-adaptable within bounds (TLR).
- **7 are T**. They are tenant-supplied values: chargeback windows (two rows), HFC escalation text (two rows), scheme limits, working calendar and invitation deemed-rejection days.
- **51 are N**: citations, legends and research notes. No runtime behaviour waits on them.
- **81 rows keep a feature OFF** until closure.

No item marked `permissive` can activate on secondary sources (§V.2.4).

### V.3.4 Register (469 rows)

| ID | Cat | Tier | Key / rule pack | Changed by | Default / fallback |
|---|---|---|---|---|---|
| J-001 | SL | G | `wrk_ir_s42_voluntary_arbitration` | HL | OFF until Form V template approved and State row verified |
| J-002 | SL | L | `ins_policy_suit_bar` | REL | Informational "contestable — likely void"; never a bar |
| J-003 | CI | G | `arb_appeal_tier_contractual` | HL | OFF in prod; s.34 warning on first-tier award |
| J-004 | SL | L | `ins_policy_suit_bar` | REL | As J-002 |
| J-005 | PD | N | — | CTO | Documentation legend only |
| J-006 | RV | G | `azure_docintel_centralindia` | CTO | OFF; Sarvam Vision primary |
| J-007 | SL | G | `platform.integrations.elevenlabs.base_url` | CTO | India residency URL only |
| J-008 | SL | G | `platform.integrations.sarvam.callback_auth` | CTO | Per-job token + status re-fetch |
| J-009 | SL | G | `platform.integrations.elevenlabs.test_api` | CTO | Agent Testing API |
| J-010 | SL | G | `platform.integrations.exotel.callback_auth` | CTO | Path token + Basic auth + IP list + re-fetch |
| J-011 | RV | G | `platform.integrations.gupshup.auth_mode` | CTO | Both modes in config; Meta Cloud API primary |
| J-012 | RV | G | `platform.integrations.gupshup.enabled` | CTO | OFF until contracted |
| J-013 | RV | G | `platform.integrations.gupshup.callback_auth` | CTO | Treat as unsigned; token + IP list + re-fetch |
| J-014 | SL | G | `platform.integrations.msg91.callback_auth` | CTO | Path token + IP list |
| J-015 | SL | G | `platform.integrations.msg91.correlation_field` | CTO | CRQID (≤ 52 alphanumerics) |
| J-016 | RV | G | `indiapost_api` | CTO | OFF; manual desk + barcode + POD upload |
| J-017 | SL | G | `platform.integrations.setu.esign_auth` | CTO | Headers as verified |
| J-018 | RV | G | `platform.integrations.digio.webhook_auth` | CTO | Status poll only |
| J-019 | SL | G | `IN-ST.stamp.estamp_coverage` | CTO | Uncovered State → physical stamping checklist |
| J-020 | RV | G | `platform.integrations.liveness.callback_auth` | CTO | Accept only after server-side fetch |
| J-021 | SL | G | `platform.integrations.cashfree.idempotency` | CTO | x-idempotency-key |
| J-022 | RV | G | `ESCROW_PORT` | CTO | OFF; direct-with-proof only |
| J-023 | RV | G | `platform.integrations.100ms.enabled` | CTO | OFF; LiveKit primary |
| J-024 | RV | G | `platform.ai.bedrock.citations_mode` | CTO | Equator span-anchoring; in.* profiles only |
| J-025 | RV | G | `azure_docintel_centralindia` | CTO | As J-006 |
| J-026 | W | G | `IN.arbitration.defensibility` | HL | "Supported, not settled"; no claim |
| J-027 | PC | G | `arb_statutory_ea` | HL | OFF; s.34A never called statutory |
| J-028 | CI | G | `tenant.i18n.legal_glossary.hi` | HL | hi-IN legal keys below legal_approved |
| J-029 | PD | G | `platform.identity.face_match_threshold` | CTO | No auto-reject; manual review / K3 |
| J-030 | RV | G | `lookupBarRoll` | CTO | OFF all States |
| J-031 | RV | G | `indiapost_api` | CTO | CSV/manual import |
| J-032 | CI | L | `profile_display_policy` | REL | advocate_restricted (BCI r.36 fields only) |
| J-033 | SL | G | `platform.integrations.razorpay.capture_window` | CTO | ≤ 3 days |
| J-034 | CI | G | `arb_appeal_tier_contractual` | HL | As J-003 |
| J-035 | RV | G | `ESCROW_PORT` | CTO | OFF; never labelled "escrow" |
| J-036 | SL | G | `IN-ST.stamp.estamp_coverage` | CTO | Contracted per-State matrix only |
| J-037 | RV | G | `indiapost_api` | CTO | OFF |
| J-038 | RV | G | `indiapost_api` | CTO | OFF |
| J-039 | RV | G | `connectors.ondc.enabled` | CTO | OFF |
| J-040 | W | G | `connectors.msme_odr.enabled` | CTO | Manual pack |
| J-041 | RV | G | `platform.integrations.esign.mobile_mode` | CTO | Browser tab; no WebView |
| J-042 | SL | G | `platform.mobile.min_os` | CTO | Per pinned Expo SDK |
| J-043 | SL | G | `platform.mobile.min_os` | CTO | Per pinned Expo SDK |
| J-044 | RV | G | `platform.integrations.esign.mobile_mode` | CTO | Browser tab only |
| J-045 | PD | N | — | CTO | Migration rehearsal blocked until export received |
| J-046 | CI | G | `consent_award_requested_post_settlement` | HL | OFF; Part III conciliation |
| J-047 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | complaint_receipt; never auto-close |
| J-048 | CI | G | `fam_property_arbitration` | HL | OFF; stamp-as-partition + registration task |
| J-049 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | As J-047 |
| J-050 | SL | G | `IN.payroll.gratuity.due_days` | HL | 30 days (informational clock) |
| J-051 | SL | G | `IN.labour.codes.grc_clocks` | HL | As verified |
| J-052 | CI | L | `IN.exclusions.agri_land_partition_arbitration` | REL | Blocked for agricultural land; `fam_property_arbitration` OFF (as J-066) |
| J-053 | CI | L | `IN.rbi.conduct.borrower_costs` | REL | No borrower cost-in-any-event clause |
| J-054 | SL | G | `IN-ST.stamp.family_instruments` | HL | "Estimate — confirm with Sub-Registrar"; DL/RJ OFF |
| J-055 | CI | G | `IN.privacy.dpdp.lawful_basis` | HL+DPO | s.17(1)(a) per purpose; no marketing to respondents |
| J-056 | SL | L | `FIN_CONTACT_WINDOW` | REL | 08:00–19:00 hard block; MFI 09:00–18:00 to 31 Dec 2026 |
| J-057 | CI | G | `IN.rbi.conduct.offer_relay` | HL | NN-12 on all FIN contacts; lender number only |
| J-058 | CI | L | `IN.rbi.conduct.borrower_fees` | REL | No borrower-payable fee in lender programmes |
| J-059 | CI | G | `IN.irdai.conduct.ombudsman_cap` | HL | ombudsman_capped warning; Consumer forum first |
| J-060 | SL | G | `mact_6m` | HL | Informational; never time-barred |
| J-061 | SL | G | `wrk_ir_s42_voluntary_arbitration` | HL | OFF per State until form verified |
| J-062 | SL | G | `IN.labour.codes.retrenchment_divisor` | HL | 26 (Equator policy); "indicative" |
| J-063 | SL | G | `IN.labour.codes.tribunal_dates` | HL | Earlier date; other as information |
| J-064 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | As J-047 |
| J-065 | CI | G | `notional_partition_include_wife` | TLR | No default; lawyer selects |
| J-066 | CI | G | `fam_property_arbitration` | HL | OFF |
| J-067 | SL | G | `IN-ST.family.partition_forum` | HL | Generic "revenue authority under State law" |
| J-068 | W | G | `IN.edu.grievance.ugc_equity` | HL | 2012 Regulations cell |
| J-069 | SL | G | `IN.edu.grievance.aicte_days` | TLR | 15/15/30 days labelled "Equator target" |
| J-070 | SL | G | `IN.consumer.cpa.mediation_finality` | HL | Finality copy without proviso numbers |
| J-071 | SL | N | — | PO | No launch date in copy |
| J-072 | CI | G | `voice.equator_service_number.enabled` | HL+TC | OFF until operator letter + telecom opinion |
| J-073 | CI | L | `IN.privacy.it_rules.intermediary` | REL | Due diligence ON (24 h / 7 d / 3 h) |
| J-074 | SL | G | `hague_visby_1y` | HL | Clock ON |
| J-075 | SL | G | `IN.professions.bci.cop_cycle_years` | HL | 5 years; annual re-verification |
| J-076 | RV | G | `lookupBarRoll` | CTO | OFF; two-person staff check with evidence |
| J-077 | SL | G | `IN.privacy.pml.bo_threshold_pct` | HL | > 10% (Equator policy) |
| J-078 | RV | G | `platform.integrations.whatsapp.otp` | CTO | OFF; DLT SMS OTP |
| J-079 | CI | G | `IN.rbi.conduct.rbios_periods` | HL | Advisory clock; never blocks filing |
| J-080 | SL | G | `IN.professions.bci.cop_cycle_years` | HL | 5 years |
| J-081 | RV | G | `lookupBarRoll` | CTO | OFF; staff check + letter (21-day chase) |
| J-082 | RV | G | `platform.integrations.institute_lookup` | CTO | No automated lookups |
| J-083 | CI | L | `profile_display_policy` | REL | No ratings or video on advocate profiles |
| J-084 | RV | G | `lookupBarRoll` | CTO | OFF; two-person verification |
| J-085 | CI | G | `consent_award_requested_post_settlement` | HL | Behind legal-review flag; Part III default |
| J-086 | CI | L | `IN.arbitration.acta.arbmed_s29a_guard` | REL | Unseal-and-sign before s.29A date |
| J-087 | CI | G | `consent_award_requested_post_settlement` | HL | As J-046 |
| J-088 | RV | G | `platform.payments.upi_autopay.limits` | CTO | Caps and retries in config |
| J-089 | SL | L | `IN.rbi.conduct.cic_status_block` | REL | PT-FIN-03 block; UCRF status named |
| J-090 | CI | G | `IN-ST.stamp.s33_restamp` | HL | Stamp certificate before release; review on amount change |
| J-091 | CI | G | `IN-ST.stamp.interstate_differential` | HL | Legal-review task; no computation for unverified States |
| J-092 | SL | G | `IN.payroll.gratuity.due_days` | HL | 30 days + interest |
| J-093 | CI | G | `IN.arbitration.acta.execution_limitation` | HL | 3-year reminder; no settled-period copy |
| J-094 | SL | G | `IN.rbi.conduct.cic_status_codes` | HL | Circular RBI/2023-24/71 |
| J-095 | CI | G | `IN.rbi.conduct.offer_relay` | HL | Recorded, in window, GRO footer, lender number |
| J-096 | SL | G | `IN.irdai.conduct.health_deductions` | HL | "Schedule per policy terms entered" |
| J-097 | SL | G | `IN.labour.codes.tribunal_dates` | HL | 45 / 90 days / 2 years |
| J-098 | SL | N | — | HL | Cite circular without paragraph number |
| J-099 | CI | G | `IN.privacy.dpdp.role_matrix` | HL+DPO | No live connector until DPA records role |
| J-100 | SL | G | `IN-ST.labour.grc_forms` | HL | Central r.7–8 content |
| J-101 | SL | G | `IN.edu.grievance.aicte_days` | TLR | As J-069 |
| J-102 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | As J-047 |
| J-103 | SL | G | `IN.edu.grievance.aicte_days` | TLR | As J-069 |
| J-104 | W | G | `IN-ST.labour.grc_forms` | HL | Central text + "confirm State form" banner |
| J-105 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | As J-047 |
| J-106 | SL | L | `platform.naming.restricted_words` | REL | Block National/Union/Central/Bharat |
| J-107 | CI | L | `referral.exclude_advocates` | REL | No referral reward of any kind (cash, credit, discount, priority) to advocates, CAs, CSs or CMAs (NN-17, X-54, X-62) |
| J-108 | CI | L | `FIN_CONTACT_WINDOW` | REL | Block outside window unless borrower chose slot |
| J-109 | CI | L | `IN.consumer.ecommerce_rules` | REL | Comply by default (App. O §6.3) |
| J-110 | PD | G | `platform.finance.fx.aed_method` | CFO | Derived rate with trail; AD-bank TT if auditor declines |
| J-111 | RV | G | `platform.integrations.esign.max_doc_mb` | CTO | 10 MB; split/compress |
| J-112 | RV | G | `AA_PORT` | CTO | OFF per tenant until TSP confirms |
| J-113 | RV | G | `gov.ondc_igm.enabled` | CTO | OFF |
| J-114 | PD | N | — | PO | Documentation legend only |
| J-115 | SL | G | `IN.rbi.conduct.doc_release_30d` | HL | 30-day obligation unchanged |
| J-116 | W | G | `sec_smart_odr_connector` | HL | OFF |
| J-117 | SL | N | — | PO | Citation recorded |
| J-118 | SL | N | — | MKT | No clause-level citation |
| J-119 | SL | N | — | HL | Corpus ingestion needs source URL |
| J-120 | CI | G | `IN-ST.stamp.s33_restamp` | HL | As J-090 |
| J-121 | PD | N | — | MKT | Not used in marketing (no Claims Register entry) |
| J-122 | SL | G | `platform.telecom.cnap` | CTO | Best effort; first-utterance ID remains |
| J-123 | SL | G | `connectors.vikalp.enabled` | CTO | OFF |
| J-124 | SL | G | `connectors.vikalp.enabled` | CTO | OFF |
| J-125 | RV | G | `platform.ai.bedrock.citations_mode` | CTO | Span-anchoring fallback |
| J-126 | PD | G | `platform.mobile.bundle_ids` | PO | Set at store upload |
| J-127 | PD | G | `platform.qa.device_farm` | CTO | Physical lab only |
| J-128 | PD | G | `platform.qa.device_farm` | CTO | Physical lab only |
| J-129 | SL | N | — | MKT | No clause-level citation |
| J-130 | PD | N | — | CTO | As J-045 |
| J-131 | CI | G | `IN.posh.act.inquiry_clock_start` | HL | As J-047 |
| J-132 | SL | G | `sec_smart_odr_connector` | HL | OFF; payer rule "both" before ON |
| J-133 | PD | G | `lawdocs_esign` | PO | OFF |
| J-134 | SL | G | `FIN_DRT_EXCLUSIVE` | TLR | Tenant-attested S.O.; unknown → warning + review |
| J-135 | SL | L | `com.s12a_equator_authorised` | REL | Form-1 routed to SLSA/DLSA only |
| J-136 | SL | G | `IN.court.lok_adalat_limits` | HL | ₹1 crore; S.O. number withheld |
| J-137 | PC | G | `sec_smart_odr_connector` | HL | OFF; no SEC revenue planned |
| J-138 | PC | G | `IN.sebi.odr.panel_segregation` | HL | Segregation ON (Equator policy) |
| J-139 | SL | G | `sec_smart_odr_connector` | HL | OFF; draft ruleset for impact tests |
| J-140 | PC | G | `IN.irdai.conduct.ombudsman_rules` | HL | No appellate step; 2023 r.17(3) |
| J-141 | PC | G | `ins_internal_ombudsman` | HL | OFF |
| J-142 | SL | G | `IN.payroll.gratuity.ceiling` | HL | ₹20,00,000; interest unset |
| J-143 | SL | L | `IN.telecom.tcccpr.a2p_declaration` | REL | Declarations before 17 Nov 2026; own DIDs OFF |
| J-144 | SL | L | `IN.telecom.tcccpr.cli_hygiene` | REL | Per-CLI controls ON |
| J-145 | W | G | `IN.intl.s44b_territories` | HL | INT_SEAT_NOT_NOTIFIED until S.O. on file |
| J-146 | PC | G | `IN.irdai.conduct.ombudsman_rules` | HL | No draft-rule behaviour |
| J-147 | PC | G | `IN.sebi.odr.panel_segregation` | HL | Segregation ON |
| J-148 | CI | G | `arb_appeal_tier_contractual` | HL | OFF; s.34 reminder ON |
| J-149 | SL | L | `IN.telecom.tcccpr.a2p_declaration` | REL | Guard enforced from go-live |
| J-150 | SL | G | `voice.equator_service_number.enabled` | HL+TC | OFF until operator + counsel |
| J-151 | SL | G | `IN.payroll.gratuity.ceiling` | HL | As J-142 |
| J-152 | SL | G | `IN.payroll.gratuity.ceiling` | HL | As J-142 |
| J-153 | W | G | `IN.intl.s44b_territories` | HL | INT_SEAT_NOT_NOTIFIED |
| J-154 | SL | G | `sec_smart_odr_connector` | HL | OFF |
| J-155 | W | G | `gov.ondc_igm.enabled` | CTO | OFF |
| J-156 | CI | L | `ai.award_reasoning_drafting` | REL | OFF; clerical help with disclosure |
| J-157 | CI | G | `billing.model.equator_principal` | CFO+TAX | OFF; neutral_direct |
| J-158 | CI | G | `billing.wallet.gst_mode` | CFO+TAX | advance (tax at receipt) |
| J-159 | CI | G | `billing.eco_withholding` (alias `tax.eco_tds`) | CFO+TAX | OFF; shadow ledger |
| J-160 | CI | G | `IN.tax.gst_it.memo_flags` | CFO+TAX | Conservative defaults |
| J-161 | CI | G | `IN.tax.gst_it.treaty_relief` | CFO+TAX | OFF per country; HB without TRC |
| J-162 | CI | G | `billing.eco_withholding` | CFO+TAX | OFF; shadow ledger |
| J-163 | CI | G | `billing.eco_gst_tcs` | CFO+TAX | OFF; shadow computation |
| J-164 | CI | G | `billing.wallet.deposit_subledger` | CFO+TAX | OFF; taxed at receipt |
| J-165 | CI | G | `billing.wallet.gst_mode` | CFO+TAX | As J-157/J-158 |
| J-166 | CI | G | `billing.fee_note_autogen` | CFO+TAX | Only with signed authorisation; else self-upload |
| J-167 | CI | G | `billing.eco_withholding` | CFO+TAX | OFF; shadow ledger |
| J-168 | SL | G | `IN.tax.gst_it.pan_form97` | CFO+TAX | `conservative_value`: PAN or Form 97 always required until threshold and form verified |
| J-169 | CI | G | `IN.tax.gst_it.academy_rate` | CFO+TAX | 18%; no "exempt" copy |
| J-170 | PD | G | `platform.org.legal_entity` | CS | Footer particulars withheld until MCA data uploaded |
| J2-001 | CI | L | `sign_instruments_on_behalf` | REL | OFF unless physical PoA verified; party signs |
| J2-002 | PD | L | `platform.neutral.public_labels` | REL | "Principal", never "Senior" |
| J2-003 | PC | G | `IN.privacy.spdi_dpdp_dual` | HL+DPO | Build to both regimes |
| J2-004 | SL | N | — | HL | Not cited in public copy |
| J2-005 | SL | N | — | HL | No probate-mandatory copy; citation withheld |
| J2-006 | PC | G | `com.msefc_referral_msp` | HL | OFF until both sections commence |
| J2-007 | CI | G | `fam.s15_prelit` | HL | Signpost to court/LSA mediation |
| J2-008 | CI | G | `IN.family.mwpsc.claimant_rules` | HL | No citizenship rejection; signpost |
| J2-009 | SL | G | `mact_6m` | HL | 6-month pill + SC interim-order note |
| J2-010 | SL | L | `IN.exclusions.bnss_s514` | REL | Live |
| J2-011 | SL | G | `copy.probate_s213_note` | HL | "No longer compulsory, may still be sought" |
| J2-012 | SL | G | `tenant.signposts.shebox_url` | HL | Link check; text without link on failure |
| J2-013 | CI | G | `IN-ST.family.rent_fora` | HL | "Rent Controller / Authority under State law" |
| J2-014 | SL | L | `IN.exclusions.waqf_s83` | REL | Exclusion live |
| J2-015 | SL | G | `IN-ST.family.partition_forum` | HL | Generic revenue-court text |
| J2-016 | SL | G | `tenant.signposts.nalsa_helpline` | HL | 15100 |
| J2-017 | SL | G | `IN.labour.codes.s53_settlement` | HL | Live |
| J2-018 | SL | G | `IN.consumer.telecom_signpost` | HL | "Telegraph Act repealed" copy; no s.7B |
| J2-019 | CI | G | `IN.consumer.cpa.education_status` | HL | Coaching/edtech: Consumer Commission "may be available" |
| J2-020 | SL | G | `coop_ombudsman` | HL | Signpost ON |
| J2-021 | SL | G | `IN.irdai.conduct.hit_and_run` | HL | Live |
| J2-022 | SL | L | `IN.rbi.conduct.rbios_representation` | REL | Equator never the representative |
| J2-023 | PC | G | `IN.signposts.national_sports_tribunal` | HL | Sports body / HC; no NST routing |
| J2-024 | SL | N | — | HL | Citation recorded |
| J2-025 | SL | N | — | HL | Citation recorded |
| J2-026 | SL | N | — | HL | Citation recorded |
| J2-027 | RV | G | `IN.court.formats.SC_EFILING` | HL | unverified; split at 20 MB |
| J2-028 | CI | G | `IN.court.formats.exhibit_series` | TLR | Annexure labels only; no Exhibit numbers |
| J2-029 | SL | G | `IN.court.formats.NCLT` | HL | unverified; corrected seed; 20 MB split |
| J2-030 | SL | L | `IN.court.formats.memo_lint` | REL | Caste/religion fields blocked |
| J2-031 | PC | G | `studio.ai_use_declaration` | HL | Stamp ON; declaration export OFF |
| J2-032 | PD | G | `platform.i18n.glossary_licences` | PO | No SUVAS terms without licence |
| J2-033 | CI | G | `bsa63_certificates` | HL | Draft-only until reviewer sign-off |
| J2-034 | SL | G | `IN.court.formats.NCLT` | HL | As J2-028/J2-029 |
| J2-035 | RV | G | `TRANSLATION_PORT` | CTO | Sarvam → IT2; G/Az OCR OFF |
| J2-036 | SL | N | — | HL | Internal reference only |
| J2-037 | PC | G | `studio.ai_use_declaration` | HL | Stamp ON; export OFF until notified |
| J2-038 | PC | G | `studio.ai_use_declaration` | HL | As J2-037 |
| J2-039 | CI | G | `IN-ST.stamp.arbitral_affidavits` | HL | Dutiable at affidavit rate; "check with notary" |
| J2-040 | CI | G | `TPL-PLS-SOT-CCA@1` | HL | OFF until verbatim text pasted; always sworn |
| J2-041 | CI | G | `studio.oath.remote.<forum_code>` | HL | OFF except cited HC rule |
| J2-042 | CI | L | `platform.neutral.public_labels` | REL | Sub-label mandatory |
| J2-043 | CI | G | `publication_class` | HL | statistics_only for challenges |
| J2-044 | CI | G | `platform.institution.pi_insurance` | CFO | PI cover before launch |
| J2-045 | CI | L | `platform.neutral.public_labels` | REL | Sub-label mandatory |
| J2-046 | CI | G | `tenant.neutral.judicial_title_display` | HL | Opt-in + verification |
| J2-047 | RV | G | `IN.professions.imi_code_map` | HL | Map to A&C s.12; IMI numbers blank |
| J2-048 | CI | G | `platform.neutral.body_reporting` | HL | Counsel review before report |
| J2-049 | PD | G | `platform.neutral.agreement_dr_institution` | PO | Agreement not issued until named |
| J2-050 | W | L | `INTL.intl.saudi_arbitrator_qual` | REL | Hard block stays |
| J2-051 | SL | G | `copy.probate_s213_note` | HL | ON after reviewer approves wording |
| J2-052 | SL | G | `copy.probate_s213_note` | HL | As J2-051 |
| J2-053 | PD | N | — | PO | Documentation legend only |
| J2-054 | SL | G | `IN.privacy.spdi_dpdp_dual` | HL+DPO | LR-ITA-001 IN_FORCE to 13 May 2027 |
| J2-055 | CI | L | `INTL.privacy.gdpr_art10` | REL | NN-24 minimum; AI blocked on Art. 10 data |
| J2-056 | SL | G | `INTL.privacy.uk_mode` | HL+DPO | Conditional on UK targeting |
| J2-057 | SL | G | `INTL.privacy.uk_mode` | HL+DPO | Live |
| J2-058 | W | G | `INTL.privacy.uae_pdpl` | HL+DPO | Strictest control set; no UAE claims |
| J2-059 | SL | G | `breach.adgm.hours` | HL+DPO | 72 h |
| J2-060 | CI | L | `IN.privacy.it_rules.synthetic_content` | REL | AI disclosure + provenance ON |
| J2-061 | SL | G | `tenant.contracts.cyber_annex` | TLR | Tenant annex; 6-h-ready notice |
| J2-062 | CI | L | `IN.privacy.dpdp.publication_anonymisation` | REL | Consent + redaction + re-ID test |
| J2-063 | SL | G | `INTL.privacy.gdpr_breach_routing` | HL+DPO | Live |
| J2-064 | SL | G | `INTL.privacy.us_ca_breach_days` | HL+DPO | Dormant; 30 days |
| J2-065 | SL | G | `INTL.privacy.gdpr_transfer_model` | HL+DPO | Live |
| J2-066 | RV | G | `platform.security.pci_saq_version` | CTO | File after acquirer confirms |
| J2-067 | RV | G | `platform.security.iso27701_target` | CTO | 27701:2025 directly |
| J2-068 | SL | G | `IN.privacy.spdi_dpdp_dual` | HL+DPO | Live |
| J2-069 | CI | G | `platform.security.isms_baseline` | CTO | Documented ISMS + annual audit |
| J2-070 | CI | G | `INTL.privacy.gdpr_art27_marketing` | HL+DPO | No EUR pricing until representative |
| J2-071 | CI | G | `ai.neutral_assist.eu_matters` | HL+DPO | OFF for EU-party matters |
| J2-072 | W | G | `INTL.privacy.uae_pdpl` | HL+DPO | SCC-equivalents; strictest clock |
| J2-073 | SL | G | `INTL.privacy.ccpa_mode` | HL+DPO | OFF; annual threshold test |
| J2-074 | SL | G | `INTL.privacy.uk_mode` | HL+DPO | Live |
| J2-075 | RV | G | `platform.security.pci_saq_version` | CTO | As J2-286–J2-288 |
| J2-076 | SL | N | — | HL | Citation recorded |
| J2-077 | RV | G | `platform.security.cert_roadmap` | CTO | Nothing before L+12 m |
| J2-078 | CI | L | `IN.privacy.dpdp.publication_anonymisation` | REL | PC-36 unchanged |
| J2-079 | CI | G | `retention.kyc_years` | HL+DPO | 5 years after relationship end |
| J2-080 | CI | G | `IN.arbitration.acta.execution_limitation` | HL | 12-year clock + 3-year prompt |
| J2-081 | CI | G | `IN.conciliation.acta_p3.s74_clocks` | HL | Per-party delivery date; "confirm with counsel" |
| J2-082 | CI | G | `arb_appeal_tier_contractual` | HL | Behind flag; protective challenge copy |
| J2-083 | CI | G | `IN.court.jurisdiction_rules` | HL | UNVERIFIED rows; generic forum text |
| J2-084 | CI | G | `IN.court.jurisdiction_rules` | HL | "Counsel to confirm"; no auto forum |
| J2-085 | CI | G | `IN-ST.court.execution_form_skins` | HL | Tabular particulars; State skins OFF |
| J2-086 | SL | N | — | HL | Cite Rahul S. Shah only |
| J2-087 | CI | G | `IN-ST.court.efiling_checklist` | HL | Generic list; State items OFF |
| J2-088 | CI | G | `IN-ST.stamp.family_arrangement` | HL | Lawyer review; no AI duty estimate |
| J2-089 | CI | G | `IN.family.nri_registration` | HL | Statutory steps + "confirm with Mission" |
| J2-090 | CI | L | `profile_display_policy` | REL | Five r.36 categories only |
| J2-091 | PD | N | — | PO | Documentation legend only |
| J2-092 | CI | L | `sign_instruments_on_behalf` | REL | Only with physical stamped PoA |
| J2-093 | CI | G | `IN.privacy.dpdp.respondent_verification` | HL+DPO | Verify only on respondent's action |
| J2-094 | CI | G | `retention.ovse_artefacts` | HL+DPO | Hash + result only; photo 30 days |
| J2-095 | CI | G | `retention.digilocker_attributes` | HL+DPO | Explicit consent; no images |
| J2-096 | RV | G | `platform.identity.epassport_pa` | CTO | Not relied on for K1 |
| J2-097 | CI | L | `IN.rbi.conduct.cic_report_upload` | REL | Tribunal direction or borrower consent |
| J2-098 | CI | G | `IN.professions.non_advocate_representation` | HL | Own officer or tribunal leave only |
| J2-099 | CI | G | `IN-ST.stamp.loa` | HL | LoA scopes per S-D1 |
| J2-100 | SL | G | `IN.professions.bci.cop_cycle_years` | HL | Live |
| J2-101 | PD | N | — | PO | Documentation legend only |
| J2-102 | SL | N | — | HL | Citation recorded |
| J2-103 | SL | N | — | HL | Citation recorded |
| J2-104 | SL | N | — | HL | Citation recorded |
| J2-105 | CI | G | `limitation_contract` | HL | Advisory 3 y / 12 y; never auto-closes |
| J2-106 | SL | N | — | HL | Citation recorded |
| J2-107 | SL | L | `IN.rbi.conduct.bureau_wording` | REL | Never promise "closed"; UCRF code recorded |
| J2-108 | TC | T | `tenant.fin.chargeback_window_days` | TA | "Ask your issuer"; no date unless set |
| J2-109 | TC | T | `tenant.fin.hfc_escalation_text` | TA | Tenant text; never RB-IOS |
| J2-110 | TC | T | `tenant.fin.scheme_limits.pm_vidyalaxmi` | TA | Config figures + "verify with bank" |
| J2-111 | PC | G | `IN.rbi.conduct.p2p` | HL | Provisional; no T+1 automation |
| J2-112 | PD | G | `interest_rate_pa` | HL | OFF unless verified State row |
| J2-113 | SL | G | `IN.rbi.conduct.co_lending` | HL | Both REs required |
| J2-114 | SL | L | `IN.rbi.conduct.bureau_wording` | REL | As J2-107 |
| J2-115 | TC | T | `tenant.fin.chargeback_window_days` | TA | Mediate after chargeback or joint consent |
| J2-116 | SL | G | `FIN_DRT_EXCLUSIVE` | TLR | As J-134 |
| J2-117 | PD | G | `interest_rate_pa` | HL | OFF |
| J2-118 | CI | G | `tenant.fin.settlement_grid` | TLR | Only with Board-policy evidence |
| J2-119 | PD | G | `tenant.fin.dlsa_recording_list` | HL | Hidden unless DLSA confirmed |
| J2-120 | RV | G | `platform.integrations.edrt_lookup` | CTO | Manual entry only |
| J2-121 | PD | G | `rbi_tat_2019` | HL | "Indicative" until table loaded and checked |
| J2-122 | PD | N | — | PO | Documentation legend only |
| J2-123 | SL | G | `IN.insolvency.ibc.clocks` | HL | Live |
| J2-124 | PC | G | `com.ibbi_reg2b` | HL | OFF; private pre-s.9 mediation only |
| J2-125 | PC | G | `IN.msme.msmed.s18_track` | HL | Original s.18 ON; substituted track OFF |
| J2-126 | PC | G | `com.msefc_referral_msp` | HL | OFF; new s.19 rule not applied |
| J2-127 | CI | G | `msme_works_contract` | HL | Warning; no auto-routing |
| J2-128 | CI | G | `consent_award_requested_post_settlement` | HL | As J-046 |
| J2-129 | SL | N | — | HL | Cite by name and date |
| J2-130 | SL | N | — | HL | Cite without file number |
| J2-131 | CI | L | `IN.arbitration.contract_s28_timebars` | REL | No auto time-bar; flag only |
| J2-132 | SL | N | — | HL | Citation (corpus only) |
| J2-133 | SL | N | — | HL | Citation (corpus only) |
| J2-134 | SL | N | — | HL | Citation (corpus only) |
| J2-135 | CI | L | `IN.exclusions.ip_registry_relief` | REL | Registry/validity relief blocked |
| J2-136 | SL | G | `IN-ST.realty.rera_interest` | HL | No figure for unverified States |
| J2-137 | CI | G | `IN-ST.realty.rera_limitation` | HL | No clock computed |
| J2-138 | SL | G | `IN.corporate.s442_eligibility` | REG | Manual registrar check |
| J2-139 | CI | G | `IN.corporate.s442_hosting` | HL | No fee; recorded consent to host |
| J2-140 | SL | G | `IN.corporate.s241_limitation` | HL | Indicative clock |
| J2-141 | SL | N | — | HL | Citation recorded |
| J2-142 | SL | L | `IN.insolvency.ibc.withdrawal_cta_guard` | REL | Withdraw CTA blocked outside the `withdrawal_window` (LR-IBC-003) |
| J2-143 | SL | G | `IN.insolvency.ibc.ppirp_threshold_pct` | HL | 51% |
| J2-144 | SL | G | `IN.insolvency.ibc.liquidation_reg2b` | HL | Live |
| J2-145 | PC | G | `IN.msme.msmed.s18_track` | HL | As J2-125 |
| J2-146 | SL | G | `FIN_DRT_EXCLUSIVE` | TLR | Needs recorded notification reference |
| J2-147 | SL | G | `IN.insolvency.ibc.withdrawal_window` | HL | Live |
| J2-148 | SL | G | `IN.insolvency.ibc.ppirp_threshold_pct` | HL | 51% |
| J2-149 | SL | G | `IN.insolvency.ibc.liquidation_reg2b` | HL | Live |
| J2-150 | PC | G | `com.ibbi_reg2b` | HL | Footer mandatory; OFF |
| J2-151 | SL | G | `IN-ST.realty.rera_interest` | HL | As J2-136 |
| J2-152 | SL | N | — | HL | Cite without file number |
| J2-153 | SL | N | — | HL | Citation recorded |
| J2-154 | PC | G | `com.msefc_referral_msp` | HL | OFF until all S.O.s, MCI regulations, recognition |
| J2-155 | CI | L | `COM_MSME_INTEREST_WAIVER_UNACKED` | REL | Hard block stays |
| J2-156 | PD | G | `IN-ST.procurement.state_adoption` | HL | State entities: signpost only |
| J2-157 | PD | L | `IN.arbitration.acta.s29a_scrutiny_guard` | REL | Scrutiny never passes s.29A date |
| J2-158 | PD | G | `tenant.arb.post_award_interest_source` | TLR | Rate field mandatory with source; no default |
| J2-159 | SL | L | `probate_mandatory_claim` | REL | Copy lint ON |
| J2-160 | PC | G | `fam.ucc_uk` | HL | OFF |
| J2-161 | SL | G | `fam.s15_prelit` | HL | OFF; Mediation Centre/LSA signpost |
| J2-162 | SL | G | `fam.s15_prelit` | HL | OFF |
| J2-163 | SL | G | `IN.family.hma_one_year_bar` | HL | Hard alert + lawyer review |
| J2-164 | SL | G | `IN-ST.family.divorce_act_s10a` | HL | 2 years; Kerala note with review |
| J2-165 | W | L | `IN.exclusions.matrimonial_status` | REL | Consequences only; no status statement |
| J2-166 | PC | G | `fam.ucc_uk` | HL | OFF; residence question at intake |
| J2-167 | CI | G | `IN-GA.family.civil_code` | HL | Out of scope; route to counsel |
| J2-168 | CI | G | `IN.family.mwpsc.claimant_rules` | HL | No block; "Tribunal decides" warning |
| J2-169 | SL | L | `IN.family.succession.decree_claim_lint` | REL | Lint blocks "decree" claims; `fam.s15_prelit` OFF (as J2-178) |
| J2-170 | CI | G | `copy.probate_s213_note` | HL | Silent on pre-20 Dec 2025 deaths |
| J2-171 | SL | G | `IN.family.succession.probate_limitation` | HL | Information only |
| J2-172 | SL | G | `IN.family.succession.nomination` | HL | Live |
| J2-173 | SL | G | `IN-ST.family.partition_forum` | HL | Generic; only UP s.116 named |
| J2-174 | CI | L | `IN.family.nri_agri_land` | REL | HB beyond inherited share; warning + counsel |
| J2-175 | CI | G | `fam.khula_pathway` | HL | ON as protective framing |
| J2-176 | PC | G | `fam.ucc_uk` | HL | OFF; UCC clocks disabled |
| J2-177 | SL | L | `probate_mandatory_claim` | REL | Lint ON |
| J2-178 | CI | G | `fam.s15_prelit` | HL | OFF; LSA signpost |
| J2-179 | SL | N | — | HL | Research note only |
| J2-180 | SL | G | `ins.surveyor_threshold_minor` | HL | Config value + "verify"; no hard block |
| J2-181 | SL | L | `IN.irdai.conduct.citation_lint` | REL | Cite by title/date; serial blocked |
| J2-182 | SL | G | `mact_6m` | HL | As J-060 |
| J2-183 | SL | G | `IN.irdai.conduct.ombudsman_scope` | HL | "Likely available"; bank route |
| J2-184 | SL | G | `mact_6m` | HL | As J-060 |
| J2-185 | SL | L | `IN.irdai.conduct.citation_lint` | REL | As J2-181 |
| J2-186 | SL | L | `IN.irdai.conduct.citation_lint` | REL | Title/date only |
| J2-187 | CI | G | `policy_issue_regime` | HL | Both computations; "argued position" |
| J2-188 | SL | G | `IN.irdai.conduct.portability_tats` | HL | Informational |
| J2-189 | SL | G | `mact_6m` | HL | Informational |
| J2-190 | SL | N | — | HL | Not cited until confirmed |
| J2-191 | SL | N | — | HL | Cite as "(SC, 13 Apr 2023)" |
| J2-192 | SL | G | `IN.irdai.conduct.carrier_clocks` | HL | Informational + review flag |
| J2-193 | SL | G | `IN.irdai.conduct.centre_map` | HL | Residence district + branch selector |
| J2-194 | PD | G | `ins.leap_day_rule` | HL | feb28 |
| J2-195 | SL | L | `ins_policy_suit_bar` | REL | Warning only |
| J2-196 | CI | G | `policy_issue_regime` | HL | Dual computation |
| J2-197 | PD | G | `ins.leap_day_rule` | HL | feb28 |
| J2-198 | PD | N | — | PO | Documentation legend only |
| J2-199 | CI | L | `IN.labour.codes.settlement_form` | REL | Form I pack; never an s.74 award |
| J2-200 | SL | N | — | HL | Cite chapter only |
| J2-201 | PC | G | `IN-RJ.labour.gig_workers` | HL | Informational; no RJ clocks |
| J2-202 | CI | L | `IN.labour.codes.manager_arrears_arbitration` | REL | Arbitration ✖; mediation; signpost |
| J2-203 | SL | G | `IN.payroll.maternity` | HL | Live |
| J2-204 | SL | G | `IN.payroll.leave.encashment` | HL | Entered component; no clause number |
| J2-205 | CI | G | `IN-ST.labour.se_termination` | HL | Generic signpost; no State clocks |
| J2-206 | CI | L | `IN.labour.codes.fte_arbitration` | REL | Warning; no A&C for worker FTEs |
| J2-207 | SL | L | `IN.labour.codes.ec_settlement_registration` | REL | Proof required before closure |
| J2-208 | SL | N | — | HL | Case name removed until verified |
| J2-209 | SL | G | `IN.payroll.leave.encashment` | HL | As J2-204 |
| J2-210 | PC | G | `IN.payroll.bonus.ceilings` | TLR | Tenant/counsel-entered; blocks until set |
| J2-211 | SL | G | `IN.labour.codes.ei_court_limitation` | HL | 3 years + regulations note |
| J2-212 | SL | G | `IN.payroll.maternity` | HL | No clock; "file promptly" |
| J2-213 | SL | G | `IN-ST.labour.grc_forms` | HL | "Check State form" banner |
| J2-214 | SL | G | `wrk_reskilling_remit_10d` | HL | Both clocks ON |
| J2-215 | CI | L | `IN.labour.codes.fte_arbitration` | REL | As J2-206 |
| J2-216 | PC | G | `IN-RJ.labour.gig_workers` | HL | As J2-201 |
| J2-217 | W | G | `IN-ST.labour.gig_workers` | HL | Informational |
| J2-218 | SL | N | — | HL | As J2-200 |
| J2-219 | PC | G | `IN.signposts.whistle_blowers_act` | HL | Signpost only; no clocks |
| J2-220 | SL | G | `IN.signposts.hiv_act` | HL | Signpost without section numbers |
| J2-221 | SL | G | `wrk.irc42` | HL | OFF until template approved and State form loaded |
| J2-222 | SL | G | `IN.labour.codes.ec_limitation` | HL | 2 years, condonable |
| J2-223 | CI | G | `IN-ST.labour.se_termination` | HL | As J2-205 |
| J2-224 | SL | G | `IN.labour.codes.ec_authority` | HL | Live |
| J2-225 | PC | G | `IN-RJ.labour.gig_workers` | HL | RJ_AUTHORITY hidden |
| J2-226 | SL | G | `IN.signposts.hiv_act` | HL | As J2-220 |
| J2-227 | SL | G | `wrk_reskilling_45d` | HL | Informational + 10-day remittance clock |
| J2-228 | SL | G | `IN.payroll.gratuity.due_days` | HL | Live |
| J2-229 | SL | G | `IN-ST.labour.settlement_forms` | HL | Form I central; "confirm State form" |
| J2-230 | CI | G | `IN.payroll.gratuity.part_year_rule` | TLR | part_year_over_6m + exact_fraction shown |
| J2-231 | SL | G | `IN.labour.codes.s53_settlement` | HL | Live |
| J2-232 | PD | N | — | PO | Documentation legend only |
| J2-233 | CI | G | `INTL.intl.s74_cross_border` | HL | s.74 only for India enforcement; consent award abroad |
| J2-234 | SL | G | `IN.intl.s44b_territories` | HL | INT_SEAT_NOT_NOTIFIED warning |
| J2-235 | SL | G | `hague_visby_1y` | HL | Live |
| J2-236 | CI | G | `tier_unreasoned_award` | TLR | Warning; reasoned award default |
| J2-237 | CI | L | `intl.ea_ppo_india_seat` | REL | OFF; court under s.9 |
| J2-238 | CI | G | `tribunal_constituted_for_purpose` | HL | Only with live dispute and existing agreement |
| J2-239 | CI | G | `INTL.intl.s74_cross_border` | HL | As J2-233 |
| J2-240 | CI | G | `hague_visby_1y` | HL | Indicative day; "file by" day earlier |
| J2-241 | CI | G | `INTL.intl.s74_cross_border` | HL | As J2-233 |
| J2-242 | SL | N | — | CFO+TAX | No section number in copy |
| J2-243 | CI | G | `IN.tax.gst_it.nonresident_honoraria` | CFO+TAX | No payment until memo |
| J2-244 | CI | G | `IN.tax.gst_it.sac_codes` | CFO+TAX | SAC 999293 at 18% |
| J2-245 | CI | G | `billing.plan_credit_tax_model` | CFO+TAX | Model (a); zero-value redemption invoices |
| J2-246 | PD | N | — | CFO+TAX | Generic label |
| J2-247 | CI | G | `billing.fee_note_autogen` | CFO+TAX | Self-upload default |
| J2-248 | CI | G | `IN.tax.gst_it.no_pan_tds` | CFO+TAX | Flag ON; section label blank |
| J2-249 | SL | N | — | HL | Unnamed example only |
| J2-250 | CI | L | `IN.arbitration.acta.s12_qualification` | REL | Rules' qualification enforced exactly |
| J2-251 | RV | G | `platform.neutral.qap_budget` | CFO | Budget line TBC |
| J2-252 | SL | G | `tenant.contracts.outsourcing_clauses` | TLR | "Standard RBI-style clauses"; no compliance claim |
| J2-253 | CI | G | `academy.institute_referral_fee` | BRD | OFF; Board + s.184 disclosure |
| J2-254 | SL | N | — | HL | Cite rule level only |
| J2-255 | SL | L | `billing.wallet.redemption_scope` | REL | Equator invoices only (X-30) |
| J2-256 | SL | L | `IN.payments.card_data` | REL | No card data (NN-31) |
| J2-257 | CI | G | `IN.court.jurisdiction_rules` | HL | Both courts named; "advocate will confirm" |
| J2-258 | CI | G | `IN.insolvency.ibc.withdrawal_window` | HL | Plain-language labels |
| J2-259 | SL | G | `retention.ovse_artefacts` | HL+DPO | Hash + minimal attributes |
| J2-260 | SL | G | `IN.rbi.conduct.card_directions` | HL | C-FIN-19 unchanged |
| J2-261 | TC | T | `tenant.fin.hfc_escalation_text` | TA | As J2-109 |
| J2-262 | SL | G | `IN.rbi.conduct.card_directions` | HL | Live |
| J2-263 | SL | G | `IN.rbi.conduct.gold_loans` | HL | Legacy-loan rule as stated |
| J2-264 | SL | G | `IN.rbi.conduct.msme_revival` | HL | Cite without paragraph |
| J2-265 | SL | G | `tenant.fin.sarfaesi_attestation` | TLR | Tenant attestation with S.O. |
| J2-266 | SL | G | `IN.rbi.conduct.card_directions` | HL | ₹500/day after 7 working days |
| J2-267 | TC | T | `tenant.fin.working_calendar` | TA | Mon–Fri + State NI Act holidays |
| J2-268 | SL | G | `IN.rbi.conduct.cic_compensation` | HL | "Indicative" until Annex tests pass |
| J2-269 | SL | G | `IN.insolvency.ibc.liquidation_reg2b` | HL | Live |
| J2-270 | CI | G | `msme_works_contract` | HL | As J2-127 |
| J2-271 | SL | N | — | HL | No SAROD fee figures |
| J2-272 | PD | G | `com.rera_forum_tieup` | PO | OFF outside Maharashtra |
| J2-273 | PC | G | `IN.corporate.s442_track` | HL | 2016 Rules; sunset on s.63 commencement |
| J2-274 | SL | G | `IN.family.succession.isa_ch2` | HL | s.33A OFF for Christians |
| J2-275 | PD | G | `IN-ST.court.court_fees` | HL | Estimator OFF; "per State law" |
| J2-276 | SL | G | `fam.mwpsc_conciliation.v1` | HL | Only on written Tribunal nomination |
| J2-277 | CI | G | `IN.family.mwpsc.claimant_rules` | HL | Warning only |
| J2-278 | CI | G | `IN.consumer.cpa.pecuniary_basis` | HL | Premium basis + claim basis shown |
| J2-279 | SL | G | `IN.payroll.gratuity.ceiling` | HL | As J-142 |
| J2-280 | SL | G | `IN.labour.codes.ei_court_limitation` | HL | As J2-211 |
| J2-281 | PC | G | `IN.payroll.bonus.ceilings` | TLR | As J2-210 |
| J2-282 | PD | G | `tenant.fees.quote_on_request` | REG | Registrar quote |
| J2-283 | RV | G | `connectors.ondc.enabled` | CTO | OFF; signpost without empanelment claim |
| J2-284 | SL | G | `rent_authority` | HL | Generic; no State limits |
| J2-285 | RV | G | `TRANSLATION_PORT` | CTO | Coverage test before routing |
| J2-286 | RV | L | `platform.security.payment_page_controls` | REL | Controls ON; attest after acquirer confirms |
| J2-287 | RV | G | `platform.payments.mobile_sdk` | CTO | OFF; hosted link in system browser |
| J2-288 | RV | G | `platform.security.csp_pay` | CTO | Enforce after 7 clean report-only days |
| J2-289 | PD | L | `platform.trust.badges` | REL | No badge until certified (NN-17) |
| J2-290 | PD | G | `platform.identity.face_match_threshold` | CTO | No automated adverse decision |
| J2-291 | SL | N | — | HL | Citation recorded |
| J2-292 | CI | G | `com.msefc_referral_msp` | HL | OFF; readiness dossier only |
| J2-293 | CI | L | `IN.exclusions.pwdva_counselling` | REL | No DV product; signpost Protection Officer |
| J2-294 | RV | G | `platform.integrations.bima_sugam` | CTO | No integration; watch-list |
| J2-295 | SL | L | `platform.migrations.ins_ddl_guard` | REL | Blocked until golden tests pass |
| J2-296 | RV | G | `platform.integrations.hrms_vendors` | CTO | Manual/SFTP CSV; per-vendor flag |
| J2-297 | TC | T | `tenant.case.mediation_invite_deemed_rejection_days` | TA | 30 days |
| J2-298 | SL | N | — | MKT | Cite with "as published" date |
| J2-299 | PD | N | — | PO | Documentation legend only |

---

## V.4 Settings Catalogue

### V.4.0 Conventions

**Columns.**
- **Key**: canonical key, with the `tenant.` prefix implied in §V.4.1.
- **Tier**: L, G or T. "T≥G" means a bounded T: the tenant chooses within a G floor or range. "T≥L" means the tenant may only raise a locked platform baseline.
- **Who**: the lowest role that may make the change.
- **Approval**:
  - none — applies immediately;
  - TC — tenant checker (a second tenant user holding the permission);
  - TLR — tenant `legal_reviewer`;
  - platform function — CFO, DPO, Head of Legal (HL) or CTO.
- **Default**.
- **Validation**: enforced by `cfg` validators before save.

**Audit.** Every change writes an `audit.audit_events` row: actor, scope, key, before and after digest, reason, tier and change ID. It also writes a `cfg.setting_changes` row. The audit trail cannot be switched off (NN-22). Changes to money, privileged roles and sensitive exports also write a `ctl` approval record (NN-36).

### V.4.1 Organisation catalogue (every tenant kind)

| Module | Key | Tier | Who | Approval | Default | Validation |
|---|---|---|---|---|---|---|
| Profile | `org.display_name` | T | tenant admin | none | KYB name | 2–80 chars; restricted-word list (L): "Court", "Tribunal", "National", "Union", "Central", "Bharat", regulator names; "Court" needs counsel review (D2-16) |
| Profile | `org.legal_entity` (legal name, CIN/LLPIN, GSTIN, registered office, PAN) | G | tenant admin | TC + Equator KYB re-check | MCA21 / GSTN pull | CIN regex; GSTIN checksum; mismatch with KYB → `CFG_KYB_MISMATCH` |
| Profile | `org.grievance_officer`, `org.dpo_contact`, `org.nodal_officer` | G | tenant admin | TC | Required for regulated tenants before go-live | Domain email; verified phone; printed in recovery messages (NN-12) and notices |
| Profile | `org.contact_channels` (support email, phone, WhatsApp, postal) | T | tenant admin | none | — | Email verified; phone verified by OTP; WhatsApp only on a verified WABA |
| Branding | `brand.logo`, `brand.favicon` | T | tenant admin, brand delegate | none | Equator neutral mark | SVG/PNG ≤ 1 MB; attestation of rights; no national emblem or court imagery (L, Emblems Act 1950) |
| Branding | `brand.colours` (primary, secondary, accent, surface, text) | T | brand delegate | none | Equator tokens | WCAG 2.2 AA: text ≥ 4.5:1, large text and UI ≥ 3:1, focus ring ≥ 3:1; clock colours fixed (L); dark mode auto-derived; failure → `CFG_CONTRAST_INSUFFICIENT` |
| Branding | `brand.fonts` | T | brand delegate | none | System stack | Approved list only; must cover every enabled script (Devanagari, Tamil, etc.); body ≥ 16 px |
| Branding | `brand.email_sender` (from name, domain) | G | tenant admin | TC | Equator domain | SPF, DKIM and DMARC aligned; display name ≠ another organisation |
| Domains | `domains.custom` | G | tenant admin | TC | `<slug>.equatorresolution.in` | DNS TXT proof; TLS auto-issued; HSTS on (L) |
| Languages | `i18n.enabled_locales`, `i18n.default_locale` | T | tenant admin | none | en-IN, hi-IN | A locale without approved legal templates is UI-only (NN-23) |
| Time | `time.timezone` | T | tenant admin | none | Asia/Kolkata | IANA zone; statutory clocks always use the forum calendar (L) |
| Time | `time.working_calendar` | T≥G | tenant admin | none | State list per office | National holidays locked; festival choices within the State count [RC C-15] |
| Structure | `org.units` (departments, offices, teams, programmes, GRM variants) | T | tenant admin, unit admin | none | One unit "Head office"; Operations Platform uses the D3-06 list | Tree depth ≤ 6; each unit maps to one legal entity (NN-38) |
| Structure | `org.cost_centres`, `org.locations` | T | tenant admin | none | — | Unique codes |
| Access | `access.invite_policy` (who may invite; allowed domains) | T | tenant admin | none | Admins only | Domain list syntax |
| Access | `access.role_assignments` (standard roles) | T | tenant admin, unit admin within unit | none | — | SoD conflicts blocked (Appendix S §6.7) |
| Access | `access.role_assignments` (privileged: admin, finance, payroll, legal reviewer, export) | G | tenant admin | TC (NN-36) | — | Maker ≠ grantee; step-up; expiry ≤ 12 months |
| Access | `access.permission_sets`, `access.role_templates` (`role_bundle`) | G | tenant admin | TC (elevated, 2 checkers) | Platform bundles | Cannot exceed platform guardrails; validator lists the deltas |
| Access | `access.delegated_admin` (unit admins with a scoped permission set) | T | tenant admin | none | — | A delegate can never grant more than they hold |
| Access | `access.delegations` | T | user with authority | none | — | Appendix S §6.4 limits (≤ 90 days; depth 1) |
| Access | `access.temporary_access` (just-in-time) | T | requester → approver | Approver ≠ requester | — | ≤ 72 h; reason ≥ 20 chars; auto-revoke |
| Access | `access.review_cadence` | T≥G | tenant admin | none | Privileged quarterly; others half-yearly | Privileged ≤ 3 months; others ≤ 6 months |
| Access | `access.support_session` | T | tenant admin | none | None granted | ≤ 72 h; scoped (read, configure); visible banner (D3-14) |
| Cases | `case.dispute_types_enabled` | G | tenant admin | TC; TLR for new types | Plan default | Master §5.2 matrix (L); a type needs routing and signposting before activation |
| Cases | `case.intake_forms` (form engine) | G for legal fields; T for optional fields | tenant admin, form designer | TLR for legal fields | Platform `form_schema` | EN and HI parity; legal text reviewed; schema version pinned (NN-21) |
| Cases | `case.document_requirements` | T to add; G to remove a statutory item | case lead | TLR to remove | Pack default | Statutory items cannot be removed (L) |
| Cases | `case.templates.legal` (notices, letters, settlement and award shells) | G | tenant legal | TLR | Platform templates | Mandatory disclosure blocks locked (L); citation lint (§V.2.4) |
| Cases | `case.templates.non_legal` (covering emails, reminders) | T | case lead | none | Platform text | Prohibited-phrase lint (P13) |
| Cases | `case.clocks.internal_targets` | T≥G | case lead | none | None | Only stricter than statutory; owners mandatory (NN-04, L) |
| Cases | `case.status_labels` | T | tenant admin | none | Canonical labels | 1:1 to canonical states; glossary lint blocks "decree", "judgment" and "court" (L); pinned once used in a served notice |
| Cases | `case.queues`, `case.auto_assignment` (case managers) | T | case lead | none | Round-robin by language and skill | Never assigns neutrals; allocation is platform G (NN-03, NN-28) |
| Cases | `case.sla_policies`, `case.escalation_matrix` | T≥G | case lead | none | Statutory floor; 3 levels | Level 3 mandatory for statutory clocks (L) |
| Notifications | `notify.channels_enabled`, `notify.channel_order` | T | tenant admin | none | Portal, email, SMS, WhatsApp | Legal-service journeys keep ≥ 2 channels (L) |
| Notifications | `notify.quiet_hours` | T≥G | tenant admin | none | 21:00–08:00; FIN floor 19:00–08:00 | Narrow-only against NN-12 (L). The floor is the registered L key `platform.notify.contact_window_floor` (08:00–19:00; microfinance 09:00–18:00 to 31 Dec 2026; guard `FIN_CONTACT_WINDOW`, J-056) |
| Notifications | `notify.digests` | T | user / tenant | none | Daily for professionals | — |
| Notifications | `notify.templates` (non-legal) | T | tenant admin | none | Platform | DLT template ID required for SMS (G) |
| Notifications | `notify.sender_ids` (DLT headers, WABA numbers) | G | tenant admin | TC + evidence | Equator headers | DLT registration evidence; 1600-series only for RBI, SEBI, IRDAI or PFRDA regulated tenants (NN-12) |
| Billing | `billing.plan`, `billing.add_ons` | T | tenant admin, billing admin | none | Contracted plan | Honest pricing (NN-29, L); proration preview (Appendix O §5.3) |
| Billing | `billing.gst_details`, `billing.place_of_supply` | G | billing admin | TC | KYB data | GSTIN validation; changes only prospective |
| Billing | `billing.payment_methods`, `billing.mandates` | T | billing admin | none | — | Hosted checkout only (NN-31); e-mandate rules (NN-29) |
| Billing | `billing.approval_thresholds` | G | finance admin | TC (NN-36) | Authority matrix | Amount bands ascending; approver ≠ maker |
| Billing | `billing.contacts`, `billing.po_reference` | T | billing admin | none | — | Email verified |
| Integrations | `integrations.api_keys` | G | integration admin | TC | None | Scopes from catalogue; expiry ≤ 365 days; shown once; IP binding optional |
| Integrations | `integrations.webhooks` | T (no personal data) / G (personal data) | integration admin | TC for personal data + DPA on file | None | HTTPS; signing secret; event allow-list |
| Integrations | `integrations.sso` (SAML / OIDC), `integrations.scim` | G | tenant admin + IT | TC | Off | Test sign-in before "enforce"; break-glass admin retained |
| Integrations | Connector flags and switches as named by Appendix AC §AC.17 and Appendix X §X.13: `mkt.brevo.enabled` (one flag for both Brevo ports), `ops.workspace.google.enabled` (canonical `platform.ops.workspace.google.enabled`), `mkt.social.<adapter>.enabled`, `tenant.ops.connectors.<provider>.enabled`, `tenant.ops.connectors.brevo_crm_sync.enabled`; shared Brevo budget `tenant.mkt.brevo.max_requests_per_hour`. `integrations.connectors.*` is not used | G (flags); T (sync switches, budgets) | owner named in AC §AC.17 / X §X.13 | TC for G | Off | Appendix AC §AC.11 (catalogue), §AC.12 (system of record and field mappings) and §AC.17 (connector settings); system-of-record declared (NN-40) |
| Data model | `custom.fields`, `custom.tags`, `custom.picklists` | T | tenant admin | none | — | ≤ 100 fields per object; special-category or ID fields need DPO (G); no fields in sealed stores (L) |
| Reports | `reports.saved_views`, `reports.dashboards` | T (user or tenant) | any permitted user | none | Role dashboards (Appendix S §5) | Sealed data never (NN-07); n ≥ 5 internal and n ≥ 10 public aggregates (X-28) |
| Reports | `reports.scheduled_exports` | G if personal data; T otherwise | report owner | TC for personal data (NN-36) | None | Destination allow-list; encryption |
| Data | `data.import` | T (reference data) / G (people, cases, money) | data admin | TC for G | — | Schema validation; dry run; duplicate checks |
| Data | `data.export.full` (NN-37) | T to request | tenant admin | Sensitive classes need TC | — | `EQ-EXPORT-1.0` package; free at exit |
| Data | `data.retention` | T≥G | DPO (tenant) | TC | Statutory schedule (Appendix Q) | Longest wins; never below the statutory minimum (L); outcomes ≥ 13 years (X-36) |
| Data | `data.legal_hold` | G | legal reviewer, DPO | TC | — | Blocks deletion; reason and matter reference |
| Data | `data.deletion_requests` | G | DPO | TC + 7-day cooling-off | — | Not during legal hold; audit keeps tombstones |
| Security | `security.mfa_policy` | T≥L | tenant admin | none | Platform baseline; staff phishing-resistant (L) | Raise-only |
| Security | `security.session_idle_minutes`, `security.session_absolute_hours` | T≥L | tenant admin | none | 30 min / 12 h | Idle 5–240 min; absolute ≤ 24 h; sealed tiers ≤ 15 min (L) |
| Security | `security.allowed_email_domains`, `security.device_rules` | T | tenant admin | none | Open; managed devices optional | Raise-only for device rules |
| Security | `security.ip_allow_list` | G | tenant admin | TC | Off | Admin's current IP must be included; break-glass path |
| Privacy | `privacy.notices`, `privacy.consent_purposes` | G | tenant DPO | TLR | Platform notices | Itemised; per language; versioned (NN-15) |
| Privacy | `privacy.dsr_sla_days` | T≥G | tenant DPO | none | Statutory | Shorter only |
| Privacy | `privacy.cross_border` | G | tenant DPO | HL (platform) | Off | s.16 basis recorded (NN-15) |
| AI | `ai.features.<feature>` | T to switch OFF; G to switch ON a case-affecting feature | tenant admin | TLR for ON | Plan default | NN-01, NN-25 (L); no training on case data (L) |
| AI | `ai.translation_engines`, `ai.ocr_engines` | G | tenant admin | TC | India-resident engines (X-33) | Non-India engines OFF unless approved |
| AI | `ai.voice_agent.*` | G | tenant admin | TLR | Off | Disclosure nodes cannot be removed (L) |
| Profile | `profile.public_page` (content) | T | tenant admin | none | — | Claims need a Claims Register entry (NN-17, G) |
| Marketplace | `marketplace.listing` (for chambers tenants this is `tenant.chm.marketplace.opt_in`, Appendix W §W.8.1) | T (opt-in) | tenant admin | none | Off | Private Practice Marketplace only; category law checks (Appendix AA §AA.15); platform flag `marketplace.paid_placement` (G, OFF until Board and counsel) and `marketplace.paid_placement.advocates` (L, OFF) are not tenant settings (NN-34) |
| Availability | `platform.availability.<feature>` by plan, jurisdiction, segment | G (platform) | product owner; HL for legal features | Platform checker | Per Appendix AB §AB.8 | Shown as "available on {plan}"; never as a dark-pattern upsell (NN-29) |

### V.4.2 Party or individual user (`/settings`; Appendix S §7)

All of these settings apply immediately, with audit.

| Setting | Tier | Default | Rules |
|---|---|---|---|
| Profile, contact points, addresses | T (user) | From sign-up | Legal name read-only after K1; change by re-verification |
| Sign-in methods, passkeys, recovery codes, devices | T (user) | OTP + passkey offered | Cannot remove the last factor where the role requires one |
| Language, notice language, accessibility (font scale, contrast, motion, captions, assisted mode) | T (user) | Browser locale | Applies across web and mobile |
| Notification channels and categories, digest | T (user) | All case-critical channels on | Legal notices cannot be switched off (the page explains which and why) |
| Quiet hours, blackout dates | T (user, narrow-only) | NN-12 window shown locked | Blackouts honoured by every channel |
| Consents by purpose; notices; data requests; download my data; delete account | T (user) | Per notice | Withdrawal propagates (FR-P01-38); legal-hold explanation shown |
| Representatives and authorities (grant, narrow, revoke) | T (user) | None | NN-27; settlement above the limit needs the party's own e-sign |
| Payment methods, receipts | T (user) | — | NN-31 |
| Publication consent per case | T (user) | Off | NN-26; revocable before publication |
| Marketing consent (separate) | T (user) | Off | NN-16; respondents excluded unless they opt in |

### V.4.3 Representative or advocate (`/counsel/settings`)

| Setting | Tier | Default | Rules |
|---|---|---|---|
| Public profile fields | L (field set) / T (values) | BCI r.36 Schedule fields | Advocates: name, contact, enrolment, qualifications, areas of practice only (J-032); no ratings, fees, testimonials or rankings (NN-34, NN-39) |
| Firm profile, members, firm admin, sub-delegation | T | Owner is firm admin | Same firm; one level (Appendix S §6.4) |
| Client authorities dashboard (renounce, expiry reminders) | T | 30-day reminders | — |
| Calendar feed (ICS), digest, notification channels | T | Weekly digest | Feed titles carry the case number only |
| Personal drafting snippets (non-pleading) | T | None | Never inserted into a party's AI-drafted pleading by staff (NN-25) |
| Conflict declarations, practice areas for matching | T | — | Declarations feed the conflict check (Appendix S §4.9) |
| Referral rewards | L (OFF for advocates, CAs, CSs and CMAs) | Off | BCI Part VI (J-107); NN-34 |
| Directory listing (group registry) | T (opt-in, per-field consent) | Off | NN-39; public search flag OFF |

### V.4.4 Neutral (`/mediator/settings`, `/arbitrator/settings`)

| Setting | Tier | Default | Rules |
|---|---|---|---|
| Availability calendar, leave, maximum concurrent matters | T≥G | Platform cap | Personal cap ≤ platform concentration and capacity caps (G) |
| Languages, sectors, cities, mechanisms offered | T (claims) + G (verification) | — | Each claim verified before it counts for eligibility (NN-28) |
| Public profile | T (values) / G (display policy) | `profile_display_policy` by credential | Advocate-neutrals restricted (L); no win rates or "friendly" tags (NN-16) |
| Fee preferences | G | Platform fee card | Within Appendix B bands; regulated schedules exact (NN-18) |
| Payout bank account, tax details (PAN, GST, TRC) | G | — | Cooling-off 3 working days with out-of-band confirmation (NN-36); tax memo flags (LG-12) |
| Tech concierge delegation | T | Off | Per session; controls only (Appendix S §6.4) |
| Disclosure statements, conflict declarations | T (content) / L (duty) | — | Mandatory before appointment (A&C s.12) |
| Private-practice marketplace listing | T (opt-in) | Off | Separate surface. Advocate-neutrals may list only when `marketplace.advocate_neutrals.listing` (G, OFF) is ON and are never eligible for sponsored placement (`marketplace.paid_placement.advocates`, L). Paid placement for other neutrals OFF until Board and counsel (NN-34; Appendix AA §AA.15) |
| Notifications, digest, calendar feed | T | — | — |

### V.4.5 Private ADR Chambers (summary; detail in Appendix W §W.8)

| Area | Examples | Tier |
|---|---|---|
| Website and brand | Chambers page on the Equator site, logo, colours, domain, practice areas, team pages, rules of procedure (versioned) | T (content), G (rules of procedure; claims) |
| Case administration | Intake forms, fee schedules within NN-18, clocks above floors, templates, status labels, queues | G for fees, rules and legal templates; T for operational settings |
| Staff and case managers | Users, roles (`chambers_owner`, `chambers_admin`, `chambers_case_manager`, `chambers_staff`, `chambers_hr`, `chambers_accounts`), permission sets, delegation | T; privileged grants G |
| HR-lite and salary | Small-establishment mode, payroll rule-pack adoption, leave template ("statutory minimum" or "Equator standard"), salary disbursal maker-checker | G for parameters and money (NN-36); T for policy above the floor |
| Billing and revenue | Plan, add-ons, marketplace listing, revenue-stream switches `tenant.rev.stream.<code>.enabled` (Appendix AB §AB.8) | T; prices G; sponsored placement is a platform flag, never a chambers setting (NN-34) |

### V.4.6 Enterprise tenants (lender, insurer, employer, university GRM; POSH)

| Variant | Settings a tenant admin changes unaided (T) | Governed (G) — approver | Locked (L) |
|---|---|---|---|
| Lender (FIN, `grm_client` RBI variant) | Queues, SLAs above floors, escalation matrix, templates' non-legal text, branding, users, bulk templates, working calendar, scheme limits, HFC escalation text | Contact-window narrowing, offer-relay programme (counsel, LG-01), settlement grid with Board-policy evidence (J2-118), 1600-number authorisation, RE grievance and IO routing day (≤ day 20), SARFAESI and DRT attestations — tenant `legal_reviewer` | NN-12 window; no borrower-payable Equator fee in lender programmes; RB-IOS outcome taxonomy; no neutral choice or veto (NN-03) |
| Insurer (INS) | Queues, SLAs, branding, users, chargeback or claim document lists | Health-deduction schedules per policy terms; surveyor threshold display; centre map — TLR | No success fee (NN-18); Ombudsman signposting (NN-20) |
| Employer (WRK GRM, IR Code GRC) | Units, GRC membership, queues, templates' non-legal text | GRC forms per State (state_pack), retrenchment divisor (26 or 30), leave and settlement packs — TLR | Workman arbitration blocked; statutory clocks; no waiver of statutory dues |
| University (EDU GRM) | SGRC membership, queues, labels, timelines stricter than the regulations | UGC or AICTE timelines ("Equator target" labels) — TLR | Student ombudsperson route |
| POSH tenant | IC membership roster, meeting scheduling, branding, annual-report contacts | IC composition validation, external-member card, inquiry templates — TLR | Sealed store; clocks not editable; s.10 conciliation only at the aggrieved woman's written request; no POSH data in analytics or AI (NN-07) |

### V.4.7 Equator Operations Platform (`apps/ops`; detail in Appendix X §X.13, Y §Y.12, Z §Z.15 and AC §AC.17)

| Area | Examples of settings | Who (without a super admin) | Tier |
|---|---|---|---|
| Departments and teams (D3-06) | Rename, merge or add departments; cost centres; legal entity per unit | `ops_director`, `department_head` (own unit) | T |
| CRM and pipeline (X) | Pipelines and stages, stage probabilities, routing rules, speed-to-lead SLA; scoring model; discount bands | `ops_manager`, `bd_manager`; `finance_ops` for discounts | T; scoring model G; discount bands G (NN-36); stage gates G |
| Support and grievance (X) | Ticket categories, macros, queues, first-response targets | `support_lead`; `grievance_officer` for grievance categories | T; grievance clocks G (EOP-L12) |
| Marketing and social (Y) | Campaign calendar, brand kit, approval routes, posting caps | `marketing_manager` | T; claims G (NN-17); case data never (NN-16, L) |
| HRMS and payroll (Z) | Leave policy above the floor, holiday choices, appraisal cycles, pay day, payroll variance thresholds (1–50%) | `hr_manager`, `payroll_checker` | T≥G; parameters G (rule packs); monitoring limits L (NN-35) |
| Internal controls (`ctl`) | Authority matrix (`tenant.ctl.authority_rules`, DoFP), separation-of-duties additions, bank-change cooling-off (1–7 working days) | `finance_controller` with the CEO's designation; Board resolution reference for financial limits; `internal_auditor` reads | G (NN-36); cooling-off T above the L floor |
| Workspace (AC) | UPN pattern; licence (SKU) rules with maker-checker; deletion delay (30–365 days); Google Workspace enablement | `it_admin` (security lead checks SKU rules; `hr_manager` co-approves deletion delay); Google enablement: Company Secretary + DPO after the residency ADR (AC §AC.17) | T; Google enablement G (flag `platform.ops.workspace.google.enabled`, alias `ops.workspace.google.enabled`, OFF) |

### V.4.8 Group administration (detail in Appendix AD §AD.16)

| Setting | Tier | Who | Rule |
|---|---|---|---|
| Group companies register, legal entities | G | `group_admin` → Company Secretary | One row per entity; CIN validated |
| Group policy templates (security baseline, branding kit, HR policy templates, retention defaults) | T at group scope; may lock for tenants | `group_admin` | Locks visible to tenants (§V.1.3) |
| Cross-company role grants | G | `group_admin` → data owner of the providing entity, with `dpo` for duration limits | Purpose-bound, time-limited, under a Group Data-Sharing Agreement; never case or allocation data to Finbyx or Udofin (NN-38, L) |
| Shared dashboards and content | G | `group_admin` + DPO | Aggregates only unless a lawful basis is recorded |
| Professional registry (group shared service) | G | Registry owner entity (D3-05) | NN-39 |

### V.4.9 Who can change what without a super admin

| Actor | Can change unaided (T) | Can propose (G; needs the named checker) | Cannot change (L) |
|---|---|---|---|
| Party | Own profile, sign-in methods, language, accessibility, notifications, consents, representatives, publication consent | Correction of legal name (re-verification) | Legal notices, contact-window floor, case pins |
| Representative | Firm, members, digests, snippets, opt-in listing values | — | Advocate profile field set; referral rewards |
| Neutral | Availability, personal caps (within platform cap), notifications, opt-in listing | Fee preferences, bank and tax details | Allocation rules, grade, display policy for advocate-neutrals |
| Chambers owner or admin | Site content, operational case settings, staff and roles, plan | Rules of procedure, fees, legal templates, payroll parameters, salary runs | NN rules; paid placement in the institutional directory |
| Enterprise tenant admin | Users, units, queues, SLAs above floors, branding, labels, non-legal templates, dashboards | Legal templates, dispute types, contact-window narrowing, GRM clocks within the floor, SSO, API keys, retention | Statutory clocks, NN-12, NN-03, sealed-data rules |
| Ops department head | Own unit's queues, targets, rosters, labels | Authority bands, payroll parameters, workspace rules | Monitoring prohibitions (NN-35), separation of duties (NN-36) |
| Group admin | Group templates and locks | Cross-company grants, shared dashboards | Group-membership data access (NN-38) |
| `platform_admin` | Platform operations only; tenant settings only inside a tenant-granted support session (D3-14) | Platform integration settings (with CTO), emergency block (with HL) | L values (release only) |

### V.4.10 v3.1 key register (integration of 24 October 2026) *(v3.1)*

**Part A — keys first named outside an owner catalogue.** Registered here so that the registry-before-use check (D3-11, `CFG-REG-02`) passes. Where the source used a name without a scope prefix, the canonical key carries the prefix the `cfg.setting_definitions.key` CHECK requires and the source name becomes a `cfg.setting_aliases` row.

| Canonical key (alias) | Tier | Default | Bounds / rule | Who changes | Detail in |
|---|---|---|---|---|---|
| `platform.events.consumer_lag_alert_minutes` | T within platform bounds | 15 | 5–120; consent-withdrawal and leaver-revocation consumers alert at 60 s (L; NN-15, X-57) | `platform_admin` (tenant: none) | F §F.9 consumer contract |
| `tenant.legal.open_items.chase_days` | T | 14 | 7–30 | tenant `legal_ops` | J §J.9.2 |
| `platform.cfg.review_sla_business_days` | T at tenant scope within platform bounds | `standard` 2 · `elevated` 3 · `legal` 5 | 1–10 each; tenant holiday calendar | tenant admin | P00 FR-P00 review SLA |
| `platform.cfg.draft_idle_days` | T | 30 | 7–90 | tenant admin | P00 |
| `tenant.escrow.funding_window_days` | T | 14 | 3–60; a settlement may set its own term | tenant admin | P05 escrow timeouts |
| `tenant.intake.prefill_min_confidence` | T≥L | 0.85 | L floor 0.70 | `institution_admin` | P08 FR-P08-86; P11 §9 |
| `tenant.intake.doc_wait_days` | T | 14 (reminder at day 7) | 7–30 | `institution_admin` | P08 §5 overlay `awaiting_party_document` |
| `tenant.enterprise.bulk.column_map` | T | none | Per template version; diff banner when the header row changes | enterprise operator | P09 FR-P09-49 |
| `tenant.mobile.push.digest_hour` (`mobile.push.digest_hour`) | T | 18:00 local | 08:00–20:00; `hearing`, `deadline`, `signing`, `payment` never digested (L) | tenant admin; user may narrow | P12 §9 |
| `tenant.ai.d3.validation_reminder_day` | T | day 5 of the 7-day window | At least one reminder before the window closes (L) | rules version owner | P11 §9, FR-P11-32 |
| `tenant.growth.lead_ack_promise_text` | T | from the routing SLA | Must equal the configured SLA; lint blocks promises shorter than the SLA | `growth.operator` | P13 §9 |
| `platform.incidents.outage_certificate_threshold_minutes` | G | 15 (party-facing function) | ≥ 5 | incident manager → CTO | P14 §9, FR-P14-22 |
| `tenant.prelit.duplicate_window_days` (`prelit.duplicate_window_days`) | T | 180 | 30–365 | case lead | K §8.5 |
| `tenant.prelit.hold_max_days` (`prelit.hold_max_days`) | T≤L | 30, renewable once | Ceiling 30 (L) | case lead | K §8.5 |
| `tenant.prelit.reopen_window_days` (`prelit.reopen_window_days`) | T | 90 | 0–90; 0 disables reopening | case lead | K §8.5 |
| `tenant.dms.bulk_upload.max_files` | T≤L | 200 | Ceiling 200 | tenant admin | L §9.5 |
| `tenant.dms.review_sets.enabled` / `.qc_sample_percent` | T | ON / 10 | 5–25 | tenant admin | L §9.5 |
| `tenant.dms.scrutiny.batch_accept_max` | T≤L | 50 | Procedural filings only (L) | case lead | L §9.5 |
| `user.studio.review_chain` (`studio.review_chain`) | T (party organisation) | none | 0–3 reviewers, each a different user; signatory last (L) | organisation's party admin | M §8.7 |
| `tenant.studio.review.deadline_nudges` (`studio.review.deadline_nudges`) | T | T-7, T-3, T-1 | Quiet hours and contact window apply (L) | tenant admin | M §8.7 |
| `tenant.billing.plan_change_undo_hours` (`billing.plan_change_undo_hours`) | T≤L | 24 | 0–24 | billing admin | O §8.6 |
| `dashboard_pack.waiting_on` | G (legal Ruleset Studio config kind, not a setting key; maker-checker) | R seed table | Exactly one chip per case state | `legal_reviewer` | R §1.4.17 |
| `tenant.dashboard_pack.unclear_status_threshold_pct` (`dashboard_pack.unclear_status_threshold_pct`) | T | 30 | 10–60 | tenant admin | R |
| `tenant.legal_entity.dpo_deputy` | G | none | Named person; reply always carries the DPO contact (L) | tenant admin (TC) | Q §2.4 |
| `platform.mkp.search.sort_options` | G | `published_order`, `earliest_start`, `price_total_asc`, `name_az`, `nearest_venue` (ships disabled until the P19 ADR) | Never rating, bookings, plan, sponsorship or related party (L); 30-day notice | `marketplace_manager` → `compliance_officer` | AA §AA.5 |
| `platform.mkp.search_synonyms.version` (`mkp.search_synonyms`) | G | `MKP-SYN-2026.1` | Targets limited to AA.5.1 filters (L) | `marketplace_manager` → `compliance_officer` | AA §AA.5 |
| `platform.mkp.conflict_check.validity_days` | G | 14 | 7–30 | `marketplace_manager` → `legal_reviewer` | AA §AA.6.3 |
| `platform.mkp.slot_hold_minutes` | T | 30 | 15–120 | `marketplace_manager` | AA §AA.6.6 |
| `platform.mkp.on_hold_max_days` | T | 30 | 7–60 | `marketplace_manager` | AA §AA.6.7 |
| `platform.mkp.onboarding.weights` / `.reminder_days` | T | AA §AA.4.7 / 3, 7, 12 | Weights total 100 and never read by ranking (L); ≤ 3 reminders per step (L) | `marketplace_manager` | AA §AA.4.7 |
| `platform.rev.viability.amber_band_pct` / `.min_accounts_for_score` / `.decision_sla_days` | G | 10 / 10 / 10 working days | `min_accounts_for_score` ≥ 5 | CFO (→ Board for SLA) | AB §AB.7.4, §AB.8 |
| `platform.rev.viability.auto_execute` | L | false | Proposals never self-execute | release only | AB §AB.8 |
| `tenant.xpt.early_part_download` | T | ON | — | tenant admin | AC §AC.13.15 |
| `tenant.xpt.test_open.sample_pct` / `.max_fail_pct` | T | 5 / 2 | 1–20 / 0–5; minimum 20 sampled files (L) | tenant admin | AC §AC.13.15 |
| `tenant.xpt.schedules` | T (plan-entitled) | none | Monthly or quarterly; sensitive scopes still maker-checker on every run (L) | tenant admin | AC §AC.13.15 |
| `platform.xpt.download.parallel_parts` / `.auto_retries` | T | 3 / 3 | 1–6 / 0–5 | platform engineering | AC §AC.13.15 |
| `platform.eng.restore_test.missed_grace_hours` | T≤L | 24 | ≤ 72 (L) | `sre` | AE §AE.9 |
| `platform.eng.restore_test.rto_warning_pct` | T | 80 | 50–95 | `sre` | AE §AE.9 |
| `platform.eng.standard.train_time` | T | 11:00 IST, working days | Outside freezes (L) | `release_manager` | AE §AE.4 |
| `platform.eng.standard.max_failure_pct` | G | 5 | ≤ 10 | CAB | AE §AE.4 |

**Part B — v3.1 keys registered in their owner catalogues** (index only; tier, default and bounds are in the owner file):
- Appendix W §W.8: `tenant.chm.ai.hr_summary`, `tenant.chm.hr.micro_mode`, `tenant.chm.work.assignment_strategy`, `.queue_weights`, `.overload_threshold_pct`, `.leave_reassign_min_days`, `.sla_pause_reasons`, `tenant.chm.enquiry.awaiting_enquirer_close_days`, `.duplicate_window_days`.
- Appendix X §X.13: `tenant.ops.approvals.sla_by_type`, `tenant.ops.automation.shadow_hours`, `tenant.ops.cs.sentiment_override_max`, `tenant.ops.cs.provisional_missing_weight_pct`, `tenant.ops.kb.deflection.enabled`, `tenant.ops.ob.max_hold_days`, `tenant.ops.ob.template_autoselect`, `tenant.ops.reports.weekly_pack_cron`, `tenant.ops.grievance.level2_decision_days`, `tenant.ops.l2c.*`.
- Appendix Y §Y.12: `tenant.mkt.calendar.blackouts`, `.overlap_pct`, `tenant.mkt.engagement.triage_rules`, `tenant.mkt.review.buffer_hours`, `tenant.mkt.review.sla_hours.<stage>.<tier>`.
- Appendix Z §Z.15: `tenant.ctl.anomaly.shadow_days`, `tenant.ctl.delegation.on_leave.min_days`, `tenant.hr.appraisal.min_evidence_completeness_pct`, `tenant.hr.leave.coverage.min_on_duty_pct`, `tenant.hr.probation.reminder_offsets_days`, `tenant.hr.work_summary.reply_window_days`, `tenant.pay.lop_divisor`.
- Appendix AD §AD.16: `group.grants.default_duration_days`, `group.grants.max_duration_days`, `group.grants.approval_sla_working_days`, `group.assignments.decision_sla_working_days`.
- Appendix AC §AC.17: `platform.integrations.rehearsal_max_age_days`.
- Appendix AG §AG.10.5: `platform.nav.menu_version.<shell>`, `tenant.nav.*`, `tenant.inbox.*`, `tenant.bulk.undo_window_minutes`, `tenant.bulk.max_rows`, `tenant.drafts.retention_days`, `tenant.dashboards.defaults.<code>.<role>`, `tenant.nba.rules`, `user.inbox.*`, `user.ui.single_key_shortcuts`, `platform.analytics.navigation.enabled`.
- This appendix and P15 §9: `tenant.cfg.approval.escalation_working_days`, `platform.cfg.bulk.max_cells`, `tenant.cfg.bulk.undo_minutes`, `platform.notify.contact_window_floor`, `tenant.access.review_cadence.privileged_months` / `.standard_months`.

**Tier columns confirmed.** The tier columns added in v3.1 to Appendix K §8.5, L §9.5, M §8.7, N §11.6 and O §8.6 use the §V.1.1 vocabulary (L, G, T, T≥G, T≤L) and agree with Part A for every key listed there.

---

## V.5 Settings UX

| Capability | Specification |
|---|---|
| Settings home and search | One shell per portal (`/settings`, `/admin/settings`, `ops…/settings` and `/chambers/admin/settings`; *v3.1:* the Operations Platform route is host-relative and the chambers route is the P20 SCR-P20-10 route, Appendix AG §AG.3.1, D3-47(a)). The left rail lists modules from §V.4. Global search over key, label, synonyms (en, hi) and help text returns settings the user may view, with tier badges. Typing a key (e.g., `notify.quiet_hours`) jumps straight to it |
| Tier badge and "who can change this" | Every setting row shows 🔒 L / ⚖ G / ✎ T. The "Who can change this" popover lists roles, the approvers needed, the bounds, the cited rules (G) and the current effective scope |
| Inherited or overridden indicator | Chips: "Inherited from {scope}", "Overridden here", "🔒 Locked by {scope}". "Compare with parent" shows both values; "Reset to inherited" removes the override (T: immediate; G: change request). "Reset to default" sets the registered `default_value` at this scope through the same tier path, and every row links to its change history (master DoD V-1) *(v3.1)* |
| Preview | Branding: live preview in light and dark mode with a contrast report. Templates: rendered sample in each enabled language. Clocks and rule packs: the golden-case diff (§V.2.6). Notifications: a sample message on each channel with the DLT template ID |
| Validation | Inline, before save. Errors carry `CFG_*` codes with plain-language text and a fix hint. Warnings (e.g., "this narrows the contact window for 3 units") need acknowledgement |
| Change history | Per setting and per module: who, when, from and to (masked for secrets), reason, change ID, tier and approvals. Filter by actor and date; export CSV |
| Approval inbox | "Waiting for me" and "My requests", with SLA timers. Approvers see the diff, validation report, preview, impact report and citations. Approve or reject needs step-up (aal2). Bulk approval is not permitted for G-legal items |
| Approver absence and escalation | An approver marked absent (approved leave from `hr`/`chm`, or an out-of-office set in the profile) is skipped. Items go to **alternates**: the delegate named under `access.delegations` (Appendix S §6.4) or, failing one, the other holders of the same approval permission at that scope. The maker is never an alternate. A pending G item escalates once after `tenant.cfg.approval.escalation_working_days` (default 3; bounds 1–10) to the owner role's alternate, then, if still pending, to the tenant admin or, for platform scope, to the Head of Legal. Escalation never approves anything. Each re-routing writes an audit event and appears in "My requests" *(v3.1)* |
| Inbox ordering and filters | Order: items whose `effective_from` or open-item launch gate is nearest first, then SLA age. Saved filters cover "Legal only", "Money (NN-36)", "My units" and "Expiring pins". Non-legal G items of the same key may be bulk-decided with one step-up; each item is still recorded separately *(v3.1)* |
| Rollback | T: "Restore this version" on any history row (immediate, audited). G: "Propose rollback" creates a pre-filled change request |
| Export and import as JSON | `GET /v1/cfg/export` produces a signed bundle `eq-settings-1.0` (JSON + manifest + SHA-256). It contains definitions referenced, values by scope, packs adopted and locks, and never secrets (only `secret_ref` names). Import runs a dry run, shows a diff, applies T items immediately, turns G items into change requests and rejects L or out-of-bounds items (`CFG_IMPORT_CONTAINS_LOCKED`) |
| Setting packs and templates | Curated onboarding packs: "NBFC lender — RBI", "Insurer — IRDAI", "Employer — IR Code GRC", "University — UGC", "POSH IC", "Private Chambers — Solo", "Private Chambers — Small practice", "Private Chambers — Institution", "Advocate-led centre (BCI r.36 mode)", "Group company". A pack bundles T values, recommended G adaptations (as draft change requests) and rule-pack adoptions. Applying a pack is itself a change set with a preview. One-click onboarding, partial apply and pack updates: §V.5.1 *(v3.1: two chambers packs added)* |
| Bulk change | Several keys across several scopes in one change set, with an impact preview and an undo window (§V.5.2) *(v3.1)* |
| Compare and diff | Scope against scope, date against date, version against version, or tenant against its recommended pack (§V.5.3) *(v3.1)* |
| Configuration health | A dashboard (SCR-P15-14) shows overdue reviews, fallbacks in force, pending approvals, settings diverging from the recommended pack, and open items linked to the tenant |
| Command palette and shortcuts | `Ctrl/⌘ K` opens the palette. Entries: "Find setting…", "Change setting…" (opens the row), "Compare with…", "Apply pack…", "Bulk change…", "Open approvals", "Restore previous value…" (T only). `/` focuses settings search (inside the settings shell; screen-scoped key, Appendix AG §AG.5.5); `G` then `,` opens settings search from anywhere; `G` then `I` opens the Work Inbox, filtered to source `cfg` when pressed inside the settings shell; "Open configuration health" is a palette entry (no chord: `G` then `H` is Home in every shell). Bindings follow Appendix AG §AG.5.4–§AG.5.5, which prevails. Palette results respect read permissions and tier (L rows open read-only) *(v3.1)* |
| Accessibility and language | Settings UI meets WCAG 2.2 AA; labels and help text in en and hi; keyboard-only operation; changes announced to screen readers |

### V.5.1 Setting packs and one-click onboarding *(v3.1)*

1. **Suggested pack.** At tenant creation, the onboarding wizard proposes one pack. The proposal is a deterministic rule on `core.tenants.kind` and the KYB facts: RBI registration category → "NBFC lender — RBI"; IRDAI licence → "Insurer — IRDAI"; `chambers` with one natural person → "Private Chambers — Solo"; 2–10 users → "Private Chambers — Small practice"; `is_advocate_entity` → "Advocate-led centre (BCI r.36 mode)". The admin may pick another pack or "Start blank".
2. **Apply modes.** The admin can apply **all** items, or open **select items** and untick any T item or recommended G adaptation. Rule-pack adoptions marked `mandatory` (statutory packs) cannot be unticked.
3. **Preview.** The preview groups items by module and shows T items applied now, G items becoming draft change requests (with the approver each needs) and adoptions. Every row shows its current value, its pack value and any conflict with a parent lock (skipped, with the reason).
4. **Result.** One change set (`kind = pack`, with `pack_key` and `pack_version`). T items apply within 60 s; G items wait in the approval inbox. The wizard shows a checklist of "what is left": pending approvals, required tenant inputs such as the grievance officer and sender IDs, and launch gates.
5. **Pack updates.** When a platform pack version changes, adopting tenants see "Pack update available" with a diff limited to items they have not overridden. They choose apply all, apply selected or ignore. Ignored items count as divergence on Configuration Health. A pack update never overwrites a tenant override silently.
6. **Tenant packs.** "Save my configuration as a pack" captures T values and adoptions, never secrets, contact data or G values not approved. A group admin may share a group pack with the group's tenants for `group_lockable` definitions.
7. **KPIs.** Median time from tenant creation to "pack applied" ≤ 15 minutes; ≥ 90% of new tenants onboard with a pack; ≤ 5% of pack G items rejected by checkers (a higher rate means the pack's recommended adaptations need revision).

### V.5.2 Bulk change with impact preview *(v3.1)*

1. **Selection.** Choose one or more keys and one or more scopes (units by tree, filter or saved list). Then choose one action per key: set value, reset to inherited, lock or unlock. The limit is `platform.cfg.bulk.max_cells` (scope × key cells per set; default 500, L ceiling 2,000); `CFG_BULK_LIMIT_EXCEEDED` above it.
2. **Impact preview** (`POST /cfg/change-sets/preview`, side-effect-free), for each cell:
   - before → after value and its source scope;
   - validation result;
   - descendants whose resolved value would change;
   - locks that block the cell;
   - users affected (count);
   - for `case_pinned` keys, open cases that will keep their pinned value.

   Cells that fail validation are listed and excluded. The admin must acknowledge warnings such as "narrows quiet hours for 14 units".
3. **Apply.** One change set (`kind = bulk`), with one idempotency key for the whole set. T cells apply in a single transaction per scope. G cells become one change request per key per scope, linked to the set; each change request is decided on its own (bulk approval of G-legal items stays prohibited). If any T cell fails at apply time, the set becomes `partially_applied`, and the report lists applied and failed cells with a one-click "retry failed".
4. **Undo window.** T cells can be undone together for `tenant.cfg.bulk.undo_minutes` (default 15; 5–60). Undo writes new versions equal to the prior values, never deletes rows, and marks the set `undone`. After the window, or once a later change touches a cell, only per-setting rollback remains (`CFG_UNDO_WINDOW_EXPIRED`).
5. **Audit and KPIs.** One audit event per cell plus one per set. KPIs: median preview-to-apply time; share of sets undone within the window (a high share means the preview is not understood).

### V.5.3 Compare and diff *(v3.1)*

| Compare | Who | Rules |
|---|---|---|
| Scope with parent or sibling (unit A vs unit B) | Admin of both scopes | Resolved values with source scope; "differences only" toggle |
| Value now vs value at a date or version (`at=`) | Any reader of the setting | Uses `cfg.setting_changes` and `core.config_change_requests` history; shows who changed what in between |
| Tenant vs its recommended pack | Tenant admin | Same data as the divergence count on Configuration Health |
| Two tenants | `group_admin`, for tenants of the same group and `group_lockable` or policy definitions only. Equator staff only inside a support session granted by **both** tenants | Configuration values only: no personal data, contact settings, secrets or `sensitive` values (shown as "differs" without values). Never a basis for data access (NN-38) |
| Two settings bundles (`eq-settings-1.0`) or a bundle vs the live tenant | Tenant admin | Signature and hash shown; the import dry run uses the same view |

Results group by module and show tier badges. They export as XLSX or CSV. From any difference, "Copy A → B" opens a pre-filled bulk change (§V.5.2) subject to B's tiers and approvals. A comparison the caller may not make returns `CFG_COMPARE_SCOPE_DENIED`.

---

## V.6 Data model, APIs, events, errors, RBAC and audit

### V.6.1 `cfg` schema (DDL sketches; Appendix F conventions; tenant RLS unless stated)

```sql
CREATE SCHEMA cfg;

CREATE TABLE cfg.scopes (                       -- platform/group/tenant/unit nodes
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  kind text NOT NULL CHECK (kind IN ('platform','group','tenant','unit')),
  parent_id uuid REFERENCES cfg.scopes(id),
  tenant_id uuid REFERENCES core.tenants(id),   -- NULL for platform/group
  group_id uuid,                                -- grp.groups (Appendix AD)
  path ltree NOT NULL,                          -- e.g. platform.grp_infrabyx.t_equator.u_case_services
  UNIQUE (path));

CREATE TABLE cfg.setting_definitions (          -- registry (D3-11); platform rows, no RLS write for tenants
  key text PRIMARY KEY CHECK (key ~ '^(platform|group|tenant|unit|user)\.[a-z0-9_]+(\.[a-z0-9_<>]+)+$'),
  module text NOT NULL, label_i18n jsonb NOT NULL, help_i18n jsonb NOT NULL,
  tier char(1) NOT NULL CHECK (tier IN ('L','G','T')),
  risk_class text CHECK (risk_class IN ('standard','elevated','legal')),   -- G only
  value_type text NOT NULL,                     -- boolean|int|decimal|money|duration|enum|string|json|ref|secret_ref
  json_schema jsonb NOT NULL,
  allowed_scopes text[] NOT NULL,
  child_direction text NOT NULL DEFAULT 'any' CHECK (child_direction IN ('any','narrow_only','raise_only','lower_only')),
  merge_strategy text NOT NULL DEFAULT 'most_specific',
  protective_direction text,                    -- lower|higher (for 'strictest')
  bounds jsonb,                                 -- {"min":..,"max":..} or allow-list
  default_value jsonb, fallback_kind text NOT NULL DEFAULT 'last_approved', fallback_value jsonb,
  case_pinned boolean NOT NULL DEFAULT false,
  group_lockable boolean NOT NULL DEFAULT false,         -- FR-P15-11/13: may be set and locked at group scope
  affects_third_party_rights boolean NOT NULL DEFAULT false, -- FR-P15-19: tenant legal_reviewer step required
  owner_role text NOT NULL, approver_roles text[] NOT NULL DEFAULT '{}', -- OP-6 "approver_role": non-empty for every G flag
  blocking_item text,                           -- v3.1 OP-6: what keeps a G flag OFF (open-item ID, counsel opinion, vendor contract, Board approval); NULL when none
  next_review_due date,                         -- v3.1 V-1: review date for G keys (§V.2.9 cadence)
  legal_rule_codes text[] NOT NULL DEFAULT '{}', feature_flag_key text, -- core.feature_flags (legal flags)
  entitlement text,                             -- rev entitlement required (Appendix AB)
  audit_class text NOT NULL DEFAULT 'standard', -- standard|sensitive|money|security
  deprecated_at timestamptz);

CREATE TABLE cfg.setting_aliases (alias text PRIMARY KEY, key text NOT NULL REFERENCES cfg.setting_definitions(key));

CREATE TABLE cfg.setting_values (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id uuid,                               -- RLS; NULL = platform/group rows
  scope_id uuid NOT NULL REFERENCES cfg.scopes(id),
  user_id uuid,                                 -- user-scope preferences
  key text NOT NULL REFERENCES cfg.setting_definitions(key),
  value jsonb NOT NULL, version int NOT NULL,
  locked boolean NOT NULL DEFAULT false, locked_by uuid, lock_reason text,
  effective_from timestamptz NOT NULL DEFAULT now(), expires_at timestamptz,
  source text NOT NULL CHECK (source IN ('t_change','g_change_request','pack','import','seed')),
  change_ref uuid NOT NULL,                     -- cfg.setting_changes.id or core.config_change_requests.id
  UNIQUE NULLS NOT DISTINCT (scope_id, user_id, key, version));

CREATE TABLE cfg.setting_changes (              -- T-tier change log + rollback source (append-only)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, scope_id uuid NOT NULL, key text NOT NULL,
  from_value_digest char(64), to_value jsonb NOT NULL, reason text,
  actor_id uuid NOT NULL, acting_role text NOT NULL, support_session_id uuid,
  change_set_id uuid, rolled_back_by uuid, created_at timestamptz NOT NULL DEFAULT now());

CREATE TABLE cfg.change_sets (                  -- groups T changes and G change requests (packs, imports, bulk; v3.1 §V.5.1–§V.5.2)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, kind text NOT NULL CHECK (kind IN ('manual','pack','import','rollback','bulk')),
  status text NOT NULL CHECK (status IN ('draft','previewed','applied','partially_applied','rejected','undone')),
  diff jsonb NOT NULL, config_change_request_ids uuid[] NOT NULL DEFAULT '{}', created_by uuid NOT NULL, created_at timestamptz DEFAULT now(),
  pack_key text, pack_version text,              -- kind = 'pack'
  preview_hash char(64),                         -- apply refused if the live state no longer matches the preview (CFG_PREVIEW_STALE)
  idempotency_key text, undo_until timestamptz, undone_by uuid,
  UNIQUE (tenant_id, idempotency_key));

CREATE TABLE cfg.pack_change_acks (             -- v3.1: tenant acknowledgement of a rule-pack "what changed" summary (§V.2.7)
  tenant_id uuid NOT NULL, ruleset_version_id uuid NOT NULL REFERENCES core.ruleset_versions(id),
  tenant_action text NOT NULL, due_on date NOT NULL, acknowledged_by uuid, acknowledged_at timestamptz, escalated_at timestamptz,
  PRIMARY KEY (tenant_id, ruleset_version_id));

CREATE TABLE cfg.rule_pack_meta (               -- side table for core.rulesets(kind='rule_pack') versions
  ruleset_version_id uuid PRIMARY KEY REFERENCES core.ruleset_versions(id),
  pack_key text NOT NULL CHECK (pack_key ~ '^rulepack\.(IN|IN-[A-Z]{2}|INTL|[A-Z]{2}|T-[a-z0-9-]+)\.[a-z_]+\.[a-z0-9_.]+@[0-9]{4}\.[0-9]+$'),
  jurisdiction text NOT NULL, sphere text CHECK (sphere IN ('central','state','intl','tenant')),
  domain text NOT NULL, effect text NOT NULL CHECK (effect IN ('protective','computational','permissive','mixed')),
  applicability jsonb NOT NULL,                 -- predicate: dispute types, party classes, dates
  applies_to text NOT NULL DEFAULT 'events_on_or_after',
  propagation_mode text NOT NULL DEFAULT 'prospective',
  verification_status text NOT NULL CHECK (verification_status IN ('VERIFIED','SECONDARY_ONLY','NOT_CONFIRMED')),
  citations jsonb NOT NULL, source_sha256 char(64)[] NOT NULL,
  fallback_kind text NOT NULL, next_review_due date NOT NULL, volatile boolean NOT NULL DEFAULT false,
  owner_role text NOT NULL, impact_report jsonb, golden_suite_hash char(64) NOT NULL,
  change_summary_i18n jsonb NOT NULL,           -- v3.1 §V.2.7: {"en": "...", "hi": "..."}, ≤ 120 words each
  tenant_action text NOT NULL DEFAULT 'none' CHECK (tenant_action IN ('none','review_adaptation','move_pin','configure')));

CREATE TABLE cfg.rule_params (                  -- typed read model of pack parameters (pay.rule_params derives from it)
  ruleset_version_id uuid REFERENCES core.ruleset_versions(id), param_code text, jurisdiction text,
  applies_to_class text NOT NULL DEFAULT 'all', value jsonb NOT NULL, unit text,
  verification_status text NOT NULL, effective_from date NOT NULL, effective_to date,
  PRIMARY KEY (ruleset_version_id, param_code, applies_to_class));

CREATE TABLE cfg.rule_pack_adoptions (
  tenant_id uuid NOT NULL, pack_key_base text NOT NULL,           -- without @version
  mode text NOT NULL CHECK (mode IN ('auto_follow','pinned','adapted')),
  pinned_version_id uuid, pin_deadline date, overlay_ruleset_id uuid,   -- tenant adaptation (core.rulesets tenant row)
  tenant_legal_reviewer_id uuid, disclaimer_version text NOT NULL, accepted_by uuid NOT NULL, accepted_at timestamptz NOT NULL,
  PRIMARY KEY (tenant_id, pack_key_base));

CREATE TABLE cfg.golden_cases (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, pack_key_base text NOT NULL,
  name text NOT NULL, inputs jsonb NOT NULL, expected jsonb NOT NULL, is_synthetic boolean NOT NULL DEFAULT true CHECK (is_synthetic));

CREATE TABLE cfg.reg_watch_items (id uuid PRIMARY KEY DEFAULT uuidv7(), source text NOT NULL, title text NOT NULL,
  url text, published_on date, detected_at timestamptz NOT NULL, domains text[] NOT NULL,
  triage text CHECK (triage IN ('pending','no_impact','draft_change','open_item','flag_review')),
  triage_due date NOT NULL, owner_role text NOT NULL, linked_open_item_ids text[], linked_ruleset_ids uuid[],
  linked_rule_ids text[] NOT NULL DEFAULT '{}',   -- v3.1: Appendix G LR IDs (§G.4.3)
  linked_flag_keys text[] NOT NULL DEFAULT '{}',  -- v3.1: registered flag keys; ON blocked while review open
  fired_at timestamptz, review_closed_at timestamptz);

CREATE TABLE cfg.rule_challenges (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, pack_key_base text NOT NULL,
  statement text NOT NULL, sources jsonb NOT NULL, status text NOT NULL, response text, response_due date NOT NULL);

CREATE TABLE cfg.setting_packs (key text PRIMARY KEY, title_i18n jsonb NOT NULL, tenant_kinds text[] NOT NULL,
  version text NOT NULL, content jsonb NOT NULL, content_hash char(64) NOT NULL, status text NOT NULL);

CREATE TABLE cfg.support_sessions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL,
  granted_by uuid NOT NULL, staff_user_id uuid NOT NULL, scope text NOT NULL CHECK (scope IN ('read','configure')),
  starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL CHECK (ends_at <= starts_at + interval '72 hours'), revoked_at timestamptz);

CREATE TABLE cfg.temporary_access (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, user_id uuid NOT NULL,
  role text NOT NULL, reason text NOT NULL CHECK (length(reason) >= 20), approver_id uuid NOT NULL CHECK (approver_id <> user_id),
  starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL CHECK (ends_at <= starts_at + interval '72 hours'));

CREATE TABLE cfg.access_reviews (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, scope_id uuid NOT NULL,
  cadence text NOT NULL, due_on date NOT NULL, reviewer_id uuid, completed_at timestamptz, findings jsonb);
-- Owned by Appendix AC but living in cfg (full list in AC §AC.15): workspace_connections, workspace_capability_matrix, workspace_group_map,
--   integration_catalogue, system_of_record, mapping_sets, field_mappings, ledger_maps, migration_rehearsals, connector_health_checks,
--   mirror_targets, mirror_items, transliteration_tables, doc_type_abbreviations, vendor_price_refs.
-- core.open_items gains: config_category text, tier char(1), cfg_key text, rule_pack text, changed_by text, fallback_text text (X-46).
```

**Integrity.**
- Triggers:
  - `cfg.guard_tier()` rejects a `setting_values` insert for an L key, or for a G key whose `source` is not `g_change_request` / `seed`;
  - `cfg.guard_bounds()` validates `json_schema`, `bounds` and `child_direction` against the parent's resolved value;
  - `cfg.guard_lock()` rejects writes beneath a locked parent.
- `setting_changes` is append-only: `UPDATE` and `DELETE` are revoked, except setting `rolled_back_by` once.
- RLS: tenants read their own rows plus platform and group definitions; sealed-tier settings (POSH, health, safety) live in the sealed database as `posh_sealed.settings`, using the same model.

**Resolver.**
- `cfg.resolve(key, ctx)` lives in `packages/config` (server), with Redis caching (60 s; busted by `equator.cfg.setting.changed.v1`).
- It returns `{value, tier, source_scope, locked_by, fallback_applied, version, pin}`.
- Web and mobile receive resolved values only.

### V.6.2 APIs (`/v1`; Idempotency-Key on every POST; step-up for G approvals)

| Method and path | Purpose | Permission |
|---|---|---|
| GET `/cfg/definitions?module=&q=` | Search the registry (labels in the caller's locale) | `cfg:read` |
| GET `/cfg/settings?scope=&keys=` | Resolved values with provenance | `cfg:read` |
| PUT `/cfg/settings/{key}` `{scope, value, reason}` | T change (immediate) or G draft (returns the change-request ID) | `cfg:write:t` / `config:propose` |
| POST `/cfg/settings/{key}/lock` · DELETE …`/lock` | Lock or unlock for children | `cfg:lock` at the parent scope |
| POST `/cfg/settings/{key}/rollback` `{to_change_id}` | T restore / G rollback request | `cfg:write:t` / `config:propose` |
| GET `/cfg/history?key=&scope=&from=` | Change history | `cfg:read:history` |
| GET `/cfg/approvals/inbox` · POST `/config/change-requests/{id}/approve` (P00) | Approval inbox | `config:approve`, `config.approve.legal` |
| GET `/cfg/export` · POST `/cfg/import` (`dry_run=true` default) | JSON bundle `eq-settings-1.0` | `cfg:export` (G for sensitive) / `cfg:import` |
| GET `/cfg/packs` · POST `/cfg/packs/{key}/apply` | Setting packs | `cfg:pack:apply` |
| GET `/cfg/rule-packs?jur=&domain=` · GET `/cfg/rule-packs/{key}/versions` | Catalogue and versions | `cfg:read` |
| POST `/cfg/rule-packs/{key}/versions` (draft) · POST …`/{ver}/preview` · POST …`/{ver}/impact` | Author, preview, impact | `config:propose` |
| PUT `/cfg/rule-packs/{key}/adoption` `{mode, pinned_version, overlay}` | Adopt, pin or adapt | `cfg:rulepack:adopt` (+ TLR for adapted) |
| POST `/cfg/rule-packs/{key}/challenges` | Tenant rule challenge | `cfg:rulepack:adopt` |
| GET/POST `/cfg/golden-cases` | Tenant golden cases (synthetic only) | `config:propose` |
| GET `/cfg/reg-watch` · PATCH `/cfg/reg-watch/{id}` | Watch feed triage | `cfg:regwatch:triage` (legal_ops, DPO, Payroll Compliance Officer) |
| POST `/cfg/support-sessions` · DELETE …`/{id}` | Grant or revoke support access | `support_session:grant` (tenant admin roles) |
| POST `/cfg/temporary-access` · POST `/cfg/access-reviews/{id}/complete` | Just-in-time access; access reviews | `access:jit:request` / `access:review` |
| GET `/cfg/health` | Configuration health | `cfg:read` |
| POST `/cfg/change-sets/preview` · POST `/cfg/change-sets/{id}/apply` · POST `/cfg/change-sets/{id}/undo` · POST `/cfg/change-sets/{id}/retry-failed` | Bulk change with impact preview and undo (§V.5.2) *(v3.1)* | `cfg:write:t` at every target scope (G cells: `config:propose`) |
| GET `/cfg/compare?a=&b=&at=&keys=&differences_only=` | Compare scopes, dates, versions, packs or bundles (§V.5.3) *(v3.1)* | `cfg:read` on both sides; `cfg:compare:cross_tenant` for two tenants |
| POST `/cfg/packs/{key}/preview` · POST `/cfg/packs/{key}/apply` `{items[]}` | Pack preview and partial apply (§V.5.1) *(v3.1)* | `cfg:pack:apply` |
| GET `/cfg/rule-packs/{key}/versions/{ver}/what-changed` · POST …`/acknowledge` | Tenant "what changed" summary and acknowledgement (§V.2.7) *(v3.1)* | `cfg:read`; `cfg:rulepack:adopt` to acknowledge |

### V.6.3 Events (CloudEvents; IDs and keys only, never values of `sensitive`, `secret_ref` or personal data)

- **Settings:** `equator.cfg.setting.changed.v1` · `equator.cfg.setting.rolled_back.v1` · `equator.cfg.setting.locked.v1` · `equator.cfg.setting.unlocked.v1` · `equator.cfg.change_set.applied.v1` · `equator.cfg.change_set.undone.v1` *(v3.1)* · `equator.cfg.setting_pack.applied.v1` · `equator.cfg.export.created.v1` · `equator.cfg.import.applied.v1` · `equator.cfg.approval.escalated.v1` *(v3.1)*
- **Rule packs:** `equator.cfg.rule_pack.submitted.v1` · `.approved.v1` · `.scheduled.v1` · `.activated.v1` · `.superseded.v1` · `.retired.v1` · `.adopted.v1` · `.review_due.v1` · `.change_acknowledged.v1` *(v3.1)* · `equator.cfg.impact_analysis.completed.v1` · `equator.cfg.fallback.activated.v1`
- **Watch and challenges:** `equator.cfg.reg_watch.item_created.v1` · `equator.cfg.reg_watch.triaged.v1` · `equator.cfg.rule_challenge.opened.v1`
- **Access:** `equator.cfg.support_session.granted.v1` · `equator.cfg.temp_access.granted.v1` · `equator.cfg.temp_access.expired.v1` · `equator.cfg.access_review.completed.v1`
- **Owned by Appendix AC:** `equator.cfg.connector.health_changed.v1` and other connector events in the `cfg` context (AC §AC.12).

### V.6.4 Error codes (register in Appendix F §F.10.4)

| Code | HTTP | Message (en) |
|---|---|---|
| `CFG_UNREGISTERED_KEY` | 400 | This setting is not registered. |
| `CFG_TIER_LOCKED` | 403 | This value is a platform guardrail and cannot be changed here. |
| `CFG_SCOPE_NOT_ALLOWED` | 403 | This setting cannot be set at this level. |
| `CFG_LOCKED_BY_PARENT` | 409 | This setting is locked by {scope}. Request a change from them. |
| `CFG_APPROVAL_REQUIRED` | 409 | This change needs approval; a request has been created. |
| `CFG_OUT_OF_BOUNDS` | 422 | The value is outside the allowed range ({min}–{max}). |
| `CFG_DIRECTION_VIOLATION` | 422 | This setting can only be made stricter at this level. |
| `CFG_VALIDATION_FAILED` | 422 | The value is invalid. See the listed problems. |
| `CFG_CONTRAST_INSUFFICIENT` | 422 | These colours do not meet accessibility contrast rules. |
| `CFG_CITATION_REQUIRED` | 422 | A governed rule needs at least one source citation. |
| `CFG_RULE_NOT_ELIGIBLE` | 409 | A cited legal rule is not verified or not in force for this effect. |
| `CFG_GOLDEN_CASES_FAILED` | 422 | The rule pack fails one or more test cases. |
| `CFG_PREVIEW_STALE` | 409 | Run the preview again before approving. |
| `CFG_EFFECTIVE_DATE_INVALID` | 422 | The effective date does not meet the minimum lead time. |
| `CFG_RULE_CONFLICT` | 409 | Two rules give different results; a legal reviewer must decide. |
| `CFG_PIN_DEADLINE_PASSED` | 409 | Your organisation must move to the current rule-pack version. |
| `CFG_ADAPTATION_RELAXES_FLOOR` | 422 | An adaptation may only be stricter than the platform rule. |
| `CFG_TENANT_REVIEWER_REQUIRED` | 409 | A named legal reviewer of your organisation must approve this. |
| `CFG_IMPORT_SCHEMA_INVALID` | 422 | The settings file is not a valid eq-settings bundle. |
| `CFG_IMPORT_CONTAINS_LOCKED` | 422 | The file contains locked or out-of-range values; they were not imported. |
| `CFG_SECRET_IN_EXPORT` | 422 | Secrets cannot be exported. |
| `CFG_STALE_VERSION` | 412 | This setting changed since you opened it. |
| `CFG_ENTITLEMENT_REQUIRED` | 403 | This setting is available on another plan. |
| `CFG_SUPPORT_SESSION_REQUIRED` | 403 | Equator staff need a support session granted by your administrator. |
| `CFG_DELEGATION_EXCEEDS_GRANTOR` | 403 | You cannot grant more than you hold. |
| `CFG_KYB_MISMATCH` | 409 | These details differ from your verified business records. |
| `CFG_BULK_LIMIT_EXCEEDED` *(v3.1)* | 422 | This bulk change is too large. Split it into smaller sets. |
| `CFG_UNDO_WINDOW_EXPIRED` *(v3.1)* | 409 | The undo window has closed or a later change touched these settings. Restore them one by one. |
| `CFG_FLAG_REVIEW_OPEN` *(v3.1)* | 409 | This flag cannot be switched on while its legal review is open. |
| `CFG_COMPARE_SCOPE_DENIED` *(v3.1)* | 403 | You cannot compare these organisations or scopes. |
| `CFG_CHANGE_SUMMARY_REQUIRED` *(v3.1)* | 422 | Add a plain-language "what changed" summary in English and Hindi before submitting. |

`MAKER_CHECKER_SAME_USER`, `RULESET_VERSION_PINNED` and `RULESET_GUARDRAIL_VIOLATION` (Appendix F §F.10.1) are reused unchanged.

**Undo codes** *(v3.1)*. `CFG_UNDO_WINDOW_EXPIRED` is the settings change-set code (`cfg.change_sets.undo_until`, window `tenant.cfg.bulk.undo_minutes`, §V.5.2). `CFG_BULK_UNDO_WINDOW_CLOSED` (Appendix AG §AG.10.4) is the generic bulk-job code of pattern PAT-03 (`POST /bulk-jobs/{id}:undo`, window `tenant.bulk.undo_window_minutes`). The settings bulk screen uses only the first; the two are not aliases.

### V.6.5 RBAC (Cerbos resources `cfg_setting`, `rule_pack`, `cfg_pack`, `support_session`, `access_review`; extends Appendix S §6.2 "Config" column)

| Role | T | G propose | G approve | Lock | Rule packs | Support session |
|---|---|---|---|---|---|---|
| user (any) | Own user-scope preferences | — | — | — | Read adopted | — |
| unit admin | Unit scope | Unit scope | — | Unit children | — | — |
| `enterprise_admin`, `chambers_admin`, `institution_admin`, `university_admin` | Tenant scope | Yes | Standard and elevated, as tenant checker (≠ maker) | Yes | Adopt and pin | Grant |
| tenant `legal_reviewer` | — | Yes | Legal (tenant adaptations, tenant rules) | — | Adapt | — |
| `dpo` (tenant or platform) | — | Privacy and retention | Privacy and retention | — | Privacy packs | — |
| `finance_controller` / `accounts_checker` | — | Money | Money (NN-36 bands) | — | Tax packs (with tax adviser) | — |
| `legal_ops` (platform) | — | Platform packs | — | — | Author | — |
| platform `legal_reviewer`, Head of Legal | — | — | Platform legal; permissive (HL) | — | Approve, retire | — |
| `platform_admin` | Platform operations only | Integration (with CTO) | Emergency block (with HL) | Platform | — | Receives |
| `group_admin` *(v3.1 row)* | Group scope (`group_lockable` only) | Group scope | — | Group children | Read | — |
| `auditor`, `internal_auditor` | Read history | — | — | — | Read | — |

Permission `cfg:compare:cross_tenant` (§V.5.3) is held only by `group_admin`, for tenants of its own group, and by Equator staff while a support session from each compared tenant is active. *(v3.1)*

### V.6.6 Audit and tests

**Audit.**
- Every T and G change and every lock, unlock, import, export, pack application, support session, temporary access and fallback activation writes a hash-chained audit event (NN-22). History views are produced from `cfg.setting_changes` and `core.config_change_requests`.

**Tests** (in `tests/cfg/`):

| Test | Asserts |
|---|---|
| `NN-33_tier_enforced` | An L key write is refused in the API and the DB |
| `NN-33_g_requires_checker` | A G change needs a checker other than the maker |
| `NN-33_t_immediate_and_rollback` | A T change applies immediately and can be rolled back |
| `NN-33_badge_and_who` | Every rendered setting shows its tier badge and "who can change this" |
| `NN-21_pinned_rule_pack` | A pinned case keeps its rule-pack version after a new version activates |
| `CFG-OI-01` | Every open item is classified |
| `CFG-OI-02` | No key carries two tiers in §V.3.4 |
| `CFG-REG-01` | No code reads an unregistered key |
| `CFG-FB-01` | Overdue review → fallback applied and labelled |
| `CFG-MERGE-01…06` | One test per merge strategy |
| `CFG-IMP-01` | Import rejects L and out-of-bounds values |
| `CFG-SUP-01` | `platform_admin` cannot write tenant settings without a support session |
| `CFG-BULK-01` *(v3.1)* | A bulk set's preview equals its applied result. Undo inside the window restores every T cell; after the window it is refused |
| `CFG-CMP-01` *(v3.1)* | A cross-tenant compare outside one group, or without a support session from both tenants, is refused; `sensitive` values never appear in any compare output |
| `CFG-WC-01` *(v3.1)* | A rule-pack version without an en/hi change summary cannot be submitted; a version with `tenant_action ≠ none` creates an acknowledgement row for every adopting tenant |
| `CFG-ESC-01` *(v3.1)* | A G item pending past the escalation threshold is re-routed to an alternate who is not the maker; an absent approver is skipped |
| `CFG-OI-03` *(v3.1)* | The `V3` open-item loader (Appendix J §J.9 rule 5) loads one `core.open_items` row per native v3 open-item ID and per **[VERIFY — open]** marker in V–AF and P15–P21 (the Appendix J §J.9 rule 5 scope); the row count equals the scripted count of the source files |
| `CFG-RW-01` *(v3.1)* | A fired `cfg.reg_watch_items` row sets `next_review_due = today` on every linked rule and refuses switching a linked flag ON until the review closes (`CFG_FLAG_REVIEW_OPEN`) |
| `CFG-REG-02` *(v3.1)* | Every key in §V.4.10 exists in `cfg.setting_definitions` with the tier shown; every alias resolves; every G flag has `approver_roles` and, while OFF for a dependency, `blocking_item` (OP-6) |

---

## V.7 Phase addenda

### For P00

**FR-P00-V3-V01 — Retired status and rule-pack kind.**
- Add `retired` to `core.ruleset_versions.status`.
- Register config kind `rule_pack` (pinnable, risk class per effect).
- Add columns to `core.config_change_requests`: `tier`, `scope_kind`, `scope_id`, `impact_report`, `fallback_kind`.

*Acceptance:* a retired version cannot be reactivated; a pinned case still resolves it.

**FR-P00-V3-V02 — Alias registry for flags.** Every `core.feature_flags` key and every legacy flag named in Appendices J and V gets a G definition and an alias row (X-44). The seed also loads the v3 cross-file aliases below (integration of 23 October 2026). The loader collapses chains, so every alias row points directly at the scoped canonical definition (an unscoped "written form" in the right-hand column is itself registered under its scoped canonical key per X-44).

| Alias (written in a v3 draft or legacy file) | Resolves to | Source |
|---|---|---|
| `tax.eco_tds` | `billing.eco_withholding` | RVA, RVD; AB-R12 |
| `tax.eco_gst_tcs` | `billing.eco_gst_tcs` | RVA, RVD; AB-R12 |
| `cms.display_ads` | `platform.rev.ads.enabled` | Appendix AB §AB.8 (RS-25) |
| `mkt.sponsored_placement`, `marketplace.sponsored_placement` | `marketplace.paid_placement` (platform G flag, OFF; NN-34) | Appendix AA §AA.15 |
| `brevo.crm.max_requests_per_hour`, `tenant.ops.connectors.brevo.max_requests_per_hour` | `tenant.mkt.brevo.max_requests_per_hour` (one budget for the Brevo account) | Appendix AC §AC.17; X §X.13 |
| `tenant.ops.connectors.brevo.enabled` | `mkt.brevo.enabled` (single Brevo connector flag) | Appendix AC §AC.17; X §X.13 |
| `growth.brevo.sms_whatsapp.enabled` | `mkt.brevo.sms_whatsapp.enabled` | Appendix AC §AC.17 |
| `ops.adobe_embed.enabled` | `mkt.adobe_embed.enabled` | Appendix AC §AC.11.1; Y §Y.12 |
| `ops.workspace.google.enabled` | `platform.ops.workspace.google.enabled` | Appendix AC §AC.17 |
| `group.mkt.cross_sell.enabled` | `group.ops.cross_sell.enabled` | Appendix X §X.13 |
| `mkt.automation.global_pause` | `tenant.mkt.automation.global_pause` | Appendix Y §Y.12 |
| `mkt.ma03.enabled`, `mkt.ma10.enabled` | `tenant.mkt.automation.<id>.enabled` | Appendix Y §Y.12 |
| `mkt.social.meta_graph.daily_post_cap` | `tenant.mkt.social.ig_daily_cap` | Appendix Y §Y.12 |
| `mkt.social.x_v2.monthly_credit_budget_usd` | `tenant.mkt.social.x_monthly_budget_usd` | Appendix Y §Y.12 |
| `workspace.sku_exception.max_days` | `platform.hr.workspace.sku_exception_max_days` | P21 §9 |
| `meetings.classes.permitted` | `platform.ops.meetings.permitted_classes` | P21 §9 |
| `grp.modules.never_shareable`, `platform.grp.never_shareable_modules` | `platform.grp.modules.never_shareable` | Appendix AD §AD.16 |
| `audit.applicability.*` | `group.audit.applicability.*` | Appendix AE §AE.15 |
| `xpt.path_budget_below_root`, `xpt.exclusions.*` | `platform.xpt.path_budget_below_root`, `platform.xpt.exclusions.*` | Appendix AC §AC.17 |
| `feature.ops.meeting_transcripts` | `tenant.ops.workspace.meeting_transcripts.enabled` | P16 §9 |

*Acceptance:* `CFG-REG-01` green; resolving `fam.s15_prelit` returns the canonical key's value.

**FR-P00-V3-V03 — Ruleset Studio becomes "Rules and legal".** SCR-P00-07 onwards are mounted inside the Configuration Studio shell (X-43), with tier badges and the approval inbox shared with P15.

**FR-P00-V3-V04 — Open-item linkage.** `core.open_items` gains `config_category`, `tier`, `cfg_key`, `rule_pack`, `changed_by` and `fallback_text`, loaded from §V.3 (X-46). The legal-rule review reminder also emits `equator.cfg.rule_pack.review_due.v1`.

**FR-P00-V3-V05 — `REGWATCH_PORT`.** Add `REGWATCH_PORT` to the master §4.4 port list (beyond the 25 v2.1 ports; the consolidated v3.0 list in master §4.4 and P00 is 35 ports) and to `core.provider_routing.port`, with `http_fetch`, `email_in` and `fake` adapters (P15 §8). Its system of record is `cfg.reg_watch_items` (NN-40).

### For P02

**FR-P02-V3-V01 — Case and intake settings from `cfg`.** Deficiency window, response window, draft expiry, notice attempt plan, status labels, queues and tracker visibility are read through `cfg.resolve`, with the bounds in P02 §9 as definition bounds. Status labels are pinned once used in a served notice.

**FR-P02-V3-V02 — PinSet includes rule packs.** At filing, every applicable rule-pack version (domain and State packs) and the tenant adaptation version are added to the PinSet. *Acceptance:* `NN-21_pinned_rule_pack`.

### For P05

**FR-P05-V3-V01 — Money settings are G-elevated.** Payout approval threshold, refund matrix, concession limits, promo caps, mandate limits, GST and TDS maps and FX sources are `cfg` G definitions using P00 elevated or legal approvals and the `ctl` authority matrix (NN-36).

**FR-P05-V3-V02 — Tax memo flags with shadow ledgers.** `billing.model.equator_principal`, `billing.wallet.gst_mode`, `billing.eco_withholding` and `billing.eco_gst_tcs` are G definitions with `fallback_kind = conservative_value` (§V.3: J-157 to J-167). The legacy names `tax.eco_tds` and `tax.eco_gst_tcs` are aliases of the last two (X-44).

### For P07

**FR-P07-V3-V01 — Contact and channel settings.** The contact window (`narrow_only`, NN-12 floor), Sunday and holiday block, attempt caps (`lower_only`), blackout durations (`raise_only`), recording retention (`longest`) and languages become `cfg` definitions with the merge strategies in §V.1.4.

**FR-P07-V3-V02 — Telecom pack.** `rulepack.IN.telecom.tcccpr` holds the A2P declaration guard, CLI hygiene and number-series rules. `voice.equator_service_number.enabled` stays OFF with `fallback_kind = flag_off` (J-072, J-150).

### For P08

**FR-P08-V3-V01 — Vertical parameters as rule packs.** Every P08 §9 item becomes a rule-pack parameter with bounds, citations, `verification_status` and fallback. WRK gratuity, bonus, leave-encashment and maternity parameters are read from `rulepack.IN.payroll.*` (one home; Appendix Z). Calculators show "indicative" when a parameter is `SECONDARY_ONLY`.

**FR-P08-V3-V02 — State packs.** Stamp, labour (GRC, S&E), family (partition and rent fora) and court-fee data move into `IN-<ST>` packs. Unverified States use the generic fallback text listed in §V.3.

### For P09

**FR-P09-V3-V01 — Enterprise settings catalogue.** Implement §V.4.6. SLA policies, escalation matrix, GRM taxonomy and IO routing day are `cfg` definitions: floors are G; tenant targets are bounded T. POSH settings are stored in the sealed store with the same model.

**FR-P09-V3-V02 — Onboarding setting packs.** Ship the packs "NBFC lender — RBI", "Insurer — IRDAI", "Employer — IR Code GRC", "University — UGC" and "POSH IC" (§V.5) and apply one during tenant onboarding.

### For P13

**FR-P13-V3-V01 — Website and legal-entity settings.** The legal entity profile, prohibited-phrase lists, claim expiry and locale enablement are `cfg` definitions. Copy that depends on an open item reads its fallback text, e.g., `copy.probate_s213_note` (J2-051) and the Lok Adalat limit (J-136). N-tier items such as SAROD fees (J2-271) are enforced as copy-lint rules, not settings.

### For P14

**FR-P14-V3-V01 — Go-live reads configuration health.** The go-live checklist fails if:
- any launch-gate item (§J.5.2) has a G key not at its approved value and not at a declared fallback;
- any `volatile` pack is overdue for review;
- any L-tier test fails.

**FR-P14-V3-V02 — Configuration audit evidence.** Quarterly export of the `cfg` registry, adoption list, overdue reviews and fallback counts to the audit-evidence catalogue (Appendix AE §AE.8.1).
