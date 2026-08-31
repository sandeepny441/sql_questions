# 18 — APR (Annual Percentage Rate) Math

**Prerequisite:** 17 — Amortization Schedule

**Goal:** Compute APR per Reg Z, the related "Amount Financed," and the comparison tests (APOR, HPML/HOEPA) that determine pricing-tier classification.

---

## 1. Core Definition (Reg Z, 12 CFR §1026.22)

APR is the rate $r_{APR}$ that solves:

$$ \boxed{\text{Amount Financed} = \sum_{k=1}^{n} \frac{M_k}{\left(1 + \dfrac{r_{APR}}{12}\right)^{k}}} $$

For a fully-amortizing fixed-rate loan with constant $M$:

$$ \text{AF} = M \cdot \frac{1 - (1 + i_{APR})^{-n}}{i_{APR}}, \qquad i_{APR} = \frac{r_{APR}}{12} $$

Solve iteratively for $i_{APR}$ (Newton-Raphson).

---

## 2. Amount Financed

$$ \boxed{\text{AF} = L - F_\text{prepaid}} $$

Where $F_\text{prepaid}$ = Prepaid Finance Charges (PFC):
- Origination fees / discount points
- Mortgage broker comp (when borrower-paid)
- Required mortgage insurance premium (up-front portion)
- PMI single premium (if any)
- Lender admin / underwriting / processing fees
- Per-diem interest from closing to first payment
- *Excludes:* third-party fees not paid to/retained by lender (title, recording, appraisal, etc., **if** not lender-required and not retained)

### Worked Example
$L = \$400{,}000$, origination = \$3,000, 1 discount point = \$4,000, processing = \$500, per-diem interest = \$1,200, PMI up-front = \$0:
$$ F_\text{prepaid} = 3{,}000 + 4{,}000 + 500 + 1{,}200 = \$8{,}700 $$
$$ \text{AF} = 400{,}000 - 8{,}700 = \$391{,}300 $$

---

## 3. Finance Charge

$$ \text{FC} = (n \cdot M - L) + F_\text{prepaid} $$

Equivalently:
$$ \text{FC} = \text{Total Interest} + \text{PFC} $$

### Worked Example
Using §2's loan: $M = \$2{,}528.27$, $n = 360$, $L = \$400{,}000$, PFC = \$8,700:
$$ \text{FC} = (360 \cdot 2{,}528.27 - 400{,}000) + 8{,}700 = 510{,}177 + 8{,}700 = \$518{,}877 $$

---

## 4. APR vs Note Rate — Quick Approximation

For small PFC relative to loan:

$$ r_{APR} \approx r + \frac{2 \cdot F_\text{prepaid}}{L \cdot n_\text{eff,years}} $$

(Crude but useful for quick sanity check; not Reg-Z compliant.)

### Worked Example
$r = 6.500\%$, PFC = \$8,700, $L = \$400{,}000$, expected hold 30 yrs:
$$ r_{APR} \approx 6.500\% + \frac{2 \cdot 8{,}700}{400{,}000 \cdot 30} \approx 6.500\% + 0.145\% = 6.645\% $$

---

## 5. Iterative Solve for APR (Newton-Raphson)

Define:
$$ g(i) = \text{AF} - M \cdot \frac{1 - (1+i)^{-n}}{i} $$

Update:
$$ i_{k+1} = i_k - \frac{g(i_k)}{g'(i_k)} $$

Where:
$$ g'(i) = M \cdot \frac{(1+i)^{-n}(1 + ni + i) - 1}{i^2} $$

Start with $i_0 = r/12$. Converges in 3–5 iterations.

---

## 6. APR for Loans with Step / Variable Payments

For ARMs or step-rate loans:
$$ \text{AF} = \sum_{k=1}^{n} \frac{M_k}{(1 + i_{APR})^{k}} $$

Reg Z requires using the fully-indexed rate assumption (or initial rate, per scenario rules) for each payment.

---

## 7. APOR (Average Prime Offer Rate)

APOR is published weekly by the CFPB; it benchmarks "prime" pricing. The HPML / HOEPA tests compare APR to APOR.

### HPML Test (Higher-Priced Mortgage Loan)

A loan is an HPML if:

$$ r_{APR} > \text{APOR} + T_\text{lien} $$

Where:
| Lien | Threshold $T_\text{lien}$ |
|---|---|
| First lien, conforming | 1.50% |
| First lien, jumbo (> CLL) | 2.50% |
| Subordinate lien | 3.50% |

### Worked Example
APOR = 6.000%, conforming 1st lien, $r_{APR} = 7.250\%$:
$$ \text{Spread} = 7.250 - 6.000 = 1.250\% < 1.500\% \Rightarrow \text{Not HPML} $$

If $r_{APR} = 7.750\%$:
$$ 7.750 - 6.000 = 1.750\% > 1.500\% \Rightarrow \text{HPML} $$

---

## 8. HOEPA "High-Cost" Test (Three Triggers, Any One Triggers)

### APR Trigger
$$ r_{APR} > \text{APOR} + T_\text{HOEPA} $$

| Lien Type | $T_\text{HOEPA}$ |
|---|---|
| First lien | 6.50% (8.50% for $L < \$50k$ secured by personal property) |
| Subordinate lien | 8.50% |

### Points & Fees Trigger
$$ \frac{\text{Points & Fees}}{L} > P_\text{thresh} $$

| Loan Size $L$ | Threshold (2024 figures, indexed annually) |
|---|---|
| $\ge \$26{,}092$ | 5% |
| $< \$26{,}092$ | greater of 8% or \$1,305 |

### Prepayment Penalty Trigger
Any prepayment penalty after 36 months OR exceeding 2% of prepaid amount.

---

## 9. QM (Qualified Mortgage) Points-and-Fees Cap

| Loan Size (2024) | Cap |
|---|---|
| $\ge \$130{,}461$ | 3.00% |
| $\$78{,}277 - \$130{,}461$ | \$3,914 |
| $\$26{,}092 - \$78{,}277$ | 5.00% |
| $\$16{,}308 - \$26{,}092$ | \$1,305 |
| $< \$16{,}308$ | 8.00% |

QM "price-based" definition (general QM): $r_{APR} \le \text{APOR} + \text{spread}$, where spread depends on loan size (1.5%–6.5% tiered).

---

## 10. Section 32 (HOEPA) Triggers vs Section 35 (HPML)

| Test | Spread to APOR | Effect |
|---|---|---|
| HPML (§35) — Conforming 1st | $> 1.50\%$ | Escrow required for 5 years, ATR requirements |
| HOEPA (§32) — 1st lien | $> 6.50\%$ | Full high-cost disclosure regime |

---

## 11. APR Tolerance (Reg Z §1026.22(a)(2)–(4))

Permissible APR error:
$$ |r_{APR,\text{disclosed}} - r_{APR,\text{actual}}| \le 0.125\% \text{ (regular loans)} $$
$$ |r_{APR,\text{disclosed}} - r_{APR,\text{actual}}| \le 0.25\% \text{ (irregular loans)} $$

Larger errors → must redisclose and re-wait per TRID 3-day rule.

---

## 12. Effective Cost to Borrower vs APR

APR assumes loan held to maturity. Effective cost over actual hold:

$$ y_\text{hold} = \text{IRR of} \left\{ -\text{AF},\, M_1, M_2, \ldots, M_h, B_h \right\} $$

Where $h$ = months held, $B_h$ = payoff balance.

### Practical Approximation (for hold $h$ years)
$$ y_\text{hold} \approx r + \frac{F_\text{prepaid}}{L \cdot h} $$

---

## 13. Summary Formula Table

| Quantity | Formula |
|---|---|
| Amount Financed | $\text{AF} = L - \text{PFC}$ |
| Finance Charge | $\text{FC} = nM - L + \text{PFC}$ |
| APR equation | $\text{AF} = M \cdot [1 - (1+i)^{-n}] / i$, solve for $i = r_{APR}/12$ |
| APR approximation | $r_{APR} \approx r + 2 \cdot \text{PFC}/(L \cdot n_\text{yrs})$ |
| HPML test | $r_{APR} > \text{APOR} + T_\text{lien}$ |
| HOEPA APR trigger | $r_{APR} > \text{APOR} + T_\text{HOEPA}$ |
| HOEPA P&F trigger | P&F / $L > $ threshold |
| QM 3% P&F cap | P&F / $L \le 3.00\%$ for loans $\ge \$130{,}461$ |
| APR tolerance | $\le 0.125\%$ regular, $\le 0.25\%$ irregular |
