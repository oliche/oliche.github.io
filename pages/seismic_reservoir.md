---
layout: page
show_meta: false
title: "Reservoir"
header:
    image_fullwidth: "banner_seismic_processing.jpg"
    caption: Get Me out of here !
    caption_url: "/"
permalink: "/seismic_reservoir/"
---

{% comment %}
*  This loops through the paginated posts
*
*  Total posts: {{ paginator.total_posts }}
*  Total paginate-pages: {{ paginator.total_pages }}
*
{% endcomment %}

<ul>
    {% for post in site.categories.seismic_reservoir %}
    <li><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
</ul>


<div class="row">
  <div class="medium-8 columns t30">


    {% for post in site.categories.seismic_reservoir %}
  <div class="row">
    <div class="row t100 homepage">
      <h2><a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
      <p>
        {% if post.image.thumb %}<a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ post.title escape_once }}"><img src="{{ site.urlimg }}{{ post.image.thumb }}" class="alignleft" width="150" height="150" alt="{{ page.title escape_once }}"></a>{% endif %}

        {% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}

        <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="{{ site.data.language.read }} {{ post.title escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a>
      </p>
    </div><!-- /.small-12.columns -->
  </div><!-- /.row -->
{% endfor %}

  </div><!-- /.medium-7.columns -->


  <div class="medium-4 columns t30">


        <dl class="accordion" data-accordion>
      {% assign counter = 1 %}
      {% for post in site.categories.seismic_reservoir limit:1000 %}
      <dd class="accordion-navigation">
      <a href="#panel{{ counter }}"><span class="iconfont"></span> <strong>{{ post.title }}</strong></a>
        <div id="panel{{ counter }}" class="content">
          {% if post.meta_description %}{{ post.meta_description | strip_html | escape }}{% elsif post.teaser %}{{ post.teaser | strip_html | escape }}{% endif %}
          <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}" title="Read {{ post.title | escape_once }}"><strong>{{ site.data.language.read_more }}</strong></a><br><br>
        </div>
      </dd>
      {% assign counter=counter | plus:1 %}
      {% endfor %}
    </dl>


  </div><!-- /.medium-5.columns -->
</div><!-- /.row -->



