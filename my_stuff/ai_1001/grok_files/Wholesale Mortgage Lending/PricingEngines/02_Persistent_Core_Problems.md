# 02 — Persistent Core Problems in Pricing

**Purpose:** Some pricing problems have existed for centuries — every new mechanism reduces them but never fully resolves them. Understanding *which* problems are still open explains why PPEs keep evolving and why mortgage pricing remains messy despite decades of computerization.

---

## Problem 1 — Information Asymmetry

**Definition:** One side of the transaction knows more than the other.

**Historical instance:** Medieval grain merchants knew supply conditions in other towns; villagers buying did not.

**In mortgages today:**
- Lenders know their hedge stance, comp plan internals, and reprice triggers.
- Brokers know their pipeline composition.
- Borrowers know their actual intent (refi-or-stay, sell-or-hold).
- *None of these are shared symmetrically.*

**What PPEs try to do:** Aggregate visible info (rate sheets) so brokers see *across* lenders. Doesn't solve asymmetry between lender ↔ borrower.

**Why it persists:** Asymmetry is endogenous to the business model. Lenders don't want to reveal hedge positions; borrowers can't credibly commit to a hold period.

---

## Problem 2 — Adverse Selection

**Definition (Akerlof, 1970, "Market for Lemons"):** Hidden quality differences cause better-quality counterparties to exit the market, leaving worse-quality ones — until the market collapses or seizes up.

**Historical instance:** Used-car markets, life insurance (sicker people buy more), medieval craft guilds (good craftsmen left guilds that protected bad ones).

**In mortgages today:**
- Borrowers most likely to refinance early are the ones lenders make the least money on.
- Investors price MBS *assuming* this selection ("burnout" models).
- Brokers who shop hardest (and most likely to fall out of a lock) are penalized via best-efforts pricing.

**What PPEs try to do:** Surface multiple options simultaneously, narrowing the spread that adverse selection requires.

**Why it persists:** Lender pricing must protect against the worst expected behavior; the better-than-average borrower subsidizes the worse.

---

## Problem 3 — The Stale-Price Problem

**Definition:** Quoted prices lag underlying market reality. The faster the market moves, the worse the lag.

**Historical instance:** Tulip mania (1637) — by the time tulip prices were posted in Amsterdam markets, growers in Haarlem already knew the bubble had burst.

**In mortgages today:**
- Daily rate sheets published at 9:30 AM ET assume morning TBA levels.
- A 30 bp intraday rally in MBS makes that morning sheet wrong by ~1.2 points.
- Reprice fires — but locks made before the reprice are honored at stale prices.

**What PPEs try to do:** Real-time API feeds, push-based reprice notifications, cache invalidation.

**Why it persists:** Lenders deliberately *want* some lag (gives them carry); brokers want zero lag. Trade-off between freshness and stability.

---

## Problem 4 — The Calculation-Cost Problem

**Definition:** The "right" price requires more computation than is feasible in the time you have.

**Historical instance:** 19th-century stock exchanges literally couldn't price 1,000 stocks in real-time — they had specialists by stock, runners by trade.

**In mortgages today:**
- Best-execution across 150 investors × 30 products × 60 rates × 6 lock periods × 50 borrower variables = ~270 million possible scenarios.
- Borrower waits ~3 seconds for a PPE quote — must compute in ~300 ms.
- Forces pre-computation, caching, and aggressive eligibility pruning.

**What PPEs do:** Eligibility filtering *before* pricing, hash-keyed adjuster lookups, parallelized investor APIs.

**Why it persists:** Scenario space grows faster than compute. New products (e.g., DSCR with rate buckets, temporary buydowns with subsidies) constantly expand it.

---

## Problem 5 — Fragmentation of Markets

**Definition:** When supply is split across many uncoordinated sellers, buyers can't easily compare.

**Historical instance:** Medieval European trade fairs — each city had its own weights, measures, and currencies; merchants needed money changers and weight-masters.

**In mortgages today:**
- 100+ wholesale lenders, each with proprietary rate sheets (PDF, XML, JSON, vendor-specific formats).
- Each with idiosyncratic LLPA naming, lock policies, and submission portals.
- No central exchange. No standardized API across all lenders.

**What PPEs do:** Build per-lender ingestion adapters; normalize into an internal canonical format.

**Why it persists:** Lenders *want* to differentiate. MISMO (the standard) exists for loan files but not for rate sheets. Network effects benefit incumbent PPEs (Optimal Blue, LoanSifter).

---

## Problem 6 — Multi-Objective Optimization

**Definition:** No single number captures "best." Different stakeholders have different objective functions.

**Historical instance:** A medieval guild pricing bread had to balance: bakers' livelihoods, peasants' subsistence, the lord's revenue, and the crown's grain reserve.

**In mortgages today:**
- Broker wants max net price (comp).
- Borrower wants min APR / min cash-to-close / min monthly payment — these can conflict.
- Lender wants max profit *given* pull-through.
- Regulator wants demonstrable benefit to borrower (anti-steering).

**What PPEs do:** Pareto-frontier displays; multi-axis ranking; "lowest rate / lowest pts / lowest fees" three-option presentations.

**Why it persists:** The objectives are *genuinely* different. There is no "right" weighting between them.

---

## Problem 7 — Predicting Optionality (Prepayment)

**Definition:** When the contract embeds an option (borrower can prepay), the security's value depends on uncertain future behavior.

**Historical instance:** Callable bonds in the 19th c. — investors demanded higher coupons to compensate for the issuer's right to refinance.

**In mortgages today:**
- Every fixed-rate mortgage gives the borrower a free option to prepay.
- This option's value depends on rates, borrower attributes, refi friction, originator marketing, and behavioral factors.
- Mis-pricing the option mis-prices the MBS, which mis-prices the rate sheet.

**What PPEs do:** Take TBA prices as input — they don't model prepayment themselves. The prepay model lives at the capital-markets desk and feeds the TBA market.

**Why it persists:** Prepay behavior is endogenous and human; no model captures it perfectly. Models systematically underpredict refi waves and overpredict burnout.

---

## Problem 8 — Eligibility ≠ Pricing

**Definition:** "Can I qualify?" and "What price?" are different questions, but conflated in practice.

**Historical instance:** Medieval moneylenders extended credit only to people they personally knew; price was a function of relationship, not formula.

**In mortgages today:**
- Eligibility = binary: does loan meet investor's underwriting rules?
- Pricing = continuous: at what rate/price is the loan offered?
- A borrower may be ineligible at investor A's lowest price but eligible at a higher price; eligible at investor B's slightly higher price overall.

**What PPEs do:** Two-stage architecture — eligibility filter first, then price the surviving products.

**Why it persists:** Underwriting rules are constantly updated (overlays) and rarely fully encoded. Some investor exceptions require human judgment.

---

## Problem 9 — The Regulatory-Pricing Tension

**Definition:** Pricing innovation runs ahead of regulation; regulation catches up by restricting price discrimination.

**Historical instance:** Just-price doctrine restricted usury; modern fair-lending laws restrict discriminatory loan pricing.

**In mortgages today:**
- LLPAs are *sanctioned* risk-based price discrimination.
- ML-driven personalized pricing is *unsanctioned* — would likely violate ECOA disparate-impact tests.
- The line between "risk pricing" (allowed) and "discrimination" (disallowed) is narrow and contested (cf. the 2023 LLPA controversy).

**What PPEs do:** Stay strictly inside the agency-LLPA framework; expose adjusters transparently; produce audit trails.

**Why it persists:** Society wants both efficient risk pricing and equal access. Those aren't perfectly compatible.

---

## Problem 10 — Trust in the Quoting System

**Definition:** Counterparties must believe the quoted price will be honored.

**Historical instance:** Lloyd's Coffee House (London, 1688) — informal insurance market that worked because of reputation, not contracts.

**In mortgages today:**
- A lock confirmation is a contract — but disputes around eligibility, pricing tolerance, and last-minute repricing are frequent.
- Worst-case relock policies test the trust.
- Concessions are how lenders maintain broker relationships despite disagreements.

**What PPEs do:** Audit trails — every quote stored with timestamp, sheet ID, and inputs.

**Why it persists:** Software bugs, sheet errors, and human discretion at the lock desk always create some uncertainty.

---

## Problem 11 — Pricing the Tail (Rare Scenarios)

**Definition:** Common scenarios get priced well; unusual ones get priced badly or not at all.

**Historical instance:** Insurance pricing of catastrophes — Hurricane Andrew (1992) bankrupted multiple insurers because tail-risk pricing was wrong.

**In mortgages today:**
- A 760 FICO, 75 LTV, owner-occ, conv refi has 100 lenders competing fiercely.
- A 680 FICO, 90 LTV, investment 3-unit, cash-out, in a flood zone, with a HELOC subordination — maybe 3 lenders will touch it, all at penalty pricing.
- Tail scenarios drive disproportionate broker frustration.

**What PPEs do:** Encode every adjuster, including the obscure ones; surface eligibility failures with reasons.

**Why it persists:** Lender economics don't justify investing in rare scenarios. Non-QM exists partially to fill this gap.

---

## Problem 12 — The Translation Problem

**Definition:** The borrower-facing price doesn't naturally map to the producer-facing price.

**Historical instance:** Restaurant pricing — the menu price doesn't tell you the wholesale cost of ingredients, kitchen labor, or table turnover economics.

**In mortgages today:**
- Borrower sees: rate, APR, monthly payment, cash to close.
- Broker sees: net price after LLPAs, after comp, after lock adjuster.
- Lender sees: TBA execution, SRP, hedge cost, comp paid out.
- Investor sees: coupon yield, prepay-adjusted yield, OAS.

PPEs must produce all four views from the same input scenario. Errors at translation boundaries cause most pricing disputes.

---

## Which problems LoanSifter / PPEs actually *solve*

| Problem | Solved | Reduced | Untouched |
|---|---|---|---|
| 1 — Information asymmetry | | ✅ (broker side) | (borrower side) |
| 2 — Adverse selection | | ✅ | |
| 3 — Stale prices | | ✅ (real-time feeds) | (lock-period staleness) |
| 4 — Calculation cost | ✅ (sub-second) | | |
| 5 — Fragmentation | ✅ (aggregation) | | |
| 6 — Multi-objective optimization | | ✅ (Pareto display) | |
| 7 — Prepay optionality | | | ✅ (capital markets does it) |
| 8 — Eligibility vs pricing | ✅ (two-stage) | | |
| 9 — Regulatory tension | | ✅ (audit trails) | |
| 10 — Trust | | ✅ (timestamped quotes) | |
| 11 — Tail pricing | | ✅ | |
| 12 — Translation | ✅ (multi-view) | | |

The unfinished work — borrower-side information asymmetry, lock-period staleness, prepay modeling — is what the next generation of PPEs is trying to attack.
