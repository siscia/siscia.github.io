---
layout: post
title: "Read Clojure Map Values 2/2"
description: ""
category: programming
tags: [clojure, maps, map, keys, vals, select-keys, read map]
---
{% include JB/setup %}


Here is another chapter of the series.

For those who missed the previous chapter:

*   [First general introduction about clojure maps]({% post_url 2014-09-12-clojures-maps-overview %})

*   [Create Maps Overview of: hash-map, array-map, zipmap, sorted-map and sorted-map-by]({% post_url 2014-09-15-create-clojure-map-advanced-methods-part-1 %})

*   [Create Maps Overview of: bean, frequencies, group-by, clojure.set/index]({% post_url 2014-09-16-create-clojure-map-advanced-methods-part-2 %})

*   [Read Clojure Map 1/2: get, get-in, contains?, find]({% post_url 2014-09-23-read-clojure-map-values-12%})

We are going to continue to explore how to read clojure map.

This time we are going to talk about `keys`, `vals` and `select-keys`.

## keys and vals

`keys` and `vals` are extremely similar.

`keys` return a sequence of all the keys of a map.

{% highlight clojure %}
user> (keys {:a 1 :b 2 :c 3 :d 4})
(:c :b :d :a)
{% endhighlight %}

`vals` return a sequence of all the values of a map.

{% highlight clojure %}
user> (vals {:a 1 :b 2 :c 3 :d 4})
(3 2 4 1)
{% endhighlight %}

Using `keys` and `vals` you need to remember that there is no order inside a simple `hash-map` so you cannot make any assumption about the final sequence.

However if you use `sorted-map` or also `array-map` you can assume that the order of the keys and the order of the values will be maintained.

{% highlight clojure %}
user> (keys (sorted-map :a 1 :b 2 :c 3 :d 4))
(:a :b :c :d)
user> (vals (sorted-map :a 1 :b 2 :c 3 :d 4))
(1 2 3 4)
user> (keys (array-map :a 1 :b 2 :c 3 :d 4))
(:a :b :c :d)
user> (vals (array-map :a 1 :b 2 :c 3 :d 4))
(1 2 3 4)
{% endhighlight %}

Something pretty obvious but useful to remember the use of `keys` and `vals` is the following snippet.

{% highlight clojure %}
user> (let [m {:a 1 :b 2}]
	    (= (zipmap (keys m) (vals m)) m))
true
{% endhighlight %}

## select-keys

This function is useful to shrink map.

Given a map and a sequence of keys return the map shrinked to only the keys in the sequence.

{% highlight clojure %}
user> (select-keys {:a 1 :b 2 :c 3} [:a :c])
{:c 3, :a 1}
user> (select-keys {:a 1 :b 2 :c 3} [:a :c :d])
{:c 3, :a 1}
{% endhighlight %}

As you can see if a key is not present in the original map the returning map won't contains such key.

## end

This was the last chapter about reading clojure map.

Next time we are going to explore deeply how to modify a map adding and removing entries.

As always stay tunned, and for any question don't esitate to write me.
