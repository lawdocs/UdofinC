"""
Equator Resolution — Insurance vertical reference implementation: domain layer.

Thin service layer over store.py. It translates the database constraints into
HTTP-shaped RuleViolations (the same 409/422 the OpenAPI spec documents) and adds the
logic that is not expressible as a single CHECK: the clock engine, the Ombudsman
eligibility engine, and the R3 closure guard.

The tests in test_rules.py prove that the three institutional rules cannot be bypassed.
"""
import sqlite3, datetime
from store import Store, _uid, _now


class RuleViolation(Exception):
    def __init__(self, status, rule, code, message):
        super().__init__(message)
        self.status = status      # 409 / 422 / 403
        self.rule = rule          # R1 / R2 / R3
        self.code = code
        self.message = message


def _d(s):
    return datetime.date.fromisoformat(s) if s else None


def _today():
    return datetime.date.today()


CLOCK_PERIODS = {
    "insurer_reply_30d": 30,
    "ombudsman_1y": 365,
    "consumer_2y": 730,
}


class Equator:
    def __init__(self, store: Store):
        self.s = store

    # ---------- setup ----------
    def add_insurer(self, name):
        iid = _uid()
        self.s.ordinary.execute("INSERT INTO insurer (id,name) VALUES (?,?)", (iid, name))
        self.s.ordinary.commit()
        return iid

    def add_policy(self, insurer_id, policy_no, line, cls, legacy_arb=False):
        pid = _uid()
        self.s.ordinary.execute(
            "INSERT INTO policy (id,insurer_id,policy_no,line,class,legacy_arbitration_clause)"
            " VALUES (?,?,?,?,?,?)", (pid, insurer_id, policy_no, line, cls, 1 if legacy_arb else 0))
        self.s.ordinary.commit()
        return pid

    # ---------- create case ----------
    def create_case(self, case_no, policy_id, amount=0.0, fraud_alleged=False,
                    representation_date=None, insurer_reply_date=None, reply_outcome=None,
                    pending_forum=None):
        row = self.s.ordinary.execute("SELECT class FROM policy WHERE id=?", (policy_id,)).fetchone()
        if row is None:
            raise RuleViolation(422, "—", "policy_missing", "policy_id does not exist")
        is_retail = 1 if row["class"] in ("retail", "group_member") else 0
        cid = _uid()
        self.s.ordinary.execute(
            "INSERT INTO dispute_case (id,case_no,policy_id,amount_in_dispute,is_retail,fraud_alleged,"
            "status,representation_date,insurer_reply_date,reply_outcome,pending_forum,opened_at)"
            " VALUES (?,?,?,?,?,?, 'intake', ?,?,?,?,?)",
            (cid, case_no, policy_id, amount, is_retail, 1 if fraud_alleged else 0,
             representation_date, insurer_reply_date, reply_outcome, pending_forum, _now()))
        self.s.ordinary.commit()
        self.s.audit("case.create", case_id=cid, detail=case_no)
        # seed the clocks that the dates allow
        self._seed_clocks(cid)
        return cid

    def _seed_clocks(self, case_id):
        c = self.s.ordinary.execute(
            "SELECT representation_date, insurer_reply_date FROM dispute_case WHERE id=?", (case_id,)).fetchone()
        rep, reply = c["representation_date"], c["insurer_reply_date"]
        if rep:
            self.add_clock(case_id, "insurer_reply_30d", rep)
            trig = reply if reply else (_d(rep) + datetime.timedelta(days=30)).isoformat()
            self.add_clock(case_id, "ombudsman_1y", trig)

    def add_clock(self, case_id, kind, trigger_date, owner=None):
        try:
            self.s.ordinary.execute(
                "INSERT INTO clock (id,case_id,kind,trigger_date,period_days,owner) VALUES (?,?,?,?,?,?)",
                (_uid(), case_id, kind, trigger_date, CLOCK_PERIODS.get(kind, 365), owner))
            self.s.ordinary.commit()
        except sqlite3.IntegrityError:
            pass

    def clock_table(self, case_id):
        out = []
        for r in self.s.ordinary.execute("SELECT * FROM clock WHERE case_id=?", (case_id,)):
            exp = _d(r["trigger_date"]) + datetime.timedelta(days=r["period_days"])
            out.append({"kind": r["kind"], "expiry": exp.isoformat(),
                        "days_left": (exp - _today()).days, "owner": r["owner"],
                        "prompted_at": r["prompted_at"]})
        return out

    def set_clock_owner(self, case_id, kind, owner):
        self.s.ordinary.execute("UPDATE clock SET owner=? WHERE case_id=? AND kind=?", (owner, case_id, kind))
        self.s.ordinary.commit()

    def record_prompt(self, case_id, kind):
        self.s.ordinary.execute("UPDATE clock SET prompted_at=? WHERE case_id=? AND kind=?",
                                (_now(), case_id, kind))
        self.s.ordinary.commit()
        self.s.audit("clock.prompt", case_id=case_id, detail=kind)

    # ---------- signposting ----------
    def deliver_signposting(self, case_id, channel="call", language="en",
                            script_version="v3.1", delivered_by="case_manager"):
        self.s.ordinary.execute(
            "INSERT INTO signposting_event (id,case_id,delivered_at,channel,language,script_version,delivered_by)"
            " VALUES (?,?,?,?,?,?,?)", (_uid(), case_id, _now(), channel, language, script_version, delivered_by))
        self.s.ordinary.commit()
        self.s.audit("signposting.deliver", case_id=case_id)

    # ---------- triage ----------
    def triage(self, case_id, route, classified_by, reviewed_by):
        c = self.s.ordinary.execute(
            "SELECT is_retail, fraud_alleged FROM dispute_case WHERE id=?", (case_id,)).fetchone()
        # R1 — the retail arbitration bar (mirror the DB CHECK with a friendly 409)
        if route == "arbitration" and c["is_retail"]:
            raise RuleViolation(
                409, "R1", "no_arbitration_on_retail",
                "Retail policies shall not carry an arbitration clause (IRDAI circular, 27 October 2023). "
                "Available routes: insurer_grievance, insurance_ombudsman, consumer_commission, civil_court, "
                "equator_mediation.")
        if c["fraud_alleged"] and route == "equator_mediation":
            raise RuleViolation(409, "R1", "no_mediation_of_alleged_fraud",
                                "A fraud allegation is not mediated; investigate or litigate.")
        # second-officer review
        if reviewed_by == classified_by:
            raise RuleViolation(409, "R1", "reviewer_must_differ",
                                "The retail/commercial classification must be reviewed by a second officer.")
        # must be signposted before leaving triage (part of R3)
        n = self.s.ordinary.execute("SELECT count(*) n FROM signposting_event WHERE case_id=?",
                                    (case_id,)).fetchone()["n"]
        if n == 0:
            raise RuleViolation(409, "R3", "signposting_required",
                                "A case cannot leave triage without a recorded signposting event.")
        try:
            self.s.ordinary.execute("INSERT INTO triage (id,case_id,classified_by,reviewed_by) VALUES (?,?,?,?)",
                                    (_uid(), case_id, classified_by, reviewed_by))
            self.s.ordinary.execute("UPDATE dispute_case SET route=?, status='triaged' WHERE id=?", (route, case_id))
            self.s.ordinary.commit()
        except sqlite3.IntegrityError as e:
            # the DB CHECK is the backstop if the friendly guard above is ever bypassed
            raise RuleViolation(409, "R1", "constraint", str(e))
        self.s.audit("case.triage", case_id=case_id, detail=route)

    def force_arbitration_via_sql(self, case_id):
        """Test hook: attempt to bypass the service and write arbitration directly. The DB must refuse."""
        self.s.ordinary.execute("UPDATE dispute_case SET route='arbitration' WHERE id=?", (case_id,))
        self.s.ordinary.commit()

    # ---------- Ombudsman eligibility engine ----------
    def ombudsman_eligibility(self, case_id):
        c = self.s.ordinary.execute("SELECT * FROM dispute_case WHERE id=?", (case_id,)).fetchone()
        rep = _d(c["representation_date"]); reply = _d(c["insurer_reply_date"])
        today = _today()
        c1 = rep is not None
        c2 = (c["reply_outcome"] in ("rejected", "unsatisfactory")) or (rep is not None and (today - rep).days > 30)
        trig = reply if reply else (rep + datetime.timedelta(days=30) if rep else None)
        c3 = (trig is not None) and (today <= trig + datetime.timedelta(days=365))
        c4 = c["amount_in_dispute"] <= 5000000 if c["amount_in_dispute"] else True
        c5 = c["pending_forum"] is None
        last_date = (trig + datetime.timedelta(days=365)).isoformat() if trig else None
        return {"c1": c1, "c2": bool(c2), "c3": bool(c3), "c4": bool(c4), "c5": bool(c5),
                "eligible": all([c1, c2, c3, c4, c5]), "last_date_to_file": last_date}

    # ---------- deductions ----------
    def add_deduction(self, case_id, head, billed, allowed, reason_code=None):
        if allowed > billed:
            raise RuleViolation(422, "—", "deduction_arith", "allowed cannot exceed billed")
        if billed != allowed and not reason_code:
            raise RuleViolation(422, "—", "reason_required", "a non-zero deduction requires a reason code")
        self.s.ordinary.execute(
            "INSERT INTO deduction_line (id,case_id,head,billed,allowed,reason_code) VALUES (?,?,?,?,?,?)",
            (_uid(), case_id, head, billed, allowed, reason_code))
        self.s.ordinary.commit()

    # ---------- settlement (R2) ----------
    def record_settlement(self, case_id, amount, continuity=False,
                          statutory_rights_waived=False, future_claims_discharged=False):
        if statutory_rights_waived:
            raise RuleViolation(422, "R2", "no_statutory_waiver",
                                "A settlement may not recite waiver of a non-waivable statutory right.")
        if future_claims_discharged:
            raise RuleViolation(422, "R2", "no_future_discharge",
                                "A settlement may not purport to discharge future claims.")
        try:
            self.s.ordinary.execute(
                "INSERT INTO settlement (id,case_id,amount,continuity_preserved,statutory_rights_waived,"
                "future_claims_discharged) VALUES (?,?,?,?,0,0)",
                (_uid(), case_id, amount, 1 if continuity else 0))
            self.s.ordinary.execute("UPDATE dispute_case SET status='settlement' WHERE id=?", (case_id,))
            self.s.ordinary.commit()
        except sqlite3.IntegrityError as e:
            raise RuleViolation(422, "R2", "constraint", str(e))
        self.s.audit("case.settlement", case_id=case_id, detail=str(amount))

    def force_waiver_via_sql(self, case_id, amount):
        """Test hook: attempt to write a waiver settlement directly. The DB must refuse."""
        self.s.ordinary.execute(
            "INSERT INTO settlement (id,case_id,amount,statutory_rights_waived) VALUES (?,?,?,1)",
            (_uid(), case_id, amount))
        self.s.ordinary.commit()

    def register_settlement(self, case_id):
        self.s.ordinary.execute("UPDATE settlement SET registered_at=? WHERE case_id=?", (_now(), case_id))
        self.s.ordinary.commit()

    # ---------- discharge voucher ----------
    def record_voucher(self, case_id, basis, amount, balance_reserved=0.0):
        if basis == "under_protest" and balance_reserved <= 0:
            raise RuleViolation(422, "—", "protest_needs_balance",
                                "An 'under protest' voucher must reserve a balance.")
        try:
            self.s.ordinary.execute(
                "INSERT INTO discharge_voucher (id,case_id,basis,amount,balance_reserved) VALUES (?,?,?,?,?)",
                (_uid(), case_id, basis, amount, balance_reserved))
            self.s.ordinary.commit()
        except sqlite3.IntegrityError as e:
            raise RuleViolation(422, "—", "constraint", str(e))

    # ---------- closure (R3) ----------
    def close_case(self, case_id):
        n = self.s.ordinary.execute("SELECT count(*) n FROM signposting_event WHERE case_id=?",
                                    (case_id,)).fetchone()["n"]
        if n == 0:
            raise RuleViolation(409, "R3", "no_signposting",
                                "Cannot close: no signposting event recorded.")
        unowned = self.s.ordinary.execute(
            "SELECT count(*) n FROM clock WHERE case_id=? AND owner IS NULL", (case_id,)).fetchone()["n"]
        if unowned:
            raise RuleViolation(409, "R3", "unowned_clock",
                                f"Cannot close: {unowned} clock(s) have no owner.")
        self.s.ordinary.execute("UPDATE dispute_case SET status='closed' WHERE id=?", (case_id,))
        self.s.ordinary.commit()
        self.s.audit("case.close", case_id=case_id)

    # ---------- health store (segregation) ----------
    def store_medical_record(self, case_ref, doc_type, content, authority_ref):
        if not authority_ref:
            raise RuleViolation(403, "—", "authority_required",
                                "A medical record requires an authority reference on file.")
        rid = _uid()
        self.s.health.execute(
            "INSERT INTO medical_record (id,case_ref,doc_type,content_cipher,authority_ref,received_at)"
            " VALUES (?,?,?,?,?,?)", (rid, case_ref, doc_type, content, authority_ref, _now()))
        self.s.health.commit()
        return rid

    def read_medical_record(self, record_id, actor, actor_role, case_ref, scope):
        if scope != "health":
            raise RuleViolation(403, "—", "health_scope_required", "Reading a medical record requires the health scope.")
        r = self.s.health.execute("SELECT * FROM medical_record WHERE id=?", (record_id,)).fetchone()
        if r is None:
            raise RuleViolation(404, "—", "not_found", "no such record")
        self.s.health.execute(
            "INSERT INTO medical_access_log (record_id,actor,actor_role,case_ref,accessed_at) VALUES (?,?,?,?,?)",
            (record_id, actor, actor_role, case_ref, _now()))
        self.s.health.commit()
        return r["content_cipher"]

    def health_visible_from_ordinary_store(self):
        """There is no table in the ordinary store that references medical_record."""
        names = [r["name"] for r in self.s.ordinary.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")]
        return "medical_record" in names
