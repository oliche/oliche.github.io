---
layout: page
breadcrumb: true
title:  "Rosaces and multiplication tables"
subheadline:  "The beauty of maths"
teaser: "When multiplication tables morph into beautiful rosaces"
categories:
    - culture
tags:
image:
   thumb: "thumb_culture_visual_multiplication.png"
header:
    image_fullwidth: "Banner_Archive.png"
---

![Illustration]({{ site.urlimg }}post_culture_rosace.png)

It turns out that representing multiplication tables on a circle can be quite beautiful !
The idea is to represent multiplication tables on a clock, where the origin is the multiplied number, and the destination the result modulo the table multiplier.


And when we sweep a range of multipliers and put all displays together in an amimated picture, the result is hypnotizing.

<div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/FccXPv1TKzo" frameborder="0" allowfullscreen></iframe>
</div>

[This Youtube video](https://www.youtube.com/watch?v=-X49VQgi86E) explains in much greater detail and fun the idea. 


The implementation of this in Matlab is a great example of how to deal with a higher level language for fast graphics. The rosace code itself fits in 2 lines using complex numbers.

```matlab
x = 78;
y = 854;
% Table of x modulo y, the trick is to represent it using the circle
% equation for complex numbers
in = [1:(y-1)].';
cir = @(x) exp(-1i .* x .* 2 .* pi + 1i .* pi / 2);
% Update the display, this will be way to slow if each line is an object
% so this uses a single vector
toplot = ([cir(in / y) cir(mod(in * x , y) ./ y )  in.*NaN].');
toplot = toplot(:);
```

It is then possible to display hundreds of lines in real time using two Matlab optimization tricks:
-   create objects upfront and only update their properties at each iteration
-   create a single high level Matlab line object by putting all segments in a long vector with a NaN between each to break the line.

The full git repository, with an interactive could be found [here](https://github.com/oliche/visual_multiplication).