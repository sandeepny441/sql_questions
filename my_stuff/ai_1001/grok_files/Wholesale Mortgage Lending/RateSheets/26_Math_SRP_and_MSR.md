# 26 — SRP & MSR Valuation Math

**Prerequisite:** 17 — Amortization; 25 — Broker Compensation

**Goal:** Value mortgage servicing rights (MSRs) and compute the service-release premium (SRP) that an aggregator pays an originator for releasing those rights. SRP is a major component of the price embedded in the rate sheet.

---

## 1. Servicing Fee Math

The annual servicing fee retained from each payment:
$$ \boxed{\text{Service Fee Strip}_\text{annual} = s \cdot B_k} $$

Where $s$ = annual servicing fee rate (typically 25 bp for agency loans).

### Monthly Service Fee Income
$$ I_\text{service, k} = \frac{s \cdot B_{k-1}}{12} $$

### Worked Example
$B_0 = \$400{,}000$, $s = 0.25\%$:
$$ I_\text{service, 1} = \frac{0.0025 \cdot 400{,}000}{12} = \$83.33 $$

---

## 2. Servicing Cost (Per Loan, Per Year)

$$ K_\text{service} = K_\text{fixed} + K_\text{variable} \cdot B_k $$

Typical:
- Performing loan: $\$60\text{-}\$80/\text{year}$
- Non-performing: $\$500\text{+}/\text{year}$
- Loss-mit / FC: much higher

---

## 3. Servicing Net Income (Per Loan, Per Period)

$$ \text{Net Servicing Income}_k = I_\text{service, k} - \frac{K_\text{service}}{12} $$

---

## 4. MSR Present Value

$$ \boxed{\text{MSR Value} = \sum_{k=1}^{n} \frac{(I_\text{service, k} - K_\text{service, k}) \cdot p_k}{(1 + d)^{k/12}} - L \cdot R_\text{recapture} \cdot E[\text{loss}]} $$

Where:
- $d$ = annual discount rate (often 10–13% for MSR investors)
- $p_k$ = probability loan is still active at month $k$ (survival function)
- $R_\text{recapture}$ = recapture rate adjustment
- $E[\text{loss}]$ = expected credit losses

Closed-form approximation (constant prepay and discount):
$$ \text{MSR Value} \approx \frac{s - K_\%}{d + \text{CPR}} \cdot L $$

Where $\text{CPR}$ = annualized prepayment speed and $K_\%$ = servicing cost as % of UPB.

### Worked Example
$s = 0.25\%$, $K_\% = 0.02\%$, $d = 0.10$, CPR = 0.10, $L = \$400{,}000$:
$$ \text{MSR} \approx \frac{0.0025 - 0.0002}{0.10 + 0.10} \cdot 400{,}000 = \frac{0.0023}{0.20} \cdot 400{,}000 = \$4{,}600 $$

In price points: $\$4{,}600 / \$400{,}000 = 1.15\%$ = **115 bp**.

---

## 5. MSR Multiple

A common shorthand: MSR is expressed as a multiple of the annual servicing strip:

$$ \boxed{\text{MSR Multiple} = \frac{\text{MSR Value}}{s \cdot L}} $$

### Worked Example
Using §4: $\text{MSR Value} = \$4{,}600$, annual strip $= 0.0025 \cdot 400{,}000 = \$1{,}000$:
$$ \text{Multiple} = \frac{4{,}600}{1{,}000} = 4.6\text{x} $$

Typical agency MSR multiples in normal markets: 3.5x – 5.5x; reach 5–6x in low-prepayment regimes.

---

## 6. SRP (Service-Released Premium) Paid by Investor

When the originator sells the loan servicing-released, the investor (aggregator) pays an SRP that compensates for the value of the MSR they're taking on:

$$ \boxed{\text{SRP} \approx \text{MSR Value} - \text{Investor MSR Cost}} $$

Where Investor MSR Cost includes their servicing setup, capital cost, and modeling haircut.

### As a Price Point
$$ \text{SRP}_\text{points} = \frac{\text{SRP}}{L} \cdot 100 $$

### Worked Example
MSR value = \$4,600, investor takes \$500 cushion:
$$ \text{SRP} = \$4{,}100 = 102.5 \text{ bp} \approx 1.025 \text{ pts price} $$

---

## 7. Service-Retained vs Service-Released Pricing

| Approach | Originator Cash Flow | Originator Asset |
|---|---|---|
| Service-Released | + SRP at sale | None |
| Service-Retained | + Net Servicing income over time | MSR on balance sheet |

Break-even SRP (the SRP at which the originator is indifferent):
$$ \text{SRP}_\text{indifferent} = \text{MSR Value}_\text{at originator's cost of capital} $$

---

## 8. Capitalized Rate / Service Multiple Approximation

For quick MSR estimation:
$$ \text{MSR} \approx s \cdot L \cdot M_s $$

Where $M_s$ is the service multiple (a function of market conditions, prepay outlook, and rate environment).

### Common Quick-Reference Multiples
| Rate Environment | $M_s$ (typical) |
|---|---|
| Strong rally (high prepay risk) | 2.0–3.0 |
| Stable | 4.0–5.0 |
| Strong sell-off (low prepay) | 5.5–6.5 |

---

## 9. Excess Servicing Strip

When servicing fee exceeds the base 25 bp minimum required by agencies:
$$ \text{Excess Strip} = s - 0.25\% $$

Excess strip can be sold separately as an IO (interest-only) strip.
$$ \text{IO Value} \approx \frac{\text{Excess Strip} \cdot L}{d + \text{CPR}} $$

---

## 10. Prepayment Speed (CPR / SMM / PSA)

### SMM (Single Monthly Mortality)
$$ \text{SMM} = \frac{\text{Voluntary Prepayments in Month}}{\text{Beginning Balance}} $$

### CPR (Conditional Prepayment Rate, Annualized)
$$ \boxed{\text{CPR} = 1 - (1 - \text{SMM})^{12}} $$

### PSA (Public Securities Association Curve)
$$ \text{PSA Speed} = \begin{cases} 0.2\% \cdot t & t \le 30 \text{ months} \\ 6.0\% & t > 30 \text{ months} \end{cases} $$

100 PSA = above; 150 PSA = above × 1.5; etc.

### Worked Example
SMM = 1.0%:
$$ \text{CPR} = 1 - (0.99)^{12} = 1 - 0.886 = 11.4\% $$

---

## 11. Survival Probability

Probability that loan is still outstanding at month $k$:
$$ p_k = \prod_{j=1}^{k} (1 - \text{SMM}_j) $$

For constant SMM:
$$ p_k = (1 - \text{SMM})^k $$

### Worked Example
SMM = 1.0%, $k = 60$:
$$ p_{60} = (0.99)^{60} = 0.547 $$

---

## 12. Weighted Average Life (WAL) — Approximation

$$ \text{WAL} = \frac{1}{12} \cdot \sum_{k=1}^{n} \frac{k \cdot p_k \cdot \mathit{Pr}_k}{L} $$

Typical agency 30Y MBS: WAL ≈ 6–8 years.

---

## 13. SRP Across Loan Attributes

SRP varies by loan attributes (analogous to LLPAs):

$$ \text{SRP}_\text{net} = \text{SRP}_\text{base} + \sum_j \Delta\text{SRP}_j $$

Typical adjusters:
- High loan amount: $+$ (more dollars of servicing)
- Investment property: $-$ (higher default risk)
- High LTV: $-$ (default + early payoff via refi)
- Low FICO: $-$
- ARM: $-$ (shorter expected life)

---

## 14. Servicing Released Indemnification (Recourse)

Reserve for early payoff or default within first 6–12 months:
$$ \text{Indemnity Reserve} = R \cdot \text{SRP} $$

Where $R$ = 0.10–0.25 (10–25% holdback).

Released back to originator if no events within window.

---

## 15. Summary Formula Table

| Quantity | Formula |
|---|---|
| Monthly service fee income | $s \cdot B_{k-1} / 12$ |
| Net servicing income | $I_\text{service} - K_\text{service}/12$ |
| MSR closed-form approx | $(s - K_\%)/(d + \text{CPR}) \cdot L$ |
| MSR full NPV | $\sum (I_\text{svc} - K_\text{svc}) p_k / (1+d)^{k/12}$ |
| MSR multiple | $\text{MSR Value} / (s \cdot L)$ |
| SRP | $\approx$ MSR Value − Investor Cost |
| SRP in price points | $\text{SRP} / L \cdot 100$ |
| CPR from SMM | $1 - (1 - \text{SMM})^{12}$ |
| Survival probability | $p_k = (1 - \text{SMM})^k$ |
| Excess strip value | $(s - 0.25\%) \cdot L / (d + \text{CPR})$ |
| WAL | $(1/12) \sum k \cdot p_k \cdot \mathit{Pr}_k / L$ |
