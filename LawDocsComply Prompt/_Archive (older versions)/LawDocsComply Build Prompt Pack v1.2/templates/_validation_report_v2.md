# Template validation report — contract v2.0 (pack v1.2)

Run: `python3 templates/_validate_templates_v2.py templates` · Contract: `templates/_build/v12_contract.py` · Date: 2026-10-25

**Result: 29/29 PASS**

## Tests

| Test | Check |
|---|---|
| T01 | Sheets and order (register, Lists, Read Me, _Template_Info) |
| T02 | Template identity in _Template_Info (code, version 2.0, family, sheet, column count) |
| T03 | Row-2 headers equal the contract, in order, nothing after the last column |
| T04 | Header SHA-256 and key SHA-256 recorded and correct |
| T05 | Column contract table in _Template_Info matches headers, keys and letters |
| T06 | Row-1 group bands: labels, merges, colours, order |
| T07 | Base keys complete and in order; extension columns = family allowance (0–4) placed after Applicable Until |
| T08 | Lists: family vocabularies exact; base vocabularies (frequency, department, compliance type, risk, status, risk type, change, RAG, audit result) present |
| T09 | Named ranges exist and resolve to the Lists values |
| T10 | Data validation on every dropdown/date column for rows 3–5000; dependent lists; multi-value columns non-blocking |
| T11 | Department → Function → Sub-function matrix complete |
| T12 | Outline: 9 list-view columns visible; other groups hidden (level 1 first column, level 2 rest) |
| T13 | Freeze panes D3; AutoFilter on row 2 across all columns |
| T14 | Print area A:I, titles rows 1–2, A4 landscape, fit to one page wide |
| T15 | _Template_Info protected; no data rows; RAG conditional formatting; Read Me legend |

## Results by workbook

| Workbook | Columns | T01 | T02 | T03 | T04 | T05 | T06 | T07 | T08 | T09 | T10 | T11 | T12 | T13 | T14 | T15 | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LDC-TPL-AI-GOV-v2.0 - AI Governance.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-COOP-CCS-v2.0 - Credit Co-operative Societies.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-COOP-GEN-v2.0 - Other Co-operative Societies.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-CYBER-v2.0 - Cyber Security.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-DATA-PRIV-v2.0 - Data Protection and Privacy.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-ESG-BRSR-v2.0 - ESG BRSR and CSR.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-GOV-v2.0 - Governance Register.xlsx | 44 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-IFSCA-FCFU-v2.0 - IFSCA Finance Companies and Units.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-IFSCA-FME-v2.0 - IFSCA Fund Management Entities.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-IFSCA-GEN-v2.0 - IFSCA Regulated Entities.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-INTL-GEN-v2.0 - International Jurisdictions.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-IRDAI-INS-v2.0 - Insurers.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-IRDAI-INT-v2.0 - Insurance Intermediaries.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-LAB-POSH-v2.0 - Labour Codes and POSH.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-MCA-CO-v2.0 - Companies.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-MCA-LLP-v2.0 - LLPs.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-ARC-v2.0 - Asset Reconstruction Companies.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-NBFC-v2.0 - NBFCs.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-OTH-v2.0 - Other RBI Regulated Entities.xlsx | 62 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-RCB-v2.0 - Rural Co-operative Banks.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-SCB-v2.0 - Commercial Banks SFBs PBs LABs RRBs.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RBI-UCB-v2.0 - Urban Co-operative Banks.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-RISK-v2.0 - Risk Register.xlsx | 46 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-SEBI-AIF-v2.0 - Alternative Investment Funds.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-SEBI-INT-v2.0 - SEBI Intermediaries.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-SEBI-LISTED-v2.0 - Listed Entities.xlsx | 65 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-SEBI-MF-v2.0 - Mutual Funds.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-SEBI-REIT-INVIT-v2.0 - REITs and InvITs.xlsx | 63 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |
| LDC-TPL-TAX-GST-v2.0 - GST and Direct Tax.xlsx | 64 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | PASS |

## Sample export check (synthetic)

`samples/SAMPLE - Working Register Export - RBI-NBFC.xlsx` — 40 rows

| Check | Meaning | Result |
|---|---|---|
| X01 | Register headers equal the RBI-NBFC v2.0 contract | PASS |
| X02 | Every closed-list value valid; Function/Sub-function dependent on Department; Event Trigger present for Event Based / Immediately; issue ≤ actionable updated ≤ last amended | PASS |
| X03 | CompIDs match the platform grammar and are unique | PASS |
| X04 | Summary, grouped list, per-department sheets, Lists, Read Me, _Template_Info and _Export_Info present | PASS |
| X05 | RAG conditional formatting present | PASS |

## Legacy

The 27 v1.0 workbooks are kept in `templates/_legacy_v1.0/` for the legacy importer path (Appendix E §A.9). They are validated by the unchanged v1.0 validator (`templates/_validate_templates.py`); see `_legacy_v1.0/_validation_report_v1.0.md`.
