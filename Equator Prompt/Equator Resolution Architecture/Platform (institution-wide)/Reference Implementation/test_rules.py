"""
Equator Resolution — executable proof of the institutional rules.

Every test here corresponds to a UAT script in the Test & UAT Plan and to a
guard constraint in the DDL. If a test fails, the specification is wrong or the
implementation drifted — either way the build should not ship.

Run:  python3 test_rules.py          (standard library only)
"""
import unittest, sqlite3, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from store import Store, _uid, _now
from domain import Equator, RuleViolation


class Base(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.eq = Equator(self.store)
        self.store.ordinary.execute(
            "INSERT INTO employer (id,name,estab_size,posh_subscriber,ic_constituted)"
            " VALUES ('emp1','Acme Ltd','300_plus',1,1)")
        for pid, role in (("p1", "employee"), ("p2", "employer")):
            self.store.ordinary.execute(
                "INSERT INTO party (id,role,full_name,created_at) VALUES (?,?,?,?)",
                (pid, role, f"Party {pid}", _now()))
        self.store.ordinary.commit()

    def tearDown(self):
        self.store.close()


class TestSafetyFlag(Base):
    """UAT-04 / WU: a safety flag must block a joint session at the API, not the UI."""

    def test_joint_session_blocked_when_safety_flag_raised(self):
        c = self.eq.create_case("family", ["custody", "maintenance"])
        r = self.eq.record_screening(c["id"], "p1", "not_suitable_safety", "shuttle only")
        self.assertTrue(r["safety_flag_raised"])
        self.assertFalse(r["joint_sessions_permitted"])
        with self.assertRaises(RuleViolation) as cm:
            self.eq.schedule_session(c["id"], "joint", "2026-08-01T10:00:00Z")
        self.assertEqual(cm.exception.status, 409)
        self.assertEqual(cm.exception.code, "safety_flag_blocks_joint_session")

    def test_shuttle_still_available_when_flag_raised(self):
        c = self.eq.create_case("family", ["custody"])
        self.eq.record_screening(c["id"], "p1", "not_suitable_safety")
        s = self.eq.schedule_session(c["id"], "shuttle", "2026-08-01T10:00:00Z")
        self.assertEqual(s["mode"], "shuttle")

    def test_joint_session_allowed_when_screening_clear(self):
        c = self.eq.create_case("family", ["maintenance"])
        r = self.eq.record_screening(c["id"], "p1", "suitable")
        self.assertFalse(r["safety_flag_raised"])
        s = self.eq.schedule_session(c["id"], "joint", "2026-08-01T10:00:00Z")
        self.assertEqual(s["mode"], "joint")

    def test_database_rejects_posh_case_in_ordinary_state(self):
        """The CHECK constraint is the backstop if application code is bypassed."""
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.ordinary.execute(
                "INSERT INTO mediation_case (id,case_number,vertical,dispute_types,status,is_posh,"
                "safety_flag,opened_at) VALUES (?,?,?,?,?,1,0,?)",
                (_uid(), "XX-9999", "workplace", '["posh"]', "in_session", _now()))
            self.store.ordinary.commit()


class TestPoshSeal(Base):
    """POSH matters are refused as ordinary cases and live in a separate store."""

    def test_posh_refused_as_ordinary_case(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.create_case("workplace", ["posh"])
        self.assertEqual(cm.exception.status, 422)
        self.assertEqual(cm.exception.code, "posh_must_be_sealed")

    def test_posh_surface_requires_scope(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.open_posh_complaint("emp1", "A", "B", "particulars", scope=[])
        self.assertEqual(cm.exception.status, 403)

    def test_posh_tables_are_not_visible_from_ordinary_store(self):
        """R3: no join path exists — the ordinary connection cannot see the POSH tables."""
        tables = self.eq.posh_visible_from_ordinary_store()
        for t in ("posh_complaint", "internal_committee", "posh_conciliation"):
            self.assertNotIn(t, tables)
        with self.assertRaises(sqlite3.OperationalError):
            self.store.ordinary.execute("SELECT * FROM posh_complaint").fetchall()

    def test_ic_requires_external_member(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.constitute_ic("emp1", "Ms P", 4, 3, external_member_id=None, scope=["posh"])
        self.assertEqual(cm.exception.code, "external_member_required")

    def test_ic_requires_half_women(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.constitute_ic("emp1", "Ms P", 4, 1, external_member_id="ext1", scope=["posh"])
        self.assertEqual(cm.exception.code, "women_members_insufficient")

    def test_ic_valid_composition_accepted(self):
        r = self.eq.constitute_ic("emp1", "Ms P", 4, 3, external_member_id="ext1", scope=["posh"])
        self.assertTrue(r["compliant"])

    def test_database_rejects_ic_without_external_member(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.posh.execute(
                "INSERT INTO internal_committee (id,employer_ref,presiding_officer,member_count,"
                "women_members,external_member_id) VALUES (?,?,?,?,?,NULL)",
                (_uid(), "emp1", "Ms P", 4, 3))
            self.store.posh.commit()


class TestSection10(Base):
    """POSH s.10 — her request only, never on a monetary basis."""

    def setUp(self):
        super().setUp()
        self.c = self.eq.open_posh_complaint("emp1", "A", "B", "particulars", scope=["posh"])

    def test_conciliation_refused_if_not_her_request(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.record_s10_conciliation(self.c["id"], False, False, "terms", scope=["posh"])
        self.assertEqual(cm.exception.status, 422)
        self.assertEqual(cm.exception.code, "s10_requires_aggrieved_womans_request")

    def test_conciliation_refused_on_monetary_basis(self):
        with self.assertRaises(RuleViolation) as cm:
            self.eq.record_s10_conciliation(self.c["id"], True, True, "pay 2 lakh", scope=["posh"])
        self.assertEqual(cm.exception.code, "s10_no_monetary_basis")

    def test_valid_conciliation_recorded_and_forwarded(self):
        r = self.eq.record_s10_conciliation(self.c["id"], True, False,
                                            "written apology; transfer; no retaliation", scope=["posh"])
        self.assertTrue(r["recorded"])
        self.assertTrue(r["forwarded_to_employer"])

    def test_database_rejects_monetary_conciliation(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.posh.execute(
                "INSERT INTO posh_conciliation (id,complaint_id,requested_by_woman,monetary_basis)"
                " VALUES (?,?,1,1)", (_uid(), self.c["id"]))
            self.store.posh.commit()


class TestStatutoryDues(Base):
    """Gratuity, PF and ESI are paid, never waived."""

    def test_settlement_refused_if_waiver_asserted(self):
        c = self.eq.create_case("workplace", ["full_and_final"])
        with self.assertRaises(RuleViolation) as cm:
            self.eq.record_settlement(c["id"], 196795, 138462, statutory_dues_waived=True)
        self.assertEqual(cm.exception.status, 422)
        self.assertEqual(cm.exception.code, "statutory_dues_cannot_be_waived")

    def test_database_rejects_waiver(self):
        c = self.eq.create_case("workplace", ["full_and_final"])
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.ordinary.execute(
                "INSERT INTO settlement (id,case_id,net_payable,statutory_dues_waived) VALUES (?,?,?,1)",
                (_uid(), c["id"], 100000))
            self.store.ordinary.commit()

    def test_compliant_settlement_accepted(self):
        c = self.eq.create_case("workplace", ["full_and_final"])
        r = self.eq.record_settlement(c["id"], 196795, 138462, statutory_dues_waived=False)
        self.assertTrue(r["enforceable_s27"])


class TestFullAndFinal(Base):
    """Code on Wages arithmetic, and the warning that catches under-computed gratuity."""

    def test_gratuity_formula(self):
        r = self.eq.compute_ff(monthly_wages=40000, wages_pct_of_ctc=0.55, completed_years=6)
        self.assertAlmostEqual(r["gratuity"], round(15 * 40000 * 6 / 26, 2), places=2)
        self.assertTrue(r["gratuity_eligible"])
        self.assertFalse(r["wage_definition_warning"])

    def test_wage_definition_warning_below_50pct(self):
        r = self.eq.compute_ff(monthly_wages=40000, wages_pct_of_ctc=0.32, completed_years=6)
        self.assertTrue(r["wage_definition_warning"])
        self.assertIn("Code on Wages", r["warning_detail"])

    def test_gratuity_not_payable_below_five_years(self):
        r = self.eq.compute_ff(monthly_wages=40000, wages_pct_of_ctc=0.55, completed_years=3)
        self.assertEqual(r["gratuity"], 0.0)
        self.assertFalse(r["gratuity_eligible"])

    def test_net_payable_arithmetic(self):
        r = self.eq.compute_ff(40000, 0.55, 6, unpaid_salary=60000, leave_encashment=25000,
                               bonus=20000, deductions=8000)
        self.assertAlmostEqual(r["net_payable"], r["gross_earnings"] - 8000, places=2)


class TestConfidentiality(Base):
    """Caucus notes are sealed to the neutral; screening is per-party."""

    def test_caucus_notes_denied_to_party(self):
        c = self.eq.create_case("family", ["maintenance"])
        self.eq.record_screening(c["id"], "p1", "suitable")
        s = self.eq.schedule_session(c["id"], "caucus", "2026-08-01T10:00:00Z")
        self.eq.add_caucus_note(s["id"], "neutral1", "party A flexible on quantum")
        with self.assertRaises(RuleViolation) as cm:
            self.eq.read_caucus_notes(s["id"], "party", "p2", "neutral1")
        self.assertEqual(cm.exception.status, 403)

    def test_caucus_notes_available_to_appointed_neutral(self):
        c = self.eq.create_case("family", ["maintenance"])
        self.eq.record_screening(c["id"], "p1", "suitable")
        s = self.eq.schedule_session(c["id"], "caucus", "2026-08-01T10:00:00Z")
        self.eq.add_caucus_note(s["id"], "neutral1", "note")
        rows = self.eq.read_caucus_notes(s["id"], "neutral", "neutral1", "neutral1")
        self.assertEqual(len(rows), 1)

    def test_party_cannot_read_other_partys_screening(self):
        c = self.eq.create_case("family", ["custody"])
        self.eq.record_screening(c["id"], "p1", "not_suitable_safety", "fear of contact")
        visible = self.eq.screening_for_other_party(c["id"], "p2")
        self.assertEqual(visible, [])


class TestTriage(Base):
    """Statutory matters are signposted, not absorbed."""

    def test_mediable_matter_routes_to_mediation(self):
        c = self.eq.create_case("workplace", ["wage_dues"])
        r = self.eq.run_triage(c["id"])
        self.assertEqual(r["route"], "mediation")
        self.assertTrue(r["mediable"])

    def test_collective_dispute_signposted(self):
        c = self.eq.create_case("workplace", ["retrenchment_layoff"])
        r = self.eq.run_triage(c["id"])
        self.assertEqual(r["route"], "grc_ir_code")
        self.assertEqual(r["status"], "signposted")
        self.assertFalse(r["mediable"])

    def test_secured_debt_signposted_not_mediated(self):
        c = self.eq.create_case("financial", ["secured_debt"])
        r = self.eq.run_triage(c["id"])
        self.assertEqual(r["route"], "drt_sarfaesi")
        self.assertFalse(r["mediable"])

    def test_criminal_signposted_to_police(self):
        c = self.eq.create_case("family", ["assault"])
        r = self.eq.run_triage(c["id"])
        self.assertEqual(r["route"], "police")


class TestEscrow(Base):
    """Final release is conditional on relieving letter and asset return."""

    def setUp(self):
        super().setUp()
        self.c = self.eq.create_case("workplace", ["full_and_final"])
        self.e = self.eq.create_escrow(self.c["id"], 196795, [
            {"name": "on_signature", "condition": "signed", "amount": 100000},
            {"name": "final", "condition": "relieving_and_assets", "amount": 96795}])

    def test_first_tranche_releases(self):
        r = self.eq.release_milestone(self.e["id"], "on_signature")
        self.assertTrue(r["released"])

    def test_final_tranche_blocked_without_relieving(self):
        self.eq.record_settlement(self.c["id"], 196795, 138462,
                                  relieving_letter=False, assets_returned=False)
        with self.assertRaises(RuleViolation) as cm:
            self.eq.release_milestone(self.e["id"], "final")
        self.assertEqual(cm.exception.status, 409)
        self.assertEqual(cm.exception.code, "milestone_conditions_not_met")

    def test_final_tranche_releases_when_conditions_met(self):
        self.eq.record_settlement(self.c["id"], 196795, 138462,
                                  relieving_letter=True, assets_returned=True)
        r = self.eq.release_milestone(self.e["id"], "final")
        self.assertTrue(r["released"])


class TestAuditChain(Base):
    """The audit log is hash-chained, so tampering is detectable."""

    def test_chain_valid_after_normal_activity(self):
        c = self.eq.create_case("family", ["maintenance"])
        self.eq.run_triage(c["id"])
        self.eq.record_screening(c["id"], "p1", "suitable")
        ok, broken = self.store.verify_audit_chain()
        self.assertTrue(ok)
        self.assertIsNone(broken)

    def test_tampering_is_detected(self):
        c = self.eq.create_case("family", ["maintenance"])
        self.eq.run_triage(c["id"])
        self.store.ordinary.execute(
            "UPDATE audit_event SET detail='tampered' WHERE id=(SELECT MIN(id) FROM audit_event)")
        self.store.ordinary.commit()
        ok, broken = self.store.verify_audit_chain()
        self.assertFalse(ok)
        self.assertIsNotNone(broken)


if __name__ == "__main__":
    unittest.main(verbosity=2)
