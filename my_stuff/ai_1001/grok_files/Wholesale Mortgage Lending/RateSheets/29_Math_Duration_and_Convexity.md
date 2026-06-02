# 29 — Duration & Convexity Math

**Prerequisite:** 28 — Pipeline & Hedging

**Goal:** Quantify how MBS and pipeline prices respond to interest-rate moves using duration (first-order) and convexity (second-order). These are the mathematical engines behind hedge ratios and reprice triggers.

---

## 1. Macaulay Duration

Weighted average time of cash flows:
$$ \boxed{D_\text{Mac} = \frac{\sum_{k=1}^{n} t_k \cdot \dfrac{\text{CF}_k}{(1+y)^{t_k}}}{P}} $$

Where:
- $t_k$ = time of cash flow $k$ in years
- $\text{CF}_k$ = cash flow at $t_k$
- $y$ = yield to maturity
- $P$ = current price (= PV of all CFs)

### Worked Example (Simple Bond)
4-year annual-pay bond, 5% coupon, $100 face, $y = 6\%$:

| $t_k$ | CF | PV @ 6% | $t_k \cdot$ PV |
|---|---|---|---|
| 1 | 5 | 4.717 | 4.717 |
| 2 | 5 | 4.450 | 8.900 |
| 3 | 5 | 4.198 | 12.594 |
| 4 | 105 | 83.180 | 332.720 |
| **Σ** | | **96.535** | **358.931** |

$$ D_\text{Mac} = \frac{358.931}{96.535} = 3.72 \text{ years} $$

---

## 2. Modified Duration

$$ \boxed{D_\text{mod} = \frac{D_\text{Mac}}{1 + y/m}} $$

Where $m$ = compounding periods/year (12 for monthly).

For monthly-pay mortgages:
$$ D_\text{mod} = \frac{D_\text{Mac}}{1 + r/12} $$

### Worked Example
$D_\text{Mac} = 3.72$, $y = 6\%$ annual:
$$ D_\text{mod} = \frac{3.72}{1.06} = 3.51 $$

---

## 3. Price Sensitivity (First-Order)

$$ \boxed{\frac{\Delta P}{P} \approx -D_\text{mod} \cdot \Delta y} $$

Or equivalently:
$$ \Delta P \approx -D_\text{mod} \cdot P \cdot \Delta y $$

### Worked Example
$D_\text{mod} = 5$, $P = 100$, $\Delta y = +25 \text{ bp} = +0.0025$:
$$ \Delta P \approx -5 \cdot 100 \cdot 0.0025 = -1.25 \text{ points} $$

---

## 4. Effective Duration (For MBS with Embedded Option)

Numerical (model-based) approach:
$$ \boxed{D_\text{eff} = \frac{P_{-} - P_{+}}{2 \cdot P_0 \cdot \Delta y}} $$

Where:
- $P_{+}$ = price with yields shocked up by $\Delta y$
- $P_{-}$ = price with yields shocked down by $\Delta y$
- $P_0$ = baseline price

Captures path-dependence of prepayments.

### Worked Example
$P_0 = 100$, $P_{+} = 98.5$ at $+50$ bp, $P_{-} = 101.0$ at $-50$ bp:
$$ D_\text{eff} = \frac{101.0 - 98.5}{2 \cdot 100 \cdot 0.005} = \frac{2.5}{1.0} = 2.5 \text{ years} $$

Note: For an MBS, $D_\text{eff}$ may be much shorter than $D_\text{Mac}$ because falling rates trigger prepayments that cut cash flows short.

---

## 5. Convexity

Second-order curvature of price-yield relationship:
$$ \boxed{C = \frac{1}{P} \cdot \frac{d^2 P}{dy^2} = \frac{\sum_{k} t_k(t_k+1) \cdot \text{CF}_k / (1+y)^{t_k+2}}{P}} $$

Numerical / effective convexity:
$$ \boxed{C_\text{eff} = \frac{P_{+} + P_{-} - 2 P_0}{P_0 \cdot (\Delta y)^2}} $$

### Worked Example
$P_0 = 100$, $P_{+} = 98.5$, $P_{-} = 101.0$, $\Delta y = 0.005$:
$$ C_\text{eff} = \frac{98.5 + 101.0 - 200}{100 \cdot (0.005)^2} = \frac{-0.5}{0.0025} = -200 $$

Negative convexity! Classic MBS pattern.

---

## 6. Second-Order Price Approximation

$$ \boxed{\frac{\Delta P}{P} \approx -D_\text{mod} \cdot \Delta y + \frac{1}{2} \cdot C \cdot (\Delta y)^2} $$

### Worked Example
$D = 5$, $C = +60$ (positive — typical bullet bond), $\Delta y = +0.01$:
$$ \frac{\Delta P}{P} \approx -5 \cdot 0.01 + 0.5 \cdot 60 \cdot 0.0001 = -0.05 + 0.003 = -4.7\% $$

Convexity adds back 30 bp of the duration-implied loss.

For an MBS with negative convexity ($C = -100$), same $\Delta y$:
$$ \frac{\Delta P}{P} \approx -5 \cdot 0.01 + 0.5 \cdot (-100) \cdot 0.0001 = -0.05 - 0.005 = -5.5\% $$

Negative convexity *amplifies* losses in both directions.

---

## 7. Why MBS Have Negative Convexity

When yields **fall**:
- Borrowers refi → faster prepay → cash flows shorten → price doesn't rise as fast as a comparable bullet bond

When yields **rise**:
- Borrowers stay put → slower prepay → cash flows extend → price falls faster than a bullet

Mathematically:
$$ \frac{\partial \text{CF}_k}{\partial y} \neq 0 \text{ (cash flows are themselves rate-dependent)} $$

---

## 8. Key Rate Duration (KRD)

Price sensitivity to a shift in yield at specific tenor $t$:
$$ \text{KRD}_t = -\frac{1}{P} \cdot \frac{\partial P}{\partial y_t} $$

For a 30-year MBS, the dominant KRD buckets are the 5Y and 10Y points (because of expected prepay-shortened life).

Sum of KRDs = effective duration:
$$ D_\text{eff} = \sum_t \text{KRD}_t $$

---

## 9. Dollar Duration (DV01 / PVBP)

Dollar value of a 1 bp move:
$$ \boxed{\text{DV01} = D_\text{mod} \cdot P \cdot 0.0001} $$

### Worked Example
$D_\text{mod} = 5$, $P = 100$:
$$ \text{DV01} = 5 \cdot 100 \cdot 0.0001 = 0.05 \text{ price points per bp} $$

For \$1M notional:
$$ \text{DV01}_\$ = 0.05/100 \cdot 1{,}000{,}000 = \$500 \text{ per bp} $$

---

## 10. Hedge Ratio Using Duration Matching

To neutralize $L$ dollars of pipeline using hedge instrument of price $P_H$ and duration $D_H$:
$$ \boxed{H = L \cdot \frac{D_\text{pipeline}}{D_H} \cdot \frac{P_H}{P_\text{pipeline}}} $$

For matched-coupon TBA hedge of par-priced pipeline:
$$ H = L \cdot \frac{D_\text{pipeline}}{D_\text{TBA}} \approx L \quad \text{(when durations match)} $$

---

## 11. OAD (Option-Adjusted Duration)

Same as effective duration but computed using a stochastic interest-rate model and full prepayment model:
$$ \text{OAD} = \frac{P_{-} - P_{+}}{2 \cdot P_0 \cdot \Delta y} \quad \text{(via Monte Carlo)} $$

Where shocks are applied to the *entire path* of rates.

---

## 12. Spread Duration

Sensitivity to OAS shock:
$$ D_\text{spread} = -\frac{1}{P} \cdot \frac{\partial P}{\partial \text{OAS}} $$

For MBS this is close to effective duration; for credit-sensitive bonds it diverges sharply.

---

## 13. Duration & Convexity of a Pipeline

$$ D_\text{pipeline} = \frac{\sum_j L_j D_j}{\sum_j L_j} $$
$$ C_\text{pipeline} = \frac{\sum_j L_j C_j}{\sum_j L_j} $$

(Weighted-average by exposure.)

---

## 14. Duration Drift Over Time

As time passes and rates move, pipeline duration changes:
$$ \Delta D_\text{pipeline} \approx -1 \cdot \Delta t_\text{yrs} + \text{convexity term} $$

Roughly: each month, duration falls by ~1/12 year, requiring small rebalancing.

---

## 15. Empirical Mortgage Duration Examples

| Coupon | $D_\text{eff}$ (typical) |
|---|---|
| Discount (well below current rates) | 6.0–7.5 |
| At-the-money / current coupon | 4.5–6.0 |
| Slight premium (refi-able) | 2.0–4.0 |
| Deep premium (high refi-able) | 1.0–2.5 |

Convexity worsens as coupon moves into premium territory.

---

## 16. Summary Formula Table

| Quantity | Formula |
|---|---|
| Macaulay duration | $\sum t_k \text{PV}(CF_k) / P$ |
| Modified duration | $D_\text{Mac} / (1 + y/m)$ |
| Effective duration | $(P_{-} - P_{+}) / (2 P_0 \Delta y)$ |
| Price change (1st order) | $\Delta P/P \approx -D_\text{mod} \Delta y$ |
| Convexity (analytic) | $\sum t_k(t_k+1) \text{PV}(CF_k) / [P (1+y)^2]$ |
| Effective convexity | $(P_{+} + P_{-} - 2 P_0) / [P_0 (\Delta y)^2]$ |
| Price change (2nd order) | $\Delta P/P \approx -D \Delta y + 0.5 C (\Delta y)^2$ |
| DV01 | $D_\text{mod} \cdot P \cdot 0.0001$ |
| Hedge ratio (duration match) | $H = L \cdot D_L/D_H \cdot P_H/P_L$ |
| Pipeline duration | $\sum L_j D_j / \sum L_j$ |
| OAD (Monte Carlo) | $(P_{-} - P_{+}) / (2 P_0 \Delta y)$ |
