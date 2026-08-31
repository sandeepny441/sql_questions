# 05 — Base Pricing & Par Rate

**Prerequisite:** 04 — Anatomy of a Rate Sheet

**Goal:** Understand how the unadjusted base price is built, where par lives on the grid, and how MBS markets drive the daily base.

## Concepts covered
- Where base price comes from (MBS → coupon → base price)
- The relationship between rate, price, and lender yield
- Identifying par on the grid and reading premium vs discount
- Why base price changes daily, sometimes intraday

## Jargon

| # | Term | Definition |
|---|------|------------|
| 1 | Base Price | Pre-adjustment price tied to a specific rate and lock period. |
| 2 | Par Rate | The rate on the sheet priced closest to 100.000. |
| 3 | Premium (Above Par) | Price > 100; lender pays a rebate. |
| 4 | Discount (Below Par) | Price < 100; borrower pays points. |
| 5 | Tick | 1/32 of a point in bond pricing (used in MBS markets). |
| 6 | Basis Point (bp) | 1/100 of 1% (0.01%). |
| 7 | Coupon Rate | The rate of the underlying MBS security into which the loan will be pooled. |
| 8 | Note Rate vs Coupon | Note rate is what the borrower pays; coupon is what flows to investors after servicing fee. |
| 9 | TBA (To-Be-Announced) Market | Forward MBS market that drives daily base pricing for agency loans. |
| 10 | Live Pricing / Live Market | Real-time price feed used by lenders to publish or reprice the sheet. |
| 11 | MBS (Mortgage-Backed Security) | Bond backed by a pool of mortgages; primary funding source for conforming loans. |
| 12 | Agency MBS | Pools guaranteed by Fannie Mae, Freddie Mac, or Ginnie Mae. |
| 13 | Pricing Bucket | A range of coupons that share similar economics in the TBA market. |
| 14 | Roll | Movement from one delivery month to the next in TBA; affects daily base price. |
| 15 | Spread to TBA / Spread to Coupon | Lender's margin added to TBA price to arrive at the broker-facing base price. |
| 16 | Servicing-Released vs Servicing-Retained | Whether the loan is sold with or without the future servicing rights; affects the base price. |
| 17 | Concession / Lender Margin | Profit margin baked into the base before adjusters. |
