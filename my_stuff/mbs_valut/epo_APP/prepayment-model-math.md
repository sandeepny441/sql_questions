# Prepayment Model – Mathematical Documentation

This document explains the mathematics behind the Single Loan Prepayment Model in a clear, step-by-step manner.

---

## 1. Overview

The model simulates the **monthly evolution** of a single loan over up to 30 years (360 months). Each month it calculates:

- How much principal is paid down (scheduled + prepayments)
- The probability that the loan has been fully prepaid by that point

The two main outputs are:
- **Remaining Principal %** (blue line)
- **Cumulative Payoff Probability %** (red line)

---

## 2. Monthly Prepayment Rate (CPR)

The heart of the model is the **monthly conditional prepayment rate**.

### 2.1 Core Formula

$$
\text{monthlyCPR} = 0.005 \times S \times (1 + 4 \cdot I) \times F \times G \times L \times A \times B
$$

Where the terms are capped so that $0 \leq \text{monthlyCPR} \leq 0.15$.

### 2.2 Factor Definitions

#### Interest Rate Incentive ($I$)

$$
I = \frac{1}{1 + e^{-20 \cdot (\text{incentive} - 1.0)}}
$$

where

$$
\text{incentive} = r_{\text{note}} - r_{\text{market}}
$$

**Example**:
- Note rate = 6.5%, Market rate = 4.5% → incentive = 2.0%
- $I \approx 0.88$ (very strong incentive)

#### FICO Factor ($F$)

$$
F = 0.5 + 1.0 \times \frac{\text{FICO} - 500}{350}
$$

- FICO = 500 → $F = 0.5$
- FICO = 720 → $F \approx 1.13$
- FICO = 850 → $F = 1.5$

#### Seasoning / Age Factor ($G$)

This combines two effects:

**Ramp-up effect** (logistic):

$$
\text{ramp} = \frac{1}{1 + e^{-0.015 \cdot (\text{current age} - 20)}}
$$

**Peak effect** (Gaussian around month 35):

$$
\text{peak} = 0.2 \times \exp\left( -\frac{(\text{current age} - 35)^2}{8000} \right)
$$

Final seasoning factor:

$$
G = 0.3 + 0.65 \times \text{ramp} + \text{peak}
$$

#### LTV Factor ($L$)

$$
L = 1 - 0.4 \times \frac{\text{LTV} - 50}{50}
$$

- LTV = 50% → $L = 1.0$
- LTV = 80% → $L = 0.76$
- LTV = 100% → $L = 0.60$

Higher LTV → lower factor (harder to refinance).

#### Housing Appreciation Factor ($A$)

$$
A = 1 + 0.15 \times \text{annual HPA}
$$

- 3% annual appreciation → $A = 1.45$

#### Seasonality ($S$)

User-controlled multiplier, typically between 0.5 and 1.5.

#### Borrower Propensity ($B$)

Direct multiplier (default = 1.0). Values > 1.0 increase prepayment speed.

---

## 3. Scheduled Amortization (Simplified)

The model uses a very simple scheduled principal paydown:

$$
\text{scheduled monthly rate} = \frac{1}{\text{original term (months)}}
$$

This is a crude approximation (real amortization is front-loaded in interest). It is deliberately kept simple so the focus stays on prepayment behavior.

---

## 4. Monthly Simulation Loop

For each future month $t = 1, 2, \dots, 360$:

### Step 1: Compute this month’s prepayment rate

$$
\text{CPR}_t = \text{monthlyCPR}(\text{age} = \text{loan age} + t)
$$

### Step 2: Total principal reduction

$$
\text{Total reduction}_t = \text{scheduled} + \text{CPR}_t \times \text{current principal}
$$

### Step 3: Update principal balance

$$
\text{New principal} = \max(0, \text{old principal} - \text{Total reduction}_t)
$$

### Step 4: Record payoff probability increment

Let $S_{t-1}$ = probability the loan has **not** prepaid yet (survival probability).

Then the probability it prepays in month $t$ is:

$$
\text{Payoff increment}_t = S_{t-1} \times \text{CPR}_t
$$

Update cumulative payoff probability:

$$
S_t = S_{t-1} - \text{Payoff increment}_t
$$

---

## 5. Key Derived Metrics

### 5.1 Weighted Average Life (WAL)

$$
\text{WAL} = \frac{\sum_{t=1}^{360} (t/12) \times \text{payoff probability in month } t}{\sum \text{payoff probabilities}}
$$

This is the expected average life of the loan in years, weighted by when principal actually leaves.

### 5.2 5-Year Payoff Probability

Sum the payoff increments over the first 60 months:

$$
P(\text{paid off within 5 years}) = \sum_{t=1}^{60} \text{Payoff increment}_t
$$

---

## 6. Big Picture Formula (Conceptual)

While the model is computed month-by-month, conceptually it can be summarized as:

$$
\text{Principal remaining}(T) = 1 - \sum_{t=1}^{T} \left( \text{scheduled}_t + \text{CPR}_t \times \text{survival up to } t \right)
$$

$$
\text{Cumulative Payoff Probability}(T) = 1 - \prod_{t=1}^{T} (1 - \text{CPR}_t)
$$

(approximately, ignoring the interaction with scheduled payments)

The full simulation combines both scheduled amortization and the time-varying, multi-factor CPR.

---

## 7. Important Simplifications & Limitations

- Scheduled amortization is linear (not real mortgage amortization schedule).
- No burnout effect (borrowers who could have refinanced but didn’t).
- No media or psychological effects modeled explicitly.
- No distinction between refinancing, sale, and cash payoff.
- No stochastic interest rate paths (deterministic scenario).
- Many borrower-specific factors (DTI, employment, life events) are not yet included in the calculation engine (they exist only as UI placeholders).

---

## 8. Summary

The model is a **multi-factor, time-varying hazard model** for loan survival, combined with a simplified amortization schedule. The core innovation is the rich CPR function that reacts to rate incentive, credit, seasoning, leverage, and housing market conditions.

This structure allows the interactive tool to show how changes in borrower, loan, and market conditions translate into dramatically different principal decay and payoff probability curves.