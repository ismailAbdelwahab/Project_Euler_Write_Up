#!/usr/bin/env python3
#----------------------------------------------------------------
#  Copyright (c) ABDEL WAHAB Ismail.      Created: June 19 2019				
#   https://github.com/ismailAbdelwahab/Project_Euler_Wrprime_factor_Up	
#----------------------------------------------------------------
#----------------------------------------------------------------
#        7th Problem : https://projecteuler.net/problem=7
#
#  	  Find the 10001st prime number.
#----------------------------------------------------------------
def isPrime(n, list_of_primes): 
	""" Check if n is prime by seeing if n is not a multiple of any previous 
	prime number in "list_of_primes" that is <= to n/2 """
	sup = n/2
	for div in [ x for x in list_of_primes if x <= sup ]:
		if( n % div == 0 ):
			return False
	return True

counter = 1
number = 1 
l_primes = []
while counter != 10001:
	number += 2
	if (isPrime(number, l_primes) ):
		l_primes.append(number)
		counter += 1
		print ("Prime number n°",counter,"found.")

print ("The 10001st prime number is :")
print ("     Prime number = ",number)