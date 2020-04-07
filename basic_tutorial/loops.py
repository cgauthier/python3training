#importing the clear_screen.py file to use for clearing screen when executing a python script

from clear_screen import cls
from custom_lib_funcs import *

cls()

#Fibonacci series
print("**** WHILE LOOP ****\n")
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

print("**** FOR LOOP ****\n")

print("Simple for statement")

words = ['cat', 'window', 'door']
longLength = longestStrLengthInArray(words)

for w in words:
    print (w.ljust(longLength, ' '), " ", len(w), "characters long")


print("\n**** FOR LOOP in DICTIONARY ****\n")

users = {

    'claude': 'active',
    'tom': 'active',
    'harry': 'inactive',
    'jack': 'active',
    'john': 'active',
    'jimmy': 'inactive'
}

print("Iterate over a copy\n")

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

print("\nCreate a new collection\n")

active_users = {}

for user, status in users.copy().items():
    if status == 'active':
        active_users[user] = status

print(active_users)        

print("\nSimple Range Function\n")

for i in range(3):
    print(i)


print("\nStart and End Range Function\n")

for i in range(3, 6):
    print(i)

print("\nStart and End Range with Step Function\n")

for i in range(3, 13, 3):
    print(i)

print("\nQuick Sum with a range\n")

print(sum(range(10)))


print("\n**** break, continue and else in loops ****\n")

print("\nbreak example in for loop")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0: # modulus operator %
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # no factor found
        print(n, ' is a prime number')

print("\ncontinue example in for loop")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found even number: ", num)
        continue
    print("Found odd number", num)
    # the above work due to the binary logic of num % 2, assuming that with continue, your next number
    # is actually odd


print("\n**** Pass statement ****\n")

print("see code for example of pass\n")

#while True:
 #  pass # busy waiting for keyboard interupt (ctrl-c)

#class myEmptyClass:
#   pass #creates a minimal class

#def initlog(*args):
#   pass # create a place-holder for function or conditional body


print("\n**** Defining Functions ****\n")

