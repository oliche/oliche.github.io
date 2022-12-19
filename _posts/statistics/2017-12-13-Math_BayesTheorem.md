---
layout: page
breadcrumb: true
title:  "Bayes Theorem"
subheadline: "Maths"
teaser: "Basic notions of statistics"
categories:
    - stats
image:
   thumb: "thumb_maths.png"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---

Short version:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

Full version:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(A)P(B|A)+P(B|\neg A)(1-P(A))}
$$

This can be understood as:

$$
Posterior = \frac{Prior \times TruePositive}{Prior \times TruePositive + NotPrior \times FalsePositive}
$$



## Example: breast cancer from N. Silver
A positive breast cancer exam could sound like catastrophic news when we know the rate of false positives of the mammogram is around 10%. But for a young patient this is not always intuitively sound as the prior probability of being afflicted by cancer is low.

A woman has roughly 1.4% chance of devlopping breast cancer in her forties, this is the prior $$P(A)$$.
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


### References and Further Reading

N. Silver. The Signal and the Noise: Why So Many Predictions Fail but Some Don't.