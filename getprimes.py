# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# GetPrimes
# Calculate the first n prime numbers

nprimes = 100
primes = [2]
candidate = primes[-1] + 1

for i in range(2, nprimes+1):
    isPrime = False
    while isPrime == False: 
        isPrime = True
        for j in primes: 
            if candidate % j == 0: 
                isPrime = False
        if isPrime == True: 
            primes.append(candidate)
        candidate = candidate + 1

for n in range(0, nprimes) :
    print (n+1,": ",primes[n])
    