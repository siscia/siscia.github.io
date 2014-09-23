---
layout: post
title: "Read clojure map values 1/2"
description: ""
category: programming
excerpt: "First chapter about how to read values from a clojure map: get, get-in, contains?, find ."
tags: [clojure, map, read map, read, get, get-in, "contains?", find,]
---
{% include JB/setup %}

Continuing the series about clojure map we are now going to explore more deeply how to read a map.

For those who missed the previous chapters:

*   [First general introduction about clojure maps]({% post_url 2014-09-12-clojures-maps-overview %})

*   [Create Maps Overview of: hash-map, array-map, zipmap, sorted-map and sorted-map-by]({% post_url 2014-09-15-create-clojure-map-advanced-methods-part-1 %})

*   [Create Maps Overview of: bean, frequencies, group-by, clojure.set/index]({% post_url 2014-09-16-create-clojure-map-advanced-methods-part-2 %})

In the next 2 chapters we are going to explore more deeply functions such as: `get`, `get-in`, `contains?`, `find`, `keys`, `vals` and `select-keys`.

Let's start with the easiest one,

### get

As you already know from the first part of the series, `get` takes a map and a key as inputs and returns the value associated with that key in the map.

If the key is not present `get` returns nil.

{% highlight clojure %}
user> (get {:a 1 :b 2} :a)
1
user> (get {:a 1 :b 2} :c)
nil
{% endhighlight %}

`get` is a little more powerfull than this, if you provide a third argument in case of a missing key `get` will return such argument.

{% highlight clojure %}
user> (get {:a 1 :b 2} :c :value-not-found)
:value-not-found
user> (get {:a 1 :b 2} :c "of course it can be everything")
"of course it can be everything"
{% endhighlight %}

Also :keywords, that can be used as functions passing the map as argument, have this nice feature of the third argument.

{% highlight clojure %}
user> (:a {:a 1 :b 2})
1
user> (:d {:a 1 :b 2} :key-not-found)
:key-not-found
{% endhighlight %}

Now that we understand `get` let's move to its big brother,

### get-in

As you know maps can contain anything as value, even other maps.

It is easy to see that you can create arbitrarialy nested maps.

{% highlight clojure %}
user> (def nested-map {:a {:b {:c {:d "foo"} :e {:f {:g "bar"}}}}})
#'user/nested-map
user> nested-map
{:a {:b {:e {:f {:g "bar"}}, :c {:d "foo"}}}}
{% endhighlight %}

How do you access "foo" and "bar" ?

A possible, acceptable, solution would be to use the `->` macro.

{% highlight clojure %}
user> (-> nested-map :a :b :e :f :g)
"bar"
user> (-> nested-map :a :b :c :d)
"foo"
{% endhighlight %}

However this is exactly the job of `get-in`, let's see it in action:

{% highlight clojure %}
user> (get-in nested-map [:a :b :e :f :g])
"bar"
user> (get-in nested-map [:a :b :c :d])
"foo"
user> (get-in nested-map [:a :b :wrong :d])
nil
user> (get-in nested-map [:a :b :wrong :d] :not-found)
:not-found
{% endhighlight %}

Using the `get-in` function you will also get the possibility to specify the key-not-found return value.

### contains?

The name is self explanatory, it will tell you if a particular key is in the map or not, it won't return the value.

Bonus Fact: A little note about the name conventions in clojure: a function whose name terminates with `?` is supposed to return either `true` or `false`.

{% highlight clojure %}
user> (contains? {:a 1 "b" 2} :a)
true
user> (contains? {:a 1 "b" 2} :c)
false
user> (contains? {:a 1 "b" 2} "b")
true
{% endhighlight %}

### find

Finally let's talk briefly about `find`, as you may have guessed `find` will lookup a map entry in your map and return it.

A map entry is a pair `[:key "value"]`.

{% highlight clojure %}
user> (find {:a 1 "b" 2} "b")
["b" 2]
user> (find {:a 1 "b" 2} :c)
nil
{% endhighlight %}

### End

Next time we are going to explore three more functions, `keys`, `vals` and `select-key`.

In a couple of chapters we will discuss why map entries are important.

As always, if you have any questions or would like to just say `hi` you can comment here or write me an email.
