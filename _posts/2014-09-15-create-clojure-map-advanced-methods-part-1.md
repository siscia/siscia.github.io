---
layout: post
title: "Create Clojure Map, advanced methods, PART 1"
description: ""
category: programming
tags: [clojure, maps, create maps, array-map, hash-map, zipmap, sorted-map, sorted-map-by]
excerpt: "Deeper overview of few function to create clojure's maps, in particular hash-map, array-map, zipmap, sorted-map and sorted-map-by."
---
{% include JB/setup %}

As I promised in the [first general introduction about clojure maps]({% post_url 2014-09-12-clojures-maps-overview %}) I am going to show way methods to create maps.

Let's start exploring the function that return maps.

### hash-map

How you may guess by yourself hash-map takes as input an even number of argument and return a map.

{% highlight clojure %} 
user> (hash-map :key :val :a :b)
{:key :val, :a :b}
user> (hash-map :key :val :a :b :wrong)
IllegalArgumentException No value supplied for key: :wrong  clojure.lang.PersistentHashMap.create
{% endhighlight %}

### array-map

Here it is something more exotic.

Let's start introducing what an ArrayMap is. An ArrayMap is an array of key, val, key, val, etc... that does implement the whole map interface.

Because the implementation it will keep the order of the key val, however it is only suitable for very small maps.

ArrayMap is guaranteed to keep the order only when unmodified.

{% highlight clojure %}
user> (array-map :a 1 :b 2)
{:a 1, :b 2}
user> (assoc (array-map :a 1 :b 2) :c 3)
{:c 3, :a 1, :b 2}
user> (seq (array-map :a 1 :b 2)) ;; more of this in another chapter
([:a 1] [:b 2])
user> (seq (assoc (array-map :a 1 :b 2) :c 3))
([:c 3] [:a 1] [:b 2])
{% endhighlight %}

Those are not extremely popular structure, but they exists.

### zipmap

`zipmap` is a very handy function, you may compare this function to the zip of your jacket, you have a sequence of little tooth from one side, another sequence of little tooth from the other side and running the zipper you map a teeth to the other.

The function takes two sequence as input, a sequence of keys and a sequence of values and return a map.

The map is as long as the shorter of the two inputs.

{% highlight clojure %}
user> (zipmap [:a :b :c] [1 2 3])
{:c 3, :b 2, :a 1}
user> (zipmap [:a :b :c :d :e] [1 2 3]) ;;the shorter seq wins
{:c 3, :b 2, :a 1}
user> (zipmap [:a :b :c] [1 2 3 4 5 6])
{:c 3, :b 2, :a 1}
user> (zipmap [:a :b :c] (range)) ;; it works with lazy seq too
{:c 2, :b 1, :a 0}
user> (zipmap (range) (range)) ;; careful here, it will run forever.
;; Evaluation interrupted
{% endhighlight %}

### sorted-map

Here something very interesting.

You can think about SortedMap as a mix between HashMap and ArrayMap, with the best from the two worlds.

SortedMap keep the order of the keys, but at the same time is implemented as a tree so it is fast to look up values or modify the map.

However there are some point to keep in mind.

The order that a sorted-map keeps is the order given by the function [`compare`](http://grimoire.arrdem.com/1.6.0/clojure.core/compare/) this means that the keys of your map must be comparable somehow.

It intuitive to define the order between a sequence of Number, either Int, Float, etc... first the smaller then the bigger. It is still easy to define the order between strings, let's follow the alphabet. But what is the order between a string and a number ? Which come first ?

{% highlight clojure %}
user> (compare 1 2)
-1 ;; < 0 => 1 before 2
user> (compare "b" "a")
1 ;; > 0 => "b" after "a"
user> (compare :a :a)
0 ;; == 0 => :a == :a
user> (compare "a" 1) ;; Error, string and number cannot be compared
ClassCastException java.lang.Long cannot be cast to java.lang.String
{% endhighlight %}

An implication of this is that you cannot build a sorted-map which has some integer and some string as keys.

{% highlight clojure %}
user> (sorted-map :a 2 "a" 3)
ClassCastException clojure.lang.Keyword cannot be cast to java.lang.String
user> (sorted-map :a 2 1 3)
ClassCastException clojure.lang.Keyword cannot be cast to java.lang.Number
{% endhighlight %}

Now that we know the details that SortedMaps are based on we can move on something more practical.

{% highlight clojure %}
user> (sorted-map :a 1 :b 2)
{:a 1, :b 2}
user> (seq (sorted-map :a 1 :b 2))
([:a 1] [:b 2])
user> (sorted-map :a 1 :b 2 :az 3)
{:a 1, :az 3, :b 2}
user> (seq (sorted-map :a 1 :b 2 :az 3))
([:a 1] [:az 3] [:b 2])
user> (compare :a :az)
-1 ;; < 1 :a before :az
{% endhighlight %}

Of course you can still merge, assoc and dissoc SortedMap and they will always keep their order.

{% highlight clojure %}
user> (seq (assoc (sorted-map :a 1 :b 2) :az 3))
([:a 1] [:az 3] [:b 2])
user> (seq (dissoc (sorted-map :a 1 :b 2 :az 3) :az))
([:a 1] [:b 2])
user> (seq (merge (sorted-map :a 1 :bz 2) (sorted-map :az 3 :b 4)))
([:a 1] [:az 3] [:b 4] [:bz 2])
{% endhighlight %}

SortedMap are very useful but are limited by what the function `compare` can takes as input, to solve this problem we can use

### sorted-map-by

SortedMapBy are a generalizazion of SortedMap.

`sorted-map-by` takes as input also a function, a comparator, that it is used to determinate the order between the keys in your map.

A comparator is a function that takes two inputs and return > 0 if the second input is smaller than the first one < 0 otherwise or 0 if the inputs are equals.

You need to be careful writing your own comparator because if two different keys are compared equal you will loose a value from your map.

{% highlight clojure %}
user> (defn wrong-comparator [a b]
	(if (and (string? a) (string? b))
	  0
	  (compare a b)))
#'user/wrong-comparator
user> (sorted-map-by wrong-comparator "a" 1 "b" 2)
{"a" 2} ;; ??? Completely unexpected
{% endhighlight %}

Of course if you pass `compare` as function in `sorted-map-by` you will end up with a simple SortedMap.

### End

This is all I get for now, next time I will talk about other functions that return maps: `bean`, `frequencies`, `group-by` and `clojure.set/index`

If you have any questions or suggestions please let me know, I am extremely interested in your opinion.

Also, if you have some topic you wish to explore more deeply feel free to require it in the comments below.
(Eg. Anyone here is interested in the use of transiet ?) 

