#How import works in Python
import math
a = int(input("Enter number : "))
print(math.sqrt(a))

def func(x):
    a = 0.00000
    b = x
    c = 0.00000
    while a<=b:
        mid = a+(b-a)/2.00000
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            a = mid+1.00000;
            ans = mid;
        else :
            b = mid-1.00000

    return (ans)

print(func(16.00000))

#from keyword : to import particular func()
from math import pi
print(pi) #now dont need to write math.()

#import everything
from math import*
print(sqrt(16))

# as keyword :
from math import floor as m
print(m(10.65654564646))

#dir() : use to see all names of the function and variables of a module
print(dir(math))

#we can import our own modules
from functionsInPython import  greaterNumber as gm
gm(10,11)

print(__name__) #main