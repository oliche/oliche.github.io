---
layout: page
show_meta: false
subheadline: "Because it's not all about code"
title: "Culture"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
permalink: "/arts/"
---

## Literature
<ul>
    {% for post in site.categories.arts %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>
