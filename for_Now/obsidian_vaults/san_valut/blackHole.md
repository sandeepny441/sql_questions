# Black Hole Mathematics

Comprehensive overview of the core math behind black holes — formatted for **Obsidian**.

---

## 1. Einstein’s Field Equations

$$
G_{\mu\nu} = 8\pi T_{\mu\nu}
$$

**In vacuum** (outside the black hole, \( T_{\mu\nu} = 0 \)):

$$
G_{\mu\nu} = 0
$$

---

## 2. Schwarzschild Metric (Non-rotating, Uncharged Black Hole)

$$
ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right)c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta \, d\phi^2
$$

### Key Radii
- **Event Horizon (Schwarzschild Radius)**:
  $$
  r_s = \frac{2GM}{c^2}
  $$

- **Photon Sphere**: \( r = \frac{3}{2} r_s \)
- **ISCO** (Innermost Stable Circular Orbit): \( r = 3 r_s \)

---

## 3. Kerr Metric (Rotating Black Hole)

$$
ds^2 = -\left(1 - \frac{2Mr}{\Sigma}\right) dt^2 - \frac{4Mar \sin^2\theta}{\Sigma} dt d\phi + \frac{\Sigma}{\Delta} dr^2 + \Sigma d\theta^2 + \left(r^2 + a^2 + \frac{2Ma^2 r \sin^2\theta}{\Sigma}\right) \sin^2\theta \, d\phi^2
$$

Where:
- \( \Sigma = r^2 + a^2 \cos^2\theta \)
- \( \Delta = r^2 - 2Mr + a^2 \)
- \( a = \frac{J}{M} \) (spin parameter)

### Horizons
- Outer (Event Horizon): \( r_+ = M + \sqrt{M^2 - a^2} \)
- Inner (Cauchy Horizon): \( r_- = M - \sqrt{M^2 - a^2} \)

---

## 4. Black Hole Thermodynamics (Bekenstein-Hawking)

**Hawking Temperature**:

$$
T_H = \frac{\hbar c^3}{8\pi G M k_B}
$$

**Bekenstein-Hawking Entropy**:

$$
S = \frac{k_B c^3 A}{4 \hbar G} = \frac{A}{4 \ell_P^2}
$$

Where \( A = 4\pi r_s^2 \) is the horizon area and \( \ell_P = \sqrt{\frac{\hbar G}{c^3}} \) is the Planck length.

**Surface Gravity** (Schwarzschild):

$$
\kappa = \frac{c^2}{2 r_s}
$$

---

## 5. First Law of Black Hole Mechanics

$$
dM = \frac{\kappa}{8\pi} dA + \Omega \, dJ + \Phi \, dQ
$$

---

## Quick Reference Table

| Black Hole Type       | Parameters       | Horizon Formula                     |
|-----------------------|------------------|-------------------------------------|
| Schwarzschild         | M                | \( r_s = 2M \)                      |
| Reissner-Nordström    | M, Q             | \( r_\pm = M \pm \sqrt{M^2 - Q^2} \) |
| Kerr                  | M, a             | \( r_+ = M + \sqrt{M^2 - a^2} \)    |
| Kerr-Newman           | M, a, Q          | More complex                        |

---

> **Tip**: In Obsidian, enable **MathJax** in Settings → Editor if equations aren't rendering.

Copy and paste the whole block above into a new note. Everything is cleanly formatted with proper headings, spacing, and LaTeX blocks for perfect Obsidian rendering.

Would you like me to reorganize any section, add more derivations, or make separate notes for each metric?