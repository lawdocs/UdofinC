# LawDocs Website Content Deck v1.0

> **Status:** Binding copy source for P21 (Public Website, CMS, SEO/GEO, Help Centre). Version 1.0, 25 October 2026.
> **Owner:** Company Secretary, Infrabyx Group (project owner and product manager).
> **Used by:** P21 (website build and CMS seeding), P06 (Vidhi drafting block), P08 (eSign/eStamp notices), P16 (marketplace and retainer copy), P17 (pricing page), P15 (Consumer Help brand), P04 (Legal Vault), P11/P12 (trackers).
> **Sources:** Owner brief (25 Oct 2026); the owner's four manuals (`src/Manual_*.md`); R5 (voice, one-liners, templates, copied-content and outdated-law lists); R3 (legal accuracy, rule IDs LG-xxx); R6 (pricing seeds); R2 (Consumer Help); R1 (competitor patterns — studied, never copied); Authoring Conventions §7, §13.
> **Decisions applied:** D-04, D-05, D-06, D-08, D-11, D-15, D-16, D-17 · **Challenges applied:** CH-01, CH-12, CH-13, CH-14, CH-15, CH-20, CH-22, CH-23, CH-27, CH-30, CH-31 · **Non-negotiables reflected in copy:** NN-03, NN-07, NN-08, NN-14, NN-20, NN-21, NN-22, NN-23, NN-26, NN-41, NN-42, NN-49, NN-50.

---

## 1. How to use this deck

### 1.1 Who this is for

| Reader | What they do with the deck |
|---|---|
| Owner | Approves the voice, the messaging house and every `[OWNER]` / `[OWNER TO SET]` item before launch. |
| Content team (`OPS_CONTENT_PUBLISHER`) | Pastes the copy into the CMS templates exactly as written. Changes wording only inside the rules in §2.6. Never edits a sentence that carries a legal citation without a reviewer. |
| Legal reviewer of record (`PLT_LEGAL_REVIEWER`) | Clears every `[COUNSEL]` and `[VERIFY]` flag, signs the "Reviewed by" field, sets the next review date. |
| Coding agent (P21) | Builds the templates, seeds the CMS with this copy, and enforces the publish gate in §1.5. |

### 1.2 Flags used in this deck

| Flag | Meaning | Publish rule |
|---|---|---|
| `[COUNSEL]` | A lawyer must confirm the statement or the structure. | Page stays `noindex` and unpublished until cleared. |
| `[VERIFY: …]` | A fact not confirmed in research. The note says what to check and where. | Remove the flag only after the check is logged in `docs/compliance/verification-log.md` (NN-38). If unverified at launch, delete the sentence; never publish a flag. |
| `[OWNER]` | A business decision. | Owner decides; content team updates. |
| `[OWNER TO SET]` | A price or number. Seeds come from R6 and are not final. | Page shows "Price coming soon" until set. Never publish a seed as a real price. |
| `PLACEHOLDER` | Text that must be replaced with genuine material (testimonials, names, numbers). | Never published as it stands. The CMS blocks publishing while the word PLACEHOLDER is present. |
| `[●]` | A field to fill from Super Admin → Legal entities (D-08). | Rendered from settings, not typed. |

### 1.3 Where each page goes

| Deck ref | Page | Canonical URL | CMS template | Launch wave | Reviewer |
|---|---|---|---|---|---|
| FP-01 | Home | `/` | Home | 1 | Owner + counsel |
| FP-02 | Rent / Lease Agreement | `/documents/property-transactions/rent/rent-agreement` | Document page (R5 §7.2) | 1 | Advocate |
| FP-03 | Agreement to Sell (immovable property) | `/documents/property-transactions/sale-and-purchase/agreement-to-sell` | Document page | 1 | Advocate |
| FP-04 | Vehicle Sale Agreement | `/documents/financial-transactions/sale-of-goods/vehicle-sale-agreement` | Document page | 1 | Advocate |
| FP-05 | Non-Disclosure Agreement | `/documents/deals-and-agreements/contracts-and-agreements/non-disclosure-agreement` | Document page | 1 | Advocate |
| FP-06 | Offer Letter and Appointment Letter | `/documents/hr-and-service/job-application-and-offers/offer-and-appointment-letter` | Document page | 1 | Advocate / CS |
| FP-07 | Partnership Deed | `/documents/planning-and-execution/partnership-and-founders/partnership-deed` | Document page | 1 | Advocate / CS |
| FP-08 | Founders' Agreement and Startup Desk | `/startups` (landing) + `/documents/planning-and-execution/partnership-and-founders/founders-agreement` | Section landing + document page | 1 | Advocate / CS |
| FP-09 | Legal Notice (incl. cheque bounce) | `/documents/legal/legal-notices/legal-notice` | Document page | 1 | Advocate |
| FP-10 | Aadhaar eSign and eStamp | `/esign` | Product page | 1 | Counsel |
| FP-11 | Legal Vault | `/legal-vault` | Product page | 1 | Counsel + DPO |
| FP-12 | Litigation and Case Tracker | `/case-tracker` | Product page | 2 | Advocate |
| FP-13 | Trademark Registration and Tracker | `/trademarks` | Service + product page | 2 | TM agent / advocate |
| FP-14 | Marketplace and Retainer Advisory | `/marketplace` and `/retainers` | Storefront landing | 1 (shell) / 2 | Counsel |
| FP-15 | Pricing | `/pricing` | Pricing | 1 | Owner + tax |
| CH-HOME etc. | Consumer Help starter pages | `[consumer-help-domain]/` | Consumer Help brand templates | 3 | Counsel |

Old URLs are redirected with 301s per R5 §2 (for example `/smartdrafts/property-matters/rent` → FP-02). P21 owns the redirect map.

### 1.4 Editing rules for the content team

1. Character limits are hard: SEO title ≤ 60 characters, meta description ≤ 155, answer-first summary 40–60 words, FAQ answers ≤ 60 words.
2. Placeholders in square brackets render from settings: `[LawDocs Operating Entity]`, `[Consumer Help Brand]`, `[Public phone]`, `[Support email]`, `[Grievance Officer]`. Do not hard-code them.
3. Every legal page keeps its "Reviewed by" footer. A page without a named reviewer is `noindex` automatically (R5 §7.4 item 10).
4. Do not paste any sentence from the manuals. Section 5 lists the manual sections that must be rewritten from scratch.
5. Do not add numbers, ratings, logos of regulators, or "as seen in" claims. Section 2.4 lists what may be claimed.

### 1.5 Publish gate (enforced by the CMS)

| Check | Blocks publishing when |
|---|---|
| Flags | Any `[COUNSEL]`, `[VERIFY`, `[OWNER` or `PLACEHOLDER` string remains. |
| Reviewer | "Reviewed by" or "Next review date" is empty on a legal page. |
| Prices | A price block shows a value not present in the live price catalogue (OH8). |
| Claims | Text matches the banned-words list in §2.5 (warning; editor must justify). |
| SEO | Title or meta over limit; duplicate title or meta across URLs; missing H1. |
| Accessibility | Images without alt text; heading levels skipped; link text "click here". |

---

## 2. Brand voice and messaging house

### 2.1 Positioning

**Positioning line (site-wide):** *Draft it. Sign it. Keep it.*

**One-sentence positioning:** LawDocs is India's legal operations app for people and businesses: draft with Vidhi AI, agree terms with the other side, stamp and eSign, keep every document in your Legal Vault, track cases and trademarks, and bring in a professional when judgement matters.

**25-word boilerplate:** LawDocs helps individuals and companies in India draft, negotiate, stamp, eSign, store and track legal documents, with Vidhi AI and qualified professionals on call.

**50-word boilerplate (About, press, app stores):** LawDocs (lawdocs.in) is a legal operations platform from Infrabyx Group. Individuals use it to prepare everyday agreements, sign with Aadhaar eSign where the law allows, and keep documents safe in a Legal Vault. Companies use it to run contracts, cases, trademarks and approvals in one place, with on-demand professionals.

**What LawDocs is not (say this plainly when relevant, D-17, CH-14, NN-41):** not a law firm; not a replacement for your advocate; not a government service; not DigiLocker; not a payment collector for fines, dues or stamp duty beyond the authorised pass-through shown at checkout.

### 2.2 Messaging house

**Roof:** Your legal work in one place. For as long as you need it.

| Pillar | Promise (one line) | What we explain | Proof we may show | Signature line |
|---|---|---|---|---|
| **Draft** | Start from a vetted template, answer a few questions, get a clean draft. | Template automation is free; AI-custom drafts are labelled and can be reviewed by a professional. | Number of published templates (from CMS count); named reviewer on each template. | First draft free. Final word yours. |
| **Negotiate** | Agree terms with the other side without email chaos. | Track changes, comments, in-app messages, one version per round. | Feature demo; none of the parties sees the other's internal notes. | Terms first. Trust follows. |
| **Sign** | Stamp, then sign — with Aadhaar eSign, DSC or wet ink, as the law allows. | Eligibility check before every signing; stamp duty at actuals; evidence pack after signing. | Licensed eSign Service Provider named once contracted `[OWNER]`; eligibility rules published. | One OTP. One recognised signature. |
| **Store** | Every document in one Legal Vault, searchable, shareable on your terms. | Originals locked; typed copies and translations labelled; export everything free. | Hosting region and encryption once verified at launch `[VERIFY at launch]`; export format published. | Store once. Find it fast. |
| **Track** | Hearings, trademark deadlines and renewals on one calendar. | Data from official sources and licensed partners, refreshed on a schedule you can see. | "Last updated" time on every record. Never "real-time". | Every hearing, on your radar. |
| **Get expert help** | Hire a qualified professional at a fixed price, shown in full before you pay. | Professional fee, LawDocs platform fee and GST shown as separate lines; advocates act in their own name. | Fee breakdown on every service card. | Expert eyes. Fixed price. |

**Foundation (brand principles):**

| Principle | Means | Copy test |
|---|---|---|
| Neutral by design | Templates protect both parties fairly. We say where a clause favours one side. | Would the other party feel ambushed? Rewrite. |
| Price before payment | Every fee, duty and tax is shown before the pay button (NN-22, NN-50). | Can the user see the total including GST? |
| Your data, your exit | Free export at any time in plain folders (NN-11). | Does any line suggest lock-in? Remove it. |
| AI with a human check | Vidhi drafts and explains; a professional advises (NN-14). | Does Vidhi sound like a lawyer? Rewrite. |
| Indian law, current law | Cite the current Act (BNS, BNSS, BSA, CPA 2019, Labour Codes, Income-tax Act 2025). | Is any 1860/1872/1973/1986 citation used without "formerly"? Fix. |

### 2.3 Voice

**Voice in one sentence:** LawDocs talks like a sharp senior associate with a good ear for a pun: it states the legal point in a few words, gives the human reason, and ends with an action.

| Trait | Do | Don't |
|---|---|---|
| Short | "Rent right. Live light." Two to six words per tagline. | Stack three taglines on one screen. |
| Second person | "You keep the original. We keep the record." | "LawDocs provides users with…" |
| Plain | "Stamp duty is a State tax. You pay it at actuals." | "The instrument shall be duly stamped as per applicable laws." |
| Honest | "eSign is not valid for a will. Here is the print-and-sign pack." | "eSign anything, anywhere." |
| Warm in personal matters | "Part ways. Keep the peace." | Jokes in divorce, custody, death or violence pages. |
| Action at the end | "Draft it, now." | End a section on a definition. |

### 2.4 Proof points allowed (NN-20)

| Claim type | Allowed? | Evidence required before use | Approved wording |
|---|---|---|---|
| Template count | Yes | Live CMS count of published, reviewed templates | "[n] reviewed templates" (auto-filled) |
| Documents signed / users | Only when measured | Product analytics, monthly snapshot, audited by owner | "[n] documents signed on LawDocs since [month year]" — `[OWNER]` |
| "Verified lawyers" / "verified professionals" | No | — | "Enrolment or membership number checked at onboarding" — only after the check process exists `[VERIFY]` |
| Licensed eSign | Yes, once contracted | Contract with an aggregator/ESP; ESP on the CCA list (R3 LG-005) | "Aadhaar eSign through a CCA-licensed eSign Service Provider" |
| Stamp duty channel | Yes, once contracted | Contract with an authorised collection centre or State channel (R3 LG-098–LG-100) | "e-stamp certificates through authorised channels, at actual duty" |
| Data in India | Yes, once deployed | Hosting evidence (ap-south-1/ap-south-2) | "Your vault is stored on servers in India" |
| Encryption | Yes, once deployed | Security design record | "Encrypted in transit and at rest" |
| Certifications (ISO 27001, SOC 2, PCI DSS) | No, until issued | Certificate or attestation letter | PCI: "Card payments are handled on Razorpay's hosted checkout. We never see or store your card number." (CH-19) |
| "Real-time" court or trademark data | Never | — | "Updated from official sources and licensed partners. Last updated [time]." |
| Success rates, savings, rankings, "No. 1", "best" | Never | — | — |
| "Government-approved", regulator logos | Never | — | Link to the regulator's own page instead. |
| Speed ("in minutes") | Only when measured | Median time from analytics | "Most users finish a rent agreement draft in [n] minutes" `[VERIFY from analytics]` |
| Group membership | Yes | Fact | "LawDocs is part of Infrabyx Group." |
| Founding year | Yes, once confirmed | Incorporation record | "Building legal tools since [year]" `[OWNER]` |

### 2.5 Words to use and words to avoid

| Use | Avoid | Why |
|---|---|---|
| Legal Vault | DigiLocker, digital locker (for our product) | LawDocs is not a Digital Locker under the 2016 Rules (R3 LG-036; CH-15). |
| Import from DigiLocker | "Our DigiLocker", "government locker" | DigiLocker is a government service we connect to with your consent. |
| Aadhaar eSign | Aadhaar login, Aadhaar sign-in | Aadhaar is never a login method (NN-03; CH-01). |
| Verify with Aadhaar App | Fetch your Aadhaar, Aadhaar auto-fill | Offline verification only (R3 LG-025, LG-030). |
| eSign-eligible / not eSign-eligible | "eSign everything", "100% legal" | The IT Act First Schedule excludes some instruments (NN-07). |
| e-stamp certificate, stamp duty at actuals | "Buy stamp paper from us", "no stamp paper needed" | Stamps come only through authorised channels (NN-08; R3 LG-102). |
| Professional, advocate, chartered accountant, company secretary | "Top lawyer", "best CA", "verified expert" | BCI Rule 36 and NN-20. |
| Fixed price, shown in full | "From ₹99*", "hidden charges none" (with asterisks) | Drip pricing is a dark pattern (NN-50). |
| Vidhi drafts, Vidhi explains | "AI lawyer", "legal advice from AI" | NN-14; LG-119. |
| AI draft — not reviewed by a professional | "Lawyer-grade AI draft" | NN-14. |
| Last updated [time] | Real-time, live, instant | NN-20; CH-27. |
| Track, remind, prepare | Guarantee, ensure success, win | Outcome promises are unlawful or misleading (NN-23). |
| Cancel anytime from Settings | "Cancel by calling us" | Cancellation as easy as sign-up (NN-50). |
| Consumer commission | Consumer forum, District Forum | CPA 2019 renamed them (R5 §5). |
| BNS / BNSS / BSA (formerly IPC / CrPC / Evidence Act) | IPC, CrPC, Evidence Act alone | New criminal laws in force 1 July 2024 (R5 §5). |
| Blockchain, smart contract (never, unless a real feature exists) | Used in the manuals for rent, lease and partnership pages | No such feature is in scope; unevidenced claim. |

### 2.6 House style

1. **CTA formula:** "[Verb] [object], now." Keep the comma: "Draft it, now." "Send the notice, now." Use "now" once per screen.
2. **The "…, legally." kicker:** maximum one per page and twelve on the whole site.
3. **Capitals:** sentence case for headings and buttons ("Draft free with Vidhi"). Proper nouns keep capitals: Legal Vault, Vidhi, FinLegal Academy, Aadhaar eSign.
4. **Numbers and money:** ₹1,499 (Indian grouping: ₹1,00,000; ₹3 lakh in prose). "18% GST" not "GST@18%". Dates: 1 July 2026.
5. **Citations on the site:** Act name + year + section, linked to India Code or the regulator: "Registration Act 1908, s.17". In FAQs, one citation per answer is enough.
6. **Inclusive:** "they" for an unknown party; "spouse" not "wife" unless the law is gender-specific.
7. **Spelling:** British/Indian (licence as noun, license as verb; organisation; authorise; judgement in general prose, judgment for a court decision).
8. **Placement of the one-liner:** eyebrow above the H1, never the H1 itself (R5 §7.2).

### 2.7 The owner's signature lines — kept and polished

| Original (manuals) | Polished | Where it lives | Note |
|---|---|---|---|
| Team up. | Team up. | Collaboration and JV hub | Kept as is. |
| Neutral drafts. Equal Favours. | Neutral drafts. Equal footing. | Brand pillar, Partnership, NDA | "Equal Favours" is ungrammatical; alternative "Neutral drafts. Equal favour." `[OWNER]` picks one. |
| Drafts that don't take sides. | Drafts that don't take sides. | Partnership and Founders hub | Kept. |
| Rent happiness. | Rent happiness. | Rent hub | Kept. |
| Lease with ease. | Lease with ease. | Lease hub | Kept. |
| Cheque. Check. Checkmate. | Cheque. Check. Checkmate. | Cheque-bounce notice | Kept; strongest pun. |
| Bounce back. Legally. | Bounce back. Legally. | Reply to a legal notice | Kept (counts towards the "legally" cap). |
| Trade a Mark. Trade with Mark. | Make your mark. Trade on it. | Trademark assignment and licence | Original reads as a name ("Mark"). |
| Get identified. | Get identified. | Trademark registration | Kept. |
| Apply professionally. Offer legally. | Apply professionally. Offer clearly. | Offer letters | Avoids a second "legally". |
| Take care, it's an annual affair. | Take care. It's an annual affair. | Annual ROC filings | Punctuation fixed. |
| Execute. Intimate. Comply. | Execute. Intimate. Comply. | Corporate compliances | Kept. |
| Create, negotiate & Sign off. | Create. Negotiate. Sign off. | Sign-off hub | Rhythm restored. |
| Build your partnership, on firm foundation. | Build your partnership on a firm foundation. | Partnership firm | Grammar fixed. |
| Make 1 + 1 = 11. | One plus one makes eleven. | Partnership deed body | Kept as a body line. |
| Run the one man show. | Run the one-person show. | OPC | Gender-neutral, matches the law's name. |
| Multiply power. | Multiply power. | Partnership registration | Kept. |
| Get trusted | Get trusted. | Trust registration | Full stop added. |
| Gift with Love and Law. | Gift with love. And law. | Gift deed | Rhythm. |
| Divide with Rules. | Divide by the rules. | Partition | Idiom fixed. |
| Seniority at priority. | Seniority, at priority. | Senior citizens | Kept. |
| Pay. Save. / File. Smile. | Pay. Save. / File. Smile. | Tax pages | Kept. |
| Write & Claim on papers, driven by Law. | Drive safe. Paper safer. | Motor vehicles hub | Original was unclear. |
| Sale and purchase with security of Law. | Buy the house. Not the dispute. | Sale and purchase hub | Sharper. |
| Take the first step to raise any grievance. | Say it once. Say it in a notice. | Legal notices | Sharper. |
| Created in minutes. Approved in seconds. | Create with ease. Exit with peace. | Distributorship, franchise | Speed claims removed (NN-20). |
| Fold your business and double the money. | Merge right. Grow together. | M&A | "Fold" means close down. |
| Get out of the trouble. Or say it, 'Get out'. | Part ways. Keep the peace. | Divorce | Sensitive category. |
| Conflict is inevitable, but combat is optional. | Talk it out. Sign it off. | Mediation, arbitration | Borrowed quotation (R5 §6.1). |
| Competition makes us faster, collaboration makes us better. | Two logos. One rulebook. | Collaboration | Circulating quotation. |
| Write everything except love-letters. | We draft everything except love letters. | Home (playful strip) | `[OWNER]` to approve tone. |

### 2.8 One-liner bank (112 lines, original)

Use one line per page as the eyebrow and, if needed, one inside the body. Lines marked * reuse or adapt the R5 §6.2 bank, which was written for this pack.

**A. Brand and home**

| # | Line | CTA |
|---|---|---|
| 1 | Draft it. Sign it. Keep it.* | Start a document, now. |
| 2 | Your agreements, in your pocket.* | Open your vault, now. |
| 3 | Neutral by design. Fair by default.* | — |
| 4 | Paperwork, minus the paper.* | — |
| 5 | Legal work, without the waiting room. | — |
| 6 | One app. Every agreement. | Get started, now. |
| 7 | From first draft to last renewal. | — |
| 8 | Know what you sign. Keep what you signed. | — |

**B. Vidhi AI**

| # | Line | CTA |
|---|---|---|
| 9 | Ask Vidhi. Then decide.* | Ask, now. |
| 10 | First draft free. Final word yours.* | Draft free, now. |
| 11 | Speak your terms. Vidhi writes them.* | — |
| 12 | AI drafts. Experts check. You sign.* | — |
| 13 | Every clause, explained. | — |
| 14 | Plain answers. Real sources. | — |
| 15 | Your language in. Clean draft out. | — |

**C. eSign and eStamp**

| # | Line | CTA |
|---|---|---|
| 16 | One OTP. One recognised signature. | eSign, now. |
| 17 | Stamp first. Sign next. Sleep well. | Stamp it, now. |
| 18 | Signed from anywhere. Proven everywhere. | — |
| 19 | Duty at actuals. Not a rupee more. | — |
| 20 | Check before you sign. | Check eligibility, now. |
| 21 | Ink where the law insists. eSign where it allows. | — |

**D. Legal Vault and data**

| # | Line | CTA |
|---|---|---|
| 22 | Store once. Find it fast.* | — |
| 23 | Every deed, one drawer.* | — |
| 24 | Leave anytime. Take everything.* | Export, now. |
| 25 | Share a page. Not the whole file. | — |
| 26 | Originals locked. Copies labelled. | — |
| 27 | Your family's papers, finally in one place. | — |

**E. Negotiation and contracts**

| # | Line | CTA |
|---|---|---|
| 28 | Terms first. Trust follows.* | — |
| 29 | Deal fair. Draft fairer.* | Strike the deal, now. |
| 30 | Redline, not red tape. | — |
| 31 | Every change, on record. | — |
| 32 | Agree in writing. Disagree in comments. | — |
| 33 | Scope it. Then ship it.* | — |
| 34 | Create with ease. Exit with peace. | — |

**F. Property**

| # | Line | CTA |
|---|---|---|
| 35 | Own the land. Own the papers.* | — |
| 36 | Rent right. Live light.* | Draft the rent agreement, now. |
| 37 | Buy the house. Not the dispute.* | Draft the agreement, now. |
| 38 | Brick by brick. Clause by clause.* | — |
| 39 | Booked a flat? Book your rights.* | — |
| 40 | Eleven months, done right. | — |
| 41 | Token paid? Terms written. | — |

**G. Family and personal**

| # | Line | CTA |
|---|---|---|
| 42 | Settle hearts. Then settle papers.* | — |
| 43 | Two families. One record.* | Register, now. |
| 44 | The child first. Always.* | — |
| 45 | Respect, with remedies.* | — |
| 46 | Your wishes. Your words. Your will.* | — |
| 47 | Pass the legacy, not the litigation.* | — |
| 48 | Hand over power. Not control.* | — |

**H. Money, loans and vehicles**

| # | Line | CTA |
|---|---|---|
| 49 | Money talks. Paper proves.* | — |
| 50 | Lend with proof. Borrow with clarity.* | — |
| 51 | Every rupee, on record.* | — |
| 52 | Promise the risk. Price the risk.* | — |
| 53 | Use it now. Own it later.* | — |
| 54 | Sell the car. Keep the proof.* | Draft the sale agreement, now. |
| 55 | Keys handed over. Time noted. | — |

**I. Business, startups and companies**

| # | Line | CTA |
|---|---|---|
| 56 | Idea today. Entity tomorrow.* | Plan it, now. |
| 57 | Founders agree first. Investors follow.* | Draft the founders' agreement, now. |
| 58 | Raise money. Not disputes.* | — |
| 59 | Board-ready. Auditor-ready.* | — |
| 60 | Run the firm by the book. Literally.* | — |
| 61 | Register today. Rule tomorrow.* | Incorporate, now. |
| 62 | Split the equity. Not the team. | — |
| 63 | Vest in the vision. | — |
| 64 | Your legal desk, from day one. | Meet the Startup Desk, now. |

**J. Employment and HR**

| # | Line | CTA |
|---|---|---|
| 65 | Hire on paper. Part by the book.* | — |
| 66 | Offer clearly. Retain gladly.* | Draft the offer, now. |
| 67 | Fair wage. Firm terms.* | — |
| 68 | Remote work. Real terms.* | — |
| 69 | Day one, documented. | — |
| 70 | Secrets stay. People move on. | — |

**K. Confidentiality and IP**

| # | Line | CTA |
|---|---|---|
| 71 | Share the idea. Not the ownership. | Draft the NDA, now. |
| 72 | Talk freely. Sign first. | — |
| 73 | Own the idea. Officially.* | — |
| 74 | Your brand. Nobody else's.* | File, now. |
| 75 | Filed. Tracked. Registered.* | Track, now. |
| 76 | Create. Register. Royalty.* | — |
| 77 | Invent once. Earn often.* | — |
| 78 | Watch the Journal. So you don't have to. | — |

**L. Notices, disputes and courts**

| # | Line | CTA |
|---|---|---|
| 79 | Say it once. Say it in a notice.* | Send the notice, now. |
| 80 | Answer back. On record.* | — |
| 81 | Thirty days to act. Don't spend them waiting. | — |
| 82 | Your case, in the court's language.* | Draft the plaint, now. |
| 83 | Liberty deserves good drafting.* | — |
| 84 | Plead it right the first time.* | — |
| 85 | Talk it out. Sign it off.* | — |
| 86 | Private forum. Binding award.* | — |
| 87 | Swear by it. Properly.* | — |
| 88 | Paid for it? Claim for it.* | — |

**M. Trackers**

| # | Line | CTA |
|---|---|---|
| 89 | Every hearing, on your radar.* | Add a case, now. |
| 90 | Next date. Next step. No surprises. | — |
| 91 | All your cases. One calendar. | — |
| 92 | Deadlines don't hide here. | — |

**N. Compliance and GRC**

| # | Line | CTA |
|---|---|---|
| 93 | Comply quietly. Grow loudly.* | — |
| 94 | Due dates, never overdue.* | — |
| 95 | Your RBI calendar, organised every quarter.* | Talk to the GRC team, now. |
| 96 | Policies that pass the inspection. | — |
| 97 | Minutes that matter.* | — |
| 98 | Resolve. Record. Report.* | — |
| 99 | File on time. Sleep on time.* | — |
| 100 | Close the books. Close the chapter.* | — |

**O. Marketplace, retainers and academy**

| # | Line | CTA |
|---|---|---|
| 101 | Expert eyes. Fixed price.* | Hire a professional, now. |
| 102 | A lawyer when it matters. Not before.* | — |
| 103 | Pick a service. Know the price. | — |
| 104 | A legal team on retainer. Not on payroll.* | Ask for a retainer, now. |
| 105 | Your maker. Your checker. Your call. | — |
| 106 | Practise before you practise.* | Explore courses, now. |

**P. Pricing**

| # | Line | CTA |
|---|---|---|
| 107 | Free to start. Fair to grow. | Start free, now. |
| 108 | The full price. Before you pay. | — |
| 109 | Cancel in two taps. Keep your files. | — |

**Q. Consumer Help brand**

| # | Line | CTA |
|---|---|---|
| 110 | Rejected? You can still escalate.* | Start your complaint, now. |
| 111 | Complain in order. Escalate on time. | — |
| 112 | Challan received. Options explained. | Check your options, now. |

---

## 3. Global page elements

Deck references GB-01 to GB-14 identify the reusable blocks. The CMS stores each as a component with its own version and reviewer (NN-30).

### 3.1 Header and navigation (GB-01)

**Primary navigation (desktop):**

| Label | Mega-menu groups (label → destination) |
|---|---|
| Documents | Property · Family · Business and deals · Employment · Money and loans · IP and brands · Notices and disputes · Court pleadings · All documents (A–Z) |
| Sign and stamp | Aadhaar eSign · eStamp · Signing for teams · Check if your document can be eSigned |
| Legal Vault | Personal vault · Company document management · Import from DigiLocker · Export your data |
| Trackers | Case tracker · Trademark tracker · Renewals and obligations |
| Business | Startup Desk · Start a business · Compliance services · Company legal department · Regulated entities (RBI, SEBI, IRDAI, IFSCA) |
| Experts | Services marketplace · Retainers · Book a consultation · FinLegal Academy |
| Pricing | — |

**Utility navigation:** Ask Vidhi · Log in · **Start free** (primary button).

**Mobile:** hamburger opens the same groups as accordions. App tab bar (logged in): Home · Documents · Vault · Vidhi · Account.

**Search box placeholder:** "Search documents, e.g. rent agreement, NDA, legal notice"

**Language switcher label:** "Language" (lists the ten launch languages by their own names, e.g. हिन्दी, বাংলা, मराठी — D-07).

**Skip link (first focusable element):** "Skip to main content".

### 3.2 Footer (GB-02)

| Column | Links |
|---|---|
| Product | Vidhi AI · Aadhaar eSign · eStamp · Legal Vault · Case tracker · Trademark tracker · Mobile apps · Pricing |
| Documents | Rent agreement · Agreement to sell · Vehicle sale agreement · NDA · Offer letter · Partnership deed · Legal notice · All documents |
| Business | Startup Desk · Start a business · Compliance services · Regulated entities · Retainers · Services marketplace |
| Learn | Blog · Videos · Help centre · Tutorials · Legal glossary · FinLegal Academy |
| Company | About · Careers · Contact · Partners · Press · Infrabyx Group |
| Legal | Terms of Use · Privacy Notice · Cookie Policy · Refund and Cancellation Policy · Disclaimer · eSign Terms · Marketplace Terms · Acceptable Use Policy · **Grievance Officer** · Accessibility Statement |

**Legal-entity block (renders from Super Admin → Legal entities, D-08):**

> lawdocs.in is operated by [LawDocs Operating Entity], CIN [●], GSTIN [●]. Registered office: [●].
> **Grievance Officer:** [Name], [email], [phone]. We acknowledge complaints within 24 hours and resolve them within 7 days [VERIFY: IT Rules 2021 r.3(2) as amended 2026 — R3 LG-077]. Consumer complaints about purchases are acknowledged within 48 hours and resolved within one month (Consumer Protection (E-Commerce) Rules 2020, r.4(5) — R3 LG-141).
> **Data protection contact:** [DPO name], [email].

**Footer disclaimer (always visible):**

> LawDocs is a technology platform. It is not a law firm and does not give legal advice. Legal advice and representation are provided by independent advocates in their own name, under their own engagement terms. Information on this site is general and is not a substitute for advice on your facts.

**Group line:** "LawDocs is part of Infrabyx Group."
**Copyright:** "© [year] [LawDocs Operating Entity]. All rights reserved."
**Contact line:** "[Public phone] · [Support email] · Offices: New Delhi · Noida · Jaipur" `[OWNER: choose one public number — R5 found three in use]`

### 3.3 CTA and interface microcopy (GB-03)

| Context | Primary | Secondary |
|---|---|---|
| Document page hero | Draft free with Vidhi | Hire a professional |
| Product page (eSign) | Sign a document | Check eligibility |
| Vault | Open your vault | See how export works |
| Trackers | Add a case / Add a trademark | See a sample tracker |
| Marketplace card | View service and price | Ask a question first |
| Retainer | Request a retainer proposal | Download sample SLA |
| Pricing card | Start free / Choose Personal / Choose Pro / Choose Business | Compare all features |
| Enterprise | Talk to us | — |

**States:**

| State | Copy |
|---|---|
| Saving | "Saving…" then "Saved [time]" |
| Draft ready | "Your draft is ready. Review each clause before you share it." |
| Sent for signing | "Sent to [name]. We'll tell you when they sign." |
| All signed | "Signed by everyone. Your evidence pack is in the vault." |
| Payment success | "Payment received. Your GST invoice is on its way to [email]." |
| Payment failed | "The payment did not go through. You have not been charged. Try again or choose another method." |
| Empty vault | "Nothing here yet. Upload a file, import from DigiLocker, or start a document." |
| Empty tracker | "No cases yet. Add one with its CNR or case number." |
| Error (generic) | "Something went wrong on our side. Your work is saved. Try again in a minute." |
| Session timeout warning | "You'll be signed out in 2 minutes to protect your account. Stay signed in?" (with extendable timer, WCAG 2.2.1) |

### 3.4 "Draft free with Vidhi" block (GB-04)

Placed on every document page, above the fold on mobile (R-087). Two modes; the label must match the mode (NN-14, CH-30).

**Block heading:** Draft free with Vidhi
**Sub-heading:** Answer a few questions. Get a clean, editable draft.

**Mode 1 — Template draft (free):**

> Vidhi fills a template written and reviewed by our legal team with your answers. You can edit every clause and see why it is there.
> **Label on output:** "Template draft · Template reviewed by [Reviewer name, qualification] on [date]"
> **What you get free:** editable draft · clause explanations · download as PDF or Word · save to your vault
> **Paid steps, shown with prices before you choose:** eStamp · Aadhaar eSign · professional review

**Mode 2 — Custom AI draft (when the user asks for changes beyond the template):**

> You asked Vidhi to write or change clauses that are not in our reviewed template. Vidhi will draft them with AI.
> **Label on output (fixed, cannot be removed by the user):** "AI draft — not reviewed by a professional"
> **Line under the label:** "AI can make mistakes. Check names, numbers and clauses. For advice on your situation, ask a professional to review this draft."
> **Button:** Get it reviewed — from ₹[OWNER TO SET]

**Form microcopy:**

| Element | Copy |
|---|---|
| Start button | Start drafting |
| Progress | Step [n] of [m] |
| Optional field hint | "Optional — leave blank if not agreed yet." |
| "i" next to a term | Opens the glossary entry (`hlp.tpl.<term>`) |
| Language choice | "Draft in: English / हिन्दी / … (translations are labelled machine translations until reviewed — NN-48)" |
| Consent line (before first AI use) | "Vidhi uses AI to draft. What you type is processed to create your document and is never used to train AI models. See our Privacy Notice." |
| Save prompt | "Save to your vault so you can finish later." |

**Disclaimer (small text, always under the block):**

> Vidhi is an AI drafting assistant, not a lawyer. Template drafts are prepared from your answers; custom AI drafts are marked as not reviewed. Neither is legal advice.

### 3.5 "Hire a professional to review" block (GB-05)

**Heading:** Want an expert to check it?
**Sub-heading:** Fixed scope. Fixed price. The full amount before you pay.

**Service tiers (seed — R6 §R6.2.5; prices `[OWNER TO SET]`):**

| Tier | What the professional does | Turnaround | Who delivers |
|---|---|---|---|
| Review | Reads your draft, marks changes, answers up to [n] questions in writing | [n] working days `[OWNER]` | Advocate (legal advice) |
| Draft and review | Prepares the document from your instructions and one round of changes | [n] working days | Advocate or company secretary, by document type |
| Draft, stamp and registration help | As above, plus stamp-duty calculation and a registration checklist; appointment help where the State allows | [n] working days | Advocate; LawDocs operations for scheduling |

**Price card (every card shows all four lines):**

| Line | Example (placeholders) |
|---|---|
| Professional's fee (paid to the professional) | ₹[●] |
| LawDocs platform fee | ₹[●] |
| GST | ₹[●] on the platform fee; on the professional's fee as applicable to the supplier `[TAX MEMO]` |
| Government fees / stamp duty (if any) | At actuals: ₹[●] |
| **Total you pay** | **₹[●]** |

**Role statement (NN-41, NN-21):**

> Legal advice comes from an independent advocate who works in their own name and is responsible for that advice. LawDocs provides the platform, scheduling, secure workspace and payment handling, and charges its own platform fee for these. LawDocs does not take a share of the advocate's fee. We assign an available professional for this fixed-price service; we do not rank or rate advocates.

**For business buyers:** "If you buy for a business, legal services from an advocate may be taxed under reverse charge, which means your business pays the GST directly. Your invoice will show this. [TAX MEMO: Notification 13/2017-CT(Rate), Sl. 2 — R3 LG-130]"

**SLA line:** "Your service terms, scope and turnaround are set out in a short engagement letter that you and the professional sign inside LawDocs."

**Refund line:** "If the professional has not started, cancel for a full refund. After work starts, our Refund Policy applies." `[OWNER: confirm refund code]`

### 3.6 Trust strip (GB-06)

Show four to six of these. Each item may be shown only when its evidence exists (§2.4). Counters stay OFF (`web.trust_strip.counters_enabled = false`) until the owner approves measured numbers.

| Item | Copy | Precondition |
|---|---|---|
| eSign | Aadhaar eSign through a CCA-licensed eSign Service Provider | ESP/aggregator contract live |
| Stamp | Stamp duty paid through authorised channels, at actuals | Channel contract live |
| Price | Full price, including GST, before you pay | Always true by design (NN-22) |
| Exit | Export everything, free, any time | Export live (P20) |
| Hosting | Stored in India | Production hosting verified |
| Payments | Card payments on Razorpay's hosted checkout | Razorpay live |
| Group | Part of Infrabyx Group | Always |
| Review | Every template reviewed by a named professional | Reviewer field populated for all published templates |

### 3.7 Testimonials (GB-07)

**Rules (NN-49, CH-20, R3 LG-143):**

1. Only genuine customers with a verified purchase or completed service. The CMS links each testimonial to an order ID and a stored consent record.
2. Never about an advocate, and never naming one (BCI Rule 36; Madras HC 2024 — R3 LG-111, LG-113). Testimonials may describe the LawDocs product, a document, or a non-legal service.
3. No photos by default; first name and initial, city, role, month and year.
4. No star ratings in structured data (R5 §7.1). No editing beyond spelling, and only with the customer's approval.
5. Disclose any incentive ("Received a ₹[●] credit for feedback").
6. Do not suppress negative feedback; moderation follows IS 19000:2022 (published policy page).
7. Testimonials block stays OFF (`web.testimonials.enabled = false`) until at least three approved testimonials exist for that page category.

**Six display formats — all PLACEHOLDER:**

> **Format T1 — short quote (document pages)**
> PLACEHOLDER — replace with genuine consented testimonials
> "[One or two sentences in the customer's own words about the document they made.]"
> — [First name + initial], [City] · [Role, e.g. tenant] · Verified purchase: [document] · [Month YYYY]

> **Format T2 — before and after (product pages)**
> PLACEHOLDER — replace with genuine consented testimonials
> **Before:** "[What the customer did before LawDocs, in their words.]"
> **After:** "[What changed, in their words. No numbers unless the customer gives and confirms them.]"
> — [First name + initial], [Role], [Company type, e.g. 20-person startup] · [Month YYYY]

> **Format T3 — company quote (Business plan, retainers)**
> PLACEHOLDER — replace with genuine consented testimonials
> "[Quote about the platform or a non-advocate service such as compliance calendar management.]"
> — [Name], [Designation], [Company name — only with written company consent] · [Month YYYY]

> **Format T4 — video transcript (vlog)**
> PLACEHOLDER — replace with genuine consented testimonials
> [Embedded video with captions] · Transcript: "[Full transcript.]" · Recorded [date] with consent · [Name or initials]

> **Format T5 — in-app feedback card**
> PLACEHOLDER — replace with genuine consented testimonials
> "[Short in-app comment selected by moderation, unchanged.]" · Verified user · [Feature] · [Month YYYY]

> **Format T6 — case study (Business and Enterprise)**
> PLACEHOLDER — replace with genuine consented testimonials
> **Customer:** [Company, with consent] · **Problem:** [their words] · **What they used:** [modules] · **Result:** [their words; any figure needs the customer's written confirmation and the evidence class MEASURED / ESTIMATED — NN-36]

### 3.8 eSign eligibility notice (GB-08)

Shown in the key-facts box of every document page and again before signing. The variant is set by the document's eligibility row (Appendix F; R5 CSV flag; R3 LG-003).

**Variant A — eSign-eligible:**

> **Can be eSigned: Yes.** This document can be signed with Aadhaar eSign or a Class 3 digital signature (IT Act 2000, ss.3, 3A and 5). If it needs stamp duty, we stamp it first.

**Variant B — eSign-eligible with conditions:**

> **Can be eSigned: Yes, with steps.** You can eSign this document, but it may also need stamp duty paid before signing, and registration with the sub-registrar if the law requires it (for example, leases over one year — Registration Act 1908, s.17). We show you the steps for your State.

**Variant C — not eSign-eligible:**

> **Can be eSigned: No.** The law does not allow electronic signatures for this type of document (IT Act 2000, s.1(4) and First Schedule — wills, trust deeds, most powers of attorney and certain negotiable instruments). Draft it here, then use our print-and-sign pack: what to print, who signs, witnesses, notary or registration.

**Before-signing check (modal):** "We checked this document against the eSign rules. Result: [A/B/C]. If you think we classified it wrongly, ask a professional before you sign."

### 3.9 Stamp-before-sign notice (GB-09)

> **Stamp first, then sign.** Stamp duty is a State tax on many documents. It must be paid before or at the time of signing (Indian Stamp Act 1899, s.17, and State Stamp Acts). An unstamped or under-stamped document cannot be used as evidence until the duty and penalty are paid (s.35). We calculate the duty for your State, buy the e-stamp certificate through an authorised channel in the first party's name, attach it, and only then open signing. You pay the duty at actuals, plus our facilitation fee shown separately.

### 3.10 AI disclaimer (GB-10)

**Short (chat header):** "Vidhi is an AI assistant. It explains and drafts; it does not give legal advice. Check important answers with a professional."

**Long (Vidhi page and Terms):**

> Vidhi is an artificial-intelligence assistant built into LawDocs. It answers general legal questions, explains clauses and prepares drafts. It can make mistakes. Every legal citation Vidhi shows is checked against our legal-rules register or a source document; if it cannot be checked, Vidhi marks it "unverified". Vidhi does not know every fact of your situation and is not a lawyer. Custom AI drafts are marked "AI draft — not reviewed by a professional" until a qualified professional reviews them. Your content is not used to train AI models. [VERIFY: final wording against the Anthropic Usage Policy disclosure requirement for legal use — R4; conventions §13.15]

**Synthetic media label (videos, voice, avatars — R3 LG-078):** "AI-generated" on screen and in metadata; audio prefix "This message uses an AI voice."

### 3.11 Cookie banner (GB-11)

**Banner (first visit; equal-weight buttons, no pre-ticked boxes — NN-50, R3 LG-141):**

> **We use cookies.** Essential cookies keep the site working and your account secure. With your permission, we also use cookies to remember your preferences and to understand how the site is used. We do not use advertising cookies on your vault, documents or cases.
> [Accept all] [Reject non-essential] [Choose cookies]

**Preferences panel:**

| Category | Default | Description |
|---|---|---|
| Essential | Always on | Sign-in, security, load balancing, your cookie choice. |
| Preferences | Off | Language, region and display settings. |
| Analytics | Off | Anonymous usage statistics to improve pages. No document content is ever collected. |
| Marketing | Off | Measures our ads on other sites. Never used on logged-in pages. |

**Panel footer:** "You can change this any time from 'Cookie settings' in the footer. Withdrawing consent is as easy as giving it (DPDP Act 2023, s.6(4))."

### 3.12 Legal information disclaimer and reviewed-by footer (GB-12)

**On every legal page, above the footer:**

> **Reviewed by** [Name], [Advocate, Enrolment No. ●, Bar Council of ●] / [ACS/FCS No. ●] · **Last reviewed** [date] · **Next review** [date] · **Legal basis:** [linked list of Act + section on India Code]
> This page gives general information about Indian law as on the review date. It is not legal advice. Laws and State rules change; check the current position before you act.

### 3.13 Privacy notice snippet for forms (GB-13)

> We use these details only to [purpose shown per form]. See our Privacy Notice for how long we keep them and how to withdraw consent. [Checkbox, unticked:] "Send me product news by email. I can unsubscribe at any time."

### 3.14 Accessibility statement teaser (GB-14)

> We build LawDocs to WCAG 2.2 AA and IS 17802 standards. If something does not work with your screen reader, keyboard or captions, tell us at [accessibility email] and we will fix it or help you complete the task another way.

---

## 4. Flagship pages (15)

Every page below follows the R5 §7.2/§7.3 templates. Global blocks (GB-xx) are inserted where shown and are not repeated in full. FAQs are visible HTML; FAQPage JSON-LD is optional and gives no Google rich result (R5 §7.1). "i" keys refer to the glossary registry (`hlp.<module>.<term>`).

---

### FP-01 — Home

| Field | Copy |
|---|---|
| URL | `/` |
| SEO title | LawDocs: Draft, eSign and Store Legal Documents Online |
| Meta description | Draft agreements free with Vidhi AI, stamp and Aadhaar eSign them, keep them in your Legal Vault and hire a professional at a fixed price. |
| Display line (above H1) | Draft it. Sign it. Keep it. |
| H1 | Draft, sign and keep your legal documents in one place |

**Answer-first summary (hero sub-text):**
LawDocs is a legal operations app for individuals and businesses in India. Draft agreements free from reviewed templates with Vidhi AI, agree changes with the other party, pay stamp duty and sign with Aadhaar eSign where the law allows, store everything in your Legal Vault, track cases and trademarks, and hire a professional at a fixed price.

**Hero buttons:** Start free · Ask Vidhi a question
**Hero search placeholder:** "What do you need? e.g. rent agreement, NDA, legal notice"
**Hero reassurance line:** "Free account. No card needed. Export your files any time."

**Section: Everything a legal document needs**

| Card | Heading | Text | Link |
|---|---|---|---|
| Draft | First draft free. Final word yours. | Answer a few questions. Vidhi fills a template reviewed by our legal team. Every clause comes with a plain-English reason. | Browse documents |
| Negotiate | Terms first. Trust follows. | Invite the other party. Suggest changes in track-changes mode, comment, chat and agree — one clean version per round. | How negotiation works |
| Sign | One OTP. One recognised signature. | We check whether your document can be eSigned, stamp it first if duty is due, then collect Aadhaar eSign, DSC or wet-ink signatures. | Aadhaar eSign and eStamp |
| Store | Store once. Find it fast. | Your Legal Vault keeps originals locked, finds any clause in seconds and shares only what you choose. | Legal Vault |
| Track | Every hearing, on your radar. | Add a case or a trademark application. We remind you of the next date and the next deadline. | Trackers |
| Get expert help | Expert eyes. Fixed price. | Need judgement? Hire an advocate, company secretary or chartered accountant for a fixed-scope service. The full price shows before you pay. | Services marketplace |

**Section: Built for**

| Audience | Line | Text | Link |
|---|---|---|---|
| Individuals and families | Your family's papers, finally in one place. | Rent, property, vehicle, loans, wills and notices — drafted, signed and kept safe. Add family members to share what matters. | For individuals |
| Startups and small businesses | Your legal desk, from day one. | Founders' agreement, NDAs, offer letters, vendor contracts, trademark and incorporation — with the Startup Desk on call. | Startup Desk |
| Companies and legal teams | Board-ready. Auditor-ready. | Contract lifecycle, maker-checker approvals, case management, board minutes and an audit trail nobody can edit. | For companies |
| NBFCs and regulated entities | Your RBI calendar, organised every quarter. | Policies, compliance testing, risk assessment and board support from our GRC professionals, with LawDocsComply for software-led compliance. | Regulated entities |
| Professionals | Practise with better tools. | Advocates, CAs and CSs can run their own client work on LawDocs Pro. | For professionals |

**Section: How it works (ordered list)**
1. Tell us what you need, or pick a document.
2. Answer a few questions. Vidhi prepares the draft.
3. Share it with the other party and agree changes.
4. Pay stamp duty if due. Sign with Aadhaar eSign, DSC or ink.
5. Keep it in your vault. We remind you before renewals, rent increases and deadlines.

**Section: Meet Vidhi**
> **Ask Vidhi. Then decide.** Vidhi is the AI assistant inside LawDocs. Ask in English, Hindi or eight other Indian languages. Vidhi explains the law in plain words, shows where each answer comes from, drafts from our reviewed templates, and tells you when you need a professional. Vidhi is not a lawyer and says so. [GB-10 short]
> Button: Ask Vidhi

**Section: Honest about eSign**
> **Ink where the law insists. eSign where it allows.** Most agreements can be signed with Aadhaar eSign. Some cannot — wills, trust deeds and most powers of attorney, for example. LawDocs checks every document before signing and gives you a print-and-sign pack when ink is the law.
> Link: Check if your document can be eSigned

**Section: Your data, your exit**
> **Leave anytime. Take everything.** Download every document, version, signature record and invoice in plain folders that open in Word, Excel and any PDF reader. No fee, no request, no waiting.
> Link: See how export works

**Trust strip:** GB-06 (only evidenced items).
**Testimonials:** GB-07, Format T1/T3, OFF until genuine.

**Section: Plans**
> **Free to start. Fair to grow.** The Free plan keeps your vault and template drafts free, within its storage limit `[OWNER: confirm the Free plan commitment]`. Personal, Pro and Business plans add eSign credits, trackers and team tools. Every price shows GST before you pay, and you can cancel from Settings.
> Button: See pricing

**Home FAQs:**

| Q | A |
|---|---|
| What is LawDocs? | LawDocs is a legal operations app for India. You can draft legal documents, negotiate with the other party, pay stamp duty, sign with Aadhaar eSign where allowed, store documents in a Legal Vault, track cases and trademarks, and hire professionals at fixed prices. |
| Is LawDocs a law firm? | No. LawDocs is a technology platform. Legal advice and representation come from independent advocates who act in their own name. LawDocs provides the tools, the workspace and the scheduling. |
| Are documents drafted on LawDocs legally valid? | A document is valid when its contents are lawful, it is signed by the right people, and it meets formalities such as stamp duty and registration. LawDocs shows the formalities for each document and checks them before marking it complete. |
| Can I sign every document with Aadhaar eSign? | No. The IT Act 2000 (First Schedule) excludes wills, trust deeds, most powers of attorney and certain negotiable instruments. LawDocs checks this before signing and gives a print-and-sign pack for excluded documents. |
| Is Vidhi free? | Template drafting and short questions are free within your plan's monthly AI credits. Larger AI tasks, such as long reviews or translations, use credits. You see the credit cost before you start. |
| Can I take my data out if I leave? | Yes. Export everything at any time, free, as a ZIP of folders with Word, PDF, Excel and CSV files and a readable index. |

**Final CTA band:** "Draft it, now." · Button: Start free · Secondary: Talk to us (businesses)

**Related links:** Documents A–Z · Aadhaar eSign · Legal Vault · Pricing · Startup Desk · Help centre
**Schema:** Organization (name, url, logo, `sameAs` social profiles, `parentOrganization` Infrabyx Group), WebSite with SearchAction. No reviews or ratings markup.
**"i" keys:** `hlp.sgn.esign`, `hlp.sgn.estamp`, `hlp.dms.legal_vault`, `hlp.ai.vidhi`.
**Review flags:** [OWNER] approve hero and audience order; [OWNER] public phone; [VERIFY at launch] each trust-strip item; [COUNSEL] "Is LawDocs a law firm?" answer.

---

### FP-02 — Rent / Lease Agreement

| Field | Copy |
|---|---|
| URL | `/documents/property-transactions/rent/rent-agreement` (consolidates the manual's "Rent Agreement Residential" and "Rent Agreement Flat"; "Rent Agreement Commercial" stays a separate leaf) |
| SEO title | Rent Agreement Online: Draft Free, eStamp and eSign |
| Meta description | Make a rent agreement online. Draft free with Vidhi, pay stamp duty at actuals, eSign with Aadhaar and get the registration steps for your State. |
| Eyebrow | Rent right. Live light. |
| H1 | Rent Agreement — Draft Free, eStamp and eSign Online |

**Answer-first summary:**
A rent agreement is a contract in which a landlord lets a home to a tenant for rent. In law it is a lease under the Transfer of Property Act 1882 (s.105). Stamp duty is payable under State law, and a lease for more than one year, or from year to year, must be registered (Registration Act 1908, s.17).

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Transfer of Property Act 1882, ss.105–117; State rent or tenancy law; State Stamp Act |
| Stamp duty | Yes — rate set by your State |
| Registration | Compulsory if the term is more than one year or year to year (Registration Act 1908, s.17(1)(d)); some States require it for shorter terms too |
| Witnesses | Two recommended; needed for registration |
| eSign | GB-08 Variant B |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: who is the landlord and tenant; property address; furnished or not; rent and due date; deposit; start date and term; lock-in; yearly increase; notice period; who pays maintenance and utilities; pets and use restrictions).
**Professional block:** GB-05 (tiers: Review · Draft and review · Draft, stamp and registration help).

**When to use it**
- You are letting out, or renting, a flat, house, room or floor for living.
- You are renewing an expired agreement or changing the rent.
- You need a stamped record of rent and deposit for your own safety, your bank or your employer.

For a shop, office or warehouse, use the Commercial Rent Agreement. For paying-guest accommodation, use the PG Agreement.

**Rent agreement, lease or leave and licence?**

| | Rent agreement / lease | Leave and licence |
|---|---|---|
| What the occupant gets | An interest in the property for the term (TPA s.105) | Only a permission to use; no interest in the property (Indian Easements Act 1882, s.52) |
| Typical use | Homes and shops across most States | Common in Maharashtra, where it has its own registration rule [VERIFY: Maharashtra Rent Control Act 1999, s.55] |
| Registration | If over one year or year to year | Depends on State law |
| Choose it when | You want a standard tenancy | Your State practice or your housing society expects it |

**Why so many agreements run for 11 months**
The Registration Act requires registration of leases for more than one year. An 11-month term falls outside that rule, so many parties choose it and renew. It still needs stamp duty, and some States require registration whatever the term [VERIFY per State]. If you want a longer, secure tenancy, register it; we show you how. [COUNSEL: confirm wording is explanatory, not advice to avoid registration]

**Model Tenancy Act 2021**
The Central Government's Model Tenancy Act 2021 suggests limits on deposits, a written agreement and a Rent Authority. It applies only where a State adopts it in its own law [VERIFY: list of adopting States]. Vidhi applies the rules of the State you select.

**What's included**
- Parties, with addresses and ID references (Aadhaar masked to the last four digits)
- Property schedule, fittings and an inventory annexure
- Term, start date, lock-in period and renewal option
- Rent amount, due date, payment mode and late-payment terms
- Security deposit, permitted deductions and refund timeline
- Yearly increase (escalation)
- Maintenance, society charges, electricity, water and internet
- Repairs: who fixes what, and how quickly
- Use, guests, pets and subletting (only with written consent)
- Landlord's visits with prior notice
- Ending early: notice period and lock-in consequences
- Handover condition and joint inspection
- Police verification cooperation, where your city requires it
- Disputes: talk first, then mediation (option to use Equator), then courts with jurisdiction
- Signatures and witnesses

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Landlord | Identity proof; address proof; PAN (needed where the tenant must deduct tax on high rent [VERIFY: threshold and section under the Income-tax Act 2025]); proof of ownership or right to let (sale deed, allotment letter or property-tax receipt); society NOC if your society asks |
| Tenant | Identity proof; current address proof; passport-size photographs (for registration) |
| Company as tenant | Board resolution or authorisation letter for the signatory; company PAN and GSTIN if applicable |
| Both | Two witnesses with identity proof (for registration); e-stamp certificate; registration-fee receipt where registered |

**How it works**
1. Answer the questions. Vidhi prepares the draft.
2. Read each clause; tap "i" for the reason behind it.
3. Invite the other party to review. Agree changes in track-changes mode.
4. Pay stamp duty: we buy the e-stamp certificate for your State through an authorised channel.
5. Both parties sign with Aadhaar eSign. Witnesses can eSign too.
6. If registration is needed, book the sub-registrar appointment or use your State's online registration where available.
7. Your signed agreement and evidence pack go to your vault. We remind you before the rent increase, renewal and deposit refund.

**State, stamp and registration notes**
Stamp duty and registration rules differ by State and change often. The CMS renders this table from the State rules register; each row shows its source and "verified on" date.

| State | Duty basis | Registration rule | e-stamp channel | Status |
|---|---|---|---|---|
| Delhi | [VERIFY] | Registration Act s.17 | SHCIL e-stamp [VERIFY] | [VERIFY] |
| Maharashtra | Leave and licence: State schedule [VERIFY] | Registration of leave and licence agreements [VERIFY: MRC Act s.55]; online registration available [VERIFY] | GRAS / e-SBTR / franking [VERIFY] | [VERIFY] |
| Karnataka | [VERIFY] | s.17 | SHCIL with Kaveri [VERIFY] | [VERIFY] |
| Uttar Pradesh | [VERIFY] | State tenancy law 2021 [VERIFY] | SHCIL [VERIFY] | [VERIFY] |
| Rajasthan | [VERIFY] | s.17 | [VERIFY] | [VERIFY] |
| Tamil Nadu | [VERIFY] | Registration of tenancy with the Rent Authority under State law [VERIFY] | [VERIFY] | [VERIFY] |
| Haryana | [VERIFY] | s.17 | SHCIL; State e-stamp rules 2017 [VERIFY] | [VERIFY] |
| Telangana | [VERIFY] | s.17 | [VERIFY] | [VERIFY] |

Under-stamping has a cost: an unstamped or under-stamped agreement cannot be relied on in evidence until the duty and a penalty are paid (Indian Stamp Act 1899, s.35, and State equivalents). An unregistered lease that needed registration cannot be used to prove the lease terms (Registration Act 1908, s.49).

**eSign eligibility:** GB-08 Variant B. A lease is not excluded by the IT Act First Schedule, so it can be eSigned once stamped. Registration, where needed, follows the sub-registrar's process for your State.

**FAQs**

| Q | A |
|---|---|
| Is an online rent agreement legally valid? | Yes, if it is stamped as your State requires and signed by both parties. Aadhaar eSign is a legally recognised signature (IT Act 2000, s.5). If the term is over one year, it must also be registered (Registration Act 1908, s.17). |
| Do I need to register an 11-month rent agreement? | Usually not under the Registration Act, because the term is not more than one year. Some States require registration of all tenancy or leave-and-licence agreements [VERIFY per State]. Stamp duty is still payable. |
| Who pays the stamp duty? | Whoever the agreement says. If it is silent, the Indian Stamp Act puts it on the tenant (s.29(c)); State Acts may differ [VERIFY per State]. |
| How much security deposit can a landlord ask for? | No central limit applies everywhere. The Model Tenancy Act 2021 suggests up to two months' rent for homes, but only in States that adopt it [VERIFY]. Otherwise it is what the parties agree. |
| Can the landlord raise the rent mid-term? | Only as the agreement allows, usually through a yearly escalation clause, or as your State's rent law permits. |
| Is tenant police verification compulsory? | Many cities require it under local police orders [VERIFY per city]. The agreement includes a cooperation clause, and we link to your State police's online form where one exists. |
| Can a rent agreement be used as address proof? | Many service providers accept a stamped agreement, and some insist on a registered one. Check the accepted-documents list of the authority you are applying to. |
| How is the deposit refunded? | As the agreement says: usually after handover, less unpaid dues and damage beyond normal wear and tear. We remind both parties of the refund date. |

**Related:** Commercial rent agreement · Leave and licence agreement · Notice to tenant · Rent receipt · Suit for eviction (Pleadings) · Registration assistance (service)
**Schema:** WebPage + BreadcrumbList; Service (document drafting) with Offer only for live prices; optional FAQPage.
**"i" keys:** `hlp.tpl.lock_in`, `hlp.tpl.escalation`, `hlp.sgn.stamp_duty`, `hlp.sgn.registration`, `hlp.tpl.leave_and_licence`.
**Review flags:** [COUNSEL] 11-month paragraph; [VERIFY] every State row, Model Tenancy Act adoption, TDS threshold, police-verification rule; manual text "blockchain and Smart Contracts", "None of the party can make default" and "home delivery" removed (unevidenced).

---

### FP-03 — Agreement to Sell (immovable property)

| Field | Copy |
|---|---|
| URL | `/documents/property-transactions/sale-and-purchase/agreement-to-sell` (variants as toggles: flat, house, plot, commercial; consolidates four manual leaves) |
| SEO title | Agreement to Sell Property: Draft, Stamp and eSign |
| Meta description | Draft an agreement to sell a flat, house or plot. Know the stamp duty, registration and eSign rules, and why only a registered sale deed transfers title. |
| Eyebrow | Buy the house. Not the dispute. |
| H1 | Agreement to Sell a Property — Draft, Stamp and Sign |

**Answer-first summary:**
An agreement to sell is a contract in which a seller promises to sell, and a buyer promises to buy, an immovable property on agreed terms. It does not transfer ownership; only a registered sale deed does (Transfer of Property Act 1882, s.54). Stamp duty applies, and registration may be compulsory.

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Transfer of Property Act 1882 (ss.53A, 54, 55); Indian Contract Act 1872; Specific Relief Act 1963; State Stamp Act; Registration Act 1908 |
| Transfers ownership? | No. The sale deed does, once registered. |
| Stamp duty | Yes — State rate; higher in some States if possession is given [VERIFY] |
| Registration | Compulsory if it supports possession under part performance (Registration Act s.17(1A)); some States go further [VERIFY] |
| eSign | GB-08 Variant B (see note below) |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: sellers and buyers, including co-owners; property details; price; advance or earnest money; payment schedule; home loan; date for sale deed; possession; title documents to hand over; who pays which costs).
**Professional block:** GB-05, plus a fourth tier "Title check before you pay" (advocate reviews the title chain and encumbrance certificate) — price `[OWNER TO SET]`.

**Agreement to sell or sale deed?**

| | Agreement to sell | Sale deed |
|---|---|---|
| Purpose | Fixes the terms and timeline of a future sale | Completes the sale and transfers ownership |
| Ownership passes? | No | Yes, on registration |
| Stamp duty | Lower in most States; conveyance-level in some where possession is given [VERIFY] | Full conveyance duty on market value or price, whichever the State prescribes |
| Registration | When s.17(1A) or State law requires | Always for property worth ₹100 or more (TPA s.54; Registration Act s.17(1)(b)) |
| Can it be eSigned? | Yes, since the 2022 amendment [VERIFY] | Execution and registration follow your State's sub-registrar process |

**Check the title before you pay**
- The chain of title documents for the property, usually going back several transfers [COUNSEL: recommended look-back period].
- An encumbrance certificate from the sub-registrar for the same period.
- Mutation in municipal or revenue records, and paid property tax.
- Approved building plan and occupancy or completion certificate for a flat or house.
- Any home loan on the property and the lender's closure plan.
- Housing society NOC and share certificate, where applicable.
- Sales through a "GPA", agreement to sell or will do not pass title by themselves (*Suraj Lamp & Industries v. State of Haryana*, Supreme Court, 2011) [VERIFY citation].

**Buying from a builder?**
The Real Estate (Regulation and Development) Act 2016, s.13, bars a promoter from taking more than 10% of the cost of a flat, plot or building as an advance without first entering into a registered written agreement for sale. Most States prescribe a model form under their RERA rules [VERIFY per State]. Use the builder's RERA-registered project number in the agreement and check it on your State RERA website.

**What's included**
- All sellers and buyers, including every co-owner and their consent
- Property schedule with boundaries, area and survey or unit number
- Price, earnest money and payment schedule through bank channels
- Seller's title warranties and duty to disclose defects (TPA s.55)
- List of original documents to be handed over at the sale deed
- Clearance of loans, charges and dues before the sale deed
- Tax deduction by the buyer where the law requires it [VERIFY: section and threshold under the Income-tax Act 2025]
- Date for executing the sale deed and handing over possession
- Who pays stamp duty, registration fees and society transfer charges
- What happens on default: refund with interest, reasonable forfeiture of earnest money, or specific performance
- Risk of loss before handover
- Disputes: mediation first (option to use Equator), then courts with jurisdiction
- Signatures and two witnesses

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Seller | Title deed and earlier chain documents; encumbrance certificate; mutation record; latest property-tax and utility receipts; approved plan and occupancy certificate (built property); society NOC or share certificate; loan statement and closure letter if mortgaged; identity proof; PAN |
| Buyer | Identity proof; PAN or the declaration the law allows instead [VERIFY: Income-tax Rules 2026]; address proof; photographs for registration; proof of each payment |
| Company or LLP | Board or partners' resolution authorising the sale or purchase; authorised signatory's identity proof |
| Agricultural land | Permission or NOC required by State land laws for the buyer [VERIFY per State] |

**How it works**
1. Optional: order a title check from a professional.
2. Answer the questions. Vidhi drafts the agreement for your State.
3. Share with the other side; agree changes in track-changes mode.
4. Pay stamp duty through an authorised e-stamp channel.
5. Sign — Aadhaar eSign where accepted [VERIFY], or print-and-sign — with two witnesses.
6. Register the agreement if your facts or your State require it.
7. Pay instalments as agreed; record each payment in the vault.
8. Execute and register the sale deed at the sub-registrar. We prepare the draft deed and the registration pack.
9. Apply for mutation. Keep every document in your vault.

**State, stamp and registration notes**
- Stamp duty is levied by each State on agreements to sell and sale deeds, often with different rates for women buyers, joint owners and rural or urban property [VERIFY per State].
- In some States an agreement to sell that gives possession is charged like a conveyance [VERIFY: e.g., Maharashtra Stamp Act, Sch. I, Art. 25 explanation].
- The draft Registration Bill 2025 proposes making all agreements to sell compulsorily registrable (R3 LG-105). It is not law yet [VERIFY status before publishing].
- State table: same structure as FP-02, rendered from the State rules register.

**eSign eligibility:** Since the 2022 amendment to the IT Act First Schedule (notification S.O. 4720(E) [VERIFY: Gazette date]), contracts for the sale or conveyance of immovable property are no longer excluded from electronic signature by the IT Act First Schedule (R3 LG-003). An agreement to sell can therefore be eSigned once it is stamped [VERIFY: R5 inventory still flags these documents "Not valid" — update the eligibility row after counsel sign-off]. The sale deed must be registered; whether your sub-registrar accepts an electronically signed deed depends on the State's e-registration system [VERIFY per State]. By default we plan the sale deed for signing at the sub-registrar's office.

**FAQs**

| Q | A |
|---|---|
| Does an agreement to sell make me the owner? | No. It gives you a right to have the sale completed on the agreed terms. Ownership passes only through a registered sale deed (Transfer of Property Act 1882, s.54). |
| Is registering an agreement to sell compulsory? | It is compulsory if the agreement lets the buyer take possession in part performance (Registration Act 1908, s.17(1A); TPA s.53A). Some States require registration in more cases [VERIFY per State]. |
| How much stamp duty is payable? | It depends on your State and on whether possession is handed over. Vidhi shows the rate and its source for your State before you pay [VERIFY State tables]. |
| Can I eSign an agreement to sell? | Yes. Since the 2022 amendment to the IT Act First Schedule, property sale contracts are no longer excluded [VERIFY]. It must be stamped first, and registered where required. |
| What if the seller refuses to complete the sale? | You can ask the court to order specific performance (Specific Relief Act 1963, s.10, as amended in 2018). The suit is usually due within three years of the date fixed for the sale or of the refusal (Limitation Act 1963, Sch., Art. 54). |
| Can the seller keep my advance if I back out? | Only if the agreement provides for it, and only a reasonable earnest-money amount; courts can refuse forfeitures that act as a penalty (Indian Contract Act 1872, s.74). |
| Is a property bought through a GPA valid? | A general power of attorney, agreement to sell or will does not transfer title by itself; the Supreme Court said so in *Suraj Lamp* (2011) [VERIFY citation]. Insist on a registered sale deed. |
| I am buying from a builder. What changes? | RERA s.13 bars the builder from taking more than 10% of the price before a registered agreement for sale. Check the project's RERA registration first. |

**Related:** Sale deed · Receipt for sale consideration · Title check (service) · Gift deed · Legal notice for refund of advance · Suit for specific performance (Pleadings)
**Schema:** WebPage + BreadcrumbList; Service; optional FAQPage.
**"i" keys:** `hlp.tpl.earnest_money`, `hlp.tpl.part_performance`, `hlp.sgn.registration`, `hlp.tpl.encumbrance_certificate`, `hlp.tpl.mutation`.
**Review flags:** [COUNSEL] eSign paragraph and the R5 CSV conflict; [VERIFY] Suraj Lamp citation, State duty treatment, TDS section, Registration Bill status; [COUNSEL] title look-back period. Manual claims "legally complied which may be produced before any Court" removed.

---

### FP-04 — Vehicle Sale Agreement

| Field | Copy |
|---|---|
| URL | `/documents/financial-transactions/sale-of-goods/vehicle-sale-agreement` (301 from the manual's "agreement-for-sale-of-car") |
| SEO title | Vehicle Sale Agreement for Car or Bike: Draft Free |
| Meta description | Sell a used car or bike safely. Draft a vehicle sale agreement free, add a time-stamped delivery note, eSign it and track the RC transfer deadline. |
| Eyebrow | Sell the car. Keep the proof. |
| H1 | Vehicle Sale Agreement — Sell Your Car or Bike Safely |

**Answer-first summary:**
A vehicle sale agreement records the sale of a used car, motorcycle or commercial vehicle: the price, the exact date and time of handover, the vehicle's condition and who is responsible for what. Ownership in the registration certificate changes only when the registering authority records the transfer on Vahan (Motor Vehicles Act 1988, s.50).

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Sale of Goods Act 1930; Motor Vehicles Act 1988, s.50; Central Motor Vehicles Rules 1989 (Forms 28, 29, 30, 35) |
| Transfers RC ownership? | No — the RTO does, on application |
| Transfer deadline | Seller reports within 14 days (same State) or 45 days (other State); buyer reports within 30 days (Motor Vehicles Act 1988, s.50(1)) [VERIFY: s.50 and CMVR] |
| Stamp duty | Depends on the State [VERIFY] |
| eSign | GB-08 Variant A for the agreement; RTO forms follow the RTO's process |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: seller and buyer; registration number; chassis and engine number; make, model, year; odometer reading; price and payment mode; handover date and time; loan on the vehicle; known defects; accessories and documents handed over).
**Professional block:** GB-05 (Review · Draft and review). Disputes after sale: "Hire an advocate".

**Why the handover time matters**
Challans, tolls and accident claims after you hand over the keys should be the buyer's responsibility. Until the RC is transferred, records still show you as the owner, and you may have to prove the handover [VERIFY: case law on registered-owner liability]. The agreement and a delivery note with the date, time and odometer reading give you that proof.

**Before you sell: checklist**
- Pending challans: check on the official e-challan portal and settle them there.
- Loan on the vehicle: close it, get the lender's NOC and Form 35 signed, and have the hypothecation removed.
- Valid insurance and PUC certificate.
- Road tax paid; no blacklisting or theft report on the vehicle.
- Original RC, spare key, service records and accessories ready.

**After you sign: transfer steps**
1. Seller and buyer sign Form 29 (notice of transfer) and Form 30 (application for transfer).
2. If the buyer is in another State or RTO area, the seller obtains a NOC in Form 28.
3. The buyer applies on Vahan with the fee and uploads the forms; some States still need a visit to the RTO [VERIFY per State].
4. The buyer transfers the insurance into their name [VERIFY: MV Act s.157 timeline].
5. Keep the new RC copy in your vault. If the transfer is not done in time, we draft a protective intimation to the RTO for the seller [VERIFY State practice].

**What's included**
- Seller and buyer details
- Vehicle particulars: registration, chassis and engine numbers, make, model, colour, year, odometer
- Price, payment method and receipt (bank transfer recommended; LawDocs does not hold payments)
- Date and time of delivery, with a delivery-note annexure
- Condition "as is", with disclosed defects and accident history
- Documents and items handed over
- Seller's warranty: clear title, no undisclosed loan, no pending challans at handover
- Liability cut-off: challans, accidents and claims after handover belong to the buyer
- Cooperation on Forms 29/30 and the transfer deadline
- Insurance transfer
- Indemnity for each side's period of possession
- Disputes and jurisdiction

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Seller | Original RC; identity and address proof; insurance certificate; PUC; NOC and Form 35 if the vehicle had a loan; Form 28 if needed |
| Buyer | Identity and address proof; passport-size photographs [VERIFY RTO]; insurance in the buyer's name |
| Both | Signed Forms 29 and 30; delivery note with time; payment proof (UTR or cheque number) |

**How it works**
1. Run the pre-sale checklist.
2. Draft the agreement with Vidhi.
3. Agree the terms and price.
4. Pay stamp duty if your State charges it [VERIFY].
5. Both parties eSign.
6. Buyer pays seller directly; record the UTR.
7. Hand over the vehicle; both sign the time-stamped delivery note with odometer and key photos.
8. Pre-filled Forms 29/30 are generated for the RTO.
9. Track the transfer deadline; close when the new RC is issued.

**State, stamp and registration notes**
Whether a vehicle sale agreement attracts stamp duty, and at what rate, depends on the State's schedule — some treat it as a general agreement, some as a transfer of movable property [VERIFY per State]. Vahan online services differ by State; some RTOs still require physical submission. No registration with a sub-registrar is needed.

**eSign eligibility:** GB-08 Variant A. The sale agreement and delivery note can be eSigned. Forms 29 and 30 are submitted as your RTO accepts them; Vahan uses an OTP to the owner's registered mobile.

**FAQs**

| Q | A |
|---|---|
| Does the sale agreement transfer the RC? | No. The registering authority transfers ownership on Vahan after the buyer applies with Forms 29 and 30 (Motor Vehicles Act 1988, s.50). The agreement proves the sale and the handover time. |
| How soon must the RC be transferred? | The seller must report the transfer within 14 days if the vehicle is registered in the same State, or within 45 days if it is registered in another State; the buyer must report it within 30 days (Motor Vehicles Act 1988, s.50(1)) [VERIFY: s.50 and CMVR]. On Vahan both usually file together. Late fees apply. |
| Who pays challans issued after the sale? | Under the agreement, the buyer pays for anything after the handover time. Because challans go to the registered owner until transfer, keep the delivery note and raise a grievance on the e-challan portal if needed. |
| My car has a loan. Can I sell it? | Yes, after you close the loan or agree how it will be closed. Get the lender's NOC and Form 35. Lenders must release documents within 30 days of full repayment [VERIFY: applicability of RBI directions to vehicle loans]. |
| Is stamp duty payable on a vehicle sale agreement? | It depends on your State [VERIFY]. Vidhi shows your State's rule before signing. |
| Can I sell to a buyer in another State? | Yes. Get a NOC in Form 28 from your RTO. The buyer then registers the transfer in their State within the deadline [VERIFY]. |
| What about insurance? | The policy must be transferred to the buyer; the buyer applies to the insurer [VERIFY: MV Act s.157 timeline]. Without it, claims can be refused. |
| Does LawDocs hold the payment? | No. The buyer pays the seller directly by bank transfer. Record the transaction reference in the agreement or receipt. |

**Related:** Delivery note · Receipt of payment · Form 29/30 checklist · Challan help (Consumer Help) · Loan closure and NOC request letter · Legal notice to buyer for non-transfer
**Schema:** WebPage + BreadcrumbList; Service; optional FAQPage.
**"i" keys:** `hlp.chp.form_29_30`, `hlp.chp.hypothecation`, `hlp.chp.vahan`, `hlp.tpl.delivery_note`.
**Review flags:** [VERIFY] transfer deadlines, insurance timeline, State stamp treatment, registered-owner liability case law, lender NOC rule.

---

### FP-05 — Non-Disclosure Agreement (NDA)

| Field | Copy |
|---|---|
| URL | `/documents/deals-and-agreements/contracts-and-agreements/non-disclosure-agreement` (from the manual's "confidentiality-and-non-disclosure-agreement") |
| SEO title | Non-Disclosure Agreement (NDA): Draft Free and eSign |
| Meta description | Create a mutual or one-way NDA for a pitch, vendor or new hire. Draft free with Vidhi, decide what stays secret and for how long, then eSign. |
| Eyebrow | Share the idea. Not the ownership. |
| H1 | Non-Disclosure Agreement (NDA) — Mutual or One-Way |

**Answer-first summary:**
A non-disclosure agreement (NDA) is a contract in which one or both parties promise to keep shared information confidential and to use it only for an agreed purpose. In India it is enforced under the Indian Contract Act 1872: the injured party can claim damages (s.73) and ask the court for an injunction (Specific Relief Act 1963).

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Indian Contract Act 1872; Specific Relief Act 1963; DPDP Act 2023 where personal data is shared |
| Stamp duty | Usually the State's general "agreement" rate [VERIFY per State] |
| Registration | Not required |
| Notarisation | Not required by law |
| eSign | GB-08 Variant A |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: mutual or one-way; parties; purpose; what is confidential; how long the duty lasts; who may receive it; personal data shared or not; return or destruction; governing law and courts).
**Professional block:** GB-05.

**Mutual or one-way?**

| | One-way NDA | Mutual NDA |
|---|---|---|
| Who shares | Only one party | Both parties |
| Typical use | A founder pitching to a vendor or freelancer; an employer sharing with a consultant | Two companies exploring a partnership, merger or joint bid |
| Balance | Protects the discloser | Same duties on both — neutral by design |

**What an NDA can and cannot do**
- It can protect business plans, source code, customer lists, pricing, designs and know-how.
- It cannot protect information that is already public, that the recipient already had, or that the recipient develops independently. These exclusions are standard and fair.
- It cannot stop someone from working for a competitor after the relationship ends. Post-term non-compete restraints are generally void in India (Indian Contract Act 1872, s.27) [VERIFY: current case law]. Use non-solicitation and confidentiality instead.
- It does not replace a trademark, copyright or patent filing.

**What's included**
- Parties and the purpose of disclosure
- Definition of confidential information, with marking and oral-disclosure rules
- Standard exclusions (public, already known, independently developed, legally required disclosure)
- Duty of care and permitted recipients (employees and advisers on a need-to-know basis)
- Personal data: lawful processing and security duties under the DPDP Act 2023
- Term of the relationship and how long confidentiality survives
- Return or destruction of information, with a certificate on request
- No licence or ownership transfer
- Non-solicitation of staff (optional, time-limited)
- Remedies: injunction and damages
- Governing law, courts or arbitration
- Electronic signature clause (IT Act 2000, ss.5 and 10A)

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Individual | Full legal name and address |
| Company or LLP | Registered name, CIN or LLPIN, registered address, signatory's name and designation, authorisation (board resolution or delegation) |
| Both | Purpose of sharing; duration; any information to exclude |

**How it works**
1. Pick mutual or one-way.
2. Answer the questions; Vidhi drafts.
3. Send it to the other party; agree changes in track-changes mode.
4. Pay stamp duty if your State requires it.
5. Both sign with Aadhaar eSign or a Class 3 DSC.
6. Stored in your vault with a reminder before the confidentiality period ends.

**State and stamp notes:** Most States charge a small fixed duty on agreements not specifically listed in their stamp schedule [VERIFY per State]. Vidhi shows the amount and source before signing. No registration is needed.

**eSign eligibility:** GB-08 Variant A.

**FAQs**

| Q | A |
|---|---|
| Is an NDA enforceable in India? | Yes. It is a contract under the Indian Contract Act 1872. If it is breached, you can seek damages and an injunction to stop further disclosure. |
| Can an NDA stop an employee from joining a competitor? | No. A restraint that applies after the employment ends is generally void under s.27 of the Indian Contract Act [VERIFY case law]. An NDA can still stop them from using or disclosing your confidential information. |
| How long should confidentiality last? | Commonly two to five years after the relationship ends; trade secrets and source code may be protected for as long as they remain secret. Choose what fits the information. |
| Do I need stamp paper for an NDA? | Most States charge a small stamp duty on agreements. Pay it before signing so the NDA can be produced in court without a penalty [VERIFY per State]. |
| Does an NDA need to be notarised? | No. Notarisation is not required for an NDA to be valid, and it does not replace stamp duty. |
| Should I ask investors to sign an NDA before a pitch? | You can ask, but many investors decline at the first meeting. Share a summary first and use an NDA before detailed data is shared. |
| What should I do if someone breaches my NDA? | Collect the evidence, send a legal notice, and consider an urgent injunction. Your evidence pack and a BSA 2023 s.63 certificate help prove the signed NDA in court. |
| Does an NDA cover personal data? | It can, but if the other party will process personal data for you, add data-processing terms that meet the DPDP Act 2023 as well. |

**Related:** Data processing agreement · Employment agreement · Founders' agreement · Consultancy agreement · Legal notice for breach of confidentiality
**Schema:** WebPage + BreadcrumbList; Service; optional FAQPage.
**"i" keys:** `hlp.tpl.confidential_information`, `hlp.tpl.non_solicitation`, `hlp.tpl.injunction`, `hlp.dms.s63_certificate`.
**Review flags:** [VERIFY] s.27 case-law line; State duty rows; [COUNSEL] "two to five years" guidance wording.

---

### FP-06 — Offer Letter and Appointment Letter

| Field | Copy |
|---|---|
| URL | `/documents/hr-and-service/job-application-and-offers/offer-and-appointment-letter` (consolidates the manual's "Offer Letter" and "Appointment letter"; each remains a toggle) |
| SEO title | Offer Letter and Appointment Letter: Draft and eSign |
| Meta description | Draft an offer letter and appointment letter in line with the Labour Codes. Set pay, probation, notice and confidentiality, then eSign with the new hire. |
| Eyebrow | Offer clearly. Retain gladly. |
| H1 | Offer Letter and Appointment Letter — Aligned to the Labour Codes |

**Answer-first summary:**
An offer letter invites a candidate to join on stated terms; an appointment letter confirms the job once the offer is accepted. The Occupational Safety, Health and Working Conditions Code 2020 requires an appointment letter for every employee (s.6(1)(f)), and pay terms must follow the Code on Wages 2019.

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Code on Wages 2019; Industrial Relations Code 2020; Social Security Code 2020; OSH Code 2020 (all in force 21 November 2025 — R3 LG-162); State Shops and Establishments Acts; Indian Contract Act 1872 |
| Stamp duty | Often treated as an agreement under State schedules [VERIFY per State] |
| Registration | Not required |
| eSign | GB-08 Variant A |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: employer and candidate; role and location; work from office, home or hybrid; joining date; pay break-up; probation; notice period; working hours and leave; confidentiality and IP; background checks; fixed-term or permanent).
**Professional block:** GB-05 (Review by an advocate · HR document pack by a company secretary).

**Offer letter or appointment letter?**

| | Offer letter | Appointment letter |
|---|---|---|
| When | Before joining | On or after joining |
| Purpose | States the main terms and asks for acceptance | Confirms employment, role, pay and service conditions |
| Legal requirement | Good practice | Required for every employee (OSH Code s.6(1)(f)) |
| Signed by | Employer; candidate accepts | Employer and employee |

**What the Labour Codes change for these letters**
- **Wages:** the Code on Wages defines "wages" so that excluded allowances above half of total pay are added back (s.2(y)). Your pay break-up affects gratuity and provident-fund calculations [VERIFY: rule-level effect with the labour rulepack].
- **Pay dates:** monthly wages are due by the 7th of the following month; full-and-final settlement within two working days of exit (Code on Wages s.17 — R3 LG-163).
- **Fixed-term employment:** allowed under the Industrial Relations Code, with gratuity after one year of service under the Social Security Code (R3 LG-165).
- **State law still applies:** Shops and Establishments Acts govern hours, holidays and leave alongside the Codes.

**What's included**
- Job title, department, reporting line, place of work and remote-work terms
- Start date and conditions precedent (documents, background check with consent)
- Pay break-up, benefits and pay date
- Probation and confirmation
- Working hours, weekly off, leave and holidays (higher of Code or State Act)
- Code of conduct, POSH policy acknowledgement and IT-use policy
- Confidentiality and assignment of work-product IP
- Non-solicitation of staff and clients (time-limited)
- Notice period, termination and full-and-final settlement
- Return of company property
- Personal-data notice for HR processing (DPDP Act 2023)
- Acceptance and electronic signature

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Employer | Legal name, address, CIN/LLPIN or registration, authorised signatory, salary structure, leave policy, POSH policy |
| Candidate | Full name, address, date of joining, ID and education proofs requested in the offer, bank details (after joining), PAN (for payroll) |

**How it works**
1. Choose offer letter, appointment letter, or both.
2. Answer the questions; Vidhi drafts using your State's leave rules.
3. Send to the candidate for acceptance by eSign.
4. Store in the employee's folder; the appointment letter is generated on joining.
5. Reminders for probation end and annual review. Company HRMS users get the record in the people file (P13).

**eSign eligibility:** GB-08 Variant A.

**FAQs**

| Q | A |
|---|---|
| Is an appointment letter compulsory? | Yes. The OSH Code 2020 requires every employer to issue an appointment letter to each employee (s.6(1)(f)). It applies from 21 November 2025, when the Labour Codes came into force. |
| Can I add a non-compete clause? | You can restrict competing work during employment. A restraint after employment ends is generally void in India (Indian Contract Act 1872, s.27) [VERIFY case law]. Use confidentiality and non-solicitation clauses instead. |
| How long can probation be? | No single central limit applies; it depends on your policy, standing orders and State law [VERIFY]. Three to six months is common. State the confirmation process clearly. |
| Does the 50% wage rule affect my salary structure? | Yes. Allowances above half of total pay are counted as wages for some calculations under the Code on Wages (s.2(y)), which can change gratuity and PF amounts [VERIFY with payroll rules]. |
| Can the offer be accepted by eSign? | Yes. An offer letter and an appointment letter can both be signed with Aadhaar eSign or a DSC. |
| Is stamp duty payable on an appointment letter? | Some States treat employment agreements as chargeable agreements [VERIFY per State]. Vidhi shows your State's rule. A simple offer letter is often not stamped. |
| Can I withdraw an offer after acceptance? | Withdrawing an accepted offer can be a breach of contract. State any conditions (such as background checks) in the offer itself. |

**Related:** Employment agreement · NDA · Work-from-home policy · POSH policy · Relieving letter · Full-and-final settlement letter
**Schema:** WebPage + BreadcrumbList; Service; optional FAQPage.
**"i" keys:** `hlp.hr.wages_definition`, `hlp.hr.fixed_term_employment`, `hlp.hr.probation`, `hlp.tpl.non_solicitation`.
**Review flags:** [VERIFY] Labour Code effects with the shared labour rulepack; probation line; State duty. Manual line "LawDocs can work as your outsourced HR department" removed (scope claim).

---

### FP-07 — Partnership Deed

| Field | Copy |
|---|---|
| URL | `/documents/planning-and-execution/partnership-and-founders/partnership-deed` |
| SEO title | Partnership Deed Online: Draft, Stamp and Register |
| Meta description | Draft a partnership deed free with Vidhi. Set capital, profit share, roles and exit rules, pay stamp duty, eSign and get your Registrar of Firms checklist. |
| Eyebrow | Neutral drafts. Equal footing. |
| H1 | Partnership Deed — Draft, Stamp and Register Your Firm |

**Answer-first summary:**
A partnership deed is the written agreement between the partners of a firm under the Indian Partnership Act 1932. It fixes capital, profit sharing, duties and exit. Without one, default rules apply, such as equal profit shares (s.13). Registration is optional, but an unregistered firm cannot sue third parties to enforce its contracts (s.69).

**Key facts box:**

| Fact | Value |
|---|---|
| Governing law | Indian Partnership Act 1932; State Stamp Act; income-tax law for firms [VERIFY: Income-tax Act 2025 provisions] |
| Stamp duty | Yes — State schedule entry for partnership instruments [VERIFY: Indian Stamp Act Sch. I, Art. 46 and State equivalents] |
| Registration | Optional, with the State Registrar of Firms (s.58); strongly recommended (s.69) |
| eSign | GB-08 Variant A for the deed; the Registrar of Firms may ask for physical or notarised copies [VERIFY per State] |
| Last legal review | [date] |

**Draft block:** GB-04 (questions: firm name and business; partners; capital contributions; profit and loss ratio; remuneration and interest on capital; working and sleeping partners; bank operation; decisions needing all partners; admission, retirement and death; non-compete during partnership; dispute resolution).
**Professional block:** GB-05, plus "Firm registration with the Registrar of Firms" (service, price `[OWNER TO SET]`).

**If the deed is silent — the Act's default rules**

| Topic | Default rule (Indian Partnership Act 1932) |
|---|---|
| Profit and loss | Shared equally (s.13(b)) |
| Remuneration | None for taking part in the business (s.13(a)) |
| Interest on capital | Only if agreed, and only out of profits (s.13(c)) |
| Interest on advances | 6% a year (s.13(d)) |
| Taking part | Every partner may take part in the business (s.12(a)) |
| Ending a partnership at will | Any partner may dissolve it by written notice (s.43) |

A clear deed replaces these defaults with what you actually agreed. One plus one makes eleven only when the terms are clear.

**Why register the firm**
Registration is made by filing a statement with the Registrar of Firms of your State (s.58). If the firm is not registered, the firm cannot sue a third party to enforce a contract, and a partner cannot sue the firm or the other partners to enforce rights under the deed (s.69(1)–(2)). Registration can be done later, but it is cheaper than losing a claim.

**Partnership or LLP?** A partnership firm is quick to set up but partners have unlimited liability. A limited liability partnership under the LLP Act 2008 limits liability and has its own legal identity, with annual filings. See Start a Business → LLP.

**What's included**
- Firm name, principal place of business and nature of business
- Partners' details and date of commencement
- Duration (at will or fixed term)
- Capital contributions and further capital
- Profit and loss ratio
- Partners' remuneration and interest on capital, within income-tax limits [VERIFY]
- Duties, authority limits and decisions that need unanimous consent
- Bank account operation
- Books of account and annual accounts
- Admission of new partners; retirement; expulsion (only if the deed allows, s.33)
- Death or insolvency of a partner and valuation of their share
- Non-compete during the partnership; confidentiality
- Dissolution and settlement of accounts
- Disputes: mediation, then arbitration or courts
- Signatures and witnesses

**Documents and information needed**

| Party | What to keep ready |
|---|---|
| Each partner | Identity proof, address proof, PAN, photograph |
| Firm | Proof of business address (rent agreement or ownership proof plus NOC), proposed name |
| For registration | Form prescribed by the State Registrar, stamped deed, fee [VERIFY per State] |

**How it works**
1. Answer the questions; Vidhi drafts the deed.
2. All partners review and agree changes in track-changes mode.
3. Pay stamp duty on the deed through an authorised channel.
4. Partners sign (Aadhaar eSign or ink) with two witnesses.
5. Apply for firm PAN and bank account.
6. Register with the Registrar of Firms (online in some States [VERIFY]).
7. Keep the deed in the firm's vault; we remind you to update it when partners or ratios change.

**State, stamp and registration notes:** Stamp duty on partnership deeds is often linked to the capital contributed, and differs by State [VERIFY per State]. Registrar of Firms procedures, forms and fees are State-specific; some accept online filing [VERIFY]. Retirement or admission of partners needs a supplementary deed and notice to the Registrar.

**eSign eligibility:** GB-08 Variant A.

**FAQs**

| Q | A |
|---|---|
| Is registering a partnership firm compulsory? | No, but an unregistered firm cannot sue a third party to enforce a contract (Indian Partnership Act 1932, s.69). Most firms register for this reason. |
| What if we don't have a partnership deed? | The Act's default rules apply: equal profit sharing, no remuneration, and 6% interest on advances (s.13). A deed lets you agree your own terms. |
| Does a partnership deed need stamp duty? | Yes. It is chargeable under your State's Stamp Act, often based on capital [VERIFY per State]. An unstamped deed cannot be used in evidence until duty and penalty are paid. |
| Can a partnership deed be signed online? | Yes, with Aadhaar eSign after stamping. Some Registrars of Firms still ask for physical signed or notarised copies [VERIFY per State]. |
| Can a partner be expelled? | Only if the deed gives the power and it is used in good faith (s.33). Include a clear expulsion clause if you want this option. |
| How do we add or remove a partner? | Sign a supplementary deed of admission or retirement, pay stamp duty, and inform the Registrar of Firms of the change. |
| Should we choose an LLP instead? | Choose an LLP if you want limited liability and a separate legal entity, and can handle annual filings. A firm is simpler but liability is unlimited. |

**Related:** Deed of retirement · Deed of admission · Dissolution deed · Notice to partner · LLP agreement · Partnership firm registration (service)
**Schema:** WebPage + BreadcrumbList; Service; optional FAQPage.
**"i" keys:** `hlp.tpl.partnership_at_will`, `hlp.bsv.registrar_of_firms`, `hlp.tpl.sleeping_partner`.
**Review flags:** [VERIFY] Art. 46 and State rates; Registrar procedures; income-tax limits for partners' remuneration under the 2025 Act. Manual text "Future ready documents with blockchain technology" removed.

---

### FP-08 — Startup Desk (section landing) and Founders' Agreement

#### FP-08A — Startup Desk landing

| Field | Copy |
|---|---|
| URL | `/startups` |
| SEO title | Startup Desk: Legal Help for Founders, Idea to Funding |
| Meta description | Founders' agreement, incorporation, DPIIT recognition, trademarks, ESOPs and contracts, plus a Startup Legal Officer retainer at a fixed monthly fee. |
| Eyebrow | Idea today. Entity tomorrow. |
| H1 | Startup Desk — Legal Work for Founders, from Idea to Funding |

**Answer-first summary:**
The LawDocs Startup Desk brings a startup's legal work into one place: founders' agreement, choice of entity and incorporation, DPIIT recognition, trademark filing, offer letters, ESOPs, investor documents and compliance calendars. Draft standard documents yourself with Vidhi, or hand them to professionals at a fixed fee or on a monthly retainer.

**Section: Your first 90 days, sorted**

| Stage | What you need | On LawDocs |
|---|---|---|
| Before incorporation | Founders' agreement, NDA for early talks, name and trademark search | Draft free with Vidhi; trademark search service |
| Incorporation | Private limited company, LLP or OPC; DSC; PAN and TAN | Start a Business services (CS-led) |
| Recognition | DPIIT startup recognition [VERIFY: eligibility — entity age up to 10 years and turnover up to ₹100 crore, per the current notification] | Application support service |
| Team | Offer letters, appointment letters, IP assignment, ESOP plan | Templates + review |
| Customers | Terms of service, privacy notice, vendor and client contracts | Templates + review |
| Funding | Term sheet review, shareholders' agreement, data room | Professional services; virtual data room add-on |
| Every month | ROC, GST and TDS due dates | Compliance calendar; reminders |

**Section: Startup Legal Officer retainer**
> **Your legal desk, from day one.** A monthly retainer with an hour bank for contract reviews, founder and ESOP documents, investor paperwork and a monthly compliance calendar. Legal advice is given by an advocate in their own name; ROC work by a company secretary. Fee `[OWNER TO SET — R6 seed ₹14,999–₹24,999/month]`, scope and response times in an SLA you eSign inside LawDocs.
> Button: Ask for a retainer proposal

**Section: Plans for startups** — Pro plan teaser: founders' pack, three seats, eSign credits, trademark tracker, basic CLM. Link: Pricing.

**Section: Learn** — FinLegal Academy courses for founders (link to trainings.lawdocs.in catalogue, open without login).

**Landing FAQs** (reuse FP-08B FAQs 1–3, plus this one):

| Q | A |
|---|---|
| Which entity should a startup choose? | Most venture-funded startups choose a private limited company because investors can take shares and ESOPs are possible. An LLP suits service firms that do not plan equity funding. An OPC suits a single founder. A professional can advise on your plan. |

#### FP-08B — Founders' Agreement

| Field | Copy |
|---|---|
| URL | `/documents/planning-and-execution/partnership-and-founders/founders-agreement` (canonical; the M&A duplicate redirects here — R5 §3.1) |
| SEO title | Founders' Agreement: Equity, Vesting and IP, Draft Free |
| Meta description | Agree equity, vesting, roles, IP and exits before you raise money. Draft a founders' agreement free with Vidhi and have it reviewed at a fixed price. |
| Eyebrow | Founders agree first. Investors follow. |
| H1 | Founders' Agreement — Equity, Vesting, Roles and IP |

**Answer-first summary:**
A founders' agreement is a contract between co-founders that settles the equity split, vesting, roles, decision-making, ownership of intellectual property and what happens when a founder leaves. To bind the company and future shareholders, key share-transfer terms should also be written into the company's Articles of Association (Companies Act 2013, s.5).

**What's included**
- Founders, the business and the proposed entity
- Equity split and the reasons for it
- Vesting schedule and cliff (for example four years with a one-year cliff — common market practice, not a legal rule)
- Roles, time commitment and titles
- Decisions that need all founders (fund-raise, new founder, sale of business)
- Assignment of all IP created for the business to the company
- Good-leaver and bad-leaver terms, buy-back price and method
- Deadlock resolution
- Confidentiality and non-solicitation
- Founder salaries and expenses policy
- Steps to carry key terms into the Articles and a later shareholders' agreement
- Disputes: mediation (option to use Equator), then arbitration

**Process:** answer questions → all founders review and agree in track-changes mode → stamp duty as an agreement [VERIFY per State] → eSign → after incorporation, adopt matching Articles (board and shareholder approvals) → store in the company vault.

**eSign eligibility:** GB-08 Variant A.

**FAQs**

| Q | A |
|---|---|
| When should we sign a founders' agreement? | Before you incorporate or take outside money, while everyone agrees. It is much harder to settle equity after the business has value. |
| Is a founders' agreement binding on the company? | It binds the founders who sign it. To bind the company and future shareholders, transfer restrictions and similar terms should be in the Articles of Association [VERIFY: case law on Articles prevailing]. |
| What is vesting? | Vesting means a founder earns their shares over time. If they leave early, unvested shares can be bought back at an agreed price. It protects the founders who stay. |
| Who owns the code or brand a founder created before incorporation? | The founder does, unless they assign it. The agreement should assign it to the company once incorporated. |
| Can founders get ESOPs? | Generally ESOPs are not for promoters, but promoters of DPIIT-recognised startups may receive them for a period after incorporation [VERIFY: Companies (Share Capital and Debentures) Rules 2014, r.12]. |
| Do investors ask for the founders' agreement? | Investors usually review it during due diligence and replace parts of it with a shareholders' agreement and amended Articles. |

**Related:** Shareholders' agreement · ESOP plan · IP assignment deed · NDA · Private limited company registration · Trademark registration
**Schema:** Landing — CollectionPage + BreadcrumbList; founders' page — WebPage + Service; optional FAQPage.
**"i" keys:** `hlp.bsv.dpiit`, `hlp.tpl.vesting`, `hlp.tpl.cliff`, `hlp.tpl.good_leaver`, `hlp.gov.articles_of_association`.
**Review flags:** [VERIFY] DPIIT criteria, ESOP rule, Articles case law; [OWNER TO SET] retainer fee; [COUNSEL] entity-choice FAQ.

---

### FP-09 — Legal Notice (including cheque bounce)

| Field | Copy |
|---|---|
| URL | `/documents/legal/legal-notices/legal-notice` with variants: money recovery, cheque bounce (s.138 NI Act), property, consumer, employment dues, defamation; reply variant at `/documents/legal/reply-to-legal-notices/reply-to-legal-notice` |
| SEO title | Legal Notice Online: Draft, Send and Track |
| Meta description | Draft a legal notice for unpaid money, a bounced cheque, property or consumer issues. Use our template free, or have an advocate draft and send it. |
| Eyebrow | Say it once. Say it in a notice. |
| H1 | Legal Notice — Draft It Yourself or Through an Advocate |

**Answer-first summary:**
A legal notice is a formal written demand that tells the other side what went wrong, what you want and by when, before you go to court. Some laws make a notice compulsory, such as the 30-day demand for a bounced cheque (Negotiable Instruments Act 1881, s.138) or two months' notice before suing the Government (CPC, s.80).

**When a notice is required by law**

| Situation | Requirement | Provision |
|---|---|---|
| Bounced cheque | Written demand within 30 days of receiving the bank's information that the cheque was returned unpaid; drawer gets 15 days from receipt of the notice to pay | NI Act 1881, s.138 proviso (b)–(c) |
| Suit against the Government or a public officer | Two months' notice before filing | CPC 1908, s.80 |
| Ending a monthly tenancy (no written term) | 15 days' notice, unless a contract, local law or usage says otherwise; State rent laws may add conditions | Transfer of Property Act 1882, s.106 |
| Commercial dispute (no urgent relief) | Pre-institution mediation before filing a suit — a separate step, not a notice | Commercial Courts Act 2015, s.12A |
| Most other disputes | Not compulsory, but expected and often decisive | — |

**Cheque bounce: the clock**

| Step | Time limit | Provision |
|---|---|---|
| Present the cheque | Within its validity (three months from its date) | NI Act s.138 proviso (a) (six months or the validity period, whichever is earlier); RBI three-month validity [VERIFY circular reference] |
| Send the demand notice | Within 30 days of receiving the bank's return information | NI Act s.138(b) |
| Drawer may pay | Within 15 days of receiving the notice | s.138(c) |
| File the complaint | Within one month after those 15 days expire (delay can be condoned for sufficient cause) | s.142(1)(b) |
| Where to file | Court where the branch of the bank at which the payee keeps the account (through which the cheque was presented for collection) is located | s.142(2)(a) |
| Possible outcome | Imprisonment up to two years, or fine up to twice the cheque amount, or both; interim compensation up to 20% may be ordered | ss.138, 143A |

Note: courts have considered whether the pre-cognisance hearing in BNSS 2023 s.223 applies to cheque complaints; follow the position in your State [VERIFY — R5 §5].

**Draft it yourself or use an advocate?**

| | Self-drafted notice (free template) | Advocate's notice (paid service) |
|---|---|---|
| Signed by | You | An advocate on your instructions, on their letterhead |
| Best for | Simple dues, first reminders, consumer complaints | Cheque bounce, property, high-value or disputed claims |
| Includes | Vidhi draft from a reviewed template; dispatch checklist | Facts review, legal grounds, drafting, dispatch, one reply review |
| Price | Free (template) | Professional fee + LawDocs platform fee + GST, shown in full `[OWNER TO SET — R6 seed ₹1,499–₹2,999 + postage at actuals]` |

**What's included (notice template)**
- Sender and recipient details
- Facts in numbered paragraphs, with dates and amounts
- The legal basis (for example, s.138 NI Act; breach of contract under the Indian Contract Act 1872)
- The demand: amount, action or stop-doing, with a deadline
- Consequences if ignored (civil suit, criminal complaint where the law provides, consumer complaint)
- List of enclosures (cheque copy, return memo, invoices, agreement)
- Signature and date

**Documents and information needed**

| Notice type | Keep ready |
|---|---|
| Cheque bounce | Copy of the cheque; bank return memo with date; proof of the debt (invoice, loan agreement, ledger); drawer's address |
| Money recovery | Invoices, purchase orders, emails or chats agreeing the amount, ledger statement |
| Property | Agreement, receipts, title papers, photographs |
| Consumer | Bill or order, warranty, complaint references, replies from the company |

**How it works**
1. Choose the notice type; Vidhi asks only the questions that matter.
2. Review the draft; tap "i" to see what each paragraph does.
3. Sign it (eSign or ink), or send it to an advocate to sign and issue.
4. Send it by registered post or speed post with tracking, and by email where you have it; keep the receipts [VERIFY: courts' approach to email and messaging service].
5. Upload the postal receipt and tracking proof to the vault. We count the deadline from the delivery date and remind you when to file.
6. If a reply comes, tap "Answer back. On record." to draft a para-wise rejoinder.

**eSign eligibility:** GB-08 Variant A (a notice is a letter). The cheque itself is not signed on LawDocs.

**FAQs**

| Q | A |
|---|---|
| Can I send a legal notice without a lawyer? | Yes. Anyone can send a notice in their own name. For cheque bounce, property and high-value claims, an advocate's notice is often more effective because it is reviewed for legal grounds. |
| How many days do I have to send a cheque-bounce notice? | 30 days from the day you receive the bank's information that the cheque was returned unpaid (NI Act 1881, s.138(b)). Missing this deadline can defeat the criminal complaint. |
| What happens after I send a s.138 notice? | The drawer has 15 days from receiving it to pay. If they do not, you can file a complaint within the next month (s.142(1)(b)). |
| Is a notice by email or WhatsApp valid? | Courts have accepted electronic service in some cases, but registered or speed post with tracking remains the safest proof [VERIFY current position]. Use both. |
| Do I have to reply to a legal notice? | There is usually no legal duty to reply, but a clear para-wise reply puts your side on record and can prevent or narrow a case. Bounce back. Legally. |
| Can a company send a legal notice? | Yes. It is signed by an authorised person or issued by the company's advocate. Keep the board or delegated authority on file. |
| How long does the other side get to respond? | The law fixes it in some cases (15 days for s.138; two months under CPC s.80). Otherwise 7 to 30 days is common, depending on the demand. |
| Is the 30-day cheque deadline counted from the cheque date? | No. It runs from when you receive information from your bank that the cheque bounced. |

**Related:** Reply to legal notice · Cheque-bounce complaint (Pleadings) · Money recovery suit (Pleadings) · Loan agreement · Consumer complaint · Case tracker
**Schema:** WebPage + BreadcrumbList; Service (advocate notice: Offer only for live prices); optional FAQPage.
**"i" keys:** `hlp.pld.s138`, `hlp.pld.return_memo`, `hlp.pld.para_wise_reply`, `hlp.pld.s80_cpc`, `hlp.pld.s12a_mediation`.
**Review flags:** [COUNSEL] whole page (advocate review mandatory); [VERIFY] RBI cheque validity reference, BNSS s.223 position, electronic service. Manual's IPC/Evidence Act citation under "Legal Notices" removed (R5 §5).

---

### FP-10 — Aadhaar eSign and eStamp

| Field | Copy |
|---|---|
| URL | `/esign` (eStamp section anchored at `/esign#estamp`; `/estamp` 301s here) |
| SEO title | Aadhaar eSign and eStamp Online for Agreements |
| Meta description | Sign agreements with Aadhaar eSign through a licensed eSign Service Provider. Pay State stamp duty at actuals first. See which documents can be eSigned. |
| Eyebrow | One OTP. One recognised signature. |
| H1 | Aadhaar eSign and eStamp — Stamp First, Then Sign |

**Answer-first summary:**
Aadhaar eSign is an electronic signature issued by a licensed eSign Service Provider after you confirm with an OTP sent to your Aadhaar-linked mobile. It is recognised under the IT Act 2000 (s.3A and Second Schedule). LawDocs checks that your document may be eSigned, pays stamp duty through an authorised channel, then opens signing.

**How Aadhaar eSign works**
1. You review the final document. It is locked so nobody can change it while signing.
2. A consent screen explains what will happen. You agree.
3. The eSign Service Provider sends an OTP to your Aadhaar-linked mobile. You enter it on the provider's screen.
4. The provider issues a one-time signing certificate and signs the document's fingerprint (hash). The key is then deleted.
5. The signature, certificate and time are embedded in the PDF. Anyone can check it in a PDF reader.
6. When everyone has signed, your evidence pack is created.

LawDocs never sees or stores your Aadhaar number, OTP or biometrics. The eSign Service Provider handles authentication (NN-04, NN-06).

**Other ways to sign**

| Method | Who it suits | Legal status |
|---|---|---|
| Aadhaar eSign (OTP) | Anyone with an Aadhaar-linked mobile | Electronic signature (IT Act s.3A, Second Schedule) |
| Class 3 digital signature certificate (DSC) | Company signatories, professionals | Digital signature (IT Act s.3) |
| Account-based eSign | People without an Aadhaar-linked mobile, NRIs and foreign nationals, where our provider supports it [VERIFY] | Electronic signature under eSign API 3.x (R3 LG-004, LG-008) |
| Electronic acceptance (OTP or click) | Low-risk acknowledgements | A valid contract acceptance (IT Act s.10A), but not an "eSign" — labelled "electronic acceptance" |
| Wet ink | Documents the law excludes, or where a party prefers ink | Ordinary signature |

**What can and cannot be eSigned**

| Can be eSigned (examples) | Cannot be eSigned (IT Act s.1(4), First Schedule as amended 2022) |
|---|---|
| Rent agreements and leases (stamp first; register where required) | Wills and codicils (Entry 4) |
| Agreements to sell property (since 2022 [VERIFY]) | Trust deeds (Entry 3) |
| NDAs, service, vendor and employment agreements | Powers of attorney, except those empowering a regulated financial entity (Entry 2) |
| Partnership deeds, founders' agreements, loan agreements | Promissory notes and bills of exchange, except those in favour of a regulated financial entity; cheques are outside the exclusion (Entry 1) |
| Legal notices, board resolutions, minutes (where SS-1 permits [VERIFY]) | Affidavits need a notary or oath commissioner — an eSign does not make them sworn (Notaries Act 1952; Oaths Act 1969) |

**eStamp: how stamp duty is paid**
1. We work out the duty for your State and document type, and show the rule and its source.
2. We buy an e-stamp certificate in the first party's name through an authorised channel — Stock Holding Corporation of India (the Central Record-keeping Agency), its authorised collection centres, or the State's own system (for example GRAS or franking in Maharashtra) (R3 LG-098, LG-099).
3. We verify the certificate's unique number and attach it to the document before signing.
4. You pay the duty at actuals, plus our facilitation fee as a separate line.

If your State has no e-stamping, or you already hold stamp paper, upload it; we verify what we can and record it. We never let signing start before the stamp is attached (NN-08).

**After signing: proof that lasts**
Your evidence pack holds the signed PDF, every signer's event trail, certificate details, document fingerprints and timestamps. One click prepares a draft certificate under the Bharatiya Sakshya Adhiniyam 2023, s.63(4), for producing the document in court (Part A for you; Part B for an expert).

**Witnesses and notaries:** where witnesses are customary, they can eSign in the same ceremony; where the law requires attestation (for example wills, and gifts and mortgages of immovable property), we prepare a print-and-sign pack instead [COUNSEL: electronic attestation]. Notarisation is not available online in India [VERIFY]; we prepare a print pack and can book a notary appointment where offered.

**Price:** Aadhaar eSign ₹[OWNER TO SET — seed ₹29] per signer, or included credits on paid plans · eStamp facilitation ₹[OWNER TO SET — seed ₹49] per stamp + duty at actuals · GST extra on our fees.

**FAQs**

| Q | A |
|---|---|
| Is Aadhaar eSign legally valid? | Yes. It is an electronic signature specified in the Second Schedule of the IT Act 2000 and has the same effect as a handwritten signature for documents the Act does not exclude (ss.3A and 5). |
| Do both parties need Aadhaar? | No. A party without an Aadhaar-linked mobile can sign with a DSC, account-based eSign where available, or ink. |
| Does LawDocs store my Aadhaar number? | No. Authentication happens with the licensed eSign Service Provider. Where an Aadhaar number appears in a document you upload, we mask the first eight digits in every text version we create (search, previews, AI). Your original file stays as you uploaded it, encrypted and visible only to people you allow, and you can replace it with a masked copy. |
| Can I eSign a power of attorney? | Generally no. Powers of attorney are excluded from electronic signature, except those authorising a regulated financial entity to act for you (IT Act First Schedule, Entry 2). We give you a print-and-sign pack. |
| Does eSign remove the need for stamp duty? | No. Stamp duty depends on the document, not on how it is signed. Pay it before signing (Indian Stamp Act 1899, s.17). |
| Can I buy e-stamp paper for any State? | We can buy through authorised channels in the States our partners cover [VERIFY coverage list]. Elsewhere, upload stamp paper you bought locally. |
| Is an eSigned document accepted by courts? | Courts accept electronic records and signatures; a secure electronic signature carries a presumption under the BSA 2023 (s.86 [VERIFY]). Keep the evidence pack and use the s.63 certificate. |
| What if the other party refuses to sign online? | They can sign in ink on a printed copy. Upload the signed copy; the vault keeps both. |

**Related:** Check eSign eligibility · Signing for teams · Legal Vault · Rent agreement · Evidence pack explained (help) · Pricing
**Schema:** WebPage + Service (eSign, eStamp facilitation) + BreadcrumbList; Offer only for live prices; optional FAQPage.
**"i" keys:** `hlp.sgn.esp`, `hlp.sgn.hash`, `hlp.sgn.estamp_uin`, `hlp.sgn.electronic_acceptance`, `hlp.sgn.evidence_pack`, `hlp.dms.s63_certificate`.
**Review flags:** [COUNSEL] whole page; [OWNER] name the eSign/eStamp partner once contracted; [VERIFY] account-based eSign availability, State coverage, notarisation, BSA s.86 wording, SS-1 eSign of minutes.

---

### FP-11 — Legal Vault

| Field | Copy |
|---|---|
| URL | `/legal-vault` |
| SEO title | Legal Vault: Store, Share and Export Legal Documents |
| Meta description | Keep every agreement, deed and court paper in one secure Legal Vault. Import from DigiLocker with consent, share selectively and export everything free. |
| Eyebrow | Store once. Find it fast. |
| H1 | Legal Vault — Every Legal Document, Safe and Searchable |

**Answer-first summary:**
The LawDocs Legal Vault is a secure online space for your legal documents: agreements, property papers, court records, notices, receipts and IDs. Originals are locked against changes, every version is kept, and you choose what to share, with whom and for how long. You can export everything, free, at any time.

**What it does**

| Feature | What you get |
|---|---|
| Locked originals | Every uploaded or signed file is stored unchanged with a digital fingerprint taken on arrival (NN-09). |
| Typed copies and translations | Vidhi can type out handwritten pages and WhatsApp screenshots and translate them into English. These are labelled copies you can correct; the original never changes. |
| Search | Find a clause, a name or a date across every document. |
| Folders that make sense | Property, Family, Employment, Vehicles, Loans and Insurance, Disputes, Tax — for individuals; departments and years for companies. |
| Selective sharing | Share one document, or one page, by link or with a named person; set view-only, expiry and watermark; revoke any time. |
| Import from DigiLocker | With your consent, pull issued documents such as your PAN card or driving licence. Issuer-verified documents carry a badge. |
| Bulk upload | Drop a whole folder; we keep your folder structure. |
| Family and nominee | Add family members to shared folders. Name a nominee who can request access in an emergency, after verification. |
| Reminders | Rent increases, renewals, warranty ends, hearing dates. |
| Export | One click gives you a ZIP of plain folders with Word, PDF, Excel and CSV files, an index and a "Read me first" guide. |

**About DigiLocker (say this clearly):** The Legal Vault is not DigiLocker and is not a government service. DigiLocker is the Government of India's digital document wallet. With your consent, LawDocs can fetch documents from DigiLocker. By default we keep the link and its verification result and fetch the document again when you need it; we keep a copy only where you save it for a purpose you choose and DigiLocker's terms allow (R3 LG-038; NN-42) [VERIFY: confirm retained-copy rules with NeGD].

**Privacy and security** (each line shown only once verified at launch — §2.4):
- Stored on servers in India [VERIFY at launch].
- Encrypted in transit and at rest [VERIFY at launch].
- Aadhaar numbers in your uploads are masked automatically to the last four digits.
- Your documents are never used to train AI models.
- Every view, download and share is logged; you can see the log.
- LawDocs staff can open your vault only with a time-limited grant you approve (NN-17).

**Price:** Free plan includes [1 GB — OWNER TO SET]; paid plans add storage. Export is free on every plan, always.

**FAQs**

| Q | A |
|---|---|
| Is the Legal Vault the same as DigiLocker? | No. DigiLocker is a government service. The Legal Vault is LawDocs' own storage for your legal documents. You can import documents from DigiLocker into it with your consent. |
| Are documents in DigiLocker legally valid? | Documents issued into DigiLocker by the issuing authority are treated as at par with the originals (IT Digital Locker Rules 2016, r.9A). A copy you upload to any vault is a copy, not an issued document. |
| Can LawDocs staff see my documents? | Not by default. Staff need a scoped, time-limited grant that you approve, and every access appears in your access log. |
| What happens to my files if I stop paying? | You keep access to read and export them. Paid features stop; your files are not deleted at the end of a paid term. [OWNER: confirm downgrade storage policy] |
| How do I get everything out? | Settings → Export. You get a ZIP with self-explanatory folders and an index that works without LawDocs. |
| Can someone access my vault if something happens to me? | You can name a nominee. They can request access, and we release it only after verifying the documents required (for example, a death certificate). |
| Can I correct a typed copy that Vidhi made? | Yes. Typed copies and translations are editable and versioned. The original stays unchanged next to them. |

**Related:** Import from DigiLocker (help) · Export your data · Company document management · Aadhaar eSign · Pricing
**Schema:** WebPage + SoftwareApplication (applicationCategory: BusinessApplication) + BreadcrumbList.
**"i" keys:** `hlp.dms.legal_vault`, `hlp.dms.original_vs_copy`, `hlp.kyc.digilocker`, `hlp.dms.nominee`, `hlp.xpt.export`.
**Review flags:** [COUNSEL + DPO] privacy section; [VERIFY] NeGD retained-copy rules; [OWNER] downgrade policy and free storage.

---

### FP-12 — Litigation and Case Tracker

| Field | Copy |
|---|---|
| URL | `/case-tracker` (company section `/case-tracker#for-companies`) |
| SEO title | Case Tracker: Hearing Dates, Orders and Matters in One Place |
| Meta description | Track court cases by CNR or case number. Get next-date reminders, keep orders and pleadings together, and manage all company matters on one calendar. |
| Eyebrow | Every hearing, on your radar. |
| H1 | Case Tracker — Hearings, Orders and Matters for People and Companies |

**Answer-first summary:**
The LawDocs Case Tracker keeps your court cases in one place. Add a case by its CNR or case number; we fetch its status and next date from official sources and licensed data partners, remind you before each hearing, and file orders and pleadings with the case. Companies manage every matter, counsel and deadline on one calendar.

**How case data reaches you (be exact):**
> We collect case information from the eCourts services and other official court websites through licensed data partners, and from details you or your advocate add. Each case shows when it was last updated. Court records can change after our last update, so check the court's website before acting on a date. We do not claim live or real-time updates.

**For individuals**
- Add a case with the CNR number, or the court, case type, number and year.
- Next-date reminders by app, email or SMS.
- Your documents for that case — notices, pleadings, orders, evidence — in one folder.
- Vidhi summarises an order in plain language, labelled as an AI summary.
- Share the case folder with your advocate.

**For companies and legal teams**
- All matters across courts, tribunals and authorities, with internal matter numbers.
- Assign internal owners and external counsel; track tasks and filing deadlines.
- Hearing calendar and daily digest for the legal team.
- Exposure and contingent-liability view for management (amounts you enter or approve).
- Legal spend against matters; counsel invoices attached.
- Board and audit committee reports exported to Excel or PDF.
- Optional alert when a new case naming your company appears in sources our partners cover [VERIFY: partner coverage].

**What it does not do:** it does not file cases, appear in court or log in to court portals with your credentials. Filing and appearance are done by you or your advocate.

**Price:** Free — 1 case; Personal — 5; Pro — 50 matters; Business — 300 matters; more by add-on `[OWNER TO SET — R6 seeds]`. Court-data refreshes beyond plan use credits.

**FAQs**

| Q | A |
|---|---|
| What is a CNR number? | The Case Number Record is a unique 16-character number given to each case in district courts and many High Courts on the eCourts system. It appears on case papers and the eCourts website. |
| Is the case status updated in real time? | No. We refresh from official sources and licensed partners on a schedule and show the time of the last update. Check the court's website before acting on a date. |
| Which courts are covered? | District courts and High Courts on eCourts, and other forums our data partners cover [VERIFY coverage list]. For any other forum, add the case manually and update the next date yourself. |
| Can I track a case if I am not a party? | Public case status is available on official court websites. Track only cases you have a legitimate reason to follow, and do not upload documents you are not entitled to share. |
| Can my advocate update the case? | Yes. Invite your advocate to the case folder with the access you choose. |
| Can the tracker remind my whole legal team? | Yes. Company plans send hearing reminders and a daily digest to assigned users, with escalation if a task is overdue. |

**Related:** Court pleadings · Legal notice · Hire an advocate · Company legal department · Legal Vault
**Schema:** WebPage + SoftwareApplication + BreadcrumbList.
**"i" keys:** `hlp.lit.cnr`, `hlp.lit.next_date`, `hlp.lit.cause_list`, `hlp.lit.contingent_liability`, `hlp.lit.last_updated`.
**Review flags:** [VERIFY] partner coverage and new-case alert; [OWNER TO SET] limits. Never use "live", "real-time" or "instant" on this page (NN-20; CH-27).

---

### FP-13 — Trademark Registration and Tracker

| Field | Copy |
|---|---|
| URL | `/trademarks` (service leaf `/start-a-business/protect-your-intellectual-property/trademark-registration`; tracker anchor `/trademarks#tracker`) |
| SEO title | Trademark Registration and Tracker in India |
| Meta description | Search, file and track your trademark in India. Fixed professional fee, government fee shown separately, and reminders for objections and renewal. |
| Eyebrow | Your brand. Nobody else's. |
| H1 | Trademark Registration and Tracker — File, Track and Renew |

**Answer-first summary:**
A registered trademark gives you the exclusive right to use your brand name or logo for the goods or services it is registered for, and to sue for infringement (Trade Marks Act 1999). Registration lasts ten years and can be renewed indefinitely (s.25). LawDocs helps you search, file through a professional, and track every deadline.

**Filing: what you get**

| Step | Who | Notes |
|---|---|---|
| Search | Professional, with a search report | Checks identical and similar marks in your classes |
| Class selection | Professional | Goods and services are grouped into 45 classes |
| Application (TM-A) | Registered trademark agent or advocate | Filed online with IP India |
| Use ™ | You | You can use ™ at any time; use ® only after registration — falsely representing a mark as registered is an offence (s.107) |
| Examination reply | Professional | If the examiner objects (paid add-on) |
| Opposition | Professional | If a third party opposes (quoted separately) |

**Price card:** professional fee ₹[OWNER TO SET — seed ₹1,999 per class] + government fee per class at actuals (₹4,500 for individuals, startups and small enterprises; ₹9,000 for others, for e-filing [VERIFY: Trade Marks Rules 2017, First Schedule, current]) + GST on our fees. Total shown before you pay.

**Tracker: how it works**
- Add your application number. We show the status in plain words ("Examiner objected", "Published in the Journal") and the next deadline.
- Status comes from a licensed data partner where we have one, or from the status you check on IP India and add; we do not run automated retrieval from IP India (NN-05; R6; CH-27). Updates are not instant. Each record shows when it was last updated.
- Journal watch (add-on): we compare new marks published in the Trade Marks Journal with yours, through a licensed data partner [VERIFY partner], so you can oppose within the four-month window (s.21).
- Renewal reminders start well before the ten-year date.

**Key deadlines** (shown as guidance; confirm on the notice you receive [VERIFY: Trade Marks Rules 2017 periods]):

| Event | Typical deadline |
|---|---|
| Reply to an examination report | Within one month from the date of receipt (Trade Marks Rules 2017, r.33(4)) |
| Opposition after advertisement | Four months from the Journal date (s.21) |
| Counter-statement to an opposition | Two months from receiving the notice |
| Renewal | Before the ten-year expiry; late renewal with surcharge within six months after expiry; restoration up to one year |

**FAQs**

| Q | A |
|---|---|
| How long does registration take? | If no objection or opposition arises, often 18 to 24 months; contested marks can take years. You can use ™ from the filing date. |
| Can I use ® after filing? | No. Use ® only once the mark is registered. Using it earlier is falsely representing a mark as registered (Trade Marks Act 1999, s.107). |
| What is the government fee? | Per class, ₹4,500 for individuals, startups and small enterprises and ₹9,000 for others when filed online [VERIFY current Schedule]. We show it as a separate line at actuals. |
| Who files my application? | A registered trademark agent or an advocate engaged for your order files it. LawDocs provides the platform and tracking. |
| Does the tracker get updates automatically? | Where a licensed data partner covers your application, yes, on a schedule. Otherwise you add the status from IP India yourself and we set the reminders. Each record shows when it was last updated and never claims real-time status. |
| What if someone files a similar mark? | With Journal watch, we alert you when a similar mark is published so you can oppose within four months (s.21). A professional can file the opposition. |
| How long does a registration last? | Ten years, renewable every ten years (s.25). We remind you well before the date. |

**Related:** Trademark assignment deed · Trademark licence · Copyright registration · Startup Desk · Logo and brand guidelines
**Schema:** WebPage + Service (trademark filing) + BreadcrumbList; Offer only for live prices.
**"i" keys:** `hlp.ipm.class`, `hlp.ipm.examination_report`, `hlp.ipm.opposition`, `hlp.ipm.journal`, `hlp.ipm.renewal`.
**Review flags:** [VERIFY] government fees, rule periods and Journal-watch partner; [COUNSEL] filing-by-agent language. Copied Wikipedia/ebizfiling text in the manual's Trademark section must not be reused (R5 §4 #16).

---

### FP-14 — Services Marketplace and Retainer Advisory

| Field | Copy |
|---|---|
| URL | `/marketplace` (storefront, open without login — D-11) and `/retainers` |
| SEO title | Legal, Compliance and Tax Services at Fixed Prices |
| Meta description | Buy legal, compliance, tax and GRC services at fixed prices, or set up a retainer with an SLA. Browse FinLegal Academy courses without logging in. |
| Eyebrow | Pick a service. Know the price. |
| H1 | Services Marketplace — Fixed-Price Help from Qualified Professionals |

**Answer-first summary:**
The LawDocs Services Marketplace sells fixed-scope legal, compliance, tax and governance services at prices shown in full before you pay. Each order is delivered by a qualified professional — an advocate, company secretary or chartered accountant, as the work requires. Businesses can also set up a monthly retainer with an SLA signed inside LawDocs. You can buy services without a software plan.

**How it works**
1. Browse by need: Documents and drafting · Notices and disputes · Start a business · Compliance and filings · Tax · Regulated entities (GRC) · Trademarks and IP · Training.
2. Each service card shows scope, turnaround, who delivers it and the full price (GB-05 fee lines).
3. Pay through Razorpay's hosted checkout. Your GST invoice is emailed.
4. A professional is assigned; you work in a secure order room with messages and files.
5. Deliverables land in your vault. Rate the LawDocs service experience (not the advocate — NN-21, NN-49).

**Our commitments**
- No ranking or rating of advocates, no paid placement, no commissions from advocates' fees.
- Advocates give legal advice in their own name; LawDocs provides technology and administration (NN-41).
- Government fees and stamp duty at actuals, on separate lines.
- Cancellation and refund terms shown before you pay.

**GRC services for NBFCs and regulated entities**
> **Your RBI calendar, organised every quarter.** Our governance, risk and compliance professionals work with NBFCs, housing finance companies, co-operative credit institutions and other regulated entities on:
> - Board-approved policies (for example KYC/AML, fair practices code, grievance redressal, outsourcing, IT and information security) aligned to the RBI Directions applicable to your layer under Scale Based Regulation [VERIFY: current consolidated Directions per policy]
> - Compliance testing and gap assessments
> - Risk assessments, stress testing and scenario analysis
> - Board and committee meeting support: agendas, notes and minutes (SS-1/SS-2)
> - Regulatory returns calendars and filing support
> - Annual report and board's report drafting
>
> For software-led compliance management, ask about LawDocsComply, our group's GRC platform (cross-referral, never a condition of purchase).
> Price: per engagement, quoted `[OWNER TO SET — R6 seeds ₹50,000–₹5,00,000]`.

**Retainers (`/retainers`)**

| Retainer | For | Includes (seed) | Monthly fee |
|---|---|---|---|
| Startup Legal Officer | Early-stage startups | Hour bank, contract reviews, founder/ESOP documents, trademark filings at member price, compliance calendar | `[OWNER TO SET]` |
| SME Legal Desk | SMEs and LLPs | Hour bank, notices, vendor contracts, case tracking, HR policies | `[OWNER TO SET]` |
| NBFC / FI Regulatory Retainer | NBFCs, HFCs, co-operative societies, IFSCA units | Advisory, policy reviews, board support, returns calendar, dedicated relationship manager | `[OWNER TO SET]` |
| Managed Legal Department | Mid-size companies without in-house legal | Named legal manager, contract operations, litigation coordination with external counsel, monthly legal MIS | `[OWNER TO SET]` |

> **Your maker. Your checker. Your call.** On a retainer, your relationship manager works inside your LawDocs workspace as a maker under a delivery grant you approve. Your team checks and approves. You see every action in the access log, and you can end the grant at any time (NN-17, R-064).
> Legal advice under a retainer is supplied by advocates in their own name [COUNSEL: structure of the advocates' engagement — R6 §R6.2.7].
> Button: Request a retainer proposal

**FinLegal Academy**
> **Practise before you practise.** Courses on compliance, KYC and AML, recovery-agent (DSA/DMA) conduct, information security, drafting and more, from FinLegal Academy at trainings.lawdocs.in. Browse freely, no login needed. Prices on each course page.
> Button: Explore courses

**Mediation and arbitration:** for dispute resolution, we refer you, at your choice, to Equator, our group's dispute-resolution platform, which runs under its own rules.

**FAQs**

| Q | A |
|---|---|
| Do I need a LawDocs plan to buy a service? | No. Anyone can buy a service. Subscribers get included allowances and member prices. |
| Who will do my work? | A qualified professional assigned to your order: an advocate for legal advice and notices, a company secretary for company filings, a chartered accountant for tax and accounts. Their name and enrolment or membership number appear in your order. |
| Can I choose a specific advocate? | You can request one you already work with to join your order room. We do not list, rank or rate advocates. |
| What does the platform fee cover? | LawDocs' own services: the order room, scheduling, secure storage, payment handling and invoicing. It is shown separately and is not a share of the professional's fee. |
| Why is GST shown differently for some services? | GST depends on the supplier and the buyer. For example, advocates' services to a business may fall under reverse charge, so the business pays the GST directly [TAX MEMO]. Your invoice shows the treatment. |
| What is an SLA in a retainer? | A service-level agreement sets scope, response and turnaround times and the hour bank. You and LawDocs sign it inside the app, and it is stored in your vault. |
| Are FinLegal Academy certificates official qualifications? | They are course-completion certificates from FinLegal Academy. Where a regulator requires a specific certificate (for example, the IIBF certificate for recovery agents), we say so on the course page [VERIFY]. |

**Related:** Pricing · Startup Desk · Regulated entities · Start a business · FinLegal Academy
**Schema:** CollectionPage + OfferCatalog (services with real prices) + BreadcrumbList; LegalService only for LawDocs' own non-reserved services; no Person/ProfilePage markup for advocates.
**"i" keys:** `hlp.mkp.platform_fee`, `hlp.mkp.reverse_charge`, `hlp.mkp.retainer`, `hlp.mkp.hour_bank`, `hlp.sdc.delivery_grant`, `hlp.mkp.maker_checker`.
**Review flags:** [COUNSEL] whole page (BCI Rule 36, ICAI/ICSI listing rules — R3 LG-111–LG-117); [TAX MEMO] GST lines; [OWNER TO SET] all prices.

---

### FP-15 — Pricing

| Field | Copy |
|---|---|
| URL | `/pricing` |
| SEO title | LawDocs Pricing: Free, Personal, Pro and Business Plans |
| Meta description | Start free. Compare Personal, Pro and Business plans for drafting, eSign, Legal Vault and trackers. See GST before you pay and cancel any time. |
| Eyebrow | Free to start. Fair to grow. |
| H1 | Plans and Pricing |

**Answer-first summary:**
LawDocs is free to start: keep your documents in the Legal Vault and draft from templates at no cost. Personal, Pro and Business plans add eSign credits, more storage, trackers and team tools. Services and pay-per-use items, such as stamp duty, are separate. Every price shows GST before you pay, and you can cancel from Settings.

**Billing toggle:** Annual · Monthly (monthly costs more: annual price ÷ 12, plus 20% — R6 principle 5). Toggle label: "Pay yearly — save compared with monthly" (no fake countdowns, no "only today").

**Plan cards (prices `[OWNER TO SET]`; seeds from R6 §R6.2.2, ex-GST). Display rule: the Personal card shows the GST-inclusive price; Pro and Business cards show the ex-GST price with the GST-inclusive total directly beneath it — never GST revealed only at checkout (NN-22, NN-50; W.9 LA-17):**

| | **Personal** | **Pro** | **Business** |
|---|---|---|---|
| For | Individuals and families | Startups, freelancers and professionals | Companies, LLPs and NBFCs |
| Line | Draft, sign and keep every agreement your family needs. | Run your startup's or practice's legal work in one place. | A legal department in one workspace, with approvals and an audit trail. |
| Price (seed) | ₹1,499/year | ₹9,999/year | ₹59,999/year |
| Button | Choose Personal | Choose Pro | Choose Business |

Links under the cards: **Free plan** — "Start free" · **Enterprise** — "For banks, NBFCs, groups and platforms that need scale, APIs and a managed legal team. Talk to us."

**Feature comparison (seeds, `[OWNER TO SET]`):**

| Feature | Free | Personal | Pro | Business | Enterprise |
|---|---|---|---|---|---|
| Template drafts with Vidhi | Unlimited | Unlimited | Unlimited | Unlimited | Unlimited |
| Vidhi AI credits / month | 30 | 300 | 1,500 | 6,000 | Custom |
| People or seats | 1 | Up to 5 family members | 3 seats | 10 working seats + free approver and viewer seats | Bands |
| Legal Vault storage | 1 GB | 10 GB | 50 GB | 250 GB | 1 TB+ / own storage |
| Aadhaar eSign credits | Pay per use | 2 / month | 10 / month | 50 / month | Contracted |
| Electronic acceptance (OTP) | 5 / month | Fair use | Unlimited | Unlimited | Unlimited |
| eStamp facilitation | Per use | Member price | 2 / month included (duty extra) | 10 / month included (duty extra) | Volume |
| Negotiation (track changes, chat) | View only | Yes | Yes | Yes + approval workflows | Yes |
| Case tracker | 1 case | 5 | 50 matters | 300 matters | Custom |
| Trademark tracker | 1 | 3 | 10 + Journal watch | 50 + Journal watch | Custom |
| Contract management | — | Renewal reminders | Basic | Full, with obligations | Custom |
| Guided sessions with the LawDocs documentation team (not legal advice) `[COUNSEL]` | — | 1 × 15 min / year | 2 × 30 min / year | 6 × 30 min / year | Retainer |
| Advocate consultations | Bought separately at a fixed fee paid to the advocate; never part of a plan price (CH-08, NN-21) | Same | Same | Same | Same |
| Board, minutes and registers | — | — | Lite (1 entity) | Full (3 entities) | Groups |
| Export everything | Yes | Yes | Yes | Yes + scheduled export | Yes |
| Support | Help centre, Vidhi | Email and chat | Priority chat | Phone + 30-day onboarding | Named manager, SLA |

**Why each plan is worth it (benefit copy):**
- **Personal:** "Two Aadhaar eSigns a month, renewal reminders and room for your family's papers — for about the cost of one professional review a year." [VERIFY comparison against live service prices before publishing]
- **Pro:** "Everything a founder or practitioner needs to run agreements, trademarks and cases without spreadsheets."
- **Business:** "Maker-checker approvals, an audit trail nobody can edit, board tools and team reminders, so a small legal team can run approvals, records and reminders in one place."

**Add-ons and pay-per-use:** extra seats · family extension · litigation pack · trademark watch · advanced CLM · advanced document intelligence (handwriting, screenshots, translation) · virtual data room · SSO · API access · own-storage export · premium support. eSign packs, eStamp facilitation, AI credit packs and court-data refreshes are sold separately, valid 12 months, with no automatic top-up unless you switch it on. Prices `[OWNER TO SET — R6 §R6.2.3–R6.2.4]`.

**What's never charged:** exporting your data · reading and sharing your own documents · deleting your account.

**Pricing FAQs (NN-50)**

| Q | A |
|---|---|
| Is there a free trial? | Paid plans include a [14]-day trial [OWNER TO SET]. We remind you [3] days before it ends [OWNER TO SET], and you are charged only if you chose to continue when you started the trial; otherwise the trial ends on its own. |
| How does renewal work? | If you turned on auto-renewal at checkout, your plan renews at the end of each term (POL-LD-05 §2); if not, it ends and your files stay readable and exportable. We send a reminder with the amount before renewal, and for e-mandates a pre-debit notice as RBI rules require [VERIFY: RBI e-mandate Directions 2026]. |
| How do I cancel? | Settings → Billing → Cancel plan. It takes two taps, the same as buying. Your plan runs to the end of the paid term; your files stay available to read and export. |
| Do you give refunds? | [OWNER TO SET: refund rule — e.g. full refund within 14 days of the first paid annual term for individuals; unused credits are not refundable once used]. The Refund and Cancellation Policy has the full terms. |
| Are prices inclusive of GST? | Personal plan prices on the cards include GST; Pro and Business cards show the price before GST with the GST-inclusive total printed beneath it, and the full total appears again before you pay (NN-22, NN-50). LawDocs' fees carry 18% GST. Stamp duty and government fees are passed through at actuals [TAX MEMO]. |
| Can I upgrade or downgrade? | Yes, any time from Settings. Upgrades start immediately with a prorated charge; downgrades take effect at the next renewal. |
| What happens to unused credits? | Monthly plan credits reset each month. Purchased packs stay valid for 12 months from purchase. |
| Do I need a plan to buy a service from the marketplace? | No. Services can be bought on their own; plans add member prices and allowances. |
| Do you store my card details? | No. Payments run on Razorpay's hosted checkout. LawDocs never sees or stores your full card number. |
| Can I get a GST invoice in my company's name? | Yes. Add your GSTIN at checkout and the tax invoice is issued in your company's name and emailed to you. |

**Schema:** WebPage + Product/Offer for each plan only once real prices are live; no ratings.
**"i" keys:** `hlp.bil.credits`, `hlp.bil.auto_renewal`, `hlp.bil.proration`, `hlp.bil.gst_invoice`, `hlp.bil.e_mandate`.
**Review flags:** [OWNER TO SET] every price, trial and refund term; [TAX MEMO] GST lines; [VERIFY] e-mandate notice rule. CMS blocks publication while any seed price remains.

---

## 5. Page inventory and rewrite plan summary

### 5.1 Counts by section (R5 §8.5 plus pages beyond the manuals)

| Section | Landing | Hubs | Leaf pages (recommended) | Total | Source |
|---|---|---|---|---|---|
| Documents | 1 | 18 categories + 134 sub-categories | 330 | 483 | Manual_Documents |
| Pleadings | 1 | 13 | 68 (from 89 after merging duplicates) | 82 | Manual_Pleadings |
| Compliance | 1 | 7 | 22 | 30 | Manual_Compliance |
| Start a Business | 1 | 6 | 26 | 33 | Manual_Start_a_Business |
| Regulated entities (RBI, SEBI, IRDAI, other registrations, reporting) | 1 | 5 | ≈ 50 | ≈ 56 | Live sitemap (no manual — write new) |
| Advisory practice areas | 1 | — | 6 | 7 | Live sitemap |
| Product and brand pages | — | — | Home, Vidhi, eSign/eStamp, Legal Vault, Case tracker, Trademark tracker, Startup Desk, Marketplace, Retainers, Pricing, FinLegal Academy link page, For individuals, For companies, For professionals, About, Contact, Careers, Partners | ≈ 18 | This deck + P21 |
| Policies | — | — | Terms, Privacy Notice (DPDP), Cookie, Refund and Cancellation, Disclaimer, Grievance Officer, Acceptable Use, eSign Terms, Marketplace Terms, Professional Code, Accessibility Statement | 11 | P21 + counsel |
| Consumer Help brand | 1 | 4 | ≈ 20 (starter) | ≈ 25 | §7 + P15 |
| **Total indexable at full build** | | | | **≈ 765** | |

Hold pages: 48 stubs and "(upcoming)" sections stay `noindex` until written (R5 §2).

### 5.2 Priority waves

| Wave | Pages | Gate |
|---|---|---|
| 1 (Vault and Sign GA) | The 15 flagship pages in this deck; the 18 product and brand pages; the 11 policies; the top 50 document pages by search demand (rent, lease, sale, gift, affidavit, POA print pack, will print pack, NDA, employment, partnership, LLP, loan, legal notice, reply, cheque bounce); Documents and Start a Business landings | Reviewer named; flags cleared; SSR verified (no-JS fetch shows title, H1, body) |
| 2 (Legal Ops) | Remaining Documents sub-hubs with copy (86) and template leaves; 68 canonical pleadings; Compliance (30); regulated-entity pages (≈ 56); advisory pages | Old→new law maps applied; plagiarism scan passed |
| 3 (Services and Consumer) | Start a Business remainder; the 63 sub-hubs whose document lists must be defined; Consumer Help brand pages | Consumer Help entity and counsel opinion in place |

### 5.3 Sections that must be rewritten from scratch (copied third-party text — R5 §4)

| Manual | Sections | Problem |
|---|---|---|
| Compliance | Closure of Business (hub); Closure of LLP; ITR Filing; TDS Return Filing; Professional Tax Registration; Accounting (hub); Accounting and Book-keeping; Payroll Maintenance; PF Registration; Shops and Establishments; Audit (hub) / Company Audit | Text naming or linking Wikipedia, LegalWiz, Vakilsearch, Corpbiz, Provenience, Registrationwala; scraped FAQ accordions |
| Compliance | Seven hub pages with "Customer experiences" | Adapted or fabricated testimonials from proposal software — delete; never republish (NN-49) |
| Start a Business | LLP; Nidhi Company; Patent; Trademark; FSSAI; IEC; Spices Board; Hallmark Certification; Agmark | Links and text from toppr, enterslice, LegalRaasta, upcounsel, Wikipedia, ebizfiling, legaldocs.co.in, eximguru, Business Standard; Agmark text from dmi.gov.in (cite, do not copy) |
| All four | Every sentence | Run a full plagiarism scan before reuse; exact-phrase checks were not completed in research (R5 §4) |
| Documents | Mediation and Arbitration one-liner; Collaboration quote; "Win the workplace…"; Yoda line | Borrowed quotations (R5 §6.1) |

### 5.4 Outdated law to correct during the rewrite (R5 §5)

| Old reference | Replace with | Main places |
|---|---|---|
| CrPC 1973 | BNSS 2023 (e.g. s.438 → s.482; s.439 → s.483; s.125 → s.144), with "(formerly CrPC s.x)" | Criminal and family pleadings; maintenance, divorce documents |
| IPC 1860 | BNS 2023 (498A → ss.85/86; 420 → s.318; 406 → s.316; 499/500 → s.356; 506 → s.351) | Pleadings; domestic violence; legal notices |
| Indian Evidence Act 1872, s.65B | BSA 2023, s.63 and the Schedule certificate | Affidavits, notices, POA |
| Consumer Protection Act 1986, "District Forum" | CPA 2019; District/State/National Commissions; e-Jagriti filing | Consumer pleadings and documents |
| Companies Act 1956 | Companies Act 2013 | Banking, clubs, companies, Section 8 |
| Listing Agreement / Clause 49 | SEBI (LODR) Regulations 2015 | Companies, secretarial |
| Udyog Aadhaar | Udyam Registration and revised MSME limits | MSME pages |
| GSTR-2/3 matching; s.35(5) GST audit | GSTR-1/1A, 3B, 2B, IMS; self-certified GSTR-9C | GST pages |
| Income-tax Act 1961 | Income-tax Act 2025 (from 1 April 2026), dual-cited for earlier years [VERIFY section numbers] | Tax pages; partnership; property TDS |
| Pre-Code labour Acts | Four Labour Codes (21 November 2025) | Labour, PF, ESI, payroll, HR documents |
| "eSign on every document" | IT Act First Schedule as amended 2022 (R3 LG-003) | POA, will, trust, promissory note pages |
| Sale agreements flagged "not eSign-valid" | Eligible since the 2022 amendment [VERIFY] | R5 CSV rows D12.8.x — update the eligibility register |

### 5.5 Unevidenced claims found in the manuals (remove — NN-20)

| Claim (manual) | Where | Replace with |
|---|---|---|
| "LawDocs uses latest technology of blockchain and Smart Contracts" | Rent, Lease, Partnership Firm | Nothing; describe the real evidence pack instead |
| "None of the party can make default of the agreement…" | Rent | "Clear terms make defaults easier to prove and remedy." |
| "Legally complied which may be produced before any Court in India" | Sale and Purchase | "Prepared for stamping and registration as your State requires." |
| "Our documents are relied by the industry experts" | Apprenticeship and others | Named reviewer footer (GB-12) |
| "LawDocs services for the home delivery of your rent agreement" | Rent | Only if a delivery service exists `[OWNER]` |
| "You receive the amount… immediately" on IP assignment | Trademark (Documents) | Remove; LawDocs does not handle consideration between parties |
| "LawDocs can work as your outsourced HR department" | Job Application and Offers | Link to services actually sold |
| "Call now. 9468776000" on 26 service pages | Start a Business | Single public number from settings + GB-04/GB-05 blocks |

### 5.6 Other clean-up

- Heading typos and slugs: apply R5 §3.2 (e.g. Promissory, Questionnaire, Vakalatnama, Articles of Association, underwriting).
- Duplicates: one canonical leaf per document (R5 §3.1); variants as toggles.
- Redirects: `/smartdrafts/*` → `/documents/*`; `/compliance-services/business-registration/*` → `/start-a-business/*`; feature-bullet URLs under `/compliance-services/*-consultation/*` → parent (301) or 410; `/buy/*` → `noindex`, out of sitemap.

---

## 6. FAQ writing rules and FAQ bank

### 6.1 Rules

1. Write the question the way a user types it ("Can I eSign a rent agreement?"), not as a heading ("eSign of rent agreements").
2. Answer in the first sentence. Yes / No / It depends — then why.
3. Maximum 60 words. One citation when the answer rests on law. Link the citation to India Code or the regulator.
4. No promises, no "always", no "100%". Use "usually" only when true.
5. Mark unverified facts `[VERIFY]`; the CMS blocks them from publishing.
6. FAQs must be visible on the page; FAQPage markup only for visible FAQs (R5 §7.1).
7. Each FAQ has an owner topic and a review date; legal FAQs need a reviewer.
8. Reuse from this bank by ID; never duplicate a slightly different answer on another page.

### 6.2 FAQ bank (72)

**eSign validity (ES)**

| ID | Q | A |
|---|---|---|
| ES-01 | Is an electronic signature legally valid in India? | Yes. The IT Act 2000 gives electronic signatures in the Second Schedule, such as Aadhaar eSign, the same legal effect as handwritten signatures (ss.3A and 5), except for documents the First Schedule excludes. |
| ES-02 | Which documents cannot be eSigned? | Wills, trust deeds, most powers of attorney, and promissory notes or bills of exchange not in favour of a regulated financial entity (IT Act, First Schedule, as amended 2022). |
| ES-03 | Is a scanned or typed signature an eSign? | No. A scanned image or typed name is not an electronic signature under s.3A. It may show acceptance, but proof is weaker. Use Aadhaar eSign or a DSC for important documents. |
| ES-04 | What is the difference between eSign and a DSC? | Aadhaar eSign issues a one-time certificate after an OTP; a DSC is a certificate stored on a USB token that you reuse. Both are legally recognised; companies often use DSCs for filings. |
| ES-05 | Can an NRI eSign? | Yes, if they have an Aadhaar-linked Indian mobile, or through a DSC or account-based eSign where our provider supports it [VERIFY]. |
| ES-06 | Can witnesses eSign? | Where witnesses are customary, yes, in the same signing session. Where the law requires attestation (for example wills, and gifts and mortgages of immovable property), use ink; electronic attestation is offered only where counsel has confirmed it [COUNSEL]. Registration offices have their own rules for identifying witnesses. |
| ES-07 | Is an eSigned agreement accepted in court? | Yes, as an electronic record. Keep the evidence pack and file a certificate under BSA 2023 s.63(4), which LawDocs drafts for you. |
| ES-08 | Can an affidavit be eSigned? | An affidavit must be sworn before a notary or oath commissioner. An eSign alone does not make it sworn. Use our print pack. |
| ES-09 | Does eSign need both parties to be online at the same time? | No. Each party signs when they receive the link; the document is complete when the last person signs. |
| ES-10 | Can I change a document after someone has signed it? | No. Any change after signing breaks the signature. Create an amendment or a new version and sign again. |

**Stamp duty (SD)**

| ID | Q | A |
|---|---|---|
| SD-01 | What is stamp duty? | A State tax on many documents, such as leases, sale agreements and partnership deeds. The rate depends on your State and the document (Indian Stamp Act 1899 and State Stamp Acts). |
| SD-02 | When must stamp duty be paid? | Before or at the time of signing (Indian Stamp Act 1899, s.17). LawDocs attaches the stamp first, then opens signing. |
| SD-03 | What if a document is not stamped? | It cannot be used as evidence until the duty and a penalty are paid (s.35). It may still bind the parties, but you lose easy proof. |
| SD-04 | Is e-stamp paper valid? | Yes. e-stamp certificates issued through authorised channels are valid in the States that use e-stamping. Each has a unique number you can verify. |
| SD-05 | Does LawDocs sell stamp paper? | No. We buy e-stamp certificates for you through authorised channels and pass the duty through at actuals, plus a separate facilitation fee. |
| SD-06 | Which State's stamp duty applies? | Usually the State where the document is signed or the property is situated; documents signed in one State and used in another may need extra duty [VERIFY: inter-State rules]. |
| SD-07 | Does eSigning avoid stamp duty? | No. Duty depends on the document, not the signing method. |
| SD-08 | Who pays stamp duty? | Whoever the document says. If silent, the Stamp Act sets a default — for example, the tenant for a lease (s.29) [VERIFY State variations]. |

**Registration (RG)**

| ID | Q | A |
|---|---|---|
| RG-01 | Which documents must be registered? | Among others: sale deeds and gifts of immovable property, leases over one year, and agreements to sell supporting part-performance possession (Registration Act 1908, s.17). |
| RG-02 | What happens if a document that needs registration is not registered? | It does not affect the property and cannot be used as evidence of the transaction, with limited exceptions (s.49). |
| RG-03 | How soon must I register? | Present the document within four months of signing (s.23). Delay can be condoned with a fine in limited cases. |
| RG-04 | Can I register online? | Some States allow online registration for some documents, such as leave and licence in Maharashtra [VERIFY]. Most still need a visit to the sub-registrar. |
| RG-05 | Is notarisation the same as registration? | No. Notarisation authenticates signatures; registration records the document with the State. Notarisation never replaces compulsory registration. |
| RG-06 | Do I need witnesses for registration? | Yes, usually two, with identity proof. Check your sub-registrar's list. |
| RG-07 | Can LawDocs register my document? | We prepare the document and the registration pack and help book the appointment where offered. You or your authorised agent appear before the sub-registrar. |

**DigiLocker, Aadhaar and identity (ID)**

| ID | Q | A |
|---|---|---|
| ID-01 | Can I log in with Aadhaar? | No. You log in with a mobile or email OTP, a passkey or a password with two-step verification. Aadhaar is used only for eSign and, optionally, offline verification. |
| ID-02 | How does LawDocs verify my identity? | Optionally through the Aadhaar App or Aadhaar QR (offline verification), or DigiLocker documents. We keep only what is needed and never your full Aadhaar number. |
| ID-03 | Is LawDocs connected to DigiLocker? | LawDocs can fetch documents from DigiLocker with your consent [VERIFY: requester onboarding complete]. LawDocs is not DigiLocker. |
| ID-04 | Why does LawDocs not pull my CIBIL score? | Credit information can be shared only with lenders and other specified users (CICRA 2005, s.17). Download your own report from the credit bureau and upload it if you need help. |
| ID-05 | Do you check PAN automatically? | We use the PAN card issued in your DigiLocker, or a licensed verification route. We never scrape government portals. |
| ID-06 | Is there an age limit? | Accounts are for people aged 18 or above. Guardian-managed access for a minor needs proof of guardianship. |

**Data privacy and security (DP)**

| ID | Q | A |
|---|---|---|
| DP-01 | Who can see my documents? | Only you and the people you share them with. LawDocs staff need a time-limited grant you approve. |
| DP-02 | Is my data used to train AI? | No. Your documents and chats are never used to train AI models. |
| DP-03 | Where is my data stored? | On servers in India [VERIFY at launch], with a disaster-recovery copy also in India. |
| DP-04 | Can I delete my account? | Yes, from Settings. We delete your data after the period the law requires us to keep certain records, which the Privacy Notice lists. |
| DP-05 | What are my rights under the DPDP Act? | You can access, correct and erase your personal data, withdraw consent, nominate someone, and complain to us and then to the Data Protection Board (DPDP Act 2023, ss.11–14). |
| DP-06 | Do you share my data with other Infrabyx companies? | Only with your specific consent for a stated purpose, or where the law allows. Each share is recorded. |
| DP-07 | What happens if there is a data breach? | We inform affected users and the authorities within the time limits the law sets, and tell you what to do. |

**AI drafting and Vidhi (AI)**

| ID | Q | A |
|---|---|---|
| AI-01 | Is Vidhi a lawyer? | No. Vidhi is an AI assistant. It explains, drafts and organises. For advice on your situation, ask a professional. |
| AI-02 | Is a Vidhi draft legally valid? | Validity depends on the content, signatures and formalities, not on who typed it. Template drafts use reviewed templates; custom AI drafts are labelled "AI draft — not reviewed by a professional". |
| AI-03 | Can Vidhi make mistakes? | Yes. Check names, numbers and dates. Vidhi shows its sources and marks any citation it cannot verify. |
| AI-04 | Which languages does Vidhi support? | English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, Malayalam and Punjabi. Translations of legal text are labelled until reviewed. |
| AI-05 | Can Vidhi read handwritten documents and WhatsApp screenshots? | Yes. It creates a typed copy linked to the original, with a confidence score. Check and correct it before you rely on it. |
| AI-06 | Can I file a Vidhi translation in court? | Courts usually require a certified translation. Vidhi's translation is a draft; order a certified translation for filing. |
| AI-07 | Will Vidhi send or sign anything for me? | Never without your confirmation. Sending, signing, paying and sharing always need your tap. |
| AI-08 | What are AI credits? | Units for larger AI tasks such as long reviews and translations. Short questions and template drafts use few or none. You see the cost before you start. |

**Payments, subscriptions and refunds (PY)**

| ID | Q | A |
|---|---|---|
| PY-01 | How do I pay? | Through Razorpay's hosted checkout: UPI, cards, net banking and wallets. LawDocs never stores your card number. |
| PY-02 | Will I get a GST invoice? | Yes, by email after every payment, and in Settings → Billing. |
| PY-03 | Can I cancel any time? | Yes, from Settings in two taps. Your plan runs until the end of the paid term. |
| PY-04 | Do you auto-renew? | Yes, with a reminder before renewal and, for e-mandates, a pre-debit notice [VERIFY timing]. You can switch auto-renew off any time. |
| PY-05 | How do refunds work? | As the Refund and Cancellation Policy states [OWNER TO SET]. Refunds go back to the original payment method. |
| PY-06 | Why is stamp duty shown separately? | It is a State tax, not our fee. It is paid at actuals to the authorised stamp channel for you (through our payment partner's split settlement or directly to the vendor), and our fees and GST are shown on separate lines [TAX MEMO]. |
| PY-07 | Is there any hidden fee? | No. The total, including GST and any duty, appears before you pay. |
| PY-08 | Can a company pay by bank transfer? | Business and Enterprise customers can pay by invoice through a virtual account [OWNER: confirm Smart Collect]. |

**Professionals and marketplace (PR)**

| ID | Q | A |
|---|---|---|
| PR-01 | Are the professionals qualified? | Every professional's enrolment or membership number is recorded and shown on your order [VERIFY: onboarding check process]. |
| PR-02 | Why can't I see ratings for advocates? | Bar Council of India rules restrict advocates' advertising, and in 2024 the Madras High Court held that online platforms advertising advocates' services breach the Bar Council rule against advocate advertising (an appeal is pending in the Supreme Court). We do not rate or rank advocates. |
| PR-03 | Does LawDocs take a cut of the advocate's fee? | No. The advocate's fee goes to the advocate. LawDocs charges a separate platform fee for its own services. |
| PR-04 | Who is responsible for the advice? | The professional who gives it, under their own professional rules. LawDocs is responsible for its platform and services. |
| PR-05 | Can a professional represent me in court? | An advocate can, under a separate engagement and vakalatnama. LawDocs itself does not appear in court. |
| PR-06 | What if I am unhappy with a service? | Raise it in the order room or with our Grievance Officer. We acknowledge within 48 hours and resolve within one month (E-Commerce Rules 2020, r.4(5)). |
| PR-07 | Can I hire a CA to file my return? | Yes. A chartered accountant prepares it; you verify and submit it with your own OTP or DSC. |
| PR-08 | Can professionals join LawDocs? | Yes. Apply at /professionals. We check credentials and service fit. There are no listing fees for advocates. |

**Trackers (TR)**

| ID | Q | A |
|---|---|---|
| TR-01 | Is court data live? | No. We refresh it on a schedule from official sources and licensed partners and show when it was last updated. |
| TR-02 | Does LawDocs log in to court or IP India portals for me? | No. We use public records and licensed data, plus details you add. |
| TR-03 | Can I add a case from a tribunal? | Yes. If our partners do not cover it, add it manually and update the next date yourself. |
| TR-04 | How early are reminders sent? | You choose: for example seven days, one day and the morning of the hearing or deadline. |

**General (GN)**

| ID | Q | A |
|---|---|---|
| GN-01 | Is LawDocs a law firm? | No. It is a technology platform. Advocates on LawDocs act in their own name. |
| GN-02 | Is LawDocs a government website? | No. We link to official portals where you need to file or pay. |
| GN-03 | Does LawDocs work on mobile? | Yes, in the browser and in the LawDocs apps for Android and iOS. |
| GN-04 | Is LawDocs accessible with a screen reader? | We build to WCAG 2.2 AA and IS 17802. Tell us about any barrier and we will fix it or help you another way. |

---

## 7. Consumer Help brand — starter copy

All pages run under `[Consumer Help Brand]`, operated by `[Consumer Help Entity]`, a separate entity with its own staff and data and an ethical wall from the group's lender, insurer and compliance products (D-06, NN-23). The brand never promises a waiver, settlement, refund or outcome, never collects money owed to lenders, insurers or the State, and uses advocates only where the forum's rules allow. Success-linked fees stay OFF (CH-31) [COUNSEL].

### 7.1 Consumer Help home

| Field | Copy |
|---|---|
| SEO title | [Consumer Help Brand]: Loan, Insurance and Challan Help |
| Meta description | Organise your complaint, follow the official escalation steps on time and keep every document in one place. No outcome promises. Clear, fixed fees. |
| Eyebrow | Rejected? You can still escalate. |
| H1 | Help with Loan, Insurance and Challan Problems — the Official Way |

**Answer-first summary:** [Consumer Help Brand] helps you take a complaint about a bank, NBFC, insurer or traffic challan through the official steps: the company's own grievance desk first, then the ombudsman or the court, within the time limits. We draft, organise and remind. You stay in control, and you pay any dues or fines only on official portals.

**What we do / what we don't**

| We do | We don't |
|---|---|
| Draft complaints and escalation letters | Promise waivers, settlements or refunds |
| Track time limits and remind you | Take money meant for your lender, insurer or the State |
| Organise evidence in your vault | Claim to be from RBI, IRDAI or the police |
| Explain each forum's rules | Let an advocate file where the forum does not allow it |
| Connect you to an advocate for court matters, on a fixed fee | Share your case with any lender or insurer we work with |

**Fee line:** "Fixed fees, shown before you pay. No fee for using official portals. [OWNER TO SET]"
**Conflict line:** "Before we accept your case, we check that it does not conflict with any client of our group. If it does, we tell you and do not take it."

### 7.2 Loan and lending grievances

| Field | Copy |
|---|---|
| SEO title | Complaint Against a Bank or NBFC: Step-by-Step Help |
| Meta description | Complain to your bank or NBFC first, then to the RBI Ombudsman on time. We draft, track deadlines and organise evidence. No waiver or settlement promises. |
| H1 | Loan or Bank Complaint — Escalate in the Right Order |

**Answer-first summary:** Complain to the bank or NBFC first. If it rejects your complaint or does not reply within 30 days, you can complain to the RBI Ombudsman under the Reserve Bank Integrated Ombudsman Scheme 2026, within the time limit, usually through cms.rbi.org.in. You can file yourself or through a representative other than an advocate (R2; R3 LG-171) [VERIFY clause references].

**The ladder (from R2 §1(b)):**
1. The lender's grievance officer — keep the complaint number.
2. Wait up to 30 days for a reply (the lender's internal ombudsman may review it automatically).
3. RBI Ombudsman — file within the period allowed after the reply or the 30 days [VERIFY: 90-day limit, Cl. 10(1)(g)]. Compensation for consequential loss and harassment is capped by the Scheme.
4. If needed: consumer commission, civil court, or police for threats and harassment.

**Common problems we help with:** wrong charges and interest · harassment by recovery agents (calls outside permitted hours, threats, contacting relatives) · documents not returned after repayment · credit-report errors (dispute with the credit bureau; ₹100 a day compensation after 30 days under RBI's framework [VERIFY]) · unregistered loan apps (report on Sachet and the cyber-crime portal).

**Important:** "We cannot get your loan waived and nobody can lawfully promise that. RBI has warned the public against entities offering 'loan waivers' for a fee." (R2 §0 item 5)

### 7.3 Insurance claim help

| Field | Copy |
|---|---|
| SEO title | Insurance Claim Rejected? Complaint and Ombudsman Help |
| Meta description | Claim rejected or short-paid? Write to the insurer first, then go to the Insurance Ombudsman within one year. We draft, track and organise your papers. |
| H1 | Insurance Claim Rejected or Delayed — What to Do Next |

**Answer-first summary:** Write to your insurer's grievance officer first; insurers must resolve complaints within 14 days [VERIFY: IRDAI PPHI Master Circular 2024, current text]. If the insurer rejects it or does not reply within one month, you can go to the Insurance Ombudsman within one year, for claims up to ₹50 lakh (Insurance Ombudsman Rules 2017, rr.14 and 17). You file the complaint yourself; we help you prepare it.

**Steps:** insurer grievance officer → Bima Bharosa (IRDAI) → Insurance Ombudsman (≤ ₹50 lakh, within one year) → consumer commission on e-Jagriti for larger or excluded claims.
**What to keep ready:** policy schedule and wording · proposal form · claim form · rejection or short-settlement letter · bills and medical or survey reports · all correspondence.
**Representation note:** "The Ombudsman complaint is filed by you, your legal heir, nominee or assignee. An advocate may assist at the hearing stage only where the law allows [VERIFY outside Karnataka — R2]."
**No outcome line:** "We cannot promise that your claim will be paid. We make sure your complaint is complete, on time and in the right forum."

### 7.4 Traffic challan help

| Field | Copy |
|---|---|
| SEO title | Traffic Challan: Check, Pay Officially or Contest |
| Meta description | Got an e-challan? Check it on the official portal, pay there, settle eligible ones at a Lok Adalat, or contest it with an advocate. |
| H1 | Traffic Challan — Check, Pay or Contest the Right Way |

**Answer-first summary:** An e-challan is issued on the government's Parivahan system. You can pay it on the official portal, settle eligible challans at a Lok Adalat, or contest it before the Virtual Court or a regular court. [Consumer Help Brand] explains your options and connects you to an advocate for contests. We never collect challan amounts; you pay only on official portals.

**Options:**

| Option | When | How |
|---|---|---|
| Pay online | You accept the challan | Official e-challan or Virtual Court portal (we open the official page) |
| Lok Adalat | Compoundable challans, when a Lok Adalat is announced in your State | Book a slot on the official site; we remind you |
| Contest | You dispute the challan | Choose "contest" on the Virtual Court; an advocate can appear for a fixed fee `[OWNER TO SET]` |
| Wrong vehicle or sold vehicle | The challan is not yours | Grievance on the e-challan portal with your delivery note or proof (see Vehicle Sale Agreement) |

**Honest line:** "We know of no official API that lets a private company fetch your challans; the transport ministry has said its data access is for government organisations. You check them on the official portal with an OTP to your own mobile, or upload the challan you received." (R2 §0 item 7)

**Consumer Help review flags:** [COUNSEL] all pages, the entity structure and fee model; [VERIFY] RB-IOS 2026 clause numbers and time limits, credit-bureau compensation rule, Insurance Ombudsman representation, State Lok Adalat practice; [OWNER] brand name, entity, fees.
