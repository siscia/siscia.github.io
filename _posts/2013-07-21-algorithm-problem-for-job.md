---
layout: post
title: "Algorithm problem for job"
description: ""
category: 
tags: []
---
I was taking a curious look at a list of offer for functional job, and one in particular caught my attention.

I am not really interested in the job the offer, however, along with your resume you were suppose to send the solution to a couple of problem.

Both problem are very interesting, but for now I studied only one, and I have to say that I wasn't really able to solve it; I found a solution, but it is not good enough, I am sure that somehow is possible to make everything faster.

Anyway, the problem was similar to this one:
Given a list of integer, either positive and negative, write a function that return true if any subset of the list sum up to zero.

{% highlight clojure %}
(f [2 3 -5])
;; => true (== (+ 2 3 -5) 0)
(f [-6 2 3])
;; => false
(f [-7 4 3 8 -5])
;; => true (== (+ -7 4 3) 0)
{% endhighlight %}

The problem is already interesting, but I like to generalized the case so that the function works with any number, not only 0.

The obvious, slow and wrong solution (mine) is pretty easy, generate all the subset of the list, and then check if any of those subset add up to the number we are looking for.

The only tricky part here is how to generate all the subsets, I used a recursive call and the power of `lazy-cat`.

{% highlight clojure %}
(defn subset
  ([s]
     (subset [] s))
  ([tot r]
     (if (seq r)
       (lazy-cat
        (subset (conj tot (first r)) (next r))
        (subset tot (next r)))
       [tot])))
{% endhighlight %}

The algorithm is not very difficult, and looking carefully you will definitely understand it very quickly, however for the laziest, a [Stanford lecture](https://www.youtube.com/watch?v=NdF1QDTRkck) explain it.

Now that we have all the subsets, it is only a matter to check if any of those add up to the number we are looking for.


{% highlight clojure %}
(defn check-seq [num s]
  (cond
   (and
    (seq s)
    (= (apply + s) num)) s
   :else false))

(defn find-solutions [num s]
  (let [solutions
        (map #(check-seq num %)
             (subset s))]
    (filter boolean solutions)))

user> (find-solutions 0 [2 3 -5])
([2 3 -5])
user> (find-solutions 0 [-6 2 3])
()
user> (find-solutions 0 [-7 4 3 8 -5])
([-7 4 3] [-7 4 8 -5])
{% endhighlight %}

I hope you enjoy :)

Now, everyone who can think at some more efficient solution ?
You may comment this [gist](https://gist.github.com/siscia/6050217)

{% include JB/setup %}

