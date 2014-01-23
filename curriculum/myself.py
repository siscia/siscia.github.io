from functools import wraps
import inspect
import pystache


def lazy():
    return run("curriculum.mustache", "cv.html")

def run(inp, outp):
    me = MySelf("Simone Mosciatti", "siscia")
    struct = generate_struct(me)
    with open(inp, "r") as t:
        text = t.read()
        html = pystache.render(text, struct)
        with open(outp, "w") as h:
            h.write(html)
            return html

def isToShow(f):
    try:
        return f.to_show
    except Exception:
        return False

def callMethods(obj, attribute):
    methodcall = [{"alias" : obj.alias,
                   "method-name" : x[0],
                   "results" : x[1]()} for x in attribute]
    return methodcall
        
def generate_struct(obj):
    struct = {"method-call" : [],
              "alias" : obj.alias,
              "name" : obj.name,}
    attribute = inspect.getmembers(obj)
    attribute = [x for x in attribute if isToShow(x[1])]
    attribute.sort(key = lambda a: a[1].order)
    methodCall = callMethods(obj, attribute)
    struct["method-call"] = methodCall
    return struct
    
def manage_method(order, to_show=True):
    def _inner(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        inner.to_show = to_show
        inner.order = order
        return inner
    return _inner

        
class MySelf(object):
    def __init__(self, name, alias):
        self.name = name
	self.alias = alias
        self.info = {"Email" : "simone@mweb.biz",
                     "Born" : "9th July 1994",
                     "Address" : "Via Pitteri, 56 Milano Italy"}
        self.online = {"Blog" : "siscia.github.com",
                       "Github" : "github.com/siscia",
                       "Twitter" : "@siscia_"}
        self.languanges = {"Love it" : ["Python", "Clojure"],
                           "Know it" : ["C/C++"],
                           "Learning" : ["Javascript", "Haskel", "Golang"]}

    @manage_method(1, True)
    def print_info(self):
        info = [self.name]
        my_info = [k + ": " + v for k, v in self.info.items()]
        info += my_info
        return info
        
    @manage_method(15, True)    
    def online_presence(self):
	online = [k + ": " + v for k, v in self.online.items()]
        return online

    @manage_method(3, True)
    def idea_of_software(self):
        idea = ["My philosophy is to always think before to code, most of the time the better solution is also the simplest one."]
        idea.append("On the other side the value of an idea is on the realization, there are too many \"Good Ideas but Bad Implementation\"")
        idea.append("I have had the pleasure to work on very well tested code, so I am able to value such important thing as UnitTest")
        idea.append("Finally I tried to be involved in OpenSource, it had taught me most of what I know, and also the value of good documentation.")
        return idea
        
    @manage_method(4)
    def tool_box(self):
	tools = [proficiency + ": " + ", ".join(langs) for proficiency, langs in self.languanges.items()]
	return tools

    @manage_method(5)
    def previous_works(self):
	previous = ["I worked as clojure developer for a very short amount of time at Washington Startup: \"BlueMontains\""]
        previous.append("I ran a touristic shop in Monteriggioni, Italy during the summer 2013")
	return previous

    @manage_method(6)
    def other_experience(self):
        experience = ["I have been an exchange student, AFS, in the USA for the year 2011/2012"]
	experience.append("I was part of the boy scout; I was involved in key club and in swimming and track")
	return experience

    @manage_method(7)
    def show_off(self):
        proud_of = ["The last project I worked on: "]
        proud_of.append("Vaun: http://vaun.bitbucket.org/ html5 app to share picture at your favorite locale, you have fun and the locale get some free ads on facebook. I made it to learn JavaScript, there is no server-side code, only front-end.")
        proud_of.append("gOrge: http://gorgeapp.appspot.com/ I made this host for markdown document to learn GoLang, it is hosted on Google AppEngine.")
        proud_of.append("EchoNest clojure API: https://github.com/siscia/echonest-clojure-api an interface to query EchoNest with clojure.")
	return proud_of

    @manage_method(8)
    def interest(self):
	interests = ["I am very curios about everything, from math to licterature, but what I love the most is software."]
        interests.append("Since I am so curious, I have some theoric knowledge about pretty much everything on the software field (games, distributed system, AI, apps, database, you name it...); however I still lack the practice I would like on some topic.")
	return interests

    @manage_method(9)
    def school(self):
	school = ["High School: 100/100 -> 4.0 GPA"]
        school.append("College (Politecnico di Milano): Still in progress, not real/definitely vote to show yet.")
	return school

    @manage_method(10)
    def is_real(self):
	real = ["Yes, it is a real, python class, it has some simple meta-programming, you can see the source here: https://gist.github.com/siscia/8512255 "]
        real.append("I didn't want to show a piece of paper where I listed my school achievement, I wanted to show that I can code and that I enjoy it.")
        real.append("I think outside the box, I solve problems in the easiest and most efficient way, I design solution for the right problem, that's why my resume is different.")
	return real


lazy()
