"""
Equator Resolution — Insurance vertical reference implementation: the proof.

Run:  python -m unittest -v   (from this directory)

These tests prove that the three institutional rules cannot be bypassed — not by the
service layer, and not by a direct SQL write that tries to go around it. This is the
Insurance counterpart to the platform Reference Implementation's 34-test suite.
"""
import unittest, datetime
from store import Store
from domain import Equator, RuleViolation


def iso(days_ago):
    return (datetime.date.today() - datetime.timedelta(days=days_ago)).isoformat()


class Base(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.e = Equator(self.store)
        self.ins = self.e.add_insurer("Meridian General")

    def retail_case(self, **kw):
        p = self.e.add_policy(self.ins, "P-1", "health_individual", "retail")
        return self.e.create_case("INS-1", p, **kw)

    def commercial_case(self, **kw):
        p = self.e.add_policy(self.ins, "P-2", "fire", "commercial")
        return self.e.create_case("INS-2", p, **kw)

    def tearDown(self):
        self.store.close()


# ─────────────────────────── R1 — the retail arbitration bar ───────────────────────────
class TestR1RetailArbitrationBar(Base):
    def test_retail_arbitration_rejected_in_service(self):
        cid = self.retail_case()
        self.e.deliver_signposting(cid)
        with self.assertRaises(RuleViolation) as cm:
            self.e.triage(cid, "arbitration", "menon", "iyer")
        self.assertEqual(cm.exception.rule, "R1")
        self.assertEqual(cm.exception.status, 409)

    def test_retail_arbitration_rejected_by_database(self):
        """Bypass the service and write arbitration directly — the DB CHECK must refuse."""
        import sqlite3
        cid = self.retail_case()
        with self.assertRaises(sqlite3.IntegrityError):
            self.e.force_arbitration_via_sql(cid)

    def test_group_member_treated_as_retail(self):
        p = self.e.add_policy(self.ins, "P-G", "health_group", "group_member")
        cid = self.e.create_case("INS-G", p)
        self.e.deliver_signposting(cid)
        with self.assertRaises(RuleViolation) as cm:
            self.e.triage(cid, "arbitration", "menon", "iyer")
        self.assertEqual(cm.exception.rule, "R1")

    def test_commercial_arbitration_allowed(self):
        cid = self.commercial_case()
        self.e.deliver_signposting(cid)
        self.e.triage(cid, "arbitration", "menon", "iyer")   # must not raise
        row = self.store.ordinary.execute("SELECT route FROM dispute_case WHERE id=?", (cid,)).fetchone()
        self.assertEqual(row["route"], "arbitration")

    def test_legacy_clause_does_not_force_arbitration(self):
        p = self.e.add_policy(self.ins, "P-L", "motor_od", "retail", legacy_arb=True)
        cid = self.e.create_case("INS-L", p)
        self.e.deliver_signposting(cid)
        with self.assertRaises(RuleViolation):
            self.e.triage(cid, "arbitration", "menon", "iyer")

    def test_reviewer_must_differ(self):
        cid = self.retail_case()
        self.e.deliver_signposting(cid)
        with self.assertRaises(RuleViolation) as cm:
            self.e.triage(cid, "equator_mediation", "menon", "menon")
        self.assertEqual(cm.exception.code, "reviewer_must_differ")

    def test_fraud_not_mediated(self):
        p = self.e.add_policy(self.ins, "P-F", "motor_od", "retail")
        cid = self.e.create_case("INS-F", p, fraud_alleged=True)
        self.e.deliver_signposting(cid)
        with self.assertRaises(RuleViolation):
            self.e.triage(cid, "equator_mediation", "menon", "iyer")


# ─────────────────────────── R2 — no waiver of a non-waivable right ───────────────────────────
class TestR2NoWaiver(Base):
    def test_waiver_rejected_in_service(self):
        cid = self.retail_case()
        with self.assertRaises(RuleViolation) as cm:
            self.e.record_settlement(cid, 100000, statutory_rights_waived=True)
        self.assertEqual(cm.exception.rule, "R2")
        self.assertEqual(cm.exception.status, 422)

    def test_future_discharge_rejected(self):
        cid = self.retail_case()
        with self.assertRaises(RuleViolation) as cm:
            self.e.record_settlement(cid, 100000, future_claims_discharged=True)
        self.assertEqual(cm.exception.code, "no_future_discharge")

    def test_waiver_rejected_by_database(self):
        import sqlite3
        cid = self.retail_case()
        with self.assertRaises(sqlite3.IntegrityError):
            self.e.force_waiver_via_sql(cid, 100000)

    def test_valid_settlement_allowed(self):
        cid = self.retail_case()
        self.e.record_settlement(cid, 390000, continuity=True)
        row = self.store.ordinary.execute("SELECT amount, continuity_preserved FROM settlement WHERE case_id=?",
                                          (cid,)).fetchone()
        self.assertEqual(row["amount"], 390000)
        self.assertEqual(row["continuity_preserved"], 1)


# ─────────────────────────── R3 — no closure without signposting & owned clocks ───────────────────────────
class TestR3Closure(Base):
    def _prepped(self):
        cid = self.retail_case(representation_date=iso(40), insurer_reply_date=iso(20), reply_outcome="rejected")
        return cid

    def test_no_closure_without_signposting(self):
        cid = self._prepped()
        for k in ("insurer_reply_30d", "ombudsman_1y"):
            self.e.set_clock_owner(cid, k, "menon")
        with self.assertRaises(RuleViolation) as cm:
            self.e.close_case(cid)
        self.assertEqual(cm.exception.code, "no_signposting")

    def test_no_closure_with_unowned_clock(self):
        cid = self._prepped()
        self.e.deliver_signposting(cid)
        # owners deliberately not set
        with self.assertRaises(RuleViolation) as cm:
            self.e.close_case(cid)
        self.assertEqual(cm.exception.code, "unowned_clock")

    def test_closure_succeeds_when_complete(self):
        cid = self._prepped()
        self.e.deliver_signposting(cid)
        for c in self.e.clock_table(cid):
            self.e.set_clock_owner(cid, c["kind"], "menon")
        self.e.close_case(cid)
        row = self.store.ordinary.execute("SELECT status FROM dispute_case WHERE id=?", (cid,)).fetchone()
        self.assertEqual(row["status"], "closed")

    def test_cannot_leave_triage_without_signposting(self):
        cid = self._prepped()
        with self.assertRaises(RuleViolation) as cm:
            self.e.triage(cid, "equator_mediation", "menon", "iyer")
        self.assertEqual(cm.exception.rule, "R3")


# ─────────────────────────── the clock engine ───────────────────────────
class TestClockEngine(Base):
    def test_ombudsman_clock_from_reply(self):
        cid = self.retail_case(representation_date="2026-03-20", insurer_reply_date="2026-04-02",
                               reply_outcome="rejected")
        table = {c["kind"]: c for c in self.e.clock_table(cid)}
        self.assertEqual(table["ombudsman_1y"]["expiry"], "2027-04-02")

    def test_ombudsman_clock_from_rep_plus_30_when_no_reply(self):
        cid = self.retail_case(representation_date="2026-03-20")
        table = {c["kind"]: c for c in self.e.clock_table(cid)}
        # 2026-03-20 + 30 = 2026-04-19; + 365 = 2027-04-19
        self.assertEqual(table["ombudsman_1y"]["expiry"], "2027-04-19")

    def test_prompt_recorded(self):
        cid = self.retail_case(representation_date=iso(320))
        self.e.record_prompt(cid, "ombudsman_1y")
        row = self.store.ordinary.execute(
            "SELECT prompted_at FROM clock WHERE case_id=? AND kind='ombudsman_1y'", (cid,)).fetchone()
        self.assertIsNotNone(row["prompted_at"])


# ─────────────────────────── Ombudsman eligibility engine ───────────────────────────
class TestEligibility(Base):
    def test_eligible_when_all_five_met(self):
        cid = self.retail_case(amount=480000, representation_date=iso(60),
                               insurer_reply_date=iso(50), reply_outcome="rejected")
        elig = self.e.ombudsman_eligibility(cid)
        self.assertTrue(elig["eligible"])
        self.assertIsNotNone(elig["last_date_to_file"])

    def test_not_eligible_no_representation(self):
        cid = self.retail_case(amount=480000)
        self.assertFalse(self.e.ombudsman_eligibility(cid)["eligible"])

    def test_not_eligible_over_limit(self):
        cid = self.retail_case(amount=7500000, representation_date=iso(60),
                               insurer_reply_date=iso(50), reply_outcome="rejected")
        elig = self.e.ombudsman_eligibility(cid)
        self.assertFalse(elig["c4"])
        self.assertFalse(elig["eligible"])

    def test_not_eligible_pending_elsewhere(self):
        cid = self.retail_case(amount=200000, representation_date=iso(60), insurer_reply_date=iso(50),
                               reply_outcome="rejected", pending_forum="consumer_commission")
        self.assertFalse(self.e.ombudsman_eligibility(cid)["c5"])


# ─────────────────────────── deductions ───────────────────────────
class TestDeductions(Base):
    def test_allowed_gt_billed_rejected(self):
        cid = self.retail_case()
        with self.assertRaises(RuleViolation):
            self.e.add_deduction(cid, "Surgeon", 100000, 120000)

    def test_deduction_needs_reason(self):
        cid = self.retail_case()
        with self.assertRaises(RuleViolation):
            self.e.add_deduction(cid, "Implant", 165000, 103125)   # no reason_code

    def test_valid_deduction(self):
        cid = self.retail_case()
        self.e.add_deduction(cid, "Implant", 165000, 103125, reason_code="proportionate")


# ─────────────────────────── discharge voucher ───────────────────────────
class TestVoucher(Base):
    def test_under_protest_needs_balance(self):
        cid = self.retail_case()
        with self.assertRaises(RuleViolation):
            self.e.record_voucher(cid, "under_protest", 110000, balance_reserved=0)

    def test_under_protest_with_balance(self):
        cid = self.retail_case()
        self.e.record_voucher(cid, "under_protest", 110000, balance_reserved=280000)


# ─────────────────────────── health-data segregation ───────────────────────────
class TestHealthSegregation(Base):
    def test_no_medical_table_in_ordinary_store(self):
        self.assertFalse(self.e.health_visible_from_ordinary_store())

    def test_medical_record_requires_authority(self):
        with self.assertRaises(RuleViolation):
            self.e.store_medical_record("INS-1", "discharge_summary", b"cipher", "")

    def test_read_requires_health_scope(self):
        rid = self.e.store_medical_record("INS-1", "discharge_summary", b"cipher", "F-I01 consent")
        with self.assertRaises(RuleViolation) as cm:
            self.e.read_medical_record(rid, "menon", "case_manager", "INS-1", scope="ordinary")
        self.assertEqual(cm.exception.code, "health_scope_required")

    def test_read_is_access_logged(self):
        rid = self.e.store_medical_record("INS-1", "discharge_summary", b"cipher", "F-I01 consent")
        self.e.read_medical_record(rid, "menon", "case_manager", "INS-1", scope="health")
        n = self.store.health.execute("SELECT count(*) n FROM medical_access_log").fetchone()["n"]
        self.assertEqual(n, 1)


# ─────────────────────────── audit chain ───────────────────────────
class TestAuditChain(Base):
    def test_chain_verifies(self):
        cid = self.retail_case()
        self.e.deliver_signposting(cid)
        self.e.record_settlement(cid, 100000)
        ok, broken = self.store.verify_audit_chain()
        self.assertTrue(ok)
        self.assertIsNone(broken)

    def test_tampering_detected(self):
        cid = self.retail_case()
        self.e.record_settlement(cid, 100000)
        self.store.ordinary.execute("UPDATE audit_event SET detail='tampered' WHERE id=1")
        self.store.ordinary.commit()
        ok, broken = self.store.verify_audit_chain()
        self.assertFalse(ok)
        self.assertEqual(broken, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
