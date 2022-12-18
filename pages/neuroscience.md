---
layout: page
show_meta: false
subheadline: "Software engineering in systems neuroscience"
title: "Neurophysiology"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
permalink: "/neuroscience/"
---

## Neuropixels
<ul>
    {% for post in site.categories.neuropixels %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
