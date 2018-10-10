---
layout: page
breadcrumb: true
title:  "Elasticity"
subheadline: "Rock Physics"
teaser: "Basics of Elasticity for the Geophysicist in a Hurry."
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


## Hooke's law

Strain $$\varepsilon$$ (dimensionless :  $$\varepsilon = \frac{\partial u}{u} $$, where $$u$$ is a distance).
Stress $$\sigma$$ ($$Pa$$, equivalent to $$N.m^{-2}$$) 
Modulus of elasticity or Young's Modulus $$E$$ ($$Pa$$, equivalent to $$N.m^{-2}$$) 

$$
\sigma = E.\varepsilon
$$

## Tensors

$$
\sigma_{xy} = 
\begin{pmatrix}
\sigma_{11}&\sigma_{12}&\sigma_{13}& \\\
\sigma_{21}&\sigma_{22}&\sigma_{33}& \\\
\sigma_{31}&\sigma_{32}&\sigma_{33}& \\\
\end{pmatrix}
,
\varepsilon_{xy} = 
\begin{pmatrix}
\varepsilon_{11}&\varepsilon_{12}&\varepsilon_{13}& \\\
\varepsilon_{21}&\varepsilon_{22}&\varepsilon_{33}& \\\
\varepsilon_{31}&\varepsilon_{32}&\varepsilon_{33}& \\\
\end{pmatrix}
$$


Symmetry implies $$\sigma_{ij}=\sigma_{ji}$$ and $$\varepsilon_{ij}=\varepsilon_{ji}$$ which leaves 6 unique terms in both tensors.

![Cauchy Stress Tensor](https://upload.wikimedia.org/wikipedia/commons/b/b3/Components_stress_tensor_cartesian.svg)

Cauchy Stress Tensor.
By Sanpaz (Own work) [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0) or [GFDL](http://www.gnu.org/copyleft/fdl.html)], via Wikimedia Commons


## Elastic material constants
#### Young's Modulus , ($$Pa \Leftrightarrow N.m^{-2} \Leftrightarrow kg.m^{-1}.s^{-2}$$).

$$
E =  \frac{\sigma_{11}}{\varepsilon_{11}}
$$

As a function of seismic velocities and density:
$$
E = \rho \frac{V_s^2(3V_p^2-4V_s^2)}{V_p^2 - V_s^2}
$$
As a fonction of P and S Impedances:
$$
E\rho =  \frac{I_s^2(3I_p^2-4I_s^2)}{I_p^2 - I_s^2}
$$


#### Poisson's Ratio (dimensionless : ratio of strains).

$$
\nu =  \frac{\varepsilon_{33}}{\varepsilon_{11}} 
$$

As a function of seismic velocities and impedances
$$
\nu =  \frac{1}{2} \frac{\frac{V_p^2}{V_s^2} - 2 }  {\frac{V_p^2}{V_s^2} - 1 } = \frac{1}{2} \frac{\frac{I_p^2}{I_s^2} - 2 }  {\frac{I_p^2}{I_s^2} - 1 }
$$


#### Shear Modulus $$\mu$$ , ($$Pa \Leftrightarrow N.m^{-2} \Leftrightarrow kg.m^{-1}.s^{-2}$$).

$$
\mu =  \frac{1}{2} . \frac{\sigma_{13}}{\varepsilon_{13}}
$$

#### Bulk Modulus $$K$$ , ($$Pa \Leftrightarrow N.m^{-2} \Leftrightarrow kg.m^{-1}.s^{-2}$$).

$$
K =  \frac{\sigma_{00}}{\varepsilon_{00}} = \frac{\sigma_{11}+\sigma_{22}+\sigma_{33}}{\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}}
$$



## Seismic velocities as a function of Lame parameters
#### P-Wave velocity ($$m.s^{-1}$$)

$$
V_{p}=\sqrt{\frac{K+\frac{4}{3}\mu}{\rho}} = \sqrt{\frac{\lambda+2\mu}{\rho}}
$$

#### S-Wave velocity ($$m.s^{-1}$$)

$$
V_{s}=\sqrt{\frac{\mu}{\rho}}
$$

#### Lame parameters ($$Pa \Leftrightarrow N.m^{-2} \Leftrightarrow kg.m^{-1}.s^{-2}$$): 

$$
\mu = V_s^2 \rho
$$

$$
\lambda = \rho (V_p^2 - 2V_s^2)
$$


## Stiffness pmatrix - Voigt notation
In the anisotropic case, the relation between stress and strain is a 6 by 6 tensor.

$$
\begin{pmatrix}
\sigma_{1}\\\
\sigma_{2}\\\
\sigma_{3}\\\
\sigma_{4}\\\
\sigma_{5}\\\
\sigma_{6}\\\
\end{pmatrix}
=
\begin{pmatrix}
c_{11}&c_{12}&c_{13}&c_{14}&c_{15}&c_{16}\\\
c_{21}&c_{22}&c_{23}&c_{24}&c_{25}&c_{26}\\\
c_{31}&c_{32}&c_{33}&c_{34}&c_{35}&c_{36}\\\
c_{41}&c_{42}&c_{43}&c_{44}&c_{45}&c_{46}\\\
c_{51}&c_{52}&c_{53}&c_{54}&c_{55}&c_{56}\\\
c_{61}&c_{62}&c_{63}&c_{64}&c_{65}&c_{66}\\\
\end{pmatrix}
.
\begin{pmatrix}
\varepsilon_{1}\\\
\varepsilon_{2}\\\
\varepsilon_{3}\\\
\varepsilon_{4}\\\
\varepsilon_{5}\\\
\varepsilon_{6}\\\
\end{pmatrix}
$$

where

$$
\begin{pmatrix}
\sigma_{1}\\\
\sigma_{2}\\\
\sigma_{3}\\\
\sigma_{4}\\\
\sigma_{5}\\\
\sigma_{6}\\\
\end{pmatrix}
=
\begin{pmatrix}
\sigma_{11}\\\
\sigma_{22}\\\
\sigma_{33}\\\
\sigma_{23}\\\
\sigma_{13}\\\
\sigma_{12}\\\
\end{pmatrix}
, and, 
\begin{pmatrix}
\varepsilon_{1}\\\
\varepsilon_{2}\\\
\varepsilon_{3}\\\
\varepsilon_{4}\\\
\varepsilon_{5}\\\
\varepsilon_{6}\\\
\end{pmatrix}
=
\begin{pmatrix}
\varepsilon_{11}\\\
\varepsilon_{22}\\\
\varepsilon_{33}\\\
\varepsilon_{23}\\\
\varepsilon_{13}\\\
\varepsilon_{12}\\\
\end{pmatrix}
$$



## Stiffness matrix - Isotropic Material
In the isotropic case, the relation between stress and strain depends only on 2 parameters : $$c_{11}$$ and $$c_{44}$$.
The isotropic solid has no preferred direction regarding elastic properties.

$$
C=
\begin{pmatrix}
c_{11}&c_{11}-2c_{44}&c_{11}-2c_{44}&0&0&0\\\
c_{11}-2c_{44}&c_{11}&c_{11}-2c_{44}&0&0&0\\\
c_{11}-2c_{44}&c_{11}-2c_{44}&c_{11}&0&0&0\\\
0&0&0&c_{44}&0&0\\\
0&0&0&0&c_{44}&0\\\
0&0&0&0&0&c_{44}\\\
\end{pmatrix}
$$

$$
C=
\begin{pmatrix}
\lambda + 2\mu & \lambda & \lambda&0&0&0\\\
\lambda & \lambda + 2\mu  & \lambda&0&0&0\\\
\lambda & \lambda & \lambda + 2\mu  &0&0&0\\\
0&0&0&\mu&0&0\\\
0&0&0&0&\mu&0\\\
0&0&0&0&0&\mu\\\
\end{pmatrix}
$$


## Stiffness matrix - VTI Material
Material with a vertical axis of symmetry (layer cake), 5 parameters in the stiffness matrix.

$$
C=
\begin{pmatrix}
c_{11}&c_{11}-2c_{66}&c_{13}&0&0&0\\\
c_{11}-2c_{66}&c_{11}&c_{13}&0&0&0\\\
c_{13}&c_{13}&c_{33}&0&0&0\\\
0&0&0&c_{44}&0&0\\\
0&0&0&0&c_{44}&0\\\
0&0&0&0&0&c_{66}\\\
\end{pmatrix}
$$

$$
V_{PH} = \sqrt{\frac{c_{11}}{\rho}},\quad
V_{PV} = \sqrt{\frac{c_{33}}{\rho}},\quad
V_{SH} = \sqrt{\frac{c_{44}}{\rho}},\quad
V_{SV} = \sqrt{\frac{c_{66}}{\rho}};
$$



## Stiffness matrix - HTI Material
Material with an horizontal axis of symmetry, this is the transposed of the VTI case, 5 parameters.

$$
C=
\begin{pmatrix}
c_{11}&c_{13}&c_{13}&0&0&0\\\
c_{13}&c_{33}&c_{33}-2c_{44}&0&0&0\\\
c_{13}&c_{33}-2c_{44}&c_{33}&0&0&0\\\
0&0&0&c_{44}&0&0\\\
0&0&0&0&c_{55}&0\\\
0&0&0&0&0&c_{55}\\\
\end{pmatrix}
$$

$$
V_{PH} = \sqrt{\frac{c_{11}}{\rho}},\quad
V_{PV} = \sqrt{\frac{c_{33}}{\rho}},\quad
V_{SH} = \sqrt{\frac{c_{44}}{\rho}},\quad
V_{SV} = \sqrt{\frac{c_{55}}{\rho}};
$$

## Stiffness matrix - Orthorhombic Material
Material with three mutually orthogonal axis of symmetry : 9 parameters in the stiffness matrix.

$$
C=
\begin{pmatrix}
c_{11}&c_{12}&c_{13}&0&0&0\\\
c_{12}&c_{22}&c_{23}&0&0&0\\\
c_{13}&c_{23}&c_{33}&0&0&0\\\
0&0&0&c_{44}&0&0\\\
0&0&0&0&c_{55}&0\\\
0&0&0&0&0&c_{66}\\\
\end{pmatrix}
$$

$$
\begin{aligned}
V_{PH1} = \sqrt{\frac{c_{11}}{\rho}},\quad
V_{PH2} = \sqrt{\frac{c_{22}}{\rho}},\quad
V_{PV}  = \sqrt{\frac{c_{33}}{\rho}};
\end{aligned}
$$

$$
\begin{aligned}
V_{SH1} = \sqrt{\frac{c_{44}}{\rho}},\quad
V_{SH2} = \sqrt{\frac{c_{55}}{\rho}},\quad
V_{SV} = \sqrt{\frac{c_{66}}{\rho}};
\end{aligned}
$$




