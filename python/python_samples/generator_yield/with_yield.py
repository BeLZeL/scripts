#!/usr/bin/python

def gen(string):
    for char in string:
        yield char

for char in gen("foobar"):
    print(char)