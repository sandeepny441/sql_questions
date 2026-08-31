# Credit Quality, Defects, and Repurchase Risk

These models should prioritize review and prevention. They should not silently redefine credit policy or replace required quality-control samples.

| Knob | ML approach | Decision / action | Metric | Guardrail |
|---|---|---|---|---|
| Prefunding QC selection | Risk model + required random sample | Add targeted reviews above mandatory sampling | Severe defects prevented per review | Preserve required random and discretionary samples |
| Post-closing QC selection | Risk model | Prioritize loans with high expected defect loss | Review yield and loss avoided | Do not omit required coverage |
| Income inconsistency | Rules + anomaly detection | Flag mismatches across documents and data | Material defect rate | Human verification; explainable evidence |
| Asset inconsistency | Entity matching + anomaly detection | Detect unexplained deposits or conflicting balances | Defects and fraud loss | Avoid unsupported fraud labels |
| Occupancy / identity risk | Graph + anomaly detection | Route suspicious relationships for investigation | Confirmed loss prevented | Privacy and human investigation |
| Collateral risk | Appraisal analytics | Flag comparables, adjustments, or values needing review | Collateral defect severity | Appraiser independence; no automated value coercion |
| Eligibility defect | Rules engine | Recheck product, agency, and investor eligibility | Unsaleable loans avoided | Versioned rules and effective dates |
| Data integrity | Cross-system reconciliation | Detect LOS, AUS, closing, and delivery mismatches | Purchase suspense and defect rate | System-of-record controls |
| Early payment default | Survival model | Reserve, investigate root causes, and tighten controls | Expected loss | Credit-policy changes require governance |
| Early payoff | Survival model | Price servicing/EPO exposure and improve recapture | EPO cost and MSR value | Borrower prepayment rights |
| Repurchase severity | Frequency-severity model | Estimate reserve and remediation priority | Expected repurchase loss | Conservative stress and finance approval |
| Broker quality | Hierarchical model | Adjust review intensity for credible quality signals | Risk-adjusted QC efficiency | Minimum evidence; avoid guilt by association |
| Root-cause classification | NLP + taxonomy mapping | Map findings to process, broker, vendor, or policy cause | Repeat-defect reduction | Reviewer confirmation |
| Corrective action | Causal analysis | Select training, workflow, or control most likely to work | Defect recurrence | Track completion and effectiveness |

## Loss target

Model both probability and severity:

```text
Expected quality loss
= P(material defect) x P(enforcement | defect) x expected severity
+ expected remediation and carrying cost
```

Use this value to prioritize incremental reviews. Mandatory quality-control requirements remain independent constraints.

## Regulatory and agency anchors

- [Fannie Mae loan defect taxonomies](https://singlefamily.fanniemae.com/loan-defect-taxonomies)
- [Fannie Mae loan quality resources](https://singlefamily.fanniemae.com/originating-underwriting/loan-quality)
- [Fannie Mae quality-control guidance update](https://singlefamily.fanniemae.com/originating-underwriting/loan-quality/quality-insider/july-2025)
- [Fannie Mae QC validation service](https://singlefamily.fanniemae.com/applications-technology/desktop-underwriter-validation-service/du-validation-service-resource-center/quality-control)

