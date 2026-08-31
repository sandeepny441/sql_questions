# 01. Landscape

## The Big Idea

Before a lender grants a loan, it is not only asking:

```text
Can the borrower repay?
Is the collateral good?
Is the loan salable?
```

It is also asking:

```text
Are we allowed to do business with everyone in this transaction?
Is anyone excluded from a government or investor program?
Does the file show fraud risk?
Do we need to file or escalate anything?
```

That is the screening landscape.

## Five Different Screening Buckets

### 1. Sanctions / OFAC

This is the highest-severity category.

OFAC screening asks:

```text
Is this person, business, country, vessel, or entity blocked or sanctioned?
```

If there is a true match, the lender may not be allowed to proceed normally. The action may need to be blocked, rejected, reported, or escalated.

OFAC is not a normal "credit risk" list. It is a legal restrictions list.

More detail: [02-ofac-and-sanctions.md](02-ofac-and-sanctions.md)

### 2. Fraud-Risk Tools

FraudGuard-style tools are different.

They usually do not say:

```text
This person is legally forbidden.
```

They say:

```text
Something about the identity, property, employment, occupancy, transaction, or history needs review.
```

A fraud alert is not always a stop sign. Often it is a question mark that must be cleared.

More detail: [03-fraudguard-and-fraud-tools.md](03-fraudguard-and-fraud-tools.md)

### 3. Exclusion / Debarment / Ineligibility Lists

These lists ask:

```text
Is this borrower, seller, appraiser, broker, contractor, company, or other party barred from participating in this program?
```

Examples include:

```text
HUD Limited Denial of Participation
SAM exclusions
FHFA Suspended Counterparty Program
Fannie Mae / Freddie Mac exclusionary lists
Investor-specific ineligible-party lists
```

More detail: [04-exclusion-eligibility-and-watchlists.md](04-exclusion-eligibility-and-watchlists.md)

### 4. Program Eligibility Databases

These tools ask:

```text
Is the borrower eligible for this government-backed loan program?
```

Example:

```text
CAIVRS for certain federal debt / default checks on FHA, VA, USDA, and related government loan programs.
```

This is not exactly a "bad person" list. It is an eligibility control.

### 5. Licensing / Credential Checks

These checks ask:

```text
Is the broker, MLO, appraiser, settlement agent, or company licensed, approved, active, and allowed to participate?
```

Examples:

```text
NMLS
State licensing records
Investor approved-seller or approved-broker records
Appraiser independence / panel controls
Settlement agent approval controls
```

## Who Gets Screened?

Depending on the rule, investor, product, and policy, screening may cover:

```text
Borrower
Co-borrower
Non-borrowing spouse when relevant
Guarantor
Seller
Listing agent
Selling agent
Builder
Broker
Loan originator
Loan officer assistant
Processor
Appraiser
Appraisal company
Title company
Settlement agent
Escrow agent
Power-of-attorney signer
Trustee
Business entity borrower
Beneficial owners / control persons
Vendor
Servicing transfer counterparty
```

The exact scope depends on the list. OFAC might apply broadly to transaction parties. CAIVRS is borrower/program specific. NMLS is originator/license specific.

## The Core Distinction

Not all hits mean the same thing.

```text
OFAC true match:
  Possible legal prohibition. Stop and escalate.

Fraud tool alert:
  Investigate and clear or escalate. Not automatically a decline.

Exclusion list hit:
  May make a person, company, or transaction ineligible for a program or investor.

CAIVRS hit:
  May make a borrower ineligible for certain government loan programs until resolved or excepted.

NMLS/license issue:
  May mean the originator or company cannot legally handle the transaction.
```

## Before vs After Closing

Before closing, screening protects the lender from funding a loan it should not fund.

After closing, screening protects the lender from:

```text
Delivering an ineligible loan
Missing a reportable fraud event
Violating sanctions after a party becomes sanctioned
Keeping a defective loan in the pool
Ignoring servicing restrictions
Failing investor or agency requirements
```

The clean mental model:

```text
Pre-close screening = Can we make this loan?
Post-close screening = Can we sell, service, report, and keep this loan clean?
```

