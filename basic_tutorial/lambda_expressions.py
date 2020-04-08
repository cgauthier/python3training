#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import cls
from custom_lib_funcs import *

cls()

print("\n**** Lambda Expressions  ****\n")


print ("\nSimple lambda example\n")

def make_incrementor(n):
    return lambda x: x + 1

f = make_incrementor(42)

print(f(0))
print(f(1))


print ("\nSorting an array of tuples using a lambda\n")

# this is an array of tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# this uses the sort method
# key is a lambda
# the lambda is pair
# the pair[1] refers to the index of the tuple
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print ("\nSorting an array of tuples using a lambda in reverse order\n")

# this is an array of tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

# this uses the sort method
# key is a lambda
# the lambda is pair
# the pair[1] refers to the index of the tuple
pairs.sort(key=lambda pair: pair[1], reverse=True)
print(pairs)
