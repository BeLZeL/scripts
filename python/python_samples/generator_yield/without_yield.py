#!/usr/bin/python

def gen(string):
    result = []
    for char in string:
        result.append(char)
    return result

for char in gen("foobar"):
    print(char)