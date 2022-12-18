---
layout: page
breadcrumb: true
title:  "Correlation Amplitude Levels"
subheadline: "Signal Processing"
teaser: "What kind of normalisation can be found on correlated vibroseis data"
categories:
    - sigproc
tags:
    - vibroseis
    - signal processing
    - correlation
image:
   thumb: "thumb_processing.jpg"
header:
    image_fullwidth: "Banner_Wave.jpg"
---


In frequency domain the correlation can be written as the multiplication of uncorrelated data $$D_u$$ by the complex conjugate of the reference $$S$$ :

$$
D_c(\nu)=‎ D_u(\nu).\bar{S}(\nu)
$$

The resulting scaling amplitude of the result is obviously linked to the reference power (length, drive etc...).
Several options for the scaling :


### Normalize the correlation according to the total energy of the reference used : 

$$
D_c(\nu) = \frac{D_u(\nu).\bar{S(\nu)}}{\sum{S_n^2}}
$$

In this case the gain of the obtained "Earth Response" is independent of the reference : **all the signal is at the same level**.

### Normalize the correlation according to the signal-to-noise ratio :

$$
D_c(\nu) = \frac{D_u(\nu).\bar{S(\nu)}}{\sqrt{\sum{S_n^2}}}
$$

In this case the gain of the obtained "Earth Response" id scaled according to the reference and **all the noise is at the same level**.

### Hybrid Sercel Unite/428 version :

$$
D_c(\nu) = \frac{2.D_u(\nu).\bar{S(\nu)}}{N.\sum{S_n^2}}
$$

Here the obtained "Earth Response" is scaled on the amplitude part of the reference but not on its length. The sweep length has no impact on the output gain.
 
	