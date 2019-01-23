---
layout: page
breadcrumb: true
title:  "PSD "
subheadline: "Signal Processing"
teaser: "Spectral Density, Parseval theorem and Root Mean Square,... in Proper Units..."
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


For an input in millivolts ($$mV$$) **Power Spectral Density** (PSD) is expressed in ($$mV^2.Hz^{-1}$$). The **Spectral density** is in ($$mV.(\sqrt{Hz})^{-1}$$).
The PSD is defined as follows for a finite time serie $$x_n$$ of length $$T$$ secs sampled at $$\Delta t$$ secs :

$$
PSD(f) = \frac{(\Delta t)^2}{T} \left|{\sum_{n=1}^{N}{x_ne^{-2i\pi n}}}\right|^2
$$

When dealing with PSD it is always helpful to keep in mind Parseval theorem :

$$
\int_{-\infty}^{\infty} \left| x(t) \right| ^2 dt =  \int_{-\infty}^{\infty} \left| X(f) \right| ^2 df
$$

It means that the sum of square of a signal is the same in time domain and in frequency domain. 

The Parseval theorem serves to prove that the RMS equals the square root of the PSD integration over the bandwidth (and is a good way to write a unit test...).

$$
 RMS=\sqrt{\frac{1}{N}\sum_1^N{x_n^2}}=\sqrt{\int_{f_1}^{f_2} PSD(f)  df}
$$

## Matlab example :

```matlab
    %% PSD
    Nech=2501; Si=0.001; % 2501 samples at 1ms
    W=rand(Nech,1); W=W-mean(W);
    df=1/Si/Nech;
    % Spectral density
    SD=decons(abs(fft(W)).*sqrt(2*Si/Nech));
    % Parseval verified
    sum( SD.^2 / Si) ./ sum(W.^2)
    % Rms is the root of integration of the PSD
    sqrt( sum(SD.^2).*df) ./ rms(W)
```


