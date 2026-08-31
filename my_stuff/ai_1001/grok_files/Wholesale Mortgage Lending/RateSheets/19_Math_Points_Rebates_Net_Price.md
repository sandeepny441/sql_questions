# 19 — Points, Rebates & Net Price Math

**Prerequisite:** 15 — Price/Rate/BP Conversions; 16 — Loan Ratios

**Goal:** Compose a final all-in price from the base grid price plus every adjuster (LLPA + lender overlays), and convert it to dollars from any of the perspectives (broker, lender credit, borrower discount).

---

## 1. Points & Rebates — Dollar Conversions

### Discount Points (Borrower-Paid)
$$ \text{Points}_\$ = \frac{p}{100} \cdot L $$

Where $p$ is points expressed as a percent (e.g., $1.000$ point = 1%).

### Rebate (Lender Credit)
$$ \text{Rebate}_\$ = \frac{P - 100}{100} \cdot L \quad \text{for } P > 100 $$

### Discount Cost (Borrower)
$$ \text{Discount}_\$ = \frac{100 - P}{100} \cdot L \quad \text{for } P < 100 $$

### Lender Credit (Premium-Funded)
$$ \text{LC}_\$ = \frac{P - 100}{100} \cdot L \quad \text{(equal to Rebate when broker passes all premium to borrower)} $$

---

## 2. The LLPA Stack

The full price adjustment is the algebraic sum of all individual adjusters:

$$ \boxed{\Delta P_\text{total} = \sum_{j} \Delta P_j} $$

Where each $\Delta P_j$ is signed:
- **Negative** = price hit (worse for broker)
- **Positive** = price credit (better for broker)

### Common Adjuster Components
$$ \Delta P_\text{total} = \Delta P_\text{FICO/LTV} + \Delta P_\text{occupancy} + \Delta P_\text{property} + \Delta P_\text{purpose} + \Delta P_\text{loan\_amt} + \Delta P_\text{state} + \Delta P_\text{lock} + \Delta P_\text{escrow} + \ldots $$

---

## 3. Net Price (Pre-Comp)

$$ \boxed{P_\text{net} = P_\text{base} + \Delta P_\text{total}} $$

In dollar terms:
$$ P_\text{net,\$} = \frac{P_\text{net} - 100}{100} \cdot L $$

### Worked Example
Base price $P_\text{base} = 100.875$. Adjusters:

| Adjuster | $\Delta P$ |
|---|---|
| 740 FICO / 75 LTV | $-0.250$ |
| Investment property | $-2.125$ |
| Cash-out refi | $-1.250$ |
| 45-day lock | $-0.125$ |
| Escrow waiver | $-0.250$ |
| **Sum** | $-4.000$ |

$$ P_\text{net} = 100.875 + (-4.000) = 96.875 $$

On a $\$400{,}000$ loan:
$$ P_\text{net,\$} = \frac{96.875 - 100}{100} \cdot 400{,}000 = -\$12{,}500 \text{ (discount owed)} $$

---

## 4. Net Price (Post-Comp)

For an LPC broker on comp plan $c$ (% of loan):

$$ \boxed{P_\text{broker} = P_\text{net} - c \cdot 100} $$

(Subtract comp expressed in price-point form.)

### Worked Example
$P_\text{net} = 101.500$, LPC = $2.000\%$:
$$ P_\text{broker} = 101.500 - 2.000 = 99.500 $$

For BPC: comp paid by borrower, so $P_\text{broker} = P_\text{net}$ and borrower pays $c \cdot L$ separately.

---

## 5. Price Caps (Lender-Imposed)

Many lenders cap the maximum premium price:
$$ P_\text{capped} = \min(P_\text{net}, P_\text{cap}) $$

Typical cap: $P_\text{cap} = 103.000$ (no further premium past 3 points rebate).

### Worked Example
$P_\text{net} = 104.250$, $P_\text{cap} = 103.000$:
$$ P_\text{capped} = 103.000 \Rightarrow 1.250 \text{ points of premium lost} $$

---

## 6. Cumulative LLPA Cap (Agency Rule)

Fannie/Freddie cap aggregate LLPAs at:
$$ |\Delta P_\text{agency}| \le 3.000 \text{ (capped at 3 points hit)} $$

Some loan types (cash-out investor, 2-4 unit etc.) exempt or have different caps.

$$ \Delta P_\text{agency,net} = \max(\Delta P_\text{agency}, -3.000) $$

---

## 7. Stacking Order Matters (When Caps Apply)

When the lender applies caps to subgroups of adjusters:

$$ \Delta P_\text{total} = \max(\sum_\text{agency} \Delta P_j, -C_\text{agency}) + \sum_\text{lender} \Delta P_j $$

Or with lender-side cap:
$$ \Delta P_\text{lender,net} = \max(\sum_\text{lender} \Delta P_j, -C_\text{lender}) $$

---

## 8. Borrower-Facing Out-of-Pocket Math

Cash a borrower brings depends on net price disposition:

$$ \text{Borrower Cash}_\text{points} = \begin{cases} \dfrac{100 - P_\text{net}}{100} \cdot L & \text{if } P_\text{net} < 100 \\ 0 & \text{if } P_\text{net} \ge 100 \end{cases} $$

If $P_\text{net} > 100$, the premium can fund other closing costs:
$$ \text{LC to Borrower}_\$ = \frac{P_\text{net} - 100}{100} \cdot L - \text{Broker Comp (if LPC)} $$

---

## 9. Buying Down a Rate — Cost Mapping

Each rate row on the grid costs (or pays) a specific number of points. Walking down one row:

$$ \Delta P_\text{down 1/8\% rate} \approx -0.500 \text{ points} $$

So to buy the rate down by $k$ eighths:
$$ \text{Buydown Cost}_\$ \approx \frac{0.5 \cdot k}{100} \cdot L $$

(Sheet-specific; actual increments vary.)

---

## 10. Buying Up a Rate — Rebate Mapping

Walking up one row:
$$ \Delta P_\text{up 1/8\% rate} \approx +0.500 \text{ points} $$

$$ \text{Buy-Up Rebate}_\$ \approx \frac{0.5 \cdot k}{100} \cdot L $$

---

## 11. Composite Worked Example (End-to-End)

Loan: \$500,000 / 30Y Fixed / 720 FICO / 80 LTV / Owner-Occ / Purchase / TX / 45-day lock / Escrow waived / LPC at 2.00%.

| Element | Value |
|---|---|
| Base price at 6.500% (45-day lock col.) | 100.500 |
| FICO/LTV LLPA (720/80) | $-1.000$ |
| Purchase (no adj) | 0 |
| TX state credit | $+0.125$ |
| Escrow waiver | $-0.250$ |
| Subtotal $\Delta P$ | $-1.125$ |
| **Net price (pre-comp) $P_\text{net}$** | **99.375** |
| LPC | $-2.000$ |
| **Broker-facing $P_\text{broker}$** | **97.375** |

Dollar flows:
$$ P_\text{net,\$} = \frac{99.375 - 100}{100} \cdot 500{,}000 = -\$3{,}125 \text{ (discount on loan)} $$
$$ \text{Broker Comp}_\$ = 0.020 \cdot 500{,}000 = \$10{,}000 \text{ (paid by lender out of premium / coupon)} $$

The lender absorbs the gap: $\$3{,}125 + \$10{,}000 = \$13{,}125$ comes out of lender's secondary execution (i.e., lender funds at a coupon that supports both).

---

## 12. Net to the Lender (After All Components)

$$ \text{Lender Net}_\$ = P_\text{base,\$} - \text{Hedge Cost} - \text{Comp} - \text{Concessions} - \text{Tolerance Cures} - \text{Servicing Cost} $$

Where each is in dollars on UPB $L$.

---

## 13. Tolerance Cure Math (TRID)

If APR-affecting fees rise above the disclosed amount by more than tolerance:

$$ \text{Cure}_\$ = (\text{Actual Fees} - \text{Disclosed Fees} - \text{Allowed Tolerance})^+ $$

Where $(x)^+ = \max(x, 0)$, and allowed tolerance is either 0% or 10% depending on fee category.

### Zero-Tolerance Categories
- Origination fees
- Lender credits (cannot decrease)
- Transfer taxes

### 10% Tolerance Categories (Aggregate)
- Recording fees
- Lender-required services from lender's list

### Unlimited Tolerance
- Services borrower shopped for (not on lender's list)
- Prepaids, escrows
- Property taxes

---

## 14. Summary Formula Table

| Quantity | Formula |
|---|---|
| Points in dollars | $(p/100) \cdot L$ |
| Rebate dollars | $(P-100)/100 \cdot L$ |
| Discount dollars | $(100-P)/100 \cdot L$ |
| Total LLPA | $\Delta P_\text{total} = \sum_j \Delta P_j$ |
| Net price | $P_\text{net} = P_\text{base} + \Delta P_\text{total}$ |
| Net price in dollars | $(P_\text{net} - 100)/100 \cdot L$ |
| LPC adjustment | $P_\text{broker} = P_\text{net} - 100 \cdot c$ |
| Price cap | $\min(P_\text{net}, P_\text{cap})$ |
| Agency cap | $\max(\Delta P_\text{agency}, -3.000)$ |
| Rate buy-down ~cost | $0.500 \cdot k$ points per $1/8\%$ |
| TRID cure | $(\text{Actual} - \text{Disclosed} - \text{Tol.})^+$ |
