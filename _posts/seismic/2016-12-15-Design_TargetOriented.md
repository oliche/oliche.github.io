---
layout: page
breadcrumb: true
title:  "Fresnel Zone, Migration Aperture and Survey Apron"
subheadline:  "Survey Design"
teaser: "Target Oriented Survey Design."
categories:
    - seismic_design
tags:
    - design
image:
   thumb: "thumb_nodding_donkey.png"
header:
    image_fullwidth: "seismic_acquisition_header.png"
---


One-sided maximum displacement of a sample as a function of $$V_{rms}$$, 2-way time and dip $$\alpha$$.
This is considered as the migration apron.

$$
x = \frac{2.V_{rms}.t.\sin{(\alpha)}}{4}
$$


The Fresnel zone is frequency dependent. It is not strictly defined, often described as the area of constructive reflection accumulation surrounding the ray theory reflection point. Intuitively, this is the width of the useful part of a seismic diffraction in the migration process.

The purpose of the migration is to collapse this zone into a much smaller one, whose size is the seismic resolution assuming a perfect migration.
The Fresnel zone size, assuming we want to sample three times per wavelength :

$$
F_z(\lambda,z) = 3 * \sqrt{\bigg(z+\frac{\lambda}{4}\bigg)^2 - z^2 }
$$

$$
F_z(V_{rms},f,z) = 3 * \sqrt{\bigg(z+\frac{V_{rms}}{4f}\bigg)^2 - z^2 }
$$


The theoretical limit for spatial resolution is the size of the collapsed Fresnel zone after a perfect migration, one quarter wavelength

$$
F_{mig} = \frac{\lambda}{4}
$$


### References / Further Reading
Kun Liu and John C. Bancroft. The effects of diplimited kirchhoff migration and f-k migration., 2002. CREWES Research Report - Volume 14.

J. P. Lindsey. The fresnel zone and its interpetive significance. The Leading Edge, 8(10) :33–39, 1989. doi : 10.1190/1.1439575. [URL](http://dx.doi.org/10.1190/1.1439575)
