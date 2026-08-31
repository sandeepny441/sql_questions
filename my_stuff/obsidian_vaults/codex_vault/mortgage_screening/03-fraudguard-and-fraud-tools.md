# 03. FraudGuard and Fraud Tools

## What FraudGuard-Style Tools Do

FraudGuard-style products are mortgage fraud-risk tools.

They usually aggregate data and produce alerts around:

```text
Identity
Social Security number patterns
Address history
Employment
Income reasonableness
Occupancy
Property ownership
Property flipping
Valuation risk
Undisclosed relationships
Prior fraud indicators
Public records
Bankruptcy / liens / judgments when available
Deceased-person indicators
OFAC or sanctions screening when bundled
```

The exact data depends on the vendor and product configuration.

## The Key Difference From OFAC

OFAC is a legal sanctions screen.

FraudGuard-style tools are risk screens.

That means:

```text
OFAC true match:
  You may be legally prohibited from transacting.

Fraud alert:
  The file needs review, verification, or escalation.
```

A fraud alert should not automatically mean:

```text
Decline the loan.
```

It usually means:

```text
Do not ignore this. Resolve it before moving forward.
```

## Common Alert Categories

### Identity Alerts

Examples:

```text
SSN does not match identity pattern.
Borrower address history is inconsistent.
Borrower appears associated with deceased-person data.
Name, DOB, or address conflicts with other records.
```

Common clearance steps:

```text
Verify identity documents.
Use trusted third-party verification.
Ask for explanation or supporting documentation.
Escalate if documents look altered or inconsistent.
```

### Occupancy Alerts

Examples:

```text
Borrower claims primary residence but owns another nearby primary residence.
Mailing address does not fit occupancy story.
Employment location and subject property location do not make sense.
```

Common clearance steps:

```text
Document reason for move.
Verify relocation, family change, job change, or lease termination.
Look for undisclosed investment-property intent.
```

### Property / Valuation Alerts

Examples:

```text
Recent property flip.
Rapid price increase.
Unusual seller relationship.
Prior transfer at much lower value.
Multiple related transactions.
```

Common clearance steps:

```text
Review chain of title.
Review appraisal support.
Check seller relationship.
Require additional valuation support when policy requires it.
```

### Employment / Income Alerts

Examples:

```text
Employer address is residential or virtual.
Borrower appears connected to employer ownership.
Income does not fit job title or industry.
Employment phone number cannot be independently verified.
```

Common clearance steps:

```text
Independently verify employer.
Use tax transcripts or approved income verification.
Look for self-employment or related-party employment.
Escalate suspected fabricated employment.
```

### Transaction Relationship Alerts

Examples:

```text
Borrower and seller share an address.
Borrower and appraiser appear connected.
Broker, seller, or borrower appear in prior suspicious transactions.
Repeated use of same parties across risky files.
```

Common clearance steps:

```text
Identify the relationship.
Determine whether it was disclosed.
Check investor and agency rules.
Escalate undisclosed conflicts.
```

## Before-Closing Use

Before closing, fraud tools help answer:

```text
Is the borrower real?
Is the employment real?
Is the property story real?
Is the occupancy story real?
Are the transaction parties connected in a risky way?
```

The goal is to prevent funding a defective or fraudulent loan.

## After-Closing Use

After closing, fraud tools and post-close reviews help answer:

```text
Did we miss something?
Is the loan deliverable?
Is there a reportable fraud finding?
Do we need to notify an investor, insurer, agency, or law enforcement?
Do we need to repurchase, indemnify, cure, or monitor?
```

Post-closing fraud can appear through:

```text
Early payment default
Quality control re-verification
Investor audit
Borrower complaint
Servicing contact
Returned mail
Payment pattern
Third-party tip
```

## Important Compliance Caution

If a vendor report is used in a way that affects credit eligibility, pricing, or adverse action, the lender should understand whether consumer-reporting, adverse-action, fair lending, privacy, and notice rules apply.

In plain English:

```text
Do not let a black-box fraud score silently decide the loan.
Resolve the facts and document the reason.
```

## Source Links

See [07-sources.md](07-sources.md) for vendor and regulatory source links.

