---
layout: page
show_meta: false
title: "Code Libraries"
breadcrumb: true
header:
    image_fullwidth: "Banner_Wave.jpg"
    caption: Get Me out of here !
    caption_url: "/"
permalink: "/code_libraries/"
---

So far I have only linked a [bitbucket](https://bitbucket.org/oliche/) account below with 2 repositories.
One for elastic wave modeling, another for neural networks.

<div class="flex-video widescreen vimeo" style="display: block;">
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/U0hT9vO_oHA" frameborder="0" allowfullscreen></iframe>
</div>

Both are mainly for educational purposes or small-scale applications: they are efficient considering this is Matlab, but will not allow scaling on huge datasets where we would rather work outside of the RAM.

Codes are **fully vectorized** to harness the speed of low level Matlab libraries: the modeling is done in time-domain by spatial convolution of a derivative operator. For the neural networks, the forward and backward propagations are entirely written without loops as matrix multiplications.

The two libraries are **object-oriented** and implement **unit-testing**. This is obvious for a developper, but not so obvious for a geophysicist.

{% comment %}
*  This loops through the paginated posts
*
*  Total posts: {{ paginator.total_posts }}
*  Total paginate-pages: {{ paginator.total_pages }}
*
{% endcomment %}



<div class="row">
  <div class="medium-8 columns t30">
    



    {% for post in site.categories.code_libraries %}
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
      {% for post in site.categories.code_libraries limit:1000 %}
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



