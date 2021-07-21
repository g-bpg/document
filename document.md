# /bpg/ - The Beginner Programmer's General
[Thread text available here](https://github.com/g-bpg/document/blob/master/thread.txt).

See [the official document](https://docs.google.com/document/d/1SC8tXlg5p-1SqwwddRdzNv-8MJmQ1WFSMOsMXfT7BNM/edit?usp=sharing). Don't contribute there, contribute here.
[Find a thread on /g/](https://boards.4channel.org/g/bpg) or [view historical threads](https://desuarchive.org/g/search/subject/%2Fbpg%2F/ghost/none/type/op/).
Scroll to the bottom if you want to talk to /bpg/ off of 4chan.

## Table of Contents
[TOC2]

## What is Programming?
At a fundamental level, *programming* is the act of telling your computer to execute instructions to accomplish a task. There are quite a few *sub-fields* within computer science, so knowing what you're interested in will be very helpful:

1. **Graphics** - This covers anything related to drawing things on the screen; there's a bit of overlap in this field between systems here, since both of them require an extensive knowledge of the inner-workings of a machine.
2. **Machine Learning** - Essentially applied statistics, but with extremely large data sets.
3. **Programming Languages** - Studying the semantics of programming languages in general, and analyzing how designs in a language affect different aspects of programs written in it.
4. **Networking** - How to get some data from Point A to Point B
5. **Systems** - How to *implement* much of the groundwork that the rest of CS builds on. Includes things like Operating Systems, Databases, and so on.
6. **Theoretical Computer Science** - This field analyzes models of computation as well as algorithms and data structures.

## So, You Want to Program?
Below are some Intro to Computer Science courses. The important thing is *not* what language they use, or whether one course is better than another. What's important is to just *choose one course and stick with it*.

1. [*Carnegie Mellon University (CMU) - Fundamentals of Computer Science*](https://csd.cmu.edu/course-profiles/15-112-fundamentals-programming-computer-science)
2. [*Harvard CS50 - Intro to Computer Science*](https://online-learning.harvard.edu/course/cs50-introduction-computer-science?delta=0)
3. [*Stanford University CS106A - Programming Methodology*](https://see.stanford.edu/Course/CS106A)
    1. A more up-to-date course is [*here*](http://web.stanford.edu/class/cs106a/) and taught in Python. I *highly recommend* you look at the assignments; they even give you starter code you can dump into PyCharm.

I intentionally give a small list to prevent people from asking *which of these N links is the __best__*. I will reiterate, It doesn't matter. Watch a couple of lectures, and if you seem to follow, keep at it.

### Why don't I just self-learn it?
You can totally do it! But CS is difficult, and having someone to teach you the ropes is great. Think of learning how to drive; you can probably learn by yourself, but having someone explain the basic concepts and what to watch out for is incredibly useful.

Additionally, I've helped teach CS courses, and have seen first-hand how going to lecture and doing homework assignments help. CS is all about practice, so if you're able to follow the lecture and do the assignments, you're on your way to "learning how to program".

### I see people talking about "Rust", "Lisp", "Go", should I be worried about this?
Not at all. These people are talking about other programming languages; they're in their own little world. Ignore them for now. If you *really* want to know what they're talking about, then make sure you have some programming experience under your belt, and begin investigating other programming languages.

What you'll find is that if you have a solid grasp on the fundamentals of CS, then learning other languages shouldn't be *as* difficult; there will of course be some initial learning, but it won't be as difficult as starting from scratch.

#### I disagree with the fact that you're suggesting people use Language X
Good for you.

### I'm Done with the Courses, Now What?
Welcome to the real world! Now find something to program!

You can program something you're interested in, like a small game, or begin reading the codebase of a project you're interested in. If you want to know where to start on a project, ask in /bpg/!

#### Git
One of the most widely used tools, *git* is a version-control system. Its purpose is to help you keep track of the changes you've made to your code. Another way of understanding the utility of version control software is this: How many times have you saved duplicate versions of an assignment "just in case you needed to go back to it", and ended up with a folder of "ASSIGNMENT 5(FINAL) (REVISION) (FINAL) (BEFORE MIDNIGHT) (2).docx"?

Git allows you to specify which files you want to track, and as long as you "commit" your changes, they'll be stored forever, and you'll be able to go back to a previous version at a moment's notice.

If you're going to do any real-world development, I can't stress enough how helpful and ubiquitous this tool is.

Unfortunately, it's also very difficult to learn for many people. Fortunately for you though, many programmers understand that it's difficult to learn *git* and so have made tutorials for it:

1. [*Git Tutorial (General Git concepts / workflow)*](https://git-scm.com/docs/gittutorial)
2. [*Learn Git Branching (What is a Branch, Why is it useful, and How to do it)*](https://learngitbranching.js.org/)
3. [*Git Handbook*](https://guides.github.com/introduction/git-handbook/)

#### Ask other people to review your code
It's very easy to make something that *just works*, but unfortunately this leads to a lot of very difficult to follow code. If possible, have someone read through your code and let them give advice on how to improve it.

Some easy things you should look out for are:

1. Very long functions. You should strive to have a program be a set of relatively short, modular functions. This makes it much easier to spot and debug a problem with your code.
2. Copy+Pasted code. If you find yourself using copy+paste, something's wrong. Much like a math expression, you should try to *factor out* common code into its own function with a couple of parameters, and simply call that function a couple of times instead of having a longer function
3. Comment your code: When you're starting out, write comments to explain what it is you're trying to do. This will often allow anyone reading your code to see whether or not you have an error (such as, if your comment says your code does one thing, but your code does another thing).

### What do I learn after this?
Some things you can begin to look into after the intro courses:

1. **Data Structures and Algorithms** - Learn about a variety of ways to solve problems, and how to build structures that store data in a convenient manner.
    1. [*Introduction to Algorithms - CLRS*](https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf) - Fantastic book
    2. [*Cracking the Coding Interview*](http://libgen.lc/item/index.php?md5=5DAB013ECD7E940841C8C82C623E1315) - More focused on the "Getting a Job" part of Algorithms and Data Structures, but still useful as an occasional reference.
2. **Introduction to Systems** - Learn a low-level language such as C and learn how files are implemented in Unix.
    1. [*The C Programming Language: Kernighan and Ritchie*](https://kremlin.cc/k&r.pdf) - The K&R Book. Teaches you much of the basic syntax of C.
    2. [*The Linux Programming Interface*](http://1.droppdf.com/files/87BCs/the-linux-programming-interface.pdf) - Covers everything you want or need to know about how Linux implements different aspects of the operating system, as well as the interface to access these resources.
3. **Probability and Statistics** - Very useful, since probability is used *everywhere* in CS.
4. **Databases** - Also very useful, allows somewhat easy organization and storage of data.

## I Need Help with X
There isn't a single soul that hasn't asked this question. However, we can't read your mind, so you're going to need to help us help you. Before you ask your question, make sure you inform the thread of:

1. What you're trying to do
2. Where you're having trouble
3. If you've searched for the error already, explain what part you aren't understanding.
4. Post output in a pastebin.

Try to also solve the problem yourself; this will give you experience reading error messages.

## Resources
This section contains a non-comprehensive and non-exhaustive collection of useful resources and tools.

### IDEs
An *IDE* (Integrated Development Environment). It provides everything you need to develop a program, and is generally a very low-friction way to start programming.

1. [*VS Code, General Programming*](https://code.visualstudio.com/)
    1. Most people prefer VS code, since it has quite a large number of plugins for different languages. There are other Language-Specific IDEs you might want to look into.
2. [*Eclipse - Java Programming*](https://www.eclipse.org/downloads/)
3. [*NetBeans - Java Programming*](https://netbeans.apache.org/download/index.html) (More Beginner-Friendly)
4. [*PyCharm, Python Programming*](https://www.jetbrains.com/pycharm/)
    1. If you're a fan of PyCharm, JetBrains provides IDEs for other languages although you might have to pay for them.

### Text Editors
A *text editor* is a more barebones version of an IDE. These are necessarily much more difficult to get started with, so I would suggest holding up on them until you're comfortable programming. Some of the main text editors are

1. *Nano* - A *very* barebones text editor. You can type, you can delete, you can search, and that's about it.
2. *VIM* - *Vi, IMproved* - A more advanced text editor. The main way you edit text is by switching between *modes*. Make sure you follow *vimtutor* before doing anything serious in vim.
    1. Neovim is pretty much the same thing as vim if this confuses you.
3. *Emacs* - *Editor MACroS* - Commonly referred to as a "hackable text editor", Emacs allows you to change how the editor functions. To extend it, all you need to do is write some lisp.
    1. Common frameworks for emacs are *Spacemacs* and *DOOM Emacs*, which provide a bunch of functionality out of the box.

### Databases
A *database* is simply a place to store your data in an organized fashion. They are used for everything from storing login details, to data for storefronts, and much, much more.

1. [*The Manga Guide to Databases*](https://arxius.io/f/d12be045) [](TODO: store in a better place) - "A little bit more than a decade ago the nuked people made a comic book series to explain the basis of difficult concepts in a very simple way." 

### Useful Reading
Some intro books and resources you may find helpful:

1. [*General Resources*](https://wiki.installgentoo.com/wiki/Programming_resources) *(Install Gentoo Wiki)*
2. **Python**
    1. [*The Python 3 Tutorial*](https://docs.python.org/3/tutorial/index.html)
    2. [*Real Python*](https://realpython.com/)
    3. [*Automate the Boring Stuff with Python*](https://automatetheboringstuff.com/)
    4. Learn Python the Hard Way
3. **C**
    1. [The C Programming Language, K&R](https://kremlin.cc/k&r.pdf)
    2. [*Modern C, Jens Gustedt*](https://gforge.inria.fr/frs/download.php/latestfile/5298/ModernC.pdf)
    3. *C Programming: A Modern Approach, K.N King*
4. **C++**
    1. Programming: Principles and Practice Using C++, by Bjarne Stroustrup

Some /g/entoomen put together a torrent containing a "metric fuckton" of books. You can download it [here (file)](https://g.sicp.me/books/gentoomen-library.torrent) or [here (magnet)](magnet:?xt=urn:btih:0bbfaaf5f469a2bd3d762f6942a302f7014a35e9&tr.1=udp://tracker.ccc.de:80&tr.2=udp://tracker.openbittorrent.com:80&tr.3=udp://tracker.opentrackr.org:1337&tr.4=udp://tracker.coppersurfer.tk:6969&tr.5=udp://tracker.leechers-paradise.org:6969&tr.6=udp://zer0day.ch:1337&tr.7=udp://explodie.org:6969).
It most likely has what you're looking for.

## What Language Should I Use for X?
Ah! Fantastic question. Your choice of language influences the design of your program, and vice versa. Luckily due to a property called *Turing Completeness*, if your programming language can simulate a Turing Machine (hint, every mainstream programming language can), then it can do anything any other Turing Complete Language can.

In layman's terms, anything you do in C can be done in Python, and it can be done in Lisp.

If you're asking, "what language is the best for *this application*," then you have some questions to ask yourself:

1. What am I optimizing for?
    1. If you just want something quick and dirty, I recommend *Python*, since its standard library covers basically every use case you can imagine. Use the above *Python Standard Library* tutorial for more
    2. If you want to focus on speed, I recommend that you can compile, such as *Go, C++, or C*. The reason for this is that, in an interpreted language, your computer needs to convert from the source language to machine code on the fly, whereas in a compiled language, the compilation step already does this for you. Compiled programs can be anywhere from 10x to 100x faster than their compiled counterparts.
    1. If you wish to squeeze out every inch of speed, and build stuff from the ground up, use *C++ or C. *These two languages are compiled, but they also have what's called *manual memory management.* In many languages, you create objects, and the run-time environment makes sure they're freed once they won't be used. With C/C++, you need to manually keep track of this, which ends up improving runtime, at the cost of being more difficult to keep track of.
2. Will I be reinventing the wheel?
    1. It's okay that you'll be writing things other people have implemented, but make sure you're aware of this.
    2. For example, in languages like C, you'll probably be implementing basic routines (such as "read a line from a file") very often. Languages like python already provide this and many other abstractions, so you can focus more on getting stuff done.
3. What are the requirements I need to fulfill?
    1. You won't always have a GAMER PC to run your program; sometimes you'll have a board with a microcontroller containing a very small amount of memory. In this case, you want a language that has a very low memory overhead, such as C.

Here's a summary of what language is a *good fit* for a given type of task:

*Task*                                               |*Language* 
--|--
Web Crawler                                          | Python 
Small HTTP Server                                    | Python / Go 
Numerical Computations like Machine Learning         | Python (Numpy + Pandas), or Julia (much newer language) 
Unix Tool Clone, like cat/grep/ls                    | C/C++ 
Games / Anything requiring low latency (like music)  | C/C++ 
Embedded Devices                                     | C/C++ 

### List of Very Commonly Used Programming Languages
Here's a list of programming languages and what they're usually used for. I will reiterate, focus on getting experience with learning how to program before jumping around.

*Language*      | *Good at\...*
-- | --
C               | Embedded / Low-Level optimizations. Very fine-grained control of your computer's resources.
C++             | C-like speed with better abstractions. Game Development.
C\#             | Game / Windows Development
Python / Ruby   | Rapid prototyping and proof-of-concept scripts. "Gluing together" different scripts.
Python (+Numpy) | Data analysis / Machine Learning

### How to Learn a Programming Language
After taking intro-to-CS courses, I found the following to work reasonably effectively when attempting to learn a new programming language:

1. Choose a language you want to learn
2. Look up how to create for/while loops, conditionals, variables, and functions.
    1. If your language doesn't support some of these constructs, figure out how people work around this (For example, languages that don't support looping often *collection-based iteration*, such as *map* or *filter*).
3. Once you do that, make a small program, like a clone of *ls*.

Zed Shaw has a series called [*Learn Code the Hard Way*](https://learncodethehardway.org/) that people seem to like. Currently, [*Python*](https://learncodethehardway.org/python), [*more Python*](http://learncodethehardway.org/more-python/), [*Ruby*](http://learncodethehardway.org/ruby/), [*C*](http://learncodethehardway.org/c/), and [*JavaScript*](http://learncodethehardway.org/javascript/) are available, along with books for [*SQL*](http://learncodethehardway.org/sql/), [*UNIX*](http://learncodethehardway.org/unix/) and [*Regex*](http://learncodethehardway.org/regex/).
He is however a controversial figure and I've read many responses that say that his books are garbage but many other responses say they're good.

#### Project Based Learning
Project Based Learning is also a way to learn a language, where you learn a language by actually building projects. You might not use them, they probably wont look good on a portfolio, but it might just get the job done.

1. [tuvtran's repo on Github](https://github.com/tuvtran/project-based-learning)
2. [karan's repo on Github](https://github.com/karan/Projects)
3. [rby90's repo on Github, specific to C](https://github.com/rby90/Project-Based-Tutorials-in-C)

## Useful Libraries in Language X
### Python
To use a python library, you have to run `import <library>`, or alternatively `from <library> import <something>` which allows you to use whatever you imported without typing `<library>` behind it.

Library Name | Description
-- | --
**The Standard Library**       | Seriously, for almost all of your use cases, the standard library is enough. I will warn though that there are modules in here that you aren't expected to understand as a beginner, such as *subprocess* or *itertools*. Get some experience with the basics before tackling this. [*Python 3.9 Documentation*](https://docs.python.org/3/download.html)
[**Numpy / Scipy**](https://numpy.org/) | General-purpose numerical computation library. The python library is essentially a wrapper around C functions, so you don't actually get the speed penalty you're expecting.
[**Pandas**](https://pandas.pydata.org/)                       | A data processing library. Synergizes very well with numpy.
**curses**                     | Allows you to make a text-user-interface (TUI) in the terminal. Very nice for prototyping.
[**Pillow**](https://pillow.readthedocs.io/en/stable/)         | A *fork* (git term for "we cloned the repo and made it our own") of the Python Image Library (PIL). Provides functionality to read in and manipulate images. Very fun library to use.
[**Matplot lib**](https://matplotlib.org/)                    | Graphing library; Work well with Numpy. Use this if you want to make pretty graphs. A little unintuitive, but it's great practice for reading the documentation.
[**Requests \[Advanced\]**](https://requests.readthedocs.io/en/master/)                     | This library is fantastic for making HTTP requests to servers. This is tagged as \[advanced\] since it assumes you know what HTTP Requests are and how they work.
[**Beautiful Soup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Synergizes very well with *requests*. This is an HTML processing library. You feed it an HTML string or file, and it allows you to walk through the document after parsing it. Very useful for web crawling.

#### Extremely Quick Explanation of Python's Standard Library
"Which parts of the standard library are a *must know*?". Below is a table of different parts of the standard library, as well as a (subjective) assessment of how difficult it is to use/understand each module.

 *Module*   | *Relative Difficulty Level*      | *Description*
-- | -- | --
 *json*     | Easy                      | JSON (JavaScript Object Notation) is a way to serialize data into a common encoding. Its benefits are its flexibility, relatively simple syntax, and human-readability.      
 *string*   | Easy                      | Common string operations
 datetime   | Medium                    | Provides a way to manipulate dates and differences between dates. Incredibly useful 
 *csv*      | Medium                    | CSV Reading/Writing. Not super imperative that you teach yourself this module, but useful to    
 *urllib*   | Medium                    | Provides a simple interface to fetch resources from URLs. Think of it as an easier-to-understand version of the *requests* library.                
 *argparse* | Medium                    | Provides a way of setting up your script such that you can let the user provide input flags such as "\--verbose" or "\--debug"               
 *curses*   | Advanced                  | Allows you to write interfaces such as those in the *htop* or *cmus* applications.          
 *os*       | Advanced                  | Operating System utilities, such as process management, low-level file creation, and miscellaneous error handling. Of particular interest is the *os.path* submodule

### C
Note that any C library can be included by *linking it* with your executable. This usually involves installing the library to your */usr/lib/* folder, and then specifying a path to your library while compiling.

Library Name | Description
-- | --
[*GNU Readline*](https://tiswww.case.edu/php/chet/readline/rltop.html) | For basic text input (what python repl uses)
[*xlib*](https://www.x.org/releases/X11R7.7/doc/libX11/libX11/libX11.html) | Xorg interface (some suckless tools)
[*libarchive*](https://github.com/libarchive/libarchive) | Useful for unzipping / zipping files.
[*curl*](https://curl.se/libcurl/) | Useful for sending requests and analyzing responses. Use this if you want to do networking.

## Okay... But How Do I Solve Problems?
A common question intermediate programmer's have is "*I know how to do Hello World, I know how to read in and write files\... How do I begin working on larger projects? What do I even choose for a larger project?"*

Now that you know the basics of programming, quite a few avenues open up for you: Below are several tips for moving forward to more difficult problems:

1. **Take it One Step at a Time**
    1. Many times, trying to code everything without having a *very* clear idea of what you're doing will lead to you wasting time and having a design that's difficult to work with
    2. Something you should get practice with is making a "Design Document": Describe the goals of your project, and some of the functionality your project should support
2. **Work Backwards**
    1. Oftentimes, it's useful to think about where your current function fits in the larger pipeline. This allows you to analyze what you have left, and what other things you need to do before you make progress.
3. **Understand the underlying concepts before you delve too deeply in a project**
    1. Chances are, you won't be able to debug a graph algorithm without understanding how the graph is represented, or what the algorithm is doing.
    2. Doing some background reading before implementing something can be very useful.

## Onto More Advanced Projects
Many people want to learn how to "program AI" or "How to make a game", so here's a brief section of resources for types of projects. Each section aims to answer things such as "I want to do a project in X\... What are some good beginner resources for it?"

### Artificial Intelligence
As mentioned above, what many people view as "AI" is actually "applied statistics." If you're good at math, and you want to do AI, I recommend you brush up on your probability, statistics, and linear algebra.

Here are some AI-related resources:

1. [*Stanford University - CS 229: Machine Learning*](http://cs229.stanford.edu/syllabus-fall2020.html)
2. [*(Medium) Intro to Machine Learning Concepts*](https://medium.com/machine-learning-in-practice/a-gentle-introduction-to-machine-learning-concepts-cfe710910eb)

### GUI Development
A big question people commonly have is "Writing programs that print in a terminal is fine and all, but when do I get to make something with a *Graphical User Interface*?" Turns out that making a GUI is actually pretty hard, so make sure you're comfortable reading documentation if you're going to follow this route.

Chances are, there are several *GUI* frameworks in your language of choice. Here's a sample platter of a set of popular GUI development libraries for each language:

*Language* | GUI Frameworks
-- | --
**Python** | [*tkinter*](https://docs.python.org/3/library/tkinter.html), based on the *tk *programming language.
           | [*PyGObject*](https://pygobject.readthedocs.io/en/latest/), based on GTK
**C/C++**  | [*Qt*](https://www.qt.io/)
           | [*GTK*](https://www.gtk.org/)
           | [*MiniGUI*](https://minigui.fmsoft.cn/)

### General Scripting
Not nearly as daunting as the other areas in this section, but it still requires a learning curve.

"Scripting" is generally the act of writing a small python or bash program to automate a task you do repeatedly. For example, make a script that runs as a regularly scheduled task that moves all the images in your "Downloads" folder to your "Images" folder, or run a script that sends an HTTP Request to a REST API to get information (4Chan has a REST API you can send HTTP requests to if you want to experiment!)

Scripts are generally small-ish programs that accomplish a task, so they won't really give you experience with writing larger programs, but they are a good way to find your bearings; if you're comfortable scripting, then larger programs won't seem as difficult to you as they once were.

### Systems
My personal favorite. *Systems* is a relatively broad term, but at a bird's eye view, it covers "implementing the dirty parts" of an application. If you go this route, I *highly* recommend you read [*The Linux Programming Interface*](http://1.droppdf.com/files/87BCs/the-linux-programming-interface.pdf). It covers many of the abstractions that Linux provides, and gives you a good way of understanding what happens when you open a file (creates a file descriptor in the file-descriptor table).

Knowing about Systems also allows you to improve the performance of your programs. Specifically, two important aspects about systems involve *multiprocessing* and *multithreading*, as well as the difference between the two (this is covered in TLPI).

### Other Ideas
1. *[Project Euler](https://projecteuler.net/)* - Math problems you can solve via programming. Starts out easy, quickly gets very difficult. (Need an account)
2. *[Advent of Code](https://adventofcode.com)* - Coding advent calendar, you get a new Christmas-themed challenge every day until the 25th. Historical calendars are available. (Need an account on another service, like \>reddit or GitHub.)
3. *[Leetcode](https://leetcode.com/)* - (ripped off of front page) "LeetCode is the best platform to help you enhance your skills, expand your knowledge and prepare for technical interviews."
3. Implement basic Unix coreutils such as *grep*, *ls*, and *cat*

#### Other Resources
1. [Open Source University](https://github.com/ossu). Has a code of conduct, but essentially mimics a collage course.
    1. [OSSU Computer Science](https://github.com/ossu/computer-science)
    2. [OSSU Data Science](https://github.com/ossu/data-science)
2. [Programming, Motherfucker](http://programming-motherfucker.com/become.html) - Written by Zed Shaw, the person behind the *Learn X the Hard Way* series.

*note: What you need to know ends here. If you don't want to contribute or talk to /bpg/ outside of 4chan, there's nothing else to see.*

## Contributing
This document is rough in some places, so if you have an improvement you can submit it to the [Git repository](https://github.com/g-bpg/document).

I read the threads occasionally, so just suggest things there and it might find it's way through to me, or alternatively use the meta channels (see next section for more details).
Or just use GitHub.

**NOTE ON CONTRIBUTING TO THE ORIGINAL GOOGLE DOC:** *Use incognito mode!* No, seriously! Your name might be attributed to the changes you make, so you might dox yourself slightly by giving away your name to everyone.
Also, you shouldn't anyway. The author of that document has since said to just use this instead of his document.

## Talk to /bpg/!
**READ THE RULES FIRST IF YOU INTEND ON JOINING.** It's a 30 second read, you can do it.

The main spot to talk is [on the Discord](https://discord.gg/YfBUDU7GYn) but Matrix and IRC bridges are operated too, but as a warning they are kinda slow and unreliable at times.
It is slow at times, excluding off-topic, but if you ask for help you might get an answer provided you don't feed the trolls.

[Here's the link for the Matrix space.](https://matrix.to/#/!iCmyhLwtzepRiZOYSh:matrix.org?via=matrix.org) Turn on spaces, *or* see the table below.

Bridges are operated, here is the mapping: *All IRC channels are on Rizon.*

**Discord** | **IRC** | **Matrix** | **Note**
--|--|--|--
announcements|N/A|#g-bpg-announcements:matrix.org|I'll work on getting this on IRC eventually.
meta|#/g/bpg/meta|#g-bpg-meta:matrix.org|Discussion regarding /bpg/.
general|#/g/bpg|#g-bpg-general:matrix.org|
off-topic|#/g/bpg/off-topic|#g-bpg-offtopic:matrix.org|Most people are active here but it can be a cesspool at times.
lang-c|#/g/bpg/c|#g-bpg-c:matrix.org|
lang-lisp|#/g/bpg/lisp|#g-bpg-lisp:matrix.org
lang-python|#/g/bpg/python|#gbpg-python:matrix.org|**THE MATRIX ROOM NAME IS NOT A TYPO.**
lang-rust|#/g/bpg/rust|#g-bpg-rust:matrix.org|
lang-shell|#/g/bpg/shell|#g-bpg-shell:matrix.org|

### Da Roolez
It's expected you read this bit before you join any community/channel, but they are *intentionally* kept as *light as possible*.
Punishments range from just a simple message deletion to a ban, if you do manage to break these rules you're doing something very wrong.

- Don't post pornography or NSFW/NSFW content. This isn't /h/.
- Don't post people's dox.
- Don't aggressively shill other communities/channels.
  - This isn't to say you can't do it if it pertains to a discussion. Just don't DM people/spam channels advertising whatever.
- Don't spam.
- Keep things civil. 
- Off-topic discussion belongs in off-topic channels.

## That's all folks!
Congratulations, you have reached the end of the document.

With a little bit of luck and willpower, you will eventually become a programmer and if you wish, even enter the CS field.

Good luck on your journey!
