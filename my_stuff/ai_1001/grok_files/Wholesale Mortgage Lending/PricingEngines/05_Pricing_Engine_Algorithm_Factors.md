# 05 — Pricing Engine Algorithm: The Factors Inside the Math

**Purpose:** Enumerate every quantitative and architectural factor that goes into building a mortgage pricing engine's algorithm. Uses LoanSifter / Optimal Blue / Polly as proprietary reference points, and adjacent open-source projects as analogues where mortgage-specific OSS doesn't exist.

> **No major open-source mortgage PPE exists today.** The closest open-source components are:
> - **QuantLib** — bond and MBS pricing math (C++/Python)
> - **Drools / OpenL Tablets / CLIPS** — rules engines for eligibility logic
> - **OR-Tools (Google)** — optimization for best-execution search
> - **Apache Calcite / DuckDB** — SQL-style scenario querying
> - **Apache Kafka / NATS** — event-driven reprice notification
>
> This file uses these as illustration only; production PPEs are proprietary.

---

## Architectural Layers

A pricing engine has six logical layers, each with its own algorithmic concerns:

```
┌─────────────────────────────────────┐
│  6. API / UI Layer                  │
├─────────────────────────────────────┤
│  5. Best-Execution Optimization     │
├─────────────────────────────────────┤
│  4. Adjuster Stacking & Net Price   │
├─────────────────────────────────────┤
│  3. Eligibility Rules Engine        │
├─────────────────────────────────────┤
│  2. Canonical Data Model            │
├─────────────────────────────────────┤
│  1. Rate Sheet Ingestion            │
└─────────────────────────────────────┘
```

The next sections walk through each layer's algorithmic factors.

---

## Layer 1 — Rate Sheet Ingestion

### Factor 1.1 — Format Heterogeneity
Each lender publishes rate sheets in a different format. The engine needs adapters for:
- Structured XML/JSON APIs (preferred)
- Excel/CSV exports
- PDF (structured tables vs. scanned images)
- HTML scraping
- Email-attached files
- Proprietary feeds (Optimal Blue Investor Feed, MCT MarksmanMSR feed)

**Algorithmic concern:** Parser robustness, OCR for scanned PDFs, schema versioning.

### Factor 1.2 — Schema Mapping
Lender A's "Investment Property" = Lender B's "Non-Owner Occupied" = Lender C's "NOO." Each must map to the same canonical attribute.

**Algorithmic concern:** Many-to-one schema mapping with adapter tests.

### Factor 1.3 — Reprice Detection
When a new sheet arrives, the engine must determine: is this a daily replacement, an intraday reprice, or a partial-product update?

**Algorithmic concern:** Diff detection at the price-cell level; partial cache invalidation.

### Factor 1.4 — Sheet Versioning
Every quote must be reproducible from a versioned sheet. A sheet replaced at 11:32 AM must still be retrievable for audit a year later.

**Algorithmic concern:** Append-only sheet storage with monotonic version IDs.

### Factor 1.5 — Time-of-Day Effective Logic
Sheets often have "effective at 9:30 AM" and "good until reprice" rules. New locks before 9:30 may use the prior day's closing sheet.

**Algorithmic concern:** Time-zone-aware effective-date logic per lender.

---

## Layer 2 — Canonical Data Model

### Factor 2.1 — The Core Data Tuple
Every quote is a function of:

$$ \text{Price} = f(\text{Investor}, \text{Product}, \text{Rate}, \text{LockPeriod}, \text{LoanAttributes}, \text{BorrowerAttributes}, \text{Geography}) $$

The canonical model must represent every dimension uniformly across lenders.

### Factor 2.2 — Rate Grid Representation
Stored as a sparse 2D structure:
```
Investor i → Product p → { (Rate, LockPeriod) → BasePrice }
```
With higher-dim extensions for state-specific or coupon-specific overlays.

**Algorithmic concern:** Memory efficiency. With 150 investors × 30 products × 60 rates × 6 lock periods, even sparse storage adds up.

### Factor 2.3 — Adjuster Matrix Representation
LLPAs are 2D (e.g., FICO × LTV) or higher-dim (FICO × LTV × Loan Amount). Stored as decision matrices.

**Algorithmic concern:** Indexing for fast lookup; interpolation rules for boundary cases.

### Factor 2.4 — Bucket Boundary Encoding
The 80% LTV boundary is *inclusive on the lower bucket* per agency rule. Encoding `<= 80%` vs `< 80.01%` matters at the boundary.

**Algorithmic concern:** Off-by-one consistency across all adjusters and all investors.

### Factor 2.5 — Composite Keys for Caching
A scenario's *adjuster fingerprint* is the hash of:
- (FICO bucket, LTV band, occupancy, property type, purpose, state, loan amount band, lock period, …)

Two scenarios with the same fingerprint get the same price → cacheable.

**Algorithmic concern:** Hash collisions, cache TTL aligned to sheet TTL.

---

## Layer 3 — Eligibility Rules Engine

### Factor 3.1 — Rule Representation
Each investor's eligibility rules are encoded as a decision tree or rule set:

```
IF (Program == "FHA") AND (LTV > 96.5%) THEN INELIGIBLE
IF (Property == "Condo") AND (LTV > 90%) AND (Condo Type == "Non-Warrantable") THEN INELIGIBLE
IF (Occupancy == "Investment") AND (FICO < 680) THEN INELIGIBLE
```

**Open-source analogue:** Drools (Java rule engine), CLIPS (NASA-derived), OpenL Tablets (Excel-driven rules).

### Factor 3.2 — Rule Composition / Overlay Layering
Agency rules (Fannie/Freddie/FHA) come first. Lender overlays restrict further (never loosen). The engine must compose them:

$$ \text{Eligible}_\text{final} = \text{Eligible}_\text{agency} \cap \text{Eligible}_\text{lender overlay} \cap \text{Eligible}_\text{program} $$

### Factor 3.3 — Reason-Code Generation
When ineligible, the engine must return *which rule failed*. Critical for broker UX ("Try a different lender for this scenario" vs "Try a different program").

### Factor 3.4 — Eligibility-First Pruning (Performance Optimization)
Best to filter eligibility *before* pricing. A loan that's ineligible at investor X doesn't need to be priced at any of X's 30 products.

**Performance benefit:** ~80% fewer pricing computations on typical scenarios.

### Factor 3.5 — Soft Eligibility vs Hard Eligibility
- Hard: loan cannot be made (e.g., FHA cash-out LTV > 80%)
- Soft: loan can be made but needs underwriter exception (rare)

Most PPEs only encode hard rules. Soft exceptions handled offline.

---

## Layer 4 — Adjuster Stacking & Net Price

### Factor 4.1 — Order of Application
$$ P_\text{net} = P_\text{base} + \sum_j \Delta P_j $$

But some adjusters interact:
- Cumulative agency LLPA cap
- Lender-specific stacking rules
- "Maximum of N adjusters" rules

Order matters when caps apply. Must encode investor-specific stacking logic.

### Factor 4.2 — Cap & Floor Logic
$$ P_\text{net} = \text{clip}(P_\text{base} + \sum \Delta P_j, P_\text{floor}, P_\text{cap}) $$

Different lenders cap at different levels. Some cap before comp; some after.

### Factor 4.3 — Comp Plan Layer
$$ P_\text{broker} = P_\text{net} - C_\text{LPC} \cdot 100 $$

With min/max comp constraints (file 25 in RateSheets/):
$$ C_\text{actual} = \max(C_\text{min}, \min(C_\text{max}, c \cdot L)) $$

### Factor 4.4 — Lock Adjuster
$$ P_\text{lock} = P_\text{30} + \Delta P_\text{lock}(d) $$

Some lenders publish per-lock-period grids; others publish a base grid + delta. Must handle both.

### Factor 4.5 — State / Geographic Overrides
A few lenders have state-specific rate sheets entirely; most have state adjusters layered on. Must detect which mode applies per lender.

### Factor 4.6 — Sub-Coupon Pricing
Within a 5.5 TBA coupon, loans with note rate 5.50%, 5.625%, 5.75%, 5.875% all deliver into the same pool but have different *to-the-borrower* prices. The engine must allocate the within-coupon "excess strip" value across these rates.

### Factor 4.7 — Tie-Breaking
When two products score equally:
- Investor preference (broker-configured)
- Lock period (shorter usually preferred)
- Lender turn time
- Historical service rating

Some PPEs allow weighted scoring.

---

## Layer 5 — Best-Execution Optimization

### Factor 5.1 — Objective Function
The objective varies by use case:
- $\arg\max P_\text{broker-facing}$ (broker comp maximizing)
- $\arg\min r_{APR}$ (borrower APR minimizing)
- $\arg\min \text{Cash-to-Close}$ (borrower up-front cost minimizing)
- $\arg\min M$ (borrower monthly minimizing)
- Pareto frontier across rate × cost

### Factor 5.2 — Constraint Set
Eligibility (binary), program restrictions, broker-allowed lender set, lock period bounds, comp plan availability.

### Factor 5.3 — Search Strategy
With small candidate sets (post-eligibility), brute-force enumeration is fine. With larger sets, branch-and-bound or beam search.

**Open-source analogue:** Google OR-Tools' constraint solver, Pyomo (Python optimization).

### Factor 5.4 — Pareto Frontier Construction
For multi-objective optimization:
$$ \mathcal{P} = \{ x : \nexists y \text{ s.t. } y \succ x \} $$

Returned to the user as the set of non-dominated offers.

### Factor 5.5 — Latency Budget
A best-ex search must return in ~300 ms for good UX. This drives:
- Pre-computed adjuster tables
- Parallel investor queries
- Aggressive caching
- Eligibility pruning before pricing

### Factor 5.6 — Determinism
Two identical scenario submissions at the same instant must return identical results. No nondeterministic ranking, no random tie-breaks (unless seeded).

---

## Layer 6 — API / UI Layer

### Factor 6.1 — Quote Object Schema
Output of a pricing call includes:
- (Investor, Product, Rate, LockPeriod) — the identity
- Net price
- Adjuster waterfall (every line item)
- Eligibility status (eligible / not eligible + reasons)
- Sheet version / timestamp
- Reproducibility token

### Factor 6.2 — Real-Time Update Push
When a reprice fires, downstream subscribers must be notified.

**Open-source analogue:** Kafka, NATS, Server-Sent Events.

### Factor 6.3 — Audit Logging
Every API call logged with inputs, outputs, sheet versions, user identity. Required for compliance and dispute resolution.

### Factor 6.4 — Rate Limiting
Brokers may spam the API. Each call must enforce per-user QPS limits.

### Factor 6.5 — Versioning
API contracts must evolve without breaking integrations.

---

## Cross-Cutting Mathematical Concerns

### A. Monotonicity Invariants
Pricing must be monotonic in expected directions:
- Higher FICO ⇒ better price (within bucket)
- Lower LTV ⇒ better price
- Shorter lock ⇒ better price

Violations indicate adjuster bugs.

### B. No-Arbitrage Within a Sheet
$$ P_\text{base}(r_1) > P_\text{base}(r_2) \quad \text{if } r_1 > r_2 $$

Higher rate must always give higher base price on the same sheet.

### C. Sheet Consistency Tests
Automated tests run on each new sheet ingestion:
- All rates have a price
- Prices are within expected daily range (no fat-finger errors)
- No adjuster is missing
- Adjuster totals don't exceed cap

### D. Boundary Condition Math
FICO bands, LTV bands, loan amount bands — each boundary must be encoded identically across investors. Off-by-one bugs at boundaries are a major source of pricing disputes.

### E. Numerical Precision
Prices stored as fixed-point (3–4 decimal places, e.g., 100.875). Float arithmetic risks rounding errors that compound across adjusters.

### F. Discount Curve Math
For loans that haven't priced yet (lock-and-shop, TBD), the engine must extrapolate prices forward in time using a discount-curve approximation. Touches duration / convexity math (file 29 in RateSheets/).

---

## Performance Budget (Typical)

| Stage | Latency budget |
|---|---|
| Scenario validation | < 5 ms |
| Eligibility filtering (150 investors) | 50 ms |
| Pricing (post-filter, ~30 surviving investors × 30 products) | 150 ms |
| Best-ex sort / ranking | 30 ms |
| API serialization + network | 65 ms |
| **Total target** | **~300 ms** |

---

## Where Open-Source Tools Could Help (Theoretically)

| Concern | Open-source candidate | Status in mortgage |
|---|---|---|
| Bond/MBS valuation | **QuantLib** | Used by capital-markets desks, not PPEs |
| Eligibility rules | **Drools, OpenL Tablets, CLIPS** | Used in adjacent finance; some PPEs use Drools internally |
| Best-ex optimization | **Google OR-Tools, Pyomo** | Used in airline / logistics; rare in mortgage PPEs |
| Cache layer | **Redis, Memcached** | Universally used in PPEs |
| Event streaming | **Kafka, NATS** | Used by larger PPEs (Polly, Optimal Blue infra) |
| Schema serialization | **Protocol Buffers, Avro** | Used internally; not exposed to integrators |
| Rule editing UI | **OpenL Tablets (Excel-as-rule-source)** | Theoretically applicable; few PPEs adopt |
| Data validation | **Great Expectations, pandera** | Could be used for sheet ingestion sanity checks |

---

## What a Greenfield Open-Source Mortgage PPE Would Need

A genuine OSS mortgage PPE doesn't exist today but would require, at minimum:

1. **MISMO XML compliance** for loan data ingestion.
2. **Adapter framework** for ~50–150 wholesale lender feeds (each a custom build).
3. **Canonical rate sheet model** (no industry standard exists — the project would *create* one).
4. **Rules DSL** for eligibility + adjuster expression.
5. **Best-ex solver** plug-in.
6. **Audit / replay system**.
7. **Reprice event bus**.
8. **APR / TILA calculation library** (Reg Z compliant).
9. **Compliance reporting modules** (HMDA, anti-steering, fair lending).
10. **LOS connector library** (Encompass, Calyx, etc.).

The barrier is not the algorithms — it's the **business-development cost** of getting 150 lenders to provide structured feeds to an open-source project they don't control.

---

## The One-Line Algorithmic Summary

> A pricing engine is a **rules-engine + matrix-lookup + constraint-solver**, glued together with **adapter parsers** and **versioned caches**, optimized to return a non-dominated set of priced, eligible offers within ~300 ms of scenario submission — and reproducibly auditable months later.

That's the math. Everything else is the business problem of getting the right data into it.
