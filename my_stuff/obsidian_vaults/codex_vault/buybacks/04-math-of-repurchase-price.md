# 04. The Math of the Repurchase Price

This is the core contractual math. When Fannie Mae or Freddie Mac (or other investors) demands repurchase, they specify a **Repurchase Price** (sometimes called "make-whole amount") that is designed to put the investor in the same economic position as if the loan had never been sold or had remained in their portfolio/MBS.

From UWM's perspective, this is **not** a market-value transaction. It is a contractual obligation. Understanding the exact components is essential for modeling potential exposure and for negotiating or rebutting demands where possible.

## Fannie Mae / Freddie Mac Repurchase Price Components (Active Loan)

Based on official Selling and Servicing Guides (see sources), the repurchase price for an active (non-liquidated) mortgage loan typically includes:

$$
\begin{aligned}
\text{Repurchase Price} ={}& \text{UPB} + \text{Accrued Interest} + \text{Advances} \\
&+ \text{GSE Expenses} + \text{Other Amounts Due} \\
&- \text{Credits / Payments Received}
\end{aligned}
$$

Where:

- **UPB** = Current Unpaid Principal Balance as of the repurchase settlement date (or a specified cutoff).
- **Accrued Interest** = Interest accrued at the **note rate** (not the pass-through rate) from the last paid installment date through the repurchase date. This can be material if the loan is delinquent.
- **Advances** = Any principal or interest advances the servicer/GSE made that have not been recovered, plus escrow advances for taxes/insurance.
- **GSE Expenses** = Property preservation, maintenance, marketing, legal, or other expenses incurred by the GSE (more relevant if the property went into REO or foreclosure process before repurchase demand).
- **Other Amounts Due** = Fees, penalties, or other contractual amounts owed under the Lender Contract.
- **Credits / Payments** = Any principal/interest payments or other credits the GSE received that reduce the amount owed.

**Important notes from GSE guidance**:
- Loan-Level Price Adjustments (LLPAs) paid at delivery are generally **not** refunded or included in the repurchase price calculation in a way that benefits the lender on repurchase.
- The price is **not** reduced to current market value of the loan or property. The GSE does not take a "haircut" for market conditions; the lender bears that risk.
- For loans that have been liquidated (foreclosed or short sale), the demand is often for a **make-whole payment** equal to the amount the GSE would have received had the loan performed, including any loss on the property disposition.

Freddie Mac example phrasing (from Guide): The repurchase price is calculated as the UPB (including negative amortization if applicable) plus accrued interest at the applicable mortgage interest rate, plus other amounts due.

## Concrete Numerical Example (UWM Wholesale Loan)

Assume a typical wholesale-originated loan UWM sold to Fannie Mae:

- Original Loan Amount: \$400,000
- Note Rate: 6.50%
- Sold to Fannie Mae at: 101.25 (premium) + SRP (servicing release premium, assume captured at sale)
- Months since sale when demand issued: 8 months
- Current UPB at demand: \$397,200 (some amortization + any curtailments)
- Loan is 2 payments delinquent at time of demand
- Accrued interest owed to Fannie (simplified, ignoring exact day count): ~\$4,300 (2 months interest roughly)
- Fannie has made no property advances yet (loan still active, borrower-occupied per file)
- No other fees/expenses

**Repurchase Price UWM must pay**:

$$
\begin{array}{lr}
\text{UPB} & \$397{,}200 \\
+ \text{Accrued Interest (note rate)} & \$4{,}300 \\
+ \text{Advances / Expenses} & \$0 \\
\hline
\text{Total Repurchase Price} & \$401{,}500
\end{array}
$$

UWM pays Fannie Mae approximately **\$401,500** to take the loan back.

Note: Even though UWM originally received ~\$405,000 at sale (101.25 on \$400k), it does **not** get to "give back" only the net economics. It pays the full contractual amount.

## Additional Math Considerations

### Delinquency Impact
If the loan is seriously delinquent, accrued interest + advances grow. A 6-month delinquent loan can add tens of thousands in interest + escrow advances.

### Make-Whole on Liquidated Loans
If the property has already been foreclosed and sold by the GSE for a loss:

$$
\begin{aligned}
\text{Make-Whole Payment} ={}& \text{UPB at liquidation} \\
&+ \text{Accrued Interest \& Advances to liquidation} \\
&+ \text{GSE's Net Loss on REO Sale} + \text{Costs}
\end{aligned}
$$

The lender is essentially reimbursing the GSE's realized loss plus opportunity cost.

### Partial vs. Full Repurchase
Sometimes GSEs offer alternatives (e.g., fee in lieu of repurchase for certain curable defects, or indemnification instead of full buyback). These have their own math — see later files on loss mitigation.

### Time Value of Money for UWM
UWM must fund the \$401,500 repurchase (often via warehouse line or cash). While the loan is on UWM's books, it incurs carrying cost at its cost of funds (warehouse spread + any hedge costs). This is real economic drag until the loan is cured/re-sold or liquidated.

## Why This Math Favors Strong Prevention

A single unresolved FraudGuard employment or occupancy alert that leads to a buyback can cost UWM \$30k–\$80k+ in net loss (repurchase price minus recovery, plus operational costs, minus any broker recourse collected). See the economics file for full severity modeling.

UWM's scale makes even small improvements in clearance discipline or fraud tool integration produce outsized financial returns through avoided repurchase prices.

Next files will layer on the **net loss to UWM** after paying this price and what happens to the loan afterward.
