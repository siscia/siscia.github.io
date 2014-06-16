---
layout: post
title: "Extend postgres to json fields"
description: ""
category: 
tags: [clojure, postgres, postgressql, json]
---

For a little side project I need a very easy, "slow" and simple database to contain very few NoSql data.

Even MongoDB was overkilling, so I thought about use a tiny instance of PostgresSQL and use the type "json".

Unfortunatley jdbc does not support (as far as I know) the JSON type, nor for Postgres, so I started google around and two awesome guys did exactly what I needed to do.

Firt Andrey Antukh ["niwibi"](http://www.niwi.be/about.html) in [this](http://www.niwi.be/2014/04/13/postgresql-json-field-with-clojure-and-jdbc/
) blog post and then [Travis Vachon](https://twitter.com/tvachon/) in [this](http://hiim.tv/clojure/2014/05/15/clojure-postgres-json/) other blog post.

However any of them wrote a library to reuse such code, so here is born [postgres-type](https://github.com/siscia/postgres-type).

It is just very few lines of code, but it is been thought to be extended, could be interesting, for example, support also hstore.

;; Simone

{% include JB/setup %}
