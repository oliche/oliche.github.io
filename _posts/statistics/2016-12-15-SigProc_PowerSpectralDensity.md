---
layout: page
breadcrumb: true
title:  "PSD "
subheadline: "Signal Processing"
teaser: "Spectral Density, Parseval theorem and Root Mean Square,... in Proper Units..."
categories:
    - sigproc
tags:
    - phase
image:
   thumb: "thumb_processing.jpg"
header:
    image_fullwidth: "Banner_Wave.jpg"
---


For an input in millivolts $$mV$$ **Power Spectral Density** (PSD) is expressed in $$mV^2.Hz^{-1}$$. The **Spectral density** is in $$mV.(\sqrt{Hz})^{-1}$$.
The PSD is defined as follows for a finite time serie $$x_n$$ of length $$T$$ secs sampled at $$\Delta t$$ secs :

$$
PSD(f) = \frac{\Delta t}{T} \left|{\sum_{n=1}^{N}{x_ne^{-2i\pi n}}}\right|^2
$$

When dealing with PSD it is always helpful to keep in mind Parseval theorem :

$$
\int_{-\infty}^{\infty} \left| x(t) \right| ^2 dt =  \int_{-\infty}^{\infty} \left| X(f) \right| ^2 df
$$

It means that the sum of square of a signal is the same in time domain and in frequency domain. 

The Parseval theorem serves to prove that the RMS equals the square root of the PSD integration over the bandwidth.

$$
 RMS=\sqrt{\frac{1}{N}\sum_1^N{x_n^2}}=\sqrt{\int_{f_1}^{f_2} PSD(f)  df}
$$

## Matlab example :
[dsp.freduce dependency here](https://bitbucket.org/oliche/echo-matlab/src/master/)

```matlab
%% Parseval verified
ns = 2501; si = 0.001; % 2501 samples at 1ms
w = randn(ns, 1); w = w - mean(w);
df = 1 / si / ns;
% Spectral density
SD = dsp.freduce(abs(fft(w)) .* sqrt( 2 * si / ns));
% Parseval verified
sum( SD.^2 / si) ./ sum(w.^2)
% Rms is the root of integration of the PSD
sqrt( sum(SD.^2) .* df) ./ rms(w)
```

## Python example :

```python
import numpy as np
from scipy import fft
from scipy.signal import periodogram

ns = 2501  # number of sample
si = 0.001  # sampling interval (s)
w = np.random.rand(ns)
w = w - np.mean(w)
df = 1 / si / ns
# spectral density
sd = np.abs(fft.rfft(w)) * np.sqrt(2 * si / ns)
# Parseval verified
np.sum(sd ** 2 / si) / np.sum(w ** 2)
# rms is the root of integration of the PSD
np.sqrt(np.sum(sd ** 2) / si / ns) / np.sqrt(np.mean(w ** 2))
# make sure it matches the psd from scipy
f, sd_ = periodogram(w, 1 / si)
np.all(np.isclose(sd ** 2, sd_))
```

## Further Reading
[mathworks recipe](https://www.mathworks.com/help/signal/ug/power-spectral-density-estimates-using-fft.html)
 