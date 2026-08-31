# Experimentation, Governance, and Compliance

## Safe deployment ladder

1. **Historical backtest:** verify timestamps, leakage, calibration, economics, and subgroup outcomes.
2. **Shadow mode:** produce recommendations without changing decisions.
3. **Human decision support:** show prediction, reasons, uncertainty, and approved actions.
4. **Controlled test:** randomize within policy-approved boundaries.
5. **Limited automation:** automate low-risk decisions with confidence thresholds and review samples.
6. **Scale:** expand only after realized profit and control outcomes remain sound.

Do not deploy contextual bandits or reinforcement learning until the action set, reward, experiments, delayed outcomes, constraints, and shutdown mechanism are mature.

## Experiment scorecard

| Dimension | Measure |
|---|---|
| Primary | Incremental risk-adjusted contribution dollars / bps |
| Conversion | Application-to-lock, lock-to-fund, pull-through |
| Price | Margin, concession bps, borrower price, extension cost |
| Operations | Cycle time, touches, SLA, labor minutes, vendor cost |
| Quality | Defects, repurchases, indemnifications, EPO, complaints |
| Fair lending | Approval, pricing, exception, service time, fallout disparities |
| Stability | Performance by broker, product, geography, month, and rate regime |

## Required controls

- Model owner, business owner, compliance owner, and independent validator.
- Approved purpose, users, inputs, outputs, actions, limits, and prohibited uses.
- Development documentation and reproducible training data.
- Independent conceptual-soundness, process, and outcome validation.
- Drift, calibration, subgroup, override, and realized-profit monitoring.
- Versioned reason codes and evidence for credit-related decisions.
- Human appeal, correction, and shutdown paths.
- Vendor-model due diligence and ongoing monitoring.
- Audit log from source data through recommendation and final action.

## Compliance boundaries

### Fair lending

Test underwriting, pricing, concessions, turn time, service, fallout, and quality-control intensity. Remove protected characteristics from production decisioning, but retain properly governed data for compliance testing. Investigate both disparate treatment and unjustified disparate impact.

### Adverse action and explainability

Complexity is not a defense for failing to provide the specific principal reasons required for adverse action. If the system cannot reliably produce faithful reasons, keep it out of credit-decision logic.

### Loan originator compensation and steering

Optimization cannot evade restrictions on compensation based on loan terms or proxies, dual compensation, or steering. Treat compensation-plan changes as legal/compliance projects, not model tuning.

### RESPA Section 8

Broker incentives, referrals, marketing arrangements, leads, and service tiers require review. Payments must not become things of value for referrals; compensable services must be actual, necessary, distinct, and fairly valued.

## Model-risk anchor

The Federal Reserve's revised model-risk guidance emphasizes a risk-based framework covering model development, validation, governance, and controls. The formal scope depends on institution type and size, but these principles are useful for any lender deploying material pricing or credit models. See [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm).

Additional references:

- [CFPB loan originator rule](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/loan-origination-rule/)
- [CFPB RESPA FAQs](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/real-estate-settlement-procedures-act/real-estate-settlement-procedures-act-faqs/)
- [CFPB AI adverse-action circular](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/)

