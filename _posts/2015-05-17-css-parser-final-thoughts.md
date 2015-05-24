---
layout: post
title: "css parser final thoughts"
description: "Final thoughts and key take away from my experience  with writing a CSS parser."
category:
tags: [clojure, programming, parser, css, CSS, lazy-seq, take away]
---

I just released the very first draft version of [css-parser](https://github.com/siscia/css-parser).

Write the grammar was a rough job and I would like to share what went good and what went bad.

## The Bad

### CSS

If you write a grammar to parse any CSS file you will get to know a lot about CSS.

I was definitely acquainted with CSS, but the more I worked with it the less I liked it.

For most shorthand, property than set more values at the same time, some example are `font` and `margin`, you can mix up the order of any value, and even if a standard form seems to have been reached online, I believe that it does not help the maintainability of the code.

#### Take Away

Get to know your enemy well before fighting it...

### Documentation

The documentation around CSS is very sparse and not well written.

I decided to take the MDN documentation as the official one for the project, but a lot of times I found myself frustrated and unable to fully understand it.

I need to say that the most used property are well documented, however a more systematic approach is more desirable in my opinion.

#### Take Away

Create your own certainties.

Probably the MDN documentation is not the best one for every single property and rule, however in a big project it is necessary to set a few key points in stone and start moving forward.

### Big

The whole grammar is HUGE, the work seems never ending and most of the times I just wanted to give up.

There seems to be always more and more. You write your way around a problem and something you haven't think about pops up, it gets really frustrating after a while.

What helped me is that I divided the work into two big chunks, first I wrote a parser for the CSS types (stuff like, `2px` or `4em` or `rgb(10, 10, 10)`) and then the parser for the whole property and rules.

#### Take Away

One single big project is more difficult than a lot of smaller simple projects: break your task in measurable smaller chunks and reward yourself after any small victory. They sum up...

## The Good

### Instaparse

I cannot stretch enough what a wonderful servant Instaparse has been. The grammar it understands is extremely powerful and flexible and I had only a very [small problem](https://github.com/Engelberg/instaparse/issues/95) to express the CSS grammar needed, problem that was simple to circumnavigate.

The grammar ended up being pretty big, and it needs about 5 secs to generate the parser Instaparse.

It seems a lot, and actually it is a lot, but the work behind the scenes must be huge.

It is extremely fast to parse and produce the tree for reasonable string.

I noticed, however, that my grammar suffer a lot if too many white spaces are inside the string.

#### Take Away

Leverage other people's works: their work will never perfectly fit your needs but reinventing the wheel every time won't let you move forward.

### Lazy-seq / Clojure

The power of lazy-seq is really amazing, but what is more amazing is how simple is to write a function that generate lazy-seq.

I wrote a small algorithm to break a big file into more manageable pieces, it looks almost a procedural algorithm and the tools that I used, `loop`, `transiet`, `recur` and `lazy-seq` were the best tools I could think of.

#### Take Away

Have powerful ally and know their strengths. I knew how powerful clojure and lazy sequence are when you analyze and manipulate data: leverage such strengths made my works a breeze.

### Emacs

I was able to find online [a reference](http://cssvalues.com/) with all the value that any property can assume.

I used import.io to download such reference and I used Emacs to edit it and create a instaparse grammar.

This approach shaved a lot of work but didn't work well enough with the shorthands.

Of course shorthands are the most used property in CSS so it was out of question to leave them out, I ended up writing the grammar for the shorthands by myself.

Another approach I thought was to encode the reference in a clojure map and programmatically write the grammar via software. I chose not to follow this route because it would have been really too much work and I wasn't really sure that I could leverage such work in the future...

#### Take away

Automatization is the key, however write the algorithms necessary takes a lot of time. Use heavily what you already got and think carefully if you really need to make everything automatic. Most of the times get your hands dirty will be faster than writing the code that does the job for you.

### Keep pushing

I lost interest in the project around midway, however I decided to keep pushing it and keep doing it.

I really wanted to get something done and finished.

I allocated around one hour per day to the project and slowly I worked my way through the end.

I am extremely glad I finished it, because the satisfaction of a public release, knowing that you did a good and solid job is great.

I was amazed by how much you can accomplish in one hour a day every day.

#### Take Away

It really feels good to finish it. Maybe nobody will never use the code I wrote and I will forget everything in 2 months, but it does feel good to have accomplished something, even if small and trivial.

## Final Though

As I said, writing this parser was a really neat experience, I am glad I did and I am looking forward to see if the parser is useful to anybody.



{% include JB/setup %}
