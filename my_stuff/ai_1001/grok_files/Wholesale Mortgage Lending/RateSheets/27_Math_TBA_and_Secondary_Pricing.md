# 27 — TBA & Secondary Market Pricing Math

**Prerequisite:** 15 — Price/Rate/BP; 26 — SRP & MSR

**Goal:** Read TBA quotes in 32nds, compute the dollar roll, value specified-pool pay-ups, and translate TBA prices into rate-sheet base prices for the originator.

---

## 1. TBA Quote Notation

A TBA price like $\boxed{99\text{-}24+}$ decodes to:
$$ 99 + \frac{24}{32} + \frac{1}{64} = 99 + 0.75 + 0.015625 = 99.765625 $$

| Symbol Suffix | Meaning |
|---|---|
| `24` | 24/32 |
| `24+` | 24/32 + 1/64 |
| `24 1/4` | 24/32 + 1/128 (rare) |

### Converting 32nds → Decimal
$$ P_\text{dec} = \text{handle} + \frac{n}{32} + \frac{\text{plus or quarter}}{64\text{ or }128} $$

### Converting Decimal → 32nds
$$ n_{32} = \text{round}(P_\text{frac} \cdot 32) $$

---

## 2. TBA Coupon Stack

The active TBA market trades fixed coupons in 50 bp increments. As of any given day, a handful are liquid:

| Pool Coupon | Note Rate Range Eligible |
|---|---|
| 5.0 | 5.00% – 5.99% |
| 5.5 | 5.50% – 6.49% |
| 6.0 | 6.00% – 6.99% |
| 6.5 | 6.50% – 7.49% |

Loan delivers into the highest pool coupon $c^*$ such that:
$$ r - s - g \ge c^* $$

Where $s$ = servicing, $g$ = guarantee fee.

---

## 3. Coupon Selection (Net to Investor)

$$ \boxed{c_\text{net} = r - s - g} $$

Round down to nearest 50 bp pool coupon:
$$ c_\text{pool} = 0.5 \cdot \lfloor 2 c_\text{net} \rfloor $$

### Worked Example
$r = 6.625\%$, $s = 0.25\%$, $g = 0.50\%$:
$$ c_\text{net} = 6.625 - 0.25 - 0.50 = 5.875\% $$
$$ c_\text{pool} = 0.5 \cdot \lfloor 2 \cdot 5.875 \rfloor / 100 = 0.5 \cdot \lfloor 11.75 \rfloor / 100 = 0.055 = 5.5\% $$

Loan goes into 5.5 coupon pool. Excess servicing = $5.875 - 5.5 = 0.375\%$ (75 bp).

---

## 4. Note Rate → Base Price Mapping

The lender's base price for a given rate is approximately:
$$ \boxed{P_\text{base}(r) = P_\text{TBA}(c_\text{pool}) + \text{Excess Strip Value} + \text{SRP} - \text{Margin} - \text{Hedge Cost}} $$

### Excess Strip Value
$$ \text{Excess Strip Value (price points)} \approx \frac{c_\text{net} - c_\text{pool}}{\text{Discount Rate} + \text{CPR}} $$

### Worked Example
$P_\text{TBA}(5.5) = 99\text{-}24 = 99.750$. Excess strip 0.375%, discount 10%, CPR 12%:
$$ \text{Excess Strip} \approx \frac{0.375}{22} = 1.70 \text{ points} $$

Add SRP ~1.00 points, subtract margin & hedge cost ~0.75 points:
$$ P_\text{base} \approx 99.750 + 1.70 + 1.00 - 0.75 = 101.700 $$

---

## 5. The Dollar Roll

Selling current-month TBA and buying next-month TBA simultaneously:
$$ \boxed{\text{Roll} = P_\text{front} - P_\text{back}} $$

Or as $\text{drop}$ (more common terminology):
$$ \text{Drop} = P_\text{front} - P_\text{back} $$

A positive drop ⇒ front month richer (typical when financing rates < coupon).

### Roll Implied Financing Cost
$$ \text{Implied Financing} \approx c - \left(\text{Drop} \cdot \frac{12}{\text{Days}}\right) \cdot \frac{360}{P} $$

Where $c$ = coupon, Days = days between settlements.

---

## 6. Specified Pool Pay-Ups

Specified pools (with desirable prepayment characteristics) trade above TBA:
$$ \boxed{P_\text{spec} = P_\text{TBA} + \text{Pay-Up}} $$

### Common Specified-Pool Categories & Typical Pay-Ups

| Story | Why Premium | Pay-Up (rough) |
|---|---|---|
| Low Loan Balance ($\le \$110k$) | Slower prepay (refi math weak) | 50–150 bp |
| Med Loan Balance ($\le \$150k$) | Slower prepay | 25–75 bp |
| NY / High-Cost State | Tax friction slows refi | 25–60 bp |
| Investor Property | Higher rate, less refi sensitivity | 50–150 bp |
| FICO < 700 | Refi credit-constrained | 30–80 bp |
| 100% HARP | Government program; no refi | 100–200 bp |

---

## 7. WAC (Weighted Average Coupon) Adjustment

For seasoned pools with WAC ≠ coupon:
$$ \text{Pool Premium} \approx (\text{WAC} - \text{Coupon}) \cdot \text{WAL} - \text{Prepay Hit} $$

---

## 8. Cash Window Pricing

Fannie/Freddie cash-window prices via their pricing engines:
$$ P_\text{cash} = P_\text{TBA} + \text{Cash Premium} - \text{Cash Discount} $$

Cash premium reflects: cleaner execution, no roll risk, but smaller dollar amounts.

Typical cash vs MBS: cash is competitive on small flows (< \$1M/month per coupon), MBS wins above.

---

## 9. AOT (Assignment of Trade)

A hedger sells loans to an investor and assigns the hedge TBA position:
$$ \text{AOT Net to Investor} = P_\text{whole-loan} - P_\text{TBA assigned} $$

Equivalent loan-level price:
$$ P_\text{loan} = P_\text{TBA} + \text{Whole-Loan Spread} + \text{SRP} $$

---

## 10. Mandatory Delivery Improvement

Forward mandatory commitments price better than best-efforts:
$$ P_\text{mand} = P_\text{best-eff} + \Delta_\text{mand} $$

Typical $\Delta_\text{mand} \approx 25\text{-}50$ bp.

Trade-off: pair-off fee if loan doesn't close.

---

## 11. Pair-Off Math

If the originator can't deliver against a mandatory commitment:
$$ \boxed{\text{Pair-Off Fee} = (P_\text{commitment} - P_\text{market today}) \cdot \text{Notional}} $$

If market is worse (prices fell), commitment is worth more than current market → originator pays a fee equal to the gain forgone by the investor.

### Worked Example
Committed at $P = 100.500$ on \$2M notional. Market today $P = 100.000$:
$$ \text{Pair-Off} = (100.500 - 100.000) \cdot 0.01 \cdot 2{,}000{,}000 = \$10{,}000 \text{ owed} $$

---

## 12. Settlement Date Convention (TBA)

TBA settlement follows Class A/B/C cycle:
- Class A: 1st settlement day of month
- Class B: 2nd settlement day
- Class C: 3rd settlement day

Notification date for pools: 48 hours before settlement (the "48-hour rule").

---

## 13. Forward Price Curve

The future-month TBA price depends on financing carry:
$$ P_\text{forward} = P_\text{spot} - \left( \frac{c}{12} - \frac{r_\text{repo}}{12} \right) \cdot P_\text{spot} $$

When carry is positive ($c > r_\text{repo}$), forward is below spot (front month worth more = "drop").

---

## 14. OAS (Option-Adjusted Spread) — Conceptual

$$ \text{MBS Price} = \sum_\text{paths} \frac{\sum_k \text{CF}_k}{(1 + r_k + \text{OAS})} $$

OAS is the spread that, added to risk-free rates along each interest-rate path, makes the model price match the market price. Adjusts for prepayment option.

Typical agency OAS: 30–60 bp.

---

## 15. Summary Formula Table

| Quantity | Formula |
|---|---|
| 32nds → decimal | $\text{handle} + n/32 + \text{plus}/64$ |
| Net coupon to investor | $c_\text{net} = r - s - g$ |
| Pool coupon | $c_\text{pool} = 0.5 \cdot \lfloor 2 c_\text{net} \rfloor$ |
| Excess strip value | $(c_\text{net} - c_\text{pool}) / (d + \text{CPR})$ |
| Base price | $P_\text{TBA} + \text{Excess} + \text{SRP} - \text{Margin} - \text{Hedge}$ |
| Dollar roll / drop | $P_\text{front} - P_\text{back}$ |
| Specified pool | $P_\text{spec} = P_\text{TBA} + \text{Pay-Up}$ |
| Mandatory uplift | $P_\text{mand} = P_\text{best-eff} + 25\text{-}50\text{bp}$ |
| Pair-off fee | $(P_\text{commit} - P_\text{today}) \cdot \text{Notional}$ |
| Forward price | $P_\text{spot} \cdot (1 - (c - r_\text{repo})/12)$ |
| OAS (definition) | spread making model price = market price |
