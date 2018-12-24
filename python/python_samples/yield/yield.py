#!/usr/bin/env python3

'''
$ ./yield.py
['H', 'e', 'l', 'l', 'o']
H
e
l
l
o
<generator object gen_yield at 0x7f47a15fb570>
W
o
r
l
d
'''

def gen_classic(string):
    result = []
    for char in string:
        result.append(char)
    return result

def gen_yield(string):
    for char in string:
        yield char

def gen_yield_range(i):
    j=0
    while j < i:
        yield j
        j += 1

res = gen_classic('Hello')
print(res)
for char in res:
    print(char)

res = gen_yield('World')
print(res)
for char in res:
    print(char)

res = gen_yield_range(3)
print(res)
print(res.__next__())
print(res.__next__())
print(res.__next__())
