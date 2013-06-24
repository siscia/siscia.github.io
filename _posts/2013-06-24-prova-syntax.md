---
layout: post
title: "prova syntax"
description: ""
category: 
tags: []
---

Start Start

With 3 \` syntax below:

```clojure
(def trying []
  (println "formatting for jekyll in github"))

(doall
   (map trying (range 10)))


(defn a []
  (loop [a 1 b 2]
    (if (= a 3)
    b
    (recur (inc a) (dec b)))))
```

With other pygems below:

{% highlight clojure %}

(map fancy-function [:fancy :collection])

(reduce + [1 2 3])

(defn a []
  (loop [a 1 b 2]
    (if (= a 3)
    b
    (recur (inc a) (dec b)))))

{% endhighlight%}


End End

{% include JB/setup %}
