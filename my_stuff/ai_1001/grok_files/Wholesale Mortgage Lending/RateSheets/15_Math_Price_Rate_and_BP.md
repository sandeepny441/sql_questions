# 15 — Price, Rate, and Basis Point Conversions

**Prerequisite:** 14 — Math Formulas Index

**Goal:** Convert fluently between the four ways pricing is quoted on a rate sheet: percentages, basis points, ticks (32nds), and dollar amounts. Every other math file assumes you can do these in your head.

---

## 1. Unit Definitions

### Basis Points
$$ 1\,\text{bp} = 0.01\% = 0.0001 $$
$$ 100\,\text{bp} = 1.00\% = 0.01 $$
$$ \text{bp} \to \text{decimal: } \quad x \mapsto \frac{x}{10{,}000} $$
$$ \text{decimal} \to \text{bp: } \quad y \mapsto y \times 10{,}000 $$

### Ticks (32nds — used in TBA / MBS markets)
$$ 1\,\text{tick} = \frac{1}{32}\,\text{point} = 0.03125 $$
$$ 1\,\text{half-tick (plus)} = \frac{1}{64} = 0.015625 $$
$$ 1\,\text{point} = 32\,\text{ticks} $$

### Reading 32nds Notation
A quote of $99\text{-}24$ means:
$$ 99 + \frac{24}{32} = 99.750 $$

A quote of $99\text{-}24\text{+}$ (the "plus" tick) means:
$$ 99 + \frac{24}{32} + \frac{1}{64} = 99.765625 $$

A quote of $101\text{-}08$ means:
$$ 101 + \frac{8}{32} = 101.250 $$

---

## 2. Price ↔ Dollar Conversion

For loan amount $L$ and quoted price $P$ (% of par):

$$ \boxed{\text{Price}_{\$} = \frac{P}{100} \cdot L} $$

For the **premium / discount portion only** (most useful at the lock desk):

$$ \boxed{\text{Rebate}_{\$} = \frac{P - 100}{100} \cdot L} $$

| Sign of $(P-100)$ | Meaning | Direction of Money |
|---|---|---|
| $> 0$ | Premium | Lender → Broker (rebate / lender credit) |
| $= 0$ | Par | No exchange |
| $< 0$ | Discount | Borrower → Lender (points) |

### Worked Example A — Premium
$L = \$400{,}000$, $P = 101.250$:
$$ \text{Rebate}_\$ = \frac{101.250 - 100}{100} \cdot 400{,}000 = 0.01250 \cdot 400{,}000 = \$5{,}000 $$

### Worked Example B — Discount
$L = \$400{,}000$, $P = 99.000$:
$$ \text{Discount}_\$ = \frac{100 - 99}{100} \cdot 400{,}000 = \$4{,}000 \text{ owed} $$

---

## 3. Points ↔ Dollars

$$ 1\,\text{point} = 1\% \text{ of } L $$
$$ \text{Point}_\$ = \frac{\text{Points}}{100} \cdot L $$

### Worked Example
$L = \$350{,}000$, $0.75$ point paid:
$$ 0.75\% \cdot 350{,}000 = \$2{,}625 $$

---

## 4. Bp ↔ Price Movement (Duration Approximation)

A small yield change moves price approximately by:

$$ \boxed{\Delta P \approx -D \cdot P \cdot \Delta y} $$

For current-coupon agency MBS, $D \approx 4.5\text{–}6$ years.

### Worked Example
A 25 bp rally ($\Delta y = -0.0025$), $D = 5$, $P \approx 100$:
$$ \Delta P \approx -5 \cdot 100 \cdot (-0.0025) = +1.25\,\text{points} $$

The classic lock-desk shortcut: **~25 bp yield move ≈ ~1 point price move**.

---

## 5. Inversion: Price Move → Implied Yield Change

$$ \Delta y \approx -\frac{\Delta P}{D \cdot P} $$

### Worked Example
Sheet improves by $+0.500$ points; $D = 5$, $P \approx 100$:
$$ \Delta y \approx -\frac{0.500}{5 \cdot 100} = -0.001 = -10\,\text{bp} $$

---

## 6. Note Rate → Coupon → Pool

The rate the borrower pays is split among investor, servicer, and guarantor:

$$ \boxed{\text{Coupon}_\text{investor} = r - s - g} $$

Where:
- $s$ = servicing fee (typically $0.25\%$ for agency)
- $g$ = guarantee fee paid to Fannie/Freddie/Ginnie (typically $0.40\text{–}0.60\%$)

### Worked Example
$r = 6.500\%$, $s = 0.25\%$, $g = 0.50\%$:
$$ \text{Coupon} = 6.500 - 0.25 - 0.50 = 5.750\% $$
Delivered into the nearest pool coupon (rounded down to 50 bp tick): **5.5 coupon pool**.

---

## 7. Effective Yield Including Up-Front Points

Borrower's effective annual cost when paying $p$ points on rate $r$:

$$ y_\text{eff} \approx r + \frac{p}{n_\text{eff}} $$

Where $n_\text{eff}$ is expected years to payoff (often 5–7, not the full 30).

### Worked Example
$r = 6.250\%$, paid 1 point, expected hold 7 years:
$$ y_\text{eff} \approx 6.250\% + \frac{1.000\%}{7} \approx 6.393\% $$

---

## 8. Common Adjuster Sizes — Quick Reference

| Adjustment | In Price Points | In Bp |
|---|---|---|
| $\frac{1}{8}\%$ rate increment (one grid row) | ≈ 0.500 | 50 bp |
| 1 full point | 1.000 | 100 bp |
| $\frac{1}{4}$ point | 0.250 | 25 bp |
| $\frac{1}{8}$ point | 0.125 | 12.5 bp |
| 1 tick (1/32) | 0.03125 | 3.125 bp |
| 5-day lock extension (typical) | 0.125 | 12.5 bp |
| 0.5% LLPA hit | 0.500 | 50 bp |

---

## 9. Dollar-Equivalent of a Bp on Various Loan Sizes

$$ \text{1 bp}_\$ = \frac{1}{10{,}000} \cdot L $$

| Loan Size $L$ | 1 bp = | 25 bp = | 100 bp = 1 point |
|---|---|---|---|
| \$200,000 | \$20 | \$500 | \$2,000 |
| \$400,000 | \$40 | \$1,000 | \$4,000 |
| \$600,000 | \$60 | \$1,500 | \$6,000 |
| \$1,000,000 | \$100 | \$2,500 | \$10,000 |

---

## 10. Summary Formula Table

| Quantity | Formula |
|---|---|
| Bp → decimal | $x / 10{,}000$ |
| Decimal → bp | $y \times 10{,}000$ |
| Ticks → points | $t / 32$ |
| 32nds notation → decimal | $a\text{-}b \mapsto a + b/32$ |
| Price in dollars | $\text{Price}_\$ = (P/100) \cdot L$ |
| Rebate / discount dollars | $(P-100)/100 \cdot L$ |
| Points in dollars | $(p / 100) \cdot L$ |
| Coupon from note rate | $c = r - s - g$ |
| Price move from yield | $\Delta P \approx -D \cdot P \cdot \Delta y$ |
| Yield move from price | $\Delta y \approx -\Delta P / (D \cdot P)$ |
| Effective yield with points | $r + p / n_\text{eff}$ |
| 1 bp in dollars | $L / 10{,}000$ |
