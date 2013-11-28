---
layout: post
title: "Visualize hierarchy behind java class"
description: ""
category: 
tags: [clojure, go, clojurescript]
---

Once upon a time any young programmer feel the need to learn something new, and sure as the Murphin law this need will be more urgent as the young programmers approaches his exams at the university.

At my class of programming 101 we are studying C (again) and pointer, impure functions and other thing I wish I had forget thanks to Clojure come back being daily bread (again :( )

Since I already know (inc 'B') good enough to pass my class without too much effort, but since I also feel guilty to don't doing anything while I should be re-studying how to use pointer, I decided to use that time studying Go, so I could refresh the use of pointer, structs, types. 

At very basic level C and Go are pretty much the same language with a slightly different syntax.

Honestly Go felt like home pretty quickly, a duck-type language background helped me a lot here, so I was able to start coding some data-structure quickly and I decide to see what a VList looks like (VList are very basic building block in clojure, for what I have understand are the base of maps, sets and lists), I spend a lot of time studying the paper which introduces VList and finally I was able to implement my own version.

And here it comes the idea, what if I write the interfaces of such Vlist in such way to respect the interface/protocol of clojure list ?

Then I would need to add maps, vector, functions, numbers, string, etc... and I get all the clojure structure coded in Go.

Then we take the ClojureScript AST and we just auto-generate code from ClojureScript to Go.

And here we go we have clojure(script) that compile down to Go, sound easy doesn't ?

So I decide to see what is the interface of clojure list; if you take a look at [PersistentList.java](https://github.com/clojure/clojure/blob/master/src/jvm/clojure/lang/PersistentList.java) you will see that  PersistenList extends an abstract class and implements 4 interfaces (IPersistentList, IReduce, List and Counted), already too much to code by hand.

Fortunately the java class Class let you inspect any class, so with few lines of code is possible to see what interfaces are implemented and what is extended.

At this point we can just build a tree of hierarchy, and print it out, that is exactly what I did, just to have an idea how big is the system behind clojure you can take a look at this picture.

It all took ~50 lines of code, [here](https://github.com/siscia/java-interface-to-go/blob/master/src/java_interface_to_go/from_runtime.clj)

(sorry for the formatting, but I want to show all together...)

`(show-tree (class '()))`
![empty-list](https://raw.github.com/siscia/java-interface-to-go/master/images/class%20clojure.lang.PersistentList$EmptyList.png)
`(show-tree (class {:a :b}))`
![map](https://raw.github.com/siscia/java-interface-to-go/master/images/class%20clojure.lang.PersistentArrayMap.png)
`(show-tree (class inc))`
![inc-function](https://raw.github.com/siscia/java-interface-to-go/master/images/class%20clojure.core$inc.png)

Next step is to generate the Go interfaces and glue them together to copy the clojure system, this is pretty much already done, but I already wrote to much for this post.

After that I need to really start thinking about what I am doing and if it will never possibly works and if it is worthed...

If I decide to keep moving then it would be necessary to code all those structures and that is gonna be a pretty big job, but since the interface are already defined it shouldn't be too problematic.

Please let me know what you think :)

PS: I am gonna be a volunteer and the Milan, ITALY, CodeMotion if you are gonna be there just drop me a line we can share a beer, or something.

{% include JB/setup %}