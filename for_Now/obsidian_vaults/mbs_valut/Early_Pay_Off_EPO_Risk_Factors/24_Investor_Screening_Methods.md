# Investor Screening Methods (How Buyers Detect EPO Risk Pre-Purchase)

## Loan-Level Tape Analysis
When bidding on a bulk pool or flow purchase, investors compute per-loan EPO scores:

- Compute **SATO** for each loan (note rate vs. market at lock date).
- Flag high SATO + high FICO combos.
- Flag low-point / lender-credit loans.
- Flag refi loans (especially rate/term recent-refi patterns).
- Flag FHA/VA (streamline-refi eligible).
- Flag high-balance loans in low-rate environments.

## Segmentation Overlays
- Investor's approved-seller list has **per-seller EPO haircuts**.
- Per-channel adjustments (broker/wholesale/correspondent).
- Per-state adjustments (trigger lead intensity, HPI).

## Data Providers Used
- **Recursion Cognitive / Recursion**: agency data, prepay analytics.
- **Optimal Blue / ICE**: pricing/rate benchmarks.
- **Corelogic, ATTOM**: property/borrower history.
- **NMLS**: LO IDs, licensing.
- Internal EPO databases.

## Post-Purchase Verification
- Some aggregators do **rapid re-underwriting** on random samples.
- QC teams pull credit re-pulls at day 30 to catch competitor loan applications.

## Model Outputs
- Predictive EPO score per loan.
- Pool-level expected EPO % → premium bid haircut.
- Segments with predicted EPO > threshold are excluded from bid or bid at par only.

## Related
- [[26_Data_and_Modeling_Approaches]]
- [[01_Loan_Rate_and_SATO]]
- [[21_Lender_EPO_History]]
