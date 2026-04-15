i Team,

Sharing a structured overview of how we designed the group assignment for the pricing A/B test, along with the reasoning behind the approach and what it means for our analysis.

1. Core Experimental Design Strategy
	•	We used a matched-pair assignment approach to construct control and treatment groups by pairing Loan Officers with highly similar profiles (performance, volume, loan mix, etc.)
	•	This was driven using an optimization-based framework to ensure tight comparability rather than relying on chance balance
	•	The goal was to create pre-balanced groups, so any observed differences can be more directly attributed to the pricing strategy rather than underlying LO variability

2. How This Differs from Traditional A/B Testing
	•	A standard A/B test relies on randomization alone, assuming that differences average out across large samples
	•	In our case, the LO population is highly heterogeneous, and certain segments are relatively small — making pure randomization prone to imbalance
	•	By matching first and then assigning, we effectively reduce variance upfront, leading to clearer, more stable measurement without heavy reliance on post-hoc adjustments

3. Practical Challenges and How We Addressed Them
	•	Not all LOs could be cleanly matched — about 23% were either inactive (limited data) or had highly unique profiles
	•	Instead of excluding them (which would shrink scope and introduce bias), we took a hybrid approach:
	•	Relaxed matching constraints selectively to recover additional high-quality pairs
	•	Assigned the remaining LOs using stratified randomization within comparable tiers (e.g., PRO segments)
	•	This ensured full population coverage, while still preserving as much balance as possible across groups

4. Key Takeaways for Analysis
	•	Lower-volume LOs: High match quality and consistency across this segment → expected to provide the most stable and reliable signal
	•	Higher-volume LOs: Greater variability and uniqueness → harder to match, so results should be interpreted with additional context
