# 07. Post-Buyback Loan Management & Upstream Prevention Math (UWM View)

After UWM pays the Repurchase Price and takes the loan back, the story is not over. This file covers what happens next and — more importantly — the powerful math of **prevention** that makes buybacks less frequent and less severe in the first place.

## What UWM Does With a Repurchased Loan

Options, in rough order of preference for minimizing loss:

1. **Cure & Re-Sell (Best Outcome)**
   - If the defect is curable (e.g., obtain missing verification, correct data error, provide additional appraisal support), UWM cures it and sells the loan again — ideally to another investor or back to the same GSE if accepted.
   - Recovery can be close to UPB minus modest discount.
   - Requires the defect to be fixable and the loan still performing or made performing.

2. **Scratch-and-Dent Sale**
   - Sell "as-is" with known defects to specialized investors who accept higher risk for higher yield.
   - Typical pricing: 90–96 cents on the dollar depending on severity of defect, delinquency status, documentation issues, and interest rate environment.
   - Fastest liquidity but crystallizes a loss vs. UPB.

3. **Loan Modification / Reperforming Strategy**
   - If borrower has capacity but temporary issue, modify (rate, term, principal forbearance) to make payments sustainable.
   - Then sell as reperforming loan (better pricing than scratch-and-dent) or hold in portfolio.
   - Math trade-off: Modification costs vs. higher recovery value and avoided foreclosure costs.

4. **Foreclosure / Liquidation (Worst Case)**
   - If fraud, severe capacity issues, or strategic default: pursue foreclosure, REO sale, or short sale.
   - Recovery often 50–75% of UPB after all costs and delays (6–24+ months).
   - Highest loss severity.

**UWM decision framework**: Net present value of each path, considering time value, carrying costs, operational bandwidth, and recourse/insurance timing. Strong servicing or asset management capabilities (or partnerships) improve outcomes.

## The Most Important Math: Prevention ROI

Every buyback avoided is worth far more than the cost of strong upstream controls.

### Simple Prevention ROI Example

Assume:
- Average gross loss severity before mitigants: **$40,000** per buyback event (conservative; studies show ~$32k average, but can be higher).
- UWM can reduce buyback rate by investing more in fraud tools, QC sampling, broker training, and strict alert clearance.
- Cost of enhanced prevention (additional FraudGuard reviews, extra QC hours, better systems): **$150 per loan** originated.

For 100,000 loans originated per year:

**Without extra prevention**:
- Buyback rate: 0.50% of loans (500 events)
- Gross losses: 500 × $40,000 = **$20,000,000**

**With extra prevention** (reduces buyback rate to 0.35%):
- Buyback events: 350
- Gross losses: 350 × $40,000 = **$14,000,000**
- Prevention cost: 100,000 × $150 = **$15,000,000**
- **Net savings**: $20M – $14M – $15M = **$1,000,000+** (plus softer benefits: better GSE relationship, lower operational burden, stronger broker accountability)

Even if prevention only reduces events by 0.10% (100 fewer buybacks), it saves ~$4M in gross losses for $15M spend — still compelling when you factor in net severity after recourse/insurance (often 40–60% lower) and avoided process costs.

### Key Prevention Levers for UWM (Wholesale Lender)

- **FraudGuard-style tools integration** (see companion screening folder): Every identity, occupancy, employment, valuation, and relationship alert that is **properly cleared with independent evidence** prevents a future demand. Weak clearance = future loss.
- **Risk-based QC sampling**: Higher sampling or full review on files with fraud alerts, high-risk brokers, complex transactions, or EPD indicators.
- **Broker scorecards & accountability**: Track buyback rates, EPD rates, and defect rates by broker. Adjust pricing, approval authority, or terminate poor performers. Recourse collection is easier with strong relationships and data.
- **Pre-funding and pre-delivery refresh screens**: Re-run OFAC, exclusions, and key fraud checks before clear-to-close and before investor delivery (as recommended in the "When to Screen" materials).
- **Training & culture**: Underwriters and processors trained to treat fraud alerts as "resolve or escalate," not "find a way to clear."
- **Data analytics**: Use historical buyback data to identify patterns (certain loan types, geographies, broker behaviors) and adjust guidelines or pricing dynamically.

## Tying It All Together — End-to-End from UWM POV

**Upstream (Prevention)**:
Fraud tools + strict clearance + QC → fewer demands issued.

**Midstream (Process)**:
Fast, evidence-based response to demands → more cures/rebuttals, fewer repurchases.

**Downstream (Loss Realization & Recovery)**:
Pay Repurchase Price → pursue broker recourse + insurance → dispose of loan optimally (cure/re-sell > scratch-and-dent > mod > liquidation) → book net loss.

**Financial Outcome**:
Net loss severity kept as low as possible through layered mitigants. Expected loss modeling informs reserves, pricing, and capital allocation.

**Strategic Outcome**:
UWM maintains strong seller status with GSEs, favorable warehouse financing terms, predictable earnings, and the ability to grow volume profitably.

Buybacks will always exist in mortgage lending — the goal is to make them rare, containable, and well-covered. The math in this folder shows that disciplined prevention and strong recourse/insurance layers deliver excellent returns on investment for a high-volume wholesale lender like UWM.

This completes the core educational series on buybacks from end to end.

