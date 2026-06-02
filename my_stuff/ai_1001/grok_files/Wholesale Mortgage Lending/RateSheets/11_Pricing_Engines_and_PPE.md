# 11 — Pricing Engines & PPE Technology

**Prerequisite:** 10 — Margin, SRP & Broker Compensation

**Goal:** Understand how rate sheets are consumed by software — Product & Pricing Engines (PPE), eligibility logic, and LOS integrations — and the vocabulary you'll encounter in vendor demos and API docs.

## Concepts covered
- What a PPE does and why it replaces manual sheet reading
- Eligibility vs pricing logic
- The major commercial PPEs and integration points
- Rate sheet feeds, formats, and ingestion
- Best-execution searches across multiple investors

## Jargon

| # | Term | Definition |
|---|------|------------|
| 1 | PPE (Product & Pricing Engine) | Software that consumes rate sheets and returns eligible products/prices for a borrower scenario. |
| 2 | Optimal Blue | Leading commercial PPE. |
| 3 | Polly | Modern cloud-native PPE. |
| 4 | EPPS (Encompass Product & Pricing Service) | ICE's PPE bundled with Encompass. |
| 5 | Loansifter | Multi-investor PPE often used by brokers. |
| 6 | Mortech, LenderPrice, ARIVE PPE | Other PPE platforms. |
| 7 | LOS (Loan Origination System) | System of record for the loan (Encompass, Empower, BytePro, LendingPad, ARIVE, Calyx). |
| 8 | Rate Sheet Feed | Electronic feed of pricing data delivered to PPE (XML, JSON, proprietary). |
| 9 | MISMO | Industry XML standard; less common for sheets, dominant for loan data. |
| 10 | Eligibility Engine | Logic layer that determines if a loan qualifies for a product before pricing. |
| 11 | Eligibility Hit | Reason a loan is ruled out (e.g., LTV > 80 on investment cash-out). |
| 12 | Best Execution (Best-Ex) Search | PPE function returning the highest-net-priced eligible product across investors. |
| 13 | Scenario / Pricing Scenario | The set of borrower/loan inputs sent into a pricing call. |
| 14 | Quote | A PPE output: rate, price, lock period, eligible products. |
| 15 | Sticky Quote | A quote stored to a specific timestamp/sheet version for audit. |
| 16 | Lock Request | System message to the lender's lock desk to bind a quote. |
| 17 | Float Request | Scenario saved without committing. |
| 18 | Reprice Notification | System alert that current sheet has been replaced. |
| 19 | Adjuster Logic Tree | PPE's internal representation of stacked adjusters. |
| 20 | Cache Invalidation | Process of clearing stale sheets when a reprice fires. |
| 21 | Sandbox vs Production Feed | Test vs live pricing endpoints. |
| 22 | API Throttle | Rate-limit on pricing calls per minute. |
