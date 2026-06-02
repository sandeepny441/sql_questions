# 23 — Mortgage Insurance & Government Fee Math

**Prerequisite:** 17 — Amortization; 16 — Loan Ratios

**Goal:** Compute every type of mortgage-insurance premium (BPMI, LPMI, Single, Split, FHA MIP, USDA, VA funding fee) and the trigger points for cancellation.

---

## 1. When MI Is Required

| Program | Threshold | Required If |
|---|---|---|
| Conventional | LTV > 80% | Standard BPMI / LPMI |
| FHA | All loans | UFMIP + Annual MIP |
| VA | All loans | Funding fee (one-time) |
| USDA | All loans | Guarantee fee (upfront) + Annual fee |

---

## 2. BPMI (Borrower-Paid Monthly)

### Monthly Premium
$$ \boxed{\text{MI}_\text{monthly} = \frac{\text{MI Rate} \cdot L}{12}} $$

Where MI Rate is the annual factor in decimal (e.g., 0.45% = 0.0045).

### Typical Rate Card (Conv. 30Y, $\le \$726{,}200$, Standard Coverage)

| LTV | 760+ FICO | 740–759 | 720–739 | 700–719 | 680–699 | 660–679 |
|---|---|---|---|---|---|---|
| 95.01–97% | 0.45% | 0.55% | 0.85% | 1.10% | 1.45% | 1.95% |
| 90.01–95% | 0.30% | 0.40% | 0.55% | 0.75% | 1.00% | 1.30% |
| 85.01–90% | 0.20% | 0.25% | 0.35% | 0.45% | 0.60% | 0.85% |
| 80.01–85% | 0.15% | 0.17% | 0.22% | 0.30% | 0.40% | 0.55% |

### Worked Example
$L = \$300{,}000$, LTV = 95%, FICO 740, MI rate = 0.55%:
$$ \text{MI}_\text{monthly} = \frac{0.0055 \cdot 300{,}000}{12} = \frac{1{,}650}{12} = \$137.50 $$

---

## 3. BPMI Cancellation Triggers

### Borrower Right (HPA — Homeowners Protection Act)
Borrower can request cancellation when:
$$ \text{LTV based on original value} \le 80\% $$

Lender must auto-cancel when:
$$ \text{LTV based on original value} \le 78\% $$

Final termination (regardless of LTV):
$$ k = n/2 \quad \text{(midpoint of loan)} $$

### Months to Reach 80% via Amortization
Solve for $k$ in:
$$ \frac{B_k}{V_\text{original}} = 0.80 $$

Using balance formula from file 17:
$$ B_k = L \cdot \frac{(1+i)^n - (1+i)^k}{(1+i)^n - 1} = 0.80 \cdot V_\text{original} $$

---

## 4. LPMI (Lender-Paid MI)

LPMI is funded by a higher note rate, not a separate monthly premium:
$$ r_\text{LPMI} = r_\text{base} + \Delta r_\text{LPMI} $$

Typical $\Delta r_\text{LPMI}$ by LTV/FICO:

| LTV | $\Delta r$ |
|---|---|
| 95% | +25 to +50 bp |
| 90% | +15 to +35 bp |
| 85% | +10 to +25 bp |

### Single Premium LPMI Cost (Paid by Lender Out of Price)

$$ \text{LPMI Cost}_\$ = \text{LPMI Factor} \cdot L $$

Lender funds via reduced price (worse rebate or worse net price).

### Trade-Off Break-Even (BPMI vs LPMI)

$$ \text{BE}_\text{LPMI vs BPMI} = \frac{\text{Σ BPMI Saved}_\text{to cancel}}{\Delta r_\text{LPMI} \cdot L / 12 \text{ (monthly extra interest)}} $$

If borrower expects to refinance/sell before BPMI cancels at ~80% LTV (~5–8 years), LPMI often wins.

---

## 5. Single-Premium MI (Borrower or Seller Paid)

One-time up-front premium:
$$ \text{SPMI}_\$ = \text{SPMI Factor} \cdot L $$

Typical factor: 1.50% – 2.75% of loan amount.

Can be financed into loan (within LTV limits) or paid at closing.

---

## 6. Split-Premium MI

Combines up-front and monthly:
$$ \text{Up-front}_\$ = f_\text{up-front} \cdot L $$
$$ \text{MI}_\text{monthly,split} = \frac{f_\text{monthly,reduced} \cdot L}{12} $$

Lower monthly than BPMI but requires up-front payment.

---

## 7. FHA UFMIP (Up-Front Mortgage Insurance Premium)

$$ \boxed{\text{UFMIP} = 1.75\% \cdot L_\text{base}} $$

Almost always financed:
$$ L_\text{total} = L_\text{base} + \text{UFMIP} = L_\text{base} \cdot 1.0175 $$

### Worked Example
$L_\text{base} = \$300{,}000$:
$$ \text{UFMIP} = 0.0175 \cdot 300{,}000 = \$5{,}250 $$
$$ L_\text{total} = \$305{,}250 $$

---

## 8. FHA Annual MIP

$$ \text{MIP}_\text{monthly} = \frac{\text{MIP Rate} \cdot L_\text{avg outstanding}}{12} $$

Practical: lender computes monthly using current UPB (close to original).

### Rate Card (Effective March 2023)

| Loan Term | LTV | Loan Amount | Annual MIP |
|---|---|---|---|
| > 15Y | ≤ 90% | ≤ \$726,200 | 0.50% |
| > 15Y | > 90% | ≤ \$726,200 | 0.55% |
| > 15Y | ≤ 90% | > \$726,200 | 0.70% |
| > 15Y | > 90% | > \$726,200 | 0.75% |
| ≤ 15Y | ≤ 90% | ≤ \$726,200 | 0.15% |
| ≤ 15Y | > 90% | ≤ \$726,200 | 0.40% |

### Worked Example
$L = \$305{,}250$, 30Y, LTV 96.5%, rate 0.55%:
$$ \text{MIP}_\text{monthly} = \frac{0.0055 \cdot 305{,}250}{12} = \$139.91 $$

---

## 9. FHA MIP Duration

| LTV at Origination | MIP Duration |
|---|---|
| ≤ 90% | 11 years |
| > 90% | Life of loan |

For loans originated 2023+ at LTV ≤ 90%, MIP drops after 132 payments.

---

## 10. VA Funding Fee

$$ \text{VA FF} = \text{Fee Rate} \cdot L $$

### Rate Card (As of April 2023)

| Use | Down Payment | First Use | Subsequent Use |
|---|---|---|---|
| Purchase / CO Refi | 0% | 2.15% | 3.30% |
| Purchase / CO Refi | 5–10% | 1.50% | 1.50% |
| Purchase / CO Refi | ≥ 10% | 1.25% | 1.25% |
| IRRRL | N/A | 0.50% | 0.50% |

### Exempt Borrowers
- Veterans receiving disability comp
- Surviving spouses (KIA)
- Purple Heart recipients

$$ \text{VA FF}_\text{exempt} = 0 $$

### Worked Example
First-use veteran, 0% down, $L = \$400{,}000$:
$$ \text{VA FF} = 0.0215 \cdot 400{,}000 = \$8{,}600 $$

Usually financed: $L_\text{total} = 400{,}000 + 8{,}600 = \$408{,}600$.

---

## 11. USDA Guarantee Fee & Annual Fee

### Up-Front Guarantee Fee
$$ \text{USDA GF} = 1.00\% \cdot L $$

### Annual Fee
$$ \text{USDA Annual}_\text{monthly} = \frac{0.0035 \cdot L_\text{outstanding}}{12} $$

(35 bp annual; runs for life of loan.)

### Worked Example
$L = \$250{,}000$:
$$ \text{GF (upfront, financed)} = \$2{,}500 $$
$$ \text{Annual monthly} = \frac{0.0035 \cdot 250{,}000}{12} = \$72.92 $$

---

## 12. Combined Monthly Housing Payment with MI

### Conventional + BPMI
$$ \text{PITIA} = M + \frac{T}{12} + \frac{I_{ins}}{12} + \text{MI}_\text{monthly} + \text{HOA} $$

### FHA
$$ \text{PITIA}_\text{FHA} = M_\text{base} + \frac{T}{12} + \frac{I_{ins}}{12} + \text{MIP}_\text{monthly} + \text{HOA} $$

Where $M_\text{base}$ is computed on $L_\text{total} = L_\text{base} + \text{UFMIP}$.

### VA
$$ \text{PITIA}_\text{VA} = M_\text{total} + \frac{T}{12} + \frac{I_{ins}}{12} + \text{HOA} \quad \text{(no MI)} $$

Where $M_\text{total}$ is on $L_\text{base} + \text{VA FF}$.

---

## 13. Effective Rate Including MI

The "true" cost rate accounting for MI:
$$ r_\text{effective} = r + \text{MI Rate} $$

For LPMI:
$$ r_\text{effective,LPMI} = r_\text{LPMI} \quad \text{(MI already in rate)} $$

### Worked Example (Comparison)
- BPMI scenario: $r = 6.500\%$, MI 0.55% → effective ≈ 7.050%
- LPMI scenario: $r_\text{LPMI} = 6.875\%$ (no MI) → effective = 6.875%

LPMI wins by 17.5 bp.

---

## 14. MI Premium Refund Eligibility (FHA Up-Front)

If refinanced FHA-to-FHA within 36 months:
$$ \text{Refund} = \text{UFMIP} \cdot (1 - k/36) $$

Where $k$ = months since original UFMIP paid (capped at 36).

### Worked Example
UFMIP = \$5,250, refinanced at month 18:
$$ \text{Refund} = 5{,}250 \cdot (1 - 18/36) = 5{,}250 \cdot 0.50 = \$2{,}625 $$

---

## 15. Summary Formula Table

| Quantity | Formula |
|---|---|
| BPMI monthly | $\text{MI Rate} \cdot L / 12$ |
| LPMI rate adder | $r_\text{LPMI} = r + \Delta r_\text{LPMI}$ |
| SPMI cost | $\text{Factor} \cdot L$ |
| FHA UFMIP | $0.0175 \cdot L_\text{base}$ |
| FHA total loan | $L_\text{total} = L_\text{base} \cdot 1.0175$ |
| FHA monthly MIP | $\text{MIP Rate} \cdot L / 12$ |
| VA funding fee | $\text{Fee Rate} \cdot L$ |
| USDA up-front GF | $0.0100 \cdot L$ |
| USDA monthly | $0.0035 \cdot L / 12$ |
| BPMI cancel (auto) | LTV (orig) $\le 78\%$ |
| Effective rate w/ BPMI | $r + \text{MI Rate}$ |
| FHA UFMIP refund | $\text{UFMIP} \cdot (1 - k/36)$ |
