# Borrower Conversion and Retention

Borrower analytics should remove friction and improve product fit. In wholesale, actions are often delivered through the broker, and credit or pricing decisions require strong fair-lending and adverse-action controls.

| Knob | ML approach | Decision / action | Metric | Guardrail |
|---|---|---|---|---|
| Application completion | Funnel / survival model | Send timely document or milestone reminders through permitted channel | Completed applications | Consent, privacy, equal service |
| Document readiness | Missing-item prediction | Generate a tailored, rule-validated checklist | Days and touches to complete | Never invent requirements |
| Closing-date risk | Time-to-event model | Escalate dependencies likely to miss closing | On-time close and extension cost | Actionable reasons |
| Product fit | Eligibility engine + ranking | Present compliant eligible options and trade-offs | Selection and funded contribution | No steering to lender-profit-only option |
| Rate-lock timing support | Scenario simulation | Explain lock-period cost and timing risk | Pull-through and extension cost | Borrower retains decision |
| Churn / shopping risk | Propensity + uplift model | Trigger service recovery or broker outreach | Incremental retained contribution | Avoid individualized price exploitation |
| Communication channel | Contextual response model | Use preferred lawful channel and timing | Response time | Consent and frequency caps |
| Condition resolution | Next-best-action model | Prioritize the clearest resolvable condition | Cycle time | Underwriter retains credit authority |
| Early payoff risk | Survival model | Forecast portfolio economics and recapture opportunity | EPO / MSR value | Do not impair right to prepay |
| Refinance recapture | Uplift model | Contact borrowers likely to benefit and respond | Incremental retained servicing / origination value | Licensing, consent, suitability, fair lending |
| Complaint prevention | NLP classification | Route emerging service issues before escalation | Complaint and fallout reduction | Human review; do not suppress complaints |

## Borrower features to restrict

Exclude protected characteristics from production decisioning. Also review geography, language, name-derived signals, education, device, browsing behavior, and other variables that can act as proxies. Even a feature that improves accuracy may be inappropriate if it creates unjustified disparities or cannot support required reasons.

## Appropriate objective

Use borrower models to maximize the probability of a **suitable, compliant, on-time funded loan** while reducing borrower effort. Do not optimize “willingness to pay,” discouragement, or selective service based on expected profitability.

## Regulatory anchors

- [CFPB AI adverse-action circular](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/)
- [Federal agencies on automated systems and discrimination](https://files.consumerfinance.gov/f/documents/cfpb_joint-statement-enforcement-against-discrimination-bias-automated-systems_2023-04.pdf)
- [DOJ fair lending enforcement](https://www.justice.gov/crt/fair-lending-enforcement)

