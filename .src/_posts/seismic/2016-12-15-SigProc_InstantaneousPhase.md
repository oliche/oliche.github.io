---
layout: page
breadcrumb: true
title:  "Instantaneous Phase and Frequency "
subheadline: "Signal Processing"
categories:
    - seismic_processing
tags:
    - phase
    - signal processing
image:
   thumb: "thumb_processing.jpg"
header:
    image_fullwidth: "Banner_Wave.jpg"
---


The analytic signal $$S_a(t)$$ is a complex representation of a real time serie $$S(t)$$. Its real part is the signal $$S(t)$$

$$
\Re{ \{S_a(t)\} } = S(t)
$$

while its imaginary part is the Hilbert transform of $$S(t)$$.

$$
\Im{\{S_a(t)\}} = Hilbert(S(t)) 
$$

The Euler decomposition (argument and magnitude) of the analytic signal have  useful applications.

$$
S_a(t) = \|{S_a(t)}\| . e^{(i\varphi)}
$$

$$\|{S_a(t)}\|$$ is referred to as the Envelope of $$S(t)$$.
$$\varphi$$ is referred to as the Instantaneous Phase of $$S(t)$$.

The Instantaneous Frequency $$IF$$ (especially meaningful for sweeps) is the time-derivative of the Instantaneous Phase.

$$
IF = \frac{d\varphi}{dt} . \frac{1}{2\pi}
$$

[link to the sweep article](todo)