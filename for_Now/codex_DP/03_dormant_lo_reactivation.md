# Low-Active and Dormant LOs: Targeted Reactivation

## Business question

What is the smallest incentive that materially increases the probability that a dormant LO re-engages?

The goal is not to maximize the discount. The goal is to identify the point where an incentive changes behavior while preserving as much margin as possible.

## Dormant does not mean one thing

Low-active LOs should first be separated into meaningful groups:

| Dormant profile | Interpretation | Likely action |
|---|---|---|
| Previously valuable, recently inactive | Possible relationship lapse | Test a targeted reactivation offer |
| Active elsewhere but quiet with us | Share-of-wallet opportunity | Competitive incentive or engagement |
| Newly onboarded with limited history | Insufficient evidence | Conservative offer and learning strategy |
| Low activity across the market | Limited underlying demand | Avoid deep blanket discount |
| Historically unresponsive to concessions | Low price sensitivity or product mismatch | Hold back and investigate other barriers |

This segmentation prevents the lender from treating low demand and competitive loss as the same problem.

## Reactivation model

The model should predict a specific outcome, such as:

- Submission within 30 days
- Lock within 30 days
- Funded loan within 60 days
- Second lock within 90 days

The second-lock outcome is useful because it distinguishes durable reactivation from a one-time subsidized loan.

## Why uplift modeling is important

A standard classification model identifies LOs who are likely to re-engage. It does not necessarily identify LOs whose behavior changes because of an incentive.

**Uplift modeling** estimates:

> The difference between the probability of reactivation with an incentive and the probability of reactivation without it.

This creates four intuitive populations:

1. **Persuadable:** Reactivates because of the incentive
2. **Sure thing:** Would reactivate without the incentive
3. **Lost cause:** Unlikely to reactivate even with the incentive
4. **Do-not-disturb / negative response:** Incentive does not improve behavior and may have an undesirable effect

The discount should be concentrated on the persuadable group.

## Building the incentive-response curve

### Step 1: Define approved incentive levels

Create a controlled corridor, for example:

- 0 BPS
- 5 BPS
- 10 BPS
- 15 BPS
- 20 BPS
- Additional approved steps when economically justified

### Step 2: Run controlled tests

Within comparable LO segments, assign different incentive levels using a randomized or carefully controlled design.

This creates:

- A **control group** receiving the current strategy
- Multiple **treatment groups** receiving incremental discount levels
- A logged treatment probability for each observation

Randomization reduces selection bias and allows the model to estimate a causal treatment effect.

### Step 3: Estimate the response

Potential methods include:

- Logistic regression with incentive-level interactions
- Generalized additive models for a smooth nonlinear response curve
- Causal forests for heterogeneous treatment effects
- Doubly robust learners combining outcome regression and propensity scores
- Hierarchical Bayesian regression for sparse LO histories

The **treatment coefficient** estimates how the incentive changes reactivation probability. Interaction coefficients estimate which LO traits modify that response.

### Step 4: Identify diminishing returns

The model estimates the probability of reactivation at every approved discount.

The typical curve increases and then begins to flatten. The flattening region represents **diminishing marginal uplift**:

- Early incentive steps create meaningful incremental response.
- Later steps surrender additional margin but produce little incremental volume.

The recommended discount is the smallest amount that:

- Reaches the target reactivation probability
- Produces positive incremental contribution
- Stays inside the approved corridor
- Has acceptable statistical confidence

## Illustrative decision

Suppose the model estimates:

| Discount | Reactivation probability | Incremental interpretation |
|---:|---:|---|
| 0 BPS | 22% | Natural reactivation baseline |
| 10 BPS | 36% | Meaningful uplift |
| 16 BPS | 50% | Target probability reached |
| 30 BPS | 71% | Additional lift, but higher margin cost |
| 60 BPS | 74% | Very little lift beyond 30 BPS |

In this illustrative example:

- The minimum effective incentive is 16 BPS for a 50% target.
- A blanket 60-BPS offer gives away an additional 44 BPS.
- The large discount is inefficient because the response curve has already flattened.

## Safe-corridor operating strategy

The production process can follow a controlled ladder:

1. Score the LO at the current offer.
2. Evaluate the predicted uplift at each approved incentive.
3. Select the first economically valid treatment.
4. Observe response for the defined window.
5. Increase only when the expected incremental value remains positive.
6. Stop when the target probability is reached or marginal uplift becomes too small.

This is a **dose-response optimization** problem: the incentive is the dose and reactivation is the response.

## Success metrics

Leadership should monitor:

- Incremental reactivation rate
- Incremental locks and funded loans
- Cost per incremental lock
- Net contribution after incentive cost
- 30-day and 90-day repeat behavior
- Pull-through after reactivation
- Margin saved versus the blanket offer
- Treatment-effect confidence intervals

The word “incremental” matters. Raw activation rate includes LOs who would have returned without a discount.

## Important technical terminology

- **Uplift modeling:** Predicts the behavioral change caused by treatment
- **Treatment effect:** Difference between the treated and untreated outcomes
- **Propensity score:** Estimated probability of receiving a particular treatment
- **Doubly robust estimation:** Combines treatment and outcome models to reduce bias
- **Dose-response curve:** Outcome response across multiple incentive levels
- **Diminishing marginal uplift:** Smaller incremental benefit from each additional BPS
- **Heterogeneous treatment effect:** Different incentive responses across LOs
- **Confidence interval:** Range expressing uncertainty around an estimate

## Leadership takeaway

Reactivation is not about finding the most generous offer:

> Use uplift modeling to find the smallest incentive expected to create behavior that would not have happened otherwise.

