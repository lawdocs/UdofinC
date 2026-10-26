"""
Equator Resolution — reference implementation: domain rules.

This is where the institutional rules become executable. Each rule raises a
RuleViolation carrying the HTTP status the API contract promises, so the
specification and the implementation cannot drift apart silently.

Standard library only.
"""
import json, hashlib
from store import Store, _uid, _now

POSH_TYPES = {"posh", "sexual_harassment"}
STATUTORY_ROUTES = {"grc_ir_code", "statutory_forum", "drt_sarfaesi", "police"}


class RuleViolation(Exception):
    """Domain rule breach. `status` mirrors the OpenAPI contract."""
    def __init__(self, status, code, message):
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message


def _cipher(text: str) -> bytes:
    """Stand-in for field-level encryption. Real deployment: KMS/HSM-backed AES-256."""
    return hashlib.sha256(("equator-demo-key::" + text).encode()).digest() + text.encode()[:0]


class Equator:
    def __init__(self, store: Store):
        self.s = store

    # ---------------------------------------------------------------- cases
    def create_case(self, vertical, dispute_types, employer_id=None, employee_id=None):
        """
        R1 — a POSH matter is refused as an ordinary case (422).
        The caller must use open_posh_complaint() instead.
        """
        types = [t.strip().lower() for t in dispute_types]
        if POSH_TYPES & set(types):
            self.s.audit("case.create.refused_posh", detail=json.dumps(types))
            raise RuleViolation(422, "posh_must_be_sealed",
                                "A sexual-harassment matter cannot be created as an ordinary case. "
                                "Use the sealed POSH surface.")
        cid = _uid()
        n = self.s.ordinary.execute("SELECT COUNT(*) c FROM mediation_case").fetchone()["c"] + 1
        num = f"{vertical[:2].upper()}-{1000+n}"
        self.s.ordinary.execute(
            "INSERT INTO mediation_case (id,case_number,vertical,dispute_types,status,employer_id,"
            "employee_id,is_posh,safety_flag,opened_at) VALUES (?,?,?,?,'intake',?,?,0,0,?)",
            (cid, num, vertical, json.dumps(types), employer_id, employee_id, _now()))
        self.s.ordinary.commit()
        self.s.audit("case.create", case_id=cid, detail=num)
        return {"id": cid, "case_number": num, "status": "intake", "vertical": vertical,
                "dispute_types": types}

    def get_case(self, case_id):
        r = self.s.ordinary.execute("SELECT * FROM mediation_case WHERE id=?", (case_id,)).fetchone()
        if not r:
            raise RuleViolation(404, "not_found", "Case not found")
        d = dict(r); d["dispute_types"] = json.loads(d["dispute_types"]); return d

    # ------------------------------------------------------------- triage
    def run_triage(self, case_id):
        """Routes the matter. Statutory-only matters are signposted, not absorbed."""
        c = self.get_case(case_id)
        types = set(c["dispute_types"])
        if {"retrenchment_layoff", "union_dispute"} & types:
            route, rationale, status = ("grc_ir_code",
                "Collective or statutory industrial dispute — Industrial Relations Code machinery.", "signposted")
        elif {"secured_debt", "sarfaesi"} & types:
            route, rationale, status = ("drt_sarfaesi",
                "Secured enforcement is non-mediable; signposted. A settlement may be mediated around it.", "signposted")
        elif {"criminal", "assault", "threat"} & types:
            route, rationale, status = ("police",
                "Criminal conduct or a threat to safety — signposted to the police.", "signposted")
        else:
            route, rationale, status = ("mediation", "Suitable for mediation under the Equator Rules.", "triaged")
        self.s.ordinary.execute("UPDATE mediation_case SET route=?, status=? WHERE id=?",
                                (route, status, case_id))
        self.s.ordinary.commit()
        self.s.audit("case.triage", case_id=case_id, detail=route)
        return {"route": route, "rationale": rationale, "status": status,
                "mediable": route == "mediation"}

    # ---------------------------------------------------------- screening
    def record_screening(self, case_id, party_id, outcome, safeguards=""):
        """
        Screening is per-party and confidential. A safety outcome raises the case
        safety flag, which is what later blocks joint sessions.
        """
        self.get_case(case_id)
        sid = _uid()
        self.s.ordinary.execute(
            "INSERT INTO screening (id,case_id,party_id,outcome,safeguards,created_at) VALUES (?,?,?,?,?,?)",
            (sid, case_id, party_id, outcome, safeguards, _now()))
        raised = outcome in ("not_suitable_safety", "shuttle_only")
        if raised:
            self.s.ordinary.execute("UPDATE mediation_case SET safety_flag=1 WHERE id=?", (case_id,))
        self.s.ordinary.commit()
        self.s.audit("screening.record", case_id=case_id, detail=outcome)
        return {"outcome": outcome, "safety_flag_raised": raised,
                "joint_sessions_permitted": not raised}

    def screening_for_other_party(self, case_id, requesting_party_id):
        """
        Confidentiality: a party can never read another party's screening.
        Returns only the requester's own record.
        """
        rows = self.s.ordinary.execute(
            "SELECT * FROM screening WHERE case_id=? AND party_id=?",
            (case_id, requesting_party_id)).fetchall()
        return [dict(r) for r in rows]

    # ----------------------------------------------------------- sessions
    def schedule_session(self, case_id, mode, when):
        """
        R-SAFETY — a raised safety flag blocks a JOINT session at the API layer (409),
        not merely in the interface.
        """
        c = self.get_case(case_id)
        if mode == "joint" and c["safety_flag"] == 1:
            self.s.audit("session.blocked_safety_flag", case_id=case_id)
            raise RuleViolation(409, "safety_flag_blocks_joint_session",
                                "A safety flag is in force. Joint sessions are not available. "
                                "Shuttle mediation and support options are offered instead.")
        sid = _uid()
        self.s.ordinary.execute("INSERT INTO session (id,case_id,mode,scheduled_at) VALUES (?,?,?,?)",
                                (sid, case_id, mode, when))
        self.s.ordinary.execute("UPDATE mediation_case SET status='in_session' WHERE id=?", (case_id,))
        self.s.ordinary.commit()
        self.s.audit("session.schedule", case_id=case_id, detail=mode)
        return {"id": sid, "mode": mode, "scheduled_at": when}

    def add_caucus_note(self, session_id, neutral_id, text):
        nid = _uid()
        self.s.ordinary.execute(
            "INSERT INTO caucus_note (id,session_id,neutral_id,note_cipher,created_at) VALUES (?,?,?,?,?)",
            (nid, session_id, neutral_id, _cipher(text), _now()))
        self.s.ordinary.commit()
        self.s.audit("caucus.write", detail=session_id)
        return {"id": nid, "sealed": True}

    def read_caucus_notes(self, session_id, requester_role, requester_id, neutral_id):
        """Sealed to the appointed neutral. Any other requester is refused (403)."""
        if requester_role != "neutral" or requester_id != neutral_id:
            self.s.audit("caucus.read.denied", detail=f"{requester_role}:{requester_id}")
            raise RuleViolation(403, "caucus_sealed",
                                "Caucus notes are sealed to the appointed neutral (Mediation Act, s.22).")
        rows = self.s.ordinary.execute("SELECT id,created_at FROM caucus_note WHERE session_id=?",
                                       (session_id,)).fetchall()
        return [dict(r) for r in rows]

    # --------------------------------------------------------- F&F / money
    def compute_ff(self, monthly_wages, wages_pct_of_ctc, completed_years,
                   unpaid_salary=0.0, leave_encashment=0.0, bonus=0.0, deductions=0.0):
        """
        Gratuity = (15 x wages x completed years) / 26, on the Code on Wages
        definition. Where wages are below 50% of CTC the figure is flagged, because
        the Code requires the excess to be added back for statutory computation.
        """
        eligible = completed_years >= 5
        gratuity = (15 * monthly_wages * completed_years) / 26 if eligible else 0.0
        gross = unpaid_salary + leave_encashment + bonus + gratuity
        warn = wages_pct_of_ctc < 0.50
        return {"gratuity": round(gratuity, 2),
                "gratuity_eligible": eligible,
                "gross_earnings": round(gross, 2),
                "total_deductions": round(deductions, 2),
                "net_payable": round(gross - deductions, 2),
                "wage_definition_warning": warn,
                "warning_detail": ("Wages are below 50% of CTC. Under the Code on Wages, 2019 the excess "
                                   "must be added back for statutory computation — gratuity may be "
                                   "understated. Recompute before settling.") if warn else None,
                "indicative": True}

    def record_settlement(self, case_id, net_payable, gratuity_amount=0.0,
                          statutory_dues_waived=False, relieving_letter=False,
                          assets_returned=False):
        """R2 — a settlement asserting waiver of statutory dues is refused (422)."""
        self.get_case(case_id)
        if statutory_dues_waived:
            self.s.audit("settlement.refused_waiver", case_id=case_id)
            raise RuleViolation(422, "statutory_dues_cannot_be_waived",
                                "Gratuity, provident fund and ESI are paid, not waived. "
                                "Record their proper payment instead.")
        sid = _uid()
        self.s.ordinary.execute(
            "INSERT INTO settlement (id,case_id,net_payable,gratuity_amount,statutory_dues_waived,"
            "relieving_letter,assets_returned,enforceable_s27,signed_at) VALUES (?,?,?,?,0,?,?,1,?)",
            (sid, case_id, net_payable, gratuity_amount,
             int(relieving_letter), int(assets_returned), _now()))
        self.s.ordinary.execute("UPDATE mediation_case SET status='settlement' WHERE id=?", (case_id,))
        self.s.ordinary.commit()
        self.s.audit("settlement.record", case_id=case_id, detail=str(net_payable))
        return {"id": sid, "net_payable": net_payable, "enforceable_s27": True}

    def create_escrow(self, case_id, amount, milestones):
        eid = _uid()
        self.s.ordinary.execute("INSERT INTO escrow (id,case_id,amount,state) VALUES (?,?,?,'funded')",
                                (eid, case_id, amount))
        for m in milestones:
            self.s.ordinary.execute(
                "INSERT INTO escrow_milestone (id,escrow_id,name,condition,amount,released) VALUES (?,?,?,?,?,0)",
                (_uid(), eid, m["name"], m["condition"], m["amount"]))
        self.s.ordinary.commit()
        self.s.audit("escrow.create", case_id=case_id, detail=str(amount))
        return {"id": eid, "state": "funded"}

    def release_milestone(self, escrow_id, milestone_name):
        """The final tranche is conditional on relieving letter and asset return (409)."""
        m = self.s.ordinary.execute(
            "SELECT * FROM escrow_milestone WHERE escrow_id=? AND name=?",
            (escrow_id, milestone_name)).fetchone()
        if not m:
            raise RuleViolation(404, "not_found", "Milestone not found")
        e = self.s.ordinary.execute("SELECT * FROM escrow WHERE id=?", (escrow_id,)).fetchone()
        if m["condition"] == "relieving_and_assets":
            st = self.s.ordinary.execute("SELECT * FROM settlement WHERE case_id=?",
                                         (e["case_id"],)).fetchone()
            if not st or not (st["relieving_letter"] and st["assets_returned"]):
                self.s.audit("escrow.release.blocked", case_id=e["case_id"], detail=milestone_name)
                raise RuleViolation(409, "milestone_conditions_not_met",
                                    "Final release requires the relieving letter to be issued and "
                                    "company assets returned.")
        self.s.ordinary.execute("UPDATE escrow_milestone SET released=1 WHERE id=?", (m["id"],))
        self.s.ordinary.commit()
        self.s.audit("escrow.release", case_id=e["case_id"], detail=milestone_name)
        return {"released": True, "milestone": milestone_name, "amount": m["amount"]}

    # ------------------------------------------------------- sealed POSH
    def open_posh_complaint(self, employer_ref, complainant, respondent, particulars, scope):
        """R3 — requires the `posh` scope; data lands in the separate store."""
        if "posh" not in scope:
            raise RuleViolation(403, "posh_scope_required",
                                "The POSH surface requires the 'posh' scope, held by Internal-Committee "
                                "members and designated support only.")
        cid = _uid()
        n = self.s.posh.execute("SELECT COUNT(*) c FROM posh_complaint").fetchone()["c"] + 1
        self.s.posh.execute(
            "INSERT INTO posh_complaint (id,complaint_number,employer_ref,received_on,stage,"
            "complainant_cipher,respondent_cipher,particulars_cipher) VALUES (?,?,?,?,'received',?,?,?)",
            (cid, f"POSH-{400+n}", employer_ref, _now(),
             _cipher(complainant), _cipher(respondent), _cipher(particulars)))
        self.s.posh.commit()
        self.s.audit("posh.complaint.open", store="posh", detail=f"POSH-{400+n}")
        return {"id": cid, "complaint_number": f"POSH-{400+n}", "sealed": True}

    def constitute_ic(self, employer_ref, presiding_officer, member_count, women_members,
                      external_member_id, scope):
        """POSH s.4 — external member mandatory; at least half the members women."""
        if "posh" not in scope:
            raise RuleViolation(403, "posh_scope_required", "The POSH surface requires the 'posh' scope.")
        if not external_member_id:
            raise RuleViolation(422, "external_member_required",
                                "POSH s.4 requires at least one external member.")
        if women_members * 2 < member_count + 1:
            raise RuleViolation(422, "women_members_insufficient",
                                "POSH s.4 requires at least half the members to be women.")
        iid = _uid()
        self.s.posh.execute(
            "INSERT INTO internal_committee (id,employer_ref,presiding_officer,member_count,"
            "women_members,external_member_id) VALUES (?,?,?,?,?,?)",
            (iid, employer_ref, presiding_officer, member_count, women_members, external_member_id))
        self.s.posh.commit()
        self.s.audit("posh.ic.constitute", store="posh", detail=employer_ref)
        return {"id": iid, "compliant": True}

    def record_s10_conciliation(self, complaint_id, requested_by_woman, monetary_basis, terms, scope):
        """POSH s.10 — her request only, and never on a monetary basis (422)."""
        if "posh" not in scope:
            raise RuleViolation(403, "posh_scope_required", "The POSH surface requires the 'posh' scope.")
        if not requested_by_woman:
            self.s.audit("posh.s10.refused_not_her_request", store="posh")
            raise RuleViolation(422, "s10_requires_aggrieved_womans_request",
                                "Conciliation under s.10 may only be attempted at the aggrieved woman's "
                                "request. The Committee cannot initiate it, nor may the respondent request it.")
        if monetary_basis:
            self.s.audit("posh.s10.refused_monetary", store="posh")
            raise RuleViolation(422, "s10_no_monetary_basis",
                                "No monetary settlement may be made the basis of conciliation under s.10.")
        rid = _uid()
        self.s.posh.execute(
            "INSERT INTO posh_conciliation (id,complaint_id,requested_by_woman,monetary_basis,terms_cipher)"
            " VALUES (?,?,1,0,?)", (rid, complaint_id, _cipher(terms)))
        self.s.posh.commit()
        self.s.audit("posh.s10.record", store="posh", detail=complaint_id)
        return {"id": rid, "recorded": True, "forwarded_to_employer": True}

    def posh_visible_from_ordinary_store(self):
        """
        Proof of R3: the ordinary connection cannot even see the POSH tables.
        Returns the tables the ordinary store can enumerate.
        """
        rows = self.s.ordinary.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        return [r["name"] for r in rows]
