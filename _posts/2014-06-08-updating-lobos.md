---
layout: post
title: "Updating Lobos"
description: ""
category: 
tags: [clojure, lobos, open source]
---

I needed to work with Lobos and Korma together.

Unfortunately the last version of Korma use the jdbc version 3 while Lobos use the jdbc version 2.

The architecture of Lobos is not so obvious, so "porting" (I didn't do much work honestly) it to use jdbc 3 is being a little hummm... "weird".

Anyway here is the github repo:

[https://github.com/siscia/lobos](https://github.com/siscia/lobos)

So everybody can use Lobos together with Korma.

Edit, the path is now being merged in Lobos.

{% include JB/setup %}
