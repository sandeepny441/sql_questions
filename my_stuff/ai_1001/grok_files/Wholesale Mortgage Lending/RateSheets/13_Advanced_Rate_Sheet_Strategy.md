# 13 — Advanced Rate Sheet Strategy

**Prerequisite:** 12 — Secondary Market & Investor Pricing

**Goal:** Tie everything together — read a sheet through a capital-markets lens, anticipate reprices, identify mispricings across investors, and make best-execution decisions for the broker and the borrower.

## Concepts covered
- Cross-investor best-ex on the same scenario
- Reprice prediction using TBA market signals
- Stack optimization (rate vs price vs comp)
- Lock-period selection as an economic decision
- Reading reprice notices and reverse-engineering the lender's hedge stance

## Jargon

| # | Term | Definition |
|---|------|------------|
| 1 | Best-Ex Strategy | Systematically choosing the highest-net-price eligible offer across lenders. |
| 2 | Stack Optimization | Re-engineering the loan attributes (e.g., shifting LTV across a bucket break) to improve LLPA outcomes. |
| 3 | Bucket Break | The exact FICO/LTV boundary where pricing jumps; key target for optimization. |
| 4 | Cliff Adjuster | Adjuster that changes sharply at a threshold (vs gradual). |
| 5 | Crossover Rate | The rate at which two pricing strategies (e.g., BPC vs LPC) deliver equal economics. |
| 6 | Effective Yield | APR-equivalent yield accounting for all rebate, comp, and adjusters. |
| 7 | Break-Even Analysis | Months to recover discount points via lower payment. |
| 8 | Rate Sheet Arbitrage | Exploiting price differences between investors on identical scenarios. |
| 9 | Reprice Risk | Probability current sheet will be republished worse before lock can be secured. |
| 10 | TBA Tick Watch | Monitoring intraday MBS moves to anticipate reprices. |
| 11 | Reprice Threshold | Bp move in TBA that historically triggers a given lender's reprice (often 25–37 bp). |
| 12 | Reprice for the Worse | Sheet republished with lower prices. |
| 13 | Reprice for the Better | Sheet republished with higher prices. |
| 14 | Lock Timing | Tactical decision of when to lock relative to expected reprice direction. |
| 15 | Float Strategy | Deliberate decision to float in expectation of a rally. |
| 16 | Renegotiation Threshold | Market move at which lender will entertain a lock renegotiation (often 25–50 bp). |
| 17 | Pipeline Hedge Coverage Ratio | Hedge notional ÷ pipeline notional, adjusted for pull-through. |
| 18 | Duration / Convexity | Bond-market measures of sensitivity that drive hedge sizing. |
| 19 | Lender Profitability Margin | Spread the lender embeds between secondary execution and the broker-facing price. |
| 20 | Sheet Velocity | How often a lender reprices intraday; a tell for hedge aggressiveness. |
| 21 | Stale Quote Risk | Risk of acting on an outdated price; mitigated by lock confirmations and PPE cache invalidation. |
| 22 | Cure / Curtailment | Post-close adjustment if a pricing tolerance is missed. |
| 23 | Audit Trail | Full timestamped history of pricing scenarios, lock requests, and confirmations — required for QC and exams. |
