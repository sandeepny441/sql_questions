# Operations, Cycle Time, and Cost

The goal is not merely speed. It is the lowest expected cost to produce a compliant, saleable loan on time.

| Knob | ML approach | Decision / action | Metric | Guardrail |
|---|---|---|---|---|
| Queue priority | Learning-to-rank | Rank work by closing risk, value, SLA, and resolvability | Contribution saved per labor hour | Never deprioritize by protected traits or expected denial alone |
| Staff scheduling | Demand forecast + optimization | Match processors, underwriters, closers, and funders to arrivals | Cost per funded loan and SLA | Labor rules and skill constraints |
| Skill-based routing | Matching model | Route complexity to the right specialist | First-touch resolution | Avoid permanent unequal service tiers |
| File completeness | Classification | Detect missing or inconsistent submission data | Touches and suspense days | Rule-validated prompts |
| Condition prediction | Multi-label classification | Prepare likely conditions before underwriting | Condition cycle time | Model cannot replace credit policy |
| Condition clarity | NLP quality checks | Flag vague, duplicate, or conflicting conditions | Rework and complaints | Underwriter approval of changes |
| Appraisal delay | Survival model | Escalate orders likely to miss target | Appraisal days and extensions | Appraiser independence |
| Title / insurance delay | Vendor-duration model | Route or escalate based on expected completion | Vendor cycle time | Approved-vendor and fair-pricing rules |
| Closing readiness | Milestone model | Trigger final checks before documents | On-time closing rate | Required checks remain mandatory |
| Post-close suspense | Defect prediction | Route likely trailing-document problems early | Days to purchase | Evidence-based prioritization |
| Automation eligibility | Rules + classifier | Straight-through low-complexity tasks; review uncertain cases | Labor minutes and error rate | Confidence threshold and audit sampling |
| Duplicate work | Process mining | Remove loops, handoffs, and unnecessary re-entry | Touches per funded loan | Validate control purpose before removal |
| Vendor selection | Causal performance model | Allocate work by quality, speed, cost, and capacity | All-in vendor value | Independence, licensing, geographic coverage |
| Overtime / outsourcing | Forecast + optimizer | Select lowest-cost capacity response | Marginal cost per SLA saved | Quality and security controls |

## Useful operational target

```text
Priority score
= probability of preventable delay
x contribution at risk
x probability the next action resolves the blocker
/ expected labor minutes
```

Apply policy constraints before ranking. A high score recommends attention; it does not authorize a credit decision.

## Process-mining sequence

1. Reconstruct each loan's event timeline.
2. Find loops, handoffs, idle time, and exception paths.
3. Quantify their effect on cost, extensions, fallout, and defects.
4. Test workflow changes in comparable queues.
5. Keep only changes that improve net contribution and quality.

