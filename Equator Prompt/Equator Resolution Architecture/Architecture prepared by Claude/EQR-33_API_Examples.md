# EQR-33 · API Examples (curl + JSON). Confidential. Companion to EQR-18/33.
BASE=https://sandbox.api.equatorresolution.com/v1 ; TOKEN=<bearer>

## Register a party
curl -X POST $BASE/parties -H "Authorization: Bearer $TOKEN" -H "Idempotency-Key: 7c1..." \
 -H "Content-Type: application/json" -d '{
  "full_name":"Meera Rao","dob":"1990-04-12","mobile":"+919812345678",
  "email":"meera@example.in","party_role":"Respondent","consent_flag":true }'
# 201 -> {"party_id":"01J...","full_name":"Meera Rao","role":"Respondent","kyc_status":"pending"}

## File a case (commercial arbitration)
curl -X POST $BASE/cases -H "Authorization: Bearer $TOKEN" -H "Idempotency-Key: 91a..." -d '{
  "claimant_ids":["01Jca..."],"respondent_ids":["01Jcb..."],
  "pillar":"Commercial","mechanism":"Arbitration","claim_value":450000,"currency":"INR",
  "facts":"Undelivered goods under PO-2211.","reliefs":"Payment + interest",
  "clause_ref":"PO-2211-arb","consent_flag":true }'
# 201 -> {"case_id":"EQR-2026-004821","pillar":"Commercial","status":"Filed","confidentiality_tier":"Standard"}

## Escalate a company ticket (must include consent)
curl -X POST $BASE/escalations -H "Authorization: Bearer $TOKEN" -d '{
  "source_system":"ArcusLMS","ticket_ref":"88421","party_consent_ref":"cons_01J...",
  "pillar":"NBFC","payload":{"loan_id":"L-99","amount":180000},
  "confidentiality_tier":"Standard","callback":"https://arcus.example/webhooks/equator" }'
# 201 -> {"escalation_id":"esc_01J...","case_id":"EQR-2026-004990","status":"case_created"}
# 409 -> {"code":"conflict","message":"party_consent_ref missing or invalid"}

## Get case status (timeline + clocks)
curl $BASE/cases/EQR-2026-004821/status -H "Authorization: Bearer $TOKEN"
# 200 -> {"case_id":"EQR-2026-004821","status":"InProceedings",
#   "timeline":[{"state":"Filed","at":"2026-06-02T10:02:00Z"}, ...],
#   "clocks":[{"name":"award_29a","due_at":"2027-05-15T00:00:00Z","state":"amber"}]}

## Initiate payment
curl -X POST $BASE/payments -H "Authorization: Bearer $TOKEN" -d '{"invoice_id":"inv_01J...","rail":"Razorpay"}'
# 201 -> {"payment_id":"pay_01J...","rail":"Razorpay","status":"created","redirect_url":"https://rzp..."}

## Dispute Explorer (advisory)
curl -X POST $BASE/explorer/sessions -H "Authorization: Bearer $TOKEN" -d '{
  "description":"Supplier didn'"'"'t deliver goods worth 4.5L after 50% advance; PO has arbitration clause.",
  "consent_flag":true }'
# 201 -> {"session_id":"exp_01J...","suggested_pillar":{"value":"Commercial","confidence":"High"},
#   "suggested_method":{"value":"Arbitration","why":"PO arbitration clause + written proof"},
#   "viability":{"band":"Reasonable","reasons":["written PO","proof of payment"]},
#   "recommended_next_step":{"value":"File","text":"File on Equator, pre-filled."},
#   "caveat":"Informational only; not legal advice."}

## Webhook signature (verify)
# header: X-Equator-Signature: sha256=<hex>
# verify: hmac_sha256(signing_secret, raw_body) == provided ; then process; dedupe on payload.event_id
