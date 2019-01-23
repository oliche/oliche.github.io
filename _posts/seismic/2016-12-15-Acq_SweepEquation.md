---
layout: page
title:  "Generalized Sweep Equation"
subheadline:  "Acquisition"
breadcrumb: true
teaser: "Framework for advanced sweep design."
categories:
    - seismic_acquisition
tags:
    - acquisition
    - vibroseis
image:
   thumb: "thumb_acquisition.png"
header:
    image_fullwidth: "seismic_acquisition_header.png"
---

The sweep equation in its simplest form is written :

$$
S(t) = A_0(t)sin(\varphi(t))
$$

Where $$A_0(t)$$ is the envelope and $$\varphi$$ the instantaneous phase, both as a function of time.
This is the expression used in traditional vibrator electronics.


The instantaneous frequency is the time derivative of the instantaneous phase :

$$
f(t) = \frac{1}{2\pi}\frac{d\varphi}{dt}
$$

The full sweep equation has the instantaneous sweep frequency computed by integrating the time-domain sweep rate $$S_r$$ :

$$
f(t) = f_{min} + \int_0^TS_r(t)dt
$$

Which is then integrated again over the sweep length to get the instantaneous phase :

$$
\varphi(t) = \varphi_0 + 2\pi\int_0^Tf(t)dt 
$$

The complete sweep equation becomes: 

$$
 S(t)=\cos\Bigg[\varphi_0 + 2\pi\int_0^T \bigg(f_{min} + \int_0^TS_r(t)dt \bigg) dt \Bigg]
$$



### References / Further Reading
Julien Meunier and Thomas Bianchi. How long should the sweep be ?, pages 1–5. 2012. doi : 10.1190/segam2012-0182.1.
[URL](http://library.seg.org/doi/abs/10.1190/segam2012-0182.1)