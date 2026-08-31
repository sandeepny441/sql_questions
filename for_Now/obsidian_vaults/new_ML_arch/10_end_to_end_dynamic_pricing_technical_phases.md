# Dynamic Pricing Approach — Technical Phase Guide

> **Coefficient principle:** Model coefficients are data-driven estimates, not permanent business rules. Their sign and size summarize observed relationships. They should be monitored, challenged, and re-estimated when new pricing and performance outcomes become available.

## Phase 1 — Segmentation and Objective Design

- **Cohort segmentation:** Divide loan officers into active and inactive populations using consistent production rules.
- **Observation window:** Use a defined historical period, such as the previous six or twelve months.
- **Behavioral threshold:** Set the funded-loan level that separates active, low-active, and dormant loan officers.
- **Objective function:** Define whether the decision should maximize expected margin, expected volume, or relationship value.
- **Pricing treatment:** Represent each approved margin increase or discount as a basis-point treatment.
- **Risk constraints:** Set maximum churn, closing-probability, EPO, and profitability limits.
- **Policy design:** Create different pricing rules for active and inactive cohorts.

## Phase 2 — Data Preparation and Feature Engineering

- **Analytical grain:** Build records at the loan, opportunity, loan-officer-week, or loan-officer-month level.
- **Feature engineering:** Convert raw pricing, activity, market, and operational data into model-ready variables.
- **Temporal joins:** Ensure every feature uses only information available before the pricing decision.
- **Missing-value treatment:** Apply consistent rules for incomplete or unavailable observations.
- **Outlier treatment:** Cap or review unusually large margins, volumes, concessions, and loan values.
- **EPO aggregation:** Calculate broker-level and loan-officer-level early-payoff risk measures.
- **Feature mart:** Store the final variables in one governed analytical dataset.

## Phase 3 — Correlation and Coefficient Analysis

- **Correlation matrix:** Measure the direction and strength of historical relationships between features and outcomes.
- **Regression coefficients:** Estimate how each feature is associated with closing, churn, or reactivation while holding other factors constant.
- **Coefficient sign:** Use positive and negative signs to show whether a factor increases or decreases the predicted outcome.
- **Coefficient magnitude:** Use the size of the coefficient to compare the relative impact of different variables.
- **Statistical significance:** Review confidence intervals and uncertainty before treating a relationship as dependable.
- **Multicollinearity testing:** Identify overlapping variables that may make coefficients unstable or misleading.
- **Coefficient governance:** Re-estimate coefficients as observed results change instead of treating them as fixed conclusions.

## Phase 4 — Active-LO Margin and Churn Modeling

- **Closing-probability model:** Estimate the likelihood of closing at every approved margin adjustment.
- **Price-elasticity curve:** Measure how closing probability changes when lender margin increases.
- **Marginal BPS effect:** Calculate the expected probability change from each additional basis-point step.
- **Churn model:** Predict whether an active loan officer will materially reduce future business.
- **Survival analysis:** Estimate when relationship churn may occur, not only whether it occurs.
- **Probability calibration:** Confirm that predicted risks match observed closing and churn rates.
- **Constrained optimization:** Select the highest safe margin while keeping churn below the approved threshold.

## Phase 5 — Dormant-LO Reactivation Modeling

- **Uplift modeling:** Estimate which loan officers will respond because of a discount rather than without one.
- **Treatment and control:** Compare discounted offers with similar opportunities that did not receive the offer.
- **Incremental response:** Measure the additional lock probability caused by each incentive.
- **Dose-response curve:** Estimate how reactivation changes across increasing discount levels.
- **Diminishing marginal lift:** Identify when deeper discounts create little additional response.
- **Minimum effective discount:** Choose the smallest incentive that reaches the target probability or lift.
- **Holdout validation:** Keep a comparison group to confirm that the measured lift is real.

## Phase 6 — Decision Engine and Pricing Optimization

- **Expected-value calculation:** Combine close probability, margin, loan value, churn cost, and EPO risk.
- **Risk-adjusted margin:** Reduce the expected benefit when churn or early-payoff risk is high.
- **Decision corridor:** Restrict recommendations to approved basis-point ranges.
- **Optimization rule:** Select the action with the best expected value that satisfies every guardrail.
- **Model explainability:** Show the main factors and coefficients supporting each recommendation.
- **SHAP values:** Provide a loan-officer-level view of which variables increased or decreased the prediction.
- **Human-in-the-loop review:** Allow authorized users to review, approve, or override model recommendations.

## Phase 7 — Experimentation, Monitoring, and Recalibration

- **Controlled pilot:** Test the strategy on a limited population before wider deployment.
- **A/B testing:** Compare model-guided pricing with the current pricing approach.
- **Outcome monitoring:** Track locks, closings, margin, volume, churn, reactivation, and EPO performance.
- **Calibration monitoring:** Compare predicted probabilities with actual observed rates.
- **Data and concept drift:** Detect changes in borrower, broker, market, and pricing behavior.
- **Coefficient recalibration:** Update coefficient estimates when new observations show that relationships have changed.
- **Model governance:** Document versions, approvals, thresholds, overrides, and performance reviews.

## How Leadership Should Read the Coefficients

- A coefficient is a summary of what the historical data currently indicates.
- A positive coefficient means the modeled outcome tends to increase as the feature increases.
- A negative coefficient means the modeled outcome tends to decrease as the feature increases.
- Larger coefficients may indicate stronger effects, but their scales must be comparable.
- Confidence intervals show how certain or uncertain the estimated relationship is.
- Controlled tests help separate true incremental impact from simple historical correlation.
- New observed results should be used to validate and update the coefficients over time.
