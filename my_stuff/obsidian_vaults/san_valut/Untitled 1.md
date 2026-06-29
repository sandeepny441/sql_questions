Goal of a Decision Tree

A decision tree asks questions like:

* “Is age > 30?”
* “Is income high?”
* “Did the person click the ad?”

And tries to split the data into “pure” groups.

“Pure” means:

* almost all Yes
    or
* almost all No

⸻

Tiny Dataset

Suppose we want to predict:

Will the person buy a laptop?

Person	Age	Buy Laptop
A	Young	No
B	Young	No
C	Middle	Yes
D	Old	Yes

We have:

* 2 Yes
* 2 No

⸻

Step 1 — Measure Disorder

Decision trees first measure:

“How mixed up is the data?”

This is called impurity.

The most common formula is:

Entropy

Entropy = -p_1 \log_2(p_1) - p_2 \log_2(p_2)

Where:

* p_1 = probability of Yes
* p_2 = probability of No

⸻

Step 2 — Entropy Before Splitting

We have:

* Yes = 2
* No = 2
* Total = 4

So:

$p(Yes)=\frac{2}{4}=0.5$


p(No)=\frac{2}{4}=0.5

Now plug into formula:

Entropy = -(0.5)\log_2(0.5) -(0.5)\log_2(0.5)

We know:

\log_2(0.5) = -1

So:

Entropy = -(0.5)(-1) -(0.5)(-1)

=0.5+0.5

=1

⸻

Meaning

`Entropy = 1 means:`

`“Very mixed.”`
`We are uncertain.`

`Half Yes, half No.`


⸻

Step 3 — Try a Split

Suppose we split by:

“Age = Young?”

Left Side

Person	Buy
A	No
B	No

All are No.

%% Entropy becomes: %%


Entropy = -(1)\log_2(1)

Since:

\log_2(1)=0

Entropy:

=0

Perfect purity.

⸻

Right Side

Person	Buy
C	Yes
D	Yes

Again all Yes.

Entropy:

=0

⸻

Step 4 — Total Entropy After Split

Weighted average:

\frac{2}{4}(0)+\frac{2}{4}(0)

=0

⸻

Step 5 — Information Gain

Decision trees compare:

* Entropy before split
    vs
* Entropy after split

Formula

Information\ Gain
=
Entropy_{before}
-
Entropy_{after}

So:

1 - 0 = 1

Huge improvement.

⸻

Big Picture

The tree is basically asking:

“Which question reduces confusion the most?”

That is all.

⸻

Intuition Like a 10-Year-Old

Imagine a basket with:

* red balls
* blue balls

A messy basket has mixed colors.

A good split separates:

* red on one side
* blue on the other

Decision trees are just repeatedly asking:

“Which question separates the colors best?”