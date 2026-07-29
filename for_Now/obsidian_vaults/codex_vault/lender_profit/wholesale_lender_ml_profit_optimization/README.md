# Wholesale Lender ML Profit Optimization

This folder maps the practical decisions a wholesale mortgage lender can optimize with machine learning. The central idea is to optimize **risk-adjusted contribution profit**, not volume, approval rate, or conversion in isolation.

## Core objective

```text
Expected contribution per lock
= P(fund)
 x (gain on sale + lender fees + SRP/MSR value)
- acquisition and fulfillment cost
- hedge and fallout cost
- warehouse and capital cost
- expected defect, EPO, indemnification, and repurchase loss
```

The best operating metric is usually **expected contribution bps per lock**, supported by dollars per application and dollars per funded loan.

## Who has the knobs?

| Owner | Most useful knobs | Important caution |
|---|---|---|
| Lender | Rate-sheet margin, concessions, execution, staffing, workflow, QC, servicing strategy | This is where the lender has the greatest direct control. |
| Broker / loan officer | Product fit, submission quality, responsiveness, lock timing, borrower communication | In wholesale, the broker is the lender's primary channel customer. |
| Borrower | Documentation speed, product selection, lock decision, closing readiness | Do not optimize borrower pricing by inferred willingness to pay. Test fair-lending outcomes. |
| Capital markets | Hedge coverage, pooling, investor allocation, best execution, servicing release | Profit can move materially after the loan is locked. |
| Operations / credit | Queue priority, touch count, conditions, exception handling, QC sample | Faster is valuable only when quality and risk remain controlled. |

## Playbook

1. [[01-pricing-margin-conversion]]
2. [[02-broker-loan-officer-channel]]
3. [[03-borrower-conversion-retention]]
4. [[04-capital-markets-hedging-execution]]
5. [[05-operations-cycle-time-cost]]
6. [[06-credit-quality-repurchase-risk]]
7. [[07-servicing-msr-recapture]]
8. [[08-model-catalog-data-design]]
9. [[09-experimentation-governance-compliance]]
10. [[10-prioritized-roadmap]]

## Highest-value starting points

| Priority | Use case | Why it often wins first |
|---:|---|---|
| 1 | Lock pull-through and fallout | Directly connects pricing, operations, hedge cost, and conversion. |
| 2 | Broker risk-adjusted profitability | Reveals where volume is economically misleading. |
| 3 | Turn-time and bottleneck prediction | Converts service speed into funded-loan economics. |
| 4 | Defect and repurchase triage | Prevents large tail losses and avoidable rework. |
| 5 | Investor best execution | Captures value on every eligible funded loan. |

Not every lever applies to every lender. Agency eligibility, state law, investor agreements, warehouse facilities, compensation plans, and servicing strategy determine the available action set.

