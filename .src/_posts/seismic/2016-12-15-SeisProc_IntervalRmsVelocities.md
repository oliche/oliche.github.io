---
layout: page
breadcrumb: true
title:  "Interval and RMS velocities"
subheadline: "How to convert from interval to RMS velocities. And the way around."
teaser: "Seismic Processing"
categories:
    - seismic_processing
tags:
    - velocities
image:
   thumb: "thumb_processing.jpg"
header:
    image_fullwidth: "Banner_Wave.jpg"
---

The Dix conversion allows to translate RMS velocities (stacking velocities) to interval velocities (borehole velocities).

$$
V_{int(n)}= \sqrt{ \frac{ V_{rms(n)}^2\tau_{(n)} - V_{rms(n-1)}^2\tau_{(n-1)}} {\tau_{(n)}-\tau_{(n-1)}} }
$$

After re-arranging to get RMS velocities from interval velocities:

$$
V_{rms(n)}= \sqrt{ \frac{ V_{int(n)}^2(\tau_{(n)}-\tau_{(n-1)}) + V_{rms(n-1)}^2\tau_{(n-1)}} {\tau_{(n)}} }
$$

See Yilmaz, Vol 2, pp. 1534 for the full demonstration of the result.

### Further reading
Oz Yilmaz. Seismic data analysis. Society of Exploration Geophysicists, 2001.