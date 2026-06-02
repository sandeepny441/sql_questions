# 25 — Broker Compensation Math

**Prerequisite:** 19 — Points, Rebates & Net Price

**Goal:** Convert broker compensation plans (LPC %, BPC %, min/max constraints) into dollar amounts and into the price-point equivalents that flow through the rate sheet.

---

## 1. LPC (Lender-Paid Comp) Dollars

$$ \boxed{C_\text{LPC} = c \cdot L} $$

Where $c$ = comp plan as decimal (e.g., $2.000\% = 0.0200$).

### Worked Example
Comp plan 2.50%, $L = \$400{,}000$:
$$ C_\text{LPC} = 0.025 \cdot 400{,}000 = \$10{,}000 $$

---

## 2. LPC in Price Points

$$ C_\text{LPC, points} = c \cdot 100 $$

A 2.50% comp = 2.500 points subtracted from rate-sheet price.

$$ P_\text{broker-facing} = P_\text{net} - C_\text{LPC, points} $$

### Worked Example
$P_\text{net} = 101.250$, comp 2.000%:
$$ P_\text{broker-facing} = 101.250 - 2.000 = 99.250 $$

---

## 3. BPC (Borrower-Paid Comp)

$$ C_\text{BPC} = c \cdot L $$

Same dollar amount as LPC, but **paid by borrower at closing** (not from price). Rate sheet shows pricing **net of comp** (the broker keeps the entire visible rebate).

### Worked Example
$L = \$400{,}000$, BPC 2.00%:
$$ C_\text{BPC} = \$8{,}000 \text{ paid at closing} $$
$$ P_\text{broker-facing} = P_\text{net} \text{ (unmodified)} $$

---

## 4. Min/Max Comp Constraints

Most comp plans are tiered: a percentage **with** floor and ceiling dollar amounts:

$$ \boxed{C_\text{actual} = \max\bigl(C_\text{min},\, \min(C_\text{max},\, c \cdot L)\bigr)} $$

### Typical Plan Structure
- 2.00% comp
- \$2,000 minimum
- \$10,000 maximum

### Worked Examples (Plan above)

| Loan $L$ | $c \cdot L$ | After Constraints | Effective % |
|---|---|---|---|
| \$80,000 | \$1,600 | **\$2,000** (min binds) | 2.50% |
| \$250,000 | \$5,000 | \$5,000 | 2.00% |
| \$500,000 | \$10,000 | \$10,000 | 2.00% |
| \$750,000 | \$15,000 | **\$10,000** (max binds) | 1.33% |

---

## 5. Effective Comp Percentage (When Caps Bind)

$$ c_\text{eff} = \frac{C_\text{actual}}{L} $$

For small loans (min binds):
$$ c_\text{eff} = \frac{C_\text{min}}{L} > c $$

For large loans (max binds):
$$ c_\text{eff} = \frac{C_\text{max}}{L} < c $$

---

## 6. Comp-as-Price Conversion (With Min/Max)

$$ C_\text{LPC, points} = \frac{C_\text{actual}}{L} \cdot 100 $$

### Worked Example
$L = \$80{,}000$, comp = \$2,000 (min binds):
$$ C_\text{points} = \frac{2{,}000}{80{,}000} \cdot 100 = 2.500 \text{ points} $$
$$ P_\text{broker-facing} = P_\text{net} - 2.500 $$

---

## 7. Comp Plan Change Math

Brokers change LPC plans on a published schedule (typically monthly or quarterly with NMLS-level filings). For loan $L$:

$$ C_\text{plan A vs plan B} = (c_A - c_B) \cdot L $$

The broker chooses the plan optimizing expected total comp across their pipeline:
$$ \text{Expected Comp}_\text{plan } i = \sum_\text{loans} \max\bigl(C_{\min,i},\, \min(C_{\max,i},\, c_i \cdot L_j)\bigr) $$

---

## 8. Dual Compensation Prohibition (Reg Z)

For a single loan, broker may collect from **either** lender **or** borrower, never both:

$$ C_\text{LPC} + C_\text{BPC} = C_\text{actual} $$
subject to: exactly one of $C_\text{LPC}$, $C_\text{BPC}$ is non-zero.

---

## 9. LPC vs BPC — Borrower Cost Comparison

For the same comp percentage, borrower's all-in cost may differ:

### LPC Scenario
$$ \text{Rate}_\text{LPC} = r + \Delta r_\text{LPC} $$
Borrower pays slightly higher rate; no separate broker fee at closing.

### BPC Scenario
$$ \text{Rate}_\text{BPC} = r \text{ (lower)} $$
Borrower pays $C_\text{BPC}$ at closing.

### Break-Even Hold Period
$$ h^* = \frac{C_\text{BPC,\$}}{\Delta M_\text{LPC vs BPC monthly}} $$

If borrower holds < $h^*$ months, LPC wins (lower up-front).
If borrower holds > $h^*$, BPC wins (lower long-term rate).

### Worked Example
$L = \$400{,}000$, comp 2.00%, BPC payment \$8,000, LPC rate adder = 25 bp:

LPC $M$ at 6.500% → $\$2{,}528.27$. 
BPC $M$ at 6.250% → $\$2{,}462.87$.
$\Delta M = \$65.40$/mo.

$$ h^* = \frac{8{,}000}{65.40} \approx 122 \text{ months} \approx 10.2 \text{ years} $$

---

## 10. Concession to Broker (Lender Discretion)

When pricing tolerance / file issues arise, lender may concede:

$$ C_\text{adj} = C_\text{LPC} + \text{Concession} $$

Concession typically capped:
$$ \text{Concession} \le \min(C_\text{LPC}, \$Y) $$

Where $\$Y$ is lender's max concession (often \$1,500–\$2,500 per loan).

---

## 11. Premium Recapture (Comp Cap on Pricing)

When sheet premium exceeds broker comp + lender's required cushion:
$$ \text{Recapture} = \max(0, \text{Premium} - C_\text{LPC} - \text{Lender Margin}) $$

Excess premium is kept by lender, not paid out to broker.

---

## 12. Min Loan Amount Where Plan Yields Min Comp

$$ L^* = \frac{C_\text{min}}{c} $$

Below $L^*$, the floor binds and effective $c$ rises sharply.

### Worked Example
$C_\text{min} = \$2{,}000$, $c = 2.000\%$:
$$ L^* = \frac{2{,}000}{0.02} = \$100{,}000 $$

Loans below \$100k pay the broker a fixed \$2,000.

---

## 13. Max Loan Amount Where Plan Yields Max Comp

$$ L^{**} = \frac{C_\text{max}}{c} $$

Above $L^{**}$, the ceiling binds.

### Worked Example
$C_\text{max} = \$10{,}000$, $c = 2.000\%$:
$$ L^{**} = \frac{10{,}000}{0.02} = \$500{,}000 $$

Loans above \$500k cap broker at \$10,000.

---

## 14. Profitability of Loan to Broker (Simplified)

$$ \text{Broker Net} = C_\text{actual} - \text{Loan Officer Comp} - \text{Processing Cost} - \text{Office Allocation} $$

Common breakdown: ~60% to LO, ~10% processing, ~10% overhead, ~20% retained.

---

## 15. Anti-Steering Safe Harbor (Reg Z §1026.36(e))

Broker must present at least three options including:
1. Loan with lowest interest rate
2. Loan with lowest total dollar amount of discount/origination points
3. Loan with lowest total points + fees

$$ \text{Options} = \{ L_\text{lowest rate}, L_\text{lowest points}, L_\text{lowest fees} \} $$

---

## 16. Summary Formula Table

| Quantity | Formula |
|---|---|
| LPC dollars | $C_\text{LPC} = c \cdot L$ |
| LPC in points | $c \cdot 100$ |
| Broker-facing price | $P_\text{net} - c \cdot 100$ |
| Constrained comp | $\max(C_\text{min}, \min(C_\text{max}, c \cdot L))$ |
| Effective % | $C_\text{actual} / L$ |
| Comp-as-points (with caps) | $(C_\text{actual}/L) \cdot 100$ |
| LPC vs BPC BE (months) | $C_\text{BPC,\$} / (M_\text{LPC} - M_\text{BPC})$ |
| Min loan for plan rate | $L^* = C_\text{min}/c$ |
| Max loan for plan rate | $L^{**} = C_\text{max}/c$ |
| Premium recapture | $\max(0, \text{Prem} - C_\text{LPC} - \text{Margin})$ |
