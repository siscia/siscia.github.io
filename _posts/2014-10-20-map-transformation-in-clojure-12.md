---
layout: post
title: "Map transformation in clojure 1/2"
description: "First chapter about how to modify maps in clojure: assoc, dissoc and merge"
category: programming
tags: [clojure, map, maps, clojure map, assoc, dissoc, merge]
excerpt: "First chapter about how to modify maps in clojure: assoc, dissoc and merge" 
---
{% include JB/setup %}

Here it's another chapter of the series about clojure map.

For those who missed the previous chapter:


*   [First general introduction about clojure maps]({% post_url 2014-09-12-clojures-maps-overview %})

*   [Create Maps Overview of: hash-map, array-map, zipmap, sorted-map and sorted-map-by]({% post_url 2014-09-15-create-clojure-map-advanced-methods-part-1 %})

*   [Create Maps Overview of: bean, frequencies, group-by, clojure.set/index]({% post_url 2014-09-16-create-clojure-map-advanced-methods-part-2 %})

*   [Read Clojure Map 1/2: get, get-in, contains?, find]({% post_url 2014-09-23-read-clojure-map-values-12%})

*   [Read Clojure Map 2/2: keys, vals, select-keys]({% post_url 2014-09-28-read-clojure-map-values-22 %})

Let's keep going in our journey about clojure map.

In the next chapters I am going to talk about how to modify clojure maps.

As you may know in Clojure we usually don't "modify" anything but we rather return a new value.

Let's explore what function clojure.core gives us to modify maps.

The easiest function to start with is definitely

## assoc

Given a map, a key and a value `assoc`(ciate) add the key and the respective value to the map.

{% highlight clojure %}

user> (assoc {:a 1 :b 2} :c 3)
{:c 3, :b 2, :a 1}
{% endhighlight %}

As you may guess `assoc` can take more than just a couple of `:keys value`.

{% highlight clojure %}

user> (assoc {:a 1 :b 2} :c 3 :d 4)
{:d 4, :c 3, :b 2, :a 1}
user> (assoc {:a 1 :b 2} :c 3 :d 4 :e 5)
{:e 5, :d 4, :c 3, :b 2, :a 1}
{% endhighlight %}

It is important is that you don't forget to provide an even number of argument after the map.

{% highlight clojure %}

user> (assoc {:a 1 :b 2} :c 3 :d)
IllegalArgumentException assoc expects even number of arguments after map/vector, found odd number  clojure.core/assoc (core.clj:192)
{% endhighlight %}

You may also wonder what happens if you try to `assoc` to an already existing key.

{% highlight clojure %}

user> (assoc {:a 1 :b 2} :a "new-value")
{:b 2, :a "new-value"}
{% endhighlight %}

As we can see `assoc` will reset (update) the old value to the new one.

`assoc` is a perfectly legitimate way to update old values in a clojure map.

If `assoc` will make our maps bigger

## dissoc

will make them smaller.

As you may have already guessed `dissoc`(ciate) will remove a map entry from our maps.

It works exactly like `assoc`.

{% highlight clojure %}

user> (dissoc {:a 1 :b 2 :c 3} :a)
{:c 3, :b 2}
{% endhighlight %}

If you pass more arguments it will remove more map entries

{% highlight clojure %}

user> (dissoc {:a 1 :b 2 :c 3} :a :b)
{:c 3}
{% endhighlight %}

Also note that `dissoc` a not existing key is a valid behavior, dissoc will eliminate the map entry, which does not exist and will return the (not) updated map.

{% highlight clojure %}

user> (dissoc {:a 1 :b 2 :c 3} :d :e :f)
{:c 3, :b 2, :a 1}
{% endhighlight %}

## merge

Another very useful function is `merge` which, as you may have guessed, merge two or more different maps into one.

{% highlight clojure %}

user> (merge {:a 1 :c 3} {:b 2 :d 4})
{:d 4, :b 2, :c 3, :a 1}
user> (merge {:a 1 :c 3} {:b 2 :d 4} {:foo "foo" :bar :bar})
{:foo "foo", :bar :bar, :d 4, :b 2, :c 3, :a 1}
{% endhighlight %}

`merge` is very simple to reason about, but there is a little detail to keep in mind.

What happens if there is a key collision (if we try to merge two maps with some keys in common) ?

Fortunately this case is documented and made clear in the spec.

In case of key collision the resulting element will be the later to appear.

{% highlight clojure %}

user> (merge {:a 1} {:a 2})
{:a 2}
user> (merge {:a 1 :b 1} {:a 2 :c 2} {:c 3 :b 3})
{:c 3, :b 3, :a 2}
{% endhighlight %}

## end

In the next chapter we are going to explore some function a little more complex, function such as `update-in` and `merge-with`.

As always stay tuned and for any question please don't hesitate to write me or to comment bellow.

