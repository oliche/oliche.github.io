---
layout: page
breadcrumb: true
title: "Zoeppritz equations primer"
subheadline: "Quantitative Interpretation"
teaser: "AVA basics"
categories:
    - seismic_reservoir
tags:
    - differential calculus
image:
   thumb: "thumb_reservoir.jpg"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---

## Acoustic Impedance

Acoustic impedance can be seen as a measure of the opposition a medium offers to an acoustic pressure applied.
This is the basic equation relating reflectivity $$R_{P0}$$, to acoustic impedance $$Z_{P}$$ for the $$i^{th}$$ interface in a layered Earth.

$$
R_{P0i} = \frac{\rho_{i+1}V_{Pi+1}-\rho_iV_{Pi}}{\rho_{i+1}V_{Pi+1}+\rho_iV_{Pi}}= \frac{Z_{Pi+1} - Z_{Pi}}{Z_{Pi+1} + Z_{Pi}}
$$

Where :
-	$$Z_{Pi} = \rho_{i}V_{Pi}$$, is the 1D acoustic impedance ($$Pa.m^{-1}$$)
-	$$\rho_{i}$$ is the density ($$kg.m^{-3}$$)
-	$$V_{Pi}$$ is the P-wave velocity ($$m.s^{-2}$$)


![Reflection at an interface](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Reflection_at_an_interface.png/605px-Reflection_at_an_interface.png)

Reflection at an interface.
By Nwhit (Own work) [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0), via Wikimedia Commons.
{: style="color:gray; font-size: 80%; text-align: center;"}


## AVA

### Converting from offset to angle

The straight ray assumption :

$$
\theta=\arctan{\left(\frac{offset}{2\times depth}\right)}=\arctan{\left(\frac{offset}{t_{pick} \times V_{rms}}\right)}
$$

Using the ray parameter with Yilmaz:

$$
\theta=\arctan{\left(\frac{offset\times V_{int}}{t_{pick}\times V_{rms}^2}\right)}
$$


### Full Zoeppritz Equations

Zoeppritz (1881-1908) derived a set of equations that describe the partitioning of seismic wave energy at an interface. They relate the amplitude of an incident P-wave to the resulting reflected and refracted P and S-waves. They are the basis of AVO (amplitude versus offset) and AVA (amplitude versus angle), wich consists in analysing the amplitude of returning waves when the incident angle is altered.

This is the full formulation of Zoeppritz equations :

$$
\begin{pmatrix}
-\sin{\theta_1}&-\cos{\phi_1}&-\sin{\theta_2}&\cos{\phi_2}\\\
\cos{\theta_1}&-\sin{\phi_1}&\cos{\theta_2}&-\sin{\phi_2}\\\
\sin{2\theta_1}&\frac{V_{P1}}{V_{S1}}\cos{2\phi_1}&\frac{\rho_2V_{S2}^2V_{P1}}{\rho_1V_{S1}^2V_{P1}}\cos{2\phi_1}&\frac{\rho_2V_{S2}V_{P1}}{\rho_1V_{S1}^2}\cos{2\phi_2}\\\
-\cos{2\phi_1}&\frac{V_{S1}}{V_{P1}}\sin{2\phi_1}&\frac{\rho_2V_{P2}}{\rho_1V_{P1}}\cos{2\phi_2}&-\frac{\rho_2V_{S2}}{\rho_1V_{P1}}\sin{2\phi_2}\\\
\end{pmatrix}
.
\begin{pmatrix}
R_P(\theta_1)\\\
R_S(\theta_1)\\\
T_P(\theta_1)\\\
T_S(\theta_1)\\\
\end{pmatrix}
=
$$

$$
\begin{pmatrix}
\sin{\theta_1}\\\
\cos{\theta_1}\\\
\sin{2\theta_1}\\\
\cos{2\phi_1}\\\
\end{pmatrix}
$$

### Linearisation of the Zoeppritz Equations

#### Linearisation of the Zoeppritz Equations : Wiggins/ Suey and Fatti Intercept and Gradient formulation
Sometimes considered as "the" AVO equation (cf. Shuey 1985 <sup id="a1">[1](#f1)</sup>.)

$$
R_{PP}(\theta)= R_{P0} +G\sin^2{\theta} + C\tan^2{\theta} \sin^2{\theta}
$$

$$
R_{P0} = \frac{\Delta V_p}{2V_p}+\frac{\Delta \rho}{2\rho}
$$

$$
G = \frac{\Delta V_p}{2V_p} + \frac{V_s^2}{V_p^2}  \bigg( -8 \frac{\Delta V_s}{2V_s} - 4 \frac{\Delta \rho}{2\rho}\bigg)
$$

$$
C = \frac{\Delta V_p}{2V_p}
$$

$$R_0$$ is referred as the intercept, $$G$$ as the gradient and $$F$$ as the third-term.
$$V_p$$, $$V_s$$ and $$\rho$$ are the average P-wave velocity, S-wave velocity and density for the two layers.
$$\Delta V_p$$, $$\Delta V_s$$ and $$\Delta\rho$$ are the difference of P-wave velocities, S-wave velocities and densities for the two layers.



#### Linearisation of the Zoeppritz Equations : Fatti and Smith
Another form of the AVO equation was formulated by Fatti and Smith <sup id="a2">[2](#f2)</sup> . Practical for pre-stack inversion.

$$
R_{pp}(\theta)=aR_{P0} + bR_{S0} + c'R_D
$$

$$
a=1+\tan^2{\theta}, b=-8\frac{V_s^2}{V_p^2}\sin^2{\theta}, c'=4\frac{V_s^2}{V_p^2}\sin^2{\theta}-\tan^2{\theta}
$$

$$
R_{P0}=\frac{1}{2}\left(\frac{\Delta V_p}{V_p}+\frac{\Delta\rho}{\rho}\right)
$$

$$
R_{S0}=\frac{1}{2}\left(\frac{\Delta V_s}{V_s}+\frac{\Delta\rho}{\rho}\right)
$$

$$
R_{D}=\frac{1}{2}\frac{\Delta V_p}{V_p}
$$

In practice, the amplitudes are extracted from an horizon and the parameters from a linearised equation are estimated using a regression.

## AVAz

### Linearisation of the Zoeppritz Equations in HTI medium : Ruger's equation

Ruger <sup id="a3">[3,](#f3)</sup><sup id="a3">[4](#f3)</sup> linearized the Zoeppritz equation for an HTI half-space under an isotropic half-space.

$$
R(\theta,\phi) = R_{P0} + ( G_{iso} + G_{ani}\cos^2 \phi) \sin^2 \theta + ( C_{iso} + C_{ani}) \sin^2\theta  \tan^2 \theta 
$$

$$
G_{ani} = \frac{1}{2} \bigg[\Delta \delta^{(V)} - 8 \Big(\frac{V_s}{V_p}\Big)^2 \Delta \gamma^{(V)} \bigg]
$$

$$
C_{ani} = \frac{1}{2} \bigg[\Delta \delta^{(V)} \sin^2 \phi + \Delta \epsilon ^{(V)} \cos^ 2 \phi\bigg] \cos^2 \phi
$$

$$R_{P0}$$, $$G$$, $$C$$, are the isotropic terms from Shuey and Fatti, $$\epsilon^{(V)}$$, $$\delta^{(V)}$$, $$\gamma^{(V)}$$ are the Thomsen parameters defined with respect to vertical, $$\theta$$ is the incidence angle, and $$\phi$$ the azimuth angle.


### References and Further Reading
<b id="f1">1: Shuey(1985)</b>  [↩](#a1)
R. T. Shuey. A simplification of the zoeppritz equations. GEOPHYSICS, 50(4) :609–614, 1985. doi : 10.1190/1.1441936. [URL](http://dx.doi.org/10.1190/1.1441936)

<b id="f2">2: Fatti et al.(1994)</b>  [↩](#a2)
Jan L. Fatti,George C. Smith, Peter J. Vail, Peter J. Strauss, and Philip R. Levitt. Detection of gas in sandstone reservoirs using avo analysis : A 3-d seismic case history using the geostack technique. GEOPHYSICS, 59(9) :1362–1376, 1994. doi : 10.1190/1.1443695. [URL](http://dx.doi.org/10.1190/1.1443695)

<b id="f3">3: Rüger 1997</b>  [↩](#a3)
Andreas Rüger. Pwave reflection coefficients for transversely isotropic models with vertical and horizontal axis of symmetry. GEOPHYSICS, 62(3) :713–722, 1997. doi : 10.1190/1.1444181. [URL](http://dx.doi.org/10.1190/1.1444181)

<b id="f4">4: Rüger 1998</b>  [↩](#a4)
Andreas Rüger. Variation of p-wave reflectivity with offset and azimuth in anisotropic media. GEOPHYSICS, 63(3) :935–947, 1998. doi :10.1190/1.1444405. [URL](http://dx.doi.org/10.1190/1.1444405)
