# 04 — LoanSifter: Business Functionality

**Purpose:** What LoanSifter actually *does* — features, workflows, integrations, and the commercial model. Pairs with file 03 (philosophy).

---

## 1. Product Category

| Attribute | Value |
|---|---|
| Type | Multi-investor Product & Pricing Engine (PPE) |
| Primary user | Mortgage broker / TPO (third-party originator) |
| Secondary user | Mini-correspondent, small banker |
| Channel served | Wholesale (broker → wholesaler) |
| Today | Part of Optimal Blue, which is part of ICE Mortgage Technology (Black Knight) |

---

## 2. Inputs Ingested

LoanSifter consumes data from three sources:

### A. Lender Rate Sheets
- ~150+ wholesale investor rate sheets ingested daily and on each reprice.
- Formats: proprietary XML/JSON APIs (preferred), structured PDF, Excel, faxed PDFs (legacy).
- Each lender's overlays, lock policies, and program-specific guidelines normalized into LoanSifter's internal model.

### B. Loan Scenario Inputs
Brokers enter (or LOS pushes via integration):
- Borrower attributes: FICO, income, assets, employment type
- Loan attributes: amount, LTV, CLTV, purpose, occupancy, property type
- Lock period and target close date
- Comp plan selection
- State / property location

### C. Comp Plans & Broker Settings
- Each broker company's LPC plans across each wholesale relationship
- BPC defaults
- Minimum / maximum comp dollar constraints
- AE / branch identifiers

---

## 3. Core Functions

### Function 1 — Eligibility Filtering
Given a scenario, determine which (investor, product) pairs the loan qualifies for.

- Programs: Conventional, FHA, VA, USDA, Jumbo, Non-QM, HELOC, second liens
- Encoded rules per investor: min FICO, max LTV/CLTV, max DTI, property restrictions, geographic exclusions, program-specific overlays
- Returns: eligible set + reason codes for each rejection

### Function 2 — Pricing
For each eligible (investor, product), compute the price grid across rates and lock periods:

- Pull base price for each rate/lock combination
- Apply stacked adjusters (FICO/LTV, occupancy, property, purpose, loan amount, state, etc.)
- Apply lender overlays
- Apply lock period adjuster
- Apply broker comp plan
- Output: net price by rate

### Function 3 — Best Execution Display
Across all eligible (investor, product, rate, lock) combinations, surface the highest-net-priced options:

- Default view: best rate at each net-price level (e.g., "the best rate where price ≤ par")
- Per-investor view: each investor's best price at a target rate
- Side-by-side view: top-5 investors at a chosen rate

### Function 4 — Quote Generation & Audit
- Each quote stored with timestamp, sheet ID, scenario inputs
- "Sticky quote" reproducible for compliance / dispute resolution
- Lock request workflow (originally generated paper/PDF requests; later API-driven)

### Function 5 — Anti-Steering Documentation
Auto-generate the Reg Z safe-harbor three-option presentation:
- Lowest interest rate eligible
- Lowest total points eligible
- Lowest total cost of credit (points + fees) eligible

This satisfies §1026.36(e) requirements and is exportable to the loan file.

### Function 6 — Lock & Pipeline Tracking
- Submitted lock requests visible across the broker's pipeline
- Lock expiration calendar
- Extension cost estimation
- Worst-case relock price comparison

### Function 7 — Search & Scenario Comparison
- "What if" panel: vary one input (FICO, LTV, lock period) and watch pricing move
- LLPA-bucket-break finder: e.g., "if you went to 79% LTV from 80.5%, you'd pick up 50 bp"
- Stack visualizer: show every adjuster line by line

---

## 4. Integrations

| Integration Class | Examples |
|---|---|
| LOS (loan origination system) | Encompass, Calyx, BytePro, LendingPad, ARIVE |
| TPO portals | Each wholesale lender's broker portal |
| Lender lock desks | API-based for major lenders; legacy email/portal for smaller |
| AUS (automated underwriting) | DU (Fannie), LPA (Freddie) — pass-through |
| CRM | Various (Salesforce, HubSpot-flavored mortgage CRMs) |
| Document services | Disclosures, LE generation handoff to LOS |

---

## 5. Workflow — A Day in the Life of a Broker Using LoanSifter

1. **Borrower calls** — broker pulls credit, gets target rate/scenario.
2. **Scenario entry** — broker punches FICO, LTV, occupancy, property, state, comp plan into LoanSifter.
3. **Eligibility check** runs across 100+ investor × 30 product combinations.
4. **Pricing returns** — sorted best-ex view shown in ~1–3 seconds.
5. **Broker reviews waterfall** — clicks into top investor to verify adjuster stack, lock policy, turn times.
6. **Quote saved** — sticky quote with timestamped sheet version for later reference.
7. **Lock request initiated** — generated electronically or via lender portal.
8. **Pipeline tracking** — lock added to dashboard with expiration date, file status.
9. **Reprice notification** — if market moves and any pipeline lock is affected, broker is alerted.
10. **Three-option doc generated** — Reg Z safe-harbor presentation attached to file.

---

## 6. Commercial Model

| Stakeholder | What they pay / get |
|---|---|
| Broker | SaaS subscription (per-user, per-month or per-loan); access to multi-lender view |
| Wholesale lender | Subscription / distribution fee for inclusion in the engine |
| Optimal Blue / ICE | Operates the platform, captures recurring revenue from both sides |

Lender fees are for *inclusion* and *daily ingestion bandwidth*, **not** for ranking or steering. (This is the structural commitment behind the lender-neutral philosophy in file 03.)

---

## 7. Differentiators vs. Competitors

| Competitor | Differentiator vs. LoanSifter |
|---|---|
| Optimal Blue (retail PPE side) | More features for retail lenders; less broker-focused UX |
| Polly | Cloud-native, modern API, real-time tick-driven pricing; smaller lender catalog |
| EPPS (Encompass Product & Pricing) | Bundled with Encompass LOS; ICE-owned cross-sell |
| LenderPrice | Highly configurable engine; weaker broker-channel coverage |
| ARIVE PPE | Bundled with ARIVE TPO platform; vertically integrated |
| Mortech (Zillow) | Strong retail / consumer-facing rate display |

LoanSifter's positioning: *largest broker-channel investor catalog, sheet-faithful, fast*.

---

## 8. Operational Scale (Approximate)

| Metric | Order of magnitude |
|---|---|
| Wholesale investors integrated | ~150+ |
| Products covered | ~30 per investor → ~4,500 total |
| Daily rate sheet ingestions | ~150 sheets/day + reprice events |
| Reprice events / day across all investors | 50–300 (varies with volatility) |
| Pricing scenarios computed / day | Millions |
| Broker users | Tens of thousands historically |

---

## 9. Compliance & Audit Features

- Every quote stored with full inputs and sheet version
- Reg Z safe-harbor presentation auto-generated
- LO comp plan changes tracked with effective dates
- HMDA-relevant data captured for downstream reporting (in conjunction with LOS)
- Tolerance-cure scenarios flagged when pricing drifts post-LE

---

## 10. Notable Limitations (Honest Assessment)

| Limitation | Why it exists |
|---|---|
| Sheet ingestion lag for new lenders | Each ingestion adapter is custom-built |
| Niche programs incomplete | Investor-specific overlays may not be fully encoded |
| Eligibility rules occasionally stale | Lenders change overlays faster than adapters can keep up |
| UI density | Power users love it; new brokers find it intimidating |
| Legacy lock workflow | Some lenders still require portal submission; not all API-direct |
| Limited borrower-facing surface | Designed for broker use, not consumer presentation |

---

## 11. Where the Engine Sits in the Loan Lifecycle

```
[Application] → [LoanSifter scenario] → [Best-ex pick] → [Lock request]
        ↓                                                       ↓
       LOS  ←————————————————————————————————————————  [Lock confirm]
        ↓
   [Underwriting] → [CTC] → [Closing] → [Funding] → [Sale to investor]
```

LoanSifter is the *pricing & decision* layer between application and lock. Once locked, the file moves to the LOS for processing, and LoanSifter's role narrows to lock-tracking and possible reprice handling.

---

## 12. Strategic Function in the Broader Industry

LoanSifter (and its peers) function as a **distribution layer** comparable to:

| Industry | Equivalent layer |
|---|---|
| Airlines | Sabre/Amadeus GDS + Kayak/Expedia metasearch |
| E-commerce | Amazon marketplace |
| Insurance | Aggregator sites (CompareInsurance, Insurify) |
| Investing | Brokerage best-ex routing |

This is the **value chain choke point** through which most wholesale loans must pass to be priced competitively. Owning this layer is strategically powerful — which is why ICE/Black Knight rolled it up.

---

## 13. The One-Line Functional Summary

> LoanSifter is a **rate-sheet ingestion engine + eligibility filter + best-execution search + audit-trail generator**, optimized for the broker workflow, monetized as a SaaS distribution layer, and operated as a *neutral* aggregator across ~150 wholesale lenders.
