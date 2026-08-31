# 24 — Escrow & Cash-to-Close Math

**Prerequisite:** 17 — Amortization; 23 — Mortgage Insurance

**Goal:** Compute initial escrow deposits, monthly escrow accruals, cushion calculations under RESPA, and the full cash-to-close figure shown on the CD (Closing Disclosure).

---

## 1. Monthly Escrow Accrual

Lender collects 1/12 of annual tax + insurance with each P&I payment:

$$ \boxed{E_\text{monthly} = \frac{T + I_{ins} + \text{MI}_\text{annual} + \text{Flood} + \ldots}{12}} $$

Where each is the annual amount due.

### Worked Example
$T = \$6{,}000/\text{yr}$, $I_{ins} = \$1{,}200/\text{yr}$, flood = \$400/yr:
$$ E_\text{monthly} = \frac{6{,}000 + 1{,}200 + 400}{12} = \frac{7{,}600}{12} = \$633.33 $$

---

## 2. RESPA Cushion (Maximum Allowed)

RESPA §1024.17 allows lender to maintain a cushion in the escrow account:
$$ \text{Cushion}_\text{max} = 2 \cdot E_\text{monthly} $$

(Two months of total escrow deposit.)

### Worked Example
Using §1: Cushion ≤ $2 \cdot 633.33 = \$1{,}266.67$.

---

## 3. Initial Escrow Deposit (At Closing)

The amount collected at closing depends on when first disbursement of each item falls relative to closing date:

$$ \boxed{\text{Initial Deposit} = \sum_{i} m_i \cdot \frac{A_i}{12} + \text{Cushion}} $$

Where:
- $A_i$ = annual amount for item $i$
- $m_i$ = months until item's first disbursement after closing minus months until first mortgage payment

### Worked Example (Aggregate Analysis)
Closing date: March 15. First payment due: May 1 (so 1.5 months until first payment).
- Property tax \$6,000 due Nov 1 (8 months from closing, 6.5 from first pmt)
- Insurance \$1,200 due March 14 next year (12 months from closing, 10.5 from first pmt)

Months of tax collected at closing = 6 (so 6 monthly accruals on hand when November disbursement hits).
Months of insurance collected = 1 (only 1 month needed by next March).

Cushion: 2 months total = $2 \cdot (500 + 100) = \$1{,}200$.

$$ \text{Initial Deposit} = 6 \cdot 500 + 1 \cdot 100 + 1{,}200 = 3{,}000 + 100 + 1{,}200 = \$4{,}300 $$

(Aggregate analysis is item-by-item; this is a simplified case.)

---

## 4. Per-Diem Interest (Closing Date)

Interest from closing date to end of month, prepaid at closing:

$$ \boxed{\text{Per-Diem Interest} = L \cdot i_\text{daily} \cdot d_\text{remaining}, \qquad i_\text{daily} = \frac{r}{365}} $$

### Worked Example
$L = \$400{,}000$, $r = 6.500\%$, closing March 15 (16 days remaining in March):
$$ i_\text{daily} = 0.065/365 = 0.000178 $$
$$ \text{Per-Diem} = 400{,}000 \cdot 0.000178 \cdot 16 = \$1{,}139.73 $$

First payment May 1 covers April interest (paid in arrears).

---

## 5. Prepaid Items at Closing

Items pre-paid at closing typically include:
$$ \text{Prepaids} = \text{Per-Diem Interest} + \text{Initial Escrow Deposit} + I_{ins,\text{annual}} + \text{Property Tax (if pro-rated)} $$

If borrower pays a full year of homeowner's insurance up front (separate from escrow):
$$ \text{Insurance Prepaid} = I_{ins,\text{annual}} $$

---

## 6. Cash-to-Close (Purchase)

$$ \boxed{\text{CTC} = \text{Down Payment} + \text{Closing Costs} + \text{Prepaids} - \text{Credits} - \text{Earnest Money}} $$

### Components Broken Out
| Component | Formula |
|---|---|
| Down Payment | $V - L_\text{net of UFMIP/VAFF}$ |
| Closing Costs | Origination + title + recording + appraisal + etc. |
| Prepaids | Per-diem int + escrow deposit + insurance |
| Seller Credits | Negotiated; capped by IPC limits |
| Lender Credits | From premium pricing |
| Earnest Money | Deposit already paid pre-closing |

### Worked Example
Purchase price = $\$500{,}000$, $L = \$400{,}000$ conv 80% LTV:
| Item | Amount |
|---|---|
| Down payment | \$100,000 |
| Closing costs (origination, title, recording, etc.) | \$8,500 |
| Prepaids (per-diem int + escrow + ins.) | \$5,200 |
| Lender credit | $(\$2{,}000)$ |
| Seller credit | $(\$3{,}000)$ |
| Earnest money deposit | $(\$10{,}000)$ |
| **Cash to close** | **\$98,700** |

---

## 7. Cash-to-Close (Refinance)

$$ \text{CTC}_\text{refi} = (\text{Closing Costs} + \text{Prepaids}) - (\text{Credits}) - (L_\text{new} - L_\text{payoff} - \text{Other Liens Paid Off}) $$

If $L_\text{new} > L_\text{payoff} + \text{costs}$, borrower receives cash (cash-out refi); if less, borrower brings cash.

### Worked Example (Cash-Out)
Current loan payoff = \$280,000, new loan $L_\text{new} = \$350{,}000$, costs+prepaids = \$8,000:
$$ \text{Cash to Borrower} = 350{,}000 - 280{,}000 - 8{,}000 = \$62{,}000 $$

### Worked Example (Rate-Term)
Payoff = \$300,000, $L_\text{new} = \$300{,}000$, costs+prepaids = \$5,500, no credits:
$$ \text{CTC} = 5{,}500 - (300{,}000 - 300{,}000) = \$5{,}500 \text{ (borrower brings)} $$

---

## 8. Aggregate Adjustment (RESPA)

When the sum of monthly escrow accruals overstates required cushion at any month, lender must make a negative aggregate adjustment to reduce the initial deposit:

$$ \text{Aggregate Adj.} = -(\min_{k} \text{Projected Balance}_k - \text{Cushion}) $$

If the minimum projected balance exceeds the allowed cushion, the excess is credited back to borrower at closing.

---

## 9. Annual Escrow Analysis

Each year, lender re-analyzes the escrow account:

$$ \text{Shortage} = \text{Required Balance}_\text{lowest month} - \text{Actual Balance} - \text{Cushion} $$

If shortage > \$50, lender can:
1. Collect lump sum, or
2. Spread over 12 months added to monthly escrow

$$ \Delta E_\text{monthly} = \frac{\text{Shortage}}{12} $$

If surplus > \$50:
$$ \text{Refund to Borrower}_\$ = \text{Surplus} $$

---

## 10. Loan Estimate (LE) vs Closing Disclosure (CD) — TRID Cash-to-Close

| Section | Source |
|---|---|
| Total Closing Costs | LE Section J → CD Section J |
| Loan Amount | LE Section L |
| Cash to Close | LE/CD bottom-line calculation |

Reconciliation:
$$ \text{CTC}_\text{CD} = \text{CTC}_\text{LE} + \Delta\text{Costs} + \Delta\text{Credits} + \Delta\text{Other} $$

---

## 11. TRID Tolerance Re-Disclosure Triggers

Re-disclosure required if any of:
$$ |r_{APR,\text{LE}} - r_{APR,\text{CD}}| > 0.125\% $$
$$ \text{Product Changes} \quad \text{(e.g., fixed → ARM)} $$
$$ \text{Add Prepayment Penalty} $$

Plus 10% aggregate tolerance:
$$ \frac{\sum (\text{Actual Fees}_\text{10\% bucket}) - \sum (\text{Disclosed Fees}_\text{10\% bucket})}{\sum (\text{Disclosed Fees}_\text{10\% bucket})} > 0.10 $$

---

## 12. Sellers' Net Proceeds (Cash-to-Seller)

$$ \text{Seller Net} = \text{Sale Price} - \text{Existing Mortgage Payoff} - \text{Realtor Commission} - \text{Seller Closing Costs} - \text{Seller Credits to Buyer} $$

### Worked Example
Sale = \$500,000, existing payoff = \$220,000, 6% commission = \$30,000, seller costs = \$3,000, credits = \$3,000:
$$ \text{Seller Net} = 500{,}000 - 220{,}000 - 30{,}000 - 3{,}000 - 3{,}000 = \$244{,}000 $$

---

## 13. IPC (Interested Party Contribution) Cap

Maximum seller/builder credit:

| Program | LTV/CLTV | Cap |
|---|---|---|
| Conventional (primary/2nd home) | > 90% | 3% |
| Conventional (primary/2nd home) | 75.01–90% | 6% |
| Conventional (primary/2nd home) | ≤ 75% | 9% |
| Conventional (investment) | All | 2% |
| FHA | All | 6% |
| VA | All | 4% (plus VA-allowable) |
| USDA | All | 6% |

$$ \text{IPC}_\text{allowed} = \text{IPC \%} \cdot \min(V, \text{Sale Price}) $$

---

## 14. Summary Formula Table

| Quantity | Formula |
|---|---|
| Monthly escrow | $(T + I_{ins} + \text{MI} + \text{Flood})/12$ |
| Max cushion (RESPA) | $2 \cdot E_\text{monthly}$ |
| Per-diem interest | $L \cdot r/365 \cdot d_\text{remaining}$ |
| Initial deposit | $\sum m_i \cdot A_i/12 + \text{Cushion}$ |
| CTC (purchase) | DP + Costs + Prepaids − Credits − Earnest |
| Cash-out refi proceeds | $L_\text{new} - L_\text{payoff} - \text{Costs}$ |
| Escrow shortage | $\text{Required}_\text{lowest} - \text{Actual} - \text{Cushion}$ |
| Spread shortage / mo | $\text{Shortage}/12$ |
| APR re-disclosure trigger | $\|\Delta r_{APR}\| > 0.125\%$ |
| Seller net | $\text{Sale} - \text{Payoff} - \text{Comm} - \text{Costs} - \text{Credits}$ |
| IPC cap | $\text{IPC\%} \cdot \min(V, \text{Price})$ |
