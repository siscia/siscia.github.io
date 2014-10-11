---
layout: post
title: "transducer explained"
description: ""
category: 
tags: []
---
{% include JB/setup %}


# A minuscule guide about transducers

What follow is a very small walkthrought of transducers for my brothers who asked for, I have never used transducers in any project so this is just my understanding from the official documentation plus some test.

If you see any error or mistake please let me know.

Transducers are not complex or difficult, you just need to visualize the flow of data.

Suppose we have a small sequence.

{% highlight clojure %}
(def s [1 2 3 4])
{% endhighlight %}

Now we want to increment of one the value of any element in the sequence and then remove the element that are odd.

The standard approach would look similar to this:

{% highlight clojure %}
(remove odd? (map inc s))
{% endhighlight %}

What is happening here ?

First every element in s is incremented.

{% highlight clojure %}
=>(inc 5)
6
=>(map inc s)
;;(2 3 4 5)
{% endhighlight %}

Then the element incremented are passed through a remove which remove every element that return `true` to the predicate `odd?`

{% highlight clojure %}
=>(odd? 3)
;;true
=>(odd? 4)
;;false
=>(remove odd? '(2 3 4 5))
;;(2 4)
{% endhighlight %}

For sake of simplicity let's call stuff like `(map inc s)` or `(remove odd? s)` with a simple name `transformation`.

Also let's call `flow` a composition of transformation.

Now let's write the code above in a more clojurist way:

{% highlight clojure %}
=>(->> s (map inc)
	     (remove odd?))
;;(2 4)
{% endhighlight %}

Now it is important to don't get confused, `->>` is a macro, not a function.

The two codes above are exactly the same.

{% highlight clojure %}
=>(macroexpand '(->> s (map inc) (remove odd?)))
;;(remove odd? (map inc s))
{% endhighlight %}

However the macro expression is pretty useful to visualize what is happening.

The sequence `s` flow inside the transformation `(map inc)` the result, then, flow inside the transformation `(remove odd?)` and we get our output.

transducers are a way to create `flow` combining different `transformation`.

Without transducers you have to pass an input, a sequence, to our transformation, with transducer we don't have this necessity anymore.

Also, function like `map`, `remove`, `filter` create a lazy sequence each.

{% highlight clojure %}
(->> s (map inc) (remove even?) (map str))
{% endhighlight %}

A flow like the one above will create 3 lazy sequence.

However if we use transducer

{% highlight clojure %}
(def inc-even-str (comp (map inc)
                        (remove even?)
                        (map str)))
#'user/inc-even-str
(sequence inc-even-str [2 3 4 5])
;; ("3" "5")						
{% endhighlight %}

we don't create the intermediate lazy sequences.

Also I can see transducer usefully if we have a lot of different `flow` that need to be composed.

{% highlight clojure %}
(def add-metadata (comp ...))
(def sanitize-data (comp ...))
(def prepare-database-write (comp ...))
(def store-data (comp ...))
(def analyze-sales-data (comp ...))

(sequence (comp add-metadata
                analyze-sales-data
                prepare-database-write
                store-data) get-sales-data)

(sequence (comp add-metadata
                sanitize-data
                store-data) datas-from-mobile-app)
{% endhighlight %}

If you have any question just let me know :)
