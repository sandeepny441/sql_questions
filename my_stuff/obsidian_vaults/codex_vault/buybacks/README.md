# Mortgage Buybacks and Repurchases

This folder explains, from a UWM (United Wholesale Mortgage) lender perspective, how buybacks (repurchase demands) happen from end to end. It covers the full lifecycle: what triggers them, the contractual and operational process, the detailed math of costs and losses, how those losses are covered or mitigated, and what happens after repurchase.

It is written for intuition and practical understanding first, with explicit math using KaTeX where relevant. UWM-specific nuances (as a high-volume wholesale lender selling primarily to GSEs and government programs) are highlighted. Compliance, legal, and accounting teams should always consult current investor guides, internal policy, counsel, and auditors.

## Reading Order

1. [01-triggers-and-root-causes.md](01-triggers-and-root-causes.md)  
   What causes investors (especially Fannie Mae / Freddie Mac) to issue repurchase demands. Connection to fraud tools, QC, early payment default (EPD), and screening processes.

2. [02-reps-warrants-framework.md](02-reps-warrants-framework.md)  
   The representations and warranties (reps & warrants) that create the legal basis for buybacks. Life-of-loan vs. sunset provisions.

3. [03-buyback-process-end-to-end.md](03-buyback-process-end-to-end.md)  
   The operational timeline from demand notification through cure/rebuttal, indemnification, or repurchase. Key control points and evidence requirements.

4. [04-math-of-repurchase-price.md](04-math-of-repurchase-price.md)  
   Exact formulas and examples for calculating what UWM must pay the investor. Make-whole mechanics.

5. [05-lender-economics-loss-severity.md](05-lender-economics-loss-severity.md)  
   Full economic impact on the lender: gain-on-sale (GOS) effects, net loss calculation, scratch-and-dent market realities, carrying costs, and severity modeling.

6. [06-how-losses-are-covered.md](06-how-losses-are-covered.md)  
   How UWM (and similar wholesale lenders) actually pay for or mitigate these losses: broker recourse, internal reserves / CECL provisioning, Representations & Warranties (R&W) insurance, captive structures, and capital impact.

7. [07-post-buyback-management-and-mitigation.md](07-post-buyback-management-and-mitigation.md)  
   What happens to the repurchased loan, recovery strategies, and upstream prevention math (why strong pre-funding fraud screening and QC save money).

8. [08-sources.md](08-sources.md)  
   Official GSE guides, regulatory references, and further reading.

## The One-Sentence Version

A buyback occurs when an investor enforces its contractual right (stemming from breached representations and warranties or performance issues) to require the originating lender to repurchase a previously sold loan at a contractually defined "make-whole" price; from UWM's perspective as a wholesale lender, the financial loss is the difference between that repurchase price and the ultimate economic recovery on the loan, net of any recourse collected from brokers and any insurance recoveries, and these losses are managed through a combination of preventive QC/fraud controls, broker recourse agreements, loan loss reserves, and specialized insurance.

## Why This Matters for UWM

UWM originates tens of billions in loans monthly through the wholesale channel. Even a low buyback rate (historically in the range of 0.2%–0.6% of UPB sold, or roughly 20–60 basis points depending on vintage and economic cycle) multiplied by average loss severity of $25,000–$60,000+ per event creates material P&L and operational impact. Strong integration of fraud tools (see the sibling "Mortgage Screening Lists" folder), post-close QC, and broker accountability directly reduces the frequency and severity of these events.

