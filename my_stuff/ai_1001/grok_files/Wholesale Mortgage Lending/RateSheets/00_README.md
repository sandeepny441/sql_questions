# Rate Sheets — Wholesale Mortgage Lending

A sequential, prerequisite-aware learning path for understanding **rate sheets** in the wholesale mortgage lending channel, followed by the **mathematical formulas** that underlie every quoted price.

## How to use this folder
Read the files in numbered order. Each section builds on the prior ones. Sections 01–13 are vocabulary (jargon tables); sections 14–30 are mathematical formulas with worked examples.

## Part I — Vocabulary & Concepts

| # | Section | Focus |
|---|---------|-------|
| 01 | Mortgage Lending Foundations | Core lending vocabulary |
| 02 | Wholesale Channel Basics | Who's who in wholesale |
| 03 | Introduction to Rate Sheets | What a rate sheet is and why it exists |
| 04 | Anatomy of a Rate Sheet | Reading the grid: rates, prices, terms |
| 05 | Base Pricing & Par Rate | The starting point of all pricing |
| 06 | Loan Programs & Product Codes | Conforming, Govt, Jumbo, Non-QM |
| 07 | Loan-Level Price Adjustments (LLPAs) | Risk-based pricing add-ons |
| 08 | Pricing Adjusters & Caps | State, occupancy, property, cash-out hits |
| 09 | Rate Locks & Lock Periods | Pricing time value |
| 10 | Margin, SRP & Broker Compensation | How the broker gets paid |
| 11 | Pricing Engines & PPE Technology | Tools that consume rate sheets |
| 12 | Secondary Market & Investor Pricing | Where rate sheets come from |
| 13 | Advanced Rate Sheet Strategy | Reprice risk, best-ex, hedging |

## Part II — Mathematical Formulas

| # | Section | Focus |
|---|---------|-------|
| 14 | Math Formulas (Master Index) | Notation + topic index + cheat sheet |
| 15 | Price, Rate & BP Conversions | bp/ticks/32nds, price↔dollar, duration approx |
| 16 | Loan Ratios | LTV, CLTV, HCLTV, DTI, PITI |
| 17 | Amortization Schedule | P&I, balance, interest/principal split |
| 18 | APR | Reg Z APR, HPML/HOEPA, QM, APOR |
| 19 | Points, Rebates & Net Price | LLPA stacking, net price construction |
| 20 | Break-Even & Buydowns | Point BE, 3-2-1 / 2-1 / 1-0 subsidies |
| 21 | Lock & Extensions | Lock adjusters, extensions, worst-case relock |
| 22 | ARM Math | FIR, caps, floors, payment recast |
| 23 | Mortgage Insurance | BPMI, LPMI, FHA UFMIP/MIP, VA FF |
| 24 | Escrow & Cash-to-Close | Escrow setup, CTC, IPC caps |
| 25 | Broker Compensation | LPC/BPC, min/max plans |
| 26 | SRP & MSR Valuation | Servicing strip, MSR NPV, multiples |
| 27 | TBA & Secondary Pricing | 32nds, dollar roll, spec pool pay-ups |
| 28 | Pipeline & Hedging | Pull-through, hedge ratio, pair-off |
| 29 | Duration & Convexity | Macaulay, modified, effective, OAD |
| 30 | Best Execution | Cross-investor optimization |

## Notation conventions (used across math files)

| Symbol | Meaning |
|---|---|
| $L$ | Loan amount |
| $V$ | Property value $= \min(\text{Price}, \text{Appraisal})$ |
| $r$ | Annual note rate (decimal) |
| $i = r/12$ | Monthly periodic rate |
| $n$ | Total months |
| $M$ | Monthly P&I |
| $P$ | Price as % of par (100 = par) |
| $\Delta P$ | Price adjuster (signed) |

Math notation uses LaTeX (`$...$` inline, `$$...$$` display), rendered by Obsidian, GitHub, and most modern markdown viewers.
