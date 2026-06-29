# 05. Lender Economics and Loss Severity (UWM Perspective)

Paying the Repurchase Price is only the starting point. From UWM's viewpoint as a wholesale lender, the true economic loss is almost always larger than the headline repurchase price because of:

- Reversal or provisioning against prior Gain-on-Sale (GOS)
- The repurchased loan's depressed recovery value (especially if defective or now delinquent)
- Operational, legal, and carrying costs
- Potential impact on future sale pricing or GSE relationship

This file walks through the full math of loss severity.

## Simplified Economic Loss Equation for a Repurchased Loan

\text{Net Economic Loss to UWM} = (\text{Repurchase Price} - \text{Recovery Value}) + \text{Operational & Legal Costs} + \text{Carrying Costs} + \text{GOS Recapture / Provision} - \text{Broker Recourse Collected} - \text{Insurance Recovery}






Where each term is defined below with realistic UWM-scale examples.

### 1. Repurchase Price (already covered)
See previous file. Example: **$401,500**

### 2. Recovery Value (what UWM ultimately gets back)
After taking the loan back, UWM has options:
- Cure the defect (if curable) and re-sell to another investor or in scratch-and-dent market.
- Modify the loan and hold or sell as reperforming.
- If seriously delinquent or fraudulent: pursue foreclosure, short sale, or deed-in-lieu and sell the REO.
- In worst case (identity theft, total fraud): limited recovery.

**Typical recovery ranges (illustrative, based on industry data for defective loans)**:
- Clean, curable loan re-sold quickly: 97–99% of UPB
- Minor defect, sold in scratch-and-dent: 90–95% of UPB
- Credit-impaired or delinquent: 75–88% of UPB
- Fraud / major collateral issue or REO: 50–70% of UPB (after foreclosure costs)

**Example continuation**:
UWM pays $401,500, takes back a now 2-month delinquent loan with some documentation issues. After cure attempts fail or are uneconomic, UWM sells it in the scratch-and-dent market for **$378,000** (roughly 95% of original UPB, discounted for defect + delinquency + market conditions).

**Recovery Value = $378,000**

### 3. Operational, Legal & Carrying Costs
- Legal / compliance response to demand: $2,000 – $8,000 typical
- QC re-review, broker communication, evidence gathering: $1,000 – $5,000
- Carrying cost on the $401,500 (warehouse interest or opportunity cost) for 60–180 days until resolution/sale: depends on rates, but at 6–8% annual, ~$2,000 – $5,000+ for a few months
- Potential foreclosure costs if pursued: $5k–$15k+

**Example total add-on costs: ~$8,000**

### 4. Gain-on-Sale (GOS) Recapture / Accounting Impact
When UWM originally sold the loan at a premium (e.g., 101.25), it booked GOS including the premium + any SRP.

Accounting rules (ASC 860 for transfers of financial assets) and auditor practice often require:
- Reversal of previously recognized GOS if the transfer is no longer considered a true sale due to the repurchase obligation, **or**
- Establishment of a specific reserve / ALLL (Allowance for Loan and Lease Losses) or CECL provision against the repurchased loan or for the expected loss.

In practice for repurchase events, UWM recognizes an immediate loss equal to the difference between carrying value (often close to UPB or repurchase price) and fair value, plus any required GOS adjustment.

For modeling, many lenders treat a portion of the original premium as at risk of recapture on buyback loans.

**Illustrative impact**: Original GOS on this loan might have been ~$8,000–$12,000 (premium + fees net of costs). On buyback, UWM may have to reverse $4,000–$8,000 of that or provision equivalently.

### 5. Broker Recourse Collected (Critical for Wholesale Lenders like UWM)
UWM buys loans from independent mortgage brokers. Many broker agreements include **recourse** or **indemnification** provisions for:
- Early Payment Default (EPD)
- Fraud or misrepresentation
- Certain QC defects

If the root cause traces to broker-submitted data or the broker, UWM can often require the broker to:
- Buy the loan back from UWM at the same (or similar) price UWM paid the GSE, **or**
- Indemnify UWM for the net loss.

**Example**: UWM collects **$35,000** from the originating broker under the recourse agreement.

This is a major mitigant for wholesale lenders.

### 6. Insurance Recovery (R&W Insurance)
If UWM has Representations & Warranties insurance covering this type of defect (not all fraud or all defects are covered; policies have exclusions, waiting periods, deductibles), it may recover a portion after claim process.

**Example**: $15,000 recovered from R&W carrier (after deductible/coinsurance).

## Putting It Together — Full Example Loss Severity

Using the running example:

| Component                        | Amount          | Notes |
|----------------------------------|-----------------|-------|
| Repurchase Price paid to Fannie  | +$401,500      | Contractual obligation |
| Recovery from scratch-and-dent sale | -$378,000   | What UWM actually receives |
| Operational + Legal + Carrying   | +$8,000        | Real costs |
| GOS Recapture / Provision        | +$6,000        | Accounting / economic adjustment |
| **Subtotal before mitigants**    | **+$37,500**   | Gross loss |
| Broker Recourse Collected        | -$35,000       | From originating broker |
| R&W Insurance Recovery           | -$15,000       | Partial claim payout |
| **Net Economic Loss to UWM**     | **-$12,500**   | **Net after all** |

In this case, strong broker recourse and insurance turned a potential ~$37k gross loss into a manageable ~$12.5k net loss.

If no broker recourse was available (e.g., internal origination or weak agreement) and no insurance, net loss could easily exceed $40k–$50k on a single file.

## Portfolio-Level Severity Math (UWM Scale)

UWM models at scale:

- **Buyback Rate**: e.g., 0.40% of UPB sold (40 bps) or ~4–5 loans per 1,000 sold (varies by vintage, channel, economic conditions).
- **Average Severity (gross)**: $30,000 – $55,000 per repurchased loan (industry studies show ~$32k average in recent periods).
- **Net Severity after recourse/insurance**: Often 30–60% lower depending on recourse strength and insurance attachment.

**Expected Loss (EL)** modeling:

\[
\text{EL} = \text{UPB Sold} \times \text{Buyback Rate} \times \text{Average Net Severity}
\]

For $50 billion annual production at 40 bps buyback rate and $25k average net severity:

\[
\text{EL} \approx \$50\text{B} \times 0.0040 \times \$25{,}000 = \$5\text{M per year}
\]

This is why UWM invests heavily in fraud tools, QC, and broker management — reducing the buyback rate by even 10–20 bps or improving recourse collection by 20% has multi-million dollar annual impact.

## Key Takeaway for UWM

Loss severity is highly variable and heavily influenced by:
1. Strength of broker recourse agreements and collection discipline.
2. Quality of pre-funding fraud screening and alert clearance (prevention beats cure).
3. Having R&W insurance with broad coverage and efficient claims process.
4. Operational efficiency in post-demand cure/rebuttal and rapid disposition of repurchased loans.

The next file details exactly how these coverage mechanisms work in practice.

