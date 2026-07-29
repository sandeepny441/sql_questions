# Autoencoders — Part 1: The Building Blocks

An **autoencoder** is a neural network trained to do something that sounds useless at first: reproduce its own input. Feed it `x`, ask it to output `x̂ ≈ x`. The trick is that the data must pass through a **narrow bottleneck** on the way, so the network is forced to learn a *compressed representation* of the data.

```
x  ──►  [ ENCODER ]  ──►  z (bottleneck)  ──►  [ DECODER ]  ──►  x̂
        compress            small code           decompress
```

There are five building blocks. We'll walk through each with a single running numerical example so you can verify every number by hand.

---

## The Running Example

One input vector with 4 features (imagine a tiny 2×2 image, pixel values in [0, 1]):

```
x = [1, 0, 1, 0]
```

We'll compress it to a 2-dimensional code, then reconstruct all 4 values.
Architecture: **4 → 2 → 4**.

---

## Block 1: The Encoder

The encoder is just one (or more) standard neural network layers that map the input to a smaller vector:

$$
a^{(1)} = W_1 x + b_1
$$

- `W₁` is a **2 × 4** weight matrix (2 outputs, 4 inputs)
- `b₁` is a bias vector (we'll use zeros to keep the arithmetic clean)

**Hand math.** Let

```
W₁ = [  0.5  -0.2   0.3   0.1 ]
     [ -0.4   0.6   0.2  -0.1 ]
```

Multiply row by row against `x = [1, 0, 1, 0]`:

```
a₁ = (0.5)(1) + (-0.2)(0) + (0.3)(1) + (0.1)(0) =  0.8
a₂ = (-0.4)(1) + (0.6)(0) + (0.2)(1) + (-0.1)(0) = -0.2
```

Pre-activation output of the encoder:

$$
a^{(1)} = [\,0.8,\; -0.2\,]
$$

Notice the dimensionality already dropped: 4 numbers went in, 2 came out. That's the compression happening — each output is a *weighted mixture* of all input features.

---

## Block 2: The Activation Function (Non-linearity)

A pure matrix multiply is linear, and stacking linear layers stays linear. To learn interesting structure we squash each value through a non-linear function. We'll use the **sigmoid**:

$$
\sigma(t) = \frac{1}{1 + e^{-t}}
$$

**Hand math.**

```
σ(0.8)  = 1 / (1 + e⁻⁰·⁸)  = 1 / (1 + 0.4493) = 0.690
σ(-0.2) = 1 / (1 + e⁰·²)   = 1 / (1 + 1.2214) = 0.450
```

A useful fact we'll need later for gradients:

$$
\sigma'(t) = \sigma(t)\,\bigl(1 - \sigma(t)\bigr)
$$

(ReLU, `max(0, t)`, is the more common modern choice, but sigmoid keeps the demo output in [0, 1].)

---

## Block 3: The Latent Code (Bottleneck)

The activated encoder output **is** the latent code:

$$
z = \sigma(W_1 x + b_1) = [\,0.690,\; 0.450\,]
$$

This is the heart of the autoencoder:

- It has **fewer dimensions than the input** (2 < 4), so the network *cannot* simply copy the input through. It must decide what information is worth keeping.
- The space of all possible `z` vectors is called the **latent space**. After training, similar inputs land near each other in this space — the network has invented its own coordinate system for the data.

Think of it as forcing someone to describe a photo in exactly two numbers. They'll be forced to pick the two most informative properties.

---

## Block 4: The Decoder

The decoder mirrors the encoder: it expands the code back to the original size.

$$
a^{(2)} = W_2 z + b_2, \qquad \hat{x} = \sigma\!\left(a^{(2)}\right)
$$

`W₂` is **4 × 2**. Importantly, `W₂` is a *new* set of learned weights — the decoder must learn to *decompress* on its own.

**Hand math.** Let

```
W₂ = [  0.6  -0.3 ]
     [ -0.2   0.5 ]
     [  0.4   0.1 ]
     [  0.1  -0.4 ]
```

Multiply against `z = [0.690, 0.450]`:

```
a₁ = (0.6)(0.690) + (-0.3)(0.450) =  0.414 − 0.135 =  0.279
a₂ = (-0.2)(0.690) + (0.5)(0.450) = −0.138 + 0.225 =  0.087
a₃ = (0.4)(0.690) + (0.1)(0.450)  =  0.276 + 0.045 =  0.321
a₄ = (0.1)(0.690) + (-0.4)(0.450) =  0.069 − 0.180 = −0.111
```

Apply the sigmoid to each:

```
x̂₁ = σ(0.279)  = 0.569
x̂₂ = σ(0.087)  = 0.522
x̂₃ = σ(0.321)  = 0.580
x̂₄ = σ(-0.111) = 0.472
```

Reconstruction:

$$
\hat{x} = [\,0.569,\; 0.522,\; 0.580,\; 0.472\,]
\quad \text{vs.} \quad
x = [\,1,\; 0,\; 1,\; 0\,]
$$

With random-ish weights, the reconstruction is mush — everything near 0.5. That's expected. The next two blocks are how it gets better.

---

## Block 5: The Reconstruction Loss

We need a single number measuring "how wrong is `x̂`?" The standard choice for continuous data is **Mean Squared Error**:

$$
L = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{x}_i)^2
$$

**Hand math** (n = 4):

```
(1 − 0.569)² = (0.431)²  = 0.1858
(0 − 0.522)² = (−0.522)² = 0.2725
(1 − 0.580)² = (0.420)²  = 0.1764
(0 − 0.472)² = (−0.472)² = 0.2228
                  sum    = 0.8575
L = 0.8575 / 4           = 0.214
```

Note what this loss is **not**: there are no labels. The target is the input itself. This is why autoencoders are called **self-supervised** — the data supervises itself.

---

## Block 6: Learning — Backpropagation & Gradient Descent

Training = nudge every weight in the direction that reduces `L`:

$$
w \leftarrow w - \eta \,\frac{\partial L}{\partial w}
$$

where `η` is the learning rate. Let's hand-compute the gradient for **one** decoder weight, `W₂[1,1] = 0.6` (the weight connecting `z₁` to the first output). The chain rule breaks the path into three links:

$$
\frac{\partial L}{\partial W_2[1,1]}
= \underbrace{\frac{\partial L}{\partial \hat{x}_1}}_{\text{loss → output}}
\cdot
\underbrace{\frac{\partial \hat{x}_1}{\partial a_1}}_{\text{output → pre-act}}
\cdot
\underbrace{\frac{\partial a_1}{\partial W_2[1,1]}}_{\text{pre-act → weight}}
$$

**Link 1 — loss w.r.t. output:**

$$
\frac{\partial L}{\partial \hat{x}_1} = \frac{2}{n}(\hat{x}_1 - x_1) = \frac{2}{4}(0.569 - 1) = -0.216
$$

**Link 2 — sigmoid derivative:**

$$
\frac{\partial \hat{x}_1}{\partial a_1} = \hat{x}_1(1 - \hat{x}_1) = 0.569 \times 0.431 = 0.245
$$

**Link 3 — pre-activation w.r.t. weight:** since `a₁ = W₂[1,1]·z₁ + W₂[1,2]·z₂`,

$$
\frac{\partial a_1}{\partial W_2[1,1]} = z_1 = 0.690
$$

**Multiply the chain:**

```
∂L/∂W₂[1,1] = (−0.216)(0.245)(0.690) ≈ −0.0365
```

**Update** with learning rate η = 0.1:

```
W₂[1,1] ← 0.6 − (0.1)(−0.0365) = 0.6037
```

The gradient is negative, so the weight *increases* — which makes sense: `x̂₁ = 0.569` was too low (target was 1), and `z₁ = 0.690` is positive, so strengthening this connection pushes `x̂₁` up. The same chain rule, extended one layer deeper, updates the encoder weights `W₁` too. Repeat over thousands of examples and the mush sharpens into faithful reconstructions.

---

## Building-Block Summary

| # | Block | Formula | Role |
|---|-------|---------|------|
| 1 | Encoder | `a = W₁x + b₁` | Compress input |
| 2 | Activation | `σ(t)` | Add non-linearity |
| 3 | Latent code | `z = σ(W₁x + b₁)` | The bottleneck / learned representation |
| 4 | Decoder | `x̂ = σ(W₂z + b₂)` | Decompress code |
| 5 | Loss | `L = ‖x − x̂‖²/n` | Measure reconstruction error |
| 6 | Backprop | `w ← w − η ∂L/∂w` | Learn |

➡️ **Part 2** ties these into one unified picture: why the bottleneck matters, what the network is *really* learning, and where autoencoders lead (PCA, denoising, VAEs).
