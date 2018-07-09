#!/usr/bin/env python3

'''
$ ./sandwitch.py 
</======\>
#tomates#
--jambon--
~salades~
<\______/>
'''

def pain(func):
    def wrapper():
        print('</======\>')
        func()
        print('<\______/>')
    return wrapper

def ingredients(func):
    def wrapper():
        print('#tomates#')
        func()
        print('~salades~')
    return wrapper

@pain
@ingredients
def sandwitch(nourriture='--jambon--'):
    print(nourriture)

sandwitch()
