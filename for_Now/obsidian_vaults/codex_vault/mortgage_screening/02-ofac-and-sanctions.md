# 02. OFAC and Sanctions

## What OFAC Is

OFAC is the U.S. Treasury office that administers and enforces economic sanctions.

In mortgage lending, OFAC screening is about this question:

```text
Are we dealing with a blocked or sanctioned person, entity, country, or other restricted party?
```

This is not normal credit underwriting.

Credit underwriting asks:

```text
Can the borrower repay?
```

OFAC asks:

```text
Are we legally allowed to transact with this party?
```

## What Gets Checked

The most familiar OFAC list is the SDN list, but OFAC also publishes consolidated sanctions data and other lists.

Common screening inputs:

```text
Full legal name
Aliases
Date of birth
Address
Country
Citizenship or nationality when collected
Business name
Tax ID / entity identifiers when applicable
Beneficial owners / control persons when applicable
```

## Who Might Be Screened

For a mortgage transaction, policy may require OFAC screening on:

```text
Borrower
Co-borrower
Guarantor
Seller
Business entity borrower
Trusts and trustees
Power-of-attorney parties
Settlement agent
Title company
Broker or broker company
Vendors
Servicing counterparties
Payment recipients
```

The key point:

```text
OFAC risk is not only about the borrower.
It can attach to other parties in the transaction.
```

## What a Match Means

There are two very different things:

```text
Possible match
True match
```

A possible match might be caused by a similar name.

Example:

```text
Borrower name: John Smith
OFAC record: John Smith with different DOB, country, address, and alias pattern
```

That may be a false positive.

A true match means the identifiers line up enough that the compliance team treats it as the sanctioned party.

## What to Do With a Possible Match

Typical workflow:

```text
Pause normal clearance.
Compare identifiers.
Collect missing identifiers if allowed and needed.
Escalate to compliance / sanctions officer.
Document the decision.
Only clear the hit when the false positive is explainable.
```

Do not treat a name match alone as final.

Do not ignore it either.

## What to Do With a True Match

A true OFAC match is a serious escalation.

The lender may need to:

```text
Block or reject the transaction depending on the sanctions program.
Avoid closing or funding without legal/compliance clearance.
Report blocked or rejected transactions when required.
Preserve records.
Ask OFAC for guidance or a license if appropriate.
```

In practical lending language:

```text
OFAC true match = stop the conveyor belt.
```

## When to Run OFAC

Common checkpoints:

```text
At application or file setup
When a new party is added
Before clear-to-close
Before funding
Before sale / delivery to investor or GSE
During servicing / portfolio monitoring
Before paying or transferring funds to a party
```

The reason for repeat checks is simple:

```text
Names can be added to sanctions lists after the loan starts.
Transaction parties can change.
The lender needs evidence that the loan was clean at the important control points.
```

## OFAC vs FraudGuard-Style Tools

OFAC:

```text
Legal restriction / sanctions risk.
True match can stop the transaction.
```

FraudGuard-style tool:

```text
Fraud-risk signal.
Alert usually requires investigation, not automatic denial.
```

They are both screening controls, but they are not the same animal.

## Source Links

See [07-sources.md](07-sources.md) for official links to OFAC sanctions tools and guidance.

