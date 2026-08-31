# 01. Common-Sense Map

## The Basic Cast

In a UWM-like wholesale setup, the borrower usually does not walk into the lender's retail branch. The borrower works with an independent mortgage broker.

The broker helps the borrower shop for a loan. The wholesale lender supplies the rate sheet, underwriting, funding, closing infrastructure, and access to the capital markets.

So the simple picture is:

```text
Borrower -> Broker -> Wholesale Lender -> Investor / MBS Market
                         |
                         v
                    Servicing Asset
```

The wholesale lender is not just "charging an interest rate." It is manufacturing a mortgage asset and then monetizing that asset.

## The Product Is Not Just the Loan

The borrower thinks they are buying a mortgage:

```text
"I need $400,000 at a rate and payment I can live with."
```

The wholesale lender thinks in a few pieces:

```text
"If I fund this $400,000 loan, what can I sell it for?"
"What is the servicing right worth?"
"How much did I have to give away to win it?"
"How much did it cost me to process, fund, hedge, and close?"
"What risks am I keeping?"
```

That is the core shift.

The borrower's mortgage becomes an asset that can be sold, securitized, serviced, or used to create future cash flows.

## The Main Money Buckets

A wholesale lender can make money from several places.

### 1. Secondary Market Premium

If the lender funds a `$400,000` loan and the market values that loan at `101.50`, the loan is worth `101.50%` of par.

That means:

```text
101.50% x $400,000 = $406,000
```

The premium over par is:

```text
$406,000 - $400,000 = $6,000
```

That `$6,000` is a major source of transaction economics.

### 2. Servicing Value

After a mortgage is made, someone has to collect payments, send statements, manage escrow, handle payoff requests, and deal with delinquencies.

The right to service the loan can be valuable because the servicer may receive a small strip of cash flow over time.

So a loan may create value in two ways:

```text
Value of the loan itself
+ value of the right to service the loan
```

### 3. Fees

There may be underwriting, processing, admin, or other loan-level fees. In the real world, which fees exist and who pays them depends on the product, channel, regulations, and pricing setup.

For learning purposes, treat fees as a small extra revenue bucket.

### 4. Net Interest / Carry

The lender may temporarily own the loan before selling it. During that time, it may earn some interest but also pay warehouse funding costs.

Sometimes this is positive. Sometimes it is negative. It is usually not the main driver in the simplified transaction model.

## The Main Money Drains

### 1. Broker Compensation

In wholesale, the broker has to get paid. If the lender pays the broker, that compensation is economically part of the transaction's cost.

Even when the borrower does not write a separate check to the broker, the money has to come from somewhere. Usually it is embedded in the pricing.

### 2. Borrower Credits

The lender might give the borrower a credit to help cover closing costs.

That can win the loan, but it reduces the lender's economics.

### 3. Operational Cost

The lender must pay people, systems, underwriting, quality control, closing operations, compliance, support, and technology.

A clean, automated file is cheaper. A messy file is more expensive.

### 4. Hedge / Lock Cost

When a lender locks a rate, the market can move before the loan closes and sells.

The lender usually hedges this pipeline. But hedging is imperfect. Fallout, extensions, renegotiations, pair-offs, and market movement can cost money.

### 5. Credit, Defect, and Repurchase Risk

If the loan has a defect, early payment default, fraud issue, documentation problem, or investor challenge, the lender may have to pay fees, indemnify, or even repurchase the loan.

The expected value of that risk belongs in the economics.

## The Simple Profit Story

The easiest mental model:

```text
What the loan is worth to the market
+ what the servicing is worth
+ fees and small income
- broker comp
- borrower credits
- operating cost
- hedge/funding leakage
- expected defect/repurchase risk
= transaction profit
```

This is why two loans with the same principal balance can have very different profitability.

The lender does not simply make money because the borrower pays interest. The lender makes money because the funded loan has a market value, and the lender tries to create that value for less than it costs to originate the loan.

