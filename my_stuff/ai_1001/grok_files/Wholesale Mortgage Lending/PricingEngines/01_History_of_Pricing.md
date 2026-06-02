# 01 — A History of Pricing

**Purpose:** Place mortgage rate-sheet pricing in the long arc of how humans have priced *anything*. Every era introduced a new pricing mechanism to solve a *specific* problem. Modern PPEs (LoanSifter, Optimal Blue, Polly) sit at the end of that lineage and inherit problems from each stage.

---

## Timeline at a glance

| Era | Pricing Mechanism | Core Problem It Solved |
|---|---|---|
| Pre-3000 BCE | Barter | How to exchange goods with no common medium |
| 3000 BCE – 600 BCE | Commodity money (grain, metals) | Double-coincidence-of-wants problem |
| 600 BCE | Coinage (Lydia) | Trust in weight/purity at point of trade |
| Antiquity – Medieval | Just Price (Aquinas) | Moral framework to prevent exploitation |
| 16–18th c. | Mercantilism / Guild prices | State revenue & guild monopoly protection |
| 18–19th c. | Classical economics (cost / labor theory) | Explain prices from production inputs |
| 1870s | Marginalist revolution | Why diamonds > water (subjective utility) |
| 1890s | Marshallian supply-and-demand equilibrium | Unified framework: price as intersection |
| 1900s–1950s | Posted / sticker pricing (retail) | Scale of mass-market commerce |
| 1968–1972 | Yield management / dynamic pricing (airlines) | Maximize revenue from perishable inventory |
| 1973 | Black–Scholes options pricing | Consistent price for contingent claims |
| 1968–1985 | Mortgage securitization → MBS pricing | Tie loan price to capital-markets execution |
| 1990s | Internet retail dynamic pricing | Real-time adjustment to demand |
| 1996–2005 | Mortgage PPEs (Optimal Blue, LoanSifter) | Aggregate fragmented investor rate sheets |
| 2008+ | Risk-based pricing via LLPAs | Align price to credit-risk granularity |
| 2010s+ | ML-driven personalized pricing | Per-customer price discrimination at scale |
| 2015+ | Cloud-native, API-first PPEs (Polly) | Sub-second pricing across many investors |

---

## 1. Barter (pre-3000 BCE)

**Mechanism**: Direct goods-for-goods exchange.
**Core problem solved**: How do strangers exchange value without trust infrastructure?
**Limit it exposed**: The double-coincidence-of-wants — both parties must want what the other has, *now*. Made specialization impossible.

## 2. Commodity Money (~3000 BCE – 600 BCE)

**Mechanism**: Use a universally desired commodity (grain in Mesopotamia, cocoa in Mesoamerica, copper rings in Egypt) as a unit of account.
**Core problem solved**: Eliminated double-coincidence — anyone would take the commodity.
**Limit it exposed**: Bulky, variable quality, perishable.

## 3. Coinage (~600 BCE, Lydia under King Croesus)

**Mechanism**: State-stamped metal coins of certified weight and purity.
**Core problem solved**: Trust in the medium itself — no need to weigh or assay at each trade.
**Limit it exposed**: Counterfeiting, debasement by sovereigns (a recurring problem for 2,500 years).

## 4. Just Price Doctrine (Antiquity → 13th-c. Scholasticism)

**Mechanism**: Aristotle, Aquinas, scholastic theologians argue price should reflect "natural worth" — fair to seller's labor and buyer's need, not exploitative of either.
**Core problem solved**: Moral/legal framework to prevent usury, hoarding, and price gouging in famines.
**Limit it exposed**: No mechanism to *compute* the just price; reduced to subjective rulings by courts/guilds.

## 5. Mercantilism & Guild-Set Prices (~1500–1750)

**Mechanism**: Trade guilds, royal monopolies (East India Companies), and bullion-accumulation policies fix prices by edict, with the goal of national treasure accumulation.
**Core problem solved**: Coordinated state revenue extraction, protection of guild members from underbidding.
**Limit it exposed**: Black markets, smuggling, and the inefficiency of fixed prices in dynamic conditions.

## 6. Classical Economics — Labor / Cost-of-Production Theory (1776 → 1870s)

**Mechanism**: Adam Smith (1776), Ricardo (1817), J.S. Mill — price ≈ cost of production, especially labor input.
**Core problem solved**: A *theory* connecting prices to something objective and computable (inputs used).
**Limit it exposed**: Cannot explain why diamonds, with low labor input, cost more than water; cannot explain prices that diverge from cost (luxury goods).

## 7. The Marginalist Revolution (1870s)

**Mechanism**: Jevons (England), Menger (Vienna), Walras (Lausanne) — independently propose that price emerges from *marginal* (last-unit) utility to the consumer.
**Core problem solved**: Explained the diamond-water paradox; turned pricing from "objective cost" into a subjective-equilibrium problem.
**Limit it exposed**: Requires modeling each buyer's preferences — computationally intractable in 1880.

## 8. Marshallian Supply-and-Demand Equilibrium (1890)

**Mechanism**: Alfred Marshall, *Principles of Economics* — price is the intersection of aggregate supply and aggregate demand curves. The "scissors of supply and demand."
**Core problem solved**: A *graphical, teachable, calculable* framework that unified cost-of-production (supply side) with marginal utility (demand side).
**Still the dominant framework** in every undergraduate textbook 130 years later.
**Limit it exposed**: Assumes equilibrium, full information, homogeneous goods — all of which break in real markets.

## 9. Posted Retail Pricing (1850s–present)

**Mechanism**: Department stores (Wanamaker's 1876, Macy's) introduce the *price tag* — same price for everyone, no haggling.
**Core problem solved**: Scaled retail operations beyond what one-on-one negotiation could handle.
**Limit it exposed**: Left margin on the table by ignoring willingness-to-pay differences.

## 10. Yield Management / Dynamic Pricing (1972 → 1985 → today)

**Mechanism**: Kenneth Littlewood (BOAC, 1972) develops the first overbooking model. American Airlines launches DINAMO (Dynamic Inventory Allocation and Maintenance Optimizer) in 1985 — different prices for the same seat depending on time-to-departure, fare class, and remaining inventory.
**Core problem solved**: Maximize revenue from *perishable inventory* (a seat empties at takeoff; a hotel room at midnight).
**Direct ancestor of**: hotel pricing, car rental pricing, ride-share surge pricing, and — by analogy — *intraday rate-sheet repricing* in mortgages.

## 11. Black–Scholes & the Derivatives Revolution (1973)

**Mechanism**: Fischer Black, Myron Scholes, Robert Merton publish a closed-form formula to price European options:
$$ C = S N(d_1) - K e^{-rt} N(d_2) $$
**Core problem solved**: A *consistent, replicable* price for contingent claims (options, derivatives) based on no-arbitrage.
**Why it matters here**: Mortgage-backed securities contain an embedded option (the borrower's right to prepay). Pricing MBS requires Black-Scholes-style option-adjusted spread (OAS) math, which flows back into rate-sheet base pricing.

## 12. Mortgage Securitization & MBS Pricing (1968 → present)

| Year | Event |
|---|---|
| 1968 | Ginnie Mae chartered as separate from Fannie Mae |
| 1970 | Ginnie issues first MBS; Freddie Mac chartered |
| 1981 | Fannie Mae issues first MBS |
| 1983 | First CMO (Collateralized Mortgage Obligation, Freddie) |
| 1985 | TBA (To-Be-Announced) market matures into the dominant agency MBS execution |
| 2008 | Conservatorship of Fannie/Freddie; LLPAs introduced |
| 2019 | UMBS (Uniform MBS) replaces separate Fannie/Freddie pools |

**Core problem solved at each stage**: Connecting individual loan origination to capital-markets execution. Each step pushes pricing complexity *down* into the rate sheet a broker sees.

## 13. Mortgage Pricing Engines — The Birth of PPEs

| Year | Event |
|---|---|
| ~1996 | Optimal Blue founded (Plano, TX); early secondary-marketing tool |
| 2002 | Optimal Blue launches retail PPE |
| ~2005 | LoanSifter founded by Pat Welch (Wisconsin); broker-channel PPE |
| ~2008 | Post-crisis LLPA explosion makes manual sheet-shopping impractical |
| 2014 | LoanSifter acquired by Optimal Blue |
| 2016 | Polly founded (cloud-native, API-first PPE) |
| 2020 | ICE/Black Knight acquires Optimal Blue umbrella |
| 2023 | Major LLPA redesign by FHFA (later partially withdrawn) |

**Core problem solved**: With 100+ wholesale lenders, each with 50+ products, each with daily reprices, each with 20+ adjusters — no human can do best-execution comparison. PPEs aggregate and rank in seconds.

## 14. Internet & E-Commerce Dynamic Pricing (1995 → present)

**Mechanism**: Amazon famously reprices millions of SKUs *per day*; Uber surge pricing reprices rides *per minute*; airline metasearch (Kayak, Priceline) aggregates fares across carriers.
**Core problem solved**: Continuous matching of supply to demand at consumer scale.
**Direct analog in mortgages**: PPE intraday reprice handling; lender hedge-desk-driven sheet updates.

## 15. ML / AI-Driven Personalized Pricing (2010s → present)

**Mechanism**: Recommender-system style models that estimate each customer's willingness-to-pay and present a personalized price — used in insurance underwriting, auto lending, online retail, and increasingly in mortgage scenarios via "borrower segment" pricing.
**Core problem solved**: Price discrimination at scale, optimizing realized margin per customer.
**Tension**: Regulatory pushback (ECOA, fair-lending) limits how far this can go in mortgages; LLPAs are the only sanctioned form of borrower-attribute price discrimination.

---

## What each era contributed to mortgage rate sheets

| Era | Trace it back to → |
|---|---|
| Coinage | The standardized "price" expressed as a percent of par |
| Just Price | Anti-steering, consumer-protection rules in Reg Z |
| Cost-of-production | Lender margin / hedge cost embedded in base price |
| Marginalism | Borrower willingness-to-pay → APR break-even decisions |
| Marshall | The supply/demand intersection that sets daily TBA price |
| Yield management | Intraday reprices when market moves |
| Black–Scholes | OAS that prices the prepay option embedded in MBS |
| MBS securitization | The base price itself — derived from capital markets |
| Dynamic web pricing | API-driven PPE feeds; real-time best-ex |
| Personalized AI pricing | LLPAs as the regulated form of risk-tier pricing |

Every cell on a wholesale rate sheet is the *accumulated sediment* of 5,000 years of pricing innovation.
