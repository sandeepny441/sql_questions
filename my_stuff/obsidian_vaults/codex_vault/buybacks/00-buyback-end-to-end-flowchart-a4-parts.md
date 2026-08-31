# Buyback End-to-End Flowchart: A4 Print Parts

This version divides the buyback lifecycle into twenty narrow Mermaid diagrams. Each part is designed to stay in a single reading pane, avoid left-right scrolling, and print cleanly on one A4 page.

The numbering is hierarchical. Part 1 uses steps 1.1, 1.2, 1.3, and so on; Part 2 uses 2.1, 2.2, 2.3; and the pattern continues through the process.

Each Mermaid block uses larger font settings and short wrapped node labels.

Suggested print settings: A4, portrait orientation, default margins, and scale around 90-100%.

## Part 1: Loan Creation

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["1.1<br/>Broker<br/>submits file"] --> B["1.2<br/>UWM<br/>underwrites"]
  B --> C["1.3<br/>Loan<br/>closes"]
  C --> D["1.4<br/>File<br/>retained"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  class A,B,C,D process;
```

What it means: the evidence trail begins before the loan is sold.

<div style="page-break-after: always; break-after: page;"></div>

## Part 2: Sale and Contractual Risk

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["2.1<br/>Loan sold<br/>to investor"] --> B["2.2<br/>Reps and<br/>warranties attach"]
  B --> C["2.3<br/>Investor<br/>owns risk"]
  C --> D["2.4<br/>UWM keeps<br/>contract duties"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  class A,B,C,D process;
```

What it means: selling the loan does not eliminate UWM's repurchase obligations.

<div style="page-break-after: always; break-after: page;"></div>

## Part 3: Post-Sale Monitoring

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["3.1<br/>Investor<br/>monitors loan"] --> B["3.2<br/>QC or<br/>servicing review"]
  B --> C["3.3<br/>EPD or<br/>fraud signal"]
  C --> D["3.4<br/>Issue<br/>flagged"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B process;
  class C,D risk;
```

What it means: a demand often starts with monitoring after sale, not with a closing-day event.

<div style="page-break-after: always; break-after: page;"></div>

## Part 4: Defect Review

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["4.1<br/>Investor<br/>opens review"] --> B["4.2<br/>Defect<br/>tested"]
  B --> C["4.3<br/>Evidence<br/>assembled"]
  C --> D["4.4<br/>Materiality<br/>assessed"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef decision fill:#fff7ed,stroke:#c2410c,color:#111827,font-size:20px;
  class A,C process;
  class B,D decision;
```

What it means: not every defect becomes a demand; the investor decides whether it is material.

<div style="page-break-after: always; break-after: page;"></div>

## Part 5: Demand Notice

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["5.1<br/>Demand<br/>issued"] --> B["5.2<br/>Loan and<br/>defect listed"]
  B --> C["5.3<br/>Deadline<br/>set"]
  C --> D["5.4<br/>Clock<br/>starts"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,D risk;
  class B,C process;
```

What it means: the demand letter defines the response window and the alleged breach.

<div style="page-break-after: always; break-after: page;"></div>

## Part 6: Intake and Ownership

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["6.1<br/>Demand<br/>logged"] --> B["6.2<br/>Owner<br/>assigned"]
  B --> C["6.3<br/>File<br/>locked down"]
  C --> D["6.4<br/>Workplan<br/>created"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  class A,B,C,D process;
```

What it means: intake control keeps the response organized and preserves the audit trail.

<div style="page-break-after: always; break-after: page;"></div>

## Part 7: Evidence Pull

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["7.1<br/>Underwriting<br/>notes"] --> B["7.2<br/>QC<br/>records"]
  B --> C["7.3<br/>Fraud-screen<br/>history"]
  C --> D["7.4<br/>Servicing<br/>history"]
  D --> E["7.5<br/>Evidence<br/>gap list"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B,C,D process;
  class E risk;
```

What it means: a strong response depends on finding the exact support for the original decision.

<div style="page-break-after: always; break-after: page;"></div>

## Part 8: Strategy Triage

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["8.1<br/>Defect<br/>reviewed"] --> B["8.2<br/>Exposure<br/>estimated"]
  B --> C["8.3<br/>Best path<br/>selected"]
  C --> D["8.4<br/>Cure,<br/>rebut, or settle"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef decision fill:#fff7ed,stroke:#c2410c,color:#111827,font-size:20px;
  class A,B process;
  class C,D decision;
```

What it means: triage decides whether UWM should cure, rebut, negotiate, or prepare for repurchase.

<div style="page-break-after: always; break-after: page;"></div>

## Part 9: Cure Path

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["9.1<br/>Curable<br/>defect"] --> B["9.2<br/>Missing docs<br/>requested"]
  B --> C["9.3<br/>Cure package<br/>built"]
  C --> D["9.4<br/>Package<br/>submitted"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  class A,B,C,D process;
```

What it means: cure tries to fix the defect without repurchase.

<div style="page-break-after: always; break-after: page;"></div>

## Part 10: Cure Decision

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["10.1<br/>Investor<br/>reviews cure"] --> B["10.2<br/>Accepted?"]
  B --> C["10.3<br/>Yes path:<br/>demand closed"]
  C --> D["10.4<br/>No path:<br/>escalate"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef closed fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B process;
  class C closed;
  class D risk;
```

What it means: rejection does not always mean immediate repurchase; the file may move to rebuttal or negotiation.

<div style="page-break-after: always; break-after: page;"></div>

## Part 11: Rebuttal Path

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["11.1<br/>Rebuttable<br/>finding"] --> B["11.2<br/>Guide rule<br/>mapped"]
  B --> C["11.3<br/>File evidence<br/>linked"]
  C --> D["11.4<br/>Rebuttal<br/>submitted"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  class A,B,C,D process;
```

What it means: rebuttal argues that the investor finding is incorrect or not material under the rules.

<div style="page-break-after: always; break-after: page;"></div>

## Part 12: Rebuttal Decision

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["12.1<br/>Investor<br/>reviews rebuttal"] --> B["12.2<br/>Accepted?"]
  B --> C["12.3<br/>Yes path:<br/>demand closed"]
  C --> D["12.4<br/>No path:<br/>negotiate"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef closed fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B process;
  class C closed;
  class D risk;
```

What it means: if rebuttal fails, UWM evaluates settlement alternatives before full repurchase.

<div style="page-break-after: always; break-after: page;"></div>

## Part 13: Negotiated Alternatives

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["13.1<br/>Escalation<br/>opened"] --> B["13.2<br/>Indemnity<br/>option?"]
  B --> C["13.3<br/>Fee in lieu<br/>option?"]
  C --> D["13.4<br/>Option used:<br/>demand closed"]
  D --> E["13.5<br/>No option:<br/>repurchase"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef closed fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B,C process;
  class D closed;
  class E risk;
```

What it means: negotiated alternatives may avoid immediate repurchase but can preserve future exposure.

<div style="page-break-after: always; break-after: page;"></div>

## Part 14: Repurchase Price

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["14.1<br/>UPB"] --> B["14.2<br/>Add<br/>interest"]
  B --> C["14.3<br/>Add<br/>advances"]
  C --> D["14.4<br/>Add<br/>expenses"]
  D --> E["14.5<br/>Less<br/>credits"]
  E --> F["14.6<br/>Final<br/>price"]

  classDef cost fill:#fef3c7,stroke:#d97706,color:#111827,font-size:20px;
  class A,B,C,D,E,F cost;
```

What it means: the repurchase price is contractual, not a current market value.

<div style="page-break-after: always; break-after: page;"></div>

## Part 15: Settlement and Transfer

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["15.1<br/>Settlement<br/>confirmed"] --> B["15.2<br/>UWM funds<br/>payment"]
  B --> C["15.3<br/>Demand<br/>closed"]
  C --> D["15.4<br/>Loan<br/>returns"]
  D --> E["15.5<br/>Reserve<br/>set"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef cost fill:#fef3c7,stroke:#d97706,color:#111827,font-size:20px;
  class A,C,D,E process;
  class B cost;
```

What it means: settlement moves the loan back onto UWM's books if applicable.

<div style="page-break-after: always; break-after: page;"></div>

## Part 16: Workout Assignment

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["16.1<br/>Asset<br/>boarded"] --> B["16.2<br/>Workout<br/>owner assigned"]
  B --> C["16.3<br/>Loan status<br/>reviewed"]
  C --> D["16.4<br/>Recovery<br/>plan chosen"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef decision fill:#fff7ed,stroke:#c2410c,color:#111827,font-size:20px;
  class A,B process;
  class C,D decision;
```

What it means: after repurchase, the next job is managing recovery and limiting final loss.

<div style="page-break-after: always; break-after: page;"></div>

## Part 17: Recovery Paths

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["17.1<br/>Performing:<br/>hold or resell"] --> B["17.2<br/>Defective:<br/>scratch sale"]
  B --> C["17.3<br/>Defaulted:<br/>loss mitigation"]
  C --> D["17.4<br/>Recovery<br/>measured"]

  classDef recovery fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  classDef risk fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B,D recovery;
  class C risk;
```

What it means: recovery depends on whether the loan is performing, saleable, or defaulted.

<div style="page-break-after: always; break-after: page;"></div>

## Part 18: Recourse and Insurance

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["18.1<br/>Broker<br/>recourse checked"] --> B["18.2<br/>Insurance<br/>claim checked"]
  B --> C["18.3<br/>Recoveries<br/>collected"]
  C --> D["18.4<br/>Net loss<br/>reduced"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef recovery fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  class A,B process;
  class C,D recovery;
```

What it means: third-party recovery can materially reduce UWM's final loss.

<div style="page-break-after: always; break-after: page;"></div>

## Part 19: Loss Finalization

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["19.1<br/>Recovery<br/>known"] --> B["19.2<br/>Costs<br/>added"]
  B --> C["19.3<br/>Credits<br/>applied"]
  C --> D["19.4<br/>Net loss<br/>finalized"]

  classDef cost fill:#fef3c7,stroke:#d97706,color:#111827,font-size:20px;
  classDef loss fill:#fef2f2,stroke:#dc2626,color:#111827,font-size:20px;
  class A,B,C cost;
  class D loss;
```

What it means: final severity is the repurchase cost minus recoveries, plus carrying and workout costs.

<div style="page-break-after: always; break-after: page;"></div>

## Part 20: Prevention Loop

```mermaid
%%{init: {"themeVariables": {"fontSize": "20px", "fontFamily": "Arial"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 20, "rankSpacing": 26}}}%%
flowchart TB
  A["20.1<br/>Root cause<br/>review"] --> B["20.2<br/>Broker<br/>scorecard"]
  B --> C["20.3<br/>QC rule<br/>update"]
  C --> D["20.4<br/>Fraud rule<br/>update"]
  D --> E["20.5<br/>Future loss<br/>reduced"]

  classDef process fill:#eef2ff,stroke:#4f46e5,color:#111827,font-size:20px;
  classDef recovery fill:#ecfdf5,stroke:#059669,color:#111827,font-size:20px;
  class A,B,C,D process;
  class E recovery;
```

What it means: the buyback process should feed directly into better prevention, lower demand frequency, and lower loss severity.
