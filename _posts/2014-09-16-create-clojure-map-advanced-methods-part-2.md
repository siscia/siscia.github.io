---
layout: post
title: "Create Clojure Map, advanced methods, PART 2"
description: ""
category: programming
tags: [clojure, map, create map, bean, frequencies, group-by, index, clojure.set/index]
excerpt: "Final chapter about functions which return map: bean, frequencies, group-by and clojure.set/index ."
---
{% include JB/setup %}

Let's continue our journey of functions that return maps.

For those missed the first chapters:

*   [First general introduction about clojure maps]({% post_url 2014-09-12-clojures-maps-overview %})

*   [Part 1 Overview of: hash-map, array-map, zipmap, sorted-map and sorted-map-by]({% post_url 2014-09-15-create-clojure-map-advanced-methods-part-1 %})

In this chapter I am going to talk about, `bean`, `frequencies`, `group-by` and finally `clojure.set/index`.

Let's start with

### bean

if you don't take advantage of the clojure compatibility with java, `bean` is quite useless to you. However if you do import java libraries in your clojure code `bean` can be one of your best friends.

Given a java object, `bean` returns a "map" that represents such object.

The best example I could figure out is the one from the clojure doc.

{% highlight clojure %}
user> (def now (Date.))
#'user/now
user> now
#inst "2014-09-17T06:56:43.345-00:00"
user> (def bean-map (bean now))
#'user/bean-map
user> bean-map
{:day 3, :date 17, :time 1410937003345, :month 8, :seconds 43, :year 114, :class java.util.Date, :timezoneOffset -120, :hours 8, :minutes 56}
user> (.setDate now 25) ;; attention here
nil
user> now
#inst "2014-09-25T06:56:43.345-00:00"
user> bean-map ;; please note the field `date`
{:day 4, :date 25, :time 1411628203345, :month 8, :seconds 43, :year 114, :class java.util.Date, :timezoneOffset -120, :hours 8, :minutes 56}
{% endhighlight %}

Please, be very careful here.

What bean returns is not an actual map but something more complex that implements the map protocol.

What you need to know is that changing the underneath original object will do change the "map" that `bean` returns, so be very careful.

### frequencies

As the name suggests, given a sequence, `frequencies` returns a map with the frequency of each object in the sequence itself.

{% highlight clojure %}
user> (frequencies [:a :b :a :a :b :c :d :a :b])
{:a 4, :b 3, :c 1, :d 1} ;; there are 4 :as, 3 :bs, one :c and one :d
user> (frequencies (take 100 (repeatedly #(rand-int 4))))
{3 24, 2 27, 0 15, 1 34} ;; pretty random
{% endhighlight %}

If you have understood `frequencies`

### group-by

is similar. Let me show you a simple example.

{% highlight clojure %}
user> (odd? 1)
true ;; 1 is odd
user> (odd? 2)
false ;; 2 is even
user> (range 10)
(0 1 2 3 4 5 6 7 8 9)
user> (group-by odd? (range 10))
{false [0 2 4 6 8], true [1 3 5 7 9]}
user> (defn odd-but-3 [n]
	(if (== 3 n)
		"Three"
		(odd? n)))
#'user/odd-but-3
user> (group-by odd-but-3 (range 10))
{false [0 2 4 6 8], true [1 5 7 9], "Three" [3]}
{% endhighlight %}

As you can see `group-by` calls the function you provide for every element in the sequence. It stores the output as a key and, as a value, the collection of those elements who returns the same output.

### clojure.set/index

This function is a little complex.

First and foremost we are working with sets, as you may know sets are collections of unique unordered elements.

{% highlight clojure %}
user> #{:a :b :c}
#{:c :b :a}
user> (clojure.set/union #{:a :b :c} #{:a :h :g})
#{:g :c :h :b :a} ;; no repetition of :a
{% endhighlight %}

It is very fast to add element to a set or to check if an element is in the set.

{% highlight clojure %}
user> (contains? #{:a :b} :a)
true
user> (contains? #{:a :b} :c)
false
{% endhighlight %}

Of course sets may also contain maps.

{% highlight clojure %}
{% raw %}
user> #{ {:a 1 :b 2} {:a 1 :b 3} {:a 2 :b 2} }
#{{:b 2, :a 1} {:b 3, :a 1} {:b 2, :a 2}}
{% endraw %}
{% endhighlight %}

If I have a big set of maps I may want to explore those maps more deeply and I may need to aggregate together all the maps with the same value for some particular key, this is `clojure.set/index`.

{% highlight clojure %}
{% raw %}
user> (require '[clojure.set :refer [index]])
nil ;; or call clojure.set/index
user> (def my-set #{ {:a 1 :b 2} {:a 2 :b 1} {:a 1 :b 1} })
#'user/my-set
user> (index my-set [:a]) ;; aggregate for :a
{
 {:a 2} #{ {:b 1, :a 2} }, ;; set of one map
 {:a 1} #{ {:b 2, :a 1} {:b 1, :a 1} } ;; set of two maps
}
user> (index my-set [:b]) ;; aggregate for :b
{
 {:b 1} #{{:b 1, :a 2} {:b 1, :a 1}},
 {:b 2} #{{:b 2, :a 1}}
}
user> (index my-set [:a :b])
{
 {:b 1, :a 1} #{{:b 1, :a 1}},
 {:b 1, :a 2} #{{:b 1, :a 1}},
 {:b 2, :a 1} #{{:b 2, :a 1}}
}
{% endraw %}
{% endhighlight %}

`index` is very complex to explain thus I am afraid that I would create more confusion than other trying to word what you can see in action.

If you aren't completely sure about `index` you may try to run the function inside a repl: maybe a bigger and more etereogeneous map will help.

As always if you have any question please write a comment bellow.

### End

This chapter was very short and probably somehow boring, but it was necessary for the sake of completeness.

Next time we are moving on to something way more fun and useful.

[Next Chapter, Read Clojure Map overview of: get, get-in, contains? and find]({% post_url 2014-09-23-read-clojure-map-values-12.md %})

As always, stay tuned and write to me if you have anything to say (Ex. Some question, a request for an article, anything...)

