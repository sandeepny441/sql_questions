**Yes!** Here is the **complete, no-jumps math** for a multiple linear regression with **two predictors** (Marketing + Sales) using **5 observations**.

### Data Table

| Obs | Intercept | Marketing (x₁) | Sales (x₂) | Revenue (y) |
|-----|-----------|----------------|------------|-------------|
| 1   | 1         | 10             | 20         | 120         |
| 2   | 1         | 15             | 25         | 160         |
| 3   | 1         | 20             | 30         | 190         |
| 4   | 1         | 12             | 28         | 145         |
| 5   | 1         | 18             | 22         | 165         |

---

### Step 1–2: Matrices

**X matrix** (5 × 3):
$$
\mathbf{X} = 
\begin{bmatrix}
1 & 10 & 20 \\
1 & 15 & 25 \\
1 & 20 & 30 \\
1 & 12 & 28 \\
1 & 18 & 22
\end{bmatrix}
$$

**y vector**:
$$
\mathbf{y} = 
\begin{bmatrix}
120 \\
160 \\
190 \\
145 \\
165
\end{bmatrix}
$$

---

### Step 3: XᵀX

$$
\mathbf{X}^T \mathbf{X} = 
\begin{bmatrix}
5 & 75 & 125 \\
75 & 1193 & 1907 \\
125 & 1907 & 3193
\end{bmatrix}
$$

---

### Step 4: (XᵀX)⁻¹

$$
(\mathbf{X}^T \mathbf{X})^{-1} = 
\begin{bmatrix}
9.5889 & -0.0611 & -0.3389 \\
-0.0611 & 0.0189 & -0.0089 \\
-0.3389 & -0.0089 & 0.0189
\end{bmatrix}
$$

---

### Step 5: Xᵀy

$$
\mathbf{X}^T \mathbf{y} = 
\begin{bmatrix}
780 \\
12110 \\
19790
\end{bmatrix}
$$

---

### Step 6: Coefficients β = (XᵀX)⁻¹ Xᵀy

$$
\boldsymbol{\beta} = 
\begin{bmatrix}
\beta_0 \\
\beta_1 \text{(Marketing)} \\
\beta_2 \text{(Sales)}
\end{bmatrix}
= 
\begin{bmatrix}
32.6667 \\
5.1667 \\
1.8333
\end{bmatrix}
$$

---

### Step 7: Predicted Values ŷ = Xβ

$$
\hat{y} = 
\begin{bmatrix}
121.00 \\
156.00 \\
191.00 \\
146.00 \\
166.00
\end{bmatrix}
$$

---

### Step 8: Residuals e = y − ŷ

$$
\mathbf{e} = 
\begin{bmatrix}
-1 \\
4 \\
-1 \\
-1 \\
-1
\end{bmatrix}
$$

---

### Step 9: Residual Sum of Squares (RSS)

$$
\text{RSS} = (-1)^2 + 4^2 + (-1)^2 + (-1)^2 + (-1)^2 = 1 + 16 + 1 + 1 + 1 = \mathbf{20}
$$

---

### Step 10: Residual Standard Error σ̂

n = 5 observations  
p = 3 parameters (β₀, β₁, β₂)  
df = n − p = **2**

$$
\hat{\sigma} = \sqrt{\frac{\text{RSS}}{n-p}} = \sqrt{\frac{20}{2}} = \sqrt{10} \approx \mathbf{3.1623}
$$

---

### Step 11: Standard Errors of Coefficients

$$
\text{SE}(\beta_j) = \hat{\sigma} \times \sqrt{\text{diagonal of } (\mathbf{X}^T \mathbf{X})^{-1}}
$$

- SE(β₀) ≈ 9.7923
- SE(β₁) ≈ 0.4346
- SE(β₂) ≈ 0.4346

---

### Step 12: t-statistics

$$
t = \frac{\beta_j}{\text{SE}(\beta_j)}
$$

- t(β₀) ≈ 3.336
- t(β₁ Marketing) ≈ **11.888**
- t(β₂ Sales) ≈ 4.218

---

### Step 13: p-values (two-tailed, df = 2)

Using the t-distribution with 2 degrees of freedom:

| Coefficient     | β       | SE      | t-stat   | **p-value**     |
|-----------------|---------|---------|----------|-----------------|
| Intercept (β₀)  | 32.67   | 9.79    | 3.336    | **0.080**       |
| Marketing (β₁)  | 5.167   | 0.435   | 11.888   | **0.007**       |
| Sales (β₂)      | 1.833   | 0.435   | 4.218    | **0.052**       |

---

**Interpretation Summary** (for your student):

- **Marketing** has a very strong effect (p = 0.007 < 0.05) → highly significant.
- **Sales** is marginally significant (p = 0.052, just above 0.05).
- With only 5 observations, it’s hard to get very small p-values.

Would you like me to explain any specific step in more detail, or expand this to show confidence intervals next?

**Yes!** Let's continue with the **same 5-observation example** (Marketing + Sales) and calculate **Confidence Intervals** with full math.

### Current Results (from before)

| Coefficient       | β          | Std. Error | t-statistic |
|-------------------|------------|------------|-------------|
| Intercept (β₀)    | 32.6667    | 9.7923     | 3.336       |
| Marketing (β₁)    | 5.1667     | 0.4346     | 11.888      |
| Sales (β₂)        | 1.8333     | 0.4346     | 4.218       |

**Degrees of Freedom (df)** = 5 − 3 = **2**

---

### Step 14: Confidence Intervals (95%)

**Formula** for each coefficient:

$$
\text{95\% CI} = \beta_j \pm t_{\text{critical}} \times \text{SE}(\beta_j)
$$

Where **t_critical** is the value from the t-distribution table for **df = 2** and **95% confidence** (two-tailed).

**t_critical (df=2, 95%) = 4.303**

---

### Step-by-step Calculation

#### 1. For **Intercept (β₀)**

$$
\text{Margin of Error} = 4.303 \times 9.7923 \approx 42.13
$$

$$
\text{CI} = 32.6667 \pm 42.13 = [-9.46,\ 74.80]
$$

#### 2. For **Marketing (β₁)**

$$
\text{Margin of Error} = 4.303 \times 0.4346 \approx 1.87
$$

$$
\text{CI} = 5.1667 \pm 1.87 = [3.30,\ 7.04]
$$

#### 3. For **Sales (β₂)**

$$
\text{Margin of Error} = 4.303 \times 0.4346 \approx 1.87
$$

$$
\text{CI} = 1.8333 \pm 1.87 = [-0.04,\ 3.70]
$$

---

### Final Complete Table with Confidence Intervals

| Coefficient       | β        | Std. Error | t-stat   | p-value   | **95% Confidence Interval**      | Interpretation |
|-------------------|----------|------------|----------|-----------|----------------------------------|----------------|
| Intercept (β₀)    | 32.67    | 9.79       | 3.336    | 0.079     | **[-9.46, 74.80]**               | Very wide (uncertain) |
| **Marketing**     | **5.17** | 0.435      | 11.888   | **0.007** | **[3.30, 7.04]**                 | **Statistically significant** |
| Sales             | 1.83     | 0.435      | 4.218    | 0.052     | **[-0.04, 3.70]**                | Marginally significant |

---

### Simple Explanation for Students

- The **95% Confidence Interval** means:  
  “If we repeated this study many times, 95% of the time the true coefficient would fall inside this range.”

- If the interval **does NOT include zero** → the variable is statistically significant.
  - Marketing: [3.30, 7.04] → Does **not** include 0 → Strong effect.
  - Sales: [-0.04, 3.70] → Barely includes 0 → Weak evidence.

Would you like me to explain:
- How to interpret these confidence intervals in business language?
- Or show how the interval changes if we add more observations?

Just tell me what’s next!

---

