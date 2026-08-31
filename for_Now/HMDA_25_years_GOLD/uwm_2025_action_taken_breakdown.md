# United Wholesale Mortgage — 2025 HMDA action-taken breakdown

UWM LEI: `549300HW662MN1WU8550`

## 2025 totals

The 2025 UWM HMDA file contains **578,838 records**. This is the full LAR record count for UWM, including purchased-loan records reported under action code 6.

| HMDA action code | Category | Records | Share of UWM records |
|---:|---|---:|---:|
| 1 | Loan originated | 422,120 | 72.93% |
| 2 | Approved but not accepted | 10,283 | 1.78% |
| 3 | Application denied | 69,523 | 12.01% |
| 4 | Application withdrawn by applicant | 54,820 | 9.47% |
| 5 | File closed for incompleteness | 19,964 | 3.45% |
| 6 | Loan purchased by the institution | 2,128 | 0.37% |
| **Total** | **All UWM HMDA records** | **578,838** | **100.00%** |

## How to interpret correspondent loan purchases

The **422,120 originated loans** are the loans UWM reported as originated under action code 1. The **2,128 action-code-6 records are not additional UWM originations**. They represent loans UWM acquired after closing (or repurchased) when UWM did not make the original credit decision. That population may include correspondent acquisitions, but HMDA does not identify the warehouse-line or funding arrangement behind a particular loan.

Therefore:

- For UWM’s closed/originated-loan volume, use **422,120**.
- Do **not** add action code 6 to originated loans when measuring UWM production.
- Add action code 6 separately only when measuring UWM’s total HMDA-reported acquisition activity; do not treat it as a generic correspondent-loan measure.

If a broker such as Imperium took the application but UWM was the creditor that made the credit decision and funded/closed the loan, HMDA would generally place that loan in UWM’s action-code-1 production. A later sale to the secondary market does not change that original action code; it is captured separately in HMDA’s type-of-purchaser field when applicable. HMDA alone cannot confirm whether a specific loan used a UWM warehouse line.

The total record count is useful for describing all HMDA activity associated with UWM, but it should not be labeled “loans closed by UWM.”

Source: verified 2025 annual HMDA Parquet file in `hmda_yearly_analysis_2007_to_2025`, filtered to UWM LEI `549300HW662MN1WU8550`.

## Monthly-count limitation

The public 2025 HMDA LAR data used for this table contain `activity_year`, but do **not** contain an action-taken date (or any month field). Therefore, monthly counts for January through December cannot be derived reliably from this file. Any monthly allocation of the annual totals would be an assumption, not an HMDA observation.

To produce a true monthly table, we would need a source that includes the action/closing date—such as UWM's internal loan-level data, a permitted non-public HMDA extract, or another dated production report. The annual totals above remain fully verifiable from the public HMDA file.
