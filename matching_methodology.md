# Twin-Pair A/B Testing Methodology

## Objective

The goal of this work is to construct a high-quality **matched-pair randomized experiment** for mortgage loan officers identified by `NMLS`.

Instead of assigning people into a generic `Control` group and `Treatment` group at random, we first try to find a highly similar counterpart for each person. Each matched pair acts like a "twin pair":

- one member is assigned to **Control**
- the other member is assigned to **Treatment**

This design improves interpretability because the treatment effect can be evaluated by comparing outcomes **within pairs**, not just across two broad groups.

In experimental-design language, this is a **matched-pair A/B test** or **paired randomized design**.

---

## Why We Started With Strict Pair Matching

The business requirement was not simply:

"Create two groups of similar size."

It was more specific:

"Create twin-like pairs so that each treated loan officer has a nearly identical control counterpart."

That requirement naturally leads to this sequence:

1. Match similar loan officers into pairs.
2. Randomize assignment inside each pair.
3. Compare treatment vs control within the pair after the intervention.

This is stronger than plain randomization when the sample is not huge, because it reduces pre-treatment imbalance.

---

## Phase 1: The Original Strict Exact Pairing Logic

Our first strict approach was designed for smaller datasets.

### Step 1: Use only pre-treatment variables

We matched on variables that describe the baseline profile of each loan officer before any test strategy is applied, such as:

- `pro_score`
- `uwm_production`
- `overall_production`
- `conv_mix`
- `fha_mix`
- `va_mix`
- `purchase_pct`
- `total_ytd_closings`

These are the variables used to define similarity.

### Step 2: Enforce exact matching on rank bucket

We did not allow pairing across different `pro_ranking` groups.

That means:

- `PRO Elite` matches only with `PRO Elite`
- `PRO Plus` matches only with `PRO Plus`
- and so on

This is called an **exact matching constraint**.

It prevents bad business matches that might look numerically close but are not comparable in business context.

### Step 3: Standardize the numeric features

The variables are on different scales:

- `pro_score` might be in the 50 to 130 range
- `overall_production` might be in the 70 to 450 range
- `purchase_pct` is a percentage

If we used raw values directly, larger-scale variables would dominate the distance calculation.

So we standardized each feature using a z-score:

\[
z = \frac{x - \mu}{\sigma}
\]

where:

- \(x\) is the raw feature value
- \(\mu\) is the mean of that feature
- \(\sigma\) is the standard deviation

After standardization, each feature contributes on a comparable scale.

### Step 4: Compute weighted pairwise distance

For each possible pair of loan officers inside the same rank bucket, we computed a **weighted Euclidean distance**:

\[
d(i,j) = \sqrt{\sum_k w_k (z_{ik} - z_{jk})^2}
\]

where:

- \(i, j\) are two loan officers
- \(k\) indexes the matching features
- \(w_k\) is the business weight for feature \(k\)

This means some variables matter more than others. For example, production-related variables may deserve more weight than smaller mix components.

### Step 5: Solve for the best strict pairs

In the first version, we used an **exact dynamic-programming pair solver** within each rank bucket.

Conceptually, that solver searched for the set of one-to-one pairs that minimized total mismatch:

\[
\min \sum_{\text{pairs }(i,j)} d(i,j)
\]

This is an exact optimization objective.

### Step 6: Handle outliers by leaving one unmatched when needed

If a rank bucket had an odd number of people, we did **not** force everyone into pairs.

Instead, one person could be left out as an **outlier** or **unmatched record**.

This is important because forcing bad matches can damage experimental quality.

### Step 7: Randomize within pair

After forming each pair, we randomly assigned:

- one member to **Control**
- one member to **Treatment**

This preserves the randomized nature of the experiment while keeping pair similarity high.

---

## Why the First Exact Solver Was Good for Small Data

The first strict solver was high quality for small datasets because:

- it enforced exact rank matching
- it used weighted baseline similarity
- it did not force poor pairs
- it produced interpretable `pair_id`, `twin_nmls`, and `pair_distance` outputs

For a 20 to 30 row sample, this is excellent.

---

## Why We Upgraded the Matching Engine for Larger Populations

The issue was not the matching logic.

The issue was the **solver scale**.

The first strict solver used a recursive dynamic-programming algorithm. That approach is exact, but it becomes computationally expensive as a rank bucket grows.

For example, if you want to run the same methodology on something like:

- `420` loan officers total

then some `pro_ranking` buckets may contain many records. At that point, the dynamic-programming matcher becomes the bottleneck.

So we upgraded not because the method was wrong, but because we wanted:

- the **same business logic**
- the **same strict quality**
- but a solver that remains reliable on larger groups

---

## Phase 2: The Upgraded Exact MILP Approach

To support larger populations while preserving quality, we introduced a second approach based on **exact optimization with MILP**.

MILP stands for **Mixed-Integer Linear Programming**.

### What stayed the same

The upgrade kept the same experimental principles:

- exact matching within `pro_ranking`
- only pre-treatment covariates
- standardized numeric features
- weighted similarity
- outliers allowed when no good twin exists
- randomized control/treatment assignment after matching

### What changed

The internal pairing engine changed from recursive pair enumeration to an exact mathematical optimization model.

---

## Step-by-Step Logic of the Upgraded Model

### 1. Define candidate edges

Inside each `pro_ranking` bucket, we consider possible candidate pairs.

Each candidate pair is an **edge** between two nodes in a graph:

- node = one loan officer
- edge = one allowed possible twin pairing

Each edge has a cost equal to the weighted distance:

\[
c_{ij} = d(i,j)
\]

### 2. Apply calipers before optimization

We also added **calipers**.

A caliper is a maximum allowed difference on a key variable or on the total pair distance.

That means some candidate edges are forbidden before the optimization even begins.

Example conceptually:

- if two loan officers are too far apart on `pro_score`
- or too far apart on `purchase_pct`
- or too far apart overall

then they are **not eligible twins**

This improves match quality because the solver is not allowed to use clearly weak pairs just to make the math work.

### 3. Introduce unmatched decisions

We allow a loan officer to remain unmatched.

In the optimization, that is represented by an **unmatched variable** with a large penalty.

That means:

- the solver prefers matching when a good match exists
- but it prefers leaving someone unmatched rather than forcing a poor twin

This is exactly what we want in a strict A/B setup.

### 4. Solve a minimum-cost exact matching problem

The optimization chooses:

- which candidate pair edges are selected
- which records remain unmatched

subject to the rule:

each loan officer must either:

- belong to exactly one selected pair
- or be explicitly marked unmatched

The optimization objective is:

\[
\min \left(\sum_{\text{selected pairs }(i,j)} c_{ij} + \sum_{\text{unmatched }u} P\right)
\]

where:

- \(c_{ij}\) is the pair cost
- \(P\) is a large unmatched penalty

This is an **exact minimum-cost matching** formulation.

### 5. Randomize within accepted pairs

Once the optimization produces the final strict pairs:

- one twin is randomly assigned to `Control`
- the other is randomly assigned to `Treatment`

This produces the final experiment-ready assignment file.

---

## Why the Upgrade Is Better for 420 Loan Officers

For a larger population, the upgraded solver is better because it gives:

- **exact optimization quality**
- **scalability beyond tiny buckets**
- **explicit control over weak matches through calipers**
- **clean handling of unmatched outliers**

So if the business asks:

"Can we do this for 420 loan officers while preserving twin quality?"

the upgraded MILP approach is the correct answer.

It is not a heuristic shortcut. It is still an exact optimization framework.

---

## A/B Testing Interpretation

Once the pairs are created, the experiment is interpreted as follows:

- Each `pair_id` is a matched experimental block.
- `Control` receives the existing strategy or no new intervention.
- `Treatment` receives the new strategy being tested.
- `pair_distance` quantifies how similar the two baseline profiles are.
- `twin_nmls` identifies the paired counterpart.

This gives a strong basis for later evaluation.

For example, after the intervention period, the treatment effect can be evaluated as a within-pair difference:

\[
\Delta_p = Y_{p,\text{treatment}} - Y_{p,\text{control}}
\]

where \(Y\) is the post-test outcome of interest.

Then the average treatment effect across pairs can be summarized by averaging those pair-level differences.

This is often easier to explain to business stakeholders because it is a fair "like-for-like" comparison.

---

## Files We Built Around This Process

### Small-data strict version

- `strict_twin_pairs.py`
- output: `strict_paired_ab_assignments.csv`

This version is appropriate when the dataset is small and bucket sizes remain modest.

### Larger-data exact version

- `strict_twin_pairs_exact.py`
- output examples:
  - `strict_paired_ab_assignments_exact.csv`
  - `test_twin_data.csv` for the richer HTML upload schema

This version is the one to prefer when accuracy matters and the population can be much larger.

---

## Output Schema Concepts

The core output assignment files contain fields such as:

- `nmls`
- `assignment`
- `pair_id`
- `twin_nmls`
- `pair_distance`

The richer HTML-ready upload file can additionally include:

- map coordinates like `plot_x`, `plot_y`
- `match_score`

These extra fields are for visualization, not for the matching logic itself.

---

## Final Summary

The full methodology can be summarized in one sentence:

We built a **strict matched-pair randomized A/B design** that first handles outliers, then creates high-quality twin pairs using exact matching logic, and finally assigns one member of each pair to control and the other to treatment.

The original exact pair solver was excellent for small datasets.

The upgraded MILP formulation preserves the same statistical and business logic, but is the better choice when moving toward something like 420 loan officers because it keeps match quality high without relying on a small-scale recursive solver.
