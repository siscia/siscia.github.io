---
layout: post
title: "Manage (Mongodb's) ObjectId and json"
description: ""
category:
tags: [clojure, mongo, mongodb, rest, REST]
---

I was writing yet another REST interface in Clojure + MongoDB (this is the last time) and if you have ever mixed this technology there is a little issue that raises every single time.

The product is simple, pure REST that respond to the canonical GET, POST, PUT, PATCH and DELETE verb in JSON, the standard.

In some way you manage to get the request, you process whatever you need to process, you probably write something in the database and finally you need to generate a response.

The most immediate approach works pretty well, you generate a clojure map that represent the response, you convert such map into a JSON string and you return such string.

However if you are using MongoDB changes are that you will have some of this object `org.bson.types.ObjectId` hanging around, most likely your JSON generator won't know how to deal with them, so it will just raise an Exception, and if you are working with Liberator you will probably loose some solid minutes figuring out what went wrong.

After you figure out what is wrong, the most immediate solution is something very simple, you simply figure out that `ObjectId` is the values of MongoDB ids and you just make sure to replace every single `:_id` with a string.

```clojure
(ns your.namespace
  (:require [cheshire.core :refer [generate-string]]))

(defn generate-json [m]
  (-> m
      (update-in [:_id] str)
      generate-string))
```

If your backend is pretty simple it may just work fine, but most likely the backed will grow, and you will start to make connections between the different objects of your MongoDB database, most likely you will add at the simple `movie` document the list of your users who watched the movie, and now you get more `ObjectId` around.

Of course we can keep adding `(update-in ....)` in your `generate-json` but it is pretty obvious that such approach won't last long.

The next solution I implemented is another very obvious solution, coerce every `ObjectId` in your map into string.

Easy to say, but not so easy to implement.

The simplest solution that I found is to use `clojure.walk/{pre,post}walk`.

The code is pretty much the same as `clojure.walk/stringify-keys`

```clojure

(defn convert-ObjectId-to-string [[k v]]
  (if (= org.bson.types.ObjectId (class v))
    [k (str v)]
    [k v]))

(defn convert-all-ObjectId [m]
  (clojure.walk/postwalk
    (fn [m]
      (if (map? m)
        (into {} (map convert-ObjectId-to-string m))
        m))
    m))

(defn generate-json [m]
  (-> m
      convert-all-ObjectId
      generate-string))

```

This approach works everytime, but it may not be so efficient because, before writing the string, you will walk all the map in order to convert every single possible `ObjectId`, even if there are none of them.

Finally the most elegant solution I found is to teach your JSON writer how to deal with `ObjectId'.

The approach is possible in [cheshire](https://github.com/dakrone/cheshire) and [clojure.data.json](https://github.com/clojure/data.json).

If you are using cheshire you add an encoder, internally it extends a protocol.

```clojure

(ns your.namespace
  (:require [cheshire.core :refer [generate-string]]
            [cheshire.generate :refer [add-encoder encode-str]]))

(add-encoder org.bson.types.ObjectId encode-str)

;; which is equivalent to

(add-encoder org.bson.types.ObjectId (fn [s g] (.writeString g (str s))))

(generate-string {:_id (ObjectId.)})
;; "{\"_id\":\"53ff596144fc363fad297b75\"}"

```

If you are using `clojure/data.json` you just need to write a small function and parse it as argument at the generator.

```clojure
(ns your.namespace
  (:require [clojure.data.json :refer [write-string]]))

(defn write-ObjectId [k v]
  (if (= org.bson.types.ObjectId (class v))
    (str v)
    v))

(write-string {:_id (ObjectId.)}
              :value-fn write-ObjectId)
;; "{\"_id\":\"53ff596144fc363fad297b75\"}"
```

I am actually looking for a job, if you are interested in hire me or just say "hi" please feel free to send me an email.

Also, if you wold like more posts about clojure and rest please let me know.

I was planning to write about [Liberator](http://clojure-liberator.github.io/liberator/), a clojure micro-framework for rest app, so you are welcome to email me or write a comment.


{% include JB/setup %}
