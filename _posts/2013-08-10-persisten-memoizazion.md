---
layout: post
title: "Non-volatile memoizazion"
description: ""
category: programming
tags: [clojure, memoizazion, non-volatile]
excerpt: "an idea for a non-volatile memoizazion"
---

Clojure provide a very handy function `memoize`, such function is so stupid and so powerful at the same time that is almost amazing.

Memoizazion is a technique that let to memorize the input and the output of a particular function, usually a heavy one, in this way if we need to re-call the same function with the same input we don't have to wait for the completation of the execution but we can just look up at the result.

Obviously it is not black-magic, and the function has to be a pure one, otherwise it won't works properly.

The little down-side of `memoize` is that it is volatile, if you memoize a function and then you restart your machine all the values of the first memoizazion are now gone.

The only way to get a non-volatile memoizazion is to write the result down somewhere that is not volatile, in this way even shutting down the machine the values are still there.

Obviously there are several trades off to do, write and read from the disk is way slower than from the RAM, and somehow more difficult; however it may worth if the function to memoize is a function ***very*** slow.

Let's check out the code of the function `fake` (aka persistent-memoize).

{% highlight clojure %}
(import '[java.io PushbackReader])

(defn make-name [f]
  (str "memo/"(clojure.string/replace (str f) #" " "") "-memo-function.clj"))

(defn- open-memo-file [name]
  (let [name (make-name name)]
    (try
      (with-open [r (clojure.java.io/reader name)]
        (read (PushbackReader. r)))
      (catch Exception e
        (do
          (println (str "File don't exist, will create file " name))
          {})))))

(defn fake [input name]
  (fn [& args]
    (let [stored (open-memo-file name)]
      (if-let [v (get stored args)]
        v
        (let [result (apply input args)
              new-file (merge stored {args result})]
          (with-open [w (clojure.java.io/writer (make-name name))]
            (binding [*out* w
                      *print-dup* true]
              (pr new-file)))
          result)))))
{% endhighlight %}

The function is very basic, it return another function that load a map and check if in such map there is, as a key, the argument of the function, if so return the value.

If in the map there is not the answer we were looking for the function compute the result, update the map, write the map down to disk and finally return the result itself.

Just like any other memoize functions.

There are several details worth a better look, so...

`fake` takes as argument a function *and* a name, such name will be part of the name of the file where the result would be stored.

This is very powerful, and, at the same time, very dangerous.

{% highlight clojure %}
user> (defn per ([a] (* a a)))
#'user/per
user> (def fake-per (fake per "per"))
#'user/fake-per
user> (fake-per 3)
File don't exist, create file memo/per-memo-function.clj
9
user> (fake-per 4)
16
user> (fake-per 5)
25
user> (defn per2 
		 ([a] (* a a))
		 ([a b] (* a b)))
		 
#'user/per2
user> (def fake-per (fake per2 "per")) ;;note, different function same name
#'user/fake-per
user> (fake-per 5)
25 ;; note that the file already exist
user> (fake-per 5 6)
30
{% endhighlight %}

The curious reader would like also to see how the files looks:

{% highlight clojure%}
#=(clojure.lang.PersistentArrayMap/create {(5 6) 30, (5) 25, (4) 16, (3) 9})
{% endhighlight %}

This is the power of clojure, code is data and data is code.

Another thing to point out is that the function, every time is called at least read the file, and if the result is not into the map, re-write the whole file.

Obviously it is not the best approach, it is very slow to read and to write a big file, if the file is too big we can also get memory issues.

However this type of memoizazion should be used only with very slow function and the bottle neck would be the execution of the function, not the reading/writing of the file.
Also a file too big to be read in clojure means a data-structure too big, even for the normal `memoize`.

In conclusion this is definitely not a perfect solution, however it is simple, does not need of anything, it is less than 50 lines of code, and is all I need.

I would like to invite anyone who is willing to try to fix some of the problem of this implementation:

What if I don't want it to write the whole file every single time a new value is created ? 

What if I don't want it to read the file every single time ?

What if I don't limit myself to .clj file ? And what about if we use a real SQL DB ? (can I encode the list of arguments in something easy to index ?)

It is this approach thread-safe ? Why ? Why not ? If not, how can we make it thread-safe ?

What if I want to make a kick-ass library out of idea ?

Comments with your suggestions, ideas, gist, or repo :)

Happy Hacking

Ah, I am for hire ;-)

{% include JB/setup %}
