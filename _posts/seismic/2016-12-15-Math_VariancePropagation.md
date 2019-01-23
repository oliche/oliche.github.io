---
layout: page
breadcrumb: true
title:  "Stacking : The Square-Root Law"
subheadline: "Maths"
teaser: "An intuitive demonstration of why random noise stacks out proportionally to the square-root of the stacking fold."
categories:
    - maths
tags:
    - noise
image:
   thumb: "thumb_maths.png"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---

If $$f$$ is a function of two Gaussian variables,

$$
y = f(x_1,x_2)
$$

the variance propagates according to the norm of partial derivatives weighted with covariances [NIST engineering statistics handbook](http://www.itl.nist.gov/div898/handbook/):

$$
\sigma_y = \sqrt{\bigg(\frac{\partial{y}}{\partial{x_1}}\bigg)^2\sigma^2_{x_1} + \bigg(\frac{\partial{y}}{\partial{x_2}}\bigg)^2\sigma^2_{x_2} + ... + \bigg(\frac{\partial{y}}{\partial{x_1}}\bigg).\bigg(\frac{\partial{y}}{\partial{x_2}}\bigg)\sigma_{x_1x_2}^2}
$$

For a $$n$$ repeated experiments with noise of constant variance throughout, the equation simplifies to 

$$
y = \sum_n{x_n};
$$

$$
\sigma_y^2 = \sum_n{\sigma_n} = n\sigma^2;
$$

The variance of the noise is reduced by a $$\sqrt{n}$$ factor, the square-root of the stack-order :

$$
\sigma_y = \sqrt{n}.\sigma;
$$

