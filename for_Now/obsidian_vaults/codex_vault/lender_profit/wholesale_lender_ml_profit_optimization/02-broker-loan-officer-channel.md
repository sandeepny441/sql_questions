# Broker and Loan Officer Channel

For a wholesale lender, the broker or loan officer is usually the primary relationship to optimize. Rank relationships by **incremental, risk-adjusted lifetime contribution**, not raw funded volume.

| Knob | ML approach | Decision / action | Metric | Guardrail |
|---|---|---|---|---|
| Broker acquisition | Lookalike / value model | Prioritize brokers resembling profitable, compliant partners | 12-month contribution after acquisition cost | RESPA review of anything of value |
| Broker activation | Uplift model | Select onboarding, training, or service treatment | Incremental first-lock and first-fund profit | Treatments must be legitimate services |
| Dormant broker reactivation | Survival + uplift model | Contact brokers whose volume is recoverable | Incremental contribution after outreach cost | Contact and privacy controls |
| Share of wallet | Latent-demand model | Identify products and geographies where lender is underused | Incremental profitable submissions | Avoid pressure to steer borrowers |
| Account executive coverage | Portfolio optimization | Assign AE time by incremental opportunity and service need | Contribution per AE hour | Do not abandon smaller protected-market brokers |
| Lead / broker routing | Matching model | Match broker to AE, underwriter, or specialty desk | Conversion and resolution time | Capacity and fairness monitoring |
| Broker tiering | Clustering + expected value | Tailor service level to economics and complexity | Net contribution by tier | Publish objective criteria; periodic review |
| Training recommendation | Next-best-action model | Recommend product, process, or submission-quality training | Defect and touch reduction | Training, not inducement |
| Submission quality | Defect prediction | Prompt broker for likely missing or inconsistent items | First-pass completeness | Do not discourage valid applications |
| Pull-through coaching | Explainable classification | Show broker-specific fallout drivers and remedies | Funded / locked ratio | Use actionable reasons, not opaque score alone |
| Product affinity | Learning-to-rank | Surface products a broker can successfully originate | Profitable product adoption | Eligibility and borrower suitability first |
| Concession discipline | Uplift + anomaly detection | Identify concessions that do not change behavior | Bps saved without lost funds | Consistent policy and exception review |
| Broker fraud / quality risk | Graph analytics + anomaly detection | Increase review, suspend, or investigate based on evidence | Avoided loss | Human investigation before adverse action |
| Broker lifetime value | Survival + discounted cash flow | Set relationship investment and retention priority | Risk-adjusted broker LTV | Include quality, EPO, defects, and service cost |

## Broker scorecard

A useful broker scorecard combines:

```text
Funded contribution
- concessions
- fulfillment and exception cost
- hedge fallout cost
- expected EPO / repurchase / indemnification loss
- AE and support cost
```

Also display pull-through, cycle time, first-pass completeness, defect rate, product mix, concentration, and trend. Keep predicted value separate from observed facts.

## What not to reward

- Raw volume without margin and quality.
- Referral volume purchased through marketing or service arrangements.
- A low denial rate achieved through discouraging applications.
- Short-term production that creates EPO, defect, or repurchase losses.

## Experiment

Within comparable brokers, randomize a genuine treatment such as specialized training, proactive scenario support, or faster status communication. Use uplift modeling to learn who benefits; compare incremental funded contribution after service cost.

## Regulatory anchors

- [CFPB RESPA FAQs](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/real-estate-settlement-procedures-act/real-estate-settlement-procedures-act-faqs/)
- [CFPB digital mortgage comparison-shopping advisory](https://www.consumerfinance.gov/rules-policy/final-rules/real-estate-settlement-procedures-act-regulation-x-digital-mortgage-comparison-shopping-platforms-and-related-payments-to-operators/)
- [DOJ wholesale fair-lending case materials](https://www.justice.gov/crt/housing-and-civil-enforcement-cases-documents-316)

