# Buyback End-to-End Flowchart

This Mermaid flowchart shows the full buyback lifecycle from loan sale through investor demand, cure/rebuttal, repurchase, recovery, and upstream control improvements.

```mermaid
flowchart TD
  A["Loan originated through broker channel"] --> B["Loan closes and is sold to investor or GSE"]
  B --> C["Representations and warranties attach"]
  C --> D["Investor servicing, QC, EPD, fraud, or defect monitoring"]

  D --> E{"Trigger or defect found?"}
  E -->|No| F["Normal servicing continues"]
  F --> D

  E -->|Yes| G["Investor opens review or issues finding"]
  G --> H["Formal repurchase demand or make-whole request"]
  H --> I["UWM logs demand and preserves evidence record"]
  I --> J["Initial triage: defect type, materiality, deadline, exposure"]

  J --> K{"Can the defect be cured?"}
  K -->|Yes| L["Collect missing docs, independent verification, or corrected data"]
  L --> M["Submit cure package to investor"]
  M --> N{"Cure accepted?"}
  N -->|Yes| Z["Demand closed; response costs only"]
  N -->|No| O["Escalate to rebuttal or negotiation"]

  K -->|No| P{"Is the finding rebuttable?"}
  P -->|Yes| Q["Build rebuttal with file evidence and policy support"]
  Q --> R{"Rebuttal accepted?"}
  R -->|Yes| Z
  R -->|No| O
  P -->|No| O

  O --> S{"Alternative resolution available?"}
  S -->|Indemnification| T["UWM agrees to cover defined future losses"]
  S -->|Fee in lieu| U["UWM pays negotiated fee to close demand"]
  T --> Z
  U --> Z

  S -->|No| V["Repurchase or make-whole demand stands"]
  V --> W["Calculate repurchase price"]
  W --> W1["UPB + accrued interest + advances + expenses - credits"]
  W1 --> X["UWM funds settlement"]
  X --> Y["Loan and servicing rights transfer back if applicable"]
  Y --> AA["Book asset, establish reserve, and assign workout owner"]

  AA --> AB{"Post-buyback recovery path"}
  AB -->|Performing or curable| AC["Hold, cure, refinance, or resell"]
  AB -->|Defective but saleable| AD["Scratch-and-dent sale"]
  AB -->|Delinquent or defaulted| AE["Loss mitigation, foreclosure, or REO liquidation"]

  AA --> AF["Pursue broker recourse, insurance, or indemnity recovery"]
  AC --> AG["Net loss finalized"]
  AD --> AG
  AE --> AG
  AF --> AG

  AG --> AH["Root-cause analysis"]
  AH --> AI["Update broker scorecards, QC rules, fraud-screening, and training"]
  AI --> D

  classDef start fill:#e8f5f1,stroke:#2f855a,color:#111827;
  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827;
  classDef decision fill:#fff7ed,stroke:#c2410c,color:#111827;
  classDef closed fill:#ecfdf5,stroke:#059669,color:#111827;
  classDef loss fill:#fef2f2,stroke:#dc2626,color:#111827;

  class A start;
  class B,C,D,G,H,I,J,L,M,O,Q,T,U,W,W1,X,Y,AA,AF,AH,AI process;
  class E,K,N,P,R,S,AB decision;
  class F,Z closed;
  class V,AC,AD,AE,AG loss;
```

## How to Read It

- The left side of the process starts before any demand: origination, sale, reps and warranties, and post-sale monitoring.
- The middle is the response window: triage, cure, rebuttal, negotiation, indemnification, fee in lieu, or full repurchase.
- The bottom is economic recovery: disposition of the loan, broker or insurance recovery, final loss measurement, and root-cause feedback.
- The loop back into monitoring represents prevention: each buyback should improve upstream QC, broker management, and fraud-screening discipline.
