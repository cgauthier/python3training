from clear_screen import *
cls()

print("if and else if (elif) statements\n")
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative value changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")