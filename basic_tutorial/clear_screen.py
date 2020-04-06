# to clear a terminal screen
# sleep for a minimum of 1 second
# clear

# import only system from os 
from os import system, name 
import math

# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def cls(x = 1): 
    if math.isnan(x) or (not isinstance(x, int)):
        x = 1

    sleep(x)
    clear()