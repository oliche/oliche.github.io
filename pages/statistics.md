---
layout: page
show_meta: false
title: "Statistics and Signal Processing"
subheadline: "Cheat sheets"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
permalink: "/statistics/"
---

## Statistics
<ul>
    {% for post in site.categories.stats %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Signal Processing
<ul>
    {% for post in site.categories.sigproc %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Linear Algebra and Calculus
<ul>
    {% for post in site.categories.maths %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
