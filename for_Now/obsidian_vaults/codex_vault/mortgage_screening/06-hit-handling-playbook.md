# 06. Hit Handling Playbook

## The Basic Rule

Do not treat every hit the same way.

First ask:

```text
What kind of hit is this?
```

Then ask:

```text
Is it a real match?
What rule or investor requirement applies?
Can it be cleared?
Who must approve the clearance?
What evidence do we keep?
```

## Step 1: Classify the Hit

| Hit Type | Typical Meaning | First Move |
|---|---|---|
| OFAC / sanctions | Possible legal restriction | Stop normal clearance and escalate |
| Fraud alert | Risk signal | Investigate and resolve facts |
| HUD LDP / SAM / FHFA / GSE exclusion | Possible program or investor ineligibility | Check exact party, role, and rule |
| CAIVRS | Possible government-loan eligibility problem | Confirm borrower and program rules |
| NMLS / licensing issue | Originator or company may lack authority | Verify status and state/product coverage |
| Internal watchlist | Institution-specific restriction | Follow internal policy and governance |

## Step 2: Verify Identity

For person matches, compare:

```text
Full name
Aliases
Date of birth
SSN or tax ID when appropriate
Address
Country
Employer or business affiliation
Role in transaction
Known identifiers from the list
```

For entity matches, compare:

```text
Legal name
DBA names
Tax ID
Address
State of organization
Control persons
Beneficial owners
Affiliates
```

## Step 3: Decide the Disposition

Common dispositions:

```text
False positive
Cleared with documentation
More information required
Escalated to compliance
Escalated to fraud investigation
Party removed or replaced
Loan suspended
Loan declined / not eligible
Transaction blocked or rejected
Report filed
Investor / agency notified
Internal watchlist updated
```

## OFAC Hit Handling

Possible OFAC hit:

```text
Compare identifiers.
Do not rely on name alone.
Escalate to sanctions compliance.
Document the false-positive rationale if cleared.
```

True OFAC hit:

```text
Stop the normal loan process.
Do not fund, pay, transfer, or close without compliance/legal clearance.
Block or reject when required.
Report when required.
Preserve records.
```

Plain English:

```text
OFAC is not "ask for one more document and move on."
OFAC is "pause and let the sanctions process control the next step."
```

## Fraud Tool Hit Handling

Fraud alert:

```text
Read the alert.
Map it to a fact in the file.
Ask what would make the alert harmless.
Ask what would make it serious.
Collect independent evidence.
Document the conclusion.
Escalate unresolved or suspicious facts.
```

Example:

```text
Alert: Employer phone number cannot be independently verified.

Weak clearance:
  Borrower says it is fine.

Stronger clearance:
  Employer verified through independently sourced phone number,
  payroll records support income,
  tax transcript or approved verification source agrees,
  no related-party employment issue remains.
```

## Exclusion Hit Handling

Exclusion list hit:

```text
Confirm exact person/entity.
Confirm role in transaction.
Confirm which program/investor rule applies.
Determine whether the party can be removed or replaced.
Document investor or agency guidance if needed.
```

Example:

```text
If an appraiser is ineligible, the issue may be solved by using an eligible appraiser and following appraisal independence rules.

If the borrower is ineligible under the program, replacing the party is not possible.
```

## CAIVRS Hit Handling

CAIVRS hit:

```text
Confirm the borrower.
Confirm the debt/default source.
Check whether the program allows a resolution or exception.
Document the clearance before approval.
```

Plain English:

```text
CAIVRS is often about federal credit eligibility, not general character.
```

## NMLS / Licensing Hit Handling

NMLS or license issue:

```text
Confirm the MLO/company.
Confirm state coverage.
Confirm license status and sponsorship.
Confirm whether the person touched the loan in a licensed capacity.
Escalate if the loan was originated by an unlicensed or unauthorized party.
```

## SAR / AML Escalation

Mortgage lenders and originators covered by FinCEN rules may have AML program and suspicious activity reporting obligations.

Possible triggers:

```text
Suspected identity theft
Straw buyer indicators
Fabricated employment
Occupancy fraud
Altered documents
Suspicious source of funds
Unusual transaction relationships
Possible money laundering
Fraud discovered after closing
```

Important:

```text
Do not tell the borrower or transaction party that a SAR was or may be filed.
Escalate internally according to AML policy.
```

## What Good Documentation Looks Like

A good resolution note says:

```text
What list/tool hit occurred.
Who or what matched.
Which identifiers matched or did not match.
What evidence was reviewed.
Who reviewed it.
What policy/rule was applied.
What final action was taken.
Why the file is cleared or not cleared.
```

Bad resolution note:

```text
Cleared.
```

Better resolution note:

```text
OFAC possible match to same name reviewed.
DOB, address, nationality, and alias data do not match OFAC record.
Compliance reviewer cleared as false positive on 2026-06-28.
Evidence retained in file.
```

## The Core Habit

Every hit should become one of three things:

```text
Resolved
Escalated
Stopped
```

It should not become:

```text
Ignored
```

