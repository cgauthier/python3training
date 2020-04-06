#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import *
from custom_lib_funcs import *

cls()

#Fibonacci series
print ("Fibonacci series example using while loop\n")
a, b = 0, 1 #this declares and initialized a with 0 and b with 1
while a < 10:
    print(a)
    a, b = b, a+b #this will set a with the value of b and b with the value of a+b

print("using print and avoid printing a new line with the following while loop\n")    

print ("Fibonacci series example using while loop with a comma to separate the output\n")

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b #this will set a with the value of b and b with the value of a+b

print('\n')
print("Simple for statement")
words = ['cat', 'window', 'door']
longLength = longestStrLengthInArray(words)

for w in words:
    print (w.ljust(longLength, ' '), " ", len(w), "characters long")
