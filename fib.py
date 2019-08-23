#!/usr/bin/python

# fibonacci sequence
# give it how many iterations you want to run it

def fib(iterations):
    a,b = 1,1

    for i in range(1,iterations+1):
        print ("%d : %d + %d = %d" % (i,a,b,a+b))
        a,b = b,a+b

fib(25)
