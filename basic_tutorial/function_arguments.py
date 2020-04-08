#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import cls
from custom_lib_funcs import *

cls()

print("\n**** Function Arguments in Functions  ****\n")

print("Function Arguments Examples\n")

# standard typical function arguments
def standard_arg(arg):
    print(arg)

# positional only arguments
def pos_only_arg(arg, /):
    print(arg)

# keyword only arguments
def kwd_only_arg(*, arg):
    print(arg)

# combining all forms of arguments
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


def multiple_kwd_only_arg(*, arg, arg2, arg3):
    print(arg, "\n", arg2, "\n", arg3)


print("\nUsing a standard function argument\n")

# either pass a value without keyword
standard_arg(1)
# or pass a value with a keyword
standard_arg(arg=2)

print("\nUsing position function argument\n")

# pass a value only by position without keyword
pos_only_arg(2)
            
try:
    # pass a value with keyword will fail
    pos_only_arg(arg=4)
except:
    print("Can't use a keyword as part of the argument\n")


print("\nUsing keyword only function argument\n")

# pass a value with a keyword
kwd_only_arg(arg=4)


try:
    # pass a value only without keyword will fail
    kwd_only_arg(2)
except:
    print("MUST use a keyword as part of the argument\n")


print("\nUsing keyword only function with multiple arguments\n")

multiple_kwd_only_arg(arg3="args do not need to be in order", arg2="world", arg="hello")
    
