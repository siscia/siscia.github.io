---
layout: post
title: "Base conversion in plain clojure"
description: ""
category: programming
tags: [clojure, base conversion, number, change of base, change, base, int, integer]
excerpt: "Conversion of number between different bases using plain clojure."
---
{% include JB/setup %}

Whoever write some computer code must know that number can be represented in different bases, one of those bases is base 10, another one is base 2 (binary) and other important bases are base 8 (octal) and base 16 (hexadecimal).

Whoever write computer code should be able to convert from a base to another one, this is such a common task that in high-level language is given for granted.

Clojure itself make so easy to bring number in base 10 from every base that no one think any more about this trivial task.

{% highlight clojure %}
(int 16rCACCA)
;; => 830666
{% endhighlight %}

However change of base is a must know skill and I catch myself not sure enough about the implementation of such algorithm.

So I have re-implemented 2 simple function that convert from base 10 to base n and from base n to base 10.

I am sure that everybody know the theory behind such function, and I am also sure that none will have difficulties to implement such algorithm with a quick google search.

But are you sure you can implement it right now ?
Not goggling allow, only clojure (or whatever language) and a piece of paper.

What need to be implemented are 2 functions, that behave like so:

{% highlight clojure %}
(base-10-to-base-n 3452 17)
;; => "BG1"
(base-n-to-base-10 "BG1" 17)
;; => 3452
;;;; and just to be sure
(int 17rBG1)
;; => 3452
{% endhighlight %}

`base-10-to-base-n` convert the first integer in a number using like base the second argument.

`base-n-to-base-10` is the other way around.

My simple solutions is here:

[Base conversion in Clojure](https://gist.github.com/siscia/5939462)

Please feel free to comment with your own solution.

Now another question raise:

how to convert a number from base n to base m, without pass to base 10 ?

I wasn't able to answer, even using google, if you have a solution feel free to share.

------------------

I have bothered you with this little challenge just because I have too much free time, if you need some clojure/python freelancer *I am for hire*, feel free to drop me an [email](mailto:{{ site.author.email }}) or tweet me @siscia_.

------------------