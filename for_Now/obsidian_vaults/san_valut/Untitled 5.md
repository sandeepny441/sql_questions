**Here’s a clean, Obsidian-ready explanation of backpropagation with all the key calculus equations.**

---

### How Backpropagation Works

Backpropagation is the algorithm that efficiently computes the **gradient** of the loss function with respect to every weight and bias in a neural network using the **chain rule** from calculus.

#### 1. Forward Pass
You feed the input through the network and compute the loss.

Let the network output be $\hat{y}$ and the true value be $y$.

A common loss is Mean Squared Error:
$$
L = \frac{1}{2} (\hat{y} - y)^2
$$

#### 2. Backward Pass (Backpropagation)

We want to compute:
$$
\frac{\partial L}{\partial w}
$$
for every weight $w$ in the network.

This is done layer by layer, starting from the output and moving backwards, applying the **chain rule** at each step.

---

### Core Calculus: The Chain Rule in Neural Networks

For a simple network with one hidden layer:

Let:
- $z^{(l)}$ = pre-activation of layer $l$
- $a^{(l)}$ = activation of layer $l$

Then:
$$
z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}
$$
$$
a^{(l)} = \sigma(z^{(l)})
$$

The gradient flows backwards as:

**For the output layer:**
$$
\delta^{(L)} = \frac{\partial L}{\partial z^{(L)}} = \frac{\partial L}{\partial \hat{y}} \odot \sigma'(z^{(L)})
$$

**For previous layers:**
$$
\delta^{(l)} = \left( (W^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(z^{(l)})
$$

**Gradient w.r.t. weights:**
$$
\frac{\partial L}{\partial W^{(l)}} = \delta^{(l)} (a^{(l-1)})^T
$$

**Gradient w.r.t. bias:**
$$
\frac{\partial L}{\partial b^{(l)}} = \delta^{(l)}
$$

---

### Simple 1-Neuron Example (Full Derivation)

Let’s take a single neuron:

$$
z = w x + b
$$
$$
\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}
$$
$$
L = \frac{1}{2} (\hat{y} - y)^2
$$

**Step-by-step derivatives:**

1. $\frac{\partial L}{\partial \hat{y}} = \hat{y} - y$

2. $\frac{\partial \hat{y}}{\partial z} = \sigma'(z) = \sigma(z)(1 - \sigma(z)) = \hat{y}(1 - \hat{y})$

3. $\frac{\partial L}{\partial z} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} = (\hat{y} - y) \hat{y}(1 - \hat{y})$

4. $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial w} = (\hat{y} - y) \hat{y}(1 - \hat{y}) \cdot x$

5. $\frac{\partial L}{\partial b} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial b} = (\hat{y} - y) \hat{y}(1 - \hat{y})$

This $\frac{\partial L}{\partial w}$ tells us how much changing $w$ affects the loss.

---

### Weight Update (Gradient Descent)

$$
w \leftarrow w - \eta \frac{\partial L}{\partial w}
$$
$$
b \leftarrow b - \eta \frac{\partial L}{\partial b}
$$

where $\eta$ is the learning rate.

---

### Why This is Powerful

Instead of computing each partial derivative separately (which would be exponentially expensive), backpropagation reuses intermediate gradients ($\delta$ values) by propagating them backwards through the network using the chain rule. This makes training deep networks feasible.

---

Copy and paste everything above directly into Obsidian. It should render beautifully with proper math formatting.

Want me to add:
- A full 2-layer example with numbers?
- Cross-entropy loss + softmax?
- Visual diagram description?
- More advanced topics (vanishing gradients, etc.)?

Just say the word and I’ll extend it in the same clean style.

======

**Here’s the extended version** with everything you asked for — ready to copy-paste into Obsidian.

---

### Full 2-Layer Neural Network Example (with numbers)

Let’s train a tiny network with **1 input**, **2 hidden neurons**, and **1 output**.

**Forward Pass:**

$$
z^{(1)}_1 = w^{(1)}_{11} x + b^{(1)}_1 = 0.5 \cdot 1 + 0.1 = 0.6
$$
$$
z^{(1)}_2 = w^{(1)}_{21} x + b^{(1)}_2 = -0.3 \cdot 1 + 0.2 = -0.1
$$

$$
a^{(1)}_1 = \sigma(0.6) \approx 0.6457
$$
$$
a^{(1)}_2 = \sigma(-0.1) \approx 0.4750
$$

$$
z^{(2)} = w^{(2)}_{1} a^{(1)}_1 + w^{(2)}_{2} a^{(1)}_2 + b^{(2)} = 0.4\cdot0.6457 + (-0.7)\cdot0.4750 + 0.1 \approx 0.0253
$$

$$
\hat{y} = \sigma(0.0253) \approx 0.5063
$$

Loss (MSE):
$$
L = \frac{1}{2} (\hat{y} - y)^2 = \frac{1}{2} (0.5063 - 1)^2 \approx 0.1219
$$

---

### Backpropagation Step-by-Step (Calculus)

**Output layer error:**
$$
\delta^{(2)} = \frac{\partial L}{\partial z^{(2)}} = (\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \approx (0.5063 - 1) \cdot 0.5063 \cdot 0.4937 \approx -0.1234
$$

**Gradients for output layer:**
$$
\frac{\partial L}{\partial w^{(2)}_1} = \delta^{(2)} \cdot a^{(1)}_1 \approx -0.1234 \cdot 0.6457 \approx -0.0797
$$
$$
\frac{\partial L}{\partial w^{(2)}_2} = \delta^{(2)} \cdot a^{(1)}_2 \approx -0.1234 \cdot 0.4750 \approx -0.0586
$$
$$
\frac{\partial L}{\partial b^{(2)}} = \delta^{(2)} \approx -0.1234
$$

**Hidden layer error:**
$$
\delta^{(1)}_1 = \left( w^{(2)}_1 \cdot \delta^{(2)} \right) \odot \sigma'(z^{(1)}_1) = (0.4 \cdot -0.1234) \cdot 0.6457 \cdot (1-0.6457) \approx -0.0113
$$
$$
\delta^{(1)}_2 = ( -0.7 \cdot -0.1234 ) \cdot 0.4750 \cdot (1-0.4750) \approx 0.0215
$$

**Gradients for hidden layer:**
$$
\frac{\partial L}{\partial w^{(1)}_{11}} = \delta^{(1)}_1 \cdot x \approx -0.0113 \cdot 1 = -0.0113
$$

---

### Cross-Entropy Loss + Softmax (Modern Standard)

For classification problems we usually use:

**Softmax:**
$$
\sigma(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

**Cross-Entropy Loss:**
$$
L = -\sum_{i=1}^C y_i \log(\hat{y}_i)
$$

**Beautiful simplification** (when combined with softmax):
$$
\frac{\partial L}{\partial z_i} = \hat{y}_i - y_i
$$

This is why modern networks are so efficient — the derivative becomes incredibly simple.

---

### Visual Diagram Description (for Obsidian)

```
Input Layer     Hidden Layer          Output Layer
    x ───► [z¹₁ → a¹₁] ───────┐
          [z¹₂ → a¹₂] ───────┼──► [z² → ŷ] → Loss
                             │
                       weights W²
```

---

### Advanced Topics

**Vanishing Gradient Problem**

When using sigmoid or tanh in deep networks:
$$
\sigma'(z) = \sigma(z)(1-\sigma(z)) \leq 0.25
$$

If you have 10 layers, the gradient can be multiplied by 0.25¹⁰ ≈ 9.5 × 10⁻⁷ → almost zero → learning stops.

**Solution:** ReLU activation  
$$
\operatorname{ReLU}(z) = \max(0, z) \quad \Rightarrow \quad \operatorname{ReLU}'(z) = \begin{cases} 1 & z > 0 \\ 0 & z \leq 0 \end{cases}
$$

**Exploding Gradient:** Opposite problem — solved by gradient clipping or better weight initialization (Xavier/He).

---

Copy the entire block above into Obsidian. It should look clean and beautiful with proper rendering.

Would you like:
- A 3-layer example with actual numbers?
- Code (Python + NumPy) that implements this?
- More on momentum / Adam optimizer?
- Anything else?

Just tell me what to add next!