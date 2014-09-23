---
layout: page
title: About me
tagline: 
---

I am a freelancer programmer, who is specialized in Clojure and Python.

I love to code MVP and webb app and I will find the way to get your idea ready as quick as possible. 

I work with clients of any size and budget.

For any inquiry you can contact me at: simone (at) mweb (dot) biz

What I wrote in this blog for now:

{% for post in site.posts %}
   [{{post.title}}]({{post.url}})
   {{ post.excerpt }}
{% endfor %}