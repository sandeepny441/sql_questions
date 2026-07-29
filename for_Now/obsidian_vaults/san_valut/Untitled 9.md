**Here’s the clean, Obsidian-friendly version** with **only one predictor (Sales)** + intercept.

---

### Simple Linear Regression Example  
**Revenue = β₀ + β₁ × Sales Budget + ε**

#### Data (5 months)

| Month | Sales Budget ($000) | Revenue ($000) |
|-------|---------------------|----------------|
| 1     | 20                  | 120            |
| 2     | 25                  | 160            |
| 3     | 30                  | 190            |
| 4     | 28                  | 145            |
| 5     | 22                  | 165            |

---

### Final Regression Results

$$
\text{Revenue} = 32.67 + 5.17 \times \text{Sales Budget} + \epsilon
$$

**Full Statistics Table**

| Coefficient       | Estimate ($\hat{\beta}$) | Std. Error | t-statistic | p-value   | 95% Confidence Interval     |
|-------------------|--------------------------|------------|-------------|-----------|-----------------------------|
| Intercept ($\beta_0$) | 32.67                    | 9.79       | 3.34        | 0.079     | $[-9.46,\ 74.80]$          |
| **Sales** ($\beta_1$) | **5.17**                 | **0.435**  | **11.89**   | **0.007** | **[3.30, 7.04]**           |

---

### Interpretation (Student-friendly)

- **Intercept (β₀ = 32.67)**: Even if we spend $0 on Sales, we expect about $32,670 in base revenue (not statistically significant here, p=0.079).
- **Sales (β₁ = 5.17)**: For every extra **$1,000** spent on Sales, we expect **+$5,170** in Revenue.
  - This is **highly statistically significant** (p = 0.007).
  - 95% Confidence Interval **[3.30, 7.04]** means we are quite confident the true effect is between $3.30 and $7.04 revenue per $1 spent.

---

### Model Summary
- **R² = 0.986** → Sales budget explains **98.6%** of the variation in Revenue.
- Degrees of Freedom = 3.

---

Copy and paste the whole thing above using **⌘ + Shift + V** in Obsidian. It should look clean.

Would you like me to make it even simpler, or add the full step-by-step math for this single-variable case?