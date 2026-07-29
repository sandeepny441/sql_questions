# Servicing, MSR, and Recapture

Servicing decisions belong in origination economics. A higher cash execution is not necessarily better after MSR value, EPO exposure, operational cost, and liquidity are considered.

| Knob | ML / optimization approach | Decision / action | Metric | Guardrail |
|---|---|---|---|---|
| Retain vs release | Loan-level cash-flow simulation | Choose retained or released execution | Risk-adjusted NPV | Liquidity, capital, accounting, capacity |
| Servicer / buyer choice | Best-execution optimizer | Select highest all-in eligible servicing bid | SRP uplift | Include LLPAs, fees, and counterparty risk |
| MSR valuation | Prepayment + default + cost models | Estimate loan-level servicing cash flows | MSR NPV and valuation error | Independent validation and stress testing |
| Prepayment forecast | Competing-risks survival model | Improve MSR valuation and hedge | Duration and NPV error | Rate-regime monitoring |
| Delinquency forecast | Survival / transition model | Forecast servicing cost and credit exposure | Expected servicing cost | Assistance and loss-mitigation compliance |
| Servicing cost | Activity-based model | Price operational intensity by segment | Cost-to-service accuracy | Do not reduce required service |
| EPO exposure | Survival model | Price or reserve for early payoff clauses | EPO cost per funded loan | No barriers to prepayment |
| Refinance recapture | Causal uplift model | Contact borrowers likely to benefit and respond | Incremental recapture NPV | Consent, suitability, licensing, fair lending |
| Portfolio sale timing | Scenario optimizer | Compare hold, bulk sale, and flow execution | Risk-adjusted proceeds | Liquidity and market-risk limits |
| MSR hedge | Duration / convexity model + optimizer | Size approved hedge instruments | P&L volatility and hedge cost | Risk limits and independent oversight |
| Complaint / attrition risk | NLP + classification | Route service recovery early | Complaint, transfer, and retention outcomes | Preserve complaint rights and records |

## All-in choice

```text
Retain value
= servicing fee cash flows
- servicing cost
- default and advance cost
- hedge and capital cost

Release value
= SRP
- LLPAs and delivery fees
- expected EPO and counterparty cost
```

Compare both on the same valuation date and assumptions.

## References

- [Fannie Mae Servicing Marketplace](https://singlefamily.fanniemae.com/applications-technology/servicing-marketplace)
- [Fannie Mae servicing retained/released guide](https://singlefamily.fanniemae.com/media/document/pdf/servicing-retainedreleased-resource-guide)

