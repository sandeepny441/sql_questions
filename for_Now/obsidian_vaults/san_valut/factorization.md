**Muon Optimizer — Core Mathematical Components**

### 1. Momentum Accumulation (Nesterov-style)
$$
\mathbf{M}_t = \mu \mathbf{M}_{t-1} + \nabla \mathcal{L}(\mathbf{W}_{t-1})
$$

### 2. Newton-Schulz Orthogonalization
Start with:
$$
\mathbf{X}_0 = \frac{\mathbf{M}_t}{\|\mathbf{M}_t\|_F}
$$

Iterative update (quintic):
$$
\mathbf{X}_{k} = a \mathbf{X}_{k-1} + b \, (\mathbf{X}_{k-1}\mathbf{X}_{k-1}^T)\mathbf{X}_{k-1} + c \, (\mathbf{X}_{k-1}\mathbf{X}_{k-1}^T)^2 \mathbf{X}_{k-1}
$$

Typical coefficients:  
$a \approx 3.4445$, $b \approx -4.7750$, $c \approx 2.0315$  
(5–10 iterations)

Final orthogonalized direction:
$$
\mathbf{O}_t \approx \mathbf{X}_N \quad (\approx UV^T \text{ from SVD of } \mathbf{M}_t)
$$

### 3. Scaled Weight Update
$$
\mathbf{W}_t = \mathbf{W}_{t-1} - \eta \Bigl( \gamma \cdot \mathbf{O}_t + \lambda \mathbf{W}_{t-1} \Bigr)
$$

Where:  
- $\eta$: learning rate  
- $\gamma$: shape-dependent scaling ($\approx \sqrt{\max(n,m)}$ or RMS-matched)  
- $\lambda$: weight decay coefficient

These three blocks (momentum → Newton-Schulz → scaled update) constitute the complete core of Muon.π