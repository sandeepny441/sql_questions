# Data and Modeling Approaches for EPO

## Modeling Techniques
- **Logistic regression / GLM**: EPO ~ 1 if payoff within window, 0 otherwise. Predictors: SATO, FICO, LTV, purpose, channel, etc.
- **Survival / hazard models (Cox PH)**: Time-to-payoff as continuous outcome; hazard function conditioned on covariates.
- **Gradient boosted trees (XGBoost, LightGBM)**: Handle nonlinearities and interactions (e.g., high FICO × high SATO × broker channel).
- **Deep learning**: Some large aggregators use neural nets on rich feature sets.

## Standard Feature Set
Combining everything from prior notes:
- Loan: rate, SATO, product, purpose, size, LTV, points, term.
- Borrower: FICO, DTI, income, occupancy, sophistication proxies, geography, prior refis.
- Origination: LO NMLS, channel, lender, seller EPO history.
- Environment: rates at origination, current rates, HPI trend.

## Data Sources
- **Internal historical purchases**: Own EPO outcomes across years.
- **GSE loan-level data**: Fannie / Freddie public datasets (great for prepay modeling).
- **Recursion, RiskSpan, Andrew Davidson**: prepay models.
- **Credit bureau tri-merge and monitoring feeds**.
- **Rate/pricing engines** (Optimal Blue, Polly, LenderPrice).

## Model Outputs
- **EPO probability at 3, 6, 9, 12 months** per loan.
- **Expected loss** = premium paid × EPO probability × haircut factor.
- **Loan-level bid adjustment**.

## Validation
- Backtesting on out-of-sample vintages.
- Rate-shock robustness (does model predict well in falling-rate cycles?).
- Segment-level fit checks (FHA/VA vs. conventional).

## Related
- [[24_Investor_Screening_Methods]]
- [[21_Lender_EPO_History]]
- [[11_Borrower_Sophistication_and_History]]
