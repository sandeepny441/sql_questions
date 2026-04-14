Subject: Twin-Pair A/B Testing Summary

Hi [Name],

Why This Approach

We are using a matched-pair A/B testing strategy instead of a broad random split.
The main reason is that loan officers differ meaningfully in baseline profile, so a standard Control vs Treatment split may not create the cleanest comparison.

How It Works

We first identify “twin” loan officers who are very similar on key pre-treatment characteristics.
Once the pair is formed, one is assigned to Control and the other to Treatment, which creates a more like-for-like experiment.

What We Match On

The pairing is based on baseline variables such as score, production, mix, purchase share, and closings.
We also keep matching strict within the same ranking bucket so the pairs are comparable both statistically and from a business standpoint.

Flow

Prepare the baseline dataset.
Find the strongest twin pairs.
Exclude weak matches or outliers instead of forcing them.
Randomly assign one twin to Control and the other to Treatment.

What We Expect to See

The two groups should look balanced before the test begins.
Each treated loan officer should have a close control counterpart, which makes later differences easier to interpret as strategy-driven.

Validation

We validate by checking pair quality, reviewing group balance, and confirming that unmatched outliers were excluded for a good reason.
After the test runs, results should be compared within pairs first and then summarized across the full experiment.

Best,
[Your Name]
