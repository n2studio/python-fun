#!/usr/bin/python

def fib(iterations):
    a,b = 1,1
    c=0
    for i in range(1,iterations+1):
        c=a+b
        print "%d : %d + %d = %d" % (i,a,b,c)
        a=b
        b=c

fib(25)
