#!/usr/bin/python

def fib(iterations):
    a,b = 1,1

    for i in range(1,iterations+1):
        print "%d : %d + %d = %d" % (i,a,b,a+b)
        a,b = b,a+b

fib(25)
