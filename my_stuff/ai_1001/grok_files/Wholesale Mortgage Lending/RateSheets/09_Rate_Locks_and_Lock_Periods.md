# 09 — Rate Locks & Lock Periods

**Prerequisite:** 08 — Pricing Adjusters & Caps

**Goal:** Understand how a rate moves from "quoted" to "locked," what a lock period actually buys, and the lifecycle of a lock (extend, relock, float-down, expire).

## Concepts covered
- The rate-lock contract and what binds whom
- Lock-period columns on the rate sheet and their cost in bps
- Extensions, expirations, and relocks
- Float vs lock and float-down options
- Worst-case repricing and lock policy

## Jargon

| # | Term | Definition |
|---|------|------------|
| 1 | Rate Lock | Lender's commitment to honor a rate/price for a defined period subject to terms. |
| 2 | Lock Confirmation | Written confirmation issued by the lock desk with rate, price, expiration. |
| 3 | Lock Desk | Wholesale lender's team that processes lock requests, extensions, and policy questions. |
| 4 | Lock Period | Days the lock is valid: commonly 15, 30, 45, 60, 75, 90. |
| 5 | Short-Term Lock | 15 or fewer days, typically post-CTC. |
| 6 | Long-Term Lock | 75+ days; higher hedge cost. |
| 7 | Lock Expiration Date | Last day the lock is valid for funding. |
| 8 | Lock Extension | Paid extension when funding will slip past expiration. |
| 9 | Extension Fee | Bp cost per day to extend (typical schedule: 7-day, 15-day tiers). |
| 10 | Float | Not locked; rate moves with the market. |
| 11 | Float-to-Lock | Locking after a period of floating. |
| 12 | Lock-to-Float | Breaking a lock to refloat (rare; usually penalized). |
| 13 | Float-Down Option | Lock with a one-time right to reduce the rate if markets improve. |
| 14 | Relock | Locking again after expiration, often at worst-case pricing. |
| 15 | Worst-Case Pricing | Greater of original lock price or current market price. |
| 16 | Best-Ex Relock | Rare alternative offering current market price after expiration. |
| 17 | Lock-and-Shop | Locking before a specific property is identified (TBD address). |
| 18 | TBD Lock | Same; pricing held while shopping for a home. |
| 19 | Extended Lock Program | 90/120/180-day locks for new construction or pipeline planning. |
| 20 | Lock Policy | Lender's published rules on cut-off times, extensions, relocks, worst-case. |
| 21 | Cut-Off Time | Daily deadline for new locks (e.g., 8:30 PM ET). |
| 22 | Reprice Lock Protection | Period (often a few minutes) after a reprice during which prior locks are honored. |
| 23 | Renegotiation | Repricing an existing lock when markets move significantly in borrower's favor (lender discretion). |
