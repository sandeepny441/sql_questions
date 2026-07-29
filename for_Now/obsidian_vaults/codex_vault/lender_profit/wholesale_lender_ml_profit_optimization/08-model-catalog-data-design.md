# Model Catalog and Data Design

## Match the algorithm to the decision

| Problem | Good starting method | Upgrade when justified |
|---|---|---|
| Fund / fallout probability | Calibrated logistic regression or gradient boosting | Hierarchical model by broker and product |
| Time to close / payoff / default | Survival analysis | Competing-risks or time-varying survival model |
| Price response | Randomized-test elasticity model | Hierarchical causal model |
| Who benefits from an intervention | Uplift / causal forest | Doubly robust heterogeneous-treatment model |
| Queue order / product rank | Rules plus learning-to-rank | Constrained contextual bandit after experiments |
| Best execution / staffing / warehouse use | Linear or mixed-integer optimization | Stochastic optimization under scenarios |
| Missing documents / conditions | Multi-label classifier | Document model with human-verified extraction |
| Defect / fraud triage | Gradient boosting + anomaly detection | Graph analytics for relationship patterns |
| Broker segmentation | Transparent business rules or clustering | Dynamic lifecycle / hidden-state model |
| Market and volume forecast | Baseline time series + calendar effects | Regime-aware ensemble |
| Complaint and condition text | Controlled taxonomy + NLP classifier | Retrieval-assisted reviewer workflow |

Start with interpretable baselines. Deep learning is useful only when unstructured documents, images, text, or very large behavioral datasets justify the additional governance burden.

## Minimum data model

| Domain | Required fields |
|---|---|
| Application | Application, borrower, broker, LO, product, purpose, geography, timestamps |
| Pricing | Every quote, lock, extension, relock, concession, rule version, approver, reason |
| Eligibility | AUS result, product rules, agency / investor eligibility, effective dates |
| Operations | Milestones, queue entries, touches, conditions, owners, vendor events, SLA |
| Capital markets | Market snapshots, hedge positions, pair-offs, investor bids, delivery results |
| Accounting | Revenue and cost at application, lock, funded loan, broker, and product levels |
| Quality | QC sample basis, findings, severity, taxonomy, cure, repurchase, indemnification |
| Servicing | Retain/release, SRP, EPO, payoff, delinquency, cost, recapture outcome |
| Experiments | Eligibility, treatment, control, assignment time, exposure, outcome |

## Critical design rules

1. Preserve the data and policy version visible **at the decision timestamp**.
2. Use an immutable loan event history rather than only the latest status.
3. Separate predictions, recommendations, human actions, and realized outcomes.
4. Allocate fulfillment, capital-markets, quality, and servicing costs to the loan level.
5. Record every override with actor, reason, old value, new value, and timestamp.
6. Maintain protected-class data separately for authorized fair-lending testing, not production targeting.
7. Prevent leakage: post-decision events cannot train a model as if known earlier.

## Model evaluation

Accuracy alone is insufficient. Track calibration, profit lift, stability, subgroup outcomes, reason fidelity, override rate, operational adoption, and realized-vs-expected economics. Validate using out-of-time samples and different rate regimes.

