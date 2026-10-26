# Appendix B — Fee Engine and Rate Cards (binding specification)

> Binding reference for P05 (engine, billing, payments), P03 (neutral fee bands), P06 (stamp procurement, certified copies, execution packs), P08 (vertical estimators), P09 (GRM/POSH/Enterprise/SEC), P10 (Chambers, Academy, Campus) and P13 (public fee pages). Precedence: `01_MASTER_PROMPT.md` > this appendix > phase files (for any figure, rule or formula). Version 1.0, 19 October 2026.
>
> **Every default figure in this appendix is "Subject to Board approval".** Until a schedule row carries a `board_approval_ref`, the public calculator, quotes and invoices show the "Subject to Board approval" badge (P05 FR-P05-01). Figures are editable data in Ruleset Studio (master §6), never constants in code. **Rate cards are fully customisable and approval-gated (master §7, M-01):** every schedule moves `draft → in_review → approved → published → superseded` through maker–checker with the approver role and approval evidence recorded, and nothing is quoted on a binding basis or invoiced from a schedule that is not `published` (`SCHEDULE_NOT_APPROVED`).

## B.0 Conventions and map of this appendix

| Convention | Rule |
|---|---|
| Currency | INR default. `INT` and international enterprise contracts: USD authoritative, invoiced in USD/EUR/GBP/SGD/AED (§B.6). Every table caption states its currency. |
| Number format | Indian digit grouping for INR (₹1,00,000; ₹1,27,500.00); ISO code beside foreign amounts (USD 15,000.00). |
| Tax | All amounts **exclusive of GST** unless a caption says otherwise. GST, RCM, TDS and withholding per §B.4 and §B.10. Stamp duty, registration fees, government fees, bank/trustee charges and postage are pure-agent pass-throughs at actuals (CGST Rules 2017 r.33). |
| Who pays | Every table caption names the default payer rule (enum in §B.2.4). Rules are overridable only by agreement recorded in the case or by registrar order (P05 FR-P05-04). |
| Source | Every table caption names its source (corpus digest section) or benchmark. "Equator default" means a reconciled figure set in this appendix. |
| Units | Money in integer minor units (`amount_minor BIGINT` + `currency CHAR(3)`); rates in integer parts-per-million (`rate_ppm`); no floating point anywhere in the money path (NN-13, P05 FR-P05-02). |

Map of the 15 requested deliverables:

| # | Deliverable | Section |
|---|---|---|
| (i) | FIN retail + lender bulk programme | §B.11 Cards FIN-R, FIN-L |
| (ii) | COM (incl. Fourth Schedule, emergency arbitrator, expedited) | §B.11 Cards COM-STD, COM-M |
| (iii) | FAM (incl. property, partition, succession) | §B.11 Card FAM-STD |
| (iv) | INS | §B.11 Cards INS-RET, INS-COM, INS-SUB |
| (v) | WRK + POSH SaaS | §B.11 Cards WRK-STD, WRK-POSH |
| (vi) | INT (USD + conversion policy) | §B.11 Cards INT-USD, INT-MED; §B.6 |
| (vii) | SEC (SMART ODR) | §B.11 Card SEC-SMART |
| (viii) | GRM SaaS plans | §B.11 Card GRM |
| (ix) | Enterprise API, subscriptions, volume tiers | §B.11 Card EAPI |
| (x) | Private Chambers plans | §B.11 Card CH |
| (xi) | Academy rate card and memberships | §B.11 Card ACAD |
| (xii) | Neutral fee norms and payout splits | §B.7 |
| (xiii) | Refund/cancellation matrix | §B.8 |
| (xiv) | Concessions and pro bono | §B.9 |
| (xv) | Taxes (GST/TDS/withholding) | §B.4, §B.10 |
| — | Platform-wide ancillary items (notices, eStamp, eSign, certified copies, execution packs, escrow handling) | §B.11 Card ANC |

## B.1 Fee principles (binding; tested in the P05 schedule harness, FR-P05-07)

| ID | Principle | Enforcement |
|---|---|---|
| P1 | **Published, versioned, pinned, deterministic.** One engine (`packages/rules/fees`) produces the public calculator, the filing quote, the enterprise API quote and the invoice; a case is pinned to the schedule version at filing (NN-21). No AI computes, rounds, estimates or explains a fee beyond reading back engine output (NN-01). | `NN-21_fee_quote_reproducible`; `NN-01_*` |
| P2 | **Neutral remuneration is outcome-neutral and never discounted.** A neutral's fee never varies with who wins, whether a matter settles or the amount settled/awarded, and no concession, promo, partner or volume discount reduces a neutral component. Sole exception: a regulator-fixed schedule (SEC SMART ODR, where the settled/unsettled conciliation differential is mandated). | DB CHECKs on `core.tariff_items` (P05 §7.2); harness rule (d) |
| P3 | **Success/settlement-linked fees only where lawful** — see matrix below. Neutral components may never be settlement-linked (except P2 exception). | Publish-time validator → `SUCCESS_FEE_NOT_PERMITTED` |
| P4 | **Who pays is a rule.** Repeat-player programmes (lender, insurer, employer bulk, GRM escalations) default to enterprise-pays with the individual counterparty at ₹0 for FIN/INS consumers (P09 FR-P09-31). Paying never buys any influence over appointment (NN-03) and the commercial relationship is disclosed to the counterparty (NN-16). | Payer rule per card; disclosure banner |
| P5 | **Never charged:** Dispute Explorer; any signposting event or signposting report in any vertical (incl. INS F-I19); interpretation for individual parties in the 12 enabled Indian languages (NN-23); accessibility accommodations; POSH complainants (any fee, any line); family DV safety screening and safety signposting; grievance tickets to complainants on GRM desks; DPDP data-principal requests; QR/case-status verification; the first certified copy of an outcome to each party. | Engine rejects any item whose `applies_when` can match these contexts with `amount > 0` |
| P6 | **Money handling (NN-13).** Fees and neutral fees go through the gateway with split at source; settlement sums never pass through Equator's merchant account. Escrow handling is a fee for Equator's escrow-administration service; escrowed principal sits with the bank/trustee. | `NN-13_*` tests |
| P7 | **Regulated schedules exact (NN-18).** `REGULATED_TABLE` lines are verbatim, non-discountable, non-promotable and tenant-immutable. | `REGULATED_FEE_IMMUTABLE` |
| P8 | **Access is never denied for inability to pay.** Concessions are rule-based, confidential (tier `high`), never visible to the counterparty and never conditional on settling or on any outcome. | §B.9 |
| P9 | **Advocates and partners.** No contingency or success fee for counsel (Bar Council of India Rules, Part VI, Ch. II, Section II, r.20; solicitation bar Section IV, r.36); advocate referral rewards are non-cash credits only (NN-17). | Chambers/P13 validators |

**P3 — success/settlement-linked fee matrix**

| Context | Institution fee linked to settled/awarded amount | Neutral fee linked to outcome | Basis |
|---|---|---|---|
| FIN retail (FIN-R) | Prohibited | Prohibited | NN-18; C2 gap 7 and 31 (FL success component removed) |
| FIN lender programme (FIN-L) | **Outcome-triggered flat stage fee by claim band only** (never a % of the settled sum) | Prohibited (same neutral component settled or not) | P05 FR-P05-08 |
| COM B2B mediation | Permitted only as opt-in Card COM-M, agreed in writing by all parties at filing | Prohibited | C1 H.2 (`success_fee: true`), P05 FR-P05-08 |
| COM arbitration, expert determination | Prohibited (fees run on claim value) | Prohibited | — |
| INT B2B mediation | Permitted only as opt-in INT-M settlement administration line | Prohibited | P05 FR-P05-08 |
| INS (all, incl. B2B) | Prohibited | Prohibited | Equator Insurance Rules r.27 (C2 IN-7); NN-18 |
| FAM (all) | Prohibited | Prohibited | NN-18; vulnerability |
| WRK individual matters and POSH | Prohibited | Prohibited | NN-07, NN-18 |
| WRK where every party is a business entity (e.g., co-founder exit through holding vehicles) | COM-M rules apply | Prohibited | COM analogy |
| SEC | Only as the regulator's table provides | As mandated | NN-18; R1 §8.1 |

## B.2 Data model (binding DDL for `fee_schedules`, `quotes`, `quote_lines`, `fx_rates`; `tariff_items` per P05 §7.2)

### B.2.1 DDL

```sql
CREATE TABLE core.fee_schedules (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id uuid,                                   -- NULL = platform template; tenant rows override within guardrails
  code text NOT NULL,                               -- e.g. 'FIN-R','FIN-L','COM-STD','COM-M','FAM-STD','INS-RET','INS-COM','INS-SUB',
                                                    -- 'WRK-STD','WRK-POSH','INT-USD','INT-MED','SEC-SMART','GRM','EAPI','CH','ACAD','ANC'
  version int NOT NULL,
  vertical text CHECK (vertical IN ('FIN','COM','FAM','INS','WRK','INT','SEC')),   -- NULL for cross-vertical cards
  scope text NOT NULL CHECK (scope IN ('institution','chambers_tenant','enterprise_contract','subscription','academy')),
  currency char(3) NOT NULL,                        -- authoring currency (INR; USD for INT-*)
  invoice_currencies char(3)[] NOT NULL DEFAULT '{INR}',
  rounding_unit_minor bigint NOT NULL DEFAULT 100,  -- ₹1 / USD 1.00 at item level (§B.3.4)
  unquantified_default_minor bigint,                -- FR-P05-05
  refund_policy_set text NOT NULL,                  -- §B.8 policy code(s)
  status text NOT NULL CHECK (status IN ('draft','in_review','approved','published','superseded','retired')),  -- retired = withdrawn without successor
  effective_from timestamptz, effective_to timestamptz,
  board_approval_ref text,                          -- NULL ⇒ "Subject to Board approval" badge
  regulated boolean NOT NULL DEFAULT false,
  regulator_ref text,                               -- Legal Rules Register id (Appendix G) when regulated
  source_ref text NOT NULL,                         -- corpus/benchmark citation shown in Ruleset Studio
  parent_schedule_id uuid REFERENCES core.fee_schedules(id),
  golden_suite_run_id uuid,                         -- FR-P05-07 evidence; required to leave in_review
  created_by uuid NOT NULL, approved_by uuid,
  UNIQUE (tenant_id, code, version),
  CHECK (approved_by IS NULL OR approved_by <> created_by),
  CHECK (status <> 'published' OR golden_suite_run_id IS NOT NULL),
  CHECK (NOT regulated OR regulator_ref IS NOT NULL)
);

CREATE TABLE core.quotes (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id uuid NOT NULL,
  case_id uuid,                                     -- NULL for public/indicative and enterprise bulk rows
  kind text NOT NULL CHECK (kind IN ('indicative','binding_filing','stage','enterprise','bulk_row','subscription','academy')),
  schedule_id uuid NOT NULL REFERENCES core.fee_schedules(id),
  engine_version text NOT NULL,                     -- semver of packages/rules/fees
  facts jsonb NOT NULL,                             -- §B.2.5, PII-free (party refs are case_party ids)
  facts_sha256 char(64) NOT NULL,
  fx_snapshot_ids uuid[] NOT NULL DEFAULT '{}',
  totals jsonb NOT NULL,                            -- per currency: taxable, cgst, sgst, igst, rcm_tax, pure_agent, grand
  quote_hash char(64) NOT NULL,                     -- §B.3.6
  valid_until timestamptz NOT NULL,                 -- default as_of + 30 days
  status text NOT NULL CHECK (status IN ('issued','accepted','expired','superseded','void')),
  accepted_by uuid, accepted_at timestamptz, accepted_ip inet, accepted_ua text, consent_text_version text,
  UNIQUE (tenant_id, quote_hash, kind, case_id)
);

CREATE TABLE core.quote_lines (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  tenant_id uuid NOT NULL,
  quote_id uuid NOT NULL REFERENCES core.quotes(id),
  tariff_item_id uuid NOT NULL REFERENCES core.tariff_items(id),
  item_code text NOT NULL, component text NOT NULL, revenue_owner text NOT NULL,
  payer_case_party_id uuid, payer_org_id uuid,      -- one row per item × payer after allocation
  currency char(3) NOT NULL,
  base_minor bigint NOT NULL CHECK (base_minor >= 0),
  multipliers jsonb NOT NULL DEFAULT '[]',          -- [{code, ppm}] in applied order
  gross_minor bigint NOT NULL CHECK (gross_minor >= 0),          -- after multipliers, caps, rounding
  discounts jsonb NOT NULL DEFAULT '[]',            -- [{kind, code, minor}] in stacking order
  taxable_minor bigint NOT NULL CHECK (taxable_minor >= 0),
  tax_treatment text NOT NULL,                      -- §B.4 row code
  cgst_minor bigint NOT NULL DEFAULT 0, sgst_minor bigint NOT NULL DEFAULT 0, igst_minor bigint NOT NULL DEFAULT 0,
  rcm_tax_minor bigint NOT NULL DEFAULT 0,          -- tax the recipient self-assesses (shown, not collected)
  pure_agent boolean NOT NULL DEFAULT false,
  tds_expected_minor bigint NOT NULL DEFAULT 0,
  fx_snapshot_id uuid REFERENCES core.fx_rates(id),
  inr_equivalent_minor bigint NOT NULL,
  explanation_i18n jsonb NOT NULL,                  -- deterministic template text, en + hi
  sort_order int NOT NULL,
  CHECK (cgst_minor = sgst_minor), CHECK (igst_minor = 0 OR cgst_minor = 0),
  CHECK (NOT pure_agent OR (cgst_minor + sgst_minor + igst_minor) = 0)
);

CREATE TABLE core.fx_rates (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  base char(3) NOT NULL, quote char(3) NOT NULL,    -- quote = 'INR' for primary legs
  rate_e8 bigint NOT NULL CHECK (rate_e8 > 0),      -- 1 base = rate_e8 / 10^8 quote
  source text NOT NULL CHECK (source IN ('FBIL_REFERENCE','PEG_DERIVED','PROVIDER_MID','AD_BANK_TT','MANUAL','PARTY_AGREED','REALISED')),
  as_of timestamptz NOT NULL, fetched_at timestamptz NOT NULL DEFAULT now(),
  provider_ref text, document_id uuid, approved_by uuid,
  sha256 char(64) NOT NULL,
  UNIQUE (base, quote, source, as_of),
  CHECK (source NOT IN ('MANUAL','PARTY_AGREED') OR (document_id IS NOT NULL AND approved_by IS NOT NULL))
);
-- fx_rates is world-readable and immutable (UPDATE/DELETE revoked).

CREATE TABLE core.fee_policies (                    -- P3 matrix as data; validator input
  vertical text NOT NULL, context text NOT NULL,   -- e.g. ('COM','b2b_mediation')
  settlement_linked_institution text NOT NULL CHECK (settlement_linked_institution IN ('prohibited','opt_in_written','outcome_flat_only','regulator_only')),
  settlement_linked_neutral text NOT NULL CHECK (settlement_linked_neutral IN ('prohibited','regulator_only')),
  legal_rule_id text NOT NULL,                      -- Appendix G
  PRIMARY KEY (vertical, context)
);
```

### B.2.2 Tariff-item fields (P05 §7.2 DDL is canonical) — semantics

`component` enum: `registration`, `administration`, `arbitration_admin`, `neutral_session`, `neutral_case`, `tribunal`, `emergency_arbitrator`, `appeal_tier`, `expert_fee`, `notice_digital`, `notice_physical`, `adjournment`, `late_fee`, `execution_pack`, `certified_copy`, `stamp_procurement`, `stamp_duty_passthrough`, `registration_facilitation`, `esign`, `escrow_handling`, `escrow_bank_passthrough`, `interpretation`, `translation`, `venue`, `travel_passthrough`, `settlement_admin` (COM-M/INT-M only), `subscription`, `seat`, `overage`, `usage`, `academy_fee`, `membership`, `competition_fee`, `consultation`, `drafting`. Component `settlement_principal` does not exist in the tariff model by design (NN-13).

`revenue_owner` ∈ `equator` | `neutral` | `tenant` | `university` | `third_party_passthrough`. `revenue_recognition` per P05 FR-P05-53.

### B.2.3 Rule JSON (validated by Zod + JSON Schema `fee-rule.v1`)

```jsonc
// FLAT
{ "basis": "FLAT", "amount_minor": 50000 }
// SLAB_FIXED — bands are upper-inclusive; last band upto_minor = null (open)
{ "basis": "SLAB_FIXED", "on": "claim.amount_minor",
  "bands": [ { "upto_minor": 10000000, "amount_minor": 250000 }, { "upto_minor": null, "amount_minor": 600000 } ] }
// MARGINAL — mode 'rate' (base + rate_ppm × excess over band floor) or 'interpolate' (linear between fee_from and fee_to)
{ "basis": "MARGINAL", "on": "claim.amount_minor", "min_minor": 100000, "cap_minor": 50000000,
  "bands": [ { "from_minor": 0,        "upto_minor": 10000000, "base_minor": 100000, "rate_ppm": 0 },
             { "from_minor": 10000000, "upto_minor": 50000000, "base_minor": 100000, "rate_ppm": 10000 } ] }
{ "basis": "MARGINAL", "mode": "interpolate", "on": "claim.amount_minor",
  "bands": [ { "from_minor": 100000000, "upto_minor": 500000000, "fee_from_minor": 1000000, "fee_to_minor": 2000000 } ] }
// PER_UNIT
{ "basis": "PER_UNIT", "unit": "session|half_day|day|hour|party|notice|page|signature|document|seat|employee|ticket|api_call_1000|child_consultation",
  "rate_minor": 600000, "quantity_from": "facts.sessions_planned", "free_units": 0 }
// PCT_OF_ITEM
{ "basis": "PCT_OF_ITEM", "of_item": "FIN-R.ARB.ARBITRATOR", "rate_ppm": 150000, "min_minor": 250000 }
// PCT_OF_AMOUNT
{ "basis": "PCT_OF_AMOUNT", "on": "escrow.principal_minor", "rate_ppm": 2500, "min_minor": 100000, "cap_minor": 2500000 }
// REGULATED_TABLE — verbatim; split mandatory
{ "basis": "REGULATED_TABLE", "table_ref": "LR-SEBI-001", "rows": [ { "key": "concil_settled", "neutral_minor": 480000, "institution_minor": 60000 } ] }
// PASSTHROUGH — amount supplied by provider/party fact; quote shows "at actuals"
{ "basis": "PASSTHROUGH", "amount_from": "facts.stamp_duty_minor", "pure_agent": true }
// Multipliers (applied in array order to the item's base, before caps unless cap_stage says otherwise)
{ "multipliers": [ { "code": "FOURTH_SCH_CAP", "cap_minor": 300000000, "stage": "pre" },
                   { "code": "SOLE_25", "ppm": 1250000, "when": { "==": [ { "var": "tribunal_size" }, 1 ] } },
                   { "code": "TRIBUNAL_X3", "ppm": 3000000, "when": { "==": [ { "var": "tribunal_size" }, 3 ] } },
                   { "code": "EXPEDITED_75", "ppm": 750000, "when": { "==": [ { "var": "track" }, "expedited" ] } } ] }
```

`applies_when` is JSON-logic over facts (§B.2.5) and must be total (no exceptions on missing facts; missing = false).

### B.2.4 Payer rule enum (P05 FR-P05-04)

`claimant` · `respondent` · `filer` · `equal_split` · `equal_per_party_group` · `pro_rata_custom` · `enterprise_pays` · `lender_pays` · `insurer_pays` · `employer_pays` · `employer_employee_split` (default 75:25) · `applicant` · `counterclaim_increment` · `per_party_each` · `deferred_cost_follows_event` (collected per `collect_as` default, reallocated by award/order under A&C Act 1996 s.31A). Each item may carry `collect_as` (the on-account rule) and `fallback` (`substitute_payment_allowed`).

### B.2.5 Facts contract (input to `computeQuote`)

```ts
type FeeFacts = {
  asOf: string;                       // ISO instant; engine never reads the clock
  vertical: 'FIN'|'COM'|'FAM'|'INS'|'WRK'|'INT'|'SEC'|null;
  mechanism: 'negotiation'|'conciliation'|'mediation'|'arbitration'|'med_arb'|'arb_med'|'arb_med_arb'|'expert_determination'|'grievance'|'posh_inquiry'|null;
  track: 'standard'|'expedited'|'documents_only'|'streamlined'|'emergency'|'appeal';
  subType: string;                    // taxonomy code, e.g. 'fin.ots', 'fam.partition', 'ins.health.repudiation'
  claim: { amountMinor: bigint|null; currency: string; quantified: boolean };
  counterclaim?: { amountMinor: bigint; currency: string };
  tribunalSize?: 1|3;
  stage: 'filing'|'acceptance'|'appointment'|'session'|'constitution'|'pleadings'|'hearing'|'outcome'|'closure'|'post_outcome';
  outcomeFlag?: 'settled'|'not_settled'|null;      // only for FIN-L outcome-triggered stage fees and SEC
  sessionsPlanned?: number; hearingsPlanned?: number; neutralBand?: 'I'|'II'|'III'|'IV';
  coMediation?: boolean; shuttle?: boolean; childConsultations?: number;
  parties: Array<{ casePartyId: string; role: string; ordinal: number; group?: string;
    kind: 'individual'|'sole_prop'|'msme'|'company'|'llp'|'firm'|'government'|'foreign_entity'|'foreign_individual';
    isBusiness: boolean; gstin?: string; stateCode?: string; country: string; aatoBand?: 'le_20l'|'gt_20l';
    sez?: boolean; ifsc?: boolean; invoiceCurrency: string }>;
  programme?: { planCode: string; volumeTier: 'T0'|'T1'|'T2'|'T3'; contractId: string };
  concessions?: Array<{ code: string; casePartyId: string; approvedRef: string }>;
  promoCode?: string; partnerCode?: string;
  escrow?: { principalMinor: bigint; currency: string };
  passthroughs?: Record<string, bigint>;            // stamp duty, registration fee, postage — actuals
  supplierModel: 'neutral_direct'|'equator_principal';
  neutralTax?: Record<string, { gstRegistered: boolean; stateCode?: string; resident: boolean }>;
};
```

## B.3 Algorithm (`computeQuote`) — normative pseudocode

```ts
// packages/rules/fees/src/computeQuote.ts — pure; no I/O, no clock, no LLM (NN-01). BigInt arithmetic only.
export function computeQuote(s: ScheduleVersion, f: FeeFacts, fx: FxSnapshot[], engineVersion: string): Quote {
  assertValid(f);                                              // Zod; unknown keys rejected
  assertPinned(s, f);                                          // case pinned version (NN-21) or published version for public quotes
  const ctx = deriveContext(f);                                // claim for fees = claim (+ counterclaim in increment pass), unquantified default (FR-P05-05)
  // 1. SELECT
  let items = s.items.filter(i => jsonLogic(i.applies_when, ctx) && stageMatches(i, f.stage));
  assertNeverChargedClean(items, ctx);                         // P5: throws NEVER_CHARGED_ITEM if a P5 context would bill > 0
  assertPolicy(items, ctx, s.feePolicies);                     // P3 matrix; throws SUCCESS_FEE_NOT_PERMITTED
  // 2. BASE
  const lines = items.sortBy('sort_order').map(i => ({ item: i, base: base(i.rule, ctx, linesSoFar) }));
  // 3. MULTIPLIERS → 4. MIN/MAX/CAP → 5. ROUND (item level)
  for (const l of lines) {
    let v = toRational(l.base);
    for (const m of l.item.rule.multipliers ?? []) {
      if (!jsonLogic(m.when ?? true, ctx)) continue;
      if (m.cap_minor && m.stage === 'pre') v = min(v, m.cap_minor);   // e.g. Fourth Schedule per-arbitrator ceiling
      if (m.ppm) v = v * m.ppm / 1_000_000n;                         // rational; no intermediate rounding
    }
    v = clamp(v, l.item.min_minor, l.item.max_minor ?? l.item.cap_minor);
    l.gross = roundHalfUp(v, s.rounding_unit_minor);
  }
  // 6. COUNTERCLAIM INCREMENT (FR-P05-05): for each ad valorem item, increment = fee(claim + counterclaim) − fee(claim); payer = counterclaimant
  addCounterclaimIncrements(lines, ctx);
  // 7. DISCOUNTS (only discountable lines: never neutral, never REGULATED_TABLE, never PASSTHROUGH) — §B.9.4 stacking order
  for (const l of lines.filter(isDiscountable)) applyStack(l, ['waiver','programme_plan','volume_tier','partner','promo'], ctx);
  // 8. PAYER ALLOCATION — largest remainder in minor units; residual unit to lowest ordinal (claimant first)
  const payerLines = lines.flatMap(l => allocate(l, payerRule(l, ctx), ctx.parties));
  // 9. TAX — §B.4 decision table per payer line; per-head rounding to 1 minor unit half-up
  for (const p of payerLines) Object.assign(p, tax(p, ctx, s.legalEntity));
  // 10. FX — authoring currency → payer invoice currency (§B.6); INR equivalent from authoring-currency amount
  for (const p of payerLines) Object.assign(p, convert(p, fx, ctx));
  // 11. TOTALS + HASH
  const totals = sumByCurrency(payerLines);
  const quote_hash = sha256(jcs({ engineVersion, scheduleId: s.id, version: s.version, facts: f, fx: fx.map(x => x.id), lines: payerLines, totals }));
  return { lines: payerLines, totals, quote_hash, validUntil: addDays(f.asOf, s.quote_validity_days ?? 30) };
}
```

### B.3.1 Base functions

| Basis | Formula (all in minor units) | Boundary convention |
|---|---|---|
| `FLAT` | `amount_minor` | — |
| `SLAB_FIXED` | amount of first band with `x ≤ upto_minor` | Upper-inclusive: "≤ ₹1,00,000" includes ₹1,00,000; next band starts at ₹1,00,001 |
| `MARGINAL` (rate) | `base_minor + rate_ppm × (x − from_minor) / 10^6`, then `max(min_minor)`, `min(cap_minor)` | Band chosen by `from_minor < x ≤ upto_minor` (first band includes 0) |
| `MARGINAL` (interpolate) | `fee_from + (x − from) × (fee_to − fee_from) / (upto − from)` | Same; continuous across bands is a harness check |
| `PER_UNIT` | `rate_minor × max(0, qty − free_units)`; quantities in milli-units for hours | Quantity from facts; quote shows planned quantity, invoice shows actual |
| `PCT_OF_ITEM` | `rate_ppm × gross(of_item) / 10^6` (computed after referenced item) | Cycles rejected at publish |
| `PCT_OF_AMOUNT` | `rate_ppm × fact / 10^6` with min/cap | Policy-gated if fact is a settled/awarded amount (P3) |
| `REGULATED_TABLE` | verbatim row amounts; split into neutral/institution lines | No multipliers except regulator-defined late fees |
| `PASSTHROUGH` | `passthroughs[key]` (actuals); `null` in quotes ⇒ "at actuals" | Pure agent if r.33 conditions met |

### B.3.2 Multiplier catalogue (order of application is the order listed in the item)

| Code | ppm | Used by |
|---|---|---|
| `FOURTH_SCH_CAP` (cap, stage pre) | cap ₹30,00,000 per arbitrator | COM-STD, FIN-R (> ₹1 crore), FAM-ARB — applied to the per-arbitrator Fourth Schedule figure **before** `SOLE_25` (*ONGC v Afcons Gunanusa JV*, SC, 30 Aug 2022, 2022 LiveLaw (SC) 723: the ceiling applies per arbitrator and a sole arbitrator is paid 25% 'over and above' it; `cap_stage = pre` confirmed; maximum ₹37,50,000) |
| `SOLE_25` | 1,250,000 | Fourth Schedule note (sole arbitrator +25%) |
| `TRIBUNAL_X3` | 3,000,000 | COM-STD, FIN-R, FAM-ARB (each arbitrator per Fourth Schedule) |
| `TRIBUNAL_X2_5` | 2,500,000 | INS-COM, INT-USD (three-member = 2.5 × sole) |
| `EXPEDITED_75` | 750,000 | COM-STD tribunal fee (A&C Act s.29B fast track) |
| `EXPEDITED_80` | 800,000 | INT-USD tribunal fee |
| `COMED_160` | 1,600,000 | FAM/WRK co-mediation |
| `SHUTTLE_125` | 1,250,000 | FAM/WRK shuttle surcharge on neutral session |
| `HALF_DAY_250` / `FULL_DAY_450` | 2,500,000 / 4,500,000 | Session-length conversions (§B.7.2) |
| `LATE_X2` / `LATE_150_PER_MONTH` | regulator-defined | SEC-SMART only |
| `ONLINE_ADMIN_75` | 750,000 | INT-MED online-only admin discount (institutional line; not a commercial discount) |

### B.3.3 Who-pays allocation

1. Resolve the item's payer rule (card default → case agreement override → registrar `fee_reallocation` order for future items).
2. Build payer weights: `equal_split` → each party with role ∈ {claimant side, respondent side} weight 1 per **side** (co-claimants share their side's half equally); `equal_per_party_group` → weight 1 per `group` (FAM heir branches); `per_party_each` → full amount to each party (not split); `employer_employee_split` → 75:25; `pro_rata_custom` → ratio map (registrar-approved, sums to 10^6 ppm).
3. Split `gross` in minor units by weight; floor each share; distribute residual units one by one to payers in ascending `ordinal` (claimant = 1).
4. Concessions apply **after** allocation to the eligible payer's share only (a borrower's hardship waiver never shifts cost to the lender unless the card's rule says `waiver_absorbed_by: 'equator'` — default — or `'enterprise'` under a programme contract).
5. Substitute payment: a party may pay another's deposit share (`paid_on_behalf_of_party_id`); the engine records it, it does not re-allocate it (recovery is for the tribunal under s.31A).

### B.3.4 Rounding policy (binding; ADR "rounding policy" in P05)

| Step | Rule |
|---|---|
| Rates | Integer ppm; FX `rate_e8` integer (8 dp). |
| Intermediate | Exact rational arithmetic (BigInt numerator/denominator); no rounding inside an item. |
| Item gross | Half-up (ties away from zero) to `rounding_unit_minor` (₹1 for INR schedules; 1.00 unit for USD schedules). ₹5,00,001 × marginal = ₹5,000.006 → ₹5,000. |
| Allocation | Minor units (paise/cents), largest remainder (§B.3.3). Shares may carry paise (₹2,42,187.50). |
| Discounts | Each discount step rounded half-up to `rounding_unit_minor`; floors applied after the last step. |
| Tax | Per payer line, per tax head (CGST, SGST, IGST separately), 1 minor unit half-up. CGST and SGST each computed at 9% (never 18% halved), guaranteeing `cgst = sgst`. |
| FX conversion | Cross rates via INR at 8 dp half-up; converted amounts 2 dp half-up per line; INR equivalent computed from the authoring-currency amount. |
| Proration | `price × remaining_days / cycle_days`, half-up to rounding unit; days are IST calendar days inclusive of change day. |
| Invoice total | Sum of lines; no round-off line by default. Per-legal-entity flag `invoice_round_off_to_rupee` (default OFF); GST payable in returns is rounded per CGST Act s.170 (amounts payable or refundable under the Act) by the returns process; invoice lines may carry paise. |

### B.3.5 Caps, floors and minima

- `min_minor`/`cap_minor` are **displayed** tariff features (e.g., FIN-R admin minimum ₹1,000, cap ₹5,00,000).
- `floor_minor` is an **internal** commercial floor (never displayed outside Finance) that limits commercial discount stacking: default floor = 50% of the list institutional component. Waivers (§B.9) may go below the floor to zero; commercial discounts (plan, volume, partner, promo) may not.
- Maximum combined commercial discount on any line: 50% (harness check).

### B.3.6 Hash and reproducibility

`quote_hash = SHA-256(JCS(canonical object))` (RFC 8785 JSON Canonicalization Scheme), object = engine version, schedule id + version, facts, FX snapshot ids, all payer lines, totals. Re-running stored facts on the same engine version must reproduce the hash byte-for-byte (`NN-21_fee_quote_reproducible`). Engine upgrades keep old versions callable (`engine_version` dispatch) for historical re-computation.

### B.3.7 Validation errors (RFC 9457 `code`)

`FEE_FACTS_INVALID`, `SCHEDULE_NOT_PINNED`, `SCHEDULE_NOT_APPROVED`, `NEVER_CHARGED_ITEM`, `SUCCESS_FEE_NOT_PERMITTED`, `REGULATED_FEE_IMMUTABLE`, `CONCESSION_LIMIT_EXCEEDED`, `DISCOUNT_FLOOR_BREACHED`, `FX_SNAPSHOT_STALE`, `CURRENCY_NOT_ENABLED`, `MECHANISM_NOT_PERMITTED` (master §5.2 matrix, e.g., arbitration fee item on a FAM custody matter — NN-06), `UNQUANTIFIED_CLAIM_DEFAULT_APPLIED` (warning).

## B.4 Tax computation — GST place of supply and treatment decision table (P05 FR-P05-28 implements exactly)

Supplier GSTIN state = legal entity of the line's supplier. Default rate 18% (9% + 9% or 18% IGST). Every row is a `tax_treatment` code stored on the line.

| Code | Supplier (line) | Recipient | Condition | Treatment | Authority |
|---|---|---|---|---|---|
| `T01_B2B_INTRA` | Equator / registered neutral / Chambers tenant | Registered person | GSTIN state = supplier state | CGST 9% + SGST 9% | IGST Act 2017 s.12(2)(a); CGST Act s.9 |
| `T02_B2B_INTER` | same | Registered person | different state | IGST 18% | IGST Act s.12(2)(a), s.5 |
| `T03_B2C_ADDR` | same | Unregistered with address on record | address state = supplier state → CGST+SGST; else IGST | — | IGST Act s.12(2)(b)(i) |
| `T04_B2C_NOADDR` | same | Unregistered, no address | location of supplier → CGST + SGST | — | IGST Act s.12(2)(b)(ii) |
| `T05_EXPORT_LUT` | Equator / registered neutral | Recipient outside India | consideration in convertible FX (or INR where RBI permits); not merely establishments of a distinct person | Zero-rated, "Supply meant for export under LUT without payment of IGST" | IGST Act s.2(6), s.13(2), s.16 |
| `T06_OFFSHORE_NOT_EXPORT` | same | Recipient outside India | any s.2(6) condition fails (e.g., realisation not evidenced within window) | IGST 18% | IGST Act s.7(5)(a) |
| `T07_SEZ_LUT` | same | SEZ unit/developer | authorised operations | Zero-rated under LUT | IGST Act s.16(1)(b) |
| `T08_IFSC` | same | IFSC unit | flag `tax.ifsc_zero_rating` (OFF) | Zero-rated when ON **and** the recipient is an IFSC/SEZ unit receiving the service for authorised operations (LoA/endorsement stored; LUT on file); else T01/T02 | IGST Act s.16(1)(b) (R5 §4) |
| `T09_ARB_RCM` | Arbitral tribunal (`neutral_direct`) | Business entity in taxable territory with turnover above exemption threshold | — | No GST on fee note; "Tax payable on reverse charge: Yes"; recipient self-assesses 18% (`rcm_tax_minor` shown for information) | Notification 13/2017-CT(Rate), Sl. 3 |
| `T10_ARB_EXEMPT` | Arbitral tribunal | Non-business person, or business entity whose preceding-FY aggregate turnover makes it eligible for exemption from registration under CGST s.22 (currently ₹20 lakh; ₹10 lakh in Manipur, Mizoram, Nagaland, Tripura); config `gst.reg_exemption_threshold` | — | Exempt; bill of supply | Notification 12/2017-CT(Rate), Sl. 45, as amended by Notification 21/2019-CT(Rate) w.e.f. 1 Oct 2019 |
| `T11_NEUTRAL_FWD` | Mediator, conciliator, expert, IC external member | Any | neutral GST-registered | Forward 18% under T01–T05 by place of supply | CGST Act s.9(1); s.22 threshold |
| `T12_NEUTRAL_UNREG` | same | Any | neutral not registered | No GST | CGST Act s.22 |
| `T13_IMPORT_RCM` | Non-resident neutral → Equator (`equator_principal`) | Equator | import of services | Equator pays IGST 18% under RCM; ITC per s.16 | IGST Act s.5(3); Notification 10/2017-Integrated Tax (Rate), Sl. 1 |
| `T14_PRINCIPAL_RESUPPLY` | Equator resupplying tribunal/neutral services (`equator_principal`) | Indian recipient | Equator is not an "arbitral tribunal" | Forward 18% (T01–T04) | RCM entry Sl. 3 covers only supplies by an arbitral tribunal **[VERIFY — open: tax memo to confirm characterisation of `equator_principal` resupply]** |
| `T15_PURE_AGENT` | Equator | Any | stamp duty, registration fees, government/court fees, bank/trustee charges, postage at actuals; r.33 conditions met (recipient liable, authorised, separately indicated, actual amount) | Excluded from value; shown below taxable total | CGST Rules r.33 |
| `T16_ADVANCE` | Equator | Wallet top-up / deposit / advance subscription | receipt before supply | Receipt voucher; GST at time of receipt | CGST Act s.13(2), s.31(3)(d); CGST Rules r.50 (receipt voucher), r.51 (refund voucher); s.2(31) proviso (unapplied deposits are not consideration) **[VERIFY — open: tax memo to classify wallet top-ups as deposit (tax at consumption) or advance (tax at receipt)]** |
| `T17_GOVT_TDS` | Equator / neutral | Notified government entity (s.51) | contract value > ₹2,50,000 | Recipient deducts GST-TDS 2% (1% CGST + 1% SGST, or 2% IGST) where contract value excluding tax > ₹2,50,000; credit tracked | CGST Act s.51 |

Neutral-fee billing model (P05 FR-P05-27): `neutral_direct` (default; neutral is supplier; fee note generated in the neutral's name under standing authorisation) or `equator_principal` (INT non-resident neutrals; enterprise contracts requiring a single supplier; opted-in Chambers tenants). Under `equator_principal` the neutral's line is re-tagged `revenue_owner = equator` for the customer invoice and the neutral is paid as Equator's vendor (T13 or a resident vendor invoice).

## B.5 Worked examples (golden vectors — each is a test in `packages/rules/fees/test/golden`)

All figures "Subject to Board approval". Equator legal entity GSTIN state: Delhi (07) unless stated.

**WE-01 FIN-R administration boundaries** (INR, GST exclusive). Marginal slab (Card FIN-R F2): ₹1,00,000 → ₹1,000 (minimum); ₹5,00,000 → ₹1,000 + 1.0% × ₹4,00,000 = ₹5,000; ₹5,00,001 → ₹5,000.006 → **₹5,000**; ₹20,00,000 → ₹5,000 + 0.6% × ₹15,00,000 = **₹14,000**; ₹2,50,00,000 → ₹42,000 + 0.15% × ₹1,50,00,000 = ₹64,500. Matches P05 scenario "Marginal ad valorem boundary".

**WE-02 FIN-R filing and acceptance invoices; place of supply** (INR). Claim ₹7,50,000 (OTS dispute). Borrower (individual, address Jaipur, Rajasthan) files; NBFC respondent GSTIN Delhi. Registration ₹500 payer `filer` → separate filing invoice: ₹500 + IGST ₹90.00 (T03, inter-state). Administration at acceptance: ₹5,000 + 0.6% × ₹2,50,000 = ₹6,500, `equal_split` → ₹3,250 each. Borrower invoice: IGST ₹585.00 (T03). NBFC invoice: CGST ₹292.50 + SGST ₹292.50 (T01), IRN when e-invoicing applies. Neutral: 2 sessions Band II × ₹6,000 = ₹12,000, ₹6,000 each, neutral unregistered (T12). Matches P05 GST scenario.

**WE-03 FIN-L programme line; neutral never discounted** (INR). Lender on EAPI-GROWTH (Programme plan −25%) with committed 30,000 cases/yr (tier T2 −20%). Claim ₹80,000 (band ₹50,001–₹1,00,000). Notice + negotiation ₹149 (no neutral) → ₹149 × 0.75 = ₹111.75 → ₹112 → × 0.80 = ₹89.60 → **₹90**. Conciliation settled ₹1,499 = neutral ₹400 + institutional ₹1,099 → ₹1,099 × 0.75 = ₹824.25 → ₹824 → × 0.80 = ₹659.20 → **₹659**; floors ₹75 and ₹550 respected. Line total ₹400 + ₹659 = **₹1,059** before GST (P05 scenario "Neutral component never discounted"). Lender GSTIN Maharashtra → IGST 18% on ₹749 = ₹134.82 (T02). Neutral ₹400 unregistered (T12); lender deducts TDS 10% = ₹40 once its tax-year payments to that neutral exceed ₹50,000 (Income-tax Act 2025 s.393(1) Table Sl. 6(iii)). Borrower pays ₹0. *(Stepwise rounding per §B.3.4 is normative; a single-step product gives the same ₹659.)*

**WE-04 COM arbitration ₹1,50,00,000, sole arbitrator, standard** (INR). Fourth Schedule: ₹3,37,500 + 1% × ₹50,00,000 = ₹3,87,500 → `SOLE_25` → **₹4,84,375**. Administration: ₹1,10,000 + 0.35% × ₹50,00,000 = **₹1,27,500**. Registration **₹20,000** (filer on account; `deferred_cost_follows_event`). Subtotal ₹6,31,875. Claimant company GSTIN Delhi; respondent company GSTIN Haryana. Forward GST (Equator): registration CGST ₹1,800 + SGST ₹1,800; administration ₹63,750 each → claimant CGST ₹5,737.50 + SGST ₹5,737.50; respondent IGST ₹11,475.00. Tribunal ₹2,42,187.50 each, T09 RCM: each party self-assesses ₹43,593.75. **Total tax incidence ₹1,13,737.50** (₹26,550.00 forward + ₹87,187.50 RCM) → economic total ₹7,45,612.50; per party at equal ultimate sharing ₹3,72,806.25 (P08 COM golden vector). Payouts (§B.7.6): ₹1,21,093.75 at constitution, ₹1,21,093.75 at pleadings complete, ₹2,42,187.50 at award; each corporate payer deducts TDS 10% on its share (₹24,218.75; s.393(1) Table Sl. 6(iii)).

**WE-05 COM three-member tribunal with counterclaim; expedited sub-case** (INR). Claim ₹4,00,00,000: per arbitrator ₹3,37,500 + 1% × ₹3,00,00,000 = ₹6,37,500; × 3 = ₹19,12,500; administration ₹1,10,000 + 0.35% × ₹3,00,00,000 = ₹2,15,000; split equally. Counterclaim ₹1,00,00,000: at ₹5,00,00,000 per arbitrator ₹7,37,500 × 3 = ₹22,12,500 (increment ₹3,00,000); administration ₹2,50,000 (increment ₹35,000); counterclaim registration ₹20,000 — all `counterclaim_increment` (respondent). Expedited sub-case: ₹1,50,00,000 sole, s.29B fast track → ₹4,84,375 × 0.75 = ₹3,63,281.25 → **₹3,63,281**.

**WE-06 FAM partition among heirs** (INR). Declared gross value ₹3,20,00,000 (value entered by parties from documents; never estimated by AI — NN-01). Three heir branches (groups), six parties. Registration ₹2,500 + ₹500 × 2 parties beyond four = ₹3,500 (`filer`). Property administration: ₹25,000 + 0.05% × ₹1,20,00,000 = **₹31,000**, `equal_per_party_group` → ₹10,333.34 (branch 1, lowest ordinal) / ₹10,333.33 / ₹10,333.33. Co-mediation 4 sessions Band II: ₹6,000 × 1.6 = ₹9,600 × 4 = ₹38,400 → ₹12,800 per branch (two co-mediators paid ₹19,200 each). Partition deed: NN-08 registration route → registration facilitation ₹5,000 + stamp duty and registration fee at actuals (T15). Institutional total before GST ₹39,500.

**WE-07 INS retail refund** (INR). Policyholder (Lucknow, UP) claim ₹3,20,000; band ₹1,00,001–₹5,00,000 → mediation **₹6,000** (neutral component ₹4,500; institutional ₹1,500); registration ₹1,500. The insurer has no protocol and declined to share at filing; the policyholder paid the insurer's share as substitute (`paid_on_behalf_of`). Withdrawal after notice, before first session → RP-INS-RET: 75% of mediation fee = **₹4,500** refunded; registration ₹1,500 retained. Neutral hold ₹4,500 reversed first; the neutral is GST-registered in Delhi (T11, `neutral_direct`), so the credit note in the neutral's name against its fee note reverses IGST ₹810.00 (18% of ₹4,500). Matches P05 refund scenario.

**WE-08 INS commercial arbitration settled before first hearing** (INR). B2B quantum-only, claim ₹1,20,00,000: arbitration admin ₹1,75,000; sole tribunal ₹6,50,000 (three-member would be ₹16,25,000). Payout 25% at constitution (₹1,62,500). Settlement after pleadings, before first hearing → RP-INS-COM: refund 50% of tribunal fee = ₹3,25,000 to payers pro rata; tribunal retains ₹3,25,000 (balance ₹1,62,500 released on registrar order); administration refunded at the stage rate (S4, 25%) = ₹43,750.

**WE-09 WRK separation, employee files** (INR). Registration ₹1,000 (filer: employee) → 50% concession → ₹500. Administration ₹5,000, 75:25 → employer ₹3,750; employee ₹1,250 → 50% concession → ₹625. Neutral 2 sessions Band II ₹12,000 → employer ₹9,000; employee ₹3,000 (never discounted). Escrow F&F ₹1,96,795 × 0.25% = ₹491.9875 → minimum ₹1,000 → employer ₹750 / employee ₹250. Employee pays ₹4,375; employer ₹13,500 (GST extra).

**WE-10 INT USD 2,000,000, sole arbitrator, German claimant invoiced in EUR** (USD authoritative; FX snapshot FBIL_REFERENCE USD/INR 88.2500, EUR/INR 102.4000). Registration USD 2,000 (filer) → INR ₹1,76,500.00 → **EUR 1,723.63**, zero-rated T05. Administration interpolated in USD 1m–5m band: 10,000 + (1m/4m) × 10,000 = **USD 12,500**; sole arbitrator maximum 35,000 + 0.25 × 45,000 = **USD 46,250** (three-member: USD 115,625); total USD 60,750 (P08 INT vector). Equal deposits: admin USD 6,250 each → claimant EUR 5,386.35; tribunal USD 23,125 each → claimant EUR 19,929.50. Indian respondent (GSTIN Maharashtra) pays INR: admin ₹5,51,562.50 + IGST ₹99,281.25 (T02). Sole arbitrator of neutral nationality (NN-19), resident in Singapore → `equator_principal`: Equator self-assesses IGST under RCM on the import (T13); withholding under Income-tax Act 2025 s.393(2), Table Sl. 17, at the lower of the rate in force and the India–Singapore DTAA rate. An individual arbitrator's fee falls under DTAA Art. 14 and is taxable in India only if a fixed base is regularly available in India or the arbitrator is present 90 days or more in the fiscal year; otherwise it is not chargeable (Form 145 Part D, nil withholding). Requires TRC, Form 41 (formerly 10F) and a no-fixed-base/no-PE declaration. If chargeable: Form 145 Part A (aggregate ≤ ₹5 lakh in the tax year) or Part C with Form 146 (> ₹5 lakh). CA sign-off per treaty.

**WE-11 SEC SMART ODR (flag ON)** (INR, + GST). Settled conciliation: ₹5,400 = neutral ₹4,800 + institution ₹600. Arbitration claim ₹12,00,000: neutral ₹12,000 + institution ₹1,500 = ₹13,500 (P09 scenario). Conciliation initiated 7 months after the dispute: + ₹1,000 late fee. Promo or concession on any line → `REGULATED_FEE_IMMUTABLE`.

**WE-12 Subscription proration** (INR). CH-PRO, 3 seats monthly at ₹2,999; on day 11 of a 30-day cycle add 2 seats: 2 × ₹2,999 × 20 / 30 = ₹3,998.67 → **₹3,999** + GST ₹719.82.

**WE-13 Academy revenue share** (INR). T-40-S partner cohort 40 × ₹9,500 = ₹3,80,000 − refunds ₹28,500 − gateway ₹4,200 = net ₹3,47,300 → Equator 70% ₹2,43,110 / university 30% ₹1,04,190 (P10 scenario; C5 A.6).

## B.6 Multi-currency and FX rules (binding)

| # | Rule |
|---|---|
| FX-1 | Enabled currencies: INR, USD, EUR, GBP, SGD, AED (config `currencies.enabled`). Domestic cards are INR only; `INT-USD`, `INT-MED`, international enterprise contracts and Chambers tenants outside India may invoice in any enabled currency. |
| FX-2 | **Authoring currency is authoritative.** INT schedules are authored in USD. EUR/GBP/SGD/AED amounts are derived per line: `amount_X = round_half_up_2dp(amount_USD × USDINR / XINR)`; INR equivalent = `amount_USD × USDINR` (paise). Published EUR/GBP/SGD/AED price lists are labelled "indicative at snapshot of {date}; invoiced at the quote-date snapshot". |
| FX-3 | Sources, in order: `FBIL_REFERENCE` (USD, EUR, GBP, JPY only; published around 13:00 IST since 6 Jan 2025); AED: `PEG_DERIVED` = USDINR ÷ 3.6725 (CBUAE peg); SGD (and AED if peg disabled): `PROVIDER_MID` from the licensed data provider, else `AD_BANK_TT` file. Source order per currency is configuration (`fx.sources.<CCY>`, `fx.aed_peg_enabled`). `MANUAL` and `PARTY_AGREED` need a document and `fin.approver`. |
| FX-4 | Cross rates via INR at 8 dp half-up; snapshots immutable with hash (`core.fx_rates`). |
| FX-5 | Staleness: last snapshot ≤ 3 business days (India + issuing-centre holidays) may be used; older → `FX_SNAPSHOT_STALE` and foreign-currency quotes blocked (P05). |
| FX-6 | Lock: a quote locks its snapshot for `quote_validity_days` (30). Deposits or stage fees requested after expiry use a new snapshot. A party's invoice currency is chosen at registration and fixed for the case unless all parties and the registrar agree. |
| FX-7 | GST valuation of a foreign-currency invoice uses the snapshot on the time of supply (CGST Rules r.34(2): GAAP-determined rate for the date of time of supply; CBIC customs-notified rates under r.34(1) apply only to goods and are not required); the invoice shows the INR taxable value, snapshot id, source and date. |
| FX-8 | Refunds are made in the original currency and amount (never re-converted); FX difference posts to FX gain/loss (P05 FR-P05-51). |
| FX-9 | Neutral payouts follow the neutral's rate-card currency; snapshot recorded at remittance; withholding computed in INR at that snapshot. |
| FX-10 | Sanctions (NN-19): foreign-currency collection requires `SANCTIONS_PORT` clearance; USD rails are disabled for flagged nexus cases; INR/AED alternatives only where lawful and approved by compliance. |
| FX-11 | INR track for INT: India-seated international arbitration may elect Card COM-STD in INR plus the INT surcharge (Card INT-USD line I9); the GIFT IFSC track uses Card INT-USD with treatment `T08_IFSC` when that flag is ON (R5 D5). |

## B.7 Neutral fee norms and payout splits (deliverable xii)

### B.7.1 Bands and grades (P03 FR-P03-11; C2 FL-5; C3 2.5/3.5)
*Currency INR · GST exclusive (T09–T12 per neutral) · Payer: per vertical card · Source: P03, C3 2.5/3.5 (grade rates), R4 §4.3 (IAMC ₹7,500/session anchor), R1 §8.1 (SMART ₹4,800 anchor).*

| Band | Mediation/conciliation session (≤ 2 h), range | Engine default | Grades eligible | Typical use |
|---|---|---|---|---|
| I | ₹3,000–₹5,000 | ₹3,000 | C, B | FIN-R consumer, WRK individual, FAM standard, campus |
| II | ₹5,000–₹7,500 | ₹6,000 | B, A | FAM property/multi-issue, WRK separation, FIN-R MSME |
| III | ₹7,500–₹15,000 | ₹12,000 | A | COM ≤ ₹5 crore, FIN-R large MSME, INS-COM mediation sessions beyond fixed fee |
| IV | ₹15,000–₹25,000 | ₹20,000 | A (senior endorsement) | COM > ₹5 crore, complex FAM business separation |

Quotes use the engine default until the appointed neutral's band rate is known (stage re-quote). C3's per-party-per-session figures (₹15,000–₹40,000 per party) and legacy per-party rates (C4 C.2) are **retired** in favour of per-session totals.

### B.7.2 Session definitions
Session = up to 2 hours (online default). Half-day (≤ 4 h) = 2.5 × session; full day (≤ 8 h) = 4.5 × session. Co-mediation = 1.6 × (each co-mediator receives 0.8 ×). Shuttle (FAM/WRK safety pathway) = +25%. Child-inclusive consultation (FAM) ₹8,000 per child. Outstation: travel and lodging at actuals (economy air/rail, 3-star equivalent) + one session fee per travel day.

### B.7.3 Mechanism norms

| Mechanism | Norm (default) | Source |
|---|---|---|
| Small-ticket conciliation, retail (per case) | ₹1,500–₹4,800 per case (Band I alternative to per-session) | P03; SMART ₹4,800 ceiling |
| FIN-L bulk conciliation (per case docket rate) | ₹250–₹3,000 by claim band, same whether settled or not | Card FIN-L; P05 WE-03 |
| Arbitration, retail ≤ ₹5 lakh | ₹4,800 (≤ ₹1 lakh) / ₹8,000 (₹1–5 lakh) | R1 §8.5 C |
| FIN-L documents-only arbitration | ≈ 70% of the stage fee | R1 §8.5 A |
| Arbitration > ₹5 lakh (COM, FIN-R large, FAM-ARB) | Fourth Schedule, A&C Act 1996 (inserted by Act 3 of 2016), ceiling ₹30,00,000 per arbitrator; sole +25% | R1 §8.2; *ONGC v Afcons* |
| Emergency arbitrator | COM ₹2,40,000 of ₹3,00,000; INT USD 12,500 default (10,000–15,000 fixed by Registrar) | C3 1.5; R5 §6.1 |
| Appellate tier (D4) | Each of 3 members: 40% of the first-instance per-arbitrator Fourth Schedule figure (before sole +25%) | Equator default |
| Expert determination | Band III day rate ₹30,000/day; Band IV ₹50,000/day; fixed by Registrar on terms of reference | Equator default |
| INT arbitrator | Card INT-USD scale maximum; or hourly USD 400–600 for > USD 25m by agreement | R5 §6.1 |
| POSH IC external member | ₹60,000/yr retainer; ₹15,000 per inquiry (employer pays; statutory ₹200 per day plus travel under POSH Rules 2013 r.3 is a floor, not the market rate) | C3 2.5; P09 FR-P09-36; R4 §4.3 |

### B.7.4 Cancellations, adjournments, chosen-neutral premium
- Party-caused adjournment: ₹1,000 administration (`applicant`) + 50% of the session neutral fee to the neutral if cancelled < 48 hours before start. Neutral-caused cancellation: no fee; rescheduling priority.
- Chosen-neutral premium (non-repeat-player matters only; FAM excluded — no direct fee negotiation): a jointly chosen neutral may quote one band above default with all parties' written consent. Never available where NN-03 institutional allocation applies.

### B.7.5 Billing model
Default `neutral_direct` (fee note in the neutral's name; Route linked account; party may be TDS deductor). `equator_principal` for INT non-resident neutrals, enterprise contracts requiring a single supplier, pro bono matters funded by Equator, and opted-in Chambers tenants.

### B.7.6 Payout milestones (Temporal `PayoutReleaseWorkflow`; P05 FR-P05-22)

| Fee type | Release schedule | Early termination |
|---|---|---|
| Mediation/conciliation session | 100% on `session.held` + minutes/attendance filed, T+2 working days | Unheld sessions reversed |
| Retail conciliation per case | 50% on first session held; 50% on proceeding closed (any outcome) | Registrar fixes pro rata |
| FIN-L docket (neutral component) | 100% on stage completion (proceeding closed, any outcome) | Reversed if no neutral activity |
| Arbitration (oral) | 25% `tribunal.constituted`; 25% `pleadings.completed`; 50% `award.delivered` | Registrar order fixes amount (s.38-style); unreleased holds reversed |
| Documents-only arbitration | 30% constitution; 70% award | same |
| Emergency arbitrator | 100% on EA order or withdrawal after appointment | — |
| Appellate tier | 50% constitution; 50% appellate decision | — |
| Expert determination | 40% on terms of reference signed; 60% on determination | — |
| POSH external member | Retainer quarterly in arrears; inquiry fee on `posh_inquiry.report_submitted` (opaque token only, NN-07) | Pro rata by IC presiding officer certificate |
| Arb-med sealed award | Award-stage 50% released at sealing (hash recorded) | — |

Releases > ₹2,00,000 per transfer need `fin.approver`. A neutral removed under A&C ss.13–14 receives only what the registrar fixes.

### B.7.7 Panel administration fee (deducted from neutral transfer; invoiced monthly to the neutral with GST)

| Engagement type | Default % of neutral fee | Rationale |
|---|---|---|
| Equator-administered case (institutional fee already charged to parties) | 0% | No double charge |
| FIN-L / INS batched days / bulk dockets | 0% | Institutional component priced separately |
| Marketplace booking (parties book a listed neutral directly, non-administered) | 15% | R4 §4.4 (15–20% take). *Internal note only, never public (NN-17; AF-S29; Appendix AB AB-R10): the competitor take-rate in R1 §8.3 is unsourced third-party data.* v3.0: applies only on the Private Practice Marketplace (surface (ii)) and only to non-advocate providers (Appendix AA X-59(c); master X-62(d)); plan-dependent rates and the advocate-neutral flat fee await the Board and counsel (AFC-B-02) |
| POSH external-member engagement via marketplace | 15% | R4 §4.4 |
| Chambers overflow referral to an Equator neutral | 10% | P10 FR-P10-10 referral default |
| SEC | 0% (institution fee fixed by regulator) | NN-18 |

## B.8 Refund and cancellation matrix (deliverable xiii)

*Currency: as invoiced · GST: credit note reverses GST on the refunded taxable value (CGST Act s.34) · Refund to original instrument (RBI PA Directions, 15 Sep 2025) · Neutral holds reversed before Equator's share · Pass-through items refunded only if the provider refunds · Source: C1 H.6, C2 IN-5, C5 A.5, P05 FR-P05-32, Equator default.*

**RP-STD-MED** — mediation/conciliation (FIN-R, COM mediation, FAM, WRK, INT-MED)

| Stage | Registration | Administration | Neutral fees paid |
|---|---|---|---|
| S0 Rejected as outside the Rules / Equator cannot act | 100% | 100% | 100% |
| S1 Withdrawn before notice served | 0% | 100% | 100% |
| S1a Respondent does not respond / non-commencement | 0% | 100% | 100% |
| S1b Unsuitable at triage or signposted | 0% | 100% | 100% |
| S2 After notice, before appointment | 0% | 75% | 100% |
| S3 After appointment, before first session | 0% | 50% | 100% (less any < 48 h cancellation fee) |
| S4 After first session | 0% | 0% | Unheld prepaid sessions 100% |
| Duplicate/erroneous payment; Equator or neutral cancels | 100% of affected amount | | |

**RP-STD-ARB** — arbitration (COM-STD, FIN-R arbitration, FAM-ARB, INT-USD)

| Stage | Registration | Administration | Tribunal deposits |
|---|---|---|---|
| S0 Outside the Rules | 100% | 100% | 100% |
| S1 Withdrawn before notice | 0% | 100% | 100% |
| S2 After notice, before constitution | 0% | 75% | 100% |
| S3 After constitution, before pleadings complete | 0% | 50% | 75% |
| S4 After pleadings, before first hearing | 0% | 25% | 50% |
| S5 After first hearing | 0% | 0% | Registrar fixes per work done; default 25% of unreleased |
| EA application rejected before EA appointment | 0% | 100% of EA admin | 100% of EA fee |
| Consent award on settlement | Stage reached at settlement | | |

**RP-INS-RET** (C2 IN-5, exact): other side does not respond → 100% mediation fee (registration retained); withdrawal before notice → 100% mediation fee; after notice before first session → 75%; after first session → 25%; unsuitable at triage → 100% except registration; outside the Rules (e.g., third-party motor) → 100% of everything. **RP-INS-COM**: RP-STD-ARB, except settlement before first hearing → 50% of tribunal fee (C2 IN-5).

**RP-FIN-L**: stage fees are post-paid on stage completion → refunds only for duplicate/erroneous charges or billing disputes (credit note). **RP-REG (SEC)**: per the regulator's instrument; the Master Circular has no general refund rule: the successful party's deposits are refunded subject to the award, and the MII may release up to ₹5 lakh of the MP's deposit to the investor pending award → Equator refunds duplicates only.

**RP-SUB** (GRM, POSH, EAPI, CH, memberships): monthly fees non-refundable; annual plans non-refundable except Equator convenience termination or Equator material breach (pro rata); unused allowances lapse; wallet balances refundable on termination net of dues (P05 FR-P05-36, FR-P05-39).

**RP-ACAD** (C5 A.5; P10 FR-P10-30): participant cancellation > 21 days 90%; 8–21 days 50%; ≤ 7 days or after start nil; Institute cancels → 100% or transfer; medical → transfer within 12 months; safeguarding/POSH complaint → withdrawal without loss of fee; refunds ≤ 21 days. Institution-paid programmes: cancellation > 30 days nil; 15–30 days 25%; 7–14 days 50%; < 7 days 100% + costs; one free postponement > 21 days. Competitions: 50% before draw, nil after. Institutional membership: non-refundable except Institute convenience termination (pro rata).

**v3.0 refund codes for new stream types (23 October 2026; Appendix AB §AB.5; AFC-B-08).** Defaults, *Subject to Board approval*; refund to the original instrument with a credit note reversing GST (CGST Act s.34).

| Code | Applies to (Appendix AB stream) | Rule (default) |
|---|---|---|
| RP-ROOM | RS-16 hearing-room rental; RS-17 venue bookings | Cancellation ≥ 48 h before start: 100%; 24–48 h: 50%; < 24 h: nil. Equator or venue cancels, or the room fails for > 15 minutes for a platform reason: 100% plus free rebooking |
| RP-SVC | RS-26, RS-27, RS-39, RS-40 services | Milestone fees refundable before work on the milestone starts; non-refundable after acceptance; Equator-caused failure of a milestone: that milestone's fee refunded; termination for convenience by Equator: pro rata |
| RP-MKP | RS-18 marketplace take; RS-52 buyer processing fee | Follow the booking: refunded in full when the booking is refunded under the provider's published stage rules; Equator's take is never retained on a booking refunded for provider non-delivery |
| RP-ADS | RS-19 sponsored listing; RS-25 advertising | Monthly in advance; pro-rata refund for any period in which Equator removes the slot (eligibility loss, label-audit failure, kill switch); no refund for sponsor-initiated mid-month cancellation |
| RP-EVT | RS-23 events | > 14 days before the event: 90%; 7–14 days: 50%; < 7 days: nil, with free transfer to another person; Equator cancels: 100% or transfer |
| RP-DIG | RS-24, RS-34, RS-37, RS-49 digital goods | Refundable only if not delivered or materially defective within 7 days of delivery |
| RP-ASSESS | RS-21 EQAP sitting | ≥ 7 days before the sitting: 100%; one free reschedule; < 7 days: 50%; medical or Equator cancellation: free reschedule or 100% |

## B.9 Concessions, promos and pro bono (deliverable xiv)

### B.9.1 Concession catalogue
*Currency INR · applies to the eligible individual payer's share of institutional lines (registration, administration, institutional components) only — never neutral, regulated or pass-through lines · cost absorbed by Equator unless a programme contract says enterprise · Source: C2 FL-5, IN-5; C3 2.5, 3.5; C4 A.6; Equator default.*

| Code | Eligibility (evidence) | Default concession | Approval |
|---|---|---|---|
| CN-LEGALAID | DLSA/legal-aid/consumer-organisation referral (letter verified) | 100% institutional | Auto |
| CN-COURT | Court-referred matter | As directed by the referring order | Registrar |
| CN-HARD | Household income below threshold (default ₹3,00,000 p.a., self-declaration) | 50–100% sliding: < ₹1,50,000 → 100%; ₹1,50,000–₹3,00,000 → 50% | Auto ≤ ₹5,000 value; else case_manager |
| CN-SENIOR | Age ≥ 60 from KYC (Maintenance and Welfare of Parents and Senior Citizens Act 2007 s.2(h)) | 50% | Auto |
| CN-PWD | Person with disability (UDID; RPwD Act 2016) | 50% | Auto |
| CN-INS-SMALL | INS retail claim < ₹50,000 | 100% registration + mediation | Auto |
| CN-INS-DEATH | Death claim by nominee/heir | 100% registration | Auto |
| CN-GOVT-SCHEME | PMJAY, PMFBY, PMSBY, PMJJBY policies | 100% | Auto |
| CN-MSE | Micro/small enterprise (Udyam verified) in COM | 50% registration + administration (resolves C3 "50% of the above") | Auto |
| CN-EMPLOYEE | WRK individual employee/worker | 50–100% registration + administration (means-based) | case_manager |
| CN-DV | FAM DV safety pathway | Screening and signposting free (P5); mediation only if safe, with CN-HARD applied | Safeguarding lead |
| CN-PROBONO | §B.9.2 | 100% institutional | Registrar lead |

Concessions are never outcome-conditional (P8); evidence is tier `high`; one code per payer per item (highest wins), then the commercial stack.

### B.9.2 Pro bono policy
Quota: up to 2% of the previous month's new cases per vertical (minimum 5 matters per month platform-wide). Eligible: individuals meeting CN-HARD, community disputes with claim < ₹1,00,000 (C4 A.6), matters referred by partner clinics or campus mediation cells. Institutional fees nil. Neutral: volunteer from the pro bono roster (express per-matter consent, counted for CPD) or Equator-funded at Band I under `equator_principal` (Equator deducts TDS). Pro bono status is never disclosed to the counterparty and never affects allocation.

### B.9.3 Approval limits (value = total concession per payer per case)

| Approver | Limit |
|---|---|
| Rule-based auto-approval (evidence-verified codes) | No limit for listed codes |
| `case_manager` | ≤ ₹5,000 |
| `registrar` | ≤ ₹50,000 |
| `fin.approver` | > ₹50,000 |
| Pro bono designation | Registrar lead + quota check |

Maker ≠ checker; a case manager cannot approve own proposal.

### B.9.4 Commercial discounts and stacking
Order: waiver (B.9.1) → programme plan (EAPI/insurer subscription) → volume tier → partner discount (≤ 10% of institutional lines) → promo (only `promo_eligible` lines; ≤ 50%; validity ≤ 90 days; max uses; e.g., C4 "first 50 cases at 50% off"). Multiplicative, each step rounded; floor and 50% maximum commercial discount per §B.3.5. Promos are never offered to served respondents without separate marketing consent (NN-16). Promo request: growth → `fin.approver`.

## B.10 Taxes — GST/TDS/withholding treatment table (deliverable xv)

*All rows require sign-off in the signed tax memo (P05 exit gate) before go-live; statutory references verified Oct 2026. Income-tax Act 2025 applies to payments on or after 1 Apr 2026 (s.393 Table entries cited per row; old 1961 Act sections shown for mapping in config `tds_map`).*

| Item | GST (default) | SAC (proposed) | TDS / withholding | Who deducts / pays |
|---|---|---|---|---|
| Registration, administration, case management, execution pack, certified copies | 18% forward (T01–T08) | 998215 (arbitration and conciliation services) | Corporate payer may deduct on professional/technical fees: s.393(1) Table Sl. 6(iii) (old s.194J; 10% professional / 2% technical) once the ₹50,000 tax-year threshold is crossed | Payer; Equator tracks Form 26AS/AIS |
| Arbitrator fees (`neutral_direct`) | RCM to business > threshold (T09); exempt otherwise (T10) | 998215 | 10% (2% FTS), threshold ₹50,000 per tax year per payee: Income-tax Act 2025 s.393(1) Table Sl. 6(iii) (old s.194J) | Corporate payer; Equator where principal |
| Mediator/conciliator/expert/IC member fees | Forward 18% if neutral registered (T11), else nil (T12) | 998215 / 998399 | as above | as above |
| Non-resident neutral (`equator_principal`) | Equator RCM on import (T13) | 998215 | s.393(2) Table Sl. 17 (old s.195) at the lower of the rate in force and the DTAA rate, with TRC (s.159(8)), Form 41 (old 10F), no-PE/no-fixed-base declaration; Form 145 (old 15CA) every remittance, Form 146 (old 15CB) where chargeable and > ₹5 lakh aggregate in the tax year (r.220) | Equator |
| Equator fees to foreign parties | Export under LUT (T05) | 998215 | Foreign payer may withhold under its law; INT terms require gross-up; Equator claims foreign tax credit | Foreign payer |
| SaaS subscriptions (GRM, POSH, EAPI, CH) | 18% forward; export if foreign | 998315 (hosting/IT infrastructure) or 997331 (software licence); choice in tax memo | Payer may treat as technical services (2%) or royalty (10%) under s.393(1) Table Sl. 6(iii) | Payer |
| Academy courses, workshops, memberships (Equator ADR Institute) | 18% forward (no educational exemption assumed) | 999293 | Trainer payouts: 10%, threshold ₹50,000 (s.393(1) Table Sl. 6(iii)) | Institute |
| Competition fees, sponsorships | 18% | 998596 / 998397 | Sponsor may deduct (advertising/contract rates) | Sponsor |
| University revenue share | 18% on university's invoice if registered | 999293 | Per university's tax status (exemption certificate) | Equator |
| Escrow handling (Equator fee) | 18% | 998599 | as first row | Payer |
| Escrow bank/trustee charges, stamp duty, registration fees, government fees, postage at actuals | Pure agent (T15) | — | — | — |
| eSign (actuals + ₹20) and eStamp procurement fee (₹49) | 18% on the whole eSign line (input to Equator's supply, not pure agent); 18% on procurement fee only | 998599 | — | — |
| Interpretation, certified translation (where chargeable) | 18% | 998395 | — | — |
| Wallet top-ups, deposits on account, advance subscriptions | GST at receipt (T16) | as underlying | — | — |
| Government recipients | GST-TDS 2% (T17) | — | — | Recipient |
| Partner (non-professional partners only: DSA, software vendors, associations) commissions | Partner's GST | 998599 | Commission TDS: s.393(1) Table Sl. 1(ii) (old s.194H), 2%, threshold ₹20,000 per tax year; no referral reward to advocates, CAs, CSs or CMAs (NN-34; master X-62; [RE] F1.5; AFC-B-07) | Equator (P13) |
| E-commerce-operator exposure (party payments for neutral services collected on the platform) | GST-TCS 0.5% under CGST s.52 with compulsory registration (s.24), if Equator is an ECO for these supplies | — | TDS 0.1% under s.393(1) Table Sl. 8(v) (old s.194-O; ₹5 lakh resident individual/HUF threshold with PAN/Aadhaar, none otherwise — [RE] F3.4), interacting with the payer's Sl. 6(iii) deduction; GST-TCS is not collected on exempt or reverse-charge supplies | Equator, if applicable — **[VERIFY — open: tax memo before go-live]**; config `billing.eco_withholding`, `billing.eco_gst_tcs` default OFF (LR-TAX-007/008; `tax.eco_tds`, `tax.eco_gst_tcs` are aliases only — Appendix AA X-59(h)) |

| Hearing-room rental for non-administered matters (RS-16); venue-partner commission (RS-17) | 18% forward (master §7 default; confirm in tax memo) | SAC per tax memo **[VERIFY]** | Venue may deduct TDS s.393(1) Sl. 1(ii) on commission, if applicable | Payer |
| Practice-software rental to tenants (RS-36); service-provider tools plan (RS-57) | 18% forward (master §7 default; confirm in tax memo) | SaaS SAC per tax memo **[VERIFY]** | as SaaS row | Payer |
| Event tickets and exhibitor packages (RS-23) | 18% forward | Sponsorship 998397; competition 998596; tickets per tax memo **[VERIFY]** | Sponsor may deduct | Payer |
| Publications and digital goods (RS-24) | 18% forward (master §7 default; confirm in tax memo) | SAC per tax memo **[VERIFY]** | — | Payer |
| Sponsored listings (RS-19) and display advertising (RS-25) — both OFF | 18% forward | SAC per tax memo **[VERIFY]** | Advertiser may deduct TDS | Payer |
| Notarisation facilitation (RS-46) | Facilitation fee 18% forward; notary fee pure agent (T15) | SAC per tax memo **[VERIFY]** | — | Payer |

*v3.0 rows above added 23 October 2026 from Appendix AB §AB.3.2 (AFC-B-09); figures are unchanged and every row needs tax-memo sign-off.*

## B.11 Default rate cards (all "Subject to Board approval"; seeded by P05 as `core.fee_schedules` v1)

Item codes are `{CARD}.{LINE}`; P08 estimator keys are listed as aliases where they exist.

### Card ANC — platform-wide ancillary items
*INR · GST exclusive (pass-throughs per T15) · Payer: as stated; default `equal_split` · Source: R1 §8.3 (Sama), §8.5 A; P10 add-ons; C3 1.5/2.5/3.5; C4 C.2.*

| Line | Fee | Payer | Note |
|---|---|---|---|
| ANC.EXPLORER | ₹0 | — | P5 |
| ANC.CONSULT | ₹999 (30 min) / ₹1,999 (60 min), credited against registration if filed within 30 days | requester | Replaces live-site ₹1,000/30 min (R4 §1) |
| ANC.NOTICE.DIGITAL | Included in registration (email, SMS, WhatsApp, in-app; 3 attempts) | — | FIN-L prices per stage |
| ANC.NOTICE.PHYSICAL | Speed Post/registered post at actuals + ₹50 handling per address | filer | Actuals T15 |
| ANC.ESTAMP | ₹49 procurement per stamp certificate + duty at actuals | per instrument rule | P06 FR-P06-15 |
| ANC.ESIGN | Provider charge at actuals + ₹20 per signature | per signer's party | P10 alignment |
| ANC.STAMP.PHYSICAL | Franking/e-SBTR/stamp-paper facilitation ₹500 per instrument + duty at actuals | per instrument rule | physical-only states |
| ANC.REGN.FACIL | Registration-route facilitation (Registration Act 1908 s.17 instruments; NN-08) ₹5,000 per instrument + statutory fees at actuals | equal_split | FAM/COM property |
| ANC.CERT.COPY | First copy to each party ₹0; additional ₹500 per copy | requester | P06 FR-P06-18 |
| ANC.EXEC.PACK | ₹2,500 (claim ≤ ₹50 lakh) / ₹5,000 (above); FIN-L per card | requester | P06 |
| ANC.ESCROW | 0.25% of escrowed principal, min ₹1,000, cap ₹25,000 (INS-RET cap ₹2,500) + bank/trustee charges at actuals | equal_split (WRK 75:25) | Unifies FL 0.20%, WRK/FAM 0.25%, FAM model 0.5%, INS flat ₹2,500 |
| ANC.ADJOURN | ₹1,000 + §B.7.4 neutral late-cancellation share | applicant | C2/C3 |
| ANC.REMEDIATION | Return-to-mediation session on breach (P06 FR-P06-22): one session at the case's band rate, no administration | party in breach per instrument; else equal_split | — |
| ANC.INTERP | ₹0 for individual parties in enabled Indian languages (P5); B2B/INT certified interpretation and translation at actuals + 10% | requesting party | — |
| ANC.VENUE | Equator room ₹5,000 per half-day; third-party venue at actuals | equal_split | C4 C.2 |

### Card FIN-R — Financial retail (individual and MSME borrowers; NI Act s.138; lenders outside a programme)
*INR · GST exclusive · Payer: registration `filer`; administration and neutral `equal_split` (Rules Art.16); arbitration deposits `equal_split` on account → s.31A · Source: C2 FL-5 (reconciled), R1 §8.5 C · Refund: RP-STD-MED / RP-STD-ARB · Unquantified default ₹1,00,000.*

| Line | Fee |
|---|---|
| F1 Registration | Individual borrower ₹500 (waivable, CN-HARD) · NI Act s.138 complainant ₹1,000 · MSME/business borrower ₹2,500 per facility · lender filing outside programme ₹2,500 |
| F2 Administration (marginal, once per case; covers negotiation, conciliation, mediation) | ≤ ₹1,00,000: ₹1,000 (minimum) · ₹1,00,001–₹5,00,000: ₹1,000 + 1.0% over ₹1 lakh · ₹5,00,001–₹20,00,000: ₹5,000 + 0.6% over ₹5 lakh · ₹20,00,001–₹1,00,00,000: ₹14,000 + 0.35% over ₹20 lakh · > ₹1 crore: ₹42,000 + 0.15% over ₹1 crore; cap ₹5,00,000 |
| F3 Neutral session | Band I ₹3,000 (consumer/small) · Band II ₹6,000 · Band III ₹12,000 (MSME/large) |
| F4 Arbitrator (sole) | ≤ ₹1 lakh ₹4,800 · ₹1–5 lakh ₹8,000 · ₹5–10 lakh ₹12,000 · ₹10–20 lakh ₹16,000 · ₹20–50 lakh ₹30,000 · ₹50 lakh–1 crore ₹60,000 · > ₹1 crore: Fourth Schedule with `SOLE_25` and cap |
| F5 Arbitration administration | 15% of F4, minimum ₹2,500 (`PCT_OF_ITEM`) |
| F6 Oral hearing | + one F3 Band II session per hearing day beyond documents-only |
| F7 Success component | **Removed** (FL-5 0.25–0.75% of settled sum prohibited, P3) |

### Card FIN-L — Lender/NBFC bulk programme (enterprise contract)
*INR · GST exclusive · Payer: `lender_pays` (borrower ₹0; Equator-drafted settlement terms never add Equator fees to borrower dues) · Source: R1 §8.5 A reconciled with C2 FL-5 and P05 FR-P05-08 · Refund: RP-FIN-L · Invoiced monthly on usage (P05 FR-P05-38).*

| Stage (per case) | ≤ ₹50,000 | ₹50,001–₹1,00,000 | ₹1,00,001–₹5,00,000 | ₹5,00,001–₹20,00,000 | ₹20,00,001–₹50,00,000 |
|---|---|---|---|---|---|
| L1 Digital notice + assisted negotiation (WhatsApp/SMS/email/voice, pay-link on lender rail) | ₹129 | ₹149 | ₹249 | ₹399 | ₹599 |
| L2 Conciliation — settled (neutral component) | ₹999 (₹250) | ₹1,499 (₹400) | ₹3,499 (₹900) | ₹7,499 (₹1,800) | ₹12,499 (₹3,000) |
| L3 Conciliation — not settled (same neutral component) | ₹299 (₹250) | ₹499 (₹400) | ₹1,099 (₹900) | ₹2,199 (₹1,800) | ₹3,999 (₹3,000) |
| L4 Arbitration, documents-only, AI-assisted drafting, sole (arbitrator ≈ 70%) | ₹2,499 (₹1,750) | ₹3,999 (₹2,800) | ₹6,999 (₹4,900) | ₹11,999 (₹8,400) | ₹24,999 (₹17,500) |
| L5 Oral hearing add-on, per hearing (arbitrator 70%) | ₹2,000 | ₹2,500 | ₹4,000 | ₹6,000 | ₹9,000 |
| L6 Execution pack | ₹499 | ₹499 | ₹799 | ₹999 | ₹1,499 |
| L7 eStamp / eSign / physical notice | ANC rates | | | | |

Claims > ₹50 lakh use FIN-R F4–F5 under the programme contract. Volume tiers (annual committed cases, institutional components only): T1 5,000+ −10%; T2 25,000+ −20%; T3 1,00,000+ −30% + dedicated case desk. Programme plan (any EAPI plan) −25%. L2/L3 differ only in the institutional component (outcome-triggered flat fee, P3); the neutral component is identical. NN-03: no programme term may confer any appointment choice or veto; the Independence Evidence Pack is included at no charge.

### Card COM-STD — Commercial arbitration and mediation
*INR · GST exclusive (tribunal fees T09/T10) · Payer: registration `filer` on account; administration and tribunal deposits `equal_split` on account, reallocated by award (`deferred_cost_follows_event`, A&C s.31A; Rules art.23); counterclaims `counterclaim_increment` · Source: C3 1.5 (tariff prevails over estimator and model), R1 §8.2, R4 §4.1 (s.12A, IAMC), P08 golden vector · Refund: RP-STD-ARB / RP-STD-MED · Unquantified default ₹50,00,000.*

| Line (P08 alias) | Fee |
|---|---|
| C1 Registration — arbitration (`com.registration`) | ₹20,000 (estimator ₹25,000 retired) |
| C2 Registration — mediation | ₹10,000 |
| C3 Administration — arbitration (`com.admin_slab`, marginal) | ≤ ₹10 lakh ₹20,000 · ₹10 lakh–1 crore ₹20,000 + 1.0% over ₹10 lakh · ₹1–10 crore ₹1,10,000 + 0.35% over ₹1 crore · ₹10–50 crore ₹4,25,000 + 0.15% over ₹10 crore · > ₹50 crore ₹10,25,000 + 0.10% over ₹50 crore; cap ₹20,00,000 |
| C4 Arbitrator (`arb.fourth_schedule`, per arbitrator) | ≤ ₹5 lakh ₹45,000 · ₹5–20 lakh ₹45,000 + 3.5% over ₹5 lakh · ₹20 lakh–1 crore ₹97,500 + 3% over ₹20 lakh · ₹1–10 crore ₹3,37,500 + 1% over ₹1 crore · ₹10–20 crore ₹12,37,500 + 0.75% over ₹10 crore · > ₹20 crore ₹19,87,500 + 0.5% over ₹20 crore; ceiling ₹30,00,000; sole +25%; three-member × 3 |
| C5 Expedited / fast track (A&C s.29B) | Tribunal fee × 0.75 |
| C6 Emergency arbitrator | ₹3,00,000 fixed (EA ₹2,40,000 + administration ₹60,000); `applicant`; payable before EA appointment |
| C7 Appellate tier (opt-in, claims ≥ ₹1 crore) | 3 members × 40% of per-arbitrator C4 figure; appeal administration 25% of C3, minimum ₹50,000; `applicant` on account |
| C8 Administration — private pre-suit mediation | ≤ ₹10 lakh ₹15,000 · ₹10–50 lakh ₹30,000 · ₹50 lakh–1 crore ₹40,000 · ₹1–3 crore ₹50,000 · > ₹3 crore ₹75,000 (bands mirror PIMS Rules 2018 Schedule II; statutory s.12A pre-institution mediation is conducted only by the Legal Services Authority. Equator cannot conduct it until the Mediation Act Ninth Schedule (s.64) is notified, Equator is an MCI-recognised MSP (s.40), the Central Government authorises it under the substituted s.12A(2)(ii) and new rules are made (M-06); flag `com.s12a_equator_authorised` OFF) |
| C9 Mediator session (`com.mediation_session`) | Band III ₹12,000 (≤ ₹5 crore) · Band IV ₹20,000 (> ₹5 crore); half-day/day per §B.7.2 |
| C10 MSME delayed payment (pre-MSEFC) | Flat ₹1,999 negotiation + conciliation, `filer`; escalation pack to MSME ODR/MSEFC free (signposting, NN-20) |
| C11 Expert determination | Administration ₹25,000 + expert per §B.7.3 |
| C12 MSE concession | CN-MSE: 50% of C1/C2 + C3/C8 for the MSE party's share |

### Card COM-M — Settlement administration fee (opt-in, B2B only)
*INR · GST exclusive · Payer `equal_split` · Source: C1 H.2; P05 FR-P05-08.* 0.5% of the settled amount stated in the signed settlement, no minimum, cap ₹5,00,000; institutional only; available only if every party is a business entity and all signed the opt-in at filing; disclosed on every quote; never offered in repeat-player matters. INT-M equivalent: 0.25%, cap USD 20,000.

### Card FAM-STD — Family, marital and family property
*INR · GST exclusive · Payer `equal_split` (property matters `equal_per_party_group` by heir branch; `pro_rata_custom` by agreed shares) · Source: C3 3.5(b) Schedule of Fees adopted as canonical; 3.5(a) per-party-per-session and 3.5(c) 20% share/0.5% escrow retired; new property lines per C3 3.0 · Refund: RP-STD-MED (RP-STD-ARB for FAM-ARB).*

| Matter | Registration | Administration |
|---|---|---|
| Mutual-consent terms | ₹1,000 | ₹3,000 |
| Parenting plan | ₹1,000 | ₹5,000 |
| Maintenance | ₹1,000 | ₹5,000 |
| Matrimonial property / multi-issue (streedhan, shared household) | ₹2,000 | ₹8,000 |
| Court-referred | Nil | As directed |
| Elder maintenance (Senior Citizens Act 2007; tribunal signposted) | ₹0 for the senior citizen | ₹3,000, payable by respondent family members |
| **Partition, HUF partition, succession/inheritance among heirs, family settlement deed, family-business separation (new)** | ₹2,500 + ₹500 per party beyond 4 | Marginal on declared gross value: ≤ ₹50 lakh ₹10,000 · ₹50 lakh–2 crore ₹10,000 + 0.10% over ₹50 lakh · ₹2–10 crore ₹25,000 + 0.05% over ₹2 crore · > ₹10 crore ₹65,000 + 0.02% over ₹10 crore; cap ₹2,00,000 |

Mediator: Band I ₹3,000 / Band II ₹6,000 / Band III ₹12,000 per session (half-day 2.5×); co-mediation 1.6×; child-inclusive ₹8,000 per child; shuttle +25%; non-standard MSA drafting ₹3,000; adjournment ₹1,000; escrow per ANC; registration route per ANC.REGN.FACIL. **FAM-ARB** (partition/property rights only, NN-06): COM-STD C3–C5 with registration ₹10,000; never for status, custody, guardianship, testamentary or criminal matters (`MECHANISM_NOT_PERMITTED`). Probate and will validity: signposted (free). DV safety pathway free (P5).

### Card INS-RET — Insurance retail (policyholders, nominees)
*INR · GST exclusive · Payer: registration `filer` (₹0 if insurer-referred under protocol — `insurer_pays`); mediation `equal_split` unless insurer protocol/subscription → `insurer_pays` · Source: C2 IN-5 (effective 1 Aug 2026 draft) · Refund: RP-INS-RET · No success fee (r.27).*

| Line | Fee (neutral component) |
|---|---|
| I1 Registration & triage | ₹1,500 |
| I2 Claim-file retrieval & schedule build | ₹2,500 |
| I3 Mediation, all sessions up to three: ≤ ₹1 lakh | ₹2,500 (₹2,000) |
| ₹1,00,001–₹5,00,000 | ₹6,000 (₹4,500) |
| ₹5,00,001–₹20,00,000 | ₹15,000 (₹11,000) |
| ₹20,00,001–₹50,00,000 | ₹30,000 (₹22,000) |
| > ₹50,00,000 (new band; consumer-commission territory, still mediable) | ₹45,000 (₹33,000) |
| I4 Additional session beyond three | ₹3,500 (₹3,000) |
| I5 Settlement drafting & registration | ₹3,500 |
| I6 Escrow handling | ANC.ESCROW, cap ₹2,500 |
| I7 Drafting Ombudsman complaint (F-I07) | ₹2,000 |
| I8 Interpretation; signposting report F-I19 | ₹0 (P5) |

### Card INS-COM — Insurance commercial (B2B, quantum-only arbitration)
*INR · GST exclusive · Payer `equal_split` (insurer–insurer, insurer–reinsurer, corporate insured) · Source: C2 IN-5 · Refund: RP-INS-COM.*

| Amount in dispute | Mediation admin | Mediator (all sessions) | Arbitration admin | Tribunal (sole) |
|---|---|---|---|---|
| ≤ ₹10,00,000 | ₹15,000 | ₹40,000 | ₹40,000 | ₹1,25,000 |
| ₹10,00,001–₹50,00,000 | ₹30,000 | ₹90,000 | ₹90,000 | ₹3,00,000 |
| ₹50,00,001–₹2,00,00,000 | ₹60,000 | ₹2,00,000 | ₹1,75,000 | ₹6,50,000 |
| ₹2,00,00,001–₹10,00,00,000 | ₹1,25,000 | ₹4,50,000 | ₹3,50,000 | ₹15,00,000 |
| ₹10,00,00,001–₹50,00,00,000 | ₹2,50,000 | ₹9,00,000 | ₹7,00,000 | ₹30,00,000 |
| > ₹50,00,00,000 | ₹4,00,000 | ₹15,00,000 | ₹12,00,000 | ₹50,00,000 |

Three-member tribunal = 2.5 × sole. Arbitration only under a separate B2B agreement, never against a retail policyholder (DB CHECK `no_arbitration_on_retail`). Expert determination (surveyor/assessor): §B.7.3.

### Card INS-SUB — Insurer subscriptions and batched settlement days
*INR · GST exclusive · Payer `insurer_pays` · Source: C2 IN-5 (tariff per-case figures prevail over the ₹7,500 model figure, C2 gap 21) · Refund: RP-SUB.*

| Plan | Annual fee | Included | Per case beyond |
|---|---|---|---|
| INS-SUB-ENTRY (≤ 2,000 grievances/yr) | ₹6,00,000 | Protocol, SPOC, 40 matters, quarterly pack | ₹4,000 |
| INS-SUB-STD (2,001–10,000) | ₹18,00,000 | 150 matters, 2 batched days, named account manager | ₹3,500 |
| INS-SUB-ENT (10,001–30,000) | ₹45,00,000 | 450 matters, 6 batched days, monthly reporting, API | ₹3,000 |
| INS-SUB-GROUP (> 30,000) | ₹90,00,000 | 1,000 matters, 12 batched days, dedicated team, data feed | ₹2,500 |

Batched settlement day: neutral ₹60,000/day (≤ 30 files) + administration ₹35,000/day + ₹1,500 per file settled + registration ₹900 per file; settlement-grid preparation ₹75,000 one-off per programme; policyholder ₹0.

### Card WRK-STD — Workplace and HR
*INR · GST exclusive · Payer: registration `filer`; administration and neutral `employer_employee_split` 75:25 in individual matters (employer 100% in employer-panel bulk) · Source: C3 2.5 · Refund: RP-STD-MED (arbitration only for non-workman contracts: RP-STD-ARB with COM-STD C3–C5).*

| Matter | Registration | Administration |
|---|---|---|
| Wages / full-and-final (individual) | ₹500 | ₹2,500 |
| Separation / termination | ₹1,000 | ₹5,000 |
| Notice / bond / restraint (non-compete) | ₹1,000 | ₹5,000 |
| Benefits (gratuity, PF-linked) | ₹500 | ₹2,500 |
| Grievance after GRC (IR Code 2020) | ₹500 | ₹2,000 |
| Co-founder exit (business parties) | COM-STD | COM-STD |

Neutral: Band I ₹3,000 / II ₹6,000 / III ₹12,000 per session; half-day 2.5×; shuttle +25%; escrow per ANC (75:25); adjournment ₹1,000; CN-EMPLOYEE 50–100%; DLSA referral nil institutional fee. Statutory dues are never discounted inside settlements (P09 `STATUTORY_DUES_WAIVER_BLOCKED`).

### Card WRK-POSH — POSH / Internal Committee SaaS and services
*INR · GST exclusive · Payer `employer_pays`; complainant never charged (P5, NN-07) · Source: C3 2.5; R4 §4.3; P09 FR-P09-36 · Refund: RP-SUB.*

| Plan / service | Price | Included |
|---|---|---|
| POSH-SME (≤ 50 employees) | ₹15,000/yr | 1 IC workspace, sealed inquiry module, 90-day clocks, annual-report generator |
| POSH-GROWTH (51–500) | ₹36,000/yr | + 3 locations, training tracker |
| POSH-ENT (501–5,000) | ₹90,000/yr | + unlimited ICs, HRMS sync, SSO |
| POSH-LARGE (> 5,000) | ₹30/employee/yr, minimum ₹1,50,000 | + BYOK option |
| E-learning add-on | ₹40/employee/yr | Awareness modules, completion certificates |
| External IC member | ₹60,000/yr retainer; ₹15,000 per inquiry | Via marketplace (§B.7.7: 15%) |
| IC training (half-day, ≤ 15) / awareness session / annual-report support / compliance audit | ₹35,000 / ₹15,000 / ₹20,000 / ₹50,000 | — |

Dunning never blocks an open inquiry within its 90-day clock (P05 FR-P05-37).

### Card INT-USD — International commercial arbitration
*USD authoritative; invoiced in USD/EUR/GBP/SGD/AED (§B.6), INR equivalent shown · GST: export under LUT (T05) for foreign recipients; T01–T04 for Indian parties · Payer: registration `filer`; deposits `equal_split` with substitute payment (ICC Art. 37 / SIAC practice) · Source: R5 §6.1 proposed schedule; P08 INT vector · Refund: RP-STD-ARB.*

| Sum in dispute (USD) | I1 Registration | I2 Administration | I3 Sole arbitrator (scale maximum) | Track |
|---|---|---|---|---|
| ≤ 250,000 | 750 | 2,500 fixed | 7,500 fixed | Streamlined, documents-only (opt-in or default by Rules) |
| 250,001–1,000,000 | 1,500 | 6,000 → 10,000 interpolated | 15,000 → 35,000 interpolated | Expedited eligible |
| 1,000,001–5,000,000 | 2,000 | 10,000 → 20,000 | 35,000 → 80,000 | Standard |
| 5,000,001–25,000,000 | 2,500 | 20,000 → 35,000 | 80,000 → 150,000 | Standard |
| > 25,000,000 | 3,000 | 35,000 + 0.05% over 25m, cap 50,000 | 150,000 + 0.25% over 25m, cap 250,000; or hourly USD 400–600 by agreement | Standard |

Rules: standard-track claims ≤ USD 250,000 use the 250,001 band floor (admin 6,000; arbitrator 15,000). Registrar fixes the arbitrator's fee at or below the scale maximum (deposit at maximum). Three-member = 2.5 × sole. Expedited −20% on tribunal fees. Emergency arbitrator: administration USD 3,000 + EA fee USD 12,500 (Registrar may fix 10,000–15,000). Appointing authority only (UNCITRAL/ad hoc): USD 2,000 per appointment. Consent-award conversion (arb-med-arb; NN-19): USD 1,500 administration + USD 2,500 tribunal (sole). I9 INR-track surcharge (India-seated ICA billed on COM-STD in INR): ₹50,000 flat for international gates (sanctions, KYC/UBO, DPDP s.16, FEMA). Interpretation, certified translation, apostille/legalisation and couriers at actuals + 10%.

Benchmark (approximate, R5 §6.1; verify before publication): at USD 1m — ICC admin ≈ 23.3k, arbitrator 14.6k–64.1k; SIAC (SGD) admin 15,000, arbitrator max 60,000; Equator admin 10,000, arbitrator max 35,000. At USD 5m — ICC admin ≈ 45.0k, arbitrator up to ≈ 141.9k; SIAC (SGD) 36,000 / 130,000; Equator 20,000 / 80,000. LCIA is time-based (GBP 250–650/h, registration GBP 1,950); HKIAC registration HKD 10,000 from 1 Jan 2026; MCIA (INR) filing ₹50,000 with no USD schedule. Positioning: below SIAC/ICC, at or above MCIA/IAMC (R5 D5).

### Card INT-MED — International mediation
*USD · GST as INT-USD · Payer `equal_split` · Source: R5 §6.2 (ICC Mediation filing USD 3,000 benchmark) · Refund: RP-STD-MED.*
Filing USD 500; administration USD 1,500 (≤ 1m) / 3,000 (1m–10m) / 5,000 (> 10m); online-only administration × 0.75; mediator per session-day USD 2,000 (≤ 1m) / 4,000 (1m–10m) / 6,000 (> 10m); INT-M opt-in per COM-M; consent-award conversion per INT-USD.

### Card SEC-SMART — Securities (SEBI SMART ODR), feature flag OFF by default
*INR · **plus GST** · `REGULATED_TABLE`, verbatim, non-discountable (NN-18) · Payer: conciliation `enterprise_pays` (borne by the MII and recovered from the market participant; never passed to the investor); arbitration `both_parties` (initiator and respondent each deposit their fee within 7 days of the choice to arbitrate; the initiator may pay the respondent's share and recover it — Master Circular para 28(c); an MP respondent also deposits 100% of the admissible claim with the MII within 10 days, outside Equator's merchant per NN-13); both-sides payment is current law (para 28(c)); the 23 Jul 2026 draft moves payment to each party's MII · Source: R1 §8.1 (help.smartodr.in; SEBI ODR Master Circular); P09 FR-P09-43 · Refund: RP-REG.*

| Stage / claim | Neutral | ODR institution | Total |
|---|---|---|---|
| Pre-conciliation | ₹0 | ₹0 | ₹0 |
| Conciliation — settled | ₹4,800 | ₹600 | ₹5,400 |
| Conciliation — not settled | ₹3,240 (SEBI Master Circular SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2023/195, para 8, as updated 28 Dec 2023; the SMART ODR help page shows ₹3,200, so the circular is used) | ₹600 | ₹3,840 |
| Arbitration ≤ ₹1 lakh | ₹4,800 | ₹600 | ₹5,400 |
| > ₹1–10 lakh | ₹8,000 | ₹1,000 | ₹9,000 |
| > ₹10–20 lakh | ₹12,000 | ₹1,500 | ₹13,500 |
| > ₹20–30 lakh | ₹16,000 | ₹2,000 | ₹18,000 |
| > ₹30–50 lakh | ₹60,000 | ₹7,500 | ₹67,500 |
| > ₹50 lakh–1 crore | ₹1,20,000 | ₹15,000 | ₹1,35,000 |
| > ₹1 crore | max(₹1,20,000, 1% of claim) | ₹35,000 | ≥ ₹1,55,000 |
| Late fee — conciliation filed > 6 months after dispute | — | — | ₹1,000 |
| Late fee — arbitration | Fee × 2 (non-refundable) if initiated more than 1 month and up to 6 months after failed conciliation; market participant initiating after 6 months: +50% of the table fee per additional month | | |

Three-member tribunal (> ₹30 lakh): neutral fee split 40:30:30, the larger share to the arbitrator who writes the award (Master Circular para 8; same in the 23 Jul 2026 draft). Award within 30 days of appointment, extendable by 30 days. The unpublished draft ruleset for SEBI's 23 Jul 2026 consultation is for impact testing only; no revenue line depends on this card (master §1.2).

### Card GRM — Grievance Redressal Mechanism SaaS (L4)
*INR · GST exclusive · Payer `enterprise_pays`; complainants ₹0 · Source: R4 §4.3 (₹25,000–₹1,00,000/month + ₹20–₹100/ticket), R1 §8.5 D (₹15,000–₹75,000/month), Equator default · Refund: RP-SUB · Annual prepay = 10 × monthly.*

| Plan | Monthly | Included tickets/month | Overage per ticket | Key entitlements |
|---|---|---|---|---|
| GRM-LENDER-S | ₹25,000 | 500 | ₹40 | `FIN_RBI` profile (RB-IOS 2026 clocks, IO routing), RE + LSP nodal desks, MIS |
| GRM-LENDER-M | ₹50,000 | 2,500 | ₹30 | + Internal Ombudsman workspace, API, multi-brand |
| GRM-LENDER-L | ₹1,00,000 | 10,000 | ₹20 | + dedicated CSM, BYOK option |
| GRM-LISTED-S | ₹15,000 | 100 | ₹50 | SEBI LODR/SCORES-mapped clocks, RTA hand-off, quarterly investor-grievance statement |
| GRM-LISTED-M | ₹35,000 | 1,000 | ₹40 | + multi-entity, API |
| GRM-EMPLOYER-S (≤ 250 employees) | ₹10,000 | 200 | ₹40 | IR Code GRC workflow, HR-policy desks |
| GRM-EMPLOYER-M (251–2,000) | ₹25,000 | 1,000 | ₹30 | + HRMS sync |
| GRM-EMPLOYER-L (> 2,000) | ₹15/employee, min ₹40,000 | 3,000 | ₹20 | + SSO, multi-site |
| GRM-UNIV-S (≤ 5,000 students) | ₹10,000 (annual prepay ₹1,00,000) | 300 | ₹30 | UGC 2023 SGRC + Ombudsperson workflows, campus-cell hand-off |
| GRM-UNIV-M (5,001–20,000) | ₹20,000 | 1,000 | ₹25 | + multi-campus |
| GRM-UNIV-L (> 20,000) | ₹30,000 | 3,000 | ₹20 | + API, SSO |

Escalation to ODR is billed per the vertical card (FIN-L for lenders; INS-RET/INS-SUB for insurers; WRK-STD for employers); complainant ₹0 for FIN/INS consumers (P09 FR-P09-31). Dunning never blocks ticket intake or regulator clocks (NN-04).

### Card EAPI — Enterprise API, subscriptions and volume tiers (L3)
*INR (USD for foreign contracts) · GST exclusive · Payer `enterprise_pays` · Source: R1 §8.5 A (₹25,000–₹1,00,000/month platform option, −25% per-case), C4 A.6 (API ₹50,000–₹2,00,000/month), C4 B.13 (clause insertion ₹1.5–5 lakh/yr) · Refund: RP-SUB.*

| Plan | Monthly | API calls/month | Overage per 1,000 calls | Entitlements |
|---|---|---|---|---|
| EAPI-SANDBOX | ₹0 | sandbox only | — | Test tenant, synthetic data |
| EAPI-STARTER | ₹25,000 | 2,50,000 | ₹50 | Case APIs, webhooks, 1 concurrent bulk job, Programme plan −25% |
| EAPI-GROWTH | ₹60,000 | 10,00,000 | ₹40 | + clause API, white-label portal, MIS packs, 2 bulk jobs |
| EAPI-SCALE | ₹1,00,000 | 50,00,000 | ₹30 | + mTLS tokens, SFTP, dedicated case desk at T3, 99.9% SLA credits |

Add-ons: Clause Registry ₹1,50,000/yr (≤ 10,000 instruments) / ₹3,00,000 (≤ 1,00,000) / ₹5,00,000 (unlimited); BYOK ₹2,00,000/yr; dedicated SFTP ₹10,000/month. Volume tiers (annual committed cases): T1 5,000+ −10%; T2 25,000+ −20%; T3 1,00,000+ −30%; quarterly true-up prospective; minimum-commitment shortfall fee OFF by default. Prepaid wallet optional (P05 FR-P05-39).

### Card CH — Private ADR Chambers (L2) — identical to P10 FR-P10-03
*INR · GST exclusive · Payer: tenant (`chambers_admin`) · Source: R4 §4.4 (₹1,499–₹4,999/seat/month), C1 H.3 (ARPU ₹60,000), C4 D.2 (₹800–₹1,000/case) · Refund: RP-SUB.*

| Plan | Price | Included | Per case beyond |
|---|---|---|---|
| CH-SOLO | ₹1,499/seat/month or ₹14,990/seat/yr; 1–2 seats | 5 new cases/month | ₹999 |
| CH-PRO | ₹2,999/seat/month or ₹29,990/seat/yr; min 3 seats | 25 | ₹899 |
| CH-INST | ₹4,999/seat/month or ₹49,990/seat/yr; min 10 seats | 100 | ₹799 |
| CH-IAAS | ₹3,00,000–₹8,00,000/yr platform fee + contracted revenue share | Contracted | Contracted |

Add-ons: secretariat ₹2,500/case or ₹45,000/month per FTE-equivalent; video beyond 1,000 participant-minutes/seat/month ₹1.50/participant-minute; premium AI drafting ₹999/seat/month; messaging at actuals + 10%; eStamp ₹49/document + duty; eSign actuals + ₹20/signature; storage ₹500/100 GB/month. Trial 14 days. Referral fee to the administering institution 10% of its administration fee for 12 months; no referral reward of any kind (cash, credit, discount or priority) to advocates, bar bodies, CAs, CSs or CMAs (NN-34; master X-62; supersedes the v2.1 "non-cash credits only" wording — AFC-B-03). Tenant own fee schedules must pass the P1–P9 validators; tenant share flows via Route (`revenue_owner = tenant`).

### Card ACAD — Equator ADR Academy (L6; issuing entity Equator ADR Institute **[VERIFY — open: the training site's operator is shown as Infrabyx Consultancy (OPC) Private Limited (Equa Trainings / Equa.Law) and its displayed prices are in USD and do not match this card; confirm the entity and reconcile before any referral — Board; Appendix AF AFC-B-04; D3-38]**)
*INR · **exclusive of applicable taxes** (quotes carry this wording only, P10 OI-06) · Payer: learner, institution or sponsor per programme · Source: C5 A.5–A.7 (04.1 rate card; effective date blank) · Floors stored, never displayed · Refund: RP-ACAD.*

| Code | List | Partner | Code | List | Partner |
|---|---|---|---|---|---|
| T-40-S | ₹12,500 | ₹9,500 | T-40-P | ₹38,000 | — |
| T-20-S | ₹7,500 | ₹5,500 | T-20-P | ₹22,000 | — |
| C-CERT | ₹14,000 | ₹11,000 | T-TTT | ₹45,000 | — |
| W-HALF-S | ₹1,500 | ₹1,200 | T-ASSESS | ₹12,000 | — |
| W-FULL-S | ₹2,800 | ₹2,200 | SCH-RES | ₹26,000 | ₹22,000 |
| W-SERIES | ₹3,800 | ₹3,000 | SCH-DAY | ₹16,000 | ₹13,500 |

Institution-paid (per programme): T-FDP ₹3,50,000; T-FDP-3 ₹2,25,000; W-FULL-I ₹65,000; W-HALF-I ₹38,000; A-POSH ₹85,000; A-SGRC ₹95,000; A-CELL ₹1,45,000; CUSTOM ₹28,000/day. Advisory/licensing/coaching: ADV-A ₹3,60,000 p.a.; ADV-B ₹1,80,000; ADV-IC ₹18,000/sitting; ADV-OMB ₹22,000/matter; COACH-INTL ₹2,25,000/team/season; COACH-NAT ₹1,10,000; LIC-CURR ₹1,25,000 p.a.; LIC-CASE ₹65,000 p.a. Competitions: team national ₹7,500; regional ₹4,500; late +₹2,000; observer ₹2,500; sponsorship title ₹12,00,000 / associate ₹6,00,000 / round ₹2,50,000 / award ₹1,00,000 / hospitality ₹75,000.

**Institutional Membership:** ₹1,75,000 p.a.; 3-year ₹1,60,000/yr paid annually in advance; additional campus ₹1,20,000; no commencement before payment; no auto-renewal; 12 quantity-limited inclusions per P10 FR-P10-28; 10% catalogue discount (non-stacking, exclusions apply). **Revenue share (Institute operator : partner institution):** T-40-S/T-20-S 70:30; C-CERT 65:35; workshops 75:25; residential 60:40; hosted competition surplus 60:40; advisory/licensing/coaching 100:0; computed on Net Collections (gross cleared receipts − refunds − gateway charges actually incurred); Equator Resolution Service Private Limited books ₹0 from courses unless stream RS-22 is approved (D3-38; AFC-B-06). **Discount authority:** list/partner — BD; ≤ 10% — PD; 10.01–25% — PD + FC with commitment; > 25%, below floor or free — Programme Board. **Neutral pipeline:** empanelment listing ₹0 (C4 B.13 empanelment fee retired); every applicant pays the same EQAP sitting fee, whatever the training provider (master X-29; CN-04; RS-21; AFC-B-05).

## B.12 Change control and Board approval

Board pack per card (figures, benchmarks, margin, harness results, legal/tax sign-off) → `board_approval_ref` recorded for that version only. Every change is a new version (maker `institution_admin` → checker `fin.controller`; regulated cards `platform_admin` → legal reviewer, verbatim). Annual review each April and on any regulator or GST change. P13 renders the published version with its approval state; marketing use of a figure needs a Claims Register entry (NN-17).

## B.13 Open items and verification flags

1. **Appendix F §F.4.8 conflicts** with P05/this appendix: `fee_schedules.status` enum (`pending_approval/active` vs `in_review/published`), FX staleness (24 h vs 3 business days), `fx_rates.rate numeric` vs `rate_e8 bigint`, `core.plans.product_line` (L2–L6 vs named lines). This appendix and P05 prevail; F should be aligned (ADR).
2. **P03 FR-P03-11** small-ticket conciliation ₹1,500–₹4,800 per case conflicts with FIN-L bulk docket neutral components (₹250–₹3,000) fixed by the P05 golden test; recommend P03 note the bulk-docket exception.
3. **P08 COM golden vector** shows GST ₹1,13,737.50 as one figure; correct invoice treatment splits it into ₹26,550.00 forward + ₹87,187.50 RCM (WE-04). Totals agree.
4. Resolved: *Afcons* (30 Aug 2022): sole-arbitrator 25% is over and above the ₹30 lakh ceiling; apply the cap first, then SOLE_25.
5. Resolved per Master Circular /195 (28 Dec 2023): unsuccessful conciliation ₹3,240 + ₹600; arbitration fees payable at initiation by both the initiator and the respondent within 7 days; the initiator may pay the respondent's share and recover it in the arbitration (Master Circular para 28(c)); late fees as in Card SEC-SMART (+50%/month for market participants only); three-member split 40:30:30 (40 to the award-writer); successful party's deposit refunded subject to the award. **[VERIFY — open (watch): payer rule corrected 22 Oct 2026 against Master Circular para 28(c); no final circular on the 23 Jul 2026 consultation as of 15 Oct 2026]**
6. RESOLVED (Oct 2026): SAC 998215 for ADR; arbitral-tribunal exemption = Notif. 12/2017 Sl. 45 with the s.22 registration threshold (Notif. 21/2019); RCM Sl. 3; s.170 rounding and s.51 GST-TDS confirmed; IFSC zero-rating via IGST s.16(1)(b). **[VERIFY — open, tax memo: GST on `equator_principal` resupply (forward 18% assumed); wallet deposit vs advance (s.2(31) proviso); e-commerce-operator TDS/GST-TCS exposure]**
7. RESOLVED (Oct 2026): s.194J → s.393(1) Sl. 6(iii) (10%/2%, ₹50,000); s.194H → s.393(1) Sl. 1(ii) (2%, ₹20,000); s.195 → s.393(2) Sl. 17; Forms 145/146 (r.220; ₹5 lakh aggregate per tax year); Form 10F → Form 41; DTAA: individual arbitrators under Art. 14 IPS (fixed base / 90 days for Singapore). Per-treaty table to be signed off by CA.
8. FBIL covers USD/GBP/EUR/JPY only; SGD/AED need fallback sources (resolved Oct 2026). **[VERIFY — open: statutory auditor's acceptance of the AED peg derivation (USDINR ÷ 3.6725) vs AD-bank TT]**
9. Reconciliation choices needing Board ratification: FIN success component removed; COM registration ₹20,000 (not ₹25,000) and admin cap ₹20 lakh (not ₹10 lakh); FAM schedule (b) adopted, escrow 0.25%; senior-citizen concession at 60+ (IN-5 had 65+); INS retail > ₹50 lakh band added; escrow fee unified; neutral session = 2 hours (C3 used 90 minutes).
10. Resolved (M-06): Equator may run private pre-suit mediation and Part III conciliation now (C8 fees). Statutory s.12A PIMS stays with the SLSA/DLSA (CCA s.12A(2); PIMS Rules 2018, G.S.R. 606(E)). Equator prepares the Form-1 pack only. Equator-conducted s.12A mediation needs (i) notification of Mediation Act s.64 and the Ninth Schedule, (ii) MCI recognition under s.40, (iii) a Central Government authorisation under the new s.12A(2)(ii), and (iv) new rules; flag `com.s12a_equator_authorised` stays OFF.
11. Resolved in part: fees not in the KFS cannot be charged without the borrower's explicit consent (RBI KFS instructions, 15 Apr 2024, now in RBC Directions 2025); LSP fees are paid by the NBFC, not borrowers (NBFC Credit Facilities Directions 2025, para 10(4)). Default rule stands: Equator documents never add its fees to borrower dues. Costs allocated by a tribunal under A&C s.31A are separate. **[VERIFY — open (counsel): A&C s.31A(5) voids a pre-dispute agreement that a party pays costs 'in any event'; tribunal discretion under s.31A(1)–(3) stays; CPA 2019 s.2(46) unfair-term risk; Equator templates carry no pre-dispute cost-shifting clause]**
12. Resolved: master §1.5 now includes `finance_controller`, mapped to the `fin.controller` bundle; other fee approvals use the `fin.*` bundles (P05 §3).
