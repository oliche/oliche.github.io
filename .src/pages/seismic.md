---
layout: page
show_meta: false
title: "Seismic Lab Notes"
subheadline: "Cheat sheets"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
permalink: "/seismic/"
---

## Acquisition
<ul>
    {% for post in site.categories.seismic_acquisition %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Survey Design
<ul>
    {% for post in site.categories.seismic_design %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Maths
<ul>
    {% for post in site.categories.seismic_maths %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Processing
<ul>
    {% for post in site.categories.seismic_processing %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>

## Reservoir
<ul>
    {% for post in site.categories.seismic_reservoir %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>