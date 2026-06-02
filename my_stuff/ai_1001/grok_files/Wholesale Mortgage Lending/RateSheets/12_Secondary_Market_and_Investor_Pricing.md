# 12 — Secondary Market & Investor Pricing

**Prerequisite:** 11 — Pricing Engines & PPE Technology

**Goal:** Trace a rate sheet's price back to its source — the secondary market — and understand how MBS trading, hedging, and investor commitments shape what a broker sees.

## Concepts covered
- Primary vs secondary mortgage market
- How TBA trading determines daily base
- Cash window vs MBS execution
- Specified pools and pay-ups
- Hedge desks, pipeline management, and why reprices happen

## Jargon

| # | Term | Definition |
|---|------|------------|
| 1 | Primary Market | Origination of new loans to consumers. |
| 2 | Secondary Market | Sale, securitization, and trading of closed loans. |
| 3 | GSE (Government-Sponsored Enterprise) | Fannie Mae & Freddie Mac. |
| 4 | Fannie Mae (FNMA) | Buys conventional conforming loans; issues MBS. |
| 5 | Freddie Mac (FHLMC) | Same as Fannie; UMBS issuer. |
| 6 | Ginnie Mae (GNMA) | Government guarantor of FHA/VA/USDA MBS. |
| 7 | UMBS (Uniform MBS) | Single security platform combining Fannie & Freddie pools. |
| 8 | TBA (To-Be-Announced) | Forward-traded generic MBS contract. |
| 9 | Specified Pool | MBS pool with defined characteristics (e.g., low loan balance, NY, high LTV) that trades at a premium. |
| 10 | Pay-Up | Premium over TBA for specified-pool features. |
| 11 | Cash Window | Selling closed loans individually to Fannie/Freddie for cash. |
| 12 | MBS Execution | Pooling loans and delivering an MBS in exchange for the security. |
| 13 | Best Execution (Sec. Market) | Choosing between cash, MBS, and AOT/whole-loan to maximize proceeds. |
| 14 | AOT (Assignment of Trade) | Assigning a TBA position to an investor as part of whole-loan sale. |
| 15 | Whole Loan Sale | Selling individual closed loans (not pooled) to an investor. |
| 16 | Forward Commitment | Agreement to deliver loans at a future date and price. |
| 17 | Mandatory Commitment | Forward commitment with delivery obligation; better pricing. |
| 18 | Best-Efforts Commitment | No delivery obligation; weaker pricing. |
| 19 | Pipeline | All loans in process between application and sale. |
| 20 | Hedge Desk / Capital Markets Desk | Internal team trading TBAs/treasuries to hedge pipeline duration risk. |
| 21 | Pull-Through Rate | % of locked loans expected to fund; drives hedge ratio. |
| 22 | Reprice (Driver) | Reprice fires when intraday TBA moves a defined number of ticks. |
| 23 | Pair-Off Fee | Cost of unwinding a hedge when pull-through misses. |
| 24 | Investor Sheet / Bulk Sheet | Pricing published by aggregators to correspondents. |
| 25 | Co-Issue / MSR Flow | Sale of servicing rights separately from the loan itself. |
| 26 | MSR (Mortgage Servicing Rights) | Asset representing future servicing income; valued and traded. |
| 27 | Loan-Level Pricing (Cash Window) | Per-loan price returned by Fannie/Freddie pricing APIs (LPA Direct, PE Whole Loan). |
