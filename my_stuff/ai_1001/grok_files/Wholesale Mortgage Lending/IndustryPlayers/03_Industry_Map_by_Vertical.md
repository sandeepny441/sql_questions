# 03 — Industry Map: Verticals, Focus Areas, and Companies

A comprehensive map of the U.S. mortgage industry organized by **vertical domain**. For each vertical: what it does, the unique focus, and the major companies in it.

> Information current to early 2026. The industry consolidates rapidly via M&A; expect ownership changes annually.

---

## How to Read This Map

A typical residential mortgage touches ~12–18 different vertical domains from first lead to final paid-off loan. Each vertical has its own dominant players, competitive dynamics, and integration challenges.

This file groups them into **17 verticals** plus a summary of the **top 10 lenders** and **government / regulatory** layer.

---

## Vertical 1 — Lenders (Origination)

**Focus:** Take borrower applications, underwrite, fund loans. Largest single vertical by people and dollars.

### Sub-channels
- **Retail** — lender originates directly to consumer
- **Wholesale** — broker submits to wholesale lender
- **Correspondent** — smaller lender funds, then sells to aggregator

### Top 10 U.S. Lenders (by 2024–2025 origination volume)
| Rank | Lender | Channel Focus | Notes |
|---|---|---|---|
| 1 | **United Wholesale Mortgage (UWM)** | Wholesale | Pontiac, MI; led by Mat Ishbia; #1 since 2022 |
| 2 | **Rocket Companies / Rocket Mortgage** | Retail (+ Pro TPO wholesale) | Detroit; acquired Mr. Cooper & Redfin in 2025 |
| 3 | **Pennymac Financial Services** | Retail / Correspondent / Wholesale | Largest correspondent aggregator |
| 4 | **Wells Fargo Home Mortgage** | Retail (bank channel) | Shrinking footprint post-2022 strategic shift |
| 5 | **JPMorgan Chase Home Lending** | Retail (bank) | |
| 6 | **U.S. Bank** | Retail (bank) | |
| 7 | **Bank of America Home Loans** | Retail (bank) | |
| 8 | **Citizens Bank** | Retail | |
| 9 | **CrossCountry Mortgage** | Retail | Cleveland-based; aggressive growth |
| 10 | **Guild Mortgage** | Retail | NYSE-listed; PE-backed |

### Notable Non-Top-10
- **loanDepot** — went public 2021; restructuring through 2024
- **Better.com** — went public via SPAC 2023; consumer-direct
- **AmeriSave** — large direct lender
- **New American Funding** — large retail
- **Fairway Independent Mortgage**
- **Movement Mortgage**
- **Caliber Home Loans** — acquired by Newrez (Rithm) 2022
- **Newrez / Rithm Capital** — large via acquisitions
- **Mr. Cooper** — being acquired by Rocket (announced 2025)
- **Home Point Capital** — acquired by Mr. Cooper 2023, exited wholesale

---

## Vertical 2 — Loan Origination Systems (LOS)

**Focus:** The system-of-record for a loan in process. Borrower data, document storage, workflow, disclosures, vendor integration.

### Unique angle
LOS is the **operating system of the mortgage** — every other vertical plugs into it.

### Major Players
| Company | Product | Channel | Notes |
|---|---|---|---|
| **ICE Mortgage Technology** | **Encompass** | All channels | Dominant; ~50% market share |
| **Constellation Software (CFM)** | **Empower** | Banks, large lenders | Divested from BK→ICE; now standalone |
| **Calyx Software** | Calyx Point, Path | Small/mid brokers, lenders | Long-tenured (since 1991) |
| **MeridianLink** | LendingQB | Banks, credit unions | Public (NYSE: MLNK) |
| **Byte Software** | BytePro | Small lenders, brokers | Long-tenured |
| **LendingPad (WeiLLC)** | LendingPad | Wholesale, retail | Modern UX; popular with brokers |
| **ARIVE** | ARIVE | Brokers / TPO | Broker-focused, integrated TPO platform |
| **Maxwell** | Maxwell Point of Sale + LOS | Community lenders | |
| **Path Software** | Path LOS | Smaller lenders | |
| **Floify** | (POS) | Brokers | Acquired by Porch 2021 |
| **Vellum (formerly Lender Toolkit)** | | Encompass extensions | |

---

## Vertical 3 — Point-of-Sale (POS) / Borrower-Facing Apps

**Focus:** The consumer-facing application experience. Mobile-first, smartphone-friendly application + document upload.

### Major Players
| Company | Notes |
|---|---|
| **Blend** | NYSE-listed (BLND); largest standalone POS |
| **SimpleNexus** | Acquired by nCino 2022; later by ICE |
| **Maxwell** | POS + LOS bundle |
| **BeSmartee** | |
| **Floify** | Owned by Porch (NASDAQ: PRCH) |
| **Capacity** (AI assistant) | Multi-purpose |
| **Roostify** | Acquired by CoreLogic 2023 |
| **LiteSpeed** | |

---

## Vertical 4 — Product & Pricing Engines (PPE)

**Focus:** Real-time pricing aggregation across investor/lender rate sheets; eligibility filtering; best-execution display.

### Major Players
| Company | Product | Channel Focus | Owner |
|---|---|---|---|
| **Optimal Blue** | Optimal Blue PPE + LoanSifter | Retail + Wholesale | Constellation Software |
| **Polly** | Polly | Cloud-native, growing | VC-funded standalone |
| **ICE Mortgage Technology** | **EPPS** (Encompass PPE) | Bundled with Encompass | ICE |
| **LenderPrice** | LenderPrice | Highly configurable | Standalone |
| **Mortech** | Mortech | Retail / consumer-facing | Zillow Group |
| **ARIVE PPE** | | Bundled with ARIVE TPO | ARIVE |
| **LendingPad PPE** | | Bundled with LendingPad | WeiLLC |
| **Loan Pricer** | | Smaller-scale | |

See `PricingEngines/` folder for deep dives on Optimal Blue and LoanSifter.

---

## Vertical 5 — Servicing Systems

**Focus:** Run the loan after closing — collect payments, manage escrow, handle delinquency, send statements.

### Major Players
| Company | Product | Notes |
|---|---|---|
| **ICE Mortgage Technology** | **MSP** | Dominant; services > 50% of US residential mortgages |
| **Sagent** | LoanServ / Sagent Cloud | Cloud-native alternative; backed by Warburg Pincus + Fiserv |
| **Black Knight (now ICE)** | LoanSphere, ICE Servicing Digital | Borrower-facing portal |
| **FICS** | Mortgage Servicer | Smaller lenders / credit unions |
| **Servicing Director** | | ICE-owned |

### Servicing-Adjacent (sub-services)
- **LERETA, CoreLogic Tax** — property tax services
- **ServiceMac** — sub-servicer for portfolios
- **Cenlar FSB** — large sub-servicer

---

## Vertical 6 — Capital Markets / Hedge Advisory

**Focus:** Help lenders hedge their pipeline of locked-but-unfunded loans against rate movement; advise on best-execution to investors.

### Major Players
| Company | Notes |
|---|---|
| **MCT (Mortgage Capital Trading)** | Independent leader |
| **Vice Capital Markets** | |
| **Optimal Blue Hedge Analytics** | Bundled with Optimal Blue PPE |
| **Polly Capital Markets** | Newer entrant |
| **Compass Analytics** | Part of Black Knight → ICE |
| **Riivos** | |
| **THINK Realty** | |

### Adjacent: Whole-Loan Trading Platforms
| Company | Notes |
|---|---|
| **Resitrader** | Part of Optimal Blue |
| **MAXEX** | Standalone exchange; jumbo focus |
| **Pennymac** (correspondent platform) | Largest correspondent aggregator |
| **AmeriHome** (Western Alliance) | Major correspondent aggregator |

---

## Vertical 7 — Data & Analytics

**Focus:** Property data, valuations, prepayment models, market analytics. Sold to lenders, servicers, capital markets, regulators.

### Major Players
| Company | Focus | Notes |
|---|---|---|
| **CoreLogic** | Property data, MLS data, AVMs, climate data | Taken private 2021 by Stone Point + Insight |
| **ICE Data Services / Black Knight D&A** | Mortgage performance data, prepayment | Part of ICE |
| **ATTOM Data** | Property records, foreclosure data | |
| **HouseCanary** | AVM + valuations | |
| **Clear Capital** | AVM + appraisal | |
| **Verisk** | Insurance-adjacent property data | |
| **First American Data Tree** | Title & property data | |
| **Quantarium** | AVM provider | |
| **Polygon Research** | Mortgage industry analytics | |
| **Inside Mortgage Finance** | Trade publication + data | |

---

## Vertical 8 — Property Listings / MLS / Consumer Discovery

**Focus:** Where consumers see homes for sale and rent; lead generation for agents and lenders.

### Major Players
| Company | Focus | Notes |
|---|---|---|
| **Zillow Group** | Listings + estimates + Zillow Home Loans + Mortech | NASDAQ: ZG |
| **Realtor.com (Move Inc.)** | Listings | Owned by News Corp |
| **Redfin** | Listings + brokerage + (formerly) mortgage | Acquired by Rocket 2025 |
| **Trulia** | Listings | Part of Zillow |
| **CoStar Group** | Commercial listings + Homes.com (residential) | Aggressive Homes.com push |
| **Apartments.com** | Rentals | CoStar-owned |
| **Compass** | Brokerage + agent platform | NYSE: COMP |
| **eXp World Holdings** | Brokerage | NASDAQ: EXPI |
| **Anywhere Real Estate** (Coldwell, Century 21) | Traditional brokerage | NYSE: HOUS |

### MLS Providers (regional)
- Bright MLS (Mid-Atlantic)
- California Regional MLS (CRMLS)
- NWMLS (Northwest)
- Stellar MLS (Florida)
- ~~600+ local MLSs nationwide

---

## Vertical 9 — Valuation / AVM / Appraisal Management

**Focus:** Determine property value for lending. Mix of human appraisers and automated valuation models (AVMs).

### AVMs (Automated Valuation Models)
| Company | Notes |
|---|---|
| **CoreLogic** | Largest |
| **ICE / Black Knight** | |
| **HouseCanary** | |
| **Clear Capital** | |
| **Quantarium** | |
| **ATTOM** | |

### Appraisal Management Companies (AMCs)
| Company | Notes |
|---|---|
| **Class Valuation** | |
| **Solidifi** (parent: Real Matters) | |
| **ServiceLink** | |
| **Reggora** | Modernized AMC |
| **Clear Capital** | Both AVM and AMC |
| **Property Vista** | |
| **Mortgage Connect (Triserv)** | |

### Disruptors
- **Reggora** — modern AMC API platform
- **Birdseye** — appraisal modernization
- Fannie/Freddie **Value Acceptance / Appraisal Waivers** — eliminating need for appraisal on lower-risk scenarios

---

## Vertical 10 — Verifications (Income, Asset, Employment)

**Focus:** Verify borrower-stated income, assets, and employment electronically.

### Major Players
| Company | Focus | Notes |
|---|---|---|
| **The Work Number** (Equifax) | Employment / income | Dominant in employer records |
| **Plaid** | Asset verification via bank API | Big tech infrastructure |
| **AccountChek** (Informative Research) | Asset verification | |
| **FormFree** | Income + asset verification | |
| **Truework** | Employment / income | |
| **Argyle** | Income / employment via payroll APIs | |
| **Atomic** | Payroll connectivity | |
| **Pinwheel** | Payroll connectivity | |
| **MicroBilt** | Multi-source verification | |
| **Yodlee** (Envestnet) | Account aggregation | |

---

## Vertical 11 — Credit Bureaus / FICO

**Focus:** Borrower credit data and scoring models.

### Major Players
| Company | Role |
|---|---|
| **Experian** | One of three main bureaus |
| **Equifax** | Bureau + The Work Number (verification) |
| **TransUnion** | Bureau |
| **Fair Isaac (FICO)** | Score model provider (NYSE: FICO) |
| **VantageScore** | Joint-venture score from three bureaus |

### Tri-Merge Resellers
- **Credit Plus, Factual Data, MeridianLink (CBC), Birchwood, Xactus** — pull and merge bureau data for lenders

---

## Vertical 12 — Title Insurance & Closing

**Focus:** Confirm clean title; insure against title defects; manage the closing process.

### Major Title Insurance Underwriters
| Company | Notes |
|---|---|
| **Fidelity National Financial (FNF)** | NYSE: FNF; largest |
| **First American Financial (FAF)** | NYSE: FAF |
| **Old Republic International** | NYSE: ORI |
| **Stewart Information Services** | NYSE: STC |
| **Doma** (formerly States Title) | Tech-forward; struggled post-IPO |

### Closing Software / RON
| Company | Notes |
|---|---|
| **Qualia** | Cloud-native closing software; largest standalone |
| **SoftPro** (FNF subsidiary) | Long-incumbent |
| **ResWare** | (acquired by Qualia) |
| **RamQuest** (FNF) | |
| **Snapdocs** | Closing coordination |
| **Notarize / Proof.com** | RON (remote online notarization) |
| **NotaryCam** | RON |
| **Pavaso** | eClose + RON |
| **DocuSign** | eSignature backbone |
| **Stavvy** | Modern eClose |

---

## Vertical 13 — Document Processing / AI / Compliance

**Focus:** Generate disclosures, manage closing documents, run compliance checks.

### Disclosure / Doc-Prep
| Company | Notes |
|---|---|
| **DocMagic** | Leading doc-prep |
| **IDS** (International Document Services) | |
| **Compliance Systems** | |
| **Wolters Kluwer** | ComplianceEase, Expere |
| **Mavent** (Ellie Mae / ICE) | |

### Compliance / Audit
| Company | Notes |
|---|---|
| **LoanLogics** (Sutherland) | Loan QC |
| **ARMCO ACES** | Audit / QC |
| **TRK Connection** | |
| **MQMR** | Mortgage Quality Management Research |

### AI / Doc Intelligence
| Company | Notes |
|---|---|
| **Tavant** | AI for income calc, doc processing |
| **Capacity** | AI assistant |
| **Sora Finance** | Document AI |
| **Ocrolus** | Doc OCR/extraction |
| **Brace** | Loss-mit automation |

---

## Vertical 14 — Mortgage Insurance (MI)

**Focus:** Insure lenders against borrower default on loans with > 80% LTV.

### Major Private MI Companies
| Company | Notes |
|---|---|
| **MGIC Investment Corporation** | NYSE: MTG |
| **Radian Group** | NYSE: RDN |
| **Enact Holdings** (formerly Genworth MI) | NASDAQ: ACT |
| **Essent Guaranty** | NYSE: ESNT |
| **National MI (NMI Holdings)** | NASDAQ: NMIH |
| **Arch Mortgage Insurance** | Part of Arch Capital |

### Government Equivalents
- **FHA** mortgage insurance (HUD)
- **VA** loan guaranty (VA)
- **USDA** Rural Development guarantee

---

## Vertical 15 — TPO Platforms (Broker-Side Tech)

**Focus:** The software brokers use to submit loans to wholesale lenders.

### Major Players
| Company | Notes |
|---|---|
| **ARIVE** | Independent TPO platform |
| **UWM EASE / Bolt / Boost** | UWM's proprietary tools (broker-must-use) |
| **Rocket Pro TPO** | Rocket's broker channel |
| **Floify** | Borrower-facing POS popular with brokers |
| **LendingPad** | LOS with TPO functionality |
| **Maxwell** | POS for smaller lenders + broker |
| **LoanScorecard** | AUS / pricing engine for non-QM |
| **Connexions (LenderPrice)** | Multi-investor broker platform |

---

## Vertical 16 — Marketplaces / Consumer Lead Gen

**Focus:** Consumer-facing comparison sites; send leads to lenders for compensation.

### Major Players
| Company | Notes |
|---|---|
| **LendingTree** | NASDAQ: TREE; classic lead marketplace |
| **Bankrate** (Red Ventures) | Comparison content + lead gen |
| **NerdWallet** | NASDAQ: NRDS |
| **Credible** | Owned by Fox |
| **Owning** | Acquired by Guaranteed Rate 2021 |
| **MoneyTips** | Owned by Red Ventures |
| **Better Mortgage** (consumer-direct) | NASDAQ: BETR |

---

## Vertical 17 — Default Management / Loss Mitigation

**Focus:** Manage delinquent loans — modifications, short sales, foreclosures, REO disposition.

### Major Players
| Company | Notes |
|---|---|
| **Black Knight (ICE) Default Solutions** | Major in-house at ICE |
| **Sagent** | Default workflow |
| **Brace** | Loss-mit AI |
| **Sourcepoint** | Outsourced operations |
| **Auction.com** | REO disposition marketplace |
| **Hubzu** (Altisource) | REO marketplace |
| **Servis1st / ServiceMac** | Servicer-attached default ops |

---

## Vertical 18 — GSEs, Government, and Regulators

**Focus:** Set the rules, guarantee the loans, regulate the industry.

### GSEs / Government Loan Securitizers
| Entity | Focus |
|---|---|
| **Fannie Mae** | Conventional conforming MBS |
| **Freddie Mac** | Conventional conforming MBS (UMBS jointly with Fannie) |
| **Ginnie Mae** | Government-backed (FHA/VA/USDA) MBS |
| **FHA / HUD** | Insures FHA loans |
| **VA (Veterans Affairs)** | Guarantees VA loans |
| **USDA Rural Development** | Guarantees USDA loans |

### Federal Regulators
| Entity | Authority |
|---|---|
| **CFPB** (Consumer Financial Protection Bureau) | TRID, Reg Z, RESPA |
| **FHFA** (Federal Housing Finance Agency) | Oversees Fannie/Freddie; sets CLL; sets LLPAs |
| **OCC** (Office of the Comptroller of Currency) | National bank regulator |
| **FDIC** | Deposit insurance + state-chartered banks |
| **Federal Reserve** | Bank holding companies; rate policy |
| **HUD** | FHA + fair-housing |
| **DOJ / FTC** | Antitrust |

### State / Industry
- **NMLS** (Nationwide Multistate Licensing System) — broker/LO licensing
- **CSBS** (Conference of State Bank Supervisors) — operates NMLS
- **MBA** (Mortgage Bankers Association) — industry trade association
- **NAMB** (National Association of Mortgage Brokers) — broker trade
- **NAR** (National Association of Realtors) — agent trade

---

## Quick Cross-Reference: Who Owns What (2026)

| Parent | Owns |
|---|---|
| **ICE** (NYSE: ICE) | Encompass, MSP, MERS, Simplifile, AllRegs, Velocify, eMBS, ICE Data Services |
| **Constellation Software** | Optimal Blue (Perseus), Empower LOS (CFM), many small verticals |
| **Stone Point Capital + Insight Partners** | CoreLogic (taken private 2021) |
| **Fidelity National Financial** | First American (no — separate), SoftPro, RamQuest, ServiceLink, several title brands |
| **First American Financial** | Data Tree, Docutech, others |
| **Zillow Group** | Zillow Home Loans, Mortech, Trulia, StreetEasy |
| **News Corp** | Realtor.com (Move Inc.) |
| **Rocket Companies** | Rocket Mortgage; (announced 2025) Mr. Cooper, Redfin |
| **Black Knight (within ICE)** | All BK assets except divested Optimal Blue & Empower |
| **CoStar Group** | Homes.com, Apartments.com, LoopNet |
| **Warburg Pincus + Fiserv** | Sagent |

---

## Mental Model: The Mortgage Stack

```
┌─────────────────────────────────────────────────────────────┐
│ CONSUMER DISCOVERY                                          │
│ Zillow, Redfin, Realtor.com, NerdWallet, LendingTree        │
├─────────────────────────────────────────────────────────────┤
│ LEAD / POS                                                  │
│ Blend, Maxwell, Floify, SimpleNexus                         │
├─────────────────────────────────────────────────────────────┤
│ PRICING / LOCK                                              │
│ Optimal Blue, LoanSifter, Polly, EPPS, LenderPrice          │
├─────────────────────────────────────────────────────────────┤
│ LOS (System of Record)                                      │
│ Encompass (ICE), Empower, Calyx, LendingPad, ARIVE          │
├─────────────────────────────────────────────────────────────┤
│ UNDERWRITING                                                │
│ DU (Fannie), LPA (Freddie), TOTAL, GUS (USDA)               │
├─────────────────────────────────────────────────────────────┤
│ VERIFICATIONS                                               │
│ The Work Number, Plaid, FormFree, Argyle, Truework          │
├─────────────────────────────────────────────────────────────┤
│ VALUATION                                                   │
│ CoreLogic, Class Valuation, Clear Capital, Reggora          │
├─────────────────────────────────────────────────────────────┤
│ CREDIT                                                      │
│ Experian, Equifax, TransUnion, FICO                         │
├─────────────────────────────────────────────────────────────┤
│ MI                                                          │
│ MGIC, Radian, Enact, Essent, NMI, Arch                      │
├─────────────────────────────────────────────────────────────┤
│ DOCS / COMPLIANCE                                           │
│ DocMagic, IDS, Wolters Kluwer, LoanLogics                   │
├─────────────────────────────────────────────────────────────┤
│ TITLE / CLOSING                                             │
│ FNF, First American, Old Republic, Qualia, Notarize         │
├─────────────────────────────────────────────────────────────┤
│ FUNDING / REGISTRY                                          │
│ MERS (ICE), Simplifile (ICE)                                │
├─────────────────────────────────────────────────────────────┤
│ CAPITAL MARKETS / HEDGE                                     │
│ MCT, Vice Capital, OB Hedge, Polly Capital                  │
├─────────────────────────────────────────────────────────────┤
│ INVESTORS / GSEs                                            │
│ Fannie, Freddie, Ginnie; Pennymac, AmeriHome, Wells          │
├─────────────────────────────────────────────────────────────┤
│ SERVICING                                                   │
│ MSP (ICE), Sagent, ICE Servicing Digital, FICS              │
├─────────────────────────────────────────────────────────────┤
│ DEFAULT MGMT                                                │
│ ICE Default, Brace, Sagent, Auction.com, Hubzu              │
├─────────────────────────────────────────────────────────────┤
│ DATA & ANALYTICS (cross-cutting)                            │
│ CoreLogic, ICE Data, ATTOM, HouseCanary, eMBS               │
└─────────────────────────────────────────────────────────────┘
```

Every loan touches most of these layers. Owning a layer with **strong network effects** (LOS, PPE, servicing, registry) is the most defensible business in the industry — which is why ICE rolled up so many of them.

---

## Key Industry-Wide Observations

1. **Consolidation pressure is structural.** Mortgage tech is a low-growth, recurring-revenue, integration-heavy market. PE roll-ups (Constellation, GTCR, Thoma Bravo) and strategic giants (ICE) both thrive here.

2. **Most innovation comes from outside.** New entrants (Polly, Blend, Better, Qualia, Sagent) keep pressure on incumbents. The biggest companies (ICE) lead by acquisition, not invention.

3. **Networks are the moats.** MERS, Encompass network, Ellie Mae Network, MSP, Optimal Blue — these are valuable because *everyone else* connects to them, not because their software is uniquely good.

4. **Regulatory complexity is a feature, not a bug, for incumbents.** Every new Reg Z update, every LLPA redesign, every TRID amendment increases the cost of entry — moats deepen for those already in.

5. **Watch the GSEs.** Most pricing economics flow from Fannie/Freddie's LLPA matrix and pricing engines (DU, LPA). When they change rules (2023 LLPA redesign), the whole industry resets.
