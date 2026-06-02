# 22 — ARM (Adjustable-Rate Mortgage) Math

**Prerequisite:** 17 — Amortization

**Goal:** Compute the fully-indexed rate, enforce periodic and lifetime caps, and reamortize the payment at each adjustment date for hybrid ARMs (5/6, 7/6, 10/6 SOFR, etc.).

---

## 1. ARM Structure Notation

A hybrid ARM is written $a/b$ where:
- $a$ = initial fixed-rate period in years
- $b$ = adjustment frequency in months

Examples:
- **5/6 SOFR**: 5 years fixed, then adjusts every 6 months
- **7/6 SOFR**: 7 years fixed, then every 6 months
- **10/6 SOFR**: 10 years fixed, then every 6 months
- **5/1**: 5 years fixed, then annual adjustment (legacy)

Cap notation: $\text{IC}/\text{PC}/\text{LC}$
- IC = Initial cap at first adjustment
- PC = Periodic cap on subsequent adjustments
- LC = Lifetime cap above initial rate

Example: 2/1/5 → initial cap 2%, periodic 1%, lifetime 5%.

---

## 2. Initial Period Payment

For initial period $k \le 12a$:
$$ M_\text{init} = L \cdot \frac{i_\text{init}\,(1 + i_\text{init})^n}{(1 + i_\text{init})^n - 1}, \qquad i_\text{init} = \frac{r_\text{init}}{12} $$

---

## 3. Fully-Indexed Rate (FIR)

At any adjustment date:
$$ \boxed{\text{FIR} = \text{Index} + \text{Margin}} $$

Common indices:
- **30-Day Avg SOFR** (current standard)
- 1-Year CMT (legacy)
- 11th District COFI (legacy California)
- 12-Month MTA (legacy)

Margin is set at origination (typically 2.00% – 2.75%).

### Worked Example
30-day avg SOFR = 5.30%, margin = 2.75%:
$$ \text{FIR} = 5.30 + 2.75 = 8.05\% $$

---

## 4. Capped Rate Calculation

At each adjustment, the new rate must satisfy three caps simultaneously.

### Initial Adjustment (First Reset)
$$ r_1 = \max\bigl(\text{Floor},\, \min(\text{FIR}, r_\text{init} + \text{IC}, r_\text{init} + \text{LC})\bigr) $$

### Subsequent Adjustments ($k > 1$)
$$ r_k = \max\bigl(\text{Floor},\, \min(\text{FIR}, r_{k-1} + \text{PC}, r_{k-1} - \text{PC} \text{ on downward}, r_\text{init} + \text{LC})\bigr) $$

More explicitly (separating up and down moves):
$$ r_k = \begin{cases} \min(\text{FIR}, r_{k-1} + \text{PC}, r_\text{init} + \text{LC}) & \text{if FIR} > r_{k-1} \\ \max(\text{FIR}, r_{k-1} - \text{PC}, \text{Floor}) & \text{if FIR} < r_{k-1} \end{cases} $$

### Worked Example
2/1/5 ARM, $r_\text{init} = 6.000\%$, Floor = margin = 2.75%.

**Adjustment 1**: FIR = 8.05%.
$$ r_1 = \min(8.05, 6.00 + 2.00, 6.00 + 5.00) = \min(8.05, 8.00, 11.00) = 8.00\% $$
(Capped by initial 2% cap.)

**Adjustment 2**: FIR rises to 8.50%.
$$ r_2 = \min(8.50, 8.00 + 1.00, 11.00) = \min(8.50, 9.00, 11.00) = 8.50\% $$

**Adjustment 3**: FIR rises to 12.00%.
$$ r_3 = \min(12.00, 8.50 + 1.00, 11.00) = \min(12.00, 9.50, 11.00) = 9.50\% $$
(Capped by periodic 1% cap.)

---

## 5. Floor

Most ARMs floor at the margin (i.e., FIR cannot drop below margin alone):
$$ r_k \ge \text{Margin} $$

Some include an explicit floor (e.g., initial rate as floor).

---

## 6. Payment Recast at Each Adjustment

When the rate changes at month $k$, payment is recomputed to fully amortize the **remaining balance** over the **remaining term**:

$$ \boxed{M_k = B_{k-1} \cdot \frac{i_k\,(1 + i_k)^{n - k + 1}}{(1 + i_k)^{n - k + 1} - 1}} $$

Where:
- $B_{k-1}$ = balance just before adjustment
- $i_k = r_k / 12$
- $n - k + 1$ = remaining months

### Worked Example
$L = \$400{,}000$, 5/6 SOFR, $r_\text{init} = 6.000\%$, $M_\text{init} = \$2{,}398.20$, $n = 360$.

Balance after 60 months ($k = 60$):
$$ B_{60} \approx \$372{,}569 $$

At month 61, rate adjusts to $r_1 = 8.000\%$. Remaining term = 300 months.
$$ i_1 = 0.0066667 $$
$$ M_{61} = 372{,}569 \cdot \frac{0.0066667 \cdot (1.0066667)^{300}}{(1.0066667)^{300} - 1} \approx \$2{,}876.10 $$

Payment jumps by $\$478$/mo at first adjustment.

---

## 7. Qualifying Rate for ARMs (Ability-to-Repay)

Per ATR rules, qualify borrower using the higher of:

$$ r_\text{qual} = \max(r_\text{init},\; \text{Index}_\text{today} + \text{Margin}) $$

For Non-QM, qualification may use:
$$ r_\text{qual} = \max(r_\text{init} + \text{IC},\; \text{FIR}) $$

(Conservative; ensures borrower can afford post-adjustment payment.)

---

## 8. Max Possible Rate (Lifetime)

$$ r_\text{max} = r_\text{init} + \text{LC} $$

Max possible payment (at $k$ = first month of adjustment, full term remaining):
$$ M_\text{max} = L \cdot \frac{i_\text{max}\,(1 + i_\text{max})^n}{(1 + i_\text{max})^n - 1}, \qquad i_\text{max} = \frac{r_\text{max}}{12} $$

### Worked Example
$L = \$400{,}000$, $r_\text{init} = 6.000\%$, LC = 5%, $n = 360$:
$$ r_\text{max} = 11.000\%, \qquad i_\text{max} = 0.00917 $$
$$ M_\text{max} = 400{,}000 \cdot \frac{0.00917(1.00917)^{360}}{(1.00917)^{360} - 1} \approx \$3{,}809 $$

Borrower must be aware of payment up to $\$3{,}809$ vs initial $\$2{,}398$.

---

## 9. Payment Shock Calculation

$$ \text{Payment Shock}_\% = \frac{M_\text{new} - M_\text{init}}{M_\text{init}} $$

### Worked Example
From §6: $M_\text{init} = \$2{,}398$, $M_{61} = \$2{,}876$:
$$ \text{Shock} = \frac{2{,}876 - 2{,}398}{2{,}398} = 19.9\% $$

Regulators flag > 1% rate / 7.5% payment shock for additional disclosure.

---

## 10. Interest-Only ARM Math

During IO period, payment = $L \cdot i$ at then-current rate:
$$ M_\text{IO, k} = L \cdot i_k $$

After IO ends, payment amortizes remaining balance over remaining term:
$$ M_\text{post-IO, k} = L \cdot \frac{i_k\,(1+i_k)^{n - k + 1}}{(1+i_k)^{n - k + 1} - 1} $$

---

## 11. Hybrid ARM Pricing (Curve Math)

ARM rates are priced off the swap/Treasury curve at the corresponding tenor minus margin:
$$ r_\text{ARM init} \approx \text{Treasury}_\text{tenor} + s_\text{ARM} $$

Where $s_\text{ARM}$ is the spread to Treasuries. Shorter initial periods → lower rates (steeper curve).

Typical relationship (normal curve):
$$ r_\text{5/6} < r_\text{7/6} < r_\text{10/6} < r_\text{30Y fixed} $$

---

## 12. SOFR Index Calculation

30-Day Average SOFR:
$$ \text{SOFR}_\text{30d avg} = \frac{1}{30} \sum_{d=t-29}^{t} \text{SOFR}_d $$

90-Day Average SOFR:
$$ \text{SOFR}_\text{90d avg} = \frac{1}{90} \sum_{d=t-89}^{t} \text{SOFR}_d $$

Published daily by the New York Fed. The lender's note specifies which average to use.

---

## 13. Lookback Period

Most ARM notes use a **45-day lookback**: the index value used at adjustment date $t$ is from $t - 45$ days. This gives notice/disclosure time before payment changes.

---

## 14. ARM Conversion Option

Some ARMs include a one-time conversion to fixed at a specified date:
$$ r_\text{converted} = \text{Conversion Index} + s_\text{convert} $$

Conversion fee typically $\$250\text{-}\$500$.

---

## 15. Summary Formula Table

| Quantity | Formula |
|---|---|
| Fully-indexed rate | $\text{FIR} = \text{Index} + \text{Margin}$ |
| Initial adj capped rate | $r_1 = \min(\text{FIR}, r_\text{init} + \text{IC}, r_\text{init} + \text{LC})$ |
| Subsequent adj | $r_k = \min(\text{FIR}, r_{k-1} + \text{PC}, r_\text{init} + \text{LC})$ |
| Floor | $r_k \ge \text{Margin}$ |
| Max rate | $r_\text{max} = r_\text{init} + \text{LC}$ |
| Recast payment | $M_k = B_{k-1} \cdot i_k(1+i_k)^{n-k+1} / [(1+i_k)^{n-k+1} - 1]$ |
| Qualifying rate (QM) | $\max(r_\text{init}, \text{FIR}_\text{today})$ |
| Qualifying rate (Non-QM) | $\max(r_\text{init} + \text{IC}, \text{FIR})$ |
| Payment shock % | $(M_\text{new} - M_\text{init}) / M_\text{init}$ |
| IO payment | $M_\text{IO} = L \cdot i$ |
| 30-day SOFR avg | $\sum_{d=t-29}^{t} \text{SOFR}_d / 30$ |
