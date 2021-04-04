# json-memory-comparative

## Problem
Sometime ago, I had to load an huge json file into a Python application.

Then I realized that there is a problem to do it with this programming language, it will consume a lot of memory to do this operation.

In application memory the json was 7 times bigger then on file system.

## Analysis and Results
I wanted to compare this behavior with JS (running with Node), and also find for a solution in Python.

I tried to load the same file both in JS and in Python.

The memory of the json file on filesystem is 18,6MB.

The nodejs application memory, after parsing the json, was 47.92MB.

The Python application memory, after dumping the json, was 133.02MB.

The problem seems to be inside the C json library used in python.


## Workaround
But what if I need to do this stuff with Python?

So, I realized that there is a new library (from community) that could be used for a task like this.

Its name is 'bigjson', and it allow us to parse a json file without keeping it in memory. It basically treats the structured object in a custom way, keeping the json in binary, and parsing it just when a specific property of that object is requested.

In this way, the memory used by the application is just the memory of the json loaded in binary, in my case, just 10.18MB.
