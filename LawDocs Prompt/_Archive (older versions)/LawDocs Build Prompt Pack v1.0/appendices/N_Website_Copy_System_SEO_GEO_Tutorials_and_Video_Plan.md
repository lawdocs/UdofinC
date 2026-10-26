# Appendix N — Website Copy System, SEO/GEO, Tutorials and Video Plan

> **Status:** Binding for P21 (public website, CMS, help centre) and P22 (store listings); binding for P16/P17 wherever they render public copy; reference for the Operations Hub marketing team (Appendix X).
> **Used by:** P21, P22, P15 (Consumer Help brand site), P16, P17, P06 (template one-liners and clause "i" text), P09 (Vidhi help-mode answer style).
> **Prepared:** 25 October 2026. Sources: R5 (primary: site inventory, manual analysis, voice, one-liners, templates, outdated-law and copied-content lists), R1 (competitor SEO weaknesses), R3 §11–§12 (accessibility, consumer protection, advertising), R4 §10–§11 (funnels and autopilot growth).
>
> **How to use.** This appendix is the content system: how LawDocs sounds, what each page type must contain, how pages link, how metadata and structured data are written, how the ≈626 manual-derived pages are migrated, and how tutorials and videos are produced and reused on social channels. P21 implements the CMS rules that enforce it. Every number, customer name, certification, comparison and "verified" statement must resolve to an approved claims-register entry (P21 FR-P21-45; NN-20). Placeholders in `{{double braces}}` are filled from platform registries, never typed by hand. Legal facts here carry the tags of the conventions ([LAW], [INTERP], [REC], [VERIFY]); a writer re-verifies each citation at publication. The flagship copy deck for about 15 pages (D-04) is maintained separately in `content/`; this appendix governs it.

---

## N.1 Voice, tone and style

### N.1.1 The voice in one sentence

**LawDocs talks like a sharp senior associate who is also good with puns: it says the legal point in three words, adds a human reason, and ends with an action** (R5 §6.1). Competitors sell trust and scale; LawDocs sells **wit, brevity and neutrality**, and pairs every line with one verifiable proof point.

### N.1.2 Traits — keep, fix, retire

| Trait | Example (owner's manuals) | Rule |
|---|---|---|
| Ultra-short, full-stop rhythm | "Team up." · "Take care." · "Pay. Save." · "File. Smile." | Keep. Signature style for eyebrows and CTAs. |
| Verb triads | "Execute. Intimate. Comply." · "Create. Maintain. Preserve." · "Agree. Accept. Acknowledge." | Keep; never repeat a triad on two pages. |
| Puns and double meanings | "Cheque. Check. Checkmate." · "Trade a Mark. Trade with Mark." · "Raise a bar." · "Lease with ease." | Keep; strongest lines. Never in sensitive categories (N.1.4). |
| Law plus human value | "Gift with Love and Law." · "Write your family story, in legal language." · "Seniority at priority." | Keep for personal categories. |
| "…, legally." kicker | "Maintain your life, legally." · "Bounce back. Legally." | Use on at most 1 in 20 pages. |
| Neutrality promise | "Neutral drafts. Equal favour." | Brand pillar "Neutral by design. Fair by default." |
| CTA formula | "[Verb] [object], now." ("Draft it, now.") | Keep; standardise the comma. |
| Humour with edge | "Get out of the trouble. Or say it, 'Get out'." · "Fold your business and double the money." | Retire both: the first is unsafe in divorce pages; "fold" means *close down*. |
| Borrowed lines | "Conflict is inevitable, but combat is optional." · "Competition makes us faster, collaboration makes us better." · "Win the workplace to win the marketplace." · "do or do not, there is no try" | Retire (originality and attribution risk). |
| Grammar slips | "Sale the Goods." · "Equal Favours." · "Reach to the consumers" · "collaboration makes as better" · "Add salt to your business" | Fix (N.2.2). |

### N.1.3 Style rules (all public copy)

1. **Second person, active voice, present tense.** "You can eSign this agreement" — not "The agreement may be executed electronically by the parties".
2. **Plain Indian English**, British spelling (organisation, licence, authorise). Reading grade: ≤ 8 for consumer pages, help and glossary plain definitions; ≤ 10 for business pages; ≤ 12 for regulated-entity pages.
3. **One idea per sentence; ≤ 4 sentences per paragraph; ≤ 25 words per sentence** (warning above 30).
4. **Define on first use.** Every acronym is expanded once and linked to its "i" term (`<abbr>` + glossary link).
5. **Lead with the answer.** The first sentence under each heading answers the heading.
6. **Numbers:** Indian digit grouping (₹1,49,999), lakh and crore for large sums (₹50 lakh; ₹2.5 crore), no decimals on whole rupees; dates "12 March 2026"; time "10:30 am IST".
7. **Fees:** always split professional fee, LawDocs platform fee, government fee or stamp duty "at actuals", and GST; never "starting at" without the full breakdown link (R1 finding 5; NN-22).
8. **Law:** cite the instrument and provision ("Registration Act 1908, s.17"); new criminal laws with the former provision in brackets ("Section 482 BNSS (formerly Section 438 CrPC)"); Income-tax Act 2025 dual-cited with the 1961 Act during transition [VERIFY new section numbers].
9. **No legal advice voice.** Write "Generally, …", "In most States, …", "Ask a professional if …"; never "You will win", "This guarantees", "Fully legal".
10. **Inclusive language:** gender-neutral party labels ("the tenant", "they"); no assumptions about religion or family structure; personal-law variants presented neutrally.
11. **Accessibility in copy:** meaningful link text ("Read the stamp-duty table for Karnataka", not "Click here"); no instructions that rely on colour, shape or position alone ("the green button"); alternatives for every image of text.

### N.1.4 Sensitive categories (tone overrides)

Applies to divorce, child custody, domestic violence, maintenance, criminal matters, succession after a death, debt distress, insurance claim rejection, senior citizens' protection, and all Consumer Help pages.

- No puns, humour or "now" urgency in the H1, eyebrow or CTA; calm, factual lines ("The child first. Always." is acceptable; "Get out" is not).
- Safety first: domestic-violence pages show emergency and helpline information at the top (Women Helpline 181, Police 112 [VERIFY numbers at publication]) and a quick-exit control that clears the page; no retargeting pixels (P21 FR-P21-105).
- Do not promise outcomes, waivers or settlements (NN-23); state the forum's rules (e.g., the RBI Ombudsman route requires a complaint to the regulated entity first [VERIFY RB-IOS 2026 clause]).

### N.1.5 Prohibited words and claims (claims gate blocks them)

"best", "No. 1", "India's leading" (unless a claims-register metric supports it), "guaranteed", "100% legal", "fully compliant", "government-approved", "RBI-approved", "court-approved format", "verified lawyers" (unless the verification record and approved wording exist), "real-time court status", "live tracking" (court and trademark data), "AI lawyer", "replace your lawyer" (D-17, CH-14), "certified" (before a certificate is held), fake scarcity ("only 2 slots left") and any countdown not bound to a real event (NN-50).

### N.1.6 Consumer Help brand voice

Calmer and shorter; no puns; reassurance through process ("Step 1: complain to your lender. Step 2: wait 30 days. Step 3: …"); every page states that users pay fines and dues on official portals and that the brand does not collect them (NN-23).

---

## N.2 One-liner bank

### N.2.1 Use rules

- One approved line per page as the **eyebrow** above the H1 (never the H1); optional CTA line in the "[Verb] [object], now." formula.
- A line is used on one canonical page only (exceptions: brand pillars on home, about and footer).
- Lines are data in `web.one_liners` with status KEEP / FIXED / NEW / RETIRED, page binding and approver. The CMS blocks RETIRED lines.

### N.2.2 Owner's originals (selected; status after review)

| Line (as in manual) | Status | Published form | Page |
|---|---|---|---|
| Team up. | KEEP | Team up. | Collaboration and joint venture |
| Neutral drafts. Equal Favours. | FIXED | Neutral drafts. Equal favour. | Brand pillar / Collaboration |
| Take care. | KEEP | Take care. | Contracts and agreements |
| Created in minutes. Approved in seconds. | KEEP (once) | Created in minutes. Approved in seconds. | Distributorship and agencies |
| Create with ease, terminate with peace. | KEEP | Create with ease. Terminate with peace. | Franchise and licence |
| Calculate. Integrate. Regulate. | KEEP | Calculate. Integrate. Regulate. | Mergers and acquisitions |
| Fold your business and double the money. | RETIRED | — | — |
| Cheque. Check. Checkmate. | KEEP | Cheque. Check. Checkmate. | Dishonour of cheque notice |
| Trade a Mark. Trade with Mark. | KEEP | Trade a mark. Trade with a mark. | Trademark assignment / licence |
| Gift with Love and Law. | KEEP | Gift with love. And law. | Gift deed hub |
| Write your family story, in legal language. | KEEP | Write your family story, in legal language. | Family matters hub |
| Seniority at priority. | KEEP | Seniority at priority. | Senior citizens |
| Divide with Rules. | KEEP | Divide by the rules. | Partition |
| Get out of the trouble. Or say it, 'Get out'. | RETIRED | — | — |
| Take the custody, yourself. | FIXED | The child first. Always. (new line #23) | Child custody |
| Raise your voice through writing. | KEEP | Raise your voice. In writing. | Domestic violence (no CTA urgency) |
| Rent happiness. | KEEP | Rent happiness. | Paying-guest agreement |
| Lease with ease. | KEEP | Lease with ease. | Lease hub |
| Bounce back. Legally. | KEEP | Bounce back. Legally. | Cheque-bounce pleadings hub |
| Get the Trust. / Get trusted | KEEP (one each) | Get trusted. | Trust registration |
| Host the guest. | KEEP | Host the guest. | FSSAI |
| Cross the border. | KEEP | Cross the border. | IEC |
| Raise a bar. | KEEP | Raise the bar. | Barcode registration |
| Add salt to your business | FIXED | Spice up your exports. | Spices Board registration |
| Execute. Intimate. Comply. | KEEP | Execute. Intimate. Comply. | Corporate compliances |
| Take care, it's an annual affair. | KEEP | Take care. It's an annual affair. | Annual filings |
| Chase dreams with Private Limited Company. | FIXED | Chase dreams. Limit liability. | Pvt Ltd registration |
| Get a business face. | KEEP | Get a business face. | OPC |
| Run the one man show. | FIXED | Run the one-person show. | Sole proprietorship |
| Multiply power. | KEEP | Multiply power. | Partnership firm |
| Dream unlimited with limited risks. | KEEP | Dream unlimited. Risk limited. | LLP |
| Get a company of money, for money. | KEEP | A company of money, for money. | Nidhi company |
| Register your copy, create a right. | KEEP | Register your copy. Create a right. | Copyright |
| Get GI. Get pride. | KEEP | Get GI. Get pride. | Geographical indications |
| Pay. Save. | KEEP | Pay. Save. | Taxation hub |
| Close. Lock. Forget. | FIXED | Close it. Cleanly. | Closure of business |
| Conflict is inevitable, but combat is optional. | RETIRED | Talk it out. Sign it off. (#57) | Mediation |
| Competition makes us faster, collaboration makes us better. | RETIRED | Two logos. One rulebook. (#18) | JV |
| Sale the Goods. | FIXED | Sell the goods. Keep the proof. | Sale of goods |
| Sign of the Deal, now. | FIXED | Sign off the deal, now. | Sign-off hub |

The full owner inventory (131 Documents one-liners and 48 service one-liners) is in R5 §8; each is triaged into this table during migration (N.9).

### N.2.3 New one-liner bank (R5 §6.2, 82 lines, original; approved for use)

| # | Page | Line | # | Page | Line |
|---|---|---|---|---|---|
| 1 | Home hero | Draft it. Sign it. Keep it. | 42 | Trademark registration | Your brand. Nobody else's. |
| 2 | Home sub | Your agreements, in your pocket. For life. | 43 | Trademark tracker | Filed. Tracked. Registered. |
| 3 | Pillar | Neutral by design. Fair by default. | 44 | Patent | Invent once. Earn often. |
| 4 | Pillar | Paperwork, minus the paper. | 45 | IT and websites | Code ships. Contracts protect. |
| 5 | Aadhaar eSign | One OTP. One binding deal. | 46 | Website policies | Collect data. Not liability. |
| 6 | eSign | Signed in seconds. Valid for years. | 47 | Cookie/privacy | Consent, clearly. |
| 7 | Vidhi AI | Ask Vidhi. Then decide. | 48 | HR and service | Hire on paper. Part by the book. |
| 8 | Vidhi AI | First draft free. Final word yours. | 49 | Offer letters | Offer clearly. Retain gladly. |
| 9 | Vidhi AI | Speak your terms. Vidhi writes them. | 50 | Labour agreements | Fair wage. Firm terms. |
| 10 | Vidhi + expert | AI drafts. Experts check. You sign. | 51 | Work from home | Remote work. Real terms. |
| 11 | Hire a professional | Expert eyes. Fixed price. | 52 | Legal notices | Say it once. Say it in a notice. |
| 12 | Hire a professional | A lawyer when it matters. Not before. | 53 | Reply to notice | Answer back. On record. |
| 13 | Vault | Store once. Find forever. | 54 | Affidavits | Swear by it. Properly. |
| 14 | Vault | Every deed, one drawer. | 55 | RTI | Ask the State. In writing. |
| 15 | Data export | Leave anytime. Take everything. | 56 | Consumer | Paid for it? Claim for it. |
| 16 | Deals and agreements | Deal fair. Draft fairer. | 57 | Mediation and ODR (Equator shown with other providers, disclosed) | Talk it out. Sign it off. |
| 17 | Contracts | Terms first. Trust follows. | 58 | Arbitration | Private forum. Binding award. |
| 18 | Collaboration/JV | Two logos. One rulebook. | 59 | Property hub | Own the land. Own the papers. |
| 19 | Statement of work | Scope it. Then ship it. | 60 | Building contracts | Brick by brick. Clause by clause. |
| 20 | Family matters | Settle hearts. Then settle papers. | 61 | Rent | Rent right. Live light. |
| 21 | Marriage | Two families. One record. | 62 | Sale and purchase | Buy the house. Not the dispute. |
| 22 | Divorce (mutual) | Part ways. Keep the peace. | 63 | RERA buyers | Booked a flat? Book your rights. |
| 23 | Child custody | The child first. Always. | 64 | RERA builders | Register first. Sell faster. |
| 24 | Senior citizens | Respect, with remedies. | 65 | Secretarial | Minutes that matter. |
| 25 | Financial transactions | Money talks. Paper proves. | 66 | Resolutions | Resolve. Record. Report. |
| 26 | Loans/bonds | Lend with proof. Borrow with clarity. | 67 | NBFC/RBI compliance | RBI-ready, every quarter. |
| 27 | Receipts | Every rupee, on record. | 68 | Students | Paperwork done. Back to books. |
| 28 | Guarantee/indemnity | Promise the risk. Price the risk. | 69 | Succession hub | Pass the legacy, not the litigation. |
| 29 | Hire-purchase | Use it now. Own it later. | 70 | Will | Your wishes. Your words. Your Will. |
| 30 | Operations and management | Run the firm by the book. Literally. | 71 | Power of attorney | Hand over power. Not control. |
| 31 | Companies | Board-ready. Auditor-ready. | 72 | Pleadings hub | Your case, in the court's language. |
| 32 | Partnership | Shake hands. Then sign hands. | 73 | Criminal pleadings | Liberty deserves good drafting. |
| 33 | Trusts | Give with purpose. Govern with rules. | 74 | Civil suits | Plead it right the first time. |
| 34 | Planning/start-up | Idea today. Entity tomorrow. | 75 | Compliance hub | Comply quietly. Grow loudly. |
| 35 | Founders | Founders agree first. Investors follow. | 76 | Compliance calendar | Due dates, never overdue. |
| 36 | Funding | Raise money. Not disputes. | 77 | GST/tax | File on time. Sleep on time. |
| 37 | Marketing and sales | Promise in ads. Prove in contracts. | 78 | Closure | Close the books. Close the chapter. |
| 38 | Invoices | Bill right. Get paid. | 79 | Start a business | Register today. Rule tomorrow. |
| 39 | Industries | Your industry. Your clauses. | 80 | Licences/marks | Licensed to grow. Certified to be trusted. |
| 40 | IPR hub | Own the idea. Officially. | 81 | NGO/Section 8 | Do good. Register well. |
| 41 | Copyright | Create. Register. Royalty. | 82 | Litigation tracker | Every hearing, on your radar. |

**New verticals:** Marketplace "Pick a pro. Pay per job." · Retainership "A legal team on retainer. Not on payroll." · FinLegal Academy "Practise before you practise." · Loan/insurance grievances "Rejected? Not the final word." · Challans "Check the challan. Pay it officially." (replaces R5's "Challan today. Cleared today.", which implies an outcome — NN-23) · Vehicle sale "Sell the car. Keep the proof." · Savings page "Hours saved. Penalties avoided. Counted." (shown only with NN-36 evidence classes).

**Lines to verify before use:** #6 "Valid for years" — use only on eSign-eligible pages; #67 "RBI-ready, every quarter" — must not imply RBI approval (claims gate checks context); #12 "A lawyer when it matters" — the CTA leads to a LawDocs service, never to a named advocate (NN-21).

---

## N.3 Page-copy templates, minimum content and editorial checklist

Word counts are for original body copy and exclude navigation, FAQs, tables generated from data and the footer. Block order is defined in P21 §4C; this table sets the copy rules.

| Page type | H1 pattern | Summary answer | Body minimum | FAQs | Other copy rules |
|---|---|---|---|---|---|
| Home | "Draft, sign and keep every agreement — with Vidhi AI and real professionals" (≤ 70 chars) | 30–40 words | 500 | 6 | Issue tiles in plain questions; three proof points from claims register; no stats without claims |
| Section landing | "[Section] — [what you can do]" ("Legal Documents — Draft Free, eSign Online") | 40–60 | 300 | 5 | Category grid one-liners + 15-word descriptions |
| Category hub | "[Category] Documents & Agreements" | 60–80 (definition) | 250 | 4–6 | "Most used" list from metric, never paid |
| Sub-category hub | "[Sub-category]: Agreements, Notices and Formats" | 40–60 | 150–300 explainer | 4–6 | "Use this when…" line ≤ 15 words per document |
| Document page | "[Document] — Draft Free, eSign Online" / "— Draft Free, Print and Register" | 40–60 | 400 | 5–8 | Clause list 8–15 bullets ≤ 20 words; requirements table; ordered process; State table with source + verified-on |
| Pleading page | "[Pleading] under Section [x] [Act] (formerly Section [y] [old Act])" | 40–60 | 450 | 5–8 | Annexure checklist; savings-clause note; "File through an advocate" |
| Service page | "[Service] Online — [outcome/timeline]" | 40–60 | 400 | 6–10 | Price card from catalogue; documents required; process; comparison where relevant |
| Regulated-entity service | "[Regulator] [Service] for [entity type]" | 40–60 | 500 | 6–10 | Cite master direction/regulation with para; "Law as of"; reviewer CS/advocate |
| Comparison page | "[A] vs [B]: Which One Do You Need?" | 40–60 | 500 | 4–6 | Table with citation per legal row; "If you…, choose…" list |
| Glossary term | "[Term] — Meaning in Law and in LawDocs" | plain definition ≤ 40 | 120–250 | 0–3 | Quoted legal definition with citation |
| State variant | "[Document] in [State] — Stamp Duty, Registration and Format" | 40–60 | 250 State-specific | 3–5 | Only if ≥ 3 material facts (P21 FR-P21-27) |
| Blog post | Question or claim headline ≤ 65 chars | 40–60 | 800 (guide 1,200) | 3–5 | Author + reviewer; dated updates; "Related documents" |
| Video page | "[Topic] — [format] (x min)" | 40–60 | 150 + transcript | 0–3 | Chapters; transcript; ISL link where produced |
| Tool page | "[Tool] — Free Calculator" | 30–50 | 200 (method + limits) | 3–5 | Inputs, formula, sources, "not legal advice" |
| Landing page | Audience + job ("For landlords: a registered rent agreement without visiting a lawyer's office") | 25–40 | 250 | 3–5 | One primary CTA; real dates; no fake urgency |
| Legal policy | Policy name | — | as Appendix O | — | Version, effective date, change summary |
| Help article | Task as verb phrase ("Send a document for eSign") | 1–2 sentences | 150–600 | — | Numbered steps; one screenshot per 2–3 steps; "i" links |

**Editorial checklist (CMS-enforced where marked ●)**

1. ● One H1; headings in order; title ≤ 60, description ≤ 155, both unique.
2. ● Summary answer present (what it is + which law + who uses it).
3. ● Body meets the minimum; no placeholder text ("Educate on what is ?").
4. ● Every legal citation structured and resolved; superseded law mapped (N.8, N.9.3).
5. ● Plagiarism ≤ threshold; no competitor brands or links (N.9.2).
6. ● Every number, logo, certification, comparison bound to a claims entry.
7. ● Fees only from the catalogue; split lines; GST stated.
8. ● eSign badge from Appendix F; wording matches the badge.
9. ● Alt text on informative images; tables with headers; link text meaningful.
10. ● Reviewer of record set for legal types; next review date set.
11. ○ Reading grade within target (warning).
12. ○ One-liner bound and not reused.
13. ○ 4–6 related links; hub link; one guide; one video where available (N.6).
14. ○ FAQs from real question sources; each answer ≤ 60 words.
15. ○ Sensitive-category overrides applied (N.1.4).

### N.3.1 Worked example — residential rent agreement (copy skeleton)

- **Eyebrow:** Rent right. Live light.
- **H1:** Residential Rent Agreement — Draft Free, eSign Online
- **Summary answer (52 words):** "A residential rent agreement is a contract in which a landlord lets a home to a tenant for rent, governed by the Transfer of Property Act 1882 (s.105) and your State's rent law. Agreements for more than 11 months generally need stamping and registration under the Registration Act 1908 (s.17) [VERIFY State practice]."
- **Key facts:** Governing law · Stamp duty: by State (table below) · Registration: required for leases of a year or more; commonly done for 11-month agreements only by choice [INTERP; VERIFY per State] · Witnesses: two recommended · eSign: **Check** — eSign is valid for the agreement, but stamping and any registration still apply · Typical time: 15 minutes to draft · Law as of {{facts.verified_on}}.
- **Drafter intro:** "Answer seven questions. Vidhi fills a vetted template. Free to draft; pay only to stamp, sign or remove the watermark."
- **Hire block intro:** "Want a professional to check it? Fixed price. Delivered by a LawDocs-assigned professional."
- **Clause bullets (examples):** Rent and due date — when and how rent is paid · Security deposit — amount and refund timeline · Lock-in — minimum period before either side can exit · Escalation — yearly increase, if any · Maintenance — who pays for what · Notice — how either party ends the agreement.
- **FAQ examples:** "Is an online rent agreement valid?" · "Do I need to register an 11-month rent agreement?" · "Who pays stamp duty, landlord or tenant?" · "Can I eSign a rent agreement with Aadhaar?" · "What happens if a rent agreement is not stamped?" (answer: inadmissible in evidence until duty and penalty are paid — Indian Stamp Act 1899, s.35 or the State equivalent [VERIFY State Act]).

---

## N.4 FAQ writing rules

1. **Source real questions:** Search Console queries, People Also Ask, de-identified Vidhi chat clusters (aggregated, k ≥ 30), support tickets, sales calls. Never invent questions to stuff keywords.
2. **Format:** question as the user asks it (≤ 12 words, sentence case, question mark); answer **≤ 60 words**, first sentence answers yes/no/what; second sentence gives the condition or exception; cite the provision when legal; link to the canonical page or tool.
3. **Visible HTML only:** FAQs are on the page in the server HTML; `FAQPage` JSON-LD only mirrors visible Q&A (P21 FR-P21-49). No hidden or tab-only FAQs.
4. **No duplication:** one canonical answer per question across the site; other pages link to it.
5. **No advice:** general information wording; "Ask a professional if …" for fact-specific issues.
6. **Freshness:** each FAQ bound to the rules items it relies on; a law change flags it.
7. **Locale:** translated FAQs are reviewed like body copy (NN-48).
8. **Remove manual FAQs** that name competitors (R5 §4 rows 2, 5, 7, 8), restate Wikipedia, or cite superseded law without mapping.

---

## N.5 Keyword and intent clusters

Seed clusters per category. Refresh quarterly from Search Console, Bing Webmaster and the AI-answer panel (N.8.3). "Intent": I = informational, T = transactional (draft/buy), N = navigational, L = local. Hindi variants are listed for the top clusters; other D-07 languages follow the same pattern after review.

| Cluster | Head terms | Modifiers | Intent | Canonical target | Sample questions |
|---|---|---|---|---|---|
| Rent and lease | rent agreement, rental agreement, leave and licence, lease deed; किराया अनुबंध, रेंट एग्रीमेंट | online, format, 11 months, stamp duty, registration, PDF, [State] | T, I | `/documents/property-transactions/rent/rent-agreement-residential` | Is an online rent agreement valid? 11 months or 12? |
| Property sale | agreement to sell, sale agreement flat, sale deed format | stamp duty, registration, eSign valid? | I, T | `/documents/property-transactions/sale-and-purchase/agreement-for-sale-of-flat` | Can I eSign a sale agreement? (No — IT Act First Schedule) |
| Gift and succession | gift deed, will format, simple will, probate; वसीयत | immovable, family, stamp duty, registration | I, T | gift deed hub; `/documents/succession-and-inheritance/will/simple-will` | Does a will need registration? Can a will be eSigned? |
| Power of attorney | general power of attorney, special POA | format, registration, revoke | T | `/documents/succession-and-inheritance/power-of-attorney/general-power-of-attorney` | Can a POA be signed online? |
| Business contracts | NDA, service agreement, vendor agreement, consultancy agreement | format, India, online, free | T | contracts and agreements hub | What makes an NDA enforceable in India? |
| Startup founders | founders agreement, shareholders agreement, ESOP, term sheet | template, vesting, India | T, I | `/startups` + founder documents | When should founders sign an agreement? |
| Employment | offer letter, employment agreement, appointment letter, relieving letter | format, notice period, Labour Codes | T | HR and service hub | Is a notice-period clause enforceable? |
| Notices | legal notice format, cheque bounce notice, reply to legal notice | 15 days, s.138, recovery, rent arrears | T | legal notices hub | How many days for a cheque bounce notice? |
| Cheque bounce | section 138 complaint, cheque bounce case | limitation, court, procedure | I, T | `/pleadings/cheque-bounce-matters/complaint-under-section-138` | What is the time limit to file a s.138 complaint? |
| Bail | anticipatory bail, regular bail; अग्रिम जमानत | BNSS 482, 480, 483, format | I, T | criminal pleadings hub | What is BNSS 482? (formerly CrPC 438) |
| Family pleadings | mutual consent divorce, maintenance petition, child custody | BNSS 144, cooling-off waiver, format | I, T | family pleadings hub | Can the six-month period be waived? |
| Consumer | consumer complaint, District Commission, e-Daakhil | CPA 2019, limits, format | I, T | `/pleadings/consumer-law/consumer-complaint-cpa-2019` | Which commission hears my complaint? |
| Civil suits | money recovery suit, summary suit, injunction, written statement | Order XXXVII, s.12A mediation | I, T | civil pleadings hub | Is pre-litigation mediation mandatory? |
| Company registration | private limited company registration, LLP, OPC | cost, documents, time, SPICe+ | T | Start a Business service pages | Pvt Ltd vs LLP — which is better? |
| IP | trademark registration, trademark objection reply, copyright registration | class, fee, status, TM-A | T, I | IP services + trademark tracker | How long does trademark registration take? |
| Registrations | GST registration, Udyam/MSME, FSSAI, IEC | online, documents, fee, renewal | T | registration service pages | Is Udyam the same as Udyog Aadhaar? (Replaced) |
| Tax and returns | ITR filing, TDS return, GST return | due date, tax year, Income-tax Act 2025 | T, I | compliance taxation hub | What is a "tax year" under the 2025 Act? |
| ROC compliance | annual filing, AOC-4, MGT-7, DIR-3 KYC | due date, penalty | T, I | ROC hub | What is the penalty for late annual filing? |
| Regulated entities | NBFC compliance, RBI returns, SEBI LODR, IRDAI | master direction, policy, return | T, I | `/regulated-entities/*` (cross-link LawDocsComply) | Which RBI returns does a base-layer NBFC file? |
| eSign and eStamp | Aadhaar eSign, e-stamp paper online, stamp duty calculator | valid, State, cost | I, T | `/esign`, `/estamp`, stamp-duty tool | Is Aadhaar eSign legally valid? |
| Vault | digital document locker, store legal documents | secure, India, export | I, N | `/legal-vault` | Is it like DigiLocker? (Different — explain, CH-15) |
| Litigation tracker | case status, CNR number, hearing date | track, alerts | I, N | `/litigation-tracker` | How do I find my CNR number? |
| Consumer Help (brand host) | loan complaint, RBI ombudsman complaint, insurance claim rejected, challan check | how to, time limit, documents | I, T | brand site hubs | Can I complain to the RBI Ombudsman directly? |
| Vehicle | car sale agreement, delivery note, RC transfer | format, Vahan, challan | T, I | `/documents/financial-transactions/sale-of-goods/agreement-for-sale-of-car` | Does the agreement transfer the RC? (No — Vahan, CH-23) |

**Cluster rules:** one canonical page per primary intent; secondary intents become H2 sections or FAQs on that page, not new URLs; State or city modifiers stay as table rows unless the materiality test passes (P21 FR-P21-27); keyword lists live in `web.keyword_clusters` and are linked to pages in the CMS.

**Competitor gaps to exploit (R1 §3.6):** LegalKart's programmatic `find-{practice}-lawyer-in-{city}` pages are thin and mismatched, show no JSON-LD, leave FAQs unanswered and display zero counters. LawDocs wins with fewer, deeper pages; answered FAQs; valid schema; named reviewers; "law as of" dates; original State matrices and old→new law maps.

---

## N.6 Internal-linking model (hub and spoke)

| Link | Rule |
|---|---|
| Leaf → hub | Breadcrumb plus one in-body link to the immediate hub. |
| Hub → leaves | Every leaf listed with a "use this when…" line. |
| Leaf ↔ leaf | 4–6 related leaves in the same or adjacent hub (e.g., rent agreement ↔ leave and licence ↔ notice to tenant ↔ rent receipt). |
| Cross-section bridge | Document ↔ pleading ↔ service for the same life event (rent agreement → eviction suit → registration assistance; cheque bounce notice → s.138 complaint → litigation tracker). Maintained in `web.bridges`. |
| Content → product | Each leaf links the product page for the action it promotes (eSign, eStamp, vault, tracker) once. |
| Blog/video → canonical | Every post links at least one canonical leaf in the first 150 words and the "Related documents" block. Posts never compete with leaves for the same primary intent. |
| Glossary | First use of a defined term on a page links to its glossary page (once per page). |
| Anchor text | Descriptive, varied, matches the target's intent; no exact-match stuffing; no "click here". |
| Limits | ≤ 100 in-body links per page; no sitewide footer links to individual leaves beyond section hubs. |
| Orphans | No published leaf may have zero inbound links (P21 FR-P21-19). |

---

## N.7 Metadata rules

| Element | Rule | Example |
|---|---|---|
| Title | ≤ 60 chars; `[Primary intent] — [qualifier] | LawDocs`; unique | `Rent Agreement Online — Draft Free & eSign | LawDocs` |
| Meta description | ≤ 155 chars; answer + action; unique | "Draft a residential rent agreement free in 7 questions. See State stamp duty, eSign with Aadhaar and store it in your Legal Vault." |
| Slug | lower-case, hyphens, ≤ 6 words, no stop-word sentences, typos fixed | `rent-agreement-residential` |
| H1 | One; matches the template pattern; may differ from title | — |
| OG title/description | Same as title/description unless social copy is approved | — |
| OG image | Generated: title + one-liner on brand tokens; 1200 × 630; alt text | — |
| Canonical | Self, absolute, `https://www.lawdocs.in/...` | — |
| hreflang | Only reviewed locales + `x-default` | — |
| `dateModified` | Substantive changes only | — |
| Image alt | Describe purpose ("Sample first page of a rent agreement with clause numbers"); decorative = empty alt | — |
| File names | `rent-agreement-sample-page-1.webp` | — |

---

## N.8 Citation, review and AI-answer monitoring

### N.8.1 Citation rules

1. Cite the **primary source**: India Code (Acts), Gazette (rules/notifications), the regulator (RBI, SEBI, IRDAI, MCA, CBIC, CBDT, IP India, CCA), e-Courts and court websites (judgments). Secondary sources only to explain, never as the legal basis.
2. Citation format: `[Act] [year], s.[n]` · `[Rules] [year], r.[n]` · `[Regulator] [instrument] dated [date], para [n]` · case: `[Party] v [Party] ([Court], [date])` with a neutral citation where available.
3. Every citation is a structured reference resolved against `rul` or a URL with "verified on" (P21 FR-P21-60). Unresolved → "unverified" and blocks legal page types.
4. Judgments: cite only judgments retrieved and read by the reviewer; no case law from AI output without retrieval (NN-14).
5. Quoting statutes is allowed (government works; attribute); quoting commentary is limited to short attributed quotes.

### N.8.2 Review rules

| Page type | Reviewer of record | Review cycle |
|---|---|---|
| Document, property, family, succession | Advocate (`PLT_LEGAL_REVIEWER`) | 365 days, or on law change |
| Pleading | Advocate with litigation practice | 180 days |
| Company, startup, ROC, secretarial | Company Secretary | 180 days |
| Tax, GST, accounting | Chartered Accountant or tax practitioner | 180 days; on Budget/Finance Act |
| Regulated entities (RBI/SEBI/IRDAI) | CS or advocate with regulatory practice | 120 days; on master-direction change |
| Labour and HR | Advocate or CS with labour practice | 180 days; on Code rule notification |
| Consumer Help | Advocate (content only; the brand's non-advocate case managers do not review legal text) | 180 days |
| Blog (legal) | As per subject | 365 days |
| Glossary legal definitions | Advocate or CS | With the linked rule |

Reviewers' public profiles follow BCI Rule 36 (advocates) and ICAI/ICSI guidance (CA/CS) [VERIFY]; enrolment or membership numbers appear only with the reviewer's consent.

### N.8.3 AI-answer monitoring panel (run monthly; P21 FR-P21-70)

30 fixed prompts across engines (Google AI Overviews/AI Mode, ChatGPT search, Perplexity, Copilot, Claude). Log: cited (Y/N, URL), accuracy of the statement about LawDocs or the law, competitor cited. Seed prompts:

1. Is an online rent agreement valid in India? 2. How do I make a rent agreement online in [Delhi/Bengaluru/Mumbai]? 3. Can I eSign a property sale agreement with Aadhaar? 4. Can a will be signed electronically in India? 5. What is the stamp duty on a rent agreement in Karnataka? 6. Best way to draft an NDA for a startup in India. 7. How to send a cheque bounce legal notice. 8. What is BNSS Section 482? 9. Format of an anticipatory bail application. 10. How to file a consumer complaint online in India. 11. Private limited company vs LLP for a startup. 12. Documents needed for trademark registration. 13. How to reply to a trademark objection. 14. Is Udyam registration the same as Udyog Aadhaar? 15. What is a tax year under the Income-tax Act 2025? 16. How to track a court case with a CNR number. 17. Which app stores legal documents securely in India? 18. What is LawDocs? 19. What is Vidhi AI? 20. Is LawDocs a law firm? 21. How do I complain to the RBI Ombudsman about a loan? 22. What can I do if my health insurance claim is rejected? 23. How to check a traffic challan online. 24. How to write a car sale agreement in India. 25. What does a section 63 BSA certificate contain? 26. Do I need to register an 11-month rent agreement? 27. What is a leave and licence agreement? 28. Founders agreement checklist India. 29. How to close a private limited company. 30. NBFC compliance calendar for base layer.

Prompts 18–20 verify entity accuracy (N.14 entity registry); inaccuracies become content tasks (e.g., an About page FAQ "Is LawDocs a law firm? No — LawDocs is a legal technology and services platform; legal advice is given by independent professionals engaged through it" — D-17, NN-41).

---

## N.9 Content-migration plan for the ≈626 manual-derived pages

### N.9.1 Inventory and waves

| Wave (P21) | Scope | Pages | Throughput assumption |
|---|---|---|---|
| Wave 1 | Top 50 content pages (below) + their 18 hubs needed for breadcrumbs (hub copy minimal but above minimum) | ≈ 70 | 4 writers × 4 sprints ≈ 4–5 pages per writer per week including review |
| Wave 2 | Remaining Documents sub-hubs with body copy (86) and their template lists (71 hubs), all 48 service pages, the 68 canonical pleadings | ≈ 300 | Content agent drafts + human rewrite; 2 reviewers |
| Wave 3 | The 63 sub-hubs with undefined document lists (define documents first), remaining document leaves, regulated-entity pages (≈ 50), advisory (6), State variants that pass the materiality test | ≈ 300 | — |
| Hold | 48 stubs and "(upcoming)" placeholders (D7 Industries, D14 SEBI, D15 Secretarial, D18 Accounting & Tax and similar) | — | Not published until content exists (no thin pages) |

**Wave 1 — top 50 content pages**

| # | Page | URL (canonical) | eSign badge (Appendix F governs) |
|---|---|---|---|
| 1 | Residential rent agreement | `/documents/property-transactions/rent/rent-agreement-residential` | Check |
| 2 | Commercial rent agreement | `/documents/property-transactions/rent/rent-agreement-commercial` | Check |
| 3 | Leave and licence agreement (canonical moved to Rent — R5 §3.1) | `/documents/property-transactions/rent/leave-and-licence-agreement` | Check |
| 4 | Paying-guest agreement | `/documents/property-transactions/rent/agreement-for-paying-guest` | Check |
| 5 | Notice to the tenant | `/documents/property-transactions/rent/notice-to-the-tenant` | Check |
| 6 | Lease deed of residential property | `/documents/property-transactions/lease/lease-deed-of-residential-property` | Check |
| 7 | Agreement for sale of flat | `/documents/property-transactions/sale-and-purchase/agreement-for-sale-of-flat` | Not valid |
| 8 | Simple gift deed | `/documents/succession-and-inheritance/gift-deed/simple-gift-deed` | Check |
| 9 | Simple will | `/documents/succession-and-inheritance/will/simple-will` | Not valid |
| 10 | General power of attorney | `/documents/succession-and-inheritance/power-of-attorney/general-power-of-attorney` | Not valid |
| 11 | Confidentiality and non-disclosure agreement | `/documents/deals-and-agreements/contracts-and-agreements/confidentiality-and-non-disclosure-agreement` | Valid |
| 12 | Employment agreement | `/documents/hr-and-service/job-agreements/employment-agreement` | Valid |
| 13 | Offer letter | `/documents/hr-and-service/job-application-and-offers/offer-letter` | Valid |
| 14 | Founders' agreement (canonical in funding hub — R5 §3.1) | `/documents/planning-and-execution/investment-support-and-business-funding/founders-agreement` | Valid |
| 15 | Partnership deed | `/documents/planning-and-execution/partnership-and-founders/partnership-deed` | Valid |
| 16 | Shareholders' agreement | `/documents/operations-and-management/companies/shareholders-agreement` | Valid |
| 17 | Website development agreement | `/documents/it-and-websites/it-and-net-related-contracts/agreement-for-development-of-website` | Valid |
| 18 | Agreement for sale of car | `/documents/financial-transactions/sale-of-goods/agreement-for-sale-of-car` | Valid |
| 19 | Rent receipt | `/documents/financial-transactions/receipts/rent-receipt` | Valid |
| 20 | Promissory note for payment | `/documents/financial-transactions/promissory-note/promissory-note-for-payment` | Not valid |
| 21 | Cheque bounce legal notice | `/documents/legal/legal-notices/dishonour-of-cheque-notice` | Valid |
| 22 | Notice for making payment | `/documents/legal/legal-notices/notice-for-making-payment` | Valid |
| 23 | Consumer protection legal notice | `/documents/legal/legal-notices/consumer-protection-notice` | Valid |
| 24 | Reply to a legal notice | `/documents/legal/reply-to-legal-notices/reply-to-the-legal-notice` | Valid |
| 25 | Affidavit for loss of marksheet or certificate | `/documents/students/affidavits-for-students/loss-of-marksheet-or-certificate` | See note (affidavits) |
| 26 | Anticipatory bail application (BNSS s.482) | `/pleadings/criminal-law-pleadings/anticipatory-bail-application` | n/a (court filing) |
| 27 | Regular bail application (BNSS s.480/483) | `/pleadings/criminal-law-pleadings/regular-bail-application` | n/a |
| 28 | Mutual consent divorce petition | `/pleadings/family-law-pleadings/mutual-consent-divorce-petition` | n/a |
| 29 | Maintenance application (BNSS s.144) | `/pleadings/family-law-pleadings/maintenance-application-bnss-144` | n/a |
| 30 | Cheque bounce complaint (NI Act s.138/142) | `/pleadings/cheque-bounce-matters/complaint-under-section-138` | n/a |
| 31 | Consumer complaint (CPA 2019) | `/pleadings/consumer-law/consumer-complaint-cpa-2019` | n/a |
| 32 | Suit for money recovery (incl. Order XXXVII and s.12A) | `/pleadings/money-recovery-and-financial-matters/suit-for-money-recovery` | n/a |
| 33 | Suit for permanent injunction | `/pleadings/civil-pleadings/suit-for-permanent-injunction` | n/a |
| 34 | Written statement | `/pleadings/civil-pleadings/written-statement` | n/a |
| 35 | Petition for probate | `/pleadings/succession-and-inheritance/petition-for-grant-of-probate` | n/a |
| 36 | Private limited company registration | `/start-a-business/incorporate-your-business/private-limited-company` | — |
| 37 | LLP registration | `/start-a-business/incorporate-your-business/limited-liability-partnership` | — |
| 38 | One person company registration | `/start-a-business/incorporate-your-business/one-person-company` | — |
| 39 | Trademark registration | `/start-a-business/protect-your-intellectual-property/trademark` | — |
| 40 | Copyright registration | `/start-a-business/protect-your-intellectual-property/copyright` | — |
| 41 | MSME (Udyam) registration | `/start-a-business/registrations-for-business/msme-registration` | — |
| 42 | FSSAI registration and licence | `/start-a-business/get-a-license/fssai` | — |
| 43 | Import Export Code (IEC) | `/start-a-business/get-a-license/import-export-code-iec` | — |
| 44 | GST registration | `/compliance/gst/gst-registration` | — |
| 45 | GST return filing | `/compliance/gst/gst-return-filing` | — |
| 46 | Income tax return filing | `/compliance/taxation/income-tax-return-itr-filing` | — |
| 47 | Company and OPC annual filings | `/compliance/roc-compliances/companies-and-opc-annual-filings` | — |
| 48 | Closing a company (strike off) | `/compliance/closure-of-business/closing-of-company` | — |
| 49 | NBFC compliance services (regulated entities) | `/regulated-entities/rbi/nbfc-compliance` | — |
| 50 | Comparison: rent agreement vs leave and licence vs lease | `/compare/rent-agreement-vs-leave-and-licence-vs-lease` | — |

**Affidavit note [INTERP][COUNSEL]:** the R5 CSV flags student and company affidavits "Valid (Aadhaar eSign)", but an affidavit is sworn before an oath commissioner or notary; the deponent's eSign alone does not complete it (conventions §13.2). Until Appendix F rules otherwise, affidavit pages show "Draft free; sign before a notary or oath commissioner" and the notary-facilitation service, and the badge reads **Check**.

### N.9.2 Rewrite rules for copied third-party text (R5 §4)

1. **Rewrite from scratch, not edit**, for every section in R5 §4 (21 sections: Compliance — closure hub, LLP closure, ITR, TDS, professional tax, accounting hub, bookkeeping, payroll, PF, shops and establishments, audit hub/company audit; Start a Business — LLP, Nidhi, patent, trademark, FSSAI, IEC, Spices Board, Hallmark, Agmark; plus the seven compliance hub testimonials). The writer does not open the manual text while drafting the rewrite; they work from the facts list (requirements, procedure, documents, law) extracted by the content engineer.
2. **Never publish** the adapted testimonials (R5 §4 row 12) or any FAQ that names a competitor or links to a competitor accordion.
3. Remove every outbound link that is not a primary source; replace Wikipedia definitions with an original definition plus a primary-source citation.
4. Run the full plagiarism scan over all four manuals before reuse (R5 §4 instruction; web-search checks were incomplete), then again on each rewritten page.
5. Contact details: replace "Call now. 9468776000" endings with the drafter and hire blocks and the single public number (`web.contact.public_phone` [OWNER]).

### N.9.3 Outdated-law rules (R5 §5 → linter dictionary)

| Old reference | Write instead | Notes |
|---|---|---|
| CrPC 1973 s.125 / 167(2) / 200 / 437 / 438 / 439 | BNSS 2023 s.144 / 187 / 223 / 480 / 482 / 483 | "(formerly CrPC s.x)" in brackets; BNSS s.531 savings for proceedings pending before 1 July 2024 |
| IPC s.498A / 406 / 420 / 499–500 / 506 | BNS s.85–86 / 316 / 318 / 356 / 351 | Offences before 1 July 2024 remain under IPC |
| Evidence Act s.65B | BSA 2023 s.63 with the Schedule certificate | Link the s.63 certificate product feature (NN-10) |
| Consumer Protection Act 1986; "District Forum" | CPA 2019; District/State/National Commissions; e-Daakhil | Pecuniary limits per the 2021 Rules [VERIFY current limits] |
| Companies Act 1956 s.25 / s.292 | Companies Act 2013 s.8 / s.179–180 | "formerly s.25" as context only |
| Listing Agreement / Clause 49 | SEBI (LODR) Regulations 2015 | Retire "Listing agreement" templates |
| Udyog Aadhaar | Udyam Registration (from 1 July 2020); revised limits from 1 April 2025 | Rewrite MSME pages completely |
| GSTR-2 / GSTR-3 matching | GSTR-1/1A, 3B, 2B and the Invoice Management System | Add current rate structure [VERIFY] |
| CGST s.35(5) audit, CA-certified 9C | Omitted w.e.f. 1 Aug 2021; self-certified GSTR-9C | Re-scope page to annual return and reconciliation |
| Income-tax Act 1961; "assessment year" | Income-tax Act 2025 (from 1 April 2026), "tax year" | Dual-cite during transition [VERIFY section numbers] |
| Pre-Code labour statutes | Code on Wages 2019; IR Code 2020; SS Code 2020; OSH Code 2020 (in force 21 Nov 2025) | Note transitional continuation of old rules; State S&E Acts continue |
| Hallmarking from 15 Jan 2020 | Mandatory from 16 June 2021 in notified districts; HUID-only from 1 April 2023 | — |
| Pre-2022 Nidhi rules | Nidhi (Amendment) Rules 2022 (NDH-4) | — |
| Pre-2021 OPC limits | 2021 liberalisation | — |
| Specific Relief pre-2018 | SRA as amended 2018 (s.10) | — |
| Money suits without mediation | Commercial Courts Act s.12A pre-institution mediation | Add s.12A paragraph |
| IT Act s.43A/SPDI as the privacy basis | DPDP Act 2023 and Rules 2025 | Phased commencement [VERIFY dates] |
| "eSign every document" | IT Act s.1(4) and First Schedule | Show the eSign badge (Appendix F) |

### N.9.4 Structural fixes during migration

Apply R5 §3: one canonical leaf per duplicate (D1.3/D1.4 lists; bonds; release deeds; ESOP touchpoints; job application); give Mergers & Acquisitions real documents (share purchase agreement, business transfer agreement, term sheet, scheme of arrangement, due-diligence checklist); re-file mis-filed pleadings (DV complaint out of Consumer; consumer complaints out of Corporate; arbitral award out of pleadings); commission the promised but missing sets (writ petitions, NCLT s.241–242, IBC s.7/9, s.252 restoration, arbitration statement of claim/defence) or remove the promises; fix every heading typo in R5 §3.2; strip zero-width characters.

### N.9.5 Per-page migration workflow and tracking

`Source extracted (facts list) → content agent draft (labelled) → writer rewrite → plagiarism + outdated-law + claims checks → editor review → legal review → publish → post-publish QA (no-JS fetch, schema, CWV, axe)`. Tracking fields per page in the CMS: source manual and section ID (e.g., `D12.7.7`), wave, writer, reviewer, status, plagiarism score, linter flags resolved, template bound (`tpl_`), service bound (`svc_`), State facts bound, publish date.

---

## N.10 Tutorial and video plan

### N.10.1 Formats and presets

| Channel | Aspect / resolution | Length | Captions | Other |
|---|---|---|---|---|
| Help centre and YouTube (long) | 16:9, 1920 × 1080 | 2–6 min | WebVTT EN + HI (others when reviewed); burned-in off | Chapters per step; transcript on page; ISL picture-in-picture for core set |
| YouTube Shorts | 9:16, 1080 × 1920 | 30–60 s default [VERIFY current maximum] | Burned-in + SRT | Hook in first 2 s; end card with canonical URL |
| Instagram Reels | 9:16, 1080 × 1920 | 30–60 s [VERIFY] | Burned-in | Safe areas for UI overlays |
| LinkedIn | 1:1 (1080 × 1080) or 4:5 (1080 × 1350) | 45–90 s | Burned-in + SRT | Business audience cut |
| In-app contextual | 16:9 or 9:16 | ≤ 60 s | Default on | Opened from the help panel per screen |

All clips: brand tokens, readable type at mobile size (≥ 48 px on 1080 width), no flashing (≥ 3 flashes/s prohibited), captions accurate to the script, synthetic-voice label where TTS is used, claims-gated captions and descriptions, no advocate promotion, synthetic demo data only.

### N.10.2 Script outline (every tutorial)

1. **Hook (one line):** the user's job ("Sign a rent agreement without printing anything").
2. **Who it is for** and prerequisites (plan, role).
3. **Steps** (3–7), each: action, where to tap, what you see, "i" term if any.
4. **Check:** how you know it worked.
5. **Watch out:** one legal caution (e.g., "eSign does not replace registration").
6. **Next:** related tutorial and canonical page.
Narration ≤ 150 words per minute; one idea per sentence; on-screen text mirrors narration.

### N.10.3 Feature-video catalogue (launch and Wave 2–3)

Core set (★) gets ISL renditions and Hindi voice-over by Wave 3.

| ID | Title | Persona | Wave | Social cut |
|---|---|---|---|---|
| T-01 ★ | Draft your first agreement free with Vidhi | Individual | 1 | Shorts, Reels |
| T-02 ★ | Aadhaar eSign: sign in one OTP | Individual, guest | 1 | Shorts, Reels, LinkedIn |
| T-03 ★ | Is my document valid for eSign? The eligibility badge explained | All | 1 | Shorts |
| T-04 ★ | Buy eStamp or attach your own stamp paper | Individual, company | 1 | Shorts |
| T-05 ★ | Your Legal Vault: folders, search and sharing | Individual | 1 | Reels |
| T-06 | Hire a professional at a fixed price | Individual, SME | 1 | Reels |
| T-07 ★ | Sign a document someone sent you (no account needed) | Guest | 1 | Shorts |
| T-08 | Export everything: your data, your folders | All | 1 | LinkedIn |
| T-09 ★ | Scan a document with your phone | Individual | 2 | Shorts, Reels |
| T-10 ★ | Turn a WhatsApp chat into evidence with a typed copy | Individual | 2 | Shorts, Reels |
| T-11 | Translate a document into English (and what "machine translation" means) | Individual | 2 | Reels |
| T-12 ★ | Negotiate in track changes and chat | Company, individual | 2 | LinkedIn |
| T-13 | Internal vs external comments in a deal room | Company | 2 | LinkedIn |
| T-14 ★ | Maker and checker: approve a contract | Company checker | 2 | LinkedIn |
| T-15 | Set up your company workspace and users | Company admin | 2 | LinkedIn |
| T-16 | Delivery grants: let your LawDocs RM work as maker | Company admin | 2 | LinkedIn |
| T-17 ★ | Track a court case with a CNR number | Company, individual | 2 | Shorts |
| T-18 | Hearing alerts and the legal calendar | CLO | 2 | LinkedIn |
| T-19 | Track a trademark application and deadlines | Startup | 2 | Shorts |
| T-20 | Draft a legal notice and send it on record | Individual, SME | 2 | Reels |
| T-21 | Prepare a pleading draft and file through an advocate | Individual | 2 | — |
| T-22 | BSA s.63 certificate for electronic evidence | Individual, advocate | 2 | LinkedIn |
| T-23 | Run your legal department with one CLO and Vidhi | Company | 2 | LinkedIn (VSL cut) |
| T-24 | Board resolutions and minutes | Company secretary | 2 | LinkedIn |
| T-25 | Vidhi agents: what they can and cannot do | Company | 2 | LinkedIn |
| T-26 | Accessibility settings: text size, contrast, captions, Listen | All | 1 | Shorts, Reels |
| T-27 | Use the "i" button to understand legal terms | All | 1 | Shorts |
| T-28 | Start a company: Pvt Ltd vs LLP vs OPC | Startup | 2 | Shorts, LinkedIn |
| T-29 | Founder kit: agreements every startup needs | Startup | 2 | LinkedIn |
| T-30 | Retainers and SLAs signed inside LawDocs | Company | 2 | LinkedIn |
| T-31 | Plans, credits and cancelling (no surprises) | All | 1 | — |
| T-32 | Connect OneDrive, Google Drive or your own bucket | Company admin | 2 | LinkedIn |
| T-33 | Bulk import documents by folder | Company admin | 2 | — |
| T-34 | Savings dashboard: how we count hours and penalties avoided | Company | 3 | LinkedIn |
| T-35 | Loan complaint: the right order (lender → wait → ombudsman) | Consumer Help | 3 | Shorts, Reels |
| T-36 | Insurance claim rejected: your options | Consumer Help | 3 | Shorts, Reels |
| T-37 | Check a traffic challan and pay on the official portal | Consumer Help | 3 | Shorts |
| T-38 | Sell your car: agreement, delivery note and Vahan | Individual | 3 | Shorts, Reels |
| T-39 | Tax workspace basics (ITR, GST) | Individual, SME | 3 | Reels |
| T-40 | Mobile app: offline documents and biometric lock | Individual | 2 | Shorts |

Explainer series (blog + video, non-product): "Old law, new law" (CrPC→BNSS, IPC→BNS, Evidence Act→BSA) 10 × 60 s; "Stamp duty by State" 10 × 60 s (one State each, source on screen); "Clause of the week" 52 × 30 s.

### N.10.4 Captions, transcripts and ISL

- Captions from the script (exact), then aligned; ≥ 99% accuracy; speaker identification; sound cues in brackets ("[notification sound]").
- Transcripts on the page as HTML (not a PDF), with chapter headings.
- ISL: recorded with a qualified interpreter (ISLRTC-trained [VERIFY credential route]) for the ★ set; interpreter window ≥ 1/4 of frame height, unobstructed, consistent side; ISL version linked from the standard video and available as a separate file (R3 LG-137).
- Audio description: where visuals carry meaning not in narration, provide an extended or described version (WCAG 1.2.5).

### N.10.5 Production cadence

Wave 1: T-01–T-08, T-26, T-27, T-31 (11 videos). Wave 2: T-09–T-25, T-28–T-30, T-32, T-33, T-40 (23). Wave 3: T-34–T-39 and ISL renditions of all ★. Ongoing: 2 social clips per week from the catalogue and explainer series, pushed to the OH7 social calendar (P21 FR-P21-138).

---

## N.11 Blog category taxonomy and Word-folder mapping [OWNER to supply folder list]

Proposed taxonomy (max depth 2). Each category has an intro (≥ 120 words), an owner and a legal flag.

| Category | Sub-categories | Legal flag | Primary bridge |
|---|---|---|---|
| Property and Rent | Rent and lease · Buying and selling · Gift and partition · RERA | Y | Property documents |
| Family and Succession | Marriage and divorce · Custody and maintenance · Wills and inheritance · Senior citizens | Y | Family/succession documents and pleadings |
| Business and Startups | Starting up · Founders and funding · Contracts · IP and brand | Y | Start a Business, founder kit |
| Employment and HR | Hiring and offer letters · Labour Codes · Workplace policies | Y | HR documents |
| Courts and Disputes | Notices · Civil · Criminal · Consumer · Cheque bounce · ADR | Y | Pleadings, litigation tracker |
| Tax and Compliance | Income tax · GST · ROC and secretarial · Audit | Y | Compliance services |
| Regulated Finance | RBI/NBFC · SEBI · IRDAI · Fintech | Y | Regulated entities; LawDocsComply |
| Digital Life and Privacy | eSign and eStamp · DPDP and privacy · Cyber safety | Y | Product pages |
| Consumer Help (brand host only) | Loans · Insurance · Challans · Vehicles | Y | Brand site |
| LawDocs Product | Release notes · How-tos · Case studies (claims-gated) | N | Help centre |

**Folder mapping table (`web.cms.folder_category_map`):**

| Owner folder path (as supplied) | Category | Sub-category | Default tags | Legal flag |
|---|---|---|---|---|
| [OWNER to supply] | — | — | — | — |

Rules: folder names are matched case-insensitively after trimming; unmapped folders create a proposal, not a category (P21 FR-P21-79); a Word file's first Heading 1 becomes the post H1 candidate; the file name never becomes the slug without editing.

---

## N.12 Glossary priority list (by wave)

Keys follow `hlp.<module>.<term>`; general legal jargon uses `hlp.gen.<term>` (P21 FR-P21-119). Each term needs a plain definition in every enabled D-07 language.

**Wave 1 (≥ 150) — product, signing, stamping, vault, drafting (selected):** eSign (`hlp.sgn.esign`), Aadhaar eSign, ESP (eSign service provider), ASP, DSC, signer consent, evidence pack, BSA s.63 certificate, hash value, eStamp, e-stamp certificate UIN, stamp duty, State stamp article, franking, ACC (authorised collection centre), SHCIL, registration (Registration Act), sub-registrar, notarisation, oath commissioner, attestation, witness, wet-ink signature, instrument eligibility, First Schedule (IT Act), execution, counterpart, original vs derived rendition, OCR, type copy, machine translation, confidence score, Legal Vault, folder view, version, legal hold, retention, export package, BYO storage, template, template automation, questionnaire, clause, clause library, AI draft, professional review, Vidhi, Vidhi help mode, maker, checker, approver, delivery grant, workspace, tenant, consent artefact, DPDP notice, data principal, grievance officer, platform fee, government fee, GST, reverse charge, invoice, credit pack, subscription, renewal, cancellation, consideration, indemnity, warranty, representation, termination, notice period, lock-in, security deposit, escalation clause, force majeure, jurisdiction, governing law, arbitration clause, severability, entire agreement, counterparts clause, power of attorney, general vs special POA, gift deed, will, codicil, probate, nominee, guardian, leave and licence, lease, rent agreement, paying guest, eviction, legal notice, reply notice, affidavit, deponent, vakalatnama, NDA, founders' agreement, vesting, cliff, ESOP, shareholders' agreement, partnership deed, LLP agreement, MoA, AoA, DIN, DSC (company), CIN, GSTIN, PAN (masked), Aadhaar masking, DigiLocker, offline verification (OVSE).

**Wave 2 (to ≥ 350) — contracts, litigation, IP, governance:** redline, round, track changes, deal room, internal comment, obligation, renewal date, CNR number, cause list, next date of hearing, interim order, ex parte, adjournment, written statement, plaint, petition, caveat, injunction, specific performance, summary suit (Order XXXVII), pre-institution mediation (s.12A), limitation period, condonation of delay, court fee, e-filing, BNSS, BNS, BSA, anticipatory bail, regular bail, default bail, maintenance (BNSS s.144), cooling-off period, Section 138 NI Act, demand notice, District/State/National Commission, e-Daakhil, trademark class, TM-A, examination report, objection, show-cause hearing, opposition, advertisement in TM Journal, renewal (10 years), copyright, patent, GI, board meeting, quorum, resolution (ordinary/special), minutes, KMP, director, AGM, RPT, DoA (delegation of authority), CLO, legal intake, matter, legal spend, retainer, SLA.

**Wave 3 (to ≥ 500) — business services, tax, Consumer Help:** SPICe+, Udyam, FSSAI registration vs licence, IEC, tax year (Income-tax Act 2025), ITR forms, TDS, TCS, GSTR-1, GSTR-3B, GSTR-2B, IMS, GSTR-9/9C, ROC annual filing (AOC-4, MGT-7/7A), DIR-3 KYC, strike off, ombudsman, RB-IOS, regulated entity, internal ombudsman, insurance ombudsman, claim repudiation, challan, Virtual Court, Vahan, RC transfer, delivery note, hypothecation, NOC (loan), recovery agent conduct, credit report dispute.

---

## N.13 Store listing copy system (P22)

| Field | LawDocs (English) draft | Rules |
|---|---|---|
| App name | LawDocs: Agreements & eSign | ≤ 30 chars (Apple) [VERIFY]; no "best", no advocate names |
| Subtitle (iOS) / short description (Android) | Draft free, eSign, keep forever | ≤ 30 / ≤ 80 chars [VERIFY] |
| Full description opening | "Draft it. Sign it. Keep it. LawDocs helps you draft agreements from vetted templates, sign with Aadhaar eSign where the law allows, buy eStamp through authorised channels and keep every document in your Legal Vault." | First 3 lines carry the value; claims-gated; no "real-time" court data; AI disclosure ("Vidhi is an AI assistant, not a lawyer") |
| Feature bullets | Draft free with Vidhi · eSign and eStamp · Legal Vault with offline access · Scan and type copy · Negotiate in track changes · Case and trademark tracker (with refresh times) · Hire professionals at fixed prices · 10 Indian languages (as enabled) · Accessibility settings | Each bullet must exist in the shipped build (parity matrix) |
| Keywords (iOS) | rent agreement, esign, e stamp, legal documents, agreement maker, document scanner, notice, will, nda, contract | No competitor names; no trademarks of others |
| Screenshots | 6–8 per device class from the tutorial pipeline (synthetic data), caption ≤ 6 words each, text also in the description for screen-reader users | No fake data that looks real (no real names, Aadhaar or PAN even masked-looking) |
| What's new | Plain list of user-visible changes; no marketing superlatives | — |
| Localised listings | Hindi first; others when the app locale is ≥ 99% complete | Reviewed translations only |
| Consumer Help flavour | Name `[Consumer Help Brand]`; calm voice (N.1.6); "We do not collect fines or dues" | Separate developer listing entity per D-06 [OWNER] |

---

## N.14 Structured-data snippets (JSON-LD; generated by P21 from page data)

Values in `{{…}}` come from registries. Never emit markup that does not match visible content.

**Organization (sitewide)**

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.lawdocs.in/#organization",
  "name": "LawDocs",
  "legalName": "{{entity.legal_name}}",
  "url": "https://www.lawdocs.in/",
  "logo": "https://www.lawdocs.in/assets/brand/lawdocs-logo-512.png",
  "parentOrganization": { "@type": "Organization", "name": "Infrabyx Group" },
  "sameAs": ["{{entities.lawdocs.same_as}}"],
  "contactPoint": [{
    "@type": "ContactPoint",
    "contactType": "customer support",
    "telephone": "{{web.contact.public_phone}}",
    "areaServed": "IN",
    "availableLanguage": ["en", "hi"]
  }]
}
```

**Document page (WebPage + BreadcrumbList + Service with Offer for a hire tier)**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.lawdocs.in/documents/property-transactions/rent/rent-agreement-residential#webpage",
      "url": "https://www.lawdocs.in/documents/property-transactions/rent/rent-agreement-residential",
      "name": "Residential Rent Agreement — Draft Free, eSign Online",
      "description": "{{page.summary_answer}}",
      "inLanguage": "en-IN",
      "dateModified": "{{page.date_modified}}",
      "reviewedBy": { "@id": "https://www.lawdocs.in/team/{{reviewer.slug}}#person" },
      "isPartOf": { "@id": "https://www.lawdocs.in/#website" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.lawdocs.in/" },
        { "@type": "ListItem", "position": 2, "name": "Documents", "item": "https://www.lawdocs.in/documents" },
        { "@type": "ListItem", "position": 3, "name": "Property Transactions", "item": "https://www.lawdocs.in/documents/property-transactions" },
        { "@type": "ListItem", "position": 4, "name": "Rent", "item": "https://www.lawdocs.in/documents/property-transactions/rent" },
        { "@type": "ListItem", "position": 5, "name": "Residential Rent Agreement" }
      ]
    },
    {
      "@type": "Service",
      "name": "Rent agreement review by a professional",
      "serviceType": "Legal document review",
      "provider": { "@id": "https://www.lawdocs.in/#organization" },
      "areaServed": { "@type": "Country", "name": "India" },
      "offers": {
        "@type": "Offer",
        "price": "{{svc.review.total_incl_gst}}",
        "priceCurrency": "INR",
        "availability": "https://schema.org/InStock",
        "url": "https://www.lawdocs.in/marketplace/documents/rent-agreement-review"
      }
    }
  ]
}
```

**Product + Offer (only where a fixed-price template unlock is sold on the page)**

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Residential rent agreement — clean DOCX and PDF",
  "description": "Unlock a watermark-free copy of your completed rent agreement.",
  "brand": { "@type": "Brand", "name": "LawDocs" },
  "offers": {
    "@type": "Offer",
    "price": "{{tpl.unlock.price_incl_gst}}",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  }
}
```

**LegalService per real office (never for city pages)**

```json
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "LawDocs — {{office.city}} office",
  "parentOrganization": { "@id": "https://www.lawdocs.in/#organization" },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{office.street}}",
    "addressLocality": "{{office.city}}",
    "addressRegion": "{{office.state}}",
    "postalCode": "{{office.pin}}",
    "addressCountry": "IN"
  },
  "telephone": "{{web.contact.public_phone}}",
  "url": "https://www.lawdocs.in/contact#{{office.slug}}"
}
```

**BlogPosting with author and reviewer**

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{{post.h1}}",
  "description": "{{post.summary_answer}}",
  "datePublished": "{{post.published_at}}",
  "dateModified": "{{post.date_modified}}",
  "author": { "@type": "Person", "@id": "https://www.lawdocs.in/team/{{author.slug}}#person", "name": "{{author.name}}" },
  "publisher": { "@id": "https://www.lawdocs.in/#organization" },
  "mainEntityOfPage": "{{post.url}}",
  "image": "{{post.og_image}}"
}
```

**VideoObject**

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Aadhaar eSign: sign in one OTP",
  "description": "{{video.summary}}",
  "thumbnailUrl": "https://www.lawdocs.in/media/video/{{video.id}}/thumb.webp",
  "uploadDate": "{{video.upload_date}}",
  "duration": "{{video.iso_duration}}",
  "embedUrl": "https://www.youtube-nocookie.com/embed/{{video.youtube_id}}",
  "creator": { "@id": "https://www.lawdocs.in/#organization" },
  "inLanguage": "en-IN"
}
```

**DefinedTerm**

```json
{
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": "eStamp certificate",
  "description": "{{term.plain_definition}}",
  "inDefinedTermSet": "https://www.lawdocs.in/glossary",
  "url": "https://www.lawdocs.in/glossary/estamp-certificate"
}
```

**FAQPage (only mirrors visible Q&A; `web.schema.faqpage_mode = VISIBLE_ONLY`)**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "Can I eSign a rent agreement with Aadhaar?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Yes. A rent agreement can be signed with Aadhaar eSign. You still need to pay stamp duty in your State and, for leases of a year or more, register it."
    }
  }]
}
```

**ProfilePage for an advocate reviewer (BCI Rule 36 fields only)**

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://www.lawdocs.in/team/{{reviewer.slug}}#person",
    "name": "{{reviewer.name}}",
    "jobTitle": "Advocate",
    "address": { "@type": "PostalAddress", "addressLocality": "{{reviewer.city}}", "addressCountry": "IN" },
    "email": "{{reviewer.public_email}}",
    "knowsAbout": ["{{reviewer.practice_areas}}"],
    "hasCredential": {
      "@type": "EducationalOccupationalCredential",
      "credentialCategory": "Enrolment",
      "recognizedBy": { "@type": "Organization", "name": "{{reviewer.state_bar_council}}" },
      "identifier": "{{reviewer.enrolment_no}}"
    }
  }
}
```

No `image`, ratings, reviews, fees or "awards" for advocates (NN-21). No `Review`/`AggregateRating` for LawDocs (self-serving), no `HowTo`, no `Course`.

---

## N.15 Editorial calendar

**Cadence (steady state):** 3 blog posts per week (one evergreen guide, one law-change explainer, one practical "how to"); 1 long video per fortnight; 2 social clips per week; monthly newsletter (sent by OH); quarterly law-change sweep report; monthly AI-answer panel (N.8.3).

**Recurring anchors** (dates to be confirmed each year [VERIFY]; legal due dates under the Income-tax Act 2025 and GST rules must be re-verified before publication):

| Month | Anchor | Content |
|---|---|---|
| January | New year; Republic Day (26 Jan) | "Legal checklist for the year"; constitutional rights explainer |
| February | Union Budget (1 Feb) | Budget explainer for individuals and startups (reviewed by CA) |
| March | World Consumer Rights Day (15 Mar); financial year end | Consumer complaint guides; year-end compliance checklist |
| April | New FY / tax year; World IP Day (26 Apr) | Rent escalation reminders; trademark and copyright series |
| May–June | Admission season; property season | Student affidavits; rent and sale agreement guides |
| July | Return-filing season [VERIFY due dates]; BNSS anniversary (1 Jul) | ITR guides; "two years of BNSS" explainer |
| August | Independence Day | Startup registration series |
| September | AGM season [VERIFY]; GST rate changes if any | Board and AGM guides |
| October | Festive season; vehicle purchases | Car sale agreement; gift deeds; consumer rights for online shopping |
| November | Constitution Day (26 Nov); DPDP milestones [VERIFY] | Privacy rights; DPDP explainer |
| December | National Consumer Day (24 Dec); GST annual return [VERIFY]; National Lok Adalat dates [VERIFY] | Year-end compliance; settlement and Lok Adalat explainers |

**Planning rules:** the calendar lives in the OH7 social and content calendar (Appendix X); the CMS stores the posts and links each to its calendar slot; legal-review lead time is 5 working days for scheduled law-change posts; no post claims a law change until the Gazette or regulator source is published and verified.
