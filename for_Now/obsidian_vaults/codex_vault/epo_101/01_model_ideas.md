**This is a classic rare-event prediction problem in credit risk / lending, but with important nuances due to the time-to-event nature of prepayment.** Your setup (2M loans over 10 years, <1% observed prepayments) is common in loan portfolios, especially if many loans are recent, long-term (e.g., mortgages), or if "prepaid" is strictly defined (full payoff before maturity, excluding partial curtailments). The low positive rate creates class imbalance, but the bigger issue is usually **right-censoring**: many loans are still active or haven't had enough time to prepay, so you can't simply label them as "will never prepay."

### 1. Reframe the Problem (Strongly Recommended)
Pure binary classification ("will this loan ever prepay?") is often suboptimal here because:
- It ignores *when* prepayment happens and discards timing information.
- Recent loans get biased toward the negative class (short observation window).
- It doesn't naturally handle loans that mature without prepaying or are still active.

**Better framing: Survival analysis (time-to-prepayment modeling)**. This directly models the hazard $h(t)$ (instantaneous probability of prepaying at time $t$, given survival so far) or the survival function $S(t \mid X)$ — the probability of not having prepaid by time $t$, given loan characteristics $X$. From this you can derive exactly what you want: the probability that a new loan will prepay (by any horizon relevant to your business).

Key advantages for your data:
- Naturally incorporates **censoring** (the majority of your "negatives" contribute valuable information up to their censor time).
- Captures **seasoning** (prepayment risk often changes with loan age — e.g., peaks after a few years).
- Uses *all* 2M loans efficiently instead of discarding recent ones.
- With thousands of observed events (even at <1% overall), you have enough signal; the large sample size helps.

Literature on mortgages, auto loans, and consumer credit frequently uses this approach (Cox models, discrete-time hazards, random survival forests, etc.). Logistic regression is a simpler practical approximation when event rates are low, but survival is theoretically superior when you have loan-level timing data.

If your business truly needs only a single binary-style probability (e.g., "prepay within 12/24 months"), you can still derive it from a survival model. Or fall back to filtered binary classification (see below).

### 2. Recommended Approach: Survival Analysis Pipeline
#### Step 1: Data Preparation & EDA (Critical)
- **Define events and censoring clearly**:
  - Event = prepayment (full payoff before scheduled maturity).
  - Censoring time $C = \min(\text{maturity date},\, \text{observation end date},\, \text{default date},\, \text{other exit})$ if no prepayment observed.
  - Record observed time $T_i$ (time from origination to event/censor for loan $i$) and event indicator $\delta_i$ ($\delta_i = 1$ if prepaid, $\delta_i = 0$ if censored). In code: `duration` and `event`.
- Handle competing risks if relevant (e.g., default can prevent prepayment observation). Use cause-specific hazards or subdistribution models (Fine-Gray).
- **Features** (at origination for new loans; time-varying where possible):
  - Loan: amount, term, interest rate (and spread vs. market at origination), LTV, DTI, purpose (purchase vs. refi — refis often prepay faster), type.
  - Borrower: credit score, income stability, age, demographics.
  - Macro/context: origination-year factors, location, property type. For forward prediction, include or scenario on rate incentive ($\text{current market rate} - \text{note rate}$), unemployment, home prices (these drive refinancing).
  - Derived: ratios, interactions ($\text{rate} \times \text{credit score}$), bins for interpretability.
- **EDA**:
  - Kaplan–Meier curves (overall and stratified by key features like credit score buckets, LTV, rate spread). This shows baseline prepayment behavior and highlights differences.
  - Check event counts by vintage/seasoning — confirms your <1% rate and identifies data issues.
  - Missing values (common in loan data) — impute or use models that handle them natively (trees).

**Time-based splitting** for train/validation/test (e.g., train on originations up to year $T_{\text{train}}$, validate on later periods). This mimics predicting new incoming loans and avoids leakage from future macros or performance.

#### Step 2: Modeling Options (Start Simple, Scale Up)
1. **Baseline: Cox Proportional Hazards (Cox PH)** — Highly recommended starting point.
   - Models hazard:
     $$h(t \mid X) = h_0(t)\,\exp(\beta^\top X)$$
     where $h_0(t)$ is the baseline hazard (captures seasoning) and $\exp(\beta)$ are interpretable hazard ratios.
   - Easy in Python with `lifelines` (great documentation, plotting, stats tests).
   - Check proportional hazards assumption (Schoenfeld residuals). If violated, add time interactions or move to ML/non-proportional models.
   - Outputs full survival curve per loan → probability of prepayment by any $t$ you choose:
     $$P(\text{prepay by } t \mid X) = 1 - S(t \mid X)$$

2. **Machine Learning Survival Models** (better for complex non-linear interactions, large feature sets):
   - Random Survival Forests or Gradient Boosted Survival models (`scikit-survival`).
   - Neural survival models (e.g., DeepSurv-style or multi-task logistic regression in `pysurvival` — has a credit-risk/loan tutorial).
   - XGBoost/LightGBM with survival extensions or custom objectives (used successfully in recent mortgage prepayment papers).

3. **Discrete-Time Hazard Model (Very Flexible & Powerful)**:
   - Expand data to person-period format (one row per loan per time interval — monthly/quarterly — until event or censor).
   - Model the conditional probability of prepaying in interval $s$ given survival to $s-1$ using any classifier (Logistic Regression, LightGBM, XGBoost, Neural Net).
   - Add time features or baseline hazard terms; easily include time-varying covariates (e.g., evolving rate incentive, macros).
   - Derive cumulative probability:
     $$
     P(\text{prepay by } t \mid X) = 1 - \prod_{s=1}^{t} \bigl(1 - h(s \mid \text{survived to } s-1,\, X)\bigr)
     $$
   - Handles your imbalance naturally per period (use `scale_pos_weight` or class weights). Great for age-period-cohort effects (loan age, vintage, calendar time).
   - Caution with data size: $2\text{M}$ loans $\times$ many periods can explode memory — use coarser granularity, sampling, or stick to continuous-time models for prototyping.

**For new/incoming loans** (at origination, $t=0$): Feed origination characteristics $X$. Predict the full curve or probability up to a business-relevant horizon. For forward-looking macros (rates, economy), use scenarios, averages, or assume constant incentive. Many production models output sensitivities or expected prepayment under rate paths.

#### Step 3: Handling the Extreme Imbalance (<1% Events)
Survival models handle this better than naive binary classification because:
- Partial likelihood in Cox focuses on event times.
- Censored observations still contribute up to their censor time.
- You retain all 2M loans.

Additional techniques:
- **Class weights / scale_pos_weight** in tree-based or boosting models (e.g., in LightGBM/XGBoost or survival extensions).
- Regularization ($L_1$/$L_2$, early stopping) to prevent overfitting on rare events.
- For discrete-time: focal loss or careful weighting per period.
- If events are *extremely* sparse in some segments, consider pooling or hierarchical models.
- SMOTE/ADASYN variants exist for survival but are less common and computationally heavy on 2M rows — usually unnecessary if you use proper survival methods + weights.

#### Step 4: Evaluation & Calibration (Probabilities Matter)
- **Metrics**: Concordance index (C-index, like AUC for survival), integrated Brier score (proper scoring for probabilities + calibration), time-dependent AUC/PR curves, calibration plots/reliability diagrams.
- **Do not use accuracy**. Focus on Precision-Recall (imbalance-aware) and proper scoring rules (log-loss, Brier) for probabilities.
- **Calibrate probabilities** post-training (isotonic regression or Platt scaling, or `CalibratedClassifierCV` equivalents for survival). Tree-based and neural models are often miscalibrated out-of-the-box.
- Validate on time-held-out data. Monitor for distribution shift (prepayment behavior changes with interest rates, economy, borrower behavior).

#### Step 5: Implementation Notes (Scalability)
- **Python stack**:
  - `lifelines` — Cox PH, Kaplan–Meier, easy start.
  - `scikit-survival` — ML survival models + scikit-learn compatibility + metrics.
  - `pysurvival` — Additional models (including neural) + credit risk examples.
  - `XGBoost` / `LightGBM` / `CatBoost` — For discrete-time or boosted survival.
  - `imbalanced-learn`, `scikit-learn` for preprocessing/weights/calibration.
- With 2M rows: Prototype on a stratified subsample or recent vintages. Full data is feasible for tree-based models (they scale well). For discrete-time expansion, consider quarterly intervals or memory-efficient implementations.
- Interpretability (important in lending/regulatory contexts): SHAP values, partial dependence plots, hazard ratios from Cox. Use explainable ML survival variants.
- Production: Version models, monitor drift (especially macro-driven prepay), document assumptions. Consider model risk governance.

### 3. Simpler Alternative: Binary Classification (If Survival Not Feasible Initially)
Define a fixed horizon $H$ (e.g., prepay within 24 months) and filter to loans with sufficient observation time (originated $\geq H + \text{buffer}$ ago, so all can be fully labeled). Label $1$ if event $\leq H$, $0$ otherwise (or censored after $H$).

Then:
- Use **XGBoost/LightGBM/CatBoost** with $\texttt{scale\_pos\_weight} \approx \dfrac{\text{negatives}}{\text{positives}}$.
- Or resampling (SMOTE variants, but subsample first due to size).
- Logistic Regression as interpretable baseline (add class weights or balanced sampling).
- Always calibrate probabilities.
- Metrics: PR-AUC, F1, expected calibration error, Brier score.

**Caveats**: Loses power (smaller effective sample, especially recent loans), ignores exact timing, and can bias if censoring is informative. Compare performance to a survival model on the same filtered data.

### 4. Practical Next Steps & Considerations
1. **Clarify with stakeholders**: Exact definition of "prepaid," business-relevant time horizon(s) for the probability output, loan type (mortgage/auto/personal changes drivers), competing events (default?), and whether partial prepayments/curtailments count.
2. Perform EDA with Kaplan–Meier curves and event counts by key segments/vintages.
3. Prototype a Cox PH model in `lifelines` (quick win, interpretable).
4. Compare to a discrete-time LightGBM hazard model or Random Survival Forest.
5. Iterate on features (especially rate incentive/spread and macro proxies) and validate temporally.
6. If events are truly extremely rare after proper definition, investigate data quality or consider whether a "prepayment score" / risk tier (rather than precise probability) suffices for decisioning.

This approach leverages your large dataset effectively, produces well-calibrated probabilities, handles the rarity and censoring properly, and aligns with established practices in lending and structured finance. Survival models (or discrete-time ML approximations) are the gold standard here for exactly the reasons your data presents challenges.

If you share more details (loan type, exact target definition/horizon, sample features, or whether you have time-varying data/macros), I can refine this further — e.g., suggest specific code structure, feature ideas, or even help prototype in the sandbox. What aspect would you like to dive into first?