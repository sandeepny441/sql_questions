# 01. Triggers and Root Causes of Buyback Demands

From a UWM lender point of view, a buyback demand is almost never random. It is the downstream consequence of something that was either missed or misrepresented upstream in origination, underwriting, or the sale to the investor.

## Primary Trigger Categories

### 1. Early Payment Default (EPD) / Performance Triggers
Investors (especially GSEs) often review loans that become 60+ or 90+ days delinquent shortly after sale (typical look-back windows: first 6–12 payments, sometimes longer for certain defects).

Common root causes UWM sees:
- Income or employment fabrication / overstatement (ties directly to FraudGuard employment/income alerts that were not fully cleared).
- Occupancy misrep (borrower claimed primary residence but data showed investment intent or undisclosed other properties — see occupancy alerts in FraudGuard materials).
- Credit or capacity issues not properly mitigated.

**UWM operational reality**: High-volume wholesale channel means reliance on broker-submitted packages. Strong pre-funding fraud tools and QC sampling reduce EPD buybacks dramatically.

### 2. Quality Control (QC) / Post-Close Audit Findings
Both UWM's internal QC and investor/GSE QC sample loans (often 10%+ for new sellers or high-risk channels, lower for well-performing ones).

Defect types that commonly lead to repurchase demands:
- **Income / Employment defects** (most frequent per industry studies): Inability to verify income, employer verification failures, related-party employment not disclosed.
- **Appraisal / Collateral defects**: Unsupported value, appraisal independence issues, property condition or flip concerns (see Property/Valuation alerts in the screening materials).
- **Identity / Misrepresentation**: SSN issues, identity theft indicators, undisclosed relationships between borrower/seller/appraiser/broker (Transaction Relationship alerts).
- **Documentation or data integrity**: Altered documents, conflicting information across 1003/ transcripts / title, etc.
- **Eligibility / Program compliance**: FHA/VA/USDA issues, or GSE-specific requirements.

These often surface because pre-funding FraudGuard-style tools flagged something that was "cleared" too lightly, or because new data (tax transcripts, post-close reverification) contradicts the file.

### 3. Fraud or Material Misrepresentation Discovered Later
Fraud can be latent:
- Straw buyer / nominee patterns.
- Inflated income that looked reasonable at origination but fails deep dive.
- Property flipping schemes or undisclosed flip profits.
- Undisclosed liabilities or relationships.

Fraud tools (identity, occupancy, employment, transaction relationship) are the primary upstream defense. If a FraudGuard alert was escalated and properly resolved with independent verification, the chance of a later buyback on that issue drops sharply.

### 4. Servicing-Related or Other Triggers
- Borrower complaints or disputes that reveal origination issues.
- Title defects or lien issues discovered in servicing or payoff.
- Changes in borrower circumstances that prompt investor review.
- GSE or investor periodic reviews / targeted audits.

## Connection to the Screening & Fraud Tools Folder

The materials in the sibling folder on OFAC, FraudGuard, exclusions, and hit handling are **preventive controls** precisely because unresolved issues there become buyback root causes here.

Example linkage:
- An unresolved "Borrower appears connected to employer ownership" FraudGuard alert that was not independently verified → later QC finds related-party income inflation → repurchase demand.
- An occupancy alert cleared only with borrower letter (weak) instead of lease termination docs + relocation evidence → EPD + QC finds investment property intent → buyback.

**UWM lesson**: Every dollar spent on robust pre-funding fraud screening and strict clearance standards has a high ROI in avoided buyback losses, operational friction, and reputational risk with investors and warehouse lenders.

## Why "End to End" Understanding Matters

A buyback is not just "pay the money back." It triggers:
- Operational cost (responding to demand, gathering evidence, cure attempts).
- Financial loss (detailed in later files).
- Potential recourse collection from the originating broker (key for wholesale lenders like UWM).
- Possible impact on UWM's seller/servicer status, pricing with GSEs, or warehouse line covenants.
- Accounting provisions and capital considerations.

Understanding the root causes lets UWM focus prevention where it has the highest leverage: strong broker onboarding and ongoing monitoring, tight integration of fraud tools into underwriting workflow, risk-based QC sampling, and clear escalation protocols for alerts.

In short: Most buybacks are preventable with disciplined upstream controls. The math later in this folder shows exactly why that discipline pays.

