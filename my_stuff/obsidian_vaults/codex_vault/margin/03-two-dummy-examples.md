# 03. Two Dummy Examples

Both examples use the same loan size:

```text
Loan amount: $400,000
```

The difference is not the loan balance. The difference is pricing, costs, market value, servicing value, and execution.

## Quick Conversion

On a `$400,000` loan:

```text
1 basis point = 0.01% x $400,000 = $40
10 basis points = $400
100 basis points = 1 point = $4,000
```

## Example A: Higher-Profit Transaction

This is a clean file with favorable pricing, decent servicing value, and low operational friction.

### Revenue / Value Created

| Item | Dummy Assumption | Dollar Value |
|---|---:|---:|
| Secondary market premium | Loan sells at `101.80` | `$7,200` |
| Servicing right value | `0.75 points` | `$3,000` |
| Loan-level fees | Flat dummy amount | `$900` |
| Net warehouse / carry | Small positive | `$200` |
| **Total value** |  | **`$11,300`** |

Secondary market premium math:

```text
101.80% x $400,000 = $407,200
$407,200 - $400,000 = $7,200
```

Servicing value math:

```text
0.75% x $400,000 = $3,000
```

### Costs / Value Given Up

| Item | Dummy Assumption | Dollar Cost |
|---|---:|---:|
| Broker compensation paid by lender | `1.00 point` | `$4,000` |
| Borrower credit | `0.15 points` | `$600` |
| Fulfillment / operations cost | Clean file | `$1,700` |
| Hedge / lock leakage | Smooth execution | `$400` |
| Expected defect / repurchase reserve | Low-risk file | `$200` |
| **Total cost** |  | **`$6,900`** |

### Net Result

```text
Total value: $11,300
- total cost: $6,900
= net transaction profit: $4,400
```

Margin in basis points:

```text
$4,400 / $400,000 = 1.10%
1.10% = 110 bps
```

### Common-Sense Explanation

The lender made good money because:

```text
The loan sold at a good premium.
The servicing right had meaningful value.
The broker comp and borrower credit were not too large.
The file was cheap to process.
The hedge/lock execution did not leak much value.
The defect risk was low.
```

This does not mean the borrower was treated badly. It means the lender found a good balance between competitive borrower pricing and strong secondary-market execution.

## Example B: Lower-Profit Transaction

This loan has the same `$400,000` balance, but the lender competes harder to win it and the execution is less favorable.

### Revenue / Value Created

| Item | Dummy Assumption | Dollar Value |
|---|---:|---:|
| Secondary market premium | Loan sells at `101.35` | `$5,400` |
| Servicing right value | `0.35 points` | `$1,400` |
| Loan-level fees | Flat dummy amount | `$700` |
| Net warehouse / carry | Slightly negative | `-$100` |
| **Total value** |  | **`$7,400`** |

Secondary market premium math:

```text
101.35% x $400,000 = $405,400
$405,400 - $400,000 = $5,400
```

Servicing value math:

```text
0.35% x $400,000 = $1,400
```

### Costs / Value Given Up

| Item | Dummy Assumption | Dollar Cost |
|---|---:|---:|
| Broker compensation paid by lender | `1.15 points` | `$4,600` |
| Borrower credit | `0.25 points` | `$1,000` |
| Fulfillment / operations cost | Messier file | `$2,100` |
| Hedge / lock leakage | Extension and market movement | `$700` |
| Expected defect / repurchase reserve | More uncertainty | `$300` |
| **Total cost** |  | **`$8,700`** |

### Net Result

```text
Total value: $7,400
- total cost: $8,700
= net transaction profit: -$1,300
```

Margin in basis points:

```text
-$1,300 / $400,000 = -0.325%
-0.325% = -32.5 bps
```

### Common-Sense Explanation

The lender made less money, and in this dummy case lost money, because:

```text
The sale premium was lower.
The servicing right was worth less.
The lender paid more to win the loan.
The borrower credit consumed economics.
The file cost more to process.
The lock leaked more value.
The risk reserve was higher.
```

This kind of transaction might still happen if the lender cares about volume, broker relationship, market share, pull-through, or keeping its platform busy.

But one thin or negative loan only makes sense if the whole book of business works.

## The Core Lesson From Both Examples

The difference between higher-profit and lower-profit transactions is not mysterious.

It is this:

```text
Higher-profit loan:
More market value + servicing value + clean execution
relative to broker comp + credits + costs + risk.

Lower-profit loan:
Less market value + less servicing value + more concessions
relative to broker comp + credits + costs + risk.
```

The wholesale lender is constantly deciding how much economics to keep and how much to spend to win the loan.

