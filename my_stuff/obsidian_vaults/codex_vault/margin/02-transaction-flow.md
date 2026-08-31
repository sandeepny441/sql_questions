# 02. Transaction Flow

This file walks through the life of one dummy wholesale mortgage transaction.

Assume:

```text
Loan amount: $400,000
Borrower: wants a conventional mortgage
Broker: shops wholesale lenders
Wholesale lender: funds the loan
Investor / market: ultimately buys or finances the mortgage asset
```

## Step 1: The Wholesale Lender Publishes Pricing

The wholesale lender gives brokers a rate sheet.

That rate sheet says, in effect:

```text
For this borrower, this loan type, this lock period, and this rate,
here is the price.
```

The price determines whether the lender can:

```text
Pay broker compensation
Offer a borrower credit
Charge discount points
Keep a margin
Still sell the loan profitably
```

## Step 2: The Broker Chooses a Lender

The broker compares wholesale lenders.

The broker cares about:

```text
Rate
Borrower cost
Compensation
Turn time
Underwriting reliability
Ability to close
Product fit
```

The wholesale lender wants to win the broker's loan without overpaying for it.

That is the competitive tension.

## Step 3: The Rate Is Locked

Once the borrower locks a rate, the wholesale lender has a pipeline commitment.

The lender now has market risk:

```text
If rates move before closing, the value of the future loan changes.
```

The lender hedges that risk, but hedging is not perfect.

## Step 4: The Loan Is Underwritten and Closed

The lender verifies income, assets, appraisal, credit, property, eligibility, documentation, and compliance.

Some loans are clean:

```text
Low touches
Fast approval
Few conditions
Easy closing
Low cost
```

Some loans are messy:

```text
Many conditions
Multiple resubmissions
Lock extensions
Manual reviews
Higher cost
More defect risk
```

This matters because the sale price might be similar, but the cost to manufacture the loan can be very different.

## Step 5: The Lender Funds the Loan

At closing, the lender provides the money.

In simplified form:

```text
Lender funds $400,000
Borrower gets mortgage debt
Seller or payoff parties receive funds
Lender now owns a $400,000 mortgage asset
```

The lender may use warehouse lines or other funding sources. That creates short-term funding cost.

## Step 6: The Lender Sells or Securitizes the Loan

The lender does not usually want to hold every mortgage forever on its own balance sheet.

It typically monetizes the loan by selling it, pooling it, securitizing it, or otherwise moving it into the capital markets.

If the market price is `101.50`, then the loan has a value of:

```text
101.50% x $400,000 = $406,000
```

That is a `$6,000` premium above the `$400,000` principal.

But that is not profit yet. The lender still has to subtract broker comp, credits, costs, hedging, and risk.

## Step 7: Servicing Is Retained or Sold

The servicing right can be:

```text
Retained by the lender
Sold to another servicer
Subserviced by someone else
Valued as an asset
```

If the servicing right is valued at `0.60 points`, that means:

```text
0.60% x $400,000 = $2,400
```

That servicing value can be a major part of the total transaction economics.

## Step 8: The Lender Computes the Transaction Economics

Now the lender asks:

```text
What did we get?
What did we give away?
What did it cost?
What risks remain?
```

The answer might be a healthy gain. It might be thin. It might even be a loss if the lender priced aggressively, the file was expensive, or the market moved against the pipeline.

## The Key Mental Picture

The wholesale lender is like a factory plus a trading desk plus a servicing platform.

It manufactures loans, prices them against the capital markets, compensates distribution partners, manages lock risk, and either keeps or sells servicing value.

Profit is not one line. It is the residue after all those pieces net against each other.

