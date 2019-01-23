---
layout: page
breadcrumb: true
title:  "Minimum Phase "
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

A system is minimum phase when it is **causal and stable**, and if its inverse is also **causal and stable**.
A filter is minimum phase when all of its poles and zeroes are inside the unit circle.

- The inverse of a minimum phase system is minimum phase.
- For a given amplitude spectrum, there is one and only one minimum phase spectrum.
- The convolution of 2 minimum phase systems is minimum phase.



```matlab
	% This computes the minimum phase of the wavelet W
	% Needs the signal processing toolbox
	W = flipud(real(ifft(exp(hilbert(real(log(fft(W))))))));
```