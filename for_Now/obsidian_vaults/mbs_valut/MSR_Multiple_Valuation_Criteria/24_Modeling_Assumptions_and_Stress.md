# Modeling Assumptions and Stress Testing

MSR valuation is model-driven; assumptions and stress scenarios finalize the bid.

## Core Model Inputs
- **Prepayment model**: Vendor (Yield Book, Andrew Davidson, Polypaths, BlackRock AnSer, RiskSpan, Recursion) or proprietary.
- **Default & severity model**: FICO/LTV/DTI/HPA-driven.
- **Cost model**: Per-loan performing/DQ cost curves.
- **Ancillary model**: Late fee, float, recapture.
- **Discount rate**: OAS + risk-free curve (see [[18_Discount_Rate_Assumptions]]).

## Standard Scenarios Run
- **Base case**: Fwd curve, model-driven prepay.
- **+/- 25, 50, 100 bps parallel shifts**: Duration & convexity.
- **Prepay stress**: +/- 25% CPR.
- **Credit stress**: DQ rate shock, HPA down 10-20%.
- **Combined stress**: Recession scenario (rates down + DQ up = worst case).

## Bid Formation
- Multi-scenario weighted average.
- Adjustments for:
  - Bulk vs. flow purchase
  - Data quality / due diligence findings
  - Boarding cost & transfer risk
  - Timing of trade
- Final multiple = raw model output − risk adjustments − target return spread.

## Bid Discipline
- Winning bids often 2–5% above 2nd place (winner's curse).
- Sophisticated buyers benchmark against Fannie/Freddie MSR indices, Recursion / MIAC / MountainView marks.

## Related
- [[18_Discount_Rate_Assumptions]]
- [[21_Counterparty_and_Seller_Quality]]
- [[22_Portfolio_Concentration]]
