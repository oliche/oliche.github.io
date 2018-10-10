---
layout: page
breadcrumb: true
title:  "Noises and Sensor Wiring"
subheadline:  "Acquisition"
teaser: "Pickup, ambient and recorder noise on a geophone array."
categories:
    - seismic_acquisition
tags:
    - acquisition
    - geophone
    - receiver 
    - ambient noise
image:
   thumb: "thumb_acquisition.png"
header:
    image_fullwidth: "seismic_acquisition_header.png"
---


Several kinds of noise affect the receiver.

Ambient noise contain surface-waves that can be attenuated using proper array distribution and non-coherent noise such as wind or traffic. Assuming the spatial distribution results in a sufficiently random sampling, the square-root estimation will apply. 
[link to variance propagation rule]

For inducted noise and instrument noise, the induction is proportional to the impedance, so the number of units in parallel $$N_p$$ will attenuate the noise picked-up. On another hand increasing the number of units in serie $$N_s$$ will increase the sensitivity, thus decreasing the relative instrument noise compared to the signal.



|        | Ambient                     | Pickup            | Recorder |
|--------|-----------------------------|-------------------|----------|
| Signal | $$N_sN_p / N_p$$        | $$N_s$$             | $$N_s$$    |
| Noise  | $$\sqrt{N_s.N_p} / N_p$$ | $$N_s/N_p$$ | constant |
| SNR    | $$\sqrt{N_s.N_p}$$             | $$N_p$$             | $$N_s$$    |

