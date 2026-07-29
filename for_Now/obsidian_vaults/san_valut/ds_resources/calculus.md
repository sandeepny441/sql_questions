# **Chapter 1: Core Calculus Foundations**

1. What is a function?
2. What is a limit?
3. What is continuity?
4. What is a derivative?
5. Derivative as rate of change
6. Power rule
7. Product rule
8. Chain rule
9. What is an integral?
10. Definite vs indefinite integrals

---

# **Chapter 2: Multivariable Calculus and Matrix Calculus**

11. Functions with multiple variables
12. What is a partial derivative?
13. What is a gradient?
14. Directional derivatives
15. Multivariable chain rule
16. Vector-valued functions
17. The Jacobian matrix
18. The Hessian matrix
19. Derivative of matrix multiplication
20. Taylor series intuition

---

# **Chapter 3: Optimization for Machine Learning**

21. What is a loss function?
22. What does minimizing loss mean?
23. What is gradient descent?
24. What is a learning rate?
25. Local minimum vs global minimum
26. Saddle points
27. Convex vs non-convex functions
28. Second derivative and curvature
29. Momentum and adaptive learning rates
30. Why gradients help models learn

---

# **Chapter 4: Calculus Inside Neural Networks**

31. What is a computational graph?
32. Forward pass
33. Backward pass
34. What is backpropagation?
35. Chain rule inside backpropagation
36. What is automatic differentiation?
37. Derivatives of sigmoid and ReLU
38. Vanishing gradient problem
39. Exploding gradient problem
40. Why calculus powers neural networks

# **Chapter 5: Important Mathematical Functions Used in Machine Learning**

1. Sigmoid Function
2. Tanh Function
3. ReLU (Rectified Linear Unit)
4. Leaky ReLU
5. Softmax Function
6. Probit Function
7. Gaussian Function
8. Logarithmic Function
9. Exponential Function
10. Swish / GELU Functions

| #   | Function                  | What it does                                                                | Output range       | Where used         |
| --- | ------------------------- | --------------------------------------------------------------------------- | ------------------ | ------------------ |
| 1   | ==**Step function**==     | Outputs 1 if input is positive, 0 otherwise — a hard on/off switch          | {0, 1}             | activation         |
| 2   | ==**Sigmoid**==           | Squashes any number into a smooth curve between 0 and 1                     | (0, 1)             | output             |
| 3   | ==**Tanh**==              | Like sigmoid but centred at zero — outputs between −1 and 1                 | (−1, 1)            | activation         |
| 4   | ==**ReLU**==              | Keeps positive values as-is, turns all negatives to zero                    | [0, ∞)             | activation         |
| 5   | ==**Leaky ReLU**==        | Like ReLU but lets a tiny fraction through for negative inputs              | (−∞, ∞)            | activation         |
| 6   | ==**Softmax**==           | Turns a list of numbers into probabilities that all add up to 1             | (0, 1) — sums to 1 | output             |
| 7   | ==**Logit**==             | Inverse of sigmoid — converts a probability back to an unconstrained number | (−∞, ∞)            | inverse / link     |
| 8   | ==**Probit**==            | Uses the normal distribution curve as a threshold instead of log-odds       | (−∞, ∞)            | inverse / link     |
| 9   | ==**Log-softmax**==       | Takes the log of softmax — numerically stable form used in loss functions   | (−∞, 0)            | output             |
| 10  | ==**Linear / identity**== | Passes input through unchanged — used when no squashing is needed           | (−∞, ∞)            | regression / other |
![[01_step_function.png]]

![[02_sigmoid.png]]

![[03_tanh.png]]

![[04_relu.png]]

![[05_leaky_relu.png]]

![[06_softmax.png]]

![[08_probit.png]]

![[07_logit.png]]

![[10_linear_identity.png]]

![[09_log_softmax.png]]

![[overview.png]]