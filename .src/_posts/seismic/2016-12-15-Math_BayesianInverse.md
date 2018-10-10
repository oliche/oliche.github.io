---
layout: page
breadcrumb: true
title:  "The Least-Squares Criterion in Inverse Problems"
subheadline: "Maths"
teaser: "How to include uncertainties in the model and data spaces."
categories:
    - seismic_maths
tags:
    - inversion
    - Bayes
image:
   thumb: "thumb_maths.png"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---


The full expression for the updated model $$\tilde{m}$$ is given with priors and posterior covariance matrices $$C_D, C_m$$ :

$$
\tilde{m} = m_{prior} + C_M G^T \Big(G C_M G^T + C_D \Big)^{-1} \Big(d_{obs} - Gm_{prior} \Big)
$$

$$
\tilde{C_M} = C_M - C_M G^T \Big(G C_M G^T + C_D\Big)^{-1} G C_M
$$


### References and further reading :
_Inverse Problem Theory and Methods for Model Parameter Estimation_. Albert Tarantola.
Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2004. ISBN 0898715725. Available [here.](http://www.ipgp.fr/~tarantola/)
