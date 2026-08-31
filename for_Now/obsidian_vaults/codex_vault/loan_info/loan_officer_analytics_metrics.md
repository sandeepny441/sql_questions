# Loan Officer Analytics Metrics

Representative metric framework for a wholesale lender evaluating LO and broker performance. This is not proprietary UWM reporting; it is a practical analytics checklist for production, quality, economics, risk, and growth.

## 1. LO and Broker Profile

| Submetric | What to Track | Useful Slices |
|---|---|---|
| LO identity | LO name, NMLS ID, email, phone, status | LO, branch, broker shop |
| Broker relationship | Broker company, branch, parent account, account executive | Broker, AE, region |
| Licensing footprint | Active licensed states and eligible lending markets | State, county, product |
| Tenure | Time since onboarding, first submission date, first funded loan date | New, ramping, mature, dormant |
| Role and team | LO, processor, team lead, owner, assistant relationship | Role, team, broker shop |
| Activity status | Active, new, dormant, reactivated, declining | Month, quarter, trailing 12 months |
| Contact coverage | AE touches, support contacts, training contacts | AE, contact type, outcome |
| Compliance readiness | Licensing alignment, agreement status, required credentials | State, broker, LO |

## 2. Production and Pipeline

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Applications | Count of borrower applications started or received | Month, product, LO |
| Submissions | Loans submitted to lender for review | LO, broker, channel |
| Locks | Number of locked loans and locked volume | Rate environment, product |
| Funded units | Number of closed and funded loans | Month, LO, broker |
| Funded volume | Total funded loan amount | State, product, purchase/refi |
| Average loan size | Funded volume divided by funded units | Product, geography, borrower segment |
| Pipeline balance | Active unpaid principal balance in process | Stage, expected closing month |
| Pipeline stage mix | Submitted, approved, CTC, closing, funded | LO, processor, milestone |
| Pipeline aging | Days in current stage and days since submission | Stage, file owner, exception status |
| Production momentum | Month-over-month and quarter-over-quarter trend | LO, broker, AE |

## 3. Conversion and Pull-Through

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Application-to-submission rate | Percent of applications that become submitted files | LO, product, borrower type |
| Submission-to-lock rate | Percent of submissions that lock | Product, rate period, LO |
| Lock-to-close pull-through | Percent of locked loans that fund | LO, broker, product |
| Submission-to-funding rate | End-to-end conversion from submission to funded loan | Month, LO, AE |
| Fallout rate | Locked or submitted files that do not close | Reason code, stage, product |
| Withdrawn rate | Borrower or broker withdrawn loans | LO, reason, timing |
| Denial rate | Credit or eligibility denials | Program, DTI, FICO, LTV |
| Relock rate | Loans requiring relock after expiration or fallout | LO, rate movement, product |
| Extension rate | Locks requiring extension | LO, processor, cycle time |
| Lost-loan reason | Competitive pricing, borrower changed, documentation, eligibility | Reason, competitor, stage |

## 4. Product and Borrower Mix

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Product type | Conventional, FHA, VA, USDA, jumbo, non-QM if applicable | LO, state, time period |
| Purchase vs refinance | Share of purchase, rate-term refi, cash-out refi | Market cycle, LO, realtor channel |
| Loan purpose | Purchase, refinance, construction, renovation if applicable | Product, state |
| Occupancy | Primary, second home, investment property | Product, risk tier |
| Property type | Single family, condo, PUD, 2-4 unit, manufactured | LO, county, investor |
| Borrower credit band | FICO ranges | Product, approval outcome |
| LTV and CLTV band | Leverage profile of submitted and funded loans | Product, MI status |
| DTI band | Ability-to-repay risk profile | Approval outcome, product |
| First-time buyer share | Percent of loans to first-time homebuyers | Product, geography |
| Down payment profile | Down payment percent and source of funds | Product, borrower segment |
| Assistance usage | DPA, gift funds, grants, seller credits | Program, state |

## 5. Pricing and Profitability

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Note rate | Borrower interest rate at lock and close | Product, FICO/LTV, LO |
| Price or points | Lock price, discount points, premium pricing | Product, rate period |
| Lender credits | Credits offered to borrower | LO, product, margin tier |
| Margin proxy | Gain-on-sale, SRP, or internal profitability measure | Product, broker, LO |
| Price exceptions | Exceptions, concessions, overrides, special pricing | AE, LO, exception reason |
| Competitive pressure | Cases where pricing was cited as reason for loss | Competitor, product |
| Lock extension cost | Cost and count of extensions | LO, processor, milestone delay |
| Relock cost | Economic impact of relocks | Rate movement, LO |
| Discount-heavy share | Percent of files requiring heavy discounting | Product, LO, market |
| Profitability by LO | Revenue or margin per funded unit and per funded dollar | LO, broker, cohort |

## 6. Operational Quality

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Submission completeness | Missing data or documents at first submission | LO, processor, document type |
| Conditions per file | Number of underwriting or closing conditions | LO, product, complexity |
| Touches per file | Number of underwriting, processing, or closing touches | Stage, team, LO |
| Resubmission count | Number of times a file is reworked | LO, defect type |
| Time to approval | Days from submission to conditional approval | Product, LO, processor |
| Time to clear-to-close | Days from submission or approval to CTC | Stage, condition type |
| Time to fund | Days from submission, lock, or CTC to funding | Product, LO |
| Closing delay rate | Loans delayed past expected closing date | Reason, responsible party |
| Document defect rate | Incorrect, missing, stale, or inconsistent documents | Document type, LO |
| Service escalation rate | Files requiring manager or support escalation | LO, AE, issue type |

## 7. Risk and Compliance

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Early payment default | Loans with early delinquency or default signals | LO, product, vintage |
| Repurchase exposure | Loans with repurchase, indemnification, or investor defect risk | Investor, product, LO |
| QC findings | Pre-fund and post-close quality control findings | Finding type, severity |
| Fraud flags | Identity, income, occupancy, asset, or collateral red flags | Source, LO, geography |
| Occupancy risk | Owner-occupancy inconsistencies or investor-property risk | Product, borrower profile |
| Disclosure timing | Timeliness of LE, CD, redisclosures, and change events | LO, processor, stage |
| Fee tolerance cures | Cure frequency and dollar amount | Fee type, product |
| HMDA completeness | Missing or inconsistent HMDA-reportable fields | Field, LO, broker |
| Fair-lending monitoring | Pricing, approval, and product access patterns | Protected-class proxies where permitted |
| Licensing exceptions | Loans where LO or branch licensing needs review | State, LO, broker |

## 8. Relationship and Engagement

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Portal activity | Logins, pricing searches, scenario runs, uploads | LO, broker, week |
| Scenario volume | Number of pricing or eligibility scenarios evaluated | Product, borrower segment |
| Training engagement | Webinar attendance, course completion, product education | LO, topic, completion |
| AE engagement | Calls, emails, meetings, coaching sessions | AE, LO, outcome |
| Responsiveness | Time to respond to conditions or lender requests | LO, stage, severity |
| Campaign response | Opens, clicks, registrations, submissions after campaigns | Campaign, product |
| Product adoption | Use of new products, tools, or lender programs | Product, launch cohort |
| Support tickets | Count, type, resolution time, satisfaction | Issue type, LO |
| Sentiment or feedback | Survey score, service comments, complaint themes | LO, broker, AE |
| Reactivation behavior | Dormant LO activity after outreach | Campaign, AE, market |

## 9. Market and Growth Opportunity

| Submetric | What to Track | Useful Slices |
|---|---|---|
| Geographic footprint | States, counties, MSAs, and ZIP codes served | LO, broker, market |
| Local volume trend | Production by market over time | County, state, LO |
| Purchase opportunity | Purchase share in active markets | Realtor, builder, product |
| Referral channel | Realtor, builder, past client, online, branch referral | LO, source |
| Product gap | Products the LO does not use but similar LOs do | Peer cohort, state |
| Share of wallet | Estimated lender share of LO total production | LO, broker, time period |
| Dormancy risk | Declining engagement or volume trend | LO, broker, AE |
| Growth potential score | Combined signal from market size, engagement, quality, and conversion | LO, AE, region |
| Peer benchmark | Comparison to similar LOs by market, product, or tenure | Cohort, percentile |
| Next best action | Recommended outreach, training, pricing review, or product pitch | LO, reason code |

## 10. Scorecard Outputs

| Output | Metrics Included | How It Is Used |
|---|---|---|
| LO scorecard | Volume, pull-through, speed, margin, quality, risk, engagement | Rank and monitor LO health |
| Broker account scorecard | Aggregate LO performance inside broker shop | Prioritize account coverage |
| AE book dashboard | LO and broker performance by account executive | Manage sales coverage |
| Coaching queue | LOs needing help with pricing, docs, pull-through, or product mix | Trigger targeted outreach |
| Risk watchlist | LOs or brokers with rising defects, EPD, or compliance flags | Escalate monitoring |
| Growth target list | High-quality LOs with underused products or market headroom | Drive expansion |
| Dormancy/reactivation list | Previously active LOs with recent decline | Win-back campaigns |
| Product adoption tracker | New product usage and conversion | Measure launch success |
| Service friction report | Escalations, delays, support tickets, and satisfaction | Improve operations |

