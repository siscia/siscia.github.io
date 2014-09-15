---
layout: post
title: "Clojure's Maps Overview"
description: "A simple and easy to follow view about clojure maps."
excerpt: "A simple and easy to follow view about clojure maps."
category: programming
tags: [clojure, map, data structure, datastructure, overview, quick, simple, easy]
---
{% include JB/setup %}

 Maps are fundamental data structures in any clojure program.

They are extremely fast, simple to reason about and very handy.

## Declaration of maps

As you may know, maps are a correlation between two clojure 'object' and are defined as so:

{% highlight clojure %} 
{"key_a" "value_a" 
 "key_b" (fn [b] "value_b") 
 :etc :etc} 
{% endhighlight %}

Let's notice first that a map must contain an even number of elements, otherwise the reader will let you know.

{% highlight clojure %} 
user> {"a" "b" "c"} 
RuntimeException Map literal must contain an even number of forms 
{% endhighlight %}

Also you can use different types of object as your key or values in your map.

{% highlight clojure %} 
user> {"string" (fn [] "function") 
       :keyword 1} 
{"string" #<user$eval2509$fn__2510 user$eval2509$fn__2510@63a081d2>, :keyword 1 }
{% endhighlight %}

In the clojure world we use a lot of `:keywords`. They are particular data-type, very similar to string but that fit particularly well into map.

Of course you can assign a name to your map.

{% highlight clojure %} 
user> (def my-map {:a "b" "c" "d"})
#'user/my-map
user> my-map
{"c" "d", :a "b"} ;; important, note the order of the couple key-value 
{% endhighlight %}

One very important thing to notice is that the order of the couple `{:key :value}` is not fixed inside a map: in fact if you think about it, it doesn't make sense for a map to be ordered.

You can find a deeper explaination about how to create maps in the following post:
    [Create clojure map, advanced method. PART 1]({% post_url 2014-09-15-create-clojure-map-advanced-methods-part-1 %})

## Read map

Now that we know how to define a basic map, let's see how to read the values inside it.

One of the simplest ways to read a value from a map is the function get.

{% highlight clojure %}
user> (get {:a :b} :a)
:b
user> (get {:a :b} :foo)
nil
{% endhighlight %}

Another and more used way to get values from a map is to use the map itself as a function and the key as an argument.

{% highlight clojure %}
user> (def my-map {:a "b" "c" "d"})
#'user/my-map
user> (my-map "c")
"d"
user> (my-map "value not present")
nil
{% endhighlight %}

Finally a very used way to get values out of a map is to use keywords as functions and the map itself as argument.

{% highlight clojure %}
user> (:a my-map) ;;using the keyword as a function
"b"
user> (my-map :a) ;; normal behaviour using the map as a function
"b"
user> ("c" my-map) ;; only keywords may be used as functions
ClassCastException java.lang.String cannot be cast to clojure.lang.IFn
{% endhighlight %}

## "Modify" map

As you may know it is not possible to modify a clojure map, since it is  immutable.

However you may create new maps with a different number of keys, thus a different number of values.

To add a value into a map, the easiest way is to use the function assoc, that gets the old map, the new keys and the new values  as arguments.

{% highlight clojure %}
user> my-map
{"c" "d", :a "b"}
user> (assoc my-map "d" "e")
{"d" "e", "c" "d", :a "b"}
user> my-map
{"c" "d", :a "b"}
user> (assoc my-map "first new key" :first-new-value
                    :second-new-key "second new value")
{:second-new-key "second new value", "first new key" :first-new-value, "c" "d", :a "b"}
user> (assoc my-map :a "bar") ;; attention here
{"c" "d", :a "bar"}
{% endhighlight %}

In case of conflict `assoc` will overwrite the old values.

On the other side it is also very easy to remove keys-values from a map using the function `dissoc`.

`dissoc` takes the map as input and one or more keys you want to eliminate.

{% highlight clojure %}
user> (def my-map {:a "pointless-value" :interesting-key "interesting-value" "pointless-key" :d})
#'user/my-map
user> (dissoc my-map :a)
{"pointless-key" :d, :interesting-key "interesting-value"}
user> (dissoc my-map :a "pointless-key")
{:interesting-key "interesting-value"}
{% endhighlight %}

Finally it is possible to merge two different maps using the function merge that takes 2 or more maps as argument and returns one single map.

{% highlight clojure %}
user> (def m1 {:a 1 :b 2})
#'user/m1
user> (def m2 {:c 3 :d 4})
#'user/m2
user> (merge m1 m2)
{:c 3, :b 2, :d 4, :a 1}
user> (merge {:a 1} {:a 2} {:a :foo}) ;;attention here
{:a :foo}
{% endhighlight %}

Please note that the last argument is the one that will be chosen in case of conflict between the keys.

## End

This post was just a very quick overview about clojure maps, each of the three points I tackled (declare, read and modify maps) can be expandend quite a lot.

It would be awesome if you guys could comment asking which point you'd rather me to cover next time.
