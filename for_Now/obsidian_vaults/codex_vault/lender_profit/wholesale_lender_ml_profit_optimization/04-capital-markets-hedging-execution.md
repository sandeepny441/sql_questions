# Capital Markets, Hedging, and Execution

These levers often improve profit without changing borrower treatment. They require accurate timestamps, market data, loan state history, investor grids, and cost allocation.

| Knob | ML / optimization approach | Decision / action | Profit metric | Guardrail |
|---|---|---|---|---|
| Lock fallout forecast | Gradient boosting + calibration | Set expected funded balance by segment | Hedge cost per lock | Recalibrate by regime and horizon |
| Closing-date forecast | Survival model | Align hedge duration with expected funding | Pair-off and carry cost | Operational events must update forecast |
| Hedge ratio | Constrained portfolio optimization | Size coverage for expected exposure and risk limits | Hedge effectiveness | Hard position and risk limits |
| TBA coupon allocation | Scenario optimization | Allocate exposure across coupons | Expected execution less basis risk | Stress tests and human supervision |
| Pair-off timing | Expected-value model | Pair off excess coverage at controlled threshold | Pair-off loss avoided | No unconstrained market speculation |
| Investor best execution | Rules + constrained optimizer | Choose eligible investor / cash / MBS execution | Net sale proceeds | Include all LLPAs, fees, reps, and delivery cost |
| Pool composition | Integer optimization | Form pools balancing price, eligibility, and speed | Pooling uplift | Delivery and concentration constraints |
| Specified pay-up forecast | Regression / market model | Estimate collateral pay-up by pool attributes | Incremental execution bps | Conservative out-of-sample validation |
| Mandatory vs best efforts | Expected-value model | Select commitment type by pull-through and economics | Net execution after fallout | Contract and capacity limits |
| Delivery timing | Time-series + optimization | Balance carry, market exposure, and investor cutoffs | Days to sale and carry cost | Liquidity limits |
| Warehouse allocation | Linear / mixed-integer optimization | Route loans across facilities | Interest, dwell, and facility fee | Covenants, haircuts, concentration |
| Cash and liquidity | Forecasting + stress testing | Forecast draws, paydowns, margin calls | Liquidity cost and buffer | Severe stress scenarios |
| Product / coupon appetite | Portfolio optimizer | Set pricing overlays within risk appetite | Portfolio contribution and risk | Governance-approved bounds |

## Execution equation

```text
Net execution
= investor or security price
+ servicing value
- LLPAs and delivery fees
- hedge slippage and pair-offs
- warehouse carry
- expected representation, warranty, and liquidity cost
```

Best execution should be recalculated whenever eligibility, investor grids, servicing bids, market prices, or loan data change.

## Experiment and validation

Backtest every recommendation against the exact opportunity set available at the decision timestamp. Use a shadow mode before allowing automated allocations. Report realized uplift versus the legacy strategy after fees, with stress results by rate regime.

## Reference

- [Fannie Mae Servicing Marketplace](https://singlefamily.fanniemae.com/applications-technology/servicing-marketplace)
- [Fannie Mae servicing-released pricing API](https://singlefamily.fanniemae.com/media/22206/display)

