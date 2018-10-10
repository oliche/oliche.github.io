---
layout: page
breadcrumb: true
title:  "Statistics"
subheadline: "Maths"
teaser: "A hodgepodge of basic survival skills in statistics"
categories:
    - seismic_maths
image:
   thumb: "thumb_maths.png"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---
## Definitions
-	The **Sample Space** $$\mathcal{S}$$ is the set of all possible outcomes.
-	A **Random Variable** $$x$$ assigns quantities to outcomes $$\mathcal{O}$$. For example a fair dice has one sixth probability for the quantity 6.
-	An **Event** $$\mathcal{E}&& is a set of outcomes.
-	The **Probability Distribution** is the cumulative **Probability density function** and tends to 1 at infinity.

## Bayes Theorem
Short version:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

Full version:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(A)P(B|A)+P(B|\neg A)(1-P(A))}
$$


### Example: breast cancer from N.Silver
A woman has roughly 1.4% Chance of devlopping breast cancer in her forties, this is the prior $$P(A)$$.
If she does a mammogramm, there is a 10% rate of false positives $$(P(B|\neg A)$$, and 75% percent of true positives $$P(B|A)$$.

Applying Bayes Theorem,

$$
P(A|B) = \frac{P(B|A)P(A)}{P(A)P(B|A)+P(B|\neg A)(1-P(A))}= \frac{0.75 \times 0.014}{0.014 \times 0.75 + 0.1 \times (1-0.014)} = 9.62\%
$$


The chance of that a woman in her forties has breast cancer given she's had a positive mammogram is still low, around 10%.


## Independence example from N. Silver

Each pool contains 5 securities that each have a 5% chance of default. The probability of loosing the bet depends drastically on the assumption of correlation between the securities.

| Bet          | Rules                        | No Correlation | Perfect Correlation |
|--------------|------------------------------|----------------|---------------------|
| Alpha Pool   | Bet lost if 5 on 5 defaults  | 0.00003%       | 5%                  |
| Beta Pool    | Bet lost if 4+ on 5 defaults | 0.003%         | 5%                  |
| Gamma Pool   | Bet lost if 3+ on 5 defaults | 0.1%           | 5%                  |
| Delta Pool   | Bet lost if 2+ on 5 defaults | 2.1%           | 5%                  |
| Epsilon Pool | Bet lost if 1+ on 5 defaults | 20.4%          | 5%                  |


``` matlab
	n = [1:5]';
	p = 0.05;
	res = (p.^n .* (1-p).^(5-n)) .* factorial(5)./factorial(max(5-n,n))./max(1,min(5-n,n));
	sprintf('%10f',res*100)
```

## Simpson's Paradox from J.Pearl
When an event $$C$$ increases the probability of $$E$$ in a given population $$p$$ and, at the same time, decreases the probability of $$E$$ in every subpopulation of $$p$$. For complementary properties  $$F$$ and $$\neg F$$ of two subpopulations, we may encounter the inequalities:

$$
\begin{align}
P(E|C) > P(E | \neg C) \\\\
P(E|C,F) < P(E | \neg C, F) \\\\
P(E|C, \neg F) < P(E | \neg C, \neg F)\\\\
\end{align}
$$

Here is an example where $$F$$ and $$\neg F$$ are the gender of individuals, $$C$$ and $$\neg C$$ the test and control groups and $$E$$ the recovery.


| **Combined**         | $$E$$ | $$\neg E$$ |    | Recovery Rate |
|----------------------|-------|----------|----|---------------|
| Drug ($$C$$)         | 20    | 20       | 40 | 50%           |
| No drug ($$\neg C$$) | 16    | 24       | 40 | 40%           |
|                      | 36    | 44       | 80 |               |

| **Males**          | $$E$$ | $$\neg E$$ |    | Recovery Rate |
|--------------------|-----|----------|----|---------------|
| Drug ($$C$$)         | 18  | 12       | 30 | 60%           |
| No drug ($$\neg C$$) | 7   | 3        | 10 | 70%           |
|                      | 25  | 15       | 40 |               |

| **Females**        | $$E$$ | $$\neg E$$ |    | Recovery Rate |
|--------------------|-----|----------|----|---------------|
| Drug ($$C$$)         | 2   | 8        | 10 | 20%           |
| No drug ($$\neg C$$) | 9   | 21       | 30 | 30%           |
|                      | 11  | 29       | 40 |               |

In this case the main factor of recovery is the gender, so a disproportion of males in the combined sample leaves the impression that the drug is benefecial while it is really harmful.


### References and Further Reading

J. Pearl. Causality: Models, Reasoning and Inference. Second Edition.

N. Silver. The Signal and the Noise: Why So Many Predictions Fail but Some Don't.