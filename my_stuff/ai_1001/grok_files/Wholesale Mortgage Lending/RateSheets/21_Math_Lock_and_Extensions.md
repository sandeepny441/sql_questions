# 21 — Lock & Extension Math

**Prerequisite:** 19 — Points & Net Price

**Goal:** Quantify the cost of choosing a lock period, paying for extensions, relocking after expiration, and breaking a lock for renegotiation.

---

## 1. Lock Period Adjuster (Δ vs Base Period)

Most sheets quote the 30-day lock as base. Each other column carries an additional adjuster:

$$ P_\text{lock,d} = P_\text{30} + \Delta P_\text{lock}(d) $$

Typical schedule:

| Lock Period $d$ (days) | $\Delta P_\text{lock}$ |
|---|---|
| 15 | $+0.125$ |
| 30 | $0$ (base) |
| 45 | $-0.125$ |
| 60 | $-0.250$ |
| 75 | $-0.375$ |
| 90 | $-0.500$ |
| 120 | $-0.875$ |
| 180 | $-1.500$ |

(Each lender publishes its own schedule; longer = more hedge cost = worse price.)

---

## 2. Daily Cost of Holding a Lock

Approximate marginal cost per day:
$$ c_\text{day} \approx \frac{\Delta P_\text{lock}(d_2) - \Delta P_\text{lock}(d_1)}{d_2 - d_1} $$

### Worked Example
From the table: $\Delta P_{60} - \Delta P_{30} = -0.250$ over 30 days:
$$ c_\text{day} \approx \frac{-0.250}{30} = -0.00833 \text{ points/day} = -0.833 \text{ bp/day} $$

Holding cost ~0.8 bp/day on the front end of the curve.

---

## 3. Extension Fee Math

When a lock will expire before funding, broker pays an extension fee:

$$ \text{Ext}_\$ = f_\text{day} \cdot d_\text{ext} \cdot L $$

Where $f_\text{day}$ = bp/day cost (set by lender) and $d_\text{ext}$ = extension days.

### Typical Extension Schedule

| Extension Length | Fee (bp of $L$) |
|---|---|
| 5 days | 6.25 ($1/16$ pt) |
| 7 days | 8.75 |
| 15 days | 18.75 ($3/16$ pt) |
| 30 days | 37.50 ($3/8$ pt) |

$$ f_\text{day} \approx 1.25 \text{ bp/day (typical)} $$

### Worked Example
$L = \$400{,}000$, 15-day extension at $1/16$ pt per 5 days = $3/16$ pt total:
$$ \text{Ext}_\$ = \frac{0.1875}{100} \cdot 400{,}000 = \$750 $$

---

## 4. Worst-Case Relock Pricing

After lock expiration (or broken lock), most lenders relock at the **worse** of original and current pricing, possibly plus a relock hit:

$$ \boxed{P_\text{relock} = \min(P_\text{original}, P_\text{current,today}) - \delta_\text{relock}} $$

Where $\delta_\text{relock}$ is the relock penalty (often $1/4$ pt = 25 bp).

### Worked Example
Original lock $P = 100.500$. Current sheet shows $P = 100.875$. Relock penalty $1/8$ pt:
$$ P_\text{relock} = \min(100.500, 100.875) - 0.125 = 100.500 - 0.125 = 100.375 $$

If market is worse — current $P = 99.875$:
$$ P_\text{relock} = \min(100.500, 99.875) - 0.125 = 99.750 $$

---

## 5. Cost of Worst-Case Relock vs Extending

Compare extension cost to relock loss:

$$ \text{Extend if: } \text{Ext}_\$ < (P_\text{original} - P_\text{relock}) \cdot \frac{L}{100} $$

### Worked Example
$L = \$400{,}000$, 15-day extension = \$750. Expected market move makes relock cost = $1/4$ point worse = $\$1{,}000$:
$$ \$750 < \$1{,}000 \Rightarrow \text{Extend} $$

---

## 6. Renegotiation Math (Lock Float-Down by Negotiation)

When markets rally significantly, broker may request lender re-price the lock. Lender typically requires:

$$ \Delta y_\text{required} \ge \theta_\text{renog} \quad \text{(threshold, e.g., 25-50 bp better)} $$

If granted, new price often splits the move:
$$ P_\text{new} = P_\text{original} + \alpha \cdot (P_\text{current} - P_\text{original}) $$

Where $\alpha \in [0.5, 0.75]$ (lender keeps the rest as hedge cost offset).

### Worked Example
Market improved by 50 bp price (rally); lender splits 50/50:
$$ P_\text{new} = P_\text{original} + 0.50 \cdot 0.500 = P_\text{original} + 0.250 $$

---

## 7. Formal Float-Down Option (Pre-Priced)

Some lenders offer a one-time float-down option at lock for an up-front fee:

$$ P_\text{float-down lock} = P_\text{standard} - \delta_\text{FDO} $$

Where $\delta_\text{FDO}$ typically = $1/8$ to $1/4$ point.

Float-down can be exercised if market rallies by at least $\Delta y_\text{trigger}$ (often 25 bp) before lock expires. New rate = current market rate at trigger.

---

## 8. TBD Lock / Lock-and-Shop

For locks before a specific property is identified:

$$ P_\text{TBD} = P_\text{standard} - \delta_\text{TBD} - \delta_\text{lock} $$

Typical TBD adjuster: $-0.125$ to $-0.375$ point + the standard lock-period adjuster.

---

## 9. Extended Lock (Construction / Forward) Math

For 90-/120-/180-day locks during construction:

$$ P_\text{extended} = P_\text{30} + \Delta P_\text{ext} $$

Often paid as up-front deposit:
$$ \text{Deposit}_\$ = \delta_\text{deposit} \cdot L $$

Typical: 1% of loan, refundable at close.

---

## 10. Lock Confirmation Tolerance Math

When the loan attributes at funding differ from those locked, lender may reprice:

$$ \text{Price Δ at funding} = \sum_j \Delta P_j(\text{actual}) - \sum_j \Delta P_j(\text{locked}) $$

If $|\text{Price Δ}| < $ tolerance (often $1/8$ pt = 12.5 bp), no reprice. Else worst-case applies.

---

## 11. Daily Pricing Risk During Float

Expected daily price change during float period:

$$ \sigma_\text{daily price} \approx \sigma_\text{daily yield} \cdot D $$

Where $\sigma_\text{daily yield}$ ≈ 4–8 bp/day historical for TBA MBS, and $D \approx 5$ years.

$$ \sigma_\text{daily price} \approx 5 \cdot 6 \text{ bp} = 30 \text{ bp/day price std dev} $$

Over $h$ days (independence assumption):
$$ \sigma_\text{cumulative} = \sigma_\text{daily} \cdot \sqrt{h} $$

### Worked Example
Float for 10 days:
$$ \sigma_\text{10d} = 30 \cdot \sqrt{10} \approx 95 \text{ bp} = \sim 1 \text{ point std dev} $$

---

## 12. Cut-Off Time & Same-Day vs Next-Day Math

When a lock is requested near cut-off:

$$ P_\text{effective} = \begin{cases} P_\text{today} & \text{if request} < t_\text{cutoff} \\ P_\text{tomorrow's open} & \text{otherwise} \end{cases} $$

Overnight risk = full $\sigma_\text{daily price}$ exposure.

---

## 13. Reprice Lock Protection Window

After a reprice fires at time $t_R$, prior pricing is honored for window $W$ (often 15–30 minutes):

$$ P_\text{lock} = \begin{cases} P_\text{prior sheet} & t_\text{request} < t_R + W \\ P_\text{new sheet} & t_\text{request} \ge t_R + W \end{cases} $$

---

## 14. Summary Formula Table

| Quantity | Formula |
|---|---|
| Lock-period price | $P_\text{lock,d} = P_\text{30} + \Delta P_\text{lock}(d)$ |
| Daily lock cost | $c_\text{day} \approx \Delta\Delta P_\text{lock} / \Delta d$ |
| Extension cost | $\text{Ext}_\$ = f_\text{day} \cdot d_\text{ext} \cdot L$ |
| Worst-case relock | $P_\text{relock} = \min(P_\text{orig}, P_\text{today}) - \delta_\text{relock}$ |
| Extend-vs-relock | Extend if $\text{Ext}_\$ < (P_\text{orig} - P_\text{relock}) \cdot L/100$ |
| Renegotiation | $P_\text{new} = P_\text{orig} + \alpha(P_\text{today} - P_\text{orig})$ |
| Float-down price | $P_\text{FDO} = P_\text{std} - \delta_\text{FDO}$ |
| TBD lock | $P_\text{TBD} = P_\text{std} - \delta_\text{TBD}$ |
| Daily price σ | $\sigma_\text{daily price} \approx \sigma_y \cdot D$ |
| $h$-day cumulative σ | $\sigma_h = \sigma_\text{daily} \cdot \sqrt{h}$ |
