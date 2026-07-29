# Loan Delivery and Pooling

How lenders deliver loans to Fannie Mae for purchase.

## Delivery Execution Options
- **Cash Window (Whole Loan)**: Fannie Mae buys individual loans for cash. Common for smaller lenders.
- **MBS Swap**: Lender delivers pool of loans, receives Fannie Mae MBS in exchange, then sells MBS in market.

## Delivery Data
- Delivered via **Loan Delivery** application.
- **Uniform Loan Delivery Dataset (ULDD)**: Standardized data format (MISMO).
- Requires Loan-Level Price Adjustments (LLPAs) calculated.

## MBS Pooling
- Loans grouped into pools by note rate, product, term.
- Pool must meet minimum size ($1M typical).
- **TBA-eligible** pools follow SIFMA "good delivery" standards.
- Note rate must fit within allowable **coupon** range (net rate = note rate − guaranty fee − servicing fee).

## Settlement
- Pool issuance date and settlement per PSA calendar.
- Fannie Mae guarantees timely P&I to MBS investors.

## Related
- [[19_Pricing_and_LLPAs]]
