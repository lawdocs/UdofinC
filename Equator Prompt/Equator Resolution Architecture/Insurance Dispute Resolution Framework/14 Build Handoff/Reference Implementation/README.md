# Insurance vertical — Reference Implementation

A runnable proof that the three institutional rules of the Insurance vertical **cannot be
bypassed** — not by the service layer, and not by a direct SQL write that tries to go around it.
This is the Insurance counterpart to the platform Reference Implementation (which proves the
Family/Workplace rules in 34 tests).

## Run

```
cd in_ref
python -m unittest -v
```

No dependencies — Python 3.8+ standard library only. **33 tests, all passing.**

## What it proves

| Rule | Meaning | How it is proven |
|------|---------|------------------|
| **R1** | No arbitration route on a retail (or group-member) policy — IRDAI circular, 27 Oct 2023 | Rejected in the service layer (409) **and** by a database `CHECK` when a direct SQL write attempts it. A legacy arbitration clause in a retail policy does not force arbitration. Commercial arbitration is allowed. |
| **R2** | No settlement may waive a non-waivable statutory right or discharge future claims | Rejected in the service (422) **and** by a database `CHECK` on a direct write. |
| **R3** | No case closes without a delivered signposting event and an owner on every clock; and no case leaves triage without signposting | Enforced in the domain guard; closure and triage-exit both refuse. |

It also exercises the **clock engine** (Ombudsman one-year expiry computed from the reply date,
or representation + 30 days), the **Ombudsman eligibility engine** (all five conditions), the
**deduction** integrity checks, the **discharge-voucher** under-protest rule, **health-data
segregation** (a physically separate database with no join path, access-logged reads requiring the
`health` scope), and a **hash-chained audit log** with tamper detection.

## Files

- `store.py` — two physically separate SQLite databases (ordinary + health) with the CHECK
  constraints that carry R1 and R2.
- `domain.py` — the service layer: `RuleViolation`, the clock engine, the eligibility engine,
  and the R3 closure guard.
- `test_rules.py` — the proof.

The SQLite schema here mirrors the production PostgreSQL DDL in `14 Build Handoff/schema_in.sql`.
