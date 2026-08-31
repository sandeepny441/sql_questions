# 17 — Amortization Schedule Math

**Prerequisite:** 14 — Math Formulas Index; 16 — Loan Ratios

**Goal:** Derive every payment-, balance-, and interest-related quantity on a fixed-rate fully-amortizing loan. These formulas underlie every monthly payment quoted to a borrower.

---

## 1. Setup & Definitions

| Symbol | Meaning |
|---|---|
| $L$ | Original loan amount |
| $r$ | Annual note rate (decimal) |
| $i = r/12$ | Periodic (monthly) rate |
| $n$ | Total number of monthly payments |
| $M$ | Monthly P&I |
| $B_k$ | Balance after payment $k$, with $B_0 = L$ |
| $I_k$ | Interest portion of payment $k$ |
| $\mathit{Pr}_k$ | Principal portion of payment $k$ |

---

## 2. Monthly Payment (Fully Amortizing)

$$ \boxed{M = L \cdot \frac{i\,(1+i)^n}{(1+i)^n - 1}} $$

Equivalent form using annuity factor:
$$ M = \frac{L}{a_{\overline{n}|i}}, \qquad a_{\overline{n}|i} = \frac{1 - (1+i)^{-n}}{i} $$

### Worked Example
$L = \$400{,}000$, $r = 6.500\%$, $n = 360$:
$$ i = \frac{0.065}{12} = 0.0054167 $$
$$ M = 400{,}000 \cdot \frac{0.0054167 \cdot (1.0054167)^{360}}{(1.0054167)^{360} - 1} = \$2{,}528.27 $$

---

## 3. Remaining Balance After $k$ Payments

$$ \boxed{B_k = L\,(1+i)^k - M \cdot \frac{(1+i)^k - 1}{i}} $$

Equivalent closed form (using $M$ from §2):
$$ B_k = L \cdot \frac{(1+i)^n - (1+i)^k}{(1+i)^n - 1} $$

### Worked Example
After 60 months on the loan above:
$$ B_{60} = 400{,}000 \cdot \frac{(1.0054167)^{360} - (1.0054167)^{60}}{(1.0054167)^{360} - 1} \approx \$369{,}833 $$

---

## 4. Interest / Principal Split

For each payment $k$:

$$ \boxed{I_k = B_{k-1} \cdot i} $$
$$ \boxed{\mathit{Pr}_k = M - I_k} $$
$$ B_k = B_{k-1} - \mathit{Pr}_k $$

### Worked Example (Payment 1)
$B_0 = \$400{,}000$, $i = 0.0054167$:
$$ I_1 = 400{,}000 \cdot 0.0054167 = \$2{,}166.67 $$
$$ \mathit{Pr}_1 = 2{,}528.27 - 2{,}166.67 = \$361.60 $$

---

## 5. Total Interest Paid Over Life of Loan

$$ \text{Total Interest} = n \cdot M - L $$

### Worked Example
$$ 360 \cdot 2{,}528.27 - 400{,}000 = 910{,}177 - 400{,}000 = \$510{,}177 $$

---

## 6. Total Interest Through Payment $k$

$$ \sum_{j=1}^{k} I_j = k \cdot M - (L - B_k) $$

### Worked Example (first 60 months)
Principal paid = $L - B_{60} = 400{,}000 - 369{,}833 = \$30{,}167$.
$$ \sum_{j=1}^{60} I_j = 60 \cdot 2{,}528.27 - 30{,}167 = 151{,}696 - 30{,}167 = \$121{,}530 $$

---

## 7. Solve for Loan Amount Given Target Payment

$$ \boxed{L = M \cdot \frac{(1+i)^n - 1}{i\,(1+i)^n} = M \cdot a_{\overline{n}|i}} $$

### Worked Example
$M = \$3{,}000$, $r = 6.500\%$, $n = 360$:
$$ L = 3{,}000 \cdot \frac{(1.0054167)^{360} - 1}{0.0054167 \cdot (1.0054167)^{360}} \approx \$474{,}649 $$

---

## 8. Solve for Term Given Loan, Rate, and Payment

$$ n = \frac{-\ln\!\left(1 - \dfrac{L\,i}{M}\right)}{\ln(1+i)} $$

Loan is payable only if $M > L \cdot i$.

### Worked Example
$L = \$400{,}000$, $r = 6.500\%$, $M = \$3{,}000$ (above min interest of $\$2{,}166.67$):
$$ n = \frac{-\ln(1 - 400{,}000 \cdot 0.0054167 / 3{,}000)}{\ln(1.0054167)} \approx 222 \text{ months} \approx 18.5 \text{ years} $$

---

## 9. Solve for Rate Given Loan, Payment, and Term

No closed form — iterate via Newton-Raphson on:

$$ f(i) = M - L \cdot \frac{i(1+i)^n}{(1+i)^n - 1} $$

Initial guess: $i_0 = M/L - 1/n$.

---

## 10. Early Payoff Math

### Cumulative Principal Reduction
$$ \text{Principal Paid through } k = L - B_k $$

### Payoff Amount on Day $d$ of Month $k$
$$ \text{Payoff} = B_k + B_k \cdot i \cdot \frac{d}{30} $$

(Per-diem interest accrued from last paid date.)

---

## 11. Effect of Extra Principal Payments

If borrower adds $X$ extra to payment $k$:
$$ B_k = (B_{k-1} - \mathit{Pr}_k - X)\quad(\text{floor at zero}) $$

New term $n'$ if extra payment is continued each month:
$$ n' = \frac{-\ln\!\left(1 - \dfrac{L\,i}{M + X}\right)}{\ln(1+i)} $$

### Worked Example
$L = \$400{,}000$, $r = 6.5\%$, $M = \$2{,}528.27$, plus $X = \$200$/mo:
$$ n' = \frac{-\ln(1 - 400{,}000 \cdot 0.0054167 / 2{,}728.27)}{\ln(1.0054167)} \approx 312 \text{ months} \approx 26.0\text{ years} $$
Roughly 4 years shaved off.

---

## 12. Biweekly Conversion

Biweekly payment:
$$ M_\text{biweekly} = \frac{M}{2} $$

Number of payments per year:
$$ N_\text{biweekly/yr} = 26 = 13 \text{ monthly equivalents} $$

Equivalent extra principal per month:
$$ X_\text{equiv} = \frac{M}{12} $$

(One full extra monthly payment per year.)

---

## 13. Interest-Only Period

During the IO period (length $n_{IO}$):
$$ M_{IO} = L \cdot i $$

After IO period ends, payment reamortizes over remaining term $(n - n_{IO})$:
$$ M_\text{post-IO} = L \cdot \frac{i\,(1+i)^{n - n_{IO}}}{(1+i)^{n - n_{IO}} - 1} $$

### Worked Example
$L = \$400{,}000$, $r = 6.5\%$, $n = 360$, $n_{IO} = 120$:
$$ M_{IO} = 400{,}000 \cdot 0.0054167 = \$2{,}166.67/\text{mo (yrs 1-10)} $$
$$ M_\text{post-IO} = 400{,}000 \cdot \frac{0.0054167 \cdot (1.0054167)^{240}}{(1.0054167)^{240} - 1} = \$2{,}983.95/\text{mo (yrs 11-30)} $$

---

## 14. Balloon Payment

Loan amortizes over $n$ but balloons at payment $k < n$:
$$ \text{Balloon} = B_k = L \cdot \frac{(1+i)^n - (1+i)^k}{(1+i)^n - 1} $$

### Worked Example
$L = \$400{,}000$, $r = 6.5\%$, amortized 30 yrs, balloons at 7 years ($k = 84$):
$$ B_{84} \approx \$362{,}450 $$

---

## 15. Summary Formula Table

| Quantity | Formula |
|---|---|
| Monthly P&I | $M = L \cdot i(1+i)^n / [(1+i)^n - 1]$ |
| Periodic rate | $i = r/12$ |
| Balance after $k$ | $B_k = L(1+i)^k - M\bigl[(1+i)^k - 1\bigr]/i$ |
| Interest portion | $I_k = B_{k-1} \cdot i$ |
| Principal portion | $\mathit{Pr}_k = M - I_k$ |
| Total interest | $nM - L$ |
| Solve for $L$ | $L = M \cdot \bigl[(1+i)^n - 1\bigr] / \bigl[i(1+i)^n\bigr]$ |
| Solve for $n$ | $n = -\ln(1 - Li/M) / \ln(1+i)$ |
| IO payment | $M_{IO} = L \cdot i$ |
| Balloon amount | Same as $B_k$ |
| Biweekly equiv extra | $X = M/12$ per month |
