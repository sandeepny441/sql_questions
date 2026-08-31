# 04. Math Model

This file turns the common-sense model into formulas.

The goal is not to make the math look fancy. The goal is to make each variable say what it means.

## Variables

Use readable names first:

| Variable | Meaning |
|---|---|
| `loan_amount` | Loan amount / unpaid principal balance |
| `sale_price_percent` | Sale price as percent of par, such as `101.50` |
| `servicing_value_bps` | Servicing value in basis points |
| `loan_fees_dollars` | Loan-level fees and other income in dollars |
| `warehouse_carry_dollars` | Net warehouse / carry income in dollars |
| `broker_comp_bps` | Broker compensation paid by lender in basis points |
| `borrower_credit_bps` | Borrower credits paid by lender in basis points |
| `ops_cost_dollars` | Fulfillment / operations cost in dollars |
| `hedge_cost_dollars` | Hedge, lock, fallout, and extension cost in dollars |
| `risk_reserve_dollars` | Expected defect, indemnification, or repurchase reserve in dollars |

If you want shorter spreadsheet column names later, use these:

| Long name | Shorter abbreviation |
|---|---|
| `loan_amount` | `loan_amt` |
| `sale_price_percent` | `sale_px_pct` |
| `servicing_value_bps` | `svc_bps` |
| `loan_fees_dollars` | `fees` |
| `warehouse_carry_dollars` | `carry` |
| `broker_comp_bps` | `broker_bps` |
| `borrower_credit_bps` | `credit_bps` |
| `ops_cost_dollars` | `ops_cost` |
| `hedge_cost_dollars` | `hedge_cost` |
| `risk_reserve_dollars` | `risk_reserve` |

## Basis Points and Points

```text
1 basis point = 0.01%
100 basis points = 1.00% = 1 point
```

For a `$400,000` loan:

```text
1 bp = $400,000 x 0.0001 = $40
100 bps = $4,000
```

## Revenue Side

### Secondary Market Premium

If the loan sale price is `sale_price_percent`, then:

```text
secondary_market_premium =
  loan_amount x ((sale_price_percent / 100) - 1)
```

Example:

```text
loan_amount = $400,000
sale_price_percent = 101.80

secondary_market_premium =
  $400,000 x ((101.80 / 100) - 1)

secondary_market_premium =
  $400,000 x 0.018

secondary_market_premium =
  $7,200
```

Plain English:

```text
The lender funded $400,000.
The market pays $407,200.
The extra $7,200 is the secondary market premium.
```

### Servicing Value

If servicing value is quoted in bps:

```text
servicing_value_dollars =
  loan_amount x (servicing_value_bps / 10,000)
```

Example:

```text
loan_amount = $400,000
servicing_value_bps = 75

servicing_value_dollars =
  $400,000 x (75 / 10,000)

servicing_value_dollars =
  $3,000
```

Plain English:

```text
75 bps means 0.75% of the loan amount.
0.75% of $400,000 is $3,000.
```

### Total Value

```text
total_value =
  secondary_market_premium
+ servicing_value_dollars
+ loan_fees_dollars
+ warehouse_carry_dollars
```

Plain English:

```text
Total value is everything the lender creates or receives from the loan.
```

## Cost Side

### Broker Compensation

```text
broker_comp_dollars =
  loan_amount x (broker_comp_bps / 10,000)
```

Example:

```text
loan_amount = $400,000
broker_comp_bps = 100

broker_comp_dollars =
  $400,000 x (100 / 10,000)

broker_comp_dollars =
  $4,000
```

### Borrower Credit

```text
borrower_credit_dollars =
  loan_amount x (borrower_credit_bps / 10,000)
```

Example:

```text
loan_amount = $400,000
borrower_credit_bps = 15

borrower_credit_dollars =
  $400,000 x (15 / 10,000)

borrower_credit_dollars =
  $600
```

### Total Cost

```text
total_cost =
  broker_comp_dollars
+ borrower_credit_dollars
+ ops_cost_dollars
+ hedge_cost_dollars
+ risk_reserve_dollars
```

Plain English:

```text
Total cost is everything the lender paid away, spent, or reserved for risk.
```

## Net Profit

```text
net_profit =
  total_value
- total_cost
```

Expanded:

```text
net_profit =
  loan_amount x ((sale_price_percent / 100) - 1)
+ loan_amount x (servicing_value_bps / 10,000)
+ loan_fees_dollars
+ warehouse_carry_dollars
- loan_amount x (broker_comp_bps / 10,000)
- loan_amount x (borrower_credit_bps / 10,000)
- ops_cost_dollars
- hedge_cost_dollars
- risk_reserve_dollars
```

Plain English:

```text
Profit =
  what the loan is worth
+ what servicing is worth
+ extra income
- what the lender gave away
- what the lender spent
- what risk the lender kept
```

## Margin in Basis Points

```text
margin_bps =
  (net_profit / loan_amount) x 10,000
```

Example:

```text
net_profit = $4,400
loan_amount = $400,000

margin_bps =
  ($4,400 / $400,000) x 10,000

margin_bps =
  110 bps
```

Plain English:

```text
The lender made $4,400 on a $400,000 loan.
That is 1.10% of the loan.
1.10% equals 110 bps.
```

## Spreadsheet Layout

You can model each loan like this:

| Line | Item | Formula |
|---:|---|---|
| 1 | Loan amount | Input |
| 2 | Sale price percent | Input |
| 3 | Secondary premium | `loan_amount x ((sale_price_percent / 100) - 1)` |
| 4 | Servicing value bps | Input |
| 5 | Servicing value dollars | `loan_amount x servicing_value_bps / 10,000` |
| 6 | Fees | Input |
| 7 | Net carry | Input |
| 8 | Total value | `line 3 + line 5 + line 6 + line 7` |
| 9 | Broker comp bps | Input |
| 10 | Broker comp dollars | `loan_amount x broker_comp_bps / 10,000` |
| 11 | Borrower credit bps | Input |
| 12 | Borrower credit dollars | `loan_amount x borrower_credit_bps / 10,000` |
| 13 | Ops cost | Input |
| 14 | Hedge / lock cost | Input |
| 15 | Risk reserve | Input |
| 16 | Total cost | `line 10 + line 12 + line 13 + line 14 + line 15` |
| 17 | Net profit | `line 8 - line 16` |
| 18 | Margin bps | `line 17 / line 1 x 10,000` |

## Why the Formula Helps

The formula makes the hidden tradeoff visible:

```text
Every 10 bps of borrower credit on a $400,000 loan costs $400.
Every 25 bps of extra broker comp costs $1,000.
Every 20 bps of better servicing value adds $800.
Every 50 bps of better sale execution adds $2,000.
```

Small changes in bps become meaningful dollars because the loan balance is large.

## The Most Important Sensitivity

For any `loan_amount`, every 1 bp is worth:

```text
loan_amount / 10,000
```

So:

```text
$200,000 loan: 1 bp = $20
$400,000 loan: 1 bp = $40
$800,000 loan: 1 bp = $80
```

That is why lenders obsess over basis points. A few bps per loan multiplied across thousands of loans becomes a business.

