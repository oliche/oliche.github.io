---
layout: page
breadcrumb: true
title:  "Spatial Aliasing"
subheadline:  "Survey Design"
teaser: "Elementary."
categories:
    - seismic_design
tags:
    - design
image:
   thumb: "thumb_design.jpg"
header:
    image_fullwidth: "seismic_acquisition_header.png"
---

The Shannon/Nyquist theorem states that to fully sample an analog signal, the sampling interval should be at least half of the shortest period in the signal.

$$
F_{alias}=\frac{V}{2d}
$$

Where $$F_{alias}$$ is the aliased frequency, $$V$$ the linear event velocity, and $$d$$ the point spacing.

$$
N=\frac{dF}{V}
$$

Gives the number of rounds of aliasing $$N$$: how many times the plane wave crosses the $$k=0$$ axis in the F-K domain.

