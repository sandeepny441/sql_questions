# Early Loan Payoff Analysis Using Servicing Data

This guide explains how to understand the factors behind **Early Loan Payoff $EPO$** when UWM receives servicing data from a subservicer such as **MR Cooper** or **Cenlar**.

The goal is not just to predict that a loan may pay off early. The goal is to explain **why** it paid off early, which factors were visible before payoff, and whether the payoff looked like a refinance, sale, curtailment, servicing transfer, or data-quality issue.

---

## 1. What EPO Means

An **Early Loan Payoff** happens when a mortgage is paid in full sooner than expected, usually within a defined early window after origination or sale.

Common EPO windows:

| Window | Meaning |
|---|---|
| 3 months | Very fast payoff, often refinance churn, sale fallout, or origination/boarding issue |
| 6 months | Common repurchase or premium-recapture concern |
| 12 months | Broader early runoff measure |
| 18 months | Useful for borrower-retention and servicing-performance analysis |

From a lender or investor perspective, EPO matters because the loan exits before expected income, servicing value, or secondary-market economics can be realized.

---

## 2. Main Question

The core question is:

> Given what the servicer knew month by month, what factors made this borrower more likely to pay off early?

Servicing data can help answer that question because it shows the loan after closing:

- Payment behavior
- Current unpaid principal balance
- Delinquency status
- Escrow changes
- Payoff request activity
- Curtailments
- Servicing notes or event codes
- Loss mitigation or hardship flags
- Property and borrower contact changes
- Transfer, boarding, and payoff dates

The servicer usually cannot explain every borrower decision directly, but the servicing tape can reveal strong signals.

---

## 3. The Five EPO Driver Buckets

Most early payoff explanations fall into five buckets.

| Bucket | What It Means | Servicing Data Clues |
|---|---|---|
| **Rate incentive** | Borrower had a financial reason to refinance | Note rate, market-rate comparison, payoff during rate drop, high FICO, low LTV |
| **Equity and liquidity** | Borrower had enough equity or cash to refinance, sell, or pay down | UPB decline, property value estimate, LTV, curtailments, escrow refunds |
| **Borrower behavior** | Borrower showed signs of active mortgage management | Extra principal payments, payoff quote requests, frequent account activity |
| **Life or property event** | Borrower sold, moved, divorced, inherited cash, or changed plans | Mailing-address change, occupancy clues, payoff source, real estate sale timing |
| **Servicing or operational issue** | Payoff was connected to servicing experience, transfer, boarding, or data issue | Complaints, disputes, payment misapplication, boarding errors, transfer flags |

The best EPO analysis does not rely on one field. It combines these buckets into a story.

---

## 4. Data UWM Should Request From MR Cooper or Cenlar

For EPO analysis, the most useful file is a **monthly loan-level servicing snapshot** plus a **payoff event file**.

### A. Monthly Loan Snapshot

Each row should represent one loan for one reporting month.

Recommended fields:

| Field | Why It Matters |
|---|---|
| Loan ID / investor loan number | Joins servicing records to origination and sale data |
| Reporting month | Creates the loan timeline |
| Origination date | Measures loan age |
| Boarding date | Detects transfer or onboarding issues |
| First payment due date | Helps identify first-payment behavior |
| Original UPB | Starting balance |
| Current UPB | Tracks balance decline |
| Scheduled principal and interest | Separates scheduled amortization from extra paydown |
| Actual principal paid | Detects curtailments or payoff buildup |
| Interest rate | Drives refinance incentive |
| Remaining term | Shows amortization path |
| Loan type | Conventional, FHA, VA, USDA, jumbo, etc. |
| Occupancy | Primary, second home, investment |
| Property state and ZIP | Captures local housing and rate behavior |
| Delinquency status | Distinguishes voluntary prepay from distress behavior |
| Current due date | Confirms payment status |
| Payment received date | Shows payment consistency |
| Escrow balance | May flag tax/insurance changes or refunds |
| Loss mitigation flag | Separates hardship exits from normal EPO |
| Bankruptcy flag | Separates legal or distress-driven exits |
| Foreclosure flag | Avoids misclassifying default exits as voluntary payoff |
| Servicing transfer flag | Controls for operational changes |

### B. Payoff Event File

Each row should represent a payoff or liquidation event.

Recommended fields:

| Field | Why It Matters |
|---|---|
| Loan ID | Joins to monthly snapshots |
| Payoff date | Defines the EPO event date |
| Payoff amount | Confirms full liquidation |
| Payoff reason code | Best direct clue if available |
| Payoff quote request date | Leading indicator of payoff |
| Payoff quote expiration date | Helps time borrower intent |
| Payoff funds received date | Confirms execution |
| Investor remittance date | Confirms reporting month |
| Liquidation code | Separates payoff, repurchase, foreclosure, transfer, short sale |
| New servicer or transfer indicator | Avoids false EPO classification |
| Refinance indicator | Strongest label if available |
| Sale indicator | Separates housing turnover from refinance |

### C. Servicing Event or Activity File

This file is optional but very valuable.

Useful events:

| Event | EPO Interpretation |
|---|---|
| Payoff quote requested | Borrower is actively preparing to exit |
| Verbal payoff request | High-intent signal |
| Written payoff demand | High-intent signal |
| Address change | Possible sale, move, divorce, or occupancy shift |
| Complaint or dispute | Possible servicing-friction payoff |
| Recast request | Borrower has liquidity but may not fully prepay |
| Large curtailment | Borrower has liquidity or sale/refi preparation |
| Escrow cancellation | Possible refinance or payoff preparation |
| ACH cancellation | Possible upcoming payoff or servicer switch |
| Insurance cancellation/change | Possible sale or refinance |
| Tax disbursement anomaly | May cause borrower frustration or refinance |

---

## 5. Create a Clean EPO Label

Before modeling factors, define the event clearly.

Suggested EPO label:

```text
EPO = 1 if loan paid in full within N months of origination or sale date
EPO = 0 otherwise
```

Use multiple labels:

| Label | Definition |
|---|---|
| `epo_3m` | Paid off within 3 months |
| `epo_6m` | Paid off within 6 months |
| `epo_12m` | Paid off within 12 months |
| `epo_18m` | Paid off within 18 months |

Also create an exclusion flag:

```text
exclude_from_voluntary_epo = 1 if liquidation was foreclosure, short sale, servicing transfer, repurchase correction, data cleanup, or investor transfer
```

This prevents operational exits from being confused with borrower-driven payoffs.

---

## 6. Build the Core Explanatory Variables

The raw servicing fields become more useful after transformation.

### A. Loan Age

```text
loan_age_months = months between origination date and reporting month
```

Why it matters:

- Extremely early payoff may suggest churn, sale fallout, or bad lead retention.
- Payoff after several months may look more like rate-driven refinance or property sale.

### B. Rate Incentive

```text
rate_incentive = note_rate - current_market_rate_for_similar_product
```

Interpretation:

| Rate Incentive | Meaning |
|---|---|
| Negative | Borrower rate is better than market; refinance is unlikely for rate savings |
| 0.00% to 0.50% | Weak refinance incentive |
| 0.50% to 1.00% | Moderate incentive |
| Greater than 1.00% | Strong refinance incentive |

This is usually one of the strongest EPO drivers.

### C. Balance Burnoff

```text
monthly_balance_change = prior_month_upb - current_month_upb
extra_principal = actual_principal_paid - scheduled_principal
```

Interpretation:

- Small regular balance decline means normal amortization.
- Large extra principal payments may indicate liquidity.
- A sudden full payoff after a payoff quote suggests intentional exit.

### D. Payment Behavior

Useful features:

| Feature | Meaning |
|---|---|
| Days past due | Separates clean voluntary payoff from distress |
| Number of late payments | Shows payment friction |
| Payment timing variance | Measures consistency |
| First payment default flag | May indicate early credit/boarding issue |
| ACH enrollment | Stable payment behavior; cancellation may signal payoff |

Clean payers with strong rate incentive are classic refinance EPO candidates.

Late payers are less likely to refinance through standard channels, so their payoff may need a different explanation.

### E. Curtailment Behavior

```text
large_curtailment_flag = 1 if extra principal exceeds threshold
```

Possible thresholds:

| Threshold | Use Case |
|---|---|
| Greater than 1 scheduled payment | Detects intentional extra paydown |
| Greater than 5% of UPB | Detects major liquidity event |
| Greater than $10,000 | Simple operational threshold |

Large curtailments before payoff can mean:

- Borrower has excess cash
- Borrower is preparing for refinance
- Borrower is selling and clearing balance
- Borrower received proceeds from another event

### F. Servicing Friction

Create indicators for:

| Indicator | Why It Matters |
|---|---|
| Complaint filed | Borrower may refinance away due to poor experience |
| Payment dispute | Possible dissatisfaction |
| Escrow shortage shock | Payment increase can trigger refinance or sale |
| Force-placed insurance | Strong servicing friction signal |
| Tax/insurance error | Can create payoff motivation |
| Repeated call activity | Borrower is engaged or frustrated |

Servicing friction is rarely the only cause, but it can explain why a borrower leaves even without a strong rate incentive.

---

## 7. Distinguish Refinance EPO From Sale EPO

This distinction is critical.

### Refinance-Like EPO

Likely refinance indicators:

- Strong positive rate incentive
- High FICO at origination
- Clean payment history
- Low or improving LTV
- Payoff quote requested before payoff
- No delinquency or hardship flag
- Same mailing address after payoff if available
- Payoff occurs during broad refinance wave

Likely story:

> The borrower had the ability and incentive to refinance, requested a payoff quote, and exited cleanly.

### Sale-Like EPO

Likely sale indicators:

- Mailing address changed
- Property insurance changed or canceled
- Payoff not strongly explained by rate incentive
- Local home price appreciation is high
- Borrower paid off during spring/summer home-sale season
- Payoff amount aligns with property transfer timing if public record is joined

Likely story:

> The loan prepaid because the property was likely sold, not because the borrower refinanced for rate savings.

### Distress or Operational Exit

Possible non-voluntary indicators:

- Delinquency before payoff
- Bankruptcy or loss mitigation flag
- Foreclosure or short-sale code
- Servicing transfer indicator
- Repurchase or correction code
- Data cleanup or investor-transfer code

Likely story:

> This payoff should not be analyzed as normal borrower EPO without further review.

---

## 8. EPO Factor Scorecard

A simple scorecard can make the analysis explainable before building a statistical model.

| Factor | Low Risk | Medium Risk | High Risk |
|---|---|---|---|
| Rate incentive | Less than 0.50% | 0.50% to 1.00% | Greater than 1.00% |
| Loan age | Greater than 18 months | 7 to 18 months | 0 to 6 months |
| Payment history | Late or unstable | Mostly current | Always current |
| Curtailments | None | Occasional extra principal | Large extra principal before payoff |
| Payoff quote activity | None | Inquiry only | Formal payoff quote |
| LTV/equity | High LTV | Moderate equity | Strong equity |
| Servicing friction | None | One issue | Multiple issues or complaint |
| Seasonality | Off-season | Neutral | Spring/summer sale season or refi wave |

Example interpretation:

```text
High EPO risk = strong rate incentive + clean payment history + strong equity + payoff quote request.
```

That pattern points toward refinance-driven EPO.

---

## 9. Recommended Analysis Workflow

### Step 1: Build the Loan Timeline

For every loan, create a month-by-month record:

```text
loan_id
reporting_month
loan_age_months
current_upb
payment_status
actual_principal_paid
scheduled_principal
event_codes
payoff_flag
```

The timeline is the foundation. Without it, you only know that a payoff happened, not what happened before it.

### Step 2: Classify the Payoff

Assign each payoff into one of these categories:

| Category | Description |
|---|---|
| Refinance-like payoff | Strong rate/equity/credit pattern |
| Sale-like payoff | Address/property/seasonality pattern |
| Curtailment/liquidity payoff | Large principal reductions before payoff |
| Servicing-friction payoff | Complaints, disputes, escrow shocks, servicing errors |
| Distress/operational payoff | Default, foreclosure, transfer, correction, repurchase |
| Unknown | Not enough evidence |

### Step 3: Compare EPO Loans to Non-EPO Loans

For each factor, compare:

```text
EPO loans vs loans still active at the same age
```

Do not compare a 3-month-old EPO loan to a 36-month-old active loan. That creates false conclusions.

Use same-age comparison cohorts:

| Cohort | Comparison |
|---|---|
| 0 to 3 months | EPO within 3 months vs active at 3 months |
| 4 to 6 months | EPO within 6 months vs active at 6 months |
| 7 to 12 months | EPO within 12 months vs active at 12 months |

### Step 4: Measure Factor Lift

For each factor, calculate:

```text
EPO rate when factor is present / EPO rate when factor is absent
```

Example:

```text
EPO rate with payoff quote = 18%
EPO rate without payoff quote = 3%
Lift = 6.0x
```

That means a payoff quote request is associated with six times the EPO rate.

### Step 5: Build an Explainable Model

Good first models:

| Model | Why Use It |
|---|---|
| Logistic regression | Clear directional effects |
| Decision tree | Easy payoff-rule explanations |
| Gradient boosting | Strong predictive power |
| Survival model | Best when timing matters |

The best structure for EPO is usually a **survival or hazard model**, because EPO is a timing problem:

```text
What is the probability this active loan pays off next month, given that it has survived until now?
```

---

## 10. Monthly Hazard View

For each active loan-month, define:

```text
target = 1 if loan pays off in the next month
target = 0 if loan remains active
```

Then use the fields known as of that month:

```text
note_rate
market_rate
rate_incentive
loan_age_months
current_upb
payment_status
extra_principal
payoff_quote_flag
complaint_flag
escrow_shortage_flag
property_state
occupancy
loan_product
```

This avoids hindsight. The model only sees information that would have been available before payoff.

---

## 11. Example EPO Explanations

### Example 1: Rate-Driven Refinance

```text
Loan paid off in month 5.
Borrower was current every month.
Note rate was 7.125%.
Comparable market rate fell to 6.000%.
Payoff quote was requested 18 days before payoff.
No delinquency, complaint, or transfer flag.
```

Explanation:

> This looks like a refinance-driven EPO. The borrower had a strong rate incentive, clean payment history, and clear payoff intent before liquidation.

### Example 2: Sale-Driven EPO

```text
Loan paid off in month 8.
Rate incentive was weak.
Borrower mailing address changed.
Insurance activity occurred before payoff.
Payoff occurred in June.
Property was in a high-appreciation ZIP code.
```

Explanation:

> This looks more like a property-sale payoff than a refinance. The rate incentive was not strong enough to explain the payoff by itself.

### Example 3: Servicing-Friction EPO

```text
Loan paid off in month 4.
No meaningful rate incentive.
Borrower filed escrow dispute.
Payment increased after escrow analysis.
Payoff quote requested shortly after the dispute.
```

Explanation:

> This payoff may have been influenced by servicing friction. The borrower had no obvious refinance incentive, but servicing events preceded the payoff.

### Example 4: Operational Exclusion

```text
Loan liquidated in month 2.
Liquidation code indicates servicing transfer.
No borrower payoff funds were received.
```

Explanation:

> This should not be counted as borrower-driven EPO. It is an operational transfer event, not a voluntary early payoff.

---

## 12. Dashboard Metrics

A useful EPO dashboard should include:

| Metric | Purpose |
|---|---|
| EPO count | Number of early payoffs |
| EPO rate | EPO count divided by eligible population |
| EPO UPB | Dollar exposure that paid off early |
| EPO by month-on-book | Shows timing pattern |
| EPO by product | Identifies product concentration |
| EPO by channel or broker | Detects origination channel risk |
| EPO by state/MSA | Captures geography and housing turnover |
| EPO by rate incentive band | Separates refi-driven payoff from other causes |
| EPO by payoff reason | Explains event type |
| Payoff quote to payoff conversion | Measures borrower intent |
| Large curtailment before payoff | Captures liquidity-driven behavior |
| Complaint before payoff | Captures servicing-friction behavior |

The key view is:

```text
EPO rate by loan age, segmented by rate incentive and payoff type.
```

That view usually separates normal prepayment behavior from abnormal early runoff.

---

## 13. Red Flags in Servicing Data

Watch for these issues before drawing conclusions:

| Red Flag | Why It Matters |
|---|---|
| Payoff date missing but UPB is zero | Event may be coded incorrectly |
| Liquidation code says transfer, not payoff | Not borrower EPO |
| Boarding date after origination by a long gap | Early activity may be missing |
| First reporting month already shows zero balance | Loan may have paid off before clean servicing history exists |
| Payoff reason code is blank | Requires proxy classification |
| Duplicate loan IDs | Can double-count EPO |
| Negative or impossible UPB | Data-quality issue |
| Delinquency status inconsistent with due date | Payment status may be unreliable |
| Servicer transfer around payoff date | May be operational, not borrower behavior |

Data quality is especially important for 3-month and 6-month EPO because small date errors can change the label.

---

## 14. Practical Takeaways

To understand EPO from MR Cooper or Cenlar servicing data, focus on four questions:

1. **Did the borrower have a financial incentive to leave?**
   - Rate incentive, equity, loan size, product type.

2. **Did the borrower have the ability to leave?**
   - Clean payment history, sufficient equity, no distress flags.

3. **Did the borrower show intent before payoff?**
   - Payoff quote request, large curtailment, ACH cancellation, account activity.

4. **Was the event truly borrower-driven?**
   - Exclude transfers, foreclosure, repurchase corrections, and data cleanup events.

The strongest EPO explanation usually combines:

```text
rate incentive + borrower ability + payoff intent + clean voluntary payoff code
```

When those are absent, look for:

```text
sale signals, servicing friction, liquidity events, distress codes, or operational exclusions
```

---

## 15. Best Final Output

For each EPO loan, produce a short explanation like this:

```text
Loan 12345 paid off 5 months after origination.
The payoff appears refinance-driven.
The borrower had a 1.25% rate incentive, remained current, had no hardship flags, and requested a payoff quote 21 days before payoff.
No servicing transfer, foreclosure, or operational exclusion was present.
```

For portfolio reporting, summarize like this:

```text
Of all 6-month EPO loans, 58% appear refinance-driven, 19% appear sale-driven, 7% show servicing-friction signals, 4% are distress-related, 6% are operational exclusions, and 6% remain unknown.
```

That turns servicing data into an explanation, not just a payoff count.



