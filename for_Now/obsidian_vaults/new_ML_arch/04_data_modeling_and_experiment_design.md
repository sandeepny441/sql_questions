# Data, Modeling, and Experiment Design

## Purpose

The pricing strategy requires reliable probability curves, incremental treatment estimates, and clear guardrails. This document describes the data and statistical foundation needed to produce them.

## Unit of analysis

The data should include every eligible pricing opportunity, including opportunities that did not lock.

Useful observation grains include:

- **Opportunity level:** One row per quote, pricing impression, or loan opportunity
- **LO-week level:** One row per LO per week for engagement and churn modeling
- **LO-month level:** One row per LO per month for longer-term relationship monitoring

Only using funded loans creates **selection bias** because the model never sees the opportunities that were lost.

## Core data structure

| Data group | Example variables | Modeling purpose |
|---|---|---|
| Identifiers | LO, broker, opportunity, timestamp | Join observations and measure history |
| Pricing | Base price, margin, concession, BPS treatment | Measure price exposure |
| LO profile | Volume, pull-through, tenure, wallet share | Estimate relationship strength |
| Loan profile | FICO, LTV, DTI, product, purpose, amount | Control for opportunity difficulty |
| Market | Benchmark rates, spread, competition | Control for external price pressure |
| Engagement | Searches, submissions, calls, tool usage | Detect intent and relationship change |
| Outcomes | Lock, fund, fallout, churn, reactivation | Create labels |
| Experiment | Treatment level and assignment probability | Estimate causal uplift |

## Feature engineering

The model should use behavior as it existed at the decision time.

Examples include:

- Rolling 30-, 90-, and 365-day production
- Exponentially weighted activity score
- Change in wallet share
- Change in pull-through rate
- Days since last quote, submission, lock, and funding
- Historical response to concessions
- Average competitor spread
- Rate-shop frequency
- Concession-request frequency
- Interaction between price adjustment and activity segment

An **exponentially weighted feature** gives more importance to recent activity while still retaining older information.

## Labels

Labels must be precise and operationally meaningful:

- `close_7d`: Current opportunity closes within seven days
- `fund_60d`: Locked opportunity funds within 60 days
- `churn_90d`: Previously active LO has no meaningful activity during the next 90 days
- `reactivate_30d`: Dormant LO submits or locks within 30 days
- `repeat_90d`: Reactivated LO produces a second lock within 90 days

Changing label definitions after model development creates inconsistent measurement. Definitions should be approved before training.

## Recommended model ladder

### Stage 1: Interpretable baseline

Start with:

- Logistic regression
- Regularized regression such as LASSO or ridge
- Generalized additive models

These methods provide interpretable coefficients and a defensible baseline.

### Stage 2: Nonlinear challenger

Evaluate:

- Gradient-boosted trees
- Monotonic gradient boosting
- Random forests
- Survival models

These models can capture nonlinear response and interactions.

### Stage 3: Causal treatment models

Add:

- Uplift trees
- Causal forests
- Doubly robust learners
- Propensity-score weighting
- Meta-learners such as S-learners, T-learners, and X-learners

These methods estimate heterogeneous incremental effects.

### Stage 4: Sparse-LO treatment

For LOs with limited history, use:

- Hierarchical regression
- Mixed-effects models
- Bayesian partial pooling
- Segment-level shrinkage

**Shrinkage** prevents a small number of observations from creating an extreme individual recommendation.

## Experiment design

Historical pricing is usually confounded because concessions are often given to opportunities already believed to be at risk.

A controlled experiment should:

1. Define approved BPS corridors.
2. Stratify by activity, product, market, and baseline competitiveness.
3. Randomize at an appropriate level, such as broker-week or LO-week.
4. Maintain a control group.
5. Log every assigned treatment and its probability.
6. Measure both immediate and longer-term outcomes.
7. Stop or narrow treatment when guardrails are breached.

Cluster-level randomization can reduce the chance that one broker organization receives inconsistent simultaneous pricing treatments.

## Statistical power

Before launching an experiment, estimate the sample size required to detect a commercially meaningful change.

Key concepts include:

- **Minimum detectable effect:** Smallest uplift worth acting on
- **Statistical power:** Probability of detecting a real effect
- **Type I error:** Concluding that an effect exists when it does not
- **Type II error:** Missing a real effect
- **Confidence interval:** Uncertainty around the estimated treatment effect

Large sample size alone does not make an effect economically important. Statistical significance and business significance should both be reported.

## Model validation

### Probability models

- AUC / ROC
- Precision and recall
- Log loss
- Brier score
- Calibration curve
- Out-of-time validation
- Segment-level residual analysis

### Uplift models

- Qini coefficient
- Area under the uplift curve
- Incremental gain by treatment decile
- Off-policy policy-value estimate
- Treatment-effect calibration

### Business validation

- Incremental funded volume
- Incremental contribution
- Margin retained
- Churn prevented
- Cost per incremental lock

## Confidence-aware recommendations

The system should not treat every estimate as equally reliable.

Recommendations can be reduced or suppressed when:

- The LO has limited history
- The treatment is outside the observed pricing range
- Model confidence is low
- The segment is experiencing data drift
- The predicted improvement is economically immaterial

This is sometimes called a **conservative policy** or **lower-confidence-bound optimization**.

## Monitoring

Production monitoring should include:

- Feature drift
- Prediction drift
- Calibration drift
- Treatment distribution
- Approval-corridor violations
- Churn and conversion by model score
- Incremental policy value
- Data latency and missingness

A **champion-challenger** framework allows the current model and a proposed replacement to run side by side before promotion.

## Governance boundary

Protected characteristics should not be pricing-model features. Any legally permitted monitoring data should remain separated and be used only through an approved compliance process.

All production decisions should retain:

- Model version
- Input snapshot
- Recommended action
- Final applied action
- Reason codes
- Guardrail checks
- Override and approver

## Leadership takeaway

The credibility of the recommendation comes from three things:

> Complete opportunity data, controlled treatment variation, and calibrated models that distinguish correlation from incremental impact.

