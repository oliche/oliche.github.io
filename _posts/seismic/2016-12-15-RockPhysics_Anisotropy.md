---
layout: page
breadcrumb: true
title:  "P-wave anisotropy : Thomsen & Tsvankin Parameters"
subheadline: "Rock Physics"
teaser: "A little primer on the connection between elasticity and seismic velocities."
categories:
    - seismic_reservoir
tags:
    - anisotropy
    - rock physics
    - elasticity
    - modeling
image:
   thumb: "thumb_reservoir.jpg"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---

The weak anisotropy developed by Thomsen for the VTI case was extended to the Orthorhombic case by Tsanvskin <sup id="a1">[1](#f1)</sup>.


![Geophone Response]({{ site.urlimg }}Velocities_Tsvanskin.png)
Thomsen Parameters in different symmetries.
{: style="color:gray; font-size: 80%; text-align: center;"}



## Velocities in VTI

Reference velocities and equivalences: (cf. Thomsen 1986 <sup id="a2">[2](#f2)</sup>.)

$$
V_{P0} = V_{PV} = \sqrt{\frac{c_{33}}{\rho}},\quad
V_{S0} = V_{SH1} = V_{SH2} = \sqrt{\frac{c_{55}}{\rho}},
$$

Velocity as a function of incidence angle $$\theta$$

$$
\begin{aligned}
V_P(\theta) = V_{P0}\bigg[1+\delta\sin^2 \theta \cos^2\theta + \epsilon \sin^4 \theta \bigg]\\
V_{SV}(\theta) = V_{S0}\bigg[ 1 +\frac{V_{P0}^ 2}{V_{S0}^2}(\epsilon - \delta) \sin^2 \theta \cos^2 \theta \bigg]\\
V_{SH}(\theta) = V_{S0}\bigg[ 1 + \gamma \sin^2\theta \bigg]\\
\end{aligned}
$$


## Velocities in HTI

Reference velocities and equivalences: (cf. Ruger 1997 <sup id="a3">[3](#f3)</sup>.)

$$
V_{P0} = V_{PV} = V_{PH2} = \sqrt{\frac{c_{33}}{\rho}},\quad
$$

Velocity as a function of incidence angle $$\theta$$

$$
\begin{aligned}
V_P(\theta,\phi) = V_{P0}\bigg[1+\delta^{(V)} \sin^2 \theta \cos^2 \phi + (\epsilon^{(V)} - \delta^{(V)}) \sin^4 \theta\cos^4 \phi \bigg]\\
\end{aligned}
$$


## Velocities in Orthorhombic Medium
Reference velocities and equivalences:  (cf. Ruger 1998 <sup id="a4">[4](#f4)</sup>.)

$$
V_{P0} = V_{PV} = \sqrt{\frac{c_{33}}{\rho}},\quad
$$

Velocity as a function of incidence angle $$\theta$$

$$
\begin{aligned}
V_P(\theta,\phi) =  V_{P0}\bigg[1+\delta(\psi)\sin^2 \theta \cos^2\theta + \epsilon(\phi) \sin^4 \theta \bigg]\\
\delta(\phi) = \delta^{(1)}\sin^2\phi + \delta^{(2)} \cos^2 \phi \\
\epsilon(\phi) = \epsilon^{(1)} \sin^4 \phi + \epsilon^{(2)} \cos^4 \phi + (2\epsilon^{(2)} + \delta^{(3)})\sin^2 \phi \cos^2 \phi
\end{aligned}
$$


### References and Further Reading

<b id="f1">1: Tsvankin 1997 </b> [↩](#a1)
Ilya Tsvankin. Anisotropic parameters and pwave velocity for orthorhombic media. GEOPHYSICS, 62(4) :1292–1309, 1997. doi :10.1190/1.1444231. [URL]( http://dx.doi.org/10.1190/1.1444231)

<b id="f2"> 2: Thomsen 1986</b> [↩](#a2)
Leon Thomsen. Weak elastic anisotropy. GEOPHYSICS, 51 (10) :1954–1966, 1986. doi : 10.1190/1.1442051. [URL](http://dx.doi.org/10.1190/1.1442051)

<b id="f3">3: Rüger 1997</b>  [↩](#a3)
Andreas Rüger. Pwave reflection coefficients for transversely isotropic models with vertical and horizontal axis of symmetry. GEOPHYSICS, 62(3) :713–722, 1997. doi : 10.1190/1.1444181. [URL](http://dx.doi.org/10.1190/1.1444181)

<b id="f4">4: Rüger 1998</b>  [↩](#a4)
Andreas Rüger. Variation of p-wave reflectivity with offset and azimuth in anisotropic media. GEOPHYSICS, 63(3) :935–947, 1998. doi :10.1190/1.1444405. [URL](http://dx.doi.org/10.1190/1.1444405)
