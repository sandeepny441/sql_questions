# Simplest Backpropagation Math

We will use:

- 1 input
- 1 weight
- 1 prediction
- 1 loss

Goal:

Learn how the weight updates.

---

# Step 1 — Input

Suppose:

$$
x = 2
$$

Weight:

$$
w = 3
$$

True answer:

$$
y = 10
$$

---

# Step 2 — Forward Pass

Prediction formula:

$$
\hat{y} = wx
$$

Substitute:

$$
\hat{y} = 3 \times 2
$$

$$
\hat{y} = 6
$$

Prediction is:

$$
6
$$

Actual answer is:

$$
10
$$

Model is wrong.

---

# Step 3 — Loss Function

Use Mean Squared Error:

$$
L = (y-\hat{y})^2
$$

Substitute:

$$
L = (10-6)^2
$$

$$
L = 4^2
$$

$$
L = 16
$$

Large error.

---

# Step 4 — Main Goal of Backpropagation

We want:

$$
\frac{dL}{dw}
$$

Meaning:

> "How much does loss change if weight changes?"

This is the gradient.

---

# Step 5 — Chain Rule

We know:

$$
L = (y-\hat{y})^2
$$

and:

$$
\hat{y} = wx
$$

Loss depends on prediction.

Prediction depends on weight.

So we use:

$$
\frac{dL}{dw}
=
\frac{dL}{d\hat{y}}
\times
\frac{d\hat{y}}{dw}
$$

This is backpropagation.

---

# Step 6 — First Derivative

Loss:

$$
L=(y-\hat{y})^2
$$

Derivative:

$$
\frac{dL}{d\hat{y}}
=
-2(y-\hat{y})
$$

Substitute:

$$
=-2(10-6)
$$

$$
=-8
$$

---

# Step 7 — Second Derivative

Prediction:

$$
\hat{y}=wx
$$

Derivative wrt weight:

$$
\frac{d\hat{y}}{dw}=x
$$

Since:

$$
x=2
$$

we get:

$$
\frac{d\hat{y}}{dw}=2
$$

---

# Step 8 — Multiply Them

Chain rule:

$$
\frac{dL}{dw}
=
(-8)(2)
$$

$$
=-16
$$

Gradient:

$$
-16
$$

---

# Meaning of Negative Gradient

Negative means:

> Increase the weight.

Because increasing weight will reduce loss.

---

# Step 9 — Gradient Descent Update

Update rule:

$$
w_{new}
=
w_{old}
-
\eta
\frac{dL}{dw}
$$

Where:

$$
\eta
$$

is learning rate.

Suppose:

$$
\eta=0.1
$$

Substitute:

$$
w_{new}
=
3
-
0.1(-16)
$$

$$
=
3+1.6
$$

$$
=
4.6
$$

Weight updated.

---

# Step 10 — New Prediction

Now:

$$
w=4.6
$$

Prediction:

$$
\hat{y}=4.6 \times 2
$$

$$
=9.2
$$

Closer to:

$$
10
$$

Loss reduced.

Model improved.

---

# Core Idea of Backpropagation

Backpropagation is simply:

1. Make prediction
2. Compute error
3. Compute derivatives
4. Send gradients backward
5. Update weights

Repeat many times.

---

# Most Important Equation

$$
\frac{dL}{dw}
=
\frac{dL}{d\hat{y}}
\times
\frac{d\hat{y}}{dw}
$$

This is the heart of backpropagation.

---

# Slightly Bigger Example

Neuron:

$$
z = w_1x_1 + w_2x_2 + b
$$

Activation:

$$
a = \sigma(z)
$$

Sigmoid:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Loss:

$$
L=(y-a)^2
$$

Backprop:

$$
\frac{dL}{dw_1}
=
\frac{dL}{da}
\times
\frac{da}{dz}
\times
\frac{dz}{dw_1}
$$

This is repeated layer-by-layer in neural networks.

---

# Common Derivatives Used

## Linear

$$
\frac{d}{dx}(x)=1
$$

---

## Power Rule

$$
\frac{d}{dx}(x^2)=2x
$$

---

## Sigmoid Derivative

If:

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Then:

$$
\sigma'(x)=\sigma(x)(1-\sigma(x))
$$

---

## ReLU

$$
ReLU(x)=\max(0,x)
$$

Derivative:

$$
ReLU'(x)=
\begin{cases}
1 & x>0 \\
0 & x\le0
\end{cases}
$$

---

# Intuition

Backpropagation asks:

> "Which weight caused how much error?"

Then slightly adjusts each weight to reduce future error.