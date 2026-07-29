# Prioritized Roadmap

## Phase 0: Economic foundation

Before modeling, create one reconciled contribution ledger at application, lock, funded-loan, broker, product, and investor levels.

Deliverables:

- Agreed contribution formula and cost allocation.
- Immutable event timeline and pricing history.
- Broker scorecard with quality and servicing effects.
- Model inventory, compliance boundaries, and experiment process.

## Phase 1: First 90 days

| Order | Build | Initial action | Success measure |
|---:|---|---|---|
| 1 | Lock pull-through / fallout model | Improve hedge forecast and proactive broker follow-up | Higher contribution per lock; lower pair-off cost |
| 2 | Broker profitability model | Reallocate AE analysis and training using risk-adjusted LTV | Higher contribution per AE hour |
| 3 | Closing-time / bottleneck model | Prioritize preventable delays | Lower extension cost and fallout |
| 4 | QC defect triage | Add risk-based reviews above required sampling | Severe defects prevented per review |
| 5 | Investor best execution | Shadow recommendations on funded loans | Realized execution uplift after all fees |

These projects use existing decisions, produce measurable outcomes quickly, and can begin in recommendation mode.

## Phase 2: Months 4-9

| Build | Action |
|---|---|
| Price elasticity | Optimize product/channel margin within approved bands |
| Concession uplift | Approve concessions with positive incremental value |
| Broker treatment uplift | Select training and service interventions that cause improvement |
| Workforce optimizer | Match capacity and skills to forecasted arrivals |
| Warehouse optimizer | Allocate funded loans across facilities under covenants |
| Retain / release optimizer | Compare MSR and SRP economics loan by loan |
| EPO and recapture models | Improve reserves, servicing value, and suitable outreach |

## Phase 3: Months 9-18

- Multi-period capital, product, and coupon appetite optimization.
- Regime-aware hedge and liquidity scenarios.
- Contextual bandits for low-risk, pre-approved service actions.
- Broker graph analytics for fraud and concentration risk.
- Document intelligence with reviewer-confirmed evidence.

## Build / buy guidance

Build models where proprietary broker behavior, internal cycle time, cost, and execution create an edge. Buy commodity capabilities such as document extraction, address standardization, fraud data, market data, and agency/investor rule content, while validating every vendor model in the lender's own population.

## One-page executive dashboard

Track these together:

| Economics | Funnel | Operations | Risk / quality |
|---|---|---|---|
| Contribution $ and bps per lock | Application-to-lock | Median and tail cycle time | Material defect rate |
| Contribution per funded loan | Lock-to-fund | Touches per funded loan | Expected repurchase loss |
| Concession and leakage bps | Fallout reasons | Labor and vendor cost | EPO / early default |
| Hedge and execution bps | Broker share of wallet | Extension and relock rate | Complaints and fair-lending disparities |
| SRP / MSR value | Broker activation / retention | Warehouse dwell days | Model drift and overrides |

## Recommended first decision

Start with **lock pull-through** because it influences pricing, broker behavior, workflow priority, hedge coverage, and expected contribution. Deploy it first as an explainable daily forecast, then use controlled interventions to learn which fallout is actually preventable.

