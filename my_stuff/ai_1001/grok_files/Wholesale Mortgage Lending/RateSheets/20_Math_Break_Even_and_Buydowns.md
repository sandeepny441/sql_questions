# 20 — Break-Even & Buydown Math

**Prerequisite:** 17 — Amortization; 19 — Points & Net Price

**Goal:** Quantify whether paying points (permanent buy-down) or funding a temporary buydown is economically rational, and how subsidy costs are calculated.

---

## 1. Simple Break-Even on Discount Points

How many months until monthly P&I savings recover the up-front cost?

$$ \boxed{\text{BE}_\text{months} = \frac{\text{Points Paid}_\$}{M_\text{high} - M_\text{low}}} $$

Where:
- $M_\text{high}$ = monthly P&I at higher (no-points) rate
- $M_\text{low}$ = monthly P&I at lower (with-points) rate

### Worked Example
$L = \$400{,}000$, $n = 360$:

| Scenario | Rate | $M$ |
|---|---|---|
| No points | 6.500% | \$2,528.27 |
| 1 point ($\$4{,}000$) | 6.250% | \$2,462.87 |

$$ \text{BE} = \frac{4{,}000}{2{,}528.27 - 2{,}462.87} = \frac{4{,}000}{65.40} \approx 61.2 \text{ months} \approx 5.1 \text{ years} $$

If borrower expects to hold > 5.1 years, paying the point is rational.

---

## 2. After-Tax Break-Even

For an itemizer in marginal tax bracket $t$:

$$ \text{BE}_\text{after-tax} = \frac{\text{Points}_\$ \cdot (1 - t)}{(M_\text{high} - M_\text{low})(1 - t)} = \frac{\text{Points}_\$}{M_\text{high} - M_\text{low}} $$

Tax effect on points (deductible up front on purchases; amortized on refis) often roughly cancels tax effect on monthly interest — but for refis the up-front deductibility lag matters.

---

## 3. NPV Break-Even (Time Value of Money)

Find $n^*$ such that:
$$ \text{Points}_\$ = \sum_{k=1}^{n^*} \frac{M_\text{high} - M_\text{low}}{(1 + d)^k} $$

Where $d$ is the borrower's monthly discount rate (often opportunity cost / risk-free rate / 12).

$$ n^* = \frac{-\ln\!\left(1 - \dfrac{\text{Points}_\$ \cdot d}{M_\text{high} - M_\text{low}}\right)}{\ln(1+d)} $$

### Worked Example
Using §1 numbers with $d = 0.004$/mo (≈ 5% annual):
$$ n^* = \frac{-\ln(1 - 4{,}000 \cdot 0.004 / 65.40)}{\ln(1.004)} \approx 71 \text{ months} $$

Time value extends break-even from 61 → 71 months.

---

## 4. Cost-Per-Bp of Buydown

$$ \text{Cost per bp rate reduction} = \frac{\text{Points}_\$}{\text{bp reduction}} $$

### Worked Example
1 point ($\$4{,}000$) bought down rate by 25 bp:
$$ \text{Cost/bp} = \frac{4{,}000}{25} = \$160/\text{bp} $$

A 25 bp reduction "costs" \$160 per bp. Useful for comparing buy-down deals.

---

## 5. Permanent Rate Buy-Up Economics

Borrower takes a higher rate to receive lender credit (LC):
$$ \text{LC}_\$ = (P_\text{higher rate} - P_\text{lower rate}) \cdot \frac{L}{100} $$

Break-even for buy-up:
$$ \text{BE}_\text{up} = \frac{\text{LC}_\$}{M_\text{higher} - M_\text{lower}} $$

If borrower holds **less than** BE months, buying up wins.

---

## 6. Temporary Buydown — Mechanics

Borrower pays the note rate $r$, but during the buydown period, payments are computed at a reduced rate. Subsidy is escrowed up front.

| Year | 3-2-1 | 2-1 | 1-0 |
|---|---|---|---|
| 1 | $r - 3\%$ | $r - 2\%$ | $r - 1\%$ |
| 2 | $r - 2\%$ | $r - 1\%$ | $r$ |
| 3 | $r - 1\%$ | $r$ | $r$ |
| 4+ | $r$ | $r$ | $r$ |

---

## 7. Monthly Payment During Buydown Year $y$

$$ M_y = L \cdot \frac{i_y\,(1+i_y)^n}{(1+i_y)^n - 1}, \qquad i_y = \frac{r - b_y}{12} $$

Where $b_y$ = buydown decrement for year $y$ (e.g., 3, 2, 1, 0 percentage points).

Note: This is a *qualifying* payment calculation. Borrower still owes the full P&I at note rate; the subsidy covers the difference.

---

## 8. Buydown Subsidy Cost (Per Year)

$$ S_y = 12 \cdot (M_\text{note} - M_y) $$

Total subsidy for a 3-2-1:
$$ S_\text{total} = S_1 + S_2 + S_3 = 12 \cdot \bigl[ (M_\text{note} - M_1) + (M_\text{note} - M_2) + (M_\text{note} - M_3) \bigr] $$

### Worked Example (3-2-1)
$L = \$400{,}000$, $r = 7.000\%$, $n = 360$, $M_\text{note} = \$2{,}661.21$.

| Year | Effective Rate | $M_y$ | Annual Subsidy |
|---|---|---|---|
| 1 | 4.000% | \$1,909.66 | $12 \cdot (2{,}661.21 - 1{,}909.66) = \$9{,}019$ |
| 2 | 5.000% | \$2,147.29 | $12 \cdot (2{,}661.21 - 2{,}147.29) = \$6{,}167$ |
| 3 | 6.000% | \$2,398.20 | $12 \cdot (2{,}661.21 - 2{,}398.20) = \$3{,}156$ |
| **Total** | | | **\$18,342** |

---

## 9. 2-1 Buydown Subsidy

$$ S_{2\text{-}1} = 12 \cdot \bigl[ (M_\text{note} - M_1) + (M_\text{note} - M_2) \bigr] $$

For above scenario (years 1 & 2 only):
$$ S_{2\text{-}1} = 9{,}019 + 6{,}167 = \$15{,}186 $$

---

## 10. 1-0 Buydown Subsidy

$$ S_{1\text{-}0} = 12 \cdot (M_\text{note} - M_1) $$

For above scenario:
$$ S_{1\text{-}0} = \$9{,}019 $$

---

## 11. Subsidy as % of Loan

$$ S_\% = \frac{S_\text{total}}{L} $$

### Worked Example (3-2-1 above)
$$ S_\% = \frac{18{,}342}{400{,}000} = 4.59\% \text{ of loan} $$

This is what the seller/builder/lender funds at closing.

---

## 12. Who Pays Buydown Subsidy?

Subsidy can be funded by:
- **Seller concession** — limited by IPC (Interested Party Contribution) caps:
  - Conventional 80% LTV: 6%, 80.01–90%: 6%, > 90%: 3%, investment: 2%
  - FHA: 6% regardless of LTV
  - VA: 4% (plus VA-allowable charges)
- **Lender credit** (from premium pricing)
- **Builder concession**
- **Borrower's own funds** (rare; defeats the purpose)

Cap check:
$$ S_\text{total} \le \text{IPC}_\text{max} \cdot L $$

---

## 13. Buydown Account Balance Over Time

After $k$ months into buydown:
$$ \text{Buydown Balance}_k = S_\text{total} - \sum_{j=1}^{k}(M_\text{note} - M_{j,\text{year}}) $$

Should reach zero exactly when buydown ends.

---

## 14. Comparison: Permanent vs Temporary Buydown

| Metric | Permanent (points) | Temporary (3-2-1) |
|---|---|---|
| Up-front cost (typical) | ~1–2% of $L$ per 25 bp | ~3–5% of $L$ |
| Payment relief horizon | Life of loan | 3 years only |
| Helps qualifying? | Yes (lower note rate) | Per Reg, qualify at full note rate (most cases) |
| Break-even months | 40–80 typical | N/A — subsidy fully consumed in 36 mo |
| Refi destroys benefit? | Yes (lose unused points) | Yes (forfeit remaining subsidy in some structures) |

---

## 15. Buydown Funds on Refi or Sale

If borrower refis or sells before buydown ends, the unused subsidy is typically credited toward the payoff:
$$ \text{Refund}_\text{at month } k = S_\text{total} - \sum_{j=1}^{k}(M_\text{note} - M_{j,\text{year}}) $$

Some lenders credit to principal; others refund to borrower.

---

## 16. Summary Formula Table

| Quantity | Formula |
|---|---|
| Simple BE (months) | $\text{Points}_\$ / (M_\text{high} - M_\text{low})$ |
| NPV BE | $n^* = -\ln(1 - \text{Pts} \cdot d / \Delta M) / \ln(1+d)$ |
| Cost per bp | $\text{Pts}_\$ / \text{bp reduced}$ |
| Buy-up BE | $\text{LC}_\$ / (M_\text{higher} - M_\text{lower})$ |
| Buydown rate yr $y$ | $i_y = (r - b_y)/12$ |
| Buydown annual subsidy | $S_y = 12 \cdot (M_\text{note} - M_y)$ |
| Total 3-2-1 subsidy | $\sum_{y=1}^{3} S_y$ |
| Subsidy as % loan | $S_\text{total} / L$ |
| IPC cap check | $S_\text{total} \le \text{IPC}_\text{max} \cdot L$ |
| Unused refund | $S_\text{total} - \sum \text{used}$ |
