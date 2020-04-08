#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import cls
from custom_lib_funcs import *

cls()

print("\n**** Documentation Strings and Function Annotations  ****\n")

print("\n**** Documentation Strings  ****\n")

def my_function():
    """Do nothing but document this

    No, really, this doesn't do anything!
    """
    pass

print(my_function.__doc__);

print("\n**** Function Annotations  ****\n")

def f(ham: str, eggs: str = 'eggs') -> str: 
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
f('spam', "cheese")
