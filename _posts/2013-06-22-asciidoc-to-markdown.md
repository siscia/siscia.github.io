---
layout: post
title: "Asciidoc to Markdown"
description: "Translate asciidoc to markdown"
category: programming
tags: [clojure, programming, markdown, asciidoc, conversion]
excerpt: "Little tool to convert asciidoc documents from the clojure-cookbook project to markdown files to use in jekyll"
---
{% include JB/setup %}

I have some free time and so I am trying to contribute to the clojure-cookbook project.
(It's really interesting, you should check it out)

I wrote a couple of very stupid recipes and now I am waiting for the proof reading and correction, if you wanna help:

[Deploy on lein](https://github.com/siscia/clojure-cookbook/blob/lein/deployment/deploy-on-lein/deploy-on-lein.asciidoc)

[Database up and running](https://github.com/siscia/clojure-cookbook/blob/database-up-n-running/databases/database-up-n-running/database-up-n-running.asciidoc)


Meanwhile, I thought that you might be interested to those recipe.
They are very entry-level recipes so they may help just somebody who is very new to clojure, however if you know clojure just a little bit you might find those interesting and you may help me to review either my English or my clojure.

But there is a problem: the clojure-cookbook project use the .asciidoc (it is kinda like markdown but it looks more powerful, and it is a better fit to write real-paper book) while my blog run with jekyll that use the markdown format.
Jekyll is thinking about allow other file format, but it is not ready yet.

So I tried to figure out a solution by myself and I write a couple of lines of code.

The script convert basic asciidoc to basic markdown, nothing fancy at all but it takes care of the title, of the block of code and also of the in-line code, enough for my recipes.

It uses just with regex and it is really dummy, but it works.

You can check the code on [github](https://github.com/siscia/asciidoc-to-markdown/)

How you can see the code is not very interesting, it is mainly regex application.

One thing may, however, be interesting: how I manage to "translate" the titles.

In asciidoc titles have this syntax:

{% highlight text %}
= H1 TITLE 
== H2 TITLE
==== H4 TITLE
{% endhighlight %}

In markdown it is very similar, but instead of `=` you can use `#`.

So I just needed a regex to change that `=` in `#`, well I am not a regex expert and I haven't find out any smart way to do it but the one that you can see, I also store the regex in a map to link them each other.
 
{% highlight clojure %}
(def titles-regex
  (sorted-map-by #(> (count %1) (count %2))
                 "###### $1" #"====== +([^ \t\n\r\f\v].*?)"
                 "##### $1" #"===== +([^ \t\n\r\f\v].*?)"
                 "#### $1" #"==== +([^ \t\n\r\f\v].*?)"
                 "### $1" #"=== +([^ \t\n\r\f\v].*?)"
                 "## $1" #"== +([^ \t\n\r\f\v].*?)"
                 "# $1" #"= +([^ \t\n\r\f\v].*?)"))
{% endhighlight %}

The problem is that if you start to parse the file with the wrong order you will just substitute the last `=` of any asciidoc title with a `#` that will generate a bunch of wrong H1.

You definitely need to start looking for H6 and the for H5 and so on.

And here it comes the sorted map that helped to sort the regex from the longer to the shorter and to still have them linked each other.

Finally, just one last little note, on github it is possible to define block of code using a syntax like:

{% highlight text %}
``` language 
fancy code
```
{% endhighlight %}

This is not true here on jekyll (they are working on it, though) where you have to use a syntax like django.

My little script is been thought to let me publish here on jekyll, so it generate a slightly wrong syntax; you can fix that by passing the `--no-jekyll` parameter.

The whole code:

{% gist 5841486 %}

If you are interested you can just download everything from github and run it to convert basic asciidoc into markdown.

{% highlight text %}
    git clone git@github.com:siscia/asciidoc-to-markdown.git
    cd asciidoc-to-markdown
    lein run input-file.asciidoc output-file.md
{% endhighlight %}

{% include JB/setup %}