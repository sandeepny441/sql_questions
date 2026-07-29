# **Chapter 1: Foundations of Calculus**

## **1. Functions and Mathematical Relationships**

1. What is a function?
2. Inputs and outputs
3. Domain and range
4. Graphing functions
5. Linear vs nonlinear functions
6. Polynomial, exponential and logarithmic functions

## **2. Understanding Change**

7. What is a limit?
8. Left-hand and right-hand limits
9. Infinite limits
10. What is continuity?
11. Continuous vs discontinuous functions

## **3. Derivatives — Measuring Instantaneous Change**

12. What is a derivative?
13. Derivative as slope
14. Derivative as rate of change
15. Tangent line intuition
16. Differentiation from first principles

## **4. Rules of Differentiation**

17. Power rule
18. Constant rule
19. Sum and difference rules
20. Product rule
21. Quotient rule
22. Chain rule

## **5. Common Derivatives**

23. Derivative of exponential functions
24. Derivative of logarithmic functions
25. Derivative of trigonometric functions
26. Derivative of sigmoid-like functions

## **6. Integrals — Accumulating Change**

27. What is an integral?
28. Area under the curve
29. Indefinite integrals
30. Definite integrals
31. Fundamental theorem of calculus
32. Simple integration rules

---

# **Chapter 2: Multivariable Calculus**

## **1. Functions with Many Variables**

33. Functions of multiple variables
34. Visualizing 3D surfaces
35. Scalar-valued vs vector-valued functions

## **2. Partial Derivatives**

36. What is a partial derivative?
37. Holding other variables constant
38. First-order partial derivatives
39. Second-order partial derivatives

## **3. Gradients and Directions**

40. What is a gradient?
41. Gradient as direction of steepest ascent
42. Negative gradient and descent direction
43. Magnitude of the gradient
44. Directional derivatives

## **4. Multivariable Optimization Basics**

45. Critical points
46. Stationary points
47. Local minima
48. Local maxima
49. Saddle points

## **5. Multivariable Chain Rule**

50. Small changes and total derivatives
51. Total differential
52. Multivariable chain rule
53. Nested functions and dependency flow

## **6. Function Approximation**

54. Taylor series intuition
55. Linear approximation
56. Quadratic approximation

## **7. Activation and ML-Relevant Functions**

57. Derivative of sigmoid
58. Derivative of tanh
59. Derivative of ReLU
60. Derivative of softplus
61. Why derivatives of activations matter

---

# **Chapter 3: Matrix Calculus**

## **1. Vectors and Matrices Refresher**

62. Scalars vs vectors vs matrices
63. Matrix dimensions
64. Dot products
65. Matrix multiplication
66. Transpose operations

## **2. Derivatives in Vector Form**

67. Derivative of a scalar with respect to a vector
68. Derivative of a vector with respect to a vector
69. Gradient vectors
70. Matrix-shaped derivatives

## **3. The Jacobian Matrix**

71. What is the Jacobian matrix?
72. Jacobian as stacked partial derivatives
73. Jacobians for vector-valued functions
74. Shape intuition of Jacobians

## **4. The Hessian Matrix**

75. What is the Hessian matrix?
76. Second derivatives in matrix form
77. Curvature interpretation
78. Hessian and optimization

## **5. Matrix Form of the Chain Rule**

79. Chain rule in vector notation
80. Composition of transformations
81. Gradient flow through layers

## **6. Matrix Derivatives Used in ML**

82. Derivative of a dot product
83. Derivative of matrix multiplication
84. Derivative of quadratic forms
85. Derivative of norms

## **7. Softmax and Cross Entropy**

86. What is softmax?
87. Softmax derivatives
88. What is cross-entropy loss?
89. Derivative of cross-entropy
90. Why softmax + cross-entropy work well together

---

# **Chapter 4: Derivatives and Optimization**

## **1. Optimization Fundamentals**

91. What is optimization?
92. Objective functions
93. What is a loss function?
94. Cost vs loss functions

## **2. Minimization and Learning**

95. What does minimizing a loss mean?
96. Error surfaces
97. Parameter updates
98. Iterative learning intuition

## **3. Gradient Descent**

99. What is gradient descent?
100. Batch gradient descent
101. Stochastic gradient descent (SGD)
102. Mini-batch gradient descent
103. Gradient descent as downhill walking

## **4. Learning Dynamics**

104. What is a learning rate?
105. Small vs large learning rates
106. Convergence
107. Overshooting
108. Oscillation during learning

## **5. Geometry of Optimization**

109. Convex functions
110. Non-convex functions
111. Local minimum vs global minimum
112. Saddle points
113. Flat regions and plateaus

## **6. Curvature and Second Derivatives**

114. Second derivative intuition
115. Curvature of functions
116. Positive vs negative curvature
117. Hessian-based optimization intuition

## **7. Advanced Optimization Concepts**

118. Momentum
119. Nesterov momentum
120. RMSProp
121. Adam optimizer
122. Adaptive learning rates
123. Learning rate scheduling

---

# **Chapter 5: Calculus Inside Neural Networks**

## **1. Neural Networks as Mathematical Functions**

124. Neural networks as nested functions
125. Inputs, weights and outputs
126. Weighted sums
127. Activation functions inside networks

## **2. Computational Graphs**

128. What is a computational graph?
129. Nodes and edges
130. Breaking computations into steps
131. Why graphs help differentiation

## **3. Forward Propagation**

132. What is the forward pass?
133. Computing predictions
134. Layer-by-layer transformations
135. Prediction and loss computation

## **4. Backward Propagation**

136. What is the backward pass?
137. Propagating error backward
138. Local gradients
139. Gradient flow through layers

## **5. Backpropagation**

140. What is backpropagation?
141. Applying the chain rule repeatedly
142. Backpropagation through a single neuron
143. Backpropagation through deep networks
144. Weight updates using gradients

## **6. Automatic Differentiation**

145. What is automatic differentiation?
146. Symbolic vs numerical differentiation
147. Reverse-mode autodiff
148. Why deep learning frameworks use autodiff

## **7. Training Problems in Deep Networks**

149. Vanishing gradient problem
150. Exploding gradient problem
151. Gradient instability in deep networks
152. Initialization issues

## **8. Stabilizing Deep Learning**

153. Gradient clipping
154. Batch normalization
155. Residual connections
156. Better activation functions

## **9. Why Calculus Makes Neural Networks Learn**

157. Gradients as learning signals
158. Error correction through derivatives
159. Optimization across millions of parameters
160. End-to-end learning intuition