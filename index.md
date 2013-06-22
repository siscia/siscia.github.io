---
layout: page
title: About me
tagline: Supporting tagline

---

Programmer and, in my spare time, student.

I am born in Pesaro but I grew up is Siena.

Other that code, I enjoy to run and to travel.

I am available for contractor work and code review.

I work mainly in Clojure but I am fluent with python too and I have a good knowledge of C/C++, I can learn any language (OOP/FP) in matter of 1-2 weeks.

You can contact me at: simone (at) mweb (dot) biz

What I wrote in this blog for now:

{% for post in site.posts %}
   [{{post.title}}]({{post.url}})
   {{ post.excerpt }}
{% endfor %}
