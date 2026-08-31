
| **#** | **Prepayment Type**              | **What Happens**                                                             | **Typical Trigger**                    | **Common Industry Impact**           |
| ----- | -------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------ |
| 1     | Rate-and-Term Refinance          | Borrower replaces existing loan with a lower-rate or different-term mortgage | Interest rates fall                    | Faster agency MBS prepays, MSR loss  |
| 2     | Cash-Out Refinance               | Borrower refinances and extracts home equity as cash                         | Home appreciation or liquidity need    | Larger loan balance resets           |
| 3     | Home Sale Payoff                 | Mortgage fully paid when property is sold                                    | Moving homes                           | Natural turnover-driven prepayment   |
| 4     | Curtailment / Partial Prepayment | Borrower pays extra principal without fully closing loan                     | Wants faster payoff                    | Loan amortizes faster                |
| 5     | Full Early Payoff                | Entire mortgage balance paid off ahead of maturity                           | Large cash inflow                      | Immediate servicing termination      |
| 6     | Recapture Refinance              | Existing lender refinances borrower internally                               | Retention campaign                     | Helps preserve customer relationship |
| 7     | Streamline Refinance             | Simplified refinance program                                                 | Government-backed loan programs        | High-speed refinance waves           |
| 8     | Cash-In Refinance                | Borrower brings cash to closing to reduce balance                            | Improve LTV or monthly payment         | Reduces credit risk                  |
| 9     | Distressed Payoff                | Loan terminated due to liquidation/distress                                  | Foreclosure, short sale                | Credit loss implications             |
| 10    | Involuntary Prepayment           | Insurance or external event forces payoff                                    | Disaster, condemnation, death          | Unexpected portfolio runoff          |
| 11    | Balloon Payoff                   | Large remaining balance paid at maturity                                     | Balloon loan maturity                  | Concentrated payoff event            |
| 12    | Builder / Relocation Buyout      | Employer or builder helps retire mortgage                                    | Relocation or incentives               | Accelerated turnover                 |
| 13    | Assumption-Driven Payoff         | Existing mortgage replaced during property transfer                          | Assumption denied or replaced          | Loan exits pool                      |
| 14    | Portfolio Optimization Payoff    | Investor or borrower restructures debt strategically                         | Tax or financial planning              | High-net-worth borrower behavior     |
| 15    | Strategic Refinance              | Borrower refinances despite small rate incentive                             | Product switch or cash-flow preference | Harder to model behavior             |

---

# **Detailed Breakdown**

## **1. Rate-and-Term Refinance**

| **Aspect**         | **Details**                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Definition         | Borrower refinances primarily to reduce interest rate or change loan term |
| Example            | 7% mortgage refinanced into 5.9% mortgage                                 |
| Most Sensitive To  | Treasury yields, Fed rates                                                |
| Industry Name      | “Refi wave” driver                                                        |
| MBS Impact         | Major source of agency prepayment risk                                    |
| Modeling Variables | Coupon spread, FICO, burnout, incentive                                   |

---

## **2. Cash-Out Refinance**

| **Aspect**          | **Details**                                                       |
| ------------------- | ----------------------------------------------------------------- |
| Definition          | Borrower refinances for a larger amount and takes cash difference |
| Example             | Owes $300K, refinances into $400K loan, receives $100K cash       |
| Common Uses         | Renovation, debt consolidation, business needs                    |
| Risk Characteristic | Higher leverage after refinance                                   |
| Industry Importance | Very important in rising home-price environments                  |
| Analytics Focus     | Equity extraction propensity                                      |

---

## **3. Home Sale Payoff**

| **Aspect**           | **Details**                          |
| -------------------- | ------------------------------------ |
| Definition           | Loan fully repaid when house is sold |
| Trigger              | Relocation, upsizing, downsizing     |
| Key Driver           | Housing turnover                     |
| Economic Sensitivity | Labor market + housing demand        |
| Modeling Category    | Mobility-based prepayment            |

---

## **4. Curtailment / Partial Prepayment**

| **Aspect**       | **Details**                                           |
| ---------------- | ----------------------------------------------------- |
| Definition       | Borrower pays extra principal but keeps same mortgage |
| Example          | Monthly payment + extra $500                          |
| Goal             | Reduce interest burden                                |
| MBS Impact       | Slower but steady balance runoff                      |
| Hard to Predict? | Yes, borrower-behavior driven                         |

---

## **5. Full Early Payoff**

|**Aspect**|**Details**|
|---|---|
|Definition|Entire balance paid before maturity|
|Sources|Bonus, inheritance, business sale|
|Common In|Wealthy borrower segments|
|Servicing Impact|Immediate MSR termination|
|Analytics Term|Unscheduled payoff|

---

## **6. Recapture Refinance**

| **Aspect**      | **Details**                                       |
| --------------- | ------------------------------------------------- |
| Definition      | Original lender retains borrower during refinance |
| Goal            | Prevent competitor takeover                       |
| Example         | UWM refinances its own servicing customer         |
| KPI             | Recapture rate                                    |
| Strategic Value | Preserves servicing economics                     |

---

## **7. Streamline Refinance**

|**Aspect**|**Details**|
|---|---|
|Definition|Simplified refinance requiring limited underwriting|
|Common Programs|FHA Streamline, VA IRRRL|
|Benefit|Faster refinance process|
|Risk|Can create rapid prepayment spikes|
|Modeling Challenge|Program eligibility timing|

---

## **8. Cash-In Refinance**

|**Aspect**|**Details**|
|---|---|
|Definition|Borrower adds cash during refinance|
|Goal|Reduce LTV or monthly payment|
|Common During|Declining home prices|
|Risk Impact|Improves collateral quality|
|Typical Borrower|Financially strong borrowers|

---

## **9. Distressed Payoff**

|**Aspect**|**Details**|
|---|---|
|Definition|Loan terminates through distress event|
|Examples|Foreclosure sale, short sale|
|Not Truly “Good” Prepay|Often associated with losses|
|Credit Impact|Negative|
|Investor Concern|Severity + recovery timing|

---

## **10. Involuntary Prepayment**

|**Aspect**|**Details**|
|---|---|
|Definition|External event forces loan payoff|
|Examples|Natural disaster insurance claim|
|Frequency|Rare|
|Portfolio Impact|Difficult to forecast|
|Modeling Need|Catastrophe overlays|

---

## **11. Balloon Payoff**

|**Aspect**|**Details**|
|---|---|
|Definition|Large remaining principal due at maturity|
|Common In|Commercial or non-QM loans|
|Risk|Refinance dependency|
|Timing|Highly predictable|
|Analytics Use|Scheduled payoff forecasting|

---

## **12. Builder / Relocation Buyout**

|**Aspect**|**Details**|
|---|---|
|Definition|Builder/employer incentivizes payoff|
|Example|Corporate relocation package|
|Common In|Executive relocation|
|Market Sensitivity|Housing cycles|
|Modeling Difficulty|Moderate|

---

## **13. Assumption-Driven Payoff**

|**Aspect**|**Details**|
|---|---|
|Definition|Existing mortgage replaced during ownership transfer|
|Common With|FHA/VA assumptions|
|Why Payoff Happens|New financing replaces old loan|
|Market Relevance|Rising-rate environments|
|Industry Concern|Loan retention loss|

---

## **14. Portfolio Optimization Payoff**

|**Aspect**|**Details**|
|---|---|
|Definition|Borrower restructures liabilities strategically|
|Seen In|Wealth management clients|
|Motivation|Tax efficiency or liquidity planning|
|Modeling Challenge|Non-rate-sensitive behavior|
|Frequency|Low|

---

## **15. Strategic Refinance**

|**Aspect**|**Details**|
|---|---|
|Definition|Borrower refinances for non-obvious reasons|
|Examples|Product switch, ARM → fixed|
|Not Fully Rate Driven|Yes|
|Behavioral Complexity|High|
|Important For|Advanced ML prepayment models|

---

# **Simplified Big-Picture Hierarchy**

| *Main Bucket*                  | *Subtypes*                                          |
| ------------------------------ | --------------------------------------------------- |
| Refinance-Based                | Rate-term, cash-out, streamline, cash-in, recapture |
| Property Turnover-Based        | Home sale payoff, relocation payoff                 |
| Voluntary Principal Reduction  | Curtailment, full payoff                            |
| Distress-Based                 | Foreclosure payoff, liquidation payoff              |
| Structural / Contractual       | Balloon payoff                                      |
| External / Rare Events         | Insurance/disaster payoff                           |
| Strategic / Financial Planning | Portfolio optimization, strategic refinance         |
|                                |                                                     |

---

# **Most Important Types in Real Mortgage Analytics**

|**Importance Rank**|**Type**|
|---|---|
|1|Rate-and-term refinance|
|2|Home sale payoff|
|3|Cash-out refinance|
|4|Recapture refinance|
|5|Curtailment|
|6|Distressed payoff|

These six dominate most:

- agency MBS models
- MSR valuation systems
- EPO prediction models
- lender retention analytics
- mortgage hedge models.