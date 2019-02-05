#!/usr/bin/env python3
# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
'''
x=1, y=2, z=3
x=1, y=2, z=3
x=1, y=2, z=3
'''

def foo(x,y,z):
    print("x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
    
mylist = [1,2,3]
foo(*mylist)

mydict = {'x':1,'y':2,'z':3}
foo(**mydict)

mytuple = (1, 2, 3)
foo(*mytuple)
