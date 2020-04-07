#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import cls
from custom_lib_funcs import *

cls()

print("\n**** Defining Functions  ****\n")

print("with default values arguments\n")

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print('\nyes indeed!')
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print('\nya say no!')
            return False
        retries = retries - 1
        if retries < 0:
                try:
                    raise ValueError
                except ValueError:
                    print("There was an exception")
                    return False
        print(reminder)

ask_ok("Please enter a yes or no answer: ")

print("\ndealing with scope\n")

i = 10
def f(arg = i):
    print(arg)

i = 20
f()
f(i)

# in the above expect f() to print i because it was defined prior and as such became the default argument, when none is invoked

print("\nlists are passed by reference, so you will see how we keep appending to L\n")

def mutableDemoFunction(y, L=[]):
    L.append(y)
    return L

print(mutableDemoFunction(1))
print(mutableDemoFunction(2))
print(mutableDemoFunction(3))

print("\nIf you wish for an argument not to be initialized\n")

def nonInitArgFunc(y, L=None):
    if L is None:
        L = []
    L.append(y)
    return L

print(nonInitArgFunc(1))
print(nonInitArgFunc(2))
print(nonInitArgFunc(3))

print("\nPassing a tuple \n")
# a tuple is a list but its immutable, so think of it as a list of constants

def passTupleArgFunc(str, *args):
    print(str)
    for arg in args:
        print(arg)

passTupleArgFunc('foo', 1, 2, 3, 4, 5)

print("\nPassing a dictionary \n")
# a tuple is a list but its immutable, so think of it as a list of constants

def passDictArgFunc(str, **json):
    print(str)
    for j in json:
        print(j, json[j])

passDictArgFunc('json', foo="bar", super="hero", cold="case")

