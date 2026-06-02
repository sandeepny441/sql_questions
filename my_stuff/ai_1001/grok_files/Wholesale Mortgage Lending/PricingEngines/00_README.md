# Pricing Engines — Math, Philosophy, and Business

A focused study of how **pricing engines** (PPEs) work — using **LoanSifter** as the reference mortgage example — placed in the broader historical context of how humans have priced goods, securities, and risk over time.

## Reading Order

| # | File | Focus |
|---|------|-------|
| 01 | History of Pricing | Chronological timeline of pricing systems and what each solved |
| 02 | Persistent Core Problems | The hard problems pricing has wrestled with for centuries |
| 03 | LoanSifter — Philosophy | Why LoanSifter exists, design principles, market view |
| 04 | LoanSifter — Business Functionality | What it actually does: features, workflow, integrations |
| 05 | Pricing Engine Algorithm Factors | What goes into the mathematical engine (LoanSifter / proprietary + adjacent open-source) |

## Why this folder is separate from RateSheets/

The RateSheets folder explains what a rate sheet *is*. This folder explains the **engines** that consume rate sheets at scale — turning a stack of PDFs and XML feeds from 150+ wholesale investors into a single best-execution quote in under a second.

Rate sheets are the *raw input*. PPEs are the *machine* that makes them usable.

## Quick orientation

- A pricing engine in mortgage = **Product & Pricing Engine (PPE)**
- LoanSifter (founded ~2005, acquired by Optimal Blue ~2014, now under ICE/Black Knight) is the dominant broker-channel PPE
- Major competitors / peers: Optimal Blue, Polly, EPPS (ICE Encompass), Mortech (Zillow), LenderPrice, ARIVE PPE
- No major open-source mortgage PPE exists today; closest open-source analogues are QuantLib (bond/MBS math), Drools/CLIPS (rules engines), and OR-Tools (best-ex optimization)
