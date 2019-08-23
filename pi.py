#!/usr/bin/python

# calculate the value of pi
# Using the Nilakantha series
# The more iterations, the closer it converges to the real value.

from decimal import *
import math

def piNila(iterations):
    a,b,c = 2,3,4
    pi = Decimal(3)
    term = Decimal(0)
    # account for first iteration, which is only pi = 3
    print ("1 : %.10f" % (pi))
    for i in range(2,iterations+1):
        term = Decimal(4)/(a*b*c)
        if (i%2 == 0):
            # add 
            pi = pi + term
        else:
            # subtract 
            pi = pi - term
        print ("%d : %.10f" % (i,pi))
        a,b,c = a+2,b+2,c+2
    return pi

piNila(50)
# Now print the real value of pi for comparison ... 
print ("pi : %.10f" % (math.pi))
print ("Note that even after 50 iterations, the Nilakantha series is only accurate to 5 decimal places. ")
print ("100 iterations will yield accuracy to 6 decimal places.")
