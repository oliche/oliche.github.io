---
layout: page
breadcrumb: true
title:  "Solving the Wave-Equation using Finite-Differences"
subheadline: "Rock Physics"
teaser: "Seismic modeling"
categories:
    - seismic_processing
tags:
    - modeling
image:
   thumb: "thumb_processing.jpg"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
---

## Acoustic Wave equation

The acoustic wave equation for dimensions $$x,y,z$$ with a medium velocity $$c$$ :

$$
\frac{\partial^2p}{\partial t^2} = c^2\nabla^2p = c^2\bigg[\frac{\partial^2p}{\partial x^2}+\frac{\partial^2p}{\partial y^2}+\frac{\partial^2p}{\partial z^2}\bigg]
$$

A first-order in time and N-order in space explicit finite-difference scheme will be compute the Pressure wave-field $$P$$ at time $$t$$ recursively:

$$
P^{(t+1)} = 2\times P^{(t)} - P^{(t-1)} + \bigg(\frac{V}{dt\times dx}\bigg).\bigg(OP*P^{(t)}\bigg)
$$


Where $$*$$ denotes convolution and $$OP$$ is a spatial derivative operator.
The computation of the spatial operator coefficients is detailed in Fornberg.

## Elastic Wave equation
The elastic case involves the 6 components of stress $$S_{ij}$$ and the 3 components of displacement $$u_i$$ ;

$$
S_{xx} = (\lambda + 2\mu)\frac{\partial }{\partial_x} u_x+ \lambda \frac{\partial }{\partial_y} u_y + \lambda \frac{\partial }{\partial_z} u_z
$$

$$
S_{yy} = (\lambda + 2\mu)\frac{\partial }{\partial_y} u_y+ \lambda \frac{\partial }{\partial_x} u_x + \lambda \frac{\partial }{\partial_z} u_z
$$

$$
S_{zz} = (\lambda + 2\mu)\frac{\partial }{\partial_z} u_z+ \lambda \frac{\partial }{\partial_y} u_y + \lambda \frac{\partial }{\partial_x} u_x
$$

$$
S_{xy}=\mu \bigg[\frac{\partial }{\partial x} u_y + \frac{\partial }{\partial y} u_x \bigg]
$$

$$
S_{xz}=\mu \bigg[\frac{\partial }{\partial x} u_z + \frac{\partial }{\partial z} u_x \bigg]
$$

$$
S_{yz}=\mu \bigg[\frac{\partial }{\partial y} u_z + \frac{\partial }{\partial z} u_y \bigg]
$$

$$
\rho\frac{\partial^2 }{\partial t^2} u_x = \frac{\partial }{\partial x} S_{xx} +\frac{\partial }{\partial y} S_{xy} +\frac{\partial }{\partial z} S_{xz}
$$

$$
\rho\frac{\partial^2 }{\partial t^2} u_y = \frac{\partial }{\partial y} S_{yy} +\frac{\partial }{\partial x} S_{xy} +\frac{\partial }{\partial z} S_{yz}
$$

$$
\rho\frac{\partial^2 }{\partial t^2} u_z = \frac{\partial }{\partial z} S_{zz} +\frac{\partial }{\partial y} S_{yz} +\frac{\partial }{\partial x} S_{xz}
$$


### References and Further Reading
B. Fornberg. Generation of finite difference formulas on arbitrary spaced grids, 1988. Mathematics of Computation, Vol. 51, No. 184, pp. 699-706.

Jean Virieux. P-SV wave propagation in heterogeneous media: Velocity‐stress finite‐difference method. GEOPHYSICS 1986 51:4, 889-901.