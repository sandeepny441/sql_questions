# Dynamic Pricing Approach — Phase by Phase

## Phase 1 — Define the Business Goal

- Start with the full population of approximately 50,000 loan officers.
- Separate active loan officers from inactive or dormant loan officers.
- Use recent funded-loan activity to define each group consistently.
- For active loan officers, focus on capturing more lender margin.
- For inactive loan officers, focus on winning new locks and volume.
- Use basis-point adjustments as the main pricing lever.
- Protect closing probability, relationships, and total profitability.

## Phase 2 — Bring the Data Together

- Collect historical pricing, locks, closings, and funded-loan information.
- Add loan-officer activity, production, tenure, and relationship information.
- Add loan details such as FICO, LTV, DTI, purpose, and product.
- Add market information such as wallet share and competitor activity.
- Add operational information such as concessions and lock-to-close time.
- Add broker-level and loan-officer-level EPO risk scores.
- Combine everything into one consistent analytical dataset.

## Phase 3 — Understand What Drives Behavior

- Review how every feature has historically moved with closing activity.
- Identify factors that are linked to higher or lower closing probability.
- Measure how strongly each factor is connected to the outcome.
- Check whether the relationship remains stable across different time periods.
- Compare the results for active and inactive loan officers.
- Remove repeated or unreliable information that adds little value.
- Keep a clear list of the features that will enter the models.

## Phase 4 — Protect Active Loan Officers

- Estimate closing probability at every approved margin increase.
- Show how the probability changes as additional basis points are added.
- Estimate relationship churn risk at every basis-point level.
- Keep the recommended churn risk below the agreed limit, such as 5%.
- Find the maximum margin increase that stays within the guardrails.
- Flag sensitive loan officers as “Protect” instead of stretching pricing.
- Give leadership a clear reason for every recommended margin change.

## Phase 5 — Reactivate Inactive Loan Officers

- Start with the loan officer’s current closing or engagement probability.
- Test discounts in small and controlled basis-point steps.
- Estimate the additional lift created by each discount level.
- Find the minimum discount that meaningfully improves the chance of a lock.
- Stop increasing the discount when additional lift becomes very small.
- Flag promising loan officers as “Reactivate” and others as “Hold.”
- Replace broad discounts with targeted offers that protect margin.

## Phase 6 — Make the Pricing Decision

- Use different decision rules for active and inactive loan officers.
- Recommend a safe margin stretch for active loan officers.
- Recommend a minimum effective discount for inactive loan officers.
- Include closing probability, churn risk, margin, and EPO risk.
- Keep every recommendation inside approved pricing limits.
- Show a short business explanation beside each recommendation.
- Allow authorized users to review or override unusual recommendations.

## Phase 7 — Pilot, Measure, and Improve

- Begin with a small group before using the approach across the full channel.
- Compare recommended pricing with the current pricing process.
- Track locks, closings, funded volume, margin, churn, and EPO results.
- Confirm that active loan officers remain within the churn guardrail.
- Confirm that dormant-loan-officer discounts create real additional volume.
- Review overrides, unexpected outcomes, and feedback from the business.
- Refresh the data, thresholds, and models as behavior changes.
