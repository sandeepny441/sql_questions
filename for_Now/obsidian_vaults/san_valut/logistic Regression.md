# **Goal of Logistic Regression**

Logistic regression predicts a probability between 0 and 1.

Example:

- “Will this loan default?”
- “Is this transaction fraud?”
- “Will this customer churn?”

Output:

- 0 → No
- 1 → Yes

---

# **Step 1 — Start Like Linear Regression**

Suppose we have:

- Income = x_1
- Debt = x_2

We first build a weighted score:

z = w_1x_1 + w_2x_2 + b

This is just a straight-line equation.

Example:

z = 0.8x_1 - 0.5x_2 + 2

Interpretation:

- Higher income increases score
- Higher debt decreases score

This z can become:

- negative
- positive
- huge numbers

Problem:  
We need probabilities between 0 and 1.

---

# **Step 2 — Convert Score into Probability**

We pass z into the sigmoid function.

$\sigma(z)=\frac{1}{1+e^{-z}}$


This squeezes every number into:

- 0 to 1

---

# **Step 3 — Understand Sigmoid Intuitively**

If:

z = -10

Probability becomes almost:

0

If:

z = 10

Probability becomes almost:

1

If:

z = 0

Probability becomes:

0.5

So:

- Negative score → likely class 0
- Positive score → likely class 1

---

# **Step 4 — Final Logistic Regression Formula**

We combine both steps:

P(y=1)=\sigma(w^Tx+b)

Meaning:

P(y=1)=\frac{1}{1+e^{-(w^Tx+b)}}

P(y=1)=\frac{1}{1+e^{-(w^Tx+b)}}

---

# **Step 5 — Example**

Suppose:

- Income = 5
- Debt = 2

Weights:

- w_1 = 0.8
- w_2 = -0.5
- b = 1

Compute score:

z = (0.8)(5) + (-0.5)(2) + 1

z = 4

Now apply sigmoid:

P(y=1)=\frac{1}{1+e^{-4}}

Result:

0.982

Meaning:

- 98.2% probability of class 1

---

# **Step 6 — How Does the Model Learn?**

The model adjusts:

- weights w
- bias b

to reduce prediction errors.

---

# **Step 7 — Why Not Use Least Squares?**

Linear regression uses:

(y-\hat y)^2

But logistic regression outputs probabilities.

So instead we use likelihood.

Idea:

- “How likely are the observed labels given our probabilities?”

---

# **Step 8 — Likelihood Intuition**

Suppose:

- Actual label = 1
- Model predicts 0.95

Good.

Suppose:

- Actual label = 1
- Model predicts 0.02

Very bad.

We want probabilities:

- close to 1 for true positives
- close to 0 for true negatives

---

# **Step 9 — Logistic Regression Loss Function**

This becomes log loss / cross entropy.

$L = -\left[y\log(p) + (1-y)\log(1-p)\right]$


$L=-\left[y\log(p)+(1-y)\log(1-p)\right]$


Where:

- y = actual label
- p = predicted probability

---

# **Step 10 — Why Logarithms?**

Logs heavily punish confident wrong predictions.

Example:

- Predict 0.99 for actual 0
- Huge penalty

This helps training.

---

# **Step 11 — Optimization**

The model uses:

- Gradient Descent

to adjust weights.

Basic idea:

1. Predict
2. Compute error
3. Compute gradients
4. Update weights
5. Repeat

---

# **Big Picture**

Linear Regression:

- predicts continuous values

Logistic Regression:

- predicts probabilities

Core flow:

\text{Features} \rightarrow \text{Linear Score} \rightarrow \text{Sigmoid} \rightarrow \text{Probability}

---

# **One-Line Intuition**

Logistic regression is:

“Linear regression whose output is squeezed into a probability using the sigmoid function.”



