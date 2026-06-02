# 16 — Loan Ratios (LTV, CLTV, HCLTV, DTI)

**Prerequisite:** 14 — Math Formulas Index

**Goal:** Compute every ratio a rate sheet's eligibility grids and LLPA tables key on. These ratios drive both pricing tiers (which row of the LLPA matrix you land on) and program eligibility (whether you qualify at all).

---

## 1. Property Value (Denominator for the LTV Family)

Agency rule:
$$ \boxed{V = \min(\text{Purchase Price}, \text{Appraised Value})} $$

For a **refinance** (no purchase contract):
$$ V = \text{Appraised Value} $$

For a **construction-to-perm**:
$$ V = \min(\text{Land Acquisition} + \text{Construction Cost}, \text{Appraised Value at Completion}) $$

---

## 2. Loan-to-Value (LTV)

$$ \boxed{\text{LTV} = \frac{L}{V}} $$

As a percentage:
$$ \text{LTV}\% = \frac{L}{V} \times 100 $$

### Worked Example
$L = \$320{,}000$, $V = \$400{,}000$:
$$ \text{LTV} = \frac{320{,}000}{400{,}000} = 0.80 = 80\% $$

### LTV Banding (Standard Agency LLPA Buckets)

| Band | Range (use lower band on boundary) |
|---|---|
| $\le 60\%$ | $L/V \le 0.60$ |
| 60.01 – 70% | $0.60 < L/V \le 0.70$ |
| 70.01 – 75% | $0.70 < L/V \le 0.75$ |
| 75.01 – 80% | $0.75 < L/V \le 0.80$ |
| 80.01 – 85% | $0.80 < L/V \le 0.85$ |
| 85.01 – 90% | $0.85 < L/V \le 0.90$ |
| 90.01 – 95% | $0.90 < L/V \le 0.95$ |
| 95.01 – 97% | $0.95 < L/V \le 0.97$ |

---

## 3. Combined Loan-to-Value (CLTV)

For a property with first lien $L_1$ and subordinate liens $L_2, L_3, \ldots, L_n$:

$$ \boxed{\text{CLTV} = \frac{\sum_{j=1}^{n} L_j}{V}} $$

For all subordinates, use the **drawn balance** (not the line limit).

### Worked Example
First lien $L_1 = \$300{,}000$, drawn HELOC $L_2 = \$50{,}000$, $V = \$500{,}000$:
$$ \text{CLTV} = \frac{300{,}000 + 50{,}000}{500{,}000} = 0.70 = 70\% $$

---

## 4. HCLTV / TLTV (High CLTV)

Like CLTV, but **HELOC line limits** (not drawn balances) are used in the numerator:

$$ \boxed{\text{HCLTV} = \frac{L_1 + \sum_{j} \max(L_j^\text{drawn},\, L_j^\text{limit})}{V}} $$

For fixed-balance seconds use the balance; for HELOCs use the line limit.

### Worked Example
$L_1 = \$300{,}000$; HELOC drawn $\$50{,}000$, limit $\$100{,}000$; $V = \$500{,}000$:
$$ \text{HCLTV} = \frac{300{,}000 + 100{,}000}{500{,}000} = 0.80 = 80\% $$

---

## 5. Debt-to-Income (DTI)

### Front-End (Housing-Only)
$$ \text{DTI}_\text{front} = \frac{\text{PITI} + \text{HOA} + \text{MI}}{I_\text{gross,monthly}} $$

### Back-End (Total Debt)
$$ \boxed{\text{DTI}_\text{back} = \frac{\text{PITI} + \text{HOA} + \text{MI} + \sum \text{Other Debts}}{I_\text{gross,monthly}}} $$

"Other debts" includes:
- Minimum credit card payments
- Auto loans / leases
- Student loan payments (IBR or amortizing — agency-specific)
- Installment loans (the greater of stated payment or final 10 months)
- Child support / alimony
- Co-signed loans not paid by another party for 12+ months

### Worked Example
- PITI = \$2,400, HOA = \$150, MI = \$120
- Auto = \$450, Min CC = \$80, Student = \$200
- Gross monthly income = \$8,000

$$ \text{DTI}_\text{back} = \frac{2{,}400 + 150 + 120 + 450 + 80 + 200}{8{,}000} = \frac{3{,}400}{8{,}000} = 0.425 = 42.5\% $$

---

## 6. Components of PITI

$$ \boxed{\text{PITI} = M + \frac{T}{12} + \frac{I_{ins}}{12}} $$

Where:
- $M$ = monthly P&I (from amortization, file 17)
- $T$ = annual property tax
- $I_{ins}$ = annual hazard insurance premium

Add mortgage insurance and HOA for the qualifying payment:
$$ \text{PITIA} = M + \frac{T}{12} + \frac{I_{ins}}{12} + \text{MI}_\text{monthly} + \text{HOA} $$

---

## 7. Gross Monthly Income — By Source

### Salaried
$$ I_\text{gross} = \frac{\text{Annual Salary}}{12} $$

### Hourly (full-time, 40 hr/week assumed)
$$ I_\text{gross} = \text{Hourly Rate} \times 40 \times \frac{52}{12} = \text{Hourly Rate} \times 173.33 $$

### Hourly (variable hours, 24-month average)
$$ I_\text{gross} = \frac{\sum_\text{24 mo} \text{Gross Pay}}{24} $$

### Self-Employed (Two-Year Average)
$$ I_\text{gross} = \frac{\text{Yr1 Adj. Income} + \text{Yr2 Adj. Income}}{24} $$

If most recent year is **lower** than prior year, use:
$$ I_\text{gross} = \frac{\text{Most Recent Yr Adj. Income}}{12} $$

### Bonus / Commission / Overtime
$$ I_\text{variable} = \frac{\sum_\text{24 mo} \text{Variable Pay}}{24} $$

Use only if income trend is flat or increasing; declining trend → use lower figure.

### Rental Income (Existing Property)
$$ I_\text{rental,qualifying} = (\text{Gross Rents}) \times 0.75 - \text{PITI of that property} $$

The 0.75 multiplier is the standard 25% vacancy/maintenance factor.

---

## 8. Residual Income (VA Loans)

$$ \text{Residual} = I_\text{net,monthly} - \text{PITI} - \text{Other Debts} - \text{Maintenance} - \text{Utilities} $$

Where:
- $I_\text{net,monthly}$ = gross income minus federal/state taxes & FICA
- Maintenance ≈ \$0.14/ft² (varies by region)
- Utilities use VA tables

Residual must meet or exceed VA's published table by region, family size, and loan amount.

---

## 9. Reverse: Solve for Loan Amount Given Target LTV

$$ L = V \cdot \text{LTV}_\text{target} $$

### Worked Example
Borrower wants 80% LTV on a \$500k home:
$$ L = 500{,}000 \times 0.80 = \$400{,}000 $$
Down payment = $V - L = \$100{,}000$.

---

## 10. Reverse: Solve for Income Needed Given Target DTI

$$ I_\text{gross,required} = \frac{\text{PITI} + \text{Other Debts}}{\text{DTI}_\text{max}} $$

### Worked Example
PITI = \$2,500, other debts = \$700, target DTI = 43%:
$$ I_\text{required} = \frac{2{,}500 + 700}{0.43} = \frac{3{,}200}{0.43} \approx \$7{,}442\,\text{/month} $$

---

## 11. Reverse: Solve for Max PITI Given Income & Target DTI

$$ \text{PITI}_\text{max} = I_\text{gross} \cdot \text{DTI}_\text{max} - \text{Other Debts} $$

### Worked Example
$I = \$9{,}000$, $\text{DTI}_\text{max} = 0.45$, other debts = \$500:
$$ \text{PITI}_\text{max} = 9{,}000 \cdot 0.45 - 500 = 4{,}050 - 500 = \$3{,}550 $$

---

## 12. Reverse: Max Loan Amount From Max PITI (back through amortization)

Given $\text{PITI}_\text{max}$, $T$, $I_{ins}$, $r$, $n$:

Step 1 — extract max $M$:
$$ M_\text{max} = \text{PITI}_\text{max} - \frac{T}{12} - \frac{I_{ins}}{12} $$

Step 2 — invert amortization (see file 17):
$$ L_\text{max} = M_\text{max} \cdot \frac{(1+i)^n - 1}{i\,(1+i)^n} $$

---

## 13. Summary Formula Table

| Quantity | Formula |
|---|---|
| Property value | $V = \min(\text{Price}, \text{Appraisal})$ |
| LTV | $L / V$ |
| CLTV | $\sum L_j / V$ |
| HCLTV | $\bigl(L_1 + \sum \max(\text{drawn}, \text{limit})\bigr) / V$ |
| Front DTI | $(\text{PITI} + \text{HOA} + \text{MI}) / I_\text{gross}$ |
| Back DTI | $(\text{PITI} + \text{HOA} + \text{MI} + \text{Debts}) / I_\text{gross}$ |
| PITI | $M + T/12 + I_{ins}/12$ |
| Loan from target LTV | $L = V \cdot \text{LTV}$ |
| Income from target DTI | $I = (\text{PITI} + \text{Debts}) / \text{DTI}$ |
| Max PITI from income | $\text{PITI} = I \cdot \text{DTI} - \text{Debts}$ |
| Rental qualifying income | $0.75 \cdot \text{Gross Rents} - \text{PITI}_\text{rental}$ |
| VA residual | $I_\text{net} - \text{PITI} - \text{Debts} - \text{Maint.} - \text{Util.}$ |
