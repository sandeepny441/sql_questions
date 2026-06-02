# 30 — Best Execution Math

**Prerequisite:** All prior math files (especially 19, 25, 26, 27)

**Goal:** Across multiple investors / wholesalers with different rate sheets, pick the offer that maximizes broker net price and/or minimizes borrower cost — subject to eligibility constraints.

---

## 1. The Core Best-Ex Optimization

For a given scenario across investors $i = 1, \ldots, N$:

$$ \boxed{i^* = \arg\max_{i \in \mathcal{E}} P_\text{net}^{(i)}} $$

Subject to eligibility:
$$ \mathcal{E} = \{ i : \text{loan passes investor } i\text{'s underwriting and product rules} \} $$

Where:
$$ P_\text{net}^{(i)} = P_\text{base}^{(i)} + \sum_j \Delta P_j^{(i)} - C_\text{LPC}^{(i)} $$

---

## 2. Broker-Maximization Best-Ex

$$ \boxed{i^*_\text{broker} = \arg\max_i \bigl( P_\text{broker-facing}^{(i)} \bigr)} $$

This is the standard view: broker keeps the most rebate at the same rate.

### Worked Example
Three investors quote the same rate (6.500%):

| Investor | Base | Adjusters | LPC | Net (broker) |
|---|---|---|---|---|
| A | 100.500 | -1.125 | -2.000 | 97.375 |
| B | 100.625 | -1.000 | -2.000 | 97.625 |
| C | 100.250 | -0.875 | -2.000 | 97.375 |

$$ i^*_\text{broker} = B \text{ (highest at 97.625)} $$

---

## 3. Borrower-Cost Minimization

For the **borrower's** perspective, minimize total cost over expected hold $h$:

$$ \boxed{i^*_\text{borrower} = \arg\min_i \bigl( \text{Discount}_\$^{(i)} + \text{Closing Costs}_\$^{(i)} + \text{NPV of P\&I}^{(i)} - \text{LC}_\$^{(i)} \bigr)} $$

NPV of P&I over hold $h$:
$$ \text{NPV(P\&I)}^{(i)} = \sum_{k=1}^{h \cdot 12} \frac{M^{(i)}}{(1+d)^k} + \frac{B_h^{(i)}}{(1+d)^{h \cdot 12}} $$

Where $d$ = borrower's discount rate (often opportunity cost).

---

## 4. Effective Borrower APR Ranking

Simpler than full NPV — rank by APR:
$$ i^*_\text{APR} = \arg\min_i r_{APR}^{(i)} $$

But APR assumes loan to maturity; for short hold:
$$ y_\text{hold}^{(i)} \approx r^{(i)} + \frac{\text{PFC}^{(i)}}{L \cdot h} $$

Rank by $y_\text{hold}^{(i)}$ for hold horizon $h$.

---

## 5. Anti-Steering Safe Harbor (Reg Z) — Three-Option Test

Broker must present from each pricing class:

$$ \text{Set}_\text{safe-harbor} = \{ L_\text{lowest rate},\; L_\text{lowest pts},\; L_\text{lowest fees} \} $$

Where each is selected from offers the borrower likely qualifies for. Broker may close on any of the three.

---

## 6. Eligibility Filtering Math

Investor $i$ eligibility is a set of binary tests:
$$ \mathcal{E}_i = \prod_j \mathbb{1}\bigl( \text{Loan attribute}_j \in \text{Investor}_i\text{'s allowed set}_j \bigr) $$

Loan passes investor $i$ iff $\mathcal{E}_i = 1$.

### Common Filters
| Filter | Test |
|---|---|
| Loan amount | $L_\text{min}^{(i)} \le L \le L_\text{max}^{(i)}$ |
| FICO | $\text{FICO} \ge \text{FICO}_\text{min}^{(i)}$ |
| LTV | $\text{LTV} \le \text{LTV}_\text{max}^{(i,\text{prog})}$ |
| DTI | $\text{DTI} \le \text{DTI}_\text{max}^{(i)}$ |
| Property type | $\in \text{allowed}$ |
| Occupancy | $\in \text{allowed}$ |

---

## 7. Rate-Adjusted Cross-Investor Comparison

When two investors quote different rates, normalize to same target rate (or same target price):

### Method A: Same Rate, Compare Prices
Compute each investor's price at borrower's target rate $r^*$:
$$ P_i(r^*) = P_i^\text{grid}(r^*) + \sum_j \Delta P_j^{(i)} $$
$$ i^* = \arg\max_i P_i(r^*) $$

### Method B: Same Price, Compare Rates
Find each investor's rate that yields a target price (e.g., par):
$$ r_i^{(\text{par})} = \arg\min_r |P_i(r) - 100| $$
$$ i^* = \arg\min_i r_i^{(\text{par})} $$

---

## 8. Multi-Dimensional Best-Ex (Pareto Frontier)

For borrowers comparing rate AND closing cost simultaneously:

A loan offer $i$ **dominates** offer $j$ if:
$$ r^{(i)} \le r^{(j)} \quad \text{AND} \quad \text{Cash to Close}^{(i)} \le \text{Cash to Close}^{(j)} $$
with at least one strict.

Borrower chooses from the Pareto frontier; broker presents the dominant options.

---

## 9. Lender-Credit-Maximizing Best-Ex

If borrower wants maximum lender credit at a specific rate ceiling $r_\text{max}$:
$$ i^* = \arg\max_i \text{LC}_\$^{(i)} \quad \text{s.t.} \quad r^{(i)} \le r_\text{max} $$

---

## 10. Cross-Channel Best-Ex (Wholesale vs Correspondent)

Broker selling correspondent may compare:
$$ P_\text{wholesale}^{(i)} \quad \text{vs.} \quad P_\text{correspondent}^{(j)} - K_\text{correspondent overhead} $$

Where $K$ = warehouse cost, hedging cost, ops cost.

Break-even:
$$ P_\text{correspondent}^* = P_\text{wholesale}^* + K_\text{correspondent overhead} $$

---

## 11. Scenario Coverage Matrix

Best-ex must run across product variations:
$$ \mathcal{S} = \{ (\text{program}_a, \text{rate}_b, \text{lock}_c, \text{MI option}_d) : \text{eligible} \} $$

Total scenarios:
$$ |\mathcal{S}| = |\text{programs}| \cdot |\text{rates}| \cdot |\text{locks}| \cdot |\text{MI options}| $$

PPE software evaluates the full Cartesian product and surfaces the optimum.

---

## 12. Real-Time Best-Ex Update Math

Net price changes as sheets refresh. Probability that current best-ex changes after $t$ minutes:
$$ P(\text{best-ex changes}) = 1 - \prod_i \bigl(1 - p_\text{reprice}^{(i)}(t)\bigr) $$

If 5 investors each have 5% probability of repricing in 30 minutes:
$$ P = 1 - 0.95^5 = 1 - 0.774 = 22.6\% $$

(Justifies real-time re-pricing rather than morning-only.)

---

## 13. Best-Ex Across Different Comp Plans (Self-Compensation Decision)

A broker may have multiple comp plans across investor relationships:
$$ i^* = \arg\max_i \bigl( P_\text{net}^{(i)} - C^{(i)} + \text{Net to Broker Pocket}^{(i)} \bigr) $$

Where "Net to Broker Pocket" is the actual dollar comp the LO/broker keeps, accounting for plan-by-plan caps/floors.

---

## 14. Mandatory Best-Ex (Secondary Market Side)

For a correspondent/aggregator selling to multiple investors:
$$ i^* = \arg\max_i \bigl( P_\text{cash}^{(i)} - K_\text{delivery}^{(i)} - K_\text{eligibility}^{(i)} \bigr) $$

Considering:
- Cash execution
- MBS execution (TBA + spec pool)
- Co-issue
- AOT

Net of delivery fees and counterparty risk.

---

## 15. Best-Ex with Tie-Breakers

When two offers are within a tolerance:
$$ |P^{(i)} - P^{(j)}| < \epsilon \quad \text{(typically 1/16 to 1/8 point)} $$

Tie-breakers:
1. Turn time / SLA
2. Underwriting flexibility
3. Lock policy generosity
4. Concession history
5. AE relationship

These are **non-quantitative** but can be encoded as weights:
$$ \text{Score}_i = P_\text{net}^{(i)} + \sum_w w_k \cdot \text{Quality}_k^{(i)} $$

---

## 16. Composite End-to-End Worked Example

Loan: \$500,000, 30Y Fixed, 720 FICO, 80 LTV, Owner-Occ Purchase.

| Investor | Rate | Base @ 30-day | LLPA sum | State adj | LPC (2%) | $P_\text{broker}$ |
|---|---|---|---|---|---|---|
| Investor X | 6.500 | 101.000 | -1.250 | 0 | -2.000 | 97.750 |
| Investor Y | 6.500 | 100.875 | -1.000 | +0.125 | -2.000 | 98.000 |
| Investor Z | 6.500 | 101.250 | -1.500 | 0 | -2.000 | 97.750 |

$$ i^* = \text{Y at 98.000} \Rightarrow \text{Broker prefers Y by 25 bp} $$

Dollar advantage:
$$ \Delta\$ = (98.000 - 97.750) \cdot \frac{500{,}000}{100} = \$1{,}250 $$

---

## 17. Summary Formula Table

| Quantity | Formula |
|---|---|
| Investor net price | $P_\text{net}^{(i)} = P_\text{base} + \sum \Delta P - C_\text{LPC}$ |
| Broker best-ex | $\arg\max_i P_\text{broker}^{(i)}$ |
| Borrower min APR | $\arg\min_i r_{APR}^{(i)}$ |
| Effective hold yield | $r + \text{PFC}/(L \cdot h)$ |
| Eligibility filter | $\mathcal{E}_i = \prod_j \mathbb{1}(\text{attr}_j \in \text{allowed})$ |
| Pareto dominance | $r^{(i)} \le r^{(j)}$ and CTC$^{(i)} \le$ CTC$^{(j)}$ |
| Cross-channel BE | $P_\text{corr}^* = P_\text{whole}^* + K_\text{corr}$ |
| Best-ex change prob | $1 - \prod (1 - p_\text{reprice}^{(i)})$ |
| Tie-breaker score | $P + \sum w_k Q_k$ |
| Three-option safe harbor | $\{L_\text{lowest rate}, L_\text{lowest pts}, L_\text{lowest fees}\}$ |
| Scenario space | $|\mathcal{S}| = \prod_\text{dims} |\text{options}_\text{dim}|$ |
