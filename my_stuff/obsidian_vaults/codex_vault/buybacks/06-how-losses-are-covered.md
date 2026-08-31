# 06. How Losses Are Covered — From UWM Lender Point of View

UWM does not simply "eat" every buyback loss. As a sophisticated wholesale lender with billions in annual volume, it layers multiple mitigants. This file explains each layer with the associated math and practical considerations.

## 1. Broker / Correspondent Recourse (First Line of Defense for Wholesale)

Because UWM primarily buys closed loans from independent brokers (wholesale channel), its agreements with those brokers are critical.

Typical provisions in broker agreements:
- **Early Payment Default (EPD) Recourse**: Broker must repurchase or indemnify if the loan defaults in the first 6–12 payments and certain conditions met.
- **Fraud / Misrepresentation Recourse**: Full indemnification or buyback obligation for identity fraud, income/employment fabrication, occupancy fraud, undisclosed relationships, etc.
- **QC Defect Recourse**: For material defects discovered in post-close review that breach the reps & warrants UWM made to the investor.

**Math of Recourse Recovery**:
If UWM's net loss on a file (after all costs) is $25,000 and the broker agreement allows full recourse, UWM can demand the broker pay UWM the Repurchase Price it paid the GSE **or** the net loss amount, depending on contract wording.

**Collection rate reality**: Not 100%. Some brokers are small, go out of business, or dispute. UWM maintains broker scorecards, withholds funds, or terminates relationships for poor performers. Strong recourse language + active collection is a major profit protector.

In the earlier example, collecting $35k from the broker turned the economics positive or near-breakeven.

## 2. Representations & Warranties (R&W) Insurance

Large lenders like UWM purchase bulk or loan-level R&W insurance policies from specialty insurers (e.g., MGIC, Radian, or others in the mortgage insurance space, or dedicated R&W carriers).

**What it typically covers**:
- Certain breaches of reps & warrants leading to repurchase demands or make-whole payments (often excludes or limits fraud, intentional misrep, or "life of loan" certain defects).
- Indemnification for investor demands.
- Sometimes covers costs of cure or rebuttal.

**Policy Math & Structure** (typical terms):
- **Premium**: Paid upfront as a percentage of UPB (e.g., 8–25 bps depending on coverage breadth, lender history, loan mix). Or ongoing premium.
- **Deductible / Attachment Point**: Lender retains first $X per loan or aggregate (e.g., $10k–$50k per claim or portfolio retention).
- **Coinsurance**: Lender may share 10–25% of losses above deductible.
- **Coverage Limit**: Per loan cap (e.g., $250k–$500k) and/or aggregate limit for the policy year.
- **Exclusions**: Fraud (sometimes), compliance violations, certain property types, known defects at binding.

**Example Claim Math**:
UWM has a policy with:
- $25k per-loan deductible
- 80% coinsurance above deductible
- $400k per-loan limit

On a loan with $80k gross loss:
- Lender pays first $25k
- Remaining $55k: Insurer pays 80% = $44k
- UWM pays 20% = $11k
- **Net to UWM after insurance**: $25k + $11k = $36k (instead of $80k)

R&W insurance is **not** a complete backstop — it has gaps, especially for fraud (which is often carved out or requires proof the lender didn't know). However, it smooths earnings and protects capital on covered defects.

UWM, like peers, evaluates the cost-benefit: premium expense vs. expected loss reduction and earnings volatility protection.

## 3. Internal Loan Loss Reserves & CECL Provisioning

Under CECL (Current Expected Credit Loss) accounting, UWM must estimate and provision for expected credit losses on loans it holds, including repurchased loans and for the contingent liability of future buybacks on sold loans (to the extent not transferred).

For repurchased loans:
- Upon repurchase, the loan is recorded at fair value or amortized cost less allowance.
- A specific reserve is established for the expected loss (difference between UPB/carrying value and expected recovery).

For the sold portfolio:
- UWM models lifetime buyback probability and severity and holds reserves against the contingent exposure.

**Math impact**: Provisions hit P&L immediately when the expected loss is estimable, even before the actual buyback demand. This creates earnings volatility that insurance and recourse help dampen.

## 4. Other Mitigants

- **Captive Insurance / Reinsurance**: Some large mortgage companies have captive insurers that reinsure part of the R&W risk or self-insure certain layers. This can optimize capital and tax treatment but requires regulatory setup and risk retention.
- **Warehouse Line & Financing Structure**: Repurchase demands can trigger collateral substitution or margin calls on warehouse facilities if the loan is still financed. UWM manages liquidity buffers accordingly.
- **Pricing & Risk-Based Adjustments**: UWM can adjust SRP or pricing paid to brokers on higher-risk files or channels to build in a loss buffer.
- **Capital & Liquidity Management**: As a public company (UWMC), UWM maintains capital levels and liquidity to absorb repurchase spikes without breaching covenants or affecting operations.

## Layered Protection Summary (UWM View)

Think of it as a "waterfall" of loss absorption:

1. **Prevention** (cheapest): Robust FraudGuard-style tools + strict alert clearance + QC → fewer triggers. (See screening folder and prevention file.)
2. **Broker Recourse** (first dollar recovery): Contractual right to push loss back to the party who introduced the risk.
3. **R&W Insurance** (risk transfer for covered events): Pays after deductible/coinsurance on qualifying claims.
4. **Internal Reserves / Provisions** (self-insurance layer): Absorbs what slips through 1–3.
5. **P&L / Equity** (last resort): Ultimate hit to profitability and capital if all else insufficient.

**UWM advantage as wholesale leader**: Heavy reliance on broker recourse gives it more first-dollar protection than a retail lender that originates everything itself. Combined with scale to negotiate good R&W terms and invest in prevention technology, UWM can keep **net** loss severity well below gross repurchase economics.

The final file in this series covers what UWM does with the loan after paying the repurchase price and how upstream prevention math works.

