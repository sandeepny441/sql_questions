# 28 — Pipeline & Hedging Math

**Prerequisite:** 27 — TBA & Secondary Pricing

**Goal:** Quantify pipeline composition, expected pull-through, hedge ratios, mark-to-market P&L, and pair-off/fallout costs that drive reprice frequency on the rate sheet.

---

## 1. Pipeline Stages & Pull-Through

### Pull-Through Rate (PT)
$$ \boxed{\text{PT} = \frac{\text{Loans Funded}}{\text{Loans Locked}}} $$

Computed at each stage as cumulative survival.

### Typical Pull-Through by Stage

| Stage | Cumulative PT |
|---|---|
| Locked | 100% |
| Application complete | 95% |
| Submitted to UW | 90% |
| Approved | 85% |
| Cleared to close (CTC) | 95–98% |
| Closed / Funded | 65–85% (overall) |

### Stage-Specific Survival
$$ \text{PT}_\text{stage} = \frac{\text{Loans Moving Forward}}{\text{Loans in Stage}} $$

Overall PT:
$$ \text{PT}_\text{overall} = \prod_\text{stages} \text{PT}_\text{stage} $$

---

## 2. Fallout Rate

$$ \text{Fallout} = 1 - \text{PT} $$

### Pull-Through Sensitivity to Rate
As rates **fall** below lock rates, fallout **rises** (borrowers refi elsewhere or renegotiate):
$$ \text{PT}(\Delta r) \approx \text{PT}_0 + \beta \cdot \Delta r \cdot \mathbb{1}_{\Delta r > 0} $$

Where $\beta$ is sensitivity coefficient (often $\sim 5\%$ pull-through per 25 bp rally).

---

## 3. Pipeline Notional

$$ L_\text{pipeline} = \sum_\text{open locks} L_j $$

Weighted by pull-through:
$$ \boxed{L_\text{exposure} = \sum_j L_j \cdot \text{PT}_j} $$

### Worked Example
Pipeline of 100 loans, each \$400k, PT = 75%:
$$ L_\text{exposure} = 100 \cdot 400{,}000 \cdot 0.75 = \$30{,}000{,}000 $$

---

## 4. Required Hedge Notional (Linear Model)

$$ \boxed{H = L_\text{pipeline} \cdot \text{PT}} $$

For duration-matched hedging:
$$ H_\text{adj} = L_\text{pipeline} \cdot \text{PT} \cdot \frac{D_\text{loan}}{D_\text{hedge}} $$

(Usually $D_\text{loan} \approx D_\text{hedge}$ for matched-coupon TBA hedge → coefficient ≈ 1.)

---

## 5. Hedge Coverage Ratio

$$ \text{HCR} = \frac{H_\text{actual}}{H_\text{required}} $$

Targets: HCR = 1.0 ± 0.05. Outside this range → re-hedge.

---

## 6. Mark-to-Market P&L on Pipeline

For each lock, MTM gain/loss vs. lock price:
$$ \text{PnL}_\text{loan} = (P_\text{lock} - P_\text{market today}) \cdot \frac{L}{100} $$

### Sign Convention
- $P_\text{market} < P_\text{lock}$ ⇒ pipeline gain (loan worth less to deliver, but originator already locked at higher price → wins)

Wait — careful. Originator promised borrower a rate at $P_\text{lock}$. If market price falls, originator can fund and sell at the lock rate but only realize the *current* lower price. So originator **loses** $(P_\text{lock} - P_\text{market})$.

Corrected sign:
$$ \text{PnL}_\text{loan} = (P_\text{market today} - P_\text{lock}) \cdot \frac{L}{100} $$

---

## 7. Hedge P&L

If short TBA at price $P_\text{hedge enter}$:
$$ \text{Hedge PnL} = (P_\text{hedge enter} - P_\text{market today}) \cdot \frac{H}{100} $$

### Worked Example
Pipeline locked at $P = 100.500$, hedge short TBA at $P = 99.750$. Market today: TBA = $99.250$, pipeline retail price = $100.000$.

Pipeline MTM (per loan, \$400k):
$$ (100.000 - 100.500) \cdot 4{,}000 = -\$2{,}000 \text{ (loss)} $$

Hedge MTM (per loan, $H = L \cdot \text{PT} = \$300{,}000$):
$$ (99.750 - 99.250) \cdot 3{,}000 = +\$1{,}500 \text{ (gain)} $$

Net per loan: $-\$2{,}000 + \$1{,}500 = -\$500$.

Hedge offsets 75% of pipeline loss (matches PT ratio).

---

## 8. Pair-Off Cost (Hedge Unwind on Fallout)

When loans fall out, hedge is excess and must be paired off:
$$ \boxed{\text{Pair-Off} = (P_\text{hedge enter} - P_\text{market}) \cdot \frac{H_\text{excess}}{100}} $$

Negative when market improved (loss); positive when market worsened (gain).

### Worked Example
Hedged \$30M at $P = 99.750$. Only \$25M funds (fallout \$5M from PT miss). Today TBA $P = 100.250$:
$$ \text{Pair-Off} = (99.750 - 100.250) \cdot \frac{5{,}000{,}000}{100} = -\$25{,}000 $$

---

## 9. Expected Pair-Off Cost (Risk Reserve)

$$ E[\text{Pair-Off}] = L_\text{pipeline} \cdot \sigma_\text{PT} \cdot E[|\Delta P|] $$

Where $\sigma_\text{PT}$ = standard deviation of pull-through estimate and $E[|\Delta P|]$ = expected absolute price move over lock-to-fund window.

---

## 10. Reprice Trigger Math

A lender's reprice is typically triggered when intraday TBA moves $\ge $ threshold:
$$ \boxed{|\Delta P_\text{TBA, intraday}| \ge \theta_\text{reprice}} $$

Typical $\theta_\text{reprice} = 8\text{-}12$ ticks $= 25\text{-}37.5$ bp.

### Frequency Math (Empirical)
Over $N$ trading days with $f$ reprice events:
$$ \text{Reprice Rate} = \frac{f}{N} \cdot 100\% $$

Industry norms: ~15–25% of days have an intraday reprice.

---

## 11. Optimal Lock Cut-Off Time

Lender wants to lock new loans before the next likely reprice:
$$ t_\text{cutoff} = \arg\min_t E[\text{Pipeline MTM Loss from } t \text{ to } t+\text{overnight}] $$

Common cut-offs: 8:00 PM ET (gives buffer for market close at 3:00 PM ET).

---

## 12. Portfolio Duration of the Pipeline

$$ D_\text{pipeline} = \frac{\sum_j L_j \cdot D_j}{\sum_j L_j} $$

Where each $D_j$ depends on coupon, age, lock period remaining.

Hedge to neutralize duration:
$$ H = \frac{L_\text{pipeline} \cdot D_\text{pipeline}}{D_\text{hedge}} $$

---

## 13. Convexity Hedge (Optional Layer)

For very large pipelines, a layered hedge with TBA + options:
$$ H_\text{convex} = H_\text{linear} + \text{Payer Swaption Notional} $$

Adds protection against large rate moves (where linear hedge under-protects).

---

## 14. Best-Efforts vs Mandatory Trade-Off

Originator chooses delivery method to maximize:
$$ \text{Net Execution} = P_\text{commit} \cdot \text{PT} - (P_\text{pair-off cost}) \cdot (1 - \text{PT}) $$

| Method | Pricing | Pair-Off Risk |
|---|---|---|
| Best-Efforts | Worse (~25 bp lower) | Zero (no delivery obligation) |
| Mandatory | Better | Full (must pay or deliver) |

Break-even PT for mandatory:
$$ \text{PT}^* = \frac{\Delta P_\text{mandatory uplift}}{\Delta P_\text{mandatory uplift} + E[\text{Pair-Off}/L]} $$

If actual PT > PT*, mandatory wins.

---

## 15. Hedge Ratio Re-Balancing Frequency

Rebalance threshold:
$$ |\text{HCR} - 1.0| > \delta_\text{rebalance} $$

Typical $\delta_\text{rebalance} = 0.05$ (5% drift triggers a re-hedge).

Cost per rebalance trade: bid-ask + brokerage ≈ 1–2 bp.

---

## 16. Servicing Float (Earnings on Escrow)

Servicer earns interest on escrow balances:
$$ \text{Float Income} = \bar{B}_\text{escrow} \cdot r_\text{float} $$

Where $r_\text{float}$ = short-term yield earned on escrow balances (currently ~5% on Fed Funds-like rates).

Typical: ~$50–\$100/loan/year of float income.

---

## 17. Summary Formula Table

| Quantity | Formula |
|---|---|
| Pull-through | Funded / Locked |
| Overall PT | $\prod$ stage PTs |
| Fallout | $1 - \text{PT}$ |
| Pipeline exposure | $\sum L_j \cdot \text{PT}_j$ |
| Required hedge | $H = L \cdot \text{PT} \cdot (D_\text{loan}/D_\text{hedge})$ |
| Hedge coverage ratio | $H_\text{actual}/H_\text{required}$ |
| Loan MTM PnL | $(P_\text{today} - P_\text{lock}) \cdot L/100$ |
| Hedge PnL (short) | $(P_\text{enter} - P_\text{today}) \cdot H/100$ |
| Pair-off cost | $(P_\text{enter} - P_\text{today}) \cdot H_\text{excess}/100$ |
| Reprice trigger | $|\Delta P_\text{TBA}| \ge \theta$ (typically 25-37bp) |
| Pipeline duration | $\sum L_j D_j / \sum L_j$ |
| Mandatory BE PT | $\text{PT}^* = \Delta_\text{uplift}/(\Delta_\text{uplift} + E[\text{po}])$ |
| Float income | $\bar{B}_\text{esc} \cdot r_\text{float}$ |
