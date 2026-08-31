# Pricing, Margin, and Conversion

Pricing is not simply “raise price” or “lower price.” The useful problem is finding the margin that maximizes expected contribution after conversion, fallout, hedge cost, and credit risk.

| Knob | ML approach | Decision / action | Primary profit metric | Guardrail |
|---|---|---|---|---|
| Base rate-sheet margin | Hierarchical price-elasticity model | Set product/channel/day margin within approved bands | Contribution bps per lock | Published, auditable rules; disparity testing |
| Product-level margin | Elasticity + constrained optimization | Shift margin by product where competition and execution differ | Profit per eligible scenario | Do not use protected traits or proxies |
| Broker-specific concessions | Causal uplift model | Approve only concessions likely to change funding outcome | Incremental profit per concession bp | Policy limits and consistent exception reasons |
| Lock extension pricing | Survival / hazard model | Offer extension terms based on close probability and hedge cost | Net extension recovery | No borrower willingness-to-pay targeting |
| Relock policy | Classification + expected-value model | Select fee, original market, or worse-of treatment permitted by policy | Relock contribution | Uniform policy and auditable exceptions |
| Float-down option | Option-value simulation | Price float-down protection to cover expected cost | Option premium less exercise cost | Clear disclosures and consistent eligibility |
| Lock period | Time-to-close model | Recommend shortest realistic lock period | Lock cost and pull-through | Preserve borrower choice |
| Product recommendation | Eligibility rules + learning-to-rank | Rank eligible products by borrower fit and lender economics | Expected contribution per scenario | Suitability, steering, and fair-lending review |
| Discount points / credits | Constrained scenario optimizer | Show compliant rate/point combinations | Profit across selected coupon | Transparent comparison; no dark patterns |
| Price exception routing | Anomaly detection + approval model | Auto-approve low-risk cases; escalate unusual requests | Exception leakage and cycle time | Human review, reason codes, broker parity |
| Competitive response | Market-regime model | Adjust approved margin bands when competitive position changes | Lock share at target margin | No coordination or use of improper competitor data |
| Minimum profitability floor | Expected-value model | Block or escalate loans below a risk-adjusted threshold | Loss avoidance | Explainable components and override governance |

## Best modeling pattern

Estimate three quantities separately:

1. Probability the broker locks at a given price.
2. Probability the lock funds by expected closing date.
3. Contribution if funded and expected cost if it falls out.

Then choose among **pre-approved price actions**. A causal experiment is needed to estimate true price response; historical concessions are biased because they were given to harder-to-win loans.

## Safer wholesale personalization

Prefer product-, market-, time-, and channel-level optimization plus governed broker exception policies. Avoid borrower-specific “maximum price tolerance” models. They create significant fair-lending, UDAAP, explainability, and reputational risk.

## Experiment

Randomize a small, policy-approved margin difference across comparable broker-product cells. Measure funded contribution, not lock count. Monitor approval, exception, fallout, and price outcomes by prohibited-basis proxy groups before expansion.

## Regulatory anchors

- [CFPB loan originator rule](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/loan-origination-rule/)
- [DOJ fair lending enforcement](https://www.justice.gov/crt/fair-lending-enforcement)
- [FHFA guarantee fees](https://www.fhfa.gov/policy/guarantee-fees)

