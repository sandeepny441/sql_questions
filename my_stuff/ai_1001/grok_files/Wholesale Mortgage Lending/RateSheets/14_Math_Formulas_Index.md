# 14 — Mathematical Formulas in Mortgage Rate Sheets (Master Index)

**Prerequisite:** Sections 01–13 — know the vocabulary before learning the math.

**Goal:** Catalog every quantitative relationship a wholesale rate sheet (and the pricing workflow around it) relies on. Each topic below has its own `MM_Math_*.md` file with formulas, variable definitions, derivations, and worked examples.

> Math notation uses LaTeX rendered by KaTeX/MathJax. Inline: `$...$`. Display: `$$...$$`. Renders in Obsidian, GitHub, VS Code, and most modern markdown viewers.

---

## Universal Notation

These symbols appear consistently across every math file in this series.

| Symbol | Meaning | Units |
|---|---|---|
| $L$ | Loan amount (original UPB) | $ |
| $V$ | Property value $= \min(\text{Price}, \text{Appraisal})$ | $ |
| $r$ | Annual nominal note rate | decimal (0.0625 = 6.25%) |
| $i$ | Periodic (monthly) rate $= r/12$ | decimal |
| $n$ | Total number of monthly payments | months |
| $k$ | Payment-number index | $1 \le k \le n$ |
| $M$ | Monthly principal & interest payment | $ |
| $B_k$ | Remaining balance after payment $k$ | $ |
| $I_k$ | Interest portion of payment $k$ | $ |
| $\mathit{Pr}_k$ | Principal portion of payment $k$ | $ |
| $P$ | Price as percent of par (100.000 = par) | % |
| $\Delta P$ | Price adjuster (positive = credit, negative = hit) | points |
| $\text{bp}$ | Basis point ($1\,\text{bp} = 0.01\%$) | % |
| $T$ | Annual property tax | $ |
| $I_{ins}$ | Annual hazard insurance premium | $ |
| $\text{DTI}$ | Debt-to-income ratio | decimal |
| $\text{LTV}$ | Loan-to-value ratio | decimal |
| $s, g$ | Servicing fee, guarantee (g-) fee | decimal (annual) |
| $D$ | Duration (effective or modified) | years |
| $C$ | Convexity | years² |

---

## Topic Index

| # | File | Topic | What's inside |
|---|---|---|---|
| 15 | `15_Math_Price_Rate_and_BP.md` | Price, Rate & BP Conversions | bp/tick/price/dollar conversions |
| 16 | `16_Math_Loan_Ratios.md` | Loan Ratios | LTV, CLTV, HCLTV, DTI |
| 17 | `17_Math_Amortization_Schedule.md` | Amortization | P&I, balance, interest/principal split |
| 18 | `18_Math_APR.md` | APR & Amount Financed | Reg Z APR equation, APOR comparison |
| 19 | `19_Math_Points_Rebates_Net_Price.md` | Points, Rebates, Net Price | Discount math, LLPA stack, net price |
| 20 | `20_Math_Break_Even_and_Buydowns.md` | Break-Even & Buydowns | Point BE, temp & perm buydown subsidies |
| 21 | `21_Math_Lock_and_Extensions.md` | Lock Period Math | Lock adjusters, extensions, worst-case relock |
| 22 | `22_Math_ARM.md` | ARM Calculations | Fully-indexed rate, caps, floors, recast |
| 23 | `23_Math_Mortgage_Insurance.md` | MI / MIP / Funding Fees | BPMI, LPMI, FHA UFMIP/MIP, VA funding fee |
| 24 | `24_Math_Escrow_and_Cash_to_Close.md` | Escrow & CTC | Escrow setup, prepaids, cash-to-close |
| 25 | `25_Math_Broker_Compensation.md` | Broker Comp | LPC/BPC, min/max, dollar conversions |
| 26 | `26_Math_SRP_and_MSR.md` | SRP & MSR Valuation | SRP multiples, MSR present value |
| 27 | `27_Math_TBA_and_Secondary_Pricing.md` | TBA & Secondary | 32nds, roll, spec-pool pay-ups |
| 28 | `28_Math_Pipeline_and_Hedging.md` | Pipeline & Hedging | Pull-through, hedge ratio, pair-off |
| 29 | `29_Math_Duration_and_Convexity.md` | Duration & Convexity | Modified duration, convexity, MBS OAD |
| 30 | `30_Math_Best_Execution.md` | Best Execution | Cross-investor net price comparison |

---

## "Use Every Day" Cheat Sheet

Full derivations live in each per-topic file. These are the ten formulas a broker, AE, or capital-markets analyst uses constantly.

**1. Loan-to-Value**
$$ \text{LTV} = \frac{L}{V} $$

**2. Back-End DTI**
$$ \text{DTI} = \frac{\text{PITI} + \text{Other Monthly Debts}}{\text{Gross Monthly Income}} $$

**3. Monthly P&I (amortization)**
$$ M = L \cdot \frac{i\,(1+i)^n}{(1+i)^n - 1}, \qquad i = \frac{r}{12} $$

**4. Remaining Balance**
$$ B_k = L\,(1+i)^k - M \cdot \frac{(1+i)^k - 1}{i} $$

**5. Price in Dollars (Rebate / Discount)**
$$ \text{Price}_{\$} = \frac{P - 100}{100}\,L $$

**6. Net Price After Adjusters**
$$ P_\text{net} = P_\text{base} + \sum_{j} \Delta P_j $$

**7. Break-Even on Points (simple)**
$$ \text{BE} = \frac{\text{Points Paid}_\$}{M_{\text{high}} - M_{\text{low}}} \quad \text{(months)} $$

**8. ARM Fully-Indexed Rate**
$$ \text{FIR} = \text{Index} + \text{Margin} $$

**9. Pull-Through-Adjusted Hedge Notional**
$$ H = L_\text{pipeline} \times \text{PT} $$

**10. Modified Duration Price Sensitivity**
$$ \Delta P \approx -D_\text{mod} \cdot P \cdot \Delta y $$

---

## Reading Order

1. Start with `15` if you've never converted between bp/ticks/dollars.
2. `16` and `17` are the "must-know" computations behind every loan.
3. `18`–`23` cover the day-to-day broker math.
4. `24`–`25` cover what hits the borrower's wallet.
5. `26`–`30` are the capital-markets side: where the rate sheet *comes from*.
